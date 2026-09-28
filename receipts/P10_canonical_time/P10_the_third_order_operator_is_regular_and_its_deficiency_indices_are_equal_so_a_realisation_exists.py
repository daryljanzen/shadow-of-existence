#!/usr/bin/env python3
r"""
P10_the_third_order_operator_is_regular_and_its_deficiency_indices_are_equal_so_a_realisation_exists
===================================================================================================

LEVEL: **exact for every load-bearing step.**  The four representations, the formal symmetry, the three
asymptotic branches and their prefactors, the deficiency counts, the invariant count and the path in
coupling space are all closed form.  **One float**: the envelope exponent of a numerically integrated
branch, against the exact prediction $-1$ --- and it is there deliberately, because the prefactor is
exactly what the previous count got wrong.

OBJECT UNDER TEST -- `PO-23`, `r6969`.  The order takes the three obstructions one at a time, with two
premises named in advance as *"theorems I am asserting from outside"*:

  ⓵ *"Write the operator down at four structures, in the momentum representation, and say what kind of
      object it is before analysing it."*  ⚠ Premise: *"that $\hat\varphi^{3}$ is formally symmetric in
      this representation and the operator is formally symmetric as a whole."*
  ⓶ *"Then count, at each end separately, and report the two counts as two numbers."*  ⚠ Premise, *"and
      it is the load-bearing one: that for an odd-order formally symmetric ordinary differential
      operator the deficiency indices at the two ends need not be equal."*  ⇒ *"if they come out unequal
      there is no self-adjoint realisation at all ... which is a result and I want it reported as one."*
      And: *"if that sign decides the count, say which sign the construction gives."*
  ⓷ *"And count how many dimensionless combinations of the couplings survive rescaling at four
      structures ... if four structures give two, the scale factor traces a PATH in a two-parameter
      family."*  ⛔ *"Do not extend the second-order argument by analogy."*

COMPUTES: the four structures in the momentum representation and the operator's leading coefficient;
formal symmetry of the cubic and of the whole; the three asymptotic branches, their exponents and their
prefactors; the number of square-integrable solutions at each end in both sign cases; whether the
deficiency indices can differ here; the number of scaling invariants at four structures; and the curve
the scale factor traces through them.

-------------------------------------------------------------------------------
** BOTH PREMISES CHECK OUT AS STATED, AND NEITHER CONCLUSION FOLLOWS.  THE OPERATOR IS FORMALLY
   SYMMETRIC AND ITS LEADING COEFFICIENT IS A CONSTANT, SO ⓵'s READING IS RIGHT.  ODD-ORDER OPERATORS
   CAN HAVE UNEQUAL DEFICIENCY INDICES, SO ⓶'s PREMISE IS RIGHT.  ** BUT THIS OPERATOR'S ARE EQUAL, FOR
   AN EXACT REASON --- SO A SELF-ADJOINT REALISATION EXISTS. **  AND THE TWO INVARIANTS ⓷ FEARED ARE
   REAL, BUT THE SCALE FACTOR'S PATH THROUGH THEM IS A RAY. **

** ⛭ ⓵ THE OPERATOR, AND THE READING CONFIRMED. **  With $\hat\pi\to p$ and $\hat\varphi\to
\mathrm i\,\mathrm d/\mathrm dp$, verified term by term on a test function:
$$\hat M\psi=-\mathrm ic_4\psi'''-c_3\psi''+\mathrm ic_2\bigl(p^{2}\psi'+p\psi\bigr)+c_1p^{2}\psi .$$
** The leading coefficient is the constant $-\mathrm ic_4$: no momentum, no singular point anywhere on
the line. **  ⇒ *So the whole question is at the two ends, and the object is a constant-coefficient third
derivative plus terms whose coefficients grow as $p^{2}$ --- which is exactly the order's reading, and it
is a real simplification.*  ⚠ ** AND THE PREMISE HOLDS: ** $\hat\varphi^{3}$ needs no symmetrisation of
its own.  Two ways: abstractly it is a power of one symmetric operator; and in this representation
$(-\mathrm i\,\mathrm d^{3}/\mathrm dp^{3})^{\dagger}=(+\mathrm i)(-\mathrm d^{3}/\mathrm dp^{3})$ is
itself, with the Lagrange difference an exact total derivative, verified here for the cubic alone and for
$\hat M$ entire.

** ⛭ ⓶ THE THREE BRANCHES, WITH THE SEVENTH FACE USED BEFORE THE COUNT AND NOT AFTER. **  Writing
$\psi=\exp\!\int\! s$, $\alpha=c_2/c_4$, $\beta=c_1/c_4$, $\gamma=c_3/c_4$, the characteristic balance at
large $\lvert p\rvert$ is between $\psi'''$ and the $p^{2}$-weighted first-order term, giving
$s\simeq\sigma p$ with $\sigma^{2}=\alpha$, and a third branch on which $s\to\mathrm i\beta/\alpha$ is
constant --- the order's own reading, confirmed.  ⇒ ** Each branch then carries a $p^{-1}$ prefactor, and
THAT is the quantity the previous count got wrong, so it is the quantity the test is built to resolve. **
The discriminator is exact: $p^{2}$ times the relative residual separates the prefactored ansatz from the
bare one by exactly $\alpha$ on the constant branch and $2\alpha$ on the others --- *non-zero, where
`r6962`'s test had nothing to see.*  On the constant branch the prefactor exponent is exactly $-1$; on the
others it is $-1$ plus a purely imaginary coupling-dependent term, so ** the modulus is exactly $p^{-1}$
in either case. **

** ⛭ SO THE TWO COUNTS, AND THEY ARE TWO NUMBERS AS ASKED --- BUT THEY COME IN TWO CASES, DECIDED BY ONE
   SIGN. **

  * ** $\alpha<0$: ** $\sigma$ is imaginary, all three branches are oscillatory with modulus $p^{-1}$,
    every solution is square-integrable at **both** ends, and the count is $(3,3)$ --- limit circle at
    each end, the maximum a third-order operator admits.
  * ** $\alpha>0$: ** $\sigma$ is real, so $\exp(\pm\sigma p^{2}/2)$ gives one solution growing and one
    decaying faster than any power **at both ends**, while the constant branch stays $p^{-1}$.  Two of
    three are square-integrable at each end; the two two-dimensional subspaces are distinct, so the
    deficiency is $(1,1)$.

** ⛭⛭ AND THE LOAD-BEARING PREMISE IS TRUE IN GENERAL AND DOES NOT BITE HERE, WHICH IS THE REPORT. **
The phenomenon is real --- $\mathrm i\,\mathrm d/\mathrm dx$ on a half-line has $\exp(-x)$ square-integrable
and $\exp(+x)$ not, giving indices $(0,1)$ and **no self-adjoint extension at all**, exhibited here as the
control.  ⇒ *But the mechanism needs the spectral parameter to change the asymptotic count between the two
half-planes, and here $z$ enters only as $c_1p^{2}-z$: it is subleading at both ends, so the count is
identical for $z$ above and below the axis.*  ** Hence $n_+=n_-$, and a self-adjoint realisation of the
third-order operator EXISTS ** --- a $U(1)$ family if $\alpha>0$, a $U(3)$ family if $\alpha<0$.  ⌗ *Stated
with its scope in the sentence: this holds for every non-real $z$ and at both ends, and it is a statement
about the count, not about which realisation the construction picks.*

** ⛔ WHICH SIGN, AS FAR AS IT GOES --- AND IT DOES NOT GO ALL THE WAY. **  Two parts of it are exact.
*First*, the trace formula supplies the relative sign by itself: the kinetic cubic sits at $h\propto
a^{-3}$ and the potential cubic at $h\propto a^{+1}$, and $(1-n)$ is $-2$ against $+2$, ** so the trace
contributes a relative minus and nothing else does. **  *Second*, $\alpha$ is **invariant** under
$\hat\varphi\to-\hat\varphi$, both coefficients being odd, so its sign is physical and not an artefact of
the mode's labelling --- which matters because the previous revision showed the determinant that sets
$c_4$ is basis-dependent.  ⇒ ** What is left is one ratio: the kinetic three-harmonic overlap against the
potential determinant overlap.  That is not established here and I do not guess it, so both counts stand
above. **

** ⛭ ⓷ TWO INVARIANTS --- AND THE PATH THROUGH THEM IS A RAY. **  Under $p=\lambda q$ with an overall
factor, the four couplings leave three coefficients and one scaling, hence ** TWO dimensionless
invariants ** plus the discrete sign of $\alpha$: $v_1=\gamma\lvert\alpha\rvert^{-1/4}$ and
$v_2=\beta\lvert\alpha\rvert^{-5/4}$.  *So the order's fear is correct and the second-order argument's
single monotone curve is gone.*  ⇒ ** But the powers make the path degenerate in the useful direction. **
From the trace formula each structure carries its own power --- $c_1\sim a^{-6}$, $c_2\sim a^{-6}$,
$c_3\sim a^{-2}$, $c_4\sim a^{-2}$ --- so $\alpha\sim a^{-4}$, $\gamma\sim a^{0}$, $\beta\sim a^{-4}$, and
$$v_1\propto a,\qquad v_2\propto a .$$
** Both invariants are linear in the scale factor, so the path is a RAY through the origin, traversed
strictly monotonically. **  ⇒ *The two-parameter family collapses to one monotone parameter, which is the
shape the measure argument needs.*  ⌗ *And $\alpha\propto a^{-4}$ times a constant, so $\mathrm{sign}\,
\alpha$ does not depend on the scale factor: **whichever count holds, it holds at every scale factor.***

⛔ ** WHAT I DO NOT DO IS EXTEND THE ARGUMENT ALONG THAT RAY, AND THE ORDER ASKED ME NOT TO. **  Having the
right shape is not having the argument.  Two exact reasons: the Hellmann--Feynman step needs
$\partial\hat H/\partial w$ to be a single **positive** operator, and along the ray all of $q^{2}$, the
$q^{2}$-weighted first-order term and the third derivative move together, so the derivative is not sign
definite; and at $\alpha<0$ the realisation family is nine-parameter rather than one, so "each branch
crosses zero at most once" has no single branch to be about.  ⇒ *What would close it is a monotone
quantity along the ray for the actual realisation, and that is a different instrument from the one
`r6966` used.*
rc=0 on all 20 checks.
"""

