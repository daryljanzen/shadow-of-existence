#!/usr/bin/env python3
r"""
r7608 — PO-94's QUANTUM HALF: WHETHER IT CAN CARRY A DISCRIMINATOR AT ALL, AND WHETHER IT IS THE
GAUGE HALF'S TEST.

Arms Ⓐ..Ⓗ as registered in PREDICTION.md (committed before this file existed).  Every sentence the
argument uses is LOCATED in the papers by containment, never paraphrased and never pinned; the one
predicate that is measured rather than read is arm Ⓔ, and no existing receipt implements it (checked:
the thresholds are asserted in P10's text and in P10_gamma_is_one_quarter_and_is_the_maximum, which
states in its own words that it does not verify the index or the Friedrichs selection).

RUN: python3 discriminator.py
"""
import glob, os, re, sys
import numpy as np
from scipy.special import jv, gamma as G
from scipy.optimize import brentq
from scipy.integrate import quad

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
CORPUS = os.path.join(ROOT, 'corpus')
RECEIPTS = os.path.join(ROOT, 'receipts')

def load(name):
    p = os.path.join(CORPUS, name)
    if not os.path.exists(p):
        sys.exit(f"FATAL: {name} is not where this reads it from; the paper map has moved.")
    return ' '.join(open(p, errors='replace').read().split())

P13 = load('boundary_paper.tex')
P10 = load('canonical_time.tex')

CHECKS = []          # every check this file makes, so the count at the end is counted and not typed

def note(ok, label):
    CHECKS.append((bool(ok), label))
    return bool(ok)

def locate(hay, needle, label):
    ok = note(needle in hay, label)
    print(f"   [{'HIT ' if ok else 'MISS'}] {label}")
    if not ok:
        print(f"          NOT FOUND: {needle[:90]}...")
    return ok

print("=" * 78)
print("Ⓐ  THE GAUGE HALF'S TEST HAS A DEFINITE LOGICAL FORM")
print("=" * 78)
A1 = locate(P13, "a rhyme and an identification are told apart by \\emph{dynamics}",
            "P13: told apart by DYNAMICS")
A2 = locate(P13, "an actual gauge sector carries a field strength and a coupling",
            "P13: an actual gauge sector carries A FIELD STRENGTH AND A COUPLING")
A3 = locate(P13, "the bundle at the branch point is flat",
            "P13: and the blocker -- THE BUNDLE AT THE BRANCH POINT IS FLAT")
ARM_A = A1 and A2 and A3
print(f"   ⇒ Ⓐ {'HIT' if ARM_A else 'MISS'}: the gauge half's test asks the face to carry the")
print("     sector's own STRUCTURE -- a connection with curvature -- and a coupling.")

print()
print("=" * 78)
print("Ⓑ  THE CORPUS PLACES THE QUANTUM'S STRUCTURE ON THE LORENTZIAN FORM AND ONLY ITS SCALE")
print("   ON THE OTHER")
print("=" * 78)
B1 = locate(P13, "The framework's \\emph{structure}---the constraint algebra, unitarity, the "
                 "discreteness of the graviton tower, the problem of time and its cure---is "
                 "Lorentzian, the temporal real form's own",
            "P13: the framework's STRUCTURE is Lorentzian")
B2 = locate(P13, "Only the framework's \\emph{scale}, the quantum of action $\\hbar$, is set on the "
                 "Euclidean face",
            "P13: only the framework's SCALE is set on the Euclidean face")
B3 = locate(P13, "the quantum is not a third thing", "P13: the quantum is not a third thing")
ARM_B = B1 and B2 and B3
print(f"   ⇒ Ⓑ {'HIT' if ARM_B else 'MISS'}")

print()
print("=" * 78)
print("Ⓒ / Ⓗ  THE NET: DOES ANY PAPER PLACE A QUANTUM *STRUCTURE* ON THE COMPACT FACE?")
print("=" * 78)
FACE = ('compact face', 'Euclidean face', 'Euclidean real form', 'global-Wick',
        '$S^{5}$', '$S^5$', '\\SO(6)', 'so(6)', '\\so(6)')
QUANT = ('commutator', 'commutation', 'uncertainty', 'non-commut', 'noncommut',
         'operator algebra', 'deformation', 'Hilbert space', 'quantization',
         'quantisation', 'quantum of action', 'operator-valued')
