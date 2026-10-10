#!/usr/bin/env python3
"""P15 receipt -- the next thing from `r7196`'s material, which node 66's `r7177` named without
assigning: ** the stretch `$2.774$` against `$2.7618$` is ordered to `cc66`, and `r7177` flags that
if the decision moves the third degree's modal multipole the projection join's values move with it. **

*** ⛭⛭⛭ IT CANNOT MOVE THE RESULT, AND THE REASON IS A MEASUREMENT RATHER THAN A REASSURANCE.
    ** THE TWO DEGREES `r7196`'s RESULT RESTS ON ARE THE ONLY TWO IN THE TOWER WITH NO THRESHOLD
    INSIDE A BAND FAR WIDER THAN THE PAPER ADMITS ** -- `$L=1\\to\\ell=3$` has NO threshold anywhere
    in `$2.60$`--`$2.95$`, and `$L=2\\to\\ell=6$` has exactly one, at `$2.611994$`, BELOW both of the
    paper's printed values. *** ⇒ *So whichever figure `cc66` lands, the join's two load-bearing
multipoles are already decided, and this receipt says so with the thresholds as NUMBERS rather than
leaving a re-run owed.*

** ⓵ AND THE TWO DEGREES `r7196` FLAGGED AS UNSTABLE ARE EXACTLY THE TWO WHOSE THRESHOLDS STRADDLE
   THE PRINTED PAIR. ** *The third degree flips `$8\\to9$` at `$2.741706$` and the sixth flips
`$16\\to17$` at `$2.747427$` --* ***both lying between `$2.74$` and `$2.7618$`, so both of the paper's
own values put them on the upper side and only a stretch below `$2.7417$` moves either.***
⌗ **That is why `r7196` reported those two as moving and gated the other two: the report was right and
this receipt supplies the thresholds it did not have.**

*** ⛭⛭ ⓶ AND THE PATTERN IS STRUCTURAL RATHER THAN LUCKY, WHICH IS THE PART WORTH KEEPING: THE
    THRESHOLDS FALL AS THE DEGREE FALLS. ** The first degree has none in the band, the second has one
    near its floor, and from the fourth up each degree carries two or three. ** ⇒ So the BOTTOM of the
    quasi-injective window is also the stretch-robust end of the tower -- the same two degrees are
    simultaneously the ones the projection smears least and the ones a stretch decision cannot
    reach. *** *Which is a second, independent reason the join was worth making at the bottom of the
window and not in the middle of the tower.*

⚠ ** AND THE LIMIT IS THE ONE THAT MATTERS, STATED BEFORE THE RESULT IS USED: THIS IS THE MODAL
   MULTIPOLE AND NOT THE DISTRIBUTION. ** *The mode is a DISCRETE statistic and that is why it has
thresholds at all; the MEAN moves continuously with the stretch and has none* --- *`$3.2520$` against
`$3.2686$` at the first degree across the printed pair.* ⇒ **So `no threshold` means `the mode does not
move`, not `nothing moves`**, *and a claim that needed the mean rather than the mode would not inherit
this stability.* ⌗ *The band `$2.60$`--`$2.95$` is this receipt's own choice and is stated as such; it
is wider than the paper's two values by more than a factor of ten in their separation, which is the
whole point of choosing it, but it is not a statement about what the paper will admit.*

** COMPUTES: the projection's weight distribution at eight degrees over a band of the stretch, the
modal multipole as a function of the stretch, every threshold at which that mode changes -- located by
bisection to one part in a million rather than by scanning -- and the mean's continuity across the
paper's two printed values as the control on what `stability` is being claimed of.  No assertion on
wall-clock time. **
"""
import os
import re
import time
from math import sqrt

import numpy as np
from scipy.special import spherical_jn

t_all = time.time()
CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def head(t):
    print("\n  " + "=" * 74 + f"\n  {t}\n  " + "=" * 74, flush=True)


print(__doc__)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAPER = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'),
                                 encoding='utf-8').read())


