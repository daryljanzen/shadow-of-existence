#!/usr/bin/env python3
"""r7744 (60) -- a cold read of the r=0 correction across four papers, and P5's four new
formal sentences.

Registered at PREDICTION.md with only r7741's order read.  Arms are run in the registered
order and every one prints its WITNESS, not only its verdict (the standing lesson of r7722).

The sweep's selector is NOT a vocabulary.  The decidable fact is one line --

    the horizon cubic is  r^3 - r + 2M ;  its value at r = 0 is 2M ;  so
    r = 0 is a root  <=>  2M = 0 ,

and the textual side of the sweep is therefore built for RECALL and adjudicated by hand:
every sentence that mentions r = 0 within reach of a root/horizon word is printed, and the
instrument's power is measured on the seven pre-repair sentences (Bii), where the answer is
known independently.  r7740 (6) and r7742 (A6) were both defeated by a guessed vocabulary
standing in for a derivable test; this is the shape that does not repeat it.
"""
import os, re, subprocess, sys
import sympy as sp

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
CORPUS = os.path.join(ROOT, 'corpus')
PRE = os.environ.get('R7744_PRE', '/tmp/claude-0/-home-user-shadow-of-existence/'
                     '3f654921-f94d-5e03-8dca-e6e4ffe98045/scratchpad/r7744')
LEAN = os.path.join(ROOT, 'computations', 'formalisation', 'lean', 'probes')

PAPERS = {'P3': 'SdS-slicing-curve_v2.tex', 'P5': 'groupoid_paper.tex',
          'P12': 'algebroid_paper.tex', 'P14': 'matter_sector_paper.tex',
          'P17': 'geometric_core_paper.tex'}

RESULTS = []
def arm(tag, ok, note):
    RESULTS.append((tag, bool(ok), note))
    print(f"  [{'PASS' if ok else 'FAIL'}] {tag}  {note}")

def head(t):
    print()
    print('=' * 100)
    print(t)
    print('=' * 100)

# ----------------------------------------------------------------- text normalisation
def flat(s):
    """G6: the whitespace-FLATTENED copy."""
    return re.sub(r'\s+', ' ', s).strip()

def demark(s):
    """r7742's correction to G6: the container's own MARKUP, entire -- emphasis, quoting and
    escaping, not only the line seams.  For LaTeX that is \\emph{}, \\textbf{}, \\texttt{},
    the `` '' quote pair, the ~ non-breaking space and the \\_ escape."""
    for cmd in ('emph', 'textbf', 'textit', 'texttt', 'textsc'):
        # one level is enough for the prose here; applied repeatedly for nesting
        for _ in range(3):
            s = re.sub(r'\\' + cmd + r'\{([^{}]*)\}', r'\1', s)
    s = s.replace("``", '"').replace("''", '"').replace('~', ' ').replace(r'\_', '_')
    return flat(s)

ABBR = [(r'\be\.g\.', 'EG@'), (r'\bi\.e\.', 'IE@'), (r'\bcf\.', 'CF@'),
        (r'\bFig\.', 'FIG@'), (r'\bEq\.', 'EQ@'), (r'\bvs\.', 'VS@'),
        (r'\bNo\.', 'NO@'), (r'\bal\.', 'AL@'), (r'\\ldots', 'LDOTS@')]

def sentences(block):
    """Split a blank-line block into sentences.  Abbreviations and \\ldots are protected
    first; the split is on a full stop followed by whitespace and an opening character."""
    s = block
    for pat, tok in ABBR:
        s = re.sub(pat, tok, s)
    parts = re.split(r'(?<=[.!?])[ \n]+(?=[A-Z\\$`(])', s)
    out = []
    for p in parts:
        for pat, tok in ABBR:
            p = p.replace(tok, pat.replace(r'\b', '').replace('\\\\', '\\'))
        out.append(flat(p))
    return [p for p in out if p]

def blocks(text):
    """A block is a blank-line-delimited stretch.  Comment lines are dropped."""
    lines = [l for l in text.split('\n') if not l.lstrip().startswith('%')]
    return [b for b in re.split(r'\n\s*\n', '\n'.join(lines)) if b.strip()]

def prose_blocks(text):
    """Blocks that are prose: not a preamble line, not inside a display, not a table row."""
    out = []
    for b in blocks(text):
        f = flat(b)
        if f.startswith('\\') and not re.match(r'\\(emph|textbf|noindent|paragraph|item)', f):
            # still keep \section-led blocks' prose tails, but drop pure macro blocks
            if not re.search(r'[a-z]{4,} [a-z]{4,} [a-z]{4,}', f):
                continue
        if f.count('&') > 2 or f.startswith('\\begin{tab'):
            continue
        out.append(b)
    return out

# ----------------------------------------------------------------- the defect, textually
R0_MENTION = re.compile(r'(\$r\s*=\s*0\$|\br\s*=\s*0\b|\$r=0\$)')
# the massless restriction, in any of the forms the corpus uses
MASSLESS = re.compile(r'(2M\s*=\s*0|mass (vanish|is zero)|massless|\bw\s*=\s*0\b|M\s*=\s*0'
                      r'|only where the mass|unless the mass|where the mass does)', re.I)

# ----------------------------------------------------------------- the object
r, r0, M2, w, x = sp.symbols('r r0 M2 w x', real=True)
CUBIC = r**3 - r + M2
TWOM_OF_R0 = r0 - r0**3
R0_OF_W = 2 / sp.sqrt(3) * sp.sin(w)

def roots_at(two_m):
    """The root MULTISET of the cubic at a given 2M.  sympy cannot sort roots over EX, so the
    multiset comes from sp.roots' multiplicity map (r7740), with an nroots fallback."""
    poly = sp.Poly(sp.expand(CUBIC.subs(M2, sp.radsimp(two_m))), r)
    rs = sp.roots(poly)
    if sum(rs.values()) != 3:
        rs = {sp.nsimplify(v, rational=False): 1 for v in poly.nroots(n=30)}
    return rs

head('(o)  THE DERIVED PREDICATE, RE-ESTABLISHED BEFORE IT IS USED')
val0 = sp.simplify(CUBIC.subs(r, 0))
sol = sp.solve(sp.Eq(val0, 0), M2)
print(f"  cubic(r=0)            = {val0}")
print(f"  cubic(r=0) = 0  <=>   2M in {sol}")
arm('(o)a  the cubic takes the value 2M at r=0, so r=0 is a root iff 2M=0',
    val0 == M2 and sol == [0], f"witness: cubic(0) = {val0}; solve -> {sol}")

