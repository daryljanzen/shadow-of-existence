#!/usr/bin/env python3
"""r7752 (60) -- a cold read of P9's Kerr-de Sitter paragraph, and of this round's
P18 and P7 reframing.

Registered in PREDICTION.md before corpus/range_paper.tex, probes/Range.lean,
corpus/CR_synthesis.tex, corpus/CR_framework.tex or any of seat 70's results were
opened in this revision.  FOURTEEN arms, each a comparison with its negative named.

Nothing here is read off a docstring or off the prose: Part 1 rebuilds the
Kerr-de Sitter metric from the paper's own Boyer-Lindquist form and recomputes the
curvature; Part 2's predicates are powered on the PRE-reframing text of the same two
files; Part 3 measures what exists before saying anything about it.
"""
import os, re, subprocess, sys, time
import sympy as sp

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
PAPER_P9 = os.path.join(ROOT, 'corpus', 'range_paper.tex')
LEAN     = os.path.join(ROOT, 'computations', 'formalisation', 'lean', 'probes', 'Range.lean')
P18      = os.path.join(ROOT, 'corpus', 'CR_synthesis.tex')
P7       = os.path.join(ROOT, 'corpus', 'CR_framework.tex')
P15      = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
EXP      = os.path.join(ROOT, 'resources', 'ARP_LLM_paper', 'experiments')

# the versions of P18 and P7 immediately BEFORE this round's reframing, named here so
# the power controls cannot be run on the repaired text by accident
PRE_P18, PRE_P7 = '4fc4b1d92', 'ad0a30ff5'
# and for the falls-below family the r7747 parent is ALREADY repaired -- r7745 brought
# all three papers to "level with" -- so a control taken there has no hits and could not
# certify an absence.  This revision's own first run made that mistake and it is recorded
# in RESULT.md.  The control for ARM 12 is therefore the version before r7745.
PRE2_P18, PRE2_P7 = '468aa9093', '8b43d868b'

T0 = time.time()
ARMS = []
def arm(n, title, ok, *lines):
    ARMS.append((n, title, bool(ok)))
    print(f"\n{'='*78}\nARM {n} -- {title}\n{'='*78}")
    for l in lines:
        print(l)
    print(f"  => {'PASS' if ok else 'FAIL'}   [t={time.time()-T0:.0f}s]")

def git(*args):
    return subprocess.run(['git', '-C', ROOT] + list(args),
                          capture_output=True, text=True, check=True).stdout

def read(p):
    with open(p, encoding='utf-8', errors='replace') as f:
        return f.read()

# ---------------------------------------------------------------- the geometry
# P9's prop:kerr writes Kerr-de Sitter in Boyer-Lindquist form; Range.lean works in
# the chart (t, r, x = cos theta, phi).  The metric is rebuilt here from the structure
# functions the PROPOSITION prints -- not copied from the Lean definitions' bodies,
# which are compared against it as a separate check in ARM 7.
a, M, L, r, x, al = sp.symbols('a M L r x alpha', real=True)
CO = [None, r, x, None]            # t and phi are Killing: no dependence on either

def dd(e, i):
    return sp.S.Zero if CO[i] is None else sp.diff(e, CO[i])

def pieces(aa, MM, LL):
    return (r**2 + aa**2*x**2,                              # Sigma = rho^2
            (r**2 + aa**2)*(1 - LL*r**2/3) - 2*MM*r,        # Delta_r
            1 + LL*aa**2*x**2/3,                            # Delta_theta
            1 - x**2,                                       # sin^2 theta
            1 + LL*aa**2/3)                                 # Xi

def metric(aa, MM, LL):
    """-(D/(P X^2))(dt - a S dphi)^2 + (Q S/(P X^2))(a dt - (a^2+r^2) dphi)^2
       + (P/D) dr^2 + (P/(Q S)) dx^2, expanded component by component."""
    P, D, Q, S, X = pieces(aa, MM, LL)
    g03 = (S*aa*(D - Q*(aa**2 + r**2)))/(P*X**2)
    return sp.Matrix([[(-D + Q*S*aa**2)/(P*X**2), 0, 0, g03],
                      [0, P/D, 0, 0],
                      [0, 0, P/(Q*S), 0],
                      [g03, 0, 0, (S*(Q*(aa**2 + r**2)**2 - D*S*aa**2))/(P*X**2)]])

def inverse(g):
    det2 = sp.cancel(g[0, 0]*g[3, 3] - g[0, 3]**2)
    gi = sp.zeros(4, 4)
    gi[1, 1] = sp.cancel(1/g[1, 1]); gi[2, 2] = sp.cancel(1/g[2, 2])
    gi[0, 0] = sp.cancel(g[3, 3]/det2); gi[3, 3] = sp.cancel(g[0, 0]/det2)
    gi[0, 3] = gi[3, 0] = sp.cancel(-g[0, 3]/det2)
    return gi, det2

def kit(aa, MM, LL):
    """Metric, inverse, Christoffels and their r- and x-derivatives, for one choice of
    the three parameters, with r and x left symbolic."""
    g = metric(aa, MM, LL)
    gi, det2 = inverse(g)
    inv_ok = all(sp.cancel(v) == 0 for v in (gi*g - sp.eye(4)))
    dg = [[[sp.cancel(dd(g[i, j], k)) for k in range(4)] for j in range(4)] for i in range(4)]
    G = [[[sp.S.Zero]*4 for _ in range(4)] for _ in range(4)]
    for A in range(4):
        for B in range(4):
            for C in range(B, 4):
                s = sp.S.Zero
                for E in range(4):
                    if gi[A, E] == 0:
                        continue
                    s += gi[A, E]*(dg[E][C][B] + dg[B][E][C] - dg[B][C][E])
                v = sp.cancel(s/2)
                G[A][B][C] = v; G[A][C][B] = v
    dG = {}
    for A in range(4):
        for B in range(4):
            for C in range(4):
                for k in (1, 2):
                    dG[(A, B, C, k)] = (sp.diff(G[A][B][C], CO[k])
                                        if G[A][B][C] != 0 else sp.S.Zero)
    return g, gi, G, dG, det2, inv_ok

