r"""
RECEIPT -- P15: ** `r7223` ORDERED IT: `evaluate the kernel's own phase contribution on EACH ARM'S OWN
r_s, D_M and r_D, and state the difference between the two arms against the measured residual's
size`.  *** THE DIFFERENCE IS `$-0.0141^{\circ}$` AGAINST A RESIDUAL OF `$-78.3^{\circ}$` (r7657;
`$-96.6$` before it) -- NEARLY
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
  difference is `$1.8\times10^{-4}$` of the residual (r7657's `$-78.3$`; `$1.5\times10^{-4}$`
  against the `$-96.6$` this file used before it).  No threshold the row could reasonably set is
  anywhere near it.*

  ⌈ ⛭⛭ ** AND THE PRE-REGISTERED THIRD OUTCOME HOLDS ALONGSIDE IT, WHICH IS A DIFFERENT STATEMENT
  FROM `cleared`. **  *The kernel's ABSOLUTE running phase is `$-15.45^{\circ}$`, which is `$19.7$`
  per cent of the residual's `$-78.3^{\circ}$` -- A FIFTH, and a sixth of the `$-96.6$` this file
  measured against before r7657 re-pointed it -- and it is present in ANY spectrum this
  instrument projects, the control's included, agreeing between the arms to `$0.09$` per cent.*
  ⇒ **So `a running phase at correct spacing` is not a phase-clean observable: a fifth of the scale
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
import re                     # r7655: the endpoint logs and the paper are parsed, not typed
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
# ⛭⛭⛭ r7657 (69's ask, verbatim): "** Please re-point the closing receipt's gates from -96.6 to it **"
#   -- `it` being -78.3, the ARM OF RECORD's own drift at l.2142, which r7655 routed as a discrepancy
#   between this file and the paragraph it closes.  ** The paragraph and this receipt now measure
#   against the same residual, which is what Ⓗ⑥ asked for and no longer has to report. **
#   ⌗ *Every `orders below` in this file moves with it, and so does the FLOOR FRACTION: 15.4 against
#     78.3 is a FIFTH where 15.4 against 96.6 was a sixth.  69 landed `a fifth` on that reading, so
#     Ⓕ moves with the constant rather than being left to contradict the paper.*
#   ⌷ *THE FILENAME STILL SAYS `a_sixth_of_the_scale_is_common_mode`, and it is now the namesake's
#     fraction.  A rename reaches `receipts/INDEX.md`, the appendices and every `\rcpt` that cites
#     this file across six documents, so it is ROUTED to 69 and not done here.*
RESIDUAL = -78.3              # degrees of a comb period, l.2142 (r7657); was -96.6 before r7657
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
def phase_window(l, rs, DM, rD, nu=20000, reach=80.0, ns=None, **_):
    """arg INT dt W(x;l) exp(2i (x-l) r_s/D_M),  x = l cosh t.  The substitution absorbs the
    inverse-square-root edge of <j_l^2> = 1/(x sqrt(x^2-l^2)) exactly, so this is plain quadrature.

    ⛭ `ns` was the module constant `NS` until r7655.  It is now an argument DEFAULTING to it, so
    every call above is unchanged -- but the arm of record RAN AT `NS=1.015066` while the control
    ran at the instrument default `0.96`, and a tilt the two arms do not share is a THIRD input to
    a kernel the paper calls a function of two ratios.  Ⓗ below measures what that costs.
    """
    ns = NS if ns is None else ns
    tmax = np.arccosh(max(1.0 + 1e-12, reach * DM / (l * rD)))
    t = np.linspace(0.0, tmax, nu)
    x = l * np.cosh(t)
    k = x / DM
    W = k ** (ns - 2) * np.exp(-2.0 * (k * rD) ** 2) / x
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

# ───────────────────────────────────────────────────────────────────────────────────────────────
# ⛭⛭⛭ r7651+cc66.93 -- ** Ⓐ③ᵃᵒʳ: THE ACOUSTIC-ANGLE HALF OF THE CLAIM, ON THE ARM OF RECORD,
#   ordered by `r7651` ⓷ -- and the other half is BLOCKED ON A BANK, which is said here rather
#   than left to be inferred from an absence. **
#
#   l.2385 claims the arms "share the other, the acoustic angle, to A PART IN SEVENTY THOUSAND".
#   `r_s/D_M` IS `theta_*/pi`, and it needs only `r_s` and `D_M`, both of which the arm-of-record
#   sibling's `cr_base.npz` carries.  So this half is measurable now and is measured here.
#
#   ⛔ ** THE r_D HALF IS NOT. **  `r7093_directions/grid_oneclock_leafrec1/` holds nine `cr_*.npz`
#   and NO `cr_base.log`, and `arm_inputs` reads `r_D` out of that log's line
#   `diffusion: r_D at the visibility peak = ... Mpc`.  Without it `rD` is `None` and every figure
#   downstream of it -- the `0.27` per cent in `r_D/D_M`, and therefore the `-0.014` degrees the
#   sentence turns on -- cannot be computed on the arm of record at all.  *The ask, for 70: the
#   `cr_base.log` beside that sibling grid, or `r_D` banked as a key in the `.npz`.  One line of
#   output, and it unblocks a figure in print.*
AGO = GO + '_leafrec1'
_aor_base = os.path.join(AGO, 'cr_base.npz')
_aor_log = os.path.join(AGO, 'cr_base.log')
_zA = np.load(_aor_base, allow_pickle=True)
AORD = dict(rs=float(_zA['r_s']), DM=float(_zA['D_M']), lA=float(_zA['l_A']),
            rD=None, has_log=os.path.exists(_aor_log))
_t_ns = ARM['rs'] / ARM['DM']
_t_ao = AORD['rs'] / AORD['DM']
_t_ct = CTL['rs'] / CTL['DM']
_rel_ns = abs(_t_ns / _t_ct - 1)
_rel_ao = abs(_t_ao / _t_ct - 1)
print(f"\n    theta_*/pi = r_s/D_M, this grid's own bases:")
print(f"      control          r_s {CTL['rs']:11.6f}  D_M {CTL['DM']:13.6f}  "
      f"r_s/D_M {_t_ct:.10f}")
print(f"      namesake arm     r_s {ARM['rs']:11.6f}  D_M {ARM['DM']:13.6f}  "
      f"r_s/D_M {_t_ns:.10f}   1 part in {1 / _rel_ns:,.0f}")
print(f"      ARM OF RECORD    r_s {AORD['rs']:11.6f}  D_M {AORD['DM']:13.6f}  "
      f"r_s/D_M {_t_ao:.10f}   1 part in {1 / _rel_ao:,.0f}")
print(f"      and l_A on this grid: control {CTL['lA']:.4f}, namesake {ARM['lA']:.4f} "
      f"({100 * (ARM['lA'] / CTL['lA'] - 1):+.4f}%), arm of record {AORD['lA']:.4f} "
      f"({100 * (AORD['lA'] / CTL['lA'] - 1):+.4f}%)")
gate("⛭⛭⛭ ** Ⓐ③ᵃᵒʳ l.2385's `a part in seventy thousand` IS THE NAMESAKE'S, and on the arm of "
     "record the acoustic angle is shared to A PART IN TWELVE THOUSAND -- a factor 5.3 looser, and "
     "still shared. **  *1 part in 63,059 becomes 1 part in 11,927.  The CLAIM survives: the two "
     "arms do share the angle, because the angle is what this construction computes, and 1.2e-4 is "
     "still four orders below the residual the sentence compares it with.  The FIGURE moves and is "
     "routed.*",
     bool(60000 < 1 / _rel_ns < 70000 and 10000 < 1 / _rel_ao < 13000 and _rel_ao > 4.0 * _rel_ns))
gate("⛔⛭⛭ ** AND THE OTHER HALF IS BLOCKED, WHICH THIS GATE ASSERTS AS A FACT ABOUT THE BANK "
     "RATHER THAN LEAVING AS A GAP: ** the arm-of-record sibling grid has its nine `cr_*.npz` and "
     "NO `cr_base.log`, so `r_D` -- read from that log's `diffusion: r_D at the visibility peak` "
     "line -- cannot be had, and the `0.27` per cent in `r_D/D_M` and the `-0.014` degrees "
     "downstream of it are not computable on this arm.  ⇒ *The ask is one line of output: that log, "
     "or `r_D` banked as a key*",
     # ⛭ r7653 (69): 70 banked that log at r7651+70.1 (an addition), so the gate now holds either
     #   state of the bank: the log absent, as when this gate was written, or present and carrying the
     #   `r_D` line the computation needs -- which unblocks the other half for cc66's re-point.
     bool(os.path.isdir(AGO)
          and len([f for f in os.listdir(AGO) if f.endswith('.npz')]) == 9
          and (not AORD['has_log']
               or 'diffusion: r_D at the visibility peak' in open(_aor_log).read())))

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

#
# ⛔ ** l.2387-2388's OTHER CONVENTION HAD NO CARRIER ANYWHERE IN THE CORPUS. **  The sentence reads
#   "The two arms' damping lengths respond to the choice of endpoint in opposite directions, so on
#   the other convention their separation in the governing ratio widens tenfold and the difference
#   between them changes sign, at 0.14 degrees; the clearance survives either way, at no less than
#   2.8 orders of magnitude."  ** Every banked log in this corpus reports exactly ONE endpoint --
#   `r_D at the visibility peak` -- and to two decimals. **  So neither half of that sentence was
#   reproducible from any banked quantity, on any arm, when it was written.
#   ⇒ `ACOUSTIC_two_arm.py` now prints the whole endpoint table beside its original line, additively
#     and at six decimals, and `r7655_cc66_the_endpoint_conventions/` banks one run per arm.
#
# ⛭ ** THE SHORTCUT IS LICENSED BY A GATE AND NOT BY AN ARGUMENT. **  Those runs use `LMAXL=100
#   LSTEP=50` and take eight seconds each, because r_D is a BACKGROUND quantity built before the
#   hierarchy is touched.  Ⓗ① asserts that each cheap run's two-decimal line equals the PRODUCTION
#   bank's -- 7.10, 7.12, 7.26 -- so if the shortcut ever stops being legitimate this receipt says so
#   instead of quietly reporting a spectrum-resolution artefact as a damping length.
# ⛭ ** THE PAPER IS OPENED HERE AND BOUND TO A NAME, which is what makes the two gates below
#   READS-PAPER rather than NO-READ.  r7655: `check_unread_figure` flagged Ⓗ④ and Ⓗ⑥ as two NEW
#   unread-figure keys, and it was RIGHT -- they attributed `0.14 degrees`, `2.8 orders` and `-78.3`
#   to the paper while their verdicts depended on nothing read out of it.  Ⓗ⑥ even called `open()`
#   on the `.tex`, but INSIDE the boolean, so no name carried the read and the taint could not see
#   it.  ** A figure attributed to the paper has to be READ OUT OF THE PAPER, and the fifth time
#   this seat has been told is the time to stop needing to be told. **
_P15TEX = open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'),
               encoding='utf-8', errors='replace').read()
_P15FLAT = re.sub(r'\s+', ' ', _P15TEX)
_PAPER_CONV = re.search(r'their separation in the governing ratio widens (\w+) and the difference '
                        r'between them changes sign, at \$([\d.]+)\$ degrees; the clearance '
                        r'survives either way, at no less than \$([\d.]+)\$ orders', _P15FLAT)
_PAPER_RESID = re.search(r'against a residual of \$([-\d.]+)\$', _P15FLAT)
# ⛭ ** BOTH READS TOLERATE THEIR OWN MISS, AND THE MISS IS PRINTED.  r7655: `check_quote_pins`
#   named these two REGEXES as sentence pins on 69's wording, and it was right -- worse, a reworded
#   sentence would have made `.group()` RAISE, and a crash is not a verdict.  ** This turn ROUTES
#   both sentences for rewording, so each read is one arm of a disjunction whose other arm is "the
#   sentence is no longer there", and the gates below take that arm explicitly. **
_P_WORD = _PAPER_CONV.group(1) if _PAPER_CONV else None
_P_DEG = float(_PAPER_CONV.group(2)) if _PAPER_CONV else None
_P_ORD = float(_PAPER_CONV.group(3)) if _PAPER_CONV else None
_P_RES = float(_PAPER_RESID.group(1)) if _PAPER_RESID else None
print(f"    read out of the paper: l.2387-2388 "
      + (f"says `{_P_WORD}`, {_P_DEG} degrees, {_P_ORD} orders"
         if _PAPER_CONV else "** NO LONGER CARRIES THAT SENTENCE -- reworded since r7655 **")
      + ";  l.2383's residual "
      + (f"{_P_RES}" if _PAPER_RESID else "** NOT FOUND -- reworded since r7655 **"))

EPD = os.path.join(BW, 'r7655_cc66_the_endpoint_conventions')
_EP_LOGS = {'control': 'control_lcdm.log', 'namesake': 'namesake_arm_cr.log',
            'arm of record': 'arm_of_record_cr_leafrec1.log'}


def endpoints(fn):
    """every `r_D at <convention>` row the run printed, plus the n_s it actually ran at."""
    txt = open(os.path.join(EPD, fn), encoding='utf-8', errors='replace').read()
    eps = {m.group(1).strip(): float(m.group(2))
           for m in re.finditer(r'r_D at (.+?)\s+eta =\s*[\d.]+\s+r_D =\s*([\d.]+) Mpc', txt)}
    two_dp = re.search(r'r_D at the visibility peak = ([\d.]+) Mpc', txt)
    ns = 0.96
    sw = re.search(r'__SWITCHES__.*', txt)
    if sw:
        for tok in sw.group(0).split():
            if tok.startswith('NS='):
                ns = float(tok[3:])
    return dict(eps=eps, ns=ns, two_dp=float(two_dp.group(1)))


EP = {k: endpoints(v) for k, v in _EP_LOGS.items()}
_PROD = {'control': CTL['rD'], 'namesake': ARM['rD'], 'arm of record': 7.26}
print("    the cheap runs against the PRODUCTION banks, two-decimal visibility-peak line:")
for k in _EP_LOGS:
    print(f"      {k:14s} cheap run {EP[k]['two_dp']:.2f} Mpc   production bank "
          f"{_PROD[k]:.2f} Mpc   n_s as run {EP[k]['ns']:.6f}")
gate("Ⓗ① ** THE LICENCE FOR THE EIGHT-SECOND RUNS, ASSERTED: ** each one's two-decimal "
     "visibility-peak r_D equals the production bank's, so r_D is independent of the spectrum "
     "resolution these runs threw away -- which is what makes the endpoint table a measurement of "
     "the same arms and not of a cheaper instrument",
     bool(all(abs(EP[k]['two_dp'] - _PROD[k]) < 5e-3 for k in _EP_LOGS)))

# ═════════════════════════════════════════════════════════════════════════════════════════════════
head("Ⓕ  THE PRE-REGISTERED THIRD OUTCOME, WHICH HOLDS ALONGSIDE `cleared` AND IS NOT THE SAME THING")
# ═════════════════════════════════════════════════════════════════════════════════════════════════
# ⌗ lifted above Ⓕ at r7657: the floor is now read on the arm of record, so Ⓕ needs it too.
def _run(p, ns):
    return -(phase_window(LHI, **p, ns=ns) - phase_window(LLO, **p, ns=ns)) * DEG


# ⛭⛭⛭ r7657 -- ** THE FLOOR IS RE-POINTED ONTO THE ARM OF RECORD, because that is the figure 69
#   LANDED: "the kernel's own running phase is `-15.4` degrees, a fifth of the residual, and common
#   to the two arms to three tenths of a per cent". **  `wA`/`wC` below are the NAMESAKE pair, which
#   is what this gate measured before r7657 and is kept beside the new pair rather than replaced --
#   the namesake's agreement is TIGHTER and dropping it would hide that.
_AOR_FLOOR = _run(dict(rs=AORD['rs'], DM=AORD['DM'],
                       rD=EP['arm of record']['eps']['visibility peak']), 0.96)
_CTL_FLOOR = _run(dict(rs=CTL['rs'], DM=CTL['DM'],
                       rD=EP['control']['eps']['visibility peak']), 0.96)
_frac = abs(_AOR_FLOOR / RESIDUAL)
_frac_ns = abs(wA / RESIDUAL)
print(f"    the kernel's ABSOLUTE running phase, ARM OF RECORD at a common tilt: "
      f"{_AOR_FLOOR:+.4f} deg = {100*_frac:.1f}% of the residual {RESIDUAL:+.1f}")
print(f"    its control, same tilt:                   {_CTL_FLOOR:+.4f} deg -- the two agree to "
      f"{100*abs(_AOR_FLOOR-_CTL_FLOOR)/abs(_AOR_FLOOR):.2f}%")
print(f"    and the NAMESAKE pair, for comparison:    {wA:+.4f} / {wC:+.4f} deg "
      f"= {100*_frac_ns:.1f}%, agreeing to {100*abs(wA-wC)/abs(wA):.2f}%")
gate("⛭⛭⛭ ** Ⓕ① l.2393's FLOOR, ON THE ARM OF RECORD: the kernel's own running phase is -15.4 "
     "degrees, A FIFTH of the residual -- which is a fifth because r7657 re-pointed the residual "
     "onto -78.3, and was a sixth against -96.6 on the same phase. **  *The figure moved because "
     "the DENOMINATOR moved, not the measurement: `-15.41` against `-78.3` is 19.7 per cent and "
     "against `-96.6` was 16.0.*",
     bool(abs(_AOR_FLOOR - -15.4) < 0.05 and 0.18 < _frac < 0.22))
gate("⛭⛭ Ⓕ② and it is COMMON MODE on the arm of record to THREE TENTHS of a per cent, which is "
     "l.2394's figure and is LOOSER than the namesake pair's tenth: the two arms carry the floor to "
     "0.27 per cent of itself here against 0.09 per cent there.  *Stated as a weakening rather "
     "than folded into one tolerance, because the claim is about THIS arm.*",
     bool(abs(_AOR_FLOOR - _CTL_FLOOR) / abs(_AOR_FLOOR) < 3.5e-3
          and abs(wA - wC) / abs(wA) < 1e-3))
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
print("    ⌗ the residual is QUOTED from the paper (l.2142 via l.2383) and not re-measured here;")
print("      r7657 re-pointed it from -96.6 to the arm of record's own drift, and Ⓗ⑥ checks the")
print("      constant back against the paper rather than trusting the edit.")
gate("Ⓖ① the r_D convention is declared and its sensitivity measured rather than assumed",
     bool(len(_sens) == 3 and all(v < 0 for _, v in _sens)))
gate("Ⓖ② and the answer is a DIFFERENCE at a common convention, so the convention cancels from it "
     "to first order -- which is checked by re-running the difference at a shifted r_D",
     bool(abs((running_window(dict(rs=ARM['rs'], DM=ARM['DM'], rD=ARM['rD'] * 1.05))
               - running_window(dict(rs=CTL['rs'], DM=CTL['DM'], rD=CTL['rD'] * 1.05))) - DIFF)
          < 0.5 * abs(DIFF)))

# ═════════════════════════════════════════════════════════════════════════════════════════════════
# ═════════════════════════════════════════════════════════════════════════════════════════════════
head("Ⓗ  ⛭⛭⛭ r7655 (cc66), ORDERED BY 69 ITEM 1 -- THE PARAGRAPH'S WHOLE SET ON THE ARM OF RECORD, "
     "AND THE OTHER CONVENTION MEASURED RATHER THAN QUOTED")
# ═════════════════════════════════════════════════════════════════════════════════════════════════

# ── the third input: the arm of record did not run at the control's tilt ─────────────────────────
_PK = 'visibility peak'
_aor = dict(rs=AORD['rs'], DM=AORD['DM'], rD=EP['arm of record']['eps'][_PK])
_ctl = dict(rs=CTL['rs'], DM=CTL['DM'], rD=EP['control']['eps'][_PK])
_ns_aor, _ns_ctl = EP['arm of record']['ns'], EP['control']['ns']


_d_own = _run(_aor, _ns_aor) - _run(_ctl, _ns_ctl)
_d_96 = _run(_aor, 0.96) - _run(_ctl, 0.96)
_d_ao = _run(_aor, _ns_aor) - _run(_ctl, _ns_aor)
print(f"\n    the arm of record's kernel phase against the control, across {LLO:.0f}-{LHI:.0f}:")
print(f"      each arm on its OWN n_s ({_ns_aor:.6f} vs {_ns_ctl:.2f}):  {_d_own:+.5f} deg   "
      f"{np.log10(abs(RESIDUAL / _d_own)):.2f} orders below the residual")
print(f"      both arms at a COMMON n_s = 0.96          :  {_d_96:+.5f} deg   "
      f"{np.log10(abs(RESIDUAL / _d_96)):.2f} orders")
print(f"      both arms at a COMMON n_s = {_ns_aor:.6f}    :  {_d_ao:+.5f} deg   "
      f"{np.log10(abs(RESIDUAL / _d_ao)):.2f} orders")
gate("⛭⛭⛭ ** Ⓗ② THE TWO-RATIO IDENTITY SURVIVES AT FIXED TILT AND THE ARMS DO NOT SHARE THE "
     "TILT.  l.2384's `exactly two dimensionless ratios` IS TRUE AT FIXED n_s AND INCOMPLETE FOR "
     "THIS PAIR. **  *The difference at a common n_s is the same number whichever common value is "
     "chosen -- 0.96 and 1.015066 agree to better than 1e-4 degrees -- so the identity holds.  But "
     "the arm of record RAN at 1.015066 and the control at 0.96, and n_s enters the kernel as "
     "k^(n_s-2), so as the runs were actually configured the difference is EIGHT TIMES the "
     "fixed-tilt one.  Both numbers are real and they answer different questions.*",
     bool(abs(_d_96 - _d_ao) < 1e-4 and abs(_d_own) > 5.0 * abs(_d_96)))

# ── the endpoint conventions, all five, on both pairs ───────────────────────────────────────────
CONV = ['eta_rec (fixed A_REC)', 'visibility peak', 'tau = 1',
        'visibility FWHM, early edge', 'visibility FWHM, late edge']
print(f"\n    EVERY DEFENSIBLE ENDPOINT, both pairs, at a common n_s = 0.96 "
      f"(so the tilt of Ⓗ② is held fixed and only the convention moves):")
print(f"      {'convention':31s} {'namesake: sep / phase':>26s}   {'arm of record: sep / phase':>26s}")
_rows = {}
for _c in CONV:
    _out = []
    for _k, _rs, _DM in (('namesake', ARM['rs'], ARM['DM']),
                         ('arm of record', AORD['rs'], AORD['DM'])):
        _rDa, _rDc = EP[_k]['eps'][_c], EP['control']['eps'][_c]
        _sep = (_rDa / _DM) / (_rDc / CTL['DM']) - 1
        _ph = (-(phase_window(LHI, _rs, _DM, _rDa, ns=0.96)
                 - phase_window(LLO, _rs, _DM, _rDa, ns=0.96)) * DEG
               - (-(phase_window(LHI, CTL['rs'], CTL['DM'], _rDc, ns=0.96)
                    - phase_window(LLO, CTL['rs'], CTL['DM'], _rDc, ns=0.96)) * DEG))
        _out.append((_sep, _ph))
        _rows[(_k, _c)] = (_sep, _ph)
    print(f"      {_c:31s} {_out[0][0]*100:+10.4f}% {_out[0][1]:+10.5f} deg   "
          f"{_out[1][0]*100:+10.4f}% {_out[1][1]:+10.5f} deg")

_ns_phases = [_rows[('namesake', c)][1] for c in CONV]
_ao_phases = [_rows[('arm of record', c)][1] for c in CONV]
gate("⛭⛭⛭ ** Ⓗ③ l.2386's `only the magnitude is a convention-free statement, and the sign is not` "
     "IS TRUE OF THE NAMESAKE PAIR AND FALSE OF THE ARM OF RECORD -- in the direction that "
     "STRENGTHENS the paragraph. **  *The namesake's difference changes sign between conventions "
     "(negative at the visibility peak and at eta_rec, POSITIVE at tau=1 and at the late FWHM "
     "edge).  On the arm of record every one of the five is POSITIVE, so there the sign is "
     "convention-free too, and 69's reading -- that the arm-of-record difference is already "
     "positive -- is a property of the arm and not of a choice.*",
     bool(min(_ns_phases) < 0 < max(_ns_phases) and all(p > 0 for p in _ao_phases)))
gate("⛔⛭⛭ ** Ⓗ④ AND NO ENDPOINT CONVENTION REPRODUCES l.2388's `0.14 degrees` OR ITS `no less "
     "than 2.8 orders`, ON EITHER PAIR.  THIS GATE ASSERTED THE MISS AND r7657 ACTED ON IT: 69 "
     "REMOVED BOTH FIGURES AND `widens tenfold` WITH THEM, so the read above now MISSES and "
     "this gate runs on its FALLBACK LITERALS -- kept as the record of what the sentence said "
     "and why it went, and the absence arm built at r7655 fired on its first real test one "
     "turn later. **  "
     "*The largest magnitude any of the five gives on the namesake pair is the late FWHM edge at "
     "0.080 deg, 2.99 orders below r7657's -78.3 -- a factor 1.8 short of 0.14, and only a FIFTH of "
     "an order clear of 2.8 where against -96.6 it was 3.08 and a quarter.  On the arm of record "
     "the five run 0.028 to 0.063 deg, 3.10 to 3.44 orders."
     "  ⌗ *The re-point COSTS this gate margin and the gate says so rather than being widened.*  ⇒ The "
     "sentence's mechanism is REAL and measured here -- the two arms' damping lengths do respond to "
     "the endpoint in opposite directions -- but its two figures are not this instrument's on "
     "either arm, and `widens tenfold` is the wrong direction: at eta_rec the namesake's separation "
     "NARROWS ninefold (-0.305% to -0.034%).*",
     bool((max(abs(p) for p in _ns_phases + _ao_phases) < (_P_DEG if _P_DEG else 0.14)
           and min(np.log10(abs(RESIDUAL / p)) for p in _ns_phases + _ao_phases)
               > (_P_ORD if _P_ORD else 2.8))
          and (_P_WORD == 'tenfold' or _PAPER_CONV is None)))

# ── the r_D/D_M share, attributed, and what two decimals costs it ────────────────────────────────
_sep_ns = (ARM['rD'] / ARM['DM']) / (CTL['rD'] / CTL['DM']) - 1
_sep_ns_full = _rows[('namesake', _PK)][0]
_sep_ao_full = _rows[('arm of record', _PK)][0]
_lo = ((_aor['rD'] - 0.005) / AORD['DM']) / ((_ctl['rD'] + 0.005) / CTL['DM']) - 1
_hi = ((_aor['rD'] + 0.005) / AORD['DM']) / ((_ctl['rD'] - 0.005) / CTL['DM']) - 1
print(f"\n    l.2385's `differ by 0.27 per cent` in r_D/D_M, attributed:")
print(f"      namesake, r_D as the log prints it (two decimals) : {_sep_ns*100:+.3f} per cent")
print(f"      namesake, r_D at six decimals                     : {_sep_ns_full*100:+.3f} per cent")
print(f"      ARM OF RECORD, six decimals                       : {_sep_ao_full*100:+.3f} per cent")
print(f"      and what TWO DECIMALS alone would allow there      : "
      f"[{_lo*100:+.3f}, {_hi*100:+.3f}] per cent")
gate("⛭⛭⛭ ** Ⓗ⑤ l.2385's `0.27 per cent` IS THE NAMESAKE'S AND IS ITSELF A ROUNDING ARTEFACT: at "
     "six decimals the same pair reads 0.305 per cent, and the ARM OF RECORD reads +0.81 per cent "
     "WITH THE SIGN REVERSED. **  *The two-decimal r_D the logs print moves the namesake's own "
     "figure by a tenth of its value, and on the arm of record it would allow anything from 0.68 "
     "to 0.96 -- which is why `about 0.8 per cent` is the honest precision for a two-decimal read "
     "and why the full-precision line was added.  The CLAIM -- the arms share the angle and differ "
     "in the damping ratio at the per-cent level -- survives on both arms.*",
     bool(abs(_sep_ns_full) > 1.1 * abs(_sep_ns) and _sep_ao_full > 0
          and _sep_ns_full < 0 and 0.0068 < _sep_ao_full < 0.0096))
# ⛭⛭ ** Ⓗ⑥ WAS A ROUTED DISCREPANCY AND r7657 RESOLVED IT, so this gate no longer reports a
#   mismatch -- it asserts the AGREEMENT.  At r7655 it read `l.2383 compares against -78.3 where
#   this file computes against -96.6, so every orders below in that paragraph is quoted against a
#   different denominator`; 69's ruling was to move the RECEIPT and not the paper, and `RESIDUAL`
#   at the top of this file is now the paragraph's own figure.
#   ⌗ *The DISJUNCTION STAYS, for the other reason it was written: the read can legitimately miss
#     if 69 rewords the sentence, and a crash is not a verdict.  What it no longer does is hold a
#     SECOND residual open as an acceptable state -- there is one residual now, and this file does
#     not get to pick which.*
if _PAPER_RESID is None:
    _res_state = "** NOT FOUND -- reworded since r7655, so the agreement cannot be checked **"
elif abs(_P_RES - RESIDUAL) < 1e-9:
    _res_state = f"{_P_RES}, and RESIDUAL here is {RESIDUAL} -- THE SAME FIGURE, which is r7657's ask"
else:
    _res_state = (f"{_P_RES}, against {RESIDUAL} here -- ** THESE NO LONGER AGREE: the paragraph "
                  f"moved again after r7657 and this file has to follow it **")
print(f"    l.2383's residual reads {_res_state}")
gate("⛭⛭ ** Ⓗ⑥ THE PARAGRAPH'S RESIDUAL AND THIS RECEIPT'S NOW AGREE, AND THE AGREEMENT IS "
     "THE GATE: `RESIDUAL` is checked BACK AGAINST l.2383 rather than left to be typed. **  "
     "*r7655 routed the discrepancy -- l.2383 compared against -78.3 where this file computed "
     "against -96.6, so every `orders below` in that paragraph was quoted against a different "
     "denominator than the gates here used.  r7657 ruled for the PAPER's figure and this file "
     "moved onto it, which is why Ⓕ① now reads a FIFTH where it read a sixth: the denominator "
     "moved and the measurement did not.  ** Still a disjunction on the READ and not on the "
     "residual: a reworded sentence makes the read miss and this gate prints the miss instead of "
     "crashing, but no second residual passes any more. **",
     bool(_PAPER_RESID is None or abs(_P_RES - RESIDUAL) < 1e-9))

# =================================================================================================
head("Ⓘ  ⛭⛭⛭ r7657 ITEM 3 -- EVERY FIGURE THE LANDED PARAGRAPH CARRIES, READ OUT OF THE "
     "PAPER AND MET BY A COMPUTATION HERE")
# =================================================================================================
# ⛭ ** 69's ITEM 3, verbatim: "Pin the kernel paragraph's landed figures where they are computed:
#   0.8 per cent, twelve thousand, +0.041, +0.028/+0.063, +0.33, the tilt's share, -15.4 and a
#   fifth."  Each one below is READ OUT OF `corpus/CR_cosmology.tex` and compared with what this
#   file measures -- the LITERAL TWIN pattern, so a figure drifting in either direction fails. **
#   ⌗ *Every read tolerates its own miss and PRINTS it: a reworded sentence must not crash a
#     receipt, and `.group()` on a `None` is not a verdict (the r7655 lesson, four rounds of it).*
#   ⌗ *The WORD figures are read as words and converted through `_WORDS` rather than being
#     matched as prose: `nearly nine tenths` is a quantitative claim and is gated as one.*
_WORDS = {'twelve thousand': 12000.0, 'seventy thousand': 70000.0,
          'a fifth': 0.2, 'a sixth': 1 / 6, 'nine tenths': 0.9, 'three tenths': 0.3}
_PAPER = {}


def paper(key, pat, *cast):
    """read ONE of l.2378-2397's figures out of the .tex, tolerate its absence, and print which."""
    m = re.search(pat, _P15FLAT)
    _PAPER[key] = tuple(c(g.strip()) for c, g in zip(cast, m.groups())) if m else None
    print(f"      {key:26s} " + (f"{_PAPER[key]}" if m else
                                 "** NOT FOUND -- reworded since r7657 **"))
    return _PAPER[key]


