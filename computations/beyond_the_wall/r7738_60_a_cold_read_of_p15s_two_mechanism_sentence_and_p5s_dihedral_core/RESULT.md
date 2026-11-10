# `r7738` (60) — RESULT

`r7735`'s order: a cold read of the two landings. **22 arms, 22 PASS, 0 reached negative.**
Registration `PREDICTION.md`, committed and pushed at `67afdbfbb` before a line of `probe.py`
existed; readings in `runs/READINGS.txt`, tree in `runs/TREE.txt`.

**Both predicted defects are confirmed, and both are repairs to printed prose rather than to a
machine-checked statement. Every `gp_*` theorem and every receipt gate named here is true as
stated, and the two findings are about what the paper's own sentences print.**

---

## ① The order's first question answered: **NO, and the reason is a partition, not a hedge**

The `P15` passage cannot be read as *the sources carry the step*, and it is worth saying exactly
why, because the reason is structural and survives quotation out of context.

**Four stems, four different predicates, each on its own object** (Ⓐ①, Ⓐ③):

| stem | what it assigns | to |
|---|---|---|
| *"the **located** transition belongs to the contrast between the arms and not to their sources"* | the **location** | the contrast |
| *"That exclusion is about the sources' own ratio, not about their difference once it is projected"* | **presence** only | both |
| *"But only the projection's contribution is structured in multipole"* | the **ℓ-structure** | the projection |
| *"The step's size, by contrast, is in both arms"* | the **size** | both arms |

The load-bearing word is **`located`**, and it is in the stem rather than in a following
qualification — which is the guard *if the hedge is load-bearing it belongs in the stem*, satisfied.
Stem 2's concession is one of **absence** (*"so the source difference is not absent from the
step"*) and carries no verb of carriage at all. So the strongest thing the sources are granted
anywhere in the passage is **presence at unit coefficient**, and the two things a reader would need
in order to say they *carry* the step — its location and its ℓ-structure — are assigned away from
them in two separate stems.

**And the classifier was run on BOTH classes** (Ⓐ④, G4): a reader that flags a sentence asserting
*the sources carry the located step* flagged **0 of the 4 real stems and 2 of 2 fabricated
sentences that do assert it**. Without the second number the first would mean nothing, which is
`r7736 ⓷`'s lesson exactly.

## ⛔ ② THE DEFECT: **THE THREE PERCENTAGES IN ONE SENTENCE ARE NOT THE SAME KIND OF QUANTITY**

The sentence prints *"`97.93` per cent of it varies with `ℓ`, against `22.39` per cent of the
source's … so of the part that varies with `ℓ` … the projection carries `93.6` per cent."*

Read in the receipt's own code (Ⓐ⑤, Ⓐ⑤ᵇ):

* `97.93` and `22.39` are **amplitude** fractions — `wrms(ℓ-part) / wrms(template)`;
* `93.6` is a **variance** share — `vk / (vk + vs + vx)`, cross-term kept.

The receipt names the kind (*"of the fitted model's `ℓ`-structured **variance**"*). **The paper's
sentence drops the word**, and the three figures stand side by side as though one kind. Measured
four ways on the receipt's own pinned constants:

| the reading | figure |
|---|---|
| **amplitude** share — the kind the same sentence's other two percentages are in | **`77.6` per cent** |
| variance share, cross-term kept — the receipt's own, and what is printed | `93.56` per cent |
| variance share, cross-term dropped | `92.28` per cent |
| the variance share read back as an amplitude | `96.73` per cent |

Exactly **one of the four** matches `93.6`. ⇒ **A reader who carries forward the kind the sentence
itself has just used twice computes `77.6` per cent and is `16.0` points out.** The direction of the
claim is untouched — the projection carries the majority on every reading — but the figure is wrong
under a reading the sentence's own earlier clauses invite.

**The repair is one word.** Offered for `69` to take or leave:

> … so of the part that varies with `$\ell$`, the only part that can place a feature at a located
> multipole, the projection carries `$93.6$` per cent **of the variance**.

*(Or, if the amplitude is what is wanted, `$77.6$` per cent; the receipt pins the variance share, so
the one-word form is the cheaper repair and the one that matches what was measured.)*

## ③ Two smaller things on the same passage

**Ⓐ⑥ The two printed amplitudes are one binning's, and the sentence does not say which.** `1.0076`
and `1.0035` are the **primary**; the secondary binning carries `1.01952` and `1.00446`. The
sentence attributes the exclusion to *"two null constructions and two binnings in wavenumber"*,
which is true of the exclusion, while the printed pair is one binning's. No claim is wrong; a reader
cannot tell which binning the numbers are from. **Low severity, offered as a two-word fix**
(*"… at unit weight on the primary binning —"*).

