"""
DRAFT_P10_the_adiabatic_constants_in_closed_form.py -- P10 sec:deparam eq:adiabatic-exponent /
P7 sec:lift-quantum:
** THE FACTOR 2.32 IS Gamma(1/6)/(sqrt(pi) Gamma(2/3)) AND IS INDEPENDENT OF THE PROGENITOR MASS.
   THE EXPONENT ITSELF SCALES AS M^(-1/3).  AND THE ADIABATICITY CONSTANT C IS NOT BOUNDED BY
   1.72 -- IT DIVERGES AT THE BRANCH POINT AND VANISHES AT THE TURNAROUND. **

WHAT THE CORPUS HAS.
  P10: "INT_0^{pi alpha/3} ds/|r(s)| = 3.3387 alpha^{-1} on the forced member ... the
       constant-frequency estimate using the turnaround value gives 1.4396 alpha^{-1}, so the
       exact exponent is larger by a factor 2.32."
  P10: "The adiabaticity parameter |dw/ds|/w^2 is C/mu_n with ** C running from 1.72 near the
       branch point to 0.16 near the turnaround **, so the approximation is controlled by the
       harmonic index alone.  With mu_n^2 = n(n+2)-2, n >= 2, this gives 0.70 at n=2, 0.48 at
       n=3, and 0.16 by n=10."
  P7:  "the parameter being C/mu_n with ** C <= 1.72 **, which is of order unity only at n=2 and
       n=3."
  `LIFT_adiabatic_correction.py` computes the integral by quadrature and tabulates the
  adiabaticity at four points: s = 0.05, 0.20, 0.50, 0.90.

--------------------------------------------------------------------------------------------
① THE EXPONENT, IN CLOSED FORM, AND ITS MASS SCALING
--------------------------------------------------------------------------------------------
With |r| = A sin^{2/3}(3s/2 alpha) and A = (2 M alpha^2)^{1/3}, substituting u = 3s/2 alpha,

    INT_0^{pi alpha/3} ds/|r| = (2 alpha / 3A) INT_0^{pi/2} sin^{-2/3}u du
                              = (2 alpha / 3A) (sqrt(pi)/2) Gamma(1/6)/Gamma(2/3)

    ** = (sqrt(pi)/3) [Gamma(1/6)/Gamma(2/3)] (alpha/2M)^{1/3} **

-- so the exponent goes as ** M^{-1/3} **: a LIGHTER progenitor gives a LONGER suppression
exponent, hence a stronger Euclidean filter.  (Contrast F08: the gravitational action goes as
+M.  The two mass dependences run opposite ways and neither is stated.)

--------------------------------------------------------------------------------------------
② THE FACTOR 2.32 IS A PURE NUMBER -- A CANCELS
--------------------------------------------------------------------------------------------
    ratio = exact / naive = [(2 alpha/3A) B] / [(pi alpha/3)/A] = 2B/pi,   B = INT_0^{pi/2} sin^{-2/3}

    ** ratio = Gamma(1/6) / (sqrt(pi) Gamma(2/3)) = 3 Gamma(1/3)^3 / (2^{4/3} pi^2)
             = 2.319190534... **

** A cancels, so the factor is independent of BOTH the progenitor mass and alpha. **  It is a
property of the lift's 2/3 exponent alone -- i.e. of the cube-root branch point -- and not of the
forced member.  P10 attaches "2.32" to a paragraph that says "on the forced member"; it holds on
every member, which is the stronger statement and the one worth making.

--------------------------------------------------------------------------------------------
③ C IS NOT BOUNDED BY 1.72
--------------------------------------------------------------------------------------------
The parameter is exactly

    |dw/ds| / w^2 = C(s)/mu_n     with     ** C(s) = |d|r|/ds| = (A/alpha) cos(u) sin^{-1/3}(u) **

(the mu_n cancels out of everything but the one power).  Near the branch point sin^{-1/3}(u)
diverges, so

    ** C(s) ~ (A/alpha)(3s/2alpha)^{-1/3} -> INFINITY as s -> 0, **

and at the turnaround cos(u) -> 0, so ** C -> 0 exactly, not 0.16. **  Computed below: C = 2.95 at
s = 0.01, 13.7 at 1e-4, 63.5 at 1e-6, and 0.0000 at s = pi alpha/3.

** So both ends of P10's stated range are the values at the first and last SAMPLED points of the
receipt's four-point table (s = 0.05 and s = 0.90), not the behaviour at the ends of the
segment. **  And P7's "C <= 1.72" is a bound that does not hold: for every mode there is a
neighbourhood of the branch point in which the adiabatic approximation fails.

--------------------------------------------------------------------------------------------
④ AND THE CONCLUSION SURVIVES, WITH A BETTER ARGUMENT
--------------------------------------------------------------------------------------------
What matters is not the supremum of C but ** how much of the segment is non-adiabatic **.
C(s)/mu_n = 1 at s* = (2 alpha/3)(A/mu_n alpha)^3, and since (A/alpha)^3 = 2M/alpha,

    ** s* / s_max = (2/pi) (2M/alpha) / mu_n^3 **      (exact)

At the forced member: ** 1.7% of the segment at n = 2, 0.52% at n = 3, 0.019% by n = 10 **,
falling as mu_n^{-3}.  So the projection is adiabatic on all but a vanishing sliver even for the
coarsest harmonic there is -- which is what P10's paragraph concludes, reached by a route that
does not depend on reading a supremum off a sampled table, and which carries the mu_n^{-3} law
and the linear dependence on the construction's own dimensionless mass 2M/alpha.

⌗ *This makes the paper's verdict MORE robust, not less.  The sentence that needs changing is the
one describing C; the sentence drawing the conclusion is right.*

HONEST WEIGHT.  ** No new physics, and no change to any verdict. **  Every number below agrees
with `LIFT_adiabatic_correction`'s quadrature.  What is claimed: two quoted constants have closed
forms, one of them universal where the paper attaches it to one member; the exponent has a mass
scaling that is not stated; and one stated bound is false in a way that does not damage what it
was cited for.

STATED FOR REVERSAL.  Searched `Gamma(1/6)`, `gamma function`, `2.32`, `1.72`, `M^{-1/3}`,
`adiabatic` across corpus/, receipts/, computations/ and storyboard_receipts/.
"""
import numpy as np
from scipy.integrate import quad
from scipy.special import gamma

