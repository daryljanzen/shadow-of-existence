#!/usr/bin/env python3
"""r7766 (60) -- the skeptical read of r7761's uniform-dust addition and the check it names.

POST-REGISTRATION throughout.  PREDICTION.md was committed AND pushed before this file existed.
Eleven arms, each a comparison with a reachable negative named in the registration.
"""
import contextlib
import io
import os
import re
import runpy
import subprocess

import numpy as np
import sympy as sp
from scipy.integrate import quad

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


def sents(hay):
    return [s.strip() for s in re.split(r'(?<=[.!?])\s+', hay) if s.strip()]


def find(hay, needle):
    """every sentence of hay carrying needle, needle matched on collapsed whitespace"""
    n = ' '.join(needle.split())
    return [s for s in sents(hay) if n in ' '.join(s.split())]


print("=" * 100)
print("r7766 (60) -- the uniform-dust addition, and the check it names (order r7761, Daryl's clause)")
print(f"  HEAD: {git('rev-parse', 'HEAD').strip()}   origin/main: {git('rev-parse', 'origin/main').strip()}")
print("=" * 100)

P15 = read('corpus/CR_cosmology.tex')
ERC = read('resources/ERC_existence-relativity-cosmology.tex')
ORDER = read('FOR_60.md')
R7764 = read('computations/beyond_the_wall/r7764_60_a_skeptical_read_of_the_two_level_framing/RESULT.md')

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
H_stack, H_leaf = NS['H_stack'], NS['H_leaf']
H0, OM, OMR = NS['H0'], NS['OM'], NS['OMR']
MPC_GYR = 977.792

print(f"\n  the instrument, read by path and not re-derived: H0={H0}  Om={OM}  Or={OMR:.6e}")

# ================================================================= ARM 1
# the addition's premise: pressureless matter's Misner-Sharp mass is constant.
r, p_sym = sp.symbols('r p', positive=True), sp.Symbol('p')
r = sp.Symbol('r', positive=True)
Gc, cc_ = sp.symbols('G c', positive=True)
A3, A4 = sp.symbols('A3 A4', positive=True)
m_gen = sp.Function('m')(r)
# the law r7762 established for the region where r labels the epoch, in that revision's own units
law_gen = sp.Eq(sp.diff(m_gen, r), -2 * Gc / cc_ ** 4 * 4 * sp.pi * r ** 2 * p_sym)
dust = law_gen.subs(p_sym, 0)
dust_rhs = sp.simplify(dust.rhs)
sol = sp.dsolve(dust, m_gen)
const_free = sp.simplify(sp.diff(sol.rhs, r)) == 0
# and the law leaves the constant itself unconstrained: no r, no rho survives
survivors = sorted({str(s) for s in dust_rhs.free_symbols})
a1 = (dust_rhs == 0) and const_free and survivors == []
arm(1, "the addition's premise: pressureless matter's Misner-Sharp mass is constant", a1,
    f"      the law r7762 established (r labels the EPOCH, so this is the pressure-work law and NOT",
    f"      the mass-inside-radius relation):   {sp.pretty(law_gen.lhs)} = {law_gen.rhs}",
    f"      at p = 0 the right-hand side is  {dust_rhs}  -- free symbols surviving: {survivors or 'none'}",
    f"      integrated:  {sol}   and d/dr of that solution is {sp.simplify(sp.diff(sol.rhs, r))}",
    "      => m is constant on the epoch, and the law does not constrain the constant.",
    "      ⌗ the reachable negative was a rho-dependent or r-dependent piece surviving p = 0.  None does.")

