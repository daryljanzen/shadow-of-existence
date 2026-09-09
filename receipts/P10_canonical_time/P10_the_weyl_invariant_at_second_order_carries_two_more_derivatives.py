"""
P10_the_weyl_invariant_at_second_order_carries_two_more_derivatives
===================================================================

Object under test -- `PO-43`, "the Weyl-squared coefficient at second order in the
shear", discharged by that coefficient "with the sub-leading heat-kernel
coefficients, which is the instrument P10 names and stopped short of running".

The coefficient multiplies an invariant, so the invariant is the first thing to fix.
`P10` states it in one clause:

    "an anisotropic shear of amplitude sigma over an isotropic expansion gives
     C^2 = 4 sigma^2 + O(sigma^4)"

** COMPUTED HERE, AND IT IS NOT THAT SHAPE. **  For the general anisotropic metric
over an isotropic expansion,

    ds^2 = -dt^2 + a(t)^2 sum_i exp(2 eps beta_i) dx_i^2 ,   sum_i beta_i = 0 ,

the Weyl-squared invariant at second order in the amplitude is

    ** C^2 = 2 eps^2 sum_i ( beta_i'' + H beta_i' )^2 + O(eps^3) ,   H = a'/a **

i.e., writing the shear as sigma_i = eps beta_i',

    ** C^2 = 2 sum_i ( sigma_i' + H sigma_i )^2 . **

TWO THINGS FOLLOW, AND THE SECOND IS WHAT `PO-43` NEEDS.

  (1) ** DIMENSIONS. **  A shear has dimension 1/time, so sigma^2 is 1/L^2 while
      C^2 is 1/L^4.  "C^2 = 4 sigma^2" cannot be right with sigma the shear; read
      instead with sigma a dimensionless amplitude, the computed coefficient is not
      4 and the structure is not sigma^2.  ** Either way the stated form does not
      survive the computation, and the clause wants checking at source. **

  (2) ** THE INVARIANT CARRIES TWO MORE DERIVATIVES THAN THE ROW ASSUMES, and that
      is the whole difference for a TOWER. **  For a mode of frequency omega the
      shear oscillates, so sigma' ~ omega sigma and C^2 ~ omega^2 sigma^2.  The
      counterterm therefore multiplies a quantity that grows with the mode's
      frequency -- which is what makes it ultraviolet-sensitive at all, and what a
      sigma^2-shaped invariant would not be.  ** A discharge computed against
      4 sigma^2 would be computing the coefficient of the wrong object. **

  ⌗ AND A CASE THAT SEPARATES THEM CLEANLY: a CONSTANT comoving shear on a static
    background (sigma' = 0, H = 0) gives C^2 = 0 at this order, where 4 sigma^2
    would give 4 sigma^2.  ** The two forms disagree on whether a constant shear
    curves the Weyl tensor at all. **

METHOD.  The invariant is computed from the metric with no expansion assumed --
Christoffels, Riemann, Ricci, scalar, Weyl, then the full contraction -- and the
closed form above is checked against that exact expression at three decreasing
amplitudes, the ratio converging to 1 linearly in eps (1.0404, 1.0040, 1.00040 at
eps = 1e-2, 1e-3, 1e-4).  ** The closed form is READ OFF one computation and
VERIFIED against another, rather than asserted from either. **

NOT ESTABLISHED: the coefficient itself.  That is `PO-43`'s object and needs the
sub-leading heat-kernel coefficients for the tower's own operator.  ** What this
fixes is what they multiply. **  It also does not touch `PO-23`, whose log lives on
the degenerate combination and which `PO-43` already distinguishes.
"""

import sympy as sp

t, e = sp.symbols('t'), sp.symbols('epsilon', positive=True)
x = [t] + list(sp.symbols('x y z'))
n = 4


