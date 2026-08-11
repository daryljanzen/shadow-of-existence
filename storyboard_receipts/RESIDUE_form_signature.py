"""The fibre is FUNCTIONS on the root set; its natural form is the RESIDUE pairing,
diagonal with entries 1/f'(r_i) = 1/(2 kappa_i) -- the surface gravities the corpus already assigns.
Compute the metric connection it induces and the holonomy around the dial."""
import numpy as np
al=1.0
def raw(w):
    M2=(2/(3*np.sqrt(3)))*al*np.sin(3*w)
    return np.roots([1,0,-al**2, M2*al**2])
def track(ws):
    out=[np.sort_complex(raw(ws[0]))]
    for w in ws[1:]:
        r=raw(w); prev=out[-1]; used=[False]*3; cur=np.zeros(3,dtype=complex)
        for i,p in enumerate(prev):
            k=min((j for j in range(3) if not used[j]), key=lambda j: abs(r[j]-p))
            cur[i]=r[k]; used[k]=True
        out.append(cur)
    return np.array(out)
def fprime(r, w):
    """f(r) = 1 - 2M/r - r^2/a^2 ; but on the cubic r^3 - a^2 r + 2M a^2 = 0 use the polynomial's derivative"""
    return 3*r**2 - al**2                      # d/dr of r^3 - a^2 r + 2M a^2
N=3000; period=2*np.pi/3
ws=np.linspace(1e-3,1e-3+period,N); R=track(ws)
def G_of(r,w):
    d=np.real(1.0/fprime(r,w))
    return np.diag(d)
print("   residue weights 1/f'(r_i) at three dial positions:")
for k in (0, N//4, N//2):
    d=np.real(1.0/fprime(R[k],ws[k]))
    print("      w=%.3f : %s"%(ws[k], '  '.join('%+9.4f'%x for x in d)))
print()
U=np.eye(3)
for i in range(N-1):
    G0,G1=G_of(R[i],ws[i]),G_of(R[i+1],ws[i+1])
    Gm=0.5*(G0+G1); dG=G1-G0
    with np.errstate(all='ignore'):
        step=np.eye(3)-0.5*np.linalg.solve(Gm+1e-9*np.eye(3),dG)
    U=step@U
print("   holonomy around one dial period (residue form):")
for row in U: print("      [%s]"%'  '.join('%+10.5f'%x for x in row))
print("   det U = %+.6f"%np.linalg.det(U))
print("   diagonal? %s   -> abelian, in the CARTAN torus"%np.allclose(U,np.diag(np.diag(U)),atol=1e-6))
print("   eigenvalues: %s"%'  '.join('%+.5f'%x for x in np.real(np.linalg.eigvals(U))))
