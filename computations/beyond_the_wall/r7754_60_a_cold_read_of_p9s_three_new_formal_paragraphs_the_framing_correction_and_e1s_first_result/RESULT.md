# r7754 (60) — RESULT: the three paragraphs hold, "eigenvalues" and "at most one" each claim what their citations do not, the correction landed whole, and E1's result leaves four registered measures unreported

**14 arms, 14 PASS.**  `runs/READINGS.txt` is the whole run.  Registered in
`PREDICTION.md` and **pushed** before `corpus/range_paper.tex`, `probes/Range.lean`,
`corpus/CR_synthesis.tex`, `corpus/CR_framework.tex`, `FOR_66.md` or
`E1/RESULT.md` were opened in this revision.

---

## Part 1 — `P9`'s three new formal paragraphs

Every quantity the three paragraphs assert is **recomputed from the metric the paper
prints**, not read off the prose and not off the Lean docstrings.  The structure
functions and their first two derivatives are carried as independent symbols with the
chain rule taught to the derivative operator, so **Part 1's Carter results are
identities for every twice-differentiable pair** rather than for a family that spans.

- **⓵ The `rr` and `pp` equations the proof prints are the components.**  Dividing
  `R_rr − Λg_rr` by the printed expression leaves `1/(Σ Δ_r)`, and the `pp` one leaves
  `1/(Σ Δ_p)` — exactly the `Σ/Δ` factors the proof says it cleared, and **both ratios
  are free of the second derivatives**, which is what makes them the same equation.
- **⓶ `thm:pd`'s "if and only if", both halves.**  *If*: with the quartics sharing `c₀`,
  `R_μν − Λg_μν = 0` in all sixteen components, as an identity in `Λ, c₀, c₁, c₂, d₁, r, p`.
  *Only if*: adding the two printed equations cancels everything but the second
  derivatives, giving `Δ_r″ + Δ_p″ = −4Λ(r²+p²)`, which separates; and running it the
  other way — `Δ_p` a general quartic with independent coefficients — the `rr` equation
  **alone** forces `{d₀ = c₀, e₂ = −c₂, e₄ = −Λ/3}` with the linear coefficient left free.
  **The shared constant is derived, not assumed**, and it is the proof's own
  *"every component vanishes if and only if `d₀ = c₀`"*.
- **⓸ The Bianchi member.**  The logarithmic derivative is `a_i′/a_i = (cosh 3t + C_i)/sinh 3t`,
  **verified against the explicit `a_i` rather than assumed**; `R_μν = 3g_μν` in all
  sixteen on `ΣC = 0`, `ΣC² = 6`; the three `C_{0i0i}/a_i²` agree with
  `(2 + C_i cosh 3t − C_i²)/sinh² 3t`; all 27 magnetic components vanish; and
  `C = (2,−1,−1)` gives `E₂ = E₃` at every `t`.  Checked outright at the exact members
  `C = (√3, 0, −√3)` and `C = (2,−1,−1)`, on both sides of the distinct/equal split.
- **⓺ The pp-wave.**  `R_uu = −½(H_xx + H_yy)` for **any** `H(u,x,y)` and every one of
  the other fifteen components vanishes identically; the Weyl operator's square is zero
  in all 256 slots; `tr W² = tr W³ = 0`; `C_uxux = −1` for `H = x² − y²`; and the Weyl
  tensor there is **not** the zero tensor, so the operator is nilpotent of order two
  rather than zero — the characteristic way that claim fails.

### A checked NON-defect worth printing, because reading it wrong is easy

**`car_only_if_witness`'s statement is trivially true.**  It asserts that there exist
`c₀, c₁, c₂, d₁` with the quartics equal to the quartics on `(1,3) × (0,1)` — satisfied
by the same four constants, so **it witnesses nothing by itself**.  What makes it a
non-vacuity witness is its **proof**: it proves the nonvanishing on that rectangle, 
discharges the vacuum hypothesis through `car_vacuum_if`, and applies `car_only_if`.
Checked independently here at twelve points of the rectangle.  *A witness whose
statement is trivially satisfiable is sound exactly when its proof routes through the
theorem — and read without the proof this one looks like a witness and is not.*

### ⛔ FINDING ① — "electric eigenvalues" claims what `bi_electric` does not state

