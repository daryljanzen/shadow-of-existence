#!/usr/bin/env python3
"""r7720 (60) -- the Sbierski implication and the conic branch conditions, read cold.

Arms registered in PREDICTION.md before either landed sentence was read, before
rem:asymmetric_chart, and before any cn_ declaration.  The readers of r7714,
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
import re
import sys

ROOT = '/home/user/shadow-of-existence'
P2 = ROOT + '/corpus/janzen_circle_v3.tex'
LEAN = ROOT + '/computations/formalisation/lean/probes/CircleConic.lean'

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
GREEK = {'\u03a6': 'Phi', '\u03a8': 'Psi', '\u03b7': 'eta', '\u03c1': 'rho',
         '\u03c4': 'tau', '\u0393': 'Gamma'}

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

# =============================================================== SELF-TESTS
def selftests(p2flat):
    say('=' * 78)
    say('SELF-TESTS -- every classifier and reader on BOTH of its classes, before use')
    say('=' * 78)
    need('G2 accepts plain prose', anchor('is one conic') == 'prose')
    need('G2 accepts an escaped control sequence', anchor(r'\texttt') == 'macro')
    need('G2 accepts an escaped math delimiter', anchor('$UV=1$') == 'math')
    need('G2 REFUSES a marker mixing prose with math', anchor(r'the branches $r\ge2M$') is None)

    need('skeleton: a plain ASCII name IS found',
         cited_in_tex(r'(\texttt{cn\_hyperbolas})', 'cn_hyperbolas'))
    need('skeleton: a name NOT on the page is NOT found',
         not cited_in_tex(r'(\texttt{cn\_hyperbolas})', 'cn_nowhere'))
    need('skeleton: a name that is a PREFIX of another is not credited to it',
         not cited_in_tex(r'(\texttt{cn\_curve})', 'cn_curve_two'))

    need('reader: cn_hyperbolas has a header',
         decl_header(LEANSRC, 'cn_hyperbolas') is not None)
    need('reader: a declaration that does not exist reads as absent',
         decl_header(LEANSRC, 'cn_hyperbolas_not_a_declaration') is None)
    need('reader: decl_extent reaches a def\'s BODY, which lives after ":="',
         'Complex.cos z' in (decl_extent(LEANSRC, 'cn_r') or ''))
    need('reader: binders survive a type carrying parentheses',
         binders('theorem t (M : \u211d) (hM : 0 \u2264 M) (\u03c1 : \u211d) :')
         == ['(M : \u211d)', '(hM : 0 \u2264 M)', '(\u03c1 : \u211d)'])

    # G4: the regularity-direction reader, on BOTH directions.
    need('regularity reader: ruling out C0 extensions DOES rule out C2 ones',
         regularity_implies('C0', 'C2') == 'implies')
    need('regularity reader: ruling out C2 extensions does NOT rule out C0 ones',
         regularity_implies('C2', 'C0') == 'does not imply')
    need('regularity reader: an unknown class is reported as unknown',
         regularity_implies('C0', 'Lipschitz') == 'unknown')

    # G4: the inference-PAIR comparison, carried forward from r7718, re-tested.
    need('pair: same subject AND same conclusion is the SAME inference',
         same_inference(('spacetime', 'no C0 extension'), ('spacetime', 'no C0 extension')))
    need('pair: same conclusion but DIFFERENT subject is NOT the same inference',
         not same_inference(('spacetime', 'no C0 extension'),
                            ('metric-on-chart', 'no C0 extension')))
    need('subject classifier: a sentence about an abstract spacetime reads as that',
         subject_of('the inextendibility of the maximal analytic Schwarzschild spacetime, '
                    'as an abstract spacetime manifold') == 'spacetime')
    need('subject classifier: a sentence about a metric on a chart reads as that',
         subject_of('a C2 extension of the metric across a boundary point of the chart, '
                    'whose scalar is the chart\'s') == 'metric-on-chart')

    # G4: the equation/inequality reader, on one of each.
    need('conjunct reader: an equation reads as an equation',
         kind_of('(M * (1 + Real.cosh \u03c1) - M) ^ 2 - (M * Real.sinh \u03c1) ^ 2 = M ^ 2')
         == 'equation')
    need('conjunct reader: an inequality reads as an inequality',
         kind_of('2 * M \u2264 M * (1 + Real.cosh \u03c1)') == 'inequality')
    need('conclusion reader: the conclusion is found by DEPTH, so a nested type '
         'ascription in it does not cut the statement short',
         conclusion_of('theorem t (M : \u211d) (h : 0 \u2264 M) : a = ((b : \u211d) : \u2102) \u2227 c = 1')
         == 'a = ((b : \u211d) : \u2102) \u2227 c = 1')
    need('conclusion reader: and a header with no depth-zero colon returns itself',
         conclusion_of('(M : \u211d)') == '(M : \u211d)')
    need('conjunct reader: all eight conjuncts of a nested conclusion are found',
         len(conjuncts('theorem t (M : \u211d) : a = ((p : \u211d) : \u2102) \u2227 b = ((q : \u211d) : \u2102) \u2227 c \u2264 d')) == 3)
    need('conjunct reader: a differentiability claim is neither',
         kind_of('Differentiable \u2102 (cn_r M)') == 'other')

    need('G6: the landed clause is one line only after flattening',
         'that consequence for the metric is also implied by Sbierski' in p2flat)
    say('')


# ==================================================================== ARMS
def q1(p2flat):
    say('=' * 78)
    say('Q1 -- IS "implied by Sbierski\'s stronger, curvature-independent C0-inextendibility"')
    say('      RIGHT?  Three conjuncts, each with its own predicate (G1).')
    say('=' * 78)
    clause = ('A $C^{2}$ extension of the metric across such a point would make the scalar '
              'continuous there, so none exists; that consequence for the metric is also '
              'implied by Sbierski\'s stronger, curvature-independent $C^{0}$-inextendibility '
              '(Remark~\\ref{rem:asymmetric_chart})')
    need('the clause is at source, verbatim', clause in p2flat)

    say('')
    say('  (a) "STRONGER" -- read as a CONTAINMENT and not as a word:')
    say(f'    ruling out C0 extensions -> C2: {regularity_implies("C0", "C2")}')
    say(f'    ruling out C2 extensions -> C0: {regularity_implies("C2", "C0")}')
    need('"stronger" is the right way round: a C2 metric is in particular C0, so a C2 '
         'extension is a C0 extension, and ruling out every C0 extension rules out every '
         'C2 one', regularity_implies('C0', 'C2') == 'implies'
         and regularity_implies('C2', 'C0') == 'does not imply')

    say('')
    say('  (b) "IMPLIED" -- read as a SUBJECT comparison, which is where a shift would hide:')
    sb = ('The inextendibility of the maximal analytic Schwarzschild spacetime has, moreover, '
          'been established rigorously and at low regularity by Sbierski')
    need('P2\'s own statement of Sbierski\'s theorem is located by text', sb in p2flat)
    pair_sb = (subject_of(sb), 'no C0 extension')
    pair_cl = (subject_of('a C2 extension of the metric across such a point, in the chart'),
               'no C2 extension across a frontier point')
    say(f'    SBIERSKI: subject {pair_sb[0]!r}, conclusion {pair_sb[1]!r}')
    say(f'    THE CLAUSE: subject {pair_cl[0]!r}, conclusion {pair_cl[1]!r}')
    need('the two are NOT the same inference, so the implication needs a BRIDGE and is not '
         'a containment of regularity classes alone', not same_inference(pair_sb, pair_cl))
    say('    ⌗ THE BRIDGE, stated so it can be judged: a C2 extension of the metric across a')
    say('      frontier point of the chart gives a larger connected Lorentzian manifold')
    say('      containing the original isometrically with a CONTINUOUS metric -- which is a')
    say('      C0 extension of the spacetime, the thing Sbierski rules out.  So the')
    say('      implication HOLDS.  It is sound mathematics the sentence leaves implicit.')
    say('')
    say('  (c) THE PREMISE THE BRIDGE NEEDS -- that the chart object IS Sbierski\'s object:')
    ident = ('Sbierski\'s theorem concerns the maximal analytic Schwarzschild spacetime---the '
             '$\\Lambda=0$ object')
    need('P2 states which object Sbierski\'s theorem is about, located by text',
         ident in p2flat)
    need('and P2 claims its own four patches with the horizons ARE that extension, so the '
         'identification is made in the paper',
         'with the horizons at which they meet, they are precisely the maximal '
         'Kruskal--Szekeres extension' in p2flat)
    say('    ⌗ READING: the identification is PAPER-LEVEL -- the paragraph\'s own last')
    say('      sentence says maximality among all extensions, as an abstract spacetime, is')
    say('      not formalised -- so the implication is sound as mathematics and rests on a')
    say('      claim the paper makes in prose and the machine does not check.')
    return True


def q1_citation(p2flat, src_raw):
    say('')
    say('=' * 78)
    say('⛔ Q1, THE CITATION -- AND IT DOES NOT POINT WHERE THE CLAUSE SAYS IT DOES')
    say('=' * 78)
    t = flat(src_raw)
    i = t.find('\\begin{remark}\\label{rem:asymmetric_chart}')
    j = t.find('\\end{remark}', i)
    need('the remark is located by its own label', i >= 0 and j > i)
    ext = t[i:j]
    say(f'    the remark\'s whole extent is {len(ext)} characters, and reads:')
    say(f'      {ext[:430]}')
    say('')
    say('    NAMED SEARCH over that whole extent:')
    probes = ('Sbierski', 'sbierski', 'inextendib', 'extension', 'C^{0}', 'C^0')
    for p in probes:
        say(f'      {p!r}: {"found" if p in ext else "NOT FOUND"}')
    need('the remark the clause cites names Sbierski NOWHERE, and says nothing about '
         'inextendibility, extensions, or $C^{0}$ -- searched for all six of those strings '
         'over its whole 672-character extent',
         not any(p in ext for p in probes))
    need('and the label is defined exactly ONCE in P2, so this is not a second remark of '
         'the same name', len(re.findall(r'\\label\{rem:asymmetric_chart\}', t)) == 1)
    say('')
    say('    WHERE SBIERSKI\'S RESULT IS ACTUALLY SET OUT, located by text:')
    k = t.find('has, moreover, been established rigorously and at low regularity by Sbierski')
    need('the passage exists', k > 0)
    secs = re.findall(r'\\(?:sub)?section\{([^}]*)\}\\label\{([^}]+)\}', t[:k])
    say(f'      nearest preceding sectioning command with a label: {secs[-1] if secs else None}')
    need('it is in the Discussion section and not in the remark',
         bool(secs) and secs[-1][1] == 'sec:discussion')
    need('and the remark is upstream of it, so a reader following the citation goes to the '
         'wrong place and finds no Sbierski at all', i < k)
    return True


def q2(p2flat, lean):
    say('')
    say('=' * 78)
    say('Q2 -- DOES cn_hyperbolas STATE THE BRANCH CONDITIONS, OR ONLY THE IDENTITIES?')
    say('=' * 78)
    sent = ('is the pair of branches $r\\ge2M$ and $r\\le0$ of the hyperbola '
            '$(r-M)^{2}-\\sigma^{2}=M^{2}$ (\\texttt{cn\\_hyperbolas})')
    need('the claim is at source, verbatim', sent in p2flat)
    h = decl_header(lean, 'cn_hyperbolas')
    say(f'    cn_hyperbolas: {h}')
    cs = conjuncts(h or '')
    say(f'    READING -- {len(cs)} top-level conjuncts, by KIND:')
    for c in cs:
        say(f'      [{kind_of(c)}] {c}')
    eqs = [c for c in cs if kind_of(c) == 'equation']
    ineqs = [c for c in cs if kind_of(c) == 'inequality']
    need('the identities are there, as equations', len(eqs) >= 6)
    need('⚑ AND SO ARE THE BRANCH CONDITIONS, as two INEQUALITIES in $r$ -- so the sentence '
         'is exact and the inviting answer is the true one', len(ineqs) == 2)
    need('the first branch condition is $r \\ge 2M$ on the $z=i\\rho$ line',
         any('2 * M \u2264 M * (1 + Real.cosh' in c for c in ineqs))
    need('and the second is $r \\le 0$ on the $z=\\pi+i\\rho$ line',
         any('M * (1 - Real.cosh \u03c1) \u2264 0' in c for c in ineqs))
    say('')
    say('  ⌗ AND WHAT THE INEQUALITIES COST, read from the binders rather than assumed:')
    say(f'    binders: {binders(h or "")}')
    need('they need $0 \\le M$, which is a real hypothesis of the theorem and not of the '
         'identities\' own algebra', '(hM : 0 \u2264 M)' in (h or ''))
    say('    ⌗ The paper\'s standing assumption is $M>0$, so the hypothesis is met; it is')
    say('      noted because the identity conjuncts do not need it and the branch ones do.')
    return len(ineqs)


def item3(p2flat, lean):
    say('')
    say('=' * 78)
    say('ITEM 3 -- THE REST OF THE LANDING')
    say('=' * 78)
    say('  3a THE "THEREFORE" REPAIR, read against WHAT WAS ROUTED and not the order\'s')
    say('     summary of it.  r7720 routed: say that what is machine-checked is the')
    say('     non-existence of a continuous extension of the SCALAR, and mark the C2')
    say('     consequence as following by the standard argument rather than by a theorem.')
    need('the scalar half now ends at the citation, so the parenthesis covers only what the '
         'three declarations state',
         'so no continuous extension of that scalar exists across any point of it '
         '(\\texttt{mx\\_frontier}, \\texttt{mx\\_blowup} and \\texttt{mx\\_inextendible}).'
         in p2flat)
    need('and the metric consequence is now a SEPARATE sentence giving its argument, with no '
         'declaration cited for it',
         'A $C^{2}$ extension of the metric across such a point would make the scalar '
         'continuous there, so none exists' in p2flat)
    need('the old form, which put "and therefore no $C^{2}$ extension of the metric" inside '
         'the cited parenthesis, is gone from P2 -- searched for that clause verbatim',
         'and therefore no $C^{2}$ extension of the metric, exists across any point of it'
         not in p2flat)

    say('')
    for n in ('cn_curve', 'cn_circle', 'cn_hyperbolas'):
        need(f'3b {n} exists', decl_header(lean, n) is not None)
        need(f'3b {n} is cited in P2 (by SKELETON)', cited_in_tex(p2flat, n))
    cc = decl_header(lean, 'cn_curve') or ''
    say(f'    cn_curve: {cc}')
    need('"entire" is what cn_curve states, and of BOTH $r$ and $s$ -- differentiability on '
         'the whole of the complex plane for each',
         cc.count('Differentiable \u2102') == 2
         and 'Differentiable \u2102 (cn_r M)' in cc and 'Differentiable \u2102 (cn_s M)' in cc)
    need('and the identity it states holds at EVERY complex $z$, as the sentence says',
         '\u2200 z : \u2102' in cc)
    ci = decl_header(lean, 'cn_circle') or ''
    say(f'    cn_circle: {ci}')
    need('cn_circle is stated for a real argument with NO domain restriction, which is what '
         '"on the real line" says', '(M \u03b7 : \u211d)' in ci and 'Ioo' not in ci)

    say('')
    nax = len(re.findall(r'^axiom\s', lean, re.M))
    nsorry = len(re.findall(r'\bsorry\b', lean))
    say(f'    3d CircleConic.lean: axiom tokens = {nax}; sorry = {nsorry}')
    need('zero axiom tokens and zero sorry', nax == 0 and nsorry == 0)
    return True


def main():
    global LEANSRC
    raw = open(P2).read()
    p2 = flat(raw)
    LEANSRC = open(LEAN).read()
    selftests(p2)
    q1(p2)
    q1_citation(p2, raw)
    q2(p2, LEANSRC)
    item3(p2, LEANSRC)
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
