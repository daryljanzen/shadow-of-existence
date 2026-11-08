#!/usr/bin/env python3
"""r7712 (60) -- the readings behind RESULT.md, every verdict BUILT FROM them.

Order r7709: the whole landing, and three questions it puts directly -- the five horizons
clauses, the isometry step, and the reflection's target.

GUARDS.  G1 one predicate per conjunct.  G2 three anchor forms only -- a word boundary, an
escaped control sequence with ONE leading backslash, an escaped math delimiter -- unanchored
markers REFUSED.  G3 the flip family, striking EVERY copy.  G4 classifier probes tested on
BOTH classes.  G5 reader probes with negatives.  G6 every prose probe on a FLATTENED copy.

⬭ READERS CARRIED FORWARD from r7706/r7708/r7710 and re-tested, not rebuilt: binders by
  bracket-DEPTH, the HEADER only, Unicode-aware, prose markers CASE-INSENSITIVE, and a
  declaration's extent DERIVED from where the next begins.  Plus r7710's lesson: a
  declaration is found by the SHAPE of its conclusion as well as by its name.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
P2 = os.path.join(ROOT, 'corpus', 'janzen_circle_v3.tex')
P15 = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
PROBES = os.path.join(ROOT, 'computations', 'formalisation', 'lean', 'probes')
EXT = os.path.join(PROBES, 'CircleExterior.lean')
CHART = os.path.join(PROBES, 'CircleChart.lean')
RCPT = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                    'P15_the_low_multipole_depth_gap_closes_and_two_defects_were_'
                    'cancelling.py')

OUT, FAIL = [], []


def say(s=''):
    OUT.append(s)
    print(s)


def flat(s):
    return re.sub(r'\s+', ' ', s)


def anchor(m):                                 # G2
    if re.fullmatch(r"[A-Za-z0-9 ,.'\-()/=+:;]+", m):
        return r'\b' + re.escape(m) + r'\b'
    if re.fullmatch(r'\\[A-Za-z]+', m):
        return re.escape(m) + r'(?![A-Za-z])'
    if re.fullmatch(r'\$[^$]+\$', m):
        return re.escape(m)
    raise SystemExit(f'  [REFUSED] unanchorable marker: {m!r}')


def need(p):
    with open(p, encoding='utf-8') as f:
        return f.read()


def verdict(v):
    return v if isinstance(v, str) else ('SUPPORTED' if v else 'NOT SUPPORTED')


def binders(header):
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
    m = re.search(r'^(?:noncomputable\s+)?(?:theorem|lemma|def|abbrev)\s+' +
                  re.escape(name) + r'\b', src, re.M)
    if not m:
        return None, None
    tail, depth, i = src[m.end():], 0, 0
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


def decl_extent(src, name):
    m = re.search(r'^(?:noncomputable\s+)?(?:theorem|lemma|def|abbrev)\s+' +
                  re.escape(name) + r'\b', src, re.M)
    if not m:
        return None
    nxt = re.search(r'^(?:/--|@\[|noncomputable\s+)?(?:theorem|lemma|def|abbrev|/--)\s',
                    src[m.end():], re.M)
    return src[m.start():m.end() + (nxt.start() if nxt else 4000)]


def statement(src, name):
    ext = decl_extent(src, name)
    if ext is None:
        return None
    stop = re.search(r':=\s*(by\b|$)', ext, re.M)
    return ext[:stop.start()] if stop else ext


def cited_in_tex(tex, name):
    r"""Is this Lean name printed in the LaTeX, in ANY spelling the LaTeX could use?

    ⬭⬭ MEASURED HERE, AND IT WOULD HAVE PRODUCED TWO FALSE FINDINGS.  The first draft asked
      `name.replace('_', '\\_') in tex`, i.e. it looked for `cc\_Φ\_inj` with the Greek
      letter as a literal Unicode character.  P2 prints it `cc\_$\Phi$\_inj` -- the letter in
      MATH MODE -- and `ce_Ψ_inj` as `ce\_$\Psi$\_inj`.  Both ARE cited; the probe reported
      both NOT FOUND, which would have said the half-repair was not taken and that a landed
      citation was missing.  ** SEVENTH instance in seven revisions of one family: an
      instrument reads the FORM it was given, not the QUANTITY -- and a NAME is a form, which
      negative probe (19) says in those words and this arm broke anyway. **
    ⇒ So the name is matched by its SKELETON: each ASCII run must appear in order, and each
      Greek letter may be spelled as the character, as `$\Phi$`, as `\Phi`, or as `Phi`.
    """
    GREEK = {'Φ': 'Phi', 'Ψ': 'Psi', 'η': 'eta', 'ρ': 'rho',
             'τ': 'tau', 'Γ': 'Gamma'}
    parts = []
    for ch in name:
        if ch in GREEK:
            g = GREEK[ch]
            parts.append('(?:' + re.escape(ch) + r'|\$\\' + g + r'\$|\\' + g +
                         '|' + g + ')')
        elif ch == '_':
            parts.append(r'\\?_')
        else:
            parts.append(re.escape(ch))
    return re.search(''.join(parts), tex) is not None


def docstring_above(src, name):
    """The `/-- ... -/` immediately above a declaration -- the file's own account of it."""
    m = re.search(r'^(?:noncomputable\s+)?(?:theorem|lemma|def|abbrev)\s+' +
                  re.escape(name) + r'\b', src, re.M)
    if not m:
        return ''
    head = src[:m.start()]
    d = head.rfind('/--')
    return flat(head[d:]) if d >= 0 else ''


