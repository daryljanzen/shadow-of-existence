#!/usr/bin/env python3
"""r7660 (60) -- A COLD READ OF l.1938-1955 AND THE FLOOR SENTENCE, ON THE OBJECT **AND THE ROW**.

⛭ WHY THE ROW IS THE NEW PRECONDITION.  `r7658` enforced same-procedure-same-run on both sides of a
comparison, and that held.  It did NOT enforce which ROW of a multi-row table a figure is read from,
and that is exactly where its one reported defect went: I read the kernel receipt's NAMESAKE rows and
reported `-15.4` unsupported on the arm of record.

⛔ AND THE RESOLUTION WAS A TREE, WHICH IS THIS FILE'S FIRST RULE.  The arm-of-record running-phase row
did not exist in the receipt I banked: `cc66` added it in `3630fff1`, which is not an ancestor of the
`main` that bank was taken against.  So `r7658`'s reading and `r7659`'s correction were both right,
about different trees.  ⌗ *A cold read is a statement about a TREE and it has to name the tree* --
so every verdict here prints the commit it was read on, and `runs/TREE.txt` records it, written BEFORE
the banks were made.

WHAT THIS FILE CHECKS, in order:
  ⓐ  the forbidden-route paragraph and the four-ceiling sentence, every figure against the ARM OF
     RECORD row, with the NAMESAKE row printed beside it so the row the paper uses is visible
  ⓑ  the floor sentence, including the two clauses `cc66` routed last turn and `69` took
  ⓒ  the finding: the receipt's own paper-reader, seven groups, and the three that have gone BLIND

⛔ EVERY VERDICT IS A FUNCTION OF ITS STATED VALUE AND A DECOY MUST FLIP IT.  ⌗ *`r7656`'s pool
decoy-RATE control is deliberately not carried over: there is no pool here.  Saying so each time is
cheaper than rediscovering it.*
"""
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RUNS = os.path.join(HERE, 'runs')
_fail = []


def check(label, ok):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    if not ok:
        _fail.append(label)


def bank(n):
    return open(os.path.join(RUNS, n), encoding='utf-8', errors='replace').read()


LIC, KER, TREE = bank('licensed.txt'), bank('kernel.txt'), bank('TREE.txt')
RAW = open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'),
           encoding='utf-8', errors='replace').read()
FLAT = re.sub(r'\s+', ' ', RAW)


def grab(txt, pat, what, cast=float):
    m = re.search(pat, txt, re.S)
    if m is None:
        sys.exit(f"⛔ the bank no longer prints {what} in the form this file parses.  A stale number "
                 f"is worse than a failed parse, so this is a hard stop and not a fallback.")
    return [cast(g) for g in m.groups()]


print(__doc__)
print("=" * 112)
print("  r7660 (60) -- two stretches, the object AND the row, on a named tree")
print("=" * 112)

# ════════════════════════════════════════════════════════ ① the tree
print("\nⓐ  ① THE TREE EVERY VERDICT BELOW IS READ ON, recorded before the banks were made")
for line in TREE.strip().split('\n')[:4]:
    print("      " + line)
_wt = re.search(r'worktree: ([0-9a-f]{40})', TREE)
_dirty = re.search(r'dirty: (\d+) path', TREE)
try:
    _live = subprocess.run(['git', '-C', ROOT, 'rev-parse', 'HEAD'],
                           capture_output=True, text=True, timeout=20).stdout.strip()
except Exception:
    _live = ''
print(f"      the tree this run is reading from NOW: {_live[:40] or '(git unavailable)'}")
check("ⓐ① ① the tree is NAMED, with the commit of each receipt file the verdicts are read from, so "
      "a later reading can tell whether it disagrees with this one or with a different tree",
      _wt is not None and TREE.count('P15_the_') >= 2)
check(f"ⓐ② and nothing the verdicts read from was dirty when the banks were made "
      f"({_dirty.group(1) if _dirty else '?'} path(s), this revision's own output directory)",
      _dirty is not None and int(_dirty.group(1)) <= 1)

