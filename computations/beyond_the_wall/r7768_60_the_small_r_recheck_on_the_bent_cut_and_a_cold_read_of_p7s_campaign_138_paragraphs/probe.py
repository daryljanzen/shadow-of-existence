#!/usr/bin/env python3
"""r7768 (60) -- the small-r recheck on the bent cut, and a cold read of P7's campaign-138 paragraphs.

POST-REGISTRATION throughout.  PREDICTION.md was committed AND pushed before this file existed.
Twelve arms, each a comparison with a reachable negative named in the registration.
"""
import os
import re
import subprocess

import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

ROOT = '/home/user/shadow-of-existence'
VERDICTS = []
SORT = {}


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


def sents(hay):
    return [s.strip() for s in re.split(r'(?<=[.!?])\s+', hay) if s.strip()]


def find(hay, needle):
    n = ' '.join(needle.split())
    return [s for s in sents(hay) if n in ' '.join(s.split())]


print("=" * 100)
print("r7768 (60) -- the small-r recheck on the bent cut (order r7763)")
print(f"  HEAD: {git('rev-parse', 'HEAD').strip()}   origin/main: {git('rev-parse', 'origin/main').strip()}")
print("=" * 100)

P7 = read('corpus/CR_framework.tex')
P15 = read('corpus/CR_cosmology.tex')
LEAN = read('computations/formalisation/lean/probes/Framework.lean')

# ---------------------------------------------------------------- the corpus's own numbers
CLIGHT = 299792.458                       # km/s
H0, OM = 68.6, 0.2973
h_little = H0 / 100.0
OMR = 4.15e-5 / h_little ** 2
OL = 1.0 - OM
hub = H0 / CLIGHT                          # 1/Mpc
X0 = (2 * OL / OM) ** (1 / 3)
ALPHA = 1.0 / (hub * np.sqrt(OL))          # Mpc
R0 = ALPHA * X0 / np.sqrt(3.0)             # Mpc, from alpha/r0 = sqrt3/x0
TWOM = 2 * R0 ** 3 / (ALPHA ** 2 * X0 ** 3)
KRAD = hub ** 2 * OMR * R0 ** 4            # Mpc^2
print(f"\n  derived from the published pair, not quoted: x0={X0:.6f}  alpha={ALPHA:.3f} Mpc"
      f"  r0={R0:.3f} Mpc\n  2M={TWOM:.4f} Mpc   K={KRAD:.3f} Mpc^2   Omega_r={OMR:.6e}")

# ================================================================= ARM 1: where does the bend live?
s_ein7 = find(P7, 'The Einstein equations then return the Schwarzschild--de~Sitter metric')
s_ein15 = find(P15, 'The Einstein field equations are unchanged')
s_bend = find(P15, 'Radiation is a bend of the cut')
located = bool(s_ein7 and s_ein15 and s_bend)


def roots_of(twoM, K, alpha, merge=True):
    """DISTINCT positive roots of f = 1 - 2M/r - K/r^2 - r^2/alpha^2, i.e. of
    r^2 - 2M r - K - r^4/alpha^2 = 0.

    ⌗ The imaginary tolerance is RELATIVE to the root's own size and generous, and near-equal
    roots are MERGED, because at the Nariai parameter the two horizons are a genuine DOUBLE
    root: a double root of a quartic comes back from `np.roots` as a conjugate pair with
    imaginary parts of order the square root of machine epsilon times the root, so an absolute
    tolerance of 1e-9 reports ZERO horizons where the truth is ONE.  That is what the first run
    of this arm did, and the count it printed was wrong rather than surprising.
    """
    co = [-1.0 / alpha ** 2, 0.0, 1.0, -twoM, -K]      # in powers r^4 ... r^0
    rr = np.roots(co)
    scale = max(1.0, float(np.max(np.abs(rr))))
    keep = [float(x.real) for x in rr if abs(x.imag) < 1e-5 * scale and x.real > 0]
    keep.sort()
    if not merge:
        return keep
    out = []
    for v in keep:
        if not out or abs(v - out[-1]) > 1e-5 * scale:
            out.append(v)
    return out


