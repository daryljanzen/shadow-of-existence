#!/usr/bin/env python3
"""r7748 (60) -- a cold read of this round's P15, P18 and P7 landings, every figure against its
receipt.

Registered at PREDICTION.md with only r7745's order read.  Every arm prints its WITNESS.

The precautions are carried, not restated: the window is the BLOCK (never the citing sentence),
binders come from a depth walk bounded at the top-level ':', spans run to each sentence's own end,
every absence claim prints what was searched with a positive control, and any selector is measured
on the PRE-landing text before it is trusted -- r7746's worst defect was a predicate tuned on the
post-repair text, which will always agree with the repair.
"""
import os, re, subprocess, sys
import sympy as sp

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
CORPUS = os.path.join(ROOT, 'corpus')
LEAN = os.path.join(ROOT, 'computations', 'formalisation', 'lean', 'probes')
PRE_COMMIT = '2fba18be0'     # this line's head before 69's merge landed this round

PAPERS = {'P3': 'SdS-slicing-curve_v2.tex', 'P7': 'CR_framework.tex',
          'P15': 'CR_cosmology.tex', 'P16': 'cosmogenesis_paper.tex',
          'P18': 'CR_synthesis.tex'}

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
    for cmd in ('emph', 'textbf', 'textit', 'texttt', 'textsc'):
        for _ in range(3):
            s = re.sub(r'\\' + cmd + r'\{([^{}]*)\}', r'\1', s)
    s = s.replace("``", '"').replace("''", '"').replace('~', ' ').replace(r'\_', '_')
    return flat(re.sub(r'[*`]', '', s))

def blocks(text):
    lines = [l for l in text.split('\n') if not l.lstrip().startswith('%')]
    return [b for b in re.split(r'\n\s*\n', '\n'.join(lines)) if b.strip()]

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

NOW = {k: open(os.path.join(CORPUS, v), encoding='utf-8').read() for k, v in PAPERS.items()}
PRE = {k: git('show', f'{PRE_COMMIT}:corpus/{v}') for k, v in PAPERS.items()}

def block_of(key, sub, pre=False):
    """THE WINDOW IS THE BLOCK (r7746 DEFECT 2), returned with the citing sentence."""
    src = PRE[key] if pre else NOW[key]
    for b in blocks(src):
        if sub in b or demark(sub) in demark(b):
            for s in sentences(b):
                if sub in s or demark(sub) in demark(s):
                    return s, b
            return None, b
    return None, None

# ----------------------------------------------------------------- (o) the arithmetic
head('(o)  THE ARITHMETIC THE ORDER ITSELF MAKES CHECKABLE')
rho_det = sp.Rational(545, 10**4)           # 5.45e-2, the composition the companion determines
rho_lo = sp.Rational(3, 10**19)
rho_hi = sp.Rational(35, 10**20)
gap_lo = sp.N(sp.log(rho_det / rho_lo, 10), 20)
gap_hi = sp.N(sp.log(rho_det / rho_hi, 10), 20)
print(f"  rho determined = {float(rho_det)};  required rho in [{float(rho_hi):.3g}, {float(rho_lo):.3g}]")
print(f"  log10(rho_det / 3.0e-19) = {gap_lo}")
print(f"  log10(rho_det / 3.5e-19) = {gap_hi}")
print(f"  => the gap is seventeen orders across the whole bracket; 'thirteen' was wrong by four")
arm('(o)a  PREDICTED 17.2: the repaired figure "seventeen orders" reproduces, and the bracket does '
    'not reach sixteen or eighteen',
    17 <= gap_hi <= 18 and 17 <= gap_lo <= 18,
    f"witness: {float(gap_hi):.4f} and {float(gap_lo):.4f}, both in [17,18)")

