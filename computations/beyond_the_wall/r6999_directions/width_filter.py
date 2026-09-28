"""⓶ THE FILTER APPLIED TO THE PROJECTION WIDTH, ON PAPER, BEFORE ANY RUN -- r6999+cc66.52.

⛔ *The order's ⓶: "apply your own filter to it before running it.  If it fails the filter on paper,
that is the answer and the run is not needed."  The criterion is `r6993`'s, committed before this
measurement: the target's departure GROWS (G = 3.55) and DECELERATES (curvature negative).*

** THIS FILE CARRIES A CORRECTION TO ITS OWN FIRST PASS AND KEEPS THE SUPERSEDED NUMBER. **
The first estimate written here treated the projection kernel as a PLANE WAVE in conformal time --
`Phi(k) = |INT g(eta) e^{-i k eta} d eta| / INT g d eta` -- on the reading that the Bessel argument
`k(eta_0 - eta)` advances at rate `k`.  ⛔ ** It does not. **  `j_l(x)` near its turning point
`x ~ l` -- which is where the whole window sits, because `k D_M ~ l` is what the projection is --
oscillates in `x` at local rate `sqrt(1 - l^2/x^2)`, which goes to ZERO there.  The plane-wave proxy
therefore assigns the window a smearing it does not apply.  *Measured below: at the top band it
overstates the size of the departure by a factor of FIFTEEN and gets its SIGN wrong.*  ⇒ The correct
computation uses the
instrument's own kernel, `scipy.special.spherical_jn`, at the instrument's own `l`, `k`, `eta_0`.

** AND THE OPERATION THE ORDER ASKS FOR IS NAMED EXACTLY, BECAUSE IT IS NOT THE OBVIOUS ONE. **  ⓵:
*"give the control arm this arm's conformal width AT THE SAME LEAF WIDTH"*.  So the source's acoustic
phase `cos(k rs_leaf(eta))` is held at the control's and only the BESSEL argument is stretched:

    I_l(k; s) = | INT g(eta) exp(i k rs_leaf(eta)) j_l( k (eta_0 - a - s (eta - a)) ) d eta |

with `s` the measured conformal-width ratio and `a` the fixed point of the stretch.  `s = 1` is the
control as built.  ⌗ *Holding the phase is what makes this the PROJECTION channel and not `cc66.47`'s
window channel over again.*

⚠ ** AND `a` IS NOT A CONVENTION, WHICH IS THE SECOND FINDING. **  A stretch needs a fixed point, and
the two natural ones -- the visibility's MEAN in eta and its PEAK -- give answers of opposite sign.
A stretch about the wrong point is a stretch plus a DISPLACEMENT, and a displacement of the window
moves the comb rather than the contrast.  ⇒ *Both are reported; neither is chosen; the spread between
them is the honest size of the channel.*
"""
import os

import numpy as np
from scipy.special import spherical_jn

SP = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'spectra')
A = {t: np.load(os.path.join(SP, f'r6959_eta_{t}.npz')) for t in ('lcdm', 'cr')}
F = {t: np.load(os.path.join(SP, f'r6941_fine_{t}.npz')) for t in ('lcdm', 'cr')}
QE = A['cr']['q_edges']
QC = 0.5 * (QE[:-1] + QE[1:])
NL = 21


def norm_vis(t):
    d = A[t]
    e = np.asarray(d['eta'], float)
    g = np.asarray(d['vis'], float)
    return e, g / np.trapezoid(g, e)


def chi_half(x, w, e):
    """the half-fall width of a distribution: 1/kappa where |characteristic function| = 1/2"""
    from scipy.optimize import brentq
    f = lambda k: np.hypot(np.trapezoid(w * np.cos(k * x), e), np.trapezoid(w * np.sin(k * x), e)) - 0.5
    hi = 1e-3
    while f(hi) > 0:
        hi *= 2
    return 1.0 / brentq(f, 1e-9, hi)


def plane_wave_ratio():
    """THE SUPERSEDED ESTIMATE -- kept because it is what the filter was first applied to"""
    out = []
    for t in ('lcdm', 'cr'):
        e, g = norm_vis(t)
        k = np.pi * QC / float(A[t]['r_s'])
        out.append(np.array([np.hypot(np.trapezoid(g * np.cos(kk * e), e),
                                      np.trapezoid(g * np.sin(kk * e), e)) for kk in k]))
    return out[1] / out[0], out[0], out[1]


def stretch_ratio(s, anchor):
    """the control's OWN projection, recomputed with its conformal window widened by s and its leaf
    phase untouched -- the order's ⓵ operation, done in the kernel rather than in a solve"""
    d = A['lcdm']
    e, g = norm_vis('lcdm')
    rl = np.asarray(d['rs_leaf'], float)
    e0 = float(d['D_M']) + float(d['eta_ls'])
    rs, lA = float(d['r_s']), float(d['l_A'])
    a = float(np.trapezoid(g * e, e)) if anchor == 'mean' else float(e[np.argmax(g)])

    def amp(l, k, ss):
        j = spherical_jn(l, k * (e0 - a - ss * (e - a)))
        return np.hypot(np.trapezoid(g * np.cos(k * rl) * j, e), np.trapezoid(g * np.sin(k * rl) * j, e))

    return np.array([np.mean([amp(int(round(q * lA)), np.pi * q / rs, s)
                              / amp(int(round(q * lA)), np.pi * q / rs, 1.0)
                              for q in np.linspace(lo, hi, NL)])
                     for lo, hi in zip(QE[:-1], QE[1:])])


