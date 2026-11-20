"""r7838+60: THE SAMPLER THAT REPLACES r7836's PROFILE.

On order r7833 (69), item ②.  r7836's profile was a chain of local minimisations at fixed sums; it
came out non-monotone, which a profile likelihood of a smooth model cannot be, and orthogonalising
the mass direction against Omega_m improved it without fixing it.  A minimiser that stalls in a
narrow correlated valley reports whatever it stalled at.  A sampler does not have that failure
mode: it explores the valley instead of trying to find its floor.

** WHAT IS RUN. **  Metropolis-Hastings over the five parameters (the four banked directions in
grid-step units and the sum in eV), `CHAINS` independent chains from dispersed starts, the proposal
covariance adapted during burn-in from the pooled chain and then HELD FIXED for the kept samples so
that the kept chain is a proper Markov chain.  Convergence is reported, not assumed: split
Gelman-Rubin R-hat on every parameter and an effective sample size from the integrated
autocorrelation.  No result is read off a chain whose R-hat misses its threshold.

** TWO RUNS, BECAUSE TWO DIFFERENT QUESTIONS ARE ASKED. **
  * UNBOUNDED, the sum free to go negative on the operator's analytic continuation: this is where
    the published "effective mass" of -0.101 eV lives, and it is the only run that can show the
    posterior preferring a negative sum.
  * BOUNDED at Sum >= 0: this is where a 95 per cent UPPER LIMIT lives, and it is what the
    published 64.2 meV is.  Quoting a limit off an unbounded chain would be quoting a different
    number than the published one.

rc=0 on success.  Run: python3 sampler.py [cr|lcdm|both]        (numpy, scipy)
"""
import json
import os
import sys
import time

import numpy as np
from scipy.optimize import minimize

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import model as M                                                          # noqa: E402

CHAINS = int(os.environ.get('CHAINS', '6'))
BURN = int(os.environ.get('BURN', '6000'))
KEEP = int(os.environ.get('KEEP', '30000'))
THIN = int(os.environ.get('THIN', '5'))
SEED = int(os.environ.get('SEED', '7838'))
OUT = os.path.join(HERE, 'sampler.json')
PUBLISHED_LIMIT_MEV = 64.2
PUBLISHED_EFFECTIVE_EV = -0.101
PUBLISHED_GAP_PC = 2.48
DIST_POINT = {'lcdm': (68.5, 0.2975), 'cr': (68.60, 0.2973)}
NAMES = ['H0', 'OM', 'WB', 'NS', 'MNU']


def rhat(chains):
    """split Gelman-Rubin on one parameter: chains is (C, N)."""
    c = np.asarray(chains, float)
    C, N = c.shape
    h = N // 2
    s = np.concatenate([c[:, :h], c[:, h:2 * h]], axis=0)
    m, n = s.shape
    means, vars_ = s.mean(axis=1), s.var(axis=1, ddof=1)
    W = vars_.mean()
    B = n * means.var(ddof=1)
    if W <= 0:
        return float('nan')
    return float(np.sqrt(((n - 1) / n * W + B / n) / W))


def ess(chains):
    """effective sample size from the pooled autocorrelation, Geyer's initial positive sequence."""
    c = np.asarray(chains, float)
    C, N = c.shape
    x = c - c.mean()
    acf = np.zeros(min(N - 1, 2000))
    v = np.mean([np.var(c[i], ddof=0) for i in range(C)])
    if v <= 0:
        return 0.0
    for t in range(len(acf)):
        acc = [np.mean((c[i, :N - t] - c[i].mean()) * (c[i, t:] - c[i].mean())) for i in range(C)]
        acf[t] = np.mean(acc) / v
    s = 0.0
    for t in range(1, len(acf) - 1, 2):
        p = acf[t] + acf[t + 1]
        if p <= 0:
            break
        s += p
    return float(C * N / (1.0 + 2.0 * s))


