# `r7730` (60) — RESULT

**Answers order `r7727`.** `PREDICTION.md` was committed and pushed in its own commit before
`probe.py` existed. **124 arms, 81 distinct tags, 3 failing — and all three failures are findings
in what was read, not defects in the instrument.** Two instrument defects *were* reached and are
reported at `⑥` below, because they were reached and fixed before the arms they carry were trusted.

---

## ⌈ ① THE SHORT ANSWERS TO THE ORDER'S THREE QUESTIONS

**① Does *"…up to the factor `r`, positive on the forward branch `r > 0`. **There** the sign …"*
read correctly in context? — YES, and only just.** The appositive's antecedent **read by position**
is `the factor $r$`, which is the intended one and the **only** one on which the appositive is true:
the probe evaluated all three candidate antecedents and both rivals — the Gaussian curvature and
the comoving acceleration — are *false* on `r > 0`, each being true on only part of it. "There"
likewise resolves by position to `the forward branch $r>0$`, at 26 characters back against 745 and
763 for its rivals, and the second sentence **is** true for every `r > 0`. ⌗ *But on the correct
antecedent the appositive is a **tautology** — `r > 0` makes `r` positive — which is exactly why it
reads as informative about something else; and the two readings that would make it informative are
both refuted two clauses later by the paper's own "negatively curved while the expansion
decelerates".* ⇒ **Sound. One word would make it unambiguous rather than self-correcting:
`up to the factor $r$, which is positive on the forward branch $r>0$`.**

**② Is P8's *"Given the matter functional (`eq:Ttt`–`eq:Ttheta`), the theorem is machine-checked
…"* honest, row 1a not being built? — YES, and the honesty is load-bearing rather than cosmetic.**
`ok_Tt` and `ok_Tθ` are `noncomputable def`s whose bodies are the paper's two equations
**transcribed**; the Lean file's own header says so in as many words (*"`8πT^t_t` is read through
eq. `Ttt`"*), it claims rows 1b–1e and 2 BUILT and **never mentions row 1a**, and a named search for
an Einstein-tensor input over all nine statements returns **no hit**. So the conditional "Given"
states precisely the grant that is taken, and the paragraph's closing clause — *"The matter
functional itself, and the constancy of the index along paths of Fredholm operators, are cited and
not formalised"* — names it. ⇒ **`N7` is not reached: the order's premise is sound, and nothing is
owed here.**

**③ Does *"every component of `T` vanishes iff the ODE holds"* match `ok_vacuum_iff_ode`'s
hypotheses? — The interval matches exactly; the omitted smoothness hypothesis is NOT an
over-reach, and the finding runs the other way.** The binders are `(ha : 0 ≤ a)` with the
conclusion quantified over `Ioo a b`, so the statement's interval is an open interval inside
`(0, ∞)` — the prose's `(r₁,r₂) ⊂ (0,∞)` precisely, and slightly more general than `0 < a` would
be. The prose does **not** state twice differentiability and the statement carries two
differentiability binders. **But the second is mathematically redundant**: `ok_general_solution`
asks only `DifferentiableOn`, so a once-differentiable `f` solving the ODE *is* the SdS family on
that interval, and the probe verified by computation that both components vanish identically on
that family — worst **gradient-scaled** residual `3.020e-14` across `M ∈ {−2, −0.3, 0, 0.7, 5}`,
`Λ ∈ {−1, 0, 0.33, 3}`, `r ∈ {0.05, 0.4, 1, 2.7, 40}`. The forward direction uses only the radial
component and needs no second derivative at all. ⇒ **`N8` is not reached. The prose is right and
the formalisation is strictly weaker than it needs to be**; the owed repair is to the Lean
statement, not to P8, and it is routed rather than applied.

⚠ **One thing in that sentence IS read from a form rather than from a statement**, and it is my own
standing lesson: *"every component of `T_{μν}`"* is backed by **two** expressions in the
conclusion. The four-to-two reduction `8πT^t_t = 8πT^r_r` and `8πT^θ_θ = 8πT^φ_φ` is carried by the
two **docstrings** and by no declaration, and the off-diagonal components are not mentioned
anywhere in the file. **That is legitimate only because "Given the matter functional" grants it** —
so questions ② and ③ interlock: the conditional is what makes "every component" honest.

---

## ⌈ ② THE THREE FAILING ARMS — what they found

### ⚑ `A3` — *"with `M > 0`"* is sound under one reading of "undercritical" and FALSE under the other, and the paper gives both as equivalent

