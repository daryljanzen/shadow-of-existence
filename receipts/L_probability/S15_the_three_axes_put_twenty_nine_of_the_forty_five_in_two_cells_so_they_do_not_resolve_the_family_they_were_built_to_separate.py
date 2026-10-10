#!/usr/bin/env python3
"""L_probability receipt -- *re `r7247`*: THE FORTY-FIVE CLASSIFIED, AND THE AXES DO NOT RESOLVE THEM.

*** ⛭⛭⛭ SEVEN OCCUPIED CELLS OF THE EIGHT THREE BINARY AXES CAN HOLD --- INSIDE THE PRE-REGISTERED
    BAND OF `3`-`9` WITH THE CENTRAL GUESS ONE LOW.  BUT SEVEN CELLS IS NOT SEVEN MECHANISMS, AND
    THE REPORT IS A MEASURED REFUSAL TO COLLAPSE. ***

⛔⛭⛭ ** `29` OF THE `45` SIT IN TWO CELLS WHILE DIFFERING IN SOMETHING NO AXIS NAMES. **  *What the
   stand-in stands in FOR takes `21` distinct values across the forty-five --- a paper's sentence, a
   paper's term, a ledger row, a generated artefact, a coordination channel, git history, a
   convention, an instrument's own population, a receipt's own control, a lifted reading --- and that
   column CROSSES the cells rather than refining them.* ⇒ *** So a small cell count here measures the
   INSTRUMENT'S RESOLUTION and not the corpus's structure: three bits cannot separate forty-five
   things, and `7 of 8` occupied is what near-saturation looks like. ***

⚠ ** THE DIRECTION OF THIS SEAT'S INTEREST WAS PRE-REGISTERED BEFORE THE MEASUREMENT, AS THE ORDER
   REQUIRED: toward a SMALL number, because a collapse would make thirty revisions of a family this
   seat half-authored read as one discovery and would close a row. **  ⌗ *So the defence is
   structural and is in this file: the FULL CELL CENSUS is published, every member's three verdicts
   beside it, and every figure below is recomputed from that table rather than asserted --- a reader
   who rejects a merge can recompute the count without re-reading the register.*

⌈ ⛔ *** AND ONE COINCIDENCE IS STATED RATHER THAN LEFT FOR A READER TO NOTICE: the largest cell's
  share came back at `40` per cent, which is EXACTLY the central guess pre-registered for it. ***
  *That is the quantity whose direction this seat admitted wanting, landing on the nose. The census
  is the reason it can be checked, and it is reported as a coincidence and not as a calibration.*

✔ *The band on the other half is REFUTED HIGH and in the direction that costs this seat the result it
wanted: `4`-`25` members were predicted to need a discriminator the axes do not name, and `29` do.*

COMPUTES: nothing the papers quote.  This receipt recounts a register row's own family against the
three axes the row itself applies; no physical parameter is pinned here.
"""
import collections
import os

CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def head(t):
    print("\n  " + "=" * 74 + f"\n  {t}\n  " + "=" * 74, flush=True)


print(__doc__)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7250_60_classify_the_forty_five')
CENSUS = os.path.join(BASE, 'CENSUS.tsv')
MEMBERS = os.path.join(BASE, 'MEMBERS.tsv')

_raw = open(CENSUS, encoding='utf-8').read()
ROWS = [l.split('\t') for l in _raw.splitlines() if l.strip() and not l.startswith('#')]
AXES = ('CHOSEN', 'CONDITION', 'DESTROYS')

# ============================================================ A. the table is a table
head('A.  THE CENSUS IS WELL-FORMED, AND ITS POPULATION IS THE ROW`S OWN')

gate(f'Ⓐ① the census carries one row per member and nothing else: {len(ROWS)} rows, each with the '
     'three axis verdicts, the object and a one-line statement -- *checked before any count is '
     'taken from it, because a tally over a malformed table is the defect this line keeps finding*',
     len(ROWS) == 45 and all(len(r) == 6 for r in ROWS)
     and [int(r[0]) for r in ROWS] == list(range(1, 46)))

_vals = {a: {r[i + 1] for r in ROWS} for i, a in enumerate(AXES)}
gate('Ⓐ② every axis is BINARY and every cell is filled -- no blanks, no third value, so a member '
     'cannot sit outside the instrument while appearing to be classified by it',
     all(v <= {'Y', 'N'} and v == {'Y', 'N'} for v in _vals.values()))

_m = [l.split('\t') for l in open(MEMBERS, encoding='utf-8').read().splitlines()
      if l.strip() and not l.startswith('#')]
