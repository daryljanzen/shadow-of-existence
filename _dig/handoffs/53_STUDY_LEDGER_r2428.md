---
name: study-ledger
kind: RECORD
current: reading, pre-commit
job: What a new node reading the corpus end to end has found worth changing, and what it has worked out. Nothing here is committed. Items are S-numbered in a private space and carry no register ID until they are routed.
sources: [chat]
---

# STUDY LEDGER — a reading of the programme, r2428 / c54.178

> **⌗ WHAT THIS IS.** *A new node was pointed at the repository and asked to learn the whole programme
> and to draft, as it goes, the things it would want to tell someone. This is that file.*
>
> ⛔ **NOTHING HERE IS COMMITTED AND NOTHING HERE CLAIMS A REGISTER ID.** *`S-` numbers are private to
> this reading. When an item is routed it takes an ID from the correct band per `THE_HUB`, and per that
> document's corrected rule — **allocate far from the other line's frontier, never merely above it**.*
>
> ⌗ **THE STANDING DISCIPLINE, inherited and kept:** *controls before conclusions; a check whose
> known-good case has not been verified is not a check; a receipt naming a defect is evidence it was
> **found**, never evidence it is still **there** — so **check the fix, not just the diagnosis** before
> listing anything.*

---

## ⛭⛭⛭ THE FIRST THING, AND IT IS NOT A DEFECT — IT IS A COLLISION OF RESULTS

**`S-001` · c54.178 reports ℓ₁ = 220. This node's independent arc reports ℓ₁ = 201.3. Both are on
"the same" CR arm and both carry discharged controls.**

*From `BUNDLE_r2376+c54.178.md`:*

| build | peaks | P1/P2 | P1/P3 | χ²/dof |
|---|---|---|---|---|
| c54.177 fluid + derived envelope | **220** / 524 / 804 / 1116 | 2.216 | 2.420 | 28.62 |
| c54.178 hierarchy, baryons sharing CDM density | **220** / 532 / 804 / 1124 | 2.115 | 1.969 | 15.14 |
| c54.178 hierarchy, no Π source | **220** / 532 / 812 / 1124 | 2.216 | 2.180 | **10.93** |

*From this node's arc (`ACOUSTIC_LIVE_ARC.md`, L-97…L-122, r2381 instrument):*

| | ℓ₁ | P1/P2 | P1/P3 |
|---|---|---|---|
| CR derived (ℋ = ℋ_stack, Ω against ρ_stack) | **201.3** | 3.514 | 2.436 |
| ΛCDM control | 221.1 | 2.159 | 2.163 |
| sky | 220.6 | 2.2170 | 2.2768 |

⇒ ***THIS IS THE MOST INFORMATIVE OBJECT IN THE REPOSITORY RIGHT NOW AND IT IS THE FIRST THING TO
UNDERSTAND.*** *Two lines, the same physics, a 9% disagreement on the observable both are aiming at.
Exactly one of the following is true and they are distinguishable:*

1. *the two builds are **not the same configuration** — different rate assignment, different seam,
   different normalisation — in which case the difference is a **statement about which assignment the
   sky prefers**, and that is a result rather than a bug;*
2. *one of the two instruments has a defect its own controls do not catch.*

⌗ **The discriminator is already in hand and costs nothing**: this node's ΛCDM control returns
ℓ₁ = 221.1 against the sky's 220.6 (0.2%), and its heights only to 3–5%. **If c54.178's ΛCDM control
has the same signature, the instruments agree where they should and the disagreement is (1).**

⚠ *Do not resolve this by adopting either number. **Read c54.177/178's build first**, find what it
assigns where this node assigned ℋ = ℋ_stack with Ω against ρ_stack, and only then compare.*

**STATUS: ⛭ DISSOLVED at `S-010`.** *The 220 in `BUNDLE_r2376+c54.178.md` is from the fluid/hierarchy
builds, **not** from `ACOUSTIC_two_arm.py`. That instrument's CR arm gives **ℓ₁ = 172, ℓ₁/l_A =
0.5703**, which I have now reproduced independently from a clean clone.* ⇒ **Both instruments find a
first-peak deficit and disagree about its SIZE — 23% against 8.7% — which is the same disagreement
`S-002` localises to one exponent.** *A sharper statement than the one this row opened with.*

---

## READING ORDER, and why

*The programme is 166 top-level documents, 35 `.tex`, ~340 registered receipts and a 4.1 MB append-only
changelog. Reading it "in order" is not defined; reading it in **dependency order** is.*

1. **The method documents first** — `THE_METHOD`, `THE_OPERATING_MANUAL`, `THE_HUB` *(done)*, because
   they say what counts as a claim here, and a reader who does not know that will mistake convention
   for error and file noise.
2. **`ONTOLOGY_FOUNDATION_INDEX` and `FOUNDATIONAL_DEPENDENCY_MAP`** — what rests on what.
3. **The papers in causal order** per `CORPUS_MAP`, not numerical order.
4. **`receipts/INDEX.md` and the receipts as I reach each paper** — a claim and its receipt read
   together, never apart.
