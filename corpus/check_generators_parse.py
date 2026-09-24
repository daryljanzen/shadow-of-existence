#!/usr/bin/env python3
"""check_generators_parse.py -- do the GENERATORS still compile?

** PROPOSED BY NODE 60 AT r6810 AFTER THE SAME BREAK TWICE IN TWO REVISIONS.  IT IS A CHANGE TO THE
GATE LIST, WHICH IS 66's TO MAKE, SO IT ARRIVES AS ITS OWN COMMIT AND CAN BE DROPPED ALONE. **

WHAT HAPPENED, TWICE.  `scripts/regen_frontier.py` carries the frontier's row text as Python string
literals.  Prose contains apostrophes -- "the control's 0.9559" (r6805), "node 60's r6804" and "m'(r)"
(r6809) -- and an apostrophe inside a SINGLE-quoted literal closes it early:

      r6805  line 197   SyntaxError: unterminated string literal
      r6809  line 130   SyntaxError: invalid decimal literal

** Each time the generator could not run, so the row the revision had just written never reached
THE_FRONTIER.md -- and each time every gate stayed green. **  `grep` for the revision's own marker found
it once in the generator source and zero times in the document, both times.

WHY NOTHING CAUGHT IT.  `regen_frontier.py` is not in `gates.yml` at all, and `check_frontier_current`
IS -- but it compares runways against rows and never invokes the generator.  ** So a served document's
generator can be broken on `main` with the whole fast job green.  That is the shape
`check_receipts_run`'s own comment names: green because nothing looked. **

WHAT THIS DOES.  Compiles every generator and gate in `scripts/` and `corpus/` -- parse only, nothing is
executed and nothing is written -- and fails on the first that does not.  *It is the cheapest possible
check for the cheapest possible failure: a file that cannot run cannot be doing its job.*

    python3 corpus/check_generators_parse.py
"""
import ast
import glob
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# ** SCOPED TO WHAT WRITES OR CHECKS A DOCUMENT, WHICH IS WHERE A BROKEN FILE DOES SILENT DAMAGE. **
# `scripts/` holds the generators and `corpus/check_*`/`make_*` the gates and builders.  *Analysis
# scripts elsewhere in `corpus/` are deliberately OUT of scope: nothing runs them, so a break in one
# costs a reader an error message rather than costing a document its content.*
#   ⌗ Two of those do currently fail to parse on the pinned interpreter -- `corpus/the_mapping.py` and
#     `corpus/the_mapping_full.py`, both "f-string expression part cannot include a backslash", which is
#     legal from Python 3.12 and `gates.yml` pins 3.11.  ** Reported to 66 rather than edited here: they
#     are nobody's generator and fixing them is not this order's business. **
PATS = ('scripts/*.py', 'corpus/check_*.py', 'corpus/make_*.py')

print()
print("  check_generators_parse -- every generator and gate compiles")
print("  " + "-" * 66)

bad, n = [], 0
for pat in PATS:
    for f in sorted(glob.glob(os.path.join(ROOT, pat))):
        n += 1
        rel = os.path.relpath(f, ROOT)
        try:
            ast.parse(open(f, encoding='utf-8').read(), filename=rel)
        except SyntaxError as e:
            bad.append((rel, e.lineno, e.msg))

print(f"    {n} file(s) parsed")
if bad:
    print()
    for rel, lineno, msg in bad:
        print(f"  ⛔ [FAIL] {rel}:{lineno} -- {msg}")
    print()
    print("     A generator that does not compile cannot write its document, and the document")
    print("     then sits at whatever it last contained while every other gate passes.")
    print("     ⌗ The usual cause here is prose: an apostrophe inside a single-quoted literal.")
    print("       Requote that line to double quotes -- the row texts carry no double quote.")
    sys.exit(1)

print()
print("  every generator and gate compiles.")
print("  ⌗ Parse only: this says a file CAN run, not that its output is current.")
print("    check_frontier_current and check_pages_current say the second thing, and they")
print("    pass without invoking a generator -- which is why both checks are wanted.")
