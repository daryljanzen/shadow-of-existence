#!/usr/bin/env python3
r"""S1 -- cc54, found by RUNNING: scripts/queue.py (the work-on-the-table list, r2615) SHADOWS the stdlib
`queue` module, and because `python3 scripts/run_all_receipts.py` puts scripts/ at sys.path[0],
ThreadPoolExecutor's lazy `import queue` crashed the full receipt sweep AND the nightly heavy CI tier with
"module 'queue' has no attribute 'SimpleQueue'". Fixed with a sys.path guard in the runner; this receipt
is the regression check, reproducing the crash and the fix in subprocesses.

** Board lead L-810 (cc54's band); instrument work (informs no vein). The fourth namespace-collision class
the programme has hit -- after row IDs (r2434), receipt filenames (L-510), item numbers (the double-44),
and branches -- now PYTHON MODULE NAMES. Found the only way it could be: by running the sweep, the
capability neither chat line has. **

** THE BUG. ** scripts/queue.py is a legitimate module (imported by regen_teed_up, stamp, table), but its
NAME collides with the standard library's `queue`. `run_all_receipts.py` lives in scripts/ and is invoked
as `python3 scripts/run_all_receipts.py`, which places scripts/ at sys.path[0]. concurrent.futures.thread
does `import queue` and calls `queue.SimpleQueue()`; with scripts/ on the path the LOCAL queue.py wins, it
has no SimpleQueue, and the runner dies before running a single receipt. The nightly heavy CI tier runs the
same command, so it died the same way -- the one gate that runs the camb/pynucastro receipts, silently
down since scripts/queue.py landed.

** THE FIX (in run_all_receipts.py). ** Drop the runner's own directory from sys.path before the executor
imports, so the stdlib `queue` is found. Minimal, local to the runner, and it renames nothing.

** WHAT THIS RECEIPT CHECKS. **
  1. scripts/queue.py exists and does NOT expose SimpleQueue -- i.e. it really is a stdlib shadow.
  2. Reproduce the crash: a subprocess run FROM scripts/ that instantiates ThreadPoolExecutor dies with
     the AttributeError.
  3. The fix works: the same subprocess with the sys.path guard applied first succeeds.
  4. run_all_receipts.py carries the guard.

** WHAT IS NOT CLAIMED, stated for reversal. ** Not that the fix is the ROOT fix -- the root fix is to
rename scripts/queue.py so no module shadows the stdlib (routed to 56, whose file it is, with a
check-no-stdlib-shadow gate proposed). Not that only run_all_receipts is exposed -- any script run from
scripts/ that needs stdlib `queue` (directly or via threading/multiprocessing) is, which is exactly why a
rename plus a gate is the durable answer. This receipt fixes and guards the one that was actually broken.

Written r2670 (cc54, L-810). Asserts against the filesystem and live subprocesses -- never the register.
Stated for reversal.
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SCRIPTS = os.path.join(ROOT, 'scripts')
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def run_from_scripts(code):
    """run a one-liner with scripts/ as cwd (so scripts/ is on sys.path[0])."""
    return subprocess.run([sys.executable, '-c', code], cwd=SCRIPTS,
                          capture_output=True, text=True)


def main():
    print()
    print('  S1 -- does the sweep runner survive scripts/queue.py shadowing stdlib `queue`?')
    print()

    # 1. scripts/queue.py exists and shadows stdlib (no SimpleQueue)
    r = run_from_scripts('import queue; print(hasattr(queue, "SimpleQueue"), queue.__file__)')
    local_has_simplequeue = r.stdout.strip().split()[0] if r.stdout.strip() else 'ERR'
    check('scripts/queue.py exists and SHADOWS stdlib when imported from scripts/ -- it has no '
          f'SimpleQueue (import queue from scripts/ -> hasattr SimpleQueue = {local_has_simplequeue})',
          os.path.exists(os.path.join(SCRIPTS, 'queue.py')) and local_has_simplequeue == 'False')

    # 2. reproduce the crash: ThreadPoolExecutor from scripts/ dies
    crash = run_from_scripts('from concurrent.futures import ThreadPoolExecutor; '
                             'ThreadPoolExecutor(max_workers=2)')
    check('REPRODUCED: instantiating ThreadPoolExecutor from scripts/ crashes with '
          '"module \'queue\' has no attribute \'SimpleQueue\'" -- exactly what killed the sweep and the '
          'heavy CI tier',
          crash.returncode != 0 and 'SimpleQueue' in crash.stderr)

    # 3. the fix works: the same, with the sys.path guard applied first
    guard = ('import os, sys; '
             '_d=os.path.dirname(os.path.abspath("run_all_receipts.py")) or os.getcwd(); '
             'sys.path[:]=[p for p in sys.path if os.path.abspath(p or os.getcwd())!=os.getcwd()]; '
             'from concurrent.futures import ThreadPoolExecutor; '
             'ex=ThreadPoolExecutor(max_workers=2); ex.shutdown(); print("OK")')
    fixed = run_from_scripts(guard)
    check('THE FIX: dropping scripts/ from sys.path before the executor import lets stdlib `queue` win '
          f'and ThreadPoolExecutor works (subprocess prints OK: {fixed.stdout.strip()!r})',
          fixed.returncode == 0 and 'OK' in fixed.stdout)

    # 4. run_all_receipts.py carries the guard
    runner = open(os.path.join(SCRIPTS, 'run_all_receipts.py'), encoding='utf-8').read()
    check('run_all_receipts.py carries the sys.path guard (so the sweep and the nightly heavy tier run '
          'again)',
          'shadows the stdlib' in runner and 'sys.path[:]' in runner
          and 'ThreadPoolExecutor' in runner.split('sys.path[:]')[1])

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: scripts/queue.py shadows stdlib `queue`; it crashed the full sweep and the nightly')
    print('  heavy CI tier (both run `python3 scripts/run_all_receipts.py`). The runner now drops its own')
    print('  directory from sys.path before the executor imports, so the stdlib module wins and both run')
    print('  again. Root fix (rename scripts/queue.py + a no-stdlib-shadow gate) routed to 56. Found by')
    print('  running the sweep -- the fourth namespace-collision class, now Python module names.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
