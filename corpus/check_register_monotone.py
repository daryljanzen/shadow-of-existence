#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_register_monotone -- does any register row carry LESS than it once did?

⚑ WHY THIS EXISTS, AND IT IS A DEFECT OF THIS SEAT'S OWN MAKING AT `r6993`.

`THE_REGISTER` is APPEND-FORWARD by design: a row's prior state is preserved and each gate
writes the row further, so a row's text only ever grows.  That is a design invariant nobody
had ever checked -- and at `r6993` this seat broke it.

Resolving a merge conflict in that file, the seat compared ONE of the two conflicting lines
against its counterpart, established that side was a strict superset, and then replaced the
WHOLE conflict block with that side.  The block held TWO rows.  The second was `PO-23`, and
the incoming side's copy of it predated two revisions of work: 124,849 characters of row went
back to 116,789, silently, and the next revision was written on top of the reverted row.

⌗ ** THE SHAPE OF THE ERROR IS WORTH MORE THAN THE INSTANCE: A CHECK WAS RUN ON ONE OBJECT AND
  A CONCLUSION WAS DRAWN ABOUT ANOTHER. **  It is the same class as `PO-65` -- a verdict that is
  true of what it examined and silent about what it was taken to license.

⛔ ** AND NOTHING CAUGHT IT. **  `check_frontier_current` reads each row's revision stamp, which
  did not move, so it reported the row current.  A row can lose two revisions of content while
  every gate in the suite stays green, because no gate was comparing the row to its own past.

⇒ WHAT THIS GATE DOES.  For each row id, the maximum length that row has ever had over the
  file's recent history, against its length now.  Shrinking below that maximum fails, and so
  does a row disappearing altogether.  It is a statement about the ROW rather than about the
  file's total size, so growth elsewhere cannot mask a loss here.

⌗ SCOPE, STATED.  `THE_REGISTER` only.  `THE_FRONTIER` is generated from `regen_frontier.py`
  and is checked by regeneration; the other append-forward documents are not covered here and
  saying so is the point -- this gate covers the file whose invariant was broken, and extending
  it is a measurement somebody should make rather than a line somebody should add.
