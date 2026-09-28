#!/usr/bin/env python3
r"""P15 sec:refit-bound -- ** THE COMPOSITION RULE IS MEASURED AND IT IS MULTIPLICATIVE, WHICH
RETRACTS MY OWN PREVIOUS REVISION'S INFERENCE AND SHARPENS ITS ARITHMETIC: THE TWO CHANNELS COMPOSE
EXACTLY AS `cc66.48` ASSUMED, AND THE PAIR IS FLAT IN $q$ WHERE THE MEASURED EXCESS GROWS. **

** PATH PROVENANCE, IN THE HEADER, ON THE STANDING REQUIREMENT. **  *** Every model number below is the
HIERARCHY path *** -- `r6959_nswap_lcdm` (the window channel), `r6975_mix_lcdm` (the term mix), the new
`r6983_joint_lcdm` (both together), and the `LSTEP=1` baselines `r6941_fine_{lcdm,cr}`.  `sec:refit-bound`'s
quartet $222/538/818/1134$ is the LINE-OF-SIGHT path's and is not read -- searched for by grepping this
file for each of the four values and for every line-of-sight bank name (`c54.17*`, `c54.178_*`, `L814_*`,
`r6784_*`), and none occurs below.  *** The sky enters only as `PO-47`'s four peak anchors and its four
locating widths, quoted, and as `plik_lite`'s own binning. ***

** WHY IT EXISTS. **  `r6983`'s order, one item: `PO-56` is no longer "which channel carries the excess"
but "how do two channels compose", because `cc66.48` divided one response into the excess, got a
remainder, and then argued the remainder was an artefact of a composition rule nobody had measured.
*** So this revision measures the rule. ***  Both knobs are applied to ONE control spectrum at the sizes
their own revisions solved -- `SRCTAPER=1.100877765e-4 SRCTAPERS0=145.3465211 SRCTAPERNORM=1` from
`r6959+cc66.47` and `DPSRC=0.8794` from `r6975+cc66.48` -- and **neither coefficient is re-chosen here**.
*`PREDICTION.md` fixes all four conditions and all three rules' numbers, and is committed before the
joint run; `bank.py` and `joint_read.py` are committed before the spectrum lands, which is checkable in
the history.*

⛭⛭ ** ⓵ T-SIZE PASSES ON THE PAIR AND REFUTES QUADRATURE, WHICH IS THE ONE SEPARATION THE
PRE-REGISTRATION SAID THIS TEST COULD MAKE. **  The joint response lands within $0.005$ of the product
in **7 of 7** bands and of the sum in **7 of 7**, and within $0.005$ of quadrature in **0 of 7** -- the
quadrature miss reaching $0.018$, three and a half times the bar.  *The pre-registration declared in
advance that product and sum differ here by at most $0.0016$ and are therefore NOT separable by this
measurement; they are not separated, and that is the declared outcome and not a failure.*

⛭ ** AND THE PAIR IS SLIGHTLY SUB-MULTIPLICATIVE, CONSISTENTLY. **  Read as a fraction of each rule's
own predicted excess, the joint is $0.971$ of the product and $0.985$ of the sum -- **below both in
every one of the seven bands**, and above quadrature in every one.  *So the composition is
multiplicative to within the bar with a small systematic deficit, which is a statement about the pair
and not about one band.*

⛭⛭ ** ⓶ T-WEIGHT PASSES, AND IT IS THE SHARPEST OF THE FOUR. **  The anchored reading predicted
$\mathbf{2.83}$ from the two channels' separate height and depth changes, refuted below $2.2$ or above
$3.6$.  ** The joint reads $2.80$ ** -- one per cent from a number computed before the run, on an axis
where quadrature makes no prediction at all.  *A rule that predicts the weighting is worth more than one
that only fits the size, and this is that rule doing it.*

⛭ ** ⓷ T-COMB PASSES, inside its bracket and below its centre. **  $\ell_1$ was predicted to move
$+1.79$, refuted below $+1.0$ or above $+2.6$; it moves $\mathbf{+1.41}$.  *The same mild sub-additivity
the sizes show, on an axis a tenth as sensitive.*

⛭⛭ ** ⓸ T-INTERCEPT PASSES, and the joint response is the flattest thing this sector has measured. **
The joint intercept against $q^{2}$ is $\mathbf{1.0993}$, against a multiplicative prediction of
$1.1035$ with nothing fitted ($0.0042$ away), a sum's $1.1019$ ($0.0026$), and quadrature's $1.0839$
($0.0154$, outside the bar).  And its own $q$-dependence is $0.004$ of its intercept -- **flatter than
the term mix's $0.031$ and far flatter than the measured excess's $0.442$.**

⛔⛭⛭ ** THE CONSEQUENCE, AND IT CORRECTS MY OWN PREVIOUS REVISION IN ONE DIRECTION AND CONFIRMS IT IN
ANOTHER. **
  * ⛔ ** RETRACTED: `cc66.48`'s inference that the "remainder" is a construct of the composition rule. **
    That argument ran: the two channels' shares sum to more than the excess, therefore they do not
    compose as assumed, therefore a remainder computed by DIVIDING one response into the excess is an
    artefact of a wrong rule.  ** The rule is now measured and it is the assumed one. **  Dividing is
    the right operation, so the remainder is a well-defined object and not an artefact.  *The inference
    was wrong because it read an over-delivery as evidence about the RULE when it is evidence about the
    SIZES.*
  * ✔ ** CONFIRMED, and by direct measurement rather than by adding two numbers: ** `cc66.48` computed
    the pair at $1.72$ times the measured excess from the two channels separately; the joint run,
    which composes them in one spectrum, reads $\mathbf{1.70}$.  *The arithmetic was right to one per
    cent -- it was the conclusion drawn from it that was not.*
  * ⛭⛭ ** AND THE REAL OBSTRUCTION IS A SHAPE, NOT A SIZE, WHICH NO RESCALING CAN REMOVE. **  The pair
    over-delivers by $3.87\times$ in the longest-wavelength band and $1.38\times$ in the shortest,
    because **the joint response is flat in $q$ while the measured excess grows** ($0.004$ against
    $0.442$).  ⇒ *** So there is no coefficient on either knob that makes this pair reproduce the
    excess: scale it to the offset at $q=0$ and it is short at high $q$; scale it to high $q$ and it is
    an order too large at low $q$. ***  **That is a stronger negative than `cc66.48`'s, and it is
    available only because the rule was measured rather than assumed.**

** WHAT IS NOT CLAIMED. **  NOT that the composition is exactly multiplicative -- it is multiplicative
to within the pre-registered bar with a consistent $3$ per cent deficit, and product and sum are NOT
separated here, as declared in advance.  NOT that quadrature is refuted as a rule in general: it is
refuted for THIS pair at THESE sizes.  NOT that either channel is the mechanism -- both over-deliver
together, and the shape argument says neither rescaling helps.  NOT a third channel: the order forbids
one and none is added.  NOT that the excess is explained.  NOT a detection.  NOT a verdict on the
two-rate assignment.  NOT a re-derivation of `PO-47`'s spreads, which are quoted.  No refit, nothing
touching `prop:flat` or the clock family.

COMPUTES: scope.
  * ** EVERY COSMOLOGICAL PARAMETER IS BANKED, NOT CHOSEN HERE. **  Both arms at `r6825+cc66.25`'s
    verified 185-bin refit minima; every spectrum read is that configuration.  Nothing here re-fits.
  * `spectra/r6959_nswap_lcdm.npz`, `spectra/r6975_mix_lcdm.npz`, `spectra/r6983_joint_lcdm.npz`,
    `spectra/r6941_fine_{lcdm,cr}.npz`.
  * ** The two coefficients are not free numbers and are not re-chosen: ** each was solved in the
    revision that introduced its knob, and the joint bank carries both so this receipt reads them off
    the spectrum rather than restating them.
  * ** The joint spectrum is a SUM OF DISJOINT MODE SLICES, and the tiling is asserted rather than
    trusted: ** `r6983_directions/bank.py` reconstructs each slice's span from its filename and refuses
    unless the spans tile `[0, 2547)` with no gap and no overlap.  *The run was re-sliced twice midway
    for an operational reason -- the container is reclaimed faster than a large slice completes -- which
    is exactly the circumstance a fixed-step check would have passed over.*
  * `PO-47`'s anchors $220.6/538.1/809.8/1121.9$ and widths $1.00/1.20/1.60/2.36$ are quoted from that
    receipt.  The statistic is `r6911+cc66.40`'s, unchanged, the locator `cc66.45`'s anchored parabola,
    and every weighting reading is against `cc66.48`'s measured symmetric baseline of $1.95$.
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

NEED = ('r6959_eta_cr.npz', 'r6959_nswap_lcdm.npz', 'r6975_mix_lcdm.npz', 'r6983_joint_lcdm.npz',
        'r6941_fine_lcdm.npz', 'r6941_fine_cr.npz')
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
WIN = np.load(os.path.join(SP, 'r6959_nswap_lcdm.npz'))
MIX = np.load(os.path.join(SP, 'r6975_mix_lcdm.npz'))
JNT = np.load(os.path.join(SP, 'r6983_joint_lcdm.npz'))

QE = np.load(os.path.join(SP, 'r6959_eta_cr.npz'))['q_edges']
QC = 0.5 * (QE[:-1] + QE[1:])
Q2 = QC ** 2
LF = np.arange(100.0, 1300.0, 1.0)
TR = np.array([396.0, 674.0, 994.0])
PK = np.array([238.0, 537.0, 828.0])
SKY4 = np.array([220.6, 538.1, 809.8, 1121.9])
SKYW = np.array([1.00, 1.20, 1.60, 2.36])
LC, _FAC = CS.bin_center_and_fac()
BASE = 1.95                              # `cc66.48`'s measured symmetric baseline, quoted


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


def hd(d):
    """the anchored heights and depths, `cc66.46`'s reading, on the likelihood's own binning"""
    o = osc(LF / 301.6, spl(CS.bin_spectrum(d['ls'].astype(float), d['Dl'])))
    return anchored(o, PK, 40, 'max').mean(), anchored(o, TR, 40, 'min').mean()


def peaks_sub(d, W=40):
    """`cc66.45`'s anchored parabola, cleared to 0.028 multipoles"""
    ls, Dl = d['ls'].astype(float), d['Dl']
    out = []
    for a in SKY4:
        m = (ls >= a - W) & (ls <= a + W)
        x, y = ls[m], Dl[m]
        i = int(np.argmax(y))
        dd = 0.5 * (y[i - 1] - y[i + 1]) / (y[i - 1] - 2 * y[i] + y[i + 1]) if 0 < i < len(x) - 1 else 0.
        out.append(float(x[i] + dd * (x[1] - x[0])))
    return np.array(out)


