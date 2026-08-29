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

WHY THE DISTINCTION IS LOAD-BEARING RATHER THAN PEDANTIC.  disc(C) has FOUR roots in r_0 and the
  slicing discriminant has TWO: the squared factor contributes r_0 = +-1/sqrt3, where 4 - 3 r_0^2
  equals 3.  So "the discriminant vanishes" is ambiguous in this corpus until you say WHICH.

⛔⛭⛭ AND THE FIRST VERSION OF THIS RECEIPT GOT THE REASON WRONG -- CORRECTED r3560, BY 59 AT r3555.
  r3556 wrote that a reader taking the two as interchangeable "will read a LINE-MEETS-CONIC
  DEGENERATION as a Nariai point", which asserts that the extra zeros are not Nariai.  ** They are.
  All four are. **  Verified here rather than conceded:

      r_0 = +-1/sqrt3  ->  2M = -+2/(3 sqrt3),  roots (-1.1547, 0.57735, 0.57735), disc = 0
      r_0 = +-2/sqrt3  ->  2M = +-2/(3 sqrt3),  roots (-0.57735, -0.57735, 1.1547), disc = 0

  Every one of the four carries the Nariai mass exactly and leaves the cubic with a repeated root.
  ⇒ *** The four zeros are the four r_0-DESIGNATIONS of the two Nariai configurations, at the two
      signs of the mass. ***  And the two factors say WHICH root is designated at the merger:

      4 - 3 r_0^2 = 0   the CONIC's own two roots collide with each other, and the designated
                        root r_0 stands apart as the simple one.
      3 r_0^2 - 1 = 0   the designated root r_0 IS the repeated one -- it has collided with a
                        root of the conic.

  ** So the right reason to name which discriminant is meant is not that one set of zeros is not
  Nariai. It is that the slicing parameter's own discriminant MISSES HALF THE DESIGNATIONS at which
  Nariai is reached. **  ⌗ *A correct computation with a wrong gloss is still a wrong finding, and
  the gloss is the half a reader carries away.*

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
print("  ** VERDICT 3: the two are NOT the same condition -- the slicing zeros are a PROPER subset. **")

# ── AND ALL FOUR ARE NARIAI, which is what r3556 got wrong and 59 corrected at r3555 ────
NARIAI = 2 / (3 * sp.sqrt(3))
print("\n  and every one of the four zeros is a NARIAI configuration:")
for z in z_cubic:
    twoM = sp.radsimp(sp.simplify((r0 - r0**3).subs(r0, z)))
    poly = sp.Poly(sp.expand(r**3 - r + twoM), r)
    assert sp.simplify(sp.Abs(twoM) - NARIAI) == 0, \
        "every zero of disc(C) must carry the Nariai mass exactly"
    assert sp.simplify(sp.discriminant(poly.as_expr(), r)) == 0, \
        "and must leave the cubic with a repeated root"
    rts = [complex(x).real for x in poly.nroots(n=30)]
    dbl = [x for x in set(round(v, 12) for v in rts) if sum(abs(v - x) < 1e-9 for v in rts) > 1]
    designated_is_doubled = abs(dbl[0] - float(z)) < 1e-8
    slic = sp.simplify((4 - 3 * r0**2).subs(r0, z))
    print(f"      r_0 = {str(z):>12}: 2M = {float(twoM):+.7f} (Nariai), repeated root "
          f"{dbl[0]:+.6f}, r_0 IS it: {str(designated_is_doubled):>5}, slicing disc = {slic}")
    # ** the two factors say WHICH root is designated at the merger **
    if slic == 0:
        assert not designated_is_doubled, \
            "where the CONIC's discriminant vanishes, its own two roots collide and r_0 stands apart"
    else:
        assert designated_is_doubled, \
            "where the RESULTANT vanishes, the designated root r_0 is itself the repeated one"
print("  ** VERDICT 4: ALL FOUR ARE NARIAI. They are the four r_0-DESIGNATIONS of the two")
print("     Nariai configurations, at the two signs of the mass -- and the two factors say")
print("     WHICH root is designated at the merger: where 4-3r_0^2 vanishes the CONIC's own")
print("     roots collide and r_0 stands apart; where the resultant vanishes r_0 IS the")
print("     repeated root. So the reason to name which discriminant is meant is that the")
print("     slicing parameter's own MISSES HALF THE DESIGNATIONS, not that some are not")
print("     Nariai. ⛔ r3556 asserted the latter and was wrong; 59 corrected it at r3555. **")

print("\n" + "=" * 78)
print("  ALL PASS")
print("=" * 78)
