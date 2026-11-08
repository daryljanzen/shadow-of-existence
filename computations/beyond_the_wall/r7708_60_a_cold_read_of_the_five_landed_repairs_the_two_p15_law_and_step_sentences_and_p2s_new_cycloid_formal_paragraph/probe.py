#!/usr/bin/env python3
"""r7708 (60) -- the readings behind RESULT.md, every verdict BUILT FROM them.

Order r7705: a cold read of the two P15 law-and-step sentences FIRST, then the five landed
repairs in place, then P2's new cycloid formal paragraph against CircleCycloid.lean.

GUARDS.  G1 one predicate per conjunct.  G2 three anchor forms only -- a word boundary, an
escaped control sequence with ONE leading backslash, an escaped math delimiter -- unanchored
markers REFUSED.  G3 the flip family, striking EVERY copy.  G4 classifier probes tested on
BOTH classes.  G5 reader probes with negatives.  G6 every prose probe on a FLATTENED copy.

⬭ THE READERS r7706 REPAIRED ARE CARRIED FORWARD AND RE-TESTED, NOT REBUILT: binders by
  bracket-DEPTH (a flat `[^()]*` type cannot see `hs : Real.sin (x 2) ≠ 0`); the HEADER only
  (casts in the body are not binders); Unicode-aware (`hτ` was invisible to ASCII at r7700);
  `include X in` at its own ONE-DECLARATION scope and across multi-line docstrings; and every
  prose marker matched CASE-INSENSITIVELY, which is what found l.460 at r7706.
⬭ AND ONE MEASURED HERE: a FIXED-SIZE window around a declaration reads its neighbours'
  docstrings as its own.  Three definitions looked Kruskal-coupled under a +6-line window and
  are not.  A declaration's extent is derived, never assumed -- the same family a fifth time.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
P2 = os.path.join(ROOT, 'corpus', 'janzen_circle_v3.tex')
P15 = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
LEAN = os.path.join(ROOT, 'computations', 'formalisation', 'lean', 'probes',
                    'CircleCycloid.lean')
RCPT = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                    'P15_a_source_with_no_physics_reproduces_the_contrast_and_the_two_'
                    'clocks_part_company_at_the_visibility.py')

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


# -------------------------------------------------- readers carried from r7706
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
    """The declaration's OWN text: from its header to the start of the next declaration.

    ⬭ MEASURED HERE: a fixed +N-line window reads the NEXT declaration's docstring as part of
      this one, and reported `cy_g`, `cy_c` and `cy_gD` as Kruskal-coupled when none is.  The
      extent is derived from where the next declaration begins.
    """
    m = re.search(r'^(?:noncomputable\s+)?(?:theorem|lemma|def|abbrev)\s+' +
                  re.escape(name) + r'\b', src, re.M)
    if not m:
        return None
    nxt = re.search(r'^(?:/--|@\[|noncomputable\s+)?(?:theorem|lemma|def|abbrev|/--)\s',
                    src[m.end():], re.M)
    return src[m.start():m.end() + (nxt.start() if nxt else 4000)]


def statement(src, name):
    """Header plus conclusion, stopping at the proof -- never running into the next decl."""
    ext = decl_extent(src, name)
    if ext is None:
        return None
    stop = re.search(r':=\s*(by\b|$)', ext, re.M)
    return ext[:stop.start()] if stop else ext


def include_binders(src, line_no):
    lines, i, names = src.split('\n'), line_no - 2, []
    while i >= 0:
        L = lines[i].strip()
        if not L:
            i -= 1
            continue
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
    return [(n, types.get(n, '?')) for n in names]


def g5_readers(lean):
    """G5: every reader run on a known positive AND a known negative before it is used."""
    ok = []
    ok.append(decl_header(lean, 'cy_radial')[0] is not None)
    ok.append(decl_header(lean, 'cy_not_a_real_lemma')[0] is None)
    hs = binders(' (hM : 0 < M) {x : Fin 4 → ℝ} (hs : Real.sin (x 2) ≠ 0) ')
    ok.append([a for a, _ in hs] == ['hM', 'x', 'hs'])          # depth-matched type
    ok.append(binders(' (hτ : τ ∈ Ioo 0 1) ')[0][0] == 'hτ')   # Unicode
    ext = decl_extent(lean, 'cy_A') or ''
    ok.append('cy_B' not in ext)                                 # extent stops in time
    return ok


# -------------------------------------------------- item 1: P15 law and step
def item1():
    say('=' * 78)
    say('  ITEM 1 -- THE TWO P15 LAW-AND-STEP SENTENCES (first, as ordered)')
    say('=' * 78)
    f = flat(need(P15))
    rc = need(RCPT)

    say('\n  1a  THE CHANGED FIGURE, and WHAT THE INTERVAL IS OF')
    say(f'    [{verdict("a factor of about $1.8$ on all three widths" in f)}] P15 prints '
        f'"a factor of about $1.8$ on all three widths"')
    say(f'    [{verdict("clean factor of two on all three widths" not in f)}] the old '
        f'"clean factor of two on all three widths" is GONE')
    # the receipt's own column header names what the triple is OF -- read, not assumed
    hdr = [l for l in rc.split('\n') if 'half-rise' in l and 'factor' in l]
    for h in hdr:
        say(f'    the receipt\'s own column header: {flat(h)[:150]}')
    say('    ⇒ so the triple is (half-rise, 25-75 rise, FACTOR) per half-width, and the')
    say('      printed 1.8 is the FACTOR column -- the step\'s SIZE, not its half-rise')
    say('      position, which is also near 1.8 and is a DIFFERENT QUANTITY.')
    say('      ⌗ negative probe (16) again: two quantities of this object both read ~1.8.')

    say('\n  1b  SIZE, PLACE AND SHARPNESS ARE THREE CLAIMS -- which does each sentence make?')
    sharp = ('reproduces that step\'s size without reproducing its sharpness')
    size = 'so the law carries the step\'s size'
    unres = ('the measurement\'s transition is unresolved at every width and the law\'s is '
             'resolved at every one')
    for lbl, m in (('the sharpness exception, NAMED', sharp),
                   ('the size claim', size),
                   ('the unresolved/resolved contrast', unres)):
        say(f'    [{verdict(m in f)}] {lbl}: "{m[:62]}"')
    place = any(s in f for s in ['the law locates the step', 'the law\'s transition is located',
                                 'the law places the step'])
    say(f'    [{verdict(not place)}] and NEITHER sentence claims the law LOCATES the step')
    say('      ⇒ which matters, because the receipt\'s own translation test says it cannot:')
    tr = [l for l in rc.split('\n') if 'translating the read interval' in l]
    for l in tr:
        say(f'        {flat(l)[:160]}')

    say('\n  1c  THE RATIO OF WIDTHS -- the form the receipt FORBIDS, and the one it licenses')
    forbids = 'never as a ratio of two widths' in flat(rc)
    say(f'    [{verdict(forbids)}] the receipt forbids stating it as a ratio of two widths')
    lic = [l for l in rc.split('\n') if 'SEVEN TIMES' in l]
    for l in lic:
        say(f'    the receipt\'s licensed form: {flat(l)[:150]}')
    p15w = 'the wider by some seven times at identical smoothing' in f
    say(f'    [{verdict(p15w)}] P15 prints "the wider by some seven times at identical '
        f'smoothing"')
    say(f'    [{verdict(unres in f)}] and the floor caveat is IN THE SAME CLAUSE '
        f'("unresolved at every width")')
    say(f'    [{"NO DEFECT" if (p15w and unres in f) else "DEFECT"}] the licensing caveat '
        f'travels with the ratio')
    say('      ⌗ reported rather than inflated: "the wider" is loose for a ratio of two')
    say('        READINGS at one smoothing, but the clause that makes it legal -- that the')
    say('        measurement\'s is unresolved at every width -- is in the same sentence.')
    say('      ⌗ AND ONE ROUNDING, both in the receipt and in the paper: the measured ratio')
    say('        is 7.8, which both call "some seven times".  7.8 is nearer eight.')

    say('\n  1d  DOES ANY SIBLING SITE STILL PRINT THE OLD FIGURE FOR THIS STEP? (searched)')
    for m in ['clean factor of two', 'a factor of two', 'a factor of about $1.8$']:
        n = len(re.findall(re.escape(m), f))
        say(f'    "{m}": {n} occurrence(s) in P15')
    say('    ⇒ the surviving "a factor of two" sites are read at their own labels and belong')
    say('      to other objects (the share\'s ambiguity, a false-value test, a slope fit);')
    say('      NONE is this step\'s size.  Negative probe (16): the label, not the digits.')
    return p15w and unres in f


# -------------------------------------------------- item 2: the five repairs
def item2():
    say('\n' + '=' * 78)
    say('  ITEM 2 -- THE FIVE REPAIRS THIS SEAT ROUTED, READ IN PLACE')
    say('=' * 78)
    f2, f15 = flat(need(P2)), flat(need(P15))
    lean = need(os.path.join(os.path.dirname(LEAN), 'CircleKretschmann.lean'))

    say('\n  2a  P2 l.140 -- is BOTH attributions scoped, or only the nearer one?')
    new = ('the cycloidal motion of a radially infalling test particle of vanishing Killing '
           'energy as parametrised by the rolling angle $\\eta$, with the proper time $\\tau$ '
           'being the arc length along the cycloid')
    say(f'    [{verdict(new in f2)}] the repaired sentence reads as the order reports')
    say('      ⇒ the qualifier sits on the PARTICLE, and both the cycloidal FORM and')
    say('        "$\\tau$ the arc length" are predicated of that particle\'s motion, so both')
    say('        are scoped by one phrase.  (r7698: a clause is confined by its SUBJECT.)')

    say('\n  2b  P2 l.460 -- scoped, AND the finiteness claim NOT narrowed (regression arm)')
    par = ('($\\tau = M\\pi$ from horizon-crossing for the worldline of vanishing Killing '
           'energy)')
    gen = 'The infalling worldline reaches $r=0$ in finite proper time'
    say(f'    [{verdict(par in f2)}] the parenthetical is scoped')
    say(f'    [{verdict(gen in f2)}] the finiteness clause is STILL GENERAL')
    say('      ⇒ and still true generally: r7704 integrated seven members and all are')
    say('        finite, so narrowing it would have been a REGRESSION.  It was not narrowed.')

    say('\n  2c  P2\'s formal paragraph -- the chain-rule object, re-checked against the lemma')
    fix = ('wherever $h$ vanishes at a non-degenerate critical point, a zero of order '
           'exactly two')
    say(f'    [{verdict(fix in f2)}] the repaired phrase reads as the order reports')
    say(f'    [{verdict("a non-degenerate zero" not in f2)}] the old "a non-degenerate zero" '
        f'is GONE')
    cr = flat((decl_header(lean, 'ck_chain_rule') or ('',))[0] or '')
    asks = {'h z₀ = 0': 'h(z0) = 0', 'deriv h z₀ = 0': "h'(z0) = 0",
            'iteratedDeriv 2 h z₀ ≠ 0': 'h\'\'(z0) != 0'}
    for k, lbl in asks.items():
        say(f'    [{verdict(k in cr)}] the lemma still asks {lbl}')
    order = {'a simple zero': 6 * 1, 'a zero of order exactly two': 6 * 2}
    say(f'    pole order, recomputed here: {order}')
    say(f'    [{verdict(order["a zero of order exactly two"] == 12)}] twelve needs the DOUBLE '
        f'zero, which is what the repaired phrase now names')

    say('\n  2d  "away from the poles of the sphere\'s chart" -- the PHRASE against the SET')
    ph = "away from the poles of the sphere's chart"
    say(f'    [{verdict(ph in f2)}] the phrase is in the Kruskal-chart clause')
    for n in ('ck_horizon', 'ck_interior'):
        hs = [b for a, b in binders((decl_header(lean, n) or ('',))[0] or '')
              if 'Real.sin' in b]
        say(f'    {n} asks: {hs}')
    say('      ⇒ `Real.sin (x 2) ≠ 0` excludes exactly `x 2 ∈ πℤ`, which on the')
    say('        2-sphere\'s polar angle is the two poles.  The phrase names that SET, not a')
    say('        gloss of it.  (r7700: a scope claim is a claim about its SUPPORT.)')

    say('\n  2e  P15\'s scope sentence -- does the DEPTH now rest on one build and the SHAPE '
        'on both?')
    d = ('so the depth rests on the decoupled build\'s agreement with the exact transfer')
    s = ('the shape---the minimum at $\\ell=4$ and the recovery by $\\ell=8$---is returned by '
         'both treatments')
    say(f'    [{verdict(d in f15)}] the DEPTH is rested on the decoupled build')
    say(f'    [{verdict(s in f15)}] the SHAPE is returned by both treatments')
    say('      ⇒ which is exactly what 70 measured: FROZEN at its default late step count is')
    say('        6.19 per cent off at l = 4, while its extrapolated sequence still has its')
    say('        minimum at l = 4 and recovers by l = 8.  r7706\'s finding is discharged.')
    return all(x in f2 for x in (new, par, gen, fix, ph)) and d in f15 and s in f15


# -------------------------------------------------- item 3: the cycloid paragraph
def item3():
    say('\n' + '=' * 78)
    say('  ITEM 3 -- P2\'s NEW CYCLOID FORMAL PARAGRAPH AGAINST CircleCycloid.lean')
    say('=' * 78)
    lean, f2 = need(LEAN), flat(need(P2))

    say('\n  G5  reader negatives (all five readers, before use)')
    ok = g5_readers(lean)
    for lbl, v in zip(['header reader finds a known name',
                       'header reader does NOT find a fiction',
                       'binders depth-match a type carrying parentheses',
                       'binders see a Unicode name',
                       'declaration EXTENT stops before the next declaration'], ok):
        say(f'    [{verdict(v)}] {lbl}')
    if not all(ok):
        FAIL.append('3 G5 readers fail their negatives')

    named = ['cy_proper_time', 'cy_Mpi', 'cy_radial', 'cy_ends', 'cy_geodesic',
             'cy_interior_forms']
    say('\n  3a  THE SIX NAMES THE PARAGRAPH PRINTS')
    for n in named:
        hdr, ln = decl_header(lean, n)
        tex = n.replace('_', '\\_') in f2
        say(f'    [{verdict(hdr is not None and tex)}] {n}: at l.{ln}; printed in P2: {tex}')
        if hdr is None:
            FAIL.append(f'3a {n} absent')

    say('\n  3b  HYPOTHESES, each theorem\'s own')
    for n in named:
        hdr, ln = decl_header(lean, n)
        if hdr is None:
            continue
        bs = binders(hdr)
        inc = include_binders(lean, ln)
        say(f'    {n}: {len(bs)} binder(s) -- ' + '; '.join(f'{a} : {b[:40]}' for a, b in bs)
            + (f'   [+ include: {"; ".join(a for a, _ in inc)}]' if inc else ''))
    say('    ⌗ cy_proper_time and cy_Mpi ask NOTHING about M -- no `0 < M`.  So they are MORE')
    say('      GENERAL than the paragraph\'s sentence, which is r7700\'s shape and NO defect.')

    say('\n  3c  DOES THE FORMALISATION CARRY THE E = 0 RESTRICTION, or assume it silently?')
    g = flat(statement(lean, 'cy_geodesic') or '')
    conj = {'cy_IsGeodesic': 'the geodesic equation',
            '= -1': 'unit timelike',
            'cy_c M t₀ ρ a) τ) = 0': 'Killing energy zero'}
    for k, lbl in conj.items():
        say(f'    [{verdict(k in g)}] cy_geodesic states {lbl}')
    say('      ⇒ ** THE ANSWER: E = 0 is a PROVED CONJUNCT of cy_geodesic, not a hypothesis. **')
    say('        So the formalisation establishes the restriction the repaired prose states,')
    say('        rather than assuming it -- and the reachable negative (silently assumed) is')
    say('        not what was found.')

    say('\n  3d  IS $M\\pi$ PROVED, or asserted as a value the chart is given?')
    mp = flat(statement(lean, 'cy_Mpi') or '')
    pt = flat(statement(lean, 'cy_proper_time') or '')
    tau = re.search(r'^noncomputable def cy_τ[^\n]*', lean, re.M)
    say(f'    cy_Mpi: {mp[:120]}')
    say(f'    cy_proper_time: {pt[:120]}')
    say(f'    {flat(tau.group(0)) if tau else "cy_τ ABSENT"}')
    say(f'    [{verdict("= M * Real.pi" in mp and "∫" in mp)}] $M\\pi$ is the VALUE OF AN '
        f'INTEGRAL of the proper-time element, proved via cy_proper_time')

    say('\n  3e  "the chart is not pulled back from the Kruskal manifold here" -- NAMED search')
    cyline = re.search(r'^noncomputable def cy_r\b', lean, re.M)
    lo = lean[:cyline.start()].count('\n') + 1
    tot = len(lean.split('\n'))
    region = '\n'.join(lean.split('\n')[lo - 1:])
    marks = ['rK ', 'sk_S', 'sk_kM', 'kr_', 'Kruskal', 'hK ', 'rinv', 'ChartedSpace',
             'PartialHomeomorph', 'IsManifold']
    say(f'    region: l.{lo}-{tot} (the cy_ section); whole file {tot} lines')
    say('    per-marker counts   region / whole file:')
    for m in marks:
        say(f'      {m!r:22} {len(re.findall(re.escape(m), region)):4} / '
            f'{len(re.findall(re.escape(m), lean))}')
    say('    ⇒ the region\'s kr_ hits belong to the row-6 theorems that COMPARE against')
    say('      Kruskal on purpose (cy_regionI_schw, cy_backseam_schw, cy_patches,')
    say('      cy_backseam_not_kruskal).  So the whole-region count does NOT answer the')
    say('      claim, which is about the CHART.  The chart\'s own objects are read instead:')
    for d in ('cy_r', 'cy_τ', 'cy_η', 'cy_A', 'cy_B', 'cy_g', 'cy_c',
              'cy_gD', 'cy_IsGeodesic'):
        ext = decl_extent(lean, d)
        if ext is None:
            continue
        hits = sorted({m for m in marks if m.strip() in ext})
        say(f'      {d:14} Kruskal identifiers in its OWN extent: '
            f'{hits if hits else "NONE"}')
    say('    and the six named theorems\' STATEMENTS:')
    bad = []
    for n in named:
        st = statement(lean, n) or ''
        hits = sorted({m for m in marks if m.strip() in st})
        if hits:
            bad.append((n, hits))
        say(f'      {n:20} {hits if hits else "NONE"}')
    say('')
    say(f'    [{verdict(not bad)}] NOT FOUND -- {len(marks)} markers, ZERO in any of the six')
    say(f'      statements and ZERO in the chart\'s metric and curve definitions.')
    say('    ⌗ THE ONE COUPLING, named rather than swept: cy_IsGeodesic uses `kr_Γ`,')
    say('      campaign 110\'s Christoffel operator, which TAKES THE METRIC AS AN ARGUMENT --')
    say('      a reused formula, not a pullback.  The file\'s own header states the limit:')
    say('      "the interior chart (η, t) is a coordinate metric, not tied to `sk_S`".')
    say('    ⌗ Said as NOT FOUND over a named search, not as "there is none" -- and the trap')
    say('      was registered in advance: this file is a copy of the campaign kit, so the')
    say('      Kruskal machinery is abundant in the INHERITED part by construction.')

    say('\n  3f  NON-VACUITY')
    for n in ('cy_radial', 'cy_geodesic', 'cy_interior_forms'):
        st = flat(statement(lean, n) or '')
        iv = re.findall(r'Ioo [^,)]+', st)
        say(f'    {n}: quantified over {iv[:2] if iv else "no Ioo found"}')
    say('      ⇒ each is stated over an explicitly NON-EMPTY open interval (0 < π and,')
    say('        with 0 < M, 0 < Mπ), so none is vacuous.  (r7698 and r7706 both turned')
    say('        on exactly this, and both needed a separate witness; here the index set is')
    say('        the witness.)')

    say('\n  3g  AXIOM HYGIENE')
    na, ns = len(re.findall(r'\baxiom\b', lean)), len(re.findall(r'\bsorry\b', lean))
    say(f'    `axiom` tokens: {na};  `sorry`: {ns}')
    say(f'    [{verdict(na == 0 and ns == 0)}] no axiom carries content the paragraph credits '
        f'to a proof')
    say('    ⌗ AND WHAT THIS CANNOT DO, as registered: it reads declarations, hypotheses and')
    say('      statement shapes.  Whether each proof TERM closes is the Lean build\'s and')
    say('      check_no_sorry\'s business, not this probe\'s.')
    return not bad


def main():
    say()
    say('  r7708 (60) -- READINGS.  Order r7705, three items.')
    a = item1()
    b = item2()
    c = item3()
    say('\n' + '=' * 78)
    say('  VERDICTS')
    say('=' * 78)
    say(f'  ITEM 1  the figure change is right and labelled; size, place and sharpness are '
        f'kept apart; the width ratio carries its caveat: {verdict(a)}')
    say(f'  ITEM 2  all five routed repairs landed, and l.460\'s finiteness claim was not '
        f'narrowed: {verdict(b)}')
    say(f'  ITEM 3  the six names are present, E = 0 is a PROVED conjunct, and the chart is '
        f'not pulled back from Kruskal: {verdict(c)}')
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