print("\n    l.2378-2397's figures, each READ OUT OF corpus/CR_cosmology.tex:")
paper('r_D/D_M, per cent', r'by about \$([\d.]+)\$ per cent and share the other', float)
paper('the angle, a part in', r'the acoustic angle, to a part in ([a-z ]+?), because', str)
paper('the range', r'degrees across \$(\d+)\\le\\ell\\le(\d+)\$', float, float)
paper('fixed-tilt difference', r'phase difference between the arms is \$\+([\d.]+)\$ degrees',
      float)
paper('endpoint range', r'the difference runs from \$\+([\d.]+)\$ to \$\+([\d.]+)\$ degrees',
      float, float)
paper('the two tilts', r'run at different ones, \$([\d.]+)\$ and \$([\d.]+)\$', float, float)
paper('as-run difference', r'as run, the difference is \$\+([\d.]+)\$ degrees, nearly '
                           r'([a-z ]+?) of it the tilt', float, str)
paper('the floor, share, spread', r"running phase is \$(-[\d.]+)\$ degrees, a ([a-z]+) of the "
                                 r"residual, and common to the two arms to ([a-z ]+?) of a per "
                                 r"cent", float, str, str)

_ANG_AOR = (AORD['rs'] / AORD['DM']) / (CTL['rs'] / CTL['DM']) - 1
_ANG_NS = (ARM['rs'] / ARM['DM']) / (CTL['rs'] / CTL['DM']) - 1
_TILT_SHARE = (_d_own - _d_96) / _d_own
_EP_LO, _EP_HI = min(_ao_phases), max(_ao_phases)
_ORD_96 = np.log10(abs(RESIDUAL / _d_96))
_ORD_OWN = np.log10(abs(RESIDUAL / _d_own))
_ORD_EP = min(np.log10(abs(RESIDUAL / q)) for q in _ao_phases)
print(f"\n    and what this file measures on the ARM OF RECORD, in the same order:")
print(f"      r_D/D_M                    {100*_sep_ao_full:+.3f} per cent")
print(f"      r_s/D_M, the angle         {_ANG_AOR:+.3e}  = one part in {1/abs(_ANG_AOR):,.0f}"
      f"   (the NAMESAKE's was one part in {1/abs(_ANG_NS):,.0f})")