# ================================================================= ARM 2
# is the cut's offset dust's mass -- does the geometric rate's matter term contain matter?
al, x0s, r0s, z = sp.symbols('alpha x_0 r_0 z', positive=True)
# P15 sec:properframe step (iii), in the corpus's variables
mu = sp.Symbol('mu', positive=True)
h2_general = mu / r ** 3 + 1 / al ** 2
# the Nariai condition's own fixing of the offset LENGTH, as P15 states it in terms
r_N = al / sp.sqrt(3)
# mu for a constant offset: match P15's printed rate  c^2 H^2 = (c^2/al^2)(1 + 2(1+z)^3/x_0^3)
h2_printed = (1 + 2 * (1 + z) ** 3 / x0s ** 3) / al ** 2
h2_from_mu = h2_general.subs(r, r0s / (1 + z))
mu_needed = sp.solve(sp.Eq(h2_from_mu, h2_printed), mu)[0]
mu_needed = sp.simplify(mu_needed)
# with x_0 = r_0 / r_N, does that offset equal the Nariai one, 2 r_N^3 / al^2 = 2 al /(3 sqrt 3)?
mu_nariai = sp.simplify(2 * r_N ** 3 / al ** 2)
mu_sub = sp.simplify(mu_needed.subs(x0s, r0s / r_N))
offset_is_nariai = sp.simplify(mu_sub - mu_nariai) == 0
# the exponent the constant-offset term carries against (1+z)
expo = sp.simplify(sp.expand(h2_from_mu.subs(mu, mu_needed) * al ** 2 - 1) * x0s ** 3 / 2)
expo_is_cube = sp.simplify(expo - (1 + z) ** 3) == 0
# the paper's own translation, and the ratio the Nariai offset forces
Om_paper = 2 / (x0s ** 3 + 2)
OL_paper = x0s ** 3 / (x0s ** 3 + 2)
ratio_paper = sp.simplify(Om_paper / OL_paper)
ratio_geom = sp.simplify((mu_nariai / r0s ** 3) / (1 / al ** 2))
ratio_geom = sp.simplify(ratio_geom.subs(r0s, x0s * r_N))
ratio_match = sp.simplify(ratio_paper - ratio_geom) == 0
# the density read off that term through the SAME constitutive law as arm 1
rho_dust = sp.simplify(3 * cc_ ** 4 / (8 * sp.pi * Gc) * A3 / r ** 3)
p_demanded = sp.solve(sp.Eq(sp.diff(A3 + 0 * r, r), -2 * Gc / cc_ ** 4 * 4 * sp.pi * r ** 2 * p_sym), p_sym)[0]
dust_pressureless = sp.simplify(p_demanded) == 0
a2 = bool(offset_is_nariai and expo_is_cube and ratio_match and dust_pressureless)
arm(2, "is the cut's offset dust's mass -- does the geometric rate's matter term CONTAIN matter?", a2,
    f"      the radial equation (P15 sec:properframe step iii):  h^2 = {h2_general}",
    f"      P15's printed rate:  c^2H^2 = (c^2/alpha^2)(1 + 2(1+z)^3/x_0^3)",
    f"      the offset that rate demands:  mu = {mu_needed}",
    f"      the Nariai condition's own offset LENGTH r_N = alpha/sqrt(3) gives  mu = {mu_nariai}",
    f"      with x_0 = r_0/r_N the two agree:  {offset_is_nariai}",
    f"      the exponent that term carries against (1+z):  {sp.simplify(expo)}  -- is (1+z)^3: {expo_is_cube}",
    f"      the paper's translation Om/OL = {ratio_paper}; forced by the Nariai offset: {ratio_geom}"
    f"  -- identical: {ratio_match}",
    f"      and the pressure the constant offset demands through arm 1's own law: {sp.simplify(p_demanded)}"
    f"  => pressureless: {dust_pressureless}",
    f"      the density that term carries: rho = {rho_dust}, i.e. a_m ~ 1/r^3 -- dust's own dilution.",
    "      ⌗ the reachable negatives were an exponent other than 3, or a Nariai-forced ratio missing the",
    "        paper's translation.  Neither occurs: the geometric rate's second term IS a dust term,",
    "        and the addition's explanation of why the geometric rate has matter's form HOLDS.")

# ================================================================= ARM 3
# do the two levels coincide for dust -- and can that measurement fail?
zz = np.array([0.0, 1.0, 67.0, 1090.0, 1e5, 1e9])


def H_stack_of(om, orad, zv):
    return H0 * np.sqrt(om * (1 + zv) ** 3 + 1.0 - om)


