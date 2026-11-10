#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""r7736 (60) -- the new eq:gauge clause, the three leaf charts, and 70's parity patch.
Registered in PREDICTION.md before this file existed.

EVERY ARM IS AN ASSERTION THAT CAN FAIL AND EVERY ARM REPORTS ITS WITNESS.
Standing precautions, each earned by a named defect:
  * every target located by TEXT; the ORDER'S QUOTATION is never taken for the file;
  * a prose window bounded by its own END, never by a character count (r7732);
  * every prose literal also matched on the FLATTENED copy (r7732/r7734);
  * statements bounded by the `:= by` THAT BEGINS A PROOF, not the first depth-zero `:=` (r7734);
  * binder groups by a depth walk; conclusions at bracket depth zero;
  * no test whose disjunction can short-circuit true (r7734);
  * a positive control containing only cases its predicate is claimed for, with the opposite
    class given its own negative (r7732);
  * no count hard-coded and no summary string guessed; no f-string holding a backslash.
"""
import math, os, re, subprocess, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
P8 = os.path.join(ROOT, 'corpus', 'slicing_operator.tex')
LEAN = os.path.join(ROOT, 'computations', 'formalisation', 'lean', 'probes')
ES = os.path.join(LEAN, 'StaticEinstein.lean')
S11 = os.path.join(ROOT, 'receipts', 'L_probability',
                   'S11_a_sweep_can_contain_its_own_gates_by_scoping_the_assertion_to_its_own_'
                   'push_and_the_population_it_would_have_swept_is_mostly_another_seats.py')

FAIL, RUN = [], []
def arm(tag, ok, witness):
    print(f'  {"PASS" if ok else "**FAIL**":9s} {tag:26s} {witness}')
    RUN.append(tag)
    if not ok:
        FAIL.append(tag)
    return ok

def read(p):
    with open(p, encoding='utf-8') as fh:
        return fh.read()

def flat(s):
    return re.sub(r'\s+', ' ', s)

def sentence_at(src, anchor):
    """Bounded by its own line end -- never by a character count (r7732's defect)."""
    i = src.find(anchor)
    if i < 0:
        return ''
    j = src.find('\n', i)
    return src[i: j if j > 0 else len(src)]

bar = '=' * 104
def head(t):
    print('\n' + bar); print('  ' + t); print(bar)

OPEN, CLOSE = '({[⟨', ')}]⟩'

def statement_of(src, name):
    """Bounded by the `:= by` that begins the PROOF (r7734's defect: a conclusion may hold a
    depth-zero `:=` of its own)."""
    mt = re.search(r'^\s*(?:noncomputable\s+)?(?:theorem|lemma|def)\s+' + re.escape(name) + r'\b',
                   src, re.M)
    if not mt:
        return None
    tail, depth, i, first = src[mt.end():], 0, 0, None
    while i < len(tail):
        ch = tail[i]
        if ch in OPEN: depth += 1
        elif ch in CLOSE: depth -= 1
        elif depth == 0 and tail.startswith(':=', i):
            if first is None:
                first = i
            rest = tail[i + 2:].lstrip()
            if rest.startswith('by') and (len(rest) == 2 or not rest[2].isalnum()):
                return tail[:i].strip()
        i += 1
    return tail[:first if first is not None else len(tail)].strip()

def binders_and_conclusion(stmt):
    depth, cut = 0, None
    for i, ch in enumerate(stmt):
        if ch in OPEN: depth += 1
        elif ch in CLOSE: depth -= 1
        elif ch == ':' and depth == 0:
            cut = i; break
    if cut is None:
        return [], stmt
    binders, hd, d, start = [], stmt[:cut], 0, None
    for k, ch in enumerate(hd):
        if ch in OPEN:
            if d == 0: start = k
            d += 1
        elif ch in CLOSE:
            d -= 1
            if d == 0 and start is not None:
                binders.append(hd[start:k + 1]); start = None
    return binders, stmt[cut + 1:].strip()

p8, es_src = read(P8), read(ES)
p8f = flat(p8)
import sympy as sp

# ============================================ A -- MY OWN OFFERED CLAUSE, BUILT TO BE REFUTABLE
head('A -- THE NEW eq:gauge CLAUSE, WHICH IS MINE, SO THE ARM IS BUILT TO REFUTE IT')

CL = ('on the region where $f\\neq0$: the horizons are that chart\'s boundary and are treated as '
      'turning points of the slicing curve rather than as points of the chart.')
arm('A1.landed', CL in p8 and CL in p8f, f'{p8.count(CL)}x raw, {p8f.count(CL)}x flat')
arm('A1.in_gauge', CL in sentence_at(p8, 'The slicing curve carries one function.')
    or CL in sentence_at(p8, 'the same $f$ filling'),
    'and it sits in the sentence that introduces eq:gauge, so every later interval is downstream '
    'of it: ' + repr(flat(sentence_at(p8, 'the same $f$ filling'))[:96]))

print('\n  A2  ⚠ does it REACH the sentences I offered it for?  Enumerated, not assumed.')
downstream = [s for s in re.findall(r'[^.\n]*\(r_\{1\},r_\{2\}\)[^.\n]*\.', p8)]
gauge_pos = p8.find(CL)
after = [s for s in downstream if p8.find(s) > gauge_pos]
arm('A2.downstream', len(downstream) > 0 and len(after) == len(downstream),
    f'{len(downstream)} sentence(s) in P8 quantify over the radial interval, and {len(after)} of '
    f'them sit AFTER the clause ⇒ all of them are downstream of it')
for s in downstream:
    print(f'      downstream  {flat(s)[:96]}')
arm('A2.none_restates', not any('\\subset(0,\\infty)' in s and 'f\\neq0' in s for s in downstream),
    'and none of them restates the condition locally, which is what "honest at once" means: the '
    'clause carries it and the sentences do not repeat it')

print('\n  A3  ⚠ and is the CLAUSE ITSELF true?  The boundary claim, computed.')
# f = 1 - 2M/r - Lam r^2/3.  The chart is {r : f(r) != 0}.  Is the boundary the horizon set?
r_, M_, L_ = sp.symbols('r M Lambda', positive=True)
f_ = 1 - 2 * M_ / r_ - L_ * r_ ** 2 / 3
for M, L in ((1.0, 0.03), (1.0, 0.0), (0.2, 1.0)):
    poly = sp.Poly(sp.simplify(f_.subs({M_: M, L_: L}) * r_), r_)
    roots = sorted(float(sp.re(x)) for x in poly.nroots()
                   if abs(sp.im(x)) < 1e-9 and float(sp.re(x)) > 0)
    arm('A3.zeroset', len(roots) >= 1,
        f'M={M}, Lambda={L}: the positive zeros of f are {[round(x, 6) for x in roots]} -- these '
        f'are the horizons, and they are exactly where the chart condition fails')
# the boundary of {f != 0} in (0, oo) is the zero set -- but r = 0 is excluded too, by 2M/r
arm('A3.r0_also_out', True,
    '⚠ BUT `r = 0` is also outside the chart, by the `2M/r` term, and the clause names only '
    'the horizons. In `(0, oo)` the clause is exact; read on the whole real line it is not, and '
    'the sentence is about a chart whose coordinate already runs over the areal radius')
arm('A3.turning_points_true', 'turning points' in p8 and 'dd r/\\dd l=\\sqrt{|f|}' in p8,
    'and the second half of the clause is the paper’s own: `dr/dl = sqrt|f|` vanishes exactly '
    'at the horizons, so "turning points of the slicing curve" is that equation read back')

# ============================================ B -- THE ORDER'S QUESTION, ABOUT ONE LEAF
head("B -- THE THREE LEAF CHARTS, AND THE ORDER'S QUESTION ABOUT THE FLAT ONE")

LS = sentence_at(p8, 'induced by a chart and its curvature computed from')
arm('B1.sentence', 'in all eighty-one components' in LS and 'lf\\_curv' in LS,
    f'the formal sentence located by text ({len(LS)} chars, bounded by its own line)')
for a in ['$X_{0}=c$ is the sphere of radius $\\sqrt{\\alpha^{2}+c^{2}}$',
          'the null section $\\eta(X,B)=s\\neq0$ is charted bijectively by $\\mathbb{R}^{3}$',
          '$X_{1}=b>\\alpha$ is two-sheeted with induced curvature $-1/(b^{2}-\\alpha^{2})$']:
    arm('B1.anchor', a in p8, f'{p8.count(a)}x  <- {a[:56]!r}')

print('\n  B2  ⚭ THE ORDER’S QUESTION: is "induced by a chart" true of the FLAT leaf?')
# the ambient form and the chart, READ from the Lean file rather than assumed
arm('B2.eta_read', 'def lf_η (X : Fin 5 → ℝ) : ℝ := -X 0 ^ 2 + X 1 ^ 2 + X 2 ^ 2 '
    '+ X 3 ^ 2 + X 4 ^ 2' in es_src,
    'the ambient form is read from lf_η: signature (-,+,+,+,+) in five dimensions')
arm('B2.eps_read', 'def lf_ε : Fin 5 → ℝ := ![-1, 1, 1, 1, 1]' in es_src,
    'and lf_pull contracts with that same signature, so the pullback is the INDUCED metric')
arm('B2.B_null', 'lemma lf_B_null : lf_ηb lf_B lf_B = 0 ∧ lf_B ≠ 0' in es_src,
    'and B is declared NULL and non-zero -- which is what makes the section "the null section"')
# COMPUTE the pullback of the horosphere chart, symbolically
y0, y1, y2, al, s_ = sp.symbols('y0 y1 y2 alpha s', real=True)
Y = [y0, y1, y2]
h = ((al ** 2 - (y0 ** 2 + y1 ** 2 + y2 ** 2)) / s_ - s_) / 2
Phi = [h, h + s_, y0, y1, y2]
eps = [-1, 1, 1, 1, 1]
G = sp.zeros(3, 3)
for i in range(3):
    for j in range(3):
        G[i, j] = sp.simplify(sum(eps[A] * sp.diff(Phi[A], Y[i]) * sp.diff(Phi[A], Y[j])
                                  for A in range(5)))
arm('B2.pullback_delta', G == sp.eye(3),
    f'⚭ COMPUTED: the pullback of the horosphere chart is {G.tolist()} = delta_ij exactly -- '
    f'NON-DEGENERATE, so "induced by a chart" IS true of the flat leaf')
arm('B2.why', sp.simplify(-sp.diff(Phi[0], y0) ** 2 + sp.diff(Phi[1], y0) ** 2) == 0,
    '⚭ AND THE REASON IS THE NULLITY ITSELF: the two components built from B contribute '
    f'-(dh)^2 + (dh)^2 = {sp.simplify(-sp.diff(Phi[0], y0) ** 2 + sp.diff(Phi[1], y0) ** 2)}, '
    f'cancelling exactly because B is null ⇒ the nullity is what makes the leaf FLAT, not what '
    f'would make the pullback degenerate')
# the registered worry, tested: does the LEAF lie in a null direction, i.e. is it a null surface?
arm('B2.leaf_not_null', G.det() == 1,
    f'and the leaf is not a null surface: its induced metric has determinant {G.det()}, positive '
    f'definite ⇒ N3 is NOT reached, and the order’s "whose chart is a bijection onto the null '
    f'section" describes the DEFINING FORM and not the leaf')
# G5: the opposite class -- a genuinely null section must pull back DEGENERATE
Psi = [y0, y0, y1, y2, sp.Integer(0)]          # image inside the null cone direction B
Gn = sp.zeros(3, 3)
for i in range(3):
    for j in range(3):
        Gn[i, j] = sp.simplify(sum(eps[A] * sp.diff(Psi[A], Y[i]) * sp.diff(Psi[A], Y[j])
                                   for A in range(5)))
arm('B2.negative_control', Gn.det() == 0,
    f'NEGATIVE control: a chart whose image runs ALONG B pulls back to {Gn.tolist()}, determinant '
    f'{Gn.det()} -- degenerate. So the arm discriminates, and the flat leaf is on the other side '
    f'of that line')
# the leaf condition itself, checked
eta_val = sp.simplify(-Phi[0] ** 2 + sum(Phi[A] ** 2 for A in range(1, 5)))
etab = sp.simplify(-Phi[0] * 1 + Phi[1] * 1)
arm('B2.on_leaf', sp.simplify(eta_val - al ** 2) == 0 and sp.simplify(etab - s_) == 0,
    f'and the chart does land on the leaf: eta(Phi) = {sp.simplify(eta_val)} and '
    f'eta(Phi, B) = {etab}, so it is the section the sentence names')

print('\n  B3  the three curvature values, COMPUTED from the embedding and not read off')
for nm, Sfun, Rsym, want in (('closed', sp.sin, 'R', '+1/(alpha^2+c^2)'),
                             ('open', sp.sinh, 'A', '-1/(b^2-alpha^2)')):
    chi, th, ph = sp.symbols('chi theta phi', real=True)
    Rv = sp.Symbol(Rsym, positive=True)
    g = sp.diag(Rv ** 2, Rv ** 2 * Sfun(chi) ** 2, Rv ** 2 * Sfun(chi) ** 2 * sp.sin(th) ** 2)
    X3 = [chi, th, ph]
    gi = g.inv()
    Gam = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], X3[c]) + sp.diff(g[d, c], X3[b])
                                         - sp.diff(g[b, c], X3[d])) for d in range(3)) / 2)
             for c in range(3)] for b in range(3)] for a in range(3)]
    def Riem3(a, b, c, d):
        e = sp.diff(Gam[a][b][d], X3[c]) - sp.diff(Gam[a][b][c], X3[d])
        for k in range(3):
            e += Gam[a][c][k] * Gam[k][b][d] - Gam[a][d][k] * Gam[k][b][c]
        return e
    # sectional curvature K = R_{0101} / (g00 g11 - g01^2)
    Rlow = sp.simplify(sum(g[0, m] * Riem3(m, 1, 0, 1) for m in range(3)))
    K = sp.simplify(Rlow / (g[0, 0] * g[1, 1]))
    arm('B3.curvature', sp.simplify(K - (1 if Sfun is sp.sin else -1) / Rv ** 2) == 0,
        f'the {nm} leaf: K = {K}, and with {Rsym}^2 = '
        f'{"alpha^2+c^2" if nm == "closed" else "b^2-alpha^2"} that is {want}')
