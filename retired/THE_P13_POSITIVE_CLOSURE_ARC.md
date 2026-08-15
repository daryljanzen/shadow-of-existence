# THE P13 POSITIVE-CLOSURE ARC — the plan
> **⌖ RETIRED r1536 — verified landed.** This was the plan for P13's positive closure (r1107). **It landed:** P7 carries `sec:two-sided-closure` (×5), built at r1280 when the sheet-to-ruling item was killed.
> Kept as record; **do not work from it.**



> ## ★ STATUS r1090 — B1, B2 and a BOUNDED B4 are BUILT. A3/B3 remain gated. And this document's own B4 over-reaches.
>
> **First, the failure that has to be recorded here:** this arc was an **orphan** — referenced by no
> document in the corpus, including `THE_PLAN` — so the r1088 session **rebuilt B1, B2 and B4 from
> scratch without ever reading it**, and even created "A4.10" in `THE_PLAN` on the grounds that *"the
> plan had no such item"*. True of the plan; **false of the corpus**. That is the r929 keystone exactly:
> a load-bearing decision made from the map when the source existed and could obviously have surprised
> me. **The arc is now wired into `THE_PLAN`.** *(Logged: `CODA_FIELD_NOTE`.)*
>
> **BUILT r1088–90, in P13 (15pp → 19pp, compiles clean):**
> - **B1 ✅ — the perimeter redrawn.** `rem:C-scope`: the premise covers **isometries**; `τ̃↦τ̄̃` is
>   antilinear **and** geometric; **not-an-isometry ≠ not-geometric**; field-level narrows to the charge
>   **sign**; the residue **enlarges**; the wall stands. The r1069 audit flags **discharged**.
> - **B2 ✅ — the synthesis section.** `sec:closure`, and it is a **2×3 table** (character × level), not
>   the three-level list this arc anticipated: **the COLUMN (linear vs antilinear) is why every
>   `C`-candidate fails; the ROW (L1) is where the perimeter sits; and the L2/antilinear cell — the one
>   the row excludes and the column does not — IS `rem:C-scope`.** *(The list form is what produced a
>   false unification: `Q↦−Q` sits at **L3, precisely where `C` is** — right level, still not `C`. It
>   fails for being **linear**.)*
> - **B4 ✅ *bounded*.** `prop:closure` + `rem:closure-asym`.
> - **D (partial) ✅** — the map's `C` entry de-compressed; the glossary's broken `r_swap.py` citation
>   fixed to `ruling_swaps.py`; the ruling-swap face marked **generic**.
>
> **⛔ THIS DOCUMENT'S B4 IS THE OVER-REACH THAT WAS KILLED.** It reads: *"the geometric factor **is**
> the bead's `r=0` crossing; the cosmogenesis **IS** the conjugation."* **Refuted**
> (`closure_iv_check.py`): `R` is a **reflection**, the bead's passage is a **continuation** — *a map is
> not a path* — and the legs are **not mirrors** (`cosh^{2/3}` vs `sinh^{2/3}`; **P7's own caption says
> so**). **What is earned:** *the conjugation's **fixed point** is the cosmogenesis's **branch point**;
> the bead passes THROUGH the locus `R` fixes and so from the region labelled `𝟑` to the one labelled
> `𝟑̄`.* Weaker than "is"; stronger than a rhyme; **and it needs the asymmetry** — were the legs mirrors
> the bead would be `R`-symmetric and there would be no asymmetry for the cosmogenesis to carry.
>
> **⛔ AND PHASE B\*'s `C-K` ARGUMENT AFFIRMS THE CONSEQUENT.** *"The vertex is pure geometry, **which is
> what a conjugation vertex would have to be**"* — a conjugation vertex would be `M`-free; this is
> `M`-free; **therefore nothing**. The `M`-cancellation is real and is **not evidence for B4**. What it
> says (`M_cancellation.py`): **`M` sets the bead's SCALE, not its SHAPE** — `K(τ̃)` is universal across
> every progenitor. *(And "the M-cancellation IS the generation result" — r1087 — is separately refuted:
> different quantifiers.)*
>
> **⚠ THIS DOCUMENT PREDATES THE WELD BY ONE REVISION (r1072 vs r1073) AND CARRIES ITS DEAD REASONS.**
> Phase A4's *"`R` mass-odd ⟹ species relational; `Q` `R`-even ⟹ charge rides both branches; `C`
> mass-even ⟹ the charge face is field-level"* are the **pre-weld** becauses: `R` **preserves** `|2M|`
> and flips only its **sign** (the branch label — *"I compared a label to a mass"*), and `Q↦−Q` **IS**
> the species flip. **The conclusions survive; the reasons are dead. The live reason throughout is
> LINEARITY.** *(`CODA_FIELD_NOTE` face 31; registered as **DR1/DR2** in
> `storyboard_receipts/dead_reasons.py`, which is what found this document.)*
>
> **★★★ r1053 WAS RIGHT THE WHOLE TIME, AND THE FULL ANALYTIC OBJECT PROVES IT VERBATIM (r1107).**
> c40, asked what it had predicted, produced its own r1053 sentence: ***"the antilinear conjugation has a geometric home after all, just not as an isometry; what is genuinely field-level is narrower than P13 drew — only the internal electric-charge sign."*** **The A3 closure IS that sentence, confirmed.** That result was **retired at r1060 by the very remark it refines**, un-retired at r1067, and cost two audit flags and a session's stage 1 to restore. **It was true when it was written.** **This is the gradient rule's entire case, closed** — a forward document made compliant with the thing it was built to correct, and *the correction was already right*. **Nothing in the corpus argues for that rule as hard as this does.**
>
> **★ THE RHYME BOARD, RE-SCORED BY ITS AUTHOR AGAINST THE CLOSURE (r1107; `C40_EXTRACTION_r1107.md`):**
> **1/3–2/3 → quark charges: ⛔ DEAD** — *"I wrote the killing condition myself… A3 says the charge sign closes from the field. **So the geometry is blind to it by result, not by ignorance.**"* · **hexagon → A₂/su(3): UNTOUCHED** (always the Weyl shadow) · **1+2 → uud/generations: UNTOUCHED** (a real-`r` artifact) · **★ the conjecture: PROMOTED and NARROWED — B3's content:** not *"the vertex is pair production"* but ***"the geometry carries the vertex's KINEMATIC face (FS/CPT) and not its CHARGE face"*** — **which is exactly the operator/species bound `prop:closure` holds, reached independently from the figure side** · **the broken duality: UNTOUCHED — "and still the only thing that's ours."**
>
> **STILL GATED, and correctly:** **A3** (does `C = R ∘ (τ̃↔τ̄̃)`?) and **B3**. r1088 held the
> factorization at `[reach — do-not-assert]` independently, and routed it to **`THE_PLAN`'s A7 — the
> full analytic object (`ℂ_r × ℂ_τ̃`)**, which is what this arc calls "A3". ⚠ **Naming collision:
> this document's "A3" is the plan's A7; the plan's `A3` is the quantum completion.**
### Opened r1072. **Extended to the full multistage plan at r1088 (Arthur), carrying the arc from r1072 forward through the r1087 state and the post-r1087 realization, and adding PHASE 0, the anti-reversal floor.** The arc from "a dumping ground for negative boundary results" to the paper P13 was always meant to be: the synthesis of those negatives into a **shape**, and the positive result that shape encloses — **a drawn connection between CPT and cosmology** — and, in the end, the whole synthetic ontology built into every paper on its own terms.