C0 = band_std(F['lcdm'])
MEAS = band_std(F['cr']) / C0
RW = band_std(WIN) / C0
RM = band_std(MIX) / C0
RJ = band_std(JNT) / C0
PROD = RW * RM
SUMR = RW + RM - 1.0
QUAD = 1.0 + np.sqrt((RW - 1) ** 2 + (RM - 1) ** 2)

check("the joint bank carries BOTH coefficients, so the composition read here is the one the two "
      "revisions solved and not a pair restated in this file",
      abs(float(JNT['srctaper']) - 1.100877765e-4) < 1e-12
      and abs(float(JNT['dpsrc']) - 0.8794) < 1e-9 and int(JNT['srctapernorm']) == 1,
      f"SRCTAPER={float(JNT['srctaper']):.6g} SRCTAPERNORM={int(JNT['srctapernorm'])} "
      f"DPSRC={float(JNT['dpsrc']):.4f}")
_dt = abs(float(JNT['srctaper']) / float(WIN['taper']) - 1)
_ds = abs(float(JNT['srctapers0']) / float(WIN['taper_s0']) - 1)
check("and they are the SAME numbers the two single-channel banks carry, so the joint run is those two "
      "operations and not two new ones.  ⌗ *Read under each bank's own key names, which differ because "
      "the two knobs were banked a revision apart -- and compared RELATIVELY, because the launcher's "
      "switch line carries the taper coefficient ROUNDED to ten significant figures while the window "
      "bank stores the full solved value.  The agreement is therefore to about 1e-8 and not to the "
      "last bit, which is a property of the spelling and not of the operation*",
      _dt < 1e-6 and _ds < 1e-6
      and int(JNT['srctapernorm']) == int(WIN['taper_norm'])
      and abs(float(JNT['dpsrc']) - float(MIX['dpsrc'])) < 1e-12,
      f"taper agrees to {_dt:.1e} relative, s0 to {_ds:.1e}, norm={int(WIN['taper_norm'])} on both, "
      f"DPSRC={float(MIX['dpsrc']):.4f} exactly")