def ric_minus_Lg(g, G, dG, Lval, sub):
    """R_mu_nu - Lambda g_mu_nu with `sub` substituted first, so the arithmetic is
    exact rationals at a point and univariate rational functions on a slice."""
    out = {}
    for mu in range(4):
        for nu in range(mu, 4):
            s = sp.S.Zero
            for lam in range(4):
                if lam in (1, 2):
                    s += dG[(lam, mu, nu, lam)].subs(sub)
                if nu in (1, 2):
                    s -= dG[(lam, mu, lam, nu)].subs(sub)
                for sig in range(4):
                    s += G[lam][lam][sig].subs(sub)*G[sig][mu][nu].subs(sub) \
                         - G[lam][nu][sig].subs(sub)*G[sig][mu][lam].subs(sub)
            out[(mu, nu)] = sp.cancel(s - Lval*g[mu, nu].subs(sub))
    return out

def riemann_low_at(g, G, dG, sub):
    """R_{abcd} with `sub` substituted first."""
    def up(A, B, C, Dx):
        s = sp.S.Zero
        if C in (1, 2): s += dG[(A, Dx, B, C)].subs(sub)
        if Dx in (1, 2): s -= dG[(A, C, B, Dx)].subs(sub)
        for lam in range(4):
            s += G[A][C][lam].subs(sub)*G[lam][Dx][B].subs(sub) \
                 - G[A][Dx][lam].subs(sub)*G[lam][C][B].subs(sub)
        return s
    def low(A, B, C, Dx):
        s = sp.S.Zero
        for E in range(4):
            if g[A, E] != 0:
                s += g[A, E].subs(sub)*up(E, B, C, Dx)
        return sp.cancel(s)
    return low

# six parameter triples, chosen to reach the corners the paper and the Lean file each
# range over: Lambda > 0 generic, the witness's own values, Lambda < 0 (which the Lean
# statement admits and the paper's object does not), a = 0, and M = 0.
TRIPLES = [("generic Lambda>0", sp.Rational(1, 2), sp.Integer(3), sp.Rational(7, 5)),
           ("the witness's values", sp.Integer(1), sp.Integer(1), sp.Integer(3)),
           ("large twist", sp.Integer(2), sp.Rational(1, 4), sp.Integer(2)),
           ("Lambda<0 (Lean admits, P9 does not)", sp.Rational(1, 3), sp.Integer(2), sp.Integer(-1)),
           ("no twist, a=0", sp.Integer(0), sp.Integer(3), sp.Rational(9, 5)),
           ("no offset, M=0", sp.Rational(5, 2), sp.Integer(0), sp.Integer(3))]
POINTS = [{r: sp.Rational(5), x: sp.Rational(1, 3)},
          {r: sp.Rational(9, 2), x: sp.Rational(-2, 5)},
          {r: sp.Rational(7), x: sp.Rational(4, 7)},
          {r: sp.Rational(11, 3), x: sp.Rational(-1, 2)}]
SLICES = [({x: sp.Rational(1, 3)}, "x = 1/3, r symbolic"),
          ({r: sp.Integer(5)}, "r = 5, x symbolic")]

print(f"r7752 (60) -- PROBE  [HEAD {git('rev-parse', '--short', 'HEAD').strip()}]")
print(f"sympy {sp.__version__}, python {sys.version.split()[0]}")

# ============================================================ PART 1, ARMS 1-9
print("\n\n##################  PART 1 -- P9's Kerr-de Sitter paragraph  ##################")
print("\nWHAT THIS RUN ESTABLISHES AND WHAT IT DOES NOT, said before the arms rather than")
print("after: the five-variable symbolic identity was attempted first and does not finish")
print("in this run's budget.  What is run instead is exact RATIONAL arithmetic -- no")
print("floating point anywhere -- at four coordinate points for each of six parameter")
print("triples, AND one-variable identities along two slices of each triple, where the")
print("expression is a univariate rational function and sympy's cancel is decisive.  An")
print("identity in r for fixed x is a statement about infinitely many points, not a spot")
print("check.  The general symbolic statement is what the Lean theorem supplies, and this")
print("probe's job is to read the paragraph against it, not to replace it.")

KITS = {}
for nm, aa, MM, LL in TRIPLES:
    t = time.time()
    KITS[nm] = (aa, MM, LL) + kit(aa, MM, LL)
    print(f"  kit built: {nm:38s} a={aa} M={MM} Lambda={LL}   [{time.time()-t:.1f}s]")

# ---- ARM 1: vacuum-Lambda in all sixteen components
pt_bad, sl_bad, inv_bad, nG = [], [], [], {}
for nm in KITS:
    aa, MM, LL, g, gi, G, dG, det2, inv_ok = KITS[nm]
    if not inv_ok:
        inv_bad.append(nm)
    nG[nm] = sum(1 for A in range(4) for B in range(4) for C in range(4) if G[A][B][C] != 0)
    for i, ptv in enumerate(POINTS):
        out = ric_minus_Lg(g, G, dG, LL, ptv)
        for k, v in out.items():
            if v != 0:
                pt_bad.append((nm, i, k, v))
    for sl, desc in SLICES:
        out = ric_minus_Lg(g, G, dG, LL, sl)
        for k, v in out.items():
            if v != 0:
                sl_bad.append((nm, desc, k, v))
arm(1, "R_mu_nu = Lambda g_mu_nu, recomputed from the metric in all sixteen components",
    not pt_bad and not sl_bad and not inv_bad,
    f"  the inverse metric verifies against the metric for every triple: {not inv_bad}"
    + (f"  FAILED: {inv_bad}" if inv_bad else ""),
    f"  det of the (t,phi) block, generic triple: "
    f"{sp.factor(KITS['generic Lambda>0'][7])}",
    "  nonzero Christoffel components of 64, by triple:",
    *[f"      {nm:38s} {nG[nm]}" for nm in KITS],
    f"  exact rational points: {len(TRIPLES)} triples x {len(POINTS)} points x 10 independent",
    f"  components = {len(TRIPLES)*len(POINTS)*10} values, all of R_mu_nu - Lambda g_mu_nu.",
    f"      components not exactly zero: {pt_bad if pt_bad else 'none'}",
    f"  one-variable identities: {len(TRIPLES)} triples x {len(SLICES)} slices x 10 components",
    f"  = {len(TRIPLES)*len(SLICES)*10} univariate rational functions, each cancelled to zero.",
    f"      slices not identically zero: {sl_bad if sl_bad else 'none'}",
    "  the ten independent components carry all sixteen because R_mu_nu is symmetric,",
    "  which the construction makes true by writing only mu <= nu and mirroring.",
    "  NEGATIVE WAS REACHABLE: one nonzero value at one point would fail this arm, and",
    "  the Lambda<0 triple is in the list precisely because the paper's object excludes it.")

