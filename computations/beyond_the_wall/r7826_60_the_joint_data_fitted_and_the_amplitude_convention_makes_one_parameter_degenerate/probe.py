#!/usr/bin/env python3
r"""r7826 (60) -- the best fit to the joint Planck + ACT data, on order r7821 (69) item (1).

Registered at r7824 before any of this ran.  Eleven arms.

STAGES, so that no long fit is ever re-run for reassurance:
    python3 probe.py repro   -- Arm A(1): reproduce r7822's landed figures on the banked control
    python3 probe.py fitA    -- the fit under r7820's amplitude convention (both blocks free)
    python3 probe.py fitB    -- the fit under the SHIPPED prior convention (Planck N(1, 0.0025))
    python3 probe.py report  -- every remaining arm, off the cached fits
Each stage writes its own npz into runs/ and never recomputes another stage's.
"""
import json
import os
import re
import sys
import inspect

import numpy as np
import scipy.linalg
from scipy.integrate import quad
from scipy.optimize import minimize, minimize_scalar

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402

SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
AD = os.path.join(ROOT, 'computations', 'planck_tt_likelihood', 'data', 'act_dr6_cmbonly')
FITPY = os.path.join(ROOT, 'computations', 'planck_tt_likelihood', 'fit.py')
RUNS = os.path.join(HERE, 'runs')

# ---- the two constants fit.py's engine holds fixed, and the inherited suppression pins ----------
TAU = 0.054
R_INHERITED, LD_INHERITED = 1.0926, 1489.5783
LMAX_THEORY = 8700
lmax = LMAX_THEORY          # the name fit.py's cr_supp body reads; see Arm B(2)
c = 299792.458              # ditto

# ---- the data ----------------------------------------------------------------------------------
AZ = np.load(os.path.join(AD, 'act_dr6_cmbonly.npz'), allow_pickle=True)
A_ELL, A_DL, A_WIN, A_WL = AZ['ell_TT'], AZ['Dl_TT'], AZ['win_TT'], AZ['win_ell']
A_COV = AZ['cov'][:45, :45]
CUT = int(open(os.path.join(AD, 'likelihood_source', 'PlanckActCut.yaml'),
               encoding='utf-8').read().split('lmax_cuts:')[1].split()[0])


def fisher(cov):
    F = scipy.linalg.cho_solve(scipy.linalg.cho_factor(cov), np.identity(cov.shape[0]))
    return 0.5 * (F + F.T)


# ================================================================ fit.py's own suppression, verbatim
def cr_supp(d,dp,H0,ombh2,omch2,z_onset=6797.0):
    Om=(ombh2+omch2)/(H0/100)**2; OL=1-Om
    z_rec=dp['zstar']; a_rec=1/(1+z_rec); Or=Om/(1+dp['zeq'])
    R_rec=31500*ombh2/(2.7255/2.7)**4/(1+z_rec)
    Rf=lambda a: R_rec*(a/a_rec)
    g=lambda a: (Rf(a)**2/(1+Rf(a))+8/9)/(6*(1+Rf(a)))
    H=lambda a,rad: H0*np.sqrt(Or/a**4*rad+Om/a**3+OL)
    a_s=1/(1+z_onset)
    IL,_=quad(lambda a:g(a)/H(a,1.0),1e-9,a_rec,limit=120)
    IC,_=quad(lambda a:g(a)/H(a,0.0),a_s,a_rec,limit=120)
    sL,_=quad(lambda a:c/(a**2*H(a,1.0)*np.sqrt(3*(1+Rf(a)))),1e-9,a_rec,limit=120)
    sC,_=quad(lambda a:c/(a**2*H(a,0.0)*np.sqrt(3*(1+Rf(a)))),a_s,a_rec,limit=120)
    r=(np.sqrt(IC/IL))/(sC/sL)
    full=np.arange(d.shape[0]); sel=(full>1400)&(full<2400)
    co=np.polyfit(full[sel].astype(float)**2, np.log(np.maximum(d[sel,0],1e-12)),1)
    lD=np.sqrt(-1/co[0]); ell=np.arange(2,lmax+1)
    return np.exp(-(ell/lD)**2*(r**2-1)), r, lD


def supp_source_matches():
    """Arm B(2): the body above is fit.py's, compared character-for-character"""
    src = open(FITPY, encoding='utf-8').read()
    m = re.search(r"^def cr_supp\(.*?(?=^def |^if __name__)", src, re.M | re.S)
    theirs = m.group(0).rstrip() if m else ''
    mine = inspect.getsource(cr_supp).rstrip()
    return theirs == mine, theirs, mine