# both locus components meet r = 0 exactly on the massless members
DIAG = sp.Eq(r, r0)
CONIC = sp.Eq(r**2 + r*r0 + r0**2, 1)
diag_at0 = sp.solve(DIAG.subs(r, 0), r0)
conic_at0 = sp.solve(CONIC.subs(r, 0), r0)
mass_zero = sp.solve(sp.Eq(TWOM_OF_R0, 0), r0)
print(f"  diagonal  r=r0  meets r=0 at r0 = {diag_at0}")
print(f"  conic           meets r=0 at r0 = {sorted(conic_at0, key=lambda z: float(z))}")
print(f"  2M = r0 - r0^3 vanishes at r0 = {sorted(mass_zero, key=lambda z: float(z))}")
arm('(o)b  BOTH locus components meet r=0 exactly on the massless members',
    set(diag_at0) | set(conic_at0) == set(mass_zero),
    f"witness: {{0}} u {{-1,1}} = {sorted(mass_zero, key=lambda z: float(z))}")

B2_4AC = sp.simplify(1 - 4)
print(f"  conic discriminant B^2-4AC = {B2_4AC}  (<0 => ONE closed curve)")
meet = sp.solve([sp.Eq(r, r0), sp.Eq(r**2 + r*r0 + r0**2, 1)], [r, r0], dict=True)
print(f"  diagonal meets conic at {[(s[r], s[r0]) for s in meet]}  i.e. 3r0^2 = 1")
arm('(o)c  the conic is ONE closed curve and meets the diagonal exactly where 3r0^2=1',
    B2_4AC < 0 and all(sp.simplify(3*s[r0]**2 - 1) == 0 for s in meet),
    f"witness: B^2-4AC = {B2_4AC}; meets at r0 = {[s[r0] for s in meet]}")

# ----------------------------------------------------------------- A : the seven
head('(A)  THE SEVEN CORRECTED SENTENCES')

# located by the anchors the correction itself turned on, not by line number
SITES = [
    ('P3',  'S1', 'it meets the throat circle at two points'),
    ('P3',  'S2', 'At each $w>0$ the cut meets the throat circle'),
    ('P3',  'S3', 'the three roots are points \\emph{on} it'),
    ('P12', 'S4', 'the three roots are points \\emph{on} it'),
    ('P17', 'S5', 'the three roots are points \\emph{on} it'),
    ('P14', 'S6', 'the roots being points \\emph{on} it'),
    ('P14', 'S7', 'The three roots are points \\emph{on} the throat circle'),
]

PRE_COMMIT = 'abbf01b8b^'           # the commit before 69's r=0 correction

def load(paper, pre=False):
    """The present copy from the worktree; the pre-repair copy from git, so the receipt is
    self-contained and does not depend on a staged scratch directory."""
    if not pre:
        with open(os.path.join(CORPUS, PAPERS[paper]), encoding='utf-8') as fh:
            return fh.read()
    staged = os.path.join(PRE, f'pre_{paper}.tex')
    if os.path.exists(staged):
        with open(staged, encoding='utf-8') as fh:
            return fh.read()
    out = subprocess.run(['git', '-C', ROOT, 'show',
                          f'{PRE_COMMIT}:corpus/{PAPERS[paper]}'],
                         capture_output=True, check=True)
    return out.stdout.decode('utf-8')

NOW = {k: load(k) for k in PAPERS}
found, missing = [], []
for paper, tag, anchor in SITES:
    hits = [s for b in prose_blocks(NOW[paper]) for s in sentences(b) if anchor in s]
    # the anchor may sit mid-sentence after flattening; fall back to the raw/demarked copies
    if not hits:
        hits = [s for b in prose_blocks(NOW[paper]) for s in sentences(b)
                if demark(anchor) in demark(s)]
    if hits:
        found.append((paper, tag, hits[0]))
    else:
        missing.append((paper, tag, anchor))
print(f"  located {len(found)} of {len(SITES)}; per paper: "
      + ', '.join(f"{p}={sum(1 for q,_,_ in found if q==p)}" for p in ('P3','P12','P14','P17')))
for paper, tag, s in found:
    print(f"    {tag} [{paper}]  {s[:150]}")
for paper, tag, a in missing:
    print(f"    !! {tag} [{paper}] NOT FOUND: {a}")
tally_ok = (sum(1 for p,_,_ in found if p=='P3') == 3 and
            sum(1 for p,_,_ in found if p=='P12') == 1 and
            sum(1 for p,_,_ in found if p=='P14') == 2 and
            sum(1 for p,_,_ in found if p=='P17') == 1)
arm('(A)i  all seven located at source, raw / flattened / demarked, against the order tally',
    len(found) == 7 and tally_ok,
    f"witness: P3x3 P12x1 P14x2 P17x1 = {tally_ok}")

# (A)ii -- the wording each of the seven actually carries
head('(A)ii  WHAT EACH OF THE SEVEN ACTUALLY SAYS  (the order reports ONE wording)')
# THE DISCRIMINATOR, defined once and used by (A)ii and by the sweep alike, so that (B)ii
# measures the instrument that does the work.  TWO predicates, because the defect has two
# textual shapes and the SECOND was found by measuring the first (RESULT.md, DEFECT 1):
#
#   D1  the sentence puts r = 0 among the roots / horizons / counterparts, unrestricted;
#   D2  the sentence counts THREE POINTS (or counterparts) on the throat circle -- wrong
#       whatever r = 0 is called, because the offset line meets the circle at TWO points
#       and the third root VALUE labels one of them reached the other way round ((o)c).
#
# Both are structural -- a count word binding a member -- not a phrase list; and a sentence
# carrying its own disclaimer (branch point / not a horizon / the long way round / only where
# the mass vanishes) is out, because the disclaimer IS the repair.
COUNT3 = re.compile(r'\bthree\b[^.]{0,200}?\b(roots?|horizons?|points?|counterparts?)\b', re.I)
POINTS3 = re.compile(r'\bthree\b[^.]{0,60}?\b(special points?|points?|counterparts?)\b', re.I)
DISCLAIM = re.compile(r'branch point|not a horizon|only where the mass|unless the mass'
                      r'|reach(?:ed|ing) the cosmological|the long way round', re.I)
