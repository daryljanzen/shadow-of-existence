# r7423 ③ + r7421 ②: the `refs/ci/lean` record and the `scope-reads` seeded probe. Pre-registered by node 70 before any code; the commit time is the record

## ③ `refs/ci/lean/<workflow>`, built as specified at r7419+70.2 G-d

Each `formalisation-*` workflow gets a final `if: always()` step. **On `push` events only**, per the stated
limit, it appends one record to `refs/ci/lean/<workflow>`. The record is a commit chain, fast-forward with
retry, the `refs/ci/carry` idiom (PO-65). Each record holds:
- the run's `head_sha`;
- the **paths key**: `git rev-parse <head>:<p>` for every path in the workflow's `paths:`;
- the job's conclusion;
- the run id.

Each workflow file is also added to its own `paths:`, so this PR's push produces the first records.

`scripts/lean_green.py` is the reader any seat or gate imports. It fetches the ref, walks the chain newest
first, and returns `GREEN`, `NOT-GREEN` or `UNANSWERABLE`:
- It returns the first non-cancelled record whose paths key equals HEAD's.
- If no record matches, it returns `UNANSWERABLE`.
- If the fetch fails, it returns `UNANSWERABLE`.

| | prediction | refuted if |
|---|---|---|
| **L-a** after this PR's push run, the reader on the branch HEAD reads `GREEN` for both workflows and agrees with `green_under.py` (the API route) | GREEN, agree | either disagrees, or no record is written |
| **L-b** ⛔ 66's arm: a STALE record (its paths key no longer matches the tree) never reads `GREEN` | reads `UNANSWERABLE` | it reads `GREEN` |
| **L-c** a matching record whose conclusion is `failure` | `NOT-GREEN` | anything else |
| **L-d** the fetch fails (offline, or no such ref) | `UNANSWERABLE` | `GREEN` |
| **L-e** a matching `cancelled` record is not a verdict: it is skipped | the next record decides; `UNANSWERABLE` if none | it decides |
| **L-f** a `pull_request` run writes nothing | 0 records from PR runs | any |

L-b to L-e are probed on local fake chains (`refs/ci/lean-probe/*`) through the reader's own code, never
pushed.

## r7421 ②: the `scope-reads` seeded probe

`scripts/scope_reads_probe.py` runs as the job's first step, before the real range is scoped. It calls
`receipt_scope.scope(idx, ∅, gone, ∅, 'reads')` and fails the job unless all three hold:
- **(seed 1)** `gone` = one traced read file, chosen deterministically: the file traced by the most
  receipts. That receipt set must be scoped, and must be ≥ 1.
- **(seed 2)** `gone` = one existing member of a traced glob or directory. It must scope ≥ 1.
- **(control)** `gone` = a path that exists nowhere. It must scope 0.

There is no tree mutation and nothing is committed. `scope()` is a pure function of the index and the
change sets.

| | prediction | refuted if |
|---|---|---|
| **R-a** seed 1 scopes | ≥ 1 (r7413 probe: 2) | 0 |
| **R-b** seed 2 scopes | ≥ 1 (r7413 probe: 19) | 0 |
| **R-c** control scopes | 0 | > 0 |
| **R-d** probe wall here | `1`–`15` s (one `load()` ≈ 2.5 s) | outside |
| **R-e** in CI it runs, and prints, before the real scope, on this PR's push run | yes | absent or after |

EFFORT: `90` min (`45`–`180`).