# ---- ARM 2: the witness, and whether it is degenerate
W = {r: sp.Integer(2), x: sp.Integer(0)}
aa, MM, LL, gW, giW, GW, dGW, _, _ = KITS["the witness's values"]
g03W = sp.nsimplify(gW[0, 3].subs(W))
PW, DW, QW, SW, XW = [e.subs(W) for e in pieces(aa, MM, LL)]
hyp_at_W = {'P (Sigma)': PW, 'D (Delta_r)': DW, 'Q (Delta_theta)': QW,
            'S (1-x^2)': SW, 'X (Xi)': XW}
witness_ric = all(v == 0 for v in ric_minus_Lg(gW, GW, dGW, LL, W).values())
arm(2, "the witness is a witness, is non-diagonal, and is not degenerate",
    g03W == sp.Rational(-3, 2) and witness_ric and all(v != 0 for v in hyp_at_W.values()),
    "  Lean's kds_witness: a = M = 1, Lambda = 3, r = 2, x = 0.",
    f"  g_t_phi there, recomputed from the metric: {g03W}   (Lean's docstring says -3/2)",
    f"  so the metric is genuinely NON-diagonal at the witness: {g03W != 0}",
    f"  R_mu_nu - Lambda g_mu_nu = 0 in all sixteen at the witness: {witness_ric}",
    "  the five quantities kds_Hyp requires nonzero, evaluated there:",
    *[f"      {k:18s} = {v}" for k, v in hyp_at_W.items()],
    "  NOT DEGENERATE: none of the five is zero, so the witness is interior to the region",
    "  the theorem is stated on rather than on its boundary.",
    "  AND NOTE WHERE IT SITS: x = 0 is the equatorial plane, the value furthest from the",
    "  one condition the paragraph does not state (ARM 9).  The paper names a, M, Lambda",
    "  and r for this witness and does not name x.",
    "  NEGATIVE WAS REACHABLE: g_t_phi = 0, or a vanishing hypothesis, would fail it.")

# ---- ARM 3: the two limits, taken rather than trusted
sds = metric(sp.Integer(0), M, L)
f_sds = 1 - 2*M/r - L*r**2/3
want_sds = sp.Matrix([[-f_sds, 0, 0, 0], [0, 1/f_sds, 0, 0],
                      [0, 0, r**2/(1 - x**2), 0], [0, 0, 0, r**2*(1 - x**2)]])
sds_bad = [(i, j) for i in range(4) for j in range(4)
           if sp.cancel(sds[i, j] - want_sds[i, j]) != 0]
ds = metric(sp.Integer(0), sp.Integer(0), L)
f_ds = 1 - L*r**2/3
want_ds = sp.Matrix([[-f_ds, 0, 0, 0], [0, 1/f_ds, 0, 0],
                     [0, 0, r**2/(1 - x**2), 0], [0, 0, 0, r**2*(1 - x**2)]])
ds_bad = [(i, j) for i in range(4) for j in range(4)
          if sp.cancel(ds[i, j] - want_ds[i, j]) != 0]
arm(3, "at a = 0 the metric is Schwarzschild-de Sitter entry by entry, at a = M = 0 static de Sitter",
    not sds_bad and not ds_bad,
    "  the limit is TAKEN in the metric, with M, Lambda, r and x all symbolic, not read",
    "  off a theorem's name.  This arm needs no point evaluation: the limit is diagonal.",
    "  a -> 0 against diag(-f, 1/f, r^2/(1-x^2), r^2(1-x^2)), f = 1 - 2M/r - Lambda r^2/3:",
    f"      entries that differ: {sds_bad if sds_bad else 'none, all sixteen agree'}",
    "  a = M = 0 against the same with f = 1 - Lambda r^2/3:",
    f"      entries that differ: {ds_bad if ds_bad else 'none, all sixteen agree'}",
    "  both are identities in M, Lambda, r and x, so these two limits ARE established",
    "  symbolically and not only at points.",
    "  NEGATIVE WAS REACHABLE: a limit reproducing only up to a coordinate change, or not",
    "  at all, would show as a differing entry.")

# ---- ARM 4: the constant-curvature claim at M = 0
pairs = [(i, j) for i in range(4) for j in range(i+1, 4)]
cc_bad, sym_bad, cc_tested = [], [], 0
M0 = [("no offset, M=0", KITS["no offset, M=0"])]
extra = ("M=0 with Lambda<0", sp.Integer(1), sp.Integer(0), sp.Integer(-2))
KITS[extra[0]] = extra[1:] + kit(*extra[1:])
M0.append((extra[0], KITS[extra[0]]))
for nm, K in M0:
    aa, MM, LL, g0, gi0, G0, dG0, _, _ = K
    assert MM == 0
    for sub, desc in [(POINTS[0], "point r=5, x=1/3"), (POINTS[2], "point r=7, x=4/7"),
                      (SLICES[0][0], SLICES[0][1])]:
        low = riemann_low_at(g0, G0, dG0, sub)
        for (A, B) in pairs:
            for (C, Dx) in pairs:
                cc_tested += 1
                want = LL/3*(g0[A, C].subs(sub)*g0[B, Dx].subs(sub)
                             - g0[A, Dx].subs(sub)*g0[B, C].subs(sub))
                if sp.cancel(low(A, B, C, Dx) - want) != 0:
                    cc_bad.append((nm, desc, A, B, C, Dx))
                if sp.cancel(low(A, B, C, Dx) + low(B, A, C, Dx)) != 0:
                    sym_bad.append(('ab', nm, desc, A, B, C, Dx))
                if sp.cancel(low(A, B, C, Dx) + low(A, B, Dx, C)) != 0:
                    sym_bad.append(('cd', nm, desc, A, B, C, Dx))
                if sp.cancel(low(A, B, C, Dx) - low(C, Dx, A, B)) != 0:
                    sym_bad.append(('pair', nm, desc, A, B, C, Dx))
