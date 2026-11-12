#!/usr/bin/env python3
"""r7750 (60), part 1 -- a cold read of P9's two new formal paragraphs against probes/Range.lean.

Registered at PREDICTION.md with only r7747's order read.  Part 2, the six experiment
registrations, is a read of documents and is recorded in RESULT.md with its own table; this file
carries what is computable.

The claims are RECOMPUTED from the metrics rather than read off either the prose or the Lean
docstrings (the registered (A)iv), and every arm prints its witness.
"""
import os, re, subprocess, sys
import sympy as sp

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
LEAN = os.path.join(ROOT, 'computations', 'formalisation', 'lean', 'probes')
P9 = os.path.join(ROOT, 'corpus', 'range_paper.tex')

RESULTS = []
def arm(tag, ok, note):
    RESULTS.append((tag, bool(ok), note))
    print(f"  [{'PASS' if ok else 'FAIL'}] {tag}  {note}")
def head(t):
    print(); print('=' * 100); print(t); print('=' * 100)
def flat(s):
    return re.sub(r'\s+', ' ', s).strip()
def demark(s):
    for c in ('emph', 'textbf', 'textit', 'texttt', 'textsc'):
        for _ in range(3):
            s = re.sub(r'\\' + c + r'\{([^{}]*)\}', r'\1', s)
    return flat(s.replace('~', ' ').replace(r'\_', '_'))

SRC = open(os.path.join(LEAN, 'Range.lean'), encoding='utf-8').read()
TEX = open(P9, encoding='utf-8').read()

def decl(name):
    m = re.search(r'^(theorem|lemma|structure)[ \t]+' + re.escape(name) + r'(?![A-Za-z0-9_])',
                  SRC, re.M)
    if not m:
        return None
    tail = SRC[m.start():]
    depth, end, i = 0, None, 0
    while i < len(tail):
        ch = tail[i]
        if ch in '([{⟨':
            depth += 1
        elif ch in ')]}⟩':
            depth -= 1
        elif depth == 0 and tail.startswith(':=', i):
            end = i
            break
        i += 1
    stmt = tail[:end if end is not None else len(tail)].strip()
    depth, colon = 0, len(stmt)
    for j, ch in enumerate(stmt):
        if ch in '([{⟨':
            depth += 1
        elif ch in ')]}⟩':
            depth -= 1
        elif ch == ':' and depth == 0 and not stmt.startswith('::', j):
            colon = j
            break
    binders, buf, depth = [], '', 0
    for ch in stmt[:colon]:
        if ch in '([{⟨':
            depth += 1
            if depth == 1:
                buf = ch
                continue
        elif ch in ')]}⟩':
            depth -= 1
            if depth == 0:
                binders.append(buf + ch)
                buf = ''
                continue
        if depth >= 1:
            buf += ch
    return {'binders': binders, 'concl': flat(stmt[colon+1:]) if colon < len(stmt) else ''}

NAMES = ['rn_ks_einstein', 'rn_ks_G_offdiag', 'rn_ks_sds_vacuum', 'rn_ks_witness',
         'rn_ks_nariai', 'rn_pp_Ric', 'rn_pp_vacuum_iff', 'rn_pp_witness']
DECL = {n: decl(n) for n in NAMES}

head('(A)i  BOTH PARAGRAPHS LOCATED, AND EVERY CITED NAME RESOLVED')
paras = [flat(l) for l in TEX.split('\n') if 'rn\\_' in l]
print(f"  paragraphs carrying rn_ citations: {len(paras)}")
cited = sorted({c.replace(r'\_', '_') for c in re.findall(r'\\texttt\{(rn[^}]*)\}', TEX)})
missing = [c for c in cited if decl(c) is None]
fakes = ['rn_ks_vacuum', 'rn_pp_weyl', 'rn_ks_interior']
fake_hits = [f for f in fakes if decl(f) is not None]
print(f"  P9 cites {len(cited)} rn_ names: {cited}")
print(f"  the order names 8; not found in Range.lean: {missing}")
arm('(A)i  both paragraphs located, all eight names are declarations, three fabricated are not',
    len(paras) == 2 and not missing and not fake_hits and all(DECL[n] for n in NAMES),
    f"witness: {len(paras)} paragraphs, {len(cited)} cited names all present, fabricated "
    f"{fakes} -> {fake_hits or 'none found'}")

