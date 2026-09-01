(function () {
  "use strict";

  const PAGE_SIZE = 25;
  const KIND_LABELS = {
    paths: "Complete paths",
    headings: "Index headings",
    locators: "Locator assessments",
    cross_references: "Cross-references",
    source_subjects: "Source subjects"
  };

  const state = {
    projection: null,
    collections: new Map(),
    activeView: "primary",
    activeKind: null,
    query: "",
    band: "all",
    page: 1,
    loadingKind: null
  };

  const byId = (id) => document.getElementById(id);

  function node(tag, className, text) {
    const element = document.createElement(tag);
    if (className) element.className = className;
    if (text !== undefined && text !== null) element.textContent = String(text);
    return element;
  }

  function titleCase(value) {
    return String(value)
      .replace(/_/g, " ")
      .replace(/\b\w/g, (letter) => letter.toUpperCase());
  }

  function compactNumber(value, maximumFractionDigits = 2) {
    const number = Number(value);
    if (!Number.isFinite(number)) return String(value);
    return new Intl.NumberFormat("en", { maximumFractionDigits }).format(number);
  }

  function percentage(value) {
    const number = Number(value);
    if (!Number.isFinite(number)) return String(value);
    return new Intl.NumberFormat("en", {
      style: "percent",
      minimumFractionDigits: 1,
      maximumFractionDigits: 1
    }).format(number);
  }

  function shortHash(value) {
    return `${String(value).slice(0, 12)}…${String(value).slice(-8)}`;
  }

  function renderSummary() {
    const projection = state.projection;
    byId("reportTitle").textContent = projection.title;
    byId("reportSubtitle").textContent = projection.subtitle;
    byId("canonicalScore").textContent = compactNumber(projection.primary_view.score, 1);
    byId("canonicalLabel").textContent = projection.primary_view.performance_label;
    byId("adjustedScore").textContent = compactNumber(projection.secondary_view.score, 1);
    byId("adjustedLabel").textContent = projection.secondary_view.label;
    byId("adjustedNote").textContent = "Secondary · representation assumptions only";
    byId("counterfactualDescription").textContent = projection.secondary_view.description;
    byId("projectionIdentity").textContent = `${projection.projection_id} · ${shortHash(projection.projection_sha256)}`;
    byId("footerIdentity").textContent = `${projection.schema_version} · ${projection.projection_id}`;
  }

  function componentValue(component) {
    const candidates = [
      ["normalized_value", "normalized"],
      ["rounded_rating", "rating"],
      ["score", "score"],
      ["observed_value", "observed"],
      ["raw_numerator", "numerator"]
    ];
    for (const [key, label] of candidates) {
      if (component[key] !== undefined && component[key] !== null) {
        return `${label}: ${compactNumber(component[key], 4)}`;
      }
    }
    return component.measurement_status || "structured result";
  }

  function renderDimensions() {
    const projection = state.projection;
    const view = state.activeView === "primary" ? projection.primary_view : projection.secondary_view;
    const grid = byId("dimensionGrid");
    grid.replaceChildren();

    view.dimensions.forEach((dimension, index) => {
      const card = node("article", "dimension-card");
      const top = node("div", "dimension-topline");
      const nameBlock = node("div");
      nameBlock.append(
        node("p", "dimension-index", `Q${String(index + 1).padStart(2, "0")} · ${dimension.label}`),
        node("h3", "", dimension.question)
      );
      const score = node("div", "dimension-score");
      score.append(
        node("strong", "", `${compactNumber(dimension.awarded_points, 2)} / ${compactNumber(dimension.maximum_points, 2)}`),
        node("span", "", `${compactNumber(dimension.rating, 4)} of 5`)
      );
      top.append(nameBlock, score);
      card.append(top, node("p", "dimension-description", dimension.description));

      const track = node("div", "rating-track");
      track.setAttribute("aria-label", `${dimension.rating} out of 5`);
      const fill = node("div", "rating-fill");
      fill.style.width = `${Math.max(0, Math.min(100, Number(dimension.rating) * 20))}%`;
      track.append(fill);
      card.append(track);

      const meta = node("div", "dimension-meta");
      meta.append(node("span", "meta-chip", titleCase(dimension.status)));
      if (dimension.applied_cap) {
        meta.append(node("span", "meta-chip", `Applied cap · ${dimension.applied_cap.cap_id}`));
      } else {
        meta.append(node("span", "meta-chip", "No applied cap"));
      }
      meta.append(node("span", "meta-chip", `${dimension.components.length} component${dimension.components.length === 1 ? "" : "s"}`));
      card.append(meta);

      const details = node("details", "dimension-details");
      details.append(node("summary", "", "Components, cap checks, and formula ID"));
      const components = node("ul", "component-list");
      dimension.components.forEach((component) => {
        const row = node("li");
        row.append(
          node("code", "", component.component_id || "component"),
          node("span", "", componentValue(component))
        );
        components.append(row);
      });
      const formula = node("li");
      formula.append(node("code", "", "formula"), node("span", "", dimension.formula_id));
      components.append(formula);
      const caps = node("li");
      caps.append(
        node("code", "", "cap checks"),
        node("span", "", `${dimension.cap_evaluations.length} evaluated`)
      );
      components.append(caps);
      details.append(components);
      card.append(details);
      grid.append(card);
    });
  }

  function renderGates() {
    const gateStatus = state.projection.gate_status;
    byId("gateEffect").textContent = gateStatus.effect;

    const totals = byId("gateTotals");
    totals.replaceChildren();
    Object.entries(gateStatus.counts).forEach(([status, count]) => {
      const card = node("div", "gate-total");
      card.append(node("strong", "", count), node("span", "", status));
      totals.append(card);
    });

    const list = byId("gateList");
    list.replaceChildren();
    gateStatus.gates.forEach((gate) => {
      const card = node("details", "gate-card");
      const summary = node("summary", "gate-summary");
      summary.append(
        node("span", `gate-icon ${gate.status}`, ""),
        node("span", "gate-name", gate.description),
        node("span", "gate-status", gate.status)
      );
      const body = node("div", "gate-body");
      body.append(node("p", "", gate.finding));
      if (gate.evidence_ids && gate.evidence_ids.length) {
        body.append(node("p", "evidence-line", `Evidence: ${gate.evidence_ids.join(", ")}`));
      }
      card.append(summary, body);
      list.append(card);
    });
  }

  function renderMetrics() {
    const metrics = state.projection.key_metrics;
    const density = metrics.density;
    const values = [
      ["Weighted locator precision", percentage(metrics.weighted_locator_precision), "Frozen two-axis locator credit"],
      ["Strict substantive precision", percentage(metrics.strict_substantive_precision), "Full substantive treatment"],
      ["Expected-treatment recall", percentage(metrics.expected_treatment_recall), "Frozen expected-treatment set"],
      ["Weighted F1", percentage(metrics.weighted_f1), "Precision–recall balance"],
      ["Assessable locators", compactNumber(metrics.assessable_locator_count, 0), "Complete locator ledger"],
      ["Density-fit rating", `${compactNumber(density.rounded_rating, 2)} / 5`, density.details.profile_id],
      ["Treatment categories", compactNumber(Object.keys(metrics.counts_by_treatment_tier).length, 0), "Frozen treatment tiers"],
      ["Fit categories", compactNumber(Object.keys(metrics.counts_by_fit_tier).length, 0), "Frozen complete-path fit tiers"]
    ];
    const grid = byId("metricGrid");
    grid.replaceChildren();
    values.forEach(([label, value, note]) => {
      const card = node("article", "metric-card");
      card.append(node("p", "metric-label", label), node("strong", "", value), node("span", "", note));
      grid.append(card);
    });
  }

  function legendLabel(entry) {
    if (entry.minimum_score === null) return `${titleCase(entry.band)} · no score`;
    return `${titleCase(entry.band)} · ${entry.minimum_score}+`;
  }

  function renderGradeLegend() {
    const itemGrades = state.projection.item_grades;
    const legend = byId("gradeLegend");
    const filter = byId("gradeFilter");
    legend.replaceChildren();
    filter.replaceChildren(new Option("All bands", "all"));
    itemGrades.color_legend.forEach((entry) => {
      const item = node("span", `legend-item ${entry.color_token}`);
      item.append(node("span", "legend-swatch", ""), node("span", "", legendLabel(entry)));
      legend.append(item);
      filter.append(new Option(titleCase(entry.band), entry.band));
    });
    byId("gradeDisclosure").textContent = itemGrades.disclosure;
  }

  function renderBrowserTabs() {
    const bindings = state.projection.item_grades.collections;
    const tabs = byId("browserTabs");
    tabs.replaceChildren();
    bindings.forEach((binding) => {
      const button = node("button", "browser-tab");
      button.type = "button";
      button.role = "tab";
      button.dataset.kind = binding.item_kind;
      button.setAttribute("aria-selected", String(binding.item_kind === state.activeKind));
      if (binding.item_kind === state.activeKind) button.classList.add("is-active");
      button.append(
        document.createTextNode(KIND_LABELS[binding.item_kind]),
        node("span", "tab-count", compactNumber(binding.count, 0))
      );
      button.addEventListener("click", () => selectKind(binding.item_kind));
      tabs.append(button);
    });
  }

  function collectionBinding(kind) {
    return state.projection.item_grades.collections.find((entry) => entry.item_kind === kind);
  }

  async function loadCollection(kind) {
    if (state.collections.has(kind)) return state.collections.get(kind);
    state.loadingKind = kind;
    byId("browserStatus").textContent = `Loading ${KIND_LABELS[kind].toLowerCase()}…`;
    const binding = collectionBinding(kind);
    if (!binding) throw new Error(`No collection binding for ${kind}.`);
    const response = await fetch(binding.artifact_path, { cache: "no-store" });
    if (!response.ok) throw new Error(`Unable to load ${binding.artifact_path} (${response.status}).`);
    const collection = await response.json();
    if (
      collection.schema_version !== binding.schema_version ||
      collection.collection_sha256 !== binding.collection_sha256 ||
      collection.count !== binding.count ||
      collection.item_kind !== kind
    ) {
      throw new Error(`Collection binding mismatch for ${kind}.`);
    }
    state.collections.set(kind, collection);
    state.loadingKind = null;
    return collection;
  }

  async function selectKind(kind) {
    state.activeKind = kind;
    state.page = 1;
    state.query = "";
    state.band = "all";
    byId("itemSearch").value = "";
    byId("gradeFilter").value = "all";
    byId("itemSearch").disabled = false;
    byId("gradeFilter").disabled = false;
    renderBrowserTabs();
    try {
      await loadCollection(kind);
      renderItems();
    } catch (error) {
      renderBrowserError(error);
    }
  }

  function matchingItems(collection) {
    const query = state.query.trim().toLocaleLowerCase("en");
    return collection.items.filter((item) => {
      if (state.band !== "all" && item.grade.band !== state.band) return false;
      if (!query) return true;
      const searchable = [
        item.item_id,
        item.label,
        item.summary,
        item.grade_scope,
        ...(item.evidence_ids || []),
        ...Object.values(item.detail || {}).flatMap((value) =>
          Array.isArray(value) ? value.map(String) : [String(value)]
        )
      ].join(" ").toLocaleLowerCase("en");
      return searchable.includes(query);
    });
  }

  function gradeBadge(grade) {
    return node("span", `grade-badge ${grade.color_token}`, titleCase(grade.band));
  }

  function renderItems() {
    const collection = state.collections.get(state.activeKind);
    if (!collection) return;
    const items = matchingItems(collection);
    const pages = Math.max(1, Math.ceil(items.length / PAGE_SIZE));
    state.page = Math.min(state.page, pages);
    const start = (state.page - 1) * PAGE_SIZE;
    const pageItems = items.slice(start, start + PAGE_SIZE);

    byId("browserStatus").textContent = `${compactNumber(items.length, 0)} of ${compactNumber(collection.count, 0)} records · authoritative order retained`;
    const list = byId("itemList");
    list.replaceChildren();
    if (!pageItems.length) {
      list.append(node("p", "empty-state", "No records match this search and grade filter."));
    } else {
      pageItems.forEach((item) => {
        const row = node("button", "item-row");
        row.type = "button";
        row.setAttribute("aria-label", `Open ${item.item_id}: ${item.label}`);
        const label = node("span", "item-label");
        label.append(node("strong", "", item.label), node("code", "", item.item_id));
        const grade = gradeBadge(item.grade);
        const score = node("span", "item-score", item.grade.score === null ? "—" : compactNumber(item.grade.score, 2));
        const scoreWrap = node("span");
        scoreWrap.append(score, node("span", "row-arrow", " ›"));
        row.append(label, grade, scoreWrap);
        row.addEventListener("click", () => openItem(item));
        list.append(row);
      });
    }
    renderPagination(items.length, pages);
  }

  function renderPagination(total, pages) {
    const pagination = byId("pagination");
    pagination.replaceChildren();
    const previous = node("button", "", "Previous");
    previous.type = "button";
    previous.disabled = state.page <= 1;
    previous.addEventListener("click", () => {
      state.page -= 1;
      renderItems();
      byId("itemList").focus();
    });
    const next = node("button", "", "Next");
    next.type = "button";
    next.disabled = state.page >= pages;
    next.addEventListener("click", () => {
      state.page += 1;
      renderItems();
      byId("itemList").focus();
    });
    const start = total ? (state.page - 1) * PAGE_SIZE + 1 : 0;
    const end = Math.min(state.page * PAGE_SIZE, total);
    pagination.append(previous, node("span", "", `${start}–${end} · page ${state.page} of ${pages}`), next);
  }

  function renderBrowserError(error) {
    state.loadingKind = null;
    byId("browserStatus").textContent = "Supporting detail could not be loaded.";
    byId("itemList").replaceChildren(node("p", "empty-state", error.message));
    byId("pagination").replaceChildren();
  }

  function displayValue(value) {
    if (value === null) return "Not measured";
    if (Array.isArray(value)) return value.length ? value.map(displayValue).join(", ") : "None";
    if (typeof value === "object") return JSON.stringify(value);
    if (typeof value === "boolean") return value ? "Yes" : "No";
    return String(value);
  }

  function openItem(item) {
    const dialog = byId("itemDialog");
    byId("dialogKind").textContent = `${titleCase(item.item_kind)} · ${item.item_id}`;
    byId("dialogTitle").textContent = item.label;
    const body = byId("dialogBody");
    body.replaceChildren();
    body.append(node("p", "dialog-summary", item.summary));

    const meta = node("div", "dialog-meta");
    meta.append(gradeBadge(item.grade));
    meta.append(node("span", "meta-chip", item.grade.score === null ? "Not measured" : `${compactNumber(item.grade.score, 2)} / 100`));
    meta.append(node("span", "meta-chip", item.grade_scope));
    if (item.confidence !== null && item.confidence !== undefined) {
      meta.append(node("span", "meta-chip", `Confidence · ${item.confidence}`));
    }
    body.append(meta);

    if (item.factors.length) {
      const section = node("section", "dialog-section");
      section.append(node("h3", "", "Component results and factors"));
      item.factors.forEach((factor) => {
        const card = node("article", "factor-card");
        const heading = node("h3", "", factor.label || factor.factor_id);
        if (factor.score !== null && factor.score !== undefined) {
          heading.append(node("span", "factor-score", compactNumber(factor.score, 2)));
        }
        card.append(heading);
        if (factor.status) card.append(node("p", "", `Status: ${titleCase(factor.status)}`));
        if (factor.explanation) card.append(node("p", "", factor.explanation));
        if (factor.severity_caps && factor.severity_caps.length) {
          factor.severity_caps.forEach((cap) => {
            const capText = [
              cap.defect_id,
              cap.severity ? `severity ${cap.severity}` : null,
              cap.maximum_score !== undefined ? `maximum ${cap.maximum_score}` : null
            ].filter(Boolean).join(" · ");
            card.append(node("p", "factor-cap", `Severity cap: ${capText}`));
          });
        }
        if (factor.applied_cap !== null && factor.applied_cap !== undefined) {
          card.append(node("p", "factor-cap", `Applied maximum: ${factor.applied_cap}`));
        }
        if (factor.evidence_ids && factor.evidence_ids.length) {
          card.append(node("p", "evidence-line", `Evidence: ${factor.evidence_ids.join(", ")}`));
        }
        section.append(card);
      });
      body.append(section);
    }

    const details = node("section", "dialog-section");
    details.append(node("h3", "", "Stable relationships and assessment fields"));
    const table = node("table", "detail-table");
    const tableBody = node("tbody");
    Object.entries(item.detail).forEach(([key, value]) => {
      const row = node("tr");
      row.append(node("th", "", titleCase(key)), node("td", "", displayValue(value)));
      tableBody.append(row);
    });
    table.append(tableBody);
    details.append(table);
    body.append(details);

    if (item.evidence_ids.length) {
      const evidence = node("section", "dialog-section");
      evidence.append(
        node("h3", "", "Scoped evidence identifiers"),
        node("p", "evidence-line", item.evidence_ids.join(", "))
      );
      body.append(evidence);
    }
    document.body.classList.add("dialog-open");
    dialog.showModal();
  }

  function closeDialog() {
    const dialog = byId("itemDialog");
    if (dialog.open) dialog.close();
    document.body.classList.remove("dialog-open");
  }

  function renderMethod() {
    const disclosure = state.projection.calculation_disclosure;
    const cards = [
      ["Independent locator axes", disclosure.treatment_and_complete_path_fit_are_independent ? "Treatment and complete-path fit remain independent." : ""],
      ["Page-reference Reliability", disclosure.page_reference_reliability_source],
      ["Gates and caps", disclosure.dimension_gates_and_caps],
      ["Aggregate score", disclosure.aggregate_score_source],
      ["Diagnostic item grades", disclosure.diagnostic_grades_used_in_dimension_arithmetic ? "Used in dimension arithmetic." : "Display diagnostics are not substituted into dimension arithmetic."],
      ["Displayed locator", disclosure.displayed_locator_language]
    ];
    const grid = byId("methodGrid");
    grid.replaceChildren();
    cards.forEach(([heading, copy]) => {
      const card = node("article", "method-card");
      card.append(node("h3", "", heading), node("p", "", copy));
      grid.append(card);
    });
  }

  function renderProvenance() {
    const projection = state.projection;
    const repositories = byId("repositoryCards");
    repositories.replaceChildren();
    Object.entries(projection.repositories).forEach(([name, repository]) => {
      const card = node("article", "repo-card");
      card.append(node("h3", "", name), node("div", "", repository.repository));
      card.append(node("code", "", repository.commit));
      const link = node("a", "", "Open pinned revision ↗");
      link.href = repository.url;
      link.target = "_blank";
      link.rel = "noreferrer";
      card.append(link);
      if (repository.tool_identity) card.append(node("code", "", `Tool: ${repository.tool_identity}`));
      repositories.append(card);
    });

    const bindings = byId("artifactBindings");
    bindings.replaceChildren();
    projection.provenance.source_artifacts.forEach((binding) => {
      const row = node("div", "binding-row");
      row.append(node("strong", "", titleCase(binding.role)));
      const pathLink = node("a", "", binding.artifact_path);
      pathLink.href = binding.github_url;
      pathLink.target = "_blank";
      pathLink.rel = "noreferrer";
      row.append(pathLink, node("code", "hash", shortHash(binding.sha256)));
      bindings.append(row);
    });

    const contract = byId("projectionContract");
    contract.replaceChildren();
    const fields = [
      ["Projection ID", projection.projection_id],
      ["Projection self-hash", projection.projection_sha256],
      ["Schema", projection.schema_version],
      ["Builder", `${projection.builder.builder_id} @ ${projection.builder.version}`],
      ["Builder source", `${projection.builder.source.artifact_path} · ${projection.builder.source.sha256}`],
      ["Creation command", projection.builder.command],
      ["Ordering", projection.builder.ordering_rules.join("; ")],
      ["Migration", `${projection.provenance.migration_id} · ${projection.provenance.migration_sha256}`],
      ["Validation receipt", `${projection.provenance.validation_receipt_id} · ${projection.provenance.validation_receipt_sha256}`]
    ];
    fields.forEach(([term, description]) => {
      contract.append(node("dt", "", term), node("dd", "", description));
    });
  }

  function renderLimitations() {
    const list = byId("limitationsList");
    list.replaceChildren();
    state.projection.limitations.forEach((limitation) => list.append(node("li", "", limitation)));
  }

  function bindControls() {
    document.querySelectorAll("[data-view]").forEach((button) => {
      button.addEventListener("click", () => {
        state.activeView = button.dataset.view;
        document.querySelectorAll("[data-view]").forEach((candidate) => {
          const active = candidate === button;
          candidate.classList.toggle("is-active", active);
          candidate.setAttribute("aria-pressed", String(active));
        });
        renderDimensions();
      });
    });

    let searchTimer;
    byId("itemSearch").addEventListener("input", (event) => {
      window.clearTimeout(searchTimer);
      searchTimer = window.setTimeout(() => {
        state.query = event.target.value;
        state.page = 1;
        renderItems();
      }, 120);
    });
    byId("gradeFilter").addEventListener("change", (event) => {
      state.band = event.target.value;
      state.page = 1;
      renderItems();
    });
    byId("dialogClose").addEventListener("click", closeDialog);
    byId("itemDialog").addEventListener("close", () => document.body.classList.remove("dialog-open"));
    byId("itemDialog").addEventListener("click", (event) => {
      if (event.target === byId("itemDialog")) closeDialog();
    });
  }

  async function initialize() {
    try {
      const response = await fetch("projection.v1.json", { cache: "no-store" });
      if (!response.ok) throw new Error(`Unable to load projection.v1.json (${response.status}).`);
      const projection = await response.json();
      if (
        projection.schema_version !== "oxford-published-index-web-projection-v1" ||
        projection.projection_role !== "deterministic_display_only_projection" ||
        projection.primary_view.view_id !== "canonical_as_delivered" ||
        projection.secondary_view.view_id !== "representation_adjusted" ||
        projection.secondary_view.role !== "secondary_counterfactual_representation_view"
      ) {
        throw new Error("Projection identity or primary/secondary view binding is invalid.");
      }
      state.projection = projection;
      renderSummary();
      renderDimensions();
      renderGates();
      renderMetrics();
      renderGradeLegend();
      renderBrowserTabs();
      renderMethod();
      renderProvenance();
      renderLimitations();
      bindControls();
      byId("itemSearch").disabled = true;
      byId("gradeFilter").disabled = true;
      byId("dataState").textContent = "Verified projection loaded";
      byId("dataState").classList.add("is-ready");
    } catch (error) {
      byId("dataState").textContent = "Projection unavailable";
      const message = node("div", "fatal-error", `The bound projection could not be rendered: ${error.message}`);
      message.setAttribute("role", "alert");
      document.body.append(message);
    }
  }

  initialize();
})();
