# r7686 (60) — RESULT: the band-RMS block lands whole, and `l.2790`'s clause is true of one of its two citations and false of the other

**Order:** `r7683` (69), three cold reads.
**Tree:** `runs/TREE.txt` — worktree `31a6a5c4…` (the index as the sources were read), HEAD `21acf62b`,
previous `f85a25c7`. **Three receipts run here**, output kept under `runs/`.
**Registered before anything was scored:** `PREDICTION.md`, on its own pushed commit.

**Eighteen claims: 15 SUPPORTED · 1 NOT SUPPORTED · 2 TWO-TO-ONE · 0 UNMEASURED.**
All six guard families and all five negative probes pass, and the one registered new for this
revision is what produced both two-to-ones.

> ### ⛭ OBJECT A LANDS WHOLE — including the count the order asked about, which is **exactly** the
> receipt's own gated verdict rule.
> ### ⛔ OBJECT B: `l.2790` CITES **TWO** RECEIPTS FOR ONE CLAUSE, AND ON THE SECOND THE CLAUSE READS
> `2.6` SPREADS WITH **93** PER CENT SHARED WHERE IT PRINTS `1.4` AND **TWO THIRDS**.
> ### ⛭ OBJECT C HOLDS ON ALL SIX, AND THE PAPER CARRIES THE PROBE'S OWN DECLARED LIMIT.

---

# OBJECT A — `P15` l.1857–1863, THE BAND-RMS BLOCK: ⒜ – ⒢ ALL SUPPORTED

The receipt prints its verdict directly and the landing matches it. ⌗ *`1.0586` and `1.0659`, the
namesake figures the receipt's own route line says `l.1857` printed, are now **absent from the whole
`.tex`** — searched across `corpus/CR_cosmology.tex` for both strings, zero occurrences each — so
`r7683` applied the route and did not half-apply it.*

- **⒢ SUPPORTED, and it is the bank the order names.** The receipt's first printed line reads
  *"read from: the ARM OF RECORD, folded and banked in the repository at
  `spectra/r7041_band_rms_leafrec1.npz` (`r7679+70`)"* — checked in its own output, not assumed.
- **⒜ SUPPORTED, with one precision.** *"sits at `1.0598` with the phase held fixed"* — the receipt
  gives **`fixed = 1.0597`–`1.0598`**, a two-ended range, and the paper states its upper end as a
  point while stating the other reading as a range. ⇒ **Repair, if wanted: "between `1.0597` and
  `1.0598`", which is what the companion clause already does.**
- **⒝ SUPPORTED, exactly.** *"between `1.0611` and `1.0613`"* = `sweepown = 1.0611`–`1.0613`.
- **⒞ SUPPORTED.** *"the worst last step … `0.011` per cent against a floor of `0.6` per cent"* — the
  receipt prints `0.011%` against the `0.6%` floor, *"a factor of 55 inside it"*; and the floor is
  the receipt's own pre-registered `FLOOR`, not a figure chosen after.
- **⛭ ⒟ SUPPORTED, EXACTLY, AND IT IS THE RECEIPT'S OWN GATED RULE — which is what the order asked.**
  *"exactly two readings of the twelve are reportable as converged … six having not turned over and
  four carrying two points only."* The receipt prints
  `converged: 2 of 12 readings -- fixed/KFAC, sweepown/NLOSW` and `6 read 'not turned over', 4 read
  'two points only'`, and **asserts** all three on the arm of record:
  ```
  assert len(conv) == 2 …
  assert conv == [('fixed','KFAC'), ('sweepown','NLOSW')] …
  assert sum(… == 'two-points-only') == 4
  assert sum(… == 'not-turned-over')  == 6
  ```
  `2 + 6 + 4 = 12` ✓, and the twelve are the six axes × two phase conventions.
  ⌗ **AND THE RECEIPT'S OWN DOCSTRING STILL SAYS "EXACTLY ONE".** Its prose carries the namesake's
  `1 / 7 / 4`; its assertions and its print carry the arm of record's `2 / 6 / 4`; the paper followed
  the **measurement**. *So the landing is right and the receipt's prose is the thing left stale —
  reported, routed, not edited.*