# the adjudication, keyed by a distinctive substring of each candidate.  SCALE = the sentence places
# the quantum's SCALE (hbar, the quantum of action) on the face.  SELECTION = it claims the face
# closes a freedom (which is what arm Ⓔ scores, not a structure placement).  STRUCTURE = it places a
# commutator / Hilbert space / operator algebra / deformation on the face -- which would fire Ⓗ.
ADJ = {
    "borne on the substrate's conjugate (Euclidean) real form": 'SCALE',
    "they carry the two sides of the divides the corpus keeps apart": 'SCALE',
    "So the quantum of action and the colour symmetry share the one Euclidean real form": 'SCALE',
    "closes the free sector's lone quantization ambiguity without a free parameter": 'SELECTION',
    "that places it, together with the quantum of action, on the substrate's Euclidean real form": 'SCALE',
    "So the thermal and the gauge registers are not two entries in the ledger": 'SCALE',
}
found, unmatched = {}, []
for f in sorted(glob.glob(os.path.join(CORPUS, '*.tex'))):
    txt = open(f, errors='replace').read()
    for s in re.split(r'(?<=[.!?])\s+', txt):
        if any(k in s for k in FACE) and any(k in s for k in QUANT):
            s1 = ' '.join(s.split())
            hit = [k for k in ADJ if k in s1]
            if hit:
                found.setdefault(hit[0], []).append(os.path.basename(f))
            else:
                unmatched.append((os.path.basename(f), s1[:200]))
print(f"   candidates the net returns over all {len(glob.glob(os.path.join(CORPUS,'*.tex')))} corpus "
      f"files: {sum(len(v) for v in found.values()) + len(unmatched)}")
for k, v in found.items():
    print(f"     [{ADJ[k]:9s}] {', '.join(sorted(set(v)))}: \"{k[:78]}\"")
for f, s in unmatched:
    print(f"     [UNADJUDICATED -- READ IT] {f}: {s}")
n_struct = sum(1 for k in found if ADJ[k] == 'STRUCTURE')
ARM_C = (ARM_A and ARM_B and n_struct == 0 and not unmatched and len(found) == len(ADJ))
ARM_H_FIRES = n_struct > 0
print(f"   sentences placing a quantum STRUCTURE on the face: {n_struct}")
print(f"   ⇒ Ⓒ {'HIT' if ARM_C else 'MISS'}   Ⓗ {'FIRES' if ARM_H_FIRES else 'does not fire'}")
print("     The two halves make claims of DIFFERENT STRENGTH: gauge asks the face to carry the")
print("     sector's own structure; the quantum claim is only that the face carries its scale.")
print("     A test for a structure-claim cannot score a scale-claim.")

print()
print("=" * 78)
print("Ⓓ  THE VALUE SLOT: WHAT THE THERMAL RELATION CONSTRAINS ON THE LEDGER")
print("=" * 78)
D0 = locate(P10, "the place the quantum constant enters is not the place a value is fixed",
            "P10: the place the quantum constant enters is NOT the place a value is fixed")
D1 = locate(P10, "adding one equation and one unknown, whose net constraint on what the ledger "
                 "already holds is zero",
            "P10: one equation and one unknown, NET CONSTRAINT ZERO")
import sympy as sp
hbar, alpha, kB, T = sp.symbols('hbar alpha k_B T', positive=True)
rel = sp.Eq(T, hbar / (2 * sp.pi * alpha * kB))           # Gibbons--Hawking
sol = sp.solve(rel, T)
new_unknowns = {T} - {hbar, alpha, kB}
# the projection of the relation's solution set onto the ledger coordinates (hbar, alpha, k_B):
# for EVERY positive assignment there is exactly one T, so the projection is onto and the relation
# imposes nothing on the ledger.  Checked rather than asserted, on random positive assignments.
rng = np.random.default_rng(7608)
onto = True
for _ in range(200):
    v = {hbar: float(rng.uniform(0.1, 9)), alpha: float(rng.uniform(0.1, 9)),
         kB: float(rng.uniform(0.1, 9))}
    cand = [s.subs(v) for s in sol]
    onto &= (len(cand) == 1 and float(cand[0]) > 0)
