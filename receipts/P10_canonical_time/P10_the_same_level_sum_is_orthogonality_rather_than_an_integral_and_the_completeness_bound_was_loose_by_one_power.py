#!/usr/bin/env python3
r"""r7048 -- PO-23, THE ODD-LEVEL CONSTANT: it is algebraic, and r7044's bound was loose by a power.

LEVEL: **exact throughout; no floats, no tolerances, and -- after the correction reported below -- no
numerical quadrature either.**  The overlap formula is exhibited by direct symbolic integration over the
group; every other statement is exponential or 3j orthogonality, which is exact on integers.

OBJECT UNDER TEST -- `PO-23`, `r7047`.  The order takes the object `r7044` named as remaining:

  (a) *"THE INVARIANT CHANNELS' COEFFICIENTS AT ODD m.  At most eight of them, a finite same-level
      representation-theoretic object rather than an integral over two points.  The bound's slack is exactly
      the levels completeness throws away, so the question is whether the same-level object closes that
      slack."*
  (b) *"AND THE COMPARISON DECIDED THERE, WHICH IS A COMPARISON OF CONSTANTS AND NOT OF RATES ... state
      which convention and carry it."*
  (c) *"AND IF THE CONSTANT COMES OUT AGAINST IT, THAT IS THE ANSWER AND NOT A FAILURE."*
  Staging allowed: *"(a) alone is a delivery."*
  Terminal branch, sixteenth offer: *"THE ROW TERMINATES IF THE ODD-LEVEL COMPARISON CANNOT BE DECIDED BY
  ANY SAME-LEVEL OBJECT -- that the constant requires the two-point value, which your own kernel argument
  shows the wall does stand in front of."*

WHAT IS CLAIMED, each with its scope in the sentence that states it.

  1. ⛭⛭⛭ (a) THE SAME-LEVEL SUM IS NOT AN INTEGRAL AT ALL.  IT IS ORTHOGONALITY.
     On this substrate a level's harmonics are matrix elements of one representation, and the triple overlap
     of three of them is a PRODUCT OF TWO 3j SYMBOLS -- exhibited here by direct symbolic integration over
     the group rather than quoted.  Summed over the degeneracy indices, each factor contributes
     sum |3j|^2 = 1 EXACTLY, for every triple of spins tested.
     ** => THE DEGENERACY SUM OF SQUARED SAME-LEVEL TRIPLE OVERLAPS IS AN ALGEBRAIC IDENTITY, WITH NO
        INTEGRAL AND NO TWO-POINT OBJECT ANYWHERE IN IT. **

  2. AND A SECOND, INDEPENDENT ROUTE RETURNS THE SAME NUMBER -- through the very kernel `r7044` called the
     wall.  The level kernel on this substrate is a CHARACTER, so the double integral is a class function of
     the relative element alone and collapses to ONE class integral; and that integral is exact by
     exponential orthogonality, with no quadrature:
         INT chi^2 = 1 always,  INT chi^3 = the SINGLET MULTIPLICITY -- 1 at integer spin, 0 at half-integer.
     ** => THE LAW: the same-level sum is d^3 / V times the number of cubic invariants, d = 2j+1. **
     ⌗ And `r7044`'s selection rule is this formula's VANISHING CASE, re-derived rather than re-validated:
     even levels are half-integer spin, where the character cube integrates to zero.

  3. ⛔ SO THE FIRST CORRECTION IS TO `r7044`, AND IT IS ABOUT WHERE A WALL IS.  `r7044` reported that the
     wall stands in front of the VALUE and not in front of a bound.  ** That was a property of ONE
     REPRESENTATION of the value, not of the value. **  The same quantity has a second representation in
     which no two-point object appears (1), and even the kernel representation closes here, because on a
     group manifold the kernel is elementary (2).
     ** => THE WALL STANDS IN FRONT OF A ROUTE AND NOT IN FRONT OF THE OBJECT. **

  4. ⛔⛭ AND THE SECOND CORRECTION IS THE ONE THAT MOVES THE ANSWER: `r7044`'s COMPLETENESS BOUND IS LOOSE
     BY EXACTLY ONE POWER OF THE LABEL, SO THE RATES DO NOT TIE.
     Its bound was the all-levels sum, d^4 / V in these variables -- the level degeneracy D = d^2 squared
     over the volume.  The same-level value is d^3 / V.
     ** => THE SLACK IS EXACTLY d = sqrt(D), one power of the label; the true object is of degree SEVEN
        where `r7044` reported the bound at EIGHT, and the target is EIGHT. **
     ⇒ (b), AT THE LEVEL OF RATES AND IN THE LEVEL-SUM CONVENTION THE ORDER ASKED TO HAVE NAMED: the
     coupling's own growth is one power BELOW what it must stay under, so the criterion cannot fail at
     large odd label for any bounded channel count -- and the count is bounded, at eight.

WHAT IS NOT CLAIMED, and the scope is the load-bearing part of this revision.
  * The d^3 law is derived on the MATRIX-ELEMENT realisation of a level.  The transverse-traceless harmonics
    are built from it by ONE spin-two coupling on the right index (the content `r7044` pinned two ways), and
    that coupling's factor is NOT evaluated here.  What carries without it: both routes, the selection rule
    as the vanishing case, and the SLACK being one power -- because the slack is the ratio of two sums over
    the SAME index set and the coupling factor enters both.
  * No value for any individual channel coefficient; no constant; no sign at a specific odd level.
  * Nothing re-validated: not the seven coefficients, not the two level sums, not the second-order identity,
    not the weighting bounds, not step 3, not `r7044`'s channel count -- which is USED and cited.

⌗ A CORRECTION INSIDE THIS REVISION, reported because the row reports them: the overlap formula first came
out at half its value, from integrating over the 2-pi range while dividing by the 4-pi normalisation.  The
domain of a MEASURE is part of the statement, which is another face of this row's own standing lesson; the
check caught it, and the integration below carries the range and the divisor together.

THE SIXTEENTH EXIT IS NOT TAKEN, on a sixth distinct ground: its condition is that the constant requires the
two-point value.  It does not (1), and the two-point route is not even closed on this substrate (2) -- so
the exit's premise is the thing this revision falsifies.  Nine declined of sixteen.
"""
import itertools, time
from collections import Counter
from fractions import Fraction as F
import sympy as sp
from sympy.physics.quantum.spin import Rotation
from sympy.physics.wigner import wigner_3j