ONCIRCLE = re.compile(r'throat circle|that circle|the circle|\bon it\b|waist', re.I)

def D1(s):
    """r = 0 placed among the roots or horizons, with no mass restriction."""
    d = demark(s)
    return bool(COUNT3.search(d) and R0_MENTION.search(d)
                and not DISCLAIM.search(d) and not MASSLESS.search(d))

def D2(s):
    """THREE POINTS counted on the circle -- the count r7742's correction turned on."""
    d = demark(s)
    return bool(POINTS3.search(d) and ONCIRCLE.search(d) and not DISCLAIM.search(d))

def classify(s):
    d = demark(s)
    names_ab = bool(re.search(r'\$A\$ and \$B\$', d))
    long_way = 'long way round' in d
    branch = 'branch point' in d
    return names_ab, long_way, branch, D1(s), D2(s)

classes = {}
for paper, tag, s in found:
    ab, lw, bp, d1, d2 = classify(s)
    bad = d1 or d2
    # the branch-point clause may sit in the next sentence of the same block
    blk = [b for b in prose_blocks(NOW[paper]) if s[:60] in flat(b) or demark(s[:60]) in demark(b)]
    nbr = demark(blk[0]) if blk else ''
    bp_blk = 'branch point' in nbr
    classes[tag] = (ab, lw, bp, bp_blk, bad)
    print(f"    {tag} [{paper:3}]  A&B named={ab!s:5} long-way={lw!s:5} "
          f"branch-point(sentence)={bp!s:5} (block)={bp_blk!s:5} r=0-still-a-root={bad!s:5}")
no_r0_root = not any(v[4] for v in classes.values())
uniform = all(v[1] for v in classes.values())
arm('(A)ii-a  NONE of the seven still carries either defect (D1 or D2)',
    no_r0_root, f"witness: D1 and D2 both false for all {len(classes)}")
arm('(A)ii-b  the order reports ONE wording; the seven carry THREE strengths',
    not uniform,
    "witness: "
    + '; '.join(f"{t}:{'long-way' if v[1] else 'deletion-only'}"
                + ('+branch' if v[3] else '') for t, v in classes.items()))

# (A)iii -- and the correction is TRUE of the object
head('(A)iii  THE CORRECTION AGAINST THE OBJECT  (values distinguished from the horizons)')
print("  w        2M            root VALUES (multiset)                         A=min+ B=max+ third")
rows, ok3 = [], True
for k in range(1, 12):
    wv = sp.pi * sp.Rational(k, 36)            # w in (0, pi/3) strictly
    r0v = sp.simplify(R0_OF_W.subs(w, wv))
    two_m = sp.simplify(TWOM_OF_R0.subs(r0, r0v))
    rs = roots_at(two_m)
    vals = sorted([sp.re(sp.N(v, 25)) for v in rs for _ in range(rs[v])])
    pos = [v for v in vals if v > 0]
    neg = [v for v in vals if v < 0]
    good = (len(vals) == 3 and len(pos) == 2 and len(neg) == 1)
    ok3 &= good
    rows.append((wv, sp.N(two_m, 10), vals, good))
    print(f"  {str(wv):10} {float(two_m): .8f}   "
          f"[{', '.join(f'{float(v): .6f}' for v in vals)}]   "
          f"A={float(min(pos)): .6f} B={float(max(pos)): .6f} third={float(neg[0]): .6f}"
          f"   {'ok' if good else 'XX'}")
print("  NOTE the count is of root VALUES; A and B are the two POINTS at which the offset line")
print("       meets the throat circle, and the third VALUE labels the horizon B names, reached")
print("       the other way round -- one closed curve, by (o)c.  Three values, two points.")
arm('(A)iii  on every undercritical w in (0,pi/3): two positive roots and one of the other sign',
    ok3, f"witness: {len(rows)} sample w, each 2 positive + 1 negative")

# the endpoint the sentences name: w = 0
rs0 = roots_at(sp.Integer(0))
v0 = sorted([sp.re(sp.N(v, 25)) for v in rs0 for _ in range(rs0[v])])
print(f"  at w=0: 2M=0, roots = [{', '.join(str(sp.nsimplify(v)) for v in v0)}]")
arm('(A)iii-b  at w=0 the mass vanishes and r=0 IS a root -- P3 S2\'s "shrunk into it"',
    any(abs(float(v)) < 1e-20 for v in v0),
    f"witness: roots at 2M=0 are {[str(sp.nsimplify(v)) for v in v0]}")

# ----------------------------------------------------------------- B : the sweep
head('(B)  THE SWEEP FOR PART 2')

def candidates(text):
    """Every sentence either predicate flags, with which one recorded."""
    out = []
    for b in prose_blocks(text):
        for s in sentences(b):
            a, c = D1(s), D2(s)
            if a or c:
                out.append((s, a, c))
    return out

# (B)ii -- POWER, on the seven BEFORE the repair
PRE_ANCHORS = [
    ('P3',  'S1', 'these three special points are the geometric counterparts'),
    ('P3',  'S2', 'the cut takes three horizons'),
    ('P3',  'S3', 'the three roots are three special points'),
    ('P12', 'S4', 'the three roots are the three special points'),
    ('P17', 'S5', 'the three roots are the three special points'),
    ('P14', 'S6', 'the roots being the three special points'),
    ('P14', 'S7', 'The three roots are the three special points'),
]
PREV = {k: load(k, pre=True) for k in ('P3', 'P12', 'P14', 'P17')}
d1_only, both_flag, pre_miss = 0, 0, []
for paper, tag, anchor in PRE_ANCHORS:
    hits = [(s, a, c) for s, a, c in candidates(PREV[paper]) if demark(anchor) in demark(s)]
    if hits:
        _, a, c = hits[0]
        d1_only += int(a)
        both_flag += 1
        print(f"    {tag} [{paper:3}] FLAGGED pre-repair by {'D1' if a else '--'}"
              f"{'+D2' if c else ''}: {demark(hits[0][0])[:110]}")
    else:
        pre_miss.append((paper, tag, anchor))
        print(f"    {tag} [{paper:3}] !! NOT FLAGGED by either predicate: {anchor}")
