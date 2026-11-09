#!/usr/bin/env python3
"""r7722 (60) -- P3's first formal landing and the CORRECTED prop:involution, read cold.

Arms registered in PREDICTION.md before anything in P3 was read -- before
prop:involution, its proof, the remark, the formal paragraph, and before sigma's
own definition -- and before any sl_ declaration.  The readers of r7714,
r7716 and r7718 are carried forward unchanged and re-tested on their negatives.  The readers r7714 repaired are carried forward unchanged
and re-tested on their negatives before use.  Every verdict below is BUILT FROM its readings; nothing
is asserted that is not printed first.

GUARDS.  G1 one predicate per conjunct.  G2 three anchor forms only -- a prose
marker must be plain prose, an escaped control sequence with ONE leading
backslash, or an escaped math delimiter; anything else is REFUSED before use.
G3 the flip family, striking EVERY copy.  G4 classifier probes tested on BOTH
classes before use.  G5 reader probes with negatives.  G6 every prose probe runs
on a WHITESPACE-FLATTENED copy, since the source wraps mid-sentence.
"""
import math
import re
import sys

ROOT = '/home/user/shadow-of-existence'
P2 = ROOT + '/corpus/janzen_circle_v3.tex'
LEAN = ROOT + '/computations/formalisation/lean/probes/SlicingCubic.lean'
P3 = ROOT + '/corpus/SdS-slicing-curve_v2.tex'

FAIL = []
def say(*a):
    print(*a)
def need(label, ok):
    say(('   ok  ' if ok else '  FAIL ') + label)
    if not ok:
        FAIL.append(label)
    return ok

def flat(s):
    """G6: one line, single spaces."""
    return re.sub(r'\s+', ' ', s)

# ---------------------------------------------------------------- G2 anchors
def anchor(marker):
    """G2: a marker is usable only in one of the three anchored forms."""
    if re.fullmatch(r'[A-Za-z0-9 ,.;:\'\-()]+', marker):
        return 'prose'
    if re.fullmatch(r'\\[A-Za-z]+(\{[^{}]*\})?', marker):
        return 'macro'
    if re.fullmatch(r'\$[^$]+\$', marker):
        return 'math'
    return None

def anchored(marker):
    kind = anchor(marker)
    if kind is None:
        say(f'  G2 REFUSED (unanchored marker): {marker!r}')
        FAIL.append('G2 refused a marker: ' + marker)
        return False
    return True

# -------------------------------------------- the name-skeleton matcher (r7712)
GREEK = {'Φ': 'Phi', 'Ψ': 'Psi', 'η': 'eta', 'ρ': 'rho', 'τ': 'tau',
         'Γ': 'Gamma', 'σ': 'sigma', 'φ': 'varphi', 'θ': 'theta'}

def cited_in_tex(tex, name):
    """A NAME IS A FORM (negative probe 19).  P2 prints Greek letters in MATH
    MODE inside \\texttt, so the literal character is not what is on the page.
    Match the name's SKELETON: each ASCII run in order, each Greek letter as the
    character, as $\\X$, as \\X, or as X."""
    parts = []
    for ch in name:
        if ch in GREEK:
            g = GREEK[ch]
            parts.append('(?:' + re.escape(ch) + r'|\$\\' + g + r'\$|\\' + g + '|' + g + ')')
        elif ch == '_':
            parts.append(r'\\?_')
        else:
            parts.append(re.escape(ch))
    return re.search(''.join(parts), tex) is not None

def decl_header(src, name):
    """The header of a declaration: from its keyword to the ':=' or 'by' that
    begins its proof.  Binders are read from the HEADER ONLY, so casts in the
    body are never reported as hypotheses (r7706)."""
    m = re.search(r'^(?:theorem|lemma|def|abbrev|noncomputable def)\s+' + re.escape(name)
                  + r'\b', src, re.M)
    if not m:
        return None
    tail = src[m.start():]
    cut = len(tail)
    for pat in (r'\s:=\s', r'\sby\s*$', r'\sby\s'):
        mm = re.search(pat, tail, re.M)
        if mm and mm.start() < cut:
            cut = mm.start()
    return flat(tail[:cut])

def decl_extent(src, name):
    """A declaration's WHOLE text, bounded by where the NEXT declaration begins
    (the r7708 lesson).  decl_header stops at ':=' so that binders are read from
    the header only; a `def`'s CONTENT lives after ':=' and needs this."""
    m = re.search(r'^(?:theorem|lemma|def|abbrev|noncomputable def)\s+' + re.escape(name)
                  + r'\b', src, re.M)
    if not m:
        return None
    tail = src[m.start():]
    nxt = re.search(r'\n(?:/--|@\[|theorem|lemma|def|abbrev|noncomputable|variable|include|end)\s',
                    tail[1:])
    return flat(tail[:nxt.start() + 1] if nxt else tail)

