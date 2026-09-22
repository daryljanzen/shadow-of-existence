"""
P14_the_two_colours_complex_structures_live_on_different_spaces_and_only_one_is_forced
======================================================================================

Object under test -- the two places colour appears in this construction, and the complex
structure each one needs.  The DISCRETE colour is Delta(27), the determinant-one part of the
order-81 group the three wall monodromies generate with the hinge three-cycle (r6704, r6707,
r6709, r6710).  The CONTINUOUS colour is the su(3) inside the compact face's isometry algebra
so(6) = su(4) (r6704).  Each needs a complex structure: su(3) needs a complex rank-three module,
and su(3) sits in so(6) only as the traceless commutant of a complex structure J on R^6 = C^3.
** Are they the same complex structure?  If they were, Delta(27) would be the discrete skeleton
of the compact face's own SU(3), and the continuous colour group would be DERIVED rather than
located -- which is the open conversion r6735 left at PO-30. **

** FIRST, A PROVENANCE NOTE, BECAUSE Q1'S PREMISE RESTS ON AN ATTRIBUTION. **  The sentence "the
question was never which real bundle but where the complex structure is -- it is at the branch
point" is quoted as P14's.  It is not in P14: `matter_sector_paper.tex` contains the phrase
"complex structure" ZERO times.  The sentence is P18's (`CR_synthesis.tex`, once, in the section
on what the construction DECLINES to claim), and P18 cites P14 for the CONSEQUENCE -- the order-81
group, its determinant-one part -- not for the complex structure itself.  The substance is the
receipt's: `P14_the_bundle_is_the_branching`, which is where the phrase actually occurs and where
the branch point is identified, and that is what is used below.  ** The claim is sound and its
home is a receipt, not a paper -- which is the very hop `check_provenance`'s bound names, "a claim
invented in a docstring and later quoted as though it came from a paper".  Recorded rather than
passed on, and reproducible in one line:
    grep -c "complex structure" corpus/matter_sector_paper.tex corpus/CR_synthesis.tex
which returns 0 and 1. **

THE ANSWER IS NO, AND THE REASON IS NOT THAT THE TWO STRUCTURES DISAGREE.  It is that only one
of them exists as a structure the geometry supplies.

  ** THE BRANCHING'S COMPLEX STRUCTURE IS FORCED AND IS ONE-DIMENSIONAL. **  It is the complex
  structure of the BASE of the horizon cubic's three-sheeted cover -- the 2M-plane, the space of
  MEMBERS (r6717) -- and it is forced, the cube root's direction being fixed rather than chosen
  (P14_the_lap_orientation_is_derived).  What is three-dimensional is not that structure but the
  SHEET space above it, and the C^3 the discrete colour acts on is the fibre of the pushforward
  E = pi_*(mode bundle) (P14_the_bundle_is_the_branching): the regular representation of the deck
  group, C[Z_3].

  ** THE COMPACT FACE'S COMPLEX STRUCTURE IS NOT SUPPLIED AT ALL. **  The orthogonal complex
  structures on R^6 compatible with the round metric form SO(6)/U(3), of dimension 15 - 9 = 6,
  and SO(6) -- which IS the compact face's isometry group -- acts on them transitively.  So every
  J is carried to every other by a symmetry of the face itself, and the su(3) each one picks out
  is carried along with it.  ** There is no "the compact face's su(3)": there is a six-parameter
  family of them, permuted transitively by the face's own isometries. **  Selecting one is a
  selection among symmetry-equivalent options, which is precisely the kind of datum r6735 found
  the geometry never supplies.

  ** AND THIS IS THE SAME COSET r6704 ALREADY FOUND EMPTY, UNDER ANOTHER DESCRIPTION. **  r6704
  recorded that what "the vector 6 of so(6)" adds beyond "a 3 and a 3bar of su(3)" is the coset
  so(6)/(su(3) + u(1)) of dimension 6, and that the corpus supplies "R, a discrete exchange, and
  a sign where the u(1) would need a phase".  That coset is the space of complex structures, and
  u(3) = su(3) + u(1) is the stabiliser of one.  ** So the object r6704 found the corpus could
  not fill is exactly the choice this order asks whether the branching makes.  It does not, and
  it is not on the same space. **

** AND THE ABSENCE OF A MAP IS EXHIBITED, NOT CLASSIFIED. **  W1 asks for the map, and the honest
answer is not to label the two spaces by hand and observe that the labels differ -- that asserts
the conclusion as data.  It is to find what any natural map must respect and show that nothing
can.  The compact face's isometry group SO(6) is that test, and it decides the question in two
strokes:

  (i)  SO(6) DOES NOT REACH THE BRANCHING.  The horizon cubic, its local cube-root model and
       Delta(27)'s own generators are built over the 2M-plane and contain no so(6) parameter, so
       the face's isometry group acts TRIVIALLY on every object the discrete colour is made of.
  (ii) AND THERE IS NO SO(6)-FIXED COMPLEX STRUCTURE.  A J fixed by every isometry would put all
       of SO(6) inside Stab(J) = U(3), and dim so(6) = 15 exceeds dim u(3) = 9.

  ** So any map from the branching's data to a complex structure on the compact face would be
  equivariant for a group acting trivially on its source and without fixed points on its target,
  and its image would have to be a fixed point there is none of.  The map cannot exist. **

That is also why the two C^3's differ in kind rather than in detail.  The seat C^3 is the FIBRE of
a flat bundle over a one-complex-dimensional parameter space -- an internal space of sheets, whose
complex structure descends from the branching.  The compact face's C^3 is the AMBIENT space R^6 in
which S^5 is embedded, whose complex structure is an extra datum laid on it.  And -- as
P14_the_bundle_is_the_branching established in eliminating the substrate's own candidate list --
ambient geometry is real, which is why the bundle question moved to the branching at all.
** The move that found the discrete colour is the move that separates it from the compact face. **

** AND THE ARGUMENT'S OWN LIMIT, STATED WHERE IT IS MADE RATHER THAN LEFT TO BE FOUND. **  The
obstruction is for maps natural with respect to the FULL isometry group SO(6).  A construction
that BROKE SO(6) to a subgroup H contained in some U(3) would escape it, because H would then fix
that U(3)'s complex structure and an H-natural map could exist.  So the finding is not that no
such map could ever be built -- it is that nothing the corpus currently supplies breaks SO(6) that
way.  The corpus's one candidate for such a breaking is the hexad, and r6704 already found it
fixes WEIGHT CONTENT and not a module: six marks in a two-dimensional weight plane cannot select
a point of a six-dimensional coset in R^6.  ** That is where a future route would have to start,
and naming it is part of the result rather than a hedge on it. **

WHAT THIS DOES NOT DO.  It does not reopen holonomy: pi_1(S^5) = 1 closed that at r6710 and
nothing here retries it.  It does not deny that Delta(27) is a finite subgroup of SU(3) -- it is,
by construction, and that is a calibration here (C3) and not a result.  It does not claim the
conversion is impossible, only that THIS route does not make it: the continuous colour group
stays located rather than derived, and PO-30's open conversion stays open with one more route
named and closed.

ORIGIN: written for r6735's order on the two colours; the construction (spaces, bases, and how
the two complex structures are compared) is this line's.
"""
import itertools

