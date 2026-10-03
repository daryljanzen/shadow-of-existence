#!/usr/bin/env python3
"""check_prose_pins.py -- EVERY PROSE-PIN SITE IS EITHER ADJUDICATED OR COUNTED, AND THE UNREAD COUNT ONLY FALLS.

** WHAT A PROSE-PIN IS. **  A non-zero pin on a COUNT OF MATCHES in text a receipt reads -- another paper's
prose, another file's source, a ledger.  *** The defect is an assertion that passes on something other than
its own measurement: a count can hold while the thing it counts has moved. ***

** WHY THIS GATE EXISTS, AND IT IS NOT A NEW IDEA -- IT IS A HAND-CAUGHT CLASS MADE MECHANICAL. **  Four real
instances were caught by hand in this programme: `C41b`'s literal `8.2` (which turned out to be a
polarisation figure, not the damping signature), `R1`'s `likelihood` count, and two peak locators demanding
exact equality on a coarse grid.  *** Node 70 built the instrument that finds them -- `scripts/mutate_assertions.py`,
`r7113+70.1` -- and this gate is the ratchet on its static operator. ***

  ⌗ ** THE MEASUREMENT IS 70's AND THIS GATE DOES NOT REIMPLEMENT IT. **  It runs that script's `--prose`
  operator as a subprocess and compares the sites it reports against the adjudication baseline.

** WHAT IT CHECKS, AND THERE ARE THREE THINGS. **
  ⓵ ** every site the instrument reports is in the baseline ** -- a NEW prose-pin is a `[FAIL]`, so the class
    cannot grow silently;
  ⓶ ** every baseline site is still reported ** -- a listed site whose expression is gone means the receipt
    moved and the adjudication no longer describes anything, so the entry must be removed (reported as a
    `[STALE]` failure, the same rule as the marker-transposition baseline);
  ⓷ ** the UNADJUDICATED count may only FALL. **  *The 170 sites seeded at `r7119` stand in the open as a
    backlog with its own register row.  They are not exemptions: the bucket means work, and the ratchet is
    that it can only shrink.*

  ⛔ ** THE BACKLOG IS NOT A FAILURE AND THIS GATE DOES NOT TREAT IT AS ONE. **  *A gate that went red on all
  170 at once would be turned off within a day, and the class would go back to being caught by hand.  What it
  enforces is the direction: no new sites, no stale entries, and the unread count monotone down.*

** THE KEY IS (receipt, expression), NOT A LINE NUMBER, DELIBERATELY. **  *A line-keyed baseline goes stale the
moment anything above a site is edited -- which is the same `assertion pinned to a spelling` failure this file
exists to catch.  An expression that is reworded is a NEW site and is read again, which is correct.*

  python3 corpus/check_prose_pins.py
  python3 corpus/check_prose_pins.py --list      # print the unadjudicated backlog, complete and unfiltered

Written r7119.  Stated for reversal.
"""
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
BASELINE = os.path.join(HERE, 'prose_pin_baseline.tsv')
INSTRUMENT = os.path.join(ROOT, 'scripts', 'mutate_assertions.py')

LINE = re.compile(r'\s*\[PROSE-PIN\s*\]\[(PIN|PRESENCE)\]\s+(\S+?):(\d+):(\d+)\s+(.*)$')
UNREAD = 'UNADJUDICATED'


def read_baseline():
    rows = {}
    if not os.path.exists(BASELINE):
        return rows
    for ln in open(BASELINE, encoding='utf-8'):
        ln = ln.rstrip('\n')
        if not ln.strip() or ln.startswith('#'):
            continue
        p = ln.split('\t')
        if len(p) >= 4:
            rows[(p[0], p[1])] = (p[2], p[3], p[4] if len(p) > 4 else '')
    return rows


