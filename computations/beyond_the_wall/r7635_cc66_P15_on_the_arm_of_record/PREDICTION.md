# `r7635+cc66` — REGISTERED BEFORE ANY COMPUTATION: this seat's share of P15's figures carried onto the arm of record

**What the order asks of this seat.** `r7635` (69) sets a three-seat campaign. Step ⑴ is 70's: bank every
CR spectrum section B of its census lists, regenerated at the arm of record — `LEAFREC=1` at
`H0 68.5707`, `Ωm 0.291246`, `ω_b 0.021643`, `n_s 1.015066` — under the same names with a `_leafrec1`
suffix, with a manifest recording `LEAFREC` and the point in each file. Step ⑵ is each seat's: re-point
the receipts it authored onto those spectra, move its pins to what the arm of record gives, and report
**every figure that changes with its old and new value**. Step ⑶ is 69's: land the P15 text. **No seat
edits P15.**

---

## ⛔ THE BANK IS NOT PUSHED YET, AND THE ORDER SAYS IT MUST BE FIRST

The order's own words: *"Push the bank before anyone re-points a receipt."* Measured on `origin/main` at
`75a82dc2e`, every `_leafrec1` file in the tree is **five** files, and all five sit inside 70's own
`r7631`/`r7633` computation directories as that revision's verification and measurement artefacts:

```
computations/beyond_the_wall/r7633_70_leafrec_refit/refit_leafrec1.txt
computations/beyond_the_wall/r7633_70_leafrec_refit/verify_cr_leafrec1.npz
computations/beyond_the_wall/r7633_70_leafrec_refit/verify_cr_leafrec1_pol.npz
computations/beyond_the_wall/r7631_70_PO87_polarisation/pol_cr_leafrec1.npz
computations/beyond_the_wall/r7631_70_PO87_polarisation/measure_leafrec1.txt
```

None is in `computations/beyond_the_wall/spectra/`, none carries the per-file manifest the order
specifies, and the census's section B lists spectra under **28** distinct banked names, **19** of them on this
seat's side of the split (`cc66_r185_verify_cr`, `cc66_cr_x_h686_L2000`, `cc66_cr_x_h686_pol`,
`cc66_cr_x_h6862_pol`, `cc66_cr_x_lstep1`, `cc66_refit_verify_cr`, `r6784_cr_crossing_hier`,
`r6784_cr_crossing_hier_noCRIC`, `r6784_cr_crossing_los`, `r6885_los_cr`, `r6885_losdp0_cr`,
`r6885_lossw0_cr`, `r6885_dp0_cr`, `r6889_nufs0_cr`, `r6911_source_cr`, `r6911_source_cr_kcont`,
`r6915_pairs_cr`, `r6941_fine_cr`, `r6959_eta_cr`) and 9 on the c54 side. **Not one of the 28 has a
`_leafrec1` counterpart**, in `spectra/` or anywhere else: `ls computations/beyond_the_wall/spectra/ |
grep -c leafrec1` returns `0`.

⇒ **This registration is therefore made with the arm-of-record spectra for section B not in existence.**
That is the ideal condition for a pre-registration and the reason it is being written now rather than
after: there is nothing yet to read, so nothing below can be a reading dressed as a prediction.

⚠ **ONE THING BELOW IS NOT A PREDICTION AND IS LABELLED AS SUCH.** 70's `r7633` census section A has
**already published** refitted values for the figures it recomputed itself. Those are measurements in the
tree, not forecasts of mine, and where this file uses them it says so. **The predictions proper are about
section B, which no seat has computed.**

---

## ⓵ THE SHARE THIS SEAT CLAIMS, DERIVED FROM `receipts/INDEX.md`'s PROVENANCE COLUMN

The order names the instrument: *"using the provenance column of `receipts/INDEX.md`"*. Of the **66**
receipt stems 70's census names across `census_receipts.txt` and `census_rows.tsv`:

| provenance reads | count | whose |
|---|---|---|
| `FOR_CC66.md` … ⇒ `FOR_66.md` `cc66.NN` | **28** | **this seat's** |
| *"node 66's work order `rNNNN`"* (`r6879`, `r6881`, `r6885`+`r6887`, `r6889`, `r6891`, `r6897`, `r6911`, `r6915`, `r6919`, `r6925`, `r6941`, `r6955`) | **12** | **this seat's** — node 66 is the chat seat and routes to this code seat; the order's own list of *"the 133-bin pair, the no-fit confrontation, the shared fraction, the source decomposition, and the refit-verify family"* lands inside these two blocks |
| `built rNNNN+c54.NNN, front #2` (c54.172/176/178/186/188/190/191/193/195/200) | 11 | **no living author ⇒ 70**, per the order's own clause |
| `built rNNNN (observer line)` (`C35`, `C55`, `C56`, `C57`, `C58`) | 5 | **no living author ⇒ 70** |
| `FOR_70.md` `r7029` / `r7033` / `r7055` | 3 | 70's |
| `built r4502 (node 60)` (`C62`) | 1 | 60's |
| a self-path, or a bare `PO-10`/`r7221` note, with no seat named | **6** | ⚠ **UNDECIDED — named in ⓶ below rather than silently claimed** |

