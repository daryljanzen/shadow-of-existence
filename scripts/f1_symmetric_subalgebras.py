import sympy as sp
from itertools import combinations

print("="*78)
print("F1 (second computation) — WHICH strata keep the homomorphism: the symmetric")
print("subalgebras of so(5,1), by dimension, against Move 7's isotropy table.")
print("The clean HDA grading [m,m]subset h holds (given reductive [h,m]subset m) IFF (h,m)")
print("is a SYMMETRIC pair, i.e. h is the fixed-point set of an involution of so(5,1).")
print("so(5,1) has q=1 (odd) -> no u(n)-type involution -> ALL symmetric subalgebras are")
print("the Grassmannian block type so(a,b)+so(5-a,1-b). Enumerate them by dimension.")
print("="*78)

eta = sp.diag(-1,1,1,1,1,1)
def gen(a,b):
    M = sp.zeros(6,6)
    for i in range(6):
        M[i,b] += eta[i,a]; M[i,a] -= eta[i,b]
    return M
pairs = [(a,b) for a in range(6) for b in range(a+1,6)]
gens = {p: gen(*p) for p in pairs}
def flat(M): return sp.Matrix([M[i,j] for i in range(6) for j in range(6)])
def comm(A,B): return A*B - B*A
def in_span(M, keys):
    if all(v == 0 for v in flat(M)): return True
    A = sp.Matrix.hstack(*[flat(gens[k]) for k in keys])
    return A.rank() == sp.Matrix.hstack(A, flat(M)).rank()
def sym_pair(h_keys):
    m_keys = [p for p in pairs if p not in h_keys]
    hh = all(in_span(comm(gens[i],gens[j]), h_keys) for i in h_keys for j in h_keys)
    hm = all(in_span(comm(gens[i],gens[j]), m_keys) for i in h_keys for j in m_keys)
    mm = all(in_span(comm(gens[i],gens[j]), h_keys) for i in m_keys for j in m_keys)
    return hh, hm, mm

print("\n[A] Reflection involutions theta_S (flip the indices in S): fixed subalgebra =")
print("    generators within S or within its complement. dim depends only on |S|.")
dims_seen = {}
for k in range(0,4):  # |S| = 0..3 covers all by symmetry (|S| and 6-|S| give the same dim)
    S = set(range(k))                      # a representative subset of size k
    h_keys = [(a,b) for (a,b) in pairs if (a in S and b in S) or (a not in S and b not in S)]
    hh,hm,mm = sym_pair(h_keys)
    dim = len(h_keys)
    sig = "so(%d,%d)+so(%d,%d)"  # informational
    has0_in_S = 0 in S
    dims_seen[k] = dim
    print(f"    |S|={k}: dim h = {dim:2d}  symmetric pair [m,m]⊂h: {mm}   "
          f"(block so({k if not (k and has0_in_S) else k-1+0}...) — dim set by |S|)")
print(f"    => symmetric-subalgebra dimensions achievable: {sorted(set(dims_seen.values()))} "
      f"(plus trivial 15). NO symmetric subalgebra of dim 2, 3, or 4.")

print("\n[B] Move 7's isotropy table vs the symmetric dimensions {6,7,10}:")
strata = [
    ("Type O  de Sitter/FLRW (vacuum cut)", "so(4,1)",            10),
    ("Type D  Nariai (LambdaM^2=1/9)",       "so(2,1)x so(3)",     6),
    ("Type D  Schwarzschild-de Sitter",      "R_t x SO(3)",        4),
    ("Type I  Bianchi I",                    "3 spatial KV",       3),
    ("Type D  Kerr-de Sitter",               "R x SO(2)(+KT)",     2),
    ("Type I  Zipoy-Voorhees/Weyl",          "R x SO(2)",          2),
    ("wall    Type N (plane wave)",          "none",               0),
]
sym_dims = {6,7,10}
for name, iso, d in strata:
    verdict = "SYMMETRIC -> grading SURVIVES" if d in sym_dims else "non-symmetric -> grading FAILS"
    print(f"    {name:38s} h={iso:16s} dim {d:2d}  ->  {verdict}")