5. **The open registers** — `PROTECTED_OPEN`, `OPEN_PROBLEMS_MAP`, `THE_OPEN_PROBLEMS_LEDGER`,
   `PROGRAMME_UNFINISHEDNESS_CATALOGUE` — last, so that what reads as a gap is checked against what
   the programme already knows is a gap.

---

## ITEMS

### ⛭⛭⛭ `S-002` · THE EXPONENT DISAGREEMENT IS −0.97 vs −0.62, NOT −2 vs −0.62 — **draft written, verified by running**

*Full note: `drafts/S-002_the_exponent_disagreement_is_narrower.md`.*

**Two corrections, one in each line.** `receipts/P15_CR_cosmology/P15_the_driving_shift_by_subtraction.py`
PART 4 says the acoustic fold *"reports Q₁k² constant — an exponent of −2 — which its mechanism
requires"*. **It quotes the fold accurately; the fold was wrong about itself.**

- ⛔ **The fold's arc mislabels its own quantity.** `Q₁·k²` spans a factor of **3.94**. The
  numbers 0.120–0.124 it quotes are `k²·Δη₁` — a different object, correct where it was computed,
  and carried onto the wrong label, then propagated into a shipped handoff.
- ⛔ **The mechanism never required −2.** Q is a *sound phase*, not a time: Δη₁ ∼ 1/k² ⟹
  Q₁ ∼ k·k⁻² = **k⁻¹**. And **k·Q₁ is constant to 15%** on the fold's own data — *the mechanism is
  confirmed by them, at the exponent it actually predicts.*
- ✔ **Both fold k-sets fit k^−0.968 ± 0.001**, against the receipt's k^−0.622.
- ✔ **The obvious explanation was tested and eliminated**: the receipt's own first recorded
  correction is that Q must be read on Θ₀, not Θ̂ = Θ₀+Ψ, and the fold reads Θ̂ throughout. **Refit on
  Θ₀ in the same process (control reproduces L-114 to 0.0004): −0.854, not −0.62.** The variable is
  not it.
- ⚠ **And the fold carries a defect the receipt does not:** the receipt *measures* its undriven
  calibration at 0.9968–1.0003; the fold never checked that its undriven reference returns Q = 1.
  **That is where to look next, and it is a live reason to prefer the receipt's number today.**

⛭⛭⛭ **SECOND ADDENDUM — THE DISAGREEMENT LARGELY DISSOLVES.** *Re-ran `ACOUSTIC_two_arm.py QSCAN=1`
on the current instrument after `S-011` flagged the receipt as pinned at c54.169.* **The pin holds —
still k^−0.63.** But the **c54.170 coupling split**, which post-dates the receipt this item corrects,
changes what the disagreement is:

| configuration | fitted exponent |
|---|---|
| undriven *(calibration)* | k^+0.00 |
| **continuity only** *(4Φ′ — the DECAY channel)* | **k^−0.18** |
| **Euler only** *(k²Ψ — the GRADIENT)* | **k^−1.04** |
| **driven** *(both)* | **k^−0.63** |

⇒ ***THE FOLD'S −0.968 SITS ON THE EULER COLUMN, NOT THE DRIVEN COLUMN.*** **Both numbers are right
and they were never the same object.** *The corpus is right about the mechanism — the fold blames
decay, and decay is the nearly-flat channel (−0.18); the receipt's "the k-dependence lives in the
potential's gradient, not in its decay" is exact.* **And the fold's number matches Euler-only to 7%:
it measured the gradient and attributed it to decay.**

⌗ *And it explains the reading-variable clue the first addendum could not use:* **Θ̂ = Θ₀+Ψ absorbs
the potential's value, which is what continuity feeds — so a Θ̂-read suppresses continuity and leaves
Euler standing.** *Named test: run `QSCAN=1` with Q on Θ̂ and see whether the driven column moves
from −0.63 toward −1.*

**STATUS: draft ready to route, REFRAMED — what survives as a correction to the fold is its
MECHANISM, not its exponent. The receipt's PART 4 narrative still needs the −2 clause removed.**

---

### ⚠ `S-003` · THE FOLD'S SHIPPED HANDOFF RE-INTRODUCES EXACTLY WHAT `PO-7`'s REWORDING REMOVED

*⛭ **DRAFTED** — `drafts/S-003_the_handoff_carried_the_figure_PO-7_had_just_retired.md`.*

`PROTECTED_OPEN` `PO-7` was **reworded at c54.165** because the old figure — *"ℓ₁ ≃ 140–150 against
the sky's 220"* — is **an artefact of one instrument's initial-data block**: across four readings of
the *same stated* initial condition ℓ₁ moves over {150, 165, 315}. The row now says, explicitly:

> ⚑ *"What is measured and stable is the **COMB**, not the peak … The figure to carry, if one must
> be carried, is **ℓ₁/l_A** and not ℓ₁."*

