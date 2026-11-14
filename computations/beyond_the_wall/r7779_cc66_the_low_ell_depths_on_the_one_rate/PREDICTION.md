# `r7779+cc66` — REGISTRATION ONLY: the low-multipole depths on the one rate, item ① of `r7779`

**Registered before a single depth value is read.** What is read below, at registration time, is the
bank's *metadata* only: the `config` and `manifest` dictionaries, the key names, the array shapes,
and the instrument's own source. No depth array has been opened.

## The switch, as 69 named it

`storyboard_receipts/HIER_photon_hierarchy.py`:

- **One rate** = `ARM` unset **and** `SPLITCLOCK` unset. `Hub` is then the content-carrying leaf
  rate for everything — grid, conformal time, projection distance, ionisation history, dynamics.
  The file says so itself: *"With ARM unset this file runs ONE rate for everything"*.
- **`SPLITCLOCK=L`** = the arm of record's own construction: `Hub` becomes the radiation-free
  stacking rate (grid, `eta_onset`, `rs_f`, `D_M`), `_Hrec` keeps the leaf rate for `xe_history`,
  and `_rhs` reads `_Hdyn` = the leaf conformal rate with output multiplied by
  `Jac_of = H_stack/H_leaf`.
- `SPLITCLOCK=1` is the *retired* pairing (`STACKPERT`): stacking-rate dynamics against
  leaf-normalised content fractions. **It is not the arm of record and is not read here.**

A **depth**, in this bank, is the ratio of the boundary-quantised discrete sum to the continuum
integral **of the same transfer** at the same $\ell$ — the low-$\ell$ deficit. `depth → 1` is
recovery. The banks carry $\ell = 2 \dots 8$, one depth per $\ell$, and a `recovery_definition` of
*"first $\ell \ge 5$ with depth $\ge 0.99$"*.

## ⚠ A correction I owe before any row: my `r7767` reply was too strong

I reported that item 3 *"needs a run the bank cannot stand in for"*. **With the switch named that is
wrong, and the registration says so up front.** What was true is narrower: the pair *I* had looked
at differed by parameter point, and I could not identify the projection switch. Once the switch is
`SPLITCLOCK`, the bank's key names resolve — `__L` against `__one_clock` — and clock-only pairs are
already banked. R0 and R1 below establish exactly how many and where, and R1 isolates the one pair
that is **not** clock-only, which is the very pair 69's order names.

## The rows

**On licences.** Depths are strictly positive and bounded away from zero over $\ell = 2\dots8$, so a
*relative* comparison is licensed here and the standing absolute-bound rule (for rows where both
expressions vanish somewhere in range) does not bite. Where a row compares a depth *difference*
against a *reference move*, the reference is the projection distance's $-0.4984\,\%$ measured at
`r7767`, not a round number.

### R0 — the bank holds at least three CLOCK-ONLY pairs, at both parameter points

| where | one rate | arm of record |
|---|---|---|
| arm A, distances' point | `distances__armA__one_clock_gate` | `distances__armA__L` |
| arm A, refit point | `refit__armA__one_clock_gate` | `refit__armA__L` |
| arm B frozen, refit point | `refit__armB_frozen__one_clock` | `refit__armB_frozen__L` |
| arm B decoupled, refit point | `refit__armB_decoupled__one_clock` | `refit__armB_decoupled__L` |

**PREDICT** four such pairs, each inside a *single* `.npz`, and within each pair every `config`
field equal except `SPLITCLOCK` — same instrument blob, same point, same per-row numerics.

**FAILS IF** fewer than four pairs resolve, or any pair differs in a field other than `SPLITCLOCK`.

### R1 — the pair the order names is the ONE that is not clock-only: its instrument blobs differ

`distances__armB_frozen__L` / `distances__armB_decoupled__L` live in
`p15_lowell_depths_leafpert_leafrec1.npz` at `HIER_blob = c66bfff27…`; the one-clock leg at the same
point lives in the separate `p15_lowell_depths_distances_oneclock_leafrec1.npz` at
`HIER_blob = 5936a51b8…`.

**PREDICT** the two blob strings are unequal, and the working tree's current blob equals the
`leafpert` file's — so the one-clock leg at the distances' point is the older instrument.

**FAILS IF** the blobs are equal, or the current blob matches the one-clock file instead.

### R2 — but the blob difference is INERT with `SPLITCLOCK` unset, and that is checkable textually

The instrument's own claim is *"UNSET or =1: `_Hdyn` is the same object as `Hc_of`, no Jacobian —
byte-identical."*

**PREDICT** every line that differs between blob `5936a51b8…` and blob `c66bfff27…` is either a
comment or docstring line, or sits on a path reachable only when `_SPLIT` or `_SPLITL` is true. So
no difference lies on the unconditional path, and the distances-point pair is licensed as clock-only
*after all*, by reachability rather than by provenance.

**FAILS IF** any differing executable line is reachable with `SPLITCLOCK` unset and `ARM` unset.
**This row is the one that can overturn the order's own pairing, so it is the row I most expect to
have to report against myself.**

### R3 — the depths move by LESS than the projection distance that carries them

The projection distance moves $-0.4984\,\%$ between these two rate choices (`r7767`, item 2). The
ladder's sampled modes go as $L/\chi$, so a depth that merely tracked its own sampling would move by
of order that.

