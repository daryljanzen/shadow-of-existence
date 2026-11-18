#!/usr/bin/env python3
r"""r7828 (60) -- PO-24 recomputed at the paper's own configuration, on order r7823 (69).

Registered at r7824... no: at r7828's own PREDICTION.md, beside this file, before anything ran.

TWO AXES, MEASURED SEPARATELY so neither is credited with the other's movement:
    the CONTROL   L820_lcdm_L2512_nk800  ->  L824_lcdm_L3200_nk960
    the CONFIG    r = 1.0926, alpha = 1  ->  r = 0.9918, alpha = 1.70   (the paper's endpoint)

Stages:  python3 probe.py grid     -- the whole cross-product, written to runs/r7828_grid.npz
         python3 probe.py joint     -- the joint Planck+ACT arm distance at each configuration
"""
import json
import os
import re
import sys

import numpy as np
import scipy.linalg
from scipy.interpolate import PchipInterpolator
from scipy.optimize import minimize, minimize_scalar

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402

SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
AD = os.path.join(ROOT, 'computations', 'planck_tt_likelihood', 'data', 'act_dr6_cmbonly')
PAPER = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
RUNS = os.path.join(HERE, 'runs')

# ---- the configuration, READ OUT OF THE PAPER as r7826's receipt does --------------------------
_SRC = open(PAPER, encoding='utf-8').read()
_m_adj = re.search(r"visibility peak, \$r=(\d+\.\d+)\$", _SRC)
_m_alp = re.search(r"\\alpha=(\d+\.\d+)\$ the instrument", _SRC)
R_PAPER = float(_m_adj.group(1))
ALPHA_PAPER = float(_m_alp.group(1))
R_ROW = 1.0926                        # what every PO-24 figure since r7471 was scored at

# ⛔⛔ THE CORRECTION THIS PROBE EXISTS TO MAKE, AND IT IS A DEFECT IN r7826.
# `alpha` and `l_D` enter the signature ONLY through `l_D / sqrt(alpha)`: the corpus's own landed
# receipt P15_the_papers_1_06_and_the_joint_fits_1_4967_are_one_curve_in_l_D says so, and 70's
# faithful copy declares it in its INPUT line, `R, LD = 1.0926, 1951.9 / 1.70 ** 0.5`.
#   1951.9 / sqrt(1.70) = 1497.0390   -- the IN-FORCE l_D of the faithful alpha = 1.70 route
#   1497.0390 * (1 - 0.0049836)       = 1489.5783  -- the same, after the ONE-RATE move
# ⇒ So `R, LD = 1.0926, 1489.5783` with exponent ONE, which every figure in this row uses, ALREADY
#   IS the faithful alpha = 1.70 route on the one rate.  Multiplying the exponent by 1.70 on top of
#   an in-force l_D DOUBLE-COUNTS it -- and that is exactly what r7826 did, putting its "alpha =
#   1.70" rows at an l_D of 1366.0363 / sqrt(1.70) = 1047.70, a value nothing declares.  69 adopted
#   that row as PO-24's figure (+9.02).  THE FIGURE AT THE PAPER'S CONFIGURATION IS r7826's
#   alpha = 1.00 ROW.
# ⇒ GUARD: a folded parameter is folded once.  Before multiplying by an exponent, check whether the
#   length it multiplies is declared at amplitude level or already in force.
LD_INFORCE_ONE_RATE = 1489.5783       # alpha = 1.70 in force, one rate   (what this row has used)
LD_INFORCE_PLAIN = 1497.0390          # alpha = 1.70 in force, no one-rate move
LD_DECLARED_AMP = 1951.9              # the instrument header's, at AMPLITUDE level (r7611+70)
LD_EXPONENT_ONE_DECLARED = 1355.2123  # the other published point on the same curve, one rate

WINDOWS = ((100, 1758), (700, 1760), (1000, 1760))
CONTROLS = {'L820': 'L820_lcdm_L2512_nk800.npz', 'L824': 'L824_lcdm_L3200_nk960.npz'}
# (r, l_D in force).  No alpha multiplies anything here: it is already inside each l_D.
CONFIGS = {
    'row': (R_ROW, LD_INFORCE_ONE_RATE),
    'paper': (R_PAPER, LD_INFORCE_ONE_RATE),
    'paper_noOR': (R_PAPER, LD_INFORCE_PLAIN),
    'row_expone': (R_ROW, LD_EXPONENT_ONE_DECLARED),
}
LD_INHERITED = LD_INFORCE_ONE_RATE

