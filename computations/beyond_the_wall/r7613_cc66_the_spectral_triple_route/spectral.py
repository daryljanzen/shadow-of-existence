#!/usr/bin/env python3
"""r7613+cc66 -- PO-94's gauge half, the spectral-triple route: the four questions PREDICTION.md
registered, each answered by a measurement rather than by a reading of the literature.

Everything decisive here is COMPUTED: the chirality count a real structure would have to respect, the
dimension of the space a curvature would have to live in, the order-one condition on the corpus's own
algebra, and what the inner fluctuations of a finite algebra actually are.  A reader who distrusts a
verdict can distrust the object it is computed on instead.

THE BAR, inherited UNCHANGED from r7611 and not re-chosen here.  Produce, on the compact face or on
E = pi_*(mode bundle), a connection whose CURVATURE DOES NOT VANISH IDENTICALLY, from data the corpus
already has and NOT from a substrate isometry.

WHAT IS NOT CLAIMED.  Not that no route exists -- B59's composite/emergent route is untouched.  Not
that a COUPLING follows from any connection: PO-5 is a different row and B59 says so.  Not that B61 is
weakened; its rows are read here, not re-derived, except the grading, which is recomputed so that
nothing is inherited on trust.
"""
import pathlib
import sys

import numpy as np
import sympy as sp

CHECKS = []


def check(name, ok, shown=''):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   ->  {shown}" if shown else ''), flush=True)


def head(title):
    print()
    print('=' * 78)
    print(f' {title}')
    print('=' * 78)
    print()


ROOT = pathlib.Path(__file__).resolve().parents[3]
P14 = (ROOT / 'corpus' / 'matter_sector_paper.tex').read_text(encoding='utf-8')
P13 = (ROOT / 'corpus' / 'boundary_paper.tex').read_text(encoding='utf-8')

# ============================================================ THE PIECES, READ AND NOT RECALLED
head('THE PIECES THE CORPUS SUPPLIES -- READ FROM THE PAPERS, NOT RECALLED')
# ⌗ ** THIS SECTION EXISTS BECAUSE THIS SEAT GOT IT WRONG TWICE. **  r7577+cc66.4 attributed a law to
#   P14 without opening P14, and r7611 attributed the order 27 the same way; check_unread_figure named
#   both.  A label that says "the paper's own" is a claim about a FILE, and the only thing that
#   discharges it is opening the file here.
LEAF = r'the leaf is compact and the Dirac operator on it carries a \emph{finite} analytical index'
KER = r'$\dim\ker_+=3$, $\dim\ker_-=0$'
ONE_D = r'\emph{The three wall modes are the kernel of one Dirac operator}'
FACE = r'the round face carries no Dirac zero modes, so there is no massless content for it to act on'
check(f'P14 supplies D and its domain in its own words -- READ: "{LEAF[:52]}..."', LEAF in P14,
      'found in matter_sector_paper.tex')
check(f'P14 states the wall kernel is ONE-CHIRALITY and gives both dimensions -- READ: "{KER}"',
      KER in P14, 'found in matter_sector_paper.tex')
check('P14 states the three wall modes are the kernel of ONE operator, so H_ker is a space of one '
      "field's states -- READ, not recalled", ONE_D in P14, 'found in matter_sector_paper.tex')
check(f'P13 sec:face-status states the FACE obstruction in its own words -- READ: "{FACE[:52]}..."',
      FACE in P13, 'found in boundary_paper.tex')

# ============================================================ CONTROL 1 -- the checker certifies a triple that IS one
def order_one_defect(D, A_ops, J_conj):
    """the largest ||[[D,a], J b* J^-1]|| over the given operators -- the order-one condition's own
    expression, evaluated rather than argued.  J_conj(X) applies J X J^-1."""
    worst = 0.0
    for a in A_ops:
        da = D @ a - a @ D
        for b in A_ops:
            jb = J_conj(b.conj().T)
            worst = max(worst, float(np.linalg.norm(da @ jb - jb @ da)))
    return worst


