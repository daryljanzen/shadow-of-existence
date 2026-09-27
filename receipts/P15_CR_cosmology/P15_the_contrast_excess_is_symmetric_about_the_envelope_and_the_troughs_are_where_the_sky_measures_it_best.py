#!/usr/bin/env python3
r"""P15 sec:refit-bound -- ** THE CONTRAST EXCESS IS SYMMETRIC ABOUT THE ENVELOPE, AND THE TROUGHS ARE
WHERE THE SKY MEASURES IT BEST -- WHICH IS NOT THE REASON THE ORDER GAVE. **

** PATH PROVENANCE, IN THE HEADER, AT 66's REQUEST AFTER `cc66.45`. **  *** Every model number below is
the HIERARCHY path: *** the reported spectra `cc66_r185_verify_{lcdm,cr}`, the `LSTEP=1` fine references
`r6941_fine_{lcdm,cr}`, and the `VISLEAF` family `r6929_scan_cr` / `r6941_fine_cr_visleaf`.
`sec:refit-bound`'s quartet $222/538/818/1134$ is the LINE-OF-SIGHT path's and is not read here at all
-- searched for by grepping this file for each of the four values and for every line-of-sight bank name
(`c54.17*`, `c54.178_*`, `L814_*`, `r6784_*`), and none of them occurs in the code below.  *** The sky side is `plik_lite` TT through the likelihood's OWN binning *** --
`chi2_of_spectrum.bin_spectrum` -- and the models are binned identically before any comparison, so every
sky-facing number is matched-procedure by construction and not by assertion.

** WHY IT EXISTS. **  `r6955`'s order: four things have been eliminated -- the contrast is not in the
source at any grain, not the cross term, not absorbable by the clock assignment, and not the comb
residual -- so what is left is the $\chi^{2}$, which is trough-dominated in the whitened residual.  The
order's reading, stated as 66's own: *the trough DEPTHS mix the two clocks in a way $\theta_D/\theta_*$
does not, because a depth needs the diffusion scale in MULTIPOLES and so needs the projection distance,
which rides the other clock.*  ⓶ᵃ locate the excess before assuming it; ⓶ᵇ then the clock sensitivity of
whichever carries it, against $\mathrm d(\theta_D/\theta_*)/\mathrm df$; ⓶ᶜ and the sky's own spread on
it, the way `PO-47` did for the fourth peak.

⛭⛭ ** ⓶ᵃ THE EXCESS IS SYMMETRIC ABOUT THE ENVELOPE, SO IT IS NEITHER TROUGH-DOMINATED NOR
PEAK-DOMINATED. **  Splitting the band variance of the envelope-normalised oscillation at its own zero
-- which is a decomposition, the two parts adding to the whole -- the arm/control ratio is $1.0668$ on
the positive side and $1.0561$ on the negative.  Read instead at the literal extrema, the arm's
excursion exceeds the control's by $5.7$ per cent at the maxima and $5.3$ at the minima.  ⇒ *** The
contrast is an AMPLITUDE excess about the envelope, carried equally by peak heights and trough depths. ***
⌗ *So $\Delta$'s trough dominance is a statement about the whitened residual and does NOT transfer to
the contrast's own decomposition -- which the order explicitly declined to assume, and the answer is that
they do not agree.*  ⚠ *And the order's stop condition does not fire either: the excess is not in the
peaks, so the row is not pushed back onto the driving.*

⛔ ** ⓶ᵇ THE DEPTHS ARE THE MORE CLOCK-SENSITIVE OF THE TWO -- BUT $\theta_D/\theta_*$ IS MORE SENSITIVE
THAN EITHER, WHICH REFUTES THE ORDER'S BRANCH. **  Across the `VISLEAF` family the mean trough depth
moves $-2.58$ per cent and the mean peak height only $-0.77$, so the depths are $3.4\times$ the more
responsive -- *that half of the reading holds.*  But $\theta_D/\theta_* = r_D/r_s$ moves $-4.08$ per
cent over the same family, because $r_D$ is itself `Jac`-weighted under `LEAFSCALES` and the $\tau$
re-weighting moves it directly.  ⇒ *** The paper's discriminant of principle is not the insensitive one:
it is the MOST sensitive of the three, and by the order's own rule -- both move together -- the depths
are not a new handle on the clock. ***

⛭⛭⛭ ** ⓶ᶜ AND YET THE TROUGHS ARE WHERE THE ASSIGNMENT BECOMES OBSERVABLE, FOR A REASON NEITHER OF US
NAMED: THE SKY MEASURES DEPTHS TWICE AS WELL AS HEIGHTS. **  On the matched binned statistic, with
`COV_TT` propagated by Monte Carlo through the identical anchored locator, the sky's own spread is
$0.0059$ on the trough depth and $0.0114$ on the peak height.  The arm-minus-control excess is the same
size in both -- $+0.0106$ and $+0.0103$ -- so in the sky's own units it reads

    trough depths :  arm - control = +1.81 sigma      control - sky = -0.05 sigma
    peak heights  :  arm - control = +0.91 sigma      control - sky = -0.59 sigma

*** The control lands on the sky's trough depths to a twentieth of a sigma and the arm sits $1.76\sigma$
above the sky.  This is the first statistic in this sector whose residual is NOT shared with the
control *** -- against the fourth peak, where the arm-minus-control displacement was $0.83\sigma$ and
both models sat high of the sky.  ⇒ ** So the order's conclusion stands and its argument does not: the
trough depths are the sharpest CR-specific observable this campaign has measured, because of how well
the SKY measures them rather than because of how they mix the clocks. **

⚑ ** THE GUARDS. **  *The window bias the order warned about does not exist for this statistic:* the
anchored depth is identical to five decimals over $W=20\ldots70$, because it reads a VALUE at a located
extremum rather than the LOCATION of one, and the value's window dependence enters only through which
sample is the minimum.  ⚠ *But `PO-47`'s trap reproduces exactly:* a free extremum search under noise
returns a spread of $0.0369$ against the anchored $0.0059$, six times worse, because the search latches
onto noise minima -- **which is why the anchoring is necessary and not a convenience**, and it is gated
below.  ⌗ *The one real systematic is the envelope window's abscissa: the sky's depth runs
$0.2790\to0.2830$ as the $\ell_A$ that sets it goes $298\to305$, about $0.3\sigma$, and it is reported
rather than minimised.*

** WHAT IS NOT CLAIMED. **  NOT that the $1.8\sigma$ is a detection; it is $1.8$ of the sky's own spread
on one statistic, and the same differencing at the fourth peak gave $0.83$.  NOT a mechanism for the
amplitude excess -- this receipt locates it and measures how well the sky sees it.  NOT a re-derivation
of `PO-47`'s peak-position spreads, which are cited and not touched.  NOT that the depths discriminate
the CLOCK: they do not, and the order's branch on that is refuted here.  NOT a verdict on the two-rate
assignment, which is the row's question.  No refit, nothing touching `prop:flat` or the clock family, and
no corpus edits -- the paper-side consequences are routed to 66.

COMPUTES: scope.
  * ** EVERY COSMOLOGICAL PARAMETER IS BANKED, NOT CHOSEN HERE. **  Both arms at `r6825+cc66.25`'s
    verified 185-bin refit minima; the fine references are the same configuration at `LSTEP=1 LMAXL=2000`.
    Nothing here re-fits and nothing here moves.
  * `spectra/r6941_fine_{lcdm,cr}.npz`, `r6941_fine_cr_visleaf.npz`, `r6929_scan_cr.npz`,
    `r6929_geometry.npz`, `cc66_r185_verify_{lcdm,cr}.npz`.
  * The sky is `plik_lite` TT's `X_data` and `COV_TT` through
    `computations/planck_tt_likelihood/chi2_of_spectrum.py`; `PO-47`'s fourth-peak spread $2.36$ and its
    $0.83\sigma$ are quoted from that receipt and not recomputed.
  * The statistic is `r6911+cc66.40`'s envelope-normalised oscillation with its running arithmetic mean
    over one acoustic period, unchanged, and the anchored-extremum reading is `PO-47`'s applied to
    values instead of locations.
"""
import os
import sys

