"""
P15_three_quarters_of_the_arms_residual_is_the_controls_and_what_is_left_is_position_not_amplitude
=================================================================================================

LEVEL: the verified 185-bin refit minima, re-scored through the full `plik_lite` bandpower
covariance, with the figure's own banked numbers recomputed independently and gated against them.

OBJECT UNDER TEST -- `PO-47`'s successor, routed at `r6879` alongside the figure:

    "Binned means of (model - data)/sigma on diagonal errors give, for this arm: -0.22, -0.07,
     +0.42, +1.46, -1.86, -0.06 ...  That is not a monotone offset -- it is a SWING, high through
     700-900 and low through 900-1100 -- and the control shows the same pattern at about two-thirds
     the amplitude.  So: IS THE RESIDUAL A PEAK-POSITION OR DAMPING-SHAPE MISMATCH RATHER THAN AN
     AMPLITUDE ONE, and how much of it is shared with the control?  Report the band means on the
     full covariance, the whitened version, and the shared fraction.  IF IT IS SHARED, IT IS THE
     TRANSFER'S AND NOT THE CONSTRUCTION'S."

-------------------------------------------------------------------------------
WHAT THIS PROBE FINDS.

** THE SWING IS REAL AND IT IS MOSTLY THE CONTROL'S. **  Whitened against the full covariance, the
cosine between this arm's residual vector and the control's is +0.855, and ** 73.1 per cent of the
arm's chi^2 lies along the control's own residual direction **.  Projecting that direction out
leaves 76.2 of 282.96.  On the order's own criterion that part is the TRANSFER'S and not the
construction's -- the same distinction that has decided four questions in this sector.

** AND THE BAND MEANS ARE A THIRD OF THE QUICK RENDER'S, WITH HALF OF THE DIFFERENCE DEMONSTRABLE. **
Through the proper pipeline the arm's six band means are -0.61, -0.07, +0.33, +0.54, -1.06, -0.36
against the render's -0.22, -0.07, +0.42, +1.46, -1.86, -0.06.  ** The shape reproduces -- high
through band 4, low through band 5 -- and the amplitude does not. **  Fitting the single amplitude
on DIAGONAL errors instead of the covariance, which is what a quick render does, moves the arm's
amplitude 0.83% high and takes band 4 from +0.54 to +1.08: ** the metric used for the amplitude
accounts for about half the inflation **, and the rest is in the render rather than here.

** AND WHAT IS LEFT IS POSITION, NOT AMPLITUDE AND NOT TILT -- BUT IT IS SMALL. **  Against the same
bins, fitting one further parameter on top of the amplitude:

      peak-position rescale    best eps = -7.5e-4   dchi^2 = +4.68    <- the largest
      damping-shape change     best fac = +1.7e-2   dchi^2 = +1.36
      tilt  dn_s               best     = -1.3e-3   dchi^2 = +0.09    <- nothing

and on the CONTROL the position direction buys +0.00 while the damping buys +0.30.  ** So the
position/spacing direction is the only one of the three that is the construction's, and the tilt is
exhausted -- the refit already spent it, a 1% tilt costing +8.6 in chi^2. **  But eps = -7.5e-4 is
0.075 per cent in ell, about 0.8 multipoles at the fourth peak, consistent with the +2.0 measured
there at `r6875+cc66.32`; and dchi^2 = 4.7 of 283 is ** under two per cent of the misfit **.

** SO THE HONEST DECOMPOSITION IS: three quarters shared with the control and therefore the
transfer's; of the remaining quarter, a position/spacing mismatch that is the construction's but
accounts for under two per cent; and the bulk of the misfit absorbed by NONE of amplitude, tilt,
damping or position. **  The shape is rejected and this receipt does not say by what.

-------------------------------------------------------------------------------
WHAT IS CLAIMED.

 (1) The banked verified refit spectra, carried through P15's derived lensing operator and binned,
     reproduce the refit's own chi^2 exactly: 186.51 (1.008/bin) and 292.42 (1.581/bin) over the
     full 185 bins -- so the pipeline here is the refit's and not a new one.
 (2) On the figure's 179-bin set (ell <= 1900, the cut the shifted-model tests need), 177.88
     (0.994/bin) and 282.96 (1.581/bin).
 (3) Band means in sixths, on diagonal errors and whitened, for both arms, with the rms growing
     with ell as the order reports.
 (4) The whitened cosine is +0.855 and the shared fraction 73.1%, leaving 76.2 of 282.96.
 (5) A diagonal amplitude fit inflates the arm's amplitude by 0.83% and roughly doubles band 4.
 (6) The three single-parameter directions, their best values and their dchi^2, on both arms.
 (7) Every number the figure plots is recomputed here from the banked spectra and gated against
     `cc66_fig_acoustic_numbers.npz`, so the figure and this receipt cannot drift apart.

WHAT IS NOT CLAIMED.

 * NOT a mechanism for the bulk of the misfit.  Four directions are excluded as the whole of it and
   none is offered in their place.
 * NOT that the shared part is a defect of the transfer as implemented rather than of the modelling
   both arms share; "the transfer's" is the order's own phrase for "not construction-specific".
 * NOT a re-derivation of the refit minima, which are `r6825+cc66.25`'s and are used as banked.
 * NOT anything about the low-multipole floor's score, which is `r6831`'s and is untouched.
 * The whitening mixes bins, so a whitened band mean is a mean over a rotated basis and is reported
   beside the diagonal one rather than instead of it.

WHAT WOULD FALSIFY IT.  The banked spectra not reproducing the refit's chi^2; the band means not
reproducing the swing's shape; the shared fraction depending on the bin cut; the position direction
buying more on the control than on the arm; or the figure's banked numbers disagreeing with the
recomputation.
"""
import os
import sys

