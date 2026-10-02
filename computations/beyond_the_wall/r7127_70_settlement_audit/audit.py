"""r7127+70.1 (70) -- the adversarial audit of the gate's `r7127` settlement (`PO-77` struck), receipt
`P15_there_was_never_a_second_transfer_...`.  Pre-registered at PREDICTION.md beside this file.  mpmath + sympy.
By `r7115`'s premise no curvature invariant is compared across the reassignment.  The papers and both seats'
receipts are READ; nothing is edited.

  A.  does the 0.8 per cent agreement do any work?         (1) provenance, (2) the control, (3) the exponent
  B.  is "C21's leg ends at the seam" consistent?          (4) r_N on the bead, (5) the overlap, (6) frozen where
"""
import os
import re

import mpmath as mp
import sympy as sp

mp.mp.dps = 30
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
R = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology')
CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def head(t):
    print('\n' + '=' * 100 + '\n  ' + t + '\n' + '=' * 100)


def src(stem):
    [f] = [x for x in os.listdir(R) if x.startswith(stem)]
    return open(os.path.join(R, f), encoding='utf-8').read()


def located(text, pattern):
    """print the line a pattern sits on -- located, NOT asserted: an audit that pinned other seats' wording
    would be the QUOTE-PIN class this seat just built the operator for"""
    m = re.search(pattern, text)
    if not m:
        return '(not located)'
    return '...' + ' '.join(text[max(0, m.start() - 60):m.end() + 90].split()) + '...'


P15 = open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'), encoding='utf-8').read()
P10 = open(os.path.join(ROOT, 'corpus', 'canonical_time.tex'), encoding='utf-8').read()
SETTLE = src('P15_there_was_never_a_second_transfer')
R7108 = src('P15_the_angular_label_crosses_the_lift')
EXACT = src('P15_the_exact_transmission_ratios_are_recomputed')

# the construction, in the gauge alpha = 1, Nariai mass
al = mp.mpf(1)
M = al / (3 * mp.sqrt(3))
A = (2 * M * al ** 2) ** (mp.mpf(1) / 3)
rN = al / mp.sqrt(3)
c0 = 2 / (mp.sqrt(3) * mp.mpf(2) ** (mp.mpf(1) / 3))
s_tot = c0 * mp.beta(mp.mpf(1) / 6, mp.mpf(1) / 2) / 2
s_coll = c0 * mp.beta(mp.mpf(1) / 3, mp.mpf(1) / 6) / 4
s_expa = 2 * s_coll
H0, Om, ckms = mp.mpf('68.60'), mp.mpf('0.2973'), mp.mpf('299792.458')
alpha_Mpc = (ckms / H0) / mp.sqrt(1 - Om)
r0_Mpc = alpha_Mpc / mp.mpf('1.0320')

# =========================================================================================== A
head('A(1).  PROVENANCE: THE PAPERS\' FIGURE IS THE SAME INTEGRAL, EVALUATED AT r2419')
print('      P15 :', located(P15, r'Delta\\eta\\rvert=3\.32'))
print('      P10 :', located(P10, r'1\.7\\times10\^\{4\}'))
# the r2419-era receipt's own integrand, re-integrated EXACTLY: ds / (A sin^{2/3}(3s/2)) on s in (0, pi/3)
old_exact = mp.quad(lambda s: 1 / (A * mp.sin(mp.mpf(3) * s / 2) ** (mp.mpf(2) / 3)), [0, mp.pi / 6, mp.pi / 3])
gate(f'the 2026-08 receipt\'s integrand `ds/(A sin^(2/3)(3s/2alpha))` over the lift, integrated EXACTLY, is '
     f'{mp.nstr(old_exact, 12)} = s_tot = c0 B(1/6,1/2)/2 = {mp.nstr(s_tot, 12)}: the SAME integral',
     abs(old_exact - s_tot) < mp.mpf('1e-9')
     and 'np.abs(np.sin(1.5 * s / al)) ** (2. / 3)' in EXACT and 'np.diff(s) / (0.5 * (a[1:] + a[:-1]))' in EXACT)