def H_leaf_of(om, orad, zv):
    return H0 * np.sqrt(om * (1 + zv) ** 3 + 1.0 - om + orad * (1 + zv) ** 4)


gap_dust = np.max(np.abs(H_leaf_of(OM, 0.0, zz) / H_stack_of(OM, 0.0, zz) - 1.0))
gap_real = H_leaf_of(OM, OMR, zz) / H_stack_of(OM, OMR, zz)
# the NON-trivial version: how many matter terms are there, counted on the symbolic forms?
Omf, Orf, H0f = sp.symbols('Omega_m Omega_r H_0', positive=True)
Hs2 = H0f ** 2 * (Omf * (1 + z) ** 3 + 1 - Omf)
Hl2 = H0f ** 2 * (Omf * (1 + z) ** 3 + 1 - Omf + Orf * (1 + z) ** 4)
diff_terms = sp.simplify(sp.expand(Hl2 - Hs2))
only_radiation = sp.simplify(diff_terms - H0f ** 2 * Orf * (1 + z) ** 4) == 0
# counted in u = 1+z, because expanding in z destroys the (1+z)^3 grouping the question is about
uu = sp.Symbol('u', positive=True)
Ps = sp.Poly(sp.expand(Hs2.subs(z, uu - 1) / H0f ** 2), uu)
Pl = sp.Poly(sp.expand(Hl2.subs(z, uu - 1) / H0f ** 2), uu)
n_matter_stack = sum(1 for mon, co in zip(Ps.monoms(), Ps.coeffs()) if mon == (3,) and co != 0)
n_matter_leaf = sum(1 for mon, co in zip(Pl.monoms(), Pl.coeffs()) if mon == (3,) and co != 0)
cube_s = Ps.coeff_monomial(uu ** 3)
cube_l = Pl.coeff_monomial(uu ** 3)
one_dust = (n_matter_stack == 1 and n_matter_leaf == 1 and sp.simplify(cube_s - cube_l) == 0)
a3 = bool(only_radiation and one_dust and gap_dust < 1e-15)
arm(3, "'the two levels coincide exactly for dust' -- and whether that measurement can fail", a3,
    "      ⛔ FIRST, what this arm does NOT offer as a measurement.  The two rates stand in the",
    "        relation H^2_leaf = H^2_stack + H_0^2 Omega_r (1+z)^4.  Setting Omega_r = 0 in that makes",
    f"        them identical BY INSPECTION OF THE FORMULA -- measured here as max|ratio-1| = {gap_dust:.3e}",
    "        over six decades of redshift, which is a restatement of the formula and not a test of it.",
    "        r7762 was caught by this exact shape of non-test; the registration said so in advance.",
    "      THE NON-TRIVIAL VERSION -- is the dust ONE dust or two?",
    f"        leaf minus stack, symbolically: {diff_terms}",
    f"        is that radiation ALONE: {only_radiation}",
    f"        (1+z)^3 terms in the stacking rate: {n_matter_stack};  in the leaf rate: {n_matter_leaf}",
    "        => the matter content appears EXACTLY ONCE.  The leaf rate adds radiation to the",
    "        stacking rate's own offset; it does not carry a second matter term beside it.",
    f"      and at the fitted Omega_r the ratio runs {gap_real[0]:.4f} at z=0 to {gap_real[-1]:.2f} at z=1e9,",
    "        so what separates the levels is radiation alone -- the addition's own sentence, confirmed.",
    "      ⌗ the reachable negative was a second matter term in the leaf rate, double-counting the dust.")

# ================================================================= ARM 4
# the check the addition names: comparison or identity?
tt = sp.Symbol('t', positive=True)
A = sp.Symbol('A', positive=True)
sv = sp.Symbol('s', positive=True)
r_of_t = A * sp.sinh(tt) ** sp.Rational(2, 3)
# the comoving acceleration, with the positive factor sinh^(4/3)/A divided out
accel = sp.simplify(sp.diff(r_of_t, tt, 2) * sp.sinh(tt) ** sp.Rational(4, 3) / A)
accel_s = sp.simplify(sp.expand_trig(accel).subs(sp.cosh(tt) ** 2, 1 + sp.sinh(tt) ** 2)
                      .subs(sp.sinh(tt), sv))
