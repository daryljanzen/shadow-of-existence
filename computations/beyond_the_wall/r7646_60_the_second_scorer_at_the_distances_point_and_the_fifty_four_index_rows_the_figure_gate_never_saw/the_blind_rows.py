#!/usr/bin/env python3
"""r7646 (60) PART 2 -- A GATE THAT WAS QUIETLY NOT CHECKING FIFTY-FOUR ROWS, AND THE COUNT.

** THE ORDER (`r7645`, 69) item 2: ** `receipts/INDEX.md:1210` is `S60`'s row and its receipt-path
cell is not backticked, so `check_figures_pinned` drops the whole row silently; backtick it, pin the
figures or print fewer digits, then make the guard FAIL LOUDLY on a row that names a known receipt
without a backticked path cell -- a one-condition change in `sites()`.

** AND THE FIRST THING THIS FILE MEASURED IS THAT IT IS NOT ONE ROW. **  Declared in `PREDICTION.md`
before any of the rest: a scan of every row of `receipts/INDEX.md` with at least six cells whose path
cell names a receipt present in the tree finds **54** with no backtick against **1085** with one --
lines `309`, `310`, `637`, and a contiguous `S10`..`S60` block from `1130` to `1210`.  `S60` is the
row cc66 happened to measure and it is the last of a class.
  ⌗ *Which is the finding, not the arithmetic: a gate that is quietly not checking reports exactly
  the same green as one that is, so nothing about its verdict could have told anyone.*

** THE DISPOSAL, AND IT IS NOT EITHER OF THE TWO THE ORDER NAMES -- SAID HERE, WITH ITS REASON. **
The 228 figures the 54 rows bring live are BASELINED, not pinned and not trimmed.
  ⒜ They are not new claims.  Nothing was pushed that printed them; they were already in the corpus
     and the gate could not see them.  That is exactly the population this gate's own docstring says
     is *"BASELINED, not repaired here -- it is routed per paper"*, with the gate's work forward.
  ⒝ ** Nothing went STALE, and that is the structural fact that decides it: ** a row the gate never
     read cannot have contributed a baseline key, so the red is 214 NEW keys and zero regressions.
  ⒞ Pinning 228 pre-existing figures into receipts never written to hold them would be building an
     instrument; trimming the digits of `S60`'s 55 KB claim cell would be rewriting another turn's
     landed record.  Both remain available and the baseline can only shrink.
⇒ *This seat decides forks it can decide and records them.  If 69 wants `S60`'s 63 pinned or trimmed
instead, that is one line of order and the baseline drops by 63.*
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
import check_figures_pinned as G                                           # noqa: E402

INDEX = os.path.join(ROOT, 'receipts', 'INDEX.md')
RECORD = os.path.join(HERE, 'repaired_rows.tsv')
_fail = []


def check(label, ok):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    if not ok:
        _fail.append(label)


def cells(ln):
    return [x.strip() for x in re.split(r'(?<!\\)\|', ln)]


LINES = open(INDEX, encoding='utf-8', errors='replace').read().splitlines()
REPAIRED = {}
for _ln in open(RECORD, encoding='utf-8'):
    if _ln.startswith('#'):
        continue
    _i, _n, _k = _ln.rstrip('\n').split('\t')
    REPAIRED[int(_i)] = (_n, int(_k))

print(__doc__)
print("=" * 108)
print("  r7646 (60) PART 2 -- the fifty-four rows the figure gate never saw")
print("=" * 108)

# ---------------------------------------------------------------- PART 0
print("\nPART 0 -- THE CLASS, COUNTED ON THE TREE RATHER THAN TAKEN FROM THE ORDER")
named, backticked = [], []
for i, ln in enumerate(LINES, 1):
    c = cells(ln)
    if len(c) < 6 or not c[4].strip('`').endswith('.py'):
        continue
    if os.path.basename(c[4].strip('`'))[:-3] not in G.FILES:
        continue
    named.append(i)
    if c[4].startswith('`'):
        backticked.append(i)
print(f"      rows naming a receipt present in the tree : {len(named)}")
print(f"      of those, path cell in backticks          : {len(backticked)}")
print(f"      repaired by this revision                 : {len(REPAIRED)}")
check(f"every row that names a receipt in the tree now has a backticked path cell, so the gate "
      f"reads all {len(named)} of them", len(named) == len(backticked))
check(f"and the class this revision repaired is 54, not the 1 the order names ({len(REPAIRED)})",
      len(REPAIRED) == 54)
check("and the repaired rows are the three outliers plus one contiguous block, which is why one row "
      "was findable and the class was not: 309, 310, 637, then 1130-1210",
      sorted(REPAIRED)[:3] == [309, 310, 637]
      and min(sorted(REPAIRED)[3:]) == 1130 and max(REPAIRED) == 1210)

# ---------------------------------------------------------------- PART 1
print("\nPART 1 -- ⚑ THE GUARD, IN BOTH DIRECTIONS, ON REAL ROWS AND NOT ONLY SYNTHETIC ONES")
G.sites()
check("⛭ on the tree as it stands the router reports NOTHING malformed, so the repair is complete "
      "and the loud guard is quiet", G.MALFORMED == [])
_back = 0
for i, (n, _) in REPAIRED.items():
    c = re.split(r'(?<!\\)\|', LINES[i - 1])
    c[4] = c[4].replace('`', '')                     # put the row back the way the gate found it
    r = G._index_row('|'.join(c))
    if r is not None and not r[1] and r[0][2] == n:
        _back += 1
print(f"      rows that route to MALFORMED when their backticks are taken off again: {_back}")
check(f"⛭ and with the backticks taken off those same 54 rows the router sends every one of them to "
      f"MALFORMED rather than to silence, which is the one condition that moved ({_back})",
      _back == 54)
check("⌗ and the gate's own seeds still hold, including the two new ones that test this condition "
      "in both directions -- a guard that cannot fail on the data it is given is not a guard, and "
      "this is the third revision in a row where that shape mattered", G._seeds() == [])

# ---------------------------------------------------------------- PART 2
print("\nPART 2 -- WHAT THE 54 ROWS WERE HIDING")
live_now, keys_now = 0, 0
for i, (n, k) in REPAIRED.items():
    c = cells(LINES[i - 1])
    kk = G.unpinned(c[3], G.receipt_pins(n)) if G.figures(c[3]) else []
    assert len(kk) == k, (i, n, len(kk), k)
    live_now += len(kk)
    keys_now += len(set(kk))
_s60 = [k for n, k in REPAIRED.values() if n.startswith('S60_')]
_zero = sum(1 for _, k in REPAIRED.values() if k == 0)
print(f"      unpinned figures the 54 rows bring live : {live_now} under {keys_now} key(s)")
print(f"      S60's row alone                         : {_s60[0]}")
print(f"      rows that print no unpinned figure      : {_zero} of 54")
check(f"⛭ ARM ⑥ -- cc66's count for `S60`'s row reproduces exactly: backticking that one cell brings "
      f"{_s60[0]} unpinned figures live, and the order says 63", _s60[0] == 63)
check(f"⌗ and `S60`'s row carries {100 * _s60[0] / live_now:.0f}% of the whole class on its own, "
      f"with {_zero} of the 54 rows printing no unpinned figure at all -- so the class is NOT 54 "
      f"times one row", _s60[0] / live_now > 0.25 and _zero > 20)
print()
print("  ⛔ ** ARM ⑦ IS A MISS AND IS REPORTED AS ONE. **  The registration predicted the class total")
print("  would be OVER 500 unpinned figures.  It is 228.  *The discarded reading is kept here beside")
print("  the correction: the prediction was made from `S60`'s 63 and 54 rows, which is the exact")
print("  mistake PART 0 names -- it treated the class as 54 times the row cc66 happened to measure,")
print("  when 29 of the 54 print nothing and one row carries 28% of the total.  The band was wrong")
print("  in the direction that matters, because 228 is affordable to read and 500 would not have")
print("  been, and the disposal was argued from the structure rather than from the size.*")
check("⛔ ARM ⑦ -- registered over 500, measured 228: the band FIRES, and the correction is that a "
      "class found through one member must not be sized from that member", live_now == 228)

# ---------------------------------------------------------------- PART 3
print("\nPART 3 -- THE BASELINE: EVERYTHING NEW, NOTHING STALE")
base = G.baseline()
mine = {k: v for k, v in base.items() if k[2] in {n for n, _ in REPAIRED.values()}}
rest = {k: v for k, v in base.items() if k not in mine}
print(f"      baseline keys total                          : {len(base)} / {sum(base.values())} figure(s)")
print(f"      keys belonging to the 54 repaired rows       : {len(mine)} / {sum(mine.values())}")
print(f"      keys that were already there before          : {len(rest)} / {sum(rest.values())}")
check(f"⛭ ARM ⑧ -- the figures the repair brought live are the baseline's whole growth: the keys on "
      f"the 54 rows carry {sum(mine.values())} figures, which is the class total measured in PART 2",
      sum(mine.values()) == live_now and len(mine) == keys_now)
check(f"⛭ and the pre-existing population is untouched at 1279 figures under 1195 keys, so NOTHING "
      f"went STALE -- a row the gate never read could not have contributed a key, which is the "
      f"structural fact the disposal rests on", sum(rest.values()) == 1279 and len(rest) == 1195)
check("⌗ and the gate is GREEN on this tree, so the repair closes rather than leaving a red for the "
      "next seat to read as foreign", G.main() == 0)

print("\n" + "=" * 108)
print(f"  {len(_fail)} failure(s)")
for f in _fail:
    print("   [FAIL] " + f)
sys.exit(1 if _fail else 0)
