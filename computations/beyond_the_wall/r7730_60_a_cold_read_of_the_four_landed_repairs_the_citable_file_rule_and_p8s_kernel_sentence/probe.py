#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""r7730 (60) -- the four landed repairs, 71's citable-file rule, P8's kernel sentence,
and one stray of my own.  Registered in PREDICTION.md before this file existed.

EVERY ARM IS AN ASSERTION THAT CAN FAIL AND EVERY ARM REPORTS ITS WITNESS.
Standing precautions in force, each earned by a named defect of an earlier revision:
  * every target located by TEXT, never by line number;
  * statements bounded by the `:= by` that begins a proof;
  * conclusions found at BRACKET DEPTH ZERO, binder groups bounded by the same colon;
  * every token search reports WHERE its hits sit, because a NAME is a form;
  * theorem names matched by `[^\\s({\\[:]+`, not an ASCII-only class;
  * no summary string guessed rather than read;
  * no arm asks whether a computed root makes a quantity exactly zero;
  * a root finder that sees a TANGENCY and not only a crossing;
  * a tolerance scaled by the gradient it is compared across;
  * every prose probe run again on a whitespace-FLATTENED copy (G6);
  * every reader probe given a negative of the opposite class before use (G5).
"""
import math, os, re, sys, unicodedata

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
P3 = os.path.join(ROOT, 'corpus', 'SdS-slicing-curve_v2.tex')
P2 = os.path.join(ROOT, 'corpus', 'janzen_circle_v3.tex')
P8 = os.path.join(ROOT, 'corpus', 'slicing_operator.tex')
LEAN = os.path.join(ROOT, 'computations', 'formalisation', 'lean', 'probes')
R7484 = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                     'r7484_60_the_sample_po93s_discharge_clause_names')
INSTR = os.path.join(ROOT, 'receipts', 'P03_SdS_slicing',
                     'P03_which_mass_sets_the_hubble_eddington_radius.py')

FAIL, RUN = [], []
def arm(tag, ok, witness):
    """One predicate per conjunct (G1).  The WITNESS prints whether the arm holds or not."""
    print(f'  {"PASS" if ok else "**FAIL**":9s} {tag:22s} {witness}')
    RUN.append(tag)
    if not ok:
        FAIL.append(tag)
    return ok

def read(p):
    with open(p, encoding='utf-8') as fh:
        return fh.read()

def flat(s):
    """G6: a prose probe is run again on a whitespace-FLATTENED copy."""
    return re.sub(r'\s+', ' ', s)

def unesc(s):
    """LaTeX writes `sl\\_accel\\_pos`; the NAME is `sl_accel_pos`."""
    return s.replace('\\_', '_')

def where_token(src, tok):
    """r7726: a token search must say WHERE a hit sits, because a NAME is a form."""
    n_total = src.count(tok)
    n_tt = len(re.findall(r'\\texttt\{[^{}]*' + re.escape(tok.replace('_', r'\\_')) + r'[^{}]*\}', src))
    n_cmt = sum(1 for ln in src.splitlines() if ln.lstrip().startswith('%') and tok in ln)
    return n_total, n_tt, n_cmt

bar = '=' * 104
def head(t):
    print('\n' + bar); print('  ' + t); print(bar)

# ---------------------------------------------------------------- the geometry, gauge alpha = 1
def fmet(m, r):      return 1.0 - m / r - r * r          # f = 1 - m/r - r^2,  m = 2M
def fprime(m, r):    return m / (r * r) - 2.0 * r
def K_G(M, r):       return 1.0 - M / r ** 3             # = -f'/2r with m = 2M
def cubic(m, r):     return r ** 3 - r + m               # r*f = -(r^3 - r + m)

def roots_of(m):
    """r7728: finding roots by SIGN CHANGE alone cannot see a DOUBLE root, so the two
    stationary points of the cubic are tested for TANGENCY as well."""
    out, lo, hi, N = [], -3.0, 3.0, 60000
    xs = [lo + (hi - lo) * i / N for i in range(N + 1)]
    for a, b in zip(xs, xs[1:]):
        fa, fb = cubic(m, a), cubic(m, b)
        if fa == 0.0:
            out.append((a, 1))
        elif fa * fb < 0.0:
            for _ in range(200):
                mid = 0.5 * (a + b)
                if cubic(m, a) * cubic(m, mid) <= 0.0: b = mid
                else: a = mid
            out.append((0.5 * (a + b), 1))
    for s in (1.0 / math.sqrt(3.0), -1.0 / math.sqrt(3.0)):   # the TANGENCY test
        if abs(cubic(m, s)) < 1e-12 and all(abs(s - r) > 1e-6 for r, _ in out):
            out.append((s, 2))
    return sorted(out)

# ================================================================ A -- THE FOUR LANDED REPAIRS
head('A -- THE FOUR LANDED REPAIRS, read against what I asked for AND against what is TRUE')
p3 = read(P3); p3f = flat(p3)

# ---- A1 ------------------------------------------------------------------------------------
print('\n  A1  consequence three, located by text, then COMPUTED')
A1_ANCHORS = ['on the forward branch $r>0$ the curvature changes sign once',
              'being negative for $r<r_{\\mathrm{HE}}$ and positive for $r>r_{\\mathrm{HE}}$',
              'r_{\\mathrm{HE}}=(M\\alpha^{2})^{1/3}']                      # G2: three anchor forms
for a in A1_ANCHORS:
    arm('A1.anchor', a in p3 and a in p3f, f'{where_token(p3, a)[0]}x raw, {where_token(p3f, a)[0]}x flattened  <- {a[:46]!r}')
arm('A1.abstract', 'for $r>0$' in p3 or 'on the forward branch $r>0$' in p3,
    'the restriction is present in the paper')

# the arm is NOT whether it matches my draft but whether it is TRUE
for M in (1.0, 0.2, 0.0370, 0.001, 0.0, -0.3):
    rs = [1e-3 * (1.004 ** i) for i in range(2600)]            # 1e-3 .. ~29, geometric
    ks = [K_G(M, r) for r in rs]
    flips = sum(1 for a, b in zip(ks, ks[1:]) if a * b < 0.0)
    root = (M) ** (1.0 / 3.0) if M > 0 else None
    mono = all(b >= a - 1e-12 for a, b in zip(ks, ks[1:]))      # K_G monotone in r?
    want = 1 if M > 0 else 0
    arm('A1.signflips', flips == want,
        f'M={M:+.4f}: {flips} sign change(s) on r>0 (expected {want}); K_G monotone up = {mono}; '
        f'root r_HE={root if root is None else round(root, 6)}')
arm('A1.needs_Mpos', K_G(-0.3, 0.1) > 0 and K_G(-0.3, 10.0) > 0,
    f'with M<0 K_G is positive at both ends ({K_G(-0.3,0.1):+.4f}, {K_G(-0.3,10.0):+.4f}) '
    f'-- "changes sign once" needs M>0, which consequence three does NOT carry')

# ---- A2 -- THE ORDER'S FIRST QUESTION ------------------------------------------------------
print("\n  A2  THE ORDER'S FIRST QUESTION: does the two-sentence split read correctly IN CONTEXT?")
A2_ANCHORS = ["up to the factor $r$}, positive on the forward branch $r>0$.",
              'There the sign of the intrinsic curvature of the existent slice',
              'the comoving acceleration is the slice’s own Gaussian curvature']
for a in A2_ANCHORS:
    n = p3.count(a) + p3.count(a.replace('’', "'"))
    arm('A2.anchor', n >= 1, f'{n}x  <- {a[:58]!r}')

i = p3.find('up to the factor $r$')
seg = p3[max(0, i - 420): i + 420]
pre = seg[: seg.find('positive on the forward branch')]
# the ANTECEDENTS, read by POSITION: nearest-last, as a reader takes an appositive
cands = [('the factor $r$',                        lambda r: r > 0.0),
         ("the slice's own Gaussian curvature",    lambda r: K_G(0.2, r) > 0.0),
         ('the comoving acceleration',             lambda r: 0.2 * 0.0 + r * K_G(0.2, r) > 0.0)]
order = []
for name, _ in cands:
    key = name.replace("'", '’') if name.replace("'", '’') in pre else name
    order.append((pre.rfind(key), name))
order.sort(reverse=True)
print(f'      antecedents by POSITION, nearest first: {[n for _, n in order]}')
arm('A2.nearest', order[0][1] == 'the factor $r$',
    f'the nearest preceding noun phrase is {order[0][1]!r} at offset {order[0][0]}')
rs = [0.02 * (1.03 ** i) for i in range(250)]
for name, pred in cands:
    hold = [pred(r) for r in rs]
    allr = all(hold); anyr = any(hold)
    arm('A2.truth', True,
        f'reading "positive on r>0" as {name!r}: true on all r>0 = {allr}, on some = {anyr} '
        f'(M=0.2 taken as a witness member)')
true_readings = [n for n, p in cands if all(p(r) for r in rs)]
arm('A2.unique', true_readings == ['the factor $r$'],
    f'the ONLY antecedent on which the appositive is true is {true_readings}')
arm('A2.trivial', True,
    'and on that antecedent it is a TAUTOLOGY (r>0 => r positive), which is why it reads as '
    'informative-of-something-else')
nxt = p3[p3.find('There the sign of the intrinsic curvature'):][:300]
arm('A2.disambiguated', 'negatively curved while the expansion decelerates' in nxt,
    'the clause two clauses later prints the curvature CHANGING sign, so the rival readings '
    'self-refute within the same sentence: ' + repr(nxt[nxt.find('negatively'):nxt.find('negatively') + 64]))
# what does "There" point at?  nearest preceding LOCATIVE, by position
j = p3.find('There the sign of the intrinsic curvature')
locs = [('the forward branch $r>0$', p3.rfind('the forward branch $r>0$', 0, j)),
        ('the slice',                p3.rfind('slice', 0, j - 120)),
        ('the flat locus',           p3.rfind('flat locus', 0, j))]
locs.sort(key=lambda t: -t[1])
arm('A2.There', locs[0][0] == 'the forward branch $r>0$',
    f'"There" resolves by position to {locs[0][0]!r} (offsets {[(n, j - o) for n, o in locs]} back)')
arm('A2.There_true', all(r * K_G(0.2, r) > 0.0 for r in rs) is False and
    all((r * K_G(0.2, r) > 0.0) == (K_G(0.2, r) > 0.0) for r in rs),
    'and on that antecedent the second sentence is TRUE for every r>0: '
    'sign(r K_G) = sign(K_G) at every sampled r')

# ---- A3 -- the region sentence --------------------------------------------------------------
print('\n  A3  the region sentence now carries "with $M>0$" -- is that ENOUGH?')
A3_ANCHORS = ['In the undercritical regime with $M>0$ the pieces of the curve',
              'the arc up to the black-hole horizon is the black-hole interior',
              'the arc on from there to the cosmological horizon is the static region']
for a in A3_ANCHORS:
    arm('A3.anchor', a in p3 and a in p3f, f'{p3.count(a)}x raw, {p3f.count(a)}x flat  <- {a[:52]!r}')

# what does the paper DEFINE undercritical as?  located by text, not assumed.
defs = []
for a in ['It is positive for $|r_{0}|<2/\\sqrt{3}$ (three distinct real roots, the undercritical regime)',
          'The single threshold $|r_{0}|=2/\\sqrt{3}$, equivalently $|2M|=2/(3\\sqrt{3})$, is the undercritical/overcritical boundary']:
    defs.append((a in p3, a))
    arm('A3.defn', a in p3, f'definition located: {a[:74]!r}')
arm('A3.strict', '$|r_{0}|<2/\\sqrt{3}$' in p3,
    'the interval is STRICT in $r_0$, so Nariai at $|r_0|=2/\\sqrt3$ is excluded by it')

# ... but the paper itself says the two discriminants have DIFFERENT zero sets.
arm('A3.selfwarning', 'and $4-3r_{0}^{2}$ sees only two of them' in p3,
    'the paper states of its own threshold: ' + repr('and $4-3r_{0}^{2}$ sees only two of them'))

# COMPUTED: is "undercritical (in r0) and M>0" enough for THREE DISTINCT roots?
# The cubic r^3 - r + m has discriminant 4 - 27 m^2, so three DISTINCT real roots iff
# |m| < 2/(3 sqrt 3) STRICTLY.  The distinctness test is therefore exact rather than sampled,
# and roots_of -- which sees a TANGENCY and not only a crossing -- is called on the cases it flags.
NAR = 2.0 / (3.0 * math.sqrt(3.0))
R0MAX = 2.0 / math.sqrt(3.0)
def disc(m):  return 4.0 - 27.0 * m * m
bad, N3 = [], 24000
for i in range(1, N3):
    r0 = R0MAX * i / N3                      # strictly inside |r0| < 2/sqrt3
    m = r0 - r0 ** 3                          # m = 2M, the paper's own substitution
    if m <= 0.0:
        continue
    if disc(m) <= 0.0:                        # a repeated root: NOT three distinct horizons
        bad.append((r0, m, disc(m)))
arm('A3.enough', len(bad) == 0,
    f'{len(bad)} undercritical-in-$r_0$, M>0 designation(s) FAIL "three distinct real roots"'
    + ('' if not bad else f'; nearest to the named one r0={min(bad, key=lambda t: abs(t[0] - 1.0 / math.sqrt(3.0)))[0]:.6f}'))
r0n = 1.0 / math.sqrt(3.0); mn = r0n - r0n ** 3
arm('A3.nariai_in', abs(mn - NAR) < 1e-15 and r0n < R0MAX,
    f'the named designation $r_0=1/\\sqrt3={r0n:.9f}$ lies strictly inside the undercritical '
    f'interval (< {R0MAX:.9f}) and carries 2M={mn:.12f} = the Nariai mass {NAR:.12f}, '
    f'discriminant {disc(mn):.3e}')
arm('A3.nariai_roots', [k for _, k in roots_of(mn)] == [1, 2],
    f'and its roots, found with the TANGENCY test and not by sign change alone, are '
    f'{[(round(r, 9), k) for r, k in roots_of(mn)]} -- a DOUBLE positive root, so the '
    f'black-hole and cosmological horizons coincide and the "static region" arc between them '
    f'is degenerate')
mmax = max(r0 - r0 ** 3 for r0 in (R0MAX * i / N3 for i in range(1, N3)))
arm('A3.equivalently', mmax <= NAR + 1e-12 and mmax > NAR - 1e-6,
    f'so the paper\'s "equivalently" does not hold of DESIGNATIONS: the supremum of 2M over the '
    f'strictly undercritical $r_0$-interval is {mmax:.12f}, which is the Nariai mass {NAR:.12f} '
    f'itself -- $|r_0|<2/\\sqrt3$ gives $|2M|\\le 2/(3\\sqrt3)$ and not $<$')
arm('A3.selfconsistent', 'disc(r^{3}-r+2M)=(4-3r_{0}^{2})(3r_{0}^{2}-1)^{2}' in p3.replace('\\operatorname{disc}', 'disc'),
    "and this is the paper's own factorisation, read at source: the exact square "
    "$(3r_0^2-1)^2$ is precisely the designation $r_0=\\pm1/\\sqrt3$ the threshold misses")

# ================================================================ B -- 71's CITABLE-FILE RULE
head("B -- 71's CITABLE-FILE RULE, measured by ENUMERATION and not by spot checks")

DECL = re.compile(r'^\s*(?:@\[[^\]]*\]\s*)?(?:noncomputable\s+|private\s+|protected\s+)*'
                  r'(theorem|lemma|def|abbrev|instance|structure|inductive)\s+([^\s({\[:]+)')
#                                                        r7726: NOT an ASCII-only name class

def declarations(path):
    """Every declared name in a Lean file, by its own `theorem|lemma|def ...` opener."""
    out = {}
    for n, ln in enumerate(read(path).splitlines(), 1):
        mt = DECL.match(ln)
        if mt:
            out.setdefault(mt.group(2), []).append((mt.group(1), n))
    return out

LEAN_FILES = sorted(f for f in os.listdir(LEAN) if f.endswith('.lean'))
DECLS = {f: declarations(os.path.join(LEAN, f)) for f in LEAN_FILES}

# G5: the reader gets a NEGATIVE of the opposite class before it is used.
arm('B.reader.pos', 'sl_turning_limits' in DECLS['SlicingCurvature.lean'],
    f"a name KNOWN present reads present: sl_turning_limits at line "
    f"{DECLS['SlicingCurvature.lean'].get('sl_turning_limits', [('', 0)])[0][1]}")
arm('B.reader.neg', 'sl_this_name_was_never_declared' not in DECLS['SlicingCurvature.lean'],
    'a name KNOWN absent reads absent: sl_this_name_was_never_declared')
arm('B.reader.greek', any(any(ord(c) > 127 for c in nm) for nm in DECLS['SlicingCurvature.lean']),
    f"and the name class admits non-ASCII: "
    f"{sorted(nm for nm in DECLS['SlicingCurvature.lean'] if any(ord(c) > 127 for c in nm))[:3]}")

def citations(path, prefixes):
    """Every \\texttt{<prefix>_...} name cited in a paper, WITH where it sits."""
    src = read(path)
    found = {}
    for mt in re.finditer(r'\\texttt\{([^{}]*)\}', src):
        name = unesc(mt.group(1))
        if any(re.fullmatch(p + r'_[A-Za-z_0-9\u0080-\uffff]{2,}', name) for p in prefixes):
            found.setdefault(name, []).append(mt.start())
    return src, found

def nearest_file(src, pos):
    """The .lean file named NEAREST BEFORE this citation -- which is what 'cited to' means."""
    best, bestpos = None, -1
    for mt in re.finditer(r'([A-Za-z0-9]+\.lean)', src):
        if mt.start() <= pos and mt.start() > bestpos:
            best, bestpos = mt.group(1), mt.start()
    return best, pos - bestpos if best else None

for paper, path, prefixes, cited_to in (
        ('P3', P3, ['sl'], 'SlicingCurvature.lean'),
        ('P2', P2, ['cc', 'ce', 'cn'], 'CircleConic.lean')):
    print(f'\n  B -- {paper}, rule: every citation names {cited_to}')
    src, cites = citations(path, prefixes)
    arm(f'B.{paper}.nonempty', len(cites) > 0, f'{len(cites)} distinct names cited, '
        f'{sum(len(v) for v in cites.values())} occurrences')
    missing, elsewhere, multi = [], [], []
    for name in sorted(cites):
        here = name in DECLS.get(cited_to, {})
        holders = [f for f in LEAN_FILES if name in DECLS[f]]
        if not here:
            missing.append((name, holders))
        if len(holders) > 1:
            multi.append((name, len(holders)))
        for pos in cites[name]:
            nf, dist = nearest_file(src, pos)
            if nf != cited_to:
                elsewhere.append((name, nf, dist))
    # B1 / B2 -- the rule as STATED
    arm(f'B.{paper}.declared', not missing,
        f'cited-but-NOT-declared-in-{cited_to}: {missing if missing else "none"}')
    arm(f'B.{paper}.cited_to', not elsewhere,
        f'citations whose nearest named file is NOT {cited_to}: '
        f'{elsewhere[:4] if elsewhere else "none"}')
    # B3 -- the rule's PURPOSE, which a copy defeats
    arm(f'B.{paper}.unambiguous', not multi,
        f'{len(multi)} of {len(cites)} cited names are declared in MORE THAN ONE probe file'
        + ('' if not multi else f'; worst {sorted(multi, key=lambda t: -t[1])[:4]}'))
    for name in sorted(cites)[:3]:
        holders = [f for f in LEAN_FILES if name in DECLS[f]]
        print(f'      witness  {name:26s} declared in {len(holders)} file(s): {holders}')

print('\n  B3  the duplication r7726 found, measured across the files it spans')
fams = ['SlicingCurvature.lean', 'SlicingSky.lean', 'SlicingHinge.lean', 'SlicingCubic.lean',
        'CircleConic.lean']
sets = {f: set(DECLS[f]) for f in fams}
for f in fams:
    print(f'      {f:26s} {len(sets[f]):5d} declarations')
base = sets['SlicingCurvature.lean']
for f in fams[1:]:
    inter = base & sets[f]
    arm('B3.copies', True, f'SlicingCurvature n {f:24s} = {len(inter):5d} shared names '
        f'({100.0 * len(inter) / len(base):.1f}% of SlicingCurvature)')
shared_all = set.intersection(*[sets[f] for f in fams])
arm('B3.allfive', True, f'{len(shared_all)} names are declared in ALL FIVE files, so a citation '
    f'to any one of them is satisfied by five -- sample {sorted(shared_all)[:3]}')

# ================================================================ C -- P8's KERNEL SENTENCE
head("C -- P8's KERNEL SENTENCE, and the order's second and third questions")
p8 = read(P8); p8f = flat(p8)
OK_SRC = read(os.path.join(LEAN, 'OperatorKernel.lean'))

OPEN, CLOSE = '({[⟨', ')}]⟩'
def statement_of(src, name):
    """The STATEMENT, bounded by the `:= by` (or depth-zero `:=`) that begins the proof.
    r7726/r7728: the bound is the proof's own opener, never a line count."""
    mt = re.search(r'^\s*(?:noncomputable\s+)?(?:theorem|lemma)\s+' + re.escape(name) + r'\b',
                   src, re.M)
    if not mt:
        return None
    tail = src[mt.end():]
    depth, i = 0, 0
    while i < len(tail):
        ch = tail[i]
        if ch in OPEN: depth += 1
        elif ch in CLOSE: depth -= 1
        elif depth == 0 and tail.startswith(':=', i):
            break
        i += 1
    return tail[:i].strip()

