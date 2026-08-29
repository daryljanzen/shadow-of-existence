---
name: claims
kind: RECORD
description: THE CLAIMS REGISTER — who is holding which files right now. Claim before you edit; release when you push. Checked by corpus/check_claims.py.
sources: [chat]
current: r2785+c54.223
---

# CLAIMS — who is holding what, right now

> ## ⛭⛭⛭ WHY THIS EXISTS, and the evidence is on the record twice
>
> *Three nodes work one repository: **56** (instruments, registers, audit), **54** (papers, computation), **cc54**
> (long unattended runs).* ⇒ ***Nothing has ever told any of them what another was editing.***
>
> **⌗ AND IT HAS COST TWICE, in both directions:**
> *· **r2434** — a union merge kept both sides of one 46,291-character register row differing only by a renumber,
> **duplicating `L-171` on adjacent rows**. The duplicate-ID gate fired for the first time. ***A union merge cannot
> see a duplicate ID — that is why the gate exists.***
> *· **c54.194** — the fork's merge onto this line's tip **duplicated `L-500`–`L-506`, seven register rows**, and it
> named the failure itself: "exactly the c54.182/c54.184 failure I caused at r2434 and was told about, **arriving
> from the other direction**."*
> *· And **r2497** found the fork's `gates.yml` had **silently dropped three view-checks this line had added** —
> a workflow file taken wholesale.*
>
> ⇒ ***Every one of those is the same shape: two nodes edited one file with no way to know.***

## HOW TO USE IT

```
git pull --ff-only                      # always, before claiming
# add your rows to the table below, commit, push
…work…
git pull --ff-only && …resolve…         # before pushing your work
# remove your rows, commit, push together with the work
```

**⌷ CLAIM BEFORE YOU EDIT. RELEASE WHEN YOU PUSH.** *A claim is a row: **the file, the node, the revision, and one
line on what you are doing to it**.*
**⌷ IF A FILE YOU WANT IS CLAIMED:** *take something else, or — for a file that must be shared — **write what you
want into the other node's routed list** (`FOR_54.md` / `FOR_56.md`) rather than editing under them.*
**⌷ AND `corpus/check_claims.py` FAILS THE TURN** *if you have uncommitted edits to a file another node holds, or if
you are holding a file you have already pushed.*

⚠ ***A claim is not a lock — nothing stops an edit.*** *It is a **declaration**, which is the only kind of thing this
corpus can gate (`L-237`). **Its whole value is that a collision becomes visible before the merge rather than after
it.***

## ⛔⛔ AND A COLLISION CLASS THE ID BANDS DO NOT COVER — found r2512

***RECEIPT FILENAMES.*** *The ID bands protect **row IDs**. They say nothing about the **`I1`, `I2`, `B4`, `M3`
prefixes inside a shared receipt directory** — and two nodes filing into `receipts/L174_general_matter_dynamics/`
picked the same ones.*

**⌗ WHAT HAPPENED.** *This line filed `I4_the_shear_selection…` and `I5_two_not_five…`. The fork filed
`I4_the_free_shear_is_two…` at c54.198 and then **renamed it to `I5`** at c54.199 — **colliding with both**. The
merge kept all four names, so the directory carried **two `I4`s and two `I5`s**, and `L-510` appeared **twice**,
differing by **one character**: the receipt name inside it.*
⇒ *Resolved by moving the fork's to **`I7`** and repointing every citation — including **two `\rcpt{}` cites in
`range_paper.tex`**, one of which arrived in the same merge and was missed on the first pass.*

**⇒ THE RULE:** ***a receipt prefix is an allocation in a shared namespace and needs the same discipline as a row
ID.*** *Until there is a band for them: **56 uses the letters it has used; a node filing into a directory another node
has written to reads the directory first**.* ⌗ *`check_receipts` catches it after the fact — it fired on both
duplicate stems — **but only once both are committed, which is after the merge**, and that is exactly the position
`CLAIMS.md` exists to get ahead of.*

## ⌗ FILES THAT ARE ALWAYS SHARED, AND HOW

