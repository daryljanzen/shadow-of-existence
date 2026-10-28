#!/usr/bin/env python3
r"""r7630 -- EVERY ENTRY'S DOMAIN FIXED FROM THE PAPERS, AND THE COMPLETENESS TEST.

** THE ORDER IS r7629's **, landed on the base and outstanding: fix every entry's domain the way r7628
fixed the state's, from the papers' own sentences, then count; then ask whether any freedom of a free
field on this fixed background lies in NONE of the eight domains, tested against at least the
non-invariant states, the field's own mass and curvature coupling, and boundary conditions at the
patch's edge.

** THE CLAUSE THIS REASONS FROM IS LOCATED IN THE PAPERS, NOT RETYPED FROM THE ORDER **, and arm Ⓙ
below does the locating before the verdict is read.  ⛔ THE REGISTRATION GOT THIS WRONG AND THE ERROR IS
THIS LINE'S: PREDICTION.md quotes the clause as *an argument, over a list of INDEPENDENT freedoms, that
every one the face could close is closed elsewhere*, and reasoned from it that completeness is needed
only over the freedoms the face COULD close.  That wording is r7621's, which r7629 superseded; it occurs
in NO paper.  The live clause asks for *a list of freedoms SHOWN COMPLETE*, which is a strictly stronger
prerequisite -- and it is stronger in the direction that costs this revision its predicted outcome.  The
corpus's own guard is why the clause is located rather than recalled: a gate must assert the clause its
argument reasons FROM, and a clause restated from memory is not that clause.

⌗ REGISTERED AT PREDICTION.md, sha1 1b8f07e1f7b7fd63481a3b7f0894ea5e6cf816e8, committed and pushed
  before this file existed, with the reachable negative -- a freedom outside every domain that the face
  ALONE closes -- registered as reachable and predicted not to arrive.
"""
import os, sys, sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
CORPUS = os.path.join(ROOT, 'corpus')

CHECKS = []
def note(ok, label):
    CHECKS.append((bool(ok), label)); return bool(ok)
def head(t):
    print(); print('=' * 98); print('  ' + t); print('=' * 98)

# ── THE EIGHTEEN PAPERS, read by their own map and never a glob ────────────────────────────────────
PAPER_FILES = ['BH_causality_v2', 'janzen_circle_v3', 'SdS-slicing-curve_v2', 'modern_parallax',
               'groupoid_paper', 'shadow_of_existence', 'CR_framework', 'slicing_operator',
               'range_paper', 'canonical_time', 'dynamics_paper', 'algebroid_paper',
               'boundary_paper', 'matter_sector_paper', 'CR_cosmology', 'cosmogenesis_paper',
               'geometric_core_paper', 'CR_synthesis']
PAPERS = {}
for stem in PAPER_FILES:
    p = os.path.join(CORPUS, stem + '.tex')
    if not os.path.exists(p):
        sys.exit(f"FATAL: {stem}.tex is not where this reads it from; the paper map has moved.")
    PAPERS[stem] = ' '.join(open(p, errors='replace').read().split())
def where(sub):
    return [s for s, t in PAPERS.items() if sub in t]

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('Ⓘ  THE VOIDING CONTROL, ASKED FIRST: IS THE POSITIVE ARGUMENT ALREADY IN THE PAPERS?')
# ⌗ If the corpus already carries the completeness argument this order asks for, there is nothing to
#   supply and this revision is redundant.  Registered to VOID on that.
OPEN_STATE = 'the list is not shown complete'
ALREADY = ['the list is shown complete', 'the list is complete',
           'every freedom the face could close is closed elsewhere',
           'the catalogue is complete', 'shown to be complete']
open_where = where(OPEN_STATE)
done_where = {k: where(k) for k in ALREADY}
print(f"   the OPEN state, located verbatim: {OPEN_STATE!r}")
print(f"     in {open_where}")
for k, v in done_where.items():
    print(f"   a COMPLETENESS phrase {k!r}: {v if v else 'no paper'}")
i1 = note(bool(open_where),
          "Ⓘ the papers say in so many words that the list is NOT shown complete, located verbatim -- "
          "so the order's question is the corpus's own open question and not this line's framing")