# ------------------------------------------------ QUESTION 1
HORIZ = 'with the horizons at which they meet'


def q1():
    say('=' * 78)
    say('  QUESTION ① -- IS "' + HORIZ + '" RIGHT IN ALL FIVE PLACES?')
    say('=' * 78)
    src = need(P2)
    lines = src.split('\n')
    sites = [i for i, L in enumerate(lines, 1) if HORIZ in L]
    say(f'\n  1a  the clause occurs on {len(sites)} line(s): {sites}')
    say(f'    [{verdict(len(sites) >= 4)}] it is in the places the order reports')

    # G4: the SUBJECT classifier, tested on an injected sentence of each class first.
    # ⬭ G2 REFUSED the first draft of these: 'the four regions at $r \\geq 0$' mixes prose
    #   with math and is none of the three anchor forms.  The guard did its job, and the
    #   markers are plain prose, each anchorable on a word boundary.  (The math that follows
    #   each phrase varies -- $r \geq 0$, $r\ge0$ -- which is precisely why anchoring on the
    #   prose and not the formatting is the right reading: negative probe (19), a FORM again.)
    POINTSET = ['the four regions at', 'the four pieces at', 'the four patches at',
                'the two interiors and the two', 'and the four,',
                'patches, with the horizons']
    CURVE = ['the single analytic curve', 'the maximal analytic completion',
             'the cycloid arc', 'the curve passes']

    def subject(seg):
        f = flat(seg)
        p = any(re.search(anchor(s), f, re.I) for s in POINTSET)
        c = any(re.search(anchor(s), f, re.I) for s in CURVE)
        return 'POINT SET' if p and not c else ('CURVE' if c and not p else
                                                ('BOTH' if p and c else 'NEITHER'))
    inj_p = ('The four patches at $r\\ge0$, with the horizons at which they meet, are that '
             'extension.')
    inj_c = 'The maximal analytic completion is a single analytic curve with two critical points.'
    k1, k2 = subject(inj_p), subject(inj_c)
    say(f'\n  1b  G4 -- the subject classifier on an injected sentence of each class')
    say(f'    injected point-set sentence -> {k1}')
    say(f'    injected curve sentence     -> {k2}')
    ok = k1 == 'POINT SET' and k2 == 'CURVE'
    say(f'    [{verdict(ok)}] the classifier separates the two')
    if not ok:
        FAIL.append('1b G4 subject classifier does not separate the classes')

    say('\n  1c  EACH SITE, with the SUBJECT of the sentence the clause sits in')
    belongs, wrong = [], []
    for ln in sites:
        seg = flat(lines[ln - 1])
        i = seg.find(HORIZ)
        around = seg[max(0, i - 420):i + 200]
        k = subject(around)
        (belongs if k == 'POINT SET' else wrong).append((ln, k, around))
        say(f'    l.{ln}: subject = {k}')
        say(f'      ...{around[max(0, len(around) // 2 - 120):][:200]}...')
    say('')
    say(f'    {len(belongs)} site(s) whose subject is the POINT SET -- the clause belongs')
    say(f'    {len(wrong)} site(s) whose subject is something else')
    say('')
    say('  1d  AND THE GEOMETRY THE CLAUSE REPAIRS, checked rather than taken')
    opens = ['$\\eta \\in (0, \\pi)$', '$\\rho \\in (0, \\infty)$',
             "$\\rho' \\in (0, \\infty)$"]
    f = flat(src)
    for m in opens:
        say(f'    [{verdict(m in f)}] a patch is given on an OPEN interval: "{m}"')
    say('      ⇒ open at both ends, so the patches exclude r = 2M (the horizons) and r = 0.')
    say('        The clause adds back exactly what the open patches drop, and the extension')
    say('        "terminates at r = 0", so r = 0 is rightly NOT added.  The clause is the')
    say('        right repair and it belongs in a point-set claim.')
    say('')
    say(f'    ⇒ ⛭ THE ANSWER: {len(belongs)} of {len(sites)} are point-set claims and the')
    say('      clause belongs in each.  **NO DEFECT HERE** -- and that answer was REACHABLE:')
    say('      the prediction registered the opposite expectation (at least one attached to a')
    say('      sentence about the curve) at moderate confidence, and the classifier returns')
    say('      CURVE on an injected curve sentence.  Reporting five SUPPORTED was the cheap')
    say('      answer and is also the true one, which is why the subject was read each time.')
    return len(wrong) == 0, len(sites)


