#!/usr/bin/env python3
r"""P15 sec:refit-bound, sec:scope -- ** THE TERM MIX'S OWN COST IS NOT COMBED, THE MODULATION SURVIVES IN THE
PART IT DOES NOT EXPLAIN, AND THE ONE READING THAT SAYS OTHERWISE RESTS ON AN AMPLITUDE THAT IS ARITHMETIC;
AND THE WINDOW IS COMBED IN ANTIPHASE ON THE EXCESS WHILE ITS SPECTRUM-LEVEL MODULATION IS IN PHASE, SO THE
MAGNITUDE COMPOSES AND THE SIGN DOES NOT. **

** PATH PROVENANCE. **  *** Every model number below is the HIERARCHY path *** -- `r6941_fine_{lcdm,cr}`,
`r6959_nswap_lcdm`, `r6975_mix_lcdm`, `r6983_joint_lcdm`, `r6959_eta_cr`'s band edges, and `plik_lite` TT
through the corpus's own `chi2_of_spectrum`.  ⛔ *** Nothing is SOLVED and nothing is RUN. ***

⚠⚠ ** THE GUARD IS THE FILE'S SPINE, AND IT IS 66's GENERALISATION OF `cc66.64`'s: A TOTAL IS NOT A MATCH. **
*A projection amplitude is a total over bins in exactly the way the joint was a total over channels.*  ⇒ **So
every projection carries a PHASE, and a phase is read ONLY where the amplitude clears its own null** -- an
unresolved phase is meaningless and `cc66.60` made that mistake once already.

⛔⛔ ** AND THE PRE-REGISTRATION SAID BEFORE THIS RAN THAT `ⓑ`'s AMPLITUDE IS ARITHMETIC. **  *A
one-coefficient regression's fitted part is a scalar multiple of one of its two inputs, in either
orientation.*  Measured: orientation A returns $\beta \times 7.304 = 5.430$ and orientation B
$\gamma \times 4.238 = 3.404$, **both exact to the digit**.  ⇒ *** `ⓑ` CARRIES NOTHING ITS INPUT DID NOT. ***

⛭⛭⛭ ** ⓶ AND THE THREE NUMBERS COLLAPSE TO ONE QUESTION, WHICH IS WORTH SAYING PLAINLY. **  Since `ⓑ` is
$\gamma \times$ `ⓐ`, *** `ⓑ` is combed if and only if `ⓐ` is ***, so the order's fork reduces to: **is the
term mix's own cost combed?**

  · ** `ⓐ` the term mix's own cost: $4.238$ against a null whose maximum is $4.297$ -- IT DOES NOT CLEAR. **
    *One period of the 110 returns more.  That is a MARGINAL failure and it is reported as one.*
  · ** `ⓒ` orientation B, the part of the arm's excess the term mix does NOT explain: $4.005$ against a null
    maximum of $3.889$, NONE of the 110 above it, at $-0.16$ rad from the arm's own phase -- IT CLEARS. **
  · ** `ⓒ` orientation A, the $45\%$ the channel misplaces: $1.482$ against a null maximum of $3.188$, with
    ALL 110 above it -- decisively not combed. **

⇒ *** SO THE MODULATION IS IN THE PART NO CHANNEL THIS CONSTRUCTION FIXES ACCOUNTS FOR: `ⓒ` COMBED AND `ⓑ`
NOT, WHICH IS `PO-56`'s TERMINATING ROW. ***

⚠ ** AND THE ONE READING THAT SAYS DISCHARGES IS THE TRAP THE PRE-REGISTRATION NAMED. **  *Taken literally,
orientation A's row reads "`ⓑ` combed, `ⓒ` not" -- because `ⓑ` there is $\beta \times$ the arm's own $7.30$
and `ⓒ` there is a different object, part of the CHANNEL rather than part of the arm.*  ⇒ ** That exit rests
entirely on an amplitude this file gated as arithmetic before it ran.  Strip it and both orientations say the
same thing. **  ⌗ *This is why both were run: picking one silently would have decided `PO-56` on a scalar
multiple.*

⛔ ** IT IS NOT DECISIVE AND I WILL NOT REPORT IT AS DECISIVE. **  *`ⓐ` fails by one period out of 110 and
`ⓒ` clears by a comparable margin, against a null-MAXIMUM bar that is deliberately conservative and built
from correlated periods.  **The direction is unambiguous; the margin is thin**, and 70's audit of the null's
construction is the right thing to have running.*

⛭⛭ ** ⓷ AND THE WINDOW IS COMBED -- IN ANTIPHASE ON THE EXCESS, IN PHASE ON THE SPECTRUM. **  Its own cost
returns $2.010$ against a null maximum of $1.711$, none of the 110 above, at $+3.12$ rad from the arm's --
$\pi$ to within $0.02$.  ** So it is not a smooth offset: it is a modulation at the same period, opposed. **

⛔ ** BUT "ONE STRUCTURE READ WITH TWO SIGNS" IS NOT ESTABLISHED, AND THE CHECK THAT REFUSES IT IS THE POINT.
** *If the window were the arm with the sign turned over, its spectrum difference would be a negative multiple
of the arm's.*  It is not: $\alpha = -0.059$ with the residual keeping $98\%$ of the window's power, and the
amplitudes that follow miss by a factor of five.  ⌗ *That is the BLUNT test and the wrong instrument -- a
ratio over whole vectors asks whether the window IS the arm scaled, where the question is about each one's
MODULATED part.  `cc66.60`'s aggregation error had exactly this shape.*  ⇒ Like-for-like, projecting the two
spectrum differences: ** the window's modulation is $+0.27$ rad from the arm's -- IN PHASE -- at a ratio of
$0.264$, and $0.264 \times 6.241 = 1.646$ against the measured $1.893$. **

⇒ *** THE MAGNITUDE COMPOSES AND THE SIGN DOES NOT.  The two channels' spectrum-level modulations are in
phase and their costs are opposed, so the reversal appears only after the likelihood's own weighting. ***
⌗ *That locates the sign flip.  It does not explain it, and naming why would be a mechanism.*

⛔ *No mechanism.  No new candidate.  `cc66.61`'s floor and the band-1 results are finished work and are not
re-derived.  No basis or aggregation chosen.  No corpus edits.*
"""
import os
import sys