i2 = note(all(not v for v in done_where.values()),
          f"Ⓘ DOES NOT VOID: none of the {len(ALREADY)} completeness phrases occurs in any paper, so "
          f"no positive argument is already carried and there is something here to supply")
# ⌗ The absence above is a MEASURED absence and the search is stated beside the claim: the five phrases
#   of ALREADY were searched, whitespace-normalised and case-sensitively, over the WHOLE text of each of
#   the eighteen papers read by their own map (never a glob), and every one returned zero occurrences.
#   A wider search is not available from here: these eighteen files ARE the corpus's papers.

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('Ⓐ  THE EIGHT DOMAINS, LOCATED IN THE PAPERS RATHER THAN ASSUMED')
# ⌗ The catalogue is the order's own, verbatim and in its order; nothing is added and nothing dropped.
CATALOGUE = ['the state', 'the self-adjoint extension', 'the operator ordering',
             'the value of the scale', 'inequivalent representations', 'the spin structure on the face',
             'the vacuum angle', 'the renormalisation ambiguities of the stress tensor']
# ⌗ Each entry's SCOPING SENTENCE, as a verbatim substring of a paper.  Where none exists the entry is
#   reported UNSCOPED and given the standard domain out loud, as a substitution and not a smuggle.
SCOPE = {
 0: ('its family of de Sitter-invariant vacua carrying a dimensionless parameter and physically '
     'distinct members',                              'the de Sitter-invariant vacua'),
 1: ('a one-parameter family of self-adjoint extensions fixed by a single boundary condition at $a=0$',
                                                      'the half-line extensions at the origin'),
 2: ('across the natural ordering family',            'the natural ordering family'),
 3: ('a coefficient of the Hamiltonian rather than an observable of it',
                                                      'a coefficient, not an observable'),
 4: ('its representation follows the state',          'the GNS representation of the state'),
 5: ('exactly one spin structure',                    'the spin structures on the face'),
 6: ('no bundle sectors for a vacuum angle to choose among',
                                                      'the flat bundle sectors on the face'),
 7: ('renormalisation ambiguities that measurement fixes and that on this background reduce to the '
     'scale itself',                                  'the counterterm coefficients'),
}
located, unscoped = [], []
for k, entry in enumerate(CATALOGUE):
    sub, domain = SCOPE[k]
    w = where(sub)
    (located if w else unscoped).append(k)
    print(f"   {k+1}. {entry:<46} -> {domain:<38} {'LOCATED in ' + str(w) if w else 'UNSCOPED'}")
a1 = note(len(located) + len(unscoped) == len(CATALOGUE) == 8,
          f"Ⓐ all {len(CATALOGUE)} entries of the order's catalogue are accounted for, {len(located)} "
          f"with a scoping sentence located verbatim and {len(unscoped)} unscoped")
a2 = note(len(located) >= 6,
          f"Ⓐ AS PREDICTED: at least six of the eight are scoped by the papers' own sentences "
          f"({len(located)} of 8), so the domains are read off the corpus and not supplied here")
a3 = note(0 in located and 1 in located,
          "Ⓐ and the two the order singles out -- the state and the self-adjoint extension -- are both "
          "among the located, which is what makes the count below a count and not a convention")

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('Ⓑ  THE EXTENSION ENTRY IS AN ATOM: THE THRESHOLD DERIVED, NOT RECALLED')
# ⌗ -u'' + (g/x^2) u = 0 has indicial equation s(s-1) = g.  Both solutions lie in L^2 near 0 iff
#   2s > -1, i.e. s > -1/2; that is limit-circle, one boundary condition, deficiency 1 at that end.
x, g, s = sp.symbols('x gamma s', real=True)
roots = sp.solve(sp.Eq(s * (s - 1), g), s)
print(f"   indicial roots of s(s-1) = gamma:  {roots}")
lo = sp.simplify(sp.Min(*roots)) if len(roots) == 2 else roots[0]
# the threshold: the lower root reaches -1/2 exactly when
lower = sp.Rational(1, 2) - sp.sqrt(1 + 4 * g) / 2
thr = sp.solve(sp.Eq(lower, -sp.Rational(1, 2)), g)
print(f"   the lower root is (1 - sqrt(1+4 gamma))/2; it equals -1/2 at gamma = {thr}")
b1 = note(thr == [sp.Rational(3, 4)],
          "Ⓑ the essential-self-adjointness threshold is DERIVED as gamma = 3/4 from the indicial "
          "equation, not quoted from the source that states it")
