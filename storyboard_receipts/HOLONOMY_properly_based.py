"""Properly based holonomies: fix ONE base point b; for each loop, transport b->near pole,
go around, transport back.  All elements then live in Hol(b) and compose legitimately."""
import numpy as np
M2=lambda r0: r0-r0**3
def roots(r0): return np.roots([1,0,-1,M2(r0)])
def a_coef(r0,r):
    den=2*r+r0
    return 0j if abs(den)<1e-12 else -(r+2*r0)/den + 0.5
def transport(path, start_roots):
    """parallel-transport along an arbitrary path; returns (diag factors, end roots, permutation vs start)"""
    r=start_roots.copy(); d=np.ones(3,dtype=complex)
    for i in range(len(path)-1):
        d=d*np.exp(np.array([a_coef(path[i],r[k]) for k in range(3)])*(path[i+1]-path[i]))
        rn=roots(path[i+1]); used=[False]*3; cur=np.zeros(3,dtype=complex)
        for a,p in enumerate(r):
            j=min((j for j in range(3) if not used[j]), key=lambda j: abs(rn[j]-p))
            cur[a]=rn[j]; used[j]=True
        r=cur
    return d, r
def Pm(perm):
    M=np.zeros((3,3),dtype=complex)
    for i,j in enumerate(perm): M[i,j]=1
    return M
b=0.0+0.35j                                  # common base point, off the real axis, away from poles
base_roots=np.sort_complex(roots(b))
def based_loop(c, rad, N=4000, Np=1500):
    out=np.linspace(b, c+rad, Np)            # b -> loop start
    th=np.linspace(0,2*np.pi,N); circ=c+rad*np.exp(1j*th)
    back=np.linspace(c+rad, b, Np)           # loop end -> b
    d1,r1=transport(out, base_roots)
    d2,r2=transport(circ, r1)
    d3,r3=transport(back, r2)
    dtot=d1*d2*d3
    perm=[int(np.argmin([abs(r3[i]-s) for s in base_roots])) for i in range(3)]
    return Pm(perm)@np.diag(dtot)
print("   base point b = %s ; roots there %s"%(b,'  '.join('%+.3f%+.3fi'%(x.real,x.imag) for x in base_roots)))
gens=[]
for c in (2/np.sqrt(3),-2/np.sqrt(3)):
    for rad in (0.10,0.20):
        U=based_loop(c,rad); gens.append(U)
        print("   loop about %+.4f rad %.2f : det %+.4f%+.4fi   |diag| %s"%(c,rad,
              np.linalg.det(U).real,np.linalg.det(U).imag,'  '.join('%.4f'%abs(x) for x in np.diag(U@Pm([0,1,2]).T) if abs(x)>1e-12) or '-'))
print()
C=gens[0]@gens[2]-gens[2]@gens[0]
print("   [loop(+pole), loop(-pole)] non-zero: %s   max |entry| %.4f"%(not np.allclose(C,0,atol=1e-8), abs(C).max()))
rows=[np.kron(U.T,U.conj().T)-np.eye(9) for U in gens]
A=np.vstack(rows); sv=np.linalg.svd(A,compute_uv=False)
print("   invariant HERMITIAN forms: smallest sv %s -> dim %d"%('  '.join('%.2e'%x for x in sorted(sv)[:3]),
      9-np.linalg.matrix_rank(A,tol=1e-6*max(sv))))
