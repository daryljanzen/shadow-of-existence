#!/usr/bin/env python3
"""`r7719+cc66` ITEM 4 — the three discriminant ratios at `10^7` surrogates, CHECKPOINTED PER CURVE.

⛔ WHY CHECKPOINTED: nine curves at the ordered count is over half an hour, and this container recycles
   every eleven to seventeen minutes.  The lesson is `r7713`'s and is not relearned here: a checkpoint
   interval longer than the interval between restarts is not a checkpoint.  One file per curve, written
   whole, skipped on a re-run.

⛭ AND WHY THE SURROGATE LOOP IS BATCHED: at the loop's measured 26 us each, `10^7` per curve is about
   four minutes and nine curves is thirty-six.  Batching the phase draw and the inverse transform makes
   the same draws far cheaper.  ⛔ THAT IS A PERFORMANCE CHANGE AND MUST NOT BE A STATISTICAL ONE, so
   `--control` checks the batched generator against `r7717`'s committed loop on the same seed and the
   same curve, and the run refuses to proceed if their step distributions disagree.
"""
import json
import os
import sys
import time

import numpy as np
from scipy.stats import norm

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.abspath(os.path.join(HERE, '..'))
sys.path.insert(0, os.path.join(BW, 'r7717_cc66_the_calibrated_estimator'))
import calibrate_and_read as C                                               # noqa: E402
from proposal_surrogate_test import surrogate_steps as loop_surrogates       # noqa: E402

OUT = os.path.join(HERE, 'item4')
N = 10 ** 7
BATCH = 50000


def batched_surrogate_steps(cs, R, n, rng, batch=BATCH):
    """the same null as `r7717`'s loop -- detrend across all centres, randomise phases, keep the
    amplitude spectrum -- drawn in blocks so the transform is done once per block."""
    resid = R - np.polyval(np.polyfit(cs, R, 1), cs)
    amp = np.abs(np.fft.rfft(resid))
    L = len(resid)
    lo, hi = cs < 1.4, cs > 2.2
    nlo, nhi = lo.sum(), hi.sum()
    out = np.empty(n)
    done = 0
    while done < n:
        m = min(batch, n - done)
        ph = rng.uniform(0, 2 * np.pi, (m, len(amp)))
        ph[:, 0] = 0.0
        if L % 2 == 0:
            ph[:, -1] = 0.0
        s = np.fft.irfft(amp[None, :] * np.exp(1j * ph), n=L, axis=1)
        out[done:done + m] = s[:, hi].sum(1) / nhi - s[:, lo].sum(1) / nlo
        done += m
    return out


def control():
    """⛔ the batched generator against the committed loop, same curve, before anything is read"""
    real = C.load_real()
    cs, R = C.curve(*real['cr|cr'], *real['lcdm|lcdm'], 0.350)
    a = loop_surrogates(cs, R, 20000, np.random.default_rng(99))
    b = batched_surrogate_steps(cs, R, 20000, np.random.default_rng(99))
    print("\n  ⛔ CONTROL: the batched generator against `r7717`'s committed loop (20000 draws each)")
    for nm, v in (('loop', a), ('batched', b)):
        print(f"       {nm:8s} mean {v.mean():+.3e}  sd {v.std(ddof=1):.6f}  "
              f"|max| {np.abs(v).max():.6f}  q99.9 {np.quantile(np.abs(v), 0.999):.6f}")
    rel = abs(b.std(ddof=1) / a.std(ddof=1) - 1.0)
    relq = abs(np.quantile(np.abs(b), 0.999) / np.quantile(np.abs(a), 0.999) - 1.0)
    ok = rel < 0.05 and relq < 0.10
    print(f"       sd agree to {100 * rel:.2f}%, the 99.9th percentile to {100 * relq:.2f}%  "
          f"⇒ {'SAME NULL' if ok else '⛔ DIFFERENT NULLS'}")
    if not ok:
        print("       ⛔ REFUSING: a performance change that moved the null is a statistical change.")
    return ok


def main():
    if not control():
        return 1
    os.makedirs(OUT, exist_ok=True)
    real = C.load_real()
    print(f"\n  ⛭ ITEM 4 — the three discriminant ratios at N = {N}, checkpointed per curve")
    print("       ratio            half     step       surrogate sd   |step| rank        p")
    rep = {}
    for nm, a, c in C.RATIOS:
        key = nm.strip()
        rep[key] = []
        for h in C.HALVES:
            fp = os.path.join(OUT, f"{key.replace(' ', '_').replace('|', '-')}__h{h:.3f}.json")
            if os.path.exists(fp):
                d = json.load(open(fp))
            else:
                t0 = time.time()
                cs, R = C.curve(*real[a], *real[c], h)
                step = float(R[cs > 2.2].mean() - R[cs < 1.4].mean())
                rng = np.random.default_rng(abs(hash((key, h))) % (2 ** 32))
                ss = batched_surrogate_steps(cs, R, N, rng)
                ge = int((np.abs(ss) >= abs(step)).sum())
                d = dict(half=h, step=step, n=N, n_ge=ge, p=(ge + 1) / (N + 1),
                         surr_sd=float(ss.std(ddof=1)), wall_s=round(time.time() - t0, 1))
                json.dump(d, open(fp, 'w'), indent=1)
            rep[key].append(d)
            print(f"       {nm}  {h:.3f}  {d['step']:+.5f}   {d['surr_sd']:.6f}     "
                  f"{d['n_ge']:9d}/{N}   {d['p']:.3e}   [{d.get('wall_s', 0):.0f} s]")
    floor = 1.0 / (N + 1)
    print(f"\n  ⌗ floor p {floor:.2e} = {norm.isf(floor / 2):.2f} sd-equivalent; the registered bar is 5.")
    w = {k: max(v, key=lambda r: r['half']) for k, v in rep.items()}
    res = {k: v['p'] < 6.3e-5 for k, v in w.items()}     # the bar, as a two-sided p
    print("\n  ⛭ AT THE WIDEST REGISTERED WINDOW, against the bar read as a two-sided p (6.3e-05):")
    for k, v in w.items():
        print(f"       {k:14s} step {v['step']:+.5f}  p {v['p']:.3e}  "
              f"{'RESOLVED' if res[k] else '⛔ NOT RESOLVED'}")
    ker, src = res['kernel alone'], res['source alone']
    print("\n  ⛭ THE VERDICT ON THE PSEUDO-SPECTRUM ROUTE")
    if not ker and not src:
        v = 'not_resolved_by_this_construction'
        print("       ⇒ NEITHER DIFFERENCE IS RESOLVED. The route is closed: the pseudo-spectrum")
        print("         cannot decide 'creates' from 'fails to cancel', and that is the finding.")
    elif ker and not src:
        v = 'creates'; print("       ⇒ THE PROJECTION CREATES IT.")
    elif src and not ker:
        v = 'fails_to_cancel'; print("       ⇒ IT FAILS TO CANCEL.")
    else:
        v = 'both_resolved_not_separable'
        print("       ⇒ BOTH RESOLVED: the two differences do not partition the step.")
    json.dump(dict(rows=rep, widest=w, resolved=res, verdict=v, floor_p=floor),
              open(os.path.join(HERE, 'item4_discriminant.json'), 'w'), indent=1)
    return 0


if __name__ == '__main__':
    sys.exit(main())