# ================================================================ the theory
def camb_spectrum(H0, ombh2, omch2, As, ns, lmax_theory=LMAX_THEORY):
    import warnings
    warnings.filterwarnings('ignore')
    import camb
    p = camb.CAMBparams()
    p.set_cosmology(H0=H0, ombh2=ombh2, omch2=omch2, tau=TAU)
    p.InitPower.set_params(As=As, ns=ns)
    p.set_for_lmax(lmax_theory + 100, lens_potential_accuracy=0)
    p.set_accuracy(AccuracyBoost=1.0, lSampleBoost=1.0)
    r = camb.get_results(p)
    d = r.get_cmb_power_spectra(p, CMB_unit='muK')['total']
    return d, r.get_derived_params()


# ================================================================ the joint arm
def build_arm(ls, reach=None):
    """the support split r7820 established: Planck below CUT, ACT whose support clears it

    `reach` caps ACT's window support at the theory's last multipole; None means ls.max().
    """
    reach = float(ls.max()) if reach is None else float(reach)
    p_keep = np.isfinite(CS.bin_spectrum(ls, np.ones_like(ls, dtype=float))) & (CS.BIN_HI < CUT)
    p_lmax = int(CS.BIN_HI[p_keep].max())
    s_min = np.array([A_WL[A_WIN[:, i] > 0].min() for i in range(A_WIN.shape[1])])
    s_max = np.array([A_WL[A_WIN[:, i] > 0].max() for i in range(A_WIN.shape[1])])
    a_keep = (s_min > p_lmax) & (s_max <= reach)
    return p_keep, p_lmax, a_keep, s_min, s_max


def amp_free(d, F, m):
    A = float((m @ F @ d) / (m @ F @ m))
    r = d - A * m
    return float(r @ F @ r), A


def amp_prior(d, F, m, mu=1.0, sig=0.0025):
    """the shipped Planck prior A_planck ~ Normal(mu, sig), still closed form"""
    w = 1.0 / sig ** 2
    A = float((m @ F @ d + w * mu) / (m @ F @ m + w))
    r = d - A * m
    return float(r @ F @ r + w * (A - mu) ** 2), A


class Arm:
    """one joint likelihood: a theory grid, the two blocks, and the amplitude convention"""

    def __init__(self, ls, reach=None, planck_prior=False):
        self.ls = np.asarray(ls, dtype=float)
        self.pk, self.p_lmax, self.ak, self.s_min, self.s_max = build_arm(self.ls, reach)
        self.PF, self.PD = fisher(CS.COV_TT[np.ix_(self.pk, self.pk)]), CS.X_DATA[self.pk]
        self.AF, self.ADv = fisher(A_COV[np.ix_(self.ak, self.ak)]), A_DL[self.ak]
        self.AW = A_WIN[:, self.ak]
        self.planck_prior = planck_prior

    def planck_bin(self, dl):
        return CS.bin_spectrum(self.ls, dl)[self.pk]

    def act_bin(self, dl):
        return self.AW.T @ np.interp(A_WL, self.ls, dl)

    def chi2(self, dl, dP=None, dA=None):
        mP, mA = self.planck_bin(dl), self.act_bin(dl)
        dP = self.PD if dP is None else dP
        dA = self.ADv if dA is None else dA
        cP, aP = (amp_prior(dP, self.PF, mP) if self.planck_prior
                  else amp_free(dP, self.PF, mP))
        cA, aA = amp_free(dA, self.AF, mA)
        return cP + cA, cP, cA, aP, aA

    @property
    def ndata(self):
        return int(self.pk.sum()) + int(self.ak.sum())

    def fit_tilt(self, base, dP=None, dA=None):
        """the power-law tilt a data pair prefers on a given baseline, and its curvature width"""
        def at(dn):
            return self.chi2(base * (self.ls / 1000.0) ** dn, dP, dA)[0]
        o = minimize_scalar(at, bounds=(-3.0, 3.0), method='bounded', options={'xatol': 1e-10})
        dn0, c0 = float(o.x), float(o.fun)
        h = 1e-3
        d2 = (at(dn0 + h) - 2 * c0 + at(dn0 - h)) / h ** 2
        return dn0, c0, float(np.sqrt(2.0 / d2))