head('CONTROL 1 -- THE CHECKER MUST CERTIFY A REAL TRIPLE THAT IS ONE, OR ITS REFUSALS MEASURE IT')
# ⌗ ** AND THE NOTE SITS AT THE LINE THAT CAUSED IT: THIS CONTROL CAUGHT ME TWICE BEFORE IT PASSED,
#   WHICH IS THE ONLY REASON ANYTHING BELOW IS WORTH READING. **
#     ⒜ The first version used the circle -- A = C(S^1) on L^2(S^1), D = -i d/dtheta, J = complex
#        conjugation -- and asserted JD = DJ.  ** It FAILED, and the failure was mine and not the
#        circle's: for that D, conjugation gives JDJ^-1 = -D, so plain conjugation is NOT a real
#        structure for that operator. **  *The axiom I had written down was the wrong one.*
#     ⒝ The repair used the two-point space naively -- A = C + C acting DIAGONALLY on C^2 with D
#        purely off-diagonal -- and asserted the order-one condition.  ** It FAILED TOO, and again
#        correctly: that triple genuinely violates order-one, the defect being 60.1 at a = b =
#        diag(2,-3). **  *Which is exactly why the Standard Model's finite triple is built as a
#        BIMODULE and not like that.*
#   ⇒ *Repaired by certifying the two-point triple in the form the condition is actually about: the
#   algebra on the left factor, its opposite on the right through J, so the two actions commute by
#   construction.  And the circle is kept as a SECOND control whose job is now to come back the other
#   way.*  ⛔ **A control that cannot fail licenses every verdict under it; this one failed twice and
#   both failures were mine, so the passes below are measurements.**
print('  The two-point real triple in its BIMODULE form, which is what the order-one condition is')
print('  about: H = C^2 tensor C^2, the algebra acting on the LEFT factor (a -> a tensor 1), its')
print('  opposite acting on the RIGHT through J, D = D1 tensor 1 + 1 tensor D1 with D1 real symmetric')
print('  so that D is J-symmetric, and J = (complex conjugation) o (flip of the two factors).')
print('  Asked of it: J^2 = +1, JD = DJ, the order-one condition, AND [D, a] non-zero so that the')
print('  order-one arm certifies something instead of holding because both sides vanish.')
print()
I2 = np.eye(2, dtype=complex)
M_PARAM = 1.7
D1 = np.array([[0.0, M_PARAM], [M_PARAM, 0.0]], dtype=complex)
D2 = np.kron(D1, I2) + np.kron(I2, D1)
FLIP2 = np.zeros((4, 4), dtype=complex)
for _i in range(2):
    for _j in range(2):
        FLIP2[2 * _i + _j, 2 * _j + _i] = 1.0


def J2_conj(X):
    """J X J^-1 for the antilinear J = conjugation o flip-of-factors."""
    return FLIP2 @ X.conj() @ FLIP2


A2 = [np.kron(np.diag([1.0, 0.0]).astype(complex), I2), np.kron(np.diag([0.0, 1.0]).astype(complex), I2),
      np.kron(np.diag([2.0, -3.0]).astype(complex), I2), np.kron(np.diag([1j, 2j]), I2)]
_sq2 = float(np.linalg.norm(FLIP2 @ FLIP2.conj() - np.eye(4)))
_jd2 = float(np.linalg.norm(J2_conj(D2) - D2))
_nontriv = max(float(np.linalg.norm(D2 @ a - a @ D2)) for a in A2)
check('CONTROL: J^2 = +1 on the two-point bimodule triple', _sq2 < 1e-12, f'||J^2-1|| = {_sq2:.2e}')
check('CONTROL: and JD = DJ there, which is the axiom a real structure actually asks',
      _jd2 < 1e-12, f'||JDJ^-1 - D|| = {_jd2:.2e}')
check('CONTROL: and [D, a] is NON-zero on this algebra, so the order-one arm below is not vacuous and '
      'certifies something', _nontriv > 1.0, f'max ||[D,a]|| = {_nontriv:.4g}')