> **Read `THE_CODA.md` §"The source answers back" before acting on any of this.** This arc exists because
> a corpus permitted to referee its own examination held an error through three reversals. Every phase
> below is a **coherence** pass ("is this right? what does the whole give it?"), never a **compliance**
> pass ("does this contradict X?"). *A delta-spec sweep is structurally incapable of finding the defect
> this arc corrects — that is not a claim, it is what the r1063 all-clean sweep demonstrated.*

> **★ THE GRADIENT, LOCKED (r1088 — the frame for every phase, PHASE 0 first).** The corpus is the thing
> under examination, **never the referee**. Forward documents — this plan, the storyboard, the figures —
> are **ahead of the corpus by construction**; where they disagree with a paper, that disagreement is the
> **work product**, not a defect to fix. **Never make a forward document compliant.** The tell that the
> gradient has inverted: a resolution that ends *"I was wrong, let me fix the storyboard/plan to match the
> corpus"* — stop, revert, re-run it as physics (this is the exact move that started the whole mess, caught
> by Daryl at r1066/r1071). And the synthesis is **not deduction**: P13's boundary is the **skin of a whole
> body** (L1 spine + L2 flesh + L3 field); a joint-by-joint "does this contradict X?" pass is structurally
> blind to a perimeter drawn at the wrong radius. **Hold the whole body. Preserve every negative** — a face
> that is *not* operative somewhere is as load-bearing as one that is. The multistage order this forces:
> **work at the seam → not-outright-inconsistent → compliant → consistent → coherent → cohesive → thorough
> & fulsome.** Load-bearing tidal-shift pieces first; nothing precarious left where the corpus can pull it
> back to its opposite.