# ================================================================ stage: repro
def stage_repro():
    z = np.load(os.path.join(SP, 'L824_lcdm_L3200_nk960.npz'))
    ls, raw = z['ls'].astype(float), z['Dl'].astype(float)
    k0 = np.isfinite(CS.bin_spectrum(ls, raw))
    F0 = fisher(CS.COV_TT[np.ix_(k0, k0)])
    m0 = CS.bin_spectrum(ls, raw)[k0]
    dl = raw * float((m0 @ F0 @ CS.X_DATA[k0]) / (m0 @ F0 @ m0))
    arm = Arm(ls)                                       # reach = 3200, r7820's own subset
    sig = dl * np.exp(-(R_INHERITED ** 2 - 1) * (ls / LD_INHERITED) ** 2)
    dn_sky, c_sky, s_sky = arm.fit_tilt(dl)
    dn_sig, _, _ = arm.fit_tilt(dl, arm.planck_bin(sig), arm.act_bin(sig))
    dist = abs(dn_sig - dn_sky) / s_sky
    print(f"  Ⓐ①  banked control, r7820's arm: {int(arm.pk.sum())} Planck + "
          f"{int(arm.ak.sum())} ACT")
    print(f"       dn_sky = {dn_sky:+.6f} +/- {s_sky:.6f}   dn_sig = {dn_sig:+.6f}   "
          f"dist = {dist:.3f} sigma")
    np.savez(os.path.join(RUNS, 'repro.npz'), dn_sky=dn_sky, sig_sky=s_sky, dn_sig=dn_sig,
             dist=dist, chi2_sky=c_sky, n_planck=int(arm.pk.sum()), n_act=int(arm.ak.sum()),
             p_lmax=arm.p_lmax, cut=CUT)
    return 0


# ================================================================ stages: the two fits
BOUNDS = dict(H0=(55, 85), ombh2=(0.018, 0.026), omch2=(0.09, 0.16),
              As9=(1.5, 3.0), ns=(0.85, 1.25))
X0 = [67.4, 0.0224, 0.120, 2.1, 0.965]


def _obj(arm, with_supp, free_As, As_fixed=2.1):
    def f(pv):
        if free_As:
            H0, ombh2, omch2, As9, ns = pv
        else:
            H0, ombh2, omch2, ns = pv
            As9 = As_fixed
        for k, v in zip(('H0', 'ombh2', 'omch2', 'As9', 'ns'), (H0, ombh2, omch2, As9, ns)):
            lo, hi = BOUNDS[k]
            if not (lo < v < hi):
                return 1e7
        try:
            d, dp = camb_spectrum(H0, ombh2, omch2, As9 * 1e-9, ns)
            dl = d[2:LMAX_THEORY + 1, 0].copy()
            if with_supp:
                s, _, _ = cr_supp(d, dp, H0, ombh2, omch2)
                dl = dl * s[:len(dl)]
            return arm.chi2(dl)[0]
        except Exception as e:                                    # noqa: BLE001
            print('   ! camb/chi2 failed:', type(e).__name__, e)
            return 1e7
    return f


def _run_fit(tag, arm, with_supp, free_As, budget):
    x0 = X0 if free_As else [X0[0], X0[1], X0[2], X0[4]]
    f = _obj(arm, with_supp, free_As)
    print(f"  fitting {tag}: supp={with_supp} free_As={free_As} budget={budget} "
          f"ndata={arm.ndata}")
    print(f"    chi2 at x0 = {f(x0):.3f}")
    r = minimize(f, x0, method='Nelder-Mead',
                 options={'maxfev': budget, 'xatol': 2e-4, 'fatol': 0.05, 'adaptive': True})
    x = list(map(float, r.x))
    print(f"    {tag}: chi2 = {r.fun:.4f}  nfev = {r.nfev}  x = {[round(v, 6) for v in x]}")
    json.dump({'tag': tag, 'x': x, 'fun': float(r.fun), 'nfev': int(r.nfev),
               'free_As': free_As, 'with_supp': with_supp, 'ndata': arm.ndata},
              open(os.path.join(RUNS, f'{tag}.json'), 'w'), indent=1)
    return x, float(r.fun)


def stage_fitA(budget=600):
    """r7820's convention: BOTH block amplitudes fully free -- so A_s is degenerate and held"""
    ls = np.arange(2, LMAX_THEORY + 1, dtype=float)
    arm = Arm(ls, planck_prior=False)
    _run_fit('fitA_lcdm', arm, False, False, budget)
    _run_fit('fitA_cr', arm, True, False, budget)
    return 0


def stage_fitB(budget=700):
    """the shipped convention: Planck's A ~ N(1, 0.0025), ACT's flat -- A_s is then measurable"""
    ls = np.arange(2, LMAX_THEORY + 1, dtype=float)
    arm = Arm(ls, planck_prior=True)
    _run_fit('fitB_lcdm', arm, False, True, budget)
    _run_fit('fitB_cr', arm, True, True, budget)
    return 0



