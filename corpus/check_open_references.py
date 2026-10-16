#!/usr/bin/env python3
"""THE OPEN-REFERENCE RATCHET -- `r7385` ⑨ ⒜ and `r7395` ⑨ ⒞.

** WHAT IT ENFORCES, AND IT IS NOT THIS FILE'S RULE. **  `P7` §frontiers carries a Daryl-directed
block stating the corpus's standing law:

    every "open / frontier / incomplete / remains / not yet / deferred" claim elsewhere in the
    corpus must reference an item here or be struck as a false-open

** WHY IT IS A RATCHET AND NOT A VERDICT. **  `r7385+cc66` priced the law's LITERAL test and it
discharges NOTHING: `P7`'s four items carry LaTeX labels (`frontier:scalar`, `frontier:sm`,
`frontier:quantum`, `frontier:crossing`), the eighteen papers compile SEPARATELY, and a `\\ref`
cannot cross a document boundary -- `0` of `221` candidate sites outside `P7` carried one.  An arm
that reds on "no reference" would red on its entire population, which is the `99`-per-cent artefact
`r7383+cc66.48` refused to report.  ⇒ ** This gate rules NOTHING and reds on ONE thing: a
(paper, sentence, expression) key that is not in the baseline. **  The backlog is frozen; it may not
GROW.  `⑨ ⒜`'s words: *"reporting candidate rows and quoting the law, never ruling."*

** THE KEY IS (paper, normalised marker SENTENCE, expression) ** -- `r7395` ⑨ ⒞: *"a new expression
at a site being a new key"*, over `r7371+cc66.46`'s sentence key, which is `prose_pin_baseline`'s own
rule one level up: *"THE KEY IS (receipt, expression) AND NOT A LINE NUMBER, DELIBERATELY.  An
expression that is reworded is a NEW site and must be read again, which is correct."*

** THE VOCABULARY IS DATA, NOT CODE ** -- corpus/open_vocabulary.tsv, seeded with the law's six plus
the `19` expressions `r7391+cc66.50` MEASURED as the carriers of the census-`OPEN` paragraphs this
arm missed.  Those `19` are `69`'s own alternative forms, not any seat's invention, which is why they
qualify under `r7383` Ⓐ: the vocabulary is harvested, not written by a seat.  An expression a person
marks `NOT-AN-OPEN` leaves the net; that is the ratchet's other direction.

Usage:
    python3 corpus/check_open_references.py              # the gate
    python3 corpus/check_open_references.py --regen      # rewrite the baseline (never a verdict)
"""
import os, re, sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASELINE = os.path.join(ROOT, 'corpus', 'open_reference_baseline.tsv')
VOCABFILE = os.path.join(ROOT, 'corpus', 'open_vocabulary.tsv')
PAPERS = [('P1', 'BH_causality_v2'), ('P2', 'janzen_circle_v3'), ('P3', 'SdS-slicing-curve_v2'),
          ('P4', 'modern_parallax'), ('P5', 'groupoid_paper'), ('P6', 'shadow_of_existence'),
          ('P7', 'CR_framework'), ('P8', 'slicing_operator'), ('P9', 'range_paper'),
          ('P10', 'canonical_time'), ('P11', 'dynamics_paper'), ('P12', 'algebroid_paper'),
          ('P13', 'boundary_paper'), ('P14', 'matter_sector_paper'), ('P15', 'CR_cosmology'),
          ('P16', 'cosmogenesis_paper'), ('P17', 'geometric_core_paper'), ('P18', 'CR_synthesis')]

# the seed, written to open_vocabulary.tsv the first time and read from it after
LAW_SIX = ['open', 'frontier', 'incomplete', 'remains', 'not yet', 'deferred']
HARVEST_19 = [r'not claimed', r'what would', r'is not settled', r'not settled', r'we have not',
              r'\bowed\b', r'undetermined', r'has not been', r'would settle', r'conjectur',
              r'not computed', r'not built', r'we do not claim', r'is missing', r'unresolved',
              r'is not fixed', r'not fixed by', r'remain to be', r'have not been']
