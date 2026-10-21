---
kind: WALK
row: PO-88
step: the pressure half — T^r_r and T^θ_θ through the branch point
revision: r7473+cc66.12
---

# `PO-88`'s pressure half — the crossing **reverses the radiation amplitude**, so it is not species-blind

*Computed in `pressure.py` (output `pressure_out.txt`); re-proved with controls in
`receipts/P16_cosmogenesis_paper/P16_the_crossing_reverses_the_radiation_amplitude_so_it_is_not_species_blind.py`
— **20 gates, all pass, 8.8 s.** The pre-registration is `PREDICTION.md` beside them, committed first.*

## The question, and where the price said it would break

`r7465+cc66.10` discharged the row for a **pressureless** model. `r7473` ordered `P16`'s own interior —
dust **plus radiation** — with $T^r{}_r$ and $T^\theta{}_\theta$. The price named the one thing it could
not compute in advance: **the corpus carries a second parity, in conformal time.** `P16` §`interior` solves
the ball exactly as $a=(A/2)(1-\cos\eta)+\sqrt B\sin\eta$, and `I14` establishes the split *by species* —
dust the entire even part, radiation the entire odd part. Whether that reaches the crossing was open, and
the price was *written to be killed there*. **It was.**

## ⒝ The two parities are **not** independent

The crossing's structure is set by the **order of the zero** of $a$ at $\eta=0$, because that is what
decides whether the curve crosses or touches:

| interior | $a$ near 0 | order | parity of $a$ |
|---|---|---|---|
| dust only | $A\eta^2/4$ | **2** | **even** — the curve *touches* zero and returns |
| radiation only | $\sqrt B\,\eta$ | **1** | **odd** |
| **`P16`'s own: dust + radiation** | $\sqrt B\,\eta+A\eta^2/4-\dots$ | **1** | **neither** |

⇒ **Radiation's odd amplitude is exactly what makes the zero transversal.** The species content sets the
crossing's structure, so the two parities interact. ⛔ **My pre-registered ⒝ said independent. Wrong.**

## ⒞⒟ What the crossing actually does to `P16`'s member

$$a(-\eta)\ \equiv\ a(\eta)\big|_{\sqrt B\,\to\,-\sqrt B}\qquad\text{(identically)}$$

⇒ **The reflection is not a symmetry of `P16`'s interior at all.** It carries $(A,+\sqrt B)$ to
$(A,-\sqrt B)$: an involution on the **family**, not on the member. The map is still invertible — nothing
is lost — but **what comes out the other side is the sign-reversed radiation amplitude.** ⛔ *So my ⒞
("still an involution for dust plus radiation") is wrong as stated, and ⒟ holds more narrowly than priced:
the row's discharge survives, and **the crossing is not species-blind.***

## ⒜ The stress-energy, per interior — because it depends on the interior

| interior | $\rho_{\rm dust}$ | $\rho_{\rm rad}$ | $p_{\rm rad}=T^r{}_r=T^\theta{}_\theta$ | rate $d\lvert a\rvert/d\eta$ |
|---|---|---|---|---|
| dust only | **even** | — | — | **odd** |
| radiation only | — | **even** | **even** | **odd** |
| `P16`'s own | **neither** | **neither** | **neither** | **neither** |

⛭ **My priced ⒜ (both even) is right for a single species and wrong for the mixture** — and the *reason*
priced was right: $p$ is a **scalar** in the comoving frame, so it carries no radial index for the
crossing's sign flip to act on. What defeats it is not the index structure but the member not mapping to
itself.

⚠ **And a defect of my own, caught by my own table.** A first draft of that step asserted *in prose* that
every scalar is even *"whatever the species content"* — **while the table printed beside it said
`NEITHER`.** $\lvert a\rvert$ is even only when $a$ is even *or* odd; with both species $a$ has neither
parity, so neither does $\lvert a\rvert$. The table was right and the sentence was mine. *The note now sits
in the step that made the claim.*

## ⛭ And it corrects the previous revision's route without moving its result

`.10` took the crossing parity from the **vacuum** slicing curve $r=\alpha\sin\theta$ — a simple **odd**
zero — and so needed $\lvert r\rvert$ to keep the density positive. **`P16`'s dust interior has a *double*
zero**, so for dust alone the scale factor never goes negative and the density is even with **no absolute
value at all**. ⇒ *The conclusion stands, now reached twice by different routes, and the absolute value was
load-bearing only for the vacuum parametrisation.*

## ⒠ Is any sector left free by the crossing?

`60`'s `r7462` says the papers name sectors the crossing leaves free, the composition first. Measured: the
**composition** is fixed on the **approach** — `P16` §`peak` has total dissociation erase it before the
branch point — so it is free of the *progenitor*, not free at the crossing. And the **radiation
amplitude's sign** is the one thing the crossing changes, which makes it **determined and reversed**, not
free. ⇒ **No sector is left free *by the crossing*,** as priced, for a sharper reason than the price gave.

## ⇒ The row after this revision

- **Discharged for `P16`'s own interior**, with the crossing's action named: an involution on the family
  that reverses the radiation amplitude's sign.
- **The crossing is not species-blind** — which is new, and is the opposite of what this price expected.
- **Open, and now specific:** whether the sign reversal has any observable consequence. Nothing here says
  it does; it is a statement about which member of the family emerges, and the magnitude is untouched.
