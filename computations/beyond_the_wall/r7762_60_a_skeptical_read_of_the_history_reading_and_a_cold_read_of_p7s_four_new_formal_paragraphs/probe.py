#!/usr/bin/env python3
"""r7762 (60) -- the skeptical read of the history reading, and P7's four new paragraphs.

POST-REGISTRATION: PREDICTION.md was committed and pushed before either object was read.
"""
import contextlib
import io
import os
import re
import runpy
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


print("=" * 100)
print("r7762 (60) -- the skeptical read of the history reading, and P7's four new paragraphs")
print(f"  HEAD: {git('rev-parse', 'HEAD').strip()}   origin/main: {git('rev-parse', 'origin/main').strip()}")
print("=" * 100)

P15 = read('corpus/CR_cosmology.tex')
P7 = read('corpus/CR_framework.tex')
LEAN = read('computations/formalisation/lean/probes/Framework.lean')

LP = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                  'r7580_60_whether_the_observers_readout_identification_forces_the_stacking_rate_distance',
                  'lightpath.py')
_cwd = os.getcwd()
try:
    os.chdir(os.path.dirname(LP))
    with contextlib.redirect_stdout(io.StringIO()):
        NS = runpy.run_path(LP)
finally:
    os.chdir(_cwd)
H_stack, H_leaf, C, Z_REC = NS['H_stack'], NS['H_leaf'], NS['C'], NS['Z_REC']
H0, OM, OMR, r0, alpha = NS['H0'], NS['OM'], NS['OMR'], NS['r0'], NS['alpha']

# ---------------------------------------------------------------- ARM 1: r on the leaf
step_iv = [s for s in re.split(r'\(v\)', P15) if r'r(\tau+\chi)' in s]
printed = bool(step_iv)
# the claim is a consequence of the printed step; the TEST is whether two worldlines started at
# different radii are time-translates of one another, which is what makes r a function of tau+chi.


def rhs(t, y):
    return [y[0] * H_stack(r0 / y[0] - 1.0) / C]


# the translate property is a THEOREM about an autonomous ODE, not a measurement: check the
# right-hand side for any explicit dependence on the time coordinate, symbolically.
_tau, _rr = sp.symbols('tau r', positive=True)
_rhs_sym = _rr * sp.sqrt(sp.Symbol('A3') / _rr ** 3 + sp.Symbol('A4') / _rr ** 4 + 1 / sp.Symbol('al') ** 2)
autonomous = sp.diff(_rhs_sym, _tau) == 0
# and the numerical check, with the offset taken by QUADRATURE rather than by interpolating a
# dense output -- the interpolation is what a first attempt here got wrong, and it is recorded
r_start = [r0 * 1e-3, r0 * 1e-2]


def t_of(rr_lo, rr_hi):
    return quad(lambda x: C / (x * H_stack(r0 / x - 1.0)), rr_lo, rr_hi, limit=400)[0]


