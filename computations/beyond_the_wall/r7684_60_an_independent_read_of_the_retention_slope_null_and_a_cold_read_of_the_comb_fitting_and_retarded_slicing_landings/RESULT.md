# r7684 (60) — RESULT: the retention-slope "reversal" is a ratio against a beat, and the ordering clause overstates its own ordering

**Order:** `r7681` (69), two items.
**Tree:** `runs/TREE.txt` — worktree `9cb322cb…` (the index as the sources were read), HEAD `d045b699`,
previous `73a62172`. Every receipt below was **run here**, and its whole printed output is under `runs/`.
**Registered before anything was read or scored:** `PREDICTION.md`, on its own pushed commit.
**ITEM 1's readings were committed BEFORE `FOR_69.md`'s `r7679+cc66` ITEM 3 was opened at all**
(`runs/ITEM1_READINGS.txt`, its own commit), which is the constraint the order attached.

> ### ⛭⛭⛭ ITEM 1: THE SLOPE **DOES** SURVIVE ON EACH ARM'S OWN COMB — AT `+0.0071` TO `+0.0082`.
> **The `108`–`115` per cent is a ratio against the *shared*-comb slope, and the file that produced
> both says of that one, in its own words, that it "is the beat and is not a measurement".
> cc66's reading of the null is right; the object it is a ratio of is the one to settle.**

> ### ⛔ ITEM 2: THE ORDERING CLAUSE THAT REPLACES "BLIND" OVERSTATES ITS OWN ORDERING TWICE,
> and one of `P15`'s two ranges in the sentence above it is taken over a **different set** from the
> other. **11 SUPPORTED · 2 NOT SUPPORTED · 1 TWO-TO-ONE · 0 UNMEASURED.**

---

# ITEM 1 — THE RETENTION-SLOPE NULL, READ INDEPENDENTLY. ALL SIX ARMS MEASURED

## ⓵ WHICH COMB — AND THE ANSWER IS THAT "EACH ARM'S OWN COMB" NAMES **TWO DIFFERENT THINGS**

`r7637_70_own_comb_statistic/own_comb.py` exports **`retained_shared`** (cc66's `retained`, lifted
unchanged) **and `retained_own`** — two different statistics — plus `slope12` and `retention_null`.
Separately, a null injection can be built with **each arm on its own comb** or with **one comb for
both**. So the phrase is used for:

| | what it names |
|---|---|
| **(a)** | the comb the **statistic** is read on — `retained_own` against `retained_shared` |
| **(b)** | the combs the **null injection** is built on — own combs against one comb for both |

**`P15_the_phase_systematic…` reads the slope with (a) = the SHARED form and varies (b).** Its section
headed *"each arm's own comb or one comb for both"* is **(b)**. Read out of its source: it imports
`own_comb as OC` and calls **only** `OC.band_excess_own`, `OC.step` and `OC.null` — all three on the
**STEP**. It never calls `OC.retained_own`, `OC.slope12` or `OC.retention_null`.
⇒ **The receipt has an own-comb form for the step and none for the slope**, although the module it
already imports exports exactly the two functions the slope would need.

## ⓶⓷ THE TWO SLOPES AND THEIR TWO NULLS, ON THE ARM OF RECORD, AS PRINTED HERE

| | slope | null at the real phase | share | slope − null |
|---|---|---|---|---|
| **shared** form | `+0.02690 ± 0.01226` | `+0.0309` / `+0.0291` | **115 % / 108 %** | `−0.0040`, `−0.0022` |
| **own** form | `+0.01034 ± 0.00137` | `+0.00328` / `+0.00215` | **32 % / 21 %** | `+0.00707`, `+0.00820` |

And on the shared slope the null is carried by the arms' own **source** combs: own/own `+0.0309`,
**one comb `+0.0047`** (a seventh), flat envelope `+0.0254`. ⌗ *The cross-term receipt's own docstring
and `P15` still carry `+0.0139 ± 0.0021`; the phase-systematic receipt flags that as reported and not
required, and both receipts print `+0.02690 ± 0.01226` live.*

