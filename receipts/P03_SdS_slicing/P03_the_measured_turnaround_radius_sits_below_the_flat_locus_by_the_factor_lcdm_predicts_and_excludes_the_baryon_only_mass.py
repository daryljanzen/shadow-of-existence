"""
P03_the_measured_turnaround_radius_sits_below_the_flat_locus_by_the_factor_lcdm_predicts_and_excludes_the_baryon_only_mass
=========================================================================================================================

Object under test -- node 66's work order in `FOR_60` (`r6837`): `PO-36`'s OBSERVATIONAL half, the row's only
remaining content and *the only confrontation in this programme that is neither microwave background nor
baryon acoustic distances.*  The order: take structures with independently determined dynamical masses and
ask whether the observed turnaround radius sits at (M_dyn alpha^2)^(1/3) or at (M_bary alpha^2)^(1/3), which
differ by f_b^(-1/3) = 1.85.  ** A literature pass and an arithmetic comparison.  Nothing is fitted -- the
order forbids it and nothing here would be improved by it. **

** THE ANSWER HAS THREE PARTS, AND THE MIDDLE ONE IS STRONGER THAN THE ORDER ASKED FOR. **

** (1) THE ORDER'S GUARD FIRES BEFORE THE MEASUREMENT DOES, AND IT FIRES ON A THIRD LOCUS RATHER THAN THE
TWO IT WARNED ABOUT. **  The order warned that force balance and density equality differ by 2^(1/3) and that
the literature is not uniform.  The literature turns out to be uniform and unambiguous -- and to report
neither of them as the corpus reads them:

  * Pavlidou & Tomaras (JCAP 2014, `arXiv:1401.3742`) give a MAXIMUM turnaround radius
    (3GM/Lambda c^2)^(1/3), "independently of cosmic epoch and the exact nature of dark matter".
    ** That is the corpus's r_HE identically -- the same formula, and the corpus's citation is exact. **
  * Korkidis et al. (A&A 639 A122, `arXiv:1912.08216`) measure R_ta KINEMATICALLY, as "the largest
    non-expanding scale around a center of gravity", in N-body only, and report that it is equivalent to
    `R_11`: a mean matter density contrast of delta ~ 11 at z = 0.

  ⇒ ** So the literature's R_ta is the ATTAINED radius and the corpus's r_HE is a BOUND on it.  They are not
  the same quantity, and comparing a measurement to the bound as though it were the prediction would read a
  systematic deficit as a discrepancy. **  The corpus's own comoving turnaround -- the density-equality
  radius -- is a THIRD locus, 2^(1/3) ABOVE r_HE, so identifying it with the literature's R_ta overpredicts
  by 2^(1/3)/0.734 = 1.72, larger than the 26% error the order named.

** (2) THE BOUND-TO-ATTAINED FACTOR IS NOT A FUDGE: IT IS FIXED BY Omega_Lambda/Omega_m AND NOTHING ELSE. **
The mean matter density inside the flat locus is exactly

      rho_bar(r_HE) / rho_m  =  2 Omega_Lambda / Omega_m  =  4.343   (Planck 2018)

-- M cancels, so it is one number for every structure.  Against the simulations' delta ~ 11 that gives

      R_ta / r_HE  =  (4.343/11)^(1/3)  =  0.734        and 0.713 if delta ~ 11 means rho/rho_m - 1

** The two readings of delta differ by 3% in the radius and the conclusion below survives both **, which is
why the ambiguity is reported rather than resolved.

** (3) THE MEASUREMENT EXISTS ONCE, IT AGREES, AND THE BARYON-ONLY READING IS EXCLUDED BY VIOLATING THE
BOUND RATHER THAN BY FITTING WORSE. **  The only observational turnaround radius with an independently
determined mass is the Milky Way (`arXiv:2105.04978`): r_ta = 839 +/- 121 kpc, kinematic, from the motions of
nearby dwarfs, and explicitly "independent from internal dynamics" -- so it is not circular on the mass.

      M_200m = 1.0e12 Msun ->  r_HE = 1.115 Mpc,  r_ta/r_HE = 0.753 +/- 0.109
      M_200m = 1.3e12 Msun ->  r_HE = 1.216 Mpc,  r_ta/r_HE = 0.690 +/- 0.100

** Both consistent with the 0.71--0.73 that LambdaCDM's own simulations give, with no parameter adjusted. **
And at the baryon-only mass f_b M_dyn the bound falls to 0.600--0.655 Mpc, which the measured 839 kpc
** EXCEEDS by 1.28 to 1.40. **  A maximum cannot be exceeded, in this construction for the same reason as in
LambdaCDM -- outside the flat locus the shell is carried off and cannot be part of the bound structure -- so
the baryon-only reading is not disfavoured but ** excluded, and excluded more strongly still if one uses the
Milky Way's actual, more concentrated baryonic mass rather than f_b M_dyn. **

  ⌗ WHICH IS THE OUTCOME THE ROW'S OWN SCOPING PREDICTED, AND IT IS REPORTED PLAINLY AS THE ORDER ASKED.
  `r6804` settled structurally that the bend takes whatever gravitates; the measurement agrees, so ** the row
  is confirmed rather than discriminated ** and the null result confirms the scoping instead of wasting it.

** ⚠ AND THE ORDER'S OWN TARGET -- RICH CLUSTERS -- HAS NO SUCH MEASUREMENT, WHICH IS THE OTHER HALF OF THE
ANSWER. **  Korkidis et al. is N-body; the 2024--25 work is still *searching* for a turnaround signature in
clusters with neural networks rather than quoting radii.  ** So on rich clusters the row stays open on data
that do not yet exist, not on nobody having looked ** -- and it stays open with the two arithmetic traps now
named, so the next pass makes neither.

COMPUTES: scope -- what this settles and what it must not be read as.
  * The loci are ESTABLISHED (`r1680`, `r6407`, `r6804`) and are re-run here as the calibration, not
    re-derived.  ** If f_b^(-1/3) = 1.8537 and 1/f_b = 6.369 and the 2^(1/3) guard do not reproduce, nothing
    below may be read. **  The banked rich-cluster pair 10.5/5.7 Mpc reproduces to 3% at H0 = 70,
    Omega_Lambda = 0.70 and to 6% at Planck 2018 -- ** a parameter-set difference, not a defect, and the
    RATIO 1.8537 on which the discrimination rests reproduces exactly. **
  * ⚠ ** NOTHING IS FITTED. **  Every number is an evaluation of a closed form at literature inputs.
  * ⚠ ** THE AGREEMENT IN (3) IS A CONSISTENCY STATEMENT, NOT A MEASUREMENT OF THE RATIO. **  The measured
    r_ta carries a 14% error, so the 2-sigma band on r_ta/r_HE spans roughly 0.53--0.97 and would admit a
    range of models.  ** The power of this pass is in (4), where the baryon-only reading falls OUTSIDE a
    bound, not in (3), where the dynamical reading falls inside a wide one. **  Said plainly because the
    reverse emphasis would overstate what one system with one error bar can carry.
  * ⚠ ** THE MILKY WAY IS NOT A RICH CLUSTER. **  The order asked for clusters; this is the one system where
    the test can presently be run at all, and it is reported as that and not generalised.
  * ⚠ ** M_200m UNDERSTATES THE MASS INSIDE r_ta **, so each ratio above is an UPPER estimate and the true
    ratio is smaller -- further below the bound, which strengthens (3) and does not weaken it.  Stated
    because the direction of a systematic matters more than its size here.
  * ⚠ `delta ~ 11` is read from an abstract whose stated parameters, "(Omega_m ~ 0.7; Omega_Lambda ~ 0.3)",
    are evidently transposed -- the simulations it uses are concordance runs.  Planck 2018 values are used
    and the transposition is reported rather than silently corrected; both readings of delta are carried.
  * ⚠ No two sources are averaged and no definition is mixed: each number is attributed to the source that
    reports it, with that source's own definition named, as the order required.
  * ⚠ This bears on f_b at the largest bound radius and on the loci's identification.  It is NOT a
    framework discriminator -- `r6407` and `r6804` already established that both frameworks take the same M
    -- and nothing here touches `PO-7` or the factor 6.37 unpinned in the local reading of Lambda.

ORIGIN: node 66's work order in `FOR_60` (`r6837`), taken directly.  The order's "uninteresting" outcome is
the one that occurred, and its instruction to report that plainly is followed; the bound violation in (3) and
the missing cluster data in the last note are the two things it did not anticipate.
"""
import sys

