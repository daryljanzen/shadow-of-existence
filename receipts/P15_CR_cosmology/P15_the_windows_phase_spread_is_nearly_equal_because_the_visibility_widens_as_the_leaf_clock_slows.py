#!/usr/bin/env python3
r"""P15 sec:refit-bound -- ** THE NORMALISATION ACROSS THE VISIBILITY IS A REAL CHANNEL CARRYING ABOUT A
THIRD OF THE CONTRAST EXCESS, AND IT IS PEAK-WEIGHTED WHERE THE EXCESS IS SYMMETRIC -- SO IT IS THE FIRST
PARTIAL MECHANISM IN THIS SECTOR AND STILL NOT THE WHOLE ONE. **

** PATH PROVENANCE, IN THE HEADER, ON THE STANDING REQUIREMENT. **  *** Every model number below is the
HIERARCHY path *** -- the `SRCETA` profiles `r6959_eta_{lcdm,cr}`, the six tapered controls
`r6959_{swap,big,swapall,bigall,nswap,nbig}_lcdm`, and the `LSTEP=1` baselines `r6941_fine_{lcdm,cr}`.
That is not a preference but the only possibility: `_project`, where `SRCETA` and `SRCTAPER` live, is
called from `hier_run` and nowhere else, so the line-of-sight path cannot reach either knob.
`sec:refit-bound`'s quartet $222/538/818/1134$ is the LINE-OF-SIGHT path's and is not read here --
searched for by grepping this file for each of the four values and for every line-of-sight bank name
(`c54.17*`, `c54.178_*`, `L814_*`, `r6784_*`), and none occurs in the code below.  *** The sky enters only
as `PO-47`'s four peak anchors and its four locating widths, quoted, and as `plik_lite`'s own binning ***
-- `chi2_of_spectrum.bin_spectrum` -- with every model binned identically before any comparison.

** WHY IT EXISTS. **  `r6959`'s order: five eliminations later the only mechanism left standing is the one
offered unasked at `cc66.46` -- that the contrast excess is the transfer's own normalisation across the
visibility window, since that is what multiplies an oscillation symmetrically about its envelope without
moving its phase.  ⓵ᵃ measure the source's conformal-time dependence across the window on both arms and
report it as a FUNCTION; ⓵ᵇ impose one arm's normalisation on the other and check the contrast moves by
the amount the measurement predicted IN ADVANCE; ⓵ᶜ state first what would refute it, and say what the
swap does to the comb and the depths as well as to the contrast.
  ⌗ ** The prediction and six refutation conditions were committed before any swap ran **, in
  `computations/beyond_the_wall/r6959_directions/PREDICTION.md`, and the taper coefficients are solved
  from the ⓵ᵃ measurement into `prediction.json`, which the launchers read -- so neither the size
  predicted nor the operation performed could be chosen after a spectrum was seen.

⛭⛭⛭ ** ⓵ᵃ THE FUNCTION, AND A CANCELLATION IN IT THAT NOBODY HAD LOOKED FOR. **  The source's own weight
across the window, band by band in $q=\ell/\ell_A$, has its spread in the phase variable $r_{s,\rm leaf}$
at $0.06523$ of $r_s$ on the control and $0.06424$ on the arm: *** the arm is the narrower, by one and a
half per cent. ***  ⇒ And the reason it is only that much is a two-clock statement with the sign reversed
from the obvious one: ** the arm's visibility is $14.6$ per cent WIDER in conformal time ($43.59$ against
$38.04$) while its acoustic phase accumulates $13.7$ per cent SLOWER per unit of it ($0.39334$ against
$0.45572$, because `Jac` runs $0.789$--$0.913$ across the arm's window and is identically $1$ across the
control's) -- and the product, which is what a smearing reads, comes to $0.9890$ of the control's. **
⌗ *So the two-rate structure does reach the window, and then very nearly cancels inside it.  That is a
fact about this construction and not about the statistic.*

⛔ ** ⓵ᵇ THE ANALYTIC PREDICTION IS OF THE RIGHT SIGN, A FIFTH OF THE SIZE, AND THE WRONG SHAPE -- AND THE
RUN THEN BEAT THE PREDICTION BY THREE, WHICH IS A CORRECTION TO MY OWN ADVANCE STATEMENT. **  The exact
characteristic function of the phase under the measured weight gives $\mathcal D_{\rm cr}/\mathcal
D_{\rm lcdm} = 1.00078 \to 1.01654$ across the seven bands against a measured excess of $1.0215 \to
1.0762$.
  * ✔ ** R5, the sign, survives: ** the arm is the less smeared of the two in every band.
  * ⛔ ** R2, the size, fires on the ANALYTIC channel: ** $\ln\mathcal R_1$ at the top band is $0.0164$
    against the measured $0.0734$ -- $0.223$, outside the $[\tfrac12,2]$ bar fixed in advance.
  * ⛔ ** R1, the shape, fires and is the durable half: ** $\ln(\text{measured excess})$ against $q^2$ has
    an intercept of $0.0392$ -- an excess of $1.0400$ at $q=0$, $0.534$ of the top band's, above the half
    the condition set.  ** A characteristic function is identically $1$ at $k=0$, so no smearing can
    supply a $q$-independent offset at all ** (the prediction's own intercept is $0.00075$).
  * ⚠ ** AND R3's BRACKET WAS WRONG IN DIRECTION, WHICH I RECORD RATHER THAN ABSORB. **  `PREDICTION.md`
    ⓵ᵇ4 argued the contrast responds *between* $f$ and $f^2$ because $D_\ell$ is quadratic in the
    transfer.  ** Measured, it responds $1.2$ to $2.5$ times MORE than $f$ per unit coefficient, at both
    coefficients and in every band ** -- so the interval was on the wrong side of the truth, and the
    condition passed only because I specified its tolerance multiplicatively on $f$ rather than on
    $f-1$, which made it too loose to bite.  *The prediction that failed is mine; the run is what
    corrected it.*

⛭⛭ ** THREE WIRINGS OF THE SAME OPERATION, BECAUSE THE FIRST TWO WERE NOT THE OPERATION. **  A Gaussian in
$r_{s,\rm leaf}$ applied to the whole source also crushes the ISW, whose support runs to $\eta_0$ where
$|s-s_0|$ reaches $427$ Mpc: its $\eta$-integral came back at $0.656$ of itself at the small coefficient
and $0.238$ at the large one, and that is what moved $\ell_1$ by $7.7$ and $27.3$ multipoles.  Tapering
only the visibility-carried source fixes it.  ⌗ *Then the ISW-preserving run still moved the contrast
three times the prediction, and I attributed that to the taper shrinking the window's total weight against
the ISW -- so a third wiring holds that weight fixed (`SRCTAPERNORM=1`).*  ⛔ ** It lands on the second to
three parts in ten thousand, so that diagnosis was wrong too: the over-response is not the weight, it is
the contrast statistic's own sensitivity to the window's spread. **  *Both wrong readings are banked and
gated rather than deleted -- the ISW pair is how the ISW's share of the low-$q$ contrast was measured.*

⛭⛭⛭ ** AND THE ANSWER THE ORDER ASKED FOR, TAKEN FROM THE INSTRUMENT'S OWN RESPONSE RATHER THAN FROM A
MODEL OF IT. **  With two coefficients the run's response is calibrated band by band and inverted: ** the
arm's own window narrowing delivers $23$ to $45$ per cent of the band excess above $q=1.9$, a third on
average **, and the direct swap -- imposing the arm's spread on the control and reading the excess against
the tapered control -- closes $20$ to $39$ per cent there, which is the same answer by a different route.
⇒ *** The narrowing that would deliver ALL of the excess is $4.5$ per cent against the arm's $1.7$, a
factor of $2.7$. ***  ⌗ *So this is the first channel in this sector to carry a measured, non-trivial
fraction of the excess from a quantity nobody chose -- and $2.7$ is a factor, not an order of magnitude,
which is why the row's remainder is now a third of a per cent of window width rather than a mystery.*

⛔ ** ⓵ᶜ R4, AND THE REFUTATION THAT CAME FROM 66'S OWN PREVIOUS REVISION. **  `cc66.46` established that
the excess is SYMMETRIC about the envelope -- $1.0668$ on the peak side against $1.0561$ on the trough
side.  ** This channel is not: the arm-sized swap delivers $81$ per cent of the arm's peak-height excess
and $14$ per cent of its trough-depth excess, a $5.7$-fold asymmetry. **  ⇒ *** A channel that is
peak-weighted cannot be the whole of an excess that is symmetric, and that argument is independent of
every size estimate above. ***  ⌗ *And the comb: the arm-sized swap moves $\ell_1$ by $+2.8$ multipoles
where the arm sits $+1.4$ above the control, so it overshoots $\ell_1/\ell_A$ past the arm's own value and
past the sky's locating width, while $\ell_2$, $\ell_3$ and $\ell_4$ stay inside theirs.  The taper that
would deliver the whole excess moves $\ell_1$ by $18.5$ multipoles and the peak heights by $45$ per cent.*

⚑ ** THE GUARDS. **  The window cut is not load-bearing: the analytic prediction moves by under two
thousandths across $\pm2$ to $\pm6$ FWHM.  Nor is the weight's term choice: on the monopole ALONE the
prediction is smaller still.  ⚠ *And the order's third-transfer warning was checked and not assumed: the
smearing's* $q$*-signature does not transfer to the term mix's, which is why the two are separable, and
the contrast's response does not transfer to the heights' and depths', which is what the asymmetry above
measures.*  ⌗ *The null: `SRCTAPER` unset takes no branch at all, so the default is byte-identical --
verified against the pre-edit file on a 60-mode slice, every saved array, after each of the three
wirings.*

** WHAT IS NOT CLAIMED. **  NOT that the normalisation across the window is the mechanism: it carries about
a third, it is peak-weighted where the excess is symmetric, and R1's $q$-independent offset is outside it.
NOT that it is nothing -- it is the first channel in this sector measured to carry any definite share.
NOT a claim about the term mix, which is reported and not swapped.  NOT a detection: the $1.8$ of
`cc66.46` is one statistic's spread and nothing here moves it.  NOT a verdict on the two-rate assignment.
NOT a re-derivation of `PO-47`'s peak spreads, which are quoted.  No refit, nothing touching `prop:flat`
or the clock family, and no corpus edits.

COMPUTES: scope.
  * ** EVERY COSMOLOGICAL PARAMETER IS BANKED, NOT CHOSEN HERE. **  Both arms at `r6825+cc66.25`'s
    verified 185-bin refit minima; the profiles and all six tapered spectra are that same configuration.
    Nothing here re-fits and nothing here moves.
  * `spectra/r6959_eta_{lcdm,cr}.npz` (the instrument's own `SRCETA` output, unaltered),
    `spectra/r6959_{swap,big,swapall,bigall,nswap,nbig}_lcdm.npz`,
    `spectra/r6941_fine_{lcdm,cr}.npz`.
  * ** The taper coefficients are not free numbers: ** each is solved from the `SRCETA` measurement -- one
    to match the arm's spread, one to deliver the observed excess at the top band under the analytic
    model -- and each is carried in the bank it produced, so this receipt reads them from the spectra
    rather than restating them.
  * ** The inversion uses the instrument's own response and no model of it: ** two coefficients fix
    $\ln R = c_1\alpha + c_2\alpha^2$ per band from the two norm-preserving runs, and that is what is
    inverted.  *The analytic characteristic function is reported beside it as the prediction it was, not
    as the calibration.*
  * `PO-47`'s four peak anchors $220.6/538.1/809.8/1121.9$ and its four locating widths
    $1.00/1.20/1.60/2.36$ are quoted from that receipt and not recomputed.  `cc66.46`'s $1.0668/1.0561$
    peak-and-trough split is quoted from that receipt; the heights and depths here are recomputed on
    these banks with its own anchored reading.
  * The statistic is `r6911+cc66.40`'s envelope-normalised oscillation with its running arithmetic mean
    over one acoustic period, unchanged, in the same seven bands; the locator is `cc66.45`'s anchored
    parabola.
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

TAP = ('swap', 'big', 'swapall', 'bigall', 'nswap', 'nbig')
NEED = (('r6959_eta_lcdm.npz', 'r6959_eta_cr.npz', 'r6941_fine_lcdm.npz', 'r6941_fine_cr.npz')
        + tuple(f'r6959_{t}_lcdm.npz' for t in TAP))
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
T = {t: np.load(os.path.join(SP, f'r6959_{t}_lcdm.npz')) for t in TAP}

QE = A['cr']['q_edges']
QC = 0.5 * (QE[:-1] + QE[1:])
NF = 3.0                       # the window cut, in FWHM of the visibility; stability gated below
TERMS = ('w2sw', 'w2dp', 'w2isw', 'w2pol')
LF = np.arange(100.0, 1300.0, 1.0)
TR = np.array([396.0, 674.0, 994.0])          # the control's own trough anchors, as at `cc66.46`
PK = np.array([238.0, 537.0, 828.0])
SKY4 = np.array([220.6, 538.1, 809.8, 1121.9])              # PO-47's quartet, the anchors only
SKYW = np.array([1.00, 1.20, 1.60, 2.36])                   # and its locating widths, PO-47's own
LC, _FAC = CS.bin_center_and_fac()


# ---- the statistic, unchanged from `r6911+cc66.40` ------------------------------------------------
def env_a(x, y, win=1.0):
    e = np.empty_like(y)
    for j, v in enumerate(x):
        m = (x >= v - win / 2) & (x <= v + win / 2)
        e[j] = np.mean(y[m])
    return e


def osc(x, y, win=1.0):
    e = env_a(x, y, win)
    return (y - e) / e


def band_std(q, o):
    return np.array([float(np.std(np.interp(np.linspace(a, b, 400), q, o)))
                     for a, b in zip(QE[:-1], QE[1:])])


# ---- the measured function, and the smearing it implies ------------------------------------------
def weight(d, key='w2md', nf=NF, taper=0.0, s0=None, nrm=False):
    """the AMPLITUDE weight across the window, and its phase abscissa r_s,leaf"""
    ee, els, w = d['eta'], float(d['eta_ls']), float(d['eta_ls_w'])
    m = (ee >= els - nf * w) & (ee <= els + nf * w)
    e, s = ee[m], d['rs_leaf'][m]
    a = np.sqrt(np.maximum(d[key][m], 0.0))
    if taper != 0.0:
        _s0 = float(d['rs_leaf'][int(np.argmin(np.abs(ee - els)))]) if s0 is None else s0
        _t = np.exp(-taper * (s - _s0) ** 2)
        if nrm:
            # the instrument's own `SRCTAPERNORM=1`: divide by the visibility-weighted mean, so the
            # window's TOTAL weight is held fixed and only its spread moves
            _g = d['vis'][m]
            _t = _t / (float(np.trapezoid(_g * _t, e)) / float(np.trapezoid(_g, e)))
        a = a * _t[:, None]
    return e, s, a


def dfac(d, b, **kw):
    """the EXACT characteristic function of the phase under the measured weight -- no Gaussian step"""
    e, s, a = weight(d, **kw)
    w = a[:, b]
    k = np.pi * QC[b] / float(d['r_s'])
    z = (float(np.trapezoid(w * np.cos(k * s), e)), float(np.trapezoid(w * np.sin(k * s), e)))
    return float(np.hypot(*z)) / float(np.trapezoid(w, e))


def spread(d, b=None, **kw):
    e, s, a = weight(d, **kw)
    w = a.sum(axis=1) if b is None else a[:, b]
    t = float(np.trapezoid(w, e))
    mu = float(np.trapezoid(w * s, e)) / t
    return float(np.sqrt(max(np.trapezoid(w * (s - mu) ** 2, e) / t, 0.0)))


def peaks_sub(ls, Dl, anch, W=40):
    """`cc66.45`'s anchored parabola -- cleared to 0.028 of a multipole at every one of the four"""
    out = []
    for a in anch:
        m = (ls >= a - W) & (ls <= a + W)
        x, y = ls[m].astype(float), Dl[m]
        i = int(np.argmax(y))
        if 0 < i < len(x) - 1:
            dd = 0.5 * (y[i - 1] - y[i + 1]) / (y[i - 1] - 2 * y[i] + y[i + 1])
            out.append(float(x[i] + dd * (x[1] - x[0])))
        else:
            out.append(float(x[i]))
    return np.array(out)


