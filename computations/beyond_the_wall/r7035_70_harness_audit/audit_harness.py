"""r7035 -> 70: one pass on the instrument-noise null harness (run after PREDICTION.md was committed).

The setup is `r7029`'s audit and `cc66.66`'s scoring, line for line in substance: the same banks, the same OK
mask, the same F, shape_fit, the per-bin excess and its detrended period-1.00 projection.  It edits nothing,
runs no accounting, and prints no central value of the term mix's ratio, phase or share.
"""
import json
import os
import sys

import numpy as np
import scipy.linalg

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS  # noqa: E402

NDRAW = int(os.environ.get('NDRAW', '2000'))
QE = np.asarray(np.load(os.path.join(SP, 'r6959_eta_cr.npz'))['q_edges'], float)
LC, _F = CS.bin_center_and_fac()


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
ma, mw, mk = MA[OK], KN['window'][OK], KN['term mix'][OK]
MSK = [(QB >= a) & (QB < b) for a, b in zip(QE[:-1], QE[1:])]
HI = MSK[3] | MSK[4] | MSK[5] | MSK[6]
qh = QB[HI]
x = np.log(qh / qh.mean())
_xf = np.log(LL / LL.mean())
NB = len(dat)


def shape_fit(m, data):
    X = (m * _xf ** 0).reshape(-1, 1)
    return X @ scipy.linalg.solve(X.T @ F @ X, X.T @ F @ data, assume_a='sym')


def detrend(v):
    return v - np.polyval(np.polyfit(x, v, 1), x)


_X1 = np.column_stack([np.cos(2.0 * np.pi * qh), np.sin(2.0 * np.pi * qh)])
_P1 = np.linalg.pinv(_X1)


def coef(v):
    """detrended period-1.00 (cos, sin) coefficients over bands 4--7 -- the receipts' own projection"""
    return _P1 @ detrend(v)


def amp(v):
    return float(np.hypot(*coef(v)))


def phase(c):
    return float(np.arctan2(-c[1], c[0]))  # cc66.65's convention


def wrap(a):
    return (np.asarray(a) + np.pi) % (2.0 * np.pi) - np.pi


def excess(m, data):
    rc = data - shape_fit(mc, data)
    d = shape_fit(m, data) - shape_fit(mc, data)
    return d * (F @ d), -2.0 * d * (F @ rc), d


def trio(data):
    """the arm's a(1.00) and cc66.66's three projections, beta and gamma re-estimated from this data"""
    qa, ca, _ = excess(ma, data)
    qk, ck, _ = excess(mk, data)
    ea, ek = (qa + ca)[HI], (qk + ck)[HI]
    be = float(ek @ ea / (ea @ ea))
    ga = float(ea @ ek / (ek @ ek))
    return np.array([amp(ea), amp(ek), amp(ea - ga * ek), amp(ek - be * ea)])


QN = ['arm a(1.00)', 'ⓐ term mix own cost', 'ⓑ arm part it does not explain', 'ⓒ the part it misplaces']
OUT = {'ndraw': NDRAW}
OBS = trio(dat)
base = shape_fit(mc, dat)
print('OBSERVED:', ', '.join(f'{n} {v:.3f}' for n, v in zip(QN, OBS)))

# the gate first: cc66.66's own seed and draw order reproduce its published multiples (2.26, 2.83, 1.44)
_r = np.random.default_rng(7033)
_Lc = np.linalg.cholesky(COV)
_n = np.array([trio(base + _Lc @ _r.standard_normal(NB)) for _ in range(2000)])
OUT['repro_cc66_66'] = dict(null_max=_n.max(0).tolist(), obs_over_max=(OBS / _n.max(0)).tolist())
print('REPRO cc66.66 (seed 7033): obs/max', np.round(OBS / _n.max(0), 2).tolist())

