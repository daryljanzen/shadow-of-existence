#!/usr/bin/env python3
"""THE OPEN-REFERENCE RATCHET -- `r7385` ⑨ ⒜ + ⒞.

** WHAT IT ENFORCES, AND IT IS NOT THIS FILE'S RULE. **  `P7` §frontiers carries a Daryl-directed
block stating the corpus's standing law:

    every "open / frontier / incomplete / remains / not yet / deferred" claim elsewhere in the
    corpus must reference an item here or be struck as a false-open

** WHY IT IS A RATCHET AND NOT A VERDICT. **  `r7385+cc66` priced the law's LITERAL test and it
discharges NOTHING: `P7`'s four items carry LaTeX labels (`frontier:scalar`, `frontier:sm`,
`frontier:quantum`, `frontier:crossing`), the eighteen papers compile separately, and a `\\ref`
cannot cross a document boundary -- `0` of `221` candidate sites outside `P7` carry one.  So an arm
that reds on "no reference" would red on its entire population, which is the `99`-per-cent artefact
`r7383+cc66.48` refused to report.  ⇒ ** This gate therefore rules NOTHING and reds on ONE thing:
a candidate site that is not in the baseline. **  The backlog is frozen; it may not GROW.

⌗ `⑨ ⒜`'s words: *"reporting candidate rows and quoting the law, never ruling."*  Every verdict in
this file is `UNREAD` until a person writes another one into the baseline.

** THE KEY IS (paper, normalised marker SENTENCE) ** -- `r7371+cc66.46`, and `prose_pin_baseline`'s
own rule one level up: *"THE KEY IS (receipt, expression) AND NOT A LINE NUMBER, DELIBERATELY.  An
expression that is reworded is a NEW site and must be read again, which is correct."*  A reworded
open claim is a new claim and is read again.

Usage:
    python3 corpus/check_open_references.py              # the gate
    python3 corpus/check_open_references.py --regen      # rewrite the baseline from the corpus
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASELINE = os.path.join(ROOT, 'corpus', 'open_reference_baseline.tsv')
PAPERS = [('P1', 'BH_causality_v2'), ('P2', 'janzen_circle_v3'), ('P3', 'SdS-slicing-curve_v2'),
          ('P4', 'modern_parallax'), ('P5', 'groupoid_paper'), ('P6', 'shadow_of_existence'),
          ('P7', 'CR_framework'), ('P8', 'slicing_operator'), ('P9', 'range_paper'),
          ('P10', 'canonical_time'), ('P11', 'dynamics_paper'), ('P12', 'algebroid_paper'),
          ('P13', 'boundary_paper'), ('P14', 'matter_sector_paper'), ('P15', 'CR_cosmology'),
          ('P16', 'cosmogenesis_paper'), ('P17', 'geometric_core_paper'), ('P18', 'CR_synthesis')]

# the law's own six words, from P7 §frontiers' block and not from this file
LAW = re.compile(r'\b(open|frontier|incomplete|remains|not yet|deferred)\b', re.I)
# the three cheap exclusions, measured at r7383+cc66.48 and each one priced there
EXCL = {
    'HEAD':  re.compile(r'\\(?:sub)*section\*?\{|\\paragraph\{|\\title\{'),
    'CLOSE': re.compile(r'rather than (?:left )?open|not left open|no longer open|settles what|'
                        r'which (?:is|was) open|left open[^.]{0,40}(?:is|was|has been) (?:now )?'
                        r'(?:settled|closed|measured|computed)|'
                        r'(?:settled|closed|measured|computed|answered)[^.]{0,30}left open', re.I),
    'ORD':   re.compile(r'\bremains\s+(?:between|the|a|an|that|this|constant|finite|valid|true'
                        r'|unchanged|positive|negative|bounded)\b|\bopen\s+(?:set|interval|ball'
                        r'|neighbourhood|neighborhood|cover|subset|map|condition)\b', re.I),
}
# the three mechanisms a site may carry.  PRESENCE IS REPORTED, NEVER TREATED AS A DISCHARGE.
MECH = {
    'ref-frontier': re.compile(r'\\(?:ref|autoref|nameref|pageref)\s*\{frontier:[^{}]*\}'),
    'cite-P7':      re.compile(r'\\cite\s*\{[^{}]*JanzenCRframework[^{}]*\}'),
    'rcpt':         re.compile(r'\\rcpt\s*\{[^{}]*\}'),
}
# ⛭ r7385+cc66 -- TWO CORRECTIONS TO THE RUN BEFORE ANY TEST TOUCHES IT, both measured:
#  ⒜ A SECTIONING COMMAND CARRIES NO TERMINAL PUNCTUATION, so the sentence split fuses it with
#     the prose that follows and a bare HEAD veto then loses that prose.  Measured on this
#     corpus: 4 PROSE open claims were invisible for exactly that reason, among them P3's
#     `\paragraph{Open.} One thing is open, and ...` -- the plainest instance of the claim the law
#     targets.  A heading's OWN words are still never a claim, so the heading is REMOVED rather
#     than used as a veto.
#  ⒝ AN IDENTIFIER IS NOT PROSE.  `\label{sec:open}`, `\ref{sec:open}` and a receipt key carry the
#     law's words as machine names.  r7391+cc66.50 found 13 of 69's 257 census rows reached ONLY
#     through such an identifier, 3 of them classed OPEN -- a false class in the other seat's
#     instrument, and this guard is that finding applied to this one before it can repeat it.
#     Stripping them also makes the KEY stable: a re-cited claim is not a reworded claim.
#  ⌗ Formatting that wraps PROSE (\emph, \textit, ...) is deliberately NOT stripped.
STRIP = re.compile(r'\\(?:sub)*section\*?{(?:[^{}]|\{[^{}]*\})*\}|'
                   r'\\(?:paragraph|title){(?:[^{}]|\{[^{}]*\})*\}|'
                   r'\\(?:label|ref|eqref|autoref|nameref|pageref|cite|citep|citet|rcpt'
                   r'|includegraphics|input|include)\s*{(?:[^{}]|\{[^{}]*\})*\}')
_SENT = re.compile(r'(?<=[.!?])\s+')
# the verdicts a person may write.  UNREAD is the only one this file ever writes.
VERDICTS = {'UNREAD', 'REFERENCED', 'FALSE-OPEN', 'NOT-AN-OPEN', 'OWED'}


def body(path):
    b = '\n'.join(l for l in open(path, encoding='utf-8', errors='replace').read().split('\n')
                  if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return b[:j] if j > 0 else b


def population():
    """The candidate sites, keyed (paper, normalised sentence).  P7 is the law's home and is out."""
    out = {}
    for num, stem in PAPERS:
        if num == 'P7':
            continue
        sec = ''
        for p in re.split(r'\n\s*\n', body(os.path.join(ROOT, 'corpus', stem + '.tex'))):
            m = re.findall(r'\\(?:sub)*section\*?\{([^}]*)\}', p)
            if m:
                sec = m[-1]
            flat = re.sub(r'\s+', ' ', p)
            for s in _SENT.split(flat):
                k = ' '.join(STRIP.sub(' ', ' '.join(s.split())).split())
                if not k or not LAW.search(k):
                    continue
                if EXCL['CLOSE'].search(k) or EXCL['ORD'].search(k):
                    continue
                hit = ','.join(n for n, r in MECH.items() if r.search(flat)) or 'none'
                out[(num, k)] = (sec or '(no section)', hit)
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
        rows[(f[0], f[4])] = (f[1], f[2], f[3])
    return rows


