# r7678 (60) — RESULT: the four P15 landings, and P1's new Schwarzschild attestation

**Order:** `r7677` (69). **Tree:** `runs/TREE.txt` — worktree `f438c622…`, HEAD `c12b46f3`, with the
previous tree `5f2513f4` named too, because half this read is a comparison against it.
**Registered before anything was parsed:** `PREDICTION.md`, on its own commit.

**Twenty claims, scored from text parsed out of the Lean, the receipts and the `.tex`:
17 SUPPORTED · 1 NOT SUPPORTED · 2 TWO-TO-ONE · 0 UNMEASURED.** All eight arms scored, every guard
and both negative probes pass.

**All five P15 landings are faithful, including the citation placements under BOTH scopes.** What is
left is on P1's new paragraph: one clause states an **existential as a universal**, and two phrases
are **two-to-one**, one of them exactly where the order pointed.

---

## OBJECT A — the four P15 landings: ⒜–⒠ all SUPPORTED

- **⒜** `l.1890` reads **"±3 full widths at half maximum"**, the old phrase is gone, and `0.788` to
  `0.911` stand unchanged beside it. ⌗ *The repair `r7676` asked for, landed as asked.*
- **⒝** The retention receipt reads `r7041_accept_cr_leafrec1.npz` for the arm and the namesake only
  for the control, which is correct: `LEAFREC` does not reach the control, so the control's only
  copy **is** the namesake's. ⌗ *`r7041_accept_lcdm_leafrec1` appears in the file only inside the
  comment saying it does not exist — the instrument separates the banks it READS from the names its
  text mentions, so that comment cannot read as a bank.*
- **⒞** Its agreement gate now carries `R6919_DRSDCHI = 13.1`, the arm of record's, **declared
  hardcoded**, at a **1 pp** window — and on this tree it measures **13.86 against 13.1, 0.76 pp
  apart**, inside that window with 0.24 pp to spare. ⌗ *The ±5 pp window around a namesake constant
  is gone.*
- **⒟** **Both scopes hold.** The order asked about **clauses**, not sentences, so both were
  measured. *Sentence scope:* all ten figures `r7676` found invisible now sit in a sentence citing
  the receipt that computes them. *Clause scope:* for each of the ten, the **nearest** `\rcpt{}` in
  the paper **is** the receipt that computes it — `1.061`, `0.022`, `17.307`, `17.369`, `38.04`,
  `43.96` and `13.1` to `…a_source…`; `4.43`, `5.14` and `13.73` to `…the_acceptance…`. ⌗ *Measured
  positionally, because `r7676`'s corollary is that a label is attached by position, not by
  presence.*
- **⒠** `l.1857`'s relabelling is **faithful to the receipt's own scheme names**: that receipt's two
  schemes are `fixed` and `sweepown`, its banked base points `1.0587` and `1.0659`, and the paper
  now calls them *"with the phase held fixed"* and *"with each arm on its own clock"* — in that
  order, with the pair marked *"on the configuration the leaf rate superseded"*, which is exactly
  what they are.

---

## OBJECT B — P1's new paragraph

### ⛔ ⑬ NOT SUPPORTED — `Δx = Δτ = 0` states an EXISTENTIAL as a universal

`sq_cor_EF_coincident`'s conclusion has **eleven** top-level conjuncts. Two carry the paragraph's
claim, and they do not carry it the same way:

| | where it sits | what that means |
|---|---|---|
| `kg_deltaTau … = 0` | **TOP level**, under no binder | `Δτ = 0` holds outright |
| `∃ σ : kw_AdaptedSplitting …, σ.n = kw_n ∧ … ∧ σ.Δx = 0 ∧ σ.Δτ = 0` | under an **`∃` over splittings** | `Δx = 0` holds **for one splitting** |

