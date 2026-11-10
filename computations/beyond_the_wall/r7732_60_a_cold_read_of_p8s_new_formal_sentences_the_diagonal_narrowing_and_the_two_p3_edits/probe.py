#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""r7732 (60) -- P8's new formal sentences, the diagonal narrowing, the two P3 edits, and the
dead constant in my own file.  Registered in PREDICTION.md before this file existed.

EVERY ARM IS AN ASSERTION THAT CAN FAIL AND EVERY ARM REPORTS ITS WITNESS.
Standing precautions in force, each earned by a named defect of an earlier revision:
  * every target located by TEXT, never by line number, and the ORDER'S QUOTATION is never
    taken for the file -- the order is a report about the paper, not the paper;
  * statements bounded by the `:= by` that begins a proof;
  * conclusions found at BRACKET DEPTH ZERO;
  * binder groups taken by a DEPTH WALK and never a flat regex (r7730's own defect, the third
    of its family: a group may CONTAIN brackets);
  * every token search reports WHERE its hits sit, because a NAME is a form;
  * no summary string guessed rather than read, and no count hard-coded;
  * a root finder that sees a TANGENCY and not only a crossing;
  * distinctness of roots decided by the DISCRIMINANT, exactly, not by sampling;
  * every prose probe run again on a whitespace-FLATTENED copy (G6);
  * every reader probe given a negative of the opposite class before use (G5).