note(onto, "the thermal relation solves uniquely for its own new quantity on every ledger point")
note(len(new_unknowns) == 1, "the thermal relation introduces exactly one new unknown")
print(f"   new unknowns introduced = {len(new_unknowns)} ({sorted(str(s) for s in new_unknowns)});"
      f"  new equations = 1")
print(f"   solution for the new unknown is unique and positive for every ledger assignment "
      f"tested: {onto}")
print(f"   ⇒ the projection onto (hbar, alpha, k_B) is ONTO, so the relation fixes NO VALUE the")
print(f"     ledger did not already hold.  net constraint = 1 equation - 1 unknown = 0.")
ARM_D = D0 and D1 and onto and len(new_unknowns) == 1
print(f"   ⇒ Ⓓ {'HIT' if ARM_D else 'MISS'}: the VALUE slot of the selection test is EMPTY.")

print()
print("=" * 78)
print("Ⓔ  THE EXTENSION SLOT, MEASURED: IS THE MEMBER EUCLIDEAN REGULARITY SELECTS THE MEMBER THE")
print("   LORENTZIAN FORM CLOSURE ALREADY SINGLES OUT?")
print("=" * 78)
print("   model problem: -psi'' + gamma psi / x^2 = E psi on (0,1), Dirichlet at x=1, gamma = 1/4")
print("   (P10's ordering-family maximum), so nu = sqrt(gamma + 1/4) = 1/sqrt(2) < 1: limit circle.")
gam = 0.25
nu = np.sqrt(gam + 0.25)
print(f"   nu = {nu:.12f}   (1/sqrt(2) = {1/np.sqrt(2):.12f})")

def A_of(x, k):      # ~ x^{1/2+nu} as x->0   (the REGULAR indicial branch)
    return np.sqrt(x) * jv(nu, k * x) * G(nu + 1) * (2.0 / k) ** nu

def B_of(x, k):      # ~ x^{1/2-nu} as x->0   (the IRREGULAR branch)
    return np.sqrt(x) * jv(-nu, k * x) * G(1 - nu) * (k / 2.0) ** nu

# the asymptotics are checked, not assumed
for k in (1.0, 3.0):
    xs = np.array([1e-6, 1e-7, 1e-8])
    rA = A_of(xs, k) / xs ** (0.5 + nu)
    rB = B_of(xs, k) / xs ** (0.5 - nu)
    print(f"   k={k}:  A/x^(1/2+nu) -> {rA[-1]:.10f}   B/x^(1/2-nu) -> {rB[-1]:.10f}  (both -> 1)")
    note(abs(rA[-1] - 1) < 1e-8, f"regular branch asymptotic at k={k}")
    note(abs(rB[-1] - 1) < 1e-8, f"irregular branch asymptotic at k={k}")
    assert abs(rA[-1] - 1) < 1e-8 and abs(rB[-1] - 1) < 1e-8

def F(k, th):        # Dirichlet at x=1 for the member psi_th = cos(th) A + sin(th) B
    return np.cos(th) * A_of(1.0, k) + np.sin(th) * B_of(1.0, k)

def lowest(th):
    ks = np.linspace(0.05, 12.0, 4000)
    vals = F(ks, th)
    for i in range(len(ks) - 1):
        if vals[i] == 0:
            return ks[i]
        if vals[i] * vals[i + 1] < 0:
            return brentq(F, ks[i], ks[i + 1], args=(th,), xtol=1e-13, rtol=1e-14)
    return np.nan

thetas = np.linspace(0.0, np.pi / 2, 19)
E0 = np.array([lowest(t) ** 2 for t in thetas])
print("\n   (i) are the members physically distinct?  lowest eigenvalue against the extension")
print("       parameter theta (theta=0 is the pure regular branch):")
for t, e in list(zip(thetas, E0))[::3]:
    print(f"        theta = {t:.6f}   E_0 = {e:.10f}")
d = np.diff(E0)
strict = note(bool(np.all(d < -1e-9)) or bool(np.all(d > 1e-9)),
              "the family's spectra move strictly with the extension parameter")
for i, (t, e) in enumerate(zip(thetas, E0)):
    note(np.isfinite(e) and e > 0, f"lowest eigenvalue exists at theta={t:.4f}")
print(f"       strictly monotone across the family: {strict}   "
      f"(E_0 runs {E0[0]:.6f} -> {E0[-1]:.6f})")

