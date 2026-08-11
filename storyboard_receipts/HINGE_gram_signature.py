"""The fibre is the span of the three hinges.  The substrate supplies a form on it directly:
eta restricted to that span.  Compute the Gram matrix and its signature -- this is what decides
which real form is available, and it is the substrate's own metric, not an import."""
import numpy as np
al=1.0; rho=2*al; X0=np.sqrt(rho**2-al**2)   # hinges: transverse 2a, X0 = +-sqrt3 a
eta=np.diag([-1.,1,1,1,1,1])
th=[0,2*np.pi/3,4*np.pi/3]
up=[np.array([+X0,rho*np.cos(t),rho*np.sin(t),0,0,0]) for t in th]
dn=[np.array([-X0,rho*np.cos(t),rho*np.sin(t),0,0,0]) for t in th]
def gram(V):
    n=len(V); G=np.zeros((n,n))
    for i in range(n):
        for j in range(n): G[i,j]=V[i]@eta@V[j]
    return G
for V,lab in ((up,'the three UPPER hinges'),(dn,'the three LOWER hinges')):
    G=gram(V); ev=np.linalg.eigvalsh(G)
    p=sum(1 for x in ev if x>1e-9); q=sum(1 for x in ev if x<-1e-9); z=3-p-q
    print("   %s:"%lab)
    print("      Gram (eta products):")
    for row in G: print("        [%s]"%'  '.join('%+7.3f'%x for x in row))
    print("      eigenvalues: %s"%'  '.join('%+.4f'%x for x in ev))
    print("      signature (p,q,zero) = (%d,%d,%d)   det = %+.4f"%(p,q,z,np.linalg.det(G)))
    print()
print("   note: each hinge is ON the quadric, eta(X,X) = alpha^2 = %.1f, so the diagonal is fixed."%al**2)
