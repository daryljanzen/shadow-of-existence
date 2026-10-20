#!/usr/bin/env python3
"""
r7454 -- THE PAPER'S OWN OPEN LIST AGAINST THE MEASUREMENTS THE CORPUS CARRIES.

Registered at PREDICTION.md (d47db6d6) before this file existed.

WHAT IS MECHANICAL AND WHAT IS ADJUDICATED, stated here so the output cannot be read
as more than it is:

  MECHANICAL -- the seven-row table's parse; the enumeration of P18's open-item
  sentences; each item's figures and cited keys; the resolution of a cited key to a
  corpus file; which lines of the CITED file carry one of the item's own figures
  together with a settlement marker.

  ADJUDICATED -- the VERDICT on each item, printed as ADJUDICATED with the quote that
  carries it, never as a measured quantity.  r7450 was voided for inferring from the
  record what the record states.

⌗ THE FIRST DRAFT OF THIS FILE OVER-FIRED AND THE CORRECTION IS PART OF THE
  MEASUREMENT.  It scored evidence by shared distinctive words -- words of five letters
  or more occurring in under two per cent of a 146,677-line population -- and returned
  1,543 evidence lines for the first table row, 135 of them carrying a settlement
  marker.  At that rate every item in the corpus is answered by something, so the
  over-fire control of PREDICTION.md Ⓥ① would have passed anything and the instrument
  would have reported the abundance of its own matches as a fact about the paper.
  ** That is this cycle's own generator, in the instrument built to look for it. **
  The rule below replaces it with the conjunction that actually found the one case this
  seat already had: THE ITEM'S OWN CITED SOURCE, THE ITEM'S OWN FIGURES, AND AN
  EXPLICIT SETTLEMENT IN THE SAME SENTENCE.  Three conjuncts, each checkable by a
  reader against the printed line.

⌘ AND THE SECOND DRAFT UNDER-FIRED, WHICH REGISTRATION CAUGHT BECAUSE THE ANSWER WAS
  DECLARED.  PREDICTION.md Ⓣ① records, before any code existed, that P18's sentence
  *"Which term of the projection makes it is the open computation"* is refuted in the
  paper it cites one sentence earlier.  The second draft returned NOT-REFUTED for it.
  ** The reason is a unit mismatch and not a threshold: the SUBJECT is a sentence and the
  MEASUREMENT was a line. **  The two figures that tie the sentence to its source,
  `0.996` and `1.045`, sit on the line above the sentence, so a line-keyed item carried
  no figures and the first conjunct could never be met.  The same mismatch was on the
  evidence side, where a settlement and a figure had to fall on one line of the cited
  file to be seen together.
  ** Both sides are sentences below. **  This is the family's own shape a third time in
  one instrument -- a population whose unit was narrower than its subject while its
  logic was correct -- and it is recorded rather than quietly repaired because what
  caught it was the declaration and not the gate.

⌘ A four-word run of ordinary words is not evidence either.  The second draft matched
  *"what is not settled"* between P18 and the framework paper and called it a
  refutation candidate on a phrase made entirely of stopwords.  A run now has to carry
  at least two words of five letters or more that are not stopwords.
"""
import os, re, sys, time, glob, collections

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
P18_FILE = 'corpus/CR_synthesis.tex'
TITLES = 'corpus/CANONICAL_TITLES.txt'

# The fixed settlement-marker list.  A marker asserts a question CLOSED.  A marker that
# asserts a LIMIT ("cannot be resolved", "the sky cannot tell") is deliberately absent:
# a limit is the state of an open item, not its settlement, and the first draft's
# inclusion of the bare "cannot be" is what let a data-gated step read as answered.
SETTLED = [
    'no single', 'not by any one', 'is excluded', 'is answered', 'answered rather than',
    'stated as a law', 'is settled', 'is not the channel', 'settled negatively',
    'is established rather than', 'rather than owed', 'and is answered', 'now answered',
    'is not open', 'closes exactly', 'is a result',
]

OPENMARK = [
    'is the open', 'remains open', 'left open', 'is open', 'not settled', 'is owed',
    'unmeasured', 'open computation', 'open item', 'open work', 'genuinely unpaid',
    'what is open', 'names as owed',
]