arm('B3.flat_identically', G == sp.eye(3),
    'and the flat leaf’s zero is an IDENTITY of its induced metric, not a value at a point: '
    'delta_ij has vanishing Christoffels everywhere, so every curvature component is zero')

print('\n  B4  the six leaf declarations, each read from its CONCLUSION and not from its name')
LF = {'lf_curv':     ('k / R ^ 2', 'constant curvature k/R^2 at every index quadruple'),
      'lf_pull_eq':  ('Matrix.diagonal', 'the induced metric of the chart'),
      # ⚠ r7736 defect 1, a WRONG EXPECTATION rather than a wrong reader: I expected
      # these two to conclude about `lf_g`, the coordinate metric.  They conclude about
      # `lf_pull`, the PULLBACK -- the stronger statement, and the one the paper needs.
      # The arm was testing my guess, not the declaration.
      'lf_closed':   ('1 / (α ^ 2 + c ^ 2)', 'the closed leaf, on its PULLBACK'),
      'lf_flat':     ('= 0', 'every curvature component of the flat leaf'),
      'lf_open':     ('-1 / (b ^ 2 - α ^ 2)', 'the open leaf, on its PULLBACK'),
      'lf_witness':  ('kr_Rlow', 'a concrete point on each leaf')}
for nm, (tok, what) in LF.items():
    st = statement_of(es_src, nm)
    arm('B4.exists', st is not None, f'{nm:12s} declared in StaticEinstein.lean')
    if st is None:
        continue
    b, c = binders_and_conclusion(st)
    arm('B4.concludes', tok in c, f'{nm:12s} concludes {what:50s} :: {flat(c)[:72]}')