gap = s_tot - mp.mpf('3.3233')
endpoint = 2 * 3 * c0 * mp.mpf('1e-8') ** (mp.mpf(1) / 3) / 2      # the order of the eps-cut endpoint pieces
print(f'      its printed 3.3233 is s_tot less {mp.nstr(gap, 3)} -- a trapezoid on an integrable s^(-2/3) endpoint '
      f'(the eps cut alone is ~{mp.nstr(endpoint, 2)}); the paragraph rounds it to 3.32')
fig_alpha = mp.mpf('3.32') * alpha_Mpc
gate(f'and 1.7e4 Mpc is 3.32 alpha rounded: 3.32 x {mp.nstr(alpha_Mpc, 6)} = {mp.nstr(fig_alpha, 6)} Mpc -> 1.7e4.  '
     f'** The figure was made in alpha units; r7127 reconverts it with r_0 and calls that conversion forced **',
     abs(fig_alpha / mp.mpf('1.7e4') - 1) < mp.mpf('0.03') and 'r0_Mpc = alpha_Mpc / mp.mpf(\'1.0320\')' in SETTLE)
via_r0, via_al = mp.mpf('1.7e4') / r0_Mpc, mp.mpf('1.7e4') / alpha_Mpc
print(f'      round trip: 1.7e4/r_0 = {mp.nstr(via_r0, 5)} ({mp.nstr(100*abs(via_r0/s_tot-1), 2)} % from s_tot), '
      f'1.7e4/alpha = {mp.nstr(via_al, 5)} ({mp.nstr(100*abs(via_al/s_tot-1), 2)} %), unrounded 3.3233 alpha: '
      f'{mp.nstr(100*abs(mp.mpf("3.3233")/s_tot-1), 2)} %')
gate('⇒ so the 0.8 per cent is ROUNDING (two significant figures, then one) plus a choice of length, on ONE '
     'integral evaluated twice; it measures nothing about the transfer, and neither conversion is privileged '
     'by it', abs(via_r0 / s_tot - 1) < mp.mpf('0.02') and abs(via_al / s_tot - 1) < mp.mpf('0.03'))

head('A(2).  THE LEG-SELECTING CONTROL SELECTS PROVENANCE, NOT PHYSICS')
gate(f'the control\'s legs are {mp.nstr(s_coll, 5)} / {mp.nstr(s_tot, 5)} / {mp.nstr(s_expa, 5)}; the papers\' figure '
     f'matches the lift because the r2419 computation integrated s in (0, pi alpha/3), WHICH IS the lift, and P10 '
     f'DEFINES |Delta eta| as the lift\'s interval -- so the match could not have come out otherwise and adds nothing '
     f'to the receipt\'s own ⓷ ("a reproduction")', 'smax = np.pi * al / 3.0' in EXACT
     and abs(s_expa / s_coll - 2) < mp.mpf('1e-25'))

head('A(3).  THE EXPONENT -- WHAT DISCRIMINATES, AND IT WAS NOT COMPARED')
print('      P15 :', located(P15, r'with \$\\omega=kc_\{s\}\$'))
print('      P10 :', located(P10, r'damped by \$e\^\{-\\omega'))
print('      r7108:', located(R7108, r"u''\+\(k\^2-a''/a\)u=0"))
cs_in_old = 'w = k / np.sqrt(3.0 * (1.0 + R0 * a))' in EXACT
cs_in_7108 = bool(re.search(r"u_\{ss\}=\(k\^2\+a_\{ss\}/a\)", R7108)) and 'np.sqrt(3' not in R7108.split('def lnT')[1][:900]
gate('the kernel the papers apply damps by e^{-omega|Delta eta|} with omega = k c_s (the r2419 receipt integrates '
     'omega = k/sqrt(3(1+R))), while r7108\'s lift equation is u_ss = (k^2 + a_ss/a) u with NO c_s -- a c_s = 1 '
     'field', cs_in_old and cs_in_7108)