print(f"      fixed tilt, both at 0.96   {_d_96:+.5f} deg   {_ORD_96:.2f} orders below"
      f" {RESIDUAL:+.1f}")
print(f"      across the five endpoints  {_EP_LO:+.5f} to {_EP_HI:+.5f} deg   {_ORD_EP:.2f} orders"
      f" at worst")
print(f"      as run ({_ns_aor:.6f} / {_ns_ctl:.2f})  {_d_own:+.5f} deg   {_ORD_OWN:.2f} orders"
      f" -- the tilt carries {100*_TILT_SHARE:.1f}% of it")
print(f"      the floor                  {_AOR_FLOOR:+.4f} deg = {100*_frac:.1f}% of the residual,"
      f" the two arms to {100*abs(_AOR_FLOOR-_CTL_FLOOR)/abs(_AOR_FLOOR):.2f}%")

_pc = _PAPER['r_D/D_M, per cent']
gate("⛭ Ⓘ① l.2381's `about 0.8 per cent` in r_D/D_M IS THE ARM OF RECORD's at the precision "
     "two decimals of r_D support.  *+0.807 at six decimals, and Ⓗ⑤ showed the two-decimal line "
     "alone would allow [0.67, 0.95] -- which is why `about` is in the sentence and why one more "
     "digit is not claimed.*",
     bool((_pc is None or abs(_pc[0] - round(100 * _sep_ao_full, 1)) < 1e-9)
          and 0.0068 < _sep_ao_full < 0.0096))
