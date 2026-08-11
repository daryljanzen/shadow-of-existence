import numpy as np
# Riemann surface of the bead law:  r = (2M)^{1/3} sinh^{2/3}(3 tau/2a),  cubed:  r^3 = 2M sinh^2(w), w=3tau/2a.
# 2M=1 => r^3 = sinh^2(w). Three r-sheets over each w; branch locus, monodromy, sheet species, S3.

# 1. branch locus: r^3 = sinh^2(w) branches where sinh^2(w)=0 => sinh(w)=0 => r=0 (triple point). Only there (finite).
# 2. monodromy around r=0: near w=0, sinh w ~ w, r ~ w^{2/3}; loop w->w e^{2pi i} sends r -> r e^{4pi i/3} (240 deg, order 3).
for k in range(4):
    print(f"loops around r=0: {k}  sheet rotation {np.degrees((4*np.pi/3*k)%(2*np.pi)):.0f} deg")

# 3. three sheets at a matter-side real w>0, with species by sign(Re r)
w=1.0; s=np.sinh(w); base=abs(s)**(2/3); arg0=0.0
sheets=[base*np.exp(1j*(2/3)*(arg0+2*np.pi*k)) for k in range(3)]
for k,z in enumerate(sheets):
    print(f"sheet {k}: r={z:.3f}  {'matter' if z.real>1e-9 else 'antimatter'}")

# 4. S3 = <Z3 sheet-cycle, complex conjugation>. Transpositions:
#    (1 2) = conjugation (swaps antimatter wings, fixes real/photon axis)
#    (0 1),(0 2) = matter <-> antimatter wing (the charge-conjugation involutions)
print("symmetry: S3 = Z3(sheet cycle e^{2pi i/3}) rtimes Z2(conjugation); transpositions = the C-involution class")