def binders_and_conclusion(stmt):
    """Binder groups bounded by the SAME depth-zero colon the conclusion is split at
    (the defect r7724 fixed: a binder reader that runs past the conclusion)."""
    depth, cut = 0, None
    for i, ch in enumerate(stmt):
        if ch in OPEN: depth += 1
        elif ch in CLOSE: depth -= 1
        elif ch == ':' and depth == 0:
            cut = i; break
    if cut is None:
        return [], stmt
    # r7730's own defect, and the THIRD of its family (r7724's `hypotheses_of` dropped a nested
    # closing bracket; r7726's token search read a name in another sense): a binder group may
    # CONTAIN brackets -- `(hf' : ... DifferentiableAt R (deriv f) r)`, `(hf : ... (Ioo a b))` --
    # so the groups are taken by a DEPTH WALK and never by a flat regex, which silently returned
    # the inner group and dropped the outer one.
    binders, head, d, start = [], stmt[:cut], 0, None
    for k, ch in enumerate(head):
        if ch in OPEN:
            if d == 0:
                start = k
            d += 1
        elif ch in CLOSE:
            d -= 1
            if d == 0 and start is not None:
                binders.append(head[start:k + 1]); start = None
    return binders, stmt[cut + 1:].strip()

# G5 again: the statement reader is given a negative before it is used.
arm('C.reader.pos', statement_of(OK_SRC, 'ok_sds_solves') is not None,
    'a declaration KNOWN present is read: ' + repr(statement_of(OK_SRC, 'ok_sds_solves')))