def spl(Db):
    m = (LC >= 100) & np.isfinite(Db)
    return CubicSpline(LC[m], Db[m])(LF)


def anchored(o, anch, W, kind):
    out = []
    for a in anch:
        k = (LF >= a - W) & (LF <= a + W)
        out.append(float(abs(np.min(o[k]))) if kind == 'min' else float(np.max(o[k])))
    return np.array(out)


# ==================================================================================================
print("\nPART 1 -- ⓵ᵃ THE FUNCTION: THE SOURCE'S WEIGHT ACROSS THE WINDOW, AND ITS PHASE SPREAD.")
print("-" * 100)
check("both profiles are the HIERARCHY path, which is the only path `_project` is reached from",
      all(str(A[t]['path']) == 'HIER' for t in A), 'HIER on both')
_JW = {t: A[t]['jac'][(A[t]['eta'] >= float(A[t]['eta_ls']) - NF * float(A[t]['eta_ls_w']))
                      & (A[t]['eta'] <= float(A[t]['eta_ls']) + NF * float(A[t]['eta_ls_w']))]
       for t in A}
check("the control's `Jac` is identically 1 across the window and the arm's is not -- the two-clock "
      "structure is present in the measurement and is not assumed",
      np.allclose(_JW['lcdm'], 1.0, atol=1e-12)
      and 0.78 < float(_JW['cr'].min()) < 0.80 and 0.91 < float(_JW['cr'].max()) < 0.92,
      f"lcdm 1.0000, cr {float(_JW['cr'].min()):.4f}..{float(_JW['cr'].max()):.4f} over "
      f"+-{NF:g} FWHM")

