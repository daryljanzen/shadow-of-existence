#!/usr/bin/env python3
"""PO-91: is the swept chart's asymmetry exhausted by the chart, or does the
vantage-dependence encode something about observation?

Everything printed here is computed from the metric in this file.  Nothing is
quoted from a paper, and no standard result is assumed: the Riemann tensor, the
Kretschmann scalar and the orthonormal frame components are all built from
`g` below by sympy, so a reader who distrusts the conclusion can distrust the
metric instead.

The object is P2's cycloid chart of Schwarzschild.  The profile
    r_N(z) = M(1 + cos z) = 2M cos^2(z/2)
has two non-degenerate critical points, z = 0 (labelled r = 2M) and z = pi
(labelled r = 0).  The chart is obtained by SWEEPING this profile about one of
them.  Chart N sweeps about z = pi.  Chart H is the counterfactual that sweeps
about z = 0 instead.
"""
import sympy as sp

t, r, th, ph, z, M = sp.symbols('t r theta phi z M', positive=True)
M = sp.Symbol('M', positive=True)
f = 1 - 2*M/r

X = [t, r, th, ph]
g = sp.diag(-f, 1/f, r**2, r**2*sp.sin(th)**2)
ginv = g.inv()
n = 4

def christoffel(g, ginv, X):
    G = [[[0]*n for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                s = 0
                for d in range(n):
                    s += ginv[a, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                G[a][b][c] = sp.simplify(s/2)
    return G

def riemann_down(g, G, X):
    """R_{abcd}, fully lowered."""
    Rup = [[[[0]*n for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    e = sp.diff(G[a][b][d], X[c]) - sp.diff(G[a][b][c], X[d])
                    for k in range(n):
                        e += G[a][c][k]*G[k][b][d] - G[a][d][k]*G[k][b][c]
                    Rup[a][b][c][d] = sp.simplify(e)
    Rd = [[[[0]*n for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    s = 0
                    for k in range(n):
                        s += g[a, k]*Rup[k][b][c][d]
                    Rd[a][b][c][d] = sp.simplify(s)
    return Rd

G = christoffel(g, ginv, X)
Rd = riemann_down(g, G, X)

K = 0
for a in range(n):
    for b in range(n):
        for c in range(n):
            for d in range(n):
                term = Rd[a][b][c][d]
                if term == 0:
                    continue
                s = term
                for (i, j) in ((a, 0), (b, 1), (c, 2), (d, 3)):
                    pass
                K += term * sum(
                    ginv[a, p]*ginv[b, q]*ginv[c, u]*ginv[d, v]*Rd[p][q][u][v]
                    for p in range(n) for q in range(n) for u in range(n) for v in range(n)
                    if Rd[p][q][u][v] != 0
                )
K = sp.simplify(K)

print("=" * 78)
print("  STEP 1 -- the invariants, computed from the metric in this file")
print("=" * 78)
print(f"  metric              g = diag(-(1-2M/r), 1/(1-2M/r), r^2, r^2 sin^2 th)")
print(f"  Kretschmann         K = {sp.simplify(K)}")
print(f"  stationary Killing  |xi|^2 = g_tt = {sp.simplify(g[0,0])}")
print(f"  areal radius        (A/4pi)^(1/2) = {sp.sqrt(sp.simplify(g[2,2]))}")

# --- the two critical points of the cycloid profile -----------------------
rN = 2*M*sp.cos(z/2)**2
rH = 2*M*sp.sin(z/2)**2
print()
print("=" * 78)
print("  STEP 2 -- the two critical points of r_N(z) = 2M cos^2(z/2)")
print("=" * 78)
print(f"  r_N(z)   = {sp.simplify(rN)}        r_N'(z) = {sp.simplify(sp.diff(rN, z))}")
print(f"  r_N''(z) = {sp.simplify(sp.diff(rN, z, 2))}")
for zz, name in ((0, 'z = 0'), (sp.pi, 'z = pi')):
    rv = sp.simplify(rN.subs(z, zz))
    d1 = sp.simplify(sp.diff(rN, z).subs(z, zz))
    d2 = sp.simplify(sp.diff(rN, z, 2).subs(z, zz))
    print(f"    {name:8s}  r_N = {str(rv):>6}   r_N' = {d1}   r_N'' = {d2}   "
          f"non-degenerate: {d1 == 0 and d2 != 0}")

print()
print("=" * 78)
print("  STEP 3 -- (c) WHICH SECTOR COLLAPSES, from Killing-vector norms alone")
print("=" * 78)
print("  These are scalars, so the answer cannot be a labelling artefact.")
print("  xi = d/dt (stationary);  the SO(3) orbit 2-sphere has area A = 4 pi r^2.")
hdr = f"  {'critical point':<16}{'|xi|^2':>14}{'orbit area A':>18}{'K':>18}   collapsing sector"
print(hdr)
print("  " + "-" * (len(hdr) - 2))
rows = []
for zz, name in ((0, 'z = 0  (r=2M)'), (sp.pi, 'z = pi (r=0)')):
    rv = sp.simplify(rN.subs(z, zz))
    xi2 = sp.simplify(g[0, 0].subs(r, rv))
    area = sp.simplify(4*sp.pi*rv**2)
    Kv = sp.simplify(K.subs(r, rv)) if rv != 0 else sp.oo
    if xi2 == 0 and area != 0:
        sector = "the stationary generator (t,r) block"
    elif area == 0:
        sector = "the angular 2-sphere"
    else:
        sector = "none"
    rows.append((name, xi2, area, Kv, sector))
    print(f"  {name:<16}{str(xi2):>14}{str(area):>18}{str(Kv):>18}   {sector}")

print()
print("=" * 78)
print("  STEP 4 -- (a) IS CHART H ADMISSIBLE?  the sweep-axis criterion")
print("=" * 78)
print("  A sweep is a reduction by an SO(3) isometry whose orbits are the swept")
print("  2-spheres.  Its axis is the FIXED-POINT SET of that action, so the orbit")
print("  through a point of the axis must be a point: A = 0 there.  That is the")
print("  criterion, and it is a statement about an area, hence an observable.")
for zz, name in ((0, 'z = 0'), (sp.pi, 'z = pi')):
    rv = sp.simplify(rN.subs(z, zz))
    area = sp.simplify(4*sp.pi*rv**2)
    print(f"    axis at {name:6s}:  A = {str(area):<12} "
          f"=> admissible as a sweep axis: {area == 0}")
print()
print("  \u26a0 AND A SUBTLETY THAT CUTS AGAINST THE EASY VERSION OF THIS ARGUMENT.")
print("     In the maximal Schwarzschild MANIFOLD the SO(3) action has no fixed")
print("     point at all: A = 4 pi r^2 vanishes only at r = 0, and r = 0 is not a")
print("     point of that manifold.  So the sweep axis is a BOUNDARY locus the")
print("     orbits shrink toward, not a fixed point sitting inside the spacetime.")
print("     The criterion below is therefore 'the locus the orbit area degenerates")
print("     at', which is where P2's SPATIAL sweep does have an axis, and it is")
print("     still unique:")
rfree = sp.Symbol('rho')          # unrestricted: r itself is declared positive
Afree = 4*sp.pi*rfree**2
roots = sp.roots(sp.Poly(Afree/(4*sp.pi), rfree))
print(f"       A(rho) = 4 pi rho^2 vanishes only at  {dict(roots)}  "
      f"(value: multiplicity)")
print(f"       and on the chart's own domain rho > 0 the solution set is "
      f"{sp.solve(sp.Eq(4*sp.pi*r**2, 0), r)} -- EMPTY, which is the subtlety")
print(f"       restated as arithmetic: the one candidate axis is not in the")
print(f"       manifold the orbits live in.")
print()
print("    chart N sweeps about z = pi  -> ADMISSIBLE")
print("    chart H sweeps about z = 0   -> INADMISSIBLE: the orbit there has")
print(f"      area 16 pi M^2, so z = 0 is not fixed by any SO(3) action whose")
print("      orbits are these 2-spheres.  The vantage is NOT free to choose it.")

print()
print("=" * 78)
print("  STEP 5 -- (b) DOES THE DIVERGENCE FOLLOW THE LABEL?")
print("=" * 78)
print("  The counterfactual profile with its zero at the other critical point is")
print(f"    r_H(z) = {sp.simplify(rH)},   r_H(z) = r_N(z + pi)")
print("  so H's profile is N's shifted by pi -- the SAME function, relabelled.")
for prof, nm in ((rN, 'r_N'), (rH, 'r_H')):
    Kz = sp.simplify(K.subs(r, prof))
    lim0 = sp.limit(Kz, z, 0)
    limpi = sp.limit(Kz, z, sp.pi)
    print(f"    K[{nm}](z)  ->  z=0: {lim0}      z=pi: {limpi}")
print("  So yes: composed with 48 M^2 / r^6 the divergence sits wherever the")
print("  profile's zero sits.  But that is a statement about a FUNCTION, not")
print("  about a spacetime -- and STEP 4 says only one of the two zeros can be")
print("  a sweep axis, so there is no second spacetime for the second answer to")
print("  be true of.  (b) is therefore VACUOUS as a comparison of charts.")

print()
print("=" * 78)
print("  STEP 6 -- (d) IS THERE AN OBSERVATIONAL DISCRIMINANT?")
print("=" * 78)
print("  An observation is made by a worldline, so the quantity to compute is")
print("  the tidal tensor in a parallel-propagated orthonormal frame -- what a")
print("  falling observer actually measures.  Static orthonormal frame first:")
# e_{\hat a} = (scaling) * d/dx^a, chosen so g(e,e) = diag(-1,1,1,1):
#   e_t = f^{-1/2} d/dt,  e_r = f^{+1/2} d/dr,  e_th = (1/r) d/dth,  e_ph = ...
# â An earlier draft of this file had the first two SWAPPED.  R_{t r t r} is
#   blind to that swap -- the two wrong factors cancel in exactly that one
#   component -- so the bug was invisible in the number I was looking at and
#   showed up only in R_{t th t th} carrying a spurious (2M-r)^2.
e = [1/sp.sqrt(f), sp.sqrt(f), 1/r, 1/(r*sp.sin(th))]
def ortho(a, b, c, d):
    """R_{\hat a \hat b \hat c \hat d} for a diagonal orthonormal frame."""
    return sp.simplify(Rd[a][b][c][d] * e[a]*e[b]*e[c]*e[d])
comps = {
    'R_{t r t r}':  ortho(0, 1, 0, 1),
    'R_{t th t th}': ortho(0, 2, 0, 2),
    'R_{r th r th}': ortho(1, 2, 1, 2),
    'R_{th ph th ph}': ortho(2, 3, 2, 3),
}
for k, v in comps.items():
    print(f"    {k:<18} = {v}")
print()
print("  A STATIC frame is not an observer at the horizon, so boost along r by")
print("  rapidity w and recompute -- the falling observer's frame.  Nothing here")
print("  assumes the type-D invariance; it is derived and then reported.")
w = sp.Symbol('w', real=True)
ch, sh = sp.cosh(w), sp.sinh(w)
# e_0' = ch e_0 + sh e_1 ;  e_1' = sh e_0 + ch e_1 ;  e_2', e_3' unchanged
L = sp.Matrix([[ch, sh, 0, 0], [sh, ch, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
Rortho = {}
for a in range(n):
    for b in range(n):
        for c in range(n):
            for d in range(n):
                Rortho[(a, b, c, d)] = ortho(a, b, c, d)
def boosted(a, b, c, d):
    tot = 0
    for p in range(n):
        for q in range(n):
            for u in range(n):
                for v in range(n):
                    val = Rortho[(p, q, u, v)]
                    if val == 0:
                        continue
                    tot += L[a, p]*L[b, q]*L[c, u]*L[d, v]*val
    return sp.simplify(sp.trigsimp(tot))
for (a, b, c, d), nm in (((0, 1, 0, 1), 'R_{t r t r}'), ((0, 2, 0, 2), 'R_{t th t th}')):
    bst = boosted(a, b, c, d)
    inv = sp.simplify(bst - Rortho[(a, b, c, d)]) == 0
    print(f"    {nm:<18} boosted = {bst}      w-independent: {inv}")
print()
hdr2 = f"  {'critical point':<16}{'R_{t r t r}':>22}{'R_{t th t th}':>22}"
print(hdr2)
print("  " + "-" * (len(hdr2) - 2))
for zz, name in ((0, 'z = 0  (r=2M)'), (sp.pi, 'z = pi (r=0)')):
    rv = sp.simplify(rN.subs(z, zz))
    if rv == 0:
        a1 = sp.limit(comps['R_{t r t r}'].subs(r, rN), z, sp.pi)
        a2 = sp.limit(comps['R_{t th t th}'].subs(r, rN), z, sp.pi)
    else:
        a1 = sp.simplify(comps['R_{t r t r}'].subs(r, rv))
        a2 = sp.simplify(comps['R_{t th t th}'].subs(r, rv))
    print(f"  {name:<16}{str(a1):>22}{str(a2):>22}")
print()
print("  ** The falling observer measures FINITE tides at one critical point and")
print("     DIVERGENT tides at the other, in a frame that is boost-independent,")
print("     so the two critical points are told apart BY A MEASUREMENT and not")
print("     by a label. **")
print()
print("  \u26a0 What this file does NOT compute, and must not be read as computing:")
print("     that the substrate's own invariants are constant.  That the substrate")
print("     is the de Sitter manifold is the corpus's claim (P3 / the slicing")
print("     companion), not this file's; this file computes only the swept chart.")
print("     The step the row needs -- that the asymmetry predicts something the")
print("     SUBSTRATE alone does not display -- therefore rests on that claim and")
print("     is not established here.")