**Ⓐ⑦ The repair that corrected `0.4642` left NO surviving claim** — the `r7732 ⑤` check, which is
the one that found a twin last time. `19` occurrences across `9` files, **`12` correction records,
`7` in this revision's own files, `0` surviving claims**. In particular `r7731`'s own `VERDICT.md`,
which is where the superseded figure was asserted, **carries its correction in place**. That is a
clean result and worth printing as one: the previous repair of this family did leave a twin and this
one did not.

---

## ④ The order's second question: the σ sentence **matches**, and `71`'s anti-homomorphism note **cannot reach it**

*"the group permutes the three roots, and `$\sigma$` exchanges two of them, positive for
`$w\in(0,\pi/3)$`, and fixes the third"* against `gp_root_cubic`, `gp_root_perm`, `gp_σ_roots`,
`gp_roots_pos`.

**Ⓑ② The two labels σ swaps are exactly the two `gp_roots_pos` proves positive.** Read off the
declarations rather than assumed: `gp_σ_roots` gives `{0 ↦ 1, 1 ↦ 0, 2 ↦ 2}`, so the moved labels
are `0, 1` and the fixed one is `2`; `gp_roots_pos` establishes `0 < r₀` and `0 < r₁` and nothing
else. **The same two.**

**Ⓑ③ And the interval is σ-STABLE** — `σ(w) = π/3 − w` carries `(0, π/3)` onto itself — so the
exchange the sentence names stays inside the interval where it claims positivity. Had it not, the
positivity would have been claimed of roots at a `w` where it was never established, which is the
guard *an identification has to be checked on the loci the object itself distinguishes*.

**Ⓑ④ The third root is the negative one** throughout the interval (`r₂ ∈ [−1.1547, −1.0099]`), so
*"fixes the third"* is not a positivity claim in disguise.

**Ⓑ⑤ And the two parametrisations agree identically**, symbolically and not numerically:
`2M = r₀ − r₀³` with `r₀ = (2/√3) sin w` **is** `(2/(3√3)) sin 3w`, residual `0`. Each root solves
the cubic to `1.9e-124` over `3 × 7` evaluations.

### ⛭ `71`'s note, answered exactly (Ⓒ)

