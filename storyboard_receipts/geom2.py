import numpy as np
np.set_printoptions(precision=4, suppress=True)
eta = np.diag([-1.,1.,1.])
def ip(u,v): return u@eta@v
def norm2(u): return ip(u,u)

# verified null generators from step 1 (alpha=1)
A = np.array([1,1,0])/np.sqrt(2)
B = np.array([-1., -1+np.sqrt(2)/2, -np.sqrt(-0.5+np.sqrt(2))])
print("checks: A^2=%.3f B^2=%.3f A.B=%.3f"%(norm2(A),norm2(B),ip(A,B)))

print("\n--- character of the directions the generator-swap involves ---")
print("A-B (swap's reflected axis): norm^2 = %.4f  -> %s"%(norm2(A-B),
      'TIMELIKE' if norm2(A-B)<0 else 'spacelike'))
print("A+B (swap fixes):            norm^2 = %.4f  -> %s"%(norm2(A+B),
      'timelike' if norm2(A+B)<0 else 'SPACELIKE'))

# Build the generator-swap sigma as an explicit linear map on R^{2+1}:
# reflect the A-B axis, fix its eta-orthogonal complement.
def reflect_in_axis(n):
    # reflection sending n->-n, fixing eta-orthogonal complement: M = I - 2 n n^T eta / (n.n)
    n=np.array(n,float); return np.eye(3) - 2*np.outer(n, eta@n)/norm2(n)
sigma = reflect_in_axis(A-B)
print("\nsigma (reflect A-B):")
print(sigma)
print("sigma@A - B =", sigma@A - B, "  sigma@B - A =", sigma@B - A, " (0,0 => swaps A<->B)")
# is sigma an isometry? M^T eta M = eta ?
print("isometry? ||sigma^T eta sigma - eta|| =", np.linalg.norm(sigma.T@eta@sigma - eta))
print("det sigma =", np.linalg.det(sigma), "  (reflection if -1)")

print("\n--- the other candidate reflections ---")
T = np.diag([-1.,1.,1.])   # time reflection X0->-X0
Pareal = np.diag([1.,-1.,1.])  # a spatial parity (reflect X1)
P2 = np.diag([1.,1.,-1.])
for name,M in [("T: X0->-X0",T),("P: X1->-X1",Pareal),("P': X2->-X2",P2)]:
    ax = np.where(np.diag(M)<0)[0]
    print("%-12s reflects axis %s (norm^2=%.1f, %s), isometry_err=%.2e, det=%.0f"%(
        name, ax, norm2(np.eye(3)[ax[0]]),
        'TIMELIKE' if norm2(np.eye(3)[ax[0]])<0 else 'spacelike',
        np.linalg.norm(M.T@eta@M-eta), np.linalg.det(M)))

print("\n--- is sigma (the A<->B swap) equal to T, or to a spatial parity, or a rotation.reflection? ---")
print("sigma vs T  : ||sigma-T|| =", np.linalg.norm(sigma-T))
# decompose sigma: eigen-structure
w,v = np.linalg.eig(sigma)
print("sigma eigenvalues:", np.round(w,4))
for i in range(3):
    vi=np.real(v[:,i]); print("  eigval %+.2f  eigvec %s  norm^2=%.3f (%s)"%(
        np.real(w[i]), np.round(vi,3), norm2(vi), 'timelike' if norm2(vi)<-1e-9 else ('null' if abs(norm2(vi))<1e-9 else 'spacelike')))

print("\n--- ALGEBRA: how sigma, T, P compose ---")
def show(name,M):
    d=np.linalg.det(M); iso=np.linalg.norm(M.T@eta@M-eta)
    print("  %-16s det=%+.0f iso_err=%.1e"%(name,d,iso))
show("sigma", sigma); show("T", T); show("sigma@T", sigma@T); show("T@sigma", T@sigma)
print("  [sigma,T] commute? ||sigmaT - Tsigma|| =", np.linalg.norm(sigma@T - T@sigma))
show("sigma@T@sigma@T (=(sigmaT)^2)", np.linalg.matrix_power(sigma@T,2))
