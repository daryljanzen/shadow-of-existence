#!/usr/bin/env python3
"""P07 receipt -- ⛭⛭⛭ THE FOURTH SEGMENT MOVES TWO CAPTION CLAUSES AND NO DRAWN CURVE, BECAUSE THE
SHIFT IS FOUR PARTS IN TEN THOUSAND OF THE BAND'S OWN EXTENT.

** WHAT THIS IS FOR. **  `r7797` asked whether the lap figure's panels (C) or (F) draw anything the
fourth segment changes -- which panel and what moves, or a check saying none does.  This receipt
answers it with the number that decides it, and the answer has two halves that must not be collapsed
into one: ** TWO CAPTION CLAUSES ARE FALSE ON THE BENT CUT, AND NO DRAWN CURVE MOVES BY AS MUCH AS THE
FIGURE CAN CARRY. **

** WHICH OBJECT EACH PANEL DRAWS, SETTLED BEFORE ANYTHING IS SAID ABOUT MOVEMENT. **  A panel is not
one object.  Ⓐ establishes from the captions themselves that the CURVES of both panels are the vacuum
continuation -- (C) states the law with the imaginary part held at `-pi alpha/3`, (F) fixes the lift at
`Re tau = 0` with the imaginary part running `-pi alpha/3 -> 0` -- while (C)'s caption ALSO carries an
actual-history clause, radiation bending the cut so the rate carries it.  So the panels mix two
objects, and an answer of the form "the panel changes" given without that split would be answering
about an object the question never fixed.

** THE TWO CLAUSES THAT ARE FALSE ON THE BENT CUT. **  Each says the lift reaches the branch point:
(C) that the lift from the comoving turnaround "up to r = 0" collapses onto the single vertical
segment, and (F) that the shaded band is the stretch "across which r climbs from the turnaround through
r = 0".  On the bent cut the radicand is POSITIVE below its inner zero (Ⓑ⑤), so the lift ENDS at
`K/2M` and a fourth segment carries the rest in real time.  Both clauses are located and MATCHED, so
they are live text and not a memory of an earlier draft.

** AND THE DRAWING DOES NOT MOVE, WHICH IS A MEASUREMENT AND NOT A CONCESSION. **  The band's upper
endpoint moves off `r = 0` by `3.9512e-4` of the band's own `r`-extent (Ⓒ⑥) and the fourth segment
advances real cosmic time by `0.054594` Mpc, a hundred-thousandth of the lift's imaginary extent (Ⓒ⑦).
Ⓒ⑨ registers BOTH outcomes in advance against one part in a thousand of the panel's range and asserts
the comparison, not a branch: the shift falls below it, so the answer to the order is that the
wording moves and the curve does not.

** WHAT SURVIVES, AND IT IS WORTH SAYING. **  Panel (F)'s vertical tangent at the branch point survives
(Ⓒ⑧): on the bent cut the approach exponent is `1/2` rather than dust's `2/3`, and `1/2 < 1` still
sends `dr/d(real time)` to infinity.  What changed is not the tangent but the stretch that reaches it --
no longer the lift.

COMPUTES: scope -- what is derived here and what is received.  `alpha`, `r_0`, the Nariai offset `2M`
and the radiation coefficient `K` are DERIVED below from the corpus's published pair and the photon
density.  Nothing is fitted and no free parameter is introduced.
  INPUT   H_0 = 68.6, Omega_m = 0.2973   -- corpus measured, the published pair
  INPUT   omega_gamma = 4.15e-5 h^-2     -- corpus measured, from the microwave background temperature

** WHAT IT DOES NOT CLAIM. **  It does not ask for the caption's "three closed-form segments" to
change: `r7797` ruled that is about the vacuum lap, and the ruling is accepted rather than
re-litigated.  It does not redraw a figure or touch a figure script.  It does not claim the layers'
deposit clause moves -- Ⓓ⑩ DECIDES that it does not, and says on what ground.  And it does not touch
`thm:bead`, the vacuum curve's theorem.

⌗ ONE NUMBER IS DELIBERATELY NOT CLAIMED.  The fourth segment's share of `pi alpha / 3` comes back as
`1.00001e-5`, which is a part in a hundred thousand to five figures.  ** The registration did not
predict it, nothing here derives it, and r7796's own guard applies: a number that matches a number is
a coincidence until the match is derived. **  It is printed because suppressing it would be worse, and
it is claimed as nothing.

Built r7798 (node 60), on order r7797 ②, from r7778, r7780 and r7796.  Stated for reversal.
"""
import io
import math
import os
import re
import sys

