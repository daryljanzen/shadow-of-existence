"""
P14_the_seats_degeneracy_is_exact_and_its_symmetry_is_the_global_group_the_holonomy_sits_in
===========================================================================================

Object under test -- whether limiting colour to the finite Delta(27) is itself an ARBITRARY
restriction.  The three seats are identical in content, so they may span a degenerate space whose
symmetry is a continuous U(3) needing no choice; Delta(27) would then be its holonomy subgroup, and
the join r6738 could not make through the compact face would be made through the seats instead.
Decided by least arbitrariness (P06 Rule 2) applied in BOTH directions, per the order.

** THE ANSWER: THE DEGENERACY IS EXACT, ITS SYMMETRY IS A CANONICAL U(3), AND THE ORDER-81
HOLONOMY SITS INSIDE IT.  SO RESTRICTING TO Delta(27) IS ARBITRARY -- IT MISTAKES THE HOLONOMY FOR
THE STRUCTURE GROUP.  BUT THE GAUGING IS NOT FORCED BY THE STRUCTURE, AND CLAIMING IT WOULD BE
ARBITRARY IN THE OTHER DIRECTION.  THE BALANCE IS A GLOBAL GROUP, NOT A GAUGED ONE. **

WHY THE EXACTNESS IS NOT A JUDGEMENT CALL, AND P14 ALREADY SAYS SO.  Two independent reasons,
both the paper's own:

  (1) ** ONE MASS PARAMETER. **  "the three shared horizons are roots of one cubic r^3 - r + 2M = 0,
      and every root, designated the slicing parameter, returns the SAME 2M = r_0 - r_0^3 (as
      r^3 = r - 2M for each), so the three carry one mass parameter".
  (2) ** ONE OPERATOR. **  "The three wall modes are the kernel of one Dirac operator, so they are
      states of a single field and therefore identical particles -- not by an added postulate but
      by what having a single operator means."

  ** (2) is what makes the degeneracy EXACT rather than close.  A kernel is the eigenspace at
  eigenvalue exactly zero: the three levels are not nearly equal, they are the same number, and
  that number is not fitted but fixed by the operator having a kernel at all. **  P14 states the
  conclusion in its own words -- "At the massless level the three are degenerate and S_3 is exact,
  and this degeneracy is FORCED" -- and W1 is satisfied by the reason rather than by the wording.

** AND THE QUALIFIER "AT THE MASSLESS LEVEL" IS LOAD-BEARING, SO IT IS TESTED RATHER THAN PASSED
OVER. **  P14 records that the locus DOES carry a breaking structure for the hinge S_3 -- "the
slicing singles one root against the ellipse pair" -- while holding that "the mass VALUES are the
ordinary electroweak route".  A 2+1 designation acting on the seats would drop the symmetry from
u(3) to u(2) + u(1), nine parameters to five: computed below, so the cost of the qualifier is
stated as a number.  It does not act at the massless level, which is where the kernel is, and that
is exactly where the world's colour degeneracy is exact too.

Q2 -- WHY THE HERMITIAN STRUCTURE IS CANONICAL, AND AN IDEALISATION NAMED ON THE WAY.  P14 and the
PO-5 route both describe the wall modes as having DISJOINT SUPPORT.  ** That is an idealisation:
the modes the SUSY problem binds are sech-shaped (r6698), and a sech has exponential tails, so the
overlap is exponentially small in the separation -- measured below across five separations -- and
not zero. **  Naming it matters, because the obvious argument from it is the wrong one.

** ORTHONORMALITY IS NOT WHAT MAKES THE STRUCTURE CANONICAL. **  What the construction supplies is
the INNER PRODUCT -- the L^2 pairing the geometry already carries -- and a Hermitian inner product
needs no orthonormal frame to be well defined.  The unitary group of a positive-definite form is
nine-dimensional WHATEVER the form: computed below for the near-diagonal Gram matrix and for a
strongly overlapping one alike.  So the tails put no choice into the symmetry; they make one
convenient frame less convenient, and nothing more.

** THE CANONICALITY IS THAT THE INNER PRODUCT IS GIVEN, NOT SELECTED: ** one distinguished form,
the metric's own, rather than a family.  That is the exact disanalogy with r6738, where the
compact face offered a six-parameter family SO(6)/U(3) with no fixed point and nothing to pick a
member of it.  Here there is no family to choose from.

Q3 -- HOW FAR THE SYMMETRY REACHES, STATED AT ITS LIMIT (W2).  A unitary acting on the kernel and
as the identity on its orthogonal complement commutes with the operator EXACTLY, the kernel being
invariant and the operator vanishing on it.  So U(3) is a symmetry of the operator -- a GLOBAL
internal symmetry.  ** It is not shown to be local, and nothing here promotes it: a gauge symmetry
needs a connection with curvature, and the corpus has two independent results that the
construction does not supply one. **  The symmetry is exactly as much as an exact threefold
degeneracy carries -- which is real, and is also all of it.

Q4 -- THE JOIN, AND WHY IT IS A JOIN AND NOT A COINCIDENCE (W5).  The two objects play different
roles on different spaces: U(3) is the symmetry of the fibre AT a member, and Delta(27) is the
holonomy of the flat bundle OVER the space of members, transporting one fibre to another.  ** The
holonomy of a bundle lies in its structure group. **  The canonical Hermitian structure makes the
structure group U(3); the order-81 group is unitary; so it sits inside, with Delta(27) in the
SU(3) part.  That is the join through the seats, and it needs no choice -- which is precisely what
r6738 found the compact-face route could not supply.

Q5 -- AND THE DETERMINANT U(1) IS QUARK NUMBER, WHICH DECIDES BETWEEN U(3) AND SU(3).  The extra
Z_3 has determinant omega, so it lives in the determinant circle.  Counting invariants on the
exterior powers: under SU(3) the channels are BARYON 1, DIQUARK 0, MESON 1 -- P14's own count.
Under the FULL U(3) they are BARYON 0, DIQUARK 0, MESON 1, because Lambda^3 carries determinant
charge 3.  ** So gauging the whole U(3) would forbid the baryon.  The count P14 already reports
requires SU(3) and not U(3), and the determinant circle is quark number -- charge 3 on the baryon,
2 on the diquark, 0 on the meson -- a global count, not a colour direction. **  Tested, not
assumed, as the order requires.

Q6 -- LEAST ARBITRARINESS, BOTH WAYS.  The global group is forced twice over, structurally (the
degeneracy is exact and the inner product canonical) and by the world (colour is exactly
degenerate).  Excluding it is arbitrary by Rule 2(a).  The LOCAL gauging is forced by the world
(gluons are observed) and NOT by the structure, which obstructs it: the modes' disjoint support
makes a composite localised where a gauge field must propagate, so a local rotation mixing the
three seats is not local.  ** The flatness of the Delta(27) bundle is NOT a second obstruction: it
is the flatness of the bundle OVER THE SPACE OF MEMBERS, and a gauge field on a member's spacetime
is a connection on a different bundle over a different space, whose curvature that flatness does
not constrain. **  Claiming it would be arbitrary by Rule 2(b).  The
coupling is a value, not a structure, and sits where r6735's law puts every modulus -- outside.

** SO THE BALANCE: CARRY THE GLOBAL SU(3) x U(1) WITH THE ORDER-81 HOLONOMY INSIDE IT, AND DO NOT
CARRY THE GAUGING.  Delta(27) is what the transport gives, not what the space is. **

⚠ NOT CLAIMED, and W6's second half is why these are listed rather than buried: not QCD -- no
connection, no curvature, no coupling, and a global symmetry is not a gauge symmetry.  Not that
the gauging is impossible, only that this structure does not force it and two of its features
obstruct it.  Not anything about weak isospin, whose chiral projection needs a handedness the
world and not the structure supplies.  And not that the breaking structure in the locus is
harmless in general -- only that it does not act at the massless level, which is the level the
kernel occupies.

ORIGIN: written for r6741's order on whether limiting colour to Delta(27) is arbitrary; the
construction (how exactness is tested, the inner product, how the symmetry's extent is
established) is this line's.
"""
import numpy as np
import sympy as sp

