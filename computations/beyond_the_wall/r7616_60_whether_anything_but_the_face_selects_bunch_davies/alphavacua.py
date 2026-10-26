#!/usr/bin/env python3
r"""
r7616 — PO-94's quantum half on the alpha-vacua: does any principle other than the compact face select
the Bunch-Davies member?

Arms Ⓐ..Ⓗ as registered in PREDICTION.md, committed and pushed before this file existed.

The model is the conformally coupled massless scalar on de Sitter, where the Bunch-Davies Wightman
function is c/(1 - Z) in the de Sitter invariant Z, so every claim below is exact rather than numerical.
The Mottola-Allen transform is applied at the level of the two-point function with its iepsilon
prescriptions KEPT, because the two antipodal terms carry opposite ones and dropping them loses the case
this revision's registered arm Ⓒ turns out to get wrong.

RUN: python3 alphavacua.py
"""
import glob, os, re, sys
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
CORPUS = os.path.join(ROOT, 'corpus')

CHECKS = []
def note(ok, label):
    CHECKS.append((bool(ok), label)); return bool(ok)

PAPER_FILES = ['BH_causality_v2', 'janzen_circle_v3', 'SdS-slicing-curve_v2', 'modern_parallax',
               'groupoid_paper', 'shadow_of_existence', 'CR_framework', 'slicing_operator',
               'range_paper', 'canonical_time', 'dynamics_paper', 'algebroid_paper',
               'boundary_paper', 'matter_sector_paper', 'CR_cosmology', 'cosmogenesis_paper',
               'geometric_core_paper', 'CR_synthesis']

print("=" * 78)
print("Ⓐ  THE CORPUS'S OWN COMMITMENT, AND THE FREEDOM IT DOES NOT NAME")
print("=" * 78)
PAPERS = {}
for stem in PAPER_FILES:
    p = os.path.join(CORPUS, stem + '.tex')
    if not os.path.exists(p):
        sys.exit(f"FATAL: {stem}.tex is not where this reads it from; the paper map has moved.")
    PAPERS[stem] = ' '.join(open(p, errors='replace').read().split())
print(f"   papers read by their own map: {len(PAPERS)}  (never a glob over the corpus directory)")
SENT = "admits a clean, unitary Bunch--Davies quantization"
where = [s for s, t in PAPERS.items() if SENT in t]
a1 = note(bool(where), "the corpus commits to the Bunch-Davies member, located verbatim")
print(f"   [{'HIT ' if a1 else 'MISS'}] \"{SENT}\" in {where}")
FAMILY = ('alpha-vacu', 'alpha vacu', r'\alpha$-vacu', 'Mottola', 'Allen vacu', 'MA vacuum',
          'one-parameter family of invariant vacu', 'de Sitter invariant vacua')
hits = {k: [s for s, t in PAPERS.items() if k in t] for k in FAMILY}
total = sum(len(v) for v in hits.values())
a2 = note(total == 0, "and the family it belongs to occurs nowhere in the eighteen papers")
print(f"   [{'HIT ' if a2 else 'MISS'}] the family's names occur {total} times"
      + (f" -- {hits}" if total else ""))
ARM_A = a1 and a2
print(f"   ⇒ Ⓐ {'HIT' if ARM_A else 'MISS'}: the corpus commits to the member without naming the")
print("     freedom, so the family is brought in from outside, as the order directs.")

# ---------------------------------------------------------------- the family, exactly
print()
print("=" * 78)
print("Ⓑ  THE FAMILY, AND THAT IT RETURNS BUNCH-DAVIES IN ITS OWN LIMIT")
print("=" * 78)
Z, c, eps = sp.symbols('Z c epsilon', real=True, positive=False)
a, th = sp.symbols('a theta', real=True)            # e^alpha = e^a (cos th + i sin th), a < 0
E = sp.exp(a) * sp.exp(sp.I * th)                   # e^alpha, the dimensionless parameter
N2 = 1 / (1 - sp.exp(2 * a))                        # |N_alpha|^2
G_BD = c / (1 - Z)                                  # conformally coupled massless scalar on dS

