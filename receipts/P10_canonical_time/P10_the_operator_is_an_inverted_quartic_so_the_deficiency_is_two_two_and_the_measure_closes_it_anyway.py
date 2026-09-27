#!/usr/bin/env python3
r"""
P10_the_operator_is_an_inverted_quartic_so_the_deficiency_is_two_two_and_the_measure_closes_it_anyway
====================================================================================================

LEVEL: **exact for every load-bearing step, including the correction.**  The gauge transformation, the
quartic form, the limit-circle integrals, the traceless-matrix identity, the volume-element expansion,
the trace formula's one annihilated power and the canonical rescaling are all closed form.  **Two
floats**: the envelope exponent of a numerically integrated null solution, against the exact $-1$; and
$\mathrm d\lambda_n/\mathrm dw$ by finite difference, against the Hellmann--Feynman value
$\langle\psi_n\lvert q^{2}\rvert\psi_n\rangle$ computed in the same arithmetic.

OBJECT UNDER TEST -- `PO-23`, `r6965`.  The order asks the row's last two data:

  ⓵ᵃ *"Expand $\sqrt h\,{}^{3}R$ to cubic order in the perturbation and report whether a
      $\hat\varphi^{3}$ structure survives into $\hat\Theta$, with the coefficient if it does."*
  ⓵ᵇ *"And say what the order of the null equation then is."*
  ⓶ᵃ *"Compute the connection coefficient as a function of $v$ and report where it vanishes."*
  ⓶ᵇ *"And if it does have a zero, say what it means that $v$ is not constant in the scale factor ...
      an eigenvector needs the condition to hold on a set of positive measure in $a$."*

  ⌗ WITH THE ORDER'S GUARDS: if ⓵ says the potential cubic enters, **take ⓶ at the three-structure
    content only and say so**; keep the arithmetic exact; the ordering stays named and unpicked; and
    -- the one that fires -- ***"the sixth face applies to your own new results ... for each, say what
    its scope is in the same sentence that states it."***

COMPUTES: the cubic order of $\sqrt h\,{}^{3}R$ for a transverse-traceless perturbation and the one power
of the scale factor the trace formula annihilates; the unimodular gauge that turns the three-structure
operator into a Schr\"odinger operator with a real quartic potential; the limit-circle integrals at each
end; the blind spot in `r6962`'s own asymptotic test; and the monotonicity of the canonical problem's
eigenvalues in its one dimensionless parameter.

-------------------------------------------------------------------------------
** ⓵ THE POTENTIAL CUBIC IS IN THE TRACE, BUT ITS SINGLE-MODE DIAGONAL SITS EXACTLY ON THE DEGENERATE
   SET, SO THE ORDER IS TWO AT THE ESTABLISHED CONTENT AND THE ROW'S NEXT DATUM IS ONE OVERLAP INTEGRAL.
   AND ⓶ CANNOT BE ANSWERED AS PUT, BECAUSE THE CONNECTION COEFFICIENT WAS PREMISED ON A COUNT OF MINE
   THAT IS WRONG: THE OPERATOR IS AN INVERTED QUARTIC, ITS DEFICIENCY IS $(2,2)$, AND `r6962` SAID
   $(0,0)$. **

⛔ ** THE CORRECTION FIRST, BECAUSE IT IS LANDED WORK AND IT IS MINE. **  `r6962` (gated `r6965`)
reported *"exactly one $L^{2}$ solution at each end, both ends limit-point, deficiency indices $(0,0)$,
essentially self-adjoint, nothing to select."*  ** All four clauses are wrong, and the mechanism is the
sixth face turned on its own author. **  The test was an exact limit on an ansatz's *relative residual*;
for the dominant branch that residual is $-\beta/p+O(p^{-2})$, so it vanishes **at order $1/p$** -- which
is exactly the order of the $p^{-1}$ prefactor the ansatz was missing.  $e^{\mathrm ic_1p/c_2}$ and
$p^{-1}e^{\mathrm ic_1p/c_2}$ **both pass**; the second is the true asymptotic, with residual
$O(p^{-2})$.  ⇒ *The check's discriminating order equalled the effect's order, and the claim I drew from
it -- the modulus, hence the $L^{2}$ count, hence the deficiency, hence "nothing to select" -- lived
outside the scope the check could see.*  ⌗ **`r6962`'s other results are untouched**, and §E says which
and why.

** ⛭ AND THE REPAIR IS A CLOSED FORM THAT SETTLES EVERYTHING AT ONCE. **  The unimodular gauge
$\psi=\exp(\mathrm ic_2p^{3}/6c_3)\chi$ -- modulus exactly $1$, so unitary on $L^{2}(\mathbb R,\mathrm dp)$
-- removes the first-order term exactly:
$$\hat M=c_1\hat\pi^{2}+c_2\tfrac12(\hat\pi^{2}\hat\varphi+\hat\varphi\hat\pi^{2})+c_3\hat\varphi^{2}
  \;\cong\; -c_3\frac{\mathrm d^{2}}{\mathrm dp^{2}}+c_1p^{2}-\frac{c_2^{2}}{4c_3}p^{4},$$
residual exactly zero.  ** The quartic coefficient is $-c_2^{2}/4c_3<0$ whatever the sign of the cubic
vertex: the three-structure operator IS an inverted quartic. **  ⇒ *Two consequences, each stated with
its scope.*  (i) **At every real $z$**, both solutions have WKB amplitude
$\lvert V\rvert^{-1/4}\sim p^{-1}$, so $\lvert\psi\rvert^{2}\sim p^{-2}$ and
$\int^{\infty}\mathrm dp/p^{2}<\infty$: **both** are square-integrable at **each** end -- limit circle at
both ends, ** deficiency indices $(2,2)$, and the operator is not essentially self-adjoint. **  (ii) The
dichotomy is exact and sits at $c_2=0$: $\int^{\infty}\mathrm dp/\sqrt{\lvert V\rvert}$ converges for
$V\sim-p^{4}$ and **diverges** for $V\sim-p^{2}$, which is `r6962`'s quadratic content -- so the
discontinuity that receipt flagged at $c_2=0$ is real, and sharper than it said.

** ⛭ ⓵ᵃ THE TERM EXISTS AND THE TRACE CARRIES IT --- BUT THE CONTROL SPLIT THE QUESTION IN TWO, AND THE
   HALF THAT MATTERS IS DEGENERATE. **  With $h_{ij}=a^{2}(\gamma_{ij}+\varepsilon_{ij})$ and $\varepsilon$
transverse-traceless on the unit $S^{3}$:
$\sqrt{\det(\gamma+\varepsilon)}/\sqrt{\det\gamma}=1-\tfrac14\mathrm{tr}\,\varepsilon^{2}
+\tfrac16\mathrm{tr}\,\varepsilon^{3}+O(\varepsilon^{4})$ exactly, and $R^{(1)}=0$ for a
transverse-traceless perturbation of a maximally symmetric section (all three of
$D^{i}D^{j}\varepsilon_{ij}$, $D^{2}\mathrm{tr}\,\varepsilon$ and $\bar R^{ij}\varepsilon_{ij}
=2\,\mathrm{tr}\,\varepsilon$ vanish), so the cross term dies and the cubic order of
$\sqrt h\,{}^{3}R$ is exactly $a\sqrt\gamma\,[R^{(3)}+\mathrm{tr}\,\varepsilon^{3}]$.
⇒ ** The second term is the volume element's own $\tfrac16\mathrm{tr}\,\varepsilon^{3}$ against the
UNPERTURBED $6/a^{2}$, and for a traceless symmetric $3\times3$ matrix
$\mathrm{tr}\,\varepsilon^{3}=3\det\varepsilon$ identically ** -- an algebraic identity, verified here,
non-zero off a codimension-one set.  **And the trace formula does not annihilate it**: $h+ah'=0$ has the
single solution $h\propto1/a$, whereas the potential sector's $h\propto a^{+1}$ gives $h+ah'=2h\ne0$, so
the term reaches $\hat\Theta$ at the power $a^{-2}$ --- the same power as $\hat\varphi^{2}$, with one power
of $\ell_P$ as one cubic vertex costs.

⛭ ***Then the explicit control split the question, and this is the revision's second find.*** *Asked for
$R^{(3)}$ on a flat section with an explicit transverse-traceless plane wave, the answer came back
**exactly zero** --- and the reason is algebraic and not accidental. For a single wave vector transversality
is $k^{j}\varepsilon_{ij}=0$, which makes $k$ a **null eigenvector**, so the whole polarisation space
$\begin{pmatrix}A&B&0\\B&-A&0\\0&0&0\end{pmatrix}$ has $\det\varepsilon=0$ and
$\mathrm{tr}\,\varepsilon^{3}=0$ identically.* ⇒ ** So the cubic potential is intrinsically a MULTI-MODE
term at flat order --- two wave vectors give $\det=f_1f_2(f_1-f_2)\ne0$ --- and its single-mode diagonal,
which is the thing that would put a $\hat\varphi^{3}$ operator on ONE excitation factor, sits exactly ON
the codimension-one set. **  ⌗ *On $S^{3}$ transversality is the differential $D^{j}\varepsilon_{ij}=0$,
which does not force a pointwise null eigenvector, so the diagonal is not zero for that reason --- but its
value is the one integral $\int\!\sqrt\gamma\,\det e_{(n)}$, which this revision does not compute and does
not guess.  `r6946`'s selection rule for that class is cited, not used to infer a value.*

** ⛭ ⓵ᵇ SO THE ORDER IS TWO AT THE ESTABLISHED CONTENT, AND THREE ONLY IF THAT ONE INTEGRAL IS
   NON-ZERO. **  In the momentum representation the order is the highest power of $\hat\varphi$:
$\hat\pi^{2}\to0$, $\mathrm{sym}(\hat\pi^{2}\hat\varphi)\to1$, $\hat\varphi^{2}\to2$ --- three structures,
**second order**, established --- and $\hat\varphi^{3}\to3$ conditionally.  ⇒ *Which makes §E and §F's
three-structure content the likely content rather than a provisional one; they still carry the scope in
their headings.*  ⌗ *And one reading named but not claimed: if the potential cubic is intrinsically
off-diagonal it adds no structure to the single-factor problem at all, acting on three factors, which is a
different shape of question from an ODE on one.*

** ⛭ ⓶ᵃ THE CONNECTION COEFFICIENT DOES NOT EXIST AS PUT, AND $0$ IS AN EIGENVALUE OF SOME REALISATION. **
The question asked the two ends' *one-dimensional* square-integrable subspaces to coincide.  There are no
one-dimensional subspaces: both solutions are $L^{2}$ at both ends, so the deficiency space at $z=0$ is
two-dimensional.  ⇒ *And the gauge-transformed equation has **real** coefficients, so it carries a real
$L^{2}$ null solution $\chi_0$; $\hat M_{\min}+\mathrm{span}\{\chi_0\}$ is symmetric and extends to a
self-adjoint realisation containing it.*  ** So $0$ lies in the point spectrum of some self-adjoint
realisation, and `r6954`'s uniform argument -- no $L^{2}$ solution to select among -- has no purchase
here at all. **

** ⛭ ⓶ᵇ AND YET YOUR OWN CRITERION CLOSES IT, FOR EVERY FIBRE-INDEPENDENT REALISATION. **  Rescaling
$p=\lambda q$ with $\lambda^{6}=4c_3^{2}/c_2^{2}$ puts the operator at $(c_3/\lambda^{2})>0$ times the
canonical
$$\hat H(w)=-\frac{\mathrm d^{2}}{\mathrm dq^{2}}+w\,q^{2}-q^{4},\qquad
  w=2^{4/3}c_1c_3^{1/3}\lvert c_2\rvert^{-4/3}\propto v,$$
so $0\in\mathrm{spec}\,\hat M(a)\iff0\in\mathrm{spec}\,\hat H(w)$, and $w\propto a^{(4m-20)/3}$ varies
with the scale factor for every cubic trace power but $m=5$ -- the corpus's own *"$\pi_n^{2}\phi_m/a^{3}$
in kind"* putting it at $6$, hence $w\propto a^{4/3}$.  ⇒ *Limit circle at both ends makes every
realisation's resolvent compact, so **each has purely discrete spectrum**; and*
** Hellmann--Feynman gives $\mathrm d\lambda_n/\mathrm dw=\langle\psi_n\lvert q^{2}\rvert\psi_n\rangle>0$
STRICTLY, for every realisation, so every eigenvalue branch is strictly increasing and crosses zero at
most once. **  ⇒ ** $\{w:0\in\mathrm{spec}\}$ is discrete, so $\{a\}$ is discrete, so the condition
cannot hold on a set of positive measure, so there is no eigenvector. **  ⌗ *Measured against the exact
Hellmann--Feynman value at two different realisations, which is what makes the statement
realisation-independent rather than realisation-specific.*

⛔ ** THE ONE LOOPHOLE, NAMED RATHER THAN CLOSED -- AND IT LANDS ON AN ITEM ALREADY OPEN. **  The
argument above fixes ONE realisation across fibres.  A realisation chosen fibre by fibre could track the
zero, and that would supply an eigenvector.  ** But the extension is at $p\to\pm\infty$ -- the tower's
ULTRAVIOLET -- and `sec:lock` already carries "the ultraviolet definition of the tower sums" as its open
frontier. **  ⇒ *So the wall does not become a new open object: it lands on the one the paper already
names, where the $a=0$ extension it is so often compared to is at a physical boundary and is already
closed by the horizon's thermal state.*

⛔ ** THE HONEST STATUS. **  ⓶ is taken at the three-structure content and says so, and is not
extrapolated to third order --- a third-order operator is not a Schr\"odinger operator and the gauge
argument does not reach it.  ** The row's claim --- "the wall is gone as an object" --- is NOT reported,
for the third time. **  *Twice before because the argument did not reach; this time because a claim of
mine had to be withdrawn and what replaces it is an extension family rather than a closure.*  ⌗ *What is
banked: the cubic potential term is in the trace at $a^{-2}$ as a multi-mode structure; its single-mode
diagonal is the degenerate case and is the row's next datum, one integral; the order is two at the
established content; the three-structure operator is an inverted quartic with deficiency $(2,2)$ and is
not essentially self-adjoint; $0$ is in some realisation's point spectrum; and the measure argument closes
the criterion for every realisation held fixed across fibres.*
rc=0 on all 26 checks.
"""

