#!/usr/bin/env python3
"""
RECEIPT -- p0: ** ITEM 52 WORKED, AND IT IS ONE CLAUSE.  THE de SITTER HORIZON'S ENTROPY IS
S = pi(alpha/l_P)^2 = 3pi/(Lambda l_P^2) ~ 3e122 -- THE LEDGER'S OWN GAUGE-COUNT SQUARED -- AND
⛭⛭ *** IT IS THE SAME NUMBER AS THE COSMOLOGICAL-CONSTANT PROBLEM'S FACTOR, NOT MERELY THE SAME
MAGNITUDE: BOTH ARE 1/(Lambda l_P^2), DIFFERING BY 3/8. *** SO HORIZON THERMODYNAMICS ADDS NO NEW
SCALE, AND THE DISSOLUTION p0 ALREADY GIVES FOR THE ONE IS THE DISSOLUTION OF THE OTHER. **

Built r2566+c54.207, lead `L-532`.  VEIN: `L-165` (PO-6, what a quantum of this geometry is).

===================================================================================================
** WHAT WAS ROUTED, AND THE ONE THING IT DID NOT SEE **
===================================================================================================

r2536 routed this as an ASYMMETRY that bites on `PO-6`: *T depends on alpha alone, S on the ratio
alpha/l_P, and PO-6 asks whether one dimensionful constant can regulate.*  r2564 answered it from p0's
own text -- *l_P is a GAUGE, not a scale, so S is a THIRD statement of one number* -- and reduced the
owing to a clause.  ** Both are right.  Neither noticed that p0's next paragraph is already holding
the same number. **

  ** ⓵ THE ARITHMETIC. **   A = 4 pi alpha^2,  S = A/4 l_P^2 = pi (alpha/l_P)^2 = 3 pi/(Lambda l_P^2).
     *With p0's own Lambda l_P^2 ~ 3e-122 this is ~3.14e122 -- the gauge-count alpha/l_P ~ 1e61
     squared, and nothing else.*

  ** ⓶ ⛭⛭ AND THE COSMOLOGICAL-CONSTANT FACTOR IS THE SAME QUANTITY. **  p0's very next paragraph
     names *"$\\Lambda$ is some $10^{122}$ times smaller than the quantum-field vacuum estimate"*.
     That factor is rho_QFT/rho_Lambda ~ l_P^-4 / (Lambda/8 pi G) = ** 8 pi/(Lambda l_P^2) **.
     ⇒ *** S / (that factor) = 3/8 EXACTLY.  Both are 1/(Lambda l_P^2); the two 10^122's are ONE
         NUMBER read with different coefficients, and it was sitting two paragraphs apart. ***
     ⇒⇒ ** So p0's existing dissolution of the cosmological-constant problem -- there is nothing
        physical for Lambda to be small AGAINST, l_P being a cross-register gauge-combination -- is
        already the dissolution of the entropy's number.  The clause costs nothing new. **

  ** ⓷ AND THE ASYMMETRY HAS A STRUCTURAL CAUSE, WHICH IS WHY THE CORPUS TAKES T AND NOT S. **
     T = 1/2 pi alpha is ONE-REGISTER (alpha alone, the thermal gauge setting only the unit);
     S = pi(alpha/l_P)^2 is a count taken ACROSS p0's own register split.
     ⇒ *The quantity the framework needs is the one-register one; the quantity that would TEST the
      ledger is the cross-register one -- and what it returns is the ledger's own number back.*

===================================================================================================
** ⛔ WHAT IS NOT CLAIMED **
===================================================================================================

** Not that a de Sitter entropy is asserted. **  *Whether S = A/4 carries to a cosmological horizon on
this reading is exactly what would have to be argued, and p0 says so in the clause.*  ** Not that
PO-6's dark half is closed ** -- the one-constant regulation question is untouched; what is removed is
the appearance that the entropy poses a NEW instance of it.  ** Not a derivation of Lambda's value **,
which p0 keeps as the ledger's one input.  ** And not that the 3/8 is meaningful **: it is a
coefficient, and the claim is about the 1/(Lambda l_P^2) both quantities are built from.

⚠ ** THE COINCIDENCE IS ONLY INTERESTING IF THE CC PARAGRAPH IS STILL THERE TO COINCIDE WITH. **
PART 4 pins p0's own $10^{122}$ sentence present -- *if it were ever cut, the new clause's second
paragraph would be comparing itself to nothing.*

SETTINGS: none -- no instrument, no spectra.  Exact symbolic reduction of S and of the vacuum-energy
ratio to a common factor, arithmetic at p0's own Lambda l_P^2, and source checks.

rc=0 on success.  Run: python3 P17_the_ds_entropy_is_the_gauge_count_squared_and_is_the_cc_number.py
                        (sympy; ~4 s)
"""
import os
import re
import sys

import sympy as sp

print(__doc__.split("rc=0")[0])

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
CORPUS = os.path.join(ROOT, 'corpus')
fail = []

al, lP, Lam = sp.symbols('alpha ell_P Lambda', positive=True)