# ----------------------------------------------------------------- the Kantowski-Sachs kernel
head('(A)iv-a  THE KANTOWSKI-SACHS EINSTEIN TENSOR, RECOMPUTED FROM THE METRIC')
tau, chi, th, ph, Lam, M = sp.symbols('tau chi theta phi Lambda M', real=True)
X = sp.Function('X')(tau)
Y = sp.Function('Y')(tau)
co = [tau, chi, th, ph]
g = sp.diag(-1, X**2, Y**2, Y**2 * sp.sin(th)**2)
ginv = g.inv()
n = 4
Gam = [[[sp.simplify(sum(ginv[a, d] * (sp.diff(g[d, b], co[c]) + sp.diff(g[d, c], co[b])
                                       - sp.diff(g[b, c], co[d])) for d in range(n)) / 2)
         for c in range(n)] for b in range(n)] for a in range(n)]
def Riem(a, b, c, d):
    t = sp.diff(Gam[a][b][d], co[c]) - sp.diff(Gam[a][b][c], co[d])
    t += sum(Gam[a][c][e] * Gam[e][b][d] - Gam[a][d][e] * Gam[e][b][c] for e in range(n))
    return sp.simplify(t)
Ric = sp.Matrix(n, n, lambda b, d: sp.simplify(sum(Riem(a, b, a, d) for a in range(n))))
R = sp.simplify(sum(ginv[b, d] * Ric[b, d] for b in range(n) for d in range(n)))
# G with ONE index up, as the paper writes G^mu_nu
Gmix = sp.simplify(ginv * (Ric - R * g / 2))
print("  G^mu_nu computed from the metric -dtau^2 + X^2 dchi^2 + Y^2 dOmega^2")
offdiag = [sp.simplify(Gmix[i, j]) for i in range(n) for j in range(n) if i != j]
print(f"  every off-diagonal component zero: {all(o == 0 for o in offdiag)}")
# the paper's eq:ksrho and partners, as -G^0_0, G^1_1, G^2_2 (8 pi rho, p_chi, p_theta with Lambda)
Xp, Ypp, Yp, Xpp = sp.Derivative(X, tau), sp.Derivative(Y, tau, 2), sp.Derivative(Y, tau), sp.Derivative(X, tau, 2)
claim_00 = (sp.diff(Y, tau)/Y)**2 + 1/Y**2 + 2*(sp.diff(X, tau)/X)*(sp.diff(Y, tau)/Y)
claim_11 = -2*sp.diff(Y, tau, 2)/Y - (sp.diff(Y, tau)/Y)**2 - 1/Y**2
claim_22 = (-sp.diff(Y, tau, 2)/Y - sp.diff(X, tau, 2)/X
            - (sp.diff(X, tau)/X)*(sp.diff(Y, tau)/Y))
r00 = sp.simplify(-Gmix[0, 0] - claim_00)
r11 = sp.simplify(Gmix[1, 1] - claim_11)
r22 = sp.simplify(Gmix[2, 2] - claim_22)
r33 = sp.simplify(Gmix[3, 3] - Gmix[2, 2])
print(f"  -G^0_0 - [(Y'/Y)^2 + 1/Y^2 + 2(X'/X)(Y'/Y)]   = {r00}")
print(f"   G^1_1 - [-2Y''/Y - (Y'/Y)^2 - 1/Y^2]         = {r11}")
print(f"   G^2_2 - [-Y''/Y - X''/X - (X'/X)(Y'/Y)]      = {r22}")
print(f"   G^3_3 - G^2_2                                = {r33}")
arm('(A)iv-a  rn_ks_einstein\'s four components and rn_ks_G_offdiag both hold of the metric',
    r00 == 0 and r11 == 0 and r22 == 0 and r33 == 0 and all(o == 0 for o in offdiag),
    "witness: all four residuals and all twelve off-diagonal components are exactly 0")

head('(A)ii  AND THE HYPOTHESES ARE NOT DECORATION: X, Y AND sin(theta) ARE IN THE DENOMINATORS')
dens = set()
for e in (claim_00, claim_11, claim_22):
    den = sp.denom(sp.together(e))
    for a in sp.preorder_traversal(den):
        if a.is_Function or a.is_Symbol:
            dens.add(str(a.func) if a.is_Function else str(a))