# ════════════════════════════════════════════════════════ ⓐ the paragraph, arm of record
print("\nⓑ  THE FORBIDDEN-ROUTE PARAGRAPH (l.1938-1955) -- the ARM OF RECORD row, the namesake beside it")
ROW = r'\s+(-?[\d.]+)\s+([\d.]+)\s+([+-][\d.]+)\s+([+-][\d.]+)\s+(\d+)\s+(\d+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)'
AOR_B = grab(LIC, r'THE ARM OF RECORD, read to ell \d+:.*?banked' + ROW, 'the arm-of-record banked row')
AOR_F = grab(LIC, r'THE ARM OF RECORD, read to ell \d+:.*?forbidden' + ROW, 'the arm-of-record forbidden row')
NS_F = grab(LIC, r'the NAMESAKE pair at the same ceiling.*?forbidden' + ROW, 'the namesake forbidden row')
CTL = grab(LIC, r'THE ARM OF RECORD, read to ell \d+:.*?control\s+(-[\d.]+)\s+([\d.]+)\s+([\d.]+)',
           'the control row')
print(f"      {'row':<26} {'c':>9} {'+-':>8} {'move/err':>9} {'|c| %':>8} {'cross':>6} {'run':>5} "
      f"{'chi2':>6} {'l_A':>9}")
for nm, r in (('ARM OF RECORD, banked', AOR_B), ('ARM OF RECORD, forbidden', AOR_F),
              ('namesake, forbidden', NS_F)):
    print(f"      {nm:<26} {r[0]:>9.4f} {r[1]:>8.4f} {r[2]:>9.2f} {r[3]:>8.1f} {int(r[4]):>6} "
          f"{int(r[5]):>5} {r[6]:>6.2f} {r[8]:>9.3f}")
print(f"      {'ARM OF RECORD, control':<26} {CTL[0]:>9.4f} {CTL[1]:>8.4f} "
      + " " * 32 + f"{CTL[2]:>9.3f}")


def claims(stated):
    """every figure the paragraph prints, as a FUNCTION of the stated values (arm \u2475 decoys)"""
    err, coef0, sd0, coef1, sd1, fall, cr0, cr1, run0, run1, x0, x1, la0, la1, lac = stated
    return dict(
        error=abs(AOR_F[2] - err) <= 0.05,
        coef_licensed=abs(AOR_B[0] - coef0) < 5e-5 and abs(AOR_B[1] - sd0) < 5e-5,
        coef_forbidden=abs(AOR_F[0] - coef1) < 5e-5 and abs(AOR_F[1] - sd1) < 5e-5,
        fall=abs(abs(AOR_F[3]) - fall) <= 0.5,
        crossings=int(AOR_B[4]) == cr0 and int(AOR_F[4]) == cr1,
        run=int(AOR_B[5]) == run0 and int(AOR_F[5]) == run1,
        chi2=abs(AOR_B[6] - x0) <= 5e-3 and abs(AOR_F[6] - x1) <= 5e-3,
        scale=abs(AOR_B[8] - la0) <= 5e-4 and abs(AOR_F[8] - la1) <= 5e-4
        and abs(CTL[2] - lac) <= 5e-4)


PAPER = (6.7, -0.0670, 0.0086, -0.0092, 0.0085, 86.0, 32, 38, 16, 12, 2.64, 1.33,
         302.943, 301.400, 301.375)
V = claims(PAPER)
print(f"\n      the paragraph's own figures, each against the ARM OF RECORD row:")
for k, v in V.items():
    print(f"         {k:<16} {'REPRODUCES' if v else '*** DOES NOT'}")
check(f"ⓑ① every figure the paragraph prints reproduces on the ARM OF RECORD row -- not on the "
      f"namesake row, which for the forbidden route reads {NS_F[0]:.4f}, {int(NS_F[4])}, "
      f"{int(NS_F[5])}, {NS_F[6]:.2f} and {NS_F[8]:.3f} instead", all(V.values()))
_d = list(PAPER)
_d[3] = -0.0192
check(f"ⓑ② \u2475 FAILABLE: moving the forbidden coefficient one digit makes that pin fail while the "
      f"rest stand, so each figure enters its own test",
      not claims(tuple(_d))['coef_forbidden'] and claims(tuple(_d))['scale'])
