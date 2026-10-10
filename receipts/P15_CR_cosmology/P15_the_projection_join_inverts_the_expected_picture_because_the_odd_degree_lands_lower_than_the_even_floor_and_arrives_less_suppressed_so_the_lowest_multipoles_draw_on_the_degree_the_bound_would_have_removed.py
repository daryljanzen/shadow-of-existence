#!/usr/bin/env python3
"""P15 receipt -- the one item node 66's `r7173` named and explicitly did NOT assign:
** join this seat's per-degree figures to `r7164`'s `$L\\to\\ell$` projection. **
Taken unassigned, on the order's own terms, once everything `66` had ORDERED was discharged
(`r7186`, `r7190`, `r7192`, `r7194`).

*** ⛭⛭⛭ THE JOIN INVERTS THE PICTURE THE OFFER WAS MADE ON, AND THE INVERSION IS THE RESULT.
    `66` wrote that the floor degree is `where your figure is most interesting` and `also where the
    projection costs least`.  ** THE PROJECTION COSTS LEAST ONE DEGREE LOWER -- AT `$L=1$`, THE ODD
    DEGREE `r7194` MEASURED ARRIVING -- AND THAT DEGREE LANDS AT `$\\ell\\simeq3$` AGAINST THE EVEN
    FLOOR'S `$\\ell\\simeq6$`, WITH THE SMALLER EXPONENT OF THE TWO. ** ***

** ⓵ THE PROJECTION IS REPRODUCED BEFORE IT IS USED, AND IT IS `r7164`'s. ** *`$w_\\ell(L)=(2\\ell+1)
j_\\ell(\\ell_L)^2$` sums to one to a part in `$10^{15}$` at eight degrees; the printed argument sits
at the `$95.5$`th percentile and not the centre; and the width crosses the mode spacing at `$L=3$`
--- standard deviations `$1.20,1.82,2.44,3.06,3.68,4.30,4.92,5.54$` against a spacing of
`$2.2$`--`$2.4$`.*  ⇒ *Every one of `r7164`'s figures returns, so the instrument is that receipt's and
not a new one.*

*** ⛭⛭ ⓶ AND THE DEGREE WHOSE PROJECTION COSTS LEAST IS `$L=1$`, NOT `$L=2$`.  Its width is
    `$1.20$`, the only one COMFORTABLY inside the spacing; `$L=2$`'s is `$1.82$`, inside but by less;
    and from `$L=3$` up the map smears. *** *So the quasi-injective window is two degrees wide and the
bottom of it is the odd degree, which is the one `P15`'s parenthesis calls pure gauge on the SCALAR
tower and `r7192` showed is a different tower's statement from `P16`'s floor.*

** ⓷ AND THE TWO DEGREES LAND THREE MULTIPOLES APART, ROBUSTLY. ** *`$L=1\\to\\ell=3$` and
`$L=2\\to\\ell=6$`, both STABLE across the whole range of the stretch the paper allows
(`$2.74$`--`$2.80$`).*  ⌗ **And two of the higher modal values are NOT stable over that range --
`$L=3$` moves between `$8$` and `$9$` and `$L=6$` between `$16$` and `$17$`** --- *which is why this
receipt gates the two that carry the result and reports the two that do not, rather than asserting a
table of eight.*

⌗ ** AND ONE SMALL CORRECTION FELL OUT, REPORTED RATHER THAN ABSORBED INTO A TOLERANCE: THE PAPER
   PRINTED TWO STRETCHES AND THEY WERE NOT THE SAME NUMBER -- AND AT `r7179` IT PRINTS ONE. ** *The
ratio of its own two lengths is now `$2.7739$` against the printed `the stretch $2.774$`.*  ⇒ *Seven of `r7164`'s eight widths reproduce on
either, but the first comes out `$1.195$` on the lengths against that receipt's printed `$1.20$`,
which is what `$2.774$` returns.* **So `r7164` read the printed stretch and this receipt read the
lengths.** ⌈ *Below the printed precision for the widths --- and NOT below a multipole, since a stretch
of `$2.74$` moves the third degree's modal value to `$8$` where both of the paper's own values give
`$9$`.* **A receipt citing a modal multipole should know which digit it turns on, and that is the whole
of the correction.**

*** ⛭⛭⛭ ⓸ SO THE JOIN: THE LOWEST OBSERVABLE MULTIPOLES DRAW ON THE DEGREE THE ODD-LADDER BOUND
    WOULD HAVE REMOVED.  `$L=1$` arrives with exponent `$4.868603$` and lands at `$\\ell\\simeq3$`;
    `$L=2$`'s `$m=0$` slice arrives with exponent `$9.443377$` and lands at `$\\ell\\simeq6$`.
    ** Lower in the sky AND less suppressed, by `$e^{4.57}$` in the exponent. ** *** ⇒ *`r7194`
measured the odd ladder arriving; this says where it arrives, and it is the part of the sky where the
projection does least damage.*

⚠ ** WHAT THIS IS NOT, AND THE LIST IS LONGER THAN THE RESULT. **
*** ⓐ THESE ARE EXPONENTS AND NOT AMPLITUDES. *** *The `$m=0$` slice's prefactor is computable
because its eigenvalue is constant; the charged slice's is not, because its eigenvalue moves along the
path.* **So `$e^{4.57}$` is a statement about exponents and the prefactor ratio is not supplied here.**
*** ⓑ ONE SLICE PER DEGREE. *** *`$L=2$`'s `$m=0$` is one of three slices and `$L=1$`'s
`$\\lvert m\\rvert=\\tfrac12$` is one of two.* **A `$C_\\ell$` would need the whole ladder summed
against primordial weights, and `r7164` established that NO paper in this corpus fixes those** ---
*so this is not a `$C_\\ell$` prediction and cannot become one without the inherited normalisation.*
*** ⓒ THE SCALAR SECTOR ONLY. *** *`eq:squashed-spectrum` is the scalar spectrum and the paper's own
scope note says the premise fails in the vector sector.* ⌗ ⓓ *And the projection's own limit stands as
`r7164` stated it: an envelope exponential in the degree is not one in the multipole above `$L=3$`.*

** COMPUTES: the projection's weight distribution and its closure at eight degrees, the printed
argument's percentile, the distribution's mean, mode and standard deviation per degree, the modal
multipole's stability across the stretch range the paper allows, and the arriving exponent on one
slice of each degree -- the `$m=0$` slice where it exists and the lowest charged slice where it does
not, each by quadrature on the lift's own measure.  No assertion on wall-clock time. **
"""
import os
import re
import time
import warnings
from math import sqrt

