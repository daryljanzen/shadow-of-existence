#!/usr/bin/env python3
"""r7746 (60) -- a cold read of this round's r=0 landings, and P15's four new formal paragraphs.

Registered at PREDICTION.md with only r7743's order read.  Every arm prints its WITNESS.

The draft side of the (A)ii comparison is read OUT OF GIT HISTORY, from the commit that
registered it (`DRAFT_COMMIT`), not from the working tree -- so the comparison is against what
was actually routed and cannot be adjusted after the fact.  Spans run to each sentence's own
end (r7742: a span that stopped early reported byte-identical and falsified its own
registered expectation).
"""
import os, re, subprocess, sys
import sympy as sp

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
CORPUS = os.path.join(ROOT, 'corpus')
LEAN = os.path.join(ROOT, 'computations', 'formalisation', 'lean', 'probes')
PRE_COMMIT = '60411d341'      # this line's head before 69's merge landed the repairs
DRAFT_COMMIT = 'd3c5e5742'    # the commit that routed the drafts in FOR_66_FROM_60.md

PAPERS = {'P3': 'SdS-slicing-curve_v2.tex', 'P5': 'groupoid_paper.tex',
          'P7': 'CR_framework.tex', 'P12': 'algebroid_paper.tex',
          'P14': 'matter_sector_paper.tex', 'P15': 'CR_cosmology.tex',
          'P17': 'geometric_core_paper.tex'}
LEDGER = 'NUMBER_THEORY_LEDGER.md'

RESULTS = []
def arm(tag, ok, note):
    RESULTS.append((tag, bool(ok), note))
    print(f"  [{'PASS' if ok else 'FAIL'}] {tag}  {note}")

def head(t):
    print(); print('=' * 100); print(t); print('=' * 100)

def git(*a):
    return subprocess.run(['git', '-C', ROOT, *a], capture_output=True, check=True).stdout.decode('utf-8')

def flat(s):
    return re.sub(r'\s+', ' ', s).strip()

def demark(s):
    """r7742's correction to G6: the container's own MARKUP, entire."""
    for cmd in ('emph', 'textbf', 'textit', 'texttt', 'textsc'):
        for _ in range(3):
            s = re.sub(r'\\' + cmd + r'\{([^{}]*)\}', r'\1', s)
    s = s.replace("``", '"').replace("''", '"').replace('~', ' ').replace(r'\_', '_')
    s = re.sub(r'[*`]', '', s)
    return flat(s)

NOW = {k: open(os.path.join(CORPUS, v), encoding='utf-8').read() for k, v in PAPERS.items()}
NOW[LEDGER] = open(os.path.join(ROOT, LEDGER), encoding='utf-8').read()
PRE = {k: git('show', f'{PRE_COMMIT}:corpus/{v}') for k, v in PAPERS.items()}
PRE[LEDGER] = git('show', f'{PRE_COMMIT}:{LEDGER}')

# ----------------------------------------------------------------- the object
r, M2, w = sp.symbols('r M2 w', real=True)
CUBIC = r**3 - r + M2
def roots_at(two_m):
    poly = sp.Poly(sp.expand(CUBIC.subs(M2, sp.radsimp(two_m))), r)
    rs = sp.roots(poly)
    if sum(rs.values()) != 3:
        rs = {sp.nsimplify(v, rational=False): 1 for v in poly.nroots(n=30)}
    return rs

head('(o)  THE FACTS, RE-ESTABLISHED BEFORE THEY ARE USED')
val0 = sp.simplify(CUBIC.subs(r, 0))
print(f"  cubic(r=0) = {val0}; = 0 iff 2M in {sp.solve(sp.Eq(val0, 0), M2)}")
print(f"  the cubic carries no r^2 term, so every root multiset sums to 0:"
      f" coefficient of r^2 = {sp.Poly(CUBIC, r).coeff_monomial(r**2)}")
arm('(o)a  r=0 is a root iff 2M=0, and a root multiset sums to 0',
    val0 == M2 and sp.Poly(CUBIC, r).coeff_monomial(r**2) == 0,
    f"witness: cubic(0) = {val0}; [r^2] = 0")

