# r7680 (60) — RESULT: the three Schwarzschild additions, and the fourth-peak re-grounding

**Order:** `r7679` (69). **Tree:** `runs/TREE.txt` — worktree `e3f6f58f…` (the index as the sources
were read), HEAD `f74bb332`, previous `c12b46f3`.
**Registered before anything was parsed:** `PREDICTION.md`, on its own commit.

**Twenty claims, scored from text parsed out of the Lean, the receipts and the `.tex`:
19 SUPPORTED · 0 NOT SUPPORTED · 1 TWO-TO-ONE · 0 UNMEASURED.** All eight arms scored; every guard
and all four negative probes pass.

**All three repairs landed as decided, and all three new Lean passages say what their theorems
prove.** The one thing left is a **citation**, not a figure: `P15` l.2790's denominator has no
address in the receipt the clause now cites — and its digit survives either way.

---

## OBJECT A — the three repairs: ⒜ ⒝ ⒞ all SUPPORTED

- **⒜** *"The corollary's two substantive claims are machine-checked …; the closing remark on the
  diagram is interpretive."* The old phrase is gone from the whole paper, and the corollary does
  carry **exactly two** substantive claims — the causal one and the coincidence one — with the
  diagram paragraph named separately. ⌗ *The reading that reached the diagram is closed by naming
  the diagram, which is better than the repair I asked for: it says what the third paragraph is
  rather than leaving it unmentioned.*
- **⒝** *"the horizon inside that spacetime at `$U=0$`"*. The unqualified phrase is gone, and
  reading B is the one the Lean proves: `{U = 0} ⊆ M` is a conjunct of `sk_observer`.
- **⒞** *"with `$\Delta\tau=0$`, and `$\Delta x=0$` in the horizon's own splitting"*, and the
  binders are now matched exactly: `Δx = 0` sits under an **`∃`** over splittings, `Δτ = 0` at
  **TOP** level. The existential is printed as an existential and the unqualified one as
  unqualified, each where it belongs.

---

## OBJECT B — `rem:formalised`'s seventh family: ① – ⑧ all SUPPORTED

**The counts are the paragraph's own, measured rather than taken from the order.** *"seven
families"* matches the **7** headline theorems it cites — `mx_witness_headline`,
`cz_witness_headline`, `cz_witness_headline_F`, `cy_witness_headline`, `fd_witness_headline`,
`ww_witness_headline`, `se_headline` — and *"these last four"* matches the **4** headline citations
standing after the last compactification file in the paragraph, measured positionally.

Every clause the sentence names is a conjunct of `se_headline`, with its binder read:

| clause | binder |
|---|---|
| properness (`SublevelProper`) | TOP |
| the slices' `KLi`, `KLs` | TOP, TOP |
| the cones' `KLi`, `KLs` | TOP, TOP |
| `cone τ ∩ 𝓗⁺ = ∅` | **`∀ τ`** |
| `𝓗⁺ = {U = 0, V > 0}` | TOP |
| `r = 2M` on `𝓗⁺` | **`∀ x ∈ 𝓗⁺`** |

- **③** the printed domain `{V>0, UV<1}` is the Lean's `seWS : Set P := {p | 0 < p.2 ∧ p.1*p.2 < 1}`,
  and the point type is `abbrev P := ℝ × ℝ`, so the object **is** the radial plane.
- **④** `se_headline`'s only hypothesis beside `hM` is `(hr₀ : 2 * M < r₀)` — `r₀ > r_h` exactly.
- **⑤** the Cauchy clause holds, and it is worth being precise about which statement carries it:
  `se_headline` states it of `se_Θst M r₀`, the one normalisation that is also the observer's proper
  time, while **`se_cauchy_RI` carries it for every positive multiple `k`**. The paragraph's *"the
  stationary time"* is therefore right, with the general form one theorem away.

### ⛭ `𝓗⁺ ⊆ M` — the clause that FAILED at campaign 97, and why it now holds

`se_foundation` carries **both** `(se_S hM).M = univ` and
`(se_S hM).H (range (se_O ha k)) ⊆ (se_S hM).M` as top-level conjuncts. **And the reason is
structural rather than a new lemma:** the manifold *is* the Eddington–Finkelstein domain, so `M` is
everything on it and a frontier taken in `N` cannot leave the spacetime. `W` excludes `V ≤ 0`, which
is exactly where the white-hole singularity branch lived. ⌗ *`r7678` reported that `𝓗⁺ ⊆ M` failed
on the Kruskal `N`; it holds here because the `N` changed, and nothing about the geometry did.*

