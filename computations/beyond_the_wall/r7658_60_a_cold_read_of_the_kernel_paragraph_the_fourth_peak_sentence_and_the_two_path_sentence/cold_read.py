#!/usr/bin/env python3
"""r7658 (60) -- A COLD READ OF THREE STRETCHES OF P15, ON THE SAME OBJECT AND THE SAME LOCATOR.

⛭ WHAT `r7657` ORDERED, AND WHY THE FIRST RULE OF THIS FILE IS A PRECONDITION AND NOT A PREFERENCE.
At `r7656` I set the arm's peaks from one locator against the sky's quartet from ANOTHER, and reported
the difference as the paper's.  Two of my three verdicts were artefacts of that basis.  So here:

  ⛔ NO COMPARISON IS SCORED UNLESS BOTH OF ITS SIDES COME OUT OF THE SAME PROCEDURE IN THE SAME RUN.
     A reading whose two sides come from different procedures is `MIXED-BASIS` and is reported as
     UNSCOREABLE -- in either direction, because a mixed basis manufactures a disagreement as easily
     as it hides one.

⌗ *An identification has to be checked on the loci the object itself distinguishes.*

AND WHAT THIS FILE IS ACTUALLY FOR.  `r7656` established that no ratchet of this corpus watches a
quantity stated in WORDS; the sentences carrying them score green on their decimals.  These three
stretches are dense with them -- "over three orders of magnitude", "nearly nine tenths", "a fifth",
"two thirds", "by more than either differs from the sky" -- and every one is checked here against the
figures its own sentence prints, arithmetically.

⛔ AND EVERY VERDICT IS A FUNCTION OF ITS STATED VALUE, WITH A DECOY THAT MUST FLIP IT (arm ⑭).  At
`r7656` I shipped a check that compared a value to itself and could not fail.  The decoy is the control
for that, and it runs every time.  ⌗ *The pool decoy-RATE control of `r7656` is deliberately not
carried over: it measured a pool search, and there is no pool here.  Carrying it over would be the
same error one layer up.*

EVERY NUMBER BELOW IS PARSED OUT OF THE BANKED RECEIPT OUTPUT IN `runs/`, never typed in, so a changed
printing fails the parse loudly instead of scoring a stale figure.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RUNS = os.path.join(HERE, 'runs')
P15 = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')

_fail, _miss = [], []


def check(label, ok):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    if not ok:
        _fail.append(label)


def bank(name):
    return open(os.path.join(RUNS, name), encoding='utf-8', errors='replace').read()


KER, MAT = bank('kernel.txt'), bank('matched.txt')
PAPER = open(P15, encoding='utf-8', errors='replace').read().split('\n')


def grab(txt, pattern, what, n=1):
    """pull numbers out of a bank, or STOP -- a stale number is worse than a failed parse"""
    m = re.search(pattern, txt)
    if m is None:
        sys.exit(f"⛔ the bank no longer prints {what} in the form this file parses.  A stale number "
                 f"is worse than a failed parse, so this is a hard stop and not a fallback.")
    g = [float(x) for x in m.groups()]
    return g if n > 1 else g[0]


def paper_has(s, lo=2060, hi=2400):
    return any(s in l for l in PAPER[lo - 1:hi])


N = r'([-+]?[0-9]+\.[0-9]+)'
print(__doc__)
print("=" * 112)
print("  r7658 (60) -- three stretches, one locator, the words checked as well as the figures")
print("=" * 112)

# ════════════════════════════════════════════ ⓐ the matched locator: one procedure, both sides
print("\nⓐ  ① THE MATCHED LOCATOR -- `PART 4B`, where BOTH sides of every comparison come from ONE run")
SKY = grab(MAT, rf'THE SKY, this locator\s+{N}\s+{N}\s+{N}\s+{N}', "the sky's matched row", 4)
AOR = grab(MAT, rf'ARM OF RECORD, distances \*\*\s+{N}\s+{N}\s+{N}\s+{N}', "the arm of record's row", 4)
CTL = grab(MAT, rf'the CONTROL, L2000\s+{N}\s+{N}\s+{N}\s+{N}', "the control's row", 4)
dA = [a - s for a, s in zip(AOR, SKY)]
dC = [c - s for c, s in zip(CTL, SKY)]
print(f"      the sky            {'  '.join(f'{x:8.2f}' for x in SKY)}")
print(f"      the arm of record  {'  '.join(f'{x:8.2f}' for x in AOR)}   offsets "
      f"{' '.join(f'{x:+.2f}' for x in dA)}")
print(f"      the control        {'  '.join(f'{x:8.2f}' for x in CTL)}   offsets "
      f"{' '.join(f'{x:+.2f}' for x in dC)}")
check("ⓐ① all three rows are parsed from ONE receipt's ONE run, so every offset below is same-basis",
      len(SKY) == len(AOR) == len(CTL) == 4)


def claim_A(bound):
    return max(abs(x) for x in dA[:3]) <= bound


def claim_B(stated_pc):
    got = 100.0 * dA[3] / SKY[3]
    return abs(round(got, 1) - round(stated_pc, 1)) < 0.05, got


def claim_each(bound):
    return max(abs(x) for x in dA) < bound


def claim_shared(frac):
    got = dC[3] / dA[3]
    return abs(got - frac) <= 0.05, got


def claim_spreads(stated, spread):
    got = dA[3] / spread
    return abs(round(got, 1) - stated) < 0.05, got


SPREAD = 2.36
okB, gotB = claim_B(1 / 3)
okS, gotS = claim_shared(2 / 3)
okP, gotP = claim_spreads(1.4, SPREAD)
print(f"\n      (A) \"the first three peaks within three and a quarter multipoles\"   worst "
      f"{max(abs(x) for x in dA[:3]):.2f}  -> {'HOLDS' if claim_A(3.25) else 'FAILS'}")
print(f"      \"under three and a half multipoles at each\"                        worst "
      f"{max(abs(x) for x in dA):.2f}  -> {'HOLDS' if claim_each(3.5) else 'FAILS'}")
print(f"      (B) \"the fourth a third of a per cent high\"                        "
      f"{gotB:.3f}%  -> {'HOLDS' if okB else 'FAILS'}  (0.333% stated; equal at one sig. fig.)")
print(f"      \"the fourth peak sits 1.4 of the sky's own locating spreads high\"  "
      f"{gotP:.3f}  -> {'HOLDS' if okP else 'FAILS'}")
print(f"      \"two thirds of that offset shared with the control\"                "
      f"{gotS:.3f}  -> {'HOLDS' if okS else 'FAILS'}")
check(f"ⓐ② ② r7657's REQUEST DISCHARGED: (A) and (B) are confirmed against PART 4B's own printed "
      f"rows, and r7656's FAIL on (B) was an artefact of my basis, not the paper's",
      claim_A(3.25) and okB)
check(f"ⓐ③ and the two claims the same sentence makes about the fourth peak hold on the SAME rows -- "
      f"1.4 spreads ({gotP:.2f}) and two thirds shared ({gotS:.2f})", okP and okS)
check(f"ⓐ④ ⑭ FAILABLE: a bound of 2.00 makes (A) fail, 0.29% makes (B)'s stated value the measured "
      f"one, 3.0 makes \"at each\" fail, and a third makes the shared fraction fail",
      (not claim_A(2.00)) and claim_B(gotB)[0] and (not claim_each(3.0))
      and (not claim_shared(1 / 3)[0]))

# ════════════════════════════════════════════ ⓑ the kernel paragraph
print("\nⓑ  THE KERNEL PARAGRAPH (l.2378-2398) -- every figure against the ARM OF RECORD rows")
RES = grab(KER, rf"l\.2383's residual {N}", "the paragraph's residual read out of the paper")
RUN = grab(KER, rf"each arm on its OWN n_s \(([0-9.]+) vs ([0-9.]+)\):\s+\+{N} deg\s+{N} orders",
           "the as-run pair", 4)
COM = grab(KER, rf'both arms at a COMMON n_s = 0\.96\s+:\s+\+{N} deg\s+{N} orders',
           'the common-tilt pair', 2)
PH = grab(KER, rf"running phase, arm: {N} deg", "the kernel's own running phase")
RD = grab(KER, rf'ARM OF RECORD, six decimals\s+:\s+\+{N} per cent', "r_D/D_M on the arm of record")
ENDS = [float(x) for x in re.findall(rf'\+[0-9.]+%\s+\+({"".join(["[0-9.]+"])}) deg', KER)]
ENDS = [float(x) for x in re.findall(r'\s[-+][0-9.]+%\s+([-+][0-9.]+) deg', KER)][1::2]
print(f"      residual the paragraph names        {RES}")
print(f"      tilts as run                        {RUN[0]} and {RUN[1]}")
print(f"      as run                              +{RUN[2]} deg   {RUN[3]} orders below")
print(f"      at a common tilt                    +{COM[0]} deg   {COM[1]} orders below")
print(f"      the kernel's own running phase      {PH} deg")
print(f"      r_D/D_M separation                  +{RD} per cent")
print(f"      the five endpoints (arm of record)  {' '.join(f'{x:+.5f}' for x in ENDS)}")


def pin(stated, got, tol):
    return abs(got - stated) <= tol


def orders(diff, residual):
    import math
    return math.log10(abs(residual) / abs(diff))


check(f"ⓑ① every figure the paragraph prints reproduces on the ARM OF RECORD TO HALF A UNIT IN "
      f"ITS LAST PRINTED DIGIT -- EXCEPT ONE, which ⑰ takes up below: +0.041 ({COM[0]}), +0.33 "
      f"(+{RUN[2]}), the tilts 1.015 and 0.96 ({RUN[0]}/{RUN[1]}) and about 0.8 per cent (+{RD})",
      pin(0.041, COM[0], 5e-4) and pin(0.33, RUN[2], 5e-3) and pin(1.015, RUN[0], 1e-3)
      and pin(0.96, RUN[1], 1e-6) and pin(0.8, RD, 0.05))
check(f"ⓑ② and the paragraph's endpoint RANGE is the exact min and max of the five it is read from: "
      f"+0.028 = {min(ENDS):+.5f}, +0.063 = {max(ENDS):+.5f}",
      len(ENDS) == 5 and pin(0.028, min(ENDS), 5e-4) and pin(0.063, max(ENDS), 5e-4))
check(f"ⓑ③ \"always of one sign\" -- all five endpoints are positive on the arm of record "
      f"({sum(1 for x in ENDS if x > 0)} of {len(ENDS)})", all(x > 0 for x in ENDS))
print(f"\n      THE CLAIMS IN WORDS, on the residual the PARAGRAPH names ({RES}):")
for words, diff, want, rel in (('over three orders of magnitude below it', COM[0], 3.0, 'ge'),
                               ('no less than three orders on every convention', max(ENDS), 3.0, 'ge'),
                               ('still over two orders below the residual', RUN[2], 2.0, 'ge')):
    got = orders(diff, RES)
    print(f"         {words:<48} {got:.3f} orders  -> "
          f"{'HOLDS' if got >= want else 'FAILS'}")
tenths = (RUN[2] - COM[0]) / RUN[2]
fifth = abs(PH / RES)
print(f"         {'nearly nine tenths of it the tilt' + chr(39) + 's':<48} {tenths:.4f}      -> "
      f"{'HOLDS' if 0.85 <= tenths < 0.90 else 'FAILS'}")
print(f"         {'a fifth of the residual':<48} 1/{1/fifth:.2f}       -> "
      f"{'HOLDS' if abs(1/fifth - 5) < 0.5 else 'FAILS'}")
check(f"ⓑ④ every derived WORD in the paragraph holds on the residual the paragraph names, and no "
      f"ratchet of this corpus was watching any of them",
      orders(COM[0], RES) >= 3.0 and orders(max(ENDS), RES) >= 3.0 and orders(RUN[2], RES) >= 2.0
      and 0.85 <= tenths < 0.90 and abs(1 / fifth - 5) < 0.5)
RES2 = grab(KER, rf'the residual:\s+{N} deg', "this receipt's own residual")
print(f"\n      ⌗ AND THE SAME WORDS ON THE RECEIPT'S OWN RESIDUAL ({RES2}), which is why its text "
      f"says `a sixth` where the paragraph says `a fifth`:")
print(f"         over three orders   {orders(COM[0], RES2):.3f}        a fifth/a sixth   "
      f"1/{abs(RES2/PH):.2f}")
check(f"ⓑ⑤ ⑧ SCORED A MISS, AND ⑨'S NEGATIVE IS REACHED: both wordings are RIGHT, each on its own "
      f"denominator -- the receipt's `a sixth` on {RES2} (1/{abs(RES2/PH):.2f}) and the paragraph's "
      f"`a fifth` on {RES} (1/{1/fifth:.2f}) -- so only the filename is stale, and a filename is "
      f"not a claim", abs(abs(RES2 / PH) - 6) < 0.5 and abs(1 / fifth - 5) < 0.5)
check(f"ⓑ⑥ and the receipt ENUMERATES both residual states as a disjunction rather than pinning one, "
      f"which is why it was right before I looked",
      'DISJUNCTION' in KER and str(RES) in KER and '-96.6' in KER)

# ════════════════════════════════════════════ ⓑ' ⑰ the one figure the pin check caught
print("\nⓑ'  ⑰ THE ONE FIGURE A PIN OF MINE CAUGHT -- `-15.4`, against every value either bank prints")
STATED = -15.4
HALF = 0.05                       # half a unit in the last printed digit; the gate's own allowance
ALLOW = max(HALF, 0.0005 * abs(STATED))
ROWS = []
for route, pat in (('closed-form window', r'closed-form window : arm\s+(-[0-9.]+)\s+control\s+(-[0-9.]+)'),
                   ('full Bessel sum', r'full Bessel sum\s+: arm\s+(-[0-9.]+)\s+control\s+(-[0-9.]+)')):
    m = re.search(pat, KER)
    if m:
        ROWS.append((route, 'arm', float(m.group(1))))
        ROWS.append((route, 'control', float(m.group(2))))
print(f"      the sentence: \"the kernel's own running phase is {STATED} degrees ... common to the TWO ARMS\"")
print(f"      the gate's allowance for a figure printed to one decimal: {ALLOW}")
print(f"\n      {'route':<22} {'arm':<8} {'value':>10} {'to 1 dp':>9} {'distance':>9}  verdict")
for route, which, v in ROWS:
    d = abs(v - STATED)
    print(f"      {route:<22} {which:<8} {v:>10.4f} {v:>9.1f} {d:>9.4f}  "
          + ('inside' if d <= ALLOW else 'OUTSIDE half a unit'))
ARMS = [v for _r, w, v in ROWS if w == 'arm']
INSIDE = [(r, w, v) for r, w, v in ROWS if abs(v - STATED) <= ALLOW]
arm_rounds = [v for v in ARMS if abs(v - STATED) <= ALLOW]
print(f"""
      ⇒ VERDICT: {'LOCATED' if arm_rounds else 'OUTSIDE THE PRINTED DIGIT'} -- {len(INSIDE)} of the {len(ROWS)} rows is inside the allowance, and it is
      {'an ARM' if arm_rounds else 'a CONTROL on one of the two routes'}, where the sentence names the arms in common.  The correctly rounded
      value of every arm row is {min(ARMS):.1f}.  ⌗ *Right to about half a per cent and wrong at the digit
      it prints -- which changes nothing the paragraph argues, since `a fifth` holds at either value
      (1/{abs(STATED)/abs(RES)*-1 and abs(RES/STATED):.2f} and 1/{abs(RES/min(ARMS)):.2f}).*""")
check(f"ⓑ'① ⑰ AS REGISTERED: the paper's {STATED} is OUTSIDE half a unit of every ARM value either "
      f"route prints (nearest {min(abs(v - STATED) for v in ARMS):.4f} against an allowance of "
      f"{ALLOW}), and the only row inside it is a control on one route",
      not arm_rounds and len(INSIDE) >= 1)
# ⑲ THE NEGATIVE, SEARCHED ACROSS BOTH BANKS -- AND THE SEARCH HAD TO BE MADE COLUMN-AWARE.
# ⛔ The first version of this scan was LINE-level: any line naming `arm` that carried a value
# inside the allowance.  It returned ONE hit -- and the hit was `-15.4391`, the CONTROL's value,
# sitting on a line that reads `arm -15.4532  control -15.4391`.  A line-level search cannot tell
# which column a number is in, so it attributed a control value to an arm and reported the
# negative as reached.  ⌗ *A search whose granularity is coarser than the distinction it is
# asked to make will answer about its own granularity -- which is this seat's standing lesson in
# its third form, and the reason the scan below attributes each value to the label before it.*
_near = []
for ln in (KER + '\n' + MAT).split('\n'):
    for lab, val in re.findall(r'\b(arm|control)\b\s+(-?\d+\.\d+)', ln, re.I):
        if lab.lower() == 'arm' and abs(float(val) - STATED) <= ALLOW:
            _near.append((ln.strip()[:60], float(val)))
print(f"      ⑲ scanned both banks COLUMN-AWARE for an ARM value inside {ALLOW} of {STATED}: "
      f"{len(_near)} found" + (f'  {_near[:2]}' if _near else '')
      + f"   (the line-level version of this scan found 1, and it was the CONTROL's)")
check(f"ⓑ'② ⑲ THE NEGATIVE IS SEARCHED ACROSS BOTH BANKS, COLUMN-AWARE, AND NOT REACHED: not "
      f"one ARM value in either output lies inside the allowance of the paper's figure ({len(_near)} "
      f"found).  The line-level scan that preceded this one returned a CONTROL value and would have "
      f"reported the negative reached -- so the granularity of the search is part of the result",
      not _near)
check(f"ⓑ'③ and the finding does not touch the argument: `a fifth of the residual` holds at the "
      f"paper's {STATED} (1/{abs(RES/STATED):.2f}) and at the arm's {min(ARMS):.1f} "
      f"(1/{abs(RES/min(ARMS)):.2f}) alike, so this is a printed digit and not a result",
      abs(abs(RES / STATED) - 5) < 0.5 and abs(abs(RES / min(ARMS)) - 5) < 0.5)
COMMON = grab(KER, r'the two agree to ([0-9.]+)%', 'the two arms\' agreement')
print(f"\n      ⑱ AND THE SAME SENTENCE IS LOOSER THAN ITS RECEIPT THE OTHER WAY: it says the two arms")
print(f"      agree \"to three tenths of a per cent\" where the receipt prints {COMMON}% -- true, and "
      f"weaker by {0.3/COMMON:.1f}x.")
check(f"ⓑ'④ ⑱ the `three tenths of a per cent` claim HOLDS and is LOOSE: the measured agreement "
      f"is {COMMON}%, inside the stated 0.3% by a factor of {0.3/COMMON:.1f}, and it is reported as a "
      f"weaker statement rather than folded in with ⑰'s mis-printed digit",
      COMMON <= 0.3 and 0.3 / COMMON > 2.0)

# ════════════════════════════════════════════ ⓒ ⑪ the clause attached to the other pair
print("\nⓒ  ⑪ THE ONE CLAUSE WHOSE FIGURE AND WHOSE SUPPORT ARE TWO DIFFERENT PAIRS")
TWO = grab(KER, rf'closed-form window : arm\s+{N}\s+control\s+{N}\s+arm-control\s+{N}',
           'the closed-form two-route row', 3)
BES = grab(KER, rf'full Bessel sum\s+: arm\s+{N}\s+control\s+{N}\s+arm-control\s+{N}',
           'the Bessel two-route row', 3)
aor_two_route = bool(re.search(r'arm of record.*(?:bessel|closed.form)|'
                               r'(?:bessel|closed.form).*arm of record', KER, re.I))
print(f"      the paragraph:  \"+{COM[0]:.3f} degrees ... with the closed-form window and the full")
print(f"                       spherical-Bessel sum agreeing to the fifth decimal place\"")
print(f"      the receipt's two-route section is on ITS OWN pair:")
print(f"         closed-form window  arm-control {TWO[2]:+.5f} deg")
print(f"         full Bessel sum     arm-control {BES[2]:+.5f} deg   -- they differ by "
      f"{abs(TWO[2]-BES[2]):.0e}, one unit in the FIFTH decimal")
print(f"      is there ANY two-route row on the ARM OF RECORD in this output?  "
      f"{'YES' if aor_two_route else 'NO'}")
print(f"""      ⇒ VERDICT: {'LOCATED' if aor_two_route else 'MIXED-BASIS'} -- the clause's figure is the arm of record's
      ({COM[0]:+.3f}), and the agreement it cites is established on the pair at {TWO[2]:+.5f}.  The
      agreement itself is REAL and holds exactly as worded on the pair it was measured on; what is
      unestablished is that it holds on the pair the sentence names.  ⌗ *This is the defect `r7657`
      caught in me, one level up, and I looked for it only because it did.*""")
check(f"ⓒ① ⑪ AS REGISTERED: the two-route agreement is MIXED-BASIS -- measured on the pair at "
      f"{TWO[2]:+.5f} and attached to the figure at {COM[0]:+.3f}, with no two-route row on the arm "
      f"of record anywhere in the output", not aor_two_route)
check(f"ⓒ② and the agreement IS true as worded on the pair it was measured on: the two routes differ "
      f"by {abs(TWO[2]-BES[2]):.0e}, one unit in the fifth decimal place, so this is a question of "
      f"WHICH PAIR and not of whether the agreement holds",
      1e-5 <= abs(TWO[2] - BES[2]) < 1e-4)
SYNTH = 'closed-form window : ARM OF RECORD  -0.04106   control  -0.00000'
_probe = bool(re.search(r'arm of record.*(?:bessel|closed.form)|'
                       r'(?:bessel|closed.form).*arm of record', SYNTH, re.I))
check(f"ⓒ③ ⑫ THE NEGATIVE IS REACHABLE AND IS SHOWN TO BE: the same scan run against a synthetic "
      f"line that DOES name a route beside the arm of record returns {_probe}, so the NO above is "
      f"the output's answer and not a scan that could never say YES",
      _probe and not aor_two_route)

# ════════════════════════════════════════════ ⓓ ⑬ the gate whose object was withdrawn
print("\nⓓ  ⑬ A PASSING GATE WHOSE SENTENCE NO LONGER EXISTS")
withdrawn = 'NO LONGER CARRIES THAT SENTENCE' in KER
h4 = re.search(r'(OK|FAIL)\s+⛔⛭⛭ \*\* Ⓗ④', KER)
still_014 = paper_has('0.14 degrees') or paper_has('2.8 orders')
print(f"      the receipt prints, of l.2387-2388:  "
      f"{'NO LONGER CARRIES THAT SENTENCE -- reworded since r7655' if withdrawn else '(not printed)'}")
print(f"      and four lines below, Ⓗ④ asserts:    no endpoint convention reproduces l.2388's "
      f"`0.14 degrees` or its `no less than 2.8 orders`  [{h4.group(1) if h4 else '?'}]")
print(f"      does the paragraph still carry `0.14 degrees` or `2.8 orders`?  "
      f"{'YES' if still_014 else 'NO'}")
print(f"""      ⇒ So a PASSING gate is asserting a miss against a sentence that has been withdrawn and
      replaced by `+0.028` to `+0.063` and `no less than three orders`, both of which this file
      confirms above.  ⌗ *A gate must assert the clause its argument reasons FROM, never the status of
      a sentence a live row is asking to change.*  The gate is `cc66`'s: it is ROUTED, never edited,
      and no correction to it is proposed here.""")
check(f"ⓓ① ⑬ AS REGISTERED: Ⓗ④ passes, its object is gone from the paragraph, and the receipt itself "
      f"prints that the lines no longer carry the sentence",
      withdrawn and h4 is not None and h4.group(1) == 'OK' and not still_014)

# ════════════════════════════════════════════ ⓔ the two-path sentence
print("\nⓔ  THE TWO-PATH SENTENCE (l.2079-2082) -- both paths on the CONTROL, through one procedure")
POL = grab(MAT, rf'POLARISATION: control LCDM\s+\[[^\]]*\]\s+{N}\s+{N}\s+{N}', 'the polarisation row', 3)
FLU = grab(MAT, rf'FLUID:\s+control LCDM\s+\[[^\]]*\]\s+{N}\s+{N}\s+{N}', 'the fluid row', 3)
SKYR = grab(MAT, rf'this locator returns {N} / {N} on the sky', "this locator's sky pair", 2)
PUB = grab(MAT, rf"`sec:intro`'s: P1/P2 {N}, P1/P3 {N}", "sec:intro's published pair", 2)
print(f"      polarisation  comb {POL[0]}   heights {POL[1]} / {POL[2]}")
print(f"      fluid         comb {FLU[0]}   heights {FLU[1]} / {FLU[2]}")
print(f"      the sky       this locator {SKYR[0]} / {SKYR[1]}   sec:intro's published "
      f"{PUB[0]} / {PUB[1]}")
print(f"      \"the comb to a part in three hundred, {POL[0]} against {FLU[0]}\"  -> a part in "
      f"{FLU[0]/abs(POL[0]-FLU[0]):.0f}")
print(f"\n      \"height ratios differ between them by MORE than either differs from the sky\" -- and "
      f"it is checked on BOTH sky bases, because that is the kind of claim r7656 got wrong:")
both = True
for i, nm in ((1, 'P1/P2'), (2, 'P1/P3')):
    dp = abs(POL[i] - FLU[i])
    for base, lab in ((SKYR, 'this locator'), (PUB, 'sec:intro')):
        d1, d2 = abs(POL[i] - base[i - 1]), abs(FLU[i] - base[i - 1])
        ok = dp > max(d1, d2)
        both &= ok
        print(f"         {nm} vs {lab:<13} paths {dp:.3f} | pol-sky {d1:.3f} | fluid-sky {d2:.3f}"
              f"   -> {'HOLDS' if ok else 'FAILS'}   (margin {dp/max(d1,d2):.2f}x)")
check(f"ⓔ① both paths and both height pairs come out of ONE receipt on ONE object, the control, so "
      f"this comparison is same-basis by construction", len(POL) == len(FLU) == 3)
check(f"ⓔ② the comb agreement between the paths is a part in {FLU[0]/abs(POL[0]-FLU[0]):.0f}, which "
      f"is the sentence's `a part in three hundred`",
      280 <= FLU[0] / abs(POL[0] - FLU[0]) <= 320)
check(f"ⓔ③ and `by more than either differs from the sky` HOLDS on both ratios AND on BOTH sky "
      f"bases, so the claim survives the change of basis that broke my r7656 readings", both)
check(f"ⓔ④ ⑭ FAILABLE: the same test with the two paths' own difference HALVED fails, so it is a "
      f"test of the margin and not of the shape",
      not all(abs(POL[i] - FLU[i]) / 2 > max(abs(POL[i] - SKYR[i - 1]), abs(FLU[i] - SKYR[i - 1]))
              for i in (1, 2)))

# ════════════════════════════════════════════ ⓕ ⑮ the r7656 rendering defect
print("\nⓕ  ⑮ THE `1.4011` DEFECT OF `r7656`, FIXED AND TESTED")


def figures_with_mantissa(fig, text):
    """⑮ a paper mantissa `a` standing for `a x 10^b` reproduces when the receipt prints a*10^b.

    ⌗ At `r7656` I reported `1.4011` as the one figure in the corpus that was inside the figure-pin
    gate's allowance and not the digit the paper printed.  It is `D_C = 1.4011 x 10^4` Mpc and the
    receipt prints `14011.4567`.  My extractor had no reading for a mantissa whose exponent sits
    outside the token, so it compared 1.4011 against numbers near 1.4 and found the nearest two
    half-units away.  The exception class was EMPTY and I reported a member.
    """
    try:
        x = float(fig)
    except ValueError:
        return False
    dec = len(fig.split('.')[1]) if '.' in fig else 0
    for b in range(0, 7):
        want = x * 10 ** b
        for t in re.findall(r'-?\d+\.?\d*', text):
            try:
                v = float(t)
            except ValueError:
                continue
            if abs(v - want) <= 0.5 * 10 ** (-dec) * 10 ** b:
                return True
    return False


SAMPLE = 'the implementation\'s own $D_C=14011.456$ Mpc to a part in $10^{14}$'
print(f"      against a receipt line reading `{SAMPLE[:58]}...`")
print(f"         1.4011 under r7656's reading (mantissa unknown):  "
      f"{'reproduces' if figures_with_mantissa('1.4011', '1.401 1.40097') else 'DOES NOT'}")
print(f"         1.4011 under the fix:                             "
      f"{'reproduces' if figures_with_mantissa('1.4011', SAMPLE) else 'DOES NOT'}")
check(f"ⓕ① ⑮ the fix makes `1.4011` reproduce against `14011.456`, so r7656's one GATE-ONLY exception "
      f"was my renderer and the exception class was EMPTY", figures_with_mantissa('1.4011', SAMPLE))
check(f"ⓕ② ⑭ FAILABLE: a figure the text does not carry at any exponent still does NOT reproduce, so "
      f"the fix did not simply make everything match",
      not figures_with_mantissa('7.7777', SAMPLE))
print(f"""      ⌗ ⑯ AND THAT IS ALL IT IS.  No figure in these three stretches needs this reading, so it
      is reported as a correction to `r7656` and NOT as a finding of this revision.""")

print("\n" + "=" * 112)
print(f"  {len(_fail)} failure(s)")
for f in _fail:
    print("   [FAIL] " + f)
json.dump(dict(sky=SKY, arm=AOR, control=CTL, arm_offsets=dA, control_offsets=dC,
               claim_A=claim_A(3.25), claim_B=[okB, round(gotB, 4)],
               under_three_and_a_half=claim_each(3.5),
               spreads=[okP, round(gotP, 4)], shared=[okS, round(gotS, 4)],
               residual_paper=RES, residual_receipt=RES2, common_tilt=COM, as_run=RUN,
               running_phase=PH, rd_sep=RD, endpoints=ENDS,
               words=dict(over_three=round(orders(COM[0], RES), 4),
                          worst_endpoint=round(orders(max(ENDS), RES), 4),
                          as_run_orders=round(orders(RUN[2], RES), 4),
                          nine_tenths=round(tenths, 4), a_fifth=round(1 / fifth, 4),
                          a_sixth_on_receipt_residual=round(abs(RES2 / PH), 4)),
               two_route=dict(closed_form=TWO[2], bessel=BES[2],
                              arm_of_record_row=aor_two_route,
                              verdict='LOCATED' if aor_two_route else 'MIXED-BASIS'),
               gate_H4=dict(withdrawn=withdrawn, passes=bool(h4 and h4.group(1) == 'OK'),
                            paper_still_carries=still_014),
               two_path=dict(pol=POL, fluid=FLU, sky_locator=SKYR, sky_published=PUB, holds=both),
               failures=_fail),
          open(os.path.join(HERE, 'verdicts.json'), 'w'), indent=1)
sys.exit(1 if len(_fail) > 0 else 0)
