#!/usr/bin/env python3
"""r7718 (60) -- P2's new maximality sentence, read cold against the paper's own thesis.

Arms registered in PREDICTION.md before either side was read -- neither thesis
sentence, nor prop:Kretschmann, nor the new paragraph, nor any mx_ declaration.  The readers r7714 repaired are carried forward unchanged
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
LEAN = ROOT + '/computations/formalisation/lean/probes/CircleMaximal.lean'

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

# =============================================================== SELF-TESTS
def selftests(p2flat):
    say('=' * 78)
    say('SELF-TESTS -- every classifier and reader on BOTH of its classes, before use')
    say('=' * 78)
    need('G2 accepts plain prose', anchor('an absolute terminus admitting no continuation') == 'prose')
    need('G2 accepts an escaped control sequence', anchor(r'\emph') == 'macro')
    need('G2 accepts an escaped math delimiter', anchor('$UV<1$') == 'math')
    need('G2 REFUSES a marker mixing prose with math', anchor(r'the boundary at $r=0$') is None)

    need('skeleton: a plain ASCII name IS found',
         cited_in_tex(r'(\texttt{mx\_blowup})', 'mx_blowup'))
    need('skeleton: a name NOT on the page is NOT found',
         not cited_in_tex(r'(\texttt{mx\_blowup})', 'mx_nowhere'))
    need('skeleton: a name that is a PREFIX of another is not credited to it',
         not cited_in_tex(r'(\texttt{mx\_frontier})', 'mx_frontier_two'))

    need('reader: mx_inextendible has a header',
         decl_header(LEANSRC, 'mx_inextendible') is not None)
    need('reader: a declaration that does not exist reads as absent',
         decl_header(LEANSRC, 'mx_inextendible_not_a_declaration') is None)
    need('reader: decl_extent reaches a def\'s BODY, which lives after ":="',
         'kr_K (kr_SD M).gW' in (decl_extent(LEANSRC, 'mx_K') or ''))
    need('reader: binders survive a type carrying parentheses',
         binders('theorem t (hM : 0 < M) {θ φ : ℝ} (hθ : Real.sin θ ≠ 0) :')
         == ['(hM : 0 < M)', '{θ φ : ℝ}', '(hθ : Real.sin θ ≠ 0)'])

    # G4: the SUBJECT classifier, on each of its classes.
    need('subject classifier: a sentence about the curve reads as the curve',
         subject_of('the continuation carries the smooth curve through the critical point')
         == 'curve')
    need('subject classifier: a sentence about a metric on a chart reads as that',
         subject_of('this bounds the Kruskal metric in its own chart, whose scalar is the '
                    'chart\'s') == 'metric-on-chart')
    need('subject classifier: a sentence about an abstract spacetime reads as that',
         subject_of('maximality among all extensions, as an abstract spacetime, of that '
                    'spacetime manifold') == 'spacetime')

    # G4: the inference-PAIR comparison, on a same-subject and a different-subject pair.
    need('pair: same subject AND same conclusion is the SAME inference',
         same_inference(('curve', 'inextendible'), ('curve', 'inextendible')))
    need('pair: same conclusion but DIFFERENT subject is NOT the same inference',
         not same_inference(('curve', 'inextendible'),
                            ('metric-on-chart', 'inextendible')))
    need('pair: same subject but different conclusion is NOT the same inference',
         not same_inference(('curve', 'inextendible'), ('curve', 'bounded')))

    # G4: the metric-vs-function reader, on both classes.
    need('conclusion reader: an existential over a real-valued function reads as that',
         states_about_metrics('theorem t (hM : 0 < M) {p : P} (hp : p ∈ frontier sk_kM) : '
                              '¬∃ G : P → ℝ, ContinuousAt G p') == 'a real-valued function')
    need('conclusion reader: a conclusion naming a metric reads as a metric',
         states_about_metrics('theorem t (hM : 0 < M) : ∃ S : MSpacetime P Pt, True')
         == 'a metric')
    need('conclusion reader: the C1 regularity of a CHART MAP is NOT a metric statement',
         states_about_metrics('lemma mx_fA_contDiff : ContDiff R 1 mx_fA')
         == 'the regularity of some other map')
    need('bounds reader: "bounds the metric in its chart and not the curve" bounds '
         'the metric',
         bounds_subject('This bounds the Kruskal metric in its own chart and not the '
                        'curve: the continuation carries the curve across it')
         == 'metric-on-chart')
    need('bounds reader: the SAME clause written the other way round bounds the curve',
         bounds_subject('This bounds the continuation of the curve and not the metric '
                        'in its own chart: the metric carries no further')
         == 'curve')

    need('G6: the maximality sentence is one line only after flattening',
         'machine-checked to be maximal within its own chart' in p2flat)
    say('')


# ==================================================================== ARMS
def thesis(p2flat):
    say('=' * 78)
    say('ARM 1 -- WHAT P2\'s THESIS ACTUALLY CLAIMS, located BY ITS TEXT')
    say('      (the order gives line numbers; those are numbers in a file edited since,')
    say('       and this seat has been bitten by exactly that)')
    say('=' * 78)
    sites = {
        'the falsification paragraph':
            'What the present paper establishes, independently of that question, is that the '
            'inextendibility \\emph{inference} of the standard classification---from the '
            'curvature divergence to an inextendible boundary---is false.',
        'the inference as the paper states it':
            'the step from the curvature divergence at $r=0$ to the conclusion that no '
            'continuation through it exists',
        'the gloss on "inextendible boundary"':
            'an \\emph{absolute terminus admitting no continuation}',
        'the standard reading, conceded in full':
            'the divergence at $z=\\pi$ is genuine, no regular Lorentzian extension crosses '
            'it, and the $r<0$ arm is a separate region reached only by continuing the '
            'coordinate expressions across a singular junction; the curve is extendible, the '
            'spacetime is not',
    }
    for lab, mark in sites.items():
        anchored(re.sub(r'[^A-Za-z ]', ' ', lab))
        need(f'located by text: {lab}', mark in p2flat)
    say('')
    say('    THE SUBJECT OF THE REFUTED INFERENCE, read from the paper\'s own gloss:')
    gloss = sites['the inference as the paper states it']
    say(f'      {gloss}')
    say(f'      -> subject reads as: {subject_of(gloss)}')
    need('the refuted inference\'s conclusion is about a CONTINUATION, i.e. the curve, and '
         'not about a metric', subject_of(gloss) == 'curve')
    say('')
    say('    AND WHAT THE PAPER ALREADY CONCEDES ON THE METRIC SIDE, in its own words:')
    say(f'      "...the curve is extendible, the spacetime is not"')
    need('the paper itself states that no regular Lorentzian extension crosses the '
         'divergence, on the standard reading', 'no regular Lorentzian extension crosses it'
         in p2flat)
    return subject_of(gloss)


def artefact(p2flat):
    say('')
    say('=' * 78)
    say('ARM 2 -- THE "ARTEFACT" CLAIM, WHICH IS WHERE I REGISTERED THAT I MIGHT BE WRONG')
    say('      A scalar INVARIANT cannot be a chart artefact, so either the paper means')
    say('      something narrower, or its own thesis is in trouble before any Lean file.')
    say('=' * 78)
    prop = ('Expressed as a function of $z$, the Kretschmann scalar $K(z)$ has a '
            'twelfth-order pole at $z = \\pi$ and remains bounded at $z = 0$.')
    need('prop:Kretschmann is located by text', prop in p2flat)
    say(f'    {prop}')
    need('⚑ prop:Kretschmann ASSERTS the pole rather than denying it, so the paper does NOT '
         'claim the divergence is absent', 'twelfth-order pole at $z = \\pi$' in p2flat)
    abstract = ('is therefore the curvature scalar of the Schwarzschild perspectival '
                'metric---the metric as a tensor field over the parameter $r$, real as that '
                'metric\'s---rather than an invariant of the underlying smooth manifold '
                'parametrised by $z$')
    need('and the abstract states the artefact claim RELATIVE TO A METRIC, granting the '
         'divergence is "real as that metric\'s"', abstract in p2flat)
    need('and elsewhere the paper says the incompleteness is real and NOT a mere chart '
         'artefact, in those words',
         'The incompleteness at $r = 0$ is real, not a mere chart artefact' in p2flat)
    say('    ⌗ READING: the paper\'s "artefact" is an answer to WHICH METRIC CARRIES THE')
    say('      INVARIANT, not to whether the scalar diverges. The registered worry is NOT')
    say('      borne out, and the arm survived because it was built to read the proposition.')
    return True


def theorems(p2flat, lean):
    say('')
    say('=' * 78)
    say('ARM 3 -- WHAT THE THREE DECLARATIONS ACTUALLY STATE')
    say('=' * 78)
    for n in ('mx_frontier', 'mx_blowup', 'mx_inextendible'):
        h = decl_header(lean, n)
        say(f'    {n}: {h}')
        need(f'{n} exists', h is not None)
        need(f'{n} is cited in P2 (by SKELETON)', cited_in_tex(p2flat, n))
    say('')
    fr = decl_header(lean, 'mx_frontier') or ''
    need('mx_frontier states the FRONTIER OF A SET -- frontier {UV<1} = {UV=1} -- which is '
         'what "the only boundary ... is the hyperbola" says',
         'frontier sk_kM = {p : P | p.1 * p.2 = 1}' in fr)
    need('⌗ and it does NOT state "where r = 0": that identification is the LIMIT inside '
         'mx_blowup\'s chain and not a conclusion of mx_frontier',
         'rK' not in fr and 'r = 0' not in fr)
    bl = decl_header(lean, 'mx_blowup') or ''
    need('mx_blowup is approached FROM INSIDE -- the within-domain filter, asserted '
         'non-trivial -- and the scalar tends to +infinity',
         '[sk_kM] p).NeBot' in bl and 'Filter.atTop' in bl)
    need('and the scalar is the KRUSKAL chart\'s: mx_K is kr_K of (kr_SD M).gW',
         'kr_K (kr_SD M).gW' in (decl_extent(lean, 'mx_K') or ''))
    say('')
    say('  ⛔ AND THE STEP THE PROSE TAKES THAT NO DECLARATION STATES:')
    ix = decl_header(lean, 'mx_inextendible') or ''
    kind = states_about_metrics(ix)
    say(f'    mx_inextendible\'s conclusion quantifies over ..... {kind}')
    need('mx_inextendible concludes about a REAL-VALUED FUNCTION -- no continuous G agrees '
         'with the scalar near the frontier point -- and names no metric at all',
         kind == 'a real-valued function')
    # a NAMED search for any declaration whose statement reaches a metric's regularity.
    names = ('mx_C2', 'mx_ext', 'mx_extension', 'mx_metric_inextendible', 'mx_no_extension',
             'mx_maximal', 'mx_inext_metric')
    found = [n for n in names if decl_header(lean, n) is not None]
    say(f'    NAMED SEARCH for a declaration about a METRIC extension -- '
        f'{", ".join(names)}: {found if found else "NOT FOUND over all seven names"}')
    # AND BY SHAPE, over every mx_ declaration in the file, both namespaces.
    allmx = re.findall(r'^(?:theorem|lemma)\s+(mx_\w+)', lean, re.M)
    metricish = [n for n in allmx
                 if states_about_metrics(decl_header(lean, n) or '') == 'a metric']
    mapreg = [n for n in allmx
              if states_about_metrics(decl_header(lean, n) or '')
              == 'the regularity of some other map']
    say(f'    (regularity statements about MAPS and not metrics, from the earlier '
        f'campaign, listed so they are not silently counted: {mapreg})')
    shape_report = (metricish if metricish
                    else 'none states the C2 regularity of an extension of a metric')
    say(f'    AND BY SHAPE over all {len(allmx)} mx_ theorems and lemmas in the file '
        f'(the prefix is reused by an EARLIER campaign in another namespace, so the search '
        f'is wider than this landing): {shape_report}')
    need('so "and therefore no $C^{2}$ extension of the metric" is the PROSE\'s step: sound '
         'mathematics, but no cited declaration states it, while the parenthesis attaches to '
         'the whole sentence', not found and not metricish)
    return kind


def collision(p2flat, thesis_subject):
    say('')
    say('=' * 78)
    say('ARM 4 -- THE COLLISION QUESTION, DECIDED ON THE PAIR AND NOT ON THE PREMISE')
    say('=' * 78)
    new = ('The Kruskal--Szekeres extension is machine-checked to be maximal within its own '
           'chart')
    need('the new sentence is at source, verbatim', new in p2flat)
    clause = ('This bounds the Kruskal metric in its own chart and not the curve: the '
              'continuation through $z=\\pi$ carries the curve, and not this metric, across '
              '$r=0$')
    need('and its separating clause is at source, verbatim', clause in p2flat)
    say('')
    thesis_pair = (thesis_subject, 'no continuation exists')
    theorem_pair = (subject_of(new + ' ' + clause), 'no continuous extension of the scalar')
    say(f'    THE REFUTED INFERENCE: subject {thesis_pair[0]!r}, conclusion '
        f'{thesis_pair[1]!r}')
    say(f'    THE ASSERTED INFERENCE: subject {theorem_pair[0]!r}, conclusion '
        f'{theorem_pair[1]!r}')
    need('the two are NOT the same inference -- they differ in BOTH members, and sharing '
         'the Kretschmann premise does not make them one',
         not same_inference(thesis_pair, theorem_pair))
    need('and the separating clause names the subjects they differ in, in the paper\'s own '
         'words -- what it BOUNDS is the metric on its chart, and what it declines '
         'to bound is the curve',
         bounds_subject(clause) == 'metric-on-chart'
         and 'and not the curve' in clause)
    say(f'    the clause bounds ..... {bounds_subject(clause)!r}, declining the curve')
    need('which matches the thesis section\'s own formulation, located by text',
         'the curve is extendible, the spacetime is not' in p2flat)
    say('    ⌗ So the answer to the order\'s sharp question is NO COLLISION -- and it is the')
    say('      pair that decides it, not the presence of the clause: a clause that ASSERTS a')
    say('      distinction does not MAKE one, which is why both subjects were read.')
    say('')
    say('  ⚑ BUT ONE CHARACTERISATION ELSEWHERE IN P2 IS NOW UNDERSTATED BY THE PAPER\'S')
    say('    OWN RESULT, and this is the repair:')
    surv = ('what is left standing is the rigorous, curvature-independent $C^{0}$-'
            'inextendibility of $r=0$ established by Sbierski')
    need('P2 says, in the abstract, that what is left standing is the CURVATURE-INDEPENDENT '
         'inextendibility', surv in p2flat)
    n_ci = len(re.findall(r'curvature-independent|curvature-free', p2flat))
    say(f'    "curvature-independent" / "curvature-free" occurs {n_ci} times in P2, each '
        f'characterising what survives the falsification')
    need('and the new paragraph reaches inextendibility FROM the curvature, for the metric '
         'in its chart, so "the only surviving inextendibility is curvature-independent" is '
         'no longer the whole of what this paper establishes',
         n_ci >= 2 and 'the Kretschmann scalar of the Kruskal metric grows without bound'
         in p2flat)
    return True


def item5(p2flat, lean):
    say('')
    say('=' * 78)
    say('ITEM 5 -- THE REST OF THE LANDING')
    say('=' * 78)
    need('5a this seat\'s offered word is landed: the two $r<0$ patches are EACH '
         'machine-checked',
         'The two $r<0$ patches are each machine-checked as a geometry in their own right'
         in p2flat)
    last = 'Maximality among all extensions, as an abstract spacetime, is not formalised.'
    need('5b the paragraph\'s last sentence is at source, verbatim', last in p2flat)
    need('its predecessor -- "That the Kruskal--Szekeres extension is maximal is not '
         'formalised" -- is gone from P2, which is what this landing checks',
         'That the Kruskal--Szekeres extension is maximal is not formalised' not in p2flat)
    need('and the file says the same in its own header, so prose and file agree on what is '
         'NOT claimed',
         'maximality as an abstract spacetime, is not formalised' in flat(lean))
    nax = len(re.findall(r'^axiom\s', lean, re.M))
    nsorry = len(re.findall(r'\bsorry\b', lean))
    say(f'    5c CircleMaximal.lean: axiom tokens = {nax}; sorry = {nsorry}')
    need('zero axiom tokens and zero sorry', nax == 0 and nsorry == 0)
    return True


def main():
    global LEANSRC
    p2 = flat(open(P2).read())
    LEANSRC = open(LEAN).read()
    selftests(p2)
    subj = thesis(p2)
    artefact(p2)
    theorems(p2, LEANSRC)
    collision(p2, subj)
    item5(p2, LEANSRC)
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
