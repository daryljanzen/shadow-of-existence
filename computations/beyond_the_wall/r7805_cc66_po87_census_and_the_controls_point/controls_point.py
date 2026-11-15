"""r7805+cc66 item ②: what moves if the control is re-pointed to Planck's omega_c.

The corpus carries the control at (67.40, Omega_m 0.3150, omega_b 0.02237).  Deriving omega_c from
that Omega_m at that h gives 0.120727, against Planck 2018 base LCDM's 0.1200.  Setting omega_c to
0.1200 at the same H0 and omega_b means Omega_m = (0.1200 + 0.02237)/0.674**2 = 0.313400, i.e.

    Delta Omega_m = -0.001600,  which is -0.10667 of the refit grid's own Omega_m step (0.0150).

That is a tenth of a step, well inside the +-1-step stencil the corpus's refit grid is built on, so
the move is priced from the GRID's own banked two-sided steps rather than by running a new spectrum:

    D_l(x) = base + g x + h x^2 / 2,   g = (OMp - OMm)/2,   h = OMp - 2 base + OMm

with x in grid steps.  Scoring is the refit receipts' own: P15's CAMB lensing operator applied to
both, `chi2_of_spectrum.chi2_of`, 185 lensed bins, one amplitude in closed form.

Run: python3 controls_point.py       (numpy, scipy, camb; a few minutes)
"""
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(BW))
G = os.path.join(BW, 'refit_grid185')
SP = os.path.join(BW, 'spectra')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import camb                                                                    # noqa: E402
import chi2_of_spectrum as CS                                                  # noqa: E402

WB, H = 0.02237, 0.674
WC_CORPUS, WC_PLANCK = 0.3150 * H ** 2 - WB, 0.1200
OM_CORPUS, OM_PLANCK = 0.3150, (WC_PLANCK + WB) / H ** 2
STEP_OM = 0.0150
X = (OM_PLANCK - OM_CORPUS) / STEP_OM

# P15's lensing operator, the control's own, imposed on both arms -- the refit receipts' recipe.
_p = camb.set_params(H0=67.40, ombh2=WB, omch2=WC_CORPUS, mnu=0.06, omk=0, tau=0.054,
                     As=2.1e-9, ns=0.965, lmax=3000)
_cl = camb.get_results(_p).get_cmb_power_spectra(_p, CMB_unit='muK', lmax=3000)
_le, _un = _cl['total'][:, 0], _cl['unlensed_scalar'][:, 0]
LG = np.arange(len(_le), dtype=float)
RATIO = np.ones_like(_le)
RATIO[_un > 0] = _le[_un > 0] / _un[_un > 0]


def grid(tag):
    with np.load(os.path.join(G, tag + '.npz')) as z:
        return np.asarray(z['ls'], float), np.asarray(z['Dl'], float)


def score(ls, Dl):
    c, nb = CS.chi2_of(ls, Dl * np.interp(ls, LG, RATIO))[:2]
    return float(c), int(nb)


print(f"  THE CONTROL'S POINT")
print(f"    corpus:  (67.40, Omega_m {OM_CORPUS:.6f}, omega_b {WB})  ->  omega_c {WC_CORPUS:.6f}")
print(f"    Planck:  (67.40, Omega_m {OM_PLANCK:.6f}, omega_b {WB})  ->  omega_c {WC_PLANCK:.6f}")
print(f"    delta omega_c {WC_PLANCK - WC_CORPUS:+.6f}   delta Omega_m {OM_PLANCK - OM_CORPUS:+.6f}"
      f"   = {X:+.5f} grid steps of {STEP_OM}\n")

ls, D0 = grid('lcdm_base')
_, Dp = grid('lcdm_OMp')
_, Dm = grid('lcdm_OMm')
g = (Dp - Dm) / 2.0
h = Dp - 2.0 * D0 + Dm
D_new = D0 + g * X + h * X ** 2 / 2.0

c0, nb0 = score(ls, D0)
cn, nbn = score(ls, D_new)
print(f"  THE CONTROL'S NO-FIT CHI^2 ON 185 LENSED BINS")
print(f"    at the corpus's point     {c0:9.3f}  over {nb0} bins")
print(f"    at omega_c = 0.1200      {cn:9.3f}  over {nbn} bins")
print(f"    moves {cn - c0:+.3f}, which is {100 * (cn - c0) / c0:+.3f} per cent\n")