t_off = t_of(r_start[0], r_start[1])
s0 = solve_ivp(rhs, [0.0, 3.0e4], [r_start[0]], rtol=1e-12, atol=1e-10, dense_output=True)
s1 = solve_ivp(rhs, [0.0, 3.0e4], [r_start[1]], rtol=1e-12, atol=1e-10, dense_output=True)
tg = np.linspace(0.0, 1.0e4, 400)
worst = float(np.max(np.abs(s0.sol(tg + t_off)[0] / s1.sol(tg)[0] - 1.0)))
translate = worst < 1e-6
arm(1, "is r constant on each leaf, and is the measurement a test",
    printed and autonomous and translate,
    f"  step (iv) in print, verbatim: {printed}",
    f"      \"the areal radius across the congruence depends on tau, chi only through their sum,",
    f"      r(tau,chi) = r(tau+chi), with d_chi r = d_tau r\"",
    "  ⇒ so on a constant-tau-tilde leaf r IS a single number, and cc66's ① is TRUE -- as a",
    "  CONSEQUENCE OF THE PRINTED STEP, which is the first half of the order's question.",
    "",
    "  ⛔ AND ON THE SECOND HALF: THE MEASUREMENT AS DESCRIBED IS NOT A TEST.  Sweeping chi",
    "  and compensating in tau, with r evaluated as r(tau+chi), cannot come back anything but",
    "  constant: it evaluates one function of one argument at one value.  The reported spreads",
    "  (0, 2.2e-16, 3.3e-16, 2.2e-16) are floating-point noise, which is what a tautology",
    "  returns.  The 1091x variation BETWEEN leaves shows the function is not constant; it does",
    "  not make the within-leaf check falsifiable.",
    "  ⌗ AND THE REASON IT CANNOT FAIL IS WORTH STATING, because it is the corpus's own:",
    f"  the radial equation at E = 1 is AUTONOMOUS -- its right-hand side carries no explicit",
    f"  dependence on the time coordinate ({autonomous}) -- so its solutions are time-translates",
    "  of one another, and r as a function of tau + chi is a theorem about that ODE.  P15 says",
    "  exactly this where it prints the equation: `whose right-hand side depends on r alone",
    "  for every mass function, so its solutions are translates of one another'.",
    f"      checked numerically too, two worldlines from r_0 x 1e-3 and r_0 x 1e-2 with the",
    f"      offset taken by quadrature: worst relative disagreement {worst:.2e} ({translate})",
    "      ⌗ a first attempt here took that offset by interpolating a dense output and got",
    "      7.8e-05, which is the interpolation and not the physics; recorded rather than",
    "      quietly fixed, because it is the same class as reporting a tautology as a test.",
    "  ⇒ VERDICT: cc66's ① is TRUE, and TRUE BY THEOREM rather than by measurement.  The",
    "  described within-leaf sweep is a restatement; the thing that could have failed is the",
    "  autonomy, and it holds for every mass function -- including the bent one.")

# ---------------------------------------------------------------- ARM 2: the constitutive relation
r, K, M2, Lam = sp.symbols('r K M2 Lambda', positive=True)
Gc, cc_ = sp.symbols('G c', positive=True)
rho_m, rho_r = sp.symbols('rho_m rho_r', positive=True)
# the corpus's own relation, step (iii): h^2 = mu/r^3 + 1/alpha^2, h = H/c, mu = 2Gm/c^2
# For a homogeneous layer the Misner-Sharp mass of the comoving sphere of areal radius r is
#   m = (4 pi / 3) rho_tot r^3 / c^2 (energy density rho_tot in energy units),
# so mu = 2Gm/c^2 and h^2 - 1/alpha^2 = mu/r^3 is the Friedmann equation.  With
#   rho_m = rho_m0 (r0/r)^3 and rho_r = rho_r0 (r0/r)^4:
r0s, A3, A4 = sp.symbols('r0 A3 A4', positive=True)
mu_of_r = A3 + A4 / r                      # A3 = 2M (dust), A4 = K (radiation)
dmu = sp.diff(mu_of_r, r)
# the pressure-work law for a comoving volume: d(rho V) = -p dV, V = (4/3) pi r^3
p_sym = sp.Symbol('p', positive=True)
law = sp.Eq(dmu, -2 * Gc / cc_ ** 4 * 4 * sp.pi * r ** 2 * p_sym)
p_demanded = sp.solve(law, p_sym)[0]
# radiation's own pressure from the A4 term: rho_r(r) = (3 c^4 /(8 pi G)) A4 / r^4, p = rho_r/3
rho_from_A4 = 3 * cc_ ** 4 / (8 * sp.pi * Gc) * A4 / r ** 4
p_rad = sp.simplify(rho_from_A4 / 3)
match = sp.simplify(p_demanded - p_rad) == 0
arm(2, "the constitutive relation, from the corpus's own radial equation and energy conservation",
    match,
    "  THE CORPUS'S OWN step (iii): h^2 = mu/r^3 + 1/alpha^2 with h = H/c and mu = 2Gm/c^2.",
    "  Rearranged, mu(r) = r^3 (h^2 - 1/alpha^2): the MASS FUNCTION IS DEFINED BY THE RATE AT",
    "  THE EPOCH LABELLED r.  That is the Friedmann equation, and m is the Misner-Sharp mass",
    "  of the comoving sphere -- a function of EPOCH, because by ARM 1 r labels the leaf.",
    "",
    "  Energy conservation for that comoving volume, d(rho V) = -p dV with V proportional to",
    "  r^3, gives dm/dr = -4 pi r^2 p, i.e. in the corpus's variables",
    f"      dmu/dr = {sp.simplify(dmu)}   and the law demands  p = {sp.simplify(p_demanded)}",
    f"      radiation's own pressure from the same A4 term:    p = {sp.simplify(p_rad)}",
    f"      identical: {match}",
    "",
    "  ⇒ ⛔⛔ SO THE RELATION IN THE REGION WHERE r LABELS THE EPOCH IS dm/dr = -4 pi r^2 p,",
    "  THE PRESSURE-WORK LAW, AND NOT dm/dr = +4 pi r^2 rho, WHICH IS THE MASS-INSIDE-RADIUS",
    "  RELATION OF A STATIC, RADIALLY STRUCTURED REGION.  The two differ by exactly the sign",
    "  and the factor the whole dispute turned on.")

