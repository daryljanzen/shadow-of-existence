#!/usr/bin/env python3
"""Recover S7's REVERSAL keys using S7's own functions, unmodified: its source is executed up to its first
section header, so the classifier, transforms, PIN and paper list are exactly the receipt's."""
import os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
S7 = os.path.join(ROOT, 'receipts/L_probability/S7_the_paper_pins_are_read_by_reversing_the_clause_they_quote_and_only_one_in_four_would_notice.py')


def load():
    src = open(S7, encoding='utf-8').read()
    cut = src.index('head("A. THE INSTRUMENT')
    src = src[:cut].replace('print(__doc__)', '')
    ns = {'__file__': S7, '__name__': 's7'}
    exec(compile(src, S7, 'exec'), ns)
    rows = ns['read_baseline'](ns['_at'](ns['PIN'], ns['BASELINE']))
    bodies = {p: ns['_at'](ns['PIN'], f'corpus/{p}.tex') for p in ns['PAPERS']}
    t, strict, neg, rev, multi = ns['classify'](rows, bodies)
    return ns, rows, bodies, t, rev, multi


if __name__ == '__main__':
    ns, rows, bodies, t, rev, multi = load()
    print(dict(t))
    print(len(rev), 'REVERSAL;', sum(1 for r, l, w, f in rev if (r, l) in multi), 'multi-site')
