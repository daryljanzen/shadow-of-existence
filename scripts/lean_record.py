#!/usr/bin/env python3
"""lean_record.py -- IS THIS TREE'S LEAN PROJECT UNDER A GREEN WORKFLOW, ANSWERED FROM A REF.  r7423 ③ (66), built r7423+70.

** WHY.  **  r7419+70.2 measured that "is this Lean file under a GREEN `formalisation-*` workflow" cannot be answered
from the tree (no committed file records a run's conclusion) and is answerable exactly only through the Actions API.
r7423 ③ authorised the record that makes it local: the `refs/ci/nightly` / `refs/ci/carry` idiom (PO-65).

** THE EXACT QUESTION IS NOT "THE RUN AT HEAD".  **  Both workflows are path-scoped, so most commits have no run.  A
run at commit H covers REF iff every path in the workflow's `push: paths:` resolves to the same object at H and at
REF -- the verdict is a function of exactly those paths.  So a record carries that PATHS KEY, and the reader compares
keys, never commits.  ** A record is a claim about the tree at the moment it was pushed (66, r7423 ③): a record whose
key no longer matches is STALE and can never read GREEN. **

** THE RECORD.  **  `refs/ci/lean/<workflow-file-stem>`: a chain of commits, newest first, each holding `RECORD`:
    head <sha> / key <path=oid;...> / conclusion <success|failure|cancelled> / run <id> / event push
Only `push` runs write (a `pull_request` run builds the MERGE ref but reports the PR head -- r7419+70.2's stated
limit).  A write is a fast-forward push of the ref, retried on a race; a token push triggers no CI.

** THE READER.  **  Three results and only one passes (r7419+70.2, adopted r7423 ②):
    GREEN          the newest non-cancelled record whose key equals REF's says success
    NOT-GREEN      ... says anything else
    UNANSWERABLE   the ref cannot be fetched, or no record's key equals REF's (stale, or not yet run)
A `cancelled` record is not a verdict and is skipped.

    python3 scripts/lean_record.py --status [--workflow W] [--ref REF] [--chain LOCALREF --no-fetch]
    python3 scripts/lean_record.py --write W --conclusion C --run ID --event E      # CI only
"""
import argparse
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
WORKFLOWS = ('formalisation-mathlib', 'formalisation-physlib')
GREEN, NOT_GREEN, UNANSWERABLE = 'GREEN', 'NOT-GREEN', 'UNANSWERABLE'


def git(*a, check=False, inp=None):
    return subprocess.run(['git', '-C', ROOT, *a], capture_output=True, text=True, check=check, input=inp)


def ref_name(wf):
    return f'refs/ci/lean/{wf}'


def push_paths(wf, at='HEAD'):
    """the workflow's own `on: push: paths:`, read from the workflow file AT `at` -- never a copy of it"""
    src = git('show', f'{at}:.github/workflows/{wf}.yml').stdout
    m = re.search(r'^  push:\n    paths:\n((?:      - .*\n)+)', src, re.M)
    if not m:
        return []
    out = []
    for ln in m.group(1).splitlines():
        p = ln.strip()[2:].strip().strip('\'"')
        out.append(p[:-3] if p.endswith('/**') else p)
    return out


def paths_key(wf, at='HEAD'):
    parts = []
    for p in push_paths(wf, at):
        r = git('rev-parse', '--verify', '--quiet', f'{at}:{p}')
        parts.append(f'{p}={r.stdout.strip() if r.returncode == 0 else "absent"}')
    return ';'.join(parts)


def parse(text):
    rec = {}
    for ln in text.splitlines():
        if ' ' in ln:
            k, v = ln.split(' ', 1)
            rec[k] = v.strip()
    return rec


def status(wf, at='HEAD', chain=None, fetch=True):
    """(GREEN | NOT-GREEN | UNANSWERABLE, why)"""
    local = chain or f'refs/ci-read/lean/{wf}'
    if fetch:
        r = git('fetch', '--quiet', 'origin', f'+{ref_name(wf)}:{local}')
        if r.returncode:
            return UNANSWERABLE, f'{ref_name(wf)} could not be fetched ({(r.stderr.strip() or "no such ref")[:80]})'
    if git('rev-parse', '--verify', '--quiet', local).returncode:
        return UNANSWERABLE, f'no record chain at {local}'
    want = paths_key(wf, at)
    seen = 0
    for c in git('rev-list', local).stdout.split():
        seen += 1
        rec = parse(git('show', f'{c}:RECORD').stdout)
        if rec.get('key') != want:
            continue
        if rec.get('conclusion') == 'cancelled':
            continue
        verdict = GREEN if rec.get('conclusion') == 'success' else NOT_GREEN
        return verdict, (f'record {c[:9]}: run {rec.get("run")} at {rec.get("head", "")[:9]} -- '
                         f'{rec.get("conclusion")} on an identical tree under {push_paths(wf, at)}')
    return UNANSWERABLE, f'none of {seen} record(s) has this tree\'s paths key (stale, or this tree is not yet run)'


def write(wf, conclusion, run, event):
    if event != 'push':
        print(f'  {event} run: no record written -- only push runs write (the merge-ref limit)')
        return 0
    # r7433 ① (66), built r7433+70: a stale RE-RUN declines, visibly -- the same guard as gates.yml's record steps
    import rerun_guard
    ok, line = rerun_guard.verdict()
    print(f'  {line}')
    if not ok:
        return 0
    head = git('rev-parse', 'HEAD', check=True).stdout.strip()
    body = (f'head {head}\nkey {paths_key(wf)}\nconclusion {conclusion}\nrun {run}\nevent {event}\n')
    for attempt in range(5):
        r = git('fetch', '--quiet', 'origin', f'+{ref_name(wf)}:refs/ci-tip/{wf}')
        parent = git('rev-parse', '--verify', '--quiet', f'refs/ci-tip/{wf}').stdout.strip() if r.returncode == 0 else ''
        blob = git('hash-object', '-w', '--stdin', inp=body, check=True).stdout.strip()
        tree = git('mktree', inp=f'100644 blob {blob}\tRECORD\n', check=True).stdout.strip()
        args = ['commit-tree', tree, '-m', f'{wf} run {run} at {head[:9]}: {conclusion}']
        if parent:
            args[2:2] = ['-p', parent]
        commit = git(*args, check=True).stdout.strip()
        p = git('push', 'origin', f'{commit}:{ref_name(wf)}')
        if p.returncode == 0:
            print(f'  recorded {conclusion} for {head[:9]} on {ref_name(wf)} ({commit[:9]})')
            print(f'  read it with:  python3 scripts/lean_record.py --status --workflow {wf}')
            return 0
        print(f'  push refused (attempt {attempt + 1}): another writer moved the ref; re-reading')
    print('  ⛔ the record could not be written after 5 attempts')
    return 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--status', action='store_true')
    ap.add_argument('--workflow', choices=WORKFLOWS)
    ap.add_argument('--ref', default='HEAD')
    ap.add_argument('--chain', help='read this local ref instead of fetching (probes)')
    ap.add_argument('--no-fetch', action='store_true')
    ap.add_argument('--write', choices=WORKFLOWS)
    ap.add_argument('--conclusion')
    ap.add_argument('--run', default='')
    ap.add_argument('--event', default='')
    a = ap.parse_args()
    if a.write:
        return write(a.write, a.conclusion, a.run, a.event)
    for wf in ([a.workflow] if a.workflow else WORKFLOWS):
        v, why = status(wf, a.ref, a.chain, not a.no_fetch)
        print(f'  {wf}: {v} -- {why}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
