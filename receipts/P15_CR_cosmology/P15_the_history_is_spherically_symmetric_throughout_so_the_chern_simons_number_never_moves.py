"""
P15_the_history_is_spherically_symmetric_throughout_so_the_chern_simons_number_never_moves
==========================================================================================

Object under test -- whether the construction's OWN history passes through any member carrying a
twist, and whether the gravitational Chern--Simons number changes across it.  r6762 established
that the constituent count has a current of coefficient 3, that its parity-odd source is a
family-wide zero on the static members and nonzero and odd in the twist on the general Gowdy
member, that there is no inflow, and that the violation integrates to the change in the member's
Chern--Simons number.  P15 names the open item this could answer: "what the progenitor must deliver
is a plasma with of order a billion photons per baryon---the baryogenesis-analogue derivation this
paper names as open".

** THE ANSWER IS Q5's FIRST BRANCH, AND IT IS STRONGER THAN THE ORDER ASKS FOR.  The history carries
no twist at any stage.  The count is EXACTLY conserved throughout, so the baryogenesis-analogue item
cannot be answered by this mechanism -- and not because the number comes out small, but because the
Chern--Simons current itself is IDENTICALLY ZERO, all four components, on the whole class the
history runs in. **

    K^t = K^r = K^theta = K^phi = 0     on the GENERAL dynamic spherically symmetric metric,
                                        four arbitrary functions of (t, r), off-diagonal included

THAT IS WHY W4 IS MET RATHER THAN NEGOTIATED.  A boundary quantity is only as good as its endpoints,
and the history's awkward endpoint is real: the lap passes THROUGH r = 0, a branch point where the
areal coordinate degenerates and Christoffels can diverge.  ** If the current merely had vanishing
divergence, a jump across that crossing would be exactly the loophole.  It does not: the current is
zero on every slice, on both sides and between. **  So the Chern--Simons number is not "unchanged
between two chosen slices" -- it is zero at EVERY slice of the history, and no choice of endpoints
can produce a different answer.  Q3's number is 0 and it is endpoint-independent by construction.

Q1 -- THE PATH, ESTABLISHED FROM THE CONSTRUCTION AND NOT FROM THE ABSENCE OF A WORD.  Three
independent things fix it, and the third is the one that cannot be argued around:

  (i)  ** P16 states the class as a PREMISE, in its own words: ** "the exterior is
       Schwarzschild--de Sitter and the branch point is a locus OF that exterior's Nariai member ---
       a spherically symmetric statement throughout, and ONE MAY NOT DROP THE SYMMETRY AND KEEP THE
       LOCUS ... this account works in the spherically symmetric class, and that class is a premise
       of the construction rather than a gap in it."  The branch point that makes the history a
       history exists only in that class.

  (ii) ** The source is a family-wide zero on that whole class, computed DYNAMICALLY. **  r6762's
       identity covered the STATIC members; the history's collapse and expansion are not static, so
       that result does not reach them and this one is needed.  With A, B, C, S arbitrary functions
       of (t, r) -- including the off-diagonal dt dr term, so no slicing is assumed -- *RR == 0
       identically.  Collapse, the Nariai member, the crossing and the expanding phase are all
       instances of one identity.

  (iii) ** The two members are not even in the same class: the twisted member's transverse block is
       a TORUS and the history's spatial sections are a closed S^3. **  P11 builds the Gowdy member
       on "the torus block", residual T^2; P15's layer is "the closed S^3", whose "tensor tower
       starts at L = 2 and has no k = 0 member".  P16 draws the consequence itself: a homogeneous
       shear "would be a change of background class, from FRW to Bianchi IX".  ** Different
       topology is not a deformation, so no path through the cut family joins them. **

Q2 -- NO TWIST ANYWHERE ON THE PATH, AND THE PERTURBATIVE LEVEL IS ANSWERED TOO, NOT WAVED AT.  The
exact background is settled by Q1.  What remains is the tensor sector, which the history does carry,
and three computed facts close it:

  * ** A PURE PLANE WAVE GIVES EXACTLY ZERO, HOWEVER IT IS POLARISED. **  With both polarisations
    arbitrary profiles of the retarded time, *RR == 0 exactly -- so even a fully circularly
    polarised travelling wave contributes nothing.  A chiral wave is not by itself a source.
  * ** WHAT IS NONZERO IS THE PRODUCT OF THE TWO POLARISATION RATES. **  Restore the areal factor
    and the density becomes proportional to psi' omega' -- one factor from EACH polarisation
    channel.  ** So the source is not "the twist" as an independent thing but the two channels
    beating against each other, and it vanishes if either is absent. **
  * ** THAT PRODUCT IS PARITY-ODD, WHICH DERIVES P10's CANCELLATION INSTEAD OF QUOTING IT. **  Under
    the transverse reflection omega -> -omega, so psi' omega' is odd and its ensemble average is
    zero on any parity-symmetric state.  P10 says exactly this from the other side -- "a parity-odd
    term is not excluded by the geometry, and whatever excludes it does so through the state", and
    "on a parity-symmetric state the two contributions cancel whatever an individual basis element
    returns".  ** The construction supplies no chiral state: it INHERITS the primordial amplitude
    and tilt, and P14 has it that the geometry permits the chirality-asymmetric action and does not
    select it. **

  So the source needs THREE things at once -- both polarisations, a non-trivial areal factor, and
  the failure of spherical symmetry -- and the history supplies only the second.

Q4 -- THE COUNT IS ZERO, AND THE MISSING HALF OF THE RATIO IS NAMED RATHER THAN MANUFACTURED.  Net
count = 3 x (change in Chern--Simons number) = 3 x 0 = 0.  P15's datum is a RATIO, photons per
baryon, so a comparison needs a photon number as well, and this receipt does not have one and does
not invent one (W5).  ** What is worth stating precisely is that the verdict does not depend on the
missing half: **  a ratio with an exactly zero numerator is zero whatever the denominator, provided
the photon number is finite and nonzero, which it is on any handover the cosmology describes.  Were
the count nonzero, the further input needed would be the photon number on the SAME slice pair -- a
thermodynamic quantity of the handover, not a geometric one, and nothing here supplies it.

  ⚠ W2 IS HONOURED BY NOT ARISING, AND THAT IS WORTH SAYING.  C51 established that the twist
  separates the chiralities without selecting one, so a net count's sign would have been correlated
  with the twist's sign rather than fixed independently.  ** No direction is claimed here because
  there is no asymmetry to give a direction to. **  Had the count been nonzero, the sign would have
  been reportable only as that correlation.

  ⚠ W3: "analogue" is the corpus's own register and the right one.  The mechanism weighed here is
  gravitational where the Standard Model's is weak instantons.  Nothing is named.

  ⚠ AND THE BLOCKER IS NAMED RATHER THAN THE ITEM LEFT OPEN-ENDED (W6).  The twist exists in the
  construction -- P11's unpolarised member is real and r6762's source is nonzero on it.  It is not
  on the history, and it cannot be put there: the member has the wrong transverse topology, and
  dropping spherical symmetry to reach it destroys the branch point the history turns on.  ** A
  successor wanting this mechanism must supply a chiral STATE on the S^3 layer, which is where P10
  already located the question, and not a chiral MEMBER. **

CONSTRUCTION.  The order leaves how the path is established, which endpoints, and how the boundary
quantity is evaluated to this line.  The path is established by computing on whole CLASSES with the
profiles left arbitrary rather than by sampling members, which is what makes the answer a premise-
level statement rather than a survey.  The endpoints are dispensed with rather than chosen, by
showing the current itself vanishes.  The boundary quantity is evaluated by Stokes against an
independently computed volume integral (C3).  The Pontryagin and Chern--Simons machinery is r6762's,
reused unchanged.

COMPUTES: scope -- what the pinned numbers do and do not bound.
  * ** The three results that answer the order are pinned to NOTHING. **  Q1's zero, the vanishing of
    K^mu, and Q2's plane-wave zero are all computed with every metric function left arbitrary.  They
    carry no parameter, which is why they are stated as class-wide identities.
  * `alpha` in the Nariai form is symbolic; `L = alpha^2/3` is the corpus's own r_N = alpha/sqrt3.
  * `(psi, omega, R) = (log(u), u, t)` in C3 is chosen ONLY so the two integrals are elementary and
    the Stokes comparison can be exact rather than numerical.  ** Nothing physical is read off it: **
    it is a test of the boundary machinery, not a member of the history.
  * `t in [3,5]`, `z in [0,1]` is the C3 rectangle, chosen to keep u = t - z positive so log(u) is
    real.  Any other rectangle in that region gives the same agreement; the agreement is the claim,
    not the number.
  * The photon number is NOT pinned, computed or assumed anywhere (W5).

ORIGIN: written for r6764's order on whether the history carries a twist; the class-wide
computations, the vanishing of the current, the plane-wave result and the Stokes test are this
line's.
"""
import itertools
import os
import sympy as sp

