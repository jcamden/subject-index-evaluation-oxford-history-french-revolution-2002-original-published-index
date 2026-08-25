# Worker locator-audit launch prompts

Use one prompt in each isolated chapter-level chat. These prompts do not authorize a worker to proceed until that chunk’s restricted PDF and page sidecar have both been reconnected and verified by SHA-256. The candidate repository `main` branch was verified at the immutable base commit below, and no `locator-audit/*` branch existed when this launch pack was prepared; every worker must check again and refuse a collision.

## CHUNK-001 — 1. France under Louis XVI

```text
@Evaluate Subject Index worker-locator-audit CHUNK-001 --project jcamden/subject-index-evaluation-oxford-history-french-revolution-2002-original-published-index

Resume the canonical evaluation in an isolated worker:

- Evaluation ID: oxford-history-french-revolution-2002-indexerlabs-truncated
- Candidate ID: oxford-history-french-revolution-2002-original-published-index
- Expected base branch: main
- Immutable base commit: 026697ecb56847a4df0c5d6272b5c2b249672d7f
- Benchmark project/ref: jcamden/subject-index-benchmark-oxford-history-french-revolution-2002 @ 98dbffd0ca171b5b7db76dbe1b2b5d5265ccacab
- Frozen benchmark canonical SHA-256: b925797fcab50b2008ad5974590e323f772e5ea7013efa84ce7606007439aeb3
- Source document SHA-256: 5f89aa2592218983c594278bfd86cc1e4b74be1dd6dd8aac5c2610a48fa34047
- Candidate identity SHA-256: 1d43fe7fb158b352393c6e2f14843aae9ae23ccfca1f61c6783307432b0a9d09
- Normalized candidate file SHA-256: 7b29d7716339038848e2b1b0ec17220ae1867cb95941f0f06a84488cd486ed79
- Item inventory file SHA-256: 3e9c2b20d49486398bd57bfa31f5d1da1743498b47d0b9e46e42f096b56b9934
- Policy v2 file SHA-256: bfb5ec9ab45b6719b8a36fa09f50dfb8d8c18b3f209bd153501173182695ac62
- Page-map canonical SHA-256: 452602deebdae19f8e35c589f2ff2a7a0b9fc955d268b14f760391b0043e9653
- Chunk-manifest canonical SHA-256: 5fc5450386114fdeb19838f54d3f1662c3d6dec81d4729c73f4f7ec0cb341a6f
- Candidate-benchmark-lock file/canonical SHA-256: 3272d5362d27ca3ab62e7a8ef5fb1cf838df269ce7892035dc5140450306cf65 / 16e26f3d50da64fb211aba44940425ccbb20dcfa74e6e5202986b36cc9344ea8

Import and fully validate this cumulative portable checkpoint from `/IndexPDF/subject-index-evaluations/oxford-history-french-revolution-2002-original-published-index/canonical-integration`:

- oxford-history-french-revolution-2002-indexerlabs-truncated-candidate-oxford-history-french-revolution-2002-original-published-index-locator-packets-checkpoint-portable.zip
- SHA-256: afaeaeff298b558b4f739ece1b4f0c459142fb510c791b59d1df7d219759b2f7

Worker scope:

- Chunk: CHUNK-001
- Chapter: 1. France under Louis XVI
- Owned document pages: 1–43
- Locator packet: `candidate/oxford-history-french-revolution-2002-original-published-index/locator-packets/candidate-locator-CHUNK-001.json`
- Packet SHA-256: 15b1df8e2c41ff96890ac5e3588ebbbc621237818fcc78bc07c0ad8546c05212
- Expected locator assignments: 442

Before substantive work, retrieve these exact restricted artifacts from ChatGPT Library, materialize them at the evaluation-relative destinations, and hash-verify them:

- Library source: `/Subject Index Evaluations/Oxford History of the French Revolution 2002 - IndexerLabs truncated/source/chunks/CHUNK-001.pdf`
  - Materialize as: `source/chunks/CHUNK-001.pdf`
  - Required SHA-256: `d07984346063e4466b5d5dc6f68e3d20ba3e9fd1adf87a83c88d1bb13782e967`
- Library source: `/Subject Index Evaluations/Oxford History of the French Revolution 2002 - IndexerLabs truncated/source/chunks/CHUNK-001.pages.json`
  - Materialize as: `source/chunks/CHUNK-001.pages.json`
  - Required SHA-256: `d5aea1f2d3936b3c491351c83dab8132bc59ee2915a878ba93e59b35d2fd43a1`

If either restricted source artifact is unavailable or has a different hash, stop as blocked. Use the unique private recovery root `workers/locator-audit/CHUNK-001/`. Use branch `locator-audit/chunk-001`; refuse it if it already exists.

Audit every one of the 442 packet assignments exactly once. Preserve the complete heading path, judge only this chunk’s owned assignments, and use only `supported`, `partially_supported`, `unsupported`, or `uninspectable`. Record concise public-safe evidence paraphrases, evidence IDs, error codes, severity, and confidence. Do not perform missing-access, global-structure, density, item-assessment, scoring, or reporting work.

Use `parallel_candidate_audit_cli.py build-locator-worker`, `bind-publication`, and `validate-worker`. Preserve the complete private audit, receipt, worker state, worker manifest, and recovery ZIP under the recovery root before publication. Publish exactly `validation/locator-audit-worker.CHUNK-001.json` in one commit and one open, unmerged pull request. Do not publish private audit data, update canonical state or manifests, modify the benchmark repository, or merge the pull request.
```

## CHUNK-002 — 2. Enlightened Opinion

```text
@Evaluate Subject Index worker-locator-audit CHUNK-002 --project jcamden/subject-index-evaluation-oxford-history-french-revolution-2002-original-published-index

Resume the canonical evaluation in an isolated worker:

- Evaluation ID: oxford-history-french-revolution-2002-indexerlabs-truncated
- Candidate ID: oxford-history-french-revolution-2002-original-published-index
- Expected base branch: main
- Immutable base commit: 026697ecb56847a4df0c5d6272b5c2b249672d7f
- Benchmark project/ref: jcamden/subject-index-benchmark-oxford-history-french-revolution-2002 @ 98dbffd0ca171b5b7db76dbe1b2b5d5265ccacab
- Frozen benchmark canonical SHA-256: b925797fcab50b2008ad5974590e323f772e5ea7013efa84ce7606007439aeb3
- Source document SHA-256: 5f89aa2592218983c594278bfd86cc1e4b74be1dd6dd8aac5c2610a48fa34047
- Candidate identity SHA-256: 1d43fe7fb158b352393c6e2f14843aae9ae23ccfca1f61c6783307432b0a9d09
- Normalized candidate file SHA-256: 7b29d7716339038848e2b1b0ec17220ae1867cb95941f0f06a84488cd486ed79
- Item inventory file SHA-256: 3e9c2b20d49486398bd57bfa31f5d1da1743498b47d0b9e46e42f096b56b9934
- Policy v2 file SHA-256: bfb5ec9ab45b6719b8a36fa09f50dfb8d8c18b3f209bd153501173182695ac62
- Page-map canonical SHA-256: 452602deebdae19f8e35c589f2ff2a7a0b9fc955d268b14f760391b0043e9653
- Chunk-manifest canonical SHA-256: 5fc5450386114fdeb19838f54d3f1662c3d6dec81d4729c73f4f7ec0cb341a6f
- Candidate-benchmark-lock file/canonical SHA-256: 3272d5362d27ca3ab62e7a8ef5fb1cf838df269ce7892035dc5140450306cf65 / 16e26f3d50da64fb211aba44940425ccbb20dcfa74e6e5202986b36cc9344ea8

Import and fully validate this cumulative portable checkpoint from `/IndexPDF/subject-index-evaluations/oxford-history-french-revolution-2002-original-published-index/canonical-integration`:

- oxford-history-french-revolution-2002-indexerlabs-truncated-candidate-oxford-history-french-revolution-2002-original-published-index-locator-packets-checkpoint-portable.zip
- SHA-256: afaeaeff298b558b4f739ece1b4f0c459142fb510c791b59d1df7d219759b2f7

Worker scope:

- Chunk: CHUNK-002
- Chapter: 2. Enlightened Opinion
- Owned document pages: 44–65
- Locator packet: `candidate/oxford-history-french-revolution-2002-original-published-index/locator-packets/candidate-locator-CHUNK-002.json`
- Packet SHA-256: bc73b46eb7ff944c79691e7f64f6c36c2f1aeb6579c88464a02c2922781281a9
- Expected locator assignments: 244

Before substantive work, retrieve these exact restricted artifacts from ChatGPT Library, materialize them at the evaluation-relative destinations, and hash-verify them:

- Library source: `/Subject Index Evaluations/Oxford History of the French Revolution 2002 - IndexerLabs truncated/source/chunks/CHUNK-002.pdf`
  - Materialize as: `source/chunks/CHUNK-002.pdf`
  - Required SHA-256: `221dc48fc9f6d433209232db442e0e5730257e8204d24c7f88a78b76c6c0033f`
- Library source: `/Subject Index Evaluations/Oxford History of the French Revolution 2002 - IndexerLabs truncated/source/chunks/CHUNK-002.pages.json`
  - Materialize as: `source/chunks/CHUNK-002.pages.json`
  - Required SHA-256: `2d4d0cc922dbeaf146e97bdf16a6ff6236e3ce3931cf2b10cc0605551b1112b5`

If either restricted source artifact is unavailable or has a different hash, stop as blocked. Use the unique private recovery root `workers/locator-audit/CHUNK-002/`. Use branch `locator-audit/chunk-002`; refuse it if it already exists.

Audit every one of the 244 packet assignments exactly once. Preserve the complete heading path, judge only this chunk’s owned assignments, and use only `supported`, `partially_supported`, `unsupported`, or `uninspectable`. Record concise public-safe evidence paraphrases, evidence IDs, error codes, severity, and confidence. Do not perform missing-access, global-structure, density, item-assessment, scoring, or reporting work.

Use `parallel_candidate_audit_cli.py build-locator-worker`, `bind-publication`, and `validate-worker`. Preserve the complete private audit, receipt, worker state, worker manifest, and recovery ZIP under the recovery root before publication. Publish exactly `validation/locator-audit-worker.CHUNK-002.json` in one commit and one open, unmerged pull request. Do not publish private audit data, update canonical state or manifests, modify the benchmark repository, or merge the pull request.
```

## CHUNK-003 — 3. Crisis and Collapse, 1776-1788

