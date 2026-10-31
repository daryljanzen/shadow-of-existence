# r7648 (60) — RESULT

**The order's reachable negative is REACHED: on the tree as it stands the class is cc66's one
instance and nothing else. But the sweep's larger finding is that the class was named by the wrong
property — the discriminator is PINNED against UNPINNED, not absolute against relative — and the
corpus holds `1877` unpinned absolute bounds that no static rule can judge at all.**

Receipt `sweep.py` — **9 checks, 0 FAIL**, 3 s. Twelve arms registered across three passes: **nine
hold, one fires as the order's registered negative, one is a MISS, and one is reported VACUOUS.**
Two of those failures each caught a defect in this revision's **own rule** rather than in the corpus,
and all three withdrawn conditions are kept beside their corrections.

---

## ① What the three passes measured

| | net | reach | blind | candidates / hits |
|---|---|---|---|---|
| pass 1 | raw bound + the receipt's own `V/S·100` normaliser | 517 receipts | **4566** bounds with no normaliser | **2** candidates |
| pass 2 | the bound's **own pin** as its scale | **2585** pinned bounds | 2285 with no printed per-cent | **93** candidates, 40 receipts |
| pass 3 | **unpinned** bounds only | **1877** unpinned bounds | 1749 never named relatively; 128 named but unscaled | **0** hits |

`1140` receipts parsed in each.

## ② The order's negative is reached, and the reach is stated beside it

- **Pass 1's 2 candidates both adjudicate as NOT the class.** Each is a two-sided pin at a measured
  value that a wrong run fails, with the relative claim separately held.
- ⛔ **But that verdict was not reportable**, because the net saw 2 of 4568 — `0.04%` visibility.
  *A sweep that returns nothing at that reach has measured its own reach, not the corpus* — the same
  shape as a guard that cannot fail on the data it is given, which is the third revision running in
  which that shape has had to be caught. Hence pass 2, registered as `r7648+60.1` before it ran.
- **Pass 3 returns 0 hits**, and the seed proves the net is live: cc66's pre-repair
  `abs(d_om) > 0.01` **is** a hit and the repaired form is not. ⇒ **ARM ② FIRES. The class is empty
  outside cc66's one** — on this tree, with the reach above printed beside the verdict.

## ③ ⚑⚑ The finding: the label "absolute bound" is many-to-one, and almost all of it is sound

All 93 of pass 2's candidates, and all 30 of them on a real (non-unity) scale, are **pinned at a
measured value** — which makes an absolute bound two-sided and failable. Three read in full:

- `P15_damping_reabsorption:111` — `abs(dlnob + 0.305) < 0.005` beside the paper's `ω_b^{−0.31}`:
  the bound is **exactly half a printed digit** of the claim, and the per-cent claim beside it has
  its **own** gate on the next line.
- `M2_reabsorption_minimization:73` — `abs(Om_b − 0.1954) < 0.005`, with the relative claim held
  separately by `abs(100·(Om_b/Om_fid − 1) + 36.35) < 1.0`.
- `P15_the_ratio_is_the_onset_in_imported_units:169` — `abs(ratio − 1.72) < 0.05`, two-sided at the
  printed value.

cc66's was `abs(d_om) > 0.01`: **one-sided, pinned at nothing.** ⇒ ***The property that makes a bound
unable to fail for its claim is being UNPINNED, and "absolute" is only how the one instance happened
to present.*** *Before two shapes are identified by a label, check how many-to-one the label is on
the object.* The corpus holds **1877** unpinned absolute bounds; of those, **1749** are never named
relatively by their receipt at all and **128** are named but carry no scale. **So a static rule can
judge essentially none of them**, and the forward protection against cc66's defect is not a sweep
but the convention it repaired to: *a bound pinned two-sided at its measured value*, which
`check_figures_pinned` already enforces wherever the figure is printed.

## ④ ⛔ Two registered arms caught defects in this revision's own rule

- **ARM ⑦ — a MISS, and the useful one.** It registered that neither pass-1 candidate would flag
  under the amendment's automated claim side. One did, at a claimed `P = 0.31` where the field
  actually prints `−36.35`: *a printed field is an EXPRESSION, not a number*, and
  `{100*(Om_b/Om_fid-1):+.2f}%` carries the scale `Om_fid = 0.307`, which the rule read as the
  printed figure. ⇒ Condition ⅲ′ **withdrawn**; no static reading of a printed field's value exists,
  which is what the first registration said when it put the claim side in a human reading.
- **ARM ⑪ — failed first, and its failure is the blind row in pass 3.** The first form admitted
  no-scale cases as hits and returned **128**, nearly all of them bounds like `abs(_rate_a) < 1e-12`
  — tight, and obviously not fail-open. *A bound whose relative size is unknown has not been judged.*
  ⇒ They are **blind**, which is what ⅲ″ already said by *"where a scale is available"*; the
  correction can only **remove** hits and never manufacture one.
- ⌗ *Three rule conditions were withdrawn or corrected and every one was caught by an arm registered
  before the pass ran. That is the whole purpose of registering them, and it is reported as three
  failures rather than smoothed into a clean sweep.*

## ⑤ Ownership, and ARM ⑤ reported VACUOUS

Pass 2's 93 candidates sit in **40** receipts: **89 in `P15_CR_cosmology`**, 4 in
`L557/R1_…`. **None is in this seat's own `S`-band, and pass 3's hit set is empty**, so there is
nothing of this seat's to repair.

⇒ **ARM ④ holds** (the deliverable is a routed list, not a repair) and **ARM ⑤ is reported as
VACUOUS, not as satisfied**: it registered that every hit in this seat's receipts would be repaired
and fail on what the old bound let through, and **there is no instance to score**. *An arm with no
instance is not a pass — the same rule as a guard that cannot fail on the data it is given.*

## Scope

No paper is edited, no figure moves, no parameter is pinned, no quote-pin key is minted, **no gate,
ledger or census is added** — this is a one-off sweep — and no receipt of `70`'s or cc66's is
touched. cc66's own receipt is already repaired by cc66 and is left alone.

## Files

- `PREDICTION.md` — the registration and its two amendments, each committed and pushed before the
  pass it governs was run.
- `sweep.py` — the receipt, all three passes, with every withdrawn condition kept in place beside
  its correction.
- `candidates.json` — all three passes' lists whole, so the adjudication can be checked.
