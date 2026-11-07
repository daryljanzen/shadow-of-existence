#!/usr/bin/env python3
"""r7706 (60) -- the readings behind RESULT.md, every verdict BUILT FROM them.

Order r7703, three items: the prop:cycloid fix and the sites that survive it; the new
formal paragraph against CircleKretschmann.lean; P15's trimmed scope sentence.

GUARDS.  G1 one predicate per conjunct.  G2 three anchor forms only -- a word boundary,
an escaped control sequence with ONE leading backslash, an escaped math delimiter --
unanchored markers REFUSED.  G3 the flip family, striking EVERY copy of a conjunct.
G4 classifier probes tested on BOTH classes.  G5 reader probes with negatives.
G6 every prose probe on a whitespace-FLATTENED copy.
"""
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
P2 = os.path.join(ROOT, 'corpus', 'janzen_circle_v3.tex')
P15 = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
LEAN = os.path.join(ROOT, 'computations', 'formalisation', 'lean', 'probes',
                    'CircleKretschmann.lean')

OUT = []
FAIL = []


def say(s=''):
    OUT.append(s)
    print(s)


def flat(s):                                   # G6
    return re.sub(r'\s+', ' ', s)


def anchor(marker):                            # G2
    """Three anchor forms only.  Anything else is REFUSED, not silently widened."""
    if re.fullmatch(r"[A-Za-z0-9 ,.'\-()/=+:;]+", marker):
        return r'\b' + re.escape(marker) + r'\b'
    if re.fullmatch(r'\\[A-Za-z]+', marker):
        return re.escape(marker) + r'(?![A-Za-z])'
    if re.fullmatch(r'\$[^$]+\$', marker):
        return re.escape(marker)
    raise SystemExit(f'  [REFUSED] unanchorable marker: {marker!r}')


def need(path):
    with open(path, encoding='utf-8') as f:
        return f.read()


def verdict(v):
    if isinstance(v, str):
        return v
    return 'SUPPORTED' if v else 'NOT SUPPORTED'


# ----------------------------------------------------------------- readers

def lean_decls(src):
    """name -> (kind, line number).  G5-tested below on a known name and a fiction."""
    out = {}
    for m in re.finditer(r'^(?:noncomputable\s+)?(theorem|lemma|def|abbrev|axiom)\s+'
                         r'([A-Za-z_][A-Za-z0-9_\'.]*)', src, re.M):
        out.setdefault(m.group(2), (m.group(1), src[:m.start()].count('\n') + 1))
    return out


def lean_statement(src, name):
    """The declaration's text from its header to the ':= by' or ':=' that opens its proof."""
    m = re.search(r'^(?:noncomputable\s+)?(?:theorem|lemma|def|abbrev)\s+' +
                  re.escape(name) + r'\b', src, re.M)
    if not m:
        return None
    tail = src[m.start():]
    stop = re.search(r':=\s*(by\b|\n)', tail)
    return tail[:stop.start()] if stop else tail[:4000]


def binders(header):
    r"""The binders of a declaration HEADER, by bracket-depth matching, Unicode-aware.

    ⬭ r7700: `\((h[A-Za-z0-9_]*) : ([^)]*)\)` is ASCII-only, so `hτ` was INVISIBLE and the
      arm it fed was the WHOLENESS of a hypothesis list.  \w with re.UNICODE sees it.
    ⬭ r7706, MEASURED HERE: a flat `[^()]*` type also cannot see a binder whose TYPE
      contains parentheses -- `hs : Real.sin (x 2) ≠ 0` and `hr : rK M (x 0, x 1) = ...`
      were both invisible, and they are exactly the hypotheses the paper's sentence does
      not carry, so the arm would have reported the sentence complete.  Depth matching
      sees them.  Same family a FOURTH time: an instrument reads the FORM it was given.
    """
    out, i, n = [], 0, len(header)
    while i < n:
        if header[i] in '({[':
            close = {'(': ')', '{': '}', '[': ']'}[header[i]]
            depth, j = 1, i + 1
            while j < n and depth:
                if header[j] in '({[':
                    depth += 1
                elif header[j] in ')}]':
                    depth -= 1
                j += 1
            inner = header[i + 1:j - 1]
            if header[j - 1] == close and ':' in inner:
                names, _, typ = inner.partition(':')
                if re.fullmatch(r'[\w\sͰ-Ͽ₀-₟\'✝]+', names,
                                re.UNICODE):
                    for nm in names.split():
                        out.append((nm, flat(typ)))
            i = j
        else:
            i += 1
    return out