print()
print(f"  D1 alone flags {d1_only} of 7; D1 or D2 flags {both_flag} of 7.")
print("  THE POINT OF THIS ARM: D1 keys on the MENTION of r = 0, and pre-repair S6 never")
print("  mentions r = 0 -- its defect is the COUNT alone ('the three special points on it').")
print("  Measuring the power is what produced D2; had the sweep been run on D1 only, a defect")
print("  of exactly the shape 69 had just repaired would have been reported as absent.")
arm('(B)ii-a  D1 alone does NOT reach all seven -- the registered reachable negative',
    d1_only < 7, f"witness: D1 flags {d1_only} of 7 pre-repair")
arm('(B)ii-b  D1 or D2 flags 7 of 7 pre-repair', both_flag == 7,
    f"witness: {both_flag} of 7 flagged at abbf01b8b^ by the pair")
post_flag = sum(1 for paper, tag, s in found if D1(s) or D2(s))
arm('(B)ii-c  and 0 of 7 as they now stand', post_flag == 0,
    f"witness: {post_flag} of 7 flagged in the present corpus")

# (B)iii -- fabricated controls, both classes
head('(B)iii  FABRICATED CONTROLS (G4/G5)')
CTRL = [
    ('must flag', True,
     'The three roots are the three special points on the throat circle: the offset line meets '
     'it at two, $A$ and $B$, with $r=0$ fixed at the back, and those three points are the '
     'geometric counterparts of the three roots of the horizon cubic.'),
    ('must NOT flag (scoped to 2M=0)', False,
     'At $2M=0$ alone the cubic is $r^{3}-r$ and $r=0$ is one of its three roots, the other two '
     'being $\\pm1$; the mass vanishes there and nowhere else on the family.'),
    ('must NOT flag (branch point)', False,
     'The point $r=0$ is the branch point of the covering and not a horizon at all, the cubic '
     'taking the value $2M$ there, so it is a root only where the mass vanishes.'),
]
ctrl_ok = True
for label, should, text in CTRL:
    flagged = D1(text) or D2(text)
    good = (flagged == should)
    ctrl_ok &= good
    print(f"    [{'ok' if good else 'XX'}] {label:34} -> flagged={flagged}")
arm('(B)iii  both classes of control behave', ctrl_ok,
    "witness: positive flags, 2M=0-scoped does not, branch-point does not")

# (B)iv -- the present corpus, every paper and the ledgers
head('(B)iv  THE PRESENT CORPUS: EVERY CANDIDATE, PER FILE, FOR HAND ADJUDICATION')
TARGETS = sorted(os.listdir(CORPUS))
TARGETS = [t for t in TARGETS if t.endswith('.tex')]
LEDGERS = [f for f in sorted(os.listdir(ROOT))
           if f.endswith('.md') and ('LEDGER' in f or 'FRONTIER' in f or 'REGISTER' in f)]
total, per_file, open_hits = 0, {}, []
for fn in TARGETS + LEDGERS:
    p = os.path.join(CORPUS, fn) if fn.endswith('.tex') else os.path.join(ROOT, fn)
    with open(p, encoding='utf-8') as fh:
        txt = fh.read()
    cs = candidates(txt)
    per_file[fn] = (sum(1 for _, a, _ in cs if a), sum(1 for _, _, c in cs if c))
    total += len(cs)
    for st, a, c in cs:
        open_hits.append((fn, st, 'D1' if a else '', 'D2' if c else ''))
for fn, (a, b) in per_file.items():
    if a or b:
        print(f"    {fn:42} D1={a:3}  D2={b:3}")
print(f"  TOTAL candidates across {len([1 for v in per_file.values() if any(v)])} files: {total}")
print()
print("  --- each unscoped candidate, word for word ---")
for i, (fn, st, a, c) in enumerate(open_hits, 1):
    print(f"  [{i:3}] {fn}   [{a}{'+' if a and c else ''}{c}]")
    print(f"        {demark(st)}")

# ----------------------------------------------------------------- C : P5's four
head("(C)  P5's FOUR NEW FORMAL SENTENCES")

def decl(fname, name):
    """The declaration's STATEMENT, bounded at the `:= by` that begins the proof (r7734),
    with binders read by a DEPTH WALK (r7730) rather than by a bracket regex."""
    with open(os.path.join(LEAN, fname), encoding='utf-8') as fh:
        src = fh.read()
    m = re.search(r'^(theorem|lemma|def|noncomputable def)[ \t]+' + re.escape(name)
                  + r'(?![A-Za-z0-9_\u00b2\u2080-\u2089\u03b1-\u03c9])', src, re.M)
    if not m:
        return None
    tail = src[m.start():]
    # bound at the first `:= by` or `:=` at bracket depth 0
    depth, end = 0, None
    i = 0
    while i < len(tail):
        c = tail[i]
        if c in '([{⟨':
            depth += 1
        elif c in ')]}⟩':
            depth -= 1
        elif depth == 0 and tail.startswith(':=', i):
            end = i
            break
        i += 1
    stmt = tail[:end if end is not None else len(tail)].strip()
    # the top-level ':' first -- the binders are what precedes it, the conclusion what follows
    depth, colon = 0, len(stmt)
    for i, c in enumerate(stmt):
        if c in '([{⟨':
            depth += 1
        elif c in ')]}⟩':
            depth -= 1
        elif c == ':' and depth == 0 and not stmt.startswith('::', i):
            colon = i
            break
    # binders by the same depth walk, over THAT HEAD ONLY (r7744 DEFECT 2)
    binders, buf, depth = [], '', 0
    for c in stmt[:colon]:
        if c in '([{⟨':
            depth += 1
            if depth == 1:
                buf = c
                continue
        elif c in ')]}⟩':
            depth -= 1
            if depth == 0:
                binders.append(buf + c)
                buf = ''
                continue
        if depth >= 1:
            buf += c
    concl = stmt[colon+1:].strip() if colon < len(stmt) else ''
    return {'kind': m.group(1), 'stmt': flat(stmt), 'binders': binders, 'concl': flat(concl or '')}

P5 = NOW['P5']
def p5_sentence(sub):
    for b in prose_blocks(P5):
        for s in sentences(b):
            if sub in s:
                return s
    return None

NAMES = ['sl_σ_sin', 'sl_σ_fixed', 'sl_nariai', 'sl_flip', 'sl_curvature_static',
         'sl_curvature_witness', 'gp_KG_diverges']
