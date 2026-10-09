r"""
RECEIPT -- P15: ** `r7223` ORDERED IT: `evaluate the kernel's own phase contribution on EACH ARM'S OWN
r_s, D_M and r_D, and state the difference between the two arms against the measured residual's
size`.  *** THE DIFFERENCE IS `$-0.0141^{\circ}$` AGAINST A RESIDUAL OF `$-96.6^{\circ}$` -- NEARLY
FOUR ORDERS BELOW -- SO THE KERNEL IS NOT A CARRIER AND THE PROJECTION IS CLEARED. *** **

  ⓵ ** THE KERNEL'S PHASE IS A FUNCTION OF EXACTLY TWO DIMENSIONLESS NUMBERS, AND THE ARMS SHARE ONE
  OF THEM BY CONSTRUCTION. **  *Writing `$x=kD_M$`, `r7234`'s window is
  `$W\propto x^{n_s-2}e^{-2(xr_D/D_M)^2}/(x\sqrt{x^2-\ell^2})$` and the oscillation it weights is
  `$\cos(2xr_s/D_M)$`, so the phase depends on `$r_D/D_M$` and on `$r_s/D_M$` and on nothing else --
  verified here by SCALING all three lengths together and getting the same phase to `$10^{-10}$`
  degrees.*  ⇒ **`$r_s/D_M$` is `$\theta_*/\pi$`, which the two arms match to `$1.5\times10^{-5}$`
  because the angle is what the construction computes; `$r_D/D_M$` differs by `$0.27$` per cent.**
  ⌗ *Moved one at a time: `$r_D/D_M$` carries `$-0.0139^{\circ}$` of the `$-0.0141^{\circ}$` and
  `$r_s/D_M$` carries `$-0.0001^{\circ}$`.*

  ⓶ ** TWO INDEPENDENT ROUTES, AND THEY AGREE ON THE DIFFERENCE TO FIVE DECIMAL PLACES. **  *The
  closed-form window gives `$-0.01406^{\circ}$` and the FULL Bessel sum `$-0.01407^{\circ}$`; on the
  absolute running phase they agree to `$0.012^{\circ}$` out of `$15.5$`.  Both are shown converged
  -- the window under the quadrature count and the tail reach, the Bessel under its `$k$` sampling.*

  ⓷ ⛔⛭⛭⛭ ** AND THE UNDER-SAMPLED BESSEL SUM MANUFACTURES A DIFFERENCE `$74$` TIMES THE TRUE ONE. **
  *At `$1.8$` points per Bessel period the arm-minus-control phase reads `$-1.05^{\circ}$`; at
  `$4.6$` and above it reads `$-0.01407^{\circ}$` and does not move again through a fifty-fold
  refinement.  **The window route is immune, because it averages the kernel analytically rather than
  sampling it.**  ⌗ This is the instrument's own documented failure mode -- `the projected peaks would
  be aliasing while the source comb stayed correct` -- arriving in the PHASE instead of the peaks, and
  it is the reason the answer is given on two routes rather than one.*

  ⓸ ⛔ ** THE PRE-REGISTERED SIGN IS WRONG, AND THE REASON IS A CONFLATION THIS SEAT HAS NOW MADE
  TWICE. **  *Predicted `$+0.06^{\circ}$`, measured `$-0.0141^{\circ}$`: the magnitude is inside the
  pre-registered band and the SIGN FAILED.  **Measured root cause: the kernel's PHASE has
  `$|{\rm running}|$` FALLING with `$r_D$` -- `$16.77^{\circ}$` at `$5.0$` Mpc to `$8.54^{\circ}$` at
  `$14.0$` -- while the kernel's PEAK-POSITION drift has `$|{\rm running}|$` RISING with `$r_D$`.**
  *I read the sensitivity off `r7234`'s peak-offset table for a question about phase, and the two have
  OPPOSITE `$r_D$` dependence.*  ⌈ ***And the central value was wrong twice over in a way that
  cancelled:*** *the `$-17^{\circ}$` absolute phase in the pre-registration was a peak-offset running
  drift converted at `$180^{\circ}$` per peak step where the paper's comb period is `$360^{\circ}$` --
  the right number by the wrong route and the wrong units at once.  The true phase is
  `$-15.45^{\circ}$`.*

  ⇒ ⛭ ** SO THE ORDER'S NEGATIVE BRANCH, IN ITS OWN WORDS: `the kernel is not a carrier, the candidate
  list stays at the driving, the loading and the clock, and the projection is cleared`. **  *The
  difference is `$1.5\times10^{-4}$` of the residual.  No threshold the row could reasonably set is
  anywhere near it.*

  ⌈ ⛭⛭ ** AND THE PRE-REGISTERED THIRD OUTCOME HOLDS ALONGSIDE IT, WHICH IS A DIFFERENT STATEMENT
  FROM `cleared`. **  *The kernel's ABSOLUTE running phase is `$-15.45^{\circ}$`, which is `$16.0$`
  per cent of the residual's `$-96.6^{\circ}$` -- a sixth -- and it is present in ANY spectrum this
  instrument projects, the control's included, agreeing between the arms to `$0.09$` per cent.*
  ⇒ **So `a running phase at correct spacing` is not a phase-clean observable: a sixth of the scale
  the row reads its candidates against is manufactured by the projection, and it cancels only because
  both arms carry it.**  *That is why `cleared` is the answer to the order and not the whole of what
  the evaluation found.*

** COMPUTES: the projection kernel's own running acoustic phase across 104 <= l <= 1886, evaluated on
   each arm's own r_s, D_M and r_D, by two independent routes -- the closed-form asymptotic window of
   r7234 read as a complex integral, and the full spherical-Bessel sum -- together with the
   arm-minus-control difference, its decomposition into the two dimensionless numbers the phase
   depends on, and the aliasing threshold above which the Bessel route is trustworthy.  *** No
   spectra are computed and no bank is written; the three background numbers per arm are read off the
   banked spectra and their run logs. *** **

STATUS: rc=0 on success.  Run: python3 <this file>   (numpy, scipy; 20s MEASURED)
"""
import os
import sys

