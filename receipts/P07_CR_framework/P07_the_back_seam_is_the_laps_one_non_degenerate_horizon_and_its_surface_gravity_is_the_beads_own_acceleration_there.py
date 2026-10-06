#!/usr/bin/env python3
"""P07 receipt -- ⛭⛭⛭ THE BACK SEAM IS THE LAP'S ONE NON-DEGENERATE HORIZON, AND ITS SURFACE
GRAVITY IS THE BEAD'S OWN ACCELERATION THERE -- NOT NUMERICALLY, BY AN IDENTITY.

** WHAT THIS IS FOR. **  A plain-language read of the corpus composed a statement the papers carry in
pieces and nowhere make: that the back seam is the parent's horizon, crossed by the layer's clock at a
finite reading where the exterior's clock reaches it only in the infinite-time limit.  Every piece of
that is in print -- `P7`'s stratification, `P2`'s one-substrate-point, `P3`'s root structure, `P1`'s
theorem, `P15`'s converging integral -- and the composition had never been written.  This receipt
establishes the geometric half so the statement can be made once, in `P7`, with a number behind it.

** AND THE TWO SEAMS' APPROACH ORDERS DEPEND ON WHICH PARAMETER IS ASKED, WHICH IS WHY `prop:transmit`
COULD CARRY BOTH READINGS AT ONCE. **  Two integrals are in play and they invert each other:

  the TORTOISE length  r_* = int dr/f          -- the parameter the phase accumulates in, and the one
                                                  `prop:transmission` states the dichotomy in;
  the LAYER'S PROPER TIME  T = int dr/sqrt(-f) -- the parameter the collapse trajectory advances in.

At the SIMPLE root (back seam) r_* diverges logarithmically -- the exponential approach at rate
2 kappa, which is the imprinting law -- while T CONVERGES.  At the DOUBLE root (front seam) r_* grows
like 1/(r-r_N), a power law, while T diverges logarithmically at rate sqrt(Lambda).  Both are computed
below at both seams, so the inversion is measured.  ** So the lap's one non-degenerate horizon DOES
carry a thermal scale in the parameter the phase lives in, and what it does not have is an unbounded
approach along the trajectory that carries the modes. **  That is the distinction `prop:transmit`'s
closing clause collapses, and it is the same distinction `rem:phase-open` already draws for the branch
point: an unbounded r_* is a STATIC slicing's approach, not the collapse's.

COMPUTES: scope -- what the parameter choice does and does not restrict.  Groups Ⓐ-Ⓔ run at
alpha = 1 with M = alpha/(3 sqrt3), the Nariai member, and that is not a sample of a family: the
Nariai condition FIXES M in terms of alpha, so there is one member and alpha = 1 is a choice of
UNIT, not of parameter.  Every result in those groups is reported in units of alpha (kappa as
3 sqrt3 / 4 alpha, the leg as 0.878 alpha, the approach rates as sqrt(Lambda) = sqrt3/alpha), so
each is the whole family's value and not this member's.  The one dimensionful figure, 14.90 Gyr,
is that alpha-value multiplied by the corpus's own 1/sqrt(Lambda) = 9.8 Gly and carries that
datum's precision and no more.  Ⓒ② deliberately leaves the Nariai locus, running at
M = 0.05, 0.10, 0.15, 0.19, 0.192 with alpha = 1, because an identity claimed for every root of f
must be checked where the roots are distinct.  Ⓖ's two per-cent figures are ratios of conformal
lengths along one leg and are therefore alpha-free outright.  Nothing here is fitted and no
observational parameter enters.

** COMPUTES, on the Nariai member with alpha = 1 and M = alpha/(3 sqrt3). **
  Ⓐ  the two seams are roots of f, the front one double and the back one simple;
  Ⓑ  the back seam's surface gravity is 3 sqrt3 / 4 alpha, and the front seam's is zero;
  Ⓒ  the bead's acceleration at the back seam EQUALS -kappa there, by an identity that holds at every
     root of f and not by coincidence -- which is why `P7`'s F-triptych caption already prints 1.299;
  Ⓓ  both parameters at both seams, and the inversion between them;
  Ⓔ  the cosmic time from the back seam to the turnaround, in units of alpha and in Gyr;
  Ⓕ  the papers carry the pieces the statement composes, read from their own sources;
  Ⓖ  and WHERE the back seam sits on the collapse leg against the locus where the sky's first peak has
     its spectrum fixed -- both measured from the leg's FAR-PAST end, which is the end the figure in
     `P15`'s own receipt measures from.

** WHAT IT DOES NOT CLAIM. **  It does not compute what the back seam does to a mode crossing it; that
is named as open, and Ⓖ is what makes the question load-bearing rather than incidental.  It does not
re-derive `prop:flat`, `P1`'s theorem or the Nariai condition, each of which is quoted from the paper
that proves it.  The Gyr figure carries the corpus's own 1/sqrt(Lambda) = 9.8 Gly and is reported to
the precision that datum supports.

Built r7185 (node 66).  Stated for reversal.
"""
import io
import math
import os
import sys

