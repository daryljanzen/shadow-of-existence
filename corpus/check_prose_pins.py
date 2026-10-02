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
    CEILING = 118
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