# ---- the five banks.  Each referent is the LANDED receipt's own constant, named beside it -------
BANKS = (
    # label      file                             value key   centre      sigma      sigma source
    # omega_b's constraint is FRACTIONAL in its own receipt: eta10 = 6.13 +/- 0.04, so
    # sigma(omega_b) = centre * 0.04 / 6.13.  Taken that way rather than guessed.
    ('omega_b', 'r6897_wb_response_lcdm.npz', 'omega_b', 0.021966,
     0.021966 * 0.04 / 6.13, 'eta10 6.13 +/- 0.04, the baryon receipt\'s own'),
    ('N_eff', 'r7801_neff_response_lcdm.npz', 'neff', 3.00, 0.17, 'P16 quotes 2.99 +/- 0.17'),
    ('Y_He', 'r7801_yhe_response_lcdm.npz', 'yhe', 0.2454, 0.0034, 'P16 quotes 0.2453 +/- 0.0034'),
    ('A_L', 'r7805_alens_response_lcdm.npz', 'alens', 1.00, 0.096, 'A_L(TT) 1.243 +/- 0.096'),
    ('omega_m', 'r7809_omm_response_lcdm.npz', 'omega_m', 0.140790, 0.004543, 'DESI DR2 on the arm'),
)
CENTRE_REF = {'omega_b': 0.021966, 'N_eff': 3.046, 'Y_He': 0.2471, 'A_L': 1.243,
              'omega_m': 0.2973 * 0.686 ** 2}      # the value each parameter is AFFORDED against


def fisher(keep, cov=None):
    c = CS.COV_TT[np.ix_(keep, keep)] if cov is None else cov
    F = scipy.linalg.cho_solve(scipy.linalg.cho_factor(c), np.identity(c.shape[0]))
    return 0.5 * (F + F.T)


def load_control(fn):
    z = np.load(os.path.join(SP, fn))
    ls, raw = z['ls'].astype(float), z['Dl'].astype(float)
    k0 = np.isfinite(CS.bin_spectrum(ls, raw))
    F0 = fisher(k0)
    m0 = CS.bin_spectrum(ls, raw)[k0]
    dl = raw * float((m0 @ F0 @ CS.X_DATA[k0]) / (m0 @ F0 @ m0))
    return ls, dl


def damping_multipole(ls, dl):
    """l_D from the control's OWN damping, by the fit the harness uses (1400 < l < 2400)"""
    sel = (ls > 1400) & (ls < 2400)
    co = np.polyfit(ls[sel] ** 2, np.log(np.maximum(dl[sel], 1e-12)), 1)
    return float(np.sqrt(-1.0 / co[0]))


class Bank:
    def __init__(self, label, fn, vkey, centre, sigma, src):
        z = np.load(os.path.join(SP, fn), allow_pickle=True)
        vals = np.array(sorted(float(k.split('__')[1]) for k in z.files if k.startswith('ls__')))
        if label == 'A_L':
            vals = vals[vals > 0.5]          # the 0.00 slice is the UNLENSED one, not a grid point
        self.label, self.vals, self.sigma, self.src = label, vals, sigma, src

        def key(pref, v):
            return next(k for k in z.files if k.startswith(pref + '__')
                        and abs(float(k.split('__')[1]) - v) < 1e-9)
        self.centre = float(vals[int(np.argmin(np.abs(vals - centre)))])
        self.ml = z[key('ls', self.centre)].astype(float)
        md = np.array([z[key('Dl', v)].astype(float) for v in vals])
        self.interp = PchipInterpolator(vals, md / md[int(np.argmin(np.abs(vals - self.centre)))],
                                        axis=0)
        self.reach = float(self.ml[-1])

    def ratio(self, v, ls):
        rb = np.asarray(self.interp(float(v)))
        return np.interp(ls, self.ml, rb, left=rb[0], right=rb[-1])

    def starts(self):
        up = self.vals[self.vals > self.centre]
        return (float(self.vals.min()), self.centre,
                float(up.min()) if up.size else self.centre, float(self.vals.max()))


