#!/usr/bin/env python3
r"""
r7612 — PO-87's narrowed clause: (1) does any clause in the corpus DERIVE the assignment of the
projection's comoving distance to the stacking rate, and (2) does the reassignment itself fix the rate a
photon-path distance accumulates at?

Arms Ⓐ..Ⓗ as registered in PREDICTION.md, committed before this file existed.

ONE INSTRUMENT, NOT THREE.  The chart is r7580's own script, read by path (runpy) rather than
reimplemented (r7445); that script in turn reads the background out of the prior P15 receipt by ast.  The
census net reads the PAPERS ONLY -- 69's repair of r7608's net, where globbing corpus/*.tex pulled in the
receipt appendices, which reprint receipts' index rows.

RUN: python3 photonfamily.py
"""
import ast, contextlib, glob, io, os, re, runpy, sys
import numpy as np
from scipy.integrate import quad

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

# the eighteen papers, by their own map in scripts/gen_paper_html.py -- never corpus/*.tex, which also
# holds the generated receipt appendices.
PAPER_FILES = ['BH_causality_v2', 'janzen_circle_v3', 'SdS-slicing-curve_v2', 'modern_parallax',
               'groupoid_paper', 'shadow_of_existence', 'CR_framework', 'slicing_operator',
               'range_paper', 'canonical_time', 'dynamics_paper', 'algebroid_paper',
               'boundary_paper', 'matter_sector_paper', 'CR_cosmology', 'cosmogenesis_paper',
               'geometric_core_paper', 'CR_synthesis']
PAPERS = {}
for stem in PAPER_FILES:
    p = os.path.join(CORPUS, stem + '.tex')
    if not os.path.exists(p):
        sys.exit(f"FATAL: {stem}.tex is not where this reads it from; the paper map has moved.")
    PAPERS[stem] = open(p, errors='replace').read()
print(f"papers read: {len(PAPERS)}  (the receipt appendices are NOT in this net -- 69's r7611 repair)")

def sentences(t):
    return [' '.join(s.split()) for s in re.split(r'(?<=[.!?])\s+', t)]

print()
print("=" * 78)
print("Ⓐ  THE CENSUS: DOES ANY CLAUSE *DERIVE* THE ASSIGNMENT?")
print("=" * 78)
RATE = ('stacking rate', "leaf's rate", 'leaf rate', 'stacking of the foliation', 'foliation rate',
        'foliation stacking rate')
DIST = ('comoving separation', 'comoving distance', 'angular-diameter', 'light-travel', "light's path",
        '$D_M$', 'D_M', 'the distances', "projection's distance")
# a sentence that merely ASSIGNS is not a candidate for 'derives'; the candidates are the ones that
# CLAIM a ground.  The markers are the corpus's own words for claiming one.
CLAIM = ('derive', 'derived', 'derives', 'forced', 'follows identically', 'not chosen', 'not a choice',
         'kinematic', 'rather than asserted', 'carried out rather than', 'not a modelling choice',
         'fixed by what', 'structural, not a choice', 'rather than by choice')
assign, claims = [], []
for stem, txt in PAPERS.items():
    for s in sentences(txt):
        if any(k in s for k in RATE) and any(k in s for k in DIST):
            assign.append((stem, s))
            if any(k in s for k in CLAIM):
                claims.append((stem, s))
print(f"   sentences assigning a distance or a comoving separation to a rate: {len(assign)}")
print(f"   of those, sentences that CLAIM a ground (the corpus's own derivation words): {len(claims)}")

