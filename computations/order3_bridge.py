"""
WP-B, the order-three bridge  --  receipt / investigation  (stage 1-3)

Question: is the GROUPOID's order-three (the sky-angle Z/3, w -> w + 2pi/3, on the
roots of the horizon cubic r^3 - r + 2M = 0) the SAME Z/3 as the BEAD's order-three
(r -> e^{2 pi i/3} r under tau~ -> tau~ + i 2 pi alpha/3, from r = A sinh^{2/3}(3 tau~/2alpha))?

We work in alpha = 1 units.  We do NOT assume the answer.  Each stage prints what it
establishes.  Stages: (1) the two cubics + their Z/3 actions; (2) branch loci and
monodromy of each cover; (3) what each Z/3 does at the Nariai point.
"""
import sympy as sp

r, M, w, u, tau, k = sp.symbols('r M w u tau k', complex=True)
Mr = sp.symbols('M', real=True, positive=True)
print("="*78)
print("STAGE 1 -- the two cubics and their order-three actions")
print("="*78)

# ---- (1a) the HORIZON cubic  f=0  ->  r^3 - r + 2M = 0 --------------------------
Ch = r**3 - r + 2*M
print("\n[1a] horizon cubic  C_h(r) = r^3 - r + 2M   (from f = 1 - 2M/r - r^2 = 0)")
# trig parameterisation claimed in the groupoid paper: r0 = (2/sqrt3) sin w, 2M = (2/(3 sqrt3)) sin 3w
r_w = (2/sp.sqrt(3))*sp.sin(w)
twoM_w = (sp.Rational(2,3)/sp.sqrt(3))*sp.sin(3*w)
check = sp.simplify(Ch.subs({r:r_w, M:twoM_w/2}))
print("    substitute r=(2/sqrt3) sin w, 2M=(2/(3sqrt3)) sin 3w into C_h  ->", check,
      " (0 confirms the parameterisation)")
# the three roots are w, w+2pi/3, w+4pi/3 (same 2M, since sin 3w is 2pi/3-periodic)
print("    three roots: r_k = (2/sqrt3) sin(w + 2 pi k/3), k=0,1,2  (all share the same 2M)")
roots_w = [sp.simplify((2/sp.sqrt(3))*sp.sin(w + 2*sp.pi*kk/3)) for kk in range(3)]
sum_roots = sp.simplify(sum(roots_w))
prod_pairs = sp.simplify(roots_w[0]*roots_w[1]+roots_w[1]*roots_w[2]+roots_w[2]*roots_w[0])
prod_roots = sp.simplify(roots_w[0]*roots_w[1]*roots_w[2])
print("    Vieta check: sum r_k =", sum_roots, " (want 0);  sum r_i r_j =", prod_pairs,
      " (want -1);  prod r_k =", sp.simplify(prod_roots - (-twoM_w)), "+ (-2M)  (want 0)")
print("    => groupoid Z/3 is  w -> w + 2pi/3 : a 3-CYCLE of the three horizon roots.")

# ---- (1b) the BEAD cubic (sheets at fixed cosmic time) -------------------------
# r = A sinh^{2/3}(3 tau~/2)  =>  r^3 = A^3 sinh^2(3 tau~/2).  Let s = A^3 sinh^2(...).
# At fixed cosmic time the three sheets are the cube roots r_k = s^{1/3} e^{2pi i k/3}.
print("\n[1b] bead law  r = A sinh^{2/3}(3 tau~/2),  A^3 = 2M   =>   r^3 = 2M sinh^2(3 tau~/2)")
print("    bead cubic in r (fixed tau~):  C_b(r) = r^3 - 2M sinh^2(3 tau~/2)   -- PURE cube (no linear term)")
print("    three sheets: r_k = (2M sinh^2)^{1/3} e^{2 pi i k/3}, k=0,1,2")
print("    => bead Z/3 is  r -> e^{2pi i/3} r : rotation by a cube root of unity.")
# verify the e^{2pi i/3} arises from tau~ -> tau~ + i 2pi/3  (u = 3tau~/2 -> u + i pi)
uu = sp.symbols('uu', complex=True)
ratio = sp.simplify(sp.sinh(uu + sp.I*sp.pi)/sp.sinh(uu))   # sinh(u+i pi) = -sinh u
print("    sinh(u+i*pi)/sinh(u) =", ratio, " so [sinh]^{2/3} picks up (-1)^{2/3} =",
      sp.simplify(sp.exp(sp.Rational(2,3)*sp.I*sp.pi)), "= e^{2pi i/3}. Confirmed.")