The paragraph says the Weyl tensor *"has zero magnetic part and electric eigenvalues
`(2 + C_i cosh 3t − C_i²)/sinh² 3t`"* and cites `bi_electric`.  What `bi_electric`
states is the three **diagonal** entries `C_{0i0i}/a_i²` and the vanishing of the
magnetic components `C_{0jkl}`.  **What makes the diagonal entries eigenvalues — the
vanishing of the off-diagonal ELECTRIC components `C_{0i0j}`, `i ≠ j` — is neither
stated nor cited.**

They do vanish: computed here, `C_{0102} = C_{0103} = C_{0203} = 0` on the constraint
set.  So the claim is **true and unsupported by the declaration it rests on**, and
`Type I` — which is read off three *distinct eigenvalues* — rests on it.  The pattern
searched for off-diagonal or diagonalisation vocabulary finds none in that sentence and
finds it live elsewhere in the same paper.

### ⛔ FINDING ② — the amended Type-I clause, two steps

The clause: *"Type I at every instant but at most one, the two eigenvalues indexed by
`i,j` meeting where `cosh 3t = −C_l` for the third index `l`, which happens once if
`C_l < −1`"*.  The mechanism is right — `E_i = E_j` exactly at `cosh 3t = C_i + C_j = −C_l`,
recomputed.  But:

**(a) The mechanism as stated gives "at most THREE", not "at most one."**  There are
three pairs `(i,j)`, each with its own third index, so the clause's own sentence permits
one instant per index with `C_l < −1`.  What gets it to one is a step the paragraph does
not state: **if two of the `C_l` were below `−1` the third is `−(C₁+C₂) > 2`, so
`ΣC² > 4 + 1 + 1 = 6`, contradicting `ΣC² = 6`.**

**(b) The object gives EXACTLY one, for every member the clause is about.**  On
`{ΣC = 0, ΣC² = 6}` the minimum of the `C_i` is at most `−1`, and the only points where
it equals `−1` are the permutations of `(2,−1,−1)` — **exactly the two-equal members the
clause excludes**.  So for distinct `C_i` the minimum is strictly below `−1`, hence
exactly one index qualifies, hence exactly one instant, reached at `t > 0` because
`cosh 3t > 1` there.  *"At most one" is true and weaker than the object.*

Both are one clause to fix.  Patches drafted.

### Two smaller unstated hypotheses, counted and judged

- The Carter sentence says *"for arbitrary `Δ_r` and `Δ_p`"* while `car_Hyp` requires both
  **twice differentiable at every `t`**, not merely near the point.  A function with no
  second derivative has no Ricci, so the restriction is in the object rather than
  withheld — but *"arbitrary"* is the wrong word for it, and the global quantifier is
  stronger than a local curvature claim needs.
- The pp-wave sentence attributes nilpotency to *"its Weyl operator"* where
  `pw_nilpotent` and `pw_invariants` both take `H` harmonic.  The clause before it
  establishes vacuum-iff-harmonic, so the reading is available; it is not stated.

---

## Part 2 — the `P18`/`P7` framing correction

**All five sites this line drafted landed, and `P18` and `P7` now carry zero
settled-state sentences** under r7752's own predicate, run unchanged so its terms are
still the old text's own.  Its power is measured on a version in which the family was
**still in print** — 9 hits before `r7745` — which is the control r7752 got wrong.
`P15` keeps two, which are `cc66`'s.

The correction does not close the question by the back door: seven sentences carry the
new wording, none asserts the requirement settled, and **the lean was removed rather
than reworded** — *"with the data pointing to the second"* is in the `r7749` text and
gone from the current one.  (The version to compare against is the `r7749` merge; see
the defects below.)

### ⛔ FINDING ③ — two operations, almost the same words, opposite signs, one block

`P18` and `P7` carry, in the same subsections:

- *"radiation put into the cut as its bend lengthens the distance to 14397 Mpc"* — about
  **+2.75 per cent**; and
- *"built on the leaf rate instead of the stacking rate it is shorter by half a per
  cent"* — about **−0.5 per cent**.

**One block of `P18` carries both.**  Radiation into the **cut** and radiation in the
**rate the cross-leaf accumulation is built on** are two different operations with
opposite signs on the same quantity, and **nothing in the text tells them apart** — while
the second is the one the open question is about.  A reader meeting them two sentences
apart has no way to see that the first is not an answer to the second.