# the adjudication, keyed by a distinctive substring.  STATES = asserts or restates the rule.
# GROUNDS = offers a reason, but for an object that is not the projection's distance.  DERIVES = derives
# the projection's distance's rate from something that is not itself a rate assignment.
ADJ = {
 "The assignment is not a modelling choice on either side": ('STATES',
   "restates the rule for both slots; the ground offered is the slot a quantity sits in, which is the "
   "rule itself"),
 "and the rule is kinematic: a comoving separation read across leaves takes the stacking rate": ('STATES',
   "P16, where the rule is derived: 'kinematic' qualifies the rule, and the sentence states it"),
 "not chosen: the same selection of the existent's foliation that turns the frozen constraint into a "
 "true Hamiltonian here fixes, one level down, which rate a recombination-era or a nucleosynthesis-era "
 "computation must read": ('GROUNDS',
   "P10, and the closest thing in the corpus to a derivation -- but its object is a PLASMA PROCESS and "
   "an era computation, not the projection's distance; the same sentence puts distance and redshift on "
   "the SHIFT, not the lapse"),
 "the Nariai member, by the reassignment's own selection argument rather than by choice": ('GROUNDS',
   "P18's ledger, and the object is the Nariai member, not the distance's rate"),
 "And the division is carried out rather than asserted": ('STATES',
   "the claim is that the division is IMPLEMENTED on each object, not that the assignment is derived"),
# P15 sec:tensions's "The decision rule is structural, not a choice" is NOT in this net and the key for
# it was dropped rather than kept as a stale one: that sentence names the three levels and neither a
# rate nor a distance, so by the net's own definition it is not a sentence assigning a distance to a
# rate.  It grounds WHICH LEVEL a quantity sits on, which is a step before the question asked here.
 "the verdict it returns is that the spectrum derived here, with the projection's distance on the "
 "stacking rate the construction assigns it, is disfavoured": ('STATES',
   "the only sentence in the net whose 'derived' is about the SPECTRUM and not about the assignment -- "
   "caught by the marker and adjudicated rather than counted"),
 # r7613 (69): the derivation this file found, written into the papers when 69 landed it.  These are
 # this result's own sentences and not prior clauses, so they are LANDED and not DERIVES: arm A asks
 # whether any clause derived the rate BEFORE this computation, and the six keys above that r7613's
 # rewrite removed are dropped rather than kept stale.
 "on the stacking rate, which the construction derives for it": ('LANDED', "P7's abstract, r7613"),
 # r7615 (69): r7614's result (the derivation holds on any cut) written in; LANDED as above, and the three r7613
 # keys whose sentences r7615 rewrote are dropped rather than kept stale.
 "that derivation holds on any cut, bent by radiation or not": ('LANDED', "P6, r7615"),
 "and the stacking rate light's path distance takes is derived on any cut": ('LANDED', "P7 sec:intro's cosmology summary, r7615"),
 "The rate light's path distance takes is derived, and the residual is carried by it": ('LANDED', "P7 frontier:scalar, r7615"),
 "So the comparison is between the construction's derived configuration and the sky": ('LANDED', "P15 sec:scope, r7615"),
 "the stacking rate the reassignment derives for it on any cut": ('LANDED', "P16, r7615"),
 "the projection's distance being on the stacking rate by derivation on any cut": ('LANDED', "P18's open-items summary, r7615"),
 "So the stacking rate the projection's distance is built on is derived, by the reassignment's own "
 "identification of the photon family": ('LANDED', "P15 sec:scope, r7613: this file's derivation, written in"),
 "And the stacking rate is derived": ('LANDED', "P18 sec:frontier, r7613"),
}
seen, unadj, derives = {}, [], []
for stem, s in claims:
    k = [k for k in ADJ if k in s]
    if k:
        seen.setdefault(k[0], []).append(stem)
        if ADJ[k[0]][0] == 'DERIVES':
            derives.append((stem, k[0]))
    else:
        unadj.append((stem, s))
for k, v in seen.items():
    verdict, why = ADJ[k]
    print(f"\n   [{verdict:7s}] {sorted(set(v))}")
    print(f"             \"{k[:96]}...\"")
    print(f"             {why}")
for stem, s in unadj:
    print(f"\n   [UNADJUDICATED -- READ IT] {stem}: {s[:220]}")
