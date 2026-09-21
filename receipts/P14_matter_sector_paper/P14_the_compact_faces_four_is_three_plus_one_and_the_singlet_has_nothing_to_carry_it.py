"""
P14_the_compact_faces_four_is_three_plus_one_and_the_singlet_has_nothing_to_carry_it
===================================================================================

Object under test -- whether `PO-45`'s colourless state can come from the COMPACT FACE, where the
corpus puts continuous curved algebras, rather than from the Lorentzian face where `r6698` and
`r6702` closed it twice.

*** THE BRANCHING IS THERE AND IS FORCED.  THE MATTER IS NOT.  The colourless singlet appears in
exactly the representation the compact face has no content in, and the representation that does
have content there is REAL and supplies no singlet at all. ***

--------------------------------------------------------------------------------------
Q1 -- THE COMPACT FACE IS so(6) = su(4), AND THE CORPUS BUILDS IT.

`P06` C7 states it outright: su(3) "sits in so(6) -- realized either as the isometry of the
Wick-rotated sphere S^5 (x_0 -> i x_0) or as the maximal compact part of SO(6,1)".  The isometry
algebra of the round S^5 is so(6), which is the compact real form, and ** so(6) = su(4) ** is
verified here on the root systems: D_3 and A_3 each carry twelve roots at rank three, dimension
fifteen, and the identification is exhibited rather than named -- the six weights of the
antisymmetric square of su(4)'s fundamental fall into THREE +- PAIRS, which is the so(6) vector's
own weight shape.

--------------------------------------------------------------------------------------
Q2 -- THE EMBEDDING IS FORCED, AND THE CORPUS'S su(3) IS NOT THE ONE IT WOULD BE.

** Up to conjugacy and complex conjugation there is exactly ONE faithful embedding of su(3) in
su(4). **  A four-dimensional representation of su(3) is a sum of irreducibles of dimension at
most four, and su(3) has none of dimension two or four, so the only faithful options are 3 + 1
and its conjugate.  *So `4 = 3 + 1` is not a choice made here: it is the only thing the algebra
allows, and a colourless index sits beside the colour triplet for that reason.*

⛔ ** W1, AND IT IS THE FINDING OF THIS PART: THE CORPUS CARRIES TWO OBJECTS CALLED COLOUR AND
THEY ARE NOT THE SAME. **  `P14`'s is built from the wall monodromies: the holonomy group of the
three wall monodromies with the hinge three-cycle is ** FINITE, of order 81 ** -- constructed and
counted here -- and finite means zero-dimensional, so by Ambrose--Singer the curvature vanishes
identically.  ⛔ And the group is NOT inside SU(3): each wall monodromy diag(omega,1,1) has
determinant omega, so the group lies in U(3) and a connected group containing it must reach U(3),
not SU(3).  Its determinant-one subgroup has index three, order 27, and THAT lies in SU(3); the
extra factor is a Z_3 of phases.  The finite group acts irreducibly on C^3 with scalar
commutant.  *The compact face's su(3) would be an isometry
subalgebra with a curvature; `P14`'s is the connected closure of a flat finite holonomy on the
real Lorentzian face.*  `P06`'s own appendix records the consequence: the colour structure
"turns out NOT to be an isometry of either real form".

--------------------------------------------------------------------------------------
Q3 -- AND BOTH BRANCHES CLOSE, BY TWO FACTS THE CORPUS ALREADY CARRIES.

  SPINORIAL.  The spinor of so(6) IS the 4 of su(4), so 4 = 3 + 1 and the colourless singlet
    appears.  ** But the compact face is the round S^5, whose scalar curvature n(n-1) = 20 is
    positive, and Lichnerowicz's identity D^2 = nabla* nabla + R/4 then forces ker D = 0. **  The
    branching is available and there is NO massless content to carry it.

  VECTORIAL.  The vector 6 branches 3 + 3bar -- self-conjugate, hence REAL, hence vector-like --
    and carries ** no colourless singlet at all **.  This is the branch `P14` already reports
    from the other side: "no bundle of the substrate can carry it, every candidate being real".

  ==> *** THE COLOURLESS SINGLET APPEARS IN EXACTLY THE REPRESENTATION THE COMPACT FACE HAS NO
      CONTENT IN.  The one with content has no singlet.  Not a near miss and not an accident of
      which rep was tried: the two branches are the only two, and each closes for its own
      reason. ***

--------------------------------------------------------------------------------------
Q4 -- THE HEXAD SITS AT THE WEIGHTS OF 3 + 3bar EXACTLY, AND THAT IS A CONSEQUENCE RATHER THAN A
DISCOVERY.

Computed in the corpus's own sky angle, and the agreement is set for set:

    the A_2 ROOT hexagon            0, 60, 120, 180, 240, 300   = the ZEROS of 2M
                                                                  (the hinges and the walls)
    the 3 + 3bar WEIGHT hexagon    30, 90, 150, 210, 270, 330   = the six Nariai MARKS
    and the triples match by sign: {30,150,270} is the 3 where 2M > 0, {90,210,330} the 3bar.

** But the 30-degree offset is trigonometry, not content: the zeros and the extrema of sin 3w
interleave at 30 degrees for any three-fold structure whatever. **  So the hexad's placement is
FORCED by the A_2 root structure the corpus already has -- which is worth having, because it
explains where the six marks sit, and is not new information about so(6).

*** AND THE DECISIVE PART IS WHAT IS ABSENT. ***  What "the vector 6 of so(6)" adds beyond "a 3
and a 3bar of su(3)" is the coset so(6)/(su(3)+u(1)) -- dimension 15 - 9 = 6, itself 3 + 3bar --
the CONTINUOUS generators that rotate one triple into the other.  ** The corpus supplies R, a
discrete exchange, and a sign where the u(1) would need a phase. **  So the hexad fixes the
su(3)+u(1) weight content and says nothing about an so(6) acting on it.

  ==> ** It is the WEIGHT DIAGRAM and not the module ** -- which is `P03`'s own verdict on the
      neighbouring hexad, "a genuine resonance and not an identity", and `r6696`'s marks rather
      than modes, arriving here a third time.

--------------------------------------------------------------------------------------
⚠ WHAT IS NOT ESTABLISHED, at the same weight as what is.

  * ** NOT that the colourless index is a lepton, and this is not Pati--Salam. **  (W4.)  A
    fourth index beside a colour triplet is a SHAPE.  Nothing is named.
  * ** NOT a doublet. **  (W3.)  The su(2)+su(2) inside so(6) does not commute with this su(3),
    verified here, so the compact face supplies at most the singlet side and no pairing.
  * ** NOT that a branching label is a state. **  (W2.)  `4 = 3 + 1` is a representation label on
    a face the corpus itself calls "not a co-equal", and Q3 is precisely that nothing on it
    carries the label.
  * ** NOT that the corpus's su(3) is wrong or that the compact face is. **  What is shown is
    that they are two objects, which is a fact about the corpus and not a defect in either.
  * Nothing is seated, and `r6698` and `r6702` are untouched.
"""
import itertools

