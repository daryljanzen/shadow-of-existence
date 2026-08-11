"""
CROSSED-WIRE HUNT (Daryl, r966): the apparent damping-tail 'near-refutation' almost certainly
means a mistake in MY computation, not a refutation of a construction with CR's coherence and
broad correspondence. Hunt the wire in the load-bearing number: theta_D/theta_* = r_D/r_s.

The asymmetry I glossed: r_D (diffusion) is dominated at recombination (z~z*); r_s (sound horizon)
samples z* all the way back. The radiation-free rate lowers H MOST at high z (rho_r/rho_m grows
with z: ~0.3 at z*, =2 at the seam z_onset). So radiation-free enhances r_s MORE than r_D --
UNLESS r_s is cut at the seam, which removes exactly the high-z region where the enhancement is
biggest. Whether that cut is legitimate is the whole question. Compute EVERY piece transparently.
"""
import numpy as np, camb
from scipy.integrate import simpson
C=299792.458

pars=camb.CAMBparams(); pars.set_cosmology(H0=67.36,ombh2=0.02237,omch2=0.1200,mnu=0.06,tau=0.0544)
pars.InitPower.set_params(As=2.1e-9,ns=0.9649)
res=camb.get_background(pars); dp=res.get_derived_params()
zstar=dp['zstar']; h=0.6736; og=2.47282e-5/h**2
Om=(0.02237+0.1200+0.06/93.14)/h**2; Or=og+3.046*(7./8.)*(4./11.)**(4./3.)*og
OL=1-Om-Or; OLc=1-Om
zeq=Om/Or-1; z_onset=2*zeq+1     # rho_r/rho_m=2 -> (Or/Om)(1+z)=2
print(f"z*={zstar:.1f}  z_eq={zeq:.0f}  z_onset(rho_r/rho_m=2)={z_onset:.0f}  CAMB r*={dp['rstar']:.2f}")

def H(z,radfree): return 67.36*np.sqrt(Om*(1+z)**3 + (OLc if radfree else Or*(1+z)**4+OL))
def R(z): return 0.75*(0.02237/2.47282e-5)/(1+z)
def cs(z): return 1/np.sqrt(3*(1+R(z)))

def r_s(radfree, z_top):
    z=np.logspace(np.log10(zstar), np.log10(z_top), 40000)
    return simpson(cs(z)/(H(z,radfree)/C), z)

def r_D(radfree, z_top):
    zd=np.linspace(zstar, min(z_top,8000), 8000)
    opac=res.get_background_redshift_evolution(zd,['opacity'],format='array')[:,0]
    Rd=R(zd); br=Rd**2/(1+Rd)+8./9.
    return np.sqrt(simpson((1/(H(zd,radfree)/C))*(1/(6*(1+Rd)*opac))*br, zd))

print("\n"+"="*74)
print("r_s and r_D on each rate, at several upper limits (Mpc):")
print("="*74)
print(f"{'':22s}{'r_s':>10s}{'r_D':>10s}{'r_D/r_s':>12s}")
rows=[]
for label, radfree, ztop in [
    ("LCDM radfull -> inf", False, 1e6),
    ("LCDM radfull -> seam", False, z_onset),
    ("CR radfree -> seam", True, z_onset),
    ("CR radfree -> inf*", True, 1e6),   # * unphysical (no radiation cap) -- shown to expose the tail
]:
    rs=r_s(radfree,ztop); rd=r_D(radfree,ztop); rows.append((label,rs,rd,rd/rs))
    print(f"{label:22s}{rs:10.2f}{rd:10.3f}{rd/rs:12.5f}")

print("\n"+"="*74)
print("WHERE THE +8% COMES FROM -- read the ratios:")
print("="*74)
lcdm=rows[0]; lcdm_seam=rows[1]; cr_seam=rows[2]
print(f" theta_D/theta_* :  LCDM(radfull,inf) = {lcdm[3]:.5f}")
print(f"                    CR  (radfree,seam) = {cr_seam[3]:.5f}   "
      f"({100*(cr_seam[3]-lcdm[3])/lcdm[3]:+.1f}% vs LCDM-inf)  <- the corpus's +8%")
print(f"   BUT the FAIR (same-limit) comparison, both cut at the seam:")
print(f"                    LCDM(radfull,seam) = {lcdm_seam[3]:.5f}")
print(f"                    CR  (radfree,seam) = {cr_seam[3]:.5f}   "
      f"({100*(cr_seam[3]-lcdm_seam[3])/lcdm_seam[3]:+.1f}% vs LCDM-seam)")
print(f"\n r_s enhancement CR/LCDM at the seam limit: "
      f"{cr_seam[1]/lcdm_seam[1]:.3f}   r_D enhancement: {cr_seam[2]/lcdm_seam[2]:.3f}")
print("""
READING: if r_s and r_D are computed on the SAME footing (same rate difference, same limits),
the radiation-free rate enhances BOTH -- and the question is whether it enhances r_s and r_D by
DIFFERENT factors (a real theta_D/theta_* shift) or nearly the SAME factor (no shift, the +8%
being an artifact of comparing CR's seam-cut r_s against LCDM's to-infinity r_s). The numbers
above decide it. If r_D/r_s(CR,seam) ~ r_D/r_s(LCDM,seam), the tail 'tension' is a crossed wire:
LCDM's own r_s barely changes between seam and infinity (radiation era contributes little), so the
honest CR-vs-LCDM comparison is the seam-vs-seam one, and the +8% lives or dies there.
""")
