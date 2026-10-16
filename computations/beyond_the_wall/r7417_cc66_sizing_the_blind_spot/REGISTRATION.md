# `r7417` ③ — SIZING THE BLIND SPOT, REGISTERED BEFORE IT IS LOOKED AT

> *"over the census's own rows, how many point at a sentence that did NOT move in a revision that changed its
> GROUND? … Give a band before you look, and give the method as well as the number, because the number
> without the method is another sentence key."*

⌗ *The last clause is the order's own guard against the defect it is measuring, so the method comes first.*

## THE METHOD

For each of the `257` rows of `items_keyed.tsv`, keyed `(paper, normalised marker sentence)`:

1. **`moved`** — its own normalised marker sentence is absent from the candidates `key.py`'s extraction finds
   in that paper **now**. *This is `.66`'s test exactly, and it returned `10`.*
2. **`ground_changed`** — the **section** the row sits in has gained or lost a marker sentence that is **not
   merely a rewording of one it already had**. Operationally: collect the section's `PAT`-matching sentences
   at the census base and now; pair them across the two sets by token Jaccard ≥ `0.50` (`pairs.py`'s rule);
   **the ground changed iff an unpaired addition or an unpaired removal survives.**
3. ⇒ **`BLIND SPOT` = `NOT moved` AND `ground_changed`.** *The row still keys cleanly, so no refresh will ever
   re-read it — and the question its verdict was about has gained or lost a settled claim underneath it.*

**Section** is the nearest preceding `\section`/`\subsection` in `body()`'s output, so the unit is the one
`66`'s form names. **Base** is `4a7a46e3`, the commit that added `items_keyed.tsv`; **now** is `main` at
`r7417`.

⛔ **WHERE THIS METHOD IS WRONG, STATED BEFORE THE NUMBER:**

- *`ground_changed` is a **proxy** for "gained or lost a settled question". A sentence can enter or leave a
  section without settling anything (an example added, a citation reworded past the pairing threshold), so
  **the proxy OVER-COUNTS**, and the direction of the error is known rather than guessed.*
- *The pairing threshold `0.50` is a judgement. ⇒ **I will report the count at `0.40` and `0.60` as well**, so
  the number carries its own sensitivity instead of resting on one cut.*
- *A row whose own sentence is unchanged can still be perfectly correct — the ground moving does not make it
  wrong. **This measures EXPOSURE, not error.** `.68` is the only thing in this phase that has measured
  error, and it did so by reading.*

## THE POPULATION AND THE CEILING, DERIVED FIRST

`257` rows. Four paper sources changed between `4a7a46e3` and `main`: `CR_cosmology` (P15, `35` rows),
`CR_framework` (P7, `40`), `cosmogenesis_paper` (P16, `11`), `groupoid_paper` (P5, `7`).

⇒ **`93` rows at risk; `10` of those already `moved` (`.66`). So the blind spot is at most `83`** — *`32.3` %
of the census, and that ceiling is reached only if every changed paper changed the ground of every section
holding a row.*

## THE BANDS, BEFORE ANY SECTION IS COMPARED

| | | central | band |
|---|---|---|---|
| ⒜ | **blind-spot rows** of the `257` | **30** | **12 – 60** |
| ⒝ | the same as a fraction of the census | **11.7 %** | 4.7 – 23.3 % |
| ⒞ | of ⒜, rows whose verdict is `OPEN` or `NOT-OPEN` (a status the ground bears on, rather than a `POINTER` or a `CHECK`) | **12** | **4 – 30** |
| ⒟ | the number is **LARGE** (`≥ 20`) | **YES** | — |

**Why I expect it well above `.66`'s `10`:** *the section is a coarser unit than the sentence.* `.68` found
that one reclassification invalidated `6` rows because `P7` cross-references its own `\S`frontiers from four
paragraphs — **and every OTHER census row sitting in those same sections is, by construction, a row whose
ground moved while its sentence did not.** ⇒ *The blind spot is the complement of the stale set inside the
affected sections, and `P7` alone carries `40` rows.*

⌗ ⒟ matters because the order says what turns on it: **if large, `PO-86`'s live clause — a ruling is
discharged when the paper it names has been READ WHOLE in its settled state — is the phase's method rather
than a note on it; if small, `66` narrows that line.** *I am registering LARGE, so I am registering that the
whole-paper read is the method.*

## WHAT THIS PRODUCES

**A count, its sensitivity, the per-paper split, and a statement about the remaining `17` stride items.**
⇒ *No row is re-verdicted and no paper is re-read: this sizes the exposure that `.68` demonstrated on ten
rows. Reading the blind-spot rows is a separate and much larger job, and whether it happens is `66`'s.*
