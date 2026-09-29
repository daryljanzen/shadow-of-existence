"""r7029 item two (node 70): an independent audit of cc66.64's comb null.

Run after PREDICTION.md was committed.  It reuses cc66.64's receipt setup line for line (the banks, the OK mask,
F, shape_fit, perbin, the detrend and amp), so every number it prints is on the receipt's own footing.  It
edits nothing and solves nothing.
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

# ------------------------------------------------------------------ cc66.64's setup, verbatim in substance
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
ma = MA[OK]
MSK = [(QB >= a) & (QB < b) for a, b in zip(QE[:-1], QE[1:])]
HI = MSK[3] | MSK[4] | MSK[5] | MSK[6]


def shape_fit(m, n, data):
    x = np.log(LL / LL.mean())
    X = np.column_stack([m * x ** j for j in range(n)])
    return X @ scipy.linalg.solve(X.T @ F @ X, X.T @ F @ data, assume_a='sym')


def terms(data):
    """cc66.64's per-bin excess of the ARM over the control, split into its two terms, at n = 1."""
    rc = data - shape_fit(mc, 1, data)
    d = shape_fit(ma, 1, data) - shape_fit(mc, 1, data)
    return (d * (F @ d)), (-2.0 * d * (F @ rc))


qh = QB[HI]
x = np.log(qh / qh.mean())


def detrend(v):
    return v - np.polyval(np.polyfit(x, v, 1), x)


def amp(period, dd):
    w = 2.0 * np.pi / period
    X = np.column_stack([np.cos(w * qh), np.sin(w * qh)])
    return float(np.hypot(*scipy.linalg.lstsq(X, dd)[0]))


PER = np.linspace(0.55, 1.95, 141)
NULLMASK = np.abs(PER - 1.0) > 0.15
OUT = {}

quad, cross = terms(dat)
det = detrend((quad + cross)[HI])
a1 = amp(1.0, det)
A = np.array([amp(p, det) for p in PER])
aq, ax = amp(1.0, detrend(quad[HI])), amp(1.0, detrend(cross[HI]))
OUT['reproduced'] = dict(a1=a1, null_mean=float(A[NULLMASK].mean()), null_max=float(A[NULLMASK].max()),
                         n_null=int(NULLMASK.sum()), peak=float(PER[A.argmax()]), cross=ax, quad=aq)
print(f"REPRODUCED: a(1.00)={a1:.4f}  null mean {A[NULLMASK].mean():.4f} max {A[NULLMASK].max():.4f} "
      f"over {NULLMASK.sum()}  peak {PER[A.argmax()]:.2f}  cross {ax:.3f}  quad {aq:.3f}")

rng = np.random.default_rng(7029)
n = len(qh)

# ------------------------------------------------------------------ Q1(a)(b): N_eff and leakage, white noise
W = np.array([[amp(p, detrend(z)) for p in PER] for z in rng.standard_normal((2000, n))])
C = np.corrcoef(W.T)
i1 = int(np.argmin(np.abs(PER - 1.0)))
leak = C[i1][NULLMASK]
# effective independent periods in the null: participation ratio of the null block's correlation eigenvalues
ev = np.linalg.eigvalsh(C[np.ix_(NULLMASK, NULLMASK)])
neff = float(ev.sum() ** 2 / (ev ** 2).sum())
OUT['Q1'] = dict(neff_null=neff, leak_gt_half=int((leak > 0.5).sum()), leak_max=float(leak.max()),
                 leak_periods_gt_half=[float(p) for p in PER[NULLMASK][leak > 0.5]])
print(f"Q1(a) N_eff of the 110-period null (participation ratio, white noise): {neff:.2f}")
print(f"Q1(b) null periods whose amplitude correlates with a(1.00) above 0.5: {(leak > 0.5).sum()} "
      f"(max corr {leak.max():.2f})")

# Q1(c): band-edge aliasing -- a unit per-band constant pattern and a unit step train at the 0.70 edges
band_const = np.zeros(n)
for k, m in enumerate(MSK[3:7]):
    band_const[m[HI]] = (-1.0) ** k
edges = QE[3:8]
step = np.array([float(np.searchsorted(edges, q, side='right') % 2) for q in qh])
bc1, st1 = amp(1.0, detrend(band_const)), amp(1.0, detrend(step - step.mean()))
bc07 = amp(0.70 * 2, detrend(band_const))  # an alternating per-band sign has period 1.40
OUT['Q1']['band_const_amp_at_1'] = bc1
OUT['Q1']['band_const_amp_at_its_own_1.40'] = bc07
OUT['Q1']['step_amp_at_1'] = st1
print(f"Q1(c) unit alternating band pattern: {bc1:.3f} at period 1.00 vs {bc07:.3f} at its own 1.40; "
      f"unit step train: {st1:.3f} at 1.00")

# ------------------------------------------------------------------ Q3(i): circular shift over bin index
cs = np.array([amp(1.0, np.roll(det, s)) for s in range(1, n)])
csx = np.array([amp(1.0, np.roll(detrend(cross[HI]), s)) for s in range(1, n)])
csq = np.array([amp(1.0, np.roll(detrend(quad[HI]), s)) for s in range(1, n)])
OUT['Q3_i_all'] = dict(n=len(cs), ge=int((cs >= a1).sum()), median=float(np.median(cs)), max=float(cs.max()),
                       top=[(int(s), float(cs[s - 1])) for s in (np.argsort(cs)[::-1][:4] + 1)])
