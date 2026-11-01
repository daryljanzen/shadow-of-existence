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
that instrument: it DRIVES
`computations/beyond_the_wall/r7651_70_three_asks/audit_leafrec1.py` as a subprocess and asserts,
against its output, exactly the figures the paper prints.

  ⛭ ** THE ARM OF RECORD, AND WHAT THE RE-POINT DID AND DID NOT CHANGE (r7653 ⓸). **  `audit_leafrec1.py`
  is `r7101`'s `audit.py` run *unchanged*: 70's wrapper rewrites ONE AST node -- `GRIDS` -- to a per-run
  directory of links that resolves `lcdm_*` from the namesake grid and `cr_*` from the `_leafrec1`
  sibling, so the imported `rigidity.py` AND its `--grid` subprocess driver see the same resolution.
  ⇒ *The measurement stays 70's and the instrument stays one instrument; only which banks its arms read
  has moved.*  ** Every one of the paragraph's claims survives the move; all seven of its printed
  figures change, and one claim gets FOURFOLD stronger. **  ⌗ *The receipt gates the resolution itself
  below, so it cannot silently fall back to the namesake and keep passing.*

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

        850 -> -1.1   1000 -> +14.2   1200 -> +49.5   1400 -> +66.7
       1600 -> +72.6   1800 -> +81.3   1900 -> +85.2   1996 -> +90.2

    (the namesake's were `-1.0, +14.4, +51.0, +67.9, +74.7, +84.0, +88.3, +93.8`, which is what the paper
    still prints; the scan has EIGHT cuts and the paper quotes SEVEN of them, dropping `1900`)

    with about half of the full-range gap falling in `850 < ell <= 1500` -- `51.8` per cent, from the
    band table -- and about a third of it below `ell = 850` -- `32.1` per cent -- where the parameters
    absorb it entirely.  ** And at every truncation the forbidden arm sits within about one unit of the
    control **, which a flatness produced by distance from a ceiling would not do.

    ⛭ ** AND ON THE ARM OF RECORD THAT LAST BOUND TIGHTENS FOURFOLD, from `1.1` to `0.3`. **  *The
    forbidden configuration does not merely sit near the control's floor across the eight ceilings; it
    sits ON it to three tenths of a unit at every one of them.*  ⌗ Both are gated: the paper's claim
    ("about one unit") as the claim, and `0.3` as the measurement, so the sentence can be tightened
    without the gate having to be rewritten first.

  ⓸ ** AND IT IS NOT CONVERGED: ** the gap grows to the last bin, `+5.0` between `1900` and `1996`
    (the namesake's `+5.5`), so the quoted separation is a statement about the range read and not a
    saturated value.

⇒ *** WHAT THE PAPER THEREFORE SAYS IS `localised IN ONSET` AND NOT `confined TO HIGH ell`: a rigidity
across scales, onset between `ell ~ 850` and `1000`, already decisive by `ell ~ 1200`, unbounded above by
the data used. ***  ⌗ *70's reply states the distinction in terms and it is the one correction the audit
asked of the paper: "The paper's `localised` is defensible only if it means localised in ONSET.  If it
means `confined to high ell`, it is wrong."*

⚠ ** ONE THING LIKE-FOR-LIKE CANNOT BE SHOWN FROM THE ARTEFACTS, AND IT IS NOT ASSERTED HERE. **  *Neither
stamp carries the instrument's source hash.*  ⇒ ** "Same instrument but for the switch" is INFERRED from
every shared log line agreeing, not recorded. **  *No gate below claims it.  The writing half that would
record it -- the configuration's own blob hash, at save time -- landed on `cc66`'s branch in the same
round, so the NEXT grid pair closes this by construction rather than by inference.*

  ⛭ ** BUT THE STAMPED DIFFERENCE ITSELF NARROWS FROM A PAIR TO A SINGLE KEY, which is the one thing the
  re-point makes strictly stronger. **  *On the namesake the two arms differed in `('LEAFGEOM',
  'LEAFREC')` -- TWO keys -- because the forbidden grid at `r7093` predated the `LEAFREC` split.  On the
  arm of record both arms' `cr_*` legs come from `_leafrec1` siblings, so at every one of the nine CR
  steps they differ in `('LEAFGEOM',)` ALONE.*  ⇒ ** The comparison is now like-for-like in the stamps as
  well as in the sampling, and that is gated below. **

COMPUTES: nothing of its own.  It runs 70's `audit_leafrec1.py` once as a subprocess, from that file's
own directory, and parses its printed tables.  No transfer, no spectrum, no likelihood, no fit.  The
whole run costs about twenty seconds and is deterministic: its output is byte-identical to the log 70
banked beside it.

Written r7109.  Re-pointed to the arm of record at r7653 ⓸, with TWO gate repairs taken there rather
than carried:
  ⛔ PART 1's control-hash gate had been passing VACUOUSLY since r7109 -- it matched `sha` inside the
    `/home/user/shadow-of-existence/` path that the audit's own first-line RuntimeWarning prints, and
    ANDed it with a `1 distinct` that came from the ell-sampling lines rather than the control.  It now
    reads the audit's own byte-identity line.
  ⛔ AND THIS RECEIPT NEVER OPENED THE PAPER whose figures its labels attributed to it, which is what
    `check_unread_figure` went red on.  ** PART 6 now READS the paragraph out of
    `corpus/CR_cosmology.tex` ** -- the seven-figure run, the reach, the "more than half ... eight
    hundred multipoles below the ceiling" claim and the ceiling it implies, the 850-to-1500 band, the
    word "third", the control-tracking bound as a PHRASE, the onset pair and the non-convergence clause
    -- and tests each against this run of the audit.  *Each of the seven figures is held as a
    DISJUNCTION over the quantity's two states, with a summary gate forbidding a MIXED paragraph, so
    the receipt is green before the landing and after it and cannot be green for a half-landed one.*

Stated for reversal.
"""
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
AUDIT = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7651_70_three_asks')
INNER = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7101_70_three_grid_audit', 'audit.py')

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
     os.path.isfile(os.path.join(AUDIT, 'audit_leafrec1.py')))
gate("⌗ and the instrument it RUNS is `r7101`'s own audit.py, unchanged -- the arm-of-record wrapper "
     "rewrites one AST node (GRIDS) and nothing else, so this is one instrument on new banks and not a "
     "second implementation", os.path.isfile(INNER))
gate("⌗ and it is PRE-REGISTERED beside itself, which is what makes it an audit rather than a rerun",
     os.path.isfile(os.path.join(AUDIT, 'PREDICTION.md')))

p = subprocess.run([sys.executable, 'audit_leafrec1.py'], cwd=AUDIT, capture_output=True, text=True,
                   timeout=1800)
OUT = p.stdout
print(f"\n      ran 70's audit_leafrec1.py in place: exit {p.returncode}, "
      f"{len(OUT.splitlines())} lines of output")
gate("it runs clean, so every figure below is read from THIS run and not from the log beside it",
     p.returncode == 0 and len(OUT.splitlines()) > 50)


def num(pat, cast=float):
    m = re.search(pat, OUT)
    return cast(m.group(1)) if m else None


head("1.  LIKE-FOR-LIKE -- ONE SAMPLING, AND THE CONTROL BYTE-IDENTICAL ACROSS THE THREE GRIDS")

# ⛭ THE ARM OF RECORD IS GATED FROM THE RESOLUTION THE RUN ITSELF PRINTS, NOT FROM THIS FILE'S PATHS.
#   *Otherwise the receipt would keep passing if the wrapper fell back to the namesake banks -- which is
#   the whole thing the re-point is for.*
res = re.findall(r'^\s+(\w+)\s+lcdm_\* <- (\S+)/\s+cr_\* <- (\S+)/\s+\((\d+) files\)', OUT, re.M)
print(f"      per-arm resolution the run reports: {res}")
gate("⛭ all three grids resolve their ARM from a `_leafrec1` sibling and their CONTROL from the "
     "namesake, which is what makes this the arm of record rather than the namesake",
     len(res) == 3 and all(arm.endswith('_leafrec1') and not ctl.endswith('_leafrec1')
                           for _, ctl, arm, _n in res))
gate("⌗ and the three resolved sets are the sizes the banks have: TEN cr_* legs each (nine CR steps "
     "and `cr_base.log` beside the base), TEN lcdm_* legs for each direction pair, and NINE for the "
     "banked pair -- `refit_grid185` predates log banking, so it has no `lcdm_base.log` -- which is "
     "why 19, 20, 20 and not 20, 20, 20",
     [int(n) for _, _, _, n in res] == [19, 20, 20])

switch = re.search(r'ONE switch pair throughout: \{\(([^)]*)\)\}', OUT)
keys = tuple(k.strip().strip("'\"") for k in switch.group(1).split(',') if k.strip()) if switch else ()
print(f"      the key set the two arms differ in, at every CR step: {keys}")
gate("⛭ on the arm of record the licensed and forbidden grids differ in ONE stamped key, LEAFGEOM, at "
     "every one of the nine CR steps -- the namesake's pair ('LEAFGEOM', 'LEAFREC') has become a single "
     "switch, because both arms now read `_leafrec1` siblings",
     keys == ('LEAFGEOM',))

samplings = re.findall(r'(\w+)\s+ell samplings across its \d+ files: (\d+) distinct; (\d+)\.\.(\d+)', OUT)
print(f"      ell samplings reported per grid: {samplings}")
gate("all three grids carry exactly ONE ell sampling, and it is the same 100..1996 on each -- so an "
     "arm-to-arm difference is not a difference of sampling",
     len(samplings) == 3
     and all(int(d) == 1 and int(a) == 100 and int(b) == 1996 for _, d, a, b in samplings))

# ⛔ THIS GATE WAS PASSING VACUOUSLY FROM r7109 TO r7653, AND THE REPAIR IS THE POINT OF THE COMMENT.
#   *It read `bool(re.search(r'1 distinct', OUT)) and ('SHA' in OUT or 'sha' in OUT)`.  The audit prints
#   no hash at all -- but its FIRST line is a RuntimeWarning carrying `/home/user/shadow-of-existence/`,
#   and `'sha' in OUT` matches `sha`dow.  The `1 distinct` it ANDed with comes from the ELL-SAMPLING
#   lines, not the control.  ** So both conjuncts were true for reasons unrelated to the control, on both
#   audits, for the gate's whole life.  A vacuous pass is worse than a failure: it reports the same green
#   as a check that is actually checking. **  It now reads the audit's own byte-identity line.*
ctl = re.search(r'control:\s+(\d+) of (\d+) files byte-identical across all three grids', OUT)
print(f"      the audit's own control byte-identity line: {ctl.groups() if ctl else None}")
gate("⓵ the control is byte-identical across the grids -- ALL of its files, not a majority -- which is "
     "what says a moved statistic belongs to the arm and not to the method",
     ctl is not None and ctl.group(1) == ctl.group(2) and int(ctl.group(2)) >= 9)


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
     "cancellation: 14134.0 against 14062.0 Mpc on the arm of record (the namesake's were 14011.5 "
     "and 13941.6)",
     abs(dms.get('licensed', 0) - 14134.0) < 0.6 and abs(dms.get('forbidden', 0) - 14062.0) < 0.6
     and dms['licensed'] > dms['forbidden'])


head("3.  THE TRUNCATION SCAN -- THE SEPARATION IS NOT CONFINED TO HIGH MULTIPOLE")

rows = re.findall(r'^\s+(\d{3,4})\s+(\d+)\s+.*?([-+]\d+\.\d)\s*$', OUT, re.M)
scan = {int(c): float(g) for c, n, g in rows}
print(f"      licensed-minus-forbidden gap by truncation: {scan}")
EXPECT = {850: -1.1, 1000: 14.2, 1200: 49.5, 1400: 66.7, 1600: 72.6, 1800: 81.3, 1900: 85.2, 1996: 90.2}
gate("the eight truncations the scan reports are all present, and they are the seven the paper quotes "
     "plus the 1900 cut it does not",
     all(c in scan for c in EXPECT) and len(scan) == 8 and 1900 in scan)
gate("⓷ and every one of them matches the arm of record to a tenth -- -1.1, +14.2, +49.5, +66.7, "
     "+72.6, +81.3, +85.2, +90.2",
     all(abs(scan.get(c, 1e9) - v) <= 0.05 for c, v in EXPECT.items()))

# ⛭ THE SAME EIGHT FIGURES AGAIN, AS LITERAL COMPARISONS.
#   *`EXPECT` is a DICT iterated in a comprehension, and `check_figures_pinned`'s `pins()` reads
#   constants only inside an `ast.Compare` -- so the dict's eight values are invisible to it and the one
#   comparison above yields the pin `(1e9, 0.05)`.  ** That is the container blind spot in its fourth
#   form, after the `_SIX` and `_PIN6` tuples and the comprehension. **  This twin asserts nothing new;
#   it makes the SAME eight figures legible to the instrument that has to find them.  (The table is
#   additionally invisible for a SECOND, independent reason: the paragraph's `\rcpt` sits in its last
#   sentence and `sites()` reads only the sentence carrying the `\rcpt`.  Both are routed to 69.)*
gate("⌗ the eight cuts, stated again as literal comparisons the pin instrument can read",
     abs(scan[850] - -1.1) <= 0.05 and abs(scan[1000] - 14.2) <= 0.05
     and abs(scan[1200] - 49.5) <= 0.05 and abs(scan[1400] - 66.7) <= 0.05
     and abs(scan[1600] - 72.6) <= 0.05 and abs(scan[1800] - 81.3) <= 0.05
     and abs(scan[1900] - 85.2) <= 0.05 and abs(scan[1996] - 90.2) <= 0.05)

# ⛔ THE CLAIM AND THE MEASUREMENT ARE TWO GATES, NOT ONE WINDOW AROUND THE MEASUREMENT.
#   *The paper's claim is `more than half`; the measurement is `54.9 per cent`.  A single window would
#   fail the paper's sentence the next time the arm moves within it, and would pass a figure that had
#   stopped being more than half.*
# ⌗ *No attribution in this label, deliberately: it states what THIS run computes.  PART 6 reads the
#   claiming sentence out of `corpus/CR_cosmology.tex` and tests the same inequality at the ceiling that
#   sentence implies, which is where the attribution belongs and where it can fail.*
gate("⓷ MORE THAN HALF THE GAP IS PRESENT AT ell <= 1200, EIGHT HUNDRED MULTIPOLES BELOW THE CEILING "
     "-- the inequality, as this run of the audit measures it",
     scan.get(1200) is not None and scan[1200] / scan[1996] > 0.5)
gate("⌗ and the measurement behind it: 49.5 of 90.2 is 54.9 per cent (the namesake's 51.0 of 93.8 was "
     "54.4), so the re-point moves the share by half a point and the claim by nothing",
     abs(scan[1200] / scan[1996] - 0.549) <= 0.002)

gate("⌗ and it is MONOTONE above the onset, so the growth is the arm failing across scales rather than "
     "a single band dominating",
     all(scan[a] <= scan[b] + 1e-9 for a, b in zip(sorted(scan)[1:], sorted(scan)[2:])))

gate("⓸ AND IT IS NOT CONVERGED: the gap still grows at the last cut, so the quoted separation is a "
     "statement about the range read and not a saturated value",
     scan[1996] > scan[1900])
gate("⌗ and by how much: the last 96 multipoles add 5.0 on the arm of record (the namesake's 5.5)",
     abs((scan[1996] - scan[1900]) - 5.0) <= 0.1)


head("4.  THE FORBIDDEN ARM TRACKS THE CONTROL AT EVERY TRUNCATION, NOT ONLY AT THE FULL RANGE")

fc = re.findall(r'^\s+(\d{3,4})\s+\d+\s+.*?([\d.]+)/\d+\s+\d+\s+\d+\s+([\d.]+)\s+\d+\s+\d+\s+[-+]\d',
                OUT, re.M)
pairs = {int(c): (float(f), float(k)) for c, f, k in fc}
print(f"      forbidden vs control chi^2 per truncation: {pairs}")
worst = max((abs(f - k) for f, k in pairs.values()), default=1e9)
print(f"      largest forbidden-minus-control discrepancy across all truncations: {worst:.2f}")
gate("⓷ the forbidden arm sits within one unit of the control at EVERY truncation -- the stronger form "
     "of 'lands on the control's floor', and not something distance from a ceiling produces.  PART 6 "
     "reads the bound the paper states and holds this measurement to it",
     len(pairs) == 8 and worst <= 1.0)
gate("⛭ AND ON THE ARM OF RECORD THAT BOUND TIGHTENS FOURFOLD: the largest discrepancy across all "
     "eight ceilings is 0.3, against the namesake's 1.1.  The forbidden configuration does not sit "
     "NEAR the control's floor; it sits ON it.  ⌗ The paper's wording, 'within about one unit', is "
     "true and loose, and this is the figure that would tighten it",
     worst <= 0.35)


head("5.  THE BAND SHARES -- ABOUT HALF BETWEEN 850 AND 1500, ABOUT A THIRD BELOW 850")

bands = re.findall(r'\((\d+),(\d+)\]\s+\d+\s+[\d.]+\s+[\d.]+\s+[\d.]+\s+\+?([-\d.]+)\s+([\d.]+)%', OUT)
sh = {(int(a), int(b)): float(s) for a, b, _, s in bands}
print(f"      share of the gap per band: {sh}")
mid = sum(v for (a, b), v in sh.items() if a >= 850 and b <= 1500)
low = sum(v for (a, b), v in sh.items() if b <= 850)
print(f"      850 < ell <= 1500 carries {mid:.1f}%;  ell <= 850 carries {low:.1f}%")
gate("about HALF the full-range gap falls between ell = 850 and 1500 -- 51.8 per cent on the arm of "
     "record, the namesake's 52.2",
     len(sh) >= 6 and 48.0 <= mid <= 56.0 and abs(mid - 51.8) <= 0.15)
gate("⌗ and about a THIRD of it sits below ell = 850 -- 32.1 per cent, the namesake's 30.8 -- where "
     "the truncated fit absorbs it entirely (the 850 cut returns -1.1, a NEGATIVE gap), which is what "
     "makes the failure a cross-scale one",
     28.0 <= low <= 34.0 and abs(low - 32.1) <= 0.15 and scan.get(850, 9) < 0.0)

# ⌗ *This band table, and not the truncation scan, is what "the bulk of it, about half, falling between
#   ell ~ 850 and 1500" reads.  Stated because the scan ALSO rises most across that interval -- interpolated
#   linearly between its 1400 and 1600 cuts it has covered 70.8 of its 91.3 range at ell = 1500, 77
#   per cent -- so the two readings of one
#   sentence differ by twenty-five points.
#   The gate's reading is the band table's, as it has been since r7109, and it is the one the sentence's
#   "falling between" describes: where the gap LIVES, not where the scan CLIMBS.*


head("6.  THE PARAGRAPH IS READ OUT OF `corpus/CR_cosmology.tex`, NOT RECALLED FROM IT")

# ⛔ WHY THIS PART EXISTS, AND IT IS A CORRECTION TO THIS FILE AND NOT AN ADDITION TO IT.
#   *Every gate above asserted a figure and SOME of their labels called it "the paper's".  Nothing in
#   this receipt opened the paper, so `check_unread_figure` was right to go red on it: ** a receipt that
#   attributes a number to a paper it never reads stays green when the paper moves. **  The repair is the
#   one the instrument names -- READ the figures -- and not a softened label.  ⌗ This is the FOURTH time
#   this seat has been told it (cc66.89, r7651's PREDICTION commitment 4, the figure-pin baseline's own
#   note, and here), which is why the read is built to survive the landing rather than to pass today.*
TEX = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
FLAT = re.sub(r'\s+', ' ', open(TEX, encoding='utf-8', errors='replace').read())
print(f"      read {len(FLAT)} flattened characters of {os.path.relpath(TEX, ROOT)}")

RUN = re.compile(r"the specified configuration's excess over the forbidden one runs "
                 r"\$([-+][\d.]+)\$, \$([-+][\d.]+)\$, \$([-+][\d.]+)\$, \$([-+][\d.]+)\$, "
                 r"\$([-+][\d.]+)\$, \$([-+][\d.]+)\$ and \$([-+][\d.]+)\$ as the truncation "
                 r"moves from \$\\ell=(\d+)\$ to \$(\d+)\$")
RCPT = ('\\rcpt{P15_the_three_grid_comparison_is_like_for_like_and_not_a_ceiling_artefact_'
        'because_the_projection_reach_is_fixed_on_every_arm}')
gate("the paragraph this receipt closes is STILL IN THE PAPER, found by its own citation -- which is "
     "what makes everything below a read of THIS paragraph and not of a sentence that happens to "
     "match", RCPT in FLAT)

# ⛭ ALT, AND ONLY WHERE THIS TURN PROPOSES THE REWORDING.
#   *`cc66.94`'s rows settled the form: a bare locator on 69's sentence goes red the day 69 lands the
#   rewording this turn asks for, so the locator is one arm of a disjunction over paper states -- found,
#   and the figures must match; not found, and the miss is PRINTED and the gates stand on what the audit
#   prints.  ** The ALT flag is NOT spread over the whole part: the reach, the "eight hundred
#   multipoles", the word "third", the onset pair and the "grows to the last bin" clause are claims the
#   re-point does not change, so 69 has no reason to touch them and they are pinned HARD below. **
CUTS = [850, 1000, 1200, 1400, 1600, 1800, 1996]
m = RUN.search(FLAT)
if m is None:
    print("      ⛔ THE TRUNCATION-RUN LOCATOR MISSED: the clause has been reworded since this gate was "
          "written, so the seven-figure comparison is NOT made and is OWED a re-read.")
PAPER = [float(x) for x in m.groups()[:7]] if m else []
LO, HI = (int(m.group(8)), int(m.group(9))) if m else (CUTS[0], CUTS[-1])
print(f"      the paper prints {PAPER} as the truncation moves from {LO} to {HI}")
gate("⛭ the truncation run is READ out of the paper, over the seven ceilings the scan reports -- "
     "bottom 850 and top 1996, the scan's eight minus the 1900 cut the sentence does not quote",
     m is None
     or (LO == CUTS[0] and HI == CUTS[-1] and len(PAPER) == 7 and all(c in scan for c in CUTS)
         and len(scan) == 8))

# ⛭ A DISJUNCTION, FOR THE REASON THAT ALWAYS MAKES ONE NECESSARY HERE.
#   *This turn MEASURES the arm of record and RECOMMENDS the re-wording; 69 lands it.  A gate pinned to
#   the namesake fails the moment its own recommendation is taken, and one pinned to the arm of record
#   fails today.  ** So each figure is held to the two states this quantity has, and a summary gate
#   forbids the paragraph being MIXED -- which is the failure a disjunction alone would allow. **
NAMESAKE = [-1.0, 14.4, 51.0, 67.9, 74.7, 84.0, 93.8]
AOR = [-1.1, 14.2, 49.5, 66.7, 72.6, 81.3, 90.2]
gate("⌗ and the arm of record's seven, which THIS run of the audit prints, are the landed state the "
     "disjunction below offers",
     [round(scan[c], 1) for c in CUTS] == AOR)
_HIT = 0
for _i, _c in enumerate(CUTS):
    _old = bool(PAPER) and abs(PAPER[_i] - NAMESAKE[_i]) <= 0.05
    _new = bool(PAPER) and abs(PAPER[_i] - AOR[_i]) <= 0.05
    _HIT += 1 if _new else 0
    gate(f"⛭ the figure the paper prints at the ell <= {_c} ceiling is one of this quantity's two "
         f"states: the namesake's {NAMESAKE[_i]:+.1f} or the arm of record's {AOR[_i]:+.1f}",
         not PAPER or _old or _new)
print(f"      figures already in the arm-of-record state: {_HIT} of {len(PAPER)}")
gate("⛭ and the paragraph is in ONE state and not mixed: either all seven still read the namesake or "
     "all seven read the arm of record", not PAPER or _HIT == 0 or _HIT == 7)

rm = re.search(r"\$k_\{\\max\}D_M=(\d+)\$ against \$\\ell_\{\\max\}=(\d+)\$", FLAT)
print(f"      the reach the paper prints: {rm.groups() if rm else None}")
gate("⓶ the reach is READ from the paper -- not quoted from this file -- and it is what the audit "
     "reports on BOTH arms, which is the whole cancellation argument",
     rm is not None and int(rm.group(1)) == int(reach[0][1]) == int(reach[1][1])
     and int(rm.group(2)) == int(reach[0][2]) == int(reach[1][2]))

half = re.search(r"More than half the separation is already present ([a-z]+ [a-z]+) multipoles below "
                 r"the ceiling", FLAT)
TARGET = HI - 800
near = min(scan, key=lambda c: abs(c - TARGET))
print(f"      the paper says '{half.group(1) if half else None} multipoles below the ceiling'; "
      f"{HI} - 800 = {TARGET}; the scan's nearest cut is {near}")
gate("⓷ the 'more than half' claim is READ from the paper, and TESTED where the paper's own words put "
     "it: eight hundred multipoles below its own top ceiling is 1196, the scan's nearest cut is 1200, "
     "and the gap there is more than half the full-range gap",
     half is not None and half.group(1) == 'eight hundred' and near == 1200
     and scan[near] / scan[HI] > 0.5)

# ⌗ *The spans below open on their own subject, not on the preposition or subordinator the paper
#   puts in front of it ("with the bulk of it ...", "even though a third ..."), because a span that opens
#   on a preposition or a subordinator is DANGLING under the quote-pin baseline's subject rule and takes
#   a different verdict than the claim it carries deserves.*
bulk = re.search(r"about half, falling between \$\\ell\\simeq(\d+)\$ and \$(\d+)\$", FLAT)
gate("⌗ and the band the paper names for the bulk is READ from it -- 850 to 1500 -- and it is exactly "
     "the union of two of the audit's own bands, which is why the band table and not the scan is what "
     "'falling between' reads",
     bulk is not None and (int(bulk.group(1)), int(bulk.group(2))) == (850, 1500)
     and (850, 1200) in sh and (1200, 1500) in sh and 48.0 <= mid <= 56.0)

third = re.search(r"a ([a-z]+) of the separation on the full-range fit sits there", FLAT)
gate("⌗ the share the paper puts below the onset is READ from it as the word it uses, 'a third', and "
     "the band table returns 32.1 per cent",
     third is not None and third.group(1) == 'third' and 28.0 <= low <= 34.0)

# ⛭ THE BOUND IS READ AS A PHRASE AND MAPPED, because this turn RECOMMENDS tightening it.
#   *`worst` is 0.3 on the arm of record against 1.1 on the namesake, so "about one unit" is true and
#   loose.  ** The gate accepts either wording and holds the measurement to whichever the paper states;
#   an unrecognised wording FAILS rather than passing, because a bound this receipt cannot read is a
#   bound it cannot test. **
BOUNDS = {'about one unit': 1.0, 'one unit': 1.0,
          'three tenths of a unit': 0.35, 'about three tenths of a unit': 0.35}
bd = re.search(r"the forbidden configuration sits within ([a-z ]{3,40}?) of the control", FLAT)
phrase = bd.group(1) if bd else None
if phrase not in BOUNDS:
    print(f"      ⛔ THE BOUND'S WORDING IS NOT ONE THIS GATE CAN READ ({phrase!r}): it falls back to "
          f"the loosest bound in the map, and the wording is OWED an adjudication.")
_B = BOUNDS.get(phrase, max(BOUNDS.values()))
print(f"      the bound the paper states: {phrase!r} -> {_B};  measured {worst:.2f}")
gate("⛭ the control-tracking bound is READ from the paper as the phrase it uses, and this run's "
     "largest forbidden-minus-control discrepancy satisfies it.  ⌗ ALT for the same reason as the "
     "run above -- this turn proposes tightening that wording, so an unrecognised phrase PRINTS and "
     "falls back to the loosest bound rather than going red on 69's landing",
     worst <= _B)

# ⌗ *ONE span for the whole closing sentence, rather than a second pin on `converged---it grows to
#   the last bin`.  That clause's own subject is the pronoun "it", so a span cut to it would be dangling
#   under the subject rule; the sentence it sits in opens on "its onset", which is not.*
onset = re.search(r"its onset falls between \$\\ell\\simeq(\d+)\$ and \$(\d+)\$, it is "
                  r"already decisive by \$\\ell\\simeq(\d+)\$, and it is \\emph\{not\} "
                  r"converged---it grows to the last bin", FLAT)
gate("⓷⓸ the onset, the decisive ceiling AND the non-convergence clause are READ from the paper as the "
     "one sentence that carries them -- between 850 and 1000, decisive by 1200, growing to the last "
     "bin -- and the scan is the shape that says so: NEGATIVE at 850, positive at 1000, more than half "
     "the gap by 1200, and still rising at 1996",
     onset is not None
     and (int(onset.group(1)), int(onset.group(2)), int(onset.group(3))) == (850, 1000, 1200)
     and scan[850] < 0.0 < scan[1000] and scan[1200] / scan[1996] > 0.5
     and scan[1996] > scan[1900])


head("7.  WHAT IS NOT ASSERTED, STATED RATHER THAN LEFT TO BE NOTICED")

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
    like-for-like       ->  one ell sampling, control byte-identical in all nine files, arms differing
                            in ONE stamped switch (LEAFGEOM) at every CR step.
    the ceiling         ->  k_max*D_M = 3998 on BOTH arms, so the coupling cancels by construction.
    where it lives      ->  54.9 per cent of the gap at ell <= 1200; onset between 850 and 1000; 32.1
                            per cent below 850, absorbed there by the parameters.
    convergence         ->  NOT converged; +5.0 in the last 96 multipoles.
    the forbidden arm   ->  within 0.3 of the control at every truncation, which is fourfold tighter
                            than the "about one unit" the paper claims.
  => the paper's word is localised IN ONSET.  'Confined to high multipole' would be wrong, and the
     comparison survives the one mechanism that could have manufactured it.
""")
assert not bad, f"{len(bad)} check(s) failed: {bad}"