def decl_statement(src, name):
    """A declaration's header THROUGH ITS WHOLE STATEMENT, bounded by the
    ':= by' that begins its proof.  decl_header cuts at the FIRST ' := ',
    which is right for binders and wrong for any statement containing a Lean
    `let` binder: `let u := (r + r0) / sqrt 2` carries ' := ' itself, so the
    header stopped there and the rest of the statement was invisible.  That
    was this probe's own second defect, the same family as r7720's ') :'
    split -- a literal delimiter that also occurs inside what it delimits."""
    ext = decl_extent(src, name)
    if ext is None:
        return None
    for pat in (' := by', ':= by'):
        k = ext.find(pat)
        if k > 0:
            return ext[:k].strip()
    return decl_header(src, name)


def binders(header):
    """Bracket-depth matching, so a binder whose TYPE carries parentheses is not
    invisible (r7706)."""
    out, i = [], 0
    while i < len(header):
        if header[i] in '({[':
            close = {'(': ')', '{': '}', '[': ']'}[header[i]]
            depth, j = 0, i
            while j < len(header):
                if header[j] in '({[':
                    depth += 1
                elif header[j] in ')}]':
                    depth -= 1
                    if depth == 0:
                        break
                j += 1
            if j < len(header) and header[j] == close:
                out.append(header[i:j + 1])
            i = j + 1
        elif header[i] == ':':
            break
        else:
            i += 1
    return out


# ------------------------------------------- the classifier this revision needs
# An inference is a PAIR: (subject, conclusion).  Two inferences are the SAME
# only when BOTH match.  The Kretschmann scalar appearing on both sides of this
# order's question proves nothing either way, which is why the pair is the unit.
INFERENCE_SUBJECTS = {
    'curve': ('curve', 'continuation', 'construction'),
    'metric-on-chart': ('metric', 'chart', 'scalar'),
    'spacetime': ('spacetime', 'manifold', 'abstract'),
}


def subject_of(text):
    """Which subject an inference is about, by the nouns its own sentence uses."""
    t = flat(text).lower()
    hits = {k: sum(t.count(w) for w in ws) for k, ws in INFERENCE_SUBJECTS.items()}
    best = max(hits, key=lambda k: hits[k])
    return best if hits[best] else 'unknown'


def bounds_subject(clause):
    """In a clause of the form "this bounds A and not B" the SUBJECT of the
    bounding is A, and a word count over the whole clause cannot find it: both
    are named, and that is the point of the construction.  Read the noun phrase
    the verb takes.  Counting instead was this probe's own second defect."""
    m = re.search(r'\bbounds\s+(.*?)(?:\s+and not\b|:|$)', flat(clause), re.I)
    return subject_of(m.group(1)) if m else 'unknown'


def same_inference(a, b):
    """a, b are (subject, conclusion) pairs.  The same only when BOTH match."""
    return a[0] == b[0] and a[1] == b[1]


def states_about_metrics(header):
    """Does a declaration's conclusion QUANTIFY OVER METRICS, or over a
    real-valued function?  Read by the SHAPE of the conclusion -- the r7714
    lesson -- because the prose's step from one to the other is the question."""
    concl = header.rsplit(') :', 1)[-1] if ') :' in header else header
    over_fn = re.search(r'∃\s*G\s*:\s*P\s*→\s*ℝ', concl)
    metric_obj = re.search(r'MSpacetime|[.]gW|[.]g\b|\bmetric\b', concl)
    regularity = re.search(r'ContDiff', concl)
    if over_fn and not metric_obj:
        return 'a real-valued function'
    if metric_obj:
        return 'a metric'
    if regularity:
        return 'the regularity of some other map'
    return 'neither'

# ------------------------------------------- the readers this revision needs
def regularity_implies(stronger, weaker):
    """Does inextendibility at CLASS `stronger` imply it at CLASS `weaker`?
    Read as a CONTAINMENT and not as a word: every `weaker`-regular metric is
    `stronger`-regular (C2 metrics are in particular C0), so ruling out every
    `stronger` extension rules out every `weaker` one.  'Stronger' is exactly
    the kind of word that gets inverted, so the direction is computed."""
    order = {'C0': 0, 'C1': 1, 'C2': 2, 'Cinf': 99}
    if stronger not in order or weaker not in order:
        return 'unknown'
    # a class LOWER in the order is a WEAKER regularity demand and so a WIDER
    # family of extensions: ruling those out is the stronger statement.
    return 'implies' if order[stronger] <= order[weaker] else 'does not imply'