STOP = set('''the a an and or of to in on at is are was were be been for with that this
those these it its as by from into than then so not no which what where whether when
how why who whom all any both each few more most other some such only own same too very
can will just should now here there one two three four five six seven eight nine ten
rather instead against about above below under over between among through during before
after while because since although though however therefore thus hence item items open
stands stand standing carries carry carried says say said state states stated'''.split())

SENT_END = re.compile(r'(?<=[.!?])\s+')


def sentences(path):
    """(first line, sentence, the paragraph it sits in) for a tex file.

    A paragraph is a run of non-blank, non-comment lines.  Line anchors are kept so a
    reader can open the file at the place the instrument read.  The paragraph is carried
    because a claim's citation is very often in the sentence BEFORE it -- which is
    exactly where P18 puts the cosmology paper for the claim this revision is about.
    """
    out = []
    para, start = [], None
    def flush():
        if not para:
            return
        joined = ' '.join(para)
        for s in SENT_END.split(joined):
            s = s.strip()
            if s:
                out.append((start, s, joined))
        del para[:]
    for n, ln in enumerate(read(path).split('\n'), 1):
        if ln.startswith('%'):
            continue
        if not ln.strip():
            flush(); start = None; continue
        if start is None:
            start = n
        para.append(ln)
    flush()
    return out


def has_run(item_text, target_low):
    """A contiguous run of the item's own words carrying >= 2 distinctive words."""
    words = [w for w in re.findall(r"[a-z']+", item_text.lower()) if w]
    best = None
    for i in range(max(0, len(words) - 3)):
        gram = words[i:i + 4]
        if len([w for w in gram if len(w) >= 5 and w not in STOP]) < 2:
            continue
        g = ' '.join(gram)
        if g in target_low:
            if best is None or len(g) > len(best):
                best = g
    return best

UNREACHABLE, NOT_REFUTED, CANDIDATE = 'UNREACHABLE', 'NO-MARKER-MATCHED', 'REFUTATION-CANDIDATE'


def read(p):
    with open(os.path.join(ROOT, p), encoding='utf-8', errors='replace') as fh:
        return fh.read()


def strip_tex(s):
    s = re.sub(r'\\(emph|textbf|textit|text|mathrm|mathcal)\{([^{}]*)\}', r'\2', s)
    for pat in (r'\\rcpt\{[^}]*\}', r'\\cite\{[^}]*\}', r'\\S?\\ref\{[^}]*\}'):
        s = re.sub(pat, ' ', s)
    s = re.sub(r'\\[a-zA-Z]+', ' ', s)
    s = s.replace('$', '').replace('{', ' ').replace('}', ' ').replace('~', ' ')
    return re.sub(r'\s+', ' ', s).strip()


def figures(s):
    return sorted({m for m in re.findall(r'\d+\.\d+', s)})


def shares_figure(item_figs, text):
    """WHOLE-TOKEN figure match.

    ⌘ The void run's Ⓣ① fired on this: `f in flat` is a SUBSTRING test, so the
      data-gated step's `0.9` matched `0.992` and `0.996` and the step came back
      answered.  A figure is a token, and two numbers sharing a prefix share nothing.
    """
    present = set(re.findall(r'\d+(?:\.\d+)?', text))
    return [f for f in item_figs if f in present]


def cited(raw):
    out = []
    for pat in (r'\\cite\{([^}]*)\}', r'\\rcpt\{([^}]*)\}'):
        for m in re.findall(pat, raw):
            for k in m.split(','):
                if k.strip():
                    out.append(k.strip())
    return out


def keyset(s):
    return {w for w in re.findall(r'[a-z\-]{5,}', s.lower()) if w not in STOP}


# ------------------------------------------------- cite key -> corpus file, mechanically
def cite_map():
    m = {}
    for ln in read(TITLES).split('\n'):
        if '|' not in ln or ln.startswith('#'):
            continue
        parts = [p.strip() for p in ln.split('|')]
        stem = parts[0]
        path = 'corpus/%s.tex' % stem
        if not os.path.exists(os.path.join(ROOT, path)):
            continue
        for k in parts[1].split(','):
            if k.strip():
                m[k.strip()] = path
    return m


def receipt_map():
    m = {}
    for p in glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True):
        m[os.path.splitext(os.path.basename(p))[0]] = os.path.relpath(p, ROOT)
    return m


