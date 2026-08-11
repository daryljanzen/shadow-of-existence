"""THE CALIBRATION.  On-shell S = int p_a da with p_a = (3/4pi) a adot  (from P10's H).
Continuing tau = i s : S = -i S_E with  S_E^grav = (3/4pi) int r r'^2 ds  along the SAME trajectory.
Compare with the contour action S_E^c = int [ (1/2) r'^2 + f/2 ] ds = 1.489 (alpha=1)."""
import numpy as np
from scipy.integrate import quad
a=1.0; M=a/(3*np.sqrt(3)); A=(2*M*a**2)**(1./3); smax=np.pi*a/3.0
f=lambda r: 1-2*M/r-r*r/a**2
r_of=lambda s: -A*np.abs(np.sin(1.5*s/a))**(2./3)
rp_of=lambda s,h=1e-7: (r_of(s+h)-r_of(s-h))/(2*h)
# on the lift r'^2 = f-1 exactly; use it (avoids numerical derivative near the endpoint)
integ=lambda s: (3.0/(4*np.pi))*r_of(s)*(f(r_of(s))-1.0)
print("   check r'^2 = f-1 on the lift:")
for s in (0.3,0.6,0.9):
    print("      s=%.1f :  r'^2=%.6f   f-1=%.6f"%(s,rp_of(s)**2,f(r_of(s))-1))
print()
print("   S_E^grav = (3/4pi) int r (f-1) ds   [r<0 on the lift, f-1>0]")
for lo in (1e-4,1e-6,1e-8):
    I,_=quad(integ,lo,smax,limit=400)
    print("      from s=%.0e : %12.6f"%(lo,I))
I,_=quad(integ,0,smax,limit=800,points=[0])
print("      full segment  : %12.6f   (units alpha=1, G=1)"%I)
print()
print("   ratio to the contour action 1.4890 : %.6f"%(I/1.4890))
print("   and (3/4pi) = %.6f"%(3/(4*np.pi)))

# --- r2376+c54.158 -------------------------------------------------------------------
# PINS THIS RECEIPT'S OWN CLAIM.  (a) r'^2 = f-1 holds on the lift: the central-difference
# derivative of the closed form and the independently evaluated f(r)-1 both give 0.025799
# at s=0.9.  (b) the on-shell gravitational Euclidean action over the full segment is
# S_E^grav = -0.048113 (alpha=1, G=1), which is -0.032312 of the contour action 1.4890.
assert abs(rp_of(0.9)**2 - 0.025799) < 1e-6, "r'^2 at s=0.9 = %.6f, not 0.025799" % rp_of(0.9)**2
assert abs((f(r_of(0.9)) - 1) - 0.025799) < 1e-6, "f-1 at s=0.9 = %.6f, not 0.025799" % (f(r_of(0.9))-1)
assert abs(I - (-0.048113)) < 1e-6, "S_E^grav (full segment) = %.6f, not -0.048113" % I
assert abs(I/1.4890 - (-0.032312)) < 1e-6, "S_E^grav / 1.4890 = %.6f, not -0.032312" % (I/1.4890)
