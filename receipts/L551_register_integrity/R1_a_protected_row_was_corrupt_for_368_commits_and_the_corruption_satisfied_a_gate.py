#!/usr/bin/env python3
# ⛔⛭⛭ THE `RERUNNABLE: NO — POINT-IN-TIME` MARK WAS REMOVED HERE AT r3126 (`L-255`), AND IT
# ** WAS NOT REMOVED BECAUSE THE CONVENTION IS WRONG BUT BECAUSE THE DIAGNOSIS UNDER IT WAS. **
# r2902 read: *"This receipt verified a REPAIR at its own revision.  Its checks compare the tree
# against a state that later legitimate edits change, so it CANNOT be re-run green and a red
# result here is not a defect."*  ⇒ *** The second half is false.  These checks compared a
# SHA-pinned pre-state against a WORKING-TREE post-state; a repair's post-state is a fact about
# the commit that made it, and pinning both ends verifies the same repair forever.  r3125 pinned
# them and all three now exit 0. ***
#   ⇒ ** AN EXEMPTION IS A CLAIM -- "no repair exists for this failure" -- and r2802 already named
#     the class: *"'not mechanically fixable' is a claim, and it is the one kind a node is never
#     asked to defend."*  It was wrong for every instance it was written for. **
#   ⌗ `corpus/check_rerunnable_honest.py` now RUNS every marked receipt: exit 0 fails the gate.
"""R1 -- `PO-4`'s row in `PROTECTED_OPEN.md` was CORRUPT for 368 commits, the corruption was a merge
artefact of the class `CLAIMS.md` already records, and it was SATISFYING a live gate rather than
tripping one.  Three further rows carried a second defect, and one of those three is mine.

** ⛔⛭⛭ ⓵ WHAT WAS WRONG. **  A protected row is `| PO-n | object | target | sources | status |`.
`PO-4`'s OBJECT column ran to *** 5069 characters *** -- against ** 106 ** for `PO-6` and ** 182 **
for `PO-3` -- because the whole status narrative had been dumped into it, three times over:

  * the object text itself duplicated: `**The colour and isospin structure** The colour and isospin
    structure**`, *** the second copy missing its opening `**` ***;
  * a ** 1629-character block appearing twice **, the copy beginning *** mid-clause *** at
    `; only the sector is not built`;
  * and a ** third partial copy beginning MID-WORD **, at `s the one geometric opening left`.

  ⌗ *** A fragment that starts mid-word is not an editing slip.  It is the signature of a three-way
    merge resolving a very long single-line cell by interleaving *** -- and `CLAIMS.md` already
    records exactly this class twice, at r2434 and c54.194, both times as ** duplicate ROWS **.
    *** This is the same failure arriving INSIDE a cell, where no ID gate can see it. ***

** ⓶ WHEN, AND HOW LONG. **  `git log -S` puts it at ** r2427 **, the `c54.163 -> c54.178`
absorption -- whose own commit message reports "the ID collision fired".  *** It fired on the rows
and missed the cell, and the cell stood 368 commits. ***

** ⛔⛔ ⓷ AND THE PART THAT MAKES IT WORSE THAN A COSMETIC DEFECT: IT SATISFIED A GATE. **
`corpus/check_family_pointers.py` reads a row's OBJECT column and asks whether the ledger family
pointing at it shares a distinctive content word.  *** With a 5069-character object, a family matches
on sheer VOLUME. ***  Measured here both ways: against the corrupt object and against the repaired
one.  ⇒ ** So the corruption was not merely unnoticed by the gates -- it was making one of them
pass. **

** ⓸ AND A SECOND DEFECT IN THREE MORE ROWS, ONE OF WHICH IS MINE. **  `PO-6`, `PO-10` and `PO-11`
split into ** 9, 9 and 29 ** cells instead of seven, because unescaped math bars -- `$|T|^2+|R|^2$`,
`$x^{1/2\\pm i|\\nu|}$` -- read as column separators.  ⇒ *** `PO-11` stood at 15 cells before this
fork touched it and at 29 after c54.214: I did not introduce the class, and I nearly doubled its
worst instance. ***
  ⌗⌗ ** AND THAT IS THE SAME DEFECT `check_receipts` GATES FOR IN `receipts/INDEX.md` -- WHERE IT
    CAUGHT ME, TWO REVISIONS EARLIER. **  *c54.214's INDEX row carried `|T|^2+|R|^2=1` unescaped and
    the column lint failed the turn; the identical text went into a `PROTECTED_OPEN` cell in the
    same revision and nothing looked.*  ⇒ *** Same hand, same session, same mistake: caught in one
    file and silent in the other, and the ONLY difference is that one file has a column gate. ***

** ⓹ REPAIRED, AND THE REPAIR IS CONTENT-PRESERVING.  ** The object column is restored to its object,
the duplicated blocks are dropped, the math bars are escaped.  *** Verified that not one distinct
word is lost -- at file level and row by row. ***

** ⛔ CONTROL -- AND IT SETS THE DETECTOR'S THRESHOLD RATHER THAN LEAVING IT GUESSED. **  A
"repeated block inside a cell" detector at ** 80 characters ** flags `PO-2`, `PO-3` and `PO-5` as
well, and all three are ** legitimate re-quotation ** -- a cell quoting the same sentence twice
because two revisions worked it.  *One of the three is this fork's own c54.216 addition.*  ⇒ *** Only
at 400 characters does `PO-4` stand alone.  The base rate is three, the finding is one, and a
detector reported without its base rate would have claimed four. ***

WHAT IS NOT CLAIMED.  ** Not that a gate should be built ** -- `PROTECTED_OPEN` is the observer
line's register and what a column lint should accept there is its call; this reports the hole and
repairs the damage.  ** Not that the r2427 merge was careless ** -- its own message says the ID gate
fired, so the merge was being watched; what was missing was anything that looks INSIDE a cell.
** Not that the other three repeats are defects ** -- the control says they are not.  ** And no
verdict is changed ** -- every word of every row survives, `PO-4` stays open, and this touches
structure and not content.

Written c54.217, `L-551`.  Stated for reversal.
"""
# ** r2901: this receipt's FAILING check is a POINT-IN-TIME. **
# *** verified a REPAIR at its own revision; every later legitimate edit to a protected row breaks the word-preservation check, and this session made hundreds. ***
# ⌗ The receipt is correct about what it did; the check cannot be re-run green.
import collections
import os
import re
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []
SPL = re.compile(r'(?<!\\)\|')
ROW = re.compile(r'\|\s*~*\*\*(PO-[\w-]+)\*\*~*\s*\|')


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def git(*args):
    return subprocess.run(['git', '-C', ROOT] + list(args),
                          capture_output=True, text=True).stdout


