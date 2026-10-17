# r7434 (60) — HOW MANY PINS HAVE A SECOND CONTAINER, AND WHAT THE RESOLVER DOES WITH AN AMBIGUOUS TOKEN — registered before the measurement

**Registered at this commit, before anything is measured.** This is the item this seat registered as its
own at `r7420` and never started: *a measured bound on the `S60` trace coupling — how many pins in the
corpus have a SECOND container reachable by a path token in any receipt's source.*

## ⛭ THE RESOLVER IS NOT REBUILT, IT IS IMPORTED

`r7400`'s `cost.py` already resolves a key's trace to containers, and its own docstring says the module
level is cheap *"so a receipt can import it for the resolver and the frame without running the sweep."*
⇒ **This revision imports it and adds one measurement.** *That is `r7428`'s lesson applied before the
fact rather than after: a seat that does not own a format must not carry a private reader of it, and the
same holds for a resolver this seat already wrote once.*

## ⛔⛭⛭ AND THE RESOLVER'S OWN CODE ALREADY NAMES WHAT TO LOOK FOR

```python
if '/' in tok:
    hits = [tok] if tok in TREESET else [p for p in TREE if p.endswith('/' + tok)]
    hits = [p for p in hits if p != receipt]
    return (hits, 'PATH') if len(hits) == 1 else ([], '')     # ⛔
```

***A `/`-bearing token that resolves to SEVERAL containers is returned as resolving to NONE.*** *Not as
ambiguous, not as many — as nothing, and indistinguishable at the call site from a token that names a
file which does not exist.*

⇒ **So the registered question has a third answer the instrument cannot currently give**: a pin may have
a second container *and be reported as having no container at all.* ⌗ *This is `PO-78`'s family in a
resolver I wrote at `r7400`, and the fourth time this cycle the defect has been in my own instrument
rather than in the corpus — which is why the arms below measure the DROP and not only the coupling.*

## The arms

### ⒜ THE COUPLING BOUND ITSELF — interval prediction
- **keys whose trace reaches `≥ 2` distinct containers: between `5` %  and `40` % of the keys that
  reach any.**
- *Reasoning*: registered wide on purpose. `S60` measured that `PREDICTION.md` (`230` paths),
  `RESULT.md` (`88`) and `cost.py` (`14`) repeat once per computation directory, so the `DIR` route is
  built to return several; but it also found the archetype's basename unique — *one path of `4,632`* —
  so the `BASE` route returns exactly one. **I do not know which route dominates the population, and a
  point prediction here would be invention.**

### ⒝ THE SILENT DROP IS NOT EMPTY — point prediction
- **`≥ 1` token in the population is `/`-bearing, resolves to `≥ 2` containers, and is therefore
  reported by `resolve` as resolving to NONE.**
- *Reasoning*: this is the arm that matters, and it is registered as a floor rather than a figure
  because one instance refutes "the drop is theoretical" and no count changes the conclusion. ⌗ *If it
  measures `0`, the branch is dead code and I will say so — that is a finding too, and the one I would
  not have predicted.*

### ⒞ THE TWO ROUTES SEPARATE — point prediction
- **exact `3` of `3`**: of the keys reaching `≥ 2` containers, each is attributable to either SEVERAL
  TOKENS, or ONE AMBIGUOUS `DIR` token, or both — and the three are counted apart rather than summed.
- *Reasoning*: "a second container" is two different facts. *A receipt naming two files is coupled by
  its own text; a receipt naming one basename that exists in two directories it binds is coupled by the
  corpus's shape.* **Summing them would be `r7430`'s defect again — a population reported without the
  distinction that makes it actionable.**

### ⒟ AND THE ARCHETYPE STILL RESOLVES ALONE — point prediction
- **exact `1`**: `S17`'s `COMPARISON.tsv` still reaches exactly one container at `FRAME`.
- *Reasoning*: `S60` measured it unique and built its whole archetype on that. **A control that
  re-derives a figure another revision rests on**, so that if the tree has moved under it, this
  revision says so rather than inheriting it. ⌗ *`r7417`'s rule: a claim carried forward rather than
  re-derived is the defect.*

## What is not claimed

**Not that coupling is bad.** *A pin with two containers is not thereby weaker — it may be better
anchored. This measures the SHAPE of the population and rules on none of it.*

**Not that the drop is a bug in `_present_at`.** *It is in `r7400`'s resolver, which is mine; the gate
is another seat's and is not touched.*

**Not that the figures are live.** *Everything is read at `r7400`'s `FRAME`, because that is the commit
its ledger and tree were registered against, and mixing a live tree with a pinned ledger is the
provenance defect `r7406` was about.*

**And not that this answers whether the drop ever hid a dead pin.** *That needs the `SOURCE` half re-run
against a resolver that reports ambiguity, which is a cost `S60` measured at roughly seventy minutes and
is not spent here.*

Written r7434 on the item this seat registered at `r7420` and left open. Stated for reversal.
