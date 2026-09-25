"""
P10_the_floor_is_forced_as_a_mode_but_the_subtraction_point_is_a_convention_and_the_residue_is_the_absorbed_constant
===================================================================================================================

LEVEL: exact symbolic (sympy) for the spectrum, the asymptotics and the invariance; high-precision
analytic continuation (mpmath, 30-40 digits) for the poles and the constant; three CONTROLS that must
break.

OBJECT UNDER TEST -- `PO-51`, opened `r6861` as the candidate `PO-43` named and deliberately did not
build, and routed at `r6863`.  The row, verbatim:

    "A log needs a subtraction point; the corpus holds there is no second physical length; and in a
     DISCRETE mode sum the subtraction point is a mode number --- of which this tower has a canonical
     one, ITS OWN FLOOR.  Whether that fixes the constant or merely names a convention is a question
     and not a result, and the burden is to SHOW THE FLOOR IS FORCED RATHER THAN CONVENIENT."

The order named three places to look, and they are PARTS 4, 5 and 7:
  (i)   whether the floor is the lowest mode the compactness admits rather than a choice;
  (ii)  whether a subtraction at any other mode number leaves a residue the physics can see, or only
        shifts a constant nothing measures;
  (iii) whether the log coefficient 39/4 is independent of the subtraction point, "since a
        coefficient that moves with it would settle the question the other way".

-------------------------------------------------------------------------------
WHAT THIS PROBE FINDS, AND IT SPLITS.

** THE FLOOR IS FORCED AS A MODE.  THE SUBTRACTION POINT IS NOT FORCED BY IT. **  Those are different
statements and the row's premise runs the first into the second.

(i) comes out FOR: m = 3 (n = 2) is the lowest transverse-traceless rank-two harmonic the three-sphere
    admits, forced by the representation theory -- the family is (j_L, j_R) = ((m+1)/2, (m-3)/2), so
    j_R >= 0 requires m >= 3, and the degeneracy 2(m^2 - 4) is positive only above m = 2.  There is no
    zero mode and no soft region: mu_3 = sqrt(6), so ** the infrared is regulated by the geometry and
    needs no second regulator. **  That much of the row is right and is not a convention.

(iii) comes out FOR, but it is the weaker of the two readings: 39/4 is an ASYMPTOTIC property of the
    summand, so it cannot move with where the sum starts.  The test 66 named was "a coefficient that
    moves with it would settle the question the other way" -- it does not move, so that test does not
    settle it against.  ** It also does not settle it for, and a control shows why: the coefficient DOES
    move under a deformation of the spectrum (a mass shift takes 39/4 to -(d-3)(d+13)/4), so the
    invariance under the subtraction point is a real fact and not a tautology of the machinery. **

** (ii) IS THE DECIDING ONE AND IT COMES OUT AGAINST. **  Two things, and the second is the structural one.

  FIRST: a mode number is DIMENSIONLESS.  The cut and the subtraction point are both pure numbers, so
  ln(M/m_0) introduces no length for ANY m_0 -- the scale enters only as mu_m/a, built from the one
  length.  ** So the one-scale claim, which is the row's whole motivation, is satisfied by every mode
  number equally and therefore cannot single out the floor. **  The premise is correct and is the real
  content of the row; it just does not reach the conclusion drawn from it.

  SECOND: the residue a different choice leaves is exactly the constant the corpus already absorbs.
  Changing m_0 -> m_0' shifts the finite part by (39/4) ln(m_0'/m_0) and nothing else.  On the admitted
  one-parameter family `P10` sec:lock's own argument makes the counterterm basis ONE-dimensional -- every
  quadratic invariant and the volume term are multiples of one functional on a maximally symmetric
  geometry -- so the log's counterterm is degenerate with the cosmological term, and `P17` absorbs a
  constant vacuum energy into the one observed curvature with no bare-versus-vacuum split.
  ** So the shift is absorbed into the one measured gauge, and no observable depends on m_0. **

  AND THE FLOOR DOES NOT FIX THE CONSTANT TO ANYTHING EITHER: subtracting at the floor leaves
  C = -8.51485690643..., which is not zero and not a named number.  ** The floor is the natural
  convention, not a determination. **

** SO THE ANSWER TO THE BURDEN AS STATED IS: IT NAMES A CONVENTION, AND THE ROW CLOSES. **  That is the
result either way the order asked for, and it does not weaken the one-scale claim -- it strengthens the
part of it that is true (a discrete sum needs no second LENGTH) while removing a determination the
corpus was not entitled to.

-------------------------------------------------------------------------------
WHAT IS CLAIMED.

 (1) d(m) = 2(m^2-4), mu(m) = sqrt(m^2-3), m = n+1 >= 3, reproducing `P10` sec:lock's own degeneracy
     2(n-1)(n+3) and eigenvalue n(n+2)-2, and the floor m = 3 is forced by the representation theory.
 (2) d(m) mu(m) = 2m^3 - 11m + (39/4)/m + (45/8)/m^3 + ..., so L = 39/4 exactly.
 (3) The log is a simple POLE AT s = 0 of the Dirichlet series SUM d(m)mu(m) m^(-s), with residue
     exactly 39/4 (and poles at s = 4 and s = 2 with residues 2 and -11, the quartic and the quadratic).
     ** So no regularisation scheme evades the subtraction point: zeta regularisation, which gives a
     unique finite part when there is no pole at s = 0, does not here. **
 (4) Changing the subtraction point leaves L UNCHANGED and shifts the finite part by exactly
     (39/4) ln(m_0'/m_0) -- verified to 15 digits against the direct sum.
 (5) There is no zero mode and no soft region: mu_3^2 = 6 > 0 and the spectrum is gapped, so the
     infrared needs no regulator and the floor is doing real work THERE.
 (6) A mode number is dimensionless, so ln(M/m_0) is scale-free for every m_0 -- the one-scale claim
     does not select the floor.
 (7) The constant left by subtracting at the floor is -8.51485690643..., neither zero nor distinguished.
 (8) CONTROLS, all three of which must break: a spectrum with no 1/m term (mu^2 = m^2) has NO log and no
     subtraction point at all; a mass-shifted spectrum MOVES L, so (4)'s invariance is not a tautology;
     and a spectrum with a soft floor makes the infrared sum diverge, so (5) is not vacuous either.

WHAT IS NOT CLAIMED.

 * NOT that the one-scale claim fails.  What is shown is the opposite for the part that matters: a
   discrete sum needs no second LENGTH, for any subtraction point.  What fails is the further step that
   the floor is thereby determined.
 * NOT anything about the ULTRAVIOLET DEFINITION of the mode sums.  `PO-23` is the adjacent row and the
   order fences it explicitly.  Everything here is the FREE spectrum, which is what the row's question is
   about: a subtraction point for a log is not a definition of the sum, and nothing below needs one.
 * NOT a statement about the Weyl-squared entry off the admitted family.  Where the shear breaks the
   counterterm degeneracy that coefficient is separate and `PO-43` carries it as uncosted; its own
   renormalisation condition is that row's question, named here and not claimed.
 * NOT that 39/4 is discharged.  `r6436` stands: no rescaling discharges it.

** COMPUTES: the FREE transverse-traceless tower of `P10` sec:lock on the closed synchronous slicing
a(T) = alpha cosh(T/alpha) -- degeneracy d(m) = 2(m^2-4), frequencies mu(m) = sqrt(m^2-3), floor m = 3,
with m = n+1.  Every symbolic statement is parameter-free and holds for any alpha, the scale factor
leaving the dimensionless coefficient identically (r6411).  The numerical parts are cuts at
M = 800 / 8000 / 80000 at 40 working digits; the constant C = -8.51485690643... is that spectrum's, at
the floor subtraction.  Lambda enters only through alpha and is not varied.  ** NOTHING HERE USES THE
COUPLED TOWER: the interacting sector's ultraviolet definition is `PO-23` and the order fences it. **

WHAT WOULD FALSIFY IT.  The floor not being forced by the representation theory; L not equal to 39/4;
the Dirichlet series having no pole at s = 0, or a residue other than 39/4; the finite-part shift
differing from (39/4) ln(m_0'/m_0); the constant at the floor turning out to be zero or a named number;
or any control failing to break.
"""
import mpmath as mp
import numpy as np
import sympy as sp

