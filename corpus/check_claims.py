#!/usr/bin/env python3
"""check_claims.py -- THE COLLISION GATE: fail if this node is editing a file another node holds.

** WHY, and the evidence is on the record twice in both directions. **
  * ** r2434 ** -- a union merge kept both sides of one 46,291-character register row differing only by a
    renumber, ** duplicating L-171 on adjacent rows **.  The duplicate-ID gate fired for the first time.
  * ** c54.194 ** -- the fork's merge onto this line's tip ** duplicated L-500 through L-506, seven register
    rows **, and it named the failure itself: "exactly the c54.182/c54.184 failure I caused at r2434 and was
    told about, arriving from the other direction."
  * ** r2497 ** -- the fork's `gates.yml` had ** silently dropped three view-checks this line had added **.
  ⇒ *** Every one is the same shape: two nodes edited one file with no way to know. ***

** WHAT IT CHECKS, and only what a DECLARATION can support (L-237): **
  (1) ** every file this node has modified but not committed is either claimed BY THIS NODE or is on the
      always-shared list ** -- otherwise a collision is being created right now, unseen;
  (2) ** no file is claimed by two nodes at once **;
  (3) ** this node is not holding a claim on a file it has already committed and pushed ** -- a stale claim
      blocks the others for nothing.

⚠ ** A CLAIM IS NOT A LOCK.  Nothing here prevents an edit. **  It is a declaration, and its whole value is
that ** a collision becomes visible BEFORE the merge rather than after it. **

    NODE=56 python3 corpus/check_claims.py

Written r2503.  Stated for reversal.
"""
import os
import re
import sys
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
CLAIMS = os.path.join(ROOT, 'CLAIMS.md')

SHARED = {
    'THE_LIVE_ARC.md', 'CORPUS_MAP.md', 'receipts/INDEX.md', 'ABSORPTION.md',
    'FOR_54.md', 'FOR_56.md', 'CLAIMS.md', 'BOARD.md', 'THE_BURN_DOWN.md',
    'WHATS_TEED_UP.md', 'ID_SPACE_CENSUS.md', 'OPEN_PROBLEMS_MAP.md',
    'DOCUMENT_LEDGER.md', 'THE_WORK.md', 'FORK_c54.md', 'THE_PLAN.md',
    'THE_OPEN_PROBLEMS_LEDGER.md', 'capstones/THE_WISDOM_LEDGER.md',
}


def node():
    return os.environ.get('NODE', '56')


def table():
    """(file, node, since, what) for every claim row"""
    if not os.path.exists(CLAIMS):
        return []
    rows = []
    for line in open(CLAIMS, encoding='utf-8', errors='replace').read().split('\n'):
        if not line.startswith('|'):
            continue
        c = [x.strip() for x in line.strip().strip('|').split('|')]
        if len(c) < 4 or c[0] in ('file', '---') or c[0].startswith('*('):
            continue
        rows.append(tuple(c[:4]))
    return rows


def dirty():
    r = subprocess.run(['git', 'status', '--porcelain'], cwd=ROOT,
                       capture_output=True, text=True)
    out = []
    for line in r.stdout.split('\n'):
        if len(line) > 3:
            out.append(line[3:].strip().strip('"'))
    return out


def main():
    me = node()
    rows = table()
    mods = dirty()
    fails = []
    print()
    print(f'  check_claims -- node {me}')
    print()
    print(f'  {len(rows)} claim(s) held; {len(mods)} file(s) modified here')

    held = {}
    for f, n, _, _ in rows:
        f = f.strip('`')
        held.setdefault(f, set()).add(n)

    # (2) double claims
    for f, ns in held.items():
        if len(ns) > 1:
            fails.append(f'{f} is claimed by {", ".join(sorted(ns))} at once')

    # (1) uncommitted edits to files this node has not claimed
    mine = {f for f, ns in held.items() if me in ns}
    for f in mods:
        if f in SHARED or f in mine:
            continue
        if f.startswith(('receipts/', 'computations/', 'kills/', 'figures/')):
            continue  # per-node artefact trees: a collision here is a duplicate name, caught elsewhere
        others = held.get(f, set()) - {me}
        if others:
            fails.append(f'{f} is modified here but held by {", ".join(sorted(others))}')
        else:
            print(f'     [warn] {f} modified without a claim '
                  f'-- fine if nobody else is in it, but nothing says so')

    # (3) stale claims
    for f in mine:
        if f not in mods and os.path.exists(os.path.join(ROOT, f)):
            print(f'     [warn] {me} holds {f} with no local edit -- release it if pushed')

    print()
    if fails:
        for f in fails:
            print(f'  [FAIL] {f}')
        print()
        print('  ⛔ A COLLISION IS BEING CREATED RIGHT NOW.  Claim it, or route your change to the')
        print('     holder via FOR_54.md / FOR_56.md instead of editing under them.')
        return 1
    print('  no collisions declared.')
    print('  ⌗ A claim is a DECLARATION, not a lock -- its value is that a collision becomes visible')
    print('    BEFORE the merge rather than after it.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
