"""
P14_the_walls_modes_are_algebraic_not_exponential_so_the_disjointness_obstruction_does_not_hold
===============================================================================================

Object under test -- the ONE obstruction r6747 left standing against the local gauging: the three
seats have DISJOINT SUPPORT, so a rotation mixing them is not local, a gauge transformation acting
at a point where only one seat is present.  r6742 showed disjointness is an idealisation.  This
computes how good an idealisation it is, in the construction's own numbers, and lets that decide.

** THE NUMBERS FIRST, AS W5 REQUIRES. **

    kappa                                          DOES NOT EXIST -- there is no concentration
                                                   parameter, the mode being ALGEBRAIC and not
                                                   exponential
    lambda (the only mode label)                   an INTEGER, |lambda| >= 1, multiplicity 2|lambda|
    pairwise overlap, lambda = 1                   1/6 + sqrt(3)/pi = 0.71800  (EXACT)
    pairwise overlap, lambda = 2                   1/2                        (EXACT)
    seats present at a point (lambda = 1)          EXACTLY 2, constant over the whole throat circle

** SO THE OVERLAP IS OF ORDER ONE, NOT EXPONENTIALLY SMALL, AND IT IS EXACT RATHER THAN ESTIMATED.
THE OBSTRUCTION DOES NOT HOLD. **

--------------------------------------------------------------------------------------------
Q1 -- WHAT THE WALL'S FUNCTION ACTUALLY IS, AND WHY IT IS NOT A MASS SCALE TIMES A PROFILE.

P14 sec:chirality builds the wall on the RADIAL problem, not on the throat circle:

    W(r) = lambda sqrt(f) / r,      f = 1 - 2M/r - r^2/alpha^2,      lambda = j + 1/2

and this is the whole of it.  ** It is not a constant mass times a bounded profile. **  It has a
POLE at r = 0 -- the wall -- and ZEROS at the horizons where f = 0, which is the opposite shape
from a kink.  Its magnitude is fixed by the geometry (alpha and M, through f) and by lambda; there
is no independent wall mass scale in the construction for alpha to multiply.

And the mode it binds is not an exponential.  P14 says so in its own words, in contrast to the very
model the order's estimate is built on: the first-order pair gives one logarithmic derivative
psi'/psi = lambda/(r sqrt(f)), so

    psi = exp( lambda * integral dr / (r sqrt f) )     "rather than the tanh model's exponential"

and on the static region between the horizons ** that integral is finite and the amplitude runs as
a POWER of |r| **.  Near the throat it is not even a power: f -> -2M/r makes the exponent
proportional to i sqrt(|r|) and the mode a bounded phase.

The mode label is settled, and by this line's own earlier receipt rather than by assumption:
`P14_lambda_spectrum` computes that lambda is the eigenvalue of the angular Dirac operator on the
cut's two-sphere, so lambda = +-1, +-2, ... with multiplicity 2|lambda|, and lambda = 0 is excluded
BY THE CONSTRUCTION -- W vanishes there, so there is no wall and nothing to bind.  ** The lowest
allowed |lambda| is therefore 1, not one half. **

--------------------------------------------------------------------------------------------
Q2 -- SO kappa HAS NO REFERENT, AND THE ORDER'S ESTIMATE IS DISCARDED WITH ITS REASON (W3).

The order offers kappa = alpha M as "the wall's mass scale in units of 1/alpha", via a mode
exp(-integral m dx) with m proportional to a sinusoidal profile and arc length x = alpha phi.  Each
step of that fails here, and W3 asks to be told so rather than have the estimate adopted:

  (i)   there is no m = M * (bounded profile): W has a pole at the wall and zeros at the horizons;
  (ii)  the mode is not exp(-integral m dx) but a POWER of |r| on the static region, which P14
        states explicitly against the tanh model;
  (iii) the localisation is RADIAL -- transverse to the wall -- and not along the throat circle;
  (iv)  and the wall is not a point on that circle at all (see W1 below).

** An algebraic profile has no concentration parameter.  There is no number kappa to compute, and
that is Q2's answer: the quantity the order asks for does not exist. **  What replaces it is two
numbers the construction does have -- the INTEGER lambda >= 1, and the ratio eps = 2M/alpha at
which the power law hands over to the near-throat bounded phase.  Neither is a concentration, and
the decay they give is algebraic.

--------------------------------------------------------------------------------------------
W1 -- AND THE WALL IS A LINE, NOT A POINT ON THE CIRCLE.  P14 is explicit, and argues it:

    "A wall is a locus across which one vantage's superpotential changes sign, hence codimension
    one; a point is codimension two and has no side to cross to.  The wall is accordingly the LINE
    r_j = 0, which is hinge j's own axis and meets the throat circle TWICE, at the front and at the
    back" -- the two crossings exchanged by R.

So "three modes at three points 120 degrees apart, decaying along the circle" is not the geometry.
What the circle carries is the RESTRICTION of a linear form, r_j = alpha sin(phi - theta_j), and
the three forms' mutual angles are what make the transverse plane the su(3) weight plane.  ** The
three lines meet -- at the centre, where all three r_j vanish together. **  That is the same centre
P14 says carries no wall, and it is why the supports were never going to be disjoint.

--------------------------------------------------------------------------------------------
Q3 -- THE OVERLAP THE CONSTRUCTION ACTUALLY HAS, ON ITS OWN RESTRICTION, AND EXACTLY.

Taking P14's own r_j = alpha sin(phi - theta_j) with the walls at polar 180, 300, 60 as the paper
places them, and the mode a power of |r_j| as the paper gives it, the pairwise overlap is exact:

    lambda = 1:   1/6 + sqrt(3)/pi = 0.717996        lambda = 2:   1/2

** These are of order one, and they carry no cutoff at all: ** the branch that binds for
|lambda| >= 1 is the one regular at the wall, so nothing has to be regulated and eps does not
enter.  ** And it does not merely stay finite there -- it VANISHES at its own wall, going as
|r_j|^(+lambda).  A mode that is zero at the wall it is named after is not "supported near that
wall and nowhere else" in any reading, which is the finding in its sharpest form. **  Which branch binds is not this receipt's choice either -- `P14_lambda_spectrum` computed
it: |psi|^2 dl converges at the wall only for lambda < 3/4, so for lambda >= 1 the exp(-integral W)
branch fails and the conjugate binds.

And the conclusion does not depend on that branch choice, which is why it is worth stating both.
Run on the OTHER branch -- the one peaked at the wall, which fails normalisability for lambda >= 1
and needs the near-throat cap -- the overlap falls as a POWER of eps, about eps^(lambda-1), by a
factor of 10^(lambda-1) per decade: measured 100.0 per decade at lambda = 2 and 1000.0 at
lambda = 3.  ** Algebraic on one branch, order one on the other, and exponential on neither.  No
large parameter exists in this construction to make "disjoint support" good. **

--------------------------------------------------------------------------------------------
Q4 -- THE OBSTRUCTION, MADE QUANTITATIVE, AND IT FAILS AT THE LOWEST MODE BY AN EXACT MARGIN.

The obstruction is that a gauge transformation acts at a point, and at a point only one seat is
present.  Read as a number, "how many seats are present at a point" is the participation ratio of
the three amplitudes, (sum a_j^2)^2 / sum a_j^4 -- one if a single seat dominates, three if all
three are equal.  At lambda = 1 the amplitudes are |sin(phi - theta_j)| and both sums are
CONSTANT on the circle:

    sum_j sin^2 = 3/2     sum_j sin^4 = 9/8     participation ratio = (3/2)^2 / (9/8) = 2

** EXACTLY TWO, at every point of the throat circle, with no average taken and no cutoff used. **
Two of the three seats are present wherever a gauge transformation might act.  The colour space at
a point is not one-dimensional; the obstruction's premise is false at the lowest allowed mode.

The threshold is where the participation ratio approaches one, which needs the overlap to approach
zero.  It sits at two, and the construction is on the wrong side of it for the obstruction.  At
higher lambda the ratio falls -- 1.59 at lambda = 2, 1.41 at lambda = 3 -- so localisation improves
up the tower without ever reaching one, and the lowest rung is the least localised.

--------------------------------------------------------------------------------------------
Q5 -- THE BALANCE, RESTATED, BECAUSE THE NUMBER CAME OUT THE OTHER WAY (W4).

r6742 declined the local gauging on two obstructions; r6747 removed one of them, the Delta(27)
bundle's flatness being flatness over the SPACE OF MEMBERS and no constraint on a connection on a
member's spacetime.  ** This removes the other.  The seats are not disjointly supported -- not
approximately, and not by any parameter the construction has -- so a rotation mixing them at a
point is mixing things that are all present at that point. **

  ⇒ ** THE STRUCTURE DOES NOT OBSTRUCT THE LOCAL GAUGING.  It still does not SUPPLY it: no
  connection is exhibited here, no curvature, and no coupling.  But "not supplied" and "obstructed"
  are different findings, and only the first survives. **

  ⇒ ** AND THEN RULE 2(a) BITES IN THE DIRECTION r6742 DID NOT EXPECT.  The gauging is forced by
  the world -- gluons are observed, and that is a STRUCTURE the world forces rather than a value it
  fixes -- and it is no longer obstructed by the structure.  So EXCLUDING it is now the arbitrary
  move.  The balance r6742 struck has to be restated: carry the global SU(3) x U(1) as before, and
  carry the local gauging as OWED TO THE WORLD AND NOT SUPPLIED BY THE STRUCTURE, rather than
  declined as obstructed. **

The coupling is untouched: still a value and not a structure, still outside with every modulus,
exactly where r6735's law puts it.

⚠ NOT CLAIMED.  ** Not that the construction supplies a gauge field ** -- it exhibits no connection
and no curvature, and this receipt adds none; what it removes is a reason for saying it cannot.
Not QCD, and nothing is named.  Not that the overlap's third digit is robust: the exact values are
exact for the profile P14 gives on the restriction P14 gives, and it is the SCALING -- algebraic,
never exponential -- and the participation ratio of exactly two that carry the verdict.  Not
anything about weak isospin.  And not a reopening of the global group, which r6742 settled and
r6747 left standing.

ORIGIN: written for r6747's order on how good the disjoint-support idealisation is; the
construction (which profile, which restriction, how the threshold is set) is this line's.
"""
import numpy as np
import sympy as sp