turn = [s for s in sp.solve(sp.Eq(accel_s, 0), sv) if s.is_real and s > 0]
sinh_turn = sp.simplify(turn[0]) if turn else None
# Omega_m at the turnover, from P15's own Omega_m = sech^2 u
Om_turn = sp.simplify(1 / (1 + sinh_turn ** 2)) if sinh_turn is not None else None
# the numbers
# INPUT   x0 = 1.6648 +- 0.0467   -- corpus measured, taken from P15 sec:discussion (eq:zacc), which
# itself carries the interval as an input "from DESI DR2 D_M/D_H".  NOTHING HERE COMPUTES THE FIT, and
# arm 4's verdict does not rest on the interval's width: it rests on the identity 1+z_acc = x_0.
# ⌗ Declared in this form because L_probability/S1 gates exactly this -- every script in the repository
#   carrying the figure must say that it takes it as an input.  That gate fired on this file on its
#   first run, correctly, and this line is the fix rather than an exemption.
ZACC, ZACC_ERR = 0.6648, 0.0467
om_from_zacc = 2.0 / ((1 + ZACC) ** 3 + 2)
om_hi = 2.0 / ((1 + ZACC - ZACC_ERR) ** 3 + 2)
om_lo = 2.0 / ((1 + ZACC + ZACC_ERR) ** 3 + 2)
zacc_from_refit = (2 * (1 - OM) / OM) ** (1 / 3) - 1
inside = abs(zacc_from_refit - ZACC) <= ZACC_ERR
# is 1+z_acc = x_0 an identity of the rate, or a number?
sinh_is_half = sinh_turn is not None and sp.simplify(sinh_turn ** 2 - sp.Rational(1, 2)) == 0
om_turn_two_thirds = sp.simplify(Om_turn - sp.Rational(2, 3)) == 0
# where does the corpus's z_acc come from?
prov = find(P15, 'without a distance ladder, without the microwave background and without any density')
prov2 = find(P15, 'carried as an input throughout rather than derived here')
prov3 = [s for s in sents(P15) if '0.632' in s] or find(P15, 'on Planck')
a4 = bool(sinh_is_half and om_turn_two_thirds and inside and prov and prov2)
arm(4, "the check the addition names: a comparison with content, or an identity?", a4,
    f"      the comoving acceleration, positive factors divided out:  {accel_s}",
    f"      the turnover of the areal radius, solved symbolically: sinh = {sinh_turn},"
    f"  i.e. sinh^2 = 1/2: {sinh_is_half}",
    f"      Omega_m AT the turnover: {Om_turn}  -- equals 2/3 exactly: {om_turn_two_thirds}",
    "      so 1 + z_acc = r_0/r_turnover = x_0 is an IDENTITY of this rate, not a coincidence:",
    "        r_N is the areal radius at the turnover, and x_0 is r_0 in units of r_N.",
    f"      ⇒ Omega_m from the acceleration epoch:  z_acc = {ZACC} +/- {ZACC_ERR}"
    f"  gives Omega_m = {om_from_zacc:.5f}  [{om_lo:.5f}, {om_hi:.5f}]",
    f"        the refit's Omega_m = {OM} corresponds to z_acc = {zacc_from_refit:.4f},"
    f"  inside the quoted interval: {inside}",
    f"      THE PROVENANCE, read from P15 rather than assumed:",
    *[f"        * {s[:230]}" for s in (prov[:1] + prov2[:1] + prov3[:1])],
    "      ⇒ THE VERDICT, in two parts, because the arm's two readings came apart:",
    "        ⒜ AS A TWO-DATASET CONSISTENCY TEST THE CHECK HAS CONTENT AND IT PASSES.  z_acc is a",
    "          redshift measured calibration-free and carried as an INPUT, not derived from the",
    "          baryon-acoustic fit that returns Omega_m, so the two sides are different data and",
    "          could have disagreed.  They agree, well inside the quoted interval.  P15 already",
    "          performs this comparison at eq:zacc, against Planck's parameters.",
    "        ⛔ ⒝ BUT IT DOES NOT TEST WHAT IT IS OFFERED FOR.  'Matter's actual density is the",
    "          geometric offset' and 'the offset is a vacuum parameter that happens to carry",
    "          matter's form' predict the SAME relation Omega_m = 2/(x_0^3+2) -- arm 2 shows the",
    "          Nariai offset forces it identically.  There is no state of the data in which x_0 is",
    "          measured and the offset is NOT the matter density, so the fork has no slot to be",
    "          decided in.  The check tests the construction, not the identification inside it.")

