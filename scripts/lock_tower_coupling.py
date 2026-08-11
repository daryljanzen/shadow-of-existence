import sympy as sp
a,phi,phidot,pi_n,mu,x,gamma = sp.symbols('a phi phidot pi_n mu x gamma', positive=True)
# P9 eq (l.160-161): S_n = 1/2 ∫ a^3[ phidot^2 - (mu^2/a^2) phi^2 ],  pi_n = a^3 phidot
L = sp.Rational(1,2)*a**3*phidot**2 - sp.Rational(1,2)*a*mu**2*phi**2
pi_expr = sp.diff(L, phidot)                     # = a^3 phidot
print("pi_n =", pi_expr)
phidot_sol = sp.solve(sp.Eq(pi_n, pi_expr), phidot)[0]
H = sp.simplify(pi_n*phidot_sol - L.subs(phidot, phidot_sol))
print("H_n  =", H, "   (tower Hamiltonian per mode)")
# kinetic piece and its behaviour at the a=0 boundary in the geodesic coordinate x ∝ a^{3/2}:
kinetic = pi_n**2/(2*a**3)
a_of_x = x**sp.Rational(2,3)                      # a ∝ x^{2/3}  =>  a^3 ∝ x^2
print("kinetic pi_n^2/2a^3  in x:", sp.simplify(kinetic.subs(a, a_of_x)), " => inverse-square at origin")
# So effective inverse-square coefficient at x=0 is promoted from c-number gamma (<=1/4)
# to an operator  Gamma = gamma + c * pi_n^2  (sum over modes), spectrum [gamma, ∞):
print()
print("free scale factor: gamma_max = 1/4  <  3/4 (limit-circle, BC needed)")
print("coupled: coefficient -> operator  Gamma = gamma + c*sum_n pi_n^2,  spec(pi_n^2)=[0,∞)")
print("  => spec(Gamma) = [gamma, ∞)  straddles 3/4: boundary structure becomes mode-state-dependent")
