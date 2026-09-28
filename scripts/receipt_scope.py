#!/usr/bin/env python3
"""receipt_scope.py -- ** PO-62 ⓶: WHICH RECEIPTS A PUSH CAN HAVE CHANGED, PER CLASS, FROM A MEASURED READ INDEX. **

Built r6975+70.1 by node 70.  NOT wired into CI.

** WHAT IT DOES. **  `sweep_runner_reads.py --out DIR` now records, for every registered receipt, every path it
opened and every glob it ran (absolute; see its `reads` field).  This builds a READ INDEX from such a trace
and answers, for a git range, which receipts the range can have affected -- under three scopes, because the
three things run on them are born in different places:

  suite       the receipt changed, or a file it READ changed, or a file matching a glob it RAN changed, or
              the receipt names a changed file in its own source (subprocess reads -- `git show`, a child
              python -- are invisible to the trace and are caught by name instead)
              ... what the plain suite needs: prose moves pins, and most receipts read papers.
  tolerance   the receipt changed, or code/data it reads or names changed (.py .npz .json, never prose)
              ... PO-60's third class is born in code or in the ENVIRONMENT, never in prose; the
              environment is not a push and is handled by cadence, not by scope.
  reads       the receipt changed, or a path it read or globbed was DELETED or RENAMED
              ... PO-60's second class is born in the receipt's own paths, or when a file it globs goes.

** MEASURED (r6975+70.1), replaying the last 400 first-parent pushes on main against an index from the full
r6975 trace (871 receipts):
    scope       receipts per push (median / p90 / max)   compute per push (mean)   pushes with nothing
    suite           55 / 172 / 320                          1,648 s                  6 / 400
    tolerance        0 /  18 /  98                            210 s  (x3 builds)   242 / 400
    reads            0 /   1 /  76                             13 s                267 / 400
  RECALL AT BIRTH, every known instance whose birth is inside the history: 8 of 8 -- the four runner-read
  instances (r6574, r6581, r6585, r6894), the two tolerance instances (r6930, r6946), and both suite
  regressions r6973/r6959 introduced.  The ninth, P16_freezeout's pin, was born in the repository's ROOT
  commit and no per-push trigger could see it; the one full sweep did.
  ⚠ WHAT IT CANNOT SEE: an index is a measurement of ONE tree, so a receipt whose reads change is indexed
    stale until the next full trace; a read through a C extension (np.load) is caught only if the file is
    named in the source; and the ENVIRONMENT (numpy, OpenBLAS, python) is not in any diff.

Usage:
    python3 scripts/receipt_scope.py --index TRACE_DIR --range A..B [--scope suite|tolerance|reads]
    python3 scripts/receipt_scope.py --seed      # both ways: a read file's change is in scope, an unread one is not
"""
import argparse
import fnmatch
import glob
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.abspath(__file__)
CODE = ('.py', '.npz', '.json')


def build_index(trace_dir, root):
    idx = {}
    for p in glob.glob(os.path.join(trace_dir, '*.json')):
        d = json.load(open(p))
        rec = os.path.relpath(d['receipt'], root) if os.path.isabs(d['receipt']) else d['receipt']
        files, pats = set(), []
        for r in d.get('reads', []):
            if r.startswith('glob:'):
                if r[5:].startswith(root):
                    pats.append(os.path.relpath(r[5:], root))
            elif r.startswith(root):
                files.add(os.path.relpath(r, root))
        src_path = os.path.join(root, rec)
        src = open(src_path, errors='replace').read() if os.path.exists(src_path) else ''
        names = set(re.findall(r'([A-Za-z0-9_]+\.(?:py|tex|md|txt|npz|json))', src))
        idx[rec] = {'files': files, 'pats': pats, 'names': names}
    return idx


def diff(root, rng):
    ns = subprocess.run(['git', 'diff', '--name-status', '-M', rng], cwd=root, capture_output=True,
                        text=True).stdout.split('\n')
    changed, gone = set(), set()
    for l in ns:
        f = l.split('\t')
        if len(f) < 2:
            continue
        changed.update(f[1:])
        if f[0].startswith(('D', 'R')):
            gone.add(f[1])
    return changed, gone