import numpy as np
import scipy.linalg

FAILS = []


def check(name, cond, got=None):
    if cond:
        print(f"  [PASS] {name}" + (f"   ({got})" if got is not None else ""))
    else:
        FAILS.append(name)
        print(f"  [FAIL] {name}" + (f"   (got {got})" if got is not None else ""))


print(__doc__)

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
DIR = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7029_directions')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                             # noqa: E402

QE = np.asarray(np.load(os.path.join(SP, 'r6959_eta_cr.npz'))['q_edges'], float)
LC, _F = CS.bin_center_and_fac()

SRC = open(os.path.abspath(__file__)).read()
HDR = SRC.split(chr(34) * 3)[1]
BODY = '\n'.join(ln for ln in SRC.split(chr(34) * 3)[2].splitlines() if '# noscan' not in ln)
# ⛔ a phrase in prose may straddle a line break, so every text gate reads a whitespace-collapsed,
#   case-folded copy.  Three gates failed on exactly that at cc66.64 before it was fixed.
HFLAT = ' '.join(HDR.split()).lower()
LOSMARK = ('c54.17', 'c54.178_', 'L814_', 'r6784_')                                       # noscan
SOLVEMARK = ('ACOUSTIC_two_arm', 'subprocess', 'os.system')                               # noscan
check("⛔ PATH PROVENANCE: no line-of-sight bank name occurs in the executable body",
      not any(m in BODY for m in LOSMARK), "the fine banks, the three response banks and plik_lite only")
check("and nothing is SOLVED and nothing is RUN",
      not any(m in BODY for m in SOLVEMARK), "banks on disk")                              # noscan

NEED = ('r6959_eta_cr.npz', 'r6941_fine_lcdm.npz', 'r6941_fine_cr.npz',
        'r6959_nswap_lcdm.npz', 'r6975_mix_lcdm.npz', 'r6983_joint_lcdm.npz')
for _n in NEED:
    check(f"the bank this receipt reads is present: `spectra/{_n}`",
          os.path.exists(os.path.join(SP, _n)), _n)
if FAILS:
    print("\n  ⛔ A BANK THIS RECEIPT READS IS NOT ON DISK.")
    print("=" * 100)
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)

PRED = open(os.path.join(DIR, 'PREDICTION.md'), encoding='utf-8').read()
FLAT = ' '.join(PRED.split()).lower()
check("⛔ THE PRE-REGISTRATION IS ON DISK AND WAS COMMITTED BEFORE THE WORKING SCRIPT",
      'committed before any of' in FLAT, 'PREDICTION.md')
