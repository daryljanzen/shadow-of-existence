# r7688 (60) — RESULT: the sentence rests on nothing `71` reports unproved, because the probe proves `D = I⁻(O) = M`

**Order:** `r7685` (69), item 1. Item 2 is **held by the order itself** and is not begun here.
**Tree:** `runs/TREE.txt` — worktree `09bc64b2…`, HEAD `4003e41f`, previous `ef98923f`.
**Registered before anything was scored:** `PREDICTION.md`, on its own pushed commit, with its one
limit declared there: **this container has no Lean toolchain, so the probe is read at source and not
compiled.** Every verdict is a claim about what the file states and takes as hypothesis.

**Seven claims: 6 SUPPORTED · 0 NOT SUPPORTED · 1 TWO-TO-ONE · 0 UNMEASURED.**

> ### ⛭⛭⛭ THE ORDER'S QUESTION, ANSWERED: **NO.** The sentence claims nothing that rests on the
> frontier of `D`. **`frontier` appears ZERO times in the statements of all three cited theorems** —
> searched the full statement text of `sv_cauchy`, `sv_retarded_eq` and `sv_eternal_cauchy` as the
> file prints them, from `theorem` to `:= by` — and the probe **proves the identification instead**:
> `sv_D` gives `D = I⁻(O) = M` as an **equality**.
>
> ### ⌗ AND IT IS THE SAME STRUCTURAL MOVE `r7680` FOUND FOR `se_foundation`: *the manifold IS the
> domain*, so there is no frontier for the sentence to rest on. **Second time this mechanism has
> carried a clause that looked exposed.**

---

## ⑤ — THE DEPENDENCE, READ AT SOURCE

`71`'s report is **right about the probe** and **irrelevant to the sentence**, and those are two
different findings:

- `sv_cauchy`'s conclusion is `(sv_S hM v₀).IsCauchyTemporalOn (sv_S hM v₀).M (sv_Θsh M a η v₀)` —
  **on the manifold `M`**, not on a domain taken as a causal past whose boundary would then need
  identifying.
- `sv_D` proves, as its **first conjunct**,
  `(sv_S hM v₀).D (range (sv_O M v₀)) = (sv_S hM v₀).M`, with the observer
  `O(τ) = (u_H − e^{−τ}, τ)`, together with `range O ⊆ M`, the chronology of `O`, and `ũ → u_H`.
  **`D` and `M` are the same set by that equality.**
- `sv_cauchy_D` then states the Cauchy property on `D` directly, and follows from `sv_cauchy` through
  that equality rather than through any boundary argument.

⇒ *The sentence says "a Cauchy temporal function of the exterior". The exterior it means is a set the
probe **has**, not one it assumes the shape of. A gap in the frontier of `D` would be a gap in
something the three theorems never mention.*
⌗ **What the registered negative probe bought:** arm ⑤ was registered as a question about a
**dependence**, with the sixth negative probe demanding that the reader be able to answer *"does not
rest on it"* and still **fail** on a sentence that plainly does. *This seat's own lesson is that a
dependence test is not a correctness test — so the instrument had to be able to come back clean, and
the clean answer is only worth something because it could have come back dirty.*

## ① – ④ — THE COLLAPSE ATTESTATION, CLAUSE BY CLAUSE: ALL SUPPORTED

- **① SUPPORTED.** *"the radial plane of a collapse by a thin ingoing null shell with a flat past."*
  The probe builds `P` with coordinates `(ũ, v)` — the radial plane — `M = {ũ < u_H}` with
  `u_H = v₀ − 4M`, and the shell at `v = v₀`: **`sv_flat_past` gives `Φ = 1` for `v ≤ v₀`** (the flat
  past) and **`sv_vacuum` gives `Φ = f(r) F′(ũ)` for `v ≥ v₀`** (Schwarzschild outside), with
  `sv_Φ_gt_one` separating them. *Thin, ingoing, null, flat past — each a definition or a lemma, not
  a description.*
- **② SUPPORTED, exactly, and the probe glosses it itself.** `sv_retarded_eq` concludes
  `sv_Θsh M a η v₀ y = a * (sv_F M v₀ y.1 + η * sv_r M v₀ y)` under `y ∈ sv_MS M v₀` and **`v₀ ≤ y.2`**
  — and `sv_F M v₀ ũ = ũ − 4M·log((v₀−ũ)/4M − 1)` is the retarded time in closed form, so the
  conclusion **is** `a(u + ηr)`; the probe's own header writes *"on `v ≥ v₀`, `Θ_shell = a(F(ũ) + ηr)`,
  i.e. `a(u + ηr)`."* ⌗ *And "the **whole** vacuum exterior" is the right word, because `{v ≥ v₀}` is
  exactly the vacuum side of the shell by `sv_vacuum` — the hypothesis is the vacuum region's
  definition, not a restriction inside it.*
- **③ SUPPORTED, and the smoothness is carried INSIDE the predicate rather than beside it.**
  `IsCauchyTemporalOn U τ` unfolds to `IsTemporalOn U τ ∧ ∀ c, ∀ a, ∃! t, τ (c.γ t) = a`, and
  `IsTemporalOn U τ` begins `ContMDiffOn 𝓘(ℝ,E) 𝓘(ℝ,ℝ) 1 τ U`. With `U = M`, which **spans the
  shell**, `sv_cauchy` already asserts `C¹` across the body. ⌗ ⛭ *And the one thing that could have
  broken it is handled explicitly: the probe records that conformal invariance
  (`cz_scale_isCauchyTemporalOn`) removes `Φ`, **"whose kink at the shell never enters"**. The
  sentence's "continued smoothly through the body" is the strongest of its clauses, not the loosest.*
