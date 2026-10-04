#!/usr/bin/env python3
"""check_unread_figure.py -- NO RECEIPT GAINS A FIGURE IT ATTRIBUTES TO A PAPER IT NEVER OPENS, AND THE OWED COUNT ONLY FALLS.

** A DRAFT BY NODE 70 (r7151+70.1) FOR NODE 66 TO REGISTER. **  *Written to run unchanged from `corpus/` beside
`unread_figure_baseline.tsv`, as `check_cannot_fail.py` does, and from this directory as it sits.  Not added to
`gates.yml`: registering a gate is the gate's call.*

** WHAT AN UNREAD-FIGURE SITE IS. **  A check whose LABEL attributes a quantity to a text -- "the paragraph's 3.32",
"P10's 0.61", "eq:rho-B" -- and whose VERDICT carries that quantity as a literal, in a receipt whose source never
reads a `.tex`.  *** Its subject is the paper and its measurement is its own arithmetic: when the paper moves the
figure, the receipt stays green against the old one, and no file-scoped gate reaches it because it names no file. ***
The routed instance is `P15_the_exact_transmission_ratios...` (`3.32`, r7145); r7147+70.1 found its repair still in
the class.

** THE MEASUREMENT IS 70's AND THIS GATE DOES NOT REIMPLEMENT IT. **  It runs `scripts/mutate_assertions.py
--unread-figure` (r7147+70.1) and compares against the baseline.  Three checks, as the other three ratchets:
  ⓵ ** NEW ** -- a `NO-READ` (receipt, label) key whose live count exceeds its baseline count.  *`READS-PAPER` sites
     are reported, NOT enforced (r7151): the partition the ratchet keys on is whether the receipt names the paper,
     which is exact; the drift partition failed its own control at 86.5 % and carries no priority.*
  ⓶ ** STALE ** -- a baseline key whose live count is below its baseline count.  Lower or remove the row.
  ⓷ ** THE OWED COUNT ** (`FIGURE` + `FORMULA` + `UNADJUDICATED`, `NO-READ` only) may only fall, against a ceiling
     declared HERE and nowhere else.

** THE KEY IS (receipt, label, READ) WITH A COUNT. **  *READ is in the key so a receipt that starts reading its
paper moves the site's row -- the repair shows as a STALE `NO-READ` row and a reported `READS-PAPER` one.*

  python3 check_unread_figure.py
  python3 check_unread_figure.py --list      # every owed key, complete and unfiltered

Drafted r7151+70.1.  Stated for reversal.
"""
import json
import os
import re
import subprocess
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = HERE
while not os.path.exists(os.path.join(ROOT, 'scripts', 'mutate_assertions.py')) and ROOT != os.path.dirname(ROOT):
    ROOT = os.path.dirname(ROOT)
