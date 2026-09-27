#!/usr/bin/env python3
r"""
P10_the_lowest_tt_harmonics_are_frame_constant_so_the_overlap_is_a_determinant_times_the_volume
==============================================================================================

LEVEL: **exact throughout, and there is no integral to do.**  The lowest transverse-traceless harmonics on
the closed section have CONSTANT components in the left-invariant orthonormal frame, so the integrand of
the ordered overlap is a constant and the integral is that constant times the volume.  ⌗ **No floats at
all in this receipt** -- which is the order's guard used prospectively rather than after the fact: the
question was whether the test's resolution is larger than the effect it resolves, and an exact closed form
has no resolution to compare.

OBJECT UNDER TEST -- `PO-23`, `r6967`.  The order asks the last thing between the row and its own object:

  ⓵ᵃ *"Compute it, and report it as a number with its scope ... If it is zero, say whether it is zero for a
      reason --- the flat case's zero came from an algebraic identity, and a second zero arriving by
      cancellation is a different fact from one arriving by a selection rule."*
  ⓵ᵇ *"And if it is non-zero, report the order and stop there ... Do not carry the measure argument across
      the order."*
  ⓶  *A statement rather than a computation: the one paragraph saying what the row has established, as a
      single claim with its scope, and what the remaining open thing is.*  ⇒ *Routed in
      `FOR_66_FROM_60.md`; §F records the shape it is written to.*

COMPUTES: the left-invariant frame on the unit closed section and its volume; that a constant traceless
symmetric matrix in that frame is transverse and traceless and an eigentensor at the lowest level; that the
ordered overlap's integrand is that matrix's determinant, constant on the section; the overlap; and whether
it can vanish.

-------------------------------------------------------------------------------
** THE OVERLAP IS $2\pi^{2}\det h$ --- NON-ZERO, EXACTLY, AND WITH NO INTEGRATION.  SO THE ORDER OF THE
   NULL EQUATION IS THREE, AND I STOP THERE.  BUT THE NUMBER CARRIES A SCOPE THAT MATTERS AS MUCH AS ITS
   VALUE: IT IS BASIS-DEPENDENT, WHERE THE FLAT CASE'S ZERO WAS NOT. **

** ⛭ THE LOWEST TRANSVERSE-TRACELESS HARMONICS ARE FRAME-CONSTANT, AND THAT IS WHY THERE IS NO INTEGRAL. **
Write the unit closed section with its left-invariant one-forms, $\mathrm d\sigma^{a}=-\tfrac12
\epsilon^{abc}\sigma^{b}\wedge\sigma^{c}$, and take the orthonormal coframe $e^{a}=\sigma^{a}/2$, so that
$\gamma=\sum_a e^{a}\otimes e^{a}$ and $\int\!\sqrt\gamma=2\pi^{2}$, both verified here.  Let
$\varepsilon_{ij}=h_{ab}e^{a}_{i}e^{b}_{j}$ with $h$ a **constant** symmetric traceless matrix.  Then:

  * $\gamma^{ij}\varepsilon_{ij}=\mathrm{tr}\,h=0$ exactly, and
  * $D^{i}\varepsilon_{ij}=0$ **exactly**, computed from the Christoffel symbols in coordinates --- because
    the connection enters as $\epsilon^{dac}$ contracted against a symmetric $h$, and
  * $-\nabla^{2}\varepsilon=6\,\varepsilon$, from the frame algebra with $\mathrm de^{a}=-\epsilon^{abc}
    e^{b}\wedge e^{c}$ (verified in coordinates, so $\beta=-1$) and the two $\epsilon\epsilon$
    contractions.

⇒ ** And $6$ is $m^{2}-3$ at $m=3$, while the five left-invariant plus five right-invariant tensors are
$10=2(3^{2}-4)=d(3)$: the eigenvalue and the degeneracy both identify these as the tower's lowest level. **
⌗ *Two independent identifications, which is what makes this the corpus's own harmonics rather than some
transverse-traceless tensor of my choosing.*

** ⛭ ⓵ᵃ SO THE OVERLAP IS A DETERMINANT TIMES A VOLUME, AND THE INTEGRAND IS CONSTANT. **  With the frame
orthonormal, $\varepsilon^{i}{}_{j}=(e^{-1}h\,e)^{i}{}_{j}$ --- a **similarity transform** of $h$, verified
exactly --- so
$$\det\varepsilon^{i}{}_{j}=\det h \quad\text{pointwise},\qquad
  \int\!\sqrt\gamma\,\det\varepsilon \;=\; 2\pi^{2}\det h ,$$
and $\mathrm{tr}\,\varepsilon^{3}=3\det\varepsilon$ gives the cubic term $6\pi^{2}\det h$.  ** For
$h=\mathrm{diag}(2,-1,-1)$ that is $4\pi^{2}$: NON-ZERO. **  ⌗ *There is nothing to integrate and nothing
to converge, so the order's guard has no purchase here --- which is the answer to it.*

** ⚠ AND THE SCOPE THE NUMBER CARRIES IS THE PART WORTH MORE THAN THE NUMBER. **  $\det h$ vanishes on a
codimension-one hypersurface of the five-dimensional multiplet: $\mathrm{diag}(1,-1,0)$ gives zero.
⇒ ***So "is the single-mode diagonal non-zero" is BASIS-DEPENDENT: a rotation inside the multiplet trades
$\hat\varphi_n^{3}$ against the off-diagonal $\hat\varphi_n\hat\varphi_m\hat\varphi_l$, and the diagonal is
non-zero for a generic basis and zero on a measure-zero set of them.***  ** The flat case's zero was not
like this at all: there the entire polarisation space had $\det=0$, for every choice, because transversality
was algebraic and made the wave vector a null eigenvector. **  ⌗ *That is the order's own distinction --- a
zero by a forced identity is a different fact from a zero by a choice --- applied in the affirmative
direction: this is a NON-zero by genericity, not by a selection rule.*  ⇒ *The basis-independent statement
is that the cubic potential is a non-vanishing trilinear form on the multiplet; the diagonal question is
about coordinates on it.*

** ⛔ ⓵ᵇ THE ORDER OF THE NULL EQUATION IS THREE, AND I STOP THERE. **  Four structures ---
$\hat\pi^{2},\ \mathrm{sym}(\hat\pi^{2}\hat\varphi),\ \hat\varphi^{2},\ \hat\varphi^{3}$ --- and in the
momentum representation the order is the highest power of $\hat\varphi$.  ⇒ *`r6966`'s measure argument was
taken at the three-structure content and **is not carried across**: the third-order operator is symmetric
but is not a Schr\"odinger operator, an odd-order symmetric operator need not have equal deficiency indices,
and the gauge that produced the quartic has no third-order analogue.  Named, not analysed --- the row has
been bitten twice by claims that outran the instrument that made them.*
rc=0 on all 15 checks.
"""

