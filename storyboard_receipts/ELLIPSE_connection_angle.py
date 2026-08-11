"""The ellipse's quadratic form Q = [[1,1/2],[1/2,1]] on the total space (r_0, r) defines a
connection by Q-orthogonality.  The fibre is constrained to the locus g(r)=g(r_0).
Compute the angle between the Q-horizontal direction and the locus tangent, along the locus."""
import numpy as np
Q=np.array([[1.,0.5],[0.5,1.]])
g=lambda t: t**3-t
# locus: g(r) = g(r_0).  branches: r = r_0 (line), and the conic r^2 + r r_0 + r_0^2 = 1
def conic_r(r0):
    disc=1-0.75*r0**2
    if disc<0: return []
    return [(-r0+np.sqrt(4*disc))/2, (-r0-np.sqrt(4*disc))/2]
# Q-horizontal: orthogonal complement of vertical (0,1) under Q -> (1,-1/2)
H=np.array([1.,-0.5]); H=H/np.linalg.norm(H)
print("   Q-horizontal direction (constant): (1, -1/2)/|.| = (%.4f, %.4f)"%(H[0],H[1]))
print("   check Q(H, vertical) = %.2e"%(H@Q@np.array([0.,1.])))
print()
print("   along the CONIC branch, the tangent and its angle to the horizontal:")
print("     r_0        r        tangent            angle to H (deg)")
for r0 in (-1.0,-0.6,-0.2,0.2,0.6,1.0):
    rs=conic_r(r0)
    if not rs: continue
    r=rs[0]
    # implicit F = r^2 + r r0 + r0^2 - 1 = 0 -> dF = (2r + r0) dr + (r + 2r0) dr0 = 0
    tan=np.array([2*r+r0, -(r+2*r0)])       # (dr0, dr) direction
    n=np.linalg.norm(tan)
    if n<1e-12: continue
    tan=tan/n
    ang=np.degrees(np.arccos(np.clip(abs(tan@H),0,1)))
    print("   %+7.3f  %+7.3f   (%+.4f,%+.4f)   %8.3f"%(r0,r,tan[0],tan[1],ang))
print()
print("   => the angle VARIES along the locus: the constant Q-horizontal is not tangent to the locus,")
print("      and the mismatch changes from point to point.  That mismatch is the connection's content.")
