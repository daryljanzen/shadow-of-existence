#!/usr/bin/env python3
"""`r7719+cc66` P15's three printed readings through the calibrated non-parametric test.

⛔ THE CURVES ARE NOT REBUILT HERE.  `r7707`'s module is imported and its own six curve functions are
   reconstructed through the same `own_comb_kinds` calls, so this tests the SAME objects the printed
   sentences rest on rather than lookalikes of them.  The surrogate machinery is imported from
   `r7717+cc66.1`.  Neither is redefined in this file, and the imports are what enforce that.

⛔ ⓷ IS A POWER CLAIM, NOT A DETECTION CLAIM, and is tested as one -- registered in `PREDICTION.md`
   before any run.  The printed sentence says a transition of the measured size WOULD HAVE STOOD at
   four to eleven times the source ratio's own scatter: a counterfactual about that ratio's power.
   Reading it as a detection claim would be the recurring fault one more time.

⚠ AND THE CEILING IS ARITHMETIC: at N surrogates no percentile below 1/N is expressible, so a printed
  multiple above the floor's sd-equivalent cannot be certified at any affordable N.  Registered, with
  the table, before the run.
"""
import json
import os
import sys
import time

import numpy as np
from scipy.stats import norm

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.abspath(os.path.join(HERE, '..'))
sys.path.insert(0, os.path.join(BW, 'r7707_cc66_where_the_steps_sharpness_is_made'))
sys.path.insert(0, os.path.join(BW, 'r7717_cc66_the_calibrated_estimator'))
sys.path.insert(0, os.path.join(BW, 'r7639_cc66_P15_repoint_paper'))
import where_the_sharpness_is as W7707                                       # noqa: E402
import own_comb_kinds as OCK                                                 # noqa: E402
from proposal_surrogate_test import surrogate_steps                          # noqa: E402

HALVES = W7707.HALVES
GRID = (0.85, 3.0, 0.05)
LO_HI = (1.4, 2.2)
N_DET = 10 ** 6            # registered
N_POW = 2000               # registered
ALPHA = 1e-3               # registered
POWER_REQ = 0.95           # registered


def curves():
    """`r7707`'s own six readings, through its own module"""
    FB = W7707.fine_banks()
    SB, _ = W7707.source_banks(True)
    STS, STK = OCK.own_state(FB, 'mean', 1.0), OCK.own_state(SB, 'mean', 1.0)
    r = lambda st, a, b: float(OCK._rms(st['ua'], st['oa'], a, b)
                               / OCK._rms(st['xc'], st['oc'], a, b) - 1.0)
    return {
        'spectra ratio (the contrast)': lambda a, b: r(STS, a, b),
        "the ARM's own spectrum": lambda a, b: OCK._rms(STS['ua'], STS['oa'], a, b),
        "the CONTROL's own spectrum": lambda a, b: OCK._rms(STS['xc'], STS['oc'], a, b),
        'source ratio': lambda a, b: r(STK, a, b),
    }


def row(fn, half):
    cs = np.arange(GRID[0] + half, GRID[1], GRID[2])
    R = np.array([fn(c - half, c + half) for c in cs])
    return cs, R


def read(cs, R):
    lo, hi = cs < LO_HI[0], cs > LO_HI[1]
    step = float(R[hi].mean() - R[lo].mean())
    return step, float(R[hi].std(ddof=1)), float(R[lo].std(ddof=1))


def detect(cs, R, n, rng):
    """the two-sided percentile of the step against step-free surrogates -- `r7717`'s machinery"""
    step, _, _ = read(cs, R)
    ss = surrogate_steps(cs, R, n, rng)
    ge = int((np.abs(ss) >= abs(step)).sum())
    p = (ge + 1) / (n + 1)
    return step, ge, p, float(ss.std(ddof=1))


