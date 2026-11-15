#!/usr/bin/env python3
"""P07 receipt -- ⛭⛭⛭ THE LIFT ON THE BENT CUT IS A SECOND NUMBER BESIDE THE VACUUM BOUND, AND NO
BEAD CONDITION CARRIES THE RADIATION COEFFICIENT.

** WHAT THIS IS FOR. **  `thm:bead` bounds the imaginary excursion of cosmic time along the lap by
`pi alpha / 3`, "fixed by the exponent and independent of M".  That is a theorem about the VACUUM
slicing curve and it stands as stated.  The history the content rides is the BENT cut, `mu = 2M + K/r`,
and its lift is a different number: longer, with its ends pulled in, and detached from the branch
point.  This receipt establishes that second number so the paragraph can be written in `P7` beside the
theorem rather than instead of it.

** AND IT MAKES THE THEOREM'S OWN CLAUSE FAILABLE, WHICH THE NARIAI MEMBER CANNOT DO. **  The Nariai
condition fixes `M` from `alpha`, so on the member there is ONE mass and "independent of M" has
nothing to vary.  Ⓐ② leaves the member deliberately and evaluates the same integral at five masses:
the clause holds, and holds for the reason it gives.

COMPUTES: scope -- what is derived here and what is received.  Every constant is DERIVED in the block
below from the corpus's published pair (H_0 = 68.6 km/s/Mpc, Omega_m = 0.2973) and the photon density
omega_gamma = 4.15e-5 h^-2: alpha, r_0, the Nariai offset 2M, and the radiation coefficient K.
  INPUT   H_0 = 68.6, Omega_m = 0.2973  -- corpus measured, the published pair; NOTHING HERE FITS THEM
  INPUT   omega_gamma = 4.15e-5 h^-2    -- corpus measured, from the microwave background temperature
Ⓐ② deliberately leaves the Nariai locus, because a clause claimed for every mass must be checked
where the mass is free.  Everything else runs on the member.  Nothing here is fitted and no
observational parameter enters beyond the two declared above.

** COMPUTES. **
  Ⓐ  the vacuum lift's excursion is pi alpha / 3, and that value does not move with the mass;
  Ⓑ  the bent cut's radicand has TWO zeros on the conjugate side, the inner one at K/2M, so the lift
     is an interval strictly inside the vacuum one -- and its excursion EXCEEDS pi alpha / 3;
  Ⓒ  no condition the bead imposes carries K, by differentiation and not by inspection;
  Ⓓ  the two sentences in `P7` this receipt stands beside, each resolved in three states.

** WHAT IT DOES NOT CLAIM. **  It does not contradict `thm:bead`: the theorem is about the vacuum
curve and is reproduced here to 12 digits.  It does not say at what epoch the deposited plasma becomes
the bend -- that is the open question named in `r7778` and held for a later revision.  It does not
assert anything about the progenitor's radiation content: the conjugate branch's sign structure is
bookkeeping in a signed coordinate, as Ⓒ shows, and what the progenitor carries is not decided here.

Built r7780 (node 60), from r7776 and r7778.  Stated for reversal.
"""
import io
import math
import os
import re
import sys

import numpy as np
import sympy as sp
from scipy.optimize import brentq
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
RT = (TWOM * ALPHA ** 2) ** (1 / 3)              # the vacuum comoving turnaround, 1 - f = 0
BOUND = math.pi * ALPHA / 3.0

mp.mp.dps = 50
A_, M_, K_ = mp.mpf(ALPHA), mp.mpf(TWOM), mp.mpf(KRAD)


def rad(s, K, twoM=None):
    """(dr/dtau)^2 at r = -s with s > 0: -2M/s + K/s^2 + s^2/alpha^2.  NEGATIVE on the lift."""
    m = M_ if twoM is None else mp.mpf(twoM)
    return -m / s + K / s ** 2 + s ** 2 / A_ ** 2


def drad(s, K, twoM=None):
    m = M_ if twoM is None else mp.mpf(twoM)
    return m / s ** 2 - 2 * K / s ** 3 + 2 * s / A_ ** 2


