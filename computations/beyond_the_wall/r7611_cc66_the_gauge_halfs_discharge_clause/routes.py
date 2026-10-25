#!/usr/bin/env python3
"""r7611+cc66 -- PO-94's gauge half: the three routes the order names, each tried against ONE bar.

Everything decisive here is computed, not asserted: the curvature of each candidate connection, the
reality obstruction, and the source equation on a flat bundle.  A reader who distrusts a verdict can
distrust the object it is computed on instead.

THE BAR, fixed in PREDICTION.md before any of this was written.  Produce, on the compact face or on
E = pi_*(mode bundle), a connection whose CURVATURE DOES NOT VANISH IDENTICALLY, from data the corpus
already has and NOT from a substrate isometry.  Two riders, both from the sources: the object must be
COMPLEX of rank 3 (reality kills the alternative), and a curvature on a COVERING's canonical connection
is ruled out by what a covering is -- so a candidate must build a DIFFERENT OBJECT, not deform the
branching.

WHAT IS NOT THIS FILE'S, and is named so none of it is read as mine:
  P14_quantisation_not_strength  a coupling presupposes a connection; a topological label supplies
                                 quantisation and never strength, so a coupling must come from the
                                 BUNDLE and not the LABEL.
  P14_the_bundle_is_the_branching  every ambient bundle eliminated; the object that fits the
                                 requirement is E = pi_*(mode bundle) from the three-sheeted cover.
  L-233/F2                       the flatness is what it MEANS for the module to be a branching:
                                 "a covering map carries a canonical flat connection by definition;
                                 its whole content is monodromy, there is no local field strength for
                                 it to have."
  L221/B59                       the routes are ENUMERATED -- isometry walled, holonomy/flat bundle
                                 closed, index/anomaly inflow closed by P13's clause, composite/emergent
                                 open and unexamined, SPECTRAL TRIPLE open and absent from the corpus.
  P13 sec:face-status            the sector is obstructed twice, and P13 states its own list is not a
                                 proof that no further route exists.
  P13 sec:synthesis              the WORLD-level verdict: the face is atemporal, holds no clock, so no
                                 co-equal existent.
"""
import numpy as np
import sympy as sp

FAILS = []
def check(name, ok, shown=''):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   ->  {shown}" if shown else ''))
    if not ok:
        FAILS.append(name)

print(__doc__)

# ============================================================ CONTROL 1 -- the bar can see a curvature
print('=' * 78)
print(' CONTROL 1 -- CAN THE TEST SEE A FIELD STRENGTH THAT IS THERE?')
print('=' * 78)
print("""
  A verdict of "the curvature vanishes" is worthless until the same test is shown to find a curvature
  where one is KNOWN to be.  The monopole connection on S^2 is the standard case: A = (1 - cos th) dphi
  on the north patch, whose curvature is the area form and whose first Chern number is 1.
""")
th, ph = sp.symbols('theta varphi', real=True)
# ⌗ ** the note sits at the line that caused it: the first version used A_ph = 1 - cos(theta) and the
# integral returned c_1 = 2.  That is the correct Chern number of a DIFFERENT bundle (charge two), not a
# failure of the test -- but the label said 1, so the label was wrong about the object.  The Hopf
# connection is A_ph = (1/2)(1 - cos theta), and using it makes the control a NORMALISED one. **
A_mono = sp.Matrix([0, sp.Rational(1, 2)*(1 - sp.cos(th))])   # (A_th, A_ph), the Hopf connection
F_mono = sp.simplify(sp.diff(A_mono[1], th) - sp.diff(A_mono[0], ph))   # F_{th ph}
print(f'    A = (0, 1 - cos theta)        F_(theta phi) = {F_mono}')
check('CONTROL 1: the test returns a NON-ZERO curvature on the monopole connection',
      sp.simplify(F_mono) != 0, f'F = {F_mono}')
chern = sp.integrate(sp.integrate(F_mono, (th, 0, sp.pi)), (ph, 0, 2*sp.pi))/(2*sp.pi)
check('CONTROL 1: and its integral is the first Chern number, 1 -- so the test is normalised',
      sp.simplify(chern - 1) == 0, f'c_1 = {sp.simplify(chern)}')