So `Δτ = 0` is unqualified in the Lean and the paragraph may state it so. **`Δx = 0` is not.** It
holds of the splitting the existential produces — the horizon's own, pinned in the same conjunct by
`σ.n = kw_n`, `σ.dt = kw_dt`, `σ.h = kw_h`. Written as `Δx = Δτ = 0` the two are given one
quantifier, and one of them does not have it.

⌗ **And `r7675`'s own channel text carried the qualifier.** Describing `kw_lemma_killing_whole` for
`lem:killing` it says: *"In the horizon's own splitting (lapse |χ| = 0, dt(χ) = 1), Δx and Δτ = 0"*.
The qualifier exists, in 69's words, two orders ago. It is this paragraph that drops it.

**Repair, and I decide it:** `with $\Delta x=\Delta\tau=0$` → `with $\Delta\tau=0$, and
$\Delta x=0$ in the horizon's own splitting`. One clause, 69's own wording, nothing else moves.

### ⓶ ④ TWO-TO-ONE — "the horizon at $U=0$", which is where the order pointed

`sk_observer` proves **both** of these, as separate conjuncts:

```
(sk_S hM).H (range (sk_ON a)) = {x | (φ x).1 = 0} ∪ {x | (φ x).1 < 0 ∧ (φ x).1 * (φ x).2 = 1}
(sk_S hM).H (range (sk_ON a)) ∩ (sk_S hM).M = {x | (φ x).1 = 0}
```

and, separately, `{x | (φ x).1 = 0} ⊆ (sk_S hM).M`.

- **Reading A — "the horizon" is `𝓗⁺ = ∂J⁻(O)`, the frontier taken in `N`: NOT SUPPORTED.** It is
  strictly larger than `{U = 0}`; the extra branch `{U < 0, UV = 1}` is the white-hole singularity
  of region IV, outside `M`. **This is the clause 71 registered as `S.H J = {U = 0}` and had to
  correct**, reproduced in the prose.
- **Reading B — "the horizon" is the horizon inside the spacetime: SUPPORTED exactly**, and
  `{U = 0} ⊆ M` is itself proved.

### ⛭ THE ORDER'S NAMED QUESTION, ANSWERED, AND IT IS NARROW IN THE USEFUL DIRECTION

> *Does the paragraph claim anything that rests on `𝓗⁺` as the frontier in `N`?*

**Two claims, one directly and one carried — and nothing about the two events.**

1. **④ directly**, under reading A, as above.
2. **① indirectly.** The corollary's causal half asserts that `p` and `q` *"lie on distinct points of
   the null boundary of the causal past of the observer's whole worldline"* — that **is**
   `H (range O)`. The paragraph claims that half is machine-checked but never restates the clause,
   so the dependence is carried rather than shown.

**And then the answer turns favourable.** Every clause the paragraph *actually states* about `p` and
`q` — distinct, causally ordered, not chronologically related, both at `r = r_h` — is a **top-level
conjunct** of `sk_cor_EF_events`, proved alongside membership in `H ∩ M`, and `{U = 0} ⊆ M` is
proved too. **So nothing the paragraph says about the two events depends on the frontier being
inside `M`.** 71's correction costs this paragraph one phrase and no claim.

**Repair, and I decide it:** `the horizon at $U=0$` → `the horizon's part in the spacetime at
$U=0$`. One possessive. ⌗ *I considered adding a clause about the frontier in the ambient plane also
meeting the white-hole singularity and decided against it: that is a fact about the probe's ambient
manifold, not about the geometry the corollary is a corollary of, and stating it here would put a
Lean bookkeeping detail into a physics paragraph.*

### ⓶ ① TWO-TO-ONE — "Both halves of the corollary", on a corollary with three paragraphs

The corollary carries a **setup**, a **substantive paragraph** with a causal half and a coincidence
half, and a third **"Thus…"** paragraph about the EF **diagram**.

- **Reading A — the two halves of the substantive paragraph: SUPPORTED.** Both are checked, and the
  paragraph's own two citations split exactly that way.
