import numpy as np
np.set_printoptions(precision=3, suppress=True)
# species = WRAP-SENSE = neck-plane handedness = sign of (X1*d2 - X2*d1) for a worldline
# direction d at point X. This is X0-independent by construction.
def wrap(X,d): return np.sign(X[1]*d[2]-X[2]*d[1])

# the two ruling families at neck points (from chiral.py): X, d+ , d-
def fams(p):
    X=np.array([0.,np.cos(p),np.sin(p)]); tang=np.array([0.,-np.sin(p),np.cos(p)]); ax=np.array([1.,0.,0.])
    return X, ax+tang, ax-tang

T =np.diag([-1.,1.,1.])   # X0 reflection (horn flip): flips the ARROW only
P =np.diag([1.,1.,-1.])   # neck-plane reflection (X2): flips the WRAP-SENSE
E =np.diag([-1.,1.,-1.])  # end-over-end = T.P

print("For the '+' worldline family around the neck: wrap-sense, and what each map does to it")
print(" phi    wrap    arrowX0   | after T: wrap,arrow | after P: wrap,arrow | after E: wrap,arrow")
for p in np.linspace(0,2*np.pi,8,endpoint=False):
    X,dp,dm=fams(p)
    w0=wrap(X,dp); a0=np.sign(dp[0])
    for M in (T,P,E):
        MX,Md=M@X,M@dp
    wT,aT=wrap(T@X,T@dp),np.sign((T@dp)[0])
    wP,aP=wrap(P@X,P@dp),np.sign((P@dp)[0])
    wE,aE=wrap(E@X,E@dp),np.sign((E@dp)[0])
    print("  %4.2f   %+d      %+d      |   %+d , %+d        |   %+d , %+d        |   %+d , %+d"%(
        p,w0,a0, wT,aT, wP,aP, wE,aE))

print("\nRead-off:")
print(" T  (X0 reflection): wrap-sense PRESERVED, arrow FLIPPED  -> species preserved => SYMMETRY, no colour swap")
print(" P  (neck reflection): wrap-sense FLIPPED               -> species swapped   => symmetry only WITH colour swap")
print(" E  (end-over-end=T.P): wrap-sense FLIPPED, arrow flipped -> species swapped => symmetry WITH colour swap")
print("\nSo: the species swap lives in the NECK-PLANE (spatial) reflection, not in the arrow.")
print("R at r=0 flips the wrap-sense (gives blue/red their orientation); because that makes the")
print("pattern consistently-handed across both horns, the pure X0 reflection returns the same figure.")

print("\n"+"="*70)
print("Re-check sigma (A<->B generator swap) against the SHARP definition (wrap-sense):")
eta=np.diag([-1.,1.,1.]); ip=lambda u,v:u@eta@v
A=np.array([1,1,0])/np.sqrt(2); B=np.array([-1.,-1+np.sqrt(2)/2,-np.sqrt(-0.5+np.sqrt(2))])
def refl(n): n=np.array(n,float); return np.eye(3)-2*np.outer(n,eta@n)/ip(n,n)
sig=refl(A-B)
for p in np.linspace(0,2*np.pi,4,endpoint=False):
    X,dp,dm=fams(p)
    w0=wrap(X,dp); ws=wrap(sig@X,sig@dp)
    print("  phi=%4.2f: wrap %+d -> after sigma %+d  (%s)"%(p,w0,ws,'FLIPPED=species swap' if ws!=w0 else 'preserved'))
print("\nSpecies-swap class members (flip wrap-sense): P (neck reflection, det-1),  E=T.P=end-over-end (det+1).")
print("NOT in the class (species-preserving): T (X0 reflection, a symmetry).")
print("sigma: read its column above -- it is in the class iff it flips wrap-sense.")