def measure():
    """run 70's own static operator and return {(receipt, expression): tier}"""
    r = subprocess.run([sys.executable, INSTRUMENT, '--prose'], cwd=ROOT,
                       capture_output=True, text=True, timeout=1800)
    out = {}
    for ln in r.stdout.splitlines():
        m = LINE.match(ln)
        if m:
            tier, path, _l, _c, expr = m.groups()
            out[(path, expr)] = tier
    return out, r.stdout


def main():
    print()
    print('  PROSE-PIN RATCHET -- is every pin on a count of matches adjudicated, or at least counted?')
    print()
    base = read_baseline()
    if not base:
        print(f'  ⛔ no baseline at {os.path.relpath(BASELINE, ROOT)} -- this gate has no record to ratchet.')
        return 1

    live, raw = measure()
    print(f"    the instrument reports {len(live)} distinct (receipt, expression) key(s); "
          f"the baseline carries {len(base)}")
    print("    ⌗ the instrument prints one line per SITE; identical expressions in one receipt collapse to "
          "one\n      adjudication here, because reading it once settles it")
    tiers = {}
    for t in live.values():
        tiers[t] = tiers.get(t, 0) + 1
    print(f"    by tier: {tiers}")
    verdicts = {}
    for _t, v, _w in base.values():
        verdicts[v] = verdicts.get(v, 0) + 1
    print(f"    by verdict: {verdicts}")
    unread = verdicts.get(UNREAD, 0)
    print(f"    {UNREAD}: {unread}   ** the only bucket that means work, and it may only fall **")

    if '--list' in sys.argv:
        print()
        print(f'  THE BACKLOG, COMPLETE AND UNFILTERED -- {unread} site(s):')
        for (p, e), (t, v, _w) in sorted(base.items()):
            if v == UNREAD:
                print(f'    [{t:<8}] {p}')
                print(f'               {e}')
        return 0

    bad = 0

    new = sorted(k for k in live if k not in base)
    if new:
        print()
        print(f'  ⛔ {len(new)} NEW PROSE-PIN SITE(S) -- not in the baseline:')
        for p, e in new[:40]:
            print(f'    [FAIL] {p}')
            print(f'           {e}')
        if len(new) > 40:
            print(f'    ... and {len(new)-40} more')
        print('     ⌗ READ IT AND RECORD A VERDICT.  A new pin on a count is the class this gate')
        print('       exists for, and the four it was built from were all found by hand.')
        bad += 1
    else:
        print('    no new site: the class has not grown.')

    gone = sorted(k for k in base if k not in live)
    if gone:
        print()
        print(f'  ⛔ {len(gone)} STALE BASELINE ENTR(Y/IES) -- the expression is no longer reported, so the')
        print('     adjudication describes nothing.  REMOVE the entry:')
        for p, e in gone[:40]:
            print(f'    [STALE] {p}')
            print(f'            {e}')
        if len(gone) > 40:
            print(f'    ... and {len(gone)-40} more')
        print('     ⌗ A fixed site left in the baseline is a silent permission to regress there (r7069).')
        bad += 1
    else:
        print('    no stale entry: every adjudication still describes a live site.')

    # ⓷ the ratchet.  The declared ceiling lives HERE and in no other file, so it cannot go stale
    #   against itself; raising it is a visible edit to this gate and nothing else.
    #   ⛭ r7119: the ceiling is 149 and NOT the instrument's 170.  *The instrument reports one line per
    #   SITE; this baseline is keyed on (receipt, expression), so 21 of those 170 are the SAME expression
    #   appearing more than once in one receipt and collapse to one adjudication -- which is correct, since
    #   reading it once settles it.*  ⛔ *A first draft declared 170 and then printed `21 already read`,
    #   which was false: nothing had been read, and the slack was an artefact of the key.  Recorded rather
    #   than quietly corrected, because inventing headroom is the failure this instrument was built to find.*
    CEILING = 0
    #: ⚑⚑ r7151+cc66.112: 24 -> **0**. THE PROSE-PIN BACKLOG IS DISCHARGED: 137 keys, every one
    #: verdicted, `UNADJUDICATED` empty for the first time since this gate was built. The ceiling can
    #: now only be raised by a visible edit here, which is what it was for.
    #:   ⌗ Final distribution, once: **DELIBERATE 74 · PRESENCE-CONTROL 50 · NOT-A-COUNT 13.**
    #: ⛑ r7151 PREDICTED that `exact census with provenance` would be commoner in `REGISTER` than
    #: anywhere, and offered its failure as the finding. **IT HOLDS, and by a wide margin: 5 of the 14
    #: `REGISTER` sites against 3 of the 46 `PAPER` ones -- 36 per cent against 7.** And the mechanism
    #: is sharper than "documents we rewrite": *every one of the five reads a PINNED BLOB* --
    #: `git show BEFORE:...`, `git show PARENT:OWED.md`, `git show _BLIND:corpus/check_receipts.py`.
    #:   ⇒ *So the shape does not follow from the text being a register. It follows from the receipt
    #:   having pinned its subject to a SHA -- and `REGISTER` is where that is done, because a register
    #:   is the thing that moves under you. A count of a file at a commit CANNOT move, so exactness is
    #:   free and a floor buys nothing.* ⌗ `L253/S1` proves it against itself: it carried the SAME
    #:   pinned expression twice, once `>= 3` and once `== 3`, two lines apart.
    #: ⛑ AND A SHAPE THE `PAPER` BLOCK DID NOT HAVE AT ALL -- **UNIQUENESS ON A LIVE DOCUMENT**,
    #: 3 of the 14: `== 1` asserting that a string survives only inside its own withdrawal
    #: (`L549/Q1`'s `144/80/24`, where r2738's bare absence pin was broken by the correction note that
    #: had to quote the value it corrected), only as a quotation (`L269/T1`'s stale `★ NEXT`), or not
    #: spliced twice (`L269/T1`'s corrupted heading). *Exactness load-bearing in the opposite direction
    #: from a floor, on text that is still being edited.*
    #: ⛔ THREE FLOORS IN THIS BLOCK CONCEALED A DEAD HEADLINE IN THE RECEIPT'S OWN PROSE, which with
    #: `P03`'s *"its three uses"* against eleven makes four in two blocks and settles the row's case:
    #: `P12/A8`'s verdict line said TWICE against a measured 5; `L254/A1`'s PART 5 said FOUR against 5
    #: -- *and in that one the floor was `>= 4`, equal to the stale figure*; `L272/F1` printed NO NUMBER
    #: at all under `> 20` against 51, so its margin was invisible to its own reader.
    #:   ⌗ *The common mechanism, now stated: a floor set at the figure the prose quotes will never
    #:   contradict that prose when the measurement moves past it. **The floor is what makes the
    #:   headline unfalsifiable**, which is the strongest form of this row's argument and was produced
    #:   by the backlog rather than by the gate.*
    #: ⛔ ONE DEFECT WAS MINE: `L218/C2`'s `open_items >= 8` is the third line of the dashboard whose
    #: r7143+cc66.108 comment -- *mine* -- says all three assert their class is non-empty. Two did.
    #: *The comment was true of what I meant and false of what I wrote, and only re-reading the file
    #: caught it.*
    #: ⛭ r7143+cc66.109: 70 -> 24, lowered by EXACTLY the 46 sites read -- THE WHOLE OF THE `PAPER`
    #: CLASS, which the r7141 partition now reports as **0 of the remaining 24**.  The 24 left are
    #: 4 SOURCE + 14 REGISTER + 6 NOT-A-COUNT, and none of them is repair owed on paper prose.
    #:   ⌗ THE SHAPE OF THE 46, which is the part worth keeping: 32 were verdicted WHERE THEY STOOD
    #:   and 14 were repaired.  Of the 14, six survive the repair as a minimal `> 0` presence check and
    #:   are verdicted here -- but **EIGHT LEFT THE CLASS ALTOGETHER**, because the bound that replaced
    #:   the round floor is DERIVED, NAMED or RELATIONAL and so has no literal left to pin:
    #:   `edges > 150` became `edges > len(g) * (len(g) - 1) // 2`, the ceiling a transitive total order
    #:   could carry; `n_lep >= 10` became `n_lep > _PREMISE_LEP`, the stale premise it was contradicting;
    #:   `len(where[a]) >= 15` became `len(where[a]) > len(where[b])`, the comparison the label actually
    #:   makes; `prox < 60` became `prox * 1000 < tot`, the *under one per thousand* the label states.
    #:   ⇒ *So the instrument's own population is a measure of how many bounds are still literals.
    #:   Repairing a pin properly does not move it to a better verdict -- it removes it from the class,
    #:   and the key count fell 147 -> 139 for exactly that reason and no other.*
    #: ⛑ THE VERDICT DISTRIBUTION, ONCE, over all 139 keys -- there is no fourth forward call after
    #: this one: **DELIBERATE 62 · PRESENCE-CONTROL 46 · NOT-A-COUNT 7 · UNADJUDICATED 24.**  The 38
    #: rows this block wrote are 24 DELIBERATE, 12 PRESENCE-CONTROL, 2 NOT-A-COUNT.
    #:   ⌗ *DELIBERATE outnumbers PRESENCE-CONTROL across the tree and inside this block alike, which
    #:   inverts what a backlog of 70 "pins on a count" suggested: the common case is a bound that IS
    #:   the finding, not a floor hiding one.  Six repairs out of 46 read is the honest hit rate.*
    #: ⛑ THE `NOT-A-COUNT` BOUNDARY, now stated rather than left to the hand-table (r7145 ⓵), with
    #: the bucket at 7: **NOT-A-COUNT is where the traced value is not a tally of matches at all** --
    #: a float comparison, an argmax index, a computed ratio dict, a coefficient table, a character
    #: offset.  The instrument matches on the SHAPE of the expression (`len(...)`, `.count(...)`) and
    #: cannot see what was counted, so these are its false positives and will recur on every new family.
    #:   ⌗ *It is ORTHOGONAL to PAPER / SOURCE / REGISTER, which say which TEXT was read.  That is why
    #:   a site can be PAPER and NOT-A-COUNT at once -- `L_numerics/Q1` reads the paper and then compares
    #:   two floats -- and why the two classifications must not be collapsed into one column.*
    #: ⛭ r7139+cc66.106: 97 -> 70, lowered by EXACTLY the 27 sites read -- the whole of
    #: `receipts/P15_CR_cosmology`, across 12 receipt files, every one verdicted in
    #: prose_pin_baseline.tsv with what was read.  ⚑ *And NOT ONE REPAIR: 20 DELIBERATE, 3
    #: PRESENCE-CONTROL already at their minimal form, 4 NOT-A-COUNT.  The live total is unchanged at
    #: 147 because no expression moved -- the largest remaining family needed no code change at all,
    #: which is the opposite of what a 27-site backlog entry suggests.*
    #:   ⌗ *WHY THIS FAMILY IS DIFFERENT, and it is a statement about this gate rather than about
    #:   `P15`: 18 of the 20 DELIBERATE sites are WIRING-UNIQUENESS assertions on an instrument's own
    #:   SOURCE -- `n_of(...) == 1`, `SRC.count(...) == 1` -- where the exactness is load-bearing in
    #:   the OPPOSITE direction from a round floor.  **Loosening one to `> 0` would destroy the claim
    #:   rather than minimise it**, and a second occurrence is the double-wiring bug the check exists
    #:   to catch.  ⇒ *That is the test separating this class from a prose pin, and it is now written
    #:   in all 18 adjudications.*
    #:   ⌗ *And 4 are the instrument's own false positives -- two float `abs(...) > 1e-9` comparisons
    #:   in an `if`, a float maximum and an ARGMAX index, none of them a count of matches in any text.
    #:   The `NOT-A-COUNT` bucket went 1 -> 5 on one family, so the B41 precedent was not a one-off.*
    #: ⛭ r7135+cc66.102: 106 -> 97, lowered by EXACTLY the 9 sites read -- the whole of
    #: `receipts/L165_defining_the_sum` (5) and `receipts/L203_reach_stations` (4), every one
    #: verdicted in prose_pin_baseline.tsv with what was read.  ⌗ *The order's sizing was right this
    #: time: 5 and 4, file rows equal to distinct keys in both families, because the cc66.99 de-dup
    #: pass had already closed that gap everywhere.*
    #:   ⌗ *The live total is unchanged at 147: 9 rows written for 9 sites read, no key collapsed and
    #:   none retired, so here the ceiling's fall equals the rows written as well as the sites read --
    #:   which it did NOT at r7131 and is a coincidence of this block, not the rule.  What the ceiling
    #:   tracks is still what is UNREAD.*
    #:   ⛔ *A first draft of the `S1` C6 repair asserted the paper's sentence as a LITERAL, which
    #:   retired that key here and put two new ones into `quote_pin_baseline.tsv` -- moving the claim
    #:   into node 70's class instead of settling it, and pinning a gate to wording the papers are
    #:   actively revising.  Measured and withdrawn; the live condition asserts the grid-free shape.*
    #: ⛭ r7131+cc66.100: 118 -> 106, lowered by EXACTLY the 12 sites read -- the whole of
    #: `receipts/L221_the_bridge`, every one verdicted in prose_pin_baseline.tsv with what was
    #: read.  ⛔ *The r7131 order said 13 and 105.  13 was the PRE-DE-DUP file count -- it is in
    #: cc66.98's own measurement, "L221_the_bridge rows 13 keys 12 overstated by 1", and the
    #: cc66.99 pass removed that duplicate row.  So the order was sized from the file as it stood
    #: before the fix for sizing from the file.*  ⌗ *File rows and distinct keys are now equal
    #: everywhere, so the discrepancy cannot arise again.*
    #:   ⌗ *12 sites were READ; the repairs collapsed two keys, so the live total fell 149 -> 147
    #:   and the unadjudicated count 118 -> 106.  The ceiling tracks what is UNREAD, which is why
    #:   it moves by the 12 read and not by the 10 rows written.*
    #: ⛭ r7125+cc66.98: 149 -> 118, lowered by EXACTLY the 31 sites read -- the whole of
    #: `receipts/L204_physics_reach`, every one verdicted in prose_pin_baseline.tsv with what was
    #: read.  ⛔ *The r7125 order said 42 and 107.  42 is the RAW site count; this file and the
    #: baseline key on distinct `(receipt, expression)` pairs, of which the family has 31, so 42
    #: would have invented 11 of headroom -- the same `(receipt, expression)` artefact that put the
    #: 149-against-170 slack in this gate's own history.  Verified both ways: 149 - 31 read = 118,
    #: and 149 live keys - 31 verdicted = 118.*
    if unread > CEILING:
        print()
        print(f'  ⛔ THE UNADJUDICATED COUNT ROSE: {unread} against the declared ceiling {CEILING}.')
        print('     ⌗ The bucket means work and the ratchet is that it only shrinks.  Lowering the')
        print('       ceiling is the point; raising it is an edit to this gate and must be argued.')
        bad += 1
    else:
        read_n = sum(1 for _t, v, _w in base.values() if v != UNREAD)
        print(f'    the ratchet holds: {unread} unadjudicated against a ceiling of {CEILING}'
              + (f'; {read_n} site(s) read and verdicted' if read_n else '; none read yet'))

    print()
    if bad:
        print('  ⛔ THE PROSE-PIN RATCHET IS RED.')
        return 1
    print('  the prose-pin class is fully accounted: no new site, no stale entry, and the backlog')
    print('  standing in the open with its register row rather than hidden as exemptions.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
