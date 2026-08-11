"""C9 — r_s AND r_D WITH THE CORRECT LOWER LIMIT: THE SEAM.
A first pass integrated from a=0 and returned r_s = 256 Mpc against the corpus's 144 -- absurd, and
the error is structural, not numerical: *** ON THIS COSMOLOGY THERE IS NO OBSERVABLE EXPANSION
BEFORE THE SEAM. *** P15: 'recombination is observable cosmology FROM THE SEAM OUTWARD'.  The L1
foliation BEGINS at the seam; integrating below it is integrating over a leg that is L2."""
import numpy as np
from scipy.integrate import quad
print("="*80); print("C9 — THE SOUND HORIZON AND THE OBSERVABLE, FROM THE SEAM"); print("="*80)
Om, OL, H0, c = 0.307, 0.693, 67.4, 299792.458
z_rec, z_onset = 1100.0, 6797.0
a_rec, a_onset = 1/(1+z_rec), 1/(1+z_onset)
ratio_rec = 2.0*(1+z_rec)/(1+z_onset)
Or = Om*ratio_rec*a_rec
Rb_rec = 0.6
def Rb_of(a): return Rb_rec*(a/a_rec)
def H_CR(a): return H0*np.sqrt(Om/a**3 + OL)
def H_LC(a): return H0*np.sqrt(Or/a**4 + Om/a**3 + OL)
print(f"  a_onset = 1/(1+{z_onset:.0f}) = {a_onset:.3e} ;  a_rec = {a_rec:.5f}")
print("  *** CR's integrals run from a_onset.  LambdaCDM's run from 0 -- it HAS a radiation era. ***")
print("  That asymmetry is not a choice: it is the two cosmologies' actual beginnings.\n")
def rs(H, lo):
    f=lambda a: c/(a**2*H(a)*np.sqrt(3*(1+Rb_of(a))))
    v,_=quad(f, lo, a_rec, limit=400); return v
def rD(H, lo):
    def g(a):
        Rb=Rb_of(a); return (Rb**2/(1+Rb)+8/9)/(6*(1+Rb))
    f=lambda a: g(a)/H(a)
    v,_=quad(f, lo, a_rec, limit=400); return np.sqrt(v)
rs_CR, rs_LC = rs(H_CR, a_onset), rs(H_LC, 1e-9)
rD_CR, rD_LC = rD(H_CR, a_onset), rD(H_LC, 1e-9)
print(f"   r_s(CR, from the seam)     = {rs_CR:8.2f} Mpc")
print(f"   r_s(LCDM, from 0)          = {rs_LC:8.2f} Mpc")
print(f"   *** P15 quotes r_s = 144.0 against CAMB 144.4.  Mine: CR {rs_CR:.1f}, LCDM {rs_LC:.1f}. ***")
print(f"\n   r_s(CR)/r_s(LCDM) = {rs_CR/rs_LC:.4f}  ->  {100*(rs_CR/rs_LC-1):+.2f}%")
print(f"   r_D(CR)/r_D(LCDM) = {rD_CR/rD_LC:.4f}  ->  {100*(rD_CR/rD_LC-1):+.2f}%")
th=(rD_CR/rs_CR)/(rD_LC/rs_LC)
print(f"\n   *** theta_D/theta_* ratio = {th:.4f}  ->  {100*(th-1):+.2f}% ***")
print("""
  READ IT.  With the lower limit at the seam, r_s comes out CLOSE to the observed acoustic scale --
  which is what the corpus says the inherited datum buys -- and the damping ratio survives as a
  SMALL residual rather than the 76% monster the wrong limit produced.
  *** AND NOTE WHAT FIXED IT: not a parameter, but the corpus's own statement of where its
      observable cosmology BEGINS.  The seam is a limit of integration. ***
""")
# --- r2376+c54.160: PIN THE CLAIM.  This receipt's whole point is that taking the lower limit at
# the seam returns a sound horizon close to the acoustic scale and a SMALL damping residual.  The
# paper (sec:envelope-consequence) quotes these same figures: "r_s = 146.4 Mpc against 145.4 on the
# radiation-included rate -- within 0.7% of each other", and "theta_D/theta_* larger by 9.4%".  Both
# are pinned here, so a retune of z_onset or of the integrals breaks the gate rather than the paper.
assert z_onset == 6797.0, f"seam redshift moved: {z_onset}"          # the paper's onset redshift
assert abs(rs_CR - 146.36) < 0.05, f"r_s(CR) = {rs_CR}"              # paper: 146.4 Mpc
assert abs(rs_LC - 145.38) < 0.05, f"r_s(LCDM) = {rs_LC}"            # paper: 145.4 Mpc
assert abs(100*(rs_CR/rs_LC - 1) - 0.67) < 0.05, f"r_s spread = {100*(rs_CR/rs_LC-1)}%"   # paper: 0.7%
assert abs(rD_CR/rD_LC - 1.1015) < 0.002, f"r_D ratio = {rD_CR/rD_LC}"                    # +10.15%
assert abs(th - 1.0941) < 0.002, f"theta_D/theta_* ratio = {th}"     # paper: larger by 9.4%
print("  SENSITIVITY, since a_onset is doing real work now:")
for zs in [5000.,6000.,6797.,8000.,10000.]:
    a_s=1/(1+zs); v=rs(H_CR, a_s)
    print(f"     z_onset={zs:>7.0f}:  r_s(CR) = {v:7.2f} Mpc   ({100*(v/rs_LC-1):+6.2f}% vs LCDM)")
print("="*80)
