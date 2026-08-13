#!/usr/bin/env python3
"""check_provenance.py -- A PHRASE QUOTED FROM A PAPER MUST BE IN THAT PAPER'S BODY, NOT ITS COMMENTS.

** WHY.  c54.207 found it and caught it one hop before print. **  A `%` header comment in P16 carried
"peak spacing"; a receipt's docstring quoted the surrounding sentence ** in quotation marks ** as "P16
distinguishes it explicitly"; and the paragraph 54 was drafting was about to cite it in a paper.

      *** header comment -> a receipt's docstring, where it reads as a quotation -> a paper. ***

  ** Measured: `peak spacing` is 0 in P16's body, 1 in P16's comments, 6 in P15's body. **  ⇒ ** The
  claim was true of P15 and attributed to P16, and the misattribution's SOURCE was a comment nobody
  treats as text. **

** ⌗ AND NOTHING IN THE TREE MEASURED THE FIRST STEP, WHICH IS THE POINT. **  Every provenance check in
this corpus asserts against a paper's ** rendered content **: `check_loci`, `check_receipt_asserts`,
`check_citations`.  *** A comment is not rendered, so it is invisible to all of them -- and a quotation
lifted from one carries the authority of the paper it sits in while being no part of it. ***

** WHAT THIS CHECKS. **  Every quoted string of 45+ characters in every receipt.  If the string is
** absent from every paper's BODY ** but ** present in some paper's COMMENTS **, it fails.
  ⇒ ** Current population: ZERO. **  54 fixed the one instance, and a scan of all 400-odd receipts finds
    no other.  *** Which is exactly when a gate is cheap: it costs nothing today and forbids the path
    that was walked once. ***

** ⚠ WHAT IT DELIBERATELY DOES NOT DO. **
  * ** It does not check that a quotation is ACCURATE ** -- only that its source is a body rather than a
    comment.  Accuracy against the body is `check_receipt_asserts`' job.
  * ** It does not forbid receipts from discussing comments ** -- only from QUOTING them in a form that
    reads as paper text.  The 45-character floor is what separates a quotation from a phrase.
  * *** It cannot catch the reverse hop *** -- a claim invented in a receipt docstring and later quoted
    as though it came from a paper.  ** That is the same class and this gate does not reach it **, which
    is stated here rather than discovered later.

    python3 corpus/check_provenance.py

Written r2572.  Stated for reversal.
"""
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
FLOOR = 45


def split_papers():
    bodies, comments = {}, {}
    for f in glob.glob(os.path.join(ROOT, 'corpus', '*.tex')):
        if os.path.basename(f).startswith('appendix_receipts'):
            continue
        tag = os.path.basename(f).replace('.tex', '')
        raw = open(f, encoding='utf-8', errors='replace').read().split('\n')
        bodies[tag] = re.sub(r'\s+', ' ', '\n'.join(
            l for l in raw if not l.lstrip().startswith('%')))
        comments[tag] = re.sub(r'\s+', ' ', '\n'.join(
            l for l in raw if l.lstrip().startswith('%')))
    return bodies, comments


def main():
    print()
    print('  check_provenance -- is every quoted phrase from a paper BODY, not a comment?')
    print()
    bodies, comments = split_papers()
    allbody = ' '.join(bodies.values())
    receipts = glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True)

    bad, checked = [], 0
    for f in receipts:
        s = open(f, encoding='utf-8', errors='replace').read()
        for m in re.finditer(rf'"([A-Za-z][^"\n]{{{FLOOR},180}})"', s):
            q = re.sub(r'\s+', ' ', m.group(1)).strip()
            checked += 1
            if q in allbody:
                continue
            for tag, c in comments.items():
                if q in c:
                    bad.append((os.path.relpath(f, ROOT), tag, q[:80]))
                    break

    print(f'  {len(receipts)} receipt(s); {checked} quoted string(s) of {FLOOR}+ chars checked.')
    print()
    if bad:
        for f, tag, q in bad:
            print(f'    [FAIL] {f}')
            print(f'           quotes "{q}"')
            print(f'           which is in {tag}.tex\'s COMMENTS and in no paper\'s body.')
        print()
        print('    ⛔ A COMMENT IS NOT RENDERED, so every other provenance check in this corpus is')
        print('       blind to it -- and a quotation lifted from one carries the authority of the paper')
        print('       it sits in while being no part of it.  ** c54.207 caught this one hop before')
        print('       print: header comment -> receipt docstring -> paper. **')
        return 1

    print('  no receipt quotes a phrase that lives only in a paper comment.')
    print()
    print('  ⌗ ** Population is ZERO and has been since c54.207 fixed the one instance. **  That is when')
    print('    a gate is cheap: ** it costs nothing today and forbids the path that was walked once. **')
    print('  ⚠ ** And it cannot catch the reverse hop ** -- a claim invented in a docstring and later')
    print('    quoted as though it came from a paper.  ** Same class, out of reach, stated here. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
