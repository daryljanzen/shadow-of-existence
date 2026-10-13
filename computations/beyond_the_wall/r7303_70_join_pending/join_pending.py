#!/usr/bin/env python3
"""r7303+70: join every PENDING blind batch to the primary verdict that has since landed in the ledger.

A pending batch (scripts/double_read_agreement.py's term) has one verdict column filled by its blind reader and the other
-- the primary's -- empty.  For each key this finds the FIRST ledger commit at which the row's verdict left
UNADJUDICATED (the primary landing), takes the verdict there, and checks it against the ledger at REV.  A key whose
verdict moved after landing is reported, and the LANDING verdict is used: that is the primary's own read.

    python3 join_pending.py [REV] [--write]     # REV defaults to origin/main; --write fills the empty column in place

Only the empty verdict cell of each row is written, plus one `#` line saying where it came from.  Nothing is reconciled."""
import json
import os
import subprocess
import sys

ROOT = subprocess.run(['git', 'rev-parse', '--show-toplevel'], capture_output=True, text=True,
                      cwd=os.path.dirname(os.path.abspath(__file__))).stdout.strip()
LEDGER = 'corpus/quote_pin_baseline.tsv'
OPEN = {'UNADJUDICATED', 'UNADJUDICATED-PINNED', ''}
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import double_read_agreement as P  # noqa: E402


def git(*a):
    return subprocess.run(['git', '-C', ROOT, *a], capture_output=True, text=True, check=True).stdout


def ledger_at(rev):
    out = {}
    for ln in git('show', f'{rev}:{LEDGER}').split('\n'):
        c = ln.split('\t')
        if len(c) >= 6 and not ln.startswith('#'):
            try:
                out[(c[0], json.loads(c[1]))] = c[5].strip()
            except ValueError:
                pass
    return out


def landing(keys, rev):
    """{key: (sha, subject, verdict)} at the first commit where each key's verdict left OPEN"""
    commits = git('log', '--reverse', '--since=5.days', '--format=%h\t%s', rev, '--', LEDGER).strip().split('\n')
    todo, got = set(keys), {}
    for line in commits:
        sha, subj = line.split('\t', 1)
        L = ledger_at(sha)
        for k in list(todo):
            if L.get(k, '') not in OPEN:
                got[k] = (sha, subj, L[k])
                todo.discard(k)
        if not todo:
            break
    return got


def main():
    rev = next((a for a in sys.argv[1:] if not a.startswith('--')), 'origin/main')
    now = ledger_at(rev)
    pend = [x for x in P.batches() if x['shape'] == 'batch' and not x['pairs']]
    total = 0
    for x in pend:
        path = os.path.join(ROOT, x['file'])
        lines = open(path, encoding='utf-8').read().split('\n')
        rows = [(i, l.split('\t')) for i, l in enumerate(lines) if l and not l.startswith('#')]
        side = {3 if c[3].strip() == '' else 2 for _, c in rows if len(c) >= 4}
        if len(side) != 1:
            print(f'  ⛔ {x["file"]}: the empty column is not the same on every row -- not joined')
            continue
        side = side.pop()
        keys = [(c[0], json.loads(c[1])) for _, c in rows]
        land = landing(keys, rev)
        missing = [k for k in keys if k not in land]
        print(f'== {x["file"]}  (readers {" | ".join(x["readers"])}; filling column {side + 1})')
        if missing:
            print(f'  waiting: {len(missing)} of {len(keys)} still open at {rev} -- not joined')
            continue
        for (i, c), k in zip(rows, keys):
            sha, subj, v = land[k]
            moved = '' if now.get(k) == v else f'  ⌗ MOVED since landing: {rev} reads {now.get(k)}'
            print(f'  {json.dumps(k[1], ensure_ascii=False)[:50]:<52} {v:<13} landed {sha} {subj[:40]}{moved}')
            c[side] = v
            lines[i] = '\t'.join(c)
        shas = sorted({land[k][0] for k in keys})
        note = (f'# r7303+70: primary column joined from the ledger at its LANDING commit(s) {", ".join(shas)} '
                f'(join_pending.py); checked against {rev}.  Only the empty cells were written.')
        hdr = max(i for i, l in enumerate(lines) if l.startswith('#') and i < rows[0][0])
        lines.insert(hdr + 1, note)
        total += len(keys)
        if '--write' in sys.argv:
            open(path, 'w', encoding='utf-8').write('\n'.join(lines))
    print(f'  {total} key(s) joinable{" and written" if "--write" in sys.argv else ""}')


if __name__ == '__main__':
    main()