import numpy as np
from scipy.special import spherical_jn

print(__doc__.split("STATUS:")[0])
BAR = "=" * 104
fail = []
ran = []


def gate(label, ok):
    ran.append(label)
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}")
    if not ok:
        fail.append(label)


def head(t):
    print(f"\n{BAR}\n  {t}\n{BAR}")


ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
GO = os.path.join(BW, 'r7093_directions', 'grid_oneclock')
MINE = os.path.join(BW, 'r7236_60_is_any_of_the_residual_phase_the_projection_kernels')
for _p in (GO, MINE):
    if not os.path.exists(_p):
        print(f"  ⛔ AN INPUT THIS RECEIPT READS IS NOT ON DISK: {_p}")
        sys.exit(1)

NS = 0.96                     # the corpus default the instrument carries
LLO, LHI = 104.0, 1886.0      # the range the residual is quoted across
RESIDUAL = -96.6              # degrees of a comb period, sec:refit-bound
DEG = 180.0 / np.pi           # radians of cos(2 k r_s) -> degrees of a comb period (2 pi rad = 360)


# ─────────────────────────────────────────────────────────────────────────────────────────────────
#  THE THREE NUMBERS PER ARM, READ OFF THE BANKS AND THEIR LOGS RATHER THAN TYPED
# ─────────────────────────────────────────────────────────────────────────────────────────────────
def arm_inputs(tag):
    z = np.load(os.path.join(GO, f'{tag}.npz'), allow_pickle=True)
    log = open(os.path.join(GO, f'{tag}.log'), encoding='utf-8', errors='replace').read()
    rD = None
    for line in log.split('\n'):
        if 'diffusion: r_D at the visibility peak' in line:
            rD = float(line.split('=')[1].split('Mpc')[0])
            break
    return dict(rs=float(z['r_s']), DM=float(z['D_M']), rD=rD, lA=float(z['l_A']))


ARM = arm_inputs('cr_base')
CTL = arm_inputs('lcdm_base')