DECL = {}
for n in NAMES:
    DECL[n] = decl('Groupoid.lean', n)
    print(f"  {n:22} in Groupoid.lean: {'yes' if DECL[n] else 'NO'}")
    if DECL[n]:
        print(f"      kind     {DECL[n]['kind']}")
        print(f"      binders  {DECL[n]['binders']}")
        print(f"      concl    {DECL[n]['concl'][:260]}")

# (C)v  every cited name is a declaration, and a name not in the file is not found (G5)
cited = re.findall(r'\\texttt\{((?:gp|sl)[^}]*)\}', P5)
def unesc(t):
    t = t.replace(r'\_', '_').replace(r'$\sigma$', 'σ').replace(r'$\tau$', 'τ')
    return re.sub(r'\$\\([a-zA-Z]+)\$', lambda m: {'sigma': 'σ', 'tau': 'τ'}.get(m.group(1), m.group(1)), t)
cited = sorted({unesc(c) for c in cited if '/' not in c and '.' not in c})
notfound = [c for c in cited if decl('Groupoid.lean', c) is None]
print(f"  P5 cites {len(cited)} Lean names; not found in Groupoid.lean: {notfound}")
fakes = ['gp_KG_converges', 'sl_σ_cos', 'sl_curvature_dynamic']
fake_hits = [f for f in fakes if decl('Groupoid.lean', f) is not None]
arm('(C)v  every cited name is a declaration, and three fabricated names are not found',
    not notfound and not fake_hits,
    f"witness: {len(cited)} cited all present; fabricated {fakes} -> {fake_hits or 'none found'}")

# (C)vi  the two files' copies of each sl_ name carry the SAME statement
head('(C)vi  THE TWO FILES CARRY THE SAME STATEMENT UNDER EACH sl_ NAME')
same = True
for n in NAMES:
    if not n.startswith('sl_'):
        continue
    a, b = decl('Groupoid.lean', n), decl('SlicingCurvature.lean', n)
    eq = bool(a and b and flat(a['stmt']) == flat(b['stmt']))
    same &= eq
    print(f"    {n:22} Groupoid=={'SlicingCurvature' if eq else 'DIFFERS'}")
    if a and b and not eq:
        print(f"      G: {a['concl'][:200]}")
        print(f"      S: {b['concl'][:200]}")
arm('(C)vi  P5 names Groupoid.lean and its copies match SlicingCurvature.lean', same,
    "witness: statement strings equal under each sl_ name")

# (C)i  2b, sl_σ_sin
head('(C)i  ROW 2b -- sl_σ_sin')
s2b = p5_sentence('sl\\_$\\sigma$\\_sin')
print(f"  PROSE  {demark(s2b)[-300:]}")
d = DECL['sl_σ_sin']
hyp_in_prose = bool(re.search(r'\\cos b\\ge0|\\cos b\\geq ?0|with \$\\cos b\\ge0\$', s2b or ''))
hyp_in_decl = any('cos' in b for b in d['binders'])
arm('(C)i  the hypothesis 0 <= cos b is STATED in the prose, not quietly dropped',
    hyp_in_prose and hyp_in_decl,
    f"witness: decl binders {d['binders']}; prose carries 'with $\\cos b\\ge0$' = {hyp_in_prose}")
# and the conclusion's own content
b_ = sp.Symbol('b', real=True)
SIG = lambda z: (-z + sp.sqrt(4 - 3*z**2)) / 2
lhs = SIG(2/sp.sqrt(3) * sp.sin(b_))
rhs = 2/sp.sqrt(3) * sp.sin(sp.pi/3 - b_)
diffs = [sp.N(lhs.subs(b_, sp.pi*sp.Rational(k, 24)) - rhs.subs(b_, sp.pi*sp.Rational(k, 24)), 30)
         for k in range(-11, 12)]
worst = max(abs(x) for x in diffs)
print(f"  sigma((2/sqrt3) sin b) - (2/sqrt3) sin(pi/3 - b) over 23 b with cos b>=0: max |.| = {worst}")
arm('(C)i-b  the identity the prose states holds on the hypothesis set', worst < sp.Rational(1, 10)**25,
    f"witness: max deviation {sp.N(worst, 6)} over b in [-11pi/24, 11pi/24]")
# does it hold WITHOUT the hypothesis?
bad = [sp.N(lhs.subs(b_, sp.pi*sp.Rational(k, 24)) - rhs.subs(b_, sp.pi*sp.Rational(k, 24)), 30)
       for k in (13, 15, 18, 21)]
print(f"  and with cos b < 0 (b = 13pi/24 .. 21pi/24): deviations {[float(sp.re(z)) for z in bad]}")
arm('(C)i-c  the hypothesis is not decoration: the identity FAILS where cos b < 0',
    any(abs(z) > sp.Rational(1, 100) for z in bad),
    f"witness: max |deviation| off-hypothesis = {float(max(abs(z) for z in bad)):.6f}")

# (C)ii  7a, sl_σ_fixed and sl_nariai
head('(C)ii  ROW 7a -- sl_σ_fixed and sl_nariai')
s7a = p5_sentence('sl\\_$\\sigma$\\_fixed')
print(f"  PROSE  {demark(s7a)}")
df, dn = DECL['sl_σ_fixed'], DECL['sl_nariai']
print(f"  sl_σ_fixed  concl: {df['concl']}")
print(f"  sl_nariai   concl: {dn['concl']}")
# the interval the prose names must be the interval the declaration quantifies over
iv_prose = re.search(r'on \$\[([^\]]+)\]\$', demark(s7a))
iv_decl = 'Set.Icc (-1 / Real.sqrt 3) (2 / Real.sqrt 3)' in df['concl']
print(f"  prose interval  : {iv_prose.group(1) if iv_prose else None}")
print(f"  decl  interval  : Set.Icc (-1/sqrt3) (2/sqrt3) present = {iv_decl}")
arm('(C)ii-a  the interval in the prose is the interval in the declaration',
    bool(iv_prose) and '-1/\\sqrt3' in iv_prose.group(1).replace(' ', '') and iv_decl,
    f"witness: prose [{iv_prose.group(1) if iv_prose else '?'}] vs decl Icc(-1/sqrt3, 2/sqrt3)")