# ------------------------------------------------------------------ the population
def table_rows(tex):
    i = tex.find('\\emph{open item} & \\emph{what would discharge it}')
    if i < 0:
        return []
    j = tex.find('\\end{tabular}', i)
    rows = []
    for raw in tex[tex.find('\\hline', i + 10):j].split('\\\\'):
        raw = raw.replace('\\hline', '').strip()
        if '&' not in raw:
            continue
        what, disc = raw.split('&', 1)
        if strip_tex(what) and 'open item' not in strip_tex(what):
            rows.append((strip_tex(what), raw))
    return rows


def frontier_paragraphs(tex):
    """The paragraphs of sec:frontier, which is where a table row's citations live."""
    i = tex.find('\\label{sec:frontier}')
    j = tex.find('\\section{', i + 10)
    paras = []
    for blk in tex[i:j].split('\n\n'):
        if '\\cite{' in blk or '\\rcpt{' in blk:
            paras.append(blk)
    return paras


# A marker reached through one of these is a CLOSURE statement, not an open-item claim.
NEGATED = ['rather than left', 'rather than being left', 'not left', 'no longer',
           'is not among the', 'not open', 'rather than open']


def open_sentences(_tex):
    """P18's open-item claims, as SENTENCES.

    ⌘ Three population defects, each found by reading the run's own output and each
      recorded rather than quietly repaired:
      (i) the unit was a LINE, so a claim's figures fell outside it -- see the docstring;
      (ii) the seven-row TABLE matched as prose and was counted twice, once as a parsed
           row and once as a sentence whose text is the tabular preamble;
      (iii) a marker reached through a negation -- *"the answer is settled negatively
            RATHER THAN LEFT OPEN"* -- was read as a claim that something is open, when
            the sentence says the opposite.  The population was counting closures as
            open items, which is this family's shape pointed the other way.
    """
    tex = read(P18_FILE)
    tb0 = tex.find('\\begin{small}\n\\noindent\\begin{tabular}')
    tb1 = tex.find('\\end{tabular}', tb0) if tb0 >= 0 else -1
    tbl0 = tex[:tb0].count('\n') + 1 if tb0 >= 0 else -1
    tbl1 = tex[:tb1].count('\n') + 1 if tb1 >= 0 else -1

    out = []
    for n, s, para in sentences(P18_FILE):
        if len(s) < 30:
            continue
        if tbl0 > 0 and tbl0 <= n <= tbl1:
            continue                      # (ii) the table is parsed as rows, not prose
        if s.lstrip().startswith('\\subsection') or s.lstrip().startswith('\\section'):
            continue                      # a heading is not a claim
        low = strip_tex(s).lower()
        hit = [m for m in OPENMARK if m in low]
        if not hit:
            continue
        if any(neg in low for neg in NEGATED):
            continue                      # (iii) a closure is not an open item
        out.append((n, s, para))
    return out


# ------------------------------------------------------------------ the locator
def locate(item_figs, item_text, sources, cmap, rmap):
    """THE THREE CONJUNCTS.  Returns (state, evidence).

      1. the line is in a file the ITEM ITSELF cites;
      2. it carries one of the ITEM'S OWN figures, or a contiguous four-word run of the
         item's own words;
      3. it carries a settlement marker in the same line.
    """
    paths = []
    for k in sources:
        if k in cmap:
            paths.append(cmap[k])
        elif k in rmap:
            paths.append(rmap[k])
    paths = sorted(set(paths))
    if not paths:
        return UNREACHABLE, [], paths

    ev = []
    for path in paths:
        sents = sentences(path)
        for i, (n, s, _para) in enumerate(sents):
            # the unit is a sentence AND ITS SUCCESSOR: a settlement very often follows
            # the restatement of what it settles, which is one level up from the
            # line-versus-sentence mismatch the void run already carried.
            s2 = s if i + 1 >= len(sents) else s + ' ' + sents[i + 1][1]
            flat = strip_tex(s2)
            low = flat.lower()
            if not any(m in low for m in SETTLED):
                continue
            shared = shares_figure(item_figs, flat)
            if shared:
                why = 'figure ' + ', '.join(shared)
            else:
                run = has_run(item_text, low)
                why = 'run "%s"' % run if run else None
            if why:
                ev.append((path, n, flat, why))
    return (CANDIDATE if ev else NOT_REFUTED), ev, paths