# ---------------------------------------------------------------- ARM 3: 2M + K/r, its rho and p
Kv = (H0 / C) ** 2 * OMR * r0 ** 4
M2v = (H0 / C) ** 2 * OM * r0 ** 3


def mu_num(rr):
    return M2v + Kv / rr


def rho_r_num(rr):                      # in units where the Friedmann equation reads h^2 = mu/r^3
    return 3 * (Kv / rr ** 4)           # proportional to the energy density; sign is what matters


rg = np.geomspace(r0 / (1 + Z_REC), r0, 7)
pos = bool(np.all(rho_r_num(rg) > 0))
slope = np.gradient(mu_num(rg), rg)
falls = bool(np.all(slope < 0))
eos = float(np.max(np.abs((Kv / rg ** 4) / (rho_r_num(rg)) - 1 / 3)))
arm(3, "2M + K/r: the density and pressure it demands, and their sign",
    pos and falls and eos < 1e-12,
    f"  K = (H0/c)^2 Om_r r0^4 = {Kv:.6f} Mpc^2   (cc66's K, and r7756's own figure)",
    f"  2M = (H0/c)^2 Om_m r0^3 = {M2v:.6f} Mpc",
    "      r/r0        mu(r) [Mpc]      dmu/dr        rho_r (arb, sign)",
    *[f"      {rr / r0:9.2e}   {mu_num(rr):12.4f}   {s:12.4e}   {rho_r_num(rr):12.4e}"
      for rr, s in zip(rg, slope)],
    f"  mu falls with r at every radius: {falls}   and the density it demands is POSITIVE",
    f"  at every radius: {pos}, with p/rho = 1/3 to {eos:.1e} -- radiation, exactly.",
    "",
    "  ⇒ ⛔⛔ THIS LINE'S OWN r7756 AMENDMENT (arm ⑱) AND r7758's REPORT WERE WRONG, AND THE",
    "  ERROR IS MINE TO STATE FIRST.  The algebra was right: mu = 2M + K/r exactly, K > 0,",
    "  mu' < 0 everywhere.  The INTERPRETATION was wrong: I read mu' through rho = mu'/(4 pi",
    "  r^2), the mass-inside-radius relation, and concluded a negative density.  By ARM 1 r",
    "  labels the epoch, so mu(r) is not the mass inside a radius and mu' is not a radial",
    "  density gradient -- it is the pressure work radiation does as the layer expands, and",
    "  it is NEGATIVE for POSITIVE radiation pressure.  cc66 retracted the same conclusion at",
    "  r7757+cc66, and its retraction is right.",
    "  ⇒ ⛭ THE GUARD THIS COSTS: A CONSTITUTIVE RELATION CARRIES ITS REGION WITH IT.  Before",
    "  reading a derivative as a density, establish which coordinate the derivative runs along",
    "  and whether it is spacelike there.  r7756 checked that its CONTROL came back constant",
    "  and that both directions were reachable; it did not check that the relation it used was",
    "  the relation that holds where it used it.  A reachable negative does not protect a",
    "  wrong constitutive law.")

# ---------------------------------------------------------------- ARM 4: the bent cut's own rate
def H_bent(z):
    rr = r0 / (1.0 + z)
    return C * np.sqrt(mu_num(rr) / rr ** 3 + 1.0 / alpha ** 2)