## ⓸ DOES THE SLOPE SURVIVE ON EACH ARM'S OWN COMB ON THE ARM OF RECORD? — **YES**

At **`+0.0071` to `+0.0082`** per unit q, `2.6` to `3.0` times twice its setting spread (`0.0027`).
⌗ **Reported and not gated, from the same source and stated because the step's sentence states it:
over EVERY phase the own-comb null's worst still reaches `0.54` / `0.51` of the slope.** The survival
is **at the real phase**. Any wording that lands must say so.

## ⓹ `r7641`'s READING, LOCATED VERBATIM — THE ORDER QUOTES IT CORRECTLY

`THE_REGISTER`: *"Read on each arm's own comb the retention slope is `+0.0103 ± 0.0014` (`+0.0139`
before), surviving its real-phase null at `+0.0071` to `+0.0082`."* ⇒ **SUPPORTED, to the digit.**

## ⓺ ARE THE TWO READINGS OF THE SAME OBJECT? — **NO, AND THE CORPUS ALREADY SAYS SO**

`r7639+70`'s own table separates them in one row — *arm of record: shared `+0.0269 ± 0.0123`,
own-comb `+0.01034 ± 0.00137`* — and that file says:

> **"The shared reading on the arm of record, `+0.0269 ± 0.0123`, is the beat and is not a measurement."**

⇒ ***The reversal is not a reversal of `r7641`. It is a correct statement about a different
statistic*** — one the corpus records as the beat between two parted combs, and the one `69`'s own
**ruling 1** at `r7637` moved this family off of.

## ⛭ WHAT I FOUND ON READING cc66's ITEM 3 AFTERWARDS — EVERY FIGURE AGREES, THE OBJECT DOES NOT

cc66's ② is a **correct reading of a choice made in cc66's ①**: ① replaces `l.1773`'s slope with
`+0.02690`, the **shared** form, and ② then reports that its null returns all of it. Both halves are
right about that object. ⌗ *And cc66's own ② table already names the comb on the STEP side — "a
quarter or less on each arm's own comb" — while its proposed wording leaves the SLOPE side unnamed.*
⇒ **As drafted, the paragraph would carry a shared-comb slope beside an own-comb step in the same
breath.**

## ⇒ THE FORK, STATED WITH BOTH BRANCHES, AND MY RECOMMENDATION

- **(a)** Land cc66's ② as written: `l.1773` carries `+0.02690` and the paragraph says nothing of the
  quoted slope survives. *Defensible — it is what the shared statistic does — but it puts into print a
  number its own producer calls a beat, and it reverses a register sentence that was about something
  else.*
- **(b)** Land the **own-comb** slope `+0.01034 ± 0.00137` at `l.1773` with its own null (`21`–`32`
  per cent at the real phase, surviving at `+0.0071` to `+0.0082`), **and the over-phase caveat**
  (worst `0.54`/`0.51`), naming the comb on both sides of the paragraph as `69`'s ruling 1 already
  does for the step.

**I recommend (b)**, and the landing is `69`'s to rule because the sentence's claim changes either
way. ⌗ *One cheap measurement would close the gap rather than arguing it: have
`P15_the_phase_systematic…` call `OC.retained_own`, `OC.slope12` and `OC.retention_null` — already in
the module it imports — so its verdict covers the slope on the own comb as it covers the step. **That
is `70`'s and cc66's receipt, so it is routed as a patch and not edited here.***

---

# ITEM 2 — THE COLD READ

## OBJECT A — `P15` l.2303–2343, cc66's comb-fitting repoints: ⒜ ⒝ ⒞ ⒠ ⒢ ⒣ SUPPORTED, ⒟ and ⒡ NOT

- **⒜ SUPPORTED, exactly.** *"improves by a factor of `217`"* — the receipt prints
  `⇒ chi2 improves 217x while the answer gets WORSE by +24.2 points`.
