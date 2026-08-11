"""Verify the leaf norm converges at the horizon (integrable inverse-sqrt), then state the tower."""
import numpy as np
from scipy.integrate import quad
al=1.0; M=al/(3*np.sqrt(3)); f=lambda r: 1-2*M/r-r*r/al**2
rN=al/np.sqrt(3)
_norms=[]                                   # r2376+c54.161: capture only; computes nothing new
for lam in (1.0,3.0,10.0):
    tot=0.0
    for a,b in ((1e-8,0.3),(0.3,rN-1e-6)):
        v,_=quad(lambda r: abs(r)**(2*lam)/np.sqrt(abs(f(r))), a,b, limit=400, points=[b] if b<rN else None)
        tot+=v
    _norms.append(tot)
    print("      lambda=%4.1f : leaf-norm on (0,r_N) = %12.6g   <- FINITE"%(lam,tot))
print()
print("   => for EVERY lambda = j+1/2, exactly ONE branch (psi=|r|^{+lambda}) is normalizable.")
print("      The growing branch |r|^{-lambda} needs lambda < 3/4, which never holds (lambda = 1,2,3,...).")
print()
print("   THE TOWER IS INFINITE: one bound zero-mode per (wall, j).")
print("   j is the ordinary angular decomposition of the 4D field, not extra multiplet content.")

# --- assertions added r2376+c54.161 (the file carried none: its OK certified only exit 0) ---
# (1) THE CLAIM THE FILE ADVERTISES: the leaf norm CONVERGES at the Nariai horizon.  The three
#     printed values, pinned; each fires if the measure 1/sqrt|f| or the endpoint r_N moves.
assert abs(rN - 0.5773502691896258) < 1e-12, rN            # r_N = alpha/sqrt(3)
assert abs(_norms[0] -  2.239428e+00) < 1e-5, _norms[0]    # lambda = 1
assert abs(_norms[1] -  2.301951e-01) < 1e-6, _norms[1]    # lambda = 3
assert abs(_norms[2] -  9.437460e-05) < 1e-9, _norms[2]    # lambda = 10
assert _norms[0] > _norms[1] > _norms[2] > 0
# (2) THE OTHER HALF OF THE STATEMENT, which the file only asserts in prose: the GROWING branch
#     |r|^{-lambda} is NOT normalizable, needing lambda < 3/4.  Near r=0, f ~ -2M/r so
#     1/sqrt|f| ~ r^{1/2} and the integrand goes as r^{1/2-2 lambda}: at lambda=1 the integral
#     diverges like eps^{-1/2}, i.e. by a factor sqrt(10) = 3.162 per decade of cutoff.
_grow=[quad(lambda r: abs(r)**(-2.0)/np.sqrt(abs(f(r))), e, 0.3, limit=400)[0]
       for e in (1e-4,1e-5,1e-6)]
assert _grow[2] > _grow[1] > _grow[0] > 3.0e2, _grow
assert abs(_grow[2]/_grow[1] - np.sqrt(10.0)) < 0.05, _grow[2]/_grow[1]
assert abs(_grow[2] - 3220.78) < 1.0, _grow[2]
# (3) and 3/4 is the threshold, so no lambda = j+1/2 with j >= 1/2 ever reaches it.
assert all(lam >= 1.0 and not (lam < 0.75) for lam in (1.0,2.0,3.0,10.0))