```text
@Evaluate Subject Index worker-locator-audit CHUNK-003 --project jcamden/subject-index-evaluation-oxford-history-french-revolution-2002-original-published-index

Resume the canonical evaluation in an isolated worker:

- Evaluation ID: oxford-history-french-revolution-2002-indexerlabs-truncated
- Candidate ID: oxford-history-french-revolution-2002-original-published-index
- Expected base branch: main
- Immutable base commit: 026697ecb56847a4df0c5d6272b5c2b249672d7f
- Benchmark project/ref: jcamden/subject-index-benchmark-oxford-history-french-revolution-2002 @ 98dbffd0ca171b5b7db76dbe1b2b5d5265ccacab
- Frozen benchmark canonical SHA-256: b925797fcab50b2008ad5974590e323f772e5ea7013efa84ce7606007439aeb3
- Source document SHA-256: 5f89aa2592218983c594278bfd86cc1e4b74be1dd6dd8aac5c2610a48fa34047
- Candidate identity SHA-256: 1d43fe7fb158b352393c6e2f14843aae9ae23ccfca1f61c6783307432b0a9d09
- Normalized candidate file SHA-256: 7b29d7716339038848e2b1b0ec17220ae1867cb95941f0f06a84488cd486ed79
- Item inventory file SHA-256: 3e9c2b20d49486398bd57bfa31f5d1da1743498b47d0b9e46e42f096b56b9934
- Policy v2 file SHA-256: bfb5ec9ab45b6719b8a36fa09f50dfb8d8c18b3f209bd153501173182695ac62
- Page-map canonical SHA-256: 452602deebdae19f8e35c589f2ff2a7a0b9fc955d268b14f760391b0043e9653
- Chunk-manifest canonical SHA-256: 5fc5450386114fdeb19838f54d3f1662c3d6dec81d4729c73f4f7ec0cb341a6f
- Candidate-benchmark-lock file/canonical SHA-256: 3272d5362d27ca3ab62e7a8ef5fb1cf838df269ce7892035dc5140450306cf65 / 16e26f3d50da64fb211aba44940425ccbb20dcfa74e6e5202986b36cc9344ea8

Import and fully validate this cumulative portable checkpoint from `/IndexPDF/subject-index-evaluations/oxford-history-french-revolution-2002-original-published-index/canonical-integration`:

- oxford-history-french-revolution-2002-indexerlabs-truncated-candidate-oxford-history-french-revolution-2002-original-published-index-locator-packets-checkpoint-portable.zip
- SHA-256: afaeaeff298b558b4f739ece1b4f0c459142fb510c791b59d1df7d219759b2f7

Worker scope:

- Chunk: CHUNK-003
- Chapter: 3. Crisis and Collapse, 1776-1788
- Owned document pages: 66–85
- Locator packet: `candidate/oxford-history-french-revolution-2002-original-published-index/locator-packets/candidate-locator-CHUNK-003.json`
- Packet SHA-256: 427a4754784e4d45560837cd2172bb125c16ce80b8d007e526f4562f5ebf8b2c
- Expected locator assignments: 192

Before substantive work, retrieve these exact restricted artifacts from ChatGPT Library, materialize them at the evaluation-relative destinations, and hash-verify them:

- Library source: `/Subject Index Evaluations/Oxford History of the French Revolution 2002 - IndexerLabs truncated/source/chunks/CHUNK-003.pdf`
  - Materialize as: `source/chunks/CHUNK-003.pdf`
  - Required SHA-256: `7f74759390a5ca8c85378649b56f58c161ef091a3ab428a17131ed27db73b00f`
- Library source: `/Subject Index Evaluations/Oxford History of the French Revolution 2002 - IndexerLabs truncated/source/chunks/CHUNK-003.pages.json`
  - Materialize as: `source/chunks/CHUNK-003.pages.json`
  - Required SHA-256: `137041fcbc7ece6a63fbef85072c760f342fc92b28734410a8aeccd1d5c8a272`

If either restricted source artifact is unavailable or has a different hash, stop as blocked. Use the unique private recovery root `workers/locator-audit/CHUNK-003/`. Use branch `locator-audit/chunk-003`; refuse it if it already exists.

Audit every one of the 192 packet assignments exactly once. Preserve the complete heading path, judge only this chunk’s owned assignments, and use only `supported`, `partially_supported`, `unsupported`, or `uninspectable`. Record concise public-safe evidence paraphrases, evidence IDs, error codes, severity, and confidence. Do not perform missing-access, global-structure, density, item-assessment, scoring, or reporting work.

Use `parallel_candidate_audit_cli.py build-locator-worker`, `bind-publication`, and `validate-worker`. Preserve the complete private audit, receipt, worker state, worker manifest, and recovery ZIP under the recovery root before publication. Publish exactly `validation/locator-audit-worker.CHUNK-003.json` in one commit and one open, unmerged pull request. Do not publish private audit data, update canonical state or manifests, modify the benchmark repository, or merge the pull request.
```

## CHUNK-004 — 4. The Estates-General, September 1788-July 1789

```text
@Evaluate Subject Index worker-locator-audit CHUNK-004 --project jcamden/subject-index-evaluation-oxford-history-french-revolution-2002-original-published-index

Resume the canonical evaluation in an isolated worker:

- Evaluation ID: oxford-history-french-revolution-2002-indexerlabs-truncated
- Candidate ID: oxford-history-french-revolution-2002-original-published-index
- Expected base branch: main
- Immutable base commit: 026697ecb56847a4df0c5d6272b5c2b249672d7f
- Benchmark project/ref: jcamden/subject-index-benchmark-oxford-history-french-revolution-2002 @ 98dbffd0ca171b5b7db76dbe1b2b5d5265ccacab
- Frozen benchmark canonical SHA-256: b925797fcab50b2008ad5974590e323f772e5ea7013efa84ce7606007439aeb3
- Source document SHA-256: 5f89aa2592218983c594278bfd86cc1e4b74be1dd6dd8aac5c2610a48fa34047
- Candidate identity SHA-256: 1d43fe7fb158b352393c6e2f14843aae9ae23ccfca1f61c6783307432b0a9d09
- Normalized candidate file SHA-256: 7b29d7716339038848e2b1b0ec17220ae1867cb95941f0f06a84488cd486ed79
- Item inventory file SHA-256: 3e9c2b20d49486398bd57bfa31f5d1da1743498b47d0b9e46e42f096b56b9934
- Policy v2 file SHA-256: bfb5ec9ab45b6719b8a36fa09f50dfb8d8c18b3f209bd153501173182695ac62
- Page-map canonical SHA-256: 452602deebdae19f8e35c589f2ff2a7a0b9fc955d268b14f760391b0043e9653
- Chunk-manifest canonical SHA-256: 5fc5450386114fdeb19838f54d3f1662c3d6dec81d4729c73f4f7ec0cb341a6f
- Candidate-benchmark-lock file/canonical SHA-256: 3272d5362d27ca3ab62e7a8ef5fb1cf838df269ce7892035dc5140450306cf65 / 16e26f3d50da64fb211aba44940425ccbb20dcfa74e6e5202986b36cc9344ea8

Import and fully validate this cumulative portable checkpoint from `/IndexPDF/subject-index-evaluations/oxford-history-french-revolution-2002-original-published-index/canonical-integration`:

- oxford-history-french-revolution-2002-indexerlabs-truncated-candidate-oxford-history-french-revolution-2002-original-published-index-locator-packets-checkpoint-portable.zip
- SHA-256: afaeaeff298b558b4f739ece1b4f0c459142fb510c791b59d1df7d219759b2f7

Worker scope:

- Chunk: CHUNK-004
- Chapter: 4. The Estates-General, September 1788-July 1789
- Owned document pages: 86–111
- Locator packet: `candidate/oxford-history-french-revolution-2002-original-published-index/locator-packets/candidate-locator-CHUNK-004.json`
- Packet SHA-256: 82be1f59a1fb0f553cef01f2696ad022063f4f88bc86158fdc4d40592fca10a2
- Expected locator assignments: 289

Before substantive work, retrieve these exact restricted artifacts from ChatGPT Library, materialize them at the evaluation-relative destinations, and hash-verify them:

- Library source: `/Subject Index Evaluations/Oxford History of the French Revolution 2002 - IndexerLabs truncated/source/chunks/CHUNK-004.pdf`
  - Materialize as: `source/chunks/CHUNK-004.pdf`
  - Required SHA-256: `a38f47cc71bf0f119fa26760d9780b6b3cd6d8885547d6e933f093da4f351cfe`
- Library source: `/Subject Index Evaluations/Oxford History of the French Revolution 2002 - IndexerLabs truncated/source/chunks/CHUNK-004.pages.json`
  - Materialize as: `source/chunks/CHUNK-004.pages.json`
  - Required SHA-256: `1353e5061e5cc9988be43e54fe912a2c5b4b2e6bd2e069edb529786a0fde01a8`

If either restricted source artifact is unavailable or has a different hash, stop as blocked. Use the unique private recovery root `workers/locator-audit/CHUNK-004/`. Use branch `locator-audit/chunk-004`; refuse it if it already exists.

Audit every one of the 289 packet assignments exactly once. Preserve the complete heading path, judge only this chunk’s owned assignments, and use only `supported`, `partially_supported`, `unsupported`, or `uninspectable`. Record concise public-safe evidence paraphrases, evidence IDs, error codes, severity, and confidence. Do not perform missing-access, global-structure, density, item-assessment, scoring, or reporting work.

Use `parallel_candidate_audit_cli.py build-locator-worker`, `bind-publication`, and `validate-worker`. Preserve the complete private audit, receipt, worker state, worker manifest, and recovery ZIP under the recovery root before publication. Publish exactly `validation/locator-audit-worker.CHUNK-004.json` in one commit and one open, unmerged pull request. Do not publish private audit data, update canonical state or manifests, modify the benchmark repository, or merge the pull request.
```

## CHUNK-005 — 5. The Principles of 1789 and the Reform of France