print("\n[1c] SHAPE COMPARISON of the two cubics-in-r:")
print("    horizon:  r^3 - r + 2M         (depressed, p = -1  != 0)")
print("    bead:     r^3 - 2M sinh^2(.)   (pure cube, p = 0)")
print("    Different depressed-cubic shape.  A Z/3 exists on BOTH, but they are the")
print("    Galois/cube-root Z/3 of DIFFERENT cubics.  Whether a canonical map identifies")
print("    them is Stages 2-3.")

print("\n"+"="*78)
print("STAGE 2 -- branch loci and monodromy of the two covers")
print("="*78)

# ---- (2a) horizon cover over the M-plane --------------------------------------
disc_h = sp.discriminant(Ch, r)
print("\n[2a] horizon cubic as a 3-sheeted cover of the M-plane:")
print("    discriminant_r(r^3 - r + 2M) =", sp.simplify(disc_h))
sols = sp.solve(sp.Eq(disc_h, 0), M)
print("    branch points (disc=0) at M =", sols, " i.e. M = +-1/(3 sqrt3) = +- Nariai mass")
print("    => the groupoid cover branches at the NARIAI points; monodromy there is the")
print("       transposition sigma (two roots collide).  Base space = the M (mass / sky-angle) line.")

# ---- (2b) bead cover over the cosmic-time (u) plane, fixed Nariai M ------------
print("\n[2b] bead cover r^3 = 2M sinh^2(u),  u = 3 tau~/2,  at FIXED M = Nariai:")
print("    as a cover of the u-plane, r = (2M)^{1/3} sinh^{2/3}(u) branches where sinh(u)=0")
print("    => u = i pi n  (n in Z);  the n=0 branch point is u=0 i.e. r=0, THE SEAM.")
print("    Base space = the cosmic-time (u) line, at the single mass M = Nariai.")

print("\n[2c] the mismatch, stated plainly:")
print("    - groupoid Z/3: cover of the MASS line, branched at NARIAI (M=+-1/(3sqrt3)).")
print("    - bead Z/3:     cover of the TIME line at fixed Nariai mass, branched at the SEAM r=0.")
print("    Different base spaces; different branch loci.  The bead lives OVER a single point")
print("    (Nariai) of the groupoid's base.")

print("\n"+"="*78)
print("STAGE 3 -- what each order-three does AT the Nariai point")
print("="*78)
MN = sp.Rational(1,3)/sp.sqrt(3)     # Nariai mass, 1/(3 sqrt3)
print("\n[3a] Nariai mass M_N = 1/(3 sqrt3) =", sp.nsimplify(MN), "~", float(MN))
Ch_N = (r**3 - r + 2*MN)
roots_N = sp.solve(Ch_N, r)
print("    horizon cubic at Nariai:  r^3 - r + 2/(3sqrt3) = 0")
print("    roots:", [sp.simplify(x) for x in roots_N], " (numerically", [complex(sp.N(x)) for x in roots_N],")")
print("    => a DOUBLE root at +1/sqrt3 and a single root at -2/sqrt3: the groupoid Z/3 has")
print("       DEGENERATED here (two of the three roots have collided). sigma's fixed point.")
print("\n[3b] the bead at Nariai is where its clean 3 sheets LIVE (r -> e^{2pi i/3} r, all distinct).")
print("    So at the very point where the groupoid Z/3 degenerates, the bead Z/3 is nondegenerate.")
print("\n[3c] where does r=0 (the bead branch point / seam) sit in the groupoid?")
print("    horizon cubic at r=0:  0 - 0 + 2M = 2M != 0, so r=0 is NOT a horizon root.")
print("    In the groupoid, r=0 is the fixed locus of the mass-reflection R (2M -> -2M),")
print("    a Z/2 (NOT the Z/3).  So the bead's Z/3-branch = the groupoid's Z/2-fixed point.")

print("\n"+"="*78)
print("PRELIMINARY READING (to be pressure-tested in stage 4, not a conclusion):")
print("  Both are 'the cube-root Z/3', but they are the cube-root Z/3 of different cubics,")
print("  over different base spaces, branched at different loci, and they behave OPPOSITELY")
print("  at Nariai (groupoid degenerates; bead is clean). A canonical identification is NOT")
print("  automatic. Stage 4 searches for a genuine bridge map before drawing any verdict.")
print("="*78)

print("\n"+"="*78)
print("STAGE 4 -- which cubic does each order-three actually belong to?")
print("="*78)

import sympy as sp
rr, Msym, tt = sp.symbols('rr M tt', positive=True)
A = (2*Msym)**sp.Rational(1,3)
r_of = A*sp.sinh(sp.Rational(3,2)*tt)**sp.Rational(2,3)          # bead law, alpha=1
drdt = sp.diff(r_of, tt)
f_expr = 1 - 2*Msym/rr - rr**2
one_minus_f = sp.simplify((1 - f_expr).subs(rr, r_of))
lhs = sp.simplify(drdt**2 - one_minus_f)
print("\n[4a] what ODE does the cosmic-time law r=A sinh^{2/3}(3tau~/2) satisfy?")
print("    (dr/dtau~)^2 - (1 - f)|_(r=bead)  simplifies to:", sp.simplify(lhs), " (0 => (dr/dtau~)^2 = 1 - f)")
print("    => COSMIC TIME turns where 1 - f = 0;  the SLICING curve (dr/dl)^2=|f| turns where f = 0.")
print("       Two DIFFERENT turning conditions (the corpus's own scope note, CR_framework:750).")

