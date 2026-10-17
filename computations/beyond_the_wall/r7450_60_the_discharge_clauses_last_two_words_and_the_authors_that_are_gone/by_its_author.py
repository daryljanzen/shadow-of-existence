#!/usr/bin/env python3
"""r7450 (60) -- `BY ITS AUTHOR`: can any present seat satisfy PO-78's discharge clause's last two words?

   The clause:  "a verdict on every one of the 2,287 with what was read, and every pin whose claim is a
   sentence's MEANING rather than its wording rewritten to what it is for, BY ITS AUTHOR."

   r7447 ⑤ rules the gated MEANING-HELD verdict IS the rewrite.  That ruling is accepted and not
   re-argued.  Three of the clause's four requirements are established by r7442 and r7447 and are
   not re-measured.  This tests the fourth.

   ⛔ THE TEST IS ONE-DIRECTIONAL AND NEEDS NO GENEALOGY.
      If a receipt was added to the tree BEFORE the adjudicating seat's first appearance anywhere in
      the record, then the adjudicator CANNOT be the author.  Nothing has to name who the author was
      -- and reconstructing that across three vanished seat generations would be a second instrument
      built to check a condition that already exists, which is PO-78's own newest face.
      It can only UNDER-count: every CANNOT-BE-AUTHOR is proved, and a key it does not report may
      still be one.  That is the direction a measurement about other seats' work has to err in.

   ⛔ AND THE THIRD STATE IS REPORTED APART AND NEVER FOLDED IN.  A key whose receipt's birth or whose
      adjudicating seat cannot be read is UNATTRIBUTABLE -- not a match, not a mismatch.  r7436's
      rule: an instrument that cannot say must say which nothing it means.

   usage:  python3 by_its_author.py [--seed]
"""
import collections, os, re, subprocess, sys, time

ROOT = subprocess.run(['git', 'rev-parse', '--show-toplevel'], capture_output=True, text=True,
                      cwd=os.path.dirname(os.path.abspath(__file__))).stdout.strip()
BASELINE = os.path.join(ROOT, 'corpus', 'quote_pin_baseline.tsv')

BAND = 3563                      # the revision at which the parity band was taken; this seat's identity dates from it

CANNOT, UNKNOWN, POSSIBLE = 'CANNOT-BE-AUTHOR', 'UNATTRIBUTABLE', 'COULD-BE-AUTHOR'

# the adjudicating seat, off the verdict's own stamp: `rNNNN+<seat>` or a bare `rNNNN`
VERDICT_STAMP = re.compile(r'^r(\d{3,5})(?:\+(cc\d+|\d+))?')
# any revision stamp in a commit subject, with an optional seat suffix
SUBJECT_STAMP = re.compile(r'\br(\d{3,5})(?:\s*\+\s*(cc\d+|\d+)(?:\.\d+)?)?')


def git(*args):
    return subprocess.run(['git', '-C', ROOT] + list(args), capture_output=True, text=True,
                          errors='replace').stdout


def meaning_held():
    """(receipt, literal, verdict_revision, verdict_seat) for every MEANING-HELD baseline row."""
    out = []
    with open(BASELINE, encoding='utf-8') as fh:
        for ln in fh:
            if ln.startswith('#'):
                continue
            f = ln.rstrip('\n').split('\t')
            if len(f) < 7 or f[5] != 'MEANING-HELD':
                continue
            m = VERDICT_STAMP.match(f[6].strip())
            rev = int(m.group(1)) if m else None
            seat = (m.group(2) if m else None)
            out.append((f[0], f[1], rev, seat))
    return out


def first_appearances():
    """seat -> the lowest revision at which that seat's own stamp appears in any commit subject.

    Read from the log and not from a hand table, because a hand table is the thing this revision
    refuses to build."""
    first = {}
    for line in git('log', '--format=%s', '--all').split('\n'):
        for rev, seat in SUBJECT_STAMP.findall(line):
            if not seat:
                continue
            r = int(rev)
            if seat not in first or r < first[seat]:
                first[seat] = r
    return first