print("\n  band   sigma_s/r_s (lcdm -> cr)   D_lcdm   D_cr    monopole fraction (lcdm -> cr)")
SIG = {t: np.array([spread(A[t], b) / float(A[t]['r_s']) for b in range(len(QC))]) for t in A}
DD = {t: np.array([dfac(A[t], b) for b in range(len(QC))]) for t in A}
FRM = {}
for t in A:
    d, m = A[t], None
    ee, els, w = d['eta'], float(d['eta_ls']), float(d['eta_ls_w'])
    m = (ee >= els - NF * w) & (ee <= els + NF * w)
    tot = np.array([[float(np.trapezoid(d[k][m][:, b], ee[m])) for k in TERMS]
                    for b in range(len(QC))])
    FRM[t] = tot / tot.sum(axis=1)[:, None]
for b in range(len(QC)):
    print(f"  q={QC[b]:.2f}      {SIG['lcdm'][b]:.5f} -> {SIG['cr'][b]:.5f}       "
          f"{DD['lcdm'][b]:.5f}  {DD['cr'][b]:.5f}     "
          f"{FRM['lcdm'][b, 0]:.4f} -> {FRM['cr'][b, 0]:.4f}")

S_L, S_C = spread(A['lcdm']) / float(A['lcdm']['r_s']), spread(A['cr']) / float(A['cr']['r_s'])
NARROW = 100 * (1 - S_C / S_L)
print(f"\n  band-summed: the control {S_L:.5f} of its r_s, the arm {S_C:.5f} of its "
      f"-- the arm is {NARROW:.2f} per cent the narrower")