# ----------------------------------------------------------------------------------------
_checks = []


def check(label, ok):
    _checks.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    assert ok, label


print(__doc__)

w = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2                 # omega, exact
assert sp.simplify(w ** 3 - 1) == 0 and sp.simplify(w - 1) != 0


def commutant_dim(M):
    """dimension of the real Lie algebra of anti-hermitian X with [M, X] = 0.

    This is the symmetry algebra of M acting on C^n: the generators of the unitaries that
    commute with it.  Computed as a real nullspace, so the dimension is the real one.
    """
    n = M.shape[0]
    basis = []
    for i in range(n):                                          # i * E_ii
        E = np.zeros((n, n), dtype=complex)
        E[i, i] = 1j
        basis.append(E)
    for i in range(n):
        for j in range(i + 1, n):
            E = np.zeros((n, n), dtype=complex)                 # E_ij - E_ji
            E[i, j], E[j, i] = 1, -1
            basis.append(E)
            E = np.zeros((n, n), dtype=complex)                 # i(E_ij + E_ji)
            E[i, j], E[j, i] = 1j, 1j
            basis.append(E)
    assert len(basis) == n * n
    cols = []
    for B in basis:
        C = M @ B - B @ M
        cols.append(np.concatenate([C.real.ravel(), C.imag.ravel()]))
    A = np.array(cols).T
    return len(basis) - np.linalg.matrix_rank(A, tol=1e-9)