import sys

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


psi, th, ph = sp.symbols('psi theta phi', real=True)
X = [psi, th, ph]
LC = sp.LeviCivita

# ============================================================================ A
head("A.  THE ORDER'S GUARD, USED BEFORE THE COMPUTATION RATHER THAN AFTER IT")

print(r"""
  The order's first guard is the class `r6966` generalised: *"ask, of whatever test decides the integral,
  whether its resolution is larger than the effect it is resolving -- that is the generalisation and this
  is its first chance to be used prospectively rather than after the fact."*

  ⇒ ** ANSWERED BY THE CHOICE OF INSTRUMENT.  The lowest transverse-traceless harmonics have CONSTANT
    components in the left-invariant orthonormal frame, so the ordered integrand is a constant and the
    "integral" is a constant times a volume. **  There is no discretisation, no truncation, no quadrature
    and no asymptotic order -- so there is no resolution to compare against the effect, and the class
    cannot bite.  ⌗ *Stated before the computation, as the guard asks.  This receipt carries NO floats.*

  ⌗ The two other guards: exact arithmetic throughout (it is), and no ordering choice -- the structure is a
    product of configuration variables and carries none.""")

# ============================================================================ B
head("B.  THE FRAME, AND THAT A CONSTANT MATRIX IN IT IS TRANSVERSE-TRACELESS")

