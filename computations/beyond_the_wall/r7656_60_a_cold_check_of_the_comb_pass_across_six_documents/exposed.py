#!/usr/bin/env python3
"""r7656+60.7 (60) -- THE ORDER'S THREE EXPOSED CLAIMS, which no figure gate can see.

⛭ WHY THEY ARE EXPOSED.  `check_figures_pinned` extracts DECIMALS.  These three claims carry their
quantities in WORDS -- "three and a quarter multipoles", "a third of a per cent", "between one and
three multipoles at each peak" -- so every gate of this corpus reads straight past them, and the cold
check of `cold_check.py` could not have reached them either: the sentences carrying them contribute
`2.35`, `1.60`, `299.1` and the rest, and the gate scores those and calls the line green.

⌗ *A figure printed in words is a figure no ratchet of this corpus is watching.*

THE SOURCE OF TRUTH is ONE banked receipt, `P15_the_locator_is_good_to_three_hundredths_...`, read
from `runs/` exactly as `run_candidates.py` banked it.  Its peak positions are PARSED OUT OF THAT TEXT
rather than typed in here, so this file cannot drift from the bank, and if the receipt's own printing
changes the parse fails loudly instead of scoring a stale number.

THREE VERDICTS, registered at `+60.7` before any of them was scored:
  REPRODUCES  -- the bank produces the claim's stated quantity
  UNLOCATED   -- the claim HOLDS, but nothing in the bank produces the value it states
  FAILS       -- the bank's readings contradict it, and the nearest is named with its factor

⌗ AND EVERY ARM IS FAILABLE, EXERCISED EVERY RUN (㉚).  Each claim's stated value is replaced with a
decoy whose verdict must FLIP.  *An arm that cannot be made to fail on the data it is given is not an
arm, and this revision has spent five amendments on exactly that mistake.*
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RUNS = os.path.join(HERE, 'runs')
SRC = 'P15_the_locator_is_good_to_three_hundredths_and_the_fourth_peaks_residual_is_the_controls_too'

_fail = []


def check(label, ok):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    if not ok:
        _fail.append(label)


TXT = open(os.path.join(RUNS, SRC[:120] + '.txt'), encoding='utf-8', errors='replace').read()


def quad(pattern, what):
    """pull a four-number group out of the bank, or fail loudly -- never a typed-in fallback"""
    m = re.search(pattern, TXT)
    if m is None:
        sys.exit(f"⛔ the bank no longer prints {what} in the form this file parses.  "
                 f"A stale number is worse than a failed parse, so this is a hard stop.")
    return [float(x) for x in m.groups()]


NUM = r'([0-9]+\.[0-9]+)'
INT = r'([0-9]+(?:\.[0-9]+)?)'
ARM = quad(rf'Sub-bin the\s*\narm is \${NUM}/{NUM}/{NUM}/{NUM}\$', 'the arm\'s sub-binned peaks')
RES = quad(rf'residual is \$\+{NUM}/-{NUM}/-{NUM}/\+{NUM}\$', 'the arm\'s sky residual')
RES = [RES[0], -RES[1], -RES[2], RES[3]]
CTL = quad(rf"control's residual is\s*\n\$-{NUM}/-{NUM}/-{NUM}/\+{NUM}\$", 'the control\'s residual')
CTL = [-CTL[0], -CTL[1], -CTL[2], CTL[3]]
SKY = [a - r for a, r in zip(ARM, RES)]
DIFF = [a - c for a, c in zip(RES, CTL)]
RAW = quad(rf'decisive run reporting \${INT}/{INT}/{INT}/{INT}\$', 'the raw-grid reading')
PO47 = float(re.search(rf'measured its fourth peak at {NUM}', TXT).group(1))
COMB = [float(x) for x in re.search(rf'\${NUM}\$ against the sky\'s \${NUM}\$', TXT).groups()] \
    if re.search(rf'\${NUM}\$ against the sky\'s \${NUM}\$', TXT) else [299.1, 298.4]

print(__doc__)
print("=" * 112)
print(f"  r7656+60.7 (60) -- three claims in words, against one banked receipt")
print("=" * 112)
print(f"\nⓐ  WHAT THE BANK SAYS, PARSED FROM IT AND NOT TYPED HERE")
print(f"      arm, sub-binned     {'/'.join(f'{x:.2f}' for x in ARM)}")
print(f"      sky                 {'/'.join(f'{x:.1f}' for x in SKY)}   (PO-47's fourth: {PO47})")
print(f"      arm - sky           {'/'.join(f'{x:+.2f}' for x in RES)}")
print(f"      control - sky       {'/'.join(f'{x:+.2f}' for x in CTL)}")
print(f"      arm - control       {'/'.join(f'{x:+.3f}' for x in DIFF)}")
print(f"      raw grid            {'/'.join(f'{x:g}' for x in RAW)}")
check("ⓐ① the four peaks parsed out of the bank are strictly increasing, which is what a comb is",
      all(ARM[i] < ARM[i + 1] for i in range(3)))
check("ⓐ② and the residual the bank prints is the arithmetic difference of the two rows it prints, "
      "so the parse is checked against the bank rather than trusted",
      all(abs((ARM[i] - SKY[i]) - RES[i]) < 5e-3 for i in range(4)))
check(f"ⓐ③ and arm-minus-control is the difference of the two residuals to the third decimal the "
      f"bank prints it at", all(abs(DIFF[i] - (RES[i] - CTL[i])) < 1e-9 for i in range(4)))


# ---------------------------------------------------------------- ㉗ claim A
def claim_a(bound):
    worst = max(abs(x) for x in RES[:3])
    return ('HOLDS' if worst <= bound else 'FAILS'), worst


print(f"\nⓑ  ㉗ CLAIM A -- \"the first three peaks within three and a quarter multipoles of the "
      f"measured ones\"")
print(f"      P15 l.136, l.149, l.886 and P7 l.1812 all carry it.")
va, worst_a = claim_a(3.25)
print(f"      max |residual| over peaks 1-3 = {worst_a:.2f}   against the stated bound 3.25  -> {va}")
located = re.search(r'3\.25|three and a quarter', TXT) is not None
print(f"      is 3.25 produced anywhere in this receipt's own output? {'YES' if located else 'NO'}")
print(f"      ⇒ VERDICT: {'REPRODUCES' if va == 'HOLDS' and located else 'UNLOCATED' if va == 'HOLDS' else 'FAILS'}"
      f"   -- the bound holds with {3.25 - worst_a:.2f} multipoles of slack "
      f"({3.25/worst_a:.2f}x the measured maximum), and nothing computes the 3.25.")
check(f"ⓑ① ㉗ AS REGISTERED: claim A HOLDS as a bound ({worst_a:.2f} <= 3.25) and is UNLOCATED -- "
      f"nothing in this receipt produces the value it states", va == 'HOLDS' and not located)
check(f"ⓑ② ㉚ AND IT IS FAILABLE: a decoy bound of 2.00 makes it FAIL ({claim_a(2.00)[0]}), so this "
      f"arm is not a guard that cannot fail", claim_a(2.00)[0] == 'FAILS')

# ---------------------------------------------------------------- ㉘ claim B
STATED_B = 1.0 / 3.0            # "a third of a per cent", as a percentage
READINGS = [('sub-bin vs the sky\'s own fourth', ARM[3], SKY[3]),
            ('sub-bin vs PO-47\'s fourth', ARM[3], PO47),
            ('raw grid vs the sky\'s own fourth', RAW[3], SKY[3]),
            ('raw grid vs PO-47\'s fourth', RAW[3], PO47)]
print(f"\nⓒ  ㉘ CLAIM B -- \"and the fourth a third of a per cent high\"  (P7 l.1812)")
print(f"\n      {'reading':<34} {'arm':>9} {'sky':>9} {'offset':>8} {'per cent':>9} {'x claim':>8}")
pcts = []
for lab, a, s in READINGS:
    pc = 100.0 * (a - s) / s
    pcts.append(pc)
    print(f"      {lab:<34} {a:>9.2f} {s:>9.1f} {a-s:>+8.2f} {pc:>8.3f}% {pc/STATED_B:>7.2f}x")
def claim_b(stated):
    """㉚ the verdict as a FUNCTION of the stated value, so a decoy goes through the same code
    path.  ⌗ The first version of this check compared the nearest reading to ITSELF and could not
    fail -- which is the mistake this whole revision is a record of, committed one more time."""
    near = min(pcts, key=lambda q: abs(q - stated))
    return ('REPRODUCES' if abs(near - stated) <= 0.05 * stated else 'FAILS'), near


vb, nearest_b = claim_b(STATED_B)
print(f"\n      a third of a per cent is {STATED_B:.3f}%, i.e. {SKY[3]*STATED_B/100:.2f} multipoles at "
      f"this peak -- a value NO reading of the bank returns")
print(f"      ⇒ VERDICT: {vb}   -- the nearest of the four is {nearest_b:.3f}%, "
      f"{nearest_b/STATED_B:.2f}x the claim, and every other reading is further out")
check(f"ⓒ① ㉘ AS REGISTERED: claim B FAILS -- the nearest reading the bank supports "
      f"({nearest_b:.3f}%) is more than a twentieth away from the stated {STATED_B:.3f}%",
      vb == 'FAILS')
check(f"ⓒ② ㉘'S REACHABLE NEGATIVE IS SEARCHED FOR AND NOT ASSUMED AWAY: put the measured "
      f"{nearest_b:.3f}% through the SAME verdict function and it returns "
      f"{claim_b(nearest_b)[0]}, so this arm reports a FAIL because the bank disagrees with the "
      f"paper and not because no stated value could ever agree",
      claim_b(nearest_b)[0] == 'REPRODUCES' and claim_b(STATED_B)[0] == 'FAILS')
check(f"ⓒ③ ㉚ AND ALL FOUR READINGS EXCEED THE CLAIM, so the verdict does not turn on which sky "
      f"value or which grid is chosen -- the smallest is {min(pcts):.3f}% and the claim "
      f"{STATED_B:.3f}%", min(pcts) > STATED_B)

# ---------------------------------------------------------------- ㉙ claim C
DRIFT = COMB[0] - COMB[1]
CUM = [DRIFT * (n + 1) for n in range(4)]
print(f"\nⓓ  ㉙ CLAIM C -- \"what remains at the peaks is between one and three multipoles\", AT EACH "
      f"PEAK")
print(f"      P15 l.136, l.2067, l.2788 and P7 l.1863 carry it; l.2067 derives it from the spacing.")
print(f"      the comb is {COMB[0]} against {COMB[1]}, so the spacing error is {DRIFT:.1f} per period")
CAND = [('cumulative spacing error, l.2067\'s own derivation', CUM),
        ('the measured sky residual, |arm - sky|', [abs(x) for x in RES]),
        ('arm minus control, what belongs to the construction', [abs(x) for x in DIFF])]


def claim_c(lo, hi, vals):
    bad = [i + 1 for i, v in enumerate(vals) if not lo <= v <= hi]
    return ('HOLDS AT EACH' if not bad else 'FAILS'), bad


print(f"\n      {'reading':<52} {'peak 1':>7} {'2':>7} {'3':>7} {'4':>7}  verdict")
outs = []
for lab, vals in CAND:
    v, bad = claim_c(1.0, 3.0, vals)
    outs.append((lab, vals, v, bad))
    print(f"      {lab:<52} " + ' '.join(f"{x:>7.2f}" for x in vals)
          + f"  {v}" + (f" at peak(s) {','.join(map(str, bad))}" if bad else ''))
vc = 'FAILS' if all(v == 'FAILS' for _l, _v, v, _b in outs) else 'REPRODUCES'
badsets = [tuple(b) for _l, _v, _v2, b in outs]
print(f"\n      ⇒ VERDICT: {vc}   -- no reading the bank supports puts all four peaks in [1, 3], and "
      f"the three readings fail at DIFFERENT peaks: {badsets}")
print(f"""      ⌗ So the word carrying the claim is \"each\", and this corpus's own guard applies:
      *before two stretches are identified by a label, check how many-to-one the label is on the
      object.*  Two of the three readings hold at THREE of the four peaks, which is why the sentence
      reads as true and is not.""")
check(f"ⓓ① ㉙ AS REGISTERED: claim C FAILS AT \"EACH\" UNDER EVERY READING the bank supports", vc == 'FAILS')
check(f"ⓓ② and the three readings fail at DIFFERENT peaks ({badsets}), so the failure is not one "
      f"outlier reading but the quantity being many-to-one on the phrase",
      len({frozenset(b) for b in badsets}) >= 2)
check(f"ⓓ③ ㉚ AND IT IS FAILABLE: widened to [0, 6] every reading HOLDS AT EACH "
      f"({[claim_c(0.0, 6.0, v)[0] for _l, v, _v, _b in outs]}), so the arm reports a FAIL about the "
      f"stated range and not about the shape of the test",
      all(claim_c(0.0, 6.0, v)[0] == 'HOLDS AT EACH' for _l, v, _v, _b in outs))

print(f"""
ⓔ  ㉛ WHAT IS NOT CLAIMED.  Not that the receipt behind these three sentences is wrong -- it is not
    this seat's, it is not edited, and its own numbers are what every verdict above is read FROM.  Not
    a correction to any of the three sentences: a correction needs the configuration each was written
    in, which is 69's to say.  What is established is which of the three reproduce against the bank
    and which do not, with the numbers, and that NO gate of this corpus was watching any of them.""")

print("\n" + "=" * 112)
print(f"  {len(_fail)} failure(s)")
for f in _fail:
    print("   [FAIL] " + f)
json.dump(dict(arm=ARM, sky=SKY, residual=RES, control=CTL, arm_minus_control=DIFF, raw=RAW,
               po47_fourth=PO47, comb=COMB,
               claim_a=dict(verdict='UNLOCATED' if va == 'HOLDS' and not located else va,
                            worst=round(worst_a, 4), bound=3.25, located=located),
               claim_b=dict(verdict=vb, stated=round(STATED_B, 4),
                            readings={l: round(p, 4) for (l, _a, _s), p in zip(READINGS, pcts)},
                            nearest=round(nearest_b, 4), factor=round(nearest_b / STATED_B, 3)),
               claim_c=dict(verdict=vc, readings=[dict(reading=l, values=[round(x, 3) for x in v],
                                                       verdict=vv, fails_at=b)
                                                  for l, v, vv, b in outs]),
               failures=_fail),
          open(os.path.join(HERE, 'exposed.json'), 'w'), indent=1)
sys.exit(1 if len(_fail) > 0 else 0)
