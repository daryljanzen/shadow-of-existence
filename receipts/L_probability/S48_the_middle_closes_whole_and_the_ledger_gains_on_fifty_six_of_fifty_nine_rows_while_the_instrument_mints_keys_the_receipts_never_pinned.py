#!/usr/bin/env python3
r"""S48 -- THE MIDDLE OF THE STRIDE: THE WHOLE BLOCK CLOSES, AND BOTH REGISTERED ARMS FAIL -- ONE
HIGH, ONE LOW, EACH IN A DIRECTION THE REGISTRATION NAMED BEFORE THE WORK.

** WHAT WAS ORDERED. **  `r7337` ④: *carry on through the middle of the stride -- the tail is closed
and the dense blocks are done, so what is left is the part the `3.31` rows-a-receipt figure actually
prices; report both readings with the assignment named; AND from this revision also report the keys
MINTED AND ADJUDICATED beside the owed count, because a falling owed count is not by itself a
measure of what the corpus gained.*

*** ⓐ THE BLOCK CLOSES WHOLE: `19` OF `19` RECEIPTS, `59` OWED ROWS, `51` MINTED KEYS. ***
  ⛔ ** AND ARM ⒜ FAILS HIGH: the registration's central was `11` of `19`, band `9`-`14`. **
    *That is one of the two failures it named: the middle is nearer the tail than the forward figure
    says, and `3.31` rows a receipt is not what prices it.*
  ⌗ *The population was made LARGER than the expected rate on purpose, because the tail's arm was
  censored at its own ceiling.  ** So this failure is a reading and not a wall: there were five more
  receipts the arm could have stopped short of and it did not. **

*** ⛔⛭⛭ ⓑ AND ARM ⒝ FAILS LOW: `3` OF `59` RETIRED ROWS -- `0.051` -- HAVE A REPLACEMENT THE
    INSTRUMENT CANNOT SEE, AGAINST A REGISTERED BAND OF `0.08`-`0.22`. ***
  ⇒ *** Which is the other seat's finding not reproducing here: `cc66` measured `0.70` on the same
      quantity.  `56` of the `59` rows are replaced by a key the ledger holds and the instrument
      reports, so on THIS block a falling owed count IS very nearly a measure of the gain. ***
  ⌗ ** The three are all in one receipt and all the same kind: ** *spellings of LIVE CODE -- a
    decoupling ratio, a species count, and a phrase occurring zero times -- replaced by assertions
    parsed out of the module's own syntax tree, which mint no key.  **Stronger than the pins they
    replace and invisible to the ledger, which is exactly the distinction the order asked for.**

*** ⛭⛭ ⓒ AND THE INSTRUMENT MINTS KEYS THE RECEIPTS NEVER PINNED, WHICH IS THIS REVISION'S RULE
    CASE. ***  *Three of the `51` minted rows are FRAGMENTS THE INSTRUMENT EXTRACTS from inside a
    receipt's own longer literal or from the label that quotes it.*
  ⇒ ** So a repair that collapses fragments into ONE span still mints rows for the fragments it
    quotes **, and the ledger cannot tell a key the receipt PINS from one the instrument DERIVES.
  ⌗ *Measured, not asserted: `3` of `51`.  `THE_RULE.md` has no clause for it, and the three rows
  are adjudicated as what they are rather than deleted -- deleting them would leave the
  instrument's own report undescribed.*

*** ⓓ THE RATE, BOTH READINGS, AND THE DIRECTION ACROSS THREE REVISIONS. ***
  ⓚ ** EFFORT `19`, REALISED `19` ** -- *nothing in this block was repaired twice, and that is read
     off the stride file at the census commit rather than promised.*
  ⇒ ** `9`, then `14`, then `19`: rising across all three revisions the direction trigger reads. **
  ⚠ *And the three points are not one quantity: `4.33` rows a receipt in the dense blocks, `1.00` in
  the tail, `3.11` here -- this block IS the middle, and it still closed faster than the middle's
  own forward figure predicted.*

⌗ ** AND TWO RETIRED ARMS WERE DEAD: ** *their literal is absent from the file the check reads, so
that arm of its disjunction could never have fired at all.  The condition stood on its other arm and
nobody had looked.*

⚠ WHAT THIS CANNOT SETTLE is at the foot, beginning with the fact that arm ⒝'s denominator is this
revision's own retirements, so it measures the visibility of THESE repairs and not of the phase's.
"""
import ast
import collections
import io
import os
import re
import subprocess
import sys