⛔ **The handoff shipped from the acoustic fold says "PO-7 is upgraded … to a firm 201.3 vs 220.6"
and carries raw ℓ₁ as its headline.** It was written against c54.108 and so could not have read the
c54.165 rewording — *but that is provenance, not defence*. Three things to check at source before
drafting:

1. **Is ℓ₁ = 201.3 stable across the fold's own initial-data variations?** *It is not.* The fold's
   own runs give 201.3 (flat Φ₀), 173.9 (envelope), 174.1 (radiation out of the constraint), and a
   buried peak (Poisson-slaved). **The fold reproduced PO-7's instability and then reported the flat
   datum's value as "an invariant of the construction"** — invariant across the *seam*, which is a
   different axis and does not license the word.
**THE THREE CHECKS, RUN.**

**① "Invariant" was established on the wrong axis, and the fold measured the other one.** ℓ₁ = 201.3
is invariant across the **seam** (four values, 201.3–201.8). *Across the initial data the fold's own
runs give **201.3 / 173.9 / 174.1 / peak buried below ℓ=453** — a spread comparable to the
{150, 165, 315} PO-7 cites.* ⇒ **The fold reproduced PO-7's instability and then called one datum's
value an invariant of the construction.**

**② The raw-ℓ₁ headline is the comparison PO-7 says cannot be made** — and the fold's own `L-107`
found the H₀/Ω_m asymmetry independently and wrote *"every cross-arm statement must be made in
l_A-normalised form"*. **The finding was in the arc and did not reach the summary.** *`THE_METHOD`
§3c exactly.*

**③ And the comb — what PO-7 says IS stable — is nowhere in the handoff's headline**, though `S-004`
shows it is where the fold's result actually lives.

⌗ **THE NEGATIVE-VERDICT BAR, run on my own closing sentence.** ⛔ **① SAME-OBJECT FAILS:** *PO-7's
object as reworded is **the comb**; the handoff's is **the peak**.* ✔ ② inversion written out ·
✔ ③ price both ways · ⚠ ④ several narrow negatives conjoined. ⇒ **A bounded negative in form that
reads as a closure in effect, and ① is why — the check the manual says catches most of them.**

⇒ **WHAT IT SHOULD HAVE LED WITH:** ℓ₁/l_A — fold **0.6675**, c54 arm **0.5703**, controls 0.7292 /
0.7300, **sky 0.7312** — and the comb: fold 0.79→0.95 of π/r_s, c54's registered band 0.72–0.79.
***Two lines, two instruments, both finding a deficit in the normalised figure and both finding a
comb short of π/r_s. Far stronger jointly than either raw ℓ₁, and it is the statement the rewording
asks for.***

**STATUS: drafted. The handoff is shipped and cannot be recalled — this note is what corrects it.**

---

### ⛭⛭⛭ `S-004` · PART 5's REGISTERED RESIDUAL IS PART 2/3's PHASE — **draft written, control passes**

*Full note: `drafts/S-004_the_comb_deficit_is_the_phase.md`. Figures machine-printed by
`drafts/S004_comb_deficit_test.py`.*

`P15_the_first_peak_figure_is_not_stable.py` PART 5 registers, unresolved: *"under EVERY initial
condition the source comb comes out at 0.72–0.79 of π/r_s … registered, not resolved. **This is what
front #5 turns out to be about.**"* And `P15_the_driving_shift_by_subtraction.py` PART 3 measures
CR's acoustic phase varying 3.9× over the same band.

⇒ **They are the same measurement.** A comb extremum at fixed η_rec is a mode's *m*-th temporal
turnover landing at recombination, so the comb is the root set of **k·r_s/π = Q₁(k) + m**, and

$$\text{spacing} = 1 + [Q_1(k_{m+1}) - Q_1(k_m)] < 1 \iff Q_1 \text{ falls with } k.$$

- ✔ **CONTROL: on ΛCDM's flat Q₁ the relation returns spacing = 0.9947.** *It must return 1 and it does.*
- ⛭ **The receipt's OWN Q₁ column predicts a first comb spacing of 0.7706 against its own registered
  band of 0.72–0.79.**
- ✔ **Within the fold's instrument, where both objects were measured on the same runs: predicted
  0.810 / 0.898 / 0.939 / 0.960 / 0.972 against measured 0.802 / 0.912 / 0.921 / 0.948 / 0.949** —
  ≤ 0.02 across a spacing that rises from 0.80 to 0.95. *It reproduces the run with m, not just a
  deficit.*
- ⚠ **m = 0 is extrapolated below the measured k band in both cases** — so the band-hit is suggestive
  and **the m ≥ 1 agreement is the evidence.**

**Why it matters beyond the residual:** PART 5 reads the deficit as *"a disagreement with the
acoustic scale — the corpus's own settled result"*. It is not; the same instrument returns π/r_s
exactly on ΛCDM. **The deficit is the phase, projected** — which is why no initial condition moves
it, while the first peak moves 165 multipoles. *Initial data set where the comb starts; the phase's
k-dependence sets how it is spaced.*

