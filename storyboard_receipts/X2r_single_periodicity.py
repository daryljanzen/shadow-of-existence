"""X2-REDONE — why the corpus computes in closed form.
CONFIRMATIONS:
 (1) rung/level: tau-tilde is the BEAD TIME -- 'cosmic time COMPLEXIFIED... the same cosmic time continued
     off the real axis, which is what gives it a period' (section 0). The layer's own clock, rung 4.
 (3) apparatus: WHICH CUBIC?  P3 separates two:
        H = r^3 - alpha^2 r + 2M alpha^2   the HORIZON cubic  (the slicing turns; disc CAN vanish -> Nariai)
        T = r^3 + 2M alpha^2               the TURNAROUND cubic (the E=1 congruence turns; disc NEVER vanishes)
     The tau-tilde period belongs to T.  The dial/cover belongs to H.  Do not merge them.
 (4) object/base/dial: r(tau) = (2M a^2)^(1/3) sinh^(2/3)(3 tau / 2 alpha) on the tau-plane;
     and 2M = (2/3sqrt3) sin 3w on the w-dial.
"""
import numpy as np, sympy as sp
t, al, M, w = sp.symbols('tau alpha M w', positive=True)

print("="*78); print("X2-REDONE — SINGLE PERIODICITY, ON BOTH OF THE CORPUS'S OWN OBJECTS"); print("="*78)

print("\nSTEP 1 — the TURNAROUND side (cubic T), in tau-tilde. Verify the period, symbolically.")
r3 = 2*M*al**2*sp.sinh(3*t/(2*al))**2
print("   r^3(tau + 2.pi.i.alpha/3) - r^3(tau) =",
      sp.simplify(sp.expand(r3.subs(t, t + 2*sp.pi*sp.I*al/3) - r3)))
print("   because 3(tau + 2.pi.i.alpha/3)/(2.alpha) = 3tau/2alpha + i.pi and sinh(x+i.pi) = -sinh(x).")

print("\nSTEP 2 — is it SINGLY or DOUBLY periodic?  That, not genus, is what decides elementary vs elliptic.")
f = lambda u: np.sinh(u)**2
rng=np.random.default_rng(11); zs = rng.normal(size=(40,2)) @ np.array([1,1j])
same = lambda W: np.allclose([f(z+W) for z in zs],[f(z) for z in zs], rtol=1e-9, atol=1e-9)
print(f"   known period i.pi:                       {same(1j*np.pi)}")
print(f"   any REAL period a in (0,20]:             {any(same(a) for a in np.linspace(0.01,20,4000))}")
found=[a+1j*b for a in np.linspace(0.05,4,80) for b in np.linspace(0.05,4,80) if same(a+1j*b)]
print(f"   any period with BOTH parts nonzero, box 4x4: {len(found)}")
print("   => ONE period. sinh^2 is SINGLY periodic: a function on the cylinder C/<i.pi> = C^x.")

print("\nSTEP 3 — the HORIZON side (cubic H), in the sky angle w. The same question.")
g = lambda x: np.sin(3*x)
sameg = lambda W: np.allclose([g(z+W) for z in zs],[g(z) for z in zs], rtol=1e-9, atol=1e-9)
print(f"   known period 2.pi/3 (P5 sec:periodicity):  {sameg(2*np.pi/3)}")
print(f"   any IMAGINARY period i.b, b in (0,20]:     {any(sameg(1j*b) for b in np.linspace(0.01,20,4000))}")
foundg=[a+1j*b for a in np.linspace(0.05,4,80) for b in np.linspace(0.05,4,80) if sameg(a+1j*b)]
print(f"   any period with BOTH parts nonzero, box 4x4: {len(foundg)}")
print("   => ONE period. sin 3w is SINGLY periodic too: a function on the cylinder C/<2.pi/3>.")

# --- r2376+c54.159 -----------------------------------------------------------------
# THE CLAIM OF STEPS 1-3, ASSERTED.  INDEX: "Verifies the tau-tilde period symbolically;
# searches for a second period of sinh^2 (none real, none with both parts nonzero); does
# the same for sin 3w (period 2 pi/3, no imaginary one)."
#   · the turnaround period 2 pi i alpha/3 leaves r^3 EXACTLY invariant (symbolic zero);
#   · i.pi IS a period of sinh^2 and i.pi/2 is NOT -- so the period is not finer than stated;
#   · the 4x4 box search returns ZERO second periods for BOTH objects, which is the whole
#     single-vs-double periodicity verdict;
#   · 2.pi/3 IS a period of sin 3w and pi/3 is NOT.
assert sp.simplify(sp.expand(r3.subs(t, t + 2*sp.pi*sp.I*al/3) - r3)) == 0, \
    "tau -> tau + 2 pi i alpha/3 must leave r^3 invariant, exactly"