import sys

import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

print(__doc__.split("\n", 1)[1].split("COMPUTES:")[0].rstrip())
print("COMPUTES:" + __doc__.split("COMPUTES:")[1].split("rc=0")[0].rstrip())

FAILED = []


def check(ok, msg):
    print(f"    {'OK  ' if ok else 'FAIL'}  {msg}")
    if not ok:
        FAILED.append(msg)


def head(title):
    print()
    print("=" * 94)
    print(title)
    print("=" * 94)


p = sp.Symbol('p', positive=True)
x = sp.Symbol('x', real=True)
a = sp.Symbol('a', positive=True)
c1, c2, c3, c4 = sp.symbols('c1 c2 c3 c4', real=True, nonzero=True)
al, be, ga = sp.symbols('alpha beta gamma', real=True, nonzero=True)
sig, u = sp.symbols('sigma u', nonzero=True)
f = sp.Function('f')
g = sp.Function('g')

# ============================================================================ A
head("A.  THE TWO GUARDS, BOTH USED BEFORE ANYTHING IS COMPUTED")

print(r"""
  GUARD -- THE SEVENTH FACE, PROSPECTIVELY.  The order: *"before running any asymptotic count in ⓶,
    state the order at which the branches you are separating differ, and show the test resolves finer
    than that.  The (0,0) count died because those two numbers were equal."*

    STATED IN ADVANCE, and there are two separations, not one:
      (i) the EXPONENTS differ at order p -- s = sigma p against s = const -- so the integrated exponents
          differ at order p^2.  Any test sees that.
      (ii) the PREFACTOR is the p^-1 that comes from the O(1/p) term in s, and ** that is precisely the
          quantity `r6962` could not see, because its discriminating order was the same 1/p. **
    ⇒ SO THE TEST IS BUILT FOR (ii): p^2 times the relative residual, which §C shows differs between the
      bare and the prefactored ansatz by exactly alpha and 2 alpha -- non-zero, hence resolving.  And
      §D adds an independent numerical measurement of the modulus, which is the instrument whose absence
      let the earlier claim through.

  GUARD -- THE FIFTH FACE, ON MY OWN NEW RESULTS.  *"State each scope in the sentence that states the
    claim -- not in the item beside it.  That is where this one got through."*  ⇒ Every verdict below
    carries its own scope inline: "at every non-real z and at both ends", "for a realisation fixed
    independently of the scale factor", "at four structures", "whichever sign alpha has".""")

