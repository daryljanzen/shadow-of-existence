#!/usr/bin/env python3
"""check_paper_pins_not_comment_only.py -- IS EVERY PAPER PIN SATISFIED BY TEXT THE PAPER RENDERS?

** r7277+70.1, on 66's r7277 ①. **  A `PAPER` quote pin reads a paper's SOURCE, and the source carries LaTeX
comments the paper never prints.  A pin whose literal matches only inside a comment is green on text the paper does
not say -- `69`'s find, `C1_conformal_vs_isometric` in `P5`'s line-7 comment.  Measured at r7275+70.2: 79 live
`PAPER` keys match a comment, and 2 match ONLY a comment.

** WHY A GATE AND NOT A SWEEP (66's ruling). **  The structural repair -- every `PAPER` pin reading the paper with
comments stripped -- is an edit to every receipt's reading helper across every prefix, which the ownership rule
forbids.  This gate instead holds the exposure where it is: a pin goes red the moment it becomes comment-only, which
for the 79 is exactly the moment a body sentence goes and the pin becomes false.

** THE CONDITION. **  Over every non-appendix `corpus/*.tex`, a comment is an unescaped `%` to end of line; a live
`PAPER` key (from `quote_pin_baseline.tsv`, which `check_quote_pins` holds equal to the instrument) FAILS when its
literal matches a comment and no body.  A literal with a backslash is matched as a regex when it compiles, as the
receipts match it.  A literal found nowhere is not this gate's -- `check_quote_pins` already counts a dead pin.
`MULTI` needs no case: a pin with several body sites is comment-only only if all of them are comments.

** KNOWN SITES (`KNOWN`), routed and allowed while they stand. **  A known site that stops being comment-only is
STALE and fails, so the list can only shrink.

    python3 corpus/check_paper_pins_not_comment_only.py
"""
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CMT = re.compile(r'(?<!\\)%.*$', re.M)

#: the r7275+70.2 two-site list, routed to their owners in FOR_66_FROM_70.md; both UNADJUDICATED when found
KNOWN = {
    ('receipts/L207_the_bend/W1_what_remains_between_the_wall_and_a_curve_dynamics.py',
     'until r2376+c54.179'): 'only in a comment of slicing_operator.tex -- routed r7275+70.2',
    ('receipts/L263_the_station_audit/S1_three_of_eight_stations_are_already_held_and_one_was_noticed_and_not_'
     'propagated.py', 'THE RECEIPT WAS MORE HONEST THAN THE PAPER'):
        'only in a comment of matter_sector_paper.tex -- routed r7275+70.2',
}


def _flat(t):
    return re.sub(r'\s+', ' ', t)


def split(text):
    """(body with comments removed, the comments' text), both whitespace-flattened"""
    return _flat(CMT.sub('', text)), _flat(' '.join(m.group(0)[1:] for m in CMT.finditer(text)))


def hit(lit, text):
    if lit in text:
        return True
    if '\\' in lit:
        try:
            return re.search(lit, text) is not None
        except re.error:
            return False
    return False


def comment_only(keys, papers):
    """[(receipt, literal)] whose literal matches a comment of some paper and the body of none"""
    halves = [split(t) for t in papers]
    return [k for k in keys
            if not any(hit(k[1], b) for b, _ in halves) and any(hit(k[1], c) for _, c in halves)]


def _seeds():
    paper = 'The wall is real.\n% a note: receipted there\nAnd 50\\% of it holds.\n'
    cases = [('a body-and-comment pin', ('r', 'The wall is real'), False),
             ('a comment-only pin', ('r', 'receipted there'), True),
             ('a pin found nowhere', ('r', 'never written'), False),
             ('text after an escaped percent is body', ('r', 'of it holds'), False)]
    bad = []
    for label, key, want in cases:
        got = bool(comment_only([key], [paper]))
        if got != want:
            bad.append(f'{label}: expected {"red" if want else "green"}, got {"red" if got else "green"}')
    return bad


def main():
    print()
    print('  PAPER PINS NOT COMMENT-ONLY -- is every PAPER pin satisfied by text the paper renders?')
    print()
    bad = _seeds()
    if bad:
        print('  ⛔ the seeds lost a direction:')
        for b in bad:
            print(f'      {b}')
        return 1
    print('    seeds hold: a body-and-comment pin passes, a comment-only pin fails, a pin found nowhere is not this '
          'gate\'s, an escaped % is body')
    keys = []
    for ln in open(os.path.join(HERE, 'quote_pin_baseline.tsv'), encoding='utf-8'):
        q = ln.rstrip('\n').split('\t')
        if len(q) >= 6 and not ln.startswith('#') and q[2] == 'PAPER':
            keys.append((q[0], json.loads(q[1])))
    papers = [open(p, encoding='utf-8', errors='replace').read()
              for p in sorted(glob.glob(os.path.join(HERE, '*.tex')))
              if not os.path.basename(p).startswith('appendix')]
    found = comment_only(keys, papers)
    new = [k for k in found if k not in KNOWN]
    stale = [k for k in KNOWN if k not in found]
    print(f'    {len(keys)} live PAPER key(s); {len(found)} comment-only, {len(KNOWN)} of them named as known')
    rc = 0
    if new:
        rc = 1
        print()
        for rc_, lit in new:
            print(f'    [COMMENT-ONLY] {rc_}  {json.dumps(lit, ensure_ascii=False)[:70]}')
        print()
        print('  ⛔ A PAPER PIN SATISFIED ONLY BY A COMMENT IS GREEN ON TEXT THE PAPER DOES NOT PRINT.')
        print('     Its sentence left the body: read whether the claim still stands, and re-pin it on the body or retire it.')
    if stale:
        rc = 1
        print()
        for rc_, lit in stale:
            print(f'    [STALE KNOWN] {rc_}  {json.dumps(lit, ensure_ascii=False)[:70]} -- no longer comment-only; remove it '
                  'from KNOWN')
    if rc == 0:
        print('  no PAPER pin is satisfied only by a comment, beyond the named sites.')
    return rc


if __name__ == '__main__':
    sys.exit(main())
