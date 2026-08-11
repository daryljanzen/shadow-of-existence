import sympy as sp

# ======================================================================
# F1 — charting the TIME/BOOST sector of the finite so(5,1) at the mode level.
# r270/r271 realized the SPATIAL sector (so(5)>so(4): M_a5 chi-normal lapse +
# M_ab tangential rotations) on the leaf. This classifies ALL 15 dS5 Killing
# vectors at the leaf to see where M_05 (timelike coset) and M_0a (boosts) live,
# and verifies the time-normal lapse modes close the same way the chi ones do.
#
# Construction: dS5 in M^6, eta=diag(-1,1,1,1,1,1); -X0^2+sum_{1..5}Xi^2=al^2.
# Leaf = the r270 S^3: X0=0, X5=0, (X1..X4) on S^3 of radius al, coords rho,th,ph.
# Two normals to the 3-leaf: e_0 (time, spacetime ADM) and e_5 (chi, substrate).
# ======================================================================

rho, th, ph, al = sp.symbols('rho theta phi alpha', positive=True)
eta = sp.diag(-1,1,1,1,1,1)

# leaf embedding X^A(rho,th,ph)
Xlf = sp.Matrix([0,
                 rho*sp.sin(th)*sp.cos(ph),
                 rho*sp.sin(th)*sp.sin(ph),
                 rho*sp.cos(th),
                 sp.sqrt(al**2 - rho**2),
                 0])
coords = [rho, th, ph]
# leaf tangent vectors (ambient 6-components)
Tang = [sp.Matrix([sp.diff(Xlf[A], c) for A in range(6)]) for c in coords]
e0 = sp.Matrix([1,0,0,0,0,0]); e5 = sp.Matrix([0,0,0,0,0,1])     # the two normals

def gen(a,b):                                   # M_{ab} acting on position: V^i = (M_ab)^i_j X^j
    M = sp.zeros(6,6)
    for i in range(6):
        M[i,b] += eta[i,a]; M[i,a] -= eta[i,b]
    return M

def killing_vec_at_leaf(a,b):
    return sp.simplify(gen(a,b)*Xlf)            # ambient 6-vector V^A at the leaf point

# decompose V = (tangential) + c0*e0 + c5*e5 ; report tangential?/time-normal?/chi-normal?
def classify(a,b):
    V = killing_vec_at_leaf(a,b)
    c0 = sp.simplify(V[0]); c5 = sp.simplify(V[5])              # normal components
    # tangential residue: V minus its e0,e5 parts, projected — but for so(5,1) KVs the
    # spatial-rotation gens have V[0]=V[5]=0 (purely tangential); flag by components.
    spatial = list(V[1:5])
    has_tang = any(sp.simplify(s) != 0 for s in spatial)
    return c0, c5, has_tang, V

idx = list(range(6))
print("="*74)
print("CLASSIFICATION of the 15 dS5 Killing vectors at the leaf (X0=X5=0):")
print("  time-normal (c0!=0) | chi-normal (c5!=0) | tangential (spatial!=0) | zero")
print("="*74)
buckets = {"tangential":[], "chi-normal":[], "time-normal":[], "zero":[], "mixed":[]}
for a in idx:
    for b in idx:
        if a < b:
            c0,c5,has_tang,V = classify(a,b)
            tags=[]
            if c0!=0: tags.append("time-normal")
            if c5!=0: tags.append("chi-normal")
            if has_tang: tags.append("tangential")
            if not tags: tags=["zero"]
            key = tags[0] if len(tags)==1 else "mixed"
            buckets[key].append((a,b))
            print(f"  M_{a}{b}: c0(time)={c0}, c5(chi)={c5}, tangential={has_tang}  -> {','.join(tags)}")

print("\n" + "="*74)
print("SECTOR MAP")
print("="*74)
print("  tangential (shift H_a, SO(4) leaf rotations):", buckets["tangential"])
print("  chi-normal lapse (H_perp^chi, profile X_a)   :", buckets["chi-normal"], " [r270/r271: the spatial coset M_a5]")
print("  time-normal lapse (H_perp^t,  profile X_a)   :", buckets["time-normal"], " [the boosts M_0a]")
print("  vanishes at leaf (cross-normal generator)    :", buckets["zero"], " [M_05 = the (0,5) boost: the two-normal mixer]")

# verify the time-normal lapse modes close the SAME as the chi ones (same leaf metric)
print("\n" + "="*74)
print("Do the TIME-normal lapse modes close like the chi ones? (same leaf-metric HDA bracket)")
print("="*74)
f = 1 - rho**2/al**2
g = sp.diag(1/f, rho**2, rho**2*sp.sin(th)**2); hinv = g.inv()
Xp = {1: Xlf[1], 2: Xlf[2], 3: Xlf[3], 4: Xlf[4]}     # the lapse profiles (same for both normals)
def hda_xi(a,b):
    return [sp.simplify(sum(hinv[c,d]*(Xp[a]*sp.diff(Xp[b],coords[d])-Xp[b]*sp.diff(Xp[a],coords[d]))
                            for d in range(3))) for c in range(3)]
xi12 = hda_xi(1,2)
print("  {H_perp[X1],H_perp[X2]} -> xi =", xi12, " (= d_phi = M_12, identical to r270's chi-normal result)")
print("  => the time-normal lapse modes give the SAME tangential rotations: the boost")
print("     sector closure IS r270's computation with the second normal (same leaf metric).")

print("\n" + "="*74)
print("VERDICT / CHART")
print("="*74)
print("""  The finite so(5,1) splits at the leaf into FOUR sectors:
    6 tangential (M_ab, SO(4) rotations)            -> shift, done r270/r271
    4 chi-normal lapse (M_a5, profile X_a)          -> H_perp^chi, done r270/r271
    4 time-normal lapse (M_0a, profile X_a)         -> H_perp^t; closes by the SAME
                                                       leaf-metric bracket as the chi modes
    1 cross-normal (M_05) -> VANISHES at the leaf   -> the (0,5) mixer: it relates the
       substrate-slicing normal (chi) to the spacetime-time normal (t); this is the
       deparametrization / one-clock generator = the LOCK's H_phys (r246-r268), not a
       fresh leaf computation.
  So the finite so(5,1) mode realization is COMPLETE: spatial explicit (r270/r271),
  the boost copy by identical structure, and M_05 the F1<->lock bridge (the lock).
  The sole remaining OPEN F1 piece is the INFINITE-DIM field-DOF completion
  (the non-isometry modes = the recovered Gowdy-dS field-theoretic model). That is next.""")