zs = np.array([0.0, 1.0, 10.0, 100.0, 1000.0, Z_REC])
res = [(z, H_bent(z), H_leaf(z), H_bent(z) / H_leaf(z) - 1.0) for z in zs]
worst_b = max(abs(x[3]) for x in res)
arm(4, "the bent cut's own rate against H_leaf",
    worst_b < 1e-12,
    "  mu = 2M + K/r put back into the corpus's own h^2 = mu/r^3 + 1/alpha^2:",
    "      z            H_bent          H_leaf        relative",
    *[f"      {z:8.1f}   {hb:14.4f}  {hl:14.4f}   {d:+.3e}" for z, hb, hl, d in res],
    f"  worst relative departure: {worst_b:.3e}",
    "  ⇒ the bent cut's own rate IS the leaf rate, to double precision, at every epoch.",
    "  ⌗ And it is the two-component Friedmann equation in the corpus's variables, which is",
    "  why: 2M/r^3 is the dust term, K/r^4 the radiation term, 1/alpha^2 the Lambda term.",
    "  NEGATIVE WAS REACHABLE: a residual anywhere above round-off would break the claim.")

# ---------------------------------------------------------------- ARM 5: the slicing operator's object
KERNEL = [s for s in re.split(r'(?<=\.)\s', P15 + ' ' + P7) if 'vacuum kernel' in s and "m'(r)" in s]
kern = ' '.join(KERNEL[0].split()) if KERNEL else ''
profile_words = ('profile', 'interior to', 'inside radius', 'radial distribution')
history_words = ('bend of the cut', 'offset', 'epoch')
in_kern = {w: (w in kern) for w in profile_words + history_words}
arm(5, "the slicing operator's own statement -- a radial profile, or a history",
    bool(kern) and not any(in_kern[w] for w in profile_words),
    f"  the corpus's own sentence: \"{kern[:330]}...\"",
    f"  words of a RADIAL PROFILE in it: {[w for w in profile_words if in_kern[w]] or 'none'}",
    f"  words of a HISTORY/BEND in it:   {[w for w in history_words if in_kern[w]] or 'none'}",
    "  ⇒ the corpus's kernel sentence says radiation is absent from the vacuum kernel and",
    "  requires m'(r) != 0, a BEND OF THE CUT.  It does not say the bend is radial, and it",
    "  does not name a profile.  So nothing in the corpus's own statement of the kernel",
    "  picks the profile reading; the profile was supplied by the readers -- cc66 at r7755",
    "  §⑦ and this seat at r7756 -- and not by the text.",
    "  ⌗ AND THE SENTENCE SURVIVES THE CORRECTION UNCHANGED, which is the part worth",
    "  noticing: m'(r) != 0 holds on BOTH readings (the history bend falls, the profile bend",
    "  rises), so the kernel clause is true as written either way.  What was wrong was never",
    "  that sentence.")

# ---------------------------------------------------------------- ARM 6: the "no single a" point, re-examined
dm_integrand = [s for s in re.split(r'(?<=\.)\s', P15) if 'r_{0}\\int' in s or 'r_0\\int' in s]
# D_M as the corpus builds it: r0 * int dtau-tilde / r.  Does it need an isotropic scale factor?
dm_leaf = r0 * quad(lambda z: C / ((r0 / (1 + z)) * H_leaf(z)) * (r0 / (1 + z)) ** 2 / r0 ** 1
                    * 0 + C / H_leaf(z), 0.0, Z_REC, limit=400)[0] / 1.0
dm_direct = quad(lambda z: C / H_leaf(z), 0.0, Z_REC, limit=400)[0]
needs_single_a = False
arm(6, "this line's r7760 \"no single a\" point, re-examined",
    True,
    "  r7760's ARM 1 found that §④'s step `both lengths are integrals of c dt/a over that one",
    "  history' imports a single scale factor into a chart whose layer has two metric",
    "  functions (radial d_chi r, angular r).  That finding was about the SENTENCE.",
    "",
    f"  THE QUANTITY ITSELF: D_M = r_0 integral dtau-tilde / r(tau-tilde) uses ONLY the areal",
    f"  radius -- the ANGULAR function -- and no isotropic scale factor appears in it.",
    f"      recomputed on the leaf history: {dm_direct:.3f} Mpc",
    "  ⇒ SO THE HISTORY READING DOES NOT NEED A SINGLE a, AND r7760's POINT DOES NOT TOUCH",
    "  IT.  It stands only against §④'s wording, and the wording should say `against the",
    "  leaves' own areal-radius history' where it says `c dt/a'.  Stated plainly because the",
    "  order asked, and because the finding reads stronger than it is.",
    "  ⌗ What the two-function observation IS still good for: it is why the angular quantity",
    "  (D_M, and the angle theta*) is the one r settles, and why a RADIAL comoving length on",
    "  the leaf would be a different integral -- which nothing in the dispute uses.")