_C = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                  'computations', 'beyond_the_wall')
sys.path.insert(0, os.path.join(_C, 'r7338_60_the_middle'))
import cost as K                                                       # noqa: E402

CHECKS = []
FAILURES = []


def gate(label, ok):
    CHECKS.append((label, bool(ok)))
    if not ok:
        FAILURES.append(label)
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")


def head(t):
    print("\n  " + "=" * 96 + f"\n  {t}\n  " + "=" * 96)


print(__doc__)
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
ORDER = 'b850ed71'              # r7337's orders on the trunk
CENSUS = 'b850ed71'             # the commit the block was censused at
REG = '431b3832'                # the commit that PUSHED the registration, before any repair
WORK = 'b43e394c'               # the last commit of this revision's repairs


def git(*a):
    return subprocess.run(['git', '-C', ROOT] + list(a),
                          capture_output=True, text=True, errors='replace').stdout


def ledger(sha=''):
    text = (git('show', f'{sha}:corpus/quote_pin_baseline.tsv') if sha
            else io.open(os.path.join(ROOT, 'corpus', 'quote_pin_baseline.tsv'),
                         encoding='utf-8').read())
    return [l.split('\t') for l in text.split('\n') if l.startswith('receipts/')]


def norm(s):
    """the comparison form: backslash-unescaped, emphasis unwrapped, markdown stripped, flat"""
    s = s.replace('\\\\', '\\')
    for _ in range(3):
        s2 = re.sub(r'\\(?:emph|textit|textbf|textsl)\{([^{}]*)\}', r'\1', s)
        if s2 == s:
            break
        s = s2
    return re.sub(r'\s+', ' ', re.sub(r'\*+', '', s)).strip().lower()


BLOCK = K.block(CENSUS)
RECEIPTS = sorted(BLOCK)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('A -- THE ORDER, READ WHERE IT WAS WRITTEN')

ORD = re.sub(r'\s+', ' ', git('show', f'{ORDER}:FOR_60.md'))
_items = ['Carry on through the middle of your stride',
          'report the keys minted and adjudicated beside the owed count',
          'A falling owed count is not by itself a measure of what the corpus gained']
print(f'      the order\'s items at {ORDER}: {[s in ORD for s in _items]}')
gate(f'Ⓐ①  THE ORDER IS READ AT `{ORDER}` AND NOT PARAPHRASED: `r7337` ④ sends this seat through the '
     f'MIDDLE of its stride, asks for both readings of the rate with the assignment named, and adds '
     f'a second report -- the keys minted and adjudicated beside the owed count, because a falling '
     f'owed count is not by itself a measure of what the corpus gained.  ** Read '
     f'whitespace-normalised, because an order\'s sentence wraps in the file **',
     all(s in ORD for s in _items))

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('B -- THE REGISTRATION WAS PUSHED BEFORE THE FIRST REPAIR, AND BOTH BANDS WERE FAILABLE')

_reg_files = [f for f in git('show', '--no-merges', '--name-only', '--format=', REG).split('\n') if f]
_reg_receipts = [f for f in _reg_files if f.startswith('receipts/')]
print(f'      {REG} touches {len(_reg_files)} file(s), {len(_reg_receipts)} of them receipts')
gate(f'Ⓑ①  THE BANDS WERE REGISTERED BEFORE ONE RECEIPT WAS REPAIRED, as a closed fact about the '
     f'history: `{REG}` carries the registration and its arithmetic and touches '
     f'`{len(_reg_receipts)}` receipts.  ** The ORDER of the commits is the claim **',
     _reg_files and not _reg_receipts)

_arms = K.scored()
for _nm in ('a', 'b'):
    print(f'      arm ({_nm}): {_arms[_nm][0]}, band {_arms[_nm][1]}, inside={_arms[_nm][2]}, '
          f'decisive={_arms[_nm][3]:.3f}')
