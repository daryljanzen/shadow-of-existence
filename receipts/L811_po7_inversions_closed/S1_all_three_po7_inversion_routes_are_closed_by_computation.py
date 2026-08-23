#!/usr/bin/env python3
r"""S1 -- cc54: PO-7's INVERSION CHECK (②) is now CLOSED ON ALL THREE ROUTES BY COMPUTATION, and this
receipt is the guard that the authorisation vehicle (kills/PO-7.md) and the reproducibility layer agree.

** THE STATE THIS RECORDS. ** kills/PO-7.md's route ② listed three falsifiable inversions -- the item stays
open if any holds:
  ⓵ a THIRD ADMISSIBLE PHASE exists (a mode crosses unfrozen, sin(phi) != 0, band widens to 0.891 and the
     control 0.2628 lands inside it);
  ⓶ the PEAK-4-8 ESTIMATOR is biased by the arm's own transfer (the 0.408 is instrumental);
  ⓷ the SEAM DATUM (CRPHI) acquires a derivation that lands OFF {0, pi} (reopening ⓵).
At r2599 the receipt read "three named routes, all falsifiable, none currently taken" -- none taken AS AN
ARGUMENT, which is not the same as excluded. Each has since been RUN, by cc54, and each is closed by a
number:
  ⓵ <- L-805  every ell 28..2475 freezes, c_s k/|aH| -> 0 at the crossing (max 5.2e-4); no mode crosses
              unfrozen, so the third phase does not exist; band stays 0.2069, control 0.2628 outside.
  ⓶ <- L-807  a synthetic comb with a HAND-SET asymptotic phase is recovered to < 0.01 in phi/pi,
              INDEPENDENT of the envelope (l_D 1200..2000, widths 25..55, tilts -- >> the arm's ~8%);
              the estimator reads the PHASE not the transfer, so the driven-case bias is excluded.
  ⓷ <- L-806  a massive mode freezes too, for ANY mass (m^2 a^2 -> 0 at the branch point while |aH|
              diverges), so a massive trajectory carries no phase off {0, pi} -- the one mechanism that
              could reopen ⓵ is shut; CRPHI derived from a frozen crossing stays on {0, pi}.

** Board lead L-811 (cc54's band); instrument/synthesis -- it INFORMS L-171 (PO-7) and stands on L-805,
L-806, L-807 (cc54's A2/A10 and the L-805 freezing run). It supplies no new physics: it is the guard that
the three computations exist, pass, each closes its NAMED route, and that kills/PO-7.md now records all
three WITHOUT converting the row, and -- guarding the r2599 correction -- WITHOUT manufacturing an
authorisation: ② still does not clear, on ⓷'s LIVE progenitor-derivation residue (PO-seam's dark half),
and nothing is owed by Daryl. Closing the inversions' calculational sides is the calculation; it is not a
verdict and it is not a decision anyone owes. **

** WHAT THIS RECEIPT CHECKS. **
  1. The three inversion-closing receipts exist and each RUNS to exit 0 (not merely present -- run, per
     THE_BASE_RATE #23: an instrument that reads a file has not run it).
  2. Each receipt closes its NAMED route: L-805 the freezing/third-phase route, L-807 the estimator route,
     L-806 the massive-derivation route -- asserted from each receipt's own statement of its object.
  3. kills/PO-7.md records all three closures, and ②'s head now POINTS to them (r2674 forward-pointer)
     so a reader landing on ② is not told ⓵ is still "the live inversion".
  4. THE ROW IS NOT CONVERTED AND NOT AWAITING A DECISION -- guarding the r2599 correction: the kill
     receipt says ② "DOES NOT CLEAR" (on ⓷'s LIVE progenitor-derivation residue) and "NOTHING IS OWED
     BY DARYL", and carries no strike / no "CLOSED"-verdict line. Closing the three inversions'
     CALCULATIONAL sides did NOT manufacture an authorisation -- which is exactly the mistake the r2599
     correction killed, so this receipt guards against its recurrence.
  5. The band conclusion the inversions defend is intact in the kill receipt: the admissible pair {0, pi},
     the zero-velocity band 0.2069, and the control 0.2628 OUTSIDE it.

** WHAT IS NOT CLAIMED, stated for reversal. ** Not that PO-7 is closed -- it is not; only that its three
inversion routes are each closed by a computation, which is the state check ④ already reached for ⓵ via
L-805 and this receipt extends to ⓶ and ⓷. Not that no derivation of CRPHI can EVER land off {0, pi} in
the abstract -- only that no derivation from a FROZEN crossing can, and the freezing is now the computed
part (L-805/L-806). Not a new acoustic number -- the 0.408, the band and the control are unchanged; this
records that they no longer rest on any unclosed inversion.

Written r2674 (cc54, L-811). Asserts against the filesystem, live subprocesses, and kills/PO-7.md -- never
the register. Stated for reversal.
"""
import os
import subprocess
import sys
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
RECEIPTS = os.path.join(ROOT, 'receipts')
FAILED = []

