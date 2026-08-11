import sympy as sp

print("="*78)
print("MOVE 9 — the wall's metric-singular species (the pass-through test).")
print("P1: a METRIC SINGULARITY is a Killing horizon -- a Killing field chi gone null,")
print("|chi|^2=0, generators of zero invariant spatial extent. It REQUIRES a degenerating")
print("Killing vector. Test the wall (Type N, isotropy 0) against that definition.")
print("="*78)

M, al, r, La = sp.symbols('M alpha r Lambda', positive=True)
f = 1 - 2*M/r - r**2/al**2          # SdS, Lambda = 3/alpha^2

print("\n[A] THE CONTRAST CASE — the horizon IS a finite-curvature metric singularity.")
# (1) the timelike Killing vector xi = d/dt has |xi|^2 = g_tt = -f ; |xi|^2 = 0 at a horizon.
xi2 = -f                            # |xi|^2 = g_tt
print("    |xi|^2 = g_tt = -f = ", sp.expand(xi2), "  -> vanishes exactly where f=0 (a HORIZON).")
print("    => at the horizon the Killing vector xi goes null (|xi|^2=0): a KILLING HORIZON.")

# (2) finite curvature there: Kretschmann of SdS.
t, th, ph = sp.symbols('t theta phi')
g = sp.diag(-f, 1/f, r**2, r**2*sp.sin(th)**2)
X = [t, r, th, ph]; gi = g.inv()
Ga=[[[sp.simplify(sum(gi[a,d]*(sp.diff(g[d,b],X[c])+sp.diff(g[d,c],X[b])-sp.diff(g[b,c],X[d]) ) for d in range(4))/2) for c in range(4)] for b in range(4)] for a in range(4)]
# Riemann R^a_{bcd}
Rm=sp.MutableDenseNDimArray.zeros(4,4,4,4)
for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                s=sp.diff(Ga[a][b][d],X[c])-sp.diff(Ga[a][b][c],X[d])
                for e in range(4):
                    s+=Ga[a][c][e]*Ga[e][b][d]-Ga[a][d][e]*Ga[e][b][c]
                Rm[a,b,c,d]=sp.simplify(s)
# lower: R_{abcd}
Rl=sp.MutableDenseNDimArray.zeros(4,4,4,4)
for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                Rl[a,b,c,d]=sp.simplify(sum(g[a,e]*Rm[e,b,c,d] for e in range(4)))
# Kretschmann K = R_{abcd} R^{abcd}
Rup=sp.MutableDenseNDimArray.zeros(4,4,4,4)
for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                Rup[a,b,c,d]=sp.simplify(sum(gi[a,e]*gi[b,fa]*gi[c,gg]*gi[d,hh]*Rl[e,fa,gg,hh]
                                             for e in range(4) for fa in range(4) for gg in range(4) for hh in range(4)))
K = sp.simplify(sum(Rl[a,b,c,d]*Rup[a,b,c,d] for a in range(4) for b in range(4) for c in range(4) for d in range(4)))
print("    Kretschmann K =", K)
print("    => at any horizon r_h>0 (f=0), K is FINITE (a function of r_h>0): FINITE curvature.")
print("    So the horizon is the FINITE-CURVATURE metric singularity (P1): worldlines pass THROUGH,")
print("    and the freed null direction (the degenerating xi) is reassignable as the E=1 clock (NBC).")

print("\n[B] THE WALL — Type N, isotropy 0.")
print("    By Move 7 / P6 the wall has NO continuous isometry (isotropy = 0): there is NO Killing")
print("    vector chi, hence NO locus |chi|^2=0, hence NO Killing horizon.")
print("    Type N is vacuum with finite Weyl: NO infinite-curvature (r=0-type) singularity either.")
print("    de Sitter has no null Killing vector (pastwall_nullshear/typeN), so the freed Type-N null")
print("    direction is the CHARACTERISTIC of ordinary evolution, not a degenerating isometry.")
print("    => the wall satisfies NEITHER metric-singularity species: it is NOT a metric singularity.")

print("\n" + "="*78)
print("VERDICT — branch (c): the wall is a REGULAR RADIATIVE BOUNDARY, not a metric singularity.")
print("="*78)
print("""
 A metric singularity (P1) is a Killing horizon: it requires a Killing vector that goes null,
 whose freed direction the NBC move reassigns as the new timelike clock. That is the
 cosmogenesis mechanism, and it is intact where it lives -- at the Killing horizons:
   * the NBC cosmogenesis horizon (P1/P7): |xi|^2=0, finite curvature, pass-through, the clock
     re-founds (branch a);
   * Nariai (the double-root Killing horizon, the inner seam): the merging Killing horizons,
     also a metric singularity of this species.
 The WALL is a different species. It is the loss of ALL continuous symmetry -- no Killing
 vector, so no Killing horizon, so no metric singularity (neither finite- nor infinite-curvature).
 The geometry there is curvature-regular, and the freed null direction is a propagation
 characteristic of ordinary inhomogeneous evolution, not a degenerating isometry (de Sitter has
 no null Killing vector to supply it). The pass-through / NBC-reassignment frame has no
 Killing vector to act on: the stratum-crossing cosmogenesis frame DOES NOT APPLY at the wall.

 So Move 9 returns branch (c), and it SHARPENS rather than breaks the picture:
   - the singular strata are NOT one species. The cosmogenesis seams -- where a clock re-founds --
     are the KILLING-HORIZON metric singularities (the NBC horizon; Nariai). Cosmogenesis-as-
     template is intact THERE.
   - the WALL is the operator's generative boundary: a regular radiative boundary where
     generation-by-sweep hands off to ordinary evolution. "Why the cut bends past the wall" is
     ordinary inhomogeneous dynamics -- a different question than cosmogenesis.
   - the vision's Entry-4 lumping of the wall with the cosmogenesis singular strata NARROWS: the
     wall is a regular boundary, not a seam where a clock re-founds.
 [computed: the horizon Killing-horizon condition + finite Kretschmann (finite-curvature metric
 singularity); the wall has no KV (Move 7/P6) so no Killing horizon. established: P1's definition,
 the NBC mechanism. reading: that the wall therefore carries no cosmogenesis -- it is the
 generative boundary, ordinary evolution past it (consistent with P6's "perfectly regular Type-N").]
""")