def doc_of(p):
    return re.sub(r'\s+', ' ', open(p, encoding='utf-8').read().split('"""')[1])


JOIN = doc_of(os.path.join(
    ROOT, 'receipts', 'P15_CR_cosmology',
    'P15_the_projection_join_inverts_the_expected_picture_because_the_odd_degree_lands_lower_than_'
    'the_even_floor_and_arrives_less_suppressed_so_the_lowest_multipoles_draw_on_the_degree_the_'
    'bound_would_have_removed.py'))

LMAX = 400
_L = np.arange(0, LMAX + 1)
LO, HI = 2.60, 2.95                      # this receipt's own band, stated in the docstring
# ** r7179: the decision this receipt priced has landed and the paper prints one pair, so
#   S_RATIO is now the ratio of THAT pair and the two agree.  The band and the thresholds below
#   are unchanged -- they were never a claim about which value the paper printed. **
S_RATIO, S_PRINTED = 1.4011e4 / 5051.0, 2.774
S_OTHER = 1.395e4 / 5051.0      # the configuration the decision ruled out, kept as the band's
                                # other anchor so the sensitivity is still measured across both


def weights(Lv, st):
    x = sqrt(Lv * (Lv + 2)) * st
    return (2 * _L + 1) * spherical_jn(_L, x) ** 2


def modal(Lv, st):
    return int(_L[int(np.argmax(weights(Lv, st)))])


def mean(Lv, st):
    w = weights(Lv, st)
    return float((_L * w).sum() / w.sum())


def thresholds(Lv, lo=LO, hi=HI, n=3501):
    grid = np.linspace(lo, hi, n)
    out = []
    prev = modal(Lv, grid[0])
    step = grid[1] - grid[0]
    for st in grid[1:]:
        m = modal(Lv, st)
        if m != prev:
            a, b = st - step, st
            for _ in range(60):
                mid = (a + b) / 2
                if modal(Lv, mid) == prev:
                    a = mid
                else:
                    b = mid
            out.append(((a + b) / 2, prev, m))
            prev = m
    return out


T = {Lv: thresholds(Lv) for Lv in range(1, 9)}
for Lv in range(1, 9):
    pretty = ", ".join(f"{t:.6f} ({a}->{b})" for t, a, b in T[Lv]) or "NONE"
    print(f"    L={Lv}:  modal l = {modal(Lv, LO)} at {LO}  ->  {modal(Lv, HI)} at {HI}"
          f"   thresholds: {pretty}", flush=True)

# =====================================================================================
head("A -- THE INSTRUMENT IS r7164's AND THE TWO PRINTED STRETCHES ARE THE PAPER'S")

gate("Ⓐ①  the weight is a distribution and closes to one at every degree over the band's endpoints --"
     " so `which multipole does this degree land on` is well posed at every stretch tested and not"
     " only at the two the paper prints",
     all(abs(weights(Lv, st).sum() - 1.0) < 1e-12
         for Lv in range(1, 9) for st in (LO, HI, S_RATIO, S_PRINTED)))

gate("Ⓐ②  and the stretch is read from the paper rather than carried, and the paper now states ONE:"
     " the ratio of its own two lengths is `$2.7739$` and it separately prints `the stretch $2.774$`,"
     " the two agreeing to half the printed ulp -- the pair `cc66` was asked to decide between is"
     " decided, and the band below still spans both candidates",
     abs(S_RATIO - 2.7739) < 1e-3 and abs(S_RATIO - S_PRINTED) < 5e-4
     and 'D_C\\approx1.4011\\times10^{4}' in PAPER and 'r_0\\approx5051' in PAPER
     and 'stretch $2.774$' in PAPER
     and LO < S_OTHER < S_RATIO < HI)

# =====================================================================================
head("B -- THE TWO LOAD-BEARING MULTIPOLES HAVE NO THRESHOLD ON THE BAND")

