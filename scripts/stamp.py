#!/usr/bin/env python3
"""stamp.py -- ONE COMMAND, THE NUMBERS, READY TO PASTE.

** WHY.  r2653, Daryl: ** "I need to keep track of how the turns are progressing.  I'd like you to build
an automated stamp you can run and use to generate the updated numbers and then just plonk them down as a
stamp."

  ⇒ *** Every turn this session ended with a hand-assembled header, and a hand-assembled number is one
      that can drift from the file it claims to summarise -- which is exactly what r2612, r2640 and r2650
      each caught after the fact. ***  ** This emits it instead. **

    python3 scripts/stamp.py

Written r2653.  Stated for reversal.
"""
import glob
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))

import queue as Q                                    # noqa: E402


def rev():
    t = open(os.path.join(ROOT, 'CORPUS_MAP.md'), encoding='utf-8', errors='replace').read()
    m = re.search(r'### Revision r(2\d{3})', t)
    return m.group(1) if m else '----'


def sha():
    r = subprocess.run(['git', 'rev-parse', '--short', 'HEAD'],
                       cwd=ROOT, capture_output=True, text=True)
    return r.stdout.strip() or '-------'


def series(path, col):
    out = []
    for l in open(os.path.join(ROOT, path), encoding='utf-8', errors='replace'):
        if l.startswith('r') and len(l.split()) > col:
            out.append(l.split()[col])
    return out


def gates():
    wf = open(os.path.join(ROOT, '.github', 'workflows', 'gates.yml'),
              encoding='utf-8', errors='replace').read().split('\n')
    i = next((k for k, l in enumerate(wf) if 'for g in' in l), None)
    names, k = set(), i
    while i is not None:
        names |= {w.rstrip(';') for w in wf[k].split() if w.startswith('check_')}
        if not wf[k].rstrip().endswith('\\'):
            break
        k += 1
    F = re.compile(r'return 1|exit\(1\)|sys\.exit\(1\)')
    can = {n for n in names
           if os.path.exists(os.path.join(ROOT, 'corpus', n + '.py'))
           and F.search(open(os.path.join(ROOT, 'corpus', n + '.py'),
                             encoding='utf-8', errors='replace').read())}
    return len(can), len(names) - len(can)


def main():
    dh = Q.dark_halves()
    po = Q.po_items()
    lw = Q.ledger_work()
    rt, dp = Q.routed(), Q.dispatch()
    live = [x for x in dh + po + lw + rt + dp if x['open']]
    answered = [x for x in dh if not x['open']]
    po_ans = [x for x in po if not x['open']]
    parked = [x for x in dp if not x['open']]
    g_can, g_rep = gates()

    tbl = series('TABLE_HISTORY.txt', 1)
    deltas = [int(b) - int(a) for a, b in zip(tbl, tbl[1:])][-9:]
    # ** the ledger's second column is LATENT / COMPUTED / INSTRUMENT, or `--` for the older
    # two-state rows.  Taking [0] rendered `--` as `-` and silently mixed the classes. **
    _K = {'LATENT': 'L', 'COMPUTED': 'C', 'INSTRUMENT': 'I'}
    kinds = [_K.get(l.split()[1], 'I') for l in
             open(os.path.join(ROOT, 'LATENT_HISTORY.txt'), encoding='utf-8', errors='replace')
             if l.startswith('r') and len(l.split()) > 1][-13:]

    print()
    print(f'# `{sha()}` · **TABLE {len(live)}** · DARK **{len(answered)}/{len(dh)}** · '
          f'PO **{len(po) - len(po_ans)} open, {len(po_ans)} answered**')
    print()
    print(f'**CHART `{deltas}`** · **TURNS `{"".join(kinds)}`** — '
          f'LATENT {kinds.count("L")} · **COMPUTED {kinds.count("C")}** · INSTRUMENT {kinds.count("I")}')
    print()
    print(f'**LEDGER {len(lw)} · ROUTED {len(rt)} · DISPATCH {len(dp) - len(parked)} live, '
          f'{len(parked)} parked · GATES {g_can} that can fail (+{g_rep} report-only)**')
    print()
    print(f'*r{rev()} · dark halves still open: '
          f'{", ".join(x["id"] for x in dh if x["open"])}*')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