def birth(path):
    """the revision at which this file was ADDED, from the earliest add commit's own subject."""
    adds = [s for s in git('log', '--diff-filter=A', '--format=%s', '--', path).split('\n') if s.strip()]
    if not adds:
        return None, None
    subject = adds[-1]                           # the earliest add
    m = SUBJECT_STAMP.search(subject)
    return (int(m.group(1)) if m else None), subject


def classify(birth_rev, seat, seat_first):
    """ONE place decides, and it returns WHICH nothing it means."""
    if birth_rev is None:
        return UNKNOWN, 'the adding commit carries no revision stamp'
    if seat is None:
        return UNKNOWN, 'the verdict carries no seat suffix, so there is no seat to date'
    if seat not in seat_first:
        return UNKNOWN, f'seat {seat} appears in no commit subject, so it cannot be dated'
    if birth_rev < seat_first[seat]:
        return CANNOT, f'born r{birth_rev}, seat {seat} first appears r{seat_first[seat]}'
    return POSSIBLE, f'born r{birth_rev}, seat {seat} first appears r{seat_first[seat]}'


# ---------------------------------------------------------------------------- the seed
def seed():
    first = {'70': 7000, '60': 3563, 'cc66': 7100}
    fails = []

    def chk(name, got, want):
        if got != want:
            fails.append(f'{name}: got {got!r} want {want!r}')

    chk('older than the seat is PROVED',      classify(2543, '70', first)[0], CANNOT)
    chk('younger than the seat is POSSIBLE',  classify(7200, '70', first)[0], POSSIBLE)
    chk('same revision is POSSIBLE',          classify(7000, '70', first)[0], POSSIBLE)
    chk('no birth is UNATTRIBUTABLE',         classify(None, '70', first)[0], UNKNOWN)
    chk('no seat is UNATTRIBUTABLE',          classify(2543, None, first)[0], UNKNOWN)
    chk('undateable seat is UNATTRIBUTABLE',  classify(2543, '99', first)[0], UNKNOWN)
    # a seat cannot predate itself -- the control's own logic, by construction
    chk('a seat never precedes itself',       classify(first['60'], '60', first)[0], POSSIBLE)
    # UNATTRIBUTABLE is never silently a match
    chk('unknown is not possible',            classify(None, None, first)[0] == POSSIBLE, False)

    print(f'seed: {len(fails)} failing of 8 assertions')
    for f in fails:
        print('  FAIL', f)
    return 1 if fails else 0