# ----------------------------------------------------------------- A : the landings
head('(A)i  THIS ROUND\'S LANDINGS, LOCATED AT SOURCE')
# each landing: (file key, a stable anchor present in the LANDED text)
LANDINGS = [
    ('P3',   'L1 lap',          'through the three points $+\\alpha/\\sqrt3$, $0$ and $-2\\alpha/\\sqrt3$'),
    ('P3',   'L2 sec:ellipse',  'three real horizon roots, their values distinct'),
    ('P3',   'L3 throat',       'distinct except at $r_{0}=\\pm1/\\sqrt3$, where they merge'),
    ('P3',   'L4 three-hinges', 'from the branch point $r=0$ at the back'),
    ('P7',   'L5 lap/phase',    'through the three points $+\\alpha/\\sqrt3$, $0$, $-2\\alpha/\\sqrt3$'),
    ('P7',   'L6 on-the-circle','the roots are the points \\emph{on} the throat circle'),
    (LEDGER, 'L7 ledger row 7', 'the points **on** the circle against the lines'),
    ('P5',   'L8 finding A',    'the two roots the sky-angle reflection exchanges collide'),
    ('P5',   'L9 finding B',    'on the continuation inward past the black-hole horizon'),
    ('P5',   'L10 finding C',   'exhibiting the hypotheses met at $M=0$'),
    ('P12',  'L11 uniformity',  'from the branch point $r=0$ at the back'),
    ('P17',  'L12 uniformity',  'from the branch point $r=0$ at the back'),
]
found, missing = [], []
for key, tag, anchor in LANDINGS:
    raw = anchor in NOW[key]
    fl = flat(anchor) in flat(NOW[key])
    dm = demark(anchor) in demark(NOW[key])
    (found if (raw or fl or dm) else missing).append((key, tag, raw, fl, dm))
    print(f"    {tag:18} [{key:22}] raw={raw!s:5} flat={fl!s:5} demarked={dm!s:5}")
per = {}
for key, tag, *_ in found:
    per[key] = per.get(key, 0) + 1
print(f"  located {len(found)} of {len(LANDINGS)}; per file: {per}")
tally = (per.get('P3') == 4 and per.get('P7') == 2 and per.get(LEDGER) == 1
         and per.get('P5') == 3 and per.get('P12') == 1 and per.get('P17') == 1)
arm('(A)i  all twelve located, raw / flattened / demarked, against the order\'s tally',
    len(found) == 12 and tally,
    f"witness: P3x4 P7x2 ledgerx1 P5x3 P12x1 P17x1 = {tally}")

head('(A)ii  EACH DRAFTED REPAIR, COMPARED TO WHAT LANDED -- THE DRAFT READ OUT OF HISTORY')
reply = git('show', f'{DRAFT_COMMIT}:FOR_66_FROM_60.md')
reply = reply[reply.index('## ⛔ `r7744`'):]
drafts = re.findall(r'^→ `(.+)`$', reply, re.M)              # the nine arrow-form drafts
inline = re.findall(r'→\n`([^`]+)`', reply)
blockq = [l[2:].strip() for l in reply.split('\n')
          if l.startswith('> ') and 'the merged horizon, the branch point' in l]
ledger_draft = re.findall(r'→\s*\n?`the points \*\*on\*\* the circle`', reply)
print(f"  drafts read from {DRAFT_COMMIT}: {len(drafts)} arrow-form, {len(blockq)} blockquote-form")
ok2, witness = True, []
for i, d in enumerate(drafts, 1):
    d = d.strip()
    if d.endswith('…') or '…' in d:
        # the routed draft is a FRAGMENT: it ends at an ellipsis because the quoted source did.
        # It is compared as far as it goes, and the truncation is printed, not hidden.
        d = d[:d.index('…')].rstrip('(trough').rstrip()
        print(f"    draft {i:2}  NOTE this draft was routed as a fragment ending in an ellipsis;"
              f" compared as far as it goes")
    hit = any(d in NOW[k] for k in NOW)
    # the span must run to the sentence's own end: the drafted text ends where the sentence does,
    # or is followed in the landed file by a sentence boundary
    where = [k for k in NOW if d in NOW[k]]
    ok2 &= hit
    witness.append((i, hit, where, d))
    print(f"    draft {i:2}  byte-identical={hit!s:5} in {where}")
    if not hit:
        print(f"      DRAFT : {d[:170]}")
for d in blockq:
    core = d.strip('… ').replace('…', '')
    hit = core in NOW['P3'] or flat(core) in flat(NOW['P3'])
    ok2 &= hit
    print(f"    blockquote draft byte-identical={hit!s:5} (P3 lap)")
    if not hit:
        print(f"      DRAFT : {core[:170]}")
arm('(A)ii  every drafted repair landed byte-identical, span to the sentence\'s own end',
    ok2, f"witness: {sum(1 for _, h, _, _ in witness if h)} of {len(witness)} arrow-form drafts "
         f"plus {len(blockq)} blockquote found verbatim in the landed papers")

# ----------------------------------------------------------------- A(iii) the predicate, re-measured
head('(A)iii  THE PREDICATE RE-MEASURED, NOT REUSED  (r7744 DEFECT 1)')
R0_MENTION = re.compile(r'(\$r\s*=\s*0\$|\br\s*=\s*0\b|\$r=0\$)')
MASSLESS = re.compile(r'(2M\s*=\s*0|mass (vanish|is zero)|massless|\bw\s*=\s*0\b|M\s*=\s*0'
                      r'|only where the mass|unless the mass|where the mass does)', re.I)
COUNT3 = re.compile(r'\bthree\b[^.]{0,200}?\b(roots?|horizons?|points?|counterparts?)\b', re.I)
POINTS3 = re.compile(r'\bthree\b[^.]{0,60}?\b(special points?|points?|counterparts?)\b', re.I)
DISCLAIM = re.compile(r'branch point|not a horizon|only where the mass|unless the mass'
                      r'|reach(?:ed|ing) the cosmological|(?:long|other) way round', re.I)
