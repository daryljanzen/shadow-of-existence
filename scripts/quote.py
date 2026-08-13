#!/usr/bin/env python3
"""quote.py -- find a phrase in the corpus AS IT IS ACTUALLY WRITTEN, markup and all.

** WHY.  ** Four receipts this session failed their first run on the same trap: a phrase read in a
stripped view and asserted against the source, where the source has `\\emph{}`, braced superscripts, or
`\\mathrm{}` inside it.  ** r2623 twice, r2627, r2632, r2633. **

  ⇒ *** The reading view and the assertion target are different strings, and the gap is invisible until
      the check fails.  This closes it: give the phrase as you read it, get back the exact substring to
      assert. ***

    python3 scripts/quote.py "the three carry one mass parameter"
    python3 scripts/quote.py "Weyl S_3 is the relation"

Written r2633.  Stated for reversal.
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))


def strip(s):
    """The view a reader sees: markup gone, whitespace flat."""
    s = re.sub(r'\\emph\{([^}]*)\}', r'\1', s)
    s = re.sub(r'\\(?:mathrm|mathbf|text|textbf)\{([^}]*)\}', r'\1', s)
    s = re.sub(r'[{}$]', '', s)
    return re.sub(r'\s+', ' ', s)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    want = re.sub(r'\s+', ' ', ' '.join(sys.argv[1:])).strip()
    hits = 0
    for f in sorted(glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))):
        raw = '\n'.join(l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
                        if not l.lstrip().startswith('%'))
        flat = re.sub(r'\s+', ' ', raw)
        # walk windows of the raw text, comparing their STRIPPED form to the wanted phrase
        n = len(want)
        for i in range(len(flat)):
            for w in (n, n + 20, n + 60, n + 120):
                seg = flat[i:i + w]
                if strip(seg).startswith(want):
                    print(f'  {os.path.basename(f)}')
                    print(f'    as read:    {want}')
                    print(f'    as written: {seg[:len(seg)]}')
                    print()
                    hits += 1
                    break
            if hits:
                break
        if hits:
            break
    if not hits:
        print('  not found -- try a shorter phrase, or check it is not inside a % comment.')
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