```text
@Evaluate Subject Index worker-locator-audit CHUNK-005 --project jcamden/subject-index-evaluation-oxford-history-french-revolution-2002-original-published-index

Resume the canonical evaluation in an isolated worker:

- Evaluation ID: oxford-history-french-revolution-2002-indexerlabs-truncated
- Candidate ID: oxford-history-french-revolution-2002-original-published-index
- Expected base branch: main
- Immutable base commit: 026697ecb56847a4df0c5d6272b5c2b249672d7f
- Benchmark project/ref: jcamden/subject-index-benchmark-oxford-history-french-revolution-2002 @ 98dbffd0ca171b5b7db76dbe1b2b5d5265ccacab
- Frozen benchmark canonical SHA-256: b925797fcab50b2008ad5974590e323f772e5ea7013efa84ce7606007439aeb3
- Source document SHA-256: 5f89aa2592218983c594278bfd86cc1e4b74be1dd6dd8aac5c2610a48fa34047
- Candidate identity SHA-256: 1d43fe7fb158b352393c6e2f14843aae9ae23ccfca1f61c6783307432b0a9d09
- Normalized candidate file SHA-256: 7b29d7716339038848e2b1b0ec17220ae1867cb95941f0f06a84488cd486ed79
- Item inventory file SHA-256: 3e9c2b20d49486398bd57bfa31f5d1da1743498b47d0b9e46e42f096b56b9934
- Policy v2 file SHA-256: bfb5ec9ab45b6719b8a36fa09f50dfb8d8c18b3f209bd153501173182695ac62
- Page-map canonical SHA-256: 452602deebdae19f8e35c589f2ff2a7a0b9fc955d268b14f760391b0043e9653
- Chunk-manifest canonical SHA-256: 5fc5450386114fdeb19838f54d3f1662c3d6dec81d4729c73f4f7ec0cb341a6f
- Candidate-benchmark-lock file/canonical SHA-256: 3272d5362d27ca3ab62e7a8ef5fb1cf838df269ce7892035dc5140450306cf65 / 16e26f3d50da64fb211aba44940425ccbb20dcfa74e6e5202986b36cc9344ea8

Import and fully validate this cumulative portable checkpoint from `/IndexPDF/subject-index-evaluations/oxford-history-french-revolution-2002-original-published-index/canonical-integration`:

- oxford-history-french-revolution-2002-indexerlabs-truncated-candidate-oxford-history-french-revolution-2002-original-published-index-locator-packets-checkpoint-portable.zip
- SHA-256: afaeaeff298b558b4f739ece1b4f0c459142fb510c791b59d1df7d219759b2f7

Worker scope:

- Chunk: CHUNK-005
- Chapter: 5. The Principles of 1789 and the Reform of France
- Owned document pages: 112–135
- Locator packet: `candidate/oxford-history-french-revolution-2002-original-published-index/locator-packets/candidate-locator-CHUNK-005.json`
- Packet SHA-256: 51a6808236571b957895e4962ca812e0f202c29ed28f1df8706e842d4e5b04f9
- Expected locator assignments: 306

Before substantive work, retrieve these exact restricted artifacts from ChatGPT Library, materialize them at the evaluation-relative destinations, and hash-verify them:

- Library source: `/Subject Index Evaluations/Oxford History of the French Revolution 2002 - IndexerLabs truncated/source/chunks/CHUNK-005.pdf`
  - Materialize as: `source/chunks/CHUNK-005.pdf`
  - Required SHA-256: `8ead7b33b569c1fd236d3126ce0868284e9aa4fece95ab16c864e81a94f135af`
- Library source: `/Subject Index Evaluations/Oxford History of the French Revolution 2002 - IndexerLabs truncated/source/chunks/CHUNK-005.pages.json`
  - Materialize as: `source/chunks/CHUNK-005.pages.json`
  - Required SHA-256: `f9117474d9c2f749acbf2564b8e9e1fa08b8ba2b8a9808cb9175376cf3a574bf`

If either restricted source artifact is unavailable or has a different hash, stop as blocked. Use the unique private recovery root `workers/locator-audit/CHUNK-005/`. Use branch `locator-audit/chunk-005`; refuse it if it already exists.

Audit every one of the 306 packet assignments exactly once. Preserve the complete heading path, judge only this chunk’s owned assignments, and use only `supported`, `partially_supported`, `unsupported`, or `uninspectable`. Record concise public-safe evidence paraphrases, evidence IDs, error codes, severity, and confidence. Do not perform missing-access, global-structure, density, item-assessment, scoring, or reporting work.

Use `parallel_candidate_audit_cli.py build-locator-worker`, `bind-publication`, and `validate-worker`. Preserve the complete private audit, receipt, worker state, worker manifest, and recovery ZIP under the recovery root before publication. Publish exactly `validation/locator-audit-worker.CHUNK-005.json` in one commit and one open, unmerged pull request. Do not publish private audit data, update canonical state or manifests, modify the benchmark repository, or merge the pull request.
```

## CHUNK-006 — 6. The Breakdown of the Revolutionary Consensus, 1790-1791

```text
@Evaluate Subject Index worker-locator-audit CHUNK-006 --project jcamden/subject-index-evaluation-oxford-history-french-revolution-2002-original-published-index

Resume the canonical evaluation in an isolated worker:

- Evaluation ID: oxford-history-french-revolution-2002-indexerlabs-truncated
- Candidate ID: oxford-history-french-revolution-2002-original-published-index
- Expected base branch: main
- Immutable base commit: 026697ecb56847a4df0c5d6272b5c2b249672d7f
- Benchmark project/ref: jcamden/subject-index-benchmark-oxford-history-french-revolution-2002 @ 98dbffd0ca171b5b7db76dbe1b2b5d5265ccacab
- Frozen benchmark canonical SHA-256: b925797fcab50b2008ad5974590e323f772e5ea7013efa84ce7606007439aeb3
- Source document SHA-256: 5f89aa2592218983c594278bfd86cc1e4b74be1dd6dd8aac5c2610a48fa34047
- Candidate identity SHA-256: 1d43fe7fb158b352393c6e2f14843aae9ae23ccfca1f61c6783307432b0a9d09
- Normalized candidate file SHA-256: 7b29d7716339038848e2b1b0ec17220ae1867cb95941f0f06a84488cd486ed79
- Item inventory file SHA-256: 3e9c2b20d49486398bd57bfa31f5d1da1743498b47d0b9e46e42f096b56b9934
- Policy v2 file SHA-256: bfb5ec9ab45b6719b8a36fa09f50dfb8d8c18b3f209bd153501173182695ac62
- Page-map canonical SHA-256: 452602deebdae19f8e35c589f2ff2a7a0b9fc955d268b14f760391b0043e9653
- Chunk-manifest canonical SHA-256: 5fc5450386114fdeb19838f54d3f1662c3d6dec81d4729c73f4f7ec0cb341a6f
- Candidate-benchmark-lock file/canonical SHA-256: 3272d5362d27ca3ab62e7a8ef5fb1cf838df269ce7892035dc5140450306cf65 / 16e26f3d50da64fb211aba44940425ccbb20dcfa74e6e5202986b36cc9344ea8

Import and fully validate this cumulative portable checkpoint from `/IndexPDF/subject-index-evaluations/oxford-history-french-revolution-2002-original-published-index/canonical-integration`:

- oxford-history-french-revolution-2002-indexerlabs-truncated-candidate-oxford-history-french-revolution-2002-original-published-index-locator-packets-checkpoint-portable.zip
- SHA-256: afaeaeff298b558b4f739ece1b4f0c459142fb510c791b59d1df7d219759b2f7

Worker scope:

- Chunk: CHUNK-006
- Chapter: 6. The Breakdown of the Revolutionary Consensus, 1790-1791
- Owned document pages: 136–158
- Locator packet: `candidate/oxford-history-french-revolution-2002-original-published-index/locator-packets/candidate-locator-CHUNK-006.json`
- Packet SHA-256: ed4501ade728c780c56893afcc9e6aab622ebe8752a157d7e430d691a747d6e5
- Expected locator assignments: 298

Before substantive work, retrieve these exact restricted artifacts from ChatGPT Library, materialize them at the evaluation-relative destinations, and hash-verify them:

- Library source: `/Subject Index Evaluations/Oxford History of the French Revolution 2002 - IndexerLabs truncated/source/chunks/CHUNK-006.pdf`
  - Materialize as: `source/chunks/CHUNK-006.pdf`
  - Required SHA-256: `22e6923731c4aeae3940f1aa95f109816eb48b7d53175ee720115ca5ed697306`
- Library source: `/Subject Index Evaluations/Oxford History of the French Revolution 2002 - IndexerLabs truncated/source/chunks/CHUNK-006.pages.json`
  - Materialize as: `source/chunks/CHUNK-006.pages.json`
  - Required SHA-256: `b87631df54474bc7167f0eb7b4dd1e187cb75da7fe5a09d7697c2e798a66f154`

If either restricted source artifact is unavailable or has a different hash, stop as blocked. Use the unique private recovery root `workers/locator-audit/CHUNK-006/`. Use branch `locator-audit/chunk-006`; refuse it if it already exists.

Audit every one of the 298 packet assignments exactly once. Preserve the complete heading path, judge only this chunk’s owned assignments, and use only `supported`, `partially_supported`, `unsupported`, or `uninspectable`. Record concise public-safe evidence paraphrases, evidence IDs, error codes, severity, and confidence. Do not perform missing-access, global-structure, density, item-assessment, scoring, or reporting work.

Use `parallel_candidate_audit_cli.py build-locator-worker`, `bind-publication`, and `validate-worker`. Preserve the complete private audit, receipt, worker state, worker manifest, and recovery ZIP under the recovery root before publication. Publish exactly `validation/locator-audit-worker.CHUNK-006.json` in one commit and one open, unmerged pull request. Do not publish private audit data, update canonical state or manifests, modify the benchmark repository, or merge the pull request.
```

## CHUNK-007 — 7. Europe and the Revolution, 1788-1791

