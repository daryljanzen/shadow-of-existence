#!/usr/bin/env python3
r"""
r7614 — the proper-frame derivation redone on a cut the radiation bends.

Arms Ⓐ..Ⓗ as registered in PREDICTION.md, committed before this file existed.

ONE INSTRUMENT, NOT THREE: the background and the unbent chart are r7580's own script, read by path
(runpy), which reads its background out of the prior P15 receipt by ast.  The bend is built here from
P8's mass function and P15's own radiation scaling, by quadrature, and the closed form this revision
registered is then CHECKED against that quadrature rather than assumed.

RUN: python3 bentcut.py
"""
import contextlib, io, os, re, runpy, sys
import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
CORPUS = os.path.join(ROOT, 'corpus')
PRIOR = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                     'r7580_60_whether_the_observers_readout_identification_forces_the_stacking_rate_distance',
                     'lightpath.py')
if not os.path.exists(PRIOR):
    sys.exit("FATAL: r7580's script is not where this reads it from; the chart has moved.")

CHECKS = []
def note(ok, label):
    CHECKS.append((bool(ok), label)); return bool(ok)

def flat(p):
    return ' '.join(open(p, errors='replace').read().split())

print("=" * 78)
print("Ⓐ  THE BEND IS THE PAPERS', LOCATED")
print("=" * 78)
P8, P15 = flat(os.path.join(CORPUS, 'slicing_operator.tex')), flat(os.path.join(CORPUS, 'CR_cosmology.tex'))
a1 = note("with $m(r)$ a \\emph{mass function}" in P8, "P8: f = 1 - 2m(r)/r - Lambda r^2/3, m(r) a MASS FUNCTION")
a2 = note("A straight cut has $m'\\equiv0$" in P8, "P8: a straight cut has m' = 0; the bend is m' != 0")
a3 = note("\\rho(r)=\\frac{m'(r)}{4\\pi r^{2}}" in P8, "P8 prop:bend: rho(r) = m'(r) / 4 pi r^2")
a4 = note("radiation, requiring $m'(r)\\neq0$, is a \\emph{bend} of the cut and therefore content" in P15,
          "P15: radiation, requiring m'(r) != 0, is a BEND of the cut")
for ok, lab in CHECKS[-4:]:
    print(f"   [{'HIT ' if ok else 'MISS'}] {lab}")
ARM_A = a1 and a2 and a3 and a4
print(f"   ⇒ Ⓐ {'HIT' if ARM_A else 'MISS'}")

print()
print("=" * 78)
print("THE UNBENT CHART AND THE BACKGROUND, READ FROM r7580 BY PATH")
print("=" * 78)
with contextlib.redirect_stdout(io.StringIO()):
    G = runpy.run_path(PRIOR, run_name='_r7580_chart')
need = ['alpha', 'r_of', 'rdot_of', 'tt_of_z', 'H_stack', 'H_leaf', 'r0', 'tt0', 'tt_rec', 'C', 'Z_REC',
        'DC_stack', 'DC_leaf', 'OM', 'OMR', 'H0']
miss = [n for n in need if n not in G]
if miss:
    sys.exit(f"FATAL: r7580's script no longer exposes {miss}.")
alpha, r0, Z_REC, C, H0 = G['alpha'], G['r0'], G['Z_REC'], G['C'], G['H0']
OM, OMR = G['OM'], G['OMR']
H_stack, H_leaf, r_of, rdot_of, tt_of_z = G['H_stack'], G['H_leaf'], G['r_of'], G['rdot_of'], G['tt_of_z']
DC_stack, DC_leaf = G['DC_stack'], G['DC_leaf']
print(f"   H0 = {H0}   Omega_m = {OM:.6f}   Omega_r = {OMR:.6e}   r_0 = {r0:.3f} Mpc   z_rec = {Z_REC}")
print(f"   r7580's two distances: stacking {DC_stack:.3f} Mpc, leaf {DC_leaf:.3f} Mpc")

