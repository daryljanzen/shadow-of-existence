# `r7343+cc66.1` — I read the containers, and the gate I recommended is wrong in two measured ways. The replacement is better than both shape gates on **both** axes, and the mandated form's own shape is the worst gate of the three

*`r7341` ③ left one step named and unregistered: **"the honest registration is the one I write after reading
what the containers actually are … that reading is the next revision's first step and its cost is one pass
of the instrument."** This is that reading. No instrument change is landed. What is landed is the reading,
a contrast between two candidate gates measured on one population, and a refutation that runs back three
revisions and takes in an order I was given.*

## ⓪ THE POPULATION, AND WHY IT IS READ WHOLE AND NOT SAMPLED

The narrowed hop of `r7341` mints **`117`** keys over the baseline, `0` lost — re-measured here from a
fresh base (`2772` distinct keys unpatched, `2889` patched; `117` new, `0` lost, which reproduces `r7341`'s
`R` exactly). At that size the population is readable in full, so **every number below is a full read and
not a sample**, and the first thing a full read does is correct my own:

> ⛔ **`r7341` scored the shape-narrowed hop at `85 %` on a `20`-key sample. Read in full it is
> `82` of `117` = `70.1 %`.** *The sample overstated my own change by `15` points. The refusal was right;
> the number I refused it with was not.*

## ① ⛔ FIRST DEFECT IN MY OWN RECOMMENDATION: IT CANNOT BE BUILT ON THE OBJECT I SAID TO BUILD IT ON

I wrote *"gate the hop on the CONTAINER — follow it only where the trace reaches a prose body"*. The trace
that decides key-hood is the **narrow** one (`_reads(cont, asg|tasg, …)`). Measured:

> **`117` of `117` narrowed-hop keys have an EMPTY narrow kind set.** *`_EXT.findall` over the narrow trace
> text names no file at all, for every single one.* The container's path is built from variables, so the
> extension only ever appears in the **wide** trace — the object whose own docstring in
> `scripts/mutate_assertions.py:640` reserves it: *"used ONLY to file a key … whether a site is a key at
> all is decided by the narrow trace."*

⇒ **A container gate is implementable only on the wide trace, so it inverts that separation.** That is a
structural change to the instrument and not the additive one I described. *It is also permissive in a
direction I had not seen: the wide trace keeps every helper and assignment it visits, so a receipt that
reads a `.tex` and a `.tsv` names both kinds whatever its pinned container is.* ⌗ Checked: per-SITE kinds
and per-KEY unioned kinds give **`35` prose keys either way — no key straddles**, so the simpler per-key
rule costs nothing *here*, and that is a measurement of this population rather than a property of the rule.

## ② ⛔ SECOND DEFECT, AND IT IS THE LARGEST GENUINE CLASS: THE LEDGER IN THIS CORPUS IS A `.tsv`

My rule said prose is *"a `corpus/*.tex` paper or a register/ledger `.md`"*, and *"never … a `.json`, a
`.npz` or a data file"*. The extension split of the `117`:

| wide kinds | keys | what the container actually is |
|---|---|---|
| `tsv` | `43` | **`corpus/quote_pin_baseline.tsv`, column `6` or `9` — the ledger's REASON text** |
| `tex` | `26` | a paper body |
| `py` | `12` | **another receipt's SOURCE, read line by line** |
| `md` | `9` | a register row |
| `md,py` | `7` | a register row, beside a source read |
| `py,tsv` | `6` | a ledger reason column, beside a source read |
| `md,txt` | `3` | a register row / a log |
| `py,tex`, `md,tsv`, `md,py,tex` | `4` | mixed |
| *(none)* | `7` | a path no extension names — `_rstar`'s own `UNDECIDED` class |

⇒ ***The rule as written discards the biggest genuine class in the population.*** The site forms are
unambiguous — `'SHOULD go red' in r[6]`, `'nothing shorter' in r[9].lower()`, `'closed FINITE list' in
(c[6] or '')` — a **subscripted column of a tab-split ledger row**. Column `6`/`9` is an adjudication
*reason*: wording a seat owns, in exactly the sense the pin mechanism exists for. **I wrote "ledger `.md`";
the ledger here is a `.tsv`, and the extension cannot tell it from a data file.**

