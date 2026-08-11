import sympy as sp
M_N = 1/(3*sp.sqrt(3)); r_N = 1/sp.sqrt(3)
rho, M = sp.symbols('rho M', positive=True)
e = sp.symbols('e', positive=True)              # e = sqrt(Delta), Delta = M_N - M
f = 1 - 2*M/rho - rho**2
D = -sp.diff(f, rho, 2) - 2/rho**2              # curvature mismatch R_2 - R_S2

# connection at throat centre: exactly linear
Dc = sp.simplify(D.subs(rho, r_N))
print("CONNECTION at centre:  D(r_N,M) =", Dc, " = -12 sqrt3 (M_N - M)  -> LINEAR (analytic). check:",
      sp.simplify(Dc - (-12*sp.sqrt(3)*(M_N - M)))==0)

# connection at the geometry's OWN horizon rho_+ = r_N + c e + ... , with Delta = e^2
c = sp.sqrt(2/sp.sqrt(3))                        # leading: x ~ sqrt(2 Delta/sqrt3) = c e
rho_plus = r_N + c*e
M_sub = M_N - e**2
D_hor = D.subs({rho: rho_plus, M: M_sub})
ser = sp.series(D_hor, e, 0, 3).removeO()
ser = sp.nsimplify(sp.expand(ser), [sp.sqrt(3)])
print("\nCONNECTION at horizon: D(rho_+, M_N - e^2), series in e=sqrt(Delta):")
print("   ", ser)
# coefficient of e^1 (the sqrt(Delta) / BRANCH term) and e^2 (the Delta / linear term)
coeff_e1 = sp.simplify(ser.coeff(e, 1))
coeff_e2 = sp.simplify(ser.coeff(e, 2))
print("    coeff of e^1 (sqrt(Delta), branch) =", coeff_e1, "   <-- ZERO means NO branch in the connection")
print("    coeff of e^2 (Delta, linear)       =", coeff_e2)

print("\nVERDICT:")
print("  connection ~ (M_N - M)^1  (analytic, linear) at BOTH the throat centre and the horizon;")
print("  the sqrt(M_N - M) is the HORIZON SPLIT (cover ramification), entering D only as (sqrt)^2 = Delta.")