import numpy as np
from scipy.interpolate import CubicSpline
from scipy.signal import argrelextrema

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

NEED = ('r6941_fine_lcdm.npz', 'r6941_fine_cr.npz', 'r6941_fine_cr_visleaf.npz',
        'r6929_scan_cr.npz', 'r6929_geometry.npz')
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

F = {t: np.load(os.path.join(SP, f'r6941_fine_{t}.npz')) for t in ('lcdm', 'cr')}
V = np.load(os.path.join(SP, 'r6941_fine_cr_visleaf.npz'))
S = np.load(os.path.join(SP, 'r6929_scan_cr.npz'))
GE = np.load(os.path.join(SP, 'r6929_geometry.npz'))

LC, FAC = CS.bin_center_and_fac()
X, COV = CS.X_DATA, CS.COV_TT
LF = np.arange(100.0, 1300.0, 1.0)
LA_SKY = 301.6                       # the sky's own acoustic scale; it only sets the envelope's abscissa
TR = np.array([396.0, 674.0, 994.0])  # the trough anchors -- the CONTROL's own minima, used everywhere
PK = np.array([238.0, 537.0, 828.0])  # and its peak anchors
WS = (20, 30, 40, 55, 70)
W0 = 40
PO47_SIG4, PO47_AC = 2.36, 0.83      # PO-47's fourth peak: the sky's spread, and arm-minus-control


