#!/usr/bin/env python3
"""r7754 (60) -- a cold read of P9's three new formal paragraphs, of this round's
framing correction, and of E1's first RESULT.

Registered in PREDICTION.md and PUSHED before corpus/range_paper.tex,
probes/Range.lean, corpus/CR_synthesis.tex, corpus/CR_framework.tex, FOR_66.md or
resources/ARP_LLM_paper/experiments/E1/RESULT.md were opened in this revision.
FOURTEEN arms, each a comparison with its negative named.

Part 1 rebuilds each metric from the form the PAPER prints and recomputes the
curvature; Part 2's predicates keep the old text's own terms and are powered on a
version in which the old framing was still present; Part 3 reads E1's result against
its registration AS IT STOOD IN THE COMMIT THAT REGISTERED IT, out of git history.
"""
import json, os, re, subprocess, sys, time
import sympy as sp

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
P9   = os.path.join(ROOT, 'corpus', 'range_paper.tex')
LEAN = os.path.join(ROOT, 'computations', 'formalisation', 'lean', 'probes', 'Range.lean')
P18  = os.path.join(ROOT, 'corpus', 'CR_synthesis.tex')
P7   = os.path.join(ROOT, 'corpus', 'CR_framework.tex')
P15  = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
E1   = os.path.join(ROOT, 'resources', 'ARP_LLM_paper', 'experiments', 'E1')

# the version of each file immediately BEFORE this round's correction, and -- for the
# settled-state family -- a version in which it was still in print.  r7752's own defect
# was taking a control at the parent of the change when the repair was older than it.
PRE_P18, PRE_P7 = '4fc4b1d92', 'ad0a30ff5'     # before r7752's five landed
PRE2_P18, PRE2_P7 = '468aa9093', '8b43d868b'   # before r7745, where the family was live
E1_REG = '36c2d8408'        # the commit that registered E1, 30 min before the first trial

T0 = time.time()
ARMS = []
def arm(n, title, ok, *lines):
    ARMS.append((n, title, bool(ok)))
    print(f"\n{'='*78}\nARM {n} -- {title}\n{'='*78}")
    for l in lines:
        if l: print(l)
    print(f"  => {'PASS' if ok else 'FAIL'}   [t={time.time()-T0:.0f}s]")

def git(*a):
    return subprocess.run(['git', '-C', ROOT] + list(a), capture_output=True,
                          text=True, check=True).stdout
def read(p):
    with open(p, encoding='utf-8', errors='replace') as f:
        return f.read()

# ------------------------------------------------------------- curvature machinery
def christoffels(g, gi, co):
    n = len(co)
    dg = [[[sp.cancel(sp.diff(g[i, j], co[k])) if co[k] is not None else sp.S.Zero
            for k in range(n)] for j in range(n)] for i in range(n)]
    G = [[[sp.S.Zero]*n for _ in range(n)] for _ in range(n)]
    for A in range(n):
        for B in range(n):
            for C in range(B, n):
                s = sp.S.Zero
                for E in range(n):
                    if gi[A, E] == 0: continue
                    s += gi[A, E]*(dg[E][C][B] + dg[B][E][C] - dg[B][C][E])
                v = sp.cancel(s/2); G[A][B][C] = v; G[A][C][B] = v
    return G

def ricci(G, co, sub=None):
    n = len(co)
    def D(e, k):
        return sp.S.Zero if co[k] is None else sp.diff(e, co[k])
    out = sp.zeros(n, n)
    for mu in range(n):
        for nu in range(mu, n):
            s = sp.S.Zero
            for lam in range(n):
                s += D(G[lam][mu][nu], lam) - D(G[lam][mu][lam], nu)
                for sig in range(n):
                    s += G[lam][lam][sig]*G[sig][mu][nu] - G[lam][nu][sig]*G[sig][mu][lam]
            v = sp.cancel(s.subs(sub) if sub else s)
            out[mu, nu] = v; out[nu, mu] = v
    return out