BASELINE = os.path.join(HERE, 'unread_figure_baseline.tsv')
INSTRUMENT = os.path.join(ROOT, 'scripts', 'mutate_assertions.py')
LINE = re.compile(r'\s*\[UNREAD-FIGURE\]\[(NO-READ|READS-PAPER)\]\[[^\]]*\]\s+(\S+?):\d+:\d+\s+\{[^}]*\}\s+(".*")$')
#: verdicts the ratchet does NOT count as owed
NOT_OWED = {'NOT-A-PAPER-FIGURE', 'REPORTED'}
#: the partition whose NEW sites are reported and not enforced (r7151)
REPORTED_ONLY = {'READS-PAPER'}
# ⓷ the ratchet: the owed count measured on the tree this was drafted against (r7151+70.1, `origin/main` 79c1b03c):
#   60 NO-READ sites read, 22 FIGURE + 31 FORMULA owed, 7 NOT-A-PAPER-FIGURE.  Lowering it is the point.
# ⛭ r7153 (66): 53 → 50.  Node 70's draft measured the ceiling at 53 before the gate's own receipt
#   was repaired.  `P15_the_exact_transmission_ratios...` -- the site that ROUTED this whole class at
#   r7145 and which 70's `U2` predicted would still be in it -- now READS `CR_cosmology.tex` and
#   parses every figure it attributes, so its three NO-READ sites no longer exist and their rows are
#   gone rather than exempted.  ** It moved to READS-PAPER, which is the reported-not-enforced half,
#   and the three figures it still carries are its own: the closed form it derives from and the
#   midpoint it measures. **  ⌈ The ceiling is written from what the operator reads on THIS tree,
#   which is the instruction the gate gave 70 and owes itself.
# ⛭ r7159 (66): 50 → 48.  `P15_the_sky_phase_fit_and_its_uncertainty.py` now READS the paper, so its
#   two NO-READ sites no longer exist and their rows are gone rather than exempted.  ** It was a DRIFTED
#   site: it attributed a sigma on the phase to the paper, and the paper quotes none -- node 70 found it
#   at r7157+70.1 while reading the 19, and found why nothing caught it: the r7147 operator had filed it
#   IN-PAPER on a TOKEN match against the paper's unrelated `0.008 per cent`.  That is the 86.5 per cent
#   chance control observed on a live site, and it is why the drift partition was never gated. **
#   ⌈ The second DRIFTED site 70 found is `cc66`'s and is routed to its author, not repaired here.
# ⛭⛭ r7161 (66): 48 → 22, the largest single fall this ratchet has taken, and it is two seats'
#   repairs rather than a re-verdict.  ** cc66 took the 17 ANCHORED sites and node 70 the 19 FIGURE ones,
#   and between them 26 receipts now PARSE the figure out of their paper's own sentence instead of
#   carrying it. **  ⌈ The one site added in the same pass is a NEW member entered as OWED rather than
#   exempted -- a fourth site in a P10 receipt, exposed by 70's work on its siblings -- because the
#   ceiling only falls and a new member of the class is what this ratchet exists to count.
# ⛭ r7161+cc66.123: 22 → 18, the first of the DERIVATION block, and ** THREE REPAIRS RETIRED FOUR ROWS,
#   WHICH IS NOT THREE REPAIRS AND A BONUS. **  `P10_the_floor_is_forced...` had four NO-READ sites.
#   Three are genuinely repaired: the paper's `2(n-1)(n+3)`, `n(n+2)-2` and `n(n+2)` are now PARSED out
#   of `canonical_time.tex`'s own sentences by `paper_formula.inline`, each with a SUBSTITUTION CONTROL
#   that fails the check under `m = n` or `m = n+2` -- so the label tests the re-parameterisation it
#   claims and not a coincidence of two polynomials.  ⌈ And they LEFT the class rather than earning a
#   better verdict, exactly as the r7143 close found: a label reading "P10's degeneracy" has no literal
#   left to pin.
#   ⛔ ** THE FOURTH IS NOT A REPAIR AND IS RECORDED AS `READS-PAPER` WITH THAT SAID IN ITS ROW. **  Its
#   `15/4` is still carried; what changed is that the FILE now opens the paper, and this gate decides
#   READS-PAPER from the file's own source -- so one `open()` reclassified every site in the file.
#   *That is a property of the instrument, and the honest reading of the fall is 18 = 22 - 3 - 1, with
#   the 1 owed a read of its own rather than counted as done.*  ⌈ It is the same shape as the note at
#   r7157 that a repair almost made its own reads invisible here: this gate sees FILES, not sites.
# ⛭ r7161+cc66.124: 18 → 15, the second DERIVATION receipt, and ** THE SAME ARITHMETIC AS cc66.123:
#   THREE ROWS RETIRED FOR TWO REPAIRS, SO THE FALL IS 15 = 18 - 2 - 1. **  In
#   `P10_the_thermal_condition...` the Casimir eigenvalue and the per-family dimension are now read
#   from `canonical_time.tex`, each with a substitution control.  The third site (the floor's
#   self-dual/anti-self-dual FIVEs) still carries its own figures and is OWED a read; it changed
#   partition only because the file now opens the paper.
#   ⌗ ** AND THE PER-FAMILY DIMENSION IS DERIVED RATHER THAN QUOTED, BECAUSE THE READER REFUSED IT. **
#   `paper_formula.inline` rejected the pattern `(n-1)(n+3)`: both occurrences sit inside
#   `2(n-1)(n+3)`, so the paper states the TOTAL and never the half.  The receipt now asserts
#   `2 x (its per-family dimension) = the paper's parsed total`.  ⛔ *The first version of that reader
#   looked only at the character AFTER a match and returned this site as `kept=2, skipped=0` -- the
#   degeneracy without its factor of two, attributed to the paper, silently.  Caught by testing the
#   instrument against the NEXT site before using it there.  A boundary rule written on one side is
#   half a boundary rule.*
# ⛭ r7161+cc66.125: 15 → 13, and ** THIS TIME THE ARITHMETIC IS CLEAN: 13 = 15 - 2, two rows for two
#   repairs. **  `P10_the_degeneracy_needs_r_constant...` and `P10_the_descent_is_free...` each had
#   exactly ONE site, so the file-level reclassification that inflated cc66.123 and cc66.124 by one
#   apiece had nothing to inflate here.  ⌈ *That is the confirmation of the diagnosis rather than a
#   different outcome: the gate reads READS-PAPER off the FILE, so the inflation appears exactly when a
#   repaired file carries OTHER sites and never otherwise.*
#   ⌗ And two rows were removed while only one was added, because one site LEFT THE CLASS: with the
#   figure parsed, the label is an f-string and carries no literal for the instrument to see -- the
#   r7143 finding again, that a pin repaired properly leaves the class rather than earning a better
#   verdict.
#   ⛭ THE PRE-REGISTERED HAZARD FIRED ON A LIVE REPAIR.  The paper writes both `R=4\Lambda` and
#   `R=4\Lambda+\kappa\Theta`; `paper_formula.inline` skipped the extended match and reported the
#   skip, so the trace-coupled scalar is not read as a restatement of the vacuum one.  Both receipts
#   print the skip count in their own output.
# ⛭ r7161+cc66.128: 13 → 12, the LIMIT form, and the site LEFT THE CLASS -- one row removed and none
#   added, because with the paper's whole expression parsed both labels are f-strings and carry no
#   literal for the instrument to see.  ** `P10_the_vertex_numbers...` is the site cc66.123 named as
#   needing a different shape from the other eight: the paper prints
#   `K_{ij}K^{ij}-K^{2}=-6H^{2}+6(\dot\beta_{+}^{2}+\dot\beta_{-}^{2})` and `-6H^2` is its
#   ISOTROPIC LIMIT, so `inline` refused the bare pattern. **  The whole expression is read and the
#   limit is applied to the PARSED side as well as to the receipt's own, with a non-vacuity control
#   asserting the paper's expression is not already isotropic.  `-6H^2` is typed nowhere.
CEILING = 12


