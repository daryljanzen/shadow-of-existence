# r7878+60 — REGISTRATION

*Register-before-measure. Committed and pushed before any measurement of this revision runs.
Nothing above a marked ADDENDUM is changed after a result lands.*

**On order `r7877` (69), items ①, ② and ③.** ④ — the lean as a separate object — is next once ①–②
land and is **not** registered here.

---

## ⌗ READS TAKEN BEFORE THIS REGISTRATION — DECLARED

1. **Order `r7877` in full**, including its ruling on this seat's fork — **EE's agreement is a
   constraint the repair must respect** — and its expectation for ①: *"The weight change alone adds
   exactly the mass the closure says is missing, so it should move TT toward one without
   overshooting."* That expectation is what ① tests, and it must be refutable.
2. **`r7876`'s own record**, for the four amplitudes the decomposition is read against:
   `A = 0.86401` and `0.81466` in TT with all three changes live, `0.94474` and `0.91120` in EE,
   against the landed `1.15162`, `1.29592`, `1.01405` and `1.04630`.
3. **`r7876`'s closure measurement**, for what the weight change alone is supposed to supply: a
   deficit of `2.024528e-03` of the total gravitating density at recombination at `Σ = 0.30` eV and
   `7.544464e-03` at `0.60`.
4. **`r7876`'s shear-arm spread**, `0.0037550` and `0.0036366` in `A` — two per cent of the
   overshoot — which is why the ladder is **not** a component of this decomposition.
5. **The instrument's own `NUPERT` block**, to establish that the three changes can be made
   separately selectable **without disturbing any `if NUPERT: <new> else: <landed>` structure**, so
   that the eighth strip class keeps working unchanged and only new switch bindings are added to it.

No spectrum of this revision has been computed. No `A` has been refitted.

---

## ① THE DECOMPOSITION

### How it is made selectable, and why that way

Three new switches, each live only under `NUPERT=1` and each defaulting to **ON** there, so that
`NUPERT=1` alone is exactly `r7876`'s run:

| switch | what it turns off | default under `NUPERT=1` |
|---|---|---|
| `NUPW` | the species' own Fermi–Dirac **weight** in the potential's source | on |
| `NUPC` | the `(1+w)` **continuity** generalisation | on |
| `NUPE` | the **Euler** generalisation — both drag terms and `c_s²/(1+w)` | on |

**⛔ The selection goes INSIDE the existing `if NUPERT:` branches, and no `else` branch is
touched.** That is deliberate: the eighth AST strip class reduces `if NUPERT: <new> else: <landed>`
to its landed `else`, so leaving every `else` byte-identical means the class keeps working and only
the new top-level bindings need adding to its exact-value map. A design that re-shaped those
statements would turn two shared receipts red for a second time in two revisions.

### The arms

Six runs: `{W only, C only, E only} × {0.30, 0.60}` eV, with `A` and `ε` refitted for **TT and EE**
on each by `r7874`'s own `shift.py`, executed with its two lines rebound as `r7876` did, and with
its reproduction leg required to return `1.15162`, `1.29592`, `1.01405` and `1.04630` on the landed
bank **before** any repaired leg is read.

### REGISTERED OUTCOMES for the weight change alone — the order's own expectation, refutable

Let `A_W` be TT's amplitude with the weight change alone.

| | condition | verdict |
|---|---|---|
| **Ⓐ** | `A_W` lands in `[1 − 0.03, 1.03]` at both sums **and** EE stays inside `\lvert A-1 \rvert ≤ 0.05` | **the order's expectation holds: the weight change alone is the repair** |
| **Ⓑ** | `A_W` moves toward one at both sums without crossing it, but stops outside `0.03` | **right direction, not enough** — the fraction of the excess removed is reported per sum |
| **Ⓒ** | `A_W` **crosses** one at either sum | **the weight change alone already overshoots**, so the overshoot is not the continuity or Euler change's doing |
| **Ⓓ** | `A_W` moves away from one at either sum, or EE leaves its band under the weight change alone | **the order's expectation is REFUTED**, and that is the finding |

**⛔ Ⓒ and Ⓓ are the states `r7876` taught this seat to enumerate.** The previous registration offered
only "falls toward one" and "does not move", and the repair did neither; this one names the crossing
explicitly, for each component separately.

