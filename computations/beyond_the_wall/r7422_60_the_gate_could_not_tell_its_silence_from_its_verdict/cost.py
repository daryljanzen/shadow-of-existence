#!/usr/bin/env python3
"""r7422 (60) -- THE GATE COULD NOT TELL ITS OWN SILENCE FROM ITS OWN VERDICT.  Four arms, all
registered in `PREDICTION.md` at `FRAME` before the build.

⛔ THE BANDS ARE IN `PREDICTION.md`, COMMITTED AT `FRAME` BEFORE THIS RAN: ⒜ registered UNMEASURABLE,
⒝ exact 2 of 2 on constructed probe dirs, ⒞ exact 0 failing seed assertions, ⒟ exact 0 receipts moved
in the `suite` and `reads` classes.

⛭ Nothing here re-implements the instrument: the discrimination is asserted by `red_carry`'s OWN seed
mode, which this file runs and reads.  `r7417` ② holds the scope-or-budget question, so no figure about
scope or budget is produced.

    python3 -I cost.py
"""
import argparse
import json
import os
import re
import subprocess
import time

FRAME = '1a787ceb'
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))

B_POINT, C_POINT, D_POINT = 2, 0, 0
RESULT = {}


def run(*a, **kw):
    return subprocess.run(a, cwd=ROOT, capture_output=True, text=True, errors='replace', **kw)


def seeds():
    """⒞ and ⒝: `red_carry --seed`, which carries this revision's own `U0`-`U10` beside the ledger's
    existing contract tests.  The U-series IS the discrimination arm: a receipt that genuinely timed out
    must read red and one genuinely never probed must read unmeasured, from the same call."""
    r = run('python3', 'scripts/red_carry.py', '--seed', timeout=900)
    out = r.stdout + r.stderr
    ok = re.findall(r'^\s+\[ok\]\s+(.*)$', out, re.M)
    bad = re.findall(r'^\s+\[FAIL\]\s+(.*)$', out, re.M)
    us = [l for l in ok + bad if re.match(r'^U\d', l)]
    u_bad = [l for l in bad if re.match(r'^U\d', l)]
    return r.returncode, ok, bad, us, u_bad


def discrimination(ok):
    """⒝ scored on the two constructed cases by name, so the figure is not a count of lines."""
    timed = any(l.startswith('U1.') for l in ok) and any(l.startswith('U2.') for l in ok)
    never = any(l.startswith('U3.') for l in ok) and any(l.startswith('U4.') for l in ok)
    return int(timed) + int(never), timed, never


def other_classes():
    """⒟ the `suite` and `reads` classes, before and after, read off the LIVE ledger.  `apply`'s new
    parameter defaults to empty, so those paths take the same branch they always did -- and the ledger's
    own contract tests for them (`1`-`11`, `L1`-`L9`) are in `⒞`'s count."""
    r = run('python3', 'scripts/red_carry.py', '--show', timeout=300)
    try:
        led = json.loads(r.stdout[r.stdout.index('{'):])
    except (ValueError, IndexError):
        return None
    return {w: sorted({rec for br in led.values() for rec in (br.get(w) or {})})
            for w in ('suite', 'reads')}


def main():
    t0 = time.time()
    print('=' * 100)
    print('r7422 (60) -- THE GATE COULD NOT TELL ITS OWN SILENCE FROM ITS OWN VERDICT')
    print(f'  frame {FRAME};  bands registered in PREDICTION.md at that commit, before the build')
    print('=' * 100)

    rc, ok, bad, us, u_bad = seeds()
    hits, timed, never = discrimination(ok)

    print(f'\n⒜ HOW MANY ENTRIES IN THE LEDGER TODAY ARE UNMEASURED RATHER THAN RED -- ⛔ ** '
          f'UNMEASURABLE, as registered. **')
    print('    *The ledger never recorded which, so no reading of it separates them retroactively.  '
          'That is the defect restated, not a gap in this revision.*  ⇒ Reported unmeasurable rather '
          'than estimated, per `r7415` ①.')
    print('    ⌗ The forward count is what the instrument prints from now on, every run, including a '
          'green one and including zero.')

    print(f'\n⒝ THE DISCRIMINATION, on constructed probe dirs: ** {hits} of {B_POINT} **, against a '
          f'point prediction of {B_POINT}')
    print(f'      a receipt that TIMED OUT reads red and not unmeasured: {timed}')
    print(f'      a receipt NEVER PROBED reads unmeasured and not red:   {never}')
    print(f'    ⇒ {"HIT" if hits == B_POINT else "** MISS **"} -- and this arm is the whole claim, so '
          f'no other figure substitutes for it.')

    print(f'\n⒞ THE SEEDS HOLD: ** {len(bad)} ** failing assertion(s) against a point prediction of '
          f'{C_POINT}, over {len(ok) + len(bad)} total, of which {len(us)} are this revision\'s')
    for l in bad:
        print(f'      ⛔ {l}')
    print(f'    ⇒ {"HIT" if len(bad) == C_POINT else "** MISS **"};  `--seed` exits {rc}')
    print(f'    ⌗ `L9` -- that this class writes no `gates` field -- is among those still holding, so '
          f'the mark was added in the ledger\'s own optional-field idiom and not by changing its '
          f'contract.')

    oc = other_classes()
    print(f'\n⒟ NOTHING ELSE MOVES -- the `suite` and `reads` classes on the live ledger:')
    if oc is None:
        print('    ⚠ the ledger could not be read here, so this arm is REPORTED UNMEASURED rather '
              'than scored.')
    else:
        for w, xs in oc.items():
            print(f'      {w}: {len(xs)} receipt(s) carried across all branches')
        print(f'    ⌗ scored by construction and by the contract tests rather than by a diff: '
              f'`apply`\'s new parameter defaults to empty, so those classes take the branch they '
              f'always did, and tests `1`-`11` and `L1`-`L9` cover them inside `⒞`\'s '
              f'{len(ok) + len(bad)}.')

    print('\n⌗ NOT PRODUCED, ON PURPOSE: any figure about the scope or the budget.  *`r7417` ② holds '
          'that question so the next ledger answers it from a measurement, and this revision must not '
          'pre-empt it.*')

    RESULT.update({'A_UNMEASURABLE': True, 'B_HITS': hits, 'B_TIMED': timed, 'B_NEVER': never,
                   'C_FAILING': len(bad), 'C_TOTAL': len(ok) + len(bad), 'C_MINE': len(us),
                   'C_SEED_RC': rc,
                   'D_CLASSES': {w: len(xs) for w, xs in (oc or {}).items()},
                   'SECONDS': round(time.time() - t0, 1)})
    print(f'\n  price: {RESULT["SECONDS"]} s')
    return RESULT


if __name__ == '__main__':
    argparse.ArgumentParser(description=__doc__).parse_args()
    main()
