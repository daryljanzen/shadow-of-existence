#!/usr/bin/env python3
"""check_receipt_exit.py -- A CITED RECEIPT MUST BE ABLE TO EXIT NON-ZERO.

** WHY, and it is a gap inside an existing gate rather than a new class. **  `check_receipt_asserts`
(r2384) tests whether a receipt has a path on which it ** could fail **, and accepts a `FAIL` token, a
`PASS` token or an `np.allclose` as evidence.  *** But the c54.161 campaign's own repair note names the
shape those miss: "the checks above compute a PASS/FAIL boolean and ONLY PRINT IT." ***

  ⇒ ** A receipt that prints `[FAIL]` and returns 0 is green in every runner. **  Its `rc=0` is what a
    caller reads, and the printed verdict is what nobody reads.

** THE MEASUREMENT, r2681. **  Of 462 receipts, ** 12 carry no `assert` and no `check()` at all ** -- and
*** all twelve are CITED IN THE PAPERS, 38 citations in total: ***

      *** P15_expansion_law 4x · BRANCHPT_transmission_character 4x
          P16_the_scalar_monodromy_is_four_pi_over_rho 4x · nine more at 3x each ***

  ⌗ ** So thirty-eight sentences in print rest on a receipt that proves only that Python exited zero. **

** WHAT THIS CHECKS. **  Every receipt cited in a paper must contain at least one construct that can
change its EXIT CODE: `assert`, `raise`, `sys.exit(1)`, or `return 1`.

  ⚠ ** A token is not enough and that is the whole point ** -- *** `FAIL`, `PASS` and `allclose` are
      accepted by `check_receipt_asserts` and are exactly what these twelve have. ***
  ⌗ ** Uncited receipts are exempt: ** a working script that nothing rests on is a script, and the
    campaign that repairs it should be aimed at the cited ones first.

    python3 corpus/check_receipt_exit.py

Written r2681.  Stated for reversal.
"""
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

CAN_EXIT = re.compile(r'^\s*assert\b|^\s*raise\b|sys\.exit\s*\(\s*1|return\s+1\b', re.M)

# ** the twelve found at r2681, recorded so the gate ships GREEN and the backlog is visible
# rather than blocking every run.  *** A gate that fails for a known backlog trains its caller
# to skip it -- cc54's own words at c54.208. ***  Each leaves this set when it is repaired.
BACKLOG = {
    'P15_the_progenitor_vacuum_is_negligible_too.py', 'P15_the_second_arm_actually_run.py',
    'AS_amplitude_leftward.py', 'P15_verify_closedS3_nonsync.py', 'P15_confront_lowell_data.py',
    'P15_expansion_law.py', 'BRANCHPT_transmission_character.py',
    'P15_no_primordial_B_modes_unconditionally.py',
    'P16_the_scalar_monodromy_is_four_pi_over_rho.py',
    'P16_the_passage_is_phase_only_above_the_first_peak.py',
    'P16_the_progenitor_composition_is_bracketed.py',
    'P16_the_leading_order_interior_is_adequate.py',
}


def body(f):
    return '\n'.join(l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
                     if not l.lstrip().startswith('%'))


def main():
    print()
    print('  check_receipt_exit -- can every cited receipt exit non-zero?')
    print()
    papers = ' '.join(body(f) for f in glob.glob(os.path.join(ROOT, 'corpus', '*.tex')))
    bad, backlog, n = [], [], 0
    for f in sorted(glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True)):
        stem = os.path.basename(f)[:-3]
        if stem not in papers:
            continue
        n += 1
        if CAN_EXIT.search(open(f, encoding='utf-8', errors='replace').read()):
            continue
        (backlog if os.path.basename(f) in BACKLOG else bad).append(os.path.basename(f))

    print(f'  {n} cited receipts checked')
    if backlog:
        print(f'  {len(backlog)} in the KNOWN BACKLOG (r2681), listed not failed:')
        for b in sorted(backlog):
            print(f'    ⌗ {b}')
    if bad:
        print()
        for b in bad:
            print(f'    [FAIL] {b} is cited and cannot exit non-zero')
        print()
        print('    ⛔ ** A RECEIPT THAT PRINTS `[FAIL]` AND RETURNS 0 IS GREEN IN EVERY RUNNER. **')
        print('       *** Its rc=0 is what a caller reads; the printed verdict is what nobody reads.')
        print('       Add an `assert` on the claim the citing sentence makes. ***')
        return 1
    print('  no NEW cited receipt is print-only.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
