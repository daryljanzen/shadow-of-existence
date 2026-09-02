"""
P15_damping_reabsorption.py -- verifies the P15 sec:coherence claim that the ~9% CR diffusion-scale shift
  does NOT dissolve under the density that would rescale it: r_D ~ omega_b^{-0.31}. Computes the reabsorption
  levers on CAMB thermodynamics (r_s re-anchored to the observed acoustic scale each time, so only r_D moves
  the observable theta_D/theta_*=r_D/r_s):
    d ln(r_D)/d ln(omega_b) = -0.305   (paper's -0.31),  d ln(r_D)/d ln(omega_c) = -0.295.
  The CR shift is +8.9%; cancelling it needs omega_b +29% (or omega_c +30%), vs the ~1%/~2% BBN+peak-height
  priors allow -> NOT reabsorbable (29x/20x the allowed range); a 1% omega_b shifts r_D ~0.3%, well under a %.
  Irreducible residual ~8.2%. The receipt's own broader verdict (a conditional multi-sigma tension IF the CR
  spectrum is otherwise LCDM's) is honestly conditional -- its anti-panic audit notes the same radiation-free
  rate also reshapes the high-ell driving, so the 'IF' is unbuilt; the paper takes only the SETTLED part
  (non-reabsorbable r_D) and flags the observable consequence as open. No overclaim.
STATUS: ✔✔ (r_D ~ omega_b^{-0.305} = paper's -0.31; non-reabsorbable within priors; conditional tension honestly flagged)
RUN: python3 P15_damping_reabsorption.py   RUNTIME: ~60s (needs camb)
ORIGIN: computations/damping_tail/damping_reabsorption.py, verified r1393.
"""
import numpy as np
import camb
from scipy.integrate import simpson
C_KMS = 299792.458

Z_ONSET = 6803.0   # CR cosmogenesis seam: rho_r/rho_m=2 -> z_onset=2*z_eq-1 (z_eq~3402). r_s clock
                   # starts at the seam (P15 sec:tensions / damping_ratio_clean.py), NOT at z=inf.
def scales(ombh2, omch2, rate_radfree, H0=67.36, mnu=0.06, tau=0.0544):
    """r_s (Mpc) and Silk 1/k_D (Mpc) with CAMB thermodynamics for these densities,
    integrated over the chosen expansion rate. For CR (radiation-free) the sound-horizon clock
    starts at the finite-curvature seam z_onset (anchored to the observed acoustic scale), not
    at z=inf -- CR has no radiation era to cap the integral, so integrating to inf is spurious."""
    pars = camb.CAMBparams()
    pars.set_cosmology(H0=H0, ombh2=ombh2, omch2=omch2, mnu=mnu, omk=0, tau=tau)
    pars.InitPower.set_params(As=2.1e-9, ns=0.9649)
    res = camb.get_background(pars); d = res.get_derived_params()
    zstar = d['zstar']
    h = H0/100.; og = 2.47282e-5/h**2
    Om = (ombh2+omch2+mnu/93.14)/h**2
    Or = og + 3.046*(7./8.)*(4./11.)**(4./3.)*og
    OL = 1.0-Om-Or; OL_cr = 1.0-Om
    def H(z):
        if rate_radfree: return H0*np.sqrt(Om*(1+z)**3 + OL_cr)      # radiation-FREE (CR)
        return H0*np.sqrt(Om*(1+z)**3 + Or*(1+z)**4 + OL)           # radiation-full (LCDM)
    def R(z): return 0.75*(ombh2/2.47282e-5)/(1+z)
    # sound horizon: LCDM to high z (radiation era converges); CR from seam z_onset (anchored)
    z_top = Z_ONSET if rate_radfree else 1e6
    zs = np.logspace(np.log10(zstar), np.log10(z_top), 16000)
    cs = 1.0/np.sqrt(3.0*(1.0+R(zs)))
    r_s = simpson(cs/(H(zs)/C_KMS), zs)
    # Silk length: needs tau'(z) = a n_e sigma_T from CAMB (recomputed for these densities)
    zd = np.linspace(zstar, 8000.0, 8000)
    opac = res.get_background_redshift_evolution(zd, ['opacity'], format='array')[:,0]
    Rd = R(zd); br = Rd**2/(1.0+Rd) + 8.0/9.0
    inv_kD2 = simpson((1.0/(H(zd)/C_KMS))*(1.0/(6.0*(1.0+Rd)*opac))*br, zd)
    return r_s, np.sqrt(inv_kD2), zstar    # r_D = 1/k_D (the DIFFUSION LENGTH), = sqrt(1/k_D^2)