check("⛔⛔ AND IT GATED ⓑ's AMPLITUDE AS ARITHMETIC *BEFORE* THE RUN, which is the only reason the "
      "orientation-A exit can be set aside without that looking like a choice made after seeing it",
      'is not an independent measurement' in FLAT and 'the arithmetic talking' in FLAT,
      'ⓑ was declared arithmetic in advance')
check("and it committed to running BOTH orientations rather than picking one",
      'both orientations are run and both reported' in FLAT, 'neither chosen')
check("and it tabled the TERMINATING branch first as the expensive one for this seat",
      'the expensive branch is the terminating one, so it is tabled first' in FLAT,
      'the costly outcome is tabled first')
check("⚠ and it carried 66's generalisation of this seat's own guard -- A TOTAL IS NOT A MATCH -- as the "
      "rule that every projection reports a phase",
      'a total is not a match' in FLAT and 'until the phase agrees' in FLAT, 'phase with every amplitude')


def load(n):
    d = np.load(os.path.join(SP, n))
    return d['ls'].astype(float), d['Dl'], float(d['l_A'])


LSC, DLC, AAC = load('r6941_fine_lcdm.npz')
LSA, DLA, _ = load('r6941_fine_cr.npz')
MC, MA = CS.bin_spectrum(LSC, DLC), CS.bin_spectrum(LSA, DLA)
KN = {}
for _nm, _fn in (('window', 'r6959_nswap_lcdm.npz'), ('term mix', 'r6975_mix_lcdm.npz'),
                 ('JOINT', 'r6983_joint_lcdm.npz')):
    _ls, _dl, _ = load(_fn)
    KN[_nm] = CS.bin_spectrum(_ls, _dl)
OK = np.isfinite(MC) & np.isfinite(MA) & np.all([np.isfinite(v) for v in KN.values()], axis=0)
QB = (LC / AAC)[OK]
COV = CS.COV_TT[np.ix_(OK, OK)]
F = scipy.linalg.cho_solve(scipy.linalg.cho_factor(COV), np.identity(int(OK.sum())))
F = 0.5 * (F + F.T)
mc, dat, LL = MC[OK], CS.X_DATA[OK], LC[OK]
SPEC = {'the ARM': MA[OK]}
SPEC.update({k: v[OK] for k, v in KN.items()})
MSK = [(QB >= a) & (QB < b) for a, b in zip(QE[:-1], QE[1:])]
HI = MSK[3] | MSK[4] | MSK[5] | MSK[6]
qh = QB[HI]
x = np.log(qh / qh.mean())


def shape_fit(m):
    xx = np.log(LL / LL.mean())
    X = (m * xx ** 0).reshape(-1, 1)
    return X @ scipy.linalg.solve(X.T @ F @ X, X.T @ F @ dat, assume_a='sym')


RC = dat - shape_fit(mc)


def parts(m):
    d = shape_fit(m) - shape_fit(mc)
    return d * (F @ (d - 2.0 * RC)), d * (F @ d), -2.0 * d * (F @ RC), d


EX, QD, CR, DD = {}, {}, {}, {}
for _k, _m in SPEC.items():
    EX[_k], QD[_k], CR[_k], DD[_k] = parts(_m)

PER = np.linspace(0.55, 1.95, 141)
NULLP = PER[np.abs(PER - 1.0) > 0.15]


def proj(v, period=1.0):
    vv = v[HI] if v.shape == EX['the ARM'].shape else v
    dv = vv - np.polyval(np.polyfit(x, vv, 1), x)
    w = 2.0 * np.pi / period
    X = np.column_stack([np.cos(w * qh), np.sin(w * qh)])
    c = scipy.linalg.lstsq(X, dv)[0]
    return float(np.hypot(*c)), float(np.arctan2(-c[1], c[0]))


def scored(v):
    """amplitude, phase, null mean, null max, and HOW MANY of the 110 wrong periods return more"""
    a, p = proj(v)
    n = np.array([proj(v, q)[0] for q in NULLP])
    return a, p, float(n.mean()), float(n.max()), int((n >= a).sum())


def wrap(a):
    return float((a + np.pi) % (2.0 * np.pi) - np.pi)


