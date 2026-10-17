#!/usr/bin/env python3
"""r7433+70 B-a / B-b: the guard's four cases through rerun_guard.verdict itself, the step wrapper's exit handling
through bash, and the concurrency key's logic as the expression states it."""
import os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import rerun_guard as G  # noqa: E402
SHA, OTHER = 'a' * 40, 'b' * 40
base = dict(GITHUB_SHA=SHA, GITHUB_REF_NAME='br', GITHUB_REPOSITORY='o/r')
cases = [('attempt 1 (tip moved)', dict(base, GITHUB_RUN_ATTEMPT='1'), lambda e: OTHER, True, 'RECORDING'),
         ('attempt 2 at the tip', dict(base, GITHUB_RUN_ATTEMPT='2'), lambda e: SHA, True, 'RECORDING'),
         ('attempt 2 off the tip', dict(base, GITHUB_RUN_ATTEMPT='2'), lambda e: OTHER, False, 'STALE RE-RUN, DECLINED'),
         ('attempt 2, tip unreadable', dict(base, GITHUB_RUN_ATTEMPT='2'), lambda e: '', False, 'could not be read -- DECLINED')]
bad = 0
for name, env, tip, want_ok, want_text in cases:
    ok, line = G.verdict(env, tip)
    good = ok == want_ok and want_text in line and line.startswith('RERUN-GUARD:')
    bad += not good
    print(f'  {"OK  " if good else "FAIL"} B-a {name:26} -> {"record" if ok else "decline"}: {line}')
# the step wrapper, exactly as gates.yml writes it, with the guard's exit code forced
for code, want in ((0, 'RECORDED'), (10, 'nothing'), (1, 'RECORDED')):
    sh = (f'set -e; rc=0; (exit {code}) || rc=$?; [ "$rc" = 10 ] && exit 0; echo RECORDED')
    out = subprocess.run(['bash', '-c', sh], capture_output=True, text=True)
    got = out.stdout.strip() or 'nothing'
    good = got == want and out.returncode == 0
    bad += not good
    print(f'  {"OK  " if good else "FAIL"} B-a wrapper: guard exits {code:>2} -> {got} (step exit {out.returncode})'
          + ('   <- a crashed guard still records' if code == 1 else ''))
# the key, as the expression's && / || logic
def key(attempt, ref, run_id=7):
    return (attempt > 1 and f'gates-rerun-{run_id}') or (ref == 'refs/heads/main' and f'gates-main-{run_id}') \
        or f'gates-{ref}'
old = lambda ref, run_id=7: (ref == 'refs/heads/main' and f'gates-main-{run_id}') or f'gates-{ref}'
for a, ref in ((1, 'refs/heads/main'), (1, 'refs/heads/x'), (2, 'refs/heads/main'), (2, 'refs/heads/x')):
    want = old(ref) if a == 1 else 'gates-rerun-7'
    good = key(a, ref) == want
    bad += not good
    print(f'  {"OK  " if good else "FAIL"} B-b attempt {a} on {ref:16} -> {key(a, ref)}'
          + ('   (unchanged from today)' if a == 1 else ''))
print(f'  {"all" if not bad else bad} {"as predicted" if not bad else "FAILED"}')
sys.exit(1 if bad else 0)
