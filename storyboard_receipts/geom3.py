import numpy as np
np.set_printoptions(precision=4, suppress=True)
eta=np.diag([-1.,1.,1.]); ip=lambda u,v:u@eta@v; n2=lambda u:ip(u,u)
A=np.array([1,1,0])/np.sqrt(2); B=np.array([-1.,-1+np.sqrt(2)/2,-np.sqrt(-0.5+np.sqrt(2))])

# reconfirm eta(X,B)=e^tau/2 numerically  (synchronous space = B-ruling)
print("eta(X(tau),B) vs e^tau*eta(A,B):")
for tau in [-1,0,1,2]:
    X=np.exp(tau)*A+np.exp(-tau)*B
    print("  tau=%+d : eta(X,B)=%.5f   e^tau * 1/2 = %.5f"%(tau, ip(X,B), np.exp(tau)*0.5))

def refl(n): n=np.array(n,float); return np.eye(3)-2*np.outer(n,eta@n)/n2(n)
sig=refl(A-B)                 # generator-swap  (verified isometry, timelike axis A-B)
T=np.diag([-1.,1.,1.])        # horn-flip X0->-X0 (timelike)
P=np.diag([1.,-1.,1.])        # a spatial parity  (spacelike)

print("\ncharacter of each single reflection (axis it flips):")
print("  sigma (A<->B swap): flips A-B, TIMELIKE, det=%.0f"%np.linalg.det(sig))
print("  T (horn flip)     : flips X0 , TIMELIKE, det=%.0f"%np.linalg.det(T))
print("  P (offset parity) : flips X1 , SPACELIKE, det=%.0f"%np.linalg.det(P))

print("\n--- generate the group <sigma,T,P>, list distinct elements by (det, #timelike-flips) ---")
gens={'sig':sig,'T':T,'P':P}
from itertools import product
seen={}; 
def key(M): return tuple(np.round(M,6).ravel())
frontier=[('I',np.eye(3))]; seen[key(np.eye(3))]=('I',np.eye(3))
for _ in range(6):
    new=[]
    for nm,M in list(seen.values()):
        for gn,g in gens.items():
            Mp=g@M; k=key(Mp)
            if k not in seen: seen[k]=(gn+'.'+nm,Mp); new.append((gn+'.'+nm,Mp))
    if not new: break
print("group order =",len(seen))
# classify each: det, and how many timelike vs spacelike eigen-flips
def classify(M):
    w,v=np.linalg.eig(M); flips=[]
    for i in range(3):
        if np.real(w[i])<0:
            vi=np.real(v[:,i]); flips.append('t' if n2(vi)<-1e-9 else 's')
    return int(round(np.linalg.det(M))), ''.join(sorted(flips))
from collections import Counter
cnt=Counter(classify(M) for _,M in seen.values())
print("elements by (det, flipped-axis-signature):")
for (d,s),c in sorted(cnt.items()): print("   det=%+d  flips=%-4s  count=%d"%(d,s if s else '(none)',c))

print("\n--- the specific question: is the A<->B swap = P (spacelike) ? or = T ? or PT ? ---")
print("  ||sig - P|| =%.3f   ||sig - T|| =%.3f   ||sig - P@T|| =%.3f   ||sig - T@P||=%.3f"%(
    np.linalg.norm(sig-P),np.linalg.norm(sig-T),np.linalg.norm(sig-P@T),np.linalg.norm(sig-T@P)))
print("  det(P@T)=%.0f  (PT is proper, det+1; sig is a reflection, det-1 -> sig != PT)"%np.linalg.det(P@T))

print("\n--- what proper isometry is sig@T ? (both timelike reflections) ---")
sT=sig@T
w,_=np.linalg.eig(sT)
print("  det(sig@T)=%+.0f  eigenvalues=%s"%(np.linalg.det(sT),np.round(w,3)))
print("  (complex eigenvalues on unit circle => a boost/rotation in the (A-B, X0) timelike-pair plane)")
