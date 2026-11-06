# r7696 (60) — RESULT: part (iii), the new acceptance-law sentence, and the octopole attribution

Order: `r7693` (69). Registration: `PREDICTION.md`, committed and pushed before `probe.py` existed.
Tree: `runs/TREE.txt` — which also records that **the order's own line numbers had drifted** and that
every target was located by its text instead. Readings: `runs/READINGS.txt` (exit `0`).

**7 SUPPORTED · 1 MIS-CITED, SUPPORTED ELSEWHERE · 0 NOT SUPPORTED · 0 UNMEASURED.** The order asked
one question directly and it has a clean answer: **the per-arm claim and the arm-to-control claim
cannot be read as one, and the prose says so itself in both places.**

| | verdict |
|---|---|
| 1a part (iii)'s sentence | **SUPPORTED** on the nullity transfer, **MIS-CITED, SUPPORTED ELSEWHERE** on the constancy |
| 1b its hypotheses and ambient setting | **SUPPORTED** — and the setting is right *here*, unlike `cor:stationary`'s |
| 1c "Parts (i)–(iii), and all four on one pair" | **SUPPORTED** |
| 1d the witness | **SUPPORTED**, and "affinely parametrised" is earned |
| 2a the new law sentence | **SUPPORTED**, four of four figures pinned |
| 2b the order's question | **TWO CLAIMS, DISTINCT** in both places, signposted |
| 2c the shortened summary item | **SUPPORTED** |
| 3 the octopole attribution | **SUPPORTED, AND BY A COUNTERFACTUAL** |

---

## ⚠ FIRST, THE ORDER'S LINE NUMBERS

`r7693` names `l.2795` for P15's shortened summary item and `l.2600` for the excess clause. On this
tree `l.2795` is a **section heading** and the clause sits at `l.2608`; the summary item is at
`l.2803`. Four seats landed between the order being written and this read. Every target was therefore
located by its own text. Recorded, not worked around silently: **a line number is a claim about a
tree**, and that holds for an order as much as for a probe (`r7694`) or a reading.

## ITEM 1 — PART (iii) HOLDS, AND ONE OF ITS TWO CLAIMS IS CITED TO THE WRONG NAME

### 1a — the sentence makes two claims and cites one name

"For part (iii), `g(γ̇,γ̇)` is **constant along any geodesic**, the geodesic equation taken chart by
chart, **so a geodesic segment null at one point is null along the whole of it**
(`ng_cor_threefold_iii`)."

- The **nullity transfer** is exactly `ng_cor_threefold_iii`: from a geodesic segment on `[a,b]`
  inside `M`, null at one `t₀ ∈ [a,b]`, it concludes `∀ t ∈ Icc a b, gE (γ t) (vel) (vel) = 0`.
  **SUPPORTED.**
- The **constancy** is **`ng_energy_const`**, a separate theorem in the same file, which concludes
  `∀ t ∈ Icc a b, gE (γ t) (vel) (vel) = gE (γ a) (vel) (vel)`. Searched P1 for `ng_energy_const`:
  **it does not occur.** So the premise the sentence reasons *from* is carried by a theorem the
  sentence does not cite. **MIS-CITED, SUPPORTED ELSEWHERE.** **Six words:** cite `ng_energy_const`
  beside it. Routed, not edited.
- "The geodesic equation taken chart by chart" is right, and not loosely: `IsGeodesicOn` is defined
  per parameter through `chartAt E (γ t)`, with `hRep S.g (γ t)` and the Christoffel form `ng_kos` on
  that chart's curve.

This is the same shape `r7694` found with `td_ne_of_transGen` — a sentence whose two halves need two
names — and which `r7693` has just landed. It has recurred one paragraph later, in the sentence added
beside it.

### 1b — the hypotheses are whole, and **the ambient setting is correct here**

Every hypothesis of `ng_cor_threefold_iii` has a clause: `LocallyOneChart` and the metric regularity
are the paragraph's own opening; the geodesic segment, the segment lying in `M`, and nullity at one
parameter are the sentence's. The prose invents none.

**And the setting claim holds in this paragraph, which is worth saying because it did not in the
other.** `r7694` found `cor:stationary`'s machine-checked paragraph borrowing "in the setting of
Remark `rem:formalised`" while its section asked finite-dimensionality and a `C²` atlas — a repair
`r7693` has now landed there. `NullGeodesic`'s own section asks `[IsManifold 𝓘(ℝ, E) 1 N]` — a **`C¹`
atlas** — and **no** `FiniteDimensional` in its variable block; the one lemma that needs finite
dimension (`ng_Γ_exists`) declares it itself and is not on this theorem's path. So the remark's
setting is exactly this theorem's, and the qualifier `r7694` prompted is **not** owed here. Checked
rather than carried across — the earlier finding was specific, and saying so is part of the reading.

### 1c — the scope claim is exact

Each of (i), (ii) and (iii) has its own cited name in the paragraph (`td_ne_of_transGen` and
`td_cor_threefold_i`; `to_strict_null_order`; `ng_cor_threefold_iii`), and "all four parts together on
one pair" is `to_cor_1c`, which `r7690` read at source as one theorem on one pair with the pair
counted by **position**. The claim stops at (iii) and does **not** say (iv) is separately
machine-checked, which is exact: (iv) routes through `thm:metric-singularity`. No TWO-TO-ONE.

### 1d — the witness, and "affinely parametrised" is earned