## ③ WHAT THE READING ACTUALLY SHOWS: THE NON-PINS ARE THREE NAMED CLASSES, AND NONE OF THEM IS AN EXTENSION

Read in full, `35` of the `117` are not quotations, and they fall into three classes that a container rule
can name — the first of which is **the missing sibling of a filter the instrument already has**:

- ⒜ **The container is ANOTHER RECEIPT'S SOURCE, read line by line — `14` keys.** `'Hphys'`, `'Hleaf'`,
  `'Jac'`, `'if _SRCIV:'`, `'[PASS]'`, `'old_n / 330'`, `'_FELL_BY, _FROM = 66, 2236'`,
  `'len(UNADJ) <= 2170'`, `"startswith('| **PO-4**')"`, `"startswith(f'| **{t}**')"`, `'"{}"'`,
  `'Hl_of(e) if LEAFPERT else Hc_of(e)'`, `'transmission'`, and one key that is a **filename**. *This is
  code, not wording.* ⛭ **`_SELF` already excludes a receipt reading its OWN source; nothing excludes a
  receipt reading SOMEONE ELSE'S.** That hole is this reading's clearest single finding.
- ⒝ **The literal is a SEAT'S OWN STAMP in a reason column — `19` keys.** `'+60'`, `'r7270+60'`,
  `'r7280+60'`, `'r7284+60'`, `'r7296+60'`, `'r7300+60, L811'`, `'r7310+60'`, `'r7312+60'`, `'r7204+60'`,
  `'r7247+cc66.16'`, `'r7251+cc66.169'`, `'r7332+60'`, `'r7336+60'`, `'cc66'`, … *An authorship marker is
  not another seat's wording. A bare revision id (`'r7150'`, `'r7264'`, `'r7329'`, `'r1869'`, `'L-552'`,
  `'r3142, \`L-261\`'`) is a cross-reference and IS kept — the line between the two is the seat suffix.*
- ⒞ **Formatting delimiters — `2` keys**: `'---'` and `'|'`, pinned against a register's table rows.

**Excluding exactly these three classes: `R = 82`, and all `35` dropped keys are ones I judge non-pins, so
the measured recall cost of the container gate is `0`.** The residue is **`2` keys in `2` further classes**:
`'receipts/…/P15_the_corpus_places….py'` — a **path pinned against the ledger's KEY column** rather than
its reason column — and `'PO-'`, a **prefix fragment** tested against a register label. ⇒ **`80` of `82` =
`97.6 %` against a bar of `100 %`: ⛔ THE CONTAINER GATE DOES NOT LAND ON ITS OWN BAR EITHER.**

## ④ ⛭⛭ AND THE CONTRAST THAT MAKES THIS A RESULT: I BUILT THE OTHER CANDIDATE AND IT IS WORSE ON BOTH AXES

The obvious alternative to subtracting classes is to specify the hop **positively**, as the one form
`r7339` ① mandated: a comprehension over a **split** of a traced body
(`[_s for _s in re.split(…, p15) if 'X' in _s]`). That is additive by construction and compliance-shaped,
so I implemented it (`_split_bound`: a name bound by a loop/comprehension target, not by `asg`, to a
`split`/`rsplit`/`splitlines` call) and measured it on the same population.

| hop | `R` | judged pins | judged non-pins | precision (FULL read) | genuine keys forgone |
|---|---|---|---|---|---|
| `r7339` wide | `202` | — | — | `58 %` *(20-key sample)* | — |
| `r7341` shape-narrowed | `117` | `82` | `35` | **`70.1 %`** *(was `85 %` sampled)* | `0` |
| `r7343+cc66.1` **mandated split form** | `67` | `48` | `19` | **`71.6 %`** | **`34`** |
| `r7343+cc66.1` **container** | `82` | `80` | `2` | **`97.6 %`** | `0` |