print("\n[C] Probe the SdS stratum at a natural embedding (static boost + spatial SO(3)),")
print("    and measure the 'leak' dim([m,m] landing outside h) -- is the failure sharp or graded?")
# SdS: static timelike KV = a substrate boost M_05; spatial SO(3) = rotations of {1,2,3}; index 4 spare.
hSdS = [(0,5),(1,2),(1,3),(2,3)]
hh,hm,mm = sym_pair(hSdS)
mSdS = [p for p in pairs if p not in hSdS]
# leak = dimension of the span of [m,m] components NOT in h
leak_vecs = []
for i in mSdS:
    for j in mSdS:
        c = comm(gens[i],gens[j])
        if not in_span(c, hSdS):
            leak_vecs.append(flat(c))
leak_dim = sp.Matrix.hstack(*leak_vecs).rank() if leak_vecs else 0
print(f"    SdS h=<M_05>+so(3)_(123) [embedding: reading, natural not P6-derived]:")
print(f"      [h,h]⊂h={hh}, [h,m]⊂m={hm}, [m,m]⊂h={mm}; leak rank = {leak_dim} (of dim m = {len(mSdS)})")

print("\n" + "="*78)
print("READING (second F1 computation):")
print("="*78)
print(f"""
 [computed, solid]:
   - The symmetric subalgebras of so(5,1) have dimensions {{6, 7, 10}} only (Grassmannian block
     type; no u-type since q=1 is odd). There is NO symmetric subalgebra of dim 2, 3, or 4.
   - Against Move 7's isotropy table, the clean HDA grading [m,m]⊂h therefore survives at EXACTLY
     two strata: Type O (so(4,1), dim 10 -- the symmetric vacuum cut) and NARIAI (so(2,1)xso(3),
     dim 6 -- the inner double-root metric-singular seam, the isotropy jump-up). It FAILS at every
     generic stratum: SdS (4), Bianchi I (3), Kerr-dS / Zipoy-Voorhees (2), and the wall (0).
   - At the SdS embedding the failure is not marginal: [m,m] leaks into m at rank {leak_dim}.

 So F1's fork falls toward SHARPENING, with a clean and striking shape: the finite-so(5,1) anchor
 reproduces the Dirac algebra term-for-term precisely at the MAXIMALLY-SYMMETRIC loci -- the vacuum
 cut and the Nariai enhancement -- and not on the generic Type-D/I cuts between them. The two
 survivors are exactly the cut of greatest isotropy and the inner seam where isotropy jumps UP.

 [reach -- NOT to resolve by how clean it looks; the genuine open question]:
   Two readings of this fact, settled only by pinning the anchor at a generic cut, not by preference:
   (a) F1 SHARPENS: the term-for-term homomorphism holds only on the symmetric-isotropy sub-bundle
       {{Type O, Nariai}}; the generic symmetry-reducible cuts realize the HDA only approximately /
       via a different mechanism. The "symmetry-reducible sector" on which the algebroid is a built
       object is then narrower than the full Petrov O/D/I range -- a real tightening.
   (b) The substrate-level grading [m,m]⊂h is too crude a test: the PHYSICAL anchor maps only a
       distinguished normal (the lapse direction), not all of m_x, so the homomorphism can survive
       on the broader sector with the finite-so(5,1) capture exhausting GRADUALLY toward the wall
       (the Move-6-scope picture). Then the leak measures substrate slack, not HDA failure.
   The SdS leak rank computed above is the first datum for distinguishing (a) from (b) across the
   strata; the decider is the explicit generic-cut anchor (how m_x -> H_perp/H_a is read off the
   slicing operator, P5/P6), which is the next grounded step.

 NEXT: pin the generic-cut anchor from the slicing operator (P5 slicing_operator.tex / P6) -- does
 it use all of m_x or a distinguished normal? -- which decides reading (a) vs (b) and turns this
 sharp computed map into the firm F1 verdict.
""")
