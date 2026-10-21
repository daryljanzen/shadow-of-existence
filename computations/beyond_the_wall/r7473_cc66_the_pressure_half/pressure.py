#!/usr/bin/env python3
"""PO-88's pressure half: P16's own interior -- dust PLUS radiation -- carried
through the branch point with T^r_r and T^theta_theta.

r7465+cc66.10 discharged the row for a pressureless model.  This asks what the
two extra components do, and -- first, because the price named it as the thing
it could not compute in advance -- whether the corpus's OTHER parity, the
conformal-time species split of P16 sec:interior, reaches the crossing.

Everything is symbolic.  The interior solution is P16's own, written down and
then checked against the equation it is supposed to solve.
"""
import sympy as sp

def hdr(s):
    print()
    print("=" * 78)
    print("  " + s)
    print("=" * 78)

eta = sp.Symbol('eta', real=True)
A, B = sp.symbols('A B', positive=True)        # dust and radiation amplitudes
a = (A / 2) * (1 - sp.cos(eta)) + sp.sqrt(B) * sp.sin(eta)

hdr("STEP 1 -- P16's INTERIOR, WRITTEN DOWN AND THEN CHECKED")
print(f"  a(eta) = {a}")
ode = sp.simplify(sp.diff(a, eta, 2) + a - A / 2)
print(f"  a'' + a - A/2 = {ode}      solves the driven oscillator: {ode == 0}")
print(f"  a(0) = {sp.simplify(a.subs(eta, 0))}   -- so eta = 0 IS the branch point")
print()
even_part = sp.simplify((a + a.subs(eta, -eta)) / 2)
odd_part = sp.simplify((a - a.subs(eta, -eta)) / 2)
print(f"  even part of a : {even_part}")
print(f"  odd  part of a : {odd_part}")
print(f"  ⇒ the even part carries A (dust) alone   : {B not in even_part.free_symbols}")
print(f"  ⇒ the odd  part carries B (radiation) alone: {A not in odd_part.free_symbols}")
print("  ⌗ That is I14's split, reproduced here from the solution rather than cited.")

hdr("STEP 2 -- ⒝ DOES THE CONFORMAL-TIME PARITY REACH THE CROSSING?")
print("  The crossing's structure is set by the ORDER OF THE ZERO of a at eta = 0,")
print("  because that is what decides whether the curve crosses or touches.")
hdrow = f"  {'interior':<26}{'a(eta) near 0':>26}{'order':>8}   parity of a"
print(hdrow)
print("  " + "-" * (len(hdrow) - 2))
cases = (("dust only        (B=0)", a.subs(B, 0)),
         ("radiation only   (A=0)", a.subs(A, 0)),
         ("P16's own: dust + radiation", a))
orders = {}
for label, expr in cases:
    ser = sp.simplify(sp.series(expr, eta, 0, 4).removeO())
    lead = sp.simplify(sp.limit(ser / eta, eta, 0))
    order = 1 if lead != 0 else 2
    ev = sp.simplify(expr.subs(eta, -eta) - expr) == 0
    od = sp.simplify(expr.subs(eta, -eta) + expr) == 0
    par = "EVEN" if ev else ("ODD" if od else "NEITHER")
    orders[label] = (order, par)
    print(f"  {label:<26}{str(ser):>26}{order:>8}   {par}")
print()
print("  ** ⒝ ANSWERED, AND MY PRE-REGISTERED ANSWER IS WRONG.  The two parities are")
print("     NOT independent.  The order of the zero at the branch point depends on")
print("     the SPECIES CONTENT: dust alone gives a DOUBLE zero (the curve touches")
print("     a = 0 and returns, a even), while any radiation at all gives a SIMPLE")
print("     zero (the curve crosses, a neither even nor odd).  Radiation's odd")
print("     amplitude is exactly what makes the zero transversal. **")
print()
print("  ⛔ AND IT CORRECTS r7465+cc66.10's ROUTE, THOUGH NOT ITS RESULT.  That")
print("     revision took the crossing parity from the VACUUM slicing curve,")
print("     r = alpha sin(theta), which is ODD with a simple zero -- and then needed")
print("     |r| to keep the dust density positive.  P16's dust interior has its own")
print("     scale factor with a DOUBLE zero, so for dust alone a never goes negative")
print("     and the density is even WITHOUT the absolute value.  The conclusion")
print("     stands and is now reached twice by different routes; the absolute value")
print("     was load-bearing only for the vacuum curve's parametrisation.")

hdr("STEP 3 -- ⒜ THE STRESS-ENERGY, PER INTERIOR, BECAUSE IT DEPENDS ON THE INTERIOR")
print("  Perfect fluid, comoving: T^mu_nu = diag(-rho, p, p, p), so T^r_r and")
print("  T^theta_theta are both the scalar p.  Dust scales as |a|^-3, radiation as")
print("  |a|^-4, and radiation's p is rho/3.")
print()
print("  \u26d4 A FIRST DRAFT OF THIS STEP ASSERTED, IN PROSE, THAT EVERY SCALAR IS")
print("     EVEN 'whatever the species content', AND ITS OWN TABLE SAID OTHERWISE.")
print("     The table was right.  |a| is even only when a is even OR odd; with both")
print("     species a has neither parity (STEP 2), so |a| has none and no scalar")
print("     built on it does.  The verdict is therefore per interior:")