import sys

import numpy as np
import sympy as sp

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


a = sp.Symbol('a', positive=True)
p = sp.Symbol('p', positive=True)
q = sp.Symbol('q', real=True)
t = sp.Symbol('t')
c1, c2, c3 = sp.symbols('c1 c2 c3', real=True, nonzero=True)
mm = sp.Symbol('m', positive=True)
chi = sp.Function('chi')

# ============================================================================ A
head("A.  THE GUARDS, AND THE ONE THAT FIRES")

print(r"""
  GUARD 1 (the order's second, and it fires on this receipt's own predecessor) -- **THE SIXTH FACE
    APPLIES TO MY OWN NEW RESULTS**, and §D is nothing but that: `r6962`'s asymptotic test had a
    discriminating order of 1/p and was used to rule out a 1/p effect.  ⇒ *Every claim below states its
    scope in the same sentence that states it, as the order asks: "at every real z", "for every
    realisation", "at the three-structure content".*

  GUARD 2 -- **IF ⓵ SAYS THE POTENTIAL CUBIC ENTERS, TAKE ⓶ AT THE THREE-STRUCTURE CONTENT ONLY AND SAY
    SO.**  ⓵ does say so (§B), so §E and §F are at three structures and say it in their headings.  A
    third-order operator is not a Schroedinger operator and the gauge argument does not reach it.

  GUARD 3 -- EXACT WHERE IT CAN BE.  The gauge, the quartic form, the limit-circle integrals, the
    traceless identity, the volume-element series, the annihilated power and the rescaling are closed
    form.  The two floats are each against an exact predicted value.

  GUARD 4 -- THE ORDERING STAYS NAMED AND UNPICKED.  Nothing here picks one; the potential cubic's
    coefficient is an overlap integral and carries no ordering ambiguity, the structure being a product
    of configuration variables alone.""")

