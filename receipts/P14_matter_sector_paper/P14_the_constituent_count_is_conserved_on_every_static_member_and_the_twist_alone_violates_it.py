"""
P14_the_constituent_count_is_conserved_on_every_static_member_and_the_twist_alone_violates_it
=============================================================================================

Object under test -- whether the determinant circle r6742 derived is a GLOBAL, exactly conserved
constituent count.  Its modes are purely chiral (dim ker_+ = 3, dim ker_- = 0), so its mixed
U(1)-gravitational anomaly coefficient need not vanish, and the source term is a parity-odd
invariant the construction has exactly one candidate to turn on.

** THE ANSWER IS BOTH, AND WHICH ONE IS A PROPERTY OF THE MEMBER.  The count is EXACTLY conserved
on every STATIC member -- not on three sampled ones but on the whole static family, for arbitrary
profiles, the source vanishing IDENTICALLY.  It is violated on the TWISTED member, and the twist is
the only thing that violates it: the source is exactly ODD in the twist and vanishes identically at
c = 0.  The coefficient is THREE. **

AND THE VIOLATION'S SIZE IS A BOUNDARY QUANTITY, WHICH IS WHAT MAKES "AT WHAT RATE" ANSWERABLE.
The source is the divergence of the gravitational Chern--Simons current, measured here rather than
cited -- sqrt(-g) *RR = -d_mu K^mu, the ratio a CONSTANT and not a function -- so the total
violation between two slices is the CHANGE IN THE MEMBER'S GRAVITATIONAL CHERN--SIMONS NUMBER:

    Delta N  =  -(3/384 pi^2) [ integral K^0 d^3x ]  between the two slices

a finite number set by the endpoints, zero whenever the member is untwisted, and odd in the twist.

THE ANSWER TO Q1 IS POSITIVE WHERE r6752's WAS NEGATIVE, AND THE SAME COMPUTATION DECIDES BOTH --
WHICH IS THE WHOLE OF W1.  r6752 found no connection because a position-dependent rotation g(x)
gives D(g Psi) = g D Psi + (dg) Psi, carrying a mode out of the kernel.  ** A global phase is
exactly the case dg = 0. **  So the identity that closed the local route is the identity that opens
the global one: e^{i theta} commutes with D on the nose, the seats' amplitudes carry a common phase,
and a common phase on a field needs NO bundle -- only a phase.  A gauge field would have needed a
connection over a member's spacetime, which there is none of; a Noether current needs a symmetry of
the action, which there is.  ** Two different demands on the same object, and this one is met. **

WHERE THE COEFFICIENT COMES FROM, AND THE 2+1 THAT WOULD HAVE GIVEN THE WRONG ONE.  The coefficient
is the LINEAR trace over the chiral content, sum_+ q - sum_- q, and P14's wall content is
dim ker_+ = 3, dim ker_- = 0 with each seat of determinant charge one, so it is 3 - 0 = 3.  ** P14
carries a 2+1 as well, and it is at the TURNAROUND LIFT and not the wall. **  Used there the
coefficient would read 2 - 1 = 1.  It is the wrong locus: the determinant circle r6742 derived acts
on the WALL kernel, whose split is forced to 3+0 by the hinge S_3's transitivity, and P14 says of
the lift in its own words that it "seats the wrong three".  Recorded because the two numbers differ
and nothing but the locus distinguishes them.

Q2 IS ANSWERED FAR ABOVE WHAT WAS ASKED, AND THAT IS THE STRONGEST RESULT HERE.  The order asks
whether the source is zero on the static members by computation rather than by argument.  It is --
and not member by member: the Pontryagin density vanishes IDENTICALLY on

    static spherical  ds^2 = -f dr^2 ... with f an ARBITRARY function        *RR == 0
    static spherical with arbitrary f, h AND areal profile S                 *RR == 0
    the static axisymmetric Weyl form with arbitrary U, K                    *RR == 0

so Schwarzschild, Schwarzschild--de Sitter, Nariai and every other static member of the corpus's
family are instances of one identity rather than three lucky zeros.  ** A zero is a result (W5), and
this one is a family-wide zero. **

AND THE TWISTED MEMBER IS COMPUTED GENERALLY TOO, NOT ON A REPRESENTATIVE.  On the unpolarised
Gowdy--de Sitter form with A, psi, omega, R ARBITRARY functions of (t, z), the density is a
polynomial in omega's derivatives in which

    bare omega appears to degree 0 -- only its DERIVATIVES occur
    every monomial has ODD total degree, the powers present being exactly {1, 3}

so *RR(-omega) = -*RR(omega) EXACTLY, and *RR == 0 identically when omega is constant, which is
P11's polarised cut.  Since P11's conserved twist c = R e^{2P} Q_t is linear in omega's derivative
and C50's orientation parity acts as c -> -c, odd in the twist is what odd in the derivatives means.
** W4 is met on the general member and not on a lucky one. **

Q4 IS NEGATIVE ON TWO INDEPENDENT GROUNDS, AND THE ORDER'S DISTINCTION IS THE LOAD-BEARING ONE.
Asked is whether the construction HAS a bulk gravitational Chern--Simons term, not whether one could
be added.  (i) The corpus contains no such term: "Chern--Simons" occurs nowhere in its papers, and
the one place a topological term's coefficient is weighed -- P17's constant ledger, on P10's
parity-odd caveat -- explicitly DECLINES it, the ledger counting no counterterm coefficient.
(ii) Structurally, the inflow term for a mixed U(1)-gravitational anomaly is integral A ^ tr(R ^ R),
which needs a ONE-FORM GAUGE POTENTIAL for the circle -- and r6752 established there is none on a
member's spacetime.  ** The ingredient is missing, not merely the term. **  So there is no inflow,
and the anomaly is not cancelled by one.

  ⚠ W2 IS THE POINT AND NOT A HEDGE.  A global symmetry's anomaly is NOT an inconsistency.  Nothing
  here is reported as a defect: the determinant circle is global (r6752 closed the gauging), and a
  global current with a nonzero gravitational anomaly is an ordinary, consistent situation -- it is
  the Standard Model's own situation for baryon number.  W3's contrast is that there the chiral
  content is vector-like in the relevant trace and here it is not, and the reason is dim ker_- = 0.

  ⚠ AND THE NON-CANCELLATION IS NOT A CONVENTION (C3).  Reversing which chirality is called
  positive sends the coefficient 3 -> -3; it does not send it to zero.  A vector-like set -- the
  same three seats with three opposite-chirality partners -- gives 3 - 3 = 0 in EITHER convention.
  So the sign is a convention and the non-vanishing is dim ker_- = 0.

CONSTRUCTION.  The order leaves how the curvature invariant is computed, on which members, and how
inflow is tested to this line.  The invariant is the Pontryagin density
*RR = (1/2) eps^{mu nu rho sigma} R_{mu nu alpha beta} R_{rho sigma}^{alpha beta} / sqrt(-g),
computed from the metric with the curvature tensor's antisymmetries used as STORAGE rather than
checked afterwards -- R_{[mn][ab]} has 36 independent components, not 256, and raising against a
sparse inverse metric costs a handful of products per component instead of sixteen.  That is what
makes a fully general Gowdy member with four arbitrary functions computable at all; the earlier
brute-force form did not finish on Kerr in nine minutes.  The machinery is calibrated three ways
before any result is read off it: against Schwarzschild's zero, against Kerr's known type-D closed
form, and against the Chern--Simons identity.

COMPUTES: scope -- what the pinned numbers do and do not bound.
  * ** The two results that answer the order are pinned to NOTHING. **  Q2's zero is computed with the
    static profiles left as ARBITRARY FUNCTIONS ($f$; $f, h$ and the areal radius; the Weyl $U, K$), and
    Q3's oddness with all four Gowdy metric functions arbitrary.  Those two carry no parameter at all,
    which is the whole reason they are stated as family-wide identities rather than as sampled zeros.
  * `M = 1` in the Kerr calibration is a LENGTH UNIT, not a physical choice: the density scales as $M^2$
    and the closed form carries that dependence symbolically, checked against symbolic $M$.
  * ** `a = +1/2, -1/2, 0` are the only spins the direct machinery is run at, and that is a real
    limit. **  What they establish is that the machinery separates zero from nonzero and returns an
    exact sign reversal.  The claim that Kerr is odd in the spin FOR ALL $a$ rests on the closed form,
    which is verified against the machinery at those three spins and then shown odd for SYMBOLIC $a$.
    *Three exact agreements plus a symbolic identity, not a sweep.*
  * `(A, psi, omega, R) = (t/3, z/5, c t z, t)` is an explicit member used only to EXHIBIT a nonzero
    density and to measure the Chern--Simons ratio.  ** It is not a solution of the field equations and
    nothing quantitative is read off it: **  the general computation above it is what carries the
    result, and the representative is there so the nonzero is shown and not only argued.
  * The anomaly's universal prefactor $1/384\pi^2$ is NOT computed here and is not this construction's.
    Only the coefficient $A = 3$ is derived, and it is an integer count, not a fitted number.

ORIGIN: written for r6758's order on whether the determinant circle's count is conserved; the
machinery, the choice of members, the general-family computations, the Chern--Simons measurement and
the inflow test are this line's.
"""
import itertools
import os
import re
import sympy as sp

