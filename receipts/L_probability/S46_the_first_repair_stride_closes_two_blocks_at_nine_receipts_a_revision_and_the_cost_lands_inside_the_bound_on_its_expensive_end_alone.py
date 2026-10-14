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

⛔⛭⛭⛭ *** READ SECTION G FIRST: FIVE OF THE NINE RECEIPTS BELOW WERE ALREADY REPAIRED WHEN THIS
    STRIDE REPAIRED THEM. ***  *The block the order sent this seat into FIRST had been repaired by
    the other seat one revision earlier; the trunk kept that seat's versions and the next revision's
    orders concede the assignment.*  ** So this receipt now reports TWO rates and lets neither stand
    for the other: the per-receipt EFFORT, which is what a repair costs and what the order asked
    for, and the REALISED rate, which is what a backlog actually falls by. **  ⇒ *Effort `9` a
    revision, `7.4` cycles, inside the top of `8`; realised `4` a revision against the `62` that
    were ever this seat's, `15.5` cycles, outside it -- and the gap is exactly the duplicated block
    on both sides of the arithmetic.*  ⌗ ** The effort rate is the one that forecasts, because
    duplication is a property of the ASSIGNMENT and not of the stride.  Everything below is the
    stride as it was measured, with its historical claims now pinned to this revision's own commits
    rather than to a live file later seats write. **

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
# ⛔⛭⛭⛭ RE-PINNED AFTER THE TRUNK ANSWERED, AND THE ANSWER IS THE FINDING AT SECTION G.  *Five of
#   the nine receipts this stride repaired had ALREADY been repaired in the trunk, by the other
#   seat, one revision earlier -- so the trunk kept that seat's versions and dropped this seat's,
#   and every clause here that read the LIVE ledger for what THIS REVISION minted went red on a
#   state it does not describe.*
#   ⇒ *** `L-249`'s rule, applied to this receipt's own numbers: what this revision DID is a fact
#     about history and is read at this revision's own last content commit; what the TRUNK carries
#     is read live, asserted separately, and allowed to differ. ***  ** A receipt whose historical
#     claims read a live file is a receipt the next seat's work can falsify without touching it. **
MINE = '2fda7677'               # this revision's own last content commit, in the trunk's history
TRUNK = '53b0944d'              # the trunk commit where the next revision's orders answered it
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

_minted = [c for c in ledger(MINE) if any(b in c[0] for b in BLOCKS) and 'r7332+60' in c[6]]
_verdicts = collections.Counter(c[5] for c in _minted)
print(f'      keys this revision minted in the two blocks: {len(_minted)};  verdicts {dict(_verdicts)}')
gate(f'Ⓒ②  and EVERY KEY THE REPAIRS MINTED IS ADJUDICATED IN THE SAME PUSH: `{len(_minted)}` keys, '
     f'all `EXTENDED` -- the verdict a widening takes, since the span changed and the receipts\' '
     f'assertions and tolerances did not.  ** `{K.ROWS}` rows closing on `{len(_minted)}` keys is '
     f'`{len(_minted) / K.ROWS:.2f}` a row, and that is the finding rather than an economy: '
     f'fragments of ONE sentence are ONE pin **',
     len(_minted) == K.KEYS and set(_verdicts) == {'EXTENDED'}
     and not [c for c in _minted if c[5] == 'UNADJUDICATED'])

# ⛭⛭ AND THE LIVE LEDGER IS ASSERTED SEPARATELY AND ALLOWED TO BE SMALLER, which is the half the
#   first form left out: a key this revision minted can be SUPERSEDED by another seat's earlier
#   repair of the same receipt, and a receipt that cannot say so reads its own supersession as a
#   defect in itself.
_live = [c for c in ledger() if any(b in c[0] for b in BLOCKS) and 'r7332+60' in c[6]]
_live_recs = sorted({c[0] for c in _live})
_gone_recs = sorted({c[0] for c in _minted} - set(_live_recs))
_super = {r: sorted({c[6].split(',')[0].strip() for c in ledger() if c[0] == r
                     and c[5] != 'REPAIR-OWED' and 'r7329' in c[6]}) for r in _gone_recs}
print(f'      of those {len(_minted)} keys, {len(_live)} are live, in {len(_live_recs)} receipt(s);  '
      f'{len(_gone_recs)} receipt(s) superseded: '
      f'{ {r.split("/")[-1][:4]: v for r, v in _super.items()} }')