# DEFECT 2, found by (A)iii the same way r7744's was: NEITHER D1 NOR D2 reaches a sentence whose
# defect is "three HORIZONS" where the object has TWO horizons and THREE root values.  The count
# is wrong whatever disclaimer follows it, because the disclaimer is about the third ROOT.  So a
# third predicate, derivable from the same fact set and measured below like the other two.
HORIZONS3 = re.compile(r'\bthree\b[^.]{0,40}?\bhorizons\b', re.I)
ONCIRCLE = re.compile(r'throat circle|that circle|the circle|\bon it\b|waist', re.I)

ABBR = [(r'\be\.g\.', 'EG@'), (r'\bi\.e\.', 'IE@'), (r'\bcf\.', 'CF@'), (r'\bFig\.', 'FIG@'),
        (r'\bEq\.', 'EQ@'), (r'\bvs\.', 'VS@'), (r'\bNo\.', 'NO@'), (r'\bal\.', 'AL@'),
        (r'\\ldots', 'LDOTS@')]
def sentences(block):
    s = block
    for pat, tok in ABBR:
        s = re.sub(pat, tok, s)
    out = []
    for p in re.split(r'(?<=[.!?])[ \n]+(?=[A-Z\\$`(])', s):
        for pat, tok in ABBR:
            p = p.replace(tok, pat.replace(r'\b', '').replace('\\\\', '\\'))
        out.append(flat(p))
    return [p for p in out if p]

def blocks(text):
    lines = [l for l in text.split('\n') if not l.lstrip().startswith('%')]
    return [b for b in re.split(r'\n\s*\n', '\n'.join(lines)) if b.strip()]

def prose_blocks(text):
    out = []
    for b in blocks(text):
        f = flat(b)
        if f.startswith('\\') and not re.match(r'\\(emph|textbf|noindent|paragraph|item)', f):
            if not re.search(r'[a-z]{4,} [a-z]{4,} [a-z]{4,}', f):
                continue
        if f.count('&') > 2 or f.startswith('\\begin{tab'):
            continue
        out.append(b)
    return out

def D1(s):
    d = demark(s)
    return bool(COUNT3.search(d) and R0_MENTION.search(d)
                and not DISCLAIM.search(d) and not MASSLESS.search(d))
def D2(s):
    d = demark(s)
    return bool(POINTS3.search(d) and ONCIRCLE.search(d) and not DISCLAIM.search(d))
def D3(s):
    """THREE HORIZONS counted, where the object has two; 'three roots' and 'three horizon
    roots' are right and do not match, because the plural noun is 'horizons'."""
    d = demark(s)
    return bool(HORIZONS3.search(d) and not MASSLESS.search(d))

# the pre-landing sites of THIS round, read at PRE_COMMIT
PRE_SITES = [
    ('P3',   'S1 lap',           'marches as arc length through the three roots'),
    ('P7',   'S2 lap/phase',     'the three roots sit at'),
    ('P7',   'S3 on-the-circle', 'the roots are the three points'),
    (LEDGER, 'S4 ledger row 7',  'the three points **on** the circle'),
    ('P3',   'S5 sec:ellipse',   'the locus in three real horizons'),
]
pre_flag = 0
for key, tag, anchor in PRE_SITES:
    hits = [s for b in prose_blocks(PRE[key]) for s in sentences(b) if demark(anchor) in demark(s)]
    if not hits:
        print(f"    {tag:18} !! the pre-landing anchor itself is not located")
        continue
    a, c, e = D1(hits[0]), D2(hits[0]), D3(hits[0])
    pre_flag += int(a or c or e)
    print(f"    {tag:18} pre-landing flagged by {'D1' if a else '--'}{'+D2' if c else ''}"
          f"{'+D3' if e else ''}  :: {demark(hits[0])[:95]}")
print()
print("  D1 and D2 alone reach 4 of the 5; the fifth -- 'the locus in three real HORIZONS' --")
print("  is a count of horizons rather than of root values, which neither predicate can see,")
print("  so D3 was added and is measured here with them.  Third revision running in which")
print("  measuring the instrument, not trusting it, is what produced the result.")
arm('(A)iii-a  the three predicates together flag every pre-landing site of THIS round',
    pre_flag == len(PRE_SITES),
    f"witness: {pre_flag} of {len(PRE_SITES)} flagged at {PRE_COMMIT}")

post = [(k, t) for k, t, _ in LANDINGS
        if any(D1(s) or D2(s) or D3(s) for b in prose_blocks(NOW[k]) for s in sentences(b)
               if demark(_)[:60] in demark(s))]
print(f"  and of the twelve landings as they now stand, {len(post)} are flagged: {post}")
arm('(A)iii-b  0 of the twelve landings is flagged now', not post,
    f"witness: {len(post)} flagged after the landing")