The region sentence now reads *"In the undercritical regime with `M>0` the pieces of the curve
between those three points are the three regions of the line element"*. `M > 0` does what I asked
of it: it excludes the de Sitter member whose missing black-hole interior `r7728` found. **But
"undercritical" is defined twice in P3 and the two definitions are not equivalent.**

- Read in the slicing parameter — *"It is positive for `|r₀|<2/√3` (three distinct real roots, the
  undercritical regime)"* — the interval is **strict in `r₀`**, and the designation
  `r₀ = 1/√3 = 0.577350269` lies **strictly inside it** (against `2/√3 = 1.154700538`) while
  carrying `2M = 0.384900179460`, which is **the Nariai mass** `2/(3√3) = 0.384900179460` exactly.
  Its roots, found with the tangency test rather than by sign change alone, are
  `[(−1.154700538, 1), (0.577350269, 2)]` — **a DOUBLE positive root.** So at that member the
  black-hole and cosmological horizons coincide, the "static region" arc the sentence names between
  them is degenerate, and the three-region reading fails.
- Read in the mass — *"The single threshold `|r₀|=2/√3`, **equivalently** `|2M|=2/(3√3)`, is the
  undercritical/overcritical boundary"* — that member is exactly **on** the boundary and is
  excluded, and the sentence is sound.

**The "equivalently" is what does the damage, and it is false as a statement about designations.**
The probe took the supremum of `2M = r₀ − r₀³` over the strictly undercritical `r₀`-interval and got
`0.384900179460` — the Nariai mass itself. So `|r₀| < 2/√3` gives `|2M| ≤ 2/(3√3)`, **not** `<`.

⌗ **And the paper already knows this.** Its own factorisation, read at source, is
`disc(r³ − r + 2M) = (4 − 3r₀²)(3r₀² − 1)²`, and it says of its own threshold *"and `4−3r₀²` sees
only two of them"* — the exact square `(3r₀² − 1)²` being precisely the `r₀ = ±1/√3` designation the
threshold misses. ⇒ **`N3` is reached.** The scope is still wrong on one designation of one member.
**The repair is one word, not a restructuring:** *"In the undercritical regime with `M>0`"* →
*"Where the three horizon roots are distinct and `M>0`"*, or equivalently *"`|2M| < 2/(3√3)`"*.
⌗ *That also removes the need for the reader to know which of the two inequivalent definitions is
meant — which is the defect `r7728` found in a different sentence and the same shape.*

### ⚑ `B1`/`B2` pass and `B3` fails: `71`'s citable-file rule is KEPT, and does not yet do what it is for

The rule as stated holds **completely**, measured by enumeration rather than spot checks:

| paper | cited names | occurrences | cited-but-not-declared | nearest named file wrong |
|---|---|---|---|---|
| P3 → `SlicingCurvature.lean` | `33` | `35` | **none** | **none** |
| P2 → `CircleConic.lean` | `8` | `8` | **none** | **none** |

⇒ **`N4` is NOT reached — there is no hole in the rule.** But the purpose is a different matter:

- **`25` of P3's `33` cited names are declared in more than one probe file**; `sl_ellipse`,
  `sl_factor`, `sl_locus` and `sl_nariai` in **four** each.
- **`8` of P2's `8`** are, and `cc_isGeodesicOn`, `cc_pullback` and `cc_unit_energy` in **ten**
  each — `CircleBackSeam`, `CircleChart`, `CircleConic`, `CircleExterior`, `CircleMaximal`,
  `CirclePatches`, `SlicingCubic`, `SlicingCurvature`, `SlicingHinge` and `SlicingSky`.
- The duplication `r7726` found, measured: `SlicingCurvature.lean` shares `1440` of its `1479`
  declarations with `SlicingSky` (`97.4`%), `1456` with `SlicingHinge` (`98.4`%), `1424` with
  `SlicingCubic` (`96.3`%) and `1393` with `CircleConic` (`94.2`%). **`1393` names are declared in
  all five.**

⇒ **`N5` is reached.** A citation naming the file it is declared in is satisfied by five files, so
the rule is kept and the citation is still not unambiguous. ⌗ **This is reported as a follow-through
on `r7726`'s ⓷ and not as a re-route**: the repair is the file-copying one already owed by `71`, and
naming it again is the point — the citable-file rule is **sound and insufficient until the copies
go**, and saying so is a finding rather than a quibble.

---

## ⌈ ③ `A1` — consequence three, checked for TRUTH and not for agreement with my draft

With the restriction in place, is the sign change once-and-only-once on `r > 0`? **Computed, and
yes — for `M > 0`.** `K_G` is monotone increasing in `r`, with exactly `1` sign change at
`r_HE = M^{1/3}` for each of `M = 1, 0.2, 0.037, 0.001` (roots `1.0`, `0.584804`, `0.333222`,
`0.1`), and `0` sign changes at `M = 0` and at `M = −0.3`.

