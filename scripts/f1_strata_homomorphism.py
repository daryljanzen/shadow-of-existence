import sympy as sp

print("="*78)
print("F1 (first computation) — does the anchor stay a homomorphism OFF the symmetric cut?")
print("Move 6 showed [m,m]subset h at the symmetric cut (isotropy h=so(4,1)). The HDA")
print("grading {H_perp,H_perp}~H_a is RIGID: two normals must close on the tangential")
print("sector, never back on H_perp (the coefficient h^{ab} may vary -> algebroid; the")
print("GRADING may not). Anchor: m<->H_perp, h<->H_a. So at a cut whose isotropy has")
print("dropped to h_x (Move 7 stratification), the test is whether the symmetric-pair")
print("grading SURVIVES: [m_x,m_x]subset h_x ?  Where it holds, the homomorphism extends;")
print("where [m_x,m_x] leaks into m_x, the finite-so(5,1) anchor stops reproducing the HDA.")
print("="*78)

# ---- so(5,1) realization, identical to adm_so51_1.py (compute IN the construction) ----
eta = sp.diag(-1,1,1,1,1,1)   # index 0 timelike; 1..5 spacelike
def gen(a,b):
    M = sp.zeros(6,6)
    for i in range(6):
        M[i,b] += eta[i,a]
        M[i,a] -= eta[i,b]
    return M
pairs = [(a,b) for a in range(6) for b in range(a+1,6)]
gens = {p: gen(*p) for p in pairs}
def flat(M): return sp.Matrix([M[i,j] for i in range(6) for j in range(6)])
def comm(A,B): return A*B - B*A
def in_span(M, keys):
    if all(v == 0 for v in flat(M)): return True
    A = sp.Matrix.hstack(*[flat(gens[k]) for k in keys])
    return A.rank() == sp.Matrix.hstack(A, flat(M)).rank()

def test_pair(h_keys, label, expect_symmetric):
    """Given an isotropy subalgebra h (by generator keys), form the complement m = pairs\\h,
       and test the three inclusions. The HDA homomorphism needs all three; the SYMMETRIC one
       [m,m]subset h is the {H_perp,H_perp}~H_a grading."""
    m_keys = [p for p in pairs if p not in h_keys]
    # is h actually a subalgebra? (must be, to be an isotropy)
    hh = all(in_span(comm(gens[i],gens[j]), h_keys) for i in h_keys for j in h_keys)
    hm = all(in_span(comm(gens[i],gens[j]), m_keys) for i in h_keys for j in m_keys)  # reductive
    mm = all(in_span(comm(gens[i],gens[j]), h_keys) for i in m_keys for j in m_keys)  # symmetric
    print(f"\n--- {label}")
    print(f"    dim h = {len(h_keys)},  dim m = {len(m_keys)}")
    print(f"    [h,h]subset h (h is a subalgebra)      : {hh}")
    print(f"    [h,m]subset m (reductive split)        : {hm}")
    print(f"    [m,m]subset h (SYMMETRIC; the HDA grading {{H_perp,H_perp}}~H_a): {mm}")
    homo = hh and hm and mm
    print(f"    => anchor reproduces the HDA grading here: {homo}"
          f"   (expected symmetric-pair: {expect_symmetric})")
    return homo

# (O) Type O — the symmetric vacuum cut: h = so(4,1) = index-5 stabilizer (generators not touching 5)
hO = [(a,b) for (a,b) in pairs if 5 not in (a,b)]
test_pair(hO, "Type O  (symmetric vacuum cut): h = so(4,1), index-5 stabilizer", True)

# (N) Nariai candidate — h = so(1,2) x so(3), block-diagonal on {0,1,2}|{3,4,5}
#     (dS2 x S2: SO(2,1)~SO(1,2) on the (1,2)-block {0,1,2}; SO(3) on the (3,0)-block {3,4,5}).
#     This is a Grassmannian-type reductive pair SO(5,1)/(SO(1,2)xSO(3)). Symmetric?
hN = [(a,b) for (a,b) in pairs if (a in (0,1,2) and b in (0,1,2)) or (a in (3,4,5) and b in (3,4,5))]
test_pair(hN, "Nariai cand.: h = so(1,2)+so(3), blocks {0,1,2}|{3,4,5}  [embedding: reach, confirm vs P6]", True)

# (D) SdS-generic candidate — h = R_boost(M_03) + so(3) on {1,2,?}. SdS isotropy = R_t x SO(3), dim 4.
#     A non-symmetric reductive candidate: one boost + an so(3). Test the grading.
hD = [(0,3),(1,2),(1,4),(2,4)]  # M_03 (a boost) + so(3) acting on {1,2,4}
test_pair(hD, "SdS cand.: h = <M_03> + so(3) on {1,2,4}, dim 4  [embedding: reach, confirm vs P6]", False)

# (I) Bianchi-I candidate — h = 3 commuting spatial translations (a non-symmetric, abelian isotropy).
#     Model 3 spatial KV as so(3) rotations {1,2},{1,3},{2,3} is symmetric-ish; instead Bianchi I
#     homogeneity = 3 translations. In so(5,1) the closest finite analogue is an abelian triple;
#     test a generic abelian-ish triple of spatial rotations vs the grading.
hI = [(1,2),(3,4),(1,3)]  # a non-closing generic triple (NOT a subalgebra in general) -> diagnostic
test_pair(hI, "Bianchi-ish cand.: h = <M_12,M_34,M_13>, dim 3  [diagnostic; confirm the real KV algebra vs P6]", False)

print("\n" + "="*78)
print("READING (first F1 computation):")
print("="*78)
print("""
 The HDA grading the anchor must reproduce is the SYMMETRIC-PAIR inclusion [m_x,m_x]subset h_x
 at each cut. The computation above tests it across candidate isotropies of decreasing dimension.

 [computed, in the so(5,1) realization]:
   - Type O (h = so(4,1)): symmetric pair -> grading holds (re-confirms Move 6).
   - The structural law it exposes: the grading survives exactly when (h_x, m_x) is a SYMMETRIC
     pair of so(5,1); it fails (the [m,m] bracket leaks into m_x) when h_x is a non-symmetric
     reductive subalgebra. This is a finite, decidable test per stratum.

 [reach -- the stratum<->subalgebra dictionary, to confirm at source (P6 range_paper / the
  slicing operator) before the per-stratum verdict is firm]:
   - Which so(5,1)-subalgebra each Petrov stratum's isotropy actually embeds as is fixed by the
     slicing construction, NOT by my choice of generators here. The Nariai/SdS/Bianchi embeddings
     above are CANDIDATES chosen by signature/dimension; the real ones must be read from P6.
   - The honest fork (per THE_PLAN): F1 closes across C iff the symmetric-pair grading survives on
     the whole symmetry-reducible sector; it SHARPENS to a sub-bundle iff some interior strata are
     non-symmetric. The computation shows the MECHANISM of the fork (symmetric vs non-symmetric
     isotropy) and makes it decidable; the VERDICT waits on the P6 embeddings.

 NEXT GROUNDED STEP: read P6 (range_paper.tex) for the explicit isometry algebra of each range
 class as it sits in the substrate, embed each in so(5,1) faithfully, and re-run this test to map
 the exact sub-bundle on which the algebroid homomorphism is term-for-term exact.
""")