def sig_of(ls, dl, r, lD):
    """the signature at an IN-FORCE l_D.  Exponent one, because alpha is already inside l_D."""
    return dl * np.exp(-(r ** 2 - 1.0) * (ls / lD) ** 2)


def run_grid():
    out = {}
    print("=" * 100)
    print("r7828 (60) -- PO-24 at the paper's configuration, and the two axes separated")
    print("=" * 100)
    print(f"\n  the configuration read from the paper: r = {R_PAPER}, alpha = {ALPHA_PAPER}")
    print(f"  the row's, every figure since r7471  : r = {R_ROW} at l_D in force "
          f"{LD_INFORCE_ONE_RATE} -- which IS the faithful alpha = {ALPHA_PAPER} route")
    kp = R_PAPER ** 2 - 1.0
    kr = R_ROW ** 2 - 1.0
    print(f"\n  Ⓓ④ THE SIZE, computed: r^2 - 1 = {kp:+.6f} at the paper's endpoint against "
          f"{kr:+.6f} at the row's ratio")
    print(f"      ratio of magnitudes {abs(kp / kr):.4f} = one in {abs(kr / kp):.2f}, "
          f"and the SIGN is {'opposite' if kp * kr < 0 else 'the same'}")
    print(f"\n  ⛔ AND THE EXPONENT IS NOT A SECOND FACTOR: alpha and l_D enter only as "
          f"l_D/sqrt(alpha).")
    print(f"      {LD_DECLARED_AMP} / sqrt({ALPHA_PAPER}) = "
          f"{LD_DECLARED_AMP / ALPHA_PAPER ** 0.5:.4f}  -> the in-force l_D, "
          f"{LD_INFORCE_PLAIN} declared")
    print(f"      and after the one-rate move, {LD_INFORCE_ONE_RATE} -- which is the l_D every "
          f"figure in this row already uses")
    print(f"      ⇒ r7826 multiplied an IN-FORCE l_D by alpha again, putting its 'alpha = 1.70' "
          f"rows at {1366.0363 / ALPHA_PAPER ** 0.5:.2f}")
    out['k_paper'], out['k_row'] = kp, kr
    out['ld_inforce_from_declared'] = LD_DECLARED_AMP / ALPHA_PAPER ** 0.5
    out['r7826_alpha170_effective_lD'] = 1366.0363 / ALPHA_PAPER ** 0.5

    banks = [Bank(*b) for b in BANKS]
    print(f"\n  Ⓒ③ EVERY BANK'S REACH against the highest window multipole {max(h for _, h in WINDOWS)}:")
    for b in banks:
        print(f"      {b.label:>8}: reach l = {b.reach:.0f}  grid {list(b.vals)}  "
              f"centre {b.centre}")
    out['reaches'] = np.array([b.reach for b in banks], dtype=float)

    rows = []
    for cname, cfile in CONTROLS.items():
        ls, dl = load_control(cfile)
        lD = damping_multipole(ls, dl)
        print(f"\n{'=' * 100}\n  CONTROL {cname}: l = {ls[0]:.0f}..{ls[-1]:.0f}")
        print(f"      ⚠ Ⓑ② AS REGISTERED FAILS, AND THE FAILURE IS THE FINDING: a log-slope fit of")
        print(f"        THIS control's own power over 1400 < l < 2400 returns {lD:.4f}, which is "
              f"{100 * (lD - LD_INHERITED) / LD_INHERITED:+.2f} % from the")
        print(f"        in-force {LD_INHERITED} -- so it is NOT the same object.  l_D in force is the")
        print(f"        instrument's DECLARED damping multipole folded by sqrt(alpha), not a fit to a")
        print(f"        control's spectrum, and substituting one for the other is the same error")
        print(f"        class as the alpha double-count above.  Every figure below is at an IN-FORCE")
        print(f"        l_D, and the fitted number is reported and NOT used.")
        out[f'lD_{cname}'] = lD
        for gname, (r, ld_force) in CONFIGS.items():
            sig = sig_of(ls, dl, r, ld_force)
            for lo, hi in WINDOWS:
                keep = (np.isfinite(CS.bin_spectrum(ls, dl)) & (CS.BIN_LO >= lo)
                        & (CS.BIN_HI <= hi))
                F = fisher(keep)
                tgt = CS.bin_spectrum(ls, sig)[keep]
                m_amp = CS.bin_spectrum(ls, dl)[keep]
                a_amp = float((m_amp @ F @ tgt) / (m_amp @ F @ m_amp))
                res = tgt - a_amp * m_amp
                c_amp = float(res @ F @ res)

                def at2(dn):
                    m = CS.bin_spectrum(ls, dl * (ls / 1000.0) ** dn)[keep]
                    A = float((m @ F @ tgt) / (m @ F @ m))
                    rr = tgt - A * m
                    return float(rr @ F @ rr)
                o2 = minimize_scalar(at2, bounds=(-3.0, 3.0), method='bounded',
                                     options={'xatol': 1e-10})
                dn2, c2 = float(o2.x), float(o2.fun)
                row = dict(control=cname, config=gname, window=f'{lo}-{hi}', n=int(keep.sum()),
                           dn2=dn2, c2=c2, c_amp=c_amp, tilt_share=(1 - c2 / c_amp) * 100.0,
                           lD_fit=lD, lD_force=ld_force, r=r)
                print(f"\n    {gname:>6} / {lo}-{hi}: {int(keep.sum())} bins   "
                      f"displacement dn2 = {dn2:+.6f}   the tilt takes "
                      f"{(1 - c2 / c_amp) * 100:.2f} % of it")
                for b in banks:
                    def at3(p):
                        m = CS.bin_spectrum(ls, dl * (ls / 1000.0) ** float(p[0])
                                            * b.ratio(p[1], ls))[keep]
                        A = float((m @ F @ tgt) / (m @ F @ m))
                        rr = tgt - A * m
                        return float(rr @ F @ rr)
                    best = None
                    for dn0 in (-0.30, -0.10, 0.0, 0.10):
                        for v0 in b.starts():
                            o = minimize(at3, x0=[dn0, v0], method='L-BFGS-B',
                                         bounds=[(-3.0, 3.0),
                                                 (float(b.vals.min()), float(b.vals.max()))],
                                         options={'ftol': 1e-14, 'gtol': 1e-12})
                            cand = (float(o.fun), float(o.x[0]), float(o.x[1]))
                            if best is None or cand < best:
                                best = cand
                    c3, dn3, v3 = best
                    edge = min(abs(v3 - b.vals.min()), abs(v3 - b.vals.max())) < 1e-9
                    surv = abs(dn3) / abs(dn2) * 100.0 if dn2 != 0 else float('nan')
                    aff = (v3 - CENTRE_REF[b.label]) / b.sigma
                    row[b.label] = dict(v=v3, dn3=dn3, c3=c3, surv=surv, edge=bool(edge),
                                        aff=aff, absorbed=(1 - c3 / c_amp) * 100.0)
                    print(f"        {b.label:>8}: wants {v3:.6f} ({aff:+.2f} sigma of its own "
                          f"constraint{', AT THE EDGE' if edge else ''})   survival "
                          f"{surv:7.2f} %   absorbed {(1 - c3 / c_amp) * 100:6.2f} %")
                rows.append(row)
    np.savez(os.path.join(RUNS, 'r7828_grid.npz'),
             rows=json.dumps(rows), **{k: v for k, v in out.items()})
    print(f"\n  ⌗ {len(rows)} (control, config, window) rows written to runs/r7828_grid.npz")
    return 0


