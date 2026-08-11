"""The holonomy at E=0.  Build the w-dependent Gram of the (centred, normalised) roots, find the
metric-compatible connection A = -(1/2) G^{-1} dG/dw, integrate around the dial, read the holonomy."""
import numpy as np
from scipy.integrate import solve_ivp
al=1.0
def rts(w):
    M2=(2/(3*np.sqrt(3)))*al*np.sin(3*w)
    r=np.roots([1,0,-al**2, M2*al**2])
    return np.sort_complex(r)                      # consistent ordering along the path
def Gram(w):
    r=rts(w); r=r-r.mean()
    G=np.real(np.outer(r,r.conj()))
    G=G+1e-12*np.eye(3)
    return G
def dG(w,h=1e-6): return (Gram(w+h)-Gram(w-h))/(2*h)
def A(w):
    G=Gram(w); return -0.5*np.linalg.solve(G, dG(w))   # metric-compatible connection form
# integrate the transport U' = -A U around one full period of the dial
def rhs(w,y):
    U=y.reshape(3,3); return (-A(w)@U).flatten()
period=2*np.pi/3                                    # the Z_3 period of the dial
sol=solve_ivp(rhs,[1e-3,1e-3+period],np.eye(3).flatten(),rtol=1e-9,atol=1e-11,dense_output=True)
U=sol.y[:,-1].reshape(3,3)
print("   holonomy matrix around one dial period (E=0):")
for row in U: print("      [%s]"%'  '.join('%+9.5f'%x for x in row))
print()
print("   det U = %+.6f"%np.linalg.det(U))
ev=np.linalg.eigvals(U)
print("   eigenvalues: %s"%'  '.join('%+.4f%+.4fi'%(x.real,x.imag) for x in ev))
print("   |eigenvalues|: %s"%'  '.join('%.5f'%abs(x) for x in ev))
print()
print("   is it a permutation matrix (flat/Galois answer)? ", np.allclose(np.abs(U), (np.abs(U)>0.5).astype(float), atol=1e-3))
print("   is it the identity?                              ", np.allclose(U,np.eye(3),atol=1e-6))