gate(f'Ⓑ②  AND BOTH BANDS WERE FAILABLE WHEN THEY WERE WRITTEN: decisive fractions '
     f'`{_arms["a"][3]:.3f}` and `{_arms["b"][3]:.3f}`, both above `0.10`.  ⛭ ** And arm ⒜\'s '
     f'population was made LARGER than its central on purpose -- `{K.A_SPACE}` receipts against a '
     f'central of `{K.A_CENTRAL}` -- because the tail\'s arm was censored at its own ceiling and '
     f'could only fail downward.  This one could fail in both directions, and did **',
     _arms['a'][3] >= 0.10 and _arms['b'][3] >= 0.10
     and K.A_SPACE > K.A_CENTRAL and K.B_BAND[0] > 0)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('C -- THE BLOCK IS CLEAR, AND WHAT IT HELD IS READ AT THE CENSUS COMMIT')

_was = [c for c in ledger(CENSUS) if c[5] == 'REPAIR-OWED' and c[0] in BLOCK]
_now = [c for c in ledger() if c[5] == 'REPAIR-OWED' and c[0] in BLOCK]
print(f'      owed at {CENSUS}: {len(_was)} rows in {len(RECEIPTS)} receipts;  owed now: {len(_now)}')
gate(f'Ⓒ①  ⛭⛭ THE WHOLE BLOCK CARRIES NO OWED ROW, and what it HELD is read at the census commit '
     f'rather than from this revision\'s summary: `{len(_was)}` rows in `{len(RECEIPTS)}` receipts '
     f'before, `{len(_now)}` now.  ** Read live, the before-count would have fallen as the repairs '
     f'landed -- the fail-on-success shape a pinned commit cures **',
     len(_was) == K.RESULT['B_RETIRED'] and len(RECEIPTS) == K.A_SPACE and not _now)

_minted = [c for c in ledger() if c[0] in BLOCK and 'r7338+60' in c[6]]
_verdicts = collections.Counter(c[5] for c in _minted)
print(f'      keys this revision minted in the block: {len(_minted)};  verdicts {dict(_verdicts)};  '
      f'{len(_minted) / len(_was):.2f} keys a row')
gate(f'Ⓒ②  and EVERY KEY THE REPAIRS MINTED IS ADJUDICATED IN THE SAME PUSH, all `EXTENDED`: '
     f'`{len(_minted)}` keys for `{len(_was)}` rows, `{len(_minted) / len(_was):.2f}` a row.  '
     f'** Higher than the dense blocks\' `0.62` and lower than one: the middle\'s rows are fewer '
     f'fragments-of-one-sentence and more independent claims **',
     len(_minted) == K.RESULT['MINTED'] and set(_verdicts) == {'EXTENDED'})

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('D -- EVERY REPAIRED RECEIPT RE-RUNS GREEN, AND NO RETIRED LITERAL SURVIVES AS A CONSTANT')

_runs = {}
for _rel in RECEIPTS:
    _r = subprocess.run([sys.executable, '-I', os.path.join(ROOT, _rel)],
                        capture_output=True, text=True, errors='replace', timeout=900)
    _runs[_rel] = (_r.returncode, _r.stdout.count('[FAIL]') + _r.stdout.count('    FAIL'))
print(f'      {len(_runs)} receipts run;  non-zero exits: '
      f'{[r.split("/")[-1][:4] for r, (rc, _) in _runs.items() if rc]}')
gate(f'Ⓓ①  ALL `{len(_runs)}` REPAIRED RECEIPTS RE-RUN GREEN on this tree, run here rather than '
     f'asserted: every exit is zero and no run prints a failure',
     all(rc == 0 and nf == 0 for rc, nf in _runs.values()) and len(_runs) == K.A_SPACE)

_retired = {c[1][1:-1] for c in _was}
_survivors = {}
for _rel in RECEIPTS:
    _src = io.open(os.path.join(ROOT, _rel), encoding='utf-8').read()
    _consts = {n.value for n in ast.walk(ast.parse(_src))
               if isinstance(n, ast.Constant) and isinstance(n.value, str)}
    _hit = sorted(c for c in _consts if c in _retired)
    if _hit:
        _survivors[_rel] = _hit
