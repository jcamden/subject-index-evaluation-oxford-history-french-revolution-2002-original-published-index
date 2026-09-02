#!/usr/bin/env python3
"""Build and validate the public V7 Oxford customer web projection.

This renderer is deliberately evaluation-local. It projects already-public,
frozen V7 artifacts into a static, progressively disclosed presentation. It
does not calculate scores, change judgments, or read restricted inputs.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
from copy import deepcopy
from decimal import Decimal
from pathlib import Path
from typing import Any, Iterable, Mapping

try:
    import jsonschema
    from referencing import Registry, Resource
except ImportError as exc:  # pragma: no cover - exercised by CLI users
    raise SystemExit(
        "jsonschema>=4 and referencing are required; install the pinned "
        "methodology requirements first."
    ) from exc


PROJECTION_SCHEMA_VERSION = "oxford-published-index-web-projection-v1"
ITEM_COLLECTION_SCHEMA_VERSION = "oxford-published-index-item-collection-v1"
BUILDER_ID = "oxford-v7-published-index-web-builder-v1"
BUILDER_VERSION = "1.0.0"
ORDERING_RULE = "ITEM-PROJECTION-DEFECT-ID-ASC-V1"

EVALUATION_REPOSITORY = "publication-intelligence/ohfr-2002-esi"
METHODOLOGY_REPOSITORY = "publication-intelligence/evaluate-subject-index"
BENCHMARK_REPOSITORY = "publication-intelligence/ohfr-2002-esi-benchmark"

EVALUATION_BASE_COMMIT = "b0b201b0641ea2bec7b27c40ccc8f4c74d22c880"
METHODOLOGY_COMMIT = "df9112d036105213da74a4cc8f8f3f2a3ad26784"
BENCHMARK_HEAD_COMMIT = "435679329cecd5facbead2b837380a8a9b9f697b"
METHODOLOGY_TOOL_IDENTITY = "dimension-score-cli-v7.0.6"

EXPECTED_CANONICAL_SCORE = Decimal("72.5")
EXPECTED_ADJUSTED_SCORE = Decimal("73.5")
EXPECTED_CANONICAL_UNRESOLVED = 312
EXPECTED_ADJUSTED_UNRESOLVED = 308
EXPECTED_CANONICAL_UNRESOLVED_HASH = (
    "c4a48defa2429a6589a52958e41d44939b83d7f54d2750c4d94bd1d40c0451f6"
)
EXPECTED_ADJUSTED_UNRESOLVED_HASH = (
    "9dc3aa84eb218865d3e347314473a0f1415512e5e334aa451c1787e3abefcfa9"
)
EXPECTED_MIGRATION_SELF_HASH = (
    "ad204595ced753f17f4eec8b16de8038ab39d16edfa19ae7479e43851a9ddc09"
)
EXPECTED_RECEIPT_SELF_HASH = (
    "d437433ab45b662457ed81b56438103040b8430219901e40897b5e31e2c51203"
)

PACKAGE_RELATIVE = Path("web/v7-published-index")
ASSET_NAMES = (
    "README.md",
    "index.html",
    "app.js",
    "styles.css",
    "projection.schema.json",
    "item-collection.schema.json",
)
COLLECTION_FILES = {
    "paths": "data/paths.v1.json",
    "headings": "data/headings.v1.json",
    "locators": "data/locators.v1.json",
    "cross_references": "data/cross-references.v1.json",
    "source_subjects": "data/source-subjects.v1.json",
}

SCHEMA_FILES = {
    "subject-index-web-report-v6": "web-report-v6.schema.json",
    "subject-index-evaluation-result-v8": "evaluation-result-v8.schema.json",
    "subject-index-item-assessments-v4": "item-assessments-v4.schema.json",
    "subject-index-dimension-calculations-v3": "dimension-calculations-v3.schema.json",
    "subject-index-v7-projection-metadata-v1": "v7-projection-metadata.schema.json",
    "subject-index-score-migration-v6-to-v7-v1": "score-migration-v6-to-v7.schema.json",
    "subject-index-score-migration-v6-to-v7-validation-v1": (
        "score-migration-v6-to-v7-validation.schema.json"
    ),
    "subject-index-structure-locator-review-v1": "structure-locator-review-v1.schema.json",
    "subject-index-v7-locator-fit-supplement-v1": "v7-locator-fit-supplement.schema.json",
    "subject-index-v7-architecture-review-supplement-v1": (
        "v7-architecture-review-supplement.schema.json"
    ),
    "subject-index-v6-to-v7-migration-input-v1": "v7-migration-input.schema.json",
    "subject-index-dimension-calculations-v2": "dimension-calculations-v2.schema.json",
    "subject-index-evaluation-result-v7": "evaluation-result-v7.schema.json",
    "subject-index-item-assessments-v3": "item-assessments-v3.schema.json",
    "subject-index-web-report-v5": "web-report-v5.schema.json",
    "subject-index-v6-projection-metadata-v1": "v6-projection-metadata.schema.json",
}

AUTHORITATIVE_ARTIFACTS = {
    "canonical_calculation": "candidate/v7-migration/dimension-calculations.v7.json",
    "canonical_result": "candidate/v7-migration/evaluation-result.v7.json",
    "canonical_items": "candidate/v7-migration/item-assessments.v7.json",
    "projection_metadata": "candidate/v7-migration/projection-metadata.v7.json",
    "migration_record": "candidate/v7-migration/score-migration.v6-to-v7.json",
    "canonical_structure_review": "candidate/v7-migration/structure-locator-review.v7.json",
    "validation_receipt": "candidate/v7-migration/validation-receipt.v7.json",
    "canonical_web_report": "candidate/v7-migration/web-report.v7.json",
    "adjusted_calculation": (
        "candidate/v7-migration/score-views/"
        "representation_adjusted.dimension-calculations.v7.json"
    ),
    "adjusted_structure_review": (
        "candidate/v7-migration/score-views/"
        "representation_adjusted.structure-locator-review.v7.json"
    ),
    "canonical_locator_fit_supplement": (
        "candidate/v7-migration-inputs/locator-fit-supplement.canonical.v7.json"
    ),
    "adjusted_locator_fit_supplement": (
        "candidate/v7-migration-inputs/"
        "locator-fit-supplement.representation-adjusted.v7.json"
    ),
    "canonical_architecture_supplement": (
        "candidate/v7-migration-inputs/"
        "supplemental-architecture-review.canonical.v7.json"
    ),
    "adjusted_architecture_supplement": (
        "candidate/v7-migration-inputs/"
        "supplemental-architecture-review.representation-adjusted.v7.json"
    ),
    "migration_input": "candidate/migration-input.v6-to-v7.json",
    "v6_calculation": "candidate/v6-migration/dimension-calculations.v6.json",
    "v6_result": "candidate/v6-migration/evaluation-result.v7.json",
    "v6_items": "candidate/v6-migration/item-assessments.v3.json",
    "v6_web_report": "candidate/v6-migration/web-report.v5.json",
    "v6_projection_metadata": "candidate/v6-migration/projection-metadata.v6.json",
    "representation_correction_ledger": (
        "candidate/representation-adjustment/correction-causal-ledger.v1.json"
    ),
    "representation_fidelity_audit": (
        "candidate/representation-adjustment/character-fidelity-audit.v1.json"
    ),
    "representation_validation_receipt": (
        "validation/representation-adjustment-validation-receipt.v1.json"
    ),
}

SELF_HASH_FIELDS = {
    "canonical_calculation": "calculation_sha256",
    "projection_metadata": "projection_metadata_sha256",
    "migration_record": "migration_sha256",
    "canonical_structure_review": "review_sha256",
    "validation_receipt": "receipt_sha256",
    "adjusted_calculation": "calculation_sha256",
    "adjusted_structure_review": "review_sha256",
    "canonical_locator_fit_supplement": "supplement_sha256",
    "adjusted_locator_fit_supplement": "supplement_sha256",
    "canonical_architecture_supplement": "supplement_sha256",
    "adjusted_architecture_supplement": "supplement_sha256",
    "v6_calculation": "calculation_sha256",
}

DIMENSION_COPY = {
    "meaningful_coverage": {
        "question": "Does the index cover the source’s meaningful subjects?",
        "description": (
            "Measures access to principal and important subsidiary subjects, "
            "relationships, distinctions, arguments, findings, and conclusions."
        ),
    },
    "editorial_selectivity": {
        "question": "Does it select useful entries rather than incidental mentions?",
        "description": (
            "Measures substantive selectivity and the separately limited "
            "chapter-level density-fit contribution."
        ),
    },
    "conceptual_stance_fidelity": {
        "question": "Do headings preserve concepts, relationships, and stance?",
        "description": (
            "Measures whether headings preserve meaning, scope, distinctions, "
            "chronology, relationships, and authorial stance."
        ),
    },
    "page_reference_reliability": {
        "question": "Do page references reliably lead to relevant treatment?",
        "description": (
            "Measures two-axis locator precision and expected-treatment recall "
            "using the frozen V7 calculation ledger."
        ),
    },
    "findability_navigation": {
        "question": "Can readers find subjects through clear access routes?",
        "description": (
            "Measures terminology, hierarchy, direct access, subdivisions, "
            "cross-references, and whole-index navigation."
        ),
    },
    "mechanics_consistency": {
        "question": "Is the index mechanically consistent?",
        "description": (
            "Measures locator validity and order, hierarchy depth, unique paths, "
            "reference mechanics, naming, and professional consistency."
        ),
    },
}


class ProjectionError(RuntimeError):
    """Fail-closed projection build or validation error."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ProjectionError(message)


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_json(path: Path, *, decimal: bool = False) -> dict[str, Any]:
    try:
        text = path.read_text(encoding="utf-8")
        value = json.loads(text, parse_float=Decimal) if decimal else json.loads(text)
    except FileNotFoundError as exc:
        raise ProjectionError(f"Required artifact is missing: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ProjectionError(f"Invalid JSON at {path}: {exc}") from exc
    require(isinstance(value, dict), f"JSON artifact must be an object: {path}")
    return value


def canonical_json_text(value: Any) -> str:
    if value is None:
        return "null"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if isinstance(value, str):
        return json.dumps(value, ensure_ascii=False)
    if isinstance(value, int):
        return str(value)
    if isinstance(value, Decimal):
        require(value.is_finite(), "Canonical JSON cannot contain a non-finite decimal.")
        return format(value, "f")
    if isinstance(value, float):
        decimal = Decimal(str(value))
        require(decimal.is_finite(), "Canonical JSON cannot contain a non-finite float.")
        return format(decimal, "f")
    if isinstance(value, list):
        return "[" + ",".join(canonical_json_text(item) for item in value) + "]"
    if isinstance(value, dict):
        require(
            all(isinstance(key, str) for key in value),
            "Canonical JSON object keys must be strings.",
        )
        return "{" + ",".join(
            f"{json.dumps(key, ensure_ascii=False)}:{canonical_json_text(value[key])}"
            for key in sorted(value)
        ) + "}"
    raise ProjectionError(f"Unsupported canonical JSON value: {type(value).__name__}")


def canonical_hash(value: Mapping[str, Any], excluded_field: str) -> str:
    clone = deepcopy(dict(value))
    clone.pop(excluded_field, None)
    return sha256_bytes(canonical_json_text(clone).encode("utf-8"))


def canonical_json_line_hash(value: Mapping[str, Any], excluded_field: str) -> str:
    """Reconstruct the structure-review script's frozen JSON-line hash profile."""
    clone = deepcopy(dict(value))
    clone.pop(excluded_field, None)
    payload = (
        json.dumps(clone, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        + "\n"
    ).encode("utf-8")
    return sha256_bytes(payload)


def decimal_value(value: Any) -> Decimal:
    return value if isinstance(value, Decimal) else Decimal(str(value))


def run_git(root: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        ["git", "-C", str(root), *args],
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if check and result.returncode:
        raise ProjectionError(
            f"git {' '.join(args)} failed in {root}: {result.stderr.strip()}"
        )
    return result


def verify_git_binding(root: Path, expected: str, *, allow_descendant: bool) -> None:
    require((root / ".git").exists(), f"Expected Git repository: {root}")
    head = run_git(root, "rev-parse", "HEAD").stdout.strip()
    if allow_descendant:
        ancestor = run_git(
            root, "merge-base", "--is-ancestor", expected, head, check=False
        )
        require(
            ancestor.returncode == 0,
            f"Repository HEAD {head} does not descend from required commit {expected}.",
        )
    else:
        require(head == expected, f"Repository HEAD {head} != required commit {expected}.")


def schema_registry(schema_root: Path) -> Registry:
    registry = Registry()
    for path in sorted(schema_root.glob("*.schema.json")):
        document = load_json(path, decimal=True)
        resource = Resource.from_contents(document)
        registry = registry.with_resource(path.resolve().as_uri(), resource)
        registry = registry.with_resource(path.name, resource)
    return registry


def validate_schema(
    document: dict[str, Any], schema_path: Path, registry: Registry, label: str
) -> None:
    schema = load_json(schema_path, decimal=True)
    errors = sorted(
        jsonschema.Draft202012Validator(schema, registry=registry).iter_errors(document),
        key=lambda item: list(item.absolute_path),
    )
    if errors:
        first = errors[0]
        location = ".".join(map(str, first.absolute_path)) or "<root>"
        raise ProjectionError(
            f"{label} fails {schema_path.name} at {location}: {first.message} "
            f"({len(errors)} error(s))."
        )


def resolve_inside(root: Path, path: Path, *, label: str) -> Path:
    resolved_root = root.resolve()
    resolved = path.resolve()
    require(
        resolved == resolved_root or resolved_root in resolved.parents,
        f"{label} escapes the repository root: {path}",
    )
    return resolved


def verify_artifact_reference(
    repository_root: Path, parent_path: Path, reference: Mapping[str, Any], label: str
) -> Path:
    require(isinstance(reference.get("artifact_path"), str), f"{label} has no artifact_path.")
    require(isinstance(reference.get("sha256"), str), f"{label} has no sha256.")
    target = resolve_inside(
        repository_root,
        parent_path.parent / str(reference["artifact_path"]),
        label=label,
    )
    require(target.is_file(), f"{label} does not resolve to a public file: {target}")
    actual = sha256_file(target)
    require(actual == reference["sha256"], f"{label} SHA-256 mismatch: {target}")
    document = load_json(target)
    if reference.get("schema_version"):
        require(
            document.get("schema_version") == reference["schema_version"],
            f"{label} schema identity mismatch: {target}",
        )
    return target


def artifact_github_url(path: str) -> str:
    return (
        f"https://github.com/{EVALUATION_REPOSITORY}/blob/"
        f"{EVALUATION_BASE_COMMIT}/{path}"
    )


def self_hash_reference(document: Mapping[str, Any], field: str) -> dict[str, str]:
    return {"field": field, "value": str(document[field])}


def source_binding(
    repository_root: Path,
    role: str,
    path_text: str,
    document: Mapping[str, Any],
    self_hash_field: str | None,
) -> dict[str, Any]:
    path = repository_root / path_text
    binding: dict[str, Any] = {
        "role": role,
        "artifact_path": path_text,
        "schema_version": str(document.get("schema_version", "evaluation-local-public-contract")),
        "sha256": sha256_file(path),
        "size_bytes": path.stat().st_size,
        "github_url": artifact_github_url(path_text),
    }
    if self_hash_field:
        binding["self_hash"] = self_hash_reference(document, self_hash_field)
    return binding


def verify_defect_order(items: Mapping[str, Any]) -> None:
    families = (
        "path_assessments",
        "heading_node_assessments",
        "cross_reference_assessments",
    )
    for family in families:
        for record in items[family]:
            record_evidence = record.get("evidence_ids", [])
            require(
                len(record_evidence) == len(set(record_evidence)),
                f"Duplicate record evidence identity in {family}.",
            )
            factors = {
                factor["factor_id"]: factor
                for factor in record.get("popover", {}).get("factors", [])
            }
            for factor in factors.values():
                caps = factor.get("severity_caps", [])
                cap_ids = [cap["defect_id"] for cap in caps]
                evidence_ids = factor.get("evidence_ids", [])
                require(
                    cap_ids == sorted(set(cap_ids)),
                    f"{ORDERING_RULE} popover-cap violation in {family}.",
                )
                require(
                    set(cap_ids).issubset(evidence_ids),
                    f"Defect-derived popover evidence is incomplete in {family}.",
                )
                require(
                    len(evidence_ids) == len(set(evidence_ids)),
                    f"Duplicate popover evidence identity in {family}.",
                )
            for container in record.get("component_results", []):
                caps = container.get("severity_caps", [])
                cap_ids = [cap["defect_id"] for cap in caps]
                require(
                    cap_ids == sorted(set(cap_ids)),
                    f"{ORDERING_RULE} violation in {record.get(family[:-12] + '_id', family)}.",
                )
                evidence_ids = container.get("evidence_ids", [])
                require(
                    set(cap_ids).issubset(evidence_ids),
                    f"Defect-derived component evidence is incomplete in {family}.",
                )
                factor = factors.get(container["dimension_id"])
                require(factor is not None, f"Missing popover factor in {family}.")
                require(
                    factor.get("severity_caps", []) == caps,
                    f"Component/popover cap mismatch in {family}.",
                )
                require(
                    factor.get("evidence_ids", []) == evidence_ids,
                    f"Component/popover evidence mismatch in {family}.",
                )


def validate_item_relationships(items: Mapping[str, Any]) -> None:
    locators = {item["locator_id"] for item in items["locator_assessments"]}
    paths = {item["path_id"] for item in items["path_assessments"]}
    nodes = {item["node_id"] for item in items["heading_node_assessments"]}
    references = {
        item["reference_id"] for item in items["cross_reference_assessments"]
    }
    subjects = {item["subject_id"] for item in items["source_subject_assessments"]}
    expected_lengths = {
        "locators": (locators, items["locator_assessments"]),
        "paths": (paths, items["path_assessments"]),
        "heading_nodes": (nodes, items["heading_node_assessments"]),
        "cross_references": (references, items["cross_reference_assessments"]),
        "source_subjects": (subjects, items["source_subject_assessments"]),
    }
    for family, (identities, records) in expected_lengths.items():
        require(len(identities) == len(records), f"Duplicate stable IDs in {family}.")
        completeness = items["assessment_completeness"][family]
        require(completeness["complete"] is True, f"Incomplete item family: {family}.")
        require(completeness["assessed"] == len(records), f"Count drift in {family}.")

    for locator in items["locator_assessments"]:
        require(locator["path_id"] in paths, f"Unknown path for {locator['locator_id']}.")
        require(set(locator["node_ids"]).issubset(nodes), f"Unknown node for {locator['locator_id']}.")
    for path in items["path_assessments"]:
        require(set(path["locator_ids"]).issubset(locators), f"Unknown locator for {path['path_id']}.")
        require(set(path["node_ids"]).issubset(nodes), f"Unknown node for {path['path_id']}.")
        require(set(path["reference_ids"]).issubset(references), f"Unknown reference for {path['path_id']}.")
        require(set(path["matched_subject_ids"]).issubset(subjects), f"Unknown subject for {path['path_id']}.")
    for node in items["heading_node_assessments"]:
        require(set(node["path_ids"]).issubset(paths), f"Unknown path for {node['node_id']}.")
        if node["parent_node_id"] is not None:
            require(node["parent_node_id"] in nodes, f"Unknown parent for {node['node_id']}.")


def validate_locator_grades(
    calculation: Mapping[str, Any], items: Mapping[str, Any]
) -> None:
    reliability = next(
        row
        for row in calculation["dimensions"]
        if row["dimension_id"] == "page_reference_reliability"
    )["reliability_provenance"]
    rows = {
        row["locator_id"]: row
        for row in reliability["locator_utility_assignments"]
    }
    require(len(rows) == len(items["locator_assessments"]), "Locator ledger count drift.")
    for assessment in items["locator_assessments"]:
        locator_id = assessment["locator_id"]
        require(locator_id in rows, f"Missing calculation row for {locator_id}.")
        row = rows[locator_id]
        require(
            assessment["locator_utility"] == row,
            f"Item/calculation locator utility mismatch for {locator_id}.",
        )
        expected_grade = decimal_value(row["combined_credit"]) * Decimal(100)
        require(
            decimal_value(assessment["grade"]["score"]) == expected_grade,
            f"Locator grade does not equal 100 × L for {locator_id}.",
        )
        require(
            decimal_value(row["diagnostic_grade"]) == expected_grade,
            f"Calculation diagnostic grade mismatch for {locator_id}.",
        )


def validate_color_legend(items: Mapping[str, Any]) -> None:
    legend = items["color_legend"]
    measured = [row for row in legend if row["minimum_score"] is not None]
    measured.sort(key=lambda row: Decimal(str(row["minimum_score"])), reverse=True)
    for family in (
        "locator_assessments",
        "path_assessments",
        "heading_node_assessments",
        "cross_reference_assessments",
        "source_subject_assessments",
    ):
        for item in items[family]:
            grade = item["grade"]
            if grade["score"] is None:
                require(
                    grade["color_token"] == "grade_neutral",
                    f"Null grade uses failure color in {family}.",
                )
                continue
            score = Decimal(str(grade["score"]))
            expected = next(
                row["color_token"]
                for row in measured
                if score >= Decimal(str(row["minimum_score"]))
            )
            require(
                grade["color_token"] == expected,
                f"Grade color drift in {family}: {item.get('locator_id') or item.get('path_id') or item.get('node_id') or item.get('reference_id') or item.get('subject_id')}.",
            )


def verify_receipt_bindings(repository_root: Path, receipt_path: Path, receipt: Mapping[str, Any]) -> None:
    references: list[tuple[str, Mapping[str, Any]]] = [("migration", receipt["migration"])]
    references.extend(
        (f"active.{name}", value)
        for name, value in receipt["active_projections"].items()
    )
    references.extend(
        (f"historical.{name}", value)
        for name, value in receipt["historical_projections"].items()
    )
    for index, view in enumerate(receipt["counterfactual_projections"]):
        references.append((f"counterfactual[{index}].calculation", view["calculation"]))
        references.append(
            (f"counterfactual[{index}].structure", view["structure_locator_review"])
        )
    for family in (
        "supplemental_architecture_reviews",
        "supplemental_locator_fit_supplements",
    ):
        for index, item in enumerate(receipt.get(family, [])):
            references.append((f"{family}[{index}]", item["artifact"]))
    for label, reference in references:
        verify_artifact_reference(repository_root, receipt_path, reference, label)


def verify_web_bindings(repository_root: Path, web_path: Path, web: Mapping[str, Any]) -> None:
    references: list[tuple[str, Mapping[str, Any]]] = [
        ("web.calculation", web["calculation_explainer"]),
        ("web.structure", web["structure_locator_review"]),
        ("web.items", web["item_grade_index"]),
        ("web.migration", web["migration_comparison"]["migration_record"]),
    ]
    for index, view in enumerate(web["score_views"]["views"]):
        references.append((f"web.view[{index}].calculation", view["calculation"]))
        references.append((f"web.view[{index}].structure", view["structure_locator_review"]))
        if view.get("locator_fit_supplement"):
            references.append((f"web.view[{index}].fit", view["locator_fit_supplement"]))
        for p_index, provenance in enumerate(view.get("provenance_artifacts", [])):
            references.append((f"web.view[{index}].provenance[{p_index}]", provenance))
    for label, reference in references:
        verify_artifact_reference(repository_root, web_path, reference, label)


def validate_authoritative_state(
    repository_root: Path, methodology_root: Path, benchmark_root: Path
) -> dict[str, dict[str, Any]]:
    verify_git_binding(repository_root, EVALUATION_BASE_COMMIT, allow_descendant=True)
    verify_git_binding(methodology_root, METHODOLOGY_COMMIT, allow_descendant=False)
    verify_git_binding(benchmark_root, BENCHMARK_HEAD_COMMIT, allow_descendant=False)

    schema_root = methodology_root / "evaluate-subject-index/references/schemas"
    require(schema_root.is_dir(), f"Methodology schema directory is missing: {schema_root}")
    registry = schema_registry(schema_root)

    documents: dict[str, dict[str, Any]] = {}
    decimal_documents: dict[str, dict[str, Any]] = {}
    for role, path_text in AUTHORITATIVE_ARTIFACTS.items():
        path = repository_root / path_text
        documents[role] = load_json(path)
        decimal_documents[role] = load_json(path, decimal=True)
        schema_version = documents[role].get("schema_version")
        if schema_version in SCHEMA_FILES:
            validate_schema(
                decimal_documents[role],
                schema_root / SCHEMA_FILES[str(schema_version)],
                registry,
                role,
            )

    structure_hash_roles = {"canonical_structure_review", "adjusted_structure_review"}
    for role, field in SELF_HASH_FIELDS.items():
        document = documents[role] if role in structure_hash_roles else decimal_documents[role]
        require(field in document, f"{role} is missing {field}.")
        reconstructed = (
            canonical_json_line_hash(document, field)
            if role in structure_hash_roles
            else canonical_hash(document, field)
        )
        require(
            reconstructed == document[field],
            f"{role} has an invalid reconstructable self-hash.",
        )

    migration = documents["migration_record"]
    receipt = documents["validation_receipt"]
    web = documents["canonical_web_report"]
    result = documents["canonical_result"]
    calculation = documents["canonical_calculation"]
    adjusted = documents["adjusted_calculation"]
    items = documents["canonical_items"]

    require(
        migration["tool"]["version"] == METHODOLOGY_TOOL_IDENTITY,
        "Methodology tool identity mismatch.",
    )
    require(
        migration["migration_sha256"] == EXPECTED_MIGRATION_SELF_HASH,
        "Migration self-hash regression mismatch.",
    )
    require(
        receipt["receipt_sha256"] == EXPECTED_RECEIPT_SELF_HASH,
        "Validation-receipt self-hash regression mismatch.",
    )
    require(
        all(value is True for value in receipt["validation"].values()),
        "The final V7 validation receipt does not pass every check.",
    )
    verify_receipt_bindings(
        repository_root,
        repository_root / AUTHORITATIVE_ARTIFACTS["validation_receipt"],
        receipt,
    )
    verify_web_bindings(
        repository_root,
        repository_root / AUTHORITATIVE_ARTIFACTS["canonical_web_report"],
        web,
    )

    require(decimal_value(calculation["total_score"]) == EXPECTED_CANONICAL_SCORE, "Canonical calculation score mismatch.")
    require(decimal_value(result["total_score"]) == EXPECTED_CANONICAL_SCORE, "Canonical result score mismatch.")
    require(decimal_value(web["grade"]["score"]) == EXPECTED_CANONICAL_SCORE, "Canonical web score mismatch.")
    require(decimal_value(adjusted["total_score"]) == EXPECTED_ADJUSTED_SCORE, "Adjusted calculation score mismatch.")

    views = {view["view_id"]: view for view in web["score_views"]["views"]}
    require(web["score_views"]["primary_view_id"] == "canonical_as_delivered", "Canonical view is not primary.")
    require(views["canonical_as_delivered"]["view_kind"] == "observed", "Canonical view is not observed.")
    require(views["representation_adjusted"]["view_kind"] == "counterfactual", "Adjusted view is not counterfactual.")
    require(decimal_value(views["representation_adjusted"]["score"]) == EXPECTED_ADJUSTED_SCORE, "Adjusted web score mismatch.")

    calculation_dimensions = {row["dimension_id"]: row for row in calculation["dimensions"]}
    result_dimensions = {row["dimension_id"]: row for row in result["scorecard"]}
    web_dimensions = {row["dimension_id"]: row for row in web["scorecard"]}
    require(list(web_dimensions) == list(DIMENSION_COPY), "Unexpected V7 dimension order or identity.")
    require(set(calculation_dimensions) == set(DIMENSION_COPY), "Canonical calculation dimensions mismatch.")
    require(set(result_dimensions) == set(DIMENSION_COPY), "Canonical result dimensions mismatch.")
    for dimension_id in DIMENSION_COPY:
        calc = calculation_dimensions[dimension_id]
        projected = web_dimensions[dimension_id]
        result_row = result_dimensions[dimension_id]
        require(projected["rating"] == calc["final_rating"], f"Web rating drift for {dimension_id}.")
        require(projected["awarded_points"] == calc["awarded_points"], f"Web points drift for {dimension_id}.")
        require(result_row["rating"] == calc["final_rating"], f"Result rating drift for {dimension_id}.")
        require(result_row["points"] == calc["awarded_points"], f"Result points drift for {dimension_id}.")

    canonical_gates = calculation["publication_readiness_gates"]
    adjusted_gates = adjusted["publication_readiness_gates"]
    require(canonical_gates == adjusted_gates, "Canonical and adjusted gate payloads differ.")
    require(
        web["gate_status"]["critical_gates"] == result["critical_gates"],
        "Web/result gate payloads differ.",
    )
    require(web["gate_status"]["used_in_score_arithmetic"] is False, "Gates entered score arithmetic.")

    supplementation = {row["view_id"]: row for row in migration["locator_fit_supplementation"]["views"]}
    expected = {
        "canonical_as_delivered": (
            EXPECTED_CANONICAL_UNRESOLVED,
            EXPECTED_CANONICAL_UNRESOLVED_HASH,
        ),
        "representation_adjusted": (
            EXPECTED_ADJUSTED_UNRESOLVED,
            EXPECTED_ADJUSTED_UNRESOLVED_HASH,
        ),
    }
    for view_id, (count, set_hash) in expected.items():
        view = supplementation[view_id]
        require(view["unresolved_set_count_before_supplementation"] == count, f"{view_id} unresolved count mismatch.")
        require(view["unresolved_set_count_after_supplementation"] == 0, f"{view_id} final unresolved count is nonzero.")
        require(view["unresolved_set_sha256"] == set_hash, f"{view_id} unresolved-set hash mismatch.")
        require(view["preflight_group_counts"]["invalid_or_contradictory_state"] == 0, f"{view_id} contains invalid/contradictory states.")

    supplement_expectations = {
        "canonical_locator_fit_supplement": {"exact_fit": 309, "no_fit": 3},
        "adjusted_locator_fit_supplement": {"exact_fit": 306, "no_fit": 2},
    }
    for role, expected_counts in supplement_expectations.items():
        counts: dict[str, int] = {}
        for decision in documents[role]["decisions"]:
            counts[decision["fit_category"]] = counts.get(decision["fit_category"], 0) + 1
        require(counts == expected_counts, f"{role} decision-count regression mismatch.")

    validate_item_relationships(items)
    validate_locator_grades(calculation, items)
    validate_color_legend(items)
    verify_defect_order(items)
    return documents


def projection_dimension(
    dimension: Mapping[str, Any], label: str
) -> dict[str, Any]:
    dimension_id = str(dimension["dimension_id"])
    copy = DIMENSION_COPY[dimension_id]
    return {
        "dimension_id": dimension_id,
        "label": label,
        "question": copy["question"],
        "description": copy["description"],
        "rating": dimension["final_rating"],
        "rating_maximum": 5,
        "awarded_points": dimension["awarded_points"],
        "maximum_points": dimension["dimension_weight"],
        "status": dimension["status"],
        "formula_id": dimension["formula_id"],
        "components": deepcopy(dimension.get("components", [])),
        "applied_cap": deepcopy(dimension.get("applied_cap")),
        "cap_evaluations": deepcopy(dimension.get("cap_evaluations", [])),
        "rounding": deepcopy(dimension.get("rounding")),
        "gate_relationship": "separate_claim_restrictions_shown_in_gate_section",
    }


def item_record(
    kind: str,
    source_order: int,
    item_id: str,
    label: str,
    source: Mapping[str, Any],
    detail: Mapping[str, Any],
) -> dict[str, Any]:
    popover = source["popover"]
    return {
        "item_id": item_id,
        "item_kind": kind,
        "source_order": source_order,
        "label": label,
        "grade": deepcopy(source["grade"]),
        "grade_scope": source["grade_scope"],
        "summary": popover["summary"],
        "confidence": source.get("confidence"),
        "factors": deepcopy(popover["factors"]),
        "evidence_ids": deepcopy(popover["evidence_ids"]),
        "navigation": deepcopy(popover["navigation"]),
        "detail": deepcopy(dict(detail)),
    }


def build_collections(items: Mapping[str, Any], source_sha256: str) -> dict[str, dict[str, Any]]:
    path_titles = {
        row["path_id"]: row["popover"]["title"]
        for row in items["path_assessments"]
    }
    records: dict[str, list[dict[str, Any]]] = {key: [] for key in COLLECTION_FILES}

    for index, row in enumerate(items["path_assessments"]):
        detail = {
            "record_id": row["record_id"],
            "record_type": row["record_type"],
            "heading_path": row["heading_path"],
            "node_ids": row["node_ids"],
            "locator_ids": row["locator_ids"],
            "reference_ids": row["reference_ids"],
            "defect_ids": row["defect_ids"],
            "matched_subject_ids": row["matched_subject_ids"],
        }
        if "locator_string_review" in row:
            detail["locator_string_review"] = row["locator_string_review"]
        records["paths"].append(
            item_record("path", index, row["path_id"], row["popover"]["title"], row, detail)
        )

    for index, row in enumerate(items["heading_node_assessments"]):
        detail = {
            "level": row["level"],
            "role": row["role"],
            "heading_path": row["heading_path"],
            "parent_node_id": row["parent_node_id"],
            "path_ids": row["path_ids"],
            "record_ids": row["record_ids"],
            "direct_path_ids": row["direct_path_ids"],
        }
        records["headings"].append(
            item_record("heading", index, row["node_id"], row["label"], row, detail)
        )

    for index, row in enumerate(items["locator_assessments"]):
        path_label = path_titles[row["path_id"]]
        label = f"{path_label} — p. {row['source_page_label']}"
        detail = {
            "path_id": row["path_id"],
            "node_ids": row["node_ids"],
            "source_page_label": row["source_page_label"],
            "document_page": row["document_page"],
            "mapping_status": row["mapping_status"],
            "judgment": row["judgment"],
            "treatment_class": row["treatment_class"],
            "source_scope_status": row["source_scope_status"],
            "severity": row["severity"],
            "locator_utility": row["locator_utility"],
        }
        records["locators"].append(
            item_record("locator", index, row["locator_id"], label, row, detail)
        )

    for index, row in enumerate(items["cross_reference_assessments"]):
        detail = {
            "record_id": row["record_id"],
            "source_path_id": row["source_path_id"],
            "source_node_id": row["source_node_id"],
            "reference_type": row["reference_type"],
            "target_display": row["target_display"],
            "target_path_id": row["target_path_id"],
            "judgment": row["judgment"],
        }
        records["cross_references"].append(
            item_record(
                "cross_reference",
                index,
                row["reference_id"],
                row["popover"]["title"],
                row,
                detail,
            )
        )

    for index, row in enumerate(items["source_subject_assessments"]):
        detail = {
            "priority": row["priority"],
            "coverage": row["coverage"],
            "matched_path_ids": row["matched_path_ids"],
            "missed_document_pages": row["missed_document_pages"],
            "severity": row["severity"],
        }
        records["source_subjects"].append(
            item_record(
                "source_subject",
                index,
                row["subject_id"],
                row["popover"]["title"],
                row,
                detail,
            )
        )

    collections: dict[str, dict[str, Any]] = {}
    for kind, values in records.items():
        seed = canonical_json_text(
            {
                "schema_version": ITEM_COLLECTION_SCHEMA_VERSION,
                "item_kind": kind,
                "source_sha256": source_sha256,
                "count": len(values),
                "ordering": "authoritative_source_array_order",
            }
        )
        collection = {
            "schema_version": ITEM_COLLECTION_SCHEMA_VERSION,
            "collection_id": f"COLL-{kind.upper()}-{sha256_bytes(seed.encode('utf-8'))[:12].upper()}",
            "item_kind": kind,
            "source_artifact": {
                "artifact_path": AUTHORITATIVE_ARTIFACTS["canonical_items"],
                "sha256": source_sha256,
                "schema_version": "subject-index-item-assessments-v4",
            },
            "ordering": {
                "record_order": "authoritative_source_array_order",
                "defect_derived_arrays": ORDERING_RULE,
                "rhetorical_reordering": False,
            },
            "count": len(values),
            "items": values,
        }
        collection["collection_sha256"] = canonical_hash(collection, "collection_sha256")
        collections[kind] = collection
    return collections


def write_json(path: Path, value: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def write_collection(path: Path, value: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    ordered_keys = (
        "schema_version",
        "collection_id",
        "item_kind",
        "source_artifact",
        "ordering",
        "count",
        "items",
        "collection_sha256",
    )
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write("{\n")
        for key_index, key in enumerate(ordered_keys):
            prefix = f"  {json.dumps(key)}: "
            if key == "items":
                handle.write(prefix + "[\n")
                values = value["items"]
                for index, item in enumerate(values):
                    suffix = "," if index + 1 < len(values) else ""
                    handle.write(
                        "    "
                        + json.dumps(
                            item,
                            ensure_ascii=False,
                            sort_keys=True,
                            separators=(",", ":"),
                        )
                        + suffix
                        + "\n"
                    )
                handle.write("  ]")
            else:
                handle.write(
                    prefix
                    + json.dumps(value[key], ensure_ascii=False, sort_keys=True)
                )
            handle.write("," if key_index + 1 < len(ordered_keys) else "")
            handle.write("\n")
        handle.write("}\n")


def build_projection(
    repository_root: Path,
    methodology_root: Path,
    benchmark_root: Path,
    output_directory: Path,
) -> dict[str, Any]:
    documents = validate_authoritative_state(
        repository_root, methodology_root, benchmark_root
    )
    web = documents["canonical_web_report"]
    calculation = documents["canonical_calculation"]
    adjusted = documents["adjusted_calculation"]
    migration = documents["migration_record"]
    receipt = documents["validation_receipt"]
    items = documents["canonical_items"]

    package_root = repository_root / PACKAGE_RELATIVE
    output_resolved = output_directory.resolve()
    package_resolved = package_root.resolve()
    if output_resolved != package_resolved:
        require(
            not output_directory.exists() or not any(output_directory.iterdir()),
            f"Clean output directory required: {output_directory}",
        )
        output_directory.mkdir(parents=True, exist_ok=True)
        for name in ASSET_NAMES:
            source = package_root / name
            require(source.is_file(), f"Projection renderer asset is missing: {source}")
            shutil.copyfile(source, output_directory / name)
    else:
        for name in ASSET_NAMES:
            require((package_root / name).is_file(), f"Projection renderer asset is missing: {name}")

    item_source_sha = sha256_file(repository_root / AUTHORITATIVE_ARTIFACTS["canonical_items"])
    collections = build_collections(items, item_source_sha)
    collection_bindings: list[dict[str, Any]] = []
    for kind, relative in COLLECTION_FILES.items():
        target = output_directory / relative
        write_collection(target, collections[kind])
        collection_bindings.append(
            {
                "item_kind": kind,
                "artifact_path": relative,
                "schema_version": ITEM_COLLECTION_SCHEMA_VERSION,
                "sha256": sha256_file(target),
                "collection_sha256": collections[kind]["collection_sha256"],
                "count": collections[kind]["count"],
                "ordering": "authoritative_source_array_order",
            }
        )

    source_bindings = []
    for role, path_text in AUTHORITATIVE_ARTIFACTS.items():
        source_bindings.append(
            source_binding(
                repository_root,
                role,
                path_text,
                documents[role],
                SELF_HASH_FIELDS.get(role),
            )
        )

    web_scorecard = {row["dimension_id"]: row for row in web["scorecard"]}
    canonical_dimensions = [
        projection_dimension(row, web_scorecard[row["dimension_id"]]["label"])
        for row in calculation["dimensions"]
    ]
    adjusted_dimensions = [
        projection_dimension(row, web_scorecard[row["dimension_id"]]["label"])
        for row in adjusted["dimensions"]
    ]

    web_views = {view["view_id"]: view for view in web["score_views"]["views"]}
    canonical_view = web_views["canonical_as_delivered"]
    adjusted_view = web_views["representation_adjusted"]
    gates = web["gate_status"]["critical_gates"]
    gate_counts: dict[str, int] = {}
    for gate in gates:
        gate_counts[gate["status"]] = gate_counts.get(gate["status"], 0) + 1

    reliability = next(
        row
        for row in calculation["dimensions"]
        if row["dimension_id"] == "page_reference_reliability"
    )["reliability_provenance"]
    selectivity = next(
        row
        for row in calculation["dimensions"]
        if row["dimension_id"] == "editorial_selectivity"
    )
    density_component = next(
        row for row in selectivity["components"] if row["component_id"] == "density_fit"
    )

    projection_seed = {
        "schema_version": PROJECTION_SCHEMA_VERSION,
        "builder_id": BUILDER_ID,
        "builder_version": BUILDER_VERSION,
        "evaluation_commit": EVALUATION_BASE_COMMIT,
        "methodology_commit": METHODOLOGY_COMMIT,
        "benchmark_commit": BENCHMARK_HEAD_COMMIT,
        "source_hashes": [binding["sha256"] for binding in source_bindings],
    }
    projection_id = (
        "OXFORD-V7-PUBLISHED-WEB-"
        + sha256_bytes(canonical_json_text(projection_seed).encode("utf-8"))[:12].upper()
    )

    methodology_url = (
        f"https://github.com/{METHODOLOGY_REPOSITORY}/blob/{METHODOLOGY_COMMIT}/"
        "evaluate-subject-index/references/customer-methodology-v7.md"
    )
    projection: dict[str, Any] = {
        "schema_version": PROJECTION_SCHEMA_VERSION,
        "projection_id": projection_id,
        "projection_role": "deterministic_display_only_projection",
        "authority_statement": (
            "The files under candidate/v7-migration and their bound public supplements "
            "remain authoritative. This package projects them for presentation and does "
            "not recalculate or reinterpret the evaluation."
        ),
        "title": "The Oxford History of the French Revolution (2002)",
        "subtitle": "Original published index — V7 evaluation",
        "builder": {
            "builder_id": BUILDER_ID,
            "version": BUILDER_VERSION,
            "source": {
                "artifact_path": "scripts/build_web_projection.py",
                "sha256": sha256_file(repository_root / "scripts/build_web_projection.py"),
            },
            "command": (
                "python scripts/build_web_projection.py build --repository-root . "
                "--methodology-root ../methodology --benchmark-root ../benchmark "
                "--output-directory web/v7-published-index"
            ),
            "ordering_rules": [
                "authoritative_source_array_order",
                ORDERING_RULE,
            ],
            "timestamps": "omitted_for_determinism",
        },
        "repositories": {
            "evaluation": {
                "repository": EVALUATION_REPOSITORY,
                "commit": EVALUATION_BASE_COMMIT,
                "role": "authoritative_evaluation_source",
                "url": f"https://github.com/{EVALUATION_REPOSITORY}/tree/{EVALUATION_BASE_COMMIT}",
            },
            "methodology": {
                "repository": METHODOLOGY_REPOSITORY,
                "commit": METHODOLOGY_COMMIT,
                "tool_identity": METHODOLOGY_TOOL_IDENTITY,
                "role": "frozen_v7_methodology",
                "url": f"https://github.com/{METHODOLOGY_REPOSITORY}/tree/{METHODOLOGY_COMMIT}",
                "customer_methodology_url": methodology_url,
            },
            "benchmark": {
                "repository": BENCHMARK_REPOSITORY,
                "commit": BENCHMARK_HEAD_COMMIT,
                "frozen_benchmark_commit": migration["repository_state"]["frozen_benchmark_commit"],
                "frozen_benchmark_sha256": migration["repository_state"]["frozen_benchmark_sha256"],
                "role": "benchmark_repository_and_frozen_evaluation_binding",
                "url": f"https://github.com/{BENCHMARK_REPOSITORY}/tree/{BENCHMARK_HEAD_COMMIT}",
            },
        },
        "primary_view": {
            "view_id": "canonical_as_delivered",
            "role": "primary_observed_evaluation",
            "label": canonical_view["label"],
            "score": canonical_view["score"],
            "maximum_score": canonical_view["maximum"],
            "performance_label": web["grade"]["label"],
            "dimensions": canonical_dimensions,
            "calculation": deepcopy(canonical_view["calculation"]),
            "structure_locator_review": deepcopy(canonical_view["structure_locator_review"]),
            "locator_fit_supplement": deepcopy(canonical_view["locator_fit_supplement"]),
        },
        "secondary_view": {
            "view_id": "representation_adjusted",
            "role": "secondary_counterfactual_representation_view",
            "label": adjusted_view["label"],
            "score": adjusted_view["score"],
            "maximum_score": adjusted_view["maximum"],
            "description": (
                "This independently calculated, provenance-bound counterfactual changes "
                "only the explicitly documented representation assumptions. It is not a "
                "correction to the published index, a replacement score, or a change to "
                "the V7 methodology."
            ),
            "dimensions": adjusted_dimensions,
            "calculation": deepcopy(adjusted_view["calculation"]),
            "structure_locator_review": deepcopy(adjusted_view["structure_locator_review"]),
            "locator_fit_supplement": deepcopy(adjusted_view["locator_fit_supplement"]),
            "provenance_artifacts": deepcopy(adjusted_view["provenance_artifacts"]),
            "gate_outcomes_equal_to_primary": migration["gate_preservation"]["outcomes_equal"],
            "item_detail_scope": "canonical_item_assessments_only",
        },
        "gate_status": {
            "used_in_score_arithmetic": web["gate_status"]["used_in_score_arithmetic"],
            "counts": gate_counts,
            "gates": deepcopy(gates),
            "effect": (
                "An applicable failed gate prevents an unqualified publication-ready "
                "claim but does not secretly change the arithmetic score."
            ),
        },
        "key_metrics": {
            "weighted_locator_precision": reliability["weighted_locator_precision"],
            "strict_substantive_precision": reliability["strict_substantive_precision"],
            "expected_treatment_recall": reliability["treatment_recall"],
            "weighted_f1": reliability["weighted_f1"],
            "assessable_locator_count": reliability["assessable_locator_denominator"],
            "counts_by_treatment_tier": deepcopy(reliability["counts_by_treatment_tier"]),
            "counts_by_fit_tier": deepcopy(reliability["counts_by_fit_tier"]),
            "counts_by_combined_credit": deepcopy(reliability["counts_by_combined_credit_value"]),
            "density": deepcopy(density_component),
        },
        "item_grades": {
            "grading_policy": items["grading_policy"],
            "disclosure": items["grade_disclosure"],
            "color_legend": deepcopy(items["color_legend"]),
            "summary": deepcopy(items["summary"]),
            "collections": collection_bindings,
            "canonical_only": True,
            "interaction": {
                "color_source": "grade.color_token",
                "popover_source": "factors_and_evidence_ids",
                "color_alone_is_meaningful": False,
                "keyboard_touch_and_pointer_access": True,
            },
        },
        "calculation_disclosure": {
            "treatment_and_complete_path_fit_are_independent": True,
            "combined_locator_credit": "L = min(T,F)",
            "locator_grade": "100 × L",
            "page_reference_reliability_source": (
                "The complete frozen locator-credit ledger, combined with unchanged "
                "expected-treatment recall under the V7 calculation profile."
            ),
            "diagnostic_grades_used_in_dimension_arithmetic": False,
            "dimension_gates_and_caps": (
                "Applied according to subject-index-dimension-calculation-v3; gates "
                "remain separate claim restrictions."
            ),
            "aggregate_score_source": (
                "The completed, validated V6-to-V7 migration bound by the final receipt."
            ),
            "displayed_locator_language": (
                "A displayed locator is one delivered page reference or continuous "
                "range. A range is audited as multiple atomic page assignments but "
                "counts as one displayed locator for scanning and subdivision review."
            ),
        },
        "provenance": {
            "source_artifacts": source_bindings,
            "migration_id": migration["migration_id"],
            "migration_sha256": migration["migration_sha256"],
            "validation_receipt_id": receipt["receipt_id"],
            "validation_receipt_sha256": receipt["receipt_sha256"],
            "canonical_calculation_id": calculation["calculation_id"],
            "canonical_calculation_sha256": calculation["calculation_sha256"],
            "adjusted_calculation_id": adjusted["calculation_id"],
            "adjusted_calculation_sha256": adjusted["calculation_sha256"],
            "projection_metadata_id": documents["projection_metadata"]["projection_metadata_sha256"],
        },
        "limitations": [
            "The result applies only to the identified 2002 source edition and the evaluated published-index representation.",
            "The counterfactual is secondary and changes only the explicitly documented representation assumptions.",
            "Canonical supporting item detail comes from the public V7 item-assessment artifact; no separate adjusted item-assessment artifact is projected.",
            "Editorial judgments are evidence-based but can differ at the margins; stable IDs and provenance make disagreements inspectable.",
            "Density targets are this framework’s calibration points, not universal indexing standards or quotas.",
            "The repository excludes source PDFs, restricted ledgers, private migration inputs, and recovery material; this projection does not attempt to reconstruct them.",
        ],
        "public_safety": {
            "source_excerpts_included": False,
            "restricted_files_included": False,
            "external_runtime_dependencies": False,
            "third_party_javascript": False,
            "tracking_or_telemetry": False,
            "absolute_paths": False,
            "displayed_candidate_data_source": (
                "Only fields already present in the merged public V7 web-report and "
                "item-assessment contracts."
            ),
        },
        "renderer_assets": [
            {
                "artifact_path": name,
                "sha256": sha256_file(output_directory / name),
            }
            for name in ("index.html", "app.js", "styles.css")
        ],
    }
    projection["projection_sha256"] = canonical_hash(projection, "projection_sha256")
    write_json(output_directory / "projection.v1.json", projection)
    validate_projection_output(output_directory)
    return projection


def validate_projection_output(output_directory: Path) -> dict[str, Any]:
    projection_path = output_directory / "projection.v1.json"
    projection = load_json(projection_path)
    projection_decimal = load_json(projection_path, decimal=True)
    projection_schema = output_directory / "projection.schema.json"
    item_schema = output_directory / "item-collection.schema.json"
    local_registry = schema_registry(output_directory)
    validate_schema(projection_decimal, projection_schema, local_registry, "projection")
    require(
        canonical_hash(projection_decimal, "projection_sha256")
        == projection_decimal["projection_sha256"],
        "Projection self-hash is invalid.",
    )

    for binding in projection["renderer_assets"]:
        path = output_directory / binding["artifact_path"]
        require(path.is_file(), f"Bound renderer asset is missing: {path}.")
        require(
            sha256_file(path) == binding["sha256"],
            f"Bound renderer asset hash mismatch: {path}.",
        )

    expected_files = {
        *ASSET_NAMES,
        "projection.v1.json",
        *COLLECTION_FILES.values(),
    }
    actual_files = {
        path.relative_to(output_directory).as_posix()
        for path in output_directory.rglob("*")
        if path.is_file()
    }
    require(actual_files == expected_files, "Projection output file set is not exact.")

    binding_by_kind = {
        row["item_kind"]: row for row in projection["item_grades"]["collections"]
    }
    for kind, relative in COLLECTION_FILES.items():
        path = output_directory / relative
        binding = binding_by_kind[kind]
        require(sha256_file(path) == binding["sha256"], f"Collection file hash mismatch: {kind}.")
        document = load_json(path)
        decimal_document = load_json(path, decimal=True)
        validate_schema(decimal_document, item_schema, local_registry, f"collection {kind}")
        require(document["item_kind"] == kind, f"Collection kind mismatch: {kind}.")
        require(document["count"] == len(document["items"]), f"Collection count mismatch: {kind}.")
        require(document["count"] == binding["count"], f"Collection binding count mismatch: {kind}.")
        require(
            canonical_hash(decimal_document, "collection_sha256")
            == decimal_document["collection_sha256"],
            f"Collection self-hash mismatch: {kind}.",
        )
        require(
            document["collection_sha256"] == binding["collection_sha256"],
            f"Collection binding self-hash mismatch: {kind}.",
        )
        require(
            [item["source_order"] for item in document["items"]]
            == list(range(document["count"])),
            f"Collection source order drift: {kind}.",
        )

    privacy_scan(output_directory)
    return projection


def privacy_scan(output_directory: Path) -> None:
    prohibited = {
        "absolute_unix_path": re.compile(r"/(?:home|Users|workspace|tmp|root|mnt|opt)/"),
        "absolute_windows_path": re.compile(r"[A-Za-z]:\\\\"),
        "file_uri": re.compile(r"file://", re.IGNORECASE),
        "library_identifier": re.compile(r"(?:library://|LIB-[A-Z0-9]{8,})"),
        "credential": re.compile(r"(?:ghp_|github_pat_|sk-[A-Za-z0-9]{16,}|BEGIN PRIVATE KEY)"),
    }
    prohibited_suffixes = {".pdf", ".zip", ".docx", ".xlsx", ".sqlite", ".db"}
    all_files = [path for path in output_directory.rglob("*") if path.is_file()]
    for path in all_files:
        require(
            path.suffix.lower() not in prohibited_suffixes,
            f"Prohibited binary or archive type in projection: {path.name}.",
        )
        text = path.read_text(encoding="utf-8")
        for label, pattern in prohibited.items():
            require(not pattern.search(text), f"Public-safety scan found {label} in {path}.")
        if path.name == "index.html":
            require(
                not re.search(r"<(?:script|link)[^>]+https?://", text, re.IGNORECASE),
                "Renderer contains a network-loaded script, font, or stylesheet.",
            )


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    for command in ("build", "validate"):
        subparser = subparsers.add_parser(command)
        subparser.add_argument("--repository-root", type=Path, required=True)
        subparser.add_argument("--methodology-root", type=Path, required=True)
        subparser.add_argument("--benchmark-root", type=Path, required=True)
        subparser.add_argument("--output-directory", type=Path, required=True)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    repository_root = args.repository_root.resolve()
    methodology_root = args.methodology_root.resolve()
    benchmark_root = args.benchmark_root.resolve()
    output_directory = args.output_directory.resolve()
    try:
        if args.command == "build":
            projection = build_projection(
                repository_root,
                methodology_root,
                benchmark_root,
                output_directory,
            )
        else:
            validate_authoritative_state(repository_root, methodology_root, benchmark_root)
            projection = validate_projection_output(output_directory)
        builder_source = repository_root / projection["builder"]["source"]["artifact_path"]
        require(builder_source.is_file(), "Projection builder source is missing.")
        require(
            sha256_file(builder_source) == projection["builder"]["source"]["sha256"],
            "Projection builder source binding mismatch.",
        )
    except ProjectionError as exc:
        print(json.dumps({"command": args.command, "ok": False, "error": str(exc)}))
        return 1
    print(
        json.dumps(
            {
                "command": "build-web-projection" if args.command == "build" else "validate-web-projection",
                "ok": True,
                "projection_identity": projection["projection_id"],
                "projection_sha256": projection["projection_sha256"],
                "canonical_score": projection["primary_view"]["score"],
                "representation_adjusted_score": projection["secondary_view"]["score"],
                "output_directory": output_directory.as_posix(),
                "warnings": [],
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