assert same(1j*np.pi) and not same(1j*np.pi/2), \
    "i.pi must be a period of sinh^2, and i.pi/2 must not be"
assert len(found) == 0, "sinh^2 must have NO period with both parts nonzero"
assert sameg(2*np.pi/3) and not sameg(np.pi/3), \
    "2.pi/3 must be a period of sin 3w, and pi/3 must not be"
assert len(foundg) == 0, "sin 3w must have NO period with both parts nonzero"
# -----------------------------------------------------------------------------------

print("\nSTEP 4 — WHY single periodicity is exactly the closed-form condition.")
print("   A meromorphic function with ONE period omega is a rational function of q = exp(2.pi.i.z/omega)")
print("   -- elementary. With TWO independent periods it is ELLIPTIC, and no elementary closed form exists.")
print("   Check the corpus's two directly:")
import numpy as np, sympy as sp
z=sp.symbols('z')
e1 = sp.simplify(sp.sinh(z)**2 - ((sp.exp(z)-sp.exp(-z))/2)**2)
print(f"     sinh^2(z) as a rational function of exp(z):  sinh^2 - ((e^z - e^-z)/2)^2 = {e1}")
e2 = sp.simplify(sp.sin(3*z).rewrite(sp.exp) - (sp.exp(3*sp.I*z)-sp.exp(-3*sp.I*z))/(2*sp.I))
print(f"     sin 3w  as a rational function of exp(3iw):  sin3w - (e^3iw - e^-3iw)/2i    = {e2}")
print("   Both are rational in the exponential of their own period-variable. ELEMENTARY, both.")

# --- r2376+c54.159 -----------------------------------------------------------------
# THE CLAIM OF STEPS 4-5, ASSERTED.  INDEX: "confirms both are rational in the exponential
# of their own period-variable, hence elementary."  Both residuals must be EXACTLY zero.
# And STEP 5's THREE-FOLD: sin 3w takes the same value at the three preimages w, pi/3 - w,
# -pi/3 - w -- which is what supplies the three horizon roots off one singly-periodic
# function; asserted symbolically at both of the non-trivial preimages.
assert e1 == 0, "sinh^2 must be rational in exp(z)"
assert e2 == 0, "sin 3w must be rational in exp(3iw)"
assert sp.simplify(sp.sin(3*(sp.pi/3 - w)) - sp.sin(3*w)) == 0 \
    and sp.simplify(sp.sin(3*(-sp.pi/3 - w)) - sp.sin(3*w)) == 0, \
    "the triple angle must give sin 3w three preimages w, pi/3 - w, -pi/3 - w"
# -----------------------------------------------------------------------------------

print("\nSTEP 5 — AND EACH IS THAT SAME ELEMENTARY FUNCTION COMPOSED WITH A THREE-FOLD.")
print("   turnaround:  r = (2M a^2)^(1/3) . [sinh^2(3.tau/2a)]^(1/3)   -- single period x CUBE ROOT")
print("   horizon:     2M = (2/3sqrt3) sin(3w),  three preimages w, pi/3-w, -pi/3-w -- single period x TRIPLE ANGLE")
print("   The cube root supplies the Z_3 sheets; the triple angle supplies the three roots.")
print("   *** So each three-ness is ONE SINGLY-PERIODIC ELEMENTARY FUNCTION COMPOSED WITH A THREE-FOLD, ***")
print("   *** and THAT is why sinh^(2/3), sin 3w and sigma(r_0) all close in elementary terms.        ***")

print("\nSTEP 6 — and the two periods are orthogonal in kind, which is P3's own separation sharpened:")
print("   turnaround period:  2.pi.i.alpha/3   PURELY IMAGINARY, in cosmic time tau-tilde")
print("   horizon period:     2.pi/3           PURELY REAL,      in the sky angle w")
print("   P3 sec:temporal-threeness already separates them -- 'a difference between the two order-threes")
print("   deeper than their affine inequivalence' -- and this is the analytic face of that difference:")
print("   one three-ness is periodic along the imaginary axis of the clock, the other along the real")
print("   axis of the dial.  Both single; neither elliptic; and the 3 in each period is the same 3.")
print("="*78)
