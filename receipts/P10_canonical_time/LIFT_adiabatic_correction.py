"""THE ADIABATIC CORRECTION.  Exact Euclidean suppression for mode n is exp(-int omega_n ds),
with omega_n = mu_n / a  (P10 sec:lock) and a = |r| along the lift.  omega DIVERGES at the branch
point (a->0).  Does the exponent converge?  And is the evolution adiabatic (|dw/ds|/w^2 << 1)?
ORIGIN: storyboard_receipts/LIFT_adiabatic_correction.py -- registered r2376 (c54); edit the origin, not this copy."""
import numpy as np
from scipy.integrate import quad
a=1.0; M=a/(3*np.sqrt(3)); A=(2*M*a**2)**(1./3); smax=np.pi*a/3.0
r_of=lambda s: -A*np.abs(np.sin(1.5*s/a))**(2./3)
absr=lambda s: abs(r_of(s))
print("   omega_n(s) = mu_n / |r(s)| ;  |r| ~ A (3s/2a)^{2/3} near the branch point (s->0)")
print("   so omega ~ s^{-2/3} : DIVERGES pointwise.  Exponent = mu_n * I,  I = int ds/|r|.")
print()
for lo in (1e-4,1e-6,1e-8,1e-10):
    I,_=quad(lambda s: 1.0/absr(s), lo, smax, limit=400)
    print("      I = int_%.0e^{pi a/3} ds/|r| = %10.6f"%(lo,I))
I,_=quad(lambda s: 1.0/absr(s), 0, smax, limit=800, points=[0])
print("      I (full)                        = %10.6f   -> CONVERGES (integrand ~ s^{-2/3})"%I)
print()
print("   compare the NAIVE constant-frequency exponent using a = A throughout:  I_naive = smax/A = %.6f"%(smax/A))
print("   ratio exact/naive = %.4f"%(I/(smax/A)))
print()
print("   adiabaticity  |dw/ds|/w^2 = |d(1/|r|)/ds| * |r|^2 / mu_n  (per unit mu_n):")
for s in (0.05,0.2,0.5,0.9):
    h=1e-6; w=1/absr(s); dw=(1/absr(s+h)-1/absr(s-h))/(2*h)
    print("      s=%.2f : |dw/ds|/w^2 = %.4f / mu_n"%(s,abs(dw)/w**2))

# --- r2376+c54.158 -------------------------------------------------------------------
# PINS THIS RECEIPT'S OWN CLAIM.  omega_n = mu_n/|r| diverges pointwise at the branch
# point, but the Euclidean exponent I = int_0^{pi a/3} ds/|r| CONVERGES to the value this
# receipt prints, 3.338738; the naive constant-frequency exponent is smax/A = 1.439614,
# so exact/naive = 2.3192.  The final adiabaticity row (s=0.90) is 0.1606/mu_n, i.e. < 1.
assert np.isfinite(I) and abs(I - 3.338738) < 1e-6, "exponent int ds/|r| = %.6f, not 3.338738" % I
assert abs(smax/A - 1.439614) < 1e-6, "naive exponent smax/A = %.6f, not 1.439614" % (smax/A)
assert abs(I/(smax/A) - 2.31919) < 1e-5, "exact/naive = %.4f, not 2.3192" % (I/(smax/A))
assert abs(abs(dw)/w**2 - 0.160619) < 1e-6, "adiabaticity at s=0.90 = %.4f, not 0.1606" % (abs(dw)/w**2)
assert abs(dw)/w**2 < 1.0, "evolution is NOT adiabatic at s=0.90"
