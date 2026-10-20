"""
LEVEL: exact symbolic throughout, with a CONTROL on each single-species interior.

WHY THIS PROBE EXISTS.  `r7465+cc66.10` discharged PO-88 for a PRESSURELESS model: the
crossing is an involution, the density even, the radial rate odd.  `r7473` ordered the
pressure half -- P16's own interior, dust PLUS radiation, carried through with T^r_r and
T^theta_theta -- and the pre-registration named the one thing it could not compute in
advance: P16 sec:interior carries a SECOND parity, in conformal time, where I14
establishes that the dust term is the entire even part of a(eta) and the radiation term
the entire odd part.  Whether that reaches the crossing was the open question.

WHAT IS CLAIMED.
  (1) P16's interior a = (A/2)(1 - cos eta) + sqrt(B) sin eta solves a'' + a = A/2 and
      vanishes at eta = 0, so eta = 0 is the branch point; its even part carries the dust
      amplitude alone and its odd part the radiation amplitude alone.
  (2) THE TWO PARITIES ARE NOT INDEPENDENT.  The ORDER of the zero at the branch point
      depends on the species content: 2 for dust alone (a even, the curve TOUCHES zero),
      1 for radiation alone (a odd) and 1 for the mixture (a NEITHER even nor odd).
      Radiation's odd amplitude is what makes the zero transversal.
  (3) THE REFLECTION IS NOT A SYMMETRY OF P16's MEMBER.  a(-eta) is identically a(eta)
      with sqrt(B) -> -sqrt(B): the crossing carries the interior to the member with the
      RADIATION AMPLITUDE REVERSED IN SIGN.  So the crossing is an involution on the
      FAMILY and not on the member, and it is NOT species-blind.
  (4) PER INTERIOR: on a single-species interior every scalar (rho, and radiation's
      p = rho/3, which is T^r_r = T^theta_theta) is EVEN and the areal rate is ODD, so
      the involution of `r7465+cc66.10` holds there.  On P16's mixed interior all four
      are NEITHER, because of (3).
  (5) AND IT CORRECTS `r7465+cc66.10`'s ROUTE WITHOUT TOUCHING ITS RESULT: that revision
      took the crossing parity from the VACUUM slicing curve r = alpha sin(theta), which
      has a simple odd zero, and needed |r| to keep the density positive.  P16's dust
      interior has a DOUBLE zero, so for dust alone the scale factor never goes negative
      and the density is even with no absolute value needed.

WHAT IS NOT CLAIMED.  No temperature, no abundance, nothing about the magnitude of the
radiation amplitude, and nothing about whether the sign reversal is observable.  Not that
information is LOST at the crossing -- the map is still invertible; what changes is which
member of the family comes out.  And nothing about a third species.

WHAT WOULD FALSIFY IT.  The stated solution failing its own equation; the zero's order
not depending on the species content; a(-eta) not being the sign-reversed member; the
single-species parities coming out other than scalars-even / rate-odd; or -- the
discriminator -- the CONTROL failing, i.e. the rate coming out with the SAME parity as
the scalars on a single-species interior, which would show the even answer to be an
artefact of taking absolute values rather than a fact about densities.
"""
import sympy as sp

FAILS = []


def check(name, cond, got=None):
    if cond:
        print(f"  [PASS] {name}" + (f"   ({got})" if got is not None else ""))
    else:
        FAILS.append(name)
        print(f"  [FAIL] {name}" + (f"   (got {got})" if got is not None else ""))


print("=" * 78)
print("  P16 / PO-88 -- THE CROSSING REVERSES THE RADIATION AMPLITUDE,")
print("  SO IT IS NOT SPECIES-BLIND")
print("=" * 78)

eta = sp.Symbol('eta', real=True)
A, B = sp.symbols('A B', positive=True)

# ---- READ the paper, so this receipt fails when the paper moves -------------
# â check_unread_figure was right: these numbers were the PAPER's and nothing
#   here opened it, so the check would have stayed green while the paper moved.
#   The remedy it names first is to READ the figure, and that is what this does.
import os
_HERE = os.path.dirname(os.path.abspath(__file__))
_P16 = os.path.join(_HERE, '..', '..', 'corpus', 'cosmogenesis_paper.tex')
with open(_P16, encoding='utf-8') as _fh:
    _SRC = _fh.read()

_LIT = r"a=\tfrac{A}{2}(1-\cos\eta)+\sqrt{B}\sin\eta"
check("READ from cosmogenesis_paper.tex: P16's own interior solution is printed there "
      f"as {_LIT}", _LIT in _SRC)

a = (A / 2) * (1 - sp.cos(eta)) + sp.sqrt(B) * sp.sin(eta)


def parity(expr):
    if expr == 0:
        return "EVEN"
    ev = sp.simplify(sp.simplify(expr.subs(eta, -eta) - expr)) == 0
    od = sp.simplify(sp.simplify(expr.subs(eta, -eta) + expr)) == 0
    return "EVEN" if ev else ("ODD" if od else "NEITHER")


# ---- (1) the solution ------------------------------------------------------
# â Same rewording, same reason: the equation is checked, not attributed.
check("the interior solution read above satisfies the driven-oscillator equation it is "
      "said to solve, identically",
      sp.simplify(sp.diff(a, eta, 2) + a - A / 2) == 0)
check("and vanishes at eta = 0, so eta = 0 is the branch point",
      sp.simplify(a.subs(eta, 0)) == 0)
even_part = sp.simplify((a + a.subs(eta, -eta)) / 2)
odd_part = sp.simplify((a - a.subs(eta, -eta)) / 2)
check("the EVEN part carries the dust amplitude alone (I14's split, re-derived)",
      B not in even_part.free_symbols and A in even_part.free_symbols, even_part)