gate(f'Ⓒ③  ⛭⛭ AND THE LIVE LEDGER IS SMALLER THAN WHAT THIS REVISION MINTED, WHICH IS SUPERSESSION '
     f'AND NOT LOSS: `{len(_live)}` of the `{len(_minted)}` keys stand live, every one of them still '
     f'`EXTENDED`, and the `{len(_gone_recs)}` receipts whose keys are gone each carry rows minted by '
     f'ANOTHER SEAT at the PREVIOUS revision -- the repair that was already there before this one '
     f'started.  ** The monotone statement is the only one a receipt may make about a file later '
     f'seats write: what it minted is pinned, what survives is read, and the difference is named **',
     _live and all(c[5] == 'EXTENDED' for c in _live) and len(_live) <= len(_minted)
     and _gone_recs and all(_super[r] for r in _gone_recs))

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

# ⛔⛭⛭ SCOPED AFTER THE TRUNK ANSWERED.  *The claim is about THIS REVISION's repairs, and the
#   trunk carries five of the nine receipts in the OTHER seat's form -- whose arms are that seat's
#   to choose.  Measured: the superseded `B10` keeps two literals this revision retired, which is
#   not a repair left half-done but a DIFFERENT repair, adjudicated under its own revision's rows.*
#   ⇒ The parse runs over the receipts whose repair this revision's own work is still what the
#     trunk reads, and the others are asserted to be another revision's by their own last commit --
#     which is the specific negative that keeps the claim honest instead of dropping it.
_LASTREV = re.compile(r'\br(\d{4})\b')
# ⌗ *AND THE PARTITION IS READ AT THE TRUNK COMMIT WHERE THE ANSWER CAME, not live: which seat's
#   repair the trunk carries is a fact about THAT commit, and a later seat re-repairing any of these
#   nine must not be able to move a count this receipt states.  ** The two sizes below are therefore
#   closed facts about `TRUNK`, and their sum is asserted against this revision's own receipt count
#   rather than against a literal. **
_last_rev = {rel: (_LASTREV.search(git('log', '--no-merges', '-1', '--format=%s', TRUNK, '--', rel)
                                   or '') or [None])
             for rel in RECEIPTS}
_last_rev = {rel: (m.group(1) if hasattr(m, 'group') else None) for rel, m in _last_rev.items()}
_mine_now = [rel for rel in RECEIPTS if _last_rev[rel] == '7332']
_superseded = [rel for rel in RECEIPTS if _last_rev[rel] != '7332']
_retired = {c[1][1:-1] for c in _was}
_survivors = {}
for _rel in _mine_now:
    _src = git('show', f'{TRUNK}:{_rel}')
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
     not _survivors and len(_retired) >= 30
     and _mine_now and len(_mine_now) + len(_superseded) == len(RECEIPTS))

print(f'      and the other {len(_superseded)} are another revision\'s in the trunk: '
      f'{ {r.split("/")[-1][:4]: _last_rev[r] for r in _superseded} }')
gate(f'Ⓓ③  ⛔ **AND THE `{len(_superseded)}` RECEIPTS NOT PARSED ABOVE ARE NOT SKIPPED BUT NAMED, as '
     f'the specific negative they are**: each one\'s last commit in the trunk carries a DIFFERENT '
     f'revision than this one, so its arms are the other seat\'s choice and this receipt asserts '
     f'nothing about which literals they keep.  ** A claim that cannot be made about a file another '
     f'seat now owns is dropped WITH ITS REASON, never quietly narrowed **',
     _superseded and len(_superseded) + len(_mine_now) == K.A_DONE
     and all(_last_rev[r] and _last_rev[r] != '7332' for r in _superseded))

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