# ----------------------------------------------------------------------------------------
_checks = []


def check(label, ok):
    _checks.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    assert ok, label


print(__doc__)

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))

PAIRS = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
EPS = {}
for _perm in itertools.permutations(range(4)):
    EPS[_perm] = int(sp.Matrix([[1 if _perm[i] == j else 0 for j in range(4)]
                                for i in range(4)]).det())


def christoffels(g, X, simp):
    """Gamma^l_{ij}, symmetric in the lower pair -- 40 entries computed, not 64."""
    gi = g.inv()
    gi = sp.Matrix(4, 4, lambda i, j: simp(gi[i, j]))
    nz = [[j for j in range(4) if gi[i, j] != 0] for i in range(4)]
    Gam = [[[None] * 4 for _ in range(4)] for _ in range(4)]
    for l in range(4):
        for i in range(4):
            for j in range(i, 4):
                e = simp(sum(gi[l, s] * (sp.diff(g[s, i], X[j]) + sp.diff(g[s, j], X[i])
                                         - sp.diff(g[i, j], X[s])) for s in nz[l]) / 2)
                Gam[l][i][j] = Gam[l][j][i] = e
    return Gam, gi, nz


def pontryagin(g, X, simp=sp.cancel):
    """*RR = (1/2) eps^{mnrs} R_{mn ab} R_{rs}^{ab} / sqrt(-g)  --  a pseudoscalar.

    The antisymmetries are the storage scheme: R^l_{i[jk]} is held on 96 slots and
    R_{[mn][ab]} on 36, and the raising runs over the inverse metric's OWN sparsity.
    """
    Gam, gi, nz = christoffels(g, X, simp)

    Rm = {}
    for l in range(4):
        for i in range(4):
            for (j, k) in PAIRS:
                e = sp.diff(Gam[l][i][k], X[j]) - sp.diff(Gam[l][i][j], X[k])
                e += sum(Gam[l][j][s] * Gam[s][i][k] - Gam[l][k][s] * Gam[s][i][j]
                         for s in range(4))
                Rm[(l, i, j, k)] = simp(e)

    def Rmix(l, i, j, k):
        if j == k:
            return sp.Integer(0)
        return Rm[(l, i, j, k)] if j < k else -Rm[(l, i, k, j)]

    RD = {(m, n, a, b): simp(sum(g[m, s] * Rmix(s, n, a, b) for s in range(4)))
          for (m, n) in PAIRS for (a, b) in PAIRS}

    def pick(T, m, n, a, b):
        if m == n or a == b:
            return sp.Integer(0)
        s = 1
        if m > n:
            m, n, s = n, m, -s
        if a > b:
            a, b, s = b, a, -s
        return s * T[(m, n, a, b)]

    RU = {(m, n, a, b): simp(sum(gi[a, al] * gi[b, be] * pick(RD, m, n, al, be)
                                 for al in nz[a] for be in nz[b]))
          for (m, n) in PAIRS for (a, b) in PAIRS}

    P = 0
    for perm, sgn in EPS.items():
        m, n, r_, s_ = perm
        # the summand is symmetric under (al,be) -> (be,al) and vanishes on al == be,
        # so the 16-term inner sum is twice the sum over the 6 pairs
        P += 2 * sgn * sum(pick(RD, m, n, al, be) * pick(RU, r_, s_, al, be)
                           for (al, be) in PAIRS)
    return simp(P / (2 * sp.sqrt(-simp(g.det()))))


