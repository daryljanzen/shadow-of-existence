"""WHICH COMBINATION WORKS?  Map every assignment of r_s and D_M to a rate, with and without the
onset cutoff, against the two things that must come out right:
   100 theta_* = 1.04109 +- 0.00030   (measured acoustic angle)
   and whether theta_* is H0-INDEPENDENT (which is what dissolves the Hubble tension)."""
import numpy as np
from scipy.integrate import quad
c=299792.458; z_rec=1089.9; a_rec=1/(1+z_rec); ombh2=0.02237; wr=4.1833e-5; Om=0.3150
def Hstack(H0): return lambda a: H0*np.sqrt(Om/a**3+(1-Om))
def Hleaf(H0):
    Hs=Hstack(H0); return lambda a: np.sqrt(Hs(a)**2+(100**2)*wr/a**4)
Rb=lambda a: 31500*ombh2/(2.7255/2.7)**4*a
def rs(H,zf): return quad(lambda a: c/(a**2*H(a)*np.sqrt(3*(1+Rb(a)))), 1/(1+zf), a_rec, limit=300)[0]
def DM(H):    return quad(lambda a: c/(a**2*H(a)), a_rec, 1.0, limit=400)[0]
rows=[]
for rs_rate,rs_lab in ((Hstack,'stack'),(Hleaf,'leaf')):
    for zf,zlab in ((6850.,'cut@6850'),(1e7,'no cut')):
        for dm_rate,dm_lab in ((Hstack,'stack'),(Hleaf,'leaf')):
            th=[]
            for H0 in (67.4,70.,73.):
                th.append(100*rs(rs_rate(H0),zf)/DM(dm_rate(H0)))
            spread=100*(max(th)/min(th)-1)
            rows.append((rs_lab,zlab,dm_lab,th,spread))
print("   r_s rate  cutoff      D_M rate |  100 theta_* at H0 = 67.4 / 70 / 73   | H0-spread | vs 1.04109")
for a,b,d,th,sp in rows:
    best=min(th,key=lambda x:abs(x-1.04109))
    print("   %-8s  %-10s  %-7s | %7.5f %7.5f %7.5f | %7.2f%% | best %+.2f%%"%(
        a,b,d,th[0],th[1],th[2],sp,100*(best/1.04109-1)))
print()
print("   H0-spread ~0 means theta_* is H0-INDEPENDENT (the Hubble-tension dissolution).")
