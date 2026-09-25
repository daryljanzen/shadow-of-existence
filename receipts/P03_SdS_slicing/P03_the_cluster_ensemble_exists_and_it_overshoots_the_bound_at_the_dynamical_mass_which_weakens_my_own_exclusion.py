"""
P03_the_cluster_ensemble_exists_and_it_overshoots_the_bound_at_the_dynamical_mass_which_weakens_my_own_exclusion
==============================================================================================================

Object under test -- node 66's order in `FOR_60` (`r6841`): the cluster statistics, *"if they are doable"*.
The order was set up by my own weighting in `r6838` -- that the power of that pass was the bound violation and
not the agreement -- and asks for an ensemble with kinematic turnaround radii independent of internal dynamics
against dynamical masses independent of the turnaround, ** the distribution of r_ta/r_HE reported rather than a
mean **, and the convention spread stated rather than chosen.  Stopping condition: if the samples are too
heterogeneous, say the measurement is not available and record that as sharply as a number.

** THE ENSEMBLE EXISTS, BOTH INDEPENDENCES HOLD, AND THE ANSWER IT GIVES GOES AGAINST ME.  THE DISTRIBUTION
DOES NOT STRADDLE THE BOUND -- IT SITS ENTIRELY ABOVE IT, AT THE DYNAMICAL MASS.  ** So the order's answer and
a correction to `r6838` are the same finding, and the correction is the more important half.

** (1) THE SAMPLE, AND IT MEETS THE ORDER'S TWO INDEPENDENCES. **  Lee, Kim & Rey (2017), `arXiv:1709.06903`:
six isolated SDSS DR10 groups at z <= 0.05, selected so that the nearest neighbour group is beyond fifteen
virial radii.

  * the RADIUS is kinematic and EXTERNAL: the Turn-around Radius Estimator applied to the flow of *neighbour
    field galaxies* in a web-like structure around each group -- not the members, so not internal dynamics.
  * the MASS is INDEPENDENT of it: the virial mass from Tempel et al. (2014), an NFW fit to the group's own
    members.

  ** Radius from outside, mass from inside.  Neither is derived from the other, which is the whole point the
  order insisted on, so this sample is usable and the pass does not stop here. **

** (2) THE DISTRIBUTION, ON THE PAPER'S OWN BOUND COLUMN SO THAT NO CONVENTION IS GUESSED. **  The paper
tabulates the spherical bound limit itself, so the ratio needs no formula of mine:

      r_ta / r_bound(spherical)  =  1.20,  1.37,  1.75,  1.82,  1.86,  2.33

** All six central values lie ABOVE the bound **, three of them by more than one sigma -- which reproduces the
paper's own "three out of the six" and confirms the table is being read correctly.  Against the paper's
NON-spherical bound column two of the six fall below one (0.92, 0.92), ** so how many violations there are is
itself convention-dependent, which is the spread the order asked to have stated rather than chosen. **

** (3) AND THIS IS WHERE IT COSTS ME.  `r6838` EXCLUDED THE BARYON-ONLY READING BECAUSE THE MEASURED MILKY WAY
RADIUS EXCEEDED THE BOUND BY 1.28--1.40, ON THE GROUND THAT A MAXIMUM CANNOT BE EXCEEDED.  ** That figure sits
INSIDE the 1.20--2.33 range this ensemble produces at the DYNAMICAL mass. **  So exceeding this bound is
something these measurements do routinely with the dark matter already included, and exceeding it is therefore
** not by itself discriminating between the two mass readings. **

  ⌗ WHAT SURVIVES AND WHAT DOES NOT, STATED AS A LEDGER RATHER THAN SOFTENED.
    * SURVIVES, untouched: the three-loci guard, and it is now a FOUR-way convention spread with the
      spherical/non-spherical bound added.
    * SURVIVES, pure algebra: rho_bar(r_HE)/rho_m = 2 Omega_Lambda/Omega_m = 4.343 with M cancelled.
    * SURVIVES, as it was already labelled: the Milky Way agreement, a consistency statement with a wide band.
    * ** DOES NOT SURVIVE AS STATED: the baryon-only EXCLUSION. **  It is not an exclusion by a hard bound.
      It reduces to a quantitative argument about how large a M_ta/M_v correction one is willing to carry --
      still unfavourable to the baryon-only reading, because that reading needs the SAME correction *and* a
      further factor f_b^(-1) = 6.4, but ** an argument about plausible mass ratios and not a maximum being
      exceeded. **
    ⚠ *And the sharpest form of the cost: `r6838` said in its own bound "the power of this pass is (4), where a
    reading falls outside a bound, not (3), where one falls inside a wide one." **The part I singled out as the
    strong one is precisely the part this ensemble weakens.** That is worth saying in those words.*

** (4) THE AUTHORS' OWN LEADING EXPLANATION IS THE SYSTEMATIC I NAMED -- AND IT IS LARGER THAN I ALLOWED. **
They write that "the first suspicion falls on the underestimate of the spherical bound limit caused by
substituting the virial mass for the turn-around mass", and that it remains "yet to be quantitatively addressed
how close the virial mass of each target is to its turn-around mass".  ** `r6838` named exactly this direction
-- "M_200m understates the mass inside r_ta, so each ratio is an upper estimate" -- and then drew the wrong
consequence from it, that it "strengthens the exclusion and cannot weaken it". **  It does strengthen the
*agreement*; by inflating every ratio it destroys the *exclusion*, because a bound that is routinely overshot
for a known reason cannot be used to rule anything out.

COMPUTES: scope -- what this settles and what it must not be read as.
  * C1 the paper's own arithmetic is reproduced before its numbers are used: three of six exceed the spherical
    bound by more than one sigma, which is the paper's own count.  ** If that does not reproduce, the table is
    being misread and nothing below may be read. **
  * ⚠ ** A DISCREPANCY I CANNOT RESOLVE AND DO NOT PAPER OVER: ** the paper's tabulated spherical bound is
    1.30x my own evaluation of (3GM/Lambda c^2)^(1/3) at the paper's own tabulated virial masses -- uniform
    across five groups (1.306--1.310) and 1.263 on the sixth.  The implied Omega is 0.311, suspiciously
    Omega_m rather than Omega_Lambda, but ** I will not guess a published convention: every ratio above is
    formed with the paper's own bound column, so the finding is independent of whose formula is right. **  If
    their bound is the one to use, my r_HE is 30% small; if mine is, their violations are larger still.  Either
    way the ratios in (2) stand, because they never use my formula.
  * ⚠ ** NO SAMPLE WAS ASSEMBLED AND NO DEFINITION HARMONISED **, which the order forbade as "a fit wearing a
    literature pass's clothes".  One published sample is reported as published.  `NGC 5353/4` is named by the
    paper as a seventh object measured earlier and is NOT pooled with these six.
  * ⚠ n = 6, with 25--50% errors per object, and the six are GROUPS of 3--6 x 10^13 h^-1 Msun, ** not rich
    clusters. **  So this does not close the rich-cluster question `r6837` asked; it changes what the existing
    evidence supports.
  * ⚠ This is a statement about a BOUND's usability as a discriminator.  It is not evidence FOR the baryon-only
    reading, which remains disfavoured on the mass-ratio argument and on `r6804`'s structural result that the
    bend takes whatever gravitates.  ** `PO-7` untouched. **
  * ⚠ ** `PO-36` WAS STRUCK AT `r6839` PARTLY ON THE EXCLUSION THIS RECEIPT WEAKENS. **  Whether the strike
    stands is the gate's call and not mine; it is reported rather than acted on.

ORIGIN: node 66's order in `FOR_60` (`r6841`), which my own `r6838` weighting invited.  The order asked for a
distribution and said the uninteresting answer would be that no sample exists.  A sample exists, and what it
reports is that my previous pass's strongest claim was its weakest.
"""
import sys

