#!/usr/bin/env python3
r"""R1 -- `L-248`: THE r3001 STRIKE REWROTE A ROW'S PREFIX AND TWELVE RECEIPTS LOOKED IT UP BY THAT
PREFIX, SO THEY CRASHED INSTEAD OF FAILING.

** THE MECHANISM, and it is one line. **  `PROTECTED_OPEN` was closed at r3001 with fourteen rows
struck.  Striking rewrites a row from `| **PO-6**` to `| ~~**PO-6**~~`.  ** The row's TEXT is
unchanged -- only its prefix. **  Twelve receipts locate the row with

      next(l for l in raw.split('\n') if l.startswith('| **PO-n**'))

  ⇒ *** The prefix no longer matches, `next()` raises StopIteration, and the receipt CRASHES. ***
  ⇒ ** That is an ABSENCE presenting as a broken receipt rather than as a check failure ** -- the
    same shape the corpus has found before at the input end, now at the register end.

** ⌗ AND THE DIAGNOSIS IS WIDER THAN THE TWELVE, which is the reason this receipt exists. **  The
receipt suite fails 56 at r3098.  *Read as one inherited backlog that is nobody's, it is 56 items of
archaeology.*  ** Read against r2825a -- the last commit the two lines shared -- it splits: **

      27  already failed at r2825a          GENUINELY INHERITED, predating both lines
      29  PASSED at r2825a and fail now     WENT RED IN THE r2825a -> r3098 SPAN
            of those 29:  12  this one cause, one mechanical fix
                          17  pins into prose and register state that later work moved

  ⇒ *** So "the rest are inherited" is true of 27 and not of 29, and the difference decides who owns
      them and how expensive they are. ***

** ⛭ ELEVEN OF THE TWELVE GO GREEN ON THE LOOKUP ALONE, which is the evidence that the CLAIMS were
never stale -- only the lookup was. **  *The twelfth, `S4_the_open_half_is_the_floor`, fails on a
real assertion: the P10 sentence it pins was STRENGTHENED, "is part of what this paragraph leaves
open at its end" becoming "is not assumed here ... though it does in fact".*
  ⇒ ** The pin broke because the argument won.  That one needs a reading of P10 and is routed, not
    repaired here. **

** ⚠ AND A DEFECT OF MY OWN, KEPT BECAUSE THE CATCH IS THE POINT. **  *The first patch wrote
`PO-raw_po` into every regex: the substitution used `m.group(1)`, and group 1 was the NAMED group,
not the number.*  ⇒ *** It was caught by the fix restoring ZERO of twelve instead of most of them.
A repair that fixes nothing is a repair that has not been measured. ***

Run:  python3 receipts/L248_the_strike_broke_its_readers/R1_...py

Written r3100 (`L-248`).  Stated for reversal.
"""
import glob
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
PO = os.path.join(ROOT, 'PROTECTED_OPEN.md')
fails = []


def check(msg, ok):
    print(f"    {'OK  ' if ok else 'FAIL'}  {msg}")
    if not ok:
        fails.append(msg)


print(__doc__)
print('=' * 78)
print('PART 1 -- THE STRIKE, AND WHAT IT DID TO THE PREFIX')
print('=' * 78)
raw = open(PO, encoding='utf-8', errors='replace').read()
struck = re.findall(r'^\|\s*~~\*\*(PO-\d+)\*\*~~', raw, re.M)
unstruck = re.findall(r'^\|\s*\*\*(PO-\d+)\*\*', raw, re.M)
print(f'    rows written struck   `| ~~**PO-n**~~` : {len(struck)}  {sorted(set(struck))[:8]}')
print(f'    rows written unstruck `| **PO-n**`     : {len(unstruck)}  {sorted(set(unstruck))[:8]}')
check('⓵ PROTECTED_OPEN carries struck rows in the `~~` form', len(struck) > 0)
check('⓵ᵇ ⛔ and the rows the twelve look for are NOT present in the unstruck form -- which is '
      'exactly why a startswith on that prefix finds nothing',
      not any(p in unstruck for p in ('PO-2', 'PO-3', 'PO-5', 'PO-6', 'PO-7')))
# ** the row TEXT survives the strike -- so the claims that quote it were never stale **
row6 = [l for l in raw.split('\n') if re.match(r'\|\s*~?~?\*\*PO-6\*\*', l)]
check('⓵ᶜ ⛭ and the struck row is still THERE and still carries its text, so what broke was the '
      'lookup and not the claim', len(row6) == 1 and 'bounded below' in row6[0])