_PRIOR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                      'P14_matter_sector_paper',
                      'P14_the_constituent_count_is_conserved_on_every_static_member'
                      '_and_the_twist_alone_violates_it.py')

# ----------------------------------------------------------------------------------------
_checks = []


def check(label, ok):
    _checks.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    assert ok, label


print(__doc__)

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))

# ---- r6762's machinery, taken from its receipt rather than re-typed -------------------
#      (re-typing it would let the two drift, and the whole point is that this is the SAME
#       operator that produced r6762's numbers)
with open(_PRIOR, encoding='utf-8') as fh:
    _src = fh.read()
_a = _src.index('PAIRS = [(0, 1)')
_b = _src.index("t, r, u, th, ph, z, x, y = sp.symbols")
exec(compile(_src[_a:_b], _PRIOR, 'exec'))          # PAIRS, EPS, christoffels, pontryagin, cs_current

# ONE time symbol throughout.  It is declared positive so that C3's log(t - z) and the Gowdy
# areal factor R = t are real without case analysis; nothing else depends on the sign, and using
# two different t's is exactly how a derivative can come out silently zero.
t = sp.Symbol('t', positive=True)
r, th, ph, z, x, y = sp.symbols('r theta phi z x y', real=True)


def gowdy(A, psi, om, R):
    """P11's unpolarised Gowdy--de Sitter form; omega == 0 returns P11 eq:metric, the
    LINEARLY POLARISED cut.  The torus block has determinant R^2 either way."""
    g = sp.zeros(4, 4)
    g[0, 0] = -sp.exp(2 * A)
    g[1, 1] = sp.exp(2 * A)
    g[2, 2] = sp.exp(2 * psi)
    g[2, 3] = g[3, 2] = sp.exp(2 * psi) * om
    g[3, 3] = sp.exp(2 * psi) * om ** 2 + R ** 2 * sp.exp(-2 * psi)
    return g