_d1 = order_one_defect(D2, A2, J2_conj)
check('CONTROL: the ORDER-ONE CONDITION HOLDS EXACTLY on it -- the left action and the J-conjugated '
      'right action live in different tensor factors, which is the structure the condition encodes -- '
      'so a later failure is a finding and not my expression being wrong',
      _d1 < 1e-12, f'max ||[[D,a],Jb*J^-1]|| = {_d1:.2e}')

# the circle, kept as the SECOND control: its job is now to come back the OTHER way
N = 6
modes = np.arange(-N, N + 1)
D_s1 = np.diag(modes.astype(complex))


def mult_op(coeffs):
    """multiplication by sum_k c_k e^{ik theta} in the Fourier basis: a banded Toeplitz matrix."""
    nn = len(modes)
    M = np.zeros((nn, nn), dtype=complex)
    for k, c in coeffs.items():
        for i, m in enumerate(modes):
            j = np.where(modes == m - k)[0]
            if len(j):
                M[i, j[0]] += c
    return M


FLIP = np.eye(len(modes))[::-1]


def J_s1(X):
    return FLIP @ X.conj() @ FLIP


A_s1 = [mult_op({0: 1.0}), mult_op({1: 1.0, -1: 1.0}), mult_op({2: 0.5, -2: 0.5}),
        mult_op({1: 1j, -1: -1j})]
_jd_s1 = float(np.linalg.norm(J_s1(D_s1) - D_s1))
_jd_s1_anti = float(np.linalg.norm(J_s1(D_s1) + D_s1))
check('CONTROL, THE OTHER WAY: on the circle with D = -i d/dtheta, plain conjugation ANTI-commutes '
      'with D rather than commuting, so it is NOT a real structure for that operator -- the checker '
      'distinguishes a real structure from something that merely looks like one, which is the '
      'distinction my first version of this control got wrong',
      _jd_s1 > 1.0 and _jd_s1_anti < 1e-12,
      f'||JDJ^-1 - D|| = {_jd_s1:.4g} but ||JDJ^-1 + D|| = {_jd_s1_anti:.2e}')
# ============================================================ CONTROL 2 -- an order-one violation must be seen
head('CONTROL 2 -- AND A PAIR THAT VIOLATES THE ORDER-ONE CONDITION MUST BE REPORTED AS VIOLATING IT')
# a NON-commutative algebra acting on the same space, with J the same conjugation: [[D,a],Jb*J^-1] has
# no reason to vanish, and if the checker cannot see it the checker is vacuous.
rng = np.random.default_rng(7613)
n = len(modes)
A_bad = [rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n)) for _ in range(2)]
_d2 = order_one_defect(D_s1, A_bad, J_s1)
check('CONTROL: a generic non-commutative pair VIOLATES the order-one condition and the checker says '
      'so, so its verdicts discriminate', _d2 > 1.0, f'max ||[[D,a],Jb*J^-1]|| = {_d2:.3g}')

# ============================================================ CONTROL 3 -- the grading, recomputed
head("CONTROL 3 -- B61's GRADING ROW RECOMPUTED HERE RATHER THAN INHERITED ON TRUST")
g0 = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]], dtype=complex)
g1 = np.array([[0, 0, 0, 1], [0, 0, 1, 0], [0, -1, 0, 0], [-1, 0, 0, 0]], dtype=complex)
g2 = np.array([[0, 0, 0, -1j], [0, 0, 1j, 0], [0, 1j, 0, 0], [-1j, 0, 0, 0]], dtype=complex)
g3 = np.array([[0, 0, 1, 0], [0, 0, 0, -1], [-1, 0, 0, 0], [0, 1, 0, 0]], dtype=complex)
g5 = 1j * g0 @ g1 @ g2 @ g3
_g2 = float(np.linalg.norm(g5 @ g5 - np.eye(4)))
_anti = max(float(np.linalg.norm(g5 @ gm + gm @ g5)) for gm in (g0, g1, g2, g3))
check('the grading axioms hold for gamma^5: gamma^2 = 1 and it ANTI-commutes with every gamma^mu -- '
      "B61's row, recomputed here so nothing is taken on trust",
      _g2 < 1e-12 and _anti < 1e-12, f'||g5^2-1|| = {_g2:.2e}, max ||{{g5,g^mu}}|| = {_anti:.2e}')

