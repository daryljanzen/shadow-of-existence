"""SCALAR adiabaticity AT ACTUAL MULTIPOLES.  |dw/ds|/w^2 = D/k with D -> ~1.4 (units alpha=1).
Comoving k for multipole l is k ~ l/D_A.  Need D_A in units of alpha."""
import numpy as np
H0=67.40/299792.458      # 1/Mpc
Om=0.3150; OL=1-Om
alpha=1.0/(H0*np.sqrt(OL))          # alpha = 1/sqrt(Lambda/3) = 1/(H0 sqrt(OL))
D_A=13865.0                          # comoving distance to last scattering, Mpc
print("   alpha = %.1f Mpc ;  D_A = %.0f Mpc  ->  D_A = %.3f alpha"%(alpha,D_A,D_A/alpha))
D=1.41                               # scalar coefficient at the branch point, units alpha=1
print("   scalar adiabaticity parameter = D/k with D = %.2f (alpha=1)"%D)
print()
print("       l     k = l/D_A [1/alpha]    D/k        controlled?")
for l in (2,3,4,5,8,15):
    k=l/(D_A/alpha)
    print("     %4d      %8.4f          %7.3f     %s"%(l,k,D/k,"NO - order unity" if D/k>0.5 else "yes"))
print()
r=(D/(2/(D_A/alpha)))/(D/(3/(D_A/alpha)))
print("   ratio l=2 : l=3  =  %.3f   (exactly 3/2, since the parameter goes as 1/l)"%r)
print("   compare the TENSOR ratio n=2:n=3 = mu_3/mu_2 = %.3f"%(np.sqrt(3*5-2)/np.sqrt(2*4-2)))
