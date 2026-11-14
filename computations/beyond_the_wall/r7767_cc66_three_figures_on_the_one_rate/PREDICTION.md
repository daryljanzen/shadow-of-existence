# `r7767+cc66` — REGISTRATION: THE THREE FIGURES `P15` STILL CARRIES FROM THE GEOMETRIC DISTANCE

⛭ **Pushed before a figure is read.** Order `r7767` items 1–3. Item 4 is a reading of `sec:refit-bound`
and carries no registration.

## WHAT IS ALREADY BANKED, AND WHAT MAY NEED A RUN — STATED BEFORE LOOKING

`computations/beyond_the_wall/spectra/` holds `271` files from `ACOUSTIC_two_arm.py`, each carrying
`ls`, `Dl`, `l_A`, `D_M`, `r_s`, `arm`, and `dampx` where a damping scan produced it. Of these, **seven
name a leaf-rate DISTANCES arm**:

> `c54.178_cr_leafrec1_distances`, `cc66_cr_x_h6862_pol_leafrec1_distances`,
> `cc66_cr_x_h686_L2000_leafrec1_distances`, `cc66_cr_x_h686_fluid_leafrec1_distances`,
> `cc66_cr_x_h686_pol_leafrec1_distances`, `p15_lowell_depths_distances_leafrec1`,
> `p15_lowell_depths_distances_oneclock_leafrec1`

⇒ *** **So items 2 and 3 look answerable from arms already on disk, and item 1 may not be: no banked
name carries both a damping scan and the leaf-rate distances.** `R0` below settles that by looking,
and it is registered as a question rather than an assumption — **if item 1 needs a fresh
`ACOUSTIC_two_arm.py` run I say so and launch it idempotently rather than quietly substituting a
proxy.** ***

## `R0` — WHAT THE BANK ACTUALLY CONTAINS (asked before any figure is read)

| row | what is established | licence |
|---|---|---|
| **①** | for each of the seven leaf-distance arms: its keys, its `arm` label, whether it carries `dampx`, and its `ls` range | printed as a table; **no figure of physics read in this row** |
| **②** | ⇒ which of items 1–3 are answerable from the bank and which need a run | stated per item, with the file named. ⌗ *If an item needs a run, the row says so and the run is registered separately before it starts* |

## `R1` — ITEM 1: THE DAMPING-SCALE SIGNATURE ON THE LEAF RATE

`sec:coherence` carries it, and the abstract now says its size *"remains to be recomputed"*.

| row | expectation | licence |
|---|---|---|
| **③** | the signature's size with `D_M` on the leaf rate — **the same rate as the Silk scale** — against its stacking-rate value | both sizes printed with the statistic the existing receipt uses, read by path and not reimplemented; **the row reports whether the signature SURVIVES and at what size, and names the outcome either way**. ⌗ *It is registered WITHOUT a predicted direction: the point of the order is that the geometric distance and the Silk scale were on different rates and now are not, so the signature may shrink, hold, or grow* |

## `R2` — ITEM 2: THE COMB, AND THE ANGLE-ALONE `H₀`

`P15` prints `299.1` against the sky's `298.4`.

| row | expectation | licence |
|---|---|---|
| **④** | the comb on the leaf-rate-distance arm, against `299.1` and the sky's `298.4` | the comb refitted from the banked arm's `ls`/`Dl` by the **same `fit_comb` the existing receipt uses**, read by path; all three numbers printed |
| **⑤** | and the angle-alone `H₀` that arm implies, against what the stacking-rate arm gives | both printed with the relation used, which is `l_A`, `D_M` and `r_s` from the arm's own keys and nothing fitted |

## `R3` — ITEM 3: THE LOW-MULTIPOLE TRANSFER'S PROJECTION

`sec:scope` item 2 says *"the projection on the stacking rate"*.

| row | expectation | licence |
|---|---|---|
| **⑥** | the low-multipole depths with the projection on the leaf rate, against the stacking-rate depths | the two banked `p15_lowell_depths_*` arms compared depth by depth; **the row fires on a DIFFERENCE being reported, not on its sign** |
| **⑦** | ⇒ whether the depths move, and by how much against the sky's own uncertainty where the receipt that prints them states one | stated; **if no uncertainty is stated in the corpus I say that and report the move bare rather than inventing a significance** |

