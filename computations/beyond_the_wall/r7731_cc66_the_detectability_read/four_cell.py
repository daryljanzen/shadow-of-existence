#!/usr/bin/env python3
"""`r7731+cc66.4` THE FOUR-CELL DETECTABILITY VERDICT, as registered.

⛭ `PREDICTION_detectability.md` §1 (the 2x2 and the fourth cell), §2 (the power requirement), §3 (the
null: PRIMARY row-and-column-normalised 2D phase randomisation, SECONDARY plain), amendments 5-6 (the
two binnings, dead bins masked at weight 0).  ⛔ Nothing is redesigned.
"""
import sys
import time

import numpy as np

BLOB = '/tmp/claude-0/-home-user-shadow-of-existence/26826c5d-5f18-5adf-9ba6-b04043e78f9b/scratchpad/dlk/r7729_dlk_four.npz'
N_NULL = 10000       # registered §4: 10^4 draws is enough for a 99% interval and a power curve
N_POW = 2000
ALPHA = 0.01         # registered §1: 99% intervals; §2: power at alpha = 0.01
POWER_REQ = 0.95     # registered §2
BINS = {'PRIMARY': 12, 'SECONDARY': 23}
SEED = 7731
FAILS = []


def gate(tag, ok, text, witness=''):
    print(f"    [{'PASS' if ok else 'FAIL'}] {tag}  {text}")
    if witness:
        print(f"             {witness}")
    if not ok:
        FAILS.append(tag)
    return ok


def binned(X, w):
    n = X.shape[1] // w
    return X[:, :n * w].reshape(X.shape[0], n, w).sum(axis=2)


def fit2(y, tk, ts, w):
    """the two-amplitude fit, contribution-weighted -- weighted least squares, no intercept"""
    sw = np.sqrt(w).ravel()
    A = np.column_stack([tk.ravel() * sw, ts.ravel() * sw])
    b = y.ravel() * sw
    return np.linalg.lstsq(A, b, rcond=None)[0]


def surrogate(field, rng, normalise):
    """registered §3.  PRIMARY normalises per-row and per-column sd before randomising and restores
    after, because the field is not stationary; SECONDARY is the plain form."""
    if normalise:
        rs = field.std(axis=1, keepdims=True)
        rs[rs == 0] = 1.0
        g = field / rs
        cs = g.std(axis=0, keepdims=True)
        cs[cs == 0] = 1.0
        g = g / cs
    else:
        g, rs, cs = field, 1.0, 1.0
    F = np.fft.rfft2(g)
    s = np.fft.irfft2(np.abs(F) * np.exp(1j * rng.uniform(0, 2 * np.pi, F.shape)), s=g.shape)
    return s * cs * rs if normalise else s


