# `r7683` (cc66) — REGISTERED BEFORE A LINE OF THE COMPUTATION EXISTS

**The order** (`r7683`, 69), two rulings. `r7681+cc66.0`–`.5` merged as PR #638, so this is a branch
restarted from `main` and a new draft PR.

## RULING 1 — the retention slope goes on each arm's OWN comb (60's branch (b)). **This is my work.**

`l.1773` carries the **own-comb** slope, not the shared one, *because `r7639+70` itself calls the
shared reading "the beat and not a measurement"*. So:
1. **Patch `P15_the_phase_systematic…`** so its VERDICT covers the slope on the own comb exactly as it
   already covers the step, using `OC.retained_own` / `OC.slope12` / `OC.retention_null` — already in
   the module the file imports.
2. **Route `l.1772–1793` as one block, wholly in the own-comb convention:** the lowest- and
   highest-band ratios, the slope `+0.0103 ± 0.0014`, the setting spread, the intercept and its
   spread; the null at 21–32 per cent surviving at `+0.0071`–`+0.0082`, with 60's over-phase caveat
   (worst phase reaching 0.51–0.54 of the slope); and the shared-comb reading stated **once** as what
   reads the drift.
3. **And answer:** if `the_cross_term…`, which `l.1773` cites, carries only the shared statistic, does
   the **citation** move or does the **receipt** gain the own-comb form?

## RULING 2 — the low-ℓ section stays on the background the distance data fix. **BLOCKED on 70.**

69 reverses its own `r7679` lean toward (a) and does not land my nine-site batch. *The reason is the
cross-background defect I named, pointed the other way: `l.2567` says the stretch is computed "on the
background the distance data fix", and that statement is what makes the floor parameter-free, so
moving the depths to the TT refit point would put a spectrum fit under a parameter-free prediction.*
⇒ **The seven printed depths stand.** Only the cross-validation claim moves, and 70 is ordered to run
the split-clock hierarchy at the distances' point first. **I draft nothing there until it reports**,
and my proposed wording form stands for when it does.

