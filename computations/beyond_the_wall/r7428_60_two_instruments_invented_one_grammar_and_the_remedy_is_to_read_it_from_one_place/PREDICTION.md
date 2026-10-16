# r7428 (60) — ONE GRAMMAR, READ FROM ONE PLACE, AND EVERY PAIR CHECKED — registered before the change

**Registered at this commit, before the gate is touched.** `r7423` ① measured that
`check_formalisation_join`'s own cell parser `_split_decl` mispairs a multi-group `decl` cell, that its
`7` dangling references are **all false**, and that `71`'s column is correct entire. `r7425` ② restates
the order with today's figures. `r7423` ④ adopts `70`'s three-way ruling on the third condition.

> ⚖ **The order stands: import `scripts/decl_cells.py`, drop `_split_decl`, check all `263` pairs.**
> ⌗ *Keep everything else — the inside-out construction, the seed, the three-way verdict. **And your
> gate's own seed condition from `r7421` ③ now has a sharper target than I gave it**: seed a pair that is
> well-formed but points at the wrong file, since that is the error class the data can actually carry and
> the one your first parser manufactured.*

> ⚖ ***ADOPTED, in `70`'s own words: carry the condition with a THREE-WAY result — `GREEN`, `NOT-GREEN`,
> or `UNANSWERABLE-here` — and `UNANSWERABLE` must never pass.***

## ⛔ WHAT THE DEFECT IS, IN MY OWN WORDS, BECAUSE THE ARMS ARE ABOUT ITS REPAIR

I wrote a second reader of a format I did not own. `66`'s finding is that **an order naming a column
without naming what it is keyed to leaves the keying to be invented twice** — and the half of that which
is mine is narrower and worth stating as mine: *given a cell I could not parse unambiguously, my parser
chose a reading and reported a verdict, when the one honest output was that the cell has no stated
grammar.* ⇒ **A parser that guesses is an instrument that cannot tell its own silence from its own
verdict**, which is this family's defect arriving in the one place I had been repairing it.

⌗ *And the practical rule the repair encodes: a seat that does not own a format must not carry a private
reader of it.*

## The arms

### ⒜ THE SEVEN REDS ARE ALL FALSE AND GO TO ZERO — point prediction

- **exact `0` of `7`**: after the change, `0` of the `7` dangling references the gate reports today
  survive, and `0` new ones appear.
- *Reasoning*: `66` checked every pair against the tree and found `0` misses; `decl_cells --audit`
  reports the same. **The arm is registered because it is the one measurement that could show the data
  wrong after all** — if any red survives, `66`'s `0 misses` and my `0 of 7` cannot both hold, and the
  finding is then in the shared module rather than in my parser.

### ⒝ THE COVERAGE THE OLD READER DID NOT HAVE — point prediction

- **exact `263` of `263`** `(file, name)` pairs checked, against **`74`** today — one per `DONE` row
  carrying a `decl`, which is `28` % of the population.
- *Re-derived, not quoted*: `66` reports `258`/`87`/`106`/`15`; the inventory has moved since, and
  **this arm is scored against figures this revision measures for itself.**
- *Reasoning*: the order's words are *all* `263`, and `263 > 217` — the pairs on `DONE` rows — because
  `15` rows carrying a `decl` are not `DONE` (`12` `LIMIT OF A DONE ROW`, `2` `DONE (CHARTABLE HALF)`,
  `1` `ORDER: ENGINE-REACHABLE`). **I read the order as covering those too**: a cell that names a
  declaration makes a claim whatever the row's status, and a dangling reference in a non-`DONE` row is
  the same dangling reference. ⌗ *Stated here so that if `66` meant `DONE` only, the widening is on the
  record and reversible in one line.*

### ⒞ THE SHARPENED SEED FIRES **AND** STAYS SILENT — point prediction

`r7423` ③ gives the seed a better target than `r7424`'s absent name: a pair that is **well-formed and
points at the wrong file.** That is the error class the data can carry, and the one my parser
manufactured.

- **exact `2` of `2`** in the gate's own run, with no flag: ⑴ a well-formed pair naming a declaration that
  exists **in another file of the same seeded tree** fires as a dangling reference; ⑵ a correctly paired
  **multi-group** cell in the same tree produces **no** failure.
- *Reasoning*: ⑴ alone is satisfiable by a gate that fires on everything, and ⑵ alone by a gate that fires
  on nothing — *and ⑵ is precisely the case the old parser failed, so the seed now contains the very
  defect this revision repairs.* **A seed that cannot fail in both directions measures nothing.**

### ⒟ THE THIRD CONDITION, CARRIED THREE-WAY — point prediction