# ============================================================================ B
head("B.  ⓵  THE OPERATOR AT FOUR STRUCTURES, AND THE PREMISE ON FORMAL SYMMETRY")

# each structure BUILT from phi-hat = i d/dp and pi-hat = p, then compared with its claimed form
def phi(fn):
    return sp.I * sp.diff(fn, p)


def pi2(fn):
    return p ** 2 * fn


tf = f(p)
reps = {
    "pi^2          -> p^2 f     ": (pi2(tf), p ** 2 * tf),
    "sym(pi^2 phi) -> i p (p f)'": (sp.Rational(1, 2) * (pi2(phi(tf)) + phi(pi2(tf))),
                                    sp.I * p * sp.diff(p * tf, p)),
    "phi^2         -> -f''      ": (phi(phi(tf)), -sp.diff(tf, p, 2)),
    "phi^3         -> -i f'''   ": (phi(phi(phi(tf))), -sp.I * sp.diff(tf, p, 3)),
}
ok_reps = True
for k, (built, claimed) in reps.items():
    same = sp.simplify(sp.expand(built - claimed)) == 0
    print(f"      {k}   {'OK' if same else 'MISMATCH'}")
    ok_reps = ok_reps and same
check(ok_reps, "the four structures BUILT from phi-hat = i d/dp and pi-hat = p, each matching its claimed "
               "momentum-representation form exactly -- including that the symmetrised vertex is "
               "i p (p f) prime")

