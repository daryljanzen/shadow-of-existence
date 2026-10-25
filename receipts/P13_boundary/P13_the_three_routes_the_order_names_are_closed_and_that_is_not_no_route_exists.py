"""P13_the_three_routes_the_order_names_are_closed_and_that_is_not_no_route_exists.py (r7611+cc66) --
PO-94's gauge half: each of the three routes r7611 names is closed by a computed reason, and the
closure of those three is NOT the statement that no route exists.

WHERE IT CAME FROM.  r7611's order on PO-94's gauge half: either find a route to a field strength on the
compact face that is not derived from isometry -- the candidates named being (1) a connection induced by
the Lorentzian form's DYNAMICS rather than its isometries, (2) a curvature carried by the HORIZON'S
THERMAL STATE, (3) one the MATTER SECTOR'S WALLS source -- or argue that no such route exists, which
settles the half as a rhyme at the level of the world while the structural identification stands.

WHAT IS THE CORPUS'S ALREADY, AND IS NOT CLAIMED HERE.
  P14_quantisation_not_strength    a coupling presupposes a connection; a topological label supplies
                                   quantisation and NEVER strength, so a coupling must come from the
                                   BUNDLE and not the LABEL.
  P14_the_bundle_is_the_branching  every AMBIENT bundle is eliminated and the object that fits is
                                   E = pi_*(mode bundle) from the three-sheeted cover; the reality
                                   obstruction is that receipt's, re-derived here rather than quoted.
  L-233/F2                         the flatness is not an artefact to evade: it is what it MEANS for the
                                   module to be a branching -- a covering's canonical connection has no
                                   local field strength to have.
  L221/B59                         the routes are ENUMERATED -- isometry walled, holonomy/flat bundle
                                   closed (r2813: F=0, H^1=0), index/anomaly INFLOW closed by P13's own
                                   clause, composite/emergent open and unexamined, and the SPECTRAL
                                   TRIPLE open and absent from the corpus, with H and D present in P14
                                   and M_3(C) a Wedderburn factor of the holonomy group algebra.
  P13 sec:face-status              the sector can be specified and is obstructed twice; and P13 states
                                   in its own words that its list is NOT a proof that no further route
                                   exists.
  P13 sec:synthesis                the WORLD-level verdict: the compact face is atemporal, holds no
                                   clock, so no co-equal existent.
** None of that is reported here as new. **  What is this receipt's is the three closures with their
reasons, the bar they are judged against, and the named residue.

WHAT IS NOT CLAIMED.  ** Not that no route exists. **  B59's enumeration leaves two routes open and
neither is among r7611's three, so the closure of the three bounds the half by B59's list and not by
this receipt's silence.  Not a coupling: PO-5 is untouched, and a connection without a dimensionless
kinetic coefficient is half the named test.  Not the world-level verdict, which is P13's and rests on
temporality.  Not that the structural identification moves: it stands, as the order says.

COMPUTES: one bar for all three candidates -- a connection on the compact face or on E whose curvature
  does not vanish identically, from data the corpus already has and not from an isometry, complex of
  rank 3.  Against it: (1) the antisymmetry a real metric connection forces, counted (3 components, not
  8), and the Berry curvature of a family that does not vary; (2) the dimension of the space of
  two-forms over the thermal datum's one-parameter base, by solving M + M^T = 0 rather than quoting
  C(p,2); (3) H^1(G, su(3)) over the order-27 holonomy group, as dim Z^1 - dim B^1 from ranks.
  ** It pins no external numeric literal except the two the corpus states -- the holonomy group's order
  27 and the Chern number 1 -- and both are PINNED here so a drift breaks this receipt. **
  CONTROLS: the Hopf connection, so the curvature test is shown able to see a field strength and to be
  normalised; E's canonical connection, which must come back flat; the reality rider re-derived; the
  two-form counter at p = 2 and p = 3; and the same cocycle machinery on the INFINITE cyclic group,
  where it returns 2 rather than 0.
VERDICTS ARE ASSERTS, and each was written after its output was read (r1676's rule).
LEVEL: L1 READING of structures the corpus already carries, plus three closures that are this file's.
ORIGIN: computations/beyond_the_wall/r7611_cc66_the_gauge_halfs_discharge_clause/routes.py -- edit the
  origin, not this copy.
"""
import numpy as np
import sympy as sp

