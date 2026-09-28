#!/usr/bin/env python3
"""receipt_scope.py -- ** PO-62 ⓶: WHICH RECEIPTS A PUSH CAN HAVE CHANGED, PER CLASS, FROM A MEASURED READ INDEX. **

Built r6975+70.1 by node 70; made wirable r6977+70.1 (a committed index, a CI range, an expiry).

** WHAT IT DOES. **  `sweep_runner_reads.py --out DIR` records, for every registered receipt, every path it
opened, every glob it ran and every module it imported (see its `reads` field).  `--emit` condenses one such
full trace into `receipts/READ_INDEX.json`, the committed READ INDEX; everything else loads that file and
answers, for a git range, which receipts the range can have affected -- under three scopes, because the
three things run on them are born in different places:

  suite       the receipt changed, or a file it READ or IMPORTED changed, or a file matching a glob it RAN
              changed, or a file its own source NAMES changed (subprocess reads -- `git show`, a child
              python -- are invisible to the trace and are caught by name instead)
              ... what the plain suite needs: prose moves pins, and most receipts read papers.
  tolerance   the same, restricted to changed files that are not prose (`.tex` `.md` `.bib`)
              ... PO-60's third class is born in code, data or the ENVIRONMENT, never in prose; the
              environment is not a push and is handled by `check_env_fingerprint`, not by scope.
  reads       the receipt changed, or a path it read or globbed was DELETED or RENAMED
              ... PO-60's second class is born in the receipt's own paths, or when a file it globs goes.

** THE INDEX FILE, AND WHY IT IS SHAPED THIS WAY. **  One line per receipt, sorted, so a refresh diffs as the
receipts whose reads changed and nothing else.  Per receipt: `sha` (its git blob when traced), `s` (seconds
under the trace, which the runner uses to schedule longest-first), `r` (files read or imported), `g` (globs),
`d` (directories read whole), `n` (file names its source mentions that no read already covers).  A
directory the receipt read at least half of, and at least eight files of, goes in `d` as `dir/*` -- a
SUPERSET, so it can only widen a scope.  ⌗ A file read (`r`, `d`) is in scope when its CONTENT changes; a
glob (`g`) only when its MEMBERSHIP does -- a path matching it added, deleted or renamed -- because a glob
returns names, and whatever the receipt then opened is a read of its own.  Patterns are matched with glob
semantics: `*` stays inside a directory and only `**` crosses one.
The header carries the commit and tree digest it was traced at, so a stale index is visible, not inferred.

** WHAT HAPPENS WHEN IT IS STALE -- STATED HERE AND PRINTED BY EVERY SCOPED RUN. **
  * A receipt edited since the trace (its blob differs from `sha`) is scoped on its traced reads PLUS the
    names and imports in its CURRENT source.  A receipt added since has only the latter.  Both counts are
    printed.  What that can miss: a read the edit added through a computed path.
  * The WHOLE index expires MAX_AGE_DAYS after the commit it was traced at: every scoped job then FAILS,
    saying the remedy -- a full trace and `--emit`, committed -- rather than scoping on a map of a tree
    that has moved on.  The monthly backstop is what refreshes it (the `index` step of that job).

** MEASURED (r6977+70.1) ** -- `--replay 400` re-derives this from the committed index (traced at r6977, 871
receipts) and main's last 400 first-parent pushes (09-12 .. 09-28); compute is the index's traced seconds:
    scope       receipts per push (median/p90/max)   compute per push (mean/p90/max)   pushes with nothing
    suite           90 / 184 / 397                     1,547 / 3,598 / 6,562 s               7 / 400
    tolerance        5 /  40 / 232                       674 / 1,539 / 5,937 s  (x3)       87 / 400
    reads            0 /   1 / 152                        19 /     9 / 3,665 s             265 / 400
  ⛔ SUPERSEDES r6975+70.1's table, which was taken with a tracer that recorded no glob at its real path
    and no import: the tolerance scope there (210 s) could not see `ACOUSTIC_two_arm.py`, the helper most
    P15 receipts import -- 12 of these 400 pushes changed it, and it is most of the tolerance mean.
  RECALL AT BIRTH: every regression whose birth is in history is in its class's scope at the push that made
    it -- 10 of 10: the four runner-read instances and the two tolerance instances (each born editing the
    receipt), L275/U1 at r6973, the three P15 inventories at cc66's r6959 switches, and the two receipts
    r6975 itself broke (L165/D2, P10_the_degeneracy...), both in r6975's own scope of 196.

  ⚠ RECALL LIMITS: an index is a measurement of ONE tree (above); a read through a C extension (np.load)
    or a subprocess is caught only if the file is NAMED in the source; and the ENVIRONMENT (numpy,
    OpenBLAS, python) is not in any diff.

Usage:
    python3 scripts/receipt_scope.py --emit TRACE_DIR                  # write receipts/READ_INDEX.json
    python3 scripts/receipt_scope.py --range A..B [--scope S] [--list OUT]
    python3 scripts/receipt_scope.py --ci [--scope S] --list OUT       # range from the GitHub event
    python3 scripts/receipt_scope.py --replay N                         # scope the last N pushes to main
    python3 scripts/receipt_scope.py --seed      # both ways, through the REAL tracer: a read file's change
                                                 # is in scope, an unread one is not
"""
import argparse
import ast
import collections
import glob
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