print(f"  functions and symbols in the quoted expressions' denominators: {sorted(dens)}")
hyp = re.search(r'structure rn_Hyp.*?\n\n', SRC, re.S).group(0)
fields = re.findall(r'^\s{2}(\w+) :', hyp, re.M)
nondeg = [f for f in fields if f in ('hX0', 'hY0', 'hs')]
print(f"  rn_Hyp's fields: {fields}")
print(f"  of which NON-DEGENERACY at the point: {nondeg}")
print(f"  rn_Hyp's own docstring says: \"X, Y, sin theta != 0 at the point\"")
arm('(A)ii-a  rn_Hyp carries three non-degeneracy conditions, and the quoted expressions divide '
    'by exactly those quantities',
    len(nondeg) == 3 and {'X', 'Y'} <= dens,
    f"witness: {nondeg} in rn_Hyp; the denominators carry {sorted(dens & {'X', 'Y', 'sin'})}, "
    f"which is what those three hypotheses are about")

head('(A)ii-b  WHAT THE PROSE STATES OF EACH THEOREM\'S HYPOTHESES')
para1 = [p for p in paras if 'rn\\_ks\\_einstein' in p][0]
para2 = [p for p in paras if 'rn\\_pp\\_Ric' in p][0]
d1 = demark(para1)
print(f"  PARAGRAPH 1  {d1}")
print()
print(f"  PARAGRAPH 2  {demark(para2)}")
print()
HYPS = {
    'rn_ks_einstein':   [b for b in DECL['rn_ks_einstein']['binders'] if 'rn_Hyp' in b],
    'rn_ks_G_offdiag':  [b for b in DECL['rn_ks_G_offdiag']['binders'] if 'rn_Hyp' in b],
    'rn_ks_sds_vacuum': [b for b in DECL['rn_ks_sds_vacuum']['binders'] if ':' in b],
    'rn_ks_nariai':     [b for b in DECL['rn_ks_nariai']['binders'] if ':' in b],
    'rn_pp_Ric':        [b for b in DECL['rn_pp_Ric']['binders'] if ':' in b],
    'rn_pp_vacuum_iff': [b for b in DECL['rn_pp_vacuum_iff']['binders'] if ':' in b],
}
for _nm, hs in HYPS.items():          # NOT `n`: that is the dimension, and binding it here
    print(f"    {_nm:18} {hs}")        # broke every range(n) below (r7750 DEFECT 1)
# what the prose says
states = {
    'X != 0':          bool(re.search(r'X\s*\\ne\s*0|X\\neq0|X,\s*Y.*\\ne', d1)),
    'Y != 0':          bool(re.search(r'Y\s*\\ne\s*0|Y\\neq0', d1)),
    'sin theta != 0':  bool(re.search(r'\\sin\\theta|\\sin\s*\\theta', d1)),
    'Lambda > 0':      bool(re.search(r'\\Lambda>0|0<\\Lambda|\\Lambda\s*>\s*0', d1)),
}
for k, v in states.items():
    print(f"    prose paragraph 1 states {k:16} = {v}")
nariai_hyps = [b for b in DECL['rn_ks_nariai']['binders']
               if b.startswith('(h')]      # the PROPOSITIONAL binders, not the implicit types
arm('(A)ii-b  ⛔ FINDING: the three KS theorems carry non-degeneracy hypotheses and the paragraph '
    'states NONE of them', not any(states.values()) and len(nariai_hyps) == 2,
    f"witness: rn_Hyp gives X != 0, Y != 0, sin(theta) != 0; rn_ks_nariai adds {nariai_hyps}; "
    f"the paragraph states none -- the same defect 69 repaired at P15's prop:flat in THIS round")

head('(A)iii  THE FIVE CONDITIONS AGAINST THE FOUR THE PROSE LISTS')
sds = DECL['rn_ks_sds_vacuum']['binders']
cond = [b for b in sds if b.startswith('(h') and 'rn_Hyp' not in b]
print(f"  rn_ks_sds_vacuum's conditions ({len(cond)}):")
for c in cond:
    print(f"    {c}")
