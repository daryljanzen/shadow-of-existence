# r7729+70 — PREDICTION (registered before any edit or run)

The order (`FOR_70.md`, `r7729`) builds what `r7725+70` priced: the real-source transfer Δ_ℓ(k) for all four source × kernel combinations, at every integer ℓ in q ∈ [0.80, 3.10], on the CR arm's ladder nodes. The ΛCDM kernel is recomputed there and only the ΛCDM source is interpolated, with a closure control at 10⁻³. Storage is a `refs/ci/*` blob plus a thin tracked summary.

## One thing the ruling cannot do as written, and the route that does it

The ruling says "interpolate only the ΛCDM source fields (`SRCSAVE`)". **`SRCSAVE` does not save the fields.**
- It writes the source at the visibility peak (`*_ls`) and its η-integral (`*_i`), never S(k, η).
- The interpolation and the cross-projection both need S(k, η) itself.

**So the build is:**
1. **`SRCFIELD=<path>`, a new output-only save in `ACOUSTIC_two_arm.py`.** It writes, per k-batch, exactly what `_project` holds: `S` (n_η × n_k), `ee`, `x0`, `kb`, and `P = kb^(NS−1)/kb · gradient(kb)` (batch-local, as `_project` builds it).
   - It is default-inert, in the same discipline as `DLKSAVE` and `SRCSAVE`.
   - **Gate:** unset, the edited file's `SAVE` output is byte-identical to the pre-edit file's on both arms, in the r6911 no-op configuration (`LSTEP=16 LMAXL=500`).
2. **One run per arm at the reported r6911 configuration** (`HIER=1 LMAXL=2000 KFAC=2`, leafrec1 points), in k-slices of 250, with `SRCFIELD` set and `LSTEP=64`.
   - `LSTEP=64` keeps the in-run projection token-sized. Its ℓ (100 + 64n) are a subset of the banked `LSTEP=8` grid.
   - The k grid is untouched, because `LMAXL` stays 2000.
3. **`project4.py`, offline.** It is `_project`'s line `np.trapezoid(S * J, ee, axis=0)` with `J = j_ℓ(k · XS · x0)`, applied to:
   - **(S_cr, K_cr):** CR's own fields on its ladder; XS = 1.
   - **(S_cr, K_lcdm):** CR's fields, x0 → XS·x0 with XS = D_M(lcdm)/D_M(cr). That is `SRCXS`'s definition of "the same source through the other arm's distance".
   - **(S_lcdm, K_lcdm):** ΛCDM's S(k, η) interpolated in k onto the ladder nodes inside the overlap (cubic spline per η row); XS = 1.
   - **(S_lcdm, K_cr):** the same interpolated source, XS = D_M(cr)/D_M(lcdm).
   - P on the ladder is the **source** arm's k^(n_s−1)/k times the ladder's own batch-local measure (CR's saved gradient).
   - Every integer ℓ with q = ℓ/l_A ∈ [0.80, 3.10]. Each combination's ℓ uses its kernel's l_A; both l_A agree to 0.1%, and the **union** is taken, so all four share one ℓ axis.
   - Checkpointed in blocks of ℓ, so a container restart costs at most one block.

**The ℓ-range knob 69 asked for is therefore not added.** The projection at every ℓ happens offline, and putting ΛCDM on the ladder grid inside the instrument would change its k grid, which the ruling forbids. A knob nothing calls is an edit with no reader.

## Closure controls (registered)

- **C1, the instrument against the bank:** each run's own `LSTEP=64` D_ℓ reproduces the banked r6911 leafrec1 D_ℓ at the shared ℓ to ≤ 1e-10 relative. That establishes the configuration.
- **C2, the projector against the instrument:** `project4.py` on each arm's **native** grid and fields, (S_A, K_A) with XS = 1, reproduces that run's D_ℓ at its ℓ to ≤ 1e-12 relative. That establishes the reimplementation.
- **C3, the ruling's control:** (S_lcdm, K_lcdm) collapsed on the **ladder** grid reproduces the native ΛCDM D_ℓ to ≤ 10⁻³ at **every** ℓ in the window. The native reference is projected at every integer ℓ on the native grid, so this is not limited to the banked stride.
  - **If it fails, the build refuses** (no blob) and the failure is reported with its worst ℓ.
- **C4:** every retained array satisfies ℓ(ℓ+1) Σ_k P Δ² = its own collapsed D_ℓ, an identity checked to 1e-12.

## Expectations (registered)

- **E1:** C1 and C2 pass at machine precision.
- **E2 (the risk):** the CR ladder spacing is about stretch/D_M ≈ 2.0×10⁻⁴ Mpc⁻¹, against the ΛCDM continuum's 1.12×10⁻⁴ and a Bessel period of 4.5×10⁻⁴. That is **about 2.2 nodes per Bessel period**, below the instrument's own 4-per-period guard.
  - **So C3 is at genuine risk:** ΛCDM summed on the ladder may miss 10⁻³ through quadrature aliasing at high ℓ.
  - **I put 50% on C3 passing at every ℓ in the window.**
  - If it fails, that is a finding about the ruling's grid, reported, and the remedy (a ladder refined by an integer factor in L, for both arms) is priced, not built.
- **E3:** the wall is under 1.5 h on 4 cores. That is two solver passes of about 8–10 min of core each at `LSTEP=64`, plus about 3 core-h of offline projection.
- **E4:** the arrays are about 4 × 695 × (≤ 1452) × 8 B ≈ 32 MB.