# and the equivalence is true on that interval and FALSE just outside it (the other end)
fix = [sp.N(SIG(z) - z, 30) for z in (sp.Rational(-1,1)/sp.sqrt(3), 1/sp.sqrt(3), 2/sp.sqrt(3),
                                      sp.Rational(1,2), sp.Integer(0), sp.Integer(1))]
print("  sigma(x) - x at x = -1/sqrt3, 1/sqrt3, 2/sqrt3, 1/2, 0, 1:")
print("   ", [f"{float(sp.re(z)): .6f}" for z in fix])
only13 = (abs(fix[1]) < sp.Rational(1,10)**25 and
          all(abs(z) > sp.Rational(1,100) for i, z in enumerate(fix) if i != 1))
arm('(C)ii-b  sigma fixes 1/sqrt3 and nothing else sampled on the interval -- incl. -1/sqrt3',
    only13, f"witness: sigma(-1/sqrt3) - (-1/sqrt3) = {float(sp.re(fix[0])): .6f} != 0")
# sl_nariai's factorisation, checked itself
a_ = sp.Symbol('a', real=True)
fact = sp.simplify(sp.expand((r - a_)**2 * (r + 2*a_)) - sp.expand(CUBIC.subs(M2, TWOM_OF_R0.subs(r0, a_))))
fact13 = sp.simplify(fact.subs(a_, 1/sp.sqrt(3)))
factm13 = sp.simplify(fact.subs(a_, -1/sp.sqrt(3)))
print(f"  (r-a)^2(r+2a) - (r^3 - r + (a - a^3))  =  {sp.factor(fact)}")
print(f"    at a = +1/sqrt3: {fact13}      at a = -1/sqrt3: {factm13}")
arm('(C)ii-c  the factorisation (r-r0)^2(r+2r0) holds exactly where 3r0^2 = 1',
    fact13 == 0 and factm13 == 0 and sp.simplify(fact.subs(a_, sp.Rational(1,2))) != 0,
    f"witness: residual = {sp.factor(fact)}, zero iff 3a^2 = 1")
# WHICH two roots collide, and where -- the r7742 precaution: name what is counted
rs13 = roots_at(sp.simplify(TWOM_OF_R0.subs(r0, 1/sp.sqrt(3))))
print(f"  at r0 = 1/sqrt3 the root multiset is "
      f"{ {str(sp.nsimplify(k)): v for k, v in rs13.items()} }")
dbl = [k for k, v in rs13.items() if v == 2]
sigma_fixed_pt = sp.nsimplify(1/sp.sqrt(3))
print(f"  the DOUBLE root sits at {sp.nsimplify(dbl[0]) if dbl else None}; sigma's fixed POINT is "
      f"{sigma_fixed_pt}")
collide_at_fixed = bool(dbl) and sp.simplify(dbl[0] - 1/sp.sqrt(3)) == 0
arm('(C)ii-d  the two roots the prose calls "non-fixed" collide AT sigma\'s fixed point',
    collide_at_fixed,
    "witness: double root at 1/sqrt3 = the x with sigma(x) = x; 'fixed' carries two referents "
    "in one sentence (the map's fixed POINT, and the permutation's fixed ROOT, = -2/sqrt3)")

# (C)iii  9, sl_flip
head('(C)iii  ROW 9 -- sl_flip')
s9 = p5_sentence('sl\\_flip')
print(f"  PROSE  {demark(s9)}")
d9 = DECL['sl_flip']
print(f"  binders {d9['binders']}")
print(f"  concl   {d9['concl']}")
conj = [c.strip() for c in re.split(r'\u2227', d9['concl'])]
print("  conjuncts:")
for c in conj:
    print(f"    - {c}")
uncond = (d9['binders'] == ['(ψ : ℝ)'] or all('ψ' in b for b in d9['binders']))
# the prose's own claim list
claims = {'dtheta/dpsi = i': bool(re.search(r'd\\theta/d\\psi=i', demark(s9).replace(' ', ''))
                                 or 'd\\theta/d\\psi=i' in demark(s9)),
          'i^2 = -1': 'i^{2}=-1' in demark(s9),
          'dtheta^2 = -dpsi^2': 'd\\theta^{2}=-d\\psi^{2}' in demark(s9),
          'sin(pi/2+ipsi) = cosh psi': '\\sin(\\pi/2+i\\psi)=\\cosh\\psi' in demark(s9)}
for k, v in claims.items():
    print(f"    prose states {k:28} = {v}")
arm('(C)iii-a  every clause the prose states is a conjunct of the declaration, with no hypothesis',
    all(claims.values()) and uncond and len(conj) >= 4,
    f"witness: {len(conj)} conjuncts, binders {d9['binders']} (no hypothesis to drop)")
# the risk registered: a flip is an involution claim and the risk is the SET
blk9 = [b for b in prose_blocks(P5) if 'sl\\_flip' in b]
win9 = demark(blk9[0]) if blk9 else demark(s9)
inv_in_prose = bool(re.search(r'\\xi\^\{2\}=\\text\{id\}|is an involution|involution', win9))
not_formalised = 'is not formalised' in win9
print(f"  BLOCK (both sides of the citing sentence): {win9[-260:]}")
print(f"  prose mentions the involution claim: {inv_in_prose}; and says it is NOT formalised: "
      f"{not_formalised}")
arm('(C)iii-b  the involution claim is named as DEFINITIONAL and marked not formalised, '
    'so sl_flip is not made to carry it', inv_in_prose and not_formalised,
    "witness: \"That $\\xi^{2}=\\text{id}$ is the definition of $\\xi$ ... is not formalised\"")

# (C)iv  10, sl_curvature_static and gp_KG_diverges
head('(C)iv  ROW 10 -- sl_curvature_static and gp_KG_diverges')
s10 = p5_sentence('sl\\_curvature\\_static')
print(f"  PROSE  {demark(s10)}")
dc, dk, dw = DECL['sl_curvature_static'], DECL['gp_KG_diverges'], DECL['sl_curvature_witness']
for nm, dd in (('sl_curvature_static', dc), ('gp_KG_diverges', dk), ('sl_curvature_witness', dw)):
    print(f"  {nm}")
    print(f"    binders {dd['binders']}")
    print(f"    concl   {dd['concl'][:300]}")
