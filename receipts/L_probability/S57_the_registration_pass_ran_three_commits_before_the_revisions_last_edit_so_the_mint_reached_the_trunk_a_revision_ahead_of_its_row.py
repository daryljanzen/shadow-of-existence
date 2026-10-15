#!/usr/bin/env python3
"""S57 -- THE ROW ONE REVISION BEHIND THE MINT.  ⛭⛭⛭ *** 66's `r7367` ⑥ REPORTS THE TRUNK'S QUOTE-PIN
RATCHET RED ON TWO CODE PINS OF `S55`'s AND READS THEM AS `r7370`'s UNADJUDICATED MINTS.  BOTH HALVES
OF THAT READING ARE OFF BY ONE REVISION, AND THE OFF-BY-ONE IS THE FINDING. ***

** Ⓐ THE KEYS ARE ADJUDICATED, AND HAVE BEEN SINCE `r7370`. **  `"_PINNED"` and `"def _class_of"`
both carry `DELIBERATE` with a reason each.  *So nothing is unverdicted anywhere; a verdict is simply
somewhere the reader is not.*

** Ⓑ THE OFF-BY-ONE, ON PINNED SHAS. **  The two literals were introduced by `0d8ac35c`, whose
subject claims **`r7368`** and which **is** an ancestor of the trunk `66` read.  Their rows were
written by `ba75b3fb`, whose subject claims **`r7370`** and which is **not**.
  ⇒ *** THE TRUNK TOOK THE MINT ONE REVISION AHEAD OF THE ROW. ***  *That is the whole of the red:
      not a missing verdict, a verdict on the other side of a merge boundary.*

** ⛔⛭⛭ Ⓒ AND THE REGISTERED REASONING FOR IT WAS WRONG, WHICH THE SCAN SAID AND THE ARGUMENT COULD
NOT. **  `r7372`'s `PREDICTION.md` argued the gap opened by *deferring a registration pass across
revisions* -- this seat's own `r7368` rule that *every receipt edit mints keys, so registration
happens in ONE pass on a settled tree*.  ⛔ *The mechanism says otherwise.*  `r7368` ran its own
registration pass at `3f30509e` and then made **three more receipt commits**, the first of which is
`0d8ac35c`.
  ⇒ ** The pass did not run a revision late.  It ran three commits early, INSIDE the revision --
    which is `66`'s SECOND candidate cause and not this seat's first. **
  ⌗ *`2` of `2` late rows were minted after their own revision's pass; there is no third mechanism
    left to look for in this class, because the class has exactly two members.*

** Ⓓ THE ARMS, REGISTERED BEFORE THE SCAN. **
      ⒜ *LATE rows* -- mint revision != row revision.  Central `7`, band `2`-`21`.  Measured **`2`**
        -- INSIDE, at the floor.  *The two keys `66` named are the entire class, against `50` rows
        that landed in their own revision.*
      ⒝ *EXPOSED rows* -- mint on the pinned trunk, row not.  Central `2`, band `2`-`14`.  Measured
        **`2`** -- INSIDE, at the floor.
      ⒞ *EARLY rows* -- row revision below mint revision.  Exact `0`.  Measured **`0`** -- HIT, and
        asserted here as a PROPERTY over every added row rather than as a count that happens to be
        zero.
      ⛔ ⒟ *the within-revision window* -- receipt commits following a revision's last pass.  Central
        `2`, band `1`-`6`.  Measured **`7`** -- **ABOVE.  The one miss, and it is the one that
        matters**: the window is open in `4` of the `5` revisions measured and seven commits wide, so
        it was never a one-off.  *Registered at a band that assumed the cross-revision story; the
        band was wrong because the story was.*

** ⛭⛭ Ⓔ AND THE ONE REVISION WITH THE WINDOW CLOSED CLOSED IT BY REGISTERING THREE TIMES. **
`r7356` has `3` registration passes and `0` receipt commits after the last.  ⇒ *** So the rule that
stopped stale rows is the rule that opened this window: `r7336`'s eight stale spans bought ONE pass
per revision, and one pass per revision is a pass that cannot be last unless it is also final. ***
  ⌊ *Two readings off one choice, which is `r7368` ②'s shape one level up -- `accurate` and `last`
    are different properties of a pass and both were read off `how many`.*

** Ⓕ THE REMEDY IS A PREDICATE AND IT IS EVALUATED, NOT ARGUED. **  *At the moment a revision is
pushed, every literal its own receipt edits introduced must already carry a row.*  Evaluated on two
pinned shas: at `r7368`'s LAST commit it reports **both** keys uncovered, and at the pass that
finally wrote them it reports **none**.  ⌗ *A condition that fires nowhere is not a condition, and a
condition that fires everywhere is not one either.*

** Ⓖ THE DETECTOR IS NOT COPIED HERE. **  ⌗ *`r7370`'s reply routed a fork of exactly this shape --
one refinement predicate living in a computation AND restated in a receipt -- with the
recommendation that it move into the definition and be consumed.  This file takes its own
recommendation: every figure is read from `measure()` in the revision's `cost.py`, the pinned shas
are read from that module rather than re-spelled here, and both facts are asserted as properties of
this file's source.*
  ⚠ *And the property test for "this file contains no pickaxe call" cannot spell the pickaxe flag,
    because spelling it would make the test match itself -- the `ABOUT` class from `r7370` ④,
    arriving in a two-line assertion.*

    python3 receipts/L_probability/S57_the_registration_pass_ran_three_commits_before_the_revisions_last_edit_so_the_mint_reached_the_trunk_a_revision_ahead_of_its_row.py
"""
import importlib.util
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []
BAR = '=' * 100

