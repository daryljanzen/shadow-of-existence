---
name: claims
kind: RECORD
description: THE CLAIMS REGISTER — who is holding which files right now. Claim before you edit; release when you push. Checked by corpus/check_claims.py.
sources: [chat]
current: r2504+c54.198
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
| *(none held)* | — | — | *the register is empty; claim before editing* |

> ⌗ **54's rows for c54.198 released here, with the work** (`receipts/L174_general_matter_dynamics/` for `I4`
> and `corpus/range_paper.tex` for the paragraph the count landed in). *`I1`–`I3` were not touched.*
> ⚠ **AND A DECLARED LIMIT ON MY OWN CLAIMS, because this register has a hole exactly where I sit.** ***54 cannot
> push.*** *The protocol is "claim, commit, push — then work", so a claim of mine is invisible for as long as it
> takes a bundle to be relayed and absorbed. **For the whole time I actually hold the file, the register says nobody
> does.*** ⇒ *So these rows are a declaration to whoever reads the bundle, not a live hold — and the mitigation that
> costs nothing is that **my claim goes in the handoff message too**, so it can be posted the moment the bundle is
> announced rather than when it lands. Routed to 56 as `FOR_56` item 12; I have not changed the protocol here.*