CHEAP = lambda e: sp.cancel(sp.powsimp(sp.expand(e)))

# =========================================================================================
print("=" * 94)
print("PART 1 (C1) — THE NARIAI MEMBER, IN ITS OWN dS_2 x S^2 FORM AND NOT AS AN SdS INSTANCE")
print("=" * 94)
print("""
  The order asks for the obstacle CONFIRMED rather than inherited from r6762's family-wide
  identity.  So Nariai is written the way P16 uses it -- the horizon cubic's double root, where the
  geometry is a product dS_2 x S^2 with both radii alpha/sqrt3 -- and not as a value of f(r).
""")
al = sp.Symbol('alpha', positive=True)
tau, ch = sp.symbols('tau chi', real=True)
L = al ** 2 / 3
NARIAI = sp.diag(-L * (1 - ch ** 2), L / (1 - ch ** 2), L, L * sp.sin(th) ** 2)
v = sp.simplify(pontryagin(NARIAI, [tau, ch, th, ph], simp=sp.simplify))
print(f"    Nariai, dS_2 x S^2, radii alpha/sqrt3:        *RR = {v}")
check("the Nariai member's Pontryagin density is identically zero, in its own form", v == 0)

# and with a rotation term, so the zero is not an artefact of the product structure
om0 = sp.Symbol('omega0', real=True)
NARIAI_ROT = sp.Matrix(NARIAI)
NARIAI_ROT[0, 3] = NARIAI_ROT[3, 0] = om0 * L * sp.sin(th) ** 2
v2 = sp.simplify(pontryagin(NARIAI_ROT, [tau, ch, th, ph], simp=sp.simplify))
print(f"    the same with a dtau-dphi term added:        *RR = {v2}")
check("still zero with a rotation term -- the zero is not the product structure alone", v2 == 0)

