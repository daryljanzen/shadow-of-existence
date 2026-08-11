"""
MOVE-8 handoff (carrier level) -- the intrinsic curvature is the single carrier of the
bend across the static/dynamical divide.

Steps 1-6 established the STATIC face: the bend (matter density rho) sits in the slicing
surface's intrinsic curvature K_G = 1/alpha^2 - m/r^3 + 4 pi rho (step 1), and its variation
across the moduli C is the algebroid [m,m]->m connection. This script tests the DYNAMICAL
face: does the propagating bend (the Gowdy graviton psi, the leaf's TT shear) sit in the
leaf's intrinsic curvature ^3R the same way, and is its energy in the TRUE Hamiltonian
(gowdy_ds_ham.py) that intrinsic-curvature term?

Result (verified):
  - ^3R of the Gowdy spatial 3-leaf CONTAINS the graviton gradient psi_z^2 -- the propagating
    bend is in the intrinsic curvature.
  - the graviton's potential energy in the Gowdy true Hamiltonian, 2 R psi_z^2, EQUALS the
    lapse-weighted intrinsic-curvature term N sqrt(h) (-^3R) graviton piece (N = e^{gamma-psi}
    the Gowdy lapse) -- both 2R, exact.
So the field-DOF (graviton) energy is carried by the leaf's intrinsic curvature, the same
TYPE of object (intrinsic curvature) that carries static matter (K_G) and whose moduli-
variation is the algebroid connection. The intrinsic curvature is the single carrier of the
bend, static and dynamical alike -- Entry-5's single-carrier picture realized at the
intrinsic-curvature/Hamiltonian level.

Honest scope [reach]:
  - This is a CARRIER-level link (both faces ride on the intrinsic curvature), NOT a proof
    that the algebroid connection literally equals the graviton dynamics as one equation.
  - The FULL reduced Gowdy H is NOT literally sqrt(h)(2 Lambda - ^3R): the area/clock-sector
    terms (R_z gamma_z, R_zz) differ by the reduction's IBP. The clean match is the
    graviton/bend piece (psi_z^2), which is the field-DOF content.
  - SECTOR NOTE (face 14): steps 1-6 are the spherical (SO(3)) sector; the Gowdy edge is the
    planar (T^2) sector. This is the COMMON intrinsic-curvature carrier across sectors, not a
    within-sector continuation of one leaf into the other.
"""
import sympy as sp

z, Lam = sp.symbols('z Lambda', real=True)
psi = sp.Function('psi')(z); gam = sp.Function('gamma')(z); R = sp.Function('R')(z)
x, y = sp.symbols('x y')

# Gowdy-dS spatial 3-leaf (t=const), coords (z,x,y)
g = sp.diag(sp.exp(2*(gam-psi)), sp.exp(2*psi), R**2*sp.exp(-2*psi))
X = [z, x, y]
ginv = g.inv()
n = 3


def christoffel(g, ginv, X):
    G = [[[0]*n for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                G[a][b][c] = sp.simplify(sp.Rational(1, 2)*sum(
                    ginv[a, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                    for d in range(n)))
    return G


def ricci_scalar(G, ginv, X):
    Ric = sp.zeros(n, n)
    for b in range(n):
        for d in range(n):
            s = 0
            for a in range(n):
                s += sp.diff(G[a][b][d], X[a]) - sp.diff(G[a][b][a], X[d])
                s += sum(G[a][a][e]*G[e][b][d] - G[a][d][e]*G[e][b][a] for e in range(n))
            Ric[b, d] = sp.simplify(s)
    return sp.simplify(sum(ginv[b, d]*Ric[b, d] for b in range(n) for d in range(n)))


G = christoffel(g, ginv, X)
R3 = ricci_scalar(G, ginv, X)
pz = sp.Derivative(psi, z)

print("^3R contains the graviton gradient psi_z^2 (propagating bend in the curvature)?",
      R3.has(pz))

sqh = R*sp.exp(gam - psi)            # sqrt(det g3)
N = sp.exp(gam - psi)                # Gowdy lapse
coeff_H = 2*R                        # psi_z^2 coeff in the Gowdy H potential 2 R psi_z^2
coeff_curv = sp.simplify(sp.expand(N*sqh*(-R3)).coeff(pz, 2))
print("graviton energy 2R psi_z^2 == lapse-weighted intrinsic-curvature term N sqrt(h)(-^3R)?",
      sp.simplify(coeff_H - coeff_curv) == 0, "  (both =", coeff_H, ")")