# ================================================================== ⓐ THE ASSUMPTION: the DRAWING covariance
sd = np.sqrt(np.diag(COV))
R0 = COV / np.outer(sd, sd)
idx = np.arange(NB)
LAG = np.abs(idx[:, None] - idx[None, :])
R2 = np.where(LAG == 0, 1.0, 0.15)
R3 = np.where(LAG == 0, 1.0, np.where(LAG <= 7, 0.15, 0.0))
VAR = {'V0 likelihood COV': COV,
       'V1 diagonal alone': np.diag(sd ** 2),
       'V2 flat 0.15, all pairs': R2 * np.outer(sd, sd),
       'V3 flat 0.15, lags 1-7': R3 * np.outer(sd, sd),
       'V4 COV x 0.5': 0.5 * COV,
       'V4 COV x 2': 2.0 * COV}
OUT['facts'] = dict(n_ok=NB, lag_mean_corr=[float(np.mean(np.diag(R0, k))) for k in (1, 2, 7, 15, 30)],
                    min_eig={k: float(np.linalg.eigvalsh(v / np.outer(sd, sd)).min()) for k, v in VAR.items()})
NUL = {}
for k, C in VAR.items():
    L = np.linalg.cholesky(C)
    rng = np.random.default_rng(7035)  # one shared seed per variant: the variants differ ONLY in C
    Z = rng.standard_normal((NDRAW, NB))
    NUL[k] = np.array([trio(base + L @ z) for z in Z])
    n = NUL[k]
    print(f'\n{k}')
    for j, nm in enumerate(QN):
        print(f'   {nm:34s} obs {OBS[j]:7.3f}  null med {np.median(n[:, j]):6.3f}  p99 '
              f'{np.quantile(n[:, j], 0.99):6.3f}  max {n[:, j].max():6.3f}  #>=obs {int((n[:, j] >= OBS[j]).sum()):4d}'
              f'  obs/max {OBS[j] / n[:, j].max():5.2f}')
OUT['A'] = {k: {nm: dict(median=float(np.median(n[:, j])), p99=float(np.quantile(n[:, j], 0.99)),
                         max=float(n[:, j].max()), ge=int((n[:, j] >= OBS[j]).sum()),
                         obs_over_max=float(OBS[j] / n[:, j].max()))
                for j, nm in enumerate(QN)} for k, n in NUL.items()}
OUT['observed'] = dict(zip(QN, map(float, OBS)))

# rescale law: does the null scale as sqrt(s)?
for s, k in ((0.5, 'V4 COV x 0.5'), (2.0, 'V4 COV x 2')):
    r = [float(np.median(NUL[k][:, j]) / np.median(NUL['V0 likelihood COV'][:, j]) / np.sqrt(s))
         for j in range(4)]
    OUT['A'].setdefault('sqrt_law', {})[str(s)] = r
    print(f'   median ratio / sqrt({s}) per quantity: {np.round(r, 4)}')
# ⚠ Found running it, not pre-registered: the sqrt(s) law FAILS -- each null draw is a FIXED part (the quadratic
#   term d'Fd, noise-free, declared in r7029's Q4) plus a noise part, and only the noise part scales.  So the
#   pre-registered s* = (obs/max)^2 is kept for the record but is NOT the margin; the margin is measured by a scan.
sstar_formula = {nm: float((OBS[j] / NUL['V0 likelihood COV'][:, j].max()) ** 2) for j, nm in enumerate(QN)}
OUT['A']['s_star_formula_INVALID'] = sstar_formula
print('   s* by the pre-registered formula (INVALID, sqrt law fails):', {k: round(v, 2) for k, v in sstar_formula.items()})
SGRID = [1.0, 1.25, 1.5, 2.0, 2.5, 3.0, 4.0, 6.0, 8.0, 12.0, 16.0, 24.0]
LV = np.linalg.cholesky(COV)
ZS = np.random.default_rng(70353).standard_normal((NDRAW, NB))
scan = {}
for s in SGRID:
    n = np.array([trio(base + np.sqrt(s) * (LV @ z)) for z in ZS])
    scan[str(s)] = dict(ge=[int((n[:, j] >= OBS[j]).sum()) for j in range(4)],
                        p99=[float(np.quantile(n[:, j], 0.99)) for j in range(4)],
                        max=[float(n[:, j].max()) for j in range(4)])
