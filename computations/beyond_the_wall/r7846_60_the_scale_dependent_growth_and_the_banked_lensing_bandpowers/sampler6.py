#!/usr/bin/env python3
"""** THE SIX-PARAMETER CHAIN: r7844's SAMPLER, DIMENSION-GENERAL, ON THE JOINT SCORE. **

Order `r7845` ③.  Everything `r7844` repaired is kept and none of it is re-derived here: the
proposal covariance from the CURVATURE at the minimum rather than a hard-coded diagonal, the starts
dispersed in that covariance's own metric, the refusal of a chain that did not move, and every limit
recorded with its own Monte-Carlo standard error beside it.

⌗ *`r7844` wrote two criteria finer than the quantile they judged and had to report a correct
prediction as refuted.  The error is recorded in the sampler itself -- `quantile_mcse` carries the
reason in its docstring -- so the next seat meets it at the point of use.*

    x = [H0, OM, WB, NS  (grid-step offsets),  Sum (eV),  tau]
"""
import json
import os
import sys
import time

import numpy as np
from scipy.optimize import minimize

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
import lensing_like as LL                                                # noqa: E402
import model6 as M6                                                      # noqa: E402

NAMES = ('H0', 'OM', 'WB', 'NS', 'MNU', 'TAU')
NDIM = len(NAMES)
CHAINS = int(os.environ.get('CHAINS', '6'))
BURN = int(os.environ.get('BURN', '24000'))
KEEP = int(os.environ.get('KEEP', '240000'))
THIN = int(os.environ.get('THIN', '20'))
SEED = int(os.environ.get('SEED', '7846'))
OUT = os.path.join(_HERE, os.environ.get('OUTNAME', 'sampler6.json'))
PUBLISHED_LIMIT_MEV = 64.2
PUBLISHED_EFFECTIVE_EV = -0.101
# ** THE DISTANCE POINT PER ARM, TAKEN FROM r7844's SAMPLER AND NOT DEFAULTED. **  A first draft
#   read it off `model3` with a fallback to the control's pair, which would have silently scored the
#   ARM OF RECORD against the control's distances -- a wrong number that no arm would have caught,
#   because the gap is reported and not pinned.
DIST_POINT = {'lcdm': (68.5, 0.2975), 'cr': (68.60, 0.2973)}


def rhat(x):
    """split Gelman-Rubin on (chains, draws)"""
    c, n = x.shape
    h = n // 2
    s = np.concatenate([x[:, :h], x[:, h:2 * h]], 0)
    m, v = s.mean(1), s.var(1, ddof=1)
    B = h * s.mean(1).var(ddof=1)
    W = v.mean()
    return float(np.sqrt(((h - 1) / h * W + B / h) / W)) if W > 0 else np.inf


def ess(x):
    c, n = x.shape
    N = c * n
    m = x.mean()
    V = x.var(ddof=1)
    if V <= 0:
        return 0.0
    s = 0.0
    for t in range(1, min(n - 1, 2000)):
        p = np.mean([(x[i, :-t] - m) * (x[i, t:] - m) for i in range(c)]) / V
        if p < 0.05:
            break
        s += p
    return float(V * N / (1.0 + 2.0 * s) / V)


def quantile_mcse(s, n_eff, q=0.95):
    """the Monte-Carlo standard error of a sample quantile -- see r7844, which needed it twice"""
    s = np.asarray(s, float)
    xq = float(np.quantile(s, q))
    h = 1.06 * float(s.std(ddof=1)) * len(s) ** -0.2
    f = float(np.mean(np.exp(-0.5 * ((s - xq) / h) ** 2)) / (h * np.sqrt(2 * np.pi)))
    return float(1000.0 * np.sqrt(q * (1.0 - q) / float(n_eff)) / f)