def weyl_squared(a_expr, betas):
    """C_{abcd}C^{abcd} for ds^2 = -dt^2 + a^2 sum_i exp(2 eps beta_i) dx_i^2."""
    B = [e*b for b in betas]
    g = sp.diag(-1, *[a_expr**2*sp.exp(2*bb) for bb in B])
    gi = g.inv()
    Gam = [[[sum(gi[i, l]*(sp.diff(g[l, j], x[k]) + sp.diff(g[l, k], x[j])
                           - sp.diff(g[j, k], x[l])) for l in range(n))/2
             for k in range(n)] for j in range(n)] for i in range(n)]

    def riem(i, j, k, l):
        r = sp.diff(Gam[i][j][l], x[k]) - sp.diff(Gam[i][j][k], x[l])
        for m in range(n):
            r += Gam[i][k][m]*Gam[m][j][l] - Gam[i][l][m]*Gam[m][j][k]
        return r

    R4 = [[[[riem(i, j, k, l) for l in range(n)] for k in range(n)]
           for j in range(n)] for i in range(n)]
    Rd = [[[[sum(g[i, m]*R4[m][j][k][l] for m in range(n)) for l in range(n)]
            for k in range(n)] for j in range(n)] for i in range(n)]
    Ric = sp.Matrix(n, n, lambda j, l: sum(R4[i][j][i][l] for i in range(n)))
    Rs = sum(gi[j, l]*Ric[j, l] for j in range(n) for l in range(n))
    W = [[[[Rd[i][j][k][l]
            - (g[i, k]*Ric[j, l] - g[i, l]*Ric[j, k]
               - g[j, k]*Ric[i, l] + g[j, l]*Ric[i, k])/2
            + Rs*(g[i, k]*g[j, l] - g[i, l]*g[j, k])/6
            for l in range(n)] for k in range(n)] for j in range(n)] for i in range(n)]
    tot = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    up = sum(gi[i, p]*gi[j, q]*gi[k, r]*gi[l, s]*W[p][q][r][s]
                             for p in range(n) for q in range(n)
                             for r in range(n) for s in range(n))
                    tot += W[i][j][k][l]*up
    return tot


def closed_form(a_expr, betas):
    """2 eps^2 sum_i (beta_i'' + H beta_i')^2."""
    H = sp.diff(a_expr, t)/a_expr
    return 2*e**2*sum((sp.diff(b, t, 2) + H*sp.diff(b, t))**2 for b in betas)


# --- generic background, generic anisotropy, nothing tuned ------------------------
a = sp.cosh(t)
b1, b2 = sp.sin(2*t), sp.cos(3*t)
betas = [b1, b2, -(b1 + b2)]

C2 = weyl_squared(a, betas)
cand = closed_form(a, betas)

print("  amplitude      C^2 exact      2 sum (b'' + H b')^2        ratio")
print("  " + "-"*64)
prev = None
for ev in (1e-2, 1e-3, 1e-4):
    ex = float(C2.subs({e: ev, t: 0.7}).evalf())
    ca = float(cand.subs({e: ev, t: 0.7}).evalf())
    print(f"  {ev:>9.0e}{ex:>15.7e}{ca:>22.7e}{ex/ca:>13.6f}")
    if prev:
        assert abs(ex/ca - 1) < abs(prev - 1), "the ratio must improve as eps falls"
    prev = ex/ca
assert abs(prev - 1) < 1e-3, "the closed form must be the eps->0 limit"
print("\n  -> ratio -> 1 linearly in eps: the closed form is verified      OK")

# --- the case that separates the two forms ---------------------------------------
c = sp.Symbol('c')
flat, lin = sp.Integer(1), [c*t, -c*t, sp.Integer(0)]      # constant shear, static
assert sp.simplify(closed_form(flat, lin)) == 0
C2_lin = sp.simplify(sp.series(sp.expand(weyl_squared(flat, lin)), e, 0, 3).removeO())
assert sp.simplify(C2_lin) == 0
print("  constant comoving shear on a static background: C^2 = 0 at O(eps^2)")
print("  -- where 4 sigma^2 would give 4 sigma^2                        OK")

print()
print("ESTABLISHED: C^2 = 2 sum_i (sigma_i' + H sigma_i)^2 at second order --")
print("two more derivatives than 4 sigma^2, and the right dimension (1/L^4).")
print("For a mode of frequency omega this is ~ omega^2 sigma^2, which is what")
print("makes the counterterm ultraviolet-sensitive at all.")
print("NOT ESTABLISHED: the coefficient. This fixes what it multiplies.")
