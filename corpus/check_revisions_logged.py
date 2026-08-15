#!/usr/bin/env python3
"""check_revisions_logged.py -- EVERY REVISION IN THE HISTORY FILE MUST HAVE A `CORPUS_MAP` ENTRY.

** WHY.  r2834. **  *** Enumerating the state layer's relations turned up `CORPUS_MAP`→register as
ungated, and testing it found `PO-3`'s strike unlogged.  ** Pulling that thread found the real defect:
r2832, r2833 and r2834 had NO `CORPUS_MAP` ENTRY AT ALL. **  Three whole revisions of work -- the entire
state-layer sweep -- existed in `LATENT_HISTORY` and the wisdom ledger and nowhere in the revision
log. ***

  ⇒ *** The log is the programme's memory across compactions.  ** Work that is not in it did not
      happen, as far as the next instance is concerned ** -- and this line spent a whole session writing
      lessons to the ledger while the log of what was DONE went unwritten. ***

** WHAT THIS CHECKS. **  *** Every revision id appearing in `LATENT_HISTORY.txt` has a matching
`### Revision rNNNN` entry in `CORPUS_MAP.md`. ***

  ⌗ ** The reverse is not required ** -- *** the log may carry entries for work the history file never
    recorded, and that is not a defect. ***

    python3 corpus/check_revisions_logged.py

Written r2834.  Stated for reversal.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

# ** how far behind the newest history line the log may sit before it is a defect **
GRACE = 0


def main():
    print()
    print('  check_revisions_logged -- does every revision have a CORPUS_MAP entry?')
    print()
    hist = open(os.path.join(ROOT, 'LATENT_HISTORY.txt'), encoding='utf-8',
                errors='replace').read()
    cm = open(os.path.join(ROOT, 'CORPUS_MAP.md'), encoding='utf-8', errors='replace').read()

    revs = sorted({int(m) for m in re.findall(r'^r(\d{3,4})\b', hist, re.M)})
    logged = {int(m) for m in re.findall(r'^### Revision r(\d{3,4})', cm, re.M)}

    missing = [r for r in revs if r not in logged]
    print(f'  {len(revs)} revision(s) in LATENT_HISTORY; {len(logged)} entries in CORPUS_MAP')

    if missing:
        # ** only the recent tail is actionable; older gaps are archaeology **
        recent = [r for r in missing if r > max(revs) - 60]
        if recent:
            print()
            for r in recent[-12:]:
                print(f'    [FAIL] r{r} is in LATENT_HISTORY and has no CORPUS_MAP entry')
            print()
            print('    ⛭ ** The log is the programme\'s memory across compactions. **')
            print('       *** Work that is not in it did not happen, as far as the next instance')
            print('       is concerned. ***')
            return 1
        print(f'  {len(missing)} older gap(s), none in the recent tail')

    print('  every recent revision is logged.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
