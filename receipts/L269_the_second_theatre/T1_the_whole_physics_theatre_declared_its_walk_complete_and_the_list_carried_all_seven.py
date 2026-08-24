#!/usr/bin/env python3
r"""T1 -- the same bookkeeping failure as L-263, in the other theatre, and complete: THE_PHYSICS_REACH
declares "THE WALK IS COMPLETE r2544 -- every station", and OWED 609 carries all seven of its stations
as owed, one of them as "the earliest unrun" -- while that station's own document has a section headed
"THE ①② STRIKE -- made r2383, and the delay is the finding".

COMPUTES: each of the seven stations' state read from its own row in THE_PHYSICS_REACH, and its state
in OWED 609's list, parsed separately and compared; the physics theatre's own completeness declaration
and its own note on the mislabelling; the span in revisions between the strike and the list; the ten of
fifteen total across both theatres; and the new gate's behaviour, seeded in both directions.  Nothing
is pinned numerically and nothing is fitted.

** ⛭ ⓵ WHAT `L-263` FOUND, AND WHY IT WAS NOT THE WHOLE OF IT. **  *Three of eight `R-M` stations were
carried as owed while their theatre recorded them held, and one -- Ⓕ -- had been diagnosed in that
document's own frontmatter.*  ⇒ ** That receipt did not audit the OTHER list. **

** ⛔⛭⛭ ⓶ AND THE OTHER LIST IS STALE IN FULL. **  `THE_PHYSICS_REACH`'s own heading:

      *** "✔✔✔ THE WALK IS COMPLETE r2544 -- every station, and the class is six-for-six" ***

  and its station table marks ①② STRUCK, ③④ WALKED, ⑤ WALKED with the owe discharged, ⑥ WALKED and
  closed, ⑦ WALKED, ⑨ WALKED, ⑩ WALKED.
  ⇒ ** `OWED` 609, written at r3122, carries all seven as ⟐ owed -- and ①② as "the earliest unrun". **

** ⛔ ⓷ AND ①② IS THE SAME STATION THAT DOCUMENT ALREADY WROTE THIS ABOUT. **  Its section heading:

      *** "THE ①② STRIKE -- made r2383, and the delay is the finding" ***

  *and inside: the row "read 'NEXT -- the earliest unrun station' while ①② had already been run."*
  ⇒ *** SO THE EXACT PHRASE `OWED` USES AT r3122 IS THE PHRASE THAT DOCUMENT RECORDED AS THE ERROR AT
      r2383.  The diagnosis was written, in the right place, about the right station, in the right
      words -- and the list downstream reproduced it seven hundred revisions later. ***

** ⌗ ⓸ SO IT IS NOT AN ANECDOTE AND NOT CARELESSNESS -- IT IS STRUCTURAL. **  *Two theatres, two
notices written at the site of the error, zero propagation, and ten stale entries of fifteen.*
  ⇒ ** A theatre document is where the work is DONE; `OWED` is where the work is LISTED; and nothing
    carried a strike from one to the other. **
  ⇒ *** Which is mechanizable, and `corpus/check_theatre_currency.py` is the mechanism: a station its
      own theatre records as done may not be carried as owed. ***

** ⚠ ⓹ AND THE GATE'S FIRST FORM UNDER-MATCHED, WHICH IS ITS OWN CLASS. **  *Its `OWED` marker regex
required `⟐` at segment end; the list writes `③④ GR/gravitation (P8, P9) ⟐ · ⑤ …`, mid-segment.*
  ⇒ ** It reported ONE station and called the other six AGREED -- six it had simply not read. **
  ⇒ *** An under-matching parse in a consistency gate IS the failure the gate exists to catch, and it
      was caught only because the gate prints its population every run: "1 marked owed" against a
      list that plainly carries seven. ***

WHAT IS NOT CLAIMED.  ** Not that the seven stations need no further work ** -- "walked" is not
"baked", the `R-M` distinction applies here too, and a station can be walked and still owe a full
field bake; what is false is the MARKING, which says unrun.  ** Not that the physics theatre is right
that the walk is complete ** -- this receipt compares the two documents' markings and does not
re-audit the walk.  ** Not that the gate catches the general case ** -- it compares markings, not
work, and a station marked done that was not done is outside its reach, which its own head says.
** And not that `L-263`'s receipt should have caught this ** -- it audited the list it was told to
strike from; what this adds is that the instruction named two stations and the failure had ten.

    python3 receipts/L269_the_second_theatre/T1_the_whole_physics_theatre_declared_its_walk_complete_and_the_list_carried_all_seven.py

Written r3158, `L-269`.  Stated for reversal.
"""
import importlib.util
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []
PARENT = '5722ecf7'          # r3156 -- before this revision strikes the R-P list

