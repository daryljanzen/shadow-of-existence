# `r7735+cc66` VERDICT — **THE SPLIT CANNOT BE DONE ON THESE ARRAYS, FOR A STRUCTURAL REASON: THE LEG CALLED "THE PROJECTION" IS ONE SCALAR. AND HOW THAT SCALAR ACTS IS LEFT OPEN, BECAUSE BOTH ONE-PARAMETER PICTURES FAILED THEIR OWN LICENCES**

Order `r7735`, all three items.  Registered at `r7735+cc66.0`, amended at `.1` before the replacement
statistics were run.  Outputs in `which_term_output.txt` and `shifts_output.txt`.

---

## ① ⛭⛭ THE FINDING, AND IT IS A CODE READING RATHER THAN A MEASUREMENT

`r7729_70_dlk_build/project4.py` ll.139–146 take `S`, the `eta` grid, **the distance map `x0(eta)`**
and the tilt `n_s` from the **source** arm in all four combinations.  The **kernel** arm enters through
one scalar, `xs = D_M(kernel)/D_M(source)`.  70's own registration says it in words: *"`SRCXS`'s
definition of **the same source through the other arm's distance**"*.

⇒ *** `r7731`'s two legs are NOT "the projection" and "the source". They are **the ratio of the two
arms' distances to last scattering** and **the two arms' sources together with their distance maps,
`eta` grids and tilts**. ***

| | |
|---|---|
| the kernel leg's whole content | one number, `xs` |
| `xs` for `S_lcdm__K_cr` / `S_cr__K_lcdm` | `1.0128706132848382` / `0.9872929344419445` |
| their product, measured | **`0.9999999999999999`** — exact inverses to `1.11e-16` |

⌗ *The exact-inverse property is the signature of a one-parameter family, and it is not decoration:
by the identity below it is why the two-template fit closes as well as it does at all.*

## ② THE TWO EXACT CLOSURES — and one of them explains `r7733`'s residual

`obs − (t_ker + t_src) ≡ −( t_ker^{S_lcdm} + t_ker^{S_cr} )`, where `t_ker^{S_cr}` is the kernel
template taken on the **cr** source.  Measured departure: **exactly `0`**.

⇒ *** So `r7733`'s residual ratio of `0.0444` is not an unexplained leftover: it IS the two source
arms' kernel templates' departure from exact antisymmetry. *** A one-parameter swap by `xs` and
`xs^{-1}` must be antisymmetric to the extent the two sources agree; it is, to four per cent.

## ③ ⛔ BUT HOW THAT SCALAR ACTS IS **NOT** CHARACTERISED — BOTH PICTURES FAILED, AND THE LICENCES WERE SET BEFORE THE RUNS

| picture | what it models | unbinned | binned | registered licence | |
|---|---|---|---|---|---|
| `M1`/`M1b` | a shift in **wavenumber** — moves the source *and* the Bessel factor | `0.7453` | `0.8999` | `0.10` | ⛔ OVER |
| `M4` | a shift in **multipole** — holds the source still, moves only the Bessel factor | `0.8016` | `0.5962` | `0.30` | ⛔ OVER |

⇒ *** Amendment 1 registered that `M4 > 0.30` **licenses nothing**.  So: neither one-parameter picture
describes the cross term on these arrays, and the characterisation of how the distance ratio acts is
LEFT OPEN pending Tier 1. ***

⌗ **What is suggestive and is NOT a result.**  The multipole shift is the closer of the two on the
binned reading (`0.60` against `0.90`), which is the direction §A1.2 argued for — the real cross term
holds the source at `k`.  ⛔ *It is still over its own licence, so it is reported as a direction and
not as an answer, and the licence is not moved to accommodate it.*

⌗ *`M1`'s failure was the registration's own named risk firing: §3 said in advance that a small `M1`
was "not expected by construction" because the comb's period in `k` is of order the shift.*

## ④ WHAT THE ACCEPTANCE LAW'S NAMED TERMS ARE, AND WHERE THEY SIT — the order's question

`P15` l.1823ff: `G_l(k) = ∫ g j_l(k chi) d eta`, `W_l = G_l^2 dk/k`,
`A_l = |∫ W_l e^{2ik rs*} dk| / ∫ W_l dk`, *"built from the window the kernel reads and the comb's
period, both of them the background's own"*.  Three named terms:

| term | the paper's measure of it | which leg of `r7731`'s fit holds it |
|---|---|---|
| **`g`**, the visibility, and its extent in `chi` | *`15.5` per cent wider on this arm*, which is *"why it retains more"* | **the SOURCE leg** |
| **`chi(eta)`**, the map | acceptance `4.43` against `5.14` of acoustic phase, `13.73` per cent narrower | **the SOURCE leg** (its shape); only its overall scale is in the kernel leg |
| **`rs*`**, the comb period | *"the same sound horizon to `0.36` per cent"* | **the SOURCE leg** |

