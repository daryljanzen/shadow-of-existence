"""Is theta(radius) smooth and monotone -- a genuine continuous holonomy -- or noise?"""
import numpy as np
c=2/np.sqrt(3); M2=lambda r0: r0-r0**3
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
    return 0j if abs(den)<1e-12 else -(r+2*r0)/den + 0.5
print("   radius     theta (deg)     |U_1|      product")
prev=None
for rad in (0.30,0.25,0.20,0.15,0.12,0.10,0.08,0.06,0.05,0.04):
    N=5000; th=np.linspace(0,2*np.pi,N); p=c+rad*np.exp(1j*th)
    R=track(p); U=np.ones(3,dtype=complex)
    for i in range(N-1):
        U=U*np.exp(np.array([a_coef(p[i],R[i][k]) for k in range(3)])*(p[i+1]-p[i]))
    ang=np.degrees(np.angle(U[0]))
    print("   %.3f      %+9.3f     %.5f    %+.5f"%(rad,ang,abs(U[0]),np.prod(U).real))
print()
print("   if theta varies SMOOTHLY with radius -> genuine non-flat connection, continuous holonomy.")
print("   if it jumps randomly -> numerical noise.")