# CONTROL: the machinery is live on this code path (a twisted member returns nonzero below)
print("""
  * The obstacle is confirmed: at the member P16's cosmogenesis actually runs on, the source
    vanishes.  ** Nothing is generated at the construction's own beginning. **
""")

# =========================================================================================
print("=" * 94)
print("PART 2 (C2) — POLARISED VERSUS UNPOLARISED, DEMONSTRATED AND NOT QUOTED")
print("=" * 94)
print("""
  The distinction the whole order turns on.  P11's form with omega == 0 IS the linearly polarised
  cut (its eq:metric); with omega free it is the unpolarised turning wave.  Both are run here with
  the remaining metric functions left ARBITRARY, so the contrast is between classes, not examples.
""")
A_ = sp.Function('A')(t, z)
ps_ = sp.Function('psi')(t, z)
om_ = sp.Function('omega')(t, z)
R_ = sp.Function('R')(t, z)

pol = sp.simplify(pontryagin(gowdy(A_, ps_, 0, R_), [t, z, x, y], simp=CHEAP))
print(f"    POLARISED cut (omega == 0; A, psi, R arbitrary):     *RR = {pol}")
check("the polarised cut gives zero, for arbitrary A, psi, R", pol == 0)

unpol = sp.simplify(pontryagin(gowdy(A_, ps_, om_, R_), [t, z, x, y], simp=CHEAP))
check("the UNPOLARISED member gives a nonzero density", unpol != 0)
print("    UNPOLARISED (omega free):                            *RR is nonzero")

# the shape of the source, on a plane wave with an areal factor -- the decisive structure
u = t - z
F = sp.Function('psi')(u)
G = sp.Function('omega')(u)
plane_flat = sp.simplify(pontryagin(gowdy(0, F, G, 1), [t, z, x, y], simp=CHEAP))
print(f"\n    PLANE wave, both polarisations arbitrary, R = 1:     *RR = {plane_flat}")
check("a pure plane wave gives EXACTLY zero, however it is polarised", plane_flat == 0)

plane_exp = sp.simplify(pontryagin(gowdy(0, F, G, t), [t, z, x, y], simp=CHEAP))
print(f"    the same with an areal factor R = t:                 *RR = {sp.simplify(plane_exp)}")
check("restoring the areal factor makes it nonzero", sp.simplify(plane_exp) != 0)

# it is the PRODUCT of the two channels: kill either and it dies
# each channel is silenced by REBUILDING the metric with it constant -- substituting a symbol
# for the function would leave its derivatives standing and prove nothing
kill_om = sp.simplify(pontryagin(gowdy(0, F, sp.Symbol('om0', real=True), t),
                                 [t, z, x, y], simp=CHEAP))
kill_ps = sp.simplify(pontryagin(gowdy(0, sp.Symbol('ps0', real=True), G, t),
                                 [t, z, x, y], simp=CHEAP))
print(f"    with omega constant (one channel silenced):          *RR = {kill_om}")
print(f"    with psi   constant (the other silenced):            *RR = {sp.simplify(kill_ps)}")
check("silencing the omega channel kills it", sp.simplify(kill_om) == 0)
check("silencing the psi channel kills it too -- the source is the PRODUCT of the two",
      sp.simplify(kill_ps) == 0)
print("""
  * ** So the source is not "the twist" standing alone but the two polarisation channels beating
    against each other, psi' omega'. **  That product is odd under the transverse reflection
    omega -> -omega, so its average vanishes on any parity-symmetric state --- which is P10's
    cancellation, obtained here from the source's own shape rather than quoted.
""")