def cs_current(g, X, simp=sp.simplify):
    """the gravitational Chern--Simons current
    K^mu = 2 eps^{mu nu rho sigma} ( Gam^a_{nu b} d_rho Gam^b_{sigma a}
                                     + (2/3) Gam^a_{nu b} Gam^b_{rho c} Gam^c_{sigma a} )"""
    Gam, _, _ = christoffels(g, X, simp)
    out = []
    for mu in range(4):
        tot = 0
        for perm, sg in EPS.items():
            if perm[0] != mu:
                continue
            _, nu, rho, sig = perm
            tot += sg * sum(Gam[a][nu][b] * sp.diff(Gam[b][sig][a], X[rho])
                            for a in range(4) for b in range(4))
            tot += sg * sp.Rational(2, 3) * sum(
                Gam[a][nu][b] * Gam[b][rho][c] * Gam[c][sig][a]
                for a in range(4) for b in range(4) for c in range(4))
        out.append(simp(2 * tot))
    return out


t, r, u, th, ph, z, x, y = sp.symbols('t r u theta phi z x y', real=True)


def kerr_bl(M, a):
    """Kerr in Boyer--Lindquist with u = cos(theta): g_{uu} = Sigma/(1-u^2), so the whole
    metric is RATIONAL and `cancel` is exact.  M = 0 or a = 0 degrade correctly."""
    S = r ** 2 + a ** 2 * u ** 2
    Dl = r ** 2 - 2 * M * r + a ** 2
    s2 = 1 - u ** 2
    g = sp.zeros(4, 4)
    g[0, 0] = -(1 - 2 * M * r / S)
    g[0, 3] = g[3, 0] = -2 * M * r * a * s2 / S
    g[1, 1] = S / Dl
    g[2, 2] = S / s2
    g[3, 3] = (r ** 2 + a ** 2 + 2 * M * r * a ** 2 * s2 / S) * s2
    return g


def gowdy_unpolarised(A, psi, om, R):
    """P11's unpolarised Gowdy--de Sitter form, coordinates (t, z, x, y):
    ds^2 = e^{2A}(-dt^2 + dz^2) + e^{2psi}(dx + om dy)^2 + R^2 e^{-2psi} dy^2.
    The off-diagonal `om` is what makes the wave unpolarised (C50's own control)."""
    g = sp.zeros(4, 4)
    g[0, 0] = -sp.exp(2 * A)
    g[1, 1] = sp.exp(2 * A)
    g[2, 2] = sp.exp(2 * psi)
    g[2, 3] = g[3, 2] = sp.exp(2 * psi) * om
    g[3, 3] = sp.exp(2 * psi) * om ** 2 + R ** 2 * sp.exp(-2 * psi)
    return g


# =========================================================================================
print("=" * 94)
print("PART 1 (C1) — THE MACHINERY TELLS SCHWARZSCHILD FROM KERR, AND IS NOT ZERO BY CONSTRUCTION")
print("=" * 94)
print("""
  The one calibration the order names.  Schwarzschild's Pontryagin density must come out
  IDENTICALLY zero and Kerr's nonzero and ODD in the spin -- from the SAME code path, with only
  the spin parameter changed, so that neither answer can be an artefact of how the case was set up.
  M = 1 throughout (a length unit, not an assumption); a = +1/2, -1/2, 0 as exact rationals.
""")

KERR = {}
for a_val in [sp.Rational(1, 2), sp.Rational(-1, 2), sp.Integer(0)]:
    KERR[a_val] = sp.factor(sp.cancel(pontryagin(kerr_bl(sp.Integer(1), a_val),
                                                 [t, r, u, ph], simp=sp.cancel)))
    print(f"    a = {str(a_val):>5}    *RR = {KERR[a_val]}")
print()

check("Schwarzschild (a = 0): *RR is IDENTICALLY zero",
      sp.simplify(KERR[sp.Integer(0)]) == 0)
check("Kerr (a = 1/2): *RR is NOT zero",
      sp.simplify(KERR[sp.Rational(1, 2)]) != 0)
check("Kerr is ODD in the spin: *RR(a) + *RR(-a) == 0, exactly",
      sp.simplify(KERR[sp.Rational(1, 2)] + KERR[sp.Rational(-1, 2)]) == 0)