check(f"ⓑ③ AND THE ROW MATTERS, WHICH IS THE ORDER'S CONDITION: the same figures read off the "
      f"NAMESAKE row would fail -- its crossings are {int(NS_F[4])} against the paper's 38 and its "
      f"longest run {int(NS_F[5])} against 12's twin at a different chi2 of {NS_F[6]:.2f}",
      int(NS_F[4]) != 38 or abs(NS_F[6] - 1.33) > 5e-3)

CEIL = grab(LIC, r'ARM OF RECORD\s+specified \[([\d, ]+)\]\s+forbidden \[([\d, ]+)\]',
            'the four-ceiling runs', str)
spec = [int(x) for x in CEIL[0].split(',')]
forb = [int(x) for x in CEIL[1].split(',')]
print(f"\n      the four reading ceilings on the ARM OF RECORD: specified {spec}  forbidden {forb}")
check(f"ⓑ④ \u2476 THE RANGE IS SCORED CEILING BY CEILING, not at its extremes: the paper's "
      f"`9, 9, 9, 16` and `7, 8, 8, 12` match element for element",
      spec == [9, 9, 9, 16] and forb == [7, 8, 8, 12])
check(f"ⓑ⑤ and `every one of them with a longest run of seven to nine bins` holds at the three "
      f"ceilings below the fourth, element by element, on BOTH configurations "
      f"({spec[:3]} and {forb[:3]})",
      all(7 <= v <= 9 for v in spec[:3] + forb[:3]))
check(f"ⓑ⑥ \u2475 FAILABLE: a stated band of seven-to-eight would FAIL on the specified runs, so the "
      f"band is tested and not recited", not all(7 <= v <= 8 for v in spec[:3]))

# ════════════════════════════════════════════════════════ ⓑ the floor sentence
print("\nⓒ  THE FLOOR SENTENCE (l.2393-2402) -- on the ARM OF RECORD row that now exists")
FL = grab(KER, r'ARM OF RECORD at a common tilt: (-[\d.]+) deg = ([\d.]+)% of the residual (-[\d.]+)',
          "the floor's arm-of-record row")
FC = grab(KER, r'its control, same tilt:\s+(-[\d.]+) deg -- the two agree to ([\d.]+)%',
          "the floor's control row")
print(f"      arm of record {FL[0]} deg = {FL[1]}% of the residual {FL[2]}")
print(f"      its control   {FC[0]} deg -- the two agree to {FC[1]}%")
check(f"ⓒ① `-15.4 degrees` reproduces on the ARM OF RECORD row ({FL[0]}, which rounds to "
      f"{round(FL[0],1)}) -- the row `r7658` could not read because it did not yet exist",
      abs(FL[0] - -15.4) <= 0.05)
check(f"ⓒ② `a fifth of the residual` holds at {FL[1]}% = 1/{100/FL[1]:.2f}", abs(100 / FL[1] - 5) < 0.5)
check(f"ⓒ③ `common to the two arms to three tenths of a per cent` holds at {FC[1]}% on THIS row, "
      f"where on the namesake pair it is a tenth -- so the paper's figure is the arm's and the "
      f"looseness I reported at `r7658` was the namesake pair's", FC[1] <= 0.30)
check(f"ⓒ④ \u2475 FAILABLE: a stated `three hundredths of a per cent` would fail at {FC[1]}%",
      not FC[1] <= 0.03)
_j1 = re.search(r'`9 to 24 per cent`.*?AGAINST (-[\d.]+) THE RANGE IS (\d+) TO (\d+)', KER, re.S)
_j2 = 'IS TRUE OF THREE CONVENTIONS AND FALSE' in KER
print(f"\n      the two clauses cc66 routed last turn and 69 took:")
print(f"         the range: the receipt asserts the old `9 to 24` was the old residual's, and against "
      f"{_j1.group(1) if _j1 else '?'} the range is {_j1.group(2) if _j1 else '?'} to "
      f"{_j1.group(3) if _j1 else '?'}; the paper now prints 11 to 30")
print(f"         the endpoints: the receipt asserts `under a tenth of a point` is true of THREE "
      f"conventions and false across the half-maximum edges: {_j2}; the paper now says exactly that")
check(f"ⓒ⑤ both routed corrections are IN THE PAPER on this tree -- `11` to `30` per cent, and the "
      f"three endpoints separated from the half-maximum edges",
      bool(_j1) and (_j1.group(2), _j1.group(3)) == ('11', '30')
      and 'runs from $11$ to' in FLAT and 'under a tenth of a point between the three endpoints' in FLAT
      and 'by eight points across the visibility' in FLAT and _j2)