```text
@Evaluate Subject Index worker-locator-audit CHUNK-007 --project jcamden/subject-index-evaluation-oxford-history-french-revolution-2002-original-published-index

Resume the canonical evaluation in an isolated worker:

- Evaluation ID: oxford-history-french-revolution-2002-indexerlabs-truncated
- Candidate ID: oxford-history-french-revolution-2002-original-published-index
- Expected base branch: main
- Immutable base commit: 026697ecb56847a4df0c5d6272b5c2b249672d7f
- Benchmark project/ref: jcamden/subject-index-benchmark-oxford-history-french-revolution-2002 @ 98dbffd0ca171b5b7db76dbe1b2b5d5265ccacab
- Frozen benchmark canonical SHA-256: b925797fcab50b2008ad5974590e323f772e5ea7013efa84ce7606007439aeb3
- Source document SHA-256: 5f89aa2592218983c594278bfd86cc1e4b74be1dd6dd8aac5c2610a48fa34047
- Candidate identity SHA-256: 1d43fe7fb158b352393c6e2f14843aae9ae23ccfca1f61c6783307432b0a9d09
- Normalized candidate file SHA-256: 7b29d7716339038848e2b1b0ec17220ae1867cb95941f0f06a84488cd486ed79
- Item inventory file SHA-256: 3e9c2b20d49486398bd57bfa31f5d1da1743498b47d0b9e46e42f096b56b9934
- Policy v2 file SHA-256: bfb5ec9ab45b6719b8a36fa09f50dfb8d8c18b3f209bd153501173182695ac62
- Page-map canonical SHA-256: 452602deebdae19f8e35c589f2ff2a7a0b9fc955d268b14f760391b0043e9653
- Chunk-manifest canonical SHA-256: 5fc5450386114fdeb19838f54d3f1662c3d6dec81d4729c73f4f7ec0cb341a6f
- Candidate-benchmark-lock file/canonical SHA-256: 3272d5362d27ca3ab62e7a8ef5fb1cf838df269ce7892035dc5140450306cf65 / 16e26f3d50da64fb211aba44940425ccbb20dcfa74e6e5202986b36cc9344ea8

Import and fully validate this cumulative portable checkpoint from `/IndexPDF/subject-index-evaluations/oxford-history-french-revolution-2002-original-published-index/canonical-integration`:

- oxford-history-french-revolution-2002-indexerlabs-truncated-candidate-oxford-history-french-revolution-2002-original-published-index-locator-packets-checkpoint-portable.zip
- SHA-256: afaeaeff298b558b4f739ece1b4f0c459142fb510c791b59d1df7d219759b2f7

Worker scope:

- Chunk: CHUNK-007
- Chapter: 7. Europe and the Revolution, 1788-1791
- Owned document pages: 159–173
- Locator packet: `candidate/oxford-history-french-revolution-2002-original-published-index/locator-packets/candidate-locator-CHUNK-007.json`
- Packet SHA-256: 209aad79a77b204d38873a62111c3ed2783640be2cff0c1baef6ab5048f24988
- Expected locator assignments: 174

Before substantive work, retrieve these exact restricted artifacts from ChatGPT Library, materialize them at the evaluation-relative destinations, and hash-verify them:

- Library source: `/Subject Index Evaluations/Oxford History of the French Revolution 2002 - IndexerLabs truncated/source/chunks/CHUNK-007.pdf`
  - Materialize as: `source/chunks/CHUNK-007.pdf`
  - Required SHA-256: `26ce178444651abe7aa3ed668ab060768fd093bb76ab6556ed9beea11cfbd55c`
- Library source: `/Subject Index Evaluations/Oxford History of the French Revolution 2002 - IndexerLabs truncated/source/chunks/CHUNK-007.pages.json`
  - Materialize as: `source/chunks/CHUNK-007.pages.json`
  - Required SHA-256: `693a25f982ac97534f3380439f2b56b35b1e1e023a4686d4e40e7b9950e9c423`

If either restricted source artifact is unavailable or has a different hash, stop as blocked. Use the unique private recovery root `workers/locator-audit/CHUNK-007/`. Use branch `locator-audit/chunk-007`; refuse it if it already exists.

Audit every one of the 174 packet assignments exactly once. Preserve the complete heading path, judge only this chunk’s owned assignments, and use only `supported`, `partially_supported`, `unsupported`, or `uninspectable`. Record concise public-safe evidence paraphrases, evidence IDs, error codes, severity, and confidence. Do not perform missing-access, global-structure, density, item-assessment, scoring, or reporting work.

Use `parallel_candidate_audit_cli.py build-locator-worker`, `bind-publication`, and `validate-worker`. Preserve the complete private audit, receipt, worker state, worker manifest, and recovery ZIP under the recovery root before publication. Publish exactly `validation/locator-audit-worker.CHUNK-007.json` in one commit and one open, unmerged pull request. Do not publish private audit data, update canonical state or manifests, modify the benchmark repository, or merge the pull request.
```

## CHUNK-008 — 8. The Republican Revolution, October 1791-January 1793

```text
@Evaluate Subject Index worker-locator-audit CHUNK-008 --project jcamden/subject-index-evaluation-oxford-history-french-revolution-2002-original-published-index

Resume the canonical evaluation in an isolated worker:

- Evaluation ID: oxford-history-french-revolution-2002-indexerlabs-truncated
- Candidate ID: oxford-history-french-revolution-2002-original-published-index
- Expected base branch: main
- Immutable base commit: 026697ecb56847a4df0c5d6272b5c2b249672d7f
- Benchmark project/ref: jcamden/subject-index-benchmark-oxford-history-french-revolution-2002 @ 98dbffd0ca171b5b7db76dbe1b2b5d5265ccacab
- Frozen benchmark canonical SHA-256: b925797fcab50b2008ad5974590e323f772e5ea7013efa84ce7606007439aeb3
- Source document SHA-256: 5f89aa2592218983c594278bfd86cc1e4b74be1dd6dd8aac5c2610a48fa34047
- Candidate identity SHA-256: 1d43fe7fb158b352393c6e2f14843aae9ae23ccfca1f61c6783307432b0a9d09
- Normalized candidate file SHA-256: 7b29d7716339038848e2b1b0ec17220ae1867cb95941f0f06a84488cd486ed79
- Item inventory file SHA-256: 3e9c2b20d49486398bd57bfa31f5d1da1743498b47d0b9e46e42f096b56b9934
- Policy v2 file SHA-256: bfb5ec9ab45b6719b8a36fa09f50dfb8d8c18b3f209bd153501173182695ac62
- Page-map canonical SHA-256: 452602deebdae19f8e35c589f2ff2a7a0b9fc955d268b14f760391b0043e9653
- Chunk-manifest canonical SHA-256: 5fc5450386114fdeb19838f54d3f1662c3d6dec81d4729c73f4f7ec0cb341a6f
- Candidate-benchmark-lock file/canonical SHA-256: 3272d5362d27ca3ab62e7a8ef5fb1cf838df269ce7892035dc5140450306cf65 / 16e26f3d50da64fb211aba44940425ccbb20dcfa74e6e5202986b36cc9344ea8

Import and fully validate this cumulative portable checkpoint from `/IndexPDF/subject-index-evaluations/oxford-history-french-revolution-2002-original-published-index/canonical-integration`:

- oxford-history-french-revolution-2002-indexerlabs-truncated-candidate-oxford-history-french-revolution-2002-original-published-index-locator-packets-checkpoint-portable.zip
- SHA-256: afaeaeff298b558b4f739ece1b4f0c459142fb510c791b59d1df7d219759b2f7

Worker scope:

- Chunk: CHUNK-008
- Chapter: 8. The Republican Revolution, October 1791-January 1793
- Owned document pages: 174–196
- Locator packet: `candidate/oxford-history-french-revolution-2002-original-published-index/locator-packets/candidate-locator-CHUNK-008.json`
- Packet SHA-256: 5dd58a4e9960d7637a5842df1b1019ac5084d68695af342ab312014022a661f5
- Expected locator assignments: 277

Before substantive work, retrieve these exact restricted artifacts from ChatGPT Library, materialize them at the evaluation-relative destinations, and hash-verify them:

- Library source: `/Subject Index Evaluations/Oxford History of the French Revolution 2002 - IndexerLabs truncated/source/chunks/CHUNK-008.pdf`
  - Materialize as: `source/chunks/CHUNK-008.pdf`
  - Required SHA-256: `9623c8767a2f57eb09e7d6ad4992ac17f78e8781db8ff176c56f474065cc2d81`
- Library source: `/Subject Index Evaluations/Oxford History of the French Revolution 2002 - IndexerLabs truncated/source/chunks/CHUNK-008.pages.json`
  - Materialize as: `source/chunks/CHUNK-008.pages.json`
  - Required SHA-256: `be52821ccc83f0449e9230ea1d0eebab1ca21509bf5757a8281f9ecd35b256ef`

If either restricted source artifact is unavailable or has a different hash, stop as blocked. Use the unique private recovery root `workers/locator-audit/CHUNK-008/`. Use branch `locator-audit/chunk-008`; refuse it if it already exists.

Audit every one of the 277 packet assignments exactly once. Preserve the complete heading path, judge only this chunk’s owned assignments, and use only `supported`, `partially_supported`, `unsupported`, or `uninspectable`. Record concise public-safe evidence paraphrases, evidence IDs, error codes, severity, and confidence. Do not perform missing-access, global-structure, density, item-assessment, scoring, or reporting work.

Use `parallel_candidate_audit_cli.py build-locator-worker`, `bind-publication`, and `validate-worker`. Preserve the complete private audit, receipt, worker state, worker manifest, and recovery ZIP under the recovery root before publication. Publish exactly `validation/locator-audit-worker.CHUNK-008.json` in one commit and one open, unmerged pull request. Do not publish private audit data, update canonical state or manifests, modify the benchmark repository, or merge the pull request.
```

## CHUNK-009 — 9. War against Europe, 1792-1797

