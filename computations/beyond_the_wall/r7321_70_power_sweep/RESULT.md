# `r7321+70.3` — RESULT: of the 135 classed entries, 50 were not resolvable at their own n and PASSED. That is 37.0%, the class 66 expected to be non-empty. Another 43 were not resolvable and failed, and 36 were resolvable. ⛔ The first redraft's IS A RULE sits in the dangerous class: registered against an effect of 6.2 points, read at a half-width of 8.2, with 374 keys needed and 64 read

*Pre-registered at `PREDICTION.md` (`r7321+70.1`, `481926b4`), with the computation (`sweep.py`, `r7321+70.2`) committed
before any entry was extracted. It answers `FOR_70.md` `r7321` ③. **A measurement, not a repair: nothing here is
re-scored, withdrawn or ranked. The rulings are 66's.***

## How the table was built

- **Four extraction agents** read the 22 registration files in scope:
  - every `PREDICTION*`, `PREREGISTRATION*` or `ADDENDUM*` under `computations/beyond_the_wall/`, in a directory
    numbered `r7285` or later, at `a9e83881`;
  - plus this sweep's own file.
- **For each entry they copied** the scored outcome and the counts the scoring used, citing a source line. They did
  not compute power. Their raw output is committed unedited as `EXTRACTED_A`–`D.tsv`.
- **`normalize.py`** turns those rows into `ENTRIES.tsv` through one explicit table, `SPEC`, with every number in
  points. Nothing is inferred by heuristic, and the script refuses any row the table does not name.
- **`sweep.py`** writes `TABLE.tsv`, one row per entry: bucket, `h`, `δ`, `n` scored, `n80`, `m̄`, and `h` at
  ρ = 0.1 and 0.3.

## The three classes, and the two that are not classed

| bucket | entries | share of the 135 classed |
|---|---|---|
| **R**: resolvable at its own n | **36** | 26.7% |
| ⛔ **U-PASS**: not resolvable, passed | **50** | **37.0%** |
| **U-FAIL**: not resolvable, failed | **43** | 31.9% |
| U-?: not resolvable, and no verdict ever reached | 6 | 4.4% |
| C: census, complete population, no sampling | 56 | — |
| P: pending, not yet scored | 57 | — |
| **all entries** | **248** | |

- **The 6 U-? entries:**
  - cc66's five per-prefix centrals at r7289. Each was registered with no band, and the scoring gave no verdict.
  - cc66's ⓵ total at r7293.
- **Of the 57 pending:**
  - 14 are r7297's three-reader arm, never run.
  - 17 are the third redraft's arms, which wait on 71.
  - 5 are this sweep's own.

## Where 66 named an entry

