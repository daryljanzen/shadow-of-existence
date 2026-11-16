# r7812 (69) — the resumable mode loop, and the sentence list before the one pass

**Registered BEFORE a line of the computation exists**, in its own commit, pushed. Written by `cc66`.

`r7812` merged `r7811+cc66.1–.6`, took all three corrections, and ruled:

* **(a1)** *"Bank the mode loop in resumable pieces, each under the limit, and assemble the spectrum
  from the banked pieces. Then check the assembled spectrum against a straight run on a short ℓ
  range, to exactness. How you split it is your call."*
* **(a2)** goes to **70** — not this seat's.
* **(4d)** stays a (b) in kind but is re-derived in the one pass.
* the four `13864.6627` literals move to `13894.421` for each read that is re-pointed.
* `gates.yml` stays as it is.

⛭ **The ruling splits the MODE LOOP and not the ℓ RANGE, which is the distinction this round
measured.** Splitting ℓ changes the spectrum — `7.3e-03` separates `cc66_lcdm` (ℓ≤1298) from
`cc66_lcdm_L2000` (ℓ≤1998) from the reach alone, through the hierarchy handover. Splitting over
$k$-modes does not: every mode's contribution enters the same sum, so a partition of the mode set
re-assembles to the same spectrum. **That is the claim (5a) tests rather than assumes.**

## Predictions

* **(5a) THE ASSEMBLY IS EXACT.** The spectrum assembled from banked mode-pieces equals a straight
  run on the same configuration to **machine precision**: predicted `max |assembled/straight − 1| <
  1e-13`. ⛭ *I expect it to be **bit-identical** (`== 0`) if and only if the pieces are summed in the
  same order the straight run sums them, and I will report which of the two it is rather than
  rounding the question away — a non-zero residual at `1e-16` is a summation-order artefact and is
  not the same finding as one at `1e-13`.*
* **(5b)** The split costs **no** accuracy and some wall time: predicted total wall **within a factor
  1.5** of the straight run's, the overhead being re-entry and I/O.
* **(5c)** The pieces number **3–6** for 2547 modes under a 2-hour limit, central guess **4**, since
  the killed run reached 2250 of 2547 in 1 h 52 m with the projection still to come.
* **(5d)** ⛔ **The instrument edit will move its blob and redden the two `instrument_blob` receipts**
  — `P15_the_fitted_comb_…` and `P15_the_1p57_…` — exactly as `r7807+cc66.4` did. **Predicted: yes,
  both, and the fix is to extend their `_Strip` reduction to the new keyword.** *Registered in advance
  because at `cc66.4` this surprised me, and a surprise I have already had once is a prediction.*
* **(5e)** The sentence list for the one pass holds **6–14** landing sites, central guess **9**.

## Scope

**No paper sentence is edited until 69 has read the list** — that is the order's own sequencing, and
it is the deliverable that does not depend on (a1). **No significance is computed.** The instrument
change is **additive and inert unless its new switch is set**, so a run that does not ask for pieces
behaves exactly as today; that is asserted, not hoped.