print("\n   (ii) exactly one member carries no irregular admixture: by construction the admixture")
print("        coefficient is sin(theta), zero only at theta = 0 in [0, pi/2].")
n_pure = int(np.sum(np.abs(np.sin(thetas)) < 1e-15))
note(n_pure == 1, "exactly one member on the grid carries no irregular admixture")
print(f"        members with zero admixture on the grid: {n_pure}")

print("\n   (iii) the quadratic FORM energy Q[psi] = int (psi'^2 + gamma psi^2 / x^2):")
def Q_eps(th, eps):
    k = lowest(th)
    def psi(x):
        return np.cos(th) * A_of(x, k) + np.sin(th) * B_of(x, k)
    h = 1e-7
    def dpsi(x):
        return (psi(x + h) - psi(x - h)) / (2 * h)
    f = lambda x: dpsi(x) ** 2 + gam * psi(x) ** 2 / x ** 2
    v, _ = quad(f, eps, 1.0, limit=400)
    return v

eps = np.array([1e-2, 1e-3, 1e-4, 1e-5, 1e-6])
print(f"        {'eps':>8s} {'Q at theta=0':>18s} {'Q at theta=0.6':>18s} {'Q at theta=pi/2':>18s}")
rows = []
for e in eps:
    r = (Q_eps(0.0, e), Q_eps(0.6, e), Q_eps(np.pi / 2, e))
    rows.append(r)
    print(f"        {e:8.0e} {r[0]:18.8f} {r[1]:18.8f} {r[2]:18.8f}")
rows = np.array(rows)
conv = abs(rows[-1, 0] - rows[-2, 0]) / abs(rows[-1, 0])
slope_mid = np.polyfit(np.log(eps), np.log(rows[:, 1]), 1)[0]
slope_pure_irr = np.polyfit(np.log(eps), np.log(rows[:, 2]), 1)[0]
print(f"        theta=0:      Q converges, last relative change {conv:.2e}")
print(f"        theta=0.6:    log-log slope in eps = {slope_mid:.6f}   (predicted -2nu = {-2*nu:.6f})")
print(f"        theta=pi/2:   log-log slope in eps = {slope_pure_irr:.6f}  (predicted -2nu = {-2*nu:.6f})")
finite_only_at_zero = (note(conv < 1e-6, "form energy converges at the regular member")
                       and note(abs(slope_mid + 2 * nu) < 0.02,
                                "form energy diverges as eps^(-2nu) at a mixed member")
                       and note(abs(slope_pure_irr + 2 * nu) < 0.02,
                                "form energy diverges as eps^(-2nu) at the irregular member"))
ARM_E = strict and n_pure == 1 and finite_only_at_zero
print(f"   ⇒ Ⓔ {'HIT' if ARM_E else 'MISS/VOID'}: the family is ontological (distinct spectra), and")
print("     the FINITE-FORM-ENERGY member is the regular-branch member and nothing else.  So the")
print("     member Euclidean regularity selects is the member the Lorentzian quadratic form")
print("     closure already singles out: the selection is real but it is NOT distinctive.")

print("\n   control at the threshold: the irregular branch leaves L^2 exactly where P10's threshold")
print("   sits, which is why there is a family to choose from below it and none above it.")
for g in (0.25, 0.70, 0.75, 1.00):
    n = np.sqrt(g + 0.25)
    # int_eps^1 x^{1-2n} dx  -- finite as eps->0 iff n < 1
    # closed form, because the integral is the thing being tested for divergence:
    # int_eps^1 x^{1-2nu} dx = (1 - eps^{2-2nu})/(2-2nu),  and log(1/eps) at nu = 1.
    val = [((1.0 - e ** (2 - 2 * n)) / (2 - 2 * n)) if abs(n - 1) > 1e-12 else np.log(1.0 / e)
           for e in (1e-20, 1e-40)]   # far enough in that the three behaviours separate cleanly
    print(f"        gamma={g:4.2f}  nu={n:.6f}  int|x^(1/2-nu)|^2: {val[0]:12.4f} -> {val[1]:12.4f}"
          f"   {'in L^2' if n < 1 else 'NOT in L^2'}")
    # as eps -> 0 the integral settles (nu<1), doubles per two decades of eps (nu=1, logarithmic),
    # or blows up as eps^(2-2nu) (nu>1).  Over 20 decades that is a factor 1.10, 2.00 and ~5e4.
    grows = val[1] > 1.5 * val[0]
    note((n < 1) != grows, f"irregular branch L^2 membership at gamma={g} matches nu<1")