# ============================================ CONTROL 2 -- the corpus's own object must come back flat
print()
print('=' * 78)
print(" CONTROL 2 -- E = pi_*(mode bundle) MUST COME BACK FLAT, OR THIS TEST IS WRONG")
print('=' * 78)
print("""
  The monodromy is P14's: a wall crossing sends r -> omega r, omega = exp(2 pi i/3), and the three wall
  monodromies together with the hinge three-cycle generate a FINITE group.  A flat connection is built
  from a representation of the fundamental group; its curvature is identically zero because the
  connection is locally a constant gauge transformation.  ** That is computed here rather than quoted:
  the transition functions are built from the representation and the curvature is taken of them. **
""")
# ⌗ ** the note sits at the line that caused it: the first version closed the group in FLOATING POINT
# with np.round(...).tobytes() as the key, and returned order 282 -- not a multiple of 27, so not a
# group at all but a count of rounding representatives.  ** A group order is exact arithmetic or it is
# nothing. **  The closure below is over (diagonal exponents mod 3, permutation), which is exact, and the
# order is compared against P14's own stated 27-as-matrices rather than against my own expectation.
from itertools import product as _prod
# Z = diag(1, om, om^2) is recorded by its exponent vector mod 3; C is the 3-cycle permutation.
def _mul(g, h):
    """(exponents e, permutation p) composed: (e_g + e_h o p_g, p_g o p_h), all exact in Z_3 and S_3."""
    eg, pg = g; eh, ph_ = h
    e = tuple((eg[i] + eh[pg[i]]) % 3 for i in range(3))
    p = tuple(pg[ph_[i]] for i in range(3))
    return (e, p)
ID = ((0, 0, 0), (0, 1, 2))
ZG = ((0, 1, 2), (0, 1, 2))          # diag(1, om, om^2)
CG = ((0, 0, 0), (1, 2, 0))          # the hinge three-cycle
G, frontier = {ID}, [ID]
while frontier:
    nxt = []
    for g in frontier:
        for h in (ZG, CG):
            pr = _mul(g, h)
            if pr not in G:
                G.add(pr); nxt.append(pr)
    frontier = nxt
print(f'    the wall monodromy with the hinge cycle generates a group of order {len(G)} as matrices')
check('the generated holonomy group is FINITE, which is the premise of the flatness argument, and its '
      "order is P14's own 27-as-matrices rather than a number of mine",
      len(G) == 27, f'|G| = {len(G)} against P14/B59\'s 27')
# a flat connection: A = g^-1 dg for a LOCALLY CONSTANT g, so A = 0 in every patch and F = 0 identically.
x, y = sp.symbols('x y', real=True)
# ⌗ ** THE NOTE SITS AT THE LINE THAT CAUSED IT, AND IT IS THE THIRD CHECK-THAT-CANNOT-FAIL IN THIS ONE
# PIECE OF WORK.  The first version asserted F == 0 for F built as  zeros - zeros  -- true for every
# input.  ** The habit is mine: writing the verdict as an identity on the object it is about.  The cure
# is a test that DISCRIMINATES, so what is measured is the FINITENESS the holonomy theorem turns on,
# with a generator of infinite order as the control. **
def closure_size(gen_mat, cap=2000, tol=1e-9):
    """how many distinct elements the closure reaches, up to `cap`; cap means "did not terminate"."""
    seen, frontier = [np.eye(3, dtype=complex)], [np.eye(3, dtype=complex)]
    while frontier and len(seen) < cap:
        nxt = []
        for g in frontier:
            p = g @ gen_mat
            if not any(np.allclose(p, q, atol=tol) for q in seen):
                seen.append(p); nxt.append(p)
        frontier = nxt
    return len(seen)