```text
@Evaluate Subject Index worker-locator-audit CHUNK-009 --project jcamden/subject-index-evaluation-oxford-history-french-revolution-2002-original-published-index

Resume the canonical evaluation in an isolated worker:

- Evaluation ID: oxford-history-french-revolution-2002-indexerlabs-truncated
- Candidate ID: oxford-history-french-revolution-2002-original-published-index
- Expected base branch: main
- Immutable base commit: 026697ecb56847a4df0c5d6272b5c2b249672d7f
- Benchmark project/ref: jcamden/subject-index-benchmark-oxford-history-french-revolution-2002 @ 98dbffd0ca171b5b7db76dbe1b2b5d5265ccacab
- Frozen benchmark canonical SHA-256: b925797fcab50b2008ad5974590e323f772e5ea7013efa84ce7606007439aeb3
- Source document SHA-256: 5f89aa2592218983c594278bfd86cc1e4b74be1dd6dd8aac5c2610a48fa34047
- Candidate identity SHA-256: 1d43fe7fb158b352393c6e2f14843aae9ae23ccfca1f61c6783307432b0a9d09
- Normalized candidate file SHA-256: 7b29d7716339038848e2b1b0ec17220ae1867cb95941f0f06a84488cd486ed79
- Item inventory file SHA-256: 3e9c2b20d49486398bd57bfa31f5d1da1743498b47d0b9e46e42f096b56b9934
- Policy v2 file SHA-256: bfb5ec9ab45b6719b8a36fa09f50dfb8d8c18b3f209bd153501173182695ac62
- Page-map canonical SHA-256: 452602deebdae19f8e35c589f2ff2a7a0b9fc955d268b14f760391b0043e9653
- Chunk-manifest canonical SHA-256: 5fc5450386114fdeb19838f54d3f1662c3d6dec81d4729c73f4f7ec0cb341a6f
- Candidate-benchmark-lock file/canonical SHA-256: 3272d5362d27ca3ab62e7a8ef5fb1cf838df269ce7892035dc5140450306cf65 / 16e26f3d50da64fb211aba44940425ccbb20dcfa74e6e5202986b36cc9344ea8

Import and fully validate this cumulative portable checkpoint from `/IndexPDF/subject-index-evaluations/oxford-history-french-revolution-2002-original-published-index/canonical-integration`:

- oxford-history-french-revolution-2002-indexerlabs-truncated-candidate-oxford-history-french-revolution-2002-original-published-index-locator-packets-checkpoint-portable.zip
- SHA-256: afaeaeff298b558b4f739ece1b4f0c459142fb510c791b59d1df7d219759b2f7

Worker scope:

- Chunk: CHUNK-009
- Chapter: 9. War against Europe, 1792-1797
- Owned document pages: 197–219
- Locator packet: `candidate/oxford-history-french-revolution-2002-original-published-index/locator-packets/candidate-locator-CHUNK-009.json`
- Packet SHA-256: c586d0b37a954ffcc2bf321dbcb7b7250aa93f4841c8409ad4b88b49b9cc7840
- Expected locator assignments: 392

Before substantive work, retrieve these exact restricted artifacts from ChatGPT Library, materialize them at the evaluation-relative destinations, and hash-verify them:

- Library source: `/Subject Index Evaluations/Oxford History of the French Revolution 2002 - IndexerLabs truncated/source/chunks/CHUNK-009.pdf`
  - Materialize as: `source/chunks/CHUNK-009.pdf`
  - Required SHA-256: `889d2ae4c025d67f39454662f6c7a69958e309110eaf097f0affe88f2c750bb8`
- Library source: `/Subject Index Evaluations/Oxford History of the French Revolution 2002 - IndexerLabs truncated/source/chunks/CHUNK-009.pages.json`
  - Materialize as: `source/chunks/CHUNK-009.pages.json`
  - Required SHA-256: `4c25483f5fbd081ae044d416e6c0218f55c32544f8d85f14d6a102bd35de1bf5`

If either restricted source artifact is unavailable or has a different hash, stop as blocked. Use the unique private recovery root `workers/locator-audit/CHUNK-009/`. Use branch `locator-audit/chunk-009`; refuse it if it already exists.

Audit every one of the 392 packet assignments exactly once. Preserve the complete heading path, judge only this chunk’s owned assignments, and use only `supported`, `partially_supported`, `unsupported`, or `uninspectable`. Record concise public-safe evidence paraphrases, evidence IDs, error codes, severity, and confidence. Do not perform missing-access, global-structure, density, item-assessment, scoring, or reporting work.

Use `parallel_candidate_audit_cli.py build-locator-worker`, `bind-publication`, and `validate-worker`. Preserve the complete private audit, receipt, worker state, worker manifest, and recovery ZIP under the recovery root before publication. Publish exactly `validation/locator-audit-worker.CHUNK-009.json` in one commit and one open, unmerged pull request. Do not publish private audit data, update canonical state or manifests, modify the benchmark repository, or merge the pull request.
```

## CHUNK-010 — 10. The Revolt of the Provinces

```text
@Evaluate Subject Index worker-locator-audit CHUNK-010 --project jcamden/subject-index-evaluation-oxford-history-french-revolution-2002-original-published-index

Resume the canonical evaluation in an isolated worker:

- Evaluation ID: oxford-history-french-revolution-2002-indexerlabs-truncated
- Candidate ID: oxford-history-french-revolution-2002-original-published-index
- Expected base branch: main
- Immutable base commit: 026697ecb56847a4df0c5d6272b5c2b249672d7f
- Benchmark project/ref: jcamden/subject-index-benchmark-oxford-history-french-revolution-2002 @ 98dbffd0ca171b5b7db76dbe1b2b5d5265ccacab
- Frozen benchmark canonical SHA-256: b925797fcab50b2008ad5974590e323f772e5ea7013efa84ce7606007439aeb3
- Source document SHA-256: 5f89aa2592218983c594278bfd86cc1e4b74be1dd6dd8aac5c2610a48fa34047
- Candidate identity SHA-256: 1d43fe7fb158b352393c6e2f14843aae9ae23ccfca1f61c6783307432b0a9d09
- Normalized candidate file SHA-256: 7b29d7716339038848e2b1b0ec17220ae1867cb95941f0f06a84488cd486ed79
- Item inventory file SHA-256: 3e9c2b20d49486398bd57bfa31f5d1da1743498b47d0b9e46e42f096b56b9934
- Policy v2 file SHA-256: bfb5ec9ab45b6719b8a36fa09f50dfb8d8c18b3f209bd153501173182695ac62
- Page-map canonical SHA-256: 452602deebdae19f8e35c589f2ff2a7a0b9fc955d268b14f760391b0043e9653
- Chunk-manifest canonical SHA-256: 5fc5450386114fdeb19838f54d3f1662c3d6dec81d4729c73f4f7ec0cb341a6f
- Candidate-benchmark-lock file/canonical SHA-256: 3272d5362d27ca3ab62e7a8ef5fb1cf838df269ce7892035dc5140450306cf65 / 16e26f3d50da64fb211aba44940425ccbb20dcfa74e6e5202986b36cc9344ea8

Import and fully validate this cumulative portable checkpoint from `/IndexPDF/subject-index-evaluations/oxford-history-french-revolution-2002-original-published-index/canonical-integration`:

- oxford-history-french-revolution-2002-indexerlabs-truncated-candidate-oxford-history-french-revolution-2002-original-published-index-locator-packets-checkpoint-portable.zip
- SHA-256: afaeaeff298b558b4f739ece1b4f0c459142fb510c791b59d1df7d219759b2f7

Worker scope:

- Chunk: CHUNK-010
- Chapter: 10. The Revolt of the Provinces
- Owned document pages: 220–246
- Locator packet: `candidate/oxford-history-french-revolution-2002-original-published-index/locator-packets/candidate-locator-CHUNK-010.json`
- Packet SHA-256: aaabd78b5d65bbc58a9add4024deba9d188f5cbf4f050dd3379eb2344f73568b
- Expected locator assignments: 348

Before substantive work, retrieve these exact restricted artifacts from ChatGPT Library, materialize them at the evaluation-relative destinations, and hash-verify them:

- Library source: `/Subject Index Evaluations/Oxford History of the French Revolution 2002 - IndexerLabs truncated/source/chunks/CHUNK-010.pdf`
  - Materialize as: `source/chunks/CHUNK-010.pdf`
  - Required SHA-256: `70d05ac8d6cc96da9bcac61000cc95e7901b80f076b11b2239a86bb98b35b03d`
- Library source: `/Subject Index Evaluations/Oxford History of the French Revolution 2002 - IndexerLabs truncated/source/chunks/CHUNK-010.pages.json`
  - Materialize as: `source/chunks/CHUNK-010.pages.json`
  - Required SHA-256: `a47ea2d7d5d3f22b92e602ec257eeb6270ec473e925c062ab0c5ae21c850f2d2`

If either restricted source artifact is unavailable or has a different hash, stop as blocked. Use the unique private recovery root `workers/locator-audit/CHUNK-010/`. Use branch `locator-audit/chunk-010`; refuse it if it already exists.

Audit every one of the 348 packet assignments exactly once. Preserve the complete heading path, judge only this chunk’s owned assignments, and use only `supported`, `partially_supported`, `unsupported`, or `uninspectable`. Record concise public-safe evidence paraphrases, evidence IDs, error codes, severity, and confidence. Do not perform missing-access, global-structure, density, item-assessment, scoring, or reporting work.

Use `parallel_candidate_audit_cli.py build-locator-worker`, `bind-publication`, and `validate-worker`. Preserve the complete private audit, receipt, worker state, worker manifest, and recovery ZIP under the recovery root before publication. Publish exactly `validation/locator-audit-worker.CHUNK-010.json` in one commit and one open, unmerged pull request. Do not publish private audit data, update canonical state or manifests, modify the benchmark repository, or merge the pull request.
```

## CHUNK-011 — 11. Government by Terror, 1793-1794

```text
@Evaluate Subject Index worker-locator-audit CHUNK-011 --project jcamden/subject-index-evaluation-oxford-history-french-revolution-2002-original-published-index

Resume the canonical evaluation in an isolated worker:

- Evaluation ID: oxford-history-french-revolution-2002-indexerlabs-truncated
- Candidate ID: oxford-history-french-revolution-2002-original-published-index
- Expected base branch: main
- Immutable base commit: 026697ecb56847a4df0c5d6272b5c2b249672d7f
- Benchmark project/ref: jcamden/subject-index-benchmark-oxford-history-french-revolution-2002 @ 98dbffd0ca171b5b7db76dbe1b2b5d5265ccacab
- Frozen benchmark canonical SHA-256: b925797fcab50b2008ad5974590e323f772e5ea7013efa84ce7606007439aeb3
- Source document SHA-256: 5f89aa2592218983c594278bfd86cc1e4b74be1dd6dd8aac5c2610a48fa34047
- Candidate identity SHA-256: 1d43fe7fb158b352393c6e2f14843aae9ae23ccfca1f61c6783307432b0a9d09
- Normalized candidate file SHA-256: 7b29d7716339038848e2b1b0ec17220ae1867cb95941f0f06a84488cd486ed79
- Item inventory file SHA-256: 3e9c2b20d49486398bd57bfa31f5d1da1743498b47d0b9e46e42f096b56b9934
- Policy v2 file SHA-256: bfb5ec9ab45b6719b8a36fa09f50dfb8d8c18b3f209bd153501173182695ac62
- Page-map canonical SHA-256: 452602deebdae19f8e35c589f2ff2a7a0b9fc955d268b14f760391b0043e9653
- Chunk-manifest canonical SHA-256: 5fc5450386114fdeb19838f54d3f1662c3d6dec81d4729c73f4f7ec0cb341a6f
- Candidate-benchmark-lock file/canonical SHA-256: 3272d5362d27ca3ab62e7a8ef5fb1cf838df269ce7892035dc5140450306cf65 / 16e26f3d50da64fb211aba44940425ccbb20dcfa74e6e5202986b36cc9344ea8

Import and fully validate this cumulative portable checkpoint from `/IndexPDF/subject-index-evaluations/oxford-history-french-revolution-2002-original-published-index/canonical-integration`:

- oxford-history-french-revolution-2002-indexerlabs-truncated-candidate-oxford-history-french-revolution-2002-original-published-index-locator-packets-checkpoint-portable.zip
- SHA-256: afaeaeff298b558b4f739ece1b4f0c459142fb510c791b59d1df7d219759b2f7

Worker scope:

- Chunk: CHUNK-011
- Chapter: 11. Government by Terror, 1793-1794
- Owned document pages: 247–271
- Locator packet: `candidate/oxford-history-french-revolution-2002-original-published-index/locator-packets/candidate-locator-CHUNK-011.json`
- Packet SHA-256: eed94135010e07c650627e0912e54e0df592335e7aa643ef3df961c7e5780bb7
- Expected locator assignments: 381

Before substantive work, retrieve these exact restricted artifacts from ChatGPT Library, materialize them at the evaluation-relative destinations, and hash-verify them:

- Library source: `/Subject Index Evaluations/Oxford History of the French Revolution 2002 - IndexerLabs truncated/source/chunks/CHUNK-011.pdf`
  - Materialize as: `source/chunks/CHUNK-011.pdf`
  - Required SHA-256: `1ccf98d94ddf7179f5a329405289af148e4d969a3471fea8ba06b1bfbfd6e701`
- Library source: `/Subject Index Evaluations/Oxford History of the French Revolution 2002 - IndexerLabs truncated/source/chunks/CHUNK-011.pages.json`
  - Materialize as: `source/chunks/CHUNK-011.pages.json`
  - Required SHA-256: `76bd6dbe287db97c2e7c9bb07da5d5646e5b7a4f4b8b7b2af07ab496248250bb`

If either restricted source artifact is unavailable or has a different hash, stop as blocked. Use the unique private recovery root `workers/locator-audit/CHUNK-011/`. Use branch `locator-audit/chunk-011`; refuse it if it already exists.

Audit every one of the 381 packet assignments exactly once. Preserve the complete heading path, judge only this chunk’s owned assignments, and use only `supported`, `partially_supported`, `unsupported`, or `uninspectable`. Record concise public-safe evidence paraphrases, evidence IDs, error codes, severity, and confidence. Do not perform missing-access, global-structure, density, item-assessment, scoring, or reporting work.

Use `parallel_candidate_audit_cli.py build-locator-worker`, `bind-publication`, and `validate-worker`. Preserve the complete private audit, receipt, worker state, worker manifest, and recovery ZIP under the recovery root before publication. Publish exactly `validation/locator-audit-worker.CHUNK-011.json` in one commit and one open, unmerged pull request. Do not publish private audit data, update canonical state or manifests, modify the benchmark repository, or merge the pull request.
```