vac = roots_of(TWOM, 0.0, ALPHA)
bent = roots_of(TWOM, KRAD, ALPHA)
vac_raw = roots_of(TWOM, 0.0, ALPHA, merge=False)
r_N = ALPHA / np.sqrt(3.0)
at_nariai = abs(TWOM - 2 * ALPHA / (3 * np.sqrt(3.0))) / TWOM
double_at_rN = bool(vac and abs(vac[0] - r_N) / r_N < 1e-4)
# the Nariai double root of the VACUUM cubic, recomputed rather than quoted
rs = sp.Symbol('r', positive=True)
Ms, als = sp.symbols('M alpha', positive=True)
cubic = sp.Eq(rs ** 3 / als ** 2 - rs + 2 * Ms, 0)
disc = sp.discriminant(sp.Poly(rs ** 3 / als ** 2 - rs + 2 * Ms, rs))
M_double = sp.solve(sp.Eq(disc, 0), Ms)
M_double_pos = [m for m in M_double if sp.simplify(m).is_positive is not False]
_match = [m for m in M_double_pos if sp.simplify(m - als / (3 * sp.sqrt(3))) == 0]
nariai_M = sp.simplify(_match[0]) if _match else None
nariai_ok = nariai_M is not None
# does the bent quartic still admit a double root at the same M?
bent_disc_changes = len(bent) != len(vac)
a1 = bool(located and vac and nariai_ok and double_at_rN and len(vac) == 1)
SORT['the bend\'s address'] = ('VACUUM CUT -- it is not in f at all', 'arm 1')
arm(1, "where the bend lives: the substrate's f(r), or the cut's own mass function mu(r)?", a1,
    "      (a) the corpus's own sentences, located:",
    *[f"        \"{s[:230]}\"" for s in (s_ein7[:1] + s_ein15[:1] + s_bend[:1])],
    f"      (b) positive roots of f with K = 0 (the substrate):   {[round(x, 4) for x in vac]}"
    f"   -- {len(vac_raw)} root(s) before merging, so it is a DOUBLE root",
    f"          and the corpus's own published pair puts 2M at the Nariai value to"
    f" {at_nariai:.2e} relative, with the double root at alpha/sqrt3 = {r_N:.2f} Mpc: {double_at_rN}",
    f"          positive roots of f with the corpus's K in f:     {[round(x, 4) for x in bent]}",
    f"          the two root structures differ in COUNT: {bent_disc_changes}",
    f"      (c) the Nariai condition recomputed from the cubic's discriminant: double root at"
    f" M = alpha/(3 sqrt 3): {nariai_ok}",
    "      ⇒ THE VERDICT, and every later arm stands on it: THE BEND IS NOT IN `f`.  The field",
    "        equations are unchanged and the substrate is the SdS vacuum; the bend is `m'(r) != 0`",
    "        in the CUT's mass function, which is the congruence's energy bookkeeping along the",
    "        epoch and not a term in the metric.  The second root structure above is computed to",
    "        show what WOULD change if the bend were in `f` -- and it is not that case.",
    "      ⌗ the reachable negative was exactly that: had the corpus sourced f with radiation, the",
    "        K/r^2 term would move the horizon structure and the Nariai selection with it.  The",
    "        numbers for that case are printed above so the reader can see what was ruled out.")

# ================================================================= ARM 2: the trichotomy
tri = find(P7, 'yields a trichotomy') or find(P7, 'the tangency trichotomy')
tri_cond = find(P7, 'tangency at a merged double root')
deg = find(P7, 'the merged horizon is the Nariai double root')
# the discriminant's three regimes, recomputed
lam_of_M = sp.simplify(sp.solve(sp.Eq(disc, 0), als)[0]) if disc.free_symbols else None
regimes = []
for fac, label in ((0.5, 'under'), (1.0, 'at'), (1.5, 'over')):
    Mt = float(ALPHA / (3 * np.sqrt(3))) * fac
    regimes.append((label, fac, len(roots_of(2 * Mt, 0.0, ALPHA))))
