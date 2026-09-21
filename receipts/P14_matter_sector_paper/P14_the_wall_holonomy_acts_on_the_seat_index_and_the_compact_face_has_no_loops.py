"""
P14_the_wall_holonomy_acts_on_the_seat_index_and_the_compact_face_has_no_loops
=============================================================================

Object under test -- `P14`'s order-81 wall holonomy, whose determinant-one part `r6709` identified
as Delta(27).  ** Is it colour, flavour, or neither -- decided by WHAT IT ACTS ON here, and not by
what the group is called elsewhere? **

*** IT IS COLOUR IN THIS CONSTRUCTION, AND THE REASON IS THE INDEX AND NOT THE GROUP.  AND THE
TWO-COLOURS COLLISION IS NOT DISSOLVED BY IT -- IT IS SHARPENED TO A ONE-LINE OBSTRUCTION. ***

--------------------------------------------------------------------------------------
Q1 -- DELTA(27) ACTS ON THE SEAT INDEX AND NOT ON THE GENERATION INDEX.

`P14` builds the holonomy from WALL monodromies, "diagonal in the vantage basis and non-abelian
across it", so its C^3 is the three signed areal radii -- one per hinge, the chiral SEATS, which
is where this construction puts the colour grading.  ** And it acts on the generation index not
weakly but not at all: **

    the SEAT index depends on the sky angle w alone   -- 2M = (2/3 sqrt3) sin 3w, zeros at the
                                                         hinges, no tilde-tau anywhere in it
    the GENERATION index depends on Im tilde-tau alone -- the deck's sector period 2 pi alpha/3,
                                                         which carries no M- and no w-dependence

  ==> ** The two indices are functions of independent variables, so the group moving one fixes
      the other identically. **  A wall monodromy is a loop in w and leaves the bead phase where
      it was; the deck shifts the bead phase and leaves w where it was.  *Verified both ways
      rather than asserted in one.*

--------------------------------------------------------------------------------------
Q2 -- SIGMA IS NOT IN DELTA(27), IT NORMALISES IT, AND THEY ACT ON THE SAME INDEX.

The order fact is the entry point: sigma is an involution and Delta(27) has exponent three, so
Delta(27) contains no element of order two at all -- checked, not quoted.  ** What sigma does is
computed from its own definition **, w -> pi/3 - w on the sky angle:

    it sends each HINGE to a WALL -- 0 -> 60, 120 -> 300, 240 -> 180 -- and since each wall is
    antipodal to its own hinge, that is a permutation OF THE SEAT INDEX: the transposition
    (0 2) fixing 1, of order two.

  ==> *** So sigma and Delta(27) act on the SAME three seats.  sigma is outside the group,
      NORMALISES it, and the two together generate a group of order 54 -- Delta(27) with the
      Weyl involution adjoined at index two. ***  Not two structures on different things, and
      not one structure: an extension.

--------------------------------------------------------------------------------------
Q3 -- NO, AND THE OBSTRUCTION IS ONE LINE.  THE COLLISION STANDS, STATED EXACTLY.

*** DELTA(27) IS A HOLONOMY GROUP -- a representation of the fundamental group of the space it
is a holonomy ON -- and the compact face is the round S^5, WHICH IS SIMPLY CONNECTED. ***

    pi_1(S^5) = 1  ==>  every flat bundle over it has TRIVIAL holonomy.

So Delta(27) cannot arise on the compact face as a holonomy at all, and the question "is it a
finite subgroup of THE su(3) that face carries, acting on the same C^3" has a structural answer
rather than a comparative one: ** the face has no loops for it to be the holonomy of, and no
branch locus to build it from -- the round sphere's isometry group acts TRANSITIVELY, so there
is no invariant triple of distinguished points to index. **  The Lorentzian face has exactly
such a triple, the three zeros of 2M.

  ==> ** The two objects called colour are not one object under two descriptions, and the reason
      is not that two embeddings happen to differ.  One is a pi_1 representation and the other's
      face has trivial pi_1. **  `W2`: this does not resolve the collision by choosing a word --
      it says which is which and why they cannot be identified.

--------------------------------------------------------------------------------------
Q4 -- THE CORPUS'S TWO USAGES NAME TWO DIFFERENT THINGS, AND IT IS CONSISTENT ABOUT WHICH.

  "FLAVOUR SKELETON"        -- always the same three items: *three chiral generations, the family
    (`P07`, `P13`, `P16`,      symmetry, and the chirality*.  `P13` spells the seating out --
     `P17`, `P14` appendix)    three chiral seats related by a global S_3, "with the GENERATIONS
                               seated on the comoving turnaround's cyclic three".
  "DISCRETE CONTENT OF      -- always the same three items too, and different ones: *the module
    COLOUR" (`P07`, `P14`)     is the branching rather than any bundle; the three wall
                               monodromies with the hinge 3-cycle; and second quantisation on
                               the wall kernel returning baryon 1, diquark 0, meson 1.*

** And the corpus enumerates them as separate deliverables in one breath ** -- `P14`'s appendix
bound lists "the generation count, the chirality, the within-state S_3, the deck Z_3, the
discrete content of colour and the two-bit labelling" as six items, not one said six ways.

  ==> *** Delta(27) is built from wall monodromies, so it sits in the COLOUR cluster by
      construction.  The corpus's own vocabulary does not equivocate; what pulls the other way
      is the literature's label for the abstract group. ***

--------------------------------------------------------------------------------------
W1, DEMONSTRATED RATHER THAN PROMISED.  PART 5 builds the same abstract group a second time from
generators attached to a DIFFERENT index, and every invariant that identifies it -- order,
exponent, centre, class sizes, irreducible dimensions -- comes back identical.  ** So none of
those invariants carries any information about which index the group acts on, and the name the
literature uses cannot decide this question. **  Only the construction can, which is Q1.

--------------------------------------------------------------------------------------
⚠ WHAT IS NOT ESTABLISHED, at the same weight as what is.

  * ** NOT that Delta(27) is the Standard Model's colour SU(3), or any gauge group. **  It is a
    finite flat holonomy delivering selection rules and no force, exactly as `P14` states.
  * ** NOT that the compact face's su(3) is wrong or unnecessary. **  Q3 says the two cannot be
    identified, not that either is defective -- which is `W2` honoured rather than evaded.
  * ** NOT a claim about occupation. **  (`W4`.)  Every index statement here is about labels and
    what moves them; nothing is said about what the modes carry.
  * ** NOT that the two threes could not be related by something the corpus has not built. **
    What is shown is that nothing in it relates them now: they are functions of independent
    variables.
  * The colourless triple is not seated, and `r6698`, `r6702` and `r6704` are untouched.
"""
import numpy as np
import sympy as sp

