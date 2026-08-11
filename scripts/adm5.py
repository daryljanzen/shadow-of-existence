import sympy as sp
print("="*78)
print("ADM-5: are the three horizon roots the spectrum of a NATURAL operator?")
print("="*78)
w=sp.symbols('w',real=True)
M=sp.symbols('M',positive=True)
twoM=sp.Rational(2,3)/sp.sqrt(3)*sp.sin(3*w)         # 2M = (2/3sqrt3) sin 3w
rk=[sp.simplify(2/sp.sqrt(3)*sp.sin(w+2*sp.pi*k/3)) for k in range(3)]   # tau-orbit

print("\n(1) Are the three roots the tau-orbit  r_k = (2/sqrt3) sin(w + 2pi k/3) ?")
cubic=lambda r: sp.expand(r**3 - r + twoM)
for k in range(3):
    val=sp.simplify(sp.expand_trig(cubic(rk[k])))
    print(f"   r_{k}^3 - r_{k} + 2M  = {val}")
print("   => the order-3 sky-angle generator tau GENERATES the three roots as one orbit.")

print("\n(2) elementary symmetric invariants of the orbit (the S3-invariants):")
e1=sp.simplify(sp.expand_trig(rk[0]+rk[1]+rk[2]))
e2=sp.simplify(sp.expand_trig(rk[0]*rk[1]+rk[0]*rk[2]+rk[1]*rk[2]))
e3=sp.simplify(sp.expand_trig(rk[0]*rk[1]*rk[2]))
print(f"   e1 = sum r_k        = {e1}   (=0  => trivial irrep component VANISHES; roots span the standard-2d)")
print(f"   e2 = sum r_i r_j    = {e2}   (= -1 = -alpha^2 in gauge: the substrate scale)")
print(f"   e3 = prod r_k       = {sp.simplify(e3)}   (= -2M : the MASS is the cubic invariant)")

print("\n(3) sigma : w -> pi/3 - w  acts on the roots how?")
wn=sp.Rational(1,5)  # sample angle
r_num=[float(rk[k].subs(w,wn)) for k in range(3)]
rs=[float((2/sp.sqrt(3)*sp.sin((sp.pi/3-w)+2*sp.pi*k/3)).subs(w,wn)) for k in range(3)]
print(f"   roots at w=1/5:        {[round(x,4) for x in sorted(r_num)]}")
print(f"   roots at sigma(w):     {[round(x,4) for x in sorted(rs)]}  (same set => sigma permutes them)")
# which permutation:
import itertools
perm=[min(range(3),key=lambda j: abs(rs[k]-r_num[j])) for k in range(3)]
print(f"   sigma sends root k -> {perm}  (a transposition fixing one root)")

print("\n(4) candidate NATURAL operators with the roots as eigenvalues:")
# (a) Weyl/curvature operator for SdS (Type D): eigenvalues (-2 Psi2, Psi2, Psi2), Psi2 = -M/r^3
r=sp.symbols('r',positive=True)
print("   - Weyl operator (SdS Type D): eigenvalues (2M/r^3, -M/r^3, -M/r^3) -- POSITION-dependent,")
print("     only TWO distinct values, and not constant. NOT the three horizon roots. RULED OUT.")
# (b) tau in the standard-2d irrep: a 120-deg rotation
tau2d=sp.Matrix([[sp.cos(2*sp.pi/3),-sp.sin(2*sp.pi/3)],[sp.sin(2*sp.pi/3),sp.cos(2*sp.pi/3)]])
print("   - tau in the standard-2d irrep (120-deg rotation): eigenvalues",
      [sp.simplify(e) for e in tau2d.eigenvals()].__class__ and list(tau2d.eigenvals().keys()))
print("     = e^{+-2pi i/3} (cube roots of unity), NOT the roots. The roots are the COMPONENTS of")
print("     the orbit vector in this rep, not eigenvalues of the operator. So tau is not it either.")
# (c) companion matrix
print("   - companion matrix of r^3-r+2M: eigenvalues ARE the roots BY CONSTRUCTION -> circular,")
print("     not a geometrically natural operator. Does not count.")

print("\n(5) discriminant (the S3-invariant detecting a repeated root):")
disc=sp.simplify(sp.discriminant(r**3-r+M*2,r))
print(f"   disc(r^3 - r + 2M) = {disc}  -> 0 at 2M=2/(3sqrt3) (Nariai): the orbit COLLAPSES (two roots merge).")