import numpy as np
import mpmath as mp

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
fails = []


def check(label, ok):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    if not ok:
        fails.append(label)


def head(t):
    print('\n' + '=' * 100 + f"\n  {t}\n" + '=' * 100)


def body(name):
    """the paper's source with whitespace collapsed, so a literal straddling a LaTeX line wrap is
    still read -- a pin that fails on where the source breaks its lines is a defect in the pin"""
    raw = io.open(os.path.join(ROOT, 'corpus', name), encoding='utf-8').read()
    return ' '.join(raw.split())


# ------------------------------------------------------- the constants, DERIVED (see COMPUTES above)
CLIGHT = 299792.458
H0, OM = 68.6, 0.2973
OMR = 4.15e-5 / (H0 / 100.0) ** 2
OL = 1.0 - OM
hub = H0 / CLIGHT
X0 = (2 * OL / OM) ** (1 / 3)
ALPHA = 1.0 / (hub * np.sqrt(OL))
R0 = ALPHA * X0 / np.sqrt(3.0)
TWOM = 2 * R0 ** 3 / (ALPHA ** 2 * X0 ** 3)
KRAD = hub ** 2 * OMR * R0 ** 4
RT = (TWOM * ALPHA ** 2) ** (1 / 3)

mp.mp.dps = 60
A_, M_, K_ = mp.mpf(ALPHA), mp.mpf(TWOM), mp.mpf(KRAD)
S0 = K_ / M_
BOUND = mp.pi * A_ / 3


def rad(s, K=None):
    """(dr/dtau)^2 at r = -s with s > 0:  -2M/s + K/s^2 + s^2/alpha^2.
    NEGATIVE on the lift, POSITIVE where real cosmic time advances."""
    k = K_ if K is None else mp.mpf(K)
    return -M_ / s + k / s ** 2 + s ** 2 / A_ ** 2


def drad(s, K=None):
    k = K_ if K is None else mp.mpf(K)
    return M_ / s ** 2 - 2 * k / s ** 3 + 2 * s / A_ ** 2


def real_advance(lo, hi):
    """the REAL cosmic time across (lo, hi) where the radicand is positive.  `hi` is a SIMPLE zero,
    so the integrand goes as |s - hi|^(-1/2) and u^2 = hi - s removes it exactly.
    ⌗ The guard is on the radicand's VALUE and not on u == 0: at 60 digits a quadrature node can be
      close enough to the end that hi - u**2 rounds TO it, where the radicand is exactly 0."""
    L = mp.sqrt(hi - lo)
    lim = 1 / mp.sqrt(abs(drad(hi)))

    def g(u):
        s = hi - u ** 2
        v = rad(s)
        return lim if v <= 0 else u / mp.sqrt(v)
    return 2 * mp.quad(g, [0, L])


print(f"\n  derived: alpha = {ALPHA:.3f} Mpc   r_0 = {R0:.3f} Mpc   2M = {TWOM:.4f} Mpc"
      f"   K = {KRAD:.3f} Mpc^2")
print(f"           the vacuum comoving turnaround r_t = {RT:.6f} Mpc     K/2M = {float(S0):.9f} Mpc")

P7 = body('CR_framework.tex')
SENTS = [' '.join(s.split()) for s in re.split(r'(?<=[.!?])\s+', P7) if s.strip()]


def resolve(key):
    """MATCHED   -- in print, inside a sentence of the paper;
       WITHDRAWN -- in the paper's FULL TEXT but in no sentence the splitter produced;
       STALE     -- nowhere in the full text.
    ** What is searched: the whole of `corpus/CR_framework.tex`, whitespace-flattened. **
    ⌗ Three states and not two, because a two-state arm returns the same word for a sentence that is
      WRONG and one that has been DELETED -- which is what happened to `r7768`'s arm 6 at `r7767`."""
    if any(key in s for s in SENTS):
        return 'MATCHED'
    return 'WITHDRAWN' if key in P7 else 'STALE'


def show(label, key):
    st = resolve(key)
    print(f"      {label:<52s} -> {st}")
    hit = next((s for s in SENTS if key in s), '')
    if hit:
        i = hit.find(key)
        print('        "...' + hit[max(0, i - 95):i + 160] + '..."')
    return st