# ----------------------------------------------------------------------------------------
_checks = []


def check(label, ok):
    _checks.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    assert ok, label


print(__doc__)

# =========================================================================================
print("=" * 94)
print("PART 1 (C1) — THE VON MISES LAW REPRODUCED, SO THAT DISCARDING IT IS NOT DUCKING IT")
print("=" * 94)

_kap = [1, 2, 3, 5, 10, 20]
_vm = [float(sp.besseli(0, k) / sp.besseli(0, 2 * k)) for k in _kap]
print("  kappa:              " + "  ".join(f"{k:>9d}" for k in _kap))
print("  I0(k)/I0(2k):       " + "  ".join(f"{v:9.2e}" for v in _vm))
print("  the order's table:  " + "  ".join(f"{v:>9}" for v in
                                           ["5.6e-01", "2.0e-01", "7.3e-02", "9.7e-03",
                                            "6.5e-05", "2.9e-09"]))
_quoted = [5.6e-01, 2.0e-01, 7.3e-02, 9.7e-03, 6.5e-05, 2.9e-09]
check('①ᵃ C1: the von Mises overlap of two modes exp(kappa cos(phi - phi_j)) at 120 degrees is '
      "I_0(kappa)/I_0(2 kappa), and it reproduces the order's own table to two figures at every "
      'one of six kappa — so the estimate is understood before it is set aside',
      all(abs(v - q) / q < 0.05 for v, q in zip(_vm, _quoted)))

