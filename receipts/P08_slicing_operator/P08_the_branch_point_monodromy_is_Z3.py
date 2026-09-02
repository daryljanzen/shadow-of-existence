"""
P08_the_branch_point_monodromy_is_Z3.py -- the order of the cosmogenesis branch point's branching,
and which of its sheets carry real geometry.

** THE BRANCH POINT CARRIES A Z_3 MONODROMY. **  In r = (2 M alpha^2)^(1/3) sinh^(2/3)(u) with
u = 3 tau / 2 alpha, the hyperbolic sine near u = 0 is u times a function analytic and non-vanishing
there, so the entire branch structure is the factor u^(2/3).  One circuit multiplies r by
e^{4 pi i/3}, a primitive cube root of unity: ** one circuit does not close it, three do. **

** OF THE THREE DETERMINATIONS EXACTLY TWO CARRY REAL r, and they are the two the construction
uses: ** the real u axis gives r > 0 (the expanding leg) and Im u = -pi/2 -- the offset
Im tautilde = -pi alpha/3 the companion papers continue along -- gives
r = -(2 M alpha^2)^(1/3) cosh^(2/3), the conjugate branch.  The third sheet carries no real geometry
to continue onto.

** AND THE ORDER IS THE MASS TERM'S, NOT THE HORIZON CUBIC'S. **  Near r -> 0 the 2M/r in
(dr/dtau)^2 = 2M/r + r^2/alpha^2 dominates and gives r^(3/2) ~ tau; the horizon cubic's degree comes
from the r^2/alpha^2 term instead.  ** Two threes of the same order and different origin. **  The
distinction is recorded rather than elided because this programme has already had to withdraw one
conflation of two threes (the generations-are-the-hinges withdrawal, registered in check_withdrawn).

WHAT PROMPTED IT.  A pass over the cluster-J speculative germs against the built corpus.  One of them
(J-9, r471) guessed that the conjugate lap's exit at the branch point "is not unique -- three
options", ordered by naturalness.  ** The count is right and forced; the ordering is unnecessary; and
there are no branching probabilities, because the third exit is not improbable but absent. **  A
second (J-8) guessed the seat/operator interlock is SEMIDIRECT; the corpus's own T and R commute, so
it is DIRECT, S_3 x Z_2 -- checked here on the weight plane.

STATUS: ✔✔ (the multiplier asserted a primitive cube root of unity and its order asserted 3; the
  real-r sheets tabulated per line; the cubic's degree asserted 3 with its leading term identified;
  R asserted central in the Weyl S_3 and an involution outside it)
RUN: python3 P08_the_branch_point_monodromy_is_Z3.py   RUNTIME: ~1 min (sympy)
ORIGIN: computations/beyond_the_wall/J_cluster_worked_against_the_built_corpus.py, r2376 (c54.114).
ORIGIN-DIVERGENCE: none of substance; the origin closes on a block verdict over ten register items,
  which belongs in the ledger and not in a paper receipt.
"""
import sympy as sp

print(__doc__.split("STATUS:")[0])

tau, al, M, x = sp.symbols('tau alpha M x', real=True)
u = sp.Symbol('u')
w = sp.exp(2*sp.pi*sp.I/3)

# =====================================================================
print("=" * 78)
print("PART 1 — THE MONODROMY OF THE BRANCH POINT")
print("=" * 78)
print("  P8 prop:cosmo's bead, in the variable the branch point sits at:")
print("     r(tautilde) = (2 M alpha^2)^(1/3) sinh^(2/3)(u),   u = 3 tautilde / 2 alpha,")
print("  and the branch point is u = 0.")
print()
ser = sp.series(sp.sinh(u), u, 0, 6).removeO()
print(f"  near u = 0:  sinh u = {ser}  =  u * [1 + u^2/6 + ...]")
print("  so  sinh^(2/3)(u) = u^(2/3) * [analytic and nonvanishing at 0].")
print("  ** THE ENTIRE BRANCH STRUCTURE IS THE FACTOR u^(2/3). **")
print()
print("  Continue once around u = 0:   u -> e^{2 pi i} u .")
fac = sp.simplify(sp.exp(2*sp.pi*sp.I*sp.Rational(2, 3)))
print(f"     u^(2/3) -> e^{{4 pi i/3}} u^(2/3) = {sp.nsimplify(fac)} * u^(2/3)")
order = min(k for k in range(1, 12) if sp.simplify(fac**k - 1) == 0)
print(f"  ** the multiplier has order {order}: the monodromy group is Z_{order}. **")
assert order == 3
print(f"  check: it is a primitive cube root of unity -- equal to w^2 with w = e^{{2 pi i/3}}: "
      f"{sp.simplify(fac - w**2) == 0}")