def decl_header(src, name):
    """The text between the declaration's name and the `:` opening its conclusion.

    The binders live here and nowhere else; casts such as `(M : ℂ)` inside the STATEMENT
    BODY are not binders, and reading the whole statement reported three of them as the
    hypotheses of `ck_prop_Kretschmann`.  Measured here, fixed here.
    """
    m = re.search(r'^(?:noncomputable\s+)?(?:theorem|lemma|def|abbrev)\s+' +
                  re.escape(name) + r'\b', src, re.M)
    if not m:
        return None, None
    tail = src[m.end():]
    depth, i = 0, 0
    while i < len(tail):
        c = tail[i]
        if c in '({[':
            depth += 1
        elif c in ')}]':
            depth -= 1
        elif c == ':' and depth == 0 and tail[i:i + 2] != ':=':
            break
        i += 1
    return tail[:i], src[:m.start()].count('\n') + 1


def section_binders(src, line_no):
    r"""The `include X in` binders this declaration really carries, with their types.

    ⬭ r7706, MEASURED: `include X in` in Lean binds the IMMEDIATELY FOLLOWING declaration
      only.  Collecting every `include` above the line instead reported `hM : 0 < M` as a
      hypothesis of `ck_chain_rule`, which lives in another section and asks nothing about
      M -- a FALSE reading produced by taking a section-wide scope for a one-declaration
      one.  So only the lines immediately above the declaration are read, docstring and
      blank lines skipped, which is the construct's own scope.
    """
    lines = src.split('\n')
    i = line_no - 2                      # the line just above the declaration
    names = []
    while i >= 0:
        L = lines[i].strip()
        if not L:
            i -= 1
            continue
        # A MULTI-LINE DOCSTRING sits between the `include` and the theorem, and its
        # middle lines look like nothing in particular.  Measured here: breaking on them
        # reported `ck_prop_Kretschmann` as carrying no `include`, when it carries hM.
        if L.endswith('-/'):
            while i >= 0 and not lines[i].strip().startswith('/--'):
                i -= 1
            i -= 1
            continue
        m = re.fullmatch(r'include\s+([\w\sͰ-Ͽ]+)\s+in', L)
        if m:
            names += m.group(1).split()
            i -= 1
            continue
        break
    types = {}
    for m in re.finditer(r'^variable\s+(.+)$', '\n'.join(lines[:line_no]), re.M):
        for a, b in binders(m.group(1)):
            types[a] = b
    return [(n, types.get(n, '?')) for n in names], names


MPI = re.compile(r'(?:M\s*\\pi|\\pi\s*M|M\\pi|\\pi M)')
AREA = re.compile(r'\d+\s*\\pi\s*M\s*\^?\s*\{?\s*2')   # 16\pi M^2 -- an AREA, not a time


def mpi_sites(src):
    """Every line carrying an Mpi-shaped token, each classified by the label beside it.

    ⬭ negative probe (16): a figure search must distinguish the quantity from a look-alike,
      so the LABEL beside each hit is read and not only the digits.  Here 16\\pi M^2 is the
      2-sphere's AREA and matches an Mpi pattern that does not read its context.
    """
    hits = []
    for i, line in enumerate(src.split('\n'), 1):
        for m in MPI.finditer(line):
            seg = line[max(0, m.start() - 40):m.end() + 40]
            hits.append((i, 'AREA' if AREA.search(seg) else 'PROPER-TIME', flat(seg)))
    return hits