## CHUNK-012 — 12. Thermidor, 1794-1795

```text
@Evaluate Subject Index worker-locator-audit CHUNK-012 --project jcamden/subject-index-evaluation-oxford-history-french-revolution-2002-original-published-index

Resume the canonical evaluation in an isolated worker:

- Evaluation ID: oxford-history-french-revolution-2002-indexerlabs-truncated
- Candidate ID: oxford-history-french-revolution-2002-original-published-index
- Expected base branch: main
- Immutable base commit: 026697ecb56847a4df0c5d6272b5c2b249672d7f
- Benchmark project/ref: jcamden/subject-index-benchmark-oxford-history-french-revolution-2002 @ 98dbffd0ca171b5b7db76dbe1b2b5d5265ccacab
- Frozen benchmark canonical SHA-256: b925797fcab50b2008ad5974590e323f772e5ea7013efa84ce7606007439aeb3
- Source document SHA-256: 5f89aa2592218983c594278bfd86cc1e4b74be1dd6dd8aac5c2610a48fa34047
- Candidate identity SHA-256: 1d43fe7fb158b352393c6e2f14843aae9ae23ccfca1f61c6783307432b0a9d09
- Normalized candidate file SHA-256: 7b29d7716339038848e2b1b0ec17220ae1867cb95941f0f06a84488cd486ed79
- Item inventory file SHA-256: 3e9c2b20d49486398bd57bfa31f5d1da1743498b47d0b9e46e42f096b56b9934
- Policy v2 file SHA-256: bfb5ec9ab45b6719b8a36fa09f50dfb8d8c18b3f209bd153501173182695ac62
- Page-map canonical SHA-256: 452602deebdae19f8e35c589f2ff2a7a0b9fc955d268b14f760391b0043e9653
- Chunk-manifest canonical SHA-256: 5fc5450386114fdeb19838f54d3f1662c3d6dec81d4729c73f4f7ec0cb341a6f
- Candidate-benchmark-lock file/canonical SHA-256: 3272d5362d27ca3ab62e7a8ef5fb1cf838df269ce7892035dc5140450306cf65 / 16e26f3d50da64fb211aba44940425ccbb20dcfa74e6e5202986b36cc9344ea8

Import and fully validate this cumulative portable checkpoint from `/IndexPDF/subject-index-evaluations/oxford-history-french-revolution-2002-original-published-index/canonical-integration`:

- oxford-history-french-revolution-2002-indexerlabs-truncated-candidate-oxford-history-french-revolution-2002-original-published-index-locator-packets-checkpoint-portable.zip
- SHA-256: afaeaeff298b558b4f739ece1b4f0c459142fb510c791b59d1df7d219759b2f7

Worker scope:

- Chunk: CHUNK-012
- Chapter: 12. Thermidor, 1794-1795
- Owned document pages: 272–296
- Locator packet: `candidate/oxford-history-french-revolution-2002-original-published-index/locator-packets/candidate-locator-CHUNK-012.json`
- Packet SHA-256: 724654f35a969ec71debf14853fc215da0acb21f4be1320e43ae13cd0dcb2709
- Expected locator assignments: 319

Before substantive work, retrieve these exact restricted artifacts from ChatGPT Library, materialize them at the evaluation-relative destinations, and hash-verify them:

- Library source: `/Subject Index Evaluations/Oxford History of the French Revolution 2002 - IndexerLabs truncated/source/chunks/CHUNK-012.pdf`
  - Materialize as: `source/chunks/CHUNK-012.pdf`
  - Required SHA-256: `adcc5f3733a4b4eae22148d711efe7799f5ab829b0896e8b61f90e0bd6a5084d`
- Library source: `/Subject Index Evaluations/Oxford History of the French Revolution 2002 - IndexerLabs truncated/source/chunks/CHUNK-012.pages.json`
  - Materialize as: `source/chunks/CHUNK-012.pages.json`
  - Required SHA-256: `1aae86ff378f6183aa249f64159ad6989faf4b2a670f99e943212e84c64c9fef`

If either restricted source artifact is unavailable or has a different hash, stop as blocked. Use the unique private recovery root `workers/locator-audit/CHUNK-012/`. Use branch `locator-audit/chunk-012`; refuse it if it already exists.

Audit every one of the 319 packet assignments exactly once. Preserve the complete heading path, judge only this chunk’s owned assignments, and use only `supported`, `partially_supported`, `unsupported`, or `uninspectable`. Record concise public-safe evidence paraphrases, evidence IDs, error codes, severity, and confidence. Do not perform missing-access, global-structure, density, item-assessment, scoring, or reporting work.

Use `parallel_candidate_audit_cli.py build-locator-worker`, `bind-publication`, and `validate-worker`. Preserve the complete private audit, receipt, worker state, worker manifest, and recovery ZIP under the recovery root before publication. Publish exactly `validation/locator-audit-worker.CHUNK-012.json` in one commit and one open, unmerged pull request. Do not publish private audit data, update canonical state or manifests, modify the benchmark repository, or merge the pull request.
```

## CHUNK-013 — 13. Counter-Revolution, 1789-1795

```text
@Evaluate Subject Index worker-locator-audit CHUNK-013 --project jcamden/subject-index-evaluation-oxford-history-french-revolution-2002-original-published-index

Resume the canonical evaluation in an isolated worker:

- Evaluation ID: oxford-history-french-revolution-2002-indexerlabs-truncated
- Candidate ID: oxford-history-french-revolution-2002-original-published-index
- Expected base branch: main
- Immutable base commit: 026697ecb56847a4df0c5d6272b5c2b249672d7f
- Benchmark project/ref: jcamden/subject-index-benchmark-oxford-history-french-revolution-2002 @ 98dbffd0ca171b5b7db76dbe1b2b5d5265ccacab
- Frozen benchmark canonical SHA-256: b925797fcab50b2008ad5974590e323f772e5ea7013efa84ce7606007439aeb3
- Source document SHA-256: 5f89aa2592218983c594278bfd86cc1e4b74be1dd6dd8aac5c2610a48fa34047
- Candidate identity SHA-256: 1d43fe7fb158b352393c6e2f14843aae9ae23ccfca1f61c6783307432b0a9d09
- Normalized candidate file SHA-256: 7b29d7716339038848e2b1b0ec17220ae1867cb95941f0f06a84488cd486ed79
- Item inventory file SHA-256: 3e9c2b20d49486398bd57bfa31f5d1da1743498b47d0b9e46e42f096b56b9934
- Policy v2 file SHA-256: bfb5ec9ab45b6719b8a36fa09f50dfb8d8c18b3f209bd153501173182695ac62
- Page-map canonical SHA-256: 452602deebdae19f8e35c589f2ff2a7a0b9fc955d268b14f760391b0043e9653
- Chunk-manifest canonical SHA-256: 5fc5450386114fdeb19838f54d3f1662c3d6dec81d4729c73f4f7ec0cb341a6f
- Candidate-benchmark-lock file/canonical SHA-256: 3272d5362d27ca3ab62e7a8ef5fb1cf838df269ce7892035dc5140450306cf65 / 16e26f3d50da64fb211aba44940425ccbb20dcfa74e6e5202986b36cc9344ea8

Import and fully validate this cumulative portable checkpoint from `/IndexPDF/subject-index-evaluations/oxford-history-french-revolution-2002-original-published-index/canonical-integration`:

- oxford-history-french-revolution-2002-indexerlabs-truncated-candidate-oxford-history-french-revolution-2002-original-published-index-locator-packets-checkpoint-portable.zip
- SHA-256: afaeaeff298b558b4f739ece1b4f0c459142fb510c791b59d1df7d219759b2f7

Worker scope:

- Chunk: CHUNK-013
- Chapter: 13. Counter-Revolution, 1789-1795
- Owned document pages: 297–317
- Locator packet: `candidate/oxford-history-french-revolution-2002-original-published-index/locator-packets/candidate-locator-CHUNK-013.json`
- Packet SHA-256: 736f3000827784c8556c46940e7673a5049e1217cd4a82d6f2967c6049092031
- Expected locator assignments: 274

Before substantive work, retrieve these exact restricted artifacts from ChatGPT Library, materialize them at the evaluation-relative destinations, and hash-verify them:

- Library source: `/Subject Index Evaluations/Oxford History of the French Revolution 2002 - IndexerLabs truncated/source/chunks/CHUNK-013.pdf`
  - Materialize as: `source/chunks/CHUNK-013.pdf`
  - Required SHA-256: `84e657a01aeee0c9857dbc8a2440d2560bf022489fbc239a6c82c6c11e49db8e`
- Library source: `/Subject Index Evaluations/Oxford History of the French Revolution 2002 - IndexerLabs truncated/source/chunks/CHUNK-013.pages.json`
  - Materialize as: `source/chunks/CHUNK-013.pages.json`
  - Required SHA-256: `9851fef1e66228487ec0e40b0e3815cd7545f32a5cb17fa160d077fe700db264`

If either restricted source artifact is unavailable or has a different hash, stop as blocked. Use the unique private recovery root `workers/locator-audit/CHUNK-013/`. Use branch `locator-audit/chunk-013`; refuse it if it already exists.

Audit every one of the 274 packet assignments exactly once. Preserve the complete heading path, judge only this chunk’s owned assignments, and use only `supported`, `partially_supported`, `unsupported`, or `uninspectable`. Record concise public-safe evidence paraphrases, evidence IDs, error codes, severity, and confidence. Do not perform missing-access, global-structure, density, item-assessment, scoring, or reporting work.

Use `parallel_candidate_audit_cli.py build-locator-worker`, `bind-publication`, and `validate-worker`. Preserve the complete private audit, receipt, worker state, worker manifest, and recovery ZIP under the recovery root before publication. Publish exactly `validation/locator-audit-worker.CHUNK-013.json` in one commit and one open, unmerged pull request. Do not publish private audit data, update canonical state or manifests, modify the benchmark repository, or merge the pull request.
```