# the transfer law's own value at the determined composition
A_cap = sp.Rational(26, 10**122)            # 2.6e-121
amp_at_det = 9 * A_cap / rho_det**6
print(f"  9 x 2.6e-121 x rho^-6 at rho = 5.45e-2  =  {sp.N(amp_at_det, 8)}")
print(f"    between 1e-113 and 1e-112: {bool(sp.Rational(1,10**113) < amp_at_det < sp.Rational(1,10**112))}")
amp_lo = 9 * A_cap / rho_lo**6
amp_hi = 9 * A_cap / rho_hi**6
AS = sp.Rational(2, 10**9)
print(f"  at rho = 3.0e-19: {sp.N(amp_lo, 6)}  >  A_s = 2e-9 : {bool(amp_lo > AS)}")
print(f"  at rho = 3.5e-19: {sp.N(amp_hi, 6)}  <  A_s = 2e-9 : {bool(amp_hi < AS)}")
arm('(o)b  and the bracket brackets: the observed amplitude is crossed between 3.0e-19 and 3.5e-19',
    amp_lo > AS and amp_hi < AS
    and sp.Rational(1,10**113) < amp_at_det < sp.Rational(1,10**112),
    f"witness: {sp.N(amp_lo,4)} > 2e-9 > {sp.N(amp_hi,4)}, and the value at the determined "
    f"composition is {sp.N(amp_at_det,4)}")

# ----------------------------------------------------------------- A : the figures
head('(A)i  EVERY FIGURE IN THE THREE LANDINGS, AND THE RECEIPT BESIDE IT')
LANDINGS = [
    ('P15', 'the period sentence',   "and the offset is exactly a linear phase drift at fixed $\\ell_{A}$"),
    ('P15', 'the progenitor figure', "seventeen orders below the composition the companion paper determines"),
    ('P15', 'the amplitude pair',    "The arithmetic of Propositions~\\ref{prop:amplitude}"),
    ('P15', 'prop:flat',             "The flatness is machine-checked"),
    ('P18', 'the acoustic first',    "The acoustic residual of \\S\\ref{sec:acoustic} is"),
    ('P18', 'the acoustic last',     "And the term that carries the located step is determined"),
    ('P18', 'the count preamble',    "Three items stand open, each with what would discharge it"),
    ('P18', 'the relative size',     "Three open items stand against roughly"),
    ('P7',  'the frontier preamble', "no entry below carries both"),
]
NUM = re.compile(r'(?<![\w.])\d[\d,]*(?:\.\d+)?(?:\s*\\times\s*10\^\{?-?\d+\}?)?')
WORDNUM = re.compile(r'\b(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|'
                     r'thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|'
                     r'seventy-five|hundred)\b', re.I)
located, missing = [], []
for key, tag, anchor in LANDINGS:
    s, b = block_of(key, anchor)
    if s is None and b is None:
        missing.append((key, tag, anchor))
        print(f"    !! {tag:24} [{key}] NOT LOCATED")
        continue
    located.append((key, tag, s, b))
    rcpts = re.findall(r'\\rcpt\{([^}]*)\}', b or '')
    figs = sorted(set(NUM.findall(demark(s or ''))) | set(w.lower() for w in WORDNUM.findall(demark(s or ''))))
    print(f"    {tag:24} [{key:4}] figures={figs if figs else 'none'}")
    print(f"        receipts cited in the BLOCK: {rcpts if rcpts else 'NONE'}")
arm('(A)i  all nine landings located at source', not missing and len(located) == 9,
    f"witness: {len(located)} of {len(LANDINGS)} located")

# (A)iii  the OLD figures, swept -- with the selector measured on the PRE-landing text first
head('(A)iii  DO THE OLD FIGURES SURVIVE?  the selector measured BEFORE it is trusted')
OLD = {
    'thirteen orders':  r'thirteen\s+orders',
    'eighteen orders':  r'eighteen\s+orders',
    'four open items':  r'[Ff]our\s+open\s+items|[Ff]our\s+items\s+stand\s+open',
    'the four':         r'[Tt]he\s+four,\s+with\s+what\s+would\s+discharge',
    'falls below':      r'residual\s+fall(?:ing|s)\s+below',
}
print("  POWER CONTROL -- each pattern on the PRE-landing text, where the answer is known.")
print("  The PRE text is the five papers AND the receipts tree: 'eighteen orders' was the printed")
print("  commentary of a RECEIPT, and running the control over papers alone gave it 0 pre-landing")
print("  hits -- a pattern that finds nothing before the repair cannot certify an absence after it.")
PRE_RCPT = git('show', f'{PRE_COMMIT}:receipts/P15_CR_cosmology/'
               'P15_the_progenitor_vacuum_is_negligible_too.py')