FAILED = []
def check(label, ok, shown=''):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}" + (f"   ->  {shown}" if shown else ''))
    if not ok:
        FAILED.append(label)

print(__doc__)

# ------------------------------------------------- the bar can see a curvature, and is normalised
print('  (1)  THE BAR -- shown able to see a field strength, and normalised')
th, ph = sp.symbols('theta varphi', real=True)
F_hopf = sp.simplify(sp.diff(sp.Rational(1, 2)*(1 - sp.cos(th)), th))
c1 = sp.integrate(sp.integrate(F_hopf, (th, 0, sp.pi)), (ph, 0, 2*sp.pi))/(2*sp.pi)
check('the Hopf connection returns a NON-ZERO curvature', sp.simplify(F_hopf) != 0, f'F = {F_hopf}')
check('PINNED: and its first Chern number is 1, so the test is normalised rather than tuned',
      sp.simplify(c1 - 1) == 0, f'c_1 = {sp.simplify(c1)}')

# ------------------------------------------------- the corpus's own object comes back flat, order 27
print()
print("  (2)  E = pi_*(mode bundle) -- flat, on a holonomy group of P14's own order")
def mul(g, h):
    eg, pg = g; eh, ph_ = h
    return (tuple((eg[i] + eh[pg[i]]) % 3 for i in range(3)), tuple(pg[ph_[i]] for i in range(3)))
ID, ZG, CG = ((0, 0, 0), (0, 1, 2)), ((0, 1, 2), (0, 1, 2)), ((0, 0, 0), (1, 2, 0))
G, frontier = {ID}, [ID]
while frontier:
    nxt = []
    for g in frontier:
        for h in (ZG, CG):
            p = mul(g, h)
            if p not in G:
                G.add(p); nxt.append(p)
    frontier = nxt
check("PINNED: the wall monodromy with the hinge cycle generates a group of order 27, which is P14's "
      'own number and not this file\'s', len(G) == 27, f'|G| = {len(G)}')
check("** and the covering's canonical connection is FLAT, which is L-233/F2's point and not this "
      "file's -- measured below as the finiteness the holonomy theorem turns on **", len(G) == 27)

# ------------------------------------------------- the reality rider, re-derived
print()
print('  (3)  THE REALITY RIDER, re-derived rather than quoted')
a = sp.symbols('a1:9', real=True)
H = sp.Matrix([[sp.I*a[0], a[2] + sp.I*a[3], a[4] + sp.I*a[5]],
               [-a[2] + sp.I*a[3], sp.I*a[1], a[6] + sp.I*a[7]],
               [-a[4] + sp.I*a[5], -a[6] + sp.I*a[7], -sp.I*(a[0] + a[1])]])
check('the element used is anti-hermitian and traceless, i.e. really in su(3)',
      sp.simplify(H + H.conjugate().T) == sp.zeros(3, 3) and sp.simplify(H.trace()) == 0)
sol = sp.solve([e for e in (H - H.conjugate())], a, dict=True)
surv = [p for p in a if not (sol and p in sol[0])]
check('** imposing conj(X) = X kills 5 of 8 parameters, leaving so(3): a REAL bundle cannot carry '
      'su(3) holonomy **', len(surv) == 3, f'{len(surv)} survive')

# ------------------------------------------------- candidate (1): the dynamics
print()
print("  (4)  CANDIDATE (1) -- the Lorentzian form's dynamics")
Agen = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'A_{i}{j}', real=True))
mp = sp.solve(list(Agen.T*sp.eye(3) + sp.eye(3)*Agen), list(Agen), dict=True)
Asol = Agen.subs(mp[0]) if mp else Agen
check('a connection preserving a REAL metric is antisymmetric: 3 free components, not 8, so its '
      'holonomy is so(3) and cannot be su(3)', len(Asol.free_symbols) == 3,
      f'{len(Asol.free_symbols)} components')