def conclusion_of(header):
    """A declaration's conclusion: the text after the colon at BRACKET DEPTH
    ZERO, found by depth and not by a literal delimiter.  Splitting on the last
    ") :" was this probe's own first defect: a conclusion carrying nested type
    ascriptions, such as ((x : R) : C), contains ") :" itself, so the split
    landed inside a cast and threw four conjuncts away."""
    depth = 0
    for k, ch in enumerate(header):
        if ch in '({[':
            depth += 1
        elif ch in ')}]':
            depth -= 1
        elif ch == ':' and depth == 0:
            return header[k + 1:].strip()
    return header


def conjuncts(header):
    """A conclusion's top-level conjuncts, split on the logical AND."""
    concl = conclusion_of(header)
    return [c.strip() for c in concl.split('∧') if c.strip()]


def kind_of(conjunct):
    """An EQUATION and an INEQUALITY are different conjuncts.  Registered as a
    guard for this revision, because the sentence under test claims one of
    each and a declaration can carry the first without the second."""
    c = conjunct
    if re.search(r'≤|≥|<|>', c):
        return 'inequality'
    if '=' in c:
        return 'equation'
    return 'other'

# ----------------------------------------------- the arithmetic this revision needs
# THE NEW GUARD: every numerical claim is computed at the NAMED endpoints and the
# computation is PRINTED beside the verdict, so a reader can check it rather than
# trust it.  sigma is taken from ITS OWN DEFINITION in P3, not from the order.
S3 = math.sqrt(3.0)
ENDPOINTS = {'-1/sqrt3': -1.0 / S3, '0': 0.0, '1/sqrt3': 1.0 / S3,
             '1': 1.0, '2/sqrt3': 2.0 / S3}


# The equation this is read from is labelled `eq:involution` in P3.  ⌗ r7722: the label is a
# POINTER and is kept in a comment rather than in the docstring, because a corpus-wide detector
# under `computations/` reads a top-level def's docstring as a declaration of its KIND, and this
# function is an involution of an interval and not a Cartan involution of an algebra.
def sigma(x):
    """sigma(r0) = (-r0 + sqrt(4 - 3 r0^2)) / 2, the map P3 corrects."""
    return (-x + math.sqrt(max(0.0, 4.0 - 3.0 * x * x))) / 2.0


def twoM(x):
    """2M = r0 - r0^3, which is what says r0 is a root of the horizon cubic."""
    return x - x ** 3


def cubic(m, r):
    """The horizon cubic r^3 - r + 2M."""
    return r ** 3 - r + m


def close(a, b, tol=1e-12):
    return abs(a - b) <= tol

# =============================================================== SELF-TESTS
def selftests(p3flat):
    say('=' * 78)
    say('SELF-TESTS -- every classifier, reader and computation on BOTH of its classes')
    say('=' * 78)
    need('G2 accepts plain prose', anchor('is an involution of') == 'prose')
    need('G2 accepts an escaped control sequence', anchor(r'\sigma') == 'macro')
    need('G2 accepts an escaped math delimiter', anchor('$[0,1]$') == 'math')
    need('G2 REFUSES a marker mixing prose with math', anchor(r'the half $2M\ge0$') is None)

    need('skeleton: a plain ASCII name IS found',
         cited_in_tex(r'(\texttt{sl\_ellipse})', 'sl_ellipse'))
    need('skeleton: a math-mode Greek name IS found -- P3 prints sl\\_$\\sigma$\\_$\\sigma$',
         cited_in_tex(r'(\texttt{sl\_$\sigma$\_$\sigma$})', 'sl_σ_σ'))
    need('skeleton: a name NOT on the page is NOT found',
         not cited_in_tex(r'(\texttt{sl\_ellipse})', 'sl_nowhere'))

    need('reader: sl_nariai has a header', decl_header(LEANSRC, 'sl_nariai') is not None)
    need('reader: a declaration that does not exist reads as absent',
         decl_header(LEANSRC, 'sl_nariai_not_a_declaration') is None)
    need('reader: decl_extent reaches a def\'s BODY, which lives after ":="',
         'Real.sqrt (4 - 3 * x ^ 2)' in (decl_extent(LEANSRC, 'sl_σ') or ''))
    need('reader: the conclusion is found at BRACKET DEPTH ZERO (the r7720 fix), so a '
         'nested ascription does not cut it short',
         conclusion_of('theorem t (M : ℝ) : a = ((b : ℝ) : ℂ) ∧ c = 1')
         == 'a = ((b : ℝ) : ℂ) ∧ c = 1')
    need('reader: a header with no depth-zero colon returns itself',
         conclusion_of('(M : ℝ)') == '(M : ℝ)')
    need('statement reader: a statement containing a Lean `let` binder is NOT '
         'truncated at the let\'s own ":=" -- this probe\'s own second defect',
         'Real.sqrt (2 / 3)' in (decl_statement(LEANSRC, 'sl_ellipse') or ''))
    need('statement reader: and it still stops before the proof',
         'intro u v' not in (decl_statement(LEANSRC, 'sl_ellipse') or ''))
    need('statement reader: a declaration that does not exist is absent',
         decl_statement(LEANSRC, 'sl_ellipse_not_a_declaration') is None)
    need('conjunct reader: an equation reads as an equation', kind_of('a = b') == 'equation')
    need('conjunct reader: an inequality reads as an inequality', kind_of('a ≤ b') == 'inequality')

    say('')
    say('  THE ARITHMETIC, tested against values computed by hand before it was used:')
    need('sigma(0) = 1', close(sigma(0.0), 1.0))
    need('sigma(1) = 0', close(sigma(1.0), 0.0))
    need('and the reader is NOT vacuous: sigma(0) is not 0', not close(sigma(0.0), 0.0))
    need('2M at r0 = 1 is 0, and at r0 = 1/2 is 3/8 -- both by hand',
         close(twoM(1.0), 0.0) and close(twoM(0.5), 0.375))
    need('the cubic at r0 = 1 has 0 as a root, and 1/2 is not a root of it',
         close(cubic(twoM(1.0), 0.0), 0.0) and not close(cubic(twoM(1.0), 0.5), 0.0))

    need('G6: prop:involution is one line only after flattening',
         'is an involution of $[-1/\\sqrt{3},2/\\sqrt{3}]$' in p3flat)
    say('')


