#!/usr/bin/env python3
"""latent.py -- WHEN IS IT SAFE TO SPLIT THE WORK?

** WHY.  r2620, Daryl: ** "one thing I definitely want to wait for is for these 'this thing already has
the thing just sitting there' turns.  I think I'm going to want us to work those turns one by one here.
That will keep things coherent.  Can't split while turns like this last one are still happening."

  ⇒ *** Right, and the reason is structural: a LATENT finding is one where the answer is already in the
      corpus and reading further finds it.  Two nodes working in parallel would both find the same
      latent thing, or one would BUILD what the other found sitting there. ***
  ⇒ ** Parallel work is safe on CONSTRUCTION and unsafe on DISCOVERY-BY-READING. **

** WHAT THIS MEASURES. **  The rate at which turns produce a latent finding.  *** While the rate is high,
the corpus is still telling us things and the turns must run one at a time.  When it falls, the stock is
exhausted and the remaining work is construction -- which parallelises. ***

  ⌗ ** The classifier under-counts by construction: ** it matches phrasings, and a latent finding stated
  in new words is missed.  *** So the printed rate is a FLOOR, and a floor is the right side to err on
  for a decision about whether to split. ***

    python3 scripts/latent.py

Written r2620.  Stated for reversal.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

# ** phrasings that mark a finding as LATENT -- the thing was in the corpus and reading found it. **
LATENT = re.compile(
    r"(already had|had already|was already|the corpus had|in its own voice|word-for-word what"
    r"|already wrote down|written for another purpose|already computed it|says so in the same"
    r"|next clause|one sentence further|one clause further|had it the whole time"
    r"|was already there|already delivered|already carries|already answered|already dissolved"
    r"|and neither knew|sitting there|already found)", re.I)


def recorded():
    """** The HAND-KEPT ledger, which supersedes the regex. **  r2624: a signal that decides whether to
    split the work should be RECORDED, not guessed."""
    hp = os.path.join(ROOT, 'LATENT_HISTORY.txt')
    if not os.path.exists(hp):
        return None
    out = []
    for l in open(hp, encoding='utf-8'):
        if not l.strip() or l.startswith('#'):
            continue
        parts = l.split(None, 2)
        out.append((parts[0], parts[1] == 'LATENT', parts[2].strip() if len(parts) > 2 else ''))
    return out


def main():
    rec = recorded()
    if rec:
        print()
        print('  latent.py -- is it safe to split the work yet?   (hand-kept ledger)')
        print()
        for lo, hi in ((0, 10), (10, 20)):
            w = rec[lo:hi]
            if not w:
                continue
            n = sum(1 for _, a, _ in w if a)
            print(f'    {w[0][0]}-{w[-1][0]}: {n} of {len(w)} LATENT  ({n / len(w):.0%})')
        print()
        recent = rec[-13:]
        n = sum(1 for _, a, _ in recent if a)
        print(f'    last 13: {"".join("L" if a else "." for _, a, _ in recent)}   {n} latent')
        print()
        for rev, a, what in rec[-6:]:
            print(f'      {rev}  {"LATENT" if a else "--    "}  {what[:62]}')
        print()
        if n >= 3:
            print('    ⛔ ** DO NOT SPLIT. **  *** The corpus is still telling us things.  Two nodes would')
            print('       both find the same latent thing, or one would BUILD what the other found')
            print('       sitting there. ***')
        else:
            print('    ✔ ** The latent stock looks thin.  What remains is construction, which')
            print('      parallelises. **')
        print()
        return 0
    return _regex_main()


def _regex_main():
    t = open(os.path.join(ROOT, 'CORPUS_MAP.md'), encoding='utf-8', errors='replace').read()
    rows = []
    for m in re.finditer(r'### Revision r(2\d{3}) — [^\n]*\n(.*?)(?=\n### Revision |\Z)', t, re.S):
        rows.append((m.group(1), bool(LATENT.search(m.group(2)))))
    rows.sort()
    rows = rows[-40:]

    print()
    print('  latent.py -- is it safe to split the work yet?')
    print()
    for lo, hi in ((0, 20), (20, 40)):
        w = rows[lo:hi]
        if not w:
            continue
        n = sum(1 for _, a in w if a)
        print(f'    r{w[0][0]}-r{w[-1][0]}: {n} of {len(w)} turns produced a LATENT finding  ({n/len(w):.0%})')
    print()
    recent = rows[-13:]
    n = sum(1 for _, a in recent if a)
    print(f'    last 13: {"".join("⛭" if a else "·" for _, a in recent)}   {n} latent')
    print()
    if n >= 3:
        print('    ⛔ ** DO NOT SPLIT. **  *** The corpus is still telling us things.  A latent finding is')
        print('       one where the answer was already there and reading found it -- and two nodes')
        print('       working in parallel would both find the same one, or one would BUILD what the')
        print('       other found sitting there. ***')
    else:
        print('    ✔ ** The latent stock looks thin.  What remains is construction, which parallelises. **')
    print()
    print('    ⌗ ** The classifier matches phrasings, so a latent finding stated in new words is')
    print('      missed.  *** The rate printed is a FLOOR -- the right side to err on for this')
    print('      decision. ***')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