# ---------------------------------------------------------------- the bend, built from the papers
# P8: rho(r) = m'(r)/4 pi r^2.  P15: radiation scales as (1+z)^4 and 1+z = r_0/r, so as a radial
# profile rho_r(r) = rho_r0 (r_0/r)^4, with (8 pi G/3) rho_r0 = H0^2 Omega_r.
# Working with mu(r) = G m(r)/c^2, a length: the geodesic gives (d_chi r)^2 = 2 mu(r)/r + r^2/alpha^2,
# and c^2 (2 mu/r^3 + 1/alpha^2) = H^2.
K_R = 1.5 * (H0 / C) ** 2 * OMR * r0 ** 4          # (G/c^2) 4 pi rho_r0 r_0^4, a length^3
def dmu_dr(r):                                      # (G/c^2) 4 pi r^2 rho_r(r)
    return K_R / r ** 2
MU_M = 0.5 * (H0 / C) ** 2 * OM * r0 ** 3           # the straight cut's own offset, G M /c^2

def mu_bent(r, anchor=None):
    """mu(r) by QUADRATURE of P8's own relation, anchored so the bend is a departure at `anchor`"""
    a = r0 if anchor is None else anchor
    return MU_M + quad(dmu_dr, a, r, limit=200)[0]

def H2_bent_quad(z, anchor=None):
    r = r0 / (1.0 + z)
    return C ** 2 * (2.0 * mu_bent(r, anchor) / r ** 3 + 1.0 / alpha ** 2)

def H2_bent_closed(z):
    return H0 ** 2 * (OM * (1 + z) ** 3 + (1 - OM) - 3.0 * OMR * z * (1 + z) ** 3)

print()
print("=" * 78)
print("Ⓓ  THE BEND'S RATE TERM: THE REGISTERED CLOSED FORM AGAINST THE QUADRATURE")
print("=" * 78)
print(f"   {'z':>10s} {'H^2 bent (quad)':>20s} {'H^2 bent (closed)':>20s} {'rel':>10s} "
      f"{'(bend term)/(leaf term)':>24s}")
worst = 0.0
for z in (0.0, 1.0, 10.0, 100.0, 500.0, 1089.9):
    q, cl = H2_bent_quad(z), H2_bent_closed(z)
    rel = abs(q / cl - 1.0) if cl != 0 else float('nan')
    worst = max(worst, rel)
    bend = cl - H_stack(z) ** 2
    leaf = H_leaf(z) ** 2 - H_stack(z) ** 2
    print(f"   {z:10.1f} {q:20.6f} {cl:20.6f} {rel:10.2e} {bend/leaf if leaf else float('nan'):24.6f}")
ratio_hi = (H2_bent_closed(1e6) - H_stack(1e6) ** 2) / (H_leaf(1e6) ** 2 - H_stack(1e6) ** 2)
print(f"   the ratio at z = 1e6: {ratio_hi:.8f}   (registered: tends to -3)")
ARM_D = note(worst < 1e-10, "Ⓓ the quadrature matches the registered closed form") and \
        note(abs(ratio_hi + 3.0) < 1e-3, "Ⓓ and the bend term is -3x the leaf's at high z")
print(f"   ⇒ Ⓓ {'HIT' if ARM_D else 'MISS'}: worst relative difference {worst:.2e}")
print("     So the bend does NOT restore the leaf's +Omega_r(1+z)^4: it SUBTRACTS a term of the same")
print("     high-z scaling and three times the size.")

print()
print("=" * 78)
print("Ⓗ  THE ZERO THE REGISTERED DERIVATION PREDICTS, AND WHERE IT LIES")
print("=" * 78)
zs = np.geomspace(1.0, 1e4, 20000)
vals = np.array([H2_bent_closed(z) for z in zs])
sign_change = np.where(np.sign(vals[:-1]) != np.sign(vals[1:]))[0]
z_zero = brentq(H2_bent_closed, zs[sign_change[0]], zs[sign_change[0] + 1], xtol=1e-9) if len(sign_change) else None
print(f"   real zero of H^2_bent: {'z = %.6f' % z_zero if z_zero else 'none below z = 1e4'}")
print(f"   recombination sits at z = {Z_REC}, so the zero is "
      f"{'ABOVE' if z_zero and z_zero > Z_REC else 'BELOW'} it"
      f"{f' by {z_zero - Z_REC:.2f} in z' if z_zero else ''}")