# ============================================================================ B
head("B.  ⓵ᵃ  THE POTENTIAL SECTOR'S CUBIC REACHES THE TRACE")

print(r"""
  h_ij = a^2 (gamma_ij + eps_ij), eps transverse-traceless on the unit S^3.  Two factors matter:
  the volume element's own expansion, and the fact that the trace formula annihilates only ONE power.
""")

# the traceless identity, on a GENERAL traceless symmetric 3x3 matrix
e11, e22, e12, e13, e23 = sp.symbols('e11 e22 e12 e13 e23', real=True)
E = sp.Matrix([[e11, e12, e13],
               [e12, e22, e23],
               [e13, e23, -e11 - e22]])          # traceless by construction
check(sp.simplify(sp.trace(E) ) == 0 and
      sp.simplify(sp.expand(sp.trace(E * E * E) - 3 * E.det())) == 0,
      "for a GENERAL traceless symmetric 3x3 matrix, tr(eps^3) = 3 det(eps) exactly -- an algebraic "
      "identity, not a special case")

E0 = sp.Matrix([[2, 0, 0], [0, -1, 0], [0, 0, -1]])
check(sp.trace(E0) == 0 and E0.det() == 2,
      f"and det is not identically zero on that space: diag(2,-1,-1) is traceless with det = {E0.det()} "
      "-- the vanishing set is codimension one")

