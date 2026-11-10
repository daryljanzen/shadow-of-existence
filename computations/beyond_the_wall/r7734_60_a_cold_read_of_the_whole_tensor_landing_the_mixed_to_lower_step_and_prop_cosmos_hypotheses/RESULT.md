# `r7734` (60) — RESULT

**Answers order `r7731`.** `PREDICTION.md` was committed and pushed in its own commit before
`probe.py` existed. **70 arms, 56 distinct tags, exit `0`, two failing — and both failures are the
two stale Lean headers the order has already assigned to `71`.** ⚠ Two instrument defects were
reached and fixed first, reported at `⑤`.

---

## ⌈ ① THE FIRST QUESTION: THE INDEX POSITION IS NOT THE GAP. THE CHART IS.

**The question.** Is *"`T_{μν} = 0` if and only if (`vacode`)"* what `ok_vacuum_iff_ode` **with**
`es_G_offdiag` delivers, given that one is stated with **mixed** components and on an interval?

**⛭⛭ The mixed-to-lower worry dissolves, and the prediction registered that it might.** I recorded
in advance that I did not know whether the order was pointing at a real gap or at one that would
vanish on inspection — and that not knowing is exactly the condition under which this seat has gone
wrong before. So the arm **computed** it: `T_{μν} = g_{μα} T^α_ν` is a **multiplication**, so a
vanishing mixed tensor gives a vanishing lower one with **no invertibility used at all**,
`g · 0 = 0` entrywise. The negative control confirms the arm discriminates: one non-zero mixed
entry lowers to `−c·A(r)`, not to zero. ⇒ **`N1`'s first reading is refuted. The order's "stated
with mixed components" is not by itself a gap.**

**⚠ But the real condition sits one level earlier, and the sentence does not state it.** `es_G` is
**defined through the inverse metric**, so it exists only where that does — and `es_Hyp` carries
`hA : A(x 1) ≠ 0` and `hF : F(x 1) ≠ 0`. On the construction gauge `es_construction_gauge` takes
`es_Hyp f f x f2`, so **the hypothesis is `f(r) ≠ 0`, which fails at every horizon.** The paper's
sentence quantifies over `(r₁,r₂) ⊂ (0,∞)` and says nothing about `f ≠ 0`.

⌗ **And yet this is the chart's condition rather than an extra hypothesis.** `eq:gauge` writes the
radial term as `dr²/f(r)`, which is undefined where `f = 0`: computed, `g_rr = 1/f → ∞` as
`f → 0⁺`, so **a horizon is not a point of this chart at all**. The gauge excludes the horizons by
its own form. ⇒ **The sentence inherits a restriction its own equation already carries, silently.**
Whether that wants a clause is a judgement, and `⑦` states mine.

**⚭ The mismatch runs both ways, which is the sharper half.** `ok_vacuum_iff_ode` carries **no**
non-vanishing hypothesis — its binders are `(ha : 0 ≤ a)` and two differentiability conditions — so
**the diagonal half is stated on the whole interval while the off-diagonal half needs `f ≠ 0`.** The
two halves of one sentence hold on different sets.

**And the quantifications differ in shape, not only in extent.** `ok_vacuum_iff_ode` is quantified
over `∀ r ∈ Ioo a b`; `es_G_offdiag` is stated **at one point `x` for one index pair**, with the
index pair universally quantified (`(b c : Fin 4) (hbc : b ≠ c)`). So *"every off-diagonal
component"* **is** delivered — but **the conjunction of the two halves is assembled by the reader
and is stated by no declaration.** `N2` is reached in this precise sense: not that the composition
fails, but that it is nowhere written down.

---

## ⌈ ② WHAT THE REST OF THE LANDING DELIVERS, READ FROM CONCLUSIONS

- **`es_sds_vacuum_full` is quantified over every index pair** — `(b c : Fin 4)` — so `4 × 4 = 16`,
  and *"a vacuum in all sixteen components"* is **exact**. The cosmological term is added on the
  diagonal only (`+ (if b = c then Λ else 0)`), which is what a vacuum with `Λ` means, and
  `es_sds_witness` exhibits a concrete point. `N3` not reached.
- **`es_Ric_offdiag` and `es_G_offdiag` both conclude `= 0` at a universally quantified off-diagonal
  index pair.** *"Every profile"* ranges over a **pair** `(A, F)` under `es_Hyp`, which is **wider**
  than the gauge `A = F = f` the paper applies it to — so the declaration is the stronger statement
  and the prose the weaker. `N4` not reached.