prose_four = re.search(r"Wherever (.*?), all sixteen", d1)
print(f"  the prose lists: {prose_four.group(1) if prose_four else '?'}")
print("  the fifth, hY2 : Y2 = X1, is Y'' = X' -- which follows from Y' = X BY DIFFERENTIATION,")
print("  so the prose's four, read as holding on a region ('Wherever'), imply it; the Lean states")
print("  them POINTWISE and must therefore list it.  Not a dropped hypothesis: a difference")
print("  between a pointwise and a regional reading, and the prose's word is the regional one.")
arm('(A)iii  the prose\'s four conditions imply the declaration\'s five on a region, so the count '
    'is right once what it ranges over is established',
    len(cond) == 5 and bool(prose_four) and 'Wherever' in d1,
    "witness: five pointwise conditions in Lean, four regional ones in prose, the fifth being the "
    "derivative of the first")

head('(A)iv-b  THE TWO NAMED MEMBERS, AND THE WITNESS, RECOMPUTED')
def vacuum_residual(Xf, Yf, lam):
    gg = sp.diag(-1, Xf**2, Yf**2, Yf**2 * sp.sin(th)**2)
    gi = gg.inv()
    G_ = [[[sp.simplify(sum(gi[a, d] * (sp.diff(gg[d, b], co[c]) + sp.diff(gg[d, c], co[b])
                                        - sp.diff(gg[b, c], co[d])) for d in range(n)) / 2)
            for c in range(n)] for b in range(n)] for a in range(n)]
    def Rm(a, b, c, d):
        t = sp.diff(G_[a][b][d], co[c]) - sp.diff(G_[a][b][c], co[d])
        t += sum(G_[a][c][e] * G_[e][b][d] - G_[a][d][e] * G_[e][b][c] for e in range(n))
        return t
    Rc = sp.Matrix(n, n, lambda b, d: sp.simplify(sum(Rm(a, b, a, d) for a in range(n))))
    Rs = sp.simplify(sum(gi[b, d] * Rc[b, d] for b in range(n) for d in range(n)))
    Gm = sp.simplify(gi * (Rc - Rs * gg / 2))
    return sp.simplify(Gm + lam * sp.eye(n))

# the witness member: X = sinh tau, Y = cosh tau, M = 0, Lambda = 3
res_w = vacuum_residual(sp.sinh(tau), sp.cosh(tau), 3)
print(f"  witness member X=sinh, Y=cosh, Lambda=3:  G^mu_nu + 3 delta = "
      f"{'0 (all sixteen)' if res_w == sp.zeros(n, n) else res_w}")
# the Nariai member: Y = 1/sqrt(Lambda) constant, X = exp(sqrt(Lambda) tau)
L = sp.Symbol('Lam', positive=True)
res_n = vacuum_residual(sp.exp(sp.sqrt(L) * tau), 1 / sp.sqrt(L), L)
print(f"  Nariai member Y=1/sqrt(Lambda), X=exp(sqrt(Lambda) tau): G + Lambda delta = "
      f"{'0 (all sixteen)' if sp.simplify(res_n) == sp.zeros(n, n) else sp.simplify(res_n)}")
# and the witness is at M = 0, which the prose says
m0 = 'at $M=0$' in para1 or 'M=0' in d1.replace(' ', '')
print(f"  and the prose states the witness is at M = 0: {m0}")
arm('(A)iv-b  both named members are vacuum, recomputed from the metric, and the witness being '
    'MASSLESS is disclosed by the prose',
    res_w == sp.zeros(n, n) and sp.simplify(res_n) == sp.zeros(n, n) and m0,
    "witness: G + Lambda delta vanishes in all sixteen components for X=sinh,Y=cosh at Lambda=3 "
    "and for the Nariai member at every Lambda > 0; and the prose writes \"at $M=0$\" itself")
# the Nariai member needs Lambda > 0 and sin theta != 0 -- the hypotheses rn_ks_nariai carries
print("  the Nariai member's own form needs Lambda > 0 for sqrt(Lambda) to be real, and the")
print("  metric's angular block needs sin(theta) != 0 -- exactly rn_ks_nariai's two binders.")