def main():
    z = np.load(BLOB, allow_pickle=True)
    C = ('S_lcdm__K_lcdm', 'S_lcdm__K_cr', 'S_cr__K_lcdm', 'S_cr__K_cr')
    M = {c: z[f'P__{c}'][None, :] * z[f'Dlk__{c}'] ** 2 for c in C}
    print(f"\n  ⛭ `r7731+cc66.4` THE FOUR-CELL VERDICT, {N_NULL} null draws per binning\n")
    rows = {}
    for name, w in BINS.items():
        B = {c: binned(M[c], w) for c in C}
        dead = np.zeros(B[C[0]].shape, bool)
        for c in C:
            dead |= B[c] <= 0
        with np.errstate(divide='ignore'):
            lb = {c: np.where(dead, 0.0, np.log(np.where(B[c] > 0, B[c], 1.0))) for c in C}
        tk = lb['S_lcdm__K_cr'] - lb['S_lcdm__K_lcdm']
        ts = lb['S_cr__K_lcdm'] - lb['S_lcdm__K_lcdm']
        obs = lb['S_cr__K_cr'] - lb['S_lcdm__K_lcdm']
        W = B['S_lcdm__K_lcdm'] / B['S_lcdm__K_lcdm'].sum(axis=1, keepdims=True)
        W = np.where(dead, 0.0, W)
        a_ker, a_src = fit2(obs, tk, ts, W)

        # ---- the null: amplitudes recovered from draws with NO genuine signal -----
        resid = obs - (a_ker * tk + a_src * ts)
        rng = np.random.default_rng(SEED)
        t0 = time.time()
        nk, ns_ = np.empty(N_NULL), np.empty(N_NULL)
        for i in range(N_NULL):
            d = fit2(surrogate(resid, rng, True), tk, ts, W)
            nk[i], ns_[i] = d
        dt = time.time() - t0
        lo_k, hi_k = np.quantile(nk, [ALPHA / 2, 1 - ALPHA / 2])
        lo_s, hi_s = np.quantile(ns_, [ALPHA / 2, 1 - ALPHA / 2])
        ker_sig = not (lo_k <= 0 <= hi_k)
        src_sig = not (lo_s <= 0 <= hi_s)
        # ⛭ the fitted amplitudes are compared against the null's own spread about ZERO
        ker_hit = abs(a_ker) > max(abs(lo_k), abs(hi_k))
        src_hit = abs(a_src) > max(abs(lo_s), abs(hi_s))

        # ---- the registered power requirement -------------------------------
        sk = np.std(nk, ddof=1)
        ss = np.std(ns_, ddof=1)
        rng2 = np.random.default_rng(SEED + 1)
        hit_k = hit_s = 0
        for _ in range(N_POW):
            n = surrogate(resid, rng2, True)
            dk_ = fit2(n + tk, tk, ts, W)            # a pure-kernel injection, a_ker = 1
            ds_ = fit2(n + ts, tk, ts, W)            # a pure-source injection, a_src = 1
            hit_k += abs(dk_[0]) > max(abs(lo_k), abs(hi_k))
            hit_s += abs(ds_[1]) > max(abs(lo_s), abs(hi_s))
        pk, ps = hit_k / N_POW, hit_s / N_POW

        print(f"    ⛭ {name} ({B[C[0]].shape[1]} bins)   [{dt:.0f} s for {N_NULL} draws]")
        print(f"         fitted   a_ker {a_ker:+.4f}   a_src {a_src:+.4f}")
        print(f"         null 99% a_ker [{lo_k:+.4f}, {hi_k:+.4f}] sd {sk:.4f}   "
              f"a_src [{lo_s:+.4f}, {hi_s:+.4f}] sd {ss:.4f}")
        print(f"         power at alpha={ALPHA}: pure-kernel {pk:.3f}, pure-source {ps:.3f} "
              f"(registered requirement {POWER_REQ})")
        rows[name] = dict(a=(a_ker, a_src), hit=(bool(ker_hit), bool(src_hit)), pow=(pk, ps))
        gate(f'power/{name}', pk >= POWER_REQ and ps >= POWER_REQ,
             f"the test can recover a planted pure-kernel AND pure-source signal [{name}]",
             f"{pk:.3f} / {ps:.3f} against {POWER_REQ}; BELOW it the verdict is "
             f"'neither, by the instrument'")

    print(f"\n  ⛭ THE REGISTERED 2x2:")
    verdicts = {}
    for name, r in rows.items():
        k_, s_ = r['hit']
        v = ('the projection CREATES it' if k_ and not s_ else
             'the projection FAILS TO CANCEL it' if s_ and not k_ else
             'BOTH CONTRIBUTE' if k_ and s_ else 'NEITHER -- the plane does not decide')
        verdicts[name] = v
        print(f"         {name:10s} a_ker {'excludes' if k_ else 'includes':8s} 0 | "
              f"a_src {'excludes' if s_ else 'includes':8s} 0   =>  {v}")
    gate('agree', len(set(verdicts.values())) == 1,
         "the two binnings agree on the cell (registered: a disagreement IS the verdict)",
         ' / '.join(f'{k}: {v}' for k, v in verdicts.items()))
    print(f"\n  {'OK' if not FAILS else '⛔'}  {len(rows) * 1 + 1 - len(FAILS)} of "
          f"{len(rows) + 1} gate(s) pass{'' if not FAILS else '; FAILED: ' + ', '.join(FAILS)}\n")
    return 1 if FAILS else 0


if __name__ == '__main__':
    sys.exit(main())