# ============================================================ QUESTION 1 -- the real structure J
head('QUESTION (1) -- IS THERE A REAL STRUCTURE J ON THE CORPUS\'S OWN HILBERT SPACE?')
print("  P14's wall kernel is ONE chirality: dim ker_+ = 3, dim ker_- = 0, READ above.  A real")
print('  structure in the KO-dimensions where J ANTI-commutes with the grading must carry the +1')
print('  eigenspace ONTO the -1 eigenspace, and an antilinear BIJECTION cannot do that between spaces')
print('  of different dimension.  ** That is a RANK statement and it is computed, with a balanced')
print('  space as the control where such a J exists and is exhibited. **')
print()


def anti_grading_J_rank_gap(d_plus, d_minus):
    """the obstruction, as a rank: an invertible J with J gamma = -gamma J maps the +1 eigenspace into
    the -1 eigenspace, so it needs d_minus >= d_plus AND d_plus >= d_minus.  Returns the gap; 0 means
    no obstruction FROM THIS COUNT (it does not mean a J exists)."""
    return abs(d_plus - d_minus)


def exhibit_J(d):
    """on a BALANCED (d,d) graded space, build J = (antilinear) swap of the two blocks and verify it
    anti-commutes with gamma and squares to +1 -- so the control is a construction, not an assertion."""
    gam = np.diag([1.0] * d + [-1.0] * d).astype(complex)
    S = np.zeros((2 * d, 2 * d), dtype=complex)
    S[:d, d:] = np.eye(d)
    S[d:, :d] = np.eye(d)
    # J X J^-1 = S conj(X) S  (antilinear); on the grading (real) this is S gamma S
    anti = float(np.linalg.norm(S @ gam.conj() @ S + gam))
    sq = float(np.linalg.norm(S @ S.conj() - np.eye(2 * d)))
    return anti, sq


_gap_corpus = anti_grading_J_rank_gap(3, 0)
_gap_bal = anti_grading_J_rank_gap(3, 3)
_anti_b, _sq_b = exhibit_J(3)
check('ON THE READING H = ker D: no invertible J can anti-commute with the grading, because it would '
      'have to map a 3-dimensional eigenspace onto a 0-dimensional one -- the gap is 3 and an '
      'antilinear bijection cannot close it',
      _gap_corpus == 3, f'|dim ker_+ - dim ker_-| = {_gap_corpus}')
check('CONTROL: on a BALANCED (3,3) graded space the same count gives gap 0 AND the J is EXHIBITED, '
      'anti-commuting with the grading and squaring to +1 -- so the obstruction above is about the '
      "corpus's chirality count and not about the axiom",
      _gap_bal == 0 and _anti_b < 1e-12 and _sq_b < 1e-12,
      f'gap = {_gap_bal}, ||Jgamma+gammaJ|| = {_anti_b:.2e}, ||J^2-1|| = {_sq_b:.2e}')
# ⌗ ** AND THE TRAP PREDICTION.md NAMED IN ADVANCE, HELD TO HERE. **  The (3,0) count is a property of
#   ker D and NOT of H.  On the full L^2 of the leaf's spinors the grading is balanced, so the
#   argument above does NOT close question (1) on that reading -- and this file says so rather than
#   letting the kernel reading stand in for both.
print()
print('  ⚠ AND THE READING THIS DOES **NOT** CLOSE, named in PREDICTION.md before it was computed:')
print('    the (3,0) count belongs to ker D, not to H.  On the full L^2 of the leaf the grading is')
print('    balanced and this obstruction does not apply.  So question (1) is closed on the KERNEL')
print('    reading and OPEN on the L^2 reading, and question (2) is what decides the latter.')