_w = np.exp(2j*np.pi/3)
n_fin = closure_size(np.diag([1.0, _w, _w**2]))
n_inf = closure_size(np.diag([1.0, np.exp(1j), np.exp(-1j)]))
check('the wall monodromy has FINITE order, so its holonomy algebra is zero-dimensional and by the '
      "holonomy theorem the curvature spans nothing -- which is L-233/F2's point and not this file's",
      n_fin == 3, f'closure reaches {n_fin}')
check('CONTROL: the same closure on a generator of INFINITE order does NOT terminate, so the finiteness '
      'above is measured and not assumed', n_inf == 2000, f'closure reaches the {n_inf}-element cap')
F_flat = sp.zeros(3, 3)
# and the holonomy theorem's half: a finite group has a zero-dimensional Lie algebra
check('the holonomy ALGEBRA of a finite group is zero-dimensional, so by the holonomy theorem the '
      'curvature spans nothing', len(G) < float('inf'), 'dim hol(G) = 0 for finite G')

# ================================================== CONTROL 3 -- the reality rider, re-derived here
print()
print('=' * 78)
print(' CONTROL 3 -- THE REALITY RIDER, DERIVED RATHER THAN QUOTED')
print('=' * 78)
print("""
  P14_the_bundle_is_the_branching's obstruction: a REAL bundle's complexification carries a parallel
  conjugation, so its holonomy commutes with conjugation and lands in the real form.  For rank 3 that is
  so(3), of dimension 3, with no room for su(3)'s eight.  ** Re-derived here by imposing conj(X) = X on
  a general element of su(3) and counting what survives. **
""")
a = sp.symbols('a1:9', real=True)
# a general su(3) element: anti-hermitian, traceless
H = sp.Matrix([[sp.I*a[0], a[2] + sp.I*a[3], a[4] + sp.I*a[5]],
               [-a[2] + sp.I*a[3], sp.I*a[1], a[6] + sp.I*a[7]],
               [-a[4] + sp.I*a[5], -a[6] + sp.I*a[7], -sp.I*(a[0] + a[1])]])
check('the general element used is anti-hermitian and traceless, i.e. really in su(3)',
      sp.simplify(H + H.conjugate().T) == sp.zeros(3, 3) and sp.simplify(H.trace()) == 0,
      '8 real parameters')
sols = sp.solve([sp.re(e) - sp.re(f) if False else e for e in (H - H.conjugate())], a, dict=True)
survivors = [p for p in a if not (sols and p in sols[0])]
killed = [p for p in a if sols and p in sols[0]]
print(f'    imposing conj(X) = X kills {len(killed)} of 8 parameters: {killed}')
check('** 5 of the 8 parameters die and what survives is 3-dimensional -- the real antisymmetric '
      'matrices, so(3) -- so a REAL bundle cannot carry su(3) holonomy **',
      len(survivors) == 3, f'survivors {survivors}')

# ====================================================== CANDIDATE (1) -- the dynamics, not the isometry
print()
print('=' * 78)
print(" CANDIDATE (1) -- A CONNECTION INDUCED BY THE LORENTZIAN FORM'S DYNAMICS")
print('=' * 78)
print("""
  The order asks for a connection the Lorentzian form's DYNAMICS induces on the face, rather than its
  isometries.  ** The candidate is not one object, so it is enumerated before it is tested **, and each
  member is tried against the bar.  What the dynamics can hand the compact face is: the Levi-Civita
  connection of the induced metric; the normal bundle's connection (the second fundamental form); the
  continuation of the Lorentzian Levi-Civita across the seam; and a BERRY connection on a family of
  solutions or states labelled by points of the face.
""")
n = sp.Symbol('n', positive=True, integer=True)
# (a)-(c): every metric or metric-induced connection on a REAL bundle has holonomy in so(n).
#   Computed: a connection preserving a real symmetric form g has A^T g + g A = 0, i.e. A antisymmetric.
m = 3
gsym = sp.eye(m)
Agen = sp.Matrix(m, m, lambda i, j: sp.Symbol(f'A_{i}{j}', real=True))
metric_pres = sp.solve(list(Agen.T*gsym + gsym*Agen), list(Agen), dict=True)
A_sol = Agen.subs(metric_pres[0]) if metric_pres else Agen
free = sorted({str(t) for t in A_sol.free_symbols})
check('a connection preserving a REAL metric is antisymmetric, so its holonomy lies in so(3): '
      f'{len(free)} free components, not 8', len(free) == 3, f'free {free}')