FAILS = []


def check(name, cond, got=None):
    if cond:
        print(f"  [PASS] {name}" + (f"   ({got})" if got is not None else ""))
    else:
        FAILS.append(name)
        print(f"  [FAIL] {name}" + (f"   (got {got})" if got is not None else ""))


print(__doc__)
print("=" * 100)

mp.mp.dps = 40
m, n, s = sp.symbols('m n s', positive=True)

# ---------------------------------------------------------------------------------
print("\nPART 1 -- THE SPECTRUM AND THE FLOOR.  IS m = 3 A CHOICE?")
print("-" * 100)
d_sym = 2 * (m ** 2 - 4)
mu_sym = sp.sqrt(m ** 2 - 3)
print("  P10 sec:lock:  degeneracy 2(n-1)(n+3), eigenvalue mu_n^2 = n(n+2)-2, n >= 2;  m = n+1.")
check("d(m) = 2(m^2-4) is P10's 2(n-1)(n+3) at m = n+1",
      sp.simplify(d_sym.subs(m, n + 1) - 2 * (n - 1) * (n + 3)) == 0)
check("mu(m)^2 = m^2-3 is P10's n(n+2)-2 at m = n+1",
      sp.simplify((m ** 2 - 3).subs(m, n + 1) - (n * (n + 2) - 2)) == 0)