# ---------------------------------------------------------------------------- the run
def main():
    t0 = time.time()
    print('r7450 (60) -- `BY ITS AUTHOR`: THE DISCHARGE CLAUSE\'S LAST TWO WORDS')
    print('=' * 100)
    print('r7447 ⑤ rules the gated MEANING-HELD verdict IS the rewrite.  That ruling is ACCEPTED and')
    print('is not re-argued.  Three of the clause\'s four requirements are established by r7442 and')
    print('r7447 and are not re-measured here.  This tests the fourth, which nothing ever has.')
    print()

    rows = meaning_held()
    recs = sorted({r[0] for r in rows})
    print(f'THE POPULATION, from the baseline\'s own MEANING-HELD rows')
    print(f'  {len(rows)} keys over {len(recs)} distinct receipts')
    byseat = collections.Counter(r[3] or '(no seat suffix)' for r in rows)
    print(f'  the ADJUDICATING seat, off each verdict\'s own stamp: '
          f'{dict(byseat.most_common())}')
    print('  ⌗ that stamp is WHO ADJUDICATED. The clause asks whose RECEIPT it is, which is the gap.')
    print()

    seat_first = first_appearances()
    print('EACH SEAT\'S FIRST APPEARANCE, read from the log and not from a hand table')
    for s in sorted(seat_first, key=lambda k: seat_first[k]):
        print(f'    r{seat_first[s]:<6} {s}')
    print()

    births, subjects = {}, {}
    for p in recs:
        births[p], subjects[p] = birth(p)
    print(f'EACH RECEIPT\'S BIRTH, from the commit that ADDED it')
    known = [b for b in births.values() if b is not None]
    pre = [p for p, b in births.items() if b is not None and b < BAND]
    print(f'  {len(known)} of {len(recs)} receipts carry a revision stamp on their adding commit')
    print(f'  {len(set(known))} distinct adding revisions')
    print(f'  ⒠ born BEFORE r{BAND}, the revision at which the parity band was taken: '
          f'{len(pre)} of {len(recs)}')
    if known:
        print(f'  the range: r{min(known)} to r{max(known)}')
    print()

    verdicts = collections.Counter()
    detail = []
    for receipt, lit, rev, seat in rows:
        state, why = classify(births[receipt], seat, seat_first)
        verdicts[state] += 1
        detail.append((state, receipt, lit, seat, why))
    print('⒞ THE ANSWER, three states, partitioning the class exactly')
    for s in (CANNOT, POSSIBLE, UNKNOWN):
        print(f'    {s:<16} {verdicts[s]:>4}')
    print(f'    {"total":<16} {sum(verdicts.values()):>4}  of {len(rows)}')
    assert sum(verdicts.values()) == len(rows)
    print()

    # ---- the control: a seat cannot predate itself
    mine = [d for d in detail if d[3] == '60']
    bad = [d for d in mine if d[0] == CANNOT]
    print('⒡ THE CONTROL -- this seat\'s own self-adjudicated keys cannot be CANNOT-BE-AUTHOR')
    print(f'   keys stamped by seat 60 : {len(mine)}')
    print(f'   of them CANNOT-BE-AUTHOR: {len(bad)}')
    if bad:
        print('   ⛔ NON-ZERO. A seat cannot predate itself, so the first-appearance table or the birth')
        print('      read is wrong. THE RUN IS VOID.')
        for d in bad[:5]:
            print(f'      {d[1]}  {d[4]}')
        return 1
    print('   zero, as the logic requires. The run stands.')
    print()

    print('THE SHAPE OF THE PROVED HALF -- which seats adjudicated what they provably did not write')
    prov = collections.Counter(d[3] for d in detail if d[0] == CANNOT)
    for s, n in prov.most_common():
        print(f'    {n:>4}  seat {s}')
    print('  ⌗ AND THAT IS NOT AN ACCUSATION. It is a statement about DATES. Every one of these seats')
    print('    adjudicated a pin in a receipt written by a seat generation that no longer exists, which')
    print('    is the only way the backlog could ever have been worked at all.')
    print()

    if verdicts[UNKNOWN]:
        print('⒟ THE UNATTRIBUTABLE, reported apart and never folded into either verdict')
        for why, n in collections.Counter(d[4] for d in detail if d[0] == UNKNOWN).most_common():
            print(f'    {n:>4}  {why}')
        print()

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'authorship.tsv')
    with open(out, 'w', encoding='utf-8') as fh:
        fh.write('state\tadjudicating_seat\tborn\tseat_first_appears\treceipt\tliteral\n')
        for state, receipt, lit, seat, why in sorted(detail):
            b = births[receipt]
            fa = seat_first.get(seat, '')
            fh.write(f'{state}\t{seat or ""}\t{b if b is not None else ""}\t{fa}\t{receipt}\t{lit}\n')
    print(f'  the full classification written to {os.path.relpath(out, ROOT)} ({len(detail)} rows)')
    print()
    print('⛔ WHAT THIS DOES NOT SAY')
    print('  It does not re-open r7447 ⑤; the ruling stands and this is the act of taking it seriously.')
    print('  It accuses no seat of anything: CANNOT-BE-AUTHOR is about dates, not about care.')
    print('  It names no receipt\'s author -- the test is one-directional so that it never has to.')
    print('  It rewrites no pin, edits no receipt and touches no baseline row.')
    print('  And it does not rule PO-78 discharged. That is the row seat\'s call; this supplies whether')
    print('  the last two words of its discharge clause are satisfiable by anyone now.')
    print()
    print(f'⒢ THE PRICE : {time.time() - t0:.1f}s')
    return 0



