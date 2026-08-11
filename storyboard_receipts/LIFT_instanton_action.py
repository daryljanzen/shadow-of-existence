"""FAMILY 10, final item: does the lift have a variational principle of its own?
Claim: S_E = int ds [ (1/2) r'^2 + V(r) ],  V = f/2,  with Euclidean first integral (1/2)r'^2 - V = -1/2.
Test the closed form r(s) = -(2 M a^2)^{1/3} |sin(3s/2a)|^{2/3} against BOTH."""
import numpy as np
a=1.0; M=a/(3*np.sqrt(3))
A=(2*M*a**2)**(1./3)
f=lambda r: 1-2*M/r-r*r/a**2
V=lambda r: 0.5*f(r)
dV=lambda r,h=1e-7: (V(r+h)-V(r-h))/(2*h)
r_of=lambda s: -A*np.abs(np.sin(1.5*s/a))**(2./3)
print("   lift: s in (0, pi a/3];  r(0)= -A = %.6f (turnaround) -> r(pi a/3)=0 (branch point)"%(-A))
print()
print("       s        r        (1/2)r'^2 - V   [want -0.5]      r''        dV/dr    [want equal]")
for s in (0.20,0.40,0.70,1.00):
    h=1e-5
    r=r_of(s); rp=(r_of(s+h)-r_of(s-h))/(2*h); rpp=(r_of(s+h)-2*r+r_of(s-h))/h**2
    print("     %.2f  %+8.5f   %+12.8f            %+10.5f %+10.5f"%(s,r,0.5*rp*rp-V(r),rpp,dV(r)))
print()
print("   (Euclidean EOM from S_E is r'' = +dV/dr : motion in the INVERTED potential.)")

# --- r2376+c54.158 -------------------------------------------------------------------
# PINS THIS RECEIPT'S OWN CLAIM.  The closed form r(s)=-(2Ma^2)^{1/3}|sin(3s/2a)|^{2/3}
# satisfies BOTH tests the docstring names, at the last tabulated point s=1.00:
#   (a) the Euclidean first integral (1/2)r'^2 - V = -1/2 (printed -0.50000000);
#   (b) the Euclidean EOM r'' = +dV/dr, motion in the INVERTED potential (both +1.09112);
# and the turnaround amplitude is A = (2Ma^2)^{1/3} = 0.727416.
assert abs((0.5*rp*rp - V(r)) - (-0.5)) < 1e-9, "first integral = %.10f, not -1/2" % (0.5*rp*rp - V(r))
assert abs(rpp - dV(r)) < 1e-5, "r'' = %.8f but dV/dr = %.8f (inverted-potential EOM fails)" % (rpp, dV(r))
assert abs(A - 0.727416) < 1e-6, "amplitude A = %.6f, not 0.727416" % A