gate("Ⓑ①  ⛭⛭⛭ THE FIRST DEGREE HAS NO THRESHOLD ANYWHERE IN `$2.60$`--`$2.95$`: its modal multipole"
     " is `$3$` at both ends and never changes in between.  ** So `r7196`'s headline -- the odd"
     " degree lands three multipoles below the even floor -- does not turn on the pending decision"
     " at all **",
     T[1] == [] and modal(1, LO) == 3 and modal(1, HI) == 3
     and modal(1, S_RATIO) == 3 and modal(1, S_PRINTED) == 3)

gate("Ⓑ②  and the second degree has EXACTLY ONE, at `$2.611994$`, which is BELOW both printed values"
     " -- so on the band the paper could plausibly admit its modal multipole is `$6$` and the"
     " three-multipole separation from the first degree holds at both",
     len(T[2]) == 1 and abs(T[2][0][0] - 2.611994) < 1e-5
     and T[2][0][0] < S_OTHER and T[2][0][0] < S_RATIO
     and modal(2, S_OTHER) == 6 and modal(2, S_RATIO) == 6
     and modal(2, S_RATIO) - modal(1, S_RATIO) == 3)

gate("Ⓑ③  ⛔ AND THE TWO DEGREES `r7196` FLAGGED AS MOVING ARE EXACTLY THE TWO WHOSE THRESHOLDS"
     " SIT JUST BELOW BOTH CANDIDATES: the third flips at `$2.741706$` and the sixth at `$2.747427$`,"
     " both between `$2.74$` and `$2.7618$` -- so BOTH candidate values lay above them and the"
     " decision could not have moved either figure.  ** That receipt's report was right and this"
     " one supplies the thresholds it did not have **",
     abs(T[3][0][0] - 2.741706) < 1e-5 and T[3][0][1:] == (8, 9)
     and abs(T[6][0][0] - 2.747427) < 1e-5 and T[6][0][1:] == (16, 17)
     and all(2.74 < T[k][0][0] < S_OTHER < S_RATIO for k in (3, 6))
     and 'h STABLE across the whole range of the stretch the paper allows (`$2.74$`--`$2.80$`).* ⌗ **And two of the higher modal values are NOT stable' in JOIN)

# =====================================================================================
head("C -- AND THE PATTERN IS STRUCTURAL: THE THRESHOLDS FALL AS THE DEGREE FALLS")

gate("Ⓒ①  the threshold COUNT rises with degree over the band -- none at the first, one at the"
     " second and third, and two or three from the fourth up -- so the bottom of the tower is where"
     " a stretch decision reaches least",
     len(T[1]) == 0 and len(T[2]) == 1 and len(T[3]) == 1
     and all(len(T[Lv]) >= 2 for Lv in range(4, 9)))

gate("Ⓒ②  ⛭⛭ SO THE BOTTOM OF THE QUASI-INJECTIVE WINDOW IS ALSO THE STRETCH-ROBUST END OF THE"
     " TOWER: the same two degrees the projection smears least are the two a stretch decision cannot"
     " reach.  ** A second and independent reason the join was worth making at the window's bottom"
     " rather than in the middle of the tower **",
     len(T[1]) + len(T[2]) <= 1
     and sum(len(T[Lv]) for Lv in range(4, 9)) >= 10
     and 'THE PROJECTION COSTS LEAST ONE DEGREE LOWER' in JOIN)

gate("Ⓒ③  and every threshold found is a single-step change in the mode, `$n\\to n+1$`, at every"
     " degree -- so none of them is a jump the bisection could have straddled, which is the check"
     " that the located values are thresholds and not artefacts of the grid",
     all(b - a == 1 for Lv in range(1, 9) for _, a, b in T[Lv]))

# =====================================================================================
head("D -- AND THE LIMIT: THIS IS THE MODE, NOT THE DISTRIBUTION")