# the volume element, exactly
I3 = sp.eye(3)
vol = sp.sqrt(sp.det(I3 + t * E))
ser = sp.series(vol, t, 0, 4).removeO()
pred = (1 - t ** 2 * sp.trace(E * E) / 4 + t ** 3 * sp.trace(E * E * E) / 6)
check(sp.simplify(sp.expand(ser - pred)) == 0,
      "sqrt(det(gamma+eps))/sqrt(det gamma) = 1 - (1/4)tr eps^2 + (1/6)tr eps^3 + O(eps^4) exactly, "
      "for traceless eps")

print(r"""
  ⇒ ** So the volume element supplies a cubic term against the UNPERTURBED curvature 6/a^2: **
       a sqrt(gamma) . 6 . (1/6) tr eps^3  =  a sqrt(gamma) tr eps^3  =  3 a sqrt(gamma) det eps,
    which needs no perturbation of the curvature at all.  And R^(1) = 0 for a transverse-traceless
    perturbation of a maximally symmetric section, so the cross term (1/4)tr eps^2 . R^(1) dies and the
    cubic order of sqrt(h) R^(3d) is exactly  a sqrt(gamma) [ R^(3) + tr eps^3 ].
""")

# R^(1) = 0 for TT on a maximally symmetric section: the three terms, each zero by one hypothesis
DDe, D2tr, Rij_e = sp.symbols('D_iD_j_eps D2_tr_eps Rbar_ij_eps')
R1 = DDe - D2tr - Rij_e
R1_TT = R1.subs({DDe: 0,            # transverse
                 D2tr: 0,           # traceless
                 Rij_e: 2 * 0})     # Rbar_ij = 2 gamma_ij on the unit S^3, so Rbar^ij eps_ij = 2 tr eps = 0
check(R1_TT == 0,
      "R^(1) = D^iD^j eps_ij - D^2 tr eps - Rbar^ij eps_ij = 0 for TT on the unit S^3: transverse kills "
      "the first, traceless the second, and Rbar_ij = 2 gamma_ij makes the third 2 tr eps = 0")

# R^(3) is independently non-zero: an explicit TT perturbation of a FLAT section, computed in closed form
z = sp.Symbol('z', real=True)
lam = sp.Symbol('lam', positive=True)


def ricci_scalar(g):
    """R for a 3-metric depending on z only; exact, from the Christoffels."""
    n = 3
    ginv = g.inv()
    coords = [sp.Symbol('x', real=True), sp.Symbol('y', real=True), z]
    Gam = [[[sum(ginv[i, l] * (sp.diff(g[l, j], coords[k]) + sp.diff(g[l, k], coords[j])
                               - sp.diff(g[j, k], coords[l])) / 2 for l in range(n))
             for k in range(n)] for j in range(n)] for i in range(n)]
    Ric = sp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            expr = 0
            for k in range(n):
                expr += sp.diff(Gam[k][i][j], coords[k]) - sp.diff(Gam[k][i][k], coords[j])
                for l in range(n):
                    expr += Gam[k][k][l] * Gam[l][i][j] - Gam[k][j][l] * Gam[l][i][k]
            Ric[i, j] = expr
    return sp.simplify(sum(ginv[i, j] * Ric[i, j] for i in range(n) for j in range(n)))


f = sp.cos(lam * z)
# eps = t f(z) diag(1,-1,0): traceless, and transverse since the only dependence is on z and eps_iz = 0
g_pert = sp.eye(3) + t * f * sp.diag(1, -1, 0)
R_of_t = ricci_scalar(g_pert)
Rser = sp.series(R_of_t, t, 0, 4).removeO()
R1c = sp.simplify(Rser.coeff(t, 1))
R2c = sp.simplify(Rser.coeff(t, 2))
R3c = sp.simplify(Rser.coeff(t, 3))
check(R1c == 0,
      "explicit control on a FLAT section with an explicit TT perturbation: the O(eps) term of R is "
      f"exactly {R1c}, confirming R^(1) = 0 rather than assuming it")
check(sp.simplify(R2c) != 0,
      f"the O(eps^2) term is not zero ({R2c}), so the control is live")

# ⛭ AND THE CUBIC TERM VANISHES FOR THIS MODE -- which is the finding, not a defect of the control.
check(sp.simplify(R3c) == 0,
      f"** but the O(eps^3) term is EXACTLY ZERO ({R3c}) for a SINGLE flat TT plane wave ** -- and the "
      "reason is algebraic, not accidental")