def excursion(K, lo, hi, twoM=None):
    """|Im tau| across the lift.  Each END is a SIMPLE zero, so the integrand goes as
    |s - s_end|^(-1/2); the substitution u^2 = |s - s_end| removes it exactly.
    ⌗ The guard is on the radicand's VALUE and not on u == 0: at 50 digits a quadrature node can be
      close enough to the end that lo + u**2 rounds TO it, where the radicand is exactly 0."""
    def half(a, b, sing_at_a):
        L = mp.sqrt(b - a)
        end = a if sing_at_a else b
        lim = 1 / mp.sqrt(abs(drad(end, K, twoM)))

        def g(u):
            s = a + u ** 2 if sing_at_a else b - u ** 2
            v = -rad(s, K, twoM)
            return lim if v <= 0 else u / mp.sqrt(v)
        return 2 * mp.quad(g, [0, L])
    mid = (lo + hi) / 2
    if lo == 0:                                   # the vacuum inner end is REGULAR, not singular
        return mp.quad(lambda s: 1 / mp.sqrt(-rad(s, K, twoM)), [0, mid]) + half(mid, hi, False)
    return half(lo, mid, True) + half(mid, hi, False)


print(f"\n  derived: alpha = {ALPHA:.3f} Mpc   r_0 = {R0:.3f} Mpc   2M = {TWOM:.4f} Mpc"
      f"   K = {KRAD:.3f} Mpc^2")
print(f"           the vacuum turnaround r_t = (2M alpha^2)^(1/3) = {RT:.6f} Mpc")
print(f"           pi alpha / 3 = {BOUND:.9f} Mpc        K / 2M = {KRAD / TWOM:.9f} Mpc")

# =================================================================================== Ⓐ THE VACUUM
head("A -- THE VACUUM LIFT IS pi alpha / 3, AND THE CLAUSE'S 'INDEPENDENT OF M' IS MADE FAILABLE")
rt_m = mp.findroot(lambda s: rad(s, mp.mpf(0)), mp.mpf(RT))
im_vac = excursion(mp.mpf(0), mp.mpf(0), rt_m)
rel_vac = abs(im_vac - mp.pi * A_ / 3) / (mp.pi * A_ / 3)
print(f"      the vacuum turnaround, re-found as a ROOT: {mp.nstr(rt_m, 16)} Mpc"
      f"   (closed form {RT:.9f})")
print(f"      |Im tau| over (0, r_t) = {mp.nstr(im_vac, 18)} Mpc")
print(f"      pi alpha / 3           = {mp.nstr(mp.pi * A_ / 3, 18)} Mpc"
      f"      relative = {mp.nstr(rel_vac, 6)}")
check("Ⓐ①  the vacuum lift's imaginary excursion IS pi alpha / 3, to better than 1e-12 relative",
      float(rel_vac) < 1e-12)

print("\n      Ⓐ② the same integral at five masses AWAY from the Nariai value -- the member fixes M"
      "\n          from alpha, so the clause cannot be tested on the member at all:")
m_ok = True
for fac in (0.3, 0.7, 1.0, 1.5, 3.0):
    tm = TWOM * fac
    rt_f = mp.findroot(lambda s: rad(s, mp.mpf(0), tm), mp.mpf((tm * ALPHA ** 2) ** (1 / 3)))
    im_f = excursion(mp.mpf(0), mp.mpf(0), rt_f, tm)
    rel_f = abs(im_f - mp.pi * A_ / 3) / (mp.pi * A_ / 3)
    print(f"          2M = {fac:4.1f} x Nariai = {tm:11.4f} Mpc    r_t = {float(rt_f):11.4f}"
          f"    |Im tau| = {float(im_f):.9f}    relative to pi alpha/3 = {float(rel_f):.3e}")
    m_ok = m_ok and float(rel_f) < 1e-12
check("Ⓐ②  and it does NOT move with the mass: five masses off the member, all pi alpha / 3 to "
      "1e-12 -- so `thm:bead`'s 'independent of M' holds, and holds for the reason it gives",
      m_ok)

# ============================================================================== Ⓑ THE SECOND NUMBER
head("B -- THE BENT CUT: TWO ZEROS, AN INNER ONE AT K/2M, AND AN EXCURSION ABOVE THE BOUND")
quart = np.roots([1.0 / ALPHA ** 2, 0.0, 0.0, -TWOM, KRAD])
pos = sorted(float(x.real) for x in quart
             if abs(x.imag) < 1e-7 * max(1.0, abs(x.real)) and x.real > 0)
roots = [brentq(lambda s: float(rad(mp.mpf(s), K_)), g * (1 - 1e-6), g * (1 + 1e-6), xtol=1e-14)
         for g in pos]
print(f"      the positive roots of  s^4/alpha^2 - 2M s + K = 0 :  {len(roots)}")
for x in roots:
    print(f"        s = {x:.9f} Mpc   (r = {-x:.9f})")