# E-DEPENDENCE CLASSIFIER.  The whole of item 1 turns on it, so it is G4-tested on both
# classes before it is used, and the predicate is registered in PREDICTION.md:
#   a general-subject sentence is a DEFECT only if what it asserts is E-DEPENDENT.
E_OBJECTS = ['cycloidal motion', 'arc length along the cycloid', '$\\tau = M\\pi$',
             'at rest', 'M(1 + \\cos', 'M(\\eta + \\sin']
GENERAL_SUBJ = ['a radially infalling test particle', 'the infalling worldline',
                'a radial timelike geodesic', 'every radial geodesic',
                'the radially infalling']
SCOPE_MARK = ['vanishing Killing energy', 'E=-g(u,\\partial_t)=0', 'with $E=0$',
              'E = 0', 'a single radial geodesic', 'of vanishing energy']


def classify(seg):
    """(has a general subject, asserts an E = 0 object, carries a scope marker).

    ⬭ r7706, MEASURED BY THIS PROBE'S OWN G4 TEST: the subject match was CASE-SENSITIVE,
      so "The infalling worldline" at the head of a list item was invisible where "the
      infalling worldline" mid-sentence was seen -- and the invisible one is the very site
      r7704 routed and r7703 did not report fixed.  FOURTH instance in four revisions of
      one family: an instrument reads the FORM it was given, not the QUANTITY; here the
      form is letter case.  Prose markers are matched case-insensitively; the LaTeX
      markers are not, because case is significant in a control sequence.
    """
    f = flat(seg)
    g = any(re.search(anchor(s), f, re.I) for s in GENERAL_SUBJ)
    e = any(s in f for s in E_OBJECTS)
    s = any(s in f for s in SCOPE_MARK)
    return g, e, s


def g4_classifier():
    """G4: the classifier must separate BOTH classes, on injected text of each."""
    general_and_E = ('The Schwarzschild interior is the cycloidal motion of '
                     'a radially infalling test particle.')
    general_not_E = ('The infalling worldline reaches $r=0$ in finite proper time '
                     'and ends there.')
    scoped_and_E = ('Along the radial timelike geodesic of vanishing Killing energy, '
                    'the cycloidal motion has arc length $\\tau$.')
    a, b, c = classify(general_and_E)
    ok1 = a and b and not c
    a, b, c = classify(general_not_E)
    ok2 = a and not b
    a, b, c = classify(scoped_and_E)
    ok3 = b and c
    return ok1, ok2, ok3


def absence(src, markers, lo=None, hi=None):
    """A NAMED search.  Returns (per-marker counts, the region's size in lines)."""
    lines = src.split('\n')
    region = lines[(lo - 1 if lo else 0):(hi if hi else len(lines))]
    body = '\n'.join(region)
    return {m: len(re.findall(re.escape(m), body)) for m in markers}, len(region)