def best_fit(mod, bounded):
    """the minimum, with any result landing on the barrier DISCARDED rather than reported"""
    lo = 0.0 if bounded else mod.cmb.s_lo
    bnds = [(-6, 6)] * 4 + [(lo, mod.s_hi), (M6.TAU_LO, M6.TAU_HI)]
    f = lambda z: mod.chi2_barrier(z, lo)                                # noqa: E731
    starts = [[0, 0, 0, 0, max(lo, 0.02), 0.054], [0.5, -0.5, 0.3, -0.3, max(lo, 0.10), 0.03],
              [-0.5, 0.5, -0.3, 0.3, max(lo, 0.20), 0.08], [0, 0, 0, 0, max(lo, 0.0), 0.054],
              [0.2, 0.2, -0.2, 0.2, max(lo, 0.15), 0.02]]
    best = None
    for st in starts:
        st = list(np.clip(st, [-6] * 4 + [lo, M6.TAU_LO], [6] * 4 + [mod.s_hi, M6.TAU_HI]))
        for meth in ('Nelder-Mead', 'Powell'):
            r = minimize(f, st, method=meth, bounds=bnds,
                         options=dict(maxiter=200000, maxfev=200000))
            if r.fun >= 1e5:
                continue
            if best is None or r.fun < best.fun:
                best = r
    if best is None:
        raise SystemExit('every start landed on the barrier -- REFUSING to report a minimum')
    for _ in range(3):
        r = minimize(f, best.x, method='Nelder-Mead', bounds=bnds,
                     options=dict(maxiter=200000, maxfev=200000, xatol=1e-8, fatol=1e-10))
        if r.fun < best.fun:
            best = r
    assert abs(f(best.x) - best.fun) < 1e-6, 'the reported minimum is not the objective at its point'
    return best


FALLBACK_SD = np.array([0.25, 0.01, 2e-4, 0.01, 0.05, 0.007])


def laplace_cov(mod, x0, lo, hi):
    """the proposal covariance from the curvature at the minimum -- r7844's repair, at NDIM

    ** AND A DIRECTION WHOSE CURVATURE COULD NOT BE MEASURED IS NAMED, NOT SILENTLY FROZEN. **
    `r7844`'s repair takes the step for each second difference from a one-dimensional probe that
    walks outward until `chi^2` moves by `1`.  If the minimum sits ON a bound, that probe hits the
    bound immediately, the step comes back at its floor, and the curvature comes back enormous --
    so the proposal's width in that direction comes back at `1e-8` and the chain never moves in it.

    *That happened on the arm of record at the first attempt:* its unbounded minimum is at
    `Sum = -0.1200` eV, exactly the model's lower bound, and the sum's proposal width came back
    `1.08e-08` eV.  ** r7844's refusal guard did not catch it, because it tests the AGGREGATE
    acceptance and the other five directions were moving perfectly well. **  A chain can be dead in
    one direction and healthy on the arithmetic that was supposed to notice.

    ⇒ So a probe that terminated against a bound rather than against `chi^2` is RECORDED, that
    direction takes a stated fallback width instead of the curvature's, and the caller is told
    which directions those were.
    """
    x0 = np.asarray(x0, float)
    h = np.empty(NDIM)
    at_bound = []
    f0 = mod.chi2(x0)
    for i in range(NDIM):
        t = 1e-4
        hit_bound = False
        for _ in range(60):
            e = np.zeros(NDIM)
            e[i] = t
            z = x0 + e
            if not (lo <= z[4] <= hi) or not (M6.TAU_LO <= z[5] <= M6.TAU_HI) \
                    or np.any(np.abs(z[:4]) > 6):
                hit_bound = True
                break
            if mod.chi2(z) - f0 > 1.0:
                break
            t *= 1.4
        if hit_bound and t <= 1e-3:
            at_bound.append(NAMES[i])
        h[i] = max(t / 4.0, 1e-8)
    H = np.zeros((NDIM, NDIM))
    for i in range(NDIM):
        for j in range(i, NDIM):
            ei, ej = np.zeros(NDIM), np.zeros(NDIM)
            ei[i], ej[j] = h[i], h[j]
            if i == j:
                H[i, i] = (mod.chi2(x0 + ei) - 2 * f0 + mod.chi2(x0 - ei)) / h[i] ** 2
            else:
                H[i, j] = H[j, i] = (mod.chi2(x0 + ei + ej) - mod.chi2(x0 + ei - ej)
                                     - mod.chi2(x0 - ei + ej) + mod.chi2(x0 - ei - ej)) \
                    / (4 * h[i] * h[j])
    H = 0.5 * (H + H.T)
    try:
        C = 2.0 * np.linalg.inv(H)
        C = 0.5 * (C + C.T)
        np.linalg.cholesky(C)
        ok = bool(np.all(np.isfinite(C)) and np.all(np.diag(C) > 0))
    except np.linalg.LinAlgError:
        ok = False
    if not ok:
        print('       the curvature is not positive definite -- diagonal fallback, recorded',
              flush=True)
        return np.diag(FALLBACK_SD ** 2), False, at_bound
    # a direction whose probe died on a bound gets a stated width, and the swap is announced
    sd = np.sqrt(np.diag(C))
    for i, nm in enumerate(NAMES):
        if nm in at_bound or sd[i] < 1e-4 * FALLBACK_SD[i]:
            print('       %s: the curvature could not be measured (the minimum is on a bound); '
                  'its proposal width is the stated fallback %.3g and NOT %.3g'
                  % (nm, FALLBACK_SD[i], sd[i]), flush=True)
            C[i, :] = 0.0
            C[:, i] = 0.0
            C[i, i] = FALLBACK_SD[i] ** 2
            if nm not in at_bound:
                at_bound.append(nm)
    return C, True, at_bound