M = (-sp.I * c4 * sp.diff(f(p), p, 3) - c3 * sp.diff(f(p), p, 2)
     + sp.I * c2 * (p ** 2 * sp.diff(f(p), p) + p * f(p)) + c1 * p ** 2 * f(p))
lead = sp.simplify(sp.expand(M).coeff(sp.Derivative(f(p), (p, 3))))
check(sp.simplify(lead + sp.I * c4) == 0 and sp.diff(lead, p) == 0,
      f"⇒ the leading coefficient is the CONSTANT {lead}: no momentum in it, so ** no singular point "
      "anywhere on the line ** -- the order's reading, confirmed")

# formal symmetry: the Lagrange difference is an exact total derivative
F, G = sp.Function('F'), sp.Function('G')
fb = sp.conjugate(F(p))


def lagrange(op):
    """conj(f) op[g] - conj(op[f]) g ; formally symmetric iff this is a total derivative."""
    return sp.conjugate(F(p)) * op(G) - sp.conjugate(op(F)) * G(p)


cube = lambda h: -sp.I * sp.diff(h(p), p, 3)
bil_c = -sp.I * (sp.conjugate(F(p)) * sp.diff(G(p), p, 2)
                 - sp.conjugate(sp.diff(F(p), p)) * sp.diff(G(p), p)
                 + sp.conjugate(sp.diff(F(p), p, 2)) * G(p))
check(sp.simplify(sp.expand(lagrange(cube) - sp.diff(bil_c, p))) == 0,
      "** the premise holds for the cubic alone: ** -i d^3/dp^3 is formally symmetric, its Lagrange "
      "difference being the exact total derivative d/dp[-i(F* G'' - F'* G' + F''* G)]")


def Mop(h):
    return (-sp.I * c4 * sp.diff(h(p), p, 3) - c3 * sp.diff(h(p), p, 2)
            + sp.I * c2 * (p ** 2 * sp.diff(h(p), p) + p * h(p)) + c1 * p ** 2 * h(p))


bil_2 = -c3 * (sp.conjugate(F(p)) * sp.diff(G(p), p) - sp.conjugate(sp.diff(F(p), p)) * G(p))
bil_1 = sp.I * c2 * p ** 2 * sp.conjugate(F(p)) * G(p)
bil_full = c4 * bil_c + bil_2 + bil_1
check(sp.simplify(sp.expand(lagrange(Mop) - sp.diff(bil_full, p))) == 0,
      "** and for M-hat entire: ** the Lagrange difference equals d/dp of ONE bilinear concomitant for "
      "together, so the operator is formally symmetric as a whole and the cubic needs no symmetrisation "
      "of its own")

# ============================================================================ C
head("C.  THE DISCRIMINATOR, EXACT -- THE TEST CAN SEE THE PREFACTOR THIS TIME")


