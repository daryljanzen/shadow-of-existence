#!/usr/bin/env python3
"""r7419+70 ②: is the Lean project at REF under a GREEN formalisation workflow?

The tree half is local and exact: a run at commit H covers REF's project iff `git diff H REF -- <the workflow's
paths:>` is empty, because a path-scoped workflow's verdict is a function of exactly those paths.  The verdict half,
the run's conclusion, exists only in the Actions API: no committed file records it (r7419+70 G-b).
    python3 -I green_under.py [REF]          (needs `gh api`; offline it says so instead of guessing)
"""
import json, subprocess, sys
REPO = 'daryljanzen/shadow-of-existence'
WF = {'formalisation-mathlib.yml': ['computations/formalisation/lean'],
      'formalisation-physlib.yml': ['computations/formalisation/lean-physlib',
                                    'computations/formalisation/lean/check_no_sorry.py']}
ref = sys.argv[1] if len(sys.argv) > 1 else 'HEAD'
git = lambda *a: subprocess.run(['git', *a], capture_output=True, text=True)
head = git('rev-parse', ref).stdout.strip()
for wf, paths in WF.items():
    r = subprocess.run(['gh', 'api', f'repos/{REPO}/actions/workflows/{wf}/runs?status=completed&per_page=100'],
                       capture_output=True, text=True)
    if r.returncode:
        print(f'{wf}: UNANSWERABLE here -- the verdict lives only in the Actions API and it is not reachable '
              f'({r.stderr.strip()[:80]})'); continue
    runs = json.loads(r.stdout)['workflow_runs']
    hit = None
    for run in runs:                                   # newest first
        h = run['head_sha']
        if git('cat-file', '-e', h + '^{commit}').returncode:
            continue                                   # a run on a commit this clone does not have
        if git('diff', '--quiet', h, head, '--', *paths).returncode == 0:
            hit = run; break
    if hit is None:
        print(f'{wf}: NO completed run in the last {len(runs)} covers {head[:9]}\'s tree under {paths}')
    else:
        print(f'{wf}: {hit["conclusion"].upper()} -- run {hit["id"]} at {hit["head_sha"][:9]} ({hit["event"]}, '
              f'{hit["created_at"]}) has an identical tree under {paths}')