COST = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                    'r7372_60_the_row_one_revision_behind_the_mint', 'cost.py')
GATE = os.path.join(ROOT, 'corpus', 'check_pins_adjudicated_on_mint.py')
S55 = 'S55_'
INDEX = os.path.join(ROOT, 'receipts', 'INDEX.md')


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def head(t):
    print(f'\n  {"-" * 96}\n  {t}\n  {"-" * 96}')


def git(*a):
    return subprocess.run(['git', '-C', ROOT, *a], capture_output=True, text=True,
                          errors='replace').stdout


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def one(prefix, where='receipts/L_probability'):
    hits = [x for x in git('ls-files', where).split('\n')
            if os.path.basename(x).startswith(prefix)]
    return hits[0] if hits else None


def main():
    print(__doc__)
    C = load(COST, 'r7372_cost')
    G = load(GATE, 'r7372_mintgate')
    R = C.measure()
    _src = open(os.path.abspath(__file__), encoding='utf-8').read()
    _s55 = one(S55)

    # ── Ⓐ the verdict exists, and the unverdicted class is the gate's own tuple ───────────────────
    head('Ⓐ  the two keys 66 named carry verdicts, and have since r7370')
    _named = {lit: (verdict, why, m, mrev) for _rec, lit, verdict, why, m, mrev in R['named']}
    for lit, (verdict, why, m, mrev) in sorted(_named.items()):
        print(f'      {lit!r:18} {verdict:12} minted {m[:8]} ({mrev})')
    print(f'      the unverdicted class, read from the gate and not typed here: {G.UNVERDICTED}')
    check(f'Ⓐ① both keys 66 named carry a verdict OUTSIDE the gate\'s own unverdicted class, each '
          f'with a non-empty reason: {sorted((l, v) for l, (v, *_r) in _named.items())}',
          len(_named) == 2 and set(_named) == set(C.NAMED)
          and all(v not in G.UNVERDICTED and w.strip() for v, w, _m, _r in _named.values()))

    _rows = R['rows_at_frame']
    _keyed = sorted((os.path.basename(rec)[:4], lit, _rows[(rec, lit)][0])
                    for (rec, lit) in _rows if lit in C.NAMED)
    _s56_ontime = [lit for _rec, lit, _m, _mr, _s, _rr in R['ontime']
                   if lit in C.NAMED and 'S56_' in os.path.basename(_rec)]
    print(f'      every row in the baseline carrying one of the two literals: {_keyed}')
    print(f'      and of those, the ones that landed in their own revision: {_s56_ontime}')
    check(f'Ⓐ② control -- a row is keyed by (receipt, literal) and NOT by the literal alone: '
          f'"def _class_of" carries a SECOND row against S56 with its own verdict, and that one '
          f'landed ON TIME in the revision that minted it -- the same literal, late against one '
          f'receipt and on time against another, which is what makes the finding about the ORDER '
          f'of commits and not about the literal: {_keyed}',
          _keyed == [('S55_', '_PINNED', 'DELIBERATE'),
                     ('S55_', 'def _class_of', 'DELIBERATE'),
                     ('S56_', 'def _class_of', 'DELIBERATE')]
          and _s56_ontime == ['def _class_of'])

    # ── Ⓑ the off-by-one, on pinned shas ──────────────────────────────────────────────────────────
    head('Ⓑ  the off-by-one: the mint is on the trunk and the row is not')
    _mrev, _rrev = C.rev_of(C.MINT_C), C.rev_of(C.ROW_C)
    print(f'      mint {C.MINT_C} -> {_mrev}      row {C.ROW_C} -> {_rrev}')
    check(f'Ⓑ① the pinned shas read back to ADJACENT revisions of this line, mint before row, with '
          f'the corpus\'s own claim_of: {_mrev} then {_rrev}',
          _mrev == 'r7368' and _rrev == 'r7370' and int(_rrev[1:]) > int(_mrev[1:]))

    _found = {lit: C.mint_of(rec, lit) for _rec, lit, _v, _w, _m, _r in R['named']
              for rec in [_rec]}
    check(f'Ⓑ② the pin AGREES with the detector -- the mint commit is not a sha typed beside the '
          f'claim but the one the scan finds for both keys: '
          f'{sorted((l, (s or "-")[:8]) for l, s in _found.items())}',
          len(_found) == 2 and all(s and s.startswith(C.MINT_C) for s in _found.values()))

    _mint_on = C.is_ancestor(C.MINT_C, C.TRUNK)
    _row_on = C.is_ancestor(C.ROW_C, C.TRUNK)
    _live = git('rev-parse', '--short=8', 'origin/main').strip()
    print(f'      pinned trunk {C.TRUNK}: mint on it {_mint_on}, row on it {_row_on}')
    print(f'      the LIVE trunk reads {_live}; mint on it {C.is_ancestor(C.MINT_C, "origin/main")}, '
          f'row on it {C.is_ancestor(C.ROW_C, "origin/main")} -- REPORTED, asserted of nothing')
    check(f'Ⓑ③ at the PINNED trunk the mint is an ancestor and the row is not, which is the whole of '
          f'66\'s red -- and it is read at the pin BY CONSTRUCTION, because the merge that lands this '
          f'branch makes both ancestors and would make the clause vacuous (r7368 ②)',
          _mint_on and not _row_on)

    # ── Ⓒ the mechanism ───────────────────────────────────────────────────────────────────────────
    head('Ⓒ  the mechanism: the pass ran three commits early, inside the revision')
    _pass_rev = C.rev_of(C.PASS_C)
    _after = C.is_ancestor(C.PASS_C, C.MINT_C)
    print(f'      r7368\'s registration pass {C.PASS_C} ({_pass_rev}); the mint follows it: {_after}')
    check(f'Ⓒ① the mint and the registration pass that should have covered it are in the SAME '
          f'revision, with the pass first: {_pass_rev} {C.PASS_C} -> {_mrev} {C.MINT_C}',
          _pass_rev == 'r7368' and _mrev == 'r7368' and _after and C.PASS_C != C.MINT_C)

    check(f'Ⓒ② as a PROPERTY and not a count -- EVERY late row was minted after its own revision\'s '
          f'last pass, and there are {len(R["mech"])} of them: '
          f'{[(l, (p or "-")[:8], f) for l, _m, _r, p, f in R["mech"]]}',
          len(R['mech']) == 2 and all(f for *_x, f in R['mech']))

    _late_keys = sorted(lit for _rec, lit, _m, _mr, _s, _rr in R['late'])
    check(f'Ⓒ③ the LATE class is EXACTLY the two keys 66 named -- nothing else in the phase landed '
          f'behind its own mint -- and it is not vacuous, because {len(R["ontime"])} rows landed in '
          f'their own revision: {_late_keys}',
          _late_keys == sorted(C.NAMED) and len(R['ontime']) >= 40)

    # ── Ⓓ the arms ────────────────────────────────────────────────────────────────────────────────
    head('Ⓓ  the arms, against the bands registered before the scan')
    print(f'      ⒜ LATE {len(R["late"])} (central 7, band 2-21) '
          f'{C.score(len(R["late"]), 2, 21)}')
    print(f'      ⒝ EXPOSED {len(R["exposed"])} (central 2, band 2-14) '
          f'{C.score(len(R["exposed"]), 2, 14)}')
    print(f'      ⒞ EARLY {len(R["early"])} (exact 0)')
    print(f'      ⒟ window {R["d_rev"]} (central 2, band 1-6) {C.score(R["d_rev"], 1, 6)}; '
          f'{R["d_sum"]} on the summed reading')
    _early_prop = all(not (C.is_ancestor(_s, _m) and _s != _m)
                      for _rec, _lit, _m, _mr, _s, _rr in R['late'] + R['ontime'])
    check(f'Ⓓ① arm ⒞ as a PROPERTY over all {len(R["late"]) + len(R["ontime"])} split rows: no row\'s '
          f'commit strictly precedes the commit that minted its literal, which is why the exact 0 is '
          f'a mechanism and not a coincidence',
          _early_prop and len(R['early']) == 0)

    check(f'Ⓓ② arm ⒟ is asserted in DIRECTION ONLY and its figure is reported: the window is open in '
          f'at least one revision of the phase ({R["d_rev"]} commits over '
          f'{sum(1 for _r, (_p, a) in R["d_detail"].items() if a)} of {len(R["d_detail"])} '
          f'revisions), which is ABOVE the band registered for it and is this revision\'s one miss',
          R['d_rev'] >= 1 and C.score(R['d_rev'], 1, 6) == 'ABOVE')

    _p56, _a56 = R['d_detail'].get('r7356', ([], None))
    check(f'Ⓔ① the control revision CLOSED the window by registering MORE THAN ONCE -- r7356 has '
          f'{len(_p56)} passes and {len(_a56 or [])} receipt commits after the last, so the figure in '
          f'⒟ is a property of ONE pass per revision and not of this seat\'s hands',
          len(_p56) >= 3 and _a56 == [])

    # ── Ⓕ the remedy as a predicate, two-sided on pinned shas ─────────────────────────────────────
    head('Ⓕ  the remedy as a predicate, evaluated on two pinned shas')
    _at_defect = C.uncovered_named(C.R7368_TIP)
    _at_fix = C.uncovered_named(C.R7370_PASS)
    print(f'      at {C.R7368_TIP} (r7368\'s last commit):      uncovered {_at_defect}')
    print(f'      at {C.R7370_PASS} (the pass that wrote them): uncovered {_at_fix}')
    check(f'Ⓕ① the condition FIRES where the defect is and is SILENT where it was repaired -- both '
          f'keys uncovered at r7368\'s last commit, none at the pass: {_at_defect} then {_at_fix}',
          sorted(_at_defect or []) == sorted(C.NAMED) and _at_fix == [])

    # ── Ⓖ the detector is not copied here ─────────────────────────────────────────────────────────
    head('Ⓖ  the detector lives in the computation and is consumed, not restated')
    _pickaxe = "'-" + "S'"          # ⚠ spelled in two pieces: a literal here would match itself
    _spelled = re.search(r"^\s*(MINT_C|ROW_C|PASS_C|TRUNK|BASE|FRAME|R7368_TIP|R7370_PASS)\s*=",
                         _src, re.M)
    print(f'      this file binds a pinned sha of its own: {bool(_spelled)}')
    print(f'      this file contains a pickaxe call of its own: {_pickaxe in _src}')
    check(f'Ⓖ① every figure is READ from the revision\'s computation: this file calls measure() and '
          f'mint_of() and holds no pickaxe call of its own ({_pickaxe in _src})',
          'C.measure(' in _src and 'C.mint_of(' in _src and _pickaxe not in _src)

    check(f'Ⓖ② and the pinned shas are read from that module rather than re-spelled here, so there '
          f'is ONE place a pin can go stale -- asserted as a property of this file\'s source, not as '
          f'a promise in a comment: binds one itself = {bool(_spelled)}',
          _spelled is None and _src.count('C.MINT_C') >= 2)

    check(f'Ⓖ③ and this receipt is REGISTERED in the index, so the suite runs it and the ratchets '
          f'that caught the original red run over it too: {os.path.basename(__file__)[:12]}',
          os.path.basename(__file__) in open(INDEX, encoding='utf-8').read())

    print(f'\n{BAR}')
    if FAILED:
        print(f'  ⛔ {len(FAILED)} CHECK(S) FAILED')
        for x in FAILED:
            print(f'      - {x[:110]}')
        return 1
    print('  ✔ every check passed')
    print()
    print('  ⇒ THE KEYS WERE ADJUDICATED; THE TRUNK TOOK THE MINT A REVISION AHEAD OF THE ROW.  The')
    print('    gap opened three commits inside r7368, after that revision\'s own registration pass')
    print('    had already run -- so one pass per revision is not enough unless it is also LAST.')
    print(f'\n{BAR}\n')
    return 0


if __name__ == '__main__':
    sys.exit(main())
