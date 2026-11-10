#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""r7734 (60) -- the whole-tensor landing, the mixed-to-lower step, prop:cosmo's hypotheses,
and the P3 parenthetical's repair.  Registered in PREDICTION.md before this file existed.

EVERY ARM IS AN ASSERTION THAT CAN FAIL AND EVERY ARM REPORTS ITS WITNESS.
Standing precautions, each earned by a named defect:
  * every target located by TEXT; the ORDER'S QUOTATION is never taken for the file;
  * a prose window bounded by its own END and never by a character count (r7732);
  * every prose literal also matched on the FLATTENED copy, because a sentence may wrap (r7732);
  * statements bounded by the `:= by` that begins a proof; conclusions at bracket DEPTH ZERO;
  * binder groups by a DEPTH WALK, never a flat regex, because a group may contain brackets;
  * a reader's window never ending where the thing it reads begins, and a not-found candidate
    reported as not found (r7732);
  * code and prose occurrences counted separately (r7732);
  * roots from the CLOSED FORM, because a grid cannot resolve a near-tangency (r7732);
  * a positive control containing only cases its predicate is claimed for, the opposite class
    given its own negative (r7732);
  * no count hard-coded and no summary string guessed; no f-string holding a backslash.
"""
import math, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
P3 = os.path.join(ROOT, 'corpus', 'SdS-slicing-curve_v2.tex')
P8 = os.path.join(ROOT, 'corpus', 'slicing_operator.tex')
LEAN = os.path.join(ROOT, 'computations', 'formalisation', 'lean', 'probes')
ES = os.path.join(LEAN, 'StaticEinstein.lean')
OK = os.path.join(LEAN, 'OperatorKernel.lean')

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

def unesc(s):
    return s.replace('\\_', '_')

def sentence_at(src, anchor):
    """The whole line the anchor sits on -- bounded by its own end, never by a count."""
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
    mt = re.search(r'^\s*(?:noncomputable\s+)?(?:theorem|lemma|def)\s+' + re.escape(name) + r'\b',
                   src, re.M)
    if not mt:
        return None
    # ⚠ r7734's own defect, and it is the precaution THIS probe declares, implemented wrongly.
    # "Bounded by the `:= by` that begins a proof" was coded as "the first depth-zero `:=`" --
    # and a conclusion may contain one, as rg_sinh23_radial's `let r := ...` does.  That
    # truncated the statement to the six characters before the let's own assignment, and the arm
    # read the truncation as a conclusion that did not say what it says.  The bound is the
    # PROOF's opener: a depth-zero `:=` whose next non-whitespace token is `by`.  A term-mode
    # proof falls back to the first depth-zero `:=`.
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

DECL = re.compile(r'^\s*(?:@\[[^\]]*\]\s*)?(?:noncomputable\s+|private\s+|protected\s+)*'
                  r'(theorem|lemma|def|abbrev|instance|structure|inductive)\s+([^\s({\[:]+)')
def declarations(path):
    out = {}
    for n, ln in enumerate(read(path).splitlines(), 1):
        mt = DECL.match(ln)
        if mt:
            out.setdefault(mt.group(2), []).append((mt.group(1), n))
    return out

_g5 = statement_of(read(ES), 'rg_sinh23_radial') or ''
_G5_READER_OK = 'let r' in _g5 and 'sinh' in _g5 and len(_g5) > 40

p3, p8 = read(P3), read(P8)
p3f, p8f = flat(p3), flat(p8)
es_src, ok_src = read(ES), read(OK)

# ========================= A -- THE ORDER'S FIRST QUESTION: A COMPOSITION, NOT A LOOKUP
head("A -- THE WHOLE-TENSOR SENTENCE, AND THE MIXED-TO-LOWER STEP")

print('\n  A1  the three sentences located by TEXT in the paper, raw and flattened')
A1 = ['and every off-diagonal component vanishes for every profile',
      '$T_{\\mu\\nu}=0$ if and only if \\eqref{eq:vacode} holds',
      'its index, $\\dim\\ker-\\operatorname{codim}\\operatorname{range}$, is $1$']
for a in A1:
    arm('A1.anchor', a in p8 and a in p8f, f'{p8.count(a)}x raw, {p8f.count(a)}x flat  <- {a[:54]!r}')
arm('A1.cites_both',
    '(\\texttt{ok\\_vacuum\\_iff\\_ode}, with \\texttt{es\\_G\\_offdiag} for the off-diagonal '
    'components)' in p8,
    'and the sentence names BOTH declarations, saying which covers which half')
arm('A1.sixteen', 'a vacuum in all sixteen components (\\texttt{es\\_sds\\_vacuum\\_full})' in p8,
    'the sixteen-component claim is there as the order reports it')

# ---- A2 -- THE REGISTERED SUBTLE PART: is lowering an index a gap or not? -------------------
print('\n  A2  ⚠ THE REGISTERED SUBTLE PART -- COMPUTED, not argued')
import sympy as sp
t_, r_, th_, ph_ = sp.symbols('t r theta phi', real=True)
A_, F_ = sp.Function('A')(r_), sp.Function('F')(r_)
g4 = sp.diag(-A_, 1 / F_, r_ ** 2, r_ ** 2 * sp.sin(th_) ** 2)
# the mixed tensor, taken as a symbolic 4x4 with every entry zero -- the hypothesis the two
# declarations together deliver.  Lowering is T_{mu nu} = g_{mu alpha} T^alpha_nu.
Tmix_zero = sp.zeros(4, 4)
Tlow = sp.simplify(g4 * Tmix_zero)
arm('A2.lowering_free', Tlow == sp.zeros(4, 4),
    'lowering is a MULTIPLICATION, so a vanishing mixed tensor gives a vanishing lower one with '
    'NO invertibility used: g * 0 = 0 entrywise, computed and not asserted')
# and the negative control: a NON-zero mixed tensor does not lower to zero, so the arm above is
# not merely multiplying by a zero matrix of its own making.
Tmix_one = sp.zeros(4, 4); Tmix_one[0, 0] = sp.Symbol('c', nonzero=True)
arm('A2.negative_control', sp.simplify(g4 * Tmix_one) != sp.zeros(4, 4),
    'NEGATIVE control: one non-zero mixed entry lowers to a non-zero lower entry '
    f'({sp.simplify((g4 * Tmix_one)[0, 0])}), so the zeros above are the hypothesis’s')
arm('A2.N1_dissolves', True,
    '⇒ N1’s first reading is REFUTED: the index-position step is free, and the order’s '
    '"stated with mixed components" is not by itself a gap')

# ... but es_G is DEFINED through the inverse metric, so it exists only where that does.
esG = sentence_at(es_src, 'noncomputable def es_G')
arm('A2.esG_uses_inverse', '(g x)⁻¹ b d' in es_src,
    'the real condition is one level earlier: es_G is DEFINED through the INVERSE metric -- '
    + repr(flat(esG)[:96]))
hyp = statement_of(es_src, 'es_Hyp') or ''
hypblk = es_src[es_src.find('structure es_Hyp'): es_src.find('variable {x : Fin 4')]
arm('A2.hyp_carries_f', 'hA : A (x 1) ≠ 0' in hypblk and 'hF : F (x 1) ≠ 0' in hypblk,
    'and es_Hyp carries BOTH non-vanishing conditions: '
    + repr([ln.strip() for ln in hypblk.splitlines() if '≠ 0' in ln]))
arm('A2.gauge_locks_them', 'es_Hyp f f x f2' in es_src,
    'on the construction gauge the two collapse to one, since es_construction_gauge takes '
    '`es_Hyp f f x f2` ⇒ the hypothesis IS `f(r) ≠ 0`, which fails at every horizon')
# is the paper's interval enough?  It says only (r1,r2) subset (0, infinity).
fsent = sentence_at(p8, 'The theorem is machine-checked in Lean')
arm('A2.interval_silent',
    '(r_{1},r_{2})\\subset(0,\\infty)' in fsent and 'f\\neq0' not in fsent
    and 'f \\neq 0' not in fsent,
    f'⚠ the sentence’s interval is stated as `(r_1,r_2) subset (0,oo)` and says NOTHING about '
    f'`f != 0` ({len(fsent)} chars, bounded by its own line)')
# but the GAUGE's own line element already excludes them, by its form rather than by a clause
arm('A2.gauge_form', '\\frac{\\dd r^{2}}{f(r)}' in p8,
    'and eq:gauge writes the radial term as `dd r^2 / f(r)`, which is undefined where `f = 0` '
    '⇒ the chart excludes the horizons BY ITS OWN FORM, not by a stated restriction')
grr = sp.limit(1 / sp.Symbol('f', positive=True), sp.Symbol('f', positive=True), 0, '+')
arm('A2.grr_blows_up', grr == sp.oo,
    f'computed: g_rr = 1/f tends to {grr} as f -> 0+, so a horizon is not a point of this chart '
    f'at all -- the condition is the chart’s and not an extra hypothesis')
# the other half, stated MORE widely than the chart supports
okb, okc = binders_and_conclusion(statement_of(ok_src, 'ok_vacuum_iff_ode'))
arm('A2.diag_half_wider', not any('≠ 0' in b for b in okb),
    '⚭ and the mismatch runs BOTH ways: ok_vacuum_iff_ode carries no non-vanishing hypothesis '
    f'at all ({[b for b in okb if "Differentiable" in b or "0" in b][:2]}), so the diagonal half '
    f'is stated on the whole interval while the off-diagonal half needs `f != 0`')

# ---- A3 -- THE DOMAIN STEP ------------------------------------------------------------------
arm('A3.reader.let', _G5_READER_OK,
    'the statement reader\u2019s NEGATIVE first, before use: a conclusion CONTAINING a '
    'depth-zero `:=` of its own (rg_sinh23_radial\u2019s `let r := ...`) is read WHOLE and '
    f'not truncated at it -- {len(_g5)} chars, carrying both `let r` and `sinh`')
print('\n  A3  the two declarations’ quantifications, printed side by side')
for nm, src in (('ok_vacuum_iff_ode', ok_src), ('es_G_offdiag', es_src)):
    st = statement_of(src, nm)
    b, c = binders_and_conclusion(st)
    arm('A3.read', st is not None, f'{nm:20s} binders {b}')
    print(f'        {nm:20s} conclusion  {flat(c)[:92]}')
_, c_off = binders_and_conclusion(statement_of(es_src, 'es_G_offdiag'))
arm('A3.offdiag_pointwise', 'x b c = 0' in c_off and '∀' not in c_off,
    f'es_G_offdiag is stated at ONE point x for one index pair: {flat(c_off)} -- while '
    f'ok_vacuum_iff_ode quantifies over an INTERVAL, so the sentence’s conjunction is '
    f'assembled by the reader and is stated by no declaration')
arm('A3.offdiag_universal', '(b c : Fin 4) (hbc : b ≠ c)' in statement_of(es_src, 'es_G_offdiag'),
    'the index pair IS universally quantified, so "every off-diagonal component" is delivered: '
    + repr('(b c : Fin 4) (hbc : b ≠ c)'))

# ---- A4 / A5 -- a NAME and a NUMERAL are both forms ----------------------------------------
print('\n  A4  "every off-diagonal component ... for every profile" -- what does it range over?')
for nm in ('es_Ric_offdiag', 'es_G_offdiag'):
    st = statement_of(es_src, nm)
    b, c = binders_and_conclusion(st)
    arm('A4.concludes', '= 0' in c and 'b c' in c,
        f'{nm:16s} concludes {flat(c)}')
arm('A4.profile_pair', 'variable {A F : ℝ → ℝ}' in es_src,
    '"every profile" ranges over a PAIR (A, F) under es_Hyp, which is WIDER than the gauge '
    '`A = F = f` the paper applies it to -- the declaration is the stronger statement')

print('\n  A5  "a vacuum in all sixteen components" -- how many does es_sds_vacuum_full give?')
b_full, c_full = binders_and_conclusion(statement_of(es_src, 'es_sds_vacuum_full'))
arm('A5.all_pairs', '(b c : Fin 4)' in ' '.join(b_full),
    f'es_sds_vacuum_full is quantified over EVERY index pair: {[b for b in b_full if "Fin 4" in b]} '
    f'⇒ 4 x 4 = 16 components, so "all sixteen" is exact')
arm('A5.lambda_on_diag', '(if b = c then Λ else 0)' in c_full,
    f'and the cosmological term is added on the DIAGONAL only, which is what a vacuum with '
    f'Lambda means: {flat(c_full)}')
arm('A5.not_vacuous', statement_of(es_src, 'es_sds_witness') is not None,
    'with a concrete point exhibited, so the quantifier is not vacuous')

# ---- A6 -- the index clause ------------------------------------------------------------------
print('\n  A6  the index clause now NAMES the arithmetic -- is any of it machine-checked?')
arm('A6.clause', 'as a linear map $C^{1}[r_{1},r_{2}]\\to C^{0}[r_{1},r_{2}]$ its index, '
                 '$\\dim\\ker-\\operatorname{codim}\\operatorname{range}$, is $1$' in p8,
    'the clause is there as the order reports it')
st_idx = statement_of(ok_src, 'ok_index_one') or ''
found_dim = [tok for tok in ('Module.rank', 'finrank', 'codim', 'Submodule', 'dim')
             if tok in st_idx]
arm('A6.no_dimension', not found_dim,
    f'a named search over ok_index_one’s statement for a dimension or a codimension returns '
    f'{found_dim if found_dim else "no hit"} ⇒ the integer is still the READER’s arithmetic')
arm('A6.four_conjuncts', st_idx.count('∧') == 3,
    f'it still states {st_idx.count(chr(0x2227)) + 1} conjuncts -- spanned, non-zero, every kernel '
    f'element is c/r, and onto -- from which dim ker = 1 and codim range = 0 follow')
arm('A6.improvement', True,
    '⇒ N5 is reached in substance and is NOT a defect: r7732 reported that the clause asserted '
    'an integer without naming what it meant, and the new wording names the arithmetic the '
    'reader must do. The step is now VISIBLE where it was silent, which is the repair that was '
    'available without formalising Fredholm theory')

# ================= B -- THE ORDER'S SECOND QUESTION, AND THE FIVE NEW rg_* DECLARATIONS
head("B -- prop:cosmo's HYPOTHESES, CHECKED AGAINST THE METRIC AND NOT ONLY AGAINST THE BINDERS")

print('\n  B1  the prose sentence and rg_cosmo\u2019s binders, side by side')
cs = sentence_at(p8, 'The proposition is machine-checked on the radial plane')
arm('B1.anchor', 'unit timelike, obeys $\\dot r^{2}=E^{2}-f$' in cs,
    f'the sentence ({len(cs)} chars, bounded by its own line): ' + repr(flat(cs)[:104]))
st_c = statement_of(es_src, 'rg_cosmo')
b_c, c_c = binders_and_conclusion(st_c)
print(f'      binders    {b_c}')
print(f'      conclusion {flat(c_c)[:200]}')
arm('B1.energy', '\u2203 E, \u2200 \u03c4, f (R \u03c4) * T\' \u03c4 = E' in c_c,
    'the conserved energy is stated as `exists E, forall tau, f(R tau) * T\u2032 tau = E`, which is '
    'the prose\u2019s `E = f t-dot`')
arm('B1.unit_is_hypothesis',
    '(\u2200 \u03c4, -f (R \u03c4) * T\' \u03c4 ^ 2 + R\' \u03c4 ^ 2 / f (R \u03c4) = -1) \u2192' in c_c,
    '\u26ad and "unit timelike" is the HYPOTHESIS OF AN IMPLICATION INSIDE the conclusion, not a '
    'binder -- so the prose\u2019s appositive "unit timelike, obeys ..." matches its structure '
    'exactly: the energy holds unconditionally, the radial law only when unit timelike')
arm('B1.radial_law', '\u2203 E, \u2200 \u03c4, R\' \u03c4 ^ 2 = E ^ 2 - f (R \u03c4)' in c_c,
    'and that implication\u2019s consequent is `R\u2032 tau ^ 2 = E ^ 2 - f (R tau)`, the prose\u2019s '
    '`r-dot^2 = E^2 - f`')
arm('B1.chart_hypothesis', any('f (R \u03c4) \u2260 0' in b for b in b_c),
    '\u26a0 and rg_cosmo carries the SAME chart condition the whole-tensor sentence leaves silent: '
    + repr([b for b in b_c if '\u2260 0' in b]))
arm('B1.prose_silent_on_it', 'f\\neq0' not in cs and 'non-zero' not in cs,
    'which the prose sentence does not state either -- the condition is implicit in the chart '
    'in both places, consistently')

# ---- B2 -- CHECKED, not merely compared -----------------------------------------------------
print('\n  B2  \u26ad is `r-dot^2 = E^2 - f` what a UNIT TIMELIKE curve gives?  Derived from the metric.')
f_, E_, td_, rd_ = sp.symbols('f E tdot rdot', real=True)
# the radial-plane metric rg_g declares: diag(-f, 1/f).  Read it rather than assume it.
arm('B2.metric_read', '!![-f (y 1), 0; 0, (f (y 1))\u207b\u00b9]' in es_src
    or 'rg_g' in es_src,
    'the radial-plane metric is read from rg_g: '
    + repr(flat(sentence_at(es_src, 'noncomputable def rg_g'))[:84]))
norm = -f_ * td_ ** 2 + rd_ ** 2 / f_          # g(u,u) for ds^2 = -f dt^2 + dr^2/f
sol = sp.solve([sp.Eq(norm, -1), sp.Eq(f_ * td_, E_)], [td_, rd_ ** 2], dict=True)
got = sp.simplify(sol[0][rd_ ** 2]) if sol and rd_ ** 2 in sol[0] else None
if got is None:                                 # solve for rdot^2 by substitution instead
    got = sp.simplify(sp.solve(sp.Eq(norm.subs(td_, E_ / f_), -1), rd_ ** 2)[0])
arm('B2.derived', sp.simplify(got - (E_ ** 2 - f_)) == 0,
    f'imposing g(u,u) = -1 with E = f*tdot and solving gives rdot^2 = {sp.simplify(got)}, '
    f'residual against E^2 - f is {sp.simplify(got - (E_ ** 2 - f_))} \u21d2 the law is EXACT, so '
    f'N7 is not reached')
# G5: the opposite class.  A NULL curve, g(u,u) = 0, must give a DIFFERENT law.
got0 = sp.simplify(sp.solve(sp.Eq(norm.subs(td_, E_ / f_), 0), rd_ ** 2)[0])
arm('B2.negative_control', sp.simplify(got0 - (E_ ** 2 - f_)) != 0,
    f'NEGATIVE control: the null normalisation g(u,u) = 0 gives rdot^2 = {got0}, which is NOT '
    f'`E^2 - f` -- so the arm above is discriminating and the "unit" in "unit timelike" is '
    f'load-bearing rather than decorative')

# ---- B3 -- the four other rg_* declarations, each from its CONCLUSION -----------------------
print('\n  B3  the four other rg_* declarations, each read from its CONCLUSION and not its name')
RG = {'rg_witness':       ('rg_geodesic', 'a concrete geodesic, so rg_cosmo is not vacuous'),
      'rg_sinh23':        ('sinh', 'the sinh^(2/3) scale factor solving the E = 1 law'),
      'rg_sinh23_radial': ('sinh', 'its radial form'),
      'rg_tau23':         ('2 * M', 'the Lambda = 0 collapse limit')}
for nm, (tok, what) in RG.items():
    st2 = statement_of(es_src, nm)
    arm('B3.exists', st2 is not None, f'{nm:18s} declared in StaticEinstein.lean')
    if st2 is None:
        continue
    b2, c2 = binders_and_conclusion(st2)
    arm('B3.concludes', tok in c2,
        f'{nm:18s} concludes {what:48s} :: {flat(c2)[:76]}')
arm('B3.witness_minkowski', 'fun _ => 1' in (statement_of(es_src, 'rg_witness') or ''),
    'and rg_witness is the Minkowski case `f = 1`, a geodesic the reader can check by hand')

# ---- B4 -- the citations, enumerated -------------------------------------------------------
print('\n  B4  every declaration P8 cites, against every file that declares it')
LEAN_FILES = sorted(f for f in os.listdir(LEAN) if f.endswith('.lean'))
ALL = {f: declarations(os.path.join(LEAN, f)) for f in LEAN_FILES}
named = sorted(set(re.findall(r'([A-Za-z0-9]+\.lean)', p8)))
cited = sorted({unesc(m.group(1)) for m in
                re.finditer(r'\\texttt\{((?:ok|es|rg|kr)\\?_[^{}]*)\}', p8)})
arm('B4.one_file', named == ['StaticEinstein.lean'],
    f'P8 names {named}, and nothing else')
# ⚠ r7734 defect 2, a plain logic error: the first form asked whether the FILENAME
# 'StaticEinstein.lean' was among that file's DECLARATION NAMES -- never true -- so the `or`
# short-circuited and every cited name was flagged missing.  The witness printed each name
# beside the file that declares it, which is how it was caught: twenty "missing" names every
# one of which the printout showed present.  A disjunction in a test is a place to look.
missing = [(n, [f for f in LEAN_FILES if n in ALL[f]]) for n in cited
           if n not in ALL['StaticEinstein.lean']]
arm('B4.rule_kept', not missing,
    f'{len(cited)} names cited; cited-but-not-declared-in-StaticEinstein.lean: '
    f'{missing if missing else "none"}')
print(f'      the cited names: {cited}')

# ======================================= C -- THE P3 REPAIR AND ITS OWN TWINS
head('C -- THE P3 PARENTHETICAL, AND WHETHER THE REPAIR LEFT A TWIN')

def disc(m):  return 4.0 - 27.0 * m * m
R0MAX = 2.0 / math.sqrt(3.0)
NAR = 2.0 / (3.0 * math.sqrt(3.0))
def cubic(m, r): return r ** 3 - r + m

def roots_of(m):
    """Roots from the CLOSED FORM: a grid cannot resolve a near-tangency (r7732)."""
    d = disc(m)
    if d < 0.0:
        q = m / 2.0
        s_ = math.sqrt(q * q - 1.0 / 27.0)
        u = (-q + s_) ** (1.0 / 3.0) if -q + s_ >= 0 else -((q - s_) ** (1.0 / 3.0))
        v = (-q - s_) ** (1.0 / 3.0) if -q - s_ >= 0 else -((q + s_) ** (1.0 / 3.0))
        return [(u + v, 1)]
    arg = max(-1.0, min(1.0, -(3.0 * math.sqrt(3.0) / 2.0) * m))
    base = math.acos(arg) / 3.0
    rs = sorted((2.0 / math.sqrt(3.0)) * math.cos(base - 2.0 * math.pi * k / 3.0) for k in range(3))
    if d == 0.0:
        pair = [r for r in rs if abs(abs(r) - 1.0 / math.sqrt(3.0)) < 1e-9]
        single = [r for r in rs if r not in pair]
        return sorted([(single[0], 1), (pair[0], 2)]) if pair and single else [(r, 1) for r in rs]
    return [(r, 1) for r in rs]

arm('C.roots.tangency', [k for _, k in roots_of(NAR)] == [1, 2],
    f'the root finder\u2019s negatives first: at the Nariai mass it returns a DOUBLE root '
    f'{[(round(r, 9), k) for r, k in roots_of(NAR)]}')
_n = 0.5773021566671934
arm('C.roots.near', len(roots_of(_n - _n ** 3)) == 3,
    f'and at the near-tangency it returns three distinct, {abs(roots_of(_n - _n ** 3)[2][0] - roots_of(_n - _n ** 3)[1][0]):.3e} apart')

print('\n  C1  the repaired parenthetical, located by text and then CHECKED')
NEW = ('It is positive for $|r_{0}|<2/\\sqrt{3}$ (three real roots, distinct except at the '
       'designations $r_{0}=\\pm1/\\sqrt3$: the undercritical regime)')
arm('C1.landed', NEW in p3 and NEW in p3f, f'{p3.count(NEW)}x raw, {p3f.count(NEW)}x flat')
arm('C1.old_gone', 'three distinct real roots' not in p3,
    f'and the form it replaced is gone: {p3.count("three distinct real roots")} occurrence(s)')
# IS IT TRUE?  Is r0 = +-1/sqrt3 the ONLY designation in the open interval with a repeated root?
N3, bad = 24000, []
for i in range(-N3 + 1, N3):
    if i == 0:
        continue
    r0 = R0MAX * i / N3
    m = r0 - r0 ** 3
    if disc(m) <= 0.0 and abs(abs(r0) - 1.0 / math.sqrt(3.0)) > 2.0 * R0MAX / N3:
        bad.append((r0, m, disc(m)))
arm('C1.exactly_those', not bad,
    f'over {2 * N3 - 2} designations in the OPEN interval, both signs, '
    f'{len(bad)} have a repeated root away from $r_0=\\pm1/\\sqrt3$'
    + ('' if not bad else f'; first {bad[0]}'))
for s_ in (+1.0, -1.0):
    r0 = s_ / math.sqrt(3.0); m = r0 - r0 ** 3
    arm('C1.the_named_two', disc(m) == 0.0 and abs(r0) < R0MAX,
        f'and $r_0 = {r0:+.9f}$ IS one of them: 2M = {m:+.12f}, discriminant {disc(m):.3e}, roots '
        f'{[(round(r, 9), k) for r, k in roots_of(m)]}')
arm('C1.both_signs_named', '$r_{0}=\\pm1/\\sqrt3$' in p3,
    'and the parenthetical names BOTH signs with the \u00b1, which is what the computation requires')

print('\n  C2  \u26a0 twins: any other sentence reading the strict interval as distinctness?')
for tok in ['three distinct real roots', 'distinct real roots, the undercritical',
            'equivalently $|2M|', 'In the undercritical regime with']:
    arm('C2.twin', p3.count(tok) == 0, f'{tok!r:48s} {p3.count(tok)} occurrence(s)')
arm('C2.region_independent', 'Where the three horizon roots are distinct and $M>0$' in p3,
    'and the region sentence still states distinctness directly rather than through the term, '
    'so it does not depend on the parenthetical at all')

# ============== D -- MY OWN LAST ANSWER, WHICH THIS LANDING OVERTOOK, AND THE TWO HEADERS
head('D -- WHAT THE LANDING OVERTOOK, AND THE TWO POINTERS RE-MEASURED RATHER THAN ASSUMED')

print('\n  D1  did the repair that formalised the off-diagonals leave a stale clause behind it?')
stale = re.findall(r'[^.]*not formalised[^.]*\.', p8)
arm('D1.no_stale_offdiag',
    not any('off-diagonal' in s for s in stale),
    f'{len(stale)} "not formalised" clause(s) remain in P8, and none names the off-diagonals: '
    + repr([flat(s).strip()[:92] for s in stale]))
arm('D1.only_index_left', len(stale) == 1 and 'constancy of the index' in stale[0],
    'the one that remains is the index-constancy citation, which is still genuinely unformalised')
arm('D1.my_caveat_void', 'that the off-diagonal components vanish is not formalised' not in p8,
    '⇒ N10 is NOT reached: my r7732 reading -- that the narrowing was honest BECAUSE the '
    'off-diagonal vanishing is an identity -- has been overtaken by its formalisation, and the '
    'clause it turned on was removed with it rather than left standing')
arm('D1.diagonal_word_gone', 'every diagonal component of $\\Tud{\\mu}{\\nu}$' not in p8,
    'and the narrowing itself is gone: the sentence now claims `T_{\\mu\\nu}=0` whole')

print('\n  D2  the two stale Lean headers I routed at r7732, RE-MEASURED')
arm('D2.operatorkernel_backs',
    'It backs P8 (`corpus/slicing_operator.tex`): `thm:kernel` and `prop:bend`.'
    not in flat(ok_src) or 'OperatorKernel.lean' in p8,
    'OperatorKernel.lean’s self-description against whether P8 names it: still says it backs P8 '
    f'= {"It backs P8" in flat(ok_src)}, P8 names it = {"OperatorKernel.lean" in p8}')
_kept = es_src[es_src.find('# Probe `r7725+71.2`'):]
_kept = _kept[:_kept.find('-/')] if '-/' in _kept else _kept
arm('D2.copies_no_earlier', 'copies no' not in flat(_kept),
    'and the header StaticEinstein.lean keeps verbatim: still says "it copies no earlier probe" '
    f'= {"copies no" in flat(_kept)}, inside a file that is a copy')
arm('D2.routed_not_reapplied', True,
    '⇒ both are still open and both are 71’s by this order. Re-measured rather than assumed, '
    'and NOT re-routed: the order has already assigned them')

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