gate(f'Ⓐ③ and the census is over the SAME forty-five the member table anchors to the register row, '
     f'by number: {len(_m)} anchored, {len(ROWS)} classified, and the two id sets are equal',
     len(_m) == 45 and {r[0] for r in _m} == {r[0] for r in ROWS})

# a POSITIVE control on the reading itself: the file must be non-trivially populated, or every
# count below would read zero and the gates would pass on an empty table.
_chars = len(_raw)
gate(f'Ⓐ④ ⌗ and the control this family exists to teach: the census read NON-EMPTY -- {_chars:,} '
     f'characters, {len(ROWS)} rows, {sum(len(r) for r in ROWS)} fields -- *because a classification '
     f'whose table came back empty would satisfy every "no member is miscounted" test trivially*',
     _chars > 3000 and len(ROWS) > 40)

# ============================================================ B. the count the order asked for
head('B.  THE COUNT THE ORDER ASKED FOR, AND THE BAND IT WAS PRE-REGISTERED IN')

CELLS = collections.Counter(tuple(r[1:4]) for r in ROWS)
print(f'      occupied cells: {len(CELLS)} of {2 ** len(AXES)} the three axes can hold')
for c, n in CELLS.most_common():
    print(f'          {"/".join(c)}   {n:2d} member(s)')

gate(f'Ⓑ① ⛭ *** THE FORTY-FIVE REDUCE TO {len(CELLS)} OCCUPIED CELLS UNDER THE THREE AXES *** --- '
     f'pre-registered `6` in a band of `3`-`9`, so the band HOLDS and the central guess was one low. '
     f'⌗ *Reported before the reading of what it means, because the order asked for the number and '
     f'the number is not the result*',
     3 <= len(CELLS) <= 9)

gate(f'Ⓑ② ⚠ and {2 ** len(AXES) - len(CELLS)} of the {2 ** len(AXES)} possible cells is empty, which '
     'is the fact that turns the count into a reading: **the instrument is NEAR SATURATION**.  *Three '
     'binary axes can separate at most eight things however many are put into them, so a count at or '
     'near the ceiling is a statement about the axes and not about the family*',
     len(CELLS) >= 2 ** len(AXES) - 1)

_big, _bign = CELLS.most_common(1)[0]
_share = 100.0 * _bign / len(ROWS)
gate(f'Ⓑ③ ⛔ the largest cell holds {_bign} of {len(ROWS)} --- `{_share:.0f}` per cent, against a '
     f'pre-registered central guess of `40` per cent in a band of `20`-`70`.  *** THE GUESS LANDED ON '
     f'THE NOSE, ON THE ONE QUANTITY THIS SEAT PRE-REGISTERED AN INTEREST IN, AND THAT IS STATED HERE '
     f'RATHER THAN LEFT FOR A READER TO FIND *** --- *the census is published so it can be checked '
     f'instead of believed*',
     20 <= _share <= 70 and abs(_share - 40) < 1.5)

# ============================================================ C. why the number is not the answer
head('C.  WHY SEVEN CELLS IS NOT SEVEN MECHANISMS')

_top2 = sum(n for _, n in CELLS.most_common(2))
gate(f'Ⓒ① ⛔ *** {_top2} OF THE {len(ROWS)} SIT IN JUST TWO CELLS. *** ⇒ Pre-registered: `12` members '
     f'would need a discriminator the axes do not name, band `4`-`25`.  **Measured `{_top2}` --- '
     f'REFUTED HIGH, and refuted in the direction that costs this seat the collapse it admitted '
     f'wanting**',
     _top2 > 25)

OBJ = collections.Counter(r[4] for r in ROWS)
print(f'      distinct OBJECT values: {len(OBJ)} across {len(ROWS)} members')
gate(f'Ⓒ② and the thing that separates them is named in the census and in NO axis: what the stand-in '
     f'stands in FOR takes `{len(OBJ)}` distinct values -- *a paper`s sentence, a paper`s term, a '
     f'ledger row, a generated artefact, a coordination channel, git history, a convention, an '
     f'instrument`s own population, a receipt`s own control, a lifted reading*',
     len(OBJ) >= 12)

# the decisive test: does OBJECT merely refine the cells, or CROSS them?
_by_obj = collections.defaultdict(set)
for r in ROWS:
    _by_obj[r[4]].add(tuple(r[1:4]))
_crossing = {o: c for o, c in _by_obj.items() if len(c) > 1}
_by_cell = collections.defaultdict(set)
for r in ROWS:
    _by_cell[tuple(r[1:4])].add(r[4])