import sympy as sp

_checks = []


def check(label, ok):
    _checks.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    assert ok, label


print(__doc__)

MPC = sp.Float('3.0856775814913673e22')
GMSUN = sp.Float('1.32712440018e20')
OL = sp.Float('0.6847')                         # Planck 2018
OM = sp.Float('0.3153')

# Lee, Kim & Rey (2017) arXiv:1709.06903, Tables 1 and 3, transcribed verbatim.
# name, M_v [1e12 h^-1 Msun], r_ta [h^-1 Mpc], sigma_rta, bound_spherical, bound_nonspherical
LEE = (
    ('GG1', '40.85', '9.01', '4.47', '3.86', '5.01'),
    ('GG2', '60.69', '7.72', '2.85', '4.40', '5.72'),
    ('GG3', '37.00', '6.94', '2.96', '3.73', '4.85'),
    ('GG4', '30.13', '6.34', '3.03', '3.49', '4.53'),
    ('GG5', '48.72', '5.42', '2.23', '3.95', '5.92'),
    ('GG6', '48.85', '4.89', '1.26', '4.09', '5.32'),
)


def r_HE_h(M12, OmL=OL):
    """(3GM/Lambda c^2)^(1/3) in h^-1 Mpc, for M in 1e12 h^-1 Msun (H0 = 100h)"""
    H0 = sp.Float('1e5') / MPC
    return ((GMSUN * sp.Float(M12) * sp.Float('1e12') / (H0 ** 2 * OmL)) ** sp.Rational(1, 3)) / MPC