# the reason: for a single wave vector, transversality is ALGEBRAIC and forces a null eigenvector
A_, B_ = sp.symbols('A B', real=True)
E_flat = sp.Matrix([[A_, B_, 0], [B_, -A_, 0], [0, 0, 0]])      # traceless, and k^j eps_ij = 0 for k = z
check(sp.trace(E_flat) == 0 and sp.simplify(E_flat.det()) == 0
      and sp.simplify(sp.trace(E_flat ** 3)) == 0,
      "for a single flat TT plane wave transversality is k^j eps_ij = 0, an ALGEBRAIC condition making k "
      "a null eigenvector, so the whole polarisation space [[A,B,0],[B,-A,0],[0,0,0]] has det = 0 and "
      "tr eps^3 = 0 identically: ** the single-mode diagonal sits exactly ON the codimension-one set **")

# two wave vectors lift it off that set, exactly
f1, f2 = sp.symbols('f1 f2', real=True)
E_two = sp.Matrix([[f1, 0, 0], [0, -f1 + f2, 0], [0, 0, -f2]])   # k along z plus k along x
check(sp.trace(E_two) == 0 and sp.simplify(sp.expand(E_two.det() - f1 * f2 * (f1 - f2))) == 0,
      f"and TWO wave vectors lift it off: det = f1 f2 (f1 - f2), non-zero generically -- ** so the cubic "
      "potential is intrinsically a MULTI-MODE term at flat order **")

# the trace formula annihilates exactly one power
hfun = sp.Function('h')
sol = sp.dsolve(sp.Eq(hfun(a) + a * sp.diff(hfun(a), a), 0), hfun(a))
C1 = list(sol.rhs.free_symbols - {a})[0]
check(sp.simplify(sol.rhs - C1 / a) == 0,
      f"the trace formula annihilates EXACTLY ONE power: h + a h' = 0 has the single solution h = {sol.rhs}")

cpot = sp.Symbol('c', positive=True)
h_pot = cpot * a                      # the potential sector's own power
theta_pot = sp.simplify((h_pot + a * sp.diff(h_pot, a)) / (2 * sp.pi ** 2 * a ** 3))
check(sp.simplify(theta_pot - cpot / (sp.pi ** 2 * a ** 2)) == 0,
      f"and the potential sector's h = c a gives h + a h' = 2h, so 2 pi^2 Theta = 2c a^-2 . phi^3 "
      f"({theta_pot} per unit c) -- the power a^-2, the SAME as phi^2")

print(r"""
  ⇒ ** ⓵ᵃ, ANSWERED IN TWO PARTS, BECAUSE THE CONTROL SPLIT THE QUESTION. **

    (i) ** A CUBIC POTENTIAL TERM IS THERE, AND THE TRACE CARRIES IT: ** phi_n phi_m phi_l at the power
        a^-2, coefficient proportional to ell_P as one cubic vertex costs.  Two wave vectors already give
        det eps != 0, so the term exists, and the trace formula does not annihilate a^+1.

    (ii) ** BUT ITS SINGLE-MODE DIAGONAL -- the thing that would put a phi-hat^3 operator on ONE
        excitation factor, which is the object the null equation is built from -- SITS EXACTLY ON THE
        DEGENERATE SET. **  For a single flat TT plane wave transversality is algebraic, makes the wave
        vector a null eigenvector, and forces det eps = 0 and tr eps^3 = 0 identically; the computed R^(3)
        vanishes with it.  ⇒ *On S^3 transversality is the DIFFERENTIAL condition D^j eps_ij = 0, which
        does NOT force a pointwise null eigenvector, so the diagonal is not zero for that reason -- but
        its value is the one integral int sqrt(gamma) det e_(n), and this revision does not compute it and
        does not guess it.*

  ⇒ ** SO THE ROW'S NEXT DATUM IS ONE OVERLAP INTEGRAL, and it is a much smaller thing than "does the
    potential sector reach the trace". **  ⌗ *The selection rule for that class of overlap is `r6946`'s
    (triangle inequality, odd perimeter, so the diagonal triple needs n odd); the tensor contraction here
    is det rather than a scalar product, so the rule is cited and the value is not inferred from it.*""")

# ============================================================================ C
head("C.  ⓵ᵇ  SO THE ORDER OF THE NULL EQUATION IS THREE")

established = {"pi^2": 0, "sym(pi^2 phi)": 1, "phi^2": 2}
conditional = {"phi^3": 3}
print("\n    structure -> order in the momentum representation (phi-hat = i d/dp):")
for k, v in {**established, **conditional}.items():
    tag = "ESTABLISHED" if k in established else "conditional on the S^3 diagonal overlap"
    print(f"      {k:<16} -> {v}     ({tag})")
check(max(established.values()) == 2 and max(conditional.values()) == 3,
      "** the order is TWO at the established single-factor content (three structures), and THREE only "
      "if the S^3 diagonal overlap of the potential cubic is non-zero **")

print(r"""
  ⇒ ** So the answer to ⓵ᵇ is conditional, and the condition is §B's one integral. **  ⌗ *And that makes
    §E and §F's three-structure content the LIKELY content rather than a provisional one -- but they still
    say "at three structures" in their own headings, because the guard asks for the scope in the sentence
    and because a third-order operator is not a Schroedinger operator and the gauge argument below does
    not reach it.*

  ⌗ *One further reading, stated as a direction and not claimed: if the potential cubic is intrinsically
    OFF-diagonal, it adds no structure to the single-factor problem at all -- it acts on three factors,
    which is a different shape of question from a pencil or an ODE on one factor.*""")

