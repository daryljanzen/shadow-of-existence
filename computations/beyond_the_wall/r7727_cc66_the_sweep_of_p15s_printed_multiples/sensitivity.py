#!/usr/bin/env python3
"""`r7727+cc66.2` the in-scope sites' printed multiples, read under each end of their own family.

⛭ This is `r7717`'s OWN form -- report the figure under each admissible denominator, side by side -- and
NOT a new instrument.  `PREDICTION.md` §5 forbids improvising a test, and this improvises nothing: every
denominator below is a value the cited receipt already computes and GATES.
"""
import math
import sys

from scipy.stats import norm

# pinned by P15_the_combs_resolution_is_four_multipoles_... at its own gates (5e-6 / 1e-4)
RR0, RRMIN = 0.04252, 0.00949
SE0, SEMIN = 0.01358, 0.00303
SIG_L, SIG_S = 2.2303, 5.1354
FS = [0.0, 0.1, 0.25, 0.5, 0.75, 1.0]
# pinned by P15_the_cross_term_is_not_the_channel_...
SLOPE_1779, SPREAD_1779, N_1779 = 0.01034, 0.00137, 12


def ceiling(n):
    p = 1.0 / math.factorial(n)
    return math.factorial(n), p, float(norm.isf(p / 2.0))


def main():
    d_lev, d_slp = SIG_L * RRMIN, SIG_S * SEMIN
    print("\n  ⛭ SITE 2059 -- two printed multiples, under each end of their own six-member family\n"
          f"     family FS = {FS}; the printed denominator is its MINIMUM, by that receipt's "
          f"own cc66.63 ruling\n")
    print(f"     LEVEL  {d_lev:+.5f}  / {RRMIN:.5f} (min)  = {d_lev / RRMIN:.2f}   <- PRINTED 2.23")
    print(f"                        / {RR0:.5f} (f=0)  = {d_lev / RR0:.2f}")
    print(f"     SLOPE  {d_slp:+.5f}  / {SEMIN:.5f} (min)  = {d_slp / SEMIN:.2f}   <- PRINTED 5.14")
    print(f"                        / {SE0:.5f} (f=0)  = {d_slp / SE0:.2f}\n")
    print(f"     ⇒ the printed 2.23 falls to {d_lev / RR0:.2f} -- BELOW ONE -- and the printed 5.14 to "
          f"{d_slp / SE0:.2f}, at the family's other end.\n")
    perm, p, sd = ceiling(len(FS))
    print(f"     ⇒ ceiling: {len(FS)} members, {perm} permutations, floor p = {p:.3g} ⇒ {sd:.2f} "
          f"sd-equivalent.\n       So 5.14 READ AS A SIGNIFICANCE exceeds what any resampling of this "
          f"family can express.\n")

    print("  ⛭ SITE 1779 -- the twelve-setting multiple\n")
    print(f"     slope {SLOPE_1779:+.5f} / setting spread {SPREAD_1779:.5f} = "
          f"{SLOPE_1779 / SPREAD_1779:.2f}   <- PRINTED as 'seven and a half'")
    perm, p, sd = ceiling(N_1779)
    print(f"     ⇒ ceiling: {N_1779} settings, {perm} permutations, floor p = {p:.3g} ⇒ {sd:.2f} "
          f"sd-equivalent.\n       So {SLOPE_1779 / SPREAD_1779:.2f} READ AS A SIGNIFICANCE also "
          f"exceeds its family's ceiling.\n")
    print("  ⛔ BUT P15 PRINTS A RATIO AT BOTH SITES, WITH ITS DENOMINATOR NAMED, AND NOT A PROBABILITY.\n"
          "    By the r7721 ruling on the both-arms ratios -- 'the sentence states a ratio and makes no\n"
          "    probability claim; the ceiling is a fact about what that statistic can carry as evidence,\n"
          "    not an error in the sentence' -- neither printed figure is an error. ⇒ The ceilings above\n"
          "    are reported and are NOT grounds for a correction.\n")
    return 0


if __name__ == '__main__':
    sys.exit(main())