- **The index clause.** *"as a linear map `C¹[r₁,r₂] → C⁰[r₁,r₂]` its index, `dim ker − codim
  range`, is `1`"*. A named search over `ok_index_one`'s statement for a dimension or a codimension
  returns **no hit**; it still states four conjuncts. ⇒ **`N5` is reached in substance and is not a
  defect.** `r7732` reported that the clause asserted an integer without naming what it meant; the
  new wording **names the arithmetic the reader must do**. The step is now visible where it was
  silent, which is the repair available without formalising Fredholm theory. *Saying what you are
  not checking is the whole of the discipline here, and this is an instance of it.*

---

## ⌈ ③ THE SECOND QUESTION: THE PROSE MATCHES, AND THE LAW IS EXACT

**`rg_cosmo`'s structure matches the prose's structure, clause for clause.** The prose reads *"a
radial geodesic conserves `E = f ṫ` and, unit timelike, obeys `ṙ² = E² − f`"*. The conclusion is a
three-fold conjunction: the energy's derivative vanishes; `∃ E, ∀ τ, f(R τ)·T′ τ = E`; and
**`(∀ τ, −f(R τ)·T′ τ² + R′ τ²/f(R τ) = −1) → ∃ E, ∀ τ, R′ τ² = E² − f(R τ)`**.

⚭ **"Unit timelike" is the hypothesis of an implication *inside* the conclusion, not a binder** — so
the prose's appositive is not loose wording but an exact match for the statement's shape: **the
energy holds unconditionally and the radial law only when unit timelike.** `N6` not reached.

**⛭ And the law was checked, not merely compared.** Comparing a prose hypothesis with a Lean binder
is a form-to-form comparison, and both could agree while neither is what a unit timelike curve
satisfies. So the normalisation was imposed on the metric the file declares and `ṙ²` solved for
independently: `g(u,u) = −1` with `E = f·ṫ` gives **`ṙ² = E² − f` exactly, residual `0`.** The
negative control: the **null** normalisation `g(u,u) = 0` gives `ṙ² = E²`, which is **not** the
same — so *"unit"* is load-bearing rather than decorative. `N7` not reached.

⚠ **`rg_cosmo` carries the same chart condition the whole-tensor sentence leaves silent**
(`hf : ∀ τ, f(R τ) ≠ 0`), and the `prop:cosmo` sentence does not state it either. ⇒ **The condition
is implicit in the chart in both places, consistently** — which is an argument for leaving both as
they are, or for saying it once where the gauge is introduced. `⑦` takes the second.

**The four other `rg_*` declarations exist in the file cited and conclude what their position
implies**, each read from its conclusion: `rg_witness` a concrete Minkowski geodesic (`f = 1`, so a
reader can check it by hand, and `rg_cosmo` is not vacuous); `rg_sinh23` the `sinh^{2/3}` scale
factor; `rg_sinh23_radial` its radial form; `rg_tau23` the `Λ = 0` collapse limit. `N8` not reached.

**Every one of the twenty names P8 cites is declared in `StaticEinstein.lean`, the only Lean path
P8 names** — the nine older `ok_*` names among them, declared there and in `OperatorKernel.lean`
both, as `⑤` of `r7732` established and the order settled.

---

## ⌈ ④ THE P3 REPAIR IS TRUE, AND THIS TIME IT LEFT NO TWIN

The parenthetical now reads *"(three real roots, distinct except at the designations `r₀ = ±1/√3`:
the undercritical regime)"*, and the form it replaced is gone — `0` occurrences of *"three distinct
real roots"* anywhere in P3.

**And it is true.** Over `47,998` designations in the open interval, **both signs**, `0` have a
repeated root away from `r₀ = ±1/√3`; and both named designations **are** among them —
`r₀ = +0.577350269` with `2M = +0.384900179460` and roots `[(−1.154700538, 1), (0.577350269, 2)]`,
`r₀ = −0.577350269` with the mirror pair. The `±` is what the computation requires and the
parenthetical carries it.

**No twins.** `0` occurrences of the old gloss, of the struck *"equivalently"*, or of the old region
scope. ⌗ *And the region sentence states distinctness directly rather than through the term, so it
does not depend on this parenthetical at all — which is why the repair could be local.* `N9` not
reached.

**`N10` is not reached either**: the repair that formalised the off-diagonals took its own caveat
with it. Exactly one *"not formalised"* clause remains in P8 — the index-constancy citation, which
is still genuinely unformalised — and the narrowing itself is gone: the sentence now claims
`T_{μν} = 0` whole. ⇒ **My `r7732` answer has been overtaken rather than contradicted**, and the
clause it turned on was removed with it instead of being left standing.

---

## ⌈ ⑤ TWO INSTRUMENT DEFECTS, AND THE FIRST IS THIS PROBE'S OWN DECLARED PRECAUTION MISIMPLEMENTED

1. **⚠ The statement reader bounded a statement at the first depth-zero `:=` rather than at the
   `:= by` that begins the proof.** `rg_sinh23_radial`'s conclusion **contains** a depth-zero `:=`
   of its own — `let r := …` — so the reader truncated the statement to `let r` and the arm read
   the truncation as a conclusion that did not say what it says. ⚠ ***This probe's own docstring
   declares the precaution as "bounded by the `:= by` that begins a proof" — and I coded "the first
   depth-zero `:=`".*** Fixed: the bound is a depth-zero `:=` whose next non-whitespace token is
   `by`, with a term-mode fallback, and the reader is now given that exact case as its negative
   before use — `268` characters, carrying both `let r` and `sinh`.
2. **A plain logic error in the citation test.** The first form asked whether the **filename**
   `StaticEinstein.lean` was among that file's **declaration names** — never true — so the `or`
   short-circuited and **all twenty** cited names were flagged missing. ⌗ *It was caught because the
   witness printed each name beside the file that declares it: twenty "missing" names, every one of
   which the printout showed present. A disjunction in a test is a place to look.*

⌗ *Both printed a verdict that was wrong in a way the verdict alone could not show — one a
truncation that looked like a short conclusion, the other a failure list that contradicted its own
witness. Fifth consecutive revision in which printing the witness is what found the instrument's
failure.*

---

## ⌈ ⑥ THE ARMS AGAINST `PREDICTION.md`

| arm | registered as | reached |
|---|---|---|
| `A1` | the sentences in the FILE, not the order | **yes**, all three |
| `A2` | ⚠ the registered subtle part: is lowering a gap? | **NO** — computed free; the **chart** is the condition |
| `A3` | the domain step | **`N2`** — the conjunction is the reader's, stated nowhere |
| `A4` | "every profile" — what does it range over? | a **pair**, wider than the gauge; `N4` not reached |
| `A5` | "all sixteen components" | **exact**, with a witness; `N3` not reached |
| `A6` | the index clause | **`N5` in substance, and not a defect** |
| `B1` | `prop:cosmo` against `rg_cosmo`'s binders | **matches clause for clause**; `N6` not reached |
| `B2` | ⛭ the law derived from the metric, not compared | **exact**, residual `0`; `N7` not reached |
| `B3` | the four other `rg_*` from their conclusions | **all four hold**; `N8` not reached |
| `B4` | the citations enumerated | **20 of 20** |
| `C1` | is the P3 parenthetical TRUE? | **yes**, both signs, `47,998` designations |
| `C2` | ⚠ twins | **none**; `N9` not reached |
| `D1` | a stale caveat left by the repair that overtook it | **none**; `N10` not reached |
| `D2` | the two headers re-measured | **both still open**, and `71`'s by this order |
| `N11` | my instrument fails first | **reached twice**, `⑤` |

**Negatives reached: `N2`, `N5` (as an improvement rather than a defect), `N11` twice. Not reached:
`N1`, `N3`, `N4`, `N6`, `N7`, `N8`, `N9`, `N10`.**

---

## ⌈ ⑦ WHAT THIS REVISION OWES OUTWARD

**One clause offered, and nothing routed that the order has not already assigned.**

- **The chart condition, said once where the gauge is introduced.** Both machine-checked sentences
  inherit `f ≠ 0` from `eq:gauge`'s own `dr²/f(r)`, and neither states it; `es_Hyp` and `rg_cosmo`
  both carry it as a hypothesis. ⇒ **Offered, not routed**: one clause after `eq:gauge` — *"the
  chart is the region where `f ≠ 0`; the horizons are its boundary and are treated as turning
  points of the slicing curve rather than as points of this chart"* — would make every downstream
  interval honest at once, and is cheaper than qualifying each sentence. ⌗ *I register that this is
  a judgement and not a defect: the gauge's own equation already excludes them, so nothing in the
  paper is false as it stands.*
- **The reader's conjunction.** `ok_vacuum_iff_ode` and `es_G_offdiag` compose to the sentence's
  claim, and nothing states the composition. ⇒ **Offered**: one declaration conjoining them over an
  interval with `f ≠ 0` would make `T_{μν} = 0` machine-checked as a single statement rather than as
  two halves a reader joins. Not routed, because the two halves are each sound and the join is
  one line of Lean that `71` may prefer to place differently.
- **The two stale Lean headers**, re-measured and both still open: `OperatorKernel.lean` still says
  it backs P8's `thm:kernel` and `prop:bend` while P8 names it nowhere, and the header
  `StaticEinstein.lean` keeps verbatim still says *"it copies no earlier probe"* inside a file that
  is a copy. **The order has assigned both to `71`, so they are reported and NOT re-routed.**

**Nothing is applied to the register, and no file outside this revision's own directory is touched.**
