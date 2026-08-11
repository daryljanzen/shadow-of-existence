"""bead_thermal_period.py (r1622) -- the bead's areal radius closes on EXACTLY the de Sitter
inverse temperature, and the turnaround cubic's Z/3 is that circle's three-fold subdivision.

STATUS: the PERIODICITY is established here. The THERMAL READING IS A LEAD, NOT A RESULT --
see the hold at the foot of this file. Do not cite this as a temperature.

WHERE IT CAME FROM. r1621 (P3 sec:temporal-threeness) established that the turnaround cubic's
Z/3 is the deck action of cosmic time's imaginary period: tau -> tau + 2.pi.i.alpha/3 leaves
r^3 invariant and cycles the three cube-root sheets. That leaves an obvious question the
placement did not ask: r^3 has period 2.pi.alpha/3, but what is the period of r ITSELF?

THE RESULT. r returns to itself only after THREE such shifts -- imaginary period 2.pi.alpha --
and 2.pi.alpha is exactly beta_dS = 2.pi/kappa at the de Sitter horizon's surface gravity
kappa = 1/alpha. So the whole bead (collapse leg, turnaround, expansion leg) is one function
on a circle of circumference beta_dS, and the Z/3 subdivides that circle into three.

WHY THIS IS NOT AUTOMATIC. r^3's invariance under a third of the period is a statement about
sinh^2; the closure of r requires the CUBE-ROOT SHEET to return too, which is a monodromy
question and has to be tracked by continuation rather than read off the formula. The
continuation below does that, off-axis to avoid the r=0 branch point.
"""
import numpy as np
import sympy as sp

# ---------------------------------------------------------------- symbolic: r^3's periods
M, al = sp.symbols('M alpha', positive=True)
t = sp.symbols('tau')
r3 = 2*M*al**2*sp.sinh(3*t/(2*al))**2
third = 2*sp.pi*sp.I*al/3
full  = 3*third                                  # = 2.pi.i.alpha
assert sp.simplify(r3.subs(t, t + third) - r3) == 0, "r^3 not invariant under a third"
assert sp.simplify(r3.subs(t, t + full)  - r3) == 0, "r^3 not invariant under the full turn"
print("1. r^3 is invariant under BOTH 2.pi.i.alpha/3 and 2.pi.i.alpha (symbolic).")
print("   So r^3 alone cannot tell us the period of r: that is a sheet/monodromy question.")

# ------------------------------------------------- numeric: continue the cube-root sheet
def sheet_ratio(T_end, a=1.0, m=0.1, offset=0.35, N=200000):
    """continuously continue r = (r^3)^(1/3) along tau = offset + i*s, s: 0 -> T_end"""
    f = lambda z: 2*m*a**2*np.sinh(3*z/(2*a))**2
    prev = None
    first = None
    for s in np.linspace(0.0, T_end, N):
        v = f(offset + 1j*s)
        roots = np.roots([1, 0, 0, -v])
        if prev is None:
            r = roots[np.argmin(np.abs(roots - np.cbrt(abs(v))))]
            first = r
        else:
            r = roots[np.argmin(np.abs(roots - prev))]   # the continuous branch
        prev = r
    return first, prev

a = 1.0
w = np.exp(2j*np.pi/3)
print()
print("2. THE ARGUMENT IS ALGEBRAIC, and is stated first (added r1675 -- if the question is")
print("   algebraic, answer it algebraically; a sweep is corroboration, never the argument):")
print("     r^3 has tau-period 2.pi.i.alpha/3 (verified symbolically above).")
print("     r = (r^3)^(1/3) is single-valued only on the 3-SHEETED cube-root cover of that")
print("     period, so r itself closes after 3 x (2.pi.i.alpha/3) = 2.pi.i.alpha. One line.")
print()
print("2b. the numerical continuation, as CORROBORATION of the sheet index (alpha=1, M=0.1, off-axis):")
for k, label in [(1, "2.pi.alpha/3   (one third)"),
                 (2, "4.pi.alpha/3   (two thirds)"),
                 (3, "2.pi.alpha     (the full turn)")]:
    r0, r1 = sheet_ratio(k*2*np.pi*a/3, a=a)
    ratio = r1/r0
    expect = w**k
    ok = abs(ratio - expect) < 1e-9
    print(f"   after {label}: r_end/r_start = {ratio.real:+.6f}{ratio.imag:+.6f}i   "
          f"expected omega^{k} = {expect.real:+.6f}{expect.imag:+.6f}i   [{'OK' if ok else 'FAIL'}]")
    assert ok, "sheet continuation did not match omega^k"

r0, r1 = sheet_ratio(2*np.pi*a, a=a)
assert abs(r1 - r0) < 1e-12, "r did not close after 2.pi.alpha"
print(f"   closure residual after 2.pi.alpha: |r_end - r_start| = {abs(r1-r0):.3e}")

# --------------------------------------------------- the de Sitter thermal identification
print()
print("3. the de Sitter horizon: surface gravity kappa = 1/alpha, so")
print("   beta_dS = 2.pi/kappa = 2.pi.alpha   and   T_dS = 1/(2.pi.alpha).")
kappa = sp.Rational(1,1)/al
beta_dS = sp.simplify(2*sp.pi/kappa)
period_r = sp.simplify(3*(2*sp.pi*al/3))
print(f"   beta_dS = {beta_dS} ;  period of r = {period_r} ;  equal: {sp.simplify(beta_dS-period_r)==0}")
assert sp.simplify(beta_dS - period_r) == 0
print("   => the bead's areal radius is periodic in imaginary cosmic time with period EXACTLY")
print("      beta_dS, and the turnaround cubic's Z/3 is that circle's three-fold subdivision.")

print()
print("="*78)
print("ESTABLISHED: the periodicity, the sheet monodromy omega^k, and the numerical identity")
print("of the period with 2.pi/kappa at kappa = 1/alpha.")
print()
print("HELD, DO-NOT-ASSERT (the lead, not the result):")
print("  * That this periodicity CARRIES thermal content. A period in imaginary time equal to")
print("    beta is suggestive of, and is NOT, a temperature: a thermal reading needs a state")
print("    and a KMS condition on it, neither of which is established here.")
print("  * Any claim of RECURRENCE. The period is in IMAGINARY cosmic time. Nothing here says")
print("    the universe repeats, and the result must not be written in a way that reads so.")
print("  * Any connection to P10's kappa = 1/alpha closure or P13's Gibbons-Hawking thermal")
print("    face. Both use the same kappa, which is why the lead is worth working -- and a")
print("    shared symbol is not a shared result.")
print("="*78)