_ang = _PAPER['the angle, a part in']
gate("⛭⛭ ** Ⓘ② l.2382's `a part in twelve thousand` IS THE ARM OF RECORD's, AND IT IS A "
     "FIVE-FOLD WEAKENING of what the paragraph claimed before r7649: the namesake pair shared "
     "the acoustic angle to a part in 63,059 -- the `seventy thousand` that stood there -- and "
     "THIS arm shares it to a part in 11,927. **  *The arms share the angle LESS WELL on the arm "
     "of record, the paragraph now says so, and that is the honest direction for the figure to "
     "have moved.  The claim the sentence is making survives it: a part in twelve thousand is "
     "8.4e-5, which is still TWO ORDERS tighter than the 8.07e-3 they differ by in the damping "
     "ratio, so the one ratio is shared by construction and the other is not.*",
     bool((_ang is None or abs(_WORDS.get(_ang[0], -1) - 12000) < 1e-9)
          and 11000 < 1 / abs(_ANG_AOR) < 13000 and abs(_ANG_NS) < abs(_ANG_AOR)))
_rng, _ft = _PAPER['the range'], _PAPER['fixed-tilt difference']
gate("⛭ Ⓘ③ l.2385's `+0.041 degrees across 104 <= l <= 1886` IS THIS FILE's fixed-tilt "
     "difference AND THE RANGE IS THIS FILE's TOO, read back out of the sentence rather than "
     "assumed to match.  *+0.04106 rounds to +0.041, and `over three orders below` is 3.28.*",
     bool((_ft is None or abs(_ft[0] - 0.041) < 5e-4)
          and (_rng is None or (_rng[0] == LLO and _rng[1] == LHI))
          and abs(_d_96 - 0.041) < 5e-4 and 3.0 < _ORD_96 < 4.0))