# ===================================================== Ⓐ WHICH OBJECT EACH PANEL'S CURVES ARE
head("A -- WHICH OBJECT EACH PANEL DRAWS, SETTLED BEFORE ANYTHING IS SAID ABOUT MOVEMENT")
a1 = show("(C) fixes its curves to the VACUUM law",
          r'with $\operatorname{Im}\tilde\tau$ held at $-\pi\alpha/3$')
check("Ⓐ①  panel (C)'s caption states the law its curves follow, with the imaginary part held at "
      "-pi alpha/3 -- so those curves are the VACUUM continuation and not the bent cut's, which is "
      "what makes the question about them a question about a clause rather than a curve",
      a1 == 'MATCHED')

a2 = show("(F) fixes the lift to the VACUUM run", r'running $-\pi\alpha/3\to0$')
check("Ⓐ②  panel (F)'s caption fixes the lift at Re tau = 0 with the imaginary part running "
      "-pi alpha/3 -> 0, the same vacuum object",
      a2 == 'MATCHED')

a3 = show("(C) ALSO carries an actual-history clause", 'bends the cut in epoch so that the rate '
          'carries it')
check("Ⓐ③  and (C)'s caption ALSO says radiation bends the cut so the rate carries it -- an "
      "actual-history clause in a caption whose curves Ⓐ① just fixed as vacuum.  ⇒ THE PANEL MIXES "
      "TWO OBJECTS, and that is why the answer has to name which of them moves",
      a3 == 'MATCHED')

# ===================================================== Ⓑ THE FOURTH SEGMENT, ON THE OBJECT ITSELF
head("B -- THE FOURTH SEGMENT, ESTABLISHED FROM THE RADICAND'S SIGN AND NOT FROM THE LABEL")
rt_v = mp.findroot(lambda s: rad(s, 0), mp.mpf(RT))
vac = [(f, rad(rt_v * mp.mpf(f), 0)) for f in
       ('1e-9', '1e-6', '1e-3', '0.01', '0.1', '0.3', '0.5', '0.7', '0.9', '0.99', '0.999')]
for f, v in vac:
    print(f"      VACUUM  s/r_t = {f:>7s} :  radicand = {mp.nstr(v, 8)}")
check("Ⓑ④  on the VACUUM cut the radicand is strictly negative at every sample from the branch "
      "point to the comoving turnaround -- one lift, reaching the branch point, and no fourth "
      "segment, which is the state both captions describe",
      all(v < 0 for _, v in vac))

s_in = mp.findroot(lambda s: rad(s), S0)
s_out = mp.findroot(lambda s: rad(s), mp.mpf(RT) * mp.mpf('0.9995'))
below = [(f, rad(s_in * mp.mpf(f))) for f in ('1e-6', '1e-3', '0.01', '0.1', '0.5', '0.9', '0.99')]
inside = [(f, rad(s_in + (s_out - s_in) * mp.mpf(f))) for f in
          ('0.001', '0.01', '0.1', '0.5', '0.9', '0.99', '0.999')]
print(f"\n      BENT zeros: inner = {mp.nstr(s_in, 16)}   outer = {mp.nstr(s_out, 16)} Mpc")
for f, v in below:
    print(f"      BENT, BELOW the inner zero   s/s_in = {f:>7s} :  radicand = {mp.nstr(v, 8)}")
for f, v in inside:
    print(f"      BENT, BETWEEN the two zeros  t     = {f:>7s} :  radicand = {mp.nstr(v, 8)}")
check("Ⓑ⑤  on the BENT cut the radicand is negative only strictly BETWEEN its two zeros and "
      "strictly POSITIVE below the inner one -- so the lift ENDS at the inner zero and a fourth "
      "segment carries the rest of the way to the branch point in real cosmic time",
      all(v > 0 for _, v in below) and all(v < 0 for _, v in inside))

# ===================================================== Ⓒ WHAT MOVES, WITH THE NUMBERS
head("C -- WHAT MOVES, AND THE NUMBER THAT DECIDES WHETHER IT MOVES IN THE DRAWING")
frac = s_in / rt_v
frac_mantissa = float(frac) * 1e4
print(f"      the band's upper endpoint moves off r = 0 by {mp.nstr(s_in, 12)} Mpc")
print(f"      as a fraction of the band's own r-extent (r_t = {mp.nstr(rt_v, 10)}): "
      f"{mp.nstr(frac, 12)}")
