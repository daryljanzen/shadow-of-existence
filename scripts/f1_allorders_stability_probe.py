# F1 live edge (c20): all-orders nonlinear stability of the PROPAGATING graviton.
# Three exact (symbolic) questions, NOT numerics (the dS blow-up is stiff per gowdy_ds_lambda_pos_shear.py):
#  (1) does sec.10's conserved shear charge survive in the full propagating system?
#  (2) is the graviton reduced-energy density positive-definite (no ghost to any order)?
#  (3) is the lab-frame graviton energy monotone, or does the expansion do work (the honest gap)?
import sympy as sp
t,z,Lam = sp.symbols('t z Lambda', real=True, positive=True)
psi=sp.Function('psi')(t,z); gam=sp.Function('gamma')(t,z); R=sp.Function('R')(t,z)
src=R*sp.exp(2*(gam-psi))
AREA = sp.diff(R,t,2)-sp.diff(R,z,2) - 2*Lam*src
WAVE = sp.diff(R*sp.diff(psi,t),t)-sp.diff(R*sp.diff(psi,z),z) - Lam*src

print("=== (1) propagating conserved current: does AREA - 2*WAVE become a continuity equation? ===")
combo = sp.simplify(AREA - 2*WAVE)
Jt = sp.diff(R,t) - 2*R*sp.diff(psi,t)     # candidate time-component
Jz = sp.diff(R,z) - 2*R*sp.diff(psi,z)     # candidate z-flux
cont = sp.simplify(combo - (sp.diff(Jt,t) - sp.diff(Jz,z)))
print("  AREA - 2WAVE  - [ d/dt(R_t-2R psi_t) - d/dz(R_z-2R psi_z) ] =", cont)
print("  => on shell  d/dt(R_t-2R psi_t) = d/dz(R_z-2R psi_z):  the Lam source CANCELS, and this is a")
print("     CONTINUITY equation. Integrate over periodic z (flux integrates to 0):")
print("     d/dt INT (R_t - 2 R psi_t) dz = 0  -> the sec.10 shear charge is conserved in the FULL")
print("     PROPAGATING nonlinear system, not just the homogeneous sector. [exact, all orders]\n")

print("=== (2) graviton reduced-energy density positive-definite? (p_psi^2/8R + 2R psi_z^2) ===")
ppsi=4*R*sp.diff(psi,t)
e_grav = sp.simplify(ppsi**2/(8*R) + 2*R*sp.diff(psi,z)**2)
print("  e_grav = p_psi^2/(8R) + 2R psi_z^2 =", e_grav)
print("  = 2R(psi_t^2 + psi_z^2) >= 0 for R>0  -> POSITIVE-DEFINITE. The graviton sector carries no")
print("     negative-energy/ghost direction to ANY order; the indefiniteness in H (the -p_g p_R/2 clock")
print("     cross-term) lives purely in the area/clock sector, which deparametrizes out in cosmic time.\n")

print("=== (3) lab-frame graviton energy flux: monotone, or does expansion do work? (the honest test) ===")
# E = INT R(psi_t^2+psi_z^2) dz ; de/dt, drop d/dz(...) total derivatives (periodic z), use WAVE for psi_tt
e = R*(sp.diff(psi,t)**2+sp.diff(psi,z)**2)
ddt = sp.diff(e,t)
# substitute R*psi_tt from WAVE: (R psi_t)_t-(R psi_z)_z=Lam*src => R psi_tt = (R psi_z)_z + Lam*src - R_t psi_t
Rpsitt = sp.diff(R*sp.diff(psi,z),z) + Lam*src - sp.diff(R,t)*sp.diff(psi,t)
ddt = ddt.subs(sp.diff(psi,t,2), Rpsitt/R)
ddt = sp.simplify(sp.expand(ddt))
# strip total z-derivative d/dz(2 R psi_z psi_t)
flux = sp.diff(2*R*sp.diff(psi,z)*sp.diff(psi,t), z)
bulk = sp.simplify(ddt - flux)
print("  de/dt (mod d/dz flux) =", bulk)
print("  => dE/dt = INT [ -R_t psi_t^2 + R_t psi_z^2 + 2 Lam R e^{2(g-p)} psi_t ] dz")
print("     SIGN-INDEFINITE: expansion R_t>0 and the Lam-source work term carry both signs. So lab-frame")
print("     energy is NOT monotone -- as expected on an expanding background (the expansion does work).")
print("     The honest gap: positive-definiteness + the conserved charge rule out ghost/zero-mode runaway")
print("     to all orders, but a monotone no-hair law for the PROPAGATING energy does not fall out here.")