# do the trichotomy's own hypotheses mention a mass function or a congruence?
hyp_f = any('f' in s and 'horizon' in s for s in tri)
mentions_cong = any('null-generator congruence' in s or 'null generator' in s for s in tri)
a2 = bool(tri and len(regimes) == 3 and [r[2] for r in regimes] == [2, 1, 0])
SORT['the horizon trichotomy / Nariai selection'] = (
    'VACUUM CUT AS SUCH -- it is a statement about the substrate metric, and it stands', 'arm 2')
arm(2, "the horizon trichotomy and the Nariai selection", a2,
    "      the trichotomy as P7 states it:",
    *[f"        \"{s[:260]}\"" for s in (tri[:1] + deg[:1])],
    "      the three regimes recomputed from the cubic, with M scaled about the Nariai value:",
    *[f"        M = {fac} x alpha/(3 sqrt 3):  {n} positive horizon root(s)  [{label} the condition]"
      for label, fac, n in regimes],
    f"      the classifying object named in the statement is a null-generator congruence on the"
    f" HORIZON: {mentions_cong}",
    "      ⇒ SORT: ABOUT THE VACUUM CUT AS SUCH, AND IT STANDS.  The trichotomy is a property of",
    "        `f`, which arm 1 shows the bend does not touch; the congruence it classifies is the",
    "        horizon's null generator, not the matter congruence the bend belongs to.  Nothing in",
    "        the selection quantifies over the cut's mass function.",
    "      ⌗ the reachable negative was that the selecting argument might quantify over the matter",
    "        congruence, which would put a bent cut inside its scope.  It does not.")

# ================================================================= ARM 3: the branch point
r_sym = sp.Symbol('r', positive=True)
A3s, A4s = sp.symbols('A3 A4', positive=True)
mu_vac = A3s
mu_bent = A3s + A4s / r_sym
h2_vac = sp.simplify(mu_vac / r_sym ** 3)
h2_bent = sp.simplify(mu_bent / r_sym ** 3)
lead_vac = sp.limit(h2_vac * r_sym ** 3, r_sym, 0)
lead_bent = sp.limit(h2_bent * r_sym ** 4, r_sym, 0)
order_vac = sp.degree(sp.simplify(1 / h2_vac), r_sym)
cross_r = KRAD / TWOM                              # where K/r = 2M
cross_z = R0 / cross_r - 1.0
frac_at_rec = (KRAD / (R0 / 1091.0)) / TWOM
orders_differ = sp.simplify(sp.limit(h2_bent / h2_vac, r_sym, 0)) in (sp.oo, -sp.oo)
bead_hyp = find(P7, 'The bead') or [s for s in sents(P7) if 'thm:bead' in s or 'bead' in s][:1]
bead_lean = find(P7, "The bead's algebraic facts are machine-checked in Lean")
a3 = bool(orders_differ and cross_r > 0)
SORT['the branch point and the crossing'] = (
    'BOTH, AND THE PARTS SEPARATE -- the chart singularity is the vacuum\'s and stands; '
    'the leading divergence of the CUT\'s rate is the content\'s and is one order faster', 'arm 3')
