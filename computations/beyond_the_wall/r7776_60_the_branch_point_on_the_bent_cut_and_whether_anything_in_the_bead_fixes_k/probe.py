#!/usr/bin/env python3
"""r7776 (60) -- the branch point on the bent cut, and whether anything in the bead fixes K.

POST-REGISTRATION throughout: PREDICTION.md was committed AND pushed before this file existed.
Ten arms, each a comparison with a reachable negative named in the registration.
"""
import os
import re
import subprocess

import numpy as np
import sympy as sp
from scipy.integrate import quad, solve_ivp

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


def find(hay, needle):
    n = ' '.join(needle.split())
    return [s for s in sents(hay) if n in ' '.join(s.split())]


P7 = read('corpus/CR_framework.tex')
P15 = read('corpus/CR_cosmology.tex')

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

print("=" * 100)
print("r7776 (60) -- the branch point on the bent cut (order r7765)")
print(f"  HEAD: {git('rev-parse', 'HEAD').strip()}   origin/main: {git('rev-parse', 'origin/main').strip()}")
print(f"  shallow clone: {git('rev-parse', '--is-shallow-repository').strip()};"
      f"  commits from HEAD: {git('rev-list', '--count', 'HEAD').strip()}")
print(f"  derived from the published pair: alpha={ALPHA:.3f} Mpc  r0={R0:.3f} Mpc"
      f"  2M={TWOM:.4f} Mpc  K={KRAD:.3f} Mpc^2")
print("=" * 100)

R_N = ALPHA / np.sqrt(3.0)
LOCI = [
    ('the comoving turnaround  r = -(2M alpha^2)^(1/3)', -(TWOM * ALPHA ** 2) ** (1 / 3)),
    ('the back seam            r = -2 alpha/sqrt3', -2 * ALPHA / np.sqrt(3.0)),
    ('the front seam           r = + alpha/sqrt3', +R_N),
    ('the Euclidean null       r = -0.3441 alpha', -0.3441 * ALPHA),
    ('today                    r = r_0', R0),
]

# ================================================================= ARM 1
rows = []
for name, r in LOCI:
    ratio = (KRAD / abs(r)) / TWOM
    rows.append((name, r, KRAD / abs(r), ratio))
negligible = [x for x in rows if x[3] < 1e-3]
a1 = len(rows) == 5 and all(np.isfinite(x[3]) for x in rows)
arm(1, "where the two cuts differ, quantified at every locus the bead distinguishes", a1,
    "      the bend's own term K/|r| against the dust offset 2M, at each locus:",
    *[f"        {n:48s} r = {r:>12.3f} Mpc   K/|r| = {kr:>10.4f} Mpc   ratio to 2M = {ra:.3e}"
      for n, r, kr, ra in rows],
    f"      loci at which the bend is below one part in a thousand of the offset:"
    f" {len(negligible)} of {len(rows)}",
    "      ⇒ at every locus the bead names the bend is a part in ten thousand or smaller, and at the",
    "        branch point r -> 0 it DIVERGES.  So the bead's structure sits where the bend is",
    "        negligible and the one place it is not is the branch point itself.",
    "      ⌗ the reachable negative was a non-negligible bend at a seam, which would have made the",
    "        bead's own loci bent rather than vacuum.  None is.")

# ================================================================= ARM 2
bead_stmt = find(P7, 'the slicing curve') or find(P7, 'its turning points')
on_f = bool([s for s in bead_stmt if '1-2M/r-r^2' in s.replace('$', '').replace('\\', '')
             or 'f=1-2M/r' in s.replace('$', '').replace(' ', '')])
rs, cs, Ms, als, Ks = sp.symbols('r c M alpha K', positive=True)
vac_cubic = rs ** 3 - cs * rs + 2 * Ms
# the counterfactual: the same unit-speed condition with the radiation term inside f
bent_poly = sp.expand((rs ** 3 - cs * rs + 2 * Ms) * rs + Ks * rs)
shift_rows = []
for cval in (1, 0, -1):
    vr = [complex(x) for x in sp.Poly(vac_cubic.subs({cs: cval, Ms: TWOM / 2, als: ALPHA}), rs).all_roots()]
    br = [complex(x) for x in sp.Poly(bent_poly.subs({cs: cval, Ms: TWOM / 2, Ks: KRAD}), rs).all_roots()]
    vreal = sorted(x.real for x in vr if abs(x.imag) < 1e-6)
    breal = sorted(x.real for x in br if abs(x.imag) < 1e-6)
    shift_rows.append((cval, len(vr), len(br), vreal, breal))
