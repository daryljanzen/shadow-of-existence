# CR matter-like high-z rate vs standard radiation-fast rate. Grounds the BBN (second-front) claim.
import numpy as np
H0=67.4; Om=0.315; Or=9.1e-5
H_CR  = lambda z: H0*np.sqrt(Om*(1+z)**3)     # CR: matter-like, no radiation term (P9 §679, eq:friedmann)
H_std = lambda z: H0*np.sqrt(Or*(1+z)**4)     # standard: radiation-dominated at high z
for name,z in [("recombination",1090),("matter-rad equality",3400),("BBN  T~1e9 K",4.0e8)]:
    print(f"{name:22s} z={z:.3g}:  H_std/H_CR = {H_std(z)/H_CR(z):8.1f}x")
print("\nA ~300x-slower expansion at BBN freeze-out alters n/p and the light-element yields:")
print("the radiation-fast rate is what standard BBN needs. This is independent of the CMB front.")