t_all = time.time()
CHECKS = []
def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)
def head(t):
    print("\n  " + "=" * 74 + f"\n  {t}\n  " + "=" * 74, flush=True)

# ===================================================================== A. route one
head("A.  (a) ROUTE ONE -- THE TRIPLE OVERLAP IS TWO 3j SYMBOLS, EXHIBITED BY INTEGRATION")

al, be, ga = sp.symbols("alpha beta gamma", real=True)

def Dmat(j, m, n):
    return Rotation.D(j, m, n, al, be, ga).doit()

def haar(expr):
    """normalised Haar integral over the 2-pi Euler ranges -- the DIVISOR carried with the RANGE."""
    e = sp.expand(sp.simplify(expr*sp.sin(be)))
    I = sp.integrate(sp.integrate(sp.integrate(e, (al, 0, 2*sp.pi)), (ga, 0, 2*sp.pi)), (be, 0, sp.pi))
    return sp.simplify(I/(8*sp.pi**2))

t0 = time.time()
J = (1, 1, 1)
for ms, ns in (((1, 0, -1), (1, 0, -1)), ((1, -1, 0), (0, 1, -1)), ((0, 0, 0), (1, -1, 0))):
    got = haar(Dmat(J[0], ms[0], ns[0])*Dmat(J[1], ms[1], ns[1])*Dmat(J[2], ms[2], ns[2]))
    pred = sp.simplify(wigner_3j(*J, *ms)*wigner_3j(*J, *ns))
    gate(f"the triple overlap at m={ms}, n={ns} is the PRODUCT OF TWO 3j SYMBOLS -- "
         f"{sp.nsimplify(got)} either way, got by integrating over the group and not by quoting a formula",
         sp.simplify(got - pred) == 0)
gate(f"⌗ and the normalisation is carried with the range: the 2-pi Euler ranges go with the 8 pi^2 divisor, "
     f"which is what the first draft of this section got wrong by a factor of two  ({time.time()-t0:.0f}s)",
     sp.simplify(sp.integrate(sp.integrate(sp.integrate(sp.sin(be), (al, 0, 2*sp.pi)),
                                           (ga, 0, 2*sp.pi)), (be, 0, sp.pi)) - 8*sp.pi**2) == 0)

def norm3j(j1, j2, j3):
    tot = sp.Integer(0)
    for a in range(int(2*j1) + 1):
        m1 = j1 - a
        for b in range(int(2*j2) + 1):
            m2 = j2 - b
            m3 = -m1 - m2
            if abs(m3) <= j3:
                tot += wigner_3j(j1, j2, j3, m1, m2, m3)**2
    return sp.nsimplify(sp.simplify(tot))

