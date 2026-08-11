"""
P16_freezeout_trev_toy.py -- verifies the P16 sec:trev claim that freeze-out is TIME-REVERSAL VIOLATING and
  lives only on the COOLING leg: "run it cooling and a relic survives; run the same network heating and the
  abundance tracks equilibrium to zero." A minimal Boltzmann abundance Y competing against the Hubble rate:
    dY/dx = -(Gamma/H)(Y - Y_eq)/x ,   x = Delta/T (clock),  Y_eq = exp(-x) (Boltzmann-suppressed),
    Gamma/H = (Gamma0/H) x^{-n}  (interaction rate falls below H as the layer dilutes/cools -> freeze-out).
  Same equation, same rates, ONLY the direction of T reversed:
    COOLING (x: small->large, T falling): Y tracks Y_eq until Gamma~H, then FREEZES at a relic Y_inf >> Y_eq.
    HEATING (x: large->small, T rising):   Gamma/H rises, equilibrium is (re)established, Y -> Y_eq -> tracks
                                           to the high-T value, leaving NO relic above equilibrium.
  DISCRIMINATING CONTROL is the pair itself: identical network, opposite time-arrow -> relic vs no relic.
RUN: python3 P16_freezeout_trev_toy.py   RUNTIME: <1s
ORIGIN: built new r1403 (sec:trev asserted "a Boltzmann two-species toy confirms" -- unreceipted; built here).
"""
import numpy as np
from scipy.integrate import solve_ivp
def Yeq(x): return np.exp(-x)                      # Boltzmann-suppressed equilibrium -> 0 as T->0 (x->inf)
GAMMA0_over_H, n = 50.0, 2.0                        # Gamma/H = 50 x^-2 : drops below 1 (freeze-out) at x~7
def ratio(x): return GAMMA0_over_H*x**(-n)         # Gamma/H
def rhs(x,Y): return [-(ratio(x)/x)*(Y[0]-Yeq(x))]
def jac(x,Y): return [[-(ratio(x)/x)]]             # analytic Jacobian (stiff)
x_fo=np.sqrt(GAMMA0_over_H)
print("="*70); print("P16 sec:trev -- freeze-out is time-reversal violating (cooling-leg only)"); print("="*70)
print(f"  freeze-out at x=Delta/T ~ {x_fo:.1f} (Gamma/H=1);  Gamma/H = {GAMMA0_over_H:.0f} x^-{n:.0f}")

# COOLING leg: x 1->50 (T falling), start in equilibrium
c=solve_ivp(rhs,[1.0,50.0],[Yeq(1.0)],method="Radau",jac=jac,rtol=1e-10,atol=1e-18,dense_output=True)
Y_relic=c.y[0,-1]; cool_ratio=Y_relic/Yeq(50.0)
print(f"\n  COOLING (T falling, x:1->50): relic Y_inf={Y_relic:.3e}, Y_eq(50)={Yeq(50.0):.2e}")
print(f"    -> Y_inf/Y_eq(final) = {cool_ratio:.2e}   RELIC SURVIVES (frozen far above equilibrium)")

# HEATING leg: same network, x 50->1 (T rising), started from the relic
h=solve_ivp(rhs,[50.0,1.0],[Y_relic],method="Radau",jac=jac,rtol=1e-10,atol=1e-18,dense_output=True)
# max departure from equilibrium along the heating leg (the tracking metric)
xs=np.linspace(2.0,1.0,200); Yh=h.sol(xs)[0]; heat_dev=np.max(np.abs(Yh/Yeq(xs)-1.0))
Y_hot=h.y[0,-1]
print(f"\n  HEATING (T rising, x:50->1, SAME network, from the relic): final Y={Y_hot:.3e}, Y_eq(1)={Yeq(1.0):.3e}")
print(f"    -> Y/Y_eq stays O(1) (max deviation {heat_dev:.2f} over x=1..2); equilibrium (re)established, NO relic")

print(f"\n  DISCRIMINATOR: cooling Y/Y_eq = {cool_ratio:.1e}  vs  heating Y/Y_eq = O(1) ({Y_hot/Yeq(1.0):.2f})")
ok = (cool_ratio > 1e10) and (heat_dev < 0.5)
print("="*70)
print("RESULT:", "PASS -- identical network, opposite time-arrow: COOLING freezes a relic ~1e19x equilibrium;\n         HEATING re-establishes equilibrium (O(1), no relic). Freeze-out is time-reversal violating, so it\n         lives only on the cooling leg -- the collapse turnaround is the event that makes the abundances." if ok else f"FAIL (cool={cool_ratio:.1e}, heat_dev={heat_dev:.2f})")
print("="*70)

# --- ASSERTIONS (added r2376+c54.158) --------------------------------------------------------
# Pins the discriminating pair this receipt prints for sec:trev (INDEX row: cooling freezes a
# relic 6e19x equilibrium; heating re-establishes equilibrium at Y/Y_eq = 1.00, no relic).
# (a) the file's own PASS/FAIL boolean.
assert ok, "P16 trev toy: the cooling/heating discriminator FAILED"
# (b) COOLING: the relic freezes at Y_inf = 1.197e-2, i.e. 6.21e19 times the final equilibrium.
assert abs(Y_relic - 1.19732e-2) < 1e-6
assert abs(cool_ratio/1e19 - 6.2078) < 5e-3
# (c) HEATING: same network, opposite arrow -- the abundance tracks equilibrium (Y/Y_eq = 0.998),
#     so no relic survives; the max departure over x=1..2 is 0.148.
assert abs(Y_hot/Yeq(1.0) - 0.99814) < 1e-4
assert abs(heat_dev - 0.14835) < 1e-4
# (d) and the two legs differ by ~20 orders of magnitude -- the time-reversal violation itself.
assert cool_ratio/(Y_hot/Yeq(1.0)) > 1e15