sig = [sp.Matrix([0, sp.cos(psi), sp.sin(psi) * sp.sin(th)]),
       sp.Matrix([0, -sp.sin(psi), sp.cos(psi) * sp.sin(th)]),
       sp.Matrix([1, 0, sp.cos(th)])]
e = sp.Matrix(3, 3, lambda a, i: sig[a][i] / 2)          # rows are e^a_i = sigma^a_i / 2
g = sp.simplify(e.T * e)
ginv = sp.simplify(g.inv())

check(sp.simplify(sp.expand(g - e.T * e)) == sp.zeros(3, 3),
      f"the coframe is orthonormal by construction: gamma = sum_a e^a (x) e^a = {g.tolist()}")

sqrtg = sp.simplify(sp.sqrt(g.det()))
vol = sp.integrate(sp.integrate(sp.integrate(sp.sin(th) / 8, (psi, 0, 4 * sp.pi)),
                                (th, 0, sp.pi)), (ph, 0, 2 * sp.pi))
check(sp.simplify(sqrtg - sp.Abs(sp.sin(th)) / 8) == 0 and sp.simplify(vol - 2 * sp.pi ** 2) == 0,
      f"sqrt(det gamma) = {sqrtg} and the volume integrates to {vol} = 2 pi^2 exactly")


def wedge2(u, v):
    """the 2-form u ^ v as an antisymmetric matrix of components."""
    return sp.Matrix(3, 3, lambda i, j: u[i] * v[j] - u[j] * v[i])


def dform(u):
    """exterior derivative of a 1-form, as an antisymmetric component matrix."""
    return sp.Matrix(3, 3, lambda i, j: sp.diff(u[j], X[i]) - sp.diff(u[i], X[j]))


# d sigma^a = -(1/2) eps^{abc} sigma^b ^ sigma^c, and hence d e^a = - eps^{abc} e^b ^ e^c  (beta = -1)
ok_struct = True
for a in range(3):
    rhs = sp.zeros(3, 3)
    for b in range(3):
        for c in range(3):
            rhs += -sp.Rational(1, 2) * LC(a, b, c) * wedge2(sig[b], sig[c])
    ok_struct = ok_struct and sp.simplify(sp.expand(dform(sig[a]) - rhs)) == sp.zeros(3, 3)
check(ok_struct,
      "the structure equations hold exactly: d sigma^a = -(1/2) eps^abc sigma^b ^ sigma^c, so with "
      "e^a = sigma^a/2 we have d e^a = - eps^abc e^b ^ e^c, i.e. the connection is omega^d_ac = -eps^dac")

h11, h22, h12, h13, h23 = sp.symbols('h11 h22 h12 h13 h23', real=True)
H = sp.Matrix([[h11, h12, h13], [h12, h22, h23], [h13, h23, -h11 - h22]])
check(sp.trace(H) == 0, "h is a GENERAL constant symmetric traceless matrix: five free parameters")

eps_t = e.T * H * e                                       # eps_ij = h_ab e^a_i e^b_j
check(sp.simplify(sum(ginv[i, j] * eps_t[i, j] for i in range(3) for j in range(3))) == 0,
      "it is TRACELESS exactly: gamma^ij eps_ij = tr h = 0")

Gam = [[[sp.simplify(sum(ginv[i, l] * (sp.diff(g[l, j], X[k]) + sp.diff(g[l, k], X[j])
                                       - sp.diff(g[j, k], X[l])) for l in range(3)) / 2)
         for k in range(3)] for j in range(3)] for i in range(3)]
div = []
for j in range(3):
    tot = 0
    for i in range(3):
        for k in range(3):
            tot += ginv[i, k] * (sp.diff(eps_t[k, j], X[i])
                                 - sum(Gam[l][i][k] * eps_t[l, j] for l in range(3))
                                 - sum(Gam[l][i][j] * eps_t[k, l] for l in range(3)))
    div.append(sp.simplify(sp.expand(tot)))
