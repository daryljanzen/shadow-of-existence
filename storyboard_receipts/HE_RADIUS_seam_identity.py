"""On the forced (Nariai) member the Hubble-Eddington radius IS the front seam, and the bead's
amplitude is 2^{1/3} times it.  Both exact."""
import numpy as np
al=1.0; M=al/(3*np.sqrt(3))
rHE=(M*al**2)**(1/3.); A=(2*M*al**2)**(1/3.); seam=al/np.sqrt(3)
print("   r_HE = (M a^2)^{1/3} = %.12f"%rHE)
print("   seam = a/sqrt(3)     = %.12f    equal: %s"%(seam, abs(rHE-seam)<1e-14))
print("   A    = (2M a^2)^{1/3}= %.12f    A/r_HE = %.12f = 2^{1/3} : %s"%(A,A/rHE,abs(A/rHE-2**(1/3.))<1e-14))
print()
print("   algebra: M = a/(3 sqrt3) = a/3^{3/2}, so (M a^2)^{1/3} = (a^3/3^{3/2})^{1/3} = a/3^{1/2}.")
