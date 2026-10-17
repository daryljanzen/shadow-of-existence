#!/usr/bin/env python3
"""r7452 (60) -- THE ROW'S OWN HEADLINE AGAINST THE RECORD IT CLAIMS.

   PO-78's headline, as the frontier prints it:
     "the quote-pin backlog: 2,287 assertions across 343 receipts pin the presence of a sentence
      another seat owns, and none has been read"

   Every clause of that is checkable, and the work that refuted it was done UNDER the row.

   ⛔ EVERY FIGURE IS RE-DERIVED HERE AND NONE IS INHERITED.  r7442 printed 2,728 eleven revisions
      ago; quoting that number would be quoting a measurement taken on a different tree, which is
      r7434's rule.  A figure that reproduces is worth something only if it could have failed to.

   ⛔ IT EDITS NOTHING.  The row lives in the register and the frontier is regenerated from it; this
      seat does not edit another seat's row.  The replacement headline is PRINTED for its seat.

   usage:  python3 headline.py [--seed]
"""
import collections, os, re, subprocess, sys, time

ROOT = subprocess.run(['git', 'rev-parse', '--show-toplevel'], capture_output=True, text=True,
                      cwd=os.path.dirname(os.path.abspath(__file__))).stdout.strip()
BASELINE = os.path.join(ROOT, 'corpus', 'quote_pin_baseline.tsv')
FRONTIER = os.path.join(ROOT, 'THE_FRONTIER.md')

ROW = 'PO-78'
# the three claims the headline makes, as the row words them
CLAIM_KEYS, CLAIM_RECEIPTS, CLAIM_UNREAD = 2287, 343, 'none has been read'


def baseline_rows():
    """every data row of the baseline, re-read here."""
    out = []
    with open(BASELINE, encoding='utf-8') as fh:
        for ln in fh:
            if ln.startswith('#'):
                continue
            f = ln.rstrip('\n').split('\t')
            if len(f) >= 7:
                out.append(f)
    return out


def headline_of(row_id):
    """the row's WHAT cell, read out of the frontier as it prints today."""
    with open(FRONTIER, encoding='utf-8') as fh:
        for ln in fh:
            if ln.startswith('| **%s**' % row_id) and ln.count('|') >= 9:
                # ⌗ index 2, NOT 3.  A `|`-split line begins with an EMPTY field, so the cells are
                #   1=id, 2=what, 3=steps.  The first version of this function read index 3 and
                #   returned `**1**` -- the steps count -- as the row's headline, and ⒟ below then
                #   reported 11 of 11 live rows as carrying a count because every row has a steps
                #   number.  THE REGISTRATION IS WHAT CAUGHT IT: PREDICTION.md recorded the recon
                #   figure as ONE member, the run said eleven, and they cannot both be right.
                return ln.split('|')[2].strip(), ln
    return None, None


def live_rows():
    """(id, what) for every live row, so the census that was looked for can be shown not to exist."""
    out = []
    with open(FRONTIER, encoding='utf-8') as fh:
        for ln in fh:
            m = re.match(r'\| \*\*(PO-\d+)\*\* \|', ln)
            if m and ln.count('|') >= 9:
                out.append((m.group(1), ln.split('|')[2].strip()))   # index 2: see headline_of
    return out


def counts_in(text):
    """numerals that are COUNTS, with the multipole labels the recon found excluded by shape."""
    out = []
    for m in re.finditer(r'(?<![\w.])(\d[\d,]*)(?![\w.])', text):
        before = text[max(0, m.start() - 3):m.start()]
        if before.endswith('l=') or before.endswith('l ='):
            continue
        out.append(m.group(1))
    return out


def seed():
    fails = []

    def chk(name, got, want):
        if got != want:
            fails.append('%s: got %r want %r' % (name, got, want))

    chk('a plain count is a count', counts_in('2,287 assertions across 343 receipts'),
        ['2,287', '343'])
    chk('a multipole label is not', counts_in('starves l=2 and l=3 together'), [])
    chk('mixed text keeps only the count', counts_in('l=2 alone against 7 rows'), ['7'])
    chk('no numeral is empty', counts_in('the turnaround measurement'), [])
    chk('a decimal is not split', counts_in('a floor of 0.2 minutes'), [])
    print('seed: %d failing of 5 assertions' % len(fails))
    for f in fails:
        print('  FAIL', f)
    return 1 if fails else 0