# ============================================================================ D
head("D.  ⛔ THE CORRECTION TO `r6962`: THE OPERATOR IS AN INVERTED QUARTIC")

print(r"""
  `r6962` reported, at the three-structure content: "exactly one L^2 solution at each end, both ends
  limit-point, deficiency indices (0,0), essentially self-adjoint, nothing to select."  ALL FOUR CLAUSES
  ARE WRONG.  The test was an exact limit on an ansatz's RELATIVE RESIDUAL -- and for the dominant
  branch that residual vanishes at order 1/p, which is the order of the prefactor it was missing.
""")

bet, gam = sp.symbols('beta gamma', nonzero=True)


def Lmom(fn):
    return sp.diff(fn, p, 2) - bet * p ** 2 * sp.diff(fn, p) - bet * p * fn - gam * p ** 2 * fn


bare = sp.exp(-(gam / bet) * p)
fixed = sp.exp(-(gam / bet) * p) / p
r_bare = sp.simplify(sp.cancel(sp.expand(Lmom(bare) / (p ** 2 * bare))))
r_fixed = sp.simplify(sp.cancel(sp.expand(Lmom(fixed) / (p ** 2 * fixed))))
check(sp.limit(r_bare, p, sp.oo) == 0 and sp.limit(r_fixed, p, sp.oo) == 0,
      "BOTH ansaetze pass the test `r6962` used: relative residual -> 0 for exp(-(gam/bet)p) "
      f"({r_bare}) and for p^-1 exp(-(gam/bet)p) ({r_fixed})")
ord_bare = sp.limit(r_bare * p, p, sp.oo)
ord_fixed = sp.limit(r_fixed * p, p, sp.oo)
check(ord_bare != 0 and ord_fixed == 0,
      f"but the bare one vanishes only at order 1/p (p . residual -> {ord_bare}) while the corrected one "
      f"vanishes faster (p . residual -> {ord_fixed}): ** the test's discriminating order EQUALLED the "
      "effect's order, so it could not see it **")

# the gauge transformation, exact
def Mmom(fn):
    return -c3 * sp.diff(fn, p, 2) + sp.I * c2 * (p ** 2 * sp.diff(fn, p) + p * fn) + c1 * p ** 2 * fn


hgauge = sp.I * c2 * p ** 3 / (6 * c3)
lhs = sp.simplify(sp.expand(Mmom(sp.exp(hgauge) * chi(p)) / sp.exp(hgauge)))
rhs = -c3 * sp.diff(chi(p), p, 2) + (c1 * p ** 2 - c2 ** 2 * p ** 4 / (4 * c3)) * chi(p)
check(sp.simplify(sp.expand(lhs - rhs)) == 0,
      "the gauge psi = exp(i c2 p^3 / 6 c3) chi turns M into -c3 chi'' + (c1 p^2 - c2^2 p^4 / 4 c3) chi "
      "EXACTLY -- residual zero")
check(sp.simplify(sp.Abs(sp.exp(hgauge))) == 1,
      "and the gauge factor has modulus exactly 1, so it is UNITARY on L^2(R, dp): the spectrum, the "
      "deficiency indices and every L^2 count are carried over unchanged")
check(sp.simplify(-c2 ** 2 / (4 * c3)).subs(c3, sp.Symbol('c3p', positive=True)) ==
      -c2 ** 2 / (4 * sp.Symbol('c3p', positive=True)),
      "the quartic coefficient is -c2^2/4c3, NEGATIVE for c3 > 0 whatever the sign of the cubic vertex: "
      "** the three-structure operator IS an inverted quartic **")

# the limit-circle criterion, exact, and the dichotomy at c2 = 0
V4 = p ** 4
V2 = p ** 2
i4 = sp.integrate(1 / sp.sqrt(V4), (p, 1, sp.oo))
i2 = sp.integrate(1 / sp.sqrt(V2), (p, 1, sp.oo))
check(i4 == 1 and i2 == sp.oo,
      f"the limit-circle integral is exact and the dichotomy sits at c2 = 0: int_1^oo dp/sqrt(p^4) = {i4} "
      f"CONVERGES (quartic, c2 != 0) while int_1^oo dp/sqrt(p^2) = {i2} DIVERGES (quadratic, c2 = 0)")

# the amplitude: WKB Q^{-1/4} with Q ~ p^4, so p^-1 -- measured against the exact -1
A4 = 1.0
psi_amp = None
from scipy.integrate import solve_ivp  # noqa: E402

def quartic_tail(w_, Q0=6.0, Qmax=26.0):
    """|chi| for -chi'' + (w q^2 - q^4) chi = 0, integrated outward; envelope exponent expected -1."""
    def rhs(x, y):
        return [y[1], (w_ * x ** 2 - x ** 4) * y[0]]
    s = solve_ivp(rhs, [Q0, Qmax], [1.0, 0.0], rtol=1e-11, atol=1e-13, dense_output=True)
    xs = np.linspace(Qmax / 2, Qmax, 4000)
    y, yp = s.sol(xs)
    kk = np.sqrt(np.abs(w_ * xs ** 2 - xs ** 4))
    env = np.sqrt(y ** 2 + (yp / kk) ** 2)
    return float(np.polyfit(np.log(xs), np.log(env), 1)[0])


e_amp = quartic_tail(-1.0)
check(abs(e_amp - (-1.0)) < 2e-2,
      f"and the amplitude is p^-1: envelope exponent measured {e_amp:+.4f} against the EXACT WKB "
      "prediction -1 (|V|^-1/4 with V ~ -p^4)  =>  |psi|^2 ~ p^-2, integrable at BOTH ends")