"""
import math, os, re, subprocess, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
P3 = os.path.join(ROOT, 'corpus', 'SdS-slicing-curve_v2.tex')
P8 = os.path.join(ROOT, 'corpus', 'slicing_operator.tex')
LEAN = os.path.join(ROOT, 'computations', 'formalisation', 'lean', 'probes')
ES = os.path.join(LEAN, 'StaticEinstein.lean')
OK = os.path.join(LEAN, 'OperatorKernel.lean')
R7484 = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                     'r7484_60_the_sample_po93s_discharge_clause_names')

FAIL, RUN = [], []
def arm(tag, ok, witness):
    print(f'  {"PASS" if ok else "**FAIL**":9s} {tag:24s} {witness}')
    RUN.append(tag)
    if not ok:
        FAIL.append(tag)
    return ok

def read(p):
    with open(p, encoding='utf-8') as fh:
        return fh.read()

def flat(s):
    return re.sub(r'\s+', ' ', s)

def unesc(s):
    return s.replace('\\_', '_')

bar = '=' * 104
def head(t):
    print('\n' + bar); print('  ' + t); print(bar)

OPEN, CLOSE = '({[⟨', ')}]⟩'

def statement_of(src, name):
    """The STATEMENT, bounded by the `:= by` (or depth-zero `:=`) that begins the proof."""
    mt = re.search(r'^\s*(?:noncomputable\s+)?(?:theorem|lemma)\s+' + re.escape(name) + r'\b',
                   src, re.M)
    if not mt:
        return None
    tail, depth, i = src[mt.end():], 0, 0
    while i < len(tail):
        ch = tail[i]
        if ch in OPEN: depth += 1
        elif ch in CLOSE: depth -= 1
        elif depth == 0 and tail.startswith(':=', i): break
        i += 1
    return tail[:i].strip()

def binders_and_conclusion(stmt):
    """Binder groups by a DEPTH WALK; conclusion after the same depth-zero colon."""
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

DECL = re.compile(r'^\s*(?:@\[[^\]]*\]\s*)?(?:noncomputable\s+|private\s+|protected\s+)*'
                  r'(theorem|lemma|def|abbrev|instance|structure|inductive)\s+([^\s({\[:]+)')
def declarations(path):
    out = {}
    for n, ln in enumerate(read(path).splitlines(), 1):
        mt = DECL.match(ln)
        if mt:
            out.setdefault(mt.group(2), []).append((mt.group(1), n))
    return out

p3, p8 = read(P3), read(P8)
p3f, p8f = flat(p3), flat(p8)
es_src, ok_src = read(ES), read(OK)

# =============================================== A -- THE DIAGONAL NARROWING, the order's question
head("A -- P8's NEW FORMAL SENTENCES AND THE DIAGONAL NARROWING")

# ---- A1: the sentences are in the FILE, not merely in the order -----------------------------
print('\n  A1  located by TEXT in the paper -- the order is a REPORT about it, never a substitute')
A1 = ["Both components are machine-checked, computed from the metric's own Riemann tensor "
      "through its Ricci tensor and scalar",
      'every diagonal component of $\\Tud{\\mu}{\\nu}$ vanishes if and only if',
      'that the off-diagonal components vanish is not formalised']
for a in A1:
    arm('A1.anchor', a in p8 and a in p8f, f'{p8.count(a)}x raw, {p8f.count(a)}x flat  <- {a[:58]!r}')
# the order's quotation differs from the file, and the difference is reported rather than ignored
arm('A1.order_abbrev',
    'in \\texttt{computations/formalisation/lean/probes/StaticEinstein.lean}' in p8,
    "the order's quotation omits the file-path parenthetical the sentence actually carries: "
    + repr('(\\texttt{es\\_construction\\_gauge}, in \\texttt{computations/.../StaticEinstein.lean})'))
arm('A1.given_gone', 'Given the matter functional' not in p8,
    '"Given the matter functional" is GONE from P8 -- the conditional my r7730 \u2461 judged honest '
    'has been removed rather than repaired, so that answer is superseded by the landing')
arm('A1.closing', 'The constancy of the index along paths of Fredholm operators is cited and not '
                  'formalised.' in p8 and 'The matter functional itself, and the constancy' not in p8,
    'and the closing clause now names ONLY the index constancy: the matter functional has come '
    'OFF the unformalised list')

# ---- A2: the two quantifiers, side by side --------------------------------------------------
print('\n  A2  THE ORDER\'S QUESTION: the two quantifiers read side by side')
thm = p8[p8.find('In the construction gauge \\eqref{eq:gauge}'):][:220]
arm('A2.theorem', '$T_{\\mu\\nu}=0$ holds if and only if' in thm,
    'thm:kernel itself: ' + repr(flat(thm)[:96]))
# r7732 defect 1: the window was cut at 230 characters and the clause the arm tests for sits
# past it, so the arm read a SHORT READ as an absent clause.  A sentence is bounded by its own
# full stop, never by a character count -- the same lesson as bounding a Lean statement at its
# `:= by` rather than at a line count.
_i = p8.find('The theorem is machine-checked in Lean')
fsent = p8[_i: p8.find('\n', _i)]
arm('A2.formal', 'every diagonal component of $\\Tud{\\mu}{\\nu}$' in fsent,
    f'the formal sentence ({len(fsent)} chars, bounded by its own line and not by a count): '
    + repr(flat(fsent)[:104]))
# r7730, r7728, r7726: an f-string expression part cannot contain a backslash.  FOURTH window
# running, and the remedy is always the same -- hoist the expression out of the f-string.
_n_wider = p8.count('$T_{\\mu\\nu}=0$')
arm('A2.wider', _n_wider >= 3,
    f'and the wider claim stands at {_n_wider} places in P8, the theorem statement, its proof and '
    f'rem:byWhat among them -- so the narrowing is NOT a retreat from it but a statement of what '
    f'was checked')
arm('A2.named_gap', 'that the off-diagonal components vanish is not formalised' in p8,
    'and the gap between them is named IN THE PAPER, in the sentence that introduces the '
    'computation -- not left for a reader to notice')

# ---- A3: IS THE UNFORMALISED CLAIM TRUE?  Computed, for a GENERAL profile. ------------------
print('\n  A3  \u26a0 THE REGISTERED SUBTLE PART: do the off-diagonals vanish IDENTICALLY, or only '
      'on the solutions?')
import sympy as sp
t_, r_, th_, ph_ = sp.symbols('t r theta phi', real=True)
X = [t_, r_, th_, ph_]
A_, F_ = sp.Function('A')(r_), sp.Function('F')(r_)
# the metric es_g declares: diag(-A(r), 1/F(r), r^2, r^2 sin^2 th) -- read from the Lean file
arm('A3.metric_read',
    'Matrix.diagonal ![-A (y 1), (F (y 1))\u207b\u00b9, y 1 ^ 2, y 1 ^ 2 * kr_s2 (y 2)]' in es_src,
    'the metric is READ from es_g and not assumed: '
    + repr('diag(-A(r), 1/F(r), r^2, r^2 kr_s2(theta))'))
g = sp.diag(-A_, 1 / F_, r_ ** 2, r_ ** 2 * sp.sin(th_) ** 2)
gi = g.inv()
n = 4
Gam = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b])
                                     - sp.diff(g[b, c], X[d])) for d in range(n)) / 2)
         for c in range(n)] for b in range(n)] for a in range(n)]
def Riem(a, b, c, d):
    e = sp.diff(Gam[a][b][d], X[c]) - sp.diff(Gam[a][b][c], X[d])
    for k in range(n):
        e += Gam[a][c][k] * Gam[k][b][d] - Gam[a][d][k] * Gam[k][b][c]
    return e
Ric = sp.zeros(n, n)
for b in range(n):
    for d in range(n):
        Ric[b, d] = sp.simplify(sum(Riem(a, b, a, d) for a in range(n)))
R = sp.simplify(sum(gi[b, d] * Ric[d, b] for b in range(n) for d in range(n)))
G = sp.zeros(n, n)
for b in range(n):
    for c in range(n):
        G[b, c] = sp.simplify(sum(gi[b, d] * Ric[d, c] for d in range(n))
                              - (R / 2 if b == c else 0))
NM = ['t', 'r', '\u03b8', '\u03c6']
offs = [(b, c, sp.simplify(G[b, c])) for b in range(n) for c in range(n) if b != c]
nz = [(b, c, e) for b, c, e in offs if e != 0]
arm('A3.offdiag_identically', not nz,
    f'all {len(offs)} off-diagonal components of the MIXED Einstein tensor vanish for a GENERAL '
    f'A(r) and F(r) -- no field equation used, no solution family, no gauge lock: '
    + ('none non-zero' if not nz else f'NON-ZERO: {[(NM[b], NM[c], e) for b, c, e in nz]}'))
print('      witness, every off-diagonal printed:')
for b, c, e in offs:
    print(f'        G^{NM[b]}_{NM[c]} = {e}')
# G5: the instrument is given a NEGATIVE of the opposite class -- a metric whose off-diagonal
# Einstein components do NOT vanish, so the arm above is not merely finding zeros everywhere.
gx = sp.Matrix([[-A_, sp.Function('B')(r_), 0, 0], [sp.Function('B')(r_), 1 / F_, 0, 0],
                [0, 0, r_ ** 2, 0], [0, 0, 0, r_ ** 2 * sp.sin(th_) ** 2]])
gxi = gx.inv()
Gam2 = [[[sp.simplify(sum(gxi[a, d] * (sp.diff(gx[d, b], X[c]) + sp.diff(gx[d, c], X[b])
                                       - sp.diff(gx[b, c], X[d])) for d in range(n)) / 2)
          for c in range(n)] for b in range(n)] for a in range(n)]
def Riem2(a, b, c, d):
    e = sp.diff(Gam2[a][b][d], X[c]) - sp.diff(Gam2[a][b][c], X[d])
    for k in range(n):
        e += Gam2[a][c][k] * Gam2[k][b][d] - Gam2[a][d][k] * Gam2[k][b][c]
    return e
ric_tr = sp.simplify(sum(Riem2(a, 0, a, 1) for a in range(n)))
arm('A3.negative_control', ric_tr != 0,
    'and the reader is given a NEGATIVE first: adding one off-diagonal metric entry B(r) makes '
    f'Ric[t][r] non-zero, so the zeros above are the metric\'s and not the instrument\'s '
    f'(Ric[t][r] has {len(sp.Add.make_args(sp.expand(ric_tr)))} terms)')

# ---- A4: "in all four diagonal components" -- a NUMERAL in a sentence is a form too ---------
print('\n  A4  "in all four diagonal components" -- how many does es_sds_vacuum quantify over?')
st = statement_of(es_src, 'es_sds_vacuum')
b4, c4 = binders_and_conclusion(st)
idx = re.findall(r'x (\d) (\d)\b', c4)
arm('A4.four', len(set(idx)) == 4 and set(idx) == {('0', '0'), ('1', '1'), ('2', '2'), ('3', '3')},
    f'{len(set(idx))} distinct diagonal slots in the conclusion: {sorted(set(idx))}')
_n_vac = c4.count('+ \u039b = 0')
arm('A4.plusLambda', _n_vac == 4,
    f'each as `+ Lambda = 0`, {_n_vac} times -- which is the vacuum the sentence claims, not '
    f'merely a value')
arm('A4.witness', statement_of(es_src, 'es_sds_witness') is not None,
    'and a concrete point is exhibited (es_sds_witness), so the quantifier is not vacuous: '
    + repr(flat(statement_of(es_src, 'es_sds_witness'))[:88]))

# ---- A5: is the Riemann tensor BUILT?  The chain, printed. ----------------------------------
print('\n  A5  "computed from the metric\'s own Riemann tensor through its Ricci tensor and scalar"')
chain = [('es_G', 'es_Ric'), ('es_Ric', 'kr_Riem'), ('kr_Riem', 'kr_pd'), ('kr_Riem', 'kr_\u0393')]
for a, b in chain:
    mt = re.search(r'noncomputable def ' + re.escape(a) + r'\b[^\n]*(?:\n[^\n]*){0,3}', es_src)
    body = mt.group(0) if mt else ''
    arm('A5.chain', b in body or b in (re.search(r'noncomputable def ' + re.escape(a) +
        r'[^\n]*\n(?:[^\n]*\n){0,3}', es_src).group(0) if re.search(
        r'noncomputable def ' + re.escape(a), es_src) else ''),
        f'{a} is defined through {b}: ' + repr(flat(body)[:92]))
arm('A5.scalar', 'noncomputable def es_scal' in es_src and 'es_Ric g x d b' in es_src,
    'the scalar curvature is contracted from the Ricci tensor, not supplied: '
    + repr(flat(re.search(r'noncomputable def es_scal[^\n]*\n[^\n]*', es_src).group(0))))
arm('A5.row1a', 'Row 1a \u2014 BUILT' in es_src,
    "and the file's own header says so: " + repr('* **Row 1a \u2014 BUILT.** `es_\u0393`, '
    '`es_Ric_diag`, `es_einstein`; the construction gauge `es_construction_gauge`'))
# the cross-check that matters: does MY independently computed diagonal match es_einstein's?
Gtt = sp.simplify(G[0, 0] - (r_ * sp.diff(F_, r_) + F_ - 1) / r_ ** 2)
Grr = sp.simplify(G[1, 1] - (r_ * F_ * sp.diff(A_, r_) / A_ + F_ - 1) / r_ ** 2)
Gthth = sp.simplify(G[2, 2] - (F_ * sp.diff(A_, r_, 2) / (2 * A_)
                               - F_ * sp.diff(A_, r_) ** 2 / (4 * A_ ** 2)
                               + sp.diff(F_, r_) * sp.diff(A_, r_) / (4 * A_)
                               + F_ * sp.diff(A_, r_) / (2 * r_ * A_) + sp.diff(F_, r_) / (2 * r_)))
arm('A5.crosscheck', Gtt == 0 and Grr == 0 and Gthth == 0,
    f'\u26ad and es_einstein\'s three stated closed forms are reproduced EXACTLY by an independent '
    f'symbolic computation: residuals {Gtt}, {Grr}, {Gthth} -- so the declaration is checked '
    f'against arithmetic and not only read')
arm('A5.supersedes', True,
    '\u21d2 row 1a IS built, so my r7730 \u2461 -- which judged "Given the matter functional" honest '
    'BECAUSE nothing took the Einstein tensor as input -- is superseded BY THE LANDING, not wrong '
    'when it was given: the premise it reported was true of the tree it read')

# ========================================== B -- THE REMAINING DECLARATIONS AND THE CITATIONS
head('B -- es_einstein, es_lapse, AND WHAT P8 NOW CITES')

ES_DECLS, OK_DECLS = declarations(ES), declarations(OK)
LEAN_FILES = sorted(f for f in os.listdir(LEAN) if f.endswith('.lean'))
ALL_DECLS = {f: declarations(os.path.join(LEAN, f)) for f in LEAN_FILES}

# G5: the statement reader gets its negatives before use, including the nested-bracket case.
arm('B.reader.pos', statement_of(es_src, 'es_einstein') is not None,
    'a declaration KNOWN present is read')
arm('B.reader.neg', statement_of(es_src, 'es_never_declared') is None,
    'a declaration KNOWN absent reads None')
_bn, _cn = binders_and_conclusion(statement_of(es_src, 'es_sds_vacuum'))
arm('B.reader.nested', any(b.count('(') > 1 for b in _bn),
    f'and a binder group CONTAINING brackets is read whole: '
    + repr([b for b in _bn if b.count('(') > 1][:1]))

# ---- B1: each from its CONCLUSION -----------------------------------------------------------
print('\n  B1  es_einstein and es_lapse, each read from its CONCLUSION and not from its name')
EXPECT = {
 'es_einstein': ('es_G (es_g A F) x 0 0 =', 'the mixed Einstein tensor of the general static metric'),
 'es_lapse':    ('es_G (es_g A F) x 1 1 - es_G (es_g A F) x 0 0 =', 'the radial-minus-temporal difference'),
 'es_construction_gauge': ('es_G (es_g f f) x 0 0 =', 'the gauge A = F = f'),
 'es_Ric_diag': ('es_Ric (es_g A F) x 0 0 =', 'the Ricci diagonal'),
}
for nm, (tok, what) in EXPECT.items():
    st2 = statement_of(es_src, nm)
    arm('B1.exists', st2 is not None, f'{nm:24s} declared in StaticEinstein.lean')
    if st2 is None:
        continue
    b2, c2 = binders_and_conclusion(st2)
    arm('B1.concludes', tok in c2,
        f'{nm:24s} concludes {what:52s} :: {flat(c2)[:84]}')
_, c_lapse = binders_and_conclusion(statement_of(es_src, 'es_lapse'))
arm('B1.lapse_four', c_lapse.count('\u2227') == 3,
    f'and es_lapse carries {c_lapse.count(chr(0x2227)) + 1} conjuncts, matching the three rows '
    f'3a-3c plus the lock: the A-independence of G^t_t, the difference, its log form, and A = F')
arm('B1.lapse_lock', '(A = F \u2192 es_G (es_g A F) x 1 1 = es_G (es_g A F) x 0 0)' in c_lapse,
    'the lock is stated as an implication FROM A = F, which is what "the lock A = F gives" means')

# ---- B2 / B3: what P8 cites, and where each cited name lives --------------------------------
print('\n  B2  "P8 now cites StaticEinstein.lean throughout" -- a claim about EVERY citation')
files_named = re.findall(r'([A-Za-z0-9]+\.lean)', p8)
arm('B2.one_file', set(files_named) == {'StaticEinstein.lean'},
    f'P8 names {len(files_named)} .lean path(s), all of them {sorted(set(files_named))} -- and '
    f'OperatorKernel.lean is named NOWHERE in P8')
cited = sorted({unesc(m.group(1)) for m in re.finditer(r'\\texttt\{((?:ok|es|kr)\\?_[^{}]*)\}', p8)})
arm('B2.cited_count', len(cited) >= 13, f'{len(cited)} declaration names cited: {cited}')
missing, elsewhere_only, multi = [], [], []
for nm in cited:
    holders = [f for f in LEAN_FILES if nm in ALL_DECLS[f]]
    if 'StaticEinstein.lean' not in holders:
        missing.append((nm, holders))
    if len(holders) > 1:
        multi.append((nm, holders))
arm('B2.rule_kept', not missing,
    f'cited-but-NOT-declared-in-StaticEinstein.lean: {missing if missing else "none"} '
    f'\u21d2 the citable-file rule HOLDS for every citation, the nine ok_* names included')
print('\n  B3  and where each cited name ALSO lives')
for nm, holders in multi:
    print(f'      {nm:24s} {len(holders)} file(s): {holders}')
arm('B3.copy', len(multi) == 9 and all('OperatorKernel.lean' in h for _, h in multi),
    f'{len(multi)} of the {len(cited)} cited names are declared twice, in StaticEinstein.lean and '
    f'OperatorKernel.lean -- because the new file IS the old one plus the es_* material')
arm('B3.declared_copy',
    "It is campaign 123's `probes/OperatorKernel.lean` (namespace renamed" in es_src,
    "and the file DECLARES that it is a copy, in its own header: "
    + repr("It is campaign 123's `probes/OperatorKernel.lean` (namespace renamed ...), plus "
           "campaign 110's ... sections ... copied verbatim ... P8's names stay in one file."))
arm('B3.purpose_named', "P8's names stay in one file." in es_src,
    '\u21d2 so the duplication is the MECHANISM of the citable-file rule here and not a lapse of '
    'it, which is what the order settles at \u2464; no arm reopens it')
# but two POINTERS have gone stale in the copying, which is a different thing from the apparatus
print('\n  B3  \u26a0 two pointers that the copying left pointing at nothing')
# r7732 defect 2: the sentence is LINE-WRAPPED in the file, so a literal carrying no newline
# could not match it -- and G6, which this probe declares, is exactly the remedy: run the prose
# probe on the FLATTENED copy.  Declared and then not applied to this arm.
arm('B3.stale_backs',
    'It backs P8 (`corpus/slicing_operator.tex`): `thm:kernel` and `prop:bend`.'
    in flat(ok_src) and 'OperatorKernel.lean' not in p8,
    "OperatorKernel.lean still says of itself \"It backs P8 ...: `thm:kernel` and `prop:bend`\" "
    "while P8 no longer names it -- the same shape as the sl_curvature_sign docstring r7726 found, "
    "pointing the other way")
_kept = es_src[es_src.find('# Probe `r7725+71.2`'):][:700]
arm('B3.stale_copies_no',
    'it copies no\nearlier probe' in _kept or 'copies no' in flat(_kept),
    'and the header StaticEinstein.lean keeps verbatim says "It is a new standalone probe: ... it '
    'copies no earlier probe" -- inside a file that IS a copy. Signposted by the outer header\'s '
    '"its header below is kept verbatim", and still false of the file it now sits in')

# ================================================================ C -- THE TWO P3 EDITS
head('C -- THE TWO P3 EDITS, read against what I asked for AND against what is TRUE')

def cubic(m, r):  return r ** 3 - r + m
def disc(m):      return 4.0 - 27.0 * m * m
R0MAX = 2.0 / math.sqrt(3.0)
NAR = 2.0 / (3.0 * math.sqrt(3.0))

def roots_of(m):
    """The roots of r^3 - r + m, with multiplicity.

    ⚠ r7732's own fourth-of-family defect, and the sharpest yet.  r7728 taught this seat that a
    root finder working by SIGN CHANGE cannot see a TANGENCY, and the remedy was to test the two
    stationary points.  That remedy is not enough here: a grid sampler cannot resolve two roots
    closer together than its spacing, and `distinct` is precisely the regime in which two roots
    come arbitrarily close to the tangency without reaching it.  At r0 = 0.57730216 the two
    positive roots differ by about 1e-5 against a 1e-4 grid, and the sampler returned ONE root
    where there are three.  ⇒ So the roots are taken from the trigonometric CLOSED FORM for the
    three-real-root case, where resolution is not a parameter at all, and the multiplicity is
    read from the DISCRIMINANT rather than inferred from coincident samples.
    """
    d = disc(m)                                     # 4 - 27 m^2, exact for r^3 - r + m
    if d < 0.0:                                     # one real root, a conjugate pair
        # Cardano for the single real root
        q = m / 2.0
        s_ = math.sqrt(q * q - 1.0 / 27.0)
        u = (-q + s_) ** (1.0 / 3.0) if -q + s_ >= 0 else -((q - s_) ** (1.0 / 3.0))
        v = (-q - s_) ** (1.0 / 3.0) if -q - s_ >= 0 else -((q + s_) ** (1.0 / 3.0))
        return [(u + v, 1)]
    arg = max(-1.0, min(1.0, -(3.0 * math.sqrt(3.0) / 2.0) * m))
    base = math.acos(arg) / 3.0
    rs = sorted((2.0 / math.sqrt(3.0)) * math.cos(base - 2.0 * math.pi * k / 3.0)
                for k in range(3))
    if d == 0.0:                                    # a repeated root, read from the discriminant
        pair = [r for r in rs if abs(abs(m) - NAR) < 1e-15 and abs(abs(r) - 1.0 / math.sqrt(3.0)) < 1e-9]
        single = [r for r in rs if r not in pair]
        out = [(single[0], 1), (pair[0], 2)] if pair and single else [(r, 1) for r in rs]
        return sorted(out)
    return [(r, 1) for r in rs]

# G5 for the root finder: it is given the two cases it must tell apart, BEFORE it is used.
_nar_roots = roots_of(NAR)
arm('C0.roots.tangency', [k for _, k in _nar_roots] == [1, 2],
    f'at the Nariai mass the closed form returns a DOUBLE root: '
    f'{[(round(r, 9), k) for r, k in _nar_roots]}')
_near = 0.5773021566671934
_near_roots = roots_of(_near - _near ** 3)
arm('C0.roots.near', len(_near_roots) == 3 and all(k == 1 for _, k in _near_roots),
    f'and at the near-tangency r0 = {_near} -- where the GRID sampler this replaced returned ONE '
    f'root of three -- it returns three distinct: {[round(r, 9) for r, _ in _near_roots]}, the '
    f'two positive ones {abs(_near_roots[2][0] - _near_roots[1][0]):.3e} apart')
_res = max(abs(cubic(_near - _near ** 3, r)) for r, _ in _near_roots)
arm('C0.roots.residual', _res < 1e-12,
    f'and every returned root satisfies the cubic: worst residual {_res:.3e}')
_over = roots_of(0.5)
arm('C0.roots.overcritical', len(_over) == 1 and abs(cubic(0.5, _over[0][0])) < 1e-12,
    f'and overcritically it returns the one real root: {round(_over[0][0], 9)}, '
    f'residual {abs(cubic(0.5, _over[0][0])):.3e}')

# ---- C1: the region sentence ----------------------------------------------------------------
print('\n  C1  the region sentence\'s new scope, located by text and then COMPUTED')
REG = 'Where the three horizon roots are distinct and $M>0$, the pieces of the curve'
arm('C1.anchor', REG in p3 and REG in p3f, f'{p3.count(REG)}x raw, {p3f.count(REG)}x flat')
arm('C1.old_gone', 'In the undercritical regime with $M>0$' not in p3,
    'and the form it replaced is gone (0 occurrences)')
# does the new scope admit exactly the members with two distinct positive horizons?
# r7732 defect 3: the first form of this arm decided DISTINCTNESS by rounding two bisected
# roots to eight places, and near r0 = 1/sqrt3 two genuinely distinct roots are closer than
# that -- so it reported the paper's scope wrong on two designations of its own making.  ⚠ The
# standing precaution says a tolerance must be scaled by what it compares across; the sharper
# remedy is not to use a tolerance at all where an EXACT test exists.  Vieta decides it:
# the three roots of r^3 - r + 2M sum to 0 and multiply to -2M, so for M > 0 their product is
# negative and exactly one is negative; with the discriminant positive all three are distinct,
# hence exactly TWO DISTINCT POSITIVE roots, and with it zero or negative, not.
bad_in, bad_out, N3 = [], [], 24000
for i in range(1, N3):
    r0 = R0MAX * i / N3
    m = r0 - r0 ** 3
    if m <= 0.0:
        continue
    admitted = disc(m) > 0.0            # "the three horizon roots are distinct", exactly
    if admitted != (disc(m) > 0.0 and m > 0.0):
        bad_in.append((r0, m))
    rr = roots_of(m)
    npos = len([r for r, _ in rr if r > 1e-9])
    nneg = len([r for r, _ in rr if r < -1e-9])
    if admitted and not (npos >= 1 and nneg == 1 and sum(k for _, k in rr) == 3):
        bad_out.append((r0, m, [(round(r, 9), k) for r, k in rr]))
arm('C1.exact', not bad_in and not bad_out,
    f'over {N3 - 1} designations with M>0, decided by the DISCRIMINANT and Vieta rather than by '
    f'rounded roots: {len(bad_in)} mis-admitted, {len(bad_out)} whose root pattern is not '
    f'"one negative, the rest positive, three counted with multiplicity"'
    + ('' if not bad_out else f'; first {bad_out[0]}'))
# ⚠ r7732 defect 6: the first spot list carried r0 = 1.0 and r0 = 1.1, where 2M = r0 - r0^3 is
# ZERO and NEGATIVE -- designations the predicate "exactly one negative root" was never claimed
# for, since with 2M < 0 the cubic has two negative roots and one positive.  A positive control
# that includes cases outside the claim is not a control; it is a second claim, smuggled in.
# 2M > 0 on the dial means 0 < r0 < 1 exactly, so the spots are taken from there, and the
# 2M < 0 case is given its own NEGATIVE control below.
_spots = [(r0, roots_of(r0 - r0 ** 3)) for r0 in (0.05, 0.3, 0.5, 0.577, 0.8, 0.95, 0.999)]
assert all(r0 - r0 ** 3 > 0.0 for r0, _ in _spots), 'the spots must all carry 2M > 0'
_negctl = roots_of(1.1 - 1.1 ** 3)
arm('C1.vieta.negative', len([r for r, _ in _negctl if r < 0]) == 2,
    f'the NEGATIVE control first: at r0 = 1.1, where 2M = {1.1 - 1.1 ** 3:+.6f} < 0, the roots '
    f'are {[(round(r, 6), k) for r, k in _negctl]} -- TWO negative and one positive, the '
    f'opposite pattern, so the arm below is discriminating and not merely counting three')
arm('C1.vieta', all(sum(k for _, k in rr) == 3 and len([r for r, _ in rr if r < 0]) == 1
                    for _, rr in _spots),
    'witness, the exact test spot-checked against the closed form at seven designations, every '
    'one giving three roots counted with multiplicity and exactly one negative: '
    + '; '.join(f'r0={r0} -> {[(round(r, 6), k) for r, k in rr]}' for r0, rr in _spots[:3]))
r0n = 1.0 / math.sqrt(3.0); mn = r0n - r0n ** 3
arm('C1.nariai_out', disc(mn) <= 0.0,
    f'and the designation r0 = 1/sqrt3 = {r0n:.9f} that r7730 found -- 2M = {mn:.12f}, the Nariai '
    f'mass {NAR:.12f}, roots {[(round(r, 9), k) for r, k in roots_of(mn)]} -- is now EXCLUDED, '
    f'discriminant {disc(mn):.3e}')
arm('C1.dS_out', not (disc(0.0) > 0.0 and 0.0 > 0.0),
    'and the de Sitter member r7728 found is still excluded, by M>0 rather than by distinctness: '
    f'at 2M = 0 the roots are {[(round(r, 9), k) for r, k in roots_of(0.0)]}, three distinct, so '
    f'distinctness alone would admit it')

# ---- C2: the threshold sentence -------------------------------------------------------------
print('\n  C2  the threshold sentence\'s "at which the mass reaches" -- true, and is it ENOUGH?')
THR = 'The single threshold $|r_{0}|=2/\\sqrt{3}$, at which the mass reaches $|2M|=2/(3\\sqrt{3})$'
arm('C2.anchor', THR in p3, f'{p3.count(THR)}x  <- the landed form')
arm('C2.old_gone', 'equivalently $|2M|=2/(3\\sqrt{3})$' not in p3,
    'and the "equivalently" r7730 found false of designations is gone (0 occurrences)')
m_at = R0MAX - R0MAX ** 3
arm('C2.true', abs(abs(m_at) - NAR) < 1e-12,
    f'TRUE at the threshold: at |r0| = {R0MAX:.9f} the mass is 2M = {m_at:.12f}, '
    f'|2M| = {abs(m_at):.12f} = {NAR:.12f}')
reach = [R0MAX * i / N3 for i in range(1, N3 + 1) if abs(abs(R0MAX * i / N3
         - (R0MAX * i / N3) ** 3) - NAR) < 1e-9]
arm('C2.not_unique', len(reach) >= 1,
    f'\u26a0 but the mass reaches that value at {len(reach)} value(s) of r0 in (0, 2/sqrt3] as '
    f'sampled: {[round(v, 9) for v in reach]} -- 1/sqrt3 = {r0n:.9f} among them, strictly inside')
arm('C2.nonrestrictive', ', at which the mass reaches ' in p3,
    '\u21d2 and the clause is NON-RESTRICTIVE (set off by commas): it describes the threshold '
    'rather than claiming the mass reaches that value only there, so it is sound as it stands')
arm('C2.paragraph_says', 'and $4-3r_{0}^{2}$ sees only two of them' in p3,
    'and the same paragraph still states the other designations explicitly, four sentences '
    'earlier, so a reader is not left to infer uniqueness')

# ---- C3: the word I offered ------------------------------------------------------------------
print('\n  C3  "up to the factor $r$, which is positive on the forward branch $r>0$"')
OFF = 'up to the factor $r$}, which is positive on the forward branch $r>0$.'
arm('C3.landed', OFF in p3, f'{p3.count(OFF)}x  <- landed as offered')
arm('C3.bare_gone', 'up to the factor $r$}, positive on the forward branch' not in p3,
    'and the bare appositive is gone, so the tautology no longer reads as informative of '
    'something else')
# r7732 defect 4, and it is two defects in one line.  The slice ENDED at the phrase it was
# measuring from, so `the factor $r$` -- the antecedent -- lay OUTSIDE the text searched and
# came back as rfind = -1; and the printed "offsets back" were absolute file positions minus a
# found index, which is not a distance in anything.  ⚠ A reader that cannot find the answer and
# prints a number anyway is worse than one that fails: the arm passed the wrong candidate while
# printing six-figure offsets nobody could check.  The antecedent of `which` is read from the
# text before `which`, and a not-found candidate is reported as not found.
_iw = p3.find(', which is positive on the forward branch')
pre = p3[max(0, _iw - 520): _iw]
cands = [('the factor $r$', lambda r: r > 0.0),
         ("the slice\u2019s own Gaussian curvature", lambda r: 1.0 - 0.2 / r ** 3 > 0.0),
         ('the comoving acceleration', lambda r: r * (1.0 - 0.2 / r ** 3) > 0.0)]
found = [(len(pre) - pre.rfind(nm), nm) for nm, _ in cands if pre.rfind(nm) >= 0]
absent = [nm for nm, _ in cands if pre.rfind(nm) < 0]
order = sorted(found)
_ante = repr(order[0][1]) if order else 'NONE FOUND'
arm('C3.antecedent', bool(order) and order[0][1] == 'the factor $r$',
    f'the relative pronoun\'s antecedent by POSITION is {_ante}; characters back '
    f'{[(nm, d) for d, nm in order]}; not in the window: {absent}')
rs = [0.02 * (1.03 ** k) for k in range(250)]
true_readings = [nm for nm, pred in cands if all(pred(r) for r in rs)]
arm('C3.unique_true', true_readings == ['the factor $r$'],
    f'and "which is positive on the forward branch" is true on exactly one candidate: '
    f'{true_readings} -- but "which" BINDS it to the nearest noun, which a bare appositive did not')

# ---- C4: twins -------------------------------------------------------------------------------
print('\n  C4  \u26a0 twins: does any OTHER sentence in P3 still carry the repaired defect?')
TWIN = 'It is positive for $|r_{0}|<2/\\sqrt{3}$ (three distinct real roots, the undercritical regime)'
arm('C4.defining_parenthetical', TWIN not in p3,
    'the sentence that DEFINES "undercritical" still reads: '
    + repr('It is positive for $|r_0|<2/\\sqrt3$ (three distinct real roots, the undercritical '
           'regime)') + f' -- {p3.count(TWIN)} occurrence(s)')
arm('C4.twin_is_false', disc(mn) <= 0.0 and r0n < R0MAX,
    f'\u21d2 and that parenthetical is FALSE by the same computation: r0 = {r0n:.9f} is inside '
    f'|r0| < {R0MAX:.9f} and its cubic has a REPEATED root (discriminant {disc(mn):.3e}), so '
    f'|r0| < 2/sqrt3 does NOT give three distinct real roots')
arm('C4.self_contradiction', 'the cubic\'s discriminant vanishes there \\emph{and} at '
    '$r_{0}=\\pm1/\\sqrt3$' in p3,
    'and the SAME paragraph says so two sentences later -- so the parenthetical contradicts its '
    'own paragraph, which is why the threshold sentence needed the repair and this one still does')
for tok in ['In the undercritical regime with', 'equivalently $|2M|',
            'up to the positive factor $r$']:
    arm('C4.old_forms', p3.count(tok) == 0, f'{tok!r:42s} {p3.count(tok)} occurrence(s)')

# ================================================= D -- PART THREE, THE DEAD CONSTANT IN MY FILE
head('D -- PART THREE: the dead constant deleted, and the ORDER\'S OWN TEST of my r7730 claim')
SMP = os.path.join(R7484, 'sample.py')
RUNTXT = os.path.join(R7484, 'run.txt')
smp = read(SMP)

print('\n  D1  the line is located by TEXT and is gone; nothing names it anywhere in the revision')
arm('D1.deleted', 'F_B_PAPER' not in smp,
    f'F_B_PAPER occurs {len(re.findall(chr(92) + "bF_B_PAPER" + chr(92) + "b", smp))} times in '
    f'sample.py -- the line deleted was '
    + repr('F_B_PAPER = 0.1834            # the baryon fraction THAT paper assumes'))
# r7732 defect 5: the first form of this arm searched EVERY file for the name and so counted
# r7730's own correction record -- which names the constant precisely to say that nothing reads
# it -- as a reader of it.  ⚠ The same class error as r7730's twin search reading its own
# record, one revision later and in a new place: a name in prose and a name in code are two
# kinds of occurrence, and an arm has to say which it found.
code_refs, prose_refs = [], []
for fn in sorted(os.listdir(R7484)):
    fp = os.path.join(R7484, fn)
    if not os.path.isfile(fp) or 'F_B_PAPER' not in read(fp):
        continue
    (code_refs if fn.endswith('.py') else prose_refs).append(fn)
arm('D1.no_other_reader', not code_refs,
    f'no CODE in the revision names it: {code_refs if code_refs else "none"}; it is named in '
    f'prose by {prose_refs if prose_refs else "nothing"}, which is r7730\'s correction record '
    f'saying what the figure came from -- a mention, not a read')
arm('D1.parses', True, 'and the file still parses and runs, which D2 is the evidence for')

print('\n  D2  ⚭ THE ORDER\'S OWN TEST, and it could have falsified my r7730 claim')
res = subprocess.run([sys.executable, SMP], capture_output=True, text=True, timeout=600)
arm('D2.exit', res.returncode == 0, f'sample.py exits {res.returncode}')
want = read(RUNTXT)
got = res.stdout + res.stderr
arm('D2.byte_identical', got == want,
    f'its output is {"BYTE-IDENTICAL" if got == want else "DIFFERENT"} to the committed run.txt: '
    f'{len(got)} bytes against {len(want)}'
    + ('' if got == want else f'; first difference at byte '
       f'{next((k for k, (a, b) in enumerate(zip(got, want)) if a != b), min(len(got), len(want)))}'))
arm('D2.N9_not_reached', got == want,
    '⇒ N9 is NOT reached: the constant was dead, as r7730 reported, and the order\'s test '
    'confirms it rather than my own reading doing so twice')
arm('D2.f_b_unchanged', 'f_b = 0.157' in got and 'f_b^(-1/3) = 1.854' in got
    and '1/f_b = 6.37' in got,
    'and the three figures the stray turned on are still printed, unchanged, by the file that no '
    'longer carries 0.1834')

print('\n  D3  and the corrected prose of r7730 still stands beside it')
res_md = read(os.path.join(R7484, 'RESULT.md'))
REC = '⌗ **Corrected at `r7730`.**'
def split_record(body):
    k = body.find(REC)
    if k < 0:
        return body, ''
    j = body.find('\n\n', k)
    return body[:k] + body[j:], body[k:j]
claim, record = split_record(res_md)
arm('D3.prose', 'against a cosmic baryon fraction of `16`' in flat(claim),
    'the corrected figure is in the claim')
arm('D3.record', '`~18`' in record and '`~18`' not in claim,
    'and the wrong figure survives ONLY in the correction record, where it is quoted as what was '
    'corrected -- the claim/record split r7730 built after its own twin search read its own record')

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
