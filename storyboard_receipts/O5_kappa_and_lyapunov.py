"""O5 — what coincides at r = alpha/sqrt3 at Nariai, and does the photon orbit's INSTABILITY
vanish with the surface gravity?   f = 1 - 2M/r - r^2/alpha^2, alpha = 1."""
import numpy as np, sympy as sp
r,M = sp.symbols('r M', positive=True)
f = 1 - 2*M/r - r**2
Mn = 1/(3*sp.sqrt(3))

print("="*78); print("O5 — THE DEGENERATE HORIZON, THE PHOTON SPHERE, AND THE INSTABILITY RATE"); print("="*78)
print("\nSTEP 1 — surface gravity kappa = f'(r_h)/2 at the merged horizon:")
fN=f.subs(M,Mn); rh=1/sp.sqrt(3)
print(f"   f(r_h)   = {sp.simplify(fN.subs(r,rh))}")
print(f"   f'(r_h)  = {sp.simplify(sp.diff(fN,r).subs(r,rh))}   =>  kappa = {sp.simplify(sp.diff(fN,r).subs(r,rh)/2)}")
print(f"   f''(r_h) = {sp.simplify(sp.diff(fN,r,2).subs(r,rh))}   (non-zero: a genuine DOUBLE root, not triple)")

print("\nSTEP 2 — the photon-orbit Lyapunov exponent (the instability rate of the circular null orbit):")
print("   lambda^2 = f(r_ph) . [ 2 f(r_ph) - r_ph^2 f''(r_ph) ] / (2 r_ph^2)")
lam2 = sp.simplify(f*(2*f - r**2*sp.diff(f,r,2))/(2*r**2))
print("   general form:", sp.simplify(lam2))
print(f"   at Nariai, r_ph = 3M = {float(3*Mn):.10f} = r_h:")
val = sp.simplify(lam2.subs({M:Mn, r:rh}))
print(f"   lambda^2 = {val}    =>  lambda = {sp.sqrt(val)}")
print("\n   *** BOTH VANISH: kappa = 0 AND lambda = 0, at the same radius, at the forced member. ***")

print("\nSTEP 3 — is that a coincidence of two zeros, or one zero seen twice?")
print("   lambda^2 carries an overall factor f(r_ph).  At Nariai r_ph = r_h, so f(r_ph) = 0,")
print("   and kappa = f'(r_h)/2 = 0 by the DOUBLE root.  These are two DIFFERENT vanishings:")
print("     kappa = 0   <=  f' = 0   (the root is double)")
print("     lambda = 0  <=  f  = 0   (the photon sphere sits ON the horizon)")
print("   and BOTH hold only because 3M = r_h, which IS the Nariai condition.")

print("\nSTEP 4 — the approach, from below:")
print(f"   {'M/M_Nariai':>11s} {'r_ph=3M':>10s} {'r_h(inner)':>11s} {'kappa':>11s} {'lambda':>11s}")
for frac in [0.5,0.8,0.95,0.99,1.0]:
    Mv=float(Mn)*frac
    fv=sp.lambdify(r, f.subs(M,Mv),'numpy'); dfv=sp.lambdify(r, sp.diff(f,r).subs(M,Mv),'numpy')
    roots=np.sort([x.real for x in np.roots([-1,0,1,-2*Mv]) if abs(x.imag)<1e-9]); pos=[x for x in roots if x>0]
    rh_v=pos[0] if pos else np.nan
    l2=float(sp.lambdify(r, lam2.subs(M,Mv),'numpy')(3*Mv))
    print(f"   {frac:11.3f} {3*Mv:10.6f} {rh_v:11.6f} {dfv(rh_v)/2:11.6f} {np.sqrt(max(l2,0)):11.6f}")