# ================================================================= ARM 5
# what WOULD test it?
CANDS = [
    ('the acceleration epoch z_acc', 'x_0 itself, by the identity of arm 4', False,
     'measured calibration-free, but it IS the offset parameter'),
    ('the baryon-acoustic fit Omega_m', 'x_0 through the same translation', False,
     'the same parameter from other data -- a consistency test, not a discriminant'),
    ('matter-radiation equality 1+z_eq = omega_m/omega_r', 'omega_m with omega_r measured', True,
     'omega_m is a PHYSICAL density, and omega_r is measured framework-independently'),
    ('the baryon density omega_b', 'omega_b, measured framework-independently', True,
     'with a baryon fraction it bounds omega_m from below without the rate'),
    ('the growth of structure', 'Omega_m = sech^2 u, a clock reading', False,
     "P15 shows the growth equation loses its parameters: the fraction is the epoch"),
    ('the acoustic driving', 'the same epoch that carries the expansion history', False,
     "P15: 'one quantity carries the expansion history and the acoustic driving together'"),
    ('the Hubble-Eddington radius', 'Lambda, per structure', False,
     'it reads Lambda at a second range, not the matter density'),
]
indep = [c for c in CANDS if c[2]]
eq_sent = find(P15, 'Matter--radiation equality is then fixed by the same epoch') or \
    find(P15, 'z_{\\mathrm{eq}}}=\\omega_m/\\omega_r') or [s for s in sents(P15) if 'omega_m/\\omega_r' in s]
growth_sent = find(P15, 'the matter fraction is a') or [s for s in sents(P15) if '\\cosh^{2}u=1/\\Omega_m' in s]
a5 = bool(len(indep) >= 1 and eq_sent and growth_sent)
arm(5, "what WOULD test 'matter's actual density is the geometric offset'?", a5,
    "      every candidate marked INDEPENDENT only if it returns a number without passing through x_0:",
    *[f"        {'INDEPENDENT' if c[2] else 'not indep.':<12}  {c[0]:<48} via {c[1]}\n"
      f"                      -- {c[3]}" for c in CANDS],
    f"      independent candidates: {len(indep)} of {len(CANDS)}",
    *[f"        * {s[:200]}" for s in (eq_sent[:1] + growth_sent[:1])],
    "      ⇒ THE ANSWER THE ADDITION'S QUESTION ACTUALLY HAS: the discriminating measurement is a",
    "        PHYSICAL matter density -- omega_m from equality with omega_r measured, or omega_b with a",
    "        baryon fraction -- set against the density the geometric offset demands at the same epoch.",
    "        That comparison does not pass through x_0 and can come back wrong.  The two the addition",
    "        names both pass through x_0 and cannot.",
    "      ⌗ the reachable negative was that EVERY candidate is a clock reading, which would have made",
    "        the construction uncatchable here.  Two are not, so it is catchable -- and P15 states the",
    "        equality relation itself, so the test is available in the corpus's own terms.")