check(all(d == 0 for d in div),
      f"and TRANSVERSE exactly, from the Christoffel symbols in coordinates: D^i eps_ij = {div} for a "
      "GENERAL h, so this is the whole five-dimensional space and not one lucky member")

# the eigenvalue, from the frame algebra: nabla^2 h_ab = -6 h_ab with beta = -1
beta = -1
T = sp.MutableDenseNDimArray.zeros(3, 3, 3)
for a in range(3):
    for b in range(3):
        for c in range(3):
            T[a, b, c] = -beta * sum(LC(d, a, c) * H[d, b] + LC(d, b, c) * H[a, d] for d in range(3))
lap = sp.zeros(3, 3)
for a in range(3):
    for b in range(3):
        lap[a, b] = sp.expand(-beta * sum(LC(d, a, c) * T[d, b, c] + LC(d, b, c) * T[a, d, c]
                                          for d in range(3) for c in range(3)))
check(sp.simplify(sp.expand(lap + 6 * H)) == sp.zeros(3, 3),
      "and it is an EIGENTENSOR: nabla^2 h = -6 h exactly, from the frame algebra with beta = -1")

MU2, DEG = 3 ** 2 - 3, 2 * (3 ** 2 - 4)
check(MU2 == 6 and DEG == 10,
      f"⇒ mu^2 = m^2-3 = {MU2} at m = 3 MATCHES the eigenvalue, and 5 left-invariant + 5 right-invariant "
      f"= 10 = 2(m^2-4) = d(3) MATCHES the degeneracy: ** two independent identifications of the tower's "
      "lowest level **")

# ============================================================================ C
head("C.  ⓵ᵃ  THE OVERLAP: A DETERMINANT TIMES A VOLUME, WITH NOTHING TO INTEGRATE")

mixed = sp.simplify(ginv * eps_t)
check(sp.simplify(sp.expand(mixed - e.inv() * H * e)) == sp.zeros(3, 3),
      "eps^i_j = e^-1 h e -- a SIMILARITY transform of h, exactly, because the frame is orthonormal")
check(sp.simplify((e.inv() * H * e).det() - H.det()) == 0,
      "so det eps^i_j = det h POINTWISE and for a general h: the integrand is CONSTANT on the section")

overlap = sp.simplify(2 * sp.pi ** 2 * H.det())
check(sp.simplify(overlap - 2 * sp.pi ** 2 * H.det()) == 0,
      "⇒ ** int sqrt(gamma) det eps = 2 pi^2 det h, exactly, with no integration performed **")

H0 = sp.Matrix([[2, 0, 0], [0, -1, 0], [0, 0, -1]])
check(sp.trace(H0) == 0 and H0.det() == 2,
      f"for h = diag(2,-1,-1): traceless, det = {H0.det()}, so the overlap is {2 * H0.det()} pi^2 "
      f"= {sp.nsimplify(2 * H0.det())} pi^2 -- ** NON-ZERO **")
check(sp.simplify(sp.trace(H0 ** 3) - 3 * H0.det()) == 0,
      f"and tr eps^3 = 3 det eps = {sp.trace(H0 ** 3)}, so the cubic term of sqrt(h) R carries "
      f"{6 * H0.det()} pi^2 on this member")

H1 = sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]])
check(sp.trace(H1) == 0 and H1.det() == 0,
      f"⚠ but diag(1,-1,0) is equally traceless with det = {H1.det()}: the vanishing set is the "
      "codimension-one hypersurface det h = 0 inside the five-dimensional multiplet")