_epr = _PAPER['endpoint range']
gate("⛭ Ⓘ④ l.2387-2389's `+0.028 to +0.063 degrees, always of one sign, no less than three "
     "orders on every convention` IS Ⓗ③'s TABLE, end to end.  *The five endpoints give +0.02829 "
     "to +0.06256, every one POSITIVE, the worst 3.10 orders below -78.3.  ** This is the sentence "
     "that replaced `widens tenfold`, `0.14 degrees` and `2.8 orders`, which Ⓗ④ found no "
     "convention reproduces -- so Ⓗ④ now gates a figure the paper no longer carries, and that "
     "is deliberate: it is the record of why the figure went. **",
     bool((_epr is None or (abs(_epr[0] - 0.028) < 5e-4 and abs(_epr[1] - 0.063) < 5e-4))
          and abs(_EP_LO - 0.028) < 5e-4 and abs(_EP_HI - 0.063) < 5e-4
          and all(q > 0 for q in _ao_phases) and _ORD_EP > 3.0))
_tl, _ar = _PAPER['the two tilts'], _PAPER['as-run difference']
gate("⛭⛭ ** Ⓘ⑤ l.2390-2392's AS-RUN SENTENCE, ALL FOUR OF ITS FIGURES: the tilts 1.015 and "
     "0.96 are THE SWITCHES THE TWO RUNS CARRY, the difference is +0.33, the tilt's share is "
     "nearly nine tenths, and `still over two orders below` is 2.37. **  *Measured 87.6 per cent "
     "of +0.33081 attributable to the tilt alone.  The tilts are checked against `__SWITCHES__` in "
     "the run logs, not against the paper's own words -- a paper figure met by the paper's figure "
     "would gate nothing.*",
     bool((_tl is None or (abs(_tl[0] - round(_ns_aor, 3)) < 1e-9 and _tl[1] == _ns_ctl))
          and (_ar is None or (abs(_ar[0] - 0.33) < 5e-3
                               and abs(_WORDS.get(_ar[1], -1) - 0.9) < 1e-9))
          and abs(_d_own - 0.33) < 5e-3 and abs(_TILT_SHARE - 0.9) < 0.05
          and 2.0 < _ORD_OWN < 3.0))