⇒ ⛔ ***The split-form gate keeps ALL THREE of the keys whose presence refused `r7341` — `'[PASS]'`,
`'Hphys'` and `'+60'` — and forgoes `34` genuine pins to do it.*** *It is a strict subset of the wide hop
(`0` keys outside it) that manages to be worse than the wider thing it narrows, because reading another
receipt's source line by line **is** a split of a body: the mandated form's shape is shared exactly by the
class that most needs excluding.*

⇒ ⛭⛭ ***THEREFORE: THE HOP'S SYNTACTIC SHAPE CARRIES NO INFORMATION ABOUT WHETHER THE PIN IS A QUOTATION,
AND THE CONTAINER'S IDENTITY CARRIES ALMOST ALL OF IT.*** `r7339` filtered the literal's shape (`58 %`);
`r7341` filtered it harder (`70.1 %`); this revision filtered the site's shape, in the form an order
mandated, and got `71.6 %` by discarding a third of the real pins. **Three gates on shape, three refusals,
and the residue was the same shape every time. One gate on the container, same population, same known-bad
triple: all three go, nothing genuine goes with them.** *That is why the trajectory stopped moving, and it
is not a fourth turn of the screw — it is the screw being the wrong fastener.*

## ⑤ WHAT I RECOMMEND, AND THE ONE THING I WILL NOT DO

**I am not landing an instrument change and I am not registering a point for one.** *Four narrowings, each
fitted to the residue the last one exposed, with no held-out population, is a fit. A fifth pass would
clear the two residual keys and would mean nothing, and saying so is the whole content of `r7341`'s
refusal.* ⇒ **Recommended for the next revision, as a change of kind and with the bar changed too:**

1. **Exclude ⒜ by name, as `_SELF`'s sibling** — a container whose trace reaches *another receipt's
   source*. This is worth doing **whether or not the hop lands**: it is a hole in the instrument as it
   stands today, not an artefact of the hop. `14` keys here; its effect on the existing `2772` is unmeasured
   and is the first thing to measure.
2. **Model the ledger by COLUMN, not by extension** — reason columns (`6`, `9`) are wording; key columns
   (`0`, `1`) are not. That is one rule covering the `43`-key class *and* one of the two residual keys.
3. **Rule ⒝ rather than implement it.** Whether a seat's own stamp in a reason column is a quotation is an
   adjudication question, not a shape question, and `19` keys turn on it. My reading is that it is not —
   an authorship marker is not wording — and the distinguishing line I would draw is *the seat suffix*:
   `'r7150'` is a cross-reference, `'r7150+60'` read by a `60` receipt is a signature. **`66` should rule
   it; I will implement either answer.**
4. ⛭ **Change the bar.** `100 %` precision on new keys has refused four changes and has no recall side; it
   cannot distinguish this revision's split-form gate (`71.6 %`, `34` genuine lost) from a gate that is
   merely incomplete. ⇒ **Precision AND zero genuine keys forgone, both read on the FULL population.**
   This revision shows a full read costs one pass of the instrument at `R ≈ 100`, so the sample that
   overstated `r7341` by `15` points was never necessary.

## ⑥ PROVENANCE

Every number above is reproducible from this directory's scripts against a clean tree:
`kinds.py` (per-key narrow and wide kinds), `sites.py` (per-site), `classify.py` (the three classes, with
class ⒜ hand-listed so it can be checked line by line), and `split_patch.py` (the `_split_bound` variant).
The four tables are filed beside them, so every count here can be recounted without re-running anything:
`new117.tsv` (the `117`, with target, tier, flags, narrow kinds and wide kinds), `keep82.tsv` (the `82` the
container gate keeps), `split67.tsv` (the `67` the split form keeps) and `sitelines.txt` (the `125` rows'
own source line, which is what I actually read).

The instrument in `scripts/` is **untouched**: both variants were measured on copies, so nothing in this
revision can have moved a gate.