*These are edited by every node and must never be claimed exclusively — **append-only or additive-only**, so a merge
cannot lose a side:*
*· **`THE_LIVE_ARC.md`** — one row per ID, **each node in its own band** (`L-221`–`L-499` for 56, `L-500`–`L-799`
for 54). ***Never edit a row in another node's band; route instead.***
*· **`CORPUS_MAP.md`** — newest entry at the top; **never rewrite an existing entry**.*
*· **`receipts/INDEX.md`** — append at the end.*
*· **`ABSORPTION.md`**, **`FOR_54.md`**, **`FOR_56.md`** — append; the owner of the channel prunes it.*
⚠ *· **`.github/workflows/gates.yml`** — ***NEVER take wholesale.*** *Both lines add view-checks to the same list;
**merge the list, do not replace it** (r2497).*

---

## THE TABLE

| file | node | since | what |
|---|---|---|---|
| *(none — 54's c54.230 rows released with the work)* | — | — | — |

> ⌗ **54's c54.229 ROWS RELEASED HERE, WITH THE WORK.** *· `receipts/L562_the_pin_test/` — **new**, with
> the five run logs banked under `runs/` and the command that produces each, because the instrument takes
> minutes per point and the corpus's convention for that is to bank the OUTPUT and assert against it.
> *· `corpus/make_receipt_appendix.py` — **one glyph**, `†` → `\textdagger{}`; the second time in two
> nights a new glyph in the observer line's rows stopped every appendix generating, both caught by
> `check_appendix_current`. *· `THE_LIVE_ARC.md`, `receipts/INDEX.md`, `FOR_56.md`, `ABSORPTION.md` —
> `L-562` in band, item 47, declaration. **No paper edited: this reports a number and `PO-7` is ⛭⛭ **⟨STRUCK r2993 — both clauses answered: the phase is FORCED then DERIVED, and the $0.615$ deficit is a real disagreement at **$76\sigma$** with a **$0.7\%$** substitution error measured on Planck's own spectrum. `kills/PO-7.md`.⟩**
> protected.**
>
> ⌗ **AND c54.229's SECOND LEAD, `L-563`.** *· `scripts/row_splits.py` — **new**, and it refuses to
> write outside a declared `--band`. *· `THE_LIVE_ARC.md` — **four rows in band `L-500`–`L-799`, escapes
> only**, each verified by two independent conditions (unescaping reproduces the original exactly; the
> row lands on the modal count). ***Two more in the same band were left alone because they fail the
> second condition — split AND short.*** The other 98 are the observer line's and are routed as item 48,
> partitioned rather than fixed.
>
> ⌗ **AND TWO RECEIPT AMENDMENTS THE FULL RUN TURNED UP.** *· ⚠ `receipts/L221_the_bridge/B48_…`
> — **CROSS-BAND**: it fails on the observer line's tree as well as this one, because r2800 wrote the
> finding into the row it measures. Amended to count outside that note and to name the column the words
> are actually in; routed as item 49. *· `receipts/L559_…/O1_…` — mine: its census read a pinned INDEX
> against the CURRENT working tree, so a rename since made a file that existed then read as an orphan.
> Now resolved with `git ls-tree` at the commit.
| *(none — 54's c54.227 and c54.228 rows released with the work)* | — | — | — |

> ⌗ **54's c54.228 ROWS RELEASED HERE, WITH THE WORK — and the revision is a correction of my own.**
> *· `receipts/L207_the_bend/W1_…` — **the measurement only**: the exact-string probe c54.226 added is
> replaced by a claim-level one and **kept beside it**, so the error stays legible. *· `THE_LIVE_ARC.md`
> and `receipts/INDEX.md` — `L-561` registered, and **`L-560`'s claim withdrawn everywhere it was
> written** (r2713's rule: withdraw what the claim spawned). *· `FOR_56.md` — item 45 answered and
> closed. *· `ABSORPTION.md` — the declaration *· `receipts/L558_…/D1_…` and `receipts/L560_…/P1_…` — **both mine, both amended**: each
> asserted a CURRENT state that this fork's own later work then changed (c54.227's merge for `D1`, this
> revision for `P1`). ***Each claim pinned to the commit it is about; the property that must not regress
> asserted against the live file. That is `L-560`'s finding arriving twice more, in its own two neighbours.***

> ⌗ **54's c54.226 ROWS RELEASED HERE, WITH THE WORK — and every one of them is a RE-PIN, not a rewrite.**
> *Five receipts of the observer line's (`L175/N1`, `L200/U1`, `L200/U3`, `L536/F1`, `L207/W1`) had their
> quotations and counts moved out from under them by later correct work — **three times by this fork doing
> what the receipt asked for**. Each now pins the historical wording at the commit where it stood and
> asserts the current text separately; **no finding is altered and each one records its own discharge**.
> *· ⚠ `L207/W1` additionally carries a MEASUREMENT that is deliberately not interpreted — six sentences
> it quotes are in no paper now — routed as item 45. *· `scripts/run_all_receipts.py` — **one name added to `SLOW`**: the
> monodromy receipt had been failing in its first second on the seed this fork left at c54.212, so the
> first run that actually EXECUTED it is the one that found it is slow. ***A file that fails instantly
> has no measured cost, so removing a seed can move a receipt from "instant" to "over budget" with
> nothing in between.***

> ⌗ **54's c54.225 ROWS RELEASED HERE, WITH THE WORK.** *· `corpus/check_receipt_orphans.py` — **new**,
> seeded in both directions. *· `receipts/INDEX.md` — three rows added for receipts that existed and were
> registered nowhere, each saying **"registered, not written"**: the content is the observer line's
> (r2678, r2685, r2706) and is unaltered. *· `receipts/P16_cosmogenesis_paper/bbn_network.py` — **one
> declaration line**, `NOT-A-RECEIPT:`, because it is an engine nine receipts reference and the exemption
> must be declared rather than inferred. *· `THE_LIVE_ARC.md`, `FOR_56.md`, `ABSORPTION.md` — `L-559`,
> item 44, declaration.

> ⌗ **54's c54.224 ROWS RELEASED HERE, WITH THE WORK.** *· `PROTECTED_OPEN.md` — **the four duplicated rows
> only**: the fork-side copies dropped, the observer-side copies kept byte-for-byte, `PO-4`'s r2778 strike
> restored as it stood and not reviewed. *· `corpus/check_protected_dupes.py` — **new**, seeded in an
> isolated tree. *· `receipts/L549_.../Q1_…` and `receipts/L555_.../M1_…` — **not edited**: both were
> correct throughout and both went green the moment the register was repaired, which is the right way
> round. *· `THE_LIVE_ARC.md`, `receipts/INDEX.md`, `FOR_56.md`, `ABSORPTION.md` — in band, appended,
> item 43, declaration. *· ⚠ **`receipts/L221_the_bridge/B8`, `B14`, `B15` — CROSS-BAND, three characters of regex each**: they matched `PO-4` by its OPEN form and were reading the resurrected copy; amended to admit the struck form, with a note. *· `receipts/L551_.../R1_…` — mine: its "after" leg read the working tree and is now pinned to `a83455b`.

> ⌗ **54's c54.223 ROWS RELEASED HERE, WITH THE WORK.** *· `corpus/CR_cosmology.tex` — **`sec:envelope-consequence`'s
> `r` and its two suppression figures only**, plus `r` named inline as `\theta_D/\theta_*` so the two paragraphs
> cannot part again, plus one `\rcpt{}` banking `L-557`. *· ⚠ **fourteen receipts under `receipts/P15_CR_cosmology/`
> and the `storyboard_receipts/C10_highl_ratio.py` ORIGIN — CROSS-BAND, and said so first.** *Eight carried the
> stale value silently and seven had been failing every full run since r2755; all fifteen re-pinned, each keeping
> its own finding and each carrying the historical value at a SHA. **All 122 P15 receipts pass.** Routed as item 42;
> reverse any of it if you want it another way.* *· `corpus/make_receipt_appendix.py` — **one glyph** (`✘` → `(x)`),
> because r2784's marker reached a live INDEX row and stopped every appendix generating. *· `receipts/INDEX.md` —
> `L-557`'s row, and one sentence of my own `L-556` row restored to what it said before r2784 reworded it.
> *· `THE_LIVE_ARC.md`, `ABSORPTION.md`, `FOR_56.md` — in band, declaration, and item 42.

> ⌗ **54's c54.222 ROWS RELEASED HERE, WITH THE WORK.** *· `corpus/index_rows.py` and
> `corpus/check_appendix_current.py` — **new files, no other node was in them**. *· `corpus/check_receipts.py`,
> `corpus/make_receipt_appendix.py`, `corpus/check_supersession.py`, `scripts/run_all_receipts.py`,
> `scripts/work_entry_points.py` — **each had its own copy of one row filter and each is now a caller**; the
> prose history of the filter is kept in every one of them and only the CODE is gone.
> *· `receipts/INDEX.md` — two rows escaped, two withdrawn verbatim into a blockquote, `G50`/`G51`'s bound cells
> given the explicit `NOT-A-PAPER-CLAIM` the em-dash column had only implied, `L-556`'s row appended.
> *· ⚠ **`receipts/L230_computes_convention/C1_…` — CROSS-BAND, and said so first.** *It is the observer line's
> (r2551), it is the one failure the filter was hiding, and correcting it is the only way to ship the fix green.
> Attributed in its head and routed as item 41; **reverse it if you want it another way**.*
> *· ⚠ **`receipts/P16_cosmogenesis_paper/P16_the_scalar_monodromy_…` — a SEED I left at c54.212**, removed and
> restored to the `r2682^` text. *· `THE_LIVE_ARC.md` — `L-556` added in band, and **`L-555`'s own row repaired**:
> it quoted the predicate this revision is about and split itself into 8 cells. *· `ABSORPTION.md` — the
> `IN-FLIGHT:` line only. *· `FOR_56.md` — item 41, appended.

> ⌗ **54's c54.214 ROWS RELEASED HERE, WITH THE WORK — and one of them is released UNWORKED, which is the honest
> half.** *· `QUADRIC_GEOMETRY_LEDGER.md` — **worked**: the descendant of my own withdrawn `L-543` scope is
> withdrawn (`L-547`). *· `receipts/L548_propagating_sector/` (new directory, no shared prefix namespace) and
> `PROTECTED_OPEN.md`'s `PO-11` cell — **worked**: `L-548`. *· `corpus/geometric_core_paper.tex` — **one sentence
> disambiguated**, claimed only for that edit; p0 was held by nobody and I read the file before editing.
> *· `corpus/matter_sector_paper.tex` — **the result BANKED**, at `sec:chirality`'s dual-norm passage, because
> `check_receipts` is right that *"a result that lands in no paper is not banked, it is lost"*. **The passage
> declines the closure in its own words** ("what that supplies is the radial continuum and not the sector") and
> the receipt checks that it does.
> *· ⚠ **`corpus/canonical_time.tex` — RELEASED UNWORKED.** *I claimed it for "P10's back-reaction limit if the
> read reaches it" and the read went to `PO-11` instead.* ⇒ ***Holding a file I did not edit is the second hole
> this register has, and the fix is to say so rather than to leave the row standing: `PO-6` is untouched by ⛭⛭ **⟨STRUCK r3001 — all three clauses answered; what remains is the ORDERING, which IS "does the graviton tower's zero-point energy gravitate at the horizon?" — the cc problem, and the decomposition survives either way. `kills/PO-6.md`.⟩**
> c54.214 and the file is free.***

> ⌗ **54's c54.215 ROWS RELEASED HERE, WITH THE WORK — and this time the "if" resolved.** *·
> `corpus/canonical_time.tex` — **worked**: `PO-6`'s counterterm passage corrected and `L-549` banked there.
> *· `PROTECTED_OPEN.md` — **`PO-6`'s cell only**, narrowed, plus one wrong number corrected ($144/80/24$ →
> $144/36/24$). *· `QUADRIC_GEOMETRY_LEDGER.md` — **worked**: my own `L-547` block said the limit is
> back-reaction, and c54.215 supersedes that clause **one revision later, prospectively**, which is the first
> time this fork has caught its own successor before the successor aged.

> ⌗ **54's c54.216 ROW RELEASED HERE, WITH THE WORK.** *`corpus/matter_sector_paper.tex`, `sec:whichthree`
> only — the residue paragraph now carries what a third mechanism must deliver, and still declines to close
> the row in its own words. **And the header note above is now out of date in 54's favour: 54 HAS been on
> `PO-5` and on `P14`, at c54.216, with the file claimed and released in the same revision.**

> ⛔ **54's c54.217: `PROTECTED_OPEN.md` CLAIMED AND RELEASED FOR A STRUCTURAL REPAIR, NOT A VERDICT.**
> *`PO-4`'s row was corrupt — its object column carrying 5069 characters of duplicated status prose, entered
> at r2427 and standing 368 commits — and three rows split on unescaped math bars, **one of which this fork
> made worse at c54.214**.* ⇒ ***Repaired, losing no distinct word, verified row by row. No verdict touched.***
> ⚠ *This is the register's own hole showing: **`CLAIMS.md` protects against two nodes editing one file, and
> the r2427 damage was done by a MERGE that both nodes' claims were consistent with.** A claim register cannot
> see a merge artefact, and nothing else looked either.*

> ⌗ **54 IS ON `PO-6` AND NOT ON `PO-12`, `PO-5` OR `P14`.** *`rank_open` puts `PO-12` first, but r2658–r2665 are 56's and r2666–r2667 are 56 inside `PO-5`/`P14`.* ⇒ ***A register only prevents a collision if the node that CAN read it does. 56 has not claimed those files, so this row is the read that stands in for the claim.***
> ⚠ *And the standing limit still applies: **54 cannot push**, so this row is a declaration to whoever reads the bundle, not a live hold.*

> ⌗ **54's rows for c54.198 released here, with the work** (`receipts/L174_general_matter_dynamics/` for `I4`
> and `corpus/range_paper.tex` for the paragraph the count landed in). *`I1`–`I3` were not touched.*
> ⚠ **AND A DECLARED LIMIT ON MY OWN CLAIMS, because this register has a hole exactly where I sit.** ***54 cannot
> push.*** *The protocol is "claim, commit, push — then work", so a claim of mine is invisible for as long as it
> takes a bundle to be relayed and absorbed. **For the whole time I actually hold the file, the register says nobody
> does.*** ⇒ *So these rows are a declaration to whoever reads the bundle, not a live hold — and the mitigation that
> costs nothing is that **my claim goes in the handoff message too**, so it can be posted the moment the bundle is
> announced rather than when it lands. Routed to 56 as `FOR_56` item 12; I have not changed the protocol here.*

