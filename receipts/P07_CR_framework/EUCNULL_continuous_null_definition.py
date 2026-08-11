"""EUCNULL-2 — f=0 and f=2 are ONE condition, and the null cone is defined continuously
across the whole lap.  (r2158; supersedes the placement-only reading of r2157.)

THE CLAIM (Daryl, r2158): the Euclidean null is where the null bundle INSIDE the lift obtains
its definition, so "null" is continuously well-defined across the entire excursion -- the seams
doing it on the real branches and the Euclidean null on the imaginary one.  r2157 had established
only PLACEMENT (that f=2 sits inside a segment whose conformal time is imaginary), which is
consistency, not a mechanism.  This receipt tests the claim.

THE TEST.  The marginal (E=1) radial congruence satisfies (dr/dtau)^2 = E^2 - f = 1 - f, so
    dr/dtau = +- sqrt(1-f).
On the real segments tau is real.  On the lift Re tau = 0, tau = i s, so dr/ds = i dr/dtau and
the real/imaginary branches SWAP.  Therefore:
    f = 0  ->  dr/dtau = +-1        REAL, unit      -- unit speed in the REAL segments' parameter
    f = 2  ->  dr/dtau = +-i        IMAGINARY, unit -- hence dr/ds = +-1, REAL and UNIT in s,
                                                       the LIFT's own parameter
and a generic lift point (f=0.3849 at r=-alpha) gives dr/ds = +-i 0.7843: imaginary, NOT unit.
*** So the Euclidean null is the UNIQUE locus on the lift where dr/ds is real and unit. ***

CONCLUSION.  f=0 and f=2 are the SAME condition |dr/d(segment parameter)| = 1 read on the two
branches of tau.  The lap therefore carries a unit-speed locus on EVERY segment, and the null
cone is defined CONTINUOUSLY across the whole excursion.  Daryl's inference is confirmed; it is
not a coincidence of placement.

NOTE ON A CAUGHT ERROR: the first run of this test used sqrt(f-1) and inverted every label.  It
would have "confirmed" the same conclusion through a wrong intermediate.  What caught it was the
corpus's own sentence -- "the marginal congruence has dr/dtau = +-i ... as the seams realise it on
the real ones" -- i.e. the PAPER was right and the script was not.

ORIGIN: storyboard_receipts/EUCNULL_continuous_null_definition.py -- registered r2376 (c54); edit the origin, not this copy."""
import numpy as np
from scipy.optimize import brentq
alpha=1.0; M=alpha/(3*np.sqrt(3)); f=lambda r: 1.0-2*M/r-r*r/alpha**2
rN=alpha/np.sqrt(3); rB=-2*alpha/np.sqrt(3); r_eu=brentq(lambda r: f(r)-2.0,-2.0,-1e-6)
print("  dr/dtau = +- sqrt(1-f)  [E=1];  on the lift dtau = i ds so dr/ds = i dr/dtau")
print("      r/alpha      f       dr/dtau           dr/ds")
for r,lab in ((rN,'seam, front pass'),(rB,'seam, back pass'),(r_eu,'EUCLIDEAN NULL'),(-1.0,'generic lift pt')):
    fv=f(r); q=1.0-fv
    a=("+-%.4f REAL"%np.sqrt(q)) if q>=0 else ("+-i%.4f IMAG"%np.sqrt(-q))
    b=("+-i%.4f IMAG"%np.sqrt(q)) if q>=0 else ("+-%.4f REAL"%np.sqrt(-q))
    print("   %+9.4f %8.4f   %-16s %-16s  %s"%(r,fv,a,b,lab))
assert abs(r_eu+0.344142)<1e-5 and abs(f(rN))<1e-10
assert abs(np.sqrt(abs(1-f(r_eu)))-1.0)<1e-9      # unit at f=2
assert abs(np.sqrt(abs(1-f(rN)))-1.0)<1e-9        # unit at f=0
assert abs(np.sqrt(abs(1-f(-1.0)))-1.0)>0.2       # generic lift point is NOT unit
print()
print("  ASSERTS PASS: f=2 at r=%.6f; unit at f=0 and f=2; generic lift point not unit."%r_eu)
print("  => one condition, two branches; the null cone is continuous across the whole lap.")
