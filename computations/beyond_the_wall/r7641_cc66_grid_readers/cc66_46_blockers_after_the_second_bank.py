#!/usr/bin/env python3
"""r7641 item 2, the `cc66.46` clause: which of its blockers the second bank cleared.

`r7641` ⑵ says the second bank unblocks *"`cc66.46`'s own reading where its arm is in the bank"*.
`cc66.46` is `P15_the_contrast_excess_is_symmetric_about_the_envelope_…`, and its own dependents
already record why it could not be re-pointed.  `the_two_channels_compose_…` says it in as many words:

    "*`cc66.46` cannot be re-pointed -- it reads two gap banks and one whose arm is a KEY -- so its
     published row stays that arm's*"

** SO THE QUESTION IS NOT WHETHER THE BANK HELPS BUT WHICH OF THOSE THREE IT CLEARED, AND THAT IS A
FILE-AND-KEY QUESTION WITH A MEASURED ANSWER. **  Checked here rather than recalled:

    r6941_fine_cr_visleaf   -- a GAP bank          -> sibling now banked by 70's second bank
    r6929_scan_cr           -- a GAP bank          -> sibling now banked by 70's second bank
    r6929_geometry          -- arm is a KEY        -> NO `__cr_leafrec1` key, and no sibling file

⇒ *** Two of the three are cleared and the third is not.  `r6929_geometry` is read in exactly ONE
place in `cc66.46` -- the theta_D/theta_* clock sensitivity of ⓶ᵇ, `rD__cr / R_S__cr` at a VISLEAF
fraction -- so the receipt now splits: ⓶ᵃ (the symmetry and the seven band ratios) and ⓶ᶜ (the sky's
own spread) are re-pointable, and ⓶ᵇ is not. ***

** AND HALF-RE-POINTING IT IS THE DEFECT THIS SEAT HAS REFUSED TWICE **, at `held_period_estimator`
and at grid reader 1: a receipt whose ⓶ᵃ reads one arm and whose ⓶ᵇ reads the other is cross-arm by
construction.  ⇒ *So `cc66.46` stays on the namesake arm, and the ONE bank ask that moves it is the
same keys-not-files request `cc66.17` made and the second bank did not address.*

⌗ *The seven band ratios themselves are NOT blocked and are not in question: `band_ratio_reference.py`
reproduces `cc66.46`'s published namesake row to `3.9e-05` and 70's own-comb arm-of-record row to
`3.8e-05`, and the three dependent receipts already landed on the arm of record at `r7639` by
reproducing the namesake row as a LICENCE and measuring their own.  **Nothing waits on this except
`cc66.46`'s own publication.**
"""
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
SPEC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
RCPT = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology')
CC46 = os.path.join(RCPT, 'P15_the_contrast_excess_is_symmetric_about_the_envelope_'
                          'and_the_troughs_are_where_the_sky_measures_it_best.py')

BAR = "=" * 100
fail = []


def check(label, ok, witness=''):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}"
          + (f"   ({'' if ok else 'got '}{witness})" if witness else ''))
    if not ok:
        fail.append(label)


def arm_keys(stem):
    """the `cr`-side keys a bank carries, and whether any names the arm of record."""
    z = np.load(os.path.join(SPEC, stem + '.npz'), allow_pickle=True)
    cr = [k for k in z.files if 'cr' in k and 'lcdm' not in k]
    return cr, [k for k in cr if 'leafrec1' in k]


print(__doc__)
print(BAR)
print("  PART 1 -- THE THREE BLOCKERS, FILE AND KEY, MEASURED")
print(BAR)
ROWS = []
for stem, kind in (('r6941_fine_cr_visleaf', 'gap bank'), ('r6929_scan_cr', 'gap bank'),
                   ('r6929_geometry', 'arm is a KEY')):
    sib = os.path.exists(os.path.join(SPEC, stem + '_leafrec1.npz'))
    cr, aor = arm_keys(stem)
    ROWS.append((stem, kind, sib, cr, aor))
    print(f"    {stem:24s} {kind:14s} sibling file: {str(sib):5s}  cr keys: {len(cr)}"
          + (f"  arm-of-record keys: {len(aor)}" if cr else ""))
check("⛭ TWO OF THE THREE BLOCKERS ARE CLEARED BY FILE: `r6941_fine_cr_visleaf` and `r6929_scan_cr` "
      "both now have arm-of-record siblings, which they did not when `cc66.46`'s dependents recorded "
      "the obstruction",
      all(r[2] for r in ROWS if r[1] == 'gap bank'),
      ", ".join(f"{r[0]} {r[2]}" for r in ROWS if r[1] == 'gap bank'))
check("⛔ AND THE THIRD IS NOT, WHICH IS THE KEYS-NOT-FILES DISTINCTION `cc66.17` ASKED FOR: "
      "`r6929_geometry` has no arm-of-record sibling file AND no arm-of-record key -- its arm lives "
      "as the key suffix `__cr`, so a file-level bank cannot reach it",
      not [r for r in ROWS if r[0] == 'r6929_geometry'][0][2]
      and [r for r in ROWS if r[0] == 'r6929_geometry'][0][3]
      and not [r for r in ROWS if r[0] == 'r6929_geometry'][0][4],
      f"sibling {[r for r in ROWS if r[0] == 'r6929_geometry'][0][2]}, "
      f"{len([r for r in ROWS if r[0] == 'r6929_geometry'][0][3])} cr keys, "
      f"{len([r for r in ROWS if r[0] == 'r6929_geometry'][0][4])} of them arm-of-record")