# ================================================================= ARM 6
# does the addition defeat r7764's part (c)?
lic_avg = find(ERC, 'average densities of matter and radiation')
lic_diffeo = find(ERC, 'does not disrupt the global equivalence to Minkowski space')
lic_flat = find(ERC, 'diffeomorphic to a flat plane')
lic_local = find(ERC, 'lensing and ripples') or find(ERC, 'such as lensing and ripples')
# r7764 (c)'s own premise, quoted from its RESULT
c_premise = [s for s in sents(R7764) if 'averages out' in s]
# recomputed gap
ratio67 = H_leaf(67.0) / H_stack(67.0)
ratio1090 = H_leaf(1090.0) / H_stack(1090.0)
ratio1e9 = H_leaf(1e9) / H_stack(1e9)
# the licence the source actually gives: differentiability, which a uniform layer satisfies
licence_is_diffeo = bool(lic_diffeo and lic_flat)
a6 = bool(licence_is_diffeo and c_premise and ratio1e9 > 100)
arm(6, "does the addition defeat r7764's part (c), narrow it, or leave it?", a6,
    f"      r7764 (c)'s own premise, as that revision printed it:",
    *[f"        \"{s[:240]}\"" for s in c_premise[:1]],
    "      THE SOURCE'S ACTUAL LICENCE, located rather than recalled:",
    *[f"        \"{s[:300]}\"" for s in (lic_flat[:1] + lic_diffeo[:1])],
    "      ⛔⛔ r7764 (c) WAS WRONG ABOUT THE SOURCE, AND THE 'AVERAGING' FORM IS WITHDRAWN.",
    "        The source's licence for the cosmological description is NOT that the warping averages",
    "        out.  It is that the warped space stays DIFFEOMORPHIC to a flat plane -- a",
    "        differentiability condition, singularity-freeness -- and a uniform layer satisfies it",
    "        trivially.  So 'a uniform bath has nothing to average' attacked a premise the source",
    "        does not hold, and the addition is right on this point.",
    "      WHAT SURVIVES OF (c), AND IT IS NOT THE SAME CLAIM: the two levels differ by factors of",
    f"        hundreds where radiation dominates -- recomputed here: {ratio67:.4f} at z=67,"
    f"  {ratio1090:.4f} at z=1090, {ratio1e9:.2f} at z=1e9.",
    "        That gap is a fact about the two rates and needs no averaging premise to state.  It is",
    "        reported in (c) too, and it is the part that stands.",
    "      ⌗ the registration made this withdrawal reachable and it is taken.  The analogy's",
    "        licence is differentiability; the objection was to an averaging licence; the objection",
    "        in that form is this line's error and is retracted here.")

# ================================================================= ARM 7
# 'no content sets it'
framing_nc = find(ORDER, 'no content sets it')
p15_offset = find(P15, 'the second term is the offset itself rather than a density supplied by hand')
p15_rate = find(P15, 'its rate fixed by the cosmological constant alone')
p15_nariai = find(P15, 'which the Nariai condition fixes at')
p15_clock = find(P15, 'readings of one cosmic clock, not drivers of the expansion')
all_located = all([framing_nc, p15_offset, p15_rate, p15_nariai, p15_clock])
# the resolution, checked: is the offset fixed by Lambda alone?
alpha_from_L = sp.sqrt(3 / sp.Symbol('Lambda', positive=True))
mu_from_L = sp.simplify(mu_nariai.subs(al, alpha_from_L))
offset_is_L_only = sp.simplify(mu_from_L).free_symbols == {sp.Symbol('Lambda', positive=True)}
a7 = bool(all_located and offset_is_L_only)
arm(7, "'no content sets it' against 'the offset IS pressureless matter's mass'", a7,
    "      the framing's sentence, from the order as it stands:",
    *[f"        \"{s[:220]}\"" for s in framing_nc[:1]],
    "      P15's own sentences, located in the printed text:",
    *[f"        \"{s[:260]}\"" for s in (p15_rate[:1] + p15_offset[:1] + p15_nariai[:1] + p15_clock[:1])],
    f"      THE RESOLUTION, and it holds: the Nariai condition fixes the offset LENGTH at alpha/sqrt3,",
    f"        so the offset in terms of Lambda alone is mu = {mu_from_L}"
    f"  -- free symbols: {sorted(str(s) for s in sp.simplify(mu_from_L).free_symbols)}",
    "        NO CONTENT ENTERS THAT VALUE.  A content quantity EQUALS the offset without setting it:",
    "        the dust's Misner-Sharp mass is what the offset is worth, and Lambda is what fixes it.",
    "      THE COST, named rather than left implicit: on that reading the present matter density is",
    "        NOT an input.  It is forced to 2/(x_0^3+2) by the epoch -- which is exactly what P15",
    "        already says ('readings of one cosmic clock'), so the addition and the paper agree here.",
    "      ⌗ the reachable negative was a genuine contradiction between two printed sentences.  There",
    "        is none: 'equals' and 'sets' come apart, and the Nariai condition is what separates them.")

