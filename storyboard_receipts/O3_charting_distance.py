"""O3 — is r_obs = sqrt7/2 a charting device, and does the triple-angle survive another chart?
P3: r_0 = R sin w with image radius R = tan(theta) = 1/sqrt(r_obs^2 - 1);
    R is FORCED to 2/sqrt3 by the requirement that 2M = r_0 - r_0^3 linearise to a pure sin 3w."""
import numpy as np, sympy as sp
w,R = sp.symbols('w R', positive=True)

print("="*78); print("O3 — IS THE CHARTING DISTANCE A GAUGE, AND IS THE TRIPLE-ANGLE CHART-FREE?"); print("="*78)
print("\nSTEP 1 — the forcing, re-derived:")
r0 = R*sp.sin(w)
twoM = sp.expand(r0 - r0**3)
print("   2M = r_0 - r_0^3 =", twoM)
expanded = sp.expand(sp.simplify(twoM.rewrite(sp.sin).expand(trig=True)))
print("   and  sin(3w) = 3 sin w - 4 sin^3 w")
print("   matching  R sin w - R^3 sin^3 w  to  C(3 sin w - 4 sin^3 w):")
Rs = sp.solve(sp.Eq(R/3, R**3/4), R)
print(f"   R/3 = R^3/4  =>  R = {[sp.nsimplify(x) for x in Rs if x>0]}   =  {float(2/np.sqrt(3)):.10f}")
print("   *** so R = 2/sqrt3 is the UNIQUE image radius giving a pure triple angle. ***")
# r2376+c54.159 -- PINS STEP 1's forcing, the figure INDEX quotes: R/3 = R^3/4 has exactly ONE
# positive solution and it is R = 2/sqrt3 = 1.1547005384, so the image radius is forced, not chosen.
_Rpos = [float(x) for x in Rs if x > 0]
assert len(_Rpos) == 1, _Rpos
assert abs(_Rpos[0] - 1.1547005384) < 1e-9, _Rpos
# and it is the image radius of P3's own charting distance r_obs = sqrt7/2 = 1.3228756555
assert abs(1/np.sqrt((np.sqrt(7)/2)**2 - 1) - 1.1547005384) < 1e-9

print("\nSTEP 2 — what happens at ANY OTHER charting distance?  The residual harmonic:")
print(f"   {'r_obs':>9s} {'R=1/sqrt(r^2-1)':>17s} {'2M(w) in harmonics':>44s}")
_harm = []                                      # r2376+c54.159: keep the printed harmonic rows
for r_obs in [np.sqrt(7)/2, 1.2, 1.5, 2.0, 3.0]:
    Rv = 1/np.sqrt(r_obs**2-1)
    expr = sp.expand((Rv*sp.sin(w) - (Rv*sp.sin(w))**3).rewrite(sp.cos).expand(trig=True))
    f = sp.simplify(sp.fourier_series(sp.lambdify, ) ) if False else None
    # project onto sin w and sin 3w
    a1 = sp.integrate(sp.expand_trig(Rv*sp.sin(w) - (Rv*sp.sin(w))**3)*sp.sin(w), (w,0,2*sp.pi))/sp.pi
    a3 = sp.integrate(sp.expand_trig(Rv*sp.sin(w) - (Rv*sp.sin(w))**3)*sp.sin(3*w), (w,0,2*sp.pi))/sp.pi
    tag = "  <- P3's" if abs(Rv-2/np.sqrt(3))<1e-9 else ""
    _harm.append((r_obs, Rv, float(a1), float(a3)))     # r2376+c54.159: keep the printed row
    print(f"   {r_obs:9.6f} {Rv:17.10f}   {float(a1):+.6f}.sin(w) {float(a3):+.6f}.sin(3w){tag}")
# r2376+c54.159 -- PINS STEP 2, the two figures INDEX quotes for the r_obs = sqrt7/2 row: the
# sin(w) coefficient is +0.000000 and the sin(3w) coefficient is +0.384900 = 2/(3 sqrt3).  And the
# qualifying half: at EVERY other charting distance the sin(w) coefficient is nonzero (|a1| > 0.3),
# so the triple-angle FORM does not survive another chart.
assert len(_harm) == 5, _harm
assert abs(_harm[0][1] - 1.1547005384) < 1e-9, _harm[0]
assert abs(_harm[0][2]) < 1e-9, _harm[0]                       # a1 = +0.000000 at P3's chart
assert abs(_harm[0][3] - 0.3849001795) < 1e-9, _harm[0]        # a3 = +0.384900 = 2/(3 sqrt3)
assert all(abs(a1v) > 0.3 for _, _, a1v, _ in _harm[1:]), _harm
assert abs(_harm[3][2] - 0.4330127019) < 1e-9, _harm[3]        # the r_obs = 2.0 row's +0.433013
print("\n   => at R = 2/sqrt3 the sin(w) coefficient VANISHES and only sin(3w) survives.")
print("      At any other charting distance BOTH harmonics are present:")
print("      the triple-angle relation DOES NOT SURVIVE another chart.")