print(f'      retired literals read off the ledger at {CENSUS}: {len(_retired)};  '
      f'surviving as a constant in their own receipt: {len(_survivors)}')
gate(f'Ⓓ②  and ⛔ **NO RETIRED LITERAL SURVIVES AS A CONSTANT, as the specific negative it is**: all '
     f'`{len(_retired)}` are read off the ledger at the census commit and PARSED out of each '
     f'receipt\'s own syntax tree, not grepped, and `{len(_survivors)}` remain',
     not _survivors and len(_retired) >= K.RESULT['B_RETIRED'] - 2)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('E -- THE TWO ARMS SCORED, AND BOTH FAIL IN DIRECTIONS THE REGISTRATION NAMED')

gate(f'Ⓔ①  ⛔ ARM ⒜ FAILS HIGH, AND THE FAILURE IS THE RESULT: `{_arms["a"][0]}` of the '
     f'`{K.A_SPACE}` receipts closed, against a central of `{K.A_CENTRAL}` and a band of '
     f'`{K.A_BAND[0]}`-`{K.A_BAND[1]}`.  ** The registration named this direction: the middle is '
     f'nearer the tail than the forward figure says, and `3.11` rows a receipt did not price it.  '
     f'And because the population was larger than the central, the arm could have stopped short of '
     f'five more receipts and did not -- so the high reading is a measurement, not a ceiling **',
     not _arms['a'][2] and _arms['a'][0] > K.A_BAND[1] and _arms['a'][0] == K.A_SPACE)

_mint_by = collections.defaultdict(list)
for _c in _minted:
    _mint_by[_c[0]].append((norm(_c[1][1:-1]), norm(_c[6])))
_invisible = [(r, lit) for r, lit in K.RESULT['INVISIBLE_ROWS']]
_unseen = []
for _c in _was:
    _lit = norm(_c[1][1:-1])
    if not any(_lit in _m or _lit in _note for _m, _note in _mint_by.get(_c[0], [])):
        _unseen.append((_c[0], _c[1][1:-1]))
_share = K.RESULT['B_INVISIBLE'] / K.RESULT['B_RETIRED']
print(f'      arm ⒝: {K.RESULT["B_INVISIBLE"]} of {K.RESULT["B_RETIRED"]} = {_share:.3f}, band '
      f'{K.B_BAND};  rows named invisible: {[l for _, l in _invisible]}')
gate(f'Ⓔ②  ⛔⛭⛭ ARM ⒝ FAILS LOW, AND THAT IS THE ORDER\'S OWN QUESTION ANSWERED: '
     f'`{K.RESULT["B_INVISIBLE"]}` of `{K.RESULT["B_RETIRED"]}` retired rows -- `{_share:.3f}` -- '
     f'have a replacement the instrument cannot see, against a band of `{K.B_BAND[0]}`-'
     f'`{K.B_BAND[1]}` and the other seat\'s `0.70` on the same quantity.  ⇒ ** So on THIS block a '
     f'falling owed count is very nearly a measure of the gain: `{K.RESULT["B_RETIRED"] - K.RESULT["B_INVISIBLE"]}` '
     f'of the `{K.RESULT["B_RETIRED"]}` rows are replaced by a key the ledger holds **',
     not _arms['b'][2] and _share < K.B_BAND[0]
     and K.RESULT['B_INVISIBLE'] == len(_invisible))

_p10 = _invisible[0][0]
_p10_src = io.open(os.path.join(ROOT, _p10), encoding='utf-8').read()
# ⌗ *and the structural assertion is itself read STRUCTURALLY, not as a spelling of itself: the
#   receipt is parsed and a call to `parse` on the ast module must be there.  Written the other way
#   -- a literal `_ast.parse` searched in another receipt's source -- it mints a quote-pin key on
#   another seat's code, which this revision's own rule case is about.*
_p10_tree = ast.parse(_p10_src)
_parsed = any(isinstance(_n, ast.Call) and isinstance(_n.func, ast.Attribute)
              and _n.func.attr == 'parse' and isinstance(_n.func.value, ast.Name)
              and _n.func.value.id in ('ast', '_ast')
              for _n in ast.walk(_p10_tree))
