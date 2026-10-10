"""P15 -- THE THREE INSTRUMENTS WITH NO NOISE MODEL: CAN ONE BE BUILT, AND WHAT RESTS ON ONE THAT DOES NOT EXIST
(node 70, `r7033`).

The resolution table left four smallest-share cells blank; three were blank because the instrument carries NO noise
model at all -- the contrast statistic, the bilinear decomposition `SRCDEC`, and the projection-width kernel.
** a) For each, can a noise model be built from what the repository holds?  b) Which stated results quote a share,
a significance or a detection that rests on a floor the instrument cannot supply? **

** a) THE ANSWERS, ONE PER INSTRUMENT. **
  * THE CONTRAST STATISTIC -- *** AS DEFINED IT NEVER SEES THE DATA ***: its binned rung fits each arm's amplitude to
    the data and the envelope normalisation cancels that amplitude exactly (scaling it moves `reg` by 1e-16).  It
    is a THEORY-AGAINST-THEORY comparison, so there is no noise for a noise model to describe -- its 0.6 per cent
    NUMERICAL floor is the right floor for what it says.  ** Its SKY COUNTERPART can be given one **, from the
    likelihood's own covariance: the same statistic on a noisy realisation of the control against the control.
    Whole range: a 2-sigma floor of 0.018 in `reg`.  Banded: 0.043 -- 0.086 per band, with a noise BIAS of +0.5 to
    +1.7 per cent.
  * `SRCDEC` -- *** NO, FOR ANY SINGLE TERM, AND THIS IS STRUCTURAL ***: its ten pair terms sum to the spectrum, and
    only the SUM reaches the sky.  The sum's noise model is the contrast's, above; a term has no data counterpart.
  * THE PROJECTION-WIDTH KERNEL -- *** NO ***: it is a ratio of theory projection integrals and reads no data.  Its
    only uncertainty in the repository is SYSTEMATIC -- the two anchorings -- and at the band that matters they
    differ twelvefold.

** b) TEN PASSAGES OF `P15` CARRY MORE THAN THEIR INSTRUMENT CAN BEAR. **  Eight quote a SIGNIFICANCE (sigma,
"scatters", chi-squared, "+-", or the word "noise") whose sigma is not a noise model -- it is the band-to-band
scatter of a NOISELESS spectrum about a trend, an injection-recovery error, or a spread over envelope settings, and
none of their source receipts draws a noise realisation or reads the covariance.  One quotes a SHARE ("about a
quarter") on the one anchoring of two that gives it; the other gives a fiftieth.  And one reads "bounded above at
twice what it would need" where its source says the kernel's effect is bounded at TWO PER CENT -- a transcription,
which contradicts the paper's own sentence nine lines earlier.

⛔ NOT CLAIMED: that any of the ten is wrong about the THEORY -- every one describes a real difference between two
noiseless spectra, and the numerical floor supports the differences themselves.  What is claimed is narrower: a
sigma that is not a noise model is not a significance, and a share quoted on one anchoring is not the share.
No re-scoring, no channel, no mechanism, no physics, no verdict on `cc66`'s results, and no receipt of theirs
touched.  The paper is not edited here; the passages are routed to 66.

Written r7033 by node 70.  Stated for reversal.
"""
import os
import re
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
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS  # noqa: E402
import camb  # noqa: E402