# ---------------------------------------------------------------------------- the sound pass
#
# ⛔ THE FIRST RUN IS VOID AND ITS CONTROL IS WHY.  `first_appearances()` above reads the lowest
# revision at which a seat's name appears as an EXPLICIT `+seat` suffix in a commit subject.  That is
# NOT when the seat began: the two main lines write BARE `rNNNN` subjects, so seat 60 dated itself to
# r7106 while the record has it holding the EVEN half since r3563.  It reported 256 of this seat's own
# 289 keys as PROVED not-by-their-author.
#   => A detector for "when did this seat exist" that measures "when did this seat first write its own
#      name in a suffix" is a population narrower than its subject.  It is PO-78's generator, inside
#      the instrument of the revision measuring PO-78's generator, and the control registered in
#      advance is the only thing that caught it.
#
# THE REPAIR IS NOT A BETTER INFERENCE.  It is to read the record's OWN statements about who held what
# and when -- the generator's rule applied the right way round -- and to report every seat the record
# does not date as UNATTRIBUTABLE rather than guess it.

# Every statement the record makes about the halves, quoted from corpus/check_revision_collisions.py
# with its source named.  DATA copied from the record, not an inference about it.
DECLARED = [
    ('54', 'EVEN', 3203, 'check_revision_collisions.py l.390: "54 takes EVEN (0); 57 takes ODD (1)."'),
    ('57', 'ODD',  3203, 'check_revision_collisions.py l.390: "54 takes EVEN (0); 57 takes ODD (1)."'),
    ('59', 'ODD',  3563, 'OTHER_HALF, node 59 r3563 CLAIMS.md: "59 takes ODD, 60 takes EVEN, from r3563 forward."'),
    ('60', 'EVEN', 3563, 'OTHER_HALF, node 59 r3563 CLAIMS.md: "59 takes ODD, 60 takes EVEN, from r3563 forward."'),
    ('61', 'ODD',  4011, 'OTHER_HALF, node 61 r4011: "61 takes over 59 ODD half from r4011 forward."'),
]
# And the statements the record makes ABOUT A RELABEL, which are the hinge:
RELABEL = ('node 61 r4011: "The partition is unchanged; only the name on the odd half is."'
           '   AND node 59 r3563: "60 is the line that has been recording the collisions"'
           ' -- said of a half that l.390 records as 54 holding.')