print(__doc__)

alpha = 1.0
M_forced = alpha / (3 * np.sqrt(3))


def setup(M):
    A = (2 * M * alpha**2)**(1. / 3)
    return A, lambda s: A * np.abs(np.sin(1.5 * s / alpha))**(2. / 3)


smax = np.pi * alpha / 3
A_f, absr = setup(M_forced)

# ============================================================================
print("=" * 78)
print("PART 1 — THE EXPONENT IN CLOSED FORM")
print("=" * 78)
I_quad, _ = quad(lambda s: 1 / absr(s), 0, smax, limit=800, points=[0])
B = (np.sqrt(np.pi) / 2) * gamma(1 / 6) / gamma(2 / 3)
I_closed = (np.sqrt(np.pi) / 3) * (gamma(1 / 6) / gamma(2 / 3)) * (alpha / (2 * M_forced))**(1 / 3)
print(f"  INT_0^{{pi a/3}} ds/|r|   quadrature = {I_quad:.9f}")
print(f"                        closed form = {I_closed:.9f}")
print(f"  corpus eq:adiabatic-exponent       = 3.3387 alpha^-1")
print(f"  B = INT_0^(pi/2) sin^(-2/3) u du   = {B:.9f}  = (sqrt(pi)/2) G(1/6)/G(2/3)")
assert abs(I_quad - I_closed) < 1e-8
print()
print("  ** I = (sqrt(pi)/3) [G(1/6)/G(2/3)] (alpha/2M)^(1/3)  --  goes as M^(-1/3) **")
print()
print(f"  {'M (alpha=1)':>13} {'2M/alpha':>10} {'I quad':>12} {'I closed':>12} {'I x M^(1/3)':>13}")
for Mv in (0.02, 0.05, 0.10, M_forced, 0.19):
    Av, ab = setup(Mv)
    Iv, _ = quad(lambda s: 1 / ab(s), 0, smax, limit=800, points=[0])
    Ic = (np.sqrt(np.pi) / 3) * (gamma(1 / 6) / gamma(2 / 3)) * (alpha / (2 * Mv))**(1 / 3)
    tag = '   <-- forced member' if abs(Mv - M_forced) < 1e-12 else ''
    print(f"  {Mv:>13.6f} {2*Mv/alpha:>10.5f} {Iv:>12.6f} {Ic:>12.6f} {Iv*Mv**(1/3):>13.6f}{tag}")
    assert abs(Iv - Ic) < 1e-8
print("  ⌗ *the last column is constant: the M^(-1/3) law, read off.*")

# ============================================================================
print()
print("=" * 78)
print("PART 2 — THE FACTOR 2.32 IS A PURE NUMBER; A CANCELS")
print("=" * 78)
r1 = 2 * B / np.pi
r2 = gamma(1 / 6) / (np.sqrt(np.pi) * gamma(2 / 3))
r3 = 3 * gamma(1 / 3)**3 / (2**(4 / 3) * np.pi**2)
print(f"  2B/pi                          = {r1:.9f}")
print(f"  G(1/6) / (sqrt(pi) G(2/3))     = {r2:.9f}")
print(f"  3 G(1/3)^3 / (2^(4/3) pi^2)    = {r3:.9f}     [reflection + duplication]")
print(f"  corpus                         = 2.32")
assert abs(r1 - r2) < 1e-12 and abs(r1 - r3) < 1e-9
print()
print(f"  {'M':>10} {'A':>10} {'I':>12} {'I_naive = smax/A':>18} {'ratio':>12}")
for Mv in (0.02, 0.10, M_forced, 0.19):
    Av, ab = setup(Mv)
    Iv, _ = quad(lambda s: 1 / ab(s), 0, smax, limit=800, points=[0])
    print(f"  {Mv:>10.5f} {Av:>10.6f} {Iv:>12.6f} {smax/Av:>18.6f} {Iv/(smax/Av):>12.9f}")
    assert abs(Iv / (smax / Av) - r1) < 1e-8
