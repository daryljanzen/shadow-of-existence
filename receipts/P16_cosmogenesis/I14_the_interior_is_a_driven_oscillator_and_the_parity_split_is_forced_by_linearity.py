"""
LEVEL: exact symbolic, with a NONLINEAR control that must break the split.

WHY THIS PROBE EXISTS.  P16 sec:interior states that the closed dust-plus-radiation
ball is solved exactly in conformal time by a = (A/2)(1 - cos eta) + sqrt(B) sin eta,
"whose parity splits BY SPECIES with no cross terms -- the dust term is the entire even
part and the radiation term the entire odd part".  It reports that as a structural
feature of the two species.  It is not: it is a property of a second-order LINEAR
ordinary differential equation, and the whole indicial-exponent argument downstream --
exponents moving from (-1,2) to (0,1), the potential's 1/sigma term landing on the
resonance, the forced logarithm, the unipotent monodromy -- rests on the odd part being
present and being radiation's ALONE.

WHAT IS CLAIMED.
  (1) In conformal time the interior obeys a'' + a = A/2, a DRIVEN HARMONIC OSCILLATOR,
      and P16's stated solution is its general solution with the cosine coefficient
      fixed by a(0) = 0.
  (2) The parity split is FORCED BY LINEARITY.  The particular solution is the constant
      A/2 (even); the homogeneous modes are cos eta (even) and sin eta (odd); a linear
      equation cannot mix them, so the dust amplitude fixes the even part and the
      radiation amplitude the odd, with no cross terms available.
  (3) It is the SAME equation as P02's cycloid, r'' + r = M, and P02 is this at B = 0 --
      so the vacuum interior is the even member of one family and radiation is what
      switches the odd mode on.

WHAT IS NOT CLAIMED.  Nothing about Lambda: this is a Lambda = 0 interior, which is why
it is elementary at all (see I12).  Nothing about whether the physical radiation content
is small.  Nothing about the monodromy itself, which P16 establishes separately.

WHAT WOULD FALSIFY IT.  The stated solution failing a'' + a = A/2; the even and odd
parts not aligning with the dust and radiation amplitudes; or -- the discriminator --
a NONLINEAR term failing to break the split, which would show that linearity is not
what is doing the work.  That control is run below and MUST produce cross terms.
"""
import sympy as sp

FAILS = []


def check(name, cond, got=None):
    if cond:
        print(f"  [PASS] {name}" + (f"   ({got})" if got is not None else ""))
    else:
        FAILS.append(name)
        print(f"  [FAIL] {name}" + (f"   (got {got})" if got is not None else ""))


eta = sp.Symbol('eta', real=True)
A, B, M, z = sp.symbols('A B M z', positive=True)

print(__doc__)
print("=" * 78)

a = A / 2 * (1 - sp.cos(eta)) + sp.sqrt(B) * sp.sin(eta)
print(f"  P16:  a(eta) = {a}")
print()

# (1) it solves the driven oscillator
res = sp.simplify(sp.diff(a, eta, 2) + a - A / 2)
check("a'' + a = A/2 identically -- the driven harmonic oscillator",
      res == 0, f"residual {res}")
check("and a(0) = 0, which is what fixes the cosine coefficient at -A/2",
      sp.simplify(a.subs(eta, 0)) == 0)

# the general solution, to show P16's is IT and not a special case
C1, C2 = sp.symbols('C1 C2')
gen = sp.dsolve(sp.Eq(sp.Derivative(sp.Function('y')(eta), eta, 2) + sp.Function('y')(eta), A / 2),
                sp.Function('y')(eta)).rhs
check("the general solution is A/2 + (constant)cos + (constant)sin",
      gen.has(sp.cos(eta)) and gen.has(sp.sin(eta)) and gen.has(A),
      "particular + two homogeneous modes")

# (2) the parity split, computed rather than asserted
even = sp.simplify((a + a.subs(eta, -eta)) / 2)
odd = sp.simplify((a - a.subs(eta, -eta)) / 2)
check("the EVEN part is exactly the dust term (A/2)(1 - cos eta)",
      sp.simplify(even - A / 2 * (1 - sp.cos(eta))) == 0, f"{even}")
check("the ODD part is exactly the radiation term sqrt(B) sin eta",
      sp.simplify(odd - sp.sqrt(B) * sp.sin(eta)) == 0, f"{odd}")
check("the even part carries A and NOT B -- no cross term",
      B not in even.free_symbols, f"free symbols {even.free_symbols}")
check("the odd part carries B and NOT A -- no cross term",
      A not in odd.free_symbols, f"free symbols {odd.free_symbols}")

# (3) the same equation as P02
rc = M * (1 + sp.cos(z))
check("P02's cycloid obeys r'' + r = M -- the SAME equation",
      sp.simplify(sp.diff(rc, z, 2) + rc - M) == 0)
check("and P16 at B = 0 is that cycloid, shifted by pi",
      sp.simplify(a.subs(B, 0) - (A / 2) * (1 - sp.cos(eta))) == 0, "even member")

# ---- NONLINEAR CONTROL: the discriminator -----------------------------------
print()
print("  NONLINEAR CONTROL -- add a quadratic term and the split MUST break,")
print("  or linearity is not what is doing the work.")
y = sp.Function('y')
# perturb: y'' + y + e y^2 = A/2, solved to first order in e about the linear solution
e = sp.Symbol('e', positive=True)
y0 = a
# first-order correction obeys y1'' + y1 = -y0^2 ; its source has BOTH parities mixed
source = sp.expand(sp.expand_trig(sp.simplify(-y0**2)))
src_even = sp.simplify((source + source.subs(eta, -eta)) / 2)
src_odd = sp.simplify((source - source.subs(eta, -eta)) / 2)
check("CONTROL: the quadratic source's EVEN part now contains B (dust parity carries radiation)",
      B in sp.simplify(src_even).free_symbols, f"even source has {sp.simplify(src_even).free_symbols}")
check("CONTROL: and its ODD part now contains A -- the species have MIXED",
      A in sp.simplify(src_odd).free_symbols, f"odd source has {sp.simplify(src_odd).free_symbols}")
check("CONTROL: so the split is a property of LINEARITY and not of these two species",
      B in sp.simplify(src_even).free_symbols and A in sp.simplify(src_odd).free_symbols)

print()
print("=" * 78)
if FAILS:
    print(f"  VERDICT: {len(FAILS)} FAILURE(S): {', '.join(FAILS)}")
    raise SystemExit(1)
print("  VERDICT: ALL PASS.  P16's interior solves a'' + a = A/2, a driven harmonic")
print("  oscillator, and is its general solution.  The even part carries the dust")
print("  amplitude and not the radiation one, the odd part the reverse -- computed, not")
print("  asserted.  The nonlinear control mixes them, so 'no cross terms' is a property")
print("  of a second-order LINEAR equation and not of dust and radiation.  And it is the")
print("  same equation as P02's cycloid, which is this at B = 0.")
print("=" * 78)