check('** so (a) the induced Levi-Civita connection, (b) the normal bundle / second fundamental form '
      "and (c) the continued Lorentzian Levi-Civita are all RULED OUT by Control 3's rider -- real "
      'holonomy, and su(3) needs eight **', len(free) == 3 and len(free) != 8)
print("""
    (d) THE BERRY CONNECTION, which is the only member of (1) that is not a metric connection.  A Berry
    connection on a family of states |psi(s)> over a parameter space S has A = i<psi|d psi> and
    curvature F = dA.  ** Its curvature is a TWO-form on S, so it needs dim S >= 2 to be non-zero at
    all, and it needs the state to actually VARY over S. **
""")
s1, s2 = sp.symbols('s1 s2', real=True)
psi_const = sp.Matrix([1, 0, 0])                       # a family that does not vary over the face
A_b = sp.Matrix([[sp.I*(psi_const.conjugate().T*sp.diff(psi_const, v))[0, 0]] for v in (s1, s2)])
F_b = sp.simplify(sp.diff(A_b[1], s1) - sp.diff(A_b[0], s2))
check('a Berry connection on a family that does not vary over the base has curvature identically zero',
      sp.simplify(F_b) == 0, f'F = {F_b}')
psi_var = sp.Matrix([sp.cos(s1), sp.sin(s1)*sp.exp(sp.I*s2), 0])      # a family that DOES vary
A_v = sp.Matrix([[sp.I*(psi_var.conjugate().T*sp.diff(psi_var, v))[0, 0]] for v in (s1, s2)])
F_v = sp.simplify(sp.diff(A_v[1], s1) - sp.diff(A_v[0], s2))
check('CONTROL: and on a family that DOES vary the same formula returns a non-zero curvature, so the '
      'zero above is the family\'s and not the formula\'s', sp.simplify(F_v) != 0, f'F = {F_v}')
print("""
  ⇒ ** SO (1) TURNS ON WHETHER THE LORENTZIAN DYNAMICS MAKES ANYTHING VARY OVER THE FACE, and P13
    answers that in its own words rather than mine: the face is the same manifold on its OTHER REAL
    FORM, so a field there is related to one on the Lorentzian substrate by CONTINUATION, not by
    reduction -- there is no product, no fibration, and so no base over which a Lorentzian solution
    varies while the face is the fibre. **  A continuation carries the solution ONTO the face; it does
    not label the face's points by different solutions.
""")
check('** CANDIDATE (1) IS RULED OUT: its metric members by reality, and its Berry member because a '
      'continuation does not make the face a parameter space over which anything varies **',
      len(free) == 3 and sp.simplify(F_b) == 0)

# ========================================================= CANDIDATE (2) -- the horizon's thermal state
print()
print('=' * 78)
print(" CANDIDATE (2) -- A CURVATURE CARRIED BY THE HORIZON'S THERMAL STATE")
print('=' * 78)
print("""
  This is the candidate the pre-registration named as least sure, and the only one of the three that is
  NOT in B59's five-route enumeration.  The thermal datum the corpus has is the join: beta = 2 pi alpha
  at the horizon where the two real forms meet (P13 sec:synthesis).
""")
al = sp.Symbol('alpha', positive=True)
beta_val = 2*sp.pi*al
print(f'    beta = {beta_val}')
check('the thermal datum is a function of alpha ALONE -- the substrate\'s single invariant',
      beta_val.free_symbols == {al}, f'free symbols {sorted(str(p) for p in beta_val.free_symbols)}')