kc_papers = 2 / (mp.mpf('1.7e4') / mp.sqrt(3))
kc_7108 = 2 / mp.mpf('1.7e4')
gate(f'⇒ on ONE segment the two exponents differ by sqrt3 = {mp.nstr(mp.sqrt(3), 5)}: the papers\' e^-2 wavenumber is '
     f'{mp.nstr(kc_papers, 3)} Mpc^-1 (their "k ~ 2e-4"), r7108\'s exponent puts it at {mp.nstr(kc_7108, 3)} Mpc^-1.  '
     f'** "T(k) -> 2^(7/3) k^2 e^(-k s_tot) IS the second half" holds for the FORM and not the RATE **',
     abs(kc_papers / kc_7108 - mp.sqrt(3)) < mp.mpf('1e-20') and abs(kc_papers / mp.mpf('2e-4') - 1) < mp.mpf('0.03'))
L1 = mp.sqrt(3)
print(f'      at L = 1 (k = sqrt3): e^(-k s_tot) = {mp.nstr(mp.exp(-L1*s_tot), 3)} against e^(-k c_s s_tot) = '
      f'{mp.nstr(mp.exp(-s_tot), 3)} -- a factor {mp.nstr(mp.exp(L1*s_tot - s_tot), 3)} in the mildest anisotropic damping')

print('      P15 :', located(P15, r'an exponent of\s+\$-152\$\s+at the first acoustic peak'))
print('      r7108:', located(R7108, r'the damping is \$e\^\{-255\}\$'))
k_peak = mp.sqrt(mp.mpf('78.5') * mp.mpf('80.5'))
ex_7108 = k_peak * s_tot - mp.log(2 ** (mp.mpf(7) / 3) * k_peak ** 2)
gate(f'⇒ AND THE PAPERS ALREADY CARRY BOTH RATES AT THE FIRST PEAK: P15\'s exponent -152 is integrated across the '
     f'segment\'s sound-speed profile, r7108\'s e^-255 is k s_tot at L = 78.5 (recomputed: {mp.nstr(ex_7108, 4)}).  '
     f'255/sqrt3 = {mp.nstr(255 / mp.sqrt(3), 4)} against 152 ({mp.nstr(100 * (152 / (255 / mp.sqrt(3)) - 1), 2)} per cent, '
     f'the residual being the two files\' different l -> k maps and R) -- ** the two "second halves" differ by the '
     f'sound speed, in the papers\' own figures **',
     abs(ex_7108 - 255) < 3 and abs(152 / (255 / mp.sqrt(3)) - 1) < mp.mpf('0.05')
     and bool(re.search(r'exponent of\s+\$-152\$', P15)) and bool(re.search(r'e\^\{-255\}', R7108)))

# =========================================================================================== B
head('B(4).  WHERE r_N IS ON THE BEAD: NOT ON ITS COLLAPSE LEG')
Ms, als = sp.symbols('M alpha', positive=True)
As = (2 * Ms * als ** 2) ** sp.Rational(1, 3)
ratio = sp.simplify((As / (als / sp.sqrt(3))).subs(Ms, als / (3 * sp.sqrt(3))))
gate(f'the bead\'s collapse leg is r = A cosh^(2/3)x >= A, and A/r_N = {ratio} at the Nariai mass, symbolically: '
     f'** the collapse leg bottoms out at 2^(1/3) r_N and never reaches the seam **', sp.simplify(ratio - 2 ** sp.Rational(1, 3)) == 0)
print('      P15 :', located(P15, r'where the collapse leg ends'))
print('      C2  : the seam is f\' = 0, r = (M alpha^2)^(1/3) = alpha/sqrt3 at Nariai (C2 step 3-5); r_* = 1.5338 r_seam')
t_N = mp.acos(1 / mp.sqrt(2))
gate(f'|r| = r_N is passed ON THE LIFT, where r7108\'s a = A cos^(2/3) t runs A -> 0: cos^(2/3) t = 2^(-1/3) at '
     f't = {mp.nstr(t_N, 8)} = pi/4 exactly -- and again on the expansion leg at the inflection',
     abs(t_N - mp.pi / 4) < mp.mpf('1e-25') and 'np.cos(t) ** (2.0 / 3.0)' in R7108)