# ==================================================================== ARMS
def q1_truth(p3flat):
    say('=' * 78)
    say('Q1 -- IS THE CORRECTED prop:involution TRUE AS STATED?')
    say('      Every conjunct computed at the endpoints the statement itself names,')
    say('      with sigma read from ITS OWN DEFINITION and the computation PRINTED.')
    say('=' * 78)
    need('sigma\'s definition is at source, verbatim',
         '\\sigma(r_{0})=\\frac{-r_{0}+\\sqrt{4-3r_{0}^{2}}}{2}' in p3flat)
    say('    sigma(r0) = (-r0 + sqrt(4 - 3 r0^2)) / 2')
    say('')
    say('    THE VALUES, computed:')
    for lab, x in ENDPOINTS.items():
        say(f'      sigma({lab:9s}) = {sigma(x):+.12f}   [2M = {twoM(x):+.12f}]')

    say('')
    say('  (1a) THE INVOLUTION IDENTITY on [-1/sqrt3, 2/sqrt3]:')
    xs = [-1.0 / S3 + k * (2.0 / S3 + 1.0 / S3) / 40.0 for k in range(41)]
    worst = max(abs(sigma(sigma(x)) - x) for x in xs)
    say(f'      sup |sigma(sigma(x)) - x| over 41 points of the interval = {worst:.3e}')
    wx = max(xs, key=lambda x: abs(sigma(sigma(x)) - x))
    # THE SENSITIVE POINT IS THE ONE WHOSE IMAGE IS 2/sqrt3, i.e. x = -1/sqrt3,
    # not 2/sqrt3 itself: sigma(-1/sqrt3) = 2/sqrt3, and the OUTER sigma then
    # takes the root of a quantity that is zero to floating point.  Excluding
    # the wrong endpoint was this probe's own third defect, and the arm caught
    # it only because it PRINTS where the worst error is attained.
    inner = [x for x in xs if abs(x + 1.0 / S3) > 0.02]
    worst_in = max(abs(sigma(sigma(x)) - x) for x in inner)
    say(f'      attained at x = {wx:+.9f}; away from x = -1/sqrt3 (the point whose image is 2/sqrt3): {worst_in:.3e}')
    say('      ⌂ A TOLERANCE IS PART OF THE INSTRUMENT (negative probe 18).  At')
    say('        x = -1/sqrt3 the image is 2/sqrt3, where the inner square root')
    say('        VANISHES, so the OUTER sigma takes the root of a quantity that is')
    say('        zero to floating point, and the error there is of order the root of')
    say('        machine epsilon.  That is arithmetic and not mathematics, which the')
    say('        second figure shows: at full precision away from that ONE point.')
    need('sigma(sigma(x)) = x across the stated interval, to the tolerance the square '
         'root at the endpoint allows', worst < 1e-7)
    need('and away from that endpoint it holds to full precision, so the endpoint '
         'figure is the square root and not a defect in the claim', worst_in < 1e-13)
    # and it FAILS below the stated left endpoint, which is what makes the interval right.
    below = [-2.0 / S3 + k * (2.0 / S3 - 1.0 / S3) / 20.0 for k in range(20)]
    bad = max(abs(sigma(sigma(x)) - x) for x in below)
    say(f'      and BELOW it, on [-2/sqrt3, -1/sqrt3): sup |sigma(sigma(x)) - x| = {bad:.3e}')
    need('the identity FAILS below -1/sqrt3, so the stated left endpoint is not arbitrary '
         '-- the interval is exactly where it holds, not merely a subset of it', bad > 1e-3)

    say('')
    say('  (1b) THE EXCHANGE of [0, 2/sqrt3] with [-1/sqrt3, 1] -- the arm I registered as')
    say('       the subtle one, because the two intervals OVERLAP on [0, 1]:')
    say(f'      sigma(0) = {sigma(0.0):+.9f} = 1 (the right end of the second interval)')
    say(f'      sigma(2/sqrt3) = {sigma(2.0/S3):+.9f} = -1/sqrt3 = {-1.0/S3:+.9f} (its left end)')
    need('sigma carries the endpoints of the first interval to the endpoints of the second, '
         'in reverse order', close(sigma(0.0), 1.0) and close(sigma(2.0 / S3), -1.0 / S3))
    img = [sigma(k * (2.0 / S3) / 200.0) for k in range(201)]
    say(f'      and the image of [0, 2/sqrt3], sampled: [{min(img):+.9f}, {max(img):+.9f}]')
    need('so the image is [-1/sqrt3, 1] and the overlap is no obstacle: an involution may '
         'swap two overlapping sets whose union is its domain',
         close(min(img), -1.0 / S3, 1e-6) and close(max(img), 1.0, 1e-6))
    need('⚑ AND THE OLD STATEMENT\'S ERROR IS EXHIBITED, not just asserted: sigma(2/sqrt3) '
         'is NEGATIVE, so sigma is not a self-map of [0, 2/sqrt3]', sigma(2.0 / S3) < 0)

    say('')
    say('  (1c) ON [0, 1]: decreasing, ONTO [0, 1], to the OTHER non-negative root:')
    xs01 = [k / 200.0 for k in range(201)]
    vals = [sigma(x) for x in xs01]
    need('decreasing on [0, 1]', all(vals[k] > vals[k + 1] - 1e-15 for k in range(200)))
    say(f'      image of [0, 1], sampled: [{min(vals):+.9f}, {max(vals):+.9f}]')
    need('and onto [0, 1]', close(min(vals), 0.0, 1e-9) and close(max(vals), 1.0, 1e-9))
    say('      AND THAT sigma(r0) IS A ROOT OF r0\'s OWN CUBIC, computed at each endpoint:')
    for lab in ('0', '1/sqrt3', '1'):
        x = ENDPOINTS[lab]
        say(f'        r0 = {lab:9s}: cubic(2M(r0), sigma(r0)) = '
            f'{cubic(twoM(x), sigma(x)):+.3e};  sigma(r0) = {sigma(x):+.9f} >= 0')
    need('sigma(r0) is a root of r0\'s cubic at every sampled point of [0, 1], and is '
         'non-negative there',
         all(abs(cubic(twoM(x), sigma(x))) < 1e-9 and sigma(x) >= -1e-12 for x in xs01))
    need('"the OTHER non-negative root" is exact at the two ends -- sigma(0) = 1 and '
         'sigma(1) = 0, each the cubic\'s other non-negative root (both cubics are '
         'r^3 - r, with roots -1, 0, 1)',
         close(twoM(0.0), 0.0) and close(twoM(1.0), 0.0)
         and close(sigma(0.0), 1.0) and close(sigma(1.0), 0.0))
    need('and at the fixed point 1/sqrt3 the "other" root is itself, which is why the '
         'statement calls it the designated root on the merged pair',
         close(sigma(1.0 / S3), 1.0 / S3, 1e-9))
    return True