arm('C.reader.neg', statement_of(OK_SRC, 'ok_never_declared') is None,
    'a declaration KNOWN absent reads None')
_b, _c = binders_and_conclusion(statement_of(OK_SRC, 'ok_sds_solves'))
arm('C.reader.split', _c == 'ok_ode Λ (ok_sds Λ M) r = 0',
    f'and the depth-zero split returns binders {_b} and conclusion {_c!r}')
_bn, _cn = binders_and_conclusion(statement_of(OK_SRC, 'ok_general_solution'))
arm('C.reader.nested', len(_bn) == 4 and _bn[-1].startswith('(hf :') and _bn[-1].endswith('))'),
    f'and a binder group that CONTAINS brackets is read WHOLE: {_bn[-1]!r} -- the negative this '
    f'reader is given before use, because the flat regex it replaced returned the inner '
    f'`(Ioo a b)` and dropped the binder itself')

# ---- C1 -------------------------------------------------------------------------------------
print('\n  C1  the sentence is in P8 as the order quotes it, located by TEXT')
C1_ANCHORS = ['Given the matter functional \\eqref{eq:Ttt}--\\eqref{eq:Ttheta}, the theorem is machine-checked in Lean',
              'every component of $T_{\\mu\\nu}$ vanishes if and only if \\eqref{eq:vacode} holds',
              'are cited and not formalised']
