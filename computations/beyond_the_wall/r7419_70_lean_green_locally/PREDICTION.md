# r7419 ②: is a Lean file's workflow status visible to READ_INDEX, and can a local gate ask whether it is GREEN? Pre-registered by node 70 before reading the workflows (the commit time is the record)

The question has two halves, and each is answered by reading code and the API, not by argument.

| | prediction | refuted if |
|---|---|---|
| **G-a** `formalisation-*` workflows are visible to READ_INDEX's nightly artifact | **no**. READ_INDEX is built by tracing the Python receipts' runtime reads (`sweep_runner_reads.py` → `receipt_scope.py --emit`). A Lean build is neither a receipt nor run by that sweep, so no Lean file is an entry, and no workflow result is recorded anywhere in the index. | any `.lean` path, or any workflow conclusion, appears in the committed or the nightly index |
| **G-b** a LOCAL run can answer "is this Lean file under a GREEN workflow" from the tree alone | **no**. No committed file records a formalisation workflow's conclusion per commit. | such a record exists in the tree |
| **G-c** it can be answered with the API (CI or a seat with `gh api`) | **yes**: `actions/workflows/<f>/runs?head_sha=` gives the conclusion, and the workflow's `paths:` filter gives which files it covers | the workflows do not run on push or have no path filter that maps files to a workflow |
| **G-d** the cheap way to make it locally answerable | a committed record written by the workflow itself, or by a seat from the API, keyed by commit and blob, and read the way `check_index_coverage` reads the index | — (a proposal, not scored) |

EFFORT: `25` min (`10`–`60`).