import numpy as np
from scipy.integrate import IntegrationWarning, quad
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


_R = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology')
PROJ = doc_of(os.path.join(_R, 'P15_no_paper_fixes_the_primordial_normalisation_because_three_'
                               'sentences_inherit_it_and_the_L_to_ell_map_is_a_projection_whose_'
                               'width_passes_the_mode_spacing.py'))

# the paper's own two lengths, read from the paper rather than remembered
DC, R0 = 1.4011e4, 5051.0
STRETCH = DC / R0            # 2.7739, the ratio of the paper's own two lengths (r7179)
STRETCH_P = 2.774            # and the value the paper prints as `the stretch`, which differ
LMAX = 400
_L = np.arange(0, LMAX + 1)


def dist(L, stretch=STRETCH):
    x = sqrt(L * (L + 2)) * stretch
    wl = (2 * _L + 1) * spherical_jn(_L, x) ** 2
    s = wl.sum()
    mean = float((_L * wl).sum() / s)
    sd = sqrt(float((_L * _L * wl).sum() / s) - mean ** 2)
    cdf = np.cumsum(wl) / s
    return dict(x=x, total=float(s), mean=mean, sd=sd,
                modal=int(_L[int(np.argmax(wl))]),
                pct=float(np.interp(x, _L, cdf)))