def read_baseline():
    rows = {}
    if not os.path.exists(BASELINE):
        return rows
    for ln in open(BASELINE, encoding='utf-8'):
        ln = ln.rstrip('\n')
        if not ln.strip() or ln.startswith('#'):
            continue
        p = ln.split('\t')
        if len(p) >= 5:
            rows[(p[0], json.loads(p[1]), p[2])] = (int(p[3]), p[4], p[5] if len(p) > 5 else '')
    return rows


def measure(files=None):
    r = subprocess.run([sys.executable, INSTRUMENT, '--unread-figure'] + (['--files'] + files if files else []),
                       cwd=ROOT, capture_output=True, text=True, timeout=600)
    live = Counter()
    for ln in r.stdout.splitlines():
        m = LINE.match(ln)
        if m:
            read, path, lab = m.groups()
            live[(path, json.loads(lab), read)] += 1
    return live


def main():
    print()
    print('  UNREAD-FIGURE RATCHET -- does any receipt gain a figure it attributes to a paper it never opens?')
    print()
    base = read_baseline()
    if not base:
        print(f'  ⛔ no baseline at {os.path.relpath(BASELINE, ROOT)} -- this gate has no record to ratchet.')
        return 1
    live = measure()
    print(f'    the instrument reports {sum(live.values())} site(s) under {len(live)} key(s); the baseline carries '
          f'{sum(n for n, _v, _w in base.values())} under {len(base)}')
    by_v = Counter()
    for (_p, _l, rd), (n, v, _w) in base.items():
        by_v[f'{rd}/{v}'] += n
    print(f'    by partition and verdict (sites): {dict(sorted(by_v.items()))}')
    owed = sum(n for (_p, _l, rd), (n, v, _w) in base.items() if rd == 'NO-READ' and v not in NOT_OWED)
    print(f'    OWED: {owed}   ** may only fall **   (not owed: {", ".join(sorted(NOT_OWED))})')

    if '--list' in sys.argv:
        print()
        for (p, l, rd), (n, v, _w) in sorted(base.items()):
            if rd == 'NO-READ' and v not in NOT_OWED:
                print(f'    [{v} x{n}] {p}\n               {json.dumps(l, ensure_ascii=False)}')
        return 0

    bad = 0
    new, reported = [], []
    for k, n in sorted(live.items()):
        had = base.get(k, (0, '', ''))[0]
        if n > had:
            (reported if k[2] in REPORTED_ONLY else new).append((k, n - had))
    if new:
        print()
        print(f'  ⛔ {len(new)} NEW UNREAD-FIGURE KEY(S) or count rise(s) -- a paper\'s figure asserted by a receipt '
              f'that never opens it:')
        for (p, l, rd), d in new[:40]:
            print(f'    [FAIL] +{d} {p}\n           {json.dumps(l, ensure_ascii=False)}')
        print('     ⌗ The label says the number is the PAPER\'s; nothing in the receipt reads the paper, so the check')
        print('       stays green when the paper moves.  Either READ the figure from the paper, or say in the label')
        print('       what THIS receipt computed and drop the attribution.  If it is not a paper\'s figure at all,')
        print('       record it in the baseline as NOT-A-PAPER-FIGURE with what was read.')
        bad += 1
    else:
        print('    no new NO-READ site: the class has not grown.')
    for (p, l, rd), d in reported:
        print(f'    [REPORTED, not enforced] +{d} {rd} {p}: {json.dumps(l, ensure_ascii=False)[:100]}')

    gone = []
    for k, (n, _v, _w) in sorted(base.items()):
        if live.get(k, 0) < n:
            gone.append((k, n - live.get(k, 0)))
    if gone:
        print()
        print(f'  ⛔ {len(gone)} STALE BASELINE ENTR(Y/IES) -- fewer live sites than recorded.  Lower or remove the row:')
        for (p, l, rd), d in gone[:40]:
            print(f'    [STALE] -{d} {rd} {p}\n            {json.dumps(l, ensure_ascii=False)}')
        bad += 1
    else:
        print('    no stale entry: every count still describes the tree.')

    if owed > CEILING:
        print()
        print(f'  ⛔ THE OWED COUNT ROSE: {owed} against the declared ceiling {CEILING}.')
        bad += 1
    else:
        print(f'    the ratchet holds: {owed} owed against a ceiling of {CEILING}')

    print()
    if bad:
        print('  ⛔ THE UNREAD-FIGURE RATCHET IS RED.')
        return 1
    print('  no receipt has gained an unread figure, every count describes the tree, and the owed count is held.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