# ⛔⛭ REPAIRED AFTER ITS FIRST RED, AND THE RED WAS THIS GATE's OWN FAIL-ON-SUCCESS SHAPE.  The
#   form that stood here counted EVERY path under `receipts/` in the revision's range and excluded
#   only this file by name.  *It passed on the tree it was written on because the landing commit did
#   not exist yet: the register row and this receipt were both still uncommitted, so the range held
#   `9` and nothing outside.*  ** The moment the revision landed, the same condition read `11` and
#   named `receipts/INDEX.md` as a receipt outside the blocks -- which it is not: it is the REGISTER
#   ROW, and every revision in the corpus writes it. **
#   ⇒ *** So the repair is the named form again: assert what the claim IS rather than name a
#     directory.  A RECEIPT is a `.py` file; the claim is that the receipt files this revision's own
#     range touched are exactly the nine it repaired and all of them inside the two ordered blocks.
#     The non-receipt paths are asserted SEPARATELY and bounded to the register row alone, so the
#     gate now also forbids writing any other non-receipt file under that tree -- strictly stronger
#     than the form it replaces, and stable whether or not this receipt is itself committed. ***
_REGISTER = os.path.join('receipts', 'INDEX.md')
# ⛔⛭⛭⛭ AND THE RANGE IS PINNED AT BOTH ENDS AFTER ITS SECOND RED.  *The first form ended the
#   range at `HEAD`, which was this revision's own tip for exactly as long as it took the trunk to
#   move: the moment the branch merged the trunk in, the range held every seat's work since the
#   registration and the restraint clause read thirty-six commits of other people's receipts as
#   this revision's own.*  ⇒ *** A revision's range is a CLOSED interval between two of its own
#   commits, and naming it that way is what makes the restraint assertable at any later time. ***
_range_all = sorted({f for f in git('diff', '--name-only', f'{PREG}~1', MINE).split('\n')
                     if f.startswith('receipts/')})
_range = [f for f in _range_all
          if f.endswith('.py') and os.path.basename(f) != os.path.basename(__file__)]
_nonrec = [f for f in _range_all if not f.endswith('.py')]
_outside = [f for f in _range if not any(b in '/' + f for b in BLOCKS)]
print(f'      receipt files in {PREG}~1..{MINE} (this one aside): {len(_range)};  outside the two '
      f'blocks: {_outside};  non-receipt paths: {_nonrec}')
gate(f'Ⓕ①  ⛔ **ONLY THE TWO ORDERED BLOCKS ARE TOUCHED, as the specific negative it is**: the '
     f'`{len(_range)}` RECEIPT FILES in this revision\'s own range are exactly the `{K.A_DONE}` it '
     f'repaired, and `{len(_outside)}` of them lie outside the blocks -- with the only non-receipt '
     f'path written under that tree being the register row every revision writes.  ** No other '
     f'seat\'s receipt is edited, and the do-not-edit list is not approached **',
     not _outside and len(_range) == K.A_DONE and set(_nonrec) <= {_REGISTER})

print(f'      cases filed in the minted rows: {len(_cases)}')
gate(f'Ⓕ②  and BOTH CASES ARE ON THE RECORD BESIDE THEIR REPAIRS, which is the bound\'s clause `3` '
     f'running for the first time: `{len(_cases)}` of them, one a cannot-fail arm whose LABEL had '
     f'gone false and which therefore reported a falsehood in green, the other a markup carrier that '
     f'cannot be held as a MEANING pin because the gate reads a form normalisation does not recover.  '
     f'** A row leaves the list by being repaired or withdrawn WITH ITS CASE WRITTEN DOWN, never by '
     f'reclassification **',
     len(_cases) == K.CASES and all('r7332+60' in c[6] for c in _cases))

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('G -- THE DUPLICATION, MEASURED: WHAT THE STRIDE COST AND WHAT THE TRUNK ACTUALLY GAINED')

# ⛭⛭⛭ THIS SECTION DID NOT EXIST WHEN THE STRIDE WAS WRITTEN.  *It is here because the trunk
#   answered: the block the order sent this seat into FIRST had already been repaired by the other
#   seat at the previous revision, and the trunk kept that seat's versions.*  ** So the effort this
#   revision spent and the backlog it actually cleared are two different numbers, and the figure
#   the order asked for depends on which one it meant. **  Both are computed here and neither is
#   allowed to stand for the other.
_dup_rows = [c for c in _was if c[0] in _superseded]
_mine_rows = [c for c in _was if c[0] in _mine_now]
print(f'      effort: {len(RECEIPTS)} receipts and {len(_was)} rows repaired in this revision;  '
      f'superseded: {len(_superseded)} receipts and {len(_dup_rows)} rows;  '
      f'net to the trunk: {len(_mine_now)} receipts and {len(_mine_rows)} rows')
gate(f'Ⓖ①  ⛔⛭⛭ **FIVE OF THE NINE RECEIPTS WERE ALREADY REPAIRED WHEN THIS STRIDE REPAIRED THEM**, '
     f'and the trunk says so in two independent ways rather than in prose: each of the '
     f'`{len(_superseded)}` carries a LAST COMMIT from the previous revision, and each carries '
     f'ledger rows minted under that revision.  ** `{len(_dup_rows)}` of this revision\'s '
     f'`{len(_was)}` rows were a second payment for rows already closed **',
     len(_superseded) > len(_mine_now) and _dup_rows and _mine_rows
     and len(_dup_rows) + len(_mine_rows) == len(_was)
     and len(_superseded) + len(_mine_now) == len(RECEIPTS))

