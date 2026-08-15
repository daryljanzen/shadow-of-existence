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
> this register has, and the fix is to say so rather than to leave the row standing: `PO-6` is untouched by
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