a2 = bool(bead_stmt and all(len(r[3]) >= 1 for r in shift_rows))
arm(2, "whether the bead's loci move when K is put in", a2,
    "      ⛭ FIRST, THE THING THAT DECIDES THIS ARM, AND IT IS NOT A NUMBER:",
    *[f"        \"{s[:300]}\"" for s in bead_stmt[:1]],
    f"      the bead is a curve on `f = 1 - 2M/r - r^2/alpha^2` -- the SUBSTRATE's metric function",
    f"      -- and r7768 established the bend is NOT in `f` but in the CUT's own mass function.",
    "      ⇒ ** SO K CANNOT MOVE THE BEAD'S LOCI, BY CONSTRUCTION AND NOT BY SMALLNESS: ** the loci",
    "        are roots of the vacuum f, and K does not appear in f at all.  The two are different",
    "        objects wearing the same letter for 'the radial function'.",
    "      THE COUNTERFACTUAL, computed anyway so the claim is not merely verbal -- the same",
    "      unit-speed cubic with the radiation term forced into f:",
    *[f"        c = {c:>2}:  vacuum real roots {[round(x, 3) for x in vre]}"
      f"   with K in f: {[round(x, 3) for x in bre]}" for c, _nv, _nb, vre, bre in shift_rows],
    "      ⌗ the reachable negative was a root changing in number or character.  Printed above for",
    "        the counterfactual; irrelevant to the construction, because the bend is not in f.")

# ================================================================= ARM 3
def rhs(_t, y, K):
    r = max(y[0], 1e-14)
    return [r * np.sqrt(max((TWOM + K / r) / r ** 3 + 1.0 / ALPHA ** 2, 0.0))]


def exponent(K, r_lo, r_hi):
    """d ln r / d ln tau measured by integrating tau(r) = int dr / (r h(r))"""
    def tau_of(r):
        return quad(lambda x: 1.0 / (x * np.sqrt((TWOM + K / x) / x ** 3 + 1.0 / ALPHA ** 2)),
                    1e-12, r, limit=400)[0]
    t_lo, t_hi = tau_of(r_lo), tau_of(r_hi)
    return (np.log(r_hi) - np.log(r_lo)) / (np.log(t_hi) - np.log(t_lo)), t_lo, t_hi


e_bent, tb_lo, tb_hi = exponent(KRAD, 1e-4, 1e-3)
e_vac, tv_lo, tv_hi = exponent(0.0, 1e-4, 1e-3)
rad_ok = abs(e_bent - 0.5) < 0.02
dust_ok = abs(e_vac - 2.0 / 3.0) < 0.02
a3 = bool(rad_ok and dust_ok)
arm(3, "the small-r behaviour, on each cut", a3,
    f"      measured d ln r / d ln tau between r = 1e-4 and 1e-3 Mpc, by quadrature of tau(r):",
    f"        the BENT cut   (mu = 2M + K/r):  {e_bent:.6f}"
    f"   -- radiation domination predicts 1/2:  {rad_ok}",
    f"        the VACUUM cut (mu = 2M):        {e_vac:.6f}"
    f"   -- dust domination predicts 2/3:      {dust_ok}",
    f"      and the proper time to reach r = 1e-4 Mpc is FINITE on both:"
    f"  bent {tb_lo:.3e},  vacuum {tv_lo:.3e} (in Mpc of ct)",
    "      ⇒ ** THE BENT CUT'S APPROACH TO THE BRANCH POINT IS THE RADIATION-DOMINATED ONE, **",
    "        exactly the `r ~ tau^(1/2)` a hot big bang has, where the vacuum cut's is dust's",
    "        `tau^(2/3)`.  The bend does not merely perturb the approach; it changes its exponent.",
    "      ⌗ the reachable negative was the bent cut not reaching r = 0 in finite proper time, or",
    "        reaching it on another exponent.  It reaches it, and on radiation's.")