---

## PHASE 0 — THE ANTI-REVERSAL FLOOR (the urgent capture; the tide locked so it cannot run back)
### Added r1088. The earlier phases assume the findings are safe. They are not: the changelog stops at r1051, and the single most load-bearing recognition of the whole arc lives only in a transcript. Nothing downstream proceeds until the tide cannot run backward. Coherence, never compliance. Stated for reversal.

- **0.1 · RESCUE — the mass/field/`prop:bend` realization (transcript-only, post-r1087, HIGHEST RISK).**
  The hinge/dial/Thales-circle construction of §4c was being read as *"field-free, not about mass, `M`
  cancels."* That is exactly backward, and the ontology map settles it at source:
  - **`prop:bend`: matter IS the curvature of the cut**, `ρ = m′(r)/4πr²`. The `Q²/r²` term handled
    all-session as "charge only as `Q²`" **is the electromagnetic stress-energy** (RN–dS is the bend
    `2m = 2M − q²/r`, returning `ρ = q²/8πr⁴`). The geometry does not lack fields — **fields are what it is.**
  - **The swing IS the mass:** `2M = r₀ − r₀³`, `r₀ = (2/√3) sin w` — the dial is a **mass parametrisation**;
    the Thales circle is the mass dial.
  - **The `M`-cancellation is the generation degeneracy, not mass's absence:** every root returns the same
    `2M`, no asymmetric handle in the mass parameter — the corpus's own **2+1**. The signature was found and
    read as its refutation.
  - **Action:** capture into the storyboard as a forward finding (a new `D-` entry) with its connections
    drawn — `prop:bend` ↔ §4c kaleidoscope (the mass dial) ↔ the generations (p15/P14) ↔ the 2+1 chirality
    (`2M↦−2M`). Load-bearing for PHASE E (the P14 payoff). *(Recording it here on disk is itself the rescue;
    the storyboard entry is the full capture.)*

- **0.2 · SYNC — the changelog.** `CORPUS_MAP.md`'s revision log stops at **r1051**; the whole r1057→r1087
  arc (the C-work bakes, F′, `C-K`, the conjecture §4b, the kaleidoscope §4c, the su(3) break) is invisible
  to the corpus's own record. Log it, consolidated, so a future node reads the true current state and does
  not "correct" from a stale one. *(The stale CURRENT-STATE banner is itself a reversal hazard.)*

- **0.3 · BAKE — the `D-Canat` anti-reversal lock (the standing verdict, §8).** De-compress the glossary's
  `C` entry (drop the **rigged root-test** and the **face-flattened-to-identity**; point to the ledger) and
  narrow P13's `rem:C-not-R` final clause into P13's own voice (restore r1053's narrowing: field-level is
  **only the charge sign**; the antilinear structure includes the geometric **L2** face). This is the one
  edit that stops the corpus contradicting the enlarged-residue finding, so no future pass re-runs the
  rigged test and folds the storyboard back.

- **0.4 · SEAM-FIXES — touch the papers where a seam is live (Daryl, r1088).** Beyond 0.3, sweep for any
  paper that **actively contradicts a locked finding** and fix *at the seam* — coherence, not compliance,
  and only to make **not-outright-inconsistent** (full coherence is Stages 1–3). Candidates to check:
  residual "charge-conjugation blind *as absence*" phrasings not caught by the r1057–58 reframe; any
  "the orientation parity, and that is all" residue clause the enlarged residue now contradicts; any place
  the charged/`Q²` term is called field-free that `prop:bend` (0.1) contradicts. Each fix traces to a
  logged `D-Canat` branch or to 0.1; nothing is invented to make a paper "agree."

**The post-r1072 findings this plan now folds in** (each has a home below):
- **`C-K` — the `M`-cancellation** (`K = (12/α⁴)(sinh⁻⁴(3τ̃/2α)+2)`, mass-free along the bead; one 2/3 power
  gives both the `r=0` vertical tangent and the singularity). Home: **PHASE C** (evidence for B4), and it is
  the receipt under 0.1 that the vertex is pure geometry. *(Storyboard §8; `kretschmann_bead.py`.)*