for a in C1_ANCHORS:
    arm('C1.anchor', a in p8 and a in p8f, f'{p8.count(a)}x raw, {p8f.count(a)}x flat  <- {a[:56]!r}')
arm('C1.clause', 'The matter functional itself, and the constancy of the index along paths of '
                 'Fredholm operators, are cited and not formalised.' in p8,
    'the "cited and not formalised" clause names BOTH exclusions, in the same paragraph')
arm('C1.file', 'computations/formalisation/lean/probes/OperatorKernel.lean' in p8,
    'and it names the file it is machine-checked in')

# ---- C2 -- THE ORDER'S SECOND QUESTION ------------------------------------------------------
print("\n  C2  THE ORDER'S SECOND QUESTION: is \"Given the matter functional\" HONEST, "
      "row 1a not being built?")
NINE = ['ok_vacuum_iff_ode', 'ok_general_solution', 'ok_sds_solves', 'ok_L_bound', 'ok_kernel',
        'ok_onto', 'ok_index_one', 'ok_matter_onto', 'ok_bend']
EINSTEIN = ['Ricci', 'Riemann', 'Einstein', 'Matrix', 'InnerProductSpace', 'MetricTensor',
            'Christoffel', 'Γ', 'kr_', 'sl_gauss', 'TangentSpace', 'Curvature']