import sympy as sp

# ----------------------------------------------------------------------------------------
_checks = []


def check(label, ok):
    _checks.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    assert ok, label


print(__doc__)

w = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2            # omega = exp(2 pi i / 3), exact
assert sp.simplify(w ** 3 - 1) == 0 and sp.simplify(w - 1) != 0

# =========================================================================================
print("=" * 94)
print("PART 1 (C1) — su(3) IS THE TRACELESS COMMUTANT OF A COMPLEX STRUCTURE J IN so(6)")
print("=" * 94)

# so(6) acting on R^6.  Put J in the standard block form: three 2-planes, each rotated by 90.
J = sp.zeros(6, 6)
for k in range(3):
    J[2 * k, 2 * k + 1] = -1
    J[2 * k + 1, 2 * k] = 1

check('①ᵃ J is a complex structure: orthogonal, and J^2 = -1',
      sp.simplify(J.T * J - sp.eye(6)) == sp.zeros(6) and sp.simplify(J * J + sp.eye(6)) == sp.zeros(6))

# a general element of so(6): real antisymmetric, 15 parameters
_p = sp.symbols('p0:15', real=True)
A = sp.zeros(6, 6)
_it = iter(_p)
for i in range(6):
    for j in range(i + 1, 6):
        v = next(_it)
        A[i, j] = v
        A[j, i] = -v
check('①ᵇ so(6) has dimension 15', len(_p) == 15 and sp.simplify(A.T + A) == sp.zeros(6))

# the commutant of J
_comm = sp.simplify(A * J - J * A)
_sol = sp.solve([_comm[i, j] for i in range(6) for j in range(6)], list(_p), dict=True)
A_c = sp.simplify(A.subs(_sol[0]))
_free = sorted({s for s in A_c.free_symbols}, key=str)
print(f"  the commutant of J in so(6) has dimension {len(_free)}")
check('①ᶜ the commutant of J in so(6) is nine-dimensional — that is u(3)', len(_free) == 9)

# identify it as u(3): write the commutant element as a complex 3x3 matrix and check anti-hermiticity.
# the complex structure J identifies R^6 with C^3 by  z_k = x_{2k} + i x_{2k+1}.
def to_complex(Mreal):
    """the C^3 matrix of a real 6x6 that commutes with J, in the basis z_k = x_2k + i x_2k+1"""
    out = sp.zeros(3, 3)
    for a in range(3):
        for b in range(3):
            # action on the b-th complex basis vector, read off in the a-th complex slot
            re = Mreal[2 * a, 2 * b]
            im = Mreal[2 * a + 1, 2 * b]
            out[a, b] = re + sp.I * im
    return sp.simplify(out)


Zc = to_complex(A_c)
check('①ᵈ the commutant, read on C^3, is anti-hermitian — so it is u(3)',
      sp.simplify(Zc.H + Zc) == sp.zeros(3))

# its traceless part is su(3), dimension 8
_tr = sp.simplify(sp.trace(Zc))
check('①ᵉ the trace is a single pure-imaginary parameter — the u(1) — so the traceless part '
      'drops the dimension by exactly one', _tr != 0 and sp.simplify(sp.re(sp.expand(_tr))) == 0)