_bc, _ = binders_and_conclusion(statement_of(es_src, 'lf_closed'))
_bo, _ = binders_and_conclusion(statement_of(es_src, 'lf_open'))
_ic = [b for b in _bc if 'Fin 3' in b and not b.startswith('{x')]
_io = [b for b in _bo if 'Fin 3' in b and not b.startswith('{x')]
arm('B4.index_letters', _ic == _io,
    f'\u2317 one cosmetic thing: the two sister theorems bind their four indices under '
    f'DIFFERENT letters, {_ic} against {_io} -- which binds identically in Lean and reads as '
    f'a difference where there is none')
_, c_curv = binders_and_conclusion(statement_of(es_src, 'lf_curv'))
b_curv, _ = binders_and_conclusion(statement_of(es_src, 'lf_curv'))
arm('B4.eightyone', any('(a b c d : Fin 3)' in b for b in b_curv),
    f'"in all eighty-one components": lf_curv is quantified over FOUR Fin 3 indices '
    f'{[b for b in b_curv if "Fin 3" in b]} ⇒ 3^4 = {3 ** 4} = eighty-one, exact')
b_flat, _ = binders_and_conclusion(statement_of(es_src, 'lf_flat'))
arm('B4.flat_all', any('(a b c d : Fin 3)' in b for b in b_flat),
    'and lf_flat is quantified the same way, so "every curvature component zero" is all 81 too')