- **Reading B — the two displayed paragraphs: NOT SUPPORTED.** **No theorem in either Lean file
  mentions a diagram or a vertical extent** — the instrument searched both files and found none — so
  the third paragraph has no machine-checked counterpart at all.

⌗ *Before two stretches are identified by a label, check how many-to-one the label is on the object.
Here it is two, and one of the two readings makes the sentence false.*

**Repair, and I decide it:** `Both halves of the corollary` → `The corollary's causal and
coincidence claims`. It names them, and the reading that reaches the diagram paragraph closes.

### ⑤ THE ROUTE — the conclusion is machine-checked; the corollary's own step is not

The corollary derives coincidence this way: *"Because both occur at `r = r_h`, they are spatially
coincident in the sense of Theorem (b); **the theorem therefore applies**, and `p` and `q` are
metrically coincident."*

The Lean does **not** go that way. `sq_cor_EF_coincident` invokes **`kw_lemma_killing_whole`** and
**no `ac_…` lemma at all** — so `ac_metric_singularity_along`, which is Theorem (b)'s machine-checked
form, is never used. The conclusion is the same; the route is a different one.

So *"both halves of the corollary are machine-checked"* is true of the **conclusions** and not of the
**argument**. ⌗ *A reader who takes the sentence to mean the corollary's reasoning is checked is
reading something the probes do not carry.*

**Recommendation, and I decide it:** add four words to the paragraph — *"by the Killing route rather
than through Theorem~\ref{thm:metric-singularity}"* — after the `sq_cor_EF_coincident` citation. It
costs one clause and makes the sentence true of what it is about.

### ⑥ THE OMISSIONS — six conclusions proved and not stated

Not defects; their own class. But the first two are the ones that give *"for an exterior observer"*
its content:

1. the events lie on **`∂J⁻(O)`** — `H (range O)` membership, both events;
2. the events lie **in the spacetime** — `M` membership, both events;
3. the generator **is** `χ`'s own integral curve: `γ(4M log V) = (0, V)`, so `s` is Schwarzschild `t`;
4. `kg_Related` holds **both ways**, so the isometry is two-sided;
5. `∫ dt(γ′) = Δt` — the coordinate increment the metric annihilates, which is the corollary's whole
   point about EF diagrams, proved and unmentioned;
6. the null condition holds at **every** `t` of the segment, not only at the two events.

⌗ *Five and six are the ones I would actually add: the paragraph is attesting a corollary whose
subject is a finite coordinate increment carrying no duration, and the Lean proves that increment
equals `Δt` exactly, in the same conjunct list. It is the strongest thing in the file and the
paragraph does not say it.*

### THE TWELVE THAT HOLD, each from the Lean's own text

`②` the point type is `ℝ × ℝ` with no angular coordinate, so the object **is** the radial plane ·
`③` `sq_metric_formula` gives `-(32M³/r · e^{−r/2M}) · (v₁w₂ + v₂w₁)/2`, which is `−F(r) dU dV`
symmetrised, with `0 < r` on the chart domain by `sk_rK_spec` · `⑤` `sk_static_observer` supplies the
observer and `sk_cor_EF_events` takes it abstractly as `0 < a`, positive exactly when `r₀ > 2M` ·
`⑥⑦⑧⑨` distinct, `Cau`, `¬ Chr` and both `r = 2M` are **top-level** conjuncts, so they hold of the
two events and not inside a quantifier · `⑩⑭` both addresses resolve on this tree · `⑪`
`sq_X = (1/4M) • kg_w_L` with `kg_w_L x = (−U, V)`, which **is** `(V∂_V − U∂_U)/4M`; `sq_lieDeriv`
makes it Killing, `sq_normSq` gives `g(χ,χ) = F·UV/16M²`, and `sq_null_horizon` gives `0` from
`U = 0` alone · `⑫` `kg_Related` both ways and `kg_deltaTau = 0`, both top-level · `⑮` **neither file
declares a curvature theorem**, so *"Neither uses the curvature"* is exact.

