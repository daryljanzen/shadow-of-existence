#!/usr/bin/env python3
"""r7325+cc66 -- IS THE WITHIN-POOL REGISTRATION FAILABLE AT THE SIZE IT WILL BE SCORED AT?

`r7325` item ⑤ is now standing and it is `60`'s: *every registration states whether its band is
FAILABLE at the size it will be scored at, and a band that is not failable says so.*  This script is
that statement, computed rather than asserted, for item ③.3's within-pool measurement.

The registered claim is the one `60` reasons to: **two agents under ONE instruction should agree more
than two pools do**, so the within-pool `pi_d` should come in BELOW the between-pool figure measured on
this frame.  That makes the test one-sided: the claim fails when the within-pool interval's UPPER bound
does not fall below the between-pool point.

⛔ The answer at `40` paired reads is NO at the rate the claim itself expects, which is why this script
exists before the registration and not after it.

  python3 failability.py
"""
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7328_60_the_registration'))
import size as G                                                       # noqa: E402

BETWEEN = 0.269          # this frame's between-pool pi_d, pi_d.py, 21/78
EXPECT = 0.159           # 60's measured pi_d, the rate the within-pool claim expects to beat
FRAME = 78               # keys available on this frame


def resolves(n, rate=EXPECT, against=BETWEEN):
    """would an observation AT `rate`, on `n` paired keys, put its upper bound below `against`?"""
    k = round(rate * n)
    lo, hi = G.wilson(k, n)
    return hi < against, k, lo, hi


def main():
    print()
    print(f'  FAILABILITY OF THE WITHIN-POOL REGISTRATION -- one-sided, against this frame s'
          f' between-pool {100 * BETWEEN:.1f}%')
    print()
    print(f'  ⒜ at n = 40, which r7325 item ③.3 offers as "a real number": which OUTCOMES could fail it?')
    worst = None
    for k in range(41):
        lo, hi = G.wilson(k, 40)
        if hi < BETWEEN:
            worst = (k, lo, hi)
    print(f'      the largest observation whose upper bound clears {100 * BETWEEN:.1f}%: '
          f'{worst[0]}/40 = {100 * worst[0] / 40:.1f}%  [{100 * worst[1]:.1f}, {100 * worst[2]:.1f}]')
    ok, k, lo, hi = resolves(40)
    print(f'      but AT THE EXPECTED RATE {100 * EXPECT:.1f}%: {k}/40 = {100 * k / 40:.1f}%  '
          f'[{100 * lo:.1f}, {100 * hi:.1f}]  -> clears {100 * BETWEEN:.1f}%: {"YES" if ok else "NO"}')
    print(f'  ⇒ ⛔ NOT FAILABLE AT THE RATE IT EXPECTS.  n = 40 can only refute the claim if the')
    print(f'     within-pool rate comes in at or below {100 * worst[0] / 40:.1f}% -- an outcome range that')
    print(f'     EXCLUDES the {100 * EXPECT:.1f}% the claim is predicated on.  Registering at 40 would be')
    print(f'     r7321 s band again in a new quantity.')
    print()
    print(f'  ⒝ the smallest n that IS failable at the expected rate.')
    # ⛔ THIRD DEFECT OF THE CYCLE, IN THIS SCRIPT'S OWN FIRST FORM, kept here as a comment because it
    #   is the reason the answer is stated the way it is.  The first form reported `the first n that
    #   resolves`, scanning upward and taking the first YES.  That gave n = 59 while the printed table
    #   showed n = 60 as NO -- a self-contradicting output.  The criterion is NOT MONOTONE in n,
    #   because the expected count is ROUNDED: n = 59 takes k = 9 (15.3%, upper 26.5, clears) and
    #   n = 60 takes k = 10 (16.7%, upper 28.0, does not).  *** A threshold quoted off a non-monotone
    #   criterion is an artefact of the rounding and not a size. ***  What is reported instead is the
    #   smallest n from which it resolves for EVERY larger n in the frame, which is a size.
    stable = None
    for n in range(10, FRAME + 1):
        if all(resolves(m)[0] for m in range(n, FRAME + 1)):
            stable = n
            break
    flips = [n for n in range(10, FRAME + 1) if resolves(n)[0] and not resolves(n + 1)[0] and n < FRAME]
    for n in (40, 50, 59, 60, 68, 69, 78):
        ok, k, lo, hi = resolves(n)
        mark = '  <- stable from here up' if n == stable else ('  <- a ROUNDING flip, not a size'
                                                               if n in flips else '')
        print(f'      n = {n:3d}: {k:3d}/{n} = {100 * k / n:5.1f}%  [{100 * lo:5.1f}, {100 * hi:5.1f}]  '
              f'{"YES" if ok else "NO ":3s}{mark}')
    print(f'      the criterion flips back to NO above {len(flips)} different n in this range, all from'
          f' rounding k')
    print(f'  ⇒ failable from n = {stable} upward, and this frame holds {FRAME} keys, so the registration')
    print(f'    takes THE WHOLE FRAME read twice rather than a 40-key subset.')
    print()
    print(f'  ⒞ what the whole frame buys, at n = {FRAME}:')
    ok, k, lo, hi = resolves(FRAME)
    print(f'      at the expected {100 * EXPECT:.1f}%: {k}/{FRAME}  [{100 * lo:.1f}, {100 * hi:.1f}]  '
          f'-> clears {100 * BETWEEN:.1f}%: {"YES" if ok else "NO"}')
    half = None
    for k2 in range(FRAME + 1):
        lo2, hi2 = G.wilson(k2, FRAME)
        if hi2 < BETWEEN:
            half = (k2, lo2, hi2)
    print(f'      and the largest observation that still clears it: {half[0]}/{FRAME} = '
          f'{100 * half[0] / FRAME:.1f}%  [{100 * half[1]:.1f}, {100 * half[2]:.1f}]')
    print(f'  ⇒ so the registered band is: within-pool pi_d at or below {100 * half[0] / FRAME:.1f}% refutes')
    print(f'    nothing-to-choose and establishes the within-pool figure as genuinely lower; above it the')
    print(f'    measurement is INCONCLUSIVE and says so.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
