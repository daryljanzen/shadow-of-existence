#!/usr/bin/env python3
"""r7343+cc66.1: the MANDATED-SPLIT-FORM variant of the narrowed hop, as measured in READING.md ④.

Applied to a COPY of scripts/mutate_assertions.py (the instrument in the tree is never touched).  It adds
`_split_bound` and requires it in the hop branch, so the hop follows a loop/comprehension binding ONLY
where that binding is a split of something -- the form r7339 ① mandated.

    python3 -I split_patch.py <copy-of-mutate_assertions.py>

Result on this corpus: R = 67, and it keeps all three of the keys that refused r7341.
"""
import sys

HELPER = '''
_SPLITTY = ('split', 'splitlines', 'rsplit')


def _split_bound(cont, tasg, asg):
    """r7343+cc66.1: is the container bound, by a loop/comprehension target that `asg` does NOT carry,
    to a SPLIT of something?  That is the r7339-MANDATED locus form and nothing else."""
    for n in ast.walk(cont):
        if not isinstance(n, ast.Name):
            continue
        plain = asg.get(n.id, [])
        for v in tasg.get(n.id, []):
            if any(v is w for w in plain):
                continue
            for c in ast.walk(v):
                if (isinstance(c, ast.Call) and isinstance(c.func, ast.Attribute)
                        and c.func.attr in _SPLITTY):
                    return True
    return False


def _quote_site(n, neg, asg, fns, src):'''

ANCHOR = '\ndef _quote_site(n, neg, asg, fns, src):'
OLD = '            if trace is None and _hop_ok(lit) and not ('
NEW = '            if trace is None and _hop_ok(lit) and _split_bound(cont, tasg, asg) and not ('

p = sys.argv[1]
s = open(p).read()
assert s.count(ANCHOR) == 1 and s.count(OLD) == 1, 'anchor not found exactly once'
open(p, 'w').write(s.replace(ANCHOR, HELPER, 1).replace(OLD, NEW, 1))
print('patched', p)