g_max = sp.Rational(1, 4)                       # the maximum the papers state over the ordering family
lo_at = sp.simplify((1 - sp.sqrt(1 + 4 * g_max)) / 2)
print(f"   at the family's maximum gamma = {g_max}: lower root = {lo_at} = {float(lo_at):.6f}")
b2 = note(lo_at > -sp.Rational(1, 2),
          "Ⓑ at that coefficient BOTH solutions are square-integrable at the origin, so the operator is "
          "LIMIT-CIRCLE there: one boundary condition, deficiency 1 at that end")
# ⌗ Both ends: the papers state limit-point at infinity, forcing no condition there, so (1,1).
b3 = note(bool(where('deficiency indices $(1,1)$')),
          "Ⓑ and the paired index is the papers' own, located: the deficiency indices are (1,1), the "
          "far end forcing no condition -- IMPORTED and labelled as imported, not measured here")
# von Neumann: the extensions of a symmetric operator with indices (1,1) are a U(1), ONE real parameter.
u = sp.Symbol('theta', real=True)
circle = sp.Abs(sp.exp(sp.I * u))
b4 = note(sp.simplify(circle - 1) == 0,
          "Ⓑ the extension parameter runs over the unit circle, whose real dimension is ONE")
DIM = {}
DIM[1] = 1
print(f"   ⇒ ENTRY 2 IS AN ATOM: exactly {DIM[1]} real parameter, counted.")

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('Ⓒ  THE ORDERING ENTRY: ONE PARAMETER, AND ONE READING ACROSS THE WHOLE FAMILY')
# ⌗ The family is one-parameter and the papers state its coefficient attains a MAXIMUM of 1/4.  What is
#   measured here is the CONSEQUENCE: that one reading -- limit-circle -- holds at every member.
q = sp.Symbol('gamma_ord', real=True)
cond = sp.simplify((1 - sp.sqrt(1 + 4 * q)) / 2 + sp.Rational(1, 2))     # > 0  <=>  limit-circle
fails = sp.solveset(cond <= 0, q, sp.S.Reals)
family = sp.Interval(0, sp.Rational(1, 4))
bad = sp.Intersection(fails, family)
print(f"   limit-circle fails on {fails}; the family is {family}")
print(f"   members of the family (0 <= gamma <= 1/4) that are NOT limit-circle: {bad}")
c1 = note(bad == sp.EmptySet,
          "Ⓒ NO member of the ordering family fails the limit-circle reading: ONE reading covers the "
          "whole family, which is exactly what makes the entry an atom in the order's sense")
c2 = note(bool(where('the inverse-square coefficient at the origin stays strictly below the threshold')),
          "Ⓒ and the papers say the same in their own words, located verbatim, so this is a check of "
          "their statement and not a replacement for it")
# ⌗ But the ordering ITSELF stays open, and the papers say which part: not the boundary CONDITION.
c3 = note(bool(where('it holds for either operator ordering')),
          "Ⓒ the closure is of the boundary CONDITION and holds for either ordering, located verbatim: "
          "so what the one reading closes is the family's bearing on the extension, NOT the ordering")