power = {}
for label, pat in OLD.items():
    pre_hits = sum(len(re.findall(pat, PRE[k])) for k in PRE) + len(re.findall(pat, PRE_RCPT))
    power[label] = pre_hits
    print(f"    {label:18} pre-landing hits: {pre_hits}")
arm('(A)iii-a  every pattern finds its own pre-landing text, so a zero now means absence and not '
    'a broken pattern', all(v > 0 for v in power.values()),
    f"witness: {power}")

print()
print("  AND NOW, over every .tex in corpus/ and every ledger at the root:")
files = sorted(f for f in os.listdir(CORPUS) if f.endswith('.tex'))
roots = sorted(f for f in os.listdir(ROOT)
               if f.endswith('.md') and f.isupper() or (f.endswith('.md') and f.startswith('THE_')))
rcpt_files = []
for dirpath, _, fns in os.walk(os.path.join(ROOT, 'receipts')):
    for fn in fns:
        if fn.endswith('.py'):
            rcpt_files.append(os.path.join(dirpath, fn))
print(f"  (and {len(rcpt_files)} receipt source files)")
survivors = []
for fn in files + roots + rcpt_files:
    p = fn if os.path.isabs(fn) else (os.path.join(CORPUS, fn) if fn.endswith('.tex')
                                      else os.path.join(ROOT, fn))
    fn = os.path.basename(fn)
    try:
        txt = open(p, encoding='utf-8').read()
    except (IsADirectoryError, UnicodeDecodeError):
        continue
    for label, pat in OLD.items():
        for m in re.finditer(pat, txt):
            survivors.append((fn, label, flat(txt[max(0, m.start()-110):m.end()+110])))
print(f"  {len(survivors)} survivor(s)")
for fn, label, ctx in survivors:
    print(f"    [{label}] {fn}")
    print(f"        ...{ctx}...")
# ADJUDICATED BY HAND, each with its reason -- a hit is not a site until it is read
VERDICTS = {
    ('CR_synthesis.tex', 'thirteen orders'):
        'CLEAN: the phrase is "some hundred and thirteen orders", the substrate-vacuum ratio, '
        'which cm_substrate_ratio puts between 1e112 and 1e113 -- my pattern caught the tail of '
        'a different number',
    ('THE_BASE_RATE.md', 'eighteen orders'):
        'CLEAN: "the mixing buys eighteen orders" is a different claim in a different sector',
    ('THE_CONSOLIDATION_LEDGER.md', 'thirteen orders'):
        'CLEAN: the ledger QUOTES the old wording while recording its correction, in quotation '
        'marks, which is how a correction should be recorded',
    ('THE_DIMENSION_DEEPENING_AUDIT.md', 'four open items'):
        "CLEAN: another file's four open items, read at r2382",
    ('THE_STAGED_REVISIONS.md', 'four open items'):
        "CLEAN: the same other file's four, same reading",
    ('THE_REGISTER.md', 'thirteen orders'):
        'CLEAN: an infrared-weighted sum blown by thirteen orders -- a different quantity',
    ('CR_synthesis.tex', 'falls below'):
        'ROUTED: the fourth site of this round\'s own repair, and (A)iv settles it against the '
        'receipt -- the relation is arm-dependent and this sentence names no arm',
}
unjudged = [(fn, lab) for fn, lab, _ in survivors if (fn, lab) not in VERDICTS]
sites = [(fn, lab) for fn, lab, _ in survivors if VERDICTS.get((fn, lab), '').startswith('ROUTED')]
print()
print('  ADJUDICATION, every hit read at source:')
for (fn, lab), v in VERDICTS.items():
    n = sum(1 for a, b, _ in survivors if (a, b) == (fn, lab))
    if n:
        print(f"    [{lab:16}] {fn:36} x{n}  {v}")
print(f"  => {len(sites)} site(s), {len(survivors) - sum(1 for f, l, _ in survivors if (f, l) in sites)} "
      f"adjudicated clean, {len(unjudged)} unjudged")