## ⛔ AMENDED AT `r7767+cc66.1` — **`R0①` WAS THE WRONG QUESTION, AND THE `_distances` ARMS ARE NOT THE ONE-RATE ARMS**

`R0①` asked for each leaf-distance arm's **keys**. That was insufficient: the answer lives in each arm's
`config`, which `R0①` did not read. Reading them:

* ⛔ **`cc66_cr_x_h686_L2000_leafrec1` and `cc66_cr_x_h686_L2000_leafrec1_distances` have BYTE-IDENTICAL
  configs** — same `ARM`, `KFAC`, `LEAFGEOM`, `LEAFREC`, `LEAFSCALES`, `LMAXL`, `NODRIVE`, `STACKPERT`,
  `VISLEAF`, `ZSTART`, and the same `instrument_blob`. **The `_distances` suffix records nothing in the
  config**, so what it varied is not recoverable from the bank.
* ⛔ **And both have `"LEAFGEOM": false`.** `ACOUSTIC_two_arm.py` l.235 is explicit: **`LEAFGEOM=1` is the
  flag that puts "the conformal-time grid and the comoving distance on the leaf rate"**, while
  `LEAFSCALES` moves `r_s` and `r_D` and `LEAFPERT` the perturbations. ⇒ *** **So neither of the arms I
  took for the pair has the projection's distance on the leaf rate at all. Had the row passed on my first
  reading I would have reported the comb's move from a pair that does not contain the change.** ***
* ⛭ **The real one-rate arms are two, and they are findable only by config:**
  `r7749_leafgeom_nofit_L2000_cr` and `r7749_leafgeom_refit_verify_cr`, both `LEAFGEOM=true`,
  `LEAFREC=true`, `LEAFSCALES=true`, `LMAXL=2000`.

| row | replacement | licence |
|---|---|---|
| **`R0①′`** | every banked arm is classified by its **`config`**, not its name: `LEAFGEOM`, `LEAFREC`, `LEAFSCALES` printed, and the arms with `LEAFGEOM=true` named | the count printed; `271` files scanned |
| **`③′`**, **`④′`** | item 2's pair is **`cc66_cr_x_h686_L2000_leafrec1`** (`LEAFGEOM=false`) against **`r7749_leafgeom_nofit_L2000_cr`** (`LEAFGEOM=true`), matched on `LEAFREC`, `LEAFSCALES` and `LMAXL`, so **`LEAFGEOM` is the only difference** | both configs printed side by side and asserted to differ in `LEAFGEOM` **alone**; the comb from each |
| **`⑥′`** | item 3's depths likewise, and **if no `LEAFGEOM=true` depths arm exists the row says the item needs a run rather than using a `_distances` arm** | the depths arms' configs printed; the answer stated either way |
| **`⑧`** | ⛔ **NEW: the comb locator must not be grid-quantised.** My first form read integer combs (`298.000`, `297.000`) off a `Δℓ = 2` grid, which is the grid speaking | the located peaks refined sub-grid (parabolic on three points) and the refinement's effect printed; the row fires if any located peak lands exactly on a grid node to machine precision across all arms |

⛭ **Reported, not fixed here: the bank's naming is a trap.** `_distances` reads as "the distances moved"
and the config says otherwise. Another seat reading the filenames would make the mistake I made. **69's to
rule whether those files are renamed or a README note is enough** — I am not renaming another seat's
banked data.

## WHAT THIS REGISTRATION DOES NOT LICENCE

* **No new fit, no new parameter.** Every number comes from a banked arm or from an instrument read by
  path. If an item cannot be answered that way, the row says so.
* ⛔ **No substituting a near-miss arm for the one an item needs.** `cc66_cr_x_h686_pol_leafrec1_distances`
  is not the damping scan, and `R0②` must say so out loud rather than letting `③` quietly use it.
* **No claim about what `P15` should then say.** The order asks for figures and a list; the prose is 69's.
* **No paper edits**, and no receipt minted until the figures are in hand and `R0` has named their source.
