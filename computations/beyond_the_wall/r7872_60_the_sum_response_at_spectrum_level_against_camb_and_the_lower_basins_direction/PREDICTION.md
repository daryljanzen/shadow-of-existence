---
kind: PREDICTION
revision: r7872
node: 60
order: r7871
---

# r7872 — REGISTERED BEFORE MEASUREMENT

**This file is committed and pushed before any computation of this revision exists.** Every arm below
is a COMPARISON with a reachable negative, not an expectation. An arm that fails is reported AS
failed, with its criterion unmoved.

⌗ **The standing rule this line works under:** *if an arm's number or scope can be moved by another
revision landing, it is a reading and the claim is something else.* Every number below is read off
banks already committed to `main`, or off `r7870`'s and `r7869`'s committed JSON, so nothing here
moves when another seat lands.

---

## Reads taken BEFORE this registration, declared

1. The order `r7871` in full, including its table of four calibrated rungs and its named candidate
   (how the perturbations carry the neutrinos: the clustering matter losing ω_ν at all times, and no
   free-streaming scale). **The candidate is the order's, not a finding of this revision**, and this
   registration does not assume it.
2. The structure of the three committed banks — which points exist, that each carries `Dl`, `Dl_EE`
   and `Dl_TE`, and that all three share the same 238 multipoles from 100 to 1996 in steps of 8.
   **Only the key structure was read, not any spectrum.**
3. That the two banks needed for the NUFD contrast are the landed one (no repair) and the separating
   one (repair on, no offset), and that both carry the control arm's full sum series.
4. `r7870`'s committed `second_basin.json`, for the two basin vectors at 0.400 eV. Their five
   components were read; **which parameter each component IS has NOT been established, and
   establishing it is arm Ⓑ②ᵃ below.**
5. The instrument's own `phys(x4, sum)` and the profiler's start vector, which together say the fit
   is over four parameters in grid steps plus one more component. **The identification of the slots
   is exactly what Ⓑ②ᵃ must check and is not assumed here.**
6. That `cc66`'s `r7869` landed a committed per-bin response record. **Its contents have not been
   read.**

---

## Ⓐ① THE SUM RESPONSE AT THE SPECTRUM LEVEL

The order asks for the instrument's `Dl(Σ)/Dl(0) − 1` for TT, TE and EE at `Σ = 0.06`, `0.30` and
`0.60` eV, at the control's cosmology with every other parameter held, with NUFD on and off, and
then for the block and ℓ range where it departs from CAMB's.

### Ⓐ①ᵃ — the response is read, not rebuilt

Every number comes from the committed banks' **control arm** (the arm whose geometry switch is off),
whose sum series is the one that holds all other parameters fixed. The 0 eV denominator is that same
series' own `Σ = 0` point in the SAME bank, so the ratio is internal to one bank and one arm.

⚠ **Reachable negative, and it is reported rather than worked around:** if a needed point is missing
from either bank, or the two banks' multipole vectors are not identical element for element, this arm
reports **BLOCKED** and no response is interpolated, re-binned or carried across banks. The two
multipole vectors are compared as arrays, not by length.

### Ⓐ①ᵇ — the comparison with CAMB, registered BOTH WAYS

CAMB is run here at the control's own cosmology with the same three sums and the same multipoles, so
the comparison does not wait on another seat and is not a quotation. The two live cases:

- **AGREES** — the instrument's response matches CAMB's everywhere, within the same few-parts-in-a-
  thousand band the background was verified to. ⇒ **The limit's move is NOT in the sum response at
  spectrum level**, and the order's named candidate is ruled out *at this level*. This is a real
  outcome and would be reported as one.
- **DEPARTS** — then the block and the ℓ range are named, and the size of the departure is given at
  the three sums, with the sign.

⛔ **The criterion is fixed now:** a departure counts where the instrument's response differs from
CAMB's by more than **five parts in a thousand of `Dl(0)`** at that multipole, which is the band the
background repair itself was verified inside. Named by the largest contiguous run of such
multipoles per block, not by a cherry-picked single bin.

### Ⓐ①ᶜ — does NUFD move the instrument towards CAMB or away? THREE live cases