# ════════════════════════════════════════════════════════ ⓒ the blind reader
print("\nⓓ  ⑫ THE FINDING -- THE RECEIPT'S OWN PAPER-READER, SEVEN GROUPS, AND WHAT THE REWORDING DID")
# ⛔ THE SEVEN GROUP NAMES ARE TAKEN FROM THE RECEIPT, NOT SCRAPED OUT OF ITS OUTPUT.
# The first version of this block scraped them with a regex over the printed lines, and the regex
# swallowed the banner above the table into one "name" and glued two others onto the lines before
# them -- so two groups fell out of the RECOVER table and were scored WITHDRAWN.  It would have
# reported 1 BLIND where there are 3, UNDERSTATING the finding.  ⌗ *A parser loose enough to
# mis-read its own input will answer about the parser, and this time in the safe-looking direction.*
GROUPS = ['coef, licensed', 'shape, licensed', 'coef, forbidden', 'the fall',
          'shape, forbidden', 'the scale', 'the ceiling']
NOTFOUND, FOUND = set(), set()
for g in GROUPS:
    m = re.search(r'^\s+' + re.escape(g) + r'\s+(\*\* NOT FOUND[^*]*\*\*|\(.*\))\s*$', LIC, re.M)
    if m is None:
        sys.exit(f"⛔ the receipt no longer prints a reader line for `{g}`.  The seven groups are "
                 f"this finding's whole object, so a missing one is a hard stop and not a zero.")
    (NOTFOUND if 'NOT FOUND' in m.group(1) else FOUND).add(g)
check(f"ⓓ①' every one of the receipt's {len(GROUPS)} reader groups is accounted for, by NAME "
      f"taken from the receipt rather than scraped from its output: {len(FOUND)} found, "
      f"{len(NOTFOUND)} not", len(FOUND) + len(NOTFOUND) == len(GROUPS))
RECOVER = {
    'coef, forbidden': r'by \$([\d.]+)\$ of its own error, from \$(-[\d.]+)\\pm([\d.]+)\$ to '
                       r'\$(-[\d.]+)\\pm([\d.]+)\$',
    'shape, forbidden': r'the sign changes rise from \$(\d+)\$ to \$(\d+)\$, the longest run of one '
                        r'sign falls from \$(\d+)\$ to \$(\d+)\$ and \$\\chi\^\{2\}\$ per bin falls '
                        r'from \$([\d.]+)\$ to \$([\d.]+)\$',
    'the ceiling': r'\\emph\{indistinguishable below \$\\ell\\simeq(\d+)\$\}---every one of them with '
                   r'a longest run of ([a-z]+) to ([a-z]+) bins',
    'coef, licensed': r'moves by \$[\d.]+\$ of its own error, its magnitude \\emph\{rising\}',
    'shape, licensed': r'the longest run of one sign goes from \$\d+\$ to \$\d+\$ bins, the wrong way',
}
print(f"      the receipt prints {len(NOTFOUND)} of its {len(GROUPS)} groups as NOT FOUND: "
      f"{sorted(NOTFOUND)}")
print(f"      and finds {sorted(FOUND)}")
print(f"\n      {'group':<18} {'receipt':>9}   an independent pattern on the CURRENT paper")
rows = []
for g in sorted(NOTFOUND):
    m = re.search(RECOVER[g], FLAT) if g in RECOVER else None
    verdict = 'BLIND' if m else 'WITHDRAWN'
    rows.append((g, verdict, list(m.groups()) if m else []))
    print(f"      {g:<18} {'NOT FOUND':>9}   "
          + (f"FOUND {list(m.groups())}  -> BLIND" if m else "also absent  -> WITHDRAWN"))