print(f"      in the MANTISSA the citing sentence prints: {frac_mantissa:.6f} against 3.9512")
check("Ⓒ⑥  the shaded band's upper endpoint stands off the branch point by 3.9512 parts in ten "
      "thousand of the band's own r-extent -- pinned both as the fraction and as the mantissa the "
      "sentence sets in type",
      abs(float(frac) - 3.9512e-4) < 5e-8 and abs(frac_mantissa - 3.9512) < 1e-4)

adv = real_advance(mp.mpf(0), s_in)
print(f"\n      the fourth segment's advance in real cosmic time = {mp.nstr(adv, 14)} Mpc")
print(f"      against pi alpha / 3 = {mp.nstr(BOUND, 14)} Mpc :  share = {mp.nstr(adv / BOUND, 8)}")
print("      ⌗ NOT CLAIMED: that share is 1.00001e-5, a part in a hundred thousand to five figures.")
print("        The registration did not predict it, nothing here derives it, and `r7796`'s own guard")
print("        applies -- a number that matches a number is a coincidence until the match is")
print("        derived.  It is printed because suppressing it would be worse, and claimed as")
print("        nothing.  ⇒ A COINCIDENCE REPORTED AS ONE IS NOT A FINDING.")
check("Ⓒ⑦  the fourth segment advances real cosmic time by 0.054594 Mpc -- finite and non-zero, so "
      "it is neither still a lift nor an infinite reach, and the branch point is attained in finite "
      "real time on the bent cut",
      abs(float(adv) - 0.054594) < 2e-6 and adv > 0 and mp.isfinite(adv))

print()
pts = []
for e in (14, 13, 12, 11, 10, 9, 8):
    s = s_in * mp.mpf(10) ** (-e)
    t = mp.quad(lambda x: 1 / mp.sqrt(rad(x)), [mp.mpf(0), s])
    pts.append((t, s))
exps = [mp.log(pts[i + 1][1] / pts[i][1]) / mp.log(pts[i + 1][0] / pts[i][0])
        for i in range(len(pts) - 1)]
for i, p in enumerate(exps):
    print(f"      the approach exponent over s/s_in = 1e-{14 - i} .. 1e-{13 - i} :  p = "
          f"{mp.nstr(p, 10)}")
print("      ⇒ r ~ t^p with p = 1/2, so dr/d(real time) ~ t^(p-1) DIVERGES, since p < 1")
check("Ⓒ⑧  panel (F)'s vertical tangent at the branch point SURVIVES on the bent cut: the approach "
      "exponent is 1/2 rather than dust's 2/3, and 1/2 is still below 1, so the derivative still "
      "diverges.  ⇒ WHAT CHANGED IS NOT THE TANGENT BUT THE STRETCH THAT REACHES IT -- no longer "
      "the lift",
      all(abs(p - mp.mpf('0.5')) < mp.mpf('1e-6') for p in exps))

print()
c_clause = show("(C): the lift up to r = 0 is ONE vertical segment",
                r'up to $r=0$ collapses here onto the single vertical segment')
f_clause = show("(F): r climbs from the turnaround THROUGH r = 0",
                r'across which $r$ climbs from the turnaround through $r=0$')
RESOLVE_LIMIT = 1e-3                      # one part in a thousand of the panel's r-range
moves_drawing = float(frac) >= RESOLVE_LIMIT
print(f"\n      THE VERDICT, both branches registered in advance:")
print(f"        the endpoint shift            = {mp.nstr(frac, 10)} of the panel's r-range")
print(f"        one part in a thousand        = {RESOLVE_LIMIT}")
print(f"        ⇒ branch {'(i): THE DRAWING MOVES' if moves_drawing else '(ii): THE DRAWING DOES NOT MOVE, THE WORDING DOES'}")
check("Ⓒ⑨  THE ORDER'S QUESTION, ANSWERED BY THE COMPARISON AND NOT BY A PREFERENCE: the shift is "
      "below one part in a thousand of the panel's range, so NO DRAWN CURVE MOVES BY AS MUCH AS THE "
      "FIGURE CAN CARRY -- while TWO CAPTION CLAUSES, one in each panel, say the lift reaches the "
      "branch point and are false on the bent cut.  Both clauses are MATCHED, so they are live text",
      (not moves_drawing) and c_clause == 'MATCHED' and f_clause == 'MATCHED'
      and float(frac) < RESOLVE_LIMIT)