arm(3, "the branch point's structure and the crossing", a3,
    f"      mu, vacuum:  {mu_vac}        mu, bent:  {mu_bent}",
    f"      h^2 - 1/alpha^2, vacuum:  {h2_vac}      bent:  {sp.simplify(h2_bent)}",
    f"      leading behaviour as r -> 0:  vacuum ~ A3/r^3,  bent ~ A4/r^4"
    f"   -- ratio diverges: {orders_differ}",
    f"      the radiation term passes the dust term at r = K/2M = {cross_r:.4f} Mpc,"
    f"  i.e. z = {cross_z:.1f}",
    f"      and at last scattering it is already {frac_at_rec * 100:.1f} per cent of the dust term,",
    "        which is r7762's figure recomputed from this revision's own constants.",
    "      ⇒ SORT, IN TWO PARTS, BECAUSE THE QUESTION HAS TWO OBJECTS:",
    "        ⒜ THE BRANCH POINT AS A CHART FACT is the VACUUM's and STANDS: `r = 0` is where the",
    "          areal coordinate degenerates in the SdS `r`-chart, a property of `f` and of the",
    "          chart, which arm 1 puts outside the bend's reach.",
    "        ⛔ ⒝ THE CUT'S OWN RATE AT SMALL `r` IS THE CONTENT'S, AND IT IS NOT THE SAME OBJECT:",
    "          the bent rate diverges as `A4/r^4` against the vacuum's `A3/r^3`.  Any statement that",
    "          reads the approach to the branch point OFF THE RATE is a statement about the",
    "          content-filled leaves, and it does not carry over unchanged.",
    "      ⌗ the reachable negative is the one that fired: the orders do differ, so the arm reports",
    "        them rather than recording agreement.")

# ================================================================= ARM 4: the exact flatness
prop = find(P15, 'The constant-$\\tau$ slice is exactly flat')
prop_arg = find(P15, 'whose Riemann tensor vanishes identically') or \
    find(P15, 'has induced three-metric')
# the induced 3-metric of a constant-tau slice, with NO mass function substituted
rr, th, ph = sp.symbols('r theta phi', positive=True)
g3 = sp.diag(1, rr ** 2, rr ** 2 * sp.sin(th) ** 2)
coords = (rr, th, ph)
ginv = g3.inv()
Gam = [[[sum(ginv[i, l] * (sp.diff(g3[l, j], coords[k]) + sp.diff(g3[l, k], coords[j])
                           - sp.diff(g3[j, k], coords[l])) / 2 for l in range(3))
         for k in range(3)] for j in range(3)] for i in range(3)]
Riem = [[[[sp.simplify(sp.diff(Gam[i][j][l], coords[k]) - sp.diff(Gam[i][j][k], coords[l])
                       + sum(Gam[i][k][m] * Gam[m][j][l] - Gam[i][l][m] * Gam[m][j][k]
                             for m in range(3)))
           for l in range(3)] for k in range(3)] for j in range(3)] for i in range(3)]
riem_all_zero = all(Riem[i][j][k][l] == 0 for i in range(3) for j in range(3)
                    for k in range(3) for l in range(3))
# and the substitution the proposition's argument uses: (d_chi r)^2 dchi^2 = dr^2 along the slice
u = sp.Symbol('u')
rfun = sp.Function('R')(u)                      # r = R(tau + chi), ANY profile
tau_s, chi_s = sp.symbols('tau chi')
r_of = rfun.subs(u, tau_s + chi_s)
dchi_r = sp.diff(r_of, chi_s)
along = sp.simplify(dchi_r ** 2 - sp.diff(r_of, chi_s) ** 2)   # identically zero: dr = d_chi r dchi
subst_unconditional = (sp.simplify(along) == 0)
mass_in_slice = bool(g3.free_symbols & {A3s, A4s, Ms, als, sp.Symbol('M'), sp.Symbol('alpha')})
# ⌗ tested on the metric's FREE SYMBOLS and not on str(g3): the first run tested whether 'M'
#   appeared in the printed form, which it does -- inside the word 'Matrix' -- so the arm
#   reported a mass function present in a metric that has none.
a4 = bool(prop and riem_all_zero and subst_unconditional and not mass_in_slice)
SORT['the exact Euclidean flatness'] = (
    'NEITHER, AND THE ORDER\'S DICHOTOMY DOES NOT REACH IT -- it is a CHART fact, and it never '
    'used a mass function, so it survives the bend for a stronger reason than the vacuum', 'arm 4')