nb = sum(1 for _g, v, _x in rows if v == 'BLIND')
nw = sum(1 for _g, v, _x in rows if v == 'WITHDRAWN')
print(f"""
      ⇒ {len(FOUND)} FOUND, {nb} BLIND, {nw} WITHDRAWN.
      ⌗ The two WITHDRAWN are the licensed half: the paragraph no longer prints a measured licensed
      null, it says `moves neither statistic by construction` -- which is THE RECEIPT'S OWN
      RECOMMENDATION ① taken, so NOT FOUND is the right answer there.
      ⛔ The {nb} BLIND are figures the paper STILL PRINTS, missed on three small rewordings:
      `the same coefficient ... to` became `the contrast coefficient ... from ... to`; `the longest
      run falls` became `the longest run OF ONE SIGN falls`; `a longest run of X or Y bins` became
      `X TO Y bins`.  And the figures recovered are the ones the receipt's own table measures.""")
# ⑭ the negative: do the recovered figures AGREE with the receipt's table?
_cf = next((x for g, v, x in rows if g == 'coef, forbidden'), [])
_sf = next((x for g, v, x in rows if g == 'shape, forbidden'), [])
_ce = next((x for g, v, x in rows if g == 'the ceiling'), [])
agree = (bool(_cf) and abs(float(_cf[1]) - AOR_B[0]) < 5e-5 and abs(float(_cf[3]) - AOR_F[0]) < 5e-5
         and bool(_sf) and int(_sf[0]) == int(AOR_B[4]) and int(_sf[1]) == int(AOR_F[4])
         and abs(float(_sf[5]) - AOR_F[6]) <= 5e-3
         and bool(_ce) and int(_ce[0]) == 900)
print(f"      ⑭ and the recovered figures AGREE with the receipt's own arm-of-record table: {agree}")
check(f"ⓓ① ⑬ AS REGISTERED: 2 FOUND, {nb} BLIND, {nw} WITHDRAWN", nb == 3 and nw == 2)
check(f"ⓓ② ⑭ THE NEGATIVE IS TESTED AND NOT REACHED: every figure recovered from the current wording "
      f"EQUALS the receipt's own measured value, so the blindness costs no claim that is wrong -- "
      f"only a check that is no longer being made", agree)
check(f"ⓓ③ ⑮ and BLIND is told from WITHDRAWN by a pattern printed beside each verdict, so the "
      f"distinction can be checked rather than believed",
      all(g in RECOVER for g, _v, _x in rows))
_short = '_PP[key] is None' in open(
    os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                 'P15_the_licensed_configuration_moves_neither_statistic_and_the_swing_was_read_'
                 'above_where_it_converges.py'), encoding='utf-8', errors='replace').read() or \
    "is None" in LIC
print(f"""
      ⇒ ⛔ AND THE CONSEQUENCE, WHICH IS THE WHOLE FINDING: the receipt tolerates a missing read by
      short-circuit -- a `None` satisfies the conjunction -- which was the RIGHT design when the
      sentence might be withdrawn.  For these {nb} the sentence was not withdrawn, only reworded, so a
      guard built to compare the paper's digits against the receipt's is comparing nothing, AND IT IS
      GREEN.  ⌗ *A guard that cannot fail on the data it is given is not a guard -- my own standing
      lesson, found this time in another seat's receipt and caused by neither seat's mistake: cc66
      wrote the reader, 69 reworded the sentence, and the tolerance that made the reader safe is what
      made the blindness silent.*  ⑯ No correction is proposed and nothing is edited; the three
      repointed patterns are routed as a diff.""")

print("\n" + "=" * 112)
print(f"  {len(_fail)} failure(s)")
for f in _fail:
    print("   [FAIL] " + f)
json.dump(dict(tree=dict(worktree=_wt.group(1) if _wt else None, live=_live,
                         dirty=int(_dirty.group(1)) if _dirty else None),
               arm_of_record=dict(banked=AOR_B, forbidden=AOR_F, control=CTL),
               namesake_forbidden=NS_F, paragraph_verdicts=V,
               ceilings=dict(specified=spec, forbidden=forb),
               floor=dict(arm=FL, control=FC,
                          range_corrected=[_j1.group(2), _j1.group(3)] if _j1 else None,
                          endpoint_split=_j2),
               reader=dict(not_found=sorted(NOTFOUND), blind=nb, withdrawn=nw,
                           rows=[dict(group=g, verdict=v, recovered=x) for g, v, x in rows],
                           recovered_agree_with_table=agree),
               failures=_fail),
          open(os.path.join(HERE, 'verdicts.json'), 'w'), indent=1)
sys.exit(1 if len(_fail) > 0 else 0)