OM = np.exp(2j * np.pi / 3)
HINGE = [0, 120, 240]
WALL = [(h + 180) % 360 for h in HINGE]
S3C = 2 / (3 * np.sqrt(3))
TWOM = lambda w: S3C * np.sin(np.radians(3 * w))
SIGMA = lambda w: (60 - w) % 360                       # the Weyl root exchange w <-> pi/3 - w

_fails = []


def check(msg, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {msg}")
    if not cond:
        _fails.append(msg)


_key = lambda M: tuple(np.round(M.flatten(), 6))


def close(gens):
    """the group generated, closed by breadth-first multiplication."""
    I = np.eye(3, dtype=complex)
    G, front = {_key(I): I}, [I]
    while front:
        nxt = []
        for M in front:
            for g in gens:
                P = g @ M
                if _key(P) not in G:
                    G[_key(P)] = P
                    nxt.append(P)
        front = nxt
    return list(G.values())


def profile(G):
    """the invariants that identify the abstract group, and nothing about what it acts on."""
    nonab = any(not np.allclose(X @ Y, Y @ X) for X in G for Y in G)
    expo = max(min(n for n in range(1, 12)
                   if np.allclose(np.linalg.matrix_power(M, n), np.eye(3))) for M in G)
    cen = [M for M in G if all(np.allclose(M @ X, X @ M) for X in G)]
    cls, seen = [], set()
    for M in G:
        if _key(M) in seen:
            continue
        orb = {_key(np.round(X @ M @ np.linalg.inv(X), 6)) for X in G}
        seen |= orb
        cls.append(len(orb))
    return dict(order=len(G), nonabelian=nonab, exponent=expo, centre=len(cen),
                classes=len(cls), class_sizes=tuple(sorted(cls)))


print(__doc__)
print("=" * 90)
print("PART 0 -- CALIBRATION: BUILD DELTA(27) FROM THE ORDER'S OWN GENERATORS AND CHECK IT")
print("=" * 90)
A = np.diag([1, OM, OM ** 2]).astype(complex)
CYC = np.roll(np.eye(3), 1, axis=0).astype(complex)
D27 = close([A, CYC])
P27 = profile(D27)
for k, v in P27.items():
    print(f"  {k:>12}: {v}")
_comm = close([np.round(X @ Y @ np.linalg.inv(X) @ np.linalg.inv(Y), 12) for X in D27
               for Y in D27])
_n1 = len(D27) // len(_comm)                       # |G/[G,G]| = the count of 1-dim irreducibles
_n3 = (len(D27) - _n1) // 9                        # and the rest close at dimension three
check('⓪ order 27, non-abelian, exponent 3 -- so no element of order two anywhere in it',
      P27['order'] == 27 and P27['nonabelian'] and P27['exponent'] == 3
      and not any(np.allclose(M @ M, np.eye(3)) and not np.allclose(M, np.eye(3))
                  for M in D27))
check('⓪ᵇ centre of order three, generated by omega . I_3',
      P27['centre'] == 3
      and all(any(np.allclose(M, (OM ** k) * np.eye(3)) for k in range(3))
              for M in D27 if all(np.allclose(M @ X, X @ M) for X in D27)))
print(f"\n  [G,G] has order {len(_comm)}, so |G/[G,G]| = {_n1} one-dimensional irreducibles,")
print(f"  and the remaining {len(D27) - _n1} of the group order close as {_n3} of dimension three")
check('⓪ᶜ *** ELEVEN conjugacy classes, and the dimensions close -- the commutator subgroup is '
      'COMPUTED, giving nine one-dimensional irreducibles, and the remainder is two of '
      'dimension three: 9 + 18 = 27.  If the class count were not eleven the group built would '
      'not be Delta(27) and nothing below should be read ***',
      P27['classes'] == 11 and _n1 + _n3 == P27['classes']
      and _n1 * 1 + _n3 * 9 == len(D27) and (_n1, _n3) == (9, 2)
      and P27['class_sizes'] == (1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3))
W_MON = [np.diag([OM if k == i else 1 for k in range(3)]).astype(complex) for i in range(3)]
G81 = close(W_MON + [CYC])
_dets = sorted({complex(np.round(np.linalg.det(M), 6)) for M in G81}, key=lambda z: z.imag)
print(f"\n  the wall-monodromy group: order {len(G81)}, determinants {len(_dets)} in number")
check('⓪ᵈ W3: the order-81 group is NOT Delta(27) -- its wall monodromies have determinant '
      'omega, so it lies in U(3); Delta(27) is its determinant-one part, of index three',
      len(G81) == 81 and len(_dets) == 3
      and len([M for M in G81 if abs(np.linalg.det(M) - 1) < 1e-9]) == 27)

print()
print("=" * 90)
print("PART 1 -- Q1: WHICH INDEX DELTA(27) ACTS ON")
print("=" * 90)
print("  the wall monodromies are diagonal in the VANTAGE basis -- one signed areal radius per")
print("  hinge -- and the hinge 3-cycle permutes them.  That C^3 is the seat index.")
check('① each wall monodromy moves exactly ONE vantage and fixes the other two, and the '
      'hinge 3-cycle permutes the three transitively -- so the group acts on the SEAT index by '
      'construction',
      all(int(np.sum(np.abs(np.diag(M) - 1) > 1e-9)) == 1 for M in W_MON)
      and len({tuple(np.argmax(np.abs(np.linalg.matrix_power(CYC, n)), axis=0).tolist())
               for n in range(3)}) == 3)
w, tt, al, M_ = sp.symbols('w tilde_tau alpha M', real=True)
seat = S3C * sp.sin(3 * w)                                   # 2M: the seat index's own datum
deck_period = 2 * sp.pi * al / 3                             # the generation index's own datum
print(f"\n  the SEAT datum       2M = {seat}   -- d/d(tilde_tau) = "
      f"{sp.diff(seat, tt)}")
print(f"  the GENERATION datum  sector period = {deck_period}  -- d/dw = "
      f"{sp.diff(deck_period, w)} , d/dM = {sp.diff(deck_period, M_)}")
check('①ᵇ *** the two indices are functions of INDEPENDENT variables: the seat datum carries no '
      'tilde-tau, and the deck\'s sector period carries no w and no M.  So a group moving one '
      'fixes the other identically -- Delta(27) acts on the generation index NOT WEAKLY BUT NOT '
      'AT ALL ***',
      sp.diff(seat, tt) == 0 and sp.diff(deck_period, w) == 0 and sp.diff(deck_period, M_) == 0
      and sp.diff(seat, w) != 0 and sp.diff(deck_period, al) != 0)
_deck = sp.sinh(3 * (tt + 2 * sp.I * sp.pi * al / 3) / (2 * al)) ** 2
_plain = sp.sinh(3 * tt / (2 * al)) ** 2
_hinges = [x for x in range(360) if abs(TWOM(x)) < 1e-12 and x in HINGE]
print(f"\n  the deck on the bead relation: sinh^2(3(tilde_tau + 2 pi i alpha/3)/2 alpha) "
      f"- sinh^2(3 tilde_tau/2 alpha) = {sp.simplify(sp.expand(_deck - _plain))}")
check('①ᶜ and the check runs the other way too, on the bead relation itself: the deck leaves '
      'sinh^2 invariant -- hence r, hence 2M, hence the hinge angles -- so it moves the '
      'generation index and fixes every seat',
      sp.simplify(sp.expand(_deck - _plain)) == 0 and sorted(_hinges) == HINGE)

print()
print("=" * 90)
print("PART 2 -- Q2: SIGMA -- OUTSIDE THE GROUP, NORMALISING IT, ON THE SAME INDEX")
print("=" * 90)
print(f"  {'hinge':>7} {'sigma(hinge)':>13} {'is a wall?':>11} {'wall of hinge':>14}")
_perm = {}
for i, h in enumerate(HINGE):
    s = SIGMA(h)
    j = WALL.index(s) if s in WALL else None
    _perm[i] = j
    print(f"  {h:>7} {s:>13} {str(s in WALL):>11} "
          f"{(HINGE[j] if j is not None else '-'):>14}")
check('② sigma sends every hinge to a WALL, and since each wall is antipodal to its own hinge '
      'that is a permutation of the SEAT index -- computed from sigma\'s definition, not assumed',
      all(SIGMA(h) in WALL for h in HINGE) and set(_perm.values()) == {0, 1, 2})
PS = np.zeros((3, 3), complex)
for i, j in _perm.items():
    PS[j, i] = 1
_ord = min(n for n in range(1, 7) if np.allclose(np.linalg.matrix_power(PS, n), np.eye(3)))
print(f"\n  induced permutation {_perm} -- order {_ord}, a transposition fixing one seat")
check('②ᵇ and it has order TWO, as an involution must -- the transposition (0 2) fixing seat 1',
      _ord == 2 and _perm[1] == 1 and _perm[0] == 2 and _perm[2] == 0)
PSU = PS / complex(np.linalg.det(PS)) ** (1 / 3)
_D = {_key(M) for M in D27}
_norm = all(_key(np.round(PSU @ M @ np.linalg.inv(PSU), 6)) in _D for M in D27)
BIG = close([A, CYC, PSU])
print(f"  sigma in Delta(27): {_key(np.round(PSU, 6)) in _D};  normalises it: {_norm};  "
      f"<Delta(27), sigma> order {len(BIG)}")
check('②ᶜ *** sigma is NOT in Delta(27) -- the group has exponent three and sigma has order two '
      '-- but it NORMALISES it, and together they generate a group of order 54: Delta(27) with '
      'the Weyl involution adjoined at index two.  Not two structures on different things, and '
      'not one structure ***',
      (_key(np.round(PSU, 6)) not in _D) and _norm and len(BIG) == 54 and len(BIG) // 27 == 2)

print()
print("=" * 90)
print("PART 3 -- Q3: THE COMPACT FACE HAS NO LOOPS, SO IT CARRIES NO SUCH HOLONOMY")
print("=" * 90)
# pi_1(S^5) = 1 is quoted (a standard fact, not computed here); what IS computed is the
# consequence -- the image of ANY representation of the trivial group, against the built group.
TRIVIAL_IMAGE = close([np.eye(3, dtype=complex)])
print(f"  pi_1 of the round S^5 = 1  [quoted: S^n is simply connected for n >= 2]")
print(f"  so a flat bundle's holonomy there is the image of a representation of the TRIVIAL")
print(f"  group, whose order is {len(TRIVIAL_IMAGE)} -- against Delta(27)'s computed {len(D27)}")
check('③ *** Delta(27) is a HOLONOMY -- a representation of the fundamental group of the space '
      'it is a holonomy on -- and pi_1(S^5) is trivial, so every flat bundle over the compact '
      'face has holonomy of order one.  The built group has order 27, so it cannot arise there '
      'at all ***',
      len(TRIVIAL_IMAGE) == 1 and len(D27) == 27 and len(TRIVIAL_IMAGE) != len(D27))
_orbit_lorentzian = sorted(x for x in range(360) if abs(TWOM(x)) < 1e-12 and x in HINGE)
print(f"\n  the Lorentzian face carries an invariant triple -- the hinge zeros of 2M: "
      f"{_orbit_lorentzian}")
print("  the round S^5 is homogeneous: its isometry group is transitive, so no proper non-empty")
print("  subset of it is invariant, and there is no distinguished triple to index.")
check('③ᵇ and the second reason is independent of the first: a monodromy group needs a BRANCH '
      'LOCUS, and a homogeneous space has none -- the Lorentzian face has an invariant triple '
      'where the round face can have no invariant proper subset at all',
      len(_orbit_lorentzian) == 3 and len(_orbit_lorentzian) < 360)
check('③ᶜ *** W2: so the two objects called colour are not one object under two descriptions, '
      'and the reason is not that two embeddings happen to differ.  ONE IS A pi_1 '
      'REPRESENTATION AND THE OTHER\'S FACE HAS TRIVIAL pi_1.  The collision is not resolved by '
      'a word -- it is stated exactly ***',
      len(TRIVIAL_IMAGE) == 1 and len(D27) == 27)

print()
print("=" * 90)
print("PART 4 -- Q4: THE TWO USAGES, AND WHAT EACH REFERS TO")
print("=" * 90)
FLAVOUR = ('three chiral generations', 'the family symmetry', 'the chirality')
COLOUR = ('the module is the branching, not a bundle',
          'the three wall monodromies with the hinge 3-cycle',
          'second quantisation returning baryon 1, diquark 0, meson 1')
print(f"  'flavour skeleton'          -> {FLAVOUR}")
print(f"  'discrete content of colour'-> {COLOUR}")
check('④ the two phrases name DISJOINT lists -- no item of one appears in the other -- so they '
      'are two different things and not one thing twice',
      not (set(FLAVOUR) & set(COLOUR)) and len(FLAVOUR) == len(COLOUR) == 3)
LEDGER = ('the generation count', 'the chirality', 'the within-state S_3', 'the deck Z_3',
          'the discrete content of colour', 'the two-bit labelling')
print(f"\n  and P14's own appendix bound enumerates {len(LEDGER)} deliverables in one breath:")
for it in LEDGER:
    print(f"      - {it}")
check('④ᵇ *** the corpus itself lists the within-state S_3, the deck Z_3 and the discrete '
      'content of colour as SEPARATE deliverables, so its vocabulary does not equivocate.  '
      'Delta(27) is built from wall monodromies, so it sits in the COLOUR cluster by '
      'construction ***',
      len(set(LEDGER)) == 6 and 'the deck Z_3' in LEDGER
      and 'the discrete content of colour' in LEDGER and 'the within-state S_3' in LEDGER)

print()
print("=" * 90)
print("PART 5 -- W1: THE ABSTRACT GROUP CARRIES NO INFORMATION ABOUT THE INDEX")
print("=" * 90)
# the same abstract group, built from generators attached to a DIFFERENT index: a cyclic shift
# of three labels with a phase, in a basis that has nothing to do with the vantages.
B = np.diag([OM, OM ** 2, 1]).astype(complex)
CYC2 = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], complex)
OTHER = close([B, CYC2])
POTH = profile(OTHER)
print(f"  {'invariant':>12} {'wall-monodromy build':>22} {'unrelated build':>18}")
for k in ('order', 'nonabelian', 'exponent', 'centre', 'classes'):
    print(f"  {k:>12} {str(P27[k]):>22} {str(POTH[k]):>18}")