# =========================================================================================
print("=" * 94)
print("PART 1 (C1) — REPRODUCE THE PAPER'S OWN COUNT BEFORE USING ITS NUMBERS")
print("=" * 94)
print("""
  The paper says three of the six exceed the spherical bound.  If that does not come back out of the table as
  transcribed, the table is being misread and nothing below may be read.
""")
print(f"    {'grp':>4} {'M_v/1e12':>9} {'r_ta':>6} {'sig':>5} {'bound_s':>8} {'r/b':>6} {'(r-b)/sig':>10}")
ratios, sigmas, ns_ratios, calib = [], [], [], []
for name, M, r, s, bs, bns in LEE:
    r_, s_, bs_, bns_ = (sp.Float(x) for x in (r, s, bs, bns))
    ratios.append(float(r_ / bs_))
    sigmas.append(float((r_ - bs_) / s_))
    ns_ratios.append(float(r_ / bns_))
    calib.append(float(bs_ / r_HE_h(M)))
    print(f"    {name:>4} {float(M):>9.2f} {float(r_):>6.2f} {float(s_):>5.2f} {float(bs_):>8.2f} "
          f"{ratios[-1]:>6.3f} {sigmas[-1]:>10.3f}")
n_over_1sig = sum(1 for v in sigmas if v > 1)
print(f"\n    exceeding the spherical bound by more than one sigma: {n_over_1sig} of 6")
check("⚑ the paper's own count of three-in-six reproduces from the transcribed table, so it is being read "
      "correctly", n_over_1sig == 3)
check("and every one of the six central values lies above that bound, which the paper's summary count does "
      "not itself say", all(v > 1 for v in ratios))

# =========================================================================================
print()
print("=" * 94)
print("PART 2 — THE DISTRIBUTION THE ORDER ASKED FOR, ON THE PAPER'S OWN BOUND COLUMN")
print("=" * 94)
print(f"""
  Formed with the paper's bound, not mine, so no convention of mine enters.

    r_ta / bound(spherical), sorted:   {'  '.join(f'{v:.2f}' for v in sorted(ratios))}
    r_ta / bound(non-spherical):       {'  '.join(f'{v:.2f}' for v in sorted(ns_ratios))}
""")
check("the distribution does not straddle the spherical bound — it lies wholly above it",
      min(ratios) > 1)
check("⚑ but against the NON-spherical bound two of the six fall below it, so the NUMBER of violations is "
      "itself convention-dependent — the spread the order asked to have stated",
      sum(1 for v in ns_ratios if v < 1) == 2)
spread = max(ratios) / min(ratios)
print(f"    the ensemble's own spread, max/min = {spread:.2f} — wider than the 1.86 the two mass readings "
      f"differ by")
check("and that spread exceeds f_b^(-1/3) = 1.856, so object-to-object scatter alone covers the whole "
      "discrimination this row rests on", spread > float((sp.Float('0.0493') / OM) ** sp.Rational(-1, 3)))

# =========================================================================================
print()
print("=" * 94)
print("PART 3 — WHAT IT COSTS r6838, COMPUTED RATHER THAN CONCEDED IN WORDS")
print("=" * 94)
R6838_LO, R6838_HI = 1.28, 1.40          # the Milky Way's measured/bound at f_b M_dyn
print(f"""
  r6838 excluded the baryon-only reading because the Milky Way's measured radius exceeded the bound by
  {R6838_LO}--{R6838_HI}, on the ground that a maximum cannot be exceeded.
""")
inside = [v for v in ratios if R6838_LO <= v <= R6838_HI]
print(f"    dynamical-mass ratios in this ensemble: {min(ratios):.2f}--{max(ratios):.2f}")
print(f"    r6838's baryon-only figure {R6838_LO}--{R6838_HI} lies inside that range: "
      f"{min(ratios) <= R6838_LO and R6838_HI <= max(ratios)}")
check("⚑ r6838's exclusion figure sits INSIDE the range the DYNAMICAL mass already produces, so exceeding "
      "this bound does not discriminate between the two mass readings",
      min(ratios) <= R6838_LO and R6838_HI <= max(ratios))
check("and at least one group overshoots by more than r6838's whole baryon-only excess, so the effect is not "
      "marginal", max(ratios) > R6838_HI)