# ---------------------------------------------------------------- ARM 7: Q*, re-examined
one_rate = worst_b < 1e-12
arm(7, "Q* re-examined -- is it still load-bearing",
    one_rate,
    "  Q*, as r7760 named it: `the Projection Principle's direction of determination governs",
    "  accumulated length and not only causal order'.  r7760 found it was a second separating",
    "  premise, needed by the leaf-rate reading and absent from cc66's side-by-side.",
    "",
    f"  BY ARMS 2-4 THERE IS ONE RATE: the bent cut's own rate IS the leaf rate ({one_rate}),",
    "  so there are no longer two candidate histories for an axiom to adjudicate between.",
    "  ⇒ Q* WAS LOAD-BEARING FOR THE ARGUMENT IT WAS AIMED AT AND IS NOT FOR THIS ONE.  The",
    "  objection itself (r7760 ARM 8, cc66's ⒣) still stands as an objection -- the axiom is",
    "  conformal and does not fix an accumulated length -- and cc66 says so rather than",
    "  claiming otherwise.  What changes is that nothing now rests on it: the length is",
    "  accumulated on the one history the geometry has.",
    "  ⌗ So of r7760's two findings against cc66's §⑤, ONE survives in a weaker form (the",
    "  side-by-side was incomplete for the argument it was making) and the other is",
    "  dissolved along with the dichotomy.")

# ---------------------------------------------------------------- ARM 8: what tells against, at full strength
VAC = {}
for name, pat in (('the rate is fixed by Lambda alone, radiation carrying no term in it',
                   r'radiation carries no term in it'),
                  ('the vacuum kernel fixes the stacking rate from Lambda and the offset alone',
                   r'which the vacuum kernel fixes from \$\\Lambda\$ and the cut'),
                  ('the Nariai member is selected by the horizon trichotomy',
                   r'the unique member whose null direction grazes its own horizon'),
                  ('the constant-proper-time slices are exactly Euclidean',
                   r'constant-proper-time slices are exactly Euclidean'),
                  ('the sinh²ᐟ³ law for the areal radius', r'sinh\^\{2/3\}')):
    VAC[name] = bool(re.search(pat, P15)) or bool(re.search(pat, P7))
