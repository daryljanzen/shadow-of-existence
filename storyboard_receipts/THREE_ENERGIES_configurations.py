"""Three energies, three root configurations of r^3+(E^2-1)a^2 r+2M a^2=0.
E<1 closed (k=+1) | E=1 flat (k=0) | E>1 open (k=-1)."""
import numpy as np
al=1.0; M=al/(3*np.sqrt(3))
def roots(E):
    return np.roots([1,0,(E**2-1)*al**2, 2*M*al**2])
for E,lab,k in ((0.0,'closed, maximally bound','+1'),(0.6,'closed','+1'),(1.0,'FLAT (observed)','0'),(1.4,'open','-1')):
    r=roots(E); r=r[np.argsort(r.real)]
    nreal=sum(abs(x.imag)<1e-12 for x in r)
    mods=sorted(abs(x) for x in r)
    print("   E=%.1f  k=%-3s %-24s real roots: %d   |moduli| %s"%(E,k,lab,nreal,
          ' '.join('%.4f'%m for m in mods)))
print()
print("   at E=1 the linear coefficient E^2-1 vanishes EXACTLY -> pure cube r^3 = -2M a^2")
r=roots(1.0)
print("      roots:", ' '.join('%.4f%+.4fi'%(x.real,x.imag) for x in r))
print("      all of modulus (2M a^2)^{1/3} = %.6f, at 120 deg apart -> EXACT Z_3"%((2*M)**(1/3.)))
print()
print("   => the equilateral configuration exists exactly when k=0, and k=0 is what is observed.")