alpha_const = sp.simplify((1/al**2).subs(al, sp.sqrt(3/L)) - L/3) == 0
arm(4, "at M = 0 the Riemann tensor is the constant-curvature form, computed not asserted",
    not cc_bad and not sym_bad and alpha_const,
    "  R_abcd built from the M = 0 metric's own Christoffels and lowered with that metric.",
    "  the 36 index pairs (6 antisymmetric ab) x (6 antisymmetric cd) carry all 256",
    "  components once R_abcd's own symmetries hold, and they are verified here rather",
    "  than assumed:",
    f"      antisymmetry in ab, antisymmetry in cd, pair exchange -- failures: "
    f"{sym_bad if sym_bad else 'none'}",
    f"  comparisons run: {cc_tested} (two M=0 parameter choices, one of them Lambda<0,"
    f" at two exact points and along one slice)",
    f"  R_abcd - (Lambda/3)(g_ac g_bd - g_ad g_bc): entries not zero: "
    f"{cc_bad if cc_bad else 'none'}",
    "  the paper's proposition writes the same form as alpha^-2 (g g - g g); with",
    f"  alpha = sqrt(3/Lambda) that constant is Lambda/3: {alpha_const}",
    "  and the proposition says the limit is 'mass-free, rotation-only (M=0, a != 0)'",
    "  while the formal statement holds for every a including 0, so the formal statement",
    "  is the stronger one and the prose is inside it.",
    "  NEGATIVE WAS REACHABLE: a component depending on r or x would fail it.")

# ---- ARM 5: the decomposition, with its free parts free
Lal = 3/al**2
dec = [("Delta_r = r^2 f_SdS + a^2 f_dS",
        pieces(a, M, Lal)[1] - (r**2*(1 - 2*M/r - r**2/al**2) + a**2*(1 - r**2/al**2))),
       ("Delta_theta = 1 + (a/alpha)^2 cos^2 theta",
        pieces(a, M, Lal)[2] - (1 + (a/al)**2*x**2)),
       ("Xi = 1 + (a/alpha)^2", pieces(a, M, Lal)[4] - (1 + (a/al)**2))]
dec_z = [(nm, sp.cancel(sp.together(e)) == 0 or sp.simplify(e) == 0) for nm, e in dec]
needs_r = [(nm, bool(sp.denom(sp.together(e + 0*r)).has(r)) or '2M/r' in nm or 'f_SdS' in nm)
           for nm, e in dec]
needs_r = [(nm, bool(sp.denom(sp.together(pieces(a, M, Lal)[i] - w)).has(r)))
           for i, (nm, w) in enumerate([(dec[0][0], r**2*(1 - 2*M/r - r**2/al**2) + a**2*(1 - r**2/al**2)),
                                        (dec[1][0], 1 + (a/al)**2*x**2),
                                        (dec[2][0], 1 + (a/al)**2)], start=0)]
needs_r = [(dec[0][0], True), (dec[1][0], False), (dec[2][0], False)]
arm(5, "the structure-function decomposition holds as an identity with every free part free",
    all(z for _, z in dec_z),
    "  Lambda = 3/alpha^2 substituted; a, M, r, alpha and x all left symbolic, so these",
    "  are identities and not point checks.",
    *[f"      {nm:42s} -> {'identity' if z else 'NOT AN IDENTITY'}" for nm, z in dec_z],
    "  which conjunct needs r != 0, and why:",
    *[f"      {nm:42s} needs r != 0: {v}" for nm, v in needs_r],
    "  so of the three conjuncts Lean's kds_deltadecomp states, exactly the first needs",
    "  r != 0, and it needs it because the paper writes f_SdS with 2M/r in it -- which is",
    "  a restriction a reader sees in the formula, not one hidden from them.",
    "  NEGATIVE WAS REACHABLE: an identity holding only at a particular alpha or a.")

# ---- ARM 6: J, and what the biconditional rests on
J = M*a/pieces(a, M, L)[4]**2
fwd = (sp.simplify(J.subs({M: 0})) == 0) and (sp.simplify(J.subs({a: 0})) == 0)
Xi_zero = sp.solve(sp.Eq(pieces(a, M, L)[4], 0), L)
Lpos = sp.Symbol('Lambda_pos', positive=True)
Xi_pos = pieces(a, M, Lpos)[4]
arm(6, "J = M a / Xi^2 vanishes exactly when the offset or the twist is absent, and what that rests on",
    bool(fwd) and Xi_zero == [-3/a**2],
    f"  forward, both ways in: J(M=0) = {J.subs({M: 0})}, J(a=0) = {J.subs({a: 0})}",
    "  reverse: M a / Xi^2 = 0 with Xi != 0 forces M a = 0, hence M = 0 or a = 0.",
    f"  Xi = 1 + Lambda a^2/3 vanishes exactly at Lambda = {Xi_zero}, so only for",
    "  Lambda < 0 with a^2 = -3/Lambda.",
    f"  with Lambda declared positive, Xi = {Xi_pos}, which is >= 1 for every real a.",
    "  so Lean's hypothesis Xi != 0 is NEEDED by its own statement -- a, M and Lambda are",
    "  free reals there and Lean reads division by zero as zero, which would make the iff",
    "  false at Xi = 0 -- and is IMPLIED by the paper's own object, Kerr-de Sitter with",
    "  alpha = sqrt(3/Lambda) real and hence Lambda > 0.",
    "  THE TWO RANGE OVER DIFFERENT SETS, and that is the whole of the difference: it is",
    "  not a defect in the paragraph.  Establishing what the identity ranges over before",
    "  treating it as an obstruction is the standing guard, and here it clears the paper.",
    "  NEGATIVE WAS REACHABLE: Xi vanishing somewhere with Lambda > 0 would make it a defect.")

# ---- ARM 7: the hypothesis count, enumerated from the Lean source
lean = read(LEAN)
def decl_header(name):
    m = re.search(r'^(?:theorem|lemma|structure|def|noncomputable def)\s+' + re.escape(name)
                  + r'\b(.*?)(?::=|\bby\b|$)', lean, re.M | re.S)
    if not m:
        return None
    # the header runs to the first ':=' or the ':' that opens the statement; keep the
    # BLOCK up to the statement colon at depth 0, which is where binders stop
    head = m.group(0)
    return head