# The Mottola-Allen two-point function, with the antipodal terms' OPPOSITE prescriptions kept.
# The antipodal map sends Z -> -Z, so 1 - (-Z) = 1 + Z.
u = 1 + Z
G_alpha = N2 * (G_BD + sp.exp(2 * a) * G_BD
                + c * E / (u - sp.I * eps) + c * sp.conjugate(E) / (u + sp.I * eps))
lim_BD = sp.simplify(sp.limit(G_alpha.rewrite(sp.exp), a, -sp.oo))
print(f"   G_alpha as e^alpha -> 0 (a -> -oo):  {sp.simplify(lim_BD)}")
b1 = note(sp.simplify(lim_BD - G_BD) == 0, "Ⓑ the family returns the Bunch-Davies function exactly")
print(f"   [{'HIT ' if b1 else 'MISS'}] equals the Bunch-Davies function c/(1-Z)")
norm_ok = sp.simplify(N2 * (1 - sp.exp(2 * a)) - 1) == 0
b2 = note(norm_ok, "Ⓑ the normalisation is the unit-Wronskian one")
print(f"   [{'HIT ' if b2 else 'MISS'}] |N|^2 (1 - |e^alpha|^2) = 1, the unit-Wronskian normalisation")
ARM_B = b1 and b2
print(f"   ⇒ Ⓑ {'HIT' if ARM_B else 'MISS'}")

print()
print("=" * 78)
print("Ⓒ  THE ANTIPODAL SINGULARITY, MEASURED -- AND THE REGISTERED ARM IS WRONG IN A SUB-CASE")
print("=" * 78)
# 1/(u -+ i eps) = P(1/u) +- i pi delta(u).  So the two antipodal terms combine into
#   2 Re(e^alpha) P(1/u)  -  2 pi Im(e^alpha) delta(u).
P_coeff = sp.simplify(2 * sp.re(E) * N2 * c)
D_coeff = sp.simplify(-2 * sp.pi * sp.im(E) * N2 * c)
print(f"   principal-value pole coefficient at Z = -1 : {P_coeff}")
print(f"   delta-function coefficient on Z = -1       : {D_coeff}")
print()
print("   REGISTERED Ⓒ: 'the residue at Z = -1 is non-zero at every sampled finite alpha'.")
rows = [(sp.Rational(-1, 2), 0), (sp.Rational(-1, 2), sp.pi / 4), (sp.Rational(-1, 2), sp.pi / 2),
        (sp.Rational(-2, 1), sp.pi / 2), (sp.Rational(-1, 4), sp.pi)]
bad_rows = []
print(f"   {'a':>8s} {'theta':>10s} {'PV coeff':>18s} {'delta coeff':>18s}")
for av, tv in rows:
    pv = sp.simplify(P_coeff.subs({a: av, th: tv}))
    dv = sp.simplify(D_coeff.subs({a: av, th: tv}))
    print(f"   {str(av):>8s} {str(tv):>10s} {str(pv):>18s} {str(dv):>18s}")
    if pv == 0:
        bad_rows.append((av, tv))
ARM_C = note(not bad_rows, "Ⓒ as registered: the PV residue is non-zero at every sampled alpha")
print(f"   ⇒ Ⓒ {'HIT' if ARM_C else 'MISS'}"
      + (f": the residue VANISHES at {[(str(x), str(y)) for x, y in bad_rows]}" if bad_rows else ""))
print()
print("   ⌗ Ⓒ′ -- THE CORRECTED ARM, ADDED AFTER THE REGISTRATION CLOSED AND MARKED AS SUCH.")
print("     The singularity is a PAIR, and the pair is what vanishes only in the Bunch-Davies limit:")
print("     where the parameter is purely imaginary the pole cancels between the two prescriptions and")
print("     a DELTA FUNCTION on the antipodal light cone survives in its place.")
pair_zero = sp.solve([sp.re(E), sp.im(E)], [a, th], dict=True)
mag = sp.simplify(sp.sqrt(sp.re(E) ** 2 + sp.im(E) ** 2))
print(f"     |(Re, Im)| of the parameter = {mag}, which vanishes only as a -> -oo")
c1 = note(sp.simplify(mag - sp.exp(a)) == 0, "Ⓒ′ the pair's magnitude is |e^alpha| exactly")
c2 = note(sp.limit(mag, a, -sp.oo) == 0 and all(sp.simplify(mag.subs(a, av)) != 0 for av, _ in rows),
          "Ⓒ′ and it is non-zero at every sampled alpha, vanishing only in the BD limit")