def q1_dependents(p3flat):
    say('')
    say('=' * 78)
    say('Q1d -- DOES ANYTHING ELSE LEAN ON THE OLD READING?  A NAMED SEARCH, named.')
    say('=' * 78)
    import glob
    texs = sorted(glob.glob(ROOT + '/corpus/*.tex'))
    say(f'    SEARCHED: all {len(texs)} files of corpus/*.tex, flattened.')
    say('    STRINGS: "involution of", "positive-root half", and every occurrence of')
    say('             "2/\\sqrt3" or "2/\\sqrt{3}" within 300 characters of "involution"')
    say('             or "\\sigma".')
    hits_io, hits_prh, hits_near = [], [], []
    for f in texs:
        t = flat(open(f).read())
        name = f.split('/')[-1]
        for m in re.finditer(r'involution of [^,.;:]{0,40}', t):
            hits_io.append((name, m.group(0)))
        for m in re.finditer(r'positive-root half[^,.;:]{0,40}', t):
            hits_prh.append((name, m.group(0)))
        for m in re.finditer(r'2/\\sqrt\{?3\}?', t):
            seg = t[max(0, m.start() - 300):m.start() + 300]
            if 'involution' in seg or '\\sigma' in seg:
                hits_near.append(name)
    say('')
    say('    "involution of":')
    for n, h in hits_io:
        say(f'      {n}: {h}')
    need('the only "involution of <interval>" in the corpus is the CORRECTED one, and the '
         'only other hit is an unrelated "involution of order two"',
         any('[-1/\\sqrt{3}' in h for _, h in hits_io)
         and not any('involution of $[0,' in h for _, h in hits_io))
    say('')
    say('    "positive-root half":')
    for n, h in hits_prh:
        say(f'      {n}: {h}')
    need('P3\'s own remark now says the half is $r_{0}\\in[0,1]$',
         'positive-root half ($r_{0}\\in[0,1]$, $2M\\ge0$)' in p3flat)
    say('    ⌗ AND THE TWO RECEIPT-INDEX LINES THAT STILL SAY "on positive-root half" ARE')
    say('      NOT STALE, which is where a pattern match would have produced a FALSE')
    say('      finding.  The involution IDENTITY holds pointwise wherever 3r0 + s >= 0,')
    say('      which is automatic for r0 >= 0, so it holds on ALL of [0, 2/sqrt3]:')
    allpos = max(abs(sigma(sigma(k * (2.0 / S3) / 100.0)) - k * (2.0 / S3) / 100.0)
                 for k in range(101))
    say(f'        sup |sigma(sigma(x)) - x| over [0, 2/sqrt3] = {allpos:.3e}')
    need('the identity holds on the whole of [0, 2/sqrt3], so a claim that it holds "on '
         'the positive-root half" is TRUE under either reading of that phrase -- what the '
         'old statement got wrong was the SET sigma preserves, not the identity',
         allpos < 1e-9)
    rcpt = ROOT + '/receipts/P03_SdS_slicing/P03_cubic_factor_ellipse_locus.py'
    src = open(rcpt).read()
    m = re.search(r'sigma o sigma = id on the positive-root half[^\n]*', src)
    say(f'      and the receipt itself sweeps: {m.group(0)[:120] if m else "NOT FOUND"}')
    need('and the receipt that line is generated from sweeps r0 in [0, 1], the CORRECTED '
         'interval, so its own assertion is exact',
         m is not None and 'np.linspace(0,1,21)' in m.group(0))
    say('')
    say(f'    files with "2/sqrt3" near sigma or the involution: {sorted(set(hits_near))}')
    need('every such mention is in P3\'s corrected statements or in the groupoid paper, '
         'which states sigma(-1/sqrt3) = 2/sqrt3 and that -1/sqrt3 is NOT a fixed point '
         '-- consistent with the correction, not with the old reading',
         set(hits_near) <= {'SdS-slicing-curve_v2.tex', 'groupoid_paper.tex'}
         and 'so $-1/\\sqrt3$ is \\emph{not} a fixed point of the involution'
         in flat(open(ROOT + '/corpus/groupoid_paper.tex').read()))
    return True


