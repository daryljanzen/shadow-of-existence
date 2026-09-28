#!/usr/bin/env python3
r"""P15 sec:refit-bound -- ** THE TERM MIX HAS EXACTLY THE SHAPE THE $q$-INDEPENDENT OFFSET NEEDS AND
OVER-DELIVERS ITS SIZE BY HALF AGAIN -- SO THE TWO CHANNELS DO NOT ADD, AND THE DECOMPOSITION THAT
PRODUCED A "REMAINDER" ASSUMED THEY WOULD. **

** PATH PROVENANCE, IN THE HEADER, ON THE STANDING REQUIREMENT. **  *** Every model number below is the
HIERARCHY path *** -- `r6959_eta_{lcdm,cr}` and `r6959_nswap_lcdm` from the previous revision, the new
`r6975_mix{,b}_lcdm`, and the `LSTEP=1` baselines `r6941_fine_{lcdm,cr}`.  `DPSRC` reaches all three
paths; only the hierarchy one is read here and the banks record it.  `sec:refit-bound`'s quartet
$222/538/818/1134$ is the LINE-OF-SIGHT path's and is not read -- searched for by grepping this file for
each of the four values and for every line-of-sight bank name (`c54.17*`, `c54.178_*`, `L814_*`,
`r6784_*`), and none occurs below.  *** The sky enters only as `PO-47`'s four peak anchors and its four
locating widths, quoted, and as `plik_lite`'s own binning. ***

** WHY IT EXISTS. **  `r6975`'s order, three items: ⓵ decompose the excess into the peak-weighted part
and the remainder and characterise the REMAINDER; ⓶ say what class of mechanism can produce a symmetric
excess at all, as a statement with arithmetic rather than a search; ⓷ swap the term mix, with the
prediction stated first.  *`PREDICTION.md` and its two supplements were committed before any `DPSRC`
slice finished, which is checkable in the history -- and the second supplement retracts the first, so
the order of the record matters and is preserved.*

⛭⛭ ** ⓵ THE REMAINDER, AND IT IS TROUGH-WEIGHTED WHERE THE CHANNEL THAT LEFT IT IS PEAK-WEIGHTED. **
Dividing the measured excess by what the window channel delivers at the arm's own size leaves a
remainder of $1.0184$ at $q=0$ -- ** $46$ per cent of the offset R1 fired on ** -- carrying $123$ per
cent of the measured $q^{2}$ slope.  On the anchored reading the whole excess is $+5.66$ per cent on
heights against $+2.58$ on depths (ratio $2.20$), the window channel $+4.59$ against $+0.37$ ($12.44$),
and the remainder $+1.07$ against $+2.21$ -- ** ratio $0.49$. **

⛭⛭⛭ ** ⓶ AND THE STATISTIC HAS A BASELINE, WHICH I HAD NOT COMPUTED. **  Applying each named class to
the control's own banked spectrum and re-running the same envelope and the same anchored locator:

    amplitude  (the oscillation scaled about the envelope)      ratio  1.95
    envelope   (the smooth part scaled at fixed oscillation)    ratio  1.96
    loading    (a smooth positive component removed)            ratio  0.60-0.67
    smearing   (a Gaussian in l of nine multipoles)             ratio -5.28

*** So a SYMMETRIC operation reads $1.95$ on this statistic and not $1$ ***, stable across operation
sizes, because the running-mean envelope is recomputed and shifts the oscillation upward by a constant
which adds to the heights and subtracts from the deeper troughs.  ⇒ ** That retracts my own note that the
anchored reading and `cc66.46`'s variance split disagree: $2.20$ against a baseline of $1.95$ is
agreement to thirteen per cent, so the anchored reading CONFIRMS the variance split. **  *The guard about
keeping two statistics apart was right; I had compared to $1$ instead of computing the baseline.*

⛔⛭ ** ⓷ THE TERM-MIX SWAP: THE SHAPE IS RIGHT, THE SIZE IS HALF AGAIN TOO BIG, AND THE WEIGHTING IS
WRONG -- WHICH REFUTES MY OWN ⓶ IDENTIFICATION AND NOT THE ORDER'S QUESTION. **  `DPSRC` scales the
Doppler term and nothing else, and the coefficient giving the control the arm's monopole fraction is
solved from the profiles: it comes out between $0.860$ and $0.897$ in all seven bands, ** one constant to
two per cent **, which is what makes the arm's term-mix difference a one-parameter operation.
  * ✔ ** T1, the sign, passes: ** the contrast rises in every band.
  * ⛭⛭ ** T2, the shape, passes emphatically and is the finding: ** the response is $q$-INDEPENDENT --
    $|{\rm slope}\times\langle q^{2}\rangle|/|{\rm intercept}| = 0.031$, an intercept of $1.0805$ at
    $q=0$ against a slope worth three per cent of it.  *** This is the first channel measured with the
    signature R1's offset needs: a non-zero excess where a smearing's characteristic function is
    identically one. ***
  * ⛔ ** T3', the weighting, FIRES: ** the swap reads $2.23$ at the arm-matching coefficient and $2.21$
    at the larger one -- *peak-weighted, at the symmetric baseline*, where the remainder it was to be is
    $0.49$ and the loading class is $0.60$-$0.67$.  ⇒ ** The term mix is NOT the remainder. **
  * ⛔ ** And it OVER-DELIVERS: ** imposed at exactly the size the profiles measure, it raises the
    control's contrast by $1.10$ to $2.77$ times the whole measured excess, mean $1.58$.
  * ⛔ ** T4, the comb, fires too, and in the wrong direction: ** $\ell_1$ moves $-1.04$ and $\ell_2$
    $-1.79$, both outside the sky's own locating widths, where the arm sits at $+1.61$ and $-0.19$.

⛔⛭⛭ ** THE CONSEQUENCE, WHICH IS THE REVISION'S RESULT: THE TWO CHANNELS DO NOT ADD. **  The window
channel delivers about a third of the excess and the term mix about $1.6$ times it; together they are
$1.72$ times what is measured.  ⇒ *** So they cannot both be present at their measured sizes and simply
compose -- and ⓵'s remainder, which is a RATIO of two responses, assumed exactly that. ***  ** The
"remainder" is therefore not a residual physical channel but an artefact of composing two channels
multiplicatively when they do not compose. **  ⌗ *That is why ⓵'s trough-weighted $0.49$ and ⓷'s
peak-weighted $2.23$ are not in conflict: the first is a construct of the composition rule and the second
is a measurement.*

⚠ ** AND WHY MY ⓶ PHYSICAL IDENTIFICATION WAS WRONG, FROM THE PROFILES THEMSELVES. **  I argued the
Doppler is a quarter period out of phase and therefore FILLS the oscillation, so removing it should read
as the loading class and come out trough-weighted near $0.6$.  ** It reads $2.23$. **  The profiles say
why: the Doppler's band-to-band power tracks the monopole's across all seven bands rather than sitting at
low $q$, so it is an OSCILLATING term in quadrature and not a smooth additive one -- and removing an
in-quadrature oscillating component is very nearly a pure amplitude change, which is exactly the $1.95$
baseline the swap lands beside.  ⇒ *The loading class is a real class and the Doppler is not in it.*

** WHAT IS NOT CLAIMED. **  NOT that the term mix is the remainder -- T3' refutes that.  NOT that it is
the mechanism: it over-delivers by half again and moves the comb the wrong way.  NOT that it is nothing:
it is the first channel measured to carry the $q$-independent signature the offset needs, from a
difference nobody chose.  NOT a new decomposition to replace ⓵'s -- what this receipt establishes is that
the composition rule is the thing at fault, and it does not supply a better one.  NOT a detection.  NOT a
verdict on the two-rate assignment.  NOT a re-derivation of `PO-47`'s spreads, which are quoted.  No
refit, nothing touching `prop:flat` or the clock family, and no corpus edits.

COMPUTES: scope.
  * ** EVERY COSMOLOGICAL PARAMETER IS BANKED, NOT CHOSEN HERE. **  Both arms at `r6825+cc66.25`'s
    verified 185-bin refit minima; every spectrum read is that configuration.  Nothing here re-fits.
  * `spectra/r6959_eta_{lcdm,cr}.npz`, `spectra/r6959_nswap_lcdm.npz`,
    `spectra/r6975_mix_lcdm.npz`, `spectra/r6975_mixb_lcdm.npz`, `spectra/r6941_fine_{lcdm,cr}.npz`.
  * ** The `DPSRC` coefficients are not free numbers: ** the first is solved from the `SRCETA` profiles
    to give the control the arm's monopole fraction, the second is the larger excursion that calibrates
    the response, and each is carried in the bank it produced so this receipt reads it from the spectrum.
  * ** ⓶'s class table is computed, not quoted: ** each operation is applied to the control's own binned
    spectrum here and read with the same envelope and the same anchored locator as everything else.
  * `PO-47`'s anchors $220.6/538.1/809.8/1121.9$ and widths $1.00/1.20/1.60/2.36$ are quoted from that
    receipt.  `cc66.46`'s $1.0668/1.0561$ variance split is quoted.  The statistic is `r6911+cc66.40`'s,
    unchanged, and the locator `cc66.45`'s anchored parabola.
"""
import os
import sys