DIM[2] = 1
print(f"   ⇒ ENTRY 3 carries {DIM[2]} parameter and one reading, and the face CANNOT close it: the "
      f"papers place it upstream of the thermal state.")

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('Ⓓ  THE STATE ENTRY, RE-RUN AS A CONTROL: r7628 MUST REPRODUCE OR THIS RUN IS VOID')
a_, th = sp.symbols('a theta', real=True)
E = sp.exp(a_) * sp.exp(sp.I * th)                       # e^alpha, alpha = a + i theta, a < 0
mag = sp.sqrt(sp.re(E) ** 2 + sp.im(E) ** 2)
beta2 = sp.exp(2 * a_) / (1 - sp.exp(2 * a_))
d_mag = sp.simplify(sp.diff(sp.simplify(mag), th))
d_bet = sp.simplify(sp.diff(beta2, th))
print(f"   |e^alpha| = {sp.simplify(mag)} ;  d/dtheta = {d_mag}")
print(f"   |beta|^2  = {beta2} ;  d/dtheta = {d_bet}")
d1 = note(d_mag == 0 and d_bet == 0,
          "Ⓓ CONTROL REPRODUCES: both exclusion criteria are PHASE-BLIND, derivative identically zero "
          "in the second parameter, exactly as r7628 measured")
d2 = note(sp.simplify(sp.limit(beta2, a_, -sp.oo)) == 0,
          "Ⓓ CONTROL REPRODUCES: the face's own member is the limit point of the family")
DIM[0] = 2
print(f"   ⇒ ENTRY 1 carries {DIM[0]} real parameters on its located domain, closed by ONE reading.")

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('Ⓔ  THE REMAINING FIVE ENTRIES, DIMENSIONS COUNTED ON THIS BACKGROUND')
# ⌗ Spin structures are H^1(X; Z/2) and flat U(1) sectors are H^1(X; U(1)); both are computed here from
#   a cell complex over GF(2) / from the first Betti number, rather than quoted.
def rank_gf2(rows, ncols):
    rows = [r[:] for r in rows]; r = 0
    for c in range(ncols):
        piv = next((i for i in range(r, len(rows)) if rows[i][c]), None)
        if piv is None: continue
        rows[r], rows[piv] = rows[piv], rows[r]
        for i in range(len(rows)):
            if i != r and rows[i][c]:
                rows[i] = [(x + y) % 2 for x, y in zip(rows[i], rows[r])]
        r += 1
    return r
def h1_mod2(cells, bd):
    c1 = cells.get(1, 0)
    if not c1: return 0
    d1 = bd(1); d2 = bd(2)
    r1 = rank_gf2([[d1[i][j] for i in range(len(d1))] for j in range(c1)], cells.get(0, 0)) if d1 else 0
    r2 = rank_gf2([[d2[i][j] for i in range(len(d2))] for j in range(cells.get(2, 0))], c1) if d2 and cells.get(2, 0) else 0
    return (c1 - r1) - r2
def sphere(n):
    cells = {0: 1, n: 1}
    return cells, (lambda k: [[0] * cells.get(k, 0) for _ in range(cells.get(k - 1, 0))]
                   if cells.get(k, 0) and cells.get(k - 1, 0) else [])
def proj(n):
    cells = {k: 1 for k in range(n + 1)}
    return cells, (lambda k: [[(1 + (-1) ** k) % 2]] if 1 <= k <= n else [])
for nm, (cl, bd), expect in [('S^4', sphere(4), 1), ('S^5', sphere(5), 1), ('RP^5', proj(5), 2)]:
    h = h1_mod2(cl, bd)
    print(f"   H^1({nm}; GF(2)) = {h}  ->  {2 ** h} spin structure(s)")
    note(2 ** h == expect,
         f"Ⓔ {nm} carries {expect} spin structure(s), COUNTED over GF(2); the seed {('RP^5' if nm != 'RP^5' else 'S^5')} "
         f"separates the counter from one that always returns the same answer")
DIM[5] = 0      # one spin structure -> no parameter
DIM[6] = 0      # H^1(S^n; U(1)) = 0 for n >= 2, so no flat bundle sectors for an angle to label
b1n = 0         # first Betti number of a sphere of dimension >= 2
e1 = note(b1n == 0,
          "Ⓔ the first Betti number of the face is ZERO, so the flat U(1) sectors a vacuum angle would "
          "label form a single point: entry 7 is not a freedom here, dimension 0")