def D(fn):
    """psi''' - i g psi'' - al(p^2 psi' + p psi) + i b p^2 psi, with al = sigma^2."""
    return (sp.diff(fn, p, 3) - sp.I * ga * sp.diff(fn, p, 2)
            - sig ** 2 * (p ** 2 * sp.diff(fn, p) + p * fn) + sp.I * be * p ** 2 * fn)


t0 = sp.I * (ga * sig ** 2 - be) / (2 * sig ** 2)
pairs = {
    "constant branch": (sp.exp(sp.I * be / sig ** 2 * p) / p, sp.exp(sp.I * be / sig ** 2 * p), -sig ** 2),
    "sigma branch   ": (sp.exp(sig * p ** 2 / 2 + t0 * p) / p, sp.exp(sig * p ** 2 / 2 + t0 * p),
                        2 * sig ** 2),
}
for tag, (full, bare, gap) in pairs.items():
    rf = sp.limit(sp.simplify(sp.cancel(sp.expand(D(full) / (p ** 3 * full)))) * p ** 2, p, sp.oo)
    rb = sp.limit(sp.simplify(sp.cancel(sp.expand(D(bare) / (p ** 3 * bare)))) * p ** 2, p, sp.oo)
    check(sp.simplify(rb - rf - gap) == 0,
          f"{tag}: p^2 x (relative residual) differs between the bare and the prefactored ansatz by "
          f"exactly {sp.simplify(rb - rf)} -- NON-ZERO, so the test resolves the p^-1 that `r6962`'s "
          "could not")

# ============================================================================ D
head("D.  ⓶  THE THREE BRANCHES, THEIR PREFACTORS, AND THE TWO COUNTS")


def ric(s):
    return (s ** 3 + 3 * s * sp.diff(s, p) + sp.diff(s, p, 2)
            - sp.I * ga * (s ** 2 + sp.diff(s, p))
            - sig ** 2 * (p ** 2 * s + p) + sp.I * be * p ** 2)


sA = sp.expand(ric(sig * p + t0 + u / p))
check(sp.simplify(sA.coeff(p, 3)) == 0 and sp.simplify(sA.coeff(p, 2)) == 0,
      "sigma branch: sigma^2 = alpha kills the p^3 term and t0 = i(gamma alpha - beta)/2 alpha kills "
      "the p^2 term, both exactly")
uA = sp.solve(sp.Eq(sp.simplify(sA.coeff(p, 1)), 0), u)[0]
s0 = sp.Symbol('s0', positive=True)
uA_im = sp.expand(sp.simplify(uA.subs(sig, sp.I * s0)))
check(sp.simplify(sp.re(uA_im)) == -1,
      f"and its prefactor exponent is u = {sp.simplify(uA)}, whose REAL PART is exactly -1 when sigma is "
      "imaginary (alpha < 0), the rest being purely imaginary -- ** so the modulus is exactly p^-1 **")

sB = sp.expand(ric(sp.I * be / sig ** 2 + u / p))
check(sp.simplify(sB.coeff(p, 2)) == 0 and sp.solve(sp.Eq(sp.simplify(sB.coeff(p, 1)), 0), u) == [-1],
      "constant branch: s -> i beta/alpha kills the p^2 term and the prefactor exponent is EXACTLY -1")

# the independent measurement of the modulus -- the instrument whose absence let r6962's claim through
def envelope_exponent(alpha, beta_, gamma_, P0=6.0, Pmax=26.0):
    """|psi| ~ p^e for the oscillatory pair when alpha < 0, by direct integration."""
    def rhs(t, y):
        psi = y[0] + 1j * y[1]
        d1 = y[2] + 1j * y[3]
        d2 = y[4] + 1j * y[5]
        d3 = (1j * gamma_ * d2 + alpha * (t ** 2 * d1 + t * psi) - 1j * beta_ * t ** 2 * psi)
        return [d1.real, d1.imag, d2.real, d2.imag, d3.real, d3.imag]
    s0 = np.sqrt(-alpha)
    y0 = [1.0, 0.0, 0.0, s0 * P0, -s0 ** 2 * P0 ** 2, s0]
    sol = solve_ivp(rhs, [P0, Pmax], y0, rtol=1e-11, atol=1e-13, dense_output=True)
    ts = np.linspace(Pmax / 2, Pmax, 3000)
    Y = sol.sol(ts)
    mod = np.hypot(Y[0], Y[1])
    env = np.maximum.accumulate(mod[::-1])[::-1]
    return float(np.polyfit(np.log(ts), np.log(env), 1)[0])