HERE = os.path.abspath(__file__)
ROOT = os.path.dirname(os.path.dirname(HERE))
INDEX = os.path.join('receipts', 'READ_INDEX.json')
TRACER = os.path.join('scripts', 'sweep_runner_reads.py')      # imported by every trace; not a receipt's read
PROSE = ('.tex', '.md', '.bib')
MAX_AGE_DAYS = 35                 # the monthly backstop plus a week: one missed refresh is visible, two fail
COLLAPSE_MIN, COLLAPSE_FRAC = 8, 0.5
SUBTREE_MIN = 40                  # a receipt reading this many `T/...*.ext` files is indexed as `T/**/*.ext`
NAME_RE = re.compile(r'([A-Za-z0-9_.-]+\.(?:py|tex|md|txt|npz|npy|json|dat|csv|bib))')
WILD = re.compile(r'[*?\[]')


_PM = {}


def pmatch(path, pat):
    """glob semantics, not fnmatch's: `*` and `?` stay inside one directory and only `**` crosses one.
    ⛔ r6977+70.1: `fnmatch` lets `*` match `/`, so a receipt that globbed the repository root (`*`) was in
    scope for every change anywhere in the tree."""
    rx = _PM.get(pat)
    if rx is None:
        out, i = '', 0
        while i < len(pat):
            c = pat[i]
            if pat.startswith('**/', i):
                out, i = out + '(?:.*/)?', i + 3
                continue
            if pat.startswith('**', i):
                out, i = out + '.*', i + 2
                continue
            if c == '*':
                out += '[^/]*'
            elif c == '?':
                out += '[^/]'
            elif c == '[':
                j = pat.find(']', i + 1)
                if j < 0:
                    out += re.escape(c)
                else:
                    body = pat[i + 1:j]
                    out += '[' + ('^' + body[1:] if body.startswith('!') else body) + ']'
                    i = j
            else:
                out += re.escape(c)
            i += 1
        rx = _PM[pat] = re.compile(out + r'\Z')
    return rx.match(path) is not None


def git(root, *a):
    return subprocess.run(['git', *a], cwd=root, capture_output=True, text=True).stdout


def blobs(root):
    """path -> git blob sha, for every tracked file (the INDEX, i.e. HEAD on a CI checkout)"""
    out = {}
    for l in git(root, 'ls-files', '-s').split('\n'):
        if '\t' in l:
            meta, p = l.split('\t', 1)
            out[p] = meta.split()[1]
    return out


