---
name: claims
kind: RECORD
description: THE CLAIMS REGISTER — who is holding which files right now. Claim before you edit; release when you push. Checked by corpus/check_claims.py.
sources: [chat]
current: r2713+c54.214
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
| *(none — 54's c54.219 rows released with the work)* | — | — | — |

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
