# r7828 (60) — PRE-REGISTRATION: `PO-24` recomputed at the paper's own configuration

**Order `r7823` (69):** *"① Recompute `PO-24`'s figures **at `r = 0.9918` with `α = 1.70`**, the
paper's configuration, on `L824_lcdm_L3200_nk960`, in one revision: the displacement on each window,
the five absorber fits, and the joint-arm distance. ② Rewrite `P15` `sec:coherence`'s `PO-24`
paragraphs as one state at that configuration. ③ Rename the receipt. Ask `70` for any bank that needs
rebuilding."*

Committed and pushed **before** anything is recomputed.

---

## 0. WHAT THE ORDER CORRECTS, AND IT IS THIS SEAT'S ERROR

`r7826` called `r = 1.0926` *"the ratio priced on the rate the universe has"* and wrote that the
joint data exclude *"the ratio priced on the one rate"*. **Neither is so**, and `69` traced it: that
figure comes from `C10_highl_ratio.py`, a computation on the **radiation-free** rate, and `C10`'s own
later correction moved even that number to `1.0816`. *The ratio on the one rate, at the paper's
endpoint, is `0.9918`.* ⇒ **So my sentence said the construction's own rate is excluded at `27σ`,
which is false** — and the receipt's name still states the error.

**And the error reaches the whole row.** Every `PO-24` figure since `r7471` was scored at
`r = 1.0926` with exponent one: the displacement, the five absorber fits, the joint-arm distances.
`69`'s ruling separates what that does and does not touch, and this revision measures both rather
than inheriting either:

- the **overlaps** are properties of the signature's *shape*, which the paper shows is the same at
  both ratios (the tilt takes seven tenths at either) — **so they should survive, and Ⓕ⑥ measures
  whether they do**;
- the **affordabilities and survivals** are properties of its *size*, and the size at `0.9918` is a
  small fraction of that at `1.0926` **with the opposite sign** — `r² − 1` is `−0.0163` against
  `+0.1938`, and the faithful route's `α = 1.70` carries `−0.0277` against `+0.1938`.

⇒ **That is why Ⓗ⑧'s negative is the one that matters: a parameter that could not afford the old
signature may well afford a signature a seventh its size, and if one does, the inherited-parameter
route `r7814` closed is REOPENED at the paper's own configuration.** It is registered as a
comparison, not predicted either way.

---

## 1. THE CONSTRUCTION, FIXED BEFORE THE MEASUREMENT

- **The configuration:** `S(ℓ) = exp[−α(r² − 1)(ℓ/ℓ_D)²]` at `r = 0.9918`, `α = 1.70`, both read
  out of `corpus/CR_cosmology.tex` by the sentences that carry them, as `r7826`'s receipt already
  does, rather than hardcoded here.
- **The control:** `L824_lcdm_L3200_nk960`, amplitude-normalised to `plik_lite` TT exactly as every
  earlier revision normalises its control. `L820_lcdm_L2512_nk800` is kept beside it so that the
  control swap and the configuration change are never credited with each other's movement (Ⓙ⑩).
- **`ℓ_D` is a property of the CONTROL**, not of the ratio, so it is **measured on `L824`** by the
  same damping fit the harness uses, and printed beside `r7611+70`'s inherited `1489.5783` (Ⓑ②).
- **The banks** are the five already banked — `r6897_wb`, `r7801_neff`, `r7801_yhe`,
  `r7805_alens`, `r7809_omm` — each entering as a **ratio to its own centre**, which is why a change
  of control is legitimate without rebuilding them. Every one reaches `ℓ = 1996`, above every window
  used (Ⓒ③).
- **The windows:** the three published ones, `100–1758`, `700–1760`, `1000–1760`.
- **The fits** are the harness's own: `fit2` the tilt alone, `fit3` the tilt with the parameter, the
  survival `|Δn₃|/|Δn₂|`, the absorbed share `1 − χ²/χ²_amp`.

---

## 2. THE ARMS — each a comparison, each with a reachable negative

**Ⓐ① The probe reproduces the LANDED figures at the OLD configuration on the OLD control.** The
three displacements and the five survivals as `r7804`, `r7806`, `r7808`, `r7812` and `r7814`
printed them. *Negative, reachable:* it does not, and then this is a different harness and **nothing
measured below may be set beside the landed numbers** — reported as that, not patched.

**Ⓑ② `ℓ_D` measured on `L824`, beside the inherited `1489.5783`.** *Negative, reachable:* it moves
far enough to change a verdict, in which case the inherited value was load-bearing for every figure
in the row and that is the finding.

**Ⓒ③ Every bank's reach covers every window used.** *Negative, reachable:* one does not, and then
`70` is told **exactly which** bank needs rebuilding on `L824`'s reach, as the order instructs.

**Ⓓ④ The size at the two configurations, computed and not quoted.** `r² − 1` at `0.9918` against at
`1.0926`, and each multiplied by its own `α`. *Negative, reachable:* the ratio of sizes is not what
`69`'s ruling assumes, and then the ruling's premise is reported as measured rather than accepted.

**Ⓔ⑤ The displacement on each published window at the paper's configuration.** *Registered as a
comparison:* whatever it is, it is reported beside the old figure for the same window.

**Ⓕ⑥ The signature's SHAPE is the same at both ratios.** The share of the signature a single tilt
takes, measured at both. *Negative, reachable and it would matter:* the shares differ, in which case
the overlaps CANNOT be inherited and the screen has to be rerun at the new configuration before any
affordability is read.

**Ⓖ⑦ The five absorber fits at the paper's configuration** — survival and absorbed share, per
parameter, per window. *Registered as a comparison against the landed values.*

**Ⓗ⑧ THE AFFORDABILITIES, and this is the arm that can reopen the row.** Each parameter's wanted
value against its own published constraint: `ω_b` on nucleosynthesis, `N_eff` against `2.99 ± 0.17`,
`Y_He` against `0.2471 ± 0.6 %` and `0.2453 ± 0.0034`, `A_L` against `1.243 ± 0.096` and
`1.180 ± 0.065`, `ω_m` against `σ = 0.004543`. *Negative, reachable, and it would overturn
`r7814`'s closure:* a parameter that could not afford the old signature affords this one, because
this one is a seventh the size.

**Ⓘ⑨ The joint-arm distance at the paper's configuration, on `L824`.** The arm `r7820` built, with
`r7826`'s support split. *Registered as a comparison;* the refit figure `r7823` adopted
(`Δχ² = +9.02`) is `r7826`'s and is cited, not recomputed here.

**Ⓙ⑩ The two axes separated.** The control swap `L820 → L824` at FIXED configuration, and the
configuration change at FIXED control, each measured on its own. *Negative, reachable:* they do not
decompose — the joint movement differs materially from the sum — and then neither may be quoted
alone.

**Ⓚ⑪ Arm count asserted at the end: eleven.** Any arm that fails is reported **as failed**, with its
criterion unchanged from this file.

---

## 3. What this revision does NOT do

It does not touch another seat's receipt, the instrument, or any gate. Item ② of the order — the
`sec:coherence` rewrite — and item ③ — the rename of `r7826`'s receipt — are carried in the same
revision as this measurement, because `69` ordered them together and the paragraph cannot be written
before the figures exist. **This file contains no result.**