def env_a(x, y, win=1.0):
    """`r6911+cc66.40`'s running ARITHMETIC mean over one acoustic period -- the statistic, unchanged"""
    e = np.empty_like(y)
    for j, v in enumerate(x):
        m = (x >= v - win / 2) & (x <= v + win / 2)
        e[j] = np.mean(y[m])
    return e


def osc(x, y, win=1.0):
    e = env_a(x, y, win)
    return (y - e) / e


def spl(Db):
    """`PO-47`'s spline of the BINNED spectrum onto every multipole -- sky and models alike"""
    m = (LC >= 100) & np.isfinite(Db)
    return CubicSpline(LC[m], Db[m])(LF)


def binned_osc(Db, lA):
    D = spl(Db)
    return osc(LF / lA, D)


def anchored(o, anch, W, kind):
    """the value at the anchored extremum -- `PO-47`'s anchoring applied to a DEPTH instead of a place"""
    out = []
    for a in anch:
        k = (LF >= a - W) & (LF <= a + W)
        out.append(float(abs(np.min(o[k]))) if kind == 'min' else float(np.max(o[k])))
    return np.array(out)


def free(o, kind, n=3, order=20):
    idx = (argrelextrema(o, np.less, order=order)[0] if kind == 'min'
           else argrelextrema(o, np.greater, order=order)[0])[:n]
    return np.array([abs(float(o[i])) for i in idx])


ED = np.arange(0.85, 5.76, 0.7)
CTR = np.array([(a + b) / 2 for a, b in zip(ED[:-1], ED[1:])])

# ===================================================================================================
print("\nPART 1 -- ⓶ᵃ WHERE THE EXCESS IS: THE BAND VARIANCE SPLIT AT ITS OWN ZERO, AND THE EXTREMA.")
print("-" * 100)
Q = {t: F[t]['ls'].astype(float) / float(F[t]['l_A']) for t in F}
O = {t: osc(Q[t], F[t]['Dl']) for t in F}


def three(Qa, Oa, a, b, n=400):
    x = np.linspace(a, b, n)
    o = np.interp(x, Qa, Oa)
    return (float(np.mean(o ** 2)), float(np.mean(np.where(o > 0, o ** 2, 0.0))),
            float(np.mean(np.where(o < 0, o ** 2, 0.0))))


TOT, PKS, TRS = [], [], []
print(f"    {'q band':>8} {'total':>9} {'peak side':>10} {'trough side':>12}")
for a, b in zip(ED[:-1], ED[1:]):
    va, vpa, vma = three(Q['cr'], O['cr'], a, b)
    vc, vpc, vmc = three(Q['lcdm'], O['lcdm'], a, b)
    TOT.append(np.sqrt(va / vc)); PKS.append(np.sqrt(vpa / vpc)); TRS.append(np.sqrt(vma / vmc))
    print(f"    {(a+b)/2:8.2f} {TOT[-1]:9.4f} {PKS[-1]:10.4f} {TRS[-1]:12.4f}")