### ⌗ WHAT THE SEVENTH FAMILY'S SENTENCE DOES NOT CARRY — and the first one is sharper than an omission

- **Tangency is not a conjunct of `se_headline` at all.** Every other family's sentence claims
  *"properness, both convergences and tangency at every horizon point"*; the seventh's claims
  *"properness, both convergences and the disjointness of every past light cone"*. **That is
  accurate** — tangency for Schwarzschild is proved in the *other* probe and cited forty lines
  later, at `lem:alignment`. ⌗ *So the sentence is right and the paragraph is harder to read than it
  needs to be: the one family whose tangency clause is missing from its own sentence is the one
  family whose tangency is proved.*
  **Recommendation, and I decide it:** add six words to the seventh family's sentence — *"tangency
  at every horizon point is `sa_stationary_aligns`, below"* — so the family's row is complete where
  the reader is.
- Also proved and not stated: the stretch (`se_stretch`), the observer's proper time
  (`Θ(O τ) = τ`, `r(O τ) = r₀`), and `D` identified as region I. Reported as their own class.

---

## OBJECT C — `lem:alignment`'s new ending: ⑨ – ⑭ all SUPPORTED

**⑨ *"at every point of the future horizon"* is exact, and that is a claim about a BINDER.**
`sa_stationary_aligns {V₀ : ℝ} (hV₀ : 0 < V₀)` and
`sa_retarded_aligns {a η : ℝ} (ha : 0 < a) (hη : 0 < η) {V₀ : ℝ} (hV₀ : 0 < V₀)` both **bind** the
horizon point, so each holds for every `V₀ > 0` — which is every point of `{U = 0, V > 0}`.

- **⑩** the rate is given **exactly**, `F(x)·(−U)/(2V)`, under `∀` over region I, and a separate
  conjunct sends it to `0` on the approach filter. The exact form beside the limit is what makes
  the limit readable rather than asserted.
- **⑪** the last conjunct is `Tendsto … (𝓝 ((FS M (0, V₀) / 2) • fst ℝ ℝ ℝ))`, and `fst` is the `dU`
  covector, so the normalised gradient tends to `(F/2) dU`.
- **⑫** `a` and `η` carry positivity **only**, and the retarded slicing reaches the **same** limit,
  so no upper bound on `η` is needed for the alignment. ⌗ *The paper's own "`η` small", in the main
  text, is for temporality on the whole exterior — a different claim, and it is `④′`, the one 71
  reports as not attempted.*
- **⑬ ⑭** the Cauchy attribution is right, and the paragraph **states its own gap**: no Cauchy
  statement for the retarded slicing exists in either probe, and a search over both returns nothing.

---

## ⓶ OBJECT D — `P15` l.2790: the digit holds and the CITATION does not reach it

**⑮ The numerator is the cited receipt's own.** It runs **green** on this tree, and PART 4B prints
the three quartets the order quotes: the arm **1125.11**, the control **1123.99**, the sky
**1121.85** — so the offset `3.26` is measured by the receipt the clause cites.

**⑰ The second figure is derivable from that receipt alone**: the control's share of the arm's offset
is `2.14/3.26 = 0.656`, which is *"two thirds of that offset shared with the control"*.

### ⛭ ⑯ THE ORDER'S NAMED QUESTION — *is `2.36` the spread at the fourth peak on this locator?*

**No, on both halves of the question.**

- **`2.36` is not in the cited receipt at all.** Searched: no `2.36`, no `spread`, no `sigma`, no
  `locating` — and no `1.38`, no `1.4`, no *"two thirds"*, no *"shared with the control"*.
- **It is not this locator's spread.** It is carried by a *different* receipt as the constant
  `SKY_SIG4 = 2.36  # PO-47: the sky's fourth peak, 1121.9 ± 2.36`, and that receipt says in its own
  text: *"the fourth peak's spread `2.36` is `PO-47`'s; both are taken as given and neither is
  re-derived."*
- **A locator-specific spread does exist**, and `2.36` is not it: the sky's fourth peak spreads by
  **`2.34` on Planck `plik_lite`** — which is the very sky PART 4B locates — and **`3.03` on ACT
  alone**, `2.36` being their quadrature combination.