def source_names(src):
    """the file names a source mentions, and the modules it imports as `X.py` -- the static half"""
    names = set(NAME_RE.findall(src))
    try:
        for node in ast.walk(ast.parse(src)):
            if isinstance(node, ast.Import):
                names.update(a.name.split('.')[0] + '.py' for a in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module and not node.level:
                names.add(node.module.split('.')[0] + '.py')
    except (SyntaxError, ValueError):
        pass
    return names


# ------------------------------------------------------------------------------------ emit
def emit(trace_dir, root, out, commit=None):
    """condense one FULL trace into the committed index: one line per receipt, sorted"""
    root = os.path.abspath(root)
    bl = blobs(root)
    bydir = collections.defaultdict(set)
    for t in bl:
        bydir[os.path.dirname(t)].add(t)
    repo_names = {os.path.basename(t) for t in bl}      # a name matches a changed file by basename, so only
                                                          # names some tracked file carries can ever match
    recs, red, timeouts = {}, 0, []
    for p in sorted(glob.glob(os.path.join(trace_dir, '*.json'))):
        d = json.load(open(p))
        rec = os.path.relpath(d['receipt'], root) if os.path.isabs(d['receipt']) else d['receipt']
        if d.get('timeout'):
            timeouts.append(rec)
        red += d.get('rc') not in (0, None)
        files, pats = set(), set()
        for r in d.get('reads', []):
            isg = r.startswith('glob:')
            a = r[5:] if isg else r
            if not a.startswith(root + os.sep):
                continue
            a = os.path.relpath(a, root)
            if isg and WILD.search(a):
                pats.add(a)
            elif a != rec and a in bl and a != TRACER:
                files.add(a)
        dd = collections.defaultdict(set)
        for f in files:
            dd[os.path.dirname(f)].add(f)
        keep, dirs = set(), set()
        for D, xs in dd.items():
            if len(xs) >= COLLAPSE_MIN and len(xs) >= COLLAPSE_FRAC * len(bydir[D]):
                dirs.add(os.path.join(D, '*') if D else '*')
            else:
                keep |= xs
        # the census receipts read a few files from each of dozens of directories; their read set is "the
        # tree", and writing it out file by file was 60% of the index (r6977+70.1: 20 receipts, 374 KB)
        byte = collections.defaultdict(set)
        for f in keep:
            if os.sep in f:
                byte[(f.split(os.sep)[0], os.path.splitext(f)[1])].add(f)
        for (T, ext), xs in byte.items():
            if len(xs) >= SUBTREE_MIN:
                dirs.add(f'{T}/**/*{ext}')
                keep -= xs
        src_path = os.path.join(root, rec)
        src = open(src_path, errors='replace').read() if os.path.exists(src_path) else ''
        covered = {os.path.basename(f) for f in keep}
        covered |= {os.path.basename(f) for f in files}
        names = sorted(n for n in source_names(src) if n not in covered and n in repo_names)
        recs[rec] = {'sha': bl.get(rec, '')[:12], 's': round(float(d.get('dt') or 0), 1),
                     'r': sorted(keep), 'd': sorted(dirs), 'g': sorted(pats), 'n': names}
    commit = commit or git(root, 'rev-parse', 'HEAD').strip()
    head = {'commit': commit, 'date': git(root, 'log', '-1', '--format=%cI', commit).strip(),
            'tree_digest': _digest(root), 'receipts': len(recs), 'red_under_trace': red,
            'timeouts': sorted(timeouts),
            'how': 'scripts/sweep_runner_reads.py --out DIR, then scripts/receipt_scope.py --emit DIR',
            'max_age_days': MAX_AGE_DAYS}
    with open(out, 'w') as fh:
        fh.write('{"traced_at": ' + json.dumps(head, sort_keys=True) + ',\n "receipts": {\n')
        fh.write(',\n'.join(f'  {json.dumps(k)}: {json.dumps(v, separators=(",", ":"))}'
                            for k, v in sorted(recs.items())))
        fh.write('\n }\n}\n')
    return head, recs


def _digest(root):
    import importlib.util
    spec = importlib.util.spec_from_file_location('rar', os.path.join(root, 'scripts', 'run_all_receipts.py'))
    m = importlib.util.module_from_spec(spec)
    argv, sys.argv = sys.argv, ['x']
    try:
        spec.loader.exec_module(m)
        return m.tree_digest()
    except Exception:                                          # noqa: BLE001  (a seed tree has no runner)
        return ''
    finally:
        sys.argv = argv


def registered(root):
    import importlib.util
    spec = importlib.util.spec_from_file_location('rar', os.path.join(root, 'scripts', 'run_all_receipts.py'))
    m = importlib.util.module_from_spec(spec)
    argv, sys.argv = sys.argv, ['x']
    try:
        spec.loader.exec_module(m)
        return [os.path.relpath(f, root) for f in m.registered()[0]]
    finally:
        sys.argv = argv


# ------------------------------------------------------------------------------------ load
def load(root, path=None, regs=None):
    """the committed index, brought to THIS tree: stale entries widened by their current source, new
    receipts given their static names.  Returns (idx, traced_at, stale, new)."""
    path = path or os.path.join(root, INDEX)
    d = json.load(open(path))
    bl = blobs(root)
    regs = registered(root) if regs is None else regs
    idx, stale, new = {}, [], []
    repo_names = {os.path.basename(t) for t in bl}
    for rec in regs:
        e = d['receipts'].get(rec)
        cur = bl.get(rec, '')
        src = ''
        if e is None or not cur.startswith(e['sha']) or not e['sha']:
            fp = os.path.join(root, rec)
            src = open(fp, errors='replace').read() if os.path.exists(fp) else ''
            (new if e is None else stale).append(rec)
        e = e or {'sha': '', 's': None, 'r': [], 'd': [], 'g': [], 'n': []}
        idx[rec] = {'files': set(e['r']), 'dirs': list(e.get('d', [])), 'pats': list(e['g']),
                    'names': set(e['n']) | ((source_names(src) & repo_names) if src else set()), 's': e['s']}
    return idx, d['traced_at'], stale, new


def age_days(root, traced):
    """days from the traced commit to HEAD, by commit time; None if the traced commit is not here"""
    t = git(root, 'log', '-1', '--format=%ct', traced['commit']).strip()
    h = git(root, 'log', '-1', '--format=%ct', 'HEAD').strip()
    if not t or not h:
        return None
    return (int(h) - int(t)) / 86400


# ------------------------------------------------------------------------------------ scope
def diff(root, rng):
    ns = git(root, 'diff', '--name-status', '-M', rng).split('\n')
    changed, gone, added = set(), set(), set()
    for l in ns:
        f = l.split('\t')
        if len(f) < 2:
            continue
        changed.update(f[1:])
        if f[0].startswith(('D', 'R')):
            gone.add(f[1])
        if f[0].startswith(('A', 'R', 'C')):
            added.add(f[-1])
    return changed, gone, added


def scope(idx, changed, gone, added, which):
    """A read file or a directory read whole is in scope when its CONTENT changed; a glob only when its
    MEMBERSHIP did (a path matching it added, deleted or renamed) -- what a glob returns is a list of names,
    and any file the receipt then opened is a read of its own."""
    listing = gone | added
    # a path added in a NEW subdirectory changes its parent's listing by the subdirectory's name
    for p in list(listing):
        while os.path.dirname(p):
            p = os.path.dirname(p)
            listing.add(p)
    if which == 'tolerance':
        keep = lambda c: not c.endswith(PROSE) or c in idx
        changed, listing = {c for c in changed if keep(c)}, {c for c in listing if keep(c)}
    base = {os.path.basename(c) for c in changed}
    out = set()
    for rec, e in idx.items():
        if rec in changed:
            out.add(rec)
        elif which in ('suite', 'tolerance'):
            if e['files'] & changed or e['names'] & base \
                    or any(pmatch(c, d) for d in e['dirs'] for c in changed) \
                    or any(pmatch(c, g) for g in e['pats'] for c in listing):
                out.add(rec)
        elif which == 'reads':
            if e['files'] & gone or any(pmatch(g_, p) for p in e['pats'] + e['dirs'] for g_ in gone):
                out.add(rec)
    return sorted(out)


def ci_range(root, env=os.environ):
    """the range a CI event asks about.  pull_request: the whole PR against its base (what is about to
    merge).  push: exactly the commits pushed.  workflow_dispatch: its `range` input, if given."""
    ev = env.get('GITHUB_EVENT_NAME', '')
    data = {}
    if env.get('GITHUB_EVENT_PATH') and os.path.exists(env['GITHUB_EVENT_PATH']):
        data = json.load(open(env['GITHUB_EVENT_PATH']))
    if ev == 'pull_request':
        return f"{data['pull_request']['base']['sha']}...{data['pull_request']['head']['sha']}", 'the whole PR'
    if ev == 'workflow_dispatch' and (data.get('inputs') or {}).get('range'):
        return data['inputs']['range'], 'the dispatched range'
    if ev == 'push':
        before, after = data.get('before', ''), env.get('GITHUB_SHA', 'HEAD')
        if before and set(before) != {'0'} and \
                subprocess.run(['git', 'cat-file', '-e', before + '^{commit}'], cwd=root, stderr=subprocess.DEVNULL).returncode == 0:
            return f'{before}..{after}', 'the commits pushed'
        mb = git(root, 'merge-base', 'origin/main', after).strip()
        if mb and mb != git(root, 'rev-parse', after).strip():
            return f'{mb}..{after}', 'a new branch, against its fork point from main'
        return f'{after}~1..{after}', 'one commit (no usable `before`)'
    raise SystemExit(f'receipt_scope --ci: no range for event {ev!r}')


# ------------------------------------------------------------------------------------ replay
def replay(root, n, path=None):
    """scope each of main's last N first-parent pushes, per class, with the committed index -- the
    measurement the cadence rests on, re-derivable rather than quoted"""
    idx, traced, _, _ = load(root, path)
    shas = git(root, 'rev-list', '--first-parent', f'-{n}', 'origin/main').split()
    q = lambda xs, f: sorted(xs)[int(f * (len(xs) - 1))]
    med = sorted(e['s'] or 0 for e in idx.values())[len(idx) // 2]
    print(f'\n  replaying {len(shas)} first-parent pushes to main against the index traced at '
          f'{traced["commit"][:10]}')
    print(f'    {"scope":10} {"receipts per push (median/p90/max)":36} {"compute mean / p90 / max":>26}  pushes with nothing')
    for which in ('suite', 'tolerance', 'reads'):
        sz, cs = [], []
        for s in shas:
            ch, gone, add = diff(root, f'{s}^1..{s}')
            a = scope(idx, ch, gone, add, which)
            sz.append(len(a))
            cs.append(sum(idx[r]['s'] if idx[r]['s'] is not None else med for r in a))
        print(f'    {which:10} {q(sz, .5):>8} / {q(sz, .9):>4} / {max(sz):<4}{"":17} '
              f'{sum(cs) / len(cs):>8.0f} / {q(cs, .9):>5.0f} / {max(cs):>6.0f} s'
              f'  {sum(1 for x in sz if x == 0):>6} / {len(sz)}')
    return 0


# ------------------------------------------------------------------------------------ seed
def seed():
    """Both ways, on a built repository, THROUGH THE REAL TRACER AND THE REAL EMIT (r6977+70.1: the first
    version fed `build_index` a hand-written JSON, so the tracer's glob bug -- every glob recorded under a
    mangled path -- passed it; this one traces, emits, loads and scopes)."""
    import importlib.util
    spec = importlib.util.spec_from_file_location('srr', os.path.join(os.path.dirname(HERE), 'sweep_runner_reads.py'))
    srr = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(srr)
    tmp = tempfile.mkdtemp(prefix='po62_seed_')
    res = {}
    try:
        g = lambda *a: subprocess.run(['git', *a], cwd=tmp, capture_output=True, text=True)
        g('init', '-q')
        g('config', 'user.email', 'seed@x')
        g('config', 'user.name', 'seed')
        for d_ in ('corpus', 'lib', 'receipts/S'):
            os.makedirs(os.path.join(tmp, d_))
        for n, t in (('corpus/read.tex', 'a'), ('corpus/unread.tex', 'b'), ('corpus/globbed_1.tex', 'c'),
                     ('lib/helper.py', 'X = 1\n')):
            open(os.path.join(tmp, n), 'w').write(t)
        open(os.path.join(tmp, 'receipts', 'S', 'R1.py'), 'w').write(
            "import os, sys, glob\nROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))\n"
            "sys.path.insert(0, os.path.join(ROOT, 'lib'))\nimport helper\n"
            "open(os.path.join(ROOT, 'corpus', 'read.tex')).read()\n"
            "glob.glob(os.path.join(ROOT, 'corpus', 'globbed_*.tex'))\n")
        g('add', '-A')
        g('commit', '-qm', 'base')
        rec = 'receipts/S/R1.py'
        trace = os.path.join(tmp, '.trace')
        os.makedirs(trace)
        srr._run(tmp, rec, 60, trace)
        emit(trace, tmp, os.path.join(tmp, '.index.json'))
        idx, _, _, _ = load(tmp, os.path.join(tmp, '.index.json'), regs=[rec])
        for label, act in (
                ('edit a READ file', lambda: open(os.path.join(tmp, 'corpus', 'read.tex'), 'a').write('x')),
                ('edit an IMPORTED module', lambda: open(os.path.join(tmp, 'lib', 'helper.py'), 'a').write('Y = 2\n')),
                ('add a GLOBBED file', lambda: open(os.path.join(tmp, 'corpus', 'globbed_2.tex'), 'w').write('d')),
                ('edit a GLOBBED, unread file', lambda: open(os.path.join(tmp, 'corpus', 'globbed_1.tex'), 'a').write('x')),
                ('edit an UNREAD file', lambda: open(os.path.join(tmp, 'corpus', 'unread.tex'), 'a').write('x')),
                ('delete a GLOBBED file', lambda: os.remove(os.path.join(tmp, 'corpus', 'globbed_1.tex')))):
            head = g('rev-parse', 'HEAD').stdout.strip()
            act()
            g('add', 'corpus', 'lib')
            g('commit', '-qm', label)
            ch, gone, add = diff(tmp, f'{head}..HEAD')
            res[label] = {w: rec in scope(idx, ch, gone, add, w) for w in ('suite', 'tolerance', 'reads')}
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    for k, v in res.items():
        print(f'    {k:26} ' + '  '.join(f'{w}:{v[w]!s:5}' for w in v))
    want = {'edit a READ file': (True, False, False), 'edit an IMPORTED module': (True, True, False),
            'add a GLOBBED file': (True, False, False), 'edit an UNREAD file': (False, False, False),
            'edit a GLOBBED, unread file': (False, False, False),
            'delete a GLOBBED file': (True, False, True)}
    ok = all(tuple(res[k].values()) == w for k, w in want.items())
    print(f'  in scope exactly when it should be, per class: {ok}')
    return 0 if ok else 1


# ------------------------------------------------------------------------------------ main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default=ROOT)
    ap.add_argument('--index', help=f'the index file (default {INDEX})')
    ap.add_argument('--emit', metavar='TRACE_DIR')
    ap.add_argument('--commit', help='with --emit: the commit the trace ran at (default HEAD)')
    ap.add_argument('--range')
    ap.add_argument('--ci', action='store_true')
    ap.add_argument('--scope', default='suite', choices=('suite', 'tolerance', 'reads'))
    ap.add_argument('--list', metavar='OUT', help='write the receipts in scope here, one per line')
    ap.add_argument('--replay', type=int, metavar='N')
    ap.add_argument('--seed', action='store_true')
    a = ap.parse_args()
    root = os.path.abspath(a.root)
    if a.seed:
        print('\n  receipt_scope --seed: is a receipt in scope exactly when a push touches what it reads?\n')
        return seed()
    if a.emit:
        head, recs = emit(a.emit, root, a.index or os.path.join(root, INDEX), a.commit)
        print(f'  emitted {len(recs)} receipt(s) traced at {head["commit"][:10]} '
              f'({head["red_under_trace"]} red, {len(head["timeouts"])} over budget under the trace)')
        return 0
    if a.replay:
        return replay(root, a.replay, a.index)
    if not (a.range or a.ci):
        ap.print_help()
        return 2
    rng, why = (a.range, 'given') if a.range else ci_range(root)
    idx, traced, stale, new = load(root, a.index)
    age = age_days(root, traced)
    print(f'  READ INDEX: traced at {traced["commit"][:10]} ({traced["date"]}), '
          + (f'{age:.1f} day(s) before HEAD' if age is not None else 'a commit NOT in this history')
          + f'; {len(stale)} receipt(s) edited since and {len(new)} added since, scoped on their '
            f'CURRENT source\'s names and imports as well', file=sys.stderr)
    if age is None or age > MAX_AGE_DAYS:
        print(f'  ⛔ THE READ INDEX HAS EXPIRED (limit {MAX_AGE_DAYS} days).  A scope computed from it is a '
              f'map of a tree that has moved on.  Remedy: `sweep_runner_reads.py --out DIR` on the whole '
              f'suite, then `receipt_scope.py --emit DIR`, and commit {INDEX}.', file=sys.stderr)
        return 3
    ch, gone, add = diff(root, rng)
    out = scope(idx, ch, gone, add, a.scope)
    print(f'  RANGE {rng} ({why}): {len(ch)} path(s) changed, {len(gone)} deleted or renamed', file=sys.stderr)
    est = sum(idx[r]['s'] or 0 for r in out)
    print(f'  ⇒ {len(out)} of {len(idx)} registered receipt(s) in the {a.scope.upper()} scope, '
          f'~{est:.0f}s of compute by the index', file=sys.stderr)
    if a.list:
        with open(a.list, 'w') as fh:
            fh.write(''.join(r + '\n' for r in out))
    else:
        print('\n'.join(out))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
