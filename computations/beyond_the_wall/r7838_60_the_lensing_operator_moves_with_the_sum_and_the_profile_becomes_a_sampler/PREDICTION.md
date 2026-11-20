# r7838 (60) — PREDICTION, registered and pushed BEFORE any measurement

On order `r7833` (69), items ①–④, which follow from `r7836`'s registered failure: the refit
harness could not bound the neutrino-mass sum because its lensing operator was formed ONCE with
the mass hardcoded, and because its profile was a chain of local minimisations that failed a
monotonicity check.  The order is: make the operator move with the sum, replace the profile with a
sampler, **land the control first**, and only then read the arm.

**This file is the registration.  It is committed and pushed before the rebuilt harness is run
even once.**  Every arm below is a COMPARISON with a REACHABLE NEGATIVE, and the criteria are
fixed here.  A failed arm will be reported AS failed, with the criterion as written and not
loosened.  The arm count is asserted at the end of the receipt.

---

## What is being rebuilt, and what is held

* The CMB side stays `r7749_70_leafgeom_refit/refit.py`'s: the same 185 lensed bins, the same
  `chi2_of_spectrum` covariance, the same analytic amplitude solve, the same banked direction
  grids, the same quadratic expansion.  **One thing changes: the lensing operator.**  Where the
  borrowed harness forms `RATIO = C_l^lensed / C_l^unlensed` once at a CAMB cosmology with
  `mnu = 0.06` hardcoded, this revision forms `RATIO(Sum)` at each trial sum, at the reference
  cosmology, **holding the total `Omega_m h^2` fixed** so that `omega_cb` falls by `omega_nu` —
  the same convention the fit itself uses and the same one `ACOUSTIC_two_arm.py` carries since
  `r7836`.
* Because the binned model's base and its four direction derivatives are all formed THROUGH the
  operator, a moving operator means the whole expansion is rebuilt at each sum.  This is done on a
  grid in the sum and interpolated between grid points; the interpolation error is itself measured
  and asserted below, not assumed.
* The BAO side stays `distances.py`'s `chi2_bao` on the leaf ruler with `r_d` minimised.
* The fifth direction stays `r7836`'s own generated pair.

## The arms

**Ⓐ① The rebuilt operator reproduces the signature `r7836` measured.**  The operator's own
fractional change against `Sum = 0` comes out `0.372` per cent at `Sum = 0.06` eV and `0.768` per
cent at `0.12`, each within `0.004` and `0.008` absolute (half a unit in the last printed digit),
with the peak in `l` between `1900` and `2060`.
*Reachable negative: a different magnitude or a peak outside that band, which would mean the
rebuild and `r7836`'s measurement disagree and one of them is wrong.*

**Ⓑ② The operator's response is monotone in the sum across the scan.**  `max_l |RATIO(Sum) /
RATIO(0) - 1|` is strictly increasing over `Sum = 0.00` to `0.30` eV on the scan's own grid.
*Reachable negative: a non-monotone response, which would mean the operator is being contaminated
by something other than the sum.*

**Ⓒ③ The interpolation in the sum is not the limiting error.**  The binned model rebuilt exactly
at an off-grid sum and the interpolated one agree to better than `0.1` of the smallest bin
uncertainty, at two off-grid sums.
*Reachable negative: an interpolation error comparable to the data error, which would make the
sampler's posterior an artefact of the grid.*

**Ⓓ④ THE SAMPLER CONVERGES.**  At least `4` independent chains over the five parameters; the
Gelman–Rubin `R̂ < 1.05` on EVERY parameter; the effective sample size on the sum `>= 1000`.
*Reachable negative: `R̂` above the threshold or too few effective samples, which would mean the
posterior is not yet measured whatever it says.*

**Ⓔ⑤ THE DECISIVE ARM — THE CONTROL LANDS NEAR THE PUBLISHED RESULT.**  Run the standard-model
control exactly as the check is run.  **Registered expectation: its `95` per cent upper limit on
the sum falls within a factor `1.5` of the published `64.2` meV — that is, inside `42.8` to `96.3`
meV — AND its fitted effective mass is NEGATIVE, the sign the published `-0.101` eV carries.**
*Reachable negative, and it is the outcome `r7836` actually got: the limit there was `26.5` meV, a
factor `2.42`, with the matter-density gap's sign reversed.  If this arm fails again, the arm of
record is NOT JUDGED again and the cause is measured, not described.*

**Ⓕ⑥ The gap's sign is the half that decides.**  The control's fitted matter-density gap against
the published `+2.48` per cent comes out POSITIVE.
*Reachable negative: a negative gap, which is `r7836`'s result and which no magnitude test would
have caught.*

**Ⓖ⑦ THEN THE ARM OF RECORD — and only if Ⓔ⑤ passes.**  Registered expectation: the construction's
own `95` per cent limit on the sum is **LOOSER** than the control's, because the construction's
`omega_cb` lever is weaker against its own distance scale.  Where `59` and `64` meV sit on the
posterior is reported either way.
*Reachable negative: a TIGHTER limit than the control's, which would be a finding against the
construction and is reported as one.*

**Ⓗ⑧ The arm count.**  The receipt asserts how many arms it ran.

## What is NOT claimed

* `P15` is not to change until the arm is read — the order says so and this revision holds to it.
* No limit on the sum will be reported for the construction unless Ⓔ⑤ passes.  A number the
  control cannot reproduce on the published case is not a measurement of the sky.
* The published bound is not in question in either direction; every arm here is a statement about
  this harness.

---

Node `60`, `r7838`, on order `r7833` (69), items ①–④.  Registered before any run.