import numpy as np

FAILS = []


def check(name, cond, got=None):
    if cond:
        print(f"  [PASS] {name}" + (f"   ({got})" if got is not None else ""))
    else:
        FAILS.append(name)
        print(f"  [FAIL] {name}" + (f"   (got {got})" if got is not None else ""))


print(__doc__)
print("=" * 100)

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402

SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
LC, FACB = CS.bin_center_and_fac()
X_DATA, COV = CS.X_DATA, CS.COV_TT

import camb                                                                # noqa: E402
_p = camb.set_params(H0=67.40, ombh2=0.02237, omch2=0.3150 * 0.674 ** 2 - 0.02237,
                     mnu=0.06, omk=0, tau=0.054, As=2.1e-9, ns=0.965, lmax=3000)
_cl = camb.get_results(_p).get_cmb_power_spectra(_p, CMB_unit='muK', lmax=3000)
_le, _un = _cl['total'][:, 0], _cl['unlensed_scalar'][:, 0]
LG = np.arange(len(_le), dtype=float)
RATIO = np.ones_like(_le)
_m = _un > 0
RATIO[_m] = _le[_m] / _un[_m]

arm = lambda t: (lambda d: (d['ls'], d['Dl']))(np.load(os.path.join(SP, f'cc66_r185_verify_{t}.npz')))


def mb_of(ls, Dl, eps=0.0, dns=0.0, fac=0.0, lD=2094.2, l0=700.0):
    """the model shifted on a FIXED abscissa, so the bin coverage never changes with eps"""
    Ds = np.interp(ls / (1.0 + eps), ls, Dl)
    Ds = Ds * (ls / l0) ** dns * np.exp(fac * (ls / lD) ** 2)
    return CS.bin_spectrum(ls, Ds * np.interp(ls, LG, RATIO))