*The continuity-only and Euler-only arms are reported the same way but carry no registered
expectation: they are measured to attribute the overshoot, not to pass or fail.*

### The attribution, stated as arithmetic before it is run

With `ΔA_X = A_X − 1.15162` at `0.30` eV (and likewise at `0.60`) for each component `X`, the sum
`ΔA_W + ΔA_C + ΔA_E` is compared against the all-three `ΔA = 0.86401 − 1.15162`. **Registered as a
measurement and not as an assumption:** the three changes need not be additive in `A`, because `A`
is a fitted amplitude and the equations are coupled. The ratio
`(ΔA_W + ΔA_C + ΔA_E) / ΔA` is reported, and **a value far from 1 is a result about the coupling,
not an error** — it is the quantity that says whether "which change over-corrects" is even a
well-posed question. ⌗ *This is the guard about labels applied before the fact: before the overshoot
is attributed to one change, check that it decomposes at all.*

---

## ② THE EXACT ADIABATIC SOUND SPEED

Behind `NUCA`, live only under `NUPERT=1` with the Euler change on, and refusing otherwise:

```
c_a²(a) = w − ẇ / (3 H (1+w))        in place of    c_s² = w
```

with `w = NUW_of`, `ẇ = dw/dη` from its own spline derivative, and `H` the conformal rate the
perturbation equations already use. **No fitted quantity.** It is the next member of the same
Fermi–Dirac family and it is named in the code and the record.

### The arms

`NUCA=1` with **all three** changes live, at `0.30` and `0.60` eV; and again with whichever subset ①
shows is sound — chosen by ①'s verdict and **not** by which subset gives the better `A`. ⌗ *The
subset is named in the result before its `A` is quoted, so the choice cannot be read off the answer.*

### REGISTERED OUTCOMES — EE-constrained, per 69's ruling on the fork

| | condition | verdict |
|---|---|---|
| **Ⓔ** | TT's `A` within `0.03` of 1 at both sums **and** EE inside `\lvert A-1 \rvert ≤ 0.05` at both | **the repair is the physics; the arm of record may follow** |
| **Ⓕ** | TT's `A` inside `0.03` at both sums but EE **outside** its band | **refused by the constraint**, not by TT — reported as such, and no limit is read |
| **Ⓖ** | TT's `A` closer to one than `c_s² = w` gave at both sums but still outside `0.03` | **a better member of the family, still not the repair** — the improvement is reported as a fraction |
| **Ⓗ** | TT's `A` no closer to one than `c_s² = w` gave at either sum | **the family is the wrong direction**, and that is the finding |

**⛔ No limit is read through any switch unless Ⓔ. ⛔ The thresholds are the ones `r7876` was judged
on and are not moved.**

---

## ③ THE TIGHTENING PATCH, ROUTED AND NOT LANDED

69 asked for the hole this seat found to be closed in the **fifth** (`BVEL`) and **seventh**
(`NUFD`) strip classes as well: both strip a switch's binding **by name**, so a later change of that
switch's default to ON would be invisible to the hatch.

Measured before routing, the same three ways the eighth class was:

- **the fixed point** — with both classes on exact-value matching, the working tree still reduces to
  the banked blob;
- **the floor** — the tightening does not make the reduction depend on something else;
- **the controls** — moving `BVEL`'s default to `'1'` keeps the row red, and moving `NUFD`'s does
  too. **Both are registered as arms that must FIRE on the landed by-name shape and must be red
  after the patch.**

**⛔ The two receipts are shared and are NOT edited here.** The patch is routed with its diff, after
being applied locally, run, and reverted.

---

## ⌗ WHAT WOULD MAKE THIS REGISTRATION WRONG

- A component arm that does not reduce to `r7876`'s run when all three are on.
- `NUPERT=1` with no component switch set not reproducing `r7876`'s four amplitudes exactly.
- Any `else` branch of an `if NUPERT:` statement differing from the landed one, which would turn the
  two blob receipts red again.
- `NUCA=1` running without the Euler change rather than refusing.
- A threshold in any table above being different in the result than it is here.
- The subset for ② being chosen after its `A` was seen.