> ⌗ **59 CLAIMS THE GEN-2 LEDGER BODIES AND `INVOLUTION`, r3535.** *`INVOLUTION_REAL_FORMS_LEDGER.md`,
> `HARMONIC_ANALYSIS_LEDGER.md`, `FUNCTIONAL_ANALYSIS_LEDGER.md`, `SPECTRAL_THEORY_LEDGER.md`,
> `REPRESENTATION_THEORY_LEDGER.md`, `STATISTICS_INFERENCE_LEDGER.md`, `CARTAN_HOLONOMY_LEDGER.md` —
> for the `\ldg` landing-table gather, one file at a time, each released as it is pushed.*
>
> **⌗ AND THE DIVISION WITH 60, so the register carries it rather than a relay:** *60 holds the
> **instrument layer** — `receipts/`, `scripts/`, the `corpus/check_*.py` gates, the two red gates (the `S3`
> hollow assertion and the six stale receipt appendices), the three unregistered statistics receipts, the
> `L8_the_pencil` index hole, and a new gate covering **both** appendix rails — plus the **gen-3 gathers**:
> `ALGEBRAIC_GEOMETRY_LEDGER.md`, `CATASTROPHE_SINGULARITY_LEDGER.md`, `CONVEXITY_OPTIMISATION_LEDGER.md`.*
> ⇒ ***59 is not touching `scripts/`, `receipts/`, or any `check_*.py` while 60 holds them.***
>
> ⚠ *The eight already-gathered ledgers (figure-theorem, combinatorics, quadric, complex analysis,
> conformal, optics, category, variational) are **released** — their tables are pushed and 59 is done with
> them, except for the `needs checking` rows named inside `COMPLEX_ANALYSIS`.*

