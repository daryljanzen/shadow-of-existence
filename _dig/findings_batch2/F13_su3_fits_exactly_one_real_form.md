# F13 — so(6,ℂ) has **four** real forms, and su(3) embeds in exactly one of them: the compact one. So "colour lives on the compact face" is forced by the group theory, not conceded against it

*status: OFFERED (a sharpening of one sentence's setup; the section's own argument is untouched).*
*receipt: `DRAFT_P13_su3_fits_exactly_one_real_form.py`, rc=0.*
*touches: P13 `sec:face-status`, first sentence; `P13_qm_S4_vs_S5` (rebuilt, not quoted).*

---

## The sentence

P13 `sec:face-status` opens the status question with a concession:

> *Mathematically the compact SO(6) face and the Lorentzian SO(5,1) substrate are co-equal real
> forms of the one complex group SO(6,ℂ); **nothing in the group theory privileges one**.*

and then breaks the tie **ontologically** — a Riemannian S⁵ has no timelike direction, no clock, no
duration, so by CR's existence criterion it is real-by-construction but not a co-equal *existent*.

**That argument is untouched by anything below and stays the section's load-bearing move.** What
changes is how much it has to concede first.

## so(6,ℂ) has four real forms, and the sentence weighs two

| real form | maximal compact | dim | su(3) fits? | why |
|---|---|---|---|---|
| **so(6) = su(4)** | su(4) *(the form is compact)* | 15 | **YES** | contains su(3) as a block |
| so(5,1) = su*(4) | sp(2) ≅ so(5) | 10 | no | 10 ≥ 8, but su(3) ⊄ so(5) |
| so(4,2) = su(2,2) | s(u(2)⊕u(2)) | 7 | no | 8 > 7 |
| so(3,3) = sl(4,ℝ) | so(4) | 6 | no | 8 > 6 |

Cartan: every compact subalgebra of a real semisimple Lie algebra is conjugate into a maximal
compact subalgebra. su(3) is compact of dimension 8, so it can only sit in a form whose maximal
compact admits it — and three of the four are ruled out by counting.

**The so(5,1) row is the one counting misses** (10 > 8), and it is settled by the corpus's own
fact, rebuilt in the receipt rather than quoted: su(3)'s smallest **faithful real** representation
has dimension **6** — the realification of the **3** — while so(5) acts faithfully on ℝ⁵. So su(3)
cannot act faithfully on ℝ⁵, hence is not in so(5), hence not in sp(2), hence not in so(5,1).
*(Corroborated: so(5)'s largest proper subalgebra is so(4) at dimension 6 < 8, so it has no
8-dimensional subalgebra at all.)*

Verified in the receipt by building su(3) ⊂ so(6) explicitly — 8 anti-Hermitian Gell-Mann
generators realified to ℝ⁶, all antisymmetric, linearly independent, closing on their own brackets.

> **Exactly one of the four. And it is the compact one.**

## What that does to the section

The sentence *"nothing in the group theory privileges one"* is true of the two forms taken **as
forms** — they are co-equal real forms of one complexification, and no group-theoretic fact ranks
them. It is **false once the question is where su(3) can live**, which is the question the section
is about.

So the section currently concedes a symmetric starting position and imports the asymmetry from
outside. It does not have to concede that much:

> **Colour and duration are not merely in different places. They are in the only places available
> to them, and those places are disjoint.** Colour can live in exactly one real form of so(6,ℂ);
> duration can live in any form carrying a timelike direction, which that one is not.

That is a sharper statement of the same wall, and it costs one clause.

## Recommended, stated for reversal

1. Replace *"the compact SO(6) face and the Lorentzian SO(5,1) substrate are co-equal real
   forms … nothing in the group theory privileges one"* with the four-form version: **so(6,ℂ) has
   four real forms; su(3) embeds in exactly one, the compact one.** Then say the ontological
   argument is what settles the *existence* question, which representation theory cannot.
2. Keep the ontological argument exactly as it stands. It does work no counting can do.

## Not claimed

- **No new mathematics.** The real-form list and the maximal compacts are textbook; su(3) ⊄ so(5)
  is `P13_qm_S4_vs_S5`'s, rebuilt here rather than cited.
- No claim that `sec:face-status`'s ontological argument is unnecessary — it is denying the compact
  face the standing of an *existent*, which no group theory reaches.
- **No claim on the universal**, which P13 explicitly declines: that no construction whatever could
  yield colour from geometry is strictly stronger and is not made here either.
- Nothing about the Atiyah–Hirzebruch obstruction, a separate face of the same wall.
- No closure on any registered item.