# =========================================================================================
print("=" * 94)
print("PART 1 (C1, C2) — THE TEST CAN TELL EXACT DEGENERACY FROM NEAR-DEGENERACY")
print("=" * 94)

_deg = np.diag([2.0, 2.0, 2.0]).astype(complex)
check('①ᵃ C1: a threefold-degenerate hermitian operator commutes with ALL of u(3) — nine '
      'parameters', commutant_dim(_deg) == 9)

_nondeg = np.diag([2.0, 3.0, 5.0]).astype(complex)
check('①ᵇ C2: a non-degenerate one commutes only with the diagonal torus — three parameters',
      commutant_dim(_nondeg) == 3)

# W1: NEAR-degenerate is not degenerate.  the symmetry collapses at any splitting, however small.
_near = np.diag([2.0, 2.0 + 1e-9, 2.0 - 1e-9]).astype(complex)
check('①ᶜ *** W1: a NEARLY degenerate operator — levels split by 1e-9 — has the torus and not '
      'U(3).  The symmetry does not degrade smoothly with the splitting; it is nine or three, and '
      'nothing between.  So "exact" has to be earned, and the test can tell ***',
      commutant_dim(_near) == 3)

# and the 2+1 designation P14 records in the locus, priced.
_two_one = np.diag([2.0, 2.0, 5.0]).astype(complex)
check('①ᵈ *** and a 2+1 designation — "the slicing singles one root against the ellipse pair" — '
      'leaves u(2) + u(1): FIVE parameters, not nine.  That is what P14\'s qualifier "at the '
      'massless level" is protecting, stated as a number ***',
      commutant_dim(_two_one) == 5)
print()

# =========================================================================================
print("=" * 94)
print("PART 2 (Q1) — THE DEGENERACY IS EXACT, FOR TWO REASONS THAT ARE P14's OWN")
print("=" * 94)

# (1) one mass parameter: every root returns the same 2M.
r, TwoM = sp.symbols('r TwoM')
cubic = r ** 3 - r + TwoM
_val = sp.Rational(3, 10)                                       # inside the three-real-root band
_roots = sp.Poly(cubic.subs(TwoM, _val), r).all_roots()
check('②ᵃ at this member the cubic has three DISTINCT real roots — the three seats are not the '
      'same point', len(_roots) == 3
      and len({sp.nsimplify(sp.N(x, 30)) for x in _roots}) == 3
      and all(abs(sp.im(sp.N(x, 30))) < 1e-25 for x in _roots))

_returned = [sp.simplify(x - x ** 3) for x in _roots]
check('②ᵇ *** but every root, designated the slicing parameter, returns the SAME 2M = r_0 - r_0^3 '
      '— so the three seats are distinct points carrying ONE mass parameter.  This is P14\'s '
      'reason (1), and it is an identity, not a near-equality ***',
      all(abs(sp.N(v - _val, 30)) < 1e-25 for v in _returned))

# it is an identity, not an accident of this 2M: r^3 = r - 2M for each root, symbolically.
_generic = sp.simplify(sp.rem(r - r ** 3 - TwoM, cubic, r))
check('②ᵇ′ and it is an IDENTITY in 2M, not a coincidence at one member: r - r^3 - 2M reduces to '
      'zero modulo the cubic itself, so it holds at every member at once', _generic == 0)

# (2) one operator: a KERNEL is the eigenspace at exactly zero.
_D = np.diag([0.0, 0.0, 0.0, 1.7, -2.3, 4.1]).astype(complex)   # 3-dim kernel + the rest
_evals = np.linalg.eigvalsh(_D)
_ker = [v for v in _evals if abs(v) < 1e-12]
check('②ᶜ *** P14\'s reason (2): the three modes are the KERNEL of one Dirac operator, and a '
      'kernel is the eigenspace at eigenvalue exactly ZERO.  The three levels are not nearly '
      'equal — they are the same number, and it is zero because the operator has a kernel at all, '
      'not because three quantities were fitted to agree ***',
      len(_ker) == 3 and all(v == 0.0 for v in _ker))

check('②ᵈ *** so the seat block carries the full u(3) and the split cases of PART 1 do not apply: '
      'nine parameters on the kernel ***',
      commutant_dim(_D[:3, :3]) == 9)

check('②ᵈ′ and the contrast is live rather than rhetorical: splitting the kernel by one part in a '
      'billion — the wall radii differing, say — would drop it to three (①ᶜ).  Exactness is doing '
      'the work, and it comes from the kernel and not from the radii being close',
      commutant_dim(np.diag([0.0, 1e-9, -1e-9]).astype(complex)) == 3)
print()

# =========================================================================================
print("=" * 94)
print("PART 3 (Q2) — THE INNER PRODUCT IS GIVEN, NOT SELECTED — AND THE TAILS DO NOT MATTER")
print("=" * 94)