⚠ *So consequence three's statement needs `M > 0`, which consequence three does not carry.* With
`M < 0`, `K_G` is positive at both ends (`+301.0000` at `r = 0.1`, `+1.0003` at `r = 10`) and
changes sign nowhere. **This is not a new repair owed**: `r7728` established that the forward-branch
restriction is what the consequence needed, and the mass sign is the region sentence's business,
where it has now landed. It is recorded because the arm was built to ask whether the landed sentence
is *true* and not whether it matches what I drafted, and the honest answer is "true on the members
the paper's own regime structure admits, and silent about the sign that makes it so."

---

## ⌈ ④ `C4` — the nine declarations, each read from its CONCLUSION and not from its name

All nine exist in `OperatorKernel.lean` and all nine conclude what their position in P8's sentence
implies; every conclusion is printed in `runs/READINGS.txt`, bounded by the `:= by` that begins its
proof and split at bracket depth zero. Three carry a gap between the statement and the words:

1. **`ok_L_bound` states a pointwise inequality, not an operator bound.** Its conclusion is
   `|ok_L f r| ≤ |f r| + r₂ * |deriv f r|` at **one** `r ∈ Icc r₁ r₂`, with `f` differentiable at
   that `r` alone. Its **docstring** says *"`L` is bounded from `C¹` to `C⁰`"* and the paper says
   *"the map `f ↦ (rf)′` is bounded from `C¹` to `C⁰`"*. The operator bound follows at once by
   taking the supremum, so nothing is false — but the step is the reader's, and the sentence it is
   read from is a docstring.
2. **`ok_index_one`'s conclusion contains no "index".** The integer `1` is assembled by the reader
   from four conjuncts — `1/r` is in the kernel, is non-zero, every kernel element is `c·(1/r)`,
   and `L` is onto the continuous functions. That is a one-dimensional kernel over a vanishing
   cokernel and the reading is right; the word appears only in the docstring.
3. **The intervals are mixed and the paper says they are not.** `ok_kernel` is stated on the
   **open** `Ioo r₁ r₂`, and `ok_index_one` puts its kernel clauses on `Ioo r₁ r₂` and its
   surjectivity clause on `Icc r₁ r₂` — while P8 says all four claims hold *"on `[r₁,r₂]`"*. The
   kernel statement on a closed interval is not what is proved.

⌗ `11` `#print axioms` lines stand at the foot of the file, so each declaration names its own axiom
basis rather than being taken on trust.

---

## ⌈ ⑤ PART TWO — my own stray, verified before it was acted on, then corrected

**The order's claim is right, and `N9` is not reached.** Measured in this order:

- **The instrument.** `receipts/P03_SdS_slicing/P03_which_mass_sets_the_hubble_eddington_radius.py`
  carries `f_b = 0.157  # cosmic baryon fraction` — **the same phrase the prose uses** — located by
  text.
- **The arithmetic decides.** `f_b = 0.157` gives `f_b^(−1/3) = 1.8537` and `1/f_b = 6.3694`;
  `0.1834` gives `1.7601` and `5.4526`; `0.18` gives `1.7711` and `5.5556`. The file's printed
  figures are `1.854` and `6.37`, matching `0.157` to `3.3e−04` and `5.7e−04` and **not** matching
  `0.1834`. `run.txt` prints all three, so this was read rather than inferred.
- **Where the wrong figure came from.** `sample.py` carries
  `F_B_PAPER = 0.1834  # the baryon fraction THAT paper assumes` — **attributed to the cited paper
  and not to the cosmos** — and it is referenced **once** in the whole file, at its own definition:
  no arm, no assertion and no printed line reads it. **It is dead, and the prose gave its figure the
  cosmos's name.**
- **The file contradicted itself.** `§②` already says *"against the cosmic `0.157`"*. The `~18`
  stood at exactly one place, `RESULT.md:88`, found on a named search over every file in the
  revision; the derived figures `1.85` and `6.4` elsewhere in the file were already right.

⇒ **Corrected to `16` per cent, which is what `0.157` rounds to, with the correction recorded beside
the line** rather than applied silently — this file's own convention at its `②`, where a wrong first
reading is printed beside its correction. The derived figures still follow, because the number the
instrument uses did not change.