def run_chains(mod, bounded, x0, S0, rng):
    lo = 0.0 if bounded else mod.cmb.s_lo
    hi = mod.s_hi

    def logp(z):
        if not (lo <= z[4] <= hi) or not (M6.TAU_LO <= z[5] <= M6.TAU_HI) \
                or np.any(np.abs(z[:4]) > 6):
            return -np.inf
        c = mod.chi2(z)
        return -np.inf if c >= 1e11 else -0.5 * c

    L0 = np.linalg.cholesky(S0)
    cur = []
    for i in range(CHAINS):
        for _ in range(400):
            z = np.array(x0, float) + (L0 @ rng.standard_normal(NDIM)) * (0.5 + 0.5 * i)
            z[4] = float(np.clip(z[4], lo, hi))
            z[5] = float(np.clip(z[5], M6.TAU_LO, M6.TAU_HI))
            if np.isfinite(logp(z)):
                break
        cur.append(z)
    cur = np.asarray(cur)
    lcur = np.array([logp(z) for z in cur])
    assert np.all(np.isfinite(lcur)), 'a chain could not be started at a finite point'

    S = np.asarray(S0, float)
    fac = 2.38 ** 2 / NDIM
    STAGES = 6
    per = max(400, BURN // STAGES)
    for st in range(STAGES):
        L = np.linalg.cholesky(S * fac)
        hist, acc = [], 0
        for t in range(per):
            for i in range(CHAINS):
                prop = cur[i] + L @ rng.standard_normal(NDIM)
                lp = logp(prop)
                if lp > lcur[i] or np.log(rng.random()) < lp - lcur[i]:
                    cur[i], lcur[i] = prop, lp
                    acc += 1
            hist.append(cur.copy())
        rate = acc / float(per * CHAINS)
        H = np.asarray(hist[per // 2:]).reshape(-1, NDIM)
        C = np.cov(H.T)
        if np.all(np.isfinite(C)) and np.linalg.det(C) > 0:
            S = C + 1e-16 * np.eye(NDIM)
        fac *= float(np.exp(np.clip((rate - 0.234) * 3.0, -1.0, 1.0)))
        print(f'       burn stage {st + 1}/{STAGES}: accept {rate:.3f}, scale factor now '
              f'{fac:.4f}', flush=True)
    burn_rate = rate

    L = np.linalg.cholesky(S * fac)
    out = np.empty((CHAINS, KEEP // THIN, NDIM))
    acc = 0
    for t in range(KEEP):
        for i in range(CHAINS):
            prop = cur[i] + L @ rng.standard_normal(NDIM)
            lp = logp(prop)
            if lp > lcur[i] or np.log(rng.random()) < lp - lcur[i]:
                cur[i], lcur[i] = prop, lp
                acc += 1
        if t % THIN == 0:
            out[:, t // THIN, :] = cur
    rate = acc / float(KEEP * CHAINS)
    assert 0.03 <= rate <= 0.70, (
        f'the kept chain accepted {rate:.4f} of its proposals -- REFUSING to report a chain that '
        f'did not move (burn ended at {burn_rate:.4f})')
    # ** PER-DIRECTION, BECAUSE THE AGGREGATE RATE CANNOT SEE A SINGLE FROZEN PARAMETER. **  The
    #   arm of record's first attempt accepted 0.30 of its proposals while its sum direction had a
    #   proposal width of 1e-8 eV: healthy on the only number r7844 checked, dead on the one the
    #   limit is read off.
    flat = out.reshape(-1, NDIM)
    dead = [NAMES[j] for j in range(NDIM)
            if float(flat[:, j].std(ddof=1)) < 1e-6 * max(abs(float(flat[:, j].mean())), 1e-3)]
    assert not dead, ('these direction(s) did not move across the kept chain: %s -- REFUSING to '
                      'report a chain that is frozen in a parameter the result is read off'
                      % ', '.join(dead))
    return out, rate, burn_rate


def summarise(mod, arm, bounded, S, rate, burn_rate):
    lab = 'bounded' if bounded else 'unbounded'
    diag = {nm: dict(rhat=rhat(S[:, :, j]), ess=ess(S[:, :, j])) for j, nm in enumerate(NAMES)}
    flat = S.reshape(-1, NDIM)
    s = flat[:, 4]
    c = M6.M3.ARMS[arm]['centre']
    H0 = c['H0'] + M6.M3.R.STEP['H0'] * flat[:, 0]
    OM = c['OM'] + M6.M3.R.STEP['OM'] * flat[:, 1]
    h0d, omd = DIST_POINT[arm]
    gap = 100.0 * ((OM * (H0 / 100.0) ** 2) / (omd * (h0d / 100.0) ** 2) - 1.0)
    res = dict(label=lab, arm=arm, chains=int(S.shape[0]), kept_per_chain=int(S.shape[1]),
               accept=float(rate), burn_accept=float(burn_rate), diagnostics=diag,
               mean={nm: float(flat[:, j].mean()) for j, nm in enumerate(NAMES)},
               sd={nm: float(flat[:, j].std(ddof=1)) for j, nm in enumerate(NAMES)},
               sum_mean_ev=float(s.mean()), sum_sd_ev=float(s.std(ddof=1)),
               sum_q=[float(np.quantile(s, q)) for q in (0.025, 0.16, 0.5, 0.84, 0.95, 0.975)],
               tau_mean=float(flat[:, 5].mean()), tau_sd=float(flat[:, 5].std(ddof=1)),
               gap_mean_pc=float(gap.mean()), gap_sd_pc=float(gap.std(ddof=1)))
    if bounded:
        res['upper95_mev'] = float(np.quantile(s, 0.95) * 1000.0)
        res['upper95_mcse_mev'] = quantile_mcse(s, diag['MNU']['ess'], 0.95)
        res['upper95_per_chain_mev'] = [float(np.quantile(S[i, :, 4], 0.95) * 1000.0)
                                        for i in range(S.shape[0])]
        res['factor_vs_published'] = float(PUBLISHED_LIMIT_MEV / res['upper95_mev'])
        for q in (0.059, 0.064):
            res[f'frac_below_{q}'] = float((s < q).mean())
    bf = best_fit(mod, bounded)
    res['best_fit'] = dict(chi2=float(bf.fun), x=[float(v) for v in bf.x])
    print(f"  [{arm}/{lab}] accept {rate:.3f} (burn {burn_rate:.3f});  "
          f"Sum = {s.mean() * 1000:+.1f} +/- {s.std(ddof=1) * 1000:.1f} meV;  "
          f"tau = {flat[:, 5].mean():.4f} +/- {flat[:, 5].std(ddof=1):.4f};  "
          f"gap {gap.mean():+.2f} pc;  chi2min {bf.fun:.2f}", flush=True)
    print('     R-hat ' + '  '.join(f'{nm}={diag[nm]["rhat"]:.4f}' for nm in NAMES), flush=True)
    print('     ESS   ' + '  '.join(f'{nm}={diag[nm]["ess"]:.0f}' for nm in NAMES), flush=True)
    if bounded:
        _pc = res['upper95_per_chain_mev']
        print(f"     95 per cent upper limit: {res['upper95_mev']:.2f} +/- "
              f"{res['upper95_mcse_mev']:.2f} meV against the published {PUBLISHED_LIMIT_MEV} -- "
              f"a factor {res['factor_vs_published']:.2f}  (six chains span "
              f"{max(_pc) - min(_pc):.2f})", flush=True)
    return res


def main():
    arm = sys.argv[1] if len(sys.argv) > 1 else 'lcdm'
    rng = np.random.default_rng(SEED)
    t0 = time.time()
    mod = M6.Model6(arm)
    print('  %s: %d CMB bins + %d lensing bandpowers, tau sampled   (model built in %.1f s)'
          % (arm, int(mod.cmb.ok.sum()), LL.NBP, time.time() - t0), flush=True)
    mod.cmb._build_bao_spline()
    err = mod.cmb.bao_error(rng, 200)
    print('    BAO tabulated: worst |spline - honest| = %.3e over 200 draws' % err, flush=True)
    assert err < 1e-3, 'the tabulated BAO term is not accurate enough to sample on'
    bf0 = best_fit(mod, False)
    print('    unbounded minimum chi2 = %.3f at Sum = %+.4f eV, tau = %.4f'
          % (bf0.fun, bf0.x[4], bf0.x[5]), flush=True)
    S0, ok, at_bound = laplace_cov(mod, bf0.x, mod.cmb.s_lo, mod.s_hi)
    print('    proposal sd from the curvature: '
          + '  '.join('%.3g' % v for v in np.sqrt(np.diag(S0)))
          + ('' if ok else '   (DIAGONAL FALLBACK)'), flush=True)
    all_res = {f'{arm}_proposal': dict(from_curvature=bool(ok),
                                       sd=[float(v) for v in np.sqrt(np.diag(S0))],
                                       curvature_unmeasurable_in=at_bound,
                                       minimum_on_a_bound=bool(at_bound)),
               f'{arm}_bao': dict(spline_worst_error=float(err))}
    for bounded in (True, False):
        S, rate, br = run_chains(mod, bounded, bf0.x, S0, rng)
        all_res[f'{arm}_{"bounded" if bounded else "unbounded"}'] = \
            summarise(mod, arm, bounded, S, rate, br)
        np.savez_compressed(os.path.join(_HERE, f'chain6_{arm}_{"b" if bounded else "u"}'
                                                f'{os.environ.get("CHAINTAG", "")}.npz'),
                            samples=S)
    old = json.load(open(OUT)) if os.path.exists(OUT) else {}
    old.update(all_res)
    old['published'] = dict(limit_mev=PUBLISHED_LIMIT_MEV, effective_ev=PUBLISHED_EFFECTIVE_EV,
                            source='arXiv:2503.14744')
    json.dump(old, open(OUT, 'w'), indent=1)
    print('\n  wrote %s' % os.path.basename(OUT), flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main())
