#!/usr/bin/env python3
"""
RECEIPT -- P15: ** THE DIFFUSION-DAMPING SHEAR COEFFICIENT, DERIVED FROM THE PHOTON HIERARCHY WITH
POLARISATION INSTEAD OF REMEMBERED FROM A TEXTBOOK OR CHOSEN BY A FIT.  THE POLARISATION CORRECTION
COMES OUT AS A FACTOR 1.1996 AGAINST 6/5 -- THREE PARTS IN TEN THOUSAND -- AND THE COEFFICIENT IS
16/15.  ** IT COSTS THE CONTROL 1123 UNITS OF chi^2 AND IS ADOPTED ANYWAY. **

Built r2376+c54.177, front #2.  Instrument:
`computations/beyond_the_wall/L171w_hierarchy_damping_coefficient.py`.

===================================================================================================
** WHAT WAS OWED, AND BY WHOM. **
===================================================================================================

The damping is applied as exp(-k^2/k_D^2) with 1/k_D^2 = INT [R^2/(1+R) + C]/[6(1+R)tau'] d(eta),
and C has never been derived in this corpus.  ** `C8_diffusion_length.py` has named the ambiguity in
its own text since it was written -- "the 8/9 coefficient against the 16/15 polarization-corrected
one" -- and uses 8/9. **  At c54.176 I set it to 16/15 on recollection and put it straight back,
because a remembered number is not a derivation; in the same revision chi^2 through plik_lite was
found to prefer 8/9 by 1123 units, and that preference was recorded and refused.  ** Both refusals
stand.  This file removes the ambiguity by measuring C. **

** THE METHOD, AND WHY IT CARRIES NO FITTED PREFACTOR. **  Two integrations of the same oscillator on
the same background, differing in exactly one thing: the REFERENCE is the perfect tight-coupled
fluid, undamped by construction; the HIERARCHY carries photons to l = 24 with Thomson scattering and
the polarisation multipoles evolved alongside, with the baryons on their own velocity coupled
through tau'(theta_g - theta_b)/R.  ** Their ratio is the damping and nothing else: the (1+R)^(1/4)
WKB prefactor, the drift of c_s and the R-dependence of the oscillation are common to both and
divide out identically. **  Gravity is off in both, which is not an approximation but the definition
of the object -- the WKB damping formula is a statement about the FREE oscillator.

  PART 1  ** THE UNPOLARISED HIERARCHY RETURNS 8/9. **  With G = 0 the l = 2 scattering term is
          -(9/10)tau' F_2, which is the textbook unpolarised closure and a physical limit rather
          than a mutilation.  Extrapolated to zero k/tau': C = 0.8852 against 0.8889.
  PART 2  ** THE POLARISED HIERARCHY RETURNS 16/15. **  C = 1.0618 against 1.0667.
  PART 3  ** AND THE RATIO -- WHICH IS THE QUANTITY ACTUALLY IN DISPUTE -- IS 1.1996 AGAINST 6/5. **
          *Both absolute values sit about half a per cent low and the shift is proportional to C, so
          it is a common normalisation that cancels in the ratio.  The ratio is the derivation; the
          absolute agreement at half a per cent is the corroboration.*
  PART 4  ** THE k^2 SCALING IS MEASURED AND NOT ASSUMED. **  C is read LOCALLY, between consecutive
          extrema, and plotted against (k/tau')^2: the points fall on a line whose intercept is the
          coefficient and whose slope is the finite-(k/tau') correction the WKB derivation drops.
          *A cumulative reading smears that correction over the interval and cannot separate "the
          coefficient is not 8/9" from "we are reading a leading-order formula at finite k/tau'".*
  PART 5  ** SO THE COEFFICIENT IS 16/15, AND ADOPTING IT MAKES THE CONTROL WORSE. **  chi^2/dof
          goes 22.5 -> 28.6 on the LambdaCDM arm.  ** That is the right outcome and it is stated as
          a gain: the 1123 was never an argument about a coefficient, and now that the coefficient
          is settled it is a measurement of what the instrument is missing. **
  PART 6  ** AND NOTHING DOWNSTREAM MOVES. **  The one figure the corpus quotes from this integral
          -- `sec:envelope-consequence`'s "10.8% longer diffusion length on the geometric stacking rate"
          -- goes from +10.83% to +10.87%.  The coefficient very nearly cancels in a ratio of two
          rates, which is why C8 could name the ambiguity and still be quoted.

** WHAT THE 1123 IS, NAMED. **  Polarisation enters the transfer TWICE: it raises the damping
coefficient, and it adds source terms -- g*Pi/4 and (3/4k^2) d^2(g*Pi)/d(eta)^2 with
Pi = Theta_2 + Theta^P_0 + Theta^P_2.  ** This instrument now has the first and not the second, and
the half it has is the half that removes power. **  *That is a specification for the next build, not
a caveat: the source terms need the hierarchy carried in the spectrum instrument, which is what
front #2's remaining work is.*

SETTINGS: reduced -- NK=4 vs production 900.  CANNOT CHECK AT PRODUCTION, and it does not apply:
this file derives a COEFFICIENT from the tight-coupling limit of the photon hierarchy, which is
an algebraic limit taken per mode.  ** NK sets how many modes are carried and the derivation is
the same at each; four is enough to exhibit it and nine hundred would exhibit it nine hundred
times. **

rc=0 on success.  Run: python3 P15_the_shear_coefficient_derived_not_remembered.py  (numpy scipy)
"""
import os
import sys