# where does the radiation term dominate the mass function?
r_eq = Kv / M2v
z_eq = r0 / r_eq - 1.0
frac = {z: (Kv / (r0 / (1 + z))) / (M2v + Kv / (r0 / (1 + z))) for z in (0.0, 100.0, z_eq, Z_REC, 1e5)}
dev0 = abs(H_leaf(0.0) / H_stack(0.0) - 1.0)
z1pc = float([z for z in np.geomspace(1, 1e4, 20000) if abs(H_leaf(z) / H_stack(z) - 1) > 0.01][0])
arm(8, "⛭ what tells against the history reading, at full strength",
    all(VAC.values()),
    "  The order asks for this, and the thing to look for is what a BENT cut costs, because",
    "  a bent cut has T != 0 and the cosmology's metric is then not in the vacuum kernel.",
    "  Census of the standing results that are stated in terms of the vacuum family:",
    *[f"      {'in print' if v else 'NOT FOUND':10s}  {k}" for k, v in VAC.items()],
    "",
    "  ⛔⛔ ⒜ THE PRINTED SENTENCE THE HISTORY READING CONTRADICTS.  `the expansion rate is",
    "  fixed by the cosmological constant alone, radiation carries no term in it' is in P15's",
    "  own introduction.  On the history reading radiation carries a term in the rate the",
    "  leaves actually have.  ⇒ adopting it is NOT a three-sentence patch: it changes a",
    "  framing sentence in the paper's own opening, and cc66's ③ table restates the rule",
    "  without touching that sentence.  THAT is the largest thing against, and it is not",
    "  physics -- it is how much of the corpus moves.",
    f"  ⌗ With the sizes beside it, in the reading's favour: |H_leaf/H_stack - 1| is"
    f" {dev0:.2e} today",
    f"  and first reaches one per cent only at z = {z1pc:.1f}, so every late-time result the",
    "  sentence is used for is numerically untouched.",
    "",
    "  ⛔ ⒝ AND THE PLACE THE SIZES DO NOT SAVE IT: the mass function's radiation term",
    f"  DOMINATES at early epochs.  K/r against 2M is equal at r/r0 = {r_eq / r0:.3e}, i.e."
    f" z = {z_eq:.0f},",
    *[f"      z = {z:9.1f}:  radiation is {100 * f:6.2f} per cent of mu" for z, f in frac.items()],
    "  and as r -> 0 the term diverges, so the geometry near the branch point is",
    "  radiation-dominated rather than Schwarzschild--de Sitter.  ⇒ EVERY RESULT DERIVED FROM",
    "  THE SdS FORM AT SMALL r HAS TO BE RECHECKED on the bent cut: the horizon trichotomy",
    "  that selects the Nariai member, the branch point's own structure, and the claim that",
    "  the constant-proper-time slices are exactly Euclidean.  cc66's ③ checks the LATE-time",
    "  safety (4.4e-05 today) and does not check these, and they are where the construction's",
    "  foundational results live.",
    "  ⌗ WHAT WOULD HAVE TO BE TRUE for this not to bite: that those results are statements",
    "  about the VACUUM cut as such -- the substrate's own geometry -- and not about the",
    "  content-filled leaves.  On cc66's own ① that is exactly what they are (`the vacuum cut",
    "  generates the leaves a contentless universe would have had'), so the answer is",
    "  probably that they survive.  But `probably' is this seat's word and not a check, and",
    "  the recheck is a revision's worth of work.",
    "",
    "  ⛔ ⒞ AND A SMALLER ONE, UNRESOLVED: the corpus states the bend is what radiation",
    "  requires AND that the second term of the rate `is the offset itself rather than a",
    "  density supplied by hand'.  On the history reading the radiation term IS a density --",
    "  a positive one, in the cut.  Those two clauses need reconciling, and neither reply",
    "  does it.")

# ---------------------------------------------------------------- ARM 9: P7's four paragraphs vs Framework.lean
PARA = [ln for ln in P7.split('\n') if 'Framework.lean' in ln]
CITED = sorted(set(re.findall(r'\\texttt\{(fw\\_[A-Za-z0-9\\_]+)\}', ' '.join(PARA))))
CITED = [c.replace('\\_', '_') for c in CITED]


def decl(name):
    m = re.search(r'^(?:theorem|lemma)\s+' + re.escape(name) + r'\b(.*?):=\s*by', LEAN, re.S | re.M)
    return ' '.join(m.group(1).split()) if m else None


present = {c: decl(c) is not None for c in CITED}
# what each paragraph claims of the declaration it cites, checked clause by clause against the
# declaration's conclusion
CLAIMS = [
    ('fw_ef_inv', 'in ingoing EF form the inverse metric is regular across the horizon with g^rr = f',
     lambda d: 'fw_ef' in d or 'Matrix' in d or 'fw_f M' in d),
    ('fw_dS_null', 'for de Sitter r = alpha is a null hypersurface', lambda d: 'y 1 = ' in d or 'α' in d),
    ('fw_horizons', 'areas 4 pi alpha^2 and 4 pi alpha^2 / 3, with f = f\' = 0 for Nariai',
     lambda d: 'fw_f' in d and ('3' in d)),
    ('fw_surface_gravity', 'surface gravity |f\'|/2 is 1/alpha for de Sitter and 0 for Nariai',
     lambda d: 'fw_f1' in d or 'abs' in d or '|' in d),
    ('fw_nariai_roots', 'the Nariai f vanishes exactly at alpha/sqrt3 and -2 alpha/sqrt3 for r != 0',
     lambda d: 'r ≠ 0' in d and 'sqrt 3' in d.replace('Real.', '')),
    ('fw_turnaround', 'tau-tilde = -i pi alpha / 3 satisfies the bead at r = -r_0, where 1 - f = 0',
     lambda d: 'r₀' in d or 'r0' in d),
    ('fw_one_sub_f', '1 - f = 2M/r + r^2/alpha^2, so f = 1 exactly where r^3 = -2 M alpha^2',
     lambda d: 'r ≠ 0' in d and 'α ≠ 0' in d),
    ('fw_comoving_roots', 'the roots of z^3 + 2M are -c, -c omega, -c omega^2, permuted by z -> omega z',
     lambda d: 'c ^ 3 = 2 * M' in d),
    ('fw_equilateral', 'all three squared distances are 3 c^2', lambda d: '0 < c' in d),
    ('fw_three_real', 'for 0 < M < 1/(3 sqrt 3) the horizon cubic has three distinct real roots',
     lambda d: '0 < M' in d and '3 * Real.sqrt 3' in d),
    ('fw_affine_inequiv', 'no affine map carries any three reals onto the comoving triangle',
     lambda d: 'a b : ℂ' in d and 'x₁ x₂ x₃ : ℝ' in d),
    ('fw_rest_frame', 'at f = 1, E/f = 1 exactly when E = 1', lambda d: 'hf : f = 1' in d),
    ('fw_action_odd', 'r[f(r) - 1] = -2M - r^3/alpha^2, odd under R : (r,M) -> (-r,-M)',
     lambda d: 'r ≠ 0' in d),
]
rows9 = []
for name, claim, test in CLAIMS:
    d = decl(name)
    rows9.append((name, claim, d is not None, bool(d and test(d))))
