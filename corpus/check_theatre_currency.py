#!/usr/bin/env python3
"""check_theatre_currency.py -- A STATION ITS OWN THEATRE RECORDS AS DONE MAY NOT BE CARRIED AS OWED.

** ⛔⛭⛭ WHY.  THE SAME BOOKKEEPING FAILURE, TWICE, IN TWO THEATRES, WITH THE NOTICE WRITTEN BOTH
TIMES AND PROPAGATING NEITHER. **

  * *`L-263`: `OWED` 609 carried Ⓕ as owed while `THE_MATHEMATICS_REACH` recorded it walked -- and
    that document's own frontmatter says "this frontmatter carried Ⓕ as owed for forty-eight
    revisions after its own ① block recorded the answer."*
  * *`L-269`: `OWED` 609 carried all seven `R-P` stations as owed, one of them as "the earliest
    unrun", while `THE_PHYSICS_REACH` declares* **"THE WALK IS COMPLETE r2544 -- every station"**
    *and carries, for that very station, a section headed* **"THE ①② STRIKE -- made r2383, and the
    delay is the finding"**, *recording that it "had been marked NEXT for 578 revisions after it
    ran."*

  ⇒ *** A NOTICE WRITTEN WHERE THE ERROR HAPPENS DOES NOT REACH THE LIST THAT REPEATS IT.  Both
      theatres diagnosed the exact failure, in writing, about the exact stations, and the list
      downstream carried the stale state for hundreds of revisions in each case. ***
  ⇒ ** So it is not an anecdote and it is not carelessness: a theatre document is where the work is
    DONE and `OWED` is where the work is LISTED, and nothing carried a strike between them. **

** ⌗ WHAT THIS CHECKS. **  For every station label in `OWED`'s theatre item, and every station row in
the two theatre documents: *** if the theatre marks it done and `OWED` marks it owed, that is a
failure, and the gate names the station. ***

  ⌷ ** The parse is REPORTED, not assumed. **  *The station counts on both sides are printed every
    run, and a parse that finds no stations FAILS rather than passing vacuously -- because a
    consistency check that matched nothing would be green forever.*
  ⚠ ** WHAT IT CANNOT DO. **  *It compares MARKINGS, not work.  A station marked done that was not
    done is outside its reach, and so is a station absent from both documents.*  ⇒ ** It catches the
    failure that actually happened twice, and says so rather than implying more. **

    python3 corpus/check_theatre_currency.py

Written r3158 (`L-269`).  Stated for reversal.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

#: the two theatres, and the row pattern each document's station table uses
THEATRES = [
    ('THE_MATHEMATICS_REACH.md', r'\|\s*\*\*(Ⓐ|Ⓑ|Ⓒ|Ⓓ|Ⓔ|Ⓕ|Ⓖ|Ⓗ)\*\*'),
    ('THE_PHYSICS_REACH.md', r'\|\s*~*\*\*(①②|③④|⑤|⑥|⑦|⑨|⑩)\*\*~*'),
]
#: a theatre marks a station done with one of these
DONE = re.compile(r'STRUCK|WALKED|CLOSED|THROWN|already held|run and closed|baked', re.I)
#: `OWED` marks a station owed with one of these, in the station's own segment.
#: ⚠ ** THE FIRST FORM OF THIS REGEX REQUIRED `⟐` AT SEGMENT END and matched ONE station of seven. **
#:   *The list writes `③④ GR/gravitation (P8, P9) ⟐ · ⑤ …`, so the marker is mid-segment.*
#:   ⇒ *** An under-matching parse in a consistency gate is the same failure the gate exists to
#:       catch: it reported six stations as AGREED that it had simply not read. ***
#:   ⇒ ** The population is printed every run for exactly this reason, and the run that caught it
#:     was the one that printed "1 marked owed" against a list that plainly carries seven. **
OWED_MARK = re.compile(r'⟐|the earliest unrun')
STATION = re.compile(r'(Ⓐ|Ⓑ|Ⓒ|Ⓓ|Ⓔ|Ⓕ|Ⓖ|Ⓗ|①②|③④|⑤|⑥|⑦|⑨|⑩)')

#: ⚠⚠ ** MENTION VERSUS USE -- THE FIFTH TIME IN THIS LINE, AND THE FIRST TIME THE VICTIM WAS THE
#:   REPAIR ITSELF. **  *The strike that discharged the seven `R-P` stations records, as it must,
#:   what the list had said:* "①② as **the earliest unrun**".  *The gate read its own repair's
#:   QUOTATION of the stale marker as a fresh assertion of it and held ①② red -- so the act of
#:   documenting the fix re-created the failure.*
#:   ⇒ *** A GATE THAT CANNOT TELL A QUOTATION FROM A CLAIM PUNISHES THE RECEIPT THAT REPAIRS IT --
#:       which is `r3105`'s rule ("a check that pins a LIVE register punishes the finding it
#:       defends") arriving from the other side: not a live register read negatively, but a dead
#:       register QUOTED and read as live. ***
#:   ⌷ *So a marker inside quotation marks is a MENTION: it reports what a list SAID.  Quoted spans
#:     are removed before the marker is sought.*
#:   ⚠ ** THE COST, NAMED. **  *A genuine owed-marker written inside quotes would be missed.  That is
#:     accepted because the convention this corpus actually uses writes live markers bare and
#:     quotes only prior state -- and because the alternative considered (treat any station with a
#:     `~~STRUCK~~` disposition as disposed regardless of markers) weakens the gate everywhere,
#:     while this weakens it only inside quotation marks.*
#:   ⛭ ** AND IT IS CONTROLLED. **  *`control_fires()` runs every invocation on a segment that USES
#:     the marker bare; if un-quoting ever swallowed the live case the gate fails loudly instead of
#:     going quietly green.*
_QUOTED = re.compile(r'"[^"]{0,400}"|\u201c[^\u201d]{0,400}\u201d')


def unquote(seg):
    """a marker inside quotation marks is a MENTION of a list's prior state, not a claim"""
    return _QUOTED.sub(' ', seg)