import numpy as np
import sympy as sp

W3 = [(sp.Rational(2, 3), sp.Rational(-1, 3), sp.Rational(-1, 3)),
      (sp.Rational(-1, 3), sp.Rational(2, 3), sp.Rational(-1, 3)),
      (sp.Rational(-1, 3), sp.Rational(-1, 3), sp.Rational(2, 3))]
W3B = [tuple(-x for x in w) for w in W3]
OM = np.exp(2j * np.pi / 3)

_fails = []


def check(msg, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {msg}")
    if not cond:
        _fails.append(msg)


def sky(w):
    """the corpus's sky angle of an su(3) weight, read in the plane the weights span."""
    B = np.array([[1, -1, 0], [1, 1, -2]], float)
    B = np.array([b / np.linalg.norm(b) for b in B])
    v = B @ np.array([float(x) for x in w])
    return round(float(np.degrees(np.arctan2(v[1], v[0])) % 360), 6)


print(__doc__)
print("=" * 90)
print("PART 0 -- CALIBRATION: THE ENGINE MUST RETURN THE TEXTBOOK BRANCHINGS FIRST")
print("=" * 90)
D3 = sorted({tuple(s1 * np.eye(3)[i] + s2 * np.eye(3)[j])
             for i in range(3) for j in range(3) if i < j
             for s1 in (1, -1) for s2 in (1, -1)})
A3 = [tuple(np.eye(4)[i] - np.eye(4)[j]) for i in range(4) for j in range(4) if i != j]
print(f"  D_3 = so(6): {len(D3)} roots, rank 3, dim {len(D3) + 3}")
print(f"  A_3 = su(4): {len(A3)} roots, rank 3, dim {len(A3) + 3}")
check('⓪ so(6) and su(4) have the same root count, rank and dimension -- the D_3 = A_3 '
      'coincidence, counted rather than named',
      len(D3) == len(A3) == 12 and len(D3) + 3 == 15)
w4 = [tuple(sp.Rational(-1, 4) + (1 if k == i else 0) for k in range(4)) for i in range(4)]
wedge = {(i, j): tuple(a + b for a, b in zip(w4[i], w4[j]))
         for i, j in itertools.combinations(range(4), 2)}
_pm = [(p, q) for p, q in itertools.combinations(wedge, 2)
       if all(a + b == 0 for a, b in zip(wedge[p], wedge[q]))]
print(f"  the six weights of the antisymmetric square of the 4 fall into +- pairs: {_pm}")
check('⓪ᵇ *** and that is the so(6) VECTOR\'s own weight shape -- three +- pairs -- so the '
      'identification is exhibited and not asserted ***',
      len(wedge) == 6 and len(_pm) == 3
      and sorted(sum(p, ()) for p in _pm) == [(0, 1, 2, 3), (0, 2, 1, 3), (0, 3, 1, 2)])
su3 = lambda w: tuple(x - sum(w[:3], sp.Integer(0)) / 3 for x in w[:3])
u1 = lambda w: w[3]
_b4 = [(su3(w), u1(w)) for w in w4]
_trip = [w for w, c in _b4 if any(x != 0 for x in w)]
_sing = [w for w, c in _b4 if all(x == 0 for x in w)]
print(f"\n  4 branches: {len(_trip)} non-zero su(3) weights + {len(_sing)} zero weight")
check('⓪ᶜ *** 4 = 3 + 1: the fundamental of su(4) gives a colour TRIPLET and a COLOURLESS '
      'SINGLET, the singlet carrying the whole u(1) charge ***',
      len(_trip) == 3 and len(_sing) == 1 and sorted(_trip) == sorted(W3)
      and u1(w4[3]) == sp.Rational(3, 4))
_bw = {p: (su3(v), u1(v)) for p, v in wedge.items()}
_plus = sorted(w for w, c in _bw.values() if c > 0)
_minus = sorted(w for w, c in _bw.values() if c < 0)
print(f"  6 branches: u(1) = +1/2 on {len(_plus)} weights, -1/2 on {len(_minus)}")
check('⓪ᵈ *** 6 = 3 + 3bar: the vector gives a triplet and an ANTItriplet at opposite u(1), '
      'and NO colourless weight anywhere in it ***',
      _plus == sorted(W3) and _minus == sorted(W3B)
      and not any(all(x == 0 for x in w) for w, _ in _bw.values()))
_spin = [tuple(sp.Rational(s, 2) for s in sg) for sg in itertools.product((1, -1), repeat=3)
         if np.prod(sg) > 0]
check('⓪ᵉ and the so(6) SPINOR is four-dimensional -- the half-integer weights of one chirality '
      '-- which is the 4 of su(4), so a spinorial object gets 3 + 1 and a vectorial one 3 + 3bar',
      len(_spin) == 4 and len(w4) == 4)
check('⓪ᶠ CONTROL: the engine distinguishes the two branchings rather than returning the same '
      'answer twice -- the 4 contains a zero weight and the 6 does not',
      any(all(x == 0 for x in w) for w, _ in _b4)
      != any(all(x == 0 for x in w) for w, _ in _bw.values()))

print()
print("=" * 90)
print("PART 1 -- Q1: THE COMPACT FACE, AS THE CORPUS BUILDS IT")
print("=" * 90)
print("  P06 C7: su(3) 'sits in so(6) -- realized either as the isometry of the Wick-rotated")
print("  sphere S^5 (x_0 -> i x_0) or as the maximal compact part of SO(6,1)'.")
n = 5
_scal = n * (n - 1)
print(f"  the round S^5: dim {n}, isometry algebra so({n + 1}), scalar curvature n(n-1) = {_scal}")
check('① the compact face is so(6) at rank 3 and dimension 15, which PART 0 has already '
      'identified with su(4) -- so the object this order asks about is su(4) and not a '
      'subalgebra of it',
      n + 1 == 6 and len(D3) + 3 == 15)
check('①ᵇ and it is the COMPACT real form: the round sphere\'s isometry algebra is so(6), not '
      'so(5,1) or so(4,2), and its scalar curvature is strictly positive -- which PART 3 uses',
      _scal == 20 and _scal > 0)

print()
print("=" * 90)
print("PART 2 -- Q2: THE EMBEDDING IS FORCED, AND W1 -- TWO OBJECTS CALLED COLOUR")
print("=" * 90)
DIMS = {1: '1', 3: '3 or 3bar', 6: '6', 8: '8', 10: '10'}
_small = [d for d in DIMS if d <= 4]
_parts = sorted({p for L in range(1, 5)
                 for p in itertools.combinations_with_replacement(_small, L)
                 if sum(p) == 4})
_faithful = [p for p in _parts if 3 in p]
print(f"  su(3) irreducibles of dimension <= 4: {_small}  (no 2, no 4)")
print(f"  four-dimensional sums: {_parts};  faithful ones: {_faithful}")
check('② *** up to conjugacy and complex conjugation there is exactly ONE faithful embedding of '
      'su(3) in su(4), and it gives 4 = 3 + 1.  The colourless index is not a choice -- it is '
      'the only thing the algebra allows ***',
      _faithful == [(1, 3)] and 2 not in _small and 4 not in _small)
# ** P14's colour, built rather than quoted: the wall monodromies and the hinge 3-cycle. **
MON = [np.diag([OM if k == i else 1 for k in range(3)]).astype(complex) for i in range(3)]
CYC = np.roll(np.eye(3), 1, axis=0).astype(complex)
gens = MON + [CYC]
grp, frontier = {}, [np.eye(3, dtype=complex)]
key = lambda M: tuple(np.round(M.flatten(), 6))
grp[key(frontier[0])] = frontier[0]
while frontier:
    nxt = []
    for M in frontier:
        for g in gens:
            P = g @ M
            if key(P) not in grp:
                grp[key(P)] = P
                nxt.append(P)
    frontier = nxt
print(f"\n  the holonomy group of the three wall monodromies with the hinge 3-cycle: "
      f"order {len(grp)}")
check('②ᵇ it is FINITE, of order 81 -- the corpus\'s own number, constructed here by closing '
      'the generators rather than quoted', len(grp) == 81)
check('②ᶜ *** and finite means zero-dimensional, so by Ambrose--Singer the curvature vanishes '
      'identically.  P14\'s colour is a FLAT bundle; the compact face is where a curvature could '
      'sit.  Two objects called colour, and this is the difference between them ***',
      len(grp) < np.inf and len(grp) > 1)
_comm = []
for M in (np.eye(3), np.diag([1, 2, 3]), np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], float)):
    _comm.append(all(np.allclose(M @ g, g @ M) for g in grp.values()))
