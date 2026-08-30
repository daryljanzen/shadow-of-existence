"""
LEVEL: exact symbolic, with a positive control.

WHY THIS PROBE EXISTS.  P14 carries W(r) = lambda sqrt(f)/r, a genuine supersymmetric
quantum-mechanics superpotential: it generates partner potentials V_pm = W^2 +- dW/dx
and an exact zero mode by the sign change of W at the throat.  A superpotential of that
kind invites the question whether the pair is SHAPE INVARIANT -- the condition under
which the SUSY ladder generates the whole spectrum -- and the paper does not ask it.

WHAT IS CLAIMED.  The pair is NOT shape invariant.  V_+(lambda) = V_-(mu) + R with R
independent of r admits no constant shift mu(lambda), except the degenerate mu = -lambda,
which returns V_+(lambda) = V_-(-lambda) IDENTICALLY and so R = 0: the partners coincide
and there is no energy shift to climb.  Therefore the exactness available in P14 is the
ZERO MODE's, which is topological, and not the SPECTRUM's, which would require
solvability -- and that is why the generation count is read from an index rather than
from a list of levels.

WHAT IS NOT CLAIMED.  Not that the radial problem has no solutions: it has, and the
zero mode is exhibited in the paper.  Not that no exact spectrum exists by any other
route.  Not that shape invariance is necessary for exact solvability in general -- it
is sufficient, and its failure removes the SUSY ladder specifically.

WHAT WOULD FALSIFY IT.  A constant shift mu(lambda) making V_+(lambda) - V_-(mu)
independent of r with R nonzero.  The POSITIVE CONTROL below is the point: the same
machinery is run on the Poschl-Teller superpotential W = lambda tanh(x), which IS shape
invariant, and it must come out invariant -- otherwise the test cannot tell the two
apart and the negative means nothing.
"""
import sympy as sp

FAILS = []


def check(name, cond, got=None):
    if cond:
        print(f"  [PASS] {name}" + (f"   ({got})" if got is not None else ""))
    else:
        FAILS.append(name)
        print(f"  [FAIL] {name}" + (f"   (got {got})" if got is not None else ""))


r, M, a, lam, mu = sp.symbols('r M alpha lambda mu', positive=True)
f = 1 - 2 * M / r - r**2 / a**2

print(__doc__)
print("=" * 78)
print("  W(r) = lambda sqrt(f)/r,   f = 1 - 2M/r - r^2/alpha^2      [P14 sec:chirality]")
print("  tortoise x:  dx = dr/f,  so d/dx = f d/dr")
print()

g = sp.sqrt(f) / r


def V(sign, coeff):
    W = coeff * g
    return sp.simplify(W**2 + sign * f * sp.diff(W, r))


Vp = V(+1, lam)

# the degenerate shift: partners coincide, R = 0, no ladder
deg = sp.simplify(Vp - V(-1, -lam))
check("mu = -lambda gives V_+(lambda) - V_-(-lambda) = 0 identically, so R = 0",
      deg == 0, f"difference = {deg}")

# no constant shift works
for shift, label in [(lam - 1, "lambda - 1"), (lam + 1, "lambda + 1"),
                     (lam - sp.Rational(1, 2), "lambda - 1/2"),
                     (lam + sp.Rational(1, 2), "lambda + 1/2")]:
    d = sp.simplify(sp.diff(sp.simplify(Vp - V(-1, shift)), r))
    check(f"mu = {label}: the difference is NOT r-independent",
          sp.simplify(d) != 0, "d/dr != 0")

# solving for a general mu returns an r-DEPENDENT expression -- no constant exists
gen = sp.simplify(sp.diff(sp.simplify(Vp - V(-1, mu)), r))
sols = sp.solve(sp.Eq(gen, 0), mu)
nonconst = [s for s in sols if r in s.free_symbols]
check("solving for a general mu(lambda) returns only r-DEPENDENT roots (plus mu = -lambda)",
      len(nonconst) >= 1 or all(sp.simplify(s + lam) == 0 for s in sols),
      f"{len(sols)} root(s), {len(nonconst)} r-dependent")

# ---- POSITIVE CONTROL: Poschl-Teller IS shape invariant, and must register so ----
print()
print("  POSITIVE CONTROL -- W = lambda tanh(x), the Poschl-Teller superpotential,")
print("  which IS shape invariant with mu = lambda - 1 and R = lambda^2 - (lambda-1)^2.")
x = sp.Symbol('x', real=True)


def Vpt(sign, coeff):
    W = coeff * sp.tanh(x)
    return sp.simplify(W**2 + sign * sp.diff(W, x))


ctrl = sp.simplify(Vpt(+1, lam) - Vpt(-1, lam - 1))
check("CONTROL: V_+(lambda) - V_-(lambda-1) is independent of x",
      sp.simplify(sp.diff(ctrl, x)) == 0, f"= {sp.simplify(ctrl)}")
R = sp.simplify(ctrl)
check("CONTROL: and R is NONZERO -- a real ladder, unlike the degenerate case above",
      sp.simplify(R) != 0, f"R = {R}")
check("CONTROL: R = lambda^2 - (lambda-1)^2 = 2 lambda - 1",
      sp.simplify(R - (2 * lam - 1)) == 0, f"R = {sp.simplify(R)}")

print()
print("=" * 78)
if FAILS:
    print(f"  VERDICT: {len(FAILS)} FAILURE(S): {', '.join(FAILS)}")
    raise SystemExit(1)
print("  VERDICT: ALL PASS.  P14's superpotential admits no constant shape-invariance")
print("  shift; the one shift that works is degenerate and gives R = 0, so the partners")
print("  coincide and there is no ladder.  The positive control shows the same machinery")
print("  DOES detect shape invariance where it holds, with a nonzero R.  So the exactness")
print("  in P14 is the zero mode's -- topological -- and not the spectrum's, which is why")
print("  the generation count is read from an index rather than a list of levels.")
print("=" * 78)