**PREDICT** at every $\ell = 2\dots8$, in **every** clock-only pair of R0,
$|{\rm depth}_L/{\rm depth}_{\rm one} - 1| < 0.004984$ — strictly smaller than the distance's own
move, i.e. the deficit is *more* clock-insensitive than the ruler that projects it, which is the
same structure item 1 found for $r_D/r_s$.

**FAILS IF** any $\ell$ in any pair moves by $\ge 0.4984\,\%$. *I am registering the sharp threshold
rather than a safe one: if the depths move by more than their own projection distance, that is the
finding and I will report it against this row.*

### R4 — the recovery multipole does not move

**PREDICT** the first $\ell \ge 5$ with depth $\ge 0.99$ is the **same** $\ell$ under both clocks, in
every pair of R0 — and, where no $\ell \le 8$ reaches $0.99$, it fails to do so under both.

**FAILS IF** the recovery multipole differs between clocks in any pair.

### R5 — the frozen/decoupled cross-validation survives the clock

The receipt's own standard is that the frozen and decoupled arm-B variants agree to $3\,\%$.

**PREDICT** at the refit point that agreement holds under the one rate as well as under (L): both
$\max_\ell |{\rm frozen}/{\rm decoupled} - 1| \le 0.03$.

**FAILS IF** the one-rate agreement exceeds $3\,\%$ where (L)'s does not.

### R6 — the distances-point pair, read ONLY on R2's licence

**PREDICT** with R2 green, the distances-point arm-B pair gives the same verdict as R3 and R4.
**This row is explicitly conditional:** if R2 goes red, R6 is withdrawn, not reported, and the
one-clock leg must be re-banked on the current blob before the pair means anything.

**FAILS IF** it is reported without R2 green.

### R7 — what is NOT claimed

No new instrument run is registered here. If R2 goes red, or if R0 resolves fewer pairs than
predicted, the re-bank is a **separate** registration with its own `PREDICTION.md`, per
*register before computing*. The refit point's need is then 69's call, as the order allows.

## Failability

R0/R1 move under any edit to a bank's `config`. R2 moves under any edit to either blob — and in
particular would go red if a future `SPLITCLOCK` change touched the unconditional path. R3/R4/R5/R6
move under any change to the banked depth arrays. R7 is a scope declaration and carries no number.

---

# AMENDMENT `r7779+cc66.1` — written after the first run, which took R3 down

**R3 is RED and the registered direction was wrong, by a factor of four.** I predicted the low-$\ell$
depths would move by *less* than the $0.4984\,\%$ their projection distance moves. They move by up to
**$1.976\,\%$** — about **four times more** — and the sign **alternates** across $\ell = 2,3,4$
($-1.4\,\%$, $+1.5\,\%$, $-1.3\,\%$ in the arm-B frozen pair), which no rescaling of a single
distance can produce. *That reshaping is the answer to item ③'s question, and it is the opposite of
what items ① and ② found for the damping signature and the comb.* **The row stands as registered and
is reported against me; nothing about it is relocated.**

Three further amendments, each saying plainly what it is responding to:

### R2′ — replaces R2's test, which was defective (the row, not the claim)

R2 asked that every differing *executable* line "name one of the split tokens". **That test fails any
rename regardless of inertness:** the removed lines `Hc=Hc_of(e)` and `return out` of course name no
split token — they are the lines being *replaced* by guarded ones. The claim was right and the
instrument's byte-identity holds; my formulation of it could not have passed.

**R2′ asserts the claim properly, by normalised AST equality.** Parse both blobs, and on each tree:
rename `_Hdyn` → `Hc_of`; reduce every `IfExp` whose test is `_SPLITL` to its `orelse`; delete every
`If` statement whose test is `_SPLITL`; delete the `_SPLITL` and `_Hdyn` bindings; and reduce
`(A or _SPLITL)` to `A`. **PREDICT the two normalised trees are IDENTICAL** — i.e. with `SPLITCLOCK`
unset the newer blob *is the same program*, not merely a program that behaves the same.
**FAILS IF** the normalised dumps differ anywhere. The runtime arm (every rate spline the dynamics
read, bit-identical, `_Hdyn is Hc_of`, `Jac_of` never defined) is kept as an independent second arm.

### R5′ — replaces R5's implementation, which was stricter than R5's own registration

R5 registered: *"FAILS IF the one-rate agreement exceeds $3\,\%$ where (L)'s does not."* The code
tested `both ≤ 3%`, which is a different and stronger claim. Measured: **(L) $3.39\,\%$, one rate
$3.51\,\%$ — both exceed $3\,\%$.** So the registered condition is *not* met: the clock does not
break the cross-validation. **R5′ asserts what was registered** (the one rate does not degrade the
frozen/decoupled agreement relative to (L) by more than the grain), **and reports the absolute level
as a separate finding for 69:** the receipt's $3\,\%$ standard was established at its own point and
build; at the refit point these leafpert banks sit at $3.4$–$3.5\,\%$ under *both* clocks.

### R8 — POST-HOC, NOT A PREDICTION: the move decomposes, and it is mostly the PROJECTION

Registered honestly as what it is: **this was read off the first run, not predicted.** Arm A carries
**CAMB's leaf-rate dynamics in both rows**, so its pair changes the *projection clock only*; arm B
changes projection *and* dynamics. Comparing the two pairs therefore splits the move. R8 asserts the
split exists and is projection-dominated, with the arithmetic shown; it is offered to 69 as a reading,
not as a discharged prediction.
