#!/usr/bin/env python3
"""P15 receipt -- `PO-84`, opened at `r7166` on this seat's own `r7170` finding and left unassigned:
** WHAT BECOMES OF A CHARGE WHOSE FIBRE DOES NOT SURVIVE? **
*taken on the row's own cheapest route, the charged SCALAR, which `r7166` names as where to start.*

*** ⛭⛭⛭ THE CHARGE IS CARRIED, AND THE CORPUS ALREADY NAMED WHERE -- SO THE ROW DISCHARGES ON ITS
    FIRST BRANCH AND NOT ITS SECOND.  FOUR THINGS:
      ⓵ THE READ FIRST, BECAUSE IT IS WHAT MAKES THE REST AN IDENTIFICATION RATHER THAN A GUESS.
         `sec:scope` already says it, once, in its own voice: the layer *\"does not carry its sphere
         through the seam; it becomes the throat's `$S^2$` there\"*, and ***the Hopf direction it
         gives up \"is the one the reassignment ... TRADES INTO `$\\chi$`\"***.  **So the fibre is not
         annihilated: it is traded, and the destination is already in print.**
      ⓶ AND THE DIVERGENCE THE CHARGED MODES SUFFER IS EXACTLY THAT TRADE.  The squashing vanishes
         LINEARLY at the double root -- slope `$3/\\alpha$`, measured -- so the charge term of
         `eq:squashed-spectrum` runs to infinity there; and the proper wavenumber along the traded
         direction, `$k^2/(-f)$`, runs to infinity at the same locus.  **Their ratio is
         `$4m^2r^2/\\alpha^2k^2$` -- FREE of `$(r-r_N)$` -- so the two diverge at exactly the same
         rate**, with the identification exact:

> ### the charge term IS the proper momentum squared of a mode with `$k=2mr/\\alpha$`

         ⇒ *** THE EIGENVALUE DIVERGENCE IS THE BLUESHIFT OF THE TRADED MOMENTUM.  Two descriptions
             of one fact, and the second one the construction supplies itself. ***
      ⓷ SO THE ANSWER IS: CARRIED IN LABEL, LOST IN AMPLITUDE.  The charge has a destination -- a
         momentum along the direction the reassignment trades the fibre into -- and what it does not
         have is a finite amplitude, because that direction's own block coefficient collapses at the
         double root.  *The row's second branch -- that the charge is simply not carried -- is the
         one this receipt declines, and it declines it with the destination named.*
      ⛭ ⓸ AND THE SURVIVING SECTOR IS THE ONE WITH NOTHING TO BLUESHIFT, WHICH IS THE SAME FACT A
         THIRD TIME.  `$m=0$` carries no momentum into the trade, so it is exactly the sector that
         descends -- already named twice over by the projection's integrality and by the parity
         rule.  ⌗ *And there is NO SMALL-CHARGE ESCAPE: the minimum nonzero charge is `$\\tfrac12$`
         at odd degree and `$1$` at even, never small -- and **at `$L=1$` the only admissible charge
         is `$\\tfrac12$`, so the entire first degree is charged** and none of it descends.* ***

⛭⛭⛭ ** ⓵ WHY THE READ COMES FIRST. **  *The row names two honest routes and this receipt takes both,
in the order the row puts them: read what the corpus already says about the reassignment that trades
the fibre away, then ask the question of a charged scalar.  **The read is what turns the second into
an identification**: without it the eigenvalue's divergence is a fact about a spectrum, and with it
the divergence has a destination to be the blueshift OF.*

⛭⛭ ** ⓶ AND THE IDENTIFICATION IS EXACT RATHER THAN ASYMPTOTIC. **  *Both quantities blow up at the
double root, which on its own proves nothing -- plenty of unrelated quantities do.  **What makes it
one object is that their RATIO is free of the distance to the root**, so they diverge at the same
rate with a finite coefficient, and solving for the wavenumber that equates them returns
`$k=2mr/\\alpha$` in closed form -- the Hopf charge converted by the horn normalisation.*
⌗ *The leading coefficients at the root, each measured: `$4\\alpha^2m^2/9$` for the charge term,
`$\\alpha^2/3$` for the inverse block coefficient, `$\\alpha^2/9$` for the inverse squashing squared.*

⛭ ** ⓷ WHAT THAT MAKES THE ANSWER, STATED SO IT CANNOT BE READ AS EITHER EXTREME. **
*It is NOT \"the charge vanishes\" -- it has a destination and the destination is in print.  It is NOT
\"the charge is transported\" in any sense that preserves an amplitude -- the destination's scale
factor collapses, so the mode's proper momentum runs to infinity and its suppression with it.*
⇒ *** CARRIED IN LABEL, LOST IN AMPLITUDE: the bookkeeping closes and the amplitude does not. ***

⌗ ** AND THE SIZE, SO THE DIVERGENCE IS NOT TAKEN ON FAITH. **  *The charged integrand exceeds the
neutral one by one full power of the squashing, `$2m/(\\varepsilon\\sqrt{L(L+2)})$`, and at `$L=1$`
with the minimum charge it passes a factor of `2` at `$\\varepsilon=0.316$`, `10` at `$0.0579$` and
`100` at `$0.00577$`.*  ⇒ *So the effect turns on well before the collapse rather than only in its
limit.*

⛔ ** WHAT THIS DOES NOT CLAIM. **  *It does not compute an exponent or a transmission figure on the
seam approach: the seam lies at infinite parameter and that is `r7156`'s result, not re-derived
here.*  ⛔ *It does not claim the trade is a diffeomorphism or that the two descriptions are related
by a coordinate change -- `sec:scope` says the opposite and this receipt reasons FROM that, taking
the trade as the reassignment the paper already asserts.*  ⛔ *It does not treat the tensor or vector
sectors: the row names the scalar as where it is cheapest and this is the scalar.*  ⛔ *It does not
claim the charged modes are absent from the progenitor's spectrum, only that this transport does not
deliver their amplitude.*  ⛔ *`$L$` is the layer degree and is not the observable multipole.*

⌗ ** THE GUARD THIS ONE LEAVES. **
> **When a quantity diverges where a structure degenerates, look for what the construction traded
> that structure FOR before concluding the quantity is lost.**  *Two things diverging at one locus
> is not an identification; their ratio being free of the distance to it is.  Here the destination
> was already one sentence in the paper, and the measurement only had to meet it.*
"""
import os
import re
import time