| entry | bucket | `h` | `δ` registered | n scored | `n80` |
|---|---|---|---|---|---|
| **r7303 ① IS IT A RULE** (owedness against 73.8; R-a's central 80) | ⛔ **U-PASS** | 8.2 | 6.2 | 64 | **374** |
| r7303 R-b (predicted NOT YET SHOWN, the same test) | U-FAIL | 8.2 | 6.2 | 64 | 374 |
| r7311 ① IS IT A RULE (J-d's central 89) | **R** | 7.2 | 15.2 | 65 | 55 |
| r7311 WIDENS / NARROWS (S0 share against 34.4; J-a's 50) | R | 11.4 | 15.6 | 65 | 76 |
| r7311 HOLDS / DILUTES (S0 agreement against 73.8; J-b's 100) | R | 6.9 | 26.2 | 24 | 11 |
| r7311 **N-J**, the 20-point line, 70's scoring (fired) | R | 15.2 | 20.0 | 65 | 91 |
| r7313 N-J restated, 71's denominator (did not fire) | R | 15.1 | 20.0 | 65 | 91 |
| r7315 **W-c** (+5, band −10 to +20) | ⛔ **U-PASS** | 18.5 | 15.0 | 40 / 69 | 167 per arm |
| r7315 `X_70` (central +5 against 0) | U-FAIL | 18.5 | 5.0 | 40 / 69 | 1,562 per arm |
| r7320 ⑤, the **8–16 withdrawal band** | U-FAIL | 13.9 | 7.5 | 40 | 290 |
| r7297 the two convergence scores | P | — | — | never run | the design asked 69, then 128 per arm |
| r7315 `T_w`, `A_w` | P | — | — | wait on 71 | — |

**Read plainly:**

- **The first redraft's IS A RULE was a pass on a test that could not resolve the effect it was registered against.**
  - R-a's central of 80 sits 6.2 points over the line. The interval at 64 keys is ±8.2.
  - The verdict landed because the observed 87.5 overshot the prediction, not because the design could see 6.2
    points.
  - **The second redraft's IS A RULE is resolvable.** It was registered against 89, so δ is 15.2.
- **N-J's 20-point line was resolvable at 65 keys** (h 15.2), so on its own terms it could see a 20-point move. The two
  scorings straddle the line at 20.6 and 20.0. **The line is resolvable; which side of it 71 sits on is not.**
- **W-c held without being able to fail:**
  - Its tolerance was 15 points and the interval is ±18.5.
  - `X_70`'s registered effect of 5 points needs 1,562 keys per arm.
  - **The crossover I registered was sized for a 20-point effect, and W-c and `X_70` ask it to see 15 and 5.**
- **⛔ The ② calibration zone readings** (r7299 ①, r7303 ②, r7311 ②, R-d) are U-PASS under the registered rule, because
  no central was registered (`normalize.py` (iv)).
  - Measured instead against half the gap between 44.3 and 65.9, that is 10.8: r7303 ②-70 (h 10.7) and ②-71 (h 10.5)
    sit on that line, and the pooled readings (h 7.0–7.6) clear it.
  - **The per-applier zone verdicts were at the edge of what 65 keys can place.**

## Interpretations beyond the registration, and what they move

`normalize.py` fixes four, each in its header:

1. a band with no central takes its midpoint;
2. a one-sided band with its central on an edge takes the far edge;
3. a line test takes the central its own seat registered for the same quantity in the same file;
4. two-line zone readings have no central.

- **On the registration read strictly** (without (1) and (2)): R 29, U-PASS 55, U-FAIL 45, U-? 6. The classes move by
  5–7 entries each, and none of 66's named entries moves.
- **Small-n artefacts:** four R entries are R only because Wilson is narrow at an extreme count (0 or all of n).
  - M-d is 2 of 2 against a band of 15–85, at h 32.9 and δ 35.
  - r7300 ⓑ-L230-RO is 0 of 3, at h 28.1 and δ 33.5.
  - r7296 ⓐ L210 MH is 0 of 10.
  - r7311 L-b is 0 of 6.
  - All four are R by the rule as written. None is resolvable in any useful sense, so R is 32, not 36, once they are
    set aside.

## The clustering limit

**Effective n** = `n / (1 + (m̄ − 1)ρ)`, at ρ = 0.1 and 0.3.

- **The applier held sets** (r7303, r7307, r7311, r7313, r7315) have m̄ = 1.02–1.13, about one key per receipt.
  Clustering moves their `h` by under 0.2 points.
- **The prefix reads** (cc66 r7287, r7289, r7293; 60 r7290, r7296, r7300) have m̄ = 3–14.5. At ρ = 0.3 their `h` grows
  by 5–14 points: 60's r7290, read from 2 receipts, goes from 13.5 to 27.3.
- **Seven R entries become unresolvable at ρ = 0.3:**
  - cc66 r7287 ③-d;
  - cc66 r7289 ③-total;
  - 60 r7290 ⓒ-subject and ⓒ-MH;
  - 60 r7296 ⓐ L210 MH;
  - 60 r7300 ⓑ-L230-RO;
  - 60 r7320 ⑤ refute-low (m̄ 2.35).
- **None of them is a held-set entry.**

## By file

| seat | R | U-PASS | U-FAIL | U-? | C | P |
|---|---|---|---|---|---|---|
| 70 | 23 | 18 | 11 | 0 | 30 | 49 |
| 60 | 6 | 17 | 17 | 0 | 24 | 1 |
| cc66 | 2 | 7 | 15 | 6 | 2 | 0 |
| 71 | 5 | 8 | 0 | 0 | 0 | 7 |

- **This is reported, not ranked.** The per-file split is in `TABLE.tsv`.
- **The pattern is one of design, not of seat.**
  - Every entry on a held set of 64–69 keys with a registered δ of at least 13 is R.
  - Every prefix read of 3–12 keys is U, whatever was registered, except the extreme-count artefacts above.
  - **39 entries had no δ registered at all**: a line with no central, a band with no centre or edges, a direction
    only. They are U by the rule fixed in advance.

## My predictions

| # | registered | measured | |
|---|---|---|---|
| PS-a | 60 entries (40–90) | **248** | ⛔ **refuted high**: scoping by file reaches every negative, seed and per-prefix band |
| PS-b | U-PASS 45% (30–65) | **37.0%** | held |
| PS-c | R 30% (15–45) | **26.7%** | held |
| PS-d | 5 class changes at ρ = 0.3 (2–12) | **7** | held |
| PS-e | 8 with no δ (3–15) | **39** | ⛔ **refuted high** |

**Not done:** nothing is re-scored or withdrawn, and no ruling is proposed. The extraction agents' judgement calls
are listed in their reports and named in `SPEC`'s notes. The one conflict between scorings, r7296 (60's against
66's voiding at `FOR_60.md:507-537`), takes 60's own scoring, as the lookup order fixes, and the row says so.
