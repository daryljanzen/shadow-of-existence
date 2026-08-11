import sympy as sp

# alpha=1, Lambda=3.  SdS f = 1 - 2M/rho - rho^2.  Nariai: M_N=1/(3 sqrt3), r_N=1/sqrt3.
rho, M, Delta = sp.symbols('rho M Delta', positive=True)
M_N = 1/(3*sp.sqrt(3)); r_N = 1/sp.sqrt(3)
f = 1 - 2*M/rho - rho**2

# --- the symmetric-space grading at Nariai is so(2,1)_dS2 x so(3)_S2 ; it holds iff the
#     two factors are balanced.  Cleanest invariant breaking-measure: the curvature
#     mismatch  D = R_2(dS2) - R_(S2),  zero exactly at the symmetric (Nariai) member. ---
R2  = -sp.diff(f, rho, 2)          # 2d (t,rho) Ricci scalar = -f''
RS2 = 2/rho**2                     # S^2 Ricci scalar (radius rho)
D   = sp.simplify(R2 - RS2)
print("curvature mismatch  D(rho,M) = R_2 - R_S2 =", D)
print("D at exact Nariai (r_N,M_N) =", sp.simplify(D.subs({rho:r_N, M:M_N})), " (expect 0)")

# (1) THE CONNECTION measured at the throat centre rho=r_N, as a function of the modulus M:
D_centre = sp.simplify(D.subs(rho, r_N))
print("\n(1) CONNECTION (mismatch at throat centre) vs modulus:  D(r_N,M) =", D_centre)
print("    = ", sp.simplify(sp.factor(D_centre - 0)), "  ->  in (M_N - M):",
      sp.simplify(D_centre.subs(M, M_N - Delta)), "  => LINEAR in (M_N-M): ANALYTIC")

# (2) THE COVER ramification: the two colliding horizons as a function of Delta=M_N-M
cubic = rho**3 - rho + 2*M                  # = -rho*f
loc = sp.expand(cubic.subs({rho: r_N + sp.Symbol('x'), M: M_N - Delta}))
x = sp.Symbol('x')
# leading split: drop x^3 vs x^2 -> solve  sqrt3 x^2 - 2 Delta = 0  (from -2Delta + sqrt3 x^2 + x^3)
print("\n(2) COVER (horizon split):  local cubic about r_N =", sp.nsimplify(loc,[sp.sqrt(3)]))
xpm = sp.solve(sp.Eq(sp.sqrt(3)*x**2 - 2*Delta, 0), x)
print("    colliding roots  x = rho - r_N = +-", sp.simplify(xpm[1]), " ~ sqrt(Delta) = sqrt(M_N-M): BRANCH (sqrt)")

# (3) robustness: the connection measured at the geometry's OWN horizon rho_+(Delta), expanded in Delta.
#     rho_+ = r_N + x_+ with x_+ ~ +sqrt(2 Delta/sqrt3).  Does the sqrt feed into D, or cancel (even)?
xplus = sp.sqrt(2*Delta/sp.sqrt(3))          # leading horizon displacement ~ sqrt(Delta)
D_hor = D.subs({rho: r_N + xplus, M: M_N - Delta})
D_hor_series = sp.series(sp.nsimplify(D_hor,[sp.sqrt(3)]), Delta, 0, 2).removeO()
print("\n(3) connection at the geometry's own horizon rho_+ ~ r_N + sqrt(Delta):")
print("    D(rho_+, M_N-Delta) leading =", sp.simplify(D_hor_series),
      "  -> leading order in Delta:", sp.simplify(sp.LT(sp.Poly(sp.expand(D_hor_series), Delta)) if D_hor_series!=0 else 0))

# (4) cross-check the connection is SMOOTH (analytic) in M: it is a rational function of M.
print("\n(4) D(rho,M) is rational in M (no radicals) -> the connection is ANALYTIC in the modulus M.")
print("    The sqrt(M_N-M) lives ONLY in the cover map u<->M (offset->modulus), not in D(M).")