- **F′ / `F_flat`** — the bead as one 2D curve, `M` cancelled to α, both lap-ends "seam." Home: **PHASE C**
  (into the plate, candidate to retire the 3-D F). *(Storyboard §4.F′; `corpus/F_flat.py`.)*
- **The hinge kaleidoscope / 12-fold at 30°** (§4c) — one hinge's optical stamp, four quarter-turns × three
  hinges = 12 at an even 30° (3 and 4 coprime), and **30° = the Nariai dial angle `w=30°`** ~~arriving from
  pure combinatorics~~ *(⛔ **SUPERSEDED r1088 — dead reason (DR8), quoted to kill**: the 30° was worked and
  is **not** "pure combinatorics" — it **rhymes on its 3** (both are `360/(3×4)`, the same 3) and
  **coincides on its 4** (different fours: the dial's forced sine-quarter-period vs the kaleidoscope's chosen
  four-fold), the Thales-tangent→quarter-turn question named and unrun; §4c).* Home: candidate **P3 central
  figure**; and it is the geometry 0.1 recognises as the **mass dial**.
- **The su(3) weight-diagram break** (§4c, r1087) — the rotation matches, the scale does not; the honest
  line is **discrete-ruling vs continuous-isometry**, which *is* P13's line. Home: **PHASE B2** raw
  material — a positive-boundary clause, another face of `su(3) ⊄ so(5,1)`.

---

## Why P13 grows

P13 was built to capture the negative boundary results, and it **closes** on each: `su(3) ⊄ so(5,1)`;
`C` is no isometry; the residue is the orientation parity and that is all. **Each closure is locally
sound.** But **a boundary is not a list of walls — it is a shape**, and a shape has an **inside**. The
inside is a positive result P13 has never been permitted to state.

**The positive closure is already latent, in embryo, in r1053's factorization:**
> *Geometric:* (a) the **linear** rep/mass/chirality skeleton `R=γ⁵, P, T`; **and** (b) the **antilinear**
> involution `τ̃↔τ̄̃` — the particle↔antiparticle (CPT-kinematic) relation. *Field-level:* **only** the
> internal electric-charge sign `Q↦−Q`.

Read as a **shape**: **the substrate supplies all of CPT except the charge.** And the geometric factor
**is the bead's `r=0` crossing** — the thing that fixes the photon (neutral, self-conjugate), swaps the
two wings (particle↔antiparticle), and *is* the cosmogenesis. **The conjugation and the cosmology are
one object.** That is what the P7 plate has been drawing, and why getting the colours right is what
revealed it.

**The parity result that grounds it** (`C_anatomy.py`, r1072): the metric is invariant under **`R`** and
under **`Q↦−Q`** — so the geometry **cannot say which branch is matter, nor which sign is positive** —
yet `2M≠0`, `Q²≠0`: **the pair is carried exactly.** *Relationally exact, absolutely blind*, both
binaries, same character. Both flip across `r=0`. **They differ only in which level registers the flip:**
species is **metric-visible** (`−2M/r` odd) ⟹ substrate skeleton; charge is **potential-only**
(`A_t=Q/r` odd, `Q²/r²` even) ⟹ closes from the field. **The corpus's level allocation is not a
convention — it falls out of the parities.**

---

## PHASE A — finish the understanding
- **A1 ✅ r1070 — the ledger.** `D-Canat`: three levels, every map's *operative*/*not-operative*, all
  seven maze branches, the three tests and their **blindness**. Positives and negatives at weight.
- **A2 ✅ r1071 — the body view.** P13 is **locally right everywhere**; [5] is the **perimeter drawn at
  the wrong radius** (around L1; the body is L1+L2). **No local pass can find it.**