# ---------------------------------------------------------------------------------
print("\nPART 1 -- THE PIPELINE IS THE REFIT'S, AND THAT IS CHECKED BEFORE ANYTHING IS READ OFF IT.")
print("-" * 100)
K185 = np.isfinite(mb_of(*arm('lcdm'))) & (LC >= 100) & (LC <= 1996)
C185 = COV[np.ix_(K185, K185)]
F185 = np.linalg.inv(C185)
D185 = X_DATA[K185]
full = {}
for t, want in (('lcdm', 186.51), ('cr', 292.42)):
    mb = mb_of(*arm(t))[K185]
    A = float(mb @ F185 @ D185 / (mb @ F185 @ mb))
    r = A * mb - D185
    c2 = float(r @ F185 @ r)
    full[t] = c2
    print(f"    {t:5s}  chi2 = {c2:8.2f} over {int(K185.sum())} bins = {c2/int(K185.sum()):.3f}/bin "
          f"  (refit reported {want})")
check("the banked spectra reproduce the refit's own chi^2 to 0.05 -- so this is the refit's "
      "pipeline and not a new one",
      abs(full['lcdm'] - 186.51) < 0.05 and abs(full['cr'] - 292.42) < 0.05 and int(K185.sum()) == 185)

# ---------------------------------------------------------------------------------
print("\nPART 2 -- THE BAND MEANS, THREE WAYS.")
print("-" * 100)
KEEP = np.isfinite(mb_of(*arm('lcdm'))) & (LC >= 100) & (LC <= 1900)
COVK = COV[np.ix_(KEEP, KEEP)]
LINV = np.linalg.inv(np.linalg.cholesky(COVK))
FISH = np.linalg.inv(COVK)
DK, LCK = X_DATA[KEEP], LC[KEEP]
SIG = np.sqrt(np.diag(COVK))
EDGES = np.linspace(100, 1300, 7)
band = lambda v: [float(np.mean(v[(LCK >= a) & (LCK < b)])) for a, b in zip(EDGES[:-1], EDGES[1:])]
bandrms = lambda v: [float(np.std(v[(LCK >= a) & (LCK < b)])) for a, b in zip(EDGES[:-1], EDGES[1:])]

fmt = lambda xs: " ".join(f"{x:+6.2f}" for x in xs)
store = {}
for t in ('lcdm', 'cr'):
    mb = mb_of(*arm(t))[KEEP]
    A = float(mb @ FISH @ DK / (mb @ FISH @ mb))
    Ad = float(np.sum(mb * DK / SIG ** 2) / np.sum(mb ** 2 / SIG ** 2))
    r, rd = A * mb - DK, Ad * mb - DK
    w = LINV @ r
    c2 = float(r @ FISH @ r)
    store[t] = dict(A=A, Ad=Ad, mb=mb, r=r, w=w, c2=c2)
    print(f"\n  {t}:  chi2 = {c2:.2f} over {int(KEEP.sum())} bins ({c2/int(KEEP.sum()):.3f}/bin),"
          f"  A(cov) = {A:.2f},  A(diag) = {Ad:.2f}  ({100*(Ad/A-1):+.3f}%)")
    print(f"    band mean, covariance amplitude, diagonal sigma : {fmt(band(r / SIG))}")
    print(f"    band mean, covariance amplitude, WHITENED       : {fmt(band(w))}")
    print(f"    band mean, DIAGONAL amplitude, diagonal sigma   : {fmt(band(rd / SIG))}")
    print(f"    band rms,  covariance amplitude, diagonal sigma : "
          f"{' '.join(f'{x:6.2f}' for x in bandrms(r / SIG))}")

print("\n  the order's quick render, for comparison:")
print("    CR      -0.22  -0.07  +0.42  +1.46  -1.86  -0.06")
print("    control                        +0.96  -1.18")
cr_b = band(store['cr']['r'] / SIG)
check("the SWING reproduces -- band 4 positive and band 5 negative on the arm, the shape the order "
      "reports -- so the feature is real and not the render's",
      cr_b[3] > 0 and cr_b[4] < 0 and cr_b[4] < cr_b[3],
      f"band4 = {cr_b[3]:+.2f}, band5 = {cr_b[4]:+.2f}")
check("...and the control carries the same sign pattern, at smaller amplitude",
      band(store['lcdm']['r'] / SIG)[3] > 0 and band(store['lcdm']['r'] / SIG)[4] < 0,
      f"control band4 = {band(store['lcdm']['r']/SIG)[3]:+.2f}, "
      f"band5 = {band(store['lcdm']['r']/SIG)[4]:+.2f}")