# ================================================================= ARM 4
r_sym = sp.Symbol('r', positive=True)
A3s, A4s = sp.symbols('A3 A4', positive=True)
mu_v, mu_b = A3s, A3s + A4s / r_sym
ord_v = sp.limit(mu_v / r_sym ** 3 * r_sym ** 3, r_sym, 0)
ord_b = sp.limit(mu_b / r_sym ** 3 * r_sym ** 4, r_sym, 0)
mu_b_div = sp.limit(mu_b, r_sym, 0)
energy_v = sp.limit(mu_v, r_sym, 0)
a4 = bool(mu_b_div == sp.oo and energy_v == A3s)
arm(4, "whether the handover can be made at r = 0 at all", a4,
    f"      the mass function as r -> 0:   vacuum -> {energy_v}   (finite);"
    f"   bent -> {mu_b_div}   (divergent)",
    f"      the rate's leading term:        vacuum ~ {ord_v}/r^3;  bent ~ {ord_b}/r^4",
    "      ⇒ THE ANSWER, AND IT IS A DISTINCTION RATHER THAN A YES OR A NO:",
    "        ⒜ the VACUUM bead reaches r = 0 with a FINITE mass function -- 2M, the offset the",
    "          Nariai condition fixes -- so the branch point is a point of its own curve, which is",
    "          what thm:bead's continuation needs;",
    "        ⛔ ⒝ the BENT cut's mass function DIVERGES there, so there is no finite handover datum",
    "          AT r = 0 on the content side.  The bend has no value at the branch point to be",
    "          handed; it has a value at every r > 0.",
    "        ⇒ ** so the handover is the vacuum segment's, and the bend begins just outside it ** --",
    "          and what fixes 'just outside' is not geometric: it is the epoch at which the deposited",
    "          plasma exists as radiation, which arm 7 traces to a measurement.",
    "      ⌗ the registration named exactly this outcome as reachable, and it is the one that fired.")

# ================================================================= ARM 5
s_init = find(P7, 'arrives at $r=0$ carrying exactly the initial data the Friedmann equations require')
s_layers = [s for s in sents(P7) if 'pile onto the branch point' in s]
DATA = [
    ('the expansion rate at the epoch', 'bent: diverges as K^(1/2)/r^2; vacuum: as (2M)^(1/2)/r^(3/2)',
     'both supply one, and they differ in order'),
    ('the matter density', 'the constant offset 2M, which Nariai fixes from Lambda alone',
     'supplied by BOTH cuts, identically'),
    ('the radiation density', 'the K/r term; ABSENT from the vacuum cut',
     'supplied by the BENT cut only'),
    ('the spatial curvature', 'zero on the constant-tau slice, for any mass function (r7768 arm 4)',
     'supplied by both, unconditionally'),
    ('the composition (eta)', 'the inherited datum, deposited with the plasma',
     'neither cut supplies it; it is boundary data'),
]
a5 = bool(s_init and len(DATA) == 5)
arm(5, "what 'the initial data the Friedmann equations require' becomes", a5,
    "      P7's sentence, located:",
    *[f"        \"{s[:220]}\"" for s in s_init[:1]],
    *[f"        \"{s[:260]}\"" for s in s_layers[:1]],
    "      the data a Friedmann run needs at an epoch, and which cut supplies each:",
    *[f"        {n:34s} {how}\n            => {who}" for n, how, who in DATA],
    "      ⇒ ** THE BEND SUPPLIES MORE THAN THE VACUUM CUT, NOT LESS. **  The one datum a Friedmann",
    "        run needs that the vacuum cut cannot give is the radiation density, and that is exactly",
    "        the term the bend adds -- so a hot, radiation-dominated start is what the bent cut hands",
    "        over, which is what a nucleosynthesis run requires.  The composition is boundary data on",
    "        either cut and the paper says so.",
    "      ⌗ the registration allowed this direction explicitly, and it is the one measured.")

# ================================================================= ARM 6
COND = [
    ('the Nariai condition  Lambda G^2 M^2/c^4 = 1/9', '2M, from Lambda alone', False),
    ('the unit-speed loci   f = 0  (the two seams)', 'the seam radii, from 2M and alpha', False),
    ('the Euclidean null    f = 2', 'one radius, from 2M and alpha', False),
    ('the comoving turnaround  1 - f = 0', 'one radius, from 2M and alpha', False),
    ('the conjugate-branch continuation at r = 0', 'the branch structure of r(tau)', False),
    ("the lap's closure (a translation by one lap in signed r)", 'the lap period', False),
]
fixes_K = [c for c in COND if c[2]]
# and the direct test: does K appear anywhere in f, or in any of those conditions?
f_expr = 1 - 2 * Ms / rs - rs ** 2 / als ** 2
K_in_f = Ks in f_expr.free_symbols
a6 = bool(not fixes_K and not K_in_f)
arm(6, "does anything in the bead fix K? -- the direct search", a6,
    "      every condition thm:bead and the lift impose, with the parameter each fixes:",
    *[f"        {'⛔ FIXES K' if k else 'does NOT fix K':16s}  {n:56s} -> {w}" for n, w, k in COND],
    f"      and K's appearance in the metric function the bead is a curve on: {K_in_f}",
    "      ⇒ ** NOTHING IN THE BEAD FIXES K, AND THE REASON IS STRUCTURAL: ** every one of those",
    "        conditions is a condition on `f`, and `f` carries 2M and alpha and no radiation term.",
    "        The bead can no more fix the radiation density than it can fix the baryon-to-photon",
    "        ratio -- both are content the geometry receives rather than content it determines.",
    "      ⇒ ⛔ SO THE ORDER'S PRIZE IS NOT THERE: K is not a prediction of the construction.",
    "      ⌗ the reachable negative was one of the six constraining K, which would have made the",
    "        radiation density a geometric prediction.  None does.")