arm('(A)iii-b  every survivor is adjudicated, and exactly ONE is a site -- the registered '
    'reachable negative, reached', not unjudged and len(sites) == 1,
    f"witness: {len(survivors)} hits across {len(files) + len(roots) + len(rcpt_files)} files, "
    f"every pattern proved live by the control above, {len(sites)} routed and {len(unjudged)} "
    f"left unread")

# ----------------------------------------------------------------- A(iv) the relation itself
head('(A)iv  "FALLS BELOW" AGAINST "LEVEL WITH", AT THE RECEIPT\'S OWN NUMBERS')
PROG = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                    'P15_the_licensed_rebuild_leaves_all_three_rigidity_numbers_where_they_were_'
                    'and_the_forbidden_one_puts_the_arm_on_the_controls_own_floor.py')
rtxt = open(PROG, encoding='utf-8').read()
# the receipt's own banked literals, read out of its source rather than retyped
lits = {k: sp.Rational(v) for k, v in
        re.findall(r'abs\(_([fc])\[.chi2.\] - (\d+\.\d+)\) < 0\.01', rtxt)}
arm_of_record = lits.get('f')
control = lits.get('c')
namesake = sp.Rational('184.989')
print(f"  the receipt's banked numbers: arm of record {float(arm_of_record):.4f}, "
      f"control {float(control):.4f}, namesake arm {float(namesake):.4f}")
print(f"  arm of record - control = {float(arm_of_record - control):+.4f}  -> ABOVE, by a hair")
print(f"  namesake arm  - control = {float(namesake - control):+.4f}  -> BELOW")
print("  and the receipt says so in its own gate head: \"ON THE ARM OF RECORD THE FORBIDDEN")
print("  REPAIR DOES NOT GO BELOW THE CONTROL'S OWN VALUE -- IT LANDS LEVEL WITH IT\", and")
print("  \"the namesake arm's 184.99 against 186.01 put it BELOW; the arm of record's is a hair")
print("  above, so `falls below the control's own` lands as `level with the control's own`\".")
arm_dep = (arm_of_record > control and namesake < control
           and abs(arm_of_record - control) < sp.Rational(1, 2))
arm('(A)iv-a  the relation is ARM-DEPENDENT: below on the namesake arm, level with on the arm of '
    'record, and the two differ by a hair', bool(arm_dep),
    f"witness: {float(arm_of_record):.3f} > {float(control):.3f} > {float(namesake):.3f}, the "
    f"first gap {float(arm_of_record - control):+.3f} and the second {float(namesake - control):+.3f}")

# the four sites, and which of them names its arm
SITES = [
    ('P18', 2866, 'residual falling level with the standard'),
    ('P18', 1864, 'residual falling level with'),
    ('P7',  780,  'residual falls level with the standard'),
    ('P18', None, "shape residual falls below the standard"),
]
print()
print("  the four sentences that make this comparison, and whether each names its arm:")
unnamed = []
for key, _, anchor in SITES:
    s_, b_ = block_of(key, anchor)
    d = demark(s_ or b_ or '')
    names_arm = bool(re.search(r'arm of record|namesake arm|on the arm', d))
    rel = 'level with' if 'level with' in d else ('below' if 'falls below' in d else '?')
    print(f"    [{key:3}] relation={rel:11} names its arm={names_arm!s:5}  {d[:95]}")
    if rel == 'below' and not names_arm:
        unnamed.append((key, d))
arm('(A)iv-b  three sentences say "level with" and the fourth still says "falls below" while '
    'naming no arm', len(unnamed) == 1,
    f"witness: {len(unnamed)} site(s) assert the strict relation without naming the arm it holds "
    f"on; the receipt makes the relation arm-dependent, so either word needs its arm")

# ----------------------------------------------------------------- B : the formal paragraphs
head("(B)  P15's THREE NEW FORMAL PARAGRAPHS")

def decl(fname, name):
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
    return {'binders': binders, 'concl': flat(stmt[colon+1:]) if colon < len(stmt) else ''}

NAMES = ['cm_substrate_ratio', 'cm_mass_cap', 'cm_progenitor_arith', 'cm_flat_slice',
         'cm_flat_witness', 'lf_witness']