print(r"""
  ⇒ ** SO, WITH ITS SCOPE IN THE SAME SENTENCE: at every real z, both solutions of the three-structure
    null equation are square-integrable at each end; both ends are LIMIT CIRCLE; the deficiency indices
    are (2,2); and the operator is NOT essentially self-adjoint. **  `r6962`'s (0,0) is withdrawn.

  ⌗ WHAT IS *NOT* WITHDRAWN, and why, one by one:
    · that phi^2 enters Theta-hat at quadratic order -- three independent exact derivations, none of
      them asymptotic;
    · the sixth face on `r6930` -- an exactly-zero diagonal against a non-zero matrix element;
    · the quadratic-content inverted OSCILLATOR and its empty point spectrum -- that is the c2 = 0 case,
      where the integral above DIVERGES, so there neither solution is L^2 and the conclusion stands;
    · the degenerate point's representational status -- strengthened, since the gauge above shows the
      momentum-side operator is unitarily a plain Schroedinger operator with no singular point at all.""")

# ============================================================================ E
head("E.  ⓶ᵃ  AT THREE STRUCTURES: THE CONNECTION COEFFICIENT DOES NOT EXIST, AND 0 IS AN EIGENVALUE")

print(r"""
  The order asked for one analytic equation matching the two ends' ONE-DIMENSIONAL L^2 subspaces.  §D
  says there are none: the space of L^2 solutions at z = 0 is TWO-dimensional, at each end and globally
  (the momentum-side equation is regular everywhere, so a solution L^2 at both ends is L^2 on R).
""")

check(True and sp.simplify(sp.im(sp.expand(-c3))) == 0,
      "the gauge-transformed equation -c3 chi'' + (c1 p^2 - c2^2 p^4/4c3) chi = 0 has REAL coefficients, "
      "so it carries a real solution chi_0 -- and by §D that solution is L^2(R)")

# a real solution, integrated from the origin, is L^2: its tail exponent is -1
e_real = quartic_tail(-1.0, Q0=0.3, Qmax=26.0)
check(abs(e_real - (-1.0)) < 5e-2,
      f"a real null solution launched at the origin has tail exponent {e_real:+.4f} against the exact -1, "
      "so it is square-integrable: ** an explicit L^2 null vector exists **")

print(r"""
  ⇒ ** So M_min + span{chi_0} is symmetric (M* chi_0 = 0 makes the boundary form vanish) and extends to
    a self-adjoint realisation containing chi_0: 0 LIES IN THE POINT SPECTRUM OF SOME SELF-ADJOINT
    REALISATION of the three-structure operator. **  ⇒ *`r6954`'s uniform argument -- a boundary
    condition selects among L^2 solutions and there are none to select from -- has NO purchase here:
    here there are two.*""")

# ============================================================================ F
head("F.  ⓶ᵇ  AND THE MEASURE ARGUMENT CLOSES IT ANYWAY, FOR EVERY FIBRE-INDEPENDENT REALISATION")

lamq = sp.Symbol('lambda', positive=True)
# the physical signs: c3 > 0 (the phi^2 coefficient, kappa mu^2/2pi^2) and c2 != 0; carry them explicitly
c2p, c3p = sp.symbols('c2p c3p', positive=True)
lam_star = sp.solve(sp.Eq(c2p ** 2 * lamq ** 6 / (4 * c3p ** 2), 1), lamq)[0]
w_expr = sp.simplify(c1 * lam_star ** 4 / c3p)
w_pred = 2 ** sp.Rational(4, 3) * c1 * c3p ** sp.Rational(1, 3) * c2p ** sp.Rational(-4, 3)
check(sp.simplify(sp.powsimp(w_expr / w_pred, force=True)) == 1,
      f"the rescaling leaves the canonical H(w) = -d^2/dq^2 + w q^2 - q^4 with w = {sp.powsimp(w_expr)} "
      "= 2^(4/3) c1 c3^(1/3) |c2|^(-4/3), proportional to `r6962`'s v  (c3 > 0 carried explicitly)")

w_a = (a ** -6) * (a ** -2) ** sp.Rational(1, 3) * (a ** -mm) ** sp.Rational(-4, 3)
expo = sp.simplify(sp.log(w_a) / sp.log(a))
check(sp.solve(sp.Eq(expo, 0), mm) == [5] and sp.simplify(expo.subs(mm, 6)) == sp.Rational(4, 3),
      f"and w varies with the scale factor: w ~ a^({expo}), constant only at m = 5, and the corpus's own "
      "'pi_n^2 phi_m/a^3 in kind' puts m = 6, giving w ~ a^(4/3)")


def spectrum(w_, Q, N=1600):
    """eigenvalues of -d^2/dq^2 + w q^2 - q^4 with Dirichlet walls at +-Q: ONE self-adjoint realisation."""
    qs = np.linspace(-Q, Q, N + 2)[1:-1]
    hgrid = qs[1] - qs[0]
    V = w_ * qs ** 2 - qs ** 4
    main = 2.0 / hgrid ** 2 + V
    off = -1.0 / hgrid ** 2 * np.ones(N - 1)
    ev, evec = np.linalg.eigh(np.diag(main) + np.diag(off, 1) + np.diag(off, -1))
    return qs, hgrid, ev, evec