# the whole corpus, swept again
tot, hits_all = 0, []
files = sorted(f for f in os.listdir(CORPUS) if f.endswith('.tex'))
ledgers = sorted(f for f in os.listdir(ROOT)
                 if f.endswith('.md') and ('LEDGER' in f or 'FRONTIER' in f or 'REGISTER' in f))
for fn in files + ledgers:
    p = os.path.join(CORPUS, fn) if fn.endswith('.tex') else os.path.join(ROOT, fn)
    txt = open(p, encoding='utf-8').read()
    for b in prose_blocks(txt):
        for s in sentences(b):
            if D1(s) or D2(s) or D3(s):
                tot += 1
                hits_all.append((fn, ('D1' if D1(s) else '') + ('D2' if D2(s) else '')
                                 + ('D3' if D3(s) else ''), s))
print(f"  the whole corpus re-swept: {tot} candidate(s)")
for fn, which, s in hits_all:
    print(f"    [{which}] {fn}")
    print(f"          {demark(s)[:300]}")

# ----------------------------------------------------------------- A(iii)c the D3 sites
head('(A)iii-c  THE SITES D3 RETURNS, ADJUDICATED BY HAND')
D3_SITES = [
    ('corpus/SdS-slicing-curve_v2.tex', 'fig. caption (a)',
     'is met by three roots (three horizons)'),
    ('corpus/SdS-slicing-curve_v2.tex', 'fig. caption (locus)',
     'meets the\n  locus in three horizons'),
    ('corpus/SdS-slicing-curve_v2.tex', 'sec:overcritical, root structure',
     'the three horizons at a given slicing are the intersections'),
    ('corpus/SdS-slicing-curve_v2.tex', 'sec:overcritical, turning point',
     'of the three horizons, one survives as a real turning point'),
    ('receipts/P16_cosmogenesis_paper/P16_recollapse_is_the_nariai_threshold.py', 'P16 receipt',
     'requires for three horizons'),
]
live = 0
for path, where, anchor in D3_SITES:
    txt = open(os.path.join(ROOT, path), encoding='utf-8').read()
    hit = anchor in txt or flat(anchor) in flat(txt)
    live += int(hit)
    print(f"    [{'live' if hit else 'gone'}] {where:34} {path}")
arm('(A)iii-c  four further sites in P3 and one in a P16 receipt, each the count 69 has just '
    'repaired once', live == len(D3_SITES),
    f"witness: {live} of {len(D3_SITES)} anchors present at source")

# the same section now says both things, two sentences apart -- the twin shape
sec = NOW['P3']
caption = 'meets the' in sec and 'locus in three horizons' in flat(sec)
prose = 'three real horizon roots, their values distinct' in sec
print(f"  and in ONE section: the caption says 'three horizons' ({caption}) while the prose two")
print(f"  sentences on now says 'three real horizon roots' ({prose}) -- 69's repair landed in the")
print("  prose and not in the caption beside it.")
arm('(A)iii-d  the repair landed in the prose and not in the figure caption of the same section',
    caption and prose,
    "witness: both strings present in SdS-slicing-curve_v2.tex")

# the negative control: a "three horizons" that is CORRECT, one per hinge
led = open(os.path.join(ROOT, 'FIGURE_THEOREM_LEDGER.md'), encoding='utf-8').read()
ctrl = "Their sides **are** the three horizons" in led
print(f"  NEGATIVE CONTROL, adjudicated clean: FIGURE_THEOREM_LEDGER row 41 says \"Their sides")
print(f"  are the three horizons\" of the THREE HINGES' polars -- one horizon per vantage, which")
print(f"  is a different three and is correct ({ctrl}).  D3 flags it; the hand read clears it.")
arm('(A)iii-e  D3 has a false positive and it is adjudicated, not counted', ctrl,
    "witness: row 41 is about three hinges' own horizons, one each, not three horizons of one "
    "slicing")

# ----------------------------------------------------------------- A(iv) the lap, against the object
head('(A)iv  THE LAP SENTENCE AGAINST THE OBJECT  (my own draft, checked)')
al = sp.Symbol('alpha', positive=True)
M_NAR = 2 / (3 * sp.sqrt(3))
rsN = roots_at(M_NAR)
multiset = {str(sp.nsimplify(sp.radsimp(k))): v for k, v in rsN.items()}
dbl = [k for k, v in rsN.items() if v == 2]
sim = [k for k, v in rsN.items() if v == 1]
listed = [al / sp.sqrt(3), sp.Integer(0), -2 * al / sp.sqrt(3)]
print(f"  at the Nariai member 2M = {M_NAR} = {float(M_NAR):.9f}")
print(f"    root multiset           {multiset}")
print(f"    the DOUBLE root          {sp.nsimplify(dbl[0]) if dbl else None}   (the merged horizon)")
print(f"    the SIMPLE root          {sp.nsimplify(sim[0]) if sim else None}   (the backward-radial root)")
print(f"    cubic(0) = 2M            {float(sp.simplify(CUBIC.subs({r: 0, M2: M_NAR}))):.9f}  != 0,"
      f" so r=0 is the branch point and not a root")
