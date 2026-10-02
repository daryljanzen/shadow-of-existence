"""r7129+70.1 (70) -- `PO-77` ⓵: which congruence's horizon the corpus's freezing argument is about, and what carrying
the leaf onto the lift would require.  Pre-registered at PREDICTION.md beside this file.  sympy + mpmath.  The papers
and every receipt are READ; nothing is edited.  Other seats' wording is located and printed, never asserted.

  R.  the row, and two corrections of my own r7127 audit (R2: the 1.96 / 19.6 do not discriminate the branch; the
      0.13 does and is not reproducible at the locus named; R3: a fourth seam, on the bead's collapse leg)
  1.  which branch each COMPUTED freezing census is on
  2.  the leaf's lift threshold, against the corpus's own radiation datum
"""
import os
import re

import mpmath as mp
import sympy as sp

mp.mp.dps = 30
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def head(t):
    print('\n' + '=' * 100 + '\n  ' + t + '\n' + '=' * 100)


def located(text, pattern):
    m = re.search(pattern, text)
    return '(not located)' if not m else '...' + ' '.join(text[max(0, m.start() - 50):m.end() + 110].split()) + '...'


def rec(stem):
    d = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology')
    [f] = [x for x in os.listdir(d) if x.startswith(stem)]
    return open(os.path.join(d, f), encoding='utf-8').read()


P15 = open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'), encoding='utf-8').read()
LOCUS = rec('P15_the_locus_is_wrong_in_six_places')
C2 = rec('C2_horizon_limits')

# alpha = 1, the Nariai member
M = 1 / (3 * mp.sqrt(3))
A = (2 * M) ** (mp.mpf(1) / 3)              # the bead's turnaround |r|; the comoving turnaround is r = -A
rN = 1 / mp.sqrt(3)
one_minus_f = lambda r: 2 * M / r + r ** 2   # signed r
aH = lambda r: mp.sqrt(abs(one_minus_f(r)))

# =========================================================================================== R
head('R2.  THE PAPER\'S 1.96 AND 19.6 DO NOT DISCRIMINATE THE BRANCH; ITS 0.13 DOES, AND IS NOT REPRODUCIBLE')
print('      P15 :', located(P15, r'it is \$0\.13\$ at the comoving turnaround'))
for x in (mp.mpf('0.1'), mp.mpf('1e-3')):
    print(f'      |r| = {mp.nstr(x, 2)}:  r > 0 gives {mp.nstr(aH(x), 6)},  r < 0 gives {mp.nstr(aH(-x), 6)}')
gate('both signs round to the paper\'s 1.96 and 19.6 -- so those two figures place the sentence on NEITHER branch.  '
     '⛔ My r7127 audit read them as placing it on the lift, and the row carries that; 66\'s 1.964 is the r > 0 value',
     all(mp.nstr(aH(s * x), 3) == w for x, w in ((mp.mpf('0.1'), '1.96'), (mp.mpf('1e-3'), '19.6')) for s in (1, -1)))
loc_norm = mp.sqrt(one_minus_f(rN))
gate(f'and the locus receipt\'s own table (r > 0, normalised by the seam, where sqrt(1-f) = {mp.nstr(loc_norm, 6)}) '
     f'prints exactly {mp.nstr(aH(mp.mpf("0.1")) / loc_norm, 3)} and {mp.nstr(aH(mp.mpf("1e-3")) / loc_norm, 3)}: the '
     f'figures in the sentence are that table\'s, i.e. the POSITIVE-r census',
     abs(loc_norm - 1) < mp.mpf('1e-25') and 'for r, tag in [(R_SEAM' in LOCUS and '(0.1 * ALPHA' in LOCUS
     and '(1e-3 * ALPHA' in LOCUS)
gate(f'the comoving turnaround is 1 - f = 0, r = -A = {mp.nstr(-A, 6)} (P07, I11), where sqrt|1-f| = '
     f'{mp.nstr(aH(-A), 3)} EXACTLY -- so "0.13 at the comoving turnaround" is not reproducible from the law the '
     f'sentence states, at the locus it names', abs(one_minus_f(-A)) < mp.mpf('1e-25'))
lo = mp.findroot(lambda x: aH(-x) - mp.mpf('0.13'), (A * mp.mpf('0.95'), A), solver='bisect')
hi = mp.findroot(lambda x: aH(-x) - mp.mpf('0.13'), (A, A * mp.mpf('1.05')), solver='bisect')
pos_min = min(aH(x) for x in mp.linspace(mp.mpf('0.05'), 3, 600))
gate(f'0.13 IS reached on the signed-negative branch only, at |r| = {mp.nstr(lo, 5)} (lift side) and {mp.nstr(hi, 5)} '
     f'(collapse side), within {mp.nstr(100 * max(A - lo, hi - A) / A, 2)} % of A; on r > 0, sqrt(1-f) never falls below '
     f'{mp.nstr(pos_min, 4)}.  ** So the sentence\'s first figure is the bead\'s contracting side and its other two are '
     f'the positive-r table: one sentence, two branches **', pos_min > mp.mpf('0.99') and lo < A < hi)

