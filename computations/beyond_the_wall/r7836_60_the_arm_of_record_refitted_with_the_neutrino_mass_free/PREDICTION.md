# r7836 (60) — PREDICTION: the arm of record refitted with the neutrino mass free

**On order `r7831` (69), added clause, routed from 72.** Registered and pushed **before any run**,
under the row-claim rule. Nothing below has been measured yet; every figure is either read from a
banked source (and said to be) or a registered expectation.

## What the order asks

① Add massive neutrinos to the arm of record's instrument — three species, normal ordering, a free
sum; relativistic in the early rate and the driving, nonrelativistic in the late dust the distances
see, with the geometric dust term's total carrying their late mass so that `ω_cb = Ω_m h² − ω_ν`.
② Refit the leaf-geometry arm on the 185-bin lensed configuration with the sum free beside the four
parameters, jointly with DESI DR2 BAO on the leaf ruler; run the control the same way.
③ Report the profile on the sum, the 95 per cent upper limit, and where 59 and 64 meV sit on it.

## What is READ, not run

- the arm of record's leaf-geometry refit minimum, `(68.585672, 0.294463, 0.022181, 0.961379)`, from
  `receipts/P15_CR_cosmology/P15_with_the_projection_distance_on_the_leaf_rate_the_refitted_spectrum_is_level_with_the_control_and_the_bao_fit_does_not_move.py`;
- the distances' point `(68.60, 0.2973)`, from the same receipt;
- 72's working estimate in
  `computations/l550_neutrino_mass_on_the_construction/the_matter_density_gap_that_drives_the_mass_bound.py`,
  which the order itself says **decides nothing**;
- the published standard-model bound it is to be checked against, `Σ < 64.2` meV at 95 per cent with
  an effective mass of `−0.101` eV when allowed negative (`arXiv:2503.14744`);
- the instrument, `computations/beyond_the_wall/ACOUSTIC_two_arm.py`, and the refit harness,
  `computations/beyond_the_wall/r7749_70_leafgeom_refit/refit.py`, with its grid
  `r7093_directions/grid_oneclock_leafrec1`.

## What the instrument does NOT currently carry, established by reading it

The generator has **no massive-neutrino knob**: it carries massless free-streaming neutrinos (the
hierarchy at `LN`), `FNU` for the neutrino share of `Ω_r`, and `DNEFF` for a consistent `ΔN_eff`.
There is no `MNU` and no `omnuh2`. So ① is a real extension and not a flag.

**Where the mass has to enter, from the instrument's own consumption of `Ω_m`:** the rate and the
distances and `Ω_Λ = 1 − Ω_m` take the TOTAL (lines forming `OL`, the two rate functions and the
stack `_rt`), while the clustering matter the perturbations see is `OCDM = OM − OB` and the matter
fraction `Om_of`. So the separation the order describes is exactly: leave the total alone, and take
`ω_ν` out of the clustering part.

## THE ARMS, registered as COMPARISONS with reachable negatives

**Ⓐ① The implementation is reachable at the reporting path.** Setting the sum moves the clustering
density and leaves the distances' rate untouched, both visible in the header the instrument prints.
*Negative branch:* it moves `D_M`, `r_s` or `l_A`, in which case the separation is wrong and the arm
fails rather than being quietly reinterpreted.

**Ⓑ② The two-limit treatment is licensed on this configuration, not assumed.** The neutrinos must
still be relativistic at recombination for the early sector to be unchanged at fixed `ω_cb`. I
expect the nonrelativistic transition `1+z ≈ 1890 (m/eV)` to fall at `z ≲ 40` for a lightest mass of
a few meV to a few tens of meV, which is far below `z_rec ≈ 1090`. *Negative branch:* if the
transition reaches within a decade of recombination anywhere in the scanned range, the two-limit
treatment is not licensed there and the arm reports the range it is not licensed on.

**Ⓒ③ The control reproduces the published effective mass when run the same way.** This is the
check on the whole apparatus, and it is the arm that can most usefully fail. *Negative branch:* the
control lands far from the published figure, in which case nothing is concluded about the arm and
the report says so.

**Ⓓ④ THE REGISTERED EXPECTATION, and it is a comparison and not a hope.** The order's reasoning is
that the standard model's matter-density gap has the CMB ABOVE the distances, which pulls the mass
negative, while this arm sits BELOW them, which should push it positive. So I register:
**the arm's 95 per cent upper limit on `Σ` is LOOSER than the standard model's `64.2` meV.**
*Negative branch, and it is reachable:* the limit comes out TIGHTER than the control's, which would
mean the sign argument does not survive the joint refit — and that is a finding against the
construction, to be reported as one.

**Ⓔ⑤ The gap's sign at the fitted point, measured rather than inherited.** 72's estimate reads the
arm `1.00` per cent below the distances from the banked minimum. Refitted with the sum free, I
expect the sign to hold — the arm's `ω_m` below the distances'. *Negative branch:* the sign reverses
once the sum is free, which would withdraw the premise the order's expectation rests on.

**Ⓕ⑥ Where 59 and 64 meV sit.** I register that **both lie inside the arm's 95 per cent interval**,
since Ⓓ④ expects a looser limit than 64.2 meV. *Negative branch:* either falls outside, which is
reported as the prediction failing at that value.

**Ⓖ⑦ The scaled estimate is NOT reproduced as a prediction.** 72's `+0.04` eV comes from scaling the
standard model's crude-to-full ratio onto this arm, and the order calls it an estimate that decides
nothing. I register that the refit's own profile is the only figure reported as a result, and that
the estimate is quoted as what it is. *Negative branch:* none — this arm is a scope statement and
fails only if the report presents the estimate as a measurement.

## WHAT IS NOT CLAIMED

- **Not** that this construction predicts a neutrino mass: the sum is inherited boundary data here,
  as `η` and the tilt are, and the fit bounds it rather than deriving it.
- **Not** that a looser limit is evidence for the construction: it is the absence of one tension,
  not the presence of a success.
- **Not** that the two-limit treatment is a full massive hierarchy. It is the treatment the order
  specifies, its licence is Ⓑ②, and anything the full hierarchy would add above that licence is out
  of scope and will be named as such.
- **Not** that `P15`'s text changes on this pass. The order forbids it before the run lands.

## ARM COUNT

**Seven arms registered: Ⓐ① Ⓑ② Ⓒ③ Ⓓ④ Ⓔ⑤ Ⓕ⑥ Ⓖ⑦.** The count is asserted at the end of the receipt,
and a failed arm is reported AS failed with its criterion unchanged.
