#!/usr/bin/env python3
"""r7423+70 L-b..L-e: the reader on LOCAL fake chains (refs/ci/lean-probe/*), built with the same plumbing the writer
uses, read through `lean_record.status` itself, and deleted afterwards.  Nothing is pushed."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'scripts'))
import lean_record as L  # noqa: E402

WF = 'formalisation-mathlib'
KEY = L.paths_key(WF)
STALE = KEY[:-6] + ('000000' if not KEY.endswith('000000') else '111111')


def chain(name, recs):
    """recs oldest first: (key, conclusion)"""
    parent = ''
    for i, (k, c) in enumerate(recs):
        body = f'head {"0" * 40}\nkey {k}\nconclusion {c}\nrun probe{i}\nevent push\n'
        blob = L.git('hash-object', '-w', '--stdin', inp=body, check=True).stdout.strip()
        tree = L.git('mktree', inp=f'100644 blob {blob}\tRECORD\n', check=True).stdout.strip()
        args = ['commit-tree', tree, '-m', f'probe {i}'] + (['-p', parent] if parent else [])
        parent = L.git(*args, check=True).stdout.strip()
    ref = f'refs/ci/lean-probe/{name}'
    L.git('update-ref', ref, parent, check=True)
    return ref


CASES = [
    ('control-green',       [(KEY, 'success')],                       L.GREEN,        'L-a control'),
    ('stale-success',       [(STALE, 'success')],                     L.UNANSWERABLE, 'L-b'),
    ('stale-newest',        [(KEY, 'failure'), (STALE, 'success')],   L.NOT_GREEN,    'L-b'),
    ('matching-failure',    [(KEY, 'failure')],                       L.NOT_GREEN,    'L-c'),
    ('newest-wins',         [(KEY, 'success'), (KEY, 'failure')],     L.NOT_GREEN,    'L-c'),
    ('cancelled-skipped',   [(KEY, 'success'), (KEY, 'cancelled')],   L.GREEN,        'L-e'),
    ('cancelled-only',      [(KEY, 'cancelled')],                     L.UNANSWERABLE, 'L-e'),
]
bad = 0
for name, recs, want, arm in CASES:
    ref = chain(name, recs)
    got, why = L.status(WF, chain=ref, fetch=False)
    ok = got == want
    bad += not ok
    print(f'  {"OK  " if ok else "FAIL"} {arm:12} {name:18} want {want:12} got {got:12} -- {why[:90]}')
    L.git('update-ref', '-d', ref)
got, why = L.status(WF, chain='refs/ci/lean-probe/none', fetch=False)
print(f'  {"OK  " if got == L.UNANSWERABLE else "FAIL"} L-d          no-chain           want UNANSWERABLE got {got} -- {why[:80]}')
bad += got != L.UNANSWERABLE
print(f'  {len(CASES) + 1 - bad} of {len(CASES) + 1} as predicted; GREEN read only where a matching success is newest')
sys.exit(1 if bad else 0)