print(f"Q3(i) circular shift, ALL 81: {(cs >= a1).sum()} return >= {a1:.2f} (median {np.median(cs):.2f}, "
      f"max {cs.max():.2f}); top shifts {OUT['Q3_i_all']['top']}")
# ⚠ Found running it, not pre-registered: a shift of a few bins barely moves a comb 33.6 bins long, and a
#   shift by a whole period carries the comb with it -- the top of the unrestricted list is shifts +-1, +-2.
#   So the valid ensemble excludes shifts within 6 bins (circularly) of 0 or of a whole period.
BPP = 1.0 / float(np.median(np.diff(qh)))
VALID = [s for s in range(1, n) if min(abs(((s - k * BPP + n / 2) % n) - n / 2) for k in range(0, 3)) > 6]
cv, cvx, cvq = cs[np.array(VALID) - 1], csx[np.array(VALID) - 1], csq[np.array(VALID) - 1]
OUT['Q3_i'] = dict(n=len(VALID), ge=int((cv >= a1).sum()), median=float(np.median(cv)), max=float(cv.max()),
                   p95=float(np.quantile(cv, 0.95)), cross_ge=int((cvx >= ax).sum()),
                   quad_ge=int((cvq >= aq).sum()), bins_per_period=BPP)
print(f"Q3(i) circular shift, {len(VALID)} VALID shifts: {(cv >= a1).sum()} return >= {a1:.2f} "
      f"(median {np.median(cv):.2f}, 95% {np.quantile(cv, 0.95):.2f}, max {cv.max():.2f}); "
      f"cross {(cvx >= ax).sum()} exceed, quad {(cvq >= aq).sum()} exceed")

# band-level vs within-band: how much of a(1.00) the per-band means carry, and the peak's own width
bm = np.zeros(n)
for m in MSK[3:7]:
    bm[m[HI]] = det[m[HI]].mean()
half = A >= A.max() / np.sqrt(2)
OUT['Q1']['band_mean_part_at_1'] = amp(1.0, detrend(bm))
OUT['Q1']['within_band_part_at_1'] = amp(1.0, det - bm)
OUT['Q1']['peak_half_power_periods'] = [float(PER[half].min()), float(PER[half].max())]
print(f"Q1(c') of a(1.00): the per-band means project {OUT['Q1']['band_mean_part_at_1']:.3f}, the within-band "
      f"part {OUT['Q1']['within_band_part_at_1']:.3f}; the data peak's half-power width in period "
      f"{PER[half].min():.2f}-{PER[half].max():.2f}")

# ------------------------------------------------------------------ Q3(ii): phase randomisation
spec = np.fft.rfft(det)
pr = []
for _ in range(1000):
    ph = np.exp(1j * rng.uniform(0, 2 * np.pi, len(spec)))
    ph[0] = 1.0
    if n % 2 == 0:
        ph[-1] = np.sign(ph[-1].real) or 1.0
    pr.append(amp(1.0, detrend(np.fft.irfft(spec * ph, n))))
pr = np.array(pr)
OUT['Q3_ii'] = dict(n=len(pr), ge=int((pr >= a1).sum()), median=float(np.median(pr)),
                    p95=float(np.quantile(pr, 0.95)))
print(f"Q3(ii) phase randomisation: {(pr >= a1).sum()} of {len(pr)} return >= {a1:.2f}; "
      f"median {np.median(pr):.2f}, 95% {np.quantile(pr, 0.95):.2f}")

# ------------------------------------------------------------------ Q3(iii): instrument noise, whole estimator
Lc = np.linalg.cholesky(COV)
base = shape_fit(mc, 1, dat)
ns, nx, nq = [], [], []
for _ in range(2000):
    dstar = base + Lc @ rng.standard_normal(len(dat))
    q_, c_ = terms(dstar)
    ns.append(amp(1.0, detrend((q_ + c_)[HI])))
    nx.append(amp(1.0, detrend(c_[HI])))
    nq.append(amp(1.0, detrend(q_[HI])))
ns, nx, nq = map(np.array, (ns, nx, nq))
OUT['Q3_iii'] = dict(n=len(ns), ge=int((ns >= a1).sum()), p=float((1 + (ns >= a1).sum()) / (1 + len(ns))),
                     median=float(np.median(ns)), p99=float(np.quantile(ns, 0.99)), max=float(ns.max()),
                     cross_ge=int((nx >= ax).sum()), cross_median=float(np.median(nx)),
                     cross_p99=float(np.quantile(nx, 0.99)), quad_median=float(np.median(nq)),
                     quad_sd=float(nq.std()), ratio_median=float(np.median(nx / nq)))
print(f"Q3(iii) instrument noise: {(ns >= a1).sum()} of {len(ns)} draws return >= {a1:.2f} "
      f"(p={OUT['Q3_iii']['p']:.4f}); median {np.median(ns):.2f}, 99% {np.quantile(ns, 0.99):.2f}, "
      f"max {ns.max():.2f}")
print(f"Q4 under (iii): cross {ax:.2f} vs its null median {np.median(nx):.2f}, 99% "
      f"{np.quantile(nx, 0.99):.2f}, {(nx >= ax).sum()} exceed; quad is noise-free: "
      f"{np.median(nq):.3f} +/- {nq.std():.1e}")

json.dump(OUT, open(os.path.join(HERE, 'audit_null.json'), 'w'), indent=1)
print('wrote audit_null.json')