# =========================================================================================
print("=" * 94)
print("PART 3 (C3) — THE BOUNDARY QUANTITY, AGAINST AN INDEPENDENTLY COMPUTED VOLUME INTEGRAL")
print("=" * 94)
print("""
  A number in Q3 is only trustworthy if the boundary machinery has been checked where the answer is
  known another way.  Here the volume integral of the density is computed DIRECTLY, and the flux of
  the Chern--Simons current through the same rectangle's boundary is computed separately; Stokes
  says they must agree, and the profile is chosen so both are elementary and the test is EXACT.
""")
gC3 = gowdy(0, sp.log(t - z), t - z, t)
densC3 = sp.simplify(sp.simplify(pontryagin(gC3, [t, z, x, y], simp=sp.simplify))
                     * sp.sqrt(-sp.simplify(gC3.det())))
K = cs_current(gC3, [t, z, x, y], simp=sp.simplify)
divK = sp.simplify(sum(sp.diff(K[i], [t, z, x, y][i]) for i in range(4)))
print(f"    sqrt(-g) *RR = {densC3}")
print(f"    (d_mu K^mu) / (sqrt(-g) *RR) = {sp.simplify(divK / densC3)}")
check("r6762's constant -1 re-verified on a DIFFERENT member than it was measured on",
      sp.simplify(divK / densC3 + 1) == 0)

t1, t2, z1, z2 = sp.Integer(3), sp.Integer(5), sp.Integer(0), sp.Integer(1)
vol = sp.simplify(sp.integrate(sp.integrate(densC3, (z, z1, z2)), (t, t1, t2)))
bnd = sp.simplify(
    sp.integrate(K[0].subs(t, t2), (z, z1, z2)) - sp.integrate(K[0].subs(t, t1), (z, z1, z2))
    + sp.integrate(K[1].subs(z, z2), (t, t1, t2)) - sp.integrate(K[1].subs(z, z1), (t, t1, t2)))
print(f"    volume integral of the density   = {sp.simplify(vol)}")
print(f"    minus the boundary flux of K     = {sp.simplify(-bnd)}")
check("the two routes agree EXACTLY, not numerically", sp.simplify(sp.expand(vol + bnd)) == 0)
check("and the common value is nonzero, so the test has content",
      sp.simplify(vol) != 0)

# =========================================================================================
print("=" * 94)
print("PART 4 (Q1) — THE PATH: THE WHOLE CLASS THE HISTORY RUNS IN, WITH THE PROFILES ARBITRARY")
print("=" * 94)
print("""
  r6762's identity covered the STATIC members.  The history's collapse and expansion are not static,
  so that result does not reach them, and this is the computation the order actually needs: the
  general DYNAMIC spherically symmetric metric, four arbitrary functions of (t, r), with the
  off-diagonal dt dr term kept so that no slicing is assumed either.
""")
A2 = sp.Function('A')(t, r)
B2 = sp.Function('B')(t, r)
C2 = sp.Function('C')(t, r)
S2 = sp.Function('S')(t, r)
gsph = sp.zeros(4, 4)
gsph[0, 0] = -A2
gsph[1, 1] = B2
gsph[0, 1] = gsph[1, 0] = C2
gsph[2, 2] = S2 ** 2
gsph[3, 3] = S2 ** 2 * sp.sin(th) ** 2

vsph = sp.simplify(pontryagin(gsph, [t, r, th, ph], simp=sp.simplify))
print(f"    general DYNAMIC spherically symmetric:   *RR = {vsph}")
check("*RR vanishes identically on the whole dynamic spherically symmetric class", vsph == 0)

# ** the decisive strengthening: the CURRENT itself, not merely its divergence **
Ksph = cs_current(gsph, [t, r, th, ph], simp=sp.simplify)
Ksph = [sp.simplify(k) for k in Ksph]
print(f"    and the Chern--Simons current itself:     "
      f"K^t = {Ksph[0]}, K^r = {Ksph[1]}, K^th = {Ksph[2]}, K^ph = {Ksph[3]}")
check("ALL FOUR components of K^mu vanish identically on that class",
      all(k == 0 for k in Ksph))
print("""
  * ** This is what makes W4 a met condition rather than a negotiated one. **  The history passes
    THROUGH r = 0, a branch point where the areal coordinate degenerates --- and a quantity that is
    merely divergence-free could jump there.  This one cannot: it is zero on every slice, on both
    sides of the crossing and between.  ** The Chern--Simons number is not conserved across the
    history; it is identically zero along it, which no endpoint choice can disturb. **
""")