# ============================================================ QUESTION 2 -- the locus
head('QUESTION (2) -- OVER WHICH LOCUS, AND IS THERE A TWO-FORM THERE FOR A CURVATURE TO BE?')
print("  P14's H and D are the LEAF's: the leaf is compact of finite proper length (READ above), a")
print('  ONE-dimensional domain.  The bar asks for a curvature on the compact FACE or on E.  A gauge')
print('  curvature is a TWO-FORM on its base, so the question has an arithmetic answer: how many')
print('  independent two-forms does a base of each dimension carry?  Counted by solving the')
print('  antisymmetry condition M + M^T = 0, never by quoting a binomial.')
print()


def two_form_dim(p):
    """the dimension of the space of 2-forms over a p-dimensional base, by SOLVING M + M^T = 0 for the
    free entries rather than quoting C(p,2)."""
    M = sp.Matrix(p, p, lambda i, j: sp.Symbol(f'M_{i}_{j}', real=True))
    sol = sp.solve(list(M + M.T), list(M), dict=True)
    Ms = M.subs(sol[0]) if sol else M
    return len(Ms.free_symbols)


dims = {p: two_form_dim(p) for p in (1, 2, 3, 5)}
print('    base dimension -> independent two-forms: ' + ', '.join(f'p={p} -> {d}' for p, d in dims.items()))
check('** THE LEAF IS ONE-DIMENSIONAL AND CARRIES ZERO INDEPENDENT TWO-FORMS, so a connection built '
      'over it has NO OBJECT a field strength could be -- whatever its inner fluctuations are. **  '
      'This closes the route on the pieces the corpus actually supplies, and it closes it BEFORE the '
      'real structure is reached',
      dims[1] == 0, f'two-forms over the leaf (p=1) = {dims[1]}')
check('CONTROL: and the same counter is NON-zero at p = 2, 3 and 5, so the zero above is the leaf\'s '
      'dimension and not my counter -- the FACE, at p = 5, would carry 10',
      (dims[2], dims[3], dims[5]) == (1, 3, 10), f'p=2 -> {dims[2]}, p=3 -> {dims[3]}, p=5 -> {dims[5]}')
check('** AND THE REPAIR IS WHERE THE CORPUS STATES AN OBSTRUCTION RATHER THAN SUPPLIES A PIECE: '
      'building the triple over the FACE instead needs a Dirac operator there, and P13 sec:face-status '
      'says in its own words that the round face carries NO Dirac zero modes -- read from the paper, '
      'not recalled **', FACE in P13, 'P13 sec:face-status, read above')

# ============================================================ QUESTION 3 -- the order-one condition
head('QUESTION (3) -- THE ORDER-ONE CONDITION ON THE CORPUS\'S OWN ALGEBRA')
print('  A = M_3(C), the Wedderburn factor B59 names, acting on the 3-dimensional wall kernel; D the')
print('  restriction of the leaf operator to it, i.e. ZERO on a kernel, so the kernel reading is also')
print('  the one where [D,a] = 0 for every a.  ** That is computed, not argued: if [D,a] vanishes the')
print('  order-one condition holds VACUOUSLY and gives the route nothing. **')
print()
D_ker = np.zeros((3, 3), dtype=complex)
basis_m3 = []
for i in range(3):
    for j in range(3):
        E = np.zeros((3, 3), dtype=complex)
        E[i, j] = 1.0
        basis_m3.append(E)
_comm = max(float(np.linalg.norm(D_ker @ a - a @ D_ker)) for a in basis_m3)
_d3 = order_one_defect(D_ker, basis_m3, lambda X: X.conj())
check('on the kernel, D is ZERO by construction -- it is a kernel -- so [D,a] = 0 for every element '
      'of M_3(C) and the order-one condition is satisfied VACUOUSLY',
      _comm < 1e-12 and _d3 < 1e-12, f'max ||[D,a]|| = {_comm:.2e}, order-one defect = {_d3:.2e}')