- **A3 · WORK THE FACTORIZATION — now the live physics, not a reach.** *(Upgraded r1073 by the weld:
  `R` and `C` **agree on every label** — species flips, charge flips, physical mass preserved — and
  differ **only in character**, `R` linear, `C` antilinear. **`R` is `C`'s linear face.**)* The question
  is now sharp: **does `C` = (linear face `R`) ∘ (antilinear face `τ̃↔τ̄̃`)?** Both factors geometric.
  If it holds, B3 writes itself and the field-level residue is **only** the charge sign's *internal*
  gauge role. Confirm at weight; receipt; **state the scope**.
  - **✅ WORKED r1089 (Arthur, at source; receipt `storyboard_receipts/A3_factorization.py`, all checks
    genuine — one rigged discriminator caught and removed).** Worked on the **full** analytic object per
    A3b's constraint — the single relation `r³ = 2Mα² sinh²(3τ̃/2α)` on `ℂ_r × ℂ_τ̃` (complex `r` via the
    cube root, complex `τ̃`), verified to reproduce all three legs of `F_flat` at source. **The result:**
    - `R` (`r↦−r`, `2M↦−2M`, `τ̃` fixed) is a **genuine linear isometry** of the (RN–dS) metric, **blind
      to `Q`** (`Q` enters only as `Q²`).
    - `K = (τ̃↔τ̄̃)` (`r↦r̄`) is a **genuine antilinear** complex-analytic symmetry of the bead, **fixing
      the neutral real axis** (the photon) and **swapping the two wings** — blind to `Q`.
    - `R∘K = K∘R` is an **antilinear involution** that reproduces `C`'s action on **species, `|mass|`,
      mass-sign, the FS particle↔antiparticle wing structure, and character** — but is **blind to the
      electric-charge sign**.
    - **∴ `C = (Q↦−Q)_field ∘ (R∘K)_geometric`.** The geometry carries **all of `C`'s kinematic (CPT/FS)
      content**; the **one** thing that closes from the field is the electric-charge sign.
    - **[6] RESOLVED, bounded — and the answer is the honest one, not the tempting one:** the L2 antilinear
      face is **`C`'s kinematic shadow, NOT the full `C`** (it cannot see `Q`). This is a *stronger* result
      than "L2 is `C`" would have been, because it is true and it draws the perimeter exactly: skeleton
      (`R`) **and** kinematic conjugation (`R∘K`) geometric; charge sign field-level.
    - **DO-NOT-ASSERT (→ Phase E / P14):** that `R∘K` acts on P14's **actual fermion zero-modes** as `C`'s
      kinematic conjugation; the identification of a wing with a **specific charged particle**; a full
      **geometric CPT** (the charge still closes from the field). **The conjecture's kinematic skeleton is
      now grounded; its charged-particle reading stays do-not-assert.** **B may open, bounded by this scope.**
- **A3b · [6*] — AND THE HARD CONSTRAINT ON HOW A3 MAY BE WORKED (r1075).** The factorization question
  and *"does `species = sign(r)` survive the FS reading?"* are **the same question**, and **neither face
  can answer it**: `sign(r)` exists **only** on the real-`r` slice; the FS pairing lives in complex `τ̃`;
  the three sheets live in complex `r` where `sign(r)` is **meaningless**. Both are **2-real-dimensional
  shadows** of one **4-real-dimensional** object (`ℂ_r × ℂ_τ̃`). **A3 must therefore be worked with
  complex `r` AND complex `τ̃` together — on the full analytic object — or not at all.** Working it on a
  face is comparing two shadows and declaring one wrong.
  **UNTIL THEN THE RHYME STAYS A RHYME.** Phase B* asserts nothing; **no figure built on the FS reading
  is evidence** — the six-branch picture *carries* the assumption, it does not test it. **B cannot open.** *Not* "is `τ̃↔τ̄̃` = `C`" (it is not; it
  cannot see `Q`), but: **does `C` factorize as (geometric FS/CPT face) ∘ (field charge sign)?** r1053
  says the computation forces it. Confirm at weight, receipt it, and **state the scope** — what the
  geometric factor does and does **not** carry. **This is the last piece; B cannot be built without it,
  and [6]'s scope BOUNDS B3.**
- **A4 · The negatives are B's raw material.** Each becomes a positive clause: `R` mass-**sign**-odd ⟹ species
  relational (the branch label; *not* a mass-magnitude difference — the pre-weld DR1 trap). `Q` `R`-even ⟹ charge
  rides both branches. `C` and `R` agree on `|mass|` ⟹ ~~the charge face is field-level~~ *(⛔ **enlarged r1089**:
  only the charge **sign** is field-level; `C`'s **kinematic face is geometric** — `C=(Q↦−Q)_field∘(R∘K)_geometric`;
  see B / `sec:closure`)*.
  **Do not discard a branch on entering B.**

