#!/usr/bin/env python3
"""scope_reads_probe.py -- THE `reads` SCOPE PROVES, IN ITS OWN RUN, THAT IT COULD HAVE FIRED.  r7421 ② (66), built r7423+70.

** WHY.  **  The `reads` scope selects a receipt only when a push DELETES or RENAMES something it traced.  It fired
on `0` of `20` revisions (r7411+70), and four one-off probes showed the zero was design (r7413+70.3).  But no run
re-checked it, so on any real revision a `0` could not tell NOTHING-TO-SELECT from a BROKEN selector -- and the two
have opposite remedies.  Standing rule (r7421, PO-78's fifteenth face): ** a gate whose population can be empty
must prove IN ITS OWN RUN that it could have fired. **  After this step, a zero is a measured zero.

** WHAT IT DOES.  **  It calls `receipt_scope.scope()` -- the job's own selector, not a copy -- on the job's own
index, with SYNTHETIC change sets.  Nothing in the tree is touched and nothing is committed: `scope()` is a pure
function of the index and the sets it is handed.
  seed 1   `gone` = the file the most receipts trace (ties by name); every receipt tracing it must be scoped.
  seed 2   `gone` = the first tracked member of the most-shared traced glob/directory; it must scope >= 1.
  control  `gone` = a path that exists nowhere; it must scope 0.
Exit 1 if any of the three fails.

    python3 scripts/scope_reads_probe.py
"""
import collections
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import receipt_scope as rs  # noqa: E402

CONTROL = 'no/such/path/r7421_control.none'


def main():
    idx = rs.load(ROOT)[0]
    tree = set(subprocess.run(['git', '-C', ROOT, 'ls-files'], capture_output=True, text=True,
                              check=True).stdout.split('\n'))
    by_file = collections.Counter(f for e in idx.values() for f in e['files'] if f in tree)
    f1 = sorted(by_file, key=lambda f: (-by_file[f], f))[0]
    readers = {r for r, e in idx.items() if f1 in e['files']}
    s1 = set(rs.scope(idx, set(), {f1}, set(), 'reads'))

    by_pat = collections.Counter(p for e in idx.values() for p in e['pats'] + e['dirs'])
    f2 = pat = None
    for pat in sorted(by_pat, key=lambda p: (-by_pat[p], p)):
        members = sorted(t for t in tree if t and rs.pmatch(t, pat))
        if members:
            f2 = members[0]
            break
    s2 = set(rs.scope(idx, set(), {f2}, set(), 'reads')) if f2 else set()
    s0 = rs.scope(idx, set(), {CONTROL}, set(), 'reads')

    ok1 = bool(readers) and readers <= s1
    ok2 = len(s2) >= 1
    ok0 = len(s0) == 0
    print('  SCOPE-READS SEEDED PROBE -- can this selector fire, measured in this run (r7421 ②)')
    print(f'    seed 1  a traced read deleted: {f1}  -> scopes {len(s1)} '
          f'(its {len(readers)} tracing receipt(s) all in it: {ok1})')
    print(f'    seed 2  a member of glob/dir {pat!r} deleted: {f2}  -> scopes {len(s2)}')
    print(f'    control a path that exists nowhere -> scopes {len(s0)}')
    if ok1 and ok2 and ok0:
        print('  the selector fires on both seeds and not on the control, so a 0 on this push is a measured 0.')
        return 0
    print('  ⛔ [FAIL] the reads selector did not read two-sidedly on synthetic input: a 0 below this line '
          'would be indistinguishable from a broken selector.')
    return 1


if __name__ == '__main__':
    sys.exit(main())
