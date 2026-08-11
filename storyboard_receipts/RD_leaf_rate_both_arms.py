"""r_D on the LEAF rate for BOTH arms, matched parameters -- the assignment P7's rule requires.
P7: "a quantity computed from a process running in the content -- the plasma's sound horizon, ITS
DIFFUSION LENGTH, recombination, the perturbations -- takes the LEAF's."
The leaf rate is content-carrying: H^2 = H0^2(Or a^-4 + Om a^-3 + OL).
The two arms differ in Om (via x0) and in the LOWER LIMIT (CR's plasma starts at z_onset)."""
import numpy as np
from scipy.integrate import quad
c=299792.458; z_rec=1089.9; a_rec=1/(1+z_rec)
def rD2(H0, Om, ombh2, z_from, z_to=z_rec):
    h=H0/100; Or=4.1833e-5/h**2; OL=1-Om
    Hub=lambda a: H0*np.sqrt(Or/a**4+Om/a**3+OL)     # LEAF rate, content-carrying
    Rb=lambda a: 31500*ombh2/(2.7255/2.7)**4*a
    # tau' = n_e sigma_T a ; use the standard scaling with a fully-ionised approximation to
    # recombination, identical in both arms so it cancels in the ratio
    taup=lambda a: 2.3e-5*ombh2/h * a**-2
    integ=lambda a: (c/(a**2*Hub(a))) / (6*(1+Rb(a))*taup(a)) * (Rb(a)**2/(1+Rb(a)) + 16./15.)
    return quad(integ, 1/(1+z_from), a_rec, limit=300)[0]
print("   r_D on the LEAF rate, both arms, the SAME recombination treatment:")
print()
# LambdaCDM: integral from z -> large (no onset)
rl=np.sqrt(rD2(67.40, 0.3150, 0.02237, 1e7))
print("      LambdaCDM  (from z->1e7)      r_D = %.4f Mpc"%rl)
# CR: same leaf rate, but the plasma exists only after z_onset
for zo in (6850., 6761.):
    rc=np.sqrt(rD2(67.40, 0.3150, 0.02237, zo))
    print("      CR (leaf rate, z_onset=%.0f)  r_D = %.4f Mpc   ratio = %.4f  (%+.2f%%)"%(zo,rc,rc/rl,100*(rc/rl-1)))
print()
print("   for contrast, the RADIATION-FREE rate for CR -- the assignment P7's rule forbids")
print("   for this quantity -- is what gives the 9% in damping_ratio_clean.")