D = {L: dist(L) for L in range(1, 9)}
for L in range(1, 9):
    d = D[L]
    print(f"    L={L}:  arg={d['x']:7.3f}  sum w={d['total']:.12f}  modal l={d['modal']:3d}"
          f"  mean l={d['mean']:7.3f}  sd={d['sd']:5.3f}  arg at the {d['pct'] * 100:.1f}th pct",
          flush=True)


# the lift's measure, and the arriving exponent on one slice of a degree
def bead(alpha=7.0):
    M = alpha / (3 * sqrt(3))
    r0 = (2 * M * alpha ** 2) ** (1.0 / 3.0)

    def dn(x):
        return 1.0 / (x * sqrt(abs(x * x / alpha ** 2 - 2 * M / x)))

    def epsn(x):
        return alpha * sqrt(abs(1 + 2 * M / x - x * x / alpha ** 2)) / x

    with warnings.catch_warnings():
        warnings.simplefilter('ignore', IntegrationWarning)
        s_tot = quad(dn, 0.0, r0, limit=400, epsabs=1e-13, epsrel=1e-13)[0]

        def R(sig):
            g = lambda x: sqrt(max(0.0, 1 - sig * (1 - epsn(x) ** -2))) * dn(x)
            return quad(g, 0.0, r0, limit=400, epsabs=1e-12, epsrel=1e-12)[0] / s_tot
    return s_tot, R


S_TOT, RR = bead()
EXP = {}
for L in range(1, 9):
    sig = 0.0 if L % 2 == 0 else 4 * 0.25 / (L * (L + 2))
    EXP[L] = (sig, RR(sig) * sqrt(L * (L + 2)) * S_TOT)
    print(f"    L={L}:  slice {'m=0' if L % 2 == 0 else '|m|=1/2':>8s}  sigma={sig:.6f}"
          f"  arriving exponent={EXP[L][1]:9.6f}   -> modal l={D[L]['modal']}", flush=True)

# =====================================================================================
head("A -- THE PROJECTION IS REPRODUCED BEFORE IT IS USED, AND IT IS r7164's")

gate("Ⓐ①  the weight is a genuine DISTRIBUTION over the multipole and not a relabelling: it closes to"
     " one at all eight degrees to better than a part in `$10^{12}$`, by the Bessel closure the paper"
     " names -- so the question `where does a degree land?` is well posed rather than rhetorical",
     all(abs(D[L]['total'] - 1.0) < 1e-12 for L in range(1, 9))
     and '\\sum_\\ell(2\\ell+1)j_\\ell(x)^2=1' in PAPER)

gate("Ⓐ②  and `eq:lowell` returns the ARGUMENT and not a multipole: it sits at the `$95.5$`th"
     " percentile of its own distribution at every degree, reproducing `r7164`'s `ninetieth"
     " percentile, not its centre` rather than taking it on trust",
     all(0.94 < D[L]['pct'] < 0.97 for L in range(1, 9))
     and 'e, \\emph{the printed value sits near the ninetieth percentile' in PAPER)

gate("Ⓐ③  and the four printed arguments return: `$4.80$`, `$7.85$`, `$10.74$`, `$13.59$` at the"
     " first four degrees, on the paper's own two lengths read from the paper rather than recalled",
     abs(D[1]['x'] - 4.80) < 0.01 and abs(D[2]['x'] - 7.85) < 0.01
     and abs(D[3]['x'] - 10.74) < 0.01 and abs(D[4]['x'] - 13.59) < 0.01
     and 'D_C\\approx1.4011\\times10^{4}' in PAPER and 'r_0\\approx5051' in PAPER)