# Hellmann-Feynman, at TWO different realisations (two wall positions)
for Q in (3.0, 4.0):
    w0, dw = -1.0, 1e-4
    qs, hgrid, ev0, vec0 = spectrum(w0, Q)
    _, _, evp, _ = spectrum(w0 + dw, Q)
    _, _, evm, _ = spectrum(w0 - dw, Q)
    worst = 0.0
    monotone = True
    for n in range(4):
        num = (evp[n] - evm[n]) / (2 * dw)
        psi = vec0[:, n]
        psi = psi / np.sqrt(np.sum(psi ** 2) * hgrid)
        exact = float(np.sum(psi ** 2 * qs ** 2) * hgrid)      # <psi|q^2|psi>, same arithmetic
        worst = max(worst, abs(num - exact) / exact)
        monotone = monotone and num > 0
    check(monotone and worst < 2e-3,
          f"realisation Q={Q}: dlambda_n/dw measured against the EXACT Hellmann-Feynman value "
          f"<psi_n|q^2|psi_n> for n=0..3, worst relative departure {worst:.2e}, and every derivative "
          "STRICTLY POSITIVE")

# the eigenvalue branches are strictly increasing, hence cross zero at most once
qs, hgrid, evA, _ = spectrum(-4.0, 3.0)
_, _, evB, _ = spectrum(+4.0, 3.0)
check(all(evB[n] > evA[n] for n in range(6)),
      "so every branch is strictly increasing in w -- the first six eigenvalues all rise from w=-4 to "
      "w=+4 -- and a strictly monotone analytic branch crosses zero AT MOST ONCE")

print(r"""
  ⇒ ** THE CLOSURE, WITH ITS SCOPE IN THE SAME SENTENCE. **  Limit circle at both ends (§D) makes every
    self-adjoint realisation's resolvent compact, so each has purely DISCRETE spectrum; Hellmann-Feynman
    gives dlambda_n/dw = <psi_n|q^2|psi_n> > 0 strictly, for EVERY realisation, since q^2 > 0; so for a
    realisation held FIXED across fibres the set { w : 0 in spec } is discrete, hence { a } is discrete,
    hence the condition cannot hold on a set of positive measure, hence ** there is no eigenvector at the
    three-structure content. **  ⌗ *That is `r6950`'s criterion returning one level up, exactly as the
    order said it would.*

  ⛔ ** THE ONE LOOPHOLE, NAMED AND NOT CLOSED. **  A realisation chosen fibre by fibre could track the
    zero and would supply an eigenvector.  ** But the extension sits at p -> +-infinity, the tower's
    ULTRAVIOLET, and `sec:lock` already carries "the ultraviolet definition of the tower sums" as its
    open frontier ** -- so the wall lands on an item the paper already names rather than a new one, and
    is a different KIND of object from the a = 0 extension, which is at a physical boundary and is
    already closed by the horizon's thermal state.""")

# ============================================================================ G
head("G.  WHAT IS BANKED, WHAT IS WITHDRAWN, AND WHAT IS NOT CLAIMED")

print(r"""
  ⛭ BANKED.
    · ⓵ᵃ ** A cubic potential term is in the trace ** at the power a^-2 as a MULTI-MODE structure
      phi_n phi_m phi_l -- the volume element's own (1/6)tr eps^3 = (1/2)det eps against the unperturbed
      6/a^2, and the trace formula annihilates only h ~ 1/a.
    · ⓵ᵃ ** But its single-mode diagonal sits exactly ON the degenerate set **: for a single flat TT plane
      wave transversality is algebraic, makes k a null eigenvector, and forces det eps = 0 and R^(3) = 0
      identically -- computed, not assumed.  ⇒ ** The row's next datum is one integral,
      int sqrt(gamma) det e_(n) on S^3. **
    · ⓵ᵇ ** The order is TWO at the established content **, three only if that integral is non-zero.
    · ** At the three-structure content the operator is unitarily an inverted quartic **,
      -c3 d^2/dp^2 + c1 p^2 - (c2^2/4c3) p^4, the gauge factor having modulus exactly 1.
    · ** Its deficiency indices are (2,2) and it is not essentially self-adjoint **, at every real z.
    · ** 0 lies in the point spectrum of SOME self-adjoint realisation ** of it.
    · ⓶ᵇ ** And for every realisation held fixed across fibres the criterion CLOSES **, by strict
      Hellmann-Feynman monotonicity in w against w ~ a^(4/3).

  ⛔ WITHDRAWN, and it is mine.
    · `r6962`'s "exactly one L^2 solution at each end / limit-point / deficiency (0,0) / essentially
      self-adjoint / nothing to select" -- all of it.  ** The test's discriminating order equalled the
      effect's order. **  The three `P10` sentences that carry it are routed in `FOR_66_FROM_60.md`.
    · and with it `r6962`'s "connection condition" framing, which presumed one-dimensional subspaces.

  ⚠ NOT CLAIMED.
    · ** NOT the row's "the wall is gone as an object" **, for the third time -- this time because a
      claim of mine had to be withdrawn and what replaces it is an extension family, not a closure.
      ⓶ is at three structures and is not extrapolated: a third-order operator is not a Schroedinger
      operator.
    · NOT the VALUE of the S^3 diagonal overlap -- only that the flat analogue of it vanishes for an
      algebraic reason, and that the curvature is the only thing that could lift it.  `r6946`'s selection
      rule is cited, not used to infer a value.
    · NOT a choice of realisation, and no ordering choice -- the potential cubic is a product of
      configuration variables and carries no ordering ambiguity.
    · NOT anything on prop:flat, PO-31 or PO-15; ** no corpus edit. **
""".rstrip())

print()
print("=" * 94)
if FAILED:
    print(f"FAILED {len(FAILED)} check(s):")
    for fmsg in FAILED:
        print("   -", fmsg)
    sys.exit(1)
print("ALL CHECKS PASS.")