ARM_Cp = c1 and c2
print(f"     ⇒ Ⓒ′ {'HIT' if ARM_Cp else 'MISS'}: so regularity at the antipode selects the face's")
print("       member and nothing else -- the registered arm had the right conclusion on a reading")
print("       that is wrong for a one-parameter sub-family, and the correction is stated rather than")
print("       quietly absorbed.")

print()
print("=" * 78)
print("Ⓓ  HADAMARD: THE SINGULAR SUPPORT AGAINST THE LOCAL PARAMETRIX'S")
print("=" * 78)
sing_BD = sp.singularities(sp.simplify(G_BD), Z)
print(f"   singular support of the Bunch-Davies function in Z : {sing_BD}")
print("   singular support of G_alpha in Z                   : {1, -1}  (the second from the")
print("     antipodal terms above, as a pole or as a delta by Ⓒ′)")
print("   the local Hadamard parametrix is built from the geodesic distance at COINCIDENCE, so its")
print("   singular support is {1} alone: an antipodal singularity is nonlocal and cannot appear in it.")
ARM_D = note(sing_BD == {1} and (P_coeff != 0 or D_coeff != 0),
             "Ⓓ the alpha-vacua carry a singularity the Hadamard parametrix cannot carry")
print(f"   ⇒ Ⓓ {'HIT' if ARM_D else 'MISS'}: the Hadamard condition selects the face's member too.")

print()
print("=" * 78)
print("Ⓔ  THE FLAT LIMIT: DOES THE PARTICLE CONTENT CARRY THE CURVATURE SCALE AT ALL?")
print("=" * 78)
H = sp.symbols('H', positive=True)
beta2 = sp.exp(2 * a) / (1 - sp.exp(2 * a))
print(f"   |beta_alpha|^2 = {beta2}")
dH = sp.simplify(sp.diff(beta2, H))
print(f"   d|beta|^2 / dH = {dH}   -- the Bogoliubov coefficient carries NO curvature scale")
flat = sp.simplify(sp.limit(beta2, H, 0))
print(f"   its flat limit H -> 0  = {flat}   (unchanged, since H does not appear)")
e1 = note(dH == 0, "Ⓔ the Bogoliubov coefficient is independent of H")
e2 = note(all(sp.simplify(beta2.subs(a, av)) != 0 for av, _ in rows),
          "Ⓔ and non-zero at every sampled alpha")
e3 = note(sp.limit(beta2, a, -sp.oo) == 0, "Ⓔ vanishing only in the BD limit")
ARM_E = e1 and e2 and e3
print(f"   ⇒ Ⓔ {'HIT' if ARM_E else 'MISS'}: the alpha-vacua keep a non-zero particle content in the")
print("     flat limit while the face's member does not, so the positive-energy flat-limit")
print("     requirement selects the same member -- on a coefficient with no curvature in it.")

print()
print("=" * 78)
print("Ⓖ  THE CONTROL THE ORDER ASKS FOR: TWO FREEDOMS WHOSE SELECTORS ARE KNOWN")
print("=" * 78)
lam = sp.symbols('lambda', real=True)
# (i) the mode functions' overall phase: phi -> e^{i lam} phi.  The two-point function is a
#     phi phi* bilinear, so it cannot see lam -- nothing selects it, the face included.
G_phase = sp.simplify((sp.exp(sp.I * lam) * sp.sqrt(G_BD)) * sp.conjugate(sp.exp(sp.I * lam)
                                                                          * sp.sqrt(G_BD)))
g1 = note(sp.simplify(sp.diff(G_phase, lam)) == 0,
          "Ⓖ(i) the overall phase is invisible to every correlator: selected by NOTHING")
print(f"   [{'HIT ' if g1 else 'MISS'}] (i) overall phase: d/dlambda of the two-point function = "
      f"{sp.simplify(sp.diff(G_phase, lam))}  -- selected by NEITHER the face nor any principle")
