#!/usr/bin/env python3
"""check_rerunnable_honest.py -- A PERMANENTLY-RED RECEIPT MUST SAY THAT IT IS ONE.

** WHY.  r2901-r2902. **  *** Sweeping the 45 receipts whose checks assert register state found six
failures, and ** three were not defects **: `R1_a_protected_row_was_corrupt`, `M1_the_merge_of_my_own_
revision` and `R1_the_registry_was_checked` each ** verified a REPAIR at its own revision ** ("the repair
loses no distinct word, file-wide").  Any later legitimate edit to a protected row breaks them, and this
session made hundreds. ***

  ⇒ ** A check that verifies a repair cannot survive later edits. **  *** Those receipts are CORRECT
      about what they did and PERMANENTLY RED, and the corpus had ** no convention distinguishing them
      from invariants ** -- not a naming rule, not a directory, not a flag.  Checked: prefixes are by
      series, directories by paper. ***

  ⌗ ** And that is how a suite becomes noise. **  *** A "run everything" gate would report three
    failures forever, and the reader learns to skim. ***

** THE CONVENTION, ADDED r2902. **  *** A receipt that cannot be re-run green carries
`# RERUNNABLE: NO — POINT-IN-TIME` in its header, with the reason. ***

** WHAT THIS CHECKS. **  *** Every receipt marked `RERUNNABLE: NO` states a reason on the following
lines -- so the mark can never become a way to silence a real failure. ***

⛔⛭⛭ ** EXTENDED r3126 (`L-255`), AND THE EXTENSION IS AGAINST r2902's OWN DIAGNOSIS. **  *r2902 said
"a check that verifies a repair cannot survive later edits" and built this convention on it.  **That
sentence is false as stated.**  Those three receipts broke because they read the repair's POST-state
from the WORKING TREE while pinning its pre-state to a SHA; pin both ends and the same check verifies
the same repair forever.*
  ⇒ *** r3125 pinned all three.  ALL THREE NOW EXIT 0 -- and all three still carried the mark. ***
  ⇒ ** So an exemption is a CLAIM: "no repair exists for this failure."  r2802 named the class it
    belongs to -- *"'not mechanically fixable' is a claim, and it is the one kind a node is never
    asked to defend"* -- and here the claim was wrong for every instance it was written for. **

** ⌗ THE SECOND CHECK, therefore: A MARKED RECEIPT THAT EXITS 0 IS A STALE EXEMPTION. **  *It is run.
Exit 0 means the mark is claiming a permanence the file does not have, and the mark must come off.*
  ⌷ ** A timeout or an environmental death is NOT counted as green ** -- it is reported, because a
    receipt that could not be run says nothing about whether it can pass.  *The conservative
    direction is the one that does not silence a real exemption.*

    python3 corpus/check_rerunnable_honest.py
    python3 corpus/check_rerunnable_honest.py --no-run    # the reason check only

Written r2902; extended r3126 (`L-255`).  Stated for reversal.
"""
import glob
import os
import re
import subprocess
import sys

#: a marked receipt gets this long to prove it is still red; longer than the runner's own per-file
#: budget, and a receipt that overruns it is REPORTED rather than judged either way
TIMEOUT = 420

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

MARK = re.compile(r'#\s*RERUNNABLE:\s*NO', re.I)


def header(src):
    """the LEADING COMMENT BLOCK -- everything before the first line that is not `#` or blank

    ⛔⛭⛭ ** ADDED r3126 (`L-255`), AND IT IS A RECURSION GUARD AS WELL AS A CORRECTNESS ONE. **
    *The mark was matched anywhere in the file.  `L-255`'s own receipt SEEDS this gate by writing a
    marked file, so it carries the mark inside a string literal -- and the gate, having just gained
    the power to RUN what it marks, ran that receipt, which runs this gate.*
      ⇒ *** The MENTION-versus-USE distinction (r3100's matcher gate) reached by a third route in one
          revision, and this time with teeth: a mention that is executed is an infinite regress. ***
      ⇒ ** The convention puts the mark in the leading comment block, above the docstring.  That is
        where it is read, and nowhere else. **
    """
    out = []
    for ln in src.split('\n'):
        if ln.startswith('#') or not ln.strip():
            out.append(ln)
            continue
        break
    return '\n'.join(out)