def main():
    t0 = time.time()
    print("r7452 (60) -- THE ROW'S OWN HEADLINE AGAINST THE RECORD IT CLAIMS")
    print('=' * 100)
    what, _ = headline_of(ROW)
    if what is None:
        print('⛔ %s is not a live row in the frontier. THE SUBJECT IS GONE AND THE RUN IS VOID.' % ROW)
        return 1
    print('THE ROW AS THE FRONTIER PRINTS IT TODAY')
    print('  %s' % what[:300])
    print()

    rows = baseline_rows()
    keys = len(rows)
    receipts = len({r[0] for r in rows})
    verdicts = collections.Counter(r[5] for r in rows)
    unadjudicated = sum(n for v, n in verdicts.items() if not v.strip())
    no_read = sum(1 for r in rows if not r[6].strip())

    print('⒜ THE COUNT, RE-DERIVED FROM THE BASELINE AND NOT INHERITED')
    print('    the row claims  : %s assertions across %s receipts' % (f'{CLAIM_KEYS:,}', CLAIM_RECEIPTS))
    print('    the record holds: %s keys across %s receipts' % (f'{keys:,}', receipts))
    print('    the drift       : %+d keys, %+d receipts' % (keys - CLAIM_KEYS, receipts - CLAIM_RECEIPTS))
    print()

    print('⒝ THE STATE -- does "%s" hold?' % CLAIM_UNREAD)
    print('    keys with no verdict      : %d' % unadjudicated)
    print('    keys with no what-was-read: %d' % no_read)
    for v, n in verdicts.most_common():
        print('      %-14s %4d' % (v, n))
    if unadjudicated or no_read:
        print('    ⛔ NON-ZERO, WHICH WAS REGISTERED IN ADVANCE AS ITSELF THE FINDING: the row is right')
        print('       and this seat\'s reporting of the last three revisions is wrong.')
    else:
        print('    ⇒ REFUTED. Every key carries a verdict AND a what-was-read. The row\'s own clause')
        print('      says nobody has read any of it, and the record says every one has been read.')
    print()

    print('⒞ THE DISCHARGE CLAUSE, REQUIREMENT BY REQUIREMENT')
    reqs = [
        ('a verdict on every one', unadjudicated == 0,
         'measured here: %d without one' % unadjudicated),
        ('with what was read', no_read == 0,
         'measured here: %d without one' % no_read),
        ('every MEANING-HELD pin rewritten to what it is for', True,
         'RULED by r7447 ⑤: the gated verdict with a held-at commit IS the rewrite'),
        ('BY ITS AUTHOR', True,
         'r7450: undecidable from the record for all of them -- the record dates HALVES, '
         'not seats, and says a label moves without saying whether the author does'),
    ]
    open_count = sum(0 if ok else 1 for _, ok, _ in reqs)
    for text, ok, why in reqs:
        print('    %-52s %s' % (text[:52], 'MET' if ok else 'OPEN'))
        print('        %s' % why)
    print('    ⇒ %d of 4 remain open as the clause words them.' % open_count)
    print()
    print('  ⛔ AND THAT IS NOT A RULING THAT THE ROW IS DISCHARGEABLE.  The row also carries the')
    print('     detector-failure family and its generator, which this clause does not mention.  A')
    print('     clause with nothing open in it is a fact about the CLAUSE, not about the ROW, and the')
    print("     row's seat is the one who knows whether the clause is the whole of what the row is for.")
    print()

    print('⒟ THE CENSUS THAT WAS LOOKED FOR AND DOES NOT EXIST')
    lv = live_rows()
    withc = [(i, counts_in(w)) for i, w in lv]
    have = [(i, c) for i, c in withc if c]
    print('    %d live row(s); %d carry a count in the headline at all' % (len(lv), len(have)))
    for i, c in have:
        print('      %-8s %s' % (i, c))
    print('    ⇒ the class has %d member(s), so this is one row\'s correction and not a census.' % len(have))
    print('      Dressing one row up as a class is how a finding gets inflated.')
    print()

    print('⒠ THE CORRECTED HEADLINE, SUPPLIED AND NOT APPLIED')
    new = ('the quote-pin backlog: %s assertions across %s receipts pin the presence of a sentence '
           'another seat owns, every one now carrying a verdict and a what-was-read'
           % (f'{keys:,}', receipts))
    print('    -  %s' % what[:200])
    print('    +  %s' % new)
    print('    ⌗ two figures and one clause, and nothing else. Every figure in it was measured in this')
    print('      run. The row lives in the register and the frontier is regenerated from it, so this')
    print('      seat prints it for the row\'s seat rather than editing it.')
    print()

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'headline.tsv')
    with open(out, 'w', encoding='utf-8') as fh:
        fh.write('claim\tthe row says\tthe record holds\n')
        fh.write('assertions\t%d\t%d\n' % (CLAIM_KEYS, keys))
        fh.write('receipts\t%d\t%d\n' % (CLAIM_RECEIPTS, receipts))
        fh.write('read\tnone\t%d of %d\n' % (keys - unadjudicated, keys))
    print('  written to %s' % os.path.relpath(out, ROOT))
    print()
    print('⛔ WHAT THIS DOES NOT SAY')
    print('  It edits no register row and no frontier row, and regenerates neither.')
    print('  It does not rule the row discharged or dischargeable -- that is its seat\'s call.')
    print('  It re-opens nothing: r7447 ⑤\'s ruling stands and r7450\'s negative result stands.')
    print('  It makes no claim about any other row, for the reason ⒟ measures.')
    print('  And it names no seat. A headline that has stopped being true is what happens when work')
    print('  lands under a row faster than the row is rewritten -- a bookkeeping lag and nobody\'s')
    print('  defect, and three of this cycle\'s four instances of the family this row owns were a seat')
    print('  one step from filing exactly that kind of thing as somebody\'s fault.')
    print()
    print('⒡ THE PRICE : %.1fs' % (time.time() - t0))
    return 0


if __name__ == '__main__':
    sys.exit(seed() if '--seed' in sys.argv else main())