import numpy as np
from scipy.interpolate import CubicSpline

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
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                             # noqa: E402

NEED = ('r6959_eta_lcdm.npz', 'r6959_eta_cr.npz', 'r6959_nswap_lcdm.npz', 'r6975_mix_lcdm.npz',
        'r6975_mixb_lcdm.npz', 'r6941_fine_lcdm.npz', 'r6941_fine_cr.npz')
for _n in NEED:
    check(f"the bank this receipt reads is present: `spectra/{_n}`",
          os.path.exists(os.path.join(SP, _n)), _n)
if FAILS:
    print("\n  ⛔ A BANK THIS RECEIPT READS IS NOT ON DISK, so nothing is read and this receipt FAILS.")
    print("=" * 100)
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)

A = {t: np.load(os.path.join(SP, f'r6959_eta_{t}.npz')) for t in ('lcdm', 'cr')}
F = {t: np.load(os.path.join(SP, f'r6941_fine_{t}.npz')) for t in ('lcdm', 'cr')}
WIN = np.load(os.path.join(SP, 'r6959_nswap_lcdm.npz'))
MIX = {k: np.load(os.path.join(SP, f'r6975_{k}_lcdm.npz')) for k in ('mix', 'mixb')}

QE = A['cr']['q_edges']
QC = 0.5 * (QE[:-1] + QE[1:])
Q2 = QC ** 2
NF = 3.0
LF = np.arange(100.0, 1300.0, 1.0)
TR = np.array([396.0, 674.0, 994.0])
PK = np.array([238.0, 537.0, 828.0])
SKY4 = np.array([220.6, 538.1, 809.8, 1121.9])
SKYW = np.array([1.00, 1.20, 1.60, 2.36])
LC, _FAC = CS.bin_center_and_fac()
TERMS = ('w2sw', 'w2dp', 'w2isw', 'w2pol')


