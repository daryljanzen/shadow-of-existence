# r7141+70.1: pre-registration for the CANNOT-FAIL ratchet gate and its baseline (`r7141`)

*This is committed before the gate or the baseline is written. It was read at `origin/main` `1add89bd`.*

## The items owed, with a state against each

| item | source | state at this commit |
|---|---|---|
| draft `check_cannot_fail.py` and `cannot_fail_baseline.tsv` in the shape of the prose and quote ratchets: fail on a new site, a stale entry, or a rise in the owed count, and on nothing else | `r7141` | pre-registered here |
| the five class names as verdict names; `SCOPE-AS-CHECK` for T2; the `P14` diagonal skip as the first `NOT-A-DEFECT` row; T5 reported-not-enforced inside the baseline | `r7141` | pre-registered here |
| the ceiling written from what is measured on the tree drafted against, not from `95` | `r7141` | pre-registered here |
| T2's concentration: name whose pass it is, and whether it is pre-split | `r7141` | pre-registered here |
| the gate's class statement corrected twice; T3 repaired on its own receipts | `r7141` | noted; nothing owed |

## Design, fixed now

- **The key is (receipt, class, normalised site text), with a COUNT.**
  - Ten bare `True` verdicts in one receipt are one key with count 10, not ten keys.
  - **A line-number key goes stale on any edit, and an occurrence-index key churns on any deletion above it.** A count does neither.
- **Fails on exactly three things:**
  1. a live count above its baseline count, or a key not in the baseline: **NEW**;
  2. a live count below its baseline count, or a baseline key with no live site: **STALE** (lower the row);
  3. the **owed** count rising above a ceiling declared in the gate.
- **Owed** = every class except `CONSTANT` (T2c, ruled deliberate at `r7119`), `NOT-A-DEFECT`, and `UBIQUITOUS-ARM` (T5, reported, not enforced).
  - **T5 rows are in the baseline and printed, but a new T5 site does not fail,** as `REGRID` sits beside `TILT`.
- **The verdict names:**

  | verdict | covers |
  |---|---|
  | `TAUTOLOGY` | T1 |
  | `SCOPE-AS-CHECK` | T2 |
  | `CONSTANT` | T2c |
  | `TRIVIAL-ENV` | T3 |
  | `GUARDED-TRUE` | T4 |
  | `UBIQUITOUS-ARM` | T5 |
  | `NOT-A-DEFECT` | `P14`'s diagonal skip |

- **Same as at `r7125`:** drafted in this directory, written to run unchanged from `corpus/`, and **not added to `gates.yml`; that is the gate's registration to make.** The operator's `--cannot-fail` output is the interface the gate parses.

## Predictions

- **The count on this tree:** 95 sites, which you measured after the T3 repairs.
  - **Prediction:** 95, T3 = 0.
  - **I measured 95 just now at `1add89bd`, before writing this**, so this one is a check, not a prediction. *Stated so it is not counted as a hit.*
- **The owed count (the ceiling):** 95 − 20 constant − 2 ubiquitous − 1 not-a-defect = **72**. *If it differs, the ceiling is what is measured.*
- **Gate cost:** under 15 s (the operator's 9 s plus parsing). **It fits the fast list.**
- **Seeds:** a scratch copy of one receipt with one extra `check(True, …)` must fail as NEW; one with a `True` removed must fail as STALE; the unchanged tree must pass.
- **T2's authorship:** the 50 in `P10_canonical_time`, by `git log --diff-filter=A` on each file and its revision tag.
  - **Prediction:** **one line's** pass (a single `r70xx+…` family), not a sweep across seats.
  - ⚠ *Whether it is "pre-split" I read from the revision tags. I do not guess it.*