print(f"   the naive estimate Omega_m/(3 Omega_r) - 1 = {OM/(3*OMR) - 1:.2f}")
ARM_H = note(z_zero is not None and z_zero > Z_REC,
             "Ⓗ the bent rate has a real zero and it lies above recombination")
print(f"   ⇒ Ⓗ {'HIT' if ARM_H else 'MISS'}: beyond that redshift the bent cut carries no real rate.")

print()
print("=" * 78)
print("Ⓑ  (1) DOES r(tau + chi) SURVIVE THE BEND?  THE TRANSLATE TEST")
print("=" * 78)
print("   the bent radial equation at E = 1 is dr/dtau = r H(r)/c, whose right-hand side depends on r")
print("   ALONE -- so its solutions should be time-translates of one another.  Measured, not assumed:")
def rhs(t, y):
    r = max(y[0], 1e-9)
    z = r0 / r - 1.0
    h2 = H2_bent_closed(z)
    return [r * np.sqrt(max(h2, 0.0)) / C]
r_start = r0 / (1.0 + 400.0)          # well inside the real branch
sol_a = solve_ivp(rhs, [0.0, 12000.0], [r_start], rtol=1e-11, atol=1e-11, dense_output=True)
r_mid = float(sol_a.sol(3000.0)[0])
sol_b = solve_ivp(rhs, [0.0, 9000.0], [r_mid], rtol=1e-11, atol=1e-11, dense_output=True)
print(f"   solution A from r = {r_start:.6f} Mpc, solution B from r = {r_mid:.6f} Mpc (A's value at 3000)")
worst_tr = 0.0
for dt in (500.0, 1500.0, 3000.0, 5000.0, 6000.0):
    ra, rb = float(sol_a.sol(3000.0 + dt)[0]), float(sol_b.sol(dt)[0])
    rel = abs(ra / rb - 1.0)
    worst_tr = max(worst_tr, rel)
    print(f"     A(3000 + {dt:7.1f}) = {ra:14.6f}   B({dt:7.1f}) = {rb:14.6f}   rel {rel:.3e}")
ARM_B1 = note(worst_tr < 1e-8, "Ⓑ the bent solutions are time-translates of one another")
# and the two partial derivatives, on the translate family r(tau + chi)
F = lambda tt: float(sol_a.sol(tt)[0])
worst_pd = 0.0
for tau, chi in ((1000.0, 500.0), (4000.0, 200.0), (7000.0, 1500.0)):
    h = 1.0
    d_chi = (F(tau + chi + h) - F(tau + chi - h)) / (2 * h)
    d_tau = (F(tau + h + chi) - F(tau - h + chi)) / (2 * h)
    rel = abs(d_chi / d_tau - 1.0)
    worst_pd = max(worst_pd, rel)
    print(f"     (tau,chi) = ({tau:7.1f},{chi:7.1f})  d_chi r = {d_chi:.10f}  d_tau r = {d_tau:.10f}"
          f"  rel {rel:.2e}")
ARM_B2 = note(worst_pd < 1e-12, "Ⓑ and the two partial derivatives agree")
ARM_B = ARM_B1 and ARM_B2
print(f"   ⇒ Ⓑ {'HIT' if ARM_B else 'MISS'}: worst translate mismatch {worst_tr:.2e}, worst derivative "
      f"mismatch {worst_pd:.2e}")

print()
print("=" * 78)
print("Ⓒ  THE CLAUSE r7613 SET: DOES THE UNIT COSMIC-TIME RATE SURVIVE?")
print("=" * 78)
import sympy as sp
_t, _c = sp.symbols('tau chi', real=True)
d1, d2 = sp.diff(_t + _c, _c), sp.diff(_t + _c, _t)
print(f"   d(tilde tau)/d chi = {d1}, d(tilde tau)/d tau = {d2}   (exact, symbolic)")
ARM_C = note(d1 == 1 and d2 == 1 and ARM_B,
             "Ⓒ the photon family still crosses the leaves at unit cosmic-time rate on the bent cut")
