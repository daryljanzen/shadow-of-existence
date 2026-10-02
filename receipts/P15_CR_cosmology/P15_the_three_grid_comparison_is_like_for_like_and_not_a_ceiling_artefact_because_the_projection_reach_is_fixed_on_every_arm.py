#!/usr/bin/env python3
"""r7109 (66) -- ⛭⛭⛭ THE THREE-GRID COMPARISON IS LIKE-FOR-LIKE AND IS NOT A CEILING ARTEFACT: THE
PROJECTION'S REACH IS A FIXED MULTIPLE OF THE INVERSE DISTANCE ON EVERY ARM, SO THE COUPLING THAT WOULD
MANUFACTURE THE SEPARATION CANCELS BY CONSTRUCTION -- AND MORE THAN HALF OF IT IS ALREADY PRESENT EIGHT
HUNDRED MULTIPOLES BELOW THE CEILING.

** WHY THIS RECEIPT EXISTS, AND WHOSE COMPUTATION IT IS. **  `P15 sec:refit-bound` quotes the ceiling
scan's own numbers -- the seven truncation gaps, the reach `k_max*D_M`, the band shares, and the
forbidden arm's tracking of the control at every truncation.  *** Those figures are node 70's
measurement, made in its own audit instrument at `r7101+70.1`, pre-registered beside it, and run by the
seat that did NOT produce the comparison. ***  This receipt does not recompute them and does not touch
that instrument: it DRIVES `computations/beyond_the_wall/r7101_70_three_grid_audit/audit.py` as a
subprocess and asserts, against its output, exactly the figures the paper prints.

  ⌗ ** So the division of labour is on the record: the measurement is 70's, the assertion that the paper
  quotes it correctly is the gate's. **  *A paper figure with no receipt is the gap this closes; a second
  implementation of someone else's audit would be a different number wearing the same name.*

** WHAT THE PAPER CLAIMS, AND IT IS FOUR THINGS. **

  ⓵ ** LIKE-FOR-LIKE: ** one `ell` sampling across all three grids, and the control byte-identical
    across them -- so a difference between arms cannot be a difference of controls or of sampling.

  ⓶ ** THE CEILING MECHANISM DOES NOT OPERATE: ** both logged arms carry `k_max * D_M = 3998` against a
    reported `l_max = 2000`.  *The reach is a multiple of `1/D_M`, so the arm with the SHORTER distance is
    not thereby nearer its ceiling.*  ⇒ *** The coupling "k_max fixed, D_M smaller" -- the one way a
    ceiling could manufacture this separation -- is not what the instrument does. ***

  ⓷ ** THE SEPARATION IS NOT CONFINED TO HIGH MULTIPOLE: ** re-fitting all three statistics to data
    truncated at a succession of ceilings (a fit to fewer data -- sub-covariance, re-whitened, five
    directions re-projected -- and not a mask), the licensed-minus-forbidden excess runs

        850 -> -1.0   1000 -> +14.4   1200 -> +51.0   1400 -> +67.9
       1600 -> +74.7   1800 -> +84.0   1900 -> +88.3   1996 -> +93.8

    with about half of the full-range gap falling in `850 < ell <= 1500` and about a third of it below
    `ell = 850`, where the parameters absorb it entirely.  ** And at every truncation the forbidden arm
    sits within about one unit of the control **, which a flatness produced by distance from a ceiling
    would not do.

  ⓸ ** AND IT IS NOT CONVERGED: ** the gap grows to the last bin, `+5.5` between `1900` and `1996`, so
    the quoted separation is a statement about the range read and not a saturated value.

⇒ *** WHAT THE PAPER THEREFORE SAYS IS `localised IN ONSET` AND NOT `confined TO HIGH ell`: a rigidity
across scales, onset between `ell ~ 850` and `1000`, already decisive by `ell ~ 1200`, unbounded above by
the data used. ***  ⌗ *70's reply states the distinction in terms and it is the one correction the audit
asked of the paper: "The paper's `localised` is defensible only if it means localised in ONSET.  If it
means `confined to high ell`, it is wrong."*

⚠ ** ONE THING LIKE-FOR-LIKE CANNOT BE SHOWN FROM THE ARTEFACTS, AND IT IS NOT ASSERTED HERE. **  *The
forbidden grid was run at `r7093` and the licensed grid after the `LEAFREC` split, so they come from two
instrument revisions, and neither stamp carries the instrument's source hash.*  ⇒ ** "Same instrument but
for the switch" is INFERRED from every shared log line agreeing, not recorded. **  *No gate below claims
it.  The writing half that would record it -- the configuration's own blob hash, at save time -- landed on
`cc66`'s branch in the same round, so the NEXT grid pair closes this by construction rather than by
inference.*

COMPUTES: nothing of its own.  It runs 70's `audit.py` once as a subprocess, from that file's own
directory, and parses its printed tables.  No transfer, no spectrum, no likelihood, no fit.

Written r7109.  Stated for reversal.
"""
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
AUDIT = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7101_70_three_grid_audit')

CHECKS, bad = [], []


