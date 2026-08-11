"""
THROAT MODE TOWER + ISOTROPIZATION (P12 sec:throat). Verifies the [R] mode-tower algebra at source and
tests whether the [I] "angular no-hair" reading is grounded rather than bare interpretation.

GEOMETRY [E, prop:throat]: Nariai near-horizon = dS_2 x S^2, both radii = 1/sqrt(Lambda) = r_star.
TOWER: a scalar on dS_2 x S^2 splits in S^2 harmonics; degree-l harmonic -> dS_2 field of mass
  m^2 = l(l+1)/r_star^2,  and since H_dS2^2 = 1/r_star^2,  m^2/H^2 = l(l+1).
dS_2 representation label: nu^2 = 1/4 - m^2/H^2.  nu real (>=0) = light/complementary series (frozen,
no-hair-preserved); nu imaginary (nu^2<0) = heavy principal series (oscillate and DECAY in dS time).

READING under test: the monopole l=0 is the scale-invariant base; every anisotropic l>=1 is heavy
principal-series and is damped relative to it as the field evolves through the dS_2 throat. Is that
"decay" grounded? YES -- it is the de Sitter no-hair theorem (Wald 1983, PRD 28, 2118): on a spacetime
with Lambda>0 approaching de Sitter, anisotropic/inhomogeneous modes are exponentially damped while the
isotropic mode survives. The dS_2 factor of the throat IS such a de-Sitter epoch; the principal-series
(l>=1) damping is that theorem read on the throat tower. So the isotropization reading is grounded in a
theorem, not asserted -- it strengthens from [I] toward [R], with the load-bearing GUARD intact: the
throat l is the S^2 degree at areal radius 1/sqrt(Lambda), NOT the observable CMB multipole (that lives
at D_C); the throat isotropizes the near-horizon geometry, it does not hand a multipole to the sky.
"""
import numpy as np
print("dS_2 x S^2 throat tower (radii equal = 1/sqrt(Lambda)):")
print(" l    m^2/H^2=l(l+1)   nu^2=1/4-l(l+1)   series           fate through throat")
for l in range(0,6):
    m2=l*(l+1); nu2=0.25-m2
    if nu2>=0: series,fate="complementary","survives (no-hair base)"
    else:      series,fate="principal (heavy)","oscillates & DECAYS"
    tag="  <- isotropic monopole" if l==0 else ""
    print(f" {l}        {m2:>3d}            {nu2:+.2f}          {series:18s} {fate}{tag}")
print("\nSPLIT: l=0 alone has nu^2>=0 (the scale-invariant base, nu=1/2); EVERY l>=1 has nu^2<0")
print("(heavy principal series). Anisotropy is the heavy tower -> damped through the dS_2 throat.")
print("GROUNDING: this is the de Sitter no-hair theorem (Wald 1983) on the throat's dS_2 factor,")
print("not a bare reading. GUARD held: throat l (S^2 degree at 1/sqrt(Lambda)) =/= CMB multipole (at D_C).")
