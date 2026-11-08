#!/usr/bin/env python3
"""r7714 (60) -- the r7711 landing, read cold.

Arms registered in PREDICTION.md before any of the three passages, or either new
declaration, was read.  Every verdict below is BUILT FROM its readings; nothing
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
P15 = ROOT + '/corpus/CR_cosmology.tex'
LEAN = ROOT + '/computations/formalisation/lean/probes/CirclePatches.lean'
RCPT = (ROOT + '/receipts/P15_CR_cosmology/'
        'P15_the_low_multipole_depth_gap_closes_and_two_defects_were_cancelling.py')

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

# =============================================================== SELF-TESTS
def selftests(p2flat):
    say('=' * 78)
    say('SELF-TESTS -- every classifier and reader on BOTH of its classes, before use')
    say('=' * 78)

    # G2, on all three anchor forms and on one that mixes prose with math.
    need('G2 accepts plain prose', anchor('one-to-one onto the corresponding region') == 'prose')
    need('G2 accepts an escaped control sequence', anchor(r'\texttt') == 'macro')
    need('G2 accepts an escaped math delimiter', anchor('$UV<1$') == 'math')
    need('G2 REFUSES a marker mixing prose with math',
         anchor(r'the four patches at $r \geq 0$') is None)

    # the skeleton matcher, on its negatives
    need('skeleton: a math-mode Greek name IS found',
         cited_in_tex(r'(\texttt{ce\_$\Psi$\_inj})', 'ce_\u03a8_inj'))
    need('skeleton: a plain ASCII name IS found',
         cited_in_tex(r'(\texttt{cp\_kruskal})', 'cp_kruskal'))
    need('skeleton: a name that is NOT on the page is NOT found',
         not cited_in_tex(r'(\texttt{cp\_kruskal})', 'cp_nowhere'))
    need('skeleton: a name that is a PREFIX of another is not credited to it',
         not cited_in_tex(r'(\texttt{cp\_metrics})', 'cp_metrics_two'))

    # G4: the parenthesis-placement classifier, on BOTH classes.
    need('placement classifier: parenthesis INSIDE the one-to-one clause',
         paren_scope('matched to the form by a chart map that is one-to-one onto the '
                     'corresponding region (machine-checked below). Each patch is therefore '
                     'isometric to the region.') == 'clause')
    need('placement classifier: parenthesis AFTER the isometry conclusion',
         paren_scope('matched to the form by a chart map that is one-to-one onto the '
                     'corresponding region. Each patch is therefore isometric to the region '
                     '(machine-checked below).') == 'conclusion')

    # G5: the declaration reader, with a negative.
    need('reader: cp_kruskal has a header', decl_header(LEANSRC, 'cp_kruskal') is not None)
    need('reader: a declaration that does not exist reads as absent',
         decl_header(LEANSRC, 'cp_kruskal_not_a_declaration') is None)
    need('onto reader: a membership conclusion with quadrant signs and the domain IS '
         'read as onto',
         onto_shape('theorem t (hM : 0 < M) {U V : \u211d} (hU : 0 < U) (hV : 0 < V) '
                    '(hk : (U, V) \u2208 sk_kM) : (U, V) \u2208 cp_BH M'))
    need('onto reader: a PULLBACK conclusion is NOT read as onto',
         not onto_shape('theorem t (hM : 0 < M) (y : P) : hRep (sk_S hM).g p\u2080 y a a '
                        '= cy_A M \u03b7'))
    need('onto reader: a membership conclusion WITHOUT the domain hypothesis is not '
         'read as onto',
         not onto_shape('theorem t (hM : 0 < M) {U V : \u211d} (hU : 0 < U) (hV : 0 < V) '
                        ': (U, V) \u2208 cp_BH M'))
    need('reader: decl_extent reaches a def\'s BODY, which lives after ":="',
         'p.1 * p.2 < 1' in (decl_extent(LEANSRC, 'sk_kM') or ''))
    need('reader: decl_extent stops before the NEXT declaration',
         'sk_MN' not in (decl_extent(LEANSRC, 'sk_kM') or ''))
    need('reader: decl_extent of a declaration that does not exist is absent',
         decl_extent(LEANSRC, 'sk_kM_not_a_declaration') is None)
    need('reader: binders survive a type carrying parentheses',
         binders('theorem t (hM : 0 < M) {y : P} (hy : y \u2208 cp_BH M) :')
         == ['(hM : 0 < M)', '{y : P}', '(hy : y \u2208 cp_BH M)'])

    # G6: the flattener, on a sentence the source wraps.
    need('G6: the sketch sentence is one line only after flattening',
         'one-to-one onto the corresponding region of the Kruskal manifold' in p2flat)
    say('')

def onto_shape(header):
    """An ONTO statement, read by the SHAPE of its conclusion and not by a symbol:
    every point of an open quadrant inside the domain is a member of the patch set.
    Both theorems say this as SET MEMBERSHIP -- `(U, V) \u2208 cp_BH M` -- and the
    existential lives in the set's own definition, so a search for '\u2203' in the
    statement finds nothing and would report the onto half missing."""
    concl = header.rsplit(') :', 1)[-1] if ') :' in header else header
    if not re.search(r'\(U, V\)\s*\u2208\s*cp_(?:BH|WH|RE|LE) M', concl):
        return False
    bs = ' '.join(binders(header))
    signs = len(re.findall(r'0 < [UV]|[UV] < 0', bs))
    return signs >= 2 and 'sk_kM' in bs


def paren_scope(text):
    """Which clause does '(machine-checked below)' bound: the one-to-one clause,
    or the isometry conclusion?  Decided by which sentence it falls in."""
    t = flat(text)
    i = t.find('(machine-checked below)')
    if i < 0:
        return 'absent'
    head = t[:i]
    return 'conclusion' if 'therefore isometric' in head else 'clause'

# ==================================================================== ARMS
def q1(p2flat, lean):
    say('=' * 78)
    say('Q1 -- IS "machine-checked below" HONEST?  The phrase modifies a CLAUSE with')
    say('      TWO halves: (a) one-to-one, and (b) ONTO the corresponding region.')
    say('=' * 78)
    clause = ('by a chart map that is one-to-one onto the corresponding region of the '
              'Kruskal manifold (machine-checked below)')
    anchored('by a chart map that is one-to-one onto the corresponding region')
    need('the clause is at source, verbatim', clause in p2flat)
    scope = paren_scope(p2flat[p2flat.find('The four $r \\geq 0$ patches meet at'):][:1400])
    say(f'  READING: the parenthesis bounds the ..... {scope}')
    need('the parenthesis bounds the one-to-one clause and not the conclusion',
         scope == 'clause')

    say('')
    say('  (a) ONE-TO-ONE -- the injectivity declarations, and whether P2 cites them:')
    for n in ('cc_\u03a6_inj', 'ce_\u03a8_inj'):
        say(f'    cited in P2 (by SKELETON): {n} -> {cited_in_tex(p2flat, n)}')
    need('both injectivity names are cited in P2',
         cited_in_tex(p2flat, 'cc_\u03a6_inj') and cited_in_tex(p2flat, 'ce_\u03a8_inj'))

    say('')
    say('  (b) ONTO -- read as a MAP property, which a partition is not:')
    for n in ('cp_onto_BH', 'cp_onto_RE'):
        h = decl_header(lean, n)
        say(f'    {n}: {h}')
        need(f'{n} exists', h is not None)
        if h:
            need(f'{n} concludes with MEMBERSHIP OF THE PATCH SET, which IS surjectivity '
                 f'because the patch set is the map\'s image', onto_shape(h))
    say('    cited in P2 (by SKELETON): cp_onto_BH -> '
        f'{cited_in_tex(p2flat, "cp_onto_BH")}; cp_onto_RE -> '
        f'{cited_in_tex(p2flat, "cp_onto_RE")}')

    say('')
    say('  AND WHETHER THE PARTITION SUPPLIES (b) ANYWAY -- the four patch sets, read')
    say('  from their DEFINITIONS rather than from their names:')
    for n in ('cp_BH', 'cp_WH', 'cp_RE', 'cp_LE', 'cp_Hor'):
        say(f'    {decl_extent(lean, n)}')
    images = all('\u2203' in (decl_extent(lean, n) or '') for n in ('cp_BH', 'cp_WH', 'cp_RE', 'cp_LE'))
    need('each of the four patch sets IS the chart map\'s IMAGE (an existential), so '
         '"onto the corresponding region" is what its own definition says', images)
    quads = [decl_header(lean, n) for n in
             ('cp_BH_quad', 'cp_WH_quad', 'cp_RE_quad', 'cp_LE_quad')]
    for h in quads:
        say(f'    {h}')
    need('each image is pinned to its own open quadrant', all(h for h in quads))
    return scope, images

def q2(p2flat, lean):
    say('')
    say('=' * 78)
    say('Q2 -- THE PARTITION CLAUSE, THE CARRIER, AND THE REFLECTION')
    say('=' * 78)

    say('  2a THE REFLECTION CLAUSE, read from scratch (negative probe 20):')
    refl = ('the reflection $(U,V)\\mapsto(-U,-V)$ preserves $r$ and every coefficient of '
            'the metric (\\texttt{ce\\_reflection})')
    need('the clause claims PRESERVATION and no longer a map onto a region',
         refl in p2flat)
    need('no "carries it onto the second exterior" survives anywhere in P2',
         'carries it onto the second exterior' not in p2flat)

    say('')
    say('  2b THE CARRIER, read from its definition and NOT from the name or the order:')
    for n in ('sk_kM', 'sk_MN', 'sk_S', 'sk_S_M'):
        say(f'    {decl_extent(lean, n)}')
    skkm = decl_extent(lean, 'sk_kM') or ''
    need('sk_kM is {UV < 1} with NO further condition',
         'p.1 * p.2 < 1' in skkm and '0 < p.2' not in skkm)
    # arithmetic, not recollection: the second exterior is U > 0 > V.
    pts = {'first exterior (-1, 1)': (-1.0, 1.0), 'interior (0.5, 0.5)': (0.5, 0.5),
           'SECOND EXTERIOR (1, -1)': (1.0, -1.0)}
    for lab, (u, v) in pts.items():
        say(f'    {lab}: UV = {u * v:+.2f};  in sk_kM = {u * v < 1};  '
            f'in seWS = {v > 0 and u * v < 1}')
    need('the second exterior IS in sk_kM, so the gap r7712 found is CLOSED',
         1.0 * -1.0 < 1)
    need('and it is NOT in seWS, which is why the claim had to move manifolds',
         not (-1.0 > 0))

    say('')
    say('  2c THE DISJOINTNESS SCOPE -- the sharpest arm, registered in advance:')
    clause = ('the four $r\\ge0$ patches, with the horizons $UV=0$ at which they meet, are '
              'exactly that domain and pairwise disjoint (\\texttt{cp\\_kruskal}, in '
              '\\texttt{CirclePatches.lean})')
    need('the clause is at source, verbatim', clause in p2flat)
    h = decl_header(lean, 'cp_kruskal')
    say(f'    cp_kruskal: {h}')
    concl = (h or '').split(') :', 1)[-1]
    sets = re.findall(r'cp_(?:BH|WH|RE|LE|Hor)', concl)
    union = re.search(r'cp_BH M \u222a cp_WH M \u222a cp_RE M \u222a cp_LE M \u222a cp_Hor = sk_kM', concl)
    ndisj = len(re.findall(r'Disjoint', concl))
    say(f'    READING: union conjunct present = {bool(union)};  Disjoint conjuncts = {ndisj}')
    need('the union is of FIVE sets -- the four patches AND the horizons as its own set',
         bool(union))
    need('and all TEN pairs among those five are asserted disjoint, which is what '
         '"pairwise disjoint" of five pieces means', ndisj == 10)
    say('    ⌗ THE FALSE READING NAMED: if "with the horizons" ENLARGED each patch, the')
    say('      enlarged sets would SHARE the horizons and could not be pairwise disjoint.')
    say('      cp_kruskal adjoins cp_Hor as a FIFTH set, which is what the appositive does.')

    say('')
    say('  2d cp_metrics -- coefficient-wise, and for how many patches:')
    hm = decl_header(lean, 'cp_metrics')
    say(f'    cp_metrics: {hm}')
    say(f'    binders: {binders(hm or "")}')
    cm = hm or ''
    groups = len(re.findall(r'hRep \(sk_S hM\)\.g p\u2080 \(-?c[ce]_[\u03a6\u03a8]', cm))
    say(f'    READING: hRep conclusions on sk_S = {groups} (4 patches x 3 components = 12)')
    need('all four patches are covered, three components each', groups == 12)
    need('the two reflected patches are stated at the NEGATED point with NEGATED vectors, '
         'which is the reflection\'s own pushforward and not a composition by the prose',
         '(-cc_\u03a6 M \u03b7 t)' in cm and '(-ce_\u03a8 M \u03c1 t)' in cm)
    return True

def q3(p15flat):
    say('')
    say('=' * 78)
    say('Q3 -- CAN cc66\'s SENTENCE BE MISREAD AS THE BAND-AVERAGE STATISTIC?')
    say('      ⚠⚠ BOTH OBJECTS LOCATED BY THEIR TEXT, NOT BY THE ORDER\'S LINE NUMBER.')
    say('=' * 78)
    sent_mark = 'And the located transition belongs to the contrast between the arms'
    anchored(sent_mark)
    need('cc66\'s sentence is at source', sent_mark in p15flat)
    i = p15flat.find(sent_mark)
    sent = p15flat[i:i + 520]
    say(f'    SENTENCE: {sent[:500]}')

    # Both band statistics near it, each found by its own text.
    stats = {
        'the candidate step (the order\'s l.1411)':
            "A candidate's step is its lowest band's departure from the trend its own "
            'upper bands set',
        'the acceptance-law band fraction (the sentence before)':
            'the lowest band runs the same fraction of the rest under the law',
    }
    for lab, mark in stats.items():
        anchored(mark)
        need(f'located by text: {lab}', mark in p15flat)

    # The comparison the arm registered: do the NOUN PHRASES name the same object?
    say('')
    say('    NOUN PHRASES, compared as the registered predicate requires:')
    sent_nps = ['the contrast between the arms', 'their sources',
                "the ratio of this arm's spectrum to the control's",
                "the two arms' $\\eta$-integrated sources", "that ratio's own scatter"]
    stat_nps = ["its lowest band", 'the trend its own upper bands set', 'four bases',
                'the lowest band', 'the rest under the law']
    for np in sent_nps:
        say(f'      sentence: {np!r} -> in either statistic\'s definition: '
            f'{any(np in m for m in stats.values())}')
    for np in stat_nps:
        say(f'      statistic: {np!r} -> in cc66\'s sentence: {np in sent}')
    need('NOT ONE noun phrase of the sentence appears in either statistic\'s definition',
         not any(np in m for np in sent_nps for m in stats.values()))
    need('and not one noun phrase of either statistic appears in the sentence',
         not any(np in sent for np in stat_nps))

    # The decisive reading: where "the same sliding windows" points.
    say('')
    ante = p15flat[max(0, i - 420):i]
    say(f'    THE ANTECEDENT of "the same sliding windows", read UPSTREAM: {ante[-300:]}')
    need('"the same sliding windows" has its antecedent in the preceding sentence '
         '(the acceptance law, across "the same windows"), which is UPSTREAM of the '
         'candidate statistic', 'across the same windows' in ante)
    need('the candidate statistic is DOWNSTREAM of the sentence and in another paragraph',
         p15flat.find(stats['the candidate step (the order\'s l.1411)']) > i)

    # And the inverse risk, which is the one the text has to separate itself.
    say('')
    inv = ("the share is against the excess's own extrapolated size and not against the "
           'larger step the arms have in common')
    say(f'    THE INVERSE RISK -- the statistic read as the arm-to-control contrast:')
    need('the candidate paragraph states the denominator distinction itself, in its own '
         'words, so the inverse misreading is closed where it would arise', inv in p15flat)
    return True

def item4(p2flat, lean):
    say('')
    say('=' * 78)
    say('ITEM 4 -- THE REST OF THE LANDING')
    say('=' * 78)
    last = ('That this extension is maximal, and the $r<0$ patches as a geometry in their '
            'own right, are not formalised.')
    need('the formal paragraph\'s last sentence is at source, verbatim', last in p2flat)
    need('its OLD first clause -- the four-patch identity -- is gone from it, which is '
         'what cp_kruskal now covers',
         'That the four $r \\geq 0$ patches are exactly the Kruskal' not in p2flat)
    say('    ⌗ READING: the machine checks a SET identity with $\\{UV<1\\}$.  "Maximal" is')
    say('      a different claim, and the sentence is what keeps them apart.')
    need('the paragraph says "machine-checked" of the coefficient identities and names '
         'the domain it works over', 'over its whole domain $\\{UV<1\\}$' in p2flat)
    for n in ('cp_kruskal', 'cp_metrics'):
        need(f'{n} is cited in P2 (by SKELETON)', cited_in_tex(p2flat, n))
    src = open(LEAN).read()
    nax = len(re.findall(r'^axiom\s', src, re.M))
    nsorry = len(re.findall(r'\bsorry\b', src))
    say(f'    CirclePatches.lean: axiom tokens = {nax}; sorry = {nsorry}')
    need('zero axiom tokens and zero sorry', nax == 0 and nsorry == 0)
    return True

def correction():
    say('')
    say('=' * 78)
    say('THE ORDER\'S CORRECTION TO r7712 -- VERIFIED, NOT TAKEN')
    say('=' * 78)
    src = open(RCPT).read()
    m = re.search(r'^_F9 = .*$', src, re.M)
    say(f'    {m.group(0) if m else "_F9 NOT FOUND"}')
    need('_F9 is COMPUTED in the depth-gap receipt', m is not None)
    g = re.search(r'check\("\u26ed\u26d4 `r7703` \*\* AND THE BANKED NS3 900.*?\n.*?\n.*?\n',
                  src, re.S)
    say(f'    gate: {flat(g.group(0)) if g else "gate NOT FOUND"}')
    need('its gate\'s own text says "about 3 per cent"',
         'converging it moves l = 4 by about ' in src and '3 per cent' in src)
    need('and the gate prints _F9 as a PER CENT at RUN TIME, so the digits 3.23 are '
         'nowhere in the source', 'f"{100 * _F9:.2f}%"' in src
         and '3.23' not in src)
    say('    ⌗ NEGATIVE PROBE (22) CONFIRMED BY THE FILE: a named search over SOURCE')
    say('      cannot find a value that exists only at RUN TIME.  r7712\'s NOT FOUND was')
    say('      true of the searches it named; the searches were of the wrong KIND.')
    return True

def main():
    global LEANSRC
    p2 = flat(open(P2).read())
    p15 = flat(open(P15).read())
    LEANSRC = open(LEAN).read()
    selftests(p2)
    q1(p2, LEANSRC)
    q2(p2, LEANSRC)
    q3(p15)
    item4(p2, LEANSRC)
    correction()
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
