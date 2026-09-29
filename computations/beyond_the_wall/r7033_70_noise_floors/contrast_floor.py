"""r7033 (node 70), item a, the contrast statistic: can a noise model be built from what the repository holds?

Reuses the contrast receipt's own definitions for its binned rung VERBATIM IN SUBSTANCE: the lensing ratio,
`mb`, `KEEP`, `FISH`, `env_a`, `osc`, `stat` and `fit4`.  It edits nothing and scores nothing.
"""
import json, os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS  # noqa: E402
import camb  # noqa: E402

VER = {t: np.load(os.path.join(SP, f'cc66_r185_verify_{t}.npz')) for t in ('lcdm', 'cr')}
LA = {t: float(VER[t]['l_A']) for t in ('lcdm', 'cr')}
LC, FACB = CS.bin_center_and_fac()
_p = camb.set_params(H0=67.40, ombh2=0.02237, omch2=0.3150 * 0.674 ** 2 - 0.02237,
                     mnu=0.06, omk=0, tau=0.054, As=2.1e-9, ns=0.965, lmax=3000)
_cl = camb.get_results(_p).get_cmb_power_spectra(_p, CMB_unit='muK', lmax=3000)
_le, _un = _cl['total'][:, 0], _cl['unlensed_scalar'][:, 0]
LGR = np.arange(len(_le), dtype=float)
RAT = np.ones_like(_le)
_m = _un > 0
RAT[_m] = _le[_m] / _un[_m]
mb = lambda ls, Dl: CS.bin_spectrum(ls, Dl * np.interp(ls, LGR, RAT))
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


LO, HI, NG = 0.85, 5.75, 1200


def stat(qA, oA, qB, oB, lo=LO, hi=HI):
    g = np.linspace(lo, hi, NG)
    a, b = np.interp(g, qA, oA), np.interp(g, qB, oB)
    return float(np.sum(a * b) / np.sum(b * b))


M = {t: mb(VER[t]['ls'].astype(float), VER[t]['Dl'])[KEEP] for t in ('lcdm', 'cr')}
A = {t: float(M[t] @ FISH @ DK / (M[t] @ FISH @ M[t])) for t in M}
Q = {t: LCK / LA[t] for t in M}
Y = {t: A[t] * M[t] * FACK for t in M}
OB = osc(Q['lcdm'], Y['lcdm'])
OUT = {}
reg_arm = stat(Q['cr'], osc(Q['cr'], Y['cr']), Q['lcdm'], OB)
OUT['reg_arm_binned_rung'] = reg_arm
# (1) the statistic AS DEFINED never sees the data: the fitted amplitude cancels in the envelope normalisation
inv = [stat(Q['cr'], osc(Q['cr'], s * Y['cr']), Q['lcdm'], OB) for s in (0.5, 0.9, 1.1, 2.0)]
OUT['amplitude_invariance_maxdev'] = float(max(abs(v - reg_arm) for v in inv))
# (2) the constructible noise model: the SAME statistic on a noisy realisation of the sky -- the control's fitted
#     binned C_l plus a draw from the likelihood's own covariance -- against the noiseless control
L = np.linalg.cholesky(COVK)
rng = np.random.default_rng(7033)
base = A['lcdm'] * M['lcdm']
regs = []
for _ in range(2000):
    d = base + L @ rng.standard_normal(len(base))
    regs.append(stat(Q['lcdm'], osc(Q['lcdm'], d * FACK), Q['lcdm'], OB))
regs = np.array(regs)
OUT['null'] = dict(n=len(regs), mean=float(regs.mean()), sd=float(regs.std()),
                   q025=float(np.quantile(regs, 0.025)), q975=float(np.quantile(regs, 0.975)))
OUT['floor_2sd'] = 2 * float(regs.std())
OUT['arm_departure'] = reg_arm - 1.0
OUT['departure_over_floor'] = (reg_arm - 1.0) / (2 * float(regs.std()))
# (3) the banded form on the same rung: per-band std of osc, noisy over noiseless
QE = np.asarray(np.load(os.path.join(SP, 'r6959_eta_cr.npz'))['q_edges'], float)
bands = [(Q['lcdm'] >= a) & (Q['lcdm'] < b) for a, b in zip(QE[:-1], QE[1:])]
bref = np.array([OB[m].std() for m in bands])
bn = []
for _ in range(2000):
    d = base + L @ rng.standard_normal(len(base))
    o = osc(Q['lcdm'], d * FACK)
    bn.append([o[m].std() / r - 1 for m, r in zip(bands, bref)])
bn = np.array(bn)
OUT['banded'] = dict(bins_per_band=[int(m.sum()) for m in bands], sd=[float(v) for v in bn.std(0)],
                     floor_2sd=[float(2 * v) for v in bn.std(0)], bias=[float(v) for v in bn.mean(0)])
for k, v in OUT.items():
    print(k, v)
json.dump(OUT, open(os.path.join(HERE, 'contrast_floor.json'), 'w'), indent=1)
