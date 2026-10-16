# r7423+70: RESULT. `refs/ci/lean` is written by push runs and read GREEN for both projects, in agreement with the API. A stale record never reads GREEN. The `scope-reads` seeded probe runs first in CI and fires two-sidedly.

Registration `a96a45065` (15:01:56 UTC); the build landed at `r7423+70.2` (`e3bf08dbb`).

## ③ `refs/ci/lean/<workflow>`

| | prediction | measured | verdict |
|---|---|---|---|
| **L-a** the reader on the branch HEAD reads GREEN for both workflows and agrees with `green_under.py` | GREEN, agree | **GREEN, GREEN**: mathlib record `5b9578ea0` (run `38920942324`), physlib record `2c51a101c` (run `38920942448`), both written by the push runs at `e3bf08dbb`. `green_under.py` (API) reads **SUCCESS, SUCCESS** at the same commit. | **HOLDS** |
| **L-b** ⛔ a stale record never reads GREEN | UNANSWERABLE | **UNANSWERABLE** for a lone stale success. A stale success *newer* than a matching failure does not mask the failure: NOT-GREEN. | **HOLDS** |
| **L-c** a matching failure reads NOT-GREEN | NOT-GREEN | **NOT-GREEN**, and the newest matching record wins over an older success | **HOLDS** |
| **L-d** fetch failure or no ref | UNANSWERABLE | **UNANSWERABLE**: before the first write, `couldn't find remote ref`; locally, a missing chain | **HOLDS** |
| **L-e** a matching cancelled record is skipped | the next record decides | **skipped**: cancelled over success reads GREEN; cancelled alone reads UNANSWERABLE | **HOLDS** |
| **L-f** a pull_request run writes nothing | 0 | **0**: both PR runs at `e3bf08dbb` succeeded, and each chain holds exactly one record, the push run's | **HOLDS** |

The local probes are in `READER_PROBES.txt` (8 of 8). They ran through `lean_record.status` itself on chains under
`refs/ci/lean-probe/*`, which were built with the writer's plumbing and deleted afterwards.

## r7421 ②: the seeded probe

| | prediction | measured | verdict |
|---|---|---|---|
| **R-a** seed 1 (the most-traced read, `corpus/CR_cosmology.tex`) scopes | ≥ 1 | **209**, and all 185 receipts that trace it are among them | **HOLDS** |
| **R-b** seed 2 (`scripts/_touched_pin_readers.py`, a member of the most-shared glob `scripts/*`) | ≥ 1 | **270** | **HOLDS** |
| **R-c** control | 0 | **0** | **HOLDS** |
| **R-d** wall here | `1`–`15` s | **0.3 s** | **REFUTED LOW**: `load()` is cached and the three `scope()` calls are set operations |
| **R-e** runs, and prints, before the real scope in CI | yes | **yes**: `scope-reads` job `117040948403` printed 209 / 270 / 0 at 15:08:31.93, then scoped the real range at 15:08:32: 0 receipts, 8 paths changed, 0 deleted or renamed | **HOLDS** |

**Both failure directions are shown** (`PROBE_RUN.txt`). With a broken selector that returns nothing, and with an
over-firing selector that returns everything, the probe exits 1. So the step cannot pass on a selector that is
wrong in either direction.

**The job's red on this push is not the probe's and not this PR's.** It is `corpus/check_formalisation_join.py`,
60's gate, carried by `red_carry`. It has been red on `main` since `d9d52886f`, with 7 dangling `decl` references
in `ROWS.tsv`. This push's own reads scope was 0.

The local fast job is green with all of this in it (`run_fast_job.sh`, exit 0).

EFFORT: `90` min registered; **≈ 45 min** measured (15:02 → ~15:47 UTC, about half of it waiting on CI). Inside
the band.