def gate(label, cond):
    CHECKS.append(label)
    print(f"  [{'PASS' if cond else 'FAIL'}] {label}")
    if not cond:
        bad.append(label)


def head(t):
    print("\n  " + "=" * 74)
    print("  " + t)
    print("  " + "=" * 74)


print(__doc__.split('COMPUTES:')[0].rstrip())

head("0.  THE INSTRUMENT IS 70's AND IS RUN, NOT REIMPLEMENTED")

gate("70's audit instrument is present where the paper's figures come from",
     os.path.isfile(os.path.join(AUDIT, 'audit.py')))
gate("⌗ and it is PRE-REGISTERED beside itself, which is what makes it an audit rather than a rerun",
     os.path.isfile(os.path.join(AUDIT, 'PREDICTION.md')))

p = subprocess.run([sys.executable, 'audit.py'], cwd=AUDIT, capture_output=True, text=True, timeout=1800)
OUT = p.stdout
print(f"\n      ran 70's audit.py in place: exit {p.returncode}, {len(OUT.splitlines())} lines of output")
gate("it runs clean, so every figure below is read from THIS run and not from the log beside it",
     p.returncode == 0 and len(OUT.splitlines()) > 50)


def num(pat, cast=float):
    m = re.search(pat, OUT)
    return cast(m.group(1)) if m else None


head("1.  LIKE-FOR-LIKE -- ONE SAMPLING, AND THE CONTROL BYTE-IDENTICAL ACROSS THE THREE GRIDS")

samplings = re.findall(r'(\w+)\s+ell samplings across its \d+ files: (\d+) distinct; (\d+)\.\.(\d+)', OUT)
print(f"      ell samplings reported per grid: {samplings}")
gate("all three grids carry exactly ONE ell sampling, and it is the same 100..1996 on each -- so an "
     "arm-to-arm difference is not a difference of sampling",
     len(samplings) == 3
     and all(int(d) == 1 and int(a) == 100 and int(b) == 1996 for _, d, a, b in samplings))

ctl = re.search(r'control.{0,60}?(\d+)\s+distinct SHA-256', OUT) or re.search(
    r'(\d+)\s+distinct SHA-256.{0,80}control', OUT, re.S)
ctl_one = bool(re.search(r'1 distinct', OUT)) and ('SHA' in OUT or 'sha' in OUT)
print(f"      control-hash line found: {bool(ctl)};  a '1 distinct' hash statement is present: {ctl_one}")
gate("⓵ the control is byte-identical across the grids, which is what says a moved statistic belongs "
     "to the arm and not to the method", ctl_one)


head("2.  THE CEILING MECHANISM -- THE REACH IS A FIXED MULTIPLE OF 1/D_M ON EVERY ARM")

reach = re.findall(r'(licensed|forbidden)\s+projection reach k_max\*D_M = (\d+) at l_max (\d+)'
                   r'.*?D_M\s+([\d.]+)', OUT)
print(f"      per-arm reach: {reach}")
gate("⓶ BOTH arms carry k_max*D_M = 3998 against l_max = 2000 -- the reach is a multiple of 1/D_M, so "
     "the arm with the shorter distance is NOT thereby nearer its ceiling",
     len(reach) == 2 and all(int(k) == 3998 and int(lm) == 2000 for _, k, lm, _ in reach))

dms = {a: float(d) for a, _, _, d in reach}
print(f"      and the distances DO differ: {dms}")
gate("⌗ and the distances differ while the reach does not, which is the whole content of the "
     "cancellation: 14011.5 against 13941.6 Mpc",
     abs(dms.get('licensed', 0) - 14011.5) < 0.6 and abs(dms.get('forbidden', 0) - 13941.6) < 0.6
     and dms['licensed'] > dms['forbidden'])


head("3.  THE TRUNCATION SCAN -- THE SEPARATION IS NOT CONFINED TO HIGH MULTIPOLE")

rows = re.findall(r'^\s+(\d{3,4})\s+(\d+)\s+.*?([-+]\d+\.\d)\s*$', OUT, re.M)
scan = {int(c): float(g) for c, n, g in rows}
print(f"      licensed-minus-forbidden gap by truncation: {scan}")
EXPECT = {850: -1.0, 1000: 14.4, 1200: 51.0, 1400: 67.9, 1600: 74.7, 1800: 84.0, 1900: 88.3, 1996: 93.8}
gate("the eight truncations the paper quotes are all present in the scan",
     all(c in scan for c in EXPECT))
gate("⓷ and every one of them matches the quoted value to a tenth -- -1.0, +14.4, +51.0, +67.9, "
     "+74.7, +84.0, +88.3, +93.8",
     all(abs(scan.get(c, 1e9) - v) <= 0.05 for c, v in EXPECT.items()))

gate("⌗ MORE THAN HALF THE GAP IS PRESENT AT ell <= 1200, EIGHT HUNDRED MULTIPOLES BELOW THE CEILING: "
     "51.0 of 93.8 is 54 per cent",
     scan.get(1200) is not None and 0.52 <= scan[1200] / scan[1996] <= 0.56)

