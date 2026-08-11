"""Solve for the Hermitian form J with U^dag J U = J for BOTH holonomies, rather than guessing diagonal ones."""
import numpy as np
def P(perm):
    M=np.zeros((3,3),dtype=complex)
    for i,j in enumerate(perm): M[i,j]=1
    return M
D1=np.diag([np.exp(-1j*np.radians(48.71)), np.exp(1j*np.radians(48.71)), 1.0])
U1=P([1,0,2])@D1
lam=2.2572
D2=np.diag([1.0+0j, lam, 1/lam])
U2=P([0,2,1])@D2
# solve the linear system for J (9 complex unknowns): U^dag J U - J = 0 for both
rows=[]
for U in (U1,U2):
    A=np.kron(U.T, U.conj().T) - np.eye(9)     # vec(U^dag J U) = (U^T kron U^dag) vec(J)
    rows.append(A)
Aall=np.vstack(rows)
u,s,vh=np.linalg.svd(Aall)
null=[vh[i].conj() for i in range(9) if s[i] < 1e-8] if len(s)>=9 else []
null=[vh[i].conj() for i in range(len(vh)) if i>=len(s) or s[i]<1e-8]
print("   singular values (smallest 4): %s"%'  '.join('%.2e'%x for x in sorted(s)[:4]))
print("   nullspace dimension: %d"%len(null))
for k,v in enumerate(null[:3]):
    J=v.reshape(3,3)
    J=(J+J.conj().T)/2                      # Hermitian part
    if np.linalg.norm(J)<1e-9: continue
    J=J/np.max(np.abs(J))
    ev=np.linalg.eigvalsh(J)
    p=sum(1 for x in ev if x>1e-8); q=sum(1 for x in ev if x<-1e-8)
    print()
    print("   invariant form #%d:"%(k+1))
    for row in J: print("      [%s]"%'  '.join('%+6.3f%+6.3fi'%(x.real,x.imag) for x in row))
    print("      eigenvalues %s  -> signature (%d,%d)"%('  '.join('%+.4f'%x for x in ev),p,q))
