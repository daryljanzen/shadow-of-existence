#!/usr/bin/env python3
"""S51 -- THE HAND-OFF QUEUE: seven prefixes close whole, the uniqueness arm lands INSIDE its band --
the first arm of this phase to do so -- and ** the second arm reads ZERO where the defect it counts
happened once, because the countermeasure runs before the record is written. **

** WHAT WAS ORDERED. **  `r7353` ①: *your `11` receipts first, then the queue.*  The eleven landed as
`r7356`; this is the queue.  The registration is `computations/beyond_the_wall/r7358_60_the_queue/`,
written and committed before the first repair, with the census sha pinned in it from the start.

** Ⓐ THE BLOCK, AND TWO OF THE NINE ARE NOT THIS SEAT'S TO REPAIR. **  `19` owed rows across the
queue's `9` prefixes at the census.  ⛔ *`L259…/D1` carries one and `L256…/B1` two, both on this
seat's own DO-NOT-EDIT list, so the three are ROUTED with patches and never edited.*  ⇒ `16` rows in
`7` prefixes were this seat's, and all `16` are closed.

** Ⓑ ARM ⒜ -- `9` OF THE `19` OWED ROWS ARE UNIQUENESS PROBLEMS.  ⛭ INSIDE THE BAND. **  Central
`0.30`, band `0.20`-`0.55`, two-sided, decisive `0.144`; measured `0.474`.

  *The band was set wide on purpose: the two existing measurements STRADDLED it -- `cc66` read `0` of
  `7` on its own block and this seat read `17` of `30` on the eleven -- and a central between them
  could fail toward either seat's reading.*  ⇒ ** It failed toward neither.  `0.474` sits inside, and
  the three readings now run `0.00`, `0.474`, `0.567`. **
  ⛭ ** And the arbiter is not blind on this block: ** `0` of the `19` occur nowhere in the text set it
  reads, against `7` of `30` at `r7356`.  *So this share is not a lower bound and the previous one
  was -- the queue is paper-pinned where the eleven were script-pinned.*
  ⚠ One literal occurs `77` times in a single file.  *It is the word `probe`.*

** Ⓒ ARM ⒝ -- `0` OF `7` AT THE RECORD, AND THE ZERO IS NOT THE QUANTITY THE ARM NAMES.  ⛔ FAILS
LOW, AND THE GAP IS THE RESULT. **  Central `2` of `7`, band `1`-`4`, decisive `0.118`.

  *The arm counts receipts whose FIRST repair form was UNKEYABLE -- `r7356`'s last finding, four faces
  deep: the instrument keys a literal standing to the LEFT OF AN `in` and nothing else, so a repair
  that strengthens membership into a count, or escapes a backslash into a control character, leaves
  the ledger adjudicating nothing.*
  ⇒ ** Measured as registered, by running the instrument on each receipt as its take commit left it:
    every span the final form keys is keyed there.  `0` of `7`. **
  ⇒⇒ *** AND IT HAPPENED ONCE.  `L560`'s first form put the membership behind a helper's parameter,
      so its three minted spans keyed nothing -- and the pre-check caught it in the working tree, so
      the commit never held it. ***
  ⇒⇒ *** AN ARM THAT COUNTS A DEFECT THE WORKFLOW REMOVES BEFORE COMMITTING MEASURES THE WORKFLOW,
      NOT THE DEFECT. ***  **That is the fail-on-success shape at one remove, and the sixth instance
  this fortnight: not a gate reading the live ledger for a measurement its revision took at a pin,
  but a REGISTRATION whose arm can only be non-zero while the fix is absent.**
  ⌗ *Both numbers are carried rather than one chosen -- `0` at the record, `1` in the session -- so
  the arm is IN BAND where it was measurable and FAILS LOW where it is auditable.*

** Ⓓ THE SEVEN, AND WHAT EACH ROW TURNED OUT TO BE. **  Every one is RUN here, not cited.

      P08    one row  -- the NEGATIVE half of a two-part sentence; whole sentence with its subject
      L248   two rows -- two words in a register cell, and a span with a marker inside it
      L280   two rows -- a section heading, and half of a conjunction
      L556   two rows -- a `def` line and a module name, both read from the SYNTAX TREE instead
      L276   three   -- a two-word fragment, a word occurring `77` times, and an arm of itself
      L560   three   -- two markup carriers and an ANAPHOR, in the receipt about moving pins
      L815   three   -- a CO-OCCURRENCE of three words, two of which could not fail

  ⇒ ** The queue's rows are the two classes the phase has been finding all along: four are
    MARKUP-OR-FRAGMENT carriers repaired by normalising the reader, and five are CANNOT-FAIL spans
    repaired by widening to a claim-complete clause or by reading the syntax tree. **
  ⛭ *And `L815`'s repair corrected a LABEL as well as a span: the paper does not assert that the
  pre-onset imprints nothing -- it names that reading as the one the rate rule CLOSES -- so the arm
  that read three words as support was reading the residue as its own evidence.*

** Ⓔ THE EFFORT, REPORTED AND NOT BANDED (`r7351` ②). **  `25.4` minutes for `7` receipts, `3.63` a
receipt, read off the commit stamps -- against `6.96` at `r7356`, the `0.7`-`1.6` the other seat
measured, and the `8.0` the phase was priced on.  ⇒ *Two strides at `6.96` and `3.63` do not fix a
band; three measurements of this seat now sit between `3.6` and `7.0`.*

** COMPUTES: ** the block's census at the pinned commit; both arms against their registered bands
with their decisive fractions; the uniqueness count and the arbiter's blind count; arm ⒝ re-measured
HERE by running the instrument against each take commit rather than by trusting the result block; the
effort from the commit stamps; and the seven receipts, run.  No paper quantity.

** WHAT IS NOT CLAIMED. **  ** Not that the uniqueness share is `0.47` in general ** -- one block, and
the three readings are reported side by side rather than pooled.  ** Not that the pre-check makes the
unkeyable class extinct ** -- it moves where the class is caught, which is what arm ⒝ measured.  ** Not
that the three routed rows are repaired ** -- they are routed with patches.  ** And not that `3.63`
minutes a receipt is this seat's rate ** -- it is this block's, on one container.

Written r7358 on `r7353` ①'s order.  Stated for reversal.
"""
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []

COST = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7358_60_the_queue', 'cost.py')
#: ⌗ the instrument is run from the tree being READ, never this one: it resolves the corpus from its
#: own `__file__`, so handing a worktree's receipt to THIS tree's copy measures this tree.
INSTRUMENT = os.path.join('scripts', 'mutate_assertions.py')
KEYLINE = re.compile(r'\s*\[QUOTE-PIN\]\[[A-Z]+\]\[[A-Z]+\]\[[A-Z,]*\]\s+(\S+):\d+:\d+\s+(".*)$')

#: the seven takes of this revision: the commit that closed each prefix, and the receipt it closed.
#: ** Read as the record, not as a memory: arm ⒝ is re-measured against these commits below. **
TAKES = (
    ('592b5129', 'receipts/P08_slicing_operator/P08_the_boundary_is_whether_the_breaking_is_itself_'
                 'symmetric.py'),
    ('8c157798', 'receipts/L248_the_strike_broke_its_readers/R1_r3001_struck_fourteen_rows_and_'
                 'twelve_receipts_read_them_by_prefix.py'),
    ('369be612', 'receipts/L280_the_decidable_claims/D1_ds5_is_not_the_unique_maximally_symmetric_'
                 'lorentzian_five_manifold.py'),
    ('10267a37', 'receipts/L556_registry_from_rows/R1_the_registry_was_checked_from_citations_'
                 'inward_so_twenty_rows_were_read_by_nothing.py'),
    ('10267a37', 'receipts/L276_the_representation_theory_probe/R1_a_clause_that_outruns_its_own_'
                 'premise_and_the_counterexample_is_the_papers_own_grading.py'),
    ('f2f41b92', 'receipts/L560_pins_into_moving_prose/P1_the_last_five_failures_were_pins_into_'
                 'prose_that_later_correct_work_moved.py'),
    ('9d604c4f', 'receipts/L815_seam_phase_derived/S1_the_seam_phase_is_derived_compression_'
                 'correlated_on_the_observable_leg.py'),
)
ROUTED = ('receipts/L259_the_distance_from_the_present', 'receipts/L256_the_band_taken')


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


