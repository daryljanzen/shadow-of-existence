---
name: the-front-edge
kind: METHOD
current: r2596+c54.207
description: THE FRONT EDGE — how the corpus and the residual register stay current with each other AS work is done. The closure protocol, the gates that enforce it, and the work that remains to make it complete. Written r2596.
sources: [chat]
---

## ⛔ NEVER ASSERT AN ABSENCE YOU ARE ABOUT TO END — r2672

*A receipt written in the turn that changes the corpus must assert the state it **LEAVES**, not the state
it **found**.*

⇒ ***Otherwise it is green exactly once — at the moment it can least be trusted — and red for every
revision after.***

**THE MEASUREMENT.** *Of 40 receipts this line wrote in `r2626`–`r2671`, **8 failed**, and every one had
the same shape:*

    check('⛔ and the PO-5 row does not mention $SU(3)$ at all',  'SU(3)' not in row)
                                                    ↑ and the same turn put it there

*Two more asserted a ledger BUCKET LABEL — `DISCOVERABLE-PROOF`, `OPEN-DOWNSTREAM` — that this line's own
later revisions retired. **Same shape, one level up.***

**⇒ THE FORM THAT SURVIVES:**

    check('✔ and NOW the PO-5 row carries the delivery (this receipt put it there)', 'SU(3)' in row)

⌗ *All ten converted at r2672; **40 of 40 pass**. And the defect was invisible for as long as the receipt
runner was — `scripts/queue.py` shadowed the stdlib `queue` from r2615 to r2670, which 54 found.*


# THE FRONT EDGE

> ***One operable surface where the corpus and the register are both current, and closing an item updates
> both.***
>
> ⌗ *All the pieces exist. What was missing is the PROTOCOL that binds them — and a name for the failure
> it prevents: **an item advertised as owed in the papers after the work that closed it was done**.*

---

# I · THE FIVE INSTRUMENTS, AND WHAT EACH GUARANTEES

| instrument | guarantee |
|---|---|
| **`corpus/open_ledger.txt`** | ***every epistemic qualification in the papers has a VERDICT***, with its reasoning, so no reading is done twice |
| **`check_open_ledger`** | ***a new qualification cannot appear without being verdicted***; `--rebuild` preserves existing verdicts, so verdicting is the only direction the file moves |
| **`check_revleak`** | ***the working record cannot enter the published text***; grandfathered at 29, and the baseline only falls |
| **`check_provenance`** | ***a `%` comment cannot become a quotation***; population zero, and it forbids the path that was walked once |
| **`PROTECTED_OPEN` + `kills/` + `F5`** | ***an open question cannot be closed by a node***; route ② writes four checks and the register's own line authorises |

⇒ ***Between them: what is open is listed, what is claimed is sourced, what is closed was authorised, and
the working record stays out of the papers.***

---

# II · THE CLOSURE PROTOCOL — **what happens when something becomes known**

**⌗ THE ORDER MATTERS, AND IT IS THE ORDER THE CAMPAIGN LEARNED THE HARD WAY.**

**⓵ RECEIPT FIRST.** *The result exists as a runnable receipt under `receipts/`, with `COMPUTES:` if it
pins a parameter, before any prose changes.*

**⓶ INVENTORY WHAT THE PROSE BINDS.** *List every `\rcpt{}` in the passage about to change.*
⚠ ***`check_receipts` catches a dropped binding only if the claim survives. A claim deleted with its
receipt cites nothing and fails nothing*** *— r2587, where a draft lost eleven live results and only the
inventory caught it.*

**⓷ REHOME, DO NOT ANNOTATE.** *The newly-known content goes **upstream into the physics**, written as
what is known, with no trace of having been a frontier. The account of how it moved goes to
`CONSOLIDATE`'s **REHOMING RECORD**.*
⌗ ***And the operation is usually a CLAUSE, not a section: if the defect is framing, the fix is one or two
clauses, and a clause cannot lose a result because no result is lifted out.***