# fiducial Planck
ob0, oc0 = 0.02237, 0.1200
print("="*76)
print("A2.3-VERDICT :: reabsorption of the CR damping-tail shift")
print("="*76)
# The observable is theta_D/theta_* = r_D/r_s.  r_s is MATCHED to the observed acoustic scale in
# BOTH frameworks (CR via the inherited datum, LCDM via the radiation-era ruler), so it is the
# common anchor and CANCELS: the CR shift in the observable is the pure diffusion-length ratio.
rsL, rDL, zsL = scales(ob0, oc0, False)      # LCDM: r_D on the radiation-full rate
rsC, rDC, zsC = scales(ob0, oc0, True)       # CR:   r_D on the radiation-free rate
shift = 100*(rDC-rDL)/rDL                     # r_s common -> observable shift = r_D ratio
print(f"\n[fiducial Planck omega_b={ob0}, omega_c={oc0};  r_s matched to observed acoustic scale]")
print(f"  Silk length r_D : LCDM(rad) = {rDL:.4f}   CR(rad-free) = {rDC:.4f} Mpc")
print(f"  CR shift in the observable theta_D/theta_* = {shift:+.2f} %   (the thing to reabsorb)")

# --- reabsorption lever: d ln(r_D)/d ln(omega_b, omega_m) in CR (r_s re-anchored to the observed
#     acoustic scale for each choice, so only r_D moves the observable) ---
def logderiv(param):
    eps=0.03
    if param=='ob':
        rp=scales(ob0*(1+eps),oc0,True); rm=scales(ob0*(1-eps),oc0,True)
    else:
        rp=scales(ob0,oc0*(1+eps),True); rm=scales(ob0,oc0*(1-eps),True)
    return (np.log(rp[1])-np.log(rm[1]))/(2*eps)   # r_D response only (r_s anchored)
dlnob = logderiv('ob'); dlnoc = logderiv('oc')
print(f"\n[reabsorption levers, standard rate]")
print(f"  d ln(theta_D/theta_*) / d ln(omega_b) = {dlnob:+.3f}")
print(f"  d ln(theta_D/theta_*) / d ln(omega_c) = {dlnoc:+.3f}")
need_ob = (-shift/100.)/dlnob      # fractional change in omega_b to cancel the shift
need_oc = (-shift/100.)/dlnoc
print(f"\n[to reabsorb {shift:+.1f}% via ONE lever]")
print(f"  omega_b would need to move {100*need_ob:+.1f} %   (i.e. omega_b -> {ob0*(1+need_ob):.5f})")
print(f"  omega_c would need to move {100*need_oc:+.1f} %   (i.e. omega_c -> {oc0*(1+need_oc):.5f})")

print("""
[what BBN + the CMB peak heights ALLOW]
  omega_b: BBN (deuterium, Cooke 2018) pins omega_b h^2 = 0.02166 +- 0.00015 -> ~0.7%;
           Planck CMB peak-height (odd/even) pins omega_b to ~0.6%. Combined allowance ~1%.
  omega_c: fixed by theta_* + the BAO Omega_m (A1.4/DESI: Omega_m=0.307) + peak heights, ~1-2%.
""")
allow_ob = 0.010   # ~1% combined BBN + peak-height allowance on omega_b
allow_oc = 0.015
print(f"[verdict on reabsorption]")
print(f"  omega_b: need {abs(100*need_ob):.0f}% vs allowed ~{100*allow_ob:.0f}%  ->  "
      f"{'REABSORBABLE' if abs(need_ob)<=allow_ob else f'NOT reabsorbable (need {abs(need_ob)/allow_ob:.0f}x the allowed range)'}")
print(f"  omega_c: need {abs(100*need_oc):.0f}% vs allowed ~{100*allow_oc:.0f}%  ->  "
      f"{'REABSORBABLE' if abs(need_oc)<=allow_oc else f'NOT reabsorbable (need {abs(need_oc)/allow_oc:.0f}x the allowed range)'}")