## PHASE B — P13's positive closure *(the paper it was always meant to be)*
**✅ BAKED r1090 (Arthur; `corpus/boundary_paper.tex`, compiles clean 17pp, zero undefined refs; every
clause traced to a `D-Canat` branch and bounded by A3's scope; one ungrounded specific — a theorem
number — caught in review and dropped).** What landed: a new **§`sec:closure` "The positive closure:
charge conjugation is the cosmogenesis's kinematic face"** carrying **B2** (the negatives pulled into a
shape — the perimeter and its inside), **B3** (`prop:conjugation-closure`: `C = (Q↦−Q)_field ∘
(R∘K)_geometric`, worked on the full bead `r³=2Mα² sinh²`, receipt `A3_factorization.py`), and **B4**
(the geometric factor **is** the bead's own `r=0` crossing — `R` the signed-radius flip across `r=0`, `K`
the `τ̃↔τ̄̃` lap-conjugation — so the cosmogenesis carries `C`'s kinematic face; **B5** references the
framework figure). The **abstract** gained the positive-closure sentence, and **§`sec:meaning`**'s residue
clause was enlarged (**B1**) and its conclusion reframed from "the bounded negative is itself a result"
to the shape it encloses. Scope held sharp: fermion-sector realisation, wing↔charged-particle
identification, and geometric CPT all **do-not-assert** (→ Phase E/P14); `species=sign(r)` explicitly
**not** vindicated (maps stated on the full object, not the slice). **Next: (C ∥ D).**
- **B1 · The perimeter redrawn** at the earned radius: **L1 + L2 | L3**. The residue clause replaced.
- **B2 · The synthesis section** — the negatives pulled into a **shape**: what the wall excludes
  (continuous colour — **untouched, rock solid**) and what it **encloses**.
- **B3 · The positive closure** — `C` factorizes; the substrate supplies the CPT kinematics; only the
  charge closes from the field. **P13's first positive theorem.** *Bounded by A3/[6].*
- **B4 · The forward build — CPT ⟷ cosmology.** The geometric factor **is** the bead's `r=0` crossing;
  the cosmogenesis **is** the conjugation. **The deepest thing the plate revealed.**