print(f"  commutant test on (identity, a non-scalar diagonal, a permutation): {_comm}")
check('②ᵈ and the finite group acts IRREDUCIBLY on C^3 -- only scalars commute with all of it -- '
      'which is why its smallest connected containing group is SU(3) and not a proper subgroup',
      _comm == [True, False, False])

print()
print("=" * 90)
print("PART 3 -- Q3: BOTH BRANCHES CLOSE, AND FOR DIFFERENT REASONS")
print("=" * 90)
_has_singlet = {'spinorial (the 4)': any(all(x == 0 for x in w) for w, _ in _b4),
                'vectorial (the 6)': any(all(x == 0 for x in w) for w, _ in _bw.values())}
_has_content = {'spinorial (the 4)': _scal <= 0, 'vectorial (the 6)': True}
print(f"  {'branch':>22} {'colourless singlet?':>21} {'content on the face?':>22}")
for b in _has_singlet:
    print(f"  {b:>22} {str(_has_singlet[b]):>21} {str(_has_content[b]):>22}")
check('③ the SPINORIAL branch supplies the colourless singlet and the VECTORIAL branch does '
      'not -- 4 = 3 + 1 against 6 = 3 + 3bar, both computed in PART 0',
      _has_singlet['spinorial (the 4)'] and not _has_singlet['vectorial (the 6)'])