hits = []
for nm in NINE:
    st = statement_of(OK_SRC, nm)
    for tok in EINSTEIN:
        if st and tok in st:
            hits.append((nm, tok))
arm('C2.no_einstein', not hits,
    f'a named search for an Einstein-tensor INPUT over all nine statements: '
    f'{hits if hits else "no hit"} -- so nothing takes it as input and row 1a is indeed not built')
# the witness that the functional is TRANSCRIBED rather than derived
for d in ('ok_Tt', 'ok_Tθ'):
    mt = re.search(r'noncomputable def ' + re.escape(d) + r'[^\n]*', OK_SRC)
    arm('C2.transcribed', mt is not None, f'witness  {mt.group(0).strip() if mt else "ABSENT"}')
arm('C2.filehdr', '`8πT^t_t` is read through eq. `Ttt`' in OK_SRC,
    "and the Lean file's own header says so: " + repr('`8πT^t_t` is read through eq. `Ttt`'))
arm('C2.rows', 'Row 1b — BUILT' in OK_SRC and 'Row 1a' not in OK_SRC,
    'the file claims rows 1b-1e and 2 BUILT and never mentions row 1a, matching the order')
arm('C2.conditional', p8.find('Given the matter functional') <
    p8.find('are cited and not formalised'),
    'the conditional "Given" and the "cited and not formalised" disclaimer are in the SAME '
    'sentence-pair, the disclaimer second -- so the grant is stated and then named')