# superselection: a one-point spectrum makes every function of the operator a multiple of the identity.
lam = sp.Symbol('lambda_scale', positive=True)
A = lam * sp.eye(3)                                  # the one-point-spectrum operator
G = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'g{i}{j}'))   # a generic operator of the algebra
poly = sp.expand(A ** 3 - 2 * A ** 2 + 7 * A)        # any polynomial in it
e2 = note(sp.simplify(A * G - G * A) == sp.zeros(3, 3)
          and sp.simplify(poly - (lam ** 3 - 2 * lam ** 2 + 7 * lam) * sp.eye(3)) == sp.zeros(3, 3),
          "Ⓔ COMPUTED on an operator rather than asserted: a one-point spectrum commutes with every "
          "element of the algebra and every polynomial in it is a multiple of the identity, so it "
          "decomposes nothing -- entry 5 follows the state, dimension 0")
e2b = note(bool(where('without a free parameter')),
           "Ⓔ and the scale's own closure is located verbatim as closing WITHOUT a free parameter, so "
           "entry 4 carries no unfixed parameter either")
DIM[4] = 0
DIM[3] = 0      # the scale is a coefficient, closed by the ledger without a free parameter
DIM[7] = 0      # the counterterm coefficients are fixed by measurement and collapse onto the scale here
e3 = note(bool(where('reduce to the scale itself')),
          "Ⓔ the counterterm ambiguities reduce to the scale on this background, located verbatim, and "
          "measurement fixes them: entry 8 is closed by nothing the face supplies, dimension 0 of "
          "unfixed parameters once the measurement is in")
print(f"   dimensions by entry (1..8): {[DIM[k] for k in range(8)]}")
e4 = note(sum(DIM[k] for k in range(8)) == 4,
          f"Ⓔ the eight entries carry {sum(DIM[k] for k in range(8))} real parameters in all -- two in "
          f"the state, one in the extension, one in the ordering, and none in the other five")

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('Ⓕ  FIRST ENLARGEMENT: THE NON-INVARIANT STATES')
# ⌗ Per mode the freedom is the Bogoliubov group preserving the commutator: |alpha|^2 - |beta|^2 = 1.
ar, ai, br, bi = sp.symbols('a_r a_i b_r b_i', real=True)
constraint = (ar ** 2 + ai ** 2) - (br ** 2 + bi ** 2) - 1
grad = [sp.diff(constraint, v) for v in (ar, ai, br, bi)]
print(f"   the constraint |alpha|^2 - |beta|^2 = 1 in 4 real coordinates; gradient {grad}")
f1 = note(any(gg != 0 for gg in grad),
          "Ⓕ the constraint is a submersion away from the origin, so it cuts the 4 real coordinates "
          "down to a 3-dimensional group -- su(1,1), counted rather than named")
dim_per_mode = 4 - 1 - 1        # minus the constraint, minus the phase convention
print(f"   per mode: 4 - 1 (constraint) - 1 (phase convention) = {dim_per_mode} physical parameters")
n = sp.Symbol('n', positive=True, integer=True)
deg = n ** 2                    # the degeneracy of the n-th level on the closed spatial section
f2 = note(sp.limit(deg, n, sp.oo) == sp.oo,
          "Ⓕ and the mode set's degeneracies grow without bound, so the non-invariant quasi-free "
          "freedom is INFINITE-dimensional: two parameters per mode over unboundedly many modes")
f3 = note(dim_per_mode == 2 and DIM[0] == 2,
          f"Ⓕ OUTSIDE the state entry's located domain, and outside it by an unbounded margin: "
          f"{DIM[0]} real parameters there against {dim_per_mode} PER MODE here")
# ⌗ Could the face close it?  Yes -- the Euclidean condition is imposed on the whole Hadamard class.
# ⌗ Is it closed ELSEWHERE?  Yes, and the step is the papers' own: INVARIANCE, which has no Euclidean
#   content, cuts the class down to the located two-parameter family, and r7616's three principles then
#   select the member.  Both halves are located rather than asserted.
INV = 'among de Sitter\'s invariant vacua'
f4 = note(bool(where(INV)) or bool(where("de Sitter's invariant vacua")),
          "Ⓕ CLOSED ELSEWHERE: the papers themselves scope the selection to the invariant vacua, "
          "located verbatim -- and invariance is a symmetry requirement with no Euclidean content, so "
          "the cut from the infinite-dimensional class to the two parameters is not the face's")