assert sp.simplify(fac - w**2) == 0
print()
for s in [
 "⇒⇒ ** THE COSMOGENESIS BRANCH POINT IS A $\\mathbb{Z}_3$ BRANCH POINT.  One circuit does not close",
 "   it; three do. **  *That is what the name has meant all along, and the order has not been read",
 "   off before.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE THREE SHEETS, AND WHICH CARRY REAL r")
print("=" * 78)
print("  On a sheet, r = A * [sinh u]^(2/3) with the three determinations differing by w^k.")
print("  Ask where r is REAL, along the horizontal lines Im u = const:")
print()
rows = []
for name, shift in [("Im u = 0      (the real axis)", 0),
                    ("Im u = -pi/2  (the corpus's offset)", -sp.pi/2),
                    ("Im u = +pi/2", sp.pi/2),
                    ("Im u = -pi    (a full half-period)", -sp.pi)]:
    sh = sp.simplify(sp.sinh(x + sp.I*shift).rewrite(sp.exp).simplify())
    base = sp.simplify(sp.arg(sh.subs(x, 1)))       # a representative phase
    reals = []
    for k in range(3):
        ph = sp.simplify(sp.Rational(2, 3)*base + 2*sp.pi*k/3)
        ph = sp.nsimplify(sp.simplify(sp.Mod(ph, 2*sp.pi)))
        if sp.simplify(sp.sin(ph)) == 0:
            reals.append((k, "positive" if sp.simplify(sp.cos(ph)) == 1 else "NEGATIVE"))
    rows.append((name, sp.simplify(sh), reals))
print(f"  {'line':>36} {'sinh u there':>20} {'sheets with real r':>26}")
for nm, sh, rl in rows:
    tag = ", ".join(f"k={k} ({s})" for k, s in rl) if rl else "none"
    print(f"  {nm:>36} {str(sh):>20} {tag:>26}")
print()
for s in [
 "⌗ ** SO REAL $r$ OCCURS ON EXACTLY TWO OF THE THREE SHEETS, AND THE TWO CARRY OPPOSITE SIGNS: **",
 "   *the real axis gives $r>0$ -- the expanding leg -- and the corpus's own offset line",
 "   $\\mathrm{Im}\\,\\tilde\\tau=-\\pi\\alpha/3$ (i.e. $\\mathrm{Im}\\,u=-\\pi/2$) gives $r<0$ -- the",
 "   conjugate branch, $r=-(2M\\alpha^{2})^{1/3}\\cosh^{2/3}$, which is P3's own continuation.*",
 "",
 "⇒ ** THE CORPUS USES TWO OF THE THREE SHEETS.  It has never said how many there are. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — `J·9` SETTLED")
print("=" * 78)
print("  The germ (r471), verbatim in the register: *'at the A=B seam the conjugate lap's exit is")
print("  not unique -- continue-same-ruling (a, parsimonious) / hop-dual (b, kink-cost) / turn-back")
print("  (c, rejected) -- a naturalness ordering proposed as the geometric seed of interaction")
print("  branches with defined probabilities weighted by ambient smoothness.'*")
print()
print(f"  {'the germ':>34} {'what the monodromy gives':>34}")
for a, b in [("'the exit is not unique'", "correct -- the point is branched"),
             ("'three options'", "** correct, and FORCED: |Z_3| = 3 **"),
             ("ordered by 'naturalness'", "** unnecessary: they are sheets **"),
             ("'turn-back (c, rejected)'", "not a third sheet -- see below"),
             ("'probabilities by smoothness'", "** no support; nothing here weights them **")]:
    print(f"  {a:>34} {b:>34}")