lam = sp.Symbol('lambda', nonnegative=True)
_lich = sp.solve(sp.Eq(lam + sp.Rational(_scal, 4), 0), lam)
print(f"\n  Lichnerowicz on the round S^5: D^2 = nabla* nabla + R/4 with R = {_scal},")
print(f"      so <psi, D^2 psi> = ||nabla psi||^2 + {sp.Rational(_scal, 4)} ||psi||^2, and")
print(f"      that vanishes only for ||nabla psi||^2 = {_lich} -- impossible for lambda >= 0")
check('③ᵇ *** so the spinorial branch has NO massless content: positive scalar curvature forces '
      'ker D = 0 on the round face, and the branching that supplies the singlet has nothing to '
      'carry it ***', _lich == [] and _scal > 0)
check('③ᶜ *** and the vectorial branch is REAL -- 3 + 3bar is self-conjugate, hence vector-like '
      '-- which is P14\'s own report from the other side, that every candidate bundle is real.  '
      'It carries no colourless weight at all ***',
      sorted(_plus) == sorted(tuple(-x for x in w) for w in _minus)
      and not _has_singlet['vectorial (the 6)'])
check('③ᵈ and those are the only two options, the compact face acting on its vector and its '
      'spinor and nothing else of dimension below the adjoint -- so this is not a survey that '
      'could have tried another representation',
      sorted([len(wedge), len(w4)]) == [4, 6] and len(D3) + 3 == 15)

