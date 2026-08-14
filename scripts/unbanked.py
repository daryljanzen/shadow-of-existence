#!/usr/bin/env python3
"""unbanked.py -- WHICH RESULTS LIVE IN RECEIPTS AND HAVE NEVER REACHED PRINT?

** WHY.  The class has now paid three times. **
  * ** `L-535` ** -- 54's routed warning, an instance rather than a class, found by running a control.
  * ** A7 (r2570) ** -- "the quartic is a constant vacuum energy, its counterterm is the one constant":
    *** lived in ledgers and receipts for a HUNDRED REVISIONS at ZERO USES in all seventeen papers ***,
    banked at c54.210.
  * ** `excentre` (r2678) ** -- a SIXTH equivalence for the hinge distance $2\\alpha$, "the first phrased
    in the substrate's own causal language", plus ** 0 of 36 null connections ** among excentres and
    hinges.  *** Five receipts, all passing.  ZERO uses across the papers. ***

  ⇒ ** 54's method, made an instrument: ** *** count a term's uses in the RECEIPTS against its uses in
      the PAPERS.  A term the working layer relies on and the printed layer never says is a result that
      did not land. ***

** WHAT THIS PRINTS. **  Technical terms (7+ letters) used at least `MIN` times across `receipts/` and
** zero times in any paper body **, with the receipts that carry them.

  ⚠ ** It cannot distinguish a RESULT from a TOOL. **  *** `simplify`, `linspace` and `abspath` top the
      raw list; a human must read the candidates.  The gate is the SURFACING, not the verdict -- which is
      why this is a script and not a `check_`. ***
  ⌗ ** And a term absent from print is not always a defect: ** a receipt may legitimately use a working
    name the papers phrase differently.  *** `station` reads as a candidate and is banked 24 times. ***

    python3 scripts/unbanked.py            # default MIN = 8
    python3 scripts/unbanked.py 4

Written r2678.  Stated for reversal.
"""
import collections
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

# ** python and LaTeX machinery -- named so the list is short enough to READ. **
NOISE = set("""simplify abspath dirname startswith nsimplify allclose findall linspace itertools
argrelextrema asarray lambdify radians trapezoid basename thebibliography endswith isinstance
returncode subprocess default symbolic assertions append encoding errors replace verdict
receipt receipts corpus python printed observer written revision stated reversal because
between another however therefore article without against nothing appears carries""".split())


def body(f):
    b = '\n'.join(l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
                  if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return b[:j] if j > 0 else b


def main():
    mn = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    print()
    print(f'  unbanked -- terms used >={mn}x in receipts and 0x in any paper')
    print()
    papers = ' '.join(body(f) for f in glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))
                      if not os.path.basename(f).startswith('appendix_receipts'))
    # ** match on the STEM, not the exact word: `station` is banked 24 times as `stations`,
    # and an exact-word set put it top of the candidate list -- a false positive at position 1
    # is what teaches a reader to ignore the tool. **
    pw = set()
    for w in re.findall(r'[A-Za-z][a-z]{4,}', papers):
        w = w.lower()
        pw.add(w)
        for suf in ('s', 'es', 'ed', 'ing'):
            if w.endswith(suf) and len(w) - len(suf) >= 4:
                pw.add(w[:-len(suf)])

    rfiles = glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True)
    texts = {f: open(f, encoding='utf-8', errors='replace').read() for f in rfiles}
    rc = collections.Counter(w.lower() for t in texts.values()
                             for w in re.findall(r'[A-Za-z][a-z]{6,}', t))

    cand = [(w, n) for w, n in rc.most_common()
            if w not in pw and w + 's' not in pw and w.rstrip('s') not in pw
            and w not in NOISE and n >= mn]
    print(f'  {len(cand)} candidate(s) -- READ them; the script surfaces, it does not verdict\n')
    for w, n in cand[:20]:
        carriers = [os.path.basename(f) for f, t in texts.items() if w in t.lower()][:3]
        print(f'    {n:>4}  {w:<20} {", ".join(c[:28] for c in carriers)}')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
