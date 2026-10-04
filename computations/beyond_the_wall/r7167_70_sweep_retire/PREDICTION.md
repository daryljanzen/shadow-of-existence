# r7167+70.1 — `C1` retires a finding by reading what its repair must change

*Pre-registered by node 70 at `origin/main` `b75cf145`, before `C1` is changed. Order: `FOR_70.md` r7167 ⚑ ⓵ ⓶ (and ⓷ as calibration).*

## The rule (66's general form: retire by reading what the repair MUST change)

A `(ii)` / `(iii)` finding is **RETIRED** when either of these holds, both read from the paper's source with no run:
- **`RETIRED-DRIFTED`:** the row's paper prints none of the finding's figures any more.
- **`RETIRED-CITED`:** for every figure the paper still prints, at least one printed occurrence has the computing receipt in its *closing group*.
  - The closing group is the first `\rcpt` group after the occurrence: adjacent markers separated only by whitespace or punctuation, as the tracer groups them.
  - It is searched up to the next sectioning command, **with no fixed character window** (66's ⓷).

Otherwise the finding is **LIVE**, and only a LIVE finding runs its property test (absent from the cited receipt, present in the computing one) and the receipts that test needs. A RETIRED finding runs nothing.

## Self-test inside the receipt (so the rule is not hollow)

A synthetic paper, independent of the corpus, must classify three ways:
1. a figure closed by a group naming the computing receipt → `RETIRED-CITED`;
2. the same text with that marker removed → `LIVE`;
3. the figure deleted → `RETIRED-DRIFTED`.

## Predictions

| id | prediction |
|---|---|
| T1 | Of the 12 `(ii)` markers (13 table rows: the refit passage is one marker with two computing receipts): **11 `RETIRED-CITED` and 1 `RETIRED-DRIFTED`** (`221.95` / `0.7354`). The `(iii)` is `RETIRED-DRIFTED` (P10 no longer prints `2.8e-4` / `5.9e-6`). **0 LIVE.** |
| T2 | 66's four hand reads (closing groups at `+140`, `+446`, `+516`, `+1429` characters) all come out `RETIRED-CITED` under the no-window rule. A fixed 300-character window, computed as a reported control, would call **at least 3** of them open. |
| T3 | With every finding retired, `C1` runs **0** other receipts. Its wall time falls from 33 s to under 10 s, and the `camb` dependency 60 found no longer touches the verdict. |
| T4 | Seeds in a throwaway worktree, with the real corpus: removing the computing receipt's marker from one row's closing group turns that row **LIVE**, and its property test then runs and passes. Deleting the paper's figure turns it **RETIRED-DRIFTED**. |
| T5 | ⓶ The host dependency is declared in the header as one line: the `(ii)` property test runs other receipts, so a missing module in the running environment can turn a LIVE row red with no change to the tree. |

*A miss will be reported as a miss.*