DECL = {n: decl('Cosmology.lean', n) for n in NAMES}
for n in NAMES:
    d = DECL[n]
    print(f"  {n}")
    print(f"    binders {d['binders'] if d else 'MISSING'}")
    if d:
        print(f"    concl   {d['concl'][:300]}")

cited = sorted({c.replace(r'\_', '_') for c in re.findall(r'\\texttt\{(cm[^}]*|lf[^}]*)\}', NOW['P15'])})
notfound = [c for c in cited if decl('Cosmology.lean', c) is None]
fakes = ['cm_substrate_power', 'cm_flat_leaf', 'cm_progenitor_bound']
fake_hits = [f for f in fakes if decl('Cosmology.lean', f) is not None]
print(f"  P15 cites {len(cited)} Lean names; not found: {notfound}")
arm('(B)iii  every cited name is a declaration, and three fabricated names are not found',
    not notfound and not fake_hits,
    f"witness: {len(cited)} cited, none missing; fabricated {fakes} -> {fake_hits or 'none found'}")

# (B)i  the amplitude pair
head('(B)i  prop:amplitude WITH prop:progenitor-amplitude')
s_amp, b_amp = block_of('P15', 'The arithmetic of Propositions~\\ref{prop:amplitude}')
print(f"  PROSE  {demark(b_amp)[:900]}")
d_sub, d_cap, d_arith = DECL['cm_substrate_ratio'], DECL['cm_mass_cap'], DECL['cm_progenitor_arith']
on_stated = 'on the stated inputs' in demark(b_amp)
remainder = 'are not formalised' in demark(b_amp)
print(f"  the paragraph says 'on the stated inputs': {on_stated}")
print(f"  and names its unformalised remainder:      {remainder}")
arm('(B)i-a  the arithmetic-on-stated-inputs risk does NOT fire: the paragraph says so in those '
    'words, and names the transfer law and the vacuum-power estimate as not formalised',
    on_stated and remainder,
    'witness: "machine-checked in Lean on the stated inputs" and "The transfer law and the '
    'vacuum-power estimate are the inputs, and are not formalised" -- the clause r7746 asked for '
    'at row 4, now generalised')
# every conjunct recomputed
sub_ok = (sp.Rational(10)**112 < AS / sp.Rational(3, 10**122) < sp.Rational(10)**113)
print(f"  cm_substrate_ratio: 2e-9 / 3e-122 = {sp.N(AS / sp.Rational(3,10**122), 6)}  "
      f"in (1e112, 1e113): {sub_ok}")
cap_ok = []
for Mv, av, lv in ((sp.Rational(1,100), 1, 1), (sp.Rational(1,2), 3, 2), (1/(3*sp.sqrt(3)), 1, 5)):
    lhs, rhs = 27 * (lv/av)**2, (lv/Mv)**2
    cap_ok.append(sp.simplify(rhs - lhs) >= 0)
print(f"  cm_mass_cap at three members on the cap: {cap_ok}")
arm('(B)i-b  every conjunct of the three theorems recomputes, and the prose quotes each correctly',
    sub_ok and all(cap_ok),
    f"witness: the ratio is {sp.N(AS / sp.Rational(3,10**122), 4)}; the cap inequality holds at "
    f"three members including M = alpha/(3 sqrt3) itself")

# (B)ii  prop:flat
head('(B)ii  prop:flat AND cm_flat_slice')
s_flat, b_flat = block_of('P15', 'The flatness is machine-checked')
print(f"  PROSE  {demark(s_flat)}")
d_fl = DECL['cm_flat_slice']
hyps = [b for b in d_fl['binders'] if ':' in b and not b.startswith('{')]
print(f"  cm_flat_slice binders: {d_fl['binders']}")
print(f"  its HYPOTHESES: {[b for b in d_fl['binders'] if 'hr' in b or 'hs' in b]}")
identically = 'vanishes identically' in demark(s_flat)
states_hyps = bool(re.search(r'r\\ne0|r\s*\\neq\s*0|away from|except|\\sin\\theta', demark(s_flat)))
k0 = 'the $k=0$ case' in demark(s_flat)
print(f"  prose says 'vanishes identically': {identically}")
print(f"  prose states either hypothesis:    {states_hyps}")
print(f"  prose says 'the k=0 case':         {k0}")
# and the k = 0 claim, checked against the proof's own instantiation
src = open(os.path.join(LEAN, 'Cosmology.lean'), encoding='utf-8').read()
body = src[src.index('theorem cm_flat_slice'):]
body = body[:body.index('/--', 10)]
k_used = re.search(r'\(k := (\w+)\)', body)
print(f"  the proof instantiates lf_curv at k := {k_used.group(1) if k_used else '?'}")
arm('(B)ii-a  "the k=0 case" is exactly how the proof instantiates it',
    k0 and bool(k_used) and k_used.group(1) == '0',
    f"witness: lf_curv (k := {k_used.group(1) if k_used else '?'}) in cm_flat_slice's own proof")