OUT['A']['scan'] = scan
first = {}
for j, nm in enumerate(QN):
    fm = next((s for s in SGRID if scan[str(s)]['ge'][j] > 0), None)
    f99 = next((s for s in SGRID if scan[str(s)]['p99'][j] >= OBS[j]), None)
    first[nm] = dict(first_s_any_draw_reaches=fm, first_s_p99_reaches=f99)
    print(f'   scan {nm:34s} first s with a draw >= obs: {fm}   first s with p99 >= obs: {f99}')
OUT['A']['s_star_measured'] = first
struct = {k: [float(NUL[k][:, j].max() / NUL['V0 likelihood COV'][:, j].max()) for j in range(4)]
          for k in ('V1 diagonal alone', 'V2 flat 0.15, all pairs', 'V3 flat 0.15, lags 1-7')}
OUT['A']['struct_max_ratio'] = struct
print('   structural variants, null max / V0 null max:', {k: np.round(v, 3).tolist() for k, v in struct.items()})

# ⚠ Found running it, not pre-registered: the maximum of 2,000 draws is itself a noisy statistic -- this seed's
#   V0 null max for the misplaced part is not cc66.66's.  So the maximum's spread across seeds is measured, and a
#   pooled ensemble gives the tail count the "x null max" ratios were standing in for.
NSEED = 10
seedmax, pooled = {}, {}
for k in ('V0 likelihood COV', 'V3 flat 0.15, lags 1-7'):
    L = np.linalg.cholesky(VAR[k])
    mx, allv = [], []
    for sd_ in range(NSEED):
        Z = np.random.default_rng(80000 + sd_).standard_normal((NDRAW, NB))
        n = np.array([trio(base + L @ z) for z in Z])
        mx.append(n.max(axis=0))
        allv.append(n)
    mx, allv = np.array(mx), np.concatenate(allv)
    seedmax[k] = {nm: dict(min=float(mx[:, j].min()), max=float(mx[:, j].max()),
                           obs_over_max_range=[float(OBS[j] / mx[:, j].max()), float(OBS[j] / mx[:, j].min())])
                  for j, nm in enumerate(QN)}
    pooled[k] = {nm: dict(n=int(len(allv)), ge=int((allv[:, j] >= OBS[j]).sum()),
                          p=float((1 + (allv[:, j] >= OBS[j]).sum()) / (1 + len(allv))))
                 for j, nm in enumerate(QN)}
    for j, nm in enumerate(QN):
        print(f"   {k:24s} {nm:34s} null max over {NSEED} seeds {mx[:, j].min():.3f}-{mx[:, j].max():.3f} "
              f"(obs/max {OBS[j] / mx[:, j].max():.2f}-{OBS[j] / mx[:, j].min():.2f});  pooled "
              f"{pooled[k][nm]['ge']} of {len(allv)} >= obs, p {pooled[k][nm]['p']:.1e}")
OUT['A']['seed_spread_of_max'] = seedmax
OUT['A']['pooled'] = pooled

# the repository's own measured noise scale: the Planck-fitted LCDM chi2 recorded in the likelihood's PROVENANCE
PROV = open(os.path.join(ROOT, 'computations', 'planck_tt_likelihood', 'PROVENANCE.md'), encoding='utf-8').read()
FIT = json.load(open(os.path.join(ROOT, 'computations', 'planck_tt_likelihood', 'lcdm.json')))
nu_fit = 215 - len(FIT['x'])
OUT['A']['s_hat'] = dict(chi2=float(FIT['fun']), nu=nu_fit, s_hat=float(FIT['fun']) / nu_fit,
                         width=float(np.sqrt(2.0 / nu_fit)),
                         prov_states='206.4 over 215 bins' in PROV)
print(f"   repository noise scale: fitted LCDM chi2 {FIT['fun']:.1f} over nu {nu_fit} -> s_hat "
      f"{FIT['fun'] / nu_fit:.3f} +/- {np.sqrt(2.0 / nu_fit):.3f}")