_fl = _PAPER['the floor, share, spread']
gate("⛭ Ⓘ⑥ l.2393-2395's FLOOR SENTENCE, read back: `-15.4 degrees`, `a fifth of the "
     "residual` and `three tenths of a per cent` are Ⓕ① and Ⓕ②'s three measurements, and the "
     "two WORD figures are converted and gated rather than left as prose.  *-15.4073, 19.7 per "
     "cent of -78.3, the two arms to 0.27 per cent.  A fifth to a tenth of a point is what the "
     "endpoint sweep leaves it -- l.2396's own claim -- and Ⓔ⑤'s sensitivity is what licenses "
     "that.*",
     bool((_fl is None or (abs(_fl[0] - round(_AOR_FLOOR, 1)) < 1e-9
                           and abs(_WORDS.get('a ' + _fl[1], -1) - 0.2) < 1e-9
                           and abs(_WORDS.get(_fl[2], -1) - 0.3) < 1e-9))
          and abs(_AOR_FLOOR - -15.4) < 0.05 and abs(_frac - 0.2) < 0.02
          and abs(100 * abs(_AOR_FLOOR - _CTL_FLOOR) / abs(_AOR_FLOOR) - 0.3) < 0.05))
gate("⛭ Ⓘ⑦ and the paragraph's THREE order-of-magnitude claims are each TRUE AND NOT "
     "UNDERSTATED, which is the one thing a `below` claim can get wrong in the safe direction and "
     "still be worth fixing: 3.28 for `over three`, 3.10 at worst for `no less than three`, 2.37 "
     "for `still over two`.  *Each lands in its own decade, so no claim is a decade shy of what "
     "was measured.*",
     bool(3.0 < _ORD_96 < 4.0 and 3.0 < _ORD_EP < 4.0 and 2.0 < _ORD_OWN < 3.0))

