"""The FULL R-conjugation is r -> -r WITH 2M -> -2M (P14: the offset-mass relation is odd).
Integrand: r(f(r)-1) = -2M - r^3/alpha^2.
Under (r,M) -> (-r,-M):  (-r)(f_{-M}(-r)-1) = +2M + r^3/alpha^2 = -[r(f-1)]   -> ODD.
So the two branches carry equal and opposite Euclidean action: no asymmetry made at the crossing.
ORIGIN: storyboard_receipts/CROSSING_no_made_asymmetry.py -- registered r2376 (c54); edit the origin, not this copy."""
import numpy as np
from scipy.integrate import quad
al=1.0; M0=al/(3*np.sqrt(3)); A=(2*M0*al**2)**(1./3); smax=np.pi*al/3.0
def SE(sgn):
    M=sgn*M0
    rf=lambda s: sgn*A*np.abs(np.sin(1.5*s/al))**(2./3)
    g=lambda s: (3.0/(4*np.pi))*( -2*M - rf(s)**3/al**2 )
    I,_=quad(g,0,smax,limit=800,points=[0]); return I
Sa=SE(-1); Sm=SE(+1)
print("   ANTIMATTER branch  (r<0, M>0 ... i.e. sgn=-1 with 2M->-2M applied)  S_E = %+.6f a^2/G"%Sa)
print("   MATTER branch      (full R-image: r->-r AND 2M->-2M)               S_E = %+.6f a^2/G"%Sm)
print("   sum = %+.3e   ->  %s"%(Sa+Sm,"EQUAL AND OPPOSITE" if abs(Sa+Sm)<1e-9 else "not"))
print()
print("   pointwise parity of the integrand under the FULL R:")
for r in (0.20,0.45,0.70):
    a=-2*M0-r**3/al**2; b=-2*(-M0)-(-r)**3/al**2
    print("      r=%.2f :  -2M-r^3 = %+9.5f   |   R-image = %+9.5f   sum %+9.2e"%(r,a,b,a+b))


# ** CHECK, added r2376+c54.156: pin the paper's printed 0.1443 alpha^2/G.  The sum-to-zero is
#    algebraically incapable of failing in this file (SE(sgn) reduces to -sgn*C), so the MAGNITUDE
#    is the only falsifiable half and it is the half the paper quotes. **
print()
print(f"  ** CHECK: |S_E| = {abs(Sa):.6f} a^2/G against the paper's printed 0.1443 **")
assert abs(abs(Sa) - 0.1443) < 5e-5, f"the paper prints 0.1443; this run gives {abs(Sa):.6f}"
assert abs(Sa + Sm) < 1e-12, "the two branches must sum to zero"
print("  CHECK PASSES")
