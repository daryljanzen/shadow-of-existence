#!/usr/bin/env python3
r"""P1 -- `L-249`: NINE PIN-BREAKS REPAIRED, AND THEY ARE ONE CLASS WITH ONE RULE.

** THE CLASS.  A receipt that pins a LIVE register -- a count, a membership, a quoted row -- fails
the moment the register moves.  And the register moves BECAUSE THE WORK SUCCEEDS. **

  ⇒ *** SO THE CHECK PUNISHES THE FINDING IT DEFENDS, and every one of these nine is that shape: ***

    `A3`   asserted "exactly 2 rows are ANSWERED".  A third was answered.  Its own question is
           *"has the unknown space NARROWED?"* -- ** the count going up IS its thesis arriving. **
    `A5`   asserted two dark halves live.  One closed.  ** Same. **
    `A7`   asserted a definedness-vs-prediction majority.  r3001 closed `PROTECTED_OPEN` ENTIRELY,
           so the live population is ZERO and `dn > pr` is `0 > 0`.
    `L805/S1` pinned a source saying its own object was **"reproduced nowhere"** -- and then
           reproduced it.  *** A receipt whose job is to close a gap, pinning a source that says
           the gap is open, breaks at the moment it does its job. ***
    `L811/S1` pinned five phrases of `kills/PO-7.md`; r2993 struck `PO-7` and rewrote the file.
           ** Its check guarded against the row being converted without authorisation -- and was
           overtaken by the row being properly closed, which is what the guard left room for. **
    `C1`   pinned *"a closure on a protected item is Daryl's"*.  ** r2826 rewrote it to "made in
           the register with a kill receipt" -- a POLICY CHANGE, closure moving from a PERSON to a
           MECHANISM. **  *A check that merely dropped the clause would have hidden that.*
    `B45`  pinned a sentence to `PO-7`'s ROW.  r2832b's cross-row dedup kept it on `PO-10`'s.
           ** The rule never left the register; only its address changed. **
    `N1`   pinned a guard in `BOARD.md`; r2832h pruned BOARD and the wording lives in the arc.
    `B59`  ** the appendix generator printing its own INDEX row into a file it greps ** -- diagnosed
           and gated at c54.232, in a span that was never absorbed, so the fix left the tree and the
           defect returned.  *** A FIX THAT IS NOT IN THE TREE IS NOT A FIX. ***

** ⌗ THE REPAIR, and it is the same one nine times. **  *Pin the historical state at the commit it
stood at; assert the CURRENT state separately; and where the finding is directional, make the live
check MONOTONE so it can still fail without failing on progress.*
  ⇒ ** `A3` now checks the count has not gone BACKWARDS and that no row un-answered itself -- which
    is strictly stronger than the number it replaced, and cannot be broken by the corpus improving. **

** ⚠ AND THE BOUNDARY THAT WAS KEPT: three of the twelve turn on P7 or P10 prose and are NOT touched
here. **  *The observer line has read both papers end to end and knows what the current text asserts;
re-pinning them from outside that reading would be guessing.*  ⌗ *`P15_the_locus_was_wrong` is not a
pin-break at all -- it fails because `check_loci` is red, which is a gate and not a quotation.*

Run:  python3 receipts/L249_a_pin_on_a_live_register/P1_...py

Written r3105 (`L-249`).  Stated for reversal.
"""
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
fails = []


def check(msg, ok):
    print(f"    {'OK  ' if ok else 'FAIL'}  {msg}")
    if not ok:
        fails.append(msg)


def run(rel):
    return subprocess.run([sys.executable, os.path.join(ROOT, 'receipts', rel)],
                          cwd=os.path.dirname(os.path.join(ROOT, 'receipts', rel)),
                          capture_output=True, text=True, timeout=600).returncode


REPAIRED = [
    ('P12_algebroid/A3_the_convergence_audit.py', 'a live ANSWERED count'),
    ('P12_algebroid/A5_the_dark_halves_audited.py', 'a live dark-half count'),
    ('P12_algebroid/A7_the_frontier_has_two_kinds.py', 'a ratio over an emptied population'),
    ('L805_freezing_reproduced/S1_every_mode_of_interest_freezes_and_the_inversion_is_closed.py',
     'a source saying its own object was unreproduced'),
    ('L811_po7_inversions_closed/S1_all_three_po7_inversion_routes_are_closed_by_computation.py',
     'five phrases of a kill file rewritten on the strike'),
    ('L221_quark_lepton/C1_the_rows_premises_are_stale_and_the_split_is_specified.py',
     'a closure-authority rule that changed'),
    ('L221_the_bridge/B45_the_object_exists_and_the_action_is_absent.py',
     'a sentence deduplicated onto another row'),
    ('L175_dimensional_descent/N1_the_cut_being_four_is_what_makes_the_dynamics_forced.py',
     'a guard pruned out of BOARD'),
    ('L221_the_bridge/B59_the_routes_are_enumerable_and_one_is_absent.py',
     'a receipt finding its own INDEX row in a generated appendix'),
]