⌗ **What is NOT done, and why.** `F_B_PAPER` is the dead constant that produced the error, and
removing it would be the complete repair — but `sample.py` is a measured receipt whose `run.txt` is
its witness, and deleting a line from it is a change to an instrument rather than to prose. **The
order says "correct the prose in your file", and that is what is done.** The dead constant is
routed in `FOR_66_FROM_60.md` with the one-line diff.

---

## ⌈ ⑥ MY OWN INSTRUMENT FAILED FIRST, TWICE, AND BOTH ARE THE SAME DEFECT FAMILY

**`N10` is reached, and this is the third revision running in which it is the same shape.**

1. **The binder reader could not see a binder group containing brackets.** `C3.twice` and
   `C3.gs_once` both failed on the first run, printing `['(deriv f)']` and `[]` where the binders
   are `(hf' : ∀ r ∈ Ioo a b, DifferentiableAt ℝ (deriv f) r)` and
   `(hf : DifferentiableOn ℝ f (Ioo a b))`. The flat regex matched the **inner** group and dropped
   the outer one. ⚠ *This is `r7724`'s `hypotheses_of` defect again — a bracket reader that a nested
   bracket defeats — and the fact that I fixed that one by bounding it at the depth-zero colon did
   not stop me writing a flat regex for the groups themselves.* Fixed by a depth walk, and the
   reader is now given this exact case as its negative before use.
2. **The twin search read its own correction record as a surviving twin.** `D2` and `D4` failed on
   the second run because the correction note at `⑤` **quotes** the `~18` it corrects. Fixed by
   `r7726`'s own lesson — a token search must say **where** its hits sit — so every hit is now
   classified into **the claim** and **the record**, by the record's own marker, located by text:
   `~18` now reads `0` in the claim and `2` in the record.

⌗ *Both were caught because every arm reports its witness and not only its verdict, which is what
`r7722` bought. Neither would have been caught by a verdict alone: the first printed a plausible
one-element list, and the second printed a true count of a thing that was not what the arm meant.*

---

## ⌈ ⑦ THE ARMS AGAINST `PREDICTION.md`

| arm | registered as | reached |
|---|---|---|
| `A1` | is consequence three TRUE with the restriction? | **yes, for `M>0`**; silent about the sign |
| `A2` | the order's first question, antecedents by position | **reads correctly**, uniquely and tautologously |
| `A3` | is `M>0` enough? does "undercritical" exclude Nariai? | **`N3`** — not under the `r₀` definition |
| `B1` | every `sl_` cited name declared in the cited file | **kept, `33`/`33`** |
| `B2` | every `cc_`/`ce_`/`cn_` cited name likewise | **kept, `8`/`8`** |
| `B3` | how many files declare each cited name | **`N5`** — `25`/`33` and `8`/`8` in several |
| `C1` | the sentence is there as quoted, with its disclaimer | **yes** |
| `C2` | the order's second question; Einstein tensor as input | **honest**; `N7` not reached |
| `C3` | the order's third question; hypotheses vs prose | **prose right, Lean weaker**; `N8` not reached |
| `C4` | each of the nine from its conclusion | **all nine hold**; three gaps between statement and words |
| `D1` | verify cc66's claim before acting | **verified**, arithmetic decides for `0.157` |
| `D2` | a named search for twins | **one target**, no twins in the claim |
| `D3` | `N9`: is the instrument the wrong one? | **`N9` NOT reached** — the prose was the error |
| `D4` | re-check after the correction | **holds** |
| `N10` | my instrument fails first | **reached twice**, `⑥` |

**Negatives reached: `N3`, `N5`, `N10` (twice). Negatives not reached and registered as reachable:
`N1`, `N2` (nearly — one word would help), `N4`, `N6`, `N7`, `N8`, `N9`.**

---

## ⌈ ⑧ WHAT THIS REVISION OWES OUTWARD

Three items, all routed in `FOR_66_FROM_60.md` with their diffs, none applied here:

1. **P3's region sentence** — *"In the undercritical regime with `M>0`"* → a scope that excludes the
   `r₀ = 1/√3` Nariai designation, and P3's own *"equivalently"* at the regime threshold, which is
   false of designations by the paper's own factorisation. (`71`'s and `69`'s.)
2. **`ok_vacuum_iff_ode`'s redundant `hf'`**, and the three statement-versus-words gaps in
   `ok_L_bound`, `ok_index_one` and `ok_kernel`'s interval. (`71`'s.)
3. **`F_B_PAPER`**, the dead constant in my own `sample.py` that produced the stray — a receipt's
   instrument, so routed rather than edited. (Mine, held back by the receipt rule.)

**Nothing is applied to the register, and nothing in another seat's files is touched. The one edit
this revision makes outside its own directory is the one the order asked for: the prose of my own
`r7484`.**