TOT, PKS, TRS = map(np.array, (TOT, PKS, TRS))
print(f"    {'mean':>8} {TOT.mean():9.4f} {PKS.mean():10.4f} {TRS.mean():12.4f}")
check("the split is a DECOMPOSITION and not two statistics: the positive and negative parts of the "
      "band variance add to the whole, band by band",
      max(abs(three(Q['cr'], O['cr'], a, b)[0]
              - three(Q['cr'], O['cr'], a, b)[1] - three(Q['cr'], O['cr'], a, b)[2])
          for a, b in zip(ED[:-1], ED[1:])) < 1e-15,
      "var = var+ + var- to machine precision in every band")
EX = {}
for t in ('lcdm', 'cr'):
    mx = argrelextrema(O[t], np.greater, order=20)[0][:6]
    mn = argrelextrema(O[t], np.less, order=20)[0][:6]
    EX[t] = (np.array([float(O[t][i]) for i in mx]), np.array([abs(float(O[t][i])) for i in mn]))
r_max = float(np.mean(EX['cr'][0] / EX['lcdm'][0]))
r_min = float(np.mean(EX['cr'][1] / EX['lcdm'][1]))
print(f"    at the literal extrema, arm/control: maxima {r_max:.4f}, minima {r_min:.4f} "
      f"(six of each, fine grid)")
check("⛭⛭ ** THE EXCESS IS SYMMETRIC ABOUT THE ENVELOPE. **  The two sides of the decomposition carry "
      "it within about one per cent of each other, and at the literal extrema the arm exceeds the "
      "control by 5.7 per cent at the maxima against 5.3 at the minima",
      abs(PKS.mean() - TRS.mean()) < 0.02 and abs(r_max - r_min) < 0.01,
      f"band split {PKS.mean():.4f} / {TRS.mean():.4f}; extrema {r_max:.4f} / {r_min:.4f}")
check("⇒ so it is an AMPLITUDE excess and neither trough- nor peak-dominated: Delta's trough dominance "
      "is a statement about the WHITENED residual and does not transfer to the contrast's own "
      "decomposition", TRS.mean() / PKS.mean() < 1.02 and TRS.mean() / PKS.mean() > 0.98,
      f"trough side / peak side = {TRS.mean()/PKS.mean():.4f}")
check("⚠ and the order's STOP condition does not fire -- the excess is not in the peaks either, so the "
      "row is not pushed back onto the driving", PKS.mean() / TRS.mean() < 1.05,
      f"peak side exceeds the trough side by only {100*(PKS.mean()/TRS.mean()-1):.1f} per cent")

# ===================================================================================================
print("\nPART 2 -- ⓶ᵇ THE CLOCK SENSITIVITY: THE DEPTHS, THE HEIGHTS, AND theta_D/theta_*.")
print("-" * 100)
FS = [0.0, 0.1, 0.25, 0.5, 0.75, 1.0]


def exc_of(ls, Dl, lA, order=3, n=5):
    o = osc(ls / lA, Dl)
    mx = argrelextrema(o, np.greater, order=order)[0][:n]
    mn = argrelextrema(o, np.less, order=order)[0][:n]
    return (float(np.mean([o[i] for i in mx])), float(np.mean([abs(o[i]) for i in mn])))


print(f"    {'f':>5} {'mean height':>12} {'mean depth':>11} {'theta_D/theta_*':>16}")
H, D, R = [], [], []
for f in FS:
    t = f'{f:g}'.replace('.', '')
    h, d = exc_of(S[f'ls__comb_cr_f{t}'].astype(float), S[f'Dl__comb_cr_f{t}'],
                  float(S[f'l_A__comb_cr_f{t}']))
    i = int(np.argmin(np.abs(GE['f__cr'] - f)))
    r = float(GE['rD__cr'][i] / GE['R_S__cr'][i])
    H.append(h); D.append(d); R.append(r)
    print(f"    {f:5.2f} {h:12.5f} {d:11.5f} {r:16.6f}")