print("\n[4b] the two turning cubics (clear denominators, alpha=1):")
print("    slicing / HORIZON  (f=0):        r^3 - r + 2M = 0     <- groupoid Z/3 lives here")
print("    cosmic-time / COMOVING (1-f=0):  r^3 + 2M     = 0     <- bead Z/3 lives here")

# root CONFIGURATIONS in the complex r-plane
Msub = sp.Rational(3,20)      # 0.15, sub-Nariai (Nariai = 0.19245)
for label, cub in [("HORIZON r^3-r+2M", rr**3-rr+2*Msym), ("COMOVING r^3+2M", rr**3+2*Msym)]:
    rts = sp.nroots(cub.subs(Msym, Msub))
    pts = [complex(x) for x in rts]
    print(f"\n    [{label}] at M=0.15 -> roots:")
    for p in pts: print(f"        {p.real:+.4f} {p.imag:+.4f}i   |arg|={abs(sp.arg(sp.N(p)))*180/sp.pi.evalf():.1f} deg" if abs(p)>1e-9 else f"        {p.real:+.4f} {p.imag:+.4f}i  (origin)")
    imags = [abs(p.imag) for p in pts]
    print(f"        max|Im| = {max(imags):.4f}  ->", "ALL REAL (colinear on real axis)" if max(imags)<1e-9 else "has complex roots")

print("\n[4c] the geometric distinction in the complex r-plane:")
print("    HORIZON roots (sub-Nariai): three REAL, COLINEAR points on the real axis.")
print("    COMOVING roots: an EQUILATERAL TRIANGLE (one real + conjugate pair at +-120 deg).")
print("    The groupoid Z/3 3-cycles three colinear real roots (casus irreducibilis);")
print("    the bead Z/3 rotates an equilateral triangle by e^{2pi i/3}. Different realisations.")

print("\n[4d] are the two cubics affinely/Moebius equivalent (could a change of variable identify them)?")
# a pure cube r^3 = c has equianharmonic roots (equilateral); r^3 - r + 2M does not for generic M.
print("    r^3 + 2M has equianharmonic (equilateral) roots for every M != 0.")
print("    r^3 - r + 2M has equilateral roots ONLY if its linear term vanishes, i.e. never (p=-1).")
print("    An affine map r->a r+b preserves the roots' shape (ratios); it cannot turn colinear-real")
print("    into equilateral. => the two cubics are NOT affinely equivalent. No canonical iso by")
print("    change of variable.")

print("\n[4e] the only sense in which they ARE 'the same order-three':")
print("    S_3 contains a UNIQUE order-3 subgroup (the alternating A_3). So each cubic's Galois")
print("    Z/3 is 'the' Z/3 abstractly -- as is every Z/3. Identifying the TWO S_3's (hence the two")
print("    Z/3's) requires identifying the two root sets, which is exactly the A_2/'triality'")
print("    resemblance the corpus already logs DO-NOT-ASSERT (J7). It is not forced by the geometry.")

print("\n[4f] does an order-three bridge -- even if granted -- close the SHEET-ASSIGNMENT question?")
print("    No. A groupoid<->bead Z/3 iso would label bead sheets by HORIZON-ROOT index, not by")
print("    congruence (A / B / photon). The congruence labels come from the ruling geometry")
print("    (slicing_operator), an independent structure. So the order-three bridge is neither")
print("    established NOR sufficient for the sheet-assignment.")

print("\n"+"="*78)
print("VERDICT (honest):")
print("  The groupoid order-three and the bead order-three are the Z/3's of TWO DIFFERENT")
print("  turning-point cubics -- horizon f=0 (r^3-r+2M, three colinear real roots) vs comoving")
print("  1-f=0 (r^3+2M, an equilateral triangle). They are not affinely equivalent; they cover")
print("  different bases; they branch at different loci (Nariai vs seam); they degenerate")
print("  oppositely at Nariai. 'Same order-three' is TRUE only in the trivial sense that S_3 has a")
print("  unique Z/3, and any nontrivial identification is the do-not-assert A_2 resemblance -- which")
print("  in any case would not force the congruence sheet-assignment. The bridge, as a structural")
print("  theorem, does NOT close; the corpus's 'the groupoid triple' language is a resemblance,")
print("  correctly held do-not-assert.")
print("="*78)
