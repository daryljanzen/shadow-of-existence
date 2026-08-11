"""O6 — the eikonal ringdown at the forced member.
Cardoso et al. 2009:  omega_QNM = Omega_c . l  -  i (n+1/2) |lambda|
  Omega_c = sqrt(f(r_ph))/r_ph   (orbital angular velocity of the circular null geodesic)
  lambda  = Lyapunov exponent,  lambda^2 = f(r_ph)[2f(r_ph) - r_ph^2 f''(r_ph)] / (2 r_ph^2)
f = 1 - 2M/r - r^2/alpha^2,  alpha = 1,  r_ph = 3M,  Nariai at M = 1/(3 sqrt3).
ORIGIN: storyboard_receipts/O6_eikonal_ringdown.py -- registered r2376 (c54); edit the origin, not this copy."""
import numpy as np, sympy as sp
r,M = sp.symbols('r M', positive=True)
f  = 1 - 2*M/r - r**2
Mn = 1/(3*sp.sqrt(3))
rph = 3*M
Om  = sp.sqrt(f.subs(r,rph))/rph
lam = sp.sqrt(sp.simplify(f*(2*f - r**2*sp.diff(f,r,2))/(2*r**2)).subs(r,rph))

print("="*78); print("O6 — THE EIKONAL RINGDOWN AT THE FORCED MEMBER"); print("="*78)
print("\nSTEP 1 — both parts of the eikonal QNM at Nariai:")
print(f"   Omega_c(Nariai) = {sp.simplify(Om.subs(M,Mn))}")
print(f"   lambda (Nariai) = {sp.simplify(lam.subs(M,Mn))}")
print("   => omega_QNM = 0.l - i(n+1/2).0 = 0.   THE WHOLE EIKONAL SPECTRUM COLLAPSES.")

print("\nSTEP 2 — but BOTH vanish, so the RATIOS are the physical content.")
print("   Compare with the surface gravity kappa = f'(r_h)/2 at the inner (black-hole) horizon.")
print(f"\n   {'M/M_N':>7s} {'Omega_c':>11s} {'lambda':>11s} {'kappa':>11s} {'lambda/kappa':>13s} {'Omega_c/kappa':>14s}")
def kap(Mv):
    rts=np.sort([x.real for x in np.roots([-1,0,1,-2*Mv]) if abs(x.imag)<1e-9])
    pos=[x for x in rts if x>0]
    if not pos: return np.nan
    rh=pos[0]
    return float(sp.lambdify(r, sp.diff(f,r).subs(M,Mv))(rh)/2)
Omf=sp.lambdify(M,Om,'numpy'); lamf=sp.lambdify(M,lam,'numpy')
for frac in [0.5,0.8,0.95,0.99,0.999,0.9999]:
    Mv=float(Mn)*frac
    O=float(Omf(Mv)); L=float(lamf(Mv)); K=kap(Mv)
    print(f"   {frac:7.4f} {O:11.6f} {L:11.6f} {K:11.6f} {L/K:13.8f} {O/K:14.8f}")
print("\nSTEP 3 — the limits, symbolically:")
eps = sp.symbols('epsilon', positive=True)
Mser = Mn*(1-eps)
print("   expanding about Nariai in eps = 1 - M/M_N:")
for name,expr in [('Omega_c',Om),('lambda',lam)]:
    ser=sp.series(sp.simplify(expr.subs(M,Mser)), eps, 0, 2).removeO()
    print(f"     {name:8s} ~ {sp.simplify(ser)}")

print("\n" + "="*78)
print("STEP 4 — Omega_c and lambda are EQUAL AT EVERY MEMBER, not only in the limit.")
print("   Omega_c^2 = f/r^2 ;  lambda^2 = f[2f - r^2 f'']/(2r^2).  Equal iff  2f - r^2 f'' = 2.")
expr = sp.simplify(2*f - r**2*sp.diff(f,r,2))
print(f"   2f - r^2 f''  =  {expr}      <- identically 2, for ALL r and ALL M")
print(f"   so  lambda^2 - Omega_c^2  =  {sp.simplify(lam**2 - Om**2)}")
print("\n   *** Omega_c = lambda IDENTICALLY on this family. ***")
print("   Therefore  omega_QNM = Omega_c.l - i(n+1/2)lambda = lambda.[ l - i(n+1/2) ] ,")
print("   so the eikonal QUALITY FACTOR  Q = Re/|Im| = l/(n+1/2)  is INDEPENDENT of M and alpha:")
for l_,n_ in [(2,0),(3,0),(2,1),(10,0)]:
    print(f"     l={l_}, n={n_}:  Q = {l_/(n_+0.5):.4f}   (same at every member of the family)")