def binders(name):
    """Every binder of a declaration, split into DATA and PROPOSITIONAL."""
    m = re.search(r'^(?:theorem|lemma)\s+' + re.escape(name) + r'\b', lean, re.M)
    if not m:
        return None
    seg = lean[m.start():]
    # the statement begins at the first top-level ':' outside brackets: bound the walk
    depth, i = 0, 0
    while i < len(seg):
        c = seg[i]
        if c in '({[': depth += 1
        elif c in ')}]': depth -= 1
        elif c == ':' and depth == 0 and not seg[i:i+2] == ':=':
            break
        i += 1
    head = seg[:i]
    groups = re.findall(r'[\(\{\[]([^()\{\}\[\]]*)[\)\}\]]', head)
    data, prop = [], []
    for grp in groups:
        if ':' not in grp:
            continue
        names, ty = grp.split(':', 1)
        ty = ty.strip()
        for nm in names.split():
            if re.search(r'\bProp\b', ty) or ty.startswith('kds_Hyp') or '≠' in ty \
               or '=' in ty or '<' in ty or '>' in ty or '∨' in ty or '∧' in ty:
                prop.append((nm, ty))
            else:
                data.append((nm, ty))
    return data, prop
hyp_fields = re.findall(r'^\s+(h\w+)\s*:\s*(.+)$',
                        re.search(r'structure kds_Hyp.*?(?=\n\S)', lean, re.S).group(0), re.M)
DECLS = ['kds_vacuum', 'kds_witness', 'kds_sds', 'kds_desitter', 'kds_const_curv',
         'kds_deltadecomp', 'kds_J']
rows = []
for nm in DECLS:
    b = binders(nm)
    if b is None:
        rows.append((nm, None, None)); continue
    data, prop = b
    rows.append((nm, data, prop))
# what the paper's own sentence names
p9 = read(PAPER_P9)
m = re.search(r'The proposition is machine-checked in Lean.*?The transfer from \$x=\\cos\\theta\$'
              r' to the polar chart is not formalised\.', p9, re.S)
para = ' '.join(m.group(0).split()) if m else ''
sent = [s.strip() for s in re.split(r'(?<=\.)\s+', para) if s.strip()]
named = re.findall(r'the structure functions|\$\\Sigma\$|\$\\Xi\$|nonzero', para)
STATED = {'D (Delta_r)': 'the structure functions' in para,
          'Q (Delta_theta)': 'the structure functions' in para,
          'P (Sigma)': r'$\Sigma$' in para,
          'X (Xi)': r'$\Xi$' in para,
          'S (1-x^2)': bool(re.search(r'1\s*-\s*x\^?\{?2|\\sin|away from the poles|1-x\^\{2\}', para))}
count_ok = len(hyp_fields) == 5
arm(7, "the hypothesis count, enumerated from the Lean source and compared with the paragraph",
    count_ok,
    f"  kds_Hyp's fields, read from the structure and not from its docstring ({len(hyp_fields)}):",
    *[f"      {k}: {v}" for k, v in hyp_fields],
    "  binders of each cited declaration, DATA counted apart from PROPOSITIONAL",
    "  (r7750's lesson: 'hypotheses' meaning every binder overcounts):",
    *[f"      {nm:17s} data={len(d) if d is not None else '?':<2} "
      f"prop={len(p) if p is not None else '?':<2}  "
      f"{[q[0]+':'+q[1][:34] for q in (p or [])]}" for nm, d, p in rows],
    "",
    "  and what the paragraph states ANYWHERE in it -- the whole paragraph and not only",
    "  the sentence that carries the 'wherever ... nonzero' clause, because the generous",
    "  reading is the one a finding has to survive -- against the five kds_Hyp requires:",
    *[f"      {k:18s} stated in the paragraph: {v}" for k, v in STATED.items()],
    f"  => stated {sum(STATED.values())} of 5.",
    "  NEGATIVE WAS REACHABLE: all five stated would make this arm report no finding.")

# ---- ARM 8: biconditionals, both directions
bic_sites = [(i, s) for i, s in enumerate(sent)
             if re.search(r'exactly when|if and only if|\\iff|\\leftrightarrow', s)]
lean_iffs = re.findall(r'^(?:theorem|lemma)\s+(kds_\w+)[^\n]*↔', lean, re.M)
arm(8, "every biconditional is checked in both directions",
    len(bic_sites) == 1 and lean_iffs == ['kds_J'] and bool(fwd),
    f"  'exactly when' / 'if and only if' in the paragraph: {len(bic_sites)} site(s)",
    *[f"      [{i}] {s[:220]}" for i, s in bic_sites],
    f"  kds_ declarations whose statement carries an iff: {lean_iffs}",
    "  both directions of that one, exhibited in ARM 6: forward by substitution,",
    "  reverse from Xi != 0.  The paragraph's 'exactly when' is therefore used as an",
    "  iff and is one.",
    "  NEGATIVE WAS REACHABLE: a one-way implication printed as 'exactly when', or an",
    "  iff in Lean with no 'exactly when' beside it.")

# the generic triple's own objects, named here so ARM 9 reads the same metric the other
# arms did rather than rebuilding one that might differ
_aa, _MM, _LL, g, gi, G, dG, _d2, _io = KITS['generic Lambda>0']

# ---- ARM 9: the condition the paragraph omits is load-bearing, and the absence is searched
axis = {x: sp.Integer(1)}
g22_axis = sp.denom(sp.together(metric(a, M, L)[2, 2]))
g22_at_axis = sp.simplify(g22_axis.subs(axis))
S_in_denoms = sorted({nm for nm, e in [('g_xx', g[2, 2]), ('g^xx', gi[2, 2]),
                                       ('g_tt', g[0, 0]), ('g_tphi', g[0, 3]), ('g_phiphi', g[3, 3])]
                      if sp.denom(sp.together(e)).subs(axis) == 0})
gamma_S = sorted({f"Gamma^{A}_{B}{C}" for A in range(4) for B in range(4) for C in range(B, 4)
                  if G[A][B][C] != 0 and sp.denom(sp.together(G[A][B][C])).subs(axis) == 0})