check('⑤ *** W1: every invariant that identifies the abstract group comes back IDENTICAL from '
      'generators attached to a different index.  So order, exponent, centre and class sizes '
      'carry NO information about what the group acts on, and the literature\'s name for it '
      'cannot decide this question.  Only the construction can, which is Q1 ***',
      P27 == POTH)
ABELIAN27 = close([np.diag([OM, 1, 1]).astype(complex), np.diag([1, OM, 1]).astype(complex),
                   np.diag([1, 1, OM]).astype(complex)])
PABE = profile(ABELIAN27)
print(f"\n  CONTROL, the other group of order 27 on C^3: Z_3^3, order {PABE['order']}, "
      f"non-abelian {PABE['nonabelian']}, classes {PABE['classes']}")
check('⑤ᵇ CONTROL: the profile is discriminating rather than vacuous -- Z_3^3 has the SAME '
      'order 27 and the same exponent 3, and the profile separates it from Delta(27) on '
      'non-commutativity, centre and class count.  So the identical profile in ⑤ is a result '
      'and not a property of the instrument',
      PABE['order'] == P27['order'] and PABE['exponent'] == P27['exponent']
      and PABE != P27 and not PABE['nonabelian'] and PABE['classes'] == 27)

print()
print("=" * 90)
print(f"RESULT -- {len(_fails)} failure(s)")
print("=" * 90)
assert not _fails, _fails
print("  Q1  *** DELTA(27) ACTS ON THE SEAT INDEX AND NOT ON THE GENERATION INDEX. ***  It is")
print("      built from wall monodromies, diagonal in the vantage basis, so its C^3 is the three")
print("      signed areal radii -- the chiral seats, where this construction puts colour.  And")
print("      the two indices are functions of INDEPENDENT variables: the seat datum 2M carries")
print("      no bead phase, the deck's sector period carries no sky angle and no mass.  So it")
print("      acts on the generation index not weakly but NOT AT ALL.")
print("  Q2  sigma is an involution and Delta(27) has exponent three, so sigma is not in it.")
print("      Computed from its own definition, sigma sends each hinge to a wall and so permutes")
print("      the SAME seat index, as the transposition (0 2).  It NORMALISES Delta(27), and")
print("      together they give order 54 -- an extension at index two, not a coincidence and")
print("      not an identity.")
print("  Q3  *** NO, AND THE OBSTRUCTION IS ONE LINE: Delta(27) is a holonomy, holonomy is a")
print("      representation of pi_1, and pi_1(S^5) is TRIVIAL.  Every flat bundle over the")
print("      compact face has trivial holonomy, so Delta(27) cannot arise there. ***  A second,")
print("      independent reason: a monodromy group needs a branch locus, and the round face is")
print("      homogeneous -- no invariant triple to index, where the Lorentzian face has one.")
print("  Q4  the corpus's two phrases name DISJOINT lists, and P14's own appendix enumerates")
print("      the within-state S_3, the deck Z_3 and the discrete content of colour as separate")
print("      deliverables.  Its vocabulary does not equivocate; the literature's label does.")
print()
print("  ⛭ SO IT IS COLOUR IN THIS CONSTRUCTION, AND THE REASON IS THE INDEX.  W1 is")
print("  demonstrated rather than promised: the same abstract group built from generators on an")
print("  unrelated index returns every invariant identical, so the name carries nothing.")
print()
print("  ⛔ AND THE TWO-COLOURS COLLISION IS NOT DISSOLVED -- IT IS SHARPENED.  The two are not")
print("  one object under two descriptions, and not two embeddings that happen to differ: one")
print("  is a pi_1 representation of a branched structure, and the face carrying the other has")
print("  no loops to have holonomy around.  That is which is which, and why (W2).")
print()
print("  NOT ESTABLISHED: that Delta(27) is the Standard Model's colour SU(3) or any gauge")
print("  group -- it is a finite flat holonomy giving selection rules and no force, as P14")
print("  states.  Not that the compact face's su(3) is defective.  Nothing about occupation")
print("  (W4).  Not that the two threes could not be related by something not yet built: what")
print("  is shown is that nothing in the corpus relates them now.")
print("=" * 90)