dH, dD, dR = H[-1] / H[0] - 1, D[-1] / D[0] - 1, R[-1] / R[0] - 1
print(f"    over the family: height {100*dH:+.3f}%, depth {100*dD:+.3f}%, "
      f"theta_D/theta_* {100*dR:+.3f}%")
check("the depths ARE the more clock-responsive of the two observables, by a factor of three -- which "
      "is the half of the order's reading that holds",
      abs(dD) > 3 * abs(dH), f"depth {100*dD:+.2f}% against height {100*dH:+.2f}%, a factor "
      f"{abs(dD/dH):.1f}")
check("⛔ ** BUT theta_D/theta_* MOVES MORE THAN EITHER, so the paper's discriminant of principle is "
      "the MOST sensitive of the three and not the insensitive one. **  r_D is itself Jac-weighted "
      "under `LEAFSCALES`, so the tau re-weighting moves it directly",
      abs(dR) > abs(dD) > 0, f"{100*dR:+.2f}% against the depths' {100*dD:+.2f}%, a factor "
      f"{abs(dR/dD):.1f}")
check("⇒ by the order's own rule -- both move together -- the depths are NOT a new handle on the clock, "
      "and that branch of the reading is refuted",
      np.sign(dR) == np.sign(dD) and abs(dR / dD) < 3,
      "same sign, within a factor of two of each other")
_hf, _df = exc_of(F['cr']['ls'].astype(float), F['cr']['Dl'], float(F['cr']['l_A']), order=20)
_hf1, _df1 = exc_of(V['ls__comb_f1'].astype(float), V['Dl__comb_f1'], float(V['l_A__comb_f1']),
                    order=20)
check("⌗ and the endpoints reproduce on the LSTEP=1 grid, so the family's response is the spectra's and "
      "not the grid's", abs((_df1 / _df - 1) - dD) < 0.01,
      f"fine {100*(_df1/_df-1):+.2f}% against coarse {100*dD:+.2f}%")

# ===================================================================================================
print("\nPART 3 -- ⓶ᶜ THE SKY'S OWN SPREAD, ON THE MATCHED BINNED STATISTIC.")
print("-" * 100)
BD = {t: CS.bin_spectrum(F[t]['ls'].astype(float), F[t]['Dl']) * FAC for t in F}
check("the models are binned by the LIKELIHOOD'S OWN binning before anything is compared, so the "
      "comparison is matched-procedure by construction",
      all(int(np.isfinite(BD[t]).sum()) == 185 for t in BD),
      f"{int(np.isfinite(BD['cr']).sum())} covered bins on each arm")
OC, OA, OS = (binned_osc(BD['lcdm'], float(F['lcdm']['l_A'])),
              binned_osc(BD['cr'], float(F['cr']['l_A'])), binned_osc(X * FAC, LA_SKY))
dc, da, ds = (anchored(OC, TR, W0, 'min').mean(), anchored(OA, TR, W0, 'min').mean(),
              anchored(OS, TR, W0, 'min').mean())
hc, ha, hs = (anchored(OC, PK, W0, 'max').mean(), anchored(OA, PK, W0, 'max').mean(),
              anchored(OS, PK, W0, 'max').mean())
print(f"    depths : control {dc:.5f}  arm {da:.5f}  sky {ds:.5f}   arm-control {da-dc:+.5f}")
print(f"    heights: control {hc:.5f}  arm {ha:.5f}  sky {hs:.5f}   arm-control {ha-hc:+.5f}")
L = np.linalg.cholesky(COV + 1e-30 * np.eye(len(COV)))
SIG = {}
for seed in (6955, 424242):
    rng = np.random.default_rng(seed)
    dv, hv = [], []
    for _ in range(600):
        o = binned_osc((X + L @ rng.normal(size=len(X))) * FAC, LA_SKY)
        dv.append(anchored(o, TR, W0, 'min').mean())
        hv.append(anchored(o, PK, W0, 'max').mean())
    SIG[seed] = (float(np.std(dv)), float(np.std(hv)))
    print(f"    seed {seed}: the sky's spread -- depth {SIG[seed][0]:.5f}, height {SIG[seed][1]:.5f}")
