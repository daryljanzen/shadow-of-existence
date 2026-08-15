#!/usr/bin/env python3
"""check_appendix_current.py -- IS EVERY GENERATED APPENDIX ACTUALLY THE ONE THE LEDGER GENERATES?

** WHY.  `make_receipt_appendix`'s own first line says: ** *"Single source of truth: the paper's
appendix can never drift from the ledger, ** because it is regenerated **."*  *** Nothing checked
that it HAD been. ***

** ⛭⛭ AND THE ONE INSTRUMENT THAT LOOKS NEARBY CANNOT SEE THIS. **  `check_compile` fails on a DEAD
LINK -- a `\\rcpt{}` in a paper body with no appendix entry to point at.  That catches a stale
appendix only when the new row is also CITED.
  ⇒ *** A row added to the INDEX and not yet cited produces no dead link, so the appendix simply
      lags, silently, for as long as nobody runs the generator by hand. ***  At c54.222 the last
      regeneration was r2727 and the INDEX had moved 49 revisions past it: `P10` was 30 lines short,
      `P14` 55, `P15` 80, and the corpus appendix 290.  ** That is r2376+c54.36's 105 dead links
      arriving again by the one route c54.36's fix does not cover. **

** ⌗ THE ONE DESIGN CHOICE, STATED.  This gate regenerates into a TEMPORARY directory and compares
bytes; it never writes into `corpus/`. **  *A gate that repaired what it measures would report green
on a tree nobody had looked at -- which is the stale-cache failure r2656+c54.208 found in the receipt
runner, and it is not worth reintroducing to save one command.*  When it fails, the fix is one line:

    python3 corpus/make_all_appendices.py

    python3 corpus/check_appendix_current.py

Written c54.222 (`L-556`).  Stated for reversal.
"""
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
GEN = os.path.join(HERE, 'make_receipt_appendix.py')

TARGETS = [(f"P{n}", f"appendix_receipts_P{n:02d}.tex" if n < 10
            else f"appendix_receipts_P{n}.tex") for n in range(1, 18)]
TARGETS.append(('corpus', 'appendix_receipts_corpus.tex'))


def main():
    print()
    print('  check_appendix_current -- is each Appendix R the one the INDEX generates right now?')
    print()
    stale, broken, checked = [], [], 0
    tmp = tempfile.mkdtemp(prefix='appx.')
    try:
        for scope, name in TARGETS:
            live = os.path.join(HERE, name)
            if not os.path.exists(live):
                continue
            out = os.path.join(tmp, name)
            p = subprocess.run([sys.executable, GEN, scope, out], cwd=HERE,
                               capture_output=True, text=True, errors='replace')
            if p.returncode or not os.path.exists(out):
                broken.append((name, (p.stderr or p.stdout).strip()[-200:]))
                continue
            checked += 1
            a = open(live, 'rb').read()
            b = open(out, 'rb').read()
            if a != b:
                da = len(b.split(b'\n')) - len(a.split(b'\n'))
                stale.append((name, da))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print(f'    {checked} appendix/appendices regenerated into a temporary directory and compared')
    if broken:
        print()
        for name, msg in broken:
            print(f'    [FAIL] {name} -- the generator could not produce it: {msg}')
    if stale:
        print()
        for name, da in stale:
            d = f'{da:+d} line(s)' if da else 'same length, different bytes'
            print(f'    [FAIL] {name} is STALE -- the ledger would write {d}')
        print()
        print('    ⛭ ** A generated file that is not regenerated is a hand-maintained one that')
        print('       nobody is maintaining. **  *** And an appendix short of the ledger does not')
        print('       LOOK wrong -- it looks like a shorter appendix. ***')
        print('       Fix:  python3 corpus/make_all_appendices.py')
    if stale or broken:
        print()
        return 1
    print('    every appendix matches what the INDEX generates.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