# LAW: a word the law itself names.  SEEDED: harvested, not yet read.  The other two are a person's.
VSTATUS = {'LAW', 'SEEDED', 'ADMITTED', 'NOT-AN-OPEN'}
LIVE = {'LAW', 'SEEDED', 'ADMITTED'}            # NOT-AN-OPEN leaves the net

BR = r'\{(?:[^{}]|\{[^{}]*\})*\}'
# ⛭ TWO CORRECTIONS TO THE RUN BEFORE ANY TEST TOUCHES IT, both measured at r7385/r7391+cc66:
#  ⒜ A SECTIONING COMMAND CARRIES NO TERMINAL PUNCTUATION, so the sentence split fuses it with the
#     prose that follows and a bare HEAD veto then loses that prose.  Measured: 4 PROSE open claims
#     were invisible for exactly that reason, among them P3's `\paragraph{Open.} One thing is open,
#     and ...` -- the plainest instance of the claim the law targets.  A heading's OWN words are
#     still never a claim, so the heading is REMOVED rather than used as a veto.
#  ⒝ AN IDENTIFIER IS NOT PROSE.  r7391+cc66.50 measured 13 of 69's 257 census rows reached ONLY
#     through a LaTeX identifier, 3 of them classed OPEN -- a false class in the other instrument.
#     r7395 ⑨: "the guard is a property your arm has and 69's net lacks, and the gate should STATE
#     that rather than inherit it silently", so main() prints it on every run.
STRIP = re.compile(r'\\(?:sub)*section\*?' + BR + r'|\\(?:paragraph|title)' + BR +
                   r'|\\(?:label|ref|eqref|autoref|nameref|pageref|cite|citep|citet|rcpt'
                   r'|includegraphics|input|include)\s*' + BR)
# the three cheap exclusions, measured at r7383+cc66.48.  HEAD is folded into STRIP above.
CLOSE = re.compile(r'rather than (?:left )?open|not left open|no longer open|settles what|'
                   r'which (?:is|was) open|left open[^.]{0,40}(?:is|was|has been) (?:now )?'
                   r'(?:settled|closed|measured|computed)|'
                   r'(?:settled|closed|measured|computed|answered)[^.]{0,30}left open', re.I)
ORD = re.compile(r'\bremains\s+(?:between|the|a|an|that|this|constant|finite|valid|true|unchanged'
                 r'|positive|negative|bounded)\b|\bopen\s+(?:set|interval|ball|neighbourhood'
                 r'|neighborhood|cover|subset|map|condition)\b', re.I)
# the three mechanisms a site may carry.  PRESENCE IS REPORTED, NEVER TREATED AS A DISCHARGE.
MECH = {
    'ref-frontier': re.compile(r'\\(?:ref|autoref|nameref|pageref)\s*\{frontier:[^{}]*\}'),
    'cite-P7':      re.compile(r'\\cite\s*\{[^{}]*JanzenCRframework[^{}]*\}'),
    'rcpt':         re.compile(r'\\rcpt\s*\{[^{}]*\}'),
}
_SENT = re.compile(r'(?<=[.!?])\s+')
# the verdicts a person may write on a SITE.  UNREAD is the only one this file ever writes.
VERDICTS = {'UNREAD', 'REFERENCED', 'FALSE-OPEN', 'NOT-AN-OPEN', 'OWED'}


def write_vocab():
    with open(VOCABFILE, 'w', encoding='utf-8') as fh:
        fh.write('# THE OPEN VOCABULARY -- the net corpus/check_open_references.py casts, as DATA.\n')
        fh.write('# ** THE SEED IS NOT A SEAT\'S LIST. **  LAW-SIX are the six words P7 §frontiers\' own\n')
        fh.write('#   block names.  HARVEST-69 are the 19 expressions r7391+cc66.50 MEASURED as the\n')
        fh.write('#   carriers of the census-OPEN paragraphs the law\'s six miss -- 69\'s own alternative\n')
        fh.write('#   forms, verbatim, which is why they qualify under r7383 Ⓐ.\n')
        fh.write('# ** status is a PERSON\'S column. **  LAW and SEEDED are what this file writes.  A\n')
        fh.write('#   reading turns a SEEDED expression into ADMITTED (it marks open items) or\n')
        fh.write('#   NOT-AN-OPEN (it does not), and NOT-AN-OPEN leaves the net.  Permitted: '
                 + ' '.join(sorted(VSTATUS)) + '.\n')
        fh.write('expression\tsource\tstatus\n')
        for w in LAW_SIX:
            fh.write(f'\\b{w}\\b\tLAW-SIX\tLAW\n')
        for a in HARVEST_19:
            fh.write(f'{a}\tHARVEST-69\tSEEDED\n')


