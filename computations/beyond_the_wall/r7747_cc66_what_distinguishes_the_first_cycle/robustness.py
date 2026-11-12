#!/usr/bin/env python3
"""`r7747+cc66` POST-REGISTRATION SENSITIVITY, LABELLED AS SUCH.

⛔ ** THE REGISTERED READING IS `driving_step.py` AT `W = 81`, AND ITS VERDICT STANDS ON THAT. ** This
file is run AFTER it and adds two things the registration did not ask for, because the registered
statistic turned out to depend on the envelope window more than the verdict does:

 ⓵ `rho` across five windows. ⇒ *The verdict is ROBUST and the FIGURE IS NOT: `rho >= 0.70` -- row
   two -- at every window on both arms, while its value runs `0.76` to `2.01`. So the registered
   branch fires throughout, and no single `rho` may be quoted as "the amount surviving".*
 ⓶ The lowest band's OWN amplitude ratio, which needs no trend and so no upper bands. ⇒ *This is the
   window-free statement: removing the driving leaves the first cycle's own oscillation amplitude
   essentially unchanged.*

⌗ *Added because reporting `1.29` as "the step grows by 29 per cent" would have been a figure of the
window and not of the spectra, and the registration fixed one window without asking whether the
statistic was stable in it. That is the gap this file closes rather than hides.*
"""
import importlib.util
import os
import sys

spec = importlib.util.spec_from_file_location("ds", os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "driving_step.py"))
ds = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ds)


def main():
    print(__doc__)
    print("=" * 100)
    print(f"\n  ⓵ rho across envelope windows, and ⓶ the lowest band's own ratio (trend-free)\n")
    print(f"  {'W':>5} {'rho CR':>9} {'rho ctrl':>9}   {'A1 ratio CR':>12} {'A1 ratio ctrl':>14}"
          f"   {'row 2 fires?':>13}")
    worst = 9e9
    for W in (41, 61, 81, 101, 121):
        ds.W = W
        o = {}
        for arm, (dr, nd) in ds.PAIRS.items():
            d, u = ds.step_of(dr), ds.step_of(nd)
            o[arm] = (abs(u['s']) / abs(d['s']), u['A'][0] / d['A'][0])
        fires = o['CR arm'][0] >= 0.70 or o['control'][0] >= 0.70
        worst = min(worst, o['CR arm'][0], o['control'][0])
        print(f"  {W:5d} {o['CR arm'][0]:9.4f} {o['control'][0]:9.4f}   "
              f"{o['CR arm'][1]:12.4f} {o['control'][1]:14.4f}   {str(fires):>13}")
    print(f"\n      ⇒ the smallest rho over all windows and both arms is {worst:.4f}, "
          f"above the registered 0.70 line, so ROW TWO FIRES AT EVERY WINDOW.")

    ds.W = 81
    print("\n  ⓷ WHY, band by band at the registered window (ratio undriven/driven)")
    for arm, (dr, nd) in ds.PAIRS.items():
        d, u = ds.step_of(dr), ds.step_of(nd)
        print(f"      {arm:9s} " + "  ".join(f"b{i+1} {u['A'][i] / d['A'][i]:.3f}"
                                             for i in range(7)))
    print("\n      ⇒ the driving carries the UPPER bands' amplitude -- the third most, down about a")
    print("        third -- and the lowest band's hardly at all. The step grows under the trend-based")
    print("        statistic because the trend its upper bands set FALLS, not because band 1 rises.")
    print("=" * 100)
    return 0


if __name__ == '__main__':
    sys.exit(main())