def env_a(x, y, win=1.0):
    e = np.empty_like(y)
    for j, v in enumerate(x):
        m = (x >= v - win / 2) & (x <= v + win / 2)
        e[j] = np.mean(y[m])
    return e


def bands(d):
    q = d['ls'].astype(float) / float(d['l_A'])
    e = env_a(q, d['Dl'])
    o = (d['Dl'] - e) / e
    return np.array([float(np.std(np.interp(np.linspace(a, b, 400), q, o)))
                     for a, b in zip(QE[:-1], QE[1:])])


def teeth(r, lbl):
    dd = r - 1.0
    crosses = dd.min() < 0.0 < dd.max()
    G = float('nan') if crosses else dd[-1] / dd[0]
    c = float(np.polyfit(QC, dd, 2)[0])
    print(f"\n  {lbl}")
    print(f"    departure {dd[0]:+.5f} -> {dd[-1]:+.5f}   "
          f"growth G = {'UNDEFINED (the departure crosses zero)' if crosses else f'{G:7.2f}'}"
          f"   curvature {c:+.6f}")
    return dd, G, c


print(__doc__)
print('=' * 100)

SE = {t: chi_half(norm_vis(t)[0], norm_vis(t)[1], norm_vis(t)[0]) for t in ('lcdm', 'cr')}
S = SE['cr'] / SE['lcdm']
print(f"\n  the measured conformal-width ratio, at the half-fall of the window's own characteristic "
      f"function:\n    control {SE['lcdm']:.5f}   arm {SE['cr']:.5f}   -> s = {S:.5f}")

PW, PL, PC = plane_wave_ratio()
print('\n  ⛔ THE SUPERSEDED PLANE-WAVE ESTIMATE (kept; it is what the filter was first applied to):')
print('   q      ' + '  '.join(f'{x:7.2f}' for x in QC))
print('   control' + '  '.join(f'{x:7.4f}' for x in PL))
print('   arm    ' + '  '.join(f'{x:7.4f}' for x in PC))
print('   ratio  ' + '  '.join(f'{x:7.4f}' for x in PW))

RM = stretch_ratio(S, 'mean')
RP = stretch_ratio(S, 'peak')
print(f'\n  ⛭ THE CORRECT KERNEL -- spherical_jn at the instrument\'s own l, k, eta_0, {NL} multipoles '
      f'per band:')
print('   mean-anchored ' + '  '.join(f'{x:7.5f}' for x in RM))
print('   peak-anchored ' + '  '.join(f'{x:7.5f}' for x in RP))
print(f'\n   ⇒ at the top band the plane-wave proxy overstates the departure by a factor '
      f'{abs(PW[-1] - 1) / abs(RM[-1] - 1):.1f} and reverses its sign (against mean-anchored)')

TGT = bands(F['cr']) / bands(F['lcdm'])
print('\n  and the target, the measured arm/control contrast ratio, for the same bands:')
print('   target ' + '  '.join(f'{x:7.4f}' for x in TGT))

dT, gT, cT = teeth(TGT, 'THE TARGET')
dM, gM, cM = teeth(RM, 'THE PROJECTION WIDTH, mean-anchored')
dP, gP, cP = teeth(RP, 'THE PROJECTION WIDTH, peak-anchored')
dW, gW, cW = teeth(PW, 'THE SUPERSEDED PLANE-WAVE ESTIMATE')

print('\n' + '=' * 100)
print(f"""
  ⛔ THE VERDICT, TOOTH BY TOOTH.

    SIGN       mean-anchored POSITIVE, matching the target; peak-anchored NEGATIVE at the bottom and
               positive at the top, so it crosses.  ** NOT DETERMINED ON PAPER. **
    GROWTH     mean-anchored G = {gM:.2f} against the target's {gT:.2f} -- the same direction, steeper.
               Peak-anchored it is UNDEFINED, the departure crossing zero.
    CURVATURE  {cM:+.6f} mean-anchored and {cP:+.6f} peak-anchored, against the target's {cT:+.6f}.
               ** BOTH ACCELERATE WHERE THE TARGET DECELERATES: FAILS. **
    SIZE       at the top band the channel delivers {100 * dM[-1]:+.2f} per cent (mean) or
               {100 * dP[-1]:+.2f} (peak), against the {100 * dT[-1]:+.2f} the measurement needs --
               at most {100 * abs(dM[-1]) / abs(dT[-1]):.0f} per cent of it.

  ⇒ ** THE CHANNEL IS REAL, IS AT MOST A QUARTER OF THE EXCESS AT THE TOP BAND, AND ITS SIGN IS NOT
    DETERMINED WITHOUT NAMING THE FIXED POINT OF THE STRETCH.  IT FAILS THE CURVATURE TOOTH UNDER BOTH
    ANCHORINGS. **  *It is not the carrier.  It is not excluded as a contributor.*

  ⚠ AND THE FILTER ITSELF NEEDED A THIRD TOOTH, FOUND ON THE SUPERSEDED ESTIMATE AND REGISTERED
    ANYWAY BECAUSE IT IS A DEFECT OF THE STATISTIC AND NOT OF THAT ESTIMATE.  The plane-wave numbers
    run {dW[0]:+.5f} -> {dW[-1]:+.5f}: G = {gW:.2f} and curvature {cW:+.6f}, ** which passes both
    pre-registered teeth while moving the contrast the WRONG WAY at every band. **  G is a ratio of a
    departure to a departure and is blind to their common sign.  ⇒ *The filter's first tooth is now
    SIGN, and G is read only after it.*
""")
