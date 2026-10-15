# The register census: what the eighteen papers say is open, against what the register says is open

*Node 69, at Daryl's direction. The register is meant to hold every open problem the papers state, so
that what it lists as open is exactly what the papers list as open. This census checks that, in both
directions.*

## How it was done

- **Every paper read at its open statements.** `extract.py` pulls every paragraph of the eighteen
  published papers (P1 to P18, the live edition's own list in `scripts/gen_live_edition.py`) that
  carries a marker of something unfinished: "open", "not yet", "owed", "not settled", "conjecture",
  "frontier", "what would", and about forty more.
  - It found 257 paragraphs, and every one was read in full.
  - The reading of each is in `items.tsv`: the paragraph number, the paper, a class, the topic, the
    register rows it touches, and a note.
  - The classes are: `OPEN`, `CHECK` (open in one paper and placed as a boundary in another),
    `POINTER` (the paper hands the item to a companion), `NOT-OPEN`, `DECLARED-NOT-OWED` and `STALE`.
- **Every register row read at its state.** `THE_REGISTER.md` holds rows `PO-10` to `PO-85`. Two are
  open: `PO-50` and `PO-78`. `THE_FRONTIER.md` is generated from those two rows, and it is what the
  live edition's frontier page shows the public.
- **The limit of the method.** A paper that states something open without any of the marker words
  would be missed. Every paper's own frontier or open-problems section was reached through its marker
  hits and read whole, so the risk sits in body prose, not in the sections that list what is open.

## The headline

**The register's open list and the papers' open list have almost nothing in common.**

- The public frontier page shows two open rows. `PO-78` is the quote-pin cleanup, which is
  infrastructure and not a paper item. `PO-50` is the turnaround-mass measurement.
- The synthesis paper P18 states its own frontier as "complete and unfiltered": seven open items, in a
  table at its §frontier. **One of the seven has a live register row (`PO-50`). The other six have
  rows that are struck.**
- Across all eighteen papers there are **29 distinct open items**. The table below gives every one of
  them, merged across papers.
  - **Struck row:** 11 of the 29 are stated open in the papers while every register row that touched
    them is struck.
  - **No row at all:** 17 have never had a register row.
  - **Live row:** 1, `PO-50`, is carried by a live row.
- **Eleven places where the papers contradict each other** about whether something is open. These are
  one-state failures in the published corpus, and they are listed after the table.

The struck-but-open cases need care. A strike is meant to rest on a receipted answer, so in each case
**either the paper is stale** (the row was answered and the paper still says open) **or the row was
struck too early** (the paper is right). The census does not decide which. The table gives each
strike's own ground, so the person who works the item can see which side to read first.

## The open items, merged across papers

*A code in the "register" column is a row of `THE_REGISTER.md`. "struck rNNNN" gives the revision at
which it was struck and, briefly, the ground the strike gave.*

### Stated open in the papers; every register row that touched it is struck

| # | the open item, in the papers' words | stated open in | register |
|---|---|---|---|
| 1 | **The acoustic peak structure.** The full-spectrum likelihood rejects the computed spectrum on its shape, and "a mechanism for that deficit is what the cosmology names as owed". P18 calls it "the largest open item". Its parts: what sets this arm's first peak (P18); what displaces the fourth peak (P7); what distinguishes the first acoustic cycle from the rest; the carrier of the contrast excess, "not attributable from here"; the running phase at correct spacing, driving or baryon loading, "named rather than measured"; separating the driving from a reparametrisation of its clock, "located rather than built"; the observed residual's own position on the component plane | P6, P7, P15, P18 | `PO-10` struck r6799 (refit run like-for-like); `PO-47` struck r6877 (stopping rule: the sky cannot tell the two models apart at the fourth peak); `PO-56` struck r7037 (the accounting closes and cannot attribute); `PO-70` struck r7201 (the distance identification answered structurally) |
| 2 | **Whether the damping-tail displacement of the inferred tilt is a tension.** It needs a constraint on $n_s$ that does not run through the damping tail | P6, P15, P18 (frontier item 7) | `PO-24` struck r6801 ("almost nothing left to weigh") |
| 3 | **The progenitor spectrum.** $A_s$ and $n_s$ come from a progenitor interior not yet modelled: "a modelling task awaiting a progenitor interior", reaching the head of a bounded genealogy | P15, P16, P18 (frontier item 4) | `PO-31` struck: its strike text says "neither is owed and neither is an open problem" |
| 4 | **The matter content's generative law.** The continuous half is not settled: a principle selecting a matter profile, and whether masses and mixings can follow. P14 says what remains "genuinely outstanding" is "the gauge group and the multiplet structure", with the bundle question (what the wall operator acts on, and what fixes it) and an account owed of the matter-to-baryon energy ratio at the onset | P7, P8, P13, P14, P17, P18 (frontier item 2) | `PO-30` struck r6758 ("the geometry supplies no choices"); `PO-26` struck r6463 |
| 5 | **Where a generation's colourless triple sits; the fifth multiplet.** The horn orbits are 2+2 where the Standard Model is 2+1+1, "delivered on neither member": "what a successor must supply" | P14, P18 (frontier item 1) | `PO-45` struck r6733 ("each part of the answer is receipted") |
| 6 | **The charged collapse and the Cauchy horizon.** More widely, the irreducible interior reassignments, Kerr-inner and Reissner–Nordström-interior: "what stays open there is the interior reassignment". P18's list carries the charged case and not Kerr-inner | P3 (its "Open" paragraph), P5, P7, P9, P18 (frontier item 6) | `PO-25` struck r6843; `PO-49` struck r6913 |
| 7 | **The ultraviolet definition of the interacting graviton tower.** The paper's words are "the one open thing". Its parts: the renormalised value at the paying dimension, unclaimed; the invariant at that dimension, unnamed; the quartic's derivative sector, not computed; the level-summed cubic sign, not claimed; the nine-level closed forms fitted, not proved; "the interacting theory is not built" | P10, P11, P18 (in its body, not its list) | `PO-23` struck r7077 ("the sums are defined by the construction's own regulator"); `PO-71` struck. **P7 says all of it is settled**: contradiction C1 |
| 8 | **The detailed worldline and field dynamics of matter crossing the branch point**, for a concrete matter model: "what remains open" | P1, P5, P15 | `PO-30` struck. **P7 says the crossing "is settled on the field side and on the worldline side"**: contradiction C2 |
| 9 | **Which exponent the imaginary segment's own field obeys**: $\omega=kc_s$, or the substrate field with no sound speed, differing by $\sqrt3$, "remains open". With it, which branch the freezing census should be run on | P15 | `PO-79` struck r7145 ("the crossing transports the species the vacuum curve supports") |
| 10 | **The source of the anisotropic spectrum on the expansion leg**: "named here as owed and developed in neither this paper nor the bead" | P15 | `PO-75` struck r7243 ("a stated limit and not an order") |
| 11 | **The chiral content.** The asymmetric action is permitted on the chiral member and not selected: "the open work is narrowed to the chiral content" | P7, P12, P17 | `PO-14`, `PO-45` struck. **P18 places it as the ordinary route, a decline and not an open item**: contradiction C8 |

### Stated open in the papers; no register row has ever carried it

| # | the open item | stated open in |
|---|---|---|
| 12 | **Dark matter.** The cosmology carries the matter density "without yet removing the component or answering its particle question; that column stands at full weight" | P15 |
| 13 | **The last-percent precision of the light-element abundances** against measurement, on the specially evaluated nuclear rates. "The open edge" in P15, P16's body and P17; **"closed rather than open" in P16's own abstract** (contradiction C4) | P15, P16, P17 |
| 14 | **The exact regulated peak temperature** through the branch point, "downstream-irrelevant"; and the thermalisation that sets the floor, "argued, not computed exactly" | P16 |
| 15 | **The unification thesis**: the substrate's maximal symmetry as one fact behind seven separately established results. It is held as "a conjecture decidable by a named test"; the test is run on both sides and has not falsified it | P6, P7, P12, P17, P18 |
| 16 | **The base rate of the criterion of necessity.** The cases where the same criteria misled "have not been sampled and no base rate has been computed"; it is set as the discipline's first programme (`THE_BASE_RATE.md` exists) | P6, P18 |
| 17 | **Whether the two real forms are physics' actual quantum and gauge sectors**, not a structural rhyme with them: "an open question ... with a stated blocker", the discriminator being dynamics. With it, whether the conjugate-form $\mathfrak{su}(3)$ is the physical colour, and whether the geometric $A_2$ and colour's coincide for a structural reason. The explainer's "whether that shared root runs deeper, into the forces themselves" is this item | P3, P13, P18, the explainer. **P5's remark `rem:a2-distinct` answers the $A_2$ half** (an analytic connection through the common complexification): contradiction C7 |
| 18 | **A third mechanism**, neither holonomy nor isometry, that could supply a colour coupling: "naming one remains open" | P14 |
| 19 | **Whether any substrate bundle furnishes the Standard Model's group action**: the five-dimensional tangent bundle, the spinor bundles, the wall's normal bundle, the ruling bundles. "We have not examined ... we do not claim the question is closed"; "the remaining candidates ... are untouched here" | P14 |
| 20 | **Whether the root triple and the causal-value triple $f\in\{0,1,2\}$ are one structure**: "held open"; no single-condition derivation has been exhibited | P2, P7 |
| 21 | **Whether the $Q\mapsto-Q$ $\mathbb{Z}_2$ is the source of a distinction between complementary readings**: "noted and not claimed; testing it is not this paper's work" | P3 |
| 22 | **Whether the involution and the sky-angle periodicity generate the full discrete vantage structure**: "we have not done" the classification | P3 |
| 23 | **The deformation invariance of the graded generation index on the branched bead**: the Atiyah–Singer statement is "traced rather than computed". The count itself is computed | P14 |
| 24 | **Whether the progenitor's angular momentum is carried off by matter or torqued away**: "this paper does not settle" | P15 |
| 25 | **Instrument limits on the acoustic comparison**: the polarisation source's pull "has not been measured"; whether the first three peaks locate to one multipole "is not settled"; the smaller gap contractions at low $\ell$ are below the grid | P15 |
| 26 | **Whether the reversal of determination extends from the rate to the scale**: "not settled by the measurement". P4 says P7 takes it up; a search of P7 found no statement settling it, so this needs a reading of P7 | P4, P18 |
| 27 | **The ultraviolet regime of the late-time collapsing surface**: "not settled here ... the companion papers are where the question has its home". P15 and P11 carry no such item, so the pointer lands nowhere | P1 |
| 28 | **Whether a child universe necessarily lives in its parent's cosmological constant**: "one of the open questions". It is found in the explainer only, not in any paper or row. **It is the explainer's, and this seat's to resolve**: either the papers state it, or the explainer's sentence is wrong | the explainer |

### Stated open in the papers, and carried by a live row

| # | the open item | stated open in | register |
|---|---|---|---|
| 29 | **Which mass the Hubble–Eddington radius tracks**: measured against independently measured baryonic or turnaround mass | P18 (frontier item 5) | `PO-50` **open** |

### Stated as not settled, and placed by the papers as a boundary rather than an open item

*Listed so that nothing falls out by reclassification. The papers place each of these where it is
fixed, or why it cannot be.*
- the operator ordering of the graviton tower (external: whether vacuum energy gravitates);
- the field-level charge structure;
- the gauge representations and the mass spectrum (the ordinary route; electroweak);
- the compact-face fermion sector (obstructed twice);
- the seam's flux (no state is selected: one locus carries two surface gravities);
- a closed-form nonlinear solution (not needed for the verdict);
- an evidence comparison over the larger model family (turns on priors, named and not run);
- lithium-7 (the standard theory's open problem, shared).

## The papers against each other

These are places where two papers, or one paper with itself, disagree about whether the same thing is
open. Each is a one-state failure in the published corpus.

| | the disagreement |
|---|---|
| C1 | **The interacting tower's UV definition.** P7 §frontiers: "all three are settled, the ultraviolet definition of the mode sums with them". P10: "the one open thing is the ultraviolet definition". P11 says P7 "carries [it] as an open problem of the programme". P18's body calls it open; P18's list of seven omits it. The register (`PO-23`, struck r7077) agrees with P7 |
| C2 | **The matter crossing.** P7: "settled on the field side and on the worldline side". P15: "what remains open is the detailed worldline and field dynamics of the crossing for a concrete matter model"; P1 and P5 say the same |
| C3 | **Deriving the inherited data, $\eta$ and $\rho_r/\rho_m$.** P7 calls it "what would go beyond" and a frontier. P15 lists it among what "remain to be built". P16's abstract, P17 §frontiers and P18 say it is closed by impossibility. P16's own body says it "sharpens the frontier" |
| C4 | **The last-percent abundance precision.** P16's abstract lists it as "closed rather than open"; P16's body, P15 and P17 call it the open edge |
| C5 | **The acoustic assignment.** P15 at its acoustic comparison: "what is open is whether that assignment is right". P15 at its §scope: the distance assignment is settled "constitutively". P18: "whether ... the wavenumber sum is not yet carried far enough"; P15 §scope says the retention "is not an artefact of how the integral is carried" |
| C6 | **Which peak.** P7: "what is open is what displaces the fourth peak". P18's list: "what sets this arm's first peak". `PO-47` (the fourth peak) was struck because the sky cannot tell the models apart there |
| C7 | **The $A_2$ coincidence.** P5 `rem:a2-distinct` answers it: an analytic connection through the common complexification. P17's tour and P18 say it is "left open" |
| C8 | **The chiral content.** P7: "the open work is narrowed to the chiral content". P18: the chiral content "remains the ordinary route", a decline |
| C9 | **P18's "complete and unfiltered" seven** omits open items P18 itself states elsewhere (the tower; the unification conjecture, which it holds open in a separate section; the base rate) and items other papers state (dark matter, the segment exponent, the anisotropic source, the abundance precision, the two-real-forms identification) |
| C10 | **P18 §displace** refers to "the sixteenth Weyl fermion of §frontier"; the frontier does not carry it (`PO-37` struck r4237) |
| C11 | **P15** says the acoustic section leaves "one bounded calculation outstanding that could still bear on it (§scope)"; §scope names none |

## The other direction: open register rows against the papers

| row | in the papers? |
|---|---|
| `PO-50` | Yes. It is P18's frontier item 5, worded there as which mass the radius tracks, and in the row as the turnaround-mass measurement. Consistent |
| `PO-78` | Not a paper item. It is the quote-pin cleanup, an infrastructure row, which the register also carries. Consistent |

No open register row is unknown to the papers. The failure runs one way: the papers carry open items
that the register has struck or never held.

## What it means for the published frontier

The live edition's frontier page reads `THE_FRONTIER.md`, which is generated from the register's live
rows. **A reader of the published book is told the programme has two open problems, one of them
infrastructure.** The papers on the same site state 29, and the synthesis paper's own count is seven.
Bringing the register up to the papers is what makes the published frontier say what the papers say.

## What the census does not do

- It does not decide, for the eleven struck-but-open items, whether the paper or the strike is right.
- It does not write the missing rows. Writing them is the coordinating node's job.
- It does not repair the eleven contradictions. Each is a rewrite of a paper to one state, and is
  owed to the paper's owner.
