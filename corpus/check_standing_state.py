#!/usr/bin/env python3
"""
check_standing_state -- is a row's STANDING STATE its own derivation, or a stale copy?

ORDERED at `r7457` ⑥, from `r7456`'s Ⓒ.  Registered-before-built at
`computations/beyond_the_wall/r7458_60_the_standing_state_against_its_own_derivation/`.

THE DEFECT IT WATCHES.  `PO-78`'s standing state is re-emitted IN FULL each revision
rather than amended, so the row carries 29 distinct values of ONE field as live text
with nothing marking which is current except position.  `r7453` reached for the `r7257`
copy of the right field and got the right population at the wrong date.  A seat reading
the row gets whichever copy its eye lands on.

WHAT THIS ASSERTS, and it is one thing: ** the value each series carries in the row's
LIVE STANDING STATE equals the value DERIVED from the row. **  The derivation is the
authority; the standing state is a copy of it.

⚠ KEYED ON THE LIVE BLOCK, NOT ON THE FILE.  `r7457` ⑥ⓑ names this as the whole
difficulty: read the file and the gate meets one of the 28 superseded values and
disagrees with a correct row.  The live/superseded boundary is the row's own marker,
`⛭ THE LIVE CLAUSE (SET rNNNN)`, and the block runs from the LAST such marker to the
end of the row.

⌗ THE DERIVATION IS NOT REIMPLEMENTED HERE.  `r7445`'s rule, promoted at `r7447`: a
reimplementation of a predicate is a second instrument and it will disagree.  So this
imports `r7456`'s `two_counts.py` and calls its `harvest`, its `row_of` and its SERIES
table.  If that file moves, this gate fails loudly rather than silently diverging.

⌗ AND THE READER IS WIDENED, which is the correction `r7457` ④ names.  `r7456`'s
`register_rows` required the BOLD row form and saw 11 of the register's 82 rows, missing
all 71 struck ones -- including the row it blamed and the row that was hit.  An
instrument prescribing a remedy for its own blind spot aims it at the object, because
the blind spot is the one thing it cannot see.  Both forms are read here.
"""
import os, re, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DERIV = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                     'r7456_60_the_rows_two_counts_derived_rather_than_read')
sys.path.insert(0, DERIV)
try:
    import two_counts as D
except Exception as exc:                                    # pragma: no cover
    print('\n  ⛔ THE DERIVATION THIS GATE CALLS IS NOT IMPORTABLE: %s' % exc)
    print('     %s/two_counts.py' % os.path.relpath(DERIV, ROOT))
    print('     This gate asserts nothing of its own; it compares the row against that')
    print('     derivation.  A missing derivation is a RED, not a skip.')
    sys.exit(1)

REG = 'THE_REGISTER.md'
WATCHED = 'PO-78'
LIVE_MARKER = re.compile(r'THE LIVE CLAUSE \(SET r(\d{4})\)')

# ** ROWS IN BOTH FORMS. **  Bold is a live row; strikethrough is a struck one.
ROW_ANY = re.compile(r'^\|\s*(?:\*\*|~~\**)\s*((?:PO|L)-[0-9]+)')


def register_row_ids(text):
    live, struck = [], []
    for ln in text.split('\n'):
        m = ROW_ANY.match(ln)
        if not m:
            continue
        (struck if ln.lstrip('| ').startswith('~~') else live).append(m.group(1))
    return live, struck


def live_block(flat):
    """From the LAST live-clause marker to the end of the row."""
    marks = list(LIVE_MARKER.finditer(flat))
    if not marks:
        return None, 0, None
    last = marks[-1]
    return flat[last.start():], len(marks), int(last.group(1))


def compare(flat):
    """(derived, stated, block, nmark, setrev) -- the pure comparison the controls run.

    \u2318 THE FIRST DRAFT OF THIS FUNCTION WAS VACUOUS AND ITS OWN CONTROLS SAID SO.
      It derived each series as "the last site anywhere in the row" and compared that
      with "the last site in the LIVE BLOCK".  The live block is the END of the row, so
      both read the SAME site: ** the gate compared a value with itself **, and both
      registered controls -- a one-off mutation and a boundary moved onto a superseded
      copy -- stayed GREEN.  That is this row's generator inside the gate built to catch
      it.
    \u21d2 The two roles are now read in the two DIFFERENT WORDINGS the row uses for them,
      which is what makes the comparison independent at all: the ANNOUNCEMENTS over the
      whole row are the authority, the live block's SUMMARY is the copy.
    """
    block, nmark, setrev = live_block(flat)
    derived, stated = {}, {}
    for name in D.SERIES:
        if name.startswith('MEMBER'):
            derived[name] = D.member_announced(flat)[0]
            stated[name] = D.member_summarised(block)[0] if block is not None else None
        elif name.startswith('FAMILY'):
            fam = [h for h in D.harvest(flat, 'ROW')[0] if h['series'] == name]
            famb = ([h for h in D.harvest(block, 'BLK')[0] if h['series'] == name]
                    if block is not None else [])
            derived[name] = fam[-1]['val'] if fam else None
            stated[name] = famb[-1]['val'] if famb else None
        else:
            derived[name] = None
            stated[name] = None
    return derived, stated, block, nmark, setrev


