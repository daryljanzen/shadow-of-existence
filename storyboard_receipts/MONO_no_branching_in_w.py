"""Monodromy done properly: the branch points are where the discriminant vanishes.
At E=0, 2M = (2/3sqrt3) a sin3w and Delta = 0 at sin3w = +-1 -> w = pi/6, pi/2, 5pi/6, ...
Integrate AROUND them in the complex w-plane, tracking roots continuously."""
import numpy as np
al=1.0
def raw(w):
    M2=(2/(3*np.sqrt(3)))*al*np.sin(3*w)
    return np.roots([1,0,-al**2, M2*al**2])
print("   branch points (Delta=0 at sin3w=+-1): w = pi/6=%.4f, pi/2=%.4f, 5pi/6=%.4f"%(np.pi/6,np.pi/2,5*np.pi/6))
print("   my dial period 2pi/3 = %.4f contains TWO of them -- which is why walking through failed."%(2*np.pi/3))
print()
def loop(centre, rad=0.25, N=3000):
    """circle the branch point in complex w; return the permutation and the residue factors"""
    ths=np.linspace(0,2*np.pi,N)
    ws=centre+rad*np.exp(1j*ths)
    r=np.sort_complex(raw(ws[0])); start=r.copy()
    fac=np.ones(3,dtype=complex)
    for k in range(1,N):
        rn=raw(ws[k]); prev=r; used=[False]*3; cur=np.zeros(3,dtype=complex)
        for i,p in enumerate(prev):
            j=min((j for j in range(3) if not used[j]), key=lambda j: abs(rn[j]-p))
            cur[i]=rn[j]; used[j]=True
        r=cur
    # which start-root did each end-slot become?
    perm=[int(np.argmin([abs(r[i]-s) for s in start])) for i in range(3)]
    return start, r, perm
for c,lab in ((np.pi/6,'w = pi/6'),(np.pi/2,'w = pi/2')):
    s,e,perm=loop(c)
    print("   circling %s:"%lab)
    print("      start roots: %s"%'  '.join('%+.4f%+.4fi'%(x.real,x.imag) for x in s))
    print("      end   roots: %s"%'  '.join('%+.4f%+.4fi'%(x.real,x.imag) for x in e))
    print("      permutation: %s   -> %s"%(perm, 'IDENTITY' if perm==[0,1,2] else ('transposition' if sorted(perm)==[0,1,2] and len([i for i in range(3) if perm[i]!=i])==2 else '3-cycle/other')))
    print()