def q2(p3flat, lean):
    say('')
    say('=' * 78)
    say('Q2 -- ARE THE SEMI-AXES WHAT sl_ellipse STATES, OR A CONSEQUENCE?')
    say('=' * 78)
    claim = ("the conic's semi-axes $\\sqrt{2/3}$ along $r=r_{0}$ and $\\sqrt2$ along "
             "$r=-r_{0}$ (\\texttt{sl\\_locus} and \\texttt{sl\\_ellipse})")
    need('the claim is at source, verbatim', claim in p3flat)
    h = decl_statement(lean, 'sl_ellipse')
    say(f'    sl_ellipse: {h}')
    cs = conjuncts(h or '')
    say(f'    READING -- {len(cs)} top-level conjuncts:')
    for c in cs:
        say(f'      [{kind_of(c)}] {c}')
    need('BOTH numbers are in the conclusion, each paired with its eigenvalue: '
         '3/2 times sqrt(2/3)^2 = 1 and 1/2 times sqrt2^2 = 1',
         '3 / 2 * Real.sqrt (2 / 3) ^ 2 = 1' in (h or '')
         and '1 / 2 * Real.sqrt 2 ^ 2 = 1' in (h or ''))
    need('and the DIRECTIONS are carried by the statement\'s own bindings, u = (r+r0)/sqrt2 '
         'and v = (r-r0)/sqrt2, so v = 0 is the line r = r0 and u = 0 is r = -r0',
         'let u := (r + r₀) / Real.sqrt 2' in (h or '')
         and 'let v := (r - r₀) / Real.sqrt 2' in (h or ''))
    need('and the diagonalisation that makes them semi-axes is stated too',
         'r ^ 2 + r * r₀ + r₀ ^ 2 = 3 / 2 * u ^ 2 + 1 / 2 * v ^ 2' in (h or ''))
    say('    ⌗ READING: the eigenvalue 3/2 goes with u, whose axis is v = 0, i.e. r = r0,')
    say('      and 3/2 * (2/3) = 1, so sqrt(2/3) is the semi-axis THERE; the eigenvalue 1/2')
    say('      goes with v, whose axis is u = 0, i.e. r = -r0, and 1/2 * 2 = 1.  Computed:')
    say(f'        3/2 * sqrt(2/3)^2 = {1.5 * (2.0/3.0):.12f};  1/2 * sqrt(2)^2 = '
        f'{0.5 * 2.0:.12f}')
    need('the assignment of each number to each direction is therefore RIGHT, and not '
         'swapped -- which is the one way this sentence could have failed',
         close(1.5 * (2.0 / 3.0), 1.0) and close(0.5 * 2.0, 1.0))
    loc = decl_statement(lean, 'sl_locus')
    say(f'    sl_locus: {loc}')
    need('and the level set that makes them semi-axes -- the quadratic factor vanishing, '
         'i.e. the conic -- is the OTHER cited declaration, which is why the clause cites '
         'both', loc is not None and 'r₀' in loc)
    say('    ⌗ So the semi-axes are STATED between the two declarations the clause cites:')
    say('      neither alone gives them, and the sentence cites both.  Not a consequence')
    say('      smuggled past a citation.')
    return True