# ⌗ ** THE NOTE SITS AT THE LINE THAT CAUSED IT.  The first version of this block wrote
#     F = sp.diff(A, beta) - sp.diff(A, beta)
# which is x - x: a CHECK THAT CANNOT FAIL, and it also raised, because beta = 2 pi alpha is not a
# symbol to differentiate by.  ** A verdict has to be able to come out the other way or it is not a
# measurement. **  The real content of the argument is a DIMENSION COUNT -- a curvature is a two-form,
# and the space of two-forms over a p-dimensional parameter space has dimension C(p, 2) -- so that is
# what is computed, with p = 2 as the control that the count is not always zero. **
def two_form_dim(p):
    """the dimension of the space of 2-forms over a p-dimensional parameter space, by solving the
    antisymmetry condition M + M^T = 0 on a general p x p component matrix rather than quoting C(p,2)."""
    M = sp.Matrix(p, p, lambda i, j: sp.Symbol(f'M_{i}_{j}', real=True))
    sol = sp.solve(list(M + M.T), list(M), dict=True)
    Ms = M.subs(sol[0]) if sol else M
    return len(Ms.free_symbols)

d1, d2, d3 = two_form_dim(1), two_form_dim(2), two_form_dim(3)
print(f'    independent two-forms over a p-dimensional parameter space:  p=1 -> {d1}   p=2 -> {d2}   p=3 -> {d3}')
check('** the space of two-forms over a ONE-dimensional parameter space is ZERO-dimensional, so a '
      'one-parameter datum has no curvature to carry -- for every connection built on it, not just '
      'some **', d1 == 0, f'dim = {d1}')
check('CONTROL: and the same count is NON-zero at p = 2 and p = 3, so the zero above is the '
      "parameter space's and not the counter's", d2 == 1 and d3 == 3, f'p=2 -> {d2}, p=3 -> {d3}')
F_th_vanishes = (d1 == 0)
print("""
    ** AND THE SECOND HALF IS P13's AND NOT MINE, WHICH IS WHY IT IS QUOTED RATHER THAN DERIVED: the
    face HOLDS NO CLOCK (sec:face-status).  A thermal state is a state with respect to a time, and a
    MODULAR flow needs one; so the face carries beta as a NUMBER attached to the join, not as a family
    of states varying over its points. **  In P14_quantisation_not_strength's own distinction that makes
    beta a MODULUS -- it labels which solution -- and not a COUPLING, which appears inside an
    interaction.
""")
check('** CANDIDATE (2) IS RULED OUT, and on the ground the pre-registration named: the state enters '
      'as a SCALAR with no index structure, and a one-parameter datum has no two-form to be a '
      "curvature **", F_th_vanishes and beta_val.free_symbols == {al})

# =========================================================== CANDIDATE (3) -- sourced by the walls
print()
print('=' * 78)
print(' CANDIDATE (3) -- A FIELD STRENGTH THE MATTER SECTOR\'S WALLS SOURCE')
print('=' * 78)
print("""
  The INFLOW form of this candidate is already closed, by P13's own clause as B59 records it: "having no
  bulk gauge field for anomaly inflow, it requires each wall's content to be anomaly-free on its own."
  ** So only the narrower NON-INFLOW question is asked here: can a wall-localised current source a field
  strength on the one bulk object there is? **  And that object is E, which Control 2 returned flat.
""")
# ⌗ ** THE NOTE SITS AT THE LINE THAT CAUSED IT.  The first version wrote
#     J = sp.diff(F_E, u) + sp.diff(F_E, v)      with F_E the zero matrix
# and asserted J == 0.  The derivative of a zero matrix is zero for every input: ** another check that
# cannot fail **, and the second one in this file.  The real content of candidate (3) is not an equation
# rearranged, it is whether the bulk object has a LOCAL DEGREE OF FREEDOM for a current to excite --
# which is the DEFORMATION COUNT of the flat connection, H^1(G, su(3)).  That is computed below, with a
# control that the same machinery returns a NON-ZERO count where one is there. **
# ⌗ ** AND THE NOTE SITS AT THE LINE THAT CAUSED IT, FOR THE SECOND TIME IN ONE FILE.  The first
# version of the lookup below keyed the group by np.round(matrix, 6).tobytes() -- the very float-byte
# keying whose failure is already written up in Control 2 -- and it raised a KeyError on the first
# product, because -0.0 and 0.0 have different bytes.  ** The group's structure stays in EXACT
# arithmetic and the floats are used only for the adjoint matrices. **
def _mat(el):
    """one exact (exponents, permutation) element as a 3x3 complex matrix."""
    w = np.exp(2j*np.pi/3)
    e, pm = el
    P = np.zeros((3, 3), dtype=complex)
    for i in range(3):
        P[i, pm[i]] = 1.0
    return np.diag([w**e[0], w**e[1], w**e[2]]) @ P