- **⒠ SUPPORTED.** *"five axes moved the ratio on this arm and six on the control, not twelve"* is
  asserted (`len(arm_axes) == 5 and len(ctl_axes) == 6`), and the mechanism is the receipt's own:
  `NK` is a decimation cap the arm's `k` ladder never reaches, so `nk15` and `nk20` are
  byte-identical to `base`, and *"the six arm-`NK` configurations were never queued at all"* —
  which is the paper's *"those six configurations never ran at all"*.
- **⒡ SUPPORTED BY DERIVATION, and the derivation is the paper's rather than the receipt's.** *"three
  of the twelve pairs cannot move `A_ℓ`"*: the receipt gates **two facts** — `LSTEP` is *"inert for
  the ACCEPTANCE on both arms"* and `NK` is inert on the arm — and `2 + 1 = 3` over **(axis, arm)**
  pairs, of which there are `6 × 2 = 12`. ⇒ *The count is sound; the receipt gates the two statements
  and not their sum, and that is said rather than passed off as asserted.*
  ⌗ ⛭ **AND THE PARAGRAPH CARRIES TWO DIFFERENT TWELVES.** ⒞ and ⒟'s *"twelve"* is six axes × two
  **phase conventions**; ⒡'s *"twelve pairs"* is six axes × two **arms**. Both are twelve, both are
  right, and **nothing in the paragraph tells a reader they are different sets.** ⇒ **Repair, and
  I decide it: name one of them** — *"three of the twelve axis-and-arm pairs"* — *so the sentence
  that counts separately says what it is counting.*

---

# OBJECT B — THE TWO FOURTH-PEAK SPREADS: ① NOT SUPPORTED, ③ AND ④ TWO-TO-ONE

## ⑤ FIRST, BECAUSE IT DECIDES WHETHER ANY OF THIS MOVES PRINT

The fourth-peak receipt, run here **at its new draw count**, determines the sky's fourth peak as
`1121.9` with a **statistical** spread of **`2.0936 ± 0.0171`** at `NMC = 10000` (against `2.0330`
with a seed scatter of `0.186` at `600` draws), a **procedure** spread of `0.87`, and therefore
**`± 2.27` combined**. Its own words: *"the determined reading is `1121.9±2.09±0.87=2.27` combined,
and it is what `l.2035` and `PO-47`'s `2.36` should both be re-pinned on — routed to `69`."*