# ─────────────────────────────────────────────────────────────────────────────────────────────────
#  ROUTE 1 -- r7234's CLOSED-FORM WINDOW, READ AS A COMPLEX INTEGRAL SO THE PHASE COMES OUT DIRECTLY
# ─────────────────────────────────────────────────────────────────────────────────────────────────
def phase_window(l, rs, DM, rD, nu=20000, reach=80.0, **_):
    """arg INT dt W(x;l) exp(2i (x-l) r_s/D_M),  x = l cosh t.  The substitution absorbs the
    inverse-square-root edge of <j_l^2> = 1/(x sqrt(x^2-l^2)) exactly, so this is plain quadrature."""
    tmax = np.arccosh(max(1.0 + 1e-12, reach * DM / (l * rD)))
    t = np.linspace(0.0, tmax, nu)
    x = l * np.cosh(t)
    k = x / DM
    W = k ** (NS - 2) * np.exp(-2.0 * (k * rD) ** 2) / x
    return float(np.angle(np.trapezoid(W * np.exp(2j * (x - l) * rs / DM), t)))


def running_window(p, **kw):
    """the RUNNING phase in the paper's sign convention: peaks drifting down is negative"""
    return -(phase_window(LHI, **p, **kw) - phase_window(LLO, **p, **kw)) * DEG


# ─────────────────────────────────────────────────────────────────────────────────────────────────
#  ROUTE 2 -- THE FULL SPHERICAL-BESSEL SUM, WITH NO ASYMPTOTIC AVERAGE ANYWHERE IN IT
# ─────────────────────────────────────────────────────────────────────────────────────────────────
def running_bessel(p, nk=250000, kmaxfac=70.0):
    rs, DM, rD = p['rs'], p['DM'], p['rD']
    kmax = kmaxfac / rD
    kk = np.linspace(kmax / nk, kmax, nk)
    dk = kk[1] - kk[0]
    w = (kk ** (NS - 2) * dk) * np.exp(-2.0 * (kk * rD) ** 2) * np.exp(2j * kk * rs)
    x = kk * DM
    out = []
    for l in (LLO, LHI):
        z = np.sum(w * spherical_jn(int(round(l)), x) ** 2) * np.exp(-2j * l * rs / DM)
        out.append(float(np.angle(z)))
    return -(out[1] - out[0]) * DEG, 2.0 * np.pi / DM / dk


# ═════════════════════════════════════════════════════════════════════════════════════════════════
head("Ⓐ  THE IDENTITY -- THE KERNEL'S PHASE DEPENDS ON TWO DIMENSIONLESS NUMBERS AND NOTHING ELSE")
# ═════════════════════════════════════════════════════════════════════════════════════════════════
print(f"    arm     : r_s = {ARM['rs']:9.4f}  D_M = {ARM['DM']:10.3f}  r_D = {ARM['rD']:5.2f}"
      f"   r_s/D_M = {ARM['rs']/ARM['DM']:.8f}   r_D/D_M = {ARM['rD']/ARM['DM']:.6e}")
print(f"    control : r_s = {CTL['rs']:9.4f}  D_M = {CTL['DM']:10.3f}  r_D = {CTL['rD']:5.2f}"
      f"   r_s/D_M = {CTL['rs']/CTL['DM']:.8f}   r_D/D_M = {CTL['rD']/CTL['DM']:.6e}")
gate("Ⓐ① the three numbers were READ from the banks and their run logs, not typed into this file",
     bool(ARM['rD'] and CTL['rD'] and ARM['rs'] != CTL['rs'] and ARM['DM'] != CTL['DM']))
_S = 1.37                        # an arbitrary scale
_scaled = dict(rs=ARM['rs'] * _S, DM=ARM['DM'] * _S, rD=ARM['rD'] * _S)
_r0, _r1 = running_window(ARM), running_window(_scaled)
print(f"    scaling all three lengths by {_S}: running phase {_r0:+.10f} -> {_r1:+.10f} deg")
gate("Ⓐ② SCALE INVARIANCE: the phase is unchanged when all three lengths are scaled together, so it "
     "is a function of the two RATIOS and of nothing dimensional",
     bool(abs(_r1 - _r0) < 1e-8))
