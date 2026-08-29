#!/usr/bin/env python3
"""RECEIPT — algebraic-geometry bake `AG1`: ** THE SLICING DISCRIMINANT AND THE HORIZON CUBIC'S ARE
NOT TWO NAMES FOR ONE THING AND NOT TWO UNRELATED THINGS. THEY ARE THE TWO FACTORS OF THE CLASSICAL
DISCRIMINANT FORMULA FOR A REDUCIBLE PLANE CURVE, AND THE CORPUS COMPUTES BOTH AND NAMES NEITHER. **

LEVEL: NO RATE — pure algebra on the horizon cubic's reducible factoring.

WHERE THIS CAME FROM.  The catastrophe gather (r3546) flagged `Q5`'s row as PREMISE WRONG IN ITS
  WORDING: it called Nariai the singular point of the "discriminant locus / bifurcation set", both
  x0 corpus-wide, and attributed to `P03` a discriminant -- 4 - 3 r_0^2, of the SLICING PARAMETER --
  that is not the horizon cubic's Delta = 4 - 27(2M)^2.  59 then found the same conflation live
  inside its own r3547 `P3` landing and repaired the paper.  ** This receipt is the algebra under
  that repair, so the relation is checked rather than recalled. **

THE FACTORING THE CORPUS ALREADY STATES.  `P03` and `P12` both give the horizon cubic in reducible
  form as a LINE times a CONIC:

        r^3 - r + 2M  =  (r - r_0) (r^2 + r r_0 + r_0^2 - 1),      2M = r_0 (1 - r_0^2)

THE TWO DEGENERATIONS, and they are geometrically different events:
  (1) THE CONIC'S OWN TWO ROOTS COLLIDE.  Its discriminant in r is exactly ** 4 - 3 r_0^2 ** --
      which IS `P03`'s slicing discriminant, and that is why `P03` reads its three regimes off it.
  (2) THE LINE MEETS THE CONIC.  Substituting r = r_0 into the conic gives ** 3 r_0^2 - 1 **, which
      is the resultant Res(line, conic): it vanishes when the linear and quadratic factors share a
      root, a DIFFERENT way for the cubic to acquire a repeated root.

AND THE WHOLE CUBIC'S DISCRIMINANT IS THEIR PRODUCT, with the resultant SQUARED:

        disc(C) = disc(conic) * Res(line, conic)^2 = (4 - 3 r_0^2)(3 r_0^2 - 1)^2

  ** That is the textbook formula for the discriminant of a reducible plane curve, instanced here.
  The corpus computes both factors, in two different papers, and names neither the formula nor the
  resultant. **

WHY THE DISTINCTION IS LOAD-BEARING RATHER THAN PEDANTIC.  59's repair says the two "vanish together
  at Nariai and differ by an exact square", which is true AT NARIAI and is the right thing to have
  put in the paper.  ** But they are not the same vanishing condition. **  disc(C) has FOUR roots in
  r_0 and the slicing discriminant has TWO: the squared factor contributes r_0 = +-1/sqrt3, where
  4 - 3 r_0^2 = 3 and is nowhere near zero.  ⇒ *** So "the discriminant vanishes" is ambiguous in
  this corpus until you say WHICH, and a reader who takes them as interchangeable will read a
  line-meets-conic degeneration as a Nariai point. ***

ROUTED, NOT APPLIED.  The paper-side repair is 59's and is done.  What is owed, if anything, is the
  NAME: `resultant` is x0 across seventeen bodies, and the formula is the algebraic-geometry framing
  this bake exists to notice.

VERDICTS ARE ASSERTS.
"""
import sympy as sp

print("=" * 78)
print("  AG1 — the two discriminants, and the resultant between them")
print("=" * 78)

r, r0 = sp.symbols('r r_0')
line = r - r0
conic = r**2 + r * r0 + r0**2 - 1
cubic = sp.expand(line * conic)

# ── the factoring is the corpus's, and it must reproduce the horizon cubic ──────────────
twoM = sp.simplify(cubic.coeff(r, 0))
print(f"\n  (r - r_0)(r^2 + r r_0 + r_0^2 - 1) = {sp.collect(cubic, r)}")
print(f"  so 2M = {sp.factor(twoM)}")
assert sp.simplify(cubic - (r**3 - r + twoM)) == 0, \
    "the reducible form must BE the horizon cubic r^3 - r + 2M"
print("  ** VERDICT 1: the reducible form is the horizon cubic identically, with 2M = r_0(1-r_0^2). **")

# ── (1) the conic's own discriminant IS P03's slicing discriminant ──────────────────────
disc_conic = sp.factor(sp.discriminant(conic, r))
print(f"\n  (1) the CONIC's own discriminant in r : {disc_conic}")
assert sp.simplify(disc_conic - (4 - 3 * r0**2)) == 0, \
    "the conic's discriminant must be exactly P03's 4 - 3 r_0^2"
print("      = 4 - 3 r_0^2, which is P03's slicing discriminant.")

# ── (2) the resultant: the line meeting the conic ───────────────────────────────────────
res = sp.expand(sp.resultant(line, conic, r))
print(f"  (2) Res(line, conic)                  : {res}")
assert sp.simplify(res - sp.expand(conic.subs(r, r0))) == 0, \
    "the resultant of a monic linear factor with the conic is the conic evaluated at its root"
assert sp.simplify(res - (3 * r0**2 - 1)) == 0, "and it must be 3 r_0^2 - 1"
print("      = 3 r_0^2 - 1, and it vanishes exactly when the LINE meets the CONIC.")

# ── the classical formula, instanced ────────────────────────────────────────────────────
disc_cubic = sp.factor(sp.discriminant(cubic, r))
print(f"\n  disc(whole cubic)          : {disc_cubic}")
print(f"  disc(conic) * Res^2        : {sp.factor(disc_conic * res**2)}")
assert sp.simplify(disc_cubic - disc_conic * res**2) == 0, \
    "disc(C) = disc(conic) * Res(line, conic)^2 -- the reducible-curve discriminant formula"
print("  ** VERDICT 2: disc(C) = disc(conic) x Res(line,conic)^2 EXACTLY -- the textbook")
print("     discriminant formula for a reducible plane curve, instanced by the horizon cubic. **")

# ── and they are NOT the same vanishing condition ───────────────────────────────────────
z_slicing = sorted(sp.solve(4 - 3 * r0**2, r0), key=lambda x: float(x))
z_cubic = sorted(sp.solve(disc_cubic, r0), key=lambda x: float(x))
print(f"\n  zeros of the SLICING discriminant : {z_slicing}")
print(f"  zeros of the CUBIC's discriminant : {z_cubic}")
assert len(z_slicing) == 2 and len(z_cubic) == 4, \
    "the cubic's discriminant must have two roots the slicing one does not"
assert set(z_slicing) < set(z_cubic), "and the slicing zeros must be a PROPER subset"
extra = [z for z in z_cubic if z not in z_slicing]
for z in extra:
    val = sp.simplify((4 - 3 * r0**2).subs(r0, z))
    assert val != 0, "at the extra zeros the slicing discriminant must NOT vanish"
    print(f"      at r_0 = {z}: cubic disc = 0 but slicing disc = {val}, not zero")
print("  ** VERDICT 3: the two are NOT the same condition. The slicing zeros are a PROPER")
print("     subset, and the squared factor adds r_0 = +-1/sqrt3, where the slicing")
print("     discriminant equals 3. 'The discriminant vanishes' is ambiguous until you say")
print("     WHICH -- which is exactly the conflation r3547 repaired in P3. **")

print("\n" + "=" * 78)
print("  ALL PASS")
print("=" * 78)