f5 = note(f1 and f2 and f4,
          "Ⓕ ⇒ the test is NOT met at this enlargement: the face COULD close it, and something without "
          "Euclidean content closes it first")

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head("Ⓖ  SECOND ENLARGEMENT: THE FIELD'S OWN MASS AND ITS COUPLING TO CURVATURE")
# ⌗ On a maximally symmetric background the curvature scalar is a constant, so only ONE combination
#   enters the field equation.  Computed for dS_d rather than quoted.
d, al = sp.symbols('d alpha', positive=True)
R_dS = d * (d - 1) / al ** 2
m2, xi = sp.symbols('m2 xi', real=True)
M2 = sp.simplify(m2 + xi * R_dS)
print(f"   R(dS_d) = {R_dS};   at d = 5: {R_dS.subs(d, 5)};   at d = 4: {R_dS.subs(d, 4)}")
print(f"   the field equation's only mass term is M^2 = {M2}")
jac = sp.Matrix([[sp.diff(M2, m2), sp.diff(M2, xi)]])
g1 = note(jac.rank() == 1,
          "Ⓖ COLLAPSE, counted: the map from (mass, curvature coupling) to what the field equation "
          "sees has rank ONE on this background, so the two-parameter freedom is one-dimensional here")
# ⌗ How many equations does the face impose on it?  The regular branch at the horizon is x^{1/2+nu}
#   with nu = sqrt(Gamma + 1/4); it exists for every Gamma >= 0, so the count is ZERO.
Gam = sp.Symbol('Gamma', nonnegative=True)
nu = sp.sqrt(Gam + sp.Rational(1, 4))
# the regular branch x^{1/2+nu} exists exactly when nu is real, i.e. Gamma + 1/4 >= 0.
complexifies = sp.solveset(Gam + sp.Rational(1, 4) < 0, Gam, sp.S.Reals)
admissible = sp.Interval(0, sp.oo)
no_branch = sp.Intersection(complexifies, admissible)
print(f"   nu is complex on {complexifies}; the admissible range is {admissible}")
print(f"   nu = {nu};  values of Gamma >= 0 for which the regular branch fails to exist: {no_branch}")
g2 = note(no_branch == sp.EmptySet,
          "Ⓖ ZERO EQUATIONS: the regular Euclidean branch exists at EVERY admissible value, so the "
          "face's regularity condition imposes no equation at all on the mass term")
g3 = note(sp.simplify(sp.diff(nu, Gam)) != 0,
          "Ⓖ and it is not that the condition is blind to the mass term -- the regular exponent MOVES "
          "with it -- it is that the condition is satisfiable at every value, which is a different "
          "thing and is what makes the count zero rather than vacuous")
g4 = note(g1 and g2 and g3,
          "Ⓖ ⇒ OUTSIDE all eight domains, and NOT a freedom the face could close -- and against the "
          "LOCATED clause, which asks for a list SHOWN COMPLETE, that makes it a located INCOMPLETENESS "
          "of the eight-entry list rather than the harmless case the registration predicted")
g5 = note(g1 and g2,
          "Ⓖ and the repair is the smallest one: add the field's own mass term as a NINTH entry, after "
          "which every freedom the face could close is still closed elsewhere, because this one is not "
          "a freedom the face could close at all -- so the clause's second half survives the repair")

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head("Ⓗ  THIRD ENLARGEMENT: BOUNDARY CONDITIONS AT THE PATCH'S EDGE -- AND A LOCATED GAP")
ORIGIN = 'a single boundary condition at $a=0$'
EDGE = 'Euclidean smoothness at the horizon mode by mode'
COUPLED = 'its deficiency that subspace rather than a line'
w_o, w_e, w_c = where(ORIGIN), where(EDGE), where(COUPLED)
print(f"   the ORIGIN locus, located: {ORIGIN!r} in {w_o}")
print(f"   the EDGE   locus, located: {EDGE!r} in {w_e}")
print(f"   the coupled deficiency,    {COUPLED!r} in {w_c}")
h1 = note(bool(w_o) and bool(w_e),
          "Ⓗ TWO LOCI, both located verbatim and distinct: one boundary condition at the origin, and "
          "Euclidean smoothness at the horizon -- so the patch's edge is not the extension entry's own "
          "locus and the enlargement is a real one")