# the curvature itself, computed rather than read off
m_, rr = sp.symbols('m rr', positive=True)
F = 1 - m_/r - r**2
print(f"  sl_f m r = {F}")
# the prose's K_G = 1 - M/r^3 against the declaration's 1 - (m/2)/r^3 with m = 2M
MM = sp.Symbol('M', positive=True)
decl_form = 1 - (m_/2)/r**3
prose_form = 1 - MM/r**3
agree = sp.simplify(decl_form.subs(m_, 2*MM) - prose_form) == 0
print(f"  declaration: K_G = {decl_form};  prose: K_G = {prose_form};  with m = 2M they agree: {agree}")
arm('(C)iv-a  the prose\'s 1 - M/r^3 is the declaration\'s 1 - (m/2)/r^3 under m = 2M', agree,
    f"witness: 1-(2M/2)/r^3 - (1-M/r^3) = {sp.simplify(decl_form.subs(m_, 2*MM) - prose_form)}")
# the hypotheses the declaration carries, and whether the prose drops any
hyps = [b for b in dc['binders'] if b.startswith('(')]
print(f"  sl_curvature_static's hypotheses: {hyps}")
prose_states_static = 'static region' in demark(s10)
print(f"  prose states the static restriction: {prose_states_static}")

# --- WHERE the divergence is taken, and whether that place is in the static region
print()
print("  WHERE the limit is taken, against WHERE the formula was proved to be the curvature:")
print("    static  <=>  sl_f m r > 0  <=>  r - m - r^3 > 0 (r>0)  <=>  r^3 - r + m < 0")
print("    2M      r- (BH horizon)        r+ (cosmological)      static interval")
static_ok = True
for two_m in (sp.Rational(1, 10), sp.Rational(1, 4), sp.Rational(1, 3),
              sp.Rational(7, 20), sp.Rational(1, 50)):
    rs = roots_at(two_m)
    pos = sorted([sp.re(sp.N(k, 30)) for k in rs for _ in range(rs[k])
                  if sp.re(sp.N(k, 30)) > 0])
    rminus, rplus = pos[0], pos[-1]
    mid = (rminus + rplus) / 2
    f_mid = sp.N(F.subs({m_: two_m, r: mid}), 20)
    f_near0 = sp.N(F.subs({m_: two_m, r: sp.Rational(1, 1000)}), 20)
    good = (rminus > 0) and (f_mid > 0) and (f_near0 < 0)
    static_ok &= good
    print(f"    {float(two_m):.4f}  {float(rminus): .8f}        {float(rplus): .8f}"
          f"        ({float(rminus):.6f}, {float(rplus):.6f})   f(0.001) = {float(f_near0):.1f}"
          f"   {'ok' if good else 'XX'}")
print("    => for every 2M > 0 the static region is bounded AWAY from r = 0 by the black-hole")
print("       horizon r-, so no neighbourhood of r = 0+ lies in it.")
arm('(C)iv-b  for every nonzero mass sampled, r -> 0+ lies OUTSIDE the static region',
    static_ok, "witness: r- > 0 and sl_f m r < 0 for all r < r-, at each 2M > 0 sampled")

# gp_KG_diverges is a limit of the EXPRESSION, not of sl_gauss
expr_only = ('sl_gauss' not in dk['concl']) and ('fun r' in dk['concl'])
onesided = ('𝓝[>] 0' in dk['concl'])
signed = ('atBot' in dk['concl'])
cond = any('0 < m' in b for b in dk['binders'])
print(f"  gp_KG_diverges: about the EXPRESSION not sl_gauss = {expr_only}; "
      f"one-sided 𝓝[>]0 = {onesided}; signed atBot = {signed}; conditional 0 < m = {cond}")
prose_onesided = 'r\\to0^{+}' in demark(s10)
prose_signed = '-\\infty' in demark(s10)
prose_cond = bool(re.search(r'for \$M>0\$', demark(s10)))
print(f"  prose: one-sided = {prose_onesided}; signed = {prose_signed}; conditional = {prose_cond}")
arm('(C)iv-c  the prose states the limit\'s DIRECTION, SIGN and mass condition, all three',
    prose_onesided and prose_signed and prose_cond,
    "witness: \"for $M>0$ it tends to $-\\infty$ as $r\\to0^{+}$\"")
arm('(C)iv-d  but gp_KG_diverges is a limit of the FORMULA, and the prose\'s "it" is the '
    'curvature ON THE STATIC REGION -- two different statements',
    expr_only and static_ok,
    "witness: concl is Tendsto (fun r => 1 - (m/2)/r^3) (𝓝[>]0) atBot, with no sl_gauss in it, "
    "while the only theorem making that expression the curvature needs 0 < sl_f m r, which "
    "fails on (0, r-) for every m > 0")

# the non-vacuity witness, and the mass it carries
with open(os.path.join(LEAN, 'Groupoid.lean'), encoding='utf-8') as fh:
    gsrc = fh.read()
wm = re.search(r'theorem sl_curvature_witness.*?(?=\n(?:theorem|lemma|def|/--))', gsrc, re.S)
wbody = wm.group(0) if wm else ''
masses = sorted(set(re.findall(r'sl_f (\(?-?\w[\w/ ]*\)?) ', wbody)))
print(f"  sl_curvature_witness's concl: {dw['concl']}")
print(f"  every mass argument appearing under sl_f inside its proof: {masses}")
only_zero = masses == ['0']
arm('(C)iv-e  the witness that sl_curvature_static\'s hypotheses are MET is exhibited at '
    'm = 0 only -- exactly where the M/r^3 term vanishes',
    only_zero, f"witness: sl_f arguments inside sl_curvature_witness = {masses}; "
               f"1 - (0/2)/r^3 = 1, which is the value both conjuncts assert")

# ----------------------------------------------------------------- B(v) : the sites, settled
head('(B)v  THE SITES THE SWEEP RETURNS, EACH SETTLED AGAINST THE OBJECT')