print(__doc__)
print('=' * 78)
print('PART 1 -- THE NINE, RUN')
print('=' * 78)
for rel, why in REPAIRED:
    rc = run(rel)
    check(f'⓵ {os.path.basename(rel)[:44]:<44} exits 0  ({why})', rc == 0)

print()
print('=' * 78)
print('PART 2 -- ⛭⛭ THE REPAIR IS NOT A WEAKENING, AND THAT IS THE PART TO CHECK')
print('=' * 78)
print('  ** The cheap way to make a broken pin pass is to delete the assertion.  Every one of these')
print('     keeps the historical claim and ADDS a live one, so the check count goes UP. **')
for rel, _ in REPAIRED:
    src = open(os.path.join(ROOT, 'receipts', rel), encoding='utf-8', errors='replace').read()
    n_now = len(re.findall(r'\bcheck\(', src))
    add = subprocess.run(['git', 'log', '--diff-filter=A', '--format=%H', '--', 'receipts/' + rel],
                         cwd=ROOT, capture_output=True, text=True).stdout.strip().split('\n')[-1]
    old_src = subprocess.run(['git', 'show', f'HEAD:receipts/{rel}'], cwd=ROOT,
                             capture_output=True, text=True).stdout
    n_before = len(re.findall(r'\bcheck\(', old_src))
    print(f'    {os.path.basename(rel)[:46]:<46} checks {n_before} -> {n_now}')
    check(f'⓶ {os.path.basename(rel)[:40]:<40} did not lose assertions', n_now >= n_before)

print()
print('=' * 78)
print('PART 3 -- EVERY HISTORICAL PIN NAMES A COMMIT THAT IS REALLY AN ANCESTOR')
print('=' * 78)
print('  *A pin to a SHA is only a pin if the SHA is in this history; otherwise it is a decoration')
print('   that will fail on a fresh clone rather than here.*')
SHAS = set()
for rel, _ in REPAIRED:
    src = open(os.path.join(ROOT, 'receipts', rel), encoding='utf-8', errors='replace').read()
    SHAS |= set(re.findall(r"'([0-9a-f]{12,40})'", src))
print(f'    {len(SHAS)} distinct commit pin(s) across the nine')
for sha in sorted(SHAS):
    ok = subprocess.run(['git', 'merge-base', '--is-ancestor', sha, 'HEAD'],
                        cwd=ROOT, capture_output=True).returncode == 0
    check(f'⓷ {sha[:12]} is an ancestor of HEAD', ok)

print()
print('=' * 78)
print('PART 4 -- ⌷ THE BOUNDARY THAT WAS KEPT')
print('=' * 78)
HANDED_BACK = {
    'L204_physics_reach/P7_the_temperature_is_taken_and_the_entropy_never_is.py':
        ('CR_framework.tex', '5e30d0e9', 'r3059 — a false sentence written into P7 and caught'),
    'L204_physics_reach/P9_the_resolution_is_the_baby_universe_one_and_it_is_never_named.py':
        ('CR_framework.tex', '901d6be3', 'r3096 — P7 read word for word'),
}
for rel, (tex, sha, why) in HANDED_BACK.items():
    print(f'    {os.path.basename(rel)[:44]:<44} pins {tex}, removed at {sha} ({why})')
    prev = subprocess.run(['git', 'show', f'{sha}^:corpus/{tex}'], cwd=ROOT,
                          capture_output=True, text=True).stdout
    cur = open(os.path.join(ROOT, 'corpus', tex), encoding='utf-8', errors='replace').read()
    check(f'⓸ {os.path.basename(rel)[:38]:<38} turns on P7 prose that a P7 edit removed -- so it '
          'is the observer line\'s to re-pin, not this one\'s',
          len(prev) > 0 and len(cur) > 0 and prev != cur)
print()
print('  ⌗ ** AND ONE THAT IS NOT A PIN-BREAK AT ALL: ** `P15_the_locus_was_wrong_in_six_places`')
print('     fails on "check_loci does not pass on the repaired tree" -- a GATE dependency, not a')
print('     quotation.  *Classifying it with the pin-breaks would have sent someone to re-pin a')
print('     receipt whose problem is a red gate.*')
loci = subprocess.run([sys.executable, os.path.join(ROOT, 'corpus', 'check_loci.py')],
                      cwd=ROOT, capture_output=True, text=True).returncode
check('⓹ `check_loci` is indeed red, which is what that receipt is waiting on', loci != 0)

print()
print('=' * 78)
if fails:
    print(f'  {len(fails)} check(s) FAILED')
    for m in fails:
        print(f'    - {m}')
    sys.exit(1)
print('  ⇒ ** ALL CHECKS PASS. **')
print()
print('  ⛭⛭⛭ ** THE RULE, stated so it can outlive these nine: A CHECK THAT PINS A LIVE REGISTER IS')
print('     A CLAIM ABOUT A MOMENT.  Pin the moment at its commit; assert the present separately;')
print('     and where the finding has a direction, make the live check MONOTONE -- so it fails when')
print('     the corpus goes backwards and not when it goes forwards. **')
print()