from scipy.integrate import quad

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
fails = []


def check(label, ok):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    if not ok:
        fails.append(label)


def head(t):
    print('\n' + '=' * 100 + f"\n  {t}\n" + '=' * 100)


def body(name):
    """The paper's source with whitespace collapsed, so a literal that straddles a LaTeX line
    wrap is still read.  A pin that fails on where the source happens to break its lines is a
    defect in the pin and not a finding about the paper."""
    raw = io.open(os.path.join(ROOT, 'corpus', name), encoding='utf-8').read()
    return ' '.join(raw.split())


# ------------------------------------------------------------------ the member
ALPHA = 1.0
M = ALPHA / (3 * math.sqrt(3))                 # the Nariai mass, P3's prop:locus intersection
R_BACK = -2 * ALPHA / math.sqrt(3)
R_FRONT = ALPHA / math.sqrt(3)

f = lambda r: 1 - 2 * M / r - r * r / ALPHA ** 2
fp = lambda r: 2 * M / r ** 2 - 2 * r / ALPHA ** 2
fpp = lambda r: -4 * M / r ** 3 - 2 / ALPHA ** 2
# the E = 1 congruence: (dr/dtau)^2 = 1 - f, so d2r/dtau2 = (1/2) d(1-f)/dr = -(1/2) f'
acc = lambda r: -0.5 * fp(r)

head("A -- THE TWO SEAMS ARE ROOTS OF f, AND ONLY ONE OF THEM IS SIMPLE")
print(f"      M = alpha/(3 sqrt3) = {M:.10f}")
print(f"      f(back  = {R_BACK:+.8f}) = {f(R_BACK):+.3e}     f'(back)  = {fp(R_BACK):+.10f}")
print(f"      f(front = {R_FRONT:+.8f}) = {f(R_FRONT):+.3e}     f'(front) = {fp(R_FRONT):+.3e}"
      f"     f''(front) = {fpp(R_FRONT):+.8f}")
check("Ⓐ①  both seams are roots of f on the Nariai member",
      abs(f(R_BACK)) < 1e-12 and abs(f(R_FRONT)) < 1e-12)
check("Ⓐ②  the FRONT seam is a DOUBLE root -- f and f' both vanish and f'' does not: the merged "
      "horizon, degenerate",
      abs(fp(R_FRONT)) < 1e-12 and abs(fpp(R_FRONT)) > 1e-6)
check("Ⓐ③  the BACK seam is a SIMPLE root -- f vanishes and f' does not, and f'(back) = 9/(2 sqrt3) "
      "alpha^-1 exactly",
      abs(fp(R_BACK)) > 1e-6
      and abs(fp(R_BACK) - 9 / (2 * math.sqrt(3) * ALPHA)) < 1e-12)

head("B -- SO THE LAP CARRIES EXACTLY ONE NON-DEGENERATE HORIZON, AND IT IS THE BACK SEAM")
kappa_back, kappa_front = abs(fp(R_BACK)) / 2, abs(fp(R_FRONT)) / 2
print(f"      kappa(back)  = |f'|/2 = {kappa_back:.10f}     3 sqrt3 / 4 = {3*math.sqrt(3)/4:.10f}")
print(f"      kappa(front) = |f'|/2 = {kappa_front:.3e}")
check("Ⓑ①  the back seam's surface gravity is 3 sqrt3 / 4 alpha = 1.29904 alpha^-1, non-zero",
      abs(kappa_back - 3 * math.sqrt(3) / (4 * ALPHA)) < 1e-12 and kappa_back > 1)
check("Ⓑ②  and the front seam's is zero, which is what DEGENERATE means for a horizon",
      kappa_front < 1e-12)