FW = {t: float(A[t]['eta_ls_w']) for t in A}
DR = {t: float(np.mean(np.gradient(A[t]['rs_leaf'], A[t]['eta'])[
    (A[t]['eta'] >= float(A[t]['eta_ls']) - NF * FW[t])
    & (A[t]['eta'] <= float(A[t]['eta_ls']) + NF * FW[t])])) for t in A}
print(f"  and the reason: the arm's visibility is {100 * (FW['cr'] / FW['lcdm'] - 1):+.1f} per cent "
      f"wider in eta ({FW['cr']:.2f} against {FW['lcdm']:.2f}) while its phase accumulates "
      f"{100 * (DR['cr'] / DR['lcdm'] - 1):+.1f} per cent slower per unit of it "
      f"({DR['cr']:.5f} against {DR['lcdm']:.5f})")
check("the arm's window is WIDER in conformal time -- by more than ten per cent",
      FW['cr'] / FW['lcdm'] > 1.10, f"{FW['cr'] / FW['lcdm']:.4f}")
check("and its phase accumulates SLOWER per unit conformal time by nearly the same factor, so the "
      "product -- the spread the smearing reads -- is nearly invariant",
      abs((FW['cr'] * DR['cr']) / (FW['lcdm'] * DR['lcdm']) - 1) < 0.02,
      f"product ratio {(FW['cr'] * DR['cr']) / (FW['lcdm'] * DR['lcdm']):.4f}")
check("so the arm is the narrower of the two in the phase variable, but by under three per cent",
      0 < NARROW < 3.0, f"{NARROW:.2f} per cent")
check("the arm carries MORE of its window's power in the monopole than the control does, in every "
      "band -- the term mix is where a normalisation difference that is NOT a smearing lives",
      bool(np.all(FRM['cr'][:, 0] > FRM['lcdm'][:, 0])),
      f"{FRM['lcdm'][0, 0]:.4f}->{FRM['cr'][0, 0]:.4f} .. "
      f"{FRM['lcdm'][-1, 0]:.4f}->{FRM['cr'][-1, 0]:.4f}")