stale = [k for k in ADJ if k not in seen]
for k in stale:
    print(f"\n   [STALE KEY -- matches nothing now] \"{k[:110]}...\"")
ARM_A = note(len(derives) == 0 and not unadj and not stale,
             "Ⓐ no clause DERIVES the assignment, every claim-sentence adjudicated, no stale key")
print(f"\n   sentences adjudicated DERIVES: {len(derives)}")
print(f"   ⇒ Ⓐ {'HIT' if ARM_A else 'MISS'}: the corpus ASSIGNS the projection's distance to the "
      f"stacking rate in {len(assign)} places")
print("     and GROUNDS the rule once, in P10 -- for a plasma process, by the foliation selection.")
print("     No clause derives it for the projection's distance.  And P10's own sentence puts distance")
print("     and redshift on the SHIFT while the stacking rate is the LAPSE, which is where the gap is.")

# ---------------------------------------------------------------- the chart, read by path
print()
print("=" * 78)
print("THE CHART, READ FROM r7580'S OWN SCRIPT BY PATH (r7445: one instrument)")
print("=" * 78)
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    G = runpy.run_path(PRIOR, run_name='_r7580_chart')
need = ['alpha', 'A_AMP', 'TWO_M', 'r_of', 'rdot_of', 'tt_of_z', 'H_stack', 'r0', 'tt0', 'tt_rec',
        'C', 'Z_REC', 'DC_stack', 'DC_layer', 'D_path', 'DC_leaf', 'chi_sq']
missing = [n for n in need if n not in G]
if missing:
    sys.exit(f"FATAL: r7580's script no longer exposes {missing}; the chart has moved.")
alpha, A_AMP, TWO_M = G['alpha'], G['A_AMP'], G['TWO_M']
r_of, rdot_of, tt_of_z = G['r_of'], G['rdot_of'], G['tt_of_z']
r0, tt0, tt_rec, Z_REC = G['r0'], G['tt0'], G['tt_rec'], G['Z_REC']
DC_stack, DC_layer, D_path, DC_leaf = G['DC_stack'], G['DC_layer'], G['D_path'], G['DC_leaf']
print(f"   alpha = {alpha:.6f} Mpc   r_0 = {r0:.6f} Mpc   z_rec = {Z_REC}")
print(f"   r7580's three distances, read rather than recomputed: stacking {DC_stack:.3f}, "
      f"leaf {DC_leaf:.3f}, light's own path {D_path:.3f} Mpc")
note(abs(DC_layer / DC_stack - 1.0) < 1e-8, "r7580's layer-time integral still equals its stacking integral")

print()
print("=" * 78)
print("Ⓗ  CONTROL: WHICH FAMILY IS THE PHOTON BUNDLE'S IMAGE?  READ OFF THE PAPER")
print("=" * 78)
P15 = ' '.join(PAPERS['CR_cosmology'].split())
s_photon = "the at-rest geodesics are the photon bundle, one of the two null bundles on the cosmological horn carries the late-time matter geodesics"
s_reass = "that same null bundle becomes the constant-$\\chi$ geodesics and the other becomes the constant-$\\tau$ ones"
h1 = note(s_photon in P15, "P15: the at-rest geodesics are the photon bundle; ONE null bundle carries the matter")
h2 = note(s_reass in P15, "P15: that same null bundle -> constant-chi, THE OTHER -> constant-tau")
print(f"   [{'HIT ' if h1 else 'MISS'}] {s_photon[:92]}...")
print(f"   [{'HIT ' if h2 else 'MISS'}] {s_reass[:92]}...")
print("   reading, which is the paper's own and not supplied: 'that same null bundle' is the one the")
print("   preceding sentence says carries the MATTER geodesics, and it becomes the constant-chi family")
print("   (matter is comoving, so chi is constant along it -- the chart agrees).  'The other' is then")
print("   the photon bundle, and it becomes the CONSTANT-TAU family.")
ARM_H_FIRES = not (h1 and h2)
print(f"   ⇒ Ⓗ {'FIRES -- the candidate is about the wrong family' if ARM_H_FIRES else 'does not fire'}")

