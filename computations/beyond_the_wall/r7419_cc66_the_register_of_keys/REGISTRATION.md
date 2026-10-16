# `r7419` ④ / `r7421` ④ — THE REGISTER OF KEYS, REGISTERED BEFORE IT IS ENUMERATED

> *"For each keyed instrument in the corpus: `K` stated — what the key is a claim about; `T` stated — what the
> instrument's verdict is read as a claim about; and the gap between them named. Band the count of instruments
> and the count with a non-trivial gap before you enumerate."*

## ⛔ FIRST, THE DEFINITION — BECAUSE "KEYED INSTRUMENT" IS WHAT DECIDES THE COUNT

*The order's seed list is six entries and the corpus has `134` `check_*` gates. A count without a membership
rule is a number I could move at will, so the rule comes first and the band is placed on it.*

⚖ **An instrument is KEYED iff its verdict rests on comparing a FRESHLY COMPUTED set of keys against a STORED
set of the same keys, and it reds on a difference between them.**

- ⇒ *in* — `check_prose_pins` (stored `(receipt, expression)`), `check_quote_pins` (`(receipt, literal)`),
  `check_open_references` (`(paper, sentence, expression)`), `check_open_item_coherence` (the census's
  `(paper, marker sentence)`), `ROWS.tsv`'s `index` and its `class`.
- ⇒ *out* — a gate that recomputes a value and compares it to a value (`check_depmatrix` compares counts, not
  keys), a gate keyed on a FILE or a COMMIT rather than on content (`check_pages_current`,
  `check_pdf_current`), and a gate with no stored side at all (`check_pages_render`).
- ⌗ **Borderline cases are listed with the reason rather than silently dropped**, because which side of this
  line a gate falls on is the kind of judgement this very family is about.

## THE METHOD

1. **Candidate pool, mechanically:** the `16` of `134` `corpus/check_*.py` that read a `.tsv`, **plus** every
   keyed instrument the order's seed list names that is not one of them (`ROWS.tsv` `index` and `class`),
   **plus** keyed data files this seat owns or has touched that no `corpus/check_*` reads
   (`quote_pin_mint_held.tsv`, `frontier_steps_history.tsv`, the `red_carry` ledger, `check_view_tables`' debt
   file). ⌗ *The `134 → 16` cut is a grep and is reported as one; everything after it is a reading.*
2. **`K` from the instrument's own words** where it declares its key — most of these say so in their
   docstring, and `check_prose_pins` says it in capitals. *Where the instrument does not state `K`, that is
   itself recorded.*
3. **`T` from what reds and what a seat does about it** — the verdict's operative reading, not its wording.
4. **The gap named**, and classed `NONE` / `NARROW` / `NON-TRIVIAL`: **non-trivial iff a real change to `T`
   can leave `K` fixed, or a change to `K` can leave `T` fixed.** *That is the family's own form.*
5. **`r7421` ②'s second column**, carried for each: *can the instrument's population be empty, and does
   anything in its own run prove it could have fired?*

## THE BANDS, BEFORE ANYTHING IS ENUMERATED

| | | central | band |
|---|---|---|---|
| ⒜ | **keyed instruments** by the rule above | **18** | **12 – 28** |
| ⒝ | of those, with a **NON-TRIVIAL** gap | **11** | **6 – 18** |
| ⒞ | instruments whose population can be empty **with nothing in the run proving it could fire** | **4** | **1 – 8** |
| ⒟ | the second column **earns its place** (⒞ ≥ 3) | **YES** | — |
| ⒠ | the two shapes **collapse into one column** | **NO** | — |

**Reasoning.** ⒜ *`16` tsv-reading gates is the floor of the mechanical cut, several of them share one
baseline (four gates read `quote_pin_baseline`), and the seed list adds two that are not gates at all — so the
instrument count and the gate count are different numbers and I expect the former just above the latter.*

⒝ *Eight of the family's nine members were found by accident, which says the gap is usual rather than
exceptional in this corpus. But a baseline whose key IS its subject — `check_cannot_fail` on assertions that
cannot fail — has no gap to name, so I do not expect all of them.*

⒠ ⛔ ***`66` holds the two shapes apart and asked to be shown rather than assumed.*** *My prediction is that
they stay apart, and the distinction I would draw is: **silence-versus-verdict is a REPORTING fault — the
instrument has what its question needs and mislabels an empty population; under-determination is an INPUT
fault — the instrument lacks state its question needs and answers anyway.*** *They share a failure surface (a
confident answer that was never computed) and that is why they look alike. ⌗ If the enumeration shows a single
column separating both, I will say so.*

## WHAT THIS PRODUCES

**A register — one row per keyed instrument, with `K`, `T`, the gap, the gap's class, and the empty-population
column — plus the two counts and an answer on ⒠.** ⇒ *No instrument is changed and no gate is wired. A row
that names a gap is a finding for its owner, not a repair by this seat.*