# and the same density against the type-D closed form, which is an INDEPENDENT route:
# Psi_2 = -M/(r - i a cos theta)^3 and *RR proportional to Im(Psi_2^2)
aa, MM = sp.symbols('a M', real=True)
Psi2 = -MM / (r - sp.I * aa * u) ** 3
ImPsi2sq = sp.simplify(sp.im(sp.expand(Psi2 ** 2).rewrite(sp.re)))
closed = sp.cancel(-96 * MM ** 2 * aa * r * u * (3 * r ** 2 - aa ** 2 * u ** 2)
                   * (r ** 2 - 3 * aa ** 2 * u ** 2) / (r ** 2 + aa ** 2 * u ** 2) ** 6)
print()
print("    the type-D closed form, from the Weyl scalar Psi_2 = -M/(r - i a cos(theta))^3:")
print(f"      *RR = {closed}")
for a_val in [sp.Rational(1, 2), sp.Rational(-1, 2), sp.Integer(0)]:
    check(f"closed form agrees with the machinery at a = {a_val}, exactly",
          sp.simplify(closed.subs({MM: 1, aa: a_val}) - KERR[a_val]) == 0)
check("the closed form is proportional to Im(Psi_2^2) -- same zero set, same factorisation",
      sp.simplify(sp.cancel(closed / sp.cancel(ImPsi2sq)) - (-48)) == 0)
check("the closed form is odd in a for SYMBOLIC a (so the rationals were not special)",
      sp.simplify(closed.subs(aa, -aa) + closed) == 0)
print("""
  * So the machinery reproduces, independently, the factorisation (3r^2 - a^2 u^2)(r^2 - 3a^2 u^2)
    that the Newman--Penrose route gives.  That is a far stronger calibration than a single zero:
    a code path returning zero by construction cannot reproduce a nontrivial factorisation. *
""")

# =========================================================================================
print("=" * 94)
print("PART 2 (C2) — THE CHANNEL CHARGES 3 / 2 / 0, FROM THE DETERMINANT OF THE SEAT REPRESENTATION")
print("=" * 94)
print("""
  P14 counts the bound channels on the EXTERIOR POWERS of the three-dimensional wall kernel:
  baryon = Lambda^3, diquark = Lambda^2, meson = V tensor V-bar.  The determinant circle is the
  central circle of r6742's canonical U(3), under which a single seat carries charge one.  The
  channel charges are then READ OFF the induced representations rather than asserted.
""")
theta = sp.Symbol('vartheta', real=True)
w = sp.exp(sp.I * theta)
V = w * sp.eye(3)                                        # the central circle, acting on the seats
Vbar = sp.conjugate(w) * sp.eye(3)                       # and on the conjugate seats

basis2 = [(0, 1), (0, 2), (1, 2)]


def induced_lambda2(g):
    """the action on Lambda^2 in the basis e_0^e_1, e_0^e_2, e_1^e_2 -- 2x2 minors of g"""
    return sp.Matrix(3, 3, lambda I, J: sp.expand(
        g[basis2[I][0], basis2[J][0]] * g[basis2[I][1], basis2[J][1]]
        - g[basis2[I][0], basis2[J][1]] * g[basis2[I][1], basis2[J][0]]))


def charges(Mx):
    """the U(1) charges carried by a channel, read off the GENERATOR rather than the group
    element: q is the eigenvalue of (d/d vartheta) rho(V(vartheta)) at the identity, divided
    by i.  Taking the log of exp(3 i vartheta) instead would ask which branch, which is a
    question about the parametrisation and not about the charge."""
    gen = sp.simplify(sp.diff(Mx, theta).subs(theta, 0) / sp.I)
    return set(sp.nsimplify(sp.simplify(e)) for e in gen.eigenvals())