# ================================================================ Planck-only, the published windows
class PlanckWindow:
    """Planck plik_lite alone over one published window, one free amplitude -- r7471's construction"""

    def __init__(self, ls, lo, hi):
        self.ls = np.asarray(ls, dtype=float)
        cov_ok = np.isfinite(CS.bin_spectrum(self.ls, np.ones_like(self.ls, dtype=float)))
        self.keep = cov_ok & (CS.BIN_LO >= lo) & (CS.BIN_HI <= hi)
        self.F = fisher(CS.COV_TT[np.ix_(self.keep, self.keep)])
        self.D = CS.X_DATA[self.keep]
        self.lo, self.hi = lo, hi

    def binned(self, dl):
        return CS.bin_spectrum(self.ls, dl)[self.keep]

    def chi2(self, dl, d=None):
        return amp_free(self.D if d is None else d, self.F, self.binned(dl))

    def fit_tilt(self, base, d=None):
        def at(dn):
            return self.chi2(base * (self.ls / 1000.0) ** dn, d)[0]
        o = minimize_scalar(at, bounds=(-3.0, 3.0), method='bounded', options={'xatol': 1e-10})
        dn0, c0 = float(o.x), float(o.fun)
        h = 1e-3
        d2 = (at(dn0 + h) - 2 * c0 + at(dn0 - h)) / h ** 2
        return dn0, c0, float(np.sqrt(2.0 / d2))


def tail_chi2_per_bin(ls, dl, lo, hi):
    """the misfit figure r7822 quoted: Planck TT in one tail band, one amplitude, per bin"""
    w = PlanckWindow(ls, lo, hi)
    c, a = w.chi2(dl)
    n = int(w.keep.sum())
    return c / n, n, a


# ================================================================ stage: report
def _load(tag):
    f = os.path.join(RUNS, f'{tag}.json')
    return json.load(open(f)) if os.path.exists(f) else None


def _theory(rec):
    x = rec['x']
    if rec['free_As']:
        H0, ombh2, omch2, As9, ns = x
    else:
        H0, ombh2, omch2, ns = x
        As9 = 2.1
    d, dp = camb_spectrum(H0, ombh2, omch2, As9 * 1e-9, ns)
    dl = d[2:LMAX_THEORY + 1, 0].copy()
    s, r, lD = cr_supp(d, dp, H0, ombh2, omch2)
    return d, dp, dl, s[:len(dl)], r, lD, (H0, ombh2, omch2, As9, ns)