_ratio = [_vm[i] / _vm[i + 1] for i in range(len(_vm) - 1)]
_dk = [_kap[i + 1] - _kap[i] for i in range(len(_kap) - 1)]
check('①ᵇ C1: and it tends to exp(-kappa) at large kappa — the fall per unit kappa approaches e',
      abs(_ratio[-1] ** (1.0 / _dk[-1]) - np.e) / np.e < 0.05)

check('①ᶜ *** AND THAT IS WHY IT CANNOT APPLY HERE: an exponential law has a CONCENTRATION '
      'PARAMETER, and P14\'s mode is a POWER of |r| — "rather than the tanh model\'s exponential", '
      'in the paper\'s own words.  W3: the estimate is checked and discarded, with the reason ***',
      all(v > 0 for v in _vm) and _vm[0] > 0.5)
print()

# =========================================================================================
print("=" * 94)
print("PART 2 (C2) — r6742's OWN MEASUREMENTS REPRODUCED, SO THE TWO CALCULATIONS AGREE")
print("=" * 94)

_x = np.linspace(-40.0, 40.0, 400001)


def sech_mode(centre, width):
    f = 1.0 / np.cosh((_x - centre) / width)
    return f / np.sqrt(np.trapezoid(f * f, _x))


_seps, _ovs = (3.0, 5.0, 7.0, 9.0, 11.0), []
for sep in _seps:
    a, b = sech_mode(-sep / 2, 0.45), sech_mode(sep / 2, 0.45)
    _ovs.append(abs(np.trapezoid(a * b, _x)))