# =================================================================================================
head("Ⓙ  ⛭⛭⛭ r7657 ITEM 2 -- l.2395's FLOOR RANGE ON THE ARM OF RECORD, AND THE ENDPOINT "
     "CLAUSE BESIDE IT")
# =================================================================================================
# ⛭ ** 69's ITEM 2, verbatim: "The floor's range, l.2395: `runs from 9 to 24 per cent as the
#   range is taken from 200 or from 50`.  Measure it on the arm of record against the -78.3
#   residual."  ** THE ANSWER IS 11 AND 30, AND THE REASON IS THE DENOMINATOR AGAIN. **
#   ⌗ *The two PHASES behind 9 and 24 are already the arm of record's -- -8.75 and -23.25
#     degrees, which this file reproduces to four decimals.  Divided by -96.6 they are 9.06 and
#     24.06, which is where l.2395's figures come from.  r7657 re-pointed the floor sentence's own
#     `-15.4` and `a fifth` onto -78.3 and left the RANGE CLAUSE on the old residual, so the
#     sentence now quotes two fractions against one denominator and a third against another.*
def _runlo(lo, rD, ns=0.96):
    """the kernel's own running phase from `lo` to LHI, arm of record, one r_D convention."""
    return -(phase_window(LHI, rs=AORD['rs'], DM=AORD['DM'], rD=rD, ns=ns)
             - phase_window(lo, rs=AORD['rs'], DM=AORD['DM'], rD=rD, ns=ns)) * DEG


_rD_pk = EP['arm of record']['eps']['visibility peak']
_LOWS = (50.0, 104.0, 200.0, 300.0)
_FRAC_LO = {}
print(f"\n    the floor and its fraction as the range's LOW END moves, arm of record, r_D at the "
      f"visibility peak:")
for _lo in _LOWS:
    _ph = _runlo(_lo, _rD_pk)
    _FRAC_LO[_lo] = (_ph, abs(_ph / RESIDUAL), abs(_ph / -96.6))
    print(f"      from l = {_lo:6.1f} to {LHI:.0f}:  {_ph:+9.4f} deg = "
          f"{100*_FRAC_LO[_lo][1]:6.2f}% of {RESIDUAL:+.1f}"
          f"   ({100*_FRAC_LO[_lo][2]:6.2f}% of the -96.6 l.2395 still divides by)")
_PAPER_RANGE = re.search(r'moving under a tenth of a point, and runs from \$(\d+)\$ to \$(\d+)\$ '
                         r'per cent as the range is taken from \$(\d+)\$ or from \$(\d+)\$ instead',
                         _P15FLAT)
_PR = [float(g) for g in _PAPER_RANGE.groups()] if _PAPER_RANGE else None
print(f"    l.2395 reads " + (f"{_PR[0]:.0f} to {_PR[1]:.0f} per cent from {_PR[2]:.0f} or from "
                              f"{_PR[3]:.0f}" if _PR else
                              "** NOT FOUND -- reworded since r7657 **"))
gate("⛔⛭⛭⛭ ** Ⓙ① l.2395's `9 to 24 per cent` IS THE ARM OF RECORD'S OWN PHASES DIVIDED "
     "BY THE OLD RESIDUAL, AND AGAINST -78.3 THE RANGE IS 11 TO 30.  THIS GATE ASSERTS THE MISS "
     "AND ROUTES THE TWO FIGURES. **  *The phases are right and this file reproduces them: -8.7491 "
     "degrees from l = 200 and -23.2458 from l = 50.  Against -96.6 they are 9.06 and 24.06 per "
     "cent -- l.2395's two figures to the digit.  Against the -78.3 the SAME SENTENCE's `a fifth` "
     "is now quoted against, they are 11.17 and 29.69.  ⇒ ** The re-point reached the floor "
     "clause and not the range clause, so one sentence now carries two denominators.  Read from "
     "200 or from 50 instead, the floor runs from ELEVEN to THIRTY per cent. ** *",
     bool((_PR is None or (abs(_PR[0] - round(100 * _FRAC_LO[200.0][2])) < 1e-9
                           and abs(_PR[1] - round(100 * _FRAC_LO[50.0][2])) < 1e-9
                           and _PR[2] == 200.0 and _PR[3] == 50.0))
          and abs(100 * _FRAC_LO[200.0][1] - 11.17) < 0.05
          and abs(100 * _FRAC_LO[50.0][1] - 29.69) < 0.05))

# -- the clause the same sentence opens with, measured on the thing the sentence is about ---------
_FRAC_EP = {k: abs(_runlo(LLO, v) / RESIDUAL) for k, v in EP['arm of record']['eps'].items()
            if 'today' not in k}
_CENTRAL = ('eta_rec (fixed A_REC)', 'visibility peak', 'tau = 1')
_EDGES2 = ('visibility FWHM, early edge', 'visibility FWHM, late edge')
print("    and the same fraction with the range held at 104-1886, across the five endpoints:")
for _nm, _f in sorted(_FRAC_EP.items(), key=lambda kv: -kv[1]):
    print(f"      {_nm:32s} {100*_f:6.2f}%"
          + ("   <- one of the three the clause is true over" if _nm in _CENTRAL else
             "   <- a HALF-MAXIMUM EDGE"))
