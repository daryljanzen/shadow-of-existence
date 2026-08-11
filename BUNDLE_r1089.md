# Bundle r1089 — P13's positive closure BUILT, and then attacked five times by the hand that built it

Stage 7 of the tidal shift (`retired/TIDAL_SHIFT_PLAN.md`), i.e. **A4.10** — the destination Daryl named at
r1071: *"p13 … currently draws a close on various proofs without actually pivoting to draw something
positive from all of it … Now it synthesises those at weight at exactly the earned level and draws a
synthetic picture of the whole AND BUILDS FORWARD FROM THAT … nothing short of a drawn connection
between CPT and cosmology."* **Built whole, then found wrong at source in five specific places —
none of them fatal, every one of them a strengthening.** P13: **15pp → 19pp**, zero errors, zero
undefined refs, every citation resolving. Builds on r1088.

## The closure — `\section{The positive closure: what the boundary bounds}` (`sec:closure`)

It opens on what was actually wrong with the paper: *"A boundary is the boundary **of** something, and
until now this paper has drawn one without saying what it encloses."*

- **The body**, and the thing five attacks turned it into — **a 2×3 table, character × level**:

  | | linear | antilinear |
  |---|---|---|
  | **L1** isometry | `R=γ⁵`, `P`, `T`, `σ` | — |
  | **L2** complex-analytic | — | `τ̃↦τ̄̃` |
  | **L3** field | `Q↦−Q` | **`C` proper** |

  **The column is why every candidate fails** (all linear; `C` is not — `rem:C-not-R`'s own argument).
  **The row is where the perimeter is drawn** (the wall asks after a continuous *isometry* — the L1 row
  and nothing else). **And the two cross at one cell the row does not contain and the column does not
  exclude — L2/antilinear — which *is* `rem:C-scope`.** *Not-an-isometry is not not-geometric* is not a
  further argument bolted on; **it is that cell, read off the table.** *"The negatives are unified by the
  column; the perimeter is set by the row; and the correction the residue needed lives where the two do
  not meet."*
- **`prop:closure` — the residue is the cosmogenesis's own symmetry.** `R` is the single reflection
  `r↦−r`, which carries `𝟑→𝟑̄`, reverses the mass, and **fixes exactly `r=0` — the bead's branch point**,
  exchanging the two regions the bead's halves occupy. **The conjugation's fixed point is the
  cosmogenesis's branch point.** The bead passes *through* the one locus `R` fixes, and in doing so passes
  from the region `R` labels `𝟑` to the region it labels `𝟑̄`.
- **`rem:closure-asym` — the asymmetry is the content, not a blemish on it.** The legs are **not** mirrors
  (`cosh^{2/3}` vs `sinh^{2/3}`; P7's own caption says so). **That the bead is not `R`-symmetric is what
  makes the crossing an *event*** — were the legs mirrors there would be no asymmetry for the cosmogenesis
  to carry. *(Daryl, r1078: "the asymmetry IS the symmetry-breaking, not a footnote to it.")*
- **The forward reading.** The continuous symmetry is spent on the geometry and cannot carry a gauge
  group; what it leaves is a discrete residue; **and that residue is the symmetry of the object the
  cosmology *is*.** So the geometry's contribution to matter is **not a separate gift standing beside its
  cosmology — it is the cosmogenesis, read on its discrete structure instead of its continuous one.**
  P7's antimatter-progenitor theorem becomes **this boundary's first consequence**; P14's crest-origin and
  no-asymmetry-at-the-seam become **the residue behaving as what it is.** *"The two questions the corpus
  keeps apart — what conjugates matter, and what became of the collapsed universe — are questions about
  one map."*
- **Scope unchanged:** wall stands, gauge content and masses the ordinary route, `[6]`/factorisation
  asserted nowhere, held at **coherence not correspondence**.

## The five attacks — all mine, all at source, all within the hour of writing it

| # | what I wrote | what the source said | receipt |
|---|---|---|---|
| **1** | `R` **carries** the expansion leg onto the conjugate branch | **False.** A map is not a path, and the legs are not mirrors — **P7's own caption says so**. `R` **fixes** `r=0` and exchanges the *regions*. | `closure_iv_check.py` |
| **2** | *both faces of the conjugation* act on the bead | Presumed `[6*]`. The proposition now rests on (i)–(iv) **alone**; the proof says *"no step above uses it."* | — |
| **3** | *"the Feynman–Stückelberg particle↔antiparticle relation"* — **in three places** | **The departure `[6*]` exists to flag**, now done in a *paper*. By `sign r` both wings are `r<0`; the exchange moves nothing. Stripped: the word "Feynman" no longer appears in P13. | `[6*]` at source |
| **4** | the ruling-swap as one of `R`'s four faces | **Generic** — *"EVERY orientation-reversing isometry swaps them; what tells the reflections apart is their OTHER action."* **And the glossary cited `r_swap.py`, which does not exist** (it is `ruling_swaps.py`). | `ruling_swaps.py` |
| **5** | the negatives are one failure — *"an attempt to find `C` at the wrong level"* | **False, and self-inflicted twice.** `Q↦−Q` sits at **L3, precisely where `C` is** — right level, still not `C`. **And all three reasons I gave were the pre-weld ones**, re-dressed in level language, **one hour after I baked the weld myself.** | `closure_levels_check.py` |

**Every correction moved a claim OFF something unearned and ONTO something verified.** The synthesis was
right five times; the sentences describing it overshot five times. **A refuter could not have done this** —
it returns *refuted* or *uncertain* on the whole; the failures were all in the *describing*.

## New face: `CODA_FIELD_NOTE` **31** — the stale REASON under a surviving CLAIM
Attack 5's root, and it is a **new class**. Every existing staleness face is about a **claim** going
stale. This is a **reason** going stale under a claim that **survives** — *"`C ≠ R`" was true before the
weld and after it*, so a claim-level check returns clean, a compile returns clean, and the new vocabulary
made the dead reasons **read as current**. *"The weld was in the paper; the pre-weld reason was still in my
head; and the synthesis was written from the head."*
**The reach, and why it is logged before stage 8:** if a correction can fail to propagate into a document
written **an hour later, in the same session, by the instance that baked it**, then *"the corpus now says
X"* ≠ *"the corpus's **reasons** now say X"* — and **an enrichment sweep that checks claims would return
all-clean over a corpus full of dead becauses.** The r1063 null in a new costume.
**Guard:** *a surviving conclusion is not evidence that its support survived — it is exactly the
camouflage.* Before building on a corrected result, **pull the corrected REASON at source, not the claim**.

## New receipts (3; all re-run clean)
`closure_iv_check.py` · `closure_levels_check.py` · (plus `ruling_swaps.py` re-run and read, not cited
blind). **33 receipts total.**

## Corrections carried into the map
Glossary `R` entry: the **broken `r_swap.py` citation** fixed to `ruling_swaps.py`; the **ruling-swap face
marked GENERIC** with the receipt quoted verbatim; and the reading instruction that was missing — **read
the four faces as four things this one map does, NOT as four things that identify it**; only (i), (ii) and
the `r=0` fixed point do that.

## Attack 6 (r1089) — my own opening claim, and face 31 caught a THIRD time in the same paper

`sec:closure` opened: *"Each preceding section closes a route; **none of them turns round**."*
**False.** `sec:meaning` turns round — *"The boundary is not a setback to CR's gravitational claim; it
**sharpens** it"*, and it already unifies the wall with the corpus (*"the same completeness that locks the
cosmological constants … is what walls a continuous geometric colour"*).
**What it does not do is turn round *and go somewhere*: it turns OUTWARD** — handing the residue's
positive content to p0 as a conjecture, and resting on *"the bounded negative is itself a result."* It is.
**The gap was never "nobody turns round"; it was "the turn faces outward."** Corrected in the text, and it
reframes the pair correctly: **`sec:closure` does not precede `sec:meaning` — it supplies what
`sec:meaning` was reaching for.** `sec:meaning` said *"the present paper fixes **only** the perimeter
within which any such reach must live"*; the closure gives that *"only"* its content, and the word is now
gone.

**And `sec:meaning` was carrying the pre-r1088 residue clause** — *"the discrete orientation parity … **the
one residue it leaves**"* — which `rem:C-scope` had corrected **that morning, in the same paper**. **Face 31
for the third time in one day**: the correction went into the remark and did not propagate to the section
that summarises it. Fixed: *"the residue it leaves **at the level of the isometries** … **not the whole of
what it leaves**."*

**The count that matters:** face 31 has now fired **three times in one session** — stage 2→7 (the weld's
reasons), and twice inside P13 itself. It is not an incident. **A correction does not propagate; it must
be carried, and the carrying is a separate act from the correcting.**

## Standing / next
**Stage 8** (the fulsome enrichment) is the last stage, and **face 31 has just changed what it must be**:
a claim-level pass is structurally blind to a dead reason, exactly as a delta-spec pass was blind to a
perimeter defect. **Name what the sweep would have to test to see a dead *because* — or say it cannot.**
**And face 31's three firings have earned stage 8 a precondition:** before the enrichment pass runs, it
needs a way to see a **dead *because***. A claim-level pass cannot. Naming that instrument — or declaring
it unavailable and saying so — is stage 8's first task, not its last.
