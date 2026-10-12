#!/usr/bin/env python3
"""r7257+70.1, B1-B3: why a COMMITTED board cannot be kept current, demonstrated on `generate` itself.
Two branches each make progress on a claimed prefix and regenerate on their own history; after the merge the history
holds both.  MEASURED, and weaker than the pre-registration's wording: the merged expiry equals the LATER progress, so
only the branch with the EARLIER progress holds a stale copy -- the race reddens the old gate when the merge keeps
that side's file, not always.  The new gate generates from the merged state and has no copy to compare."""
import os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
import check_pin_board as B
bl = ('receipts/A/x.py\tl1\tT\tt\tf\tUNADJUDICATED\tw\nreceipts/A/x.py\tl2\tT\tt\tf\tUNADJUDICATED\tw\n'
      'receipts/A/y.py\tl3\tT\tt\tf\tUNADJUDICATED\tw\n')
claims = 'A\t60\tCLAIM\tr7200\n'
base = [(7200, {'A': 3}, {'A': 3})]
hist_a = base + [(7204, {'A': 3}, {'A': 2})]            # branch A lowers A at r7204
hist_b = base + [(7208, {'A': 3}, {'A': 2})]            # branch B lowers A at r7208
hist_m = base + [(7204, {'A': 3}, {'A': 2}), (7208, {'A': 3}, {'A': 2})]
board_a, board_b, board_m = (B.generate(bl, claims, h) for h in (hist_a, hist_b, hist_m))
print(f'B1 a committed copy from either branch is stale after the merge: {board_m != board_a} (A), {board_m != board_b} (B)')
_, void = B.live_claims(B.read_claims(claims + 'A\t70\tCLAIM\tr7202\n'), hist_m)
print(f'B2 the new gate compares no copy, so the race cannot redden it: True (by construction; no committed board)')
print(f'B3 a void double claim still fails: {len(void) == 1}')
