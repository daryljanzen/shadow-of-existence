#!/usr/bin/env python3
"""check_absence_claims.py -- AN ABSENCE CLAIM MUST CARRY WHAT WAS SEARCHED.

** THE ERROR THIS EXISTS FOR, AND IT IS MINE. **  At r6481 this line wrote "the corpus
does not note this" about the offset-mass relation's maximum being the Nariai member.
It was FALSE: `P15` states the double-root condition f = f' = 0 outright, and the offset
relation IS the horizon condition f(r)=0 written in r_0, so the two are one statement.
*** The claim rested on two greps of corpus/*.tex.  P03, P17 and P15 -- the obvious
places to look -- were never opened. ***

** THE FAILURE IS A COLLAPSE OF QUANTIFIER. **  "My search did not find it" became "it
is not there."  In a corpus whose whole value is coherence, an asserted absence that is
false plants a contradiction that later work builds on -- and it is invisible, because
nothing contradicts a claim nobody re-checks.

THE CORPUS ALREADY STATES THE REMEDY and has since the source rule: never assert the
corpus does or does not have X without knowing from source, and say which -- ** NOT
FOUND / SEARCHED / NOT YET CHECKED **.  What was missing was enforcement.

** WHAT THIS CHECKS. **  A claim that a phrase or fact is ABSENT FROM THE TEXT must have
evidence of the search within reach of it -- what was grepped, how many sites, "read at
source", "zero occurrences".  ** It does NOT touch claims about what the corpus ASSERTS
("the corpus does not posit a second scale"): that is a position, not a textual absence,
and needs no search behind it.  Conflating the two was the first draft's error and it
returned 302 hits, mostly false. **

** AND IT IS A RATCHET, not a retrofit. **  89 bare sites predate it and are baselined
by exact text, the same remedy `check_receipt_prefixes` and `check_receipt_home` chose:
nothing existing must move, and what is stopped is the NEXT one.  A new bare absence
claim fails.  ⌗ To clear a failure, say what you searched -- not by deleting the claim.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..')
BASE = os.path.join(HERE, 'absence_claims_baseline.txt')

# TEXTUAL-absence claims only.  Not "the corpus does not posit/need/cross" -- those are
# positions about content, and requiring a search behind them is a category error.
CLAIM = re.compile(
    r"(appears? nowhere|occurs? nowhere|nowhere in the corpus"
    r"|occurs? zero times|zero occurrences"
    r"|unremarked in the corpus"
    r"|none (?:remarks|notes)"
    r"|(?:the corpus|no paper) (?:does not|doesn't) (?:note|remark|record|draw|connect) (?:this|it|them)"
    r"|is (?:stated|noted|drawn|recorded) nowhere)", re.I)

EVIDENCE = re.compile(
    r"(grep|searched|scanned|NOT FOUND|NOT YET CHECKED|zero (?:occurrences|hits|times)"
    r"|\d+ sites?|read (?:whole|at source)|at source|checked|x\d+|occurrences?\b)", re.I)

SKIP_DIRS = ('/.git', '/receipts/', '/BOOK_INTRO')


def scan():
    out = []
    for root, _, files in os.walk(ROOT):
        if any(k in root.replace('\\', '/') for k in SKIP_DIRS):
            continue
        for f in sorted(files):
            if not f.endswith(('.md', '.tex', '.py')):
                continue
            p = os.path.join(root, f)
            try:
                s = open(p, encoding='utf-8', errors='replace').read()
            except OSError:
                continue
            for m in CLAIM.finditer(s):
                window = s[max(0, m.start() - 300):m.start() + 300]
                if EVIDENCE.search(window):
                    continue
                rel = os.path.relpath(p, ROOT).replace('\\', '/')
                out.append((rel, m.group(0).strip().lower()))
    return out


def baseline():
    if not os.path.exists(BASE):
        return None
    return {tuple(l.rstrip('\n').split('\t', 1)) for l in open(BASE, encoding='utf-8')
            if l.strip() and not l.startswith('#')}


def main():
    found = scan()
    base = baseline()
    print()
    print('  ABSENCE CLAIMS -- does each carry what was searched?')
    print()
    if base is None:
        print(f'  [FAIL] {os.path.relpath(BASE, ROOT)} is absent; the baseline is data and must exist')
        return 1
    counts = {}
    for rel, txt in found:
        counts[(rel, txt)] = counts.get((rel, txt), 0) + 1
    new = [k for k in counts if k not in base]
    print(f'    {len(found)} bare claim(s) found; {len(base)} baselined')
    print()
    if new:
        print(f'  ⛔ {len(new)} BARE ABSENCE CLAIM(S) NOT IN THE BASELINE:')
        for rel, txt in sorted(new)[:20]:
            print(f'    [FAIL] {rel}: "{txt}"')
        print('     ⌗ Say what you SEARCHED, beside the claim -- which files, which')
        print('       phrases, or "read at source".  ** "My grep missed it" is not')
        print('       "it is not there", and that collapse is what this gate exists for. **')
        print('       If the claim is right and the search is genuinely wide, say so and')
        print('       the evidence clears it; do not delete the claim to pass.')
        print()
        return 1
    print('  no new bare absence claim.')
    print('  ⌗ Baselined sites are grandfathered: nothing existing must move, and what')
    print('    is stopped is the next one -- the remedy this corpus has chosen three')
    print('    times now for a namespace it did not want to churn.')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