# ------------------------------------------------------------------ the controls
# PREDICTION.md Ⓣ①–Ⓣ③.  Each control's claim text is quoted from the record and its
# source named, so a reader can check that the control was not written to pass.
CONTROLS = [
    ('Ⓣ① OVER-FIRE, the data-gated step',
     'PO-87, and P15 sec:refit-bound',
     'what displaces the fourth peak is open: the fourth peak is 0.9 to 1.3 standard '
     'deviations out with most of that offset shared with the control, and a candidate '
     'there can be computed but not tested against this datum',
     ['JanzenCRcosmology'], NOT_REFUTED),
    ('Ⓣ② OVER-FIRE, a row no receipt measures',
     'PO-91, opened r7393 from the residue of 69’s census',
     'whether the sweep’s asymmetry is purely an artefact of the vantage, or whether the '
     'vantage-dependence itself encodes something physical about how such geometries are '
     'observed, is a question this construction raises and leaves open',
     ['JanzenDynamics'], NOT_REFUTED),
    ('Ⓣ③ UNDER-FIRE, an item the record states as answered',
     'PO-50’s live item, retired at r7222',
     'the direction of the correction is contested in print, the caustic route putting '
     'the turnaround-enclosed mass above the virial one and the Local Volume flow route '
     'putting the mass inside the zero-velocity surface at about six tenths of it, '
     'measured over four profile families and twenty-two members it runs 1.165 to 5.228',
     ['P03_the_enclosed_mass_is_monotone_so_the_turnaround_ratio_cannot_fall_below_one_'
      'and_the_contested_direction_is_two_different_quantities'], CANDIDATE),
]


def run_controls(cmap, rmap):
    print('\n' + '=' * 78)
    print('THE CONTROLS.  A control that fires VOIDS THE RUN -- PREDICTION.md says so and')
    print('the void run is kept in the tree, as r7450\'s was.')
    print('=' * 78)
    fired = []
    for name, where, claim, keys, expect in CONTROLS:
        figs = figures(claim)
        state, ev, paths = locate(figs, claim, keys, cmap, rmap)
        ok = (state == expect)
        print('\n%s  %s' % ('✓' if ok else '⛔', name))
        print('     quoted from: %s' % where)
        print('     expected %s | got %s | figures %s' % (expect, state, figs or '-'))
        print('     searched: %s' % (', '.join(paths) or '(nothing resolved)'))
        for path, n, flat, why in ev[:2]:
            print('       ⊢ %s:%d  [%s]  %s' % (path, n, why, flat[:140]))
        if not ok:
            fired.append(name)
    print('\n' + '-' * 78)
    if fired:
        print('⛔ %d CONTROL(S) FIRED.  THE RUN IS VOID:' % len(fired))
        for f in fired:
            print('    %s' % f)
        print('  The verdicts above are not to be read as findings.  The instrument is')
        print('  the measurement, and this is what it measured about itself.')
    else:
        print('✓ ALL THREE CONTROLS HELD -- the locator neither reports an open item')
        print('  answered nor fails to find an answer the corpus carries.')
    return fired