check("and correspondingly less in the Doppler, so the two exchange weight rather than one growing",
      bool(np.all(FRM['cr'][:, 1] < FRM['lcdm'][:, 1])),
      f"{FRM['lcdm'][0, 1]:.4f}->{FRM['cr'][0, 1]:.4f}")
check("the ISW is under one per cent of the window's power on both arms, so the window statistic is "
      "not carrying the term that lives outside it",
      float(max(FRM[t][:, 2].max() for t in A)) < 0.01,
      f"max {float(max(FRM[t][:, 2].max() for t in A)):.4f}")

# ==================================================================================================
print("\nPART 2 -- ⓵ᵇ THE PREDICTION, AND ⓵ᶜ's REFUTATION CONDITIONS APPLIED TO IT.")
print("-" * 100)
Q = {t: F[t]['ls'].astype(float) / float(F[t]['l_A']) for t in F}
O = {t: osc(Q[t], F[t]['Dl']) for t in F}
C0 = {t: band_std(Q[t], O[t]) for t in F}
MEAS = C0['cr'] / C0['lcdm']
R1 = DD['cr'] / DD['lcdm']
print("  band    predicted R1 = D_cr/D_lcdm    [R1, R1^2]           measured excess")
for b in range(len(QC)):
    lo, hi = sorted((R1[b], R1[b] ** 2))
    print(f"  q={QC[b]:.2f}        {R1[b]:.5f}              [{lo:.5f}, {hi:.5f}]      {MEAS[b]:.5f}")
check("the measured excess is this campaign's own, recomputed here from `r6941_fine_*` rather than "
      "quoted -- and it reproduces `cc66.46`'s seven band ratios",
      np.allclose(MEAS, [1.0215, 1.0574, 1.0519, 1.0606, 1.0748, 1.0659, 1.0762], atol=5e-4),
      "  ".join(f"{x:.4f}" for x in MEAS))

# ---- R5, the sign -------------------------------------------------------------------------------
check("⓵ᶜ R5 THE SIGN SURVIVES: the arm is the LESS smeared of the two in every band, which is the "
      "direction a 6 per cent excess needs", bool(np.all(R1 > 1.0)),
      f"R1 = {R1.min():.5f} .. {R1.max():.5f}")

# ---- R2, the size -------------------------------------------------------------------------------
RAT2 = float(np.log(R1[-1]) / np.log(MEAS[-1]))
check("⛔ ⓵ᶜ R2 FIRES -- THE SIZE: the predicted log-excess at the top band is under half the "
      "measured one, which `PREDICTION.md` fixed in advance as the refutation bar",
      RAT2 < 0.5, f"ln R1 {np.log(R1[-1]):.5f} against measured {np.log(MEAS[-1]):.5f}, "
                  f"ratio {RAT2:.3f}, bar [0.5, 2]")
check("and it under-delivers rather than over-delivers, so it is NOT `cc66.40`'s failure repeating",
      RAT2 < 1.0, f"{1 / RAT2:.2f}x short")
check("the shortfall is worst at the bottom of the band, where a smearing has almost nothing to give",
      float(np.log(R1[0]) / np.log(MEAS[0])) < 0.1,
      f"q=1.20: {float(np.log(R1[0]) / np.log(MEAS[0])):.4f} of the measured")

# ---- R1, the shape ------------------------------------------------------------------------------
q2 = QC ** 2
sl_m, ic_m = np.polyfit(q2, np.log(MEAS), 1)
sl_p, ic_p = np.polyfit(q2, np.log(R1), 1)
print(f"\n  ln(excess) against q^2 -- measured: slope {sl_m:.6f}, intercept {ic_m:.6f} "
      f"({np.exp(ic_m):.4f} at q=0);  predicted: slope {sl_p:.6f}, intercept {ic_p:.6f}")
check("⛔ ⓵ᶜ R1 FIRES -- THE SHAPE: the measured excess extrapolates to a NON-ZERO offset at q=0, "
      "worth more than half the top band's, and a characteristic function is identically 1 there",
      ic_m / np.log(MEAS[-1]) > 0.5,
      f"intercept {ic_m:.6f} is {ic_m / np.log(MEAS[-1]):.3f} of the top band's {np.log(MEAS[-1]):.5f}")
check("the prediction's own intercept is two orders down, as a smearing's must be -- so the offset is "
      "not a shared systematic of the fit",
      abs(ic_p) < 0.02 * abs(ic_m), f"{ic_p:.6f} against {ic_m:.6f}")
check("and the q^2 SLOPE is the half that does survive: the prediction supplies a fifth to a half of "
      "it, not a hundredth", 0.2 < sl_p / sl_m < 0.6, f"{sl_p / sl_m:.3f} of the measured slope")

# ---- the two judgement calls in the measurement, gated rather than taken on trust ---------------
ST = np.array([[dfac(A['cr'], b, nf=nf) / dfac(A['lcdm'], b, nf=nf) for b in range(len(QC))]
               for nf in (2, 3, 4, 5, 6)])
check("the window cut is not load-bearing: R1 moves by under two thousandths across +-2 to +-6 FWHM, "
      "which is a twentieth of the shortfall it would have to explain",
      float(np.max(ST.max(axis=0) - ST.min(axis=0))) < 2e-3,
      f"max spread {float(np.max(ST.max(axis=0) - ST.min(axis=0))):.2e} against the "
      f"{float(MEAS[-1] - R1[-1]):.4f} it is short by")
R1SW = np.array([dfac(A['cr'], b, key='w2sw') / dfac(A['lcdm'], b, key='w2sw')
                 for b in range(len(QC))])