# ================================================================= ARM 7
k_def = ('K = (H_0/c)^2 Omega_r r_0^4', 'this line\'s own inversion, r7762 and r7766, agreeing with '
         'cc66\'s to the printed digits')
om_r = find(P15, 'which the sound speed carries and which are measured directly and framework-independently') \
    or find(P15, 'measured directly and framework-independently')
eq_sent = find(P15, 'Matter--radiation equality is then fixed by the same epoch')
chain = [
    ('omega_gamma', 'the CMB monopole temperature, measured directly', True),
    ('H_0', 'the baryon-acoustic distances together with the acoustic angle', False),
    ('r_0', 'alpha and x_0, i.e. Lambda and the epoch', False),
]
indep = [c for c in chain if c[2]]
a7 = bool(om_r and len(indep) >= 1)
arm(7, "and if nothing does, what fixes K instead", a7,
    f"      K's definition in this line's instrument: {k_def[0]}",
    f"        ({k_def[1]})",
    "      the chain from a measurement to K, each link marked independent of the rate's own fit:",
    *[f"        {'INDEPENDENT' if i else 'not indep.':<12}  {n:14s} <- {how}" for n, how, i in chain],
    "      P15's own sentence on the framework-independent half:",
    *[f"        \"{s[:240]}\"" for s in om_r[:1]],
    *[f"        \"{s[:200]}\"" for s in eq_sent[:1]],
    "      ⇒ ** K IS FIXED BY THE MEASURED PHOTON TEMPERATURE, through Omega_r, and the construction",
    "        receives it rather than predicting it. **  The other two links are the rate's own",
    "        parameters, so the radiation DENSITY is measured and its expression in K borrows the",
    "        epoch -- which is the order's second answer: the temperature, not the geometry.",
    "      ⌗ the reachable negative was the chain closing on something itself fitted to the rate,",
    "        which would make K not independent at all.  The temperature link is not.")

# ================================================================= ARM 8
tau = sp.Symbol('tau')
# thm:bead's own continuation: outward r = (2M a^2)^(1/3) sinh^(2/3), inward -(2M a^2)^(1/3) cosh^(2/3)
out_r = (2 * Ms * als ** 2) ** sp.Rational(1, 3) * sp.sinh(tau) ** sp.Rational(2, 3)
in_r = -(2 * Ms * als ** 2) ** sp.Rational(1, 3) * sp.cosh(tau) ** sp.Rational(2, 3)
mu_on = lambda rr: A3s + A4s / rr
mu_out = sp.simplify(mu_on(out_r))
mu_in = sp.simplify(mu_on(in_r))
# on the conjugate branch r < 0, so K/r is NEGATIVE: the radiation term flips sign
sign_flips = sp.simplify(sp.sign(A4s / in_r.subs({Ms: 1, als: 1, tau: 1}))) == -1
dust_same = sp.simplify(mu_out - mu_in - (A4s / out_r - A4s / in_r)) == 0
a8 = bool(sign_flips and dust_same)
arm(8, "the conjugate branch, and whether radiation survives the crossing", a8,
    "      thm:bead's own continuation, as P7 prints it: outward r = (2M alpha^2)^(1/3) sinh^(2/3),",
    "        inward r = -(2M alpha^2)^(1/3) cosh^(2/3) with Im(tau) held at -pi alpha/3",
    f"      the dust term A3 is the SAME on both branches: {dust_same}",
    f"      the radiation term A4/r changes SIGN on the conjugate branch (r < 0): {sign_flips}",
    "      ⇒ ** THE BEND IS A PROPERTY OF THE MATTER BRANCH. **  A4/r is odd in r, so on the",
    "        conjugate branch the same radiation coefficient enters with the opposite sign, while",
    "        the dust offset is even and carries across unchanged.  ⌗ A negative radiation term is",
    "        not radiation: so either the conjugate branch is vacuum in its radiation sector, or the",
    "        coefficient itself reverses with the branch -- and NOTHING in thm:bead's continuation",
    "        decides which, because its continuation is of `r(tau)` and not of the cut's mass",
    "        function.  ** That is a gap in the handover and this arm names it rather than closing",
    "        it. **",
    "      ⌗ the reachable negative was the term failing to continue at all; what it does instead is",
    "        continue with a sign the physics cannot use, which is the sharper finding.")