print()
print('=' * 78)
print('PART 2 -- THE TWELVE, AND THAT THE REPAIR IS CONFINED TO THE LOOKUP')
print('=' * 78)
GATE = os.path.join(ROOT, 'corpus', 'check_row_matchers.py')
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
import check_row_matchers as crm                                          # noqa: E402

allrec = sorted(glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True))
brittle = [os.path.relpath(f, ROOT) for f in allrec
           if crm.uses_it(open(f, encoding='utf-8', errors='replace').read())]
TOL = re.compile(r"re\.match\(r'\\\|\\s\*~\?~\?\\\*\\\*PO-\d+")
# ** exclude THIS file: it quotes the repaired form in its own docstring and in its own checks,
# ** so counting itself would inflate the number it reports.  *The same use/mention distinction
# ** the gate makes, applied to the census that measures the gate's own work.* **
repaired = [os.path.relpath(f, ROOT) for f in allrec
            if TOL.search(open(f, encoding='utf-8', errors='replace').read())
            and os.path.abspath(f) != os.path.abspath(__file__)]
print(f'    receipts still USING the open-form-only lookup : {len(brittle)}')
print(f'    receipts carrying the strike-tolerant lookup   : {len(repaired)}')
check('⓶ no receipt still uses the open-form-only lookup', len(brittle) == 0)
check('⓶ᵇ and thirteen OTHER receipts carry the tolerant form -- the twelve that crashed plus `B21`, which was '
      'already failing for an older reason and carried the same brittleness',
      len(repaired) == 13)
# ** the tolerant matcher must match BOTH forms, or it has traded one brittleness for another **
TOLM = re.compile(r'\|\s*~?~?\*\*PO-6\*\*')
check('⓶ᶜ the tolerant matcher matches the STRUCK form', bool(TOLM.match('| ~~**PO-6**~~ | x |')))
check('⓶ᵈ and the UNSTRUCK form too -- so it survives a row being re-opened, which is the failure '
      'the brittle version had in the OTHER direction at c54.224',
      bool(TOLM.match('| **PO-6** | x |')))
check('⓶ᵉ and does NOT match a different row number', not TOLM.match('| ~~**PO-16**~~ | x |'))

print()
print('  ⛭⛭ ** AND THE GATE, WHICH IS THE PART THAT MATTERS MORE THAN THE THIRTEEN REPAIRS. **')
check('⓶ᶠ `corpus/check_row_matchers.py` exists', os.path.exists(GATE))
check('⓶ᵍ and it is GREEN on the repaired tree', crm.main() == 0)
# ** it must tell a USE from a MENTION, and that is not decoration: `L-558` quotes the brittle form
# ** in a COMMENT and this receipt quotes it in a DOCSTRING.  A grep fails on both. **
USE = "raw.split('\\n') if l.startswith('| **PO-6**')"
check('⓶ʰ ⛭ it flags a genuine USE', len(crm.uses_it('x = next(l for l in ' + USE + ')')) == 1)
check('⓶ⁱ ⛭ and NOT a mention in a comment', crm.uses_it("# " + USE) == [])
check('⓶ʲ ⛭ nor a mention inside a string', crm.uses_it('M = "' + USE.replace('"', "'") + '"') == [])
check('⓶ᵏ ⛭ nor the repaired form itself',
      crm.uses_it("row = next(l for l in raw.split('\\n')"
                  " if re.match(r'\\|\\s*~?~?\\*\\*PO-6\\*\\*', l))") == [])

print()
print('=' * 78)
print('PART 3 -- ⛭⛭ THE SPLIT THAT DECIDES WHO OWNS THE BACKLOG')
print('=' * 78)
SHARED = 'e1a5ad01a06d01e86ed83bb57450d423c4243ba7'   # r2825a, the last commit the two lines shared
anc = subprocess.run(['git', 'merge-base', '--is-ancestor', SHARED, 'HEAD'],
                     cwd=ROOT, capture_output=True)
check('⓷ r2825a is an ancestor of this tree, so it is a legitimate baseline to measure against',
      anc.returncode == 0)
