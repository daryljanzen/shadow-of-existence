#!/usr/bin/env python3
"""check_branches.py -- THE STRANDING GATE: fail if a branch named in FOR_56 is not merged.

** WHY, and it is a measured cost rather than a hypothetical. **  cc54 ran routed item 38 at production
depth, filed a receipt and three spectra, and pushed them to a branch.  ** The work stranded twice. **  At
r2497 this line reported that "cc54 has never run" -- because it checked the commit log for r24xx / c54.x
prefixes and found none.  ** The work existed, on a branch, correctly done, and invisible. **

cc54, asking for a mechanism: "my work has stranded twice now by sitting on a branch nobody merged.  ** If
there's a mechanism I should be using instead of hoping 56 notices, tell me and I'll use it. **"

** THE MECHANISM: ** a node pushing a branch ** names it in FOR_56.md with its tip SHA **, and 56's standing
obligation is to fetch and merge every branch named there before working leads.
  ⇒ ** A routed note is a DECLARATION, which is the only thing this corpus can gate (L-237).  "A branch
    exists somewhere" is not. **

** WHAT THIS CHECKS: ** every SHA appearing in FOR_56's branch table is ** an ancestor of HEAD **.  If it is
not, the branch is named and unmerged, and work is stranding right now.

⚠ It cannot check for branches nobody named -- ** that is the point of naming them **, and it is why the
obligation is on the pusher as well as on 56.

    python3 corpus/check_branches.py

Written r2507.  Stated for reversal.
"""
import os
import re
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
FOR56 = os.path.join(ROOT, 'FOR_56.md')


def main():
    print()
    print('  check_branches -- is any named branch unmerged?')
    print()
    if not os.path.exists(FOR56):
        print('  FOR_56.md absent; nothing to check.')
        return 0
    t = open(FOR56, encoding='utf-8', errors='replace').read()
    # the branch table: rows naming a 7-40 hex SHA
    shas = []
    for line in t.split('\n'):
        if not line.startswith('|'):
            continue
        for m in re.finditer(r'`([0-9a-f]{7,40})`', line):
            shas.append((m.group(1), line))
    if not shas:
        print('  no branch SHAs named in FOR_56.md.')
        print('  ⌗ That is the clean state -- but it CANNOT distinguish "nothing outstanding" from')
        print('    "somebody pushed and did not declare it".  ** The obligation is on the pusher too. **')
        print()
        return 0

    bad = []
    for sha, line in shas:
        r = subprocess.run(['git', 'merge-base', '--is-ancestor', sha, 'HEAD'],
                           cwd=ROOT, capture_output=True)
        merged = (r.returncode == 0)
        state = 'merged' if merged else '** NOT MERGED **'
        print(f'    {sha}  {state}')
        if not merged:
            bad.append((sha, re.sub(r'\s+', ' ', line)[:110]))

    print()
    if bad:
        for sha, line in bad:
            print(f'  [FAIL] {sha} is named in FOR_56.md and is not an ancestor of HEAD')
            print(f'         {line}')
        print()
        print('  ⛔ WORK IS STRANDING RIGHT NOW.  git fetch the branch and merge it before working')
        print('     any lead -- and run every receipt it brings, on this tree, before landing.')
        return 1
    print('  every named branch is merged.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