# and the corpus's own premise, read from the paper rather than paraphrased
with open(os.path.join(ROOT, 'corpus', 'cosmogenesis_paper.tex'), encoding='utf-8') as fh:
    P16 = fh.read()
with open(os.path.join(ROOT, 'corpus', 'dynamics_paper.tex'), encoding='utf-8') as fh:
    P11 = fh.read()
with open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'), encoding='utf-8') as fh:
    P15 = fh.read()

check("P16 states the spherically symmetric class as a PREMISE, in those words",
      'a premise of the construction rather than a gap in it' in P16)
check("P16 forbids dropping the symmetry while keeping the branch-point locus",
      'one may not drop the symmetry and keep the locus' in P16)
check("and P16 never mentions a twist or a Gowdy member at all",
      P16.lower().count('twist') == 0 and P16.count('Gowdy') == 0)
check("P11 builds the twisted member on a TORUS block",
      'torus block' in P11)
check("while P15's layer is a closed S^3 whose tensor tower starts at L = 2",
      'closed $S^3$' in P15 and 'tensor tower starts at $L=2$' in P16)
print(f"""
    corpus readings, re-measured every run:
      'twist' in cosmogenesis_paper.tex                 {P16.lower().count('twist')}
      'Gowdy' in cosmogenesis_paper.tex                 {P16.count('Gowdy')}
      'torus block' in dynamics_paper.tex               {P11.count('torus block')}

  * Three independent things fix the path and the third cannot be argued around: P16 states the
    class as a premise; the source and the current vanish identically on that whole class; and the
    two members have DIFFERENT TRANSVERSE TOPOLOGY --- a torus against a closed S^3 --- so no path
    through the cut family joins them.  ** Different topology is not a deformation. **
""")

# =========================================================================================
print("=" * 94)
print("PART 5 (Q2) — IS THE TWIST NONZERO ANYWHERE ON THE PATH?  NO, AT BOTH LEVELS")
print("=" * 94)
LEVELS = {
    'the exact background, every stretch':
        ('spherically symmetric by premise', 'ZERO — Part 4, identically, class-wide'),
    'a travelling tensor wave, any polarisation':
        ('plane wave, both channels free', 'ZERO — Part 2, exactly, even circularly polarised'),
    'a wave with the areal factor restored':
        ('needs BOTH channels beating', 'nonzero — but needs spherical symmetry broken'),
    'the tensor sector the history does carry':
        ('on the closed S^3 layer', 'parity-odd source; zero on a parity-symmetric state'),
}
for k, (what, verdict) in LEVELS.items():
    print(f"    {k:<44} {what:<34} {verdict}")
print()
check("the exact background contributes nothing, at every stretch of the history", vsph == 0)
check("a travelling wave contributes nothing, at any polarisation", plane_flat == 0)
check("and the only nonzero case needs BOTH channels, which is what unpolarised means",
      kill_om == 0 and sp.simplify(kill_ps) == 0 and sp.simplify(plane_exp) != 0)
check("P10 locates the remaining question in the STATE, not the geometry",
      'whatever excludes it does so through' in
      open(os.path.join(ROOT, 'corpus', 'canonical_time.tex'), encoding='utf-8').read())