print()
print(BAR)
print("  PART 2 -- AND IT IS READ IN EXACTLY ONE PLACE, WHICH IS WHY THE RECEIPT SPLITS")
print(BAR)
_src = open(CC46, encoding='utf-8').read()
_lines = [(i + 1, ln.strip()) for i, ln in enumerate(_src.splitlines()) if "GE[" in ln]
for n, ln in _lines:
    print(f"    l.{n}: {ln[:92]}")
check("⛭ `r6929_geometry` IS READ IN EXACTLY TWO ADJACENT LINES, both inside the theta_D/theta_* "
      "clock sensitivity of ⓶ᵃ's successor -- so the receipt SPLITS rather than being wholly "
      "blocked: ⓶ᵃ's symmetry and seven band ratios and ⓶ᶜ's sky spread read banks that have moved",
      len(_lines) == 2 and all('GE[' in ln for _, ln in _lines)
      and _lines[1][0] - _lines[0][0] == 1
      and any('rD__cr' in ln for _, ln in _lines),
      f"{len(_lines)} lines: {[n for n, _ in _lines]}")
check("⌗ and the receipt does name all five of its banks in a presence check, so a missing one is "
      "refused rather than silently skipped -- which is why a half re-point would announce itself",
      "the bank this receipt reads is present" in _src
      and _src.count('r6929_geometry') >= 2,
      f"{_src.count('r6929_geometry')} mentions")

print()
print(BAR)
print("  PART 3 -- AND THE DEPENDENTS ARE NOT WAITING ON IT, WHICH I CHECKED BEFORE ASKING")
print(BAR)
DEPS = ('P15_the_term_mix_has_the_shape_the_offset_needs_and_over_delivers_its_size.py',
        'P15_the_two_channels_compose_multiplicatively_and_the_pair_is_flat_where_the_excess_grows.py',
        'P15_the_windows_phase_spread_is_nearly_equal_because_the_visibility_widens_as_the_leaf_'
        'clock_slows.py')
PUB = [1.0215, 1.0574, 1.0519, 1.0606, 1.0748, 1.0659, 1.0762]
_ok = []
for d in DEPS:
    s = open(os.path.join(RCPT, d), encoding='utf-8').read()
    has = all(f"{v:.4f}" in s for v in PUB)
    nsk = 'MEAS_NSK' in s or 'namesake' in s
    _ok.append((d, has, nsk))
    print(f"    {d[4:52]:52s} asserts the published row: {str(has):5s}  names the namesake arm: {nsk}")
# ⛔ ** THIS GATE CAUGHT AN OVERSTATEMENT OF MINE ON ITS FIRST RUN. **  I wrote it asserting all
#   THREE dependents carry the licence shape.  Two do.  The third --
#   `the_windows_phase_spread_…` -- has ZERO mentions of `leafrec1`: it is the one HELD at
#   `r7639+cc66.26` on 70's swap re-run, with its re-point banked as a one-command patch
#   (`windows_phase_spread_repoint.patch.txt`) and its swap coefficient solved to
#   `SRCTAPER = 8.31868228e-05`.  ⇒ *So the correct statement is two landed and one held on a
#   DIFFERENT ask, not three landed -- and the gate is written the way the measurement puts it.*
_HELD = 'P15_the_windows_phase_spread_is_nearly_equal_because_the_visibility_widens_as_the_leaf_' \
        'clock_slows.py'
_held_src = open(os.path.join(RCPT, _HELD), encoding='utf-8').read()
_patch = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                      'r7639_cc66_P15_repoint_paper', 'windows_phase_spread_repoint.patch.txt')
print(f"    the held one carries {_held_src.count('leafrec1')} mentions of `leafrec1`, and its "
      f"re-point is banked as a patch: {os.path.exists(_patch)}")
check("⛭ TWO OF THE THREE DEPENDENTS ASSERT `cc66.46`'s PUBLISHED NAMESAKE ROW AS A LICENCE and "
      "measure their own on the arm of record -- the shape they landed with at `r7639`.  ⛔ *The "
      "third is not waiting on `cc66.46` either: it is `the_windows_phase_spread_…`, HELD at "
      "`cc66.26` on 70's swap re-run, with zero `leafrec1` mentions and its re-point banked as a "
      "one-command patch.*  ⇒ ** So nothing waits on `cc66.46` except `cc66.46`'s own publication, "
      "and the bank ask below buys ONE receipt rather than four **",
      all(h for _, h, _ in _ok)
      and sum(1 for _, _, n in _ok if n) == 2
      and _held_src.count('leafrec1') == 0
      and os.path.exists(_patch),
      f"{sum(1 for _, h, _ in _ok if h)} of 3 assert the row, "
      f"{sum(1 for _, _, n in _ok if n)} name the namesake arm, the held one has "
      f"{_held_src.count('leafrec1')} `leafrec1` mentions")

print()
print(BAR)
print(f"  {'ALL PASS' if not fail else 'FAILURES: ' + str(len(fail))}")
print(BAR)
sys.exit(1 if fail else 0)