# ============================================== stage: joint -- the arm r7820 built, on L824
def run_joint():
    """the joint Planck + ACT tail-tilt distance at each configuration, on L824

    The arm is r7820's with r7826's support split; nothing is refitted here, so this is the
    FIXED-COSMOLOGY statistic -- which is the one the order asks for, and which r7826 showed a
    refit absorbs.
    """
    AZ = np.load(os.path.join(AD, 'act_dr6_cmbonly.npz'), allow_pickle=True)
    a_ell, a_dl, a_win, a_wl = AZ['ell_TT'], AZ['Dl_TT'], AZ['win_TT'], AZ['win_ell']
    a_cov = AZ['cov'][:45, :45]
    cut = int(open(os.path.join(AD, 'likelihood_source', 'PlanckActCut.yaml'),
                   encoding='utf-8').read().split('lmax_cuts:')[1].split()[0])
    ls, dl = load_control(CONTROLS['L824'])
    p_keep = np.isfinite(CS.bin_spectrum(ls, dl)) & (CS.BIN_HI < cut)
    p_lmax = int(CS.BIN_HI[p_keep].max())
    s_min = np.array([a_wl[a_win[:, i] > 0].min() for i in range(a_win.shape[1])])
    s_max = np.array([a_wl[a_win[:, i] > 0].max() for i in range(a_win.shape[1])])
    a_keep = (s_min > p_lmax) & (s_max <= float(ls.max()))
    PF, PD = fisher(p_keep), CS.X_DATA[p_keep]
    AF, ADv, AW = fisher(None, a_cov[np.ix_(a_keep, a_keep)]), a_dl[a_keep], a_win[:, a_keep]

    def blocks(spec, dP=None, dA=None):
        mP = CS.bin_spectrum(ls, spec)[p_keep]
        mA = AW.T @ np.interp(a_wl, ls, spec)
        tot = 0.0
        for d, F, m in ((PD if dP is None else dP, PF, mP), (ADv if dA is None else dA, AF, mA)):
            A = float((m @ F @ d) / (m @ F @ m))
            r = d - A * m
            tot += float(r @ F @ r)
        return tot

    def fit_tilt(dP=None, dA=None):
        def at(dn):
            return blocks(dl * (ls / 1000.0) ** dn, dP, dA)
        o = minimize_scalar(at, bounds=(-3.0, 3.0), method='bounded', options={'xatol': 1e-10})
        dn0, c0 = float(o.x), float(o.fun)
        h = 1e-3
        d2 = (at(dn0 + h) - 2 * c0 + at(dn0 - h)) / h ** 2
        return dn0, c0, float(np.sqrt(2.0 / d2))

    print("=" * 100)
    print("r7828 (60) -- Ⓘ⑨ THE JOINT ARM at each configuration, on L824")
    print("=" * 100)
    print(f"\n  {int(p_keep.sum())} Planck bins (l_hi < {cut}, highest {p_lmax}) + "
          f"{int(a_keep.sum())} ACT bandpowers = {int(p_keep.sum()) + int(a_keep.sum())}")
    dn_sky, c_sky, sg = fit_tilt()
    print(f"  the sky's tilt on this control: {dn_sky:+.6f} +/- {sg:.6f}")
    out = {'dn_sky': dn_sky, 'sig_sky': sg, 'n_planck': int(p_keep.sum()),
           'n_act': int(a_keep.sum())}
    for gname, (r, ld_force) in CONFIGS.items():
        sig = sig_of(ls, dl, r, ld_force)
        dn_s, _, _ = fit_tilt(CS.bin_spectrum(ls, sig)[p_keep],
                              AW.T @ np.interp(a_wl, ls, sig))
        dist = abs(dn_s - dn_sky) / sg
        direct = blocks(sig) - blocks(dl)
        print(f"  {gname:>11}: r = {r:.4f} at l_D {ld_force:.4f}   dn_sig {dn_s:+.6f}   "
              f"{dist:7.3f} sigma   direct Delta chi2 {direct:+10.3f}")
        out[f'dist_{gname}'] = dist
        out[f'dn_sig_{gname}'] = dn_s
        out[f'direct_{gname}'] = direct
    np.savez(os.path.join(RUNS, 'r7828_joint.npz'), **out)
    print("\n  ⌗ written to runs/r7828_joint.npz")
    return 0