CHANNELS = {
    'baryon  (Lambda^3 V)': sp.Matrix([[sp.expand(V.det())]]),
    'diquark (Lambda^2 V)': induced_lambda2(V),
    'meson   (V (x) V-bar)': sp.Matrix(9, 9, lambda I, J: sp.expand(
        V[I // 3, J // 3] * Vbar[I % 3, J % 3])),
    'one seat (V itself)  ': V,
}
EXPECT = {'baryon  (Lambda^3 V)': 3, 'diquark (Lambda^2 V)': 2,
          'meson   (V (x) V-bar)': 0, 'one seat (V itself)  ': 1}
for name, Mx in CHANNELS.items():
    qs = charges(Mx)
    print(f"    {name}:  acts as exp(i q vartheta) with q in "
          f"{sorted(qs, key=lambda s: sp.re(s))}")
    check(f"{name.split('(')[0].strip()} carries determinant charge {EXPECT[name]}",
          qs == {sp.Integer(EXPECT[name])})
check("the generator route is calibrated: the trivial representation carries charge 0",
      charges(sp.eye(2)) == {sp.Integer(0)})
print("""
  * The three numbers are 3 / 2 / 0, which is the constituent count of each channel.  ** That is
    what makes the circle a CONSTITUENT COUNT and not merely a phase: the charge of a channel is
    the number of seats in it, with the antiseat counting -1, which is why the meson is neutral. **
""")

# =========================================================================================
print("=" * 94)
print("PART 3 (C3) — A VECTOR-LIKE SET CANCELS; THE NON-CANCELLATION IS dim ker_- = 0")
print("=" * 94)
print("""
  The mixed U(1)-gravitational anomaly coefficient is the LINEAR trace over the chiral content,
  A = sum_+ q - sum_- q.  It is computed here for four contents, one of which is P14's.
""")


def coefficient(plus, minus, sign=+1):
    """A = sum over positive-chirality charges minus sum over negative.  `sign` flips which
    chirality is called positive -- a convention, tested as one."""
    return sign * (sum(plus) - sum(minus))


CONTENTS = {
    "P14's wall content   ker_+ = 3 seats, ker_- = 0": ([1, 1, 1], []),
    "a VECTOR-LIKE set    ker_+ = 3 seats, ker_- = 3": ([1, 1, 1], [1, 1, 1]),
    "one seat only        ker_+ = 1, ker_- = 0       ": ([1], []),
    "the turnaround LIFT  2 + 1  (the WRONG locus)   ": ([1, 1], [1]),
}
COEFF = {}
for name, (p, m) in CONTENTS.items():
    COEFF[name] = coefficient(p, m)
    print(f"    {name}   A = {COEFF[name]:+d}")
print()
check("P14's content gives A = 3",
      COEFF["P14's wall content   ker_+ = 3 seats, ker_- = 0"] == 3)
check("a vector-like set gives A = 0 -- it CANCELS",
      COEFF["a VECTOR-LIKE set    ker_+ = 3 seats, ker_- = 3"] == 0)
check("the vector-like cancellation survives the chirality convention (both signs give 0)",
      coefficient([1, 1, 1], [1, 1, 1], +1) == 0 == coefficient([1, 1, 1], [1, 1, 1], -1))
check("but P14's 3 only changes SIGN under that convention, never vanishing",
      {coefficient([1, 1, 1], [], +1), coefficient([1, 1, 1], [], -1)} == {3, -3})
check("so the non-cancellation traces to dim ker_- = 0 and not to a convention",
      COEFF["P14's wall content   ker_+ = 3 seats, ker_- = 0"] != 0
      and COEFF["a VECTOR-LIKE set    ker_+ = 3 seats, ker_- = 3"] == 0)
print("""
  ⌗ THE 2+1 IS REAL AND IT IS SOMEWHERE ELSE, WHICH IS WORTH RECORDING RATHER THAN OMITTING.
    P14 carries dim ker_+ = 2, dim ker_- = 1 -- at the TURNAROUND LIFT.  Used there the coefficient
    would read 1, not 3.  The determinant circle r6742 derived acts on the WALL kernel, whose split
    P14 forces to 3+0 by the hinge S_3's transitivity together with R's centrality, and of the lift
    P14 says in its own words that it "seats the wrong three".  ** Nothing but the locus separates
    the two numbers, which is exactly why W1's question has to be asked at every step. **
""")
check("the lift's locus would have given 1, so the two loci are genuinely distinguishable",
      COEFF["the turnaround LIFT  2 + 1  (the WRONG locus)   "] == 1)

# =========================================================================================
print("=" * 94)
print("PART 4 (Q1) — IS THERE A SPACETIME CURRENT AT ALL?  YES, AND r6752's IDENTITY IS WHY")
print("=" * 94)
print("""
  W1's question, and it decides the whole order.  r6752 found NO connection over a member's
  spacetime, from the identity D(g Psi) = g D Psi + (dg) Psi: a position-dependent rotation carries
  a mode out of the kernel.  ** A global phase is the case dg = 0 of that very identity. **  So the
  same computation that closed the local route opens the global one, and it is run here in both
  directions so the asymmetry is measured rather than asserted.
""")
gx = sp.Function('g')(x)                                 # a position-dependent phase
const_phase = sp.exp(sp.I * sp.Symbol('vartheta0', real=True))
Psi = sp.Function('Psi')(x)
D = lambda f: sp.diff(f, x)                              # the derivative part is what dg tests

resid_local = sp.simplify(D(gx * Psi) - gx * D(Psi))
resid_global = sp.simplify(D(const_phase * Psi) - const_phase * D(Psi))
print(f"    position-dependent g(x):  D(g Psi) - g D(Psi) = {resid_local}      <- NOT zero")
print(f"    constant phase         :  D(e^{{i th}} Psi) - e^{{i th}} D(Psi) = {resid_global}"
      "                <- zero")
check("a position-dependent rotation leaves the kernel: the residual is (dg) Psi, nonzero",
      sp.simplify(resid_local - sp.diff(gx, x) * Psi) == 0 and resid_local != 0)
check("a CONSTANT phase commutes with the operator exactly -- dg = 0",
      resid_global == 0)

# the Noether current of that phase, and its conservation on-shell, with explicit Dirac matrices
g0 = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]])
g1 = sp.Matrix([[0, 0, 0, 1], [0, 0, 1, 0], [0, -1, 0, 0], [-1, 0, 0, 0]])
g2 = sp.Matrix([[0, 0, 0, -sp.I], [0, 0, sp.I, 0], [0, sp.I, 0, 0], [-sp.I, 0, 0, 0]])
g3 = sp.Matrix([[0, 0, 1, 0], [0, 0, 0, -1], [-1, 0, 0, 0], [0, 1, 0, 0]])
GAM = [g0, g1, g2, g3]
ETA = sp.diag(1, -1, -1, -1)
ok_clifford = all(sp.simplify(GAM[i] * GAM[j] + GAM[j] * GAM[i]
                              - 2 * ETA[i, j] * sp.eye(4)) == sp.zeros(4, 4)
                  for i in range(4) for j in range(4))
check("the Dirac matrices satisfy the Clifford relation (calibration before use)", ok_clifford)

def cvec(tag):
    """a free complex 4-spinor, held as eight REAL symbols so that conjugation is exact"""
    re_ = sp.symbols(f'{tag}r0:4', real=True)
    im_ = sp.symbols(f'{tag}i0:4', real=True)
    return sp.Matrix([re_[i] + sp.I * im_[i] for i in range(4)])


m = sp.Symbol('m', real=True)
Psi = cvec('p')
dPsi = [None] + [cvec(f'd{k}') for k in (1, 2, 3)]       # the SPATIAL derivatives are free data
spatial = sp.zeros(4, 1)
for k in (1, 2, 3):
    spatial += GAM[k] * dPsi[k]