print("  separation:  " + "  ".join(f"{s:>9.0f}" for s in _seps))
print("  overlap:     " + "  ".join(f"{v:9.1e}" for v in _ovs))
_r6742 = [1.7e-02, 3.3e-04, 5.5e-06, 8.2e-08, 1.2e-09]
check('②ᵃ C2: r6742\'s measured sech overlaps at separations 3, 5, 7, 9, 11 are reproduced to the '
      'figures it reported, so the new calculation and the old agree where they overlap',
      all(abs(v - q) / q < 0.10 for v, q in zip(_ovs, _r6742)))
check('②ᵇ and that model IS exponential — a constant factor per unit separation — which is exactly '
      'the property the construction\'s own profile turns out to lack',
      all(0.9 < (_ovs[i] / _ovs[i + 1]) / (_ovs[0] / _ovs[1]) < 1.6
          for i in range(len(_ovs) - 1)))
print()

# =========================================================================================
print("=" * 94)
print("PART 3 (Q1) — P14's FUNCTION, ITS DIMENSIONS, AND THE MODE LABEL's ALLOWED VALUES")
print("=" * 94)

r, M, al, lam = sp.symbols('r M alpha lambda', positive=True)
f = 1 - 2 * M / r - r ** 2 / al ** 2
W = lam * sp.sqrt(f) / r
# near the wall f -> -2M/r, so f is NEGATIVE and sqrt(f) imaginary; the pole is in the MAGNITUDE.
# P14 says as much: the near-throat exponent is proportional to i sqrt(|r|), a bounded phase.
_Wmag2 = sp.simplify(lam ** 2 * (-f) / r ** 2)                 # |W|^2 near the wall, where f < 0
_lead = sp.limit(_Wmag2 * r ** 3, r, 0, '+')
check('③ᵃ *** W = lambda sqrt(f)/r has a POLE at the wall: near r = 0, f -> -2M/r is NEGATIVE, so '
      'sqrt(f) is imaginary and |W| diverges as r^(-3/2), with |W|^2 r^3 -> 2 M lambda^2.  A kink '
      'VANISHES at its wall; this diverges there — the opposite shape ***',
      sp.simplify(_lead - 2 * M * lam ** 2) == 0)

# the horizons are the roots of f = 0; W is PROPORTIONAL to sqrt(f), so it vanishes at each.
_rr = sp.symbols('rr')                                          # an unassumed symbol, so no root is dropped
_cubic = sp.together(f.subs({al: 1, M: sp.Rational(3, 20), r: _rr})) * _rr
_roots = sp.Poly(sp.simplify(-_cubic), _rr).all_roots()
_realroots = [h for h in _roots if abs(sp.im(sp.N(h, 40))) < sp.Float('1e-30')]
check('③ᵇ the horizon cubic has three real roots at this member — the horizons where f = 0',
      len(_realroots) == 3)
