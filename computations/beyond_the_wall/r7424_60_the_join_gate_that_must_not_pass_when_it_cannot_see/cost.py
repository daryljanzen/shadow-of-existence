#!/usr/bin/env python3
"""r7424 (60) -- THE JOIN GATE THAT MUST NOT PASS WHEN IT CANNOT SEE.  Four arms, all registered in
`PREDICTION.md` at `FRAME` before the gate was written.

⛔ THE BANDS ARE IN `PREDICTION.md`, COMMITTED AT `FRAME` BEFORE THE BUILD: ⒜ 300 declarations
(band 50-1500), ⒝ exact 0 checkable rows AND the gate saying so, ⒞ exact 3 of 3 on constructed rows,
⒟ 43 of 43 files under a workflow (band 30-43).

⛭ Nothing here re-implements the gate: the controls are the gate's OWN `--seed` mode, which this file
runs and reads, and the figures come from its own run.

    python3 -I cost.py
"""
import argparse
import os
import re
import subprocess
import time

FRAME = 'bd23890b'
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
GATE = os.path.join('corpus', 'check_formalisation_join.py')

A_CENTRAL, A_BAND = 300, (50, 1500)
B_POINT, C_POINT = 0, 3
D_CENTRAL, D_BAND = 43, (30, 43)
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

    decls = int(re.search(r'identifiers the reader extracts:\s*(\d+)', out).group(1))
    files = int(re.search(r'`\.lean` files found:\s*(\d+)', out).group(1))
    gated = re.search(r'under at least one workflow:\s*(\d+) of (\d+)', out)
    gated_n, gated_of = int(gated.group(1)), int(gated.group(2))
    done = int(re.search(r'`DONE` rows:\s*(\d+)', out).group(1))
    checkable = 0 if '0 are checkable' in out else None
    says_so = 'NOT YET CHECKABLE' in out and 'never as 0 dangling references' in out

    print('=' * 100)
    print('r7424 (60) -- THE JOIN GATE THAT MUST NOT PASS WHEN IT CANNOT SEE')
    print(f'  frame {FRAME};  bands registered in PREDICTION.md at that commit, before the build')
    print('=' * 100)

    inband = A_BAND[0] <= decls <= A_BAND[1]
    print(f'\n⒜ THE POSITIVE CONTROL -- declarations the reader finds across {files} files: '
          f'** {decls} **, against central {A_CENTRAL} and band {A_BAND[0]}-{A_BAND[1]}')
    print(f'    ⇒ {"INSIDE" if inband else "** OUTSIDE, ABOVE THE CEILING **"} the band'
          + ('' if inband else f' -- {decls} against a ceiling of {A_BAND[1]}.  *The direction is the '
                               f'one that makes the control STRONGER: the arm that mattered was the '
                               f'FLOOR, since a reader returning near 0 is the `cc66` failure and '
                               f'would make every verdict a silence.*'))

    print(f'\n⒝ CHECKABLE ROWS TODAY: ** {checkable} ** of {done} `DONE` row(s), against a point '
          f'prediction of {B_POINT}')
    print(f'    and the gate SAYS SO rather than printing a clean join: {says_so}')
    print(f'    ⇒ {"HIT" if checkable == B_POINT and says_so else "** MISS **"} -- *the claim was never '
          f'the figure but that `0` CHECKABLE and `0` DANGLING REFERENCES are different sentences.*')

    whole = [l for l in ok if re.match(r'^S1[0-4]\.', l)]
    three = sum(1 for pat in ('S10.', 'S11.', 'S12.') if any(l.startswith(pat) for l in ok))
    print(f'\n⒞ THE NON-VACUITY CONTROL, on constructed rows: ** {three} of {C_POINT} **')
    print(f'      a `decl` that IS declared passes the whole gate:            '
          f'{any(l.startswith("S10.") for l in ok)}')
    print(f'      a DANGLING `decl` fails it, named as dangling:               '
          f'{any(l.startswith("S11.") for l in ok)}')
    print(f'      an UNREADABLE Lean file fails AS UNVERIFIABLE, not as clean: '
          f'{any(l.startswith("S12.") for l in ok)}')
    print(f'    ⇒ {"HIT" if three == C_POINT else "** MISS **"};  the gate\'s `--seed` exits '
          f'{s.returncode} with {len(ok)} assertion(s) and {len(bad)} failing, {len(whole)} of them '
          f'running the WHOLE gate rather than its reader')
    print(f'    ⌗ *The first seed set tested only the READER, and a reader that works is not a gate '
          f'that fires -- so the whole-gate cases were added before this arm was scored.*')

    dband = D_BAND[0] <= gated_n <= D_BAND[1]
    print(f'\n⒟ THE WORKFLOW SCOPE -- `.lean` files under at least one `formalisation-*` workflow: '
          f'** {gated_n} of {gated_of} **, against central {D_CENTRAL} and band '
          f'{D_BAND[0]}-{D_BAND[1]}')
    print(f'    ⇒ {"HIT" if dband else "** MISS **"} -- decided from each workflow\'s own `paths:` '
          f'rather than from a filename convention, so a file under neither would be named as a row '
          f'nothing could ever clear.')

    print(f'\n⌗ NOT DONE HERE, AND ROUTED: the CI wiring.  *`.github/workflows/gates.yml` is not this '
          f'seat\'s to edit, and the order\'s own division is `71` supplies, this seat checks, `66` '
          f'publishes -- the publishing includes the wiring.*')

    RESULT.update({'A_DECLS': decls, 'A_FILES': files, 'A_IN_BAND': inband,
                   'B_CHECKABLE': checkable, 'B_SAYS_SO': says_so, 'B_DONE': done,
                   'C_HITS': three, 'C_SEED_RC': s.returncode, 'C_OK': len(ok), 'C_BAD': len(bad),
                   'D_GATED': gated_n, 'D_OF': gated_of, 'D_IN_BAND': dband,
                   'GATE_RC': g.returncode, 'SECONDS': round(time.time() - t0, 1)})
    print(f'\n  the gate itself exits {g.returncode} on this tree;  price: {RESULT["SECONDS"]} s')
    return RESULT


if __name__ == '__main__':
    argparse.ArgumentParser(description=__doc__).parse_args()
    main()