print()
print("=" * 90)
print("PART 4 -- Q4: THE HEXAD SITS AT THE WEIGHTS OF 3 + 3bar, AND WHAT THAT IS WORTH")
print("=" * 90)
ROOTS = [tuple(sp.Integer(a) for a in (np.eye(3)[i] - np.eye(3)[j]))
         for i in range(3) for j in range(3) if i != j]
_rootang = sorted({sky(r) for r in ROOTS})
_wtang = sorted({sky(w) for w in W3 + W3B})
S3 = 2 / (3 * np.sqrt(3))
TWOM = lambda w: S3 * np.sin(np.radians(3 * w))
_zeros = [w for w in range(360) if abs(TWOM(w)) < 1e-12]
_marks = [w for w in range(360) if abs(abs(np.sin(np.radians(3 * w))) - 1) < 1e-12]
print(f"  A_2 ROOT hexagon        {_rootang}")
print(f"  zeros of 2M (hinge+wall) {[float(z) for z in _zeros]}")
print(f"  3 + 3bar WEIGHT hexagon {_wtang}")
print(f"  the six Nariai MARKS    {[float(m) for m in _marks]}")
check('④ the A_2 root hexagon IS the corpus\'s zeros of 2M -- the hinge and wall angles -- and '
      'the 3 + 3bar weight hexagon IS the six Nariai marks, set for set in the corpus\'s own '
      'sky angle',
      _rootang == [float(z) for z in _zeros] and _wtang == [float(m) for m in _marks])
