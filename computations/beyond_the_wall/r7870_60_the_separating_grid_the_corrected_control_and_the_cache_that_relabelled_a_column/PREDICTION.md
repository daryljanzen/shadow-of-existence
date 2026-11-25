# `r7870` (60) — REGISTERED BEFORE ANY MEASUREMENT OF THIS REVISION EXISTS

**Committed and pushed before any computation of this revision exists.** Order `r7869` (69) carries
five items. Items ① ② ③ are measurements and are registered here as COMPARISONS with reachable
negatives. Item ④ is a defect fix whose OUTCOME is a measurement, so it is registered too. Item ⑤ is
carried and not opened here.

⛔ **The standing rule this line derived and keeps:** *if an arm's number or scope can be moved by
another revision landing, it is a reading and the claim is something else.* Every arm below is
either a figure this revision computes from its own grids, or a comparison whose two sides are both
computed here.

---

## ⓵ DECLARED READS — everything read BEFORE this registration

1. **Order `r7869`'s full text**, including its ruling to run the separating grid, its four-rung
   decomposition, and its housekeeping line about the two commit subjects.
2. **`r7866`'s committed `same_bins.json`**: the five parameters recorded for each reference mode,
   the seven totals per mode per bin set, the four moves, and both ratios. *This is how the routed
   cache defect was confirmed here rather than taken on report:* the two modes' parameters differ in
   all five while all seven totals are bit-identical on both bin sets.
3. **`r7866`'s receipt, the arm at line 169**, which pins the reference's `rd_camb` move to `-0.12`
   within `0.005`.
4. **`same_bins.py`'s `ref_profile`** and the construction of its CAMB cache: created once outside
   the mode loop, keyed on the sum alone.
5. **The first four control points at the corrected offset** and their own recorded configs.
6. **The collision gate's exit status** after the other line baselined the two subjects.

⌗ *Nothing about items ① ② ③'s limits has been read. The corrected control's limits do not exist
yet; the separating grid does not exist yet.*

---

## Ⓐ ① THE CORRECTED CONTROL, AND BOTH LIMITS ON IT

- **Ⓐ①ᵃ** The sixteen control CMB points at the corrected offset all solve, and each records the
  corrected offset in its OWN config, while the sixteen carried arm-of-record points record no
  offset at all. ⇒ *Reachable negative: a point that records no offset, or the wrong one, fails this.*
- **Ⓐ①ᵇ** The control's lensing half at the corrected offset, sixteen points, all solve.
- **Ⓐ①ᶜ** **A COMPARISON, and the negative is the landed state.** Is the minimised limit on the
  corrected bank **READABLE** — monotone above its minimum — or not? At the superseded offset it was
  **NOT**. ⇒ *If it is readable at the corrected offset, the unreadability was the offset's and not
  the repair's, and that is reported as such.*
- **Ⓐ①ᵈ** The calibrated limit on the corrected bank, against `185.69` meV at the superseded offset.
  **Registered expectation, which can fail:** the control's spectra are weakly sensitive to an offset
  this small, so the calibrated figure moves by **less than 10 meV**. ⇒ *A larger move REFUTES that
  expectation and is reported as a refutation with the criterion unmoved.*

## Ⓑ ② THE SEPARATING GRID — repair on, offset unset, thirty-two points

- **Ⓑ②ᵃ** All thirty-two points solve, and their configs record the repair ON at every nonzero sum
  and no offset anywhere, on either arm.
- **Ⓑ②ᵇ** **THE FORK'S DECIDER, registered both ways before it is run.** Is the minimised limit on
  the repair-only bank READABLE?
  - **NOT readable ⇒ branch A: the REPAIRED BACKGROUND carries the unreadable profile.**
  - **Readable ⇒ branch B: the N_eff RULING carries it.**
  ⇒ *Both branches are stated here so neither can be chosen after the fact.*
- **Ⓑ②ᶜ** The calibrated limit on the repair-only bank.
- **Ⓑ②ᵈ** The four rungs the order names, each with both limits, as one table: the landed bank
  (no repair, no offset); this grid (repair only); the repair at the superseded offset; the repair at
  the corrected one. ⇒ *A rung whose numbers cannot be produced is reported as absent, not omitted.*

## Ⓒ ③ THE NON-MONOTONIC TOP NODE — is it the grid's own edge?

- **Ⓒ③ᵃ** Measured on BOTH ① and ②: does the minimised profile dip between the two highest sum
  nodes? Reported **before any limit is read through it**, as the order requires.
- **Ⓒ③ᵇ** **A COMPARISON with a reachable negative.** The dip is re-measured with the sum axis
  extended by one node, and again with a cold start at the current top node.
  - **The dip disappears under either ⇒ it is the GRID'S EDGE.**
  - **It survives both ⇒ it is NOT the edge**, and the profile is non-monotonic as a fact about the
    model and not about where the grid stops.
  ⇒ *An arm that could only confirm "edge" would not be a test; the surviving case is named.*

## Ⓓ ④ THE CACHE THAT RELABELLED A COLUMN

- **Ⓓ④ᵃ** *(already measured — see DECLARED READS 2, and recorded as a read, not as a finding of
  this revision)* The defect is real: both reference modes' columns are bit-identical across all
  seven sums and both bin sets, while their five recorded parameters differ in all five.
- **Ⓓ④ᵇ** **A COMPARISON, and this is the one that can surprise.** The corrected `rd_camb` column is
  computed with the cache keyed so the defect is impossible, and its move compared to the voided
  `-0.1238`.
  - **Within `0.005` ⇒ the defect was PROVENANCE ONLY**: the column was mislabelled and the number
    it carried happened to be right, so nothing numerical was lost.
  - **Outside `0.005` ⇒ the reference's TWO RULERS DIFFER at the low end**, which the landed record
    could not have seen, and the comparison gains a second denominator worth reporting.
- **Ⓓ④ᶜ** The headline survives, **asserted on the code path and shown as arithmetic**: both ratios
  divide by the `rd_min` move, and `rd_min` is the mode that POPULATED the cache, so its own column
  was served its own spectra. ⇒ *Reachable negative: if the ratio's denominator were the `rd_camb`
  move, the headline would NOT survive and this arm would say so.*
- **Ⓓ④ᵈ** **A CONSEQUENCE THE ORDER DID NOT NAME, registered here so it cannot be tidied away.**
  `r7866`'s own merged receipt pins the `rd_camb` move at `-0.12`. That pin asserts an ARTEFACT of
  the cache, so the corrected column reds this seat's own receipt. The arm is re-pinned to the true
  move, the old pin is recorded as having asserted an artefact, and the receipt returns to passing.
  ⇒ *Reachable negative: if the receipt cannot be brought back to passing without weakening another
  arm, that is reported instead of done.*

## ⑤ THE MECHANISM OF THE LEAN — carried, not opened

The order carries it until ①–③ are in. Nothing about it is registered here, and no arm below reads
it. ⌗ *Named so that its absence is a decision and not an omission.*

---

## WHAT WOULD MAKE THIS REVISION WRONG

- A control point that does not record the offset it was solved at.
- A limit read through a profile whose top node was not first adjudicated by Ⓒ③.
- Choosing the fork's branch after seeing the answer rather than from Ⓑ②ᵇ as registered above.
- Reporting the corrected `rd_camb` move as a confirmation when Ⓓ④ᵇ's two cases are both live.
- Leaving `r7866`'s receipt passing on a pin that asserts the cache's artefact.