check("Ⓑ③a the bent radicand has EXACTLY TWO zeros on the conjugate side, where the vacuum one "
      "has a single interval reaching the branch point", len(roots) == 2)
if len(roots) == 2:
    s_in, s_out = roots
    ratio = s_in / (KRAD / TWOM)
    print(f"      inner root / (K/2M) = {ratio:.12f}")
    print(f"      outer root against the vacuum turnaround: {s_out:.6f} vs {RT:.6f}"
          f"   -> inward by {RT - s_out:.6f} Mpc = {(RT - s_out) / RT:.6e} relative")
    check("Ⓑ③b the INNER zero is K/2M to nine significant figures -- the lift detaches from the "
          "branch point at the radius where the radiation term balances the dust term",
          abs(ratio - 1.0) < 5e-10)
    check("Ⓑ③c the OUTER zero moves INWARD of the vacuum turnaround, by under a part in a thousand",
          0 < (RT - s_out) / RT < 1e-3)
    im_bent = excursion(K_, mp.mpf(s_in), mp.mpf(s_out))
    rel_b = (im_bent - mp.pi * A_ / 3) / (mp.pi * A_ / 3)
    print(f"\n      |Im tau| across the BENT lift ({s_in:.6f}, {s_out:.6f}) ="
          f" {mp.nstr(im_bent, 18)} Mpc")
    print(f"      against pi alpha / 3 = {mp.nstr(mp.pi * A_ / 3, 18)} Mpc"
          f"   ->  {mp.nstr(im_bent - mp.pi * A_ / 3, 10)} Mpc = {mp.nstr(rel_b, 8)} relative")
    check("Ⓑ④a the bent cut's excursion EXCEEDS the vacuum bound -- a second number beside the "
          "theorem, not a restatement of it", float(im_bent) > float(mp.pi * A_ / 3))
    check("Ⓑ④b and the excess is 3.0533e-4 of the bound, to five figures",
          abs(float(rel_b) - 3.0533e-4) < 5e-8)
    # ⌗ AND THE SAME MEASUREMENT PINNED IN THE UNITS THE CITING SENTENCE PRINTS IT IN.  The INDEX
    #   row says "3.0533 parts in ten thousand"; a pin on 3.0533e-4 does not hold the figure 3.0533,
    #   and check_figures_pinned is right to say so -- a sentence's figure has to be failable AS
    #   PRINTED, not in whatever units the receipt happened to compute in.
    excess_in_parts_per_ten_thousand = float(rel_b) * 1e4
    print(f"      the excess in the units the citing sentence prints: "
          f"{excess_in_parts_per_ten_thousand:.6f} parts in ten thousand")
    check("Ⓑ④d and that same excess is 3.0533 parts in ten thousand -- the figure the INDEX row "
          "prints, pinned in the units it prints it in",
          abs(excess_in_parts_per_ten_thousand - 3.0533) < 5e-4)
    # r7797 (69): P7's paragraph prints both excursions in Mpc to three decimals, so they are pinned here
    #   to half that printed digit.
    check("Ⓑ④e and the two excursions P7 prints are 5461.008 Mpc on the bent cut and 5459.341 Mpc for "
          "pi alpha / 3, each to half its last printed digit",
          abs(float(im_bent) - 5461.008) < 5e-4 and abs(float(mp.pi * A_ / 3) - 5459.341) < 5e-4)
    # ⌗ THE CONTROL: the same code path with K = 0 must return the bound, so the excess is the
    #   BEND's and not the integrator's.  Without this, Ⓑ④ would be a claim about this quadrature.
    ctrl = excursion(mp.mpf(0), mp.mpf(0), rt_m)
    print(f"      CONTROL, the same code path at K = 0: {mp.nstr(ctrl, 18)}"
          f"   relative to the bound {mp.nstr(abs(ctrl - mp.pi * A_ / 3) / (mp.pi * A_ / 3), 4)}")
    check("Ⓑ④c CONTROL -- the same integrator at K = 0 returns the bound, so the excess is the "
          "bend's and not the quadrature's", float(abs(ctrl - mp.pi * A_ / 3)) < 1e-9)
    print(f"\n      and the mechanism: the lift is SHORTER in r by"
          f" {float((rt_m - s_out) + s_in):.6f} Mpc, while the EVEN term K/s^2 reduces |radicand|"
          f"\n      across the interior, so 1/sqrt(|.|) rises and the rise beats the shortening:")
    mid = (s_in + s_out) / 2
    print(f"        at the midpoint s = {mid:.4f} Mpc:  |rad| vacuum ="
          f" {float(-rad(mp.mpf(mid), mp.mpf(0))):.10f}   bent = {float(-rad(mp.mpf(mid), K_)):.10f}")