head('R3.  A FOURTH SEAM, AND THE BEAD\'S COLLAPSE LEG DOES PASS IT')
print('      P15 :', located(P15, r'unit-speed loci \$r=-2\\alpha/\\sqrt3\$'))
rr = sp.symbols('r')
roots = sp.solve(sp.Eq(1 - 2 * sp.Rational(1, 1) / (3 * sp.sqrt(3)) / rr - rr ** 2, 0), rr)
gate(f'f = 0 at the Nariai mass has roots {sorted(set(float(sp.re(sp.N(x))) for x in roots))}: the double root +1/sqrt3 (r_N) and -2/sqrt3; |-2/sqrt3| = '
     f'{mp.nstr(2 / mp.sqrt(3), 5)} > A = {mp.nstr(A, 5)}, so the back seam IS on the bead\'s collapse leg (r = A '
     f'cosh^(2/3) x >= A, signed negative).  ⛔ My r7127 ⓻ ("reaches none of them") was true of the three I listed '
     f'and false of the corpus\'s own list.  Finding ⓹ -- r_N is not on that leg -- is untouched',
     set(sp.nsimplify(x) for x in roots) == {1 / sp.sqrt(3), -2 / sp.sqrt(3)} and 2 / mp.sqrt(3) > A > rN)

# =========================================================================================== 1
head('1.  WHICH BRANCH EACH COMPUTED FREEZING CENSUS IS ON')
print('      P15 prop:subhorizon:', located(P15, r'because \$2M/r\$ diverges there'))
print('      P15 sec:envelope   :', located(P15, r'\$2M/r\\to\\infty\$ carries \$aH\$ up without bound'))
loc_pos = 'return A / r ** 2 + 2.0 * MASS / r + r ** 2 / ALPHA ** 2' in LOCUS and "R_SEAM = ALPHA / np.sqrt(3.0)" in LOCUS
c2_pos = "r,M,al,A=sp.symbols('r M alpha A', positive=True)" in C2
gate('the two receipts that COMPUTE the freezing census -- C2 and P15_the_locus_is_wrong (which prop:subhorizon and '
     'sec:envelope cite) -- both evaluate (rH)^2 = A_r/r^2 + 2M/r + r^2/alpha^2 with r declared or sampled POSITIVE',
     loc_pos and c2_pos)
x = sp.symbols('x', positive=True)
Ms, Ar = sp.symbols('M A_r', positive=True)
pos = Ar / x ** 2 + 2 * Ms / x + x ** 2
gate('and on r > 0 that rate is a sum of positive terms: no turnaround, no Euclidean segment, r reaches 0 in real '
     'time.  ** Every computed freezing census in the corpus is on a branch WITH NO LIFT **',
     all(t.is_positive for t in sp.Add.make_args(pos)))

# =========================================================================================== 2
head('2.  CAN THE LEAF BE CARRIED ONTO THE LIFT?  ITS OWN RADIATION DATUM SAYS NO')
g = Ar / x ** 2 - 2 * Ms / x + x ** 2                      # the leaf's (rH)^2 on the signed contracting side, x = |r|
sol = sp.solve([sp.Eq(g, 0), sp.Eq(sp.diff(g, x), 0)], [x, Ar], dict=True)
[s0] = [s for s in sol if s[x].is_positive]
gate(f'a Euclidean segment exists iff g(x) = A_r/x^2 - 2M/x + x^2 < 0 somewhere; the double-root threshold is '
     f'x^3 = M/2 and A_r* = {sp.simplify(s0[Ar])}, i.e. (3M/2)(M/2)^(1/3)',
     sp.simplify(s0[x] ** 3 - Ms / 2) == 0 and sp.simplify(s0[Ar] - sp.Rational(3, 2) * Ms * (Ms / 2) ** sp.Rational(1, 3)) == 0)
Mn = sp.Rational(1, 1) / (3 * sp.sqrt(3))
rs = 1 / sp.sqrt(3)
A_star = sp.nsimplify(s0[Ar].subs(Ms, Mn))
A_datum = 4 * Mn * rs                                      # C2 / locus receipt: rho_r/rho_m ~ 2 at the seam
ratio_star = sp.simplify(A_star / (2 * Mn * rs))
gate(f'in the corpus\'s datum language (rho_r/rho_m at the seam = A_r/(2M r_s)): the leaf has a lift only below '
     f'{sp.nsimplify(ratio_star)} = {float(ratio_star):.4f}; the corpus\'s datum is A_r = 4M r_s = {A_datum}, ratio '
     f'{sp.simplify(A_datum / (2 * Mn * rs))} -- {float(A_datum / A_star):.2f}x the threshold',
     abs(float(ratio_star) - 0.595) < 0.001 and sp.simplify(A_datum / (2 * Mn * rs)) == 2 and 'A_RAD = 4.0 * MASS * R_SEAM' in LOCUS)
gmin = min(float(g.subs({Ar: A_datum, Ms: Mn, x: xv})) for xv in [i / 1000 for i in range(5, 3000)])
gate(f'⇒ at the datum the leaf\'s rate on the contracting side never vanishes (minimum {gmin:.4f} > 0): ** the leaf '
     f'has no lift at all.  Carrying it onto the lift would need its radiation below 0.595 of matter at the seam -- the '
     f'leaf becoming the bead there -- or the bead with radiation, which no file constructs **', gmin > 0)

head('3.  THE ANSWER TO ⓵')
gate('the composition sentence\'s two halves hold on two congruences that cannot both hold on one segment: on the LEAF '
     'every mode freezes in real time as r -> 0 and there is no kernel, because there is no lift; on the BEAD there is a '
     'kernel, and on its contracting side aH = 0 at the turnaround, so every mode is inside the horizon where the lift '
     'begins.  ⇒ "frozen, so the kernel has nothing to act on" applies the leaf\'s census to a segment only the bead '
     'has -- and the leaf, at the corpus\'s own datum, does not reach a lift to decide anything at',
     gmin > 0 and abs(one_minus_f(-A)) < mp.mpf('1e-25'))

print(f'\n  {len(CHECKS)} checks, {sum(ok for _, ok in CHECKS)} pass')
assert all(ok for _, ok in CHECKS), [n for n, ok in CHECKS if not ok]