def main():
    t0 = time.time()
    tex = read(P18_FILE)
    cmap, rmap = cite_map(), receipt_map()

    print('=' * 78)
    print("r7454 -- THE PAPER'S OWN OPEN LIST AGAINST THE MEASUREMENTS THE CORPUS CARRIES")
    print('=' * 78)
    print('cite keys resolved to corpus files: %d | receipt names resolvable: %d'
          % (len(cmap), len(rmap)))

    rows = table_rows(tex)
    print('\n-- Ⓐ  THE TABLE PARSES TO %d ROWS.  The paper says seven, twice.' % len(rows))

    paras = frontier_paragraphs(tex)
    items = []
    for i, (what, raw) in enumerate(rows, 1):
        src = cited(raw)
        resolved_from = 'the row itself'
        if not src:
            # the row carries no citation; resolve to the sec:frontier paragraph with the
            # largest distinctive-word overlap, and PRINT which one, so it is checkable.
            best, bestn = None, 0
            kw = keyset(what)
            for blk in paras:
                ov = len(kw & keyset(strip_tex(blk)))
                if ov > bestn:
                    best, bestn = blk, ov
            if best is not None and bestn >= 2:
                src = cited(best)
                resolved_from = 'sec:frontier paragraph, %d words shared: %s...' % (
                    bestn, strip_tex(best)[:60])
        items.append(('T%d' % i, what, what, raw, src, resolved_from))

    sents = open_sentences(tex)
    print('-- THE PROSE POPULATION: %d sentences in P18 name something open or owed.'
          % len(sents))
    for n, raw, para in sents:
        src_keys, how = cited(raw), 'the claim\'s own sentence'
        figs_scope = raw
        if not src_keys:
            # the citation is very often in the sentence BEFORE the claim.  Widen to the
            # paragraph and SAY SO, rather than reporting a claim untestable because its
            # source sits one sentence away.
            src_keys, how = cited(para), "the claim's own PARAGRAPH"
            figs_scope = para
        items.append(('L%d' % n, strip_tex(raw)[:72], strip_tex(raw), figs_scope,
                      src_keys, how))

    print('\n' + '=' * 78)
    print('PER ITEM.  Three conjuncts: the item\'s own cited source, the item\'s own')
    print("figures or a four-word run of its own words, and a settlement in the line.")
    print('=' * 78)

    tally = collections.Counter()
    for tag, label, text, raw, src, how in items:
        figs = figures(raw)
        state, ev, paths = locate(figs, text, src, cmap, rmap)
        tally[state] += 1
        mark = {CANDIDATE: '⚑', NOT_REFUTED: ' ', UNREACHABLE: '⌗'}[state]
        print('\n%s [%s] %s' % (mark, tag, label))
        print('      state %s | figures %s | cited %s' % (state, figs or '-', src or '-'))
        if state == UNREACHABLE:
            print('      ⌗ no cited source resolves, so this item is NOT TESTED by this')
            print('        instrument.  UNREACHABLE is its own state and is not NOT-REFUTED.')
        else:
            print('      searched: %s   (resolved via %s)' % (', '.join(paths), how))
        for path, n, flat, why in ev[:4]:
            print('      ⊢ %s:%d  [%s]' % (path, n, why))
            print('        %s' % flat[:200])

    print('\n' + '=' * 78)
    print('THE TALLY, MECHANICAL')
    print('=' * 78)
    for k in (CANDIDATE, NOT_REFUTED, UNREACHABLE):
        print('  %-22s %d' % (k, tally[k]))
    fired = run_controls(cmap, rmap)
    print('\nprice %.1fs' % (time.time() - t0))
    return items, tally, fired


def seed():
    """The assertions that fail if any of the four repairs regresses.

    Each one is a defect this run actually had, written as a test so the next reader of
    this file does not have to find it twice.
    """
    fails = []

    def ck(name, cond):
        print('  %s %s' % ('\u2713' if cond else '\u26d4', name))
        if not cond:
            fails.append(name)

    tex = read(P18_FILE)
    rows = table_rows(tex)
    sents = open_sentences(tex)
    cmap, rmap = cite_map(), receipt_map()
    flat = {n: strip_tex(x) for n, x, _ in sents}

    print('SEED')
    ck('the table parses to seven rows', len(rows) == 7)
    ck('a figure is a token, not a substring: 0.9 does not match 0.992',
       shares_figure(['0.9'], 'the ratio is 0.992 here') == [])
    ck('a figure still matches itself', shares_figure(['1.045'], "spectrum's 1.045,") == ['1.045'])
    ck('the cite key resolves to the cited paper',
       cmap.get('JanzenCRcosmology') == 'corpus/CR_cosmology.tex')
    target = [n for n, t in flat.items() if t.startswith('Which term of the projection')]
    ck('the claim this revision is about is in the population', len(target) == 1)
    if target:
        raw = [x for n, x, _ in sents if n == target[0]][0]
        para = [pa for n, _, pa in sents if n == target[0]][0]
        ck('the claim is one sentence, not a line fragment', raw.strip().endswith('computation.'))
        ck('its source resolves through its paragraph, not its own sentence',
           not cited(raw) and 'JanzenCRcosmology' in cited(para))
        ck('and its own figures are reachable at paragraph scope',
           '1.045' in figures(para) and '0.996' in figures(para))
    ck('a closure is not counted as an open item',
       not any('settled negatively rather than left open' in t for t in flat.values()))
    ck('the tabular preamble is not counted as a claim',
       not any('begin tabular' in t or 'p 0.46' in t for t in flat.values()))
    ck('the cited paper carries the negation of the claim\'s own form',
       any('no single term is the channel' in strip_tex(x).lower()
           for _, x, _ in sentences('corpus/CR_cosmology.tex')))
    print('\n  %d assertion(s) failing' % len(fails))
    return fails