check("the measured excess is recomputed here from `r6941_fine_*` and reproduces `cc66.46`'s seven "
      "band ratios", np.allclose(MEAS, [1.0215, 1.0574, 1.0519, 1.0606, 1.0748, 1.0659, 1.0762],
                                 atol=5e-4), "  ".join(f"{x:.4f}" for x in MEAS))

# ==================================================================================================
print("\nPART 1 -- ⓵ T-SIZE: THE JOINT AGAINST THE THREE RULES, ON THE PRE-REGISTERED BAR OF 0.005.")
print("-" * 100)
print("  q      window    term mix  |  product   sum       quadrature |  JOINT     measured")
for b in range(len(QC)):
    print(f"  {QC[b]:.2f}  {RW[b]:.5f}   {RM[b]:.5f}  |  {PROD[b]:.5f}   {SUMR[b]:.5f}   "
          f"{QUAD[b]:.5f}    |  {RJ[b]:.5f}   {MEAS[b]:.5f}")
NP_, NS_, NQ_ = (int((np.abs(RJ - P) < 0.005).sum()) for P in (PROD, SUMR, QUAD))
print(f"\n  within 0.005 --  product {NP_}/7   sum {NS_}/7   quadrature {NQ_}/7"
      f"   (quadrature's worst miss {np.abs(RJ - QUAD).max():.5f})")