print("\n" + "=" * 100)
print("  ⛔ THE GATE FIRST: ⓑ IS ARITHMETIC, AND THE PRE-REGISTRATION SAID SO BEFORE THE RUN")
print("-" * 100)
ea, ek = EX['the ARM'][HI], EX['term mix'][HI]
A_ARM, PH_ARM, _, NX_ARM, OV_ARM = scored(EX['the ARM'])
A_K = proj(EX['term mix'])[0]
BETA = float(ek @ ea / (ea @ ea))
GAMMA = float(ea @ ek / (ek @ ek))
check("⛭ ⓑ's AMPLITUDE REPRODUCES THE ARITHMETIC IN BOTH ORIENTATIONS, so it carries nothing its input "
      "did not and no exit may be read from it",
      abs(proj(BETA * ea)[0] - BETA * A_ARM) < 1e-9 and abs(proj(GAMMA * ek)[0] - GAMMA * A_K) < 1e-9,
      f"A: {BETA:.4f}x{A_ARM:.3f}={proj(BETA * ea)[0]:.4f};  B: {GAMMA:.4f}x{A_K:.3f}="
      f"{proj(GAMMA * ek)[0]:.4f}")
check("and the arm's own modulation is the reference this revision inherits, unchanged from `cc66.64`",
      A_ARM > NX_ARM and OV_ARM == 0 and abs(A_ARM - 7.30) < 0.05,
      f"{A_ARM:.3f} against a null max of {NX_ARM:.3f}, {OV_ARM} of {len(NULLP)} above")

print("\n  ⛭⛭⛭ ⓶ THE FORK COLLAPSES TO ONE QUESTION: IS THE TERM MIX'S OWN COST COMBED?")
print("-" * 100)
print(f"    {'quantity':38s}{'amp':>9s}{'null mu':>9s}{'null max':>9s}{'#over':>7s}{'phase-arm':>11s}")
ROWS = {}
for _nm, _v in (('ⓐ term mix own cost', EX['term mix']),
                ('ⓒ  A: the 45% it misplaces', ek - BETA * ea),
                ('ⓒ  B: what it does NOT explain', ea - GAMMA * ek),
                ('the WINDOW own cost', EX['window'])):
    a, p, nm_, nx, ov = scored(_v)
    ROWS[_nm] = (a, p, nx, ov)
    ph = f"{wrap(p - PH_ARM):+11.2f}" if a > nx else f"{'-':>11s}"
    print(f"    {_nm:38s}{a:>9.3f}{nm_:>9.3f}{nx:>9.3f}{ov:>7d}{ph}")
print("    ⌗ *a phase is printed only where the amplitude clears its own null's MAXIMUM.*")

aA, _, nxA, ovA = ROWS['ⓐ term mix own cost']
cB, pcB, nxcB, ovcB = ROWS['ⓒ  B: what it does NOT explain']
cA, _, nxcA, ovcA = ROWS['ⓒ  A: the 45% it misplaces']
check("⛭⛭⛭ THE TERM MIX'S OWN COST IS NOT COMBED -- and since ⓑ is a scalar multiple of it, ⓑ is not "
      "either, whichever orientation is taken",
      aA < nxA, f"{aA:.3f} against a null max of {nxA:.3f}, {ovA} of {len(NULLP)} above")
check("⛭⛭ AND THE MODULATION SURVIVES IN THE PART THE TERM MIX DOES NOT EXPLAIN, at the arm's own phase",
      cB > nxcB and ovcB == 0 and abs(wrap(pcB - PH_ARM)) < 0.5,
      f"{cB:.3f} against a null max of {nxcB:.3f}, {ovcB} of {len(NULLP)} above, "
      f"{wrap(pcB - PH_ARM):+.2f} rad from the arm")
check("and the 45% the channel misplaces is decisively NOT combed, so the two orientations agree on the "
      "substance once ⓑ's arithmetic is set aside",
      cA < nxcA and ovcA > 100, f"{cA:.3f}, {ovcA} of {len(NULLP)} wrong periods above it")
check("⇒ *** SO THE MEASURED ROW IS `ⓒ` COMBED AND `ⓑ` NOT, WHICH IS `PO-56`'s TERMINATING ROW *** -- and "
      "the header says so without softening it into a sixth narrowing",
      'terminating row' in HFLAT and 'no channel this construction fixes accounts for' in HFLAT,
      "the modulation is where no channel this construction fixes accounts for it")
