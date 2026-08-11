
import numpy as np
# alpha=1 units. Cosmic-time law r = A*sinh^{2/3}(3 tau~/2), A=(2M)^{1/3}, 2M=2/(3 sqrt3) (Nariai)
M2 = 2/(3*np.sqrt(3)); A = M2**(1/3)
def r_of_tau(tt):                      # tt complex -> r complex
    return A*(np.sinh(1.5*tt))**(2/3)
def tau_of_r(r):                       # r (real, signed) -> tau~ complex (principal)
    z=(complex(r)/A)**1.5
    return (2.0/3.0)*np.arcsinh(z)

print("=== (i) conjugation tau~ -> tau~* : the two wings, real r ===")
for r in [2.0, 0.5, 0.0, -0.3, -A, -1.0, -2.0]:
    t = tau_of_r(r)
    # feed conjugate time back through the forward law:
    r_back      = r_of_tau(t)
    r_back_conj = r_of_tau(np.conj(t))
    print(f" r={r:+.4f}  tau~={t.real:+.4f}{t.imag:+.4f}i   "
          f"r(tau~)={r_back.real:+.4f}{r_back.imag:+.4f}i   "
          f"r(tau~*)={r_back_conj.real:+.4f}{r_back_conj.imag:+.4f}i")

print("\n=== (ii) imaginary shift tau~ -> tau~ + i*Delta : does Delta=2pi/3 rotate r by e^{2pi i/3}? ===")
Delta = 2*np.pi/3
for tt in [0.4, 0.8, 1.2]:
    r0 = r_of_tau(tt+0j)
    r1 = r_of_tau(tt+1j*Delta)
    ratio = r1/r0
    print(f" tau~={tt:.2f}: r={r0.real:+.4f}  r(shifted)={r1.real:+.4f}{r1.imag:+.4f}i  "
          f"ratio={ratio.real:+.4f}{ratio.imag:+.4f}i  |ratio|={abs(ratio):.4f}  arg/pi={np.angle(ratio)/np.pi:+.4f}")
print(f" e^(2pi i/3) = {np.exp(2j*np.pi/3).real:+.4f}{np.exp(2j*np.pi/3).imag:+.4f}i ; the imaginary Wick period is Delta*alpha = 2pi/3 (alpha=1)")

print("\n=== (iii) the turnaround / bound: Im tau~ at r=-A, and pi/3 ===")
tA = tau_of_r(-A)
print(f" r=-A: tau~={tA.real:+.5f}{tA.imag:+.5f}i ; |Im|={abs(tA.imag):.5f} ; pi/3={np.pi/3:.5f} ; half of 2pi/3={np.pi/3:.5f}")
print(f" so the turnaround sits at HALF the full Wick period (pi/3 = (1/2)(2pi/3)); collapse leg holds Im at pi/3.")

# -- APPENDED ASSERT-VERIFICATION (r1353, Arthur) --
e2 = np.exp(2j*np.pi/3)
for r in [-0.3, -0.7, -1.0, -2.0]:
    t = tau_of_r(r)
    assert abs(r_of_tau(np.conj(t)) - np.conj(r_of_tau(t))) < 1e-9, f"conjugate legs at r={r}"
assert abs(tau_of_r(-0.3).real) < 1e-9,            "real r<0 read by a purely imaginary tau~"
for tt in [0.4, 0.8, 1.2, 2.0]:
    assert abs(r_of_tau(tt+1j*2*np.pi/3)/r_of_tau(tt) - e2) < 1e-9, f"e^(2pi i/3) rotation at tau~={tt}"
assert abs(abs(tau_of_r(-A).imag) - np.pi/3) < 1e-6, "turnaround Im tau~ = pi/3 (analytic exact; z=-i is arcsinh branch point, num ~1e-8)"
_ratios = [r_of_tau(tt+1j*1.0)/r_of_tau(tt) for tt in [0.4, 0.8, 1.2]]
assert max(abs(_ratios[k]-_ratios[0]) for k in range(3)) > 1e-3, "CONTROL: generic shift is tau~-DEPENDENT"
print("\n>> AVENUE 11 ASSERTS PASSED: conjugate legs (Schwarz), exact e^(2pi i/3) rotation at period 2pi/3, turnaround at pi/3; generic shift is tau~-dependent.")