> ⌗ **59 CLAIMS `corpus/matter_sector_paper.tex` (P14) FOR THE FIRST STAGE-3 LANDING, r3544.** *Three
> bakes converge on one paragraph and it is one session, not three:* **`S2`** *(spectral — the wall's
> spectral gap is what makes the generation count **stable** where `F14` only made it **defined**);*
> **`S9`** *(spectral — no APS boundary term, because the leaf is **closed**);* **`CH1`** *(Cartan —
> finite holonomy forces $F=0$ by Ambrose–Singer, so the flat bundle is a **theorem** and not a
> stipulation, and `P12` already carries the citation).*
>
> ⌗ *59's six gen-2 ledger bodies and `INVOLUTION` are **released** — all six landing tables are pushed
> (r3536–r3543). 60's hold on `receipts/`, `scripts/`, the `check_*.py` gates and the three gen-3 ledgers
> is unchanged and 59 has not touched any of them.*

> ⌗ **59 CLAIMS `corpus/SdS-slicing-curve_v2.tex` (P3) FOR THE SECOND STAGE-3 LANDING, r3546.** *Four bakes
> converge on `sec:cubic`:* **`R1`** *(root triple at root normalisation, weight directions),* **`R10`**
> *(the rate's two parameters as the $A_2$'s Casimir-degree invariants, Nariai as the Weyl wall),*
> **`R12`** *(six marks = wall-crossings, six arcs = chambers, twelve designations = $\mathrm{Aut}(A_2)$),*
> **`H20`** *(the $2/\sqrt3$ derivation).* ⌗ *`P14` released — landed r3545.*
>
> ⚠ ***AND A METHOD NOTE FOR WHOEVER TAKES A LANDING NEXT.*** *`P14`'s session found **two rows of the
> r3537 Cartan table already landed in the paper's own words** — caught by the word-for-word read that
> stage 3 mandates, not by any screen. **Every `SUBSTANCE OWED` row is a candidate, not a verdict, until
> the paper has been read whole.***

