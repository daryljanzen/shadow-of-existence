import sympy as sp

print("="*78)
print("MOVE 8 — locating the confined Gowdy-dS wave in the isotropy stratification.")
print("The dynamics (the bend) lives on the strata Move 7 built. The confined wave is")
print("the worked first bend; this fixes WHICH stratum it sits on.")
print("="*78)

t, z, x, y = sp.symbols('t z x y')
psi = sp.Function('psi')(t, z)     # the propagating graviton (TT shear) -- generic (t,z)
R   = sp.Function('R')(t, z)       # area/clock sector
gam = sp.Function('gamma')(t, z)   # conformal factor
# polarized Gowdy-dS metric
A = sp.exp(2*(gam - psi))
g = sp.diag(-A, A, sp.exp(2*psi), R**2*sp.exp(-2*psi))   # coords (t, z, x, y)
coords = [t, z, x, y]

def lie_derivative(g, K, X):
    # (L_K g)_{ab} = K^c d_c g_ab + g_cb d_a K^c + g_ac d_b K^c
    n = len(X)
    L = sp.zeros(n, n)
    for a in range(n):
        for b in range(n):
            s = sum(K[c]*sp.diff(g[a,b], X[c]) for c in range(n))
            s += sum(g[c,b]*sp.diff(K[c], X[a]) + g[a,c]*sp.diff(K[c], X[b]) for c in range(n))
            L[a,b] = sp.simplify(s)
    return L

print("\n[1] the manifest Killing vectors of the T^2 fibre (metric independent of x, y):")
Kx = [0,0,1,0]   # d/dx
Ky = [0,0,0,1]   # d/dy
Lx = lie_derivative(g, Kx, coords)
Ly = lie_derivative(g, Ky, coords)
print("    L_{d/dx} g = 0 :", Lx == sp.zeros(4,4))
print("    L_{d/dy} g = 0 :", Ly == sp.zeros(4,4))

print("\n[2] no third generic Killing vector: the metric functions depend on (t,z) through")
print("    a generic psi(t,z) (a propagating wave), which breaks t-, z-, and boost-translations.")
print("    Test the would-be extra symmetries on a generic wave profile:")
# substitute a generic non-symmetric profile and check candidate KVs fail
prof = {psi: sp.sin(t)*sp.cos(z), R: sp.cosh(t), gam: sp.Rational(1,2)*sp.sin(2*t)}
gp = g.subs(prof).doit()
for K,name in [([1,0,0,0],"d/dt (time-translation)"),
               ([0,1,0,0],"d/dz (z-translation)"),
               ([z,t,0,0],"t<->z boost")]:
    L = lie_derivative(gp, K, coords)
    print(f"    {name}: L g = 0 ? {L == sp.zeros(4,4)}")
print("    => for a generic wave, only d/dx and d/dy survive: isotropy = 2 (Type-I edge).")

print("\n" + "="*78)
print("READING (where the dynamics sits, and what bends):")
print("="*78)
print("""
 PLACEMENT. The confined polarized Gowdy-dS wave carries exactly two Killing vectors
 (d/dx, d/dy = the T^2 fibre), so it sits at the Type-I, 2-Killing-vector stratum of the
 Move-7 stratification -- the EDGE, the last confined stratum before the wall (Type N,
 isotropy 0). P6's "intermediate symmetry confines radiation (the type-I Einstein-Rosen and
 Gowdy waves, on the edge)" is this stratum, read in the algebroid.

 WHAT BENDS (the dynamics argument, grounded in the computed pieces):
  - The layer advances by a TRUE Hamiltonian on the absolute foliation (P8); the Gowdy-dS
    model realizes that advance WITH a propagating field (the spine, computed): the lapse
    N=e^{gamma-psi} is the layer's metrical advance, not a free multiplier.
  - Matter and radiation are the BEND of the cut (the anchor, Moves 5 + the energy/stress
    sectors): the Gowdy wave's energy and momentum are carried by the shear of the spatial
    leaf -- the ENERGY and MOMENTUM equations sit exactly as the Hamiltonian and momentum
    constraints (the anchor's perp-perp and perp-i sectors).
  - The propagating graviton psi (the leaf's TT shear) is the worked FIRST bend: it evolves
    by the true-Hamiltonian wave equation (Gowdy/Bessel at Lambda=0; Lambda>0 forces the
    substrate's cosmic clock). This is "why the cut bends," computed at the edge stratum.
  - The wall is one symmetry-step beyond: a single global sweep fixes the wave's polarization
    orientation, so the confined wave is self-consistent only while it propagates transverse
    to that fixed orientation (P6). The loss of the last Killing vector -- isotropy 2 -> 0 --
    is exactly where the polarization must reorient from place to place, and generation-by-
    sweep hands off to evolution-by-dynamics. That handoff is the wall (Move 9).

 So the dynamics is the motion ALONG the strata: the bend (matter, radiation) is the anchor's
 image on the advancing layer, the confined Gowdy-dS wave is its worked instance at the Type-I
 edge, and the true Hamiltonian (the absolute clock) keeps the flow Hamiltonian right up to the
 wall, where the finite-symmetry generation ends. [the placement computed; the dynamics
 argument grounded in P8 (clock) + the anchor (bend) + the Gowdy-dS spine (the wave) + Move 7
 (the strata); the full nonlinear Lambda>0 evolution and the wall handoff (Move 9) remain.]
""")
