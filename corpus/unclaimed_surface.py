#!/usr/bin/env python3
"""unclaimed_surface.py -- WHAT DOES THE CORPUS USE THAT NO THROWN FIELD CLAIMS?

** ⛔⛭⛭ WHY THIS EXISTS, AND IT IS NOT `field_survey` AGAIN. **

  *`corpus/field_survey.py` asks* **"is field X present?"** *-- which requires knowing X in advance.*
  ⇒ *** THAT IS EXACTLY WHY CATEGORY THEORY HID FOR NINETY REVISIONS. ***  *`groupoid` x125 was in
      plain sight; no listed field claimed it, so no survey asked about it, and the reach document's
      own diagnosis is that* **"a groupoid filed under group theory gets baked with group theory's
      tools."**
  ⇒ ** So the question is INVERTED here: take the corpus's own vocabulary, subtract every word any
    thrown field's vocabulary claims, and read what survives. **  *No list of fields is needed to ask
    it, which is the whole point.*

** ⛔ WHAT DOES NOT WORK, RECORDED SO IT IS NOT TRIED AGAIN. **  *The obvious refinement is to rank
the survivors by a statistic instead of reading them.  The natural one is CONCENTRATION -- a
field-signature word should live in a few papers while the corpus's own subject is everywhere.*
  ⇒ ** Measured on the historical case, it fails: **

        word        count   papers   Herfindahl   count x H
        groupoid      125     14        0.278         34.7
        horizon       792     16        0.136        107.6

  ⇒ *** `horizon` OUTRANKS `groupoid` by a factor of three.  A field's signature is defined by
      reference to mathematics OUTSIDE the corpus, and seventeen papers by one author on one
      programme contain no outside to contrast against. ***
  ⇒ ** So the sense pass cannot be automated from internal statistics, and this instrument does not
    pretend to: it BOUNDS the reading and the reading decides. **  *Which is `L-272`'s third pass,
    arrived at a second time and the harder way.*

** ⌗ WHAT IT DOES. **  Tokenises the seventeen de-macroed bodies with LaTeX control sequences and
label payloads stripped, drops a stated stopword list, drops every word claimed by a vocabulary in
`field_survey.FIELDS`, and prints what is left ranked by count.

  ⛭ ** THE CONTROL IS THE HISTORICAL FAILURE ITSELF. **  *Run with category theory removed from the
    claimed set, `groupoid`, `algebroid` and `morphism` must reappear among the survivors -- because
    an instrument built to catch the defect that happened must be shown to catch it.*
  ⚠ ** WHAT IT CANNOT DO. **  *It cannot tell a field's word from the corpus's own object, per the
    negative result above; it cannot see a field used only in symbols; and its stopword list is a
    judgement, stated in full below so it can be argued with.*

    python3 corpus/unclaimed_surface.py
    python3 corpus/unclaimed_surface.py --top 400

Written r3172 (`L-277`).  Stated for reversal.
"""
import collections
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
sys.path.insert(0, HERE)
import reach_baseline as RB                                                # noqa: E402
import field_survey as FS                                                  # noqa: E402

#: ** STATED IN FULL so it can be argued with. **  *Function words and the scaffolding of academic
#: prose.  It deliberately does NOT remove the corpus's own subject nouns -- `horizon`, `slicing`,
#: `substrate` -- because deciding what counts as "the corpus's own" is the judgement this
#: instrument refuses to make on the reader's behalf.*
STOP = set("""the and that this with for from are was were has have had not but its it's they them
their which when where what who whom whose how why all any both each few more most other some such
only own same than too very can will just should now then there here one two three four five six
seven eight nine ten first second third once also into over under above below between within without
because while during before after against about across along among around behind beyond down out off
again further does did doing done being been be am is per via etc we our us you your he she him her
his hers theirs would could may might must shall let lets see cf note thus hence therefore moreover
however although though whereas indeed rather instead give gives given giving take takes taken taking
make makes made making put puts read reads reading say says said carry carries carried carrying hold
holds held holding work works worked working use uses used using need needs needed following follows
followed another every any each single whole part parts case cases way ways thing things side sides
end ends new old long short large small high low big little full empty left right top bottom front
back paper section appendix figure table equation remark theorem lemma proposition corollary proof
itself alone since already merely together neither either whether cannot exactly precisely nothing
worth never these those what's""".split())

MIN_COUNT = 15
WORD = re.compile(r"[A-Za-z][A-Za-z\-']{2,}")


def prose(b):
    """strip LaTeX control sequences, environment names and label/ref/cite payloads"""
    b = re.sub(r'\\(?:label|ref|eqref|cite|rcpt|texttt|url|includegraphics)\{[^{}]*\}', ' ', b)
    b = re.sub(r'\\begin\{[^{}]*\}|\\end\{[^{}]*\}', ' ', b)
    b = re.sub(r'\\[a-zA-Z]+\*?', ' ', b)
    return re.sub(r'[$&_^{}\\~#]', ' ', b)


def vocabulary():
    """{word: count} and {word: {paper: count}} over the de-macroed bodies"""
    per, tot = {}, collections.Counter()
    for p, b in RB.BODIES_TEX.items():
        c = collections.Counter(w.lower() for w in WORD.findall(prose(b)))
        per[p] = c
        tot.update(c)
    return tot, per


def claimed(skip=()):
    """every word form any thrown field's vocabulary claims, optionally skipping fields by name"""
    out = set()
    for name, _ledger, terms in FS.FIELDS:
        if any(s.lower() in name.lower() for s in skip):
            continue
        for t in terms:
            out.update(w.lower() for w in WORD.findall(t))
    return out


def survivors(skip=(), min_count=MIN_COUNT):
    tot, _ = vocabulary()
    cl = claimed(skip)
    out = [(w, n) for w, n in tot.items()
           if n >= min_count and w not in STOP and w not in cl]
    out.sort(key=lambda x: -x[1])
    return out


def herfindahl(w, tot, per):
    n = tot[w]
    return sum((per[p][w] / n) ** 2 for p in per) if n else 0.0


def main():
    print()
    print('  unclaimed_surface -- what does the corpus use that no thrown field claims?')
    print()
    tot, per = vocabulary()
    print(f'    distinct word forms in the seventeen bodies : {len(tot)}')
    live = survivors()
    print(f'    surviving stopwords, claimed terms, count<{MIN_COUNT} : {len(live)}')

    # ** THE CONTROL: the instrument must contain the defect that actually happened. **
    without_ct = dict(survivors(skip=('category theory',)))
    hist = {w: without_ct.get(w) for w in ('groupoid', 'algebroid', 'morphism')}
    print()
    print('    CONTROL -- with category theory removed from the claimed set, the field that '
          'actually hid must reappear:')
    for w, n in hist.items():
        print(f'      {w:12s} {"×" + str(n) if n else "ABSENT"}')
    if not all(hist.values()):
        print()
        print('    ⛔ [FAIL] the historical case does not survive its own instrument.')
        print('       *An instrument built to catch the defect that happened must catch it.*')
        print()
        return 1
    print('    the historical case is contained — the instrument would have surfaced it.')
    print()
    top = int(sys.argv[sys.argv.index('--top') + 1]) if '--top' in sys.argv else 200
    print(f'    the unclaimed surface, top {top} by count '
          '(⌗ A COUNT IS NOT A FIELD — this bounds the reading, it does not do it):')
    print()
    for i in range(0, min(top, len(live)), 4):
        print('    ' + '  '.join(f'{w:>20s} {n:<5d}' for w, n in live[i:i + 4]))
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