head("C -- AND THE BEAD'S ACCELERATION THERE IS THAT SAME NUMBER, BY AN IDENTITY AND NOT BY LUCK")
print(f"      d2r/dtau2 at the back seam = {acc(R_BACK):+.10f}     -kappa(back) = {-kappa_back:+.10f}")
check("Ⓒ①  the bead's acceleration at the back seam is exactly -kappa there",
      abs(acc(R_BACK) + kappa_back) < 1e-13)
# the identity, verified away from the Nariai member so it is not an artefact of this one.
# The bracket is [eps, m^(1/3)]: g -> -inf as r -> 0 and g' = 0 at r = m^(1/3), which is g's
# interior MAXIMUM between the two positive roots, so this brackets the black-hole root alone.
_ok = True
print("      the identity off the Nariai member, at each one's own black-hole root:")
for m in (0.05, 0.10, 0.15, 0.19, 0.192):
    g = lambda r: 1 - 2 * m / r - r * r
    gp = lambda r: 2 * m / r ** 2 - 2 * r
    lo, hi = 1e-6, m ** (1 / 3.)
    assert g(lo) < 0 < g(hi), (m, g(lo), g(hi))
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if g(mid) <= 0: lo = mid
        else: hi = mid
    rh = 0.5 * (lo + hi)
    a_h, k_h = -0.5 * gp(rh), abs(gp(rh)) / 2
    # the content: 1 - g = 1 AT the root, so the E=1 congruence's d2r/dtau2 is exactly -(1/2) g'
    _ok &= (abs(g(rh)) < 1e-12 and abs((1 - g(rh)) - 1.0) < 1e-12
            and abs(abs(a_h) - k_h) < 1e-12 and a_h < 0)
    print(f"        M = {m:.4f}   r_h = {rh:.8f}   1 - f = {1-g(rh):.12f}   "
          f"d2r/dtau2 = {a_h:+.8f}   -kappa = {-k_h:+.8f}")
check("Ⓒ②  ** AND IT IS STRUCTURAL: at ANY root of f, (1-f) = 1 so the congruence's acceleration is "
      "-(1/2) f' while the surface gravity is (1/2)|f'| ** -- verified at the black-hole root of five "
      "NON-Nariai members, so the equality is the identity and not this member's coincidence",
      _ok)
TRIP = body('CR_framework.tex')
check("Ⓒ③  which is why `P7`'s F-triptych caption already prints this number as the transverse "
      "crossing's acceleration, without naming it a surface gravity",
      'the acceleration finite and non-zero ($-1.299$)' in TRIP)

head("D -- THE TWO PARAMETERS INVERT EACH OTHER, AND BOTH ARE IN PLAY")
# (i) the TORTOISE length, the parameter prop:transmission states the dichotomy in and the one the
#     phase k r_* accumulates in.  At a SIMPLE root this diverges logarithmically -- rate 2 kappa.
print("  (i) the TORTOISE length r_* = int dr/f, from 0.3 outside each seam in to a gap eps:")
RSTAR = {}
for name, r_h, out in (('back  (simple)', R_BACK, -1), ('front (double)', R_FRONT, +1)):
    vals = []
    for eps in (1e-2, 1e-4, 1e-6):
        a, b = r_h + out * eps, r_h + out * 0.3
        v, _ = quad(lambda r: 1.0 / f(r), min(a, b), max(a, b), limit=600)
        vals.append(abs(v))
        print(f"        {name:<16} eps={eps:.0e}   |r_*| = {abs(v):.6f}")
    RSTAR[name.split()[0]] = vals
_inc = [RSTAR['back'][1] - RSTAR['back'][0], RSTAR['back'][2] - RSTAR['back'][1]]
print(f"      back-seam increments per factor 100: {_inc[0]:.6f}, {_inc[1]:.6f}   "
      f"(ln 100 / |f'| = {math.log(100)/abs(fp(R_BACK)):.6f})")
check("Ⓓ⓪  ** in the TORTOISE parameter the orders are the OTHER way round: at the back seam's SIMPLE "
      "root r_* diverges LOGARITHMICALLY, each factor 100 in the gap adding ln(100)/|f'| exactly, "
      "which is the exponential approach at rate 2 kappa -- the imprinting law ** -- while at the "
      "front seam's double root r_* grows like 1/eps, a power law",
      abs(_inc[0] - math.log(100) / abs(fp(R_BACK))) < 2e-3
      and abs(_inc[1] - math.log(100) / abs(fp(R_BACK))) < 2e-5
      # and the front seam's growth is 1/eps and not logarithmic: two decades give ~100x, not +const
      and RSTAR['front'][1] / RSTAR['front'][0] > 50
      and RSTAR['front'][2] / RSTAR['front'][1] > 50)