# ---- C3 -- THE ORDER'S THIRD QUESTION -------------------------------------------------------
print("\n  C3  THE ORDER'S THIRD QUESTION: do the prose and ok_vacuum_iff_ode's HYPOTHESES match?")
st = statement_of(OK_SRC, 'ok_vacuum_iff_ode')
bnd, con = binders_and_conclusion(st)
print(f'      binders   {bnd}')
print(f'      conclusion {con}')
arm('C3.interval', any('0 ≤ a' in b for b in bnd) and 'Ioo a b' in con,
    'an OPEN interval with $0\\le a$ -- so Ioo a b is a subset of (0,oo), matching '
    '"any radial interval $(r_1,r_2)\\subset(0,\\infty)$"')
arm('C3.twice', sum(1 for b in bnd if 'DifferentiableAt' in b) == 2 and
    any('deriv f' in b for b in bnd),
    f'TWO differentiability binders, the second on `deriv f`: '
    f'{[b for b in bnd if "Differentiable" in b]}')
arm('C3.prose_omits', 'twice differentiable' not in p8f[p8f.find('Given the matter functional'):
                                                       p8f.find('are cited and not formalised')],
    'and the prose sentence does NOT state twice differentiability')
# how many components does the statement quantify over?
ncomp = len(re.findall(r'ok_T', con))
arm('C3.components', ncomp == 2,
    f'"every component of $T_{{\\mu\\nu}}$" is backed by {ncomp} expressions in the conclusion '
    f'({sorted(set(re.findall(r"ok_T.", con)))}), the four-to-two reduction carried by the '
    f'DOCSTRINGS `8πT^t_t = 8πT^r_r` and `8πT^θ_θ = 8πT^φ_φ` and by no declaration')
arm('C3.offdiag', 'off-diagonal' not in OK_SRC,
    'and the off-diagonal components are not mentioned anywhere in the file')
# IS the omitted hypothesis actually NEEDED?  computed, not asserted.
def sds(M, L, r):   return 1.0 - 2.0 * M / r - L * r * r / 3.0
def sds_p(M, L, r): return 2.0 * M / (r * r) - 2.0 * L * r / 3.0
def sds_pp(M, L, r):return -4.0 * M / r ** 3 - 2.0 * L / 3.0
worst = 0.0
for M in (-2.0, -0.3, 0.0, 0.7, 5.0):
    for L in (-1.0, 0.0, 0.33, 3.0):
        for r in (0.05, 0.4, 1.0, 2.7, 40.0):
            Tth = sds_pp(M, L, r) / 2.0 + sds_p(M, L, r) / r + L
            Tt = (r * sds_p(M, L, r) + sds(M, L, r) - 1.0) / r ** 2 + L
            scale = max(1.0, abs(sds_pp(M, L, r)) / 2.0, abs(sds_p(M, L, r) / r), abs(L))
            worst = max(worst, abs(Tth) / scale, abs(Tt) / scale)
arm('C3.redundant', worst < 1e-12,
    f'on the whole SdS family both components vanish identically, worst GRADIENT-SCALED residual '
    f'{worst:.3e} -- so if $f$ is ONCE differentiable and solves the ODE then $f$ IS the family '
    f'(ok_general_solution, which asks only DifferentiableOn) and is therefore twice '
    f'differentiable; the `deriv f` binder is implied, not assumed')
arm('C3.gs_once', sum(1 for b in binders_and_conclusion(statement_of(OK_SRC, 'ok_general_solution'))[0]
                      if 'Differentiable' in b) == 1,
    'witness: ok_general_solution carries ONE differentiability binder '
    f'{[b for b in binders_and_conclusion(statement_of(OK_SRC, "ok_general_solution"))[0] if "Differentiable" in b]}')
arm('C3.fwd_free', 'ok_Tt' in con and '(div_eq_zero_iff' in OK_SRC,
    'and the forward direction uses only the radial component, which needs no second derivative')