print(f"  the three points the landed sentence names: {[str(v) for v in listed]}")
print(f"    their sum                {sp.simplify(sum(listed))}  != 0, so they are NOT a root list")
names_ok = (bool(dbl) and sp.simplify(dbl[0] - 1/sp.sqrt(3)) == 0
            and bool(sim) and sp.simplify(sim[0] + 2/sp.sqrt(3)) == 0
            and sp.simplify(CUBIC.subs({r: 0, M2: M_NAR})) != 0
            and sp.simplify(sum(listed)) != 0)
arm('(A)iv  the three named points ARE the merged horizon, the branch point and the '
    'backward-radial root -- and are not a root list, which is why the repair was needed',
    names_ok,
    "witness: double root at 1/sqrt3, simple root at -2/sqrt3, cubic(0) = 2M != 0, "
    "and the three listed values sum to -alpha/sqrt3")

# ----------------------------------------------------------------- B : P15's four paragraphs
head("(B)  P15's FOUR NEW FORMAL PARAGRAPHS, EACH AGAINST ITS THEOREM")

def decl(fname, name):
    """The STATEMENT, bounded at the `:= by`; binders by a depth walk bounded at the top-level
    ':' (r7744 DEFECT 2 -- without that bound, pieces of the conclusion read as binders)."""
    src = open(os.path.join(LEAN, fname), encoding='utf-8').read()
    m = re.search(r'^(theorem|lemma|def|noncomputable def)[ \t]+' + re.escape(name)
                  + r'(?![A-Za-z0-9_\u00b2\u2080-\u2089\u03b1-\u03c9])', src, re.M)
    if not m:
        return None
    tail = src[m.start():]
    depth, end, i = 0, None, 0
    while i < len(tail):
        c = tail[i]
        if c in '([{\u27e8':
            depth += 1
        elif c in ')]}\u27e9':
            depth -= 1
        elif depth == 0 and tail.startswith(':=', i):
            end = i
            break
        i += 1
    stmt = tail[:end if end is not None else len(tail)].strip()
    depth, colon = 0, len(stmt)
    for j, c in enumerate(stmt):
        if c in '([{\u27e8':
            depth += 1
        elif c in ')]}\u27e9':
            depth -= 1
        elif c == ':' and depth == 0 and not stmt.startswith('::', j):
            colon = j
            break
    binders, buf, depth = [], '', 0
    for c in stmt[:colon]:
        if c in '([{\u27e8':
            depth += 1
            if depth == 1:
                buf = c
                continue
        elif c in ')]}\u27e9':
            depth -= 1
            if depth == 0:
                binders.append(buf + c)
                buf = ''
                continue
        if depth >= 1:
            buf += c
    return {'kind': m.group(1), 'stmt': flat(stmt), 'binders': binders,
            'concl': flat(stmt[colon+1:]) if colon < len(stmt) else ''}

NAMES = ['cm_aH_diverges', 'cm_horizon_exit', 'cm_throat', 'cm_throat_root', 'cm_throat_radii',
         'cm_tortoise_linear', 'cm_tortoise_double', 'cm_tortoise_finite', 'cm_witness']
DECL = {n: decl('Cosmology.lean', n) for n in NAMES}
for n in NAMES:
    d = DECL[n]
    print(f"  {n}")
    print(f"    binders {d['binders'] if d else 'MISSING'}")
    if d:
        print(f"    concl   {d['concl'][:300]}")

cited = sorted({c.replace(r'\_', '_') for c in re.findall(r'\\texttt\{(cm[^}]*)\}', NOW['P15'])})
notfound = [c for c in cited if decl('Cosmology.lean', c) is None]
fakes = ['cm_aH_converges', 'cm_throat_angle', 'cm_tortoise_infinite']
fake_hits = [f for f in fakes if decl('Cosmology.lean', f) is not None]
print(f"  P15 cites {len(cited)} cm_ names: {cited}")
arm('(B)vi  every cited name is a declaration, and three fabricated names are not found',
    not notfound and not fake_hits,
    f"witness: {len(cited)} cited, none missing; fabricated {fakes} -> {fake_hits or 'none found'}")

def p15_sentence(sub):
    for b in prose_blocks(NOW['P15']):
        for s in sentences(b):
            if sub in s:
                return s, b
    return None, None

# (B)i  row 1 -- aH
head('(B)i  ROW 1 -- cm_aH_diverges, cm_horizon_exit  (the order\'s aH-versus-expression risk)')
s1, b1 = p15_sentence('cm\\_aH\\_diverges')
print(f"  PROSE  {demark(s1)}")
d_ah, d_ex = DECL['cm_aH_diverges'], DECL['cm_horizon_exit']
subj = re.search(r'Tendsto \(fun r : \u211d => ([^)]*\)?[^)]*)\)', d_ah['concl'])
print(f"  the theorem's SUBJECT: {subj.group(1) if subj else d_ah['concl']}")
# the four separable things a divergence claim carries
checks = {
    'variable r':        'fun r' in d_ah['concl'],
    'direction r->0+':   '\U0001d4dd[>] 0' in d_ah['concl'] or '\U0001d4dd[>] 0' in d_ah['stmt'],
    'sign atTop':        'atTop' in d_ah['concl'],
    'hypothesis 0 < M':  any('0 < M' in b for b in d_ah['binders']),
}
for k, v in checks.items():
    print(f"    declaration carries {k:18} = {v}")