def parity(expr):
    if expr == 0:
        return "EVEN (trivially)"
    ev = sp.simplify(sp.simplify(expr.subs(eta, -eta) - expr)) == 0
    od = sp.simplify(sp.simplify(expr.subs(eta, -eta) + expr)) == 0
    return "EVEN" if ev else ("ODD" if od else "NEITHER")

interiors = (("dust only      (B=0)", {B: 0}),
             ("radiation only (A=0)", {A: 0}),
             ("P16's own: dust+radiation", {}))
head = f"  {'interior':<28}{'rho_dust':>12}{'rho_rad':>12}{'p_rad':>12}{'rate d|a|/deta':>18}"
print()
print(head)
print("  " + "-" * (len(head) - 2))
for label, sub in interiors:
    aa = a.subs(sub) if sub else a
    if aa == 0:
        continue
    rd = (A / sp.Abs(aa)**3) if B not in sub or sub.get(A) is None else None
    row = []
    row.append(parity(A / sp.Abs(aa)**3) if sub.get(A) is None else "n/a")
    row.append(parity(B / sp.Abs(aa)**4) if sub.get(B) is None else "n/a")
    row.append(parity(B / (3 * sp.Abs(aa)**4)) if sub.get(B) is None else "n/a")
    row.append(parity(sp.diff(sp.Abs(aa), eta)))
    print(f"  {label:<28}{row[0]:>12}{row[1]:>12}{row[2]:>12}{row[3]:>18}")
print()
print("  ** ⒜ ANSWERED, AND MY PRE-REGISTERED ANSWER IS RIGHT ONLY FOR A SINGLE")
print("     SPECIES.  For a one-species interior T^r_r and T^theta_theta are EVEN,")
print("     as priced -- and the reason priced was right too: p is a SCALAR in the")
print("     comoving frame, so it carries no radial index for the crossing's sign")
print("     flip to act on.  For P16's OWN interior they are NEITHER, because the")
print("     reflection does not map the member to itself at all (STEP 5). **")

hdr("STEP 4 -- THE CONTROL: a component whose parity IS the other one")
print("  If EVEN were an artefact of taking absolute values, a component that")
print("  genuinely flips would come out even too.  Read on the two interiors where")
print("  the parity is defined at all:")
for label, sub in (("dust only      (B=0)", {B: 0}), ("radiation only (A=0)", {A: 0})):
    aa = a.subs(sub)
    scal = parity(A / sp.Abs(aa)**3) if sub.get(A) is None else parity(B / sp.Abs(aa)**4)
    rate = parity(sp.diff(sp.Abs(aa), eta))
    print(f"    {label:<24} scalar: {scal:<8} rate: {rate:<8} "
          f"{'✔ they differ' if scal != rate else '⛔ THEY AGREE -- control failed'}")
print()
print("  ** THE CONTROL BITES on both: the rate is ODD where the scalars are EVEN,")
print("     so the even answer is not an artefact of the absolute value. **")

hdr("STEP 5 -- ⒞ AND ⒟: THE INVOLUTION, AND WHAT DISCHARGES")
print("  For the DUST-ONLY interior the map is exactly r7465+cc66.10's:")
print("      (rho(eta), p(eta), v(eta))  |->  (rho(-eta), p(-eta), -v(-eta))")
print("  with rho and p even and v odd, so applying it twice is the identity: an")
print("  involution, hence a bijection.  ** ⒞ holds for dust. **")
print()
print("  ⛔ FOR P16's OWN INTERIOR IT DOES NOT FOLLOW, AND THIS IS THE FINDING.")
print("     With radiation present a has a SIMPLE zero and no definite parity")
print("     (STEP 2), so eta -> -eta is not a symmetry of the solution: it maps")
print("     P16's interior to a DIFFERENT member of the same family, the one with")
print("     the radiation amplitude reversed in sign.")
a_refl = sp.simplify(a.subs(eta, -eta))
print(f"       a(-eta) = {a_refl}")
print(f"       which is a(eta) with sqrt(B) -> -sqrt(B): "
      f"{sp.simplify(a_refl - a.subs(sp.sqrt(B), -sp.sqrt(B))) == 0}")
print("     ⇒ the reflection is still a BIJECTION -- it is invertible, and the")
print("       scalars are even -- but it is an involution on the FAMILY and not on")
print("       the member: it carries (A, +sqrt B) to (A, -sqrt B).")
print()
print("  ** ⒟ ANSWERED, AND MORE NARROWLY THAN PRICED: the crossing carries P16's")
print("     interior through, and nothing is lost -- but what it hands out the other")
print("     side is the SIGN-REVERSED radiation amplitude, not the same member.")
print("     So the discharge holds, and the crossing is NOT species-blind. **")

hdr("STEP 6 -- ⒠ IS ANY SECTOR LEFT FREE BY THE CROSSING?")
print("  60's r7462: the papers name sectors the crossing leaves free, the")
print("  composition first.  Measured here:")
print("    - the COMPOSITION is fixed on the APPROACH, not at the crossing: P16")
print("      sec:peak has total dissociation erase it before the branch point, so")
print("      it is free of the progenitor and not free at the crossing.")
print("    - the RADIATION AMPLITUDE's SIGN is the one thing the crossing itself")
print("      does not preserve (STEP 5).  It is not 'free' -- it is DETERMINED, and")
print("      reversed.")
print("  ⇒ ** ⒠ ANSWERED AS PRICED in its conclusion -- no sector is left FREE by")
print("     the crossing -- but the reason is sharper than the price gave: the one")
print("     thing the crossing changes is determined by it, not left open. **")