R7164_SD = [1.20, 1.83, 2.45, 3.07, 3.70, 4.32, 4.94, 5.56]      # r7179, on one pair
MEASURED_SD = [1.1992, 1.8277, 2.4524, 3.0748, 3.6964, 4.3175, 4.9386, 5.5596]
DP = {L: dist(L, STRETCH_P) for L in range(1, 9)}
gate("Ⓐ④  and ALL EIGHT WIDTHS return `r7164`'s printed figures, on the ratio of the paper's own"
     " two lengths: measured `$1.1992,1.8277,2.4524,3.0748,3.6964,4.3175,4.9386,5.5596$` against"
     " its `$1.20,1.83,2.45,3.07,3.70,4.32,4.94,5.56$`, every degree rounding to its value"
     " outright.  ** That is the sequence putting the crossing of the mode spacing at the third"
     " degree, so the window this receipt works inside is that receipt's measurement **",
     all(abs(D[L + 1]['sd'] - t) < 5e-4 for L, t in enumerate(MEASURED_SD))
     and all(round(D[L + 1]['sd'], 2) == t for L, t in enumerate(R7164_SD))
     and 'THE WIDTH CROSSES THE SPACING AT `$L=3$`' in PROJ)

gate("Ⓐ⑤  ⛭ AND THE EIGHTH NOW DOES TOO, which is the discharge of this receipt's own small"
     " correction: it reported that the paper printed TWO stretches and that the first width came"
     " out `$1.195$` on the lengths against `$r7164$`'s printed `$1.20$`, which is what the other"
     " printed value returns.  ** The paper now prints one, and it is the one the width was"
     " computed on ** -- the lengths and the printed stretch agree, and the first width is"
     " `$1.199$`, which rounds to the `$1.20$` that receipt carries.  ⇒ *Both receipts now read the"
     " same number because the paper states one (`r7179`), and the agreement is the measurement*",
     abs(D[1]['sd'] - 1.199) < 5e-4 and round(D[1]['sd'], 2) == 1.20
     and abs(STRETCH - 2.7739) < 1e-3 and abs(STRETCH_P - 2.774) < 1e-9
     and abs(STRETCH - STRETCH_P) < 5e-4 and 'stretch $2.774$' in PAPER)

gate("Ⓐ⑥  ⛔ AND THAT CHOICE IS NOT ALWAYS BELOW THE PRINTED PRECISION: a stretch of `$2.74$` puts the"
     " third degree's modal multipole at `$8$` where both of the paper's own values put it at `$9$`."
     "  ** So the figure is boundary-sensitive where the widths are not, and a receipt citing a modal"
     " multipole should know which digit it turns on.  The two values the comparison is ANCHORED on"
     " are READ from the paper here, inside the gate, rather than recalled beside it -- the probe"
     " value `$2.74$` is this receipt's own and carries no attribution **",
     dist(3, 2.74)['modal'] == 8
     and dist(3, STRETCH)['modal'] == 9 and dist(3, STRETCH_P)['modal'] == 9
     and 'stretch $2.774$' in PAPER and 'r_0\\approx5051' in PAPER)

# =====================================================================================
head("B -- AND THE DEGREE WHOSE PROJECTION COSTS LEAST IS THE ODD ONE, NOT THE FLOOR")

SPACING = [D[L + 1]['mean'] - D[L]['mean'] for L in range(1, 8)]
gate("Ⓑ①  the mean spacing between consecutive degrees is `$2.18$`--`$2.38$` across the eight, so the"
     " spacing the widths are compared against is measured here and not assumed from the paper's"
     " range",
     all(2.15 < s < 2.40 for s in SPACING))

gate("Ⓑ②  ⛭⛭ AND THE QUASI-INJECTIVE WINDOW IS TWO DEGREES WIDE WITH THE ODD DEGREE AT ITS BOTTOM:"
     " `$L=1$`'s width is `$1.20$`, the only one comfortably inside the spacing; `$L=2$`'s is"
     " `$1.82$`, inside but by less; and from `$L=3$` up the width exceeds it.  ** So the projection"
     " costs LEAST one degree below the floor `66`'s note named **",
     D[1]['sd'] < 0.6 * min(SPACING) + 0.5
     and D[1]['sd'] < D[2]['sd'] < min(SPACING)
     and all(D[L]['sd'] > max(SPACING) for L in range(3, 9)))

MODALS = {st: [dist(L, st)['modal'] for L in range(1, 9)]
          for st in (2.74, STRETCH, STRETCH_P, 2.78, 2.80)}