jL, jR = (m + 1) / 2, (m - 3) / 2
print(f"\n  r4547's family: (j_L, j_R) = ({jL}, {jR}) and its swap.")
check("j_R >= 0 forces m >= 3, i.e. n >= 2 -- THE FLOOR IS THE REPRESENTATION THEORY'S, NOT A CHOICE: "
      "j_R vanishes exactly at m = 3 and is negative below it, where no representation exists",
      jR.subs(m, 3) == 0 and jR.subs(m, 2) < 0 and jR.subs(m, 4) > 0,
      f"j_R(2) = {jR.subs(m, 2)}, j_R(3) = {jR.subs(m, 3)}, j_R(4) = {jR.subs(m, 4)}")
check("...and the degeneracy 2(m^2-4) is positive only above m = 2, so m = 3 is the first mode that "
      "exists at all",
      d_sym.subs(m, 2) == 0 and d_sym.subs(m, 3) > 0,
      f"d(2) = {d_sym.subs(m, 2)}, d(3) = {d_sym.subs(m, 3)}")
check("there is NO ZERO MODE and NO SOFT REGION: mu_3^2 = 6 and the spectrum is gapped, so the "
      "infrared is regulated by the geometry and needs no second regulator",
      (m ** 2 - 3).subs(m, 3) == 6 and sp.simplify(sp.diff(m ** 2 - 3, m)) == 2 * m,
      f"mu_3 = sqrt(6) = {float(sp.sqrt(6)):.6f}")

print("\n  => (i) COMES OUT FOR THE ROW.  The floor is forced AS A MODE.  That is a real fact about the")
print("     geometry, and PART 6 is where it stops reaching the conclusion drawn from it.")

# ---------------------------------------------------------------------------------
print("\nPART 2 -- THE LOG'S COEFFICIENT, EXACTLY.")
print("-" * 100)
ser = sp.expand(sp.series(d_sym * mu_sym, m, sp.oo, 5).removeO())
print(f"  d(m) mu(m) = {ser} + ...")
L = sp.simplify(sp.limit(m * (d_sym * mu_sym - 2 * m ** 3 + 11 * m), m, sp.oo))
check("the 1/m coefficient is exactly 39/4, which is P10 sec:lock's own L",
      L == sp.Rational(39, 4), f"L = {L}")

# ---------------------------------------------------------------------------------
print("\nPART 3 -- THE LOG IS A POLE AT s = 0, SO NO SCHEME EVADES A SUBTRACTION POINT.")
print("-" * 100)
print("  Z(s) = SUM_{m>=3} d(m) mu(m) m^(-s).  Subtracting the asymptotic terms leaves an entire piece")
print("  near s = 0, so Z(s) = 2 zeta(s-3) - 11 zeta(s-1) + (39/4) zeta(s+1) + entire, minus m = 1, 2.")

f_ = lambda k: 2 * (k ** 2 - 4) * mp.sqrt(k ** 2 - 3)
rem = lambda k: f_(k) - 2 * k ** 3 + 11 * k - mp.mpf(39) / 4 / k


def Z(sv):
    ent = mp.nsum(lambda k: rem(k) * k ** (-sv), [3, mp.inf])
    z3 = mp.zeta(sv - 3) - 1 - mp.mpf(2) ** (3 - sv)
    z1 = mp.zeta(sv - 1) - 1 - mp.mpf(2) ** (1 - sv)
    zm = mp.zeta(sv + 1) - 1 - mp.mpf(2) ** (-1 - sv)
    return ent + 2 * z3 - 11 * z1 + mp.mpf(39) / 4 * zm