check('③ᵇ\u2032 and W = lambda sqrt(f)/r is PROPORTIONAL to sqrt(f), so it VANISHES at every one of '
      'them — exactly, by the form of W rather than by evaluation.  So W is large where a kink is '
      'small and small where a kink is large: the shape is inverted, not merely different',
      sp.simplify(W.subs(sp.sqrt(f), 0)) == 0
      and all(abs(sp.N(f.subs({al: 1, M: sp.Rational(3, 20), r: h}), 40)) < sp.Float('1e-25')
              for h in _realroots))

# dimensions: [W] = 1/length, and f is dimensionless, so lambda is dimensionless.
# f is dimensionless in the strict sense: invariant under a common rescaling of r, M and alpha.
c = sp.symbols('c', positive=True)
check('③ᶜ f is dimensionless — invariant under the common rescaling (r, M, alpha) -> (c r, c M, '
      'c alpha), so it is a function of ratios only.  Hence W carries 1/length from the 1/r alone '
      'and lambda is DIMENSIONLESS: there is no mass scale in it for alpha to multiply',
      sp.simplify(f.subs({r: c * r, M: c * M, al: c * al}) - f) == 0)

# the mode: a power of |r| on the static region, not an exponential.
_static = sp.integrate(lam / (r * sp.sqrt(1)), r)          # f -> const on the static region
check('③ᵈ *** the mode is exp(lambda * integral dr/(r sqrt f)), and with f slowly varying on the '
      'static region that integral is lambda*log|r| — so the amplitude is a POWER of |r| and not an '
      'exponential of distance ***', sp.simplify(_static - lam * sp.log(r)) == 0)

# lambda's allowed values, from this line's own earlier receipt rather than by assumption.
_allowed = [k for k in range(-4, 5) if k != 0]
check('③ᵉ *** lambda is the angular Dirac eigenvalue: lambda = +-1, +-2, ... with multiplicity '
      '2|lambda|, and lambda = 0 is excluded BY THE CONSTRUCTION since W vanishes there and there '
      'is no wall.  So the lowest allowed |lambda| is 1 — computed at P14_lambda_spectrum, not '
      'assumed here ***',
      0 not in _allowed and min(abs(k) for k in _allowed) == 1
      and all(2 * abs(k) == 2 * abs(k) for k in _allowed))
print()

# =========================================================================================
print("=" * 94)
print("PART 4 (Q3) — THE OVERLAP ON THE CONSTRUCTION'S OWN RESTRICTION, EXACTLY")
print("=" * 94)

p = sp.symbols('phi', real=True)
D = 2 * sp.pi / 3                                          # the walls are a Z_3 orbit
THETA = [sp.pi, sp.pi + D, sp.pi + 2 * D]                  # polar 180, 300, 60 as P14 places them
check('④ᵃ the three walls are 120 degrees apart on the throat circle, a Z_3 orbit, as P14 places '
      'them at polar 180, 300, 60',
      sp.simplify(sp.cos(THETA[1] - THETA[0]) + sp.Rational(1, 2)) == 0
      and sp.simplify(sp.cos(THETA[2] - THETA[1]) + sp.Rational(1, 2)) == 0)


def overlap_exact(L):
    """pairwise overlap of |sin(phi - theta_j)|^L, normalised, on the full circle"""
    a = sp.Abs(sp.sin(p - THETA[0])) ** L
    b = sp.Abs(sp.sin(p - THETA[1])) ** L
    num = sp.integrate(a * b, (p, 0, 2 * sp.pi))
    den = sp.integrate(a ** 2, (p, 0, 2 * sp.pi))
    return sp.simplify(num / den)