crd_b = band((store['cr']['Ad'] * store['cr']['mb'] - DK) / SIG)
check("** the AMPLITUDE METRIC accounts for about half the render's inflation **: fitting the "
      "amplitude on diagonal errors puts the arm 0.83% high and roughly doubles band 4, against "
      "the render's +1.46",
      crd_b[3] > 1.7 * cr_b[3] and abs(store['cr']['Ad'] / store['cr']['A'] - 1) > 0.005,
      f"band4 {cr_b[3]:+.2f} (cov) -> {crd_b[3]:+.2f} (diag), render +1.46")
check("the scatter grows with ell, as the order reports",
      bandrms(store['cr']['r'] / SIG)[-1] > bandrms(store['cr']['r'] / SIG)[0],
      f"rms {bandrms(store['cr']['r']/SIG)[0]:.2f} -> {bandrms(store['cr']['r']/SIG)[-1]:.2f}")

# ---------------------------------------------------------------------------------
print("\nPART 3 -- HOW MUCH IS SHARED WITH THE CONTROL.  ** THIS IS THE DECIDING NUMBER. **")
print("-" * 100)
wc, wl = store['cr']['w'], store['lcdm']['w']
cosv = float(wc @ wl / np.linalg.norm(wc) / np.linalg.norm(wl))
frac = float((wc @ wl) ** 2 / ((wl @ wl) * (wc @ wc)))
rem = float(wc @ wc - (wc @ wl) ** 2 / (wl @ wl))
print(f"    |w_CR| = {np.linalg.norm(wc):6.2f}      |w_control| = {np.linalg.norm(wl):6.2f}")
print(f"    cosine between the two whitened residual vectors : {cosv:+.4f}")
print(f"    fraction of the ARM's chi^2 along the CONTROL's direction : {100*frac:.1f}%")
print(f"    what is left once that direction is projected out : {rem:.1f} of {wc @ wc:.1f}")
check("** THREE QUARTERS OF THE ARM'S RESIDUAL LIES ALONG THE CONTROL'S **, so on the order's own "
      "criterion it is the transfer's and not the construction's",
      frac > 0.70 and cosv > 0.84, f"{100*frac:.1f}% at cos {cosv:+.3f}")
for lo, hi in ((100, 1996), (100, 1500), (200, 1900)):
    k = np.isfinite(mb_of(*arm('lcdm'))) & (LC >= lo) & (LC <= hi)
    cv = COV[np.ix_(k, k)]
    li = np.linalg.inv(np.linalg.cholesky(cv))
    fi = np.linalg.inv(cv)
    dd = X_DATA[k]
    ws = []
    for t in ('lcdm', 'cr'):
        m = mb_of(*arm(t))[k]
        a = float(m @ fi @ dd / (m @ fi @ m))
        ws.append(li @ (a * m - dd))
    f2 = float((ws[1] @ ws[0]) ** 2 / ((ws[0] @ ws[0]) * (ws[1] @ ws[1])))
    print(f"    bin cut {lo}-{hi}: shared fraction {100*f2:.1f}%")
k2 = np.isfinite(mb_of(*arm('lcdm'))) & (LC >= 200) & (LC <= 1900)
cv2 = COV[np.ix_(k2, k2)]
li2 = np.linalg.inv(np.linalg.cholesky(cv2))
fi2 = np.linalg.inv(cv2)
dd2 = X_DATA[k2]
w2 = []
for t in ('lcdm', 'cr'):
    m = mb_of(*arm(t))[k2]
    a = float(m @ fi2 @ dd2 / (m @ fi2 @ m))
    w2.append(li2 @ (a * m - dd2))
f_alt = float((w2[1] @ w2[0]) ** 2 / ((w2[0] @ w2[0]) * (w2[1] @ w2[1])))
check("...and the shared fraction does not depend on the bin cut, staying near three quarters "
      "across three of them",
      abs(f_alt - frac) < 0.08, f"{100*f_alt:.1f}% against {100*frac:.1f}%")