## CHUNK-014 — 14. The Directory, 1795-1799

```text
@Evaluate Subject Index worker-locator-audit CHUNK-014 --project jcamden/subject-index-evaluation-oxford-history-french-revolution-2002-original-published-index

Resume the canonical evaluation in an isolated worker:

- Evaluation ID: oxford-history-french-revolution-2002-indexerlabs-truncated
- Candidate ID: oxford-history-french-revolution-2002-original-published-index
- Expected base branch: main
- Immutable base commit: 026697ecb56847a4df0c5d6272b5c2b249672d7f
- Benchmark project/ref: jcamden/subject-index-benchmark-oxford-history-french-revolution-2002 @ 98dbffd0ca171b5b7db76dbe1b2b5d5265ccacab
- Frozen benchmark canonical SHA-256: b925797fcab50b2008ad5974590e323f772e5ea7013efa84ce7606007439aeb3
- Source document SHA-256: 5f89aa2592218983c594278bfd86cc1e4b74be1dd6dd8aac5c2610a48fa34047
- Candidate identity SHA-256: 1d43fe7fb158b352393c6e2f14843aae9ae23ccfca1f61c6783307432b0a9d09
- Normalized candidate file SHA-256: 7b29d7716339038848e2b1b0ec17220ae1867cb95941f0f06a84488cd486ed79
- Item inventory file SHA-256: 3e9c2b20d49486398bd57bfa31f5d1da1743498b47d0b9e46e42f096b56b9934
- Policy v2 file SHA-256: bfb5ec9ab45b6719b8a36fa09f50dfb8d8c18b3f209bd153501173182695ac62
- Page-map canonical SHA-256: 452602deebdae19f8e35c589f2ff2a7a0b9fc955d268b14f760391b0043e9653
- Chunk-manifest canonical SHA-256: 5fc5450386114fdeb19838f54d3f1662c3d6dec81d4729c73f4f7ec0cb341a6f
- Candidate-benchmark-lock file/canonical SHA-256: 3272d5362d27ca3ab62e7a8ef5fb1cf838df269ce7892035dc5140450306cf65 / 16e26f3d50da64fb211aba44940425ccbb20dcfa74e6e5202986b36cc9344ea8

Import and fully validate this cumulative portable checkpoint from `/IndexPDF/subject-index-evaluations/oxford-history-french-revolution-2002-original-published-index/canonical-integration`:

- oxford-history-french-revolution-2002-indexerlabs-truncated-candidate-oxford-history-french-revolution-2002-original-published-index-locator-packets-checkpoint-portable.zip
- SHA-256: afaeaeff298b558b4f739ece1b4f0c459142fb510c791b59d1df7d219759b2f7

Worker scope:

- Chunk: CHUNK-014
- Chapter: 14. The Directory, 1795-1799
- Owned document pages: 318–340
- Locator packet: `candidate/oxford-history-french-revolution-2002-original-published-index/locator-packets/candidate-locator-CHUNK-014.json`
- Packet SHA-256: 3421b750bc01801c5afa968b0657813c10eeab18cb842666f5d015a89552ccfb
- Expected locator assignments: 301

Before substantive work, retrieve these exact restricted artifacts from ChatGPT Library, materialize them at the evaluation-relative destinations, and hash-verify them:

- Library source: `/Subject Index Evaluations/Oxford History of the French Revolution 2002 - IndexerLabs truncated/source/chunks/CHUNK-014.pdf`
  - Materialize as: `source/chunks/CHUNK-014.pdf`
  - Required SHA-256: `381e325c2092560623bf8df064bdf1f4c6dea16e296622c17010b9ca49d35c40`
- Library source: `/Subject Index Evaluations/Oxford History of the French Revolution 2002 - IndexerLabs truncated/source/chunks/CHUNK-014.pages.json`
  - Materialize as: `source/chunks/CHUNK-014.pages.json`
  - Required SHA-256: `69931f8ac03b3e62741bd23de5a17b2bc99f0d53857c7bb150517631a2c10e17`

If either restricted source artifact is unavailable or has a different hash, stop as blocked. Use the unique private recovery root `workers/locator-audit/CHUNK-014/`. Use branch `locator-audit/chunk-014`; refuse it if it already exists.

Audit every one of the 301 packet assignments exactly once. Preserve the complete heading path, judge only this chunk’s owned assignments, and use only `supported`, `partially_supported`, `unsupported`, or `uninspectable`. Record concise public-safe evidence paraphrases, evidence IDs, error codes, severity, and confidence. Do not perform missing-access, global-structure, density, item-assessment, scoring, or reporting work.

Use `parallel_candidate_audit_cli.py build-locator-worker`, `bind-publication`, and `validate-worker`. Preserve the complete private audit, receipt, worker state, worker manifest, and recovery ZIP under the recovery root before publication. Publish exactly `validation/locator-audit-worker.CHUNK-014.json` in one commit and one open, unmerged pull request. Do not publish private audit data, update canonical state or manifests, modify the benchmark repository, or merge the pull request.
```

## CHUNK-015 — 15. Occupied Europe, 1794-1799

```text
@Evaluate Subject Index worker-locator-audit CHUNK-015 --project jcamden/subject-index-evaluation-oxford-history-french-revolution-2002-original-published-index

Resume the canonical evaluation in an isolated worker:

- Evaluation ID: oxford-history-french-revolution-2002-indexerlabs-truncated
- Candidate ID: oxford-history-french-revolution-2002-original-published-index
- Expected base branch: main
- Immutable base commit: 026697ecb56847a4df0c5d6272b5c2b249672d7f
- Benchmark project/ref: jcamden/subject-index-benchmark-oxford-history-french-revolution-2002 @ 98dbffd0ca171b5b7db76dbe1b2b5d5265ccacab
- Frozen benchmark canonical SHA-256: b925797fcab50b2008ad5974590e323f772e5ea7013efa84ce7606007439aeb3
- Source document SHA-256: 5f89aa2592218983c594278bfd86cc1e4b74be1dd6dd8aac5c2610a48fa34047
- Candidate identity SHA-256: 1d43fe7fb158b352393c6e2f14843aae9ae23ccfca1f61c6783307432b0a9d09
- Normalized candidate file SHA-256: 7b29d7716339038848e2b1b0ec17220ae1867cb95941f0f06a84488cd486ed79
- Item inventory file SHA-256: 3e9c2b20d49486398bd57bfa31f5d1da1743498b47d0b9e46e42f096b56b9934
- Policy v2 file SHA-256: bfb5ec9ab45b6719b8a36fa09f50dfb8d8c18b3f209bd153501173182695ac62
- Page-map canonical SHA-256: 452602deebdae19f8e35c589f2ff2a7a0b9fc955d268b14f760391b0043e9653
- Chunk-manifest canonical SHA-256: 5fc5450386114fdeb19838f54d3f1662c3d6dec81d4729c73f4f7ec0cb341a6f
- Candidate-benchmark-lock file/canonical SHA-256: 3272d5362d27ca3ab62e7a8ef5fb1cf838df269ce7892035dc5140450306cf65 / 16e26f3d50da64fb211aba44940425ccbb20dcfa74e6e5202986b36cc9344ea8

Import and fully validate this cumulative portable checkpoint from `/IndexPDF/subject-index-evaluations/oxford-history-french-revolution-2002-original-published-index/canonical-integration`:

- oxford-history-french-revolution-2002-indexerlabs-truncated-candidate-oxford-history-french-revolution-2002-original-published-index-locator-packets-checkpoint-portable.zip
- SHA-256: afaeaeff298b558b4f739ece1b4f0c459142fb510c791b59d1df7d219759b2f7

Worker scope:

- Chunk: CHUNK-015
- Chapter: 15. Occupied Europe, 1794-1799
- Owned document pages: 341–368
- Locator packet: `candidate/oxford-history-french-revolution-2002-original-published-index/locator-packets/candidate-locator-CHUNK-015.json`
- Packet SHA-256: 8d7dd7e2b24cd3e758db4beec3fdab108f430642a481e09e7b72a6d0ab8e8816
- Expected locator assignments: 362

Before substantive work, retrieve these exact restricted artifacts from ChatGPT Library, materialize them at the evaluation-relative destinations, and hash-verify them:

- Library source: `/Subject Index Evaluations/Oxford History of the French Revolution 2002 - IndexerLabs truncated/source/chunks/CHUNK-015.pdf`
  - Materialize as: `source/chunks/CHUNK-015.pdf`
  - Required SHA-256: `7c4ed0ce7194d3e6cbc64cb4b2a09dd46872092840da5fe2c7afba446937f1f5`
- Library source: `/Subject Index Evaluations/Oxford History of the French Revolution 2002 - IndexerLabs truncated/source/chunks/CHUNK-015.pages.json`
  - Materialize as: `source/chunks/CHUNK-015.pages.json`
  - Required SHA-256: `f289a89749e60a58a78c7c7f0dfee21c8ca38910dfab17f1adfdc08675f409d8`

If either restricted source artifact is unavailable or has a different hash, stop as blocked. Use the unique private recovery root `workers/locator-audit/CHUNK-015/`. Use branch `locator-audit/chunk-015`; refuse it if it already exists.

Audit every one of the 362 packet assignments exactly once. Preserve the complete heading path, judge only this chunk’s owned assignments, and use only `supported`, `partially_supported`, `unsupported`, or `uninspectable`. Record concise public-safe evidence paraphrases, evidence IDs, error codes, severity, and confidence. Do not perform missing-access, global-structure, density, item-assessment, scoring, or reporting work.

Use `parallel_candidate_audit_cli.py build-locator-worker`, `bind-publication`, and `validate-worker`. Preserve the complete private audit, receipt, worker state, worker manifest, and recovery ZIP under the recovery root before publication. Publish exactly `validation/locator-audit-worker.CHUNK-015.json` in one commit and one open, unmerged pull request. Do not publish private audit data, update canonical state or manifests, modify the benchmark repository, or merge the pull request.
```

