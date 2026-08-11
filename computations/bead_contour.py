"""Bead contour receipt (r974, Arthur). The cosmic-time τ̃-parametrization of the
cosmogenetic bead on the Nariai cut, and its closure structure.

Geometry (α=1 gauge): f(r)=1 - 2M/r - r²,  2M = 2/(3√3) (Nariai).
Two parametrizations of the SAME signed-r range:
  - slicing curve (proper distance l):  dr/dl = √|f|      → turns at f=0 (horizons ±α/√3, −2α/√3); CLOSES (P3, geometric).
  - cosmic-time scale factor (τ̃):       dr/dτ̃ = √(1−f) = √(2M/r + r²)  → turns at 1−f=0, i.e. r=−(2Mα²)^{1/3}=−A (comoving turnaround).
They turn at DIFFERENT r because they are different parametrizations — not a contradiction.
Solution of the τ̃ equation on r>0 is the flat-ΛCDM law r=(2Mα²)^{1/3} sinh^{2/3}(3τ̃/2α).

RESULT (verified numerically below, on the real cut, and analytically via arcsinh):
  τ̃(r) = ∫ dr/√(2M/r + r²) traces a BOUNDED contour in the complex τ̃-plane:
    r>0 (expansion)     : τ̃ real.
    0 → −A (near lap)   : τ̃ pure imaginary, |Im τ̃| growing 0 → πα/3.
    r=−A (turnaround)   : |Im τ̃| = πα/3 exactly (the boing's back). A=(2Mα²)^{1/3}.
    r<−A (collapse leg) : |Im τ̃| LOCKED at πα/3, Re τ̃ grows (prior universe's own expansion).
  The lock value πα/3 is A-INDEPENDENT and is a property of the 2/3 exponent ((2/3)(π/2)=π/3),
  NOT the de Sitter thermal period 2πα (which is 6× larger — that earlier claim was noise, retracted).
  The bead's GEOMETRIC closure (the loop through the roots) is P3 §sec:lap (proven); this contour is
  how COSMIC TIME reads that closed geometry: collapse and expansion as two legs joined through the
  imaginary turnaround, r real throughout. Open (P2 scope, not a blocker): whether the *spacetime*,
  not only the slicing curve, extends through r=0.
SYNCED r2376 (c54.3) from the cited copy receipts/P07_CR_framework/bead_contour.py -- the copy had gained content this origin lacked.
"""
import numpy as np
al=1.0; M2=2/(3*np.sqrt(3)); A=(M2*al**2)**(1/3)

def f(r): return 1 - M2/r - r**2/al**2

def tau(r, n=200000):
    """τ̃(r)=∫ dr'/√(2M/r'+r'²), principal complex sqrt, from ~0 to r."""
    a0 = 1e-9*np.sign(r)
    rs = np.linspace(a0, r, n); dr = rs[1]-rs[0]
    g = np.sqrt((M2/rs + rs**2/al**2).astype(complex))
    return np.sum(dr/g)

if __name__ == "__main__":
    print(f"A=(2M a^2)^(1/3) = {A:.5f}   -2a/sqrt3 = {-2/np.sqrt(3):.5f}   pi a/3 = {np.pi/3:.5f}")
    print("cubic roots:", sorted(np.roots([1,0,-1,M2]), key=lambda z:z.real))
    print("\n  r        Re(tau)     Im(tau)     |Im|/(pi/3)")
    for r in [0.5,0.2,-0.2,-0.5,-A,-0.85,-1.0,-2/np.sqrt(3),-2.0,-4.0]:
        if abs(r+A) < 1e-6: r += 1e-4
        t = tau(r)
        print(f"{r:+.4f}  {t.real:+.5f}   {t.imag:+.5f}    {abs(t.imag)/(np.pi/3):+.4f}")

# -- APPENDED ASSERT-VERIFICATION (r1354, Arthur) --
P3D = np.pi/3
# (1) expansion leg r>0: tau~ real
for r in [0.5, 0.2]:
    assert abs(tau(r).imag) < 1e-3, f"r={r}>0: tau~ real"
# (2) near lap 0->-A: pure imaginary (Re~0), |Im| below pi/3 and growing
t_02, t_05 = tau(-0.2), tau(-0.5)
assert abs(t_02.real) < 1e-3 and abs(t_05.real) < 1e-3,        "0->-A: tau~ pure imaginary (Re=0)"
assert abs(t_02.imag) < abs(t_05.imag) < P3D,                 "|Im| growing toward pi/3 on the near lap"
# (3) collapse leg r<-A: |Im| LOCKED at pi/3, Re grows in |r|
legs = {r: tau(r) for r in [-1.0, -2.0, -4.0]}
for r,t in legs.items():
    assert abs(abs(t.imag)-P3D)/P3D < 0.02, f"r={r}<-A: |Im tau~| locked at pi/3"
res = [abs(legs[r].real) for r in [-1.0,-2.0,-4.0]]
assert res[0] < res[1] < res[2],                              "Re tau~ grows along the collapse leg"
# (4) CONTROL: the lock is pi/3, NOT the thermal 2pi (6x larger)
assert abs(abs(legs[-2.0].imag) - P3D) < 0.02 and abs(abs(legs[-2.0].imag) - 2*np.pi) > 5.0, \
       "CONTROL: lock is pi/3, not the de Sitter thermal period 2pi"
# (5) A-INDEPENDENCE: rescale via a different 2M -> different A, lock still pi/3
def tau_alt(r, M2alt, n=200000):
    a0=1e-9*np.sign(r); rs=np.linspace(a0,r,n); dr=rs[1]-rs[0]
    return np.sum(dr/np.sqrt((M2alt/rs + rs**2).astype(complex)))
M2b=0.5*M2; Ab=(M2b)**(1/3)                     # different A
tb=tau_alt(-3.0, M2b)
assert abs(abs(tb.imag)-P3D)/P3D < 0.03,        "A-independence: collapse-leg |Im|=pi/3 for a rescaled A too"
print(f"\n>> AVENUE 11 ASSERTS PASSED: contour real(r>0)/imag(0->-A)/locked-pi3(r<-A); Re grows on collapse; lock=pi/3 (A-independent), not 2pi. [A={A:.4f}, rescaled Ab={Ab:.4f}]")
