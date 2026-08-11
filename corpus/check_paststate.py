#!/usr/bin/env python3
"""check_paststate.py -- the RG-1 gate, in check_citations' REPORT mould.

RG-1 (THE_STAGED_REVISIONS.md): a finished paper does not report the things it did not have figured
out at some stale point in the past and has since worked through.  The content is folded into the
positive synthesis; the stale state is struck and moved to CONSOLIDATE §16, which exists to hold how
the programme developed.  A KEEP is allowed -- when an account of HOW a problem was worked is
particularly pedagogical -- but it must answer the gate in one sentence, in the paper.

⚠ THIS GATE REPORTS AND DOES NOT FAIL ON CONTENT, and the reason is the reason check_citations gives:
the gate's question is a JUDGEMENT ("does this ADD, in a way that COMPLEMENTS consolidate's framing?")
and a gate that returned verdicts on judgement would be worse than none.  It exits non-zero only if it
cannot read the papers.

⚠ AND THE PATTERN SET IS NARROW BY CONSTRUCTION, because the wide one already failed once.  The r2377
census reported 17 sites; read at source there were five.  It matched "this section reads the skeleton
off" and "this section reads the crossings" -- ordinary present tense -- and a % comment no reader
sees.  That is the blind-checker class: a verification that supplies its own vocabulary is testing the
vocabulary.  So: past-tense forms only, LaTeX comments stripped, and every hit printed WITH ITS
CONTEXT so the reader adjudicates rather than the count.

Written r2378.  Stated for reversal.
"""
import os, re, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))
PATTERNS = [
    (r'stood as item',                    'frontier-history wrapper'),
    (r'\((?:C|c)orrected r\d+',           'inline revision record'),
    (r'\bStruck r\d+\b',                  'inline strike record'),
    (r'ANSWERED; struck',                 'struck item still listed'),
    (r'kept (?:here )?as the record',      'retention-of-past-state marker'),
    (r'logged rather than deleted',       'retention-of-past-state marker'),
    (r'this (?:list|bracket|section) (?:read|used to read)', 'past-wording quotation'),
    (r'was previously characterised',     'past-state characterisation'),
    (r'until it resolved',                'frontier-history wrapper'),
]
GATE = re.compile(r'RG-1|complements? .{0,40}development record|pedagogical', re.I)


def strip_comments(t):
    return '\n'.join(l for l in t.split('\n') if not l.lstrip().startswith('%'))


def main():
    os.chdir(HERE)
    files = sorted(f for f in glob.glob('*.tex') if not f.startswith('appendix_'))
    if not files:
        print('  [FAIL] no papers found'); return 1
    print('  RG-1 -- past state carried in the final presentation')
    print('  (reports; never fails on content -- the gate question is a judgement)')
    print()
    total = 0
    for f in files:
        raw = open(f, encoding='utf-8', errors='replace').read()
        t = strip_comments(raw)
        rows = []
        for rx, kind in PATTERNS:
            for m in re.finditer(rx, t):
                ctx = re.sub(r'\s+', ' ', t[max(0, m.start() - 110):m.start() + 130])
                gated = bool(GATE.search(t[max(0, m.start() - 600):m.start() + 600]))
                rows.append((kind, ctx, gated))
        if rows:
            total += len(rows)
            print(f'  {f}  ({len(rows)})')
            for kind, ctx, gated in rows:
                print(f'    [{"KEEP-answered" if gated else "unanswered"}] {kind}')
                print(f'      …{ctx}…')
            print()
    if total == 0:
        print('  No past-state markers in any paper.')
    else:
        print(f'  {total} site(s) reported.  Each is READ and dispositioned FOLD / MOVE / KEEP;')
        print( '  a KEEP carries its one-sentence gate answer in the paper, which is what turns')
        print( '  an "unanswered" line above into a "KEEP-answered" one.')
        print()
        print( '  ⚠ A hit is not a defect.  Present-tense "this section reads X" is ordinary prose;')
        print( '     the r2377 census believed its own matches and reported 17 sites where 5 existed.')
    print()
    print('=' * 78)
    print('  This gate REPORTS.  It exits zero on content, and non-zero only if it cannot read')
    print('  the papers -- because RG-1 asks whether a passage ADDS in a way that COMPLEMENTS')
    print('  the development record, and no regex adjudicates that.')
    print('=' * 78)
    return 0


if __name__ == '__main__':
    sys.exit(main())