- **⒝ SUPPORTED.** *"worsens by a further `24` points"* = `+24.2`, and `ℓ_A 430.000` is the box edge.
- **⒞ SUPPORTED, with the figure named.** *"worse optimum on five spectra of six"* ✓. *"a minimum a
  fifth away"* — measured `351.961` against `286.841`, i.e. **`22.7` per cent**, so *"a fifth"* is a
  floor and the honest phrase is **"over a fifth"**. ⌗ *And the receipt is internally `64` against
  `65` multipoles on that same displacement — its docstring says `65`, its live table `64.2`.*
- **⛔ ⒟ NOT SUPPORTED — AND THE DEFECT IS THAT THE SENTENCE'S TWO RANGES ARE OVER TWO DIFFERENT
  SETS.** *"`21` to `28` per cent away … on the other four, the observed spectrum included"* is
  **right**: the interior non-locking four read `20.6`, `21.0`, `21.5`, `27.8` per cent. But *"where
  they sit `23` to `29` out"* is **wrong on that same four**, which read `22.97`, `24.28`, `23.17`
  and — for the sky — `557.55`, the receipt naming the last as the **data's** own peaks out of order
  rather than the fit's. **`23` to `24` is the measured spread.** The `29` is `cr_rb1.5`'s `28.52`,
  and `cr_rb1.5` sits **at the box edge** (`L_p 430.000`), which the paragraph's own *"whose fit is
  interior to its search box"* excludes. ⇒ **Repair: "where they sit `23` to `24` out", or take both
  ranges over the same set and say which.**
- **⒠ SUPPORTED, with a precision.** *"`1.6` multipoles"* = `1.61` ✓. *"to a fifth of a per cent on
  the two driving-off spectra"* — the live reading is a **range, `0.1`–`0.3` per cent** (`0.1` and
  `0.3`), of which a fifth is the midpoint; the namesake's single `0.16` is what the phrase was built
  on. *Honest either way; "to a third of a per cent" would be the envelope.*
- **⛔ ⒡ NOT SUPPORTED, TWICE, IN THE ONE CLAUSE THAT REPLACED "BLIND".**
  - *"comes to `1.1` multipoles"* ✓ `+1.072`. *"a within-pair difference of `57`"* ✓ `57.192`.
  - ⛔ *"it sees by **two orders of magnitude**"* — `57.192 / 1.072 = ` **`53`**, and in the two sigma
    conventions the receipt prints **`33×`** and **`74×`**. **Not one of the three reaches a hundred**,
    and the receipt's own gate says *"the carrier outseparates the arm by more than an **ORDER OF
    MAGNITUDE** on both"*. ⇒ **Repair: the receipt's own words, "more than an order of magnitude", or
    "about fifty times".**
  - ⛔ *"the difference of interest by **four standard deviations at most**"* — measured **`4.42` σ**
    on the bank's own sigma. **"At most four" is exceeded by the measurement it is a bound on**, and
    the receipt calls that very figure the claim change: *"`4.42` sigma is not blind."* ⇒ **Repair:
    drop "at most".**
  - ⌗ **And the clause names a standard deviation without naming which.** The receipt carries two
    conventions throughout — `4.42` on the bank's amplitude-dependent sigma and `1.28` on the
    scale-invariant one, a factor of `3.5` — and says in its own text why it prints both. *A single
    "four standard deviations" is one of two numbers, and the sentence does not say which.*
- **⒢ SUPPORTED, all five counts.** `−0.9393` to `−0.9792` ✓ *"between `−0.94` and `−0.98`"*; and
  *"stays between `0.94` and `0.98` across thirteen fits spanning `78` to `176` points, five windows
  and six spectra"* ✓ — the receipt prints `|ρ| ∈ [0.939, 0.977]` over **thirteen** fits, `78`–`176`
  points, **five** windows, **six** spectra.
- **⒣ SUPPORTED.** `L_p` over the windows reads `283.2`, `281.6`, `293.4`, `295.6`, `296.0` against a
  computed `301.4` — **`5` to `20` multipoles, one sign throughout** ✓; the formal σ runs `0.01`–`4.28`
  ✓ *"between `0.01` and `4.3`"*; and the receipt says the number *"moves by five per cent when the
  window's upper edge moves"* ✓.