**And it sharpens `S-002` rather than dissolving it:** the deficit's *size* is fixed by the exponent,
so **−0.97 and −0.62 predict different comb deficits, and the comb is the stable observable.** A
sharper discriminator than either instrument had alone.

**STATUS: draft ready to route. Named unrun question: measure Q₁ and the comb in `ACOUSTIC_two_arm`
itself — it already computes the first and can be asked for the second, which removes the
cross-instrument step entirely.**

---

### ⛭⛭⛭ `S-005` · P15 l.184 ASSIGNS r_s TO THE RATE ITS OWN PARAGRAPH CALLS FATAL — **routes to `FOR_54`**

*Full note: `drafts/S-005_P15_line184_contradicts_itself.md`. All sites read whole at source in
`corpus/CR_cosmology.tex`.*

- **l.184:** *"a process running in the content—r_s, r_D, recombination, the perturbations—**takes the
  leaf's**."*
- **l.184, two sentences later:** *"the radiation-sourced L2 rate carried past the branch point
  **radiation-pins r_s** and re-manufactures the very tension this section dissolves."*
- **l.188:** *"an **L1 quantity** whose baryon-loaded c_s is ordinary content microphysics but whose
  **expansion H is the L1 rate**."*
- **l.324:** *"r_D—**like r_s**—is an L1 quantity … its expansion the L1 rate, ***not** a
  radiation-included one*."*

⇒ **The list is right and the predicate is wrong.** The distinction is between *where the microphysics
lives* (the content) and *which expansion it competes against* (L1); l.188/l.324 and
`ONTOLOGY_FOUNDATION_INDEX` §1·LEVELS draw it correctly, l.184 collapses it. **A correction is
proposed built entirely from those three sources' own words.**

⚠ **Load-bearing, and it has already cost.** l.184 is the corpus's one-line form of the decision rule
— the sentence a node goes to. For *the perturbations* it fixes the ℋ in Φ′ = −ℋΨ − k²Φ/3ℋ, i.e. the
whole driving term. **The acoustic fold hit exactly this, filed it as "P15 contradicts itself", and
spent an arc re-deriving from the equations what l.188/l.324/§1·LEVELS already state.**

⌗ *`THE_METHOD` §3c one level in: not a headline lagging a body, but a **summary sentence carrying the
negation of the two bodies that state the thing**.*

⛭⛭⛭ **AND THE CORPUS HAS ALREADY NAMED THIS EXACT SENTENCE AS ITS OWN FAILURE MODE.** *Found after
the draft was written.* `ONTOLOGY_FOUNDATION_INDEX` §1·SHADOW: *"**The old two-way form of this
discipline** … **is the very conflation that seeded the collapse**: it fuses L1 with L3, and **it
wrongly casts recombination-era plasma processes as 'local dynamics' (they are content riding the
foliation → L1, radiation-free)**."* ⇒ **P15 l.184's list does precisely that — it names
*recombination* and puts it on the leaf's rate.** *So the defect is not an internal inconsistency but
the corpus's own named error, surviving verbatim inside the paper's one-line statement of the rule
built to prevent it.* ⌗ *And `THE_METHOD` §4b explains why no local check sees it: the paragraph is
internally about L1/L2/L3, the sentence is a compression in the older idiom, and nothing at any joint
is malformed — locally right everywhere.*

**STATUS: draft ready to route to `FOR_54`. Nothing in `PROTECTED_OPEN` moves; no physics changes.**

---

### ⌗ `S-006` **CANDIDATE, NOT A FINDING** · "BRANCH POINT" MAY NAME TWO LOCI IN ADJACENT BULLETS OF §1c

*Recorded as a claim to dig, per grain 0's rule that **an advertised door is a CLAIM TO DIG, never a
fact** — and per `THE_METHOD`: before writing that anything is ambiguous, abstract-dig both papers and
re-read the sentence I am about to contradict. **I have not done that yet.***

**What I have read.** `ONTOLOGY_FOUNDATION_INDEX` §1c, two adjacent bullets:

- **l.1057:** *"The cosmogenesis branch point is a **metric** singularity (**finite curvature**), **not
  the r=0 manifold singularity**."*
- **l.1058:** *"beginning at the branch point at **r=0** (well-posed because r_* CONVERGES, **not**
  because curvature is finite — **it diverges there**; r2234)."*

And §0's own `BRANCH` row fixes sense ①: *"the analytic **BRANCH POINT — r=0**, where the slicing
closes … 'a branch point, not a barrier'."* §1f agrees throughout — *"through the branch point r=0,
which is passable"*, the manifold C^∞ there, the divergence *"a perspectival areal-coordinate
artefact."*

**Two things that may or may not be one thing:**