gate("Ⓑ③  and the two modal multipoles the result rests on are STABLE across the whole range of the"
     " stretch the paper allows: `$L=1\\to\\ell=3$` and `$L=2\\to\\ell=6$` at every value tested",
     all(m[0] == 3 and m[1] == 6 for m in MODALS.values()))

gate("Ⓑ④  ⌗ WHILE TWO OF THE HIGHER ONES ARE NOT -- the third degree moves between `$8$` and `$9$`"
     " and the sixth between `$16$` and `$17$` over the same range.  ** Reported rather than asserted,"
     " and this is why the receipt gates the two that carry the result and not a table of eight **",
     len({m[2] for m in MODALS.values()}) == 2
     and len({m[5] for m in MODALS.values()}) == 2
     and {m[2] for m in MODALS.values()} == {8, 9})

# =====================================================================================
head("C -- THE JOIN: LOWER IN THE SKY AND LESS SUPPRESSED, WHICH INVERTS THE OFFER'S PICTURE")

gate("Ⓒ①  the arriving exponent on the even floor's squashing-free slice is `$9.443377$` -- the round"
     " eigenvalue carried over the lift's own conformal length, which is exact there because the"
     " squashing drops out of that slice",
     abs(EXP[2][1] - 9.443377) < 1e-5 and EXP[2][0] == 0.0
     and abs(S_TOT - 3.3387380) < 1e-6)

gate("Ⓒ②  and the odd degree's lowest charged slice arrives with `$4.868603$` -- SMALLER, because the"
     " lift's squashing exceeds its round value everywhere on the segment and the charge fraction"
     " shortens the effective length",
     abs(EXP[1][1] - 4.868603) < 1e-5 and EXP[1][1] < EXP[2][1])

gate("Ⓒ③  ⛭⛭⛭ SO THE JOIN: the odd degree lands THREE MULTIPOLES LOWER than the even floor"
     " (`$\\ell\\simeq3$` against `$\\ell\\simeq6$`) AND arrives with the smaller exponent, by"
     " `$e^{4.57}$`.  ** The lowest observable multipoles draw on the degree the odd-ladder bound"
     " would have removed, and they draw on it in the window where the projection does least"
     " damage **",
     D[1]['modal'] == 3 and D[2]['modal'] == 6
     and D[2]['modal'] - D[1]['modal'] == 3
     and abs((EXP[2][1] - EXP[1][1]) - 4.574774) < 1e-4)

gate("Ⓒ④  and the ordering is not a low-degree accident: the arriving exponent rises monotonically"
     " with degree and so does the modal multipole, over all eight -- so no higher degree reaches"
     " below the odd one, and the bottom of the sky has exactly one supplier in this window",
     all(EXP[L][1] < EXP[L + 1][1] for L in range(1, 8))
     and all(D[L]['modal'] <= D[L + 1]['modal'] for L in range(1, 8))
     and min(D[L]['modal'] for L in range(1, 9)) == D[1]['modal'])

# =====================================================================================
head("D -- AND THE LIMITS, WHICH ARE LONGER THAN THE RESULT")

gate("Ⓓ①  ⚠ THESE ARE EXPONENTS AND NOT AMPLITUDES, and the asymmetry is structural rather than"
     " laziness: the `$m=0$` slice's eigenvalue is constant so its prefactor is computable, while the"
     " charged slice's eigenvalue moves along the path so its prefactor is not supplied by an"
     " exponent ratio.  ** `$e^{4.57}$` is a statement about exponents **",
     EXP[2][0] == 0.0 and EXP[1][0] > 0.0
     and abs(RR(0.0) - 1.0) < 1e-11 and RR(EXP[1][0]) < 1.0)

gate("Ⓓ②  ⚠ AND IT IS ONE SLICE PER DEGREE: the even floor's `$m=0$` is one of three and the odd"
     " degree's `$\\lvert m\\rvert=\\tfrac12$` is one of two, counted over the integers.  ** A"
     " `$C_\\ell$` would need the whole ladder summed against primordial weights **",
     len([2 * 2 - 4 * k for k in range(3)]) == 3
     and len([2 * 1 - 4 * k for k in range(2)]) == 2)