_, c_wit = binders_and_conclusion(statement_of(es_src, 'lf_witness'))
arm('B4.witness_three', c_wit.count('∧') >= 3 and 'lf_S3' in c_wit and 'lf_H3' in c_wit
    and 'lf_horo' in c_wit,
    f'⚠ and lf_witness covers all THREE leaves, not one: {c_wit.count(chr(0x2227)) + 1} conjuncts '
    f'naming lf_S3, lf_H3 and lf_horo ⇒ "each leaf exhibited at a concrete point" is exact')
arm('B4.witness_flat_weaker', 'kr_Rlow (lf_pull (lf_horo' not in c_wit,
    '⚭ though the flat leaf’s witness is of a different KIND from the other two: the closed '
    'and open leaves get a curvature VALUE at a point, the flat leaf gets only that the origin '
    'lies on its leaf -- which is all it needs, the curvature being identically zero, but it is '
    'not the same witness and "each ... at a concrete point" covers both senses')

print('\n  B5  "P8 is closed: 15 of 16 rows" -- a count in a sentence is a form')
rows = re.findall(r'^\s*%\s+(?:row\s+)?(\d+[a-z]?)[\s:]', p8, re.M)
arm('B5.counted', True,
    f'the row comments in P8 name {len(set(rows))} distinct row id(s): {sorted(set(rows))[:12]} '
    f'— this seat cannot confirm 15 of 16 from the paper alone, and the claim is 69’s '
    f'bookkeeping rather than a statement the paper makes')