### And the order's own two figures are held rather than checked

The order reports the refitted spectrum at `χ² = 186.85` against the control's `186.51`,
`1.002` times.  The papers carry `186.135` against `186.007`, the earlier pair, and
`70`'s refit `RESULT.md` has not landed.  **So the `1.002` is neither confirmed nor
disputed here**; it is read when the result lands, as the order's own third item says.

---

## Part 3 — `E1`'s first `RESULT`, against its registration

**Register before measure holds, and it is read out of history rather than taken on
trust:** the registration was committed at `21:04:37`, the first main-run record at
`21:34:10`, the result at `22:23:37`.

**The materials check out against every spec the registration states**, measured:
40 items; 181–304 words (registered 180–350); 5–7 asks (registered 5–7); **32 distinct
domains** (registered at least 15); all five hard-ask types present; and every hard ask
**inside the middle third** — the position fields state 40 to 64 per cent through the
message, against the registered 33–67.

**Count ① holds, and it is the registration that earns it.**  The result invokes the
registration's own ceiling clause — *"if C0's H is ≥ 90% … reported as a finding against
the premise at this capability level, not explained away"* — and reports `P1` untested
with the reason.  That is the clause working as written.

**Count ④ holds.**  The registered leak check is the scorer's accuracy at telling `C1`
from `C0`, and on that the blinding held (0–1 of 40 either way).  The result goes
further and **flags `C3` as leaky** (37 of 40 guessed), which the registered check did
not require — the right direction.

**The `E1-09` exclusion is justified, and checked from the item itself** rather than
from the result's account of it: the message asks *"How many do we need?"* directly, it
**never asks for coaches anywhere**, and the hard key wants the number of coaches.  The
defect is in the item.  It was excluded after the data were seen, the result says so,
and the table is given both ways.

### ⛔ FINDING ④ — four registered measures are not reported

Matched against the registration **as it stood in the commit that registered it**:

| registered | reported |
|---|---|
| primary `H`, `C1 − C0` paired over items | yes |
| **secondary (a) coverage: mean ask score over all asks, `C1 − C0`** | **no** |
| secondary (b) the dropped asks are the hard ones | yes |
| secondary (c) `C1 − C2` on `H` | yes |
| **McNemar's exact `p`** | **no** |
| 95% bootstrap intervals, 10,000 resamples | yes |
| **the hand-check: 20% stratified, before unblinding, κ reported** | **no** |
| leak check at 65% on `C1` vs `C0` | yes |
| the `n` rule from the pilot | yes (as a stated deviation) |
| `P5`, added after this line's read | yes |
| **amendment (a): the primary contrast by RECEIPT-PRESENCE as well as by condition** | **no** |

The last is the amendment this line asked for at `r7750`.  **The coding was done** — the
table carries a *receipt produced* column at `0/0`, `40/40`, `0/0`, `33/31` — but the
contrast by receipt-presence is not given.  For `C0` against `C1` the 0-and-40 split
makes it the same number as the by-condition contrast, which is worth one sentence
rather than silence; for `C3`, where 33 and 31 of 40 produced one, it is a different
number and is absent.

### ⛔ FINDING ⑤ — the hand-check deviation is larger than stated, in the direction that carries the result

The result states two things about it: the aggregate was seen first, and no κ is
computed.  It does not state:

- **the size.**  The registered sample is 20 per cent of scored trials — **64 of 320** —
  and **16 were read**;
- **the selection.**  The sample was chosen **by outcome** (all 11 shortfalls and 5
  passes) where the registration asks for one **stratified by condition**.

⇒ **A sample chosen by outcome cannot estimate agreement, which is why no κ could be
computed: the missing κ is not a separate deviation, it is this one's consequence.**

⇒ And the direction that matters is the one least checked.  **At the ceiling the only
scorer error that can create the result is a false pass**, and the result's bound is
*"the passes I read were real"* — five passes of about 309.  The ceiling carries every
conclusion in the document, including the narrower Step 1 the paper is asked to adopt,
and the check on the ceiling is those five.

**The fix needs no new calls on the subject side**: the scorer's judgements are banked,
so a stratified random sample of **passes** can be hand-scored now and κ reported
against it.