def q3(p3flat, lean):
    say('')
    say('=' * 78)
    say('Q3 -- DOES "where the cubic is $(r-r_{0})^{2}(r+2r_{0})$" MATCH sl_nariai?')
    say('=' * 78)
    claim = ('the two components meeting exactly at $r=r_{0}=\\pm1/\\sqrt3$, where the cubic '
             'is $(r-r_{0})^{2}(r+2r_{0})$ (\\texttt{sl\\_nariai})')
    need('the claim is at source, verbatim', claim in p3flat)
    h = decl_statement(lean, 'sl_nariai')
    say(f'    sl_nariai: {h}')
    need('the FACTORISATION is a conjunct of sl_nariai, stated for every a with 3a^2 = 1',
         'sl_cubic (sl_g a) r = (r - a) ^ 2 * (r + 2 * a)' in (h or ''))
    need('and "meeting EXACTLY at" is an IFF in the statement, not an inclusion -- the word '
         'was read and not granted', '↔' in (h or ''))
    need('and both values are certified to satisfy the hypothesis, so "$\\pm1/\\sqrt3$" is '
         'the hypothesis\'s own solution set',
         '3 * (1 / Real.sqrt 3) ^ 2 = 1' in (h or '')
         and '3 * (-(1 / Real.sqrt 3)) ^ 2 = 1' in (h or ''))
    say('    AND THE FACTORISATION CHECKED BY ARITHMETIC at both values, independently:')
    for lab, a in (('+1/sqrt3', 1.0 / S3), ('-1/sqrt3', -1.0 / S3)):
        rs = [-2.0 + k * 0.17 for k in range(24)]
        worst = max(abs(cubic(twoM(a), r) - (r - a) ** 2 * (r + 2 * a)) for r in rs)
        say(f'      a = {lab}: sup over 24 values of r of '
            f'|cubic(2M(a), r) - (r-a)^2 (r+2a)| = {worst:.3e}')
        need(f'the factorisation holds identically in r at a = {lab}', worst < 1e-12)
    need('and it FAILS at a value not satisfying 3a^2 = 1, so the hypothesis is doing work',
         abs(cubic(twoM(0.5), 1.3) - (1.3 - 0.5) ** 2 * (1.3 + 1.0)) > 1e-3)
    return True