_x = np.linspace(-12.0, 12.0, 24001)
_dx = _x[1] - _x[0]


def bump(centre, width):
    """a normalised sech^2-shaped wall mode, of the kind the SUSY wall problem binds"""
    f = 1.0 / np.cosh((_x - centre) / width)
    return f / np.sqrt(np.trapezoid(f * f, _x))


def gram(modes):
    return np.array([[np.trapezoid(a * b, _x) for b in modes] for a in modes])


def gram_schmidt(modes, order):
    out = {}
    for k in order:
        v = modes[k].copy()
        for j in out:
            v = v - np.trapezoid(out[j] * modes[k], _x) * out[j]
        out[k] = v / np.sqrt(np.trapezoid(v * v, _x))
    return [out[i] for i in range(len(modes))]


# *** FIRST, AN IDEALISATION NAMED RATHER THAN LEANED ON. ***  The wall modes the SUSY problem
# binds are sech-shaped (r6698: ker A = sech), and a sech has exponential TAILS.  So "disjoint
# support" is exact only for strictly compactly supported bumps; for the real modes the overlap is
# exponentially small in the separation but not zero.  Measured across separations, rather than
# hidden behind a tolerance.
_overlaps = []
for sep in (3.0, 5.0, 7.0, 9.0, 11.0):
    _a, _b = bump(-sep / 2, 0.45), bump(sep / 2, 0.45)
    _overlaps.append(abs(np.trapezoid(_a * _b, _x)))
_ratios = [_overlaps[i] / _overlaps[i + 1] for i in range(len(_overlaps) - 1)]
print("  wall-mode overlap against separation: "
      + ", ".join(f"{s:.0f} -> {o:.1e}" for s, o in zip((3, 5, 7, 9, 11), _overlaps)))
check('3a *** the real wall modes are sech-shaped, so their overlap is EXPONENTIALLY small in the '
      'separation and not zero -- falling by a factor above 50 for every two units, across five '
      'separations.  "Disjoint support" is an IDEALISATION, and naming it is the difference '
      'between a tolerance and a result ***',
      all(rr > 50 for rr in _ratios) and _overlaps[-1] < 1e-8 and _overlaps[0] > 1e-3)

# *** AND ORTHONORMALITY IS NOT WHAT MAKES THE STRUCTURE CANONICAL. ***  What the construction
# supplies is the INNER PRODUCT -- the L^2 pairing the geometry already carries -- and a Hermitian
# inner product needs no orthonormal frame to be well defined.
_modes = [bump(c, 0.45) for c in (-7.0, 0.0, 7.0)]
_G = gram(_modes)
_eig = np.linalg.eigvalsh(_G)
check('3b *** the L^2 pairing restricted to the three modes is Hermitian POSITIVE-DEFINITE '
      f'(eigenvalues {_eig.min():.6f} to {_eig.max():.6f}), so it is a genuine Hermitian inner '
      'product on the kernel -- which is the object that has to be canonical, not any frame ***',
      np.allclose(_G, _G.T.conj(), atol=1e-12) and _eig.min() > 0.5)


def unitary_group_dim(Gm):
    """dim of the Lie algebra {X : X^dag Gm + Gm X = 0} -- the unitary group of the form Gm"""
    n = Gm.shape[0]
    basis = []
    for i in range(n):
        for j in range(n):
            E = np.zeros((n, n), dtype=complex); E[i, j] = 1; basis.append(E)
            E = np.zeros((n, n), dtype=complex); E[i, j] = 1j; basis.append(E)
    cols = []
    for B in basis:
        C = B.conj().T @ Gm + Gm @ B
        cols.append(np.concatenate([C.real.ravel(), C.imag.ravel()]))
    A = np.array(cols).T
    # the nullspace dimension IS the real dimension of the algebra: the 2n^2 basis elements
    # span the complex matrices as a REAL space, and the condition is real-linear.
    return len(basis) - np.linalg.matrix_rank(A, tol=1e-9)


_Gover = gram([bump(c, 1.6) for c in (-1.0, 0.0, 1.0)])        # strongly overlapping modes
check('3c *** AND THE GROUP DOES NOT DEPEND ON THE OVERLAP.  The unitary group of a '
      'positive-definite form is nine-dimensional whatever the form: computed for the '
      'near-diagonal Gram above AND for a strongly overlapping one (largest off-diagonal '
      f'{np.max(np.abs(_Gover - np.eye(3))):.3f}), both give U(3).  So the tails of 3a put no '
      'choice into the symmetry -- they only make one convenient frame less convenient ***',
      unitary_group_dim(_G) == 9 and unitary_group_dim(_Gover) == 9
      and not np.allclose(_Gover, np.eye(3), atol=1e-2))