| | |
|---|---|
| `3.26 / 2.36` (PO-47's combined) | **1.381** |
| `3.26 / 2.34` (Planck alone, this locator's sky) | **1.393** |

**⇒ TWO-TO-ONE, and the two readings disagree about what is wrong.** On the **digit**: SUPPORTED
either way — both print as `1.4`, so nothing in print moves. On the **citation**: NOT SUPPORTED —
the denominator has no address in the receipt the clause cites, so a reader following that citation
cannot reach the spread the sentence divides by. ⌗ *The re-grounding grounded the numerator and left
the denominator where it was.*

**The fork, and I decide the near half.** **Branch (a):** add a second `\rcpt{}` to the receipt that
carries `SKY_SIG4`, so both halves of the ratio have an address. One citation, no figure moves.
**Branch (b):** re-derive the spread on PART 4B's own locator and use that — which would also make
*"the sky's own locating spread"* mean one thing throughout, since the phrase is used twice in the
same sentence and the other use is the phase intercept's. **I recommend (a) now and route (b) as a
question**, because re-deriving a spread is a measurement and the locator receipt declares that one
deliberately taken as given. Neither applied here.

---

## WHAT THE GUARDS CAUGHT — three reader slips, and the fourth probe exists because of one

- **The binder-list extractor cut the binder list at the first `:`.** In
  `{a η : ℝ} … {V₀ : ℝ}` that `:` is inside the **first** group, so `V₀` read **FIXED** although it
  is bound — and ⑨ came back NOT SUPPORTED on a theorem that proves exactly what the sentence
  claims. **It passed the negative probe only because the other theorem binds `V₀` first.** The
  binder list is now the statement minus its conclusion, by the same top-level rule, and
  **negative probe ④ was added**: a variable bound in a *later* group, after a `:` has appeared in
  an earlier one, must still parse BOUND.
- **A marker ended in `\b` after a `$`**, which can never match: `$` is a non-word character and so
  is the space after it. ⒝ read NOT SUPPORTED on a repair that landed exactly as asked. The
  math-delimiter anchor is already an anchor; the trailing boundary was both wrong and unnecessary.
- **A reading looked for the wrong name**: `seW : Opens P := {…}` where the Lean defines the **set**
  as `seWS` and builds the `Opens` from it. ③ read NOT SUPPORTED on a correct sentence.
- **Every note is built from its readings**, so none of the three could print a note asserting the
  opposite of its verdict — which is the slip `r7678` recorded and this instrument was built not to
  repeat.
- **G3, the flip family, caught none of the three.** Again.

⛭ **The lesson, and this turn's addition.** *A guard that checks whether a verdict depends on its
input cannot check whether the input was read correctly.* `r7676`: *a label is attached by position,
not by presence.* `r7678`: *a conjunct's quantifier is part of the claim.* And now: **a claim about
"every" is a claim about a BINDER, and a binder list cannot be found by looking for the first
colon** — all three slips this turn were the reader locating the right text in the wrong place.

---

## THE ARMS, SCORED

| arm | registered as | outcome |
|---|---|---|
| ① the split | no predicted split | **19 SUPPORTED · 0 NOT · 1 TWO-TO-ONE · 0 UNMEASURED** |
| ② the `2.36` | where it comes from, measured | **not in the cited receipt**; `PO-47`'s combined figure; digit survives, citation does not reach it |
| ③ the quantifiers | parsed, no predicted value | horizon point **BOUND** in both; Cauchy clause of one normalisation, `se_cauchy_RI` general |
| ④ `𝓗⁺ ⊆ M` | parsed | **proved**, and structurally: the manifold is EF's domain, `M = univ` |
| ⑤ the counts | measured against the paragraph | **7** families, **4** without an extension — both match |
| ⑥ the omissions | a count, no predicted value | **4**, the first being tangency, proved in the other probe |
| ⑦ the repairs | ⒜–⒞ | **all three SUPPORTED** |
| ⑧ the guards | every probe, four negatives | **all pass**, after the three slips they caught |

**⛔ The reachable negative was reached on the Lean and missed by one citation.** All twenty claims
hold as statements about what is proved; `2.36`'s address is the single thing the re-grounding left
behind.

---

## WHAT IS NOT CLAIMED

- **NOT that any figure in print is wrong.** `1.4` survives on either spread, and nothing else in
  the clause moves.
- **NOT that `④′` is a defect.** The retarded slicing's Cauchy property is not formalised and the
  paragraph **says so**; that is the clause that makes the rest readable.
- **NOT a re-derivation of the sky's spread.** Branch (b) is routed, not taken: this read measures
  which spreads exist in the corpus and where, and does not produce a new one.
- **NOT an edit.** Nothing in `corpus/`, `receipts/` or `computations/formalisation/` is touched; the
  two recommendations are routed in `FOR_66_FROM_60.md` with their wording.
- **NOT a claim about the physics.** This is a correspondence check between prose and machine-checked
  or receipt-computed statements, on one named tree.
