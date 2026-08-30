"""N1 — p0's IDENTITY CHECKED: THE de SITTER ENTROPY AND THE COSMOLOGICAL-CONSTANT FACTOR.

INFORMATION-THEORY FIELD BAKE, probe N1.

p0 makes one quantitative claim in this field's vicinity, and it is a headline:

    "The cosmological-constant problem's factor is the ratio of the field-theoretic vacuum
     estimate to the observed rho_Lambda = Lambda/8 pi G, which is 8 pi/(Lambda l_P^2); the
     entropy is 3 pi/(Lambda l_P^2).  The two differ by 3/8 and by nothing else --- both are
     1/(Lambda l_P^2) read with a different numerical coefficient, and the 10^122 of the one is
     the 10^122 of the other rather than a coincidence of size."

** THE FIELD'S INTEREST IS SPECIFIC. **  S = A/4 l_P^2 is a COUNT -- a dimensionless number of
nats, the only genuinely information-theoretic quantity the corpus carries.  If p0's identity
holds, then the cosmological-constant fine-tuning number IS that count, and the corpus has an
information-theoretic statement it never names as one.  If it does not hold, a headline is wrong.

*** SO THIS RECEIPT IS NOT A FORMALITY.  IT CAN FALSIFY A CLAIM p0 PUTS IN ITS OWN VOICE. ***

VERDICTS:
  1. S = A/(4 l_P^2) with A = 4 pi alpha^2 and alpha^2 = 3/Lambda gives 3 pi/(Lambda l_P^2).
  2. rho_Lambda = Lambda/(8 pi G) with G = l_P^2, and the field-theoretic estimate 1/l_P^4,
     gives a ratio 8 pi/(Lambda l_P^2).
  3. THE RATIO OF THE TWO IS EXACTLY 3/8 -- symbolically, with no numerics.
  4. BOTH are 1/(Lambda l_P^2) times a pure number: the Lambda- and l_P-dependence is identical,
     which is the load-bearing half of p0's sentence ("and by nothing else").
  5. AT THE OBSERVED VALUES both are ~10^122, so the "10^122 of the one is the 10^122 of the
     other" is arithmetic and not rhetoric.
  6. CONTROL -- a quantity that is NOT of this form (the de Sitter TEMPERATURE, which p0 says the
     corpus does take) must NOT come out proportional to 1/(Lambda l_P^2).  Without this the
     receipt would be showing only that two multiples of one expression are proportional.

Written r3612 by node 60, information-theory bake.  Stated for reversal.
"""
import sympy as sp

FAIL = []
def check(label, got, want):
    ok = sp.simplify(got - want) == 0 if hasattr(got, 'free_symbols') or hasattr(want, 'free_symbols') \
         else got == want
    print(f"    [{'ok' if ok else 'FAIL'}]  {label}")
    print(f"             got  = {got}")
    if not ok:
        print(f"             want = {want}")
        FAIL.append(label)
    return ok

Lam, lP = sp.symbols('Lambda ell_P', positive=True)

print("=" * 78)
print("N1 — p0's 3/8, CHECKED SYMBOLICALLY")
print("=" * 78)

print("\nVERDICT 1 — THE ENTROPY.")
alpha2 = 3 / Lam                       # alpha^2 = 3/Lambda, the throat radius squared
A = 4 * sp.pi * alpha2                 # the de Sitter horizon area
S = sp.simplify(A / (4 * lP**2))       # Bekenstein--Hawking
check("S == 3 pi / (Lambda l_P^2)", S, 3 * sp.pi / (Lam * lP**2))

print("\nVERDICT 2 — THE FINE-TUNING FACTOR.")
G = lP**2                              # G = l_P^2 in these units
rho_Lambda = Lam / (8 * sp.pi * G)     # the observed vacuum density
rho_qft = 1 / lP**4                    # the field-theoretic estimate, one Planck mass per Planck volume
F = sp.simplify(rho_qft / rho_Lambda)
check("F == 8 pi / (Lambda l_P^2)", F, 8 * sp.pi / (Lam * lP**2))

print("\nVERDICT 3 — THE RATIO, WHICH IS THE CLAIM.")
ratio = sp.simplify(S / F)
check("S / F == 3/8 exactly", ratio, sp.Rational(3, 8))
print("    *** p0's sentence is arithmetic.  The two differ by 3/8. ***")

print("\nVERDICT 4 — 'AND BY NOTHING ELSE': the Lambda- and l_P-dependence must be IDENTICAL.")
X = 1 / (Lam * lP**2)
cS = sp.simplify(S / X)
cF = sp.simplify(F / X)
print(f"    S = ({cS}) * 1/(Lambda l_P^2)      F = ({cF}) * 1/(Lambda l_P^2)")
check("S's coefficient is a pure number", cS.free_symbols, set())
check("F's coefficient is a pure number", cF.free_symbols, set())
check("and the ratio of coefficients is 3/8", sp.simplify(cS / cF), sp.Rational(3, 8))

print("\nVERDICT 5 — AT THE OBSERVED VALUES, both are ~10^122.")
# Lambda ~ 1.1e-52 m^-2 ; l_P ~ 1.616e-35 m
subs = {Lam: sp.Float('1.1e-52'), lP: sp.Float('1.616e-35')}
Sv = float(S.subs(subs)); Fv = float(F.subs(subs))
eS = sp.floor(sp.log(Sv, 10)); eF = sp.floor(sp.log(Fv, 10))
print(f"    S = {Sv:.3e}   (10^{eS})")
print(f"    F = {Fv:.3e}   (10^{eF})")
check("the entropy's exponent is 122", int(eS), 122)
check("the fine-tuning factor's exponent is 122", int(eF), 122)
check("and their ratio is still 3/8 numerically", round(Sv / Fv, 12), round(3 / 8, 12))

print("\nVERDICT 6 — THE CONTROL.  The de Sitter TEMPERATURE must NOT be of this form.")
print("  p0 says the corpus takes this horizon's temperature and never its entropy, because the")
print("  temperature is built from alpha alone -- ONE register -- while the entropy is a ratio of")
print("  alpha to l_P, a count taken ACROSS the register split.  If T also went as 1/(Lambda l_P^2)")
print("  that distinction would be empty and so would this receipt.")
alpha = sp.sqrt(alpha2)
T = sp.simplify(1 / (2 * sp.pi * alpha))
print(f"    T = {T}")
check("T carries NO l_P at all", lP in T.free_symbols, False)
tc = sp.simplify(T / X)
print(f"    T / [1/(Lambda l_P^2)] = {tc}   -- not a pure number, so T is not of that form")
check("T is NOT proportional to 1/(Lambda l_P^2)", tc.free_symbols == set(), False)
print("    *** The register distinction is real: T is one-register, S is cross-register. ***")

print("\n" + "=" * 78)
if FAIL:
    print(f"  VERDICT: {len(FAIL)} CHECK(S) FAILED -- p0's headline does not hold as written")
    for f in FAIL:
        print("   ", f)
    raise SystemExit(1)
print("  VERDICT: ALL PASS.  p0's identity is exact.  The de Sitter entropy -- the corpus's one")
print("  genuinely information-theoretic quantity, a dimensionless COUNT -- and the cosmological-")
print("  constant fine-tuning factor are one number up to 3/8, and the register distinction p0")
print("  draws between the temperature and the entropy is real.")
print("=" * 78)