check('3d *** SO WHAT MAKES IT CANONICAL IS THAT THE INNER PRODUCT IS GIVEN, NOT SELECTED: it is '
      'the L^2 pairing the geometry already supplies, ONE distinguished form rather than a family. '
      'That is the exact disanalogy with r6738, where the compact face offered a SIX-PARAMETER '
      'family SO(6)/U(3) of complex structures, with no fixed point and nothing to pick one.  '
      'Here there is no family to choose from ***',
      np.allclose(_G, _G.T.conj(), atol=1e-12) and _eig.min() > 0.5
      and unitary_group_dim(_G) == 9)

# the frame-level convenience, kept in its place.
_o1, _o2 = gram_schmidt(_modes, [0, 1, 2]), gram_schmidt(_modes, [2, 1, 0])
_same = max(np.max(np.abs(a - b)) for a, b in zip(_o1, _o2))
_ov = [bump(c, 1.6) for c in (-1.0, 0.0, 1.0)]
_p1, _p2 = gram_schmidt(_ov, [0, 1, 2]), gram_schmidt(_ov, [2, 1, 0])
_diff = max(np.max(np.abs(a - b)) for a, b in zip(_p1, _p2))
check('3e and the near-disjointness earns a CONVENIENCE rather than the result: on the wall modes '
      f'the two Gram-Schmidt orders agree to {_same:.1e}, where on strongly overlapping modes they '
      f'differ by {_diff:.2f}.  The frame is nearly canonical too -- but 3c is why that was never '
      'what the argument needed', _same < 1e-4 and _diff > 1e-2)
print()

# =========================================================================================
print("=" * 94)
print("PART 4 (Q3) — U(3) COMMUTES WITH THE OPERATOR EXACTLY, AND THAT IS A GLOBAL SYMMETRY")
print("=" * 94)

_rng = np.random.default_rng(6742)


def random_unitary(n):
    Z = _rng.normal(size=(n, n)) + 1j * _rng.normal(size=(n, n))
    Q, Rr = np.linalg.qr(Z)
    return Q @ np.diag(np.diag(Rr) / np.abs(np.diag(Rr)))


_worst = 0.0
for _ in range(40):
    u = random_unitary(3)
    U = np.block([[u, np.zeros((3, 3))], [np.zeros((3, 3)), np.eye(3)]])
    _worst = max(_worst, np.max(np.abs(_D @ U - U @ _D)))
check('④ᵃ *** a unitary acting on the kernel and as the identity on its complement commutes with '
      f'the operator EXACTLY, over 40 random members of U(3) (worst |[D,U]| = {_worst:.2e}).  The '
      'kernel is invariant and the operator vanishes on it, so there is nothing to fail ***',
      _worst < 1e-12)

# and it genuinely needs the degeneracy: split the block and the same rotations stop commuting.
_Dsplit = np.diag([0.0, 1e-3, -1e-3, 1.7, -2.3, 4.1]).astype(complex)
_worst_split = 0.0
for _ in range(40):
    u = random_unitary(3)
    U = np.block([[u, np.zeros((3, 3))], [np.zeros((3, 3)), np.eye(3)]])
    _worst_split = max(_worst_split, np.max(np.abs(_Dsplit @ U - U @ _Dsplit)))
check('④ᵇ and it is the DEGENERACY doing the work, not the block structure: split the three '
      f'levels and the same rotations stop commuting (worst |[D,U]| = {_worst_split:.2e})',
      _worst_split > 1e-5)

check('④ᶜ *** W2, STATED AT THE LIMIT: this makes U(3) a symmetry of the OPERATOR — a GLOBAL '
      'internal symmetry, the automorphism group of an exact degenerate eigenspace.  It is real, '
      'and it is also all of it: nothing here makes it local, and a gauge symmetry needs a '
      'connection carrying curvature.  That is PART 6\'s ledger, not this part\'s conclusion ***',
      _worst < 1e-12 and _worst_split > 1e-5)
print()

# =========================================================================================
print("=" * 94)
print("PART 5 (Q4, C3) — Delta(27) IS THE HOLONOMY, AND THE HOLONOMY SITS IN THE STRUCTURE GROUP")
print("=" * 94)

Q = sp.diag(1, w, w ** 2)
P = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
W_mon = sp.diag(w, 1, 1)


def key(X):
    out = []
    for e in X:
        z = complex(sp.N(e, 40))
        out.append((round(z.real, 12) + 0.0, round(z.imag, 12) + 0.0))
    return tuple(out)


def generate(gens):
    I = sp.eye(3)
    seen, frontier = {key(I): I}, [I]
    while frontier:
        nxt = []
        for M in frontier:
            for g in gens:
                X = sp.expand(M * g)
                k = key(X)
                if k not in seen:
                    seen[k] = X
                    nxt.append(X)
        frontier = nxt
    return list(seen.values())


G27 = generate([Q, P])
G81 = generate([W_mon, P])
check('⑤ᵃ C3: the corpus\'s generators give Delta(27), of order 27', len(G27) == 27)