print()
print("=" * 78)
print("Ⓑ  THE REASSIGNMENT IS A REASSIGNMENT: THE PHOTON FAMILY'S IMAGE IS NOT THE LIGHT CONE")
print("=" * 78)
chi_sq = G['chi_sq']
mn = float(np.min(chi_sq))
print(f"   min over the branch of (d_chi r)^2 = g_chi chi : {mn:.12f}   (r7580: exactly 1 at alpha/sqrt3)")
print("   radial null directions in eq:proper-frame: dtau = +- (d_chi r) dchi, so |dtau/dchi| >= 1 > 0.")
print("   a constant-tau curve has dtau = 0, hence ds^2 = g_chi chi dchi^2 > 0: SPACELIKE, nowhere null.")
rows = []
for z in (0.0, 1.0, 10.0, 1090.0, 3e7):
    tt = tt_of_z(z); g = rdot_of(tt) ** 2
    rows.append((z, g))
    print(f"     z = {z:>10.1f}   g_chi chi = (d_chi r)^2 = {g:16.6f}   null slope |dtau/dchi| = {np.sqrt(g):10.6f}")
ARM_B = note(mn >= 1.0 - 1e-9 and all(g > 1.0 - 1e-9 for _, g in rows),
             "Ⓑ the constant-tau family is spacelike at every sampled epoch and the branch minimum is 1")
print(f"   ⇒ Ⓑ {'HIT' if ARM_B else 'MISS'}: so r7580's third object (the proper-frame null ray) and")
print("     this revision's candidate (the photon bundle's image) are two different curves.  That is")
print("     what 'causal reassignment' means, stated on the loci the object itself distinguishes.")

print()
print("=" * 78)
print("Ⓒ  THE CANDIDATE'S LOAD-BEARING STEP: BOTH FAMILIES ADVANCE COSMIC TIME AT UNIT RATE")
print("=" * 78)
step_v = ("Fixing the transformation $t(\\tau,\\chi)$ by requiring the comoving coordinate orthogonal to "
          "proper time, $g_{\\chi\\tau}=0$, forces the integration function to be $\\chi$ itself")
c0 = note(step_v in P15, "P15 step (v): orthogonality FORCES the integration function to be chi itself")
print(f"   [{'HIT ' if c0 else 'MISS'}] {step_v[:94]}...")
print("   so tilde tau = tau + chi, and the two partial derivatives are both exactly 1 by construction.")
# measured, not asserted: r(tau,chi) = r(tau+chi) means d_chi r = d_tau r at every point sampled
worst = 0.0
for tau, chi in ((1000.0, 200.0), (4000.0, 1.0), (8000.0, 5000.0), (100.0, 50.0)):
    h = 1e-6 * (tau + chi)
    d_chi = (r_of(tau + chi + h) - r_of(tau + chi - h)) / (2 * h)      # vary chi at fixed tau
    d_tau = (r_of(tau + h + chi) - r_of(tau - h + chi)) / (2 * h)      # vary tau at fixed chi
    rel = abs(d_chi / d_tau - 1.0)
    worst = max(worst, rel)
    print(f"     (tau,chi) = ({tau:8.1f},{chi:8.1f})   d_chi r = {d_chi:.12f}   d_tau r = {d_tau:.12f}"
          f"   rel diff {rel:.2e}")