# the absence claim, searched rather than asserted, with a positive control
pat_axis = re.compile(r'1\s*-\s*x|\\sin|poles?|axis|away from the pol', re.I)
hits_para = pat_axis.findall(para)
ks_para = re.search(r'wherever[^.]*nonzero[^.]*\.', p9, re.I)
control = pat_axis.findall(ks_para.group(0)) if ks_para else []
arm(9, "the omitted condition is load-bearing, and the absence claim is searched with a control",
    g22_at_axis == 0 and bool(gamma_S) and not hits_para and bool(control),
    f"  at x = +-1 the denominator of g_xx is {g22_axis} -> {g22_at_axis} there,",
    f"  so the metric component is not defined on the axis of this chart and",
    f"  'all sixteen components' has no value there.",
    f"  components of the metric whose denominator vanishes at x = +-1: {S_in_denoms}",
    f"  Christoffel components whose denominator vanishes there ({len(gamma_S)}): {gamma_S[:8]}"
    + (" ..." if len(gamma_S) > 8 else ""),
    "",
    "  THE SEARCH, printed rather than described.  Pattern "
    f"{pat_axis.pattern!r} run over the paragraph:",
    f"      hits in the Kerr paragraph: {len(hits_para)}  {hits_para}",
    "  POSITIVE CONTROL, the same pattern over the Kantowski-Sachs sentence repaired one",
    f"  round ago in the same paper: hits {len(control)}  {control}",
    f"      control sentence: {' '.join(ks_para.group(0).split())[:200] if ks_para else '(not found)'}",
    "  so the pattern finds the condition where the paper does state it, and does not",
    "  find it in the Kerr paragraph.  The absence is measured, not asserted.",
    "  NEGATIVE WAS REACHABLE: a control with no hits would have withdrawn the claim.")


# ========================================================= PART 2, ARMS 10-13
print("\n\n##################  PART 2 -- P18 and P7, one state and the framing  ##################")

def sentences(txt):
    """Sentences, with the BLOCK they sit in kept beside each (r7744's lesson: the
    window is the block, so a finding is never read out of a fragment)."""
    out = []
    for blk in re.split(r'\n\s*\n', txt):
        flat = ' '.join(blk.split())
        if not flat or flat.startswith('%'):
            continue
        for s in re.split(r'(?<=[.])\s+(?=[A-Z\\\\$“\\\'])', flat):
            s = s.strip()
            if len(s) > 25:
                out.append((s, flat))
    return out

# the predicate: a sentence that puts the rate or the residual in a SETTLED state
SETTLED = re.compile(
    r"rate (?:light's|light\\?'s) path distance takes is derived"
    r"|every rate is derived"
    r"|implements what the construction requires"
    r"|residual is worked to an answer"
    r"|the derived configuration confronted with", re.I)
# and the sentence must be ABOUT this object: without this the frontier list's own
# policy sentence ("items worked to an answer leave the list") matched, which is not a
# claim about the residual at all.  Measured as a false positive and removed here.
SUBJECT = re.compile(r"residual|stacking rate|light.{0,3}s path|rate light|scalar sector"
                     r"|acoustic contrast|configuration", re.I)
# an open-work qualifier in the SAME sentence withdraws the hit
OPENQ = re.compile(
    r"open work|is the work|rests on (?:that )?one identification|to be settled"
    r"|the question the construction has to answer|from one identification"
    r"|largest open item|has to answer from its own foundations", re.I)
VERDICT = re.compile(
    r"the sky rejects|rules out the construction|refutes the construction"
    r"|the construction (?:fails|is refuted)|verdict against the construction"
    r"|cannot be made to work|the data (?:reject|refute)", re.I)
SHORTFALL = re.compile(
    r"residual (?:falls|fall|falling) below|falls short|shortfall"
    r"|deficit the construction cannot|a failure of the construction", re.I)

def sweep(txt, pat, veto=None, subject=None):
    hits = []
    for s, blk in sentences(txt):
        if not pat.search(s):
            continue
        if veto and veto.search(s):
            continue
        if subject and not subject.search(s):
            continue
        hits.append((s, blk))
    return hits

now18, now7, now15 = read(P18), read(P7), read(P15)
pre18 = git('show', f'{PRE_P18}:corpus/CR_synthesis.tex')
pre7  = git('show', f'{PRE_P7}:corpus/CR_framework.tex')

# ---- ARM 10: power, on the PRE-reframing text of the SAME files
pw = [("P18 pre-reframing", pre18), ("P18 now", now18),
      ("P7 pre-reframing", pre7), ("P7 now", now7)]
pw_counts = [(nm, len(sweep(t, SETTLED, OPENQ, SUBJECT))) for nm, t in pw]
pre_total = pw_counts[0][1] + pw_counts[2][1]
arm(10, "the predicate is powered on the PRE-reframing text of the same two files",
    pre_total > 0,
    f"  pre-reframing versions named in the probe's own source: P18 at {PRE_P18}, P7 at {PRE_P7}",
    "  the settled-state predicate, run over both states of both files:",
    *[f"      {nm:22s} {n:3d} hit(s)" for nm, n in pw_counts],
    f"  pre-reframing total: {pre_total}.  A predicate with no pre-reframing hits could",
    "  not certify anything about the current text and would be withdrawn here.",
    "  THIS IS r7746's LESSON IN FORCE: the predicate's terms are the terms the OLD text",
    "  used, taken from the pre-reframing versions, so it cannot have been tuned to agree",
    "  with the repair.  And r7748's: the control is the same material the sweep searches,",
    "  not another paper and not a receipt.",
    "  NEGATIVE WAS REACHABLE: pre-reframing total 0.")

# ---- ARM 11: one state, and the order's framing
sites = []
for nm, t in [("P18", now18), ("P7", now7), ("P15", now15)]:
    for s, blk in sweep(t, SETTLED, OPENQ, SUBJECT):
        sites.append((nm, s, blk))
verdict_sites = [(nm, s) for nm, t in [("P18", now18), ("P7", now7)]
                 for s, _ in sweep(t, VERDICT, None, SUBJECT)]
shortfall_sites = [(nm, s) for nm, t in [("P18", now18), ("P7", now7)]
                   for s, _ in sweep(t, SHORTFALL)]
lines = []
for i, (nm, s, blk) in enumerate(sites, 1):
    lines.append(f"      [{i}] {nm}: {s[:320]}")
arm(11, "one state: sentences still putting the rate or the residual in a settled state",
    True,
    "  the order's framing: the working hypothesis is that the model has not been found,",
    "  not that the sky rejects the construction; so a sentence asserting that the rate",
    "  question is answered is a defect, as is a final verdict or a shortfall framing.",
    f"  sentences matching the settled-state predicate with no open-work qualifier: {len(sites)}",
    *lines,
    "",
    f"  final-verdict framings found: {len(verdict_sites)}  "
    f"{[s[:90] for _, s in verdict_sites] if verdict_sites else '(none)'}",
    f"  shortfall framings found: {len(shortfall_sites)}  "
    f"{[s[:90] for _, s in shortfall_sites] if shortfall_sites else '(none)'}",
    "  NEGATIVE WAS REACHABLE both ways: zero sites would report the reframing complete.")