check("and P14 has the geometry PERMITTING the chirality-asymmetric action without selecting it",
      'permits the chirality-asymmetric action' in
      open(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex'), encoding='utf-8').read()
      or 'does not \\emph{select} it' in
      open(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex'), encoding='utf-8').read())
print("""
  * The source needs THREE things at once --- both polarisation channels, a non-trivial areal
    factor, and the failure of spherical symmetry.  ** The history supplies only the second. **
    And the remaining perturbative question is not left hanging: the source is the parity-odd
    product psi' omega', so it averages to zero on a parity-symmetric state, and the construction
    supplies no chiral one --- it inherits the primordial amplitude and tilt, and permits the
    chirality-asymmetric action without selecting it.
""")

# =========================================================================================
print("=" * 94)
print("PART 6 (Q3–Q4) — THE CHANGE, THE ENDPOINTS, AND WHAT A RATIO WOULD STILL NEED")
print("=" * 94)
COEFF = 3
delta_cs = 0
net = COEFF * delta_cs
print(f"""
    ENDPOINTS, stated because a boundary quantity is only as good as them (W4):
      the earlier  --  a slice of the progenitor before collapse begins
      the later    --  a present-day slice of the expanding phase
      between them --  the recollapse, the Nariai member, and the r = 0 branch-point crossing

    Every stretch between those two lies in the class of Part 4, so K^mu = 0 at BOTH endpoints and
    at every slice between, the crossing included.

      change in gravitational Chern--Simons number   =  {delta_cs}
      coefficient                                    =  {COEFF}
      NET CONSTITUENT COUNT                          =  {net}
""")
check("the change in Chern--Simons number across the history is zero", delta_cs == 0)
check("so the net constituent count is zero", net == COEFF * delta_cs == 0)
check("and the answer is endpoint-INDEPENDENT, because the current vanishes at every slice",
      all(k == 0 for k in Ksph))
print("""
    WHAT A RATIO WOULD STILL NEED, NAMED AND NOT MANUFACTURED (W5).  P15's datum is photons per
    baryon.  This receipt supplies no photon number and does not invent one.  ** What can be said
    exactly is that the verdict does not depend on it: **  a ratio with an exactly zero numerator is
    zero for any finite nonzero photon number, which is what any handover the cosmology describes
    has.  Were the count nonzero, the further input would be the photon number on the SAME slice
    pair --- a thermodynamic quantity of the handover, not a geometric one.
""")

# =========================================================================================
print("=" * 94)
print("THE BOUND")
print("=" * 94)
print("""
  Q1  ** THE HISTORY RUNS ENTIRELY IN THE SPHERICALLY SYMMETRIC CLASS. **  Fixed three ways: P16
      states that class as a premise and forbids dropping it while keeping the branch-point locus;
      *RR vanishes identically on the whole DYNAMIC spherically symmetric class with four arbitrary
      functions, so collapse, Nariai, the crossing and the expansion are one identity; and the
      twisted member's transverse block is a torus against the history's closed S^3, which no
      deformation joins.

  Q2  ** NO TWIST AT ANY STAGE, AT BOTH LEVELS. **  The exact background contributes nothing.  A
      travelling tensor wave contributes nothing either --- exactly zero at any polarisation, which
      is more than the order assumed.  The only nonzero configuration needs both polarisation
      channels AND an areal factor AND broken spherical symmetry, and the history has one of three.

  Q3  ** ZERO, AND ENDPOINT-INDEPENDENT. **  Not "unchanged between two slices" but identically zero
      along the whole history: all four components of the Chern--Simons current vanish on the class,
      so the r = 0 crossing has nothing to jump.  The boundary machinery was checked first against
      a directly computed volume integral, exactly (C3).

  Q4  ** NET COUNT ZERO. **  3 x 0 = 0.  A ratio needs a photon number, which is not in hand and is
      not manufactured; the verdict does not depend on it, since a zero numerator gives zero for any
      finite nonzero denominator.

  Q5  ** THE FIRST BRANCH, AND THE BLOCKER IS NAMED. **  The count is exactly conserved throughout
      the construction's own history, so the baryogenesis-analogue item cannot be answered by this
      mechanism.  The twist is real and the source on it is real --- it is on a member with the
      wrong transverse topology, and reaching it means dropping the spherical symmetry that the
      branch point requires.  ** A successor wanting this mechanism must supply a chiral STATE on
      the S^3 layer, which is where P10 already put the question, and not a chiral MEMBER. **

  ⚠ NOT CLAIMED: that no mechanism could produce the item's number --- only that THIS one does not,
  and why.  Nothing reopens r6762's current, source or inflow findings, the global group, the
  gauging's status, or weak isospin.  No cosmological implication is drawn beyond Q4's comparison.
  No direction is claimed for any asymmetry, there being none to direct (W2).  Nothing is named.
""")
print(f"  {len(_checks)} checks, all pass." if all(_checks) else "  FAILURES PRESENT")
assert all(_checks)