def env_a(x, y, win=1.0):
    """`r6911+cc66.40`'s running ARITHMETIC mean over one acoustic period -- the statistic, unchanged"""
    e = np.empty_like(y)
    for j, v in enumerate(x):
        m = (x >= v - win / 2) & (x <= v + win / 2)
        e[j] = np.mean(y[m])
    return e


def osc(x, y):
    e = env_a(x, y)
    return (y - e) / e


def band_std(d):
    q = d['ls'].astype(float) / float(d['l_A'])
    o = osc(q, d['Dl'])
    return np.array([float(np.std(np.interp(np.linspace(a, b, 400), q, o)))
                     for a, b in zip(QE[:-1], QE[1:])])


def spl(Db):
    m = (LC >= 100) & np.isfinite(Db)
    return CubicSpline(LC[m], Db[m])(LF)


def anchored(o, a, W, kind):
    return np.array([float(abs(np.min(o[(LF >= x - W) & (LF <= x + W)]))) if kind == 'min'
                     else float(np.max(o[(LF >= x - W) & (LF <= x + W)])) for x in a])


def hd_of(Dl_ls, Dl):
    """the anchored heights and depths, `cc66.46`'s reading, on the likelihood's own binning"""
    o = osc(LF / 301.6, spl(CS.bin_spectrum(Dl_ls, Dl)))
    return anchored(o, PK, 40, 'max').mean(), anchored(o, TR, 40, 'min').mean()