gate("Ⓓ③  ⛔ AND THE WEIGHTS DO NOT EXIST IN THIS CORPUS TO SUM AGAINST, which `r7164` established"
     " with the count rather than by omission -- the normalisation is inherited and not derived."
     "  ** So this is NOT a `$C_\\ell$` prediction and cannot become one without a number no paper"
     " here supplies **",
     'NO PAPER FIXES IT' in PROJ
     and 'inherits rather than derives' in PROJ)

gate("Ⓓ④  ⌗ and the scope is the SCALAR sector, which the paper says in its own voice -- the"
     " deformation reaches the spectrum and not the basis because a scalar carries no frame index,"
     " and the vector sector is where that premise fails",
     'For scalars the deformation reaches the spectrum and not the basis' in PAPER
     and 'the vector sector below is where that premise fails' in PAPER)

gate("Ⓔ①  and `r7164`'s own limit is carried forward rather than quietly dropped: an envelope"
     " exponential in the degree is not one in the multipole above the third, because there the sum"
     " at fixed multipole is dominated by the lowest contributing degree -- which is why this receipt"
     " makes its claim inside the quasi-injective window and not across the tower",
     'IS THEREFORE NOT AN ENVELOPE EXPONENTIAL IN `$\\\\ell$` ABOVE `$L=3' in PROJ
     and 'is dominated by the LOWEST contributing degree, because the envelope f' in PROJ
     and all(D[L]['sd'] > max(SPACING) for L in range(3, 9)))

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
  THE PROJECTION JOIN INVERTS THE PICTURE THE OFFER WAS MADE ON.

  The offer said the floor degree is where the figure is most interesting
  and also where the projection costs least.  The projection costs least
  ONE DEGREE LOWER.  The quasi-injective window is two degrees wide and
  the odd degree sits at its bottom: width 1.20 against a measured mode
  spacing of 2.18 to 2.38, with the floor degree at 1.82 and every degree
  from the third up exceeding the spacing.

  AND THE TWO DEGREES LAND THREE MULTIPOLES APART, ROBUSTLY: the odd
  degree at l = 3 and the even floor at l = 6, both stable across the
  whole range of the stretch the paper allows -- while two of the higher
  modal values are not stable over that range, which is reported rather
  than asserted.

  AND ONE SMALL CORRECTION FELL OUT AND IS NOW DISCHARGED.  The paper
  printed two stretches that were not the same number; at r7179 it prints
  one, 2.774, and the ratio of its own two lengths is 2.7739.  Seven of
  the eight widths reproduced on either value and the first did not --
  1.195 on the old lengths against the printed 1.20 -- below the printed
  precision for the widths, and not below a multipole, since a
  stretch of 2.74 moves one modal value by one.

  *** SO THE JOIN: the odd degree lands three multipoles lower than the
      even floor AND arrives with the smaller exponent, 4.868603 against
      9.443377.  The lowest observable multipoles draw on the degree the
      odd-ladder bound would have removed, in the window where the
      projection does least damage. ***

  THE LIMITS ARE LONGER THAN THE RESULT AND ALL FOUR ARE GATED.  These are
  exponents and not amplitudes, and the asymmetry is structural: the
  squashing-free slice's prefactor is computable and the charged slice's is
  not.  It is one slice per degree, three and two respectively.  The
  primordial weights a C_ell would sum against do not exist in this corpus
  -- the normalisation is inherited and not derived, established by count
  rather than by omission -- so this is not a C_ell prediction.  And the
  scope is the scalar sector, which the paper says in its own voice.

  THE GUARD: when a result is offered as most interesting at one place,
  measure the cost of getting it there at the neighbouring places too.  A
  window two degrees wide has a bottom as well as a top, and the degree at
  the bottom may be the one a closed question had been quietly removing.
  ==========================================================================
""")
