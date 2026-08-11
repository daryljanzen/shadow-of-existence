"""LIFT — a positive account of the lift, from the bead's own analytic continuation (r2157).

P7's frontier: "the lift is at present characterised only NEGATIVELY, by the coordinate's failure to
advance, and a negative characterisation is not a physical account."  It asks three things: what the
lift is, what the interior unit-speed crossing marks, and what the framework carries across.

*** 1. WHAT THE LIFT IS. ***  thm:bead is ONE function r(tau)=(2M alpha^2)^{1/3} sinh^{2/3}(3 tau/2 alpha).
On the lift Re tau = 0, so tau = i s and sinh(3 i s/2 alpha) = i sin(3 s/2 alpha); on the branch joining
the collapse leg this is real:
        r(s) = -A |sin(3 s / 2 alpha)|^{2/3},   A = (2 M alpha^2)^{1/3} = 3766.6 Mpc,
monotonic from the turnaround (-A) to the branch point (0).  Since d(tau) = i ds, the conformal time
d(eta) = d(tau)/a is PURELY IMAGINARY:  |Delta eta_lift| = (r0/A)(2 alpha/3) Int_0^{pi/2} du/|sin u|^{2/3}
                                                          = 16617 Mpc.
*** THE LIFT IS THE EUCLIDEAN SEGMENT OF THE BEAD. ***

*** 2. WHAT THE INTERIOR UNIT-SPEED CROSSING MARKS. ***  The Euclidean null (f=2, dr/dtau = +-i) sits
INSIDE a segment that is imaginary throughout -- the unit-speed condition on the imaginary branch,
in the one region where the conformal time is imaginary.  It is not an anomaly on a real interval.

*** 3. WHAT IS CARRIED ACROSS -- AND IT IS A HORIZON DISCRIMINATOR, NOT AN ATTENUATOR. ***
An oscillating mode carries exp(i k c_s eta); with eta -> eta + i|Delta| that is
        exp(i k c_s eta) x exp(-k c_s |Delta|)   -- EXPONENTIAL SUPPRESSION, not a phase shift.
But a SUPER-HORIZON mode is frozen -- a constant, not exp(i k c_s eta) -- and a constant is untouched.
So:  frozen modes pass UNCHANGED (carrying the progenitor's AMPLITUDE and TILT);
     oscillating modes are ANNIHILATED (e^-152 at P1) -- so NO PHASE carries.
*** This is the corpus's own division of labour with a mechanism underneath it: "A_s and n_s are the
progenitor's" (rem:transmission-leg) AND the phase is reset at the branch point (r2156). ***
The boundary falls at l ~ 1.5-2.5 -- the bottom of the observable range: l>=3 is oscillating and gone.

INDEPENDENT CONFIRMATION: r2156 established the reset OBSERVATIONALLY (transmission would need
D ~ 3-5e5 Mpc against 1.4e4, excluded 21-39x).  This receipt derives it GEOMETRICALLY.  Two routes.
"""
import numpy as np
from scipy.integrate import quad
alpha=5178.; M=alpha/(3*np.sqrt(3)); A=(2*M*alpha**2)**(1./3)
x0=1.6648; r0=x0*alpha/np.sqrt(3); D=13865.; cs=1/np.sqrt(3); eta_leg=9594.
print("  1. r(s) = -A|sin(3s/2alpha)|^(2/3): endpoints")
for x,lab in ((1.0,'turnaround'),(0.0,'branch point')):
    print("       s/(pi alpha/3)=%.1f -> r = %10.1f Mpc   (%s)"%(x,-A*abs(np.sin(np.pi/2*x))**(2./3),lab))
I=quad(lambda u: 1.0/abs(np.sin(u))**(2./3), 1e-12, np.pi/2)[0]
dEta=(r0/A)*(2*alpha/3)*I
print("  1. |Delta eta_lift| = %.0f Mpc, purely imaginary  (integral %.5f, converges: 2/3<1)"%(dEta,I))
assert abs(dEta-16617)<50
print("  3.    l    phase on leg   state          suppression")
for l in (1,2,3,10,220):
    k=l/D; ph=k*cs*eta_leg
    print("     %5d   %8.2f     %-12s   %.2e"%(l,ph,"FROZEN" if ph<1 else "oscillating",np.exp(-k*cs*dEta)))
print("     boundary k c_s eta_leg = 1 at l = %.2f"%(D/(cs*eta_leg)))