_drs = abs(ARM['rs'] / ARM['DM'] - CTL['rs'] / CTL['DM']) / (ARM['rs'] / ARM['DM'])
_drD = abs(ARM['rD'] / ARM['DM'] - CTL['rD'] / CTL['DM']) / (ARM['rD'] / ARM['DM'])
print(f"    the arms differ by {_drs:.2e} in r_s/D_M (= theta_*/pi) and {_drD:.2e} in r_D/D_M")
gate("Ⓐ③ and the arms share r_s/D_M to better than a part in ten thousand while differing in "
     "r_D/D_M at the per-cent level -- which is why the answer is small rather than half a per cent",
     bool(_drs < 1e-4 and 1e-3 < _drD < 1e-2))

# ═════════════════════════════════════════════════════════════════════════════════════════════════
head("Ⓑ  TWO INDEPENDENT ROUTES TO THE SAME PHASE, BOTH SHOWN CONVERGED")
# ═════════════════════════════════════════════════════════════════════════════════════════════════
wA, wC = running_window(ARM), running_window(CTL)
bA, ppA = running_bessel(ARM)
bC, ppC = running_bessel(CTL)
print(f"    closed-form window : arm {wA:+9.4f}   control {wC:+9.4f}   arm-control {wA-wC:+.5f} deg")
print(f"    full Bessel sum    : arm {bA:+9.4f}   control {bC:+9.4f}   arm-control {bA-bC:+.5f} deg"
      f"   ({ppA:.1f} points per Bessel period)")
gate("Ⓑ① the two routes agree on each arm's own running phase to better than 0.05 degrees",
     bool(abs(wA - bA) < 0.05 and abs(wC - bC) < 0.05))
gate("Ⓑ② and on the arm-minus-control DIFFERENCE to better than 0.0005 degrees",
     bool(abs((wA - wC) - (bA - bC)) < 5e-4))
_cv = [running_window(ARM, nu=n, reach=r) - running_window(CTL, nu=n, reach=r)
       for n, r in ((5000, 60.0), (20000, 80.0), (80000, 120.0))]
print(f"    window convergence (nu, reach): {['%+.5f' % v for v in _cv]}")
gate("Ⓑ③ the window route is converged: a sixteen-fold quadrature refinement and a doubled tail "
     "reach move the difference by under 1e-5 degrees",
     bool(max(_cv) - min(_cv) < 1e-5))

# ═════════════════════════════════════════════════════════════════════════════════════════════════
head("Ⓒ  ⛔ THE UNDER-SAMPLED BESSEL SUM MANUFACTURES A DIFFERENCE SEVENTY TIMES THE TRUE ONE")
# ═════════════════════════════════════════════════════════════════════════════════════════════════
_rows = []
for nk in (40000, 100000, 250000):
    dA, pp = running_bessel(ARM, nk=nk)
    dC, _ = running_bessel(CTL, nk=nk)
    _rows.append((nk, pp, dA - dC))
    print(f"    nk = {nk:7d}  ({pp:5.1f} points per Bessel period):  arm-control = {dA-dC:+9.5f} deg")
_bad = [r for r in _rows if r[1] < 4.0]
_good = [r for r in _rows if r[1] >= 4.0]
gate("Ⓒ① below four points per Bessel period the difference is inflated by more than an order",
     bool(_bad and abs(_bad[0][2]) > 10 * abs(_good[0][2])))
gate("Ⓒ② at and above it the number is stable to 1e-5 degrees across a further sixfold refinement",
     bool(len(_good) >= 2 and abs(_good[0][2] - _good[-1][2]) < 1e-5))
gate("Ⓒ③ and the window route gives the same answer at EVERY sampling, because it averages the "
     "kernel analytically instead of sampling it -- which is what makes the pair a check",
     bool(abs((wA - wC) - _good[-1][2]) < 5e-4 and max(_cv) - min(_cv) < 1e-5))

# ═════════════════════════════════════════════════════════════════════════════════════════════════
head("Ⓓ  THE ANSWER THE ORDER ASKED FOR, IN THE ONE FORM IT ASKED FOR IT IN")
# ═════════════════════════════════════════════════════════════════════════════════════════════════
DIFF = wA - wC
print(f"    the kernel's phase difference between the arms, across {LLO:.0f} <= l <= {LHI:.0f}:"
      f" {DIFF:+.4f} deg")
