#!/usr/bin/env python3
"""check_settings.py -- THE REDUCED-SETTINGS LINT: a receipt reporting a quantity measured at reduced
settings must state what changes at production settings, or say why it cannot.

** THE ROUTED ITEM (c54.191), and the discipline is the fork's -- this file only turns it into a
check. **

  "Two retractions in two revisions, one cause.  c54.190 withdrew a spacing figure that was the first
   three gaps; c54.191 withdraws a sensitivity that was the first peak.  ** Both were the right
   measurement of the WRONG QUANTITY -- and in both cases the wrong quantity was the one the cheap
   experiment could see. **  The corpus now holds four instances of that shape: c54.164, c54.176,
   c54.190, c54.191.  ** Four isn't a coincidence and nothing we have looks for it. **  The best I
   could write is a discipline rather than a check -- ** a receipt reporting a quantity measured at
   reduced settings should have to state what changes at production settings, or say why it cannot **
   -- and I've routed it to 56, who is better at turning disciplines into gates than I am."

** ⛭⛭ AND THE DISCIPLINE AS WRITTEN IS ALREADY A DECLARATION, WHICH IS WHY IT IS BUILDABLE. **

L-237's rule: ** every gate in this corpus checks something SOMEBODY DECLARED, and both lints INFER
and are outside the gate list. **  Three earlier gate requests each needed a declaration the corpus does
not carry.  ** This one names its own: "state what changes at production settings, or say why it
cannot" IS a thing a receipt declares. **  The fork wrote the declaration into the discipline without
naming it as one.

** THE CONVENTION. **  A receipt that runs at reduced settings carries a line:

    SETTINGS: reduced -- <knob>=<value> vs production <value>.  AT PRODUCTION: <what changes>.
    SETTINGS: reduced -- <knob>=<value>.  CANNOT CHECK AT PRODUCTION: <why>.
    SETTINGS: production.

** THE CHECK.  Two halves, and only the first can be mechanical: **
  * ** MECHANICAL: ** a receipt naming a reduced-setting knob (LMAXL, NK, LSTEP, NLOS, KBATCH ...) at
    a value below the production one, WITHOUT a `SETTINGS:` line, is flagged.
  * ** NOT MECHANICAL, and stated so: ** whether the receipt's stated "AT PRODUCTION" is TRUE.  ** No
    script can run someone else's experiment. **

⚠ ** SO IT IS A LINT AND NOT A GATE, for the reason check_depth is: ** a reduced-settings run is not a
defect -- it is usually the only affordable one.  ** The defect is quoting a production quantity from
it, and no script can see which quantity a human quoted. **

⌗ AND check_depth (r2484) IS THE SAME SHAPE ONE LEVEL DOWN: it reads DEPTH off the DATA, this reads
SETTINGS off the RECEIPT.  ** Together they cover the two places the evidence lives, and neither can
cover the judgement between them. **

    python3 corpus/check_settings.py            # report
    python3 corpus/check_settings.py --verbose  # every receipt that names a knob

Written r2486.  Stated for reversal.
"""
import os
import re
import sys
import glob

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

# knobs whose reduction is what the four instances have in common, with production values
# taken from the instrument's own defaults / the deepest run banked in the tree
PRODUCTION = {'LMAXL': 3000.0, 'NK': 260.0, 'LSTEP': 8.0, 'NLOS': 560.0, 'KBATCH': 250.0}
DECL = re.compile(r'^\s*(?:#\s*)?SETTINGS:', re.M)


def scan():
    flagged, declared, clean = [], [], 0
    for f in sorted(glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True)):
        t = open(f, encoding='utf-8', errors='replace').read()
        found = {}
        for knob, prod in PRODUCTION.items():
            for m in re.finditer(rf"\b{knob}\b\s*[=:]\s*'?([0-9]+(?:\.[0-9]+)?)'?", t):
                try:
                    v = float(m.group(1))
                except ValueError:
                    continue
                if v < prod:
                    found[knob] = min(found.get(knob, v), v)
        rel = os.path.relpath(f, ROOT)
        if not found:
            clean += 1
        elif DECL.search(t):
            declared.append((rel, found))
        else:
            flagged.append((rel, found))
    return flagged, declared, clean


def main():
    verbose = '--verbose' in sys.argv
    flagged, declared, clean = scan()
    print()
    print('  check_settings -- a quantity measured at reduced settings needs a stated production')
    print('                    comparison, or a stated reason there cannot be one')
    print()
    print('  production values checked: '
          + ', '.join(f'{k}={v:g}' for k, v in sorted(PRODUCTION.items())))
    print()
    print(f'  receipts naming no reduced knob      : {clean}')
    print(f'  naming one WITH a SETTINGS: line     : {len(declared)}')
    print(f'  naming one WITHOUT one               : {len(flagged)}')
    if flagged:
        print()
        for rel, found in (flagged if verbose else flagged[:10]):
            k = ', '.join(f'{a}={b:g}' for a, b in sorted(found.items()))
            print(f'     {rel}   ({k})')
        if not verbose and len(flagged) > 10:
            print(f'     ... and {len(flagged)-10} more (--verbose for all)')
    print()
    print('  ⌗ MECHANICAL half only: this sees whether a SETTINGS: line EXISTS.')
    print('    ** Whether its stated "AT PRODUCTION" is TRUE is a judgement -- no script can run')
    print('    someone else\'s experiment. **')
    print('  ⚠ LINT, not gate: a reduced-settings run is not a defect, it is usually the only')
    print('    affordable one.  ** The defect is quoting a production quantity from it. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
