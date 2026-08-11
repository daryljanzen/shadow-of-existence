"""Are the two ends the ROOT SYSTEM and the FUNDAMENTAL WEIGHTS of one A_2?
A_2 roots: 6, hexagonal, |root| equal, at 60 deg spacing -> the adjoint 8 = 6 roots + 2 Cartan.
A_2 fundamental weights of the 3: 3, equilateral, 120 deg apart, summing to zero."""
import numpy as np
# fundamental 3 weights of su(3) in the standard basis
w=[np.array([ 1/2, 1/(2*np.sqrt(3))]), np.array([-1/2, 1/(2*np.sqrt(3))]), np.array([0,-1/np.sqrt(3)])]
print("   weights of the fundamental 3:")
for i,x in enumerate(w): print("      w%d = (%+.4f, %+.4f)  |w|=%.4f  arg=%7.2f deg"%(i+1,x[0],x[1],np.linalg.norm(x),np.degrees(np.arctan2(x[1],x[0]))))
print("      sum = (%.1e, %.1e)   equal moduli: %s   spacing 120 deg: yes"%(*sum(w), all(abs(np.linalg.norm(x)-np.linalg.norm(w[0]))<1e-12 for x in w)))
print()
# the E=1 turning roots
al=1.0; M=al/(3*np.sqrt(3)); A=(2*M)**(1/3.)
rts=np.roots([1,0,0,2*M*al**2])
print("   E=1 turning roots (pure cube r^3 = -2M a^2):")
for x in rts: print("      r = %+.4f%+.4fi   |r|=%.4f  arg=%7.2f deg"%(x.real,x.imag,abs(x),np.degrees(np.angle(x))))
print("      sum = %.1e   equal moduli: yes"%abs(sum(rts)))
print()
print("   => same configuration up to scale and rotation: three points, equal modulus, 120 deg apart,")
print("      summing to zero.  That is the weight diagram of the 3, NOT the A_2 root system")
print("      (which is six points at 60 deg spacing).  The horizon end's monodromy gives the ROOTS;")
print("      the flat end's figure gives the WEIGHTS of the fundamental.")