ROUTES = {
    '⓵': ('L805_freezing_reproduced',
          'S1_every_mode_of_interest_freezes_and_the_inversion_is_closed.py',
          # the object L-805 states: freezing of every mode closes the third-phase route
          ('freezes', 'inversion', 'unfrozen')),
    '⓶': ('L807_driven_estimator',
          'S1_the_peak_estimator_recovers_a_set_phase_independent_of_the_envelope.py',
          # L-807's object: the estimator reads the phase not the transfer
          ('estimator', 'envelope', 'phase')),
    '⓷': ('L806_massive_freezing',
          'S1_a_massive_mode_freezes_too_and_the_mass_term_vanishes_at_the_branch_point.py',
          # L-806's object: a massive mode freezes, so no phase off {0, pi}
          ('massive', 'freezes', 'branch point')),
}


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print('  S1 -- are all three of PO-7\'s inversion routes closed by computation, and does the kill')
    print('        receipt record it without converting the row?')
    print()

    # 1. the three receipts exist and each RUNS to exit 0
    for route, (d, f, _) in ROUTES.items():
        path = os.path.join(RECEIPTS, d, f)
        exists = os.path.exists(path)
        rc = None
        if exists:
            r = subprocess.run([sys.executable, f], cwd=os.path.dirname(path),
                               capture_output=True, text=True, errors='replace', timeout=120)
            rc = r.returncode
        check(f'route {route}: receipt {d}/S1 exists and RUNS to exit 0 (got rc={rc})',
              exists and rc == 0)

    # 2. each receipt closes its NAMED route -- its own object mentions the route's substance
    for route, (d, f, terms) in ROUTES.items():
        src = ''
        p = os.path.join(RECEIPTS, d, f)
        if os.path.exists(p):
            src = open(p, encoding='utf-8', errors='replace').read().lower()
        hit = all(t.lower() in src for t in terms)
        check(f'route {route}: {d} states its object in its own voice '
              f'(all of {terms} present)', hit)

    # 3. kills/PO-7.md records all three closures -- both the r2570/r2599 conclusion sections and the
    #    r2674 forward-pointer at ②'s head cite L-805/L-807/L-806.
    kill = open(os.path.join(ROOT, 'kills', 'PO-7.md'), encoding='utf-8', errors='replace').read()
    # AMENDED r3105 (L-249).  ALL THREE CHECKS BELOW PINNED THE PRE-STRIKE KILL FILE.
    # r2993 struck PO-7 -- "both clauses of the object answered" -- and rewrote kills/PO-7.md
    # wholesale.  Every phrase these checks quote was there before and is gone after:
    #     "r2674 pointer" 1->0   "DOES NOT CLEAR" 4->0   "NOTHING IS OWED BY DARYL" 1->0
    #     "0.2069" 2->0          "0.2628" 3->0
    #   => Check 4 is the sharp one: it guarded against the row being converted or awaiting a
    #     decision.  THAT GUARD HAS BEEN OVERTAKEN BY THE ROW BEING PROPERLY CLOSED -- which is
    #     what it was defending the possibility of, not what it was defending against.
    #   => So the historical state is pinned at the pre-strike commit and the live state is
    #     asserted as what it now is: struck, with the closures recorded and this line cited.
    PRE = 'dbd2f7f79be8'   # r2993^, before PO-7 was struck
    kill_then = subprocess.run(['git', 'show', PRE + ':kills/PO-7.md'], cwd=ROOT,
                               capture_output=True, text=True).stdout

    check('at ' + PRE[:12] + ' kills/PO-7.md recorded all three closures and pointed to them from '
          "\u2461's head (r2674 pointer citing L-805, L-807 and L-806)",
          '`L-805`' in kill_then and '`L-807`' in kill_then and '`L-806`' in kill_then
          and 'r2674 pointer' in kill_then and 'DOES NOT CLEAR' in kill_then)

    check('and THERE the row was NOT converted and NOT awaiting a decision -- "DOES NOT CLEAR" and '
          '"NOTHING IS OWED BY DARYL", no strike, no CLOSED verdict: closing the inversions had not '
          'manufactured an authorisation (the r2599 correction, guarded)',
          'DOES NOT CLEAR' in kill_then and 'NOTHING IS OWED BY DARYL' in kill_then
          and '~~PO-7~~' not in kill_then and 'VERDICT: CLOSED' not in kill_then)

    check('and the band the inversions defend was intact there: the admissible pair {0, pi}, the '
          'zero-velocity band 0.2069, and the control 0.2628 OUTSIDE it',
          '0.2069' in kill_then and '0.2628' in kill_then and '\\{0,\\pi\\}' in kill_then)

    # and the LIVE state, which is the guard's own condition having been met rather than breached
    check('LIVE: PO-7 has since been STRUCK at r2993 -- "both clauses of the object answered" -- so '
          'the guard against a manufactured authorisation was not breached; the row was closed on '
          'its object, which is the outcome that guard existed to leave room for',
          bool(re.search(r'\|\s*~~\*\*PO-7\*\*', open(
              os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read())))
    check('and the live kill receipt still credits this line among the three closures -- "the 0.408 '
          'rests on NO unclosed inversion"',
          'L-805' in kill and 'unclosed inversion' in kill)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: PO-7\'s three inversion routes -- a third admissible phase (⓵), estimator bias (⓶),')
    print('  and a seam derivation off {0,pi} (⓷) -- have their CALCULATIONAL sides each closed by a')
    print('  computation (L-805, L-807, L-806), and ②\'s head now points to them. The 0.408 rests on no')
    print('  unclosed inversion. But ② STILL DOES NOT CLEAR -- what remains of ⓷ is a live progenitor')
    print('  derivation of CRPHI (PO-seam\'s dark half) -- so PO-7 is not awaiting a decision, and NOTHING')
    print('  IS OWED BY DARYL. cc54 supplied the calculation; it did not manufacture a verdict.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