def write_baseline(pop, prior):
    with open(BASELINE, 'w', encoding='utf-8') as fh:
        fh.write('# THE OPEN-REFERENCE BASELINE -- the frozen backlog of the corpus\'s own standing '
                 'law.\n')
        fh.write('# ** THE KEY IS (paper, normalised marker SENTENCE) AND NOT A LINE NUMBER, '
                 'DELIBERATELY. **  A reworded\n')
        fh.write('#   open claim is a NEW claim and must be read again.  corpus/'
                 'check_open_references.py reds on a key\n')
        fh.write('#   that is not here and on nothing else: the backlog is frozen, it may not GROW.'
                 '\n')
        fh.write('# ** verdict is a PERSON\'S column. **  --regen writes UNREAD for a new key and '
                 'NEVER changes an existing\n')
        fh.write('#   verdict.  Permitted: ' + ' '.join(sorted(VERDICTS)) + '.\n')
        fh.write('# mechanism is REPORTED, not a discharge: ref-frontier / cite-P7 / rcpt / none.\n')
        fh.write('paper\tsection\tmechanism\tverdict\tsentence\n')
        for (num, k) in sorted(pop, key=lambda t: ([p for p, _ in PAPERS].index(t[0]), t[1])):
            sec, hit = pop[(num, k)]
            verdict = prior.get((num, k), (None, None, 'UNREAD'))[2] if prior else 'UNREAD'
            fh.write('\t'.join((num, sec, hit, verdict, k)) + '\n')