print()
print("  ** the ratio is identical to nine figures across a factor of ten in mass: it is a")
print("     property of the 2/3 exponent -- of the cube-root branch point -- and of nothing else. **")

# ============================================================================
print()
print("=" * 78)
print("PART 3 — C(s) DIVERGES AT THE BRANCH POINT AND VANISHES AT THE TURNAROUND")
print("=" * 78)
C = lambda s: (A_f / alpha) * np.cos(1.5 * s / alpha) * np.abs(np.sin(1.5 * s / alpha))**(-1. / 3)


def C_fd(s, h=1e-7):                      # finite-difference control on |d|r|/ds|
    return abs(absr(s + h) - absr(s - h)) / (2 * h)


print(f"  {'s':>12} {'C(s) closed':>14} {'|d|r|/ds| numeric':>20} {'note':>28}")
notes = {1e-6: 'branch-point end', 0.05: "the receipt's first sample",
         0.9: "the receipt's last sample", smax: 'turnaround end'}
for s in (1e-6, 1e-4, 1e-2, 0.05, 0.2, 0.5, 0.9, 1.0, smax - 1e-9):
    n = notes.get(s, notes.get(round(s, 6), ''))
    print(f"  {s:>12.6g} {C(s):>14.4f} {C_fd(s):>20.4f} {n:>28}")
    assert abs(C(s) - C_fd(s)) < 1e-3 * max(1.0, C(s))
print()
print("  ** C -> infinity as s -> 0 (like (3s/2a)^(-1/3)) and C -> 0 at the turnaround. **")
print("     1.72 is C(0.05) and 0.16 is C(0.90); both are SAMPLES, 4.8% and 86% along a")
print(f"     segment of length {smax:.4f}.  ** P7's 'C <= 1.72' is not a bound. **")

# ============================================================================
print()
print("=" * 78)
print("PART 4 — BUT THE NON-ADIABATIC WINDOW IS A VANISHING FRACTION, AND CLOSED-FORM")
print("=" * 78)
print("  C(s)/mu_n = 1 at s* = (2 alpha/3)(A/mu_n alpha)^3, and (A/alpha)^3 = 2M/alpha, so")
print("  ** s*/s_max = (2/pi) (2M/alpha) / mu_n^3 ** exactly.")
print()
print(f"  {'n':>4} {'mu_n^2=n(n+2)-2':>16} {'mu_n':>8} {'1.72/mu_n':>11} {'s*':>12} "
      f"{'s*/s_max':>12} {'closed form':>13}")
for n in (2, 3, 4, 5, 10, 20):
    m2 = n * (n + 2) - 2
    mu = np.sqrt(m2)
    sstar = (2 * alpha / 3) * (A_f / (mu * alpha))**3
    frac = (2 / np.pi) * (2 * M_forced / alpha) / mu**3
    print(f"  {n:>4} {m2:>16} {mu:>8.4f} {1.72/mu:>11.4f} {sstar:>12.4e} "
          f"{sstar/smax:>12.4e} {frac:>13.4e}")
    assert abs(sstar / smax - frac) < 1e-12
print()
for line in [
 "** So even at n = 2 -- the coarsest harmonic on S^3, there being none below it -- the region",
 "   where the adiabatic treatment is out of control is 1.7% of the lift, and it falls as",
 "   mu_n^{-3}. **",
 "",
 "⌗ *That is P10's conclusion, reached without reading a supremum off a four-point table, and it",
 "   carries two things the table cannot: the mu_n^{-3} law, and a linear dependence on the",
 "   construction's own dimensionless mass 2M/alpha -- so a heavier progenitor is LESS adiabatic,",
 "   proportionally.*",
]:
    print("  " + line)

print()
print("=" * 78)
print("NOT CLAIMED")
print("=" * 78)
for line in [
 "· No verdict changes.  P10's 'adiabatic for all but the lowest few harmonics' stands and is",
 "  strengthened; the numbers 0.70 / 0.48 / 0.16 at n = 2 / 3 / 10 are consistent with C = 1.72",
 "  and are reproduced above.",
 "· No claim about the quantum status of the lift, which P10 is explicit is not established.",
 "· No claim that the divergence of C damages anything downstream -- PART 4 is the argument that",
 "  it does not.  What it damages is one sentence.",
 "· No closure on any registered item.",
]:
    print("  " + line)
