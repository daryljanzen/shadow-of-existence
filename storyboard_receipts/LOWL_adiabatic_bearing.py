"""Three routes to the same scale, and what the n=2,3 breakdown does to E1.
(a) transmission boundary (r2157):        l ~ 2.5
(b) Euclidean projection incompleteness:  damping e^{-2} at k~2e-4 -> l = kD ~ 3
(c) adiabatic breakdown:                  C/mu_n order unity at n=2,3
Then: E1 predicts C2/C3 = 1.18 (co-starving).  How firm is that AT n=2,3?"""
import numpy as np
D=13865.0
print("   (a) transmission boundary (r2157)              : l ~ 2.5")
k2=2e-4; print("   (b) Euclidean projection e^-2 at k=%.0e     : l = kD = %.1f"%(k2,k2*D))
mu=lambda n: np.sqrt(n*(n+2)-2.0)
print("   (c) adiabaticity C/mu_n, C<=1.72:")
for n in (2,3,4,5,8):
    print("          n=%2d  mu=%6.3f   C/mu = %.3f %s"%(n,mu(n),1.72/mu(n),"  <-- order unity" if 1.72/mu(n)>0.4 else ""))
print()
print("   => three independent routes place the filter's loss of control at the SAME lowest harmonics.")
print()
print("   E1's prediction:  C2/C3 = 0.419/0.354 = %.3f   (co-starving; sky suppresses l=2 ALONE, ~3x)"%(0.419/0.354))
print("   But the adiabaticity parameter DIFFERS between them:")
print("      n=2 : %.3f     n=3 : %.3f     ratio %.2f"%(1.72/mu(2),1.72/mu(3),(1.72/mu(2))/(1.72/mu(3))))
print("   => the correction is ~%.0f%% larger at n=2 than at n=3, and uncontrolled at both."%(100*((1.72/mu(2))/(1.72/mu(3))-1)))
print("      So the CO-STARVING is not firm where the data disagrees with it.")