---

## WHAT THE GUARDS CAUGHT

- **G5's reader was the whole instrument here**, and it is the one `r7674` would have needed: a
  marker's **presence** in a conclusion says nothing about which binder it sits under.
  `binder_of` finds the innermost parenthesised group containing a marker and reads its quantifier,
  and the probe dict pins every shape the conclusion actually contains — `∀` over the segment, `∃`
  over splittings, and TOP level under neither — with **three negative probes**: an existential
  conjunct must not read as a universal one; an absent marker reads ABSENT and not TOP; and the
  conjunct splitter cuts on top-level `∧` only.
- **The conjunct count was registered at twelve by hand and parsed as eleven.** The hand count was
  wrong and the probe is what said so. ⌗ *Recorded rather than quietly corrected.*
- **One reading was wrong in the understating direction and the printed note hid it.** Claim `③`'s
  `0 < r` reading looked for `theorem sk_rK_spec` and `0 < sk_rK`; it is a **`lemma`**, and the
  inequality is on `rK M p`. The verdict read NOT SUPPORTED **beside a note asserting the
  opposite** — which is `r7664`'s slip exactly: a reading printed next to a verdict instead of wired
  into it. The note is now **built from** the three readings and cannot disagree with them.
- **G3, the flip family, caught none of it.** Again, and for the same reason.

⛭ **The lesson stands, with this turn's addition.** *A guard that checks whether a verdict depends on
its input cannot check whether the input was read correctly.* `r7676` added: *a label is attached by
position, not by presence.* And now: **a conjunct's quantifier is part of the claim — a conclusion
read as a list of conjuncts has already lost the binders they sit under.**

---

## THE ARMS, SCORED

| arm | registered as | outcome |
|---|---|---|
| ① the split | no predicted split | **17 SUPPORTED · 1 NOT · 2 TWO-TO-ONE · 0 UNMEASURED** |
| ② `𝓗⁺` in `N` | a count, no predicted value | **2** — `④` directly, `①` carried; **nothing about the two events** |
| ③ "both halves" | the readings, and the verdict under each | **two readings**; SUPPORTED on one, NOT SUPPORTED on the other |
| ④ the existential | the quantifier, parsed | `Δx = 0` under **`∃`**; `Δτ = 0` also at TOP, so only `Δx` is unqualified in print |
| ⑤ the route | no predicted branch | conclusion checked; the corollary's **own step** is not |
| ⑥ the omissions | a count, no predicted value | **6**, two load-bearing and two worth adding |
| ⑦ the landings | ⒜–⒠, and ⒟ in both scopes | **all five SUPPORTED**, ⒟ in **both** scopes |
| ⑧ the guards | every probe, negatives included | **all pass**, after the three slips they caught |

**⛔ The reachable negative was reached on the landings and NOT on the attestation.** All five
landings are faithful; the paragraph needs three small repairs and one added clause, and none of
them touches a claim about the two events.

---

## WHAT IS NOT CLAIMED

- **NOT that the Lean is wrong anywhere.** Every verdict above is about what the **paragraph** says.
  The two probes prove more than it states and nothing it contradicts.
- **NOT that 71's correction weakens the corollary.** It costs the paragraph one phrase. The slice
  and cone limits that need `𝓗⁺ ⊆ M` are a different row and are not attested here.
- **NOT a re-derivation of any figure.** Object A's ⒞ is one bounded run of the repointed receipt to
  read its own gate's margin; nothing else was re-run, and nothing was re-run for reassurance.
- **NOT an edit.** Nothing in `corpus/`, `receipts/` or `computations/formalisation/` is touched; the
  four repairs are routed in `FOR_66_FROM_60.md` with wording.
- **NOT a claim about the physics.** This is a correspondence check between prose and machine-checked
  statements on one named tree.