And the arithmetic the conclusion turns on:

| | |
|---|---|
| the `chi`-extent the kernel leg moves | `1.287` per cent (`|xs − 1|`) |
| the arms' measured `chi`-extent difference | `15.5` per cent |
| ⇒ | **a factor of `12.04`** |

⇒ *** The leg called "the projection" moves the law's own named mechanism by about one twelfth of the
arms' actual difference in it.  So the acceptance law's named terms are ALL in the leg `r7731` called
"the source", and the order's split cannot be performed on these four arrays at all — not because they
are too coarse, but because the kernel index never exchanges any of them. ***

## ⑤ THE PRICE, AND THE REQUEST ROUTED TO 70 — order items ② and ③

**TIER 1 — the distance MAP, not its endpoint.**  Rebuild the four combinations with the *other arm's*
`x0(eta)` array in place of a scalar multiple of the source arm's: `transfer(S_A, eta_A, x0_B, …)`
with `xs = 1`.  Separates **the map's shape** from **the distance normalisation**, which is exactly
what the present cross term conflates — and it is also what would settle ③, since a map swap is not a
one-parameter object.
  * **No new solves.**  `SRCFIELD` already saves `x0` per arm (`r7729`'s `PREDICTION.md` l.12), so the
    fields on the runner, or one re-run of `launch.sh`, carry everything Tier 1 needs:
    `4 × 698 × 1450` quadratures, the same order as `r7729`'s projection step.
  * ⚠ The arms' `eta` grids and `x0` arrays differ in length, so `x0_B` must be read onto `eta_A`.
    **That interpolation is 70's choice to make and declare**, and it is the one place Tier 1 can go
    wrong quietly.

**TIER 2 — the visibility `g`, which is what the law is actually about.**  `G_l(k)` on the four
`(g, chi)` combinations, with `W_l`, `A_l` and each arm's `rs*`, so the three named terms can be
exchanged independently.
  * ⛔ **`g(eta)` is NOT in the saves** — `SRCFIELD` writes `S`, `ee`, `x0`, `kb`, `P`.  So Tier 2
    needs one more output line in the instrument, which is 70's to add.
  * ⌗ *Cheaper per cell than `Dlk`: `g` is a function of `eta` alone, so the integrand carries no `k`
    dependence beyond the Bessel factor.*

⇒ **Tier 1 answers "map shape or normalisation" and would close ③.  Tier 2 answers the order's
question as asked.**

## ⑥ ⛔ WHAT THIS DOES AND DOES NOT DO TO WHAT IS ALREADY IN PRINT

- **`r7731`'s verdict stands.**  Both amplitudes within two per cent of unity, both outside their own
  nulls on all four readings, power `1.000`.  Nothing here touches a number.
- **The landed `P15` sentence's figures are this seat's and stand.**  What ① puts in question is its
  two **names**: *"exchanging the two arms' projections"* names a wider object than the one measured
  (which is the distance ratio alone), and *"exchanging their sources"* names a narrower one (the
  object also carries the arms' distance maps, `eta` grids and tilts — and with them the law's own
  `15.5` per cent).  **The precise names are available and short**: *the ratio of the arms' distances
  to last scattering*, and *the arms' sources together with their distance maps*.
  ⇒ *Whether that is worth a rewording is 69's call. It is put to 69 rather than acted on, and no
  figure changes either way.*
- **It does not say the one-parameter cross term is wrong.**  It is `SRCXS`'s registered definition,
  and `r7731` already recorded that it is a definition and not a post-hoc rescaling.  What is new is
  that a definition with one parameter cannot carry a split into three named terms.

## ⑦ THE PROCESS RECORD

- **`M1` failed its own licence and the characterisation was withdrawn rather than reinterpreted.**
  The registration's `> 0.10` branch was written before the run and was followed.
- **`M4` was chosen after seeing `M1` fail**, which is why it was registered in its own commit and
  pushed before it was computed, with its licence as a number set in advance.  It failed too, and the
  number was not moved.
- ⛔ **A mismatch in my own `r7735+cc66.0` registration is recorded, not resolved silently**: §3 said
  "on the primary binning's live cells" and then wrote `M1`'s formula over ladder nodes, which only has
  meaning unbinned.  Both readings are reported for every statistic and neither is chosen.
- ⌗ *And a smaller one: the blob's `meta` carries two keys spelled `grid` at different depths — a prose
  string at the top level and the scalars under `closure`.  The first read took the prose one.  Caught
  by its own exception rather than by producing a plausible wrong number, which is luck and not
  design.*