sd, sh = SIG[6955]
check("the spread does not depend on the seed, which is what makes it a measurement",
      abs(SIG[6955][0] - SIG[424242][0]) < 0.0005 and abs(SIG[6955][1] - SIG[424242][1]) < 0.001,
      f"depth {SIG[6955][0]:.5f} against {SIG[424242][0]:.5f}")
check("⛭⛭⛭ ** THE SKY MEASURES TROUGH DEPTHS TWICE AS WELL AS PEAK HEIGHTS. **  Same data, same "
      "binning, same anchored locator -- and the propagated spread is half the size on the depths",
      sh / sd > 1.7, f"height {sh:.5f} against depth {sd:.5f}, a factor {sh/sd:.2f}")
print(f"    ⇒ in the sky's own units:  depths  arm-control {(da-dc)/sd:+.2f} sigma, "
      f"control-sky {(dc-ds)/sd:+.2f} sigma, arm-sky {(da-ds)/sd:+.2f} sigma")
print(f"                               heights arm-control {(ha-hc)/sh:+.2f} sigma, "
      f"control-sky {(hc-hs)/sh:+.2f} sigma, arm-sky {(ha-hs)/sh:+.2f} sigma")
check("⇒ *** SO THE SAME EXCESS READS 1.8 SIGMA IN THE DEPTHS AND 0.9 IN THE HEIGHTS -- the order's "
      "conclusion stands and its argument does not: the troughs are where the assignment becomes "
      "observable because of how well the SKY measures them, not because of how they mix the clocks ***",
      (da - dc) / sd > 1.5 and (ha - hc) / sh < 1.1
      and abs((da - dc) - (ha - hc)) < 0.15 * (da - dc),
      f"{(da-dc)/sd:+.2f} sigma against {(ha-hc)/sh:+.2f} sigma, on excesses of {da-dc:+.5f} and "
      f"{ha-hc:+.5f}")
check("⛭ ** AND THE CONTROL LANDS ON THE SKY'S TROUGH DEPTHS TO A TWENTIETH OF A SIGMA, so this is the "
      "first statistic in this sector whose residual is NOT shared with the control ** -- against the "
      f"fourth peak, where arm-minus-control was {PO47_AC} sigma and both models sat high of the sky",
      abs((dc - ds) / sd) < 0.2 and (da - ds) / sd > 1.5,
      f"control-sky {(dc-ds)/sd:+.2f} sigma, arm-sky {(da-ds)/sd:+.2f} sigma")

# ===================================================================================================
print("\nPART 4 -- THE GUARDS THE ORDER ASKED FOR: THE WINDOW, THE FREE SEARCH, AND THE ABSCISSA.")
print("-" * 100)
SW = {W: (anchored(OC, TR, W, 'min').mean(), anchored(OA, TR, W, 'min').mean(),
          anchored(OS, TR, W, 'min').mean()) for W in WS}
for W in WS:
    print(f"    W={W:3d}  control {SW[W][0]:.5f}  arm {SW[W][1]:.5f}  arm-control {SW[W][1]-SW[W][0]:+.5f}"
          f"  sky {SW[W][2]:.5f}")
_sp = max(SW[W][1] - SW[W][0] for W in WS) - min(SW[W][1] - SW[W][0] for W in WS)
check("⚑ ** THE WINDOW BIAS THE ORDER WARNED ABOUT DOES NOT EXIST FOR THIS STATISTIC. **  The anchored "
      "depth is identical over W = 20 to 70 on the sky and on both arms, because it reads a VALUE at a "
      "located extremum and not the LOCATION of one -- where `cc66.45`'s parabola apex drifted six "
      "multipoles at l_4", _sp < 1e-6,
      f"the arm-minus-control difference varies by {_sp:.2e} over the sweep")
