#!/usr/bin/env python3
"""r7778 (60) -- the lift on the bent cut, and the object r7776's sign fork was posed about.

POST-REGISTRATION throughout: PREDICTION.md was committed AND pushed before this file existed.
Eleven arms, each a comparison with a reachable negative named in the registration.

READS DECLARED
  corpus/CR_framework.tex   -- thm:bead, its proof, rem:head-admissible, the scope paragraph,
                               lem:twoturnings, the two figure captions, sec:lift-initial-rate
NOTHING HERE FITS ANYTHING.  Every constant is derived below from the published pair and omega_gamma.
"""
import os
import re
import subprocess

import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.optimize import brentq

ROOT = '/home/user/shadow-of-existence'
VERDICTS = []


def arm(n, title, ok, *lines):
    VERDICTS.append((n, ok, title))
    print(f"\n{'=' * 100}\nARM {n} -- {title}\n  [{'PASS' if ok else 'FAIL'}]")
    for ln in lines:
        print(ln)


def read(p):
    with open(os.path.join(ROOT, p), encoding='utf-8') as fh:
        return fh.read()


def git(*a):
    return subprocess.run(['git', *a], cwd=ROOT, capture_output=True, text=True).stdout


def sents(t):
    return [' '.join(s.split()) for s in re.split(r'(?<=[.!?])\s+', t) if s.strip()]


P7 = read('corpus/CR_framework.tex')
P7L = P7.splitlines()

# ---------------------------------------------------------------- the constants, derived not quoted
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
RT = (TWOM * ALPHA ** 2) ** (1 / 3)          # the comoving turnaround, 1 - f = 0, on the VACUUM cut

print("=" * 100)
print("r7778 (60) -- the lift on the bent cut (the remainder of r7763's item 2)")
print(f"  HEAD: {git('rev-parse', 'HEAD').strip()}   origin/main: {git('rev-parse', 'origin/main').strip()}")
print(f"  shallow clone: {git('rev-parse', '--is-shallow-repository').strip()};"
      f"  commits from HEAD: {git('rev-list', '--count', 'HEAD').strip()}")
print(f"  derived: alpha={ALPHA:.3f} Mpc  r0={R0:.3f} Mpc  2M={TWOM:.4f} Mpc  K={KRAD:.3f} Mpc^2")
print(f"           the vacuum comoving turnaround r_t = (2M alpha^2)^(1/3) = {RT:.3f} Mpc")
print(f"           pi*alpha/3 = {np.pi * ALPHA / 3:.6f} Mpc    K/2M = {KRAD / TWOM:.6f} Mpc")
print("=" * 100)

# ======================================================================  A -- WHAT THE FORK IS ABOUT
r, Mu, al = sp.symbols('r mu alpha', positive=True)
TwoMs, Ks = sp.symbols('twoM K', positive=True)
f = 1 - Mu / r - r ** 2 / al ** 2

# -- ARM 1 ---------------------------------------------------------------------------------------
CONDITIONS = [
    ('the Nariai condition  Lambda G^2 M^2/c^4 = 1/9  (<=> 2M = 2 alpha/(3 sqrt 3))',
     2 * al / (3 * sp.sqrt(3)) - TwoMs),
    ('the unit-speed seams     f = 0', f),
    ('the comoving turnaround  1 - f = 0', 1 - f),
    ('the Euclidean null       f = 2', f - 2),
    ("the contour radicand     (dr/dtau)^2 = 1 - f", 1 - f),
    ('the rate                 h^2 = mu/r^3 + 1/alpha^2', Mu / r ** 3 + 1 / al ** 2),
]
rows, bare = [], []
for name, expr in CONDITIONS:
    d = sp.simplify(sp.diff(expr, Mu))
    if d == 0:
        rows.append((name, 'does not involve mu at all'))
        continue
    power = None
    for n in (0, 1, 2, 3, 4):
        if sp.simplify(d * r ** n).free_symbols.isdisjoint({r}):
            power = n
            break
    rows.append((name, f'mu enters as mu/r^{power}' if power else 'mu enters BARE'))
    if power == 0:
        bare.append(name)