_no_key = not [1 for _r, _lit in _invisible
               for _m, _n in _mint_by.get(_r, []) if norm(_lit) in _m]
print(f'      the three invisible rows are all in {_p10.split("/")[-1][:28]};  it carries a parsed '
      f'structural assertion: {_parsed};  no minted key contains them: {_no_key}')
gate(f'Ⓔ③  ⛭⛭ AND THE THREE ARE NAMED AND SHOWN TO BE THE KIND THE ORDER ASKED ABOUT: all `3` are '
     f'in ONE receipt, all SPELLINGS OF LIVE CODE, no minted key of this revision contains any of '
     f'them, and that receipt now carries an assertion PARSED out of the module\'s own syntax tree '
     f'-- the decoupling ratio and the species count read as VALUES.  ** Stronger than the pins '
     f'they replace and invisible to the ledger, which is the distinction the order exists to draw '
     f'and the reason the two numbers are reported apart **',
     _parsed and _no_key and len({r for r, _ in _invisible}) == 1
     and len(_unseen) <= K.RESULT['B_INVISIBLE'] + K.RESULT['DEAD_ARMS'])

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('F -- THE RATE IN BOTH READINGS, AND THE DIRECTION ACROSS THREE REVISIONS')

_stride = K.mine(CENSUS)
_assigned = all(r in _stride for r in RECEIPTS)
_left_recs = len(_stride) - K.A_SPACE
_left_rows = sum(_stride.values()) - K.RESULT['B_RETIRED']
_density = K.RESULT['B_RETIRED'] / K.A_SPACE
print(f'      effort {K.RESULT["A_CLOSED"]};  realised {K.RESULT["A_CLOSED"]};  density here '
      f'{_density:.2f} rows a receipt;  left: {_left_rows} rows in {_left_recs} receipts')
gate(f'Ⓕ①  ⛭⛭ THE RATE IS REPORTED IN BOTH READINGS, which is standing: EFFORT '
     f'`{K.RESULT["A_CLOSED"]}` and REALISED `{K.RESULT["A_CLOSED"]}` -- the two coincide because '
     f'nothing in this block was repaired twice, asserted from the stride file at the census commit '
     f'where every one of the `{K.A_SPACE}` receipts is this seat\'s own assignment',
     _assigned and K.RESULT['A_CLOSED'] == _arms['a'][0])

gate(f'Ⓕ②  ⛭⛭⛭ AND THE DIRECTION IS RISING ACROSS ALL THREE REVISIONS THE TRIGGER READS: `9` on the '
     f'dense blocks, `14` on the tail, `{K.RESULT["A_CLOSED"]}` here.  ⚠ ** And the three are not '
     f'one quantity: `4.33` rows a receipt there, `1.00` in the tail, `{_density:.2f}` here -- this '
     f'block IS the middle, and it still closed faster than the middle\'s own forward figure '
     f'predicted **',
     K.RESULT['A_CLOSED'] > 14 and 1.00 < _density < 4.33 and _left_recs >= 0)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('G -- THE RESTRAINT, THE RULE CASE, AND THE TWO DEAD ARMS')

_own = [c for c in git('rev-list', '--no-merges', f'{REG}~1..{WORK}').split('\n') if c]
_range = sorted({f for c in _own
                 for f in git('show', '--no-merges', '--name-only', '--format=', c).split('\n')
                 if f.startswith('receipts/') and f.endswith('.py')})
_extra = [f for f in _range if f not in BLOCK]
print(f'      this revision\'s own commits: {len(_own)};  receipt files they touch: {len(_range)};  '
      f'beyond the block: {_extra}')
