"""Daryl's geometry: three hinges at transverse distance 2*alpha, equilateral, on BOTH horns of the
one-sheet hyperboloid; a null line connects each hinge to the other horn's hinges at the two ADJACENT
positions.  Test on dS_5:  -X0^2 + |Xspace|^2 = alpha^2."""
import numpy as np
al=1.0
rho=2*al                                  # transverse distance of the hinges
X0=np.sqrt(rho**2-al**2)                  # on the hyperboloid: -X0^2+rho^2=al^2
print("   hinges at transverse rho = %.4f alpha  ->  X0 = +-%.6f alpha (= sqrt3)"%(rho,X0))
th=[0,2*np.pi/3,4*np.pi/3]
up  =[np.array([+X0, rho*np.cos(t), rho*np.sin(t),0,0,0]) for t in th]
dn  =[np.array([-X0, rho*np.cos(t), rho*np.sin(t),0,0,0]) for t in th]
def interval(a,b):
    d=a-b; return -d[0]**2+np.dot(d[1:],d[1:])
print()
print("   interval^2 from each UPPER hinge to each LOWER hinge  (0 = NULL):")
for i in range(3):
    row=[]
    for j in range(3):
        s=interval(up[i],dn[j]); row.append(s)
        tag='NULL' if abs(s)<1e-12 else ('timelike' if s<0 else 'spacelike')
        print("      up%d -> dn%d :  ds^2 = %+9.6f   %s%s"%(i+1,j+1,s,tag,'   <-- adjacent' if i!=j else '   (same hinge)'))
print()
n_null=sum(1 for i in range(3) for j in range(3) if i!=j and abs(interval(up[i],dn[j]))<1e-12)
print("   null connections between horns, distinct hinges: %d"%n_null)
print("   A_2 has 6 roots.   match: %s"%(n_null==6))
print()
print("   same-horn separations (upper to upper), for contrast:")
for i in range(3):
    for j in range(i+1,3):
        print("      up%d -> up%d :  ds^2 = %+9.6f  (spacelike)"%(i+1,j+1,interval(up[i],up[j])))