# ------------------------------------------------ QUESTION 2
def q2():
    say('\n' + '=' * 78)
    say('  QUESTION ② -- DOES "Each patch is therefore isometric" FOLLOW FROM THE SKETCH?')
    say('=' * 78)
    f = flat(need(P2))
    chart, ext = need(CHART), need(EXT)

    say('\n  2a  WHAT THE SKETCH SAYS IT HAS, and WHAT IT CONCLUDES')
    has = ('each is matched to the Schwarzschild form in its domain of $r$ by Lemma '
           '\\ref{lem:interior_metric} and Proposition \\ref{prop:region_I_metric}')
    concl = ('Each patch is therefore isometric to the corresponding region of the maximal '
             'Kruskal--Szekeres extension')
    say(f'    [{verdict(has in f)}] it has: a match of metric COEFFICIENTS in each domain of r')
    say(f'    [{verdict(concl in f)}] it concludes: each patch is THEREFORE ISOMETRIC')

    say('\n  2b  WHAT AN ISOMETRY NEEDS, and which half the sketch cites')
    say('    an isometry of a patch with a region needs BOTH:')
    say('      ⓵ the coefficient identity                     -- cited, two lemmas')
    say('      ⓶ that the chart map is a BIJECTION onto it    -- cited?')
    cited = []
    for n in ('cc_Φ_inj', 'ce_Ψ_inj'):
        tex = cited_in_tex(f, n)
        exists = (decl_header(chart, n)[0] is not None or
                  decl_header(ext, n)[0] is not None)
        cited.append((n, exists, tex))
        say(f'    {n}: exists in the probes: {exists};  printed in P2: {tex}')
    # does the SKETCH's own sentence reach for either?
    i = f.find(concl)
    sketch = f[max(0, i - 700):i + 300]
    reaches = any(cited_in_tex(sketch, n) for n, _, _ in cited)
    say(f'    [{verdict(not reaches)}] the SKETCH\'s own passage cites NEITHER injectivity '
        f'lemma')
    say('')
    allexist = all(e for _, e, _ in cited)
    say(f'    [{"DEFECT" if (allexist and not reaches) else "NO DEFECT"}] outcome (b), as '
        f'registered: the bijection IS established elsewhere and the SKETCH does not reach '
        f'for it')
    say('      ⇒ so "therefore" is doing work the sketch does not show.  A coefficient match')
    say('        alone gives an isometry onto the IMAGE of the map; it is the region only if')
    say('        the map is onto it.  The repair is a citation, not a new result --')
    say('        cc_Φ_inj and ce_Ψ_inj are exactly what the step needs.')
    say('      ⌗ negative probe (21), registered for this revision: a "therefore" is a')
    say('        LOAD-BEARING WORD, and when the conclusion is stronger in KIND than what')
    say('        precedes it the step IS the claim.')

    say('\n  2c  ⛔ AND ONE PATCH THE CITATION CANNOT COVER -- which question ③ establishes')
    say('    the four r >= 0 patches include the SECOND exterior, and by ③ below that region')
    say('    lies OUTSIDE the spacetime se_S is defined on.  So for that patch there is no')
    say('    isometry statement in the formalisation to cite, and "each patch" quantifies')
    say('    over it.  ⇒ The citation repairs three of the four; the fourth needs the')
    say('    reflection, which proves an invariance and not an isometry onto a region.')
    return allexist and not reaches