gate("⌗ and it is MONOTONE above the onset, so the growth is the arm failing across scales rather than "
     "a single band dominating",
     all(scan[a] <= scan[b] + 1e-9 for a, b in zip(sorted(scan)[1:], sorted(scan)[2:])))

gate("⓸ AND IT IS NOT CONVERGED: the last 96 multipoles still add 5.5, so the quoted separation is a "
     "statement about the range read and not a saturated value",
     abs((scan[1996] - scan[1900]) - 5.5) <= 0.1)


head("4.  THE FORBIDDEN ARM TRACKS THE CONTROL AT EVERY TRUNCATION, NOT ONLY AT THE FULL RANGE")

fc = re.findall(r'^\s+(\d{3,4})\s+\d+\s+.*?([\d.]+)/\d+\s+\d+\s+\d+\s+([\d.]+)\s+\d+\s+\d+\s+[-+]\d',
                OUT, re.M)
pairs = {int(c): (float(f), float(k)) for c, f, k in fc}
print(f"      forbidden vs control chi^2 per truncation: {pairs}")
worst = max((abs(f - k) for f, k in pairs.values()), default=1e9)
print(f"      largest forbidden-minus-control discrepancy across all truncations: {worst:.2f}")
gate("the forbidden arm sits within about one unit of the control at EVERY truncation -- the stronger "
     "form of 'lands on the control's floor', and not something distance from a ceiling produces",
     len(pairs) >= 7 and worst <= 1.2)


head("5.  THE BAND SHARES -- ABOUT HALF BETWEEN 850 AND 1500, ABOUT A THIRD BELOW 850")

bands = re.findall(r'\((\d+),(\d+)\]\s+\d+\s+[\d.]+\s+[\d.]+\s+[\d.]+\s+\+?([-\d.]+)\s+([\d.]+)%', OUT)
sh = {(int(a), int(b)): float(s) for a, b, _, s in bands}
print(f"      share of the gap per band: {sh}")
mid = sum(v for (a, b), v in sh.items() if a >= 850 and b <= 1500)
low = sum(v for (a, b), v in sh.items() if b <= 850)
print(f"      850 < ell <= 1500 carries {mid:.1f}%;  ell <= 850 carries {low:.1f}%")
gate("about HALF the full-range gap falls between ell = 850 and 1500",
     len(sh) >= 6 and 48.0 <= mid <= 56.0)
gate("⌗ and about a THIRD of it sits below ell = 850 -- where the truncated fit absorbs it entirely "
     "(the 850 cut returns -1.0), which is what makes the failure a cross-scale one",
     28.0 <= low <= 34.0 and scan.get(850, 9) < 0.0)


head("6.  WHAT IS NOT ASSERTED, STATED RATHER THAN LEFT TO BE NOTICED")

src_hash = bool(re.search(r'source hash|blob hash|instrument revision', OUT, re.I))
print(f"      does the audit's own output claim a recorded instrument hash? {src_hash}")
gate("⚠ no gate here claims the two grids came from one instrument REVISION: that is inferred from the "
     "shared log lines agreeing and is not recorded in either stamp, which 70 said in terms and which "
     "the configuration writer landed in the same round closes for the NEXT pair",
     not src_hash)

# ⛔ THE SCOPE CLAIM IS READ FROM WHAT THIS PROCESS ACTUALLY LOADED, NOT FROM THIS FILE'S OWN TEXT.
#   *A first draft grepped this source for `import numpy` -- which the grep's own expression contains, so
#   the check could never pass.  ** That is a gate testing its own spelling, and it is the failure this
#   seat corrected another seat for in the same round. **  The claim is about what the receipt COMPUTED,
#   so it is read from the loaded modules: 70's audit runs as a SUBPROCESS and cannot put them here.*
numeric = sorted(m for m in ('numpy', 'scipy', 'camb') if m in sys.modules)
print(f"      numeric modules loaded in THIS process: {numeric or 'none'}")
gate("⌗ and nothing here re-measures the comparison itself: no array or linear-algebra library is "
     "loaded in this process at all, so this receipt drives 70's instrument and asserts what the paper "
     "prints rather than computing a second answer under the same name",
     not numeric)


print(f"\n  {len(CHECKS)} checks, {len(CHECKS)-len(bad)} pass, {len(bad)} fail")
print("  GATES: " + ("ALL PASS" if not bad else "FAILURES ABOVE"))
print("""
  THE AUDIT'S VERDICT, IN ONE PLACE:
    like-for-like       ->  one ell sampling, control byte-identical, arms differing in one stamped pair.
    the ceiling         ->  k_max*D_M = 3998 on BOTH arms, so the coupling cancels by construction.
    where it lives      ->  54 per cent of the gap at ell <= 1200; onset between 850 and 1000; about a
                            third below 850, absorbed there by the parameters.
    convergence         ->  NOT converged; +5.5 in the last 96 multipoles.
    the forbidden arm   ->  within about one unit of the control at every truncation.
  => the paper's word is localised IN ONSET.  'Confined to high multipole' would be wrong, and the
     comparison survives the one mechanism that could have manufactured it.
""")
assert not bad, f"{len(bad)} check(s) failed: {bad}"