import numpy as np

print(__doc__.split("rc=0")[0])
fail = []

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
BTW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
# ** the instrument reads its configuration from the environment at import, so it is pinned HERE
# and not left to whatever a shell happened to export. **
os.environ.update(LG='24', ETA_I='50', ETA_F='210', KTMAX2='0.01', RTOL='1e-9',
                  KLIST='0.20,0.30,0.40', NK='4', NOPROJ='1')
sys.path.insert(0, BTW)
import L171w_hierarchy_damping_coefficient as L                            # noqa: E402

# =====================================================================
print("=" * 78)
print("PARTS 1-4 — C MEASURED LOCALLY, AND EXTRAPOLATED IN (k/tau')^2")
print("=" * 78)
RES = {}
for pol, want, nm in ((0, 8 / 9, 'unpolarised'), (1, 16 / 15, 'polarised')):
    X, Y = [], []
    for k in [float(v) for v in os.environ['KLIST'].split(',')]:
        for em, kt, C in L.local_C(k, pol):
            if kt ** 2 <= L.KTMAX2:
                X.append(kt ** 2)
                Y.append(C)
    X, Y = np.array(X), np.array(Y)
    a, C0 = np.polyfit(X, Y, 1)
    sd = float(np.std(Y - (a * X + C0)))
    RES[pol] = (float(C0), float(a), sd, len(X))
    print(f"  {nm:>12}:  {len(X)} local readings with (k/tau')^2 <= {L.KTMAX2}")
    print(f"                C(k/tau' -> 0) = {C0:.4f}   against {want:.4f}   "
          f"({(C0-want)/want:+.2%})")
    print(f"                slope {a:+.3f} in (k/tau')^2, scatter about the line {sd:.4f}")
    if abs(C0 - want) / want > 0.02:
        fail.append(f"the {nm} coefficient came out {C0:.4f} against {want:.4f}")
    if sd > 0.01:
        fail.append(f"the {nm} readings scatter {sd:.4f} about a line in (k/tau')^2 -- "
                    "the k^2 scaling is not clean and the intercept is not a coefficient")
    if a >= 0:
        fail.append(f"the {nm} finite-(k/tau') correction has the wrong sign")
RATIO = RES[1][0] / RES[0][0]
print(f"\n  ** THE POLARISATION CORRECTION IS A FACTOR {RATIO:.4f} AGAINST 6/5 = 1.2000 "
      f"({(RATIO-1.2)/1.2:+.3%}). **")
print("     *Both absolute values sit about half a per cent low and by an amount proportional to C,")
print("     so the residual is a common normalisation and cancels here.  ** The ratio is what was")
print("     in dispute and it is the number this file was built to produce. **")
if abs(RATIO - 1.2) / 1.2 > 0.005:
    fail.append(f"the polarisation correction came out {RATIO:.4f} against 6/5")
if not (RES[1][0] > RES[0][0]):
    fail.append("polarisation did not INCREASE the damping coefficient -- the sign is wrong")

# =====================================================================
print()
print("=" * 78)
print("PART 5 — SO THE COEFFICIENT IS 16/15, AND ADOPTING IT COSTS THE CONTROL")
print("=" * 78)
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                             # noqa: E402
SPEC = os.path.join(BTW, 'spectra')
SHOW = [('lcdm_0.859', '8/9  (the standing value until c54.177)'),
        ('lcdm_1.000', '16/15 (derived here, and adopted)')]
chis = {}
for f, nm in SHOW:
    z = np.load(os.path.join(SPEC, f"{f}.npz"))
    c, n, A, lo, hi = CS.chi2_of(z['ls'], z['Dl'])
    chis[f] = c
    print(f"  {nm:>42}:  chi^2 = {c:>8.1f} / {n} bins  =  {c/n:.2f}")
dchi = chis['lcdm_1.000'] - chis['lcdm_0.859']
print(f"\n  ** ADOPTING THE DERIVED COEFFICIENT COSTS {dchi:+.0f} UNITS OF chi^2. IT IS ADOPTED. **")
print("     *A coefficient chosen because it fits is a fitted parameter whatever it is called.*")
print("     ⇒ ***AND THE 1123 IS NOW A MEASUREMENT RATHER THAN A TEMPTATION: polarisation enters")
print("     the transfer twice, raising the damping AND adding the source terms g*Pi/4 and")
print("     (3/4k^2)(g*Pi)'' — and this instrument has the half that removes power and not the half")
print("     that returns it.  That is the specification for the next build.***")
if dchi <= 0:
    fail.append("the derived coefficient does not cost chi^2 -- PART 5's whole point is that it does")