import sympy as sp

t_all = time.time()
CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def head(t):
    print("\n  " + "=" * 74 + f"\n  {t}\n  " + "=" * 74, flush=True)


def flat(t):
    """one line, comment markers stripped -- a quotation the source WRAPS is the same quotation."""
    return re.sub(r'\s+', ' ', re.sub(r'(?m)^\s*#\s?', '', t))


def body_of(path):
    src = open(path, encoding='utf-8').read()
    return flat(''.join(ln + '\n' for ln in src.splitlines() if not ln.lstrip().startswith('%')))


print(__doc__)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
b15 = body_of(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'))

# ------------------------------------------------------------- Ⓐ the read
head("Ⓐ  THE READ FIRST -- THE DESTINATION IS ALREADY IN PRINT, WHICH IS WHAT THE REST MEETS")

_TRADE = 'the Hopf direction it gives up is the one the reassignment of'
_BASE = 'degenerates onto its Hopf base rather than shrinking'
_SHAPE = "the layer's SIZE continues across the lap with it; its SHAPE does not"
gate("Ⓐ①  the paper says the fibre is TRADED and not annihilated, once, in its own voice -- the Hopf"
     " direction it gives up is the one the reassignment trades into the other block",
     b15.count(_TRADE) == 1)
gate("Ⓐ②  and it says what the degeneration does: the three-sphere descends onto its Hopf base"
     " rather than shrinking, once", b15.count(_BASE) == 1)
gate("Ⓐ③  with the size/shape split stated once as well, which is what makes the surviving factor a"
     " definite object rather than a limit of nothing", b15.count(_SHAPE) == 1)
gate("Ⓐ④  so this row's destination is READ rather than posited, and the computation below only has"
     " to meet it", b15.count(_TRADE) == 1 and b15.count(_BASE) == 1)

# ------------------------------------------------------------- Ⓑ the collapse and the spectrum
head("Ⓑ  THE FIBRE COLLAPSES LINEARLY, AND THE CHARGE TERM DIVERGES THERE")

r, al, m, k = sp.symbols('r alpha m k', positive=True)
L = sp.Symbol('L', positive=True)
e = sp.Symbol('varepsilon', positive=True)
rN = al / sp.sqrt(3)
mf = sp.simplify((r - rN)**2 * (r + 2 * rN) / (al**2 * r))
eps = sp.simplify(al * sp.sqrt(mf) / r)

gate("Ⓑ①  the block coefficient has its double root at the seam radius, derived from the factorised"
     " form rather than asserted",
     sp.simplify(mf.subs(r, rN)) == 0 and sp.simplify(sp.diff(mf, r).subs(r, rN)) == 0)
slope = sp.simplify(sp.limit(eps / (r - rN), r, rN))
print(f"\n    the squashing vanishes linearly at the double root, slope {slope}")
gate("Ⓑ②  and the squashing vanishes LINEARLY there with slope 3/α -- so the fibre closes at a"
     " finite rate rather than asymptotically", sp.simplify(slope - 3 / al) == 0)

lam = L * (L + 2) + 4 * (1 / e**2 - 1) * m**2
gate("Ⓑ③  the layer spectrum's charge dependence is through the charge SQUARED only, so the neutral"
     " sector carries no squashing at all -- which is r7160's result, re-used and not re-derived",
     sp.simplify(lam.subs(m, 0) - L * (L + 2)) == 0
     and sp.simplify(sp.diff(lam, m).subs(m, 0)) == 0)
gate("Ⓑ④  so every charged mode's eigenvalue runs to infinity as the fibre closes, and the neutral"
     " one's does not move",
     sp.limit(lam.subs({L: 1, m: sp.Rational(1, 2)}), e, 0, '+') == sp.oo
     and sp.simplify(sp.limit(lam.subs(m, 0), e, 0, '+') - L * (L + 2)) == 0)

print("\n    the admissible charges and the minimum NONZERO one, by degree:")
floors = []
for Lv in range(1, 7):
    ms = sorted({abs(sp.Rational(Lv, 2) - j) for j in range(Lv + 1)})
    nz = [x for x in ms if x != 0]
    floors.append((Lv, min(nz)))
    print(f"      L={Lv}: |m| in {[str(x) for x in ms]}   min nonzero {min(nz)}")
gate("Ⓑ⑤  and there is NO SMALL-CHARGE ESCAPE: the minimum nonzero charge is one half at odd degree"
     " and one at even, never small",
     all(f == (sp.Rational(1, 2) if Lv % 2 else sp.Integer(1)) for Lv, f in floors))
gate("Ⓑ⑥  ⇒ AND AT THE FIRST DEGREE THE ONLY ADMISSIBLE CHARGE IS ONE HALF, so the ENTIRE first"
     " degree is charged and none of it descends -- the same fact r7172 met from the other side,"
     " where the descending sector was found to contain no first-degree mode",
     floors[0] == (1, sp.Rational(1, 2)))

# ------------------------------------------------------------- Ⓒ the identification
head("Ⓒ  AND THE DIVERGENCE IS THE TRADED MOMENTUM'S BLUESHIFT -- THE RATIO IS THE PROOF")

charge_term = sp.simplify(4 * m**2 / eps**2)
proper = sp.simplify(k**2 / mf)
ratio = sp.simplify(charge_term / proper)
print(f"\n    the charge term                  = {sp.factor(charge_term)}")
print(f"    the proper momentum squared      = k²/(−f)")
print(f"    their ratio                      = {sp.simplify(ratio)}")
gate("Ⓒ①  both quantities diverge at the double root, which on its own identifies nothing",
     sp.limit(charge_term.subs(m, 1), r, rN, '+') == sp.oo
     and sp.limit(proper.subs(k, 1), r, rN, '+') == sp.oo)
gate("Ⓒ②  but their RATIO is 4m²r²/α²k² -- FREE of the distance to the root -- so they diverge at"
     " exactly the same rate with a finite coefficient, which is what makes them one object",
     sp.simplify(ratio - 4 * m**2 * r**2 / (al**2 * k**2)) == 0
     and sp.simplify(sp.limit(ratio, r, rN) - 4 * m**2 / (3 * k**2)) == 0
     and sp.limit(ratio, r, rN) != 0 and sp.limit(ratio, r, rN) != sp.oo)
keq = [x for x in sp.solve(sp.Eq(charge_term, proper), k) if sp.simplify(x).is_positive is not False]
print(f"    the wavenumber that equates them = {[sp.simplify(x) for x in keq]}")
gate("Ⓒ③  and solving for the wavenumber that equates them returns k = 2mr/α in CLOSED FORM -- the"
     " Hopf charge converted by the horn normalisation, so the identification is exact rather than"
     " asymptotic",
     any(sp.simplify(x - 2 * m * r / al) == 0 for x in keq))
leads = {}
for nm, expr in [('charge term', charge_term), ('1/(-f)', 1 / mf), ('1/eps^2', 1 / eps**2)]:
    leads[nm] = sp.simplify(sp.limit(expr * (r - rN)**2, r, rN))
print("\n    leading coefficients of 1/(r−r_N)² at the root:")
for nm, v in leads.items():
    print(f"      {nm:<12} {v}")
gate("Ⓒ④  with all three leading coefficients in closed form in the throat constant and the charge,"
     " so the rate statement is measured and not estimated",
     sp.simplify(leads['charge term'] - 4 * al**2 * m**2 / 9) == 0
     and sp.simplify(leads['1/(-f)'] - al**2 / 3) == 0
     and sp.simplify(leads['1/eps^2'] - al**2 / 9) == 0)

# ------------------------------------------------------------- Ⓓ the size
head("Ⓓ  AND THE SIZE, SO THE DIVERGENCE IS NOT TAKEN ON FAITH")

integ = sp.simplify(sp.sqrt(lam / lam.subs(m, 0)))
print(f"\n    the charged-to-neutral integrand ratio, leading order as the fibre closes:"
      f" {sp.simplify(sp.limit(integ * e, e, 0, '+'))} / ε")
rows = []
for fac in [2, 10, 100]:
    sol = [s for s in sp.solve(sp.Eq(integ.subs({L: 1, m: sp.Rational(1, 2)}), fac), e)
           if s.is_real and s > 0]
    rows.append((fac, float(sol[0])))
    print(f"      a factor of {fac:>3} is passed at ε = {float(sol[0]):.6g}")
gate("Ⓓ①  the charged integrand exceeds the neutral one by one full power of the squashing",
     sp.simplify(sp.limit(integ * e, e, 0, '+') - 2 * m / sp.sqrt(L * (L + 2))) == 0)
gate("Ⓓ②  and at the first degree with the minimum charge it passes a factor of two at ε ≈ 0.316,"
     " ten at 0.058 and a hundred at 0.0058 -- so the effect turns on well before the collapse"
     " rather than only in its limit",
     abs(rows[0][1] - 0.3162) < 1e-3 and abs(rows[1][1] - 0.05793) < 1e-4
     and abs(rows[2][1] - 0.005774) < 1e-5)

# ------------------------------------------------------------- Ⓔ the paper, partitioned
head("Ⓔ  THE PAPER'S OWN CLAUSES, PARTITIONED")

gate("Ⓔ①  eq:squashed-spectrum's LABEL is in print exactly once -- the label and never its citation"
     " count", b15.count('\\label{eq:squashed-spectrum}') == 1)
gate("Ⓔ②  the scalar-half scoping clause is in print exactly once and is reasoned FROM",
     b15.count('the scalar half is here') == 1)
gate("Ⓔ③  and the basis clause scoped to the scalar sector is in print once, read here as the"
     " settled state it has",
     b15.count('For scalars the deformation reaches the spectrum and not the basis') == 1)
gate("Ⓔ④  the ONE clause this row's result bears on is ENUMERATED over the states the paper may"
     " produce -- either the trade stands as a geometric remark, or it has acquired this row's"
     " blueshift identification, or the carried-in-label reading is named beside it -- and the"
     " receipt's reading is unchanged in all three",
     b15.count(_TRADE) == 1 or 'blueshift' in b15 or 'carried in label' in b15)

# ------------------------------------------------------------- verdict
head("VERDICT")
npass = sum(1 for _, ok in CHECKS if ok)
print(f"  {npass} of {len(CHECKS)} gates pass.   [{time.time() - t_all:.1f}s]")
bad = [nm for nm, ok in CHECKS if not ok]
if bad:
    print("\n  FAILED:")
    for nm in bad:
        print(f"    - {nm}")
    raise SystemExit(1)
print("""
  ==========================================================================
  VERDICT: THE CHARGE IS CARRIED, AND THE CORPUS ALREADY NAMED WHERE -- so
  the row discharges on its FIRST branch, not its second.

  THE READ: the paper already says, once, that the layer does not carry its
  sphere through the seam but becomes the throat's two-sphere there, and that
  the Hopf direction it gives up is the one the reassignment TRADES into the
  other block.  So the fibre is traded, not annihilated, and the destination
  is in print.

  THE MEASUREMENT: the squashing vanishes linearly at the double root, slope
  three over the throat constant, so every charged mode's eigenvalue runs to
  infinity there while the neutral one's does not move.  And that divergence
  IS the trade: the charge term and the proper momentum squared along the
  traded direction have a ratio FREE of the distance to the root, so they
  diverge at the same rate, and the wavenumber equating them is 2mr/alpha in
  closed form -- the Hopf charge converted by the horn normalisation.

  *** SO THE ANSWER IS: CARRIED IN LABEL, LOST IN AMPLITUDE.  The charge has
      a destination and no finite amplitude, because the destination's own
      block coefficient collapses. ***

  AND THE SURVIVING SECTOR IS THE ONE WITH NOTHING TO BLUESHIFT -- the
  neutral modes carry no momentum into the trade, which is why they are the
  ones that descend, now named three times over.  There is no small-charge
  escape: the minimum nonzero charge is one half at odd degree and one at
  even, and at the first degree every mode is charged.

  THE GUARD: when a quantity diverges where a structure degenerates, look for
  what the construction traded that structure FOR before concluding the
  quantity is lost.  Two things diverging at one locus is not an
  identification; their ratio being free of the distance to it is.
  ==========================================================================
""")