# --- r2376+c54.160: PIN THE LEVER AND THE VERDICT.  The paper (sec:coherence) cites this receipt
# for exactly one figure -- "r_D ~ omega_b^{-0.31}, so a percent-level omega_b shifts it by well
# under a percent" -- and the INDEX row adds the +8.9% shift, the -0.295 omega_c lever, the +29%
# omega_b move that would be needed, and the ~8.2% irreducible residual.  All are pinned.  The
# NON-REABSORBABILITY is asserted as its own claim: the needed move must stay far outside the prior,
# or the receipt's printed verdict flips to REABSORBABLE with nothing to catch it.
assert abs(rDL - 6.5623) < 0.005, f"LCDM Silk length = {rDL}"
assert abs(rDC - 7.1465) < 0.005, f"CR Silk length = {rDC}"
assert abs(shift - 8.90) < 0.05, f"CR shift in theta_D/theta_* = {shift}%"
assert abs(dlnob + 0.305) < 0.005, f"d ln r_D / d ln omega_b = {dlnob}"      # paper: -0.31
assert abs(dlnoc + 0.295) < 0.005, f"d ln r_D / d ln omega_c = {dlnoc}"
assert abs(100*need_ob - 29.2) < 0.5, f"omega_b move needed = {100*need_ob}%"
assert abs(100*need_oc - 30.2) < 0.5, f"omega_c move needed = {100*need_oc}%"
assert abs(need_ob) > 10*allow_ob and abs(need_oc) > 10*allow_oc, \
    f"a lever came inside its prior: {need_ob} vs {allow_ob}, {need_oc} vs {allow_oc}"
# and the paper's own sentence: one per cent of omega_b buys well under one per cent of r_D
assert abs(dlnob*0.01)*100 < 0.5, f"1% omega_b moves r_D by {abs(dlnob*0.01)*100}%"

# residual after floating omega_b, omega_m to the edge of their allowed priors (best case for CR)
resid = abs(shift) - (abs(dlnob*allow_ob) + abs(dlnoc*allow_oc))*100
# r2376+c54.160: the irreducible residual is the receipt's headline (INDEX: "residual ~8.2%").
assert abs(resid - 8.15) < 0.05, f"irreducible residual = {resid}%"
print(f"\n[residual shift after floating omega_b, omega_c to the EDGE of their priors]")
print(f"  best-case reabsorption from both levers at full allowance: "
      f"{(abs(dlnob*allow_ob)+abs(dlnoc*allow_oc))*100:.2f}%")
print(f"  irreducible residual in theta_D/theta_* : ~{resid:.1f}%")
print("""
[Planck sensitivity -> tension]
  Planck constrains the damping scale theta_D at roughly the ~0.3-0.5% level (the high-l TT
  tail is measured to cosmic-variance + noise across l~1000-2500). An irreducible residual of
  order several percent in theta_D/theta_* is therefore a MULTI-SIGMA effect, not a wash.
""")
print("="*76)
print("""ANTI-PANIC AUDIT (before calling this a refutation -- the r959 face):
 The large residual is real ONLY IF CR is truly committed to the radiation-free rate through
 recombination. Audit the imported assumptions:
  (1) Is r_D genuinely radiation-free in CR?  YES -- P15 sec:coherence commits it: recombination
      is observable cosmology from the seam outward, an L1 quantity; 'one may not take the rate
      radiation-free for the peak spacing and radiation-included for the diffusion.'  So the
      shift is a genuine CR prediction, not an artifact -- it does NOT dissolve on audit.
  (2) Does the same radiation-free rate shift the PEAK HEIGHTS too (not just theta_D)?  If the
      early-ISW / potential-envelope also moves, the whole high-l fit shifts and the heights-
      match claim (P15: 'Argued', digit-level confirmation OPEN) is where the real test lives.
      This is the honest locus: the damping tail is one facet of a full-transfer question the
      corpus already lists as its open frontier.
 CONCLUSION (not claimed for the sign of the final verdict, asserted on the magnitude):
  the +8.9% is NOT reabsorbable by omega_b/omega_m within BBN+height priors, so IF CR's spectrum
  is otherwise LCDM's, the damping tail is a genuine multi-sigma tension -- a real, live
  falsification exposure, exactly as the corpus flagged. It is NOT dissolved and NOT confirmed:
  the deciding computation is the full seam-to-recombination transfer (the corpus's named open
  frontier), which alone can say whether the heights/ISW move with theta_D to keep the whole
  spectrum consistent. The approximate bound sharpens the edge from 'unquantified ~8%' to
  'irreducible multi-sigma unless the full transfer redistributes it.'""")
print("="*76)