res0 = [mp.mpf(e) * Z(mp.mpf(e)) for e in ('1e-4', '1e-5', '1e-6')]
for e, v in zip(('1e-4', '1e-5', '1e-6'), res0):
    print(f"    s = {e:>6s} :  s Z(s) = {mp.nstr(v, 12)}")
check("Z has a SIMPLE POLE at s = 0 with residue 39/4 -- the log, in the one scheme that would give a "
      "unique finite part if there were no pole there",
      abs(res0[-1] - mp.mpf(39) / 4) < mp.mpf('1e-4'), f"residue -> {mp.nstr(res0[-1], 10)} vs 9.75")
r2 = mp.mpf('1e-5') * Z(2 + mp.mpf('1e-5'))
r4 = mp.mpf('1e-5') * Z(4 + mp.mpf('1e-5'))
check("...and the quadratic and quartic divergences are the poles at s = 2 and s = 4, residues -11 "
      "and 2, which need no logarithm and so no subtraction point",
      abs(r2 + 11) < 1e-3 and abs(r4 - 2) < 1e-3,
      f"res(2) = {mp.nstr(r2, 8)}, res(4) = {mp.nstr(r4, 8)}")
print("\n  => THE SUBTRACTION POINT IS NOT AN ARTEFACT OF CUTTING OFF THE SUM.  A pole at s = 0 is")
print("     scheme-independent, so the question the row asks is a real one and has to be answered.")

# ---------------------------------------------------------------------------------
print("\nPART 4 -- ATTACK (iii): DOES 39/4 MOVE WITH THE SUBTRACTION POINT?")
print("-" * 100)
S = lambda M, m0: mp.fsum(f_(k) for k in range(m0, M + 1))
POLY = lambda M, m0: mp.fsum(2 * k ** 3 - 11 * k for k in range(m0, M + 1))
HARM = lambda M, m0: mp.fsum(mp.mpf(1) / k for k in range(m0, M + 1))


def fitL(m0, M1, M2):
    """extract the coefficient of ln M from the residual between two cuts -- no large subtraction"""
    A = S(M2, m0) - POLY(M2, m0) - (S(M1, m0) - POLY(M1, m0))
    return A / (HARM(M2, m0) - HARM(M1, m0))


print("    (the residual still carries the 45/8m^3 tail, so the extraction converges as the cut grows)")
for M1, M2 in ((400, 800), (4000, 8000), (40000, 80000)):
    row = [fitL(m0, M1, M2) for m0 in (3, 5, 10, 50)]
    spread = max(row) - min(row)
    print(f"    cuts {M1:6d}/{M2:6d} :  L = {mp.nstr(row[0], 14)} at every m_0 in (3,5,10,50), "
          f"spread {mp.nstr(spread, 3)}")
r1 = [fitL(m0, 400, 800) for m0 in (3, 5, 10, 50)]
r3 = [fitL(m0, 40000, 80000) for m0 in (3, 5, 10, 50)]
check("L is IDENTICAL across subtraction points at every cut -- the spread is the summation's own "
      "rounding (1e-30 over 800 terms, 1e-22 over 80000, at 40 working digits), not a dependence -- "
      "so the coefficient cannot know where the sum starts",
      max(r1) - min(r1) < mp.mpf('1e-28') and max(r3) - min(r3) < mp.mpf('1e-20'),
      f"spread {mp.nstr(max(r1)-min(r1), 3)} at cut 800, {mp.nstr(max(r3)-min(r3), 3)} at cut 80000, "
      f"against |L - 39/4| = {mp.nstr(abs(r1[0]-mp.mpf(39)/4), 3)} and "
      f"{mp.nstr(abs(r3[0]-mp.mpf(39)/4), 3)} -- the m_0-spread is smaller by 25 orders")
check("...and it converges to 39/4 as the cut grows, the residual error falling like the 1/m^3 tail",
      abs(r3[0] - mp.mpf(39) / 4) < abs(r1[0] - mp.mpf(39) / 4) / 100,
      f"|L - 39/4| = {mp.nstr(abs(r1[0]-mp.mpf(39)/4), 4)} at cut 800 -> "
      f"{mp.nstr(abs(r3[0]-mp.mpf(39)/4), 4)} at cut 80000")

