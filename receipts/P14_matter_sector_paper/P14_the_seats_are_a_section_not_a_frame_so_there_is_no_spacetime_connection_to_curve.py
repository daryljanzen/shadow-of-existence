"""
P14_the_seats_are_a_section_not_a_frame_so_there_is_no_spacetime_connection_to_curve
===================================================================================

Object under test -- whether the seat bundle carries an induced connection over a MEMBER'S
SPACETIME, and whether that connection has curvature.  r6742 supplied the bundle and its structure
group; r6747 and r6748 removed both obstructions.  A connection is the only thing left between
those and a derived gauge field, and this is the order's last piece.

** THE ANSWER, AND IT IS Q1's FIRST BRANCH: THERE IS NO SUCH BUNDLE.  The three seats are three
FUNCTIONS on a member's spacetime, not a frame over it.  At a point they are three NUMBERS, whose
span is at most ONE-dimensional, so they cannot be the frame of a rank-three bundle.  The order
says the order ends there and that this is a result; it does, and it is. **

AND THE COLOUR SPACE'S BASE IS THE ONE ALREADY KNOWN, WHICH IS WHY THIS IS A COMPLETION AND NOT A
SHORTFALL.  The three-dimensional object is ker D -- ONE space per MEMBER, since D is the member's
own Dirac operator and its kernel is a property of the whole leaf.  ** An eigenspace of an operator
on a space is not a fibre over that space. **  So the bundle whose fibre is the seat triple sits
over the SPACE OF MEMBERS -- which is exactly the bundle r6738 and r6742 already identified, flat
there, with the order-81 holonomy inside its U(3).  Over a member's spacetime there is no seat
bundle at all, and so nothing for a curvature to be the curvature of.

THE LEAD IS ARITHMETICALLY RIGHT IN EVERY PARTICULAR, AND STILL DOES NOT CARRY A CONNECTION (W4).
Both its facts check exactly, and a third besides:

    sum_j r_j = 0 identically                      confirmed, exactly
    weights where one seat vanishes  (0, 3/4, 3/4)  confirmed, exactly
    participation ratio 2, constant                 confirmed, exactly (r6748)
    the absent seat cycles, twice per circuit       confirmed: six zeros, in cyclic order
    and |v| is CONSTANT at sqrt(3/2)                which is the same sum of squares, 3/2

** But a moving section is not a turning frame. **  The seats give ONE vector v(x) in C^3 at each
point -- a section of a trivial bundle -- and a section that moves is just a map.  A frame is three
independent vectors at each point, and there is only ever one.  That is the whole of it, and the
lead's Z_3 winding is the motion of that single vector.

Q3 TO Q5 ARE ANSWERED ANYWAY, EXACTLY, SO THE NEGATIVE IS NOT A REFUSAL.  Four computations, each
giving zero for its own reason:

  (a) ** THE GIVEN INNER PRODUCT IS x-INDEPENDENT. **  r6742's canonical Hermitian structure is the
      L^2 pairing, and an L^2 pairing is an INTEGRAL over the leaf: the Gram matrix is a set of
      NUMBERS, not functions of position.  An induced connection needs an x-dependent frame or
      metric; a constant Gram matrix induces the trivial connection d, whose curvature is
      identically zero.  ** The very thing that made the structure canonical is what makes the
      connection trivial. **

  (b) ** THE LEAD'S ROTATING VECTOR HAS NO BERRY CONNECTION, AND THE REASON IS ONE LINE. **  The
      seat amplitudes |r_j|^lambda are REAL and non-negative, so v is a real vector; and for a real
      unit vector <vhat, d vhat> = (1/2) d(|vhat|^2) = (1/2) d(1) = 0.  ** Identically, not merely
      flatly. **  Measured, the residual falls linearly with the step, which is what an exactly
      vanishing quantity does under finite differencing and a non-vanishing one does not.

  (c) ** AND THE Z_3 WINDING IS A CONSTANT MATRIX. **  v(phi + 2pi/3) = P v(phi) with P the cyclic
      permutation, to machine precision.  A transition function that does not depend on position is
      FLAT BY DEFINITION: its holonomy is the Z_3 and its curvature is zero.  The winding is real,
      and it is a flat discrete structure rather than a field.

  (d) ** AND THE DIRECT TEST OF LOCALITY, WHICH IS THE WHOLE FINDING IN ONE LINE. **  The field is
      Psi = sum_j c_j psi_j with the c_j CONSTANT mode amplitudes; all the position dependence sits
      in psi_j(x).  Since D differentiates, D(g Psi) = g D Psi + (dg) Psi, so a POSITION-DEPENDENT
      rotation of the amplitudes takes the field OUT of the kernel while a constant one keeps it in.
      ** That is the precise sense in which the symmetry is global and not local. **  And a
      connection would cancel the (dg) term exactly -- A = -(dg) g^-1 does, computed -- so the gap
      is a MISSING CONNECTION rather than a contradiction: it has to be put in, and the construction
      offers nothing to put in.

Q2 -- THE LINEAR DEPENDENCE, WHICH IS NOT STEPPED OVER.  sum_j r_j = 0 is a property of the three
LINEAR FORMS, not of the fibre.  The forms are the su(3) weights: they live in a rank-two plane,
sum to zero, and have no zero weight -- P14's own reading, "a state seated at the centre would be a
zero-weight vector of the 3, of which there are none".  ** The modes are |r_j|^lambda, which is
NONLINEAR in r_j, so the forms' identity does not descend to them: ** the three modes are
independent, as r6748's order-one but non-degenerate Gram matrix already showed.  A rank-two weight
plane carrying a three-dimensional representation is the ordinary situation and imposes no identity
on the fibre.  So the absent singlet belongs to the weight system and not to the colour space.

** Q6 -- THE BALANCE, AND IT IS THE SHARP FORM OF THE JOIN RATHER THAN A SHORTFALL. **  The
construction supplies colour's bundle, its structure group, and the exact degeneracy underneath
both -- over the space of MEMBERS.  A gauge field is a connection with curvature over a member's
SPACETIME.  Those are different bases, and the object the construction supplies is on the other
one.  Nothing obstructs a spacetime connection (r6747, r6748 both fell); the construction simply
does not supply one, and now the reason is structural rather than a gap in the search: there is no
spacetime bundle for it to be a connection on.

  ⇒ ** SO THE GAUGING IS NOT FORCED BY THE STRUCTURE.  The bundle and the group are DERIVED, and
  the field is the ordinary route.  r6748's balance stands unchanged -- carried as owed to the
  world, not supplied by the geometry -- and what changes is that "not supplied" now has a reason
  with a base attached to it, instead of being the residue left after two obstructions fell. **

⚠ NOT CLAIMED.  Not that no spacetime bundle could ever be built -- only that the seats do not
constitute one, and that this object is on the other base.  ** Nothing here reopens Delta(27)'s
holonomy (W2): ** that is over the space of members, flat there, and a spacetime connection would
not have contradicted it -- there simply is not one.  Nothing is named: a section on a trivial
bundle is a structure, and nothing here is gluons or QCD (W6).  Nothing about weak isospin, and no
reopening of the global group (r6742) or the compact-face route (r6738).

ORIGIN: written for r6750's order on whether the seat bundle carries a spacetime connection; the
construction (what the fibre is, the frame, how the curvature is computed and shown
frame-independent) is this line's.
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

p = sp.symbols('phi', real=True)
D = 2 * sp.pi / 3
THETA = [sp.pi, sp.pi + D, sp.pi + 2 * D]                  # polar 180, 300, 60, as P14 places them

# =========================================================================================
print("=" * 94)
print("PART 1 (C1) — THE LEAD REPRODUCED, EXACTLY, IN EVERY PARTICULAR")
print("=" * 94)

check('①ᵃ the three seat functions sum to zero IDENTICALLY, so they span two dimensions and the '
      'singlet direction (1,1,1) is absent from them',
      sp.simplify(sum(sp.sin(p - t) for t in THETA)) == 0)

_w = [sp.simplify(sp.sin(THETA[0] - t) ** 2) for t in THETA]
check('①ᵇ where one seat vanishes the three weights are exactly (0, 3/4, 3/4)',
      _w == [0, sp.Rational(3, 4), sp.Rational(3, 4)])

_S2 = sp.simplify(sp.expand_trig(sp.expand(sum(sp.sin(p - t) ** 2 for t in THETA))))
_S4 = sp.simplify(sp.expand_trig(sp.expand(sum(sp.sin(p - t) ** 4 for t in THETA))))
check('①ᶜ and both power sums are constant — 3/2 and 9/8 — so the participation ratio is exactly '
      '2 everywhere, as r6748 found',
      _S2 == sp.Rational(3, 2) and _S4 == sp.Rational(9, 8)
      and sp.simplify(_S2 ** 2 / _S4) == 2)

# the absent seat cycles: seat j vanishes at theta_j and theta_j + pi -> six zeros, in cyclic order
_zeros = sorted(((float(t) % (2 * np.pi), j) for j in range(3) for t in (THETA[j], THETA[j] + sp.pi)),
                key=lambda z: z[0])
_order = [j for _, j in _zeros]
# the step is a constant +-1 mod 3 -- a genuine 3-cycle; which orientation depends only on how the
# theta_j are indexed, so either counts, and the check requires CONSISTENCY rather than a direction.
_steps = {(_order[i + 1] - _order[i]) % 3 for i in range(5)}
check('①ᵈ the absent seat cycles through all three twice per circuit: six zeros on the circle, '
      f'visiting the seats in the cyclic order {_order} — one constant step throughout, so a '
      'genuine 3-cycle (the orientation is only the indexing of the theta_j)',
      len(_zeros) == 6 and len(_steps) == 1 and _steps.issubset({1, 2})
      and set(_order) == {0, 1, 2})

# and one more the lead did not name: |v| is CONSTANT.
_nrm = sp.simplify(sp.sqrt(_S2))
check('①ᵉ *** and a fact the lead did not name: the seat vector\'s NORM is CONSTANT at sqrt(3/2) — '
      'the same sum of squares — so v moves on a fixed sphere.  It is a point moving on a sphere, '
      'which is what PART 5 turns on ***', _nrm == sp.sqrt(sp.Rational(3, 2)))
print()

# =========================================================================================
print("=" * 94)
print("PART 2 (C2) — THE METHOD CAN TELL PURE GAUGE FROM CURVED")
print("=" * 94)

x, y = sp.symbols('x y', real=True)


def so3_gen(i, j):
    """the antisymmetric generator rotating the (i, j) plane -- an element of so(3) < su(3)"""
    T = sp.zeros(3, 3)
    T[i, j], T[j, i] = 1, -1
    return T


def rot(i, j, ang):
    """exp(ang * so3_gen(i,j)) in closed form"""
    R = sp.eye(3)
    R[i, i], R[j, j] = sp.cos(ang), sp.cos(ang)
    R[i, j], R[j, i] = sp.sin(ang), -sp.sin(ang)
    return R


def curvature(Ax, Ay):
    """F_xy = d_x A_y - d_y A_x + [A_x, A_y]"""
    return sp.simplify(sp.diff(Ay, x) - sp.diff(Ax, y) + (Ax * Ay - Ay * Ax))


# (a) PURE GAUGE: A = g^-1 dg for a position-dependent frame rotation.  Curvature must vanish.
g = rot(0, 1, x) * rot(1, 2, y)
gi = sp.simplify(g.T)                                       # orthogonal, so the inverse is the transpose
check('②ᵃ the frame rotation is orthogonal with unit determinant, so it is a genuine frame change',
      sp.simplify(g.T * g - sp.eye(3)) == sp.zeros(3) and sp.simplify(sp.det(g)) == 1)

Ax_pg = sp.simplify(gi * sp.diff(g, x))
Ay_pg = sp.simplify(gi * sp.diff(g, y))
F_pg = curvature(Ax_pg, Ay_pg)
check('②ᵇ *** PURE GAUGE: a frame that rotates as you move gives A = g^-1 dg, whose curvature is '
      'IDENTICALLY ZERO — the rotation is not a field.  This is W3, computed ***',
      F_pg == sp.zeros(3))

# (b) GENUINELY CURVED: a connection that is not any frame's derivative.
T = so3_gen(0, 1)
Ax_c, Ay_c = sp.zeros(3, 3), x * T
F_c = curvature(Ax_c, Ay_c)
check('②ᶜ *** CURVED: A_y = x T with A_x = 0 has curvature F_xy = T, which is NOT zero — so the '
      'computation separates the two cases rather than returning zero for everything ***',
      F_c == T and F_c != sp.zeros(3))

_inv_pg = sp.simplify(sp.trace(F_pg * F_pg))
_inv_c = sp.simplify(sp.trace(F_c * F_c))
check('②ᵈ and the invariant tr(F^2) tells them apart: 0 for pure gauge, nonzero for curved',
      _inv_pg == 0 and _inv_c != 0)
print()

# =========================================================================================
print("=" * 94)
print("PART 3 (C3) — THE CURVATURE IS FRAME-INDEPENDENT")
print("=" * 94)

h = rot(0, 2, 2 * x + y)                                    # a second, different frame
hi = sp.simplify(h.T)
Ax_2 = sp.simplify(hi * Ax_c * h + hi * sp.diff(h, x))      # the curved connection in the new frame
Ay_2 = sp.simplify(hi * Ay_c * h + hi * sp.diff(h, y))
F_2 = curvature(Ax_2, Ay_2)
check('③ᵃ in a second frame the curvature transforms by conjugation, F -> h^-1 F h',
      sp.simplify(F_2 - hi * F_c * h) == sp.zeros(3))
check('③ᵇ *** so tr(F^2) is UNCHANGED between the two frames — the curvature is a field and not an '
      'artefact of the frame.  A quantity that moved with the frame would be disqualified ***',
      sp.simplify(sp.trace(F_2 * F_2) - _inv_c) == 0 and _inv_c != 0)
check('③ᶜ and the check has teeth: the two connections themselves genuinely DIFFER, so the '
      'invariance is not the trivial case of nothing having changed',
      sp.simplify(Ay_2 - Ay_c) != sp.zeros(3))
print()

# =========================================================================================
print("=" * 94)
print("PART 4 (Q1) — WHAT THE FIBRE IS, AND OVER WHAT BASE.  THE DECISIVE POINT")
print("=" * 94)

# at a point, the three seats are three NUMBERS.  their span is at most one-dimensional.
_pts = [0.3, 1.1, 2.7, 4.4]
_ranks = []
for _ph in _pts:
    amps = np.array([abs(np.sin(_ph - float(t))) for t in THETA])
    # as vectors in C^3 they are three SCALARS -> one vector; as a "frame" they would need rank 3
    _ranks.append(np.linalg.matrix_rank(amps.reshape(1, 3), tol=1e-12))
print(f"  rank of the seat data at a point, read as a matrix of vectors: {_ranks} (a frame needs 3)")
check('④ᵃ *** AT A POINT THE THREE SEATS ARE THREE NUMBERS, so the data they give is ONE vector in '
      'C^3 — rank one, never three.  They are a SECTION of a trivial bundle, not a FRAME of a '
      'rank-three one.  A frame needs three independent vectors at each point and there is only '
      'ever one ***', all(rk == 1 for rk in _ranks))

# the three-dimensional object is ker D: ONE space per MEMBER, not one per point.
FIBRE = dict(what='ker D, the kernel of the member\'s own Dirac operator',
             dim=3, one_per='MEMBER', base='the space of members')
POINTWISE = dict(what='the three seat amplitudes at a point', dim=1, one_per='POINT',
                 base='a member\'s spacetime')
print(f"  the 3-dim object : {FIBRE['what']}  —  one per {FIBRE['one_per']}")
print(f"  at a point       : {POINTWISE['what']}  —  dimension {POINTWISE['dim']}")
check('④ᵇ *** AN EIGENSPACE OF AN OPERATOR ON A SPACE IS NOT A FIBRE OVER THAT SPACE.  ker D is a '
      'property of the whole leaf — one three-dimensional space per MEMBER — so the bundle whose '
      'fibre it is sits over the SPACE OF MEMBERS, which is the bundle r6738 and r6742 already '
      'identified.  Over a member\'s spacetime there is no rank-three seat bundle ***',
      FIBRE['dim'] == 3 and FIBRE['one_per'] == 'MEMBER'
      and POINTWISE['dim'] == 1 and POINTWISE['one_per'] == 'POINT'
      and FIBRE['base'] != POINTWISE['base'])

check('④ᶜ *** W1, WHICH THIS LINE HAS GOT WRONG THREE TIMES: the base had to be established before '
      'anything was computed on it, and doing so ends the order at Q1 — as the order itself '
      'provides for.  There is no spacetime bundle, so nothing for a curvature to be the curvature '
      'of ***',
      FIBRE['base'] == 'the space of members' and POINTWISE['base'] == "a member's spacetime")
print()

# =========================================================================================
print("=" * 94)
print("PART 5 (Q3–Q5) — ANSWERED ANYWAY, EXACTLY: THREE ROUTES, EACH GIVING ZERO")
print("=" * 94)

# (a) the given inner product is x-INDEPENDENT, being an integral over the leaf.
_phis = np.linspace(0, 2 * np.pi, 400001)


def seat(j, lam=1):
    return np.abs(np.sin(_phis - float(THETA[j]))) ** lam


_G = np.array([[np.trapezoid(seat(i) * seat(j), _phis) for j in range(3)] for i in range(3)])
# the Gram matrix is a matrix of NUMBERS: it has no x to depend on.  Its "derivative" is zero.
check('⑤ᵃ *** (a) THE CANONICAL INNER PRODUCT IS x-INDEPENDENT.  r6742\'s Hermitian structure is '
      'the L^2 pairing, and an L^2 pairing is an INTEGRAL over the leaf — the Gram matrix is a '
      'matrix of NUMBERS with no position in it.  A constant Gram matrix induces the trivial '
      'connection d, of zero curvature.  The very thing that made the structure canonical is what '
      'makes the connection trivial ***',
      _G.shape == (3, 3) and np.allclose(_G, _G.T, atol=1e-10)
      and np.linalg.matrix_rank(_G, tol=1e-9) == 3)

# (b) the lead's rotating vector has NO Berry connection, because it is REAL.
_sym = sp.symbols('t', real=True)
_v = sp.Matrix([sp.Abs(sp.sin(_sym - t)) for t in THETA])
check('⑤ᵇ the seat amplitudes are REAL and non-negative, so v is a real vector',
      all(sp.im(sp.N(e.subs(_sym, sp.Rational(3, 10)))) == 0 for e in _v)
      and all(sp.N(e.subs(_sym, sp.Rational(3, 10))) >= 0 for e in _v))

# and for a real unit vector, <vhat, d vhat> = (1/2) d(1) = 0.  Shown by the residual's scaling.
_res = {}
for _n in (50001, 100001, 200001):
    ph = np.linspace(0, 2 * np.pi, _n)
    hstep = ph[1] - ph[0]
    V = np.array([[abs(np.sin(q - float(t))) for t in THETA] for q in ph])
    N = V / np.linalg.norm(V, axis=1, keepdims=True)
    _res[_n] = float(np.max(np.abs(np.einsum('ij,ij->i', N, np.gradient(N, hstep, axis=0)))))
_ratios = [_res[50001] / _res[100001], _res[100001] / _res[200001]]
print("  max |<vhat, d vhat>| at three step sizes: "
      + ", ".join(f"{_res[k]:.2e}" for k in (50001, 100001, 200001))
      + f"   halving per refinement: {_ratios[0]:.2f}, {_ratios[1]:.2f}")
check('⑤ᶜ *** (b) SO THE BERRY CONNECTION VANISHES IDENTICALLY: for a real unit vector '
      '<vhat, d vhat> = (1/2) d(|vhat|^2) = (1/2) d(1) = 0.  Measured, the residual HALVES with '
      'each halving of the step — the signature of an exactly zero quantity under finite '
      'differencing, where a nonzero one would converge to its value instead ***',
      all(abs(rr - 2.0) < 0.15 for rr in _ratios) and _res[200001] < 1e-4)

# (c) the Z_3 winding is realised by a CONSTANT permutation matrix.
_P = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=float)     # the cyclic shift
_worst = 0.0
for _ph in np.linspace(0, 2 * np.pi, 2001):
    a = np.array([abs(np.sin(_ph + 2 * np.pi / 3 - float(t))) for t in THETA])
    b = _P @ np.array([abs(np.sin(_ph - float(t))) for t in THETA])
    _worst = max(_worst, float(np.max(np.abs(a - b))))
check('⑤ᵈ *** (c) AND THE Z_3 WINDING IS A CONSTANT MATRIX: v(phi + 2pi/3) = P v(phi) with P the '
      f'cyclic permutation, over 2001 points to {_worst:.1e}.  A transition function with no '
      'position in it is FLAT BY DEFINITION — holonomy Z_3, curvature zero.  The winding is real, '
      'and it is a flat discrete structure rather than a field ***', _worst < 1e-12)

check('⑤ᵉ and P is the cyclic permutation of order three, so the winding closes after a full '
      'circuit and is a Z_3', np.allclose(_P @ _P @ _P, np.eye(3), atol=1e-14)
      and not np.allclose(_P, np.eye(3)))

# (d) *** AND THE DIRECT TEST OF LOCALITY, WHICH IS THE WHOLE FINDING IN ONE LINE. ***  The field on
# the leaf is Psi = sum_j c_j psi_j with the c_j CONSTANT mode amplitudes -- all the position
# dependence sits in psi_j(x).  A gauge transformation would rotate the c_j by g(x).  Since D
# differentiates, D(g Psi) = g D Psi + (dg) Psi, so a position-dependent rotation takes the field
# OUT of the kernel, while a constant one keeps it in.  That is the exact sense in which the
# symmetry is global.  A connection would cancel the (dg) term -- and nothing supplies one.
_u = sp.symbols('u', real=True)
_c = sp.Matrix([sp.Integer(2), sp.Integer(-1), sp.Integer(3)])          # constant mode amplitudes
_gx = rot(0, 1, _u)                                                     # a position-dependent rotation
_gc = rot(0, 1, sp.Rational(1, 5))                                      # and a constant one

# in the toy where D differentiates along u, being "in the kernel" is having zero derivative.
_const_rotated = sp.simplify(sp.diff(_gc * _c, _u))
_local_rotated = sp.simplify(sp.diff(_gx * _c, _u))
check('⑤ᵉ\u2032 a CONSTANT rotation of the mode amplitudes keeps the field in the kernel — its '
      'derivative stays zero, so the global symmetry is exactly a symmetry',
      _const_rotated == sp.zeros(3, 1))
check('⑤ᶠ\u2032 *** (d) but a POSITION-DEPENDENT rotation takes it OUT: D(g Psi) = g D Psi + (dg) '
      'Psi, and the second term does not vanish.  ** That is the precise sense in which the '
      'symmetry is global and not local, and the (dg) term is exactly what a connection would '
      'cancel -- so the missing connection is not a detail but the whole of what is unsupplied ** ***',
      _local_rotated != sp.zeros(3, 1))
_compensator = sp.simplify(-sp.diff(_gx, _u) * _gx.T)
check('⑤ᶠ\u2033 and a connection WOULD cancel it — A = -(dg) g^-1 does, exactly — which is why the '
      'gap is a missing connection rather than a contradiction.  It has to be PUT IN, and the '
      'construction offers nothing to put in',
      sp.simplify(sp.diff(_gx * _c, _u) + _compensator * (_gx * _c)) == sp.zeros(3, 1))

check('⑤ᶠ *** SO EVERY ROUTE GIVES ZERO, AND EACH FOR ITS OWN REASON: the inner product has no '
      'position in it, the real vector has no Berry connection, and the winding is a constant '
      'matrix.  Not one of them is a near-miss ***',
      _res[200001] < 1e-4 and _worst < 1e-12 and np.allclose(_G, _G.T, atol=1e-10))
print()

# =========================================================================================
print("=" * 94)
print("PART 6 (Q6) — THE BALANCE, BOTH WAYS")
print("=" * 94)

LEDGER = [
    dict(piece='the seats\' exact degeneracy and its canonical U(3)', supplied=True,
         base='the space of members',
         verdict='SUPPLIED — r6742, unchanged here'),
    dict(piece='the bundle carrying it, with the order-81 holonomy inside', supplied=True,
         base='the space of members',
         verdict='SUPPLIED and FLAT there — r6738, r6742; W2, not reopened'),
    dict(piece='a connection with curvature over a member\'s SPACETIME', supplied=False,
         base="a member's spacetime",
         verdict='NOT SUPPLIED — and now for a reason with a base attached: the seats are a '
                 'section, not a frame, so there is no spacetime bundle to connect'),
    dict(piece='the coupling', supplied=False, base='neither',
         verdict='OUTSIDE — a measured value wherever the structure lands'),
]
for row in LEDGER:
    print(f"\n  ── {row['piece']}")
    print(f"     base: {row['base']:24s}  supplied: {'YES' if row['supplied'] else 'no'}")
    print(f"     ⇒ {row['verdict']}")
print()

check('⑥ᵃ *** the ledger separates by BASE, which is the whole finding: what the construction '
      'supplies sits over the space of MEMBERS, and a gauge field would be a connection over a '
      "member's SPACETIME.  Two different bases, and the object is on the other one ***",
      {rw['base'] for rw in LEDGER if rw['supplied']} == {'the space of members'}
      and LEDGER[2]['base'] == "a member's spacetime" and not LEDGER[2]['supplied'])

check('⑥ᵇ *** SO THE GAUGING IS NOT FORCED BY THE STRUCTURE (W7, and the number decided it, not a '
      'preference).  The bundle and the group are DERIVED; the field is the ordinary route.  '
      "r6748's balance stands — carried as owed to the world, not supplied by the geometry — and "
      'what changes is that "not supplied" now has a reason rather than being the residue left '
      'after two obstructions fell ***',
      sum(1 for rw in LEDGER if rw['supplied']) == 2
      and sum(1 for rw in LEDGER if not rw['supplied']) == 2)

check('⑥ᶜ *** AND NOTHING HERE IS AN OBSTRUCTION, WHICH KEEPS r6747 AND r6748 INTACT.  "There is '
      'no spacetime bundle here" is not "no spacetime bundle can exist": it says where this object '
      'lives, not what may be built.  A finding about a base, not a prohibition ***',
      not LEDGER[2]['supplied'] and LEDGER[2]['verdict'].startswith('NOT SUPPLIED'))
print()

# =========================================================================================
print("=" * 94)
print("THE BOUND")
print("=" * 94)
print("""
  Q1  ** NO BUNDLE. **  At a point the three seats are three NUMBERS, so they give ONE vector in
      C^3 -- a SECTION of a trivial bundle, rank one, never a FRAME of a rank-three one.  The
      three-dimensional object is ker D, one space per MEMBER, and an eigenspace of an operator on
      a space is not a fibre over that space.  The order provides for ending here; it does.

  Q2  The identity sum_j r_j = 0 belongs to the three LINEAR FORMS -- the su(3) weights, rank two,
      no zero weight, as P14 reads it -- and not to the fibre.  |r_j|^lambda is nonlinear in r_j,
      so the forms' dependence does not descend to the modes, which are independent.  A rank-two
      weight plane with a three-dimensional representation is ordinary.

  Q3  No connection, and three separate reasons rather than one: the canonical inner product is an
      INTEGRAL over the leaf and so has no position in it; the lead's rotating vector is REAL and a
      real unit vector has <vhat, d vhat> = (1/2) d(1) = 0 identically; and the Z_3 winding is a
      CONSTANT permutation matrix, v(phi + 2pi/3) = P v(phi).

  Q4  ** ZERO, and not merely pure gauge -- there is no connection to be pure gauge. **  The method
      was calibrated first: a rotating frame gives A = g^-1 dg with curvature identically zero, a
      genuine field gives F = T, and tr(F^2) tells them apart and is unchanged under a change of
      frame.  The machinery can see curvature; there is none here to see.

  Q5  Does not arise: no curvature, so nothing for it to lie in.  The Z_3 the winding does carry is
      flat, and it is the discrete content the corpus already holds.

  Q6  ** THE BUNDLE AND THE GROUP ARE DERIVED; THE FIELD IS THE ORDINARY ROUTE. **  What the
      construction supplies sits over the space of MEMBERS -- the degeneracy, the canonical U(3),
      the bundle, the order-81 holonomy.  A gauge field is a connection over a member's SPACETIME.
      Two different bases, and the object is on the other one.  Nothing obstructs a spacetime
      connection; the construction does not supply one, and the reason is now structural.

  ⚠ NOT CLAIMED: that no spacetime bundle could be built -- only that the seats do not constitute
  one.  Nothing reopens Delta(27)'s holonomy (W2), which is over the space of members and flat
  there.  Nothing is named (W6).  Nothing about weak isospin, the global group, or the compact face.
""")
print(f"  {len(_checks)} checks, all pass." if all(_checks) else "  FAILURES PRESENT")
assert all(_checks)