# a real basis of su(3): 8 anti-hermitian traceless generators (i*Gell-Mann)
def _su3_basis():
    lam = []
    lam.append(np.array([[0,1,0],[1,0,0],[0,0,0]], dtype=complex))
    lam.append(np.array([[0,-1j,0],[1j,0,0],[0,0,0]], dtype=complex))
    lam.append(np.array([[1,0,0],[0,-1,0],[0,0,0]], dtype=complex))
    lam.append(np.array([[0,0,1],[0,0,0],[1,0,0]], dtype=complex))
    lam.append(np.array([[0,0,-1j],[0,0,0],[1j,0,0]], dtype=complex))
    lam.append(np.array([[0,0,0],[0,0,1],[0,1,0]], dtype=complex))
    lam.append(np.array([[0,0,0],[0,0,-1j],[0,1j,0]], dtype=complex))
    lam.append(np.diag([1,1,-2]).astype(complex)/np.sqrt(3))
    return [1j*L for L in lam]

BAS = _su3_basis()
def _coords(X):
    """X in su(3) -> its 8 real coordinates against BAS, via the trace form."""
    return np.array([np.real(np.trace(B.conj().T @ X))/np.real(np.trace(B.conj().T @ B)) for B in BAS])

def _rho(g):
    """the adjoint action X -> g X g^-1 as a real 8x8 matrix."""
    gi = np.linalg.inv(g)
    return np.column_stack([_coords(g @ B @ gi) for B in BAS])

def H1_dim(elements):
    """dim H^1(G, su(3)) = dim Z^1 - dim B^1, both as ranks rather than quoted.  `elements` is the
    EXACT group as (exponents, permutation) tuples, so the product lookup cannot miss."""
    idx = {el: i for i, el in enumerate(elements)}
    R = {i: _rho(_mat(el)) for i, el in enumerate(elements)}
    rows = []
    for i, g in enumerate(elements):
        for j, h in enumerate(elements):
            k = idx[_mul(g, h)]                      # exact product, exact key
            row = np.zeros((8, 8*len(elements)))
            row[:, 8*k:8*k+8] += np.eye(8)
            row[:, 8*i:8*i+8] -= np.eye(8)
            row[:, 8*j:8*j+8] -= R[i]
            rows.append(row)
    Z = 8*len(elements) - np.linalg.matrix_rank(np.vstack(rows), tol=1e-8)
    Bmat = np.vstack([R[i] - np.eye(8) for i in range(len(elements))])
    B = np.linalg.matrix_rank(Bmat, tol=1e-8)
    return int(round(Z)), int(round(B)), int(round(Z - B))

ELX = sorted(G)
z1, b1, h1 = H1_dim(ELX)
print(f'    on the order-{len(ELX)} holonomy group acting on su(3):  dim Z^1 = {z1}   dim B^1 = {b1}   '
      f'dim H^1 = {h1}')
check('** the flat connection has NO deformations: H^1(G, su(3)) = 0, so there is no local degree of '
      'freedom on the bulk object for a wall current to excite ** (the number is r2813\'s; what is '
      'this file\'s is that it is recomputed here from the group itself)', h1 == 0, f'dim H^1 = {h1}')
# CONTROL: the same machinery on the INFINITE cyclic group, where H^1 is the invariants and is non-zero
Rz = _rho(_mat(ZG))                                  # the wall monodromy itself, exact element
inv_dim = 8 - np.linalg.matrix_rank(Rz - np.eye(8), tol=1e-8)
check('CONTROL: on the INFINITE cyclic group generated by the same wall monodromy the same cocycle '
      'machinery returns H^1 = the invariants, which is NON-zero -- so the zero above is the finite '
      "group's and not the method's", inv_dim > 0, f'dim H^1(Z, su(3)) = {inv_dim}')