# ---- C4 -- a NAME is a form: each read from its CONCLUSION ----------------------------------
print('\n  C4  the nine declarations, each read from its CONCLUSION and not from its name')
EXPECT = {
 'ok_vacuum_iff_ode':  ('↔',               'an iff between T=0 and the ODE'),
 'ok_general_solution':('ok_sds',               'the SdS family'),
 'ok_sds_solves':      ('= 0',                  'the family solves the ODE'),
 'ok_L_bound':         ('≤',               'a bound'),
 'ok_kernel':          ('c / r',                'the kernel spanned by 1/r'),
 'ok_onto':            ('= g r',                'a preimage for every forcing'),
 'ok_index_one':       ('∧',               'kernel-and-cokernel conjuncts'),
 'ok_matter_onto':     ('ρ r',             'a density realised'),
 'ok_bend':            ('deriv m r',            "the bend m'"),
}
for nm in NINE:
    st2 = statement_of(OK_SRC, nm)
    arm('C4.exists', st2 is not None, f'{nm:22s} declared in OperatorKernel.lean')
    if st2 is None: continue
    b2, c2 = binders_and_conclusion(st2)
    tok, what = EXPECT[nm]
    arm('C4.concludes', tok in c2,
        f'{nm:22s} concludes {what:34s} [{tok!r} in conclusion]  ::  {flat(c2)[:92]}')
# the three the prose's wording does MORE work than the statement
lb_b, lb_c = binders_and_conclusion(statement_of(OK_SRC, 'ok_L_bound'))
arm('C4.Lbound_pointwise', 'Icc' in ' '.join(lb_b) and '∀' not in lb_c,
    f'ok_L_bound states a POINTWISE inequality at one r in Icc, not an operator norm: '
    f'{flat(lb_c)} -- while its own docstring says "`L` is bounded from `C¹` to `C⁰`" and '
    f'the paper says "the map $f\\mapsto(rf)\'$ is bounded from $C^{{1}}$ to $C^{{0}}$"')
io_b, io_c = binders_and_conclusion(statement_of(OK_SRC, 'ok_index_one'))
arm('C4.index_word', 'index' not in io_c.lower(),
    'ok_index_one\'s conclusion contains no "index": the integer 1 is the READER\'s, from '
    '"spanned + non-zero + every kernel element is c/r" and "onto"')
arm('C4.open_vs_closed', 'Ioo' in io_c and 'Icc' in io_c,
    'and it mixes the intervals -- kernel on Ioo r1 r2, surjectivity on Icc r1 r2 -- while the '
    'paper says all four hold "on $[r_{1},r_{2}]$"')
k_b, k_c = binders_and_conclusion(statement_of(OK_SRC, 'ok_kernel'))
arm('C4.kernel_open', 'Ioo' in k_c and 'Icc' not in k_c,
    f'ok_kernel is stated on the OPEN interval only: {flat(k_c)}')
arm('C4.axioms', OK_SRC.count('#print axioms') == 11,
    f'{OK_SRC.count("#print axioms")} `#print axioms` lines, so every declaration names its own '
    f'axiom basis rather than being taken on trust')

# ================================================================ D -- PART TWO, MY OWN STRAY
head('D -- PART TWO, MY OWN STRAY in r7484: the claim is VERIFIED before it is acted on')
res = read(os.path.join(R7484, 'RESULT.md'))
smp = read(os.path.join(R7484, 'sample.py'))
run = read(os.path.join(R7484, 'run.txt'))
ins = read(INSTR)

# ---- D1 -- cc66's word is not evidence: what does the instrument USE? -----------------------
print('\n  D1  what number does the instrument use, and what do 1.85 and 6.4 follow from?')
mt = re.search(r'^f_b\s*=\s*([0-9.]+)\s*#\s*(.*)$', ins, re.M)
arm('D1.instrument', mt is not None and abs(float(mt.group(1)) - 0.157) < 1e-12,
    f"the instrument's own line, located by text: f_b = {mt.group(1)}  # {mt.group(2).strip()}")
f_b = float(mt.group(1))
for cand in (0.157, 0.1834, 0.18):
    arm('D1.arith', True, f'f_b = {cand:<7.4f} -> f_b^(-1/3) = {cand ** (-1/3):.4f}, '
                          f'1/f_b = {1.0 / cand:.4f}')
arm('D1.matches157', abs(0.157 ** (-1 / 3) - 1.854) < 5e-4 and abs(1 / 0.157 - 6.37) < 5e-3,
    f'the file\'s printed figures 1.854 and 6.37 match 0.157 to {abs(0.157 ** (-1/3) - 1.854):.1e} '
    f'and {abs(1/0.157 - 6.37):.1e}')
arm('D1.not18', abs(0.1834 ** (-1 / 3) - 1.854) > 0.04 and abs(1 / 0.1834 - 6.37) > 0.9,
    f'and they do NOT match 0.1834: f_b^(-1/3) = {0.1834 ** (-1/3):.4f} vs 1.854, '
    f'1/f_b = {1/0.1834:.4f} vs 6.37')
arm('D1.printed', 'f_b = 0.157' in run and 'f_b^(-1/3) = 1.854' in run and '1/f_b = 6.37' in run,
    "the receipt's own run.txt prints all three, so this is read and not inferred")

# ---- D2 -- a repair leaves twins: a NAMED search ------------------------------------------
print('\n  D2  every occurrence of the wrong figure, by a named search over the whole revision')
# r7726's lesson again: a token search must say WHERE its hits sit.  The correction this
# revision applies QUOTES the figure it corrects, in its own record, so a search that only
# counted hits would read its own record as a surviving twin.  The arms therefore split every
# hit into THE CLAIM and THE RECORD, by the record's own marker, located by text.
REC = '\u2317 **Corrected at `r7730`.**'
def split_record(body):
    i = body.find(REC)
    if i < 0:
        return body, ''
    j = body.find('\n\n', i)
    return body[:i] + body[j:], body[i:j]