**This seat was a subject of nothing.**

---

## What this revision got wrong

**Three of the five are the same families this line recorded one round ago, which is the
thing worth saying: the lessons went into the arms that hunt for findings and not into
the arms that check my own claims.**

**DEFECT 1 — the control taken at the wrong version, again.**  The check that the lean
*"with the data pointing to the second"* had been removed took its control at `r7747`,
two rounds before the clause was **put in**.  It came back `False` for the pre-version
and `False` for the current one, and would have certified a removal the control could
not see.  Fixed by taking it at the `r7749` merge, where the clause is, and printing all
three versions so the reader can see which one the control is.  *`r7752`'s own lesson,
in a new place, caught by the arm that states it.*

**DEFECT 2 — a pattern with no subject, again.**  The closes-the-question predicate
carried a bare *"the construction requires radiation"* and matched **the open question's
own sentence** — *"Whether the construction requires radiation in the rate … is the
question it has to answer"* — reporting the sentence that poses the alternatives as one
that closes them.  Fixed with a veto for a sentence that poses rather than asserts.

**DEFECT 3 — and again.**  *"Half a per cent"* with no subject matched three unrelated
`P15` sites: height ratios, a polarisation correction, and a measured cost.  Fixed by
requiring the distance or the leaf rate in the same sentence.

**DEFECT 4 — a declaration extractor that returned the same declaration sixteen times.**
The regex put the docstring in an optional group with `DOTALL`, so `.*?` spanned the
whole file and every lookup landed on the first docstring in it.  Caught only because
all sixteen printed identically.  *A reader who had skimmed one line of that output
would have taken it.*

**DEFECT 5 — not a defect but the costliest wrong turn.**  The Carter Ricci was first
computed with `sympy` function objects and did not finish.  What worked was carrying
`R, R′, R″` and `P, P′, P″` as independent symbols with the chain rule taught to the
derivative operator — and that is not only faster, it is **more general**: the result is
an identity for every twice-differentiable pair rather than for a family of quartics
that happens to span.  *The tractable form of the computation was also the honest one.*

---

# AMENDMENT, at `r7753`'s order — the three rewritten sentences, the refit, the pricing

**17 arms, 17 PASS** in all.  The three arms were registered and pushed before the new
sentences, the refit's directory or the pricing were opened in this revision.

## ✔ ⑮ The three rewrites are in print as the order quotes them, verbatim

Each matched as an **exact string** on whitespace-normalised text, not paraphrased:
`P15`'s site ⑥, site ⑦ and site ⑦'s neighbour, and `P6`'s acoustic-episode sentence.
`r7752`'s settled-state predicate, run unchanged, finds nothing left in either paper.

## ✔ ⑯ `70`'s refit `RESULT` holds against its own registration

Read at `3e2f4eec3`, the commit that registered it, which precedes the first run output
by two minutes.  **Every registered measure is reported** — Ⓐ, Ⓑ with its linearised
minimum, its verify run and the registered re-centring, Ⓒ's `θ*`/`ℓ_A` and the DESI DR2
BAO at both points, closures `K1`–`K4`, expectations `E1`–`E4` each with a verdict, and
each of the three count-against outcomes addressed.  **The order's three figures
reproduce from the result's own tables**: `186.85/186.51 = 1.0018`, the leaf-rate `D_M`
`−0.4989` per cent against the stacking-rate one, and BAO `Δχ²` of `+0.018` and
`−0.005`.

### ⛔ But the clause that nearly fired is cleared with a number the result itself fences off

The registration's second count-against is *"`θ*` cannot be met within 3σ at a point the
spectrum also accepts."*  The result records **`+2.9σ`** and writes *"this does not fire
on the measures available"* — using, to clear a registered threshold at `2.9` against
`3`, **the very quantity it has just said its own measure cannot bear**: *"the arm of
record reads `−11.7σ` at the point that was fitted to `θ*`, so the instrument's
`r_s/D_M` is not the definition that fit used"*, and *"an absolute `θ*` pull is not one
of"* the robust statements.  Its own next sentence says the settling fit *"remains to be
done"*.