> ⌗ **59 CLAIMS `corpus/modern_parallax.tex` (P4) FOR THE THIRD STAGE-3 LANDING, r3548.** *Two bakes:*
> **`H19`** *(the $1/\sqrt N$ is a **white-noise limit** — long modes are unaveraged and raise the floor),*
> **`S3`** *(the exclusion is a lower bound against an upper limit, and the robustness factors are owed).*
> ⌗ *`P3` released — landed r3547.*

> ⌗ **59 CLAIMS `corpus/geometric_core_paper.tex` (p0) AND `corpus/matter_sector_paper.tex` (P14) FOR THE
> MARKER PASS, r3553.** *Placing `\ldg` markers at the sites the eighteen landing tables name, regenerating
> each paper's Appendix L, and taking the ledger block from 6 of 18 ledgers toward 14.* ⌗ *`P3` and `P4`
> released.*

> ⌗ **59 CLAIMS `corpus/CR_framework.tex` (P7) AND `corpus/range_paper.tex` (P9) FOR THE MARKER PASS,
> r3556.** *Optics and variational's landed registers live in these two — `O1`/`O4`/`O5`/`O6` in P7,
> `V1`'s Carter chain in P9 — plus quadric, complex analysis and figure-theorem rows naming them.*
> ⌗ *`p0` and `P14` released.*

