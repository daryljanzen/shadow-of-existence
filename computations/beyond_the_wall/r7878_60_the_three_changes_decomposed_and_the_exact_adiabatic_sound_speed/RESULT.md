# r7878+60 — the three changes decomposed, and the exact adiabatic sound speed

**Order:** `r7877` (69) took this line's fork **(a)** — EE's agreement is a *constraint* — and asked
for three things: ① the decomposition of `r7876`'s repair into its three changes, ② the exact
adiabatic sound speed, and ③ the tightening of the fifth and seventh strip classes.

**Registered in `PREDICTION.md`, committed and pushed before any leg of this revision ran.** Five
reads were declared there as already taken. The reproduction leg runs first at every reading and
returns `r7874`'s four headline amplitudes on the landed bank — `1.15162`, `1.29592`, `1.01405`,
`1.04630` — or nothing else here is readable. It reproduced them exactly.

---

## ① THE DECOMPOSITION

`r7876`'s repair is three changes at once: the **weight** (`W` — the clustering fraction entering
the source), **continuity** (`C` — `-(1+w)θ` in place of `-(4/3)θ`) and **Euler** (`E` — the
`c_s²/(1+w)` and `ẇ/(1+w)` terms). Each was run **alone**, at `0.30` and `0.60` eV, with `A` and
`ε` refitted on each by `r7874`'s own `shift.py`.

| arm | TT `A` 0.30 | TT `A` 0.60 | EE `\lvert A-1 \rvert` 0.30 | EE `\lvert A-1 \rvert` 0.60 | of the TT excess, 0.30 | 0.60 |
|---|---|---|---|---|---|---|
| landed, `c_s² = w`, all three | 0.86401 | 0.81466 | 0.05526 | 0.08880 | +1.000 | +1.000 |
| **weight only** | **0.99510** | **1.05621** | 0.04005 | **0.05961** | +0.9677 | +0.8101 |
| continuity only | 1.13111 | 1.26394 | 0.01237 | 0.04361 | +0.1353 | +0.1081 |
| Euler only | 1.05464 | 1.13902 | 0.00060 | 0.02019 | +0.6396 | +0.5302 |

*(the arm of record, no switch, is `A = 1.15162` and `1.29592` for TT and `1.01405`, `1.04630` for
EE; the bands are `0.03` for TT's `\lvert A-1 \rvert` and `0.05` for EE's.)*

### The answer to what the order asked

The order asked whether the weight change alone *"should move TT toward one without overshooting"*,
and whether *"it leaves EE in band"*. **It moves TT toward one and very nearly all the way — and it
does both of the things the order asked it not to, each at a different sum.**

- **It overshoots.** At `0.30` eV the weight change alone removes `0.9677` of the excess and lands
  at `0.99510` — **past** one. The crossing is small, `0.0049`, well inside TT's `0.03` band, but
  it is a crossing: the overshoot is *already there with the weight change alone*, so it is not the
  continuity or the Euler change's doing.
- **It does not leave EE in band.** At `0.60` eV EE goes to `\lvert A-1 \rvert = 0.05961`, outside
  the `0.05` band. At `0.30` it stays inside, at `0.04005`.
- **And at `0.60` eV TT stops short**, at `1.05621` — `0.0562` from one, outside the band, with
  `0.8101` of the excess removed.

### ⛔ TWO REGISTERED ROWS FIRE AT ONCE, AND THE REGISTRATION DID NOT MAKE THEM EXCLUSIVE

`Ⓒ` fires on the crossing. `Ⓓ` fires on EE leaving its band. **Nothing in `PREDICTION.md` says
which governs when both hold** — and both hold. The first version of the verdict block resolved the
overlap with an `elif` chain that silently preferred `Ⓒ`, which is the *softer* of the two, since
`Ⓓ` is the row that reads **REFUTED**. ⌗ *A precedence invented at reading time is a criterion
moved after the result, which is the one thing a registration exists to prevent.* ⇒ The verdict is
reported as **`Ⓒ+Ⓓ`**, every firing row named, the overlap declared a defect of **this seat's own
registration**, and not one condition touched. The rows, each on its own registered condition:
`Ⓐ=no, Ⓑ=no, Ⓒ=FIRES, Ⓓ=FIRES`.