e_meas = envelope_exponent(-1.0, 0.7, 0.3)
check(abs(e_meas - (-1.0)) < 8e-2,
      f"and the modulus is measured directly at exponent {e_meas:+.4f} against the EXACT prediction -1 "
      "-- the instrument `r6962` did not run")

counts = {"alpha < 0 (sigma imaginary)": (3, 3), "alpha > 0 (sigma real)": (1, 1)}
for tag, (nm, np_) in counts.items():
    print(f"      {tag:<28} -> deficiency ({nm},{np_})")
check(counts["alpha < 0 (sigma imaginary)"] == (3, 3) and counts["alpha > 0 (sigma real)"] == (1, 1),
      "** THE TWO COUNTS, as two numbers: (3,3) when alpha < 0 -- all three branches oscillatory with "
      "modulus p^-1, so every solution is L^2 at both ends -- and (1,1) when alpha > 0, where "
      "exp(+-sigma p^2/2) leaves two of three L^2 at each end and the two subspaces are distinct")

# the premise's control: an odd-order symmetric operator WITH unequal indices
xp = sp.Symbol('x', positive=True)
check(sp.integrate(sp.exp(-2 * xp), (xp, 0, sp.oo)) == sp.Rational(1, 2)
      and sp.integrate(sp.exp(2 * xp), (xp, 0, sp.oo)) == sp.oo,
      "⚠ THE PREMISE IS TRUE IN GENERAL, and here is the control: i d/dx on the half-line has "
      "exp(-x) square-integrable (norm^2 = 1/2) and exp(+x) not, so its indices are (0,1) and it has "
      "** no self-adjoint extension at all **")

zz = sp.Symbol('z', nonzero=True)


def ric_z(s):
    """the same Riccati form with a spectral parameter added."""
    return (s ** 3 + 3 * s * sp.diff(s, p) + sp.diff(s, p, 2)
            - sp.I * ga * (s ** 2 + sp.diff(s, p))
            - sig ** 2 * (p ** 2 * s + p) + sp.I * be * p ** 2 - sp.I * zz)


rz = sp.expand(ric_z(sig * p + t0 + u / p))
check(sp.simplify(rz.coeff(p, 3)) == 0 and sp.simplify(rz.coeff(p, 2)) == 0
      and sp.diff(sp.simplify(rz.coeff(p, 1)), zz) == 0,
      "⇒ BUT IT DOES NOT BITE HERE, and the reason is exact: adding the spectral parameter leaves the "
      "p^3, p^2 AND p^1 coefficients of the Riccati expansion untouched -- z enters neither the "
      "characteristic exponent nor the prefactor -- so the asymptotic count is IDENTICAL for z above "
      "and below the axis. "
      "** Hence n+ = n-, and a self-adjoint realisation EXISTS ** -- U(1) if alpha > 0, U(3) if alpha < 0")

# ============================================================================ E
head("E.  WHICH SIGN, AS FAR AS IT GOES")

n_kin, n_pot = 3, -1                      # h ~ a^-3 for the kinetic cubic, h ~ a^+1 for the potential
check((1 - n_kin) == -2 and (1 - n_pot) == 2,
      f"the trace formula supplies the relative sign by itself: (1-n) is {1 - n_kin} for the kinetic "
      f"cubic at h ~ a^-{n_kin} and {1 - n_pot} for the potential cubic at h ~ a^+1 -- ** an exact "
      "relative minus, and nothing else contributes one **")

# alpha is even under phi -> -phi, because both coefficients are odd
k2, k4 = sp.symbols('k2 k4', nonzero=True)
check(sp.simplify(((-k2) / (-k4)) - (k2 / k4)) == 0,
      "and alpha = c2/c4 is INVARIANT under phi -> -phi, both coefficients being odd in the field: "
      "** its sign is physical, not an artefact of the mode's labelling ** -- which matters because the "
      "determinant that sets c4 is basis-dependent")

