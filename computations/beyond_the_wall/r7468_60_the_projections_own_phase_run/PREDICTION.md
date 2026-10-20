# r7468 — REGISTERED BEFORE MEASUREMENT

**THE ORDER.** `r7465`: take `PO-87` and work it as physics.

**WHERE `r7466` LEFT IT, IN ITS OWN WORDS.** Neither named candidate carries a running phase: the
driving and the baryon loading each move the per-peak phase's **offset** and barely its **run**, and
every banked lever is spent in `ℓ_A` before it reaches the drift. A linear run in `ℓ` needs a
mechanism whose effect **grows with `ℓ`**; the acoustic levers act through `ℓ_A`, a fixed unit, which
is why they shift the phase without tilting it. And `PO-87` step ① had already located the contrast
excess *"in the projection from wavenumber to multipole and not in the acoustic dynamics."*
⌗ **`r7466` also said, in writing, that it computed no projection term. This computes one.**

**AND IT IS NOT A NEW INSTRUMENT.** `r6999`'s banked width filter already builds the exact kernel
integral — the visibility, the leaf phase held, and `scipy`'s spherical Bessel at the instrument's
own `ℓ`, `k` and `η₀`:

> `I_ℓ(k; s) = ∫ g(η) · exp(i k r_s,leaf(η)) · j_ℓ(k(η₀ − a − s(η − a))) dη`

**and it takes the MODULUS.** `np.hypot` of the two quadratures, every time. ⇒ **The PHASE of that
same complex integral is the projection's own contribution to the acoustic phase, it is sitting in
the banked instrument, and nothing has ever read it.** That is what this revision reads.

**THE TARGET,** carried forward from `r7466` and not re-derived: **`+0.04628` cycles per peak**.

---

## ⌈ Ⓓ WHAT I ALREADY KNOW — NOT SCORED

**Ⓓ①** `r7466`'s results in full: the target, the lever table, the `ℓ_A` budget of `149`–`847`, the
step-not-a-drift shape result, and its two fired controls.

**Ⓓ②** That `r6999`'s filter already **ruled the projection WIDTH out as the carrier of the CONTRAST
excess** — at most `26` per cent of it at the top band, failing the curvature tooth under both
anchorings, *"not the carrier; not excluded as a contributor."* **That is a different observable
from a phase run**, which is why this is not that measurement again.

**Ⓓ③** That same file's correction, which is the physics I am relying on and did not derive: the
plane-wave proxy is wrong because `j_ℓ(x)` near its turning point `x ≈ ℓ` — *where the whole window
sits, because `k D_M ≈ ℓ` is what the projection is* — oscillates at local rate
`√(1 − ℓ²/x²)`, **which goes to zero there**; the proxy overstated the departure by a factor of
fifteen and got its sign wrong.

**Ⓓ④** That `a`, the fixed point of the stretch, is **not a convention**: the visibility's mean and
its peak give answers of opposite sign, because a stretch about the wrong point is a stretch plus a
displacement. ⌗ *This revision reads the phase at `s = 1`, where no stretch is applied, so `a` drops
out of the quantity measured — and that is asserted and checked, not assumed.*

⌊

---

## ⌈ THE ARMS

**Ⓐ THE PROJECTION'S OWN PHASE RUN, `CR` ARM.** `arg I_ℓ(k)` at the comb's peaks `n = 1…5`, fitted
in `n`, in cycles per peak.
⇒ **PREDICT: non-zero, and UNDER one quarter of the target — `|s_proj| < 0.012`.** *Reason, from
`Ⓓ③`: the window sits at the Bessel's turning point where the local oscillation rate vanishes, so
the phase the projection accumulates is nearly stationary in `ℓ` exactly where the comb's peaks are.*

**Ⓑ THE ARM MINUS THE CONTROL.** The same run on `lcdm`, differenced.
⇒ **PREDICT: smaller again, `|Δs| < 0.005`** — a tenth of the target. *A projection is a projection;
what could be this construction's is the difference, and the two arms' geometries differ by about a
per cent in the window.*

**Ⓒ THE SIGN.** Whether the projection's phase run has the sign the drift needs (**positive**, the
run going up with `n`).
⇒ **PREDICT: POSITIVE on the `CR` arm.** *A guess with a reason and no measurement behind it: the
Bessel's turning point moves out with `ℓ` faster than `k D_M` does at fixed comb order.*

**Ⓔ THE SHAPE, which `r7466` made the discriminating question.** Whether `arg I` runs as a LINE in
`n` or as a STEP, by the same two-parameter comparison `r7466` used.
⇒ **PREDICT: a LINE fits it at least as well as a step** — unlike the model's own per-peak phase,
where the step won by `5.8`. *If the projection also delivers a step, it is the wrong shape too and
the row's workable half is narrower than it looks.*

**Ⓕ THE PLANE-WAVE PROXY'S PHASE.** The same integral with `j_ℓ` replaced by a plane wave.
⇒ **PREDICT: a run at least `5×` the Bessel one, and of the OPPOSITE sign** — `Ⓓ③` records exactly
that failure on the modulus, so the phase should inherit it.

⌊

---

## ⌈ THE CONTROLS — any one firing VOIDS the run

**Ⓥ① SAME INSTRUMENT, NOT A SECOND ONE.** `|I_ℓ(k)|` from this file's complex integral must equal
`r6999`'s `amp(ℓ, k, 1.0)` to `1e-12` relative, at every comb order measured.
**If it does not, this is a second instrument and the run is VOID** — `r7445`'s rule, and the
cheapest possible test of it.

**Ⓥ② THE ANCHOR DROPS OUT AT `s = 1`.** The phase computed with `a` at the visibility's mean and
with `a` at its peak must agree to `1e-10`. **If they differ, the quantity being measured is not the
one claimed and the run is VOID** — `Ⓓ④`'s defect, checked rather than assumed.

**Ⓥ③ NOT A QUADRATURE OR UNWRAPPING ARTEFACT.** The run recomputed on a grid refined by `2×` must
agree within `10` per cent of itself, and every unwrapping step taken must be printed.
**If refining the grid moves the run, it is the quadrature's and the run is VOID.**

⌊

---

*⌗ **No new spectrum.** The visibility, the leaf phase, `η₀`, `r_s` and `ℓ_A` are the banked
instrument's own. ⌗ `PO-87`'s fourth-peak half is **data-gated** and is not touched. ⌗ **The row is
the register's**: whatever this returns is supplied, not applied.*