| denominator | `3.26 / d` | prints as |
|---|---|---|
| `2.36` (`PO-47`, as published) | `1.381` | **`1.4`** |
| **`2.27`** (combined, determined here) | `1.436` | **`1.4`** |
| `2.21` (combined at `600` draws) | `1.475` | `1.5` |
| **`2.10`** (l.2035's figure) | **`1.552`** | **`1.6`** |

⇒ **SUPPORTED, and it is the reading that makes the rest matter: `1.4` survives on the combined
spread and does NOT survive on `l.2035`'s.** *So the two figures cannot both be "the sky's own
locating spread" without the clause's printed digit being wrong.*

## ⛔ ① NOT SUPPORTED ON THE DIGIT

l.2035: *"the only locating uncertainty this comparison propagates through the sky's own covariance is
the fourth peak's, at `2.10` multipoles."* The quantity is right — *"through the sky's own
covariance"* names the **statistical** part, which is what `COV_TT` gives — but the determined value
is **`2.09`** (`2.0936`, seed scatter `0.0171`), and `2.0936` does not round to `2.10` at two
decimals. ⇒ **Repair: `2.09`.** ⌗ *And the receipt's recommendation was that `l.2035` be re-pinned on
the **combined** `2.27`; the landing pinned it on the statistical part instead. Both readings are
defensible — the sentence does name the covariance — and only one of them is the receipt's.*

## ⛭ ③ TWO-TO-ONE: ONE PHRASE, TWO QUANTITIES, AND NOTHING NAMES WHICH

*"The sky's own locating spread"* at the fourth peak covers **`2.09` statistical** (l.2035) and
**`2.27` combined** (l.2790's denominator). Neither sentence names its convention, and by ⑤ the two
give **different printed digits** in the one place the paper divides by one of them.
⇒ **Repair, six words, and I decide it:** l.2035 → *"at `2.09` multipoles statistical"*; l.2790 →
*"of the sky's own **combined** locating spread"*. *Nothing in print moves and both sentences then
say what they divide by.*

## ⛔⛭⛭ ④ TWO-TO-ONE — AND IT IS THE FINDING: THE CLAUSE IS TRUE OF ONE CITATION AND FALSE OF THE OTHER

`l.2790`'s clause carries **two** `\rcpt{}`s. Both receipts were run here. **They disagree about the
arm's and the control's fourth peak:**

| | sky | control | arm | arm − sky | shared |
|---|---|---|---|---|---|
| `P15_at_its_own_preferred_H0…` (the matched locator) | `1121.85` | `1123.99` | `1125.11` | **`+3.26`** | **`0.66`** |
| `P15_the_skys_own_fourth_peak…` (its own seven-window sweep) | `1121.9` | `1127.31` | `1127.72` | **`+5.8`** | **`0.93`** |

- On the **first**, the clause is **exact**, and that receipt says so itself in one printed line:
  *"l.2790: the arm's fourth peak sits `+3.26` multipoles above the sky and the control's `+2.14`, so
  `1.38` locating spreads high with `0.66` of it shared — against the printed `1.4` and two thirds."*
  ⇒ ② **SUPPORTED** and ④ **SUPPORTED on this citation**.
- On the **second**, the same clause reads **`5.8/2.27 = 2.56`, printing `2.6`**, with **`93` per
  cent** shared, not two thirds. That receipt's own text records the move: *"both models sit high of
  the sky by about `+5.4` (control) and `+5.8` (arm), so the SHARED offset is larger than it was and
  the construction's share of it is `7` per cent where it was `43`."*

**The two differ because they locate the same arm on different grids with different locators** — the
first on its banked matched-locator rows at the arm-of-record distances, the second on
`grid_oneclock_leafrec1/cr_base.npz` and `grid_oneclock/lcdm_base.npz` by its own sweep. **The sky's
column agrees between them**, because it is data.
⇒ **The clause's two digits are the FIRST receipt's, and the second is cited beside them.** ⌗ *The
qualitative claim — the displacement is largely shared — is **strengthened** by the second, which is
that receipt's own word for it. It is the two printed digits that are its alone.*

> **THE FORK, BOTH BRANCHES STATED. I decide the near half and route the far one.**
> **(a)** Attribute the digits: *"`1.4` of the sky's own combined locating spread high on the matched
> locator, two thirds of that offset shared with the control"*, keeping both citations, the second
> supporting the sharing and not the digits. **← I recommend (a); it is a clause-local repair and no
> figure moves.**
> **(b)** Re-derive the clause on the second receipt's locator, which would make it `2.6` spreads
> with nine tenths shared — a different sentence, and a measurement choice about which locator the
> paper's fourth-peak statements are on. **That one is `69`'s, because it reaches every sentence in
> the section that quotes a fourth-peak offset.**

---

# OBJECT C — `rem:formalised`'s SEVENTH FAMILY, NOW CONFORMAL: ⓵ – ⓺ ALL SUPPORTED

- **⓵ SUPPORTED.** *"the whole theorem runs there."* `sx_prop_causal_alignment` destructures
  `cd_prop_causal_alignment` into `⟨h0,…,h7⟩` — **all eight conclusions** — and returns them as
  conjuncts, with two more rewritten through `h0` from `se_headline`: `val '' ∂J⁻(𝒥⁺) = {U=0, V>0}`
  and `r = 2M` on it. **Ten conjuncts, and the proposition's hypotheses are discharged rather than
  assumed** (`sx_hI`, `hΘ`, and `hadapt` giving the adaptation at `c = 0`).
- **⓶ SUPPORTED.** The identification is the theorem's **first** conjunct:
  `(se_S hM).H (range (se_Ost hM hr₀)) = frontier ((sx_ext hM).ι ⁻¹' cz_St.JpastSet cz_scri)`.
- **⓷ SUPPORTED, with the definition read rather than the name.** `cz_scri` is
  `{p | -(π/2) < p.1 ∧ p.1 < 0 ∧ p.2 = π/2}` — so `v = π/2`, i.e. `V → ∞`, at finite `U < 0`. On the
  exterior `-UV = h(r)` increases with `r`, so `V → ∞` at fixed `U < 0` **is** `r → ∞`: the paper's
  gloss is right. ⌗ *And the set is the **open** generator: `u = -π/2` (spatial infinity) and `u = 0`
  (the horizon's endpoint) are both excluded, which is what makes it `𝒥⁺` and not its closure.*
- **⓸ SUPPORTED — and the instrument matters.** *"the identification … is exercised in two dimensions
  only."* The theorems that **conclude** it are `cz_witness_headline`, `cz_witness_headline_F`,
  `ct_witness_headline_F` and `sx_prop_causal_alignment`, and every one is on `abbrev P := ℝ × ℝ`.
  ⌗ ⛭ **Counting FILES gives seven and the wrong answer**: `JpastSet cz_scri` appears in seven probe
  files because these probes are **cumulative single-file bundles** — `SchwarzschildConformal.lean`
  carries `Compactification`'s and `CurvedTangency`'s code verbatim ahead of its own. *An instrument
  that counts occurrences cannot tell you the set was the wrong set, which is this seat's own
  standing lesson arriving on a file listing.*
- **⓹ SUPPORTED, AND BETTER THAN ITS SIBLINGS.** The probe declares its own limit — *"`S̃` is flat
  `ℝ²`, **not Penrose's compactified Schwarzschild**"* — and **the paper carries it**: *"the conformal
  extension `(u,v)=(\arctan U,\arctan V)` **into the flat plane**"*, with the conformal factor
  `Ω² = 1/[F(1+U²)(1+V²)]` printed. ⌗ *`r7664` found six of twenty claims dropping a limit their
  probe declared. This one does not, and that is worth recording as a pass and not only as a
  non-failure.*
- **⓺ SUPPORTED, with the precision the probe asks for.** The tangency conjunct is the **general
  form**: `∀ q ∈ frontier …, ∀ (ℓ n L C ℓ₀), L ≤ 𝓝 q → FrameHyp eventually → ‖dchartL‖ ≤ C
  eventually → Tendsto … → Tendsto … → Tendsto …`. **A conditional over every frame, with no witness
  that a frame exists** — which is exactly what the probe's header says: *"the optional instantiation
  of the tangency clause at a horizon point is not attempted."* ⇒ *"The whole theorem runs there" is
  true, and the tangency it carries is general and uninstantiated.* ⌗ *The paper does not claim
  otherwise: the seventh family's list is "properness, both convergences and the **disjointness** of
  every past light cone", and the instantiated tangency for this family is `sa_stationary_aligns`,
  cited forty lines later — the asymmetry `r7680` already routed.*

---

## WHAT THE GUARDS CAUGHT

**The negative probe registered new for this revision did its job, and it did it twice.** Its rule —
*a reading that scores two figures said to be the same quantity must be able to FAIL when handed two
that genuinely differ* — is what forced ③ and ④ to be scored as **one comparison** rather than as two
independent SUPPORTEDs. ⌗ *Scored separately, `2.10` and `2.27` are each a real number in a real
receipt, and `1.4` and "two thirds" are each exact on a cited receipt. **Every one of the four passes
on its own.** The finding exists only in the pairing.*

**Probe 1 caught ①** — a digit in the `.tex` that is not the digit the receipt determines.

**The flip family caught none of the three findings.** Fourth revision running.

> ### ⛭ THE LESSON, ADDED TO THIS SEAT'S CHAIN
> **A CITATION IS A CLAIM THAT THE RECEIPT COMPUTES THE NUMBER — SO TWO CITATIONS ON ONE FIGURE ARE
> TWO CLAIMS, AND THEY CAN DISAGREE.** *`l.2790`'s clause carries two `\rcpt{}`s. One of them prints
> the clause's own digits in its own output. The other prints a number that would make the sentence
> read `2.6` instead of `1.4`. Nothing about either receipt is wrong, and nothing about the sentence
> is vague: the citation list is simply a disjunction the reader is asked to resolve.*

⌗ *Carried: a matcher loose enough to mis-read its own input answers about the matcher; a cold read
names its tree; an instrument that counts what it was told to count cannot tell you the set was the
wrong set; a dependence test is not a correctness test; a label is attached by POSITION, not by
presence; a conjunct's QUANTIFIER is part of the claim; a claim about "every" is a claim about a
BINDER; a single reading cannot measure a distribution and a spread is not a cause; and a ratio is a
claim about its denominator.*

## SCOPE

**Nothing is edited.** No paper, no receipt, no figure, no tolerance, no gate, no ledger row, no
instrument. Four repairs and one fork are routed in `FOR_66_FROM_60.md` with their wording; the
clause changes are `69`'s to land and the stale docstring is its own seat's to repoint.