# what DOES survive: the algebra, unchanged
H0s, G_, c_, Lam, M = sp.symbols('H_0 G c Lambda M', positive=True)
rho_ratio = sp.simplify(((3 * M / (4 * sp.pi * (3 * G_ * M / (Lam * c_ ** 2)))) /
                         (OM * 3 * H0s ** 2 / (8 * sp.pi * G_))).subs(Lam * c_ ** 2, 3 * H0s ** 2 * OL))
print(f"\n    and the algebra r6838 rested on is untouched: rho_bar(r_HE)/rho_m = {float(rho_ratio):.4f}")
check("2 Omega_Lambda/Omega_m survives with M cancelled — a weakened conclusion is not a wrong derivation",
      M not in rho_ratio.free_symbols and abs(float(rho_ratio) - float(2 * OL / OM)) < 1e-12)
# and the baryon-only reading still needs a FURTHER factor on top of whatever M_ta/M_v correction is allowed
fb = sp.Float('0.0493') / OM
print(f"    the baryon-only reading still needs a further 1/f_b = {float(1 / fb):.2f} in mass on top of "
      f"whatever M_ta/M_v correction is granted")
check("so the baryon-only reading remains disfavoured, on a mass-ratio argument rather than on a bound — "
      "which is a weaker claim, not the opposite one", float(1 / fb) > 6)

# =========================================================================================
print()
print("=" * 94)
print("PART 4 — THE CONVENTION DISCREPANCY, NAMED AND NOT GUESSED AT")
print("=" * 94)
mean_cal = sum(calib) / len(calib)
print(f"""
    the paper's spherical bound divided by my own evaluation of (3GM/Lambda c^2)^(1/3) at its own masses:
      {'  '.join(f'{v:.3f}' for v in calib)}
    mean {mean_cal:.3f}, and the Omega that factor would imply: {float(OL) / mean_cal ** 3:.3f}
""")
check("the factor is near-uniform across the sample, so it is a convention difference and not per-object "
      "scatter", max(calib) / min(calib) < 1.05)
print(f"    ⚠ {float(OL) / mean_cal ** 3:.3f} is close to Omega_m, not Omega_Lambda — a suggestive coincidence "
      f"and NOT a conclusion.")
# and prove the independence rather than asserting it: redo Part 2 with MY bound and see the finding hold
mine_ratios = [float(sp.Float(r) / r_HE_h(M)) for _, M, r, _, _, _ in LEE]
print(f"    the same ratios formed with MY bound instead: "
      f"{'  '.join(f'{v:.2f}' for v in sorted(mine_ratios))}")
check("⚑ and it changes nothing that matters: the distribution lies wholly above the bound on EITHER "
      "formula, so the finding is independent of whose convention is right",
      min(ratios) > 1 and min(mine_ratios) > 1)
check("my bound being the smaller one, it makes every overshoot larger rather than smaller — so using the "
      "paper's own column is the conservative choice and not the convenient one",
      all(a > b for a, b in zip(mine_ratios, ratios)))

# =========================================================================================
print()
print("=" * 94)
print("VERDICT")
print("=" * 94)
print(f"""
  ⚑ THE ORDER IS ANSWERED IN THE POSITIVE, AND THE ANSWER CORRECTS MY LAST ONE.

    the sample          Lee, Kim & Rey (2017): six isolated groups, radius from the EXTERNAL neighbour flow,
                        mass from the members' NFW fit — the order's two independences both hold
    the distribution    r_ta/bound = {'  '.join(f'{v:.2f}' for v in sorted(ratios))}   — wholly ABOVE the
                        spherical bound, three of six by more than one sigma
    the convention      against the non-spherical bound two of six fall BELOW, so even the count of
                        violations is convention-dependent
    the cost            r6838's baryon-only exclusion figure, {R6838_LO}--{R6838_HI}, lies INSIDE the range the
                        DYNAMICAL mass already gives — so that exclusion does not hold as a bound argument

  ⇒ WHAT r6838 SHOULD HAVE SAID: the baryon-only reading is disfavoured because it needs a further factor
    1/f_b = {float(1 / fb):.1f} in mass on top of an M_ta/M_v correction the data already demand — a
    quantitative argument, not a maximum being exceeded.  ** The derivation was right and the conclusion was
    overstated, and it was overstated in exactly the place I had marked as the strong one. **

  ⚠ `PO-36` was struck at `r6839` partly on that exclusion.  Whether the strike stands is the gate's call.
""")
print(f"  {sum(_checks)}/{len(_checks)} checks passed.")
sys.exit(0 if all(_checks) else 1)