import sympy as sp

_checks = []


def check(label, ok):
    _checks.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    assert ok, label


print(__doc__)

# --- exact constants, named at the point of use ------------------------------
MPC = sp.Float('3.0856775814913673e22')          # m
GMSUN = sp.Float('1.32712440018e20')             # m^3 s^-2, IAU
H0_KMS = sp.Float('67.36')                       # Planck 2018 TT,TE,EE+lowE+lensing+BAO
OM = sp.Float('0.3153')
OL = sp.Float('0.6847')
OB = sp.Float('0.0493')
H0 = H0_KMS * 1000 / MPC

M, al, Lam, G, c = sp.symbols('M alpha Lambda G c', positive=True)


def r_HE_Mpc(M_solar, OmL=OL, H0_=H0):
    """the flat locus / Pavlidou--Tomaras maximum: r^3 = 3GM/(Lambda c^2) = GM/(H0^2 Omega_Lambda)"""
    return ((GMSUN * M_solar / (H0_ ** 2 * OmL)) ** sp.Rational(1, 3)) / MPC


# =========================================================================================
print("=" * 94)
print("PART 1 (C1) — THE ESTABLISHED LOCI AND CONSTANTS, BEFORE ANY DATUM IS TOUCHED")
print("=" * 94)
print("""
  The two radii and the two mass ratios are r1680/r6407/r6804's, not this receipt's.  They are re-run
  because every comparison below is read off them.
""")
r_force = (M * al ** 2) ** sp.Rational(1, 3)          # d^2r/dtau^2 = 0, the slice's flat locus
r_dens = (2 * M * al ** 2) ** sp.Rational(1, 3)       # density equality, the comoving turnaround
guard = sp.simplify(r_dens / r_force)
print(f"    force balance      r^3 = M alpha^2        -> r = {r_force}")
print(f"    density equality   r^3 = 2 M alpha^2      -> r = {r_dens}")
print(f"    the name guard     ratio = {guard} = {float(guard):.4f}")
check("the two loci differ by exactly 2^(1/3), M cancelling — the established name guard",
      sp.simplify(guard - 2 ** sp.Rational(1, 3)) == 0 and M not in guard.free_symbols)

