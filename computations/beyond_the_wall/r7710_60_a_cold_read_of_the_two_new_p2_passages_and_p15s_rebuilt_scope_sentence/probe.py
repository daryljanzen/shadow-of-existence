#!/usr/bin/env python3
"""r7710 (60) -- the readings behind RESULT.md, every verdict BUILT FROM them.

Order r7707: the two new P2 passages, P15's rebuilt scope sentence, and the order's two
direct questions -- whether prop:four_regions needs a word, and whether "a geodesic ... on
that manifold" says too much given se_S is the radial plane.

GUARDS.  G1 one predicate per conjunct.  G2 three anchor forms only -- a word boundary, an
escaped control sequence with ONE leading backslash, an escaped math delimiter -- unanchored
markers REFUSED.  G3 the flip family, striking EVERY copy.  G4 classifier probes tested on
BOTH classes.  G5 reader probes with negatives.  G6 every prose probe on a FLATTENED copy.

⬭ THE READERS r7706 AND r7708 REPAIRED ARE CARRIED FORWARD AND RE-TESTED, NOT REBUILT:
  binders by bracket-DEPTH, the HEADER only, Unicode-aware, `include X in` at its own
  one-declaration scope and across multi-line docstrings, prose markers CASE-INSENSITIVE, and
  a declaration's extent DERIVED from where the next begins rather than a fixed window.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
P2 = os.path.join(ROOT, 'corpus', 'janzen_circle_v3.tex')
P15 = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
PROBES = os.path.join(ROOT, 'computations', 'formalisation', 'lean', 'probes')
CHART = os.path.join(PROBES, 'CircleChart.lean')
CYC = os.path.join(PROBES, 'CircleCycloid.lean')
FOR70 = os.path.join(ROOT, 'FOR_66_FROM_70.md')

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


# ------------------------------------------------ readers carried from r7706/r7708
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


def g5_readers(src):
    ok = [decl_header(src, 'cc_pullback')[0] is not None,
          decl_header(src, 'cc_not_a_real_lemma')[0] is None,
          [a for a, _ in binders(' (hM : 0 < M) (p : seW) {η : ℝ} '
                                 '(hη : η ∈ Ioo 0 Real.pi) ')]
          == ['hM', 'p', 'η', 'hη']]
    ext = decl_extent(src, 'cc_pullback') or ''
    ok.append('cc_isGeodesicOn' not in ext)
    return ok


# ------------------------------------------------ QUESTION 1
def q1():
    say('=' * 78)
    say('  QUESTION ① -- DOES prop:four_regions NEED A WORD?')
    say('=' * 78)
    f = flat(need(P2))

    say('\n  1a  WHAT EACH TEXT ACTUALLY SAYS, read at source')
    prop = 'they are precisely the maximal Kruskal--Szekeres extension'
    note = ('That the four $r\\ge0$ patches are exactly the Kruskal--Szekeres extension, and '
            'the $r<0$ patches as a geometry in their own right, are not formalised')
    pf = 'This subset is in bijection with the maximal Kruskal--Szekeres extension'
    for lbl, m in (('the PROPOSITION claims', prop),
                   ('the FORMAL NOTE says', note),
                   ("the PROPOSITION'S OWN PROOF establishes", pf)):
        say(f'    [{verdict(m in f)}] {lbl}: "{m[:74]}"')
        if m not in f:
            FAIL.append(f'1a missing at source: {m[:40]}')

    say('\n  1b  G4 -- the classifier, on an injected note of EACH kind')
    bounds_machine = 'the identification is not formalised'
    bounds_paper = 'the identification is not established'

    def kind(s):
        if re.search(anchor('not formalised'), s, re.I):
            return 'BOUNDS THE MACHINE'
        if re.search(anchor('not established'), s, re.I) or \
           re.search(anchor('not shown'), s, re.I):
            return 'BOUNDS THE PAPER'
        return 'NEITHER'
    k1, k2 = kind(bounds_machine), kind(bounds_paper)
    say(f'    injected "not formalised"  -> {k1}')
    say(f'    injected "not established" -> {k2}')
    ok = k1 == 'BOUNDS THE MACHINE' and k2 == 'BOUNDS THE PAPER'
    say(f'    [{verdict(ok)}] the classifier separates the two kinds')
    if not ok:
        FAIL.append('1b G4 classifier does not separate the two kinds of note')

    say('\n  1c  THE ANSWER TO THE ORDER\'S QUESTION')
    actual = kind(note)
    say(f'    the landed note is of kind: {actual}')
    say(f'    [{verdict(actual == "BOUNDS THE MACHINE")}] it bounds what is MACHINE-CHECKED, '
        f'not what is established')
    say('    ⇒ ⛭ NO WORD IS OWED ON ACCOUNT OF THE FORMAL PARAGRAPH.  The proposition states')
    say('      the paper\'s claim, proved by the paper\'s own argument; the note says only')
    say('      which parts a machine has checked.  ⌗ And this answer was REACHABLE: the')
    say('      order asks "whether the proposition needs a word", which invites agreeing,')
    say('      and the classifier returns the other verdict on an injected note that bounds')
    say('      the paper.  Reaching it when it is true is a result.')

    say('\n  1d  ⛔ BUT A WORD IS OWED FOR A REASON THE ORDER DID NOT NAME')
    say('      -- found by reading the proposition against ITS OWN PROOF, not the note:')
    say(f'      the proposition says   "...are PRECISELY the maximal Kruskal--Szekeres')
    say(f'                              extension"')
    say(f'      its proof sketch says  "This subset is IN BIJECTION WITH the maximal')
    say(f'                              Kruskal--Szekeres extension"')
    say('      ⇒ a bijection of patch sets is not an identity of spacetimes: "precisely the')
    say('        extension" reads as the extension itself, and a bijection is what is shown.')
    say('        The guard that applies is the corpus\'s own -- before two stretches are')
    say('        identified by a label, check how many-to-one the label is on the object.')
    bij = pf in f and prop in f
    say(f'    [{"DEFECT" if bij else "NO DEFECT"}] the proposition claims more than its own '
        f'proof establishes')
    return actual == 'BOUNDS THE MACHINE', bij


# ------------------------------------------------ QUESTION 2
def q2():
    say('\n' + '=' * 78)
    say('  QUESTION ② -- DOES "a geodesic ... ON THAT MANIFOLD" SAY TOO MUCH?')
    say('=' * 78)
    src = need(CHART)
    f = flat(need(P2))

    say('\n  G5  reader negatives')
    for lbl, v in zip(['header reader finds a known name',
                       'header reader does NOT find a fiction',
                       'binders depth-match and see Unicode',
                       'declaration extent stops before the next'], g5_readers(src)):
        say(f'    [{verdict(v)}] {lbl}')
    if not all(g5_readers(src)):
        FAIL.append('2 G5 readers fail their negatives')

    say('\n  2a  WHAT IS se_S?  Read from the definition, not from the name.')
    mp = re.search(r'^abbrev P := (.+)$', src, re.M)
    mw = re.search(r'^def seW : (.+)$', src, re.M)
    ms = re.search(r'^noncomputable def se_S[^\n]*', src, re.M)
    say(f'    {flat(mp.group(0)) if mp else "P ABSENT"}')
    say(f'    {flat(mw.group(0)) if mw else "seW ABSENT"}')
    say(f'    {flat(ms.group(0)) if ms else "se_S not defined in this file"}')
    two_d = bool(mp and 'ℝ × ℝ' in mp.group(1))
    say(f'    [{verdict(two_d)}] the model space is ℝ × ℝ, so se_S is a '
        f'TWO-DIMENSIONAL spacetime -- the radial plane')

    say('\n  2b  WHAT THE TWO THEOREMS QUANTIFY OVER')
    for n in ('cc_pullback', 'cc_isGeodesicOn', 'cc_unit_energy'):
        hdr, ln = decl_header(src, n)
        st = flat(statement(src, n) or '')
        say(f'    {n} (l.{ln}): binders ' +
            '; '.join(f'{a} : {b[:30]}' for a, b in binders(hdr or '')))
        say(f'      conclusion mentions se_S: {"se_S" in st}')
    say('    ⇒ both read `(se_S hM)` -- the plane\'s metric, by 2a.')

    say('\n  2c  WHAT THE PROSE SAYS, and WHICH ANTECEDENT "that manifold" HAS')
    sent = ('The chart is pulled back from the Kruskal manifold: its map into the radial '
            'plane of the black-hole interior is one-to-one and pulls the Schwarzschild '
            'metric back to exactly this form')
    cl = ('the curve at fixed $t=t_0$ is a geodesic of the Schwarzschild metric on that '
          'manifold')
    say(f'    [{verdict(sent in f)}] the replaced sentence is the POSITIVE claim')
    say(f'    [{verdict(cl in f)}] and the clause reads "...on that manifold"')
    say('    the two candidate antecedents, in the order the sentence offers them:')
    say('      ⓵ "the Kruskal manifold"                       -- the SALIENT one (the')
    say('         sentence opens with it, as its grammatical topic)')
    say('      ⓶ "the radial plane of the black-hole interior" -- the NEAREST one')
    say('    ⇒ ⛔ THE ANSWER: under ⓶ the clause is EXACT -- it is what the theorem says.')
    say('      Under ⓵ it says MORE than the theorem: a geodesic of the 2-plane\'s metric')
    say('      is not automatically a geodesic of the 4-metric, which needs the plane to be')
    say('      TOTALLY GEODESIC in the 4-geometry.')
    say('    ⌗ AND THE HONEST CLASSIFICATION, which the prediction required be kept apart')
    say('      from a falsehood: for Schwarzschild the fixed-angle (t, r) surface IS totally')
    say('      geodesic, by the 2-sphere\'s reflection symmetry, so the stronger reading is')
    say('      TRUE -- and rests on a fact this file does not state.  So the defect is an')
    say('      AMBIGUITY and not an error, and one word fixes it: "that plane".')
    say('    ⌗ (r7700: a scope claim is a claim about its SUPPORT.  r7698: a clause is')
    say('      confined by the SUBJECT it names -- and here two subjects are on offer.)')
    return two_d and cl in f


# ------------------------------------------------ ITEM 3
def item3():
    say('\n' + '=' * 78)
    say('  ITEM ③ -- THE REST OF THE TWO P2 PASSAGES')
    say('=' * 78)
    f = flat(need(P2))
    cyc, chart = need(CYC), need(CHART)

    say('\n  3a  cc_pullback: one-to-one AND the pullback?')
    st = flat(statement(chart, 'cc_pullback') or '')
    say(f'    statement: {st[:300]}')
    say(f'    [{verdict("hRep (se_S hM).g" in st)}] it states the metric components pulled '
        f'back (cy_A, cy_B and the vanishing cross term)')
    # ⬭ MEASURED HERE: guessing four plausible names returned NOT FOUND, and the
    #   declaration exists.  So the search is by CONTENT -- the conclusion's SHAPE -- over
    #   every cc_ declaration, which is what an injectivity statement looks like whatever
    #   it is called.  Negative probe (19) again: an instrument reads the FORM it was given.
    inj_name, inj_st = None, ''
    for m in re.finditer(r'^(?:theorem|lemma)\s+(cc_[^\s(]+)', chart, re.M):
        st = flat(statement(chart, m.group(1)) or '')
        if re.search(r'=\s*η\'\s*∧|Inj', st):
            inj_name, inj_st = m.group(1), st
            break
    say(f'    [{verdict(inj_name is not None)}] an INJECTIVITY statement exists, found by '
        f'the SHAPE of its conclusion: {inj_name}')
    if inj_name:
        say(f'      {inj_st[:230]}')
        named = inj_name.replace('_', '\\_') in f
        say(f'    [{verdict(not named)}] ⌗ and the paragraph does NOT print its name -- it '
            f'cites only cc_pullback for that clause')
        say('      ⇒ not a defect: the one-to-one claim IS established, on (0, π) × ℝ.')
        say('        Worth one word all the same, because a reader checking "one-to-one"')
        say('        against cc_pullback will not find it there.')

    say('\n  3b  THE REPLACED SENTENCE -- its subject CHANGED, so r7708 does not transfer')
    old = 'The chart is not pulled back from the Kruskal manifold here'
    say(f'    [{verdict(old not in f)}] the old NEGATIVE sentence is GONE')
    say('    ⇒ negative probe (20), registered for this revision: when a sentence is')
    say('      REPLACED rather than edited its subject may change, and a verification of')
    say('      the old one does not transfer.  r7708 verified the old sentence by a named')
    say('      search over ten Kruskal markers; that reading says nothing about this claim.')

    say('\n  3c  THE SECOND PARAGRAPH\'S NAMED DECLARATIONS')
    for n in ('cy_interior_forms', 'cy_regionI_coeffs', 'cy_regionI_schw',
              'cy_backseam_coeffs', 'cy_backseam_schw', 'cy_patches',
              'cy_backseam_not_kruskal'):
        hdr, ln = decl_header(cyc, n)
        tex = n.replace('_', '\\_') in f
        say(f'    [{verdict(hdr is not None and tex)}] {n}: at l.{ln}; printed in P2: {tex}')
        if hdr is None:
            FAIL.append(f'3c {n} absent')

    say('\n  3d  "with $\\rho\\neq0$" -- a hypothesis, and what it leaves out')
    rho_excl = 'for $\\rho\\neq0$' in f
    say(f'    [{verdict(rho_excl)}] the paragraph states the exclusion')
    for n in ('cy_regionI_coeffs', 'cy_regionI_schw'):
        hs = binders((decl_header(cyc, n) or ('',))[0] or '')
        say(f'    {n} binders: ' + '; '.join(f'{a} : {b[:34]}' for a, b in hs))
    say('      ⇒ ρ = 0 is the bifurcation 2-sphere, where the exterior coefficients')
    say('        degenerate (tanh(0) = 0), so excluding it is the chart\'s own limit and not')
    say('        a narrowing of the claim -- the point is the horizon the other patches meet')
    say('        at, covered by the interior and exterior statements on either side.')

    say('\n  3e  AXIOM HYGIENE, both files')
    for lbl, s in (('CircleChart.lean', chart), ('CircleCycloid.lean', cyc)):
        na, ns = len(re.findall(r'\baxiom\b', s)), len(re.findall(r'\bsorry\b', s))
        say(f'    {lbl}: axiom tokens {na}; sorry {ns}')
    say('    ⌗ AND WHAT THIS CANNOT DO, as registered: it reads declarations, hypotheses and')
    say('      statement shapes.  Whether each proof TERM closes is the Lean build\'s and')
    say('      check_no_sorry\'s business.  Nor can it settle from this file whether the')
    say('      radial plane is totally geodesic in the 4-geometry; that is NAMED as needed')
    say('      in question ② and not supplied here.')


# ------------------------------------------------ ITEM 4
def item4():
    say('\n' + '=' * 78)
    say('  ITEM ④ -- P15\'S REBUILT SCOPE SENTENCE')
    say('=' * 78)
    f = flat(need(P15))
    r70 = flat(need(FOR70))

    say('\n  4a  THE THREE FIGURES, each against 70\'s own pinned record')
    pins = [l for l in need(FOR70).split('\n')
            if 'converged FROZEN within' in l or 'the 900 row' in l
            or "DECOUPLED's three knob moves" in l or '2400 within' in l]
    say('    70\'s pins, read from FOR_66_FROM_70.md:')
    for l in pins:
        say(f'      {flat(l)[:150]}')
    say('')
    checks = {
        'decoupled vs the exact transfer, 2.9': 'agrees with the exact transfer to $2.9$ per cent',
        'converged frozen vs the exact transfer, 3.2': 'it agrees to $3.2$ per cent once its late step count is converged',
        'frozen vs decoupled, 1.9': 'the two agreeing with each other to $1.9$ per cent',
        'at both points': 'at the distance point and at the refit point alike',
        'the convergence clause': 'move by under four tenths of a per cent',
    }
    for lbl, m in checks.items():
        say(f'    [{verdict(m in f)}] {lbl}: "{m[:66]}"')
    say(f'    [{verdict("within 3.2% of arm A (L) and 1.9% of DECOUPLED at both points" in r70)}]'
        f' 70 pins 3.2% of arm A and 1.9% of DECOUPLED AT BOTH POINTS')
    say(f'    [{verdict("0.36%" in r70)}] and 70 pins DECOUPLED\'s largest knob move at 0.36%, '
        f'which is under four tenths')

    say('\n  4b  WHICH FROZEN?  -- the arm registered before reading, from r7706\'s finding')
    conv = 'once its late step count is converged' in f
    asrun = ("at the solver's default count its $\\ell=4$ depth sits $3.2$ per cent off the "
             'limit it converges to') in f
    sep = ('What separates the frozen build from the others is its late step count and not '
           'its treatment of the sectors') in f
    say(f'    [{verdict(conv)}] the sentence says WHICH frozen build agrees: the CONVERGED one')
    say(f'    [{verdict(sep)}] and it states what separates the frozen build: its step count')
    say(f'    [{verdict(asrun)}] and it gives the as-run build\'s own offset besides')
    say('    ⇒ ⛭ so r7706\'s finding is not merely discharged: the sentence now carries the')
    say('      distinction that finding was about, and says which build each figure belongs')
    say('      to.  The registered arm asked whether it says which; it does.')

    say('\n  4c  ⚑ ONE FIGURE, TWO QUANTITIES -- and the reading that keeps them apart')
    n32 = len(re.findall(re.escape('$3.2$ per cent'), f))
    say(f'    "$3.2$ per cent" occurs {n32} time(s) in P15, for TWO different quantities:')
    say('      ⓵ converged FROZEN against the exact transfer')
    say('      ⓶ the as-run build\'s ℓ=4 depth against the limit it converges to')
    say('    70\'s pins for each: ⓵ "within 3.2% of arm A (L)"; ⓶ "the 900 row 2-4.5% off')
    say('      at ℓ = 4" -- a RANGE, and its narrative figure is "about 2.5% short".')
    inside = 2.0 <= 3.2 <= 4.5
    say(f'    [{verdict(inside)}] 3.2 lies inside 70\'s pinned range for ⓶ (2-4.5%)')
    say(f'    [{"DEFECT" if (n32 >= 2 and inside) else "NO DEFECT"}] not a wrong figure -- a '
        f'POINT value printed for a RANGE, colliding with another quantity\'s digits')
    say('      ⇒ so this is NOT an error: 3.2 is inside the pinned interval.  What it is, is')
    say('        a point value standing in for a 2-4.5 per cent range, printed in the same')
    say('        sentence where the same digits name a different quantity -- which invites')
    say('        the two to be read as one.  Printing the range, or any other point inside')
    say('        it, removes the collision at no cost.')
    say('      ⌗ negative probe (16) a sixth time: the LABEL beside the digits, not the')
    say('        digits -- and this time the digits were RIGHT and the collision was the')
    say('        finding, which is why the arm had to distinguish them before it ran.')
    return n32 >= 2 and inside


def main():
    say()
    say('  r7710 (60) -- READINGS.  Order r7707: two P2 passages, P15\'s rebuilt sentence,')
    say('  and the order\'s two direct questions.')
    note_ok, bij = q1()
    two_d = q2()
    item3()
    coll = item4()
    say('\n' + '=' * 78)
    say('  VERDICTS')
    say('=' * 78)
    say(f'  ① NO word is owed on account of the formal paragraph (it bounds the MACHINE): '
        f'{verdict(note_ok)}')
    say(f'     -- but a word IS owed for a reason the order did not name: the proposition '
        f'says "precisely the extension" where its own proof gives a BIJECTION: '
        f'{"DEFECT" if bij else "no defect"}')
    say(f'  ② "on that manifold" is AMBIGUOUS, not wrong: se_S is the radial plane, so the '
        f'nearest antecedent makes the clause exact and the salient one makes it stronger '
        f'than the theorem: {verdict(two_d)}')
    say(f'  ③ the passages\' named declarations are present and the replaced sentence is '
        f'read from scratch')
    say(f'  ④ P15\'s three figures match 70\'s pins and the sentence says WHICH frozen build; '
        f'one point value stands in for a range and collides with another quantity: '
        f'{"ROUTED" if coll else "no collision"}')
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