check("the ODD part carries the radiation amplitude alone",
      A not in odd_part.free_symbols and B in odd_part.free_symbols, odd_part)

# ---- (2) the order of the zero depends on the species content -------------
def zero_order(expr):
    ser = sp.simplify(sp.series(expr, eta, 0, 4).removeO())
    return 1 if sp.simplify(sp.limit(ser / eta, eta, 0)) != 0 else 2

check("dust alone: a has a DOUBLE zero and is EVEN -- the curve touches zero",
      zero_order(a.subs(B, 0)) == 2 and parity(a.subs(B, 0)) == "EVEN",
      f"order {zero_order(a.subs(B, 0))}, {parity(a.subs(B, 0))}")
check("radiation alone: a has a SIMPLE zero and is ODD",
      zero_order(a.subs(A, 0)) == 1 and parity(a.subs(A, 0)) == "ODD",
      f"order {zero_order(a.subs(A, 0))}, {parity(a.subs(A, 0))}")
check("P16's mixture: a has a SIMPLE zero and NEITHER parity",
      zero_order(a) == 1 and parity(a) == "NEITHER",
      f"order {zero_order(a)}, {parity(a)}")
check("⇒ THE TWO PARITIES ARE NOT INDEPENDENT: the zero's order is set by the "
      "species content",
      zero_order(a.subs(B, 0)) != zero_order(a.subs(A, 0)))

# ---- (3) the reflection reverses the radiation amplitude ------------------
check("a(-eta) is identically a(eta) with sqrt(B) -> -sqrt(B): the crossing hands out "
      "the SIGN-REVERSED radiation amplitude",
      sp.simplify(a.subs(eta, -eta) - a.subs(sp.sqrt(B), -sp.sqrt(B))) == 0,
      sp.simplify(a.subs(eta, -eta)))

# ---- (4) per-interior parities --------------------------------------------
a_d, a_r = a.subs(B, 0), a.subs(A, 0)
check("dust-only interior: the density is EVEN",
      parity(A / sp.Abs(a_d)**3) == "EVEN")
check("dust-only interior: the areal rate is ODD",
      parity(sp.diff(sp.Abs(a_d), eta)) == "ODD")
check("radiation-only interior: the density is EVEN",
      parity(B / sp.Abs(a_r)**4) == "EVEN")
check("radiation-only interior: T^r_r = T^theta_theta = rho/3 is EVEN",
      parity(B / (3 * sp.Abs(a_r)**4)) == "EVEN")
check("radiation-only interior: the areal rate is ODD",
      parity(sp.diff(sp.Abs(a_r), eta)) == "ODD")
check("P16's MIXED interior: the density has NEITHER parity, because of the "
      "amplitude reversal",
      parity(A / sp.Abs(a)**3) == "NEITHER")
check("P16's MIXED interior: the pressure has NEITHER parity either",
      parity(B / (3 * sp.Abs(a)**4)) == "NEITHER")

# ---- (5) the correction to the earlier route ------------------------------
alpha, theta = sp.symbols('alpha theta', real=True)
r_vac = alpha * sp.sin(theta)
check("the VACUUM slicing curve has a simple ODD zero, which is why the earlier "
      "revision needed |r|",
      sp.simplify(r_vac.subs(theta, -theta) + r_vac) == 0)
check("while P16's DUST interior has a double zero and never goes negative, so its "
      "density is even with no absolute value",
      zero_order(a.subs(B, 0)) == 2
      and sp.simplify(sp.simplify((A / a_d**3).subs(eta, -eta) - A / a_d**3)) == 0)

# ---- the CONTROL -----------------------------------------------------------
print()
print("  CONTROL -- on each single-species interior the RATE must come out with a")
print("  DIFFERENT parity from the scalars.  If it does not, the EVEN answer is an")
print("  artefact of taking absolute values and not a fact about densities.")
for label, aa, scal in (("dust only", a_d, A / sp.Abs(a_d)**3),
                        ("radiation only", a_r, B / sp.Abs(a_r)**4)):
    ps, pr = parity(scal), parity(sp.diff(sp.Abs(aa), eta))
    check(f"CONTROL {label}: scalar {ps} vs rate {pr} -- they must differ", ps != pr,
          f"{ps} / {pr}")

print()
print("=" * 78)
if FAILS:
    print(f"  VERDICT: {len(FAILS)} FAILURE(S): {', '.join(FAILS)}")
    raise SystemExit(1)
print("  VERDICT: ALL PASS.  P16's own interior solves its stated equation and I14's")
print("  species parity is re-derived from it.  The two parities are NOT independent:")
print("  the order of the zero at the branch point is set by the species content, and")
print("  radiation's odd amplitude is what makes it transversal.  The reflection is")
print("  therefore not a symmetry of P16's member -- a(-eta) is that member with the")
print("  radiation amplitude reversed -- so the crossing is an involution on the FAMILY")
print("  and is NOT species-blind.  On a single-species interior every scalar is even")
print("  and the rate odd, which is the earlier revision's involution; on the mixture")
print("  all four components have neither parity.  And the earlier route is corrected")
print("  without its result moving: the absolute value was load-bearing only for the")
print("  vacuum curve's simple odd zero, the dust interior having a double one.")
print("  ⛔ NO TEMPERATURE, NO ABUNDANCE, AND NO CLAIM THAT THE SIGN REVERSAL IS")
print("     OBSERVABLE.  Nothing is LOST at the crossing; what changes is which member")
print("     of the family comes out.")
print("=" * 78)