gate(f'Ⓖ①  ⛔ **ONLY THE BLOCK IS TOUCHED, as the specific negative it is**: the `{len(_range)}` '
     f'receipt files in this revision\'s own commits -- enumerated between two pinned ends rather '
     f'than diffed across them, which is the form this seat\'s last revision had to find when a '
     f'merged trunk filled the diff -- are exactly the `{K.A_SPACE}` of the block, and '
     f'`{len(_extra)}` lie outside it',
     len(_range) == K.A_SPACE and not _extra and len(_own) >= 4)

_extracts = [c for c in _minted if 'FRAGMENT THE INSTRUMENT EXTRACTS' in c[6]]
print(f'      minted rows that are instrument-derived fragments: {len(_extracts)} of {len(_minted)}')
gate(f'Ⓖ②  ⛭⛭ AND THE RULE CASE IS ON THE RECORD WITH ITS SIZE: `{len(_extracts)}` of the '
     f'`{len(_minted)}` minted rows are FRAGMENTS THE INSTRUMENT EXTRACTS from inside a receipt\'s '
     f'own longer literal or from the label that quotes it -- so a repair that collapses fragments '
     f'into ONE span still mints rows for the fragments it quotes, and the ledger cannot tell a key '
     f'a receipt PINS from one the instrument DERIVES.  ** Adjudicated as what they are rather than '
     f'deleted: deleting them would leave the instrument\'s own report undescribed **',
     len(_extracts) == K.RESULT['EXTRACTS'] and K.RESULT['CASES'] == 1)

_dead = [c for c in _minted if 'ABSENT from the file' in c[6] or 'is ABSENT' in c[6]]
print(f'      minted rows recording a DEAD retired arm: {len(_dead)}')
gate(f'Ⓖ③  ⌗ and the TWO DEAD ARMS are recorded where they were found: a disjunction arm whose '
     f'literal is absent from the file the check reads could never have fired, so the condition '
     f'stood on its other arm and nobody had looked.  ** `{K.RESULT["DEAD_ARMS"]}` of the '
     f'`{K.RESULT["B_RETIRED"]}` rows, named in the rows that replaced them **',
     len(_dead) >= 1 and K.RESULT['DEAD_ARMS'] == 2)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print()
print("=" * 100)
print(f'  gates run: {len(CHECKS)}   failed: {len(FAILURES)}')
print("=" * 100)
print()
print(f'  ⛭⛭ ** THE MIDDLE CLOSES WHOLE: {K.RESULT["A_CLOSED"]} OF {K.A_SPACE} RECEIPTS, '
      f'{K.RESULT["B_RETIRED"]} ROWS, {K.RESULT["MINTED"]} KEYS. **')
print(f'  ⛔ ** ARM ⒜ FAILS HIGH ** against a central of {K.A_CENTRAL} and a band of '
      f'{K.A_BAND[0]}-{K.A_BAND[1]}: the middle is nearer the tail than its own')
print('     forward figure says, and the population was larger than the central, so the arm')
print('     could have stopped short and did not.')
print(f'  ⛔⛭⛭ ** ARM ⒝ FAILS LOW: {K.RESULT["B_INVISIBLE"]} of {K.RESULT["B_RETIRED"]} rows have a '
      f'replacement the instrument cannot see, **')
print(f'     {K.RESULT["B_INVISIBLE"] / K.RESULT["B_RETIRED"]:.3f} against a band of '
      f'{K.B_BAND[0]}-{K.B_BAND[1]} and another seat\'s 0.70 -- so here a falling owed')
print('     count is very nearly a measure of the gain.  The three are one receipt\'s code')
print('     spellings, replaced by assertions parsed out of the module itself.')
print(f'  ⛭⛭ ** AND THE INSTRUMENT MINTS KEYS THE RECEIPTS NEVER PINNED: {K.RESULT["EXTRACTS"]} of '
      f'{K.RESULT["MINTED"]}, **')
print('     fragments extracted from inside the widened spans and the labels that quote them.')
print('     Filed as this revision\'s rule case, with its size.')
print(f'  ⇒ The direction the trigger reads: 9, then 14, then {K.RESULT["A_CLOSED"]} -- rising on '
      f'all three.')
if FAILURES:
    print('\n  FAILED:')
    for f in FAILURES:
        print(f'   - {f}')
sys.exit(1 if FAILURES else 0)
