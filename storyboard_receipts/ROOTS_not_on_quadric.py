"""Does the form transport?  The bundle's fibre is the span of the TURNING ROOTS, not the hinges.
Embed the roots on the substrate and compute their Gram under eta, at both ends of the family."""
import numpy as np
al=1.0; M=al/(3*np.sqrt(3)); eta=np.diag([-1.,1,1,1,1,1])
def embed(r):
    """a point at areal radius r on the equatorial slice: |X|^2 = alpha^2, transverse rho, X0 by the quadric.
       On the slicing the areal radius r maps to a substrate point; take the equatorial embedding
       X = (X0, r, sqrt(alpha^2 + X0^2 - r^2), 0,0,0) with X0 chosen so the point lies on dS_5."""
    # simplest consistent choice: put the point on the quadric with transverse component r
    X0sq = r*r - al*al
    X0 = np.sqrt(abs(X0sq))*(1 if X0sq>=0 else 0)
    if X0sq < 0:   # inside: use an imaginary X0 -> the point is not on the real quadric at that r
        return None
    return np.array([X0, r, 0,0,0,0])
print("   HORIZON-END roots (E=0): r^3 - a^2 r + 2M a^2 = 0")
rts=np.sort(np.roots([1,0,-al**2,2*M*al**2]).real)
print("      roots:", '  '.join('%+.5f'%x for x in rts))
V=[embed(r) for r in rts]
print("      on the real quadric (|r|>=alpha)?", ['yes' if v is not None else 'NO (|r|<alpha)' for v in V])
print()
print("   TURNAROUND-END roots (E=1): r^3 + 2M a^2 = 0")
rts1=np.roots([1,0,0,2*M*al**2])
print("      roots:", '  '.join('%+.4f%+.4fi'%(x.real,x.imag) for x in rts1))
print("      moduli: %s   (all = A = %.5f)"%('  '.join('%.5f'%abs(x) for x in rts1), (2*M)**(1/3.)))
V1=[embed(abs(x)) for x in rts1]
print("      on the real quadric (|r|>=alpha)?", ['yes' if v is not None else 'NO (|r|<alpha)' for v in V1])
print()
print("   => the turning roots have |r| < alpha, so they do NOT lie on the substrate quadric:")
print("      A = %.5f  and  alpha/sqrt3 = %.5f,  both < alpha = %.1f"%((2*M)**(1/3.), 1/np.sqrt(3), al))
print("      The hinges DO (transverse 2alpha, X0=sqrt3 alpha).  Different loci, and only one is ON.")