# alpha^2 = 3/Lambda, so the flat locus IS (3GM/Lambda c^2)^(1/3): the Pavlidou--Tomaras form
r_force_phys = sp.simplify(r_force.subs(al, sp.sqrt(3 / Lam)))
pt_max = (3 * M / Lam) ** sp.Rational(1, 3)
print(f"    with alpha^2 = 3/Lambda:  {r_force_phys}   against Pavlidou–Tomaras  {pt_max}")
check("⚑ the flat locus and the literature's MAXIMUM turnaround radius are the SAME closed form, so the "
      "corpus's citation is exact rather than approximate",
      sp.simplify(r_force_phys - pt_max) == 0)

fb = OB / OM
print(f"\n    f_b = Omega_b/Omega_m = {float(fb):.5f}     f_b^(-1/3) = {float(fb ** sp.Rational(-1, 3)):.4f}"
      f"     1/f_b = {float(1 / fb):.3f}")
check("f_b^(-1/3) reproduces the banked 1.8537 to better than 0.2%",
      abs(float(fb ** sp.Rational(-1, 3)) - 1.8537) / 1.8537 < 2e-3)
check("1/f_b reproduces the banked 6.369 to better than 0.5%",
      abs(float(1 / fb) - 6.369) / 6.369 < 5e-3)

r15 = r_HE_Mpc(sp.Float('1e15'))
r15_70 = r_HE_Mpc(sp.Float('1e15'), sp.Float('0.70'), sp.Float('70.0') * 1000 / MPC)
print(f"    rich cluster M = 1e15: r_HE = {float(r15):.2f} Mpc (Planck 2018), "
      f"{float(r15_70):.2f} Mpc (H0=70, OL=0.70); banked pair 10.5 / 5.7 Mpc")
check("the banked rich-cluster radius reproduces to 3% at H0=70, Omega_Lambda=0.70 — a parameter-set "
      "difference and not a defect", abs(float(r15_70) - 10.5) / 10.5 < 0.03)