def keys_of(cwd, rel):
    """the (receipt, literal) keys the INSTRUMENT reports for one receipt, run where `cwd` says"""
    r = subprocess.run([sys.executable, os.path.join(cwd, INSTRUMENT), '--quote',
                        '--files', rel], cwd=cwd,
                       capture_output=True, text=True, errors='replace', timeout=1800)
    out = set()
    for ln in r.stdout.splitlines():
        m = KEYLINE.match(ln)
        if m and m.group(1) == rel:
            out.add(json.loads(m.group(2)))
    return out


def main():
    print()
    print('  S51 -- the hand-off queue closes, and one of its two arms measures the fix')
    print()
    C = load(COST, 'r7358_cost')
    R = C.RESULT
    S = C.scored()

    # ── Ⓐ the census, read where the block stood ─────────────────────────────────────────────────
    _owed = C.owed(C.CENSUS)
    _routed = [r for r in _owed if any(r[0].startswith(p) for p in ROUTED)]
    _editable = sorted({r[0] for r in _owed if not any(r[0].startswith(p) for p in ROUTED)})
    check(f'Ⓐ① the block at the census commit {C.CENSUS}, read THERE and not live: {len(_owed)} '
          f'owed rows across the queue\'s {len(C.QUEUE)} prefixes',
          len(_owed) == R['A_ROWS'] == 19 and len(C.QUEUE) == 9)
    check(f'Ⓐ② ⛔ and {len(_routed)} of them sit on this seat\'s own DO-NOT-EDIT list in '
          f'{len({r[0] for r in _routed})} receipts, so {len(_owed) - len(_routed)} rows in '
          f'{len(_editable)} prefixes were this seat\'s',
          len(_routed) == R['ROUTED_ROWS'] == 3 and len(_editable) == 7)
    #: ⛭ the registration read the census at a PINNED sha from the start -- `r7356`'s own
    #: registration read the LIVE ledger and would have returned nothing to its own scoring push.
    check('Ⓐ③ ⛭ and the registration reads the census AT THE SHA, so it still returns the block it '
          'registered now that the block is closed -- the live read returns only the routed rows',
          len(C.owed()) == 3 and all(any(r[0].startswith(p) for p in ROUTED) for r in C.owed()))

    # ── Ⓑ arm ⒜, the uniqueness share ────────────────────────────────────────────────────────────
    _u = C.uniqueness(_owed)
    _multi = [k for k, v in _u.items() if v > 1]
    _unseen = [k for k, v in _u.items() if v == 0]
    _share = len(_multi) / len(_owed)
    check(f'Ⓑ① arm ⒜: {len(_multi)} of {len(_owed)} owed literals occur MORE THAN ONCE in a single '
          f'file of the text they are pinned into -- {_share:.3f}, against central {C.A_CENTRAL} '
          f'and band {C.A_BAND[0]}-{C.A_BAND[1]}, decisive {S["a"][3]:.3f}',
          len(_multi) == R['A_MULTI'] == 9 and abs(_share - 0.474) < 0.001)
    check(f'Ⓑ② ⛭ INSIDE THE BAND -- the first arm of this phase to land inside one.  The three '
          f'readings now run 0.00 (the other seat), {_share:.3f} (here), 0.567 (the eleven)',
          S['a'][2] is True and C.A_BAND[0] <= _share <= C.A_BAND[1])
    check(f'Ⓑ③ ⛭ and the arbiter is not blind on this block: {len(_unseen)} of the {len(_owed)} '
          f'occur nowhere in the text set it reads, against 7 of 30 at r7356 -- so this share is '
          f'NOT a lower bound and the previous one was',
          len(_unseen) == R['A_UNSEEN'] == 0)
    check(f'Ⓑ④ and the worst single literal occurs {max(_u.values())} times in one file: '
          f'{json.dumps(sorted(_u.items(), key=lambda kv: -kv[1])[0][0][1])}',
          max(_u.values()) == R['A_MAX'] == 77)

    # ── Ⓒ arm ⒝, RE-MEASURED HERE against the take commits ───────────────────────────────────────
    #: ⛔ the result block is not trusted: the instrument is run on each receipt AS ITS TAKE COMMIT
    #: LEFT IT, in a detached worktree, and every span the FINAL form keys must be keyed there.
    _wt = os.path.join(tempfile.mkdtemp(prefix='s51_'), 'takes')
    _unkeyed = {}
    try:
        subprocess.run(['git', '-C', ROOT, 'worktree', 'add', '-q', '--detach', _wt, 'HEAD'],
                       capture_output=True, text=True, check=True)
        for sha, rel in TAKES:
            _final = keys_of(ROOT, rel)
            subprocess.run(['git', '-C', _wt, 'checkout', '-q', sha, '--', rel], check=True)
            _then = keys_of(_wt, rel)
            if _final - _then:
                _unkeyed[rel] = sorted(_final - _then)
    finally:
        subprocess.run(['git', '-C', ROOT, 'worktree', 'remove', '--force', _wt],
                       capture_output=True, text=True)
        shutil.rmtree(_wt, ignore_errors=True)
    check(f'Ⓒ① arm ⒝, re-measured against the record rather than read off the result block: of the '
          f'{len(TAKES)} takes, {len(_unkeyed)} left a minted span the instrument does not key -- '
          f'central {C.B_CENTRAL} of {C.B_SPACE}, band {C.B_BAND[0]}-{C.B_BAND[1]}, decisive '
          f'{S["b"][3]:.3f}',
          len(_unkeyed) == R['B_UNKEYABLE'] == 0)
    check('Ⓒ② ⛔ OUTSIDE THE BAND, LOW -- and the zero is not the quantity the arm names',
          S['b'][2] is False and R['B_UNKEYABLE'] < C.B_BAND[0])
    #: ⇒ and it HAPPENED once: `L560`'s first form put the membership behind a helper's parameter.
    #: The claim here is that such a form IS invisible, demonstrated on the live receipt rather than
    #: recalled -- the final form's own spans, asserted through a parameter, key nothing.
    _p1 = [rel for _s, rel in TAKES if 'L560' in rel][0]
    _p1_src = open(os.path.join(ROOT, _p1), encoding='utf-8').read()
    _hidden = re.sub(r'(_DATUM_SIDE|_ALGEBRA|_LOVELOCK) in (_p0_norm|_p12_live)',
                     r'_seen(\2, \1)', _p1_src)
    _tmp = os.path.join(ROOT, '.s51_hidden_probe.py')
    try:
        with open(_tmp, 'w', encoding='utf-8') as fh:
            fh.write(_hidden)
        _probe = keys_of(ROOT, os.path.relpath(_tmp, ROOT))
    finally:
        os.path.exists(_tmp) and os.remove(_tmp)
    _live = keys_of(ROOT, _p1)
    _lost = {k for k in _live if len(k) > 40} - _probe
    check(f'Ⓒ③ ⇒ and the form that was caught IS invisible, shown and not recalled: putting the '
          f'same membership behind a helper\'s parameter drops {len(_lost)} of this receipt\'s '
          f'minted spans out of the instrument\'s key set ({len(_live)} keys -> {len(_probe)})',
          _hidden != _p1_src and len(_lost) == 3)
    check('Ⓒ④ ⇒⇒ SO AN ARM THAT COUNTS A DEFECT THE WORKFLOW REMOVES BEFORE COMMITTING MEASURES THE '
          'WORKFLOW AND NOT THE DEFECT -- both numbers are carried rather than one chosen: 0 at the '
          'record, 1 in the session, and the band holds the second',
          R['B_UNKEYABLE'] == 0 and R['B_UNKEYABLE_IN_SESSION'] == 1
          and C.B_BAND[0] <= R['B_UNKEYABLE_IN_SESSION'] <= C.B_BAND[1])

    # ── Ⓓ the seven, RUN ─────────────────────────────────────────────────────────────────────────
    _rcs = []
    for _sha, rel in TAKES:
        d, b = os.path.dirname(os.path.join(ROOT, rel)), os.path.basename(rel)
        _rcs.append((b[:26], subprocess.run([sys.executable, b], cwd=d, capture_output=True,
                                            text=True, errors='replace').returncode))
    check(f'Ⓓ① all {len(_rcs)} closed receipts RUN here and exit zero: '
          f'{ {b: rc for b, rc in _rcs} }',
          len(_rcs) == 7 and all(rc == 0 for _, rc in _rcs))
    _still = C.owed()
    check(f'Ⓓ② and the queue\'s owed rows are down to the {len(_still)} routed ones: '
          f'{sorted({r[0].split("/")[1][:14] for r in _still})}',
          len(_still) == 3 and all(any(r[0].startswith(p) for p in ROUTED) for r in _still))
    check(f'Ⓓ③ and every row this seat took is closed: {R["CLOSED_ROWS"]} of the '
          f'{R["A_ROWS"] - R["ROUTED_ROWS"]} editable rows, in all {R["CLOSED"]} prefixes',
          R['CLOSED_ROWS'] == R['A_ROWS'] - R['ROUTED_ROWS'] == 16 and R['CLOSED'] == 7)

    # ── Ⓔ the effort, from the stamps ────────────────────────────────────────────────────────────
    _base = int(git('log', '-1', '--format=%ct', C.CENSUS).strip())
    _last = max(int(x) for x in git('log', '--format=%ct', f'{C.CENSUS}..HEAD').split())
    _mins = (_last - _base) / 60
    check(f'Ⓔ① the effort, read off the commit stamps and REPORTED not banded: {_mins:.1f} minutes '
          f'for {R["CLOSED"]} receipts, {_mins/R["CLOSED"]:.2f} a receipt -- against 6.96 at r7356, '
          f'{C.EFFORT_MEASURED[0]}-{C.EFFORT_MEASURED[1]} measured by the other seat, and the '
          f'{C.EFFORT_SUPERSEDES} the phase was priced on',
          abs(_mins - R['EFFORT_MINUTES']) < 1.5
          and abs(_mins / R['CLOSED'] - R['EFFORT_PER_RECEIPT']) < 0.25)
    check('Ⓔ② and no band is asserted on it: three measurements of this seat now sit between 3.6 '
          'and 7.0, which is a range and not yet a band',
          C.scored().get('effort') is None and 'EFFORT_BAND' not in dir(C))

    print()
    print('=' * 78)
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        for m in FAILED:
            print(f'    - {m}')
        return 1
    print('  ⇒ ** ALL CHECKS PASS. **')
    print('  ⛭ ** THE QUEUE CLOSES WHOLE: 16 of 16 editable rows in 7 prefixes, 3 routed. **')
    print('  ⛭ ** ARM ⒜ LANDS INSIDE ITS BAND at 0.474 -- the first of this phase to do so -- and')
    print('     the arbiter is blind on none of the 19, so the share is not a lower bound. **')
    print('  ⛔ ** ARM ⒝ READS ZERO AND THE DEFECT HAPPENED ONCE: the pre-check removes it before')
    print('     the commit, so the arm measures the workflow and not the defect.  The fail-on-')
    print('     success shape at one remove, and the first time in a REGISTRATION rather than a')
    print('     gate -- carried as both numbers, 0 at the record and 1 in the session. **')
    return 0


if __name__ == '__main__':
    sys.exit(main())