def main(argv):
    pop = population()
    prior = read_baseline()
    if '--regen' in argv or prior is None:
        write_baseline(pop, prior)
        print(f'  open-reference baseline written: {len(pop)} candidate site(s).')
        return 0

    bad = sorted(v[2] for v in prior.values() if v[2] not in VERDICTS)
    new = sorted(k for k in pop if k not in prior)
    gone = sorted(k for k in prior if k not in pop)
    unread = sum(1 for k in pop if prior.get(k, ('', '', 'UNREAD'))[2] == 'UNREAD')

    print()
    print('  OPEN-REFERENCE RATCHET -- the corpus\'s own law, enforced as a ratchet and not a verdict')
    print(f'    {len(pop)} candidate site(s) outside P7; {unread} still UNREAD; '
          f'{len(prior)} baseline row(s)')
    print('    ⌗ This gate RULES NOTHING.  The law\'s literal test -- a reference to an item in P7')
    print('      §frontiers -- discharges 0 of them, because the papers compile separately and a')
    print('      \\ref cannot cross a document boundary.  So it reds on ONE thing: a NEW site.')
    print()

    if gone:
        print(f'  ⌗ {len(gone)} baseline row(s) no longer in the corpus (reworded or removed); '
              f'reported, not a failure:')
        for num, k in gone[:8]:
            print(f'      {num}  {k[:150]}')
        if len(gone) > 8:
            print(f'      ... and {len(gone) - 8} more')
        print('    Run: python3 corpus/check_open_references.py --regen')
        print()

    if bad:
        print(f'  [FAIL] {len(bad)} baseline row(s) carry a verdict that is not one of '
              f'{" ".join(sorted(VERDICTS))}: {" ".join(sorted(set(bad)))}')
        return 1

    if new:
        print(f'  [FAIL] {len(new)} NEW open-language site(s) with no baseline row.')
        print('    THE LAW THIS ENFORCES, from P7 §frontiers\' own block:')
        print('      "every \'open / frontier / incomplete / remains / not yet / deferred\' claim')
        print('       elsewhere in the corpus must reference an item here or be struck as a')
        print('       false-open (the result worked elsewhere, the owed reference supplied)"')
        print('    ⌗ The gate does not say these are false-opens.  It says they are UNREAD and that')
        print('      the backlog grew.  Read each one, then add its row with a verdict.')
        for num, k in new[:12]:
            sec, hit = pop[(num, k)]
            print(f'      {num} §{sec}  [{hit}]')
            print(f'        {k[:200]}')
        if len(new) > 12:
            print(f'      ... and {len(new) - 12} more')
        return 1

    print('  no new open-language site: the backlog is frozen and did not grow.')
    print('  ⌗ FROZEN IS NOT DISCHARGED.  The UNREAD count above is the worklist, and it comes')
    print('    down only by a person reading a site and writing its verdict into the baseline.')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