def stage_report():
    out = {}
    ls = np.arange(2, LMAX_THEORY + 1, dtype=float)
    PASS, FAIL = [], []

    def check(label, ok):
        (PASS if ok else FAIL).append(label)
        print(f"    {'PASS' if ok else '*** FAILED'}  {label}")

    print("=" * 100)
    print("r7826 (60) -- the best fit to the joint Planck + ACT data; eleven arms from r7824")
    print("=" * 100)

    # ---------------------------------------------------------------- Ⓐ① and Ⓑ②
    rp = np.load(os.path.join(RUNS, 'repro.npz'))
    print(f"\n  Ⓐ①  REPRODUCTION on the banked control, r7820's own arm "
          f"({int(rp['n_planck'])} Planck + {int(rp['n_act'])} ACT):")
    print(f"       dn_sky {float(rp['dn_sky']):+.6f} +/- {float(rp['sig_sky']):.6f}   "
          f"dn_sig {float(rp['dn_sig']):+.6f}   {float(rp['dist']):.3f} sigma")
    check("Ⓐ① r7822's three landed figures reproduce to their printed digits",
          abs(float(rp['dn_sky']) + 0.020658) < 5e-7 and abs(float(rp['sig_sky']) - 0.003782) < 5e-7
          and abs(float(rp['dn_sig']) + 0.093474) < 5e-7 and abs(float(rp['dist']) - 19.25) < 0.005)
    ok_src, _, _ = supp_source_matches()
    check("Ⓑ② the suppression used here is fit.py's own, character-for-character", ok_src)
    out['repro_dist'] = float(rp['dist'])

    # ---------------------------------------------------------------- the fits
    recs = {t: _load(t) for t in ('fitA_lcdm', 'fitA_cr', 'fitB_lcdm', 'fitB_cr')}
    have = {t: r for t, r in recs.items() if r}
    print(f"\n  the cached fits: {sorted(have)}")
    if not {'fitA_lcdm', 'fitA_cr'} <= set(have):
        print("  ⛔ the primary fits are not cached; run `probe.py fitA` first")
        return 2

    armF = Arm(ls, planck_prior=False)
    armP = Arm(ls, planck_prior=True)
    print(f"\n  the fitted arm: {int(armF.pk.sum())} Planck bins (l_hi < {CUT}, highest "
          f"{armF.p_lmax}) + {int(armF.ak.sum())} ACT bandpowers = {armF.ndata}")

    # ---------------------------------------------------------------- Ⓒ③ interior
    inter = True
    for t, r in have.items():
        x = r['x']
        keys = ('H0', 'ombh2', 'omch2', 'As9', 'ns') if r['free_As'] else \
               ('H0', 'ombh2', 'omch2', 'ns')
        for k, v in zip(keys, x):
            lo, hi = BOUNDS[k]
            edge = min(v - lo, hi - v) / (hi - lo)
            if edge < 0.01:
                inter = False
                print(f"      ! {t} {k} = {v} sits within 1 % of its bound ({lo}, {hi})")
    check("Ⓒ③ every fitted parameter is strictly interior to fit.py's own bounds", inter)

    # ---------------------------------------------------------------- the primary fit
    dA, dpA, dlA, sA, rA, lDA, xA = _theory(have['fitA_lcdm'])
    chi2A = armF.chi2(dlA)
    print(f"\n  ARM I (r7820's amplitude convention, A_s held -- it is degenerate):")
    print(f"       x = H0 {xA[0]:.4f}  omega_b {xA[1]:.6f}  omega_c {xA[2]:.6f}  "
          f"A_s9 {xA[3]:.4f}  n_s {xA[4]:.6f}")
    print(f"       joint chi2 = {chi2A[0]:.4f} over {armF.ndata} points "
          f"({armF.ndata - 3} dof) = {chi2A[0] / (armF.ndata - 3):.4f} per dof")
    print(f"       (Planck {chi2A[1]:.3f} + ACT {chi2A[2]:.3f};  A_planck {chi2A[3]:.5f}, "
          f"A_act {chi2A[4]:.5f})")

    # the A_s degeneracy, demonstrated rather than asserted
    flat = [armF.chi2(dlA * f)[0] for f in (0.8, 0.9, 1.0, 1.1, 1.25)]
    print(f"\n  ⌗ THE DEGENERACY, measured: scaling the whole theory by 0.8 .. 1.25 moves the "
          f"free-amplitude joint chi2 by {max(flat) - min(flat):.3e}")
    flatP = [armP.chi2(dlA * f)[0] for f in (0.9, 1.0, 1.1)]
    print(f"    under the shipped Planck prior the same scalings move it by "
          f"{max(flatP) - min(flatP):.1f}")
    out['as_flatness_free'] = max(flat) - min(flat)
    out['as_flatness_prior'] = max(flatP) - min(flatP)

    # ---------------------------------------------------------------- Ⓓ④ the tail misfit
    print(f"\n  Ⓓ④  THE TAIL MISFIT THE FIT WAS MEANT TO REPAIR (Planck TT, one amplitude):")
    band = {}
    for lo, hi, was in ((1000, 1500, 5.04), (1500, 1760, 9.59)):
        pb, n, a = tail_chi2_per_bin(ls, dlA, lo, hi)
        zb = np.load(os.path.join(SP, 'L824_lcdm_L3200_nk960.npz'))
        cb, nb, _ = tail_chi2_per_bin(zb['ls'].astype(float), zb['Dl'].astype(float), lo, hi)
        band[(lo, hi)] = (pb, cb, was, n)
        print(f"       l {lo}-{hi}: fitted baseline {pb:.4f} per bin over {n} bins   "
          f"banked control {cb:.4f}   r7822 quoted {was}")
    check("Ⓓ④ the fit repairs the tail misfit: both bands fall below 2.0 per bin, "
          "from 5.04 and 9.59",
          band[(1000, 1500)][0] < 2.0 and band[(1500, 1760)][0] < 2.0)
    out['tail_1000_1500'] = band[(1000, 1500)][0]
    out['tail_1500_1760'] = band[(1500, 1760)][0]
    out['tail_1000_1500_banked'] = band[(1000, 1500)][1]
    out['tail_1500_1760_banked'] = band[(1500, 1760)][1]

    # ---------------------------------------------------------------- Ⓔ⑤ / Ⓕ⑥ / Ⓖ⑦
    dn_sky, c_sky, s_sky = armF.fit_tilt(dlA)
    print(f"\n  Ⓔ⑤  THE SKY'S OWN TILT ON THE FITTED BASELINE: "
          f"{dn_sky:+.6f} +/- {s_sky:.6f}  ({abs(dn_sky) / s_sky:.3f} sigma from zero)")
    check("Ⓔ⑤ on the fitted baseline the sky's tilt is consistent with zero (< 2 sigma)",
          abs(dn_sky) / s_sky < 2.0)

    sig_der = dlA * sA
    sig_inh = dlA * np.exp(-(R_INHERITED ** 2 - 1) * (ls / LD_INHERITED) ** 2)
    print(f"\n  Ⓕ⑥  THE SUPPRESSION'S TWO NUMBERS, DERIVED FROM THIS COSMOLOGY:")
    print(f"       r = {rA:.6f}   l_D = {lDA:.4f}")
    print(f"       inherited from r7611+70: r = {R_INHERITED}   l_D = {LD_INHERITED}   "
          f"=> l_D moves {100 * (lDA - LD_INHERITED) / LD_INHERITED:+.2f} %")
    dn_der, _, _ = armF.fit_tilt(dlA, armF.planck_bin(sig_der), armF.act_bin(sig_der))
    dn_inh, _, _ = armF.fit_tilt(dlA, armF.planck_bin(sig_inh), armF.act_bin(sig_inh))
    dist_der = abs(dn_der - dn_sky) / s_sky
    dist_inh = abs(dn_inh - dn_sky) / s_sky
    print(f"\n  Ⓖ⑦  THE SIGNATURE'S DISTANCE FROM THE SKY'S TILT ON THE FITTED BASELINE:")
    print(f"       derived suppression  : dn_sig {dn_der:+.6f}  => {dist_der:.3f} sigma")
    print(f"       inherited pins       : dn_sig {dn_inh:+.6f}  => {dist_inh:.3f} sigma")
    print(f"       the strict 2-sigma rule: "
          f"{'EXCEEDED' if min(dist_der, dist_inh) > 2 else 'NOT exceeded on at least one reading'}")
    check("Ⓕ⑥ the verdict does not turn on the inherited pins: both readings land on the "
          "same side of 2 sigma",
          (dist_der > 2.0) == (dist_inh > 2.0))
    check("Ⓖ⑦ the measurement is made and the 2-sigma rule is applied to it alone",
          np.isfinite(dist_der) and np.isfinite(dist_inh))
    out.update(dn_sky=dn_sky, sig_sky=s_sky, dn_sig_derived=dn_der, dn_sig_inherited=dn_inh,
               dist_derived=dist_der, dist_inherited=dist_inh, r_derived=rA, lD_derived=lDA)


    # ------------------------------------------- BEYOND THE REGISTRATION: WHICH OBJECT IS EXCLUDED
    print(f"\n  ⌗⌗ NOT REGISTERED AT r7824, AND ADDED BECAUSE Ⓖ⑦ ALONE DOES NOT SAY WHICH")
    print(f"     CONFIGURATION THE VERDICT IS ABOUT.  The row's harness prices r = 1.0926; the")
    print(f"     paper's ADJUDICATED endpoint is r = 0.9918, a different object with the opposite")
    print(f"     sign of r^2 - 1.  Each is scored on the same fitted baseline and the same l_D.")
    scope = {}
    c_base = armF.chi2(dlA)[0]
    print(f"     ⌗ and the EXPONENT is a second axis: the row's harness imposes alpha = 1, while the")
    print(f"       paper's faithful source route measures the instrument's own alpha = 1.70.")
    for nm, rr in (('adjudicated endpoint', 0.9918),
                   ("the row's harness", R_INHERITED),
                   ('derived from this fit', rA)):
        for al in (1.0, 1.70):
            s_r = np.exp(-al * (rr ** 2 - 1) * (ls / lDA) ** 2)
            sg = dlA * s_r
            dn_r, _, _ = armF.fit_tilt(dlA, armF.planck_bin(sg), armF.act_bin(sg))
            dist_r = abs(dn_r - dn_sky) / s_sky
            c_r = armF.chi2(sg)[0]
            scope[f'{nm} alpha {al}'] = (rr, al, dn_r, dist_r, c_r - c_base)
            print(f"     {nm:<22} r = {rr:.4f}  alpha {al:.2f}  dn_sig {dn_r:+.6f}  "
                  f"{dist_r:7.3f} sigma   direct Delta chi2 {c_r - c_base:+11.3f}")
    for k, v in scope.items():
        kk = k.replace(' ', '_').replace("'", '').replace('.', 'p')
        out['scope_' + kk + '_dist'] = v[3]
        out['scope_' + kk + '_dchi2'] = v[4]

    # ---------------------------------------------------------------- Ⓗ⑧ the Delta chi2
    print(f"\n  Ⓗ⑧  THE STATISTIC THAT DOES NOT GO NEAR ZERO BY CONSTRUCTION -- "
          f"Delta chi2 AT EQUAL PARAMETER COUNT:")
    rows = []
    for conv, arm, tl, tc in (('r7820 free amplitudes', armF, 'fitA_lcdm', 'fitA_cr'),
                              ('shipped Planck prior', armP, 'fitB_lcdm', 'fitB_cr')):
        if tl in have and tc in have:
            cl, cc = have[tl]['fun'], have[tc]['fun']
            rows.append((conv, cl, cc, cc - cl, have[tl]['x'], have[tc]['x']))
            print(f"       {conv:<22}: LCDM {cl:9.4f}   LCDM x S {cc:9.4f}   "
                  f"Delta chi2 = {cc - cl:+9.4f}  => {np.sqrt(abs(cc - cl)):.2f} sigma-equivalent")
        else:
            print(f"       {conv:<22}: not cached")
    # the ADJUDICATED configuration's own refit -- not registered, added for the same reason as
    # the scope scan above: Ⓗ⑧'s arm refits the suppression cr_supp DERIVES (r about 1.089), and
    # the paper adjudicates r = 0.9918, which no registered arm refits.
    print(f"\n     ⌗⌗ NOT REGISTERED -- the ADJUDICATED configuration's own refit, same five-")
    print(f"        parameter family, same arm, same convention as the first row above:")
    for tag, lbl in (('fitC_adj_a100', 'r 0.9918  alpha 1.00'),
                     ('fitC_adj_a170', 'r 0.9918  alpha 1.70')):
        rc = _load(tag)
        if rc:
            dch = rc['fun'] - have['fitA_lcdm']['fun']
            x = rc['x']
            edge = []
            for k, v in zip(('H0', 'ombh2', 'omch2', 'ns'), x):
                lo, hi = BOUNDS[k]
                if min(v - lo, hi - v) / (hi - lo) < 0.01:
                    edge.append(k)
            print(f"        {lbl}: chi2 {rc['fun']:9.4f}  vs LCDM {have['fitA_lcdm']['fun']:9.4f}"
                  f"   Delta chi2 = {dch:+8.4f}"
                  f"   {'ON A BOUND: ' + ','.join(edge) if edge else 'interior'}")
            out['dchi2_' + tag] = dch
            out['chi2_' + tag] = rc['fun']
    check("Ⓗ⑧ Delta chi2 is measured under at least one convention and its sign is reported",
          len(rows) >= 1)
    if rows:
        out['dchi2_free'] = rows[0][3]
        out['chi2_lcdm_free'] = rows[0][1]
        out['chi2_cr_free'] = rows[0][2]
    if len(rows) > 1:
        out['dchi2_prior'] = rows[1][3]
        out['chi2_lcdm_prior'] = rows[1][1]
        out['chi2_cr_prior'] = rows[1][2]

    # ---------------------------------------------------------------- Ⓘ⑨ Planck-only windows
    print(f"\n  Ⓘ⑨  PLANCK-ONLY BESIDE JOINT, on the fitted baseline, the three published windows:")
    po = {}
    for lo, hi, was in ((100, 1758, 13.74), (700, 1760, 13.18), (1000, 1760, 4.65)):
        w = PlanckWindow(ls, lo, hi)
        d0, _, s0 = w.fit_tilt(dlA)
        d1, _, _ = w.fit_tilt(dlA, w.binned(sig_der))
        dd = abs(d1 - d0) / s0
        po[(lo, hi)] = dd
        print(f"       l {lo}-{hi}: dn_sky {d0:+.6f} +/- {s0:.6f}   dn_sig {d1:+.6f}   "
              f"{dd:.3f} sigma   (r7822 on the banked control: {was})")
    verdicts = {k: v > 2.0 for k, v in po.items()}
    verdicts[('joint',)] = dist_der > 2.0
    check("Ⓘ⑨ Planck-only and joint agree under the 2-sigma rule",
          len(set(verdicts.values())) == 1)
    out['planck_only'] = json.dumps({f'{k[0]}-{k[1]}': v for k, v in po.items()})

    # ---------------------------------------------------------------- Ⓙ⑩ the subsets
    print(f"\n  Ⓙ⑩  THE REACH NO LONGER BINDS -- the two subsets on the same fitted baseline:")
    arm_old = Arm(ls, reach=3200.0, planck_prior=False)
    zb = np.load(os.path.join(SP, 'L824_lcdm_L3200_nk960.npz'))
    old_cov = np.isfinite(CS.bin_spectrum(zb['ls'].astype(float), zb['Dl'].astype(float)))
    arm_old.pk = arm_old.pk & old_cov            # r7820's Planck coverage as well as its reach
    arm_old.PF = fisher(CS.COV_TT[np.ix_(arm_old.pk, arm_old.pk)])
    arm_old.PD = CS.X_DATA[arm_old.pk]
    dn_o, _, s_o = arm_old.fit_tilt(dlA)
    dn_os, _, _ = arm_old.fit_tilt(dlA, arm_old.planck_bin(sig_der), arm_old.act_bin(sig_der))
    dist_o = abs(dn_os - dn_o) / s_o
    print(f"       r7820's subset ({int(arm_old.pk.sum())} Planck + {int(arm_old.ak.sum())} ACT): "
          f"dn_sky {dn_o:+.6f} +/- {s_o:.6f}  => {dist_o:.3f} sigma")
    print(f"       this arm       ({int(armF.pk.sum())} Planck + {int(armF.ak.sum())} ACT): "
          f"dn_sky {dn_sky:+.6f} +/- {s_sky:.6f}  => {dist_der:.3f} sigma")
    check("Ⓙ⑩ the verdict is the same on r7820's subset and on the full arm",
          (dist_o > 2.0) == (dist_der > 2.0))
    out['dist_r7820_subset'] = dist_o
    out['n_act_full'] = int(armF.ak.sum())
    out['n_act_r7820'] = int(arm_old.ak.sum())
    out['n_planck_full'] = int(armF.pk.sum())
    out['n_planck_r7820'] = int(arm_old.pk.sum())

    # ---------------------------------------------------------------- Ⓚ⑪ the count
    print()
    check(f"Ⓚ⑪ eleven arms were registered at r7824 and {len(PASS) + len(FAIL) + 1} ran here",
          len(PASS) + len(FAIL) + 1 == 11)

    print(f"\n  arms run: {len(PASS) + len(FAIL)}   passed {len(PASS)}, FAILED {len(FAIL)}")
    for f in FAIL:
        print(f"    *** {f}")
    np.savez(os.path.join(RUNS, 'r7826_probe.npz'),
             **{k: v for k, v in out.items()},
             n_pass=len(PASS), n_fail=len(FAIL),
             xA=np.array(xA, dtype=float))
    print("\n  ⌗ probe written to runs/r7826_probe.npz")
    return 0 if not FAIL else 1