⌗ **What I already know, stated so no arm is registered against knowledge I have.** From
`r7681+cc66.1`: the own-comb twelve-setting slope on the arm of record is `+0.01034 ± 0.00137` with a
real-phase null of `+0.00328` (amplitude `0.5`) and `+0.00215` (the banks' own), surviving at
`+0.00707` and `+0.00820`; the shared-comb one is `+0.02690 ± 0.01226` against `+0.03088`. From 70's
`measure_retention.txt`, the own-comb seven-band ratios at window 1 on this arm are `1.0364 1.0708
1.0659 1.0699 1.0858 1.0827 1.0832`. The order itself quotes 70's and 60's `21`–`32` per cent,
`+0.0071`–`+0.0082` and `0.51`–`0.54`. **None of that is a prediction; it is last revision's and
another seat's measurement, and the arms below are about what has NOT been measured: the own-comb
INTERCEPT, its spread, the figure count, and the citation question.**

## THE ARMS

**① The own-comb intercept STRADDLES one, so `l.1774–1776`'s claim — "the intercept of that rise
covers one across the same twelve settings" — survives the convention change.** *Registered because
it is the one clause in that sentence that is a claim rather than a digit, and the whole point of
ruling 1 is that the own-comb statistic is the sounder one; if its intercept did NOT cover one, the
convention change would cost a claim rather than only digits. Falsified if the twelve own-comb
intercepts all sit on one side.*

**② The own-comb intercept's spread is SMALLER than the shared one's `0.0331`, and under `0.010`.**
*Because the own-comb slope's spread is `0.00137` against the shared `0.01226` — nine times smaller —
and the intercept is fitted in the same twelve settings by the same OLS. Falsified above `0.010`,
which would mean the stability does not carry from the slope to the intercept and the two parameters
of one fit disagree about which convention is stable.*

**③ The own-comb band endpoints reproduce 70's `1.0364` and `1.0832` to four decimals at window 1,
and the twelve-setting endpoint range is NARROWER than the shared convention's `1.0103`–`1.1612`.**
*The first half is a reproduction and not a discovery; the second is the arm. Falsified if the
own-comb endpoints span more than the shared ones.*

**④ The over-phase worst null reaches `0.51`–`0.54` of the own-comb slope, reproducing 60's caveat to
two decimals.** *Registered as a reproduction so that the caveat the order tells me to carry is
measured here rather than quoted. Falsified outside `0.49`–`0.56`.*

**⑤ `the_cross_term…` carries ONLY the shared statistic, and the right answer to 69's question is
that the RECEIPT gains the own-comb form rather than the citation moving.** *Because `OC.retained_own`
is built on that receipt's own lifted `env_a`/`osc`/`retained` — the own-comb form IS its statistic
read on each arm's own comb coordinate — so the producer of the sentence's quantity is still that
receipt, and moving the citation would attribute its own figure to another file. Falsified if that
receipt already carries an own-comb path, or if its `retained` cannot express one.*

**⑥ Between 8 and 14 printed figures across `l.1772–1793` change under the own-comb convention,
central guess 11.** *Six in `l.1772–1776` (two endpoints, the slope, its spread, the intercept, its
spread) plus the fractions in `l.1781–1793`, which are all recomputed against a different
denominator. Falsified outside that band.*

**⑦ The receipt's closing VERDICT block needs between 2 and 4 of its statements changed, central 3.**
*It currently reads "on the shared comb neither banded statistic survives its phase systematic — the
step's null is half or more of it, the retention slope's is all of it. On each arm's own comb the step
stands." Ruling 1 makes the slope's own-comb reading the one of record, so the block has to say so
for the slope as it already does for the step. Falsified outside 2–4.*

**⑧ The own-comb slope is MORE significant than the shared one, not less: between 6 and 9 sigma of its
own setting spread against the shared one's 2.2.** *`+0.0103/0.0014` is `7.4`; registered as a band
because the spread is what I will recompute. ⇒ So the convention change STRENGTHENS `l.1774`'s "none
of them returning a negative value" rather than weakening it, which is worth stating because the
natural worry about a smaller slope is that it is less secure. Falsified below 6 or above 9.*

## WHAT THIS DOES NOT SETTLE

- **Not the paper.** Ruling 1 routes `l.1772–1793`; `corpus/CR_cosmology.tex` is not edited here.
- **Not ruling 2.** It is blocked on 70's split-clock hierarchy at the distances' point. **I draft
  nothing at those six sites until it reports**, and I do not re-argue 69's reversal — the reason it
  gives is the cross-background defect I named, applied to my own batch.
- **Not `r7639+70`'s judgement** that the shared reading is "the beat and not a measurement". That is
  the premise of ruling 1 and I do not re-derive it.
- **Not the step.** Its own-comb reading is already of record and is untouched.

⌗ **The four process commitments, all still in force, and the fourth earned its keep last revision.**
**①** An exact-count site means `S4`/`S10`/`S11`/`S13` by name in the same pass.
**②** A figure a receipt quotes from the paper is fixed by correcting the **quotation**.
**③** ⛔ `turn_gates.sh` runs **neither** `check_unread_figure` **nor** `check_marker_transposition`;
both go BY NAME before every push.
**④** ⛭ Every digit in a gate label is **interpolated from what the gate computes**, never typed.
**⑤ NEW, from `r7681`'s three related falsifications.** ⛔ **A gate must not assert a PRINTED form
unless printing is what it is about.** I twice wrote gates requiring a printed digit to hold when all
I had registered was that the quantity moves by under a per cent — and a sub-per-cent move crosses a
rounding boundary whenever the digit sits near one. ⇒ *Size and printed form are two different
assertions; a gate that asserts both asserts the one its author hoped for.*