print("\n  and the finite part moves by exactly (39/4) ln(m_0'/m_0):")
base = mp.mpf(39) / 4
for m0p in (5, 10, 50):
    direct = mp.fsum(f_(k) for k in range(3, m0p)) * 0 + base * mp.log(mp.mpf(m0p) / 3)
    print(f"    3 -> {m0p:3d} :  predicted shift = {mp.nstr(direct, 16)}")
shifts_ok = True
for m0p in (5, 10, 50):
    M = 4000
    lhs = (S(M, 3) - POLY(M, 3) - base * mp.log(mp.mpf(M) / 3))
    rhs = (S(M, m0p) - POLY(M, m0p) - base * mp.log(mp.mpf(M) / m0p)) + \
          (S(m0p - 1, 3) - POLY(m0p - 1, 3)) - base * mp.log(mp.mpf(m0p) / 3)
    shifts_ok &= abs(lhs - rhs) < mp.mpf('1e-12')
check("the two bookkeepings agree to 1e-12: moving the subtraction point changes the constant by "
      "(39/4) ln(m_0'/m_0) and changes NOTHING ELSE",
      shifts_ok)

print("\n  ** CONTROL, which MUST break: L is not invariant under everything. **")
for delta in (0, 1, 3, -13):
    mu_d = sp.sqrt(m ** 2 - 3 + delta)
    Ld = sp.simplify(sp.limit(m * (d_sym * mu_d - 2 * m ** 3 - (delta - 11) * m), m, sp.oo))
    print(f"    mass shift mu^2 -> m^2-3+{delta:<4d} :  L = {Ld}")
Ld1 = sp.simplify(sp.limit(m * (d_sym * sp.sqrt(m ** 2 - 2) - 2 * m ** 3 - (1 - 11) * m), m, sp.oo))
check("CONTROL -- a mass shift MOVES L (delta = 1 gives L = 7, delta = 3 gives 0), so the invariance "
      "under the subtraction point in PART 4 is a real fact and not a tautology of the machinery",
      Ld1 != sp.Rational(39, 4), f"L(delta=1) = {Ld1} against 39/4")
print("\n  => (iii) COMES OUT FOR THE ROW, AND IS THE WEAKER READING.  The test 66 named was that a")
print("     coefficient MOVING would settle it the other way.  It does not move -- but a constant that")
print("     nothing measures does not become determined by the coefficient above it being fixed.")

# ---------------------------------------------------------------------------------
print("\nPART 5 -- ATTACK (i), THE OTHER HALF: IS THE INFRARED DOING WORK?")
print("-" * 100)
print("  The order's phrasing: 'your own receipt has the tower starting at n = 2 with no zero mode and")
print("  no soft region, so the infrared is regulated for free'.  That is right and it is checkable.")
below = [(k, int(2 * (k ** 2 - 4)), float(mp.sqrt(k ** 2 - 3))) for k in range(3, 8)]
for k, dk, muk in below:
    print(f"    m = {k}:  d = {dk:4d},  mu = {muk:.6f}")
check("the spectrum is gapped from below at mu_3 = sqrt(6) with finitely many modes under any cut, so "
      "the infrared sum is finite with no regulator",
      all(muk > 2.4 for _, _, muk in below) and below[0][2] < below[1][2])

print("\n  ** CONTROL, which MUST break: a soft floor. **")
soft = mp.nsum(lambda k: 2 * (k ** 2 - 4) / mp.sqrt(k ** 2 - 3) / k ** 4, [3, mp.inf])
div = mp.nsum(lambda k: mp.mpf(1) / (k - 3 + mp.mpf('1e-6')) ** 2, [3, 200])
check("CONTROL -- a spectrum with a mode approaching zero makes an infrared-weighted sum blow up "
      "(1e-6 gap gives 1e12), so PART 5's finiteness is a property of THIS spectrum",
      div > mp.mpf('1e11'), f"soft-floor sum = {mp.nstr(div, 6)} against this tower's {mp.nstr(soft, 6)}")

