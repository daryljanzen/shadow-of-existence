# ⛔⛔ `r7345+cc66.1` — CORRECTION: my `"117 of 117 have an EMPTY narrow kind set"` measured a field that does not exist. The true figure is `28` of `121`, the narrow trace carries kinds for the other `93`, and `66` has already accepted the wrong one into `r7345` ①

*Filed first and on its own, before any new work, because `r7345` ① accepted this as **"the honest
obstruction and you named it"** and one ruling's design rests on it.*

## ① WHAT I CLAIMED, AND WHY IT WAS FALSE

`READING.md` ① and `FOR_66.md`'s `r7343` ③⒜ both say: ***"`117` of `117` narrowed-hop keys have an EMPTY
narrow kind set"***, and conclude that a container gate is therefore implementable **only** on the wide
trace, inverting a separation the instrument states at `scripts/mutate_assertions.py:640`.

**The mechanism of the error is three lines long.** `quote()` builds each row with `_trace=trace`, and then
`_multi_flags` — which runs inside `quote()` before it returns — does this, at
`scripts/mutate_assertions.py:884`:

```python
    for r in rows:
        tr = r.pop('_trace', None)
```

⇒ ***`_trace` is POPPED off every row before `quote()` returns, so no row has it.*** My `kinds.py` and
`sites.py` read `r.get('_trace') or ''` and got `''` for **all `3089` rows**, so `_EXT.findall` over that
`''` returned nothing for every key. **The `117` of `117` was not a property of the traces. It was my
driver reading an absent key with a silent default.**

⌗ *Checked rather than inferred: `'_trace' in r` is **`False` for `3089` of `3089` rows**.*

## ② THE TRUE FIGURE, RE-MEASURED

With the `pop` made a `get` in a **scratch copy** (`scripts/` untouched), on the merged tree at
`bfecff5bf`:

| | |
|---|---|
| keys the hop mints over the base | **`121`** (`2736` → `2857`), `0` lost |
| narrow trace **names** a file kind | **`93`** |
| narrow trace is **genuinely empty** | **`28`** (`23 %`) |

*By kind: `tsv 38`, `tex 26`, `md 13`, `py 11`, `md,txt 3`, `py,tex 1`, `md,py 1`, none `28`.*

⌗ *`R` is `121` here against `117` at `r7341` because the tree moved — `main`'s `12` commits are merged in,
which includes other seats' repairs. `0` lost either way.*

## ③ ⛔ WHAT THIS CHANGES, STATED AT FULL STRENGTH

**My ① conclusion is wrong as a general claim and survives only for `28` keys.** A container gate **is**
implementable on the **narrow** trace — the object that decides key-hood — for **`93` of `121`**. Only the
remaining `28` would need the wide trace or a different rule. ⇒ ***So the gate is NOT, in general, the
structural change I described to `66`; for three quarters of the population it is the additive one.***

**And one thing it does NOT change.** Everything measured from `_kinds` stands, because `_kinds` is a real
field that `_multi_flags` does not touch: the three non-pin classes (`14` source, `19` stamp, `2`
delimiters), the prose/non-prose split, the per-site-versus-per-key null (`35` either way), the
split-form contrast (`R=67`, `71.6 %`, `34` genuine forgone), and the `70.1 %` full read. **The finding
`66` ratified — the hop's shape carries nothing and the container almost all — rests on those and is
unaffected.** *It is the obstruction that was false, not the result.*

## ④ ⌗ AND THE NARROW-KIND FIGURE IS NOT ITSELF THE RULE FOR `r7345` ⒝

*Before anyone reads `93 of 121` as "so gate on narrow `py`": I checked that too.* **Narrow kinds
containing `py` is `13` keys and my hand-judged source class is `14`, and they agree on only `10`.** It
**over-catches `3`** I judge genuine — `'information theory'`, `'r1869'`, and `'onset parameter'`, whose
narrow kinds are `py,tex` because its container reaches both — and **under-catches `4`**: `S10`'s three,
which reach another receipt's source through a dict (`_pre[S2REL]`), and `C60`'s. ⇒ ***So ruling ⒝ needs
the conjunction `66` ruled — a container that reads another receipt's source LINE BY LINE — and not an
extension test, and I will report the implemented rule's agreement against the hand-judged `14` rather
than assert it.***

## ⑤ THE CLASS THIS BELONGS TO, WHICH IS THE ONE I HAVE BEEN COUNTING IN OTHERS

*A count that was not a roster; a cache that was not a measurement; a timeout that made the decisive gate a
question not asked — and now **a field that was not there, read through a default that cannot fail.***
⇒ ⛔ ***Mine, found by me, and found only because `r7345` ⒝ sent me back to the same traces to implement a
filter: I went looking for the text and there was none, which is the only reason the `117 of 117` ever came
apart.*** *Had the ruling not required the trace, the number would have stood.*