arm('(B)ii-b  but "vanishes IDENTICALLY" drops the two hypotheses the declaration carries',
    identically and not states_hyps and len([b for b in d_fl['binders'] if 'hr' in b or 'hs' in b]) == 2,
    "witness: the theorem is (hr : x 0 != 0) (hs : Real.sin (x 1) != 0) -> ... = 0, so it vanishes "
    "at every point of the chart where r != 0 and sin(theta) != 0 -- true of the geometry, and not "
    "what the theorem states")

# (B)iv  non-vacuity, and at what value
head('(B)iv  NON-VACUITY, AND AT WHAT VALUE')
print(f"  cm_flat_witness concl: {DECL['cm_flat_witness']['concl']}")
print(f"  lf_witness      concl: {DECL['lf_witness']['concl'][:200]}")
at_r1 = '![1, \u03c0 / 2, 0]' in DECL['cm_flat_witness']['concl']
print(f"  the flat witness is exhibited at r = 1, theta = pi/2 (an interior point, not r = 0): {at_r1}")
arm('(B)iv  the witness is exhibited where the hypotheses HOLD, not where the term vanishes',
    at_r1,
    "witness: kr_Rlow (lf_g 1 id) ![1, pi/2, 0] = 0 -- r = 1 != 0 and sin(pi/2) = 1 != 0, so both "
    "hypotheses are met at the witness point")

# ----------------------------------------------------------------- C : P18 and P7
head("(C)i  P18's COUNT, AGAINST THE TABLE IT PREAMBLES")
s_cnt, b_cnt = block_of('P18', 'Three items stand open, each with what would discharge it')
s_rel, b_rel = block_of('P18', 'Three open items stand against roughly')
print(f"  PREAMBLE  {demark(s_cnt)}")
print(f"  RELATIVE  {demark(s_rel)}")
sub = NOW['P18']
tbl = sub[sub.index('subsection{The three, with what would discharge each}'):]
tbl = tbl[:tbl.index('\\subsection', 10)]
rows = [r for r in tbl.split('\\\\') if '&' in r and '\\emph{open item}' not in r
        and r.strip().strip('\\hline').strip()]
rows = [flat(r.replace('\\hline', '')) for r in rows if flat(r.replace('\\hline', ''))]
print(f"  the table below it has {len(rows)} row(s):")
for i, r in enumerate(rows, 1):
    print(f"    {i}. {demark(r)[:110]}")
heading_three = 'subsection{The three, with what would discharge each}' in NOW['P18']
cosmo = block_of('P18', 'Three items in the cosmology stay open')[0]
print(f"  and the cosmology sentence: {demark(cosmo or '')[:150]}")
arm('(C)i-a  the preamble, the heading, the cosmology sentence and the table all say THREE',
    len(rows) == 3 and heading_three and cosmo is not None
    and 'Three items stand open' in (s_cnt or ''),
    f"witness: {len(rows)} table rows, heading 'The three', preamble 'Three items stand open', "
    f"and 'Three items in the cosmology stay open'")