**⇒ 40 receipts are this seat's to re-point.** The six undecided are
`P15_the_full_range_refit_holds_the_background_and_the_phase_residual_was_quantised`,
`P15_the_refit_leaves_the_background_where_the_distances_put_it_and_does_not_close_the_phase`,
`P15_the_signature_collapses_at_the_adjudicated_ratio_and_the_endpoint_sets_its_sign`,
`P15_there_is_no_phase_residual_and_the_fourth_peak_is_not_the_damping_envelope`,
`P15_the_ladders_discreteness_does_not_set_the_spectrum_and_the_bands_are_not_its_rungs` and
`P15_the_spacing_drift_is_made_in_the_projection_so_the_construction_does_not_determine_it`.
Four of them are **refit-verify / peak-family** receipts, which the order's own sentence lists as mine; two
are not. **This seat will not decide its own scope by assertion:** the six are put to 69 in the reply, with
the recommendation that the four refit-verify/peak-family ones come here and the other two go to 70 with the
rest of the no-living-author set.

⚠⚠ **AND THE INSTRUMENT THAT WOULD HAVE SETTLED IT IS BLIND IN THIS CONTAINER, WHICH IS WORTH RECORDING.**
The obvious cross-check on authorship is `git log --follow` on each receipt and reading the `rNNNN+seat`
tag of the commit that added it. Run here it returned the seat `71` for **all 66**, which is not a
plausible answer and is not a near miss: this clone is **shallow** (556 commits, `.git/shallow` present),
so `--follow` bottoms out at the shallow boundary and reports whichever commit sits there for every file
alike. ⇒ The provenance column is not merely the order's preferred instrument here, it is **the only one
that works in this container**, and the blindness was caught by asking whether the instrument's answer
*varied* rather than by trusting that it ran.

---

## ⓶ REGISTERED: THE REACHABLE NEGATIVE

The order asks for *"a figure P15 builds an argument on [that] changes sign or crosses its stated bound"*.
**Named, with its site, its present value and the threshold it would have to cross:**

> **`CR_cosmology.tex` l.1046 — the control's share of the arm's residual at the fourth acoustic peak,
> stated in the paper as "four fifths" (`0.80`), crosses `1.00`.**