if __name__ == '__main__' and '--seed' in sys.argv:
    seed()
elif __name__ == '__main__' and '--sound' not in sys.argv:
    main()


# ============================================================================
# THE SOUND HALF.
#
# main() above is the VOID run and is kept.  Its controls fired twice and the second
# firing is not a bug:
#
#   Ⓣ① fires because the item's OWN figures sit, in the item's OWN cited source, in a
#   sentence pair that OWN carries a settlement marker -- and the item is still open.
#   ** Co-occurrence is not aboutness. **  No threshold repairs that; the three-conjunct
#   rule is answering a different question from the one it was built for, which is this
#   cycle's generator stated in its own words: an instrument built to check a condition
#   that already exists will disagree with it, and the disagreement will look like a
#   finding about the subject.
#
#   Ⓣ③ fires because the corpus closes questions in words no fixed list contains --
#   *"THERE IS NO CONTESTED DIRECTION"*, *"the quotient is bounded below by one"*, *"the
#   convention account is ELIMINATED"*.  The list is NOT grown to reach them.  Growing a
#   word list until the figure agrees is the one move this programme has refused since
#   r7125, and refusing it here is worth more than a passing control.
#
# So NOT-REFUTED was renamed NO-MARKER-MATCHED, and nothing below infers an item's state
# from a count.  What follows reports only what the record EXPLICITLY STATES, and labels
# every verdict as this seat's adjudication.
# ============================================================================

FRONTIER = 'THE_FRONTIER.md'


def live_frontier_rows():
    rows = []
    for ln in read(FRONTIER).split('\n'):
        if ln.startswith('| **PO-') and ln.count('|') >= 9:
            cells = ln.split('|')
            rows.append((cells[1].strip().strip('*'), cells[2].strip()))
    return rows