# =====================================================================
print("=" * 78)
print("PART 1 — THE ENTROPY, REDUCED RATHER THAN QUOTED")
print("=" * 78)
A = 4 * sp.pi * al ** 2
S = sp.simplify(A / (4 * lP ** 2))
S_ratio = sp.simplify(S / sp.pi)                      # should be (alpha/l_P)^2
S_lam = sp.simplify(S.subs(al, sp.sqrt(3 / Lam)))     # should be 3 pi/(Lambda l_P^2)
print(f"  A = 4 pi alpha^2 = {A}")
print(f"  S = A/(4 l_P^2)  = {S}")
print(f"  S/pi             = {S_ratio}       ** the gauge-count alpha/l_P, SQUARED **")
print(f"  with alpha = sqrt(3/Lambda):  S = {S_lam}")
_ok_sq = sp.simplify(S_ratio - (al / lP) ** 2) == 0
_ok_lam = sp.simplify(S_lam - 3 * sp.pi / (Lam * lP ** 2)) == 0
print(f"\n  S = pi (alpha/l_P)^2      : {_ok_sq}")
print(f"  S = 3 pi/(Lambda l_P^2)   : {_ok_lam}")
if not _ok_sq:
    fail.append("S is not pi times the gauge-count squared — the clause's first identity fails")
if not _ok_lam:
    fail.append("S does not reduce to 3 pi/(Lambda l_P^2) — the clause's stated form is wrong")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — ⛭⛭ AND THE COSMOLOGICAL-CONSTANT FACTOR, REDUCED TO THE SAME THING")
print("=" * 78)
G, hbar_, c_ = sp.symbols('G hbar c', positive=True)
# geometrized/natural units, hbar = c = 1, so l_P^2 = G:
rho_Lambda = Lam / (8 * sp.pi * lP ** 2)     # Lambda/(8 pi G) with G = l_P^2
rho_QFT = 1 / lP ** 4                        # ~ m_P^4
CC = sp.simplify(rho_QFT / rho_Lambda)
print(f"  rho_Lambda = Lambda/(8 pi G),  G = l_P^2   ->  {rho_Lambda}")
print(f"  rho_QFT    ~ m_P^4 = 1/l_P^4               ->  {rho_QFT}")
print(f"  ** the CC problem's factor = {CC} **")
print()
_ratio = sp.simplify(S_lam / CC)
print(f"  *** S / (CC factor) = {_ratio} ***")
print("      ** Both are 1/(Lambda l_P^2).  NOT the same magnitude -- THE SAME NUMBER, differing by a")
print("         numerical coefficient.  And p0 already dissolves the second, two paragraphs on. **")
_ok_common = sp.simplify(_ratio - sp.Rational(3, 8)) == 0
print(f"  the two differ by exactly 3/8 : {_ok_common}")
if not _ok_common:
    fail.append(f"S/CC came out {_ratio}, not 3/8 — 'the same number' is not what the algebra gives")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — AND THE NUMBER ITSELF, AT p0'S OWN Lambda l_P^2")
print("=" * 78)
LLP2 = 3.0e-122            # p0: "Lambda l_P^2 approx 3e-122", cited to P15
_S = float(3 * sp.pi / LLP2)
_CC = float(8 * sp.pi / LLP2)
_gauge = float(sp.sqrt(3 / LLP2))
print(f"  p0's own value:  Lambda l_P^2 = {LLP2:.1e}")
print(f"  gauge-count      alpha/l_P    = {_gauge:.3e}     ** p0 prints ~1e61 **")
print(f"  entropy          S            = {_S:.3e}     ** p0 now prints ~3e122 **")
print(f"  CC factor                     = {_CC:.3e}     ** p0 prints ~1e122 **")
print(f"  and (alpha/l_P)^2             = {_gauge**2:.3e}")
print()
print("  ⇒ *One number, stated three ways in one section: as a ratio, as its square, and as a")
print("     fine-tuning.  ** The entropy is the third and it is not a new one. ***")
if not (2.9e122 < _S < 3.3e122):
    fail.append(f"S evaluates to {_S:.3e}, not the ~3e122 the paper prints")
if not (0.9e61 < _gauge < 1.1e61):
    fail.append(f"the gauge-count evaluates to {_gauge:.3e}, not p0's ~1e61")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — WHAT p0 NOW SAYS, AND THE PARAGRAPH THE COINCIDENCE IS AGAINST")