def power(cs, R, planted, n, rng, alpha):
    """⛔ ⓷'s OWN TEST: plant a step of the printed size in a step-free surrogate and see it or not.
    The inner reference distribution is itself surrogate-built, so this measures the TEST's power on
    this curve and not a Gaussian's."""
    base = surrogate_steps(cs, R, n, rng)                    # step-free draws of the curve
    ref = surrogate_steps(cs, R, min(n * 5, 20000), rng)     # the reference the test compares against
    thresh = float(np.quantile(np.abs(ref), 1.0 - alpha))
    hit = int((np.abs(base + planted) >= thresh).sum())
    return hit / n, thresh


def main():
    rng = np.random.default_rng(7719)
    C = curves()
    rep, t0 = {}, time.time()
    print("\n" + "=" * 100)
    print("  ⛭ `r7719+cc66` P15's PRINTED READINGS THROUGH THE CALIBRATED TEST")
    print(f"     ceiling: {N_DET} surrogates ⇒ floor p {1/(N_DET+1):.2e} "
          f"= {norm.isf(1/(N_DET+1)/2):.2f} sd-equivalent. A printed multiple above that is NOT")
    print("     certifiable at this N, by arithmetic registered before the run.")
    print("=" * 100)

    print("\n  ⛔ ⓵ AND ⓶ — THE DETECTION CLAIMS")
    print("       object                        half    step      hi-spread  printed ratio   p          beyond")
    det = {}
    for nm in ('spectra ratio (the contrast)', "the ARM's own spectrum", "the CONTROL's own spectrum"):
        det[nm] = []
        for h in HALVES:
            cs, R = row(C[nm], h)
            step, shi, slo = read(cs, R)
            st, ge, p, ssd = detect(cs, R, N_DET, rng)
            det[nm].append(dict(half=h, step=st, hi_spread=shi, lo_spread=slo,
                                printed_ratio=abs(st) / shi if shi else float('nan'),
                                n_ge=ge, p=p, surr_sd=ssd))
            print(f"       {nm:28s}  {h:.3f}  {st:+.5f}  {shi:.6f}   "
                  f"{abs(st)/shi if shi else float('nan'):7.2f}x   {p:.2e}   "
                  f"{'ALL' if ge == 0 else f'{ge} of {N_DET}'}")
    rep['detection'] = det

    print("\n  ⛔⛔ ⓷ — THE POWER CLAIM, TESTED AS A POWER CLAIM")
    print("       the printed sentence: a transition of the measured size WOULD HAVE STOOD at four to")
    print("       eleven times the source ratio's own scatter. That is a counterfactual about POWER.")
    pw = []
    for h in HALVES:
        cs_s, R_s = row(C['spectra ratio (the contrast)'], h)
        planted = read(cs_s, R_s)[0]                    # the measured size, from the contrast
        cs, R = row(C['source ratio'], h)
        step, shi, slo = read(cs, R)
        pwr, thr = power(cs, R, planted, N_POW, rng, ALPHA)
        st, ge, p, ssd = detect(cs, R, min(N_DET, 200000), rng)
        pw.append(dict(half=h, planted=planted, source_step=st, source_hi_spread=shi,
                       printed_ratio=abs(planted) / shi if shi else float('nan'),
                       power=pwr, threshold=thr, source_p=p, surr_sd=ssd))
        print(f"       h={h:.3f}  planted {planted:+.5f}   the source ratio's own step {st:+.6f} "
              f"(p {p:.3f})")
        print(f"                 printed ratio {abs(planted)/shi if shi else float('nan'):6.2f}x   "
              f"POWER at alpha={ALPHA:g}: {pwr:.3f}  "
              f"{'✓ meets' if pwr >= POWER_REQ else '⛔ BELOW'} the registered {POWER_REQ}")
    rep['power'] = pw
    ok = all(r['power'] >= POWER_REQ for r in pw)
    print(f"\n       ⇒ the source exclusion's power is {'LICENSED' if ok else '⛔ NOT LICENSED'} "
          f"at the registered threshold")
    rep['power_licensed'] = bool(ok)
    rep['wall_s'] = round(time.time() - t0, 1)
    json.dump(rep, open(os.path.join(HERE, 'printed_through_the_test.json'), 'w'), indent=1)
    print(f"\n  wall {time.time() - t0:.1f} s")
    print("=" * 100)
    return 0


if __name__ == '__main__':
    sys.exit(main())