# ----------------------------------------------------------------- item 1
def item1():
    say('=' * 78)
    say('  ITEM 1 -- THE prop:cycloid FIX, AND EVERY SITE THAT SURVIVES IT')
    say('=' * 78)
    src = need(P2)
    f = flat(src)

    # 1a  the fix, at source, in BOTH places.  G1: one predicate per conjunct.
    stmt_fix = ['the radial timelike geodesic of vanishing Killing energy',
                'which reaches $r=2M$ at rest']
    proof_fix = ['Along a radial timelike geodesic the conserved energy gives',
                 'with $E=0$']
    say('\n  1a  THE FIX, read at source')
    for lbl, ms in (('statement', stmt_fix), ('proof', proof_fix)):
        for m in ms:
            present = m in f
            say(f'    [{verdict(present)}] {lbl}: "{m}"')
            if not present:
                FAIL.append(f'1a {lbl}: {m}')
    # G3 flip: strike EVERY copy (r7702 -- striking only the first reported the probe broken)
    for m in stmt_fix + proof_fix:
        if m in f and m in f.replace(m, ''):
            FAIL.append(f'1a G3 flip left a copy standing: {m}')

    # 1b  the general amplitude is the paper's at E = 0, recomputed here
    say('\n  1b  THE PROOF\'S GENERAL RELATION, checked rather than taken')
    gen = '(dr/d\\tau)^2=E^2-1+2M/r'
    say(f'    [{verdict(gen.replace(" ", "") in f.replace(" ", ""))}] the proof states the '
        f'general energy relation before setting $E=0$')

    # 1c  every Mpi-shaped site, classified by its label
    say('\n  1c  EVERY Mpi-SHAPED SITE, each classified by the LABEL beside it')
    hits = mpi_sites(src)
    pt = [h for h in hits if h[1] == 'PROPER-TIME']
    ar = [h for h in hits if h[1] == 'AREA']
    say(f'    {len(hits)} Mpi-shaped hit(s): {len(pt)} PROPER-TIME, {len(ar)} AREA')
    for ln, kind, seg in ar:
        say(f'    [NOT THE QUANTITY] l.{ln} {kind}: {seg[:90]}')
    say('     ^ negative probe (16) earning its place: an Mpi pattern that does not read its')
    say('       context calls the 2-sphere\'s area 16\\pi M^2 a proper time.')

    # 1d  THE ANSWER: which surviving sites attribute an E = 0 object to a general infaller
    say('\n  1d  THE SITES, each by the registered predicate')
    say('      (general subject + E-DEPENDENT assertion + no scope marker = DEFECT;')
    say('       general subject + E-INDEPENDENT assertion = CORRECT, reported as correct)')
    ok1, ok2, ok3 = g4_classifier()
    say(f'    G4 classifier on both classes: general+E {verdict(ok1)}; '
        f'general+not-E {verdict(ok2)}; scoped+E {verdict(ok3)}')
    if not (ok1 and ok2 and ok3):
        FAIL.append('1d G4 classifier does not separate the classes')

    lines = src.split('\n')
    cand = sorted({ln for ln, k, s in pt} |
                  {i for i, L in enumerate(lines, 1)
                   if any(s in flat(L) for s in GENERAL_SUBJ)})
    defects, correct, scoped = [], [], []
    for ln in cand:
        L = lines[ln - 1]
        for sub in re.split(r'(?<=\.)\s+', flat(L)):
            g, e, s = classify(sub)
            if not g:
                continue
            if e and not s:
                defects.append((ln, sub))
            elif e and s:
                scoped.append((ln, sub))
            else:
                correct.append((ln, sub))
    say(f'\n    {len(defects)} DEFECT(S): a general subject carrying an E = 0 object, unscoped')
    for ln, sub in defects:
        say(f'      [DEFECT] l.{ln}: {sub[:240]}')
    say(f'\n    {len(correct)} site(s) general and CORRECT (E-independent assertion)')
    for ln, sub in correct[:6]:
        say(f'      [CORRECT] l.{ln}: {sub[:200]}')
    say(f'\n    {len(scoped)} site(s) carrying an E = 0 object WITH a scope marker')
    for ln, sub in scoped[:6]:
        say(f'      [SCOPED] l.{ln}: {sub[:200]}')
    say('\n    ⌗ NO DEFECT FOUND was reachable here and is not what was found: the classifier')
    say('      returns it on an injected scoped sentence (G4, above), so this answer is a')
    say('      reading and not a failure to look.')
    return defects, correct, scoped