thr = np.sqrt(0.75 + 0.25)
note(abs(thr - 1.0) < 1e-15, "nu = 1 exactly at gamma = 3/4")
print(f"        nu = 1 exactly at gamma = 3/4 (computed: nu(3/4) = {thr:.12f}) -- the limit-point")
print("        threshold P10 states, reached here as the integrability of the irregular branch.")

print()
print("=" * 78)
print("Ⓕ  THE ORDERING SLOT: THE FACE CANNOT REACH THE ONE FREEDOM THE CONSTRUCTION CANNOT CLOSE")
print("=" * 78)
F1 = locate(P10, "the choice is not one this construction can make internally",
            "P10: the ordering choice is not one this construction can make internally")
F2 = locate(P10, "the horizon's thermal state and the seam's characteristic structure act "
                 "\\emph{downstream}",
            "P10: the thermal state and the seam act DOWNSTREAM")
rp = os.path.join(RECEIPTS, 'P10_canonical_time', 'P10_ordering_selection_is_external.py')
if not os.path.exists(rp):
    sys.exit("FATAL: P10_ordering_selection_is_external is not where this reads it from.")
rtxt = ' '.join(open(rp, errors='replace').read().split())
F3 = locate(rtxt, "It selects the Friedrichs extension, defined FROM the quadratic form",
            "receipt: the thermal state selects the FRIEDRICHS extension, defined FROM the form")
F4 = locate(rtxt, "the closure is ordering-independent (S11), the selection is not",
            "receipt: the closure is ordering-independent, THE SELECTION IS NOT")
ARM_F = F1 and F2 and F3 and F4
print(f"   ⇒ Ⓕ {'HIT' if ARM_F else 'MISS'}: the ORDERING slot is empty, and the receipt that")
print("     establishes it is read here rather than reimplemented (r7445).")

print()
print("=" * 78)
print("Ⓖ  THE TERMINATE CLAUSE: ARE THE HALVES ONE QUESTION?")
print("=" * 78)
ARM_G = ARM_C and not ARM_H_FIRES
print(f"   ⇒ Ⓖ {'HIT' if ARM_G else 'MISS'}: NOT one question.  Two claims of different strength")
print("     about two different objects, blocked for different reasons -- the gauge half by a")
print("     VANISHING (the bundle is flat, so the structure its test asks for is not there), the")
print("     quantum half by a NON-DISTINCTNESS (the selection the face makes is one the Lorentzian")
print("     form closure also makes).  The terminate clause does not fire.")

print()
print("=" * 78)
print("VERDICT")
print("=" * 78)
score = {'A': ARM_A, 'B': ARM_B, 'C': ARM_C, 'D': ARM_D, 'E': ARM_E, 'F': ARM_F, 'G': ARM_G}
for k, v in score.items():
    note(v, f"arm {k}")
    print(f"   {k}: {'HIT' if v else 'MISS'}")
note(not ARM_H_FIRES, "control H does not fire")
print(f"   H (control): {'FIRES -- the reading is wrong' if ARM_H_FIRES else 'does not fire'}")
print()
print("   THE QUANTUM HALF CAN CARRY A TEST, AND IT IS NOT THE GAUGE HALF'S.  The gauge half's test")
print("   is a STRUCTURE test and the quantum claim is a SCALE claim, so the right test is a")
print("   SELECTION test: the face is an actual quantum sector rather than a rhyme iff its data")
print("   remove a freedom of the quantum theory that no Lorentzian principle removes.  All three")
print("   slots where it could do that are empty -- no VALUE (Ⓓ), an EXTENSION the form closure")
print("   also picks (Ⓔ), an ORDERING it cannot reach (Ⓕ).  So the test is named and UNMET, and")
print("   what would meet it is named with it: a DIMENSIONLESS selection the compact face makes")
print("   and the Lorentzian form does not.")
assert all(score.values()), score
assert not ARM_H_FIRES
bad = [lab for ok, lab in CHECKS if not ok]
print(f"\n   {len(CHECKS)} checks, {len(bad)} failures." + (f"  FAILED: {bad}" if bad else ""))
assert not bad, bad
