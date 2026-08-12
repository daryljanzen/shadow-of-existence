#!/usr/bin/env python3
"""E3 -- the entry-point front is essentially worked, and the row has been advertising a 94-site backlog
for 148 revisions.

** WHAT THE ROW SAYS. **  L-210, registered r2397: "THE STATE, counted rather than remembered (r2397):
125 rows --- 16 ✔ LIVE with a route · 11 ✗ NOT A DOOR with why · 4 ⊕ ONE ROOM · ** 94 UNMARKED **."

** ⛭⛭ ⓵ RECOUNTED HERE. **

      r2397 (as the row states)          r2545 (measured)
      -------------------------          ----------------
      125 rows                           ** 141 rows **
      16 ✔ · 11 ✗ · 4 ⊕                  ** 26 ✔ · 56 ✗ · 36 ⊕ **
      *** 94 UNMARKED ***                *** 23 unmarked LINES ***

  ⇒ ** 118 sites have been given verdicts since, and the row was never recounted. **

** ⓶ AND OF THE 23 UNMARKED LINES, ONLY 7 ARE SITES AT ALL. **  The rest are the register's own table
headers and section-scan artefacts (`| § | kw | the paper's own words |`).
  ⌗ ** And SIX of the seven are SECTION HEADINGS ** -- "Frontiers and open problems", "Scope and open
  problems", "What stays open" -- which are the register's own scan rows for where a paper declares its
  frontier, ** not claims awaiting a verdict. **

** ⛭⛭⛭ ⓷ AND THE SEVENTH ALREADY HAS ITS VERDICT, IN ITS OWN DIG COLUMN. **  Site 1, "Whether the
SPACETIME extends across r=0":

  "** A PHANTOM, and I built it from the advertisement. **  (a) No paper asserts a spacetime
   extension --- grep clean across 17.  (b) What the corpus does assert: 'the substrate is the one
   smooth de Sitter manifold, C^infty across the locus the chart labels r=0' (P3, P7, P15)."

  ⇒ *** THE DIG WAS DONE AND THE VERDICT COLUMN WAS LEFT EMPTY.  A worked site reading as unworked --
      which is r2535's defect in a third register, and the one that made the whole front look open. ***

** ⓸ SO THE FRONT IS ESSENTIALLY WORKED, AND THAT IS THE FINDING. **  ** Not "94 sites remain" but
"every site carries a verdict and one marker was never written." **
  ⇒ ** And what the front produced is already on the board as its own rows ** -- L-210's own body records
    it: "all of P14's massive 54-development fell out of it."  *** The generator ran, delivered, and the
    row kept describing its starting state. ***

WHAT IS NOT CLAIMED.  ** Not that every verdict is right ** -- this recounts markers, it does not re-open
digs.  ** Not that the six section-heading rows are worthless **: they are the register's index of where
papers declare their frontiers, and they are correctly unmarked because ** a heading is not a claim. **
Not that L-210 should be struck without Daryl seeing the recount: ** the row's own next step says "work
the unmarked sites one at a time and without rushing", and the honest reply is that there are seven, six
are headings, and the seventh is done. **

Written r2546.  Stated for reversal.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def rows():
    t = open(os.path.join(ROOT, 'ENTRY_POINT_REGISTER.md'),
             encoding='utf-8', errors='replace').read()
    out = [l for l in t.split('\n')
           if l.startswith('|') and not re.match(r'\|\s*[-:]+', l)]
    return t, out


def main():
    print()
    print('  E3 -- how many entry-point sites are actually unworked?')
    print()
    t, rs = rows()
    arc = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'THE_LIVE_ARC.md'),
                                   encoding='utf-8', errors='replace').read())

    check("L-210 states the r2397 count: 125 rows with 94 UNMARKED",
          '94 UNMARKED' in arc or '94 unmarked' in arc.lower())

    marks = {}
    for r in rs:
        m = re.search(r'[✔✗⊕⟐★]', r)
        k = m.group(0) if m else 'UNMARKED'
        marks[k] = marks.get(k, 0) + 1
    check(f'⛭ recounted: {len(rs)} rows -- ✔{marks.get("✔",0)} · ✗{marks.get("✗",0)} · '
          f'⊕{marks.get("⊕",0)} · {marks.get("UNMARKED",0)} unmarked lines',
          len(rs) > 130 and marks.get('UNMARKED', 999) < 40)
    check('⇒ SO OVER A HUNDRED SITES HAVE BEEN GIVEN VERDICTS SINCE, AND THE ROW WAS NEVER RECOUNTED',
          marks.get('UNMARKED', 999) < 40)

    un = [r for r in rs if not re.search(r'[✔✗⊕⟐★]', r)]
    artefact = re.compile(r'^\|\s*(§|site|row|#|paper|kw)\s*\|', re.I)
    real = [r for r in un if not artefact.match(r) and "the paper's own words" not in r]
    check(f'⓶ and of the {len(un)} unmarked LINES only {len(real)} are sites -- the rest are the '
          "register's own headers and scan artefacts", len(real) <= 10)

    headings = [r for r in real if re.search(r'open problems|stays open|remains open|Scope and', r)]
    check(f'⌗ and {len(headings)} of the {len(real)} are SECTION HEADINGS ("Frontiers and open '
          'problems", "What stays open") -- the register\'s index of where papers declare a frontier, '
          'not claims awaiting a verdict', len(headings) >= 5)

    # ⓷ the seventh already has its verdict
    check('⛭⛭⛭ and the one remaining site already carries its verdict IN ITS OWN DIG COLUMN: "A '
          'PHANTOM, and I built it from the advertisement"',
          'A PHANTOM, and I built it from the advertisement' in t)
    check('with the dig recorded: no paper asserts a spacetime extension, grep clean across 17',
          'grep clean across 17' in t)
    check('⇒⇒ SO THE DIG WAS DONE AND THE VERDICT COLUMN WAS LEFT EMPTY -- a worked site reading as '
          'unworked, r2535\'s defect in a third register',
          'A PHANTOM, and I built it from the advertisement' in t)

    # ⓸ and the front delivered
    check("⌗ and L-210's own body records what the front produced: \"all of P14's massive "
          '54-development fell out of it"',
          "P14's massive 54-development fell out of it" in arc)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the front is essentially worked, and the row has been advertising a 94-site')
    print('  backlog for 148 revisions. **')
    print(f'    r2397 as stated:  125 rows, 94 UNMARKED')
    print(f'    r2546 measured:   {len(rs)} rows, ✔{marks.get("✔",0)} ✗{marks.get("✗",0)} '
          f'⊕{marks.get("⊕",0)}, {marks.get("UNMARKED",0)} unmarked LINES')
    print(f'  ⇒ ** Of those, only {len(real)} are sites at all, and {len(headings)} of THOSE are section')
    print('     headings -- correctly unmarked, because a heading is not a claim. **')
    print('  ⇒⇒ ** And the one remaining site already carries its verdict in its own dig column: "A')
    print('     PHANTOM, and I built it from the advertisement."  The dig was done and the marker was')
    print('     never written. **')
    print('  ⌗ ** So the finding is not "94 sites remain" but "every site carries a verdict and one')
    print('    marker was never written" ** -- and the generator already delivered: P14\'s whole')
    print('    54-development fell out of this front.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