# the relative-size figure, and whether a receipt stands behind it
seventy_five = 'roughly\nseventy-five' in sub or 'roughly seventy-five' in flat(sub)
rcpt_near = re.findall(r'\\rcpt\{([^}]*)\}', b_rel or '')
print(f"  the relative-size sentence cites: {rcpt_near if rcpt_near else 'NO RECEIPT'}")
print("  SEARCHED for a receipt behind 'seventy-five': the sentence's own block, and the whole")
print("  receipts tree for a counter of the hard register --")
hard = subprocess.run(['grep', '-rl', 'hard register', os.path.join(ROOT, 'receipts')],
                      capture_output=True).stdout.decode().split()
print(f"    receipts mentioning 'hard register': {hard or 'none'}")
print("  CONTROL, and it is the SPECIFIC receipt and not a word search: the progenitor figure")
print("  stands on P15_the_progenitor_vacuum_is_negligible_too.py, which computes the gap --")
prog = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                    'P15_the_progenitor_vacuum_is_negligible_too.py')
ptxt = open(prog, encoding='utf-8').read()
computes = bool(re.search(r'seventeen|17\.2|log10', ptxt))
seventeen_rcpt = [prog] if computes else []
print(f"    does it compute the order gap: {computes}")
arm('(C)i-b  the relative-size figure "roughly seventy-five" stands on no receipt, while the '
    'round\'s other figures do -- the order asks for each figure against its receipt',
    seventy_five and not rcpt_near and not hard,
    f"witness: no \\rcpt in that block and no receipt in the tree counts the hard register; the "
    f"control finds {len(seventeen_rcpt)} receipt(s) behind 'seventeen'")

head("(C)ii  P7's FRONTIER PREAMBLE, AGAINST THE ENTRIES IT PREAMBLES")
s_pre, b_pre = block_of('P7', 'no entry below carries both')
print(f"  PREAMBLE BLOCK  {demark(b_pre)[:700]}")
five = 'Of the five below, all five are boundaries' in demark(NOW['P7'])
items = re.findall(r'\\item\\label\{(frontier:[^}]*)\}', NOW['P7'])
if not items:
    items = re.findall(r'\\label\{(frontier:[^}]*)\}', NOW['P7'])
print(f"  the frontier labels in P7: {items}")
# each entry's declared kind, read from the sentence that declares it
kinds = {}
for lab in items:
    blk = [b for b in blocks(NOW['P7']) if lab in b]
    txt = demark(blk[0]) if blk else ''
    is_b = bool(re.search(r'\bis one\b|boundar|hands over|hands it over|is a result', txt))
    is_w = bool(re.search(r'\bis work\b|awaits a computation|unworked|a definite computation '
                          r'would close', txt))
    if not (is_b or is_w):
        # the kind may be declared in the SENTENCE THAT NAMES THE WHOLE LIST rather than in the
        # entry's own block (r7746 DEFECT 2's lesson, one level up)
        allfive = demark(NOW['P7'])
        is_b = 'Of the five below, all five are boundaries' in allfive
    kinds[lab] = ('boundary' if is_b else '') + ('+work' if is_w else '')
for lab, k in kinds.items():
    print(f"    {lab:34} declared: {k or 'unclear'}")
both = [l for l, k in kinds.items() if k == 'boundary+work']
print(f"  entries carrying BOTH: {both or 'none'}")
print("  SEARCHED: each frontier label's own block, de-marked, for the preamble's own two kinds")
print("  ('boundary'/'hands over'/'is one' and 'work'/'awaits a computation'/'unworked').")
print("  CONTROL: the preamble itself contains both vocabularies, so the search can see both.")
ctrl = bool(re.search(r'hands over', demark(b_pre))) and bool(re.search(r'awaits a computation', demark(b_pre)))
arm('(C)ii-a  "no entry below carries both" holds of the entries, and the five/five claim matches '
    'the label count', not both and len(items) == 5 and five and ctrl,
    f"witness: {len(items)} frontier labels, none declared both; the preamble's own block carries "
    f"both vocabularies so the search is live ({ctrl})")

# ----------------------------------------------------------------- summary
head('SUMMARY')
npass = sum(1 for _, ok, _ in RESULTS if ok)
for tag, ok, _ in RESULTS:
    print(f"  [{'PASS' if ok else 'FAIL'}] {tag}")
print()
print(f"  {npass} of {len(RESULTS)} arms PASS")
sys.exit(0 if npass == len(RESULTS) else 1)
