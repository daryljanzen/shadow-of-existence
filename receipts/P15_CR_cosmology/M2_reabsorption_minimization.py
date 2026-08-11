"""M2 — THE MINIMIZATION.  Can a parameter refit absorb the damping shape?
The honest core of the likelihood question, done on the closed forms derived in C8/C9 -- no CAMB.
SETUP, stated before running:
  FREE      : Omega_m, omega_b, and the inherited datum rho_r/rho_m (which fixes z_onset).
  CONSTRAINT: l_* = pi D_M/r_s pinned to the observed 301 -- the peak positions are measured.
  OBJECTIVE : drive theta_D/theta_* back to LambdaCDM's value.
  PRIORS    : omega_b to 1% (primordial deuterium); Omega_m to 5% (BAO/lensing).
IF the residual goes to zero the signature is reabsorbable and the exposure dissolves.
IF it floors, THAT FLOOR IS THE PREDICTION -- derived, not quoted.
ORIGIN: storyboard_receipts/M2_reabsorption_minimization.py -- registered r2376 (c54); edit the origin, not this copy."""
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq, minimize
c=299792.458; H0=67.4
z_rec=1100.0; a_rec=1/(1+z_rec)
omb_fid=0.0224; Om_fid=0.307
print("="*80); print("M2 — CAN A REFIT ABSORB IT?"); print("="*80)
def build(Om, omb, z_onset, radiation):
    OL=1-Om
    a_onset=1/(1+z_onset)
    # rho_r/rho_m at recombination from the seam datum (CR) or from the standard Or (LCDM)
    ratio_rec = 2.0*(1+z_rec)/(1+z_onset)
    Or = Om*ratio_rec*a_rec
    Rb_rec = 0.6*(omb/omb_fid)                       # Rb ~ omega_b
    def Rb_of(a): return Rb_rec*(a/a_rec)
    def H(a): return H0*np.sqrt(Or/a**4*radiation + Om/a**3 + OL)
    lo = a_onset if radiation==0.0 else 1e-9
    rs,_ = quad(lambda a: c/(a**2*H(a)*np.sqrt(3*(1+Rb_of(a)))), lo, a_rec, limit=300)
    def g(a):
        Rb=Rb_of(a); return (Rb**2/(1+Rb)+8/9)/(6*(1+Rb))
    I,_ = quad(lambda a: g(a)/H(a), lo, a_rec, limit=300)
    rD = np.sqrt(I/(omb/omb_fid))                   # r_D^2 ~ 1/n_e0 ~ 1/omega_b
    DM,_= quad(lambda a: c/(a**2*H(a)), a_rec, 1.0, limit=300)
    return rs, rD, DM
# the LambdaCDM target
rs_L, rD_L, DM_L = build(Om_fid, omb_fid, 6797.0, 1.0)
tgt = rD_L/rs_L
print(f"  LambdaCDM target:  r_s={rs_L:.2f} Mpc, l_*={np.pi*DM_L/rs_L:.1f}, (r_D/r_s)={tgt:.6f}")
def cr_state(Om, omb, z_onset):
    rs,rD,DM = build(Om, omb, z_onset, 0.0)
    return rs, rD, DM, np.pi*DM/rs, rD/rs
print("\nSTEP 1 — PIN l_* = 301 BY THE INHERITED DATUM, at each (Om, omb).")
def z_onset_for_lstar(Om, omb, target_lstar=301.0):
    f=lambda z: cr_state(Om, omb, z)[3]-target_lstar
    return brentq(f, 3000., 30000.)
z0=z_onset_for_lstar(Om_fid, omb_fid)
print(f"   at the fiducial (Om={Om_fid}, omb={omb_fid}):  z_onset = {z0:.0f}  (the corpus uses 6797)")
print("\nSTEP 2 — MINIMISE THE RESIDUAL IN theta_D/theta_* OVER THE PRIORS.")
def resid(p):
    Om, omb = p
    try:
        z = z_onset_for_lstar(Om, omb)
        _,_,_,ls,ratio = cr_state(Om, omb, z)
    except Exception:
        return 1e3
    pen = ((omb-omb_fid)/(0.01*omb_fid))**2 + ((Om-Om_fid)/(0.05*Om_fid))**2
    return abs(ratio/tgt-1)*100 + 0.01*pen        # residual in %, lightly penalised toward the priors
r0=minimize(resid, [Om_fid, omb_fid], method='Nelder-Mead',
            options={'xatol':1e-5,'fatol':1e-5,'maxiter':400})