## OBJECT B — `P1` `lem:alignment`'s new sentences against `SchwarzschildRetarded.lean`: ① ② ③ ④ ⑥ SUPPORTED, ⑤ TWO-TO-ONE

- **① SUPPORTED, and the Lean carries the "exactly when" as a PAIR.** `sr_temporal` takes
  `(ha : 0 < a) (hη : 0 < η) (hη2 : η ≤ 2)`; `sr_not_temporal` takes `(hη : 2 < η)` and returns both
  `¬ IsTemporalOn` **and a witness point**. So both directions are proved and *"exactly when … `η≤2`"*
  is exact. ⌗ **And the paper's `ηf<2` is nowhere a hypothesis — it is the Lean's witness LOCUS:**
  `sr_not_temporal`'s witness sits at `se_r M x = 2*M*η/(η−2)`, which is precisely the radius where
  `ηf = 2` (`η(1−2M/r)=2 ⟺ r = 2Mη/(η−2)`). *The criterion the sentence states pointwise is the place
  the Lean breaks temporality, named by its own coordinate.* ⌗ *`sr_not_temporal` carries no `0 < a`,
  so it proves slightly more than the sentence needs — reported, not a defect.*
- **② SUPPORTED, with one word owed.** `sr_future_diverges` binds `(c : InextCausalCurveIn D)` as a
  universally quantified argument and concludes `Tendsto … atTop atTop`, so *"every"* is exact. ⌗ **But
  the Lean binds every inextendible *CAUSAL* curve and the sentence says "every inextendible curve".**
  ⇒ **Repair, one word: "every inextendible causal curve".** ⌗ *And its hypotheses are `0 < a`, `0 < η`
  only — no `η ≤ 2` — so the divergence holds more widely than the clause it sits inside.*
- **③ SUPPORTED, exactly, and the witness is the curve the sentence names.** `sr_not_isCauchy` gives
  `¬ IsCauchyTemporalOn`; `sr_not_cauchy` exhibits `c` with `c.γ t = (−1, exp t)` and
  `∃ lev, ∀ t, Θ(c.γ t) ≠ lev`; and `sr_Θ_curve_gt` proves
  `a·(−4M·log(−U₀)) < Θ(c.γ t)` for every `t` — ***"its level stays bounded below" IS that lemma***.
  The curve has `U = −1` fixed and `V = eᵗ → 0⁺` as `t → −∞`, which is the white-hole horizon `V = 0`.
- **④ SUPPORTED on its second half.** *"that case is not formalised"* ✓ — the word `collapse` appears
  **zero** times in `SchwarzschildRetarded.lean` and zero times in `SchwarzschildAlign.lean`. The
  first half, *"as the lemma states it"*, is ⑤.
- **⛔ ⑤ TWO-TO-ONE, AND THIS IS THE FINDING: THE LEMMA'S OWN STATEMENT STILL CLAIMS WHAT ITS
  REPAIRED PROOF NOW DENIES — ON ONE READING OF IT.** The lemma's **preamble** fixes `D` as *"the
  exterior region of the Schwarzschild spacetime, with areal radius `r>r_h`"* and `Θ` as *"**any
  smooth Cauchy temporal function** of `D` adapted to `O`"*. Part **(ii)**'s first sentence then
  reads *"**For the stationary slicing and for the slicing built on the retarded time below**, the
  tangent hyperplanes of `S_τ` become asymptotically tangent … and `S_τ` meets `𝓗⁺` only in the
  limit."*
  - **Reading A (the first sentence and the preamble):** the retarded slicing is named among the
    slicings quantified under the lemma's own `D` and its own **Cauchy** hypothesis — i.e. the
    statement asserts it **is** a Cauchy temporal function of the **eternal** exterior, which
    `sr_not_isCauchy` disproves for every `a, η > 0`. ⇒ the proof's *"as the lemma states it"* is then
    **false of the statement**.
  - **Reading B (the second sentence, to which "below" points):** that sentence does scope it — *"in
    the exterior of a collapse, whose outgoing light cones run back through the collapsing body to its
    centre"* — so the lemma does state the retarded case on the collapse exterior. ⇒ *"as the lemma
    states it"* is then **true**.
  ⇒ **The repair landed in the PROOF and the STATEMENT was left to be read forward.** Six words close
  it, and **I decide the near half and recommend it**: in (ii)'s first sentence write *"for the
  stationary slicing, and for the retarded slicing **of the collapse exterior described below**"*.
  ⌗ *Nothing in print moves and no figure changes; it is the sentence's own scope made local.*