Measured only where Ⓐ①ᵇ found a departure, and only there:

- **TOWARDS** — the NUFD-on response is closer to CAMB's than the NUFD-off one, in every block where
  a departure was named;
- **AWAY** — it is further in every such block;
- **MIXED** — it is closer in one block and further in another. ⚠ **A mixed result is reported as
  mixed.** It is not resolved by choosing a block, by averaging the blocks together, or by weighting
  them — the question asks about a direction and a direction that is not common does not exist.

### Ⓐ①ᵈ — the ℓ-dependence, reported as measured and not as a diagnosis

The order's candidate predicts a particular shape: a suppression with **no scale** would be
nearly ℓ-independent across the band, where CAMB's carries a free-streaming knee. So the
ℓ-dependence of each response is reported — its value at the bottom of the band, its value at the
top, and the ratio between them — for the instrument and for CAMB, at all three sums.

⚠ **This arm does not conclude the mechanism.** If the instrument's ℓ-dependence is as structured as
CAMB's, that WEAKENS the order's candidate, and this revision says so rather than keeping it. If it
is flat where CAMB's is not, that is stated as consistent with the candidate and **not** as the
candidate established — a shape agreeing with a mechanism is not the mechanism.

---

## Ⓑ② THE LOWER BASIN'S DIRECTION

### Ⓑ②ᵃ — the parameter is named through the instrument, not through an index

`r7870` recorded two vectors at `0.400` eV, `12.5367` apart in χ². Which parameter separates them is
**not** read off a slot number. Both vectors are pushed through the instrument's own `phys`, and all
four parameters are reported **in physical units** for each basin, together with the component the
profiler holds separately.

⚠ **Reachable negative:** the difference may NOT concentrate in one parameter. The two live cases:

- **ONE DIRECTION** — one parameter's physical difference dominates, and the other three are small
  next to their own grid steps. Then it is named, with its size in physical units and in steps.
- **NOT ONE DIRECTION** — two or more move together. Then the basin is reported as a **direction in
  more than one parameter**, with the combination given, and it is NOT labelled with one name.

⌗ *The guard this arm is built against: before two stretches are identified by a label, check how
many-to-one the label is on the object. A slot index is a label; `phys` is the object.*

### Ⓑ②ᵃ′ — and the separation is checked at the loci the object distinguishes

Naming the direction is not enough: the two vectors must actually be two minima, not one minimum
reported twice. So the χ² is evaluated along the straight segment between them, and the arm reports
whether there is a **barrier** between them — a point on the segment higher than both ends.

⚠ **Reachable negative:** if no barrier is found, the two are **not** separate basins and `r7870`'s
word "basin" was the wrong one for them. This revision would say that about its own previous
record, as it has twice before.

### Ⓑ②ᵇ — whether the reference has a branch along that direction

Read from `cc66`'s committed `r7869` record, which the order says found one branch to `0.60` eV on
both rulers.

⚠ **Reachable negative, and it is the likely one:** if that record does not resolve a branch
**along the direction Ⓑ②ᵃ names** — as against a branch in some other direction, or a branch not
decomposed by parameter at all — this arm reports the question as **UNESTABLISHED and routed**, with
what would settle it. ⛔ It does not answer the order's question from the order's own summary of
another seat's work. A sentence in an order about another seat's measurement is not that
measurement.

---

## Ⓒ③ WHAT THIS REVISION DOES NOT DO

- **The arm of record is not re-run.** The order puts it behind ①, and it stays there.
- **No limit is read or reported.** No profile is run, no envelope is closed, and no crossing of any
  kind appears in this revision's record. The order's own ruling stands: an envelope crossing is a
  lower envelope over the basins reached and is never a limit.
- **The mechanism of the `100`–`207` lean stays carried**, as it has since `r7869`.
- **No receipt belonging to another seat is edited.** `r7869` converted the one-rate census to a
  property, so this revision expects to need no census routing at all; if it does need one, it is
  routed with a patch and not applied.

⌗ *This file is the registration. It is committed and pushed before the first number of this
revision is computed, and nothing in it is revised after a measurement is read.*