# the time derivative is not free: i gamma^mu d_mu Psi = m Psi fixes it
ON_SHELL = sp.expand(-sp.I * g0 * (m * Psi - sp.I * spatial))
bar = lambda v: v.conjugate().T * g0


def divergence(dt):
    d = [dt] + dPsi[1:]
    return sp.expand(sum((bar(d[mu]) * GAM[mu] * Psi)[0, 0]
                         + (bar(Psi) * GAM[mu] * d[mu])[0, 0] for mu in range(4)))


div_onshell = sp.simplify(divergence(ON_SHELL))
div_off = sp.simplify(divergence(ON_SHELL + sp.Matrix([1, 0, 0, 0])))
dens = sp.simplify(sp.expand((bar(Psi) * GAM[0] * Psi)[0, 0]))
print()
print(f"    d_mu ( Psi-bar gamma^mu Psi )  ON SHELL   =  {div_onshell}")
print(f"    CONTROL, the same sum OFF shell           =  {div_off}      <- fires")
print(f"    and the density it counts, j^0            =  {dens}")
check("the phase's Noether current is conserved classically -- there IS a spacetime current",
      div_onshell == 0)
check("CONTROL: break the Dirac equation and the divergence stops vanishing",
      div_off != 0)
check("the conserved density is |Psi|^2 -- a COUNT, non-negative, not a signed charge",
      sp.simplify(dens - sum(s ** 2 for s in Psi.free_symbols)) == 0)
print("""
  * The determinant circle acts on the leaf as a COMMON PHASE on the three seat amplitudes,
    Psi = sum_j c_j psi_j with c_j -> e^{i vartheta} c_j.  A common phase on a field is a symmetry
    of the action and has an ordinary Noether current; it needs no bundle, no frame, and no
    connection.  ** That is why Q1 is positive here and was negative at r6752: a gauge field wants a
    connection over a member's spacetime, and a conserved count wants only a phase. **
    The coefficient is the one computed in Part 3: A = 3.
""")

# =========================================================================================
print("=" * 94)
print("PART 5 (Q2) — THE SOURCE IS ZERO ON THE WHOLE STATIC FAMILY, NOT ON THREE SAMPLED MEMBERS")
print("=" * 94)
print("""
  The order asks for the static members by computation rather than by argument.  Computed here with
  the profiles left as ARBITRARY FUNCTIONS, so the answer covers Schwarzschild, Schwarzschild--de
  Sitter, Nariai and every other static member of the corpus's family at once.
""")
f = sp.Function('f')(r)
h = sp.Function('h')(r)
S_ = sp.Function('S')(r)
U_ = sp.Function('U')(r, th)
K_ = sp.Function('K')(r, th)

STATIC = {
    "static spherical, f ARBITRARY          -f dt^2 + dr^2/f + r^2 dOmega^2":
        sp.diag(-f, 1 / f, r ** 2, r ** 2 * sp.sin(th) ** 2),
    "static spherical, f, h, areal S ARBITRARY":
        sp.diag(-f, h, S_ ** 2, S_ ** 2 * sp.sin(th) ** 2),
    "static AXISYMMETRIC Weyl form, U, K ARBITRARY":
        sp.diag(-sp.exp(2 * U_), sp.exp(2 * K_ - 2 * U_), sp.exp(2 * K_ - 2 * U_),
                sp.exp(-2 * U_) * r ** 2 * sp.sin(th) ** 2),
}
for name, gm in STATIC.items():
    val = sp.simplify(pontryagin(gm, [t, r, th, ph], simp=sp.simplify))
    print(f"    {name}\n      *RR = {val}")
    check(f"*RR vanishes IDENTICALLY: {name.split(',')[0]}", val == 0)

# and the corpus's own named static members, as instances rather than as separate results
M_, al = sp.symbols('M alpha', positive=True)
NAMED = {
    'Schwarzschild          f = 1 - 2M/r': 1 - 2 * M_ / r,
    'Schwarzschild--de Sitter f = 1 - 2M/r - r^2/alpha^2': 1 - 2 * M_ / r - r ** 2 / al ** 2,
    'de Sitter              f = 1 - r^2/alpha^2': 1 - r ** 2 / al ** 2,
    'Nariai member          f at 2M = 2 alpha/(3 sqrt 3)':
        1 - 2 * (al / (3 * sp.sqrt(3))) / r - r ** 2 / al ** 2,
}
print()
for name, fv in NAMED.items():
    val = sp.simplify(pontryagin(sp.diag(-fv, 1 / fv, r ** 2, r ** 2 * sp.sin(th) ** 2),
                                 [t, r, th, ph], simp=sp.simplify))
    print(f"    {name:<52} *RR = {val}")
    check(f"*RR = 0 on {name.split()[0]}", val == 0)
print("""
  * ** A zero is a result (W5), and this one is a family-wide identity. **  Not "the static members
    the corpus happens to use return zero" but "no static member can return anything else": the
    density is a pseudoscalar and a static metric has a hypersurface-orthogonal timelike Killing
    field, so there is nothing for the orientation to be measured against.  The computation is what
    establishes that, with the profiles never specified.
""")

# =========================================================================================
print("=" * 94)
print("PART 6 (Q3) — THE TWISTED MEMBER: NONZERO, AND EXACTLY ODD IN THE TWIST, IN GENERAL")
print("=" * 94)
print("""
  P11's unpolarised Gowdy--de Sitter member, with A, psi, omega, R left as ARBITRARY functions of
  (t, z).  The density is graded by the twist: omega -> varepsilon omega and the powers of
  varepsilon that survive are read off.  ** If any EVEN power appeared, or bare omega occurred, the
  density would not be odd in the twist and W4 says that would indicate an error. **
""")
A_ = sp.Function('A')(t, z)
psi_ = sp.Function('psi')(t, z)
om_ = sp.Function('omega')(t, z)
R_ = sp.Function('R')(t, z)
gG = gowdy_unpolarised(A_, psi_, om_, R_)
PG = sp.simplify(pontryagin(gG, [t, z, x, y],
                            simp=lambda e: sp.cancel(sp.powsimp(sp.expand(e)))))