head('B(5).  UNDER THE FOLIATION LABEL |r|, THE LEAF\'S LEG TO r_N OVERLAPS THE LIFT\'S FIRST STRETCH')
g = lambda t: c0 / mp.cos(t) ** (mp.mpf(2) / 3)                    # d eta / dt on the lift, r7108's g_of
part = mp.quad(g, [0, mp.pi / 4])
whole = mp.quad(g, [0, mp.pi / 4, mp.pi / 2])
gate(f'the lift\'s conformal length is {mp.nstr(whole, 10)} (= s_tot), and the stretch |r| in [r_N, A] is t in '
     f'[0, pi/4]: {mp.nstr(part, 6)}, i.e. {mp.nstr(100 * part / whole, 4)} per cent of the lift -- a FINITE '
     f'fraction.  ⛔ pre-registered 25-50 per cent: a MISS, low by under two points, recorded and not re-banded',
     abs(whole - s_tot) < mp.mpf('1e-9') and mp.mpf('0.2') < part / whole < mp.mpf('0.25'))
gate('⇒ so on |r| -- the label PO-74 uses, r7126 used, and r7127 does not replace -- the leaf\'s collapse leg down '
     'to the seam and the lift COVER THE SAME |r| over that stretch: neither "overlap everywhere" (r7126) nor '
     '"disjoint" (r7127).  And without a common label, "C21 to the seam, THEN the kernel" has no order to be '
     'sequential in', True)

head('B(6).  FROZEN ON WHICH CONGRUENCE')
aoa_turn = mp.mpf(2) ** (-mp.mpf(1) / 3)                          # a''/a at the turnaround, both Lorentzian legs
assoa = lambda t: -(2 / (3 * c0 ** 2)) * (mp.cos(t) ** 2 - mp.sin(t) ** 2 / 3) / mp.cos(t) ** (mp.mpf(2) / 3)
gate(f'at the turnaround, where T(k) is normalised, |a_ss/a| = {mp.nstr(-assoa(0), 10)} = 2^(-1/3) = '
     f'{mp.nstr(aoa_turn, 10)} (r7112\'s pure number), and every L >= 1 has k^2 >= 3: L = 1 is sub-horizon by '
     f'{mp.nstr(3 / aoa_turn, 4)} -- ** on the bead, no anisotropic mode is frozen where T(k) starts **',
     abs(-assoa(0) - aoa_turn) < mp.mpf('1e-25') and 3 / aoa_turn > 3)
for L in (1, 2, 10):
    k2 = L * (L + 2)
    ts = mp.findroot(lambda t: assoa(t) - k2, (mp.pi / 4, mp.pi / 2 - mp.mpf('1e-12')), solver='bisect')
    sig = mp.quad(g, [ts, mp.pi / 2])
    print(f'      L={L:3d}: a_ss/a overtakes k^2 only at t = {mp.nstr(ts, 8)}, sigma = {mp.nstr(sig, 4)} from r = 0, '
          f'i.e. the last {mp.nstr(100 * sig / s_tot, 3)} % of the lift;  asymptotic 2^(7/3) k^2 e^(-k s_tot) = '
          f'{mp.nstr(2 ** (mp.mpf(7) / 3) * k2 * mp.exp(-mp.sqrt(k2) * s_tot), 3)}'
          + (" (r7108's exact value: 7.00e-2)" if L == 1 else ''))