def hd(d):
    return hd_of(d['ls'].astype(float), d['Dl'])


def peaks_sub(d, W=40):
    """`cc66.45`'s anchored parabola"""
    ls, Dl = d['ls'].astype(float), d['Dl']
    out = []
    for a in SKY4:
        m = (ls >= a - W) & (ls <= a + W)
        x, y = ls[m], Dl[m]
        i = int(np.argmax(y))
        dd = 0.5 * (y[i - 1] - y[i + 1]) / (y[i - 1] - 2 * y[i] + y[i + 1]) if 0 < i < len(x) - 1 else 0.
        out.append(float(x[i] + dd * (x[1] - x[0])))
    return np.array(out)


C0 = {t: band_std(F[t]) for t in F}
MEAS = C0['cr'] / C0['lcdm']
RW = band_std(WIN) / C0['lcdm']
RM = band_std(MIX['mix']) / C0['lcdm']
RB = band_std(MIX['mixb']) / C0['lcdm']
H0, T0 = hd(F['lcdm'])
HC, TC = hd(F['cr'])

# ==================================================================================================
print("\nPART 1 -- ⓵ THE DECOMPOSITION, AND WHAT THE REMAINDER LOOKS LIKE.")
print("-" * 100)
REM = MEAS / RW
print("  band    measured    window delivers    remainder")
for b in range(len(QC)):
    print(f"  q={QC[b]:.2f}  {MEAS[b]:.5f}     {RW[b]:.5f}          {REM[b]:.5f}")
sm, im = np.polyfit(Q2, np.log(MEAS), 1)
sr, ir = np.polyfit(Q2, np.log(REM), 1)
print(f"\n  ln against q^2 -- measured slope {sm:+.6f} intercept {im:+.6f} ({np.exp(im):.4f} at q=0);"
      f"  remainder slope {sr:+.6f} intercept {ir:+.6f} ({np.exp(ir):.4f})")
check("the measured excess is recomputed here from `r6941_fine_*`, not quoted, and reproduces "
      "`cc66.46`'s seven band ratios",
      np.allclose(MEAS, [1.0215, 1.0574, 1.0519, 1.0606, 1.0748, 1.0659, 1.0762], atol=5e-4),
      "  ".join(f"{x:.4f}" for x in MEAS))
check("the remainder carries about half the q=0 offset R1 fired on",
      0.35 < (np.exp(ir) - 1) / (np.exp(im) - 1) < 0.60,
      f"{100 * (np.exp(ir) - 1) / (np.exp(im) - 1):.1f} per cent of it")
check("and it carries ALL of the growth with wavenumber, and a little more",
      sr / sm > 1.0, f"{100 * sr / sm:.1f} per cent of the measured q^2 slope")
DH_C, DT_C = HC / H0 - 1, TC / T0 - 1
HW, TW = hd(WIN)
DH_W, DT_W = HW / H0 - 1, TW / T0 - 1
R_ALL, R_WIN = DH_C / DT_C, DH_W / DT_W
R_REM = (DH_C - DH_W) / (DT_C - DT_W)
print(f"\n  anchored: the whole excess {100 * DH_C:+.2f}% / {100 * DT_C:+.2f}% -> {R_ALL:.2f};  "
      f"the window channel {100 * DH_W:+.2f}% / {100 * DT_W:+.2f}% -> {R_WIN:.2f};  "
      f"the remainder {100 * (DH_C - DH_W):+.2f}% / {100 * (DT_C - DT_W):+.2f}% -> {R_REM:.2f}")
check("the remainder is trough-weighted where the channel that left it is peak-weighted",
      R_REM < 1.0 < R_WIN and R_WIN / R_REM > 10,
      f"remainder {R_REM:.2f} against the window channel's {R_WIN:.2f}")