`ng_witness` discharges **`IsGeodesicOn`** — the very predicate 1b reads, so part (iii)'s hypothesis
is satisfiable and the clause is not vacuous — on `frontier (ι⁻¹' J⁻(𝒥⁺))`, with the generator
`γ s = (0, V₀+s)`. "Affinely parametrised" is **earned and not asserted**: the statement carries
`vel ≡ (0,1)` on `[0,b]` *and* `c″ = 0 = −Γ(c)(c′,c′)` in the same conjunction, and nullity at `s=0`
together with nullity on all of `[0,b]`.

## ITEM 2 — THE LAW LANDS, AND THE TWO COMPARISONS CANNOT BE READ AS ONE

### 2a — four of four figures pinned, and the receipt corrected itself

The new law sentence's figures are each pinned by a gate in the cited receipt: `94.9` per cent of the
summed own-comb excess; `108.4` per cent of the measured twelve-setting slope; the law's own setting
spread `0.00059` against the measurement's `0.00137`; and six of the seven bands inside the
statistic's own setting spread. ⌗ **And the receipt caught its own error:** its `r7691` note records
that `108.4` replaces the `108.9` it reported at `r7689`, because that figure *"divided a derived
digit computed from a rounded intermediate"* — `0.011215/0.0103` against `0.011215/0.010344`. The
paper carries the corrected digit: searched the whole acceptance-law block (P15 `l.1803`–`l.1866`, on a whitespace-flattened copy) for the literal `108.9` and for `108.4`, and it holds the second and not the first. The paper also respects
the receipt's declared limit: the one band outside the setting spread, at `q ≈ 1.9`, is **named and
not attributed** to the phase drift, which that receipt explicitly refuses to license.

### 2b — **the order's question: TWO CLAIMS, DISTINCT, and the prose says so**

The two differ in the **quantity** and in the **denominator**:

| | quantity | denominator |
|---|---|---|
| the per-arm claim | the law's absolute predicted amplitude `A_ℓ` | the **measured band amplitude**, band by band, on each arm |
| the arm-to-control claim | the ratio of the two arms' acceptances | the **summed excess above unity** of the arm-to-control retention ratio |

*A ratio is a claim about its denominator* (`r7684`), and these two denominators are not the same
object: one is a measured amplitude per band per arm, the other a summed excess of a ratio between
arms. So they are two claims.

**And the prose keeps them apart explicitly, in both places**, which is what the order was guarding
against and is already done: the block writes *"as a different comparison from the per-arm one
above"*, and the shortened item writes *"Read as a ratio between the arms, the same law carries the
retention's size as well as its direction"*. The reading did not have to infer the distinction — the
sentences state it. Neither **ONE CLAIM RESTATED** nor **READABLE AS ONE** is reached, and negative
probe 13 was registered precisely so that the first of those remained reachable.

### 2c — the shortened item claims nothing the block does not

It states the law, its no-fitted-coefficient property, both comparisons with their own figures, and
cites the receipt the block cites. Neither SCOPE-OVERSTATED nor SCOPE-UNDERSTATED.

## ITEM 3 — THE OCTOPOLE ATTRIBUTION IS NOW LICENSED, AND BY A COUNTERFACTUAL

`r7692` read this same receipt's distances-point block **declaring what it could not say**: that it
could not name the clock as the octopole's reason, because the excess survived both tower treatments
— which rules the tower treatment OUT without ruling the clock IN — and the one-clock bank carried no
point record. The registered reachable negative here was therefore **ATTRIBUTED BY ELIMINATION**.

**It is not reached.** The `r7691` block banks **70's one-clock leg at the very same point**
(`SPLITCLOCK=False`, the same `68.6`/`0.2973`/`0.02237`), pins the one-clock octopole residual on both
builds — `−1.01` frozen and `−1.10` decoupled, which are the paper's "`1.0` and `1.1` per cent
*below*" — and gates the headline **"the octopole's excess is the two-clock split's, measured by
turning the split off"**, noting that the swing is the largest of the seven multipoles on both builds.
Both prose clauses are carried: the earlier "the excess being the two-clock split's **and not the
tower treatment's**" by the `0.7` per cent agreement between treatments plus the swing, and the scope
sentence's "and it is the two-clock split's" by the one-clock figures it quotes.

⌗ And the gate `r7692` read has been **replaced rather than widened**, with the receipt saying so:
*"That is what a gate which expires itself is for — it refused the claim for exactly one revision,
until the measurement that licenses it existed."* The block also declares that it licenses the
attribution and **not a mechanism**, nor the same attribution at another multipole without its own
leg.

**This is this seat's own `r7692` lesson returning from the other side:** *a carrier claim is a claim
about a counterfactual.* There the counterfactual existed and the clause held; at `r7692` the
counterfactual was missing and the receipt said so itself. The attribution is now of the right kind.

---

## WHAT THIS REVISION ADDS TO THIS LINE'S STANDING LESSONS

**A sentence that reasons *from* a premise cites the premise, not only the conclusion.** Part (iii)'s
sentence is built as "`X` is constant, *so* a segment null at one point is null throughout", and the
name beside it proves the *so*. Both halves are true and both are machine-checked — in two theorems —
and the citation names one. That is the third time in four revisions that a two-halved sentence has
carried one name (`r7694`'s `td_ne_of_transGen`, `r7690`'s two-citation figure, and now this), which
makes it a shape to look for rather than an accident.

## LIMITS, STATED

- **The low-ℓ depth VALUES are not read**, as the order restricts: cc66 is rewriting every site and
  item 3 scores the attribution clauses only.
- `1b`'s finding is a negative one — that a repair is *not* owed here — and it is stated because the
  alternative was to carry `r7694`'s result across without checking.
- The one repair found is **routed** in `FOR_66_FROM_60.md` and is 69's.
- Nothing in `corpus/`, `receipts/`, `scripts/` or `computations/formalisation/` is edited.