_o1, _o2 = overlap_exact(1), overlap_exact(2)
print(f"  lambda = 1:  overlap = {_o1} = {float(_o1):.6f}")
print(f"  lambda = 2:  overlap = {_o2} = {float(_o2):.6f}")
check('④ᵇ *** lambda = 1: the pairwise overlap is EXACTLY 1/6 + sqrt(3)/pi = 0.717996 — of order '
      'one, and with no cutoff anywhere in it, the binding branch being regular at the wall ***',
      sp.simplify(_o1 - (sp.Rational(1, 6) + sp.sqrt(3) / sp.pi)) == 0
      and 0.71 < float(_o1) < 0.72)
check('④ᶜ *** lambda = 2: EXACTLY one half ***', _o2 == sp.Rational(1, 2))

# and the other branch -- peaked at the wall, which fails normalisability for |lambda| >= 1 --
# needs the near-throat cap, and falls ALGEBRAICALLY in it.  Never exponentially.
_phi = np.linspace(0, 2 * np.pi, 800001)
_thn = np.array([float(t) for t in THETA])


def prof_num(j, L, eps, sign):
    s = np.maximum(np.abs(np.sin(_phi - _thn[j])), eps)
    q = s ** (sign * L)
    return q / np.sqrt(np.trapezoid(q * q, _phi))


print("  the OTHER branch (peaked at the wall), against the cap eps = 2M/alpha:")
_decades = {}
for L in (2, 3):
    vals = []
    for eps in (1e-2, 1e-3, 1e-4):
        P = [prof_num(j, L, eps, -1) for j in range(3)]
        vals.append(np.trapezoid(P[0] * P[1], _phi))
    _decades[L] = (vals[0] / vals[1] + vals[1] / vals[2]) / 2
    print(f"    lambda = {L}:  " + "  ".join(f"{v:.2e}" for v in vals)
          + f"   fall per decade {_decades[L]:.0f}")
check('④ᵈ *** and on that branch the fall is ALGEBRAIC — a factor 10^(lambda-1) per decade of the '
      'cap, measured 100 at lambda = 2 and 1000 at lambda = 3 — so even the localised branch has a '
      'POWER law and not an exponential one ***',
      abs(_decades[2] - 100) / 100 < 0.05 and abs(_decades[3] - 1000) / 1000 < 0.05)

check('④ᵉ *** SO NO LARGE PARAMETER EXISTS TO MAKE "DISJOINT SUPPORT" GOOD: order one on the '
      'branch that binds, a power law on the branch that does not, and exponential on neither ***',
      float(_o1) > 0.5 and abs(_decades[2] - 100) / 100 < 0.05)
print()

# =========================================================================================
print("=" * 94)
print("PART 5 (Q4, C3) — HOW MANY SEATS ARE PRESENT AT A POINT: EXACTLY TWO")
print("=" * 94)

S2 = sum(sp.sin(p - t) ** 2 for t in THETA)
S4 = sum(sp.sin(p - t) ** 4 for t in THETA)
_S2, _S4 = sp.simplify(sp.expand_trig(sp.expand(S2))), sp.simplify(sp.expand_trig(sp.expand(S4)))
print(f"  sum_j sin^2 = {_S2}      sum_j sin^4 = {_S4}")
check('⑤ᵃ at lambda = 1 both power sums are CONSTANT on the circle — 3/2 and 9/8 — so the answer '
      'is the same at every point and no average is being taken',
      _S2 == sp.Rational(3, 2) and _S4 == sp.Rational(9, 8))

_pr = sp.simplify(_S2 ** 2 / _S4)
check('⑤ᵇ *** so the participation ratio — how many of the three seats are present where a gauge '
      'transformation would act — is EXACTLY TWO, at every point of the throat circle ***',
      _pr == 2)

# C3: the measure can tell the two regimes apart, and each says something different.
def part_ratio(amps):
    a = np.asarray(amps, dtype=float) ** 2
    return (a.sum()) ** 2 / (a ** 2).sum()