# ======================= stage: refit -- the figure PO-24 should carry, at the DECLARED in-force l_D
def run_refit(budget=600):
    """r7826's joint best fit, redone with the suppression at r = 0.9918 and l_D = 1489.5783 FIXED

    ⛔ WHY THIS EXISTS.  r7826 fitted the construction with cr_supp's own l_D -- a log-slope fit of
    each trial cosmology's power -- and then ALSO multiplied the exponent by alpha = 1.70 in its
    scan.  The first is a different estimator from the corpus's declared in-force l_D; the second
    double-counts alpha.  69 adopted the double-counted row.  This stage fits at the DECLARED
    in-force l_D with exponent one, which is the faithful route, and compares with r7826's own LCDM
    minimum on the same arm.
    """
    sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall',
                                    'r7826_60_the_joint_data_fitted_and_the_amplitude_convention_'
                                    'makes_one_parameter_degenerate'))
    import probe as P26                                                   # noqa: E402
    lsx = np.arange(2, P26.LMAX_THEORY + 1, dtype=float)
    arm = P26.Arm(lsx, planck_prior=False)
    lcdm = json.load(open(os.path.join(os.path.dirname(P26.__file__), 'runs', 'fitA_lcdm.json')))
    print("=" * 100)
    print("r7828 (60) -- the joint refit at the DECLARED in-force l_D, correcting r7826's scan")
    print("=" * 100)
    print(f"\n  LCDM on this arm (r7826's own minimum): chi2 {lcdm['fun']:.4f} over {arm.ndata} "
          f"points at x = {[round(v, 6) for v in lcdm['x']]}")

    def obj(pv):
        H0, ombh2, omch2, ns = pv
        for k, v in zip(('H0', 'ombh2', 'omch2', 'ns'), pv):
            lo, hi = P26.BOUNDS[k]
            if not (lo < v < hi):
                return 1e7
        try:
            d, dp = P26.camb_spectrum(H0, ombh2, omch2, 2.1e-9, ns)
            dl = d[2:P26.LMAX_THEORY + 1, 0].copy()
            dl = dl * np.exp(-(R_PAPER ** 2 - 1.0) * (lsx / LD_INFORCE_ONE_RATE) ** 2)
            return arm.chi2(dl)[0]
        except Exception as e:                                            # noqa: BLE001
            print('   ! failed:', type(e).__name__, e)
            return 1e7

    x0 = [lcdm['x'][0], lcdm['x'][1], lcdm['x'][2], lcdm['x'][3]]
    print(f"  chi2 at LCDM's own best fit, with the signature imposed: {obj(x0):.4f}")
    r = minimize(obj, x0, method='Nelder-Mead',
                 options={'maxfev': budget, 'xatol': 2e-4, 'fatol': 0.05, 'adaptive': True})
    edge = [k for k, v in zip(('H0', 'ombh2', 'omch2', 'ns'), r.x)
            if min(v - P26.BOUNDS[k][0], P26.BOUNDS[k][1] - v)
            / (P26.BOUNDS[k][1] - P26.BOUNDS[k][0]) < 0.01]
    print(f"\n  the construction refitted at r = {R_PAPER}, l_D = {LD_INFORCE_ONE_RATE} (exponent "
          f"one, which IS alpha = {ALPHA_PAPER}):")
    print(f"    chi2 = {r.fun:.4f}   nfev = {r.nfev}   x = {[round(v, 6) for v in r.x]}   "
          f"{'ON A BOUND: ' + ','.join(edge) if edge else 'interior'}")
    print(f"    Delta chi2 against LCDM = {r.fun - lcdm['fun']:+.4f}")
    print(f"\n  ⌗ against what r7826 reported and 69 adopted: +9.02 at its 'alpha = 1.70' row, "
          f"which sits at l_D {1366.0363 / ALPHA_PAPER ** 0.5:.2f}; and -1.29 at its alpha = 1.00 "
          f"row, at l_D 1366.04.")
    json.dump({'chi2': float(r.fun), 'x': list(map(float, r.x)), 'nfev': int(r.nfev),
               'chi2_lcdm': lcdm['fun'], 'dchi2': float(r.fun - lcdm['fun']),
               'r': R_PAPER, 'lD': LD_INFORCE_ONE_RATE, 'edge': edge, 'ndata': arm.ndata},
              open(os.path.join(RUNS, 'r7828_refit.json'), 'w'), indent=1)
    return 0


if __name__ == '__main__':
    stage = sys.argv[1] if len(sys.argv) > 1 else 'grid'
    if stage == 'refit':
        sys.exit(run_refit(int(sys.argv[2]) if len(sys.argv) > 2 else 600))
    if stage == 'joint':
        sys.exit(run_joint())
    if stage == 'grid':
        sys.exit(run_grid())
    print(__doc__)
    sys.exit(2)