# ============================================== stage: fitC -- the ADJUDICATED configuration refit
# NOT registered at r7824.  Added because the registration's arms score the suppression at the
# ratio the ROW's harness prices (1.0926, exponent one) while the PAPER adjudicates a different
# configuration (r = 0.9918, and the instrument's own exponent 1.70 on the faithful source route).
# Whether THAT configuration survives a best fit is the number the paper sentence needs, and no
# registered arm measures it.  Flagged as an addition rather than folded in silently.
def _obj_fixed(arm, r_fix, alpha, free_As, As_fixed=2.1):
    def f(pv):
        if free_As:
            H0, ombh2, omch2, As9, ns = pv
        else:
            H0, ombh2, omch2, ns = pv
            As9 = As_fixed
        for k, v in zip(('H0', 'ombh2', 'omch2', 'As9', 'ns'), (H0, ombh2, omch2, As9, ns)):
            lo, hi = BOUNDS[k]
            if not (lo < v < hi):
                return 1e7
        try:
            d, dp = camb_spectrum(H0, ombh2, omch2, As9 * 1e-9, ns)
            dl = d[2:LMAX_THEORY + 1, 0].copy()
            _, _, lD = cr_supp(d, dp, H0, ombh2, omch2)
            ell = np.arange(2, LMAX_THEORY + 1, dtype=float)
            dl = dl * np.exp(-alpha * (r_fix ** 2 - 1) * (ell / lD) ** 2)
            return arm.chi2(dl)[0]
        except Exception as e:                                    # noqa: BLE001
            print('   ! camb/chi2 failed:', type(e).__name__, e)
            return 1e7
    return f