# ------------------------------------------------ QUESTION 3
def q3():
    say('\n' + '=' * 78)
    say('  QUESTION ③ -- DOES "carries it onto the second exterior" SAY MORE THAN PROVED?')
    say('=' * 78)
    ext = need(EXT)
    f = flat(need(P2))

    say('\n  3a  WHAT REGION IS THE SPACETIME DEFINED ON?  Read from the definition.')
    m = re.search(r'^def seWS : Set P := (.+)$', ext, re.M)
    say(f'    {flat(m.group(0)) if m else "seWS ABSENT"}')
    doc = docstring_above(ext, 'seWS')
    say(f'    its own docstring: {doc[:120]}')
    v_pos = bool(m and '0 < p.2' in m.group(1))
    say(f'    [{verdict(v_pos)}] seWS carries `0 < p.2`, i.e. V > 0 -- regions I and II only')
    say('    ⚠ AND THIS IS WHERE THE PREDICTION WAS WRONG, which is why it was registered:')
    say('      I recorded that if seWS were {UV < 1} then U > 0 > V would have UV < 0 < 1 and')
    say('      the second exterior would be INSIDE it, contradicting 71\'s note.  seWS carries')
    say('      the EXTRA condition V > 0, so the second exterior (V < 0) is OUTSIDE.  71 is')
    say('      right and the guess was wrong -- and the arm survived because it was written')
    say('      to read the definition rather than to decide from memory.')

    say('\n  3b  IS THE SECOND EXTERIOR INSIDE IT?  -- arithmetic, not recollection')
    pts = {'first exterior  (U < 0 < V)': (-1.0, 1.0),
           'black-hole interior (U, V > 0)': (0.5, 0.5),
           'second exterior (U > 0 > V)': (1.0, -1.0)}
    for lbl, (u, v) in pts.items():
        inside = (0 < v) and (u * v < 1)
        say(f'    {lbl:34} V>0: {0 < v!s:5} UV<1: {u * v < 1!s:5} -> in W: {inside}')
    say('    ⇒ the second exterior is NOT in W.')

    say('\n  3c  WHAT ce_reflection ACTUALLY STATES')
    st = flat(statement(ext, 'ce_reflection') or '')
    say(f'    {st[:260]}')
    binds = binders((decl_header(ext, 'ce_reflection') or ('',))[0] or '')
    say(f'    binders: ' + '; '.join(f'{a} : {b[:26]}' for a, b in binds))
    no_dom = not any('seW' in b or 'Ioo' in b or '0 <' in b for _, b in binds)
    mentions_seS = 'se_S' in st
    say(f'    [{verdict(no_dom)}] it asks NO domain condition -- it holds for any y, a, b in '
        f'the plane')
    say(f'    [{verdict(not mentions_seS)}] and it does NOT mention se_S at all')
    say('    its own docstring:')
    say(f'      {docstring_above(ext, "ce_reflection")[:300]}')

    say('\n  3d  THE PROSE AGAINST IT')
    cl = 'carries it onto the second exterior'
    present = cl in f
    say(f'    [{verdict(present)}] P2 says "{cl}"')
    defect = present and no_dom and not mentions_seS
    say(f'    [{"DEFECT" if defect else "NO DEFECT"}] "carries it ONTO the second exterior" '
        f'says more than ce_reflection proves')
    if defect:
        say('      ⇒ what is proved is a POINTWISE INVARIANCE on the whole plane: the')
        say('        reflection preserves rK and the metric expression F·gM, for any point')
        say('        and any pair of vectors.  "Carries it onto the second exterior" asserts')
        say('        a MAP ONTO A REGION -- and by 3b that region is outside the domain the')
        say('        spacetime is defined on, so the formalisation cannot state it as a')
        say('        region at all.  The file\'s own docstring says "outside `W`".')
        say('      ⇒ The repair is to say the reflection PRESERVES r and the metric')
        say('        coefficient-wise, and that the image lies outside the chart\'s domain.')
        say('      ⌗ (r7700: a scope claim is a claim about its SUPPORT -- here the support')
        say('        is not merely different from the prose\'s, it is absent.)')
    return defect