rng = np.random.default_rng(6955)
fv = []
for _ in range(300):
    o = binned_osc((X + L @ rng.normal(size=len(X))) * FAC, LA_SKY)
    v = free(o, 'min')
    if len(v) == 3:
        fv.append(float(v.mean()))
check("⚠ ** BUT `PO-47`'s TRAP REPRODUCES EXACTLY, on depths instead of positions: ** a FREE extremum "
      "search under noise returns six times the spread, because it latches onto noise minima -- which "
      "is why the anchoring is necessary and not a convenience",
      float(np.std(fv)) > 4 * sd,
      f"free search {float(np.std(fv)):.5f} against anchored {sd:.5f}, a factor "
      f"{float(np.std(fv))/sd:.1f}")
_ab = {v: anchored(binned_osc(X * FAC, v), TR, W0, 'min').mean() for v in (298.0, 301.6, 305.0)}
print("    the abscissa systematic: the sky's depth against the l_A that sets the envelope -- "
      + ", ".join(f"{v:.0f}: {_ab[v]:.4f}" for v in _ab))
check("⌗ and the one real systematic is reported rather than minimised: the envelope's abscissa moves "
      "the sky's depth by about a third of a sigma across the admissible l_A",
      (max(_ab.values()) - min(_ab.values())) < 0.5 * sd * 2,
      f"{max(_ab.values())-min(_ab.values()):.4f} against the sky's spread {sd:.5f}, "
      f"{(max(_ab.values())-min(_ab.values()))/sd:.2f} sigma")

# ===================================================================================================
print("\n" + "=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    sys.exit(1)
print("GATES: ALL PASS.")
print(f"""
  ⛭⛭ ⓶ᵃ THE EXCESS IS SYMMETRIC ABOUT THE ENVELOPE: the band-variance split gives {PKS.mean():.4f} on
  the peak side against {TRS.mean():.4f} on the trough side, and at the literal extrema the arm exceeds
  the control by {100*(r_max-1):.1f} per cent at the maxima against {100*(r_min-1):.1f} at the minima.
  So it is an AMPLITUDE excess; Delta's trough dominance does not transfer to the contrast's own
  decomposition, and the order's stop condition does not fire either.

  ⛔ ⓶ᵇ THE DEPTHS ARE THREE TIMES THE MORE CLOCK-RESPONSIVE ({100*dD:+.2f} per cent against
  {100*dH:+.2f} across the VISLEAF family) -- but theta_D/theta_* moves {100*dR:+.2f} per cent, MORE
  than either, because r_D is itself Jac-weighted under LEAFSCALES.  The paper's discriminant of
  principle is the most sensitive of the three and not the insensitive one, so by the order's own rule
  the depths are not a new handle on the clock.

  ⛭⛭⛭ ⓶ᶜ AND YET THE TROUGHS ARE WHERE THE ASSIGNMENT BECOMES OBSERVABLE, for a reason neither seat
  named: THE SKY MEASURES DEPTHS TWICE AS WELL AS HEIGHTS ({sd:.5f} against {sh:.5f} propagated from
  COV_TT through the identical anchored locator).  The same excess -- {da-dc:+.5f} in the depths,
  {ha-hc:+.5f} in the heights -- therefore reads {(da-dc)/sd:+.2f} sigma against {(ha-hc)/sh:+.2f}.
  And the control lands on the sky's depths at {(dc-ds)/sd:+.2f} sigma while the arm sits
  {(da-ds)/sd:+.2f} above: the first statistic in this sector whose residual is NOT the control's.

  ⚑ THE GUARDS: the anchored depth has NO window bias (identical over W = 20..70, because it reads a
  value and not a location), the free search reproduces PO-47's trap at six times the spread, and the
  envelope's abscissa is worth about a third of a sigma and is reported.

  NOT CLAIMED: that {(da-dc)/sd:.1f} sigma is a detection; a mechanism for the amplitude excess; a
  re-derivation of PO-47's spreads; that the depths discriminate the CLOCK, which they do not; a verdict
  on the two-rate assignment.  No refit, nothing touching prop:flat, and no corpus edits.
""")
sys.exit(0)
