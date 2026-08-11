"""LAP — the whole seam-to-seam excursion read off the single function f  (r2159).

P7's frontier asked for "a positive account of the lap".  It is here, and it is one function.
f(r) = 1 - 2M/r - r^2/alpha^2 on the Nariai member; the marginal (E=1) congruence has
(dr/dtau)^2 = 1 - f.  Every structural feature of the excursion is a value of f:

   f < 0        r TIMELIKE      beyond the back pass, and the whole r>0 cosmology
   f = 0        r NULL          *** THE SEAM ***  -- character flip THROUGH ZERO; |dr/dtau|=1 REAL
   0 < f < 1    r spacelike     the lap's real segment; |dr/dtau| < 1, decelerating
   f = 1                        *** THE TURNAROUND *** -- dr/dtau = 0, the BRANCH POINT of sqrt(1-f):
                                this is WHY the lift is Euclidean, not merely where it starts
   f > 1                        *** THE LIFT *** -- dr/dtau IMAGINARY; conformal time imaginary
   f = 2                        *** THE EUCLIDEAN NULL *** -- |dr/dtau| = 1 again, IMAGINARY:
                                the lift's own null definition (r2158)
   f -> +-inf   r flips again   *** THE BRANCH POINT r=0 *** -- character flip THROUGH INFINITY,
                                via -2M/r; hence r_* FINITE and no divergent phase carried (r2154)

TWO STRUCTURAL DUALITIES, both established here:
 (1) the unit-speed loci sit at 1-f = +1 (seam, real) and 1-f = -1 (Euclidean null, imaginary),
     ONE UNIT EITHER SIDE of the turnaround at 1-f = 0.  One condition, two branches (r2158).
 (2) the two causal-character flips are THROUGH ZERO (the seam, f=0) and THROUGH INFINITY
     (the branch point, f -> +-inf).  The second is exactly why transmission is scale-free (r2154).

NOTE: f > 0 covers only the r<0 stretch.  The r>0 side already has r timelike -- the cosmology is
running the moment the excursion is past the branch point.
"""
import numpy as np
alpha=1.0; M=alpha/(3*np.sqrt(3)); f=lambda r: 1.0-2*M/r-r*r/alpha**2
A=(2*M*alpha**2)**(1./3); rN=alpha/np.sqrt(3); rB=-2*alpha/np.sqrt(3)
print("       r/alpha       f      1-f      dr/dtau        r is        locus")
for r,lab in ((-1.5,''),(rB,'SEAM (back pass)'),(-1.0,''),(-A,'TURNAROUND'),(-0.6,''),
              (-0.344142,'EUCLIDEAN NULL'),(-0.02,''),(0.02,'past the BRANCH POINT'),
              (0.30,''),(rN,'SEAM (front pass)'),(1.2,'')):
    fv=f(r); q=1.0-fv
    d=("+-%.3f R"%np.sqrt(q)) if q>1e-12 else ("0" if abs(q)<1e-12 else "+-i%.3f I"%np.sqrt(-q))
    ch="TIMELIKE" if fv<-1e-12 else ("NULL" if abs(fv)<1e-12 else "spacelike")
    print("     %+8.4f %8.3f %+7.3f   %-11s %-10s %s"%(r,fv,q,d,ch,lab))
# asserts
assert abs(f(rB))<1e-12 and abs(f(rN))<1e-10          # seams at f=0
assert abs(f(-A)-1.0)<1e-12                            # turnaround at f=1
assert abs(f(-0.344142)-2.0)<1e-4                      # Euclidean null at f=2
assert f(0.30)<0 and f(-1.0)>0                         # r>0 timelike; r<0 lap spacelike
print()
print("  ASSERTS PASS: seams f=0; turnaround f=1; Euclidean null f=2; r>0 timelike, lap r<0 spacelike.")
print("  => 1-f = +1, 0, -1 gives seam / turnaround / Euclidean null.  ONE function, the whole run.")
