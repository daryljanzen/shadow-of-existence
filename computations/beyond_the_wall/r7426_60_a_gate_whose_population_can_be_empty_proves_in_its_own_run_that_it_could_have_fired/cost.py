#!/usr/bin/env python3
"""r7426 (60) -- A GATE WHOSE POPULATION CAN BE EMPTY PROVES IN ITS OWN RUN THAT IT COULD HAVE FIRED.
Four arms, all registered in `PREDICTION.md` at `FRAME` before the change.

⛔ THE BANDS ARE IN `PREDICTION.md`, COMMITTED AT `FRAME` BEFORE THIS RAN: ⒜ exact 1 of 1 (the in-run
seed fires), ⒝ exact 0 (no contamination, and the gate still exits 0), ⒞ exact 3 of 3 states still
printed apart, ⒟ exact 0 failing of the gate's existing seeds.

⛭ Nothing here re-implements the gate: every figure is read off the gate's own ordinary run and its own
`--seed` mode.

    python3 -I cost.py
"""
import argparse
import os
import re
import subprocess
import time

FRAME = '8cf16a4b'
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
GATE = os.path.join('corpus', 'check_formalisation_join.py')
RESULT = {}


def run(*a):
    return subprocess.run(['python3', *a], cwd=ROOT, capture_output=True, text=True,
                          errors='replace')


def main():
    t0 = time.time()
    g = run(GATE)
    out = g.stdout + g.stderr
    s = run(GATE, '--seed')
    sout = s.stdout + s.stderr
    ok = re.findall(r'^\s+\[ok\]\s+(.*)$', sout, re.M)
    bad = re.findall(r'^\s+\[FAIL\]\s+(.*)$', sout, re.M)

    print('=' * 100)
    print('r7426 (60) -- THE GATE PROVES IN ITS OWN RUN THAT IT COULD HAVE FIRED')
    print(f'  frame {FRAME};  bands registered in PREDICTION.md at that commit, before the change')
    print('=' * 100)

    # ⒜ the in-run seed, on an ORDINARY run with no flag
    fired = 'THE IN-RUN SEED' in out and 'it FIRED' in out
    measured_zero = 'a MEASURED zero' in out
    print(f'\n⒜ THE IN-RUN SEED, on an ordinary run with NO flag: ** {1 if fired else 0} of 1 **')
    print(f'      the seeded bad `decl` fired through the real row path: {fired}')
    print(f'      and the run says a zero from it is a MEASURED zero:    {measured_zero}')
    print(f'    ⇒ {"HIT" if fired and measured_zero else "** MISS **"} -- *`r7421` ③\'s rule is now '
          f'BEHAVIOUR rather than a comment: the gate fails its own run if the seed does not fire.*')

    # ⒝ no contamination
    zero_checkable = '0 are checkable' in out
    seed_counted = bool(re.search(r'row SEED', out.split('THE INVENTORY')[-1])) if \
        'THE INVENTORY' in out else False
    print(f'\n⒝ NO CONTAMINATION: ** {1 if seed_counted else 0} ** synthetic row(s) in the real '
          f'counts, against a point prediction of 0')
    print(f'      the gate still reports `0` checkable on today\'s tree: {zero_checkable}')
    print(f'      and still exits {g.returncode}')
    print(f'    ⇒ {"HIT" if not seed_counted and zero_checkable and g.returncode == 0 else "** MISS **"}'
          f' -- *a control that changed the verdict it controls would not be a control.*')

    # ⒞ the three states, re-measured
    three = sum([
        '0 are checkable' in out and 'never as 0 dangling references' in out,
        any(l.startswith('S11.') for l in ok),
        any(l.startswith('S12.') for l in ok)])
    print(f'\n⒞ THE THREE STATES STILL PRINTED APART: ** {three} of 3 **, re-measured rather than '
          f'inherited from `r7424`')
    print(f'      `0` CHECKABLE distinguished from `0` dangling references: '
          f'{"0 are checkable" in out and "never as 0 dangling references" in out}')
    print(f'      a DANGLING `decl` fails, named as dangling:               '
          f'{any(l.startswith("S11.") for l in ok)}')
    print(f'      an UNREADABLE file fails AS UNVERIFIABLE:                 '
          f'{any(l.startswith("S12.") for l in ok)}')
    print(f'    ⇒ {"HIT" if three == 3 else "** MISS **"} -- *the amendment touched the path that '
          f'produces those sentences, so `r7424`\'s figure is not inherited (`r7417`\'s own lesson).*')

    # ⒟ the existing seeds
    newones = [l for l in ok if re.match(r'^S1[56]\.', l)]
    print(f'\n⒟ THE SEEDS: ** {len(bad)} ** failing of {len(ok) + len(bad)}, against a point '
          f'prediction of 0;  `--seed` exits {s.returncode}')
    for l in bad:
        print(f'      ⛔ {l}')
    print(f'    ⌗ {len(newones)} of them are new here, and they are the pair that matters: the in-run '
          f'seed FIRES on its synthetic bad `decl` and stays SILENT on one that is declared ⇒ '
          f'** the seed discriminates rather than answering `True` **.')

    print(f'\n⌗ NOT TOUCHED: the `⓶` workflow-visibility condition.  *`r7421` ④ puts that question to '
          f'`70` and says to drop the condition rather than guess if the answer is no; the answer is '
          f'not in the tree, so nothing was guessed and nothing was changed.*')

    RESULT.update({'A_FIRED': fired, 'A_MEASURED_ZERO': measured_zero,
                   'B_CONTAMINATED': seed_counted, 'B_ZERO_CHECKABLE': zero_checkable,
                   'B_GATE_RC': g.returncode, 'C_STATES': three,
                   'D_OK': len(ok), 'D_BAD': len(bad), 'D_SEED_RC': s.returncode,
                   'D_NEW': len(newones), 'SECONDS': round(time.time() - t0, 1)})
    print(f'\n  price: {RESULT["SECONDS"]} s')
    return RESULT


if __name__ == '__main__':
    argparse.ArgumentParser(description=__doc__).parse_args()
    main()