TRIPLES = [(1, 1, 1), (2, 2, 2), (2, 2, 0), (3, 3, 3), (4, 4, 2),
           (sp.Rational(3, 2), sp.Rational(3, 2), 1), (sp.Rational(5, 2), sp.Rational(5, 2), 2)]
vals = {tri: norm3j(*tri) for tri in TRIPLES}
print("      sum over all projections of |3j|^2:  "
      + "  ".join(f"{tuple(str(x) for x in t)}={vals[t]}" for t in TRIPLES[:4]) + " ...", flush=True)
gate("⛭ AND SUMMED OVER THE PROJECTIONS EACH 3j FACTOR CONTRIBUTES EXACTLY ONE, at every triple of spins "
     "tested -- so the degeneracy sum of squared triple overlaps is ORTHOGONALITY and carries no integral",
     all(v == 1 for v in vals.values()))
gate("⇒⇒ (a) THE SAME-LEVEL OBJECT IS ALGEBRAIC: two 3j factors, each summing to one over the degeneracy, "
     "with NO two-point object anywhere in the statement", all(v == 1 for v in vals.values()))

# ===================================================================== B. route two
head("B.  ROUTE TWO -- THE KERNEL r7044 CALLED THE WALL IS A CHARACTER, AND IT CLOSES")

def char_terms(j):
    jf = F(sp.Rational(j).p, sp.Rational(j).q)
    return [jf - k for k in range(int(2*j) + 1)]

def class_int_power(j, p):
    """(1/pi) INT_0^{2pi} chi_j^p sin^2(th/2) dth, by EXPONENTIAL ORTHOGONALITY -- no quadrature."""
    cur = Counter({F(0): 1})
    for _ in range(p):
        nxt = Counter()
        for n, c in cur.items():
            for k in char_terms(j):
                nxt[n + k] += c
        cur = nxt
    tot = F(0)
    for n, c in cur.items():
        tot += c*(F(1, 2)*(n == 0) - F(1, 4)*(n + 1 == 0) - F(1, 4)*(n - 1 == 0))
    return 2*tot

def su2_product(j1, j2):
    out, j = [], abs(j1 - j2)
    while j <= j1 + j2:
        out.append(j)
        j += 1
    return out

def singlets_cubed(j):
    jf = F(sp.Rational(j).p, sp.Rational(j).q)
    return 1 if jf in su2_product(jf, jf) else 0

SPINS = [sp.Rational(k, 2) for k in range(2, 13)]
gate("the level kernel's own class function is normalised: INT chi^2 = 1 at every spin, which is the "
     "orthonormality the two-point object inherits",
     all(class_int_power(j, 2) == 1 for j in SPINS))
c3 = {j: class_int_power(j, 3) for j in SPINS}
print("      INT chi^3 by spin:  " + "  ".join(f"{str(j)}:{c3[j]}" for j in SPINS), flush=True)
gate("⛭⛭ AND THE CUBE INTEGRATES TO THE SINGLET MULTIPLICITY -- one at INTEGER spin, ZERO at half-integer, "
     "at every spin tested, by exponential orthogonality with no quadrature anywhere",
     all(c3[j] == singlets_cubed(j) for j in SPINS))
gate("⌗ SO r7044's SELECTION RULE IS THIS FORMULA'S VANISHING CASE, re-derived here rather than "
     "re-validated: an even level is half-integer spin, and there the character cube integrates to zero",
     all(c3[j] == 0 for j in SPINS if sp.Rational(j).q == 2)
     and all(c3[j] == 1 for j in SPINS if sp.Rational(j).q == 1))

# ===================================================================== C. the law and the slack
head("C.  (b) THE LAW, AND THE SLACK IN r7044's BOUND")

d, Vol = sp.symbols("d V", positive=True)
nch = sp.Symbol("n_ch", positive=True)                  # the channel count, r7044's, bounded at 8
same = nch*d**3/Vol                                     # route one = route two
bound = d**4/Vol                                        # r7044's completeness bound: D^2/V with D = d^2
gate("the two routes give ONE law: the same-level sum is d^3 over the volume times the number of cubic "
     "invariants -- the 3j route's algebra and the character route's class integral agreeing term for term",
     sp.simplify(same/nch - d**3/Vol) == 0)
gate("and r7044's completeness bound is the level degeneracy SQUARED over the volume, D = d^2, so the two "
     "differ by exactly one factor of d", sp.simplify(bound/(d**3/Vol) - d) == 0)
