# `r7724` (60) — RESULT, answering order `r7721`

**Registered before measurement.** `PREDICTION.md` was committed and pushed in its own commit
(`75526c83`) before `probe.py` existed and before anything it names was read. Readings in
`runs/READINGS.txt`: **48 arms, exit `0`, every self-check passing, four arms reporting a finding.**
The tree is named in `runs/TREE.txt` with a digest for each of the four files read.

---

## THE THREE QUESTIONS, ANSWERED

### ① "where `f<0` its sign is reversed" — **TWO OF THE THREE CONSEQUENCES NEED A WORD, and the third of them is the sharpest thing in this read**

The count was **measured**, not taken from the order: the prose says "Three consequences follow" and
exactly three ordinal markers follow it. `prop:curvature` does scope its formula to the static
region and does state the reversal; `sl_curvature_sign` is **one** statement with the two regions as
**hypotheses of two implications**, and its two values — `1 − (m/2)/r³` and `(m/2)/r³ − 1` — are
exact negatives, so the reversal is machine-checked as stated. Its subject is `-a / r l`, that is
`−r″/r`, and **not** `K_G`: `K_G` occurs once in the whole file, in a docstring, in **no** statement,
and "Gauss" and "surface of revolution" occur nowhere — so "cited and not formalised" is exact.

Measured on an undercritical member (`r₀ = 0.3`, `2M = 0.273`, horizons `0.3` and `0.8157`,
`r_HE = 0.5149` strictly between them):

- **CONSEQUENCE ONE is true as written.** It scopes its regularity claim to the static region, and
  what it asserts — finiteness and smoothness — is **sign-independent**: `|K_G|` is identical under
  the expression and under the two-case law at every radius tested. ⌗ This is the reading registered
  as (b): the scope is present *and* the claim would survive without it.
- **⛔ CONSEQUENCE TWO is no longer true as written.** It asserts a **single value AT a horizon** —
  "`K_G(r_h)=1/α²−M/r_h³` is simply a finite number" — under the headline "the curvature does not
  detect the horizons". Under the proposition's own two-case law the curvature takes **opposite
  signs** on the two sides of each horizon: at `r_h = 0.3` the one-sided values are `−4.0556` and
  `+4.0556`, a jump of `8.111`; at `r_h = 0.8157`, `+0.7485` and `−0.7485`. **The magnitude is
  horizon-blind; the sign is not** — and a sign flip exactly at `f=0` is the curvature detecting the
  horizon in the sharpest way available. The jump vanishes only where `f′(r_h)=0`, which is the
  Nariai member alone.
- **⛔⛭ CONSEQUENCE THREE is false as written outside the static region, and it is the sharpest of
  the three.** It says the curvature "changes sign **once**, at `r_HE`", "being negative for
  `r<r_HE` and positive for `r>r_HE`", with **no scope on the claim** — the scope that follows
  locates `r_HE` and does not restrict it. Witnessed: at `r = 0.12` and `r = 0.18`, both inside the
  inner horizon, `f < 0` and the actual curvature is `+77.99` and `+22.41` where the claim says
  negative; at `r = 1.6` and `r = 2.5`, beyond the cosmological horizon, it is negative where the
  claim says positive. And the actual curvature changes sign **three** times on `(0,3)` — at `r_HE`
  and at each horizon — not once.

⚠ **The endpoint I registered as likely to bite is not the one that does.** Where the curvature
*vanishes* — at `r_HE` itself — the reversal is vacuous, since `−0 = 0`. The endpoint that bites is
`f = 0`; and the arm had to be rewritten to test it by the **two one-sided values** rather than by
asking whether `f` is exactly zero, because the root is a root of the **cubic** and `f` at it is zero
only to the bisection's residual. ⌗ My first version asked the exact question and the residual
answered it: `f` came back at `−1e−17` and the "curvature at the horizon" was reported as a definite
number whose **sign was decided by that residual** — which is the sharpest witness available that
the quantity is not single-valued there.

### ② `prop:turning`'s value at the root — **A WORD IS NEEDED, and not only because the limit is unformalised**