def read_vocab():
    if not os.path.exists(VOCABFILE):
        write_vocab()
    rows = []
    for line in open(VOCABFILE, encoding='utf-8').read().split('\n'):
        if not line or line.startswith('#') or '\t' not in line:
            continue
        f = line.split('\t')
        if f[0] == 'expression':
            continue
        rows.append((f[0], f[1], f[2]))
    return rows


def segments(path):
    """Yield (where, section, text) for every PROSE paragraph and every `%` COMMENT BLOCK.

    ** r7403 ⓮: A COMMENT BLOCK IS IN THE POPULATION, AND HERE IS WHY IT HAS TO BE. **  This
    function used to drop every line whose first non-space character is `%` before anything else
    ran, so a canon note or a `STATUS` block was outside the net at ANY vocabulary.
    r7399+cc66.56 measured the cost: 97 vocabulary matches stranded in those blocks across P1-P18,
    55 of them in papers this arm covers.  *** A canon note or a STATUS block is a CLAIM the
    paper's SOURCE carries, and r7399 proved one can be wrong while the printed paper is right ***
    -- P16's STATUS block called the derivation of eta a remaining open edge while three printed
    sites class it closed.  A population that cannot see that cannot see a whole defect class.

    ** THE UNIT IS THE BLOCK, not the line. **  The corpus writes these as runs: P16's note is nine
    lines of one claim, and keying per line would split one sentence into fragments and manufacture
    keys that are not sites.

    ⌗ The bibliography is cut from both kinds, as before.  Section tracking follows DOCUMENT order
    and is taken from prose lines only, so a comment block reports the section it sits under.
    """
    raw = open(path, encoding='utf-8', errors='replace').read().split('\n')
    out, sec, prose, com = [], '', [], []
    stop = False

    def flush_prose():
        if not prose:
            return
        chunk = '\n'.join(prose)
        for p in re.split(r'\n\s*\n', chunk):
            if p.strip():
                out.append(('PROSE', sec, re.sub(r'\s+', ' ', p)))
        prose.clear()

    def flush_com():
        if com:
            out.append(('COMMENT', sec, re.sub(r'\s+', ' ', ' '.join(com))))
            com.clear()

    for line in raw:
        if line.lstrip().startswith('%'):
            flush_prose()
            com.append(re.sub(r'^\s*%+\s?', '', line))
            continue
        flush_com()
        if '\\begin{thebibliography}' in line:
            stop = True
        if stop:
            continue
        m = re.findall(r'\\(?:sub)*section\*?\{([^}]*)\}', line)
        if m:
            flush_prose()
            sec = m[-1]
        prose.append(line)
    flush_prose()
    flush_com()
    return out


def population(vocab):
    """The candidate keys (paper, sentence, expression).  P7 is the law's home and is out.

    ⌗ r7403 ⓮ ④: P7 STAYS EXCLUDED.  The scope change is the comment blocks and nothing else; P7's
    own 42 comment matches are a separate measurement with its own registration.
    """
    live = [(w, re.compile(w, re.I), src) for w, src, st in vocab if st in LIVE]
    out = {}
    for num, stem in PAPERS:
        if num == 'P7':
            continue
        for where, sec, flat in segments(os.path.join(ROOT, 'corpus', stem + '.tex')):
            for s in _SENT.split(flat):
                k = ' '.join(STRIP.sub(' ', ' '.join(s.split())).split())
                if not k or CLOSE.search(k) or ORD.search(k):
                    continue
                hit = [(w, src) for w, r, src in live if r.search(k)]
                if not hit:
                    continue
                mech = ','.join(n for n, r in MECH.items() if r.search(flat)) or 'none'
                for w, src in hit:
                    out[(num, k, w)] = (sec or '(no section)', src, where, mech)
    return out