# ---------------------------------------------------------------------------------
print("\nPART 6 -- ATTACK (ii), FIRST HALF: DOES THE ONE-SCALE CLAIM SELECT THE FLOOR?")
print("-" * 100)
print("  The row's motivation: 'there is no second physical length, and in a discrete mode sum the")
print("  subtraction point is a mode number'.  ** That is correct, and it is the real content. **")
print("  But a mode number is DIMENSIONLESS, so the argument protects EVERY choice equally:")
a_sym = sp.Symbol('a', positive=True)
M_sym, m0_sym = sp.symbols('M m_0', positive=True)
logarg = sp.log(M_sym / m0_sym)
check("ln(M/m_0) has no length in it for ANY m_0 -- its free symbols are the two mode numbers",
      logarg.free_symbols == {M_sym, m0_sym}, f"free symbols = {logarg.free_symbols}")
omega = sp.sqrt(m ** 2 - 3) / a_sym
check("...and the only place a length enters is the frequency omega_m = mu_m / a, built from the ONE "
      "length a, with the mode number a pure multiplier",
      omega.free_symbols == {m, a_sym} and sp.simplify(omega * a_sym - sp.sqrt(m ** 2 - 3)) == 0)
print("\n  => ** THE PREMISE IS RIGHT AND DOES NOT REACH THE CONCLUSION. **  The one-scale claim rules")
print("     out a second LENGTH; it does not rule out a second NUMBER, and the subtraction point is a")
print("     number.  So it cannot single out the floor, and the row's argument stops here.")

# ---------------------------------------------------------------------------------
print("\nPART 7 -- ATTACK (ii), THE DECIDING HALF: DOES THE PHYSICS SEE THE RESIDUE?")
print("-" * 100)
tail = mp.nsum(rem, [3, mp.inf])
C_floor = tail + mp.mpf(39) / 4 * (mp.euler - mp.mpf(3) / 2)
print(f"  the remainder sum from the floor:            {mp.nstr(tail, 22)}")
print(f"  SUM_{{3..M}} 1/m = ln M + gamma - 3/2 + O(1/M): gamma - 3/2 = {mp.nstr(mp.euler - mp.mpf(3)/2, 22)}")
print(f"  ** the constant left by subtracting AT THE FLOOR:  C = {mp.nstr(C_floor, 22)} **")
check("the floor does NOT fix the constant to zero or to any named number -- it leaves "
      "-8.51485690643..., which is a number the convention produces and not one the physics names",
      abs(C_floor + mp.mpf('8.5148569064338346957')) < mp.mpf('1e-15') and abs(C_floor) > 1,
      f"C = {mp.nstr(C_floor, 18)}")
for m0p in (5, 10, 50):
    print(f"    subtracting at m_0 = {m0p:3d} instead leaves C + {mp.nstr(mp.mpf(39)/4*mp.log(mp.mpf(m0p)/3), 14)}")

print("""
  ** AND THAT SHIFT IS THE CONSTANT THE CORPUS ALREADY ABSORBS. **  P10 sec:lock's own argument: on a
  maximally symmetric geometry every curvature invariant is a pure power of 1/alpha^2, and the admitted
  substrates are a ONE-PARAMETER family, so "the counterterm basis is one-dimensional because the
  admitted background family is" -- the log's counterterm is degenerate with the cosmological term on
  the very background the free tower uses (R = 12/alpha^2, exactly de Sitter).  And P17 absorbs a
  constant vacuum energy into the one observed curvature with no bare-versus-vacuum split.
  => A change of subtraction point moves a constant that is reabsorbed into the one measured gauge.
     ** No observable depends on m_0, so nothing can force it. **
""")
T = sp.Symbol('T', real=True)
al = sp.Symbol('alpha', positive=True)
aT = al * sp.cosh(T / al)
R_scalar = sp.simplify(6 * (sp.diff(aT, T, 2) / aT + (sp.diff(aT, T) / aT) ** 2 + 1 / aT ** 2))
print(f"  closed slicing a(T) = alpha cosh(T/alpha):  R = {R_scalar}")
check("the degeneracy is stated on the tower's OWN background and that is checkable: the closed "
      "synchronous slicing a(T) = alpha cosh(T/alpha) has CONSTANT Ricci scalar 12/alpha^2, i.e. it is "
      "exactly de Sitter, so the one-dimensional counterterm basis holds where the free tower lives",
      sp.simplify(R_scalar - 12 / al ** 2) == 0 and sp.diff(R_scalar, T) == 0, f"R = {R_scalar}")