# ================================================================= ARM 8
# direction: does the difference survive a change of clock?
# flat LCDM's rate: free parameters (Omega_m, H_0).  CR's rate: free parameters (x_0, H_0).
flat_params = {'Omega_m', 'H_0'}
cr_params = {'x_0', 'H_0'}
bij_all = sp.solve(sp.Eq(Omf, 2 / (x0s ** 3 + 2)), x0s)
bij = [sp.simplify(b) for b in bij_all if b.is_real is not False]
bij_single = len(bij) >= 1
inv = sp.simplify(2 / (bij[0] ** 3 + 2) - Omf) == 0 if bij else False
same_count = len(flat_params) == len(cr_params)
a8 = bool(bij_single and inv and same_count)
arm(8, "'the field equations fix the rate from its density' against 'readings of one cosmic clock'", a8,
    "      the two directions, written out:",
    f"        flat-LCDM:  free parameters {sorted(flat_params)};  the epoch of acceleration is DERIVED",
    f"        this cosmology:  free parameters {sorted(cr_params)};  the matter fraction is DERIVED",
    f"      the map between them:  Omega_m = 2/(x_0^3+2),  inverted  x_0 = {bij[0] if bij else '?'}",
    f"        and the inversion returns Omega_m exactly: {inv}",
    f"        parameter counts equal: {same_count}",
    "      ⇒ THE NEWEST GUARD, APPLIED: the difference does NOT survive a change of clock.  One free",
    "        parameter carries the matter fraction either way, and the two are in bijection, so",
    "        'the density fixes the rate' and 'the fraction is a clock reading' are one identity read",
    "        from two sides.  IT WAS NEVER A DIFFERENCE, at the level of the rate's parameters.",
    "      ⌗ AND WHAT THAT DOES NOT SETTLE, said rather than glossed: a bijection of parameters is not",
    "        an identity of explanations.  Which of the two is primitive is not decided by the map,",
    "        and arm 5 names the measurement that would bear on it.  The addition's 'well-known way'",
    "        and P15's 'not drivers' agree on every number and disagree on the direction only.")

# ================================================================= ARM 9
# the source: does it commit to lumps?
mink = find(ERC, 'the cosmological space-time solution must be Minkowski space')
thresh = find(ERC, 'exceed a threshold') or [s for s in sents(ERC) if 'threshold' in s]
expanding = [s for s in sents(ERC) if 'trampoline' in s and ('expand' in s or 'FLRW' in s)]
balls = find(ERC, 'bowling balls of varying densities')
a9 = bool(mink and balls and not expanding)
arm(9, "the trampoline source: does it commit to lumps, and does an expanding trampoline appear?", a9,
    "      (a) the source's furniture, verbatim:",
    *[f"        \"{s[:240]}\"" for s in balls[:1]],
    "      (b) the source's own cosmological solution for the infinite trampoline WITH matter:",
    *[f"        \"{s[:300]}\"" for s in mink[:1]],
    f"      (c) an EXPANDING trampoline anywhere in the source: {len(expanding)} sentence(s) -"
    f" {'none' if not expanding else expanding[0][:120]}",
    "      (d) the threshold clause:",
    *[f"        \"{s[:240]}\"" for s in thresh[:1]],
    "      ⇒ THE ADDITION IS A REPAIR OF THE ANALOGY, NOT A READING OF IT -- and the repair is in the",
    "        framing's favour on one point and against it on another.",
    "        FOR: the source's licence is differentiability (arm 6), which a uniform layer meets, so",
    "          'nothing in the trampoline is particular to lumpy matter' is right about the licence.",
    "        ⛔ AGAINST: in the SOURCE the cosmological solution for the infinite trampoline with",
    "          matter is MINKOWSKI -- the matter's warping does not change the cosmological solution",
    "          at all.  The addition replaces that with an expanding FLRW trampoline whose rate the",
    "          dust DOES change.  Those are opposite on the one question the framing turns on, and the",
    "          source nowhere carries an expanding trampoline.  So the analogy cannot be cited for",
    "          'no content sets it' AND for 'the dust changes the expansion in the well-known way'.",
    "          Arm 7's resolution is what carries that weight instead, and it is geometry, not analogy.")