arm(1, 'which object each of the six bead conditions uses', not bare,
    *[f'    {nm:<62s} -> {how}' for nm, how in rows],
    f'  bare-mu conditions among the six: {len(bare)}  {bare}',
    "  => the fork r7776 posed about mu is posed about an object no enumerated condition uses alone"
    if not bare else "  => the fork SURVIVES at the condition(s) listed above")

# -- ARM 2 ---------------------------------------------------------------------------------------
mu_bent = TwoMs + Ks / r
rad = sp.expand((1 - f).subs(Mu, mu_bent))
rad_flip = sp.expand(rad.subs(r, -r))
k_even = sp.simplify(rad.coeff(Ks) - rad_flip.coeff(Ks)) == 0
m_odd = sp.simplify(rad.coeff(TwoMs) + rad_flip.coeff(TwoMs)) == 0
num_chk = []
for s in (1e-3, 1.0, 1e3, RT):
    a = KRAD / s ** 2
    b = TWOM / s
    num_chk.append((s, a, b))
arm(2, 'the parity of the radiation term in the contour radicand', bool(k_even and m_odd),
    f'    1 - f  =  {rad}',
    f'    r -> -r:  {rad_flip}',
    f'    the K term is EVEN:        {bool(k_even)}',
    f'    the 2M term is ODD:        {bool(m_odd)}',
    *[f'      |r| = {s:<12.4g}  K/r^2 = {a:.6e} (same sign at -|r|)   2M/r = {b:.6e} (flips)'
      for s, a, b in num_chk],
    '  => radiation enters the comoving velocity with the SAME sign on both branches')

# -- ARM 3 ---------------------------------------------------------------------------------------
def h2(rr):
    return (TWOM + KRAD / rr) / rr ** 3 + 1.0 / ALPHA ** 2


rad_share = [(s, KRAD / s ** 4, KRAD / (-s) ** 4) for s in (1e-3, 1.0, 1e3, RT)]
pos_both = all(abs(p - m) / p < 1e-14 and p > 0 for _, p, m in rad_share)
arm(3, "the parity and sign of radiation's contribution to the rate", pos_both,
    *[f'    |r| = {s:<12.4g}  K/r^4 at +|r| = {p: .6e}   at -|r| = {m: .6e}' for s, p, m in rad_share],
    '  => the radiation term in the RATE is even and positive on both branches;',
    "     r7776's 'a negative radiation term is not radiation' was about mu's bookkeeping in a",
    '     SIGNED coordinate, and not about a density')

# -- ARM 4 ---------------------------------------------------------------------------------------
tau = sp.Symbol('tau', real=True)
r0s = (TwoMs * al ** 2) ** sp.Rational(1, 3)
r_conj = -r0s * sp.cosh(3 * tau / (2 * al)) ** sp.Rational(2, 3)
resid_sym = sp.simplify(sp.diff(r_conj, tau) ** 2 - (TwoMs / r_conj + r_conj ** 2 / al ** 2))
sub = {TwoMs: TWOM, al: ALPHA}
F_ok = sp.lambdify(tau, (sp.diff(r_conj, tau) ** 2).subs(sub), 'numpy')
G_ok = sp.lambdify(tau, (TwoMs / r_conj + r_conj ** 2 / al ** 2).subs(sub), 'numpy')
G_flip = sp.lambdify(tau, (-TwoMs / r_conj + r_conj ** 2 / al ** 2).subs(sub), 'numpy')
samples = np.linspace(0.05, 4.0, 9) * ALPHA
rel_ok = max(abs(F_ok(t) - G_ok(t)) / abs(G_ok(t)) for t in samples)
rel_flip = min(abs(F_ok(t) - G_flip(t)) / abs(G_flip(t)) for t in samples)
sent_R = [s for s in sents(P7) if r'2M\mapsto-2M' in s or r'2M \mapsto -2M' in s]
sent_cont = [s for s in sents(P7) if 'Continuing $r$ onto the signed lap' in s]
arm(4, "thm:bead's continuation holds 2M fixed; R = gamma^5 also flips it, and they are two maps",
    rel_ok < 1e-12 and rel_flip > 1e-3 and bool(sent_R) and bool(sent_cont),
    f'    symbolic residual with 2M POSITIVE:  {resid_sym}',
    f'    worst relative residual, 2M positive, 9 samples across the collapse leg: {rel_ok:.3e}',
    f'    best  relative residual with 2M -> -2M in the ODE only (the control):   {rel_flip:.3e}',
    f'    sentences carrying the mass reflection 2M -> -2M: {len(sent_R)}',
    f'    sentences carrying the theorem continuation of r: {len(sent_cont)}',
    *[f'      [R]    ...{s[:200]}' for s in sent_R[:2]],
    *[f'      [cont] ...{s[:200]}' for s in sent_cont[:1]],
    '  => the DYNAMICAL continuation signs r and keeps 2M; R = gamma^5 is a separate,',
    '     representational reflection -- r7776 read the second into the first')

