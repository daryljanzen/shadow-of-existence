import numpy as np
# Test: is the sheet triple the generation triple? Compare the two cubics' roots.
w=0.5
gens=[(2/np.sqrt(3))*np.sin(w+2*np.pi*k/3) for k in range(3)]   # generations: roots of r0^3 - r0 + 2M = 0
twoM=gens[0]-gens[0]**3
tau=0.7; base=(twoM*np.sinh(1.5*tau)**2)**(1/3)
sheets=[base*np.exp(2j*np.pi*k/3) for k in range(3)]            # sheets: cube roots of r^3 = 2M sinh^2 (no linear term)
print("generation |r0| (UNEQUAL, cubic has linear term):", [round(abs(g),4) for g in gens])
print("sheet      |r|  (EQUAL,   cubic r^3=const)      :", [round(abs(z),4) for z in sheets])
print("=> different cubics => different triples => sheets are NOT generations.")
print("   shared: central Z2 charge conj r->-r ; A2 pervades in two guises (physical vs kinematic).")
