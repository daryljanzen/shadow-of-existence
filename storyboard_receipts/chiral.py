import numpy as np
np.set_printoptions(precision=3, suppress=True)
eta=np.diag([-1.,1.,1.]); ip=lambda u,v:u@eta@v
# one-sheeted hyperboloid -X0^2+X1^2+X2^2=1 ; neck at X0=0, (X1,X2)=(cos p, sin p)
# find the two NULL ruling directions through each neck point, tangent to the surface.
# tangent space at X: vectors t with ip(X,t)=0 (X is the outward eta-normal, ip(X,X)=1).
# null tangent dirs: ip(d,d)=0 and ip(X,d)=0.
def rulings(p):
    X=np.array([0.,np.cos(p),np.sin(p)])
    # basis of tangent space (ip(X,.)=0): the neck tangent, and the X0 axis
    tang=np.array([0.,-np.sin(p),np.cos(p)])   # along neck, spacelike
    axial=np.array([1.,0.,0.])                 # X0 direction, timelike; ip(X,axial)=0 since X0=0
    # d = axial + s*tang ; solve ip(d,d)=0 -> -1 + s^2 =0 -> s=+-1
    dp = axial+1.0*tang; dm = axial-1.0*tang
    return X,tang,axial,dp,dm
print("check null & tangent for a sample point:")
X,tang,axial,dp,dm=rulings(0.7)
print(" ip(dp,dp)=%.3f ip(dm,dm)=%.3f  ip(X,dp)=%.3f ip(X,dm)=%.3f"%(ip(dp,dp),ip(dm,dm),ip(X,dp),ip(X,dm)))

# HANDEDNESS: sign of the ORIENTED triple [X, neck-tangent, ruling-dir] (ordinary 3D det).
# family '+' vs family '-', around the whole neck:
print("\n phi     det[X,tang,d+]   det[X,tang,d-]   (handedness sign, each family)")
for p in np.linspace(0,2*np.pi,8,endpoint=False):
    X,tang,axial,dp,dm=rulings(p)
    hp=np.linalg.det(np.array([X,tang,dp])); hm=np.linalg.det(np.array([X,tang,dm]))
    print("  %4.2f     %+.3f            %+.3f"%(p,hp,hm))

print("\n--- 'left on front, right on back' : sign of the X-component of the ruling dir")
print("    (front ~ X2>0 half, back ~ X2<0 half) for the '+' family (say matter):")
print(" phi   X2(front?)   d+_X1 (points -X1=left / +X1=right)")
for p in np.linspace(0,2*np.pi,8,endpoint=False):
    X,tang,axial,dp,dm=rulings(p)
    side = 'front' if X[2]>=0 else 'back '
    lr = 'left' if dp[1]<0 else 'right'
    print("  %4.2f   %s        d+_X1=%+.2f  -> points %s"%(p,side,dp[1],lr))

print("\nSUMMARY: the two families carry OPPOSITE, globally-consistent handedness (det sign),")
print("and one family's worldlines point one way on the front and the mirror way on the back.")
print("The mirror family does the opposite. That handedness = chirality; gamma^5 flips it.")