## CHUNK-016 — 16. An End to Revolution, 1799-1802

```text
@Evaluate Subject Index worker-locator-audit CHUNK-016 --project jcamden/subject-index-evaluation-oxford-history-french-revolution-2002-original-published-index

Resume the canonical evaluation in an isolated worker:

- Evaluation ID: oxford-history-french-revolution-2002-indexerlabs-truncated
- Candidate ID: oxford-history-french-revolution-2002-original-published-index
- Expected base branch: main
- Immutable base commit: 026697ecb56847a4df0c5d6272b5c2b249672d7f
- Benchmark project/ref: jcamden/subject-index-benchmark-oxford-history-french-revolution-2002 @ 98dbffd0ca171b5b7db76dbe1b2b5d5265ccacab
- Frozen benchmark canonical SHA-256: b925797fcab50b2008ad5974590e323f772e5ea7013efa84ce7606007439aeb3
- Source document SHA-256: 5f89aa2592218983c594278bfd86cc1e4b74be1dd6dd8aac5c2610a48fa34047
- Candidate identity SHA-256: 1d43fe7fb158b352393c6e2f14843aae9ae23ccfca1f61c6783307432b0a9d09
- Normalized candidate file SHA-256: 7b29d7716339038848e2b1b0ec17220ae1867cb95941f0f06a84488cd486ed79
- Item inventory file SHA-256: 3e9c2b20d49486398bd57bfa31f5d1da1743498b47d0b9e46e42f096b56b9934
- Policy v2 file SHA-256: bfb5ec9ab45b6719b8a36fa09f50dfb8d8c18b3f209bd153501173182695ac62
- Page-map canonical SHA-256: 452602deebdae19f8e35c589f2ff2a7a0b9fc955d268b14f760391b0043e9653
- Chunk-manifest canonical SHA-256: 5fc5450386114fdeb19838f54d3f1662c3d6dec81d4729c73f4f7ec0cb341a6f
- Candidate-benchmark-lock file/canonical SHA-256: 3272d5362d27ca3ab62e7a8ef5fb1cf838df269ce7892035dc5140450306cf65 / 16e26f3d50da64fb211aba44940425ccbb20dcfa74e6e5202986b36cc9344ea8

Import and fully validate this cumulative portable checkpoint from `/IndexPDF/subject-index-evaluations/oxford-history-french-revolution-2002-original-published-index/canonical-integration`:

- oxford-history-french-revolution-2002-indexerlabs-truncated-candidate-oxford-history-french-revolution-2002-original-published-index-locator-packets-checkpoint-portable.zip
- SHA-256: afaeaeff298b558b4f739ece1b4f0c459142fb510c791b59d1df7d219759b2f7

Worker scope:

- Chunk: CHUNK-016
- Chapter: 16. An End to Revolution, 1799-1802
- Owned document pages: 369–390
- Locator packet: `candidate/oxford-history-french-revolution-2002-original-published-index/locator-packets/candidate-locator-CHUNK-016.json`
- Packet SHA-256: f2043c1bd7714d9e016b90ca877daaf166d3d0ff97ff625bb00f624a25cc84fb
- Expected locator assignments: 314

Before substantive work, retrieve these exact restricted artifacts from ChatGPT Library, materialize them at the evaluation-relative destinations, and hash-verify them:

- Library source: `/Subject Index Evaluations/Oxford History of the French Revolution 2002 - IndexerLabs truncated/source/chunks/CHUNK-016.pdf`
  - Materialize as: `source/chunks/CHUNK-016.pdf`
  - Required SHA-256: `99e50a197f89a797538286f99cc276cdc32b3237e978d0e815b29146f624cda9`
- Library source: `/Subject Index Evaluations/Oxford History of the French Revolution 2002 - IndexerLabs truncated/source/chunks/CHUNK-016.pages.json`
  - Materialize as: `source/chunks/CHUNK-016.pages.json`
  - Required SHA-256: `645c8040bdca4f7717bd90497f417eb37e8469ae770dcdac4edc1cf5efd428fb`

If either restricted source artifact is unavailable or has a different hash, stop as blocked. Use the unique private recovery root `workers/locator-audit/CHUNK-016/`. Use branch `locator-audit/chunk-016`; refuse it if it already exists.

Audit every one of the 314 packet assignments exactly once. Preserve the complete heading path, judge only this chunk’s owned assignments, and use only `supported`, `partially_supported`, `unsupported`, or `uninspectable`. Record concise public-safe evidence paraphrases, evidence IDs, error codes, severity, and confidence. Do not perform missing-access, global-structure, density, item-assessment, scoring, or reporting work.

Use `parallel_candidate_audit_cli.py build-locator-worker`, `bind-publication`, and `validate-worker`. Preserve the complete private audit, receipt, worker state, worker manifest, and recovery ZIP under the recovery root before publication. Publish exactly `validation/locator-audit-worker.CHUNK-016.json` in one commit and one open, unmerged pull request. Do not publish private audit data, update canonical state or manifests, modify the benchmark repository, or merge the pull request.
```

## CHUNK-017 — 17. The Revolution in Perspective

```text
@Evaluate Subject Index worker-locator-audit CHUNK-017 --project jcamden/subject-index-evaluation-oxford-history-french-revolution-2002-original-published-index

Resume the canonical evaluation in an isolated worker:

- Evaluation ID: oxford-history-french-revolution-2002-indexerlabs-truncated
- Candidate ID: oxford-history-french-revolution-2002-original-published-index
- Expected base branch: main
- Immutable base commit: 026697ecb56847a4df0c5d6272b5c2b249672d7f
- Benchmark project/ref: jcamden/subject-index-benchmark-oxford-history-french-revolution-2002 @ 98dbffd0ca171b5b7db76dbe1b2b5d5265ccacab
- Frozen benchmark canonical SHA-256: b925797fcab50b2008ad5974590e323f772e5ea7013efa84ce7606007439aeb3
- Source document SHA-256: 5f89aa2592218983c594278bfd86cc1e4b74be1dd6dd8aac5c2610a48fa34047
- Candidate identity SHA-256: 1d43fe7fb158b352393c6e2f14843aae9ae23ccfca1f61c6783307432b0a9d09
- Normalized candidate file SHA-256: 7b29d7716339038848e2b1b0ec17220ae1867cb95941f0f06a84488cd486ed79
- Item inventory file SHA-256: 3e9c2b20d49486398bd57bfa31f5d1da1743498b47d0b9e46e42f096b56b9934
- Policy v2 file SHA-256: bfb5ec9ab45b6719b8a36fa09f50dfb8d8c18b3f209bd153501173182695ac62
- Page-map canonical SHA-256: 452602deebdae19f8e35c589f2ff2a7a0b9fc955d268b14f760391b0043e9653
- Chunk-manifest canonical SHA-256: 5fc5450386114fdeb19838f54d3f1662c3d6dec81d4729c73f4f7ec0cb341a6f
- Candidate-benchmark-lock file/canonical SHA-256: 3272d5362d27ca3ab62e7a8ef5fb1cf838df269ce7892035dc5140450306cf65 / 16e26f3d50da64fb211aba44940425ccbb20dcfa74e6e5202986b36cc9344ea8

Import and fully validate this cumulative portable checkpoint from `/IndexPDF/subject-index-evaluations/oxford-history-french-revolution-2002-original-published-index/canonical-integration`:

- oxford-history-french-revolution-2002-indexerlabs-truncated-candidate-oxford-history-french-revolution-2002-original-published-index-locator-packets-checkpoint-portable.zip
- SHA-256: afaeaeff298b558b4f739ece1b4f0c459142fb510c791b59d1df7d219759b2f7

Worker scope:

- Chunk: CHUNK-017
- Chapter: 17. The Revolution in Perspective
- Owned document pages: 391–425
- Locator packet: `candidate/oxford-history-french-revolution-2002-original-published-index/locator-packets/candidate-locator-CHUNK-017.json`
- Packet SHA-256: a0084e293860e8942b08f92b175105cf7c2587a8741644a850eb37083c793f85
- Expected locator assignments: 425

Before substantive work, retrieve these exact restricted artifacts from ChatGPT Library, materialize them at the evaluation-relative destinations, and hash-verify them:

- Library source: `/Subject Index Evaluations/Oxford History of the French Revolution 2002 - IndexerLabs truncated/source/chunks/CHUNK-017.pdf`
  - Materialize as: `source/chunks/CHUNK-017.pdf`
  - Required SHA-256: `26cc6541447d9175fb9ff8abc63f9e1ed63a6ea3c42f57b8f5e5c53a383071b2`
- Library source: `/Subject Index Evaluations/Oxford History of the French Revolution 2002 - IndexerLabs truncated/source/chunks/CHUNK-017.pages.json`
  - Materialize as: `source/chunks/CHUNK-017.pages.json`
  - Required SHA-256: `0d58ce5bc2a9e81e9c8adb53f2c44c9461abfbbfa70198300109dbed98079cbc`

If either restricted source artifact is unavailable or has a different hash, stop as blocked. Use the unique private recovery root `workers/locator-audit/CHUNK-017/`. Use branch `locator-audit/chunk-017`; refuse it if it already exists.

Audit every one of the 425 packet assignments exactly once. Preserve the complete heading path, judge only this chunk’s owned assignments, and use only `supported`, `partially_supported`, `unsupported`, or `uninspectable`. Record concise public-safe evidence paraphrases, evidence IDs, error codes, severity, and confidence. Do not perform missing-access, global-structure, density, item-assessment, scoring, or reporting work.

Use `parallel_candidate_audit_cli.py build-locator-worker`, `bind-publication`, and `validate-worker`. Preserve the complete private audit, receipt, worker state, worker manifest, and recovery ZIP under the recovery root before publication. Publish exactly `validation/locator-audit-worker.CHUNK-017.json` in one commit and one open, unmerged pull request. Do not publish private audit data, update canonical state or manifests, modify the benchmark repository, or merge the pull request.
```