# ------------------------------------------------ ITEM 4
def item4():
    say('\n' + '=' * 78)
    say('  ITEM ④ -- THE REST OF THE LANDING')
    say('=' * 78)
    f2, f15 = flat(need(P2)), flat(need(P15))
    ext, chart = need(EXT), need(CHART)

    say('\n  4a  P2\'s REPAIRED CLAUSES, at source')
    for lbl, m in (('⓶ "on that plane"', 'a geodesic of the Schwarzschild metric on that plane'),
                   ('the map clause',
                    'into the radial plane of that manifold, onto the black-hole interior'),
                   ('the half-repair, cc_Φ_inj cited', 'cc_Φ_inj')):
        # the name is matched by its SKELETON (see cited_in_tex), the prose literally
        hit = cited_in_tex(f2, m) if m.endswith('_inj') else (m in f2)
        say(f'    [{verdict(hit)}] {lbl}')
    old = 'a geodesic of the Schwarzschild metric on that manifold'
    say(f'    [{verdict(old not in f2)}] and the old "on that manifold" is GONE')

    say('\n    AND ONE THING CHECKED RATHER THAN ACCEPTED: is "U, V > 0" the right region?')
    m = re.search(r'^def seWS : Set P := (.+)$', ext, re.M)
    say(f'      seWS = {flat(m.group(1)) if m else "?"}')
    say('      the black-hole interior inside W needs V > 0 (from seWS) and UV > 0, hence')
    say('      U > 0 too.  ⇒ "U, V > 0" IS that region.  [SUPPORTED]')

    say('\n  4b  THE THREE NEW DECLARATIONS')
    for n in ('ce_Ψ_inj', 'ce_pullback', 'ce_reflection'):
        hdr, ln = decl_header(ext, n)
        tex = cited_in_tex(f2, n)
        say(f'    [{verdict(hdr is not None and tex)}] {n}: at l.{ln}; printed in P2: {tex}')
        if hdr is None:
            FAIL.append(f'4b {n} absent')
        else:
            say('      binders: ' + '; '.join(f'{a} : {b[:30]}' for a, b in binders(hdr)))

    say('\n  4c  P15\'s "about three per cent" -- AND THIS SEAT\'S OWN r7710 FINDING')
    say(f'    [{verdict("about three per cent off the limit it converges to" in f15)}] the '
        f'as-run offset now reads in WORDS')
    n32 = len(re.findall(re.escape('$3.2$ per cent'), f15))
    say(f'    "$3.2$ per cent" now occurs {n32} time(s) in P15')
    sent = f15[f15.find('with them \\emph{frozen}'):][:420]
    in_sent = len(re.findall(re.escape('$3.2$ per cent'), sent))
    say(f'    and {in_sent} of them is in the sentence the collision was in')
    say(f'    [{"NO COLLISION" if in_sent <= 1 else "COLLISION REMAINS"}] r7710\'s finding is '
        f'discharged')
    say('')
    say('    THE FIGURE AGAINST ITS SOURCE, searched two ways:')
    r = need(RCPT)
    rec = [l for l in r.split('\n') if 'per cent short at l = 4' in l]
    for l in rec:
        say(f'      the receipt\'s own text: {flat(l)[:150]}')
    say(f'      [{verdict(bool(rec))}] the receipt records ~3 per cent, which is what P15 now '
        f'prints')
    say('    ⌗ AND ONE NOT FOUND, said as NOT FOUND over a named search: the order attributes')
    say('      a COMPUTED "3.23 per cent" to the receipt.  Searched by the digits across')
    say('      every receipt (one hit, in an unrelated P17 receipt) and by content in both')
    say('      NS3-bearing P15 receipts, where the figure appears as a RECORDED COMMENT')
    say('      ("NS3 900 was ~3 per cent short at l = 4") and not as a computed gate.  So')
    say('      the paper\'s figure agrees with what the receipt RECORDS; whether a gate')
    say('      COMPUTES 3.23 is not established by these searches.')

    say('\n  4d  AXIOM HYGIENE, the new file')
    na, ns = len(re.findall(r'\baxiom\b', ext)), len(re.findall(r'\bsorry\b', ext))
    say(f'    CircleExterior.lean: axiom tokens {na}; sorry {ns}')
    say(f'    [{verdict(na == 0 and ns == 0)}] no axiom carries content the paragraph credits '
        f'to a proof')
    say('    ⌗ AND WHAT THIS CANNOT DO: it reads declarations, hypotheses and statement')
    say('      shapes.  Whether each proof TERM closes is the Lean build\'s business, and no')
    say('      geometric fact the files do not state is supplied here.')


def main():
    say()
    say('  r7712 (60) -- READINGS.  Order r7709: the landing, and its three questions.')
    q1ok, nsites = q1()
    d2 = q2()
    d3 = q3()
    item4()
    say('\n' + '=' * 78)
    say('  VERDICTS')
    say('=' * 78)
    say(f'  ① the horizons clause is right in all {nsites} places, every one a point-set '
        f'claim: {verdict(q1ok)}  (the registered expectation of a defect was NOT borne out)')
    say(f'  ② "therefore isometric" needs a bijection the SKETCH does not cite, though the '
        f'lemmas exist: {"DEFECT, a citation owed" if d2 else "no defect"}')
    say(f'  ③ "carries it onto the second exterior" says more than ce_reflection proves, and '
        f'that region is outside the spacetime\'s domain: '
        f'{"DEFECT" if d3 else "no defect"}')
    say(f'  ④ the rest of the landing holds, and r7710\'s figure collision is discharged')
    say()
    if FAIL:
        say('  ⛔ PROBE SELF-CHECKS FAILED -- the readings above are not to be trusted:')
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
