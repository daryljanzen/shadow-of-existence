"""replay.py -- r7163+70.1 (70) Q2: the PROPOSED predicate against main's selector on main's own recent paper edits.

For each of the last N first-parent commits on origin/main that changed a corpus/*.tex, a detached worktree at
that commit runs both selectors against its parent.  Every receipt the PROPOSED one adds is graded against the
trace (receipts/READ_INDEX.json at that commit): does the trace record it reading a file the commit changed?

  python3 replay.py [N]
"""
import fnmatch
import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
N = int(sys.argv[1]) if len(sys.argv) > 1 else 30


def sh(cwd, *a):
    return subprocess.run(list(a), cwd=cwd, capture_output=True, text=True)


def main():
    commits = sh(ROOT, 'git', 'log', '--first-parent', '--format=%h', '-n', str(N), 'origin/main', '--',
                 'corpus/*.tex').stdout.split()
    wt = tempfile.mkdtemp(prefix='replay_')
    os.rmdir(wt)
    sh(ROOT, 'git', 'worktree', 'add', '--detach', wt, commits[0])
    tot = dict(main=0, prop=0, extra=0, extra_true=0, lost=0)
    rows = []
    seen_any = set()
    lost_all = {}
    try:
        for c in commits:
            sh(wt, 'git', 'checkout', '-q', '--detach', c)
            # BOTH selectors as they stand today, run against that commit's tree and its own READ_INDEX
            shutil.copy(os.path.join(HERE, 'proposed_touched_pin_readers.py'), os.path.join(wt, 'scripts', '_prop.py'))
            shutil.copy(os.path.join(ROOT, 'scripts', '_touched_pin_readers.py'), os.path.join(wt, 'scripts', '_main.py'))
            m = set(sh(wt, sys.executable, 'scripts/_main.py', c + '^').stdout.split())
            p = set(sh(wt, sys.executable, 'scripts/_prop.py', c + '^').stdout.split())
            os.remove(os.path.join(wt, 'scripts', '_prop.py'))
            os.remove(os.path.join(wt, 'scripts', '_main.py'))
            changed = [f for f in sh(wt, 'git', 'diff', '--name-only', c + '^', c, '--', 'corpus/').stdout.split()
                       if f.endswith(('.tex', '.tsv', '.txt'))]
            try:
                idx = json.load(open(os.path.join(wt, 'receipts', 'READ_INDEX.json')))['receipts']
            except (OSError, ValueError):
                idx = {}
            extra = sorted(p - m)
            # graded on OPENED paths only: a `d` superset over corpus/*.py is not a paper read (census.py D-SUPERSET)
            true = [x for x in extra if x in idx and any(f in idx[x].get('r', []) for f in changed)]
            unseen = [x for x in true if x not in seen_any]
            seen_any.update(true)
            lost = sorted(m - p)
            for x in lost:
                lost_all.setdefault(x, []).append(c)
            tot['main'] += len(m); tot['prop'] += len(p); tot['extra'] += len(extra)
            tot['extra_true'] += len(true); tot['lost'] += len(lost)
            rows.append((c, len(changed), len(m), len(p), len(extra), len(true), len(lost), true))
            print(f'  {c}  tex/tsv/txt changed {len(changed):2d}   main {len(m):3d}   PROPOSED {len(p):3d}   '
                  f'+{len(extra):3d} (trace-confirmed readers of a changed file: {len(true):3d})   lost {len(lost)}',
                  flush=True)
        print(f'\n  over {len(commits)} commits: main ran {tot["main"]}, PROPOSED {tot["prop"]}; PROPOSED adds '
              f'{tot["extra"]}, of which {tot["extra_true"]} the trace confirms read a changed file; loses {tot["lost"]}')
        print(f'  per commit: + {tot["extra"] / len(commits):.1f} receipts run, '
              f'{tot["extra_true"] / len(commits):.1f} of them confirmed readers')
        print('\n  the trace-confirmed additions (receipts main would not have run although they read the edited paper):')
        seen = {}
        for c, *_r, true in rows:
            for x in true:
                seen.setdefault(x, []).append(c)
        for x, cs in sorted(seen.items()):
            print(f'    {len(cs):2d}x  {x}')
        print('\n  receipts main ran and PROPOSED did not (each read by hand below the log):')
        for x, cs in sorted(lost_all.items()):
            print(f'    {len(cs):2d}x  {x}')
    finally:
        sh(ROOT, 'git', 'worktree', 'remove', '--force', wt)
        shutil.rmtree(wt, ignore_errors=True)


if __name__ == '__main__':
    main()
