import numpy as np
np.set_printoptions(precision=3, suppress=True)
eta=np.diag([-1.,1.,1.]); ip=lambda u,v:u@eta@v

# hyperboloid -X0^2+X1^2+X2^2=1 ; horns along +-X0, equator X0=0.
# "end over end" = a genuine SPIN (proper rotation of the plotted 3-object) by pi about an
# equatorial axis, flipping the horns. Two candidates: about X1, about X2.
E1=np.diag([-1.,1.,-1.])   # pi-spin about X1-axis  (X0->-X0, X2->-X2)
E2=np.diag([-1.,-1.,1.])   # pi-spin about X2-axis  (X0->-X0, X1->-X1)
for nm,E in [("E1 (spin about X1)",E1),("E2 (spin about X2)",E2)]:
    print("%s : det=%+.0f  involution? E^2=I : %s  isometry? %s"%(
        nm,np.linalg.det(E),np.allclose(E@E,np.eye(3)),np.allclose(E.T@eta@E,eta)))

# the two null ruling families at neck points (from chiral.py)
def fams(p):
    X=np.array([0.,np.cos(p),np.sin(p)]); tang=np.array([0.,-np.sin(p),np.cos(p)]); ax=np.array([1.,0.,0.])
    return X, ax+tang, ax-tang    # X, d+ , d-
def handedness(E):
    # does E carry the '+' family to the '-' family? test: E maps (X,d+) to (E X, E d+);
    # is E d+ the '-' ruling at the image point E X ?  (up to scale/orientation)
    swaps=[]
    for p in np.linspace(0,2*np.pi,12,endpoint=False):
        X,dp,dm=fams(p); EX=E@X; Edp=E@dp
        # image point EX is some neck point at angle p'; get ITS families
        pprime=np.arctan2(EX[2],EX[1])
        Xp,dpp,dmp=fams(pprime)
        # is Edp parallel to dpp (+ family, no swap) or dmp (- family, swap)?
        def par(u,v): 
            u=u/np.linalg.norm(u); v=v/np.linalg.norm(v); return min(np.linalg.norm(u-v),np.linalg.norm(u+v))
        swaps.append('SWAP' if par(Edp,dmp)<par(Edp,dpp) else 'same')
    return swaps
for nm,E in [("E1",E1),("E2",E2)]:
    s=handedness(E); 
    print("\n%s: does the spin send + family -> - family (chirality swap) at each neck pt?"%nm)
    print("   ", s, " -> ", "CHIRALITY SWAPPED everywhere" if all(x=='SWAP' for x in s) else ("no swap" if all(x=='same' for x in s) else "mixed"))

print("\n--- reconcile with R,P,T from before ---")
T=np.diag([-1.,1.,1.]); P1=np.diag([1.,-1.,1.]); P2=np.diag([1.,1.,-1.])
print("E1 = T @ P2 ? ", np.allclose(E1,T@P2), "   E2 = T @ P1 ? ", np.allclose(E2,T@P1))
print("=> end-over-end is a proper involution = (time-flip)(one spatial-flip) = a 'PT' , det=+1")

# the OLD sigma (A<->B swap) for contrast: det -1 reflection -- a DIFFERENT object
A=np.array([1,1,0])/np.sqrt(2); B=np.array([-1.,-1+np.sqrt(2)/2,-np.sqrt(-0.5+np.sqrt(2))])
def refl(n): n=np.array(n,float); return np.eye(3)-2*np.outer(n,eta@n)/ip(n,n)
sig=refl(A-B)
print("\nsigma (A<->B swap): det=%+.0f  (a reflection) -- NOT the same kind as end-over-end (det+1)."%np.linalg.det(sig))
print("So R (species swap = end-over-end = PT, det+1)  !=  sigma (generator-swap reflection, det-1).")
print("That is the resolution: I had been calling sigma 'R'. R is the proper end-over-end involution.")