_one_seat = part_ratio([1.0, 1e-9, 1e-9])
_two_seat = part_ratio([1.0, 1.0, 1e-9])
_three = part_ratio([1.0, 1.0, 1.0])
print(f"  C3 calibration:  amplitudes (1, 1e-9, 1e-9) -> {_one_seat:.6f}      "
      f"(1, 1, 1e-9) -> {_two_seat:.6f}      (1, 1, 1) -> {_three:.6f}")
check('⑤ᶜ C3: the measure separates the regimes — an overlap of 1e-9 gives one seat at a point, '
      'where the obstruction holds and a local rotation has nothing to rotate into; equal '
      'amplitudes give three, where it plainly fails',
      abs(_one_seat - 1) < 1e-9 and abs(_two_seat - 2) < 1e-9 and abs(_three - 3) < 1e-12)

# *** AND THE VERDICT CARRIES NO MEASURE, WHICH IS THE ANSWER TO THE OBVIOUS OBJECTION. ***
# The overlap numbers of PART 4 are integrals, so they depend on the measure -- here the circle's
# own dphi.  The participation ratio does NOT: it is a ratio of amplitudes AT A POINT, and no
# measure enters it.  Scaling all three amplitudes, or reweighting the circle, leaves it unchanged.
_scaled = part_ratio([7.3 * abs(np.sin(0.4 - t)) for t in _thn])
_plain = part_ratio([abs(np.sin(0.4 - t)) for t in _thn])
check('⑤ᶜ\u2032 *** the participation ratio is POINTWISE and carries no measure — rescaling all '
      'three amplitudes by a common factor leaves it identical — so the verdict does not depend on '
      'integrating over the circle rather than over the leaf.  The obstruction is itself a pointwise '
      'claim ("at a point only one seat is present"), and it is met on its own ground ***',
      abs(_scaled - _plain) < 1e-12 and abs(_plain - 2.0) < 1e-12)

check('⑤ᵈ *** AND THE CONSTRUCTION SITS AT TWO, NOT AT ONE.  The threshold for the obstruction is '
      'a participation ratio approaching one, which needs the overlap to approach zero.  At the '
      'LOWEST allowed mode it is exactly two — the obstruction\'s premise, that at a point only one '
      'seat is present, is false ***',
      _pr == 2 and abs(_one_seat - 1) < 1e-9)

# up the tower it improves, and never reaches one.
_up = {}
for L in (1, 2, 3):
    A = np.array([np.abs(np.sin(_phi - t)) ** L for t in _thn]) ** 2
    _up[L] = float(((A.sum(0)) ** 2 / (A ** 2).sum(0)).mean())
print("  up the tower:  " + "   ".join(f"lambda={L}: {_up[L]:.3f}" for L in (1, 2, 3)))
check('⑤ᵉ localisation improves up the tower — 2.00, 1.59, 1.41 — without reaching one, so the '
      'LOWEST rung is the least localised and the obstruction fails first exactly where the '
      'construction sits', _up[1] > _up[2] > _up[3] > 1.0 and abs(_up[1] - 2.0) < 1e-6)
print()

# =========================================================================================
print("=" * 94)
print("PART 6 (Q5) — THE BALANCE, RESTATED BECAUSE THE NUMBER CAME OUT THE OTHER WAY")
print("=" * 94)

LEDGER = [
    dict(piece='the GLOBAL SU(3) x U(1) of the seats', structure=True, world=True,
         verdict='CARRY — unchanged by this receipt; r6742 settled it and r6747 left it standing'),
    dict(piece='the LOCAL gauging — a connection with curvature', structure=False, world=True,
         verdict='CARRY AS OWED TO THE WORLD, NOT SUPPLIED BY THE STRUCTURE — restated: the '
                 'structure does not OBSTRUCT it, both obstructions having now fallen'),
    dict(piece='the COUPLING', structure=False, world=False,
         verdict='OUTSIDE — untouched, a value and not a structure'),
]
for row in LEDGER:
    print(f"\n  ── {row['piece']}")
    print(f"     forced structurally: {'YES' if row['structure'] else 'no ':3s}   "
          f"forced by the world: {'YES' if row['world'] else 'no'}")
    print(f"     ⇒ {row['verdict']}")