# ⛔ and the harness's own control is NOT a noise estimate: it is a theory spectrum, not fitted to the data
rc0 = dat - base
OUT['A']['control_chi2_per_nu_NOT_a_noise_scale'] = float(rc0 @ F @ rc0) / (NB - 1)
print(f"   (the harness control's chi2/nu {OUT['A']['control_chi2_per_nu_NOT_a_noise_scale']:.2f} is theory misfit, "
      f"not a noise scale)")

# ================================================================== ⓑ RATIO AND PHASE
# (0) the null CANNOT carry them: phases under the null, Rayleigh test
LV0 = np.linalg.cholesky(COV)
rng = np.random.default_rng(70351)
ZN = rng.standard_normal((NDRAW, NB))
ph_null, ph_cr = [], []
for z in ZN:
    qa, ca, _ = excess(ma, base + LV0 @ z)
    ph_null.append(phase(coef((qa + ca)[HI])))
    ph_cr.append(phase(coef(ca[HI])))
OUT['B_null_phase'] = {}
for nm, ph in (('excess (quad + cross)', ph_null), ('cross term alone', ph_cr)):
    Rbar = float(np.abs(np.mean(np.exp(1j * np.array(ph)))))
    p_ray = float(np.exp(-NDRAW * Rbar ** 2))
    OUT['B_null_phase'][nm] = dict(Rbar=Rbar, rayleigh_p=p_ray)
    print(f'\nⓑ(0) arm {nm} phase under the NULL: mean resultant {Rbar:.4f}, Rayleigh p {p_ray:.3g}')
# ⚠ Found running it: the excess's null phase is NOT uniform, because the quadratic term is fixed in every draw
qa0, _, _ = excess(ma, base)
OUT['B_null_phase']['quad_fixed_amp'] = amp(qa0[HI])
OUT['B_null_phase']['quad_fixed_phase_minus_obs_arm'] = float(wrap(phase(coef(qa0[HI])) - phase(coef(
    sum(excess(ma, dat)[:2])[HI]))))


def levels(data):
    """(cos, sin) at period 1.00 of: spectrum-level d, and the per-bin excess, for arm / window / term mix"""
    out = {}
    for nm, m in (('arm', ma), ('window', mw), ('term mix', mk)):
        q_, c_, d_ = excess(m, data)
        out['d ' + nm] = coef(d_[HI])
        out['ex ' + nm] = coef((q_ + c_)[HI])
        out['cr ' + nm] = coef(c_[HI])
    return out


OBSL = levels(dat)


def perturb(scale, seed):
    r = np.random.default_rng(seed)
    Z = r.standard_normal((NDRAW, NB))
    return [levels(dat + scale * (LV0 @ z)) for z in Z]


PT = perturb(1.0, 70352)
PH = perturb(0.5, 70352)  # same z, half the noise: the linearity check


def stat(D, key_a, key_b):
    """ratio amp(b)/amp(a) and phase offset phase(b) - phase(a) across a perturbation ensemble"""
    ra = np.array([np.hypot(*e[key_b]) / np.hypot(*e[key_a]) for e in D])
    po = np.array([wrap(phase(e[key_b]) - phase(e[key_a])) for e in D])
    return ra, po