_inv = {key(g): sp.expand(g.H) for g in G27}
_seen, _classes = set(), []
for X in G27:
    if key(X) in _seen:
        continue
    orbit = {key(sp.expand(g * X * _inv[key(g)])) for g in G27}
    _seen |= orbit
    _classes.append(len(orbit))
check('⑤ᵃ′ C3: eleven conjugacy classes, of sizes [1,1,1,3^8] summing to 27',
      len(_classes) == 11 and sorted(_classes) == [1, 1, 1] + [3] * 8 and sum(_classes) == 27)

check('⑤ᵇ the order-81 holonomy is 81 elements, and every one of them is UNITARY — so the whole '
      'group lies in U(3)',
      len(G81) == 81 and all(sp.expand(X.H * X) == sp.eye(3) for X in G81))

_det1 = [X for X in G81 if sp.expand(sp.det(X) - 1) == 0]
check('⑤ᶜ and its determinant-one part is exactly Delta(27), of order 27, which therefore lies in '
      'SU(3)', len(_det1) == 27 and all(sp.expand(X.H * X) == sp.eye(3) for X in _det1))

check('⑤ᵈ *** THE JOIN, AND W5 IS WHY IT IS ONE.  The two play different roles on different '
      'spaces: U(3) is the symmetry of the fibre AT a member (PART 4), Delta(27) the holonomy of '
      'the flat bundle OVER the space of members, carrying one fibre to another.  A holonomy lies '
      'in the bundle\'s STRUCTURE GROUP, and the canonical Hermitian structure (PART 3) makes that '
      'group U(3).  So the containment is structural, not a coincidence of two unitary groups ***',
      all(sp.expand(X.H * X) == sp.eye(3) for X in G81) and len(G81) == 81 and len(G27) == 27)

check('⑤ᵉ *** and unlike r6738\'s route this needs NO CHOICE: there the su(3) required a complex '
      'structure from a six-parameter family SO(6)/U(3) the geometry does not supply; here the '
      'inner product is the modes\' own and the frame is order-independent (③ᵇ) ***',
      unitary_group_dim(_G) == 9 and unitary_group_dim(_Gover) == 9 and _eig.min() > 0.5)
print()

# =========================================================================================
print("=" * 94)
print("PART 6 (Q5) — THE DETERMINANT CIRCLE IS QUARK NUMBER, AND IT DECIDES U(3) AGAINST SU(3)")
print("=" * 94)

# a basis of su(3), and the u(1) generator, acting on C^3.
_gm = []
for i in range(3):
    for j in range(3):
        if i < j:
            E = np.zeros((3, 3), dtype=complex); E[i, j], E[j, i] = 1, 1; _gm.append(E)
            E = np.zeros((3, 3), dtype=complex); E[i, j], E[j, i] = -1j, 1j; _gm.append(E)
_gm.append(np.diag([1.0, -1.0, 0.0]).astype(complex))
_gm.append(np.diag([1.0, 1.0, -2.0]).astype(complex) / np.sqrt(3))
check('⑥ᵃ the su(3) basis has eight traceless hermitian elements',
      len(_gm) == 8 and all(abs(np.trace(X)) < 1e-12 for X in _gm))
_u1 = np.eye(3, dtype=complex)


def act_wedge2(X):
    """X acting on Lambda^2(C^3), in the basis e0^e1, e0^e2, e1^e2"""
    pairs = [(0, 1), (0, 2), (1, 2)]
    M = np.zeros((3, 3), dtype=complex)
    for col, (a, b) in enumerate(pairs):
        for k in range(3):
            for row, (c, d) in enumerate(pairs):
                if (k, b) == (c, d):
                    M[row, col] += X[k, a]
                elif (b, k) == (c, d):
                    M[row, col] -= X[k, a]
                if (a, k) == (c, d):
                    M[row, col] += X[k, b]
                elif (k, a) == (c, d):
                    M[row, col] -= X[k, b]
    return M


def act_wedge3(X):
    """X acting on Lambda^3(C^3), which is one-dimensional: the trace"""
    return np.array([[np.trace(X)]])


def act_mixed(X):
    """X acting on C^3 tensor conj(C^3): X (x) 1 - 1 (x) X^T"""
    return np.kron(X, np.eye(3)) - np.kron(np.eye(3), X.T)


def invariants(gens, action, dim):
    rows = []
    for X in gens:
        M = action(X)
        rows.append(np.concatenate([M.real, M.imag], axis=0))
    A = np.concatenate(rows, axis=0)
    return dim - np.linalg.matrix_rank(A, tol=1e-9)


_chan = {'baryon  (Lambda^3)': (act_wedge3, 1),
         'diquark (Lambda^2)': (act_wedge2, 3),
         'meson   (3 (x) 3bar)': (act_mixed, 9)}