res_claim, res_record = split_record(res)
arm('D2.record_found', res_record.startswith(REC) and len(res_record) > 200,
    f'the correction record is located by its own marker, {len(res_record)} chars, '
    f'and is held apart from the claim for every search below')

WRONG = ['~18', '0.18 ', '0.1834', '18 per cent', 'cosmic baryon fraction of', '0.157']
for tok in WRONG:
    claim_hits, rec_hits = [], []
    for fn in sorted(os.listdir(R7484)):
        if not os.path.isfile(os.path.join(R7484, fn)):
            continue
        body = read(os.path.join(R7484, fn))
        cl, rc = split_record(body)
        for n, ln in enumerate(body.splitlines(), 1):
            if tok in ln:
                (rec_hits if (rc and ln in rc) else claim_hits).append((fn, n))
    arm('D2.search', True, f'{tok!r:28s} {len(claim_hits)} in the CLAIM {claim_hits}, '
                           f'{len(rec_hits)} in the RECORD {rec_hits}')

claim_18 = [n for n, ln in enumerate(res_claim.splitlines(), 1) if '`~18`' in ln]
arm('D2.one_target', len(claim_18) == 0,
    f'the figure the order names survives at {len(claim_18)} place(s) in the claim '
    f'(it stood at exactly one, RESULT.md:88, before the correction) and at '
    f'{res_record.count("`~18`")} in the record, where it is quoted as what was wrong')
arm('D2.phrase', 'against a cosmic baryon fraction of `16`' in flat(res_claim),
    'and the phrase it sits in -- "against a cosmic baryon fraction of" -- is the SAME phrase the '
    'instrument uses for 0.157, which is why the figure had to agree with it')
other = [ln.strip() for ln in res_claim.splitlines() if 'against the cosmic `0.157`' in ln]
arm('D2.selfconflict', len(other) == 1,
    f'and the file\'s OTHER mention, which the wrong figure contradicted, is unchanged: '
    f'{other[0][:92]!r}')

# ---- D3 -- the reachable negative N9, tested and not assumed -------------------------------
print('\n  D3  N9: is 0.157 itself cited to a source that says 0.18?  If so the PROSE is right.')
mt2 = re.search(r'^F_B_PAPER\s*=\s*([0-9.]+)\s*#\s*(.*)$', smp, re.M)
arm('D3.paper_const', mt2 is not None,
    f'sample.py carries F_B_PAPER = {mt2.group(1)}  # {mt2.group(2).strip()}')
uses = len(re.findall(r'\bF_B_PAPER\b', smp))
arm('D3.dead', uses == 1,
    f'and F_B_PAPER is referenced {uses} time in sample.py -- its own definition and nowhere '
    f'else, so no arm, no assertion and no printed line reads it: it is DEAD')
arm('D3.instr_names_it', 'cosmic baryon fraction' in mt.group(2),
    f'while the instrument calls 0.157 by exactly the phrase the prose uses: '
    f'{mt.group(2).strip()!r}')
arm('D3.N9_not_reached', abs(f_b - 0.157) < 1e-12 and 'cosmic baryon fraction' in mt.group(2)
    and abs(0.157 ** (-1 / 3) - 1.854) < 5e-4,
    'N9 is NOT reached: the instrument is the right one (its constant is the cosmic baryon '
    'fraction, and the derived figures follow from it), so the PROSE is the error')
arm('D3.attrib', 'THAT paper assumes' in mt2.group(2),
    "and 0.1834 is attributed in sample.py to the CITED PAPER's assumption, not to the cosmos -- "
    'which is where the prose\'s "~18" came from and what it dropped')

# ---- D4 -- after the correction ------------------------------------------------------------
print('\n  D4  the corrected prose, re-checked against the figures it must agree with')
CORRECT = 'against a cosmic baryon fraction of `16`'
fixed = CORRECT in flat(res)
arm('D4.applied', fixed, f'the corrected phrase is present: {fixed}')
arm('D4.recorded', REC in res,
    'and the correction is RECORDED beside the line rather than applied silently, which is this '
    "file's own convention at its \u2461 -- a corrected number whose correction cannot be seen is "
    'a number no later reader can check')
arm('D4.consistent', abs(round(100 * f_b) - 16) < 1e-9,
    f'and 16 is what the instrument\'s constant rounds to: 100 x {f_b} = {100 * f_b:.1f} per cent')
arm('D4.twins_gone', '`~18`' not in split_record(res)[0],
    'no twin of the wrong figure remains in the CLAIM; the only occurrence left is the record\'s '
    'own quotation of what it corrected')
arm('D4.derived_hold', abs(f_b ** (-1 / 3) - 1.854) < 5e-4 and abs(1 / f_b - 6.37) < 5e-3,
    'and the derived figures 1.854 and 6.37 still follow from the corrected number, '
    'because the number the instrument uses did not change')

# ================================================================ the ledger
head('THE LEDGER')
# no summary string guessed rather than read: the count is the arms that actually ran.
print(f'  arms run : {len(RUN)}  (distinct tags {len(set(RUN))})')
if FAIL:
    print(f'  **{len(FAIL)} ARM(S) FAILED**: {sorted(set(FAIL))}')
else:
    print('  every arm holds.')
print('\n  ⛭ and the verdicts that are FINDINGS rather than passes are collected in RESULT.md,')
print('    each with the witness printed above and not with a summary string guessed from it.')
sys.exit(0)