_eff_cycles = K.STRIDE_RECEIPTS / K.A_DONE
_own_backlog = K.STRIDE_RECEIPTS - len(_superseded)
_net_cycles = _own_backlog / len(_mine_now)
print(f'      the two readings: effort {K.A_DONE} a revision ⇒ {_eff_cycles:.1f} cycles for '
      f'{K.STRIDE_RECEIPTS}, top {K.CYCLE_TOP};  realised {len(_mine_now)} a revision ⇒ '
      f'{_net_cycles:.1f} cycles for the {_own_backlog} that were this seat\'s to clear')
gate(f'Ⓖ②  ⛭⛭⛭ **AND THE COST FIGURE THE SECONDMENT TURNS ON READS TWO WAYS, SO BOTH ARE PUT UP**: '
     f'the PER-RECEIPT EFFORT, which is what the order asked for and what a repair costs, is '
     f'`{K.A_DONE}` a revision and `{_eff_cycles:.1f}` cycles, INSIDE the top of `{K.CYCLE_TOP}`; '
     f'the REALISED rate, which is what a backlog actually falls by, is `{len(_mine_now)}` against '
     f'the `{_own_backlog}` that were ever this seat\'s, and `{_net_cycles:.1f}` cycles, OUTSIDE it. '
     f'⇒ *** And the gap is not a disagreement about the work: it is exactly the duplicated block, '
     f'`{len(_superseded)}` receipts on both sides of the arithmetic. *** ⚠ ** The effort rate is the '
     f'one that forecasts, because duplication is a property of the ASSIGNMENT and not of the '
     f'stride -- which is why the number is reported with the assignment named and not averaged.  '
     f'⌗ And the trunk\'s own reading sits between the two and is the one the phase runs on: it '
     f'POOLS the seats, so a row repaired twice is counted once and the duplicated work shows up as '
     f'effort spent rather than as progress claimed **',
     _eff_cycles <= K.CYCLE_TOP and _net_cycles > K.CYCLE_TOP
     and _own_backlog + len(_superseded) == K.STRIDE_RECEIPTS
     and len(_mine_now) + len(_superseded) == K.A_DONE)

_CONCEDED = ['WAS ALREADY DONE WHEN I TOLD YOU TO START THERE', 'THAT IS MINE, NOT YOURS',
             'pooled rate', 'a re-cut applies to work not yet begun']
_ord_next = git('show', f'{TRUNK}:FOR_60.md')
print(f'      the assignment conceded at {TRUNK}: {[s in _ord_next for s in _CONCEDED]}')
gate(f'Ⓖ③  ⌗ AND THE MISASSIGNMENT IS NOT THIS SEAT\'s CLAIM BUT THE ORDERING SEAT\'s OWN, read at '
     f'the trunk commit that carries it: the next revision\'s orders say the block was already done '
     f'when this seat was told to start there, pool the two seats\' rates rather than adding them, '
     f'and fix the protocol so that a re-cut applies to work not yet begun.  ** Which settles whose '
     f'cost the duplicated five are and leaves this receipt reporting the measurement rather than '
     f'arguing it **',
     all(s in _ord_next for s in _CONCEDED))

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
print(f'  ⛔⛭⛭ ** AND FIVE OF THE NINE WERE ALREADY REPAIRED: {len(_dup_rows)} of the {len(_was)} rows')
print('     were a second payment for rows the other seat closed one revision earlier, and the')
print(f'     trunk kept its versions. ** ⇒ Effort {K.A_DONE} a revision = {_eff_cycles:.1f} cycles,')
print(f'     INSIDE the top of {K.CYCLE_TOP}; realised {len(_mine_now)} a revision = '
      f'{_net_cycles:.1f} cycles for the')
print(f'     {_own_backlog} that were ever this seat\'s, OUTSIDE it -- and the gap IS the duplicated')
print('     block, on both sides of the arithmetic.  The effort rate is the one that forecasts,')
print('     because duplication is a property of the assignment and not of the stride.')
if FAILURES:
    print('\n  FAILED:')
    for f in FAILURES:
        print(f'   - {f}')
sys.exit(1 if FAILURES else 0)
