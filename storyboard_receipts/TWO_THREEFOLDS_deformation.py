"""The two three-folds are two ENERGIES of one congruence, r^3+(E^2-1)a^2 r+2Ma^2=0,
with -k = E^2-1 the Friedmann curvature constant.  Where does the discriminant crossing sit,
and which end does the OBSERVED cosmology occupy?"""
import numpy as np
al=1.0
def cross(M): 
    x=3*(M/al)**(2/3.)      # 1-E^2 = 3(M/a)^{2/3}
    return x, (np.sqrt(1-x) if x<=1 else None)
print("   family: r^3 + (E^2-1) a^2 r + 2M a^2 = 0 ;  -k = E^2-1")
print("   E=1 (k=0, FLAT -- the observed cosmology) -> r^3 + 2M a^2 = 0 : EQUILATERAL")
print("   E=0 (k=+1, maximally bound)               -> r^3 - a^2 r + 2M a^2 = 0 : colinear real")
print()
print("   discriminant crossing at 1-E^2 = 3(M/alpha)^{2/3}:")
MN=al/(3*np.sqrt(3))
for M,lab in ((0.02,'light'),(0.10,'mid'),(MN,'NARIAI'),):
    x,E=cross(M)
    print("      M=%.5f (%-6s): 1-E^2 = %.4f -> E_cross = %s"%(M,lab,x, '%.4f'%E if E is not None else 'none'))
print()
print("   at the Nariai mass 1-E^2 = %.4f, so E_cross = %.4f -- the crossing arrives AT E=0."%(cross(MN)[0], cross(MN)[1]))
print()
print("   turnaround triple modulus (2 M a^2)^{1/3} at Nariai = %.6f = A, the bead amplitude"%((2*MN)**(1/3.)))
print("   and the horizon triple's radius scale a/sqrt3 = %.6f = r_HE = the front seam"%(1/np.sqrt(3)))