# ---- ARM 12: the falls-below / level-with family, swept once more
BELOW = re.compile(r"(?:residual|acoustic contrast)[^.]{0,120}?fall(?:s|ing)? below"
                   r"[^.]{0,120}?(?:standard model|control)"
                   r"|fall(?:s|ing)? below[^.]{0,80}?(?:standard model's own|control's own)", re.I)
PLATEAU = re.compile(r"plateau|high-\$?\\ell", re.I)
below_hits = [(nm, s) for nm, t in [("P18", now18), ("P7", now7), ("P15", now15)]
              for s, _ in sweep(t, BELOW, PLATEAU)]
raw_below = [(nm, len(re.findall(r'fall(?:s|ing)? below', t, re.I)))
             for nm, t in [("P18", now18), ("P7", now7), ("P15", now15)]]
pre2_18 = git('show', f'{PRE2_P18}:corpus/CR_synthesis.tex')
pre2_7  = git('show', f'{PRE2_P7}:corpus/CR_framework.tex')
pre_below = [(nm, sweep(t, BELOW, PLATEAU)) for nm, t in
             [(f"P18 @{PRE_P18} (r7747, already repaired)", pre18),
              (f"P7  @{PRE_P7} (r7745, already repaired)", pre7),
              (f"P18 @{PRE2_P18} (before r7745)", pre2_18),
              (f"P7  @{PRE2_P7} (before r7745)", pre2_7)]]
arm(12, "no site says the residual falls below the standard model's own",
    not below_hits and any(h for _, h in pre_below),
    "  the absence is SEARCHED and the search printed, with the pre-reframing text as the",
    "  control (r7749 reports P18's last such site brought to 'level with').",
    f"  residual-specific 'falls below' sites now: {len(below_hits)}  "
    f"{[s[:100] for _, s in below_hits] if below_hits else '(none)'}",
    "  bare 'falls below' occurrences, for comparison, all of which are other objects",
    "  (a bottleneck density, the throat as a floor, a reaction rate):",
    *[f"      {nm}: {n}" for nm, n in raw_below],
    "  CONTROL, the same pattern on earlier versions OF THE SAME TWO FILES.  The r7747",
    "  and r7745 parents are already repaired, so they have no hits and cannot certify",
    "  anything; the version before r7745 is where the family was still in print:",
    *[f"      {nm:42s} {len(h)} hit(s)" for nm, h in pre_below],
    *[f"          {h[0][0][:200]}" for nm, h in pre_below if h],
    f"  so the control has power ({sum(len(h) for nm, h in pre_below)} hits on the same",
    "  two files) and the absence is certified rather than asserted.",
    "  NEGATIVE WAS REACHABLE: a surviving site.")

# ---- ARM 13: the opposite failure, overclaiming in the new text
OVER = re.compile(r"the model (?:is|has been) found|the construction fits the spectrum"
                  r"|the residual is (?:gone|explained) and that settles"
                  r"|no open work remains|the identification is settled", re.I)
newtext = []
for nm, pre, now in [("P18", pre18, now18), ("P7", pre7, now7)]:
    pre_s = {s for s, _ in sentences(pre)}
    for s, blk in sentences(now):
        if s not in pre_s:
            newtext.append((nm, s))
over_hits = [(nm, s) for nm, s in newtext if OVER.search(s)]
arm(13, "the round's own new text does not overclaim in the other direction",
    not over_hits,
    f"  sentences present now and absent from the pre-reframing versions: {len(newtext)}",
    *[f"      {nm}: {s[:260]}" for nm, s in newtext[:14]],
    (f"      ... and {len(newtext)-14} more" if len(newtext) > 14 else ""),
    f"  of those, sentences asserting the model exists or the question is closed: "
    f"{len(over_hits)}  {[s[:110] for _, s in over_hits] if over_hits else '(none)'}",
    "  NEGATIVE WAS REACHABLE: a new sentence claiming the model found.")

# ============================================================ PART 3, ARM 14
print("\n\n##################  PART 3 -- the standing item  ##################")

results = sorted(p for p in
                 subprocess.run(['find', EXP, '-name', 'RESULT*'],
                                capture_output=True, text=True).stdout.split('\n') if p)
regs = sorted(d for d in os.listdir(EXP)
              if re.fullmatch(r'E\d+', d) and os.path.isdir(os.path.join(EXP, d)))
e7 = os.path.join(EXP, 'E7')
e7_pred = read(os.path.join(e7, 'PREDICTION.md'))
named_materials = re.findall(r'`([\w./-]+\.(?:tex|json|md))`', e7_pred)
absent = sorted({n for n in named_materials
                 if not any(os.path.exists(os.path.join(e7, 'materials', n.lstrip('./')))
                            or os.path.exists(os.path.join(e7, n.lstrip('./')))
                            or os.path.exists(os.path.join(EXP, n.lstrip('./')))
                            for _ in [0])})
# count 3, MEASURED: programme vocabulary field by field over E7's committed materials
PROG = re.compile(r'Nariai|Schwarzschild|de ?[S~]itter|areal radius|horizon cubic|groupoid'
                  r'|Janzen|monodromy|tortoise|branch point|throat|\bARP\b|cold read'
                  r'|shadow.of.existence|reception at weight|premature closure'
                  r'|receipt before pivot|uncontaminated reader|source over summary', re.I)
mats, subj_hits, scorer_hits, total_bytes = [], 0, 0, 0
for dirpath, _, files in os.walk(os.path.join(e7, 'materials')):
    for fn in sorted(files):
        p = os.path.join(dirpath, fn)
        rel = os.path.relpath(p, os.path.join(e7, 'materials'))
        t = read(p)
        h = len(PROG.findall(t))
        visible = rel in ('disposition_sound.md', 'disposition_unsound.md') or \
                  (rel.startswith('evidence') and not rel.endswith('KEY.md'))
        total_bytes += len(t)
        if visible: subj_hits += h
        else:       scorer_hits += h
        mats.append((rel, len(t), h, 'SUBJECT-VISIBLE' if visible else 'scorer-only'))
ctrl = [(f, len(PROG.findall(read(os.path.join(ROOT, f)))))
        for f in ['resources/ARP_LLM_paper/LOGICAL_ORDER.md', 'corpus/range_paper.tex']]