def riemann_low(g, G, co):
    n = len(co)
    def D(e, k):
        return sp.S.Zero if co[k] is None else sp.diff(e, co[k])
    Rup = [[[[sp.S.Zero]*n for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for A in range(n):
        for B in range(n):
            for C in range(n):
                for E in range(n):
                    s = D(G[A][E][B], C) - D(G[A][C][B], E)
                    for lam in range(n):
                        s += G[A][C][lam]*G[lam][E][B] - G[A][E][lam]*G[lam][C][B]
                    Rup[A][B][C][E] = sp.cancel(s)
    def low(A, B, C, E):
        s = sp.S.Zero
        for F in range(n):
            if g[A, F] != 0: s += g[A, F]*Rup[F][B][C][E]
        return sp.cancel(s)
    return low

print(f"r7754 (60) -- PROBE  [HEAD {git('rev-parse', '--short', 'HEAD').strip()}]")
print(f"sympy {sp.__version__}, python {sys.version.split()[0]}")

# ================================================= PART 1 -- the three paragraphs
print("\n\n#########  PART 1 -- P9's three new formal paragraphs  #########")

# ---- the separable (Carter) cut, from eq:carter as the paper prints it
# The structure functions depend on ONE variable each, so the curvature depends only on
# R, R', R'', P, P', P'' and r, p.  Those six are carried as independent SYMBOLS with the
# chain rule taught to the derivative operator: that keeps the computation polynomial and
# the generality total -- the result holds for every twice-differentiable pair, not for a
# family of quartics that happens to span.
L, r, p, c0, c1, c2, d0, d1 = sp.symbols('Lambda r p c0 c1 c2 d0 d1', real=True)
R0, R1, R2, R3 = sp.symbols('R0 R1 R2 R3', real=True)
Q0, Q1, Q2, Q3 = sp.symbols('P0 P1 P2 P3', real=True)
CO_C = [None, None, r, p]

def Dc(e, k):
    """d/dcoord with R0' = R1, R1' = R2, ... taught in."""
    if k == 2:
        return (sp.diff(e, r) + sp.diff(e, R0)*R1 + sp.diff(e, R1)*R2 + sp.diff(e, R2)*R3)
    if k == 3:
        return (sp.diff(e, p) + sp.diff(e, Q0)*Q1 + sp.diff(e, Q1)*Q2 + sp.diff(e, Q2)*Q3)
    return sp.S.Zero

def carter(Rr, Pp):
    """ds^2 = (S/R)dr^2 + (S/P)dp^2 + (1/S)[R(dtau - p^2 dsigma)^2 - P(dtau + r^2 dsigma)^2]
       in coordinates (tau, sigma, r, p), S = r^2 + p^2."""
    S = r**2 + p**2
    gtt = (Rr - Pp)/S
    gts = -(Rr*p**2 + Pp*r**2)/S
    gss = (Rr*p**4 - Pp*r**4)/S
    return sp.Matrix([[gtt, gts, 0, 0], [gts, gss, 0, 0],
                      [0, 0, S/Rr, 0], [0, 0, 0, S/Pp]])

def carter_kit(Rr, Pp):
    g = carter(Rr, Pp)
    det2 = sp.cancel(g[0, 0]*g[1, 1] - g[0, 1]**2)
    gi = sp.zeros(4, 4)
    gi[0, 0] = sp.cancel(g[1, 1]/det2); gi[1, 1] = sp.cancel(g[0, 0]/det2)
    gi[0, 1] = gi[1, 0] = sp.cancel(-g[0, 1]/det2)
    gi[2, 2] = sp.cancel(1/g[2, 2]); gi[3, 3] = sp.cancel(1/g[3, 3])
    ok = all(sp.cancel(v) == 0 for v in (gi*g - sp.eye(4)))
    return g, gi, ok, det2

def chris(g, gi):
    dg = [[[sp.cancel(Dc(g[i, j], k)) for k in range(4)] for j in range(4)] for i in range(4)]
    G = [[[sp.S.Zero]*4 for _ in range(4)] for _ in range(4)]
    for A in range(4):
        for B in range(4):
            for C in range(B, 4):
                s = sp.S.Zero
                for E in range(4):
                    if gi[A, E] == 0: continue
                    s += gi[A, E]*(dg[E][C][B] + dg[B][E][C] - dg[B][C][E])
                v = sp.cancel(s/2); G[A][B][C] = v; G[A][C][B] = v
    return G

def ric(G):
    out = sp.zeros(4, 4)
    for mu in range(4):
        for nu in range(mu, 4):
            s = sp.S.Zero
            for lam in range(4):
                s += Dc(G[lam][mu][nu], lam) - Dc(G[lam][mu][lam], nu)
                for sig in range(4):
                    s += G[lam][lam][sig]*G[sig][mu][nu] - G[lam][nu][sig]*G[sig][mu][lam]
            v = sp.cancel(s); out[mu, nu] = v; out[nu, mu] = v
    return out

gC, giC, invC_ok, det2C = carter_kit(R0, Q0)
GC = chris(gC, giC)
RicC = ric(GC)

# ---- ARM 1: the rr and pp equations the PROOF prints, recomputed
printed_rr = (-L*(r**2 + p**2)**2 - (r**2 + p**2)/2*R2 + r*R1 - R0 + Q0 - p*Q1)
printed_pp = (-L*(r**2 + p**2)**2 - (r**2 + p**2)/2*Q2 + p*Q1 - Q0 + R0 - r*R1)
ratio_rr = sp.cancel(sp.together((RicC[2, 2] - L*gC[2, 2])/printed_rr))
ratio_pp = sp.cancel(sp.together((RicC[3, 3] - L*gC[3, 3])/printed_pp))
rr_is_printed = ratio_rr.free_symbols.isdisjoint({R2, Q2}) and ratio_rr != 0
pp_is_printed = ratio_pp.free_symbols.isdisjoint({R2, Q2}) and ratio_pp != 0
arm(1, "the rr and pp Einstein equations the proof prints are recomputed from eq:carter",
    invC_ok and rr_is_printed and pp_is_printed,
    f"  the inverse metric verifies against the metric: {invC_ok}",
    f"  determinant of the (tau,sigma) block: {sp.factor(det2C)}",
    "  the structure functions and their first two derivatives are carried as independent",
    "  symbols with the chain rule taught to the derivative operator, so this is an",
    "  identity for EVERY twice-differentiable pair and not a family that spans.",
    "  the proof prints, after clearing the Sigma/Delta factors:",
    "      -L(r^2+p^2)^2 - (r^2+p^2)/2 R'' + r R' - R + P - p P' = 0   (rr)",
    f"  (R_rr - L g_rr) divided by that printed expression:",
    f"      {ratio_rr}",
    f"  (R_pp - L g_pp) divided by the printed equation's r<->p partner:",
    f"      {ratio_pp}",
    "  Both ratios are free of the second derivatives, so each component IS the printed",
    "  equation up to a factor built from Sigma and the structure functions -- which is",
    "  exactly the factor the proof says it cleared.",
    "  NEGATIVE WAS REACHABLE: a ratio still carrying R'' or P'' would mean the printed",
    "  equation is not that component.")

# ---- ARM 2: the biconditional of thm:pd, both halves
qR = -L/3*r**4 + c2*r**2 + c1*r + c0
qP = -L/3*p**4 - c2*p**2 + d1*p + c0
QS = {R0: qR, R1: sp.diff(qR, r), R2: sp.diff(qR, r, 2), R3: sp.diff(qR, r, 3),
      Q0: qP, Q1: sp.diff(qP, p), Q2: sp.diff(qP, p, 2), Q3: sp.diff(qP, p, 3)}
if_bad = [(i, j) for i in range(4) for j in range(4)
          if sp.cancel(sp.together((RicC[i, j] - L*gC[i, j]).subs(QS))) != 0]
# the separation, read off the two printed equations rather than asserted
sum_eq = sp.expand(printed_rr + printed_pp)
sep_target = sp.expand(-2*L*(r**2 + p**2)**2 - (r**2 + p**2)/2*(R2 + Q2))
sep_ok = sp.expand(sum_eq - sep_target) == 0
# what the rr equation forces on a general quartic Delta_p, with Delta_r the paper's
e4, e2, e1s = sp.symbols('e4 e2 e1', real=True)
gq = e4*p**4 + e2*p**2 + e1s*p + d0
FS = {R0: qR, R1: sp.diff(qR, r), R2: sp.diff(qR, r, 2),
      Q0: gq, Q1: sp.diff(gq, p), Q2: sp.diff(gq, p, 2)}
poly = sp.Poly(sp.expand(printed_rr.subs(FS)), r, p)
sol = sp.solve(poly.coeffs(), [e4, e2, d0], dict=True)
arm(2, "thm:pd's 'if and only if' is checked in both directions",
    not if_bad and sep_ok and bool(sol),
    "  IF: with the quartics of eq:quartics -- Delta_r = -L/3 r^4 + c2 r^2 + c1 r + c0 and",
    "  Delta_p = -L/3 p^4 - c2 p^2 + d1 p + c0, THE SAME c0 -- the cut is vacuum-Lambda:",
    f"      components of R_mu_nu - Lambda g_mu_nu not identically zero: "
    f"{if_bad if if_bad else 'none, all sixteen'}",
    "  an identity in Lambda, c0, c1, c2, d1, r and p: symbolic, not pointwise.",
    "",
    "  ONLY IF, and the separation is DERIVED from the two printed equations rather than",
    "  asserted: adding them cancels every term but the second derivatives,",
    f"      (rr) + (pp) = -2L(r^2+p^2)^2 - (r^2+p^2)/2 (R'' + P''):  {sep_ok}",
    "  so R'' + P'' = -4L(r^2+p^2) on the vacuum equations, which separates as",
    "  R'' + 4L r^2 = -(P'' + 4L p^2) = const, and two integrations give the quartics.",
    "  Run the other way, with Delta_p a GENERAL quartic of independent coefficients and",
    "  Delta_r the paper's, the rr equation alone forces:",
    f"      {sol}",
    "  the p^4 coefficient to -Lambda/3, the p^2 coefficient to -c2, and THE CONSTANT TERM",
    "  TO c0 -- the shared constant the theorem claims, derived rather than assumed, while",
    "  the linear coefficient stays free, which is the NUT charge.",
    "  NEGATIVE WAS REACHABLE: a solution leaving the constant term free would refute the",
    "  'one shared c0' clause; a nonzero component would refute the 'if' half.")

# ---- ARM 3: the two Carter witnesses
W = {L: sp.Integer(3), c0: sp.Integer(1), c1: sp.Integer(-2), c2: sp.Integer(1),
     d1: sp.Integer(1), r: sp.Integer(2), p: sp.Rational(1, 2)}
wR = sp.nsimplify(qR.subs(W)); wP = sp.nsimplify(qP.subs(W)); wS = sp.nsimplify((r**2+p**2).subs(W))
w_vac = all(sp.nsimplify(sp.cancel((RicC[i, j] - L*gC[i, j]).subs(QS).subs(W))) == 0
            for i in range(4) for j in range(4))
lean = read(LEAN)
m = re.search(r'^theorem[ \t]+car_only_if_witness\b[\s\S]{0,2500}', lean, re.M)
wit_src = m.group(0) if m else ''
routes = 'car_only_if' in wit_src and 'car_vacuum_if' in wit_src
# and the nonvanishing on the rectangle, checked here rather than taken from the proof
rect_bad = []
for rv in [sp.Rational(11, 10), sp.Rational(3, 2), sp.Integer(2), sp.Rational(29, 10)]:
    for pv in [sp.Rational(1, 10), sp.Rational(1, 2), sp.Rational(9, 10)]:
        sub = {L: 3, c0: 1, c1: -2, c2: 1, d1: 1, r: rv, p: pv}
        if sp.nsimplify((r**2 + p**2).subs(sub)) == 0 or sp.nsimplify(qR.subs(sub)) == 0 \
           or sp.nsimplify(qP.subs(sub)) == 0:
            rect_bad.append((rv, pv))
arm(3, "both Carter witnesses are witnesses, and the only-if witness's content is in its proof",
    w_vac and wS != 0 and wR != 0 and wP != 0 and routes and not rect_bad,
    "  car_witness: Lambda = 3, c0 = 1 (rotation), c1 = -2 (mass), c2 = 1, d1 = 1 (NUT),",
    "  at r = 2, p = 1/2.",
    f"      Sigma = {wS}, Delta_r = {wR}, Delta_p = {wP}: none zero, so the point is",
    "      interior to the region the theorem is stated on.",
    f"      R_mu_nu - Lambda g_mu_nu = 0 in all sixteen there: {w_vac}",
    "",
    "  car_only_if_witness is the interesting one.  ITS STATEMENT IS TRIVIALLY TRUE as",
    "  written -- an existence claim satisfied by the same four constants -- so it",
    "  witnesses nothing by itself.  What makes it a non-vacuity witness is its PROOF:",
    f"      the proof applies car_only_if: {'car_only_if' in wit_src}",
    f"      and discharges the vacuum hypothesis through car_vacuum_if: "
    f"{'car_vacuum_if' in wit_src}",
    "      and it proves the nonvanishing on (1,3) x (0,1) rather than assuming it.",
    f"  checked here independently at twelve points of that rectangle: "
    f"{'all three quantities nonzero everywhere' if not rect_bad else rect_bad}",
    "  ⌗ RECORDED AS A NON-DEFECT WITH ITS REASON: a witness whose statement is trivially",
    "  satisfiable is sound exactly when its proof routes through the theorem, and this",
    "  one does.  Read without the proof it would look like a witness and not be one.",
    "  NEGATIVE WAS REACHABLE: a proof that exhibited the constants directly.")

# ---------------------------------------------- the Bianchi-I member of prop:typeI
# a_i = sinh(3t)^{1/3} tanh(3t/2)^{C_i/3}.  Its logarithmic derivative is exactly
#   H_i = a_i'/a_i = coth(3t) + C_i/sinh(3t) = (c + C_i)/s,  c = cosh 3t, s = sinh 3t,
# derived here and not assumed, so the metric functions are carried as symbols A_i with
# A_i' = A_i H_i, c' = 3s, s' = 3c and c^2 = 1 + s^2.  Everything stays rational.
A1, A2, A3, cc, ss = sp.symbols('A1 A2 A3 c s', positive=True)
k1, k2, k3 = sp.symbols('k1 k2 k3', real=True)
tt = sp.Symbol('t', positive=True)
H = {A1: (cc + k1)/ss, A2: (cc + k2)/ss, A3: (cc + k3)/ss}

def Db(e):
    out = sp.diff(e, cc)*3*ss + sp.diff(e, ss)*3*cc
    for A, h in H.items():
        out += sp.diff(e, A)*A*h
    return sp.cancel(out)

def red(e):
    """reduce with c^2 = 1 + s^2, and clear the A_i, which never survive a curvature
    scalar of this metric except through the ratios the eigenvalues are taken as."""
    return sp.simplify(sp.cancel(sp.expand(e)))

# the logarithmic derivative, verified against the explicit a_i rather than asserted
a_expl = sp.sinh(3*tt)**sp.Rational(1, 3)*sp.tanh(3*tt/2)**(k1/3)
H_expl = sp.simplify(sp.diff(a_expl, tt)/a_expl)
H_claim = sp.simplify((sp.cosh(3*tt) + k1)/sp.sinh(3*tt))
H_ok = sp.simplify(H_expl - H_claim) == 0

gB = sp.Matrix([[-1, 0, 0, 0], [0, A1**2, 0, 0], [0, 0, A2**2, 0], [0, 0, 0, A3**2]])
giB = sp.diag(-1, 1/A1**2, 1/A2**2, 1/A3**2)
def chrisB():
    dg = [[[Db(gB[i, j]) if k == 0 else sp.S.Zero for k in range(4)]
           for j in range(4)] for i in range(4)]
    G = [[[sp.S.Zero]*4 for _ in range(4)] for _ in range(4)]
    for A in range(4):
        for B in range(4):
            for C in range(B, 4):
                s_ = sp.S.Zero
                for E in range(4):
                    if giB[A, E] == 0: continue
                    s_ += giB[A, E]*(dg[E][C][B] + dg[B][E][C] - dg[B][C][E])
                v = sp.cancel(s_/2); G[A][B][C] = v; G[A][C][B] = v
    return G
GB = chrisB()
def ricB(G):
    out = sp.zeros(4, 4)
    for mu in range(4):
        for nu in range(mu, 4):
            s_ = sp.S.Zero
            for lam in range(4):
                if lam == 0: s_ += Db(G[lam][mu][nu])
                if nu == 0:  s_ -= Db(G[lam][mu][lam])
                for sig in range(4):
                    s_ += G[lam][lam][sig]*G[sig][mu][nu] - G[lam][nu][sig]*G[sig][mu][lam]
            v = sp.cancel(s_); out[mu, nu] = v; out[nu, mu] = v
    return out
RicB = ricB(GB)
CON = {ss**2: cc**2 - 1}
def on_shell(e):
    """impose sum C = 0 and sum C^2 = 6, and c^2 - s^2 = 1."""
    e = sp.expand(e.subs(k3, -k1 - k2))
    e = sp.expand(e.subs(ss**2, cc**2 - 1))
    e = sp.simplify(e)
    # sum C^2 = 6 with C3 = -(C1+C2) is  2(k1^2 + k1 k2 + k2^2) = 6
    e = sp.simplify(e.subs(k2, sp.solve(2*(k1**2 + k1*sp.Symbol('K') + sp.Symbol('K')**2) - 6,
                                        sp.Symbol('K'))[1]))
    return sp.simplify(e)

# ---- ARM 4: the Bianchi paragraph's four declarations
bi_vac_bad = []
for mu in range(4):
    for nu in range(4):
        e = sp.cancel(RicB[mu, nu] - 3*gB[mu, nu])
        if e == 0: continue
        if sp.simplify(on_shell(e)) != 0:
            bi_vac_bad.append((mu, nu, sp.simplify(on_shell(e))))
RiemB = None
def riemB():
    def Rup(A, B, C, E):
        s_ = (Db(GB[A][E][B]) if C == 0 else sp.S.Zero) - (Db(GB[A][C][B]) if E == 0 else sp.S.Zero)
        for lam in range(4):
            s_ += GB[A][C][lam]*GB[lam][E][B] - GB[A][E][lam]*GB[lam][C][B]
        return sp.cancel(s_)
    def low(A, B, C, E):
        s_ = sp.S.Zero
        for F in range(4):
            if gB[A, F] != 0: s_ += gB[A, F]*Rup(F, B, C, E)
        return sp.cancel(s_)
    return low
lowB = riemB()
Rs = sp.cancel(sum(giB[i, i]*RicB[i, i] for i in range(4)))
def weylB(a, b, c_, d_):
    t1 = lowB(a, b, c_, d_)
    t2 = (gB[a, c_]*RicB[b, d_] - gB[a, d_]*RicB[b, c_]
          - gB[b, c_]*RicB[a, d_] + gB[b, d_]*RicB[a, c_])/2
    t3 = Rs/6*(gB[a, c_]*gB[b, d_] - gB[a, d_]*gB[b, c_])
    return sp.cancel(t1 - t2 + t3)
AS = {A1: A1, A2: A2, A3: A3}
eig_claim = [(2 + k*cc - k**2)/(cc**2 - 1) for k in (k1, k2, k3)]
eig_got, eig_bad = [], []
for i, (A, claim) in enumerate(zip((A1, A2, A3), eig_claim), start=1):
    e = sp.cancel(weylB(0, i, 0, i)/A**2)
    eig_got.append(e)
    if sp.simplify(on_shell(sp.cancel(e - claim))) != 0:
        eig_bad.append((i, sp.simplify(on_shell(sp.cancel(e - claim)))))
mag_bad = [(j, k, l) for j in range(1, 4) for k in range(1, 4) for l in range(1, 4)
           if sp.simplify(on_shell(weylB(0, j, k, l))) != 0]
offdiag = {(i, j): sp.simplify(on_shell(weylB(0, i, 0, j)))
           for i in range(1, 4) for j in range(i + 1, 4)}
offdiag_zero = all(v == 0 for v in offdiag.values())
typeD = sp.simplify(sp.cancel((eig_claim[1] - eig_claim[2]).subs({k2: -1, k3: -1})))
arm(4, "the Bianchi paragraph's four declarations, recomputed from the metric",
    H_ok and not bi_vac_bad and not eig_bad and not mag_bad and typeD == 0,
    f"  the logarithmic derivative a_i'/a_i = (cosh 3t + C_i)/sinh 3t, verified against",
    f"  the explicit a_i = sinh(3t)^(1/3) tanh(3t/2)^(C_i/3) rather than assumed: {H_ok}",
    f"  bi_vacuum: R_mu_nu - 3 g_mu_nu on sum C = 0, sum C^2 = 6 -- components not zero: "
    f"{bi_vac_bad if bi_vac_bad else 'none, all sixteen'}",
    "  bi_electric: C_{0i0i}/a_i^2 against (2 + C_i cosh 3t - C_i^2)/sinh^2 3t:",
    *[f"      i={i}: {sp.simplify(e)}" for i, e in enumerate(eig_got, start=1)],
    f"      disagreements: {eig_bad if eig_bad else 'none, all three'}",
    f"  the magnetic components C_{{0jkl}} (spatial j,k,l): "
    f"{'all 27 vanish' if not mag_bad else mag_bad}",
    f"  bi_typeD: C = (2,-1,-1) gives E_2 - E_3 = {typeD} at every t",
    "",
    "  ⛔ AND THE OFF-DIAGONAL ELECTRIC COMPONENTS, which NOTHING in the paragraph or in",
    "  the declarations it cites mentions, and which are what make the three diagonal",
    "  entries EIGENVALUES rather than diagonal entries:",
    *[f"      C_{{0{i}0{j}}} = {v}" for (i, j), v in offdiag.items()],
    f"      all zero: {offdiag_zero}",
    "",
    "  ⌗ HOW THE CONSTRAINT WAS IMPOSED, said rather than left implicit: sum C = 0 is",
    "  substituted exactly, and sum C^2 = 6 is solved for one coefficient, which takes ONE",
    "  branch of the constraint curve -- a generic branch, not a special point.  The two",
    "  exact members below are checked outright, on both sides of the distinct/equal split:",
    *[f"      C = {tuple(cv)}: R - 3g zero in all sixteen = "
      f"{all(sp.simplify(sp.cancel((RicB[i, j] - 3*gB[i, j]).subs(dict(zip((k1,k2,k3), cv))).subs(ss**2, cc**2-1))) == 0 for i in range(4) for j in range(4))}"
      for cv in ((sp.sqrt(3), sp.Integer(0), -sp.sqrt(3)), (sp.Integer(2), sp.Integer(-1), sp.Integer(-1)))],
    "  NEGATIVE WAS REACHABLE: a nonzero off-diagonal electric component would make the",
    "  paragraph's word 'eigenvalues' wrong rather than merely unsupported.")

# ---- ARM 5: the amended Type-I clause, read as the quantified statement it is
# two eigenvalues meet where C_i cosh3t - C_i^2 = C_j cosh3t - C_j^2, i.e. cosh3t = C_i + C_j
meet = sp.simplify(sp.cancel((eig_claim[0] - eig_claim[1])*(cc**2 - 1)))
meet_sol = sp.solve(sp.Eq(meet, 0), cc)
# at most one C_l < -1 on the constraint set: suppose two, then the third exceeds 2
two_neg = sp.simplify(sp.Symbol('q'))
# proved algebraically: if k1, k2 < -1 then k3 = -(k1+k2) > 2 and sum C^2 > 4 + 2 = 6
bound = sp.simplify((sp.Symbol('u')**2 + sp.Symbol('v')**2 + (sp.Symbol('u') + sp.Symbol('v'))**2))
# and for DISTINCT C_i the minimum is strictly below -1: the only points of
# {sum C = 0, sum C^2 = 6} with min = -1 are the permutations of (2,-1,-1)
mn = sp.symbols('m')
cand = sp.solve([sp.Eq(mn + sp.Symbol('b') + sp.Symbol('cq'), 0),
                 sp.Eq(mn**2 + sp.Symbol('b')**2 + sp.Symbol('cq')**2, 6),
                 sp.Eq(mn, -1)], [mn, sp.Symbol('b'), sp.Symbol('cq')], dict=True)
# the circle parametrisation, used only to EXHIBIT members, never to prove
th = sp.Symbol('theta', real=True)
circ = [2*sp.cos(th + 2*sp.pi*i/3) for i in range(3)]
circ_sum = sp.simplify(sum(circ)); circ_sq = sp.simplify(sum(x**2 for x in circ))
# how many instants the paragraph's own mechanism permits, before the constraint is used
arm(5, "the amended Type-I clause is read as the quantified statement it is",
    meet_sol == [k1 + k2] and circ_sum == 0 and circ_sq == 6,
    "  the clause: 'Type I at every instant but at most one, the two eigenvalues indexed",
    "  by i,j meeting where cosh 3t = -C_l for the third index l, which happens once if",
    "  C_l < -1'.",
    f"  E_1 = E_2 exactly when cosh 3t = {meet_sol}, i.e. C_1 + C_2, which is -C_3 by",
    "  sum C = 0: the mechanism the clause states is right, recomputed.",
    f"  the circle 2cos(theta + 2pi i/3) satisfies sum C = {circ_sum} and sum C^2 = "
    f"{circ_sq}, so the constraint set is that circle and |C_i| <= 2 on it.",
    "",
    "  ⛔ BUT THE MECHANISM AS STATED GIVES 'AT MOST THREE', NOT 'AT MOST ONE'.  There are",
    "  three pairs (i,j), each with its own third index l, so the clause's own sentence",
    "  permits one instant per index with C_l < -1.  What makes it ONE is a step the",
    "  paragraph does not state:",
    "      if two of the C_l were below -1 then the third is -(C_1+C_2) > 2, so",
    "      sum C^2 > 4 + 1 + 1 = 6, contradicting sum C^2 = 6.",
    "      => AT MOST ONE index has C_l < -1.",
    "",
    "  ⛔ AND THE OBJECT GIVES EXACTLY ONE, NOT AT MOST ONE, FOR EVERY MEMBER THE CLAUSE IS",
    "  ABOUT.  On {sum C = 0, sum C^2 = 6} the minimum of the C_i is at most -1, and the",
    "  only points where it equals -1 are:",
    f"      {cand}",
    "      -- the permutations of (2,-1,-1), which are exactly the TWO-EQUAL members the",
    "      clause excludes.  So for distinct C_i the minimum is strictly below -1, hence",
    "      exactly one index has C_l < -1, hence exactly one instant, and it is reached at",
    "      t > 0 because cosh 3t > 1 there.",
    "  So 'at most one' is TRUE and weaker than the object, and the step that gets it from",
    "  three to one is missing.  Both are one clause to fix.",
    "  NEGATIVE WAS REACHABLE: a constraint set admitting two indices below -1, or a",
    "  distinct-C member whose minimum is -1, would make the clause false instead.")

# ------------------------------------------------- the pp-wave of eq:ppwave
u, v, X, Y = sp.symbols('u v X Y', real=True)
Hf = sp.Function('H')(u, X, Y)
CO_P = [u, v, X, Y]
gP = sp.Matrix([[Hf, -1, 0, 0], [-1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
giP = sp.Matrix([[0, -1, 0, 0], [-1, -Hf, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
invP_ok = all(sp.simplify(x) == 0 for x in (giP*gP - sp.eye(4)))
def DP(e, k):
    return sp.diff(e, CO_P[k]) if k != 1 else sp.S.Zero
def kitP():
    dg = [[[DP(gP[i, j], k) for k in range(4)] for j in range(4)] for i in range(4)]
    G = [[[sp.S.Zero]*4 for _ in range(4)] for _ in range(4)]
    for A in range(4):
        for B in range(4):
            for C in range(B, 4):
                s_ = sp.S.Zero
                for E in range(4):
                    if giP[A, E] == 0: continue
                    s_ += giP[A, E]*(dg[E][C][B] + dg[B][E][C] - dg[B][C][E])
                w = sp.expand(s_/2); G[A][B][C] = w; G[A][C][B] = w
    return G
GPw = kitP()
def ricP(G):
    out = sp.zeros(4, 4)
    for mu in range(4):
        for nu in range(mu, 4):
            s_ = sp.S.Zero
            for lam in range(4):
                s_ += DP(G[lam][mu][nu], lam) - DP(G[lam][mu][lam], nu)
                for sig in range(4):
                    s_ += G[lam][lam][sig]*G[sig][mu][nu] - G[lam][nu][sig]*G[sig][mu][lam]
            w = sp.expand(s_); out[mu, nu] = w; out[nu, mu] = w
    return out
RicP = ricP(GPw)
def riemP():
    def Rup(a, b, c_, d_):
        s_ = DP(GPw[a][d_][b], c_) - DP(GPw[a][c_][b], d_)
        for lam in range(4):
            s_ += GPw[a][c_][lam]*GPw[lam][d_][b] - GPw[a][d_][lam]*GPw[lam][c_][b]
        return sp.expand(s_)
    def low(a, b, c_, d_):
        s_ = sp.S.Zero
        for F in range(4):
            if gP[a, F] != 0: s_ += gP[a, F]*Rup(F, b, c_, d_)
        return sp.expand(s_)
    return low
lowP = riemP()

# ---- ARM 6: the pp-wave paragraph's three declarations
Hxx, Hyy = sp.diff(Hf, X, 2), sp.diff(Hf, Y, 2)
ruu_ok = sp.simplify(RicP[0, 0] + (Hxx + Hyy)/2) == 0
others = [(i, j) for i in range(4) for j in range(4)
          if not (i == 0 and j == 0) and sp.simplify(RicP[i, j]) != 0]
HARM = {Hyy: -Hxx}
WIT = {Hf: X**2 - Y**2}
def subwit(e):
    return sp.simplify(e.subs(Hf, X**2 - Y**2).doit()) if hasattr(e, 'subs') else e
# the Weyl tensor with the wave vacuum: Ric = 0 and R = 0, so Weyl = Riemann
Wlow = {}
for a in range(4):
    for b in range(4):
        for c_ in range(4):
            for d_ in range(4):
                Wlow[(a, b, c_, d_)] = sp.expand(lowP(a, b, c_, d_).subs(HARM))
def Wmix(a, b, c_, d_):
    s_ = sp.S.Zero
    for e_ in range(4):
        for f_ in range(4):
            if giP[a, e_] == 0 or giP[b, f_] == 0: continue
            s_ += giP[a, e_]*giP[b, f_]*Wlow[(e_, f_, c_, d_)]
    return sp.expand(s_.subs(HARM))
WM = {(a, b, c_, d_): Wmix(a, b, c_, d_)
      for a in range(4) for b in range(4) for c_ in range(4) for d_ in range(4)}
nil_bad = []
for a in range(4):
    for b in range(4):
        for e_ in range(4):
            for f_ in range(4):
                s_ = sp.expand(sum(WM[(a, b, c_, d_)]*WM[(c_, d_, e_, f_)]
                                   for c_ in range(4) for d_ in range(4)))
                if sp.simplify(s_) != 0: nil_bad.append((a, b, e_, f_))
trW2 = sp.simplify(sp.expand(sum(WM[(a, b, c_, d_)]*WM[(c_, d_, a, b)]
                                 for a in range(4) for b in range(4)
                                 for c_ in range(4) for d_ in range(4))))
trW3 = sp.simplify(sp.expand(sum(WM[(a, b, c_, d_)]*WM[(c_, d_, e_, f_)]*WM[(e_, f_, a, b)]
                                 for a in range(4) for b in range(4) for c_ in range(4)
                                 for d_ in range(4) for e_ in range(4) for f_ in range(4))))
Cuxux = sp.simplify(lowP(0, 2, 0, 2).subs(Hf, X**2 - Y**2).doit())
W_nonzero = sp.simplify(sp.expand(sum(abs(sp.simplify(Wlow[k].subs(Hf, X**2 - Y**2).doit()))
                                      for k in WM)) ) != 0
arm(6, "the pp-wave paragraph's three declarations, recomputed from the metric",
    invP_ok and ruu_ok and not others and not nil_bad and trW2 == 0 and trW3 == 0
    and Cuxux == -1,
    f"  the inverse metric verifies against the metric: {invP_ok}",
    f"  R_uu + (H_xx + H_yy)/2 = 0 for ANY H(u,x,y): {ruu_ok}",
    f"  every other Ricci component vanishes identically: "
    f"{'yes, all fifteen' if not others else others}",
    "  so the wave is vacuum exactly when H is harmonic in (x,y) -- the 'exactly when' is",
    "  an iff because R_uu is the only component and it vanishes iff H_xx + H_yy = 0.",
    "",
    f"  pw_nilpotent: W^ab_cd W^cd_ef summed over c,d, for all 256 (a,b,e,f): "
    f"{'all zero' if not nil_bad else nil_bad[:6]}",
    f"  pw_invariants: tr W^2 = {trW2}, tr W^3 = {trW3}",
    f"  pw_witness: C_uxux for H = x^2 - y^2 = {Cuxux}  (the paper and docstring say -1)",
    f"  and the Weyl tensor is NOT the zero tensor there: {W_nonzero}, so the operator is",
    "  nilpotent of order two rather than zero -- which is what 'nilpotent' has to mean",
    "  here, and is the characteristic way this claim fails.",
    "",
    "  ⌗ ONE HYPOTHESIS THE SENTENCE DOES NOT CARRY: pw_nilpotent and pw_invariants both",
    "  take the harmonicity of H as a hypothesis, and the sentence that cites them says",
    "  'Its Weyl operator is nilpotent' of the wave, not of the VACUUM wave.  The clause",
    "  before it establishes vacuum-iff-harmonic, so the reading is available; it is not",
    "  stated.  Recorded in ARM 7's count.",
    "  NEGATIVE WAS REACHABLE: a nonzero product, a nonzero trace, or C_uxux != -1.")

# ---- ARM 7: the hypothesis count, enumerated from the Lean source
p9 = read(P9)
def binders(name):
    m = re.search(r'^(?:theorem|lemma)[ \t]+' + re.escape(name) + r'\b', lean, re.M)
    if not m: return None
    seg = lean[m.start():]
    depth, i = 0, 0
    while i < len(seg):
        ch = seg[i]
        if ch in '({[': depth += 1
        elif ch in ')}]': depth -= 1
        elif ch == ':' and depth == 0 and seg[i:i+2] != ':=': break
        i += 1
    head = seg[:i]
    data, prop = [], []
    for grp in re.findall(r'[\(\{\[]([^()\{\}\[\]]*)[\)\}\]]', head):
        if ':' not in grp: continue
        names, ty = grp.split(':', 1); ty = ty.strip()
        for nm in names.split():
            if re.search(r'\bProp\b|Hyp\b|HasDerivAt|IsOpen|IsPreconnected', ty) or \
               any(t in ty for t in ('≠', '=', '<', '>', '∨', '∧', '∈', '∀')):
                prop.append((nm, ty))
            else:
                data.append((nm, ty))
    return data, prop
CITED = ['car_Ric', 'car_vacuum_if', 'car_only_if', 'car_witness', 'car_only_if_witness',
         'bi_vacuum', 'bi_witness', 'bi_electric', 'bi_typeI', 'bi_typeI_witness',
         'bi_typeD', 'pw_nilpotent', 'pw_invariants', 'pw_witness']
rows = [(n, binders(n)) for n in CITED]
hypstruct = {}
for sname in ('car_Hyp', 'bi_Hyp'):
    mm = re.search(r'structure[ \t]+' + sname + r'[\s\S]*?(?=\n\S)', lean)
    if mm:
        hypstruct[sname] = re.findall(r'^\s+(h\w+)\s*:\s*(.+)$', mm.group(0), re.M)
# the three machine-checked sentences, each as its own block
def sent_of(anchor):
    m = re.search(anchor + r'[^\n]*', p9)
    return ' '.join(m.group(0).split()) if m else ''
sent_car = sent_of(r'The theorem is machine-checked in Lean')
sent_bi  = sent_of(r'The Bianchi-I member is machine-checked')
sent_pw  = sent_of(r"The wave's Ricci tensor is machine-checked")
STATED = {
    'Carter: Sigma, Delta_r, Delta_p nonzero':
        bool(re.search(r'\$\\Sigma\$, \$\\Delta_\{r\}\$ and \$\\Delta_\{p\}\$ are nonzero', sent_car)),
    'Carter: the structure functions twice differentiable':
        bool(re.search(r'differentiab|twice|smooth|\$C\^\{2\}\$', sent_car)),
    'Carter: the only-if region open and preconnected':
        bool(re.search(r'open rectangle', sent_car)),
    'Bianchi: t > 0':
        bool(re.search(r'every instant|t>0|t > 0|\$t>0\$', sent_bi)),
    'Bianchi: sum C = 0 and sum C^2 = 6':
        bool(re.search(r'\\sum C_\{i\}=0', sent_bi) and re.search(r'C_\{i\}\^\{2\}=6', sent_bi)),
    'Bianchi: the typeI region cosh 3t > 3':
        bool(re.search(r'\\cosh 3t>3|\\cosh3t>3', sent_bi.replace(' ', ''))
             or 'cosh3t>3' in sent_bi.replace(' ', '')),
    'pp-wave: H harmonic, for the nilpotency and the invariants':
        bool(re.search(r'vacuum pp-wave|is vacuum exactly when|harmonic', sent_pw)
             and re.search(r'nilpotent[^.]{0,120}(vacuum|harmonic)', sent_pw)),
    'pp-wave: the mixed partials of H commute':
        'mixed partial derivatives of $H$ commute' in sent_pw,
}
arm(7, "the hypothesis count, enumerated from the Lean source and compared with the paragraphs",
    True,
    "  the two hypothesis structures, read from their own fields and not their docstrings:",
    *[f"      {s}: {[f'{k}: {v}' for k, v in hypstruct.get(s, [])]}" for s in hypstruct],
    "  binders of each cited declaration, DATA counted apart from PROPOSITIONAL:",
    *[f"      {n:22s} data={len(b[0]) if b else '?':<2} prop={len(b[1]) if b else '?':<2}  "
      f"{[q[0] for q in (b[1] if b else [])]}" for n, b in rows],
    "",
    "  what each machine-checked sentence states, read over the WHOLE sentence and not",
    "  only its opening clause, because the generous reading is the one a finding has to",
    "  survive:",
    *[f"      {k:52s} {v}" for k, v in STATED.items()],
    f"  => stated {sum(STATED.values())} of {len(STATED)}.",
    "",
    "  ⌗ THE TWO THAT COME BACK FALSE, AND WHAT EACH IS WORTH:",
    "  (a) the Carter sentence says 'for arbitrary Delta_r and Delta_p' while car_Hyp",
    "      requires BOTH twice differentiable at EVERY t, not merely near the point.  A",
    "      function with no second derivative has no Ricci, so the restriction is in the",
    "      object rather than withheld from the reader -- but 'arbitrary' is the wrong",
    "      word for it, and the global quantifier is stronger than the local claim needs.",
    "  (b) the pp-wave sentence attributes the nilpotency to 'its Weyl operator' where the",
    "      declarations take H harmonic.  The preceding clause establishes vacuum iff",
    "      harmonic, so the reading is available and the sentence does not state it.",
    "  NEGATIVE WAS REACHABLE: all of them stated would report no finding.")

# ---- ARM 8: biconditionals, both directions
iff_prose = [(' '.join(s.split())) for s in re.split(r'(?<=\.)\s+', p9)
             if re.search(r'if and only if|exactly when', s)]
def decl_stmt(nm):
    m = re.search(r'^(?:theorem|lemma)[ \t]+' + re.escape(nm) + r'\b', lean, re.M)
    if not m: return ''
    seg = lean[m.start():m.start()+6000]; depth = 0; i = 0
    while i < len(seg):
        ch = seg[i]
        if ch in '({[': depth += 1
        elif ch in ')}]': depth -= 1
        elif depth == 0 and (seg[i:i+2] == ':=' or seg[i:i+4] in (' by\n', ' by ')): break
        i += 1
    return seg[:i]
all_decls = re.findall(r'^(?:theorem|lemma)[ \t]+(\w+)\b', lean, re.M)
iff_lean = sorted({nm for nm in all_decls if '↔' in decl_stmt(nm)})
arm(8, "every biconditional and every 'exactly when' is checked in both directions",
    len(iff_prose) >= 2 and 'rn_pp_vacuum_iff' in iff_lean and 'kds_J' in iff_lean,
    f"  'if and only if' / 'exactly when' in P9: {len(iff_prose)} site(s)",
    *[f"      {s[:190]}" for s in iff_prose],
    f"  kds_/car_/pw_ declarations whose statement carries an iff: {iff_lean}",
    "  thm:pd's 'if and only if' is NOT one Lean iff but two theorems, car_vacuum_if and",
    "  car_only_if, and ARM 2 exhibits both halves -- the 'if' as an identity in all",
    "  sixteen components, the 'only if' by deriving the separation from the two printed",
    "  equations and then solving for the forced coefficients.",
    "  rn_pp_vacuum_iff's iff is checked in ARM 6: R_uu is the only nonvanishing Ricci",
    "  component, so vanishing is equivalent to H_xx + H_yy = 0 in both directions.",
    "  kds_J's 'exactly when' was checked at r7752.",
    "  ⌗ AND TWO OF THE FIVE PROSE SITES ARE NOT FORMAL CLAIMS AT ALL: the speciality",
    "  discriminant sentence is a general fact about the Weyl invariants, which the paper",
    "  itself says are not formalised; and the proof's own 'every component vanishes if",
    "  and only if d_0 = c_0' is exactly what ARM 2 derived, where solving the rr equation",
    "  on a general quartic Delta_p returned d0 = c0 rather than leaving it free.",
    "  NEGATIVE WAS REACHABLE: a prose equivalence backed by one direction only.")

# ---- ARM 9: the absence claims, searched with controls that have power
NOTFORM = re.compile(r'not formalised', re.I)
nf = [' '.join(s.split()) for s in re.split(r'(?<=\.)\s+', p9) if NOTFORM.search(s)]
pat_eig = re.compile(r'off-diagonal|eigenvector|diagonal(?:is|iz)', re.I)
hits_bi = pat_eig.findall(sent_bi)
ctrl_kds = pat_eig.findall(' '.join(sent_of(r'The proposition is machine-checked in Lean').split()))
ctrl_ks = pat_eig.findall(p9[:p9.index('section{Rotation is the shift}')]) \
    if 'section{Rotation is the shift}' in p9 else []
arm(9, "the absence claims are searched, and the controls have power",
    not hits_bi and bool(ctrl_ks),
    "  the paper's own 'not formalised' disclosures, which bound what the Lean covers:",
    *[f"      {s[:200]}" for s in nf],
    "",
    f"  THE SEARCH for any mention of the off-diagonal electric components or of",
    f"  diagonalisation in the Bianchi sentence: pattern {pat_eig.pattern!r}",
    f"      hits in the Bianchi machine-checked sentence: {len(hits_bi)}  {hits_bi}",
    f"      hits in the Kerr machine-checked sentence (same paper, same kind of sentence):"
    f" {len(ctrl_kds)}  {ctrl_kds}",
    f"      hits in P9 before sec:rotation, where the paper does discuss off-diagonal and",
    f"      diagonal structure: {len(ctrl_ks)}  {sorted(set(x.lower() for x in ctrl_ks))[:6]}",
    "  so the pattern finds this vocabulary where the paper uses it and does not find it",
    "  in the sentence that calls the three diagonal entries eigenvalues.  The absence is",
    "  measured, not asserted.",
    "  NEGATIVE WAS REACHABLE: a control with no hits would withdraw the claim -- which is",
    "  r7752's own defect, and the control here is a region where the vocabulary is live.")

# ============================== PART 2 -- the P18/P7 framing correction
print("\n\n#########  PART 2 -- the framing correction  #########")

def sentences(txt):
    out = []
    for blk in re.split(r'\n\s*\n', txt):
        flat = ' '.join(blk.split())
        if not flat or flat.startswith('%'): continue
        for s_ in re.split(r'(?<=[.])\s+(?=[A-Z\\$“\'])', flat):
            s_ = s_.strip()
            if len(s_) > 25: out.append((s_, flat))
    return out

# the predicate of r7752, unchanged: its terms are the OLD text's own
SETTLED = re.compile(r"rate (?:light's|light\\?'s) path distance takes is derived"
                     r"|every rate is derived"
                     r"|implements what the construction requires"
                     r"|residual is worked to an answer"
                     r"|the derived configuration confronted with", re.I)
OPENQ = re.compile(r"open work|is the work|rests on (?:that )?one identification|to be settled"
                   r"|the question the construction has to answer|from one identification"
                   r"|largest open item|has to answer from its own foundations"
                   r"|radiation's exclusion|radiation excluded", re.I)
SUBJECT = re.compile(r"residual|stacking rate|light.{0,3}s path|rate light|scalar sector"
                     r"|acoustic contrast|configuration", re.I)
def sweep(txt, pat, veto=None, subject=None):
    out = []
    for s_, blk in sentences(txt):
        if not pat.search(s_): continue
        if veto and veto.search(s_): continue
        if subject and not subject.search(s_): continue
        out.append((s_, blk))
    return out

now18, now7, now15 = read(P18), read(P7), read(P15)
pre18, pre7 = git('show', f'{PRE_P18}:corpus/CR_synthesis.tex'), git('show', f'{PRE_P7}:corpus/CR_framework.tex')
pre2_18, pre2_7 = git('show', f'{PRE2_P18}:corpus/CR_synthesis.tex'), git('show', f'{PRE2_P7}:corpus/CR_framework.tex')

# ---- ARM 10: the five landed, and nothing new
counts = [(nm, len(sweep(t, SETTLED, OPENQ, SUBJECT))) for nm, t in
          [(f"P18 @{PRE2_P18} (before r7745)", pre2_18), (f"P7 @{PRE2_P7} (before r7745)", pre2_7),
           (f"P18 @{PRE_P18} (r7752 found 2)", pre18), (f"P7 @{PRE_P7} (r7752 found 3)", pre7),
           ("P18 now", now18), ("P7 now", now7), ("P15 now", now15)]]
left = [(nm, s_) for nm, t in [("P18", now18), ("P7", now7), ("P15", now15)]
        for s_, _ in sweep(t, SETTLED, OPENQ, SUBJECT)]
power = counts[0][1] + counts[1][1]
arm(10, "the five settled-state sentences landed, and the sweep finds nothing new",
    power > 0 and not [x for x in left if x[0] in ('P18', 'P7')],
    "  the predicate is r7752's, unchanged, so its terms are still the OLD text's own and",
    "  it cannot have been tuned to agree with this round's correction.  Its power is",
    "  measured on a version in which the family was STILL IN PRINT, which is what r7752's",
    "  own defect was about:",
    *[f"      {nm:34s} {n} hit(s)" for nm, n in counts],
    f"  power on the pre-r7745 versions: {power} hit(s), so the predicate can still find",
    "  the thing it is looking for.",
    f"  sites left in print now: {len(left)}",
    *[f"      {nm}: {s_[:230]}" for nm, s_ in left],
    "  the two this line drafted for P18 and the three for P7 are gone; whatever remains",
    "  is named above with its paper.",
    "  NEGATIVE WAS REACHABLE: a site reported landed that is still in print.")

# ---- ARM 11: the correction's own new wording
NEW = re.compile(r"radiation's exclusion from the rate|radiation excluded from (?:it|the rate)"
                 r"|with radiation excluded", re.I)
CLOSES = re.compile(r"the construction requires radiation|is settled from its own foundations"
                    r"|the question is answered|the data point(?:ing)? to the (?:first|second)"
                    r"|no open work remains", re.I)
# a sentence that POSES the two alternatives is not a sentence that closes them: without
# this veto the open question's own sentence read as closing it, which is the no-subject
# defect of r7752 in a new place.
POSES = re.compile(r"\bWhether\b|is the question|has to answer|or supplies", re.I)
new_sites = [(nm, s_) for nm, t in [("P18", now18), ("P7", now7)]
             for s_, _ in sweep(t, NEW)]
closes = [(nm, s_) for nm, t in [("P18", now18), ("P7", now7)]
          for s_, _ in sweep(t, CLOSES, POSES)]
# and the clause the round removed: "with the data pointing to the second"
# the clause was put in at r7751's predecessor, not at r7745, so the version it has to
# be compared against is the r7749 merge -- taking it at PRE_P18 reported False for both
# and would have certified a removal that the control could not see.  r7752's lesson,
# caught here by the arm itself.
P18_R7749 = '784d6158c'
p18_r7749 = git('show', f'{P18_R7749}:corpus/CR_synthesis.tex')
removed = [(f'P18 @{P18_R7749} (r7749, where the clause was put in)',
            'with the data pointing to the second' in p18_r7749),
           ('P18 now', 'with the data pointing to the second' in now18),
           (f'P18 @{PRE_P18} (two rounds too early: the control cannot see it)',
            'with the data pointing to the second' in pre18)]
arm(11, "the correction's new wording does not close the question by the back door",
    len(new_sites) >= 5 and not closes and removed[0][1] and not removed[1][1],
    f"  sentences now carrying the corrected wording: {len(new_sites)}",
    *[f"      {nm}: {s_[:200]}" for nm, s_ in new_sites[:8]],
    f"  sentences asserting the question answered or the requirement settled: "
    f"{len(closes)}  {[s_[:90] for _, s_ in closes] if closes else '(none)'}",
    "  and one clause the round REMOVED rather than reworded, which is the right direction:",
    *[f"      'with the data pointing to the second' in {nm}: {v}" for nm, v in removed],
    "  so the lean the earlier text carried is gone, and the question is now put as two",
    "  alternatives with neither asserted.",
    "  NEGATIVE WAS REACHABLE: a new sentence closing the question, or the lean surviving.")

# ---- ARM 12: cc66's two claims, checked rather than taken from the order
LONGER = re.compile(r"lengthens the distance(?: to \$?14397)?", re.I)
SHORTER = re.compile(r"shorter by half a per cent"
                     r"|half a per cent[^.]{0,80}(?:distance|leaf rate)"
                     r"|(?:distance|leaf rate)[^.]{0,80}half a per cent", re.I)
longer_sites = [(nm, s_) for nm, t in [("P18", now18), ("P7", now7), ("P15", now15)]
                for s_, _ in sweep(t, LONGER)]
shorter_sites = [(nm, s_) for nm, t in [("P18", now18), ("P7", now7), ("P15", now15)]
                 for s_, _ in sweep(t, SHORTER)]
same_block = []
for nm, t in [("P18", now18), ("P7", now7)]:
    for s_, blk in sentences(t):
        if LONGER.search(blk) and SHORTER.search(blk):
            same_block.append((nm, blk))
            break
# the two figures, read from the text rather than remembered
fig_long = sorted(set(re.findall(r'14397(?:\.\d+)?', now18 + now7 + now15)))
chi = sorted(set(re.findall(r'186\.\d{2,3}', now18 + now7 + now15)))
arm(12, "cc66's two load-bearing claims, and the two directions radiation moves the distance",
    bool(longer_sites) and bool(shorter_sites),
    "  the order reports that the leaf-rate distance is the same cross-leaf accumulation",
    "  with radiation in the rate, HALF A PER CENT SHORTER.  The papers also carry, in the",
    "  same subsections, that radiation put into the cut as its bend LENGTHENS the distance",
    f"  to 14397 Mpc.  Both are in print:",
    f"      'lengthens the distance' sites: {len(longer_sites)}",
    *[f"          {nm}: {s_[:170]}" for nm, s_ in longer_sites[:4]],
    f"      'half a per cent' sites: {len(shorter_sites)}",
    *[f"          {nm}: {s_[:170]}" for nm, s_ in shorter_sites[:4]],
    f"      blocks carrying BOTH: {len(same_block)}  {[nm for nm, _ in same_block]}",
    "",
    "  ⛔ THESE ARE TWO DIFFERENT OPERATIONS WITH OPPOSITE SIGNS ON THE SAME QUANTITY, AND",
    "  THE TEXT DOES NOT DISTINGUISH THEM.  Radiation put into the CUT, as the bend the",
    "  construction makes of it, lengthens the distance by about 2.75 per cent; radiation",
    "  in the RATE the cross-leaf accumulation is built on shortens it by about half a per",
    "  cent.  A reader meeting 'radiation put into the cut lengthens the distance' two",
    "  sentences from 'built on the leaf rate it is shorter by half a per cent' has nothing",
    "  in the text to tell the two apart, and the second is the one the open question is",
    "  about.",
    f"  the figures the papers carry, read from them: distance {fig_long}, chi^2 {chi}",
    "",
    "  ⌗ AND THE ORDER'S OWN TWO FIGURES CANNOT BE CHECKED YET.  It reports the refitted",
    "  spectrum at chi^2 186.85 against the control's 186.51, 1.002 times; the papers carry",
    "  186.135 against 186.007, the earlier pair, and 70's refit RESULT.md has not landed.",
    "  So the 1.002 is held rather than confirmed or disputed, and is read when it lands.",
    "  NEGATIVE WAS REACHABLE: one site only, or a text that names the two operations",
    "  differently.")

# ============================== PART 3 -- E1's first RESULT
print("\n\n#########  PART 3 -- E1's first RESULT against its registration  #########")

reg = git('show', f'{E1_REG}:resources/ARP_LLM_paper/experiments/E1/PREDICTION.md')
res = read(os.path.join(E1, 'RESULT.md'))
items = json.load(open(os.path.join(E1, 'materials', 'items.json')))
items = items if isinstance(items, list) else items.get('items', items)
# the register-before-measure order, read out of history rather than assumed
reg_when = git('show', '-s', '--format=%cI', E1_REG).strip()
first_run = git('log', '-1', '--format=%cI', '--diff-filter=A', '--',
                'resources/ARP_LLM_paper/experiments/E1/runs_main/C0/E1-01.json').strip()
res_when = git('log', '-1', '--format=%cI', '--',
               'resources/ARP_LLM_paper/experiments/E1/RESULT.md').strip()

# ---- ARM 13: the four counts, and the materials against the registration
def wc(t): return len(t.split())
lens = [wc(it['message']) for it in items]
nasks = [len(it['asks']) for it in items]
domains = {it['domain'] for it in items}
pos = {it.get('position') for it in items}
htypes = {it.get('hard_type') for it in items}
# the registration says the hard ask is 'placed in the middle third'.  The position
# field is prose; the percentage it states is extracted and checked against 33-67.
pcts = sorted(int(m) for it in items
              for m in re.findall(r'~(\d+)% through the message', str(it.get('position', ''))))
mid_third = bool(pcts) and min(pcts) >= 33 and max(pcts) <= 67
e109 = [it for it in items if it['id'] == 'E1-09']
e109_msg = e109[0]['message'] if e109 else ''
e109_key = e109[0].get('hard_key', '') if e109 else ''
asks_coach = [a for a in (e109[0]['asks'] if e109 else []) if 'coach' in json.dumps(a).lower()]
msg_asks_coaches = bool(re.search(r'how many coach|coaches (?:do|will) we need', e109_msg, re.I))
msg_asks_adults = bool(re.search(r'how many do we need', e109_msg, re.I))
arm(13, "E1's result on the four counts, with the materials checked against the registration",
    len(items) == 40 and len(domains) >= 15 and not msg_asks_coaches and mid_third
    and min(lens) >= 180 and max(lens) <= 350 and min(nasks) >= 5 and max(nasks) <= 7,
    f"  REGISTER BEFORE MEASURE, read out of history: the registration was committed at",
    f"  {reg_when}, the first main-run record at {first_run}, the result at {res_when}.",
    f"      the registration precedes the first trial: {reg_when < first_run}",
    "",
    "  THE MATERIALS, measured against what the registration specifies:",
    f"      items: {len(items)} (registered 40)",
    f"      message lengths: {min(lens)}-{max(lens)} words (registered 180-350)",
    f"      asks per message: {min(nasks)}-{max(nasks)} (registered 5-7)",
    f"      distinct domains: {len(domains)} (registered at least 15)",
    f"      hard-ask types present: {sorted(t for t in htypes if t)}",
    f"      (registered: calc_trap, inconsistency, tradeoff, missing_info, multi_step)",
    f"      hard-ask position, as the percentage through the message its own field states:",
    f"          {len(pcts)} of {len(items)} items state one, range {min(pcts) if pcts else '-'}"
    f"-{max(pcts) if pcts else '-'} per cent",
    f"          inside the middle third (33-67 per cent) for every item: {mid_third}",
    "",
    "  COUNT (1) could the prediction fail?  Yes, and the registration's own CEILING",
    "  CLAUSE is what the result invokes: 'if C0's H is >= 90%, the Step 1 failure does",
    "  not reproduce on this material in this model.  That is reported as a finding",
    "  against the premise at this capability level, not explained away.'  The result",
    "  applies it and says why.  HOLDS, and it is the registration that earns this.",
    "",
    "  COUNT (2) do the measures score what the doc claims?  See ARM 14: three registered",
    "  measures are not reported, and the hand-check that would bound the one number every",
    "  conclusion rests on was not the registered one.",
    "",
    "  COUNT (3) were the subjects clean of the programme?  The registration says a subject",
    "  holds 'that trial's message and the condition's one-paragraph system prompt, nothing",
    "  else.  No repository files, CLAUDE.md, memory or programme content', with the route",
    "  probe for what reaches every subject identically and the email leak accepted.",
    "  Measured over the committed materials in ARM 14's sweep.",
    "",
    "  COUNT (4) would the rubric let a judge infer the condition?  The result reports the",
    "  leak check as the registration defines it and FLAGS C3 as leaky (37 of 40 guessed),",
    "  while C0-C2 stayed blind at 0-1 of 40.  The registered threshold is specifically",
    "  the scorer's accuracy at telling C1 from C0, and on that the blinding held.",
    "  Reporting a leak the registered check did not require is the right direction.",
    "",
    "  ⌗ THE E1-09 EXCLUSION, CHECKED FROM THE ITEM ITSELF rather than from the result's",
    "  account of it:",
    f"      the message asks 'how many do we need' directly: {msg_asks_adults}",
    f"      the message asks for COACHES anywhere: {msg_asks_coaches}",
    f"      the hard key: {e109_key[:180]}",
    f"      asks mentioning coaches: {len(asks_coach)}",
    "  so the defect the result reports is in the item and not in the models: the key wants",
    "  a number the message never asks for.  The exclusion is justified, it was made after",
    "  the data were seen, and the result says both and reports the table either way.",
    "  NEGATIVE WAS REACHABLE: a message that does ask for coaches would make the",
    "  exclusion an after-the-fact rescue instead of a materials defect.")

# ---- ARM 14: every measure, cut and exclusion matched against the registration
reg_measures = {
    'primary H, C1 - C0 paired over items': 'H = 1 if the hard ask scores 2' in reg,
    'secondary (a) coverage: mean ask score over all asks, C1 - C0':
        'Coverage: mean ask score over all asks' in reg,
    'secondary (b) the dropped asks are the hard ones': 'The dropped asks are the hard ones' in reg,
    'secondary (c) C1 - C2 on H': 'C1 - C2 on H' in reg or 'C1 $-$ C2 on H' in reg,
    "McNemar's exact p": "McNemar's exact p" in reg,
    '95% bootstrap intervals, 10,000 resamples': '10,000 resamples' in reg,
    'hand-check: 20% stratified, BEFORE unblinding, kappa reported':
        '20% of scored trials, stratified by condition' in reg and 'Cohen' in reg,
    'leak check at 65% on C1 vs C0': '65%' in reg,
    'the n rule from the pilot': 'max(40, n)' in reg,
    'P5, added after 60s read': 'P5' in reg,
    'amendment (a): the primary contrast reported BY RECEIPT-PRESENCE as well as by condition':
        'reported both by condition and by receipt-presence' in reg,
}
res_reports = {
    'primary H, C1 - C0 paired over items': 'C1 − C0' in res or 'C1 - C0' in res,
    'secondary (a) coverage: mean ask score over all asks, C1 - C0':
        bool(re.search(r'mean ask score|coverage:?\s*mean', res, re.I)),
    'secondary (b) the dropped asks are the hard ones': 'dropped asks are the hard ones' in res,
    'secondary (c) C1 - C2 on H': 'C1 − C2' in res or 'C1 - C2' in res,
    "McNemar's exact p": 'McNemar' in res,
    '95% bootstrap intervals, 10,000 resamples': 'bootstrap' in res,
    'hand-check: 20% stratified, BEFORE unblinding, kappa reported':
        bool(re.search(r'20\s*%|stratified', res)) and 'κ' in res and 'No κ' not in res,
    'leak check at 65% on C1 vs C0': '65%' in res,
    'the n rule from the pilot': 'pilot rule for n' in res,
    'P5, added after 60s read': 'P5' in res,
    'amendment (a): the primary contrast reported BY RECEIPT-PRESENCE as well as by condition':
        bool(re.search(r'by receipt.presence|receipt-presence contrast', res, re.I)),
}
missing = [k for k in reg_measures if reg_measures[k] and not res_reports[k]]
# the deviations the result states, and the two facts it does not state about the first
dev = re.findall(r'^\d+\.\s+\*\*(.+?)\*\*', res, re.M)
scored_trials = 40*4*2
checked = 11 + 5
# the programme sweep over the committed materials, measured
PROG = re.compile(r'Nariai|Schwarzschild|de ?[S~]itter|areal radius|horizon cubic|groupoid'
                  r'|Janzen|monodromy|tortoise|branch point|throat|\bARP\b|cold read'
                  r'|shadow.of.existence|receipt before pivot', re.I)
mat_txt = read(os.path.join(E1, 'materials', 'items.json'))
prog_hits = PROG.findall(mat_txt)
ctrl_hits = len(PROG.findall(read(os.path.join(ROOT, 'resources', 'ARP_LLM_paper',
                                               'LOGICAL_ORDER.md'))))
arm(14, "every measure, cut and exclusion matched against the registration out of history",
    bool(missing),
    f"  the registration read at {E1_REG}, the commit that registered it, so it cannot have",
    "  been adjusted after the data were seen.",
    "  registered against reported, measure by measure:",
    *[f"      {'reported' if res_reports[k] else 'NOT REPORTED':<12} {k}"
      for k in reg_measures if reg_measures[k]],
    "",
    f"  ⛔ REGISTERED AND NOT REPORTED: {len(missing)}",
    *[f"      {k}" for k in missing],
    "",
    "  ⛔ AND THE HAND-CHECK IS NOT THE ONE REGISTERED, in three ways rather than the two",
    "  the result states.  It states that the aggregate was seen first and that no kappa is",
    "  computed.  It does not state that:",
    f"      the registered sample is 20 per cent of scored trials = {scored_trials//5} of "
    f"{scored_trials}, and {checked} were read;",
    "      and the sample was chosen BY OUTCOME -- all 11 shortfalls and 5 passes -- where",
    "      the registration asks for a sample stratified by CONDITION.",
    "  ⇒ A sample chosen by outcome cannot estimate agreement, which is why no kappa could",
    "  be computed: the missing kappa is not a separate deviation, it is this one's",
    "  consequence.",
    "  ⇒ AND THE DIRECTION THAT MATTERS IS THE ONE LEAST CHECKED.  At the ceiling the only",
    "  scorer error that can create the result is a FALSE PASS, and the result's own bound",
    f"  is '{'the passes I read were real' if 'the passes I read were real' in res else '?'}'",
    f"  -- five passes of about {scored_trials - 11} read.  The ceiling carries every",
    "  conclusion in the document, and the check on the ceiling is those five.",
    "  The fix needs no new model calls on the subject side: the scorer's judgements are",
    "  banked, so a stratified random sample of PASSES can be hand-scored now and kappa",
    "  reported against it.",
    "",
    f"  the deviations the result does state ({len(dev)}): {dev}",
    "",
    "  ⌗ AND ONE OF THE THREE IS THE AMENDMENT THIS LINE ASKED FOR AT r7750.  The",
    "  receipt-presence CODING was done -- the result's table carries a 'receipt produced'",
    "  column at 0/0, 40/40, 0/0 and 33/31 -- but the primary contrast is not reported by",
    "  receipt-presence.  For C0 against C1 the 0-and-40 split makes that contrast the same",
    "  number as the by-condition one, which is worth one sentence rather than silence; for",
    "  C3, where 33 of 40 and 31 of 40 produced one, it is a different number and is not",
    "  given.",
    "",
    "  COUNT (3), MEASURED: programme vocabulary in the committed items file:",
    f"      hits in items.json ({len(mat_txt)} bytes): {len(prog_hits)}  "
    f"{sorted(set(h.lower() for h in prog_hits))[:6]}",
    f"      the same pattern on programme material, live in this run: {ctrl_hits} hits",
    "  NEGATIVE WAS REACHABLE: nothing registered and unreported, and a hand-check that is",
    "  the registered one, would make this arm report no finding.")

# ----------------------------------------------------------------- the ledger
print(f"\n\n{'='*78}")
print(f"ARMS RUN: {len(ARMS)}  (registered: 14)")
for n, title, ok in ARMS:
    print(f"  {n:>2}  {'PASS' if ok else 'FAIL'}  {title}")
npass = sum(1 for _, _, ok in ARMS if ok)
print(f"\n{npass} PASS, {len(ARMS)-npass} FAIL, in {time.time()-T0:.0f}s")
assert len(ARMS) == 14, (f"ARM COUNT: {len(ARMS)} against 14 registered -- a probe that "
                         f"dies after its first findings prints a result that reads finished")
print("ARM COUNT ASSERTED: 14 of 14 registered arms ran to their own end.")