check("nor is the weight's term choice: on the monopole ALONE -- one phase rather than two -- the "
      "prediction is SMALLER still, so the conclusion does not rest on including the Doppler",
      bool(np.all(R1SW <= R1 + 1e-9)) and np.log(R1SW[-1]) / np.log(MEAS[-1]) < 0.5,
      f"monopole-only top band {R1SW[-1]:.5f} against {R1[-1]:.5f}")


# ==================================================================================================
print("\nPART 3 -- ⓵ᵇ THE RUNS: THREE WIRINGS, AND WHAT EACH OF THE FIRST TWO GOT WRONG.")
print("-" * 100)
AL, ABG, S0 = float(T['swap']['taper']), float(T['big']['taper']), float(T['swap']['taper_s0'])
check("the swap's coefficient is the one the MEASUREMENT fixes: it takes the control's band-summed "
      "spread to the arm's, in units of each arm's own r_s",
      abs(spread(A['lcdm'], taper=AL, s0=S0) / float(A['lcdm']['r_s']) - S_C) < 2e-4,
      f"SRCTAPER={AL:.6g} gives {spread(A['lcdm'], taper=AL, s0=S0) / float(A['lcdm']['r_s']):.5f} "
      f"against the arm's {S_C:.5f}")
check("the six tapered banks are the two coefficients under three wirings, and each carries which "
      "wiring produced it",
      all(float(T[t]['taper']) == (AL if t in ('swap', 'swapall', 'nswap') else ABG) for t in TAP)
      and [int(T[t]['taper_all']) for t in TAP] == [0, 0, 1, 1, 0, 0]
      and [int(T[t].get('taper_norm', 0)) for t in TAP] == [0, 0, 0, 0, 1, 1],
      "swap/big ISW-preserving, swapall/bigall all-terms, nswap/nbig weight-preserving")


def resp(t):
    q = T[t]['ls'].astype(float) / float(T[t]['l_A'])
    return band_std(q, osc(q, T[t]['Dl'])) / C0['lcdm']


R = {t: resp(t) for t in TAP}
PRED = {'nswap': np.array([dfac(A['lcdm'], b, taper=AL, s0=S0, nrm=True) / DD['lcdm'][b]
                           for b in range(len(QC))]),
        'nbig': np.array([dfac(A['lcdm'], b, taper=ABG, s0=S0, nrm=True) / DD['lcdm'][b]
                          for b in range(len(QC))])}
print("  band   predicted f (small/big)   nswap    swap    swapall  |   nbig     big     bigall")
for b in range(len(QC)):
    print(f"  q={QC[b]:.2f}   {PRED['nswap'][b]:.5f} / {PRED['nbig'][b]:.5f}      "
          f"{R['nswap'][b]:.5f}  {R['swap'][b]:.5f}  {R['swapall'][b]:.5f}  |  "
          f"{R['nbig'][b]:.5f}  {R['big'][b]:.5f}  {R['bigall'][b]:.5f}")

_iw = np.sqrt(np.maximum(A['lcdm']['w2isw'][:, 0], 0.0))
_ee, _s = A['lcdm']['eta'], A['lcdm']['rs_leaf']
ISWCUT = {k: float(np.trapezoid(_iw * np.exp(-al * (_s - S0) ** 2), _ee)
                   / np.trapezoid(_iw, _ee)) for k, al in (('small', AL), ('big', ABG))}
print(f"\n  ⛔ WIRING ONE was not the operation: over the whole eta grid the same Gaussian cuts the ISW's "
      f"own eta-integral to {ISWCUT['small']:.3f} and {ISWCUT['big']:.3f} of itself")
check("⛔ the all-terms taper removes a third of the ISW at the coefficient that narrows the window by "
      "a per cent, and the ISW's support is outside the window entirely",
      ISWCUT['small'] < 0.7, f"ISW eta-integral -> {ISWCUT['small']:.4f}")
check("and the damage is where the ISW lives: the all-terms wiring exceeds the ISW-preserving one by "
      "more than double in the lowest band, while above q=1.9 the two agree to a per cent",
      (R['swapall'][0] - 1) > 2 * (R['swap'][0] - 1)
      and float(np.max(np.abs(R['swapall'][1:] - R['swap'][1:]))) < 0.01,
      f"q=1.20 {R['swap'][0]:.5f} against {R['swapall'][0]:.5f}; above, max difference "
      f"{float(np.max(np.abs(R['swapall'][1:] - R['swap'][1:]))):.5f}")
check("⛔ AND WIRING TWO's DIAGNOSIS WAS WRONG TOO, WHICH IS WHY THERE IS A THIRD: holding the window's "
      "total weight fixed lands on the ISW-preserving run to parts in ten thousand, so the taper "
      "shrinking the window against the ISW is NOT what made the run outrun the prediction",
      float(np.max(np.abs(R['nswap'] - R['swap']))) < 1e-3
      and float(np.max(np.abs(R['nbig'] - R['big']))) < 4e-3,
      f"max |nswap - swap| {float(np.max(np.abs(R['nswap'] - R['swap']))):.2e}, "
      f"|nbig - big| {float(np.max(np.abs(R['nbig'] - R['big']))):.2e}")
OVER = (R['nswap'] - 1) / (PRED['nswap'] - 1)
OVERB = (R['nbig'] - 1) / (PRED['nbig'] - 1)
print(f"\n  the run's response against the analytic one, (run-1)/(pred-1): "
      + "  ".join(f"{x:.1f}" for x in OVER))
