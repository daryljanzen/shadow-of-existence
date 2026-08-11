import sympy as sp
u, al = sp.symbols('u alpha', positive=True)   # u = r0/alpha (slicing offset), alpha = throat
# P3 mass map (algebroid_base_and_substrate.md §2):  2M = alpha (u - u^3)
twoM = al*(u - u**3)
M = twoM/2
Lam = 3/al**2

# The transverse-modulus map M(r0): where is it stationary (the fold of the orbit-labeling)?
dM = sp.diff(M, u)
crit = sp.solve(sp.Eq(dM, 0), u)
crit = [c for c in crit if c.is_real and c > 0]
print("M(u) = ", sp.simplify(M))
print("dM/du = 0 at u = r0/alpha =", crit, "  (expect 1/sqrt(3))")
u_star = crit[0]
M_star = sp.simplify(M.subs(u, u_star))
LM2 = sp.simplify(Lam*M_star**2)
print("M at the fold       =", M_star, "   (expect alpha/(3 sqrt3))")
print("Lambda*M^2 at fold  =", LM2, "   (expect 1/9 = the Nariai double root)")

# cross-check against the horizon cubic's double root (independent route): r^3 - alpha^2 r + 2M alpha^2
r = sp.symbols('r', positive=True)
Mc = sp.symbols('M', positive=True)
cubic = r**3 - al**2*r + 2*Mc*al**2
disc = sp.discriminant(cubic, r)
print("\nhorizon cubic discriminant =", sp.factor(disc))
dbl = sp.solve(sp.Eq(disc, 0), Mc)
dbl = [d for d in dbl if d.is_real and d > 0]
print("double root at M =", dbl, " -> Lambda*M^2 =", [sp.simplify(Lam*d**2) for d in dbl])

# Is the offset->M map 2-to-1 below the fold? (two offsets share an M, meeting at Nariai)
Mtest = sp.Rational(1,1)*M_star/2   # pick an M below the max
sols = sp.solve(sp.Eq(M, Mtest), u)
sols = [s for s in sols if s.is_real and s >= 0 and s <= 1]
print("\noffsets giving M = M_fold/2 :", [sp.nsimplify(s, [sp.sqrt(3)]) for s in sols], " (two distinct offsets -> the modulus folds at Nariai)")
