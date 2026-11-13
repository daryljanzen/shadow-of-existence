# E5 — The anticipation gap: RESULT

**Headline.** A cold reviewer's valid findings are mostly ones the author did not anticipate. P1 holds: about 41% were anticipated, so 59% were new. Showing the reviewer the brief changes nothing. Showing the reviewer the author's own list of expected critiques raises the anticipated share (A) mainly because the reviewer now also echoes that list. The number of new valid findings per review does not fall significantly. **Under the registered co-primary (`r7750` amendment), "contamination closes the gap" (P2) is not established.** P3 is not supported.

- **Run:** 2026-11-13, `claude-opus-5-5`, 30 briefs.
  - Each brief has 1 author document and 3 reviewer levels × 2 replicates, so 180 reviews.
  - Each review then has a blind extraction and a blind matching pass.
  - 570 calls, 0 failed, about $42 at list price (`../USAGE.tsv`).
- **Secondary passes:** 300 calls, about $9.43.
- **Records:**
  - main run: `runs_main/`, `extract_main/`, `match_main/`;
  - secondary passes: `handling_main/`, `found_main/`, `raised_main/`;
  - analysis: `analyse_e5.py` and `analyse_e5_secondary.py`;
  - hand-check: `handcheck/`.

## n

- **The registered rule:** from the pilot's per-document SD of R2 − R0 in A (σ = 0.189), n = (2.8σ/0.15)² = 12.4 ≤ 30, so the main run uses the 30 briefs.
- **The main run's own σ** is 0.251, which gives n = 21.9. That is still ≤ 30, so the contrast is powered as registered.

## Results (per level; replicates averaged per document; 95% bootstrap over 30 documents)