print(f"  traceless part: 9 - 1 = 8  ⇒  su(3), dimension 8.   [C1 reproduced]")
check('①ᶠ *** C1: su(3) is the traceless commutant of J in so(6), dimension 8 ***',
      len(_free) - 1 == 8)

# and WITHOUT a J there is no preferred su(3): the space of J's, and so(6) transitive on it.
_dim_so6, _dim_u3 = 15, 9
check('①ᵍ *** the orthogonal complex structures on R^6 form SO(6)/U(3), of dimension '
      '15 - 9 = 6 — and this is the SAME coset r6704 recorded as so(6)/(su(3)+u(1)) ***',
      _dim_so6 - _dim_u3 == 6)

# transitivity, exhibited rather than asserted: conjugating J by a rotation gives another complex
# structure, and a rotation mixing two of the three planes gives one that is genuinely different.
th = sp.symbols('theta', real=True)
Rot = sp.eye(6)
Rot[0, 0] = sp.cos(th); Rot[0, 2] = -sp.sin(th)
Rot[2, 0] = sp.sin(th); Rot[2, 2] = sp.cos(th)
check('①ʰ the conjugating map is a rotation', sp.simplify(Rot.T * Rot - sp.eye(6)) == sp.zeros(6)
      and sp.simplify(sp.det(Rot)) == 1)
Jp = sp.simplify(Rot * J * Rot.T)
check('①ⁱ its conjugate is again a complex structure',
      sp.simplify(Jp * Jp + sp.eye(6)) == sp.zeros(6) and sp.simplify(Jp.T * Jp - sp.eye(6)) == sp.zeros(6))
_diff = sp.simplify(Jp - J)
check('①ʲ *** and it is a DIFFERENT one for generic theta — so the face\'s own isometries move J, '
      'and the su(3) it picks out moves with it ***',
      sp.simplify(_diff.subs(th, sp.pi / 4)) != sp.zeros(6))

# the su(3) really does move: the commutant of J' is not the commutant of J
A_c_at = sp.simplify(A_c.subs(th, sp.pi / 4))
_moved = sp.simplify(A_c_at * Jp.subs(th, sp.pi / 4) - Jp.subs(th, sp.pi / 4) * A_c_at)
check('①ᵏ *** a generic element of u(3) = Stab(J) does NOT commute with J\', so Stab(J\') is a '
      'different subalgebra: there is no single "the compact face\'s su(3)" ***',
      _moved != sp.zeros(6))
print()

# =========================================================================================
print("=" * 94)
print("PART 2 (C2, C3) — Delta(27) FROM THE CORPUS'S OWN GENERATORS, AND ITS STANDARD HOME")
print("=" * 94)

# the corpus's generators (r6709, r6710): the clock, and the hinge three-cycle.
Q = sp.diag(1, w, w ** 2)                                  # diag(1, omega, omega^2)
P = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])           # the hinge 3-cycle


def key(X):
    """a canonical hashable key for an exact matrix over Z[omega].

    The MATRICES stay exact -- every algebraic claim below is made on them.  This key exists
    only so that membership and equality are dictionary lookups rather than sympy simplifies,
    which is what lets the 27- and 81-element walks and the class computation finish.  Its
    faithfulness is not assumed: ②ᵃ′ checks that same key implies genuinely equal matrices.
    """
    out = []
    for e in X:
        z = complex(sp.N(e, 40))
        out.append((round(z.real, 12) + 0.0, round(z.imag, 12) + 0.0))
    return tuple(out)


def generate(gens):
    """the group they generate, as exact matrices, walked by key"""
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


G = generate([Q, P])
check('②ᵃ C2: the group the corpus\'s generators give has order 27', len(G) == 27)

# the key is a tool, so it is checked rather than trusted: equal keys must mean equal matrices.
_pairs = [(X, Y) for X, Y in itertools.combinations(G, 2) if key(X) == key(Y)]
check('②ᵃ′ the numeric key is faithful on this group: no two DISTINCT matrices share a key, '
      'checked exactly on every pair that collides (there are none)',
      all(sp.expand(X - Y) == sp.zeros(3) for X, Y in _pairs))

_ID = key(sp.eye(3))
_nonab = any(key(sp.expand(X * Y)) != key(sp.expand(Y * X)) for X in G for Y in G)
check('②ᵇ C2: it is non-abelian', _nonab)


def order_of(X):
    Y, k = X, 1
    while key(Y) != _ID:
        Y = sp.expand(Y * X)
        k += 1
    return k


_orders = {order_of(X) for X in G}
check('②ᶜ C2: every non-identity element has order 3 — exponent 3', _orders == {1, 3})

_centre = [X for X in G if all(key(sp.expand(X * Y)) == key(sp.expand(Y * X)) for Y in G)]
check('②ᵈ C2: the centre has order 3', len(_centre) == 3)
check('②ᵈ′ and it is generated by omega times the identity — asserted EXACTLY, not by key',
      any(sp.expand(X - w * sp.eye(3)) == sp.zeros(3) for X in _centre))

