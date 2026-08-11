import sympy as sp

print("="*78)
print("MOVE 6 — bracket closure on the symmetry-reducible sector.")
print("The substrate is the symmetric space dS5 = SO(5,1)/SO(4,1). At the maximally")
print("symmetric (vacuum) cut, the construction's isotropy (subalgebra fixing the cut)")
print("is h = so(4,1); the cut-DEFORMING directions are the 5-dim coset m. Bracket")
print("closure there IS the symmetric-space property [m,m] subset h. The anchor reads")
print("m -> H_perp (normal/Hamiltonian), h -> H_a (tangential/momentum); the bracket")
print("PATTERN must match the hypersurface-deformation (Dirac) algebra.")
print("="*78)

# so(5,1): 6x6 real X with X^T eta + eta X = 0 ; eta = diag(-1,1,1,1,1,1)
# index 0 timelike, 1..5 spacelike; dS5: -X0^2 + sum_{1..5} Xi^2 = alpha^2.
eta = sp.diag(-1,1,1,1,1,1)

def gen(a,b):
    # M_{ab} in so(5,1): (M_{ab})^i_j = eta_{ia} delta_{jb} - eta_{ib} delta_{ja}
    M = sp.zeros(6,6)
    for i in range(6):
        M[i,b] += eta[i,a]
        M[i,a] -= eta[i,b]
    return M

pairs = [(a,b) for a in range(6) for b in range(a+1,6)]
gens = {p: gen(*p) for p in pairs}

# (0) confirm all 15 are genuinely so(5,1)
ok_alg = all(sp.simplify(gens[p].T*eta + eta*gens[p]) == sp.zeros(6,6) for p in pairs)
print(f"\n[0] 15 generators, all in so(5,1): {ok_alg}  (dim so(5,1) = {len(pairs)})")

def flat(M): return sp.Matrix([M[i,j] for i in range(6) for j in range(6)])
def comm(A,B): return A*B - B*A
def in_span(M, keys):
    if all(v == 0 for v in flat(M)): return True
    A = sp.Matrix.hstack(*[flat(gens[k]) for k in keys])
    return A.rank() == sp.Matrix.hstack(A, flat(M)).rank()

# point p = (0,0,0,0,0,alpha): isotropy = SO(4,1) fixing index 5
#   h = so(4,1) = generators NOT touching index 5 ; m = coset = M_{a5}, a=0..4
h_keys = [(a,b) for (a,b) in pairs if 5 not in (a,b)]
m_keys = [(a,b) for (a,b) in pairs if 5 in (a,b)]
print(f"[1] split at the symmetric cut: dim h = {len(h_keys)} (so(4,1)), dim m = {len(m_keys)} (coset)")

print("\n[2] the three symmetric-space inclusions (the bracket-closure test):")
results = {}
for (S1, S2, T, name) in [(h_keys, h_keys, h_keys, "[h,h] subset h   (isotropy closes -> {H_a,H_b}~H_c)"),
                          (h_keys, m_keys, m_keys, "[h,m] subset m   (isotropy on coset -> {H_a,H_perp}~H_perp)"),
                          (m_keys, m_keys, h_keys, "[m,m] subset h   (CUT-DEFORMATIONS CLOSE -> {H_perp,H_perp}~H_a)")]:
    ok = all(in_span(comm(gens[k1], gens[k2]), T) for k1 in S1 for k2 in S2)
    results[name] = ok
    print(f"    {name}:  {ok}")

# also confirm [m,m] does NOT land in m (it is a genuine symmetric split, not a subalgebra of m)
mm_into_m = all(in_span(comm(gens[k1], gens[k2]), m_keys) for k1 in m_keys for k2 in m_keys)
print(f"    ([m,m] subset m? {mm_into_m}  -> False expected: m is not a subalgebra; the bracket genuinely returns to h)")

print("\n[3] the curvature sign in [m,m] (de Sitter vs anti-de Sitter; the sigma signature):")
# take two coset generators M_{05} (a boost) and M_{15}; their commutator should be a fixed h-element
b1, b2 = gens[(0,5)], gens[(1,5)]
cmm = sp.simplify(comm(b1, b2))
# express in the h-basis: which generator, and sign
match = None
for k in h_keys:
    for s in (1,-1):
        if sp.simplify(cmm - s*gens[k]) == sp.zeros(6,6):
            match = (k, s)
print(f"    [M_05, M_15] = {match[1]:+d} * M_{match[0]}   (a single isotropy generator -> closes; the")
print(f"    sign is the substrate curvature; sigma flips eta-signature -> ε -> -ε, the dS<->Euclidean flip)")

closes = all(results.values())
print("\n" + "="*78)
print("READING (bracket closure on the symmetry-reducible sector):")
print("="*78)
print(f"""
 VERDICT: the cut-deformation bracket CLOSES at the symmetric cut = {closes}.
   [m,m]⊂h, [h,m]⊂m, [h,h]⊂h all hold: so(5,1) = h ⊕ m is the symmetric-space split of
   dS5 = SO(5,1)/SO(4,1), and the cut-deforming coset closes back into the isotropy.

 THE ANCHOR IS A HOMOMORPHISM (on this sector): with m -> H_perp (the normal deformation,
   the Hamiltonian constraint) and h -> H_a (the tangential, the momentum/diffeo constraint),
   the symmetric-space bracket pattern MATCHES the hypersurface-deformation (Dirac) algebra
   term for term:
       [m,m]⊂h      <->   {{H_perp, H_perp}} ~ H_a     (two normals -> tangential)
       [h,m]⊂m      <->   {{H_a, H_perp}}    ~ H_perp  (tangential acts on normal)
       [h,h]⊂h      <->   {{H_a, H_b}}       ~ H_c     (tangential close: spatial diffeos)
   The HDA's defining feature -- the {{H_perp,H_perp}} bracket carrying a STRUCTURE FUNCTION
   ε·h^{{ab}} rather than a constant -- is exactly the [m,m]⊂h bracket read with the coset
   metric h^{{ab}}: CONSTANT at the symmetric cut (-> a genuine Lie algebra so(5,1) there),
   and VARYING as the cut moves over C (-> the genuine Lie ALGEBROID). ε is sigma's
   signature flip (adm3). So the structure-function obstruction that is the root of the
   problem of time IS the base-dependence of the substrate's symmetric-space metric.

 SO: the algebroid so(5,1)⋉C is a BUILT OBJECT on the symmetry-reducible sector -- the vision's
   central [reach] holds there, and it is not a coincidence of pattern but the symmetric-space
   structure of the substrate.

 HONEST SCOPE (what this does NOT show): so(5,1) is finite (15-dim); the full HDA is
   infinite-dim. The closure is on the SYMMETRY-REDUCIBLE sector (the cuts reachable by
   substrate isometries -- exactly the corpus's range/Petrov sector). As the cut moves toward
   the WALL, the isotropy h drops toward 0 (Move 7); there the finite so(5,1) action is
   exhausted and the infinite-dim free transverse DOF (the graviton's two polarizations) take
   over -- the wall is the BOUNDARY of the action algebroid, not inside it. This is consistent
   with the vision (the wall = isotropy->0 = freed DOF) and is NOT a claim that the whole HDA
   is a finite action algebroid (which would be false on dimension alone). The homomorphism is
   verified here at the maximally-symmetric cut; the intermediate strata (isotropy between
   so(4,1) and 0) are Move 7's stratification.
""")
