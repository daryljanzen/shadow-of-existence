# `r7669` (cc66) — READING THE UNDECIDABLE ITEMS: ONLY **TWO** LEAVE THE LIST, AND THE CONTROL HAS NO ARM-OF-RECORD LEG IN ANY GRID FAMILY

**Receipts:** `classify.py` — 9 checks, 0 failures; `item4_c54178.py` — 6 checks, 0 failures.
**Registered:** `PREDICTION.md`, its own commit (`r7669+cc66.0`), pushed before `classify.py` existed.
**Tree:** `5e2eb9658` (`origin/main` at `r7669`).

## THE TWO RESULTS

**① The control has no `_leafrec1` leg in any grid family — four families, four times zero.**

| directory | `.npz` | `cr_*` | `lcdm_*` |
|---|---|---|---|
| `refit_grid` → `refit_grid_leafrec1` | 20 → 10 | 9 → 9 | 9 → **0** |
| `refit_grid185` → `refit_grid185_leafrec1` | 20 → 10 | 9 → 9 | 9 → **0** |
| `grid_oneclock` → `grid_oneclock_leafrec1` | 18 → 9 | 9 → 9 | 9 → **0** |
| `r7201_cc66_loading_lever` → `…_leafrec1` | 7 → 4 | 4 → 4 | 3 → **0** |

⚠ **This is evidence about the BANK, not a measurement of the physics, and `Ⓐ②` asserts that limit
explicitly.** It says every seat that built an arm-of-record grid built the CR legs and no control
leg. It does **not** say the control's features do not move — that is 70's ordered measurement under
the order's item 3, and nothing here substitutes for it. *The reading that fits the shape is that
`LEAFREC` is a property of the CR arm's leaf-rate treatment with no referent for a ΛCDM control,
which is why no seat ever built one; that is reasoning from the bank and is labelled as such.*

**② Reading the handover set moves almost none of it off the list.** Resolving each load site
through the **directory constant it joins** — `GO = os.path.join(BW, 'r7093_directions',
'grid_oneclock')` versus `GO['cr'] = …'grid_oneclock_leafrec1'` — decides what the load site alone
could not:

| across the 104 spectrum-loading receipts in scope | count |
|---|---|
| every resolved load is **arm of record** | **3** |
| loads **both** arms | **24** |
| every resolved load is **namesake** | **65** |
| audits every `.npz` under `computations/` with a recursive glob | **6** |

Restricted to the figure-printing handover subset — PO-87's own list, **24** items here:

| | items |
|---|---|
| arm of record only → **LEAVES** | **1** |
| tree-auditing glob → **LEAVES**, on other grounds | **1** |
| both arms → **the sentence decides**, not the loads | **5** |
| namesake only → **STAYS** | **17** |
| still undecidable from source | **1** |

⛔⛭⛭ **AND THREE OF THOSE "UNDECIDABLE" ITEMS WERE GAPS IN THIS CLASSIFIER, NOT IN THEIR SOURCE.**
The first cut of this file resolved directory constants only. Reading the residue by hand showed the
source says plainly what each one loads, through three shapes it did not handle:

1. **Call sites.** `B5`/`B8` do `peaks(os.path.join(SP, 'c54.186_cr_L3000.npz'))` into
   `def peaks(path): np.load(path)` — the filename is at the **caller**. `census.py` already had
   this pass; this file did not.
2. **Tuple-of-tuples constants.** `SPECTRA = (('cr_base', os.path.join(GO, 'cr_base.npz')), …)`.
3. **Iterated tables.** `for tag, path in SPECTRA: np.load(path)` — the load site's only `Name` is
   the loop variable, so **no site-level resolution can reach the table**. That one is attributed at
   **receipt level** and labelled as such: it says what the receipt reads, not which line reads it.

⇒ Closing those three took the handover set's undecidable residue from **9 to 1** and this subset's
from **4 to 1**. ⌗ *Which is the same lesson a sixth time, now against my own second instrument: the
residue was not the tree being unreadable, it was my reader being cheaper than the source. The one
item left — `P15_the_arms_own_driving_pair_reproduces_the_banked_one…` — is named rather than
guessed.*

## THE REGISTERED ARMS — TWO MISSED, TWO HIT

**① FALSIFIED, and not narrowly.** Registered: **8 to 14** of the undecidable items leave the list
once read. **Two leave.** *I reasoned from "ten of them mention `leafrec1` in their own source" —
but mentioning it is not loading it: most of those mentions are a header guard asserting a
counterpart exists, or a comment explaining why the namesake is the one pinned. **The same mistake
as the whole `r7667` sequence, one more time: I keyed on a cheaper signal than the question.***

**② WRONG IN THE OPPOSITE DIRECTION, cause named.** Registered: the 22-vs-21 gap against
`census.py` is **one** item. This file's figure-printing handover subset is **24**, so the gap is
**two** and runs the other way. ⇒ **The cause is the candidate set, not the sentence test:**
`census.py` excludes any receipt carrying an arm-of-record load site, so its undecidable bucket
never holds the **4 both-arm items** this file keeps. *Named rather than reconciled by quietly
moving one: the classification is reported per item, so the boundary changes the headline count and
no receipt's verdict.*

**③ HIT.** The tree-auditing class is real: **6** receipts in scope, **1** in the figure-printing
handover subset, glob `computations/**/*.npz` and audit every spectrum by construction. They do not
*rest* on a namesake in any sense a rebuild would fix.

**④ HIT.** The two receipts whose own header guard asserts the loaded file **is** the LEAFREC=0
namesake and that an arm-of-record counterpart exists beside it — `P15_the_phase_is_the_driving…`
and `P15_where_the_likelihood_sits` — both resolve to the namesake side. They are **RE-GROUND with
the wording already written by the receipt**, not work to invent.

## WHAT THIS MEANS FOR THE ORDER'S ITEMS 2–4

- **Item 2 (RE-GROUND vs REBUILD) is now the whole of the work**, and it turns on sentences rather
  than loads: **17** items stay on namesake reads, **5** are decided by which figure their sentence
  prints, and **1** is still undecidable from source. `ITEM2_TRIAGE.md` sorts the 53 surviving
  figure-printing items for that reading and states plainly that it is a sorting aid, not a verdict.
- **Item 3:** every namesake-only read whose spectrum is a **control** leg has no arm-of-record
  counterpart in the bank at all, by `Ⓐ①`. ⇒ *A control-only read cannot be REBUILD, because there is
  nothing to rebuild it against* — but per the order that is not counted until **70** reports, and
  this file counts nothing.
- **Item 4 (`c54.178`) is answered in `item4_c54178.py`, and it has no work in it.** 47 receipts
  mention it, 12 load it, 3 are body-cited and **all three read the control leg**; the CR-arm
  loaders carry no body sentence at all. `c54.178_lcdm_leafrec1.npz` does not exist, so there is **no
  arm-of-record figure to re-ground onto** — which makes the one sentence in print (*"about $989$ of
  the $1320$ survives it"*) the order's **item 3** case, not item 4's, and it is not counted here.

## WHAT THIS DOES NOT SETTLE

No figure is re-derived, no sentence is rewritten, and no item is routed yet. The **4 still
undecidable** are named in `run.txt` rather than assumed either way.