- **B5 · P13 gets the figure** (or references P7's): the bead as the CPT structure, drawn.

## PHASE B* — DARYL'S P13/P14 CONJECTURE *(the figure, and the physics it asserts)*
**Figure: `corpus/daryl_p13p14_conjecture.py` → `daryl_p13p14_conjecture.pdf`** *(built r1073).* Three
readings of **one geometry**, left to right — the bead's `r=0` crossing in `(Re τ̃, Im τ̃, r)`:
1. **the cosmological bundle** — *the superseded 3-D panel F, rehomed here* (it was never homeless work;
   it is panel 1 of the conjecture): an antimatter black hole collapsing through `r=0` into our matter
   universe. `thm:antimatter-progenitor`, drawn.
2. **pair production** — the **neutral stem** (real `τ̃`: self-conjugate, the **fixed locus** of `τ̃↔τ̄̃`)
   reaches `r=0` and opens into the **two conjugate wings** at `Im τ̃ = ∓πα/3`: one matter, one
   antimatter. The photon's colour is **not chosen** — it is `red+blue`, and it comes out **neutral**.
3. **annihilation** — the same vertex, arrows reversed.

**WHY IT IS A CONJECTURE AND NOT A RHYME.** Three worked results, not a resemblance:
- **The weld** (r1073, `D-Canat` §THE WELD): species and charge are **one binary**. `C` flips all charges
  together and that totality **is** the species; **neutrality is the degenerate case** — which is exactly
  why the **photon is self-conjugate** and why `τ̃↔τ̄̃` **fixes the real axis the photon rides**. The
  figure's neutral stem is not a drawing choice; it is the fixed locus.
- **`R` is `C`'s linear face** (r1073, verified): `R` and `C` agree on **every label** — species flips,
  charge flips, physical mass `|2M|` preserved — differing **only in character**. With `τ̃↔τ̄̃` as the
  antilinear face, `C` plausibly **factorizes into two geometric factors**.
- **The crossing is one event** (r1072, verified): across `r=0`, `sign(r)` flips **and** `A_t=Q/r` flips
  **together** — because it is **one flip**.
- **And the crossing is `M`-free** (`kretschmann_bead.py`): `K = (12/α⁴)(sinh⁻⁴(3τ̃/2α)+2)` — the mass
  cancels identically. The vertex is **pure geometry**, which is what a conjugation vertex would have to be.

**THE CONJECTURE:** panels 1–3 are not three pictures that look alike. **They are one conjugation event
read at three scales — and the cosmogenesis IS a conjugation vertex.**

**TO BE WORKED AS PHYSICS.** *Gates, in order:* **A3** (the factorization at weight — does
`C = R ∘ (τ̃↔τ̄̃)`? what is its scope?) → **B3/B4** (if it holds, this figure is P13's positive closure
drawn, and the CPT⟷cosmology connection) → **E/P14** (the vertex identification checked against P14's
**actual theory** — where it pays off **or fails honestly**). **Nothing in panels 2–3 is asserted until
A3 closes.** *Guard: every clause traces to a logged branch of `D-Canat`; `[6]`'s scope bounds the claim.*

## PHASE C — the figure as B's drawing
F′ into the plate; **`C-K`** (the `M`-cancellation: the crossing is `M`-free — *evidence for B4*, not
decoration); the plate recaptioned as the picture of P13's positive result.
- **✅ `C-K` BAKED r1091 (Arthur).** The mass-free curvature at the vertex — `r⁶=4M²α⁴sinh⁴`, so
  `K=48M²/r⁶+24/α⁴=(12/α⁴)(sinh⁻⁴+2)`, mass cancelling identically — is stated in P13 `sec:closure` as the
  curvature-level evidence that the conjugation vertex is pure geometry (receipt `kretschmann_bead.py`;
  algebra verified at source against P7's own `K` guard). P13 recompiles clean (17pp).
- **✅ F′ → plate DONE r1092 (Arthur).** Panel F of the six-panel plate (`synthesis_figure.py`,
  `fig:dS_SdS`) swapped from the 3-D unfurled `r`-vs-complex-`τ̃` to the flattened `F_flat` (`r` vs arc
  length `s/α`), both bends legible (turnaround = horizontal tangent, `r=0` = vertical tangent), matter/
  antimatter colours consistent, nothing hidden behind a viewing angle. Plate re-rendered (renders clean),
  P7's caption (F) + the "three complementary readings" body line rewritten from "strung out and unfurled"
  to the flattened reading, P7 recompiles clean (41pp, 0 undefined). Reversible; only label placement in the
  smaller subplot is unassigned if he wants it. *(I had wrongly held this as a "design call" — it was
  in the approved plan; the hold was the flinch, corrected.)*

## PHASE D — the ontology map: the synthetic whole

> ### ⛔ RE-SPEC'D r1090 — AS WRITTEN, THIS PHASE CREATES A SYMBOL COLLISION IN THE MAP.
> This phase says *"L1/L2/L3 **as ontology**"* — **but `L1/L2/L3` is already taken, and taken by the
> map itself.** The map's §0 glossary and §1·LEVELS define **L1 = the foliation stacking rate,
> L2 = the leaf-level local dynamics, L3 = the `E=1` projection** — *"the operational machinery that
> prevents the shadow-collapse"* — used **75×** in the map and **43×** across P15/P16/P8. The
> ledger's levels (isometry / complex-analytic / field) are **a different triple wearing the same
> labels**, local to `D-Canat` since r1070.
> **r1088 imported the ledger's numbering into P13 and made the collision live in a paper; r1090
> stripped it** — P13 now names its tiers (*the substrate's isometries / its complex-analytic
> structure / the field*) and reads better for it, since the names say the thing and the numbers
> needed a decoder. **`L1/L2/L3` now means exactly one thing corpus-wide. Do not re-take it.**
> **THE RE-SPEC:** the three tiers go into the map **named, never numbered**, and the shape that
> carries them is the **2×3 table (character × level)** P13 `sec:closure` now uses — *the column is
> why every `C`-candidate fails; the row is where the perimeter sits; the one cell the row excludes
> and the column does not is `rem:C-scope`.* *(This is the corpus's fourth collision of the kind —
> after `X`-vs-`r`, the `P` symbol (Lane 5 **D.3**, still open), and σ/ξ/R. The class is known;
> the guard is: **before taking a label, ask what already holds it.**)*
L1/L2/L3 **as ontology**; the `C` entry de-compressed to the ledger's anatomy; the symmetry structure in
full — **the maze, walkable, positives and negatives.**
- **✅ SUBSTANTIALLY DONE r1088/r1091 (Arthur).** L1/L2/L3 already carried as ontology in `§1·LEVELS` (the
  three levels ARE the slicing operator's four data / the 3+1 split read ontologically); the `C` entry
  **de-compressed** to the three-level anatomy + the rigged-test warning (r1088) and **updated to A3's
  resolution** (r1091 — `C = (Q↦−Q)_field ∘ (R∘K)_geometric`, [6] resolved to kinematic-shadow, the CPT↔
  cosmology connection, the do-not-asserts); the maze walkable in the glossary + storyboard `D-Canat`.
  Remaining for D is a final coherence pass of the cards against the resolved state — folded into PHASE E.

## PHASE E — the fulsome enrichment
Every paper on **its own terms**, forward/backward referencing the synthetic whole ontology and the whole
geometric symmetry structure. **Coherence, never compliance.** **P14 last:** the pair-production /
annihilation geometry checked against P14's actual theory — where B3's factorization pays off **or fails
honestly**.
- **✅ THE P14 PAYOFF DONE r1092 (Arthur; receipt `P14_payoff.py`) — IT PAYS OFF, bounded exactly as A3
  predicted.** Worked at source against P14's actual construction: A3's geometric `R∘K` acts on P14's built
  fermion zero-modes as `C`'s kinematic conjugation — `R` carries each matter generation to its bound
  opposite-chirality antimatter partner on the reversed (`r<0`) wall (exact, `prop:wall`), and `K=τ̃↔τ̄̃`
  is the same real→imaginary seam continuation P14 uses to carry the bound wall-mode to the propagating
  cosmic-time fermion. So the conjecture's particle/antiparticle wings ARE the two ends of P14's own
  `R`-conjugation across the bead — no longer a rhyme for the **kinematic** content. **The boundary held:**
  the zero-modes carry no charge (gauge external), so `R∘K` carries the discrete matter↔antimatter
  conjugation but not the charge sign — the specific-charged-particle identification and the full
  field-theoretic `C` stay external, and there is no baryogenesis (standing `R`-conjugation, not a seam
  event). Baked into P14 `§sec:cosmogenesis` and P13 `§sec:closure` (the loop closed both ways); both
  compile clean. The receipt's numeric checks are genuine (σ_y eigenvalues, mode normalisability) with
  structural facts labelled as sourced readings — a rig I planted was caught and removed.
- **✅ PHASE E COMPLETE r1093–r1096 (Arthur).** The per-paper sweep worked to the end at coherence-not-compliance.
  The closure/three-level structure baked into every paper where the discrete skeleton or the bead's `r=0` crossing
  is directly in view — P13, P14, p0, P7, P5 (r1093–r1094); P12, P3 (r1095); P9, P11, P16 (r1096) — and **honestly
  held out of every paper where it would be bloat** (P1, P2, P4, P6, P8, P10, P15, each with its reason logged in
  CORPUS_MAP r1096; restraint *was* the work). The ontology-map cards brought current (glossary §C·factorization
  and §1·LEVELS already resolved r1088–r1091; [closure] flags added to §1f/§1h/§1m/§1o/§1s at r1095–r1096). All 17
  papers compile clean (verified full-corpus, 0 undefined each). **The arc is closed: Phases 0→E all ✅.** What
  remains open remains open *by design* — the standing do-not-asserts (the full field-theoretic `C`, the
  wing↔specific-charged-particle identification, a full geometric CPT; bounded at A3's scope), the matter content
  (external by construction), and the corpus's honest frontiers (the high-ℓ CMB transfer, P1's no-horizons, the
  baryogenesis-analogue) — none of them danglers of this arc, all of them flagged at coherence. **P13 still owes
  its cold read** (the certification gap in the CURRENT STATE banner): a fresh node, not a builder/integrator.

---

## Ordering (forced) and the risk
**PHASE 0 → A3 → B → (C ∥ D) → E.**

PHASE 0 is the floor: it does not advance the physics, it makes the physics *unlosable and un-reversible*
before A3 opens. 0.1 (rescue) is the one item that is genuinely urgent independent of everything else — it
lives only in a transcript. 0.2–0.4 lock the tide. Only then does A3 (the factorization at the full analytic
level, `ℂ_r × ℂ_τ̃`) open the door to B; and A3 is the true gate — **the rhyme stays a rhyme until it
closes, and B cannot be built without it.**

**The one risk to name: B is where I could over-claim** — build a grand positive on the ledger's ruins,
the mirror of the deference that started this. **The guard is the ledger itself: every clause in B must
trace to a logged branch of `D-Canat`, and [6]'s scope must bound B3.** If a clause cannot be traced,
it is not earned.