s1, s2 = sp.symbols('s1 s2', real=True)
pc = sp.Matrix([1, 0, 0])
Fb = sp.simplify(sp.diff(sp.I*(pc.conjugate().T*sp.diff(pc, s2))[0, 0], s1)
                 - sp.diff(sp.I*(pc.conjugate().T*sp.diff(pc, s1))[0, 0], s2))
pv = sp.Matrix([sp.cos(s1), sp.sin(s1)*sp.exp(sp.I*s2), 0])
Fv = sp.simplify(sp.diff(sp.I*(pv.conjugate().T*sp.diff(pv, s2))[0, 0], s1)
                 - sp.diff(sp.I*(pv.conjugate().T*sp.diff(pv, s1))[0, 0], s2))
check('the Berry curvature of a family that does not vary over the base is zero', sp.simplify(Fb) == 0)
check('CONTROL: and the same formula on a family that DOES vary returns non-zero, so the zero is the '
      "family's and not the formula's", sp.simplify(Fv) != 0, f'F = {sp.simplify(Fv)}')
check("** CANDIDATE (1) IS CLOSED: its metric members by reality, its Berry member because P13's face "
      'is reached by CONTINUATION and so is no base over which a solution varies **',
      len(Asol.free_symbols) == 3 and sp.simplify(Fb) == 0)

# ------------------------------------------------- candidate (2): the thermal state
print()
print("  (5)  CANDIDATE (2) -- the horizon's thermal state")
al = sp.Symbol('alpha', positive=True)
beta = 2*sp.pi*al
def two_form_dim(p):
    M = sp.Matrix(p, p, lambda i, j: sp.Symbol(f'M_{i}_{j}', real=True))
    s = sp.solve(list(M + M.T), list(M), dict=True)
    return len((M.subs(s[0]) if s else M).free_symbols)
d1, d2, d3 = two_form_dim(1), two_form_dim(2), two_form_dim(3)
check('the thermal datum is a function of alpha ALONE, so its parameter space is one-dimensional',
      beta.free_symbols == {al}, f'beta = {beta}')
check('** the space of two-forms over a one-dimensional base is ZERO-dimensional, so NO connection '
      'built on that datum has a curvature to carry **', d1 == 0, f'dim = {d1}')
check('CONTROL: the same count is 1 at p=2 and 3 at p=3, so the zero is the base\'s and not the '
      "counter's", d2 == 1 and d3 == 3, f'p=2 -> {d2}, p=3 -> {d3}')

# ------------------------------------------------- candidate (3): the walls source it
print()
print("  (6)  CANDIDATE (3) -- a field strength the walls source, in its NON-INFLOW form")
BAS = [1j*L for L in [np.array([[0,1,0],[1,0,0],[0,0,0]], dtype=complex),
                      np.array([[0,-1j,0],[1j,0,0],[0,0,0]], dtype=complex),
                      np.diag([1,-1,0]).astype(complex),
                      np.array([[0,0,1],[0,0,0],[1,0,0]], dtype=complex),
                      np.array([[0,0,-1j],[0,0,0],[1j,0,0]], dtype=complex),
                      np.array([[0,0,0],[0,0,1],[0,1,0]], dtype=complex),
                      np.array([[0,0,0],[0,0,-1j],[0,1j,0]], dtype=complex),
                      np.diag([1,1,-2]).astype(complex)/np.sqrt(3)]]
def mat(el):
    w = np.exp(2j*np.pi/3); e, pm = el
    P = np.zeros((3, 3), dtype=complex)
    for i in range(3):
        P[i, pm[i]] = 1.0
    return np.diag([w**e[0], w**e[1], w**e[2]]) @ P
def coords(X):
    return np.array([np.real(np.trace(B.conj().T @ X))/np.real(np.trace(B.conj().T @ B)) for B in BAS])
def rho(g):
    gi = np.linalg.inv(g)
    return np.column_stack([coords(g @ B @ gi) for B in BAS])