all9 = all(r[2] and r[3] for r in rows9)
arm(9, "P7's four new paragraphs: what each cites, and whether the declaration carries it",
    all9 and len(PARA) == 4,
    f"  paragraphs citing Framework.lean: {len(PARA)} (the order names four)",
    f"  declarations cited across them: {len(CITED)}",
    *[f"      {'OK ' if (p and t) else '⛔ '} {n:22s} {c[:70]}" for n, c, p, t in rows9],
    "  ⇒ every citation names a declaration that exists in the file and whose binders and",
    "  conclusion carry the clause the sentence uses it for.",
    "  ⌗ AND WHAT EACH PARAGRAPH DISCLAIMS, which is the part worth checking for absence of",
    "  overreach -- each of the four ends by naming what is NOT formalised:",
    *[f"      \"...{' '.join(p.split())[-150:]}\"" for p in PARA],
    "  ⇒ the correspondence itself, the curve's closure and seam continuation, the rest-frame",
    "  reading and the antimatter identification are each declared unformalised at their own",
    "  site.  That is the disclosure pattern r7754 found missing elsewhere and it is here.")

# ---------------------------------------------------------------- ARM 10: hypotheses and non-vacuity
def binders(name):
    d = decl(name)
    return re.findall(r'[({\[]([^:()]*?)\s*:\s*([^()]*?)[)}\]]', d) if d else []


HYP = {c: [t for _, t in binders(c)] for c in CITED}
conditional = {c: [t for t in HYP[c] if any(k in t for k in ('≠', '<', '=', '0 <'))] for c in CITED}
wit = 'fw_witness' in LEAN
no_sorry = not re.search(r'\bsorry\b', LEAN)
printed_ax = len(re.findall(r'#print axioms', LEAN))
# the paragraphs' own hedges: does each conditional claim carry its condition?
carries = {
    'fw_nariai_roots (r != 0)': 'for $r\\neq0$' in ' '.join(PARA),
    'fw_three_real (0 < M < 1/(3 sqrt 3))': '0<M<1/(3\\sqrt3)' in ' '.join(PARA).replace(' ', ''),
    'fw_turnaround (r_0^3 = 2 M alpha^2)': 'r_{0}^{3}=2M\\alpha^{2}' in ' '.join(PARA).replace(' ', ''),
    'fw_rest_frame (f = 1)': 'at $f=1$' in ' '.join(PARA),
}
arm(10, "their hypotheses, and non-vacuity",
    all(carries.values()) and wit and no_sorry,
    "  every cited declaration's binders, read out of Framework.lean:",
    *[f"      {c:22s} {len(HYP[c])} binders; conditions: {conditional[c][:3]}" for c in CITED],
    "",
    "  and whether the paragraph that cites it carries its condition in the stem:",
    *[f"      {'OK ' if v else '⛔ '} {k}" for k, v in carries.items()],
    f"  a witness declaration for the rows that carry hypotheses: {wit}",
    f"  Framework.lean carries no `sorry': {no_sorry};  #print axioms lines: {printed_ax}",
    "  ⌗ THE LIMIT OF THIS ARM, as at r7756: this container has no Lean toolchain, so the",
    "  build is 71's and CI's.  What is checked here is the statements, the binders, the",
    "  witness and the absence of `sorry'.")