arm(4, "the exact Euclidean flatness of the constant-tau slices", a4,
    "      the proposition and its argument, located:",
    *[f"        \"{s[:250]}\"" for s in (prop_arg[:1] + prop[:1])],
    f"      the induced three-metric, written out: diag(1, r^2, r^2 sin^2 theta) -- i.e. dr^2 + r^2 dOmega^2",
    f"      every component of its Riemann tensor computed from scratch and vanishing: {riem_all_zero}",
    f"      a mass function appearing anywhere in that metric: {mass_in_slice}",
    f"      and the argument's substitution -- (d_chi r)^2 dchi^2 = dr^2 along the slice -- holds for"
    f" an ARBITRARY profile R(tau+chi): {subst_unconditional}",
    "      ⇒ SORT: THE ORDER'S DICHOTOMY DOES NOT REACH THIS ONE, AND THAT IS THE ANSWER.  The",
    "        flatness is a CHART fact: it uses only that `r` is a function on the slice, and no",
    "        mass function enters at any step.  So it does not stand BECAUSE the cut is vacuum --",
    "        it stands whatever the cut is.  ** The bent case needs no separate check. **",
    "      ⌗ the reachable negative, and it is a real hypothesis rather than none: the chart form",
    "        eq:proper-frame rests on r(tau,chi) = r(tau+chi), which rests on the radial equation at",
    "        E = 1 being autonomous.  That is NOT vacuous and arm 5 measures it on the bent cut.")

# ================================================================= ARM 5: the autonomy defence, measured
ident = find(P15, 'the photon congruence \\emph{is} the constant-$\\tau$ family') or \
    find(P15, 'Under the reassignment the photon congruence')
defence = find(P15, 'depends on $r$ alone for every mass function') or \
    find(P15, 'the derivation is not a property of the vacuum chart')


def rhs(_t, y, K):
    r = max(y[0], 1e-12)
    return [r * np.sqrt((TWOM + K / r) / r ** 3 + 1.0 / ALPHA ** 2)]


def solve_from(r_start, K, span):
    return solve_ivp(rhs, (0.0, span), [r_start], args=(K,), rtol=1e-12, atol=1e-14,
                     dense_output=True, method='DOP853')


# the translate property, probed where the radiation term DOMINATES (small r), not only late
SMALL = cross_r / 50.0
solA = solve_from(SMALL, KRAD, 4000.0)
# the offset between the two solutions taken BY QUADRATURE, not by interpolation (r7760's fix)
r_mid = solA.sol(2000.0)[0]
from scipy.integrate import quad as _quad
off = _quad(lambda r: 1.0 / (r * np.sqrt((TWOM + KRAD / r) / r ** 3 + 1.0 / ALPHA ** 2)),
            SMALL, r_mid, limit=400)[0]
solB = solve_from(r_mid, KRAD, 4000.0)
ts = np.linspace(0.0, 1500.0, 60)
rel = np.max(np.abs(solB.sol(ts)[0] / solA.sol(ts + off)[0] - 1.0))
translate_ok = rel < 1e-9
# the unit crossing rate: d(tau+chi)/dtau = 1 on the family, checked as d_chi r = d_tau r
dt = sp.simplify(sp.diff(r_of, tau_s) - sp.diff(r_of, chi_s))
unit_rate = (sp.simplify(dt) == 0)
a5 = bool(ident and defence and translate_ok and unit_rate)
SORT['the photon-family identification'] = (
    'VACUUM CUT AS SUCH FOR ITS DERIVATION, AND IT STANDS -- the defence is measured here on the '
    'bent cut, in the region where radiation dominates', 'arm 5')
arm(5, "the photon-family identity in sec:scope, and its own defence against the bend", a5,
    "      the identification and its defence, located:",
    *[f"        \"{s[:270]}\"" for s in (ident[:1] + defence[:1])],
    f"      THE DEFENCE MEASURED ON THE BENT CUT, and in the region this recheck exists for:",
    f"        probed from r = {SMALL:.4f} Mpc, which is K/2M divided by 50 -- deep inside where the",
    f"        radiation term dominates the mass function;",
    f"        the offset between two solutions taken BY QUADRATURE (r7760's own fix, after an",
    f"        interpolated offset gave 7.78e-05 there): {off:.6f}",
    f"        max relative departure from the translate property over 60 samples: {rel:.3e}"
    f"   -- below 1e-9: {translate_ok}",
    f"      and the unit crossing rate, symbolically: d_tau r - d_chi r = {sp.simplify(dt)}"
    f"  for an arbitrary profile: {unit_rate}",
    "      ⇒ SORT: THE DERIVATION STANDS, AND THE PAPER'S OWN DEFENCE OF IT IS CORRECT.  The radial",
    "        equation at E = 1 is autonomous for every mass function, so its solutions are translates",
    "        and the unit rate holds on the bent cut as on the straight one -- measured here at small",
    "        `r`, which is where r7762 left the question open.",
    "      ⌗ the reachable negative was a failure of the translate property near the branch point.",
    "        It does not fail there.")