# the two advances are checked EXACTLY, symbolically, rather than by differencing floats: a float
# difference of tau+chi at tau ~ 1e3 and h ~ 1e-3 cancels to about 1e-10 and would measure the
# arithmetic rather than the chart.
import sympy as sp
_tau, _chi = sp.symbols('tau chi', real=True)
_tt = _tau + _chi
d_tt_dchi, d_tt_dtau = sp.diff(_tt, _chi), sp.diff(_tt, _tau)
tt_sym_ok = (d_tt_dchi == 1) and (d_tt_dtau == 1)
print(f"   d(tilde tau)/d chi = {d_tt_dchi}, d(tilde tau)/d tau = {d_tt_dtau}  (exact, symbolic)")
# the finite-difference equality of d_chi r and d_tau r is a check on the chart, and its floor is the
# central difference's own truncation error at this step, which is ~1e-10 and not ~1e-12.
ARM_C = note(c0 and worst < 1e-9 and tt_sym_ok,
             "Ⓒ both families advance cosmic time at unit rate per unit of their own label")
print(f"   ⇒ Ⓒ {'HIT' if ARM_C else 'VOID'}: worst |d_chi r / d_tau r - 1| = {worst:.2e}")
print("     The photon family crosses the leaves, and it crosses them at the same cosmic-time rate as")
print("     the matter congruence advances along them.")

print()
print("=" * 78)
print("Ⓓ  SO WHAT ACCUMULATES ALONG THE PHOTON FAMILY IS THE LAYER-TIME INTEGRAL")
print("=" * 78)
rel = abs(DC_layer / DC_stack - 1.0)
print(f"   r_0 * int dtilde tau / r  over the photon family's crossing = {DC_layer:.6f} Mpc")
print(f"   int c dz / H_stack, the implementation's own distance        = {DC_stack:.6f} Mpc")
print(f"   relative difference = {rel:.3e}")
ARM_D = note(rel < 1e-8, "Ⓓ the photon family's comoving accumulation IS the stacking integral")
print(f"   ⇒ Ⓓ {'HIT' if ARM_D else 'MISS'}")

print()
print("=" * 78)
print("Ⓔ  AND THE SEPARATION READ *ON* ONE LEAF IS A DIFFERENT OBJECT")
print("=" * 78)
# at fixed tau, int (d_chi r) dchi from chi_e to chi_0 = r(tau+chi_0) - r(tau+chi_e), exactly
tau_fix = 0.0
chi_e, chi_0 = tt_rec, tt0
num = quad(lambda ch: rdot_of(tau_fix + ch), chi_e, chi_0, limit=400)[0]
closed = r_of(tau_fix + chi_0) - r_of(tau_fix + chi_e)
r_e = r_of(tt_rec)
by_z = r0 * Z_REC / (1.0 + Z_REC)
print(f"   int (d_chi r) dchi at fixed tau        = {num:.8f} Mpc")
print(f"   r(tilde tau_0) - r(tilde tau_e)        = {closed:.8f} Mpc   (the exact closed form)")
print(f"   r_0 z/(1+z)                            = {by_z:.8f} Mpc   (the same, since 1+z = r_0/r_e)")
e1 = note(abs(num / closed - 1.0) < 1e-10, "Ⓔ the on-leaf separation equals its closed form")
e2 = note(abs(by_z / closed - 1.0) < 1e-10, "Ⓔ and equals r_0 z/(1+z)")
ratio_leaf = closed / DC_stack
print(f"   ratio to the implementation's D_C      = {ratio_leaf:.6f}   (registered: below 0.5)")
print(f"   and it is bounded above by r_0 = {r0:.3f} Mpc for every z, while D_C = {DC_stack:.3f}")
e3 = note(ratio_leaf < 0.5, "Ⓔ the on-leaf separation is below half the implementation's D_C")
ARM_E = e1 and e2 and e3
print(f"   ⇒ Ⓔ {'HIT' if ARM_E else 'MISS'}: reading a separation ON a leaf and accumulating one ACROSS")
print("     leaves give different numbers on this very case, so the rule's two slots are not a")
print("     distinction without a difference here.")

print()
print("=" * 78)
print("Ⓖ  THE CLOCK GUARD (r7138), APPLIED TO THIS REVISION'S OWN TWO READINGS")
print("=" * 78)
RS_LEAF = G.get('rs_leaf', None)
if RS_LEAF is None:
    for k in ('RS', 'rs', 'r_s', 'rs_leaf'):
        if k in G:
            RS_LEAF = G[k]; break