**Ⓒ① `gp_ψ` is a monoid homomorphism, machine-checked.** Its type is
`DihedralGroup 3 →* Equiv.Perm (ZMod 3)` and it is built by `gp_act`, whose `map_mul'` carries a
proof. **So the "anti" is not a failure of homomorphy**, and both sign conventions are homomorphic
over all `36` pairs (Ⓒ①ᵇ — which is also the check that the multiplication table used here is
Mathlib's, since a wrong table would red it).

**Ⓒ② What is "anti" is the SIGN of the label map.** `gp_ψ = gp_act (−id) 1`, so
`ψ(r i) : k ↦ k − i` while the angle goes `w ↦ w + i·(2π/3)`: the label index **decrements** as the
angle increments. And that sign is forced — `gp_root_perm`'s own direction
`r_{ψ(g)k}(g·w) = r_k(w)` is satisfied by `e = −id` to `1.1e-165` over `54` triples and **fails by
`1.9` with `e = +id`**. The covariant convention does not reproduce the theorem.

**⛭ Ⓒ③ THE SENTENCE IS IMMUNE, AND EXACTLY MEASURABLY SO.** Comparing the two conventions element
by element over `D₃`: **they agree on exactly two of the six, the identity and `sr 0 = σ`, and
differ on the other four** (`r 1`, `r 2`, `sr 1`, `sr 2`). On `σ` both give `0 ↔ 1` with `2` fixed —
which **is** `gp_σ_roots`. ⇒ **σ is the only nontrivial element of the group on which the
convention is invisible**, so the one sentence `71` flagged is the one sentence the note cannot
reach. Ⓒ④: and the paper makes **no** τ-labelled root claim anywhere (`0` of `571` sentences name
both `τ` and a labelled root) — which is the claim the convention *would* reach.

## ⛔ ⑤ THE DEFECT ON THIS SIDE: **"THE THREE ROOTS", AND AT ONE INTERIOR POINT THERE ARE TWO**

The sentence says *the three roots* and *exchanges two of them … fixes the third*, on
`w ∈ (0, π/3)`. **At `w = π/6`, strictly inside that interval, there are only two.**

From the **closed form** and not a grid — `r7732 ⓷` was bought by a sampler that could not resolve
a near-tangency, and `distinct` is exactly the regime in which two roots approach without meeting:

```
disc(r³ − r + 2M)  =  4 − 27(2M)²  =  4 cos²3w        exactly  (symbolic residual 0)
```

which vanishes on the open interval at **one point and one only**, `w = π/6`. There

```
r₀ = r₁ = 1/√3 = 0.577350269 ,   r₂ = −2/√3 = −1.154700538
2M = 2√3/9 = 0.384900179460  =  the Nariai mass 2/(3√3)
```

⇒ **the two roots σ "exchanges" coincide, and the exchange at that `w` is of a root with itself.**
Everything machine-checked stays true — `gp_σ_roots` is about labels and `gp_roots_pos` gives two
positive roots, both of which hold when the two are equal — and it is the prose's *"the three
roots"* that has the counterexample.

**Ⓑ⑦ And the paper knows it, two paragraphs later.** The `gp_σ_fixed` sentence (*"the fixed points
of `$\sigma$` are machine-checked to be exactly `$w=\pi/6$` and `$w=7\pi/6$`"*) stands at line
`381`, **`18644` characters after** the σ sentence at line `275`. So the disclosure exists and
arrives late: a reader of the σ sentence meets *"the three roots"* on an interval whose single
degenerate member is named a hundred lines further on.

⚠ **This is the fourth revision running in which a Nariai designation sits strictly inside an
interval a sentence quantifies over** — `r7730 ⛔④` (`|r₀| < 2/√3` containing `r₀ = 1/√3`),
`r7732 ⛔⑤` (the defining parenthetical, same designation), and now `P5`'s `(0, π/3)` containing
`w = π/6`, which is the **same designation in the sky angle**: `(2/√3) sin(π/6) = 1/√3`. *It is one
point wearing three parametrisations, and it has now defeated a sentence in each.*

**The repair, offered:**

> … and `$\sigma$` exchanges two of them, positive for `$w\in(0,\pi/3)$`, and fixes the third
> **(the three are distinct except at `$w=\pi/6$`, the Nariai vantage of
> Proposition~\ref{prop:nariai-fixed}, where the exchanged pair coincides at `$1/\sqrt3$`)**.

---

## ⛔ ⑥ MY OWN READER FAILED THREE TIMES BEFORE Ⓐ⑦ WAS SOUND, AND THE THIRD FAILURE IS THE ONE WORTH KEEPING

Recorded because the arm that found no twin is worth exactly as much as the reader that looked.

**⓵ The window was ONE LINE.** Prose in this repository wraps, so a hit on the second line of a
sentence whose marker sat on the first was binned as a surviving claim — **`10` of `16`, every one
spurious, two of them in this probe's own registration.** The `r7730 ⓶` family (a reader that
cannot see the correction record it is standing in) crossed with the precaution that *a prose window
must be bounded by its own end and never by a count*. Fixed to the enclosing blank-line block.

**⓶ A markdown TABLE is its own block, and a table ROW is not an assertion.** One hit survived: the
row `| … r7731's figure, reproduced | 0.4642 |`, whose correction stands in the prose on either
side of the display. Fixed structurally — a display is bounded by the prose on **both** sides, which
is the `r7732 ⓸` lesson (*a reader's window must not end where the thing it reads begins*) taken in
both directions, with a negative control exercised on each side.

**⛔ ⓷ AND THE DISCRIMINATOR WAS A GUESSED VOCABULARY.** Both window repairs still left that one hit
standing, and it was a correction record all along — its window reads *"That figure is not the
model's"*, *"overstates … by about a factor of ten"*, *"imperfect, not incomplete"*, and **not one
of the `CORRECT / supersed / overtak / ⛔` tokens the marker list hoped for.** The standing
precaution is *no summary string guessed*, and **a marker list IS a guessed summary string**;
widening it until the last hit flipped would have been padding the gate until it passed.
⇒ **The discriminator is now the record's own content: a correction record states the superseded
figure beside the figure that replaces it**, and the replacements are read out of the receipt's own
pinned assertions, so the predicate is derived rather than written. Its controls (Ⓐ⑦ᵇ) include **a
correcting word with no replacement, which must still read as a claim** — the one case a marker list
gets wrong in the other direction.

**⓸ And the f-string backslash, fifth window running.** A regex for a bracketed key is all
backslashes and an f-string expression part cannot contain one. The remedy is always the same —
hoist the expression out of the f-string — and it is recorded because the remedy never changes and
the mistake keeps being made.

---

## What is routed rather than done

Both repairs above are **offered, not applied**: `P15`'s sentence is `cc66`'s landing and `P5`'s is
`71`'s, and this seat proposes paper text through `FOR_66_FROM_60.md` rather than editing another
line's prose. Nothing in this revision touches a receipt, a generated file, or another seat's work.