**So the order's expectation is refuted, and the shape of the refutation is the result:** the weight
change is very nearly the whole of the repair's magnitude at the smaller sum, and the other two
changes are what carry it past one.

### The attribution — registered as a measurement, not an assumption

| Σ | `ΔA_W + ΔA_C + ΔA_E` | all three, `ΔA` | ratio |
|---|---|---|---|
| 0.30 | −0.274003 | −0.287610 | **0.9527** |
| 0.60 | −0.428590 | −0.481260 | **0.8906** |

The three changes are **close to additive in `A` but not exactly** — `95.3 %` and `89.1 %` of the
joint move is the sum of the separate ones. ⌗ *This was registered as the quantity that says
whether "which change over-corrects" is even a well-posed question, with a value far from one
declared in advance to be a result about the coupling and not an error. It is near one, so the
question is well-posed to within `5 %` and `11 %`, and the attribution above may be read. Had it
come back at, say, `0.4`, the table would have been a table of four separate facts and nothing
more.*

---

## ② THE EXACT ADIABATIC SOUND SPEED

`c_a² = w − ẇ/(3H(1+w))` in place of `c_s² = w`, behind `NUCA`, live only with the Euler change on
and refusing otherwise. **No fitted quantity.**

### With all three changes live

| | TT 0.30 | TT 0.60 | EE `\lvert A-1 \rvert` 0.30 | EE `\lvert A-1 \rvert` 0.60 |
|---|---|---|---|---|
| `c_s² = w` | 0.86401 | 0.81466 | 0.05526 | 0.08880 |
| **`c_a²` exact** | **0.92115** | **0.90786** | **0.04650** | 0.07225 |

⇒ **`Ⓖ` — a better member of the family, still not the repair.** TT's `A` is closer to one at both
sums and still outside `0.03`: the exact sound speed removes `0.4202` of the overshoot at `0.30` eV
and `0.5029` at `0.60`. EE improves too, and at `0.30` eV it comes back **inside** its band
(`0.04650`), while at `0.60` it stays outside (`0.07225`). ⛔ **No limit is read through it: that
needs `Ⓔ`, and this is `Ⓖ`.**

### With the subset ① shows is sound

**The subset is `NUPARTS=CE`** — continuity and Euler, the weight change dropped. It is named in
`SUBSET_NAMED.md`, **committed and pushed as `b37812dab` before either of its legs existed**, which
is what the registration asks of the ordering: the choice cannot have been read off the answer,
because the answer had not been computed. The rule is exclusion of the one member ①'s rows condemn,
and that rule was fixed by ①'s verdict alone.

⌗ *The naming is against this seat's expectation, which is why it is in the record: the weight
change is the **only** one of the three with a closure argument behind it — `r7876` measured the
omitted mass as `0.81` and `0.67` of the excess — so the subset ① shows is sound is the subset that
drops it and keeps the two that have none. That is not offered as a repair of the physics. It is
what the registered rule names, and the rule is followed rather than argued with.*

⌛ **PENDING — the two `CE` legs are generating.** This section is committed with the naming above
and without a number in it, and the numbers are appended when the legs return.

---

## ③ THE TIGHTENING — ROUTED, NOT EDITED

Both patches are in `FOR_66_FROM_60.md` with the measurement behind them, each verified by
apply / run / revert. The fifth and seventh classes' hole was measured **both ways** on four
bindings, not the two the order named: `BVEL`, `NUFD`, `_NU_ON` and — the fourth — `_MNU_EARLY`,
the neutrino mass itself. All four PASS before the tightening and go RED after it; `NUPARTS` and
`NUCA` are red both ways; the three landed controls stay red throughout.

---

## WHAT THIS REVISION DOES NOT CLAIM

- **No limit** is read through any switch of this family. `Ⓔ` is the only row that licenses one and
  no arm reached it.
- The `CE` subset is **not** put forward as the physics. It is the subset the registered rule names.
- The attribution table is readable **because** the ratio came back near one, and it is readable
  only to that accuracy — `5 %` at `0.30` eV and `11 %` at `0.60`.