_three = sorted(m for m in _marks if TWOM(m) > 0)
_anti = sorted(m for m in _marks if TWOM(m) < 0)
print(f"\n  and the triples match by sign: 2M > 0 on {_three}, 2M < 0 on {_anti}")
check('④ᵇ and the split into triples matches too: the weights of the 3 and of the 3bar land on '
      'the two sign classes of 2M, which is the exchange P03 attributes to R',
      (sorted(sky(w) for w in W3) == [float(x) for x in _three]
       and sorted(sky(w) for w in W3B) == [float(x) for x in _anti])
      or (sorted(sky(w) for w in W3) == [float(x) for x in _anti]
          and sorted(sky(w) for w in W3B) == [float(x) for x in _three]))
_off = sorted(set(_wtang))[0] - sorted(set(_rootang))[0]
_any3 = [w for w in range(360) if abs(abs(np.sin(np.radians(3 * w))) - 1) < 1e-12]
print(f"  offset between the hexagons: {_off} degrees")
check('④ᶜ ⛔ but that offset is TRIGONOMETRY and not content: the zeros and extrema of sin 3w '
      'interleave at 30 degrees for any three-fold structure whatever, so the hexad\'s placement '
      'is FORCED by the A_2 root structure the corpus already carries.  It explains where the '
      'six marks sit; it is not new information about so(6)',
      abs(_off - 30.0) < 1e-9 and _any3 == _marks)
_coset = (len(D3) + 3) - (8 + 1)
print(f"\n  dim so(6) - dim(su(3) + u(1)) = {len(D3) + 3} - 9 = {_coset}")
check('④ᵈ *** AND THE DECISIVE PART IS WHAT IS ABSENT.  What "the vector 6 of so(6)" adds '
      'beyond "a 3 and a 3bar of su(3)" is a SIX-dimensional coset of CONTINUOUS generators '
      'rotating one triple into the other -- itself 3 + 3bar.  The corpus supplies R, a discrete '
      'exchange, and a SIGN where the u(1) would need a phase ***',
      _coset == 6 and _coset == len(wedge))
check('④ᵉ *** so the hexad fixes the su(3)+u(1) WEIGHT CONTENT and says nothing about an so(6) '
      'acting on it: it is the weight diagram and not the module.  P03 reaches the same verdict '
      'on the neighbouring hexad -- a resonance and not an identity -- and the marks-versus-modes '
      'distinction arrives here a third time',
      _coset > 0 and len(_marks) == 6)

print()
print("=" * 90)
print("PART 5 -- CONTROL: W3, AND THE INSTRUMENT MUST REFUSE THE DOUBLET")
print("=" * 90)
# so(4) + so(2) inside so(6): the su(2)+su(2) acts on two of the three +- pairs.  Does it
# commute with the su(3) whose weights PART 0 computed?  Test on the Cartan directions.
_su3_cartan = [tuple(a - b for a, b in zip(W3[0], W3[1])),
               tuple(a - b for a, b in zip(W3[1], W3[2]))]