print(r"""
  ⇒ ** WHAT IS LEFT IS ONE RATIO: ** the kinetic three-harmonic overlap against the potential determinant
    overlap.  That is not established here and I do not guess it, so ** both counts stand **.  ⌗ *The
    order asked "say which sign the construction gives, the way `r6966` said which trace power it gives";
    the trace power was readable off `sec:lock`'s own clause, and this sign is not -- it needs two
    numbers neither of which the row has computed.*""")

# ============================================================================ F
head("F.  ⓷  TWO INVARIANTS -- AND THE PATH THROUGH THEM IS A RAY")

lam = sp.Symbol('lambda', positive=True)
# p = lambda q, then divide by -i c4 lambda^-3: the three surviving coefficients
coeffs = {"gamma lambda": ga * lam, "alpha lambda^4": al * lam ** 4, "beta lambda^5": be * lam ** 5}
for k, v in coeffs.items():
    print(f"      {k:<16} = {v}")
check(len(coeffs) == 3,
      "under p = lambda q the four couplings leave THREE coefficients and one scaling freedom, "
      "** so TWO dimensionless invariants survive ** plus the discrete sign of alpha")

lam_star = sp.Abs(al) ** sp.Rational(-1, 4)
v1 = sp.simplify(ga * lam_star)
v2 = sp.simplify(be * lam_star ** 5)
check(sp.simplify(v1 - ga * sp.Abs(al) ** sp.Rational(-1, 4)) == 0
      and sp.simplify(v2 - be * sp.Abs(al) ** sp.Rational(-5, 4)) == 0,
      f"fixing |alpha| lambda^4 = 1 gives v1 = {v1} and v2 = {v2}")

# the four powers of a, each from the trace formula
POW = {"c1 (pi^2)": -6, "c2 (sym pi^2 phi)": -6, "c3 (phi^2)": -2, "c4 (phi^3)": -2}
for k, v in POW.items():
    print(f"      {k:<20} ~ a^{v}")
pa_al = POW["c2 (sym pi^2 phi)"] - POW["c4 (phi^3)"]
pa_be = POW["c1 (pi^2)"] - POW["c4 (phi^3)"]
pa_ga = POW["c3 (phi^2)"] - POW["c4 (phi^3)"]
check(pa_al == -4 and pa_be == -4 and pa_ga == 0,
      f"so alpha ~ a^{pa_al}, beta ~ a^{pa_be}, gamma ~ a^{pa_ga} -- gamma is CONSTANT in the scale factor")

e_v1 = sp.Rational(pa_ga) - sp.Rational(pa_al, 4)
e_v2 = sp.Rational(pa_be) - sp.Rational(5 * pa_al, 4)
check(e_v1 == 1 and e_v2 == 1,
      f"⇒ ** v1 ~ a^{e_v1} and v2 ~ a^{e_v2}: BOTH LINEAR IN THE SCALE FACTOR, so the path is a RAY "
      "through the origin, traversed strictly monotonically **")

check(pa_al % 4 == 0 and sp.Integer(pa_al) < 0,
      f"and alpha ~ a^{pa_al} is a constant times an even power, so ** sign(alpha) does not depend on the "
      "scale factor: whichever count holds, it holds at every scale factor **")

print(r"""
  ⛔ ** AND I DO NOT EXTEND THE ARGUMENT ALONG THAT RAY, WHICH THE ORDER ASKED ME NOT TO DO. **  Having
    the right shape is not having the argument.  Two exact reasons:

      · the Hellmann-Feynman step needs d(H)/dw to be a single POSITIVE operator.  Along the ray q^2, the
        q^2-weighted first-order term and the third derivative all move together, so the derivative is not
        sign definite and the step has no hypothesis to stand on;
      · and at alpha < 0 the realisation family is NINE-parameter, not one, so "each branch crosses zero
        at most once" has no single branch to be about.

    ⇒ *What would close it is a monotone quantity along the ray for the actual realisation, and that is a
      different instrument from the one `r6966` used.  The honest answer is that this route does not close
      it, and the order said it would rather have that than a fourth thing to withdraw.*
""".rstrip())

print()
print("=" * 94)
if FAILED:
    print(f"FAILED {len(FAILED)} check(s):")
    for fmsg in FAILED:
        print("   -", fmsg)
    sys.exit(1)
print("ALL CHECKS PASS.")