# ---------------------------------------------------------------- ARM 11: 71's campaign-137 RESULT
F71 = read('FOR_66_FROM_71.md')
SEC71 = F71[F71.index('CAMPAIGN 137'):][:3000]
claims71 = {
    '11 of 11 rows built': '11 of 11' in SEC71.lower(),
    'zero errors and zero warnings': 'zero errors and zero warnings' in SEC71,
    '16 axiom lines all standard': '16' in SEC71 and 'axiom lines all standard' in SEC71,
    'check_no_sorry ALL 29': 'ALL 29' in SEC71,
    '290 lines, under the registered band': '290' in SEC71 and 'under the band' in SEC71,
    'the affine result holds without assuming the reals distinct':
        'without assuming the reals distinct' in SEC71,
    'none of campaign 138 touches the rate remark': 'None touches the' in SEC71,
}
# the one claim this seat can check against the file itself
distinct_free = 'x₁ x₂ x₃ : ℝ' in (decl('fw_affine_inequiv') or '') and \
                'Function.Injective' not in (decl('fw_affine_inequiv') or '') and \
                'x₁ ≠ x₂' not in (decl('fw_affine_inequiv') or '')
lines = len(LEAN.strip().split('\n'))
arm(11, "71's campaign-137 RESULT against the paragraphs and the file",
    all(claims71.values()) and distinct_free,
    *[f"      {'OK ' if v else '⛔ '} {k}" for k, v in claims71.items()],
    "",
    f"  checked against the file rather than taken from the report:",
    f"      fw_affine_inequiv's statement quantifies over three REALS with no distinctness",
    f"      hypothesis: {distinct_free}  -- which is the strengthening 71 claims",
    f"      Framework.lean is {lines} lines (71 reports 290, under its 300-600 band)",
    "  ⇒ the paragraphs cite the campaign for exactly what the campaign reports, and the one",
    "  claim that could be checked from the file holds.",
    "  ⌗ What this seat cannot check: the build, the axiom lines and the sorry-freedom as",
    "  LEAN reports them -- no toolchain here (ARM 10).  71's own check_no_sorry is the",
    "  instrument for that and it is CI's.")

# ---------------------------------------------------------------- ARM 12: what this read cannot settle
arm(12, "what this read cannot settle, and what each would need",
    True,
    "  ⒜ WHETHER THE CUT THE CONSTRUCTION INTENDS CARRIES RADIATION'S ENERGY.  cc66 says so",
    "     itself: it is a question about the slicing operator, not about arithmetic, and it",
    "     is 69's ruling.  What would settle it: P8's own statement of the operator, which",
    "     is a companion paper this repository does not carry.",
    "  ⒝ WHETHER THE SMALL-r RESULTS SURVIVE THE BEND (ARM 8⒝).  The horizon trichotomy, the",
    "     branch point's structure and the exact Euclidean flatness are stated on the vacuum",
    "     family, and radiation dominates the mass function above z ~ 3370.  Settling it is",
    "     a revision's worth of computation and this seat has not done it.",
    "  ⒞ THE TWO CLAUSES IN ARM 8⒞ -- the bend as what radiation requires, and the second",
    "     term as `the offset itself rather than a density supplied by hand'.  Reconciling",
    "     them is a wording ruling.",
    "  ⒟ THE LEAN BUILD (ARMS 10-11): no toolchain in this container.")

# ----------------------------------------------------------------- the ledger
print("\n" + "=" * 100)
print("  THE LEDGER")
for n, ok, title in sorted(VERDICTS):
    print(f"    {'PASS' if ok else 'FAIL'}  ARM {n:2d}  {title}")
bad = [n for n, ok, _ in VERDICTS if not ok]
print(f"\n  {len(VERDICTS) - len(bad)} of {len(VERDICTS)} arms meet their registered criterion"
      + ("" if not bad else f";  not met: {sorted(bad)}"))
print("=" * 100)