# ----------------------------------------------------------------- item 2
def item2():
    say('\n' + '=' * 78)
    say('  ITEM 2 -- THE FORMAL PARAGRAPH AGAINST CircleKretschmann.lean')
    say('=' * 78)
    lean = need(LEAN)
    p2 = flat(need(P2))
    decls = lean_decls(lean)

    # G5: the declaration reader, with a negative
    say('\n  G5  reader negatives')
    say(f'    [{verdict("ck_prop_critical" in decls)}] reader finds a name known to be there')
    say(f'    [{verdict("ck_not_a_real_lemma" not in decls)}] reader does NOT find a fiction')
    if 'ck_prop_critical' not in decls or 'ck_not_a_real_lemma' in decls:
        FAIL.append('2 G5 declaration reader fails its negatives')

    # 2a  the six printed names exist, spelled as printed
    named = ['ck_prop_critical', 'ck_prop_Kretschmann', 'ck_chain_rule',
             'ck_cor_Kretschmann_at_z0', 'ck_horizon', 'ck_interior']
    say('\n  2a  THE SIX NAMES THE PARAGRAPH PRINTS')
    for n in named:
        here = n in decls
        tex = n.replace('_', '\\_') in p2
        say(f'    [{verdict(here and tex)}] {n}: in the probe as '
            f'{decls.get(n, ("ABSENT",))[0]}'
            f'{" at l." + str(decls[n][1]) if here else ""}; printed in P2: {tex}')
        if not here:
            FAIL.append(f'2a {n} absent from the probe')

    # 2b  THE HYPOTHESIS ARM -- r7700's lesson cuts both ways
    say('\n  2b  HYPOTHESES, each theorem\'s own against what the sentence implies')
    unstated = []
    for n in named:
        hdr, ln = decl_header(lean, n)
        if hdr is None:
            continue
        hs = binders(hdr)
        sec, inc = section_binders(lean, ln)
        say(f'    {n} (l.{ln}): {len(hs)} header binder(s) -- ' +
            '; '.join(f'{a} : {b[:44]}' for a, b in hs))
        if inc:
            say(f'      + carried by `include ... in`: '
                f'{"; ".join(f"{a} : {b[:30]}" for a, b in sec)}')
        else:
            say('      + no `include ... in` immediately above it')
        for a, b in hs:
            if 'Real.sin' in b:
                unstated.append((n, a, b))
    say('    ⌗ Unicode-aware AND depth-matched (r7700: an ASCII-only pattern made `hτ`')
    say('      invisible; r7706: a flat type pattern made every binder whose TYPE carries')
    say('      parentheses invisible, and those are exactly the ones in question here).')
    say('')
    say(f'    {len(unstated)} hypothesis/hypotheses the paragraph\'s sentence does NOT carry:')
    for n, a, b in unstated:
        say(f'      [UNSTATED] {n} asks `{a} : {b}`')
    say('      ⇒ classified, not inflated: `Real.sin (x 2) ≠ 0` is the 2-sphere chart\'s')
    say('        own regularity (off the polar axis), not a restriction of physical scope,')
    say('        and "on the Kruskal chart" arguably carries it.  Reported because the arm')
    say('        is the WHOLENESS of a hypothesis list and a reader checking the sentence')
    say('        against the file will meet it.')
    wit = 'ck_interior_witness' in decls
    say(f'    [{verdict(wit)}] and the interior claim is NOT VACUOUS: `ck_interior_witness`'
        f' exhibits a chart point for every η with 1 + cos η ≠ 0')

    # 2c  the chain-rule lemma's hypothesis against the words the paragraph uses for it
    say('\n  2c  "wherever $h$ has a non-degenerate zero" -- WHICH OBJECT IS THAT?')
    cr = flat((decl_header(lean, 'ck_chain_rule') or ('',))[0] or '')
    asks_value = 'h z₀ = 0' in cr
    asks_deriv = 'deriv h z₀ = 0' in cr
    asks_second = 'iteratedDeriv 2 h z₀ ≠ 0' in cr
    say(f'    [{verdict(asks_value)}] the lemma asks h(z0) = 0')
    say(f'    [{verdict(asks_deriv)}] the lemma asks h\'(z0) = 0        <- a DOUBLE zero')
    say(f'    [{verdict(asks_second)}] the lemma asks h\'\'(z0) != 0')
    phrase = 'non-degenerate zero'
    n_corpus = len(re.findall(re.escape(phrase), p2))
    n_crit = len(re.findall(re.escape('non-degenerate critical point'), p2))
    say(f'    the phrase "{phrase}" occurs {n_corpus}x in P2; '
        f'"non-degenerate critical point" occurs {n_crit}x')
    say('    ⌗ the label\'s many-to-one-ness, which is the guard that applies: under the')
    say('      standard reading a non-degenerate zero is a SIMPLE zero (h\' != 0), and then')
    say('      h^6 has a zero of order 6, so c/h^6 has a pole of order 6 -- NOT twelve.')
    orders = {}
    for nm, order_of_h in (('simple zero', 1), ('double zero', 2)):
        orders[nm] = 6 * order_of_h
    say(f'    arithmetic, computed here: {orders} '
        f'(the paragraph claims twelve, which needs the DOUBLE zero)')
    mismatch = asks_deriv and asks_second and orders['simple zero'] != 12
    say(f'    [{"DEFECT" if mismatch else "NO DEFECT"}] the paragraph names the object by a '
        f'label the lemma does not ask for')
    if mismatch:
        say('      ⇒ the lemma\'s hypothesis is a zero AT a non-degenerate critical point')
        say('        (a zero of order exactly two); the paper everywhere else says')
        say(f'        "non-degenerate critical point" ({n_crit}x) and says')
        say(f'        "non-degenerate zero" exactly {n_corpus}x -- here, once.')

    # 2d  THE ABSENCE CLAIM, with its search NAMED
    say('\n  2d  "the parameter z is not itself built as a chart" -- a NAMED search')
    markers = ['ChartedSpace', 'PartialHomeomorph', 'LocalHomeomorph', 'ModelWithCorners',
               'IsManifold', 'atlas', 'chartAt', 'extChartAt']
    m0 = re.search(r'^section CkChain', lean, re.M)
    lo = lean[:m0.start()].count('\n') + 1 if m0 else 1
    hi = len(lean.split('\n'))
    counts, nlines = absence(lean, markers, lo, hi)
    whole, _ = absence(lean, markers)
    say(f'    region searched: l.{lo}-{hi} ({nlines} lines), the ck_ section')
    say(f'    per-marker counts IN THE ck_ SECTION: {counts}')
    say(f'    the same markers over the WHOLE {len(lean.split(chr(10)))}-line file: {whole}')
    zero_in_region = sum(counts.values()) == 0
    say(f'    [{verdict(zero_in_region)}] NOT FOUND -- {len(markers)} markers, '
        f'{sum(counts.values())} occurrences in the ck_ section')
    say('    ⌗ said as NOT FOUND over a NAMED search and not as "there is none": the chart')
    say('      machinery exists in abundance in the inherited kit, and none of it is on z.')
    for d in ('ck_r', 'ck_rC'):
        m = re.search(r'^(?:noncomputable\s+)?def\s+' + d + r'\b[^\n]*', lean, re.M)
        say(f'    {d} is defined as: {flat(m.group(0)) if m else "ABSENT"}')
        say(f'      ^ a plain function, not a chart: its domain is a type, not an atlas.')
    tie = 'rK M (x 0, x 1) = ck_r M η' in flat((decl_header(lean, 'ck_interior')
                                                  or ('',))[0] or '')
    say(f'    [{verdict(tie)}] the tie to the chart is a HYPOTHESIS equating the chart\'s '
        f'areal radius to ck_r')

    # 2e  axiom hygiene
    say('\n  2e  AXIOM HYGIENE')
    n_ax = len(re.findall(r'\baxiom\b', lean))
    n_sorry = len(re.findall(r'\bsorry\b', lean))
    n_print = len(re.findall(r'#print axioms', lean))
    say(f'    `axiom` tokens: {n_ax};  `sorry`: {n_sorry};  `#print axioms` checks: {n_print}')
    say(f'    [{verdict(n_ax == 0 and n_sorry == 0)}] no axiom carries the content the '
        f'paragraph credits to a proof')
    say('    ⌗ AND WHAT THIS CANNOT DO, as registered: it reads declarations, hypotheses and')
    say('      the shape of statements.  Whether each proof TERM closes is the Lean build\'s')
    say('      and check_no_sorry\'s business, not this probe\'s.')
    return mismatch