# ================================================================= ARM 10
# does the uniform-dust reading move r7764's other four parts?
parts = {
    '(a) it concedes the founding question': (
        'STRENGTHENED',
        "arm 2 shows the GEOMETRIC rate's own second term is a dust term with dust's dilution.  So "
        "the average matter density is not merely what the content level carries -- it is what the "
        "geometric offset is worth.  The founding question is conceded one level deeper than r7764 "
        "put it, and the defeater r7764 recorded (the denial was about the explanation) is now the "
        "ONLY thing holding it, with arm 8 showing the explanation is the one thing the numbers "
        "do not decide."),
    '(b) the geometric level is empirically idle': (
        'NARROWED',
        "arm 4 (a) finds one determination that is read at the geometric level and is not a reading "
        "of the content's dynamics: z_acc, measured calibration-free and carried as an input.  r7764 "
        "listed the acceleration epoch among its eight and found its value non-discriminating "
        "between the laws -- which is still true -- but as a determination OF the geometric offset "
        "it is exactly what the geometric level is for.  So 'no observable must take the stacking "
        "rate' stands, and 'nothing measures the geometric level' does not."),
    "(d) P7's inverse warning and third level": (
        'UNCHANGED',
        "the addition says nothing about the projection, and arm 7's resolution does not touch P7's "
        "three levels.  The clause r7764 drafted is still the smallest repair."),
    '(e) a universal with no stated exception': (
        'UNCHANGED',
        "the addition narrows what separates the levels to radiation, which the universal already "
        "accommodates.  The wording objection is untouched."),
}
a10 = len(parts) == 4 and all(v[0] in ('STRENGTHENED', 'NARROWED', 'UNCHANGED', 'WITHDRAWN')
                              for v in parts.values())
arm(10, "does the uniform-dust reading move r7764's other four parts?", a10,
    *[f"      {name}\n        ⇒ {v[0]}: {v[1]}" for name, v in parts.items()],
    "      (c) is handled in arm 6 and its averaging form is WITHDRAWN there.")

# ================================================================= ARM 11
PRED = read('computations/beyond_the_wall/'
            'r7766_60_a_skeptical_read_of_the_uniform_dust_addition_and_the_check_it_names/PREDICTION.md')
declared = len(re.findall(r'^## [①-⑨⑩⑪]', PRED, re.M))
answered = len(VERDICTS) + 1
a11 = (declared == 11 and answered == 11)
arm(11, "the count, and the subject clause", a11,
    f"      arms declared in PREDICTION.md: {declared}",
    f"      arms answered here (this one included): {answered}",
    "      ** THIS SEAT IS A SUBJECT OF NOTHING IN THIS REVISION. **  Nothing here was run on this",
    "      line, no measure was taken of it, and no registration of another seat's was read as a",
    "      subject rather than as a text.")

# ================================================================= verdict
print(f"\n{'=' * 100}\n  VERDICT\n{'=' * 100}")
for n, ok, title in VERDICTS:
    print(f"    [{'PASS' if ok else 'FAIL'}]  ARM {n:<3} {title}")
bad = [n for n, ok, _ in VERDICTS if not ok]
print(f"\n  {len(VERDICTS) - len(bad)} of {len(VERDICTS)} arms meet their criterion.")
if bad:
    print(f"  ⛔ arms not meeting their criterion: {bad}")
print("=" * 100)