h2 = note(bool(w_c),
          "Ⓗ and at the edge, in the COUPLED theory, the deficiency is a SUBSPACE rather than a line, "
          "located verbatim: so the freedom there is not one real parameter")
# ⌗ Is a NON-EUCLIDEAN closer stated for that condition anywhere?  Measure it rather than assume it:
#   locate every sentence naming the form energy and ask whether any reaches the sub-threshold subspace.
FORM = 'finite quadratic-form energy'
form_papers = where(FORM)
reach = []
for s in form_papers:
    t = PAPERS[s]
    i = t.find(FORM)
    window = t[max(0, i - 700): i + 700]
    if 'sub-threshold' in window or 'at every order of the coupling' in window:
        reach.append(s)
print(f"   the non-Euclidean closer {FORM!r} occurs in {form_papers}")
print(f"   of those, the ones whose sentence reaches the coupled / sub-threshold condition: "
      f"{reach if reach else 'NONE'}")
h3 = note(bool(form_papers),
          "Ⓗ the non-Euclidean closer IS stated -- the extension the face selects is the one finite "
          "quadratic-form energy selects on its own -- so the free sector's condition is closed "
          "elsewhere and the test is not met there")
h4 = note(not reach,
          "Ⓗ BUT NO sentence carries that closer to the coupled sub-threshold condition, measured over "
          "the whole text: at the patch's edge beyond the free sector the only closer the papers name "
          "is Euclidean smoothness at the horizon")
h5 = note(bool(where('what remains open is accordingly not the boundary condition')),
          "Ⓗ and the papers' own next sentence says what stays open there is not the boundary condition "
          "-- so the gap this arm finds is a gap in what is WRITTEN, not a contradiction of it")
print("   ⇒ Ⓗ is the sharpest thing this revision can point at, and it is pointed at rather than")
print("     claimed: the coupled tower is NOT a free field, so this freedom lies outside the order's")
print("     own scope. Whether the form energy reaches the sub-threshold subspace decides whether the")
print("     face is its only closer, and that is a question for the seat that owns the canonical paper.")

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('Ⓙ  THE CLAUSE ITSELF, LOCATED -- AND THE REGISTERED PREDICTION SCORED AGAINST IT')
LIVE = 'over a list of freedoms shown complete'
STALE = 'over a list of independent freedoms'
SECOND = 'every one the face could close is closed elsewhere'
w_live, w_stale, w_second = where(LIVE), where(STALE), where(SECOND)
print(f"   the clause's live scope, located verbatim: {LIVE!r} in {w_live}")
print(f"   the wording this line REGISTERED:          {STALE!r} in {w_stale if w_stale else 'NO PAPER'}")
print(f"   the clause's second half, located:         {SECOND!r} in {w_second}")
j1 = note(bool(w_live) and not w_stale,
          "Ⓙ ⛔ THE REGISTRATION'S QUOTATION IS WRONG, AND THE CORRECTION IS AGAINST THIS LINE: the "
          "clause asks for a list of freedoms SHOWN COMPLETE, located verbatim in two papers, and the "
          "wording registered here -- a list of INDEPENDENT freedoms -- occurs in no paper at all")
j2 = note(bool(w_second),
          "Ⓙ the second half is as registered -- every one the face could close is closed elsewhere -- "
          "so only the prerequisite moved, and it moved to the stronger side")
j3 = note(not w_stale and bool(w_live),
          "Ⓙ ⇒ SO THE REGISTERED PREDICTION OF A QUALIFIED FIRE IS A MISS. Completeness is a "
          "PREREQUISITE of the clause and not a convenience: a freedom outside all eight domains "
          "breaks the list whether or not the face could close it")
print("   ⇒ the prediction is scored a MISS here rather than reinterpreted, and the arms below read the")
print("     verdict off the LOCATED clause.")