print(f"  and at the large coefficient:                                  "
      + "  ".join(f"{x:.1f}" for x in OVERB))
check("⚠ ⓵ᶜ R3's BRACKET WAS WRONG IN DIRECTION, AND THAT IS MINE: `PREDICTION.md` argued the contrast "
      "responds BETWEEN f and f^2, i.e. no more than f; measured, it responds MORE than f in every "
      "band and at both coefficients",
      bool(np.all(OVER > 1.0)) and bool(np.all(OVERB > 1.0)),
      f"smallest over-response {min(float(OVER.min()), float(OVERB.min())):.1f}x")
check("and the two coefficients agree on that factor to within a factor two above the lowest band, so "
      "it is a property of the statistic and not of one run",
      float(np.max(OVER[1:] / OVERB[1:])) < 2.0,
      f"ratio across coefficients {float(np.min(OVER[1:] / OVERB[1:])):.2f}..."
      f"{float(np.max(OVER[1:] / OVERB[1:])):.2f}")
check("⛔ so the condition passed only because its tolerance was written multiplicatively on f instead "
      "of on f-1, which made it too loose to bite -- recorded, not absorbed",
      bool(np.all([min(p, p ** 2) / 1.5 <= r <= 1.5 * max(p, p ** 2)
                   for p, r in zip(PRED['nswap'], R['nswap'])])),
      "every band inside a bar that spans 0.67 to 1.50")

# ==================================================================================================
print("\nPART 4 -- THE SIZE, TAKEN FROM THE INSTRUMENT'S OWN RESPONSE RATHER THAN FROM A MODEL OF IT.")
print("-" * 100)


def sig_b(b, taper=0.0):
    return spread(A['lcdm'], b, taper=taper, s0=S0, nrm=True)


def alpha_for(b, target_sigma):
    lo, hi = 0.0, ABG * 4
    for _ in range(90):
        a = 0.5 * (lo + hi)
        if sig_b(b, a) > target_sigma:
            lo = a
        else:
            hi = a
    return a


NEED_PC, ARM_PC, DELIV = [], [], []
print("  band   arm's own narrowing   narrowing for ALL of it   the arm's share, through the run's "
      "own response")
for b in range(len(QC)):
    M = np.array([[AL, AL ** 2], [ABG, ABG ** 2]])
    c = np.linalg.solve(M, [np.log(R['nswap'][b]), np.log(R['nbig'][b])])
    tgt = np.log(MEAS[b])
    disc = c[0] ** 2 + 4 * c[1] * tgt
    a_all = ((-c[0] + np.sqrt(disc)) / (2 * c[1]) if c[1] != 0 and disc >= 0 else tgt / c[0])
    if not a_all > 0:
        a_all = tgt / c[0]
    own = sig_b(b)
    arm_pc = 100 * (1 - (spread(A['cr'], b) / float(A['cr']['r_s']))
                    / (own / float(A['lcdm']['r_s'])))
    a_arm = alpha_for(b, own * (1 - arm_pc / 100))
    got = float(np.exp(c[0] * a_arm + c[1] * a_arm ** 2))
    NEED_PC.append(100 * (1 - sig_b(b, a_all) / own))
    ARM_PC.append(arm_pc)
    DELIV.append((got - 1) / (MEAS[b] - 1))
    print(f"  q={QC[b]:.2f}      {arm_pc:5.2f} per cent          {NEED_PC[-1]:5.2f} per cent        "
          f"{got:.5f} against {MEAS[b]:.5f}  ->  {100 * DELIV[-1]:5.1f} per cent")
NEED_PC, ARM_PC, DELIV = np.array(NEED_PC), np.array(ARM_PC), np.array(DELIV)
print(f"\n  mean over the bands: {ARM_PC.mean():.2f} per cent available against {NEED_PC.mean():.2f} "
      f"needed -- a factor {NEED_PC.mean() / ARM_PC.mean():.2f}")
check("⛭ THE CHANNEL CARRIES A DEFINITE, NON-TRIVIAL SHARE: through the instrument's own two-coefficient "
      "response, the arm's own window narrowing delivers between a fifth and a half of the band excess "
      "everywhere above q=1.9", bool(np.all((DELIV[1:] > 0.20) & (DELIV[1:] < 0.50))),
      "shares " + "  ".join(f"{100 * x:.0f}%" for x in DELIV[1:]))
check("and the narrowing that would deliver ALL of it is a factor of a few above what the arm has, not "
      "an order of magnitude", 1.5 < NEED_PC.mean() / ARM_PC.mean() < 5.0,
      f"{NEED_PC.mean():.2f} against {ARM_PC.mean():.2f} per cent")
EXC = C0['cr'] / (R['nswap'] * C0['lcdm'])
CLOSED = (MEAS - EXC) / (MEAS - 1.0)
print("\n  and the DIRECT swap, which needs no response model at all -- the excess read against the "
      "tapered control:")
print("    " + "  ".join(f"{x:.5f}" for x in EXC) + "   against the measured "
      + "  ".join(f"{x:.5f}" for x in MEAS))
check("⛭ THE TWO ROUTES AGREE: imposing the arm's spread on the control closes a fifth to two fifths of "
      "the excess above q=1.9, which is the share the inversion gives by a different road",
      bool(np.all((CLOSED[1:] > 0.18) & (CLOSED[1:] < 0.42))),
      "closed " + "  ".join(f"{100 * x:.0f}%" for x in CLOSED[1:]))