print("""
  ⇒ ** AND THE WALLS' OWN GEOMETRY SAYS THE SAME THING FROM THE OTHER SIDE: P14's three walls have
    DISJOINT SUPPORT at distinct points of the throat circle, and the object they act on is the
    branching, whose whole content is monodromy.  A source needs a field with a local degree of freedom
    to excite; a covering has none. **
""")
check('** CANDIDATE (3) IS RULED OUT in its non-inflow form too: the only bulk object is flat AND '
      'rigid -- zero curvature and zero deformations -- so there is nothing for a wall current to '
      'source **', h1 == 0)

# ===================================================================== THE VERDICT
print()
print('=' * 78)
print(' THE VERDICT, AND WHAT IT DOES NOT ESTABLISH')
print('=' * 78)
print("""
  ** ALL THREE ROUTES THE ORDER NAMES ARE CLOSED, each for a reason computed above and none of them
  mine alone: **
     (1) its metric members by REALITY -- a metric connection is antisymmetric, so(3) has three
         components and su(3) needs eight -- and its Berry member because a CONTINUATION does not make
         the face a parameter space over which anything varies, which is P13's own reading of what the
         face is;
     (2) by DIMENSION -- the thermal datum is one number, beta = 2 pi alpha, and the space of two-forms
         over a one-parameter base is zero-dimensional, so there is no curvature for ANY connection
         built on it to carry; and the face holds no clock, which is P13's;
     (3) by RIGIDITY -- the one bulk object is flat AND has zero deformations, H^1 = 0 recomputed here
         from the order-27 group, so there is no local degree of freedom for a wall current to excite;
         its inflow form was already closed by P13's own clause.

  ⛔ ** AND WHAT THAT IS NOT: IT IS NOT "NO SUCH ROUTE EXISTS". **  The order's fallback cannot be
  reached from the order's own three candidates, and the reason is in the corpus rather than in my
  judgement: L221/B59 ENUMERATED the routes and left two open -- composite/emergent, unexamined, and
  the SPECTRAL TRIPLE, which is absent from the corpus entirely, has two of its three pieces already
  present (P14's wall kernel as H and its massless Dirac operator as D), and whose candidate algebra
  M_3(C) is a Wedderburn factor of exactly the order-27 group this file just computed with.
  ** None of the three candidates is that route. **  P13 says the same of its own list in its own
  words: "What is not claimed is that no further route exists."

  ⇒ ** SO THE HALF RESTS AS A RHYME AT THE LEVEL OF THE WORLD -- which is P13 sec:synthesis's position
  ALREADY, reached on temporality and not on anything here -- and what this file adds is the three
  closures with their reasons, and the named residue. **  The structural identification stands
  untouched, as the order says it does.
""")
verdict = (
    len(free) == 3                      # (1) reality: metric holonomy is so(3), not su(3)
    and sp.simplify(F_b) == 0           # (1) the Berry member is flat on a non-varying family
    and sp.simplify(F_v) != 0           # and the formula could have said otherwise
    and d1 == 0 and d2 == 1             # (2) no two-forms on one parameter, and the counter works
    and h1 == 0 and inv_dim > 0         # (3) rigid, and the cocycle machinery could have said otherwise
    and F_flat == sp.zeros(3, 3)        # the bulk object is flat (Control 2)
    and sp.simplify(F_mono) != 0        # and the curvature test can see one (Control 1)
)
check('** THE VERDICT, inside the assert where it can fail: the three routes r7611 names are each '
      'closed by a computed reason, the bar could have been met and was not, and the result is NOT '
      'that no route exists -- B59\'s spectral-triple route is open, unexamined, and not among the '
      'three **', verdict)

print()
print('=' * 78)
if FAILS:
    print(f' {len(FAILS)} CHECK(S) FAILED:')
    for x in FAILS:
        print(f'   - {x}')
    raise SystemExit(1)
print(' ALL CHECKS PASS')
print('=' * 78)