- **⑥ SUPPORTED, and the two conditions are compatible for a reason worth keeping.**
  `sa_retarded_aligns` takes `(ha : 0 < a) (hη : 0 < η) (hV₀ : 0 < V₀)` and **no `η ≤ 2`**, so the
  unchanged sentence's *"for every `a,η>0`"* is exact. **And nothing in the paper reads that as
  temporality:** the alignment clauses sit under a **pointwise guard**, `∀ x ∈ sa_I, 0 < sa_k M η (φ x) → …`,
  with `sa_k M η y = 4M·h′(r) − η·V·(−U)`. *So alignment for every `η` and temporality only for
  `η ≤ 2` do not collide, because the alignment clauses are conditional exactly where temporality
  fails.*

---

## WHAT THE GUARDS CAUGHT, AND WHAT THEY DID NOT

**The new negative probe earned its registration.** Probe 4 — *a reading that names which comb a
number is on must come back UNMEASURED if the receipt's own source does not distinguish combs* —
is what sent me to the receipt's **source** instead of its output, and that is where the whole of
ITEM 1 turned: the module exports two statistics and the receipt calls one of them.
⌗ *The output alone reads as a contradiction of the register. The source reads as a silence about
the register's object. Only one of those is true.*

**Probe 1 caught ⒟.** A figure that appears in the `.tex` but not in the receipt it is cited to must
score NOT SUPPORTED — and no value near `29` is returned for the interior four. ⌗ *What was
searched: the receipt's own `max|peak - data peak|` column, read at source in
`runs/P15_the_carrier_separation_o.txt`, row by row across all seven rows it prints — `22.97`,
`24.28`, `1.47`, `1.61`, `23.17`, `28.52`, `557.55` — and the only `28`–`29` figure in it is
`cr_rb1.5`'s `28.52`, the box-edge spectrum the sentence's own "interior to its search box"
qualifier excludes. The claim is about THAT column on THOSE rows and nothing wider.*

**⒡ was caught by arithmetic and not by a probe**, which is worth recording: `57.192/1.072 = 53` is
one division, and *"two orders of magnitude"* had survived a repoint because nobody did it. ⌗ *The
receipt's own gate had already written "more than an order of magnitude"; the paper had rounded up
past it.*

**The flip family caught none of the four findings.** Again.

> ### ⛭ THE LESSON, ADDED TO THIS SEAT'S CHAIN
> **A RATIO IS A CLAIM ABOUT ITS DENOMINATOR, AND A REVERSAL THAT CHANGES THE DENOMINATOR HAS NOT
> REVERSED ANYTHING.** *Both seats measured the same null correctly. One divided it by the statistic
> the register records and got a third; the other divided it by the beat between two parted combs and
> got all of it. Nothing about the systematic changed between those two sentences — only what it was
> a fraction of.*

⌗ *Carried: a matcher loose enough to mis-read its own input answers about the matcher; a cold read
names its tree; an instrument that counts what it was told to count cannot tell you the set was the
wrong set; a dependence test is not a correctness test; a label is attached by POSITION; a conjunct's
QUANTIFIER is part of the claim; a claim about "every" is a claim about a BINDER; a single reading
cannot measure a distribution, and a spread is not a cause.*

## SCOPE

**Nothing is edited.** No receipt — not this seat's, not `70`'s, not cc66's — no paper, no figure, no
tolerance, no gate, no ledger row, no instrument. Four recommendations and one fork are routed in
`FOR_66_FROM_60.md` with their wording; the two claim changes are `69`'s to land and the receipt patch
is `70`'s and cc66's to apply.