# ---------------------------------------------------------------------------------
print("\nPART 4 -- POSITION, TILT OR DAMPING?  ONE FURTHER PARAMETER AT A TIME.")
print("-" * 100)


def chi2_mod(t, **kw):
    mb = mb_of(*arm(t), **kw)[KEEP]
    A = float(mb @ FISH @ DK / (mb @ FISH @ mb))
    r = A * mb - DK
    return float(r @ FISH @ r)


best = {}
for t in ('lcdm', 'cr'):
    base = chi2_mod(t)
    print(f"\n  {t}:  amplitude only  chi2 = {base:7.2f}")
    best[t] = {}
    for lab, key, br in (("peak-position rescale eps", 'eps', (-0.008, 0.008)),
                         ("tilt dn_s", 'dns', (-0.04, 0.04)),
                         ("damping-shape fac", 'fac', (-0.06, 0.06))):
        g = np.linspace(br[0], br[1], 65)
        v = np.array([chi2_mod(t, **{key: x}) for x in g])
        i = int(np.nanargmin(v))
        best[t][key] = (float(g[i]), float(base - v[i]))
        print(f"    + {lab:26s} best {g[i]:+10.5f}   dchi2 = {base - v[i]:+7.2f}")
check("** ON THE ARM THE POSITION DIRECTION IS THE LARGEST OF THE THREE **, three times the damping "
      "and fifty times the tilt",
      best['cr']['eps'][1] > 2 * best['cr']['fac'][1] and best['cr']['eps'][1] > 10 * best['cr']['dns'][1],
      f"eps {best['cr']['eps'][1]:+.2f}, fac {best['cr']['fac'][1]:+.2f}, dns {best['cr']['dns'][1]:+.2f}")
check("** AND ON THE CONTROL IT BUYS NOTHING **, so the position piece is the construction's rather "
      "than shared",
      best['lcdm']['eps'][1] < 0.2 and best['cr']['eps'][1] > 3.0,
      f"control {best['lcdm']['eps'][1]:+.2f} against the arm's {best['cr']['eps'][1]:+.2f}")
check("the TILT is exhausted -- the refit already spent it, and a one-per-cent tilt costs chi^2 "
      "rather than buying it",
      best['cr']['dns'][1] < 0.5 and chi2_mod('cr', dns=0.01) - chi2_mod('cr') > 5,
      f"best dchi2 {best['cr']['dns'][1]:+.2f}; dn_s = +0.01 costs "
      f"{chi2_mod('cr', dns=0.01) - chi2_mod('cr'):+.1f}")
check("** but the position piece is SMALL **: eps = -7.5e-4 is 0.075 per cent in ell, and dchi^2 = "
      "4.7 of 283 is under two per cent of the misfit -- so it is not the explanation either",
      best['cr']['eps'][1] / store['cr']['c2'] < 0.02,
      f"{100*best['cr']['eps'][1]/store['cr']['c2']:.1f}% of the misfit; "
      f"eps = {best['cr']['eps'][0]:.2e} is {abs(best['cr']['eps'][0])*1130:.1f} in ell at the fourth peak")

# ---------------------------------------------------------------------------------
print("\nPART 5 -- THE FIGURE'S OWN NUMBERS, RECOMPUTED AND GATED SO THE TWO CANNOT DRIFT.")
print("-" * 100)
fn = os.path.join(SP, 'cc66_fig_acoustic_numbers.npz')
check("the figure's banked numbers exist -- corpus/make_fig_acoustic_two_arm.py has been run",
      os.path.exists(fn), fn if os.path.exists(fn) else "MISSING")
