#!/usr/bin/env python3
"""S50 -- THE ELEVEN: the block closes whole, and all three registered arms FAIL HIGH -- one because
the block was cheaper than its own figure prices it, and the other two ** because they turned out to
be measuring ONE quantity that neither registration saw. **

** WHAT WAS ORDERED. **  `r7353` ①: *your `11` receipts first, then the queue -- and `S7` before
either.*  `S7` and `S10` landed as `r7354`; this is the block.  The registration is
`computations/beyond_the_wall/r7356_60_the_eleven/`, written and committed before the first repair.

** Ⓐ THE BLOCK, AND ONE OF THE ELEVEN IS NOT THIS SEAT'S TO REPAIR. **  `30` owed rows in `11`
receipts over `11` prefixes, `2.73` a receipt.  ⛔ *`L257…/V1` carries `5` of the `30` and is on this
seat's own DO-NOT-EDIT list, so it is ROUTED with its patch and never edited.*  ⇒ The arm's population
is the `10` receipts this seat may edit, `25` rows.

** Ⓑ ARM ⒜ -- `10` OF `10` CLOSED.  ⛔ OUTSIDE THE BAND, HIGH. **  Central `7` of `10`, band
`6`-`9`, decisive `0.179`.  *Every one of the ten is RUN here, not cited.*

** Ⓒ ARM ⒝ -- `17` OF THE `30` OWED ROWS ARE UNIQUENESS PROBLEMS.  ⛔ OUTSIDE THE BAND, HIGH, AND
IT CONTRADICTS THE EXPECTATION THE ORDER CARRIED. **  Central `0.15`, band `0.08`-`0.33`, two-sided,
decisive `0.161`; measured `0.5667`.

  *`r7351` ③ reported `cc66` finding all seven of its `C13` literals occurring EXACTLY ONCE -- so not
  one of those rows was owed for uniqueness -- and asked for a line on whether the owed list is a
  uniqueness backlog.*  ⇒⇒ *** ON THIS BLOCK IT IS: `17` of `30` literals occur MORE THAN ONCE in a
  single file of the corpus text they are pinned into, one of them `15` times. ***
  ⚠ ** And the arbiter's own blind spot is measured rather than described: ** `7` of the `30` occur
  NOWHERE in the text set it reads, because they are `SOURCE` pins into `scripts/`, `kills/` and the
  root registers.  *Those `7` are counted as NOT multi-site, so **the share is a LOWER BOUND** and
  the arm fails high either way -- over the `23` the arbiter can see it is `17` of `23`.*

** Ⓓ ARM ⒞ -- `7` OF THE `10` RECEIPTS CARRY A CANNOT-FAIL GUARD.  ⛔ OUTSIDE THE BAND, HIGH. **
Central `1` of `10`, band `1`-`3`, decisive `0.361`.

  *`r7349` ② asked for one line on the rate -- three in one phase, all this seat's, and the shape one
  shape: **a guard asserting a property of the CLASS where the claim is about the MEMBER.***
  ⇒⇒ *** AND THE TWO ARMS ARE ONE ARM, WHICH IS THIS REVISION'S REAL FINDING: a literal occurring more
      than once in the file its check reads CANNOT DISTINGUISH the site the claim is about, so every
      uniqueness failure IS a class-where-the-claim-is-about-a-member guard. ***  **Arm ⒞'s `7` is arm
  ⒝'s `17` projected onto receipts, and the two bands were registered as independent when they are
  not.**  ⌗ *Registered separately on purpose, from two different orders, and they collided -- which
  is worth more than either would have been alone.*

** Ⓔ THE EFFORT READING, DRAWN FROM THE TWO MEASURED STRIDES AS `r7351` ② ASKS. **  `69.6` minutes
for `10` receipts -- **`6.96` a receipt** -- against a central of `1.5` taken from `70`'s measured
`0.7`-`1.6`, and against the `8.0` the phase was priced on.  *Read off the commit stamps, not an
impression.*  ⇒ *So this seat is `4.6x` the other seat's measured rate and still inside the original
figure; the third stride scores the band, as `r7351` ② says, and this is one of its two readings.*

** Ⓕ ⛔ AND THE REGISTRATION BROKE THE RULE THIS SEAT HAS BEEN REPAIRING ALL NIGHT, IN ITS OWN
MACHINERY. **  `owed()` and `block()` read the LIVE ledger, so *** the census would have returned
NOTHING the moment the block closed -- empty exactly when the work succeeded. ***  The arbiter is
untouched; the population is read at the census commit and asserted there.  ⌗ *Five instances of this
class in one fortnight, and the first in a REGISTRATION rather than a receipt.*

** Ⓖ ⛔⛭⛭ AND THE RATCHET CAUGHT THIS REVISION'S OWN REPAIRS BEING INVISIBLE, WHICH IS THE
THIRD FACE OF ONE CLASS. **  *Eight of the spans minted here came back STALE: the instrument keys a
literal that stands to the LEFT OF AN `in`, and nothing else.*  ⇒ ** A repair that asserts uniqueness
as `haystack.count(span) == 1` -- a STRONGER condition than membership -- removes the key from the
instrument's sight, so the ledger row adjudicating it describes nothing. **
  ⌗ *The three faces now on record, all found by falling into them: a normaliser applied inside the
  reader (`r7336`), a literal reaching its haystack only through a loop variable (`S3`), and now a
  membership test strengthened into a count.*  ⇒ *** In every one the pin got BETTER and the ledger
  went BLIND, which is why the repair here keeps the membership arm beside the count rather than
  choosing between them. ***

** COMPUTES: ** the block's census at a pinned commit; the three arms against their registered bands
with their decisive fractions; the uniqueness count and the receipts it projects onto; the effort in
minutes a receipt from the commit stamps; and the ten receipts, run here.  No paper quantity.

** WHAT IS NOT CLAIMED. **  ** Not that the owed list is a uniqueness backlog in general ** -- one
block, against another seat's one block that read zero, and the two are reported side by side rather
than pooled.  ** Not that arm ⒞'s shape is only uniqueness ** -- the collapse is shown ON THIS BLOCK,
and a guard can assert a class property without any literal at all.  ** Not that the eleventh receipt
is repaired ** -- it is routed with its patch.  ** And not that `6.96` minutes a receipt is this
seat's rate ** -- it is this block's, on one container, with the trunk moving under it.

Written r7356 on `r7353` ①'s order.  Stated for reversal.
"""
import importlib.util
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []

COST = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7356_60_the_eleven', 'cost.py')
#: this revision's own commits: the registration, and the last repair
REG = '51995684'
WORK = '224be1de'
ROUTED = 'receipts/L257_the_label_did_double_duty'


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def git(*a):
    return subprocess.run(['git', '-C', ROOT, *a], capture_output=True, text=True,
                          errors='replace').stdout


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    print()
    print('  S50 -- the eleven close whole, and all three arms fail high')
    print()
    C = load(COST, 'r7356_cost')
    R = C.RESULT

    # ── Ⓐ the census, read at the commit the block stood at ──────────────────────────────────────
    _owed = C.owed_at()
    _receipts = sorted({r[0] for r in _owed})
    _routed = [r for r in _owed if r[0].startswith(ROUTED)]
    _editable = sorted({r[0] for r in _owed if not r[0].startswith(ROUTED)})
    check(f'Ⓐ① the block at the census commit {C.CENSUS}: {len(_owed)} owed rows in '
          f'{len(_receipts)} receipts, {len(_owed)/len(_receipts):.2f} a receipt',
          len(_owed) == 30 and len(_receipts) == 11)
    check(f'Ⓐ② ⛔ and {len(_routed)} of them are on this seat\'s own DO-NOT-EDIT list, in one '
          f'receipt, so the arm\'s population is the {len(_editable)} this seat may edit',
          len(_routed) == 5 and len(_editable) == 10 and C.A_SPACE == 10)
    #: ⛭ and the live state is asserted separately and MONOTONE, which is the rule this revision's
    #: own registration broke: the owed count of this block only falls, because closing it is the work.
    _live = [l.split('\t') for l in
             open(os.path.join(ROOT, 'corpus', 'quote_pin_baseline.tsv'), encoding='utf-8')
             if l.startswith('receipts/')]
    _live_owed = [r for r in _live if r[5] == 'REPAIR-OWED'
                  and r[0].split('/')[1] in {p.split('/')[1] for p in _receipts}]
    check(f'Ⓐ③ ⛭ and the LIVE state, stated monotone: {len(_live_owed)} owed row(s) remain in this '
          f'block against {len(_owed)} at the census -- and the only ones left are the routed five',
          len(_live_owed) <= len(_owed)
          and all(r[0].startswith(ROUTED) for r in _live_owed))

    # ── Ⓑ arm ⒜, with the ten RUN here ───────────────────────────────────────────────────────────
    _rc = {}
    for _p in _editable:
        _rc[_p] = subprocess.run([sys.executable, os.path.join(ROOT, _p)],
                                 capture_output=True, text=True).returncode
    print(f'      the ten, run here: {sorted(_rc.values())}')
    check(f'Ⓑ① arm ⒜ scored as registered: {R["A_CLOSED"]} of {C.A_SPACE} closed against band '
          f'{C.A_BAND[0]}-{C.A_BAND[1]}, central {C.A_CENTRAL} -- ⛔ OUTSIDE, HIGH',
          R['A_CLOSED'] == 10 and not (C.A_BAND[0] <= R['A_CLOSED'] <= C.A_BAND[1]))
    check(f'Ⓑ② and every one of the ten RUNS GREEN here rather than being cited '
          f'({sum(1 for v in _rc.values() if v == 0)} of {len(_rc)} exit 0)',
          all(v == 0 for v in _rc.values()) and len(_rc) == 10)
    check(f'Ⓑ③ and the band could have failed at the size it is scored at: decisive '
          f'{C.decisive(C.A_SPACE, C.A_CENTRAL, C.A_BAND):.3f}, two-sided',
          C.decisive(C.A_SPACE, C.A_CENTRAL, C.A_BAND) >= 0.10)

    # ── Ⓒ arm ⒝, the arbiter applied at the pin ──────────────────────────────────────────────────
    # ⛔⛭⛭⛭ r7364+60: AND THIS ARM'S ARBITER READS THE CORPUS **LIVE**, WHICH IS THE DEFECT `r7358`
    #   WITHDREW THE HEADLINE FOR, ARRIVING IN THE GATE THAT SCORES IT.  *`r7356`'s
    #   `_corpus_texts()` takes no sha: it lists `corpus/` on the tree it is run on, and `corpus/`
    #   includes the `.tsv` ledgers.  **So the number this gate pins moves with every adjudication
    #   any seat makes** -- it stood at `17` of `30` when the arm was scored and reads `16` live.*
    #   ⇒ *** The frame is supplied HERE, at `r7356`'s own commit, rather than the registration's
    #     arithmetic being edited after the fact: the arm is a FROZEN RECORD of a withdrawn arbiter,
    #     and the live figure is PRINTED beside it with the reason it moved. ***
    #   ⌗ *`r7358` replaced this arbiter with one that excludes the ledgers and `r7360`, `r7362` used
    #     the refined form; nothing here re-opens that -- the withdrawal stands and this gate stops
    #     asserting a live number on the arbiter that was withdrawn.*
    PIN_7356 = '5b76f80a'          # r7356's own first commit: the tree the arm was scored on

    def _texts_at(sha):
        """`corpus/`'s text set AS IT STOOD at `sha` -- the frame `_corpus_texts()` does not take"""
        names = subprocess.run(['git', '-C', ROOT, 'ls-tree', '--name-only', f'{sha}:corpus'],
                               capture_output=True, text=True, errors='replace').stdout.split()
        return {n: subprocess.run(['git', '-C', ROOT, 'show', f'{sha}:corpus/{n}'],
                                  capture_output=True, text=True, errors='replace').stdout
                for n in names if n.endswith(('.tex', '.md', '.tsv', '.txt'))}

    _u = C.uniqueness(_owed, texts=_texts_at(PIN_7356))
    _u_live = C.uniqueness(_owed)
    print(f'      the arbiter at {PIN_7356}, where the arm was scored: '
          f'{sum(1 for v in _u.values() if v > 1)} multi-site of {len(_owed)};  '
          f'LIVE it reads {sum(1 for v in _u_live.values() if v > 1)} -- it counts the `.tsv` '
          f'ledgers, which is what r7358 withdrew this arbiter for')
    _multi = {k: v for k, v in _u.items() if v > 1}
    _unseen = {k: v for k, v in _u.items() if v == 0}
    _share = len(_multi) / len(_owed)
    check(f'Ⓒ① arm ⒝ scored as registered, IN THE FRAME IT WAS SCORED IN: {len(_multi)} of '
          f'{len(_owed)} = {_share:.4f} against band {C.B_BAND[0]}-{C.B_BAND[1]}, central '
          f'{C.B_CENTRAL} -- ⛔ OUTSIDE, HIGH.  ⛭ r7364: *the text set is read at `{PIN_7356}`, '
          f'r7356\'s own commit, because this arbiter lists `corpus/` LIVE and counts the `.tsv` '
          f'ledgers -- so the figure moved with other seats\' adjudications and read '
          f'{sum(1 for v in _u_live.values() if v > 1)} live. The arm is a FROZEN RECORD of the '
          f'arbiter `r7358` withdrew, and the live figure is printed above rather than asserted*',
          len(_multi) == R['B_MULTI'] and not (C.B_BAND[0] <= _share <= C.B_BAND[1])
          # and the withdrawal is RECORDED rather than left to this comment: the refined arbiter
          # that excludes the ledgers exists, and it is the one the later blocks were read on.
          and 'baseline' in open(os.path.join(
              ROOT, 'computations', 'beyond_the_wall', 'r7358_60_the_queue', 'cost.py'),
              encoding='utf-8', errors='replace').read())
    check(f'Ⓒ② ⛭ and it contradicts the expectation the order carried: the other seat found 0 of 7 '
          f'of its own block\'s literals occurring more than once, and this block reads '
          f'{len(_multi)} of {len(_owed)}, the worst of them {max(_multi.values())} times',
          max(_multi.values()) > 10)
    check(f'Ⓒ③ ⚠ and the arbiter\'s blind spot is MEASURED: {len(_unseen)} of the {len(_owed)} occur '
          f'nowhere in the text set it reads, so they are counted NOT multi-site and the share is a '
          f'LOWER bound -- over the {len(_owed) - len(_unseen)} it can see it is '
          f'{len(_multi)}/{len(_owed) - len(_unseen)}',
          len(_unseen) == R['B_UNSEEN']
          and len(_multi) / (len(_owed) - len(_unseen)) > _share)

    # ── Ⓓ arm ⒞, and the collapse ────────────────────────────────────────────────────────────────
    _per = {}
    for (_path, _lit), _n in _u.items():
        _per.setdefault(_path, []).append(_n)
    _guarded = sorted(p for p in _editable if any(n > 1 for n in _per.get(p, [])))
    check(f'Ⓓ① arm ⒞ scored as registered: {len(_guarded)} of {C.C_SPACE} receipts carry a guard of '
          f'that shape against band {C.C_BAND[0]}-{C.C_BAND[1]}, central {C.C_CENTRAL} -- ⛔ '
          f'OUTSIDE, HIGH', len(_guarded) == R['C_GUARDS']
          and not (C.C_BAND[0] <= len(_guarded) <= C.C_BAND[1]))
    #: ⛭⛭ THE COLLAPSE, ASSERTED AND NOT NARRATED: the receipts arm ⒞ counts are EXACTLY the
    #: receipts holding a row arm ⒝ counts.  ** A literal occurring more than once cannot
    #: distinguish the site the claim is about, so the two arms measure one quantity. **
    _b_receipts = sorted({k[0] for k in _multi if not k[0].startswith(ROUTED)})
    check(f'Ⓓ② ⛭⛭ and the two arms are ONE ARM: the receipts arm ⒞ counts are exactly those holding '
          f'a row arm ⒝ counts ({len(_guarded)} = {len(_b_receipts)}, same set), so arm ⒞ is arm ⒝ '
          f'projected onto receipts and the two bands were registered as independent when they are '
          f'not', _guarded == _b_receipts and R['C_IS_B_PROJECTED'] is True)

    # ── Ⓔ the effort reading, from the commit stamps ──────────────────────────────────────────────
    _t0 = int(git('log', '-1', '--format=%ct', REG).strip() or 0)
    _t1 = int(git('log', '-1', '--format=%ct', WORK).strip() or 0)
    _mins = (_t1 - _t0) / 60.0
    check(f'Ⓔ① the effort read off the commit stamps: {_mins:.1f} minutes for {R["REALISED"]} '
          f'receipts = {_mins/R["REALISED"]:.2f} a receipt, against the {C.EFFORT_CENTRAL_MIN_PER_RECEIPT} '
          f'drawn from the two measured strides and the {C.EFFORT_SUPERSEDES} the phase was priced on',
          _t1 > _t0 and abs(_mins - R['EFFORT_MINUTES']) < 2.0)
    check(f'Ⓔ② ⌗ and it is REPORTED, not banded, as `r7351` ② asks -- two strides do not fix a band '
          f'and the third scores it: this reading is {_mins/R["REALISED"]/C.EFFORT_CENTRAL_MIN_PER_RECEIPT:.1f}x '
          f'the other seat\'s measured rate and still inside the original figure',
          _mins / R['REALISED'] > C.EFFORT_CENTRAL_MIN_PER_RECEIPT
          and _mins / R['REALISED'] < C.EFFORT_SUPERSEDES)

    # ── Ⓕ the registration's own fail-on-success, declared ───────────────────────────────────────
    #: ** Asserted rather than confessed: the function as written returns NOTHING now, which is what
    #: it would have returned to the scoring push. **
    check(f'Ⓕ① ⛔ and the registration\'s own census read the LIVE ledger, so it returns '
          f'{len(C.owed())} row(s) now that the block is closed -- empty exactly when the work '
          f'succeeded, which is the class this seat has repaired five times this fortnight',
          len(C.owed()) == len(_routed) and len(C.owed()) < len(_owed))
    check('Ⓕ② while the pinned reading it is replaced by returns the whole census, and the arbiter '
          'between them is unchanged -- only the commit the population is read at moved',
          len(C.owed_at()) == 30)

    # ── Ⓖ the routed five ────────────────────────────────────────────────────────────────────────
    check(f'Ⓖ① the eleventh receipt is ROUTED and untouched: {len(_routed)} rows, and this '
          f'revision\'s own commits touch no file under that prefix',
          len(_routed) == 5
          and not any(f.startswith(ROUTED) for c in
                      [x for x in git('rev-list', '--no-merges', f'{REG}~1..{WORK}').split('\n') if x]
                      for f in git('show', '--name-only', '--format=', c).split('\n')))

    # ── Ⓗ restraint: this revision's own commits ─────────────────────────────────────────────────
    _own = [c for c in git('rev-list', '--no-merges', f'{REG}~1..{WORK}').split('\n') if c]
    _touched = sorted({f for c in _own
                       for f in git('show', '--name-only', '--format=', c).split('\n')
                       if f.startswith('receipts/')})
    check(f'Ⓗ① this revision\'s own commits, merges excluded: {len(_own)}, touching '
          f'{len(_touched)} receipt file(s) -- the ten of the block and nothing else',
          sorted(_touched) == _editable)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** THE BLOCK CLOSES WHOLE AND ALL THREE ARMS FAIL HIGH. **')
    print('  Ⓐ ** 30 rows in 11 receipts, one of them not this seat\'s to repair: ** the routed five')
    print('     go to the gate with a patch, so the arm is scored on the ten.')
    print('  Ⓑ ⛔ ** Arm ⒜: 10 of 10, against a band of 6–9. ** Every one run here.')
    print('  Ⓒ ⛔ ** Arm ⒝: 17 of 30 — 0.567 against a band of 0.08–0.33. ** ⇒ *** On this block the')
    print('     owed list IS a uniqueness backlog, where the other seat read zero of seven. *** And')
    print('     7 rows sit outside the arbiter\'s text set, so the share is a LOWER bound.')
    print('  Ⓓ ⛔⛭⛭ ** Arm ⒞: 7 of 10 — AND IT IS ARM ⒝ PROJECTED ONTO RECEIPTS. ** A literal that')
    print('     occurs more than once cannot distinguish the site the claim is about, so every')
    print('     uniqueness failure IS a class-where-the-claim-is-about-a-member guard.')
    print('     ⇒ *** Two arms registered as independent, from two different orders, measuring one')
    print('       quantity — which is worth more than either would have been alone. ***')
    print('  Ⓔ ** Effort: 6.96 minutes a receipt ** against 1.5 measured elsewhere and 8.0 priced.')
    print('  Ⓕ ⛔ ** And the registration\'s own census read the live ledger: ** it returns the routed')
    print('     five now and would have returned them to its own scoring push.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