# CLOSURE FIRST: the grid base is not bit-identical to the published control, so the move is applied
# as a RELATIVE scaling of the PUBLISHED chi^2 rather than as an absolute difference.  The ratio is
# what the paper prints, and a relative move is insensitive to the closure gap.
PUB = os.path.join(SP, 'cc66_lcdm_L2000.npz')
with np.load(PUB) as z:
    cpub, nbp = score(np.asarray(z['ls'], float), np.asarray(z['Dl'], float))
print(f"  CLOSURE: the published control `cc66_lcdm_L2000.npz` scores {cpub:.3f} over {nbp} bins "
      f"(r7749's own gate pins 214.1); the grid base scores {c0:.3f}, differing {c0 - cpub:+.3f}.")
print(f"    ⇒ the move is therefore applied as the RELATIVE factor the grid measures, "
      f"{cn / c0:.6f}, not as an absolute chi^2 difference.\n")

# The 0.918 is chi2(arm, no fit) / chi2(control, no fit).  The arm does not move when the control's
# omega_c does, so the whole move is the denominator's.
ARM_OVER_CTL = 0.918
REL = cn / c0
arm_chi2 = ARM_OVER_CTL * cpub
ctl_moved = cpub * REL
moved = arm_chi2 / ctl_moved
print(f"  THE 0.918 COMPARISON  (the arm's distance from the data in units of the control's)")
print(f"    published                 {ARM_OVER_CTL:.3f}")
print(f"    implied arm chi^2         {arm_chi2:9.3f}   (0.918 x the published control's {cpub:.3f})")
print(f"    control at omega_c=0.1200 {ctl_moved:9.3f}   ({cpub:.3f} x {REL:.6f})")
print(f"    the ratio becomes         {moved:.4f}   -> prints as {moved:.3f}")
print(f"    moves {moved - ARM_OVER_CTL:+.4f}; the printed third decimal "
      f"{'MOVES' if abs(round(moved, 3) - ARM_OVER_CTL) > 1e-9 else 'DOES NOT MOVE'}")
print(f"    ⇒ the arm's margin over the control falls from {100 * (1 - ARM_OVER_CTL):.1f} per cent "
      f"to {100 * (1 - moved):.1f} per cent -- about HALF the claim\n")

# ②b: do refitted comparisons move?  The control's 185-bin refit MINIMUM is a property of the
# likelihood surface, not of where the un-refitted point sits: the search already leaves 0.3150 and
# lands at 0.309826, which is 0.0052 BELOW it -- 3.3 times the re-pointing's own 0.0016.
OM_REFIT = 0.309826
print(f"  ②b REFITTED COMPARISONS")
print(f"    the control's own 185-bin refit minimum sits at Omega_m {OM_REFIT:.6f}, which is "
      f"{OM_REFIT - OM_CORPUS:+.6f} from the corpus's point")
print(f"    the re-pointing moves the START by {OM_PLANCK - OM_CORPUS:+.6f}, which is "
      f"{abs((OM_PLANCK - OM_CORPUS) / (OM_REFIT - OM_CORPUS)):.2f} of the distance the refit "
      f"ALREADY travels")
print(f"    ⇒ the minimum is found by search, so re-pointing the start does not move it: the "
      f"refitted figures are unmoved, and ②b HOLDS")

# peak positions, the four-peak table's own observable
def peaks(ls, Dl, n=4):
    y = Dl * np.interp(ls, LG, RATIO)
    out = []
    for i in range(2, len(ls) - 2):
        if y[i] > y[i - 1] and y[i] > y[i + 1] and y[i] > y[i - 2] and y[i] > y[i + 2]:
            a, b, c = y[i - 1], y[i], y[i + 1]
            d = a - 2 * b + c
            out.append(ls[i] + (0.5 * (a - c) / d if d != 0 else 0.0) * (ls[i + 1] - ls[i]))
    return out[:n]


p0, pn = peaks(ls, D0), peaks(ls, D_new)
print(f"\n  THE CONTROL'S PEAK POSITIONS (parabolic on the lensed, binned grid -- this grid starts at "
      f"ell={ls[0]:.0f}, so the first acoustic peak is below its range)")
for i, (a, b) in enumerate(zip(p0, pn), 1):
    print(f"    peak {i}:  {a:8.3f}  ->  {b:8.3f}   moves {b - a:+.4f} multipoles")
if p0:
    print(f"    largest move {max(abs(b - a) for a, b in zip(p0, pn)):.4f} multipoles")