"""
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGET = 'THE_REGISTER.md'

#: How many commits of the file's history to walk.  Bounded for speed: the defect this gate
#: exists for is caught at the commit that makes it, and a bounded window still catches a
#: revert of anything touched in that window.  ⌗ *A revert of something older than the window
#: is not caught, which is stated rather than left to be assumed.*
WINDOW = 200

#: ⛭ RE-BASELINES.  A row may legitimately lose text, and when it does the honest record is not
#: a waived LENGTH but a waived HISTORY: the condensation is a deliberate act at a named commit,
#: and monotonicity resumes from there.  So an entry names the commit at which the row was
#: rewritten, and everything at or before it is ignored for that row alone.
#:
#: ⌗ *A waived length would have been the wrong shape and is worth saying so: it would fire
#:   again the next time the row gained a single character -- an annotation, a withdrawal
#:   marker -- and the remedy would be to edit the number, which teaches a seat to edit numbers
#:   until gates stop complaining.  A re-baseline lets the row keep growing from where it was
#:   condensed, which is what the invariant actually is.*
#:
#: ⛔ ** AND THIS IS NOT A PLACE TO PUT A LOSS. **  Every entry below was verified by walking the
#: row's own length through history and finding the drop AT the commit named, whose subject says
#: what it did.  A row that lost text in a merge drops at a merge commit and belongs nowhere
#: near this table.
#:
#: ⌗ *All three predate the current convention.  Under it -- a strike keeps the row whole, adds
#:   the strike block, and records the prior state in the status column -- a struck row GROWS,
#:   which is why this invariant is the right one going forward and why this table should not
#:   need a fourth entry.*
DECLARED = {
    'PO-30': ('549b7e4124', 'r6758 struck the row and rewrote it as a condensed struck record, '
                            'under the convention then in force; an earlier deliberate '
                            'condensation at r6476 (dd02b80649) is inside the same waived span'),
    'PO-45': ('204e849c5a', 'r6733 struck the row and rewrote it as a condensed struck record, '
                            'under the convention then in force'),
    #: ⛭ r7465, and it IS a fourth entry the note above hoped not to need -- so the reason is
    #:   given at length rather than in a clause.  This row did not lose text; it discharged a
    #:   condensation its OWN clause set.  69's stock-take at r7443 added, as the third part of
    #:   the amended discharge, that at the strike the row collapses to one state, measured then
    #:   at 813,685 characters, 32 copies of the discharge clause and 12 superseded blocks.  By
    #:   the strike it stood at 852,992.  Daryl's ruling at r7465 struck the row -- its object
    #:   was met, and what kept its last condition open were defects in the apparatus rather
    #:   than in the corpus -- and the condensation ran with it.
    #:   ⌗ The convention above (a strike GROWS the row) is right for a row whose history is the
    #:   finding.  Here the history is 33 faces of an instrument class, which is consolidation-plan
    #:   material by the one-state rule; the four rules that outlive the row are carried in the
    #:   struck record itself, and nothing is lost -- the full row is at 722fcf0e7c.
    'PO-78': ('f5141b139d', 'r7465 struck the row on Daryl\'s ruling and collapsed it to one '
                            'state, discharging the condensation clause the row itself set at '
                            'r7443; 852,992 -> 2,944 characters, the record going to the '
                            'consolidation ledger and the full row kept at the commit named'),
    #: ⛭ 69, on taking the coordinating seat.  Daryl's order (d) is that the register carries one
    #:   state -- the question, what is known, what settles it -- with the history in the
    #:   consolidation ledger.  So a strike from here condenses rather than grows, and each
    #:   condensation is entered here against the commit that made it, its full prior row kept at
    #:   that commit's parent and pointed to from THE_CONSOLIDATION_LEDGER.md.
    'PO-90': ('8fb615b2cd', 'r7471 struck the row on its own termination clause (70\'s measurement) '
                            'and wrote it as one state; the full prior row is at the parent '
                            'of the commit named and is pointed to from the consolidation ledger'),
    'PO-88': ('e496e66559', 'r7487 struck the row on its own termination clause (cc66\'s computation) '
                            'and wrote it as one state; the full prior row is at the parent'),
    'PO-92': ('e496e66559', 'r7487 struck the row on its own termination clause (60\'s argument, a '
                            'stated limit) and wrote it as one state; the full prior row is at the parent'),
    'PO-93': ('e496e66559', 'r7487 rewrote the live row to one state on 60\'s one-cluster result; the '
                            'full prior row is at the parent'),
    'PO-24': ('e496e66559', 'r7487 rewrote the live row to one state on 70\'s off-tail tilt; the full '
                            'prior row, 19,853 characters, is at the parent'),
}

ROW = re.compile(r'\| ~?~?\*\*((?:PO|L|C)-?\d+)\*\*')


def rows(text):
    """id -> line length, for every register row in `text`."""
    out = {}
    for line in text.split('\n'):
        m = ROW.match(line)
        if m:
            out[m.group(1)] = len(line)
    return out


def git(*args):
    return subprocess.run(('git',) + args, cwd=ROOT, capture_output=True, text=True)


def _row_line(text, rid):
    """The whole register line for `rid`, or '' if it is not there."""
    for line in text.split('\n'):
        m = ROW.match(line)
        if m and m.group(1) == rid:
            return line
    return ''


def _row_text_at(sha, rid):
    r = git('show', '%s:%s' % (sha, TARGET))
    return _row_line(r.stdout, rid) if r.returncode == 0 else ''


def _row_text_now(rid):
    with open(os.path.join(ROOT, TARGET), encoding='utf-8') as fh:
        return _row_line(fh.read(), rid)


def main():
    path = os.path.join(ROOT, TARGET)
    if not os.path.exists(path):
        print('  check_register_monotone -- %s is absent; nothing to check.' % TARGET)
        return 0

    with open(path, encoding='utf-8') as fh:
        now = rows(fh.read())

    print()
    print('  REGISTER MONOTONICITY -- does any row carry LESS than it once did?')
    print()

    #: ⛔ `--full-history` IS LOAD-BEARING AND ITS ABSENCE DEFEATED THIS GATE'S FIRST DRAFT.
    #: `git log -- <path>` returns SIMPLIFIED history: across a merge it can keep one side
    #: and prune the other when the result is the same, so a commit that touched the file is
    #: simply absent from the listing.  The draft without this flag walked 370 commits where
    #: the full history has 400 -- **and the pruned set included the very commit holding the
    #: peak this gate was written to restore**, so it reported green on the exact defect it
    #: exists for, seeded.
    #: ⌗ *Which is this file's own lesson landing on this file: a tool answering about one
    #:   thing -- the history git thinks is interesting -- was taken to answer about another,
    #:   every commit that touched the file.  Third instance in one revision.*
    log = git('log', '--full-history', '--format=%H', '-n', str(WINDOW), '--', TARGET)
    if log.returncode != 0:
        print('    [skip] git history is unavailable here, so there is nothing to compare')
        print('           against.  ⌗ That is a real gap and not a pass: this gate needs a')
        print('           repository.  Under a shallow checkout it says so rather than')
        print('           reporting green, which is the class it was built for.')
        return 0

    commits = [c for c in log.stdout.split('\n') if c.strip()]
    if not commits:
        print('    [skip] %s has no recorded history yet.' % TARGET)
        return 0

    #: `commits` is newest-first, so a row's waived span is every commit from the named
    #: re-baseline onwards in that listing -- i.e. that commit and everything older.
    waived = {}
    for rid, (sha_pref, _why) in DECLARED.items():
        hit = [i for i, c in enumerate(commits) if c.startswith(sha_pref)]
        if not hit:
            print('    [note] %s\'s re-baseline %s is older than the %d-commit window, so its'
                  % (rid, sha_pref, WINDOW))
            print('           whole history here is already outside comparison.')
            waived[rid] = -1   # nothing to waive: the drop is out of window anyway
        else:
            waived[rid] = hit[0]

    best = {}          # id -> (max length ever seen, the commit it was seen at)
    for i, sha in enumerate(commits):
        blob = git('show', '%s:%s' % (sha, TARGET))
        if blob.returncode != 0:
            continue   # the file did not exist at that commit
        for rid, n in rows(blob.stdout).items():
            if rid in waived and waived[rid] >= 0 and i >= waived[rid]:
                continue   # at or before this row's declared re-baseline
            if rid not in best or n > best[rid][0]:
                best[rid] = (n, sha)

    print('    %d row(s) now; %d commit(s) of history walked; %d row(s) ever seen'
          % (len(now), len(commits), len(best)))

    for rid in sorted(DECLARED):
        print('    [re-baselined] %-7s at %s' % (rid, DECLARED[rid][0]))
        print('                   %s' % DECLARED[rid][1])

    # ⛭ r7353 (66): THE INVARIANT IS ABOUT CONTENT AND IT WAS MEASURED IN CHARACTERS.
    #   A row that drops a VERBATIM DUPLICATE of text it still carries has lost no content, and under a
    #   character measure it reds exactly like a row that lost a paragraph.  THE_REGISTER's PO-23 row
    #   carries a 2,205-char block twice; 70's RC3 at r7351 is a repair that CANNOT be made because no
    #   span inside that block is unique, and clearing it necessarily shrinks the row.
    #   ⇒ A shrink is measured against DISTINCT content: collapse every maximal verbatim-duplicated run
    #   in each version and compare what is left.  Dropping a second copy leaves the distinct size
    #   unchanged; dropping a paragraph lowers it, and still reds.
    #   ⌗ r7351 tried this with a shingle-containment test and it was WRONG: the row legitimately
    #   rewrites its live-clause marker every revision, so old shingles are absent by design and every
    #   shrink looked like a loss.  Containment asks "is the old text still there"; the invariant asks
    #   "does the row carry as much".  Those differ exactly where the row is edited rather than appended.
    #   PRICED, per r7349: runs ONLY on rows that shrink, so it costs nothing on a green tree; measured
    #   at 1.6 s for one 287k-character row.
    def _distinct_size(text, w=200):
        """len(text) less the extra copies of every maximal verbatim-duplicated run."""
        if len(text) <= w:
            return len(text)
        seen, extra, i = {}, 0, 0
        while i <= len(text) - w:
            sub = text[i:i + w]
            j = seen.get(sub)
            if j is None:
                seen[sub] = i
                i += 1
                continue
            e1, e2 = j + w, i + w
            while e2 < len(text) and text[e1] == text[e2]:
                e1 += 1
                e2 += 1
            extra += e2 - i
            i = e2
        return len(text) - extra

    shrunk, vanished, dedup = [], [], []
    for rid, (peak, sha) in sorted(best.items()):
        if rid not in now:
            vanished.append((rid, peak, sha))
        elif now[rid] < peak:
            old_text, new_text = _row_text_at(sha, rid), _row_text_now(rid)
            if old_text and new_text and _distinct_size(new_text) >= _distinct_size(old_text):
                dedup.append((rid, peak, now[rid], sha,
                              _distinct_size(old_text), _distinct_size(new_text)))
            else:
                shrunk.append((rid, peak, now[rid], sha))

    for rid, peak, cur, sha, od, nd in dedup:
        print()
        print('    [DE-DUPLICATED] %s  is %d chars against %d at %s, and NOTHING WAS LOST:'
              % (rid, cur, peak, sha[:10]))
        print('                    distinct content %d then, %d now -- the %d characters it dropped'
              % (od, nd, peak - cur))
        print('                    were verbatim second copies of text the row still carries.')

    if not shrunk and not vanished:
        print()
        print('    every row carries at least as much CONTENT as it ever did.')
        print('  ⌗ Append-forward is a DESIGN invariant of this file, and an invariant nobody')
        print('    checks is an invariant a merge can quietly undo.')
        return 0

    print()
    print('  ⛔ %d ROW(S) CARRY LESS THAN THEY ONCE DID.' % (len(shrunk) + len(vanished)))
    print()
    for rid, peak, cur, sha in shrunk:
        print('     [FAIL] %s  is %d chars; it was %d at %s  (lost %d)'
              % (rid, cur, peak, sha[:10], peak - cur))
    for rid, peak, sha in vanished:
        print('     [FAIL] %s  is GONE; it was %d chars at %s' % (rid, peak, sha[:10]))
    print()
    print('     Recover the row from the commit named beside it, merge anything the current')
    print('     copy adds, and write the result back -- then re-run.  ⌗ *Do not resolve this')
    print('     by declaring the shrink: `DECLARED` is for a shrink somebody chose, and a row')
    print('     that lost text in a merge is not one.*')
    print()
    print('  ⚠ AND IF A MERGE PRODUCED IT, THE LESSON IS THE ONE IN THIS FILE\'S HEAD: a check')
    print('    run on one object licenses a conclusion about that object and no other.  When a')
    print('    conflict block holds several rows, every row in it is its own comparison.')
    return 1


if __name__ == '__main__':
    sys.exit(main())
