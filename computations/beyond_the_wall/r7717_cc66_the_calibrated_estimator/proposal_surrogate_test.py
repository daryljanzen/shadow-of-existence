#!/usr/bin/env python3
"""`r7717+cc66` THE PROPOSAL, MADE CONCRETE — and ⛔ NOT A VERDICT AND NOT AN INSTALLED ESTIMATOR.

`r7717` asks, if the question is not resolved, for a proposal: what construction WOULD separate
"creates" from "fails to cancel". The calibration says why neither denominator can do it, so the
proposal is not a third denominator. It is to stop summarising the null with an `sd` at all.

⛭ THE ARGUMENT, which the calibration measured rather than assumed:
   · the OLD denominator counts the within-group gradient as uncertainty, so it is too LARGE;
   · the RULED denominator removes a line inside each group, which removes the gradient -- 69's reason
     is right -- but it ALSO removes the long-wavelength fluctuation, and THAT fluctuation IS the
     uncertainty of a group's LEVEL.  So it is too SMALL, and the surrogates show it: up to 349 of 2000
     step-free trials cross 5 sd at the widest window.
   ⇒ Both failures have the same cause: the step is a LOW-FREQUENCY feature of a correlated curve, and
     no within-group summary of that curve can estimate the uncertainty of a low-frequency feature.

⇒ THE PROPOSAL: compare the step against the DISTRIBUTION of steps from phase-randomised surrogates of
  the detrended curve, and report its percentile. No `sd`, no normality, no within-group summary. The
  machinery already exists -- it is the licence test, read the other way round.

⚠ WHAT IT COSTS TO EXPRESS A `5` SD BAR THIS WAY, stated because it is the proposal's real constraint:
  a bar of `5.7e-07` needs of order `10^7` surrogates to be expressible at all. ⌗ *Measured below: a
  surrogate trial is microseconds, so `10^7` is of order `10` minutes of one core -- affordable, and
  that is the point. The `2000` here can only express `p < 5e-4`, about `3.5` sd equivalent.*

⛔ WHAT THIS FILE IS NOT: it is not a reading of the four spectra under a licensed estimator, it takes
   no row of any decision table, and nothing here is a result. It exists so that 69 can see whether the
   proposal is worth ordering, with its own numbers rather than my description of them.
"""
import json
import os
import sys
import time

import numpy as np
from scipy.stats import norm

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import calibrate_and_read as C                                               # noqa: E402

N = 20000          # ⌗ ten times the licence run, to show the cost scaling honestly; NOT 10^7


def surrogate_steps(cs, R, n, rng):
    """the step distribution of step-free surrogates -- the licence test read the other way round"""
    resid = R - np.polyval(np.polyfit(cs, R, 1), cs)
    amp = np.abs(np.fft.rfft(resid))
    lo, hi = cs < 1.4, cs > 2.2
    out = np.empty(n)
    for t in range(n):
        ph = rng.uniform(0, 2 * np.pi, len(amp))
        ph[0] = 0.0
        if len(resid) % 2 == 0:
            ph[-1] = 0.0
        s = np.fft.irfft(amp * np.exp(1j * ph), n=len(resid))
        out[t] = s[hi].mean() - s[lo].mean()
    return out


def main():
    rng = np.random.default_rng(71717)
    real = C.load_real()
    print("\n" + "=" * 100)
    print("  ⛭ `r7717+cc66` THE PROPOSAL, MADE CONCRETE -- ⛔ NOT A VERDICT, NOT AN INSTALLED ESTIMATOR")
    print("=" * 100)
    print(f"\n  the step against {N} step-free surrogates of the detrended curve, per ratio per width:")
    print("       ratio            half     step       surrogate sd   |step| rank      p (two-sided)")
    rep = {}
    t0 = time.time()
    for nm, a, c in C.RATIOS:
        rep[nm.strip()] = []
        for h in C.HALVES:
            cs, R = C.curve(*real[a], *real[c], h)
            step = float(R[cs > 2.2].mean() - R[cs < 1.4].mean())
            ss = surrogate_steps(cs, R, N, rng)
            ge = int((np.abs(ss) >= abs(step)).sum())
            p = (ge + 1) / (N + 1)
            rep[nm.strip()].append(dict(half=h, step=step, surr_sd=float(ss.std(ddof=1)),
                                        n_ge=ge, p=p))
            print(f"       {nm}  {h:.3f}  {step:+.5f}   {ss.std(ddof=1):.6f}     "
                  f"{ge:5d}/{N}     {p:.5f}")
    el = time.time() - t0
    per = el / (N * len(C.RATIOS) * len(C.HALVES))
    print(f"\n  ⌗ cost: {el:.1f} s for {N * len(C.RATIOS) * len(C.HALVES)} surrogates "
          f"= {1e6 * per:.1f} us each")
    print(f"    ⇒ expressing a 5.7e-07 bar needs ~1e7 surrogates per curve: "
          f"about {1e7 * per / 60:.0f} min of one core per curve. AFFORDABLE, which is the point.")
    # ⛔ the first form of this line printed a sd-equivalent computed from nothing -- a garbage
    #    expression that produced "1.0 sd" for p = 5e-05, whose real equivalent is 4.06.  A wrong
    #    number in printed output is the one thing this revision cannot ship, so it is computed.
    pmin = 1.0 / (N + 1)
    sd_eq = float(norm.isf(pmin / 2.0))
    print(f"    ⚠ with {N} the smallest expressible p is {pmin:.2e} = {sd_eq:.2f} sd equivalent, so "
          f"any p at that floor is a FLOOR and not a value.")
    print("\n  ⛔ NOTHING HERE IS A VERDICT. The ruled denominator is not licensed, this one is not")
    print("    registered, and installing it is 69's call and not mine.")
    print("=" * 100)
    json.dump(dict(n_surrogates=N, per_surrogate_us=1e6 * per, rows=rep),
              open(os.path.join(HERE, 'proposal_surrogate_test.json'), 'w'), indent=1)
    return 0


if __name__ == '__main__':
    sys.exit(main())