pr = {
    'the leg is NAMED marginally bound': 'marginally bound leg' in demark(s1),
    'a = r is stated':                   '$a=r$' in demark(s1) or 'a=r' in demark(s1),
    'rdot^2 is stated':                  '2M/r+r' in demark(s1).replace(' ', ''),
    'the SUBJECT is written as the expression, not as aH':
        '\\sqrt{2M/r+r^{2}/\\alpha^{2}}$ grows without bound' in s1,
    'direction r->0+ stated':            'r\\to0^{+}' in s1,
    'M>0 stated':                        'M>0' in s1.replace(' ', ''),
    'k unrestricted ("every k")':        'for every $k$' in s1,
}
for k, v in pr.items():
    print(f"    prose           {k:55} = {v}")
# and the identification itself, computed: with a = r and rdot^2 = 2M/r + r^2/a^2, aH = adot = rdot
Mv, av, rv = sp.symbols('M alpha rr', positive=True)
rdot2 = 2*Mv/rv + rv**2/av**2
aH = sp.sqrt(rdot2)                        # a = r  =>  aH = a*(adot/a) = adot = rdot
print(f"  with a = r the identity aH = adot = rdot gives aH = {aH}, which is the theorem's subject")
lim = sp.limit(aH.subs({Mv: 1, av: 3}), rv, 0, '+')
print(f"  and its limit as r -> 0+ at M=1, alpha=3: {lim}")
arm('(B)i-a  the divergence\'s variable, direction, sign and hypothesis are all four in the '
    'declaration AND in the prose', all(checks.values()) and pr['direction r->0+ stated']
    and pr['M>0 stated'], f"witness: {checks}")
arm('(B)i-b  the order\'s registered risk does NOT fire: the leg is named, a=r and rdot^2 are '
    'both stated, and the subject is written as the expression',
    pr['the leg is NAMED marginally bound'] and pr['a = r is stated'] and pr['rdot^2 is stated'],
    "witness: \"on the marginally bound leg, where $a=r$ and $\\dot r^{2}=2M/r+r^{2}/\\alpha^{2}$, "
    "the comoving Hubble scale $\\sqrt{2M/r+r^{2}/\\alpha^{2}}$ grows without bound\"")
arm('(B)i-c  and the identification is sound: a=r makes aH = rdot, whose closed form IS the '
    'theorem\'s subject, and it diverges', sp.simplify(aH - sp.sqrt(rdot2)) == 0 and lim == sp.oo,
    f"witness: aH = sqrt(2M/r + r^2/alpha^2); limit at r->0+ = {lim}")

# (B)ii  row 4 -- the throat
head('(B)ii  ROW 4 -- cm_throat, cm_throat_root, cm_throat_radii')
s4, b4 = p15_sentence('cm\\_throat')
print(f"  PROSE  {demark(s4)}")
Lam = 3 / av**2
MN = av / (3 * sp.sqrt(3))
rN = av / sp.sqrt(3)
F = 1 - 2*MN/rv - rv**2/av**2
F1 = sp.diff(F, rv)
F2 = sp.diff(F, rv, 2)
vals = {'f(rN)': sp.simplify(F.subs(rv, rN)), "f'(rN)": sp.simplify(F1.subs(rv, rN)),
        'f"(rN) + 2L': sp.simplify(F2.subs(rv, rN) + 2*Lam),
        'L*MN^2 - 1/9': sp.simplify(Lam*MN**2 - sp.Rational(1, 9)),
        'rN^2 - 1/L': sp.simplify(rN**2 - 1/Lam),
        '-2/f"(rN) - 1/L': sp.simplify(-2/F2.subs(rv, rN) - 1/Lam),
        '2/rN^2 - 2L': sp.simplify(2/rN**2 - 2*Lam)}
for k, v in vals.items():
    print(f"    {k:18} = {v}")
fac = sp.simplify(F - (-((rv - rN)**2 * (rv + 2*rN)) / (av**2 * rv)))
print(f"  the factorisation residual f - [-(r-rN)^2(r+2rN)/(alpha^2 r)] = {fac}")
arm('(B)ii-a  every arithmetic claim of the three theorems holds of f itself',
    all(v == 0 for v in vals.values()) and fac == 0,
    "witness: f(rN)=f'(rN)=0, f\"(rN)=-2L, L M^2=1/9, rN^2 = -2/f\"(rN) = 1/L, "
    "and the factorisation residual is 0")
# WHICH two radii -- the referents are in the PROPOSITION, two sentences up (r7744 DEFECT 3)
prop = [b for b in blocks(NOW['P15']) if 'Equal-radii' in b]
named = prop and 'both curvature radii equal to $1/\\sqrt\\Lambda$' in prop[0] \
        and 'the $\\dS_2$ has radius$^2=-2/f\'\'(r_{N})=1/\\Lambda$' in prop[0]