# ==========================================================  B -- WHAT THE BEND DOES TO THE LIFT
def radicand(s, K):
    """(dr/dtau)^2 at r = -s, s > 0:  -2M/s + K/s^2 + s^2/alpha^2.  NEGATIVE => the lift."""
    return -TWOM / s + K / s ** 2 + s ** 2 / ALPHA ** 2


# -- ARM 5 ---------------------------------------------------------------------------------------
quart = np.roots([1.0 / ALPHA ** 2, 0.0, 0.0, -TWOM, KRAD])
pos = sorted(float(x.real) for x in quart if abs(x.imag) < 1e-7 * max(1.0, abs(x.real)) and x.real > 0)
ref = []
for g in pos:
    lo, hi = g * (1 - 1e-6), g * (1 + 1e-6)
    try:
        ref.append(brentq(lambda s: radicand(s, KRAD), lo, hi, xtol=1e-14))
    except ValueError:
        ref.append(g)
s_in, s_out = (ref[0], ref[-1]) if len(ref) >= 2 else (None, None)
guess = KRAD / TWOM
ok5 = (len(ref) == 2 and s_in is not None and 0.5 * guess < s_in < 2.0 * guess)
arm(5, 'the lift gains an inner boundary: two roots at r < 0, not one', ok5,
    f'    real positive roots of  s^4/alpha^2 - 2M s + K = 0 :  {len(ref)}',
    *[f'      s = {x:.9f} Mpc   (r = {-x:.9f})' for x in ref],
    f'    the registered estimate K/2M = {guess:.6f} Mpc;  inner root/estimate = '
    f'{(s_in / guess if s_in else float("nan")):.9f}',
    f'    vacuum cut, for comparison: the radicand is negative on exactly -r_t < r < 0, r_t = {RT:.3f}',
    '  => the imaginary excursion is an interval strictly inside (-r_t, 0): it does NOT reach r = 0')

# -- ARM 6 ---------------------------------------------------------------------------------------
if s_out:
    d_abs = RT - s_out
    d_rel = d_abs / RT
    ok6 = d_abs > 0 and d_rel < 1e-2
else:
    d_abs = d_rel = float('nan')
    ok6 = False
arm(6, "the outer root's displacement: the comoving turnaround moves inward", ok6,
    f'    vacuum  |r| = {RT:.6f} Mpc',
    f'    bent    |r| = {(s_out if s_out else float("nan")):.6f} Mpc',
    f'    inward by {d_abs:.6f} Mpc  =  {d_rel:.6e} relative',
    f'    the registered scale K/(2M r_t) = {KRAD / (TWOM * RT):.6e}')

# -- ARM 7 ---------------------------------------------------------------------------------------
def im_accum(K, lo, hi):
    """|Im tau| accumulated across the lift: integral of ds / sqrt(-radicand)."""
    return quad(lambda s: 1.0 / np.sqrt(max(-radicand(s, K), 1e-300)), lo, hi, limit=400)[0]