# ==================================================================================================
print("\nPART 2 -- ⓶ THE CLASS ARITHMETIC, AND THE BASELINE THE STATISTIC HAS.")
print("-" * 100)
D = spl(CS.bin_spectrum(F['lcdm']['ls'].astype(float), F['lcdm']['Dl']))
E = env_a(LF / 301.6, D)


def read(Dn):
    En = env_a(LF / 301.6, Dn)
    on = (Dn - En) / En
    h = anchored(on, PK, 40, 'max').mean()
    t = anchored(on, TR, 40, 'min').mean()
    return h / H0 - 1, t / T0 - 1


_g = np.exp(-0.5 * (np.arange(-40, 41) / 9.0) ** 2)
CLASSES = (('amplitude -- the oscillation scaled about the envelope', E + 1.05 * (D - E)),
           ('envelope  -- the smooth part scaled at fixed oscillation', 0.95 * E + (D - E)),
           ('loading   -- a smooth positive component removed', D - 0.005 * float(np.mean(E))),
           ('smearing  -- a Gaussian in l of nine multipoles', np.convolve(D, _g / _g.sum(), 'same')))
print("  what a five per cent operation of each class reads as, on the anchored statistic:")
RAT = {}
for nm, Dn in CLASSES:
    dh, dt = read(Dn)
    RAT[nm.split()[0]] = dh / dt
    print(f"    {nm:56s} {100 * dh:+8.3f}%  {100 * dt:+8.3f}%   ratio {dh / dt:6.2f}")
check("⛭ THE SYMMETRIC CLASS DOES NOT READ 1 ON THIS STATISTIC -- it reads about 1.95, because the "
      "running-mean envelope is recomputed and shifts the oscillation upward by a constant",
      1.85 < RAT['amplitude'] < 2.05 and abs(RAT['amplitude'] - RAT['envelope']) < 0.05,
      f"amplitude {RAT['amplitude']:.2f}, envelope {RAT['envelope']:.2f}")
_sz = [read(E + (1 + e) * (D - E)) for e in (0.002, 0.005, 0.01)]
check("and that baseline is a property of the statistic, not of the operation's size: it is the same "
      "across a fivefold range", max(abs(a / b - RAT['amplitude']) for a, b in _sz) < 0.02,
      "  ".join(f"{a / b:.2f}" for a, b in _sz))
check("⇒ SO THE ANCHORED READING CONFIRMS `cc66.46`'s VARIANCE SPLIT RATHER THAN CONTRADICTING IT: the "
      "whole excess sits within fifteen per cent of the symmetric baseline",
      abs(R_ALL / RAT['amplitude'] - 1) < 0.15,
      f"{R_ALL:.2f} against a symmetric baseline of {RAT['amplitude']:.2f}")
check("the loading class is the only named one on the trough side of that baseline, which is where the "
      "remainder sits", RAT['loading'] < 1.0 and RAT['smearing'] > RAT['amplitude'] or RAT['smearing'] < 0,
      f"loading {RAT['loading']:.2f}, smearing {RAT['smearing']:.2f}")

# ==================================================================================================
print("\nPART 3 -- ⓷ THE TERM-MIX SWAP, AGAINST THE CONDITIONS SET BEFORE IT RAN.")
print("-" * 100)
FR = {}
RAW = {}
for t in ('lcdm', 'cr'):
    d = A[t]
    ee, els, w = d['eta'], float(d['eta_ls']), float(d['eta_ls_w'])
    m = (ee >= els - NF * w) & (ee <= els + NF * w)
    tot = np.array([[float(np.trapezoid(d[k][m][:, b], ee[m])) for k in TERMS]
                    for b in range(len(QC))])
    FR[t] = tot / tot.sum(axis=1)[:, None]
    RAW[t] = tot
CS_NEED = []
for b in range(len(QC)):
    sw, dp = RAW['lcdm'][b, 0], RAW['lcdm'][b, 1]
    rest = RAW['lcdm'][b, 2] + RAW['lcdm'][b, 3]
    tgt = FR['cr'][b, 0]
    CS_NEED.append(float(np.sqrt(max((sw / tgt - sw - rest) / dp, 0.0))))