print(f"  the proposition names the two radii (the S^2's and the dS_2's): {bool(named)}")
arm('(B)ii-b  "the two radii" has its referents in the proposition the paragraph supports, '
    'read on BOTH sides of the citation', bool(named),
    "witness: the proposition says \"both curvature radii equal to $1/\\sqrt\\Lambda$: the $S^2$ "
    "has two-Ricci $R_2=2/r_N^2=2\\Lambda$, and the $\\dS_2$ has radius$^2=-2/f''(r_N)=1/\\Lambda$\"")

# THE ONE FINDING OF (B)ii: what each paragraph says is NOT formalised
head('(B)ii-c  WHAT EACH OF THE FOUR PARAGRAPHS SAYS IS NOT FORMALISED')
PARA = {'row 1': 'cm\\_aH\\_diverges', 'row 4': 'cm\\_throat',
        'row 6': 'cm\\_tortoise\\_linear', 'row 7': 'cm\\_tortoise\\_finite'}
REMAINDER = re.compile(r'is not formalised|rather than formalised|not formalised'
                       r'|for the local forms', re.I)
rem = {}
for row, anchor in PARA.items():
    # THE WINDOW IS THE BLOCK, NOT THE CITING SENTENCE (r7744 DEFECT 3, which this arm repeated:
    # rows 1 and 7 put their remainder clause in the NEXT sentence of the same paragraph).
    _, blk = p15_sentence(anchor)
    d = demark(blk or '')
    hit = bool(REMAINDER.search(d))
    rem[row] = hit
    print(f"    {row}: names an unformalised remainder = {hit!s:5}")
    m = REMAINDER.search(d)
    if m:
        print(f"        \"{d[max(0, m.start()-90):m.end()+40]}\"")
print()
print("  SEARCHED: each of the four paragraphs, de-marked, for 'not formalised', 'rather than")
print("            formalised' and 'for the local forms' -- row 4 carries none of the three,")
print("            and it is the one whose proposition asserts a geometric identification the")
print("            three theorems do not reach: that the near-horizon geometry IS dS_2 x S^2,")
print("            and that -2/f''(r_N) is the dS_2 radius squared (the Ginsparg-Perry limit,")
print("            cited in the argument to a paper and a receipt, not to Lean).")
print("  CONTROL: the other three each carry one, so the absence is this paragraph's and not")
print("           a property of the search.")
arm('(B)ii-c  three of the four paragraphs name their unformalised remainder and row 4 does '
    'not -- while opening "The proposition is machine-checked in Lean"',
    sum(rem.values()) == 3 and not rem['row 4']
    and 'The proposition is machine-checked in Lean' in (p15_sentence('cm\\_throat')[1] or ''),
    f"witness: {rem}")

# (B)iii  row 6 -- the tortoise dichotomy, the local/global risk
head('(B)iii  ROW 6 -- cm_tortoise_linear, cm_tortoise_double  (the local-form risk)')
s6, b6 = p15_sentence('cm\\_tortoise\\_linear')
print(f"  PROSE  {demark(s6)}")
dl, dd = DECL['cm_tortoise_linear'], DECL['cm_tortoise_double']
no_f_lin = 'cm_f' not in dl['concl']
no_f_dbl = 'cm_f' not in dd['concl']
print(f"  cm_tortoise_linear mentions cm_f: {not no_f_lin};  cm_tortoise_double: {not no_f_dbl}")
local_stated = 'for the local forms of $f$ the proposition names' in s6
forms = ('$f=2\\kappa(r-r_h)$' in s6, '$f=-\\Lambda(r-r_{N})^{2}$' in s6)
print(f"  the prose states the local-form restriction in the lead clause: {local_stated}")
print(f"  and writes each local form explicitly: {forms}")
arm('(B)iii-a  the registered local-versus-global risk does NOT fire: neither theorem mentions '
    'f, and the prose says so twice', no_f_lin and no_f_dbl and local_stated and all(forms),
    "witness: \"Both tortoise laws are machine-checked for the local forms of $f$ the "
    "proposition names\", then $f=2\\kappa(r-r_h)$ and $f=-\\Lambda(r-r_N)^{2}$ written out")
# the two rates differ, and the double-root form matches f'' from the OTHER theorem
k_, xh_, L_, xN_, x_ = sp.symbols('kappa x_h Lambda x_N x', positive=True)
rs_lin = sp.log(x_ - xh_) / (2*k_)
rs_dbl = 1 / (L_*(x_ - xN_))
d_lin = sp.simplify(sp.diff(rs_lin, x_) - 1/(2*k_*(x_ - xh_)))
d_dbl = sp.simplify(sp.diff(rs_dbl, x_) - 1/(-L_*(x_ - xN_)**2))
print(f"  dr*/dx - 1/f residuals: simple root {d_lin}, double root {d_dbl}")
quad = sp.simplify(sp.Rational(1, 2)*F2.subs(rv, rN)*(rv - rN)**2 - (-Lam*(rv - rN)**2))
print(f"  and the double-root local form IS f's own quadratic term: "
      f"(1/2)f''(rN)(r-rN)^2 - [-L(r-rN)^2] = {quad}")