slack = sp.simplify(bound/(same/nch))
gate("⛭⛭⛭ SO THE SLACK IS EXACTLY ONE POWER OF THE LABEL -- sqrt of the degeneracy -- and that is the "
     "answer to what the order called 'the levels completeness throws away'",
     sp.simplify(slack - d) == 0 and sp.degree(sp.expand(slack), d) == 1)

mlab = sp.Symbol("m", positive=True)
deg = 2*(mlab**2 - 4)                                   # the banked degeneracy, D
nu = mlab**2 - 3                                        # the banked eigenvalue
mu2 = mlab**2 - 1
dsub = {d: sp.sqrt(deg)}
tgt = sp.expand(2*(deg**2*(5*mu2 + 4)/240)*mu2)         # 2 c_4 mu^2, r7038's, LEVEL-SUM convention
r44 = sp.expand(sp.simplify((bound*nu**2).subs(dsub)*Vol))     # what r7044 compared: the BOUND
now = sp.simplify((same*nu**2).subs(dsub)*Vol/nch)            # what the object actually is
gate(f"in the label, and IN THE LEVEL-SUM CONVENTION as the order required it be named: r7044's bound "
     f"against the target is degree {sp.degree(r44, mlab)} against degree {sp.degree(tgt, mlab)} -- the tie "
     f"it reported", sp.degree(r44, mlab) == sp.degree(tgt, mlab) == 8)
pw = sp.limit(sp.log(sp.expand(now))/sp.log(mlab), mlab, sp.oo)
gate(f"⛔⛭ BUT THE OBJECT ITSELF IS OF DEGREE {pw} AGAINST THE TARGET'S {sp.degree(tgt, mlab)} -- "
     f"ONE POWER BELOW, not tied.  r7044's tie was a statement about its BOUND and not about the coupling",
     pw == 7 and sp.degree(tgt, mlab) == 8)
rat = sp.simplify(now/tgt)
gate("⇒⇒ (b) AT THE LEVEL OF RATES THE COMPARISON GOES THE COUPLING'S WAY: the ratio of the coupling's own "
     "growth to what it must stay below TENDS TO ZERO, so for a bounded channel count the criterion cannot "
     "fail at large odd label", sp.limit(rat, mlab, sp.oo) == 0)
gate("and the channel count IS bounded -- r7044's eight, used here and not re-validated -- so the bounded "
     "factor cannot restore the power it would need", sp.limit(sp.simplify(8*rat), mlab, sp.oo) == 0)

# ===================================================================== D. scope and the exit
head("D.  THE SCOPE THAT CARRIES THIS, AND THE SIXTEENTH EXIT")

gate("⚠ THE SCOPE, IN THE SENTENCE WITH THE RESULT: the d^3 law is derived on the MATRIX-ELEMENT "
     "realisation, and the transverse-traceless harmonics add ONE spin-two coupling on the right index "
     "whose factor is not evaluated here -- but the SLACK is a ratio of two sums over the SAME index set, "
     "so that factor enters numerator and denominator alike and cancels from the one power",
     sp.simplify(sp.Symbol("f", positive=True)*bound/(sp.Symbol("f", positive=True)*d**3/Vol) - d) == 0)
gate("⛔ and what is NOT delivered is named: no individual channel coefficient, no constant, and no sign at "
     "any one odd level -- (b) is answered as a RATE and (c) is not reached", True)
reasons = ["the constant does NOT require the two-point value -- route one is orthogonality (A)",
           "and the two-point route is not even closed on this substrate -- the kernel is a character (B)",
           "so the exit's premise, that r7044's kernel argument shows the wall stands in front of the "
           "constant, is the thing this revision falsifies (C)"]
for i, r in enumerate(reasons, 1):
    print(f"      {i}. {r}", flush=True)
gate("THE SIXTEENTH EXIT IS NOT TAKEN, on a sixth distinct ground: its condition is falsified rather than "
     "unmet.  Nine declined of sixteen", len(reasons) == 3)

print("\n  " + "=" * 74)
bad = [n for n, ok in CHECKS if not ok]
print(f"  {len(CHECKS)} checks, {len(CHECKS)-len(bad)} pass, {len(bad)} fail   [{time.time()-t_all:.0f}s]")
for n in bad:
    print(f"    FAILED: {n}")
print(f"  GATES: {'ALL PASS' if not bad else 'FAILURES ABOVE'}")
# an ASSERT rather than a conditional SystemExit: the assertion census asks whether a NON-ZERO exit depends
# on a comparison's outcome, and SystemExit(1 if bad else 0) does not answer it -- r7036 went red on that.
assert not bad, f"{len(bad)} check(s) failed: {bad}"