RES = {}
for lvl in ('d', 'ex'):
    for ch in ('window', 'term mix'):
        ka, kb = f'{lvl} arm', f'{lvl} {ch}'
        ra, po = stat(PT, ka, kb)
        ra5, po5 = stat(PH, ka, kb)
        r0 = np.hypot(*OBSL[kb]) / np.hypot(*OBSL[ka])
        p0 = float(wrap(phase(OBSL[kb]) - phase(OBSL[ka])))
        e = dict(ratio_sd=float(ra.std()),
                 phase_sd=float(np.std(wrap(po - p0))),
                 lin_ratio=float(2 * ra5.std() / ra.std()) if ra.std() > 0 else None,
                 lin_phase=float(2 * np.std(wrap(po5 - p0)) / np.std(wrap(po - p0))))
        if ch == 'window':  # the published window numbers are validated as centres; the term mix's are NOT printed
            e.update(ratio_obs=float(r0), phase_obs=p0, ratio_rel_sd=float(ra.std() / r0), ratio_med=float(np.median(ra)),
                     phase_med=float(np.median(wrap(po - p0)) + p0))
        RES[f'{lvl} {ch}/arm'] = e
        shown = (f'ratio {r0:.4f} (median {np.median(ra):.4f})  phase {p0:+.3f} rad  '
                 if ch == 'window' else '[central values withheld: cc66 runs the accounting]  ')
        print(f"ⓑ {lvl:2s} {ch:8s}/arm: {shown}ratio sd {e['ratio_sd']:.2e} "
              f"phase sd {e['phase_sd']:.2e} rad  linearity x2(half)/full: ratio {e['lin_ratio']:.3f} "
              f"phase {e['lin_phase']:.3f}")
OUT['B'] = RES

# the joint covariance of the excess-level coefficients, and delta-method floors from it
KEYS = ['ex arm', 'ex window', 'ex term mix']
V = np.array([np.concatenate([e[k] for k in KEYS]) for e in PT])
CJ = np.cov(V.T)
OUT['B_cov6'] = CJ.tolist()
sig_comp = {k: float(np.sqrt(0.5 * (CJ[2 * i, 2 * i] + CJ[2 * i + 1, 2 * i + 1]))) for i, k in enumerate(KEYS)}
OUT['B_sigma_component'] = sig_comp
print('ⓑ per-component noise sigma of the excess projections:', {k: round(v, 4) for k, v in sig_comp.items()})


def delta(i, j):
    """delta-method sd of ratio |b|/|a| and phase(b) - phase(a) from the joint 6x6 covariance at the observed"""
    a, b = OBSL[KEYS[i]], OBSL[KEYS[j]]
    A, B = np.hypot(*a), np.hypot(*b)
    g = np.zeros(6)
    g[2 * i:2 * i + 2] = -(B / A ** 3) * a
    g[2 * j:2 * j + 2] = b / (A * B)
    # phase = atan2(-s, c): d/dc = s/A^2, d/ds = -c/A^2
    h = np.zeros(6)
    h[2 * j:2 * j + 2] = np.array([b[1], -b[0]]) / B ** 2
    h[2 * i:2 * i + 2] = -np.array([a[1], -a[0]]) / A ** 2
    return float(np.sqrt(g @ CJ @ g)), float(np.sqrt(h @ CJ @ h))


dr, dp = delta(0, 1)
OUT['B_delta_window'] = dict(ratio_sd=dr, phase_sd=dp,
                             agree_ratio=dr / RES['ex window/arm']['ratio_sd'],
                             agree_phase=dp / RES['ex window/arm']['phase_sd'])
print(f"ⓑ delta method, window/arm at the excess: ratio sd {dr:.4f} (direct {RES['ex window/arm']['ratio_sd']:.4f}),"
      f" phase sd {dp:.4f} (direct {RES['ex window/arm']['phase_sd']:.4f})")

# the floor on a linear residue arm - k*channel at fixed k, as a function of k (k on a grid, not a fitted value)
KG = [0.0, 0.25, 0.5, 1.0]
res_floor = {}
for ch, j in (('window', 1), ('term mix', 2)):
    out = []
    for kk in KG:
        g = np.zeros((2, 6))
        g[:, 0:2] = np.eye(2)
        g[:, 2 * j:2 * j + 2] = -kk * np.eye(2)
        Cr = g @ CJ @ g.T
        out.append(float(np.sqrt(0.5 * np.trace(Cr))))
    res_floor[ch] = dict(zip(map(str, KG), out))
OUT['B_residue_sigma_component'] = res_floor
print('ⓑ per-component sigma of the residue arm - k*channel, k on a grid:', res_floor)

if not os.environ.get('AUDIT_NOWRITE'):
    json.dump(OUT, open(os.path.join(HERE, 'audit_harness.json'), 'w'), indent=1, ensure_ascii=False)
    print('wrote audit_harness.json')