print("\nSTEP 5 — and lambda/kappa -> 1 at the forced member (from the table above).")
print("   So at Nariai the ringdown's DAMPING RATE equals the SURFACE GRAVITY, and both vanish.")
print("\n" + "="*78)
print("RESULT O6:")
print("  (a) Omega_c = lambda identically, so the eikonal ringdown's SHAPE -- the quality")
print("      factor l/(n+1/2) -- is universal across the whole SdS family, independent of")
print("      M and alpha.  Only its SCALE, lambda, varies.")
print("  (b) At the member CR forces, that scale is ZERO: Omega_c = lambda = 0, and")
print("      lambda/kappa -> 1, so the damping rate equals the surface gravity as both vanish.")
print("  (c) READ IN CR's TERMS: the forced member is the one with a ringdown of universal")
print("      shape and zero scale -- i.e. NO RINGDOWN.  The observational signature by which")
print("      a black hole announces a completed horizon is absent at exactly the member the")
print("      framework says a collapse selects.  Consistency, not a prediction.")
print("="*78)

# =============================================================================================
# r2376+c54.161 -- ASSERTIONS, and they lift the alpha = 1 gauge.  RESULT (a) claims the quality
# factor is independent of M AND alpha, but line 9 sets f = 1 - 2M/r - r^2, i.e. alpha = 1
# throughout, so the alpha half was never run.  Below, with alpha SYMBOLIC:
#   2f - r^2 f'' = 2 identically (in r, M and alpha) -- the identity the whole result turns on;
#   lambda^2 - Omega_c^2 = 0 at r_ph = 3M for every M and alpha;
#   Q = Omega_c.l / [(n+1/2) lambda] = l/(n+1/2) evaluated numerically at alpha = 2.5 and 7.3;
#   and lambda/kappa = 0.99461174 at M/M_N = 0.9999 -- the table's last row, recomputed at
#   alpha = 2.5, where kappa comes from the horizon cubic r^3 - alpha^2 r + 2M alpha^2 = 0.
assert sp.simplify(expr - 2) == 0                                    # the printed identity
assert sp.simplify(lam**2 - Om**2) == 0
assert sp.simplify(Om.subs(M, Mn)) == 0 and sp.simplify(lam.subs(M, Mn)) == 0
al_g = sp.Symbol('alpha_g', positive=True)
f_g = 1 - 2*M/r - r**2/al_g**2
assert sp.simplify(2*f_g - r**2*sp.diff(f_g, r, 2) - 2) == 0         # ** for ALL r, M and alpha **
Om_g = sp.sqrt(f_g.subs(r, 3*M))/(3*M)
lam_g = sp.sqrt(sp.simplify(f_g*(2*f_g - r**2*sp.diff(f_g, r, 2))/(2*r**2)).subs(r, 3*M))
assert sp.simplify(lam_g**2 - Om_g**2) == 0                          # Omega_c = lambda, any alpha
Omg = sp.lambdify((M, al_g), Om_g); lamg = sp.lambdify((M, al_g), lam_g)
dfg = sp.lambdify((r, M, al_g), sp.diff(f_g, r))
for al_v in (1.0, 2.5, 7.3):
    Mn_v = al_v/(3*np.sqrt(3))
    for frac_v in (0.5, 0.99, 0.9999):
        Mv = Mn_v*frac_v
        O_v, L_v = float(Omg(Mv, al_v)), float(lamg(Mv, al_v))
        assert abs(O_v - L_v) < 1e-12                                # equal at every member
        for l_v, n_v in [(2, 0), (3, 0), (2, 1), (10, 0)]:
            assert abs(O_v*l_v/((n_v + 0.5)*L_v) - l_v/(n_v + 0.5)) < 1e-9   # Q, M- and alpha-free
        rts_v = np.roots([1.0, 0.0, -al_v**2, 2*Mv*al_v**2])
        rh_v = min(x.real for x in rts_v if abs(x.imag) < 1e-9 and x.real > 0)
        kap_v = dfg(rh_v, Mv, al_v)/2
        assert kap_v > 0 and L_v < kap_v                             # damping below surface gravity
        if abs(frac_v - 0.9999) < 1e-12:
            assert abs(L_v/kap_v - 0.99461174) < 1e-7                # the table's last row, any alpha
        if abs(frac_v - 0.5) < 1e-12:
            assert abs(L_v/kap_v - 0.78986169) < 1e-7
assert abs(float(lamg(float(Mn)*0.9999, 1.0)) - 0.014143) < 1e-6      # the alpha = 1 table row
print("  [r2376+c54.161] asserted with alpha SYMBOLIC: 2f - r^2 f'' = 2 identically, Omega_c =")
print("  lambda at every M and alpha, Q = l/(n+1/2) at alpha = 1, 2.5, 7.3, and lambda/kappa =")
print("  0.99461174 at M/M_N = 0.9999 -- the same number at every alpha, as the row claims.")