**⓸ DE-NARRATE.** *Apply the **tense test**: scope-delimitation is timeless ("this paper covers X and not
Y"); a resolved frontier is temporal ("has since", "no longer", "we wrote", "until rNNNN").*
⚠ ***And keep the exception: withdrawing a claim ON EVIDENCE is a present-state statement about what the
paper claims. Narrating that the corpus changed its mind over TIME is not.***

**⓹ FOLLOW THE CROSS-REFERENCES.** ⛭ ***The defect r2594 found: a frontier item resolves, its list entry
is removed, and an upstream sentence still points at it as "an open problem of the programme".***
⇒ *Grep the resolved item's own words across all papers before closing the turn.*

**⓺ UPDATE THE LEDGER.** *Re-run `check_open_ledger`. An entry whose sentence is gone is flagged; a new
one fails. Change the verdict and **write the reasoning beside it**.*

**⓻ UPDATE THE REGISTER.** *`PROTECTED_OPEN` on **progress**, not only on closure* — ⛭ *r2576's lesson:
**a document read only at one moment in a lifecycle goes stale between those moments**, and `PO-5` sat at
305 characters saying "Queued, never worked" through four sessions of work on it.*

**⓼ REGENERATE AND GATE.** *`make_all_appendices`, the dependency matrix in **both** copies, the full
suite.*

---

# III · THE WORK THAT MAKES IT COMPLETE

**⓵ VERDICT THE REMAINING 30.** *Each is one read, recorded once. **The only bucket that means work.***

**⓶ ✔✔ BUILT r2596 — THE BACKLOG CHECK.** ⛭ ***It was the one gate missing, and building it found two more things.*** *An entry verdicted `SELF-ANSWERED`
whose claim text still advertises openness is **an item advertised as owed after the work that closed it
was done** — exactly the failure this file exists to prevent.*
⌗ *Measured at r2596: **13 candidates, of which 11 are correct** (a `REGISTERED` item **should** read as
open — the paper is right and the register carries it). ***Two were real: one tense defect outside any
frontier section, and one verdict of mine that read the wrong object.***
⇒ ***So the check fires only on `SELF-ANSWERED`, and its precision depends on the verdicts being right — which is
why the reasoning is recorded beside each.***

⌗ **AND BUILDING IT SURFACED TWO THINGS THE MEASUREMENT HAD NOT:**
*· ⛔ ***`--rebuild` was dropping the reasoning*** — it re-derives the claim text from the paper, and the `##` notes
lived in that field. **Fixed: the rebuild now preserves both verdict and reasoning**, which is the whole point of
recording them.*
*· ⚠ ***one false positive, excluded by NAMING the sense rather than loosening the pattern***: `boundary_paper`'s
**"the gate is open and has been walked"** uses *open* to mean **available**, not unresolved. *Loosening `OPENWORD`
to dodge it would blind the check to real cases.* *(rewritten out of the paper at `r3797`; kept here as the example that shaped the rule.)*

**⓷ GIVE THE TWO GENUINELY UNBUILT THINGS REGISTER ROWS.** *The **propagating spinor sector** — ⛭ **built at `r3802`** — (p0 and
`boundary_paper`, one object) and the **bespoke transfer** (`CR_cosmology`). ***Neither is on
`PROTECTED_OPEN` and both should be.***

**⓸ NAME THE CONVERGENCE.** *`PO-5`'s mod-2 index, P14's traced Atiyah–Singer statement, and P14's
multiplicity gap are **one calculation under three names**. ***The register should say so once rather than
carry three rows that nobody connects.***

---

# IV · WHAT THIS BUYS

⇒⇒ ***A programme where "what is left?" is answered by a file rather than a re-derivation, where closing
an item is a checklist rather than a judgement call, and where the corpus cannot silently advertise a debt
it has already paid.***

⚠ **AND THE HONEST LIMIT.** *No gate checks that a verdict is **correct** — that is a reading, and one of
mine was wrong within two revisions of being written.* ⇒ ***What the system guarantees is that every
qualification HAS a verdict, that none appears without being seen, and that the reasoning is beside it so
the next reader can overturn it cheaply.***

*Written r2596. Stated for reversal.*