_SPREAD3 = 100 * (max(_FRAC_EP[k] for k in _CENTRAL) - min(_FRAC_EP[k] for k in _CENTRAL))
_SPREAD5 = 100 * (max(_FRAC_EP.values()) - min(_FRAC_EP.values()))
print(f"      spread across the THREE central conventions: {_SPREAD3:.2f} of a point;  "
      f"across all FIVE: {_SPREAD5:.2f} points")
gate("⛔⛭⛭ ** Ⓙ② AND l.2395's OTHER CLAUSE -- `it is insensitive to the endpoint "
     "convention, moving under a tenth of a point` -- IS TRUE OF THREE CONVENTIONS AND FALSE OF "
     "THE FIVE THE SAME PARAGRAPH NAMES. **  *Across eta_rec, the visibility peak and tau = 1 the "
     "fraction moves 0.05 of a point, which is the clause as written.  Across the two "
     "HALF-MAXIMUM EDGES it moves 8.10 points, from 13.09 to 21.19 per cent, because r_D itself "
     "runs 5.37 to 12.68 Mpc there and the FLOOR is a function of r_D while the DIFFERENCE is "
     "not.  ⇒ ** The clause imports the convention-independence of the arm-MINUS-arm difference "
     "(Ⓗ③, Ⓖ②) into a statement about ONE ARM's absolute phase, where it does not hold.  Routed: "
     "either name the three conventions, or say `under a tenth of a point between the three "
     "recombination-epoch conventions and eight points across the half-maximum edges`. ** *",
     bool(_SPREAD3 < 0.1 and _SPREAD5 > 1.0
          and all(0.10 < _FRAC_EP[k] < 0.25 for k in _FRAC_EP)))
# =================================================================================================
head("Ⓚ  EVERY FIGURE THE INDEX ROW AND THE DOCSTRING PRINT, PINNED AS A LITERAL TWIN")
# =================================================================================================
# ⛭ ** `check_figures_pinned`'s rule, in its own words: `a sentence prints a figure beside a
#   receipt that would not fail if it were wrong`.  r7657's INDEX row and this file's docstring
#   print SIXTEEN figures between them, and a gate that measures a quantity does not pin the
#   DIGITS a row quotes it to -- `pins()` only collects constants inside a comparison. **
#   ⌗ *So the chain below is the pin: one explicit comparison per printed figure, each on the
#     ROUNDING the row prints, so a row quoting 3.8 where this file measures 3.75 fails here.*
#   ⌗ *The table above the gate prints the MEASUREMENTS alone.  The literals live in exactly one
#     place -- the chain -- so there is nothing for a figure to drift against.*
_ORD_DIFF = np.log10(abs(RESIDUAL / DIFF))
_COMMON = 100 * abs(_AOR_FLOOR - _CTL_FLOOR) / abs(_AOR_FLOOR)
print("\n    what the row quotes, measured here:")
for _nm, _v, _nd in (("orders below, the headline difference", _ORD_DIFF, 2),
                     ("the floor, degrees", abs(_AOR_FLOOR), 2),
                     ("the floor as a per cent of the residual", 100 * _frac, 1),
                     ("the floor's common mode, per cent", _COMMON, 2),
                     ("orders below at a common tilt", _ORD_96, 2),
                     ("orders below at worst across endpoints", _ORD_EP, 2),
                     ("orders below as the arms were run", _ORD_OWN, 2),
                     ("the tilt's share of the as-run figure", 100 * _TILT_SHARE, 1),
                     ("n_s as the arm of record ran", _ns_aor, 3),
                     ("n_s as the control ran", _ns_ctl, 2),
                     ("the floor from l = 200, degrees", abs(_FRAC_LO[200.0][0]), 2),
                     ("the floor from l = 50, degrees", abs(_FRAC_LO[50.0][0]), 2),
                     ("the lowest endpoint fraction, per cent", 100 * min(_FRAC_EP.values()), 1),
                     ("the highest endpoint fraction, per cent", 100 * max(_FRAC_EP.values()), 1),
                     ("the spread across all five, points", _SPREAD5, 2),
                     ("the spread across the three, points", _SPREAD3, 2)):
    print(f"      {_nm:42s} {round(_v, _nd)}")
gate("⛭ Ⓚ① ** AND EVERY ONE OF THE SIXTEEN IS PINNED TO THE DIGIT THE ROW PRINTS IT TO, so a "
     "stale row reddens this receipt instead of going quietly wrong. **  *The one-state rule cuts "
     "both ways: an INDEX row states what its receipt finds NOW, and this gate is what makes the "
     "row's own digits the receipt's responsibility.*",
     bool(abs(round(_ORD_DIFF, 2) - 3.75) < 1e-9
          and abs(round(abs(_AOR_FLOOR), 2) - 15.41) < 1e-9
          and abs(round(100 * _frac, 1) - 19.7) < 1e-9
          and abs(round(_COMMON, 2) - 0.27) < 1e-9
          and abs(round(_ORD_96, 2) - 3.28) < 1e-9
          and abs(round(_ORD_EP, 2) - 3.10) < 1e-9
          and abs(round(_ORD_OWN, 2) - 2.37) < 1e-9
          and abs(round(100 * _TILT_SHARE, 1) - 87.6) < 1e-9
          and abs(round(_ns_aor, 3) - 1.015) < 1e-9
          and abs(round(_ns_ctl, 2) - 0.96) < 1e-9
          and abs(round(abs(_FRAC_LO[200.0][0]), 2) - 8.75) < 1e-9
          and abs(round(abs(_FRAC_LO[50.0][0]), 2) - 23.25) < 1e-9
          and abs(round(100 * min(_FRAC_EP.values()), 1) - 13.1) < 1e-9
          and abs(round(100 * max(_FRAC_EP.values()), 1) - 21.2) < 1e-9
          and abs(round(_SPREAD5, 2) - 8.10) < 1e-9
          and abs(round(_SPREAD3, 2) - 0.05) < 1e-9))

head("SUMMARY")
# ═════════════════════════════════════════════════════════════════════════════════════════════════
print(f"    gates run: {len(ran)}    failed: {len(fail)}")
for f in fail:
    print(f"      FAILED: {f}")
print()
print(f"    ⇒ arm minus control, kernel phase across {LLO:.0f}-{LHI:.0f}:  {DIFF:+.4f} deg")
print(f"    ⇒ the residual:                                     {RESIDUAL:+.1f} deg")
print(f"    ⇒ {np.log10(abs(RESIDUAL/DIFF)):.2f} orders of magnitude below -- THE PROJECTION IS CLEARED")
print(f"    ⇒ and the kernel's own phase is {100*_frac:.1f}% of the residual on the ARM OF "
      f"RECORD, common mode to {_COMMON:.2f}% there and to "
      f"{100*abs(wA-wC)/abs(wA):.2f}% on the namesake pair")

if fail:
    raise SystemExit(1)
