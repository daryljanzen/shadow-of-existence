#!/usr/bin/env python3
"""check_ingestion_current.py -- EVERY REVISION IN LATENT_HISTORY MUST APPEAR IN INGESTION.

** WHY.  r2782: ** *** Daryl asked whether cc54's updates were fully integrated.  Checking, I found
`bundle/c54_200` stale and subsumed -- ** and then found that 51 of my own claim-lines had never
landed **.  Every `--claim` write to `INGESTION.md` since r2730 was a ** silent no-op **: the anchor
string I was replacing had stopped matching, `str.replace` returned the input unchanged, and I printed
"claimed" each time. ***

  ⇒ ** The failure mode is the printed success. **  *** A write that fails LOUDLY is a nuisance; a write
      that fails while reporting success is a fabricated record -- and I generated fifty-one of them
      across an entire session without noticing. ***

  ⌗ ** `LATENT_HISTORY` was complete throughout ** -- *** it is appended to, not pattern-matched, and an
    append cannot silently miss.  ** The two logs disagreed by 51 rows and only the one built on a
    fragile operation was wrong. ** ***

** WHAT THIS CHECKS. **  Every `rNNNN` row in `LATENT_HISTORY.txt` appears somewhere in `INGESTION.md`.

  ⌗ *** It does not check the CONTENT matches -- only that the revision is present.  That is enough:
    the defect being guarded is a whole line going missing, not a line going wrong. ***

    python3 corpus/check_ingestion_current.py

Written r2782.  Stated for reversal.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))


def main():
    print()
    print('  check_ingestion_current -- is every logged revision on the claim slate?')
    print()
    lat = os.path.join(ROOT, 'LATENT_HISTORY.txt')
    ing = os.path.join(ROOT, 'INGESTION.md')
    for f in (lat, ing):
        if not os.path.exists(f):
            print(f'  [FAIL] {os.path.basename(f)} is missing')
            return 1

    logged = sorted(set(re.findall(r'^(r\d{4})\s', open(lat, encoding='utf-8',
                                                        errors='replace').read(), re.M)))
    slate = open(ing, encoding='utf-8', errors='replace').read()
    missing = [r for r in logged if r not in slate]

    print(f'  {len(logged)} revision(s) in LATENT_HISTORY')
    if missing:
        print()
        print(f'    [FAIL] {len(missing)} absent from INGESTION: {missing[:8]}'
              f'{" …" if len(missing) > 8 else ""}')
        print()
        print('    ⛭ ** This is what a silently-failing write looks like from outside. **  *** An')
        print('       anchored `str.replace` that stops matching returns its input unchanged and')
        print('       reports nothing.  `LATENT_HISTORY` is APPENDED to and cannot miss this way —')
        print('       which is why the two logs are worth comparing. ***')
        return 1
    print('  every logged revision is on the slate.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