spec = importlib.util.spec_from_file_location('_tc', os.path.join(ROOT, 'corpus',
                                                                  'check_theatre_currency.py'))
TC = importlib.util.module_from_spec(spec)
spec.loader.exec_module(TC)


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def git(*a):
    return subprocess.run(['git', '-C', ROOT] + list(a), capture_output=True, text=True,
                          errors='replace').stdout


def main():
    print()
    print('  T1 -- the other theatre, and it is stale in full')
    print()

    # ============================================================ (1) the theatre's own state
    print('  ' + '=' * 74)
    print('  PART 1 -- ⛭ WHAT THE PHYSICS THEATRE SAYS ABOUT ITSELF')
    print('  ' + '=' * 74)
    phys = open(os.path.join(ROOT, 'THE_PHYSICS_REACH.md'), encoding='utf-8').read()
    check('⓵ it declares the walk complete: "THE WALK IS COMPLETE r2544 — every station, and the '
          'class is six-for-six"',
          'THE WALK IS COMPLETE r2544' in phys and 'every station' in phys)
    th = TC.theatre_state()
    rp = {k: v for k, v in th.items() if v[0] == 'THE_PHYSICS_REACH.md'}
    print(f'    station rows in the physics theatre: {sorted(rp)}')
    check(f'⓵ᵇ and every one of its {len(rp)} station rows carries a done marking -- STRUCK, WALKED '
          'or CLOSED', len(rp) == 7 and all(v[1] for v in rp.values()))

    # ============================================================ (2) what OWED carries
    print()
    print('  ' + '=' * 74)
    print('  PART 2 -- ⛔ AND WHAT THE LIST CARRIED, AT THE PARENT COMMIT')
    print('  ' + '=' * 74)
    owed_was = git('show', f'{PARENT}:OWED.md')
    i = owed_was.find('`R-P`, seven arc stations')
    seg = owed_was[i:i + 600]
    check('⓶ at the parent, OWED 609 lists the seven R-P stations and marks six with ⟐ and ①② as '
          '"the earliest unrun"',
          i > 0 and seg.count('⟐') >= 6 and 'the earliest unrun' in seg)
    stale = [s for s in ('①②', '③④', '⑤', '⑥', '⑦', '⑨', '⑩') if s in seg]
    check(f'⓶ᵇ ⛔ and all seven appear in that one segment: {stale}', len(stale) == 7)

    # ============================================================ (3) the same station, same words
    print()
    print('  ' + '=' * 74)
    print('  PART 3 -- ⛔⛭ AND ①② IS THE STATION THAT DOCUMENT ALREADY WROTE THIS ABOUT')
    print('  ' + '=' * 74)
    check('⓷ the physics theatre carries a section headed "THE ①② STRIKE — made r2383, and the '
          'delay is the finding"', 'THE ①② STRIKE — made r2383, and the delay is the finding' in phys)
    check('⓷ᵇ and inside it, the error in the same words OWED later used: the row "read \\"NEXT — '
          'the earliest unrun station\\" while ①② had already been run"',
          'the earliest unrun station' in phys and 'had already been run' in phys)
    check('⛭ ⓷ᶜ *** so the exact phrase OWED uses at r3122 is the phrase that document recorded as '
          'the error at r2383 -- the diagnosis was written, in the right place, about the right '
          'station, in the right words, and the list reproduced it seven hundred revisions later ***',
          'the earliest unrun' in seg and 'the earliest unrun station' in phys
          and 'STRUCK r2383' in phys)

    # ============================================================ (4) ten of fifteen
    print()
    print('  ' + '=' * 74)
    print('  PART 4 -- ⌗ TEN OF FIFTEEN, ACROSS BOTH THEATRES')
    print('  ' + '=' * 74)
    rm_stale = ['Ⓑ', 'Ⓓ', 'Ⓕ']          # L-263's finding, struck at r3148
    check(f'⓸ L-263 found {len(rm_stale)} stale of eight in the mathematics list, and this receipt '
          f'finds {len(stale)} of seven in the physics list -- '
          f'{len(rm_stale) + len(stale)} of fifteen in all',
          len(rm_stale) + len(stale) == 10)
    check('⓸ᵇ and BOTH theatres had written the notice at the site: the mathematics frontmatter on '
          'Ⓕ, and the physics theatre on ①②',
          'carried Ⓕ as owed for forty-eight revisions' in
          open(os.path.join(ROOT, 'THE_MATHEMATICS_REACH.md'), encoding='utf-8').read()
          and 'the delay is the finding' in phys)

    # ============================================================ (5) the gate
    print()
    print('  ' + '=' * 74)
    print('  PART 5 -- ⌗ THE GATE, AND ITS OWN UNDER-MATCH')
    print('  ' + '=' * 74)
    src = open(os.path.join(ROOT, 'corpus', 'check_theatre_currency.py'), encoding='utf-8').read()
    check('⓹ the gate prints its population every run, and FAILS rather than passing when the parse '
          'finds too few stations to be measuring anything',
          'a consistency check that matches nothing is green forever' in src.lower()
          or 'green forever' in src)
    check('⓹ᵇ ⚠ and its first form under-matched: the marker regex required `⟐` at segment end while '
          'the list writes it mid-segment, so it reported ONE station and called six AGREED that it '
          'had not read -- recorded in the gate rather than quietly fixed',
          'reported six stations as AGREED that it had simply not read' in src
          or 'AGREED that it had' in src)
    rc = subprocess.run([sys.executable, os.path.join(ROOT, 'corpus',
                                                      'check_theatre_currency.py')],
                        cwd=ROOT, capture_output=True, text=True, errors='replace',
                        timeout=600)
    check(f'⓹ᶜ and on the repaired tree the gate is green: exits {rc.returncode}, with no station '
          'carried as owed that its theatre records done',
          rc.returncode == 0 and 'no station is carried as owed' in rc.stdout)
    # ** SEEDED both ways, on a sandbox: the gate must fire on a stale entry and pass on a struck one
    import shutil
    import tempfile
    seeds = {}
    for name, owed_line in (('stale', '`R-M`, eight stations: Ⓐ x Ⓑ x Ⓒ x Ⓓ x Ⓔ x Ⓕ x Ⓖ x Ⓗ x '
                                      '`R-P`, seven arc stations: ①② ⟐ ③④ ⟐ ⑤ ⟐ ⑥ ⟐ ⑦ ⟐ ⑨ ⟐ ⑩ ⟐'),
                            ('struck', '`R-M`, eight stations: Ⓐ x Ⓑ x Ⓒ x Ⓓ x Ⓔ x Ⓕ x Ⓖ x Ⓗ x '
                                       '`R-P`, seven arc stations: ①② ✔ ③④ ✔ ⑤ ✔ ⑥ ✔ ⑦ ✔ ⑨ ✔ ⑩ ✔')):
        with tempfile.TemporaryDirectory() as td:
            os.makedirs(os.path.join(td, 'corpus'))
            shutil.copy(os.path.join(ROOT, 'corpus', 'check_theatre_currency.py'),
                        os.path.join(td, 'corpus'))
            for f in ('THE_MATHEMATICS_REACH.md', 'THE_PHYSICS_REACH.md'):
                shutil.copy(os.path.join(ROOT, f), td)
            open(os.path.join(td, 'OWED.md'), 'w', encoding='utf-8').write(owed_line + '\n')
            r = subprocess.run([sys.executable,
                                os.path.join(td, 'corpus', 'check_theatre_currency.py')],
                               cwd=td, capture_output=True, text=True, errors='replace',
                               timeout=600)
            seeds[name] = r.returncode
    check(f'⓹ᵈ SEEDED BOTH WAYS: a list marking the seven ⟐ fails the gate ({seeds["stale"]}), and '
          f'the same list marking them ✔ passes it ({seeds["struck"]}) -- so a green result is a '
          'measurement and not an empty set',
          seeds['stale'] == 1 and seeds['struck'] == 0)

    print()
    print('  ==========================================================================')
    print('  PART 6 -- \u26d4 THE FIFTH MENTION-VERSUS-USE, AND THE VICTIM WAS THE REPAIR')
    print('  ==========================================================================')

    # ** the strike prose MUST quote the stale marker to record what the list said. **
    #   *The gate's first form read that quotation as a fresh claim and held \u2460\u2461 red -- so the
    #    act of documenting the fix re-created the failure it documents.*
    tc = open(os.path.join(ROOT, 'corpus', 'check_theatre_currency.py'),
              encoding='utf-8', errors='replace').read()
    sys.path.insert(0, os.path.join(ROOT, 'corpus'))
    import importlib
    ctc = importlib.import_module('check_theatre_currency')

    check('\u2465 the gate now distinguishes a quoted marker from a used one: un-quoting a bare '
          'marker leaves it visible, un-quoting a quoted one removes it',
          bool(ctc.OWED_MARK.search(ctc.unquote(ctc.CONTROL_USE)))
          and not ctc.OWED_MARK.search(ctc.unquote(ctc.CONTROL_MENTION)))
    check('\u2465\u1d47 and the control is not decorative: control_fires() runs on every invocation '
          'and returns a verdict rather than being asserted in a comment',
          ctc.control_fires() is True and 'if not control_fires():' in tc)
    check('\u2465\u1d9c THE FINDING IS IN THE GATE, not only here: it records that the quotation '
          'belongs to the REPAIR, so the next reader learns why un-quoting is there',
          'MENTION VERSUS USE' in tc and 'the victim' in tc.lower())
    check('\u2465\u1d48 and the cost is NAMED rather than hidden: a genuine owed-marker written '
          'inside quotes would be missed, and the weaker alternative considered is recorded',
          'THE COST, NAMED' in tc and 'weakens the gate everywhere' in tc)

    # ** and the struck OWED row does quote it -- so the situation the gate had to survive is real **
    owed = open(os.path.join(ROOT, 'OWED.md'), encoding='utf-8', errors='replace').read()
    i = owed.find('`R-P`, seven arc stations')
    seg = owed[i:i + 3000]
    check('\u2465\u1d49 and this is not hypothetical: the struck row in OWED itself quotes "the '
          'earliest unrun" while striking the station that carried it',
          '"the earliest unrun"' in seg and '~~\u2460\u2461' in seg)

    print()
    print('  ==========================================================================')
    print('  PART 7 -- \u26a0 A THIRD INSTANCE, INSIDE ONE FILE')
    print('  ==========================================================================')
    math_reach = open(os.path.join(ROOT, 'THE_MATHEMATICS_REACH.md'),
                      encoding='utf-8', errors='replace').read()
    check('\u2466 THE_MATHEMATICS_REACH\'s station table records \u24b8 CLOSED r3154',
          bool(re.search(r'\|\s*~*\*\*\u24b8\*\*~*.*CLOSED', math_reach)))
    check('\u2466\u1d47 while its own candidate-fields list carried \u24b8 as "\u2605 NEXT" -- the same '
          'staleness with no document boundary to cross at all; corrected r3158',
          math_reach.count('\u2605 NEXT') == 1
          and '"\u2605 NEXT"' in math_reach
          and 'CLOSED r3154 (`L-266`)' in math_reach)
    check('\u2466\u1d9c \u2318 AND THE GATE DOES NOT CLAIM THIS ONE: it reads station TABLES, not '
          'prose lists, and its own docstring bounds its reach rather than implying more',
          'WHAT IT CANNOT DO' in tc)
    check('\u2466\u1d48 and the file carried a corrupted heading from r2419 -- "THE FIELDS TO THROW '
          '(candid" spliced before a second copy of itself -- repaired r3158',
          'THE FIELDS TO THROW (candid## ' not in math_reach
          and math_reach.count('## THE FIELDS TO THROW (candidate bakes') == 1)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        for f in FAILED:
            print(f'    - {f[:150]}')
        return 1
    print('  VERDICT: ** the same bookkeeping failure as L-263, in the other theatre, and complete. **')
    print('  *THE_PHYSICS_REACH declares "THE WALK IS COMPLETE r2544 — every station"; OWED 609')
    print('  carries all seven of its stations as owed, one of them as "the earliest unrun".*')
    print('  ⛔ ** And ①② is the station that document already wrote this about: ** its own section is')
    print('     headed "THE ①② STRIKE — made r2383, and the delay is the finding", recording that the')
    print('     row read "the earliest unrun station" while it had already been run.  *The exact')
    print('     phrase OWED uses at r3122 is the phrase recorded as the error at r2383.*')
    print('  ⌗ ** So it is structural, not careless: ** two theatres, two notices written at the site')
    print('     of the error, zero propagation, ten stale entries of fifteen.  *A theatre document is')
    print('     where the work is DONE and OWED is where it is LISTED, and nothing carried a strike')
    print('     between them.*  `check_theatre_currency` is now that carrier.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
