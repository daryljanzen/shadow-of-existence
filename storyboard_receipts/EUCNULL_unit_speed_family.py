"""EUCNULL — THE UNIT-SPEED FAMILY OF THE BEAD, and the EUCLIDEAN NULL on the lift.

The E=1 marginal congruence obeys (dr/d tau)^2 = 1 - f, so every locus at which the comoving radial
speed has UNIT MAGNITUDE is a root of
        (1 - f)^2 = 1        <=>        f (f - 2) = 0 ,
and with 1 - f = 2M/r + r^2/alpha^2 this is ONE cubic family in c = 1 - f = (dr/d tau)^2:

        r^3 - c r + 2M = 0

    c = +1   f = 0   dr/dtau = +-1   THE SEAMS            -- three real roots (the Weyl triple)
    c =  0   f = 1   dr/dtau =  0    THE TURNAROUND       -- one real root, -(2M)^(1/3)
    c = -1   f = 2   dr/dtau = +-i   THE EUCLIDEAN NULL   -- one real root (discriminant < 0)

*** THE EUCLIDEAN NULL (named r2124). ***  The lift runs from the turnaround (dr/dtau = 0) to the branch
point (dr/dtau -> infinity) with Re tau~ frozen, so the whole excursion is in imaginary cosmic time.  The
EUCLIDEAN NULL is the single point along it at which |dr/dtau| = 1 -- where the Euclidean excursion crosses
light speed.  It is the same condition the seams realise on the real legs, realised on the conjugate branch:
the seams are the LORENTZIAN nulls, this is the EUCLIDEAN one.

*** IT IS NOT A SEAM. ***  A seam is a turning point of the slicing curve, dr/dl = sqrt|f| = 0.  Here f = 2,
so dr/dl = sqrt2 and the curve does not turn.  The name is deliberately free of 'seam'.

TWO Lorentzian nulls and exactly ONE Euclidean null, and the count is forced: r^3 - r + 2M has three real
roots, r^3 + r + 2M has discriminant -4 - 27(2M)^2 < 0 for every 2M, hence exactly one.
"""
import numpy as np
al=1.0; twoM=2/(3*np.sqrt(3)); A=twoM**(1/3)
f=lambda r: 1 - twoM/r - r**2/al**2
def roots_of(c):
    rr=np.roots([-1.0,0.0,c,-twoM])          # -r^3 + c r - 2M = 0  <=>  r^3 - c r + 2M = 0
    # a DOUBLE root returns as a near-degenerate complex pair; keep anything whose imaginary
    # part is negligible against its own modulus (the Nariai triple is 1/sqrt3 twice, -2/sqrt3).
    return sorted(x.real for x in rr if abs(x.imag) < 1e-6*max(abs(x),1.0))

print("="*78); print("THE UNIT-SPEED FAMILY:  r^3 - c r + 2M = 0,  c = 1-f = (dr/dtau)^2"); print("="*78)
for c,lab in ((1.0,"c=+1  SEAMS (Lorentzian null)"),(0.0,"c= 0  TURNAROUND"),(-1.0,"c=-1  EUCLIDEAN NULL")):
    rr=roots_of(c)
    print("  %-30s real roots: %s"%(lab, ", ".join("%+.6f"%x for x in rr)))
    for r in rr: assert abs((1-f(r))-c)<1e-9, (lab,r)

rE=roots_of(-1.0)[0]
print()
print("  EUCLIDEAN NULL      r = %+.6f alpha"%rE)
print("     f(r)               = %.6f   (exactly 2)"%f(rE))
print("     (dr/dtau)^2 = 1-f  = %+.6f  -> dr/dtau = +-i"%(1-f(rE)))
disc=-4.0-27.0*twoM**2
print("     cubic r^3 + r + 2M discriminant = %.4f < 0  ->  exactly ONE real root"%disc)
assert abs(f(rE)-2.0)<1e-12
assert abs(rE+0.344142)<1e-5
assert disc<0

# where it sits on the bead: path length s and the panel-(B) lap angle
P=np.pi/3; Acoef=2**(1/3)/np.sqrt(3)
from scipy.optimize import brentq
s_of=lambda s: -Acoef*np.sin(1.5*(P-s))**(2/3)
sE=brentq(lambda s: s_of(s)-rE, 1e-9, P-1e-9)
k=360.0/(1/np.sqrt(3)+2/np.sqrt(3))          # deg per unit r on the lap (panel B linear map)
print()
print("  on the bead:  s/P = %.5f   (the lift spans s in [0, pi/3])"%(sE/P))
print("  lap angle:    %.2f deg past r=0, i.e. panel-(B) %.2f deg, %.2f deg from the seam"
      %(abs(rE)*k, 390+abs(rE)*k, 630-(390+abs(rE)*k)))
print()
print("  ALL CHECKS PASS.")