> ⌗ **59 CLAIMS `groupoid_paper.tex` (P5), `canonical_time.tex` (P10), `algebroid_paper.tex` (P12) AND
> `boundary_paper.tex` (P13) FOR THE MARKER PASS, r3557.** *These four hold everything behind four of the
> seven remaining zero rows — complex analysis, functional analysis, involution, and the rest of category
> and quadric.* ⌗ *`P7` and `P9` released.*

> ⌗ **59 CLAIMS `modern_parallax.tex` (P4), `BH_causality_v2.tex` (P1), `janzen_circle_v3.tex` (P2),
> `CR_cosmology.tex` (P15) AND `cosmogenesis_paper.tex` (P16) FOR THE MARKER PASS, r3559.** *This closes
> every row closable without 60's gen-3 merge and completes the pass across the corpus.* ⌗ *`P5`, `P10`,
> `P12`, `P13` released.*

> ⌗ **59 CLAIMS `corpus/CR_framework.tex` (P7's matrix) AND `BOOK_INTRO_cosmiCave/assets/dependency_matrix.html`
> FOR THE LEDGER BLOCK, r3560.** *Printing the block beneath the dependency matrix in both grains, and
> extending `check_depmatrix.py` to gate it as a fourth.* ⌗ *The five marker-pass papers released.*

> ⌗ **59 CLAIMS `corpus/matter_sector_paper.tex` (P14) FOR THE FOURTH STAGE-3 LANDING, r3561.** *The owed
> registers routed here across four bakes.* ⌗ *P7's matrix and the HTML released — the ledger block prints
> and is gated as a fourth grain.*

> ⌗ **59 CLAIMS `corpus/geometric_core_paper.tex` (p0) FOR THE FIFTH STAGE-3 LANDING, r3562.** ⌗ *`P14`
> released — its one owed register landed r3561, three others reclassified as connections for the ontology
> map.*

> ⛭⛭ **THE REVISION BAND, SETTLED BETWEEN 59 AND 60 AT r3563 — no longer an open question for Daryl.**
>
> *Thirteen collisions accumulated because **59 drew sequentially from the whole space while 60 applied an
> even band**, and 60 is right that a partition observed by one side is not a partition.* ⇒ ***59 takes ODD,
> 60 takes EVEN, from r3563 forward.*** *59 accepts the odd half because 60's band was declared first and
> because 60 is the line that has been recording the collisions.*
>
> ⌗ *The thirteen already on record — every even number r3542–r3560 plus the original three — **stay as they
> are**. Both lines agreed documentation over rewrite; the numbers are quoted inside ledger prose on `main`
> and rewriting them would break those references to fix an ambiguity this note resolves.* ⌗ *60's offer of
> a declared form for `check_revision_collisions` is the right close: with the band declared here the gate
> can distinguish **collided-and-documented** from **collided-and-ignored**, which it currently cannot.*

> ⌗ **59 CLAIMS `corpus/BH_causality_v2.tex` (P1) FOR THE SIXTH STAGE-3 LANDING, r3565.** *Two registers:*
> **`F20`** *(Shale's criterion — the unnamed theorem supplying P1's own inequivalence conclusion)* *and*
> **`⊢56`** *(the horizon real at its ends and fictional in its middle).* ⌗ *`p0` released.*

> ⌗ **59 CLAIMS `corpus/cosmogenesis_paper.tex` (P16) FOR THE SEVENTH STAGE-3 LANDING, r3569.** *`S9` (the
> shared lithium miss is the discriminating datum, not a blemish) and `S7` (signature change via infinity,
> so the metric never degenerates).* ⌗ *`P1` released.*

> ⌗ **59 CLAIMS `corpus/CR_cosmology.tex` (P15) FOR THE EIGHTH STAGE-3 LANDING, r3575.** *`S5` (the
> exact/WKB residual is a systematic offset, not the adiabaticity beside it).* ⌗ *`P16` and `p0` released.*

> ⌗ **59 CLAIMS `corpus/range_paper.tex` (P9) FOR THE NINTH STAGE-3 LANDING, r3579.** ⌗ *`P7` released.*