print(f"    the residual it is measured against:                               {RESIDUAL:+.1f} deg")
print(f"    ratio {abs(DIFF/RESIDUAL):.3e}   = {np.log10(abs(RESIDUAL/DIFF)):.2f} orders of magnitude below")
gate("Ⓓ① the difference is more than THREE orders of magnitude below the residual",
     bool(abs(RESIDUAL / DIFF) > 1e3))
gate("Ⓓ② so the kernel is not a carrier: the projection is CLEARED, which is the order's own "
     "negative branch and a result rather than a null",
     bool(abs(DIFF) < 0.01 * abs(RESIDUAL)))
_mv = {}
for nm, kw in (('r_D/D_M alone', dict(rD=CTL['rD'] * ARM['DM'] / CTL['DM'])),
               ('r_s/D_M alone', dict(rs=CTL['rs'] * ARM['DM'] / CTL['DM'])),
               ('both together', dict(rD=CTL['rD'] * ARM['DM'] / CTL['DM'],
                                      rs=CTL['rs'] * ARM['DM'] / CTL['DM']))):
    q = dict(ARM)
    q.pop('lA', None)
    q.update(kw)
    _mv[nm] = wA - running_window(q)
    print(f"    moving {nm}: contributes {_mv[nm]:+.5f} deg of the {DIFF:+.5f}")
gate("Ⓓ③ and r_D/D_M carries essentially the whole of it while r_s/D_M carries under a per cent of "
     "it -- the two-number decomposition the identity predicted",
     bool(abs(_mv['r_D/D_M alone'] - DIFF) < 0.1 * abs(DIFF)
          and abs(_mv['r_s/D_M alone']) < 0.02 * abs(DIFF)))

# ═════════════════════════════════════════════════════════════════════════════════════════════════
head("Ⓔ  THE PRE-REGISTERED PREDICTION, SCORED -- AND THE SIGN IS THE PART THAT FAILED")
# ═════════════════════════════════════════════════════════════════════════════════════════════════
_pt = ' '.join(open(os.path.join(MINE, 'PREDICTION.md'), encoding='utf-8').read().split())
gate("Ⓔ① the prediction is on disk, in ONE form as r7223 required, and names its band and its sign",
     bool('+0.06^{\\circ}$` across' in _pt and '0.01^{\\circ}$` to `$0.3^{\\circ}' in _pt
          and 'POSITIVE in sign' in _pt))
print(f"    predicted: +0.06 deg, band 0.01 to 0.3 in magnitude, POSITIVE.  measured: {DIFF:+.4f} deg")
gate("Ⓔ② the MAGNITUDE is inside the pre-registered band", bool(0.01 <= abs(DIFF) <= 0.3))
gate("Ⓔ③ and `three orders of magnitude below the residual` holds",
     bool(abs(RESIDUAL / DIFF) > 1e3))
gate("Ⓔ④ ⛔ THE SIGN FAILED -- predicted POSITIVE, measured NEGATIVE.  This gate asserts the failure, "
     "not the prediction", bool(DIFF < 0))
_sens = [(rD, running_window(dict(rs=ARM['rs'], DM=ARM['DM'], rD=rD))) for rD in (5.0, 7.12, 14.0)]
print("    the kernel's PHASE against r_D: " + "   ".join(f"{r:5.2f} -> {v:+8.4f}" for r, v in _sens))
print("    r7234's PEAK-OFFSET drift against r_D ran the other way: 10.9 -> 16.9 -> 29.0 in magnitude")
gate("Ⓔ⑤ and the root cause is MEASURED: the kernel's phase magnitude FALLS with r_D while its "
     "peak-position drift RISES, so a sensitivity read off the peak table is backwards for a phase",
     bool(abs(_sens[0][1]) > abs(_sens[1][1]) > abs(_sens[2][1])))