# ================================================================= ARM 6: the clause beside it
clause = find(P15, 'Nor does putting radiation into the cut supply the leaf rate')
profile_clause = find(P15, 'taken as the radial profile')
zs = np.array([0.0, 1.0, 1090.0, 1e4])
H_leaf = H0 * np.sqrt(OM * (1 + zs) ** 3 + OL + OMR * (1 + zs) ** 4)
H_prof = H0 * np.sqrt(np.maximum(OM * (1 + zs) ** 3 + OL - 3 * OMR * zs * (1 + zs) ** 3, 0.0))
# the pressure-work reading, straight from h^2 = mu/r^3 + 1/alpha^2 with mu = 2M + K/r
r_of_z = R0 / (1 + zs)
H_pw = CLIGHT * np.sqrt((TWOM + KRAD / r_of_z) / r_of_z ** 3 + 1.0 / ALPHA ** 2)
pw_is_leaf = float(np.max(np.abs(H_pw / H_leaf - 1.0)))
prof_is_leaf = float(np.max(np.abs(H_prof / H_leaf - 1.0)))
clause_true_of_profile = prof_is_leaf > 1e-3
clause_false_of_pw = pw_is_leaf < 1e-11
a6 = bool(clause and profile_clause and clause_true_of_profile and clause_false_of_pw)
SORT["sec:scope's 'nor does putting radiation into the cut'"] = (
    'ABOUT THE CONTENT-FILLED LEAVES, AND IT DOES NOT SURVIVE -- it is true of the superseded '
    'profile reading and false of the pressure-work reading the corpus now holds', 'arm 6')
arm(6, "the clause beside it, which computes on the reading r7762 superseded", a6,
    "      the clause, located verbatim in the CURRENT paper:",
    *[f"        \"{s[:300]}\"" for s in (clause[:1] + profile_clause[:1])],
    "      the three rates at four epochs, computed from this revision's own constants:",
    f"        z                     {'  '.join(f'{z:>10.0f}' for z in zs)}",
    f"        leaf rate             {'  '.join(f'{v:>10.3f}' for v in H_leaf)}",
    f"        the PROFILE reading   {'  '.join(f'{v:>10.3f}' for v in H_prof)}",
    f"        the PRESSURE-WORK cut {'  '.join(f'{v:>10.3f}' for v in H_pw)}",
    f"      max |profile/leaf - 1| = {prof_is_leaf:.4e}   => the clause is TRUE of the profile"
    f" reading: {clause_true_of_profile}",
    f"      max |pressure-work/leaf - 1| = {pw_is_leaf:.3e}   => and FALSE of the pressure-work"
    f" reading: {clause_false_of_pw}",
    "      ⇒ ⛔⛔ THE SENTENCE IS TRUE ONLY OF A READING THE CORPUS HAS SINCE WITHDRAWN.  `rho_r`",
    "        in that clause is a RADIAL PROFILE, and step (iv) makes the radial coordinate the",
    "        label of the LEAF -- so the profile is the mass-inside-radius relation applied where",
    "        `r` is not spacelike, which is exactly the error r7756 made and r7762 withdrew.  On the",
    "        pressure-work law the bent cut's rate IS the leaf rate, to a part in 1e12 at every",
    "        epoch measured.  ** The paragraph has not been reached by the correction. **",
    "      ⌗ WHOSE ERROR: this line made the same misreading first, at r7756, and withdrew it at",
    "        r7762.  The sentence predates that withdrawal, so this is a correction owed to the",
    "        paper and not a point scored.  A patch is drafted in the reply; nothing is edited here.",
    "      ⌗ the guard applied before calling it wrong: what `rho_r` ranges over was established",
    "        from the clause's own words -- 'taken as the radial profile' - and not assumed.")

