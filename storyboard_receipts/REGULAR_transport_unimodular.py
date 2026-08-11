"""The connection where the residue form is REGULAR: stay between Nariai points.
At E=0 the discriminant vanishes at sin3w=+-1, i.e. w = pi/6, pi/2, 5pi/6...
So (pi/6, pi/2) is a regular interval.  Integrate the metric connection across it."""
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
            j=min((j for j in range(3) if not used[j]), key=lambda j: abs(r[j]-p))
            cur[i]=r[j]; used[j]=True
        out.append(cur)
    return np.array(out)
lo,hi=np.pi/6+0.05, np.pi/2-0.05          # strictly inside the regular interval
N=4000; ws=np.linspace(lo,hi,N); R=track(ws)
G=lambda r: np.diag(np.real(1.0/(3*r**2-al**2)))
print("   regular interval: w in (pi/6, pi/2) = (%.4f, %.4f), sampled inside"%(np.pi/6,np.pi/2))
print("   residue weights at the ends:")
for k in (0,N-1):
    print("      w=%.4f : %s"%(ws[k],'  '.join('%+9.4f'%x for x in np.real(1/(3*R[k]**2-al**2)))))
print("      signature at both ends: ", [int(np.sign(x)) for x in np.real(1/(3*R[0]**2-al**2))],
      [int(np.sign(x)) for x in np.real(1/(3*R[-1]**2-al**2))])
U=np.eye(3)
for i in range(N-1):
    G0,G1=G(R[i]),G(R[i+1]); Gm=0.5*(G0+G1); dG=G1-G0
    U=(np.eye(3)-0.5*np.linalg.solve(Gm,dG))@U
print()
print("   transport across the regular interval:")
for row in U: print("      [%s]"%'  '.join('%+9.5f'%x for x in row))
print("   det U = %+.6f"%np.linalg.det(U))
# check: for diagonal G the exact answer is sqrt(G_start/G_end) componentwise
ex=np.sqrt(np.abs(np.diag(G(R[0]))/np.diag(G(R[-1]))))
print("   exact (diagonal) prediction sqrt(G0/G1): %s"%'  '.join('%+9.5f'%x for x in ex))
print("   matches numerics:", np.allclose(np.abs(np.diag(U)), ex, rtol=1e-3))