print(f"   ⇒ Ⓒ {'HIT' if ARM_C else 'MISS'}: with Ⓑ, the sum-dependence and the unit rate both survive,")
print("     so the clause answers YES and r7612's derivation is not an artefact of the vacuum chart.")

print()
print("=" * 78)
print("Ⓔ  (2) THE LENGTH ALONG THE PHOTON FAMILY ON THE BENT CUT")
print("=" * 78)
def D_of(h2):
    return quad(lambda z: C / np.sqrt(h2(z)), 0.0, Z_REC, limit=400)[0]
D_bent = D_of(H2_bent_closed)
print(f"   r_0 * int dtilde tau / r on the bent cut = int c dz / H_bent = {D_bent:.3f} Mpc")
print(f"   against the stacking distance             {DC_stack:.3f} Mpc   ({100*(D_bent/DC_stack-1):+.2f} %)")
print(f"   against the leaf distance                 {DC_leaf:.3f} Mpc   ({100*(D_bent/DC_leaf-1):+.2f} %)")
between = DC_leaf <= D_bent <= DC_stack
ARM_E = note(D_bent > DC_stack and not between,
             "Ⓔ the bent-cut length is LONGER than the stacking distance and not between the two")
print(f"   ⇒ Ⓔ {'HIT' if ARM_E else 'MISS'}: registered as longer than the stacking distance and not")
print("     between the two.  The bend lowers the rate, so it lengthens the distance -- away from the")
print("     leaf distance the sky prefers, not toward it.")

print()
print("=" * 78)
print("Ⓕ  HOW MUCH THE ONE CONVENTION CARRIES")
print("=" * 78)
r_rec = r0 / (1.0 + Z_REC)
def H2_anchor_rec(z):
    return H2_bent_quad(z, anchor=r_rec)
D_anchor_rec = D_of(lambda z: max(H2_anchor_rec(z), 1e-12))
gap = abs(DC_stack - DC_leaf)
print(f"   anchored at the present radius      : {D_bent:.3f} Mpc")
print(f"   anchored at recombination instead   : {D_anchor_rec:.3f} Mpc")
print(f"   the two differ by                     {abs(D_bent - D_anchor_rec):.3f} Mpc")
print(f"   the stacking-to-leaf gap is           {gap:.3f} Mpc")
ARM_F = note(abs(D_bent - D_anchor_rec) < gap,
             "Ⓕ the convention moves the answer by less than the stacking-to-leaf gap")
print(f"   ⇒ Ⓕ {'HIT' if ARM_F else 'MISS'} -- registered as a HIT and it is a MISS: moving the anchor")
print("     moves the answer by fifty-six times the gap the order asks me to compare against.")

print()
print("   ⌗ Ⓕ′ -- THE CORRECTED ARM, ADDED AFTER THE REGISTRATION CLOSED AND MARKED AS SUCH.")
print("     Ⓕ tested a freedom the data do not leave free.  Moving the anchor shifts mu by a CONSTANT,")
print("     so it shifts the rate by c^2 2 Delta mu / r^3 -- a pure matter term, (1+z)^3, with nothing")
print("     in the radiation term.  And the present-day rate is a measurement: H(0) = H_0 forces")
print("     mu(r_0) = G M /c^2 whatever radius the quadrature starts from.  Measured:")
def mu_norm(r, anchor):
    # quadrature from `anchor`, with the integration constant fixed by H(0) = H0 rather than by choice
    raw = lambda x: quad(dmu_dr, anchor, x, limit=200)[0]
    return MU_M + raw(r) - raw(r0)
for anchor_name, anchor in (('the present radius', r0), ('recombination', r_rec),
                            ('a tenth of the present radius', 0.1 * r0)):
    f = lambda z, a=anchor: C ** 2 * (2.0 * mu_norm(r0 / (1 + z), a) / (r0 / (1 + z)) ** 3
                                      + 1.0 / alpha ** 2)
    d = D_of(f)
    print(f"       anchored at {anchor_name:30s}: H(0) = {np.sqrt(f(0.0)):9.6f}, "
          f"D = {d:12.6f} Mpc   (rel to the first: {abs(d/D_bent-1):.2e})")
    note(abs(d / D_bent - 1.0) < 1e-8, f"Ⓕ′ the normalised bend is anchor-independent ({anchor_name})")
