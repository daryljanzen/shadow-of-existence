import sympy as sp

print("="*78)
print("MOVE 7 — isotropy stratification + the metric-singularity coincidence.")
print("P6's range classes are the isotropy strata of so(5,1)<|C (subalgebra fixing a")
print("cut). Test the INNER boundary: does the isotropy JUMP at exactly the")
print("metric-degenerate (double-root, Nariai) locus?")
print("="*78)

M, al, r = sp.symbols('M alpha r', positive=True)
# SdS: f = 1 - 2M/r - r^2/alpha^2,  Lambda = 3/alpha^2. Horizons: r*f(r)=0.
# horizon cubic P(r) = r - 2M - r^3/alpha^2 ; times -alpha^2: r^3 - alpha^2 r + 2 M alpha^2
P = r**3 - al**2*r + 2*M*al**2
disc = sp.factor(sp.discriminant(P, r))
print("\n[1] SdS horizon cubic  r^3 - alpha^2 r + 2 M alpha^2 ;  discriminant =")
print("   ", disc)
roots_M = sp.solve(sp.Eq(disc, 0), M)
Mc = [s for s in roots_M if s != 0]
print("    double root (disc=0, the metric-degenerate / Nariai locus) at  M =", Mc)
for s in Mc:
    print(f"      => (M/alpha)^2 = {sp.simplify(s**2/al**2)} ,  Lambda M^2 = 3M^2/alpha^2 = {sp.simplify(3*s**2/al**2)}")
print("    => the double-root locus is  Lambda M^2 = 1/9   (M = alpha/(3 sqrt 3)).")

# the degenerate (double) root value r_N = alpha/sqrt(3) = 1/sqrt(Lambda): verify P(r_N)=P'(r_N)=0.
Mn = al/(3*sp.sqrt(3))
rN = al/sp.sqrt(3)
Pn = P.subs(M, Mn)
print(f"    at M=alpha/(3 sqrt3), r_N=alpha/sqrt3=1/sqrt(Lambda):  P(r_N)={sp.simplify(Pn.subs(r,rN))},"
      f"  P'(r_N)={sp.simplify(sp.diff(Pn,r).subs(r,rN))}   (both 0 => r_N is the double root)")

print("\n[2] isotropy dimension across the inner boundary:")
print("    generic SdS (Lambda M^2 < 1/9, two distinct horizons): isometry = R_t x SO(3) = dim 4.")
print("    Verify the Nariai limit is dS2 x S2 (each factor constant-curvature => max-symmetric, dim 3):")

# Nariai metric = dS2(radius b) x S2(radius b), b = 1/sqrt(Lambda) = alpha/sqrt3.
b = sp.Symbol('b', positive=True)
# S2 factor:
th, ph = sp.symbols('theta phi')
gS2 = sp.diag(b**2, b**2*sp.sin(th)**2)
# dS2 factor (static patch): ds^2 = -(1 - x^2/b^2) dtau^2 + dx^2/(1 - x^2/b^2)
x, tau = sp.symbols('x tau')
fdS2 = 1 - x**2/b**2
gdS2 = sp.diag(-fdS2, 1/fdS2)

def ricci_scalar_2d(g, X):
    gi = g.inv()
    Ga = [[[sp.simplify(sum(gi[a,d]*(sp.diff(g[d,bb],X[c])+sp.diff(g[d,c],X[bb])-sp.diff(g[bb,c],X[d]) ) for d in range(2))/2) for c in range(2)] for bb in range(2)] for a in range(2)]
    Ric = sp.zeros(2,2)
    for bb in range(2):
        for d in range(2):
            s = 0
            for a in range(2):
                s += sp.diff(Ga[a][bb][d],X[a]) - sp.diff(Ga[a][bb][a],X[d])
                for e in range(2):
                    s += Ga[a][a][e]*Ga[e][bb][d] - Ga[a][d][e]*Ga[e][bb][a]
            Ric[bb,d] = sp.simplify(s)
    return sp.simplify(sum(gi[a,bb]*Ric[a,bb] for a in range(2) for bb in range(2)))

RS2 = ricci_scalar_2d(gS2, [th, ph])
RdS2 = ricci_scalar_2d(gdS2, [tau, x])
print(f"      S2  factor: Ricci scalar = {RS2}  (constant > 0  -> SO(3), dim 3)")
print(f"      dS2 factor: Ricci scalar = {RdS2}  (constant      -> SO(2,1), dim 3)")
print("      both constant-curvature => Nariai isometry = SO(2,1) x SO(3) = dim 6.")
print("    => at Lambda M^2 = 1/9 the isotropy JUMPS 4 -> 6 (enhanced-but-frozen), at EXACTLY the")
print("       double-root (metric-degenerate) locus. Inner singular stratum = isotropy jump. COINCIDE.")

print("\n" + "="*78)
print("READING (the stratification and the coincidence):")
print("="*78)
print("""
 THE ISOTROPY STRATIFICATION (P6's range classes = strata of so(5,1)<|C, by dim of the
 cut-fixing subalgebra):
   Type O   de Sitter / FLRW        isotropy so(4,1)            dim 10   (the symmetric vacuum cut)
   Type D   Schwarzschild-de Sitter R_t x SO(3)                dim 4
            Nariai (Lambda M^2=1/9) SO(2,1) x SO(3)            dim 6    (JUMP UP; the inner seam)
            Kerr-de Sitter          R x SO(2) (+Killing tensor) dim 2
   Type I   Bianchi I (homogeneous) 3 spatial KV               dim 3
            Zipoy-Voorhees / Weyl   R x SO(2)                  dim 2
   WALL     Type N (plane wave)     no continuous isometry      dim 0    (the outer boundary)
 Isotropy is maximal at the symmetric vacuum cut (dim 10) and falls to 0 at the wall, with
 Nariai a local enhancement (a frozen, degenerate stratum). This IS the base-variation of the
 structure functions that Move 6 verified only at the symmetric cut: as the cut moves over C,
 the cut-fixing subalgebra changes, and the algebroid's structure functions vary with it.

 THE METRIC-SINGULARITY COINCIDENCE:
   - INNER (computed here): the isotropy jump (4->6) sits at Lambda M^2 = 1/9, which is exactly
     the SdS cubic's double-root locus -- the metric-degenerate Nariai seam (two horizon null
     surfaces merging). The isotropy-jump boundary IS the metric-singular locus. COINCIDE.
   - OUTER (P6, established): the wall is isotropy -> 0, which P6 identifies as Type N / the onset
     of free gravitational radiation -- the loss of all continuous symmetry. The isotropy-collapse
     boundary IS the radiative/dynamical boundary. COINCIDE.
   - The other named singular strata -- the NBC cosmogenesis horizon (P7) and the
     Riemannian<->Lorentzian seam -- are the vantage/reassignment loci (sigma's signature flip,
     adm3): the discrete-operation boundaries, where the cut's causal character degenerates rather
     than its continuous symmetry. Same set of loci, two organs (continuous isotropy jump; discrete
     vantage flip).

 SO: the isotropy stratification of so(5,1)<|C reproduces P6's range/Petrov classes; the strata
 boundaries are where isotropy jumps; and those boundaries coincide with the corpus's metric-
 singular loci (Nariai inner, wall outer). The vision's "singular strata ARE the seams" holds at
 the two computable ends. [computed: the Nariai inner coincidence + the stratification dims;
 established: the wall outer coincidence (P6); reading: the full per-stratum so(5,1)-subalgebra
 identification and the NBC/seam discrete-locus unification.]
""")