if os.path.exists(fn):
    F = np.load(fn)
    for k, v in (('lcdm_chi2', store['lcdm']['c2']), ('cr_chi2', store['cr']['c2']),
                 ('lcdm_A', store['lcdm']['A']), ('cr_A', store['cr']['A']),
                 ('shared_frac', frac), ('shared_cos', cosv),
                 ('cr_chi2_minus_control_dir', rem)):
        got = float(F[k])
        ok = abs(got - v) < max(1e-6, 1e-6 * abs(v))
        print(f"    {k:28s} figure {got:12.5f}   receipt {v:12.5f}   {'OK' if ok else 'MISMATCH'}")
        if not ok:
            FAILS.append(f"figure/receipt mismatch on {k}")
    check("every headline number the figure plots is reproduced here independently from the banked "
          "spectra, so the figure and this receipt cannot drift apart",
          not any(f.startswith('figure/receipt') for f in FAILS))

# ---------------------------------------------------------------------------------
print("\n" + "=" * 100)
print("THE READING.")
print("=" * 100)
print(f"""
  ** THE DECOMPOSITION, AND IT IS THREE THINGS RATHER THAN ONE. **

  1. ** {100*frac:.0f} PER CENT OF THE ARM'S RESIDUAL IS THE CONTROL'S. **  Whitened against the full
     covariance the two residual vectors sit at cosine {cosv:+.3f}, and projecting the control's
     direction out of the arm's leaves {rem:.1f} of {store['cr']['c2']:.1f}.  On the order's own
     criterion that part is the transfer's and not the construction's.

  2. ** OF WHAT IS LEFT, THE POSITION DIRECTION IS THE CONSTRUCTION'S AND THE TILT IS EXHAUSTED. **
     A peak-position rescale buys {best['cr']['eps'][1]:+.2f} on the arm and {best['lcdm']['eps'][1]:+.2f} on the
     control; a tilt buys {best['cr']['dns'][1]:+.2f} and costs {chi2_mod('cr', dns=0.01) - chi2_mod('cr'):+.1f} at one per cent, the
     refit having already spent it; the damping buys {best['cr']['fac'][1]:+.2f}.  ** So the answer to the
     order's question is: position rather than amplitude, and not tilt. **

  3. ** BUT IT IS SMALL, AND THAT IS THE PART NOT TO OVERSELL. **  eps = {best['cr']['eps'][0]:.1e} is
     {abs(best['cr']['eps'][0])*1130:.1f} multipoles at the fourth peak -- consistent with the +2.0 measured there at
     r6875+cc66.32 -- and {best['cr']['eps'][1]:.1f} of {store['cr']['c2']:.0f} is under two per cent of the misfit.
     ** Amplitude, tilt, damping and position together do not account for the shape rejection, and
     this receipt does not say what does. **

  ** AND THE QUICK RENDER'S BAND MEANS WERE ABOUT THREE TIMES THESE. **  The swing's SHAPE reproduces
  -- band 4 high, band 5 low, on both arms -- and its amplitude does not.  Fitting the amplitude on
  diagonal errors rather than the covariance puts the arm 0.83% high and roughly doubles band 4,
  which is about half the difference; the rest is in the render and is not reconstructed here.
""")

print("=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED -> " + "; ".join(FAILS))
    raise SystemExit(1)
print("GATES: ALL PASS.")
print(f"""
ESTABLISHED: the banked refit spectra reproduce the refit's own chi^2 (186.51 and 292.42 over 185
bins); the residual swing the order reports is real and reproduces in shape on both arms while its
amplitude is about a third of the quick render's, the amplitude metric accounting for about half of
that; {100*frac:.0f} per cent of the arm's chi^2 lies along the control's residual direction (cosine {cosv:+.3f}),
so most of it is the transfer's and not the construction's; and of the rest a peak-position rescale
is the largest of the three single-parameter directions ({best['cr']['eps'][1]:+.2f} against {best['cr']['fac'][1]:+.2f} for damping and
{best['cr']['dns'][1]:+.2f} for tilt) and buys nothing at all on the control -- position rather than amplitude, and
under two per cent of the misfit.
NOT CLAIMED: a mechanism for the bulk of the misfit; a re-derivation of the refit minima; anything
about the low-multipole floor's score.
""")