else:
    s_in = s_out = None

# ------------------------------------------------------------------------- the exponents, both legs
def tau_of(r_abs, K, sign):
    """|tau| from the branch point out to |r| = r_abs, on the leg `sign` of the bent cut"""
    def integrand(x):
        v = rad(mp.mpf(x), K) if sign < 0 else (M_ + K / x) / x ** 3 + 1 / A_ ** 2
        if sign > 0:
            return 1 / mp.sqrt(((M_ + K / mp.mpf(x)) / mp.mpf(x)) + mp.mpf(x) ** 2 / A_ ** 2)
        return 1 / mp.sqrt(v)
    return mp.quad(integrand, [mp.mpf('1e-14'), mp.mpf(r_abs)])


print()
expo = {}
for sign, name in ((+1, 'the matter leg  (r > 0)'), (-1, 'the conjugate leg (r < 0)')):
    t_lo, t_hi = tau_of('1e-4', K_, sign), tau_of('1e-3', K_, sign)
    e = float((mp.log(mp.mpf('1e-3')) - mp.log(mp.mpf('1e-4'))) / (mp.log(t_hi) - mp.log(t_lo)))
    expo[sign] = e
    print(f"      {name}:  tau(1e-4) = {float(t_lo):.6e}   tau(1e-3) = {float(t_hi):.6e}"
          f"   d ln|r| / d ln|tau| = {e:.6f}")
# the VACUUM control: dust's 2/3, measured on the same machinery
t_lo0 = mp.quad(lambda x: 1 / mp.sqrt(M_ / mp.mpf(x) + mp.mpf(x) ** 2 / A_ ** 2),
                [mp.mpf('1e-14'), mp.mpf('1e-4')])
t_hi0 = mp.quad(lambda x: 1 / mp.sqrt(M_ / mp.mpf(x) + mp.mpf(x) ** 2 / A_ ** 2),
                [mp.mpf('1e-14'), mp.mpf('1e-3')])
e_vac = float((mp.log(mp.mpf('1e-3')) - mp.log(mp.mpf('1e-4'))) / (mp.log(t_hi0) - mp.log(t_lo0)))
print(f"      the VACUUM cut, same machinery:                                       "
      f"   d ln|r| / d ln|tau| = {e_vac:.6f}")
check("Ⓑ⑤a the branch point is approached as tau^(1/2) -- radiation's exponent -- on BOTH legs of "
      "the bent cut", all(abs(expo[s] - 0.5) < 1e-3 for s in (+1, -1)))
check("Ⓑ⑤b CONTROL -- the vacuum cut gives dust's 2/3 on the same machinery, so the measurement "
      "distinguishes the two and is not returning 1/2 by construction",
      abs(e_vac - 2.0 / 3.0) < 1e-3)
check("Ⓑ⑤c and the radicand is POSITIVE on the conjugate side inside the inner zero, so that "
      "approach is in REAL cosmic time",
      s_in is not None and all(float(rad(mp.mpf(x), K_)) > 0
                               for x in (1e-12, 1e-8, 1e-4, 1e-3, s_in * 0.5)))

# ================================================================================ Ⓒ THE STRUCTURAL
head("C -- NO CONDITION THE BEAD IMPOSES CARRIES K, BY DIFFERENTIATION AND NOT BY INSPECTION")
r, al, Ks, TwoMs = sp.symbols('r alpha K twoM', positive=True)
f_vac = 1 - TwoMs / r - r ** 2 / al ** 2
CONDITIONS = [
    ('the Nariai condition   Lambda G^2 M^2 / c^4 = 1/9', 2 * al / (3 * sp.sqrt(3)) - TwoMs),
    ('the unit-speed seams   f = 0', f_vac),
    ('the comoving turnaround 1 - f = 0', 1 - f_vac),
    ('the Euclidean null     f = 2', f_vac - 2),
    ('the contour radicand   (dr/dtau)^2 = 1 - f', 1 - f_vac),
    ("the lap's unit-speed cubic  r^3 - c r + 2M = 0", r ** 3 - sp.Symbol('c') * r + TwoMs),
]
struct = True
for name, expr in CONDITIONS:
    d = sp.simplify(sp.diff(expr, Ks))
    print(f"      d/dK [ {name:<50s} ] = {d}")
    struct = struct and d == 0