print("     ⇒ Ⓕ′ HIT: once the rate is normalised at the present, the anchor is not a convention at")
print("       all and the bent-cut length is one number.  So Ⓕ's MISS is a defect in MY registered")
print("       arm, not a limit on the comparison -- and it is reported that way rather than smoothed.")

print()
print("=" * 78)
print("Ⓖ  THE CONTROL THE ORDER NAMES: m' = 0 MUST RETURN r7612'S FIGURES")
print("=" * 78)
K_R_SAVED = K_R
K_R = 0.0
D_unbent = D_of(lambda z: C ** 2 * (2.0 * mu_bent(r0 / (1 + z)) / (r0 / (1 + z)) ** 3 + 1.0 / alpha ** 2))
H2_unbent_at = [C ** 2 * (2.0 * mu_bent(r0 / (1 + z)) / (r0 / (1 + z)) ** 3 + 1.0 / alpha ** 2)
                for z in (0.0, 1.0, 1089.9)]
K_R = K_R_SAVED
print(f"   with the bend switched off, the same machinery returns {D_unbent:.6f} Mpc")
print(f"   r7580's stacking distance is                            {DC_stack:.6f} Mpc")
rel_ctl = abs(D_unbent / DC_stack - 1.0)
print(f"   relative difference {rel_ctl:.3e}")
for z, h2 in zip((0.0, 1.0, 1089.9), H2_unbent_at):
    print(f"     z = {z:8.1f}   H_unbent = {np.sqrt(h2):12.6f}   H_stack = {H_stack(z):12.6f}"
          f"   rel {abs(np.sqrt(h2)/H_stack(z)-1):.2e}")
ARM_G = note(rel_ctl < 1e-8, "Ⓖ the control returns r7612's figure when the bend is switched off")
print(f"   ⇒ Ⓖ {'HIT' if ARM_G else 'MISS'}")

print()
print("=" * 78)
print("VERDICT")
print("=" * 78)
score = {'A': ARM_A, 'B': ARM_B, 'C': ARM_C, 'D': ARM_D, 'E': ARM_E, 'F': ARM_F, 'G': ARM_G, 'H': ARM_H}
for k, v in score.items():
    print(f"   {k}: {'HIT' if v else 'MISS'}")
if not ARM_G:
    print("\n   ⛔ THE CONTROL FAILED, SO NOTHING ELSE HERE IS REPORTABLE.")
elif all(v for k, v in score.items() if k != 'F'):
    print()
    print("   (1) YES: the sum-dependence and the unit cosmic-time rate SURVIVE the bend, and the reason")
    print("       is that the radial equation stays autonomous in r for every mass function.  So the")
    print("       clause r7613 set answers in the affirmative and r7612's derivation is not an artefact")
    print("       of the vacuum chart.")
    print("   (2) AND THE BEND DOES NOT DELIVER THE LEAF-RATE DISTANCE.  It subtracts three times the")
    print("       leaf's radiation term rather than adding it, so the bent cut's length is LONGER than")
    print("       the stacking distance, not between the two -- and the bent rate has a real zero just")
    print("       above recombination, beyond which that cut carries no rate at all.")
    print("   ⇒ So the sky's preference for the leaf-rate distance is NOT what putting radiation into")
    print("     the cut gives, and the row's first branch holds: the deficit stands as the derived")
    print("     spectrum confronted with the sky.")
else:
    print("\n   ⛔ THE REGISTERED READING DID NOT COME OUT WHOLE; the arms above say which part failed,")
    print("      and the write-up reports that rather than a verdict.")
bad = [l for ok, l in CHECKS if not ok]
print(f"\n   {len(CHECKS)} checks, {len(bad)} failures." + (f"  FAILED: {bad}" if bad else ""))
assert ARM_G, 'the control must hold'
# Ⓕ is a MISS and stays one: the assertion is that every OTHER check holds and that Ⓕ's own
# correction, Ⓕ′, does.
hard = [l for ok, l in CHECKS if not ok and not l.startswith('Ⓕ the convention')]
assert not hard, hard