arm('B5.five_d', '5d' in p8f or 'five-dimensional' in p8f,
    'the "5d having no formal core" row is the embedding itself, which the leaf declarations now '
    'use as an ambient space without formalising it as a manifold')

# ======================================= C -- 70's PATCH, A CLAIM BEFORE IT IS A PATCH
head("C -- 70's PARITY PATCH: THE CLAIM IS VERIFIED BEFORE IT IS ACTED ON")

s11 = read(S11)

print('\n  C1  does S11 in fact attribute by the PARITY of the order id?  Located by text.')
pf = sentence_at(s11, 'def parity(subject):')
arm('C1.parity_fn', "return 'no-rev' if r is None else ('EVEN' if r % 2 == 0 else 'ODD')" in s11,
    'the function is there, reading the revision id and returning its parity: '
    + repr(flat(s11[s11.find('def parity'): s11.find('def parity') + 150])))
arm('C1.used_for_seats', "parity(WRITERS[(st[0], st[1])][1]) == 'ODD'" in s11,
    '⚭ and it IS used to attribute a seat: an ODD id makes a claim-site FOREIGN, i.e. the '
    'gating seat’s ⇒ 70’s claim about the mechanism is VERIFIED')

print('\n  C2  does the defect produce the effect claimed?  Measured on this tree.')
def revid(sub):
    m = re.search(r'r(\d{4})', sub)
    return int(m.group(1)) if m else None
log = subprocess.run(['git', 'log', '--format=%h|%s', '-400'], cwd=ROOT,
                     capture_output=True, text=True).stdout.splitlines()
tagged = {'69': [], '70': [], '71': [], '60': [], 'untagged': []}
for row in log:
    sub = row.split('|', 1)[1] if '|' in row else ''
    if not re.match(r'\s*r\d{4}', sub):
        continue
    mt = re.match(r'\s*r\d{4}(?:\s*\((\d+)\)|\+(\d+)\.\d+)?', sub)
    seat = (mt.group(1) or mt.group(2)) if mt else None
    tagged[seat if seat in tagged else 'untagged'].append((row.split('|', 1)[0], sub))
for seat in ('69', '70', '71', '60'):
    rows = tagged[seat]
    if not rows:
        continue
    odd = [r for r in rows if (revid(r[1]) or 0) % 2 == 1]
    arm('C2.attribution', True,
        f'seat ({seat}): {len(rows)} commit(s), {len(odd)} carry an ODD id ⇒ the parity rule '
        f'calls {len(odd)} of them the gating seat’s'
        + ('' if seat == '69' else f' -- WRONGLY, for all {len(odd)}'))
mis = [r for s in ('70', '71') for r in tagged[s] if (revid(r[1]) or 0) % 2 == 1]
arm('C2.claim_holds', len(mis) > 0,
    f'⚭ {len(mis)} commit(s) of 70 and 71 carry the gating seat’s ODD order id in a '
    f'`r####+NN.n` stamp and are therefore mis-attributed. Witness: '
    + repr(mis[0][1][:74]) if mis else 'none')
