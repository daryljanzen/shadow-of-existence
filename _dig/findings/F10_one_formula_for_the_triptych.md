# F10 — One closed form gives the acceleration at all four marked loci of the lap, and turns the "order of contact" distinction into a root multiplicity

*status: OFFERED (a consequence of the caption's own cubic family). No number changes.*
*receipt: `DRAFT_P07_one_formula_for_the_triptych.py`, rc=0.*
*touches: P7 `fig:F-triptych` caption and `sec:lift-initial-rate`.*

---

## Where it came from

After F08 and F09 both turned quoted decimals into closed forms, I swept every decimal literal in
the seventeen papers — 137 of them — and triaged for ones that ought to close. The triptych
caption has three: **−1.299** (back-seam acceleration), **+1.969** (Euclidean-null acceleration),
and **−0.3441α** (the f=2 radius). It also already states the structure that determines them:

> *every unit-speed locus is a root of f(f−2)=0, **one cubic family r³ − cr + 2M = 0 in c = 1−f**:
> c=+1 gives the three-root Weyl triple whose real members are the seams, c=0 the turnaround, and
> c=−1 the Euclidean null.*

## The formula

From (dr/dτ̃)² = 1 − f, differentiating gives r'' = −f'/2 on the real segments; on the lift τ̃ = is,
so (dr/ds)² = f − 1 and the sign flips. Eliminating M with the locus's own cubic:

> **r'' = ε·(3r² − cα²)/(2rα²)**,  ε = +1 on the real segments, −1 on the lift

Verified symbolically (residual exactly 0), and checked against a finite-difference derivative of
the first integral taken independently.

| locus | c | r | r'' exact | numeric | paper |
|---|---|---|---|---|---|
| front seam | +1 | +α/√3 | **0** | 0.000000 | *"the acceleration vanishing"* |
| back seam | +1 | −2α/√3 | **−3√3/(4α)** | −1.299038 | −1.299 |
| turnaround | 0 | −(2Mα²)^{1/3} | **−(3/2)(2Mα²)^{1/3}/α²** | −1.091124 | *already in closed form* |
| Euclidean null | −1 | −0.344142α | **−(3r²+α²)/(2rα²)** | +1.969101 | +1.969 |

So the caption gives one of the four in closed form and quotes the other three as decimals — from
a family it has already written down.

## And the "order of contact" becomes an identity

This is the part worth having. The numerator vanishes exactly when **3r² = cα²**. At c = +1 that
is r = ±α/√3 — and the seam cubic at the forced member factors as

```
roots with multiplicity: { −2√3α/3 : 1,   √3α/3 : 2 }
```

> **The front seam is tangential because its radius is the one that also solves 3r² = α² — which
> is the Nariai radius, which is the doubled root. The back seam is transversal because
> −2α/√3 is not.**

The paper makes the two seams *"distinguished from one another not by the presence or absence of a
feature but by order of contact"* — the point of that passage. Stated through the formula it needs
no numbers at all:

> **order of contact with the null level = multiplicity of the root** — and the doubling is the
> same doubling that makes the member Nariai.

That is a third face for α/√3, alongside the two the corpus already reads there (the Nariai
horizon radius; the seam), and it arrives as a consequence rather than an observation.

## Recommended, stated for reversal

1. Give the formula in the caption (or the section) and let the four values fall out of it. It is
   one line and it replaces three decimals.
2. State the front seam's zero as a consequence of 3r² = α², not as a measured fact — and say that
   this is why the tangency is at the Nariai radius.
3. Say that the order of contact **is** the root multiplicity. It is the sharpest form of the
   distinction the passage is drawing, and the caption is already one step from it.

## Not claimed

- No new physics. The cubic family is the caption's own; this is its consequence.
- No number changes: −1.299 is −3√3/4 to the digits quoted; +1.969 is the c=−1 root's value to the
  digits quoted; the turnaround's closed form is already there.
- Nothing about what the lift *governs* — P7 marks that as worked in `sec:lift-initial-rate` and
  this does not touch it.
- **s/P = 0.78899 is not addressed.** It is a path-length fraction and needs the arclength
  integral, not the cubic. Left open deliberately rather than guessed at.
- No closure on any registered item.
