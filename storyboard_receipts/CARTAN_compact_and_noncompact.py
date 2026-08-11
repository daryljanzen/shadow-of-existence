"""The OTHER pole at r_0 = -2/sqrt3, and what the two together generate.
If they act on different pairs, their product is not diagonal -> off-diagonal generators reached."""
import numpy as np
M2=lambda r0: r0-r0**3
def roots(r0): return np.roots([1,0,-1,M2(r0)])
def track(p):
    out=[np.sort_complex(roots(p[0]))]
    for x in p[1:]:
        r=roots(x); prev=out[-1]; used=[False]*3; cur=np.zeros(3,dtype=complex)
        for i,q in enumerate(prev):
            j=min((j for j in range(3) if not used[j]), key=lambda j: abs(r[j]-q))
            cur[i]=r[j]; used[j]=True
        out.append(cur)
    return np.array(out), out[0]
def a_coef(r0,r):
    den=2*r+r0
    return 0j if abs(den)<1e-12 else -(r+2*r0)/den + 0.5
def holo(c,rad,N=5000):
    th=np.linspace(0,2*np.pi,N); p=c+rad*np.exp(1j*th)
    R,start=track(p); U=np.ones(3,dtype=complex)
    for i in range(N-1):
        U=U*np.exp(np.array([a_coef(p[i],R[i][k]) for k in range(3)])*(p[i+1]-p[i]))
    # which root index ends where -> the permutation part
    end=R[-1]
    perm=[int(np.argmin([abs(end[i]-s) for s in start])) for i in range(3)]
    return U, perm, start
for c,lab in ((2/np.sqrt(3),'r_0 = +2/sqrt3'),(-2/np.sqrt(3),'r_0 = -2/sqrt3')):
    U,perm,start=holo(c,0.10)
    print("   %s :"%lab)
    print("      start roots  %s"%'  '.join('%+.4f'%x.real for x in start))
    print("      phases (deg) %s"%'  '.join('%+8.2f'%np.degrees(np.angle(x)) for x in U))
    print("      moduli       %s   permutation %s"%('  '.join('%.4f'%abs(x) for x in U), perm))
    print("      -> the UNIT-phase component is index %d (the root NOT in the colliding pair)"%
          int(np.argmin([abs(np.angle(x)) for x in U])))
    print()
print("   if the two poles leave DIFFERENT components fixed, the pairs differ, and the")
print("   two U(1)s lie in different Cartan directions -> together they generate more than one U(1).")
