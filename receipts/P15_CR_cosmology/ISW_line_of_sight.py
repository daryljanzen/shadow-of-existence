"""ISW — THE EARLY INTEGRATED SACHS-WOLFE, ISOLATED, AND ITS SHIFT ON THE FIRST PEAK.
Same shape as everything else in A.0: the source is a line-of-sight integral over the set rate.
   Delta_l(k) = INT d eta [ S_SW + S_ISW ] j_l(k(eta_0 - eta)),   S_ISW = (Phi' + Psi') = 2 Psi'
LambdaCDM has a nonzero early ISW because Psi is still evolving at recombination (radiation matters).
CR does not: C11 showed Psi is constant on L1.  So the QUESTION is how much of ell_1 = 220 is ISW.
ORIGIN: storyboard_receipts/ISW_line_of_sight.py -- registered r2376 (c54); edit the origin, not this copy."""
import numpy as np
from scipy.integrate import quad
from scipy.special import spherical_jn
c=299792.458
Om=0.307; H0=67.4; OL=1-Om; z_eq=3403.6; Or=Om/(1+z_eq); a_eq=1/(1+z_eq)
z_rec=1089.9; a_rec=1/(1+z_rec)
H=lambda a: H0*np.sqrt(Or/a**4+Om/a**3+OL)
def eta_of(a):
    v,_=quad(lambda x: c/(x**2*H(x)), 1e-9, a, limit=200); return v
eta_rec=eta_of(a_rec); eta_0=eta_of(1.0)
print("="*80); print("ISW — ISOLATED, AND ITS EFFECT ON THE FIRST PEAK"); print("="*80)
print(f"\n  eta_rec={eta_rec:.1f}  eta_0={eta_0:.1f}  D = {eta_0-eta_rec:.1f} Mpc")
# the standard growing-mode potential across equality (used in C11)
def Psi_of_a(a):
    y=a/a_eq
    return (9/10)*((16*np.sqrt(1+y)+9*y**3+2*y**2-8*y-16)/(10*y**3))
print(f"\n  Psi/Psi_rad:  at equality {Psi_of_a(a_eq):.4f}   at recombination {Psi_of_a(a_rec):.4f}"
      f"   asymptote {Psi_of_a(100*a_eq):.4f}")
dec=(Psi_of_a(a_rec)-Psi_of_a(1e4*a_eq))/Psi_of_a(1e4*a_eq)
print(f"  -> at recombination Psi is still {100*dec:+.2f}% above its asymptote: that residual decay is the ISW")
# --- r2376+c54.160: PIN THE SOURCE OF THE EFFECT.  The paper (sec:envelope-consequence) says that in
# flat LambdaCDM "the potential is still some four per cent above its asymptote at recombination, and
# that residual decay is what the line-of-sight integral picks up".  That four per cent IS the early
# ISW this receipt isolates, so it is pinned rather than printed.
assert abs(100*dec - 4.02) < 0.05, f"Psi excess at recombination = {100*dec}%"
assert abs((eta_0 - eta_rec) - 14008.3) < 2.0, f"comoving distance to last scattering = {eta_0-eta_rec}"
# dPsi/d eta
def dPsi_deta(a):
    h=a*1e-4
    dPda=(Psi_of_a(a+h)-Psi_of_a(a-h))/(2*h)
    return dPda*(a**2*H(a)/c)          # d a/d eta = a^2 H/c
# line-of-sight, thin-source SW + ISW after recombination
def Delta_l(l, k, with_isw=True):
    # SW: (Theta0+Psi) at recombination, take the standard (1/3)Psi_rec for the plateau normalisation
    sw = (1/3)*Psi_of_a(a_rec)*spherical_jn(l, k*(eta_0-eta_rec))
    if not with_isw: return sw
    def integ(a):
        e=eta_of(a)
        return 2*dPsi_deta(a)*spherical_jn(l, max(k*(eta_0-e),0.0))*(c/(a**2*H(a)))
    v,_=quad(integ, a_rec, min(20*a_eq,1.0), limit=60)
    return sw+v
print("\n  contribution of the post-recombination ISW to Delta_l, at the first-peak scale:")
ls=[150,180,200,220,240,260,300]
print(f"  {'l':>5s} {'SW only':>12s} {'SW+ISW':>12s} {'ISW share':>11s}")
for l in ls:
    k=l/(eta_0-eta_rec)
    a=Delta_l(l,k,False); b=Delta_l(l,k,True)
    print(f"  {l:>5d} {a:>12.5e} {b:>12.5e} {100*(b-a)/abs(a) if a!=0 else 0:>10.2f}%")
    # r2376+c54.160: THE FLATNESS IS THE CLAIM.  The paper (sec:refit-bound) reads this table as
    # "a nearly flat multiplicative factor across the first-peak region -- some ten per cent in
    # amplitude, varying by two parts in a hundred between ell=150 and ell=300", which is why the
    # ISW displaces the first peak by one or two multipoles and not by tens.  Both ends pinned:
    # the ~10% amplitude, and the ~2.3-point spread that makes it flat.
    if l == 150:
        assert abs(100*(b-a)/abs(a) + 10.95) < 0.20, f"ISW share at l=150 = {100*(b-a)/abs(a)}%"
    if l == 300:
        assert abs(100*(b-a)/abs(a) + 8.67) < 0.20, f"ISW share at l=300 = {100*(b-a)/abs(a)}%"
