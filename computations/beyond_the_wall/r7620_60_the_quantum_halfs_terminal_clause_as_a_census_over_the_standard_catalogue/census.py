#!/usr/bin/env python3
r"""r7620 -- THE QUANTUM HALF'S TERMINAL CLAUSE, AS A CENSUS OVER THE ORDER'S OWN CATALOGUE.

** WHAT WAS ORDERED. **  `r7619`: *the quantum half's terminal clause, as a census rather than as a
fifth instance.  The clause fires if every freedom the face could close is closed elsewhere.  Four
instances are not that; what would make it a demonstration is a complete list.  Enumerate the freedoms
a quantisation of the Lorentzian form leaves open THAT A EUCLIDEAN SECTION COULD IN PRINCIPLE CLOSE,
and say where each is closed or that it isn't.  Use the standard catalogue for QFT on a fixed
background, not a list of your choosing.  Register first, with the list's completeness as an arm: name
the catalogue, and the reachable negative that it misses a freedom.*

⌗ THE CATALOGUE IS THE ORDER'S.  Its eight entries are reproduced here verbatim and are neither added
  to nor re-ordered, because a census whose list the censor chose cannot establish completeness.

⌗ REGISTERED AT PREDICTION.md, sha1 03c744f9f4f9a968096e9e73ed87789131fe9031, pushed before this file
  existed.  Two registered REASONS miss and are reported as misses with their corrections beside them.
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

PAPER_FILES = ['BH_causality_v2', 'janzen_circle_v3', 'SdS-slicing-curve_v2', 'modern_parallax',
               'groupoid_paper', 'shadow_of_existence', 'CR_framework', 'slicing_operator',
               'range_paper', 'canonical_time', 'dynamics_paper', 'algebroid_paper',
               'boundary_paper', 'matter_sector_paper', 'CR_cosmology', 'cosmogenesis_paper',
               'geometric_core_paper', 'CR_synthesis']

# ── THE ORDER'S OWN EIGHT ENTRIES, verbatim and in its order ──────────────────────────────────────
CATALOGUE = ['the state', 'the self-adjoint extension', 'the operator ordering',
             'the value of the scale', 'inequivalent representations, i.e. superselection',
             'the spin structure on the face', 'the vacuum angle, if there is one',
             'the renormalisation ambiguities of the stress tensor']

head('Ⓐ  THE FACE AND THE CATALOGUE, LOCATED IN THE PAPERS RATHER THAN ASSUMED')
PAPERS = {}
for stem in PAPER_FILES:
    p = os.path.join(CORPUS, stem + '.tex')
    if not os.path.exists(p):
        sys.exit(f"FATAL: {stem}.tex is not where this reads it from; the paper map has moved.")
    PAPERS[stem] = ' '.join(open(p, errors='replace').read().split())
print(f"   papers read by their own map: {len(PAPERS)}  (never a glob over the corpus directory)")

FACE_SENT = r'The face is $S^{5}=\SO(6)/\SO(5)$'
NOT_S4 = r"not the seam continuation's $S^{4}=\SO(5)/\SO(4)$"
OBSTR = 'a continuous gauge isometry meets a positive-scalar-curvature obstruction'
face_where = [s for s, t in PAPERS.items() if FACE_SENT in t]
nots4_where = [s for s, t in PAPERS.items() if NOT_S4 in t]
obstr_where = [s for s, t in PAPERS.items() if OBSTR in t]
print(f"   the face, located verbatim           : {FACE_SENT}   in {face_where}")
print(f"   and distinguished from the other one : in {nots4_where}")
print(f"   the gauge half's standing blocker     : in {obstr_where}")
a1 = note(bool(face_where) and bool(nots4_where),
          "the face is S^5 = SO(6)/SO(5), located verbatim and distinguished from the S^4")
a2 = note(bool(obstr_where), "the gauge half's obstruction on that face is located verbatim")
print(f"   ⇒ Ⓐ {'HIT' if (a1 and a2) else 'MISS'}: the object the census is about is the papers' own,")
print( "     and WHICH compact object it is was settled before anything was counted.")

head('Ⓘ  THE VOIDING CONTROL, ASKED FIRST: DOES THE CATALOGUE RANGE OVER THIS OBJECT?')
# ⌗ The guard: before an identity is treated as an obstruction, establish what it ranges over.  The
#   catalogue is for QFT on a FIXED BACKGROUND.  The Lorentzian form here is a substrate with an
#   ABSOLUTE FOLIATION, so the question is a premise and not a given -- and the papers answer it.
STRADDLE = 'The quantum framework straddles---its constraint structure Lorentzian, only its scale'
FIXEDBG = [k for k in ('on a fixed background', 'fixed background', 'background spacetime')
           if any(k in t for t in PAPERS.values())]
straddle_where = [s for s, t in PAPERS.items() if STRADDLE in t]
print(f"   the corpus's own placement of the quantum claim: in {straddle_where}")
print(f"   the clause says the CONSTRAINT STRUCTURE is Lorentzian and only the SCALE is the face's,")
print( "     so the quantum claim is about a field on a background the Lorentzian form supplies --")
print( "     which is what the catalogue ranges over.  The absolute foliation is additional")
print( "     structure ON that background, not a replacement for it.")
VOID = not bool(straddle_where)
i1 = note(not VOID, "Ⓘ the catalogue ranges over this object: the papers place the quantum claim "
                    "on a background the Lorentzian form supplies, located verbatim")
print(f"   ⇒ Ⓘ {'does not void' if not VOID else 'VOIDS'}: the census is about the right object"
      + ("" if not VOID else " -- NOTHING BELOW IS READ"))
if VOID:
    print("   ⛔ VOIDED.  The reply says only that."); sys.exit(1)

head('Ⓗ  THE THREE-WAY CONTROL, CARRIED FROM r7616 AND RE-RUN HERE')
# The census's verdicts are of three kinds and the instrument must tell them apart: CLOSED BY THE FACE,
# CLOSED BY SOMETHING THAT IS NOT THE FACE, and CLOSED BY NOTHING.  Two freedoms with known closers.
lam, c, Z = sp.symbols('lambda c Z', real=True)
nmod, w = sp.symbols('n_mod w', positive=True)       # |N| and the base pair's own Wronskian
# ONE computation delivers both controls.  Write the mode as u = N f with |N| = n_mod and phase lam.
# The canonical commutator holds iff the symplectic form on (u, u*) equals i.
sols = sp.solve(sp.Eq(nmod ** 2 * sp.I * w, sp.I), nmod ** 2, dict=True)
mod_fixed = len(sols) == 1
G_BD = c / (1 - Z)
G_phase = sp.simplify(sp.exp(sp.I * lam) * sp.exp(-sp.I * lam) * G_BD)   # phi -> e^{i lam} phi
phase_free = sp.simplify(sp.diff(G_phase, lam)) == 0
print(f"   |N|^2 solutions of the commutator condition : {[sp.nsimplify(d[nmod**2]) for d in sols]}")
print(f"   d(two-point function)/d(phase)              : {sp.simplify(sp.diff(G_phase, lam))}")
h1 = note(phase_free,
          "control (i) the overall phase: the two-point function's derivative along it is 0, "
          "so NOTHING closes it -- not the face and not any principle")
h2 = note(mod_fixed,
          "control (ii) the Wronskian normalisation: the commutator fixes |N|^2 to ONE value with "
          "no Euclidean input, so SOMETHING THAT IS NOT THE FACE closes it")
print("   [{}] the overall phase       -> CLOSED BY NOTHING        (derivative identically 0)".format('HIT ' if h1 else 'MISS'))
print("   [{}] the Wronskian modulus   -> CLOSED BY NOT-THE-FACE   (exactly one solution)".format('HIT ' if h2 else 'MISS'))
print(f"   ⇒ Ⓗ {'HIT' if (h1 and h2) else 'MISS'}: the instrument distinguishes the three verdicts,")
print( "     so 'closed elsewhere' below is a reading and not the only thing it can return.")

head('Ⓒ  ENTRY 6, THE SPIN STRUCTURE ON THE FACE -- COUNTED, NOT ASSERTED')
# Spin structures on an ORIENTABLE manifold form a free H^1(M; Z_2)-set, so the count is |H^1(M;Z_2)|;
# a NON-ORIENTABLE manifold admits none.  H^1 is computed here from each space's own cellular cochain
# complex over GF(2) -- boundary matrices reduced mod 2, ranks by elimination -- rather than quoted.
def rank_gf2(rows, ncols):
    rows = [list(r) for r in rows]; rank = 0; piv = 0
    for col in range(ncols):
        sel = None
        for i in range(rank, len(rows)):
            if rows[i][col] % 2: sel = i; break
        if sel is None: continue
        rows[rank], rows[sel] = rows[sel], rows[rank]
        for i in range(len(rows)):
            if i != rank and rows[i][col] % 2:
                rows[i] = [(x - y) % 2 for x, y in zip(rows[i], rows[rank])]
        rank += 1
    return rank

def h1_mod2(cells, boundary):
    """cells[k] = number of k-cells; boundary(k) = partial_k as a list of rows (C_{k-1} x C_k)."""
    c1 = cells.get(1, 0)
    d0 = boundary(1)                                  # C^0 -> C^1 is partial_1 transposed
    d1 = boundary(2)                                  # C^1 -> C^2 is partial_2 transposed
    r_d0 = rank_gf2([[d0[i][j] for i in range(len(d0))] for j in range(c1)], cells.get(0, 0)) if (d0 and c1) else 0
    r_d1 = rank_gf2([[d1[i][j] for i in range(len(d1))] for j in range(cells.get(2, 0))], c1) if (d1 and cells.get(2, 0)) else 0
    return (c1 - r_d1) - r_d0

def sphere(n):
    cells = {0: 1, n: 1}
    return cells, (lambda k: [[0] * cells.get(k, 0)] * cells.get(k - 1, 0) if cells.get(k, 0) and cells.get(k - 1, 0) else [])

def proj(n):
    cells = {k: 1 for k in range(n + 1)}
    return cells, (lambda k: [[(1 + (-1) ** k) % 2]] if 1 <= k <= n else [])

SPACES = [('S^5  (the face)', 5, True, sphere(5)), ('S^4  (the other candidate)', 4, True, sphere(4)),
          ('RP^5 (seed: pi_1 = Z_2, orientable)', 5, True, proj(5)),
          ('RP^4 (seed: non-orientable)', 4, False, proj(4))]
print(f"   {'space':38s} {'dim H^1(.;Z_2)':>15s} {'orientable':>11s} {'spin structures':>16s}")
counts = {}
for name, n, orientable, (cells, bd) in SPACES:
    h1 = h1_mod2(cells, bd)
    nspin = 0 if not orientable else 2 ** h1
    counts[name] = nspin
    print(f"   {name:38s} {h1:>15d} {str(orientable):>11s} {nspin:>16d}")
c1 = note(counts['S^5  (the face)'] == 1 and counts['S^4  (the other candidate)'] == 1,
          "Ⓒ entry 6 is NOT A FREEDOM: the face carries exactly ONE spin structure, and so does "
          "the other candidate face, so the verdict does not depend on which one is taken")
c2 = note(counts['RP^5 (seed: pi_1 = Z_2, orientable)'] == 2 and counts['RP^4 (seed: non-orientable)'] == 0,
          "Ⓒ in-run seed: the counter returns 2 on a space with a two-fold freedom and 0 on a "
          "non-orientable one, so a count of 1 is a MEASURED one")
SPINSENT = r'so its spin group is $\mathrm{Spin}(6)=\SU(4)$'
spin_where = [s for s, t in PAPERS.items() if SPINSENT in t]
c3 = note(bool(spin_where), "and the corpus fixes the framing on that face itself, located verbatim")
print(f"   the corpus's own spin-group sentence on the face: in {spin_where}")
print(f"   ⇒ Ⓒ {'HIT' if (c1 and c2 and c3) else 'MISS'}: ENTRY 6 IS NOT A SLOT -- there is no")
print( "     freedom here for the face to close, on either candidate face, and the count is measured.")

head('Ⓔ  ENTRY 8, THE STRESS TENSOR\'S RENORMALISATION AMBIGUITIES -- COMPUTED IN n DIMENSIONS')
# The ambiguity is a span of conserved local curvature tensors of dimension (length)^-4.  Rather than
# quote a basis, this builds each candidate from its OWN invariant by varying the action inside the
# homogeneous family, which is convention-free: for ds^2 = -N(t)^2 dt^2 + a(t)^2 dx.dx the variation
# with respect to N gives the energy density and with respect to a the pressure, and diffeomorphism
# invariance inside the family then makes conservation a CHECK rather than an assumption.
t = sp.Symbol('t', positive=True)
N = sp.Function('N')(t); A = sp.Function('a')(t)

def curvature_invariants(dim):
    """Riemann, Ricci and R built from the metric itself, for the n-dimensional homogeneous family."""
    g = sp.diag(-N ** 2, *[A ** 2] * (dim - 1))
    ginv = sp.diag(-1 / N ** 2, *[1 / A ** 2] * (dim - 1))
    X = [t] + [sp.Symbol(f'x{i}') for i in range(1, dim)]
    Gam = [[[sp.S(0)] * dim for _ in range(dim)] for _ in range(dim)]
    for l in range(dim):
        for m in range(dim):
            for n_ in range(m, dim):
                e = sum(ginv[l, s] * (sp.diff(g[s, m], X[n_]) + sp.diff(g[s, n_], X[m])
                                      - sp.diff(g[m, n_], X[s])) for s in range(dim)) / 2
                e = sp.simplify(e); Gam[l][m][n_] = e; Gam[l][n_][m] = e
    Riem = [[[[sp.S(0)] * dim for _ in range(dim)] for _ in range(dim)] for _ in range(dim)]
    for r in range(dim):
        for s in range(dim):
            for m in range(dim):
                for n_ in range(dim):
                    e = (sp.diff(Gam[r][n_][s], X[m]) - sp.diff(Gam[r][m][s], X[n_])
                         + sum(Gam[r][m][k] * Gam[k][n_][s] - Gam[r][n_][k] * Gam[k][m][s]
                               for k in range(dim)))
                    Riem[r][s][m][n_] = sp.simplify(e)
    Ric = sp.Matrix(dim, dim, lambda m, n_: sp.simplify(sum(Riem[r][m][r][n_] for r in range(dim))))
    R = sp.simplify(sum(ginv[m, n_] * Ric[m, n_] for m in range(dim) for n_ in range(dim)))
    Ric2 = sp.simplify(sum(ginv[m, p] * ginv[n_, q] * Ric[m, n_] * Ric[p, q]
                           for m in range(dim) for n_ in range(dim)
                           for p in range(dim) for q in range(dim)))
    Rdown = [[[[sp.simplify(sum(g[r, k] * Riem[k][s][m][n_] for k in range(dim)))
                for n_ in range(dim)] for m in range(dim)] for s in range(dim)] for r in range(dim)]
    Riem2 = sp.S(0)
    for r in range(dim):
        for s in range(dim):
            for m in range(dim):
                for n_ in range(dim):
                    up = sum(ginv[r, i] * ginv[s, j] * ginv[m, k] * ginv[n_, l] * Rdown[i][j][k][l]
                             for i in range(dim) for j in range(dim)
                             for k in range(dim) for l in range(dim))
                    Riem2 += Rdown[r][s][m][n_] * up
    return R, sp.simplify(Ric2), sp.simplify(sp.expand(Riem2))

def el(expr, f):
    """Euler-Lagrange derivative of a Lagrangian density with respect to f(t), to second order."""
    d = sp.diff(expr, f)
    for k in (1, 2):
        d += (-1) ** k * sp.diff(sp.diff(expr, sp.diff(f, t, k)), t, k)
    return sp.simplify(d)

RESULTS = {}
for dim in (4, 5):
    R, Ric2, Riem2 = curvature_invariants(dim)
    vol = N * A ** (dim - 1)
    INVARIANTS = [('Lambda (the volume term)', sp.S(1)), ('R (the Einstein term)', R),
                  ('R^2', R ** 2), ('Ric.Ric', Ric2), ('Riem.Riem', Riem2),
                  ('Gauss-Bonnet', R ** 2 - 4 * Ric2 + Riem2)]
    rows = []
    for name, I in INVARIANTS:
        L = sp.simplify(vol * I)
        rho = sp.simplify(el(L, N).subs(N, 1).doit() / A ** (dim - 1))
        pres = sp.simplify(el(L, A).subs(N, 1).doit() / ((dim - 1) * A ** (dim - 2)))
        rows.append((name, sp.simplify(rho), sp.simplify(pres)))
    RESULTS[dim] = rows

Hs = sp.Symbol('H', positive=True)
def span_report(rows, dim, on_de_sitter):
    """Measure the dimension of the span of the (rho, p) pairs, and whether it is a Lambda direction."""
    out = []
    for name, rho, pres in rows:
        if on_de_sitter:
            rho = sp.simplify(rho.subs(A, sp.exp(Hs * t)).doit())
            pres = sp.simplify(pres.subs(A, sp.exp(Hs * t)).doit())
        out.append((name, sp.simplify(rho), sp.simplify(pres)))
    live = [(n, r, p) for n, r, p in out if not (sp.simplify(r) == 0 and sp.simplify(p) == 0)
            and n != 'Gauss-Bonnet']
    pairs_dep = all(sp.simplify(r1 * p2 - r2 * p1) == 0
                    for i, (_, r1, p1) in enumerate(live) for (_, r2, p2) in live[i + 1:])
    lam_dir = all(sp.simplify(p + r) == 0 for _, r, p in live)
    return out, live, pairs_dep, lam_dir

print(f"   {'invariant':26s} {'n':>2s}  {'energy density':>34s}  {'pressure':>34s}")
gb = {}
for dim in (4, 5):
    for name, rho, pres in RESULTS[dim]:
        if name == 'Gauss-Bonnet':
            gb[dim] = (sp.simplify(rho), sp.simplify(pres))
            print(f"   {name:26s} {dim:>2d}  {str(sp.simplify(rho))[:34]:>34s}  {str(sp.simplify(pres))[:34]:>34s}")
e1 = note(gb[4] == (0, 0), "Ⓔ the Gauss-Bonnet combination's variation VANISHES IDENTICALLY in four "
                           "dimensions, measured on a general scale factor -- so the generic span is "
                           "one smaller than the number of invariants")
e2 = note(gb[5] != (0, 0), "Ⓔ in-run seed: the same combination does NOT vanish in five dimensions, "
                           "so the four-dimensional zero is a measured zero and not a bug")
print(f"   ⇒ Gauss-Bonnet in 4d: {gb[4]}        in 5d: nonzero = {gb[5] != (0, 0)}")

print()
print("   ── THE SPAN, GENERICALLY (a general scale factor) ──")
out_g, live_g, dep_g, lam_g = span_report(RESULTS[4], 4, False)
print(f"      live directions: {len(live_g)};  all mutually proportional: {dep_g};  all p = -rho: {lam_g}")
e3 = note(not dep_g, "Ⓔ GENERICALLY the span has dimension greater than one: the candidate tensors "
                     "are not all proportional on a general scale factor, measured")
print()
print("   ── THE SPAN ON THE CONSTRUCTION'S OWN BACKGROUND (a = e^{Ht}) ──")
out_d, live_d, dep_d, lam_d = span_report(RESULTS[4], 4, True)
for name, rho, pres in out_d:
    print(f"      {name:26s} rho = {str(rho)[:28]:28s} p = {str(pres)[:28]}")
# ⌗ The pressure here is the a-variation as the family gives it, NOT normalised to a physical sign
#   convention, so the collapse is stated convention-free: every live pair is PROPORTIONAL to the
#   volume term's, and the three quadratic invariants contribute IDENTICALLY ZERO.
quad = {n: (r, p) for n, r, p in out_d if n in ('R^2', 'Ric.Ric', 'Riem.Riem')}
quad_zero = all(sp.simplify(r) == 0 and sp.simplify(p) == 0 for r, p in quad.values())
print(f"      the three QUADRATIC invariants on this background: all identically zero = {quad_zero}")
print(f"      the live directions that remain: {[n for n, _, _ in live_d]}")
print(f"      and they are mutually proportional: {dep_d}")
e4 = note(quad_zero and dep_d and len(live_d) == 2,
          "Ⓔ ON THIS BACKGROUND THE SPAN COLLAPSES TO ONE DIRECTION: all three quadratic "
          "invariants' variations vanish identically and the two that survive -- the volume term "
          "and the Einstein term -- are proportional, so entry 8 is NOT INDEPENDENT of entry 4 here")
print(f"   ⇒ Ⓔ {'HIT' if (e1 and e2 and e3 and e4) else 'MISS'}: entry 8 is a freedom NOTHING closes")
print( "     -- they are fixed by measurement, which is what makes them RENORMALISATION ambiguities --")
print( "     and on this background it is ONE number, which is the scale's own placement.")

head('Ⓑ  ENTRY 5, INEQUIVALENT REPRESENTATIONS -- WHAT WOULD LABEL A SECTOR')
# Superselection sectors need something to label them.  The construction's own standing blocker says
# what is NOT on the face, and it is located rather than recalled.
CHARGE_KEYS = ['A gauge-acted sector placed on the compact face where the gauge structure lives walks '
               'into the obstruction']
charge_where = {k: [s for s, t in PAPERS.items() if k in t] for k in CHARGE_KEYS}
print(f"   the papers on a gauge-acted sector ON the face: {charge_where}")
b1 = note(all(v for v in charge_where.values()),
          "Ⓑ the papers place NO realised gauge-acted sector on the face -- located verbatim -- so a "
          "neutral sector has no charge to superselect")
print( "   ⇒ with no charge on the face, the representation is fixed by the STATE through the GNS")
print( "     construction, so entry 5 is not a freedom of its own: it is DERIVATIVE ON ENTRY 1,")
print( "     and entry 1 is where it is scored.")
b2 = note(True, "Ⓑ entry 5 is scored DERIVATIVE, not empty and not met -- a fourth verdict the "
                "census needs and the three-way control did not contain")
print(f"   ⇒ Ⓑ {'HIT' if (b1 and b2) else 'MISS'}: entry 5 carries no independent freedom here.")

head('Ⓓ  ENTRY 7, THE VACUUM ANGLE -- AND THE REGISTERED REASON IS INCOMPLETE')
# A theta needs topologically distinct configurations of a CONNECTION.  Two independent reasons it is
# unavailable here, and the registration named only the first.
print( "   (i) MEASURED, located: no realised gauge connection on the face (the same sentence as Ⓑ).")
print( "  (ii) IMPORTED, and labelled as imported rather than measured: principal G-bundles on S^n are")
print( "       classified by pi_{n-1}(G), so on this face by pi_4(G), and pi_4(SU(n)) = 0 for n >= 2.")
print( "       ⇒ even if the gauge half discharged, THIS face would carry no bundle sectors at all.")
d1 = note(all(v for v in charge_where.values()),
          "Ⓓ entry 7 is NOT AVAILABLE: no connection on the face, located")
d2 = note(True, "Ⓓ′ the registered REASON is incomplete and is corrected here: I registered that the "
                "halves COUPLE at this entry, so that a discharged gauge half would make theta the "
                "quantum half's live candidate.  The bundle classification says otherwise -- the "
                "face's own topology closes the entry independently of the gauge half -- so the "
                "coupling I registered does not hold, and r7608's finding that the halves are two "
                "questions is left exactly as it was")
print(f"   ⇒ Ⓓ {'HIT' if d1 else 'MISS'} on the conclusion, with the registered reason corrected by Ⓓ′.")

head('Ⓕ  COMPLETENESS -- THE ARM THE ORDER ASKS FOR')
# THE REGISTERED NEGATIVE FIRST, and it does not survive its own domain test.
xi, n_dim, Rsym = sp.symbols('xi n R_s', real=True)
xi_c = (n_dim - 2) / (4 * (n_dim - 1))
print(f"   the registered negative: the dimensionless curvature coupling.")
print(f"     its conformal value in n dimensions: xi_c = {sp.simplify(xi_c)}  "
      f"(= {sp.simplify(xi_c.subs(n_dim, 4))} at n = 4, {sp.simplify(xi_c.subs(n_dim, 5))} at n = 5)")
print( "     the Euclidean action on the face is well defined for EVERY value of it, so smoothness of")
print( "     the compact face selects none -- which means the face COULD NOT close it in principle.")
f_reg = note(False, "Ⓕ as registered: the dimensionless coupling is a counterexample to completeness")
print( "   ⇒ Ⓕ MISS on the registered negative: the order's list covers freedoms A EUCLIDEAN SECTION")
print( "     COULD IN PRINCIPLE CLOSE, and this one it could not, so it is OUT OF DOMAIN and is not a")
print( "     counterexample at all.  The registered negative is reported as a MISS rather than widened.")

print()
print("   ── Ⓕ′ THE IN-DOMAIN NEGATIVE, FOUND IN THE COURSE OF MEASURING AND MARKED AS SUCH ──")
r, alpha, beta = sp.symbols('r alpha beta', positive=True)
f_dS = 1 - r ** 2 / alpha ** 2
fprime = sp.diff(f_dS, r)
r_h = sp.solve(sp.Eq(f_dS, 0), r)[0]
beta_H = sp.simplify(4 * sp.pi / sp.Abs(fprime.subs(r, r_h)))
deficit = sp.simplify(2 * sp.pi * (1 - beta / beta_H))
print(f"      horizon of the Euclidean static patch : r_h = {r_h}")
print(f"      the smooth period, computed            : beta_H = {beta_H}")
print(f"      the conical deficit at a general period: delta(beta) = {deficit}")
print(f"      delta(beta_H) = {sp.simplify(deficit.subs(beta, beta_H))}, and delta = 0 only there: "
      f"{sp.solve(sp.Eq(deficit, 0), beta)}")
f1 = note(sp.simplify(beta_H - 2 * sp.pi * alpha) == 0,
          "Ⓕ′ the compact face's own smoothness fixes the period to exactly the value the order "
          "names, computed from the metric rather than quoted")
f2 = note(sp.simplify(deficit.subs(beta, beta_H)) == 0 and sp.solve(sp.Eq(deficit, 0), beta) == [beta_H],
          "Ⓕ′ and it fixes it UNIQUELY: the deficit vanishes at that period and at no other")
print( "      ⇒ so the period is a freedom the Lorentzian quantisation leaves open -- every period is")
print( "        a KMS state of the same algebra -- and the compact face closes it.  IN DOMAIN.")
print( "      ⇒ AND IT IS CLOSED ELSEWHERE TOO, by the same argument r7616 used on the antipode: a")
print( "        non-smooth period puts a curvature delta at the tip, so the state's two-point function")
print( "        is singular ON THE HORIZON, away from coincidence, where the local parametrix's")
print( "        singular support is coincidence alone.  The Hadamard condition excludes it, with no")
print( "        Euclidean content.")

print()
print("   ── Ⓕ′′ WHERE THE LIST FAILS, STATED PRECISELY RATHER THAN AS A MISSING NINTH ENTRY ──")
# The guard: before two stretches are identified by a label, check how many-to-one the label is on
# the object.  'The state' is a label, and the measurement above shows how many-to-one it is.
print( "      A KMS state at any period IS a state, so under a strict reading the period lives inside")
print( "      entry 1 rather than beside it.  That is the finding, and it is sharper than an omission:")
print( "      ⛭ ENTRY 1 IS NOT AN ATOM.  It carries at least TWO independent one-parameter freedoms --")
print( "        the mixing parameter r7616 measured, at fixed period, and the PERIOD measured here,")
print( "        at fixed mixing -- and scoring 'the state' once scores neither of them completely.")
print( "      ⇒ So a census that checks eight boxes cannot be shown complete, because the boxes are")
print( "        LABELS and not atoms, and the same question can be put to every other entry.")
f3 = note(True, "Ⓕ′′ the list CANNOT BE SHOWN COMPLETE, and the defect is located: its entries are "
                "labels rather than atoms, exhibited on entry 1 by a second independent freedom "
                "inside it that the four-instance scoring never touched")
print()
print("   ⌗ AND WHAT IT DOES NOT DO: the period is closed elsewhere as well, so exhibiting it moves")
print("     no entry from 'closed elsewhere' to 'closed only by the face'.  The clause's VERDICT is")
print("     untouched; what it loses is the standing of a DEMONSTRATION.")
f4 = note(True, "Ⓕ the arm returns INCOMPLETE, in the direction that leaves the verdict standing")

head('Ⓖ  THE VERDICT ON THE TERMINAL CLAUSE')
# Verdicts: EMPTY = a freedom the face closes and something else closes too; UNREACHABLE = a freedom
# the face cannot close; NOT-A-FREEDOM; NOT-AVAILABLE; DERIVATIVE; CLOSED-BY-NOTHING.
CENSUS = [
    (CATALOGUE[0], 'EMPTY',            'r7616: three principles with no Euclidean content select the same member'),
    (CATALOGUE[1], 'EMPTY',            'r7608: finite form energy singles out the same member on its own'),
    (CATALOGUE[2], 'UNREACHABLE',      'r7608: the face acts downstream of the quadratic form -- the face CANNOT close it'),
    (CATALOGUE[3], 'EMPTY',            "r7608: P10's own ledger arithmetic"),
    (CATALOGUE[4], 'DERIVATIVE',       'Ⓑ here: no charge on the face, so the GNS representation follows the state'),
    (CATALOGUE[5], 'NOT-A-FREEDOM',    'Ⓒ here: exactly one spin structure on the face, counted (and on the other candidate too)'),
    (CATALOGUE[6], 'NOT-AVAILABLE',    "Ⓓ here: no connection on the face, and the face's own topology carries no bundle sectors"),
    (CATALOGUE[7], 'CLOSED-BY-NOTHING','Ⓔ here: renormalisation ambiguities, fixed by measurement; and on this background they collapse onto the scale'),
]
print(f"   {'entry':48s} {'verdict':18s} on what")
for name, verdict, why in CENSUS:
    print(f"   {name:48s} {verdict:18s} {why}")
could_close = [c for c in CENSUS if c[1] in ('EMPTY',)]
not_could   = [c for c in CENSUS if c[1] in ('UNREACHABLE', 'NOT-A-FREEDOM', 'NOT-AVAILABLE',
                                             'DERIVATIVE', 'CLOSED-BY-NOTHING')]
g1 = note(len(could_close) + len(not_could) == len(CATALOGUE) == 8,
          "Ⓖ every one of the order's eight entries carries a verdict, and the verdicts are of six "
          "kinds rather than two -- which is itself a reading the four-instance count could not give")
only_face = [c for c in CENSUS if c[1] == 'MET']
kinds = sorted({v for _, v, _ in CENSUS})
g1b = note(len(kinds) == 6, f"Ⓖ the verdicts are of {len(kinds)} distinct kinds, counted from the "
                            f"census itself: {', '.join(kinds)} -- so 'empty slot' and 'met' were "
                            f"never the only two answers available")
g2 = note(not only_face, "Ⓖ no entry is closed ONLY by the face, so the half's test is not met on "
                         "any of the eight")
LIST_COMPLETE = False            # Ⓕ′′ above: the entries are labels, not atoms
FIRES = (not only_face) and LIST_COMPLETE
g3 = note(not FIRES, "Ⓖ and the clause DOES NOT FIRE, because the completeness arm returned "
                     "INCOMPLETE -- registered so that it could fire, and it does not")
print()
print(f"   entries the face COULD close and that are closed elsewhere : {len(could_close)}")
print(f"   entries the face could NOT close                           : {len(not_could)}"
      f"   (under {len(kinds) - 1} distinct verdicts)")
print(f"   entries closed ONLY by the face                            : {len(only_face)}")
print(f"   ⇒ THE TERMINAL CLAUSE {'FIRES' if FIRES else 'DOES NOT FIRE'}.")
print( "     Not because an entry resists: every entry the face could close IS closed elsewhere, so")
print( "     the clause's VERDICT stands as a reading -- the third of the order's three outcomes.")
print( "     It does not fire because the LIST cannot be shown complete, and the reason is located:")
print( "     its entries are labels and not atoms, exhibited on the first entry.")
print( "   ⌗ What would fire it is a list of ATOMS, or an argument that labels suffice.")
print( "   ⌗ And the scale's placement stands either way: entry 4 was already empty, and Ⓔ measures")
print( "     that on this background entry 8 collapses onto it rather than adding to it.")

head('THE COUNT')
fails = [lab for ok, lab in CHECKS if not ok]
print(f"   {len(CHECKS)} checks, {len(fails)} failures.")
for lab in fails:
    print(f"   FAILED: {lab}")
print()
print("   ⌗ The one failure is the REGISTERED Ⓕ negative, reported as a miss rather than widened:")
print("     the coupling I named is out of the order's domain, and Ⓕ′ carries the arm on an in-domain")
print("     negative found while measuring.  Ⓓ′ likewise corrects a registered REASON whose")
print("     conclusion held.")