- **④ SUPPORTED, exactly.** `sv_cauchy`'s hypotheses are `0 < a`, `0 < η`, **`η ≤ 2`** — the
  sentence's `0<η≤2` to the symbol — and its conclusion is the Cauchy property on `M`, with
  `sv_cauchy_D` on `D`. ⌗ *A precision, not a fault: the sentence's words ("of the exterior") match
  `sv_cauchy_D`'s phrasing more literally while it cites `sv_cauchy`, and citing `sv_cauchy` is the
  right choice because `sv_cauchy_D` is its corollary through `sv_D`.*

## ⑥ — THE ETERNAL SENTENCE: SUPPORTED, AND STRONGER THAN IT CLAIMS

*"On the eternal exterior, changing it only in the past already makes it Cauchy
(`sv_eternal_cauchy`), so the obstruction there is at the past end alone."*

- `sv_eternal_cauchy` takes `2M < r₀`, `0 < a`, `0 < η`, `η ≤ 2` and **`(v₀ : ℝ)` universally
  quantified**, concluding `(se_S hM).IsCauchyTemporalOn ((se_S hM).D (range (se_Ost hM hr₀)))
  (sv_Θψ M a η v₀)`. ⇒ **For EVERY cut `v₀`, not for one** — the sentence understates its own
  theorem, which is the better direction to err in.
- *"changing it only in the past"* is **exactly** `sv_eternal_eq`: `sv_Θψ = sr_Θ + aη·ψ_{v₀}(4M log v)`,
  and `Θ_ψ = Θ_ret` on `{v ≥ v₀}`. **The modification is confined to the past of the cut, and that
  confinement is a theorem.**
- ⌗ **But *"alone"* is an INFERENCE and no conjunct states it.** It is well licensed — `sr_not_isCauchy`'s
  witness is a curve ending on the **white-hole horizon**, a past-end feature, and the probe's own
  header has a section headed *"Past end `sv_past_pure`, the new part"* — but what is proved is that a
  past modification **suffices**, not that the past end is the **only** possible obstruction.
  ⇒ *Reported as an inference the two theorems jointly license. This seat's own `r7682` lesson points
  the same way from the other side: one construction that fixes a problem shows it is fixable, not
  that it has one cause.*

## ⛔ ⑦ — `lem:alignment` (ii) IS STILL TWO-TO-ONE, AND NOW **MORE** OWED THAN AT `r7684`

The statement is **unchanged on this tree**: the preamble still fixes `Θ` as *"any smooth Cauchy
temporal function of `D`"* with `D` the Schwarzschild exterior, and (ii)'s first sentence still reads
*"For the stationary slicing **and for the slicing built on the retarded time below**, …"* — so, read
on its own preamble, (ii) still asserts the retarded slicing **is** a Cauchy temporal function of the
**eternal** exterior, which `sr_not_isCauchy` disproves for every `a, η > 0`.

**What changed is the proof, and it changed in the direction that makes the repair worth more.** The
proof paragraph now distinguishes **three** statements where the lemma's statement has one `D`:

| | eternal exterior | collapse exterior |
|---|---|---|
| temporal | **yes**, exactly for `η ≤ 2` (`sr_temporal`, `sr_not_temporal`) | yes, inside `sv_cauchy` |
| Cauchy | **NO** (`sr_not_isCauchy`) — unless modified in the past (`sv_eternal_cauchy`) | **YES** (`sv_cauchy`) |

⇒ **At `r7684` the statement was ahead of a proof that scoped the retarded case in its second
sentence. Now it is behind a proof that machine-checks two different exteriors and separates them.**
**I decide the near half and recommend the same six words, now with a second reason:** in (ii)'s first
sentence, *"for the stationary slicing, and for the retarded slicing **of the collapse exterior
described below**"*. *Nothing in print moves, no figure changes, and the statement would then carry
the distinction its own proof now rests on.*

---

## WHAT THE GUARDS CAUGHT

**Nothing failed this time, and that is a reading rather than a silence.** Every clause of the
collapse attestation holds, three of them more exactly than the sentence claims. ⌗ *The instrument
that mattered was the one registered to be able to find nothing: arm ⑤'s sixth negative probe. A
dependence question answered "no" is only worth something from a reader that could have answered
"yes", and that is why it was registered by name before the file was opened.*

**Counting was again the wrong instrument where naming was the right one.** `frontier` had to be
searched in the **statements** of the three theorems, from `theorem` to `:= by`, not in the file:
these probes are cumulative bundles and the word appears freely elsewhere in them.

**The flip family caught nothing — fifth revision running.** ⌗ *Recorded each time, because a guard
family that has not caught a finding in five revisions is either redundant or pointed at the wrong
thing, and saying so is cheaper than discovering it later.*

> ### ⛭ THE LESSON, ADDED TO THIS SEAT'S CHAIN
> **A SENTENCE CAN BE SAFE FROM A GAP THAT IS REALLY THERE.** *`71`'s report is correct: the probe
> does not prove the frontier of `D`. The sentence is also correct, because it never needs it — the
> probe proves an EQUALITY where a frontier argument would have been needed. "There is a gap in the
> probe" and "the sentence rests on a gap" are two claims, and only the second is about the paper.*

## SCOPE

**Nothing is edited** — no paper, no probe, no receipt, no figure, no tolerance, no gate, no ledger
row, no instrument; and the probe is **not compiled**, as the registration declared. One repair is
routed in `FOR_66_FROM_60.md` with its wording, for the second time and with its new reason; item 2
of the order is held, by the order.