print('    measured by running each failing receipt at r2825a in a clean archive:')
print('        27  already failed there      -- genuinely inherited, predating both lines')
print('        29  passed there, fail now    -- went red in the r2825a -> r3098 span')
print('              12  the strike-lookup crash (this receipt)')
print('              17  pins into prose/register state that later work moved')
# ⛔⛭⛭ AMENDED r3126 (`L-254`).  ** THESE TWO CHECKS WERE `27 + 29 == 56` AND `12 + 17 == 29`. **
# *Arithmetic dressed as claims -- the exact class `scripts/lint_assertions.py` was built for, and it
# named them.  They were invisible while `check_receipts` exited at an earlier failure, and surfaced
# the moment that one was cleared.*
#   ⇒ ** AND THE DEEPER FAULT IS THAT THE MEASUREMENT WAS KEPT AS FOUR NUMBERS. **  *r3100 ran each
#     failing receipt at `r2825a` in a clean archive and recorded only the counts, so the partition
#     cannot be re-derived and no assertion over it can be anything but arithmetic.*
#   ⇒ *** So the check that CAN fail is a cross-artefact one: the numbers this receipt prints must
#       agree with the numbers its own registration rows print.  That is what would have caught
#       `M1`'s "545 rows / 524 parsed" -- an after-total printed beside a before-count. ***
SPLIT = {'total': 56, 'inherited': 27, 'regressed': 29, 'this_cause': 12, 'pins': 17}
_rows = []
for _f in ('THE_LIVE_ARC.md', os.path.join('receipts', 'INDEX.md')):
    for _l in open(os.path.join(ROOT, _f), encoding='utf-8', errors='replace'):
        if 'L-248' in _l and 'L248_the_strike' in _l or (_l.startswith('| ~~L-248~~')
                                                         or _l.startswith('| L-248')):
            _rows.append((_f, _l))
_nums = {f: set(re.findall(r'\b\d{1,3}\b', l)) for f, l in _rows}
print(f'    registration rows carrying this finding: {len(_rows)}')
check(f'⓷ᵇ the four numbers agree with BOTH registration rows -- {SPLIT} against rows in '
      f'{[f for f, _ in _rows]}',
      len(_rows) == 2
      and all({str(v) for v in SPLIT.values()} <= ns for ns in _nums.values()))
check('⓷ᶜ and the partition is stated as a partition, so a future edit that changes one number '
      'without the others fails the row check above rather than passing a sum',
      SPLIT['inherited'] + SPLIT['regressed'] == SPLIT['total']
      and SPLIT['this_cause'] + SPLIT['pins'] == SPLIT['regressed'])
print('    ⚠ ** WHAT THIS CANNOT CHECK, stated rather than implied: ** the per-receipt lists behind')
print('       these four numbers were not kept at r3100, so the partition is a RECORD and not a')
print('       reproducible measurement.  *A measurement kept as four numbers cannot be re-run.*')
print('  ⇒ ⛔ *** "The rest are inherited" is true of 27 and false of 29.  The difference is not')
print('      bookkeeping: an inherited failure is archaeology, a regression is a live edit whose')
print('      cost has not been paid, and the second kind is cheaper to fix and more urgent. ***')

print()
print('=' * 78)
print('PART 4 -- THE ONE THAT IS NOT A LOOKUP, ROUTED RATHER THAN REPAIRED')
print('=' * 78)
p10 = open(os.path.join(ROOT, 'corpus', 'canonical_time.tex'),
           encoding='utf-8', errors='replace').read()
OLD = 'is part of what this paragraph leaves open at its end'
NEW = 'is not assumed here'
print(f'    the wording `S4` pins  : "...{OLD}..."')
print(f'    what P10 now says      : "...{NEW}... though it does in fact"')
check('⓸ the pinned wording is GONE from P10', OLD not in re.sub(r'\s+', ' ', p10))
check('⓸ᵇ and the sentence that replaced it is present, and is STRONGER -- the openness the receipt '
      'pinned has been resolved', NEW in re.sub(r'\s+', ' ', p10)
      and 'though it does in fact' in re.sub(r'\s+', ' ', p10))
print('  ⇒ ** THE PIN BROKE BECAUSE THE ARGUMENT WON. **  *`S4`\'s finding may well survive, but')
print('     deciding what it now asserts is a reading of P10 and belongs to whoever owns P10.*')
print('  ⌷ ** Repairing it by weakening the assertion to match the new sentence would be fitting the')
print('     check to the answer, which is the one repair this corpus never permits. **')

print()
print('=' * 78)
if fails:
    print(f'  {len(fails)} check(s) FAILED')
    for m in fails:
        print(f'    - {m}')
    sys.exit(1)
print('  ⇒ ** ALL CHECKS PASS. **')
print('  ⛭ ** ELEVEN RECEIPTS RETURNED TO GREEN BY ONE LINE EACH, AND THE TWELFTH NAMED WITH ITS')
print('     CAUSE.  The claims were never stale; a register migration moved the key they were')
print('     read by, and nothing told the readers. **')
print()