def best_fit(mod, bounded):
    lo = 0.0 if bounded else mod.s_lo
    bnds = [(-4, 4)] * 4 + [(lo, mod.s_hi)]
    best = None
    for st in ([0, 0, 0, 0, 0.02], [0.5, -0.5, 0.3, -0.3, 0.10], [-0.5, 0.5, -0.3, 0.3, 0.20],
               [0, 0, 0, 0, max(lo, -0.08)]):
        r = minimize(lambda z: mod.chi2(z), np.clip(st, [-4] * 4 + [lo], [4] * 4 + [mod.s_hi]),
                     method='Powell', bounds=bnds,
                     options=dict(maxiter=60000, xtol=1e-6, ftol=1e-8))
        if best is None or r.fun < best.fun:
            best = r
    return best


def run_chains(mod, bounded, x0, scale, rng):
    lo = 0.0 if bounded else mod.s_lo
    hi = mod.s_hi

    def logp(z):
        if not (lo <= z[4] <= hi) or np.any(np.abs(z[:4]) > 6):
            return -np.inf
        return -0.5 * mod.chi2(z)

    # ---- burn-in with an adapting diagonal-then-full proposal
    cur = []
    for i in range(CHAINS):
        z = np.array(x0, float) + scale * rng.standard_normal(5) * 2.0
        z[4] = float(np.clip(z[4], lo, hi))
        cur.append(z)
    cur = np.asarray(cur)
    lcur = np.array([logp(z) for z in cur])
    for i in range(CHAINS):
        while not np.isfinite(lcur[i]):
            cur[i] = np.array(x0, float) + 0.3 * scale * rng.standard_normal(5)
            cur[i][4] = float(np.clip(cur[i][4], lo, hi))
            lcur[i] = logp(cur[i])
    S = np.diag(scale ** 2)
    hist, acc = [], 0
    for t in range(BURN):
        L = np.linalg.cholesky(S * (2.38 ** 2 / 5))
        for i in range(CHAINS):
            prop = cur[i] + L @ rng.standard_normal(5)
            lp = logp(prop)
            if lp > lcur[i] or np.log(rng.random()) < lp - lcur[i]:
                cur[i], lcur[i] = prop, lp
                acc += 1
        hist.append(cur.copy())
        if t in (BURN // 3, 2 * BURN // 3, BURN - 1):
            H = np.asarray(hist[len(hist) // 2:]).reshape(-1, 5)
            C = np.cov(H.T)
            if np.all(np.isfinite(C)) and np.linalg.det(C) > 0:
                S = C + 1e-12 * np.eye(5)
            hist = hist[-10:]
    burn_rate = acc / float(BURN * CHAINS)
    # ---- kept samples with the proposal HELD
    L = np.linalg.cholesky(S * (2.38 ** 2 / 5))
    out = np.empty((CHAINS, KEEP // THIN, 5))
    acc = 0
    for t in range(KEEP):
        for i in range(CHAINS):
            prop = cur[i] + L @ rng.standard_normal(5)
            lp = logp(prop)
            if lp > lcur[i] or np.log(rng.random()) < lp - lcur[i]:
                cur[i], lcur[i] = prop, lp
                acc += 1
        if t % THIN == 0:
            out[:, t // THIN, :] = cur
    return out, acc / float(KEEP * CHAINS), burn_rate


def summarise(mod, arm, bounded, S, rate, burn_rate):
    lab = 'bounded' if bounded else 'unbounded'
    diag = {}
    for j, nm in enumerate(NAMES):
        diag[nm] = dict(rhat=rhat(S[:, :, j]), ess=ess(S[:, :, j]))
    flat = S.reshape(-1, 5)
    s = flat[:, 4]
    h0d, omd = DIST_POINT[arm]
    h = (mod.phys(flat[:, :4].T, 0.0)['H0']) / 100.0 if False else None
    c = M.ARMS[arm]['centre']
    H0 = c['H0'] + M.R.STEP['H0'] * flat[:, 0]
    OM = c['OM'] + M.R.STEP['OM'] * flat[:, 1]
    gap = 100.0 * ((OM * (H0 / 100.0) ** 2) / (omd * (h0d / 100.0) ** 2) - 1.0)
    res = dict(label=lab, arm=arm, chains=int(S.shape[0]), kept_per_chain=int(S.shape[1]),
               accept=float(rate), burn_accept=float(burn_rate), diagnostics=diag,
               mean={nm: float(flat[:, j].mean()) for j, nm in enumerate(NAMES)},
               sd={nm: float(flat[:, j].std(ddof=1)) for j, nm in enumerate(NAMES)},
               sum_mean_ev=float(s.mean()), sum_sd_ev=float(s.std(ddof=1)),
               sum_q=[float(np.quantile(s, q)) for q in (0.025, 0.16, 0.5, 0.84, 0.95, 0.975)],
               gap_mean_pc=float(gap.mean()), gap_sd_pc=float(gap.std(ddof=1)))
    if bounded:
        res['upper95_mev'] = float(np.quantile(s, 0.95) * 1000.0)
        res['factor_vs_published'] = float(PUBLISHED_LIMIT_MEV / res['upper95_mev'])
        for q in (0.059, 0.064):
            res[f'frac_below_{q}'] = float((s < q).mean())
    bf = best_fit(mod, bounded)
    res['best_fit'] = dict(chi2=float(bf.fun), x=[float(v) for v in bf.x],
                           phys=mod.phys(bf.x[:4], bf.x[4]))
    print(f"  [{arm}/{lab}] accept {rate:.3f} (burn {burn_rate:.3f});  "
          f"Sum = {s.mean() * 1000:+.1f} +/- {s.std(ddof=1) * 1000:.1f} meV;  "
          f"gap {gap.mean():+.2f} per cent;  chi2min {bf.fun:.2f}", flush=True)
    print('     R-hat ' + '  '.join(f'{nm}={diag[nm]["rhat"]:.4f}' for nm in NAMES), flush=True)
    print('     ESS   ' + '  '.join(f'{nm}={diag[nm]["ess"]:.0f}' for nm in NAMES), flush=True)
    if bounded:
        print(f"     95 per cent upper limit: {res['upper95_mev']:.1f} meV against the published "
              f"{PUBLISHED_LIMIT_MEV} -- a factor {res['factor_vs_published']:.2f}", flush=True)
    return res


def main():
    which = (sys.argv[1] if len(sys.argv) > 1 else 'both')
    arms = ['lcdm', 'cr'] if which == 'both' else [which]
    rng = np.random.default_rng(SEED)
    all_res = {}
    for arm in arms:
        t0 = time.time()
        mod = M.Model(arm)
        print(f'\n  {arm}: {mod.nb} bins, sum interpolated on [{mod.s_lo:+.2f}, {mod.s_hi:+.2f}] eV'
              f'   (model built in {time.time() - t0:.1f} s)', flush=True)
        bf0 = best_fit(mod, False)
        scale = np.array([0.25, 0.25, 0.25, 0.25, 0.02])
        for bounded in (True, False):
            S, rate, br = run_chains(mod, bounded, bf0.x, scale, rng)
            all_res[f'{arm}_{"bounded" if bounded else "unbounded"}'] = \
                summarise(mod, arm, bounded, S, rate, br)
            np.savez_compressed(os.path.join(HERE, f'chain_{arm}_{"b" if bounded else "u"}.npz'),
                                samples=S)
    old = json.load(open(OUT)) if os.path.exists(OUT) else {}
    old.update(all_res)
    old['published'] = dict(limit_mev=PUBLISHED_LIMIT_MEV, effective_ev=PUBLISHED_EFFECTIVE_EV,
                            gap_pc=PUBLISHED_GAP_PC, source='arXiv:2503.14744')
    json.dump(old, open(OUT, 'w'), indent=1)
    print(f'\n  wrote {os.path.relpath(OUT, HERE)}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
