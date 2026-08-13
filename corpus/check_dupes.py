#!/usr/bin/env python3
"""check_dupes.py -- A REWRITE MUST REPLACE, NOT ACCOMPANY.

** WHY.  r2648: ** at r2588 this line de-narrated `sec:diffusion-scale` by writing a clean paragraph -- and
** left the original standing beneath it. **  The result sat in the paper for sixty revisions:

    The acoustic scale is met at the directly measured H_0; the diffusion scale is not free to follow it.
    Holding \\ell_* to its measured value fixes the onset redshift, and theta_D/theta_* then follows
    with nothing left to adjust.

    ** The diffusion scale is not. **  Holding \\ell_{*} to its measured value fixes the onset redshift, and
    theta_D/theta_* then follows with nothing left to adjust: it varies from +43% to -3% ...

  ⇒ *** An orphan sentence fragment, and the sentence after it repeating what the paragraph above already
      said.  `check_compile` passed; `check_revleak` passed; nothing looks at whether a paper says the
      same thing twice. ***

** WHAT THIS CHECKS. **  Near-duplicate sentences within one paper -- the signature of a rewrite that
accompanied rather than replaced.  ** Compares normalised sentences of 40+ characters and reports pairs
above a similarity threshold. **

  ⚠ ** Legitimate repetition exists: ** a paper may restate a claim in its abstract and its body, and a
  definition may be recalled where it is used.  *** So the gate reports a BASELINE count and fails when
  that count RISES -- the same design as `check_withdrawals`: it cannot judge whether a repetition is
  wanted, so it guarantees a new one is seen. ***

    python3 corpus/check_dupes.py
    python3 corpus/check_dupes.py --rebuild

✔ ** SEED TEST PASSES as of r2649 -- clean 0, seeded 1, restored 0. **  ⛭ ** And the cause of the four
earlier failures was worth having: ** the LaTeX preamble contains no sentence-ending punctuation, so the
first real sentence of every paper glued onto it and could never match its own duplicate.  *** The gate
was blind to the opening of all seventeen papers.  Cutting at `\begin{document}` before splitting fixed
it and raised the baseline 12 -> 13 -- one real pair had been hiding in the swallowed region. ***
  ⌗ ** The gate still cannot judge whether a repetition is WANTED ** -- a paper may restate a claim in its
  abstract and its body.  *** So it baselines and fails on a RISE, as `check_withdrawals` does. ***

Written r2648.  Stated for reversal.
"""
import glob
import os
import re
import sys
from difflib import SequenceMatcher

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
BASELINE = os.path.join(HERE, 'dupes_baseline.txt')


def body(f):
    b = '\n'.join(l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
                  if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return b[:j] if j > 0 else b


def norm(s):
    s = re.sub(r'\\[a-zA-Z]+\*?(\{[^}]*\})?', ' ', s)
    s = re.sub(r'[^a-z0-9 ]', ' ', s.lower())
    return re.sub(r'\s+', ' ', s).strip()


def scan():
    hits = []
    for f in sorted(glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))):
        if os.path.basename(f).startswith('appendix_receipts'):
            continue
        # ** the preamble has no sentence-ending punctuation, so the first body sentence glues onto
        # it and never matches its own duplicate.  ⇒ *** Cut at \begin{document} before splitting:
        # what precedes it is package loading, not prose, and it was silently swallowing the first
        # real sentence of every paper. *** **
        raw = body(f)
        d = raw.find('\\begin{document}')
        t = re.sub(r'\s+', ' ', raw[d:] if d > 0 else raw)
        sents = [norm(s) for s in re.split('(?<=[.!?])' + chr(92) + 's+', t)]
        sents = [s for s in sents if len(s) >= 40]
        # ** bucket by the first six words: a near-duplicate shares its opening, and comparing every
        # sentence against every other is O(n^2) over ~2000 sentences per paper -- too slow to run
        # every turn, and a gate nobody runs is not a gate. **
        from collections import defaultdict
        buckets = defaultdict(list)
        for s in sents:
            buckets[' '.join(s.split()[:6])].append(s)
        for key, group in buckets.items():
            for i, a in enumerate(group):
                for b in group[i+1:]:
                    if SequenceMatcher(None, a, b).ratio() > 0.88:
                        hits.append((os.path.basename(f), a[:70]))
                        break
    return hits


def main():
    print()
    print('  check_dupes -- does a paper say the same thing twice?')
    print()
    hits = scan()
    print(f'  {len(hits)} near-duplicate sentence pair(s) across the papers')
    for f, s in hits[:8]:
        print(f'    {f[:24]:<24} …{s}…')
    print()

    if '--rebuild' in sys.argv or not os.path.exists(BASELINE):
        open(BASELINE, 'w', encoding='utf-8').write(
            '# ** near-duplicate sentence pairs, as last AUDITED. **  A rewrite must REPLACE, not\n'
            '# accompany.  ⇒ *** When this rises, a paragraph was written beside the one it was meant\n'
            '#     to replace -- which compiles, passes every other gate, and reads as a stutter. ***\n'
            f'{len(hits)}\n')
        print(f'  baseline set: {len(hits)}')
        return 0

    was = int([l for l in open(BASELINE, encoding='utf-8')
               if l.strip() and not l.startswith('#')][0])
    if len(hits) > was:
        print(f'    [FAIL] the papers held {was} near-duplicate pair(s) when last audited, and now hold '
              f'{len(hits)}.')
        print()
        print('    ⛔ ** A REWRITE ACCOMPANIED RATHER THAN REPLACED. **  *** Find the new pair and delete')
        print('       the paragraph that was meant to go. ***')
        return 1
    print(f'  count at {len(hits)}, baseline {was} -- not risen.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