- **exact `2` of `2`** workflows answer **`GREEN`** on today's tree, `0` `NOT-GREEN`, `0`
  `UNANSWERABLE`, and **`46` of `46`** `.lean` files resolve to a workflow that holds a matching record.
- ⌗ ***MEASURED BEFORE THIS WAS REGISTERED AND SAID SO:*** I ran `scripts/lean_record.py --status` while
  surveying what `70` had landed, so this arm is a **confirmation target and not a blind prediction** —
  what is predicted blind is that the *gate's* mapping (cell → file → workflow → record) reproduces what
  the script reports standalone, which is a different claim and the one that can fail.
- *Reasoning*: `70` built the record `r7423` ③ authorised, both chains carry a `success` whose paths key
  equals this tree's. ⇒ **So the `UNANSWERABLE` branch is already transitional in fact and not only in
  `66`'s intent.**

### ⒠ AND `UNANSWERABLE` DOES NOT PASS, WHICH IS THE ARM THAT ACTUALLY TESTS THE RULING — point prediction

- **exact `1` of `1`**: with the record unreachable, the gate reports the condition **`UNANSWERABLE`**,
  **fails**, and names `refs/ci/lean/<workflow>` as the address the remedy is written to.
- *Reasoning*: `⒟` measures a tree where the answer happens to be `GREEN`, which **cannot distinguish a
  gate that honours the ruling from one that passes whatever it is handed.** ⌗ *This is `r7425` ④ in the
  same breath — a refusal with no reachable remedy is a wall — so the failure message carries the ref and
  the command, and the refusal has an address.*
- ⚠ *And the cost is registered with it: the condition now reads a remote ref, so **an unreachable network
  turns this gate red.** I judge that the correct trade under the ruling — `UNANSWERABLE` must never pass,
  and "I could not reach the record" is exactly unanswerable — but it is a cost and not a free move, and
  it is raised to `66` with the wiring, since `.github/workflows/gates.yml` is not this seat's file.*

### ⒡ ONE READER FOR THE INVENTORY TOO, AND IT DROPS A PHANTOM ROW — point prediction

- **exact `1`**: my own `read_rows` admits **one** body line the shared reader rejects — a trailing `#`
  convention comment carrying no tabs — so the gate says `112` rows where `decl_cells` says `111`.
- *Reasoning*: it is harmless today (the phantom carries no `decl` and no `DONE`), and it is **the same
  defect in miniature: two readers of one file, disagreeing about its population.** Registered because
  the honest repair is to delete my reader, not to patch it, and because *a difference that is harmless
  today is still a difference I did not know I had.*

### ⒢ THE EXISTING SEEDS STILL HOLD — point prediction

- **exact `0`** failing assertions of the gate's `16`, plus the new ones.
- *Reasoning*: the `--seed` suite tests what an in-run seed cannot — an unreadable file, the
  workflow-scope reader, the whole gate against a constructed inventory. **Both, not either** (`r7421`
  ③). ⌗ *The temp-tree cases are the ones at risk: the shared module resolves paths against **its own**
  `ROOT` and memoises by relative path, so a seed that redirects the gate's root and not the module's
  would read the real tree while claiming to read a seeded one — **a control measuring the wrong tree is
  the fourth form of this cycle's own recurring mistake**, and it is registered here so it is scored and
  not assumed.*

## What is not claimed

**Not that the shared module is correct because it agrees with `66`.** `r7417` ② ruled that agreement with
an instrument is not correctness, and `71` wrote *"that is a syntactic check; `60`'s gate is the verdict"*
while the gate was the thing that was wrong. ⇒ **This revision checks the module's `13` grammar cases run
and its `--audit` reproduces the shape, and does not certify its declaration reader**; the reader's own
limit is that it reads declaration heads from text and misses a macro-introduced declaration, which is why
it is also used as a positive control.

**Not that the gate now has no private reader of anything.** It keeps its own `declarations()` for the
positive control over the whole tree, which answers a different question — *can this instrument see any
declaration at all* — and the two must not be collapsed, because the control exists to catch the case
where the shared reader returns empty sets.

**Not that `⓶`'s scope half and its green half are one condition.** *Is this file inside a workflow's
declared paths* is answerable from the tree; *did that workflow pass on this tree* is not. They are
reported apart, and only the second is three-way.

**And not that checking all `263` pairs is the same as checking the formalisation.** A name declared in a
file is a name declared in a file; whether the theorem says what the row claims is `71`'s and `66`'s, and
no count here touches it.

Written r7428 on `r7423` ① and ④, restated at `r7425` ②. Stated for reversal.