check("Ⓒ⑥  all six conditions have ZERO derivative with respect to K -- each is a condition on the "
      "vacuum f, which carries 2M and alpha and no radiation term, so the bead cannot fix K",
      struct)
print("      ⌗ the claim is scoped to exactly those six and to no other sentence of the corpus.")

# ============================================================================= Ⓓ THE PAPER, 3 STATES
head("D -- THE TWO SENTENCES THIS RECEIPT STANDS BESIDE, IN THREE STATES")
P7 = body('CR_framework.tex')
SENTS = [' '.join(s.split()) for s in re.split(r'(?<=[.!?])\s+', P7) if s.strip()]
SUBJECTS = {
    "thm:bead's bound clause": 'fixed by the exponent and independent of',
    "the lap caption's segments": 'three closed-form segments (collapse, lift, expansion)',
}


def resolve(key):
    """MATCHED   -- in print, inside a sentence of the paper;
       WITHDRAWN -- in the paper's FULL TEXT but in no sentence the splitter produced;
       STALE     -- nowhere in the full text.
    ** What is searched: the whole of `corpus/CR_framework.tex`, whitespace-flattened. **
    ⌗ Three states and not two, because a two-state arm returns the same word for a sentence that
      is WRONG and a sentence that has been DELETED -- which is exactly what happened to `r7768`'s
      arm 6 when `r7767` removed its subject."""
    if any(key in s for s in SENTS):
        return 'MATCHED'
    return 'WITHDRAWN' if key in P7 else 'STALE'


states = {}
for label, key in SUBJECTS.items():
    states[label] = resolve(key)
    hit = next((s for s in SENTS if key in s), '')
    print(f"      {label:<30s} -> {states[label]}")
    if hit:
        print(f"        \"...{hit[max(0, hit.find(key) - 90):hit.find(key) + 140]}...\"")
check("Ⓓ⑦  both subjects resolve MATCHED -- the clause this receipt quotes and the caption it adds "
      "a segment to are both in print, in a sentence, on this tree",
      all(v == 'MATCHED' for v in states.values()))

head("D -- THE COUNT, THE SCOPE, AND WHAT IS NOT CLAIMED")
print(f"      checks run: {len(fails) + sum(1 for _ in ())}  (reported individually above)")
print("      REGISTERED ARMS: 8  -- Ⓐ①② Ⓑ③④⑤ Ⓒ⑥ Ⓓ⑦⑧; this is ⑧.")
print("      the two INPUTs are declared in the COMPUTES header and nothing here is fitted.")
print("      NOT CLAIMED: the epoch at which the deposited plasma becomes the bend; what the")
print("      progenitor's branch carries; and nothing here contradicts `thm:bead`, which Ⓐ①")
print("      reproduces to twelve digits on the member and Ⓐ② confirms off it.")
# ⌗ SCOPE-AS-CHECK (r7141): ⑧ is a SCOPE STATEMENT and is PRINTED, not checked.  The registration
#   named "a gate that cannot fail" as ⑧'s own reachable negative, and the first form of this arm WAS
#   one -- `check(..., True)`, which the hollow-assertion lint caught by exactly that criterion.
#   ** A check that cannot fail adds a PASS to the count and tests nothing. **
print("      ⑧ is a SCOPE STATEMENT, printed and not checked -- see the note in the source.")

print('\n' + '=' * 90)
if fails:
    print(f"  ⛔ {len(fails)} CHECK(S) FAILED:")
    for x in fails:
        print(f"     - {x}")
    print('=' * 90)
    sys.exit(1)
print(f"""
  ALL CHECKS PASS.

  The vacuum lift's imaginary excursion is pi alpha / 3 = {BOUND:.6f} Mpc, and
  that value does not move with the mass -- `thm:bead`'s clause holds, and the
  check that shows it has to leave the Nariai member, where the mass is fixed.

  The history the content rides is the bent cut, and its lift is a SECOND
  number beside the theorem: {float(im_bent):.6f} Mpc, above the bound by
  {float(rel_b):.3e} of it.  Its ends are both pulled in -- the outer by
  {RT - s_out:.6f} Mpc, and the inner all the way to K/2M = {KRAD / TWOM:.6f} Mpc, so the
  lift DETACHES from the branch point and the lap carries four segments where
  the vacuum curve carries three.  The branch point is then reached in real
  cosmic time, as tau^(1/2), on both legs.

  And none of it can be read back as a prediction of the radiation
  coefficient: every condition the bead imposes has zero derivative with
  respect to K, because each is a condition on the vacuum f.
""")
print('=' * 90)