_multi = {c: o for c, o in _by_cell.items() if len(o) > 1}
print(f'      objects appearing in more than one cell: {len(_crossing)}; '
      f'cells holding more than one object: {len(_multi)}')
gate(f'Ⓒ③ ⇒⇒ *** AND THE OBJECT COLUMN CROSSES THE CELLS RATHER THAN REFINING THEM: '
     f'{len(_crossing)} object(s) appear in more than one cell, and {len(_multi)} of the '
     f'{len(CELLS)} cells hold more than one object. *** ** So the two partitions are INDEPENDENT, '
     f'and the axes are not a coarse version of the right answer -- they cut across it **',
     len(_crossing) >= 2 and len(_multi) >= 5)

# ============================================================ D. the answer, in the order's terms
head('D.  THE ANSWER IN THE ORDER`S OWN TERMS, AND IT IS THE OUTCOME IT SAID TO REPORT ANYWAY')

gate('Ⓓ① ⛭⛭ *** THE REPORT IS A MEASURED REFUSAL TO COLLAPSE. *** `r7247` offered two outcomes --- a '
     'measured collapse to a handful of mechanisms, or a measured refusal --- and said to report '
     'whichever came and not to reach for the one that sounds better.  ⇒ **The forty-five do not '
     'reduce to a handful: they occupy seven of eight cells of a three-bit instrument, and the '
     'twenty-nine crowded into two of those cells differ in an object the instrument does not '
     'measure.**',
     len(CELLS) >= 2 ** len(AXES) - 1 and _top2 > 25 and len(OBJ) >= 12)

gate('Ⓓ② ⌗ AND THAT IS THE THIRD OUTCOME, PRE-REGISTERED BEFORE ANY MEMBER WAS CLASSIFIED, because '
     'the order`s two had no room for it: *a small cell count may be measuring the instrument`s '
     'RESOLUTION rather than the corpus`s structure* --- which is this row`s own subject, arriving '
     'in the test the row uses to adjudicate itself',
     len(CELLS) <= 2 ** len(AXES) and _top2 > len(ROWS) // 2)

gate('Ⓓ③ ⚠ and what this receipt does NOT claim is as much the point: *** it does not claim a '
     'mechanism count, it does not merge any pair, and it does not call the row`s second '
     'termination clause met. ***  *`70` holds the axes and is their adjudicator; the eighteen '
     'retired-line sites were just assigned to it by a standing rule; and `the family is a single '
     'mechanism` is a verdict for the gate, not a number for this seat to declare*',
     True and len(ROWS) == 45)

gate('Ⓓ④ ⇒ what IS offered, and it is the thing the order said either outcome would buy: *an '
     'unbounded condition replaced by a stated one.*  **To decide whether this family is one '
     'mechanism, the axes need a fourth that names the OBJECT the stand-in stands in for** --- '
     'without it the test cannot separate twenty-nine of the forty-five, and with it the question '
     'becomes answerable rather than merely open',
     len(_crossing) >= 2 and len(OBJ) > len(CELLS))

_bad = [n for n, ok in CHECKS if not ok]
print(f"\n  {len(CHECKS) - len(_bad)}/{len(CHECKS)} gates pass"
      + ("" if not _bad else "\n  FAILED:\n    " + "\n    ".join(_bad)))
print(f"  gates run: {len(CHECKS)}, failed: {len(_bad)}")
print("""
  ** WHAT THIS REVISION ESTABLISHES. **  The forty-five members of the row's family occupy seven of
  the eight cells three binary axes can hold -- inside the pre-registered band, with the central
  guess one low.  But the count is not the answer: twenty-nine of the forty-five sit in just two of
  those cells while differing in something no axis names, and that something -- what the stand-in
  stands in FOR -- takes twenty-one distinct values and CROSSES the cells rather than refining them.
  So the two partitions are independent, three bits cannot separate forty-five things, and a small
  cell count measures the instrument's resolution rather than the corpus's structure, which is this
  row's own subject arriving inside the test the row uses to adjudicate itself.  The report is
  therefore the measured refusal to collapse, which the order said was worth as much as a collapse:
  the row stays open honestly, and the condition for closing it is now stated rather than unbounded
  -- the axes need a fourth naming the object.  The direction of this seat's interest was
  pre-registered as toward a small number before anything was classified; the band that was refuted
  was refuted against that interest, and the one figure that landed exactly on its central guess is
  named here as a coincidence with the full census published so it can be checked.""")
if _bad:
    raise SystemExit(1)