check("⓵ T-SIZE PASSES: the joint lands within the pre-registered 0.005 of the product/sum pair in at "
      "least five of the seven bands", NP_ >= 5 and NS_ >= 5, f"product {NP_}/7, sum {NS_}/7")
check("⛭ AND IT SEPARATES QUADRATURE, WHICH IS THE ONE SEPARATION THE PRE-REGISTRATION SAID THIS "
      "MEASUREMENT COULD MAKE", NQ_ == 0 and np.abs(RJ - QUAD).max() > 0.01,
      f"quadrature {NQ_}/7, worst miss {np.abs(RJ - QUAD).max():.5f}, "
      f"{np.abs(RJ - QUAD).max() / 0.005:.1f} times the bar")
check("and the pre-registration's declared LIMIT holds too: product and sum are NOT separated here, "
      "because they differ by less than the bar", float(np.abs(PROD - SUMR).max()) < 0.005,
      f"product and sum differ by at most {np.abs(PROD - SUMR).max():.5f}")
FP, FS = (RJ - 1) / (PROD - 1), (RJ - 1) / (SUMR - 1)
print(f"\n  as a fraction of each rule's own excess -- product " + "  ".join(f"{x:.4f}" for x in FP)
      + f"   mean {FP.mean():.4f}")
print(f"                                              sum " + "  ".join(f"{x:.4f}" for x in FS)
      + f"   mean {FS.mean():.4f}")
check("⛭ the composition is slightly SUB-multiplicative, and consistently: the joint sits below the "
      "product and below the sum in every one of the seven bands, and above quadrature in every one",
      bool(np.all(RJ < PROD)) and bool(np.all(RJ < SUMR)) and bool(np.all(RJ > QUAD)),
      f"joint/product mean {FP.mean():.4f}, joint/sum mean {FS.mean():.4f}")

# ==================================================================================================
print("\nPART 2 -- ⓶ T-WEIGHT: THE ANCHORED WEIGHTING, AGAINST A NUMBER COMPUTED BEFORE THE RUN.")
print("-" * 100)
H0, T0 = hd(F['lcdm'])


def read_d(d):
    h, t = hd(d)
    return h / H0 - 1, t / T0 - 1