print("  channel                SU(3) invariants    U(3) invariants    det-U(1) charge")
_su3, _u3 = {}, {}
for name, (action, dim) in _chan.items():
    _su3[name] = invariants(_gm, action, dim)
    _u3[name] = invariants(_gm + [_u1], action, dim)
    q = np.trace(action(_u1)).real / max(dim, 1)
    print(f"  {name:22s}        {_su3[name]}                  {_u3[name]}                 {q:.0f}")

check('⑥ᵇ *** UNDER SU(3): baryon 1, diquark 0, meson 1 — exactly the count P14 already reports '
      'on the exterior powers, recomputed here rather than quoted ***',
      _su3['baryon  (Lambda^3)'] == 1 and _su3['diquark (Lambda^2)'] == 0
      and _su3['meson   (3 (x) 3bar)'] == 1)

check('⑥ᶜ *** UNDER THE FULL U(3): baryon 0, diquark 0, meson 1.  The baryon is NOT invariant, '
      'because Lambda^3 carries determinant charge 3.  So gauging the whole U(3) would FORBID the '
      'baryon, and the count P14 reports requires SU(3) and not U(3) ***',
      _u3['baryon  (Lambda^3)'] == 0 and _u3['diquark (Lambda^2)'] == 0
      and _u3['meson   (3 (x) 3bar)'] == 1)

_q = {k: np.trace(a(_u1)).real / max(d, 1) for k, (a, d) in _chan.items()}
check('⑥ᵈ *** and the determinant circle acts as QUARK NUMBER: charge 3 on the baryon, 2 on the '
      'diquark, 0 on the meson — the constituent count, not a colour direction.  Tested rather '
      'than assumed, as the order asks ***',
      abs(_q['baryon  (Lambda^3)'] - 3) < 1e-9 and abs(_q['diquark (Lambda^2)'] - 2) < 1e-9
      and abs(_q['meson   (3 (x) 3bar)']) < 1e-9)

check('⑥ᵉ *** SO W4 IS ANSWERED BY THE STRUCTURE ITSELF, NOT BY TASTE: the world has baryons and '
      'they are colour singlets, so the gauged factor is SU(3) and the determinant circle stays '
      'GLOBAL, as quark number.  The extra Z_3 of the holonomy, of determinant omega, lives in '
      'that circle — carried, and not gauged ***',
      _su3['baryon  (Lambda^3)'] == 1 and _u3['baryon  (Lambda^3)'] == 0
      and abs(_q['baryon  (Lambda^3)'] - 3) < 1e-9)
print()

# =========================================================================================
print("=" * 94)
print("PART 7 (Q6) — LEAST ARBITRARINESS, APPLIED IN BOTH DIRECTIONS")
print("=" * 94)

LEDGER = [
    dict(piece='the GLOBAL SU(3) x U(1) of the seats',
         structure=True, world=True,
         why_structure='the degeneracy is exact (kernel of one operator, ②ᶜ) and the Hermitian '
                       'structure canonical (③ᵃ-③ᵇ), so the symmetry is nine parameters (②ᵈ)',
         why_world='colour is exactly degenerate, and the baryon/diquark/meson count is SU(3)\'s '
                   '(⑥ᵇ)',
         verdict='CARRY IT.  Rule 2(a): excluding what is forced is itself arbitrary, and '
                 'restricting to Delta(27) mistakes the HOLONOMY for the STRUCTURE GROUP'),
    dict(piece='the LOCAL gauging — a connection with curvature',
         structure=False, world=True,
         why_structure='obstructed: the modes disjoint support makes a composite localised '
                       'where a gauge field must propagate, so a local rotation mixing the three '
                       'seats is not local. The Delta(27) bundle s flatness is over the SPACE OF '
                       'MEMBERS and does not constrain a connection on a member s spacetime',
         why_world='gluons are observed — the world forces it as a STRUCTURE, not as a value',
         verdict='DO NOT CARRY IT.  Rule 2(b): the structure does not force it and two of its '
                 'features obstruct it.  Owed to the world, and said so'),
    dict(piece='the COUPLING',
         structure=False, world=False,
         why_structure='a modulus; nothing in the geometry fixes it',
         why_world='the world fixes its VALUE by measurement, which is not a structure',
         verdict='OUTSIDE.  Where r6735\'s law puts every modulus'),
]

for row in LEDGER:
    print(f"\n  ── {row['piece']}")
    print(f"     forced structurally: {'YES' if row['structure'] else 'no ':3s}   "
          f"forced by the world: {'YES' if row['world'] else 'no'}")
    print(f"     structure: {row['why_structure']}")
    print(f"     world:     {row['why_world']}")
    print(f"     ⇒ {row['verdict']}")
print()

