import sympy as sp
t, rho, chi, th, ph, al = sp.symbols('t rho chi theta phi alpha', positive=True)
f = 1 - rho**2/al**2   # vacuum dS: the M=0 SdS form

# dS5 static patch, spatial S^3 = dchi^2 + sin^2chi dOmega2^2
g5 = sp.diag(-f, 1/f, rho**2, rho**2*sp.sin(chi)**2, rho**2*sp.sin(chi)**2*sp.sin(th)**2)
co5 = [t, rho, chi, th, ph]
print("dS5 tangent signature (count signs of the diagonal):")
signs = [sp.sign(g5[i,i].subs({chi:sp.pi/3, th:sp.pi/3, rho:al/2})) for i in range(5)]
print("  ", signs, " -> (timelike, spacelike) =", (signs.count(-1), signs.count(1)), " expect (1,4)")

# --- the 4D background dS4 = {chi = pi/2}, then ADM split {t=const} -> the 3D leaf ---
# leaf coords (rho, theta, phi) at chi=pi/2, t=const:
leaf = sp.Matrix([[1/f,0,0],[0,rho**2,0],[0,0,rho**2*sp.sin(th)**2]])  # induced 3-metric
print("\n3D spatial leaf metric (rho,theta,phi) at chi=pi/2, t=const:")
sp.pprint(leaf)
hab = leaf.inv()
print("inverse leaf metric h^ab = diag:", [sp.simplify(hab[i,i]) for i in range(3)])
print("  -> h^{rr} =", sp.simplify(hab[0,0]), " = f = 1 - rho^2/al^2  (the M=0 SdS leaf form; matches the transversality leaf)")
leaf_signs = [sp.sign(leaf[i,i].subs({th:sp.pi/3, rho:al/2})) for i in range(3)]
print("  leaf signature:", (leaf_signs.count(-1), leaf_signs.count(1)), " expect (0,3) Riemannian")

# --- the decomposition of the (1,4) coset tangent ---
print("\n(1,4) dS5 coset tangent decomposes as:")
print("   leaf (rho,theta,phi)  : 3 spacelike  == the HDA structure function h^{ab} (Riemannian)")
print("   time  t               : 1 timelike   == the lapse / the problem-of-time sign epsilon")
print("   chi                   : 1 spacelike  == the 5th dimension (the codim-1 normal)")
print("   3 + 1 + 1 = 5 ;  (0,3)+(1,0)+(0,1) = (1,4)  CHECK")

# --- chi is the totally-geodesic normal (re-confirm r227): K ~ d/dchi(g) at chi=pi/2 ---
dchi_block = sp.diff(rho**2*sp.sin(chi)**2, chi).subs(chi, sp.pi/2)
print("\nchi totally-geodesic normal?  d/dchi(angular block)|_{pi/2} =", dchi_block, " -> 0  (K=0, confirms r227)")