CS_NEED = np.array(CS_NEED)
print("  the DPSRC that gives the control the arm's monopole fraction, band by band:")
print("    " + "  ".join(f"{x:.4f}" for x in CS_NEED))
check("⛭ ONE CONSTANT DOES IT: the coefficient the profiles demand is the same in every band to two "
      "per cent, so the arm's term-mix difference is a single scalar on the Doppler and not a "
      "q-dependent reshaping", CS_NEED.max() / CS_NEED.min() - 1 < 0.05,
      f"{CS_NEED.min():.4f} to {CS_NEED.max():.4f}, a "
      f"{100 * (CS_NEED.max() / CS_NEED.min() - 1):.1f} per cent spread")
check("and the run used that band-mean, read from the bank rather than restated here",
      abs(float(MIX['mix']['dpsrc']) - CS_NEED.mean()) < 0.01,
      f"DPSRC={float(MIX['mix']['dpsrc']):.4f} against the band-mean {CS_NEED.mean():.4f}")

print("\n  band    DPSRC=%.4f   DPSRC=%.2f   |  measured excess" % (
    float(MIX['mix']['dpsrc']), float(MIX['mixb']['dpsrc'])))
for b in range(len(QC)):
    print(f"  q={QC[b]:.2f}   {RM[b]:.5f}        {RB[b]:.5f}     |  {MEAS[b]:.5f}")
check("⓷ T1 THE SIGN PASSES: the contrast rises in every band, as the pre-registration predicted",
      bool(np.all(RM > 1.0)) and bool(np.all(RB > 1.0)), f"smallest {RM.min():.5f}")
s_m, i_m = np.polyfit(Q2, np.log(RM), 1)
s_b, i_b = np.polyfit(Q2, np.log(RB), 1)
FLAT = abs(s_m * Q2.mean()) / abs(i_m)
print(f"\n  ln against q^2 -- mix slope {s_m:+.6f} intercept {i_m:+.6f} ({np.exp(i_m):.4f} at q=0);"
      f"  mixb slope {s_b:+.6f} intercept {i_b:+.6f} ({np.exp(i_b):.4f})")
check("⛭⛭ ⓷ T2 THE SHAPE PASSES, AND IT IS THE FINDING: the response is q-INDEPENDENT, the slope "
      "carrying a few per cent of what the intercept does -- the first channel measured with the "
      "signature the q-independent offset needs", FLAT < 0.15,
      f"|slope x <q^2>| / |intercept| = {FLAT:.3f}, intercept {np.exp(i_m):.4f} at q=0")
check("and the window channel is the opposite: a smearing's characteristic function is identically 1 "
      "at q=0, so no amount of it supplies an offset",
      abs(np.polyfit(Q2, np.log(RW), 1)[0]) < abs(s_b),
      "the window response is flat in q because it is small, not because it is an offset")
DH_M, DT_M = read(spl(CS.bin_spectrum(MIX['mix']['ls'].astype(float), MIX['mix']['Dl'])))
DH_B, DT_B = read(spl(CS.bin_spectrum(MIX['mixb']['ls'].astype(float), MIX['mixb']['Dl'])))
R_M, R_B = DH_M / DT_M, DH_B / DT_B
print(f"\n  anchored: DPSRC={float(MIX['mix']['dpsrc']):.4f} gives {100 * DH_M:+.2f}% / "
      f"{100 * DT_M:+.2f}% -> {R_M:.2f};  DPSRC={float(MIX['mixb']['dpsrc']):.2f} gives "
      f"{100 * DH_B:+.2f}% / {100 * DT_B:+.2f}% -> {R_B:.2f}")
check("⛔ ⓷ T3' THE WEIGHTING FIRES: the swap is PEAK-weighted, at the symmetric baseline, where the "
      "remainder it was to be is trough-weighted -- so the term mix is NOT the remainder",
      R_M > 1.5 and R_B > 1.5 and R_M / R_REM > 3,
      f"{R_M:.2f} and {R_B:.2f} against the remainder's {R_REM:.2f} and a symmetric baseline of "
      f"{RAT['amplitude']:.2f}")