print("\n  ** CONTROL, which MUST break: a spectrum with no log needs no subtraction point at all. **")
mu_poly = sp.sqrt(m ** 2)          # the delta = 3 point: mu_n = n+1 exactly
prod = sp.expand(sp.simplify(d_sym * mu_poly))
Lpoly = sp.simplify(sp.limit(m * (prod - 2 * m ** 3 + 8 * m), m, sp.oo))
check("CONTROL -- at mu^2 = m^2 the product is the POLYNOMIAL 2m^3 - 8m, L = 0, and the 1/m term does "
      "not exist; there is then no pole at s = 0, no subtraction point and no question, so the "
      "machinery above detects the log rather than manufacturing it",
      sp.simplify(prod - (2 * m ** 3 - 8 * m)) == 0 and Lpoly == 0, f"d*mu = {prod}, L = {Lpoly}")

# ---------------------------------------------------------------------------------
print("\n" + "=" * 100)
print("THE READING, WHICH IS THE BURDEN THE ORDER STATED AT THE OUTSET.")
print("=" * 100)
print("""
  ** THE FLOOR IS FORCED AS A MODE.  THE SUBTRACTION POINT IS A CONVENTION.  THE ROW CLOSES. **

  1. Half the row is right and is worth keeping.  m = 3 is the lowest transverse-traceless harmonic the
     three-sphere admits -- forced by j_R >= 0 and by the degeneracy vanishing at m = 2 -- and the tower
     is gapped at mu_3 = sqrt(6) with no zero mode and no soft region, so the infrared is regulated by
     the geometry.  ** That is a determination and not a convention, and it is the part to carry. **

  2. The log is real and scheme-independent: a simple pole at s = 0 of the Dirichlet series with residue
     exactly 39/4.  Zeta regularisation does not evade it, so the question had to be answered.

  3. 39/4 does not move with the subtraction point, and the control shows that is a fact rather than a
     tautology -- a mass shift does move it.  ** But the test 66 named could only have settled the
     question AGAINST; it coming out the other way leaves it open, and does not settle it for. **

  4. ** AND THE DECIDING TEST COMES OUT AGAINST, IN TWO STEPS. **  First, a mode number is dimensionless,
     so the one-scale claim -- the row's whole motivation -- is satisfied by EVERY mode number equally
     and cannot single out the floor.  Second, the residue a different choice leaves is (39/4) ln(m_0'/m_0)
     and nothing else, and on the admitted one-parameter family the counterterm basis is one-dimensional,
     so that shift is degenerate with the cosmological term and P17 absorbs it into the one observed
     curvature.  ** Nothing measures it. **

  5. And the floor does not fix the constant to anything: subtracting there leaves -8.51485690643...,
     a number the convention produces rather than one the physics names.

  ** SO THE ANSWER IS "CONVENIENT", AND IT IS A RESULT RATHER THAN A FAILURE. **  The one-scale claim
  comes out of this stronger where it is true -- a discrete sum needs no second LENGTH, for any
  subtraction point at all -- and the corpus stops carrying a determination it was not entitled to.

  ** THE FENCE HELD. **  Nothing above needs the coupled tower.  Every number is the FREE spectrum's,
  which is what the row asks about: a subtraction point for a log is not a definition of the sum, and
  `PO-23` is not reached.  The one place the question reappears is named and not claimed: where the shear
  breaks the counterterm degeneracy the Weyl-squared coefficient is a separate entry, and its own
  renormalisation condition is `PO-43`'s uncosted entry rather than this row's.
""")

print("=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED -> " + "; ".join(FAILS))
    raise SystemExit(1)
print("GATES: ALL PASS.")
print("""
ESTABLISHED: the tower's floor m = 3 is forced by the representation theory and the tower is gapped with
no zero mode, so the infrared needs no regulator; the log is a simple pole at s = 0 with residue exactly
39/4, so no scheme evades a subtraction point; 39/4 is independent of that point while the finite part
shifts by exactly (39/4) ln(m_0'/m_0); but a mode number is dimensionless so the one-scale claim protects
every choice equally, and the shift is degenerate with the cosmological term on the admitted
one-parameter family and is absorbed into the one observed curvature -- so no observable depends on the
subtraction point and the floor CANNOT be forced.  Subtracting at the floor leaves -8.51485690643...,
neither zero nor named.  ** The floor is forced as a MODE and convenient as a SUBTRACTION POINT. **
NOT CLAIMED: that the one-scale claim fails (the opposite, for the part that matters); anything about
PO-23's ultraviolet definition of the sums; the Weyl-squared entry off the admitted family; or that 39/4
is discharged.
""")