def scope(idx, changed, gone, which):
    base = {os.path.basename(c) for c in changed}
    out = set()
    for rec, e in idx.items():
        if rec in changed:
            out.add(rec)
        elif which == 'suite':
            if e['files'] & changed or any(fnmatch.fnmatch(c, g) for g in e['pats'] for c in changed) \
                    or e['names'] & base:
                out.add(rec)
        elif which == 'tolerance':
            code = {c for c in changed if c.endswith(CODE) and not c.startswith('scripts/')}
            if {f for f in e['files'] if f.endswith(CODE)} & code \
                    or {n for n in e['names'] if n.endswith(CODE)} & {os.path.basename(c) for c in code}:
                out.add(rec)
        elif which == 'reads':
            if e['files'] & gone or any(fnmatch.fnmatch(g_, p) for p in e['pats'] for g_ in gone):
                out.add(rec)
    return sorted(out)


def seed():
    """Both ways, on a built repository: a change to a file a receipt READ puts it in scope; a change to a file
    it never touched does not; deleting a file it GLOBBED puts it in the reads scope."""
    tmp = tempfile.mkdtemp(prefix='po62_seed_')
    try:
        g = lambda *a: subprocess.run(['git', *a], cwd=tmp, capture_output=True, text=True)
        g('init', '-q')
        g('config', 'user.email', 'seed@x')
        g('config', 'user.name', 'seed')
        os.makedirs(os.path.join(tmp, 'corpus'))
        os.makedirs(os.path.join(tmp, 'receipts', 'S'))
        for n, t in (('read.tex', 'a'), ('unread.tex', 'b'), ('globbed_1.tex', 'c')):
            open(os.path.join(tmp, 'corpus', n), 'w').write(t)
        open(os.path.join(tmp, 'receipts', 'S', 'R1.py'), 'w').write('print(1)\n')
        g('add', '-A')
        g('commit', '-qm', 'base')
        rec = 'receipts/S/R1.py'
        trace = os.path.join(tmp, 'trace')
        os.makedirs(trace)
        json.dump({'receipt': os.path.join(tmp, rec), 'rc': 0, 'events': [],
                   'reads': [os.path.join(tmp, 'corpus', 'read.tex'),
                             'glob:' + os.path.join(tmp, 'corpus', 'globbed_*.tex')]},
                  open(os.path.join(trace, 'r.json'), 'w'))
        idx = build_index(trace, tmp)
        res = {}
        for label, act in (('edit a READ file', lambda: open(os.path.join(tmp, 'corpus', 'read.tex'), 'a').write('x')),
                           ('edit an UNREAD file', lambda: open(os.path.join(tmp, 'corpus', 'unread.tex'), 'a').write('x')),
                           ('delete a GLOBBED file', lambda: os.remove(os.path.join(tmp, 'corpus', 'globbed_1.tex')))):
            head = g('rev-parse', 'HEAD').stdout.strip()
            act()
            g('add', '-A')
            g('commit', '-qm', label)
            ch, gone = diff(tmp, f'{head}..HEAD')
            res[label] = {w: rec in scope(idx, ch, gone, w) for w in ('suite', 'reads')}
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    for k, v in res.items():
        print(f'    {k:24} suite:{v["suite"]!s:5}  reads:{v["reads"]!s:5}')
    ok = (res['edit a READ file']['suite'] and not res['edit an UNREAD file']['suite']
          and res['delete a GLOBBED file']['reads'] and not res['edit a READ file']['reads'])
    print(f'  in scope exactly when it should be: {ok}')
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default=os.path.dirname(os.path.dirname(HERE)))
    ap.add_argument('--index')
    ap.add_argument('--range')
    ap.add_argument('--scope', default='suite', choices=('suite', 'tolerance', 'reads'))
    ap.add_argument('--seed', action='store_true')
    a = ap.parse_args()
    if a.seed:
        print('\n  receipt_scope --seed: is a receipt in scope exactly when a push touches what it reads?\n')
        return seed()
    if not (a.index and a.range):
        ap.print_help()
        return 2
    root = os.path.abspath(a.root)
    idx = build_index(a.index, root)
    ch, gone = diff(root, a.range)
    out = scope(idx, ch, gone, a.scope)
    print('\n'.join(out))
    print(f'  {len(out)} of {len(idx)} receipt(s) in the {a.scope} scope of {a.range}', file=sys.stderr)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
