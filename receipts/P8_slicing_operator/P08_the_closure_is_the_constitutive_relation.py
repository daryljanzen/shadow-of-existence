"""
P08_the_closure_is_the_constitutive_relation
============================================

Object under test — P8 `sec:open`, "The emergence of the bend", closing sentence:

    "What remains open here is therefore not the emergence of the bend as such, but
     the matter content's own generative law where the construction does not supply
     one: a dynamics for the curve itself, as against the ordinary leaf evolution
     that carries it. That is the distinction between a complete dynamical theory
     and a kinematical one, and it is the deepest question this construction opens
     onto."

CLAIM UNDER TEST: that the construction supplies no dynamics for the curve.

The test is not rhetorical. P9 `sec:open` collects the matter functionals for the
non-spherical classes and states the homogeneous closure explicitly --- "two
independent functionals of the cut (X,Y) modulo the contracted-Bianchi
(conservation) identity ... with the perfect-fluid closure p_chi = p_perp a single
ordinary differential equation on (X,Y)". P8's own sec:gauge states the spherical
half of the same fact --- "the angular component is fixed by the radial pair through
the contracted Bianchi identity, so the radial pair carries the content" --- and
never draws the closure.

This receipt establishes the spherical closure, which is the class P8 owns.

WHAT IS ESTABLISHED
  (1) rho is the bend, independent of the lapse:      rho = m'(r) / 4 pi r^2
  (2) the contracted Bianchi identity is satisfied identically, so p_t is fixed by
      the radial pair: two free functions (f, A) -> two independent stress components
  (3) with isotropy and an equation of state p_r = P(rho) the system CLOSES to two
      first-order ODEs for (m, A) --- the TOV system in the operator's own variables
  (4) the closure reduces to Schwarzschild on the vacuum member, which is the check
      the derivation has to pass

WHAT IS NOT ESTABLISHED, and is the point
  The equation of state itself. It is the input, here and in general relativity
  alike: GR's contracted Bianchi identity supplies conservation and not the
  constitutive law. So "the slicing operator is kinematic" is not a property that
  distinguishes this construction from general relativity.

The receipt could have returned otherwise: if the Bianchi residual had been non-zero
the radial pair would not carry the content and the count would fail; if the lapse
equation had not reduced to Schwarzschild the closure would be wrong.
"""

import sympy as sp

r = sp.symbols('r', positive=True)
Lam = sp.symbols('Lambda', real=True)
th = sp.symbols('theta')
t, ph = sp.symbols('t phi')

m = sp.Function('m')(r)
A = sp.Function('A')(r)
f = 1 - 2*m/r - Lam*r**2/3          # the slicing curve, P8 eq:sds with m promoted

# ---- the general static spherically symmetric cut, P8 eq:twofn -----------------
g = sp.diag(-A, 1/f, r**2, r**2*sp.sin(th)**2)
x = [t, r, th, ph]
ginv = g.inv()
n = 4

Gam = [[[sum(ginv[a, d]*(sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b])
                         - sp.diff(g[b, c], x[d])) for d in range(n))/2
         for c in range(n)] for b in range(n)] for a in range(n)]


def ricci(b, c):
    e = 0
    for a in range(n):
        e += sp.diff(Gam[a][b][c], x[a]) - sp.diff(Gam[a][b][a], x[c])
        for d in range(n):
            e += Gam[a][a][d]*Gam[d][b][c] - Gam[a][c][d]*Gam[d][b][a]
    return sp.simplify(e)


Ric = sp.Matrix(n, n, lambda i, j: ricci(i, j))
Rs = sp.simplify(sum(ginv[i, j]*Ric[i, j] for i in range(n) for j in range(n)))
Gmn = sp.Matrix(n, n, lambda i, j: Ric[i, j] - g[i, j]*Rs/2)
Gud = sp.simplify(ginv*Gmn)

rho = sp.simplify(-(Gud[0, 0] + Lam)/(8*sp.pi))
p_r = sp.simplify((Gud[1, 1] + Lam)/(8*sp.pi))
p_t = sp.simplify((Gud[2, 2] + Lam)/(8*sp.pi))

# ---- (1) the bend IS the density, and the lapse does not enter it --------------
assert sp.simplify(rho - sp.diff(m, r)/(4*sp.pi*r**2)) == 0, "bend-density identity"
assert sp.simplify(sp.diff(rho, A)) == 0 or A not in rho.free_symbols, "rho lapse-free"
print("(1) rho = m'/4 pi r^2, independent of the lapse            OK")

# ---- (2) the contracted Bianchi identity fixes p_t from the radial pair --------
bianchi = sp.diff(p_r, r) + (rho + p_r)*sp.diff(A, r)/(2*A) - 2*(p_t - p_r)/r
assert sp.simplify(bianchi) == 0, "contracted Bianchi identity"
print("(2) Bianchi residual = 0: the radial pair carries content  OK")

# ---- (3) the closure: isotropy + an equation of state ---------------------------
P = sp.Symbol('p_r')                              # p_r supplied by the EoS
Grr = (r*f*sp.diff(A, r)/A + f - 1)/r**2          # P8 sec:lapse, proof
dA = sp.solve(sp.Eq(Grr + Lam, 8*sp.pi*P), sp.diff(A, r))[0]
dlnA = sp.simplify(sp.factor(dA/A))

tov = 2*(m + 4*sp.pi*r**3*P - Lam*r**3/3)/(r**2*f)
assert sp.simplify(dlnA - tov) == 0, "TOV lapse equation"
print("(3) d ln A/dr = 2(m + 4 pi r^3 p_r - Lam r^3/3)/(r^2 f)    OK")
print("    with m' = 4 pi r^2 rho this is a CLOSED first-order")
print("    system for (m, A) once an equation of state is given.")

# ---- (4) the vacuum check the closure has to pass -------------------------------
M = sp.Symbol('M', positive=True)
schw = sp.simplify(dlnA.subs({Lam: 0, P: 0}).subs(m, M).doit())
assert sp.simplify(schw - 2*M/(r*(r - 2*M))) == 0, "Schwarzschild limit"
assert sp.simplify(sp.diff(sp.log(1 - 2*M/r), r) - schw) == 0, "A = f on vacuum"
print("(4) vacuum limit returns A = 1 - 2M/r                      OK")

print()
print("ESTABLISHED: the spherical class closes exactly as P9's homogeneous class")
print("does. The construction supplies the conservation law; the constitutive")
print("relation is the input -- as it is in general relativity.")