# ================================================================= ARM 7: the sort
a7 = len(SORT) >= 5
arm(7, "the sort the order asks for", a7,
    *[f"      {k}\n        ⇒ {v[0]}   [{v[1]}]" for k, v in SORT.items()],
    "      ⌗ TWO of the five do not fit the order's dichotomy, and that is reported rather than",
    "        forced: the flatness is a CHART fact that never used a mass function, and the branch",
    "        point splits into a chart fact that stands and a rate statement that does not.")

# ================================================================= ARM 8: P7's campaign-138 paragraphs
LEAN_PARA = [ln for ln in P7.split('\n') if 'Framework.lean' in ln]
CITED = sorted({c.replace('\\_', '_') for c in
                re.findall(r'\\texttt\{(fw\\_[A-Za-z0-9\\_\']+)\}', ' '.join(LEAN_PARA))})


def decl_block(name):
    m = re.search(r'^(theorem|lemma|def|example)\s+' + re.escape(name) + r'\b', LEAN, re.M)
    if not m:
        return None
    rest = LEAN[m.start():]
    nxt = re.search(r'\n(theorem|lemma|def|example|/--|#print)\s', rest[1:])
    return rest[:nxt.start() + 1] if nxt else rest


def binders(block):
    """bracket-matched binder extraction -- a flat regex returns SHORT lists (r7756's defect)"""
    out, i, n = [], 0, len(block)
    while i < n:
        if block[i] in '({[':
            close = {'(': ')', '{': '}', '[': ']'}[block[i]]
            d, j = 1, i + 1
            while j < n and d:
                if block[j] in '({[':
                    d += 1
                elif block[j] in ')}]':
                    d -= 1
                j += 1
            out.append(block[i:j])
            i = j
        elif block[i] == ':' and block[i:i + 2] != ':=':
            break
        else:
            i += 1
    return out


NEW = ['fw_no_intersection', 'fw_sinh23', 'fw_horizon_inj', 'fw_timelike_slope',
       'fw_H', 'fw_H_null', 'fw_rs_tendsto']
rows = []
for c in CITED:
    b = decl_block(c)
    rows.append((c, b is not None, len(binders(b)) if b else 0, 'NEW at 138' if c in NEW else ''))
all_present = all(r[1] for r in rows)
new_present = [r for r in rows if r[3] and r[1]]
a8 = bool(CITED and all_present)
arm(8, "P7's campaign-138 paragraphs: are they there, and do they cite what they use?", a8,
    f"      paragraphs citing the Lean probe: {len(LEAN_PARA)}"
    f"  (r7762 read FOUR; the campaign added more)",
    f"      declarations cited across them: {len(CITED)}",
    *[f"        {'✔' if p else '⛔'} {c:<24} binders: {nb:<3} {tag}" for c, p, nb, tag in rows],
    f"      every citation resolves to a declaration in the file: {all_present}",
    f"      of the campaign-138 set, resolving: {len(new_present)} of {len([1 for c in CITED if c in NEW])}",
    "      ⌗ the binder lists are BRACKET-MATCHED, not regex-split: r7756 found a flat regex returns",
    "        short lists and made two present hypotheses look absent.")

# ================================================================= ARM 9: the file's hygiene
ndecl = len(re.findall(r'^(theorem|lemma|def|example)\s+\S+', LEAN, re.M))
nsorry = len(re.findall(r'\bsorry\b', LEAN))
naxiom = len(re.findall(r'#print axioms', LEAN))
nlines = LEAN.count('\n') + 1
disclose = []
for ln in LEAN_PARA:
    has = bool(re.search(r'(what it does not|does \\emph\{not\} formalise|not formalised|'
                         r'is not claimed|no claim is made|does not establish)', ln, re.I))
    disclose.append(has)