# =============================================================================================
# r2376+c54.161 -- ASSERTIONS, and they lift the alpha = 1 gauge.  Everything above was printed;
# and the file fixes alpha = 1 in its very first line (f = 1 - 2M/r - r^2), so the citing
# sentence's "kappa = 0 AND lambda = 0 at the forced member, whatever alpha" was never exercised.
# The second block below redoes STEPS 1-3 with alpha SYMBOLIC: at M = alpha/(3 sqrt3) and
# r = alpha/sqrt3 the metric function has f = 0, f' = 0 and f'' = -6/alpha^2 (a double root, not
# a triple one) and lambda^2 = 0 -- for every alpha, and with the two vanishings still coming
# from the two different conditions.  Three numeric scales are run as well.
assert sp.simplify(fN.subs(r, rh)) == 0                              # f(r_h) = 0
assert sp.simplify(sp.diff(fN, r).subs(r, rh)) == 0                  # kappa = f'/2 = 0
assert sp.simplify(sp.diff(fN, r, 2).subs(r, rh) + 6) == 0           # f'' = -6: DOUBLE root
assert sp.simplify(lam2 - (-2*M - r**3 + r)/r**3) == 0               # the printed general form
assert sp.simplify(val) == 0 and sp.simplify(sp.sqrt(val)) == 0      # lambda = 0 at Nariai
al_g = sp.Symbol('alpha_g', positive=True)
f_g = 1 - 2*M/r - r**2/al_g**2
M_g, rh_g = al_g/(3*sp.sqrt(3)), al_g/sp.sqrt(3)
lam2_g = sp.simplify(f_g*(2*f_g - r**2*sp.diff(f_g, r, 2))/(2*r**2))
assert sp.simplify(f_g.subs({M: M_g, r: rh_g})) == 0                 # ** at ARBITRARY alpha **
assert sp.simplify(sp.diff(f_g, r).subs({M: M_g, r: rh_g})) == 0
assert sp.simplify(sp.diff(f_g, r, 2).subs({M: M_g, r: rh_g}) + 6/al_g**2) == 0
assert sp.simplify(lam2_g.subs({M: M_g, r: rh_g})) == 0
assert sp.simplify(3*M_g - rh_g) == 0                                # r_ph = 3M = r_h: the reason
assert sp.simplify(sp.cancel(lam2_g/f_g).subs(r, 3*M) - 1/(9*M**2)) == 0   # lambda^2 carries f
dfg = sp.lambdify((r, M, al_g), sp.diff(f_g, r))
l2g = sp.lambdify((r, M, al_g), lam2_g)
for al_v in (1.0, 2.5, 7.3):
    Mn_v = al_v/(3*np.sqrt(3))
    assert abs(dfg(al_v/np.sqrt(3), Mn_v, al_v)/2) < 1e-12           # kappa = 0
    assert abs(l2g(al_v/np.sqrt(3), Mn_v, al_v)) < 1e-12             # lambda = 0
    rts_v = np.roots([1.0, 0.0, -al_v**2, 2*0.8*Mn_v*al_v**2])       # BELOW the member: kappa > 0
    rh_below = min(x.real for x in rts_v if abs(x.imag) < 1e-9 and x.real > 0)
    assert dfg(rh_below, 0.8*Mn_v, al_v)/2 > 0.01
    assert abs(dfg(rh_below, 0.8*Mn_v, al_v)/2*al_v - 0.896558) < 1e-5   # kappa.alpha, alpha-free
assert abs(dfg(0.35125978, 0.8*float(Mn), 1.0)/2 - 0.896558) < 1e-5  # the 0.8 row: kappa
assert abs(np.sqrt(l2g(3*0.8*float(Mn), 0.8*float(Mn), 1.0)) - 0.750000) < 1e-6   # ... and lambda
print("\n  [r2376+c54.161] asserted at SYMBOLIC alpha: f = f' = 0 and lambda^2 = 0 at")
print("  M = alpha/(3 sqrt3), r = alpha/sqrt3, with f'' = -6/alpha^2 (double, not triple), and")
print("  numerically at alpha = 1, 2.5, 7.3; the 0.8 row pinned at kappa = 0.896558, lambda = 0.75.")