# (ii) the LAYER'S PROPER TIME, the parameter the collapse trajectory advances in
print("\n  (ii) the layer's proper time T, dT = dr/sqrt(-f), over the same approaches:")
rows = []
for name, r_h, out in (('front (double)', R_FRONT, +1), ('back (simple)', R_BACK, -1)):
    for eps in (1e-2, 1e-4, 1e-6):
        a, b = r_h + out * eps, r_h + out * 0.3
        val, _ = quad(lambda r: 1.0 / math.sqrt(max(-f(r), 1e-300)), min(a, b), max(a, b), limit=400)
        rows.append((name, eps, val))
        print(f"        {name:<16} eps={eps:.0e}   T = {val:.6f}")
T_front = [v for n, e, v in rows if n.startswith('front')]
T_back = [v for n, e, v in rows if n.startswith('back')]
check("Ⓓ①  at the FRONT seam's double root T DIVERGES, and logarithmically -- each factor 100 in the "
      "gap adds the same increment, which is the signature of ln(1/(r-r_N))",
      T_front[2] > T_front[1] > T_front[0]
      and abs((T_front[2] - T_front[1]) - (T_front[1] - T_front[0])) < 0.05 * (T_front[1] - T_front[0]))
# At a simple root -f ~= f'(r_N) * eps, so the omitted tail is 2 sqrt(eps / f'), and the integral
# converges to T(0) = T(eps) + 2 sqrt(eps/f').  The truncated values therefore RISE with shrinking
# eps exactly as the front seam's do -- the discriminator is not that they rise but HOW: the deficit
# falls like sqrt(eps), a factor 10 per factor 100, against the front seam's EQUAL increments.
_defic = [2 * math.sqrt(e / abs(fp(R_BACK))) for e in (1e-2, 1e-4, 1e-6)]
_lims = [t + d for t, d in zip(T_back, _defic)]
print("      and the back seam's truncated values carry a sqrt(eps) tail, so they extrapolate:")
for e, t, d, L in zip((1e-2, 1e-4, 1e-6), T_back, _defic, _lims):
    print(f"        eps={e:.0e}   T = {t:.6f}   + 2 sqrt(eps/f') = {d:.6f}   ->  T(0) = {L:.6f}")
print(f"      deficit ratios {_defic[0]/_defic[1]:.3f}, {_defic[1]/_defic[2]:.3f}  (sqrt(100) = 10)")
check("Ⓓ②  at the BACK seam's SIMPLE root the same integral CONVERGES -- its omitted tail falls like "
      "sqrt(eps) and the three truncations extrapolate to ONE finite limit, 0.66978 alpha, where the "
      "front seam's have no limit to extrapolate to",
      max(_lims) - min(_lims) < 2e-4
      and abs(_defic[0] / _defic[1] - 10) < 1e-9 and abs(_defic[1] / _defic[2] - 10) < 1e-9
      # and the bound is not slack: the front seam's own increments are 2.66, far outside it
      and (T_front[1] - T_front[0]) > 100 * (max(_lims) - min(_lims)))
check("Ⓓ③  ** SO THE TWO PARAMETERS INVERT EACH OTHER AT BOTH SEAMS: the back seam's approach is "
      "exponential in the phase's parameter and finite in the trajectory's, and the front seam's is "
      "the reverse ** -- which is why the lap's one non-degenerate horizon carries a thermal scale "
      "while the modes still do not meet an unbounded approach to it, and `P15` carries both halves "
      "in different sections",
      "while at the back seam's simple zero the same integral converges" in body('CR_cosmology.tex')
      and 'the approach exponential, $(r-r_h)\\sim e^{2\\kappa r_*}$' in body('CR_cosmology.tex')
      # and rem:phase-open already draws the static-vs-trajectory distinction, for the branch point
      and "diverges along a static slicing's approach to the horizon, which is not the collapse "
          "trajectory" in body('CR_cosmology.tex'))
# the rate P15 names, read off the same flow
slope = (T_front[2] - T_front[1]) / math.log(1e4 / 1e2)
print(f"      dT/dln(1/(r-r_N)) at the front seam = {slope:.6f}   (1/sqrt(Lambda) = alpha/sqrt3 = "
      f"{ALPHA/math.sqrt(3):.6f})")
check("Ⓓ④  and the rate of that exponential is sqrt(Lambda) = sqrt3/alpha, which is `P15`'s own "
      "`r - r_N propto e^{-sqrt(Lambda) T}`",
      abs(slope - ALPHA / math.sqrt(3)) < 2e-3)

