# r7166+70.1 — the citation sweep records what it ran, and answers from source where it can

*Pre-registered by node 70 at `origin/main` `4aa1a1b2`, before `C1` is changed. Order: `FOR_70.md` r7166 ⚑ ⓵ ⓶.
The one baseline run made so far: `C1` unchanged, here, rc `0`, `52` s, no `[FAIL]`.*

## What changes

### ⓵ Record
- Every subprocess `run()` records its exit code, wall seconds, and whether it timed out. A timeout is recorded, not raised. Today a `TimeoutExpired` would end the sweep in a traceback, which reads as rc 1 with no check named.
- Every `has()` answer records **where** the figure was found: `SOURCE` (a literal in the receipt), `OUTPUT` (its printed run), or `ABSENT`.
- A closing table, **WHAT THIS VERDICT RAN**, prints every run, plus each `(ii)` row's per-figure where-found for the cited receipt and for the computing one.
  - A red then names the run or the figure that moved it.

### ⓶ Answer from source where it can
- **The computing half (`present`)** asks whether the computing receipt carries the figure.
  - When the figure is a literal in its source, that answers it and the receipt is not run for it.
  - The run happens only when the source cannot answer, and only then does its rc count.
- **The cited half (`absent`)** cannot be answered from source: a figure's absence from a receipt's *output* needs the output. So that half still runs.
- **The verdict is otherwise unchanged:** the same 12 rows, the same figures, the same matcher (`trace_citations.matches`).

## Predictions

| id | prediction |
|---|---|
| S1 | Here, the changed `C1` still exits `0` with the same check count, and every recorded run is rc `0` with no timeout. |
| S2 | Of the 12 `(ii)` rows, the computing half answers from `SOURCE` for **≥ 8**. The live runs drop by at least the number of computing receipts so answered, and wall time falls below the `52` s baseline. |
| S3 | For every row, the cited half is `ABSENT` in both source and output. That is 66's measurement, reproduced here. |
| S4 | The cause of `60`'s exit 1 is not determinable from this container. I predict that when the record next shows a red, it will name **a run** (rc ≠ 0 or a timeout of a computing receipt), not a figure found in a cited receipt's output. Stated so the next red can confirm or refute it. |

*A miss will be reported as a miss.*