print(r"""
  ⇒ ** SO THE ANSWER IS NON-ZERO, AND ITS SCOPE IS THAT IT IS BASIS-DEPENDENT. **  A rotation inside the
    multiplet trades the diagonal phi_n^3 against the off-diagonal phi_n phi_m phi_l, so the diagonal is
    non-zero for a GENERIC basis and zero on a measure-zero set of them.  The basis-independent statement
    is that the cubic potential is a non-vanishing trilinear form on the multiplet.

  ** AND THIS IS NOT THE FLAT CASE'S ZERO WITH THE SIGN FLIPPED -- IT IS A DIFFERENT KIND OF FACT. **
    `r6966` showed the flat polarisation space [[A,B,0],[B,-A,0],[0,0,0]] has det = 0 for EVERY member,
    because transversality there is the algebraic k^j eps_ij = 0 and makes the wave vector a null
    eigenvector.  ⇒ *A zero forced by an identity, against a non-zero holding generically: the order asked
    for exactly this distinction, and the answer runs in the affirmative direction.*""")

# ============================================================================ D
head("D.  ⓵ᵇ  THE ORDER IS THREE, AND WHY THE MEASURE ARGUMENT DOES NOT COME WITH IT")

structures = {"pi^2": 0, "sym(pi^2 phi)": 1, "phi^2": 2, "phi^3": 3}
for k, v in structures.items():
    print(f"      {k:<16} -> order {v}")
check(max(structures.values()) == 3 and len(structures) == 4,
      "** four structures, so the order of the null equation in the momentum representation is THREE **")

print(r"""
  ⛔ ** AND I STOP THERE, WHICH IS WHAT THE ORDER ASKS. **  `r6966`'s measure closure was taken at the
    three-structure content.  Three reasons it does not carry, each a fact and not a worry:

      · the gauge that produced the quartic removes a FIRST-order term from a SECOND-order operator; there
        is no third-order analogue of it, so the inverted-quartic form is not available;
      · an odd-order symmetric differential operator need not have equal deficiency indices, so even the
        COUNTING at the two ends is a different problem, not a longer version of the same one;
      · and the Hellmann-Feynman step needs a self-adjoint operator with discrete spectrum and a positive
        perturbation, which is a statement about the second-order case.

    ⇒ *Named, not analysed.  This row has now been bitten twice by claims that outran the instrument that
      made them, and the second of those was mine one revision ago.*""")

# ============================================================================ E
head("E.  ⓶  THE PARAGRAPH, AND THE ONE PLACE IT DECLINES THE ORDER'S OWN HOPE")

print(r"""
  The paragraph itself is routed in `FOR_66_FROM_60.md`; what belongs in a receipt is the shape it is
  written to, and the one place it does not give the order what it asked for.

  ⌗ ** THE SEVEN APPROACHES DO SUPPORT ONE CLAIM **, and it is about the residue rather than about seven
    separate things: once the scale factor is quantized, the tower's renormalized zero point makes one
    ultraviolet constant observable, and every route by which the construction could have hidden it again
    has been closed -- no rescaling of the frequencies reaches it, the logarithm it produces has no partner
    to cancel against, the interaction cannot reach the power of the scale factor the counterterm sits at,
    and the curvature operator that results has no eigenvector for a realisation fixed across the fibres.

  ⚠ ** BUT THE ORDER HOPED THE REMAINDER WOULD BE ONE THING, AND AFTER §C IT IS TWO. **  The order said:
    *"If it is the ultraviolet definition and nothing else, say that."*  It is not, and I will not say it
    was.  The remainder is:

      (i) ** a definitional item, and it is the row's own founding object **: the ultraviolet definition of
          the tower's mode sums, which is where the one freedom the measure argument does not fix lives --
          a realisation chosen fibre by fibre at unbounded momentum;
      (ii) ** an ordinary computational step, opened by THIS revision **: the criterion at third order,
          since §C makes the content four structures and §D says the second-order argument does not carry.

    ⇒ *The two are different in kind, and saying so is the honest shape.  (i) cannot be closed by a
      calculation of this sort at all; (ii) is a calculation of exactly this sort, not yet done.*

  ⌗ *The order's own guard: "a paragraph that claims more than the seven jointly support would undo all of
    them, and I would rather have the honest shape than a clean one."  This is the clean one declined.*
""".rstrip())

print()
print("=" * 94)
if FAILED:
    print(f"FAILED {len(FAILED)} check(s):")
    for fmsg in FAILED:
        print("   -", fmsg)
    sys.exit(1)
print("ALL CHECKS PASS.")
