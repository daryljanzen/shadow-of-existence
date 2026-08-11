import sympy as sp

print("="*78)
print("F1 firming at a GENERIC (Type-D / SdS) cut: does the HDA structure function there")
print("carry the (1,4) coset-metric form and vary across C as the algebroid requires?")
print("Anchor (Move 5): the HDA structure function IS the leaf's inverse 3-metric (CR leaves")
print("the Dirac algebra untouched). Leaf (P5): ds^2_3 = dr^2/f + r^2 dOmega^2, so h^{ab} =")
print("diag(f, 1/r^2, 1/(r^2 sin^2 th)). Symmetric-cut coset metric was (1,4) = ε ⊕ Riemannian")
print("(f1_coset_reduction.py). Test whether the SdS structure function keeps that form.")
print("="*78)

r, M, alpha, th = sp.symbols('r M alpha theta', positive=True)
Lam = 3/alpha**2
f = 1 - 2*M/r - Lam*r**2/3          # SdS lapse/leaf radial profile (Lambda = 3/alpha^2)

# --- the HDA structure function at the SdS cut (P5 leaf, inverse 3-metric) ---
h = sp.diag(f, 1/r**2, 1/(r**2*sp.sin(th)**2))
print("\n[1] HDA structure function at the SdS cut  h^{ab} = inverse leaf 3-metric:")
sp.pprint(h)

# --- (a) the angular block is Riemannian (positive-definite) wherever defined ---
ang = sp.diag(h[1,1], h[2,2])
print("\n[2] angular block diag(h^thth, h^phph) =", (h[1,1], h[2,2]),
      "-> both > 0 for r>0, sin(th)!=0  =>  Riemannian (the spatial h^{ab} of the (1,4) form).")

# --- (b) the radial component f carries the vantage sign ε; it flips at the horizons ---
# horizons: f = 0  <=>  r^3 - alpha^2 r + 2 M alpha^2 = 0
cubic = sp.expand((-alpha**2*r)*f)         # = r^3 - alpha^2 r + 2 M alpha^2  (up to sign)
cubic = sp.expand(r**3 - alpha**2*r + 2*M*alpha**2)
print("\n[3] radial component h^{rr} = f. Its SIGN is the vantage ε (sec.4 / adm3):")
print("    f > 0 : r spacelike  -> static/exterior vantage  (ε = +, the hole)")
print("    f < 0 : r timelike   -> dynamic/cosmos vantage    (ε = -, expanding)")
print("    horizons f=0 are the roots of  r^3 - alpha^2 r + 2 M alpha^2 = 0 :", cubic, "= 0")
disc = sp.discriminant(cubic, r)
print("    discriminant in r:", sp.factor(disc),
      "  (vanishes at 27 M^2 = alpha^2  =>  the Nariai double root, Move 7)")

# --- (c) so the structure function has the (1,4) coset-metric FORM at the SdS cut ---
print("\n[4] => at the SdS cut the structure function = [ε : sign(f), the radial/vantage axis]")
print("        ⊕ [Riemannian angular block] -- the SAME (1,4) coset-metric form found at the")
print("        symmetric cut (f1_coset_reduction: M_05 timelike/ε ⊕ Riemannian spacelike).")
print("        The ε is now r-dependent (flips across the horizon) = σ the vantage involution.")

# --- (d) base-variation: the structure function varies across C via f, reducing at M->0 ---
f0 = f.subs(M, 0)
print("\n[5] base-variation across C (the algebroid feature):")
print("    symmetric cut  M=0 :  h^{rr} = f =", sp.simplify(f0),
      "  = the de Sitter static leaf = the symmetric-cut coset metric (Move 6).")
dfdM = sp.diff(f, M)
print("    deform the cut  d h^{rr}/dM =", dfdM,
      " -> the offset bends the structure function off the symmetric coset metric.")
print("    SdS is the VACUUM kernel: rho = m'/4pi r^2 = 0 (m=M const), so this M-variation is")
print("    the vacuum SdS family (Move 4's offset r_0 in C), the anchor's kernel -- not matter.")

# --- consistency: vacuum check via the leaf intrinsic curvature (3R), grounding the anchor ---
g3 = sp.diag(1/f, r**2, r**2*sp.sin(th)**2)
g3inv = g3.inv()
coords = [r, th, sp.symbols('phi')]
n=3
Gamma = [[[sp.simplify(sum(g3inv[k,l]*(sp.diff(g3[l,i],coords[j])+sp.diff(g3[l,j],coords[i])-sp.diff(g3[i,j],coords[l]) ) for l in range(n))/2) for j in range(n)] for i in range(n)] for k in range(n)]
def Ric(i,j):
    return sp.simplify(sum(sp.diff(Gamma[k][i][j],coords[k]) for k in range(n))
        - sum(sp.diff(Gamma[k][i][k],coords[j]) for k in range(n))
        + sum(Gamma[k][i][j]*Gamma[m][k][m] for k in range(n) for m in range(n))
        - sum(Gamma[m][i][k]*Gamma[k][j][m] for k in range(n) for m in range(n)))
R3 = sp.simplify(sum(g3inv[i,j]*Ric(i,j) for i in range(n) for j in range(n)))
print("\n[6] leaf intrinsic curvature ^3R =", R3,
      "\n    (the energy-sector input 16pi rho = ^3R + K^2 - K_ij K^ij - 2Lambda; the SdS leaf's")
print("    ^3R is the bend off the round-S^3 substrate leaf ^3R=2Lambda=6/alpha^2 at M=0.)")
print("    ^3R at M=0:", sp.simplify(R3.subs(M,0)), " = 6/alpha^2 = 2Lambda  (round S^3, symmetric cut). check.")

print("\n"+"="*78)
print("READING:")
print("="*78)
print("""
 [computed, this script] At the Type-D / SdS cut the HDA structure function (the leaf's inverse
 3-metric, P5) keeps the (1,4) coset-metric FORM: a Riemannian angular block ⊕ a radial axis whose
 sign IS the vantage ε (σ: + exterior/hole, - cosmos, flipping at the horizon roots of
 r^3 - alpha^2 r + 2M alpha^2, double root at 27M^2=alpha^2 = Nariai). It VARIES across C through f
 (d h^{rr}/dM = -2/r), reducing at M=0 to the symmetric-cut coset metric (^3R -> 2Lambda, round S^3).
 So F1's structure-function identification -- h^{ab}(x) = the substrate coset metric, in the
 (1,4) form, across C -- holds at a generic cut, not only the symmetric one. This FIRMS the [reading]
 of sec.8 at the Type-D stratum: signature [computed], the base-varying coset-metric form exhibited.

 [the residual joint, honestly located -- NOT closed here] This firms that the structure function
 KEEPS the coset-metric form and varies (the algebroid). The full bracket-level homomorphism (B) --
 that this variation IS the so(5,1)-action on C term-for-term (the connection/anchor-derivative terms
 = the f1_strata [m,m]->m leak) -- needs the so(5,1)-action ON C, i.e. how the offset r_0 sits as a
 substrate-isometry orbit. That is exactly Move 4's open dimensional reconciliation (what the 5th
 dimension is / how P5-P6's dimension-agnostic slicing sits against genuine dS5 codim-1 slicing),
 Daryl's flagged call. So: F1's structure-function identification is firmed across the strata
 [computed]; the bracket-homomorphism's last term-for-term step is pinned to the Move-4 reconciliation.
""")