def stale_series(derived, stated):
    """The series whose live-block copy disagrees with the derivation."""
    out = []
    for name in D.SERIES:
        if name.startswith('FACE'):
            continue
        d, st = derived[name], stated[name]
        if d is not None and st is not None and d != st:
            out.append((name, d, st))
    return out


def main():
    t0 = time.time()
    with open(os.path.join(ROOT, REG), encoding='utf-8') as fh:
        reg_text = fh.read()
    live_ids, struck_ids = register_row_ids(reg_text)

    print('\n  STANDING STATE vs ITS OWN DERIVATION -- is the row\'s copy of a count current?')
    print('    the register carries %d row(s): %d live, %d struck'
          % (len(live_ids) + len(struck_ids), len(live_ids), len(struck_ids)))
    print('    ⌘ both forms are read.  r7456\'s reader required the bold form and saw')
    print('      %d of them, which is the blind spot r7457 ④ names and this fixes.'
          % len(live_ids))

    flat = D.row_of(REG)
    if not flat:
        print('\n  ⛔ [FAIL] %s carries no %s row.' % (REG, WATCHED))
        return 1

    block, nmark, setrev = live_block(flat)
    print('\n    %s: %d flattened character(s); %d live-clause marker(s)'
          % (WATCHED, len(flat), nmark))
    if block is None:
        print('\n  ⛔ [FAIL] no `THE LIVE CLAUSE (SET rNNNN)` marker, so the live/superseded')
        print('     boundary cannot be found and this gate cannot be keyed.  The remedy is')
        print('     in the row: mark the live clause.')
        return 1
    print('    the LIVE BLOCK is the last of them, SET r%d: %d character(s), %.1f per cent'
          % (setrev, len(block), 100.0 * len(block) / max(1, len(flat))))

    derived, stated, block, nmark2, _sr = compare(flat)
    ann, ann_sites = D.member_announced(flat)
    print('    the member total is derived from %d ANNOUNCEMENT site(s) over the whole row'
          % len(ann_sites))
    print('      and compared with the live block\'s SUMMARY -- two different wordings, so')
    print('      the comparison is not a value against itself.')

    # ** THREE STATES, NOT TWO. **  r7422 and r7436 are this seat's own findings that a
    # resolver must report NOT-PROBED as its own state rather than folding it into a
    # verdict.  The first draft of this gate folded two of them and fired twice on a
    # correct tree.  CURRENT / STALE / ABSENT, and ABSENT is not a failure.
    print("\n    %-46s %-9s %-9s" % ('series', 'derived', 'stated'))
    fails, absent, compared = [], [], 0
    for name in D.SERIES:
        d, s = derived[name], stated[name]
        if name.startswith('FACE'):
            # \u2317 ASSERTED OF NOTHING, BY DESIGN.  A face is an ordinal inside a member
            #   and the series has no global total, so there is no copy to be current.
            #   The first draft read any face value in the live block as a global one and
            #   fired on "member 91's third face", which is correct prose -- the gate
            #   asserting about the one series its own registration said it must not.
            print("    \u2317 %-44s %-9s %-9s  %s"
                  % (name[:44], d if d is not None else '-', '(n/a)',
                     'ordinal within a member; no total, so nothing to compare'))
            continue
        if d is None:
            mark, note = '\u26d4', 'the derivation finds no value for this series'
            fails.append((name, d, s, note))
        elif s is None:
            mark, note = '\u2317', 'ABSENT -- the live block restates no value; reported, not failed'
            absent.append(name)
        elif d != s:
            mark, note = '\u26d4', 'THE COPY IS STALE -- the row states a value it no longer has'
            fails.append((name, d, s, note))
        else:
            mark, note = '\u2713', 'the copy is current'
            compared += 1
        print("    %s %-44s %-9s %-9s  %s"
              % (mark, name[:44], d if d is not None else '-', s if s is not None else '-', note))

    # ** THE GUARD THAT KEEPS `ABSENT` FROM EMPTYING THE GATE. **  A standing state that
    #   restates NOTHING would otherwise pass by carrying no copy at all.
    if compared == 0 and not fails:
        print("\n  \u26d4 [FAIL] the live block restates NO series value, so this gate")
        print("     asserts nothing.  A standing state that carries no copy cannot be")
        print("     checked against the derivation, and silence is not agreement.")
        print("\n  price %.2fs" % (time.time() - t0))
        return 1
    if absent:
        print("\n    \u2317 %d series ABSENT from the live block, reported and not failed: %s"
              % (len(absent), ', '.join(n.split(' ')[0] for n in absent)))
        print("      Requiring the row to carry a field it has never carried would be this")
        print("      gate writing the row rather than reading it.")

    all_mem = D._scan(flat, D.SUMMARY) + D._scan(flat, D.ANNOUNCE)
    blk_mem = D._scan(block, D.SUMMARY) if block is not None else []
    print('\n    ⌘ %d distinct member value(s) stand in the row as live text; the gate'
          % len({v for _p, v, _q in all_mem}))
    print('      reads only the %d SUMMARY site(s) in the LIVE BLOCK, which is r7457 ⑥ⓑ,'
          % len(blk_mem))
    print('      and takes its authority from the %d ANNOUNCEMENTS over the whole row --'
          % len(ann_sites))
    print('      which is how the comparison avoids being a value against itself.')

    if fails:
        print('\n  ⛔ [FAIL] %d series whose standing state is not its derivation:' % len(fails))
        for name, d, s, note in fails:
            print('      %-44s derived %s, stated %s -- %s'
                  % (name[:44], d, s, note))
        print('\n     THE REMEDY IS IN THE ROW AND NOT IN THIS GATE: write the derived value')
        print('     into the live clause.  ⌗ The derivation is the authority; the standing')
        print('     state is a copy, and a copy that disagrees is the defect this row names.')
        print('\n  price %.2fs' % (time.time() - t0))
        return 1

    print('\n  every series\' standing state is the value derived from the row.')
    print('  ⌘ This gate says the COPY is current.  It says nothing about whether the')
    print('    derived value is RIGHT -- that is the row\'s own adjudication, and no gate')
    print('    reaches it.')
    print('\n  price %.2fs' % (time.time() - t0))
    return 0


