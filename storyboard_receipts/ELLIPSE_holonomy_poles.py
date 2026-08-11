"""Loop around the CONNECTION'S poles: r_0 = +-2/sqrt3, where 2r + r_0 = 0 (vertical tangent).
These are the black dots in fig6.  Also confirm what sits there."""
import numpy as np
c=2/np.sqrt(3)
print("   pole location: r_0 = 2/sqrt3 = %.6f ,  r = -r_0/2 = %.6f = -1/sqrt3"%(c,-c/2))
M2=lambda r0: r0-r0**3
print("   2M there = %.6f  ;  Nariai 2M = 2/(3sqrt3) = %.6f"%(M2(c), 2/(3*np.sqrt(3))))
print("   -> same |2M| as Nariai: the dots are the THIRD root of the Nariai configuration.")
print()
def roots(r0): return np.roots([1,0,-1,M2(r0)])
def track(p):
    out=[np.sort_complex(roots(p[0]))]
    for x in p[1:]:
        r=roots(x); prev=out[-1]; used=[False]*3; cur=np.zeros(3,dtype=complex)
        for i,q in enumerate(prev):
            j=min((j for j in range(3) if not used[j]), key=lambda j: abs(r[j]-q))
            cur[i]=r[j]; used[j]=True
        out.append(cur)
    return np.array(out)
def a_coef(r0,r):
    den=2*r+r0
    if abs(den)<1e-12: return 0j
    return -(r+2*r0)/den + 0.5
for rad in (0.20,0.10,0.05):
    N=6000; th=np.linspace(0,2*np.pi,N); p=c+rad*np.exp(1j*th)
    R=track(p); U=np.ones(3,dtype=complex)
    for i in range(N-1):
        dr0=p[i+1]-p[i]
        U=U*np.exp(np.array([a_coef(p[i],R[i][k]) for k in range(3)])*dr0)
    print("   radius %.2f : holonomy = %s"%(rad,'  '.join('%+.4f%+.4fi'%(x.real,x.imag) for x in U)))
    print("               |.| = %s   product = %+.4f%+.4fi"%('  '.join('%.4f'%abs(x) for x in U),
          np.prod(U).real, np.prod(U).imag))