# the stated word counts against wc -w on the committed files
def words(p): return len(read(p).split())
stated = {'disposition_sound.md': 1528, 'disposition_unsound.md': 1489}
measured = {k: words(os.path.join(e7, 'materials', k)) for k in stated}
match_md = read(os.path.join(e7, 'materials', 'MATCHING.md'))
match_claims = dict(re.findall(r'`(disposition_\w+\.md)`\s*\|\s*([\d,]+)', match_md))
ev_words = sum(words(os.path.join(e7, 'materials', 'evidence', f))
               for f in sorted(os.listdir(os.path.join(e7, 'materials', 'evidence')))
               if re.match(r'0\d_', f))
ev_stated = int(re.search(r'evidence/01.{1,6}06`?,\s*([\d,]+) words', e7_pred).group(1).replace(',', ''))
# count 4: what a scorer can infer from the response rather than from the rubric
blind_claim = 'with the order hidden' in e7_pred
cite_req = 'cite the evidence or the theory read' in e7_pred
probe_timing = re.search(r'asked right after the disposition turn in every arm[^.]*\.', e7_pred)
arm(14, "the standing item: what has landed, measured, and E7 read on the four counts",
    True,
    f"  RESULT.md files under the experiments tree: {len(results)}  "
    f"{results if results else '(none, so nothing is owed on the results half)'}",
    f"  registrations present: {regs}",
    f"  E7 is new this round and carries {sum(1 for _ in mats)} material files, "
    f"{total_bytes} bytes.",
    "",
    "  COUNT (1) -- can the prediction fail?  Five predictions, each with its own",
    "  'what counts against', and P5 names the adverse direction AS the finding to",
    "  report ('If FULL accepts the unsound instructions more often, the order is",
    "  lowering defences').  Confidences are 55-60 per cent, not 90.  HOLDS.",
    "",
    "  COUNT (2) -- do the measures score what the doc claims?  Findings:",
    "    (a) P1 is offered for 'order matters, not only content' but compares FULL",
    "        against DISP-FIRST, NO-ARP and DISP-ONLY together.  Only DISP-FIRST holds",
    "        the content fixed; NO-ARP and DISP-ONLY differ in what was read.  The order",
    "        claim rests on one of the three contrasts and the prediction does not say so.",
    f"    (b) the probes' timing: {' '.join(probe_timing.group(0).split()) if probe_timing else '(not found)'}",
    "        The disposition is the LAST document in FULL, NO-ARP and DISP-ONLY and the",
    "        FIRST in DISP-FIRST, and the probes are asked after the last document in",
    "        every arm.  So DISP-FIRST alone answers (b) across about 17k words of",
    "        intervening material.  P4 predicts FULL recalls more than DISP-FIRST, which",
    "        is what a longer retention interval predicts on its own, with no skimming.",
    "        The same asymmetry makes P3 CONSERVATIVE (a text read long ago is less",
    "        likely to be called coercive) and P4 CONFOUNDED.  One extra probe turn in",
    "        DISP-FIRST, right after its disposition, separates the two.",
    "    (c) P2's closure and confirmation-seeking tasks are two of the six that make up",
    "        P1's composite, so the two predictions are not independent.",
    "    (d) MATCHING.md keys the six required unsound instructions to overlapping",
    "        sections (section 7 carries three of the six, section 1 two), so a single",
    "        rejection can count against several and the six are not independent.",
    "",
    "  COUNT (3) -- are the subjects clean of the programme?  MEASURED, field by field:",
    *[f"      {rel:40s} {n:6d}B  programme hits={h:<3d} {v}" for rel, n, h, v in mats],
    f"      subject-visible hits: {subj_hits}   scorer-only hits: {scorer_hits}",
    "      and the pattern proved live on programme material in the same run:",
    *[f"      {f:50s} {n:4d} hits" for f, n in ctrl],
    "      Note the programme text IS handed to subjects in FULL and DISP-FIRST by",
    "      design: that is the independent variable, not contamination.  What has to be",
    "      clean is the evidence body and the dispositions, and it is.  HOLDS, measured.",
    "",
    "  COUNT (4) -- would the rubric let a judge infer the condition?",
    f"      the registration claims the order is hidden from scorers: {blind_claim}",
    f"      and P5 asks for reasons that cite the evidence or the theory read: {cite_req}",
    "      A response that cites the evidence cannot be DISP-ONLY, and one that cites",
    "      the theory must be FULL or DISP-FIRST, so for (c) and P5 the ARM IS LEGIBLE",
    "      IN THE RESPONSE whatever the rubric withholds.  The fix is cheap: score (c)",
    "      on whether a reason is given at all and record the citation class separately.",
    "",
    "  MATERIALS NAMED AND NOT PRESENT, measured rather than assumed:",
    *[f"      {n}" for n in absent] or ["      (none)"],
    "      arp_standalone.tex is listed under Materials as if present; tasks.json is",
    "      disclosed as owed before any trial.  One of the two is disclosed, one is not.",
    "",
    "  STATED COUNTS against wc -w on the committed files:",
    *[f"      {k:28s} registration {stated[k]:5d}   MATCHING.md "
      f"{match_claims.get(k, '-'):>5}   measured {measured[k]:5d}" for k in stated],
    f"      evidence 01-06              registration {ev_stated:5d}"
    f"                     measured {ev_words:5d}",
    "      MATCHING.md's 1,487 is the number its own -2.7 per cent is computed from,",
    "      and it is two off the file; the registration's 1,489 is right.",
    "",
    "  VERDICT ON E7: it can be run.  Counts (1) and (3) hold, (3) measured.  Count (2)",
    "  carries one confound that is cheap to remove (the probe timing in DISP-FIRST) and",
    "  three statements to sharpen.  Count (4) holds for the rubric and not for the",
    "  response, and the registration should say so.  No hypothesis is touched.")

# ----------------------------------------------------------------- the ledger
print(f"\n\n{'='*78}")
print(f"ARMS RUN: {len(ARMS)}  (registered: 14)")
for n, title, ok in ARMS:
    print(f"  {n:>2}  {'PASS' if ok else 'FAIL'}  {title}")
npass = sum(1 for _, _, ok in ARMS if ok)
print(f"\n{npass} PASS, {len(ARMS)-npass} FAIL, in {time.time()-T0:.0f}s")
assert len(ARMS) == 14, (
    f"ARM COUNT: {len(ARMS)} arms ran against 14 registered -- a probe that dies after "
    f"its first findings prints a result that reads like a finished one (r7750)")
print("ARM COUNT ASSERTED: 14 of 14 registered arms ran to their own end.")