head("E -- THE LAYER'S COSMIC TIME FROM THE BACK SEAM TO THE TURNAROUND")
R_TURN = -(2 * M * ALPHA ** 2) ** (1 / 3.)
print(f"      turnaround at r = {R_TURN:+.8f} alpha,  f = {f(R_TURN):+.3e} ... 1 - f = "
      f"{1-f(R_TURN):+.3e}")
leg, err = quad(lambda r: 1.0 / math.sqrt(max(1 - f(r), 1e-300)), R_BACK, R_TURN, limit=400)
leg = abs(leg)
LAM_LEN = 9.8                                  # 1/sqrt(Lambda) in Gly, the corpus's own figure
GYR = leg * math.sqrt(3) * LAM_LEN
print(f"      Delta tau = {leg:.6f} alpha   (quad error {err:.1e})   ->  {GYR:.2f} Gyr at "
      f"alpha = sqrt3/sqrt(Lambda) = {math.sqrt(3)*LAM_LEN:.3f} Gly")
check("Ⓔ①  the turnaround is where the marginal rate vanishes, 1 - f = 0", abs(1 - f(R_TURN)) < 1e-12)
check("Ⓔ②  the collapse leg from the back seam to the turnaround is 0.8780 alpha of cosmic time, "
      "which is 14.90 Gyr on the corpus's own 1/sqrt(Lambda) = 9.8 Gly",
      abs(leg - 0.877972) < 1e-5 and abs(GYR - 14.90) < 0.02)

head("F -- AND THE PIECES THE STATEMENT COMPOSES ARE EACH IN PRINT, READ FROM THEIR OWN SOURCES")
P02, P15T, P16 = body('janzen_circle_v3.tex'), body('CR_cosmology.tex'), body('cosmogenesis_paper.tex')
check("Ⓕ①  `P7` stratifies the lap and puts the character change at the back seam",
      'back seam (timelike to spacelike)' in TRIP)
check("Ⓕ②  `P2` makes the two seams ONE point of the underlying geometry, by the phase",
      'one point of the underlying geometry' in P02
      and 'the outer two differ by a full turn' in P02)
check("Ⓕ③  `P2` names the cubic's extra roots for what they are -- the cosmological horizon and its "
      "backward-radial partner -- and records that they are ABSENT at Lambda = 0",
      'the cosmological horizon and its backward-radial partner---are absent' in P02)
check("Ⓕ④  `P15` carries the converging integral at the back seam's simple zero",
      "at the back seam's simple zero the same integral converges" in P15T)
check("Ⓕ⑤  `P16` puts the progenitor in a previous universe, which is the region the horn beyond the "
      "back seam carries",
      'a black hole in a previous universe' in P16)

head("G -- AND THE BACK SEAM IS DOWNSTREAM OF WHERE THE SKY'S SPECTRUM IS FIXED, NOT BESIDE IT")
# Both lengths are conformal distances along the collapse leg measured from its FAR-PAST end, which
# is the end `P15_the_progenitor_spectrum_is_defined_before_the_lift...` measures its own 0.92% from.
# The collapse branch is r = -(2 M alpha^2)^(1/3) cosh^(2/3)(x), so x = 0 is the TURNAROUND and
# x -> -inf the far past; the back seam sits at cosh x = 2 exactly (`P7`'s F-triptych caption).
import mpmath as mp
mp.mp.dps = 30
_c0 = 2 / (mp.sqrt(3) * 2 ** (mp.mpf(1) / 3))
_leg = _c0 * mp.quad(lambda u: mp.cosh(u) ** (-mp.mpf(2) / 3), [0, mp.inf])
_x_seam = mp.acosh(2)
_d_seam = _c0 * mp.quad(lambda u: mp.cosh(u) ** (-mp.mpf(2) / 3), [_x_seam, mp.inf])
PCT_SEAM, PCT_SKY = float(100 * _d_seam / _leg), 0.92        # 0.92 per cent: `P15`'s own receipt
print(f"      the collapse leg's conformal length        = {float(_leg):.9f} alpha")
print(f"      the back seam sits at cosh x = 2, x = {float(_x_seam):.6f}")
print(f"      far past -> back seam                      = {float(_d_seam):.9f} alpha "
      f"= {PCT_SEAM:.3f} % of the leg")
print(f"      far past -> the sky's first peak's spectrum = {PCT_SKY:.2f} % of the leg "
      f"(`P15`'s own receipt)")