gate("Ⓔ⑥ ⛔ and the pre-registration's absolute figure was wrong twice in a cancelling way -- a "
     "peak-offset drift converted at 180 degrees per step where the comb period is 360 -- which this "
     "gate records by asserting the TRUE phase is near 15 and not near the 34 that table gives",
     bool(14.0 < abs(wA) < 17.0 and '-17^{\\circ}' in _pt))
gate("Ⓔ⑦ the two-number decomposition held, so refuting outcome 4 did not fire",
     bool(abs(_mv['r_s/D_M alone']) < 0.02 * abs(DIFF)))

# ═════════════════════════════════════════════════════════════════════════════════════════════════
head("Ⓕ  THE PRE-REGISTERED THIRD OUTCOME, WHICH HOLDS ALONGSIDE `cleared` AND IS NOT THE SAME THING")
# ═════════════════════════════════════════════════════════════════════════════════════════════════
_frac = abs(wA / RESIDUAL)
print(f"    the kernel's ABSOLUTE running phase, arm: {wA:+.4f} deg = {100*_frac:.1f}% of the residual")
print(f"    and the control's:                        {wC:+.4f} deg -- the two agree to "
      f"{100*abs(wA-wC)/abs(wA):.2f}%")
gate("Ⓕ① the kernel's own running phase is a SIXTH of the residual, not a negligible part of it",
     bool(0.10 < _frac < 0.25))
gate("Ⓕ② and it is COMMON MODE: the arms carry it to better than a tenth of a per cent of itself",
     bool(abs(wA - wC) / abs(wA) < 1e-3))
gate("Ⓕ③ so `a running phase at correct spacing` carries a projection-manufactured floor, which is "
     "a different statement from `the kernel is cleared` and was written down in advance",
     bool('third outcome' in _pt.lower() and 'common-mode floor' in _pt and 0.10 < _frac < 0.25))

# ═════════════════════════════════════════════════════════════════════════════════════════════════
head("Ⓖ  WHAT THIS DOES NOT SETTLE")
# ═════════════════════════════════════════════════════════════════════════════════════════════════
print("    ⌗ the phase evaluated here is the KERNEL's, on a damped comb with the construction's own")
print("      three lengths.  It is not the full transfer's phase: the driving and the loading are")
print("      the row's standing candidates and nothing here touches them.")
print("    ⌗ r_D is read at the visibility peak, which is the figure the runs report; the diffusion")
print("      length is itself l-dependent and a single value is a choice -- but the ANSWER is a")
print("      difference of two arms at the same choice, and the sensitivity is gated in Ⓔ⑤.")
print("    ⌗ the residual's -96.6 degrees is quoted from the paper and not re-measured here.")
gate("Ⓖ① the r_D convention is declared and its sensitivity measured rather than assumed",
     bool(len(_sens) == 3 and all(v < 0 for _, v in _sens)))
gate("Ⓖ② and the answer is a DIFFERENCE at a common convention, so the convention cancels from it "
     "to first order -- which is checked by re-running the difference at a shifted r_D",
     bool(abs((running_window(dict(rs=ARM['rs'], DM=ARM['DM'], rD=ARM['rD'] * 1.05))
               - running_window(dict(rs=CTL['rs'], DM=CTL['DM'], rD=CTL['rD'] * 1.05))) - DIFF)
          < 0.5 * abs(DIFF)))

# ═════════════════════════════════════════════════════════════════════════════════════════════════
head("SUMMARY")
# ═════════════════════════════════════════════════════════════════════════════════════════════════
print(f"    gates run: {len(ran)}    failed: {len(fail)}")
for f in fail:
    print(f"      FAILED: {f}")
print()
print(f"    ⇒ arm minus control, kernel phase across {LLO:.0f}-{LHI:.0f}:  {DIFF:+.4f} deg")
print(f"    ⇒ the residual:                                     {RESIDUAL:+.1f} deg")
print(f"    ⇒ {np.log10(abs(RESIDUAL/DIFF)):.2f} orders of magnitude below -- THE PROJECTION IS CLEARED")
print(f"    ⇒ and the kernel's own phase is {100*_frac:.1f}% of the residual, common mode to "
      f"{100*abs(wA-wC)/abs(wA):.2f}%")

if fail:
    raise SystemExit(1)
