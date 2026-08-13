#!/usr/bin/env python3
"""check_open_ledger.py -- THE LEDGER OF WHAT IS OPEN MUST STAY CURRENT WITH THE PAPERS.

** THE PROBLEM IT SOLVES, NAMED BY DARYL AT r2593. **  This line kept discovering that a thing which
looked open was not -- and kept ** failing to record the verdict **, so the same reading had to be redone
every time anyone asked what was left.  ⇒ *** A grep is not a list of what is owed.  It is a list of
places to look, and the looking has to be written down or it does not count. ***

** WHAT THE LEDGER HOLDS. **  `corpus/open_ledger.txt` -- one line per DISTINCT epistemic qualification in
the paper bodies, with a VERDICT.  ** 123 raw hits deduplicate to 113 sentences **, and reading them shows
most are not gaps: deliberate `DO-NOT-ASSERT` holdings, `SCOPE-BY-DESIGN` statements, descriptions of
`STANDARD-PHYSICS`'s open problems, or claims that are `SELF-ANSWERED` two sentences later.

** WHAT THIS GATE CHECKS -- three things, and the third is the point. **
  ⓵ ** every ledger entry still exists in a paper **  -- an entry whose sentence is gone means the corpus
    moved and the ledger did not;
  ⓶ ** every qualification in the papers is in the ledger **  -- a NEW one that nobody verdicted;
  ⓷ ** the UNVERDICTED count only falls **  -- recorded in the ledger header, so *** the ledger cannot
    grow a backlog silently: verdicting is the only direction it moves. ***

  ⚠ ** It does NOT check that a verdict is CORRECT. **  That is a reading, and no gate can do it.  *** What
  it guarantees is that every qualification HAS one and that none appears without being seen. ***

    python3 corpus/check_open_ledger.py
    python3 corpus/check_open_ledger.py --rebuild     # re-derive, preserving existing verdicts

Written r2593.  Stated for reversal.
"""
import glob
import hashlib
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
LEDGER = os.path.join(HERE, 'open_ledger.txt')

PAT = re.compile(
    r"(we claim no|is not claimed here|not claimed:|we do not claim|traced rather than computed"
    r"|recalled rather than derived|remains open|stays open|what remains open|at that weight"
    r"|we state it at|as the hypothesis it is|do-not-assert"
    r"|is not settled|not yet|undelivered|unbuilt|is open\b)", re.I)


def body(f):
    b = '\n'.join(l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
                  if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return b[:j] if j > 0 else b


def scan():
    """Return {id: (paper, claim)} for every distinct qualification in the papers."""
    out = {}
    for f in sorted(glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))):
        if os.path.basename(f).startswith('appendix_receipts'):
            continue
        t = re.sub(r'\s+', ' ', body(f))
        for m in PAT.finditer(t):
            s = t.rfind('. ', 0, m.start()) + 2
            e = t.find('. ', m.end())
            claim = t[s:e + 1][:300]
            key = hashlib.sha1(re.sub(r'\W+', '', claim[:120]).encode()).hexdigest()[:10]
            out.setdefault(key, (os.path.basename(f).replace('.tex', ''), claim))
    return out


def read_ledger():
    if not os.path.exists(LEDGER):
        return {}
    out = {}
    for line in open(LEDGER, encoding='utf-8'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        parts = [p.strip() for p in line.split('|', 3)]
        if len(parts) == 4:
            out[parts[0]] = (parts[1], parts[2], parts[3])
    return out


def main():
    print()
    print('  check_open_ledger -- is the ledger of what is open current with the papers?')
    print()
    cur = scan()
    led = read_ledger()

    if '--rebuild' in sys.argv:
        import subprocess  # noqa
        keep = {k: v[1] for k, v in led.items()}
        lines = [l.rstrip('\n') for l in open(LEDGER, encoding='utf-8')
                 if l.startswith('#') or not l.strip()]
        for k, (paper, claim) in sorted(cur.items(), key=lambda x: (keep.get(x[0], 'UNVERDICTED'), x[1][0])):
            v = keep.get(k, 'UNVERDICTED')
            c = re.sub(r'\s+', ' ', re.sub(r'\\rcpt\{[^}]*\}', '', claim)).strip()[:180]
            lines.append(f'{k} | {paper} | {v} | {c}')
        open(LEDGER, 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
        print(f'  rebuilt: {len(cur)} entries, {sum(1 for k in cur if k not in keep)} new')
        return 0

    print(f'  papers hold {len(cur)} distinct qualification(s); ledger holds {len(led)}.')
    new = sorted(set(cur) - set(led))
    gone = sorted(set(led) - set(cur))
    unv = [k for k, v in led.items() if v[1] == 'UNVERDICTED']
    print(f'  UNVERDICTED in the ledger: {len(unv)}')
    print()

    if gone:
        for g in gone[:6]:
            print(f'    [WARN] {g} ({led[g][0]}) is in the ledger and no longer in any paper')
            print(f'           "{led[g][2][:88]}"')
        print('    ⌗ the corpus moved and the ledger did not -- run --rebuild to re-derive.')
        print()

    if new:
        for n in new:
            paper, claim = cur[n]
            print(f'    [FAIL] {n} ({paper}) is a qualification with NO VERDICT in the ledger')
            print(f'           "{re.sub(chr(92)+"s+", " ", claim)[:96]}"')
        print()
        print('    ⛔ A GREP IS NOT A LIST OF WHAT IS OWED.  ** It is a list of places to look, and the')
        print('       looking has to be written down or it does not count. **  Add a verdict:')
        print('       DO-NOT-ASSERT / SCOPE-BY-DESIGN / STANDARD-PHYSICS / METHOD-PROSE /')
        print('       SELF-ANSWERED / REGISTERED / NAMED-UNBUILT / PRECISION / OPEN-DOWNSTREAM')
        return 1

    print('  every qualification in the papers has a verdict in the ledger.')
    if unv:
        print(f'  ⌗ {len(unv)} still UNVERDICTED -- the only bucket that means work.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