check("the general unpolarised member's *RR is NOT zero", PG != 0)

eps_ = sp.Symbol('varepsilon')
num, den = sp.fraction(sp.together(sp.simplify(PG.subs(om_, eps_ * om_).doit())))
powers = sorted(set(d[0] for d in sp.Poly(sp.expand(num), eps_).monoms()))
print(f"    powers of the twist grading present:  {powers}")
check("the powers present are exactly {1, 3} -- ALL ODD, no even power at all",
      powers == [1, 3])

wt = [om_, sp.diff(om_, t), sp.diff(om_, z), sp.diff(om_, t, t),
      sp.diff(om_, z, z), sp.diff(om_, t, z)]
monoms = sp.Poly(sp.expand(sp.fraction(sp.together(PG))[0]), *wt).monoms()
check("bare omega never appears -- only its DERIVATIVES (degree 0 in omega itself)",
      set(mo[0] for mo in monoms) == {0})
check("every monomial has ODD total degree in the twist variables",
      all(sum(mo) % 2 == 1 for mo in monoms))
check("so *RR(-omega) = -*RR(omega), EXACTLY",
      sp.simplify(PG.subs(om_, -om_).doit() + PG) == 0)
check("and *RR == 0 identically when omega is constant -- P11's POLARISED cut",
      sp.simplify(PG.subs(om_, sp.Symbol('omega0', real=True)).doit()) == 0)

# an explicit member, so the nonzero is exhibited and not only argued
c = sp.Symbol('c', real=True)
gR = gowdy_unpolarised(t / 3, z / 5, c * t * z, t)
PR = sp.simplify(pontryagin(gR, [t, z, x, y], simp=sp.simplify))
print()
print("    an explicit member  (A, psi, omega, R) = (t/3, z/5, c t z, t):")
print(f"      *RR = {PR}")
check("explicit member: *RR is nonzero", sp.simplify(PR) != 0)
check("explicit member: *RR is odd in c", sp.simplify(PR.subs(c, -c) + PR) == 0)
check("explicit member: *RR vanishes at c = 0", sp.simplify(PR.subs(c, 0)) == 0)
print("""
  * P11's conserved twist is c = R e^{2P} Q_t, LINEAR in omega's derivative, and C50's orientation
    parity acts as c -> -c.  So "odd in omega's derivatives" IS "odd in c", and the two statements
    are one.  ** W4 is met on the GENERAL member: the oddness is a property of the form, not of the
    representative, which is what makes the check worth anything. **
""")

# =========================================================================================
print("=" * 94)
print("PART 7 (Q4) — IS THERE INFLOW?  NO, ON TWO INDEPENDENT GROUNDS")
print("=" * 94)
print("""
  The order's distinction is the load-bearing one: whether the construction HAS a bulk gravitational
  Chern--Simons term, not whether one could be added.  Tested two ways -- against the corpus's own
  text, and against what the inflow term would need as an ingredient.
""")
papers = sorted(p for p in os.listdir(os.path.join(ROOT, 'corpus'))
                if p.endswith('.tex') and not p.startswith('appendix_'))
hits = {}
for p in papers:
    with open(os.path.join(ROOT, 'corpus', p), encoding='utf-8') as fh:
        body = fh.read()
    n = len(re.findall(r'Chern[-—–]{1,2}Simons', body))
    if n:
        hits[p] = n
print(f"    papers scanned: {len(papers)}")
print(f"    occurrences of 'Chern--Simons' in any of them: {sum(hits.values())}   {hits}")
check("the corpus's papers contain NO Chern--Simons term anywhere",
      sum(hits.values()) == 0)

with open(os.path.join(ROOT, 'corpus', 'geometric_core_paper.tex'), encoding='utf-8') as fh:
    core = fh.read()
declines = ("the ledger counts no counterterm coefficient" in
            open(os.path.join(ROOT, 'corpus', 'canonical_time.tex'), encoding='utf-8').read())
check("P10's parity-odd caveat says in terms that the ledger counts no counterterm coefficient",
      declines)
check("and P17's constant ledger places a topological term's coefficient outside it",
      "A topological term's coefficient is of the third kind" in core)
print("""
    (ii) the STRUCTURAL ground, which does not depend on reading the text at all:
         an inflow term for a mixed U(1)-gravitational anomaly is  integral_5 A ^ tr(R ^ R).
         It needs a ONE-FORM GAUGE POTENTIAL A for the circle.  r6752 established there is none
         over a member's spacetime -- the seats are a section, not a frame.
         ** So the term's ingredient is absent, not merely its coefficient unset. **
""")
prior = os.path.join(ROOT, 'receipts', 'P14_matter_sector_paper',
                     'P14_the_seats_are_a_section_not_a_frame_so_there_is_no_spacetime'
                     '_connection_to_curve.py')
with open(prior, encoding='utf-8') as fh:
    prior_body = fh.read()
check("r6752's receipt is on disk and does rule out a spacetime connection, in its own words",
      os.path.exists(prior)
      and 'THERE IS NO SUCH BUNDLE' in prior_body
      and 'nothing for a curvature to be the curvature of' in prior_body
      and prior_body.count('no spacetime bundle') >= 1)

