#!/usr/bin/env python3
r"""S46 -- THE FIRST REPAIR STRIDE, AND WHAT A REPAIR COSTS MEASURED RATHER THAN PREDICTED.

** WHAT WAS ORDERED. **  `r7331` ④: `L147_two_arm` first, because its rows are the ones `cc66`'s
disjunction-cannot-carry-a-conjunction clause decided and the seat that wrote the clause is not the
seat to test it; then `L165_defining_the_sum`, the densest block anyone holds; and ⑤ report the
per-receipt cost with a band and its decisive fraction registered BEFORE the stride starts, because
that figure replaces the bound's prediction and decides whether `70` stays seconded.

*** ⓐ BOTH BLOCKS ARE CLEAR: `39` OWED ROWS IN `9` RECEIPTS, CLOSING ON `24` MINTED KEYS. ***
  => ** `0.62` keys a row, and the reason is the finding: FRAGMENTS OF ONE SENTENCE ARE ONE PIN. **
     *Eleven of the nineteen dense-block rows were pieces of five sentences, paired two and three to
     a check so that their CONJUNCTION IN A FILE stood for what one sentence says.  Two of those
     pieces stand more than once in their own paper -- one twice, one four times -- so those pairs
     could not even locate the claim they were about.*

*** ⓑ BOTH REGISTERED ARMS LAND INSIDE THEIR BANDS, AND BOTH BANDS WERE FAILABLE. ***
  ⓘ arm ⒜, the figure the order asks for: `9` receipts of the `9`, band `5`-`9`, decisive `0.145`.
  ⓙ arm ⒝, which decides whether the amendment holds: `12` of `13` rows repaired by the named form
     with no case owed, band `9`-`13`, decisive `0.160`.
  => ** And on the rows `cc66`'s clause ACTUALLY DECIDED it is `12` of `12`: the one case filed in
     that block is a PROXY row, not a disjunction row, so the clause stands unamended. **

*** ⓒ THE COST: `9` RECEIPTS IN ONE REVISION, AGAINST `66`'s PREDICTED `11`-`16` A CYCLE.  THIS
    SEAT'S `67` RECEIPTS AT THAT RATE ARE `7.4` CYCLES, INSIDE THE BAND'S TOP OF `8` BY `0.6`. ***
  ⚠ ** AND THE RATE IS MEASURED ON THE EXPENSIVE END ALONE, which the order chose on purpose: **
    *the two blocks run `4.33` rows a receipt where the remaining `58` average `2.67`, and the
    single-row tail the order asked to be priced SECOND is not reached in this revision.*
  => *** So `9` a revision is a LOWER bound on the rate and `7.4` cycles an UPPER bound on the cost:
      the figure moves DOWN when the cheap end is measured, never up. ***

*** ⓓ AND TWO CASES ARE FILED BESIDE THE REPAIRS, which is the refinement path running. ***
  ⓚ ** A cannot-fail arm whose LABEL HAS GONE FALSE reports a falsehood in green. **  *The label said
     a register row does not carry a result and that a phrase appears there only as a question.  Both
     halves had gone untrue -- the row answers in its own voice about a different operator, and a
     later revision wrote the quoted sentence INTO the row and credited it -- and the arm passed
     THROUGHOUT, because it passes BY the row now carrying what the label denies.*  => The
     fail-on-success family in the mirror: nothing goes red and the sentence quietly stops being true.
  ⓛ ** And a markup carrier cannot be held as a MEANING pin. **  *`r7258` settled that such a span is
     repaired by NORMALISING the reader; the `MEANING-HELD` gate's own validator reads a form that
     normalisation does not recover, so the two settled rules meet.  Filed, not papered over.*

⛔ ** NOTHING OUTSIDE THE TWO BLOCKS IS TOUCHED **, and no retired literal survives as a constant in
any of the nine receipts -- both asserted rather than promised.

⚠ WHAT THIS CANNOT FIX is at the foot, beginning with the fact that one revision is one draw and the
binomial the bands were priced on assumes the per-receipt cost is constant, which is the very thing
the measurement exists to test.
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
sys.path.insert(0, os.path.join(_C, 'r7332_60_the_first_stride'))
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
ORDER = '46fed61a'              # r7331's orders on the trunk
PREG = 'ad66413b'               # the commit that PUSHED the registration, before any repair
BLOCKS = ('/L147_two_arm/', '/L165_defining_the_sum/')
RECEIPTS = sorted(
    [f'receipts/L147_two_arm/{n}' for n in os.listdir(os.path.join(ROOT, 'receipts/L147_two_arm'))
     if re.match(r'B(2|3|8|9|10)_', n)] +
    [f'receipts/L165_defining_the_sum/{n}'
     for n in os.listdir(os.path.join(ROOT, 'receipts/L165_defining_the_sum'))
     if re.match(r'S[1-4]_', n)])


def git(*a):
    return subprocess.run(['git', '-C', ROOT] + list(a),
                          capture_output=True, text=True, errors='replace').stdout


def ledger(sha=''):
    text = (git('show', f'{sha}:corpus/quote_pin_baseline.tsv') if sha
            else io.open(os.path.join(ROOT, 'corpus', 'quote_pin_baseline.tsv'),
                         encoding='utf-8').read())
    return [l.split('\t') for l in text.split('\n') if l.startswith('receipts/')]


# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('A -- THE ORDER, READ WHERE IT WAS WRITTEN')

ORD = git('show', f'{ORDER}:FOR_60.md')
_items = ['the densest block anyone holds', 'for the reason in ③',
          'with a band and its decisive fraction', 'decides whether the secondment holds',
          'the seat that wrote the clause']
print(f'      the order\'s items present at {ORDER}: {[s in ORD for s in _items]}')
gate(f'Ⓐ①  THE ORDER IS READ AT `{ORDER}` AND NOT PARAPHRASED: `r7331` ③ sends the Test-5 block '
     f'first because the seat that wrote the clause is not the seat to test it, ④ sends the densest '
     f'block second, and ⑤ asks for the per-receipt cost with a band and its decisive fraction '
     f'registered first, saying in terms that the figure decides whether `70` stays seconded.  '
     f'** The seat that is ordered does not get to choose which half of the order it answers **',
     all(s in ORD for s in _items))

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('B -- THE REGISTRATION WAS PUSHED BEFORE THE FIRST REPAIR, AND BOTH BANDS WERE FAILABLE')

_at_preg = set(git('ls-tree', '--name-only', '-r', PREG, '--',
                   'computations/beyond_the_wall/r7332_60_the_first_stride').split('\n'))
_touched_at_preg = [f for f in git('diff', '--name-only', f'{PREG}~1', PREG).split('\n')
                    if f.startswith('receipts/')]
print(f'      at {PREG} the directory holds {sorted(f.split("/")[-1] for f in _at_preg if f)};  '
      f'receipts touched by that commit: {len(_touched_at_preg)}')
gate(f'Ⓑ①  THE BANDS WERE REGISTERED BEFORE ONE RECEIPT WAS REPAIRED, as a closed fact about the '
     f'history rather than a promise in prose: `{PREG}` carries the pre-registration and its '
     f'arithmetic and touches `{len(_touched_at_preg)}` receipts.  ** `r7295`\'s ruling: what is open '
     f'is a trunk fact, so the ORDER of the commits is the claim **',
     _at_preg and not _touched_at_preg)

_arms = K.scored()
for _nm in ('a', 'b'):
    _got, _band, _inside, _frac = _arms[_nm]
    print(f'      arm ({_nm}): {_got}, band {_band}, inside={_inside}, decisive={_frac:.3f}')
gate(f'Ⓑ②  AND BOTH BANDS WERE FAILABLE WHEN THEY WERE WRITTEN, which is `r7325`\'s standing rule '
     f'applied before the work rather than after: decisive fractions `{_arms["a"][3]:.3f}` and '
     f'`{_arms["b"][3]:.3f}`, against this seat\'s own `r7320` band at `0.002` and the `16` of `25` '
     f'entries `70` found below `0.10`.  ** A band nobody could have failed is not a band **',
     _arms['a'][3] >= 0.10 and _arms['b'][3] >= 0.10)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('C -- BOTH BLOCKS ARE CLEAR, AND WHAT THEY HELD IS READ AT THE REGISTRATION COMMIT')

_was = [c for c in ledger(PREG) if c[5] == 'REPAIR-OWED' and any(b in c[0] for b in BLOCKS)]
_now = [c for c in ledger() if c[5] == 'REPAIR-OWED' and any(b in c[0] for b in BLOCKS)]
_was_recs = sorted({c[0] for c in _was})
print(f'      owed at {PREG}: {len(_was)} rows in {len(_was_recs)} receipts;  owed now: {len(_now)}')
gate(f'Ⓒ①  ⛭⛭ BOTH BLOCKS CARRY NO OWED ROW, and what they HELD is read at the registration commit '
     f'rather than from the stride\'s summary: `{len(_was)}` rows in `{len(_was_recs)}` receipts '
     f'before, `{len(_now)}` now.  ** Read live, the before-count would have fallen to zero as the '
     f'repairs landed -- the fail-on-success shape this seat\'s own recipe cures by naming a '
     f'commit **',
     len(_was) == K.ROWS and len(_was_recs) == K.A_DONE and not _now)

_minted = [c for c in ledger() if any(b in c[0] for b in BLOCKS) and 'r7332+60' in c[6]]
_verdicts = collections.Counter(c[5] for c in _minted)
print(f'      keys this revision minted in the two blocks: {len(_minted)};  verdicts {dict(_verdicts)}')
gate(f'Ⓒ②  and EVERY KEY THE REPAIRS MINTED IS ADJUDICATED IN THE SAME PUSH: `{len(_minted)}` keys, '
     f'all `EXTENDED` -- the verdict a widening takes, since the span changed and the receipts\' '
     f'assertions and tolerances did not.  ** `{K.ROWS}` rows closing on `{len(_minted)}` keys is '
     f'`{len(_minted) / K.ROWS:.2f}` a row, and that is the finding rather than an economy: '
     f'fragments of ONE sentence are ONE pin **',
     len(_minted) == K.KEYS and set(_verdicts) == {'EXTENDED'}
     and not [c for c in _minted if c[5] == 'UNADJUDICATED'])

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('D -- EVERY REPAIRED RECEIPT RE-RUNS GREEN, AND NO RETIRED LITERAL SURVIVES')

_runs = {}
for _rel in RECEIPTS:
    _r = subprocess.run([sys.executable, '-I', os.path.join(ROOT, _rel)],
                        capture_output=True, text=True, errors='replace', timeout=600)
    _runs[_rel] = (_r.returncode, _r.stdout.count('[FAIL]') + _r.stdout.count('FAILED'))
print(f'      {len(_runs)} receipts run;  non-zero exits: '
      f'{[r.split("/")[-1][:4] for r, (rc, _) in _runs.items() if rc]}')
gate(f'Ⓓ①  ALL `{len(_runs)}` REPAIRED RECEIPTS RE-RUN GREEN on this tree, run here rather than '
     f'asserted: every exit is zero and no run prints a failure.  ** A repair that leaves its own '
     f'receipt red is not a repair **',
     all(rc == 0 and nf == 0 for rc, nf in _runs.values()) and len(_runs) == K.A_DONE)

_retired = {c[1][1:-1] for c in _was}
_survivors = {}
for _rel in RECEIPTS:
    _src = io.open(os.path.join(ROOT, _rel), encoding='utf-8').read()
    _consts = {n.value for n in ast.walk(ast.parse(_src))
               if isinstance(n, ast.Constant) and isinstance(n.value, str)}
    _hit = sorted(c for c in _consts if any(c == r.replace('\\\\', '\\') for r in _retired))
    if _hit:
        _survivors[_rel] = _hit
print(f'      retired literals read off the ledger at {PREG}: {len(_retired)};  '
      f'still present as a constant anywhere: {_survivors}')
gate(f'Ⓓ②  and ⛔ **NO RETIRED LITERAL SURVIVES AS A CONSTANT, as the specific negative it is**: all '
     f'`{len(_retired)}` of them are read off the ledger at the registration commit and PARSED out '
     f'of each receipt\'s own syntax tree, not grepped, and `{len(_survivors)}` remain.  ** A repair '
     f'that leaves the old arm in place beside the new one has widened nothing **',
     not _survivors and len(_retired) >= 30)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('E -- THE TWO ARMS SCORED, AND THE COST WITH THE DIRECTION OF ITS ERROR NAMED')

gate(f'Ⓔ①  ARM ⒜ LANDS INSIDE ITS REGISTERED BAND: `{_arms["a"][0]}` receipts of the `9`, band '
     f'`{K.A_BAND[0]}`-`{K.A_BAND[1]}`, registered central `{K.A_CENTRAL}`.  ** And the arm is the '
     f'figure the order asked for, not a proxy for it: a receipt counted only when every one of its '
     f'owed rows was repaired or withdrawn with its case AND the receipt re-ran green **',
     _arms['a'][2] and _arms['a'][0] == K.A_DONE)

_l147 = [c for c in _was if BLOCKS[0] in c[0]]
_cases = [c for c in _minted if 'WITHDRAWAL WITH ITS CASE' in c[6] or 'THE CASE IS' in c[6]
          or 'case about the INSTRUMENT' in c[6]]
print(f'      L147 rows at {PREG}: {len(_l147)};  clean of a case: {K.B_CLEAN};  cases filed: '
      f'{len(_cases)}')
gate(f'Ⓔ②  ⛭⛭ ARM ⒝ LANDS INSIDE ITS BAND AND THE AMENDMENT HOLDS: `{K.B_CLEAN}` of the '
     f'`{len(_l147)}` rows repaired by the named form with no case owed, band `{K.B_BAND[0]}`-'
     f'`{K.B_BAND[1]}`.  ** And on the rows `cc66`\'s clause ACTUALLY DECIDED it is `12` of `12` -- '
     f'the one case in that block is a PROXY row and not a disjunction row -- so the clause `69` took '
     f'verbatim stands unamended on its first contact with the cases it was written for **',
     _arms['b'][2] and K.B_CLEAN == len(_l147) - 1 and len(_cases) == K.CASES)

_cycles = K.STRIDE_RECEIPTS / K.A_DONE
_rest_rows = 194 - K.ROWS
_rest_recs = K.STRIDE_RECEIPTS - K.A_DONE
print(f'      {K.A_DONE} receipts a revision ⇒ {_cycles:.1f} cycles for {K.STRIDE_RECEIPTS}, '
      f'top {K.CYCLE_TOP};  density here {K.ROWS / K.A_DONE:.2f} rows a receipt against '
      f'{_rest_rows / _rest_recs:.2f} for the rest')
gate(f'Ⓔ③  ⛭⛭ THE COST IS MEASURED AND IT LANDS INSIDE THE BOUND: `{K.A_DONE}` receipts in one '
     f'revision puts this seat\'s `{K.STRIDE_RECEIPTS}` at `{_cycles:.1f}` cycles against a band top '
     f'of `{K.CYCLE_TOP}`, so the secondment is not reversed.  ⚠ ** AND THE DIRECTION OF THE ERROR IS '
     f'NAMED RATHER THAN LEFT TO BE FOUND: the rate is measured on the EXPENSIVE END ALONE, '
     f'`{K.ROWS / K.A_DONE:.2f}` rows a receipt against `{_rest_rows / _rest_recs:.2f}` for the '
     f'remaining `{_rest_recs}`, and the single-row tail the order asked to be priced second is not '
     f'reached here.  So the rate is a LOWER bound and the cycle count an UPPER one **',
     _cycles <= K.CYCLE_TOP and K.ROWS / K.A_DONE > _rest_rows / _rest_recs)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('F -- THE RESTRAINT: TWO BLOCKS, NO OTHER SEAT\'s WORK, AND THE CASES ON THE RECORD')

_range = sorted({f for f in git('diff', '--name-only', f'{PREG}~1', 'HEAD').split('\n')
                 if f.startswith('receipts/')})
_outside = [f for f in _range if not any(b in '/' + f for b in BLOCKS)
            and os.path.basename(f) != os.path.basename(__file__)]
print(f'      receipts in {PREG}~1..HEAD: {len(_range)};  outside the two blocks and not this file: '
      f'{_outside}')
gate(f'Ⓕ①  ⛔ **ONLY THE TWO ORDERED BLOCKS ARE TOUCHED, as the specific negative it is**: '
     f'`{len(_range)}` receipts are in this revision\'s own range -- exactly the `{K.A_DONE}` it '
     f'repaired -- and `{len(_outside)}` of them lie outside the blocks.  ** No other seat\'s receipt is edited, and the do-not-edit list is not '
     f'approached **',
     not _outside and len(_range) == K.A_DONE)

print(f'      cases filed in the minted rows: {len(_cases)}')
gate(f'Ⓕ②  and BOTH CASES ARE ON THE RECORD BESIDE THEIR REPAIRS, which is the bound\'s clause `3` '
     f'running for the first time: `{len(_cases)}` of them, one a cannot-fail arm whose LABEL had '
     f'gone false and which therefore reported a falsehood in green, the other a markup carrier that '
     f'cannot be held as a MEANING pin because the gate reads a form normalisation does not recover.  '
     f'** A row leaves the list by being repaired or withdrawn WITH ITS CASE WRITTEN DOWN, never by '
     f'reclassification **',
     len(_cases) == K.CASES and all('r7332+60' in c[6] for c in _cases))

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print()
print("=" * 100)
print(f'  gates run: {len(CHECKS)}   failed: {len(FAILURES)}')
print("=" * 100)
print()
print(f'  ⛭⛭ ** BOTH BLOCKS CLEAR: {K.ROWS} OWED ROWS IN {K.A_DONE} RECEIPTS ON {K.KEYS} KEYS. **')
print('     0.62 keys a row, because fragments of ONE sentence are ONE pin -- and two of those')
print('     fragments stood more than once in their own paper, so the pairs could not even locate')
print('     the claim they were about.')
print(f'  ✔ ** BOTH REGISTERED ARMS INSIDE THEIR BANDS: {_arms["a"][0]} of 9 receipts, and '
      f'{K.B_CLEAN} of {len(_l147)} rows')
print('     repaired with no case owed -- and 12 of 12 on the rows the clause actually decided, so')
print("     cc66's amendment stands unamended on its first contact with its own cases. **")
print(f'  ⛭⛭ ** THE COST: {K.A_DONE} RECEIPTS A REVISION ⇒ {_cycles:.1f} CYCLES, INSIDE THE TOP OF '
      f'{K.CYCLE_TOP}. **')
print('     ⚠ Measured on the expensive end alone, so it is a lower bound on the rate and an upper')
print('     bound on the cost; the cheap tail is unmeasured and moves it down, never up.')
print('  ⛔ Two cases filed beside their repairs, which is the refinement path running.')
if FAILURES:
    print('\n  FAILED:')
    for f in FAILURES:
        print(f'   - {f}')
sys.exit(1 if FAILURES else 0)