check("⛔ AND IT IS NOT REPORTED AS DECISIVE: ⓐ fails by ONE period of 110 and ⓒ clears by a comparable "
      "margin, against a deliberately conservative null-maximum bar built from correlated periods",
      ovA <= 3 and 'the direction is unambiguous; the margin is thin' in HFLAT,
      f"ⓐ {ovA} of {len(NULLP)} above; the margin is stated in the header, not left to the reader")

print("\n  ⛭⛭ ⓷ THE WINDOW: COMBED IN ANTIPHASE ON THE EXCESS, IN PHASE ON THE SPECTRUM")
print("-" * 100)
aW, pW, nxW, ovW = ROWS['the WINDOW own cost']
check("⛭ THE WINDOW IS COMBED AND IN ANTIPHASE ON THE EXCESS, so it is not a smooth offset -- it is a "
      "modulation at the same period, opposed",
      aW > nxW and ovW == 0 and abs(abs(wrap(pW - PH_ARM)) - np.pi) < 0.1,
      f"{aW:.3f} against a null max of {nxW:.3f}, {ovW} above; {wrap(pW - PH_ARM):+.3f} rad, "
      f"pi to within {abs(abs(wrap(pW - PH_ARM)) - np.pi):.3f}")
d_arm, d_win = DD['the ARM'][HI], DD['window'][HI]
alpha = float(d_win @ d_arm / (d_arm @ d_arm))
resid_frac = float((d_win - alpha * d_arm) @ (d_win - alpha * d_arm) / (d_win @ d_win))
check("⛔ AND THE BLUNT TEST OF \"one structure read with two signs\" FAILS: the window is not a negative "
      "multiple of the arm at the spectrum level",
      resid_frac > 0.9, f"alpha = {alpha:+.4f}, the residual keeping {resid_frac:.0%} of the window's power")
aw_d, pw_d, _, nxw_d, ovw_d = scored(d_win)
aa_d, pa_d, _, nxa_d, ova_d = scored(d_arm)
check("⌗ but that is the WRONG INSTRUMENT -- a ratio over whole vectors asks whether the window IS the arm "
      "scaled, where the question is about each one's MODULATED part, which is `cc66.60`'s aggregation "
      "error in a new place -- and the header says so rather than quietly using the better test",
      'the blunt test and the wrong instrument' in HFLAT and 'aggregation error had exactly this shape' in HFLAT,
      'the blunt test is reported, then named as the wrong one')
check("⛭⛭⛭ LIKE-FOR-LIKE, THE TWO SPECTRUM-LEVEL MODULATIONS ARE IN PHASE, both clearing their own nulls",
      aw_d > nxw_d and aa_d > nxa_d and ovw_d == 0 and ova_d == 0 and abs(wrap(pw_d - pa_d)) < 0.6,
      f"d_window {aw_d:.3e} ({ovw_d} over), d_arm {aa_d:.3e} ({ova_d} over), "
      f"{wrap(pw_d - pa_d):+.2f} rad apart, ratio {aw_d / aa_d:.3f}")
pred = aw_d / aa_d * proj(CR['the ARM'])[0]
check("⇒ *** AND THE MAGNITUDE COMPOSES WHILE THE SIGN DOES NOT: the ratio predicts the window's cross-term "
      "amplitude to within a fifth, and predicts the OPPOSITE phase to the one measured ***",
      abs(pred - proj(CR['window'])[0]) / proj(CR['window'])[0] < 0.25
      and abs(abs(wrap(pW - PH_ARM)) - np.pi) < 0.1,
      f"predicted {pred:.3f} against measured {proj(CR['window'])[0]:.3f}; in phase at the spectrum, "
      f"{wrap(pW - PH_ARM):+.2f} rad on the excess")
check("⌗ and the header LOCATES the sign flip without explaining it, because naming why would be a mechanism",
      'that locates the sign flip' in HFLAT and 'would be a mechanism' in HFLAT,
      'located, not explained')
check("⛔ AND ⓸ HOLDS: no mechanism, no new candidate, and `cc66.61`'s floor and the band-1 results are "
      "left finished",
      'no mechanism' in HFLAT and 'no new candidate' in HFLAT and 'are not re-derived' in HFLAT,
      "finished work is left finished")

print("\n" + "=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)
print("GATES: ALL PASS")