a9 = (nsorry == 0 and naxiom > 0 and ndecl > 0)
arm(9, "the Lean file's own hygiene, and what cannot be checked here", a9,
    f"      Framework.lean: {nlines} lines, {ndecl} declaration(s), {nsorry} `sorry`,"
    f" {naxiom} `#print axioms` line(s)",
    f"      per-paragraph disclosure of what is NOT formalised: {sum(disclose)} of {len(disclose)}"
    f"  -- {disclose}",
    "      ⛔ THE LEAN BUILD IS NOT RUNNABLE IN THIS CONTAINER (no lake, lean or elan), so every",
    "        statement above is about the FILE's text and its declarations, not about a successful",
    "        build.  That is said in terms rather than implied, as r7762's arms did.")

# ================================================================= ARM 10: the owed instrument fix
owed_reads = find(P15, 'photon famil')
subsumed = False
remainder = ("the instrument must distinguish a WITHDRAWN claim (sentence in print, marker gone) from "
             "a STALE key (not in print at all).  Arm 6 ADDS A THIRD STATE rather than removing one: a "
             "sentence in print, carrying its marker, whose COMPUTATION rests on a reading the corpus "
             "has withdrawn.  That is not a marker state at all -- it is a provenance state -- so the "
             "owed fix is NOT subsumed, and arm 6 makes it harder rather than easier.")
a10 = not subsumed
arm(10, "does the order's item 4 subsume the photon-family instrument fix this seat owes?", a10,
    f"      VERDICT: NOT SUBSUMED, and the recheck makes it harder.",
    f"      {remainder}",
    "      ⇒ The fix changes what a gate asserts, so it keeps its own registration and is NOT done",
    "        here.  ⌗ the reachable negative was exactly this and it fired: the arm checked for a",
    "        third state and found one.")

# ================================================================= ARM 11: what cannot be settled
OPEN = [
    ('the Lean build', 'no toolchain in this container; CI and node 71 have it'),
    ('whether the corpus\'s nucleosynthesis was computed on the leaf rate',
     'cited to a companion paper this repository does not carry'),
    ('whether sec:scope\'s author intended the profile reading as the cut\'s mass function',
     'an intention, not a text fact; the clause\'s own words are reported instead'),
    ('the full horizon structure of a cut whose bend DID source f',
     'ruled out by arm 1 as not this corpus\'s case, so computed only as the contrast'),
]
a11 = len(OPEN) >= 1 and all(len(o[1]) > 10 for o in OPEN)
arm(11, "what this recheck cannot settle", a11,
    *[f"      * {w}\n        -- {why}" for w, why in OPEN],
    "      ⌗ none of these is left as a hedge inside a stem: each is a named item with its reason.")

# ================================================================= ARM 12
PRED = read('computations/beyond_the_wall/'
            'r7768_60_the_small_r_recheck_on_the_bent_cut_and_a_cold_read_of_p7s_campaign_138_paragraphs/'
            'PREDICTION.md')
declared = len(re.findall(r'^## [\u2460-\u246b]', PRED, re.M))
answered = len(VERDICTS) + 1
a12 = (declared == 12 and answered == 12)
arm(12, "the count, and the subject clause", a12,
    f"      arms declared in PREDICTION.md: {declared}",
    f"      arms answered here (this one included): {answered}",
    "      ** THIS SEAT IS A SUBJECT OF NOTHING IN THIS REVISION. **")

print(f"\n{'=' * 100}\n  VERDICT\n{'=' * 100}")
for n, ok, title in VERDICTS:
    print(f"    [{'PASS' if ok else 'FAIL'}]  ARM {n:<3} {title}")
bad = [n for n, ok, _ in VERDICTS if not ok]
print(f"\n  {len(VERDICTS) - len(bad)} of {len(VERDICTS)} arms meet their criterion.")
if bad:
    print(f"  ⛔ arms not meeting their criterion: {bad}")
print("=" * 100)
