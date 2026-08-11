"""r_HE is EXACTLY where the areal acceleration changes sign.
d2r/dtau^2 = -f'/2 ,  f = 1 - 2M/r - r^2/a^2 ,  f' = 2M/r^2 - 2r/a^2 = 0  <=>  r^3 = M a^2 = r_HE^3.
Decelerating inside, accelerating outside.  General in M; on the forced member r_HE = a/sqrt3 = the seam."""
import numpy as np
al=1.0
def check(M,label):
    rHE=(M*al**2)**(1/3.)
    fp=lambda r: 2*M/r**2-2*r/al**2
    acc=lambda r: -fp(r)/2
    print("   %-22s M=%.5f  r_HE=%.6f   f'(r_HE)=%+.2e" % (label,M,rHE,fp(rHE)))
    for fac,lab in ((0.5,'inside '),(1.0,'at     '),(1.7,'outside')):
        r=fac*rHE
        print("        %s r=%.4f  d2r/dtau2 = %+.6f  -> %s"%(lab,r,acc(r),
              'DECELERATING' if acc(r)<0 else ('turn' if abs(acc(r))<1e-12 else 'ACCELERATING')))
for M,lab in ((al/(3*np.sqrt(3)),'forced (Nariai)'),(0.05,'undercritical'),(0.15,'undercritical')):
    check(M,lab); print()
print("   on the forced member r_HE = a/sqrt3 = %.6f = the FRONT SEAM."%(1/np.sqrt(3)))
