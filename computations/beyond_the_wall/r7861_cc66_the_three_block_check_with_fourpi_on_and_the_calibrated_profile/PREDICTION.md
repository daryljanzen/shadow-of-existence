# `r7861+cc66` — REGISTERED BEFORE ANY COMPUTATION OF ITEM ⑥

Order `r7861` (69): **③** the three-block check with `FOURPI` on, *"as registered at `r7859+cc66.1`"*;
**⑥** bank the calibrated reference's full profile where `60` can read it, and give CAMB's `rdrag` at
the control point and at two corners of `60`'s grid.

**⚠ ITEM ③'s BANDS ARE NOT RESTATED HERE.** They are registered and pushed at `6412bd3ee`
(`r7859_cc66_the_three_block_check_with_fourpi_on/PREDICTION.md`), before any of its computation
existed, and the order points at that registration by name. Restating them now, after `60`'s
`r7860` has published `TT 1.002278` and `EE 0.991831`, would convert a registration into a
transcription. ⌗ *Those two numbers of theirs sit inside my registered `±0.02` on both blocks, which
is recorded here and is not a new band.*

**⛭ ITEM ③ IS UNBLOCKED, AND I CHECKED THE WIRING RATHER THAN THE REPORT.** On this tree
`_ee_te[j]` carries `* _FP_ACC` on both sums, `_dec[j, _c]` carries it, and `_dc` carries `/ _FP_DL`
where it is FORMED rather than in the save keyword. ⌗ *My own first grep counted one of the two
because the EE/TE assignment now wraps across two lines — a line-based count of a wrapped
expression, caught by reading the block instead of trusting the number.*

---

## ITEM ⑥ — WHAT IS READ, AND WHAT IS COMPUTED

**Read, not recomputed:** the nine `rd_camb` and nine `rd_min` checkpoints of `r7853`'s profile
already hold every field the order asks for — `total`, `chi2_cmb`, `chi2_lens`, `chi2_tau`,
`chi2_bao`, `H0`, `Om`, `ombh2`, `ns`, `tau`, `amplitude`, `rd_used` and `rd_camb` at each sum. They
are assembled into one record; nothing is re-fitted, because re-fitting would publish numbers that
are not the ones the landed limits came from.

**Computed here:** CAMB's `rdrag` at `60`'s control and across `60`'s own grid displacements, read
off `gen_pol_batched.sh`: `lcdm` at `H0 = 67.40`, `Ω_m = 0.3150`, `ω_b = 0.0224`, `n_s = 0.965`,
with steps `±2.0`, `±0.0150`, `±0.0008` and `±0.020`.
  ⌗ *`60`'s grid is a STAR and not a box, so it has no corners in the literal sense. I take the
  order's sense — the ends of the ruler's range over the grid — and give `rdrag` at all eight
  displaced `lcdm` points, reporting the control plus the two EXTREMES by name.*

## BANDS

**Ⓖ CAMB's `rdrag` at the control lands between `147.0` and `147.8` Mpc.** *The published value at
Planck's own best fit is `147.09`, and this point's `ω_c` differs from it.*
  ⇒ REFUTED outside `146.5`–`148.5`.

**Ⓗ The ruler barely moves over `60`'s grid: `rdrag`'s full range across the eight displaced points
is under `1.5` Mpc, and `ω_b` is the dominant lever — its `±0.0008` step moves `rdrag` more than the
`±0.0150` step in `Ω_m` does.**
  ⇒ REFUTED if the range exceeds `1.5` Mpc, or if `Ω_m` moves it more than `ω_b`. *The second limb
  is the one worth having: it says which of `60`'s displacements a drag-epoch ruler is sensitive to,
  which is what makes a per-point recomputation worth doing at all rather than holding it.*

**Ⓘ MY CALIBRATED ARM REALLY IS CALIBRATED, AND THE MINIMISED ARM REALLY IS FREE.** At every one of
the nine sums, the calibrated arm's `rd_used` equals its own `rd_camb` EXACTLY, and the minimised
arm's `rd_used` differs from that point's `rd_camb` by more than `1` Mpc.
  ⇒ REFUTED if either fails, and a failure on the first limb would mean `r7853`'s "calibrated" was
  not calibrated and its `30.56` meV would be withdrawn with it.

**Ⓙ And the calibrated ruler is nearly flat along the sum:** across the nine sums its `rd_camb`
varies by less than `1` Mpc, because the fit moves `H0` and `ω_b` only slightly with `Σm_ν`.
  ⇒ REFUTED above `1` Mpc, which would say the ruler and the mass are more entangled on this
  reference than the limit's reading assumes.

---

## ⚠ WHAT ITEM ⑥ CANNOT SETTLE

It gives `60` the numbers to check their drag-epoch ruler against; it does **not** check their
implementation, and it cannot say whether their `146.13` meV becomes comparable to my `30.56` once
they rerun on these terms. **That comparison is theirs to make and mine to be read against**, and
the one thing I can state in advance is that a ruler recomputed per point and a ruler held at the
control differ by at most what `Ⓗ` measures — so if their rerun moves the limit by far more than
that, the ruler is not what moved it.