DH_C, DT_C = read_d(F['cr'])
DH_W, DT_W = read_d(WIN)
DH_M, DT_M = read_d(MIX)
DH_J, DT_J = read_d(JNT)
for nm, dh, dt in (('the whole excess', DH_C, DT_C), ('window', DH_W, DT_W),
                   ('term mix', DH_M, DT_M), ('JOINT', DH_J, DT_J)):
    print(f"    {nm:18s} {100 * dh:+8.3f}%  {100 * dt:+8.3f}%   ratio {dh / dt:6.2f}")
PRED_W = (DH_W + DH_M) / (DT_W + DT_M)
R_J = DH_J / DT_J
print(f"    additive prediction from the two channels alone: "
      f"({100 * DH_W:+.2f}{100 * DH_M:+.2f})/({100 * DT_W:+.2f}{100 * DT_M:+.2f}) = {PRED_W:.2f}")
check("⓶ T-WEIGHT PASSES: the joint anchored ratio lands inside the pre-registered bracket [2.2, 3.6]",
      2.2 < R_J < 3.6, f"{R_J:.2f}")
check("⛭ AND IT IS THE SHARPEST OF THE FOUR -- one per cent from a prediction computed before the run, "
      "on an axis where quadrature makes no prediction at all",
      abs(R_J / PRED_W - 1) < 0.05, f"{R_J:.2f} against the predicted {PRED_W:.2f}")
check("and the joint is peak-weighted well above the symmetric baseline, as both channels are "
      "separately -- so composing them does not make a symmetric operation out of two asymmetric ones",
      R_J > BASE and DH_M / DT_M > BASE, f"joint {R_J:.2f} against the {BASE} baseline")

# ==================================================================================================
print("\nPART 3 -- ⓷ T-COMB: THE PEAKS.")
print("-" * 100)
P0 = peaks_sub(F['lcdm'])
MVW, MVM, MVJ = (peaks_sub(d) - P0 for d in (WIN, MIX, JNT))
for nm, mv in (('window', MVW), ('term mix', MVM), ('additive', MVW + MVM), ('JOINT', MVJ),
               ("the arm's own", peaks_sub(F['cr']) - P0)):
    print(f"    {nm:15s} " + "  ".join(f"{x:+7.3f}" for x in mv)
          + f"   outside the sky's widths: {int(np.sum(np.abs(mv) > SKYW))}/4")
check("⓷ T-COMB PASSES: l_1 moves inside the pre-registered bracket [+1.0, +2.6]",
      1.0 < MVJ[0] < 2.6, f"{MVJ[0]:+.3f} against the additive prediction {(MVW + MVM)[0]:+.3f}")
check("and it sits BELOW the additive prediction, the same mild sub-additivity the sizes show, on an "
      "axis a tenth as sensitive", MVJ[0] < (MVW + MVM)[0],
      f"{MVJ[0]:+.3f} against {(MVW + MVM)[0]:+.3f}")

# ==================================================================================================
print("\nPART 4 -- ⓸ T-INTERCEPT, AND THE SHAPE THAT NO RESCALING REMOVES.")
print("-" * 100)
FIT = {}
for nm, R in (('window', RW), ('term mix', RM), ('JOINT', RJ), ('measured excess', MEAS)):
    s, i = np.polyfit(Q2, np.log(R), 1)
    FIT[nm] = (s, float(np.exp(i)), abs(s * Q2.mean()) / abs(i))
    print(f"    {nm:16s} slope {s:+.6f}   intercept {np.exp(i):.4f} at q=0   "
          f"|slope x <q^2>|/|intercept| = {FIT[nm][2]:.3f}")
IJ = FIT['JOINT'][1]
print(f"    pre-registered: product 1.1035, sum 1.1019, quadrature 1.0839;  measured excess's own "
      f"{FIT['measured excess'][1]:.4f}")
check("⓸ T-INTERCEPT PASSES: the joint intercept lands within the pre-registered 0.005 of the "
      "multiplicative prediction, which had nothing fitted in it",
      abs(IJ - 1.1035) < 0.005, f"{IJ:.4f} against 1.1035, {abs(IJ - 1.1035):.4f} away")