im_vac = im_accum(0.0, 0.0, RT)
target = np.pi * ALPHA / 3.0
rel_vac = abs(im_vac - target) / target
im_bent = im_accum(KRAD, s_in, s_out) if s_in else float('nan')
rel_bent = (im_bent - target) / target
ok7 = rel_vac <= 1e-8 and im_bent < target and abs(rel_bent) <= 1e-3
arm(7, "the printed bound pi*alpha/3 is independent of M and NOT independent of K", ok7,
    f'    vacuum cut, by quadrature over (0, r_t):   |Im tau| = {im_vac:.9f} Mpc',
    f'    pi*alpha/3                                           = {target:.9f} Mpc',
    f'    relative agreement: {rel_vac:.3e}   (the paper: "fixed by the exponent, independent of M")',
    f'    bent cut, over the lift ({s_in:.6f}, {s_out:.6f}): |Im tau| = {im_bent:.9f} Mpc'
    if s_in else '    bent cut: no lift found',
    f'    shortfall against the printed bound: {target - im_bent:.9f} Mpc = {-rel_bent:.6e} relative',
    '  => the bend SHORTENS the imaginary excursion; the bound carries K')

# -- ARM 8 ---------------------------------------------------------------------------------------
def segments(K):
    grid = np.concatenate([np.logspace(-8, np.log10(5e4), 20000)])
    sg = np.sign(radicand(grid, K))
    out, cur, start = [], sg[0], grid[0]
    for g, s in zip(grid[1:], sg[1:]):
        if s != cur:
            out.append((start, g, cur))
            cur, start = s, g
    out.append((start, grid[-1], cur))
    return out


seg_v, seg_b = segments(0.0), segments(KRAD)
n_v = sum(1 for a, b, s in seg_v if s < 0) + sum(1 for a, b, s in seg_v if s > 0)
n_b = sum(1 for a, b, s in seg_b if s < 0) + sum(1 for a, b, s in seg_b if s > 0)
arm(8, 'the lap gains a segment: three becomes four', n_b == n_v + 1,
    f'    vacuum cut, |r| in (1e-8, 5e4):  {len(seg_v)} segment(s)',
    *[f'      |r| {a:12.6g} .. {b:12.6g}   radicand {"POSITIVE (Re tau advances)" if s > 0 else "NEGATIVE (the lift)"}'
      for a, b, s in seg_v],
    f'    bent cut:                        {len(seg_b)} segment(s)',
    *[f'      |r| {a:12.6g} .. {b:12.6g}   radicand {"POSITIVE (Re tau advances)" if s > 0 else "NEGATIVE (the lift)"}'
      for a, b, s in seg_b],
    '  => on the conjugate side the branch point is reached in REAL cosmic time on the bent cut')

# -- ARM 9 ---------------------------------------------------------------------------------------
def tau_conj(s):
    return quad(lambda x: 1.0 / np.sqrt(radicand(x, KRAD)), 1e-14, s, limit=400)[0]


lo_s, hi_s = 1e-4, 1e-3
t_lo, t_hi = tau_conj(lo_s), tau_conj(hi_s)
expo = (np.log(hi_s) - np.log(lo_s)) / (np.log(t_hi) - np.log(t_lo))
real_there = all(radicand(x, KRAD) > 0 for x in np.logspace(-14, np.log10(hi_s), 50))
ok9 = abs(expo - 0.5) <= 1e-3 and real_there
arm(9, "the approach from the conjugate side is radiation's, and in real cosmic time", ok9,
    f'    tau(1e-4 Mpc) = {t_lo:.9e} Mpc      tau(1e-3 Mpc) = {t_hi:.9e} Mpc',
    f'    d ln|r| / d ln|tau| = {expo:.6f}       (radiation 1/2, dust 2/3)',
    f'    radicand positive on the whole interval (tau real): {real_there}',
    f"    r7776 measured 0.500022 on the MATTER branch over the same decade",
    '  => the same radiation exponent on both branches, as arm 2 requires')

# -- ARM 10 --------------------------------------------------------------------------------------
pairs = []
for s in (1e-3, 1.0, RT):
    hp, hm = h2(s), h2(-s)
    pairs.append((s, hp, hm, abs(hp - hm) / abs(hp)))