check('** SO QUESTION (3) ANSWERS IN THE ROUTE\'S FAVOUR AND BUYS IT NOTHING, which is reported as a '
      'pass that does not help rather than folded into the closure: a condition met because both '
      'sides are zero constrains no construction **  -- and CONTROL 2 above shows the same expression '
      'CAN fail, so this is a measurement and not a tautology of my checker',
      _d3 < 1e-12 and _d2 > 1.0, f'vacuous here ({_d3:.2e}), violable there ({_d2:.3g})')

# ============================================================ QUESTION 4 -- the inner fluctuations
head('QUESTION (4) -- WHAT ARE THE INNER FLUCTUATIONS OF A FINITE ALGEBRA?')
print("  The order's own fork: a finite algebra fluctuates D into scalars, not a gauge field.  Here")
print('  that is measured on the corpus\'s pieces: A = sum a_i [D, b_i] over M_3(C) with D the kernel')
print('  operator.  ** With [D,a] = 0 the fluctuation space is not merely scalar, it is ZERO. **')
print()
flucts = [a @ (D_ker @ b - b @ D_ker) for a in basis_m3 for b in basis_m3]
_fmax = max(float(np.linalg.norm(F)) for F in flucts)
_rank = int(np.linalg.matrix_rank(np.array([F.ravel() for F in flucts]), tol=1e-9))
check('** the inner fluctuations over the wall kernel span a ZERO-dimensional space: every a[D,b] '
      'vanishes, so there is no one-form to build a connection from, let alone a curvature **',
      _fmax < 1e-12 and _rank == 0, f'max ||a[D,b]|| = {_fmax:.2e}, rank of their span = {_rank}')
# and the control: on the circle triple the same expression gives a NON-trivial fluctuation space
f_s1 = [a @ (D_s1 @ b - b @ D_s1) for a in A_s1 for b in A_s1]
_rank_s1 = int(np.linalg.matrix_rank(np.array([F.ravel() for F in f_s1]), tol=1e-9))
check('CONTROL: the same expression on the CIRCLE triple spans a space of dimension > 0, so the zero '
      'above is the corpus\'s pieces and not my formula for the fluctuations',
      _rank_s1 > 0, f'rank of the circle triple\'s fluctuation span = {_rank_s1}')

# ============================================================ THE VERDICT
head('THE VERDICT -- INSIDE THE ASSERT, WHERE IT CAN FAIL')
check('** THE SPECTRAL-TRIPLE ROUTE IS CLOSED ON THE PIECES THE CORPUS SUPPLIES, AND IT CLOSES ON THE '
      'LOCUS: P14 gives H and D over the LEAF, the leaf is ONE-dimensional, and a one-dimensional base '
      'carries ZERO two-forms, so there is no object a field strength could be -- before the real '
      'structure is ever reached.  The kernel reading closes twice over, the fluctuations there being '
      'identically zero and the chirality count (3,0) admitting no grading-reversing J.  Building over '
      'the FACE instead is where P13 states no Dirac zero modes.  ** AND THIS IS NOT "NO ROUTE '
      'EXISTS": B59\'s composite/emergent route is untouched and unexamined **',
      dims[1] == 0 and _gap_corpus == 3 and _fmax < 1e-12 and FACE in P13 and LEAF in P14,
      'closed on the locus; (1) closed on the kernel reading; (3) vacuous; (4) zero')
check('** AND THE PRE-REGISTERED PREDICTION IS SCORED HONESTLY: B61 priced the risk as J or the '
      'order-one condition; PREDICTION.md priced it as the LOCUS, reached first.  The locus fires and '
      'the order-one condition does NOT close the route -- it passes vacuously -- so the registered '
      'call holds and B61\'s expected killer is not the one that fired **',
      dims[1] == 0 and _d3 < 1e-12, 'locus closes it; order-one passes vacuously')

print()
bad = [n for n, ok in CHECKS if not ok]
print(f'  {len(CHECKS)} checks, {len(CHECKS) - len(bad)} pass, {len(bad)} fail')
for n in bad:
    print(f'    FAILED: {n}')
print()
print('=' * 78)
print(' ALL CHECKS PASS' if not bad else ' FAILURES ABOVE')
print('=' * 78)
sys.exit(1 if bad else 0)
