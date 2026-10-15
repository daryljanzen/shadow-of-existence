# `r7371` ⑥ — **THE KEY, named with what moves it and what does not** — and the gate it carries, priced at `0.049` s

*`r7371` ⑥ ②: **"Name the key you choose and say what moves it and what does not — that statement is
the deliverable as much as the gate is."*** ⇒ **This file is that statement.**

## ① THE KEY: **`(paper, normalised marker SENTENCE)`**

⛭ **And it is not invented here. It is `check_prose_pins`' own rule one level up**, quoted from
`corpus/prose_pin_baseline.tsv`:

> `** THE KEY IS (receipt, expression) AND NOT A LINE NUMBER, DELIBERATELY. **  A line-keyed baseline
> goes stale … An expression that is reworded is a NEW site and must be read again, which is correct.`

*The **marker sentence** is the sentence inside the candidate paragraph that carries the openness
marker — the sentence that makes the claim, not the paragraph around it.*

| | |
|---|---|
| **WHAT DOES NOT MOVE IT** | paragraph reflow and rewrapping; whitespace of any kind; paragraphs added or removed **anywhere else** in the paper; section renumbering or retitling; other paragraphs reworded; the paper gaining or losing unrelated content; the `.tex` file renamed — the `P*` label is the key's first half, not the stem |
| **WHAT DOES MOVE IT** | **rewording the sentence that states the openness** |

⇒ ⛭ ***And the second is CORRECT rather than a defect***, for the reason the prose-pin rule gives in its
own words: *a statement of openness that has been rewritten must be read again before it is credited.*
**A key that survived rewording would be asserting that an unread sentence still says what the old one
said.**

## ② ⛔ WHY NOT `69`'s `(paper, paragraph index)` — MEASURED, not asserted

| one paragraph inserted at the top of… | `cand` keys that move |
|---|---|
| `P1` | **`257` of `257` — `100` %** |
| `P2` | `251` |
| `P3` | `245` |
| median paper | **`166`** |

*18 papers, `2893` paragraphs, `257` candidates.* ⇒ **A key that a single edit anywhere near the front
of one paper invalidates wholesale cannot carry a ratchet.** ⌗ *A paragraph HASH is better than the
index and still wrong, for the reason ⑥ ② gives: it moves on any rewording of any sentence in the
paragraph, including ones that have nothing to do with the open item.*

## ③ ⛔ AND THE RE-KEYING HAD TO RUN NOW, BECAUSE THE WINDOW WAS STILL OPEN

*`69`'s `items.tsv` records its reading against the positional key, and that key **still resolves
today**: the extraction reproduces `257` candidates in the same order.* ⇒ ***The moment any paper
moves, `69`'s `257` adjudications become unattachable to the text they were made about.*** *So
`key.py` re-keys an existing reading onto a stable key; it makes no reading of its own, and changes no
`class`, `topic`, pointer or note — deciding whether an item is open is `69`'s, per ⑥ ④.*

⛔ **AND THE JOIN NEARLY WENT IN SILENTLY WRONG.** *`items.tsv`'s rows are **not** in `cand` order —
`205` of `257` sit at a position that is not their `cand` number (`cand 9` is displaced later).
**Joining by row position would have attached `69`'s classifications to the WRONG sentences for most
of the file**, with no symptom. Caught by an assertion written as a join check rather than a
formatting check.* ⌗ *The independent check that the fixed join is right: `69` recorded each
candidate's `paper` and the extraction derives it separately — **they agree on all `257`**, which is
not an assumption.*

## ④ THE GATE, and what it refuses to do

*`corpus/check_open_item_coherence.py`. ⑥ ① in both directions:*

⒜ *every item classed `OPEN` points at a **live** register row;* ⒝ *every live row is stated open by an
`OPEN` item or is **declared** infrastructure.*

⛔ ***It does not decide whether anything is open.*** *⑥ ④: that is a reading, `69` refused to make it
from a census, and each struck case is either a stale paper or a row struck too early. **The class
comes from the adjudicated baseline and never from the gate**, which compares two lists and names what
is in one and not the other.*

## ⑤ WHAT IT FINDS — and it corroborates `66` and `69` from a THIRD route

| | |
|---|---|
| adjudicated candidates | `257`, of which **`80` classed `OPEN`** |
| register `PO` rows | `75` — **`72` struck, `3` live** (`PO-50`, `PO-78`, `PO-86`) |
| ⛔ **`OPEN` items with NO live row** | **`79` of `80`**, across `14` papers |
| ⒝ live rows unstated and undeclared | **`0`** |

⇒ ⛭ ***So the register carries exactly ONE of the papers' open items, and it is `P18`'s "THE SEVEN"
table pointing at `PO-50` — its other seven pointers (`PO-45/30/47/31/25/49/24`) all struck.***

⌗ **`66` said the register carries one; `69` said "no open physics row but data-gated `PO-50`"; this
gate says `1` of `80`.** *Three seats, three routes — `66`'s reading, `69`'s census, and this
instrument built from `THE_REGISTER`'s own strikethrough markup joined to `69`'s classes on a
different key — and the same figure. **That agreement is worth more than any one of them.***

⌗ *`PO-78` and `PO-86` are **declared** infrastructure in the gate, with the reason recorded beside
each: the pin family is an instrument debt no paper states, and `PO-86` is this census's own row.*

## ⑥ THE PRICE, machine named per `70`'s `r7371` rule

| on this container | |
|---|---|
| `key.py` (the generator, re-keys `257`) | **`2.7` s** |
| **`check_open_item_coherence.py` (the gate)** | **`0.049` s** |

⇒ ⛭ **`66`'s expectation — "seconds, not minutes … which would put it in the fast job rather than any
backstop" — HOLDS**, and by a wide margin: the gate reads two files and compares two sets. *The
`2.7` s is the generator's, and generators already run in the fast job ahead of the gates.*

⚠ ***NOT WIRED.*** *The gate is not in `gates.yml` and exits `1` on the current tree, because the
correspondence it reports is `79`/`80` broken. **Wiring it now would put the fast job permanently
red**, which is the false-red shape `r7367+cc66.39` ⒞ was about. ⇒ *It belongs in the fast job the
moment the `79` are dispositioned — each one a stale paper or a row struck too early — and that
disposition is the papers' owners' and not this seat's.*
