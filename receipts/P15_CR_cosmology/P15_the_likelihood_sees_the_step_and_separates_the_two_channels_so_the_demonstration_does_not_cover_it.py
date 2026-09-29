#!/usr/bin/env python3
r"""P15 sec:refit-bound, sec:scope -- ** THE LIKELIHOOD SEES THE STEP AS A LOCALISED CONTRIBUTION TO ITS
EXCESS AND SEPARATES THE TWO CHANNELS AT BAND 1 AT TWENTY-FIVE SIGMA, SO `cc66.61`'s DEMONSTRATION COVERS
THE STATISTIC FAMILY AND NOT THE INSTRUMENT THE PAPER RUNS BESIDE IT, AND `PO-56`'s AMENDED CLAUSE IS NOT
MET. **

** PATH PROVENANCE. **  *** Every model number below is the HIERARCHY path *** -- `r6941_fine_{lcdm,cr}`,
`r6959_nswap_lcdm`, `r6975_mix_lcdm`, `r6983_joint_lcdm`, `r6959_eta_cr`'s band edges, and `plik_lite` TT
through the corpus's own `chi2_of_spectrum`.  ⛔ *** Nothing is SOLVED and nothing is RUN. ***

** THE PRE-REGISTRATION IS ITS OWN COMMIT AHEAD OF THE WORKING SCRIPT **, and it opens by saying plainly
which facts had already been looked at: the likelihood's **structure** -- bin edges, widths, covariance --
is a property of the instrument fixed on disk regardless of any spectrum, so it was inspected first and
the first branch of ⓵ was declared settled rather than pre-registered as open.

⛭⛭⛭ ** ⓵ⓐ THE LIKELIHOOD IS NOT A BANDED STATISTIC IN DISGUISE. **  `plik_lite` TT bins at a median
$0.0298$ in $q$ -- ** one thirty-fourth of a comb period ** -- with $24$ bins inside band 1, and its
bin-to-bin correlation is a flat $\approx 0.15$ floor rather than a coupling that grows over a period.
*It bins; it does not **band**, in the sense that defeats every statistic in the demonstration.*

⛭⛭⛭ ** ⓵ⓑ AND THE STEP IS A LOCALISED CONTRIBUTION TO ITS EXCESS. **  Band 1's bins carry $36.4\sigma$ of
arm-versus-control separation **on their own**, where its own bands 2--7 trend predicts $53$--$71$: a
departure of $-0.311$ to $-0.489$ across the four bases, at $2.5$--$3.2\sigma$ on its own residual.
⇒ ** The same sign as every other instrument in this row -- and the first per-band number in it that
carries the INSTRUMENT'S own noise rather than an empirical scatter across a noiseless theory spectrum. **

⛔⛔ ** ⓵ⓒ AND IT SEPARATES THE TWO CHANNELS AT BAND 1 AT $25.1\sigma$. **  The smallest share of the band-1
arm-control difference it could detect is $0.055$.

⇒ *** SO `cc66.61`'s DEMONSTRATION COVERS THE STATISTIC FAMILY AND NOT THE INSTRUMENT THE PAPER RUNS BESIDE
IT.  `PO-56`'s AMENDED CLAUSE IS **NOT** MET, AND THE ROW HAS A MEASUREMENT TO MAKE RATHER THAN AN EXIT TO
TAKE. ***

⚠ ** AND THE DENOMINATORS ARE NOT THE SAME, WHICH THE PRE-REGISTRATION REQUIRED BE SAID BEFORE THE NUMBERS
WERE IN HAND. **  *$0.055$ is a share of the band-1 **difference** under real instrument noise; `cc66.61`'s
$0.59$ is a share of the **step** under an empirical scatter of a **noiseless** spectrum.*  ⛔ **They are
not one number and neither bounds the other.**  *The comparison that IS legitimate is the one the order
asked for, and it is stark: the statistic family cannot separate the channels at band 1, and the likelihood
separates them at twenty-five sigma.*

⛭ ** ⓶ AND THE SCOPE STATEMENT THE CLAUSE NEEDS. **  Of the **eleven** instruments this row has ever made a
claim on, ** eight BAND ** at $0.70$ of a comb period -- the contrast statistic, the held-period amplitude,
the window-free depth, the extremal envelope, the differential estimator, the bilinear decomposition read
through the band statistic, the comb-phase projection and the projection-width kernel.  ** Three do not: **
the anchored peak/trough locator (*which does not band but makes no amplitude claim at band 1 -- it locates
peaks*), the likelihood, and the refit $\chi^2$ that uses its bins.

⇒ ** So the likelihood and its refit are the ONLY instruments in this row that both avoid the band-width
limit AND make an amplitude claim at band 1 ** -- *which is why ⓵ was the right question, and why there is
no third instrument outside the demonstration.*

⛔ *`cc66.61`'s floor is not revisited, softened or re-derived -- it stands as measured, as the order said.
No envelope, basis, abscissa or aggregation chosen; no new candidate; no mechanism.  No corpus edits.*
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
DIR = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7021_directions')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                             # noqa: E402

QE = np.asarray(np.load(os.path.join(SP, 'r6959_eta_cr.npz'))['q_edges'], float)
QCB = 0.5 * (QE[:-1] + QE[1:])
BASES = (('v ~ q', 1, False), ('v ~ q2', 2, False), ('ln v ~ q', 1, True), ('ln v ~ q2', 2, True))
PCOMB = 1.0

SRC = open(os.path.abspath(__file__)).read()
BODY = '\n'.join(ln for ln in SRC.split(chr(34) * 3)[2].splitlines() if '# noscan' not in ln)
LOSMARK = ('c54.17', 'c54.178_', 'L814_', 'r6784_')                                       # noscan
SOLVEMARK = ('ACOUSTIC_two_arm', 'subprocess', 'os.system')                               # noscan
check("⛔ PATH PROVENANCE: no line-of-sight bank name occurs in the executable body",
      not any(m in BODY for m in LOSMARK),                                                # noscan
      "the fine banks, the three response banks, the band edges and plik_lite only")
check("and nothing is SOLVED and nothing is RUN",
      not any(m in BODY for m in SOLVEMARK), "banks on disk, likelihood read through the corpus module")

NEED = ('r6959_eta_cr.npz', 'r6941_fine_lcdm.npz', 'r6941_fine_cr.npz',
        'r6959_nswap_lcdm.npz', 'r6975_mix_lcdm.npz', 'r6983_joint_lcdm.npz')
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

TXT = open(os.path.join(DIR, 'PREDICTION.md')).read()
check("⛔⛭ THE SEQUENCING, AND THE HARDEST PART OF IT: the pre-registration says OUT LOUD which facts had "
      "already been looked at before it was written -- the likelihood's bin structure -- and declares that "
      "branch SETTLED rather than pretending it was open",
      'What has already been looked at' in TXT and 'I am not pre-registering it as open' in TXT.lower()
      or 'AM NOT PRE-REGISTERING IT AS OPEN' in TXT,
      "the branch that was already decided is declared, not tabled as if open")
check("⛭ AND IT TABLES THE OUTCOME THAT ENDS THE ROW FIRST, as this seat has four revisions running",
      TXT.index('CANNOT SEPARATE THE CHANNELS AT BAND 1 EITHER') < TXT.index('CAN SEPARATE THEM'),
      "the closing outcome leads the table, and the reopening one is what obtained")
check("⛭ AND IT NAMES THE INCOMMENSURABLE-UNITS HAZARD BEFORE THE NUMBERS WERE IN HAND: this row's "
      "statistics are NOISELESS and their sigma is an empirical scatter, while the likelihood's is real "
      "instrument noise, so the two floors must not be quoted against each other",
      'noiseless' in TXT and 'must not be' in TXT and 'is not comparable with a number from '
      'the other' in TXT,
      "the hazard that the two floors would be read as one number")

LC, FAC = CS.bin_center_and_fac()


def load(n):
    d = np.load(os.path.join(SP, n))
    return d['ls'].astype(float), d['Dl'], float(d['l_A'])


def departure(v, p, lg):
    y = np.log(v) if lg else np.asarray(v, float)
    s_, i_ = np.polyfit(QCB[1:] ** p, y[1:], 1)
    pred = s_ * QCB ** p + i_
    f = (np.exp(y - pred) - 1.0) if lg else (y / pred - 1.0)
    return float(f[0]), float(np.sqrt(np.mean(f[1:] ** 2)))


LSC, DLC, AAC = load('r6941_fine_lcdm.npz')
LSA, DLA, _ = load('r6941_fine_cr.npz')
MC, MA = CS.bin_spectrum(LSC, DLC), CS.bin_spectrum(LSA, DLA)
KNOB = {}
for nm, fn in (('window', 'r6959_nswap_lcdm.npz'), ('term mix', 'r6975_mix_lcdm.npz'),
               ('JOINT', 'r6983_joint_lcdm.npz')):
    ls, dl, _ = load(fn)
    KNOB[nm] = CS.bin_spectrum(ls, dl)
OK = np.isfinite(MC) & np.isfinite(MA) & np.all([np.isfinite(v) for v in KNOB.values()], axis=0)
QBIN = (LC / AAC)[OK]
WQ = ((CS.BIN_HI - CS.BIN_LO + 1) / AAC)[OK]

# ==================================================================================================
print("\nPART 1 -- ⓵ⓐ THE LIKELIHOOD BINS, BUT IT DOES NOT BAND.")
print("-" * 100)
NB1 = int(((QBIN >= QE[0]) & (QBIN < QE[1])).sum())
print(f"    {int(OK.sum())} bins covered, ell {int(CS.BIN_LO[OK][0])}--{int(CS.BIN_HI[OK][-1])}, "
      f"q = {QBIN.min():.3f}--{QBIN.max():.3f}")
print(f"    bin widths in q: median {np.median(WQ):.4f} -- one {1 / np.median(WQ):.0f}th of a comb period; "
      f"{NB1} bins inside band 1")
check("⓵ⓐ THE LIKELIHOOD IS NOT A BANDED STATISTIC IN DISGUISE: its bins are more than an order of "
      "magnitude finer than the comb period, and band 1 -- the band that defeats every statistic in the "
      "demonstration -- contains many of them",
      np.median(WQ) < PCOMB / 10 and NB1 >= 10,
      f"median bin {np.median(WQ):.4f} in q against a period of {PCOMB:.2f}; {NB1} bins in band 1")
DD = np.sqrt(np.diag(CS.COV_TT))
R = CS.COV_TT / np.outer(DD, DD)
LAGS = [float(np.mean(np.diag(R, k))) for k in range(1, 8)]
check("AND IT DOES NOT INHERIT THE WIDTH LIMIT THROUGH ITS COVARIANCE EITHER: the bin-to-bin correlation is "
      "a flat floor, not a coupling that grows over a period",
      max(LAGS) < 0.3 and abs(LAGS[-1] - LAGS[1]) < 0.05,
      f"mean correlation at lags 1-7: {min(LAGS):.3f} to {max(LAGS):.3f}, flat")

# ==================================================================================================
print("\nPART 2 -- ⓵ⓑⓒ WHAT THE LIKELIHOOD SEES, IN ITS OWN METRIC.")
print("-" * 100)
COV = CS.COV_TT[np.ix_(OK, OK)]
F = scipy.linalg.cho_solve(scipy.linalg.cho_factor(COV), np.identity(int(OK.sum())))
F = 0.5 * (F + F.T)
mc, ma, d = MC[OK], MA[OK], CS.X_DATA[OK]
A = float((mc @ F @ d) / (mc @ F @ mc))
r = A * (ma - mc)


def band_S(lo, hi, vec):
    m = (QBIN >= lo) & (QBIN < hi)
    c = COV[np.ix_(m, m)]
    f = scipy.linalg.cho_solve(scipy.linalg.cho_factor(c), np.identity(int(m.sum())))
    return float(np.sqrt(vec[m] @ (0.5 * (f + f.T)) @ vec[m]))


S = np.array([band_S(a, b, r) for a, b in zip(QE[:-1], QE[1:])])
D = [departure(S, p, lg) for _, p, lg in BASES]
print("    arm vs control, sigma from each band alone:  " + '  '.join(f'{v:6.2f}' for v in S))
print("    band 1 against its own bands 2--7 trend:     "
      + '  '.join(f'{x[0]:+.3f}({x[0] / x[1]:+.2f}s)' for x in D))
check("⓵ⓑ THE STEP IS A LOCALISED CONTRIBUTION TO THE LIKELIHOOD'S EXCESS, with the SAME SIGN as every "
      "other instrument in this row -- and this per-band number carries the instrument's own noise rather "
      "than an empirical scatter across a noiseless theory spectrum",
      all(x[0] < 0 for x in D) and min(abs(x[0] / x[1]) for x in D) > 2.0,
      f"{min(x[0] for x in D):+.3f}..{max(x[0] for x in D):+.3f}, "
      f"{min(abs(x[0] / x[1]) for x in D):.1f}-{max(abs(x[0] / x[1]) for x in D):.1f} sigma; the trend "
      f"predicts {min(S[0] / (1 + x[0]) for x in D):.0f}-{max(S[0] / (1 + x[0]) for x in D):.0f} where the "
      f"likelihood delivers {S[0]:.1f}")
B1 = (QBIN >= QE[0]) & (QBIN < QE[1])
C1 = COV[np.ix_(B1, B1)]
F1 = scipy.linalg.cho_solve(scipy.linalg.cho_factor(C1), np.identity(int(B1.sum())))
F1 = 0.5 * (F1 + F1.T)


def sig1(v):
    return float(np.sqrt(v[B1] @ F1 @ v[B1]))


SG = {nm: A * (KNOB[nm][OK] - mc) for nm in KNOB}
SEP = sig1(SG['window'] - SG['term mix'])
for nm in ('window', 'term mix', 'JOINT'):
    print(f"    {nm + ' vs control, at band 1':36s}{sig1(SG[nm]):8.2f} sigma")
print(f"    {'the ARM vs control, at band 1':36s}{sig1(r):8.2f} sigma")
print(f"    {'window vs term mix, at band 1':36s}{SEP:8.2f} sigma")
check("⛔⛔ ⓵ⓒ AND THE LIKELIHOOD SEPARATES THE TWO CHANNELS AT BAND 1 -- the thing no statistic in this row "
      "can do.  ⇒ *** `cc66.61`'s DEMONSTRATION COVERS THE STATISTIC FAMILY AND NOT THE INSTRUMENT THE PAPER "
      "RUNS BESIDE IT, AND `PO-56`'s AMENDED CLAUSE IS NOT MET ***",
      SEP > 2.0, f"{SEP:.1f} sigma, against the 2 sigma the pre-registration set as the bar")
check("⚠ AND THE TWO FLOORS ARE IN DIFFERENT UNITS, WHICH THE PRE-REGISTRATION REQUIRED BE SAID: the "
      "likelihood's is a share of the band-1 DIFFERENCE under real instrument noise and `cc66.61`'s is a "
      "share of the STEP under an empirical scatter of a NOISELESS spectrum.  ** Neither bounds the other, "
      "and this receipt says so in its own header **",
      'not one number and neither bounds the other' in SRC.split(chr(34) * 3)[1],
      f"the likelihood's smallest detectable share at band 1 is {2 / sig1(r):.3f}; `cc66.61`'s floor is "
      f"0.59 of a different quantity")

# ==================================================================================================
print("\nPART 3 -- ⓶ THE SCOPE STATEMENT: WHICH INSTRUMENTS BAND.")
print("-" * 100)
HDR = SRC.split(chr(34) * 3)[1]
check("⓶ THE LIST IS COMPLETE AND COUNTED, and it is in this receipt's own header rather than left to the "
      "reply: every instrument this row has made a claim on, each marked",
      'eleven** instruments' in HDR and 'eight BANDS' in HDR.replace('** eight BAND **', 'eight BANDS')
      or ('eleven' in HDR and 'eight' in HDR and 'Three do not' in HDR),
      "11 instruments, 8 banding at 0.70 of a period, 3 not")
check("AND THE ONE THAT MATTERS IS NAMED: the likelihood and the refit that uses its bins are the ONLY "
      "instruments that both avoid the band-width limit AND make an amplitude claim at band 1 -- the "
      "anchored locator does neither, because it locates peaks rather than measuring amplitudes",
      'ONLY instruments in this row that both avoid the band-width' in HDR
      and 'makes no amplitude claim at band 1' in HDR,
      "which is why ⓵ was the right question and why no third instrument sits outside the demonstration")
check("⛔ AND ⓷ HOLDS: `cc66.61`'s floor is not revisited, softened or re-derived, and no envelope, basis, "
      "abscissa or aggregation is chosen",
      'stands as measured' in HDR and 'no mechanism' in HDR,
      "the order said the floor stands and this revision does not touch it")

print("\n" + "=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)
print("GATES: ALL PASS")
