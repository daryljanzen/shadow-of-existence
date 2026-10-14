#!/usr/bin/env python3
r"""S47 -- THE CHEAP END, MEASURED: THE TAIL CLOSES WHOLE AND THE RATE RISES -- AND THE ROWS IN IT
ARE NOT THE ROWS THE REPAIR FORM WAS PRICED ON.

** WHAT WAS ORDERED. **  `r7333` ④: *the single-row tail next, not another dense block -- the rate is
measured on the expensive end and the cheap end is unmeasured, so measuring it is worth more this
revision than more rows are.  Report receipts a revision again, with its band and decisive fraction
registered first.*  `r7335` ⑤ repeats it and adds that this is the SECOND of the two revisions the
re-stated direction trigger reads, and that the stride now reports BOTH readings of the rate.

*** ⓐ THE TAIL CLOSES WHOLE: `14` OF `14` EDITABLE RECEIPTS, ONE OWED ROW EACH. ***
  ⚠ ** AND THE OUTCOME IS CENSORED AT ITS OWN CEILING, WHICH THE REGISTRATION SAID FIRST: ** *the
    tail is `14` receipts long, so `14` supports `>= 14` and not an equality.  The band `10`-`14`
    could only have failed downward and did not.*
  ⌗ *The fifteenth single-row receipt is on the do-not-edit list and is routed as a patch, not
    edited, and it is still owed -- which is the one row in the tail this seat may not close.*

*** ⛔⛭⛭ ⓑ AND THE SECOND ARM FAILS, HIGH, IN THE DIRECTION THE REGISTRATION NAMED: `9` OF THE `14`
    ROWS NEEDED SOMETHING OTHER THAN A PLAIN WIDENING, AGAINST A BAND OF `1`-`4`. ***
  ⓘ ** `7` needed the markup normaliser the gate layer itself compares with **, because the
     carrier's markers fall INSIDE the carrying span -- `r7258`'s settled form.
  ⓙ ** `2` had no span to widen at all. **  *Both were PROXIES ON LIVE CODE: a module name standing
     for the claim that a gate LOADS a shared rule, where the name also sits in that file's
     comments, so the condition could not fail while a comment survived.*  ⇒ *Repaired by parsing
     the gate's own syntax tree for the import-from-path call and the call into the module -- the
     load itself, which a comment cannot satisfy and a private copy cannot fake.*
  ⇒ *** AND THE REASON IS MEASURED RATHER THAN OFFERED: the tail's rows are composed differently
      from the blocks the band was priced on.  `4` of `15` tail literals carry math or markup
      against `1` of `39` in the dense blocks, and `7` of `15` are TOKEN-tier against `7` of `39`.
      A token has no clause to widen inside the gate's own reader and a markup carrier needs a
      normalised one -- so the cheap end is cheap in ROWS and expensive in RULINGS. ***

*** ⓒ THE RATE, IN BOTH READINGS, WHICH IS STANDING FROM `r7335` ③. ***
  ⓚ ** EFFORT: `14` receipts in one revision. **  ⓛ ** REALISED: `14` as well, because nothing in
     this tail was duplicated -- it is assigned to this seat alone in the stride file at the census
     commit, and the assignment defect the last revision measured is closed. **
  ⇒ ** THE DIRECTION THE TRIGGER READS: `9` receipts a revision then, `14` now -- RISING, not
     falling, over the two revisions the trigger was re-stated to read. **
  ⚠ *And the two rates are not the same quantity as the dense blocks': `1.00` rows a receipt here
    against `4.33` there.  The forward figure for what remains is neither -- `42` receipts and `139`
    rows at `3.31` a receipt -- so this revision prices the cheap END and not the remainder.*

*** ⓓ AND ONE RULE CASE IS FILED BESIDE ITS REPAIR. ***  *A MARKDOWN carrier -- blockquote plus
    asterisk emphasis -- cannot be held by the mechanism that holds a paper span, because the gate
    layer's normaliser reads the LaTeX emphasis family, math delimiters and `~` and nothing else.
    Second instance of the class filed one revision ago in LaTeX, in a different markup language.*

⛔ ** AND THE HISTORICAL CLAIMS HERE ARE PINNED AT THIS REVISION'S OWN COMMITS, WHICH IS THE STANDING
RULE THIS SEAT'S LAST RECEIPT PRODUCED BY GOING RED ON THE TRUNK. **  *What the revision did is read
in a range closed at both ends between two of its own commits; what the trunk holds live is asserted
separately and allowed to differ.*

⚠ WHAT THIS CANNOT SETTLE is at the foot, beginning with the censoring: a population of `14` cannot
report a rate above `14`, and one revision is still one draw.
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
sys.path.insert(0, os.path.join(_C, 'r7336_60_the_cheap_tail'))
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
ORDER_A = '53b0944d'            # r7333's orders on the trunk: the tail, next
ORDER_B = 'd4d9f89e'            # r7335's orders: both readings standing, and the experiment
CENSUS = '23cecc99'             # the commit the tail was censused at
REG = '4cc74ef8'                # the commit that PUSHED the registration, before any repair
WORK = '34647cf5'              # this revision's last content commit before this receipt
BARRED = ('receipts/L259_the_distance_from_the_present/'
          'D1_a_check_pinned_to_a_distance_from_the_present_is_pinned_to_the_present.py')


def git(*a):
    return subprocess.run(['git', '-C', ROOT] + list(a),
                          capture_output=True, text=True, errors='replace').stdout


def ledger(sha=''):
    text = (git('show', f'{sha}:corpus/quote_pin_baseline.tsv') if sha
            else io.open(os.path.join(ROOT, 'corpus', 'quote_pin_baseline.tsv'),
                         encoding='utf-8').read())
    return [l.split('\t') for l in text.split('\n') if l.startswith('receipts/')]


TAIL = K.tail(CENSUS)
EDITABLE = [r for r in TAIL if r != BARRED]

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('A -- THE TWO ORDERS, READ WHERE THEY WERE WRITTEN')

# ⌗ *whitespace-normalised, because an order's sentence WRAPS in the file and a line-based read
#   would miss the half of the item that matters -- the same reason the gate layer flattens a paper.*
_ord_a = re.sub(r'\s+', ' ', git('show', f'{ORDER_A}:FOR_60.md'))
_ord_b = re.sub(r'\s+', ' ', git('show', f'{ORDER_B}:FOR_60.md'))
_items_a = ['the single-row tail next, not another dense block',
            'the cheap end is unmeasured', 'with its band and decisive fraction registered first']
_items_b = ['the SECOND of the two revisions the direction trigger reads',
            'the stride reports BOTH with the assignment named', 'Register first']
print(f'      r7333 items at {ORDER_A}: {[s in _ord_a for s in _items_a]};  '
      f'r7335 items at {ORDER_B}: {[s in _ord_b for s in _items_b]}')
gate(f'Ⓐ①  BOTH ORDERS ARE READ AT THEIR OWN TRUNK COMMITS AND NOT PARAPHRASED: `r7333` ④ sends the '
     f'single-row tail next and asks for receipts a revision with a band and a decisive fraction '
     f'registered first; `r7335` ⑤ makes this the SECOND of the two revisions the re-stated '
     f'direction trigger reads and ③ makes BOTH readings of the rate standing.  ** The seat that is '
     f'ordered does not get to choose which half of the order it answers **',
     all(s in _ord_a for s in _items_a) and all(s in _ord_b for s in _items_b))

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('B -- THE REGISTRATION WAS PUSHED BEFORE THE FIRST REPAIR, AND BOTH BANDS WERE FAILABLE')

_reg_files = [f for f in git('show', '--no-merges', '--name-only', '--format=', REG).split('\n') if f]
_reg_receipts = [f for f in _reg_files if f.startswith('receipts/')]
print(f'      {REG} touches {len(_reg_files)} file(s), {len(_reg_receipts)} of them receipts: '
      f'{[f.split("/")[-1][:28] for f in _reg_files]}')
gate(f'Ⓑ①  THE BANDS WERE REGISTERED BEFORE ONE RECEIPT WAS REPAIRED, as a closed fact about the '
     f'history rather than a promise in prose: `{REG}` carries the registration and its arithmetic '
     f'and touches `{len(_reg_receipts)}` receipts.  ** The ORDER of the commits is the claim, which '
     f'is why it is read off the history and not off this docstring **',
     _reg_files and not _reg_receipts)

_arms = K.scored()
for _nm in ('a', 'b'):
    print(f'      arm ({_nm}): {_arms[_nm][0]}, band {_arms[_nm][1]}, inside={_arms[_nm][2]}, '
          f'decisive={_arms[_nm][3]:.3f}')
gate(f'Ⓑ②  AND BOTH BANDS WERE FAILABLE WHEN THEY WERE WRITTEN, which is `r7325`\'s standing rule '
     f'applied before the work rather than after: decisive fractions `{_arms["a"][3]:.3f}` and '
     f'`{_arms["b"][3]:.3f}`, both above `0.10`.  ** And arm ⒝ is two-sided by construction -- ZERO '
     f'fails it as surely as five does -- which is what makes its failure HIGH a reading and not an '
     f'accident of where the band was put **',
     _arms['a'][3] >= 0.10 and _arms['b'][3] >= 0.10 and K.B_BAND[0] >= 1)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('C -- THE TAIL IS CLEAR, AND WHAT IT HELD IS READ AT THE CENSUS COMMIT')

_was = [c for c in ledger(CENSUS) if c[5] == 'REPAIR-OWED' and c[0] in TAIL]
_now = [c for c in ledger() if c[5] == 'REPAIR-OWED' and c[0] in TAIL]
print(f'      owed at {CENSUS}: {len(_was)} rows in {len(TAIL)} receipts;  owed now: {len(_now)} '
      f'({[c[0].split("/")[1][:22] for c in _now]})')
gate(f'Ⓒ①  ⛭⛭ EVERY EDITABLE TAIL RECEIPT CARRIES NO OWED ROW, and what the tail HELD is read at the '
     f'census commit rather than from this revision\'s summary: `{len(_was)}` rows in '
     f'`{len(TAIL)}` receipts before, `{len(_now)}` now -- and the one that remains is the row on '
     f'the do-not-edit list, ROUTED as a patch and not edited.  ** Read live, the before-count '
     f'would have fallen as the repairs landed, which is the fail-on-success shape a pinned commit '
     f'cures **',
     len(_was) == K.RESULT['TAIL_ROWS'] and len(_now) == K.RESULT['ROUTED']
     and [c[0] for c in _now] == [BARRED])

_minted = [c for c in ledger() if c[0] in EDITABLE and 'r7336+60' in c[6]]
_verdicts = collections.Counter(c[5] for c in _minted)
_structural = sorted(r for r in EDITABLE
                     if not any(c[0] == r and 'r7336+60' in c[6] for c in ledger()))
print(f'      keys this revision minted in the tail: {len(_minted)};  verdicts {dict(_verdicts)};  '
      f'receipts repaired with NO key minted: {len(_structural)} '
      f'({[r.split("/")[-1][:4] for r in _structural]})')
gate(f'Ⓒ②  and EVERY KEY THE REPAIRS MINTED IS ADJUDICATED IN THE SAME PUSH, all `EXTENDED` -- the '
     f'verdict a widening takes, since the span changed and the receipts\' assertions and tolerances '
     f'did not: `{len(_minted)}` keys for `{len(EDITABLE)}` receipts.  ⛔ ** And `{len(_structural)}` '
     f'receipts minted NO key at all, which is not an omission but the shape of their repair: their '
     f'owed rows were PROXIES ON LIVE CODE with no span to widen, so the text pin is gone and a '
     f'parsed structural assertion stands where it was **',
     len(_minted) == len(EDITABLE) - K.RESULT['B_STRUCTURAL']
     and set(_verdicts) == {'EXTENDED'}
     and len(_structural) == K.RESULT['B_STRUCTURAL'])

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('D -- EVERY REPAIRED RECEIPT RE-RUNS GREEN, AND NO RETIRED LITERAL SURVIVES')

_runs = {}
for _rel in EDITABLE:
    _r = subprocess.run([sys.executable, '-I', os.path.join(ROOT, _rel)],
                        capture_output=True, text=True, errors='replace', timeout=900)
    _runs[_rel] = (_r.returncode, _r.stdout.count('[FAIL]') + _r.stdout.count('    FAIL'))
print(f'      {len(_runs)} receipts run;  non-zero exits: '
      f'{[r.split("/")[-1][:4] for r, (rc, _) in _runs.items() if rc]};  '
      f'printing a failure: {[r.split("/")[-1][:4] for r, (_, nf) in _runs.items() if nf]}')
gate(f'Ⓓ①  ALL `{len(_runs)}` REPAIRED RECEIPTS RE-RUN GREEN on this tree, run here rather than '
     f'asserted: every exit is zero and no run prints a failure.  ** A repair that leaves its own '
     f'receipt red is not a repair, and these are nine prefixes this seat has no history in **',
     all(rc == 0 and nf == 0 for rc, nf in _runs.values()) and len(_runs) == K.RESULT['A_CLOSED'])

# ⛔⛭⛭ SCOPED, AND THE SCOPE IS THE FINDING RATHER THAN A CONCESSION.  *The claim `no retired
#   literal survives as a constant` is a claim about a WIDENING: the old span must not sit beside
#   the new one.  ** The two structural repairs cannot satisfy it and should not: their assertion
#   NAMES the module, so the retired token survives as an AST comparison target -- which is the
#   repair, not its residue. **
#   ⇒ *** So the parse runs over the twelve widened receipts, and the two structural ones are held
#     to the stronger statement instead: the token may appear, but NOT as the left operand of an
#     `in` test, which is the form that made it a proxy for the claim. ***
_STRUCTURAL = sorted(r for r in EDITABLE
                     if not any(c[0] == r and 'r7336+60' in c[6] for c in ledger()))
_WIDENED = [r for r in EDITABLE if r not in _STRUCTURAL]
_retired = {c[1][1:-1] for c in _was}
_survivors = {}
for _rel in _WIDENED:
    _src = io.open(os.path.join(ROOT, _rel), encoding='utf-8').read()
    _consts = {n.value for n in ast.walk(ast.parse(_src))
               if isinstance(n, ast.Constant) and isinstance(n.value, str)}
    _hit = sorted(c for c in _consts if any(c == r.replace('\\\\', '\\') for r in _retired))
    if _hit:
        _survivors[_rel] = _hit
print(f'      retired literals read off the ledger at {CENSUS}: {len(_retired)};  '
      f'still present as a constant: {_survivors}')
gate(f'Ⓓ②  and ⛔ **NO RETIRED LITERAL SURVIVES AS A CONSTANT, as the specific negative it is**: all '
     f'`{len(_retired)}` are read off the ledger at the census commit and PARSED out of each '
     f'receipt\'s own syntax tree, not grepped, and `{len(_survivors)}` remain.  ** A repair that '
     f'leaves the old arm in place beside the new one has widened nothing **',
     not _survivors and len(_retired) == K.RESULT['TAIL_ROWS']
     and len(_WIDENED) == K.A_SPACE - K.RESULT['B_STRUCTURAL'])

_in_tests = {}
for _rel in _STRUCTURAL:
    _tree = ast.parse(io.open(os.path.join(ROOT, _rel), encoding='utf-8').read())
    _hit = sorted({_n.left.value for _n in ast.walk(_tree)
                   if isinstance(_n, ast.Compare) and len(_n.ops) == 1
                   and isinstance(_n.ops[0], ast.In)
                   and isinstance(_n.left, ast.Constant) and isinstance(_n.left.value, str)
                   and any(_n.left.value == r.replace('\\\\', '\\') for r in _retired)})
    if _hit:
        _in_tests[_rel] = _hit
print(f'      and the {len(_STRUCTURAL)} structural repairs: retired token as the left operand of '
      f'an `in` test: {_in_tests}')
gate(f'Ⓓ③  ⛔ **AND THE TWO STRUCTURAL REPAIRS ARE HELD TO THE STRONGER STATEMENT, as the specific '
     f'negative it is**: their retired token may still appear -- their assertion NAMES the module it '
     f'loads -- but in `{len(_in_tests)}` of them does it appear as the LEFT OPERAND OF AN `in` '
     f'TEST, which is the form that made it a proxy for the claim.  ** The token moved from being '
     f'searched for in a file to being the thing an import is compared against **',
     not _in_tests and len(_STRUCTURAL) == K.RESULT['B_STRUCTURAL'])

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('E -- THE TWO ARMS SCORED, AND THE SECOND ONE FAILS IN THE DIRECTION IT WAS REGISTERED TO')

gate(f'Ⓔ①  ARM ⒜ LANDS INSIDE ITS BAND: `{_arms["a"][0]}` of the `{K.A_SPACE}` editable tail '
     f'receipts closed, band `{K.A_BAND[0]}`-`{K.A_BAND[1]}`, registered central `{K.A_CENTRAL}`.  '
     f'⚠ ** AND IT IS CENSORED AT ITS OWN CEILING, WHICH THE REGISTRATION SAID BEFORE THE DRAW: a '
     f'population of `{K.A_SPACE}` cannot report a rate above `{K.A_SPACE}`, so this supports '
     f'`>= {K.A_SPACE}` and not an equality, and the band could only ever have failed downward **',
     _arms['a'][2] and _arms['a'][0] == K.A_SPACE == K.RESULT['A_CLOSED'])

print(f'      arm ⒝: {K.RESULT["B_OTHER"]} of {K.B_SPACE} = '
      f'{K.RESULT["B_NORMALISED"]} normalised + {K.RESULT["B_STRUCTURAL"]} structural, against '
      f'{K.RESULT["B_PLAIN"]} plain widenings;  band {K.B_BAND}')
gate(f'Ⓔ②  ⛔⛭⛭ ARM ⒝ FAILS, AND THE FAILURE IS THE RESULT: `{K.RESULT["B_OTHER"]}` of the '
     f'`{K.B_SPACE}` rows needed something other than a plain widening, against a band of '
     f'`{K.B_BAND[0]}`-`{K.B_BAND[1]}` and a central of `{K.B_CENTRAL}` -- `{K.RESULT["B_NORMALISED"]}` '
     f'needing the markup normaliser and `{K.RESULT["B_STRUCTURAL"]}` having no span to widen at '
     f'all.  ** This is one of the two failures the registration named in advance: the tail is '
     f'where the form\'s exceptions live, so the cheap end is cheap in ROWS and expensive in '
     f'RULINGS **',
     not _arms['b'][2] and _arms['b'][0] > K.B_BAND[1]
     and K.RESULT['B_NORMALISED'] + K.RESULT['B_STRUCTURAL'] == K.RESULT['B_OTHER']
     and K.RESULT['B_OTHER'] + K.RESULT['B_PLAIN'] == K.B_SPACE)

_tail_rows = [c for c in ledger(CENSUS) if c[5] == 'REPAIR-OWED' and c[0] in TAIL]
_mk = [c for c in _tail_rows if '$' in c[1] or '\\' in c[1]]
_tok = [c for c in _tail_rows if c[3] == 'TOKEN']
print(f'      the tail\'s composition at {CENSUS}: {len(_mk)}/{len(_tail_rows)} literals carry math '
      f'or markup, {len(_tok)}/{len(_tail_rows)} are TOKEN-tier -- against '
      f'{K.RESULT["BLOCK_MARKUP"]}/{K.RESULT["BLOCK_ROWS"]} and '
      f'{K.RESULT["BLOCK_TOKEN"]}/{K.RESULT["BLOCK_ROWS"]} in the dense blocks')
gate(f'Ⓔ③  ⛭⛭ AND WHY IT FAILED IS MEASURED RATHER THAN OFFERED: the tail\'s rows are composed '
     f'differently from the blocks the band was priced on -- `{len(_mk)}` of `{len(_tail_rows)}` '
     f'literals carry math or markup against `{K.RESULT["BLOCK_MARKUP"]}` of '
     f'`{K.RESULT["BLOCK_ROWS"]}`, and `{len(_tok)}` of `{len(_tail_rows)}` are TOKEN-tier against '
     f'`{K.RESULT["BLOCK_TOKEN"]}` of `{K.RESULT["BLOCK_ROWS"]}`.  ⇒ ** A token has no clause to '
     f'widen inside the gate\'s own reader and a markup carrier needs a normalised one, so the band '
     f'was priced on a population the tail is not drawn from **',
     len(_mk) == K.RESULT['TAIL_MARKUP'] and len(_tok) == K.RESULT['TAIL_TOKEN']
     and len(_mk) / len(_tail_rows) > K.RESULT['BLOCK_MARKUP'] / K.RESULT['BLOCK_ROWS']
     and len(_tok) / len(_tail_rows) > K.RESULT['BLOCK_TOKEN'] / K.RESULT['BLOCK_ROWS'])

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('F -- THE RATE IN BOTH READINGS, AND THE DIRECTION THE TRIGGER READS')

_stride = K.mine(CENSUS)
_tail_assigned = all(r in _stride for r in TAIL)
_left_recs = len(_stride) - K.RESULT['A_CLOSED']
_left_rows = sum(_stride.values()) - K.RESULT['TAIL_ROWS'] + K.RESULT['ROUTED']
print(f'      effort {K.RESULT["A_CLOSED"]} receipts a revision;  realised '
      f'{K.RESULT["A_CLOSED"]} as well, nothing duplicated;  rows a receipt here 1.00 against '
      f'{_left_rows / _left_recs:.2f} for the {_left_recs} that remain')
gate(f'Ⓕ①  ⛭⛭ THE RATE IS REPORTED IN BOTH READINGS, which is standing from `r7335` ③: EFFORT '
     f'`{K.RESULT["A_CLOSED"]}` receipts in one revision and REALISED `{K.RESULT["A_CLOSED"]}` as '
     f'well -- **the two coincide because nothing in this tail was repaired twice**, and that is '
     f'asserted from the stride file at the census commit, where every tail receipt is this seat\'s '
     f'own assignment.  ** The duplication that split the two readings last revision was a property '
     f'of the ASSIGNMENT, and the assignment defect is closed **',
     _tail_assigned and K.RESULT['A_CLOSED'] == _arms['a'][0])

gate(f'Ⓕ②  ⛭⛭⛭ AND THE DIRECTION THE RE-STATED TRIGGER READS IS RISING, NOT FALLING: `9` receipts a '
     f'seat-revision on the dense blocks, `{K.RESULT["A_CLOSED"]}` on the tail, over the two '
     f'revisions the trigger was re-stated to read.  ⚠ ** And the two are not the same quantity: '
     f'`1.00` rows a receipt here against `4.33` there, and the forward figure for the remaining '
     f'`{_left_recs}` receipts is `{_left_rows / _left_recs:.2f}` rows a receipt -- neither end.  So '
     f'the RISE is real and the two points are not interchangeable **',
     K.RESULT['A_CLOSED'] > 9 and _left_recs > 0
     and 1.00 < _left_rows / _left_recs < 4.33)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('G -- THE RESTRAINT, PINNED AT BOTH ENDS, AND THE CASE AND THE EXPERIMENT ON THE RECORD')

_REGISTER = os.path.join('receipts', 'INDEX.md')
# ⌗ *AND THE RANGE IS THIS REVISION'S OWN COMMITS, not a tree-to-tree diff between its ends: this
#   branch MERGED the trunk between them, so a diff of the two trees would carry every other seat's
#   work since the registration -- the `HEAD`-ended range's defect in a second costume.*  ** Both
#   ends are still pinned; what is enumerated is the commits, and merges are excluded because a
#   merge touches what it merges and not what this revision did. **
_own = [c for c in git('rev-list', '--no-merges', f'{REG}~1..{WORK}').split('\n') if c]
_range_all = sorted({f for c in _own
                     for f in git('show', '--no-merges', '--name-only', '--format=', c).split('\n')
                     if f.startswith('receipts/')})
_range = [f for f in _range_all if f.endswith('.py')]
_nonrec = [f for f in _range_all if not f.endswith('.py')]
_extra = [f for f in _range if f not in EDITABLE]
print(f'      receipt files in {REG}~1..{WORK}: {len(_range)};  beyond the tail: '
      f'{[f.split("/")[-1][:12] for f in _extra]};  non-receipt paths: {_nonrec}')
gate(f'Ⓖ①  ⛔ **ONLY THE TAIL AND THE RESTRAINT RECEIPT THAT READS IT ARE TOUCHED, as the specific '
     f'negative it is**: the `{len(_range)}` receipt files in this revision\'s own range -- closed '
     f'at BOTH ends between two of its own commits, which is the rule this seat\'s last receipt '
     f'produced by going red on the trunk -- are the `{len(EDITABLE)}` tail receipts plus '
     f'`{len(_extra)}` more: the restraint receipt whose authorised-crossing list this revision '
     f'extends by name.  ** The barred row\'s receipt is NOT among them **',
     len(_range) == len(EDITABLE) + 1 and len(_extra) == 1
     and BARRED not in _range and not _nonrec)

_cases = [c for c in _minted if 'RULE CASE' in c[6]]
print(f'      rows carrying a rule case: {len(_cases)} '
      f'({[c[0].split("/")[-1][:4] for c in _cases]});  distinct cases: {K.RESULT["CASES"]}')
gate(f'Ⓖ②  and BOTH RULE CASES ARE ON THE RECORD BESIDE THEIR REPAIRS, on `{len(_cases)}` rows and '
     f'not reclassified: ⓵ a MARKDOWN carrier -- blockquote plus asterisk emphasis -- cannot be '
     f'held by the mechanism that holds a paper span, because the gate layer\'s normaliser reads the '
     f'LaTeX emphasis family, math delimiters and `~` and nothing else; ⓶ and that normaliser '
     f'cannot be reached from INSIDE a receipt\'s own reader without making the pin invisible to the '
     f'ledger instrument, which keys a literal only as a direct operand of an `in` test.  ** The '
     f'second case was found BY the instrument on this revision\'s own repair: two minted rows came '
     f'back STALE on the first run, which is the ledger catching a pin nobody would be tracking **',
     len(_cases) == K.RESULT['CASE_ROWS'] and K.RESULT['CASES'] == 2)

sys.path.insert(0, os.path.join(_C, 'r7336_60_the_span_experiment'))
import design as D                                                     # noqa: E402
_sides = D.sides()
_counted = True
try:
    D.outcome()
    _counted = False
except NotImplementedError:
    pass
print(f'      the ordered experiment: registered, arm ⒜ inventories {len(_sides["70"])} and '
      f'{len(_sides["60"])} spans, window N={D.N_REVISIONS};  outcome() raises: {_counted}')
gate(f'Ⓖ③  ⛭⛭ AND `r7335` ②\'s EXPERIMENT IS REGISTERED IN THIS PUSH AND COUNTS NOTHING: both arms '
     f'have a band, a decisive fraction and a window fixed, the symmetric negative is written down '
     f'beside the prediction, and the outcome function RAISES.  ** A design that can report a number '
     f'before its own counting commit is a design that could have chosen the number **',
     _counted and _sides['70'] and _sides['60'] and D.B_BAND[0] > D.B_NULL
     and D.decisive_share(D.B_MIN_READABLE, D.B_CENTRAL, D.B_BAND) >= 0.10)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print()
print("=" * 100)
print(f'  gates run: {len(CHECKS)}   failed: {len(FAILURES)}')
print("=" * 100)
print()
print(f'  ⛭⛭ ** THE CHEAP END CLOSES WHOLE: {K.RESULT["A_CLOSED"]} OF {K.A_SPACE} EDITABLE TAIL '
      f'RECEIPTS, **')
print('     one owed row each, across nine prefixes this seat has no history in -- and the')
print('     fifteenth is on the do-not-edit list and is routed, not edited.')
print(f'  ⛔⛭⛭ ** AND THE SECOND ARM FAILS HIGH: {K.RESULT["B_OTHER"]} OF {K.B_SPACE} ROWS NEEDED '
      f'AN INSTRUMENT OR A')
print(f'     NORMALISED READER, against a band of {K.B_BAND[0]}-{K.B_BAND[1]}. ** Measured reason:')
print(f'     {K.RESULT["TAIL_MARKUP"]} of {K.RESULT["TAIL_ROWS"]} tail literals carry math or markup '
      f'against {K.RESULT["BLOCK_MARKUP"]} of {K.RESULT["BLOCK_ROWS"]} in the')
print('     dense blocks, and the TOKEN share is 2.6 times higher.  The cheap end is cheap in')
print('     ROWS and expensive in RULINGS.')
print(f'  ⛭⛭ ** THE RATE, BOTH READINGS: EFFORT {K.RESULT["A_CLOSED"]} AND REALISED '
      f'{K.RESULT["A_CLOSED"]} -- nothing duplicated. **')
print('     ⇒ The direction the trigger reads: 9 then, 14 now, RISING over its two revisions.')
print('  ⛔ One rule case filed beside its repair, and the ordered experiment registered with')
print('     its outcome function raising.')
if FAILURES:
    print('\n  FAILED:')
    for f in FAILURES:
        print(f'   - {f}')
sys.exit(1 if FAILURES else 0)