`sl_turning` reaches the root and says nothing about a second derivative; `sl_turning_simple` is at a
root but its derivatives are those of `f` and of the cubic **in `r`**, not `d²r/dl²`;
`sl_accel_pos` and `sl_accel_neg` **are** about `d²r/dl²` (`deriv r`) and each carries a **strict**
inequality on `f`, so neither reaches `f = 0`. ⌗ The `r7718` guard was applied: the predicate's
first argument is `(deriv r)`, a property of the **curve**, while the value `f′/2` is the **metric
function's** derivative — the statement keeps the two subjects in the right places.

**⛔ But the gap is not only Lean's. The proposition's own PROOF does not give the value at the root
either.** The proof derives `d²r/dl² = ½f′·sgn f`; at `r = r_h`, `sgn f = 0`, so **the proof's own
formula returns zero exactly where the statement asserts a nonzero `±½f′(r_h)`**. Witnessed at the
simple root `r_h = 0.3`: `f′(r_h) = +2.4333`; the proof's formula at an **exact** root, where
`sgn 0 = 0`, is `+0.000000000`; and the two one-sided values are `±1.2167`, each reached from its
own side. ⚠ Evaluated in floating point the same formula returns `−1.2167` instead, its **sign decided
by `f(r_h) = −1.4e−16`** — which is not an artefact of the arm but the finding restated: the quantity
is not single-valued at the root. What is true is the **pair of
one-sided limits**, and that is exactly what the two declarations check. The formal paragraph already
says the honest thing ("wherever `f≠0`", "The limit of the second derivative at the root itself is
not formalised"), so the gap is between the **proposition and its own apparatus**, not between the
paper and Lean.

⛭ **And it is the same defect `①` found.** `prop:curvature`'s proof reaches its result "as in the
proof of Proposition~\ref{prop:turning}", so the `sgn f` formula that has nothing to say at `f = 0`
is **the single root of both of the order's first two questions.**

⚠ The reachable negative registered as (c) — that something formalised *does* reach the root, making
the order's parenthetical the stale thing — is **not** reached: a named search over every
declaration mentioning `deriv r` finds none without a strict hypothesis on `f`.

### ③ P15's "more than six … at the two wider smoothings" — **THE SENTENCE IS SOUND; THE ORDER'S `11.8` IS NOT A MEASURED NUMBER**

The host receipt was **run**, because these values exist only at run time (negative probe 22). It
comes back green, and its witness line prints one value per smoothing:
`h0.175: 3.9 sd`, `h0.25: 6.6 sd`, `h0.35: 12.4 sd`.

- **The sentence is sound, and it is an INEQUALITY and not a match** — the way an arm testing
  equality would have reported a false defect. Both wider smoothings stand above six; the narrowest
  stands **below** it, so "at the two wider smoothings" is exactly the right **set** and not a
  hedge: the claim would fail if the narrowest were included.
- ⚠ The `r7708` check, the one that bit this corpus before: the tightest of the two, `6.6`, is nearer
  **seven** than six. At `r7708` that was a defect because the sentence was an **approximation**
  ("some seven times" for `7.8`); here it is a **floor**, and a floor that holds is correct however
  much room it leaves.
- **⛔⛭ But the second half of the question turns up a finding in the receipt itself.** The order
  names "`6.6` and `11.8`", and **`11.8` is not a measured value**: it is a **hard-coded number in
  the gate's own label** ("would have shown there at `3.8` to `11.8` sd"), printed beside witnesses
  that give **`3.9` to `12.4`**. The low end is off by `0.1` and the high end by `0.6`, and the gate
  cannot catch it because what the gate **asserts** is only that each value exceeds `3.5`. The order
  inherited `11.8` from the label rather than from a measurement.

---

## THE REST OF THE LANDING

**`prop:conjugacy`.** The proposition says "conjugate on `[0,1]`"; `sl_conjugacy` carries the
interval as a **set-membership hypothesis** `x ∈ Set.Icc 0 1`, not as an unrestricted identity and
not as another set; `sl_conjugacy_fails` is **universal** over `Set.Ico (-1) 0` = `[−1,0)` and
concludes `≠`, which is the failure *at every point* the prose claims rather than one exhibited
point. ⌗ **The order's own justification is checked rather than taken:** `x = sin a` maps
`a ∈ [0, π/2]` **onto** `[0,1]` exactly — `[0, 1.000000000000000]` — so "on `[0,1]`" is the proof's
own domain, neither an unnecessary narrowing nor an insufficient one; and the proof's step
`arcsin sin(π/2−a) = π/2−a` **fails** for `a<0`, so the hypothesis is load-bearing.

**⛔ One over-reach, of the `r7718`/`r7720` class.** The formal sentence says the two sides differ on
`[−1,0)` "by the nonzero amount `(2/√3) sin(⅔ arcsin x)`" and cites `sl_conjugacy` and
`sl_conjugacy_fails`. **The amount is TRUE** — computed at 399 samples, the residual of
`(χ∘g₁ − σ∘χ) − χ` is `5.5e−15`, and at `x = −0.5` the gap is `−0.394930844 = χ(−0.5)`. But
`sl_conjugacy_fails`' conclusion is a bare `≠` and names no amount, and its proof never computes
one. **The claim is established; its pointer reaches one clause too far.**

**`prop:triple`.** `sl_triple` is the identity at **every** `w`, with no hypothesis on `w`;
`sl_triple_unique` is the uniqueness of the **pair** (scale, coefficient) — an identity plus a
separate uniqueness lemma rather than an `∃!` — and it carries `0 < ϱ`. ⚠ **That positivity is
load-bearing, shown by its witness rather than asserted:** `ϱ = −2/√3` with `k = −2/(3√3)` satisfies
the same identity at all 241 sampled `w`, the residual's supremum `9.4e−16`. So "unique" is unique **among positive
scales**; the proof says "unique **positive** root" and Lean carries `0 < ϱ`, while the
proposition's statement says only "unique" — a looseness carried by a slicing scale being a radius,
not a defect.

**The registered absence holds.** `prop:twoalpha` is present and the landing's own diff of this paper
does not touch it — `0` occurrences of "twoalpha" in `27` changed lines — so the order's "not landed
yet" is accurate. Zero `axiom` tokens and zero `sorry` in the Lean file, which is new in this landing
at 18,015 lines.

---

## ⛔ THREE DEFECTS IN THIS PROBE, AND THE FIRST IS THE ONE WORTH KEEPING

⓵ **⛭⛭ I GENERATED THE GREEK TABLE PRECISELY TO AVOID `r7722`'S DEFECT, AND THE GENERATOR
REPRODUCED IT.** `r7722`'s purest instance was a hand-written Greek table that lacked `σ`. So this
probe builds the table from the characters **actually present in the files read** — and filtered on
`'LETTER' in unicodedata.name(ch)`. `ϱ`, which `sl_triple_unique` uses, is **GREEK RHO SYMBOL** and
carries no `LETTER` at all, so it came back unmatched. **A generator is still a form, and this was
its form.** *Sixteenth instance in twelve revisions, and the first where the blind spot survived
being automated away.*

⓶ **`hypotheses_of` had two defects at once, both caught by its own self-test.** It dropped a nested
**closing** bracket, so `Set.Icc (0 : ℝ) 1` came back as `Set.Icc (0 : ℝ 1`; and it ran on the whole
statement, so parenthesised groups of the **conclusion** were returned as binders. It is now bounded
by the same depth-zero colon `conclusion_of` splits at. ⌗ The self-test that caught it is the one
that prints what it read rather than only whether it found something.

⓷ **⚠ And the arm that searched for the unformalised bridge read a NAME in a different sense.**
Searching the Lean file for `KG` returns **eight** hits, and every one is `section KG…` from an
unrelated earlier campaign. The arm now asks **where** a token sits — in a statement, in a docstring,
or nowhere — and reports the false positive it would otherwise have produced. *Negative probe (19)
exactly: an instrument reads the FORM it was given, and a name is a form.*

⌗ And `Ⓑ⑨`'s rewrite is a fourth of the same family, recorded under `①` above: asking whether a
bisected root makes `f` exactly zero is asking floating point a question it cannot answer, and the
residual answered it with a sign.