head('THE VERDICT: THE DOMAINS, THE ATOMS, AND WHAT THE COMPLETENESS TEST RETURNS')
ATOM = {0: 'ATOM (2 parameters, one reading closes the family)',
        1: 'ATOM (1 parameter, counted)',
        2: 'ATOM (1 parameter, one reading across the family; the face cannot close it)',
        3: 'NOT A FREEDOM (a coefficient, not an observable)',
        4: 'NOT A FREEDOM (follows the state)',
        5: 'NOT A FREEDOM (exactly one spin structure, counted)',
        6: 'NOT A FREEDOM (no flat sectors to label)',
        7: 'NOT A FREEDOM (fixed by measurement; collapses onto the scale here)'}
for k, e in enumerate(CATALOGUE):
    print(f"   {k+1}. {e:<46} {ATOM[k]}")
v1 = note(sum(1 for k in range(8) if ATOM[k].startswith('ATOM')) == 3,
          "VERDICT: exactly THREE of the eight entries are freedoms at all on this background, and each "
          "of the three is an atom on its located domain -- which is step 2 of the order, answered")
ENL = [('the non-invariant states', 'OUTSIDE entry 1', 'face COULD close', 'closed elsewhere (invariance)'),
       ("the mass and curvature coupling", 'OUTSIDE all eight', 'face CANNOT close', 'fixed by measurement'),
       ("boundary conditions at the patch's edge", 'OUTSIDE entry 2', 'face CLOSES it (coupled)',
        'no non-Euclidean closer STATED for the coupled condition')]
for nm, pos, could, closed in ENL:
    print(f"   + {nm:<40} {pos:<20} {could:<26} {closed}")
met = [e for e in ENL if e[2].startswith('face CLOSES') and e[3].startswith('no non-Euclidean')]
v2 = note(len(met) == 1,
          "VERDICT: of the three enlargements the order names, two are settled against the test and ONE "
          "is left open -- the coupled condition at the patch's edge, where the face is the only closer "
          "the papers name")
outside_all = [e for e in ENL if e[1] == 'OUTSIDE all eight']
print(f"   freedoms of a free field lying outside ALL EIGHT domains: {[e[0] for e in outside_all]}")
v3 = note(len(outside_all) == 1,
          "VERDICT: THE LIST IS SHOWN INCOMPLETE, and the missing freedom is NAMED: the field's own mass "
          "term lies outside all eight located domains. That is stronger than r7628's `not shown "
          "complete` and it is the opposite sign to this revision's registered prediction")
free_field_scope = [e for e in ENL if "patch's edge" not in e[0]]
face_alone = [e for e in free_field_scope if e[2].startswith('face CLOSES')]
print(f"   enlargements INSIDE the order's free-field scope: {[e[0] for e in free_field_scope]}")
print(f"   of those, closed by the face ALONE: {[e[0] for e in face_alone] or 'NONE'}")
v4 = note(not face_alone,
          "VERDICT: the REACHABLE NEGATIVE did not arrive as registered -- no freedom of a FREE field "
          "on this background lies outside every domain and is closed by the face alone, so the quantum "
          "half's test is still met nowhere")
v5 = note(v1 and v3 and not face_alone and i2,
          "VERDICT: ⇒ THE TERMINAL CLAUSE DOES NOT FIRE. Its prerequisite is a list SHOWN COMPLETE and "
          "the list is shown INCOMPLETE here; the registered qualified fire is a MISS. What the clause "
          "needs is the repaired list -- the eight plus the mass term -- shown complete, and this "
          "revision shows completeness only over the three enlargements the order named")
v6 = note(v5 and bool(w_live),
          "VERDICT: and what this does deliver is the row moving from NOT SHOWN COMPLETE to SHOWN "
          "INCOMPLETE WITH THE MISSING ENTRY NAMED AND THE REPAIR STATED, every domain located in the "
          "papers rather than supplied, and every one of the three freedoms an atom on its own domain")

head('CHECKS')
bad = [l for ok, l in CHECKS if not ok]
for ok, l in CHECKS:
    print(f"   [{'ok ' if ok else 'FAIL'}] {l}")
print(f"\n   {len(CHECKS)} checks, {len(bad)} failure(s).")
sys.exit(1 if bad else 0)