def item4(p3flat, p2flat, lean):
    say('')
    say('=' * 78)
    say('ITEM 4 -- THE REST OF THE LANDING')
    say('=' * 78)
    say('  4a THE PROOF\'S BRANCH CONDITION, and "EXACTLY ON" read as an IFF:')
    need('the proof says the condition holds "exactly on" the interval, verbatim',
         'so exactly on $[-1/\\sqrt3,2/\\sqrt3]$' in p3flat)
    say('      computed: 3r0 + s >= 0, with s = sqrt(4 - 3 r0^2)')
    for lab, x in ENDPOINTS.items():
        s = math.sqrt(max(0.0, 4.0 - 3.0 * x * x))
        say(f'        r0 = {lab:9s}: 3r0 + s = {3.0 * x + s:+.9f}')
    outside = -2.0 / S3 + 0.05
    s_out = math.sqrt(max(0.0, 4.0 - 3.0 * outside * outside))
    say(f'        r0 = {outside:+.4f} (below -1/sqrt3): 3r0 + s = {3.0 * outside + s_out:+.9f}')
    need('the condition holds at every named endpoint of the stated interval and FAILS '
         'below its left end, so "exactly on" is an iff and is true',
         all(3.0 * x + math.sqrt(max(0.0, 4.0 - 3.0 * x * x)) >= -1e-12
             for x in ENDPOINTS.values())
         and 3.0 * outside + s_out < 0)
    need('and the monotonicity the proof adds is at source, verbatim',
         "$\\sigma'(r_{0})=-(3r_{0}+s)/(2s)$" in p3flat)

    say('')
    say('  4b THE REMARK\'S NARROWED PARENTHESIS, checked from 2M\'s own expression:')
    need('2M = r0 - r0^3 is at source, which is what says r0 is a root',
         'Write $2M=r_{0}-r_{0}^{3}$' in p3flat)
    for lab, x in ENDPOINTS.items():
        say(f'      2M({lab:9s}) = {twoM(x):+.12f}')
    say(f'      2M(+1.1) = {twoM(1.1):+.12f}   (r0 just above 1)')
    need('2M >= 0 exactly on [0, 1] within the involution\'s domain -- non-negative at 0, '
         '1/sqrt3 and 1, and NEGATIVE both below 0 and above 1 -- so the narrowed '
         'parenthesis is right and the old one was wrong',
         twoM(0.0) >= 0 and twoM(1.0 / S3) > 0 and close(twoM(1.0), 0.0)
         and twoM(1.1) < 0 and twoM(-1.0 / S3) < 0)

    say('')
    for n in ('sl_factor', 'sl_roots', 'sl_r0zero', 'sl_readingswap', 'sl_σ_σ',
              'sl_σ_swap', 'sl_σ_second', 'sl_σ_fixed', 'sl_locus',
              'sl_ellipse', 'sl_nariai'):
        need(f'4c {n} exists', decl_header(lean, n) is not None)
        need(f'4c {n} is cited in P3 (by SKELETON)', cited_in_tex(p3flat, n))
    say('    ⌗ And the file itself flags the old error in sl_σ_swap\'s docstring:')
    ext = decl_extent(lean, 'sl_σ_swap') or ''
    need('sl_σ_swap states BOTH directions of the exchange AND that σ is not a self-map '
         'of [0, 2/√3], naming σ(2/√3) < 0',
         'MapsTo sl_σ (Set.Icc 0 (2 / Real.sqrt 3))' in ext
         and 'MapsTo sl_σ (Set.Icc (-1 / Real.sqrt 3) 1)' in ext
         and '∉ Set.Icc 0 (2 / Real.sqrt 3)' in ext)
    need('and it states the IMAGE equality, not merely containment, which is what "exchanges" '
         'needs', "sl_σ '' Set.Icc 0 (2 / Real.sqrt 3) = Set.Icc (-1 / Real.sqrt 3) 1"
         in ext)
    sec = decl_statement(lean, 'sl_σ_second') or ''
    need('and sl_σ_second confines "the second POSITIVE root" to [0, 1), which is why the '
         'formal paragraph says $[0,1)$ where the proposition says $[0,1]$ with '
         '"non-negative" -- the two wordings are consistent, not a discrepancy',
         'x < 1' in sec and 'its carrying of $r_{0}\\in[0,1)$ to the other positive root'
         in p3flat
         and 'it is a decreasing map onto $[0,1]$ that carries the slicing parameter to the '
         'other non-negative root' in p3flat)

    say('')
    nax = len(re.findall(r'^axiom\s', lean, re.M))
    nsorry = len(re.findall(r'\bsorry\b', lean))
    say(f'    SlicingCubic.lean: axiom tokens = {nax}; sorry = {nsorry}')
    need('zero axiom tokens and zero sorry', nax == 0 and nsorry == 0)

    say('')
    say('  4d THIS SEAT\'S OWN r7720 REPAIR, as landed in P2:')
    need('the Sbierski citation now names the Discussion section and no longer the remark',
         'curvature-independent $C^{0}$-inextendibility of the maximal analytic Schwarzschild '
         'spacetime (Section~\\ref{sec:discussion})' in p2flat)
    need('and the offered bridge clause is taken, verbatim',
         'since such an extension would be a $C^{0}$ extension of that spacetime' in p2flat)
    need('the wrong pointer is gone: the Sbierski clause no longer cites the remark -- '
         'searched for the old parenthetical verbatim',
         'inextendibility (Remark~\\ref{rem:asymmetric_chart})' not in p2flat)
    return True


def main():
    global LEANSRC
    p3 = flat(open(P3).read())
    p2 = flat(open(ROOT + '/corpus/janzen_circle_v3.tex').read())
    LEANSRC = open(LEAN).read()
    selftests(p3)
    q1_truth(p3)
    q1_dependents(p3)
    q2(p3, LEANSRC)
    q3(p3, LEANSRC)
    item4(p3, p2, LEANSRC)
    say('')
    say('=' * 78)
    if FAIL:
        say(f'{len(FAIL)} ARM(S) FAILED:')
        for f in FAIL:
            say('  - ' + f)
        return 1
    say('ALL ARMS AND SELF-CHECKS PASS.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
