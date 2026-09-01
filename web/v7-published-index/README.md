# V7 published-index web projection

This directory is a deterministic, public-safe presentation of the completed V7 evaluation of the original published index to *The Oxford History of the French Revolution* (2002). It is intended for readers who want the result, supporting detail, calculation disclosures, and provenance without navigating migration internals.

The files under `candidate/v7-migration/` and their bound public supplements remain authoritative. `projection.v1.json` and the files under `data/` are display-only derivatives of those frozen artifacts. They do not replace `candidate/v7-migration/web-report.v7.json`, recalculate a score, reinterpret a judgment, or change methodology policy.

## Views

- `canonical_as_delivered` is the primary observed evaluation. It remains the result to lead with.
- `representation_adjusted` is a separate, secondary counterfactual. It changes only the representation assumptions documented by the authoritative migration record and public provenance artifacts. It is neither a correction to the published index nor a change to V7 methodology.
- Item-level drill-down is canonical only because the authoritative public V7 package does not contain a separate adjusted item-assessment artifact.

## Contracts and files

- `projection.schema.json` — Draft 2020-12 contract for `projection.v1.json`.
- `item-collection.schema.json` — Draft 2020-12 contract shared by the five item collections.
- `projection.v1.json` — summary, views, six dimensions, gates, metrics, disclosures, provenance, limitations, artifact bindings, and renderer hashes.
- `data/paths.v1.json` — complete heading paths.
- `data/headings.v1.json` — index heading nodes.
- `data/locators.v1.json` — individual locator assessments and frozen two-axis locator utility.
- `data/cross-references.v1.json` — cross-reference assessments.
- `data/source-subjects.v1.json` — frozen source-subject access assessments.
- `index.html`, `styles.css`, and `app.js` — dependency-free static renderer.

Every collection preserves the authoritative source-array order. Search and filters narrow that order without reranking. Defect-derived arrays are checked against `ITEM-PROJECTION-DEFECT-ID-ASC-V1`. The projection and each collection have reconstructable canonical-JSON self-hashes; file hashes bind the builder source, renderer, collections, and authoritative source artifacts. Timestamps are omitted.

## Authoritative sources

The builder binds all applicable merged public artifacts, including:

- `candidate/v7-migration/web-report.v7.json`;
- `candidate/v7-migration/evaluation-result.v7.json`;
- `candidate/v7-migration/item-assessments.v7.json`;
- canonical and adjusted `dimension-calculations` and `structure-locator-review` artifacts;
- `candidate/v7-migration/projection-metadata.v7.json`;
- `candidate/v7-migration/score-migration.v6-to-v7.json`;
- `candidate/v7-migration/validation-receipt.v7.json`;
- public canonical and adjusted architecture and locator-fit supplements;
- the public migration input and V6 projection chain; and
- the public representation-audit provenance bound by the adjusted view.

Methodology is pinned to [`df9112d036105213da74a4cc8f8f3f2a3ad26784`](https://github.com/jcamden/evaluate-subject-index/tree/df9112d036105213da74a4cc8f8f3f2a3ad26784), tool identity `dimension-score-cli-v7.0.6`. The builder reuses the methodology’s existing V7 schemas and display contracts; it introduces no methodology rule.

## Regenerate

Check out the three repositories as siblings at the commits declared in `projection.v1.json`, then run from this evaluation repository:

```bash
python scripts/build_web_projection.py build \
  --repository-root . \
  --methodology-root ../methodology \
  --benchmark-root ../benchmark \
  --output-directory web/v7-published-index
```

The committed output directory must already contain only the six renderer/contract source files. For a clean repeat, target an empty directory; the builder copies those source files and generates the same output set.

Preview locally without adding any runtime dependency:

```bash
python -m http.server 8000 --directory web/v7-published-index
```

Then open `http://localhost:8000/`.

## Validate

```bash
python -m py_compile scripts/build_web_projection.py
node --check web/v7-published-index/app.js
python scripts/build_web_projection.py validate \
  --repository-root . \
  --methodology-root ../methodology \
  --benchmark-root ../benchmark \
  --output-directory web/v7-published-index
python -m unittest discover -s tests -p 'test_*.py' -v
git diff --check
```

Determinism validation generates into two empty directories, changes `PYTHONHASHSEED` for the second run, compares exact file lists, and requires byte-identical files. The builder also validates all applicable authoritative inputs with the pinned Draft 2020-12 methodology schemas, verifies self-hashes and cross-artifact bindings, checks every locator grade against frozen calculation rows, and runs a public-safety scan.

## Public-safety boundary

The projection contains only fields already allowed by the merged public web-report and item-assessment contracts. It includes no source excerpts, PDFs, restricted adjudication ledgers, preflight working files, private manifests, recovery files, absolute paths, credentials, analytics, telemetry, external fonts, third-party JavaScript, or network runtime dependencies. Links point only to pinned public repository artifacts and methodology revisions.

## Limitations

The result applies to the identified edition and evaluated published-index representation. The counterfactual remains secondary. Editorial judgments can differ at the margins, density targets are framework calibration points rather than universal quotas, and the public package intentionally cannot reconstruct restricted evidence or private adjudication work.