print("=" * 78)
P0 = open(os.path.join(CORPUS, 'geometric_core_paper.tex'), encoding='utf-8').read()
WRITTEN = [
    ("the entropy is named at all — it was at ZERO uses in p0 before this revision",
     r'Bekenstein--Hawking'),
    ("the three forms are given in one display",
     r'S=\\frac\{A\}\{4\\ell_P\^\{2\}\}=\\pi\\Bigl\(\\frac\{\\alpha\}\{\\ell_P\}\\Bigr\)\^\{2\}'),
    ("and reduced to the Lambda form",
     r'\\frac\{3\\pi\}\{\\Lambda\\ell_P\^\{2\}\}'),
    ("it is called the gauge-count squared and nothing further",
     r'the gauge-count just stated, squared, and nothing further'),
    ("the no-new-scale statement is made",
     r'introduces no scale the ledger has not already entered'),
    ("⛭ the coincidence with the cosmological-constant factor is stated as identity, not size",
     r'not merely of the same magnitude[^.]*it is the same\s*\n?number'),
    ("the 3/8 is given rather than waved at",
     r'differ by \$3/8\$ and by nothing else'),
    ("the one-register/cross-register reason for the asymmetry is stated",
     r'count taken \\emph\{across\} the\s*\n?register split'),
    ("and the not claimed is attached",
     r'not claimed is that a de~Sitter entropy is asserted here'),
]
for what, pat in WRITTEN:
    ok = re.search(pat, P0, re.I | re.S) is not None
    print(f"  {'OK ' if ok else 'MISSING'}  {what}")
    if not ok:
        fail.append(f"the written clause does not carry: {what}")

print()
ANCHORS = [
    ("p0's gauge-count sentence, which the clause squares",
     r'is the size of the universe in gauge-units---a number, not a tuning'),
    ("⚠ p0's cosmological-constant 10\\^122 sentence, which the clause coincides with",
     r'\$\\Lambda\$ is some \$10\^\{122\}\$ times smaller than the quantum-field vacuum estimate'),
    ("and p0's reading of a Planck value as a gauge and not a scale, which does the dissolving",
     r'a Planck value is \\emph\{not\} a physical scale'),
]
for what, pat in ANCHORS:
    ok = re.search(pat, P0, re.I | re.S) is not None
    print(f"  {'OK ' if ok else 'MISSING'}  {what}")
    if not ok:
        fail.append(f"the anchor the clause rests on is gone: {what}")

# =====================================================================
print()
print("=" * 78)
if fail:
    print("FAILED: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS — S reduces to pi(alpha/l_P)^2 and to 3pi/(Lambda l_P^2); the cosmological-")
print("constant factor reduces to 8pi/(Lambda l_P^2), so the two are one quantity differing by 3/8;")
print("at p0's own Lambda l_P^2 the entropy is 3.1e122 against a gauge-count of 1.0e61; and p0 now")
print("carries the clause, the coincidence and the not claimed, against all three anchors it rests on.")
print("=" * 78)

# ============================================================================================
# GATE — r2566+c54.207, `L-532`.  ** The temptation in a clause like this is to let "of the same
# order" pass for "the same quantity" **, so the pins are on the reduction being exact and on the
# clause staying a non-assertion:
#   (1) S reduced symbolically to BOTH stated forms -- ** the paper prints three expressions as one
#       identity and they are checked as one, not quoted **;
#   (2) *** the cosmological-constant factor reduced to 8 pi/(Lambda l_P^2) and the ratio pinned at
#       exactly 3/8 ***.  ** This is the gate's centre.  If the two were merely both ~1e122 the
#       clause would be a numerical coincidence and worth nothing; that they are the same
#       dimensionless combination is the whole reason it is worth a paragraph **;
#   (3) the arithmetic at p0's OWN Lambda l_P^2, bracketed -- so the printed ~3e122 and the printed
#       ~1e61 are the same input read twice and not two quoted numbers;
#   (4) nine source checks on what is written, including that the coincidence is stated as identity
#       rather than as magnitude and that the not claimed is attached;
#   (5) and *** three ANCHOR checks ***: the gauge-count sentence the clause squares, p0's own
#       10^122 sentence the clause coincides with, and the Planck-value-is-a-gauge reading that does
#       the dissolving.  ** Each is pre-existing; delete any one and the clause is arguing against
#       an absence. **
#   NOT gated: that S = A/4 applies to a cosmological horizon on this reading.  ** p0 declines it and
#   this file declines it; what is computed is what the number IS if the expression is taken. **
# ============================================================================================
assert _ok_sq and _ok_lam, "the entropy does not reduce to the forms p0 prints"
assert _ok_common, "S and the CC factor are NOT the same 1/(Lambda l_P^2) — the coincidence claim fails"
assert 2.9e122 < _S < 3.3e122, "S does not evaluate to the ~3e122 in print"
assert 0.9e61 < _gauge < 1.1e61, "the gauge-count does not evaluate to p0's ~1e61"
for what, pat in WRITTEN:
    assert re.search(pat, P0, re.I | re.S), f"source check failed: {what}"
for what, pat in ANCHORS:
    assert re.search(pat, P0, re.I | re.S), f"anchor missing: {what}"
print(f"GATE c54.207 (r2566), `L-532`: S = pi(alpha/l_P)^2 = 3pi/(Lambda l_P^2) = {_S:.2e} at p0's own "
      f"Lambda l_P^2 = {LLP2:.0e}, against a gauge-count {_gauge:.2e}; the cosmological-constant factor "
      f"is 8pi/(Lambda l_P^2), so S/CC = {_ratio} exactly and the two 10^122's are one dimensionless "
      f"combination; and p0 states the clause with its not claimed, against three standing anchors — "
      f"pinned against `FOR_54` item 52 (r2536, answered r2564).")