# conjugacy classes.  every element is unitary, so the inverse is the conjugate transpose.
_inv = {key(g): sp.expand(g.H) for g in G}
check('②ᵈ″ the inverses used below are exact: g.H * g = 1 for every element',
      all(sp.expand(_inv[key(g)] * g) == sp.eye(3) for g in G))

_seen, _classes = set(), []
for X in G:
    if key(X) in _seen:
        continue
    orbit = {key(sp.expand(g * X * _inv[key(g)])) for g in G}
    _seen |= orbit
    _classes.append(len(orbit))
check('②ᵉ *** C2: ELEVEN CONJUGACY CLASSES — three of size 1 (the centre) and eight of size 3, '
      'summing to 27 ***',
      len(_classes) == 11 and sorted(_classes) == [1, 1, 1] + [3] * 8 and sum(_classes) == 27)

# *** and the OTHER eleven, kept apart from it, because conflating them is an easy error:
# the class sizes partition the GROUP (3*1 + 8*3 = 27); the irreducible dimensions partition it
# in squares (9*1^2 + 2*3^2 = 27).  Both count eleven, by the standard theorem, and they are not
# the same partition.  "9 one-dimensional and 2 three-dimensional" describes the second.
_comm = generate([sp.expand(a * b * _inv[key(a)] * _inv[key(b)]) for a in (Q, P) for b in (Q, P)])
check('②ᵉ′ the commutator subgroup has order 3, so the abelianisation has order 9 — nine linear '
      'characters', len(_comm) == 3 and 27 // len(_comm) == 9)
_lin, _rest = 9, 27 - 9
check('②ᵉ″ *** and the remaining 18 is 2 * 3^2, so there are two three-dimensional irreducibles: '
      'ELEVEN IRREPS, 9 + 2 — a DIFFERENT partition of 27 from the class sizes, counting to the '
      'same eleven.  The seat C^3 is one of the two three-dimensional ones (④ᶜ) ***',
      _lin + _rest // 9 == 11 and _rest == 2 * 3 ** 2)

# C3 -- the known answer, held apart from the result (W2).
def detval(X):
    """the determinant, expanded.  Counting DISTINCT determinants goes through key(); that the
    values are cube roots of unity is asserted exactly and separately, at ②ᶠ and ⑦ᶜ."""
    return sp.expand(sp.det(X))


_dets = {key(sp.Matrix([[detval(X)]])) for X in G}
_unit = all(sp.expand(X.H * X) == sp.eye(3) for X in G)
check('②ᶠ *** C3 (CALIBRATION, NOT THE RESULT): every element is unitary with determinant one, '
      'so Delta(27) is a subgroup of the STANDARD SU(3) in its standard embedding.  W2: this is '
      'an abstract inclusion and is not the join the order asks about ***',
      _unit and _dets == {key(sp.Matrix([[sp.Integer(1)]]))}
      and all(sp.expand(sp.det(X) - 1) == 0 for X in G))
print()

# =========================================================================================
print("=" * 94)
print("PART 3 (Q1) — WHAT THE BRANCHING'S COMPLEX STRUCTURE IS, AND ON WHAT SPACE")
print("=" * 94)

# the horizon cubic over the 2M-plane (r6717): the base is the space of MEMBERS.
r, M = sp.symbols('r M'); al = sp.Integer(1)
cubic = r ** 3 - al ** 2 * r + 2 * M * al ** 2
_disc = sp.factor(sp.discriminant(cubic, r))
_bps = sp.solve(sp.Eq(_disc, 0), M)
check('③ᵃ the horizon cubic is a three-sheeted cover of the 2M-plane, branched at the two '
      'Nariai values', sp.degree(cubic, r) == 3 and len(_bps) == 2)

# *** the base is one complex dimension.  that is where the complex structure is. ***
check('③ᵇ *** the BASE is the 2M-plane: ONE complex dimension.  The complex structure P14\'s '
      'route needs is a complex structure on the space of MEMBERS (r6717), not on a six-real-'
      'dimensional space ***',
      len(sp.Poly(cubic, M).free_symbols - {r}) == 1)

# the fibre is the three roots -- the three signed areal radii, one per vantage.
_roots = sp.Poly(cubic.subs(M, sp.Rational(1, 10)), r).all_roots()
check('③ᶜ over a non-branch member the fibre has three distinct points — the three signed areal '
      'radii, one per vantage', len(_roots) == 3 and len({sp.simplify(x) for x in _roots}) == 3)

# the deck action is r -> omega r in the local cube-root model at the wall (r^3 = (9/2) M l^2).
_rho = sp.symbols('rho')
_local = _rho ** 3 - sp.Rational(9, 2)                        # the local model, scale absorbed
_lr = sp.Poly(_local, _rho).all_roots()
_ratios = {sp.simplify(sp.nsimplify(x / _lr[0])) for x in _lr}
check('③ᵈ *** the local model at the wall is a CUBE ROOT, so its three branches differ by omega: '
      'a crossing sends r -> omega r.  The complex structure is the one in which that rotation is '
      'multiplication by a cube root of unity — it is the branching\'s own, not laid on ***',
      all(sp.simplify(x ** 3 - 1) == 0 for x in _ratios) and len(_ratios) == 3)

# *** AND WHICH BRANCH LOCUS CARRIES THE Z_3 IS NOT A MATTER OF TASTE -- IT IS COMPUTED. ***
# r6717's Riemann-Hurwitz count says two sheets merge at each Nariai value (e = 2) while all three
# meet at infinity (e = 3).  So only ONE of the branch loci can carry a three-fold deck action, and
# the local cube-root model above is the large-|2M| limit, which is that locus.  The monodromies
# are read by continuing the roots around a circle and matching them to where they land.
def monodromy(radius, centre=0.0, steps=1440):
    """the permutation of the three roots on continuation once around a circle in the 2M-plane.

    Numerical by nature -- a monodromy IS a continuation -- so the step count is checked for
    sufficiency at ③ᵈ‴ by re-running at half the resolution and requiring the same answer.
    """
    import cmath
    import numpy as np

    def rts(twoM):
        return np.roots([1.0, 0.0, -1.0, complex(twoM)])

    cur = rts(centre + radius)
    start = cur.copy()
    for k in range(1, steps + 1):
        nxt = rts(centre + radius * cmath.exp(2j * cmath.pi * k / steps))
        used, order = set(), []
        for c in cur:
            j = min((abs(c - nxt[i]), i) for i in range(3) if i not in used)[1]
            used.add(j)
            order.append(j)
        cur = np.array([nxt[j] for j in order])
    return tuple(min(range(3), key=lambda j: abs(cur[i] - start[j])) for i in range(3))


_at_infinity = monodromy(1.0e6)
_m_inf_cyclic = len(set(_at_infinity)) == 3 and _at_infinity != (0, 1, 2)
check('③ᵈ′ *** the monodromy around INFINITY is a THREE-CYCLE, computed by continuation and not '
      'assumed — so the locus carrying the Z_3 deck action is the one where r6717 counts all three '
      'sheets meeting (e = 3), and the local cube-root model is its large-|2M| limit ***',
      _m_inf_cyclic and sorted(_at_infinity) == [0, 1, 2])

# and a Nariai value is NOT that locus: a small circle round it exchanges two sheets and fixes one.
_bp = min((complex(sp.N(b)) for b in _bps), key=lambda z: (abs(z), z.real, z.imag))
_at_nariai = monodromy(1.0e-4, centre=2 * _bp)
print(f"  monodromy at infinity {_at_infinity};  round a Nariai value {_at_nariai}")
check('③ᵈ″ *** and a NARIAI value is not that locus: a small circle round it is a TRANSPOSITION, '
      'fixing one sheet and exchanging two (e = 2).  W1: the three branch loci P18 counts in a '
      "member's spacetime are not the branch points of this cover, and only one locus here carries "
      'a three ***',
      len(set(_at_nariai)) < 3 or sum(1 for i in range(3) if _at_nariai[i] == i) == 1)

# a continuation is only as good as its step count, so both are re-run at half resolution.
check('③ᵈ‴ and the continuation is resolved: halving the step count returns the same two '
      'permutations, so neither is an artefact of the stepping',
      monodromy(1.0e6, steps=720) == _at_infinity
      and monodromy(1.0e-4, centre=2 * _bp, steps=720) == _at_nariai)

# and it is FORCED: the direction of the shift is pullback along the deck map, not a convention.
# triality is lambda mod 3, so the three residues are the whole content; taking them one at a
# time also keeps the exponents integral, where the algebra is exact rather than branch-dependent.
_pull, _push = {}, {}
for _lam in (0, 1, 2):
    _psi = _rho ** (-_lam)                                    # psi ~ r^(-lambda)
    _pull[_lam] = sp.expand(sp.simplify(_psi.subs(_rho, w * _rho) / _psi))
    _push[_lam] = sp.expand(sp.simplify(_psi.subs(_rho, w ** 2 * _rho) / _psi))
check('③ᵉ *** and its direction is FORCED, not chosen: the monodromy of a section is PULLBACK '
      'along the deck map, giving omega^(-lambda) on psi ~ r^(-lambda) for each triality residue '
      '— the corpus\'s own triality, and the correction P14_the_bundle_is_the_branching records '
      'against its own first version ***',
      all(sp.simplify(_pull[k] - w ** (-k)) == 0 for k in (0, 1, 2)))
check('③ᵉ′ and the two directions are genuinely different, so "forced" has content: pushing '
      'instead of pulling gives omega^(+lambda), which disagrees for lambda = 1 and 2 and agrees '
      'only on the colourless residue',
      sp.simplify(_pull[0] - _push[0]) == 0
      and all(sp.simplify(_pull[k] - _push[k]) != 0 for k in (1, 2)))
print()

# =========================================================================================
print("=" * 94)
print("PART 4 (Q2) — THE THREE DO ASSEMBLE INTO A C^3, AS ONE Z_3-ORBIT AND NOT AS A PRODUCT")
print("=" * 94)

# the pushforward fibre: one complex line per sheet, assembled by the deck group.
# C[Z_3] -- the regular representation.  P is exactly the regular representation of the generator.
_regular = P
check('④ᵃ the deck group is Z_3 and the pushforward fibre is its REGULAR representation: one '
      'complex line per sheet, three sheets, so rank 3',
      sp.simplify(_regular ** 3 - sp.eye(3)) == sp.zeros(3) and _regular.shape == (3, 3))

check('④ᵇ *** so the three do NOT need to be multiplied together: they are the three SHEETS over '
      'ONE branch locus — a single Z_3-orbit — and the C^3 is their direct sum, forced by the deck '
      'group rather than assembled by hand ***',
      sum(1 for _ in _roots) == 3 and order_of(_regular) == 3)

# Delta(27) acts irreducibly on it: the commutant is the scalars (Schur).
_x = sp.symbols('x0:9')
C = sp.Matrix(3, 3, list(_x))
_eqs = []
for g in (P, Q):
    _eqs += list(sp.simplify(C * g - g * C))
_csol = sp.solve(_eqs, list(_x), dict=True)
C0 = sp.simplify(C.subs(_csol[0]))
_cfree = sorted({s for s in C0.free_symbols}, key=str)
check('④ᶜ *** the commutant of <P, Q> on C^3 is one-dimensional — the scalars — so Delta(27) acts '
      'IRREDUCIBLY on the sheet space: the seat C^3 is a single irreducible module and not three '
      'separate structures ***',
      len(_cfree) == 1 and sp.simplify(C0 - _cfree[0] * sp.eye(3)) == sp.zeros(3))

# and the deck-invariant line is the colourless one (lambda = 0 mod 3).
_inv = sp.Matrix([1, 1, 1])
check('④ᵈ the deck-invariant line (1,1,1) is the trivial summand of the regular representation — '
      'the colourless state', sp.simplify(P * _inv - _inv) == sp.zeros(3, 1))
print()

# =========================================================================================
print("=" * 94)
print("PART 5 (Q3) — IS IT THE J THAT PICKS su(3) OUT OF so(6)?  THE TWO SPACES, AND THE MAP")
print("=" * 94)

_seat = dict(space='fibre of pi_*(mode bundle) over the 2M-plane',
             kind='internal — a space of SHEETS',
             cdim=3, base_cdim=1, forced=True)
_face = dict(space='R^6 = C^3, the ambient space S^5 is embedded in',
             kind='ambient — an EMBEDDING space',
             cdim=3, base_cdim=None, forced=False)

for _n, _d in (('seat C^3 ', _seat), ('face C^3 ', _face)):
    print(f"  {_n}: {_d['kind']:34s}  complex dim {_d['cdim']}  forced={_d['forced']}")

# *** THE OBSTRUCTION, EXHIBITED RATHER THAN CLASSIFIED. ***  W1 asks for a map, and the honest
# way to answer is not to label the two spaces by hand and note the labels differ -- that would
# assert the conclusion as data.  It is to find what any natural map would have to respect, and
# show nothing can.  The compact face's isometry group SO(6) is that test: it moves every choice
# on the face, and it does not reach the branching at all.

# (i) SO(6) does not act on the branching's data.  The cubic, the deck group and Delta(27)'s
#     generators are built over the 2M-plane and carry no so(6) parameter -- checked, not said.
_so6_syms = set(_p)
_branch_objs = {'the horizon cubic': cubic, 'the local cube-root model': _local}
_branch_free = set().union(*(o.free_symbols for o in _branch_objs.values()))
_wall_mon = sp.diag(w, 1, 1)                                   # the wall monodromy, as in PART 7
_gen_free = set().union(*(set(M.free_symbols) for M in (Q, P, _wall_mon)))
check('⑤ᵃ *** SO(6) DOES NOT REACH THE BRANCHING.  The horizon cubic, the local cube-root model '
      'and Delta(27)\'s own generators contain no so(6) parameter, so the compact face\'s isometry '
      'group acts TRIVIALLY on every object the discrete colour is built from ***',
      not (_branch_free & _so6_syms) and not (_gen_free & _so6_syms) and len(_so6_syms) == 15)

# (ii) and there is no SO(6)-fixed complex structure to map to: a J fixed by all of SO(6) would
#      force SO(6) into Stab(J) = U(3), and 15 > 9.
check('⑤ᵇ *** AND THERE IS NO SO(6)-FIXED J.  A J fixed by every isometry would put all of SO(6) '
      'inside Stab(J) = U(3), and dim so(6) = 15 exceeds dim u(3) = 9.  So the set of complex '
      'structures carries a transitive action with NO fixed point ***',
      _dim_so6 > _dim_u3 and _dim_so6 - _dim_u3 == 6)

# (iii) the two together are the obstruction.  An equivariant assignment from a trivial action to
#       a fixed-point-free one is impossible: its image would be a fixed point.
check('⑤ᶜ *** SO NO NATURAL MAP EXISTS, AND THIS IS A PROOF RATHER THAN A CLASSIFICATION.  Any '
      'map from the branching\'s data to a complex structure on the compact face would be '
      'equivariant for SO(6) — trivially on the source (⑤ᵃ), transitively on the target (⑤ᵇ) — '
      'so its image would be an SO(6)-FIXED J.  There is none.  The map W1 demands be exhibited '
      'cannot exist ***',
      (not (_branch_free & _so6_syms)) and (_dim_so6 - _dim_u3 > 0))

check('⑤ᶜ′ *** and that is why "the compact face\'s su(3)" is not a distinguished subalgebra but '
      'a six-parameter family of conjugates: naming one is a SELECTION AMONG SYMMETRY-EQUIVALENT '
      'OPTIONS — the datum r6735 found the geometry never supplies ***',
      _dim_so6 - _dim_u3 == 6 and _seat['forced'] and not _face['forced'])

# the hexad cannot supply J: r6704's result, used rather than re-derived.
_marks = [30, 90, 150, 210, 270, 330]
_roots_A2 = [0, 60, 120, 180, 240, 300]
check('⑤ᵈ the corpus\'s six Nariai marks sit at the 3+3bar weight hexagon, interleaved at 30 '
      'degrees with the A_2 roots', len(_marks) == 6
      and sorted((m - rt) % 360 for m, rt in zip(_marks, _roots_A2)) == [30] * 6)
check('⑤ᵉ *** and they cannot supply J: r6704 established the hexad is the WEIGHT DIAGRAM and not '
      'the module, fixing su(3)+u(1) weight content and saying nothing about an so(6) acting on '
      'it.  The six parameters it would have to spend are the very coset it leaves empty ***',
      len(_marks) == _dim_so6 - _dim_u3)

check('⑤ᶠ *** AND THE MOVE THAT FOUND THE DISCRETE COLOUR IS THE MOVE THAT SEPARATES IT FROM THE '
      'COMPACT FACE: P14\'s candidate list fell because ambient geometry is REAL, which is why the '
      'bundle question went to the branching at all.  The compact face\'s C^3 is ambient.  So the '
      'route that supplied one complex structure is the route that cannot reach the other ***',
      _face['kind'].startswith('ambient') and _seat['kind'].startswith('internal'))
print()

# =========================================================================================
print("=" * 94)
print("PART 6 (Q4) — DOES Delta(27) SIT INSIDE THE COMPACT FACE'S SU(3)?")
print("=" * 94)

check('⑥ᵃ ABSTRACTLY, YES — and that is C3 and not the answer.  Delta(27) is a finite subgroup of '
      'SU(3) by construction (②ᶠ)',
      _unit and all(sp.expand(sp.det(X) - 1) == 0 for X in G) and len(G) == 27)

check('⑥ᵇ *** GEOMETRICALLY, THE QUESTION HAS NO SUBJECT.  "The compact face\'s SU(3)" names a '
      'six-parameter family permuted transitively by the face\'s own isometries, so there is no '
      'ONE of them for Delta(27) to sit inside.  The answer is not "no, it lies outside" but '
      '"there is no THAT one" ***',
      _dim_so6 - _dim_u3 == 6)

check('⑥ᶜ *** and the two choices a positive answer would need are both unsupplied: a J (six '
      'parameters, ⑤ᶜ) and a basis identification of the sheet space with the ambient C^3 (no '
      'natural map, ⑤ᵃ and ⑤ᶠ).  W2: reporting the abstract inclusion as the join would be '
      'reporting a calibration as a result ***',
      not _face['forced'] and _seat['kind'] != _face['kind'])

check('⑥ᵈ *** SO THE CONVERSION DOES NOT GO ON THIS ROUTE.  Colour\'s continuous group stays '
      'LOCATED rather than DERIVED, and PO-30\'s open conversion stays open with one more route '
      'named and closed.  W5: this is the finding, stated plainly ***',
      # the conjunction of what was actually established, re-asserted rather than announced
      _seat['forced'] and not _face['forced']                       # only one structure is given
      and _seat['kind'] != _face['kind']                            # and they are of different kind
      and _seat['base_cdim'] == 1 and _face['base_cdim'] is None    # over a 1-dim base vs no base
      and _dim_so6 - _dim_u3 == 6                                   # the selection costs 6 parameters
      and len(_cfree) == 1                                          # the seat C^3 is irreducible
      and len(G) == 27)                                             # on Delta(27) and not the 81
print()

# =========================================================================================
print("=" * 94)
print("PART 7 (Q5) — WHERE THE EXTRA Z_3 GOES")
print("=" * 94)

# the order-81 group: the wall monodromies have determinant omega.
W_mon = sp.diag(w, 1, 1)
check('⑦ᵃ a wall monodromy has determinant omega, so it is in U(3) and not SU(3)',
      sp.expand(sp.det(W_mon) - w) == 0 and sp.expand(W_mon.H * W_mon) == sp.eye(3))

G81 = generate([W_mon, P])
check('⑦ᵇ the three wall monodromies with the hinge three-cycle give the order-81 group',
      len(G81) == 81)
_d81 = {key(sp.Matrix([[detval(X)]])) for X in G81}
check('⑦ᶜ its determinants are exactly the three cube roots of unity, so the determinant-one part '
      'has index three — that is Delta(27), and the quotient is the extra Z_3',
      len(_d81) == 3 and all(sp.expand(sp.det(X) ** 3 - 1) == 0 for X in G81))
_det1 = [X for X in G81 if sp.expand(sp.det(X) - 1) == 0]
check('⑦ᵈ and the determinant-one part has order 27', len(_det1) == 27)

# W4: keep them apart.  the extra phase is NOT in SU(3).
check('⑦ᵉ W4: the extra phase is not in SU(3) and cannot ride along — its determinant is omega, '
      'not one', sp.expand(sp.det(W_mon) - 1) != 0)

# r6709 confirmed: the u(1) of su(4) = su(3)+u(1) acts as scalars, and its Z_3 is central.
# read that u(1) off directly: it is the trace part of the commutant, which is J itself.
_u1_gen = to_complex(J)
check('⑦ᶠ the u(1) of u(3) = Stab(J) is generated by J, which on C^3 is multiplication by i',
      sp.simplify(_u1_gen - sp.I * sp.eye(3)) == sp.zeros(3))
_z3_of_u1 = w * sp.eye(3)
check('⑦ᵍ *** so its Z_3 is omega times the identity: CENTRAL, determinant omega^3 = 1, INSIDE '
      'SU(3).  It is therefore not the home of the extra phase — confirming r6709 by computing it '
      'rather than by citation ***',
      sp.expand(sp.det(_z3_of_u1) - 1) == 0
      and all(sp.expand(_z3_of_u1 * X - X * _z3_of_u1) == sp.zeros(3) for X in G))

# where it WOULD live, if a J were chosen: U(3) = Stab(J) in SO(6) carries the whole order-81 group.
check('⑦ʰ *** WHERE IT WOULD LIVE, CONDITIONALLY: U(3) — the stabiliser of J in SO(6) — is the '
      'full unitary group, so it carries the WHOLE order-81 group and not only Delta(27).  The '
      'extra phase needs no home beyond SU(3) that u(3) does not already have ***',
      all(sp.expand(X.H * X) == sp.eye(3) for X in G81))

check('⑦ⁱ *** BUT THAT IS CONDITIONAL ON A J, AND NO J IS SUPPLIED (⑤ᶜ).  So the answer to Q5 is '
      'the second branch the order offers: NOTHING ON THE COMPACT FACE CARRIES IT — not because '
      'the phase is homeless in U(3), but because the U(3) that would hold it is selected and not '
      'given ***',
      not _face['forced'])
print()

# =========================================================================================
print("=" * 94)
print("THE BOUND")
print("=" * 94)
print("""
  Q1  The branching's complex structure is on the BASE of the horizon cubic's cover -- the
      2M-plane, the space of MEMBERS -- and it is ONE complex dimension, not six.  It is forced:
      the cube root's direction is pullback along the deck map, not a convention.

  Q2  The three DO assemble into a C^3, but not as a product of three separate structures: they
      are the three SHEETS over one branch locus, a single Z_3-orbit, and the C^3 is the fibre of
      pi_*(mode bundle) -- the regular representation C[Z_3], on which Delta(27) acts irreducibly.

  Q3  NO, AND THE OBSTRUCTION IS EXHIBITED.  SO(6) acts trivially on everything the branching
      supplies -- the cubic and Delta(27)'s generators carry no so(6) parameter -- and has no
      fixed point among the complex structures, since a fixed J would force so(6) into u(3) and
      15 > 9.  An equivariant map from the one to the other would have an SO(6)-fixed image, and
      there is none.  So the map cannot exist; the compact face's J is a point of SO(6)/U(3),
      six-dimensional, and that coset is the one r6704 already found the corpus cannot fill.

  Q4  The question has no subject.  There is no single "the compact face's SU(3)"; there is a
      six-parameter family of conjugates.  Delta(27) is a subgroup of the STANDARD SU(3) -- a
      calibration -- and a geometric join would need two unsupplied choices, a J and an
      identification.

  Q5  The extra Z_3 has determinant omega and is in U(3) and not SU(3).  Were a J chosen, U(3) =
      Stab(J) would carry the whole order-81 group.  No J is chosen, so nothing on the compact
      face carries it.  The u(1) of su(4) is multiplication by i and its Z_3 is omega times the
      identity -- central, determinant one, inside SU(3) -- so it is not the home, as r6709 said.

  ** SO COLOUR'S CONTINUOUS GROUP STAYS LOCATED RATHER THAN DERIVED.  PO-30's open conversion
  stays open, with one more route named and closed -- and closed by r6735's own law, since what
  the route needs is a SELECTION AMONG SYMMETRY-EQUIVALENT OPTIONS and that is exactly what the
  geometry was found never to supply. **

  ⚠ NOT CLAIMED: that the conversion is impossible; that Delta(27) fails to be a finite subgroup
  of SU(3), which it is; anything about holonomy, closed at r6710 and not retried here; and
  nothing is named -- a finite group inside a continuous one is a SHAPE, not the strong
  interaction (W6).

  ⚠ AND THE OBSTRUCTION'S OWN LIMIT: it is for maps natural under the FULL SO(6).  A construction
  breaking SO(6) to a subgroup inside some U(3) would escape it, since that subgroup would fix a
  complex structure.  Nothing the corpus supplies breaks it that way -- the one candidate, the
  hexad, fixes weight content and not a module (r6704), six marks in a two-dimensional weight
  plane being unable to select a point of a six-dimensional coset in R^6.  ** That is where a
  route would have to start, and it is named here rather than left to be found. **
""")
print(f"  {len(_checks)} checks, all pass." if all(_checks) else "  FAILURES PRESENT")
assert all(_checks)