def rows_of(text):
    out = {}
    for l in text.split('\n'):
        m = ROW.match(l)
        if m:
            out[m.group(1)] = l
    return out


def words(t):
    return re.findall(r"[A-Za-z][A-Za-z'-]{3,}", t)


def longest_repeat(t, minlen):
    lo, hi, best = minlen, len(t)//2, None
    while lo <= hi:
        mid = (lo + hi)//2
        seen, found = {}, None
        for a in range(len(t) - mid + 1):
            sub = t[a:a+mid]
            if sub in seen:
                found = (mid, seen[sub], a, sub)
                break
            seen[sub] = a
        if found:
            best, lo = found, mid + 1
        else:
            hi = mid - 1
    return best


def main():
    print()
    print('  R1 -- was a protected row corrupt, and did anything look?')
    print()

    # AMENDED r3125 (`L-253`).  ** `before` WAS ALREADY PINNED TO A SHA AND `now` WAS NOT, so the
    # ** claim drifted from "this repair lost no word" to "no edit since has lost a word". **
    # *The second is a much stronger claim and the corpus never made it: `PROTECTED_OPEN` has since
    # had 19,753 bytes of cross-row duplication removed (r2832b) and been closed with fourteen rows
    # struck (r3001).  Words legitimately left the file, and this check called that a repair defect.*
    #   ⇒ *** A pin on one side and a live read on the other is not a comparison, it is a moving
    #       target.  Both ends are pinned; the live half is asserted separately below. ***
    REPAIRED = 'a83455b4844363ead3024a8fdaeef295627e5735'          # c54.217, where the repair landed
    now = git('show', REPAIRED + ':PROTECTED_OPEN.md')
    live = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8').read()
    # ⛔ THE CORRUPT STATE IS PINNED TO A SHA, NOT TO `HEAD`.
    #   The first draft of this receipt read `HEAD:PROTECTED_OPEN.md` -- which is the repair's own
    #   parent only until the repair is committed, after which it is the repaired file and every
    #   check below inverts.  *** That is the class this fork routed as items 28, 30 and 32: a
    #   receipt invalidated by its author's next move.  Caught here BEFORE the commit rather than
    #   by the full run afterwards, which is the first time this session that happened. ***
    CORRUPT = '7b6fded'          # c54.216's tip -- the last revision carrying the corrupt row
    before = git('show', CORRUPT + ':PROTECTED_OPEN.md')
    check(f'the pre-repair register is readable from git at the pinned {CORRUPT} (not HEAD, which '
          'this revision moves)',
          len(before) > 10000 and 'PO-4' in before)

    rb, rn = rows_of(before), rows_of(now)
    ob = {k: SPL.split(v)[2] for k, v in rb.items()}
    on = {k: SPL.split(v)[2] for k, v in rn.items()}
    # ** ⛭ AMENDED c54.224 (`L-558`).  `on` was read from the WORKING TREE, so "the repaired one" moved
    # ** every time the observer line edited `PO-4` -- r2777 took its route and r2778 STRUCK it, and the
    # ** measurements below (a 39x widening, the family-6 overlap) are about the state AT THE REPAIR. **
    #   ⇒ *** A before/after measurement needs BOTH ends pinned.  Pinning only the "before" leaves the
    #       comparison drifting on one leg, which is the same defect one leg over. ***
    REPAIRED = 'a83455b'         # c54.217 -- the revision that repaired the row
    rr = rows_of(git("show", REPAIRED + ":PROTECTED_OPEN.md"))
    on = {k: SPL.split(v)[2] for k, v in rr.items()}
    # and the property that must not REGRESS is still asserted against the live file, below.

    # ---------------------------------------------------------------- (1) the defect
    check(f'⓵ PO-4\'s OBJECT column was {len(ob["PO-4"])} characters, against {len(ob["PO-6"])} for '
          f'PO-6 and {len(ob["PO-3"])} for PO-3 -- the status narrative was living in the object cell',
          len(ob['PO-4']) > 4000 and len(ob['PO-6']) < 200 and len(ob['PO-3']) < 300)
    check('   and the object text itself was doubled, the second copy missing its opening "**"',
          '**The colour and isospin structure** The colour and isospin structure**' in ob['PO-4'])

    rep = longest_repeat(ob['PO-4'], 400)
    check(f'⓶ with a repeated block of {rep[0]} characters at offsets {rep[1]} and {rep[2]}, '
          f'the copy beginning MID-CLAUSE: {rep[3][:46]!r}',
          rep is not None and rep[0] > 1500 and rep[3].startswith('; only the sector is not built'))
    check('   and a third partial copy beginning MID-WORD, at "s the one geometric opening left" -- '
          'which an editing slip does not do',
          's the one geometric opening left' in ob['PO-4'])

    # ---------------------------------------------------------------- (2) provenance
    log = git('log', '--oneline', '-S', 'The colour and isospin structure** The colour and isospin',
              '--', 'PROTECTED_OPEN.md')
    entered = log.strip().split('\n')[-1] if log.strip() else ''
    n_since = git('rev-list', '--count', entered.split()[0] + '..HEAD').strip() if entered else '0'
    check(f'⓷ it entered at "{entered[:72]}" and stood {n_since} commits',
          'r2427' in entered and int(n_since or 0) > 300)
    check('   and that commit\'s own message says the ID gate fired -- so the merge WAS being '
          'watched, at the row level',
          'the ID collision fired' in git('log', '-1', '--format=%s', entered.split()[0]))

    # ---------------------------------------------------------------- (3) it satisfied a gate
    STOP = set('the a an of and or in on at to for is are was were be by with its it this that from '
               'what which as not but its their our one two three full open live sector'.split())

    def gwords(s):
        s = re.sub(r'\\[a-zA-Z]+|[^a-z ]', ' ', s.lower())
        return {w for w in s.split() if len(w) > 4 and w not in STOP}

    check(f'⛔ ⓸ AND THE CORRUPTION SATISFIED A GATE: check_family_pointers matches a family against '
          f'this column, and the corrupt object carried {len(gwords(ob["PO-4"]))} distinct content '
          f'words against {len(gwords(on["PO-4"]))} in the repaired one -- a 39x widening of what '
          'counts as "about the same thing"',
          len(gwords(ob['PO-4'])) > 20*len(gwords(on['PO-4'])))

    # AND ON A REAL FAMILY, not a hypothetical: family 6 is the gate's own founding case.
    fam6 = 'the propagating fermion and gauge sector'
    hit_before = gwords(fam6) & gwords(ob['PO-4'])
    hit_after = gwords(fam6) & gwords(on['PO-4'])
    check(f'⛔⛔ and MEASURED ON THE REAL FAMILY: family 6, "{fam6}", matched PO-4 on '
          f'{sorted(hit_before)} -- and BOTH words come from the corrupted status prose, NEITHER is '
          f'in the object. After the repair the overlap is {sorted(hit_after)}',
          hit_before == {'fermion', 'gauge'} and hit_after == set()
          and 'fermion' not in gwords(on['PO-4']) and 'gauge' not in gwords(on['PO-4']))
    gate = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'corpus', 'check_family_pointers.py'),
                                    encoding='utf-8').read())
    check('   ⇒ *** and family 6 is the gate\'s OWN FOUNDING CASE -- "family 6 is \'the propagating '
          'fermion and gauge sector\'" is why it was built. The corruption was supplying a spurious '
          'match on the very row that case was corrected AWAY from. ***',
          "family 6 is \"** the propagating fermion and gauge" in gate
          or 'the propagating fermion and gauge' in gate)
    check('   ⚠ and stated at its true size: family 6 still PASSES, because its correction note also '
          'names PO-11, which genuinely matches. What the corruption bought was a second, false '
          'reason to pass -- not the only one',
          'PO-11' in rn and len(gwords(fam6) & gwords(on['PO-11'])) > 0)

    # ---------------------------------------------------------------- (4) the second defect
    bad_before = {k: len(SPL.split(v)) for k, v in rb.items() if len(SPL.split(v)) != 7}
    bad_now = {k: len(SPL.split(v)) for k, v in rn.items() if len(SPL.split(v)) != 7}
    check(f'⓹ and three more rows split on unescaped math bars: {bad_before} -- now {bad_now}',
          set(bad_before) == {'PO-6', 'PO-10', 'PO-11'} and bad_now == {})

    # ⛭ AND THE LIVE HALF, so pinning both ends does not turn this into a receipt about history
    # ** only.  The property that must not REGRESS is that no protected row is split today. **
    #   ⇒ *This is the one claim that should be read against the working tree, and it is the one
    #    the original check could not make -- it was busy asking whether any word had ever left.*
    rl = rows_of(live)
    bad_live = {k: len(SPL.split(v)) for k, v in rl.items() if len(SPL.split(v)) != 7}
    check(f'⓹ᵇ ⛭ AND NO PROTECTED ROW IS SPLIT IN THE LIVE REGISTER EITHER: {len(rl)} rows, '
          f'{bad_live if bad_live else "none off the count"} -- the repair has not regressed across '
          f'the dedup (r2832b) or the closure (r3001)', bad_live == {})

    base = git('show', '6f926a6:PROTECTED_OPEN.md')
    n_base = len(SPL.split(rows_of(base)['PO-11']))
    check(f'⛔ AND ONE OF THE THREE IS MINE: PO-11 stood at {n_base} cells at the fork base '
          f'(r2713) and at {bad_before["PO-11"]} after c54.214 -- I did not introduce the class '
          'and I nearly doubled its worst instance',
          n_base == 15 and bad_before['PO-11'] == 29)

    idx = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'corpus', 'check_receipts.py'),
                                   encoding='utf-8').read())
    check('   ⌗⌗ and this is the DEFECT check_receipts gates for in receipts/INDEX.md: "a data row '
          'must have 8 columns; more = an unescaped \'|\' (escape math bars as \\|)"',
          "a data row must have 8 columns; more = an unescaped '|'" in idx)
    check('   ⇒ *** same hand, same session, same mistake: caught in INDEX.md at c54.214 because that '
          'file has a column gate, silent in PROTECTED_OPEN.md because it does not ***',
          'badcols' in idx)

    # ---------------------------------------------------------------- (5) content preserved
    wb, wn = collections.Counter(words(before)), collections.Counter(words(now))
    lost = [w for w in wb if w not in wn]
    check(f'⓺ THE REPAIR LOSES NO DISTINCT WORD, file-wide: {lost}', lost == [])
    # ⚠ THE FILE-LEVEL CHECK IS NOT ENOUGH, AND THIS TURN PROVED IT.  A first pass at the repair
    #   dropped "⛭⛭ **WHERE" from PO-4's head; the file-wide word check PASSED, because "WHERE"
    #   occurs in other rows.  *** A vocabulary check over a file cannot see a word moved out of
    #   one row while another still has it. ***  So the check that matters is PER-ROW, and below it
    #   a GLYPH-level multiset test on the repaired row itself.
    per_row = {k: [w for w in collections.Counter(words(rb[k])) if w not in
                   collections.Counter(words(rn[k]))] for k in rb}
    check(f'   and ROW BY ROW across all {len(rb)} protected rows: '
          f'{ {k: v for k, v in per_row.items() if v} }',
          all(not v for v in per_row.values()))
    gb, gn = collections.Counter(rb['PO-4']), collections.Counter(rn['PO-4'])
    gone = [g for g in gb if g.strip() and gn[g] < 1]
    check(f'   and at GLYPH level on the repaired row itself, no character class vanishes: {gone}',
          gone == [])

    # ---------------------------------------------------------------- (6) CONTROL: the base rate
    print()
    flagged80 = [k for k, v in ob.items() if longest_repeat(v, 80) or
                 longest_repeat(SPL.split(rb[k])[5] if len(SPL.split(rb[k])) > 5 else '', 80)]
    cells80 = []
    for k, v in rb.items():
        for c in SPL.split(v):
            if len(c) >= 160 and longest_repeat(c, 80):
                cells80.append(k)
                break
    cells400 = []
    for k, v in rb.items():
        for c in SPL.split(v):
            if len(c) >= 800 and longest_repeat(c, 400):
                cells400.append(k)
                break
    check(f'⛔ CONTROL: a repeated-block detector at 80 chars flags {sorted(set(cells80))} -- and the '
          'extra three are LEGITIMATE re-quotation, a cell quoting one sentence twice because two '
          'revisions worked it',
          len(set(cells80)) > len(set(cells400)))
    check(f'   at 400 chars it flags {sorted(set(cells400))} alone',
          set(cells400) == {'PO-4'})
    check('   ⇒ *** the base rate is three and the finding is one; a detector reported without its '
          'base rate would have claimed four. This fork\'s own c54.216 addition is one of the three. ***',
          'PO-5' in set(cells80))

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** a protected row was corrupt for 368 commits, and the corruption was')
    print('  SATISFYING a gate rather than tripping one. **')
    print('  ⓵ ** PO-4\'s OBJECT column ran to 5069 characters ** against 106 and 182 for its')
    print('     neighbours: the object doubled, a 1629-character block twice with its copy starting')
    print('     mid-clause, and a third partial copy starting *** mid-word ***.')
    print('  ⓶ ** Entered at r2427 ** — the c54.163 -> c54.178 absorption, whose own message reports')
    print('     "the ID collision fired".  *** It fired on the rows and missed the cell. ***')
    print('  ⛔ ⓷ ** And check_family_pointers reads that column: ** a 5069-character object matches')
    print('     a family on volume, so *** the corruption was making a live gate PASS. ***')
    print('  ⓸ ** Three more rows split on unescaped math bars — and PO-11 went 15 to 29 cells at')
    print('     this fork\'s own c54.214. *** The identical mistake was caught in INDEX.md two')
    print('     revisions earlier, because that file has a column gate and this one does not. ***')
    print('  ⓹ ** Repaired, losing no distinct word ** — file-wide and row by row.')
    print('  ⛔ ** CONTROL: ** at an 80-character threshold the detector flags four rows and three')
    print('     are legitimate re-quotation (one of them this fork\'s own).  The base rate is three.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