if __name__ == '__main__' and '--seed' not in sys.argv:
    sys.exit(main())



# ============================================================================
# THE CONTROLS.  Registered at PREDICTION.md Ⓥ①–Ⓥ③ before this file existed.
# A gate whose assertion cannot be made to FAIL on a counter-example asserts nothing,
# which is this row's own subject; so each control hands `compare` a mutated row.
# ============================================================================
def seed():
    fails = []

    def ck(name, cond):
        print('  %s %s' % ('✓' if cond else '⛔', name))
        if not cond:
            fails.append(name)

    with open(os.path.join(ROOT, REG), encoding='utf-8') as fh:
        reg_text = fh.read()
    live_ids, struck_ids = register_row_ids(reg_text)
    flat = D.row_of(REG)
    derived, stated, block, nmark, setrev = compare(flat)

    print('SEED AND CONTROLS')
    ck('the row is found and the live-clause marker is unique', bool(flat) and nmark == 1)
    ck('the live block is a small tail of the row, not the file',
       block is not None and 0 < len(block) < 0.25 * len(flat))
    ck('on the tree as it stands, nothing is stale', not stale_series(derived, stated))

    # Ⓣ③ THE REACH CONTROL -- the one r7456 failed.
    ck('Ⓣ③ the widened reader sees both row forms (82 = 11 live + 71 struck)',
       len(live_ids) + len(struck_ids) == 82 and len(live_ids) == 11)
    ck('Ⓣ③ and it names the LIVE row this gate watches', WATCHED in live_ids)
    ck('Ⓣ③ and the STRUCK row r7456 could not see at all', 'PO-75' in struck_ids)

    # Ⓣ② THE POSITIVE CONTROL -- mutate the live block's stated value by one.
    mem = [n for n in D.SERIES if n.startswith('MEMBER')][0]
    live_val = stated[mem]
    if live_val is None:
        ck('Ⓣ② a stated member value exists to mutate', False)
    else:
        i = flat.rfind('THE LIVE CLAUSE (SET r')
        head, tail = flat[:i], flat[i:]
        # ⌗ MUTATE THE SITE THE GATE ACTUALLY READS.  The first version of this control
        #   mutated the FIRST summary site in the block while the gate reads the LAST,
        #   so a correct gate stayed green and the control read as the gate's failure.
        #   A control pointed at the wrong site of the right object is this row's own
        #   shape, and it is recorded rather than quietly retargeted.
        sites = D.member_summarised(tail)[1]
        pos, val = sites[-1][0], sites[-1][1]
        seg = tail[pos:pos + 80]
        bad = tail[:pos] + re.sub(r'\b%d\b' % val, str(val + 1), seg, count=1) + tail[pos + 80:]
        ck('Ⓣ② the mutation changed the LAST summary site, the one the gate reads',
           bad != tail)
        d2, s2, _b, _n, _r = compare(head + bad)
        ck('Ⓣ② ONE-OFF IN THE LIVE BLOCK GOES RED', bool(stale_series(d2, s2)))

    # Ⓣ① THE SUPERSEDED-LEAK CONTROL -- move the live boundary back onto a stale copy.
    sup = flat.find('FIFTY-SEVEN blindness members')
    if sup < 0:
        ck('Ⓣ① a superseded copy exists to point the boundary at', False)
    else:
        moved = (flat[:sup] + 'THE LIVE CLAUSE (SET r7257). '
                 + flat[sup:sup + 1200])
        d3, s3, _b, n3, _r = compare(moved)
        ck('Ⓣ① the boundary moves to the stale copy', n3 >= 1)
        ck('Ⓣ① A STALE LIVE BLOCK GOES RED -- the gate reads the BLOCK, not the file',
           bool(stale_series(d3, s3)))

    print('\n  %d assertion(s) failing' % len(fails))
    return fails


if __name__ == '__main__' and '--seed' in sys.argv:
    seed()
