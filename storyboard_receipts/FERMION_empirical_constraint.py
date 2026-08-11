"""What the two fitted ratios REQUIRE of the fermion sector, using only measured quantities.
eta = n_b/n_gamma  (number, baryons)      -> fixes rho_b/rho_gamma at any T
rho_r/rho_m = 2 at onset (energy, all matter) -> fixes rho_m/rho_gamma at that T
The QUOTIENT is an empirical statement about the matter content per baryon."""
import numpy as np
zeta3=1.2020569; T0=2.7255*8.617333e-5   # eV
mp=938.272e6                             # eV
eta=6.10e-10
# rho_b/rho_gamma = eta * (30 zeta3/pi^4) * m_b/T
K=30*zeta3/np.pi**4
print("   30 zeta(3)/pi^4 = %.5f"%K)
print("   rho_b/rho_gamma = %.5f * eta * m_b/T"%K)
print()
print("   The onset is where rho_r/rho_m = 2.  Radiation there is photons + whatever else is relativistic;")
print("   write rho_r = (1+X) rho_gamma with X the non-photon relativistic share (unknown to CR).")
print()
print("       z_onset    T [eV]     rho_b/rho_gamma    rho_m/rho_gamma (X=0)    rho_m/rho_b")
for z in (3000,5000,6848,10000):
    T=T0*(1+z)
    rb=K*eta*mp/T
    rm=(1+0.0)/2.0          # rho_m = rho_r/2 = (1+X) rho_gamma / 2 ; X=0 here
    print("      %6d   %.4f      %10.4f          %10.4f            %8.3f"%(z,T,rb,rm,rm/rb))
print()
print("   => the quotient rho_m/rho_b is FIXED BY THE TWO FITTED RATIOS AND T ALONE.")
print("      It is an empirical number the fermion sector must account for -- not a component posited to meet it.")
