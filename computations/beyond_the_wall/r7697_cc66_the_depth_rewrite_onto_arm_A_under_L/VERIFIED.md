# `r7697` (cc66) — **THE ROW, THE PAIRING, THE LIKELIHOOD AND THE CROSS-VALIDATION, ALL COMPUTED HERE**

## ⚑ THE PAIRING CHECK — the arm `r7693` lacked, and it passes

*`r7693` was held because I took the order's word for what a bank WAS. This revision's registration says
establish the pairing from the run. Read out of `p15_lowell_depths_armA_leafpert_leafrec1.npz`'s own
`config`:*

```
SPLITCLOCK: {"distances__armA__L": "L", "distances__armA__one_clock_gate": null, ...}
STACKPERT : None
pairing   : "(L): CAMB leaf-rate dynamics (its own Recfast, reionisation tau=0.0544); projection chi,
             visibility measure ... and source Psi on the stacking grid, via HIER SPLITCLOCK=L"
note      : "(L) mirrors STACKPERT unset (LEAFPERT) and VISLEAF=0."
```

⇒ ✔ **The `(L)` rows run `SPLITCLOCK=L` with the retired `STACKPERT` pairing UNSET**, stated by the bank
about its own run. *This is the arm of record's construction, not the mixture.*

## ① WHICH PRINTED DIGITS MOVE — **CONFIRMED**, roundings under both conventions

**My read matches 69's row at every multipole, `max |diff| = 0.0`.**

| | three places | two places (`l.2771`, and `l.134`'s ℓ = 4) |
|---|---|---|
| move | **6 of 7** | **3 of 4** |
| holds | **ℓ = 7** (`0.983`) | **ℓ = 3** (`0.44`) |

`0.487 0.435 0.359 0.666 0.911 0.983 0.998` → **`0.485 0.441 0.354 0.657 0.909 0.983 0.999`**
`0.49 0.44 0.36 0.67` → **`0.48 0.44 0.35 0.66`**

⌗ ⚠ **At `r7693` the multipole that held was ℓ = 8; here it is ℓ = 7.** *So **which** multipole survives is
a property of the row, not of the sector, and a sentence reading "all but one" must name which one.*
⌗ ✔ **Both conventions agree at every place in this row**, so there is no convention question anywhere —
*checked with `decimal` rather than by eye.*

## ② THE LIKELIHOOD — **SIGN PATTERN CONFIRMED, and all four printed terms move again**

| ℓ | printed | arm A `(L)` | one place | moves? |
|---|---|---|---|---|
| 2 | `−2.5` | `−2.557` | **`−2.6`** | yes |
| 3 | `+1.0` | `+0.927` | **`0.9`** | yes |
| 4 | `+2.0` | `+2.160` | **`2.2`** | yes |
| 5 | `+1.0` | `+1.123` | **`1.1`** | yes |
| above | — | `+0.062`, `+0.002`, `+0.000` | — | nothing above |

✔ **The pattern holds: quadrupole rewarding, ℓ = 3–5 penalising, nothing above.**

⚠ **The total: `+1.58 → +1.72`** (`+1.5847 → +1.7168`, a move of `+0.132`, thirteen times the printed
precision), and `2 ≤ ℓ ≤ 8` equals `2 ≤ ℓ ≤ 10` to `+1.7168`, so *"the same to the digit"* **survives**.
⌗ *** AND THE TOTAL MOVED THE OTHER WAY THIS TIME: on `r7693`'s mixture row it fell to `+1.44`; on arm A
`(L)` it rises to `+1.72`. The DIRECTION of the total's move is row-dependent, which is exactly why I
declined to predict it on both rows. *** ⌗ *Had I guessed on either, I would have been right once.*

⚠ **The octopole estimator's range: `+0.2`–`+3.4` → `+0.4`–`+3.5`.** *Its LOW end did NOT move on the
`r7693` row and does here — a fourth printed figure, and one neither order named.*

## ③ THE CROSS-VALIDATION ON `(L)` — **no octopole exception**

| build | ℓ=2 | ℓ=3 | ℓ=4 | ℓ=5 | ℓ=6 | ℓ=7 | ℓ=8 | worst |
|---|---|---|---|---|---|---|---|---|
| **DECOUPLED** | `−2.50` | **`−0.88`** | `−2.91` | `−1.20` | `−0.30` | `−0.09` | `−0.16` | **`2.91 %`** |
| FROZEN | `−4.21` | `−0.73` | `−6.19` | `−2.71` | `−0.66` | `−0.01` | `+0.03` | `6.19 %` |

⇒ ✔ **DECOUPLED is within `2.9` per cent at every ℓ = 2–8 with the octopole at `−0.88`, so there is no
exception** — 69's figures reproduce, FROZEN's `6.19` at ℓ = 4 included.

## ⌗ ONE CORRECTION TO MY OWN WORKING, CAUGHT BEFORE IT LEFT THE SCRATCHPAD

*My first diagnostic **re-derived** the paper's two-place digits from its three-place ones instead of
reading them, and float representation put one of them out — reporting a wrong printed value AND a wrong
verdict for ℓ = 3. Reading the paper fixed both, and also found that the four two-place figures are at
`l.2771`, a line I had not identified.* ⇒ **Don't re-derive a printed digit; read it.** ⌗ *That is the
`108.9` rule and the rounding-boundary rule in a third costume today — caught this time before it
reached a commit.*
