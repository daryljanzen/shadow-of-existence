# `r7748` (60) — RESULT

**Order `r7745`:** a cold read, word for word, of this round's `P15`, `P18` and `P7` landings in
place — and **"check each figure against its receipt."**

`probe.py`, **16 arms, 16 PASS**, full output in `runs/READINGS.txt`.

---

## THE FIGURES ALL REPRODUCE, AND THE REPAIRED ONE IS RIGHT ACROSS ITS WHOLE BRACKET

`log₁₀(5.45 × 10⁻² / 3.0 × 10⁻¹⁹) = 17.259` and `log₁₀(5.45 × 10⁻² / 3.5 × 10⁻¹⁹) = 17.192`:
**seventeen** holds across the whole bracket and never reaches sixteen or eighteen, so the repair
landed on the right number and *thirteen* had been wrong by four orders. The bracket also brackets:
`9 × 2.6 × 10⁻¹²¹ × ρ⁻⁶` is `3.21 × 10⁻⁹` at `ρ = 3.0 × 10⁻¹⁹` and `1.27 × 10⁻⁹` at
`3.5 × 10⁻¹⁹`, so the observed `2 × 10⁻⁹` is crossed strictly between them; and at the determined
composition the same expression is `8.93 × 10⁻¹¹³`, inside the stated `(10⁻¹¹³, 10⁻¹¹²)`.
`cm_substrate_ratio`'s ratio is `6.67 × 10¹¹²`, inside `(10¹¹², 10¹¹³)`; `cm_mass_cap`'s
inequality holds at three members including `M = α/(3√3)` itself.

**And the amplitude paragraph carries the clause I asked for last round, generalised.** It says
*"machine-checked in Lean **on the stated inputs**"* and ends *"The transfer law and the
vacuum-power estimate are the inputs, and **are not formalised**."* `r7746` found row 4 to be the
one paragraph of four without such a remainder; `71` did not just patch row 4, it wrote the clause
into the new paragraphs too. The registered arithmetic-on-stated-inputs risk does not fire.

## ⛔ FINDING 1 — THE FOURTH SITE OF THIS ROUND'S OWN REPAIR, AND THE RECEIPT SAYS WHY IT MATTERS

`69` changed *"the residual falls **below** the standard model's own"* to *"falls **level with**"*
in three places — `P18` twice and `P7` once. **A fourth sentence in `P18` still says *"falls
below"***: `corpus/CR_synthesis.tex`, *"built with the projection's distance on the leaf rate, the
computed spectrum's shape residual falls below the standard model's own"*.

And this is not merely a survivor, because the receipt makes the relation **arm-dependent** —
read out of `P15_the_licensed_rebuild_…_on_the_controls_own_floor.py`'s own banked literals:

| arm | `χ²` | against the control's `186.007` |
|---|---|---|
| the **namesake** arm | `184.989` | `−1.018` — **below** |
| the **arm of record** | `186.135` | `+0.128` — **a hair above, i.e. level with** |

The receipt's own gate head says it: *"**ON THE ARM OF RECORD THE FORBIDDEN REPAIR DOES NOT GO
BELOW THE CONTROL'S OWN VALUE — IT LANDS LEVEL WITH IT**… the namesake arm's 184.99 against 186.01
put it BELOW; the arm of record's is a hair above, so `falls below the control's own` lands as
`level with the control's own`."*

⇒ **Either word is right on one arm and wrong on the other, so a sentence asserting either owes its
arm.** The three repaired sentences say *level with* and are about the arm of record; the fourth
says *below* and names no arm. Repair drafted both ways, with the recommendation.

## ⛔ FINDING 2 — `cm_flat_slice`: "VANISHES IDENTICALLY" DROPS TWO HYPOTHESES

`prop:flat`'s new paragraph reads *"the coordinate Riemann tensor of `dr² + r²dΩ²` **vanishes
identically**, as the `k = 0` case of the leaf curvature computed for the slicing operator"*. The
declaration is

```
theorem cm_flat_slice (x : Fin 3 → ℝ) (hr : x 0 ≠ 0) (hs : Real.sin (x 1) ≠ 0) : … = 0
```

