#!/usr/bin/env python3
"""gate_sweep.py -- RUN EVERY CORPUS GATE AND SAY WHICH ARE RED.  One command, one verdict.

** ⛔⛭⛭ WHY THIS EXISTS, AND IT IS NOT A CONVENIENCE. **  *The sweep was a shell one-liner:*

      `python3 corpus/make_all_appendices.py && for g in ...; do ...; done; echo "gates green"`

  ⇒ *** THE `&&` BINDS THE GENERATOR TO THE LOOP AND THE `echo` IS A SEPARATE COMMAND.  When the
      generator failed, the loop was SKIPPED and "gates green" printed anyway. ***
  ⇒ ** r3152 was committed with `check_appendix_current` RED, and the sweep that would have caught it
    reported a pass it had not measured. **  *Reproduced: `false && for g in a b; do echo ran; done;
    echo "gates green"` prints `gates green` and nothing else.*

  ⌗ *** A SUCCESS MESSAGE PRINTED BY A DIFFERENT COMMAND THAN THE ONE IT DESCRIBES IS NOT A RESULT.
      It is the shell's sequencing, and it will say "green" for work that never ran. ***

** WHAT IT DOES. **  Runs `corpus/make_all_appendices.py` (unless `--no-regen`), then every
`corpus/check_*.py`, and reports each one's exit code.  ** The verdict is computed from the runs and
the process exits non-zero if any gate is red or could not be run. **  *There is no path through this
file on which a pass is printed without a measurement behind it.*

  ⌷ ** `NODE` is set to `ci` for the sweep ** -- `check_claims` refuses to guess a node, and a sweep
    that skipped it would be a sweep with a silent hole.
  ⌷ ** A gate that TIMES OUT is RED, not skipped. **  *An instrument that could not finish has not
    said the tree is clean.*

    python3 scripts/gate_sweep.py
    python3 scripts/gate_sweep.py --no-regen        # skip the appendix regeneration
    python3 scripts/gate_sweep.py --only receipts   # substring filter on the gate name

Written r3154 (`L-267`).  Stated for reversal.
"""
import glob
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
TIMEOUT = 900


def run(path, env):
    t0 = time.time()
    try:
        r = subprocess.run([sys.executable, path], cwd=ROOT, capture_output=True, text=True,
                           errors='replace', timeout=TIMEOUT, env=env)
        return r.returncode, time.time() - t0, (r.stdout + r.stderr)
    except subprocess.TimeoutExpired:
        return 'TIMEOUT', time.time() - t0, ''
    except OSError as e:
        return f'{e.__class__.__name__}', time.time() - t0, str(e)


def main():
    only = None
    if '--only' in sys.argv:
        only = sys.argv[sys.argv.index('--only') + 1]
    env = {**os.environ, 'NODE': os.environ.get('NODE', 'ci')}

    print()
    print('  gate_sweep -- every corpus gate, run, with the verdict computed from the runs')
    print()
    red, ran = [], 0

    if '--no-regen' not in sys.argv:
        rc, dt, out = run(os.path.join(ROOT, 'corpus', 'make_all_appendices.py'), env)
        ran += 1
        print(f'    {"make_all_appendices":38s} {str(rc):>8}  {dt:5.1f}s')
        if rc != 0:
            red.append(('make_all_appendices', rc))
            # ** the failure that started this: print WHY, here, rather than leaving it to a rerun **
            for ln in out.split('\n'):
                if 'FAIL' in ln or 'no _UNI translation' in ln:
                    print(f'        {ln.strip()[:150]}')

    gates = sorted(glob.glob(os.path.join(ROOT, 'corpus', 'check_*.py')))
    for g in gates:
        name = os.path.basename(g)[:-3]
        if only and only not in name:
            continue
        rc, dt, out = run(g, env)
        ran += 1
        if rc != 0:
            red.append((name, rc))
            print(f'    {name:38s} {str(rc):>8}  {dt:5.1f}s   ⛔ RED')

    print()
    print(f'    {ran} instrument(s) run, {len(red)} red')
    if red:
        for name, rc in red:
            print(f'      ⛔ {name} exited {rc}')
        print()
        print('    ⌗ ** A gate that TIMED OUT counts as RED. **  *An instrument that could not finish')
        print('      has not said the tree is clean.*')
        print()
        return 1
    print('    every gate green -- and this line is printed by the same run that measured them.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
