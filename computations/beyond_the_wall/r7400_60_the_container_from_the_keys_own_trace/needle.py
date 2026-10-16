#!/usr/bin/env python3
"""r7400 (60) -- WHAT THE MANGLED NEEDLE COSTS, measured so the one-line correction can be ROUTED with a
price rather than an opinion.  ⛔ NOT A REGISTERED ARM: `PREDICTION.md`'s `⒠` registered the SUBSET
RELATION at exact `0` violations and that arm is REFUTED; this is the follow-on measurement of the
refutation, reported and never banded after the fact.

`_present_at`'s `SOURCE` branch builds its file list as

    words = ' '.join(lit.split()[:3]).replace('\\\\', '')
    names = <git grep -l -F -e words.split()[0]>

so a literal whose first word carries a backslash searches for a string that cannot occur.  This runs the
branch twice over every exposed key -- as it stands, and with the first word UNMANGLED -- and reports how
many verdicts move.

    python3 -I needle.py
"""
import importlib.util
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('r7400_cost', os.path.join(HERE, 'cost.py'))
C = importlib.util.module_from_spec(spec)
sys.modules['r7400_cost'] = C
spec.loader.exec_module(C)
Q = C.Q


def grep_names(sha, needle, receipt):
    out = Q._git('grep', '-l', '-F', '-e', needle, sha, '--').stdout
    return [n.split(':', 1)[1] for n in out.split('\n') if ':' in n and n.split(':', 1)[1] != receipt]


def present_with(sha, lit, receipt, needle):
    """`_present_at` itself, with the needle it greps for replaced -- the file list is the only change"""
    names = grep_names(sha, needle, receipt)
    return Q._present_at(sha, lit, 'SOURCE', receipt) if needle is None else _loop(sha, lit, names)


def _loop(sha, lit, names):
    real = Q._git

    def fake(*a):
        if a and a[0] == 'grep':
            return type('R', (), {'stdout': '\n'.join(f'{sha}:{n}' for n in names),
                                  'stderr': '', 'returncode': 0})()
        return real(*a)
    Q._git = fake
    try:
        return Q._present_at(sha, lit, 'SOURCE', '')
    finally:
        Q._git = real


src = [r for r in C.ledger() if r[2] == 'SOURCE']
exposed = [r for r in src if '\\' in ' '.join(r[1].split()[:3])]
print(f'# r7400 (60) -- the mangled needle, at FRAME {C.FULL[:12]}')
print(f'# {len(exposed)} of {len(src)} SOURCE keys carry a backslash in their first three words')

t0 = time.time()
moved, same = [], 0
for receipt, lit, target, tier, verdict in exposed:
    mangled = ' '.join(lit.split()[:3]).replace('\\', '').split()
    honest = lit.split()[:1]
    a = present_with(C.FULL, lit, receipt, mangled[0] if mangled else lit)
    b = present_with(C.FULL, lit, receipt, honest[0] if honest else lit)
    if a != b:
        moved.append((receipt, lit, tier, verdict, a, b))
    else:
        same += 1
wall = time.time() - t0

print(f'# WALL {wall:.1f}s for {2 * len(exposed)} branch runs on this container')
print(f'# VERDICTS THAT MOVE when the needle is left as the literal wrote it: {len(moved)} of {len(exposed)}')
print(f'#   unchanged: {same}')
print('# ⌗ A move is always ABSENT -> PRESENT: the mangled needle can only match FEWER files, so the')
print('#   branch as it stands can only over-report absence.  Direction asserted by the rows below.')
print('# receipt, literal (JSON), tier, verdict, as-it-stands, with the honest needle')
for m in sorted(moved):
    print('\t'.join((m[0], json.dumps(m[1], ensure_ascii=False), m[2], m[3], str(m[4]), str(m[5]))))
