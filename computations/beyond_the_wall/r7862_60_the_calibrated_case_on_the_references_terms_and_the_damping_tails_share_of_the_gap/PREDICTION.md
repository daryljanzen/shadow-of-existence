# r7862 (node 60) — PREDICTION, registered before any computation of this revision exists

**On order `r7861` (69) items ① – ④.** The order's finding is that `r7860`'s "calibrated" profile was
not the case `cc66` calibrates: it froze `H0` and `Ω_m` at the grid's centre and freed `ω_b` and
`n_s`, where the reference frees all four and takes the BAO ruler `r_d` **at each point from that
point's own drag-epoch sound horizon**. So `146.13` meV is not the comparison to `30.56`, and this
revision computes the case that is.

⌗ *Every criterion below is fixed here. A figure that comes out the other side of one is reported AS
a failure with the criterion unmoved — that is the whole point of writing them down first.*

---

## ⚠ DECLARED READS — taken BEFORE this registration and not presented later as findings

1. ⛔ **The drag epoch at the control point is already read.** Before writing this file, this seat
   integrated the drag optical depth on the instrument's own `taup_of` and `Rb_of` and solved
   `τ_d = 1`, then accumulated the sound horizon to that epoch on the same clock `rs_from` uses:
   **`z_drag = 1061.1846`, `r_d = 147.0732` Mpc**, against the instrument's own `r_s = 144.5281` Mpc
   at recombination. ⇒ *This is a READ. The control point is therefore NOT an arm of this revision;
   the arms are the two grid corners, which are unread.*
2. ⛔ **The reference's own drag values at the control point are already read**, from `camb`'s
   derived parameters at the control cosmology: **`rdrag = 146.8930` Mpc, `zdrag = 1060.0474`**
   (with `rstar = 144.2478`, `zstar = 1089.9246` beside them). ⇒ *So the control point's agreement —
   `0.12` per cent on the ruler, `0.11` per cent on the epoch — is a read and is reported as one.*
3. The instrument exposes `taup_of`, `Rb_of`, `a_of_eta`, `eta_rec`, `RB_REC`, `A_REC`, `Hleaf`,
   `Hgeom` and `R_S` at import, and one import at fixed switches costs about `2` s of CPU. *Read as
   a capability, before deciding to build the ruler by re-import rather than by a fitting formula.*

---

## Ⓐ① THE DRAG EPOCH, DERIVED FROM THE INSTRUMENT'S OWN IONISATION HISTORY

The order requires the ruler be the instrument's, not a number carried in: `r7854`'s `RDFIX` takes
`r_d` as a NUMBER FROM THE CALLER and the file says so, which is legitimate for one control point
and cannot serve a profile whose cosmology moves.

**What is computed:** `τ_d(η) = ∫_η^{η_end} (dτ/dη′)/R(η′) dη′` on the instrument's own `taup_of`
and `Rb_of`, the drag epoch as its root at `τ_d = 1`, and `r_d` as the sound-horizon integrand
`rs_from` already uses, accumulated from `a → 0` to `a_drag` on the clock `rs_from` is on.

**Ⓐ①ᵃ — the registered comparison, at TWO CORNERS OF THE GRID, both unread:** `r_d` and `z_drag`
against `camb`'s `rdrag` and `zdrag` at the same cosmology.
- **criterion: `|r_d/rdrag − 1| < 0.005` and `|z_drag/zdrag − 1| < 0.005` at BOTH corners.**
- ⛔ **reachable negative:** either corner outside either band ⇒ **the ruler is reported as not
  validated and Ⓑ② IS NOT RUN ON IT**, with the figures given. *This is the arm that can stop the
  revision, and it is placed first for that reason.*

**Ⓐ①ᵇ — WHAT THE RULER RANGES OVER, measured and not assumed.** A ruler in Mpc should depend on the
cosmology only through `ω_b` and `ω_m`; if it does, the per-point ruler can be built on a
two-variable grid, and if it does not, it cannot.
- **criterion: two different `(H0, Ω_m)` pairs carrying the SAME `ω_m` and the same `ω_b` give `r_d`
  equal to better than `1e-4` relative.**
- ⛔ **reachable negative:** they differ by more than that ⇒ the grid is built in three variables
  instead, at the cost, and the dependence is reported.