check("⌗ and the lowest band is the one the inversion cannot be trusted in, which is stated rather than "
      "averaged away: there the swap OVERSHOOTS, taking the excess below unity",
      EXC[0] < 1.0 and CLOSED[0] > 1.0,
      f"q=1.20 excess {EXC[0]:.5f}, closed fraction {CLOSED[0]:.3f}")

# ==================================================================================================
print("\nPART 5 -- ⓵ᶜ R4: THE COMB, THE DEPTHS, AND THE ASYMMETRY THAT REFUTES IT ON ITS OWN.")
print("-" * 100)
p0 = peaks_sub(F['lcdm']['ls'].astype(float), F['lcdm']['Dl'], SKY4)
pC = peaks_sub(F['cr']['ls'].astype(float), F['cr']['Dl'], SKY4)
MV = {t: peaks_sub(T[t]['ls'].astype(float), T[t]['Dl'], SKY4) - p0 for t in TAP}
for t in ('nswap', 'swap', 'swapall', 'nbig', 'big', 'bigall'):
    print(f"    {t:8s} peaks moved " + "  ".join(f"{x:+8.3f}" for x in MV[t]))
print("    the arm's own      " + "  ".join(f"{x:+8.3f}" for x in pC - p0))
print("    sky locating width " + "  ".join(f"{x:8.2f}" for x in SKYW))
check("⛔ ⓵ᶜ R4: the taper that would deliver the whole excess moves the comb past the sky's locating "
      "width at more than one peak, so by the order's own rule it is not a mechanism for this row",
      int(np.sum(np.abs(MV['nbig']) > SKYW)) >= 2,
      "moves " + "  ".join(f"{a:+.2f}/{b:.2f}" for a, b in zip(MV['nbig'], SKYW)))
check("⌗ and the arm-sized swap OVERSHOOTS l_1 rather than reproducing it: it moves l_1 further than the "
      "arm sits from the control, and past the sky's width there, while l_2, l_3 and l_4 stay inside",
      MV['nswap'][0] > (pC - p0)[0] and MV['nswap'][0] > SKYW[0]
      and int(np.sum(np.abs(MV['nswap'][1:]) > SKYW[1:])) == 0,
      f"l_1 {MV['nswap'][0]:+.3f} against the arm's {(pC - p0)[0]:+.3f} and a width of {SKYW[0]:.2f}")
D0 = osc(LF / 301.6, spl(CS.bin_spectrum(F['lcdm']['ls'].astype(float), F['lcdm']['Dl'])))
DC = osc(LF / 301.6, spl(CS.bin_spectrum(F['cr']['ls'].astype(float), F['cr']['Dl'])))
T0, H0 = anchored(D0, TR, 40, 'min').mean(), anchored(D0, PK, 40, 'max').mean()
TCm, HCm = anchored(DC, TR, 40, 'min').mean(), anchored(DC, PK, 40, 'max').mean()
DEP = {}
for t in TAP:
    Dt = osc(LF / 301.6, spl(CS.bin_spectrum(T[t]['ls'].astype(float), T[t]['Dl'])))
    DEP[t] = (anchored(Dt, TR, 40, 'min').mean(), anchored(Dt, PK, 40, 'max').mean())
print(f"\n    control troughs {T0:.5f} heights {H0:.5f};  arm troughs {TCm:.5f} "
      f"({100 * (TCm / T0 - 1):+.2f} per cent) heights {HCm:.5f} ({100 * (HCm / H0 - 1):+.2f})")
for t in ('nswap', 'nbig'):
    print(f"    {t:8s} troughs {DEP[t][0]:.5f} ({100 * (DEP[t][0] / T0 - 1):+.2f} per cent)   "
          f"heights {DEP[t][1]:.5f} ({100 * (DEP[t][1] / H0 - 1):+.2f})")
SH_T = (DEP['nswap'][0] / T0 - 1) / (TCm / T0 - 1)
SH_H = (DEP['nswap'][1] / H0 - 1) / (HCm / H0 - 1)
print(f"\n  ⛔ the arm-sized swap delivers {100 * SH_H:.0f} per cent of the arm's peak-HEIGHT excess and "
      f"{100 * SH_T:.0f} per cent of its trough-DEPTH excess")
check("⛔ AND THAT REFUTES IT ON ITS OWN, FROM 66's OWN PREVIOUS REVISION: `cc66.46` measured the excess "
      "SYMMETRIC about the envelope (1.0668 peak side against 1.0561 trough side), and this channel is "
      "peak-weighted by more than a factor of five -- so a symmetric excess cannot be carried by it "
      "alone, whatever its size",
      SH_H / SH_T > 3.0 and SH_H > 0.5 and SH_T < 0.3,
      f"heights {100 * SH_H:.0f} per cent against depths {100 * SH_T:.0f} -- "
      f"{SH_H / SH_T:.1f}-fold asymmetry")
check("and the argument is independent of the size estimates, because it is a RATIO of two shares of the "
      "same operation and both are read on the same banks with the same anchored locator",
      DEP['nswap'][0] > T0 and DEP['nswap'][1] > H0,
      "both move the way the excess does, by very different fractions of it")
check("⌗ the taper that would deliver the whole excess wrecks the heights outright, which is the same "
      "asymmetry at forty times the amplitude",
      (DEP['nbig'][1] / H0 - 1) > 5 * (DEP['nbig'][0] / T0 - 1),
      f"heights {100 * (DEP['nbig'][1] / H0 - 1):+.1f} per cent against troughs "
      f"{100 * (DEP['nbig'][0] / T0 - 1):+.1f}")

print("\n" + "=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)
print("GATES: ALL PASS")