def sound():
    t0 = time.time()
    print('r7450 (60) -- THE SOUND PASS, AFTER THE CONTROL VOIDED THE FIRST')
    print('=' * 100)
    print("⛔ THE FIRST RUN IS VOID. Its control -- registered in advance -- fired: 256 of this seat's")
    print('   own 289 keys came out PROVED not-by-their-author, and a seat cannot predate itself.')
    print("   THE DEFECT IS THE INSTRUMENT'S AND IT IS THIS ROW'S OWN GENERATOR: my detector measured")
    print('   WHEN A SEAT FIRST WRITES ITS NAME IN A SUFFIX, not when the seat began. The two main')
    print('   lines write BARE subjects, so seat 60 dated itself to r7106 while the record has it')
    print('   holding the EVEN half since r3563. A population narrower than its subject, in the')
    print('   instrument of the revision measuring exactly that -- caught by the control alone.')
    print()
    print("THE REPAIR IS NOT A BETTER INFERENCE. It is to read the record's own statements.")
    print()

    rows = meaning_held()
    recs = sorted({r[0] for r in rows})
    print('THE POPULATION: %d keys over %d distinct receipts' % (len(rows), len(recs)))
    seats = collections.Counter(r[3] or '(none)' for r in rows)
    print('  adjudicating seats: %s' % dict(seats.most_common()))
    print()

    print('WHAT THE RECORD ACTUALLY STATES, quoted with its source')
    for label, half, frm, src in DECLARED:
        print('    %-5s holds %-4s from r%-5d -- %s' % (label, half, frm, src))
    print()
    print("  ⛔ EVERY ONE OF THOSE STATEMENTS IS ABOUT A HALF, NOT ABOUT A SEAT'S EXISTENCE.")
    print('    And the record says in terms that a label MOVES:')
    print('      %s' % RELABEL)
    print()

    dated = set(d[0] for d in DECLARED)
    print('CAN EACH ADJUDICATING SEAT BE DATED FROM THAT?')
    verdict_rows = []
    for seat in sorted(seats, key=lambda s: -seats[s]):
        if seat == '(none)':
            why = 'the verdict carries no seat suffix, so there is no label to date'
        elif seat not in dated:
            why = ('the record makes NO statement about this seat at all -- it names the holders of '
                   'the two halves and this seat is not among them')
        else:
            why = ('the record dates the HALF this label held, and states that a label moves between '
                   'lines, so the date bounds the LABEL and not the author')
        print('    %-8s %4d key(s)  NO -- %s' % (seat, seats[seat], why))
        verdict_rows.append((seat, seats[seat], why))
    print()

    print('⒞ THE ANSWER')
    print('    UNATTRIBUTABLE   %d   of %d' % (len(rows), len(rows)))
    print('    CANNOT-BE-AUTHOR   0')
    print('    COULD-BE-AUTHOR    0')
    print()
    print('  ⇒ `BY ITS AUTHOR` IS NOT DECIDABLE FROM THE RECORD FOR ANY OF THE 538, AND THE REASON IS')
    print('    NOT MISSING DATES. It is that the record identifies lines by LABELS, and states that a')
    print('    label changes hands without ever stating whether a relabel is a change of AUTHOR. The')
    print('    seat label is many-to-one on the author in one direction and one-to-many in the other,')
    print('    and nothing in this corpus has ever checked which.')
    print()
    print("    ⚖ Which is this cycle's own standing guard, arriving where nobody was watching for it:")
    print('      BEFORE TWO STRETCHES ARE IDENTIFIED BY A LABEL, CHECK HOW MANY-TO-ONE THE LABEL IS ON')
    print('      THE OBJECT.')
    print()

    births = {}
    for p in recs:
        births[p], _ = birth(p)
    known = [b for b in births.values() if b is not None]
    pre = [p for p, b in births.items() if b is not None and b < BAND]
    print('⒠ WHAT DOES STAND, BECAUSE IT NEEDS NO SEAT TABLE: WHEN THE RECEIPTS WERE BORN')
    print('    %d of %d carry a revision stamp on their adding commit' % (len(known), len(recs)))
    print('    %d distinct adding revisions, r%d to r%d'
          % (len(set(known)), min(known), max(known)))
    print('    born before r%d, when the parity band was taken: %d of %d' % (BAND, len(pre), len(recs)))
    print()

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'undecidable.tsv')
    with open(out, 'w', encoding='utf-8') as fh:
        fh.write('adjudicating_seat\tkeys\twhy_the_label_cannot_date_the_author\n')
        for seat, n, why in verdict_rows:
            fh.write('%s\t%d\t%s\n' % (seat, n, why))
    print('  written to %s' % os.path.relpath(out, ROOT))
    print()
    print('⛔ WHAT THIS DOES NOT SAY')
    print('  It does not re-open r7447 ⑤. It makes that ruling NECESSARY rather than merely reasonable:')
    print("  if the clause's last two words cannot be decided by anyone, a reading under which the")
    print('  clause is satisfiable is the only reading it can have.')
    print("  It accuses no seat and names no receipt's author -- it establishes that nothing can.")
    print('  It does not build the seat register that would make the clause enforceable. That register')
    print("  -- each seat's first revision, and for every relabel a statement of whether the author")
    print('  changed -- is NAMED here and left to the row seat, because building the fix in the same')
    print('  pass as the measurement that justifies it is how a measurement becomes unfalsifiable.')
    print()
    print('⒢ THE PRICE : %.1fs' % (time.time() - t0))
    return 0


if __name__ == '__main__':
    if '--seed' in sys.argv:
        sys.exit(seed())
    sys.exit(sound() if '--sound' in sys.argv else main())