- ⌗ *GUARD: before two stretches are identified by a label, check how many-to-one the label is.
  `ω_m` is the label here and the two parameters are the stretches.*

---

## Ⓑ② THE CALIBRATED CASE, ON THE REFERENCE'S TERMS

All four of `H0`, `Ω_m`, `ω_b`, `n_s` free, with `r_d` taken at each likelihood call from that
point's own drag epoch through Ⓐ①'s ruler, instead of being minimised over.

- **Ⓑ②ᵃ the limit is REPORTED EITHER WAY**, as a comparison against the reference's `30.56` meV and
  beside `r7860`'s two numbers — `69.97` meV ruler-minimised and the superseded `146.13`.
- **Ⓑ②ᵇ registered expectation, which can fail:** the order's diagnosis is that holding the geometry
  forced the rest of the fit to absorb what `H0` and `Ω_m` would have taken, and that this is why
  `r7860`'s calibrated profile sat at a minimum of `0.060` eV and was flat from `0.030` to `0.100`.
  **If that diagnosis is right, the calibrated profile's minimum moves to below `0.030` eV and its
  limit lands within a factor two of `30.56` meV.**
  - ⛔ **reachable negative:** the minimum stays at or above `0.030` eV, or the limit lands outside
    `[15.3, 61.1]` meV ⇒ **the order's diagnosis is reported as REFUTED on this instrument**, with
    the criterion exactly as written here. *A configuration mismatch is a hypothesis about a cause,
    and a hypothesis that cannot come out false is not one.*
- **Ⓑ②ᶜ convergence is a condition on reporting, not a hope:** every node minimised from several
  starts including the previous node's own solution, with one polish, and **monotonicity above the
  minimum CHECKED**. A profile that dips reports NO limit, exactly as `r7860` left it.
- **Ⓑ②ᵈ the ruler is MOVING, and that is gated:** the per-point `r_d` is recorded at every node and
  asserted to vary across the profile. *A "calibrated" run whose ruler came out constant would be
  the held case again under a new name — the vacuity trap this corpus keeps catching.*

---

## Ⓒ③ THE DAMPING TAIL'S SHARE OF THE MINIMISED GAP

`r7860`'s minimised control is `69.97` meV against the reference's `54.00`: a gap of `15.97` meV.
`cc66` measured the raw spectrum departing from `CAMB` by `−6.35` per cent near `ℓ = 1920`.

- **Ⓒ③ᵃ** the minimised profile re-scored with the high-`ℓ` end cut back, at **two** cuts, each
  stated as the multipole above which bandpowers are dropped, and the limit recomputed at each.
- **Ⓒ③ᵇ registered expectation, which can fail: less than half of the `15.97` meV moves with the
  cut** — i.e. the damping-tail residual does not account for the gap.
  - ⛔ **reachable negative:** more than half of it moves ⇒ reported as the tail's gap, with the
    share at each cut, and `r7860`'s minimised number re-read in that light.
- **Ⓒ③ᶜ** the cut is gated as having actually removed bandpowers — the count dropped is reported at
  each cut, and a cut that removed none is a failure of the leg and not a null result.

---

## Ⓓ④ WHAT THIS REVISION DOES NOT DO

- **Item ③ of the order is DEFERRED, as the order directs**, and the condition is gated rather than
  asserted: `_resolved_config()` gains no key here because **this revision does not move the
  instrument's blob**, and the receipt asserts the instrument file is byte-identical to
  `origin/main`'s copy. ⇒ *If that assertion fails, the four keys are owed in this revision and the
  receipt says so instead of carrying the deferral.*
- The arm of record (item ④) is not judged here; it follows ① and ② once they stand.
- ⛔ **No figure of `cc66`'s or `70`'s is edited.** Anything owed to another seat is routed through
  `FOR_66_FROM_60.md` with its patch.

---

## The guards this revision is exposed to

- *a gate must assert the clause its argument reasons FROM* — Ⓑ②ᵇ gates the order's own stated
  cause, not merely that some number moved.
- *before an identity is treated as an obstruction, establish what it ranges over* — Ⓐ①ᵇ.
- *an identification has to be checked on the loci the object itself distinguishes* — the ruler is
  validated at the corners, not only where it was read.
- *when two descriptions differ, first ask whether the difference survives a change of clock* — the
  drag-epoch horizon is accumulated on the clock `rs_from` is on, and the receipt says which.