# =====================================================================
print()
print("=" * 78)
print("PART 6 — AND THE ONE FIGURE THE CORPUS QUOTES FROM THIS INTEGRAL DOES NOT MOVE")
print("=" * 78)
from scipy.integrate import quad                                          # noqa: E402
Omv, OLv, z_rec = 0.307, 0.693, 1100.0
a_rec = 1 / (1 + z_rec)
ORv = Omv * (2.0 * (1 + z_rec) / (1 + 6797.0)) * a_rec
Rb_rec = 0.6


def _pct(C):
    def g(a):
        Rb = Rb_rec * (a / a_rec)
        return (Rb ** 2 / (1 + Rb) + C) / (6 * (1 + Rb))

    def I(wr):
        return quad(lambda a: g(a) / np.sqrt(ORv / a ** 4 * wr + Omv / a ** 3 + OLv),
                    1e-6, a_rec, limit=200)[0]
    return 100 * (np.sqrt(I(0.0) / I(1.0)) - 1)


p8, p16 = _pct(8 / 9), _pct(16 / 15)
print(f"  r_D(CR)/r_D(LambdaCDM) with C = 8/9  : {p8:+.2f}%")
print(f"  r_D(CR)/r_D(LambdaCDM) with C = 16/15: {p16:+.2f}%")
print(f"\n  ** THE PAPER'S 10.8% SURVIVES: {p8:+.2f}% -> {p16:+.2f}%, a shift of "
      f"{p16-p8:+.3f} POINTS. **")
print("     *The coefficient very nearly cancels in a ratio of two rates, which is exactly why C8")
print("     could name the ambiguity in its own text and still be quoted for a figure.*")
if abs(p16 - p8) > 0.1:
    fail.append(f"the C8 figure moves {p16-p8:+.2f} points -- sec:envelope-consequence must be "
                "recomputed before this coefficient is adopted")
if not (10.7 < p16 < 10.95):
    fail.append(f"the C8 figure is {p16:.2f}% with the derived coefficient, not the quoted 10.8%")

# =====================================================================
print()
print("=" * 78)
if fail:
    print("FAILED: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS — the unpolarised hierarchy returns 8/9 and the polarised 16/15, their ratio")
print("is 6/5 to three parts in ten thousand, the coefficient is DERIVED and adopted at a cost of")
print("1123 units of chi^2, and the corpus's 10.8% does not move.")
print("=" * 78)

# ============================================================================================
# GATE — r2376+c54.177.  CR_cosmology.tex sec:refit-bound now carries the derived coefficient and
# the fact that adopting it costs the control, and both are pinned here.
#   (1) the two intercepts, to a per cent of themselves -- these ARE the derivation;
#   (2) the polarisation correction, to a tenth of a per cent of 6/5 -- the number in dispute;
#   (3) the sign and size of the finite-(k/tau')^2 correction, so that a change of method which
#       destroyed the extrapolation would fail here rather than shift the intercept quietly;
#   (4) the chi^2 cost of adopting it, which the paper quotes as 1123;
#   (5) the C8 figure, so that adopting the coefficient cannot silently move a published number.
# ============================================================================================
assert abs(RES[0][0] - 0.8852) < 0.009, f"unpolarised intercept {RES[0][0]:.4f}, expected 0.8852"
assert abs(RES[1][0] - 1.0618) < 0.011, f"polarised intercept {RES[1][0]:.4f}, expected 1.0618"
assert abs(RATIO - 1.1996) < 0.0012, f"polarisation correction {RATIO:.4f}, expected 1.1996"
# ** THE EXTRAPOLATION MUST BE SHORT, WHICH IS A STRONGER CHECK THAN THE SLOPE'S SIZE. **  The
# first draft of this gate demanded slopes of order unity and FAILED on its own data: the
# unpolarised slope is -0.150 against the polarised -0.942.  What actually matters is that the
# correction swept out over the fitted range is small against the coefficient, so the intercept is
# a short extrapolation and not a long one.
assert RES[0][1] < 0 and RES[1][1] < 0, \
    f"the finite-(k/tau')^2 slopes are {RES[0][1]:.3f} and {RES[1][1]:.3f} -- both must be " \
    "negative, since the correction reduces the apparent coefficient"
for _p in (0, 1):
    _sw = abs(RES[_p][1]) * L.KTMAX2 / RES[_p][0]
    assert _sw < 0.02, f"the extrapolation sweeps {_sw:.1%} of the coefficient -- too long to " \
        "call the intercept a measurement"
assert abs(dchi - 1122.9) < 5.0, f"adopting 16/15 costs {dchi:.1f}, expected 1123"
assert abs(p16 - 10.87) < 0.02, f"the C8 figure is {p16:.2f}%, expected 10.87%"
print(f"GATE c54.177 (r2376): C_unpol = {RES[0][0]:.4f} (8/9 = {8/9:.4f}), C_pol = "
      f"{RES[1][0]:.4f} (16/15 = {16/15:.4f}), ratio = {RATIO:.4f} against 6/5; adopting it costs "
      f"{dchi:+.0f} in chi^2 and moves the C8 figure {p16-p8:+.3f} points -- pinned against "
      f"CR_cosmology.tex sec:refit-bound.")
