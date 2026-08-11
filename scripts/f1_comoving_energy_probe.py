# F1 live edge (c20), the bite: find the monotone object for the propagating sector.
# Candidate: the POSITIVE-DEFINITE full graviton energy (kinetic+gradient+potential),
# E = INT [ 2R(psi_t^2+psi_z^2) + 2 Lam R e^{2(g-p)} ] dz   (potential V=Lam R e^{2(g-p)} >=0, bounded below).
# Compute dE/dt on shell (full nonlinear eqs), drop d/dz(total) (periodic z), check the sign structure.
import sympy as sp
t,z,Lam = sp.symbols('t z Lambda', real=True, positive=True)
psi=sp.Function('psi')(t,z); gam=sp.Function('gamma')(t,z); R=sp.Function('R')(t,z)
pt,pz=sp.diff(psi,t),sp.diff(psi,z); gt,gz=sp.diff(gam,t),sp.diff(gam,z); Rt,Rz=sp.diff(R,t),sp.diff(R,z)
src=R*sp.exp(2*(gam-psi))
# on-shell second derivatives:
psitt = (sp.diff(R*pz,z) + Lam*src - Rt*pt)/R            # from WAVE
Rtt   = sp.diff(R,z,2) + 2*Lam*src                       # from AREA
gtt   = sp.diff(gam,z,2) - pt**2 + pz**2 + Lam*sp.exp(2*(gam-psi))  # from gamma-eq

def onshell_dt(dens):
    e = sp.diff(dens,t)
    e = e.subs(sp.diff(psi,t,2), psitt).subs(sp.diff(R,t,2), Rtt).subs(sp.diff(gam,t,2), gtt)
    return sp.expand(e)

print("=== candidate E = INT [2R(psi_t^2+psi_z^2) + 2 Lam R e^{2(g-p)}] dz  (positive-definite) ===")
dens = 2*R*(pt**2+pz**2) + 2*Lam*src
ddt = onshell_dt(dens)
# strip total z-derivatives: subtract d/dz of the natural flux 4 R psi_t psi_z
flux = sp.diff(4*R*pt*pz, z)
bulk = sp.simplify(ddt - flux)
print("  dE/dt density (mod d/dz flux) =", bulk)
print()
# try to use the ENERGY + MOMENTUM constraints to simplify the bulk
ENERGY = 2*(Rt*gt+Rz*gz)-(Rtt+sp.diff(R,z,2)) - 2*R*(pt**2+pz**2)   # =0 on shell (note Rtt on-shell)
MOM    = Rt*gz+Rz*gt-sp.diff(R,t,z) - 2*R*pt*pz                      # =0 on shell
print("  constraints (=0 on shell): ENERGY, MOMENTUM available to reduce the bulk.")
# express bulk, then reduce modulo constraints by polynomial reduction in gt
bulk2 = sp.simplify(bulk)
print("  simplified bulk =", bulk2)

print("\n=== CONCLUSION OF THE BITE (outcome b: the monotone-energy route does not close it) ===")
print("""
 dE/dt = INT[ 4 Lam R e^{2(g-p)} g_t + 2 Lam R_t e^{2(g-p)} - 2 R_t(psi_t^2 - psi_z^2) ] dz.
 Sign-INDEFINITE: the R_t,g_t terms are the expansion's work. And on the background
 (psi=psi0) the potential 2 Lam R0 e^{2(g0-p0)} = 2 Lam a^4 GROWS -- this is the TOTAL
 field energy, which includes the de Sitter background's own growing energy. So no
 total-field energy (lab-frame sec.14, or this positive-definite one) is monotone.

 => The right monotone object is NOT the total energy but the GAUGE-INVARIANT
    PERTURBATION energy (the graviton ABOVE the dS background). At LINEAR order that
    object is exactly sec.13's Q, which DECAYS as a^-2 (bounded, no-hair) -- and its
    equation W''+(k^2-2/t^2)W=0 has a MONOTONE coefficient (2/t^2), never periodic,
    so SINGLE-MODE PARAMETRIC RESONANCE IS EXCLUDED at linear order.

 => The residual gap is therefore SHARP and NAMED: the exact NONLINEAR monotonicity of
    the gauge-invariant perturbation = INHOMOGENEOUS COSMIC NO-HAIR. The only open
    instability channel is nonlinear MODE-MODE resonant transfer outpacing the de Sitter
    DETUNING (every mode's frequency redshifts monotonically, detuning resonances). That
    is a frontier question of mathematical GR (future stability of de Sitter), NOT closed
    by any simple exact energy here -- stays do-not-assert, both ways. [bite = outcome b]
""")