# =========================================================================================
print("=" * 94)
print("PART 8 (Q5) — THE VERDICT, AND THE RATE AS A BOUNDARY QUANTITY")
print("=" * 94)
print("""
  The source is a total derivative -- the divergence of the gravitational Chern--Simons current.
  That is a theorem, and it is MEASURED here rather than cited, on the explicit twisted member,
  because it is what turns "at what rate" into a finite number rather than a density.
""")
K = cs_current(gR, [t, z, x, y], simp=sp.simplify)
divK = sp.simplify(sum(sp.diff(K[i], [t, z, x, y][i]) for i in range(4)))
dens = sp.simplify(PR * sp.sqrt(-sp.simplify(gR.det())))
ratio = sp.simplify(divK / dens)
print(f"    (d_mu K^mu) / (sqrt(-g) *RR)  =  {ratio}")
check("d_mu K^mu is nonzero on the twisted member", sp.simplify(divK) != 0)
check("the ratio is a CONSTANT, not a function -- so sqrt(-g) *RR = -d_mu K^mu exactly",
      ratio.free_symbols == set() and sp.simplify(ratio + 1) == 0)
check("and the Chern--Simons current's divergence is itself odd in the twist",
      sp.simplify(divK.subs(c, -c) + divK) == 0)

print(f"""
  ** THE VERDICT. **  The count is not simply conserved and not simply violated; which it is, is a
  property of the member, and that is the answer rather than an evasion.

    on EVERY STATIC member       *RR == 0 identically, for arbitrary profiles
                                 -> the count is EXACTLY conserved, not approximately
    on the TWISTED member        *RR nonzero, exactly odd in the twist
                                 -> the count is VIOLATED, and the twist is what violates it

  ** THE RATE. **  With the standard normalisation of the mixed anomaly and the coefficient
  A = {COEFF["P14's wall content   ker_+ = 3 seats, ker_- = 0"]} computed in Part 3,

      d_mu j^mu  =  (A / 384 pi^2) *RR ,        A = 3

  and since sqrt(-g) *RR = -d_mu K^mu the integrated violation between two slices is a BOUNDARY
  quantity rather than a secular accumulation:

      Delta N  =  -(3 / 384 pi^2) [ integral K^0 d^3x ]

  the change in the member's GRAVITATIONAL CHERN--SIMONS NUMBER.  Its three properties are the
  three results above: it is zero on every static member, it is odd in the twist, and it is
  identically zero at c = 0.  At small twist it is linear in c, the grading's degree-one part.
""")

# =========================================================================================
print("=" * 94)
print("THE BOUND")
print("=" * 94)
print("""
  Q1  ** YES, THERE IS A SPACETIME CURRENT, AND THE COEFFICIENT IS 3. **  The determinant circle
      acts on the leaf as a common phase on the three seat amplitudes; a common phase is a symmetry
      of the action with an ordinary Noether current, conserved classically (checked on explicit
      Dirac matrices).  It needs no bundle -- which is exactly why r6752's negative does not carry
      over: D(g Psi) = g D Psi + (dg) Psi kills a LOCAL rotation and is silent on dg = 0.  The
      coefficient is the linear trace sum_+ q - sum_- q = 3 - 0 = 3.

  Q2  ** ZERO, AND ON THE WHOLE STATIC FAMILY. **  Computed with arbitrary profiles: static
      spherical with f free, with f, h and the areal radius free, and the static axisymmetric Weyl
      form with U, K free -- *RR == 0 identically in every case, hence on Schwarzschild,
      Schwarzschild--de Sitter, de Sitter and Nariai as instances.  By computation, not by argument.

  Q3  ** NONZERO ON THE TWISTED MEMBER, AND EXACTLY ODD IN c. **  On the general unpolarised
      Gowdy--de Sitter form with four arbitrary functions, bare omega never appears and every
      monomial has odd total degree in omega's derivatives, the powers present being {1, 3}.  So
      *RR(-omega) = -*RR(omega) exactly, and *RR == 0 on the polarised cut.  Kerr is the precedent
      and it is reproduced in Part 1, including its factorisation.

  Q4  ** NO INFLOW.  The construction does not have a bulk gravitational Chern--Simons term. **
      Two independent grounds: the corpus's papers contain no such term and the one place a
      topological coefficient is weighed explicitly declines it; and the inflow term needs a
      one-form gauge potential for the circle, which r6752 showed does not exist over a member's
      spacetime.  The ingredient is missing, not merely the coefficient unset.

  Q5  ** VIOLATED, BY THE TWIST, AND AT A RATE THAT IS A BOUNDARY QUANTITY. **  Exactly conserved
      on every static member; violated on the twisted one at d_mu j^mu = (3/384 pi^2) *RR.  Since
      sqrt(-g) *RR = -d_mu K^mu -- measured, the ratio a constant -1 and not a function -- the
      integrated violation is the change in the member's gravitational Chern--Simons number, odd in
      the twist and identically zero without it.

  ⚠ NOT A DEFECT (W2).  The determinant circle is a GLOBAL symmetry; r6752 closed the gauging.  A
  global current with a nonzero mixed gravitational anomaly is an ordinary, consistent situation and
  is reported as one.  W3's contrast is that the Standard Model's corresponding trace is vector-like
  and this one is not, and the reason is dim ker_- = 0 (C3, where the sign is shown to be the
  convention and the non-vanishing shown not to be).

  ⚠ NOT CLAIMED: that the coefficient's universal prefactor is this construction's -- 1/384 pi^2 is
  standard and only A = 3 is derived here; that any inflow term could not be added, only that the
  construction does not have one; and nothing about cosmological consequences, which the order does
  not ask.  ** Nothing is named (W6). **  The global group (r6742), the gauging's status (r6747,
  r6748, r6752) and weak isospin are untouched.
""")
print(f"  {len(_checks)} checks, all pass." if all(_checks) else "  FAILURES PRESENT")
assert all(_checks)