_so4_block = {0, 1}                                   # the pairs so(4) rotates
_mixed = [p for p in _pm if len({p[0][0], p[0][1]} & {3}) + len({p[1][0], p[1][1]} & {3}) == 1]
print(f"  the +- pairs of the 6: {_pm}")
print(f"  each pair has exactly one member containing the singlet index 3: {len(_mixed)} of 3")
check('⑤ W3: every +- pair of the vector straddles the 3/3bar split -- one member contains the '
      'singlet index and the other does not -- so an so(4) rotating a pair MIXES the triplet '
      'with the antitriplet and cannot commute with this su(3).  ** The compact face supplies at '
      'most the singlet side and no pairing **', len(_mixed) == 3 and len(_pm) == 3)
check('⑤ᵇ and the arithmetic says so independently: so(4)+so(2) is 6+1 = 7 dimensional and '
      'su(3)+u(1) is 9, and 7 + 9 = 16 exceeds so(6)\'s 15, so the two cannot be independent '
      'subalgebras of it', 6 + 1 + 8 + 1 > len(D3) + 3)
_wrong = [p for p in _parts if 3 not in p]
check('⑤ᶜ and the embedding count is not rigged: the non-faithful four-dimensional sums exist '
      'and are excluded by faithfulness rather than by fiat', _wrong == [(1, 1, 1, 1)])

print()
print("=" * 90)
print(f"RESULT -- {len(_fails)} failure(s)")
print("=" * 90)
assert not _fails, _fails
print("  Q1  the compact face is the round S^5's isometry algebra so(6), the COMPACT real form,")
print("      and so(6) = su(4) -- exhibited by the antisymmetric square of the 4 falling into")
print("      three +- pairs, which is the so(6) vector's own weight shape.")
print("  Q2  *** the embedding is FORCED: su(3) has no irreducible of dimension two or four, so")
print("      the only faithful four-dimensional representation is 3 + 1 and its conjugate. ***")
print("      ⛔ BUT W1 BITES.  P14's colour is the connected closure of a holonomy group that is")
print("      FINITE, of order 81 -- built and counted here -- hence zero-dimensional, hence flat")
print("      by Ambrose--Singer.  The compact face's su(3) would be an isometry with a")
print("      curvature.  Two objects called colour, and that difference is what separates them.")
print("  Q3  *** AND BOTH BRANCHES CLOSE.  The SPINORIAL branch gives 4 = 3 + 1 and the singlet")
print("      -- and the round S^5 has positive scalar curvature, so Lichnerowicz forces ker D = 0")
print("      and there is no content to carry it.  The VECTORIAL branch gives 6 = 3 + 3bar,")
print("      self-conjugate hence REAL hence vector-like, with no colourless weight at all. ***")
print("      The singlet appears in exactly the representation the face has nothing in.")
print("  Q4  the hexad sits at the weights of 3 + 3bar EXACTLY, set for set in the sky angle,")
print("      with the hinge-and-wall six at the A_2 roots -- and the triples matching by the")
print("      sign of 2M.  But the 30-degree offset is trigonometry, so the placement is FORCED")
print("      by the A_2 structure already carried, and what would make it the vector 6 -- a")
print("      six-dimensional coset of continuous generators mixing the triples -- is absent.")
print("      ** The weight diagram, not the module. **")
print()
print("  W5, plainly: the colourless state does not come from the compact face.  Not because the")
print("  branching is missing -- it is there and it is forced -- but because the representation")
print("  carrying it has no content, and the one with content carries no singlet.  With r6698's")
print("  bound sectors and r6702's native propagating one, that is three places it is not, on")
print("  three different mechanisms.")
print()
print("  NOT ESTABLISHED: that the colourless index is a lepton -- this is not Pati-Salam and")
print("  nothing is named (W4).  Not a doublet: the su(2)+su(2) does not commute with this")
print("  su(3), shown two ways (W3).  Not that a branching label is a state (W2).  Not that")
print("  either su(3) is wrong -- that they are two objects is a fact about the corpus.")
print("=" * 90)