near, far = pairs[0], pairs[-1]
ok10 = near[3] < 1e-8 and far[3] > 0.5
arm(10, 'the two branches\' rates at the same areal radius', ok10,
    *[f'    |r| = {s:<12.4g}  h^2(+|r|) = {hp: .9e}   h^2(-|r|) = {hm: .9e}   rel diff {d:.6e}'
      for s, hp, hm, d in pairs],
    f'    the registered number was "better than 1e-8 at |r| = 1e-3": measured {near[3]:.6e}',
    f'    the exact relative difference is 2 (2M/K) |r| = {2 * TWOM / KRAD * 1e-3:.6e} at 1e-3 Mpc',
    '  => the qualitative half holds (radiation even, dust odd, order unity at r_t); the registered',
    '     THRESHOLD was wrong, and wrong by a factor this line could have computed before',
    f'     registering: agreement reaches 1e-8 only below |r| ~ {1e-8 * KRAD / (2 * TWOM):.3e} Mpc')

# ================================================  C -- WHAT THIS CANNOT SETTLE, AS AN ARM
def region(start_pat, end_pat, after=0):
    i = next(k for k, ln in enumerate(P7L) if k >= after and start_pat in ln)
    j = next(k for k, ln in enumerate(P7L) if k > i and end_pat in ln)
    return '\n'.join(P7L[i:j + 1])


THEO = next(k for k, ln in enumerate(P7L) if r'\begin{theorem}[The cosmogenetic bead]' in ln)
REGIONS = [
    ('the theorem', region(r'\begin{theorem}[The cosmogenetic bead]', r'\end{theorem}')),
    ('its proof', region(r'\begin{proof}', r'\end{proof}', after=THEO)),
    ('rem:head-admissible', region(r'\begin{remark}[The prior universe is not a premise', r'\end{remark}')),
    ('the scope paragraph', region(r'\noindent\emph{Scope.}', r'\begin{lemma}[Two turnings]')),
    ('lem:twoturnings', region(r'\begin{lemma}[Two turnings]', r'\end{lemma}')),
    ('caption fig:dS_SdS (C)', next(ln for ln in P7L if 'The layered handoff at the branch point' in ln)),
    ('caption of the lap figure', next(ln for ln in P7L if 'The lap in position, speed and acceleration' in ln)),
    ('sec:lift-initial-rate', '\n'.join(P7L[1192:1502])),
]
CONTENT = ('nucleosynthesis', 'plasma', 'radiation', 'the cooling leg', 'depositing', 'acoustic')
hits = []
for nm, txt in REGIONS:
    for s in sents(txt):
        low = s.lower()
        if any(w in low for w in CONTENT) and ('collapse leg' in low or 'cooling leg' in low
                                               or 'conjugate' in low or 'branch point' in low):
            hits.append((nm, s))
arm(11, 'the honest form of the fork: a disjunction over the progenitor, and what the text assigns',
    len(hits) > 0,
    f'    regions searched: {len(REGIONS)}  -- {[nm for nm, _ in REGIONS]}',
    '    *** THE REGISTRATION CALLED THESE "SEVEN PLACES" AND THEN LISTED EIGHT.'
    '  Eight were searched. ***',
    f'    sentences assigning content near the collapse leg / branch point: {len(hits)}',
    *[f'      [{nm}] {s[:260]}' for nm, s in hits[:6]],
    '  => nothing measured here says the progenitor branch CARRIES radiation; it says no sign',
    '     obstruction forbids it.  The fork is a disjunction over the progenitor, not a contradiction')

# ==================================================================================== the verdict
print(f"\n{'=' * 100}")
npass = sum(1 for _, ok, _ in VERDICTS if ok)
print(f"ARMS: {npass} of {len(VERDICTS)} meet their criterion")
for n, ok, title in VERDICTS:
    print(f"  {'PASS' if ok else 'FAIL'}  arm {n:>2}  {title}")
print(f"REGISTERED ARM COUNT: 11   MEASURED ARM COUNT: {len(VERDICTS)}")
print('=' * 100)