def read_baseline():
    if not os.path.exists(BASELINE):
        return None
    rows = {}
    for line in open(BASELINE, encoding='utf-8').read().split('\n'):
        if not line or line.startswith('#') or '\t' not in line:
            continue
        f = line.split('\t')
        if f[0] == 'paper':
            continue
        # ⌗ r7403 ⓮ widened the row: 8 columns with `where`.  A 7-column row is the PRE-⓮
        #   layout and is read as PROSE, so the scope change carries the verdicts already written
        #   rather than resetting them -- a migration that lost a person's column would be worse
        #   than the blindness it fixes.
        if len(f) >= 8:
            rows[(f[0], f[7], f[2])] = (f[1], f[3], f[4], f[5], f[6])
        elif len(f) == 7:
            rows[(f[0], f[6], f[2])] = (f[1], f[3], 'PROSE', f[4], f[5])
    return rows


def write_baseline(pop, prior):
    order = [p for p, _ in PAPERS]
    with open(BASELINE, 'w', encoding='utf-8') as fh:
        fh.write('# THE OPEN-REFERENCE BASELINE -- the frozen backlog of the corpus\'s own standing '
                 'law.\n')
        fh.write('# ** THE KEY IS (paper, normalised marker SENTENCE, expression). **  A reworded '
                 'open claim is a NEW\n')
        fh.write('#   claim, and a NEW EXPRESSION at a site is a NEW key (r7395 ⑨ ⒞).  '
                 'corpus/check_open_references.py\n')
        fh.write('#   reds on a key that is not here and on nothing else: the backlog is frozen, it '
                 'may not GROW.\n')
        fh.write('# ** verdict is a PERSON\'S column. **  --regen writes UNREAD for a new key and '
                 'NEVER changes an\n')
        fh.write('#   existing verdict.  Permitted: ' + ' '.join(sorted(VERDICTS)) + '.\n')
        fh.write('# mechanism is REPORTED, not a discharge: ref-frontier / cite-P7 / rcpt / none.  '
                 'The law\'s literal\n')
        fh.write('#   test (a \\ref to a P7 frontier item) discharges 0 of these, because the papers '
                 'compile separately.\n')
        fh.write('# `where` is PROSE or COMMENT -- r7403 ⓮ put `%` comment BLOCKS in the '
                 'population, because a canon\n')
        fh.write('#   note or a STATUS block is a claim the SOURCE carries and can be wrong while '
                 'the printed paper is right.\n')
        fh.write('paper\tsection\texpression\tsource\twhere\tmechanism\tverdict\tsentence\n')
        for (num, k, w) in sorted(pop, key=lambda t: (order.index(t[0]), t[1], t[2])):
            sec, src, where, mech = pop[(num, k, w)]
            # ⌗ the prior tuple is (section, source, where, mechanism, verdict): verdict is [4].
            verdict = prior.get((num, k, w), (None,) * 4 + ('UNREAD',))[4] if prior else 'UNREAD'
            fh.write('\t'.join((num, sec, w, src, where, mech, verdict, k)) + '\n')