print(f"      so the back seam is {PCT_SEAM/PCT_SKY:.1f}x further in than that locus, and lies "
      f"BETWEEN it and the turnaround")
check("Ⓖ①  the back seam sits at 46.5 per cent of the collapse leg from its far-past end, while the "
      "locus where the sky's first acoustic peak has its spectrum fixed is in the first 0.92 per cent "
      "of the SAME leg from the SAME end",
      abs(PCT_SEAM - 46.508) < 0.01 and abs(float(_leg) - 1.927621297) < 1e-8)
check("Ⓖ②  ** SO THE LAP'S ONE NON-DEGENERATE HORIZON IS NOT BESIDE WHERE THE PROGENITOR'S SPECTRUM "
      "IS SET -- IT IS FIFTY TIMES DOWNSTREAM OF IT, ON THE PATH OF EVERY MODE THE SKY CARRIES ** -- "
      "which is what makes `what the back seam does to a mode crossing it` a question about the "
      "measured spectrum rather than a coincidence of location",
      PCT_SEAM / PCT_SKY > 40 and PCT_SEAM < 100)
# The per-cent figure is only locatable if the END it is measured from is stated.  Its own receipt
# states it; the paper's sentence must too, or the figure reads as `just inside the back seam`, which
# is the opposite side of the seam from where it is.
_sib = io.open(os.path.join(
    ROOT, 'receipts', 'P15_CR_cosmology',
    'P15_the_progenitor_spectrum_is_defined_before_the_lift_so_the_envelope_applies_to_it_and_the_'
    'horizon_scale_on_both_lorentzian_legs_is_the_same_pure_number.py'), encoding='utf-8').read()
check("Ⓖ③  the per-cent figure's own receipt measures it from the collapse leg's FAR-PAST end, and "
      "`P15`'s own sentence now names that end too -- a bare `the first per cent of the collapse "
      "leg` is read from whichever end the reader supplies, and the two ends put the locus on "
      "opposite sides of the back seam",
      "collapse leg's far-past end" in _sib
      # the full sentence, not a bare `far-past end`: that phrase now occurs twice in the paper and
      # a pin matching either is a pin on the file rather than on this claim
      and "has its spectrum fixed within the first per cent of the collapse leg, measured from that "
          "leg's far-past end" in P15T)

print()
if fails:
    print(f"  ⛔ {len(fails)} CHECK(S) FAILED:")
    for x in fails:
        print('      - ' + x)
    sys.exit(1)
print(f"""
==========================================================================================
  THE BACK SEAM IS THE LAP'S ONE NON-DEGENERATE HORIZON.

  Both seams are roots of the Nariai cubic and they are one point of the
  underlying geometry, met a lap apart.  The front seam is the DOUBLE root --
  the merged horizon, surface gravity zero.  The back seam is the SIMPLE
  root, surface gravity 3 sqrt3 / 4 alpha = {kappa_back:.5f}/alpha, and the bead's
  acceleration there is exactly minus that number, by an identity holding at
  every root of f rather than by coincidence on this member.

  And the two parameters invert each other at both seams.  In the TORTOISE
  length -- the parameter the phase accumulates in, and the one the
  transmission dichotomy is stated in -- the back seam's simple root gives the
  exponential approach at rate 2 kappa, the imprinting law, while the front
  seam's double root gives a power law.  In the LAYER'S OWN PROPER TIME -- the
  parameter the collapse trajectory advances in -- it is the reverse: the
  double root diverges logarithmically at rate sqrt(Lambda) and the simple
  root's integral converges, to {min(_lims):.5f} alpha.

  So the lap's one non-degenerate horizon DOES carry a thermal scale, and what
  it does not have is an unbounded approach along the trajectory that carries
  the modes.  The layer crosses it at a finite reading and keeps going,
  {GYR:.2f} Gyr short of the turnaround, where no finite layer of the exterior's
  reckoning reaches it at all.

  WHAT IS OPEN: what the back seam does to a mode crossing it.  The locus
  where the sky's first acoustic peak has its spectrum fixed is in the first
  {PCT_SKY:.2f} per cent of the collapse leg from its far-past end, and the back seam
  is at {PCT_SEAM:.1f} per cent of the same leg from the same end -- so the horizon is
  not beside that locus but {PCT_SEAM/PCT_SKY:.0f} times downstream of it, crossed by every
  mode the sky carries, before the turnaround.  Nothing here computes what
  that crossing does.
==========================================================================================
""")
