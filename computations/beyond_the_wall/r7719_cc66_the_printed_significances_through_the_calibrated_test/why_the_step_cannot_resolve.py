#!/usr/bin/env python3
"""`r7719+cc66` WHY the step cannot resolve it — measured, so that the build named next rests on a
number and not on an intuition.

⛔ The order's last clause: "If it is unresolved, the finding is that the pseudo-spectrum cannot decide
   the question. Then name the build that could."  A build named from a hunch is worth nothing, so the
   limitation is measured first: how many INDEPENDENT windows does the step actually compare?
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', 'r7717_cc66_the_calibrated_estimator')))
import calibrate_and_read as C                                               # noqa: E402

real = C.load_real()
rep = {}
print("\n  ⛭ HOW MANY INDEPENDENT WINDOWS DOES THE STEP COMPARE?")
print("       half   centres  lo/hi used   range/2h   autocorr length   effective lo+hi")
for h in C.HALVES:
    cs, R = C.curve(*real['cr|cr'], *real['lcdm|lcdm'], h)
    lo, hi = cs < 1.4, cs > 2.2
    # ⒜ the geometric count: windows of width 2h tiling the band without overlap
    geo = (cs[-1] - cs[0]) / (2 * h)
    # ⒝ the measured count: the lag at which the curve's own autocorrelation first falls below 1/e
    r = R - R.mean()
    ac = np.correlate(r, r, 'full')[len(r) - 1:]
    ac /= ac[0]
    lag = int(np.argmax(ac < 1 / np.e)) if np.any(ac < 1 / np.e) else len(ac)
    acl = lag * (cs[1] - cs[0])
    eff_lo = (cs[lo][-1] - cs[lo][0]) / acl if acl else np.nan
    eff_hi = (cs[hi][-1] - cs[hi][0]) / acl if acl else np.nan
    rep[f'{h}'] = dict(centres=int(len(cs)), n_lo=int(lo.sum()), n_hi=int(hi.sum()),
                       geometric=float(geo), autocorr_length=float(acl),
                       eff_lo=float(eff_lo), eff_hi=float(eff_hi))
    print(f"       {h:.3f}  {len(cs):5d}    {lo.sum():2d}/{hi.sum():2d}      {geo:6.2f}     "
          f"{acl:.3f} in q        {eff_lo:.2f} + {eff_hi:.2f}")
print("\n  ⇒ the step compares two band MEANS, and each is an average over only a few INDEPENDENT")
print("    windows -- which is why no amount of l density helps: the l grid is already every integer,")
print("    and the limit is the number of independent WINDOWS, set by the band's width over 2h.")
print("\n  ⌗ the curve has ~40 centres but they overlap: at the widest half-width the whole band holds")
print("    about three non-overlapping windows, so the two group means rest on ~1.5 each.")
json.dump(rep, open(os.path.join(HERE, 'why_the_step_cannot_resolve.json'), 'w'), indent=1)