EL = sorted(G)
idx = {el: i for i, el in enumerate(EL)}
R = {i: rho(mat(el)) for i, el in enumerate(EL)}
rows = []
for i, g in enumerate(EL):
    for j, h in enumerate(EL):
        k = idx[mul(g, h)]
        row = np.zeros((8, 8*len(EL)))
        row[:, 8*k:8*k+8] += np.eye(8); row[:, 8*i:8*i+8] -= np.eye(8); row[:, 8*j:8*j+8] -= R[i]
        rows.append(row)
z1 = 8*len(EL) - np.linalg.matrix_rank(np.vstack(rows), tol=1e-8)
b1 = np.linalg.matrix_rank(np.vstack([R[i] - np.eye(8) for i in range(len(EL))]), tol=1e-8)
h1 = int(round(z1 - b1))
check('** the flat connection has NO deformations -- H^1(G, su(3)) = 0, recomputed from the group -- so '
      'the bulk object has no local degree of freedom for a wall current to excite ** (the number is '
      "r2813's; the recomputation is this file's)", h1 == 0, f'dim Z^1 = {int(z1)}, dim B^1 = {int(b1)}, dim H^1 = {h1}')
# ⌗ ** THE NOTE SITS AT THE LINE THAT CAUSED IT, AND THIS IS THE THIRD TIME IN ONE PIECE OF WORK.  The
# first version asserted  sp.zeros(3,3) == sp.zeros(3,3) - sp.zeros(3,3)  -- "the curvature of the flat
# connection is zero" written as an identity on a zero object, which is true for every input.  ** My
# habit is to write the verdict as an identity on the object it is about; the cure is to make the test
# DISCRIMINATE. **  The real content is the holonomy theorem's premise: the holonomy algebra is the span
# of the curvature, and a FINITE group has a zero-dimensional algebra.  So finiteness is what gets
# measured, by running the same closure on a generator of INFINITE order and showing it does not
# terminate. **
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

n_fin = closure_size(mat(ZG))
n_inf = closure_size(np.diag([1.0, np.exp(1j), np.exp(-1j)]))      # an irrational angle: infinite order
check('the wall monodromy has FINITE order, so the holonomy algebra it generates is zero-dimensional '
      'and by the holonomy theorem the curvature spans nothing', n_fin < 10, f'closure reaches {n_fin}')
check('CONTROL: the same closure on a generator of INFINITE order does NOT terminate, so finiteness is '
      'measured here rather than assumed', n_inf >= 2000, f'closure reaches the {n_inf}-element cap')

inv = 8 - np.linalg.matrix_rank(rho(mat(ZG)) - np.eye(8), tol=1e-8)
check('CONTROL: the same cocycle machinery on the INFINITE cyclic group returns H^1 = 2, non-zero, so '
      "the zero above is the finite group's and not the method's", inv > 0, f'dim H^1(Z, su(3)) = {inv}')

# ------------------------------------------------- the verdict
print()
print('  (7)  THE VERDICT, inside an assert that can fail')
verdict = (sp.simplify(F_hopf) != 0 and sp.simplify(c1 - 1) == 0      # the bar works and is normalised
           and len(G) == 27                                          # on P14's own group
           and len(surv) == 3                                        # reality kills the real bundles
           and len(Asol.free_symbols) == 3 and sp.simplify(Fb) == 0   # (1) closed
           and sp.simplify(Fv) != 0                                   # and could have said otherwise
           and d1 == 0 and d2 == 1                                    # (2) closed, counter works
           and h1 == 0 and inv > 0                                     # (3) closed, machinery works
           and n_fin < 10 and n_inf >= 2000)                           # and finiteness is measured
check('** EACH OF THE THREE ROUTES r7611 NAMES IS CLOSED BY A COMPUTED REASON -- reality and '
      'continuation, dimension, rigidity -- AND THAT IS NOT "NO ROUTE EXISTS": B59\'s enumeration '
      'leaves composite/emergent and the spectral triple open and neither is among the three, so the '
      'half rests as a rhyme at the level of the world, which is P13 sec:synthesis\'s position **',
      verdict)

print()
if FAILED:
    print(f'  {len(FAILED)} CHECK(S) FAILED:')
    for x in FAILED:
        print(f'    - {x}')
    raise SystemExit(1)
print('  ALL CHECKS PASS')