# ===================================================== Ⓓ THE CLAUSE WHOSE SUBJECT IS NOT THE BEAD
head("D -- THE ONE CLAUSE WHOSE SUBJECT IS NOT THE BEAD, DECIDED RATHER THAN ASSUMED")
d = show("(C): the layers pile onto the branch point",
         'pile onto the branch point, depositing the plasma')
print("      TWO READINGS, as registered:")
print("        (i)  the clause's locus is set by the bead's radicand, so the fourth segment now")
print("             lies between the lift and the deposit, and the clause's geometry gains a stretch;")
print("        (ii) the clause's subject is the S^3 LAYERS, whose locus the bead's radicand does not")
print("             set, so the clause is untouched.")
print("      ⇒ (ii) IS ASSERTED, on this ground: the radicand's sign fixes where the BEAD's lift")
print("        ends, and the bead still attains r = 0 -- Ⓒ⑦ measures the real time it takes to get")
print("        there as finite.  The deposit is AT the branch point either way.  What the fourth")
print("        segment inserts is between the LIFT'S END and the branch point, not between the")
print("        deposit and anything.  ⌗ The guard the registration named: before two stretches are")
print("        identified by one label, check how many-to-one the label is on the object -- 'the")
print("        approach to the branch point' names the lift on the vacuum cut and the fourth")
print("        segment on the bent one, and only the first of those is the lift.")
check("Ⓓ⑩  the layers' deposit clause is located MATCHED and DECIDED untouched -- reading (ii) -- "
      "because the bead attains the branch point in finite real time on the bent cut too, so the "
      "locus the clause names is unmoved; it is the two LIFT clauses that are false, not this one",
      d == 'MATCHED' and mp.isfinite(adv) and adv > 0)

head("THE COUNT, THE SCOPE, AND WHAT IS NOT CLAIMED")
print("      REGISTERED ARMS: 10 -- Ⓐ①②③ Ⓑ④⑤ Ⓒ⑥⑦⑧⑨ Ⓓ⑩; this is ⑩, and CHECKS RUN: 10.")
print("      the TWO inputs are declared in the COMPUTES header; nothing here is fitted.")
print("      NOT CLAIMED: that the caption's 'three closed-form segments' should change -- r7797")
print("      ruled it is about the vacuum lap and the ruling is accepted; any redraw of a figure or")
print("      change to a figure script; that the layers' deposit clause moves, which Ⓓ⑩ decides it")
print("      does not; and the share 1.00001e-5, printed and claimed as nothing.")
print("      Nothing here touches `thm:bead`, the VACUUM curve's theorem.")

print('\n' + '=' * 90)
if fails:
    print(f"  ⛔ {len(fails)} CHECK(S) FAILED:")
    for x in fails:
        print(f"     - {x}")
    print('=' * 90)
    sys.exit(1)
print(f"""
  ALL CHECKS PASS.

  THE ORDER'S ANSWER, in the two halves it has to have.

  TWO CAPTION CLAUSES ARE FALSE ON THE BENT CUT, one in each panel.  (C)
  says the lift from the comoving turnaround up to r = 0 collapses onto the
  single vertical segment; (F) says the shaded band is the stretch across
  which r climbs from the turnaround THROUGH r = 0.  On the bent cut the
  radicand turns positive below its inner zero, so the lift ends at
  {float(s_in):.6f} Mpc and a fourth segment carries the remaining distance in
  {float(adv):.6f} Mpc of real cosmic time.

  AND NO DRAWN CURVE MOVES.  The band's upper endpoint stands off the branch
  point by {float(frac):.4e} of the band's own r-extent -- four parts in ten
  thousand, below the one part in a thousand a figure at this width can carry.
  The registration enumerated both branches before either was measured, and
  this is the branch the number chose.

  WHAT SURVIVES: panel (F)'s vertical tangent.  The approach exponent is 1/2
  on the bent cut against dust's 2/3, and 1/2 is still below 1, so the
  derivative still diverges at the branch point.  What changed is not the
  tangent but the stretch that reaches it.

  AND ONE CLAUSE IS DECIDED UNTOUCHED: the layers piling onto the branch point.
  Its subject is the layers, the bead still attains r = 0 in finite real time,
  and the fourth segment is inserted between the LIFT'S END and the branch
  point rather than between the deposit and anything.
""")
print('=' * 90)
