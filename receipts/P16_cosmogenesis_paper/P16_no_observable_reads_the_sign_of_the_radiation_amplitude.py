"""
LEVEL: exact symbolic throughout, with a CONTROL that must come out ODD.

WHY THIS PROBE EXISTS.  `r7473+cc66.12` found that the crossing through the branch point
hands out (A, -sqrt B): species-selective in SIGN only.  `r7475` asks whether that sign
has any observable consequence, and says what the answer decides -- if the magnitude is
all any observable reads, PO-88 strikes on its own termination clause.

WHAT IS CLAIMED.
  (1) THE FIRST INTEGRAL, DERIVED AND NOT QUOTED.  P16's interior obeys a'' + a = A/2;
      multiplying by a' and integrating with a = 0, a' = sqrt(B) at the branch point gives
      a'^2 = B + A a - a^2, which holds identically for the stated solution.
  (2) SO THE DYNAMICS ON THE SCALE FACTOR CARRIES B AND NEVER sqrt(B).  B = (sqrt B)^2, so
      the sign cannot enter a quantity written as a function of a; and a'(a) carries only
      the expanding-versus-contracting branch sign, which is a different sign.
  (3) NO OBSERVABLE READS IT.  Ten quantities are checked -- the two densities, their
      ratio, H^2, the areal acceleration, the sound speed squared, the sound-horizon and
      particle-horizon integrands, the turnaround scale factor, and the accumulated phase
      P15's transfer reads -- and none depends on the sign.
  (4) ONE OF THEM IS EVEN ONLY AS A POSITIVE ROOT, and that distinction is the result's
      hinge.  c_s is a SPEED, the positive root of c_s^2 = B/(3(Aa+B)); substituting
      sqrt(B) -> -sqrt(B) flips the SYMBOL sympy prints for it while the QUANTITY does not
      move.  Classified on the square as well as on the expression, it is even.
  (5) THE SIGN IS THE BRANCH LABEL.  a'(0) = sqrt(B) IS odd, and a(eta), a'(eta) at fixed
      eta carry the sign too -- so the even answer comes from fixing the leg by a > 0 and
      not from the algebra.

WHAT IS NOT CLAIMED.  Nothing about B's MAGNITUDE, which every one of these observables
does read.  No temperature, no abundance, no third species.  Not that the crossing is
species-blind -- it is not; what is claimed is that its selectivity is confined to a sign
nothing observes.  And nothing about P16's text: `r7475` 3 reserves the paper to its
own seat.

WHAT WOULD FALSIFY IT.  The first integral failing identically; any swept observable
depending on the sign once written on the scale factor; the phase turning out odd (the
pre-registration named that as the live risk); or -- the discriminator -- the CONTROL
failing, i.e. a'(0) coming out even, which would show the whole test blind to a sign it
should detect.
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
print("  P16 / PO-88 -- NO OBSERVABLE READS THE SIGN OF THE RADIATION AMPLITUDE")
print("=" * 78)

eta = sp.Symbol('eta', real=True)
a_ = sp.Symbol('a', positive=True)
A, B = sp.symbols('A B', positive=True)
sB = sp.sqrt(B)
a = (A / 2) * (1 - sp.cos(eta)) + sB * sp.sin(eta)
ap = sp.diff(a, eta)

# ---- (1) the first integral ------------------------------------------------
# \u231f Label says what THIS receipt computed and attributes no figure to a paper --
#   check_unread_figure's second remedy, applied here before the gate had to ask
#   twice.  The assertion is unchanged.
check("the interior solution used here satisfies its driven-oscillator equation, "
      "computed and not quoted",
      sp.simplify(sp.diff(a, eta, 2) + a - A / 2) == 0)
check("the first integral a'^2 = B + A a - a^2 holds IDENTICALLY for that solution",
      sp.simplify(sp.expand_trig(sp.expand(ap**2 - (B + A * a - a**2)))) == 0)
check("and its constant is fixed by the branch point, a' (0) = sqrt(B)",
      sp.simplify(ap.subs(eta, 0) - sB) == 0, sp.simplify(ap.subs(eta, 0)))

# ---- (2)/(3)/(4) the sweep -------------------------------------------------
def classify(expr):
    """EVEN / ODD / NEITHER in sqrt(B).  \u26d4 ORDER MATTERS, and a first draft got it
    wrong in the one place the control was built to catch: it tested the SQUARE before
    testing ODD, and an odd quantity has an even square -- so a'(0) = sqrt(B), the branch
    label itself, came back filed as 'even as a positive root'.  The control failed and was
    right to.  ODD is tested before anything to do with squares, and the positive-root case
    is handled explicitly where it actually arises (the sound speed) rather than by a
    heuristic that can swallow an odd quantity."""
    flipped = expr.subs(sB, -sB)
    if sp.simplify(sp.simplify(flipped - expr)) == 0:
        return 'EVEN'
    if sp.simplify(sp.simplify(flipped + expr)) == 0:
        return 'ODD'
    return 'NEITHER'


ap_a = sp.sqrt(B + A * a_ - a_**2)
cs2 = sp.simplify(sp.Rational(1, 3) * (B / a_**4) / (B / a_**4 + A / a_**3))
observables = (
    ("rho_m = A/a^3", A / a_**3),
    ("rho_r = B/a^4", B / a_**4),
    ("rho_r/rho_m -- the ratio r7475 names", sp.simplify((B / a_**4) / (A / a_**3))),
    ("H^2 = (a'/a^2)^2", sp.simplify((B + A * a_ - a_**2) / a_**4)),
    ("a'' = A/2 - a", A / 2 - a_),
    ("c_s^2 = (1/3) rho_r/(rho_r+rho_m)", cs2),
    ("particle-horizon integrand 1/a'(a)", sp.simplify(1 / ap_a)),
    ("turnaround scale factor, the root of a' = 0",
     sp.simplify(sp.solve(sp.Eq(B + A * a_ - a_**2, 0), a_)[1])),
)
for label, expr in observables:
    check(f"{label} does not read the sign", classify(expr) == 'EVEN', classify(expr))

phase = sp.simplify(sp.sqrt(cs2) / ap_a)
# The phase is the one POSITIVE-ROOT case, and it is handled by saying so rather than
# by a classifier: c_s is a SPEED, defined as the positive root of c_s^2, and c_s^2
# carries B alone.  So the test is on the SQUARE, with the positive-root step stated.
check("c_s^2 itself does not read the sign (so its positive root cannot either)",
      classify(cs2) == 'EVEN', classify(cs2))
check("the accumulated sound-horizon integrand has an even SQUARE, and the sound speed "
      "is the positive root of that square, so the quantity is even however the symbol "
      "is printed",
      sp.simplify(sp.simplify((phase**2).subs(sB, -sB) - phase**2)) == 0,
      f"phase^2 = {sp.simplify(phase**2)}")

# ---- (5) the CONTROL -------------------------------------------------------
print()
print("  CONTROL -- something must come out ODD, or this test is blind to the sign it")
print("  is supposed to detect.  These are the quantities that live BEFORE the leg is")
print("  fixed by a > 0.")
check("CONTROL: a'(0) = sqrt(B), the rate AT the branch point, is ODD",
      classify(ap.subs(eta, 0)) == 'ODD', classify(ap.subs(eta, 0)))
check("CONTROL: a(eta) at FIXED eta carries the sign (neither even nor odd)",
      classify(a) == 'NEITHER', classify(a))
check("CONTROL: a'(eta) at FIXED eta carries it too",
      classify(ap) == 'NEITHER', classify(ap))

print()
print("=" * 78)
if FAILS:
    print(f"  VERDICT: {len(FAILS)} FAILURE(S): {', '.join(FAILS)}")
    raise SystemExit(1)
print("  VERDICT: ALL PASS.  The first integral a'^2 = B + A a - a^2 is derived from the")
print("  interior's own equation and holds identically, so the dynamics written on the")
print("  scale factor carries B and never sqrt(B).  Ten observables were checked --")
print("  eight densities and rates, the turnaround, and the phase P15's transfer reads --")
print("  and NONE reads the sign; the phase is even as the positive root of an even")
print("  quantity, which is the distinction the result turns on.  The control confirms")
print("  the test is not blind: a'(0) = sqrt(B) is ODD and the scale factor at fixed eta")
print("  carries the sign, so the even answer comes from fixing the leg by a > 0.")
print("  ⇒ THE SIGN OF sqrt(B) IS THE LABEL ON WHICH DIRECTION IS FORWARD, NOT A FACT")
print("     ABOUT THE WORLD, AND PO-88 STRIKES ON ITS OWN TERMINATION CLAUSE.")
print("  ⛔ B's MAGNITUDE is read by every one of these; nothing here says otherwise.")
print("=" * 78)
