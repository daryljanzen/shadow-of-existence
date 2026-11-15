# `r7801+cc66` — REGISTRATION ONLY: the frozen run measured, and θ\* on the current one-rate build

**Registered before either computation exists.** What is read at registration time is the producers'
source, the banks' configs and manifests, and 70's stored `theta_corpus.json` — not any new output.

---

## ① The frozen build on the one rate, MEASURED

The producer is `computations/beyond_the_wall/r7703_70_frozen_converged/run_frozen.py`, driving the
receipt's own arm-B harness at `FROZEN_adjudicated_KLO_0_1`. The leg that does not exist is
`distances__armB_frozen__one_clock__*`. Adding it needs one `POINTS` entry — the distances'
background `(68.60, 0.2973)` with `OBF = ORF = 1` and **no `SPLITCLOCK` key** — and the two rungs
`NS3 = 1800` and `2400`, then 70's own h² extrapolation
`(n2²·b − n1²·a)/(n2² − n1²)`.

### R1 — the run completes inside its own guards

**PREDICT** both rungs return seven depths with `max|Φ| ≤ 0.93`, the guard `r7703` item 1 added after
finding that a **finite** blow-up passes the harness's `isfinite` test and silently returns `r = 1`.
⛔ **And `NS3` stays at 1800/2400: `NS3 ≥ ~3000` is NOT usable** — at 3600 the mode at the `HKCAP`
edge (`h·k = 0.079998`) blows up at `k·η ≈ 250`. **FAILS IF** either rung exceeds `0.93`, or if I
reach for a finer rung to "converge better".

### R2 — the measured figures, against the carry they replace

`r7799+cc66` reported **3.35–3.40 %** against the exact transfer and **1.74–1.77 %** against the
decoupled build, as a **carry** across the (L) convergence correction.
**PREDICT** the measured values land inside `±0.3` percentage points of that bracket.
⛔ **This row is registered to be able to say the carry was WRONG.** If the measured figures fall
outside that window, the carry — and the clock-stability argument under it — did not hold, and I
report that as the result rather than the agreement. *A carry that is never checked is just a guess
with a footnote.*

### R3 — and the carry's own error, quantified

**PREDICT** I report `measured − carried` per multipole and as a maximum, so the next seat knows what
a convergence carry of this shape is worth. **FAILS IF** I report only the new figures and drop the
comparison.

---

## ② θ\* on the current one-rate build — ⛔ AND THE ORDER'S PREMISE IS WRONG

69 writes: *"The +2.3σ figure is from the early leaf-rate refit (r7753), so re-solve it on the build
the comb's 298.5 comes from."* The implication is that `+2.3σ` is the same quantity at a stale
revision. **It is not: it is a different POINT.**

- The `298.5` comb build is `spectra/r7749_leafgeom_nofit_L2000_cr.npz`, whose own `__SWITCHES__`
  read `ARM=cr CRH0=68.60 CROM=0.2973 HIER=1 LEAFGEOM=1 LEAFREC=1 LEAFSCALES=1` and whose manifest
  records `point: {CRH0: 68.60, CROM: 0.2973}` — **the distances' point.**
- `+2.3σ` is `theta_corpus.py`'s **leaf-rate refit minimum** row, `(68.5857, 0.29446, 0.022181)`.

**These are different cosmological points, so re-solving at the 298.5 build does not refresh `+2.3σ`
— it replaces it with another number.**

### R4 — the figure the order actually asks for

**PREDICT** θ\* on the corpus's definition at the distances' point, with `E_geom = E_leaf` (which is
what `LEAFGEOM=1` is), is **`100θ\* = 1.04235`, a pull of `+4.84σ`** — against `1.04157 / +2.33σ` at
the refit minimum and `1.03715 / −11.92σ` on the arm of record at the same point.
⇒ **So the figure `P15` can cite for the 298.5 build is `+4.8σ`, and it is WORSE than the `+2.3σ`
now in print, by about a factor of two in the pull.** **FAILS IF** the re-solve disagrees with 70's
stored value, or if the 298.5 build turns out to sit at the refit minimum after all.

### R5 — verified by re-running, not by reading the bank

**PREDICT** `theta_corpus.py` is re-executed and reproduces all six stored rows, so the figure is a
measurement here and not a quotation of `theta_corpus.json`. **FAILS IF** any row moves.

### R6 — and the onset is reported with it

**PREDICT** the onset that matches `θ_obs` at the distances' point on the leaf rate is
`1.2314e6`, with `ρ_r/ρ_m = 365.2` there — reported because the pull alone does not say whether an
onset reaching `θ_obs` exists, and at this point one does.

### R7 — what is NOT claimed

Which point `P15` should quote, and whether `+4.8σ` is acceptable, are 69's. No refit is run, no new
minimum is sought, and `θ_obs = 0.0104085 ± 3.1e-6` is inherited rather than re-derived.

## Failability

To be **measured**: perturbing the background point must move the θ\* rows and leave the
build-identification rows green.