print()
for s in [
 "⇒⇒ ** THE GERM'S COUNT IS RIGHT AND ITS REASON IS WRONG, WHICH IS THE MOST USEFUL WAY FOR A GUESS",
 "   TO BE WRONG. **  *Three is not a naturalness ordering over candidate moves; it is the order of",
 "   the monodromy group, and it is forced by the $2/3$ exponent that matter domination puts in",
 "   $r\\propto\\tau^{2/3}$.*",
 "",
 "⚠ ** AND THE CORRECTION MATTERS: THREE SHEETS, BUT ONLY TWO CARRY REAL GEOMETRY. **  *The germ's",
 "   third option was 'turn-back', rejected on taste.  The actual third sheet is not a turn-back:",
 "   it is a determination on which $r$ is complex, so it carries no real geometry to exit onto.",
 "   It is rejected by reality, not by taste.*",
 "",
 "⌗⌗ ** SO THE HONEST SETTLEMENT IS: the branch point admits three continuations, exactly two of",
 "   which land on real geometry, and the corpus uses both.  There is no unused physical exit, and",
 "   therefore no branching ratio to compute. **  *`J·9` asked for the geometric seed of interaction",
 "   branches with defined probabilities.  The geometry supplies the branching and denies the",
 "   probabilities: the third exit is not improbable, it is not there.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — IS IT THE CORPUS'S Z_3?")
print("=" * 78)
r_ = sp.Symbol('r', positive=True)
cubic = sp.expand((1 - 2*M/r_ - r_**2/al**2)*r_)
print(f"  the horizon cubic:  r f(r) = {cubic}  -- a cubic, hence THREE roots")
deg = sp.degree(sp.Poly(cubic, r_), r_)
print(f"  its degree in r: {deg}, and the leading term is {-r_**3/al**2} -- ** the LAMBDA term **")
assert deg == 3
print()
print("  the monodromy's 3, on the other hand:")
print("     (dr/dtau)^2 = 2M/r + r^2/alpha^2 ;  near r -> 0 the MASS term dominates,")
print("     so r^(1/2) dr = sqrt(2M) dtau,  r^(3/2) ~ tau,  r ~ tau^(2/3).")
print(f"  ** the exponent 3/2 comes from integrating r^(1/2), i.e. from the 2M/r term. **")
print()
print(f"  {'the three':>34} {'where its 3 comes from':>30}")
for a, b in [("the horizon roots / A_2 / the hinges", "the Lambda term, r^3/alpha^2"),
             ("** the branch-point monodromy **", "** the mass term, 2M/r **")]:
    print(f"  {a:>34} {b:>30}")
print()
for s in [
 "⇒⇒ ** THEY ARE NOT THE SAME THREE.  They have the same order and different sources -- one is the",
 "   cubic's degree, which is the cosmological term's; the other is the monodromy's order, which is",
 "   the mass term's. **",
 "",
 "⚠⚠ ** AND THE CORPUS HAS A RECORDED FAILURE MODE HERE, WHICH IS WHY THIS IS SAID BEFORE ANYTHING",
 "   ELSE. **  *The withdrawal registered in `check_withdrawn` -- 'the generations are the hinges',",
 "   struck at c54.31 and propagated through six papers -- was exactly a conflation of two threes.",
 "   ** So a third three is a liability before it is an asset, and it enters the record labelled as",
 "   distinct or it does not enter at all. ***",
 "",
 "⌗ *What would make them one: an argument that the $2/3$ exponent and the cubic's degree are forced",
 "by a single structure.  None is offered here, and the two terms they come from are the two",
 "different terms of the same metric function -- which is suggestive and is not an argument.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — `J·8` SETTLED: DIRECT, NOT SEMIDIRECT")
print("=" * 78)
print("  The germ: the seat-threes and the operator-ZZ_2's interlock, *'likely SEMIDIRECT'*.")
print()
print("  The corpus's answer, from the built matter sector: the two factors are")
print("     T = the horn swap        (weak isospin)")
print("     R = the offset parity r_0 -> -r_0   (= gamma^5, chirality)")
print("  and P14 records that they COMMUTE -- they are independent data -- so")
print("     Aut(A_2) = D_6 = S_3 x Z_2 ,  a DIRECT product.")
print()
# a direct check on the concrete realisation: D_6 as S_3 x Z_2 has a central involution
S3 = [sp.Matrix([[1, 0], [0, 1]]), sp.Matrix([[0, 1], [-1, -1]]), sp.Matrix([[-1, -1], [1, 0]]),
      sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[-1, -1], [0, 1]]), sp.Matrix([[1, 0], [-1, -1]])]