check("and the PAIR's ratio, which is what the discrimination rests on, reproduces exactly",
      abs(float(r15 / r_HE_Mpc(sp.Float('1e15') * fb)) - float(fb ** sp.Rational(-1, 3))) < 1e-9)

# =========================================================================================
print()
print("=" * 94)
print("PART 2 — THE MEAN OVERDENSITY INSIDE THE FLAT LOCUS: ONE NUMBER FOR EVERY STRUCTURE")
print("=" * 94)
print("""
  The bound-to-attained comparison needs the density inside the bound, and it is parameter-free in M.
""")
H0s, G_, c_ = sp.symbols('H_0 G c', positive=True)
r_cubed = 3 * G_ * M / (Lam * c_ ** 2)
rho_bar = sp.simplify(3 * M / (4 * sp.pi * r_cubed))
rho_m = OM * 3 * H0s ** 2 / (8 * sp.pi * G_)
ratio_sym = sp.simplify((rho_bar / rho_m).subs(Lam * c_ ** 2, 3 * H0s ** 2 * OL))
print(f"    rho_bar(r_HE) = {rho_bar}        (M has cancelled)")
print(f"    rho_bar/rho_m = {sp.nsimplify(ratio_sym, rational=False)} = {float(ratio_sym):.4f}")
check("⚑ the overdensity inside the flat locus is 2 Omega_Lambda/Omega_m exactly, with M cancelled — so it "
      "is one number for every structure and nothing was chosen",
      M not in sp.simplify(ratio_sym).free_symbols
      and abs(float(ratio_sym) - float(2 * OL / OM)) < 1e-12)

DELTA_SIM = sp.Integer(11)                        # Korkidis et al. 2020: R_ta is equivalent to R_11
frac_a = (ratio_sym / DELTA_SIM) ** sp.Rational(1, 3)
frac_b = (ratio_sym / (DELTA_SIM + 1)) ** sp.Rational(1, 3)
print(f"""
    against the simulations' delta ~ 11:
      R_ta/r_HE = {float(frac_a):.4f}   reading delta as rho/rho_m
      R_ta/r_HE = {float(frac_b):.4f}   reading delta as rho/rho_m - 1
""")
check("the two readings of delta differ by less than 3% in the radius, so the ambiguity is reportable "
      "rather than fatal", abs(float(frac_a) - float(frac_b)) / float(frac_a) < 0.03)
check("and the attained radius is strictly INSIDE the bound under either reading, which is the direction "
      "the bound requires", float(frac_a) < 1 and float(frac_b) < 1)

naive = sp.simplify(2 ** sp.Rational(1, 3) / frac_a)
print(f"    ⚠ identifying the corpus's comoving turnaround with the literature's R_ta overpredicts by "
      f"2^(1/3)/{float(frac_a):.4f} = {float(naive):.3f}")
check("that trap is LARGER than the 26% one the order named, which is why it is reported",
      float(naive) - 1 > float(guard) - 1)

# =========================================================================================
print()
print("=" * 94)
print("PART 3 — THE ONE MEASUREMENT: THE MILKY WAY, AND IT IS NOT CIRCULAR ON THE MASS")
print("=" * 94)
print("""
  arXiv:2105.04978 measures r_ta = 839 +/- 121 kpc from the motions of nearby dwarfs, kinematically (the
  outermost edge of infalling material) and explicitly independent of internal dynamics -- so the mass it is
  tested against is not the quantity the radius was read from.
""")
R_TA = sp.Float('0.839')                          # Mpc
R_TA_ERR = sp.Float('0.121')
print(f"    {'M_200m [Msun]':>14} {'r_HE [Mpc]':>11} {'r_ta/r_HE':>12} {'+/-':>7}   {'verdict':>28}")
ratios = []
for Mv in ('8.0e11', '1.0e12', '1.3e12', '1.5e12'):
    r = r_HE_Mpc(sp.Float(Mv))
    q, qe = float(R_TA / r), float(R_TA_ERR / r)
    ratios.append((q, qe))
    ok = abs(q - float(frac_a)) < 2 * qe
    print(f"    {float(Mv):>14.2e} {float(r):>11.4f} {q:>12.4f} {qe:>7.4f}   "
          f"{'consistent with 0.734 (2 sigma)' if ok else 'outside 2 sigma':>28}")