1. **The locus.** l.1057 places the cosmogenesis branch point away from r=0 (a metric singularity, and
   P1's metric singularity *is the event horizon*, i.e. the seam); l.1058 and §0 and §1f place *the*
   branch point at r=0. §1k lists **throat X=α, back-of-lap r=0, merged horizon α/√3** as *distinct*
   stations of one curve — so these are not interchangeable.
2. **The curvature.** l.1057 says finite; l.1058 says it diverges there and carries an `r2234`
   correction marker, so it is the later statement.

⚠ **Both could be innocent.** l.1057's *"not the r=0 manifold singularity"* may be denying that r=0 is
a manifold singularity at all — which §1f affirms — rather than placing the branch point elsewhere.
And "finite curvature" vs "diverges" may be the invariant vs the areal-coordinate *reading*, which
§1f explicitly distinguishes. **If so there is no defect, only a compression that reads badly beside
its neighbour.**

⛭ **RESOLVED — dug at source, and it turned into `S-007`.** *P3 §sec:lap names the two stations
separately and in the order the curve meets them: "inward along a ruling **to the equatorial seam**;
continue … around the throat **through r=0** … **The point r=0 on this lap is the branch point**."
§0's `BRANCH` row fixes ① at r=0; P15 l.936 says "the crossing at r=0 and the seam are distinct loci
on the lap"; P16's branch point is where ρ_r/ρ_m ∝ 1/a diverges, i.e. a→0.* **The canon and the
papers are consistent. l.1057's "finite curvature" is the horizon seam's property, not the branch
point's — which is the conflation, and it has two siblings. See `S-007`.**

⌗ *Kept here rather than deleted: the original unrun question was —* *in `P16 cosmogenesis_paper`
§lap and `P7 CR_framework` §sds-cosmology, at source — **which station does "the cosmogenesis branch
point" denote, and what is the invariant curvature there?*** Until that is read, nothing is claimed
and nothing is routed.


---

### ⛭⛭⛭ `S-007` · THE r2123 CONVENTION HAS THREE RESIDUAL SITES IN THE LENS — **draft written, dug at source**

*Full note: `drafts/S-007_the_r2123_convention_has_residual_sites_in_the_lens.md`.*

`ONTOLOGY_FOUNDATION_INDEX` l.505 withdraws the equation **seam = branch point** and records the
r2123 sweep as having **corrected 99 sites**; l.1140 states the correct picture and calls the
conflation *"the fault"*. **Three sites in the same file still carry it:**

| line | text | equates |
|---|---|---|
| **885** *(§1·LEVELS, P3 bullet)* | *"…outward is sinh^{2/3} cosmology (L1), **the seam its branch point**"* | seam = branch point |
| **1030** *(§1b **link 3** of the cosmological forcing chain)* | *"one analytic curve, **the seam its branch point**"* | seam = branch point |
| **1057** *(§1c)* | *"The cosmogenesis **branch point** is a metric singularity (**finite curvature**)"* | branch point = the finite-curvature seam |

✔ **Sources dug, and they agree with the convention:** P3 §sec:lap names the two stations separately
and in order; §0's `BRANCH` row fixes ① at r=0; **P15 l.936 says outright "the crossing at r=0 and the
seam are distinct loci on the lap"**; P16's branch point is a→0.

⚠ **It matters more in the lens than it would in a paper** — this is the document
`THE_OPERATING_MANUAL` §2 says to hold up to any paper, whose *"guard is the card's real content."*
**And l.1030 is a numbered link of §1b**, at the step where the collapse-to-cosmology crossing is
stated. *The two levels it fuses are the ones l.1140 says must not fuse: geometric closure through
r=0, physical seeding at the finite-curvature horizon seam that "never reaches r=0".*

⌗ **An instrument that failed, recorded:** a crude scan found 268 of 301 uses of *"the seam"* carrying
no qualifier within 40 characters. **That number is worthless** — it cannot see a qualifier set
earlier in the sentence or by a section's subject, and the r1012 note says cosmology-paper *"the
seam"* (Nariai) was *left canonical* on purpose. ***The scan located; it did not find.*** The three
sites are findings because each was read at source and each carries the withdrawn **equation**, not
merely a bare noun.

**STATUS: draft ready to route. Lens-owned, so it is this line's to fix rather than `FOR_54`'s —
but the fix is three appositions and the file already contains its own correct statement at l.1140.**

---

### ⛭⛭ `S-008` **CANDIDATE COROLLARY** · THE DIAL'S COUNT IS THE MASS PARITY — **drafted, control passes, prior-art check owed**

*Full note: `drafts/S-008_the_dial_count_reads_the_mass_parity.md`. Figures from
`drafts/S008_dial_count.py`.*

`THE_METHOD` §3b's positive face — an unnoted corollary, drawn only from P3's own displayed
relations.

| | 2M(w) | simple zeros | touch-zeros | crests + | crests − | **marks** |
|---|---|---|---|---|---|---|
| **D=4** *(§sec:tour)* | (2/3√3) sin 3w | 6 | 0 | 3 | 3 | **12** |
| **D=5** *(§rem:dimension)* | ⅛(1 − cos 4w) | 0 | 4 | 4 | **0** | **8** |

✔ **CONTROL: D=4 reproduces §sec:tour exactly** — twelve marks at 30°, zeros at 0/60/…/300, crests at
30/90/…/330, three of each sign.

⇒ **The four marks that vanish at D=5 are the antifundamental.** 2M = ⅛(1−cos 4w) ≥ 0 identically, so
R : 2M ↦ −2M has no negative crest to exchange with. General form: **4(D−1) marks at even D, 2(D−1) at
odd D** — because parity of D fixes parity of 2M in the offset, which fixes sine-vs-cosine.

**Duck gate applied: forced, not permitted.** And it passes `GEOMETRY_PHYSICS_TAXONOMY` — a mechanism
that forces the count *and* a further consequence the corpus holds independently (the hexad's 3̄, and
γ⁵, exist only at even D). ⇒ *Not a new result — an existing one wearing a face the corpus has not put
on it, which is the form §prop:twoalpha itself values.*

⛔⛔ **WITHDRAWN — RESTRAINT. P14 §sec:scope was read and it has this, and three levels deeper.**
Its sentence: *"with no sign change there is no antifundamental, hence no hexad, hence **none of the
twelve designations the four-dimensional dial carries**."* And beyond it: **① the constant** — *"at D=4
a pure multiple angle of zero mean, at D=5 one harmonic **plus a constant** … the constant is not
nothing: it holds 2M ≥ 0, and the sign change is the entire content of the mass reflection"*;
**② the root set** — *−r₀ is a root exactly at odd D, so at D=5 the cofactor degenerates to a line and
a circle,* ***"the geometry is its own image, and that is why five is vector-like"***; **③ the
monodromy** — *even in r at odd D, confining the D=5 deck group to the centraliser of (0 1)(2 3) in
S₄, order 8 against 24.* ⇒ **My count was a fourth face of a fact the corpus already holds better.**
*`THE_METHOD`: if the corpus has it, the finding is at most where it is not loud enough.*
⌗ **The one residual, graded low:** *P3 owns the dial and hands its dimensional behaviour to P14 —
a §3c "not loud enough" item, not a defect.*

*(superseded, kept as the record: OWED BEFORE ROUTING — read P14 §sec:scope.* `rem:dimension` said the separation *"is settled there"*. **It is.)**

⌗ **The counter got it wrong three times** — threshold zero-finding (2 zeros), grid alignment (11
marks), and a linear scan of a circular dial (11 again). **The same control caught all three, none
was a physics error, and none would have been visible without it.**

---

### ⛭⛭⛭ `S-009` **POSITIVE** · THE HEAVY TIER IS VERIFIABLE HERE — **288/288 PASS, run in place**

*Full note: `drafts/S-009_the_heavy_tier_is_verifiable_here.md`. Raw output:
`drafts/S009_run_all_receipts_288pass.log`.*

`THE_HUB` §CI: *"⚠ **The heavy tier is where this container cannot verify**: ten receipts import
camb/pynucastro … **In CI they can actually run**."* And `receipts/RUN_RESULT.txt` records
**264 pass, 8 fail, 4 over timeout** — every failure an ImportError before a line of computation.

⇒ **It is not an environmental limit. It is `pip install camb pynucastro --break-system-packages`,**
both resolving first time (camb 2.0.1, pynucastro 2.12.0, on python 3.11.15 / numpy 2.4.4 /
scipy 1.17.1 / sympy 1.14.0). Then:

> **`288 pass, 0 fail, 0 over timeout, in 304s wall`** *(`--jobs 2 --timeout 240`)*

- **The eight ImportErrors are gone** — the ~9% damping result, the CAMB reference, the BBN
  validation and the likelihood are **evaluated for the first time in this gate's recorded history**.
- **The four timeouts are gone without loosening anything**: the previously-`[slow]` collapse-leg
  receipt finishes in **41s**, inside the old 120s bar. *The old run used `--jobs 4` on a 2-core box —
  the contention was the timeout.* **304s against 543s, and greener.**
- **The register grew 276 → 288**; all twelve new ones pass.

**TO CHANGE:** ① refresh `receipts/RUN_RESULT.txt`, which closes with *"a registered receipt that does
not run where it is registered is not a receipt"* sitting on a result saying eight of them do not;
② `THE_HUB`'s CI row should name two dependencies rather than an environmental limit — the difference
between *"wait for CI"* and *"run it now"*, at five minutes; ③ re-ask whether the gate belongs in the
standing set, since *"it costs wall clock the others do not"* is now weak.

⌗ **AND THE FLOOR IS NOT A VERDICT.** *288 exit-zeros means every assertion was **evaluated**, not
that any is **right**.* The corpus's own consolidation found **95 receipts that ran green and could
not fail**. **A green suite is a floor.**

**STATUS: draft ready to route. Lens/instrument-owned, so this line's — but ③ touches a gate the
fork also runs.**


---

### ⛭⛭⛭ `S-010` · THE RECEIPT PINS A SUPERSEDED INSTRUMENT — **and my first diagnosis was wrong**

*Full note: `drafts/S-010_the_receipt_pins_a_superseded_instrument.md`. Logs: `twoarm_lcdm_nk290/700/1400.log`,
`twoarm_cr.log`, `twoarm_cr_conv.log`.*

⛔ **FIRST, WHAT I WITHDREW.** *My first draft said the sampling guard's `>= 4.0` threshold was too
loose and the pinned 224 was an under-sampled reading. **False.** At 4.2 points per Bessel period —
barely clearing the guard — the current instrument gives 220/532/812/1116, identical to 10.2 and to
20.5. **Three samplings across a factor of five, one answer. The guard is fine.** The discriminating
run took four minutes and I had not done it.*

| | pinned (`Built c54.168`) | **current instrument** |
|---|---|---|
| ΛCDM control | `CTRL = (224, 536, 808, 1116)` · 0.7433 | **220/532/812/1116** · **0.7300** |
| CR discrete | `(172, 396, 624, 904)` | **172/396/628/908** |
| CR continuum `KCONT=1` | `(172, 396, 624, 904)` | **172/396/628/908** |

**CAUSE: the instrument was rebuilt under the pin.** `ACOUSTIC_two_arm.py` now carries c54.178 work —
*"the matter sector is split into baryons and CDM at c54.178, until now it was ONE fluid"*, and *"the
**photon Boltzmann hierarchy with polarisation** … replaces … a two-moment **FLUID**"*. **The pinned
numbers are the fluid instrument's.**

⚠ **AND THE RECEIPT'S OWN DRIFT-DETECTOR WATCHES THE LAYER THAT DID NOT MOVE.** It says: *"what IS
recomputed is every background quantity they rest on, **which is where a drift would show first**."*
**The background is identical** — D_M 13005 / r_s 135.46 / l_A 301.6 on CR, 13865 / 144.53 / 301.4 on
the control. ***What changed is the perturbation machinery, which the receipt does not recompute.***
*A sensible prior, wrong here for a specific reason: a fluid→hierarchy rebuild changes the source, not
the background it rides.*

⌗ *`THE_HUB`'s "95 receipts that ran green and could not fail", one notch in: **this one CAN fail — it
has real assertions — but it checks its own constants**, so it stays green while the instrument
beneath it is replaced.* **A pinned figure is a claim with a freshness date and nothing carries one.**

**CHANGES, and most are improvements:** re-pin both sets · **the control's floor improves 1.66% →
0.16%, so the receipt's "factor of fourteen in margin" becomes ~140** · the CR deficit is untouched to
four figures (ℓ₁/l_A = 0.5703 before and after) · heights do not improve and PART 2's "no height claim
below ~25%" stands · **the documented `ARM=lcdm python3 ACOUSTIC_two_arm.py` still exits 1**, five
percent short of its own threshold · and one offered generally: **a receipt pinning figures from an
instrument it does not re-run should record the instrument revision the pin was taken at** — this one
names its own build in its header, which is what made the diagnosis possible, and is one field short
of self-checking.

**STATUS: draft ready to route to `FOR_54` — fork-owned instrument and receipt. Physics conclusions
all survive; three of twelve pinned integers and one percentage are stale, and the percentage moves
the receipt's way.**

---

### ⛭⛭⛭ `S-011` · THE OPERABLE QUESTION BEHIND `S-010` — **scan built, control passes**

*`drafts/S011_stale_pin_scan.py`.* Both halves are already corpus conventions: a receipt declares
`Built r2376+c54.NNN`; source files carry `(c54.NNN)` marks. So ask, mechanically: **was the
instrument revised after the pin was taken?**

✔ **CONTROL: the scan flags `P15_two_arm_control_and_guard.py`**, the case verified by hand.
**Five (receipt, instrument) pairs flagged**, four of them pinning `ACOUSTIC_two_arm.py`.

⌗ **Scope of the null, stated because a null needs one:** only **15 of 302** registered receipts
declare a build at all. *The convention that makes staleness checkable is used by 5% of them — which
is the more useful half of this scan.*

⇒ **One flag was chased and it paid: `P15_the_driving_shift_by_subtraction.py` (c54.169) is behind
`S-002`.** *Re-run on the current instrument — the pin holds. See `S-002`'s second addendum for what
it turned up instead.*

---

### ⛭⛭⛭ `S-012` · CI's FAST TIER IS RED AT HEAD AND SIXTEEN GATES NEVER RUN — **verified on a pristine clone**

*Full note: `drafts/S-012_CI_is_red_at_HEAD_and_most_gates_never_run.md`.*

`.github/workflows/gates.yml`, job `fast`, first step: `set -e` then
`python3 scripts/classify_documents.py --check` — **which exits 1 at HEAD (aa2b6ee, main) with
"28 document(s) unclassified"**. `set -e` aborts the step; a failed step aborts the job. ⇒ **the
fifteen text gates and the hollow-assertion lint never execute in CI on any push.**

⌗ **The check is behaving as designed** — its docstring says the classification is *"DECLARED, not
guessed"* and *"the unclassified count is **the step's own done-test**"*. **28 is ARC 14 step 0
reporting it is unfinished.**

⇒ ***So the defect is the wiring: a done-test is wired in as a push gate, and the one check reporting
unfinished work is suppressing every check that reports broken work.***

✔ **And everything behind the wall is green** — the other six view checks 6/6, the fifteen text gates
15/15, `lint_assertions` clean (*"No hollow assertions"*), receipts 288/288. **Nothing is broken; the
pipeline has just been red long enough that its redness carries no information.**

**FIX (middle option, smallest change):** split `classify_documents --check` into its own step or job
so a done-test cannot mask a gate — *the 28 stay visible, and a real failure becomes distinguishable.*
⌗ *And reverse the order: nothing requires the slowest-to-repair check to gate the cheapest and most
diagnostic ones.*

⌗ **Two smaller things alongside:** ① **the heavy job's `pip install … camb pynucastro` was always
right** — so `S-009` is about the container, and it is `THE_HUB`'s prose that is behind, not the
workflow. ② **Running the receipt suite dirties four tracked PNGs** (matplotlib metadata), which a
node committing after a run will sweep in — and they are LFS-tracked.

**STATUS: draft ready to route — this line's own (instruments and CI).**

---

### ⛭⛭ `S-013` · `THE_METHOD` MARKS TWO COMPLETED SWEEPS AS **OWED** — **dug at source**

*Full note: `drafts/S-013_THE_METHOD_marks_two_completed_sweeps_as_owed.md`.*

*Found while starting the deferral audit, which `THE_METHOD` §3e lists as owed.*

| `THE_METHOD` §7 | `THE_PLAN` |
|---|---|
| **`2 · The reference sweep — OWED`** | **`E1_CITATION_CATALOGUE.md` — the reference sweep: opened r1142, ✔ COMPLETE r1144.`** |
| **`3e · THE DEFERRAL AUDIT — OWED`** | **`r1140 — the deferral audit (3e) CLOSED COMPLETE: 5 items, 33 deferrals, not one a real frontier.`** |

⚠ **And the deferral audit's null is load-bearing elsewhere.** `THE_WISDOM_LEDGER`, LIVE: *"⚑ **THE
BASE RATE** … **Evidence: the deferral audit closed 33 deferrals across 5 items and found not one
real frontier**."* ⇒ ***The corpus cites this sweep's completion as the evidence for one of its
most-used priors, while the document that owns the sweep still lists it as work to do.***

⇒ **CAUSE, and it is named in the file's own header:** *"It is a `METHOD` document and its subject is
procedure, **so it does not go stale the way a position does**."* **True of the procedure, false of
§7** — whose rows carry `RUN (r1120)` / `OWED`, which are **positions**. ***A METHOD document
containing a status register is mixed-kind, and the exemption was applied to the whole file.*** ⌗ *The
same failure `THE_OPERATING_MANUAL` §3 warns about for `INDEX.md` — "KIND BEFORE CONTENT".*

**FIX:** mark rows 2 and 3e `RUN` with their revisions and verdicts · **add one line to the header:
"the procedure does not go stale; §7's per-instance statuses are positions and do"** — the fix that
stops the next instance.

⛭⛭ **THE NAMED UNRUN QUESTION, RUN — and three of the six rows are wrong, in three different ways:**
**2** CLOSED r1144 · **3e** CLOSED r1140 · **3c** and **3d** **absorbed into the arsenal's per-paper
9-checklist** (`THE_PLAN`: *"the 9-checklist (signs/**3d-defrag**/idiom …)"*) · **4** **RAN ON ALL
SEVENTEEN PAPERS BY r1406** · **3a/3b** the one plausibly still owed. ⇒ *Worse than stale — a reader
cannot tell that three rows stopped being standalone sweeps and acquired a different owner.*

⚠⚠ **AND ROW 4 CARRIES A DIAGNOSIS MADE AT r1724 AND NEVER ACTED ON.** `THE_PLAN` l.3468: *"the
gathering did not reach its ledger … `JARGON_LEDGER.md` is 3.8 KB, three entries … the pass ran on
all seventeen by r1406 … **the cheap discriminator, and it is one command: the live counts.
`do-not-assert` now stands at 43 across 14 files** against the ledger's single row for it."*
**I ran it:**

| | at r1724 | **at HEAD** |
|---|---|---|
| `JARGON_LEDGER.md` | 3.8 KB | **3.8 KB — unchanged** |
| `do-not-assert` in `corpus/*.tex` | 43 / 14 files | **45 / 14 files** |

⇒ ***Seven hundred revisions on, the ledger is the same size and the gap has widened by two.*** ⌗ *The
corpus's own law turned on itself:* **"check the fix, not just the diagnosis"** *— and what makes it
visible is that the note wrote down its own test.*

⇒ **SO THE FIX IS LARGER:** §7 needs a status vocabulary that can say what happened — `CLOSED (rev)` ·
`ABSORBED INTO <instrument>` · **`RAN, FINDINGS NOT LANDED`** · `OWED`. **Row 4 needs the third, and
the corpus has no word for it** — which may be why a found-and-unfixed defect sat quietly.

**STATUS: draft ready to route — this line's own (a METHOD document).**