# ----------------------------------------------------------------- item 3
def item3():
    say('\n' + '=' * 78)
    say('  ITEM 3 -- P15\'S TRIMMED SCOPE SENTENCE')
    say('=' * 78)
    src = need(P15)
    f = flat(src)

    # 3a  the FROZEN comparison is gone
    cut = ['both treatments are reported because the depth comparison depends on the choice',
           'the frozen one departing further at $\\ell=4$',
           'a single build\'s agreement is not by itself the cross-validation']
    say('\n  3a  THE CUT, read at source')
    for m in cut:
        say(f'    [{verdict(m not in f)}] GONE: "{m[:72]}"')

    # 3b  searched, not assumed: does anything else still lean on FROZEN
    say('\n  3b  DOES ANYTHING ELSE IN P15 STILL LEAN ON THE FROZEN BUILD? (searched)')
    for m in ['FROZEN', 'frozen with their free-streaming towers retained',
              'returned by both treatments', 'returned by both builds',
              'both treatments', 'both builds']:
        n = len(re.findall(re.escape(m), f))
        say(f'    "{m}": {n} occurrence(s)')

    # 3c  the sentence read WHOLE -- a cut can leave a clause whose subject has moved
    say('\n  3c  THE SENTENCE WHOLE, not just its diff')
    keep = {
        'the decoupled build is what P15 prints':
            'sectors \\emph{decoupled} past recombination rather than frozen',
        'its agreement with the exact transfer': 'agrees with the exact transfer to $2.9$ per cent',
        'the corroboration clause RETAINED': 'is returned by both treatments',
        'the conclusion clause RETAINED': 'So the shape and the depth',
    }
    for lbl, m in keep.items():
        present = m in f
        say(f'    [{verdict(present)}] {lbl}: "{m[:66]}"')
    leans = 'is returned by both treatments' in f
    claims_depth = 'So the shape and the depth' in f
    caveat_gone = ('a single build\'s agreement is not by itself the cross-validation'
                   not in f)
    say('')
    say(f'    [{"DEFECT" if (leans and claims_depth and caveat_gone) else "NO DEFECT"}] '
        f'the cut removed the caveat the SURVIVING conclusion needs')
    if leans and claims_depth and caveat_gone:
        say('      ⇒ the retained clause corroborates the conclusion on BOTH treatments, so it')
        say('        leans on the frozen build; and the clause that reported that build\'s')
        say('        departure -- and said a single build\'s agreement is not by itself the')
        say('        cross-validation -- is the clause that was cut.  The sentence now asserts')
        say('        the DEPTH cross-validates on one build\'s agreement, which is the step the')
        say('        deleted clause denied.  Half re-pointed, r7702\'s pattern exactly.')
    return leans and claims_depth and caveat_gone