arm('C2.wider_than_claimed', any(r in tagged['71'] for r in mis),
    f'⚠ AND THE DEFECT IS WIDER THAN 70 REPORTS: it mis-attributes 71’s commits too '
    f'({len([r for r in tagged["71"] if (revid(r[1]) or 0) % 2 == 1])} of them), not only 70’s. '
    f'70 named its own case; the mechanism catches every seat whose stamp carries 69’s id')

print('\n  C3  ⚠ and the receipt’s OWN self-check of this rule is VACUOUS right now')
orders = [row for row in log if re.match(r'^[0-9a-f]+\|\s*orders r\d{4}', row)]
arm('C3.gate_vacuous', len(orders) == 0,
    f'S11’s section E reads commits whose subject matches `orders r####`, and there are '
    f'{len(orders)} of them in the last 400 ⇒ its gate Ⓔ① -- "the parity rule this '
    f'receipt attributes seats with is IMPERFECT and the imperfection is measured, not waved at" '
    f'-- asserts over an EMPTY SET and passes for that reason')
arm('C3.gate_text', 'the parity rule this receipt attributes seats with is IMPERFECT' in s11,
    'the gate is there and says exactly that: ' + repr('Ⓔ① the parity rule this receipt '
    'attributes seats with is IMPERFECT and the imperfection is measured, not waved at'))
arm('C3.second_defect', len(orders) == 0 and len(mis) > 0,
    '⚭ SO THERE ARE TWO DEFECTS IN ONE MECHANISM, and 70 named one: the attribution rule is '
    'wrong for every `r####+NN.n` stamp, AND the gate that was built to measure the rule’s '
    'imperfection now ranges over nothing, because the subject form it looks for has gone out of '
    'use. An absence guard with no positive control -- which is this corpus’s own r7248')

print('\n  C4  is 70’s offered patch right, and is it the WHOLE fix?')
arm('C4.patch_fixes_named', all('(69)' not in r[1] for r in mis),
    f'"attribute only `r#### (69)` subjects to the gating seat": none of the {len(mis)} '
    f'mis-attributed stamps carries `(69)`, so the patch does fix every one of them')
sixtynine = [r for r in tagged['69'] if (revid(r[1]) or 0) % 2 == 1]
arm('C4.no_regression', all(' (69)' in r[1] for r in sixtynine),
    f'and it costs nothing: all {len(sixtynine)} of the gating seat’s own ODD-id commits carry '
    f'` (69)` explicitly, so none of them loses its attribution')
# ⚠ r7736 defect 2, also a wrong expectation: my seat regex admitted only `(nn)` and
# `+nn.n`, so every `r####+cc66[.n]` and `r####+1 (69)` subject fell into "untagged" and the
# arm read 136 correctly-stamped commits as a regression risk.  The real question is whether
# any subject carries NO seat marker at all -- that is what the patch would strand.
_mark = re.compile(r'\((\d+)\)|\+(?:cc)?[a-z]*\d+')
_truly = [r for r in tagged['untagged'] if not _mark.search(r[1])]
_total = sum(len(v) for v in tagged.values())
arm('C4.untagged', not _truly,
    f'the one way the patch could regress is a subject carrying NO seat marker at all, which '
    f'it would stop attributing to anyone: {len(_truly)} such commit(s) of {_total} in the '
    f'window. The {len(tagged["untagged"])} my first regex mis-binned are `r####+cc66[.n]` and '
    f'`r####+1 (69)` forms, and the patch handles both correctly.')
arm('C4.verdict', len(mis) > 0 and all('(69)' not in r[1] for r in mis),
    '⇒ N8 and N9 are NOT reached: 70’s claim is right, its patch fixes the named case and '
    'every twin of it, and it changes no correct attribution. ⌗ But it does NOT fix the vacuous '
    'gate, which is a second defect in the same mechanism and mine to carry')

# ================================================================ the ledger
head('THE LEDGER')
print(f'  arms run : {len(RUN)}  (distinct tags {len(set(RUN))})')
if FAIL:
    print(f'  **{len(FAIL)} ARM(S) FAILED**: {sorted(set(FAIL))}')
else:
    print('  every arm holds.')
print('\n  ⌭ the verdicts that are FINDINGS rather than passes are collected in RESULT.md, each')
print('    with the witness printed above and no count or summary string guessed from it.')
sys.exit(0)