def main(argv):
    vocab = read_vocab()
    bad_st = sorted({st for _w, _s, st in vocab if st not in VSTATUS})
    if bad_st:
        print(f'  [FAIL] open_vocabulary.tsv carries a status that is not one of '
              f'{" ".join(sorted(VSTATUS))}: {" ".join(bad_st)}')
        return 1
    pop = population(vocab)
    prior = read_baseline()
    if '--regen' in argv or prior is None:
        write_baseline(pop, prior)
        print(f'  open-reference baseline written: {len(pop)} key(s) over '
              f'{len({(n, k) for n, k, _w in pop})} site(s).')
        return 0

    live = [w for w, _s, st in vocab if st in LIVE]
    new = sorted(k for k in pop if k not in prior)
    gone = sorted(k for k in prior if k not in pop)
    bad = sorted(v[4] for v in prior.values() if v[4] not in VERDICTS)
    orphan = sorted({w for _n, _k, w in prior} - set(live))
    unread = sum(1 for k in pop if prior.get(k, ('',) * 4 + ('UNREAD',))[4] == 'UNREAD')

    print()
    print('  OPEN-REFERENCE RATCHET -- the corpus\'s own law, enforced as a ratchet and not a verdict')
    print(f'    {len(pop)} key(s) over {len({(n, k) for n, k, _w in pop})} site(s) outside P7; '
          f'{unread} still UNREAD; {len(prior)} baseline row(s)')
    print(f'    vocabulary: {len(live)} live of {len(vocab)} '
          f'({sum(1 for _w, s, _st in vocab if s == "LAW-SIX")} the law\'s own, '
          f'{sum(1 for _w, s, _st in vocab if s == "HARVEST-69")} harvested and measured)')
    print('    ⌗ This gate RULES NOTHING.  The law\'s literal test -- a \\ref to an item in P7')
    print('      §frontiers -- discharges 0 of them: the papers compile separately and a \\ref')
    print('      cannot cross a document boundary.  So it reds on ONE thing: a NEW key.')
    print('    ⛭ AND THE GUARD IS STATED, NOT INHERITED: a marker inside \\rcpt / \\ref / \\label /')
    print('      \\cite is MACHINERY AND NOT PROSE and is stripped before any test.  r7391+cc66.50')
    print('      measured 13 of 69\'s 257 census rows reached ONLY that way, 3 of them classed OPEN.')
    print('      A heading\'s own words are stripped for the same reason, and the prose after a')
    print('      heading in the same sentence-run is NOT -- 4 open claims were lost to that before.')
    print()

    if orphan:
        print(f'  ⌗ {len(orphan)} baseline expression(s) no longer live in the vocabulary '
              f'(read NOT-AN-OPEN, or removed); reported, not a failure: {" ".join(orphan)}')
        print('    Run: python3 corpus/check_open_references.py --regen')
        print()
    if gone:
        print(f'  ⌗ {len(gone)} baseline key(s) no longer in the corpus (reworded, removed, or an '
              f'expression retired); reported, not a failure:')
        for num, k, w in gone[:6]:
            print(f'      {num}  [{w}]  {k[:130]}')
        if len(gone) > 6:
            print(f'      ... and {len(gone) - 6} more')
        print('    Run: python3 corpus/check_open_references.py --regen')
        print()

    if bad:
        print(f'  [FAIL] {len(bad)} baseline row(s) carry a verdict that is not one of '
              f'{" ".join(sorted(VERDICTS))}: {" ".join(sorted(set(bad)))}')
        return 1

    if new:
        bysrc = Counter(f'{pop[k][1]}/{pop[k][2]}' for k in new)
        print(f'  [FAIL] {len(new)} NEW open-language key(s) with no baseline row '
              f'({", ".join(f"{n} {s}" for s, n in bysrc.most_common())}).')
        print('    THE LAW THIS ENFORCES, from P7 §frontiers\' own block:')
        print('      "every \'open / frontier / incomplete / remains / not yet / deferred\' claim')
        print('       elsewhere in the corpus must reference an item here or be struck as a')
        print('       false-open (the result worked elsewhere, the owed reference supplied)"')
        print('    ⌗ The gate does not say these are false-opens.  It says they are UNREAD and that')
        print('      the backlog grew.  Read each one, then add its row with a verdict -- or, if the')
        print('      EXPRESSION is the problem, mark it NOT-AN-OPEN in corpus/open_vocabulary.tsv')
        print('      and it leaves the net.')
        for num, k, w in new[:12]:
            sec, src, where, mech = pop[(num, k, w)]
            print(f'      {num} §{sec}  [{w} / {src} / {where} / {mech}]')
            print(f'        {k[:200]}')
        if len(new) > 12:
            print(f'      ... and {len(new) - 12} more')
        return 1

    print('  no new open-language key: the backlog is frozen and did not grow.')
    print('  ⌗ FROZEN IS NOT DISCHARGED.  The UNREAD count above is the worklist, and it comes')
    print('    down only by a person reading a site and writing its verdict into the baseline,')
    print('    or reading an EXPRESSION and marking it NOT-AN-OPEN in the vocabulary.')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