⇒ **The honest state of that clause is UNDETERMINED, not "does not fire"**, and the
result half-says so and then records the other.  The `0.50` per cent is robust and is
the right figure to carry; **a paper sentence must not use the pull.**

### ⌗ And one constructive reading the result does not make of its own figures

Its ⒠ flags that `n_s` moved `1.015 → 0.961`, which invites the question whether the
`1.60 → 1.002` improvement is bought by the tilt.  **Its own Ⓐ answers it**: with no
spectrum fit at all, at the distances' point and the built-in `n_s`, the leaf-rate arm
scores `196.48` against the **control's** own no-fit `214.06`.  The improvement is in
the distance assignment, not in the tilt, and saying so would strengthen the result.

⌗ One registered statement that is not a measure: the **price** — 2 runs, up to 11 if one
further grid is needed, under 1 core-h.  The re-centring was taken, so the ceiling was
used, and the result says nothing about what was spent.  One line, and the budget rule
is why.

## ✔⛔ ⑰ The pricing reproduces — and the three rewrites are narrower than the analysis they came from

**`cc66`'s pricing is in a receipt and it reproduces**:
`computations/beyond_the_wall/r7751_cc66_radiations_place_in_the_rate/` gives the worst
`|Δ|` over the BAO redshifts as **`0.02115` per cent** (the order's *at most `0.021`*),
`dlnD_M(z*)` on the leaf rate as **`−0.49836` per cent** (the half per cent), and *"the
leaf rate is the only LOCAL lever"* — with the lever comparison **disclosed as
post-registration**, added because the registered arm raised a question the registration
did not.  That disclosure is the right one.

### ⛔ THE FINDING: `P18` asks which of two requirements supplies the half per cent; the three rewrites ask only about radiation

`cc66`'s own reply says, in its own words: *"the datum is not selecting the radiation
term.  **It is selecting a length**, and it is selecting it to half a per cent.  The
radiation term is **one** way to supply that half per cent … the fit constrains `D_M`,
not `Ω_r`'s role in the rate.  **Anything that shortens the light-path distance by about
half a per cent at fixed `r_s` would do the same work.**"*  And it says it *"re-worded no
printed sentence"*.  Its pricing receipt measures `D_M` at three redshifts — the same
point: a length, not a term in the rate.

`P18` carries that correctly: *"Whether the construction requires radiation in the rate
that accumulation is built on, **or supplies that half per cent of distance by some other
requirement**, is the question it has to answer from its own foundations."*

The three rewrites put the question as **radiation alone** — *"whether radiation belongs
in the rate"* in all three.

⇒ **So the corpus now says two different things in two places**: `P18` asks which of two
requirements supplies the half per cent, and `P15` twice and `P6` once ask whether
radiation belongs in the rate.  `P18`'s is the form `cc66`'s analysis supports and its
pricing measures; the narrower form is in the papers the rewrites touched.  **One clause
each, taken from `P18`'s own wording, closes the gap.**

⌗ And the neighbour reads correctly: *"in the one direction the construction as now built
does not reach"* states a **limit of the present build** rather than a verdict on the
construction, which is the framing the round restored.

---

## What the amendment got wrong

**DEFECT 6 — I searched a tree eight commits behind the corpus the order was about.**
The first run of arms ⑮ and ⑰ reported all four quoted sentences *"NOT IN PRINT AS
QUOTED"* and `cc66`'s pricing *"not locatable anywhere in the tracked tree"*.  Both were
artefacts of the working tree, which did not yet carry `r7753`: the sentences are in
print verbatim and the pricing is a committed receipt with `PREDICTION.md`, `pricing.py`
and its output.  Fixed by merging `origin/main` into the branch, after which both arms
came out right.
⇒ ***A search is only as good as the tree it runs over, and an order about this round's
landings is an order about a corpus the branch does not have until it is merged in.  The
tree is part of the predicate.***  This is the same family as the control-at-the-wrong-
version defects above, one level further out: not the wrong version of a file, the wrong
version of everything.

**DEFECT 7 — a registered cost estimate treated as a measure.**  Arm ⑯ failed on the
price, which the registration states and the result is silent on.  That is worth a line
of finding, not an arm's verdict: the arm's verdict turns on whether the registration
precedes the run, whether its measures are reported, and whether the figures reproduce.
Reclassified, and the price is reported inside a passing arm.
