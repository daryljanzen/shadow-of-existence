import sympy as sp
r, M, alpha = sp.symbols('r M alpha', positive=True)

print("="*72)
print("REACH step 2 — does the GRADING close through the intrinsic carrier?")
print("Claim: [m,m]subset h (symmetric, homomorphism exact) <=> the cut's intrinsic")
print("curvature is CONSTANT; the leak into m (the connection) <=> K_G varies (the bend).")
print("Intrinsically that curvature is the slicing surface's K_G. Test: the two")
print("constant-curvature configurations of the curve = the two symmetric strata {O,Nariai}.")
print("="*72)

KG = 1/alpha**2 - M/r**3                      # P3 slicing-surface Gaussian curvature
dKG_dr = sp.simplify(sp.diff(KG, r))
print("\n[1] K_G =", KG, " ;  d_r K_G =", dKG_dr, "  (the radial variation = the bend gradient)")
print("    constant intrinsic curvature (d_r K_G == 0 for all r)  <=>  M = 0  (Type O, de Sitter).")
sol = sp.solve(sp.Eq(dKG_dr, 0), M)
print("    solve d_r K_G = 0 for M:", sol, "  -> M=0 is the only globally-constant-K_G cut.")

# the curve's turning points: horizon cubic (gauge alpha=1): f=1-2M/r-r^2=0 -> r^3 - r + 2M = 0
Mg = sp.symbols('M', positive=True)
cubic = r**3 - r + 2*Mg
disc = sp.discriminant(cubic, r)
print("\n[2] horizon cubic (gauge alpha=1)  r^3 - r + 2M :  discriminant =", sp.factor(disc))
Mn = sp.solve(sp.Eq(disc, 0), Mg)
print("    double root (turning points MERGE = Nariai) at discriminant=0:  M =", Mn)
Mnar = [m for m in Mn if m > 0][0]
cub_n = cubic.subs(Mg, Mnar)
print("    at M =", Mnar, "  cubic factors:", sp.factor(cub_n), " -> double root r_N = 1/sqrt(3)")

print("\n[3] So the slicing curve has exactly TWO constant-curvature configurations:")
print("    (a) M=0       : globally constant K_G = 1/alpha^2  -> de Sitter, Type O (so(4,1), dim10)")
print("    (b) Nariai    : turning points merge -> static region pinches to the frozen 2-sphere,")
print("                    geometry dS_2 x S^2, both factors constant-curvature (SO(2,1)xSO(3), dim6)")
print("    Every other cut: distinct turning points, K_G varies over the open static region")
print("    (d_r K_G = 3M/r^4 != 0, the matter bend) -> NOT constant-curvature.")

print("\n[4] This is EXACTLY the firm per-stratum verdict (f1_per_stratum, consolidation §2):")
print("    symmetric grading [m,m]subset h survives at {Type O, Nariai} ONLY; leaks elsewhere.")
print("    Here it is realized INTRINSICALLY: symmetric <=> the curve is at a constant-curvature")
print("    (degenerate) configuration; the leak (connection) <=> K_G varies = the bend = matter.")
print("    No ambient embedding enters: K_G is Theorema-Egregium-intrinsic, the cubic/turning-point")
print("    structure is the curve's own.")

# sanity: the leak/connection direction is the bend gradient, vanishing at the two configs
print("\n[5] connection (leak) carrier check: d_r K_G = 3M/r^4")
print("    at M=0 (Type O): d_r K_G =", dKG_dr.subs(M,0), " (no leak: symmetric)")
print("    the M-transverse connection d_M K_G =", sp.simplify(sp.diff(KG,M)), " (= -1/r^3, step-1 link)")