CONTROL_USE = 'X station (P1, P2) \u27d0 and it is owed'
CONTROL_MENTION = 'X station, struck, recording that the row said "the earliest unrun" once'


def control_fires():
    """the live marker must still be seen after un-quoting, and the quoted one must not"""
    return (bool(OWED_MARK.search(unquote(CONTROL_USE)))
            and not bool(OWED_MARK.search(unquote(CONTROL_MENTION))))


def theatre_state():
    """{station: (theatre, done?)} read from each theatre's own station table"""
    out = {}
    for fn, pat in THEATRES:
        p = os.path.join(ROOT, fn)
        if not os.path.exists(p):
            continue
        for line in open(p, encoding='utf-8', errors='replace'):
            m = re.match(pat, line)
            if m:
                st = m.group(1)
                # ** a station may have more than one row (a superseded reading kept below a new
                #   one); DONE anywhere is done, which is the direction that cannot manufacture a
                #   failure out of an old row. **
                out[st] = (fn, out.get(st, (fn, False))[1] or bool(DONE.search(line)))
    return out


def owed_state():
    """{station: owed?} read from `OWED`'s theatre item, segment by segment"""
    p = os.path.join(ROOT, 'OWED.md')
    if not os.path.exists(p):
        return {}
    s = open(p, encoding='utf-8', errors='replace').read()
    i = s.find('`R-M`, eight stations')
    if i < 0:
        return {}
    block = s[i:i + 6000]
    marks, hits = {}, [m for m in STATION.finditer(block)]
    for k, m in enumerate(hits):
        end = hits[k + 1].start() if k + 1 < len(hits) else len(block)
        seg = unquote(block[m.start():end])
        st = m.group(1)
        marks[st] = marks.get(st, False) or bool(OWED_MARK.search(seg))
    return marks


def main():
    print()
    print('  check_theatre_currency -- is a station carried as OWED that its theatre records DONE?')
    print()
    if not control_fires():
        print('    \u26d4 [FAIL] the CONTROL did not fire: un-quoting has swallowed a live marker,')
        print('       or a quoted one still reads as a claim.  The gate is not measuring.')
        print()
        return 1
    print('    control: a bare marker is seen, a quoted one is not \u2014 fires.')
    th, ow = theatre_state(), owed_state()
    print(f'    theatre station rows parsed : {len(th)}   ({sum(1 for v in th.values() if v[1])} '
          f'marked done)')
    print(f'    OWED station segments parsed: {len(ow)}   ({sum(1 for v in ow.values() if v)} '
          f'marked owed)')
    print()
    # ** a parse that finds nothing FAILS: a consistency check matching no rows is green forever **
    if len(th) < 8 or len(ow) < 8:
        print('    ⛔ [FAIL] the parse found too few stations to be measuring anything.')
        print('       *A consistency check that matches nothing is green forever, so this is a')
        print('        failure rather than a pass.*  Check the table formats in both documents.')
        print()
        return 1

    bad = sorted(st for st, owed in ow.items()
                 if owed and st in th and th[st][1])
    for st in sorted(th):
        if st in ow:
            mark = '⛔ OWED-but-DONE' if st in bad else ('owed' if ow[st] else 'agreed')
            print(f'      {st:>3}  theatre {th[st][0][:26]:26s} done={str(th[st][1]):5s}  '
                  f'OWED owed={str(ow[st]):5s}  {mark}')
    print()
    if not bad:
        print('    no station is carried as owed that its own theatre records as done.')
        print()
        return 0
    print(f'    ⛔ {len(bad)} station(s) carried as OWED while their theatre records them DONE: '
          f'{bad}')
    print()
    print('    ⛭ ** A notice written where the error happens does not reach the list that repeats')
    print('       it. **  *Both theatres diagnosed this in writing, about these stations, and the')
    print('       list downstream carried the stale state for hundreds of revisions each time.*')
    print('    ⌷ Strike the station in `OWED`, or correct the theatre if the marking is wrong.')
    print()
    return 1


if __name__ == '__main__':
    sys.exit(main())