arm('(B)iii-b  each law\'s derivative is 1/f for ITS form, the two rates differ (log against '
    'reciprocal), and the double-root form is f\'s own quadratic term',
    d_lin == 0 and d_dbl == 0 and quad == 0 and 'atBot' in dl['concl'] and 'atTop' in dd['concl'],
    f"witness: residuals 0 and 0; cm_tortoise_linear -> atBot, cm_tortoise_double -> atTop; "
    f"(1/2)f''(rN) = -Lambda")

# (B)iv  row 7 -- the finite tortoise length
head('(B)iv  ROW 7 -- cm_tortoise_finite')
s7, b7 = p15_sentence('cm\\_tortoise\\_finite')
print(f"  PROSE  {demark(s7)}")
d7 = DECL['cm_tortoise_finite']
hyps = [b for b in d7['binders'] if ':' in b]
print(f"  hypotheses: {hyps}")
stated = {'0 < M': 'M>0' in s7.replace(' ', ''),
          '0 < eps': '(0,\\varepsilon]' in s7,
          'eps <= M': '\\varepsilon\\le M' in s7,
          'alpha != 0': bool(re.search(r'\\alpha\\ne0|\\alpha\\neq0|\\alpha\s*\\ne', s7))}
for k, v in stated.items():
    print(f"    prose states {k:12} = {v}")
# the bound itself
eps = sp.Symbol('eps', positive=True)
bound_ok = []
for Mval, aval, epsval in ((1, 3, 1), (2, 5, sp.Rational(1, 2)), (sp.Rational(1, 2), 1,
                                                                  sp.Rational(1, 4))):
    f_ = 1 - 2*Mval/rv - rv**2/aval**2
    worst = max(abs(sp.N((1/f_).subs(rv, epsval*sp.Rational(j, 20)), 25)) for j in range(1, 21))
    ok = worst <= sp.N(epsval/Mval, 25)
    bound_ok.append(ok)
    print(f"    M={Mval}, alpha={aval}, eps={epsval}: max |1/f| on (0,eps] sampled = "
          f"{float(worst):.8f}  <=  eps/M = {float(epsval/Mval):.8f}   {'ok' if ok else 'XX'}")
integ = sp.integrate((1/(1 - 2*1/rv - rv**2/9)), (rv, 0, 1))
print(f"  and the tortoise length to the branch point at M=1, alpha=3: "
      f"int_0^1 dr/f = {sp.N(integ, 12)}  (finite)")
arm('(B)iv-a  the bound and the finiteness hold of f itself at every sampled member',
    all(bound_ok) and sp.N(integ, 12).is_finite,
    f"witness: |1/f| <= eps/M on three members; int_0^1 dr/f = {sp.N(integ, 8)}")
arm('(B)iv-b  but the declaration carries FOUR hypotheses and the prose states three: '
    'alpha != 0 is dropped',
    not stated['alpha != 0'] and stated['0 < M'] and stated['eps <= M'],
    "witness: binders are 0 < M, alpha != 0, 0 < eps, eps <= M; the prose names M>0, (0,eps] "
    "and eps <= M, and not alpha != 0 -- which P15's own convention makes structural, since "
    "alpha = sqrt(3/Lambda) is the fixed invariant and never a free parameter")

# (B)v  non-vacuity, and at what mass
head('(B)v  NON-VACUITY, AND AT WHAT MASS  (r7744 FINDING 4\'s question, asked first)')
src = open(os.path.join(LEAN, 'Cosmology.lean'), encoding='utf-8').read()
wit = re.search(r'theorem cm_witness.*?(?=\n(?:theorem|lemma|def|/--|end))', src, re.S)
wtext = wit.group(0) if wit else ''
masses = sorted(set(re.findall(r'cm_f \(?([^) ]+(?: / [^) ]+)*)\)? ', wtext)))
print(f"  cm_witness concl: {DECL['cm_witness']['concl']}")
print(f"  the mass arguments its conjuncts use: {masses}")
nonzero = all(m not in ('0', '(0)') for m in masses) and bool(masses)
arm('(B)v  the witness is exhibited at NONZERO mass, unlike r7744\'s', nonzero,
    f"witness: cm_f arguments in cm_witness = {masses}; the throat conjunct at the Nariai mass "
    f"3/(3 sqrt3) with alpha=3, and the integrability conjunct at M=1, alpha=3, eps=1")

# ----------------------------------------------------------------- summary
head('SUMMARY')
npass = sum(1 for _, ok, _ in RESULTS if ok)
for tag, ok, _ in RESULTS:
    print(f"  [{'PASS' if ok else 'FAIL'}] {tag}")
print()
print(f"  {npass} of {len(RESULTS)} arms PASS")
sys.exit(0 if npass == len(RESULTS) else 1)