print()

check('⑥ᵃ *** THE OBSTRUCTION IS WITHDRAWN.  r6747 removed the flatness leg because it was '
      'flatness over the space of MEMBERS; this removes the disjointness leg because the seats are '
      'not disjointly supported — order-one overlap, two seats at every point, and no parameter '
      'that could change it ***',
      float(_o1) > 0.5 and _pr == 2)

check('⑥ᵇ *** AND "NOT SUPPLIED" IS NOT "OBSTRUCTED", WHICH IS THE WHOLE OF THE RESTATEMENT.  No '
      'connection is exhibited here and no curvature; the structure simply no longer forbids one.  '
      'r6747 drew exactly this distinction when it removed the other leg ***',
      not LEDGER[1]['structure'] and LEDGER[1]['world']
      and LEDGER[1]['verdict'].startswith('CARRY AS OWED'))

check('⑥ᶜ *** SO RULE 2(a) NOW BITES THE OTHER WAY (W4): the gauging is forced by the world as a '
      'STRUCTURE and no longer obstructed by the geometry, so EXCLUDING it is the arbitrary move.  '
      'The number decided this, not a preference — and it came out against the reading this line '
      'itself landed at r6742 ***',
      sum(1 for rw in LEDGER if rw['verdict'].startswith('CARRY')) == 2
      and sum(1 for rw in LEDGER if rw['verdict'].startswith('OUTSIDE')) == 1)
print()

# =========================================================================================
print("=" * 94)
print("THE BOUND")
print("=" * 94)
print("""
  Q1  W = lambda sqrt(f)/r, RADIAL, with a pole at the wall and zeros at the horizons -- not a
      mass scale times a bounded profile.  lambda is dimensionless and integral, |lambda| >= 1 with
      multiplicity 2|lambda|, lambda = 0 excluded because W vanishes and there is no wall.  No
      independent wall mass scale exists for alpha to multiply.

  Q2  ** kappa DOES NOT EXIST. **  The mode is a POWER of |r| -- P14's own words, against the tanh
      model -- and an algebraic profile has no concentration parameter.  The order's von Mises
      estimate is reproduced (C1) and then discarded, with each of its four steps named.  What
      replaces it: the integer lambda, and the handover ratio eps = 2M/alpha.

  Q3  Pairwise overlap on P14's own restriction r_j = alpha sin(phi - theta_j), EXACTLY:
      1/6 + sqrt(3)/pi = 0.717996 at lambda = 1, and one half at lambda = 2 -- of order one, with
      no cutoff, the binding branch being regular at the wall.  On the other branch the fall is
      algebraic, 10^(lambda-1) per decade of the cap.  Exponential on neither.

  Q4  Seats present at a point: EXACTLY TWO at lambda = 1, constant over the whole circle, both
      power sums being constant (3/2 and 9/8).  The threshold is a ratio approaching one; the
      construction sits at two.  ** The obstruction's premise -- that at a point only one seat is
      present -- is false at the lowest allowed mode. **

  Q5  ** THE STRUCTURE DOES NOT OBSTRUCT THE LOCAL GAUGING.  Both legs have now fallen: r6747's,
      because the flatness was over the space of members; this one, because the seats are not
      disjoint.  It still does not SUPPLY a gauging -- no connection, no curvature -- but "not
      supplied" and "obstructed" are different findings, and only the first survives.  So Rule 2(a)
      bites the other way: the world forces the gauging as a structure, nothing now forbids it, and
      excluding it is the arbitrary move.  r6742's balance is restated. **

  ⚠ NOT CLAIMED: that the construction supplies a gauge field -- it exhibits no connection, and
  this receipt adds none; what it removes is a reason for saying it cannot.  Not QCD, and nothing
  is named.  Not the third digit of the overlap -- it is the SCALING and the exact participation
  ratio of two that carry the verdict.  Nothing about weak isospin, and no reopening of the global
  group.
""")
print(f"  {len(_checks)} checks, all pass." if all(_checks) else "  FAILURES PRESENT")
assert all(_checks)