def sound():
    t0 = time.time()
    tex = read(P18_FILE)
    rows = table_rows(tex)
    sents = open_sentences(tex)

    print('=' * 78)
    print('r7454 SOUND -- WHAT THE RECORD STATES, WITH NOTHING INFERRED FROM A COUNT')
    print('=' * 78)

    # ---- MECHANICAL, and independent of the void: which claims cite nothing at all.
    nocite = [(n, strip_tex(s)) for n, s, para in sents if not cited(s) and not cited(para)]
    print('\n⚑ Ⓐ  THE TABLE PARSES TO %d ROWS.  P18 says seven, twice.  HIT.' % len(rows))
    print('\n⚑ THE ONE THING THIS CENSUS CAN ASSERT MECHANICALLY, AND IT IS A PARSE AND NOT')
    print('  A VERDICT: ** %d of P18\'s %d open-item claims cite NOTHING, in the claim\'s own'
          % (len(nocite), len(sents)))
    print('  sentence or anywhere in its paragraph. **  An uncited claim about what is open')
    print('  cannot be checked against a source by any instrument that follows citations --')
    print('  not by a better locator, and not by a reader either, without guessing which')
    print('  result the claim is about.  This stands whatever the void above does.')
    for n, s in nocite:
        print('    ⊢ %s:%d  %s' % (P18_FILE, n, s[:118]))

    # ---- Ⓔ / Ⓕ : the seven against the register, mechanically, with the match printed.
    print('\n' + '=' * 78)
    print('Ⓔ  THE SEVEN AGAINST THE REGISTER\'S LIVE ROWS')
    print('=' * 78)
    fr = live_frontier_rows()
    matched = 0
    for i, (what, _raw) in enumerate(rows, 1):
        kw = keyset(what)
        best, bestn = None, 0
        for rid, rwhat in fr:
            ov = len(kw & keyset(rwhat))
            if ov > bestn:
                best, bestn = (rid, rwhat), ov
        if bestn >= 2:
            matched += 1
            print('  %d. %-52s → %s  (%d words shared)' % (i, what[:52], best[0], bestn))
            print('     %s' % best[1][:112])
        else:
            print('  %d. %-52s → no live row' % (i, what[:52]))
    print('\n  ** %d of the seven carry a live frontier row. **' % matched)

    # ---- Ⓖ : does any OTHER paper assert the term computation open?
    print('\n' + '=' * 78)
    print('Ⓖ  DOES ANY PAPER BUT P18 ASSERT THE TERM COMPUTATION IS OPEN?')
    print('=' * 78)
    needles = ['which term of the projection', 'term of the projection makes',
               'is the open computation']
    others = []
    for p in sorted(glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))):
        rel = os.path.relpath(p, ROOT)
        for n, s, _ in sentences(rel):
            low = strip_tex(s).lower()
            if any(nd in low for nd in needles):
                others.append((rel, n, strip_tex(s)))
    for rel, n, s in others:
        print('  ⊢ %s:%d  %s' % (rel, n, s[:130]))
    print('\n  ** %d occurrence(s), in %d paper(s). **'
          % (len(others), len({r for r, _, _ in others})))

    # ---- the adjudication, labelled, quoting the cited source in full.
    print('\n' + '=' * 78)
    print('THE ADJUDICATION.  THIS SEAT\'S, NOT THE INSTRUMENT\'S, AND LABELLED AS SUCH.')
    print('=' * 78)
    print("""
ADJUDICATED ① -- P18's claim is refuted by the paper it cites one sentence earlier.

  P18 (%s, in the sentence after it cites the cosmology paper for the
  0.996/1.045 pair):

      "Which term of the projection makes it is the open computation."

  The cited paper, in its own published text, states the answer and states it as a
  negation of the question's form:""" % P18_FILE)
    for needle in ['no single term is the channel',
                   'nor by any one source term',
                   'and so now is the mechanism',
                   'the mechanism is the kernel']:
        for n, s, _ in sentences('corpus/CR_cosmology.tex'):
            low = strip_tex(s).lower()
            if needle in low:
                print('\n      ⊢ corpus/CR_cosmology.tex:%d' % n)
                frag = strip_tex(s)
                i = low.find(needle)
                print('        ...%s...' % frag[max(0, i - 190):i + 210])
                break
    print("""
  ⇒ ** THE ITEM IS ANSWERED, AND ANSWERED AGAINST ITS OWN FORM. **  "Which term"
    has no answer of the shape it asks for, because the cited paper's answer is that
    there is no term: the projection raises this arm's contrast on nearly everything it
    projects.  An item like that cannot be discharged by doing what it asks, which is
    why it is worth separating from an item that is merely unrun.

  ⇒ ** AND THE NEXT QUESTION IS ALREADY ANSWERED TOO, WHICH THE CLAIM DOES NOT KNOW. **
    The cited paper states the mechanism as a law with nothing fitted in it, holding to
    within ten per cent of the measured amplitude on both arms at every band.  So the
    sentence does not merely lag one result; it names as open the last two steps of a
    chain the cited paper closes.

ADJUDICATED ② -- and PO-87 inherited it.

  PO-87's step (1), minted at r7393 from this sentence, reads: *"WHICH TERM OF THE
  PROJECTION MAKES THE CONTRAST EXCESS ... which term of the projection makes it is the
  open computation."*  A seat taking that step works a measurement the corpus holds in
  two receipts and in the cited paper's own prose.  ** The step is retired, and what is
  open in its place is not a term. **

  What IS open, stated from the cited paper's own words rather than invented here: the
  retention is what the kernel's acceptance makes of a given projection distance, and so
  it turns on WHICH RATE THAT DISTANCE IS BUILT ON -- the one assignment where what the
  construction specifies and what the sky prefers come apart.  That is a question about
  the line-of-sight integral on this background, it is named in the cited paper, and it
  is not "which term".

ADJUDICATED ③ -- the instrument's own verdict on the instrument.

  The mechanical half cannot certify ①.  It displays the same two sentences, but its
  conjunction -- the item's cited source, the item's figures, a settlement marker --
  also fires on P18's fourth-peak item, which is open and data-gated.  ** So the output
  that agrees with the reading is not evidence for it. **  What established ① is the
  record's own explicit statement, read; and PREDICTION.md recorded it as DECLARED
  before any code existed, which is the only reason the void run's disagreement with it
  was visible at all.
""")
    print('price %.1fs' % (time.time() - t0))


if __name__ == '__main__' and '--sound' in sys.argv:
    sound()