| | R0 (document only) | R1 (+ brief) | R2 (+ brief + author's expected critiques) |
|---|---|---|---|
| **A** (anticipated / valid) | **0.409** [0.349, 0.471] | 0.405 [0.349, 0.463] | **0.595** [0.531, 0.655] |
| **Novel valid findings per review** (co-primary) | **5.82** [5.20, 6.40] | 5.02 [4.48, 5.53] | **5.33** [4.68, 6.00] |
| Valid findings per review (A's denominator) | 9.87 | 8.57 | 13.97 |
| Valid anticipated per review (A's numerator) | 4.05 | 3.55 | 8.63 |
| Findings extracted per review | 11.6 | 10.1 | 15.7 |

**Paired contrasts:**

| | R1 − R0 | R2 − R0 |
|---|---|---|
| A | −0.004 [−0.079, +0.066] | **+0.186 [+0.095, +0.275]** |
| Novel valid | **−0.80 [−1.47, −0.08]** | −0.48 [−1.28, +0.35] |
| Valid | −1.30 [−1.97, −0.60] | +4.10 [+2.68, +5.57] |

## Against the registration

- **P1 (in R0, A ≤ 0.5): holds.** A = 0.41, with the interval wholly below 0.5. More than half of a cold reviewer's real findings were new to the author.
- **P2 (A rises R0 < R1 < R2, with the R2 − R0 interval excluding 0; read through the co-primary): not established.**
  - A does not rise from R0 to R1. It does rise at R2, and that interval excludes 0.
  - But the registered reading requires novel valid findings to fall from R0 to R2, and they do not significantly fall (−0.48, interval includes 0).
  - **A rises at R2 because its numerator doubles (4.05 → 8.63) while the denominator grows by 4.1.** R2 reviewers raise the author's anticipated points in addition to roughly the same number of new ones. They do not raise fewer new ones.
  - This is the case the amendment was written for.
- **P3 (novel valid findings fall R0 → R2): not supported.**
- **One registered contrast moved that no prediction named:** R1 (the brief added) lowers both novel valid findings (−0.80, interval excludes 0) and valid findings (−1.30). A reviewer given the brief finds fewer problems of any kind. A is unchanged.
  - **This contrast is not robust to the validity threshold** (60, `r7758`). Its interval clears 0 by 0.08, while the threshold shifts novel findings by 0.8 to 1.3 per level. On the hand-checked sample it halves, from about −0.4 under the matcher's coding to about −0.2 under the hand coding. **No paper sentence should quote it without that caveat.**

## Secondaries (registered, built at `r7755` as blind scorer passes; see deviations)

- **(b) Complications the author mishandled, and whether reviews found them.**
  - The author's document handled 108 of the 120 seeded complications and mishandled 12, spread over 10 documents.
  - The share of those 12 a single review found: R0 0.45 [0.25, 0.65]; R1 0.58 [0.28, 0.88]; R2 0.60 [0.30, 0.85].
  - **At n = 10 documents the intervals overlap fully.** No level difference can be read from this.
- **(c) The author's anticipations that no reviewer raised.**
  - R0: 0.52 [0.46, 0.58]; R1: 0.58 [0.51, 0.65]. **About half of what the author expected a careful reviewer to say, no cold reviewer said.** The anticipation is as much a list of things the reply did not need as a forecast of it.
  - R2: 0.15. Its reviewers were shown the list, so this mostly measures echo. R0 is the reading of record, as registered.

## The hand-check (registered at `r7755`, after the aggregate was read)

**What was checked.** 36 of the 180 match records (R0 11, R1 11, R2 14; seed 5755), 443 findings. I scored them blind to level and to the matcher's judgements, and committed my scores (`c5878a445`) before `KEY.json` was opened.

- **Anticipated: κ = 0.88** (agreement 94.1%). By level: R0 0.82, R1 0.90, R2 0.91. The judgement that A's numerator and the co-primary rest on holds up.
- **Valid: κ = 0.07** (agreement 86.5% against chance 85.4%). This does not hold up as an agreement statistic.
  - **The direction:** 60 disagreements, 58 of which the matcher marked invalid where I marked valid. I marked 438 of the 443 findings valid; the matcher marked 382.
  - **What the matcher rejects:** findings that are defensible but weak, such as a word-count overrun, "it is unclear whether…", or a data vintage not stated. **The two of us apply different thresholds for "a real weakness".** Neither threshold is privileged by the registration's wording.
- **What the threshold changes on the hand-checked sample.** Under my coding, novel valid findings are about 1 higher at every level:

  | Level | Matcher: novel | Hand: novel | Matcher: A | Hand: A |
  |---|---|---|---|---|
  | R0 | 5.2 | 6.0 | 0.45 | 0.47 |
  | R1 | 4.8 | 5.8 | 0.40 | 0.39 |
  | R2 | 5.6 | 6.9 | 0.58 | 0.54 |

  - R2's A advantage shrinks from about +0.14 to +0.08.
  - Novel valid findings rise from R0 to R2 rather than fall.
  - **Every conclusion about P1–P3 stands under either threshold** (the R1 − R0 contrast above does not):
    - P1 holds;
    - A rises at R2 by echo;
    - novel valid findings do not fall;
    - P2 is not established, and P3 is not supported.
- **The limit:** the hand-scorer is a model of the scorer's family. So this checks how the rubric was applied; it is not an independent human judgement.

## Deviations from the registration, stated

1. **The hand-check was registered to come before unblinding.** It was registered and done after the primary aggregate had been read. That is the same deviation E1 had, and it is stated at its size: the full registered sample (20%, R2-weighted) was taken.
2. **The two secondaries were registered but not built into the runner.** They were built after the aggregate was read, as blind scorer passes registered in `PREDICTION.md` before they ran. The level labels are opaque in their file paths, and their prompts carry no level.
3. **Leak check.** R2 reviews echo the author's list, and that echo is the effect under study. The matcher judged substance, and the hand-check sampled R2 at 40% as registered. The R2 κ on "anticipated" (0.91) is the highest of the three levels.

## What this means for the paper (Step 5)

**The anticipation gap is real at full n.** An author who writes down the critiques a careful reviewer will make has forecast well under half of what a cold reviewer actually finds, and about half of the forecast goes unused. That supports Step 5.1: the real move carries information the anticipation lacked.

**The contamination half is not supported as stated.**
- Showing the reviewer the brief costs findings of every kind. It does not specifically cost the new ones.
- Showing the reviewer the author's expectations makes the review agree with the author more, but by adding the author's points, not by removing the reviewer's own.
- A paper sentence on contamination should say that. It should not claim that context "collapses the second perspective".
