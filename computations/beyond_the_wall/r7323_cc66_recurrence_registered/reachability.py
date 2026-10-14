#!/usr/bin/env python3
"""r7323+cc66 -- IS EVERY REGISTERED OUTCOME REACHABLE?  The check the withdrawn band never got.

`r7323` item ③ withdrew `r7321`'s band because a point of `16` sits inside its own `20.8`-point
half-width: no result could have refuted it.  This script is the general form of that objection, applied
to the registration that replaces it: enumerate EVERY integer split of the `40`/`38` frame, decide each
one under the registered rule, and count the outcomes.  An outcome with no splits is a row that cannot
happen, which is the same defect under another name.

It also reproduces the two numbers `r7323` and the re-registration rest on:
  * the half-width on the difference at each rate -- where `about 21` comes from;
  * how much of the withdrawn band `8`-`24` would have decided nothing.

  python3 reachability.py

Every figure printed here is computed; nothing is asserted.
"""
import math
from collections import Counter

Z = 1.959963985                 # 95 per cent, two-sided -- the same constant score.py uses
NA, NB = 40, 38                 # draw.py's hash split of the 78-key frame
SEVENTY = 30.0                  # 70's measured within-unit owedness spread
WINDOW = (0.40, 0.80)           # r7321 §3 condition 4: the frame is reproducing inside this


def wilson(k, n):
    p = k / n
    d = 1 + Z * Z / n
    c = (p + Z * Z / (2 * n)) / d
    h = Z * math.sqrt(p * (1 - p) / n + Z * Z / (4 * n * n)) / d
    return p, max(0.0, c - h), min(1.0, c + h)


def newcombe(k1, n1, k2, n2):
    p1, l1, u1 = wilson(k1, n1)
    p2, l2, u2 = wilson(k2, n2)
    d = p1 - p2
    return (d, d - math.sqrt((p1 - l1) ** 2 + (u2 - p2) ** 2),
            d + math.sqrt((u1 - p1) ** 2 + (p2 - l2) ** 2))


def verdict(k, j):
    """The registered rule of PREREGISTRATION.md R1, on the MAGNITUDE and not on a signed bound."""
    d, lo, hi = newcombe(k, NA, j, NB)
    clears = lo > 0 or hi < 0
    below = max(abs(lo), abs(hi)) * 100 < SEVENTY
    v = ('RECURS BUT SMALLER' if clears and below else 'RECURS' if clears
         else "70's FIGURE REFUTED" if below else 'INCONCLUSIVE')
    return v, abs(d) * 100


def main():
    print()
    print(f'  REACHABILITY OF THE REGISTERED OUTCOMES -- {NA}/{NB}, 95 per cent, magnitude bound at {SEVENTY}')
    print()
    print('  half-width on the DIFFERENCE, both halves at one rate:')
    for p in (0.40, 0.50, 0.607, 0.70, 0.80, 0.947):
        d, lo, hi = newcombe(round(p * NA), NA, round(p * NB), NB)
        print(f'      rate {p:5.3f}  ->  {(hi - lo) / 2 * 100:5.1f} points'
              + ('   ** this frame\'s own rate **' if abs(p - 0.607) < 1e-9 else ''))

    win = [(k, j) for k in range(NA + 1) for j in range(NB + 1)
           if WINDOW[0] <= k / NA <= WINDOW[1] and WINDOW[0] <= j / NB <= WINDOW[1]]
    tally, rng = Counter(), {}
    for k, j in win:
        v, a = verdict(k, j)
        tally[v] += 1
        lo_, hi_ = rng.get(v, (999.0, -999.0))
        rng[v] = (min(lo_, a), max(hi_, a))
    print()
    print(f'  every integer split with BOTH halves inside the {WINDOW[0]:.0%}-{WINDOW[1]:.0%} reproducing '
          f'window: {len(win)}')
    for v in ('RECURS', 'INCONCLUSIVE', "70's FIGURE REFUTED", 'RECURS BUT SMALLER'):
        c = tally.get(v, 0)
        r = f'|d| {rng[v][0]:5.1f} to {rng[v][1]:5.1f}' if c else '--'
        print(f'      {v:22s} {c:4d}  ({100 * c / len(win):5.1f}%)   {r}')
    empty = [v for v in ('RECURS', 'INCONCLUSIVE', "70's FIGURE REFUTED") if not tally.get(v)]
    print()
    if empty:
        print(f'  ⛔ UNREACHABLE AND LOAD-BEARING: {empty} -- a registered outcome that cannot happen')
        return 1
    print('  the three load-bearing outcomes are all reachable; RECURS begins at '
          f'|d| = {rng["RECURS"][0]:.1f} points, which is where "at or above about 21" comes from.')
    print(f'  RECURS BUT SMALLER is EMPTY here ({tally.get("RECURS BUT SMALLER", 0)}) and is registered as '
          f'empty: it needs a half outside the window, where condition 4 voids the result.')

    band = [(k, j) for k, j in win if 8.0 <= verdict(k, j)[1] <= 24.0]
    tb = Counter(verdict(k, j)[0] for k, j in band)
    print()
    print(f'  THE WITHDRAWN BAND 8-24 holds {len(band)} of those {len(win)} splits.  What each would have decided:')
    for v, c in tb.most_common():
        print(f'      {v:22s} {c:4d}  ({100 * c / len(band):5.1f}%)')
    dead = tb.get('INCONCLUSIVE', 0)
    print(f'  ⇒ {100 * dead / len(band):.1f} per cent of the band decided NOTHING: interval containing both '
          f'0 and {SEVENTY}.')
    print('    That is r7323 item ③\'s objection as a count rather than an assertion.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