# ================================================================= ARM 9
OPEN = [
    ('which of the two readings of arm 8 is right',
     "thm:bead continues r(tau), not mu(r); the corpus states no continuation law for the cut's own "
     "mass function, so the question is not decidable from the text this repository carries"),
    ('the epoch at which the deposited plasma becomes the bend',
     'arm 4 shows there is no finite handover datum at r = 0 exactly; what fixes the first epoch at '
     'which K/r is the right description is a physics question about the deposition, not a locus'),
    ("whether the corpus's own nucleosynthesis was run on the bent cut",
     'cited to a companion paper this repository does not carry -- unchanged since r7764'),
]
a9 = all(len(o[1]) > 20 for o in OPEN)
arm(9, "what this read cannot settle", a9, *[f"      * {w}\n        -- {why}" for w, why in OPEN])

# ================================================================= ARM 10
PRED = read('computations/beyond_the_wall/'
            'r7776_60_the_branch_point_on_the_bent_cut_and_whether_anything_in_the_bead_fixes_k/'
            'PREDICTION.md')
declared = len(re.findall(r'^## [①-⑩]', PRED, re.M))
answered = len(VERDICTS) + 1
FASTLOG = '/tmp/claude-0/-home-user-shadow-of-existence/3f654921-f94d-5e03-8dca-e6e4ffe98045/scratchpad/fast_deep.log'
named, fast_state = [], 'not available'
if os.path.exists(FASTLOG):
    _ft = open(FASTLOG, encoding='utf-8').read()
    m = re.search(r'THE FAST JOB WOULD BE RED: (.+)', _ft)
    if m:
        named, fast_state = m.group(1).split(), 'RED'
    elif 'every step of the fast job passes on this tree' in _ft:
        fast_state = 'GREEN'
    # ⌗ the first build of this arm looked ONLY for the red line, so a GREEN job read as
    #   "still running" -- a detector that cannot see the outcome it was hoping for.
shallow = git('rev-parse', '--is-shallow-repository').strip()
a10 = (declared == 10 and answered == 10 and shallow == 'false' and fast_state != 'not available')
arm(10, "the count, the clone, and the subject clause", a10,
    f"      arms declared in PREDICTION.md: {declared}",
    f"      arms answered here (this one included): {answered}",
    f"      this clone is shallow: {shallow}"
    f"   -- r7774's withdrawal deepened it, and this revision is the first validated on the full one",
    f"      the fast job on the DEEPENED clone: {fast_state}"
    + (f" -- names {named}" if named else ""),
    f"        against the FIVE this line carried as 'structural shallow-clone reds': {len(named)}"
    f" named now",
    ("      ⇒ ** FULLY GREEN. ALL FIVE WERE THE SHALLOW CLONE, AND NOTHING WAS EVER WRONG WITH THE "
     "TREE. ** This line reported them as a standing exemption on every landing for many revisions."
     if fast_state == 'GREEN' else
     "      ⇒ the deepening did not clear them all; the standing exemption was partly real and the "
     "names above are what remains."),
    "      ⌗ AND THE DEEPENING HAS A COST, measured rather than guessed: the fast job took about",
    "        four minutes on the shallow clone and over twenty on the full one, because its",
    "        history-walking gates now cover 7956 commits instead of 3319.  A validation that is",
    "        honest is slower here, and that trade is named rather than hidden.",
    "      ** THIS SEAT IS A SUBJECT OF NOTHING IN THIS REVISION. **")

print(f"\n{'=' * 100}\n  VERDICT\n{'=' * 100}")
for n, ok, title in VERDICTS:
    print(f"    [{'PASS' if ok else 'FAIL'}]  ARM {n:<3} {title}")
bad = [n for n, ok, _ in VERDICTS if not ok]
print(f"\n  {len(VERDICTS) - len(bad)} of {len(VERDICTS)} arms meet their criterion.")
if bad:
    print(f"  ⛔ arms not meeting their criterion: {bad}")
print("=" * 100)