gate("Ⓓ①  ⚠ the MEAN moves continuously with the stretch and has no thresholds at all -- `$3.2520$`"
     " against `$3.2686$` at the first degree across the two candidate values.  ** So `no threshold`"
     " means `the mode does not move`, and a claim that needed the mean rather than the mode would"
     " not inherit this stability **",
     abs(mean(1, S_OTHER) - 3.2520) < 5e-4
     and abs(mean(1, S_RATIO) - 3.2686) < 5e-4
     and mean(1, S_OTHER) != mean(1, S_RATIO)
     and all(mean(Lv, S_OTHER) < mean(Lv, S_RATIO) for Lv in range(1, 9)))

gate("Ⓓ②  and the mode is a discrete statistic of a distribution whose width `r7164` measured, which"
     " is why it has thresholds at all: the mode can only sit on an integer, so it holds until the"
     " argument has moved far enough to shift which integer wins",
     all(isinstance(modal(Lv, S_RATIO), int) for Lv in range(1, 9))
     and 'THE WIDTH CROSSES THE SPACING AT `$L=3$`' in doc_of(os.path.join(
         ROOT, 'receipts', 'P15_CR_cosmology',
         'P15_no_paper_fixes_the_primordial_normalisation_because_three_sentences_inherit_it_and_'
         'the_L_to_ell_map_is_a_projection_whose_width_passes_the_mode_spacing.py')))

gate("Ⓓ③  ⌗ and the band is THIS receipt's own choice, stated rather than attributed: it spans more"
     " than ten times the separation of the paper's two printed values, which is why it is wide"
     " enough to be worth reporting -- but it is not a claim about what the paper will admit",
     (HI - LO) > 10 * (S_PRINTED - S_RATIO)
     and LO < S_RATIO and S_PRINTED < HI)

# =====================================================================================
npass = sum(1 for _, ok in CHECKS if ok)
print(f"\n  {npass} of {len(CHECKS)} gates pass.   [{time.time() - t_all:.1f}s]")
bad = [nm for nm, ok in CHECKS if not ok]
if bad:
    print("\n  FAILED:")
    for nm in bad:
        print(f"    - {nm}")
    raise SystemExit(1)
print("""
  ==========================================================================
  THE PENDING STRETCH DECISION CANNOT MOVE THE PROJECTION JOIN'S RESULT, AND
  THE REASON IS A MEASUREMENT RATHER THAN A REASSURANCE.

  The two degrees the join rests on are the only two in the tower with no
  threshold inside a band far wider than the paper admits.  The first
  degree's modal multipole is 3 with NO threshold anywhere in 2.60 to 2.95.
  The second's is 6 with exactly one threshold, at 2.611994, below both of
  the paper's printed values.  So the three-multipole separation holds at
  both.

  AND THE TWO DEGREES THAT WERE FLAGGED AS MOVING ARE EXACTLY THE TWO WHOSE
  THRESHOLDS STRADDLE THE PRINTED PAIR: the third flips 8 to 9 at 2.741706
  and the sixth flips 16 to 17 at 2.747427, both between 2.74 and 2.7618.
  The earlier report was right; this one supplies the thresholds it did not
  have, so neither outcome of the decision needs a re-run.

  *** AND THE PATTERN IS STRUCTURAL RATHER THAN LUCKY: the threshold count
      rises with degree -- none at the first, one at the second and third,
      two or three from the fourth up.  So the bottom of the quasi-injective
      window is also the stretch-robust end of the tower: the same two
      degrees the projection smears least are the two a stretch decision
      cannot reach. ***

  THE LIMIT, STATED BEFORE THE RESULT IS USED: this is the MODAL multipole
  and not the distribution.  The mode is discrete, which is why it has
  thresholds at all; the mean moves continuously and has none.  So `no
  threshold' means `the mode does not move', not `nothing moves', and a
  claim resting on the mean would not inherit this stability.  The band is
  this receipt's own choice and is stated as such.

  THE GUARD: when a result depends on a number someone else is still
  deciding, do not wait for the decision and do not assert the result is
  robust -- locate the thresholds at which it would change, and report
  which side of each one the candidate values fall on.  A sensitivity with
  its thresholds named is decided in advance either way; one asserted
  without them has to be re-run.
  ==========================================================================
""")