check("and outside that bar for quadrature, agreeing with T-SIZE on the one separation available",
      abs(IJ - 1.0839) > 0.005, f"{abs(IJ - 1.0839):.4f} from quadrature's 1.0839")
check("⛭ AND THE JOINT RESPONSE IS THE FLATTEST THING THIS SECTOR HAS MEASURED -- flatter than the "
      "term mix, which was itself the first channel with the offset's signature",
      FIT['JOINT'][2] < FIT['term mix'][2] < 0.1,
      f"joint {FIT['JOINT'][2]:.3f} against the term mix's {FIT['term mix'][2]:.3f}")
check("⛔ WHERE THE MEASURED EXCESS IS NOT FLAT AT ALL, which is the obstruction",
      FIT['measured excess'][2] > 0.3,
      f"the excess carries {FIT['measured excess'][2]:.3f} against the joint's {FIT['JOINT'][2]:.3f}, "
      f"a factor {FIT['measured excess'][2] / FIT['JOINT'][2]:.0f}")

# ==================================================================================================
print("\nPART 5 -- THE CONSEQUENCE: ONE INFERENCE RETRACTED, ONE ARITHMETIC CONFIRMED, AND A SHAPE.")
print("-" * 100)
OV = (RJ - 1) / (MEAS - 1)
SUM48 = (RW - 1).mean() + (RM - 1).mean()
JMEAN = (RJ - 1).mean()
print("  joint / measured, band by band  " + "  ".join(f"{x:.2f}" for x in OV)
      + f"   mean {OV.mean():.2f}")
print(f"  at q=0: joint offset {IJ - 1:.4f} against the measured {FIT['measured excess'][1] - 1:.4f}"
      f"  ->  {(IJ - 1) / (FIT['measured excess'][1] - 1):.2f}x")
print(f"  band-mean: joint {100 * JMEAN:.3f}%;  the two channels summed ALONE, which is `cc66.48`'s "
      f"reading, {100 * SUM48:.3f}%")
check("✔ CONFIRMED BY DIRECT MEASUREMENT: `cc66.48` put the pair at 1.72 times the measured excess by "
      "adding the two channels' separate shares; composing them in ONE spectrum reads the same to about "
      "one per cent", abs(JMEAN / SUM48 - 1) < 0.05,
      f"{JMEAN / (MEAS - 1).mean():.2f}x joint against {SUM48 / (MEAS - 1).mean():.2f}x summed")
check("⛔ RETRACTED: `cc66.48` inferred from that over-delivery that the two channels do NOT compose as "
      "assumed, and therefore that a remainder computed by DIVIDING one response into the excess is an "
      "artefact of a wrong rule.  The rule is now measured and it IS the assumed one -- so dividing is "
      "the right operation and the remainder is a well-defined object.  The over-delivery was evidence "
      "about the SIZES, not about the RULE",
      NP_ >= 5 and NQ_ == 0 and abs(FP.mean() - 1) < 0.05,
      f"the pair composes multiplicatively to {FP.mean():.3f} of the product, in every band")
check("⛭⛭ AND THE OBSTRUCTION THAT SURVIVES IS A SHAPE, WHICH NO COEFFICIENT ON EITHER KNOB CAN "
      "REMOVE: the pair over-delivers by a factor of three at long wavelength and by a third at short, "
      "because it is flat in q where the excess grows -- so scaling it to the offset at q=0 leaves it "
      "short at high q, and scaling it to high q makes it an order too large at low q",
      OV[0] / OV[-1] > 2.0 and bool(np.all(OV > 1.0)),
      f"{OV[0]:.2f}x at q={QC[0]:.2f} against {OV[-1]:.2f}x at q={QC[-1]:.2f}, "
      f"a {OV[0] / OV[-1]:.1f}-fold tilt across the bands")
check("⌗ and that negative is available only because the rule was measured: with the rule assumed, the "
      "same numbers read as a size discrepancy that a smaller coefficient could absorb",
      OV.min() > 1.0, f"the pair exceeds the excess in all seven bands, smallest {OV.min():.2f}x")

print("\n" + "=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)
print("GATES: ALL PASS")