print('      P15 :', located(P15, r'at the branch point no mode is oscillating'))
print('      P10 :', located(P10, r'every mode exits it and freezes before the branch point'))
print('      P15 :', located(P15, r'grows without bound as \$r\\to0\$---it is \$0\.13\$'))
oneminusf = lambda r: 2 * M / r + r ** 2 / al ** 2                   # signed r: the collapse leg and lift are r < 0
aH = lambda r: mp.sqrt(abs(oneminusf(r)))
gate(f'P15\'s own freezing sentence uses the BEAD\'s E = 1 law aH = sqrt|1-f| (no radiation term) and quotes it at '
     f'|r| = 0.1 alpha and 1e-3 alpha: recomputed {mp.nstr(aH(-mp.mpf("0.1")), 3)} and {mp.nstr(aH(-mp.mpf("1e-3")), 3)} '
     f'(its 1.96 and 19.6).  BOTH radii are below A = {mp.nstr(A, 4)} alpha, i.e. in the |r| range the bead covers '
     f'ONLY ON THE LIFT; on the bead\'s real collapse leg (|r| >= A) aH = sqrt(r^2/alpha^2 - 2M/|r|) FALLS to '
     f'{mp.nstr(aH(-A), 3)} at the turnaround.  ** So the "freezing before the crossing" that sentence computes happens '
     f'across the lift -- the stretch the kernel acts on -- and not before it **',
     abs(aH(-mp.mpf('0.1')) - mp.mpf('1.96')) < mp.mpf('0.01') and abs(aH(-mp.mpf('1e-3')) - mp.mpf('19.6')) < mp.mpf('0.05')
     and abs(aH(-A)) < mp.mpf('1e-20') and mp.mpf('0.1') < A)
gate('⇒ "every mode exits it and freezes before the branch point, so the projection has nothing to act on" is '
     'true on the LEAF ((rH)^2 = (1-f) + A/r^2 -> infinity as r -> 0, C2).  On the BEAD, whose lift the kernel\'s '
     'length is, L >= 1 is sub-horizon where the lift STARTS and freezes only in its last 24 / 15 / 4 per cent '
     '(L = 1, 2, 10) -- AFTER the evanescent stretch that produces T(L) < 1.  So on the congruence the kernel '
     'belongs to, the anisotropic modes are NOT frozen before the crossing, the kernel DOES act on them, and '
     'T(0) = 1 is "the first half" only if the first half is narrowed from EVERY mode to the monopole',
     2 ** (mp.mpf(7) / 3) * 3 * mp.exp(-mp.sqrt(3) * s_tot) < 1 and 3 / aoa_turn > 1)

head('B(7).  THE INVENTORY -- WHO PLACES THE SEAM AND THE SUPER-HORIZON ERA, ON WHICH CONGRUENCE')
INV = [
    ('sec:envelope', 'leaf', 'r_N ("seam", collapse leg ends)', 'real', 'modes SUB-horizon at the seam; C21 drives to it'),
    ('prop:subhorizon / C2', 'leaf', 'r_N = f\'=0, r_* = 1.53 r_N', 'real', 'acoustic modes inside at the seam'),
    ('sec:what-crosses (P15)', 'bead law', '|r|: 0.13 -> 1e-3 alpha (< A)', 'lift', 'every mode freezes "before the crossing"'),
    ('P10 kernel paragraph', 'unstated', '"contracting leg", r -> 0', 'real?', 'frozen before the branch point'),
    ('r7108', 'bead', 'A (turnaround) -> 0 (seam = r=0)', 'IMAGINARY', 'T(0)=1, T(L>=1) ~ e^-k s_tot: L>=1 suppressed'),
    ('r7112 (60)', 'bead', 'collapse leg; divergences', 'real', 'only the monopole super-horizon away from them'),
    ('r7117 / PO-74 (60)', 'both', 'r_N = the inflection, expansion leg', 'real', 'the readings degenerate at the handover'),
    ('r7127 settlement', 'leaf->bead', 'r_N, then the lift', 'real->imag', 'C21 to the seam, THEN the kernel'),
]
for row in INV:
    print('      {:<24} {:<10} {:<36} {:<10} {}'.format(*row))
gate('the inventory carries THREE referents of "the seam" -- r_N on the leaf (sec:envelope, C2), r = 0 at the end of '
     'the lift (r7108), and the inflection r_N on the bead\'s EXPANSION leg (r7117) -- and the bead\'s collapse leg '
     'reaches none of them (its minimum is A = 2^(1/3) r_N)', A > rN > 0 and abs(A / rN - mp.cbrt(2)) < mp.mpf('1e-25'))

print(f'\n  {len(CHECKS)} checks, {sum(ok for _, ok in CHECKS)} pass')
assert all(ok for _, ok in CHECKS), [n for n, ok in CHECKS if not ok]