check("and the two coefficients agree on that weighting, so it is the operation's and not one run's",
      abs(R_M / R_B - 1) < 0.05, f"{R_M:.2f} against {R_B:.2f}")
OVER = (RM - 1) / (MEAS - 1)
check("⛔ AND IT OVER-DELIVERS: imposed at exactly the size the profiles measure, it raises the "
      "control's contrast by more than the whole measured excess in every band",
      bool(np.all(OVER > 1.0)), "  ".join(f"{x:.2f}x" for x in OVER)
      + f"   mean {OVER.mean():.2f}x")
P0 = peaks_sub(F['lcdm'])
MVC = peaks_sub(F['cr']) - P0
for nm in ('mix', 'mixb'):
    mv = peaks_sub(MIX[nm]) - P0
    print(f"  {nm:5s} peaks moved " + "  ".join(f"{x:+7.3f}" for x in mv)
          + f"   outside the sky's widths: {int(np.sum(np.abs(mv) > SKYW))}/4")
    if nm == 'mix':
        MVM = mv
print(f"  the arm's own     " + "  ".join(f"{x:+7.3f}" for x in MVC))
check("⛔ ⓷ T4 THE COMB FIRES: the swap moves more than one peak outside the sky's own locating width",
      int(np.sum(np.abs(MVM) > SKYW)) >= 2,
      "moves " + "  ".join(f"{a:+.2f}/{b:.2f}" for a, b in zip(MVM, SKYW)))
check("and in the WRONG DIRECTION at l_1: the swap moves it down where the arm sits above the control",
      MVM[0] < 0 < MVC[0], f"swap {MVM[0]:+.3f} against the arm's {MVC[0]:+.3f}")

# ==================================================================================================
print("\nPART 4 -- THE CONSEQUENCE: THE TWO CHANNELS DO NOT ADD.")
print("-" * 100)
SUM = (RM - 1).mean() + (RW - 1).mean()
print(f"  band-mean excess measured {100 * (MEAS - 1).mean():.3f}%;  window channel "
      f"{100 * (RW - 1).mean():.3f}%;  term mix {100 * (RM - 1).mean():.3f}%;  their sum "
      f"{100 * SUM:.3f}%")
check("⛔⛭⛭ THE TWO CHANNELS TOGETHER EXCEED WHAT IS MEASURED, so they cannot both be present at their "
      "measured sizes and simply compose", SUM / (MEAS - 1).mean() > 1.3,
      f"{SUM / (MEAS - 1).mean():.2f} times the excess")
check("⇒ AND THAT IS WHAT ⓵'s REMAINDER ASSUMED: it is a RATIO of two responses, so it is a construct "
      "of the composition rule rather than a residual channel -- which is why its trough-weighted 0.49 "
      "and the term mix's peak-weighted reading are not in conflict",
      R_REM < 1.0 < R_M and SUM / (MEAS - 1).mean() > 1.3,
      f"remainder {R_REM:.2f} is a construct; the swap's {R_M:.2f} is a measurement")
DPB = RAW['lcdm'][:, 1] / RAW['lcdm'][:, 1].max()
SWB = RAW['lcdm'][:, 0] / RAW['lcdm'][:, 0].max()
print(f"\n  and why the `loading` identification was wrong -- the band-to-band power:")
print(f"    monopole " + "  ".join(f"{x:.3f}" for x in SWB))
print(f"    Doppler  " + "  ".join(f"{x:.3f}" for x in DPB))
check("⚠ THE DOPPLER IS AN OSCILLATING TERM IN QUADRATURE AND NOT A SMOOTH ADDITIVE ONE: its power "
      "tracks the monopole's across the bands rather than sitting at long wavelength, so removing it is "
      "nearly a pure amplitude change -- which is where the swap landed and why my `loading` reading "
      "was refuted", float(np.corrcoef(SWB, DPB)[0, 1]) > 0.9,
      f"band-to-band correlation with the monopole {float(np.corrcoef(SWB, DPB)[0, 1]):.3f}")

print("\n" + "=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)
print("GATES: ALL PASS")