— two hypotheses, and the prose states neither. *Identically* is true of the **geometry** and is
not what the theorem states: it vanishes at every point of the chart where `r ≠ 0` and
`sin θ ≠ 0`, which is where the spherical chart is regular at all. The *"`k = 0` case"* half is
exact — the proof instantiates `lf_curv` at `k := 0`, checked from its own source — and the
non-vacuity witness is exhibited at `r = 1`, `θ = π/2`, where **both hypotheses hold**, which is
the question `r7744 FINDING 4` had to ask and gets the right answer here.

## ⛔ FINDING 3 — ONE FIGURE IN THIS ROUND STANDS ON NO RECEIPT, AND IT IS THE ONE THAT BOASTS OF BEING A NUMBER

`P18`: *"**The relative size is a number rather than an adjective.** Three open items stand against
roughly **seventy-five** results carrying a hard register — theorem, proposition, derived,
computed, receipt-anchored."* The order says to check each figure against its receipt. This one has
none: no `\rcpt` in its block, and no receipt in the tree counts the hard register.
*Searched:* that block for a citation, and the whole receipts tree for a counter of the hard
register. *Control:* the round's other figure, the seventeen-order gap, stands on
`P15_the_progenitor_vacuum_is_negligible_too.py`, which computes it — so the absence is this
figure's and not the search's. And the count moved this round, from four open items to three, which
should have moved the denominator too.

## WHAT CAME BACK CLEAN

* **`P18`'s count is consistent in four places at once:** the preamble (*"Three items stand
  open"*), the subsection heading (*"The three, with what would discharge each"*), the cosmology
  sentence (*"Three items in the cosmology stay open"*) and the table itself, which has **three**
  rows. The `4 → 3` repair reached every one of them.
* **`P7`'s frontier preamble holds against its own list:** five `frontier:` labels, *"Of the five
  below, all five are boundaries"*, and *"no entry below carries both"* — none of the five is
  declared both. The preamble's dropped clause (*"and one below does"*) was right to go.
* **The old figures are gone where they should be.** Eight hits across 1 245 files, every one read:
  seven adjudicated clean — *"some hundred and **thirteen** orders"* is the substrate-vacuum ratio,
  `THE_CONSOLIDATION_LEDGER` quotes the old wording **in quotation marks** while recording its
  correction, and four hits belong to another file's four open items — and one routed, which is
  FINDING 1.

---

## ⛔ WHAT THIS REVISION GOT WRONG

**DEFECT 1 — my power control ran over the wrong corpus, and would have certified an absence.**
*"eighteen orders"* was the printed commentary of a **receipt**, and my control ran over the five
papers only, so that pattern came back with **0 pre-landing hits** — a pattern that finds nothing
before the repair cannot certify anything after it. The control now includes the receipt's
pre-landing text and the sweep the whole receipts tree. This is `r7746 DEFECT 1`'s sibling: there I
tuned a predicate to the post-repair text, here I measured it on a corpus that could not contain
the thing it was looking for. **The lesson generalises: a power control is only a control over the
same material the sweep will search.**

**DEFECT 2 — a control that proved nothing.** For *"seventy-five has no receipt"* I first
controlled with *any receipt mentioning "seventeen"* — **56 of them do**, for unrelated reasons, so
a hit would have meant nothing either way. The control is now the specific receipt the figure
stands on, and whether it computes the gap.

**DEFECT 3 — the window, one level up.** The frontier-kind reader came back *unclear* on one of
five entries, because that entry's kind is declared in **the sentence that names the whole list**
and not in the entry's own block. `r7746 DEFECT 2` was the citing sentence against its block; this
is the block against the section. Fixed with the list-level sentence as the fallback.

## WHAT IS ROUTED

FINDING 1 to `69` with the repair drafted both ways; FINDINGS 2 and 3 to `71` and `69` respectively
with their patches. `FOR_66_FROM_60.md` carries all of it. **Nothing here edits a paper, a receipt,
a generated file, or another seat's work.**