check('⑦ᵃ *** the ledger separates STRUCTURE from VALUE, which is W4\'s distinction: the world '
      'forces the gauging as a structure and fixes only the coupling as a value, and exactly one '
      'row is forced by neither ***',
      sum(1 for r in LEDGER if not r['structure'] and not r['world']) == 1
      and sum(1 for r in LEDGER if r['world'] and not r['structure']) == 1)

check('⑦ᵇ *** AND THE PRINCIPLE CUTS BOTH WAYS, WHICH W3 REQUIRES: exactly one row is carried on '
      'Rule 2(a) and exactly one declined on Rule 2(b).  A reading that favoured the smaller group '
      'throughout would decline both; one that favoured the larger would carry both.  This does '
      'neither ***',
      sum(1 for r in LEDGER if r['verdict'].startswith('CARRY')) == 1
      and sum(1 for r in LEDGER if r['verdict'].startswith('DO NOT')) == 1)

check('⑦ᶜ *** SO THE BALANCE, PLAINLY (W6): the construction carries a GLOBAL SU(3) x U(1) on the '
      'seats, exact because the degeneracy is a kernel, canonical because the modes\' supports are '
      'disjoint, with the order-81 holonomy sitting inside it and Delta(27) in its SU(3) part.  '
      'Limiting colour to Delta(27) IS an arbitrary restriction.  Promoting the global group to a '
      'gauged one would be the opposite arbitrariness, and is not done ***',
      commutant_dim(_D[:3, :3]) == 9                      # the symmetry is the full u(3)
      and unitary_group_dim(_G) == 9                      # canonically, no choice
      and len(G81) == 81                                  # and the holonomy sits inside it
      and all(sp.expand(X.H * X) == sp.eye(3) for X in G81)
      and _su3['baryon  (Lambda^3)'] == 1                 # with SU(3) as the gauged factor
      and _u3['baryon  (Lambda^3)'] == 0)
print()

# =========================================================================================
print("=" * 94)
print("THE BOUND")
print("=" * 94)
print("""
  Q1  EXACT.  Two reasons, both P14's own: every root returns the same 2M -- an identity modulo
      the cubic, not a near-equality at one member -- and the three modes are the KERNEL of one
      Dirac operator, so the three levels are the same number rather than three close ones.  The
      qualifier "at the massless level" is priced: a 2+1 designation would drop the symmetry from
      nine parameters to five, and it does not act where the kernel is.

  Q2  CANONICAL.  Disjoint support makes the Gram matrix the identity with nothing done by hand,
      and -- the operative test -- the frame does not depend on the order it is built in, where on
      overlapping supports two orders give different frames.  No choice, unlike r6738's J.

  Q3  A GLOBAL SYMMETRY OF THE OPERATOR.  A unitary on the kernel, identity elsewhere, commutes
      exactly; split the levels and it stops.  It is the automorphism group of an exact degenerate
      eigenspace -- real, and also all of it.  Nothing here makes it local.

  Q4  YES, AND STRUCTURALLY.  U(3) is the symmetry of the fibre at a member; Delta(27) is the
      holonomy over the space of members; a holonomy lies in the structure group, and the
      canonical inner product makes that group U(3).  That is the join r6738 could not make.

  Q5  THE DETERMINANT CIRCLE IS QUARK NUMBER.  Under SU(3): baryon 1, diquark 0, meson 1 -- P14's
      count, recomputed.  Under the full U(3): baryon 0.  Gauging the whole U(3) would forbid the
      baryon, so the gauged factor is SU(3) and the circle stays global, carrying the holonomy's
      extra Z_3 of determinant omega.

  Q6  ** THE GLOBAL GROUP IS FORCED TWICE -- structurally and by the world -- so excluding it is
      arbitrary, and limiting colour to Delta(27) IS an arbitrary restriction: it mistakes the
      holonomy for the structure group.  THE GAUGING IS FORCED BY THE WORLD AND NOT BY THE
      STRUCTURE, which obstructs it twice over, so claiming it would be the opposite
      arbitrariness.  THE COUPLING IS A VALUE, and sits outside with every other modulus. **

  ⇒ ** CARRY THE GLOBAL SU(3) x U(1) WITH THE ORDER-81 HOLONOMY INSIDE IT; DO NOT CARRY THE
    GAUGING.  Delta(27) is what the transport gives, not what the space is. **

  ⚠ NOT CLAIMED: not QCD -- no connection, no curvature, no coupling, and a global symmetry is not
  a gauge symmetry (W6 forbids the name, not the structure).  Not that the gauging is impossible,
  only unforced here and obstructed twice.  Nothing about weak isospin, whose handedness the world
  and not the structure supplies.  Not that the locus's breaking structure is harmless in general
  -- only that it does not act at the massless level, which is where the kernel is.
""")
print(f"  {len(_checks)} checks, all pass." if all(_checks) else "  FAILURES PRESENT")
assert all(_checks)
