import sympy as sp

# ============================================================================
# Aut(A2) <-> algebroid: does the connection-zero at Nariai carry the cover's
# RAMIFICATION (branch-type), while the connection-zero at Type O is analytic?
# Gauge alpha=1.  SdS: f = 1 - 2M/rho - rho^2.  Horizon cubic rho^3 - rho + 2M = 0.
# ============================================================================
rho, M, u = sp.symbols('rho M u', real=True)
al = 1
f  = 1 - 2*M/rho - rho**2
cubic = sp.expand(rho*(-f))               # rho^3 - rho + 2M   (= -rho*f)
print("horizon cubic  -rho*f =", cubic)

# --- (1) the ONE map: modulus M(u), u=r0 the offset/sheet coordinate (2M=u-u^3) ---
Mu = (u - u**3)/2
dMu = sp.diff(Mu, u)
folds = [c for c in sp.solve(sp.Eq(dMu,0), u) if c.is_real and c>0]
print("\n(1) modulus map  M(u) = (u-u^3)/2 ;  dM/du = 0  at u =", folds, " (the FOLD)")

# --- (2) branch point = double root of the cubic (discriminant=0) ---
disc = sp.discriminant(cubic, rho)
M_branch = [d for d in sp.solve(sp.Eq(disc,0), M) if d.is_real and d>0]
print("(2) cubic discriminant =", sp.factor(disc), " -> double root at M_N =", M_branch)
M_N = M_branch[0]
r_N = sp.nsimplify(1/sp.sqrt(3))
print("    fold value M(u*)=", sp.simplify(Mu.subs(u,folds[0])), "  ==  M_N ?",
      sp.simplify(Mu.subs(u,folds[0]) - M_N)==0, "   r_N =", r_N)

# --- (3) the connection-ZERO locus is {Type O, Nariai}; is each a fold? -------
# Type O = de Sitter vacuum, M=0, offset u=0.  Nariai, M=M_N, offset u=1/sqrt3.
print("\n(3) connection-zero strata, and whether each is a fold (branch) of M(u):")
for name, u0 in [("Type O (u=0)", sp.Integer(0)), ("Nariai (u=1/sqrt3)", r_N)]:
    slope = sp.simplify(dMu.subs(u,u0))
    print(f"    {name:20s}:  dM/du = {slope}   -> {'REGULAR point (simple root, NOT a branch)' if slope!=0 else 'FOLD (double root, the branch point)'}")

# --- (4) analytic character: expand the horizon roots about each stratum ------
# Solve cubic for the two physical (positive) roots as series in the modulus.
print("\n(4) horizon root behaviour in the modulus (the analytic fingerprint):")
# Type O: roots near M=0.  cubic rho^3-rho+2M.  At M=0 roots are 0,1,-1 (simple).
eps = sp.symbols('eps', positive=True)
# near M_N: set M = M_N - eps^2 * k  and see the two colliding roots split as +-eps
rt = sp.symbols('rt', real=True)
# expand cubic around r_N with M = M_N - delta
delta = sp.symbols('delta', positive=True)
c_local = sp.expand(cubic.subs({rho: r_N + rt, M: M_N - delta}))
c_local = sp.expand(c_local)
print("    near Nariai: cubic(r_N+rt, M_N-delta) =", sp.nsimplify(c_local,[sp.sqrt(3)]))
# leading: solve for rt to lowest order
sol_rt = sp.series(sp.solve(sp.Eq(c_local,0), rt)[0], delta, 0, 3) if False else None
roots_local = sp.solve(sp.Eq(sp.nsimplify(c_local,[sp.sqrt(3)]),0), rt)
print("    colliding roots rt = r - r_N :", [sp.simplify(sp.nsimplify(r,[sp.sqrt(3)])) for r in roots_local])

# Type O: roots near M=0 about the cosmological horizon rho=1 (simple root)
c_O = sp.expand(cubic.subs(rho, 1+rt))
rootsO = sp.solve(sp.Eq(c_O,0), rt)
print("    near Type-O cosmo horizon (rho=1): r-1 to leading order in M:",
      [sp.simplify(sp.series(r, M, 0, 2).removeO()) for r in rootsO])

# --- (5) surface gravity kappa = |f'(r_h)|/2 : scaling at each stratum --------
fp = sp.diff(f, rho)
print("\n(5) surface gravity kappa(r_h) = |f'|/2 scaling:")
print("    Type O  (rho=1, M->0):  f'(1) =", sp.simplify(fp.subs({rho:1,M:0})), " (nonzero -> simple root, ANALYTIC in M)")
# near Nariai: r_+ = r_N + s, with s ~ root separation; f'(r_N)=?
print("    Nariai  f'(r_N) =", sp.simplify(fp.subs({rho:r_N, M:M_N})), " (ZERO -> double root: f and f' both vanish, the FOLD)")
# kappa at r_N + s  to leading order
s = sp.symbols('s', real=True)
kap = sp.series(fp.subs({rho:r_N+s, M:M_N}), s, 0, 3).removeO()
print("    f'(r_N+s) at M=M_N  =", sp.nsimplify(kap,[sp.sqrt(3)]), " -> kappa ~ |s| (linear in the root displacement s)")
print("    and s ~ sqrt(M_N - M)  (roots split as +-sqrt of the discriminant) -> kappa ~ sqrt(M_N - M): BRANCH-TYPE")