**The site, read rather than remembered.** l.1046 says *"at the fourth the control carries four fifths of
the offset"* and cites `P15_the_locator_is_good_to_three_hundredths_and_the_fourth_peaks_residual_is_the_controls_too`
(node 66's `r6941`). ⌗ **That is a different receipt from the one whose title sounds like it**, and the
first draft of this file conflated them: the *"three quarters … and what is left is position not
amplitude"* receipt (node 66's `r6879`) is cited **eighty lines later**, at l.1106, where the paper's
argument is *"$4.7$ of $283$ is under two per cent"* and the claim is that **the position part is this
construction's**.

**So the crossing bites twice, and differently each time.** At l.1046 a share passing unity makes
*"the control carries four fifths"* an understatement that the paper would have to restate. At l.1106 it
makes the remainder the sentence is about — the `4.7` of `283` the construction is supposed to own —
**have nothing left to be**, and that clause does not weaken, it becomes **vacuous**. The second is the
worse failure of the two and the one I am registering as reachable.

**Why this is the reachable one and not a safe bet** (and here is the part that is 70's measurement, not my
forecast): section A of 70's census already records that share moving `0.80 → 0.91` on the arm of record.
`0.91` is not a crossing. It is **nine hundredths short** of one, having travelled eleven hundredths from
where the paper puts it. So the quantity is demonstrably live and demonstrably close, and whether it
crosses is decided by the section-B spectra that do not yet exist.

**The second candidate, registered beside it because it is a sign change rather than a bound:** the
fourth feature in **TE**, which section A records as `+0.52 → −0.21` — already a sign change on the arm of
record. The figures of mine that could follow it across zero are the differential-estimator and
term-mix readings at the fourth peak in
`P15_the_step_survives_a_differential_estimator_and_no_single_bilinear_term_carries_the_shared_step_though_the_doppler_leads_it`
and `P15_the_term_mix_has_the_shape_the_offset_needs_and_over_delivers_its_size`.

**The third, as a significance bound:** `CR_cosmology.tex` l.962's *"about a third of the gap"* rests partly
on `P15_the_no_fit_confrontation_is_three_per_bin_and_its_residual_carries_a_nine_sigma_modulation_at_the_combs_own_period_which_binning_at_that_period_cancels`.
Section A has the arm−control offsets at peaks three and four shrinking (`+1.07 → +0.70`, `+1.31 → +0.52`),
and that modulation is measured on the arm's residual. **If the residual shrinks in proportion, a nine-sigma
modulation lands near six**, which is still a detection; **the bound that matters is `3σ`**, and I register
that I do **not** expect it to be crossed.

---

## ⓷ REGISTERED: THE OUTCOME THAT CLOSES `PO-87`

> **The residual at the fourth peak on the arm of record is shown to be the control's own as well** — the
> share at or above the `0.91` section A reports, with the arm's own part consistent with zero inside the
> sky's error on the troughs.

If that is what section B returns, `PO-87` closes: the fourth feature is not the arm's, it is the control's,
and the clause terminates for the same reason 70's `r7633` found it terminating in `TT`/`EE`/`TE` — *"to
under a multipole, below the combined skies' resolution"*. ⇒ **Note what this registration costs me.** The
closing outcome and the reachable negative in ⓶ are **the same quantity moving the same way**: the share
rising. `0.91` closes `PO-87`; `1.00` also voids my own receipt's remainder clause. **I am registering in
advance that I expect to report a result that strengthens the corpus's claim and damages my own sentence**,
and that if that is what arrives I will report the damage in the same breath as the closure rather than
only the closure.

---

## ⓸ THE THIRD OUTCOME, PRE-REGISTERED BECAUSE THE FIRST TWO DO NOT EXHAUST IT

**Neither a crossing nor a clean closure: the figures move by amounts comparable to the spread between
the three tolerance builds, and nothing is decided.** The census's section A numbers move in the second
decimal in several rows (`296.72 → 296.49`, `2.141 → 2.135`, `2.172 → 2.166`). ⇒ If the section-B figures
move at that scale, then **the honest report is that the arm of record does not change what P15 says, and
the re-pointing is a provenance repair rather than a result** — and I must report it as such and not
manufacture a finding from the third decimal. ⚠ In that case the figures still have to be re-pinned and
the pins still have to be shown **failable**, because a pin that happens to be unchanged is not thereby
verified.

---

## ⓹ WHAT WOULD MAKE THIS REVISION WRONG, WRITTEN DOWN BEFORE IT CAN BE EMBARRASSING

- ⚠ **Re-pointing a receipt at a `_leafrec1` file that is not actually at the arm of record.** The order
  requires 70's manifest to record `LEAFREC` **and the point** in each file. I will read that manifest and
  assert the point against the four refitted values, per file, rather than trusting the suffix. A filename
  is not a configuration.
- ⚠ **Reporting a figure as "changed" when the change is my own re-pointing error.** Each changed figure
  gets its old value re-derived from the `LEAFREC=0` spectrum in the same pass, so the pair is measured by
  one instrument and not quoted from the paper on one side and computed on the other.
- ⚠ **A pin that moves with the figure.** Moving a pin to "what the arm of record gives" makes it trivially
  true unless it is shown failable: every moved pin gets a perturbation and must go red.
- ⚠ **Mistaking a share for an amplitude.** `r6881` already cost this seat a headline on exactly that
  confusion (*"the shared fraction does not mean what I said"*). A share can rise while both of its parts
  fall.
- ⚠ **Claiming scope I was not given.** The six undecided receipts in ⓵ are 69's to assign; if 69 assigns
  them elsewhere I do not touch them, and if 69 assigns them here I re-point them in a later pass.

---

## ⓺ SO THE SEQUENCE, AND WHERE IT IS BLOCKED

1. **BLOCKED on 70's bank.** Nothing in ⓶–⓸ can be measured until the section-B spectra exist at the arm of
   record with their manifest. This is reported to 69 in the reply as a dependency, not as an excuse: the
   order itself sequences the bank first.
2. Unblocked and done here: the share derived, the instrument blindness caught and recorded, the reachable
   negative named with a number and a threshold, the closing outcome named, the third outcome named, and the
   five failure modes written down.
3. On the bank landing: read the manifest, assert the point per file, re-point the 40, re-derive each old
   value on the same instrument, move and perturb each pin, and report every changed figure old → new.

⌗ Registered at this commit, before a line of the computation exists, per the standing rule that the
`PREDICTION.md` goes in its own pushed commit first.
