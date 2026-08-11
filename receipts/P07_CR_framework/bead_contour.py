"""
bead_contour.py -- verifies: cosmic time reads the bead's closed geometry as a BOUNDED contour in the
  complex tau~-plane. With dr/dtau~=sqrt(1-f)=sqrt(2M/r+r^2) (Nariai 2M=2/(3 sqrt3), alpha=1), tau~(r)=
  int dr/sqrt(2M/r+r^2) is: REAL on r>0 (expansion); PURE IMAGINARY on 0->-A with |Im| growing 0->pi/3;
  |Im tau~|=pi/3 at the turnaround r=-A; and on the collapse leg r<-A, |Im tau~| LOCKED at pi/3 while Re
  grows. The lock pi/3=(2/3)(pi/2) is A-INDEPENDENT (a property of the 2/3 exponent), NOT the de Sitter
  thermal period 2pi. [P7 CR_framework -- the bead contour / closure in cosmic time]
STATUS: OK   RUN: python3 bead_contour.py   RUNTIME: ~3s
CONTROL: |Im tau~| on the collapse leg = pi/3, and is NOT 2pi (6x larger -- the retracted thermal claim);
  rescaling A (via a different 2M) leaves the lock at pi/3 (A-independence).
ORIGIN: computations/bead_contour.py, verified + strengthened + canonicalized r1354.
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
