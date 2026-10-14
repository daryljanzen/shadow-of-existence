# The narrowed hop at a POINT, and the dead pin bound inside it

`r7341` ④ and ⑧, code seat of node `66`. **Pushed before the rule is touched.** *`r7339`'s wide rule was
refused by my own conditions at `58 %` precision; this one is narrow, and the prediction is a point
because the refused measurement supplies it.*

## ① The rule, narrowed exactly as ④ orders it

Follow the loop-or-comprehension binding **only** where all three hold:

1. the literal is tested with `in` against a container the trace reaches **as text**;
2. ⛔ the container is **never** consumed by `re.*` — `re.search`, `re.match`, `re.findall`, `re.split`
   or a compiled pattern's methods;
3. ⛔ the literal is **never** a bare identifier — no `\d`, `\s`, `\b`, `(?`, `[^`, a character class or
   an anchor, nothing of two characters or fewer, and nothing matching `^[_A-Za-z][_A-Za-z0-9]*$` that is
   all-caps or carries an underscore.

*Conditions `2` and `3` are the two classes the wide rule actually produced: `55` regex patterns and
`20` code identifiers of `202`, plus `9` too short.*

## ② THE PREDICTION, as a POINT

| | registered |
|---|---|
| **R**, new keys the narrowed instrument keys | **`118`**, a point |
| tolerance | **`±12`** — `106`–`130` |
| ⛔ refutation | outside that, **either way** |
| keys LOST | **`0`** required; any loss refutes outright |

⌗ ***`118` is not a guess and that is why it is a point: it is the measured count of prose-or-register-text
keys among the `202` the wide rule produced, classified by the same three conditions above.*** *So the
honest reading of a hit is weak — I am predicting that a filter I derived FROM a measurement reproduces
that measurement. **The informative outcomes are the misses:** below `106` means a condition is
over-broad and is cutting genuine pins; above `130` means the conditions admit a class the `202` did not
contain, which would mean my classification of them was wrong.*

## ③ The precision bar, unchanged at `100 %`, because it is the condition that did the work

**`20` new keys, every tenth in sorted order wrapping, read by hand; ONE spurious and the change does not
land.** ⌗ *`r7339`'s bar stopped an ORDERED change at `10` of `20` spurious. It is kept verbatim.*

## ④ ⛔ THE DEAD PIN, bound inside this registration as ⑧ directs

**Definition:** a live quote-pin key whose literal occurs **zero** times in the container it is checked
against. *It can sit `EXTENDED` and green indefinitely when a disjunction around it carries the check —
`P15_the_history…` was one, matching `0` times while adjudicated as a widening.*

⌗ ⛭ **And my own instrument was already finding them and throwing them away:** `floor2.py` computes a
per-container count for every live key and then does `if not hits: continue`. ***That discarded branch IS
this class.*** Recording it instead is the whole of the measurement.

| | registered |
|---|---|
| scope **this revision** | every live key filed `PAPER`, against every `corpus/*.tex` |
| **D**, dead `PAPER` keys | band **`3`–`40`** |
| point | **`12`** |
| ⛔ refutation | `D = 0` (the class would not exist and `P15`'s instance would be unexplained) or `D > 60` |

⛔ **STATED LIMIT, before the number:** *`SOURCE`-filed keys are **not** covered — their containers are
ledgers, registers and receipt sources that `floor2.py` does not load — and `143` of `r7339`'s `202` were
`SOURCE`, so the uncovered share is large and I am naming it rather than letting the `PAPER` number stand
for the ledger.* **A pin read at a PINNED commit is also excluded**, per `r7341` ⑦⒜ and for the same
reason: its container cannot move.

## ⑤ ⛔ AND THE VANISHING SPAN IS DEFERRED, WITH THE REASON, USING ⑧'s OWN ESCAPE

⑧ offers: *"if that is too much for one revision, say so and take the dead pin first."* **I am saying so.**
*The dead pin lands here because it is the one that can make a green receipt a lie. The vanishing span —
`15` of `302` `P15`-wide, every one produced by extending a literal by a character distance — needs the
same container resolution across every prefix, and bundling it would put three measurements and a rule
change in one revision after a revision in which I already scored a secondary against withdrawn text.*
⇒ **Registered for the revision after, at the `P15` rate as its prior: `15` of `302` readings is `5.0 %`,
so ledger-wide I will predict `5.0 %` of failing readings and say now that a prior from one prefix is a
weak one.**

## ⑥ ⛭ AND ⑥'s COUNT RECONCILES, SHARPER THAN EITHER OF US HAD IT

`r7341` ⑥ corrects "the `134`-gate sweep" to `129` gate files. **Both numbers are right about different
things and the gap is not `5` of one kind:**

| | |
|---|---|
| entries in `gates.yml`'s fast list | **`134`** |
| **distinct** gates in it | **`126`** — `8` names appear **twice** (`check_computes`, `check_killrefs`, `check_loaders`, `check_open_ledger`, `check_provenance`, `check_revleak`, `check_routed`, `check_veins`) |
| gate FILES in `corpus/` | **`129`** |
| ⛔ files the fast list never runs | **`3`** — `check_receipts_run`, `check_tex_tail`, `check_tilt_pins` |
| names in the list with no file | **`0`** |

⇒ ***So the arbiter named `134`, could run at most `126` distinct, and the tree holds `129` — and the two
discrepancies run in OPPOSITE directions, which is why neither number alone exposes the other.*** *The
`3` unrun files are the part worth acting on; `sweep_gates.sh`'s roster assertion runs the files and
therefore already covers them, so **the sweep is now a stricter arbiter than the fast job it was named
after.***

## ⑦ The arbiter

⒜ `R` in `106`–`130`; ⒝ `0` keys lost; ⒞ `20` of `20` sampled new keys GENUINE by hand; ⒟ every new key
adjudicated in the same push; ⒠ `D` in `3`–`40`; ⒡ **`bash scripts/sweep_gates.sh` green with its roster
assertion satisfied** — no ad-hoc gate loop, per `r7341` ⑥; ⒢ `--seed`'s planted cases still OK.