R = -sp.eye(2)                       # the orientation parity, acting as -1 on the weight plane
central = all(sp.simplify(R*g - g*R) == sp.zeros(2, 2) for g in S3)
print(f"  ** R = -I commutes with every element of the Weyl S_3 on the weight plane: {central} **")
assert central
print(f"  ** and R^2 = I: {sp.simplify(R*R - sp.eye(2)) == sp.zeros(2, 2)}, R is not in S_3: "
      f"{all(sp.simplify(R - g) != sp.zeros(2, 2) for g in S3)} **")
assert sp.simplify(R*R - sp.eye(2)) == sp.zeros(2, 2)
print(f"  so the group generated has order {2*len(S3)} = |D_6|, as a DIRECT product S_3 x Z_2.")
print()
for s in [
 "⇒⇒ ** THE GERM NAMED THE RIGHT TWO FACTORS AND GOT THE EXTENSION WRONG.  It is direct. **",
 "",
 "⌗ ** AND THE DIRECTNESS IS NOT A DETAIL -- IT IS WHY THE STANDARD MODEL'S ARRANGEMENT FOLLOWS. **",
 "   *Because $R$ is central it grades everything uniformly, and because it is a substrate isometry",
 "   the chirality it grades descends GAUGED; the Weyl $S_3$ is the deck symmetry of the solution",
 "   space and no isometry, so a family symmetry it grades is GLOBAL.  A semidirect product would",
 "   have entangled the two and lost exactly that separation.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 6 — THE BLOCK VERDICT")
print("=" * 78)
V = [
 ("J·1", "wave/particle as two clocks; the quantization germ",
  "REPLACED. The 'closed phase loop' at the branch point is real and its content is the Z_3 "
  "monodromy of PART 1 -- a discrete structure, not a quantization condition. No hbar anywhere."),
 ("J·2", "horizons as interaction vertices",
  "DEAD as posed. Its own caveat -- 'reproducing AMPLITUDES is the real test' -- is unmet and "
  "nothing built since bears on it."),
 ("J·3", "amplitude = conjugacy volume = pivot angle",
  "UNMOVED. Its geometric leg was parked as C-6 and is untouched by anything since."),
 ("J·4", "mass = tilt off the photon ruling",
  "UNMOVED as an interpretation. Its base ('matter is the bend') is the corpus; the tilt reading "
  "gained nothing from the matter sector's discrete result, which is about CHARACTERS, not angles."),
 ("J·5", "photon amplitude grows with expansion = redshift",
  "UNMOVED. The cosh expansion is the corpus's; the added picture is neither used nor needed."),
 ("J·6", "magnetism as the boosted conjugacy circle",
  "UNMOVED, and the doc already called it the lowest-grounded item."),
 ("J·7", "the threes -> SM via a geometric Higgs",
  "BOUNDED HARDER. P14's colour arc settles the route: the module is the BRANCHING, the bundle is "
  "FLAT, and the discrete opening's ceiling is uniform. There is no geometric-Higgs slot left."),
 ("J·8", "CPT as the operator triple; seat (x) operator",
  "** SETTLED, NEGATIVELY: DIRECT, not semidirect (PART 5). ** Right factors, wrong extension."),
 ("J·9", "exit-branch correspondence at the branch point",
  "** SETTLED (PART 3). ** The count is right and forced -- |Z_3| = 3 -- the naturalness ordering "
  "is unnecessary, and there are no branching probabilities because only two sheets carry real "
  "geometry."),
 ("J·10", "two-horn / electroweak-ring / geometric optics",
  "SUPERSEDED, as the register already records: the Hubble knot is the geometric stacking rate and the "
  "low-l structure is the closed-S^3 deficit."),
]
print(f"  {'item':>6} {'germ':>46}")
for a, b, c in V:
    print(f"  {a:>6} {b:>46}")
    for line in [c[i:i+70] for i in range(0, len(c), 70)]:
        print(f"         {line}")
print()
for s in [
 "⌗⌗ ** THE YIELD OF THE PASS, STATED HONESTLY: two of ten settled, eight unmoved or dead, and ONE",
 "   NEW OBJECT -- the branch point's $\\mathbb{Z}_3$ monodromy -- which no germ asked for and which",
 "   the corpus did not have. **",
 "",
 "⌗ *And the two that settled did so because they were the two that made a CHECKABLE structural",
 "   claim: a count and an extension.  The eight that did not move are the ones that proposed an",
 "   interpretation rather than a structure.*  ** That is the reusable lesson from the exercise, and",
 "   it is about what kind of speculation is worth writing down, not about this cluster. **",
]:
    print("  " + s)