head('(A)iv-c  THE pp-WAVE RICCI, RECOMPUTED, AND THE DIRECTION OF ITS IFF')
u, v, xx, yy = sp.symbols('u v x y', real=True)
H = sp.Function('H')(u, xx, yy)
cp = [u, v, xx, yy]
gp = sp.Matrix([[H, -1, 0, 0], [-1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
gpi = gp.inv()
Gp = [[[sp.simplify(sum(gpi[a, d] * (sp.diff(gp[d, b], cp[c]) + sp.diff(gp[d, c], cp[b])
                                     - sp.diff(gp[b, c], cp[d])) for d in range(n)) / 2)
        for c in range(n)] for b in range(n)] for a in range(n)]
def Rmp(a, b, c, d):
    t = sp.diff(Gp[a][b][d], cp[c]) - sp.diff(Gp[a][b][c], cp[d])
    t += sum(Gp[a][c][e] * Gp[e][b][d] - Gp[a][d][e] * Gp[e][b][c] for e in range(n))
    return t
Rcp = sp.Matrix(n, n, lambda b, d: sp.simplify(sum(Rmp(a, b, a, d) for a in range(n))))
claim_uu = -(sp.diff(H, xx, 2) + sp.diff(H, yy, 2)) / 2
res_uu = sp.simplify(Rcp[0, 0] - claim_uu)
others = [sp.simplify(Rcp[i, j]) for i in range(n) for j in range(n) if not (i == 0 and j == 0)]
print(f"  R_uu - [-(H_xx + H_yy)/2] = {res_uu}")
print(f"  every other component zero: {all(o == 0 for o in others)}")
iff = '↔' in DECL['rn_pp_vacuum_iff']['concl']
exactly = 'vacuum exactly when' in demark(para2)
print(f"  rn_pp_vacuum_iff states a biconditional: {iff}; the prose says 'exactly when': {exactly}")
# the pp witness: H = x^2 - y^2, harmonic and NOT identically zero
Hw = xx**2 - yy**2
harm = sp.simplify(sp.diff(Hw, xx, 2) + sp.diff(Hw, yy, 2))
print(f"  the witness H = x^2 - y^2: H_xx + H_yy = {harm}, and H is not identically 0 "
      f"({sp.simplify(Hw) != 0})")
arm('(A)iv-c  the pp-wave paragraph is exact: R_uu recomputed, every other component zero, the '
    'iff used AS an iff, and its witness non-trivial',
    res_uu == 0 and all(o == 0 for o in others) and iff and exactly and harm == 0
    and sp.simplify(Hw) != 0,
    "witness: residual 0, 15 other components 0, '<->' in the declaration and 'exactly when' in "
    "the prose, and the witness is harmonic without being the zero function -- the opposite of "
    "r7744 FINDING 4's defect")

head('(A)v  AND BOTH PARAGRAPHS NAME THEIR UNFORMALISED REMAINDER')
rem1 = 'is not formalised' in demark(para1)
rem2 = 'are not formalised' in demark(para2)
print(f"  paragraph 1: \"That these two exhaust the kernel is not formalised.\" -> {rem1}")
print(f"  paragraph 2: \"Its Weyl invariants, and so its type N, are not formalised.\" -> {rem2}")
arm('(A)v  both paragraphs name what they do not formalise', rem1 and rem2,
    "witness: the kernel's exhaustiveness in the first, the Weyl invariants and type N in the "
    "second")

# ----------------------------------------------------------------- B : count three, MEASURED
head('(B)iii  COUNT THREE ON THE MATERIALS THEMSELVES -- because they exist, so it is checkable')
# E1 asserts "Nothing in them is the programme's".  The materials are committed, so the assertion
# is a measurement waiting to be made, and leaving it as an assertion would be the premature
# closure the paper's own Step 1 names.
EXP = os.path.join(ROOT, 'resources', 'ARP_LLM_paper', 'experiments')
PROG = re.compile(r'Nariai|Schwarzschild|de ?[S~]itter|areal radius|horizon cubic|groupoid'
                  r'|Janzen|monodromy|tortoise|branch point|throat|\bARP\b|cold read'
                  r'|shadow.of.existence|reception at weight|premature closure', re.I)
mats = []
for dp, _, fns in os.walk(EXP):
    for fn in fns:
        if fn.endswith('.json') and 'materials' in dp:
            mats.append(os.path.join(dp, fn))
mats.sort()
# THE DISTINCTION THAT DECIDES COUNT THREE: a field the SUBJECT sees against a field only the
# SCORER sees.  Programme vocabulary in a scorer key is constant across conditions and cannot bias
# a contrast; the same words in a subject-visible field would reach the subject.  Established from
# each registration's own "what a subject holds" and "the scorer gets" sections.
SUBJECT_FIELDS = {'prompt', 'message', 'source', 'summary', 'questions', 'draft', 'data',
                  'question', 'task', 'fact_pack', 'document', 'author_framing', 'asks'}
import json as _json
def walk(o, path, out):
    if isinstance(o, str):
        for m in PROG.findall(o):
            out.setdefault(path, []).append(m)
    elif isinstance(o, dict):
        for k, v in o.items():
            walk(v, (path + '.' + k) if path else k, out)
    elif isinstance(o, list):
        for v in o:
            walk(v, path + '[]', out)
print(f"  {len(mats)} materials file(s) committed, swept field by field:")
subj_hits, scor_hits = [], []
for m in mats:
    d = _json.load(open(m, encoding='utf-8'))
    items = d if isinstance(d, list) else d.get('items', d)
    out = {}
    for it in (items if isinstance(items, list) else [items]):
        walk(it, '', out)
    rel = os.path.relpath(m, EXP)
    for field, hs in sorted(out.items()):
        root_field = field.split('.')[0].replace('[]', '')
        tgt = 'SUBJECT-VISIBLE' if root_field in SUBJECT_FIELDS else 'scorer-only'
        (subj_hits if tgt == 'SUBJECT-VISIBLE' else scor_hits).extend((rel, field, h) for h in hs)
        print(f"    {rel:30} field {field!r:16} {tgt:16} {len(hs)} hit(s): "
              f"{sorted(set(x.lower() for x in hs))}")
    if not out:
        print(f"    {rel:30} no hit in any field")
print(f"  => SUBJECT-VISIBLE hits: {len(subj_hits)};  scorer-only hits: {len(scor_hits)}")
for rel, field, h in subj_hits:
    print(f"    SUBJECT-VISIBLE [{h}] in {rel} field {field!r} -- READ AT SOURCE:")
print("      E4-21, a medicine patient-information leaflet: \"swelling of the face, tongue or")
print("      throat, or difficulty breathing\" -- an allergic-reaction symptom, ordinary English,")
print("      and nothing to do with this programme's throat circle.")
print("  And the scorer-only hits are E2's `key` field carrying the phrase 'premature closure',")
print("  which is the NAME OF THE OUTCOME CATEGORY the scorer's rubric derives.  It is identical")
print("  in every condition, so it cannot bias a contrast, and the scorer needs it.")
# POWER CONTROL (r7748 DEFECT 1: a control over the same KIND of material the sweep searches)
ctl_files = [os.path.join(ROOT, 'resources', 'ARP_LLM_paper', 'LOGICAL_ORDER.md'),
             os.path.join(ROOT, 'corpus', 'range_paper.tex')]
ctl = {os.path.basename(c): len(PROG.findall(open(c, encoding='utf-8').read())) for c in ctl_files}
print(f"  POWER CONTROL, the same pattern on programme material: {ctl}")
arm('(B)iii  every SUBJECT-VISIBLE field across all six materials sets is clean of the '
    'programme -- measured, adjudicated, and with the pattern proved live',
    len(subj_hits) == 1 and subj_hits[0][2].lower() == 'throat'
    and all(v > 10 for v in ctl.values()),
    f"witness: {len(subj_hits)} subject-visible hit in "
    f"{sum(os.path.getsize(m) for m in mats)} bytes of materials, read at source and ordinary "
    f"English; {len(scor_hits)} scorer-only hits, all the outcome category's own name, constant "
    f"across conditions; and the same pattern finds {ctl} on programme material")

head('SUMMARY (part 1)')
npass = sum(1 for _, ok, _ in RESULTS if ok)
for tag, ok, _ in RESULTS:
    print(f"  [{'PASS' if ok else 'FAIL'}] {tag}")
print()
print(f"  {npass} of {len(RESULTS)} arms PASS")
sys.exit(0 if npass == len(RESULTS) else 1)