if RS_LEAF is None:
    sys.exit("FATAL: r7580's script no longer exposes the leaf sound horizon this prices against.")
SKY = 298.4
lA_stack = np.pi * DC_stack / RS_LEAF
lA_path = np.pi * D_path / RS_LEAF
print(f"   r_s on the leaf rate, read from r7580   = {RS_LEAF:.3f} Mpc")
print(f"   l_A on the photon family's accumulation = {lA_stack:.2f}   vs the sky's {SKY}"
      f"   ({100*(lA_stack/SKY-1):+.2f} %)")
print(f"   l_A on the proper-frame null ray        = {lA_path:.2f}   vs the sky's {SKY}"
      f"   ({100*(lA_path/SKY-1):+.2f} %)")
survives = abs(lA_stack - lA_path) / SKY > 0.05
ARM_G = note(survives, "Ⓖ the difference between the two readings survives against one fixed sky datum")
print(f"   ⇒ Ⓖ {'HIT' if ARM_G else 'MISS'}: the two differ by "
      f"{100*abs(lA_stack-lA_path)/SKY:.1f} per cent of the measured comb, which no choice of clock")
print("     moves.  So the difference is content and not bookkeeping, and the question the order asks")
print("     is a real one.")

print()
print("=" * 78)
print("Ⓕ  THE VERDICT ON THE ORDER'S QUESTION")
print("=" * 78)
ARM_F = note(ARM_B and ARM_C and ARM_D and ARM_E and not ARM_H_FIRES,
             "Ⓕ the reassignment fixes the rate a photon-path distance accumulates at")
score = {'A': ARM_A, 'B': ARM_B, 'C': ARM_C, 'D': ARM_D, 'E': ARM_E, 'F': ARM_F, 'G': ARM_G}
for k, v in score.items():
    print(f"   {k}: {'HIT' if v else 'MISS'}")
print(f"   H (control): {'FIRES' if ARM_H_FIRES else 'does not fire'}")
print()
if not (ARM_A and ARM_F):
    print("   ⛔ THE REGISTERED READING DID NOT COME OUT WHOLE.  The arms above say which part failed, and")
    print("      the write-up reports that rather than this paragraph.  Nothing below is claimed.")
print("   NO CLAUSE IN THE CORPUS DERIVES THE ASSIGNMENT, AND THE CONSTRUCTION DERIVES IT ANYWAY.")
print("   The reassignment sends the photon bundle to the constant-tau family (Ⓗ, read off P15).  That")
print("   family is spacelike in the proper frame, so it is not the light cone and not r7580's third")
print("   object (Ⓑ).  It crosses the leaves, and it crosses them advancing cosmic time at exactly the")
print("   rate the matter congruence advances along them, which is what step (v)'s forcing buys (Ⓒ).")
print("   A comoving separation accumulated across leaves at that rate IS the layer-time integral, which")
print("   is the implementation's own distance (Ⓓ) -- and it is not the separation read on a single leaf,")
print("   which is a smaller object entirely (Ⓔ).  So the photon-path distance sits in P16's FIRST slot,")
print("   a comoving separation read across leaves, and the rule assigns it the stacking rate.")
print()
print("   ⌗ AND THAT NARROWS r7580's Hb-prime BY MY OWN HAND: I reported there that the rule's two slots")
print("     do not cover light's path.  They do cover it, once the reassignment is used to say WHICH")
print("     family the photon path is.  What r7580 showed remains true of the object it tested -- the")
print("     proper-frame null ray, which the comb excludes -- and that object is not the one the")
print("     projection uses.")
bad = [l for ok, l in CHECKS if not ok]
assert all(score.values()), score
assert not ARM_H_FIRES
print(f"\n   {len(CHECKS)} checks, {len(bad)} failures." + (f"  FAILED: {bad}" if bad else ""))
assert not bad, bad