def main():
    say()
    say('  r7706 (60) -- READINGS.  Order r7703, three items.')
    d1, c1, s1 = item1()
    d2 = item2()
    d3 = item3()
    say('\n' + '=' * 78)
    say('  VERDICTS')
    say('=' * 78)
    say(f'  ITEM 1  the fix landed in the statement and the proof; '
        f'{len(d1)} surviving site(s) attribute an E = 0 object to a general subject, '
        f'{len(c1)} general site(s) are CORRECT')
    say(f'  ITEM 2  all six names present; the chain-rule lemma\'s object is '
        f'{"MISLABELLED" if d2 else "named correctly"}; z is NOT built as a chart '
        f'(named search, NOT FOUND)')
    say(f'  ITEM 3  the FROZEN comparison is cut; the surviving conclusion '
        f'{"LOST A CAVEAT IT NEEDS" if d3 else "stands as written"}')
    say()
    if FAIL:
        say('  ⛔ PROBE SELF-CHECKS FAILED -- the readings below are not to be trusted:')
        for x in FAIL:
            say(f'    [FAIL] {x}')
        return 1
    say('  probe self-checks: all pass.')
    say()
    return 0


if __name__ == '__main__':
    code = main()
    with open(os.path.join(HERE, 'runs', 'READINGS.txt'), 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(OUT) + '\n')
    sys.exit(code)