def main():
    print()
    print('  check_rerunnable_honest -- does every permanently-red receipt say why?')
    print()
    files = sorted(glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True))
    marked, bad, marked_files = 0, [], []
    for f in files:
        t = open(f, encoding='utf-8', errors='replace').read()
        m = MARK.search(header(t))
        if not m:
            continue
        marked += 1
        marked_files.append(f)
        # ** r2902a: the first form measured prose in a 700-char window, and UNRELATED
        # comment blocks below the mark satisfied it -- the seed did not fire.  *** The
        # reason must be in the CONTIGUOUS comment block the mark opens: read forward only
        # while lines are comments, and stop at the first that is not. ***
        # ⌗ the header is a PREFIX of the file, so an offset into it is an offset into the file
        tail = t[m.end():].split('\n')[1:]
        block = []
        for ln in tail:
            if not ln.lstrip().startswith('#'):
                break
            block.append(ln)
        if len(re.sub(r'[#\s*]', '', '\n'.join(block))) < 80:
            bad.append(os.path.basename(f)[:46])

    print(f'  {len(files)} receipt(s); {marked} marked RERUNNABLE: NO')
    rc = 0
    if bad:
        print()
        for b in bad:
            print(f'    [FAIL] {b} is marked RERUNNABLE: NO with no reason given')
        print()
        print('    ⛭ ** The mark must never become a way to silence a real failure. **')
        rc = 1
    else:
        print('  every marked receipt states its reason.')

    # ------------------------------------------------------------------ r3126 (`L-255`)
    # ** AND THE REASON IS A CLAIM, SO IT IS TESTED. **  *An exemption says "this cannot be made
    #   green".  r2902 wrote three of them on one diagnosis and r3125 falsified the diagnosis by
    #   repairing all three.  An exemption that nobody can falsify is a silencer with a reason
    #   attached.*
    if '--no-run' in sys.argv:
        print()
        print('  --no-run: the exemptions are NOT tested this run.  *That is a weaker verdict and')
        print('   it is said so, rather than printed as a pass.*')
        print()
        return rc
    stale, unproven = [], []
    print()
    for f in marked_files:
        b = os.path.basename(f)[:52]
        try:
            r = subprocess.run([sys.executable, f], cwd=os.path.dirname(f), capture_output=True,
                               text=True, errors='replace', timeout=TIMEOUT)
            if r.returncode == 0:
                stale.append(os.path.relpath(f, ROOT))
                print(f'    [FAIL] {b} exits 0 -- the exemption is STALE')
            else:
                print(f'    [ok]   {b} exits {r.returncode} -- the exemption still holds')
        except subprocess.TimeoutExpired:
            unproven.append(os.path.relpath(f, ROOT))
            print(f'    [報]   {b} did not finish in {TIMEOUT}s -- REPORTED, not judged')
        except OSError as e:
            unproven.append(os.path.relpath(f, ROOT))
            print(f'    [報]   {b} could not be run ({e.__class__.__name__}) -- REPORTED')
    if stale:
        print()
        print(f'    ⛔ {len(stale)} STALE EXEMPTION(S).  ** A receipt that exits 0 is not permanently')
        print('       red, and its mark is claiming a permanence the file does not have. **')
        print('       *Remove the mark, or say in it what the exit-0 run is not covering.*')
        rc = 1
    if unproven:
        print(f'    ⌗ {len(unproven)} not judged either way -- reported so the number is not read as')
        print('      a clean bill: a receipt that could not be run says nothing about passing.')
    print()
    return rc


if __name__ == '__main__':
    raise SystemExit(main())