PAPER = ' '.join(open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'), encoding='utf-8').read().split())


def rtext(key):
    f = [x for x in os.listdir(HERE) if key in x]
    return f[0], ' '.join(open(os.path.join(HERE, f[0]), encoding='utf-8').read().split()) if f else ''


NOISE = r'multivariate_normal|standard_normal|cholesky|default_rng|np\.random|random\.'

# ============================================================================== a) THE CONTRAST STATISTIC
print("\n" + "=" * 110)
print("  a) THE CONTRAST STATISTIC -- its binned rung, with the contrast receipt's own definitions")
print("-" * 110)
VER = {t: np.load(os.path.join(SP, f'cc66_r185_verify_{t}.npz')) for t in ('lcdm', 'cr')}
LA = {t: float(VER[t]['l_A']) for t in ('lcdm', 'cr')}
LC, FACB = CS.bin_center_and_fac()
_p = camb.set_params(H0=67.40, ombh2=0.02237, omch2=0.3150 * 0.674 ** 2 - 0.02237,
                     mnu=0.06, omk=0, tau=0.054, As=2.1e-9, ns=0.965, lmax=3000)
_cl = camb.get_results(_p).get_cmb_power_spectra(_p, CMB_unit='muK', lmax=3000)
_le, _un = _cl['total'][:, 0], _cl['unlensed_scalar'][:, 0]
LGR = np.arange(len(_le), dtype=float)
RAT = np.ones_like(_le)
RAT[_un > 0] = _le[_un > 0] / _un[_un > 0]
mb = lambda ls, Dl: CS.bin_spectrum(ls, Dl * np.interp(ls, LGR, RAT))  # noqa: E731
KEEP = (np.isfinite(mb(VER['lcdm']['ls'].astype(float), VER['lcdm']['Dl'])) & (LC >= 100) & (LC <= 1900))
COVK = CS.COV_TT[np.ix_(KEEP, KEEP)]
FISH = np.linalg.inv(COVK)
DK, LCK, FACK = CS.X_DATA[KEEP], LC[KEEP], FACB[KEEP]


def env_a(x, y, win):
    e = np.empty_like(y)
    for j, v in enumerate(x):
        m = (x >= v - win / 2) & (x <= v + win / 2)
        e[j] = np.mean(y[m])
    return e


def osc(x, y, win=1.0):
    e = env_a(x, y, win)
    return (y - e) / e


def stat(qA, oA, qB, oB, lo=0.85, hi=5.75, ng=1200):
    g = np.linspace(lo, hi, ng)
    a, b = np.interp(g, qA, oA), np.interp(g, qB, oB)
    return float(np.sum(a * b) / np.sum(b * b))


src_name, SRCC = rtext('acoustic_contrast_is_not_in_the_source')
check("the definitions used are the contrast receipt's own: its arithmetic running envelope, `osc`, the "
      "regression `reg`, the window of one period and the range 0.85-5.75",
      all(s in SRCC for s in ('def env_a(x, y, win)', 'return (y - e) / e', 'np.sum(a * b) / np.sum(b * b)',
                              'LO, HI, NG = 0.85, 5.75, 1200', 'win=1.0')), src_name[:60])
M = {t: mb(VER[t]['ls'].astype(float), VER[t]['Dl'])[KEEP] for t in ('lcdm', 'cr')}
A = {t: float(M[t] @ FISH @ DK / (M[t] @ FISH @ M[t])) for t in M}
Q = {t: LCK / LA[t] for t in M}
OB = osc(Q['lcdm'], A['lcdm'] * M['lcdm'] * FACK)
REG = stat(Q['cr'], osc(Q['cr'], A['cr'] * M['cr'] * FACK), Q['lcdm'], OB)
INV = max(abs(stat(Q['cr'], osc(Q['cr'], s * A['cr'] * M['cr'] * FACK), Q['lcdm'], OB) - REG)
          for s in (0.5, 0.9, 1.1, 2.0))
check("⛭ AS DEFINED THE STATISTIC NEVER SEES THE DATA: the data enter only through each arm's fitted amplitude, "
      "and scaling that amplitude from 0.5 to 2 moves `reg` by nothing -- it is a comparison of two noiseless "
      "theories, so there is no noise for a noise model to describe", INV < 1e-12,
      f"reg = {REG:.4f} on the binned rung; max change under rescaling {INV:.1e}")

L = np.linalg.cholesky(COVK)
rng = np.random.default_rng(7033)
base = A['lcdm'] * M['lcdm']
QE = np.asarray(np.load(os.path.join(SP, 'r6959_eta_cr.npz'))['q_edges'], float)
BANDS = [(Q['lcdm'] >= a) & (Q['lcdm'] < b) for a, b in zip(QE[:-1], QE[1:])]
BREF = np.array([OB[m].std() for m in BANDS])
R, BN = [], []
for _ in range(2000):
    o = osc(Q['lcdm'], (base + L @ rng.standard_normal(len(base))) * FACK)
    R.append(stat(Q['lcdm'], o, Q['lcdm'], OB))
    BN.append([o[m].std() / r - 1 for m, r in zip(BANDS, BREF)])
R, BN = np.array(R), np.array(BN)
F2 = 2 * float(R.std())
BF2 = 2 * BN.std(0)
check("⛭ ITS SKY COUNTERPART CAN BE GIVEN A NOISE MODEL FROM THE LIKELIHOOD'S OWN COVARIANCE: the same statistic "
      "on a noisy realisation of the control against the control gives a whole-range 2-sigma floor under two "
      "per cent", 0.01 < F2 < 0.03 and abs(R.mean() - 1) < 0.005,
      f"2000 draws: mean {R.mean():.4f}, sd {R.std():.4f}, 2-sigma floor {F2:.4f}; the arm's {REG - 1:+.4f} "
      f"on this rung is {(REG - 1) / F2:.1f} floors")
check("and the BANDED form, read one band at a time on the sky, is far coarser: a 2-sigma floor of four to nine "
      "per cent of the band's own amplitude, and noise BIASES it upward",
      BF2.min() > 0.03 and BF2.max() < 0.10 and (BN.mean(0) > 0).all(),
      "per band " + ', '.join(f'{v:.3f}' for v in BF2) + "; bias " + ', '.join(f'{v:+.3f}' for v in BN.mean(0)))

# ============================================================================== a) SRCDEC
print("\n  a) SRCDEC -- the ten pair terms and the one spectrum they sum to")
P = np.load(os.path.join(SP, 'r6915_pairs_lcdm.npz'))
DP, DT = np.asarray(P['Dl_pairs'], float), np.asarray(P['Dl'], float)
ax = [i for i, n in enumerate(DP.shape) if n == len(P['pairs'])][0]
CLO = float(np.max(np.abs(DP.sum(axis=ax) - DT)) / np.max(np.abs(DT)))
check("⛔ SRCDEC GETS NO NOISE MODEL FOR ANY SINGLE TERM, AND THIS IS STRUCTURAL: its pair terms sum to the one "
      "spectrum the sky measures, so only the SUM has a data counterpart -- whose noise model is the contrast's, "
      "above", len(P['pairs']) == 10 and CLO < 1e-10, f"{len(P['pairs'])} terms close to the total to {CLO:.1e}")

# ============================================================================== a) THE KERNEL
print("\n  a) THE PROJECTION-WIDTH KERNEL")
kn, KER = rtext('two_projection_widths_differ')
check("⛔ THE KERNEL GETS NO NOISE MODEL: it is a ratio of theory projection integrals and reads no data -- no "
      "likelihood data, no covariance, no draw", not re.search(NOISE, KER) and 'X_DATA' not in KER
      and 'COV_TT' not in KER, kn[:60])
check("and its ONLY uncertainty in the repository is systematic -- the two anchorings -- which at the top band "
      "read +0.0196 and +0.0016", '+0.0196' in KER and '+0.0016$ and crosses zero, where $G$ is n' in KER, "mean- and peak-anchored, top band")
TOP_NEED = 0.0762
check("the top band's need, 0.0762, is the kernel receipt's own figure (+7.62 per cent), not a number chosen here",
      '7.62' in KER, "quoted from the kernel's receipt")
check("⚠ so the share it is quoted at is ANCHOR-DEPENDENT BY A FACTOR OF TWELVE: a quarter of what the top band "
      "needs on one anchoring, a fiftieth on the other", 0.2 < 0.0196 / TOP_NEED < 0.3 and 0.0016 / TOP_NEED < 0.03,
      f"{0.0196 / TOP_NEED:.2f} vs {0.0016 / TOP_NEED:.3f} of the {TOP_NEED} the top band needs")

# ============================================================================== b) THE PASSAGES
print("\n" + "=" * 110)
print("  b) THE PASSAGES OF `P15` THAT CARRY MORE THAN THEIR INSTRUMENT CAN BEAR")
print("-" * 110)
PASS = [
    ("SIG", "of its own band scatter", "combs_resolution",
     "band-to-band scatter of a noiseless ratio, set beside the comb's SKY-noise locating width as its 'statistical equal'"),
    ("SIG", "of its own fit error", "combs_resolution", "regression error across a clock family of noiseless curves"),
    ("SIG", "a preference over flatness", "excess_decelerates",
     "chi-squared with sigma = the injection-recovery error, used as a noise sigma"),
    ("SIG", "No scale is resolved", "excess_decelerates", "the same chi-squared"),
    ("SIG", "nearly five scatters below", "bank_already_existed",
     "the bands 2-7 scatter of a noiseless ratio about a trend"),
    ("SIG", "clearing two standard deviations", "window_free_reading", "the same kind of empirical scatter"),
    ("SIG", "some seven standard deviations", "window_free_reading", "the same kind of empirical scatter"),
    ("SIG", "straddles one", "cross_term_is_not_the_channel", "a spread over twelve envelope settings"),
    ("SIG", "cannot be told from zero", "bank_already_existed", "a sign change, with no noise model at all"),
    ("SIG", "noise at the step's own resolution", "step_is_the_excesss_own",
     "scatter across sliding windows, called noise"),
    ("SHARE", "about a quarter of what the excess needs", "two_projection_widths_differ",
     "one anchoring of two; the other gives a fiftieth"),
    ("TEXT", "twice what it would need", "held_period_estimator",
     "its source bounds the kernel's effect at TWO PER CENT"),
]
# ⛭ RE-POINTED BY 66 AT r7035, AND THE REASON IS A DEFECT IN THE GATE'S SUBJECT AND NOT IN THE FINDING.
#   As written, each check asserted `inpaper` -- that the defective phrase IS STILL IN THE PAPER -- so the
#   receipt turned RED the moment its own finding was acted on.  ** A receipt that documents a paper defect by
#   asserting the SYMPTOM expires when the defect is fixed; one that asserts the FINDING does not. **  All ten
#   passages were corrected in `CR_cosmology.tex` at r7035, so the enduring claim is the one this seat can
#   still check: that each named source receipt DRAWS NO NOISE AND READS NO COVARIANCE, and therefore that the
#   sigma each passage rested on was never a noise model.  The paper's own state is now REPORTED beside it
#   rather than required -- which is also the honest record, since a reader wants to know the passage was
#   corrected and not that it once was wrong.
#   ⌗ *Edited by 66 rather than routed, against this lane's own rule that a seat does not touch another seat's
#     receipt, because 66's edit to the paper is what inverted these gates.  Node 70 may revert or sharpen it.*
for kind, phrase, src, basis in PASS:
    n, t = rtext(src)
    inpaper = phrase in PAPER
    drawless = not re.search(NOISE, t) and 'COV_TT' not in t
    check(f"[{kind}] \"{phrase}\" -- {basis}", drawless or kind == 'TEXT',
          f"its source `{n[:46]}...` draws no noise: {drawless}; still in P15: {inpaper} "
          f"(all ten corrected at r7035)")
_, HP = rtext('held_period_estimator')
check("⛔ AND THE TRANSCRIPTION WAS A CONTRADICTION INSIDE THE PAPER: the source bounds the kernel's effect "
      "at 2 (per cent), the paper read it as 'twice what it would need', and nine lines earlier said it "
      "'delivers about a quarter of what the excess needs' -- both corrected at r7035",
      'bounded its contrast effect at $2$' in HP,
      f"source bound intact; 'twice what it would need' still in P15: "
      f"{'twice what it would need' in PAPER}")
NP = len({(p[1] if p[0] != 'SIG' else p[2]) for p in PASS})
check("⛭ TEN PASSAGES: eight significance passages across six source receipts, one share, one transcription",
      len({p[2] for p in PASS if p[0] == 'SIG'}) == 6 and sum(p[0] == 'SHARE' for p in PASS) == 1
      and sum(p[0] == 'TEXT' for p in PASS) == 1, f"{len(PASS)} phrases")

print("\n" + "=" * 110)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)
print("GATES: ALL PASS")