Om_b, omb_b = r0.x
z_b = z_onset_for_lstar(Om_b, omb_b)
_,_,_,ls_b,ratio_b = cr_state(Om_b, omb_b, z_b)
print(f"   start   : Om={Om_fid:.4f} omb={omb_fid:.5f}  ->  residual {resid([Om_fid,omb_fid]):.3f}%")
print(f"   BEST FIT: Om={Om_b:.4f} omb={omb_b:.5f}  z_onset={z_b:.0f}  l_*={ls_b:.1f}")
print(f"   *** RESIDUAL AT THE MINIMUM: {100*abs(ratio_b/tgt-1):.2f}% in theta_D/theta_* ***")
print(f"   (parameter moves: Om {100*(Om_b/Om_fid-1):+.2f}%, omega_b {100*(omb_b/omb_fid-1):+.2f}%)")
# --- r2376+c54.160: PIN THE MINIMISATION.  The paper (sec:refit-bound) states the outcome of THIS
# receipt: the matter density "can [absorb it], but only by moving some thirty-seven per cent, which
# is not a refit but a different cosmology".  Both halves are pinned -- that the minimiser really
# does drive the residual to zero, and that the price is the -36% walk out of the prior.  The
# l_* = 301 constraint is pinned too: a minimum found off the constraint would mean nothing.
assert abs(z0 - 6873.0) < 5.0, f"z_onset from pinning l_*=301 at the fiducial: {z0}"
assert abs(Om_b - 0.1954) < 0.005, f"best-fit Omega_m = {Om_b}"
assert abs(100*(Om_b/Om_fid - 1) + 36.35) < 1.0, f"Omega_m move = {100*(Om_b/Om_fid-1)}%"
assert abs(ls_b - 301.0) < 0.2, f"l_* at the minimum = {ls_b}"
assert 100*abs(ratio_b/tgt - 1) < 0.05, f"residual at the minimum = {100*abs(ratio_b/tgt-1)}%"

print("\n" + "="*80)
print("STEP 3 — THE SOFT PENALTY WAS TOO WEAK AND THE MINIMISER WALKED OUT OF THE PRIOR.")
print("="*80)
print(f"""
  It zeroed the residual -- but at Omega_m = {Om_b:.3f}, a {100*(Om_b/Om_fid-1):+.0f}% move, which BAO, lensing
  and growth exclude many times over.  *** A refit that succeeds outside its priors has not absorbed
  anything; it has changed cosmology. ***  So the useful object is not the minimum but the TRADE-OFF:
  how much residual survives as a function of how far one is willing to move Omega_m.
""")
print(f"   {'Om move':>9s} {'Omega_m':>9s} {'omega_b move':>13s} {'z_onset':>8s} {'residual in theta_D/theta_*':>28s}")
print("   "+"-"*76)
for frac in [0.0,0.02,0.05,0.10,0.20,0.30,0.3687]:
    Om_t=Om_fid*(1-frac)
    # at fixed Om, optimise omega_b alone within its 1% BBN prior
    best=None
    for omb_t in np.linspace(omb_fid*0.99, omb_fid*1.01, 21):
        try:
            z=z_onset_for_lstar(Om_t, omb_t); _,_,_,ls,rat=cr_state(Om_t, omb_t, z)
        except Exception: continue
        r=abs(rat/tgt-1)*100
        if best is None or r<best[0]: best=(r, omb_t, z)
    r,omb_t,z=best
    print(f"   {100*frac:>8.1f}% {Om_t:>9.4f} {100*(omb_t/omb_fid-1):>12.2f}% {z:>8.0f} {r:>26.2f}%")
    # r2376+c54.160: THE FLOOR IS THE PREDICTION, so the floor is pinned.  The paper's sentence
    # this receipt carries (sec:refit-bound) is that minimising over omega_b (1% deuterium) and
    # Omega_m (5% distance/growth) "leaves a residual of several per cent"; here that is 8.41% at
    # no Omega_m move and still 7.54% at the edge of the 5% prior.  If either ever fell to zero
    # the signature would be reabsorbable and the receipt's RESULT line would be false.
    if frac == 0.0:
        assert abs(r - 8.41) < 0.15, f"residual with Omega_m at the fiducial = {r}%"
    if frac == 0.05:
        assert abs(r - 7.54) < 0.15, f"residual at the edge of the 5% Omega_m prior = {r}%"
print("""
  *** READ IT.  WITHIN THE PRIORS -- omega_b to 1% from deuterium, Omega_m to 5% -- THE RESIDUAL
      FLOORS AT SEVERAL PER CENT.  It only vanishes when Omega_m is driven a third of the way down,
      which is not a refit but a different universe. ***
""")
print("STEP 4 — AND A CHECK THAT FELL OUT OF THE SETUP.")
print(f"   Pinning l_* = 301 by the inherited datum alone gives z_onset = {z0:.0f}.")
print(f"   *** THE CORPUS USES 6797.  Agreement to {100*abs(z0-6797)/6797:.2f}%. ***")
print("   That is the acoustic-scale calibration recovered from the derived integrals, and it was")
print("   not the thing being tested -- it is the machinery agreeing with the corpus twice over.")
print("="*80)
print("RESULT M2: the damping signature is NOT reabsorbable by a parameter refit within the priors.")
print("  omega_b cannot do it (1% of freedom against a ~9% effect), and Omega_m can only do it by")
print("  moving ~37%, which independent data exclude.")
print("  *** SO THE FLOOR IS THE PREDICTION: a several-per-cent irreducible shift in theta_D/theta_*,")
print("      derived here from the corpus's own integrals rather than quoted from a file. ***")
print("  WHAT THIS IS NOT: a likelihood. A full comparison fits the whole C_l against the data with")
print("  all parameters and their covariances; this fixes l_* and minimises one derived ratio.  It")
print("  bounds the reabsorption question and does not settle the verdict.")
print("="*80)