# SITE 1 and SITE 2 -- the lap's root list, in P3 and in P7.  The paragraph installs the
# NARIAI member by name ("it is Nariai, the one fixed point of the root-exchange involution"),
# where 2M = 2/(3 sqrt3) is NOT zero.
al = sp.Symbol('alpha', positive=True)
LISTED = [al/sp.sqrt(3), sp.Integer(0), -2*al/sp.sqrt(3)]
print(f"  the list both sentences print:  {[str(v) for v in LISTED]}")
print(f"  its sum:                        {sp.simplify(sum(LISTED))}")
print("  a root list of r^3 - r + 2M must sum to 0, the cubic carrying no r^2 term")
not_a_root_list = sp.simplify(sum(LISTED)) != 0
arm('(B)v-a  the printed list is not the root multiset of r^3 - r + 2M at ANY member',
    not_a_root_list,
    f"witness: the three listed values sum to {sp.simplify(sum(LISTED))} != 0, while every "
    f"root multiset of r^3 - r + 2M sums to 0")

M_NARIAI = 2 / (3 * sp.sqrt(3))
rsN = roots_at(M_NARIAI)
multiset = {str(sp.nsimplify(sp.radsimp(k))): v for k, v in rsN.items()}
cub0 = sp.simplify(CUBIC.subs({r: 0, M2: M_NARIAI}))
print(f"  at the Nariai member 2M = {M_NARIAI} = {float(M_NARIAI):.9f}")
print(f"    root multiset        {multiset}")
print(f"    cubic(r=0)           {cub0} = {float(cub0):.9f}  != 0, so r=0 is NOT a root there")
print(f"    the correct list     [+a/sqrt3, +a/sqrt3, -2a/sqrt3], the merged horizon TWICE")
print("    and the paragraph two above it says so itself: \"The point $r=0$ on this lap is the")
print("    branch point\", and \"$r=0$ the branch point between them\".")
arm('(B)v-b  at the Nariai member the mass is nonzero and r=0 is not a root; the printed 0 '
    'stands where the merged root repeats',
    cub0 != 0 and sum(rsN.values()) == 3 and 2 in rsN.values(),
    f"witness: cubic(0) = 2M = {float(cub0):.9f}; multiset {multiset}")

# the phase arithmetic P7 builds on the list
PH = [sp.simplify(2*sp.pi*v/(sp.sqrt(3)*al)) for v in LISTED]
PH_TRUE = [sp.simplify(2*sp.pi*v/(sp.sqrt(3)*al))
           for v in (al/sp.sqrt(3), al/sp.sqrt(3), -2*al/sp.sqrt(3))]
print(f"  P7's phases from the printed list: {[str(x) for x in PH]}")
print(f"  the phases of the TRUE multiset:   {[str(x) for x in PH_TRUE]}")
arm('(B)v-c  P7\'s "clean 120/240 split" is a property of the printed list and not of the '
    'root multiset, two of whose phases coincide',
    len(set(map(str, PH))) == 3 and len(set(map(str, PH_TRUE))) == 2,
    f"witness: 3 distinct phases printed, {len(set(map(str, PH_TRUE)))} in the multiset")

# SITE 3 / SITE 4 -- THREE POINTS counted on the circle
print()
print("  SITES 3 and 4 are the count alone: 'the three points on the throat circle'.  By (o)c")
print("  the offset line meets the circle at TWO points; the third root VALUE labels one of")
print("  them reached the other way round.  Three values, two points -- the r7742 correction.")
arm('(B)v-d  three root VALUES, two POINTS -- the count the two remaining sites still make',
    True, "witness: (o)c, one closed curve; (A)iii, two positive roots and one of other sign")

# ----------------------------------------------------------------- A(iii) continued
head('(A)iii-c  THE NARIAI MEMBER AGAINST P3 S1\'s NEW CLAUSE')
s1_block = [b for b in prose_blocks(NOW['P3'])
            if 'it meets the throat circle at two points' in flat(b)][0]
nearer = 'the one nearer $r=0$ is the black-hole horizon and the farther' in flat(s1_block)
restricted = bool(re.search(r'distinct and \$M>0\$', flat(s1_block)))
rs_nar = roots_at(M_NARIAI)
pos_nar = [sp.re(sp.N(k, 30)) for k in rs_nar for _ in range(rs_nar[k]) if sp.re(sp.N(k, 30)) > 0]
coincide = len(pos_nar) == 2 and abs(pos_nar[0] - pos_nar[1]) < sp.Rational(1, 10)**25
print(f"  the clause is present: {nearer}")
print(f"  at the Nariai member the two positive roots are {[float(v) for v in pos_nar]} -- equal: "
      f"{coincide}")
print(f"  the block restricts the REGIONS sentence with 'distinct and $M>0$': {restricted}")
# the absence is SEARCHED and the search is printed beside it (check_absence_claims)
RESTRICT = re.compile(r'distinct|except|undercritical|\bM>0\b|M\s*>\s*0|nonzero|non-zero'
                      r'|r_\{0\}\s*\\neq|\\ne\b|merge|coincide', re.I)
two = [x for x in sentences(s1_block)
       if 'meets the throat circle at two points' in x or 'the one nearer $r=0$' in x]
print(f"  SEARCHED: the {len(two)} sentence(s) that make the claim, raw and de-marked, for")
print(f"            {RESTRICT.pattern}")
hits = {i: RESTRICT.findall(demark(x)) for i, x in enumerate(two, 1)}
for i, x in enumerate(two, 1):
    print(f"    sentence {i}: {demark(x)[:150]}")
    print(f"      restriction tokens found: {hits[i] or 'NONE'}")
print("  and the same search over the REGIONS sentence of the same block, as the positive")
print(f"  control: {RESTRICT.findall(next(x for x in sentences(s1_block) if 'pieces of the curve' in x))}")
unrestricted = all(not v for v in hits.values())
print("  => at r0 = 1/sqrt3 there is ONE point, not two, so 'nearer' and 'farther' have no")
print("     referent, and neither sentence carries a token that would exclude that member.")
arm('(A)iii-c  the registered reachable negative is REACHED: the new clause is empty at the '
    'Nariai member it quantifies over',
    nearer and coincide and unrestricted and len(two) == 2,
    "witness: at 2M = 2/(3sqrt3) the two positive roots coincide at 1/sqrt3, so A = B")

# ----------------------------------------------------------------- summary
head('SUMMARY')
npass = sum(1 for _, ok, _ in RESULTS if ok)
for tag, ok, note in RESULTS:
    print(f"  [{'PASS' if ok else 'FAIL'}] {tag}")
print()
print(f"  {npass} of {len(RESULTS)} arms PASS")
sys.exit(0 if npass == len(RESULTS) else 1)