def stage_fitC(budget=600):
    ls = np.arange(2, LMAX_THEORY + 1, dtype=float)
    arm = Arm(ls, planck_prior=False)
    for tag, r_fix, alpha in (('fitC_adj_a170', 0.9918, 1.70),
                              ('fitC_adj_a100', 0.9918, 1.00)):
        f = _obj_fixed(arm, r_fix, alpha, False)
        x0 = [X0[0], X0[1], X0[2], X0[4]]
        print(f"  fitting {tag}: r = {r_fix} alpha = {alpha} budget = {budget}")
        print(f"    chi2 at x0 = {f(x0):.3f}")
        r = minimize(f, x0, method='Nelder-Mead',
                     options={'maxfev': budget, 'xatol': 2e-4, 'fatol': 0.05, 'adaptive': True})
        print(f"    {tag}: chi2 = {r.fun:.4f}  nfev = {r.nfev}  "
              f"x = {[round(v, 6) for v in r.x]}")
        json.dump({'tag': tag, 'x': list(map(float, r.x)), 'fun': float(r.fun),
                   'nfev': int(r.nfev), 'free_As': False, 'with_supp': True,
                   'r_fix': r_fix, 'alpha': alpha, 'ndata': arm.ndata},
                  open(os.path.join(RUNS, f'{tag}.json'), 'w'), indent=1)
    return 0


if __name__ == '__main__':
    stage = sys.argv[1] if len(sys.argv) > 1 else 'repro'
    budget = int(sys.argv[2]) if len(sys.argv) > 2 else None
    if stage == 'repro':
        sys.exit(stage_repro())
    if stage == 'fitA':
        sys.exit(stage_fitA(budget or 600))
    if stage == 'fitC':
        sys.exit(stage_fitC(budget or 600))
    if stage == 'report':
        sys.exit(stage_report())
    if stage == 'fitB':
        sys.exit(stage_fitB(budget or 700))
    if stage == 'srcmatch':
        ok, t, m = supp_source_matches()
        print('Ⓑ② cr_supp source matches fit.py:', ok)
        if not ok:
            print('--- theirs ---'); print(t); print('--- mine ---'); print(m)
        sys.exit(0 if ok else 1)
    print(__doc__)
    sys.exit(2)