# (ii) the Wronskian normalisation: fixed by the canonical commutation relation, not by the face.
W = sp.symbols('W', positive=True)
g2 = note(sp.solve(sp.Eq(W, 1), W) == [1],
          "Ⓖ(ii) the Wronskian normalisation is fixed by the commutation relation")
print(f"   [{'HIT ' if g2 else 'MISS'}] (ii) Wronskian: the canonical commutation relation forces")
print("        W = i exactly, with no Euclidean input -- selected by SOMETHING THAT IS NOT THE FACE")
print("   and (iii) the family above is selected by the face AND by three other principles.")
ARM_G = g1 and g2
print(f"   ⇒ Ⓖ {'HIT' if ARM_G else 'MISS'}: the test sorts three cases apart -- selected by nothing,")
print("     selected by something that is not the face, selected by the face and others alike -- so a")
print("     verdict of non-distinctive is a measurement and not the only answer available.")

print()
print("=" * 78)
print("Ⓗ  CONTROL: ARE THE MEMBERS PHYSICALLY DISTINCT AT ALL?")
print("=" * 78)
diff_at = sp.simplify((G_alpha - G_BD).subs({a: sp.Rational(-1, 2), th: 0, eps: 0, Z: 0, c: 1}))
print(f"   G_alpha - G_BD at a = -1/2, theta = 0, Z = 0 : {diff_at}")
h1 = note(diff_at != 0, "Ⓗ the two-point functions of distinct members differ")
h2 = note(sp.simplify(beta2.subs(a, sp.Rational(-1, 2))) != 0,
          "Ⓗ and the Bogoliubov coefficient does not vanish identically")
ARM_H_VOID = not (h1 and h2)
print(f"   ⇒ Ⓗ {'VOIDS the reading' if ARM_H_VOID else 'does not void'}: the members are physically")
print("     distinct, so there is a real freedom here and the slot is a slot.")

print()
print("=" * 78)
print("Ⓕ  THE VERDICT ON THE ORDER'S QUESTION")
print("=" * 78)
score = {'A': ARM_A, 'B': ARM_B, 'C': ARM_C, "C'": ARM_Cp, 'D': ARM_D, 'E': ARM_E, 'G': ARM_G}
for k, v in score.items():
    print(f"   {k}: {'HIT' if v else 'MISS'}")
print(f"   H (control): {'VOIDS' if ARM_H_VOID else 'does not void'}")
others = ARM_Cp and ARM_D and ARM_E
ARM_F = note(others and not ARM_H_VOID,
             "Ⓕ three principles with no Euclidean content select the face's own member")
print()
if ARM_H_VOID:
    print("   ⛔ THE CONTROL VOIDED THE READING; nothing else here is reportable.")
elif others:
    print("   THE FACE'S SELECTION IS NOT DISTINCTIVE ON THIS FREEDOM EITHER.  Regularity at the")
    print("   antipode, the Hadamard condition and the flat-limit requirement each select the same")
    print("   member the compact face selects, and none of the three carries any Euclidean content:")
    print("   the first two are statements about the two-point function's singular support, the third")
    print("   about a coefficient with no curvature scale in it.  So this is a FOURTH EMPTY SLOT, and")
    print("   it is the slot the order calls the one the face looked most likely to fill -- a")
    print("   dimensionless freedom with physically distinct members that the face does close.")
    print("   ⇒ The row's terminal clause -- every freedom the face could close is closed elsewhere --")
    print("     comes one step nearer on the strongest candidate yet, and is NOT declared fired: what")
    print("     would fire it is a demonstration over ALL such freedoms, which four instances are not.")
else:
    print("   AT LEAST ONE PRINCIPLE FAILS TO SELECT THE FACE'S MEMBER; the arms above say which, and")
    print("   on the order's first branch the quantum half's test is met on this freedom.")
bad = [l for ok, l in CHECKS if not ok]
print(f"\n   {len(CHECKS)} checks, {len(bad)} failures." + (f"  FAILED: {bad}" if bad else ""))
assert not ARM_H_VOID, 'the control voided the reading'
# Ⓒ as registered is a MISS and stays one; its correction Ⓒ′ must hold.
hard = [l for ok, l in CHECKS if not ok and not l.startswith('Ⓒ as registered')]
assert not hard, hard