check("⚑ the measured ratio is consistent with LambdaCDM's own simulated 0.734 across the whole plausible "
      "Milky Way mass range, with nothing adjusted",
      all(abs(q - float(frac_a)) < 2 * qe for q, qe in ratios))
check("and every ratio is below 1, so the measurement respects the bound the construction derives",
      all(q + qe < 1.15 and q < 1 for q, qe in ratios))

# =========================================================================================
print()
print("=" * 94)
print("PART 4 — AND THE BARYON-ONLY MASS IS EXCLUDED BY VIOLATING THE BOUND, NOT BY FITTING WORSE")
print("=" * 94)
print("""
  The order asked which of two radii the measurement sits at.  It sits at one of them and OUTSIDE the other.
""")
viol = []
for Mv in ('1.0e12', '1.3e12'):
    rb = r_HE_Mpc(sp.Float(Mv) * fb)
    over = float(R_TA / rb)
    viol.append(over)
    print(f"    M_bary = f_b x {float(Mv):.1e} -> bound {float(rb):.4f} Mpc;  measured/bound = {over:.3f}"
          f"   {'⛔ EXCEEDS THE BOUND' if over > 1 else 'inside'}")
check("⚑ at the baryon-only mass the measured radius EXCEEDS the maximum, so that reading is excluded "
      "rather than disfavoured", all(v > 1 for v in viol))
check("and it is exceeded by more than the measurement's own fractional error, so the exclusion is not an "
      "error-bar artefact", all(v - 1 > float(R_TA_ERR / R_TA) for v in viol))
# the Milky Way's ACTUAL baryons are more concentrated than f_b M_dyn, which worsens it
M_BARY_MW = sp.Float('1.0e11')                    # disc + bulge + hot halo, order of magnitude
rb_actual = r_HE_Mpc(M_BARY_MW)
print(f"    and with the Milky Way's actual baryonic mass ~1e11 Msun: bound {float(rb_actual):.4f} Mpc, "
      f"measured/bound = {float(R_TA / rb_actual):.2f}")
check("using the real baryonic mass rather than f_b M_dyn worsens the violation, so the exclusion does not "
      "depend on the cosmic f_b being the right baryon budget",
      float(R_TA / rb_actual) > max(viol))

# =========================================================================================
print()
print("=" * 94)
print("VERDICT")
print("=" * 94)
print(f"""
  ⚑ THE ROW'S EXPECTED OUTCOME, REACHED BY A STRONGER ROUTE THAN EXPECTED.

    the definitions        the literature's R_ta is the ATTAINED radius; the corpus's r_HE is the BOUND on
                           it and is Pavlidou–Tomaras's maximum IDENTICALLY; the corpus's comoving
                           turnaround is a THIRD locus, 2^(1/3) above r_HE
    the bound-to-attained  rho_bar(r_HE)/rho_m = 2 OL/Om = {float(ratio_sym):.3f} exactly, so with delta ~ 11
                           R_ta/r_HE = {float(frac_a):.3f} ({float(frac_b):.3f} on the other reading of delta)
    the measurement        Milky Way r_ta = 839 +/- 121 kpc: r_ta/r_HE = {ratios[1][0]:.3f} +/- {ratios[1][1]:.3f}
                           at M_200m = 1e12 -- consistent, nothing adjusted, and a WIDE band
    the discrimination     at the baryon-only mass the measured radius EXCEEDS the maximum by
                           {min(viol):.2f}--{max(viol):.2f}, so that reading is EXCLUDED

  ⇒ SO THE OBSERVED TURNAROUND RADIUS TRACKS THE DYNAMICAL MASS, as `r6804` entailed structurally and as
    both frameworks predict.  ** The row is confirmed, not discriminated, and that is what its own scoping
    said it would be. **

  ⚠ AND ON RICH CLUSTERS -- THE ORDER'S ACTUAL TARGET -- THERE IS NO SUCH MEASUREMENT: the cluster work is
    N-body, and the recent observational effort is still searching for the signature rather than quoting
    radii.  ** The row stays open there on data that do not exist yet, with both arithmetic traps named. **
""")
print(f"  {sum(_checks)}/{len(_checks)} checks passed.")
sys.exit(0 if all(_checks) else 1)
