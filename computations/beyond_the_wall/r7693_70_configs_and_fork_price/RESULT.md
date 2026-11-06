# r7693+70 — RESULT, items 1–3: the configs, the fork's price, and the drift-removed build

**Headline: HIER's split clock is not the arm of record on the perturbations.**
- The arm of record (`ACOUSTIC_two_arm.py`, `LEAFPERT` default since r3409) runs the perturbation equations on the **leaf** rate, with leaf-total fractions, and chain-rules them onto the stacking grid.
- HIER's `SPLITCLOCK=1` (mine, r7675) leaves the perturbations' `Hc_of` on the **stacking** rate, with leaf-total fractions. That is the arm of record's retired `STACKPERT=1` pairing, which ACOUSTIC and PO13 call a Poisson source "short by ρ_full/ρ_free": 3.04 at onset, 1.33 at recombination.
- So the split matches the arm of record on the grid, the projection and recombination, but not on the dynamics. The +0.026 / +0.029 at ℓ = 3 is the shift of that mixture, not of the arm of record.
- This bears directly on r7693's ruling to print the hierarchy's split depths. It also changes the fork's answer below: the arm of record keeps a consistent leaf constraint, so an exact transfer of it needs only a projection edit.

## Item 1 — the bank configs (approved, done)

`rekey_configs.py` → `rekey.json`. Committed as `r7693+70.0`.
- **What changed:** `p15_lowell_depths_leafrec1.npz` and `p15_lowell_depths_distances_leafrec1.npz` now carry:
  - a per-row `clock`;
  - a per-row `SPLITCLOCK` (`armA_exact: false`, `armB_*: true`);
  - an `ARM` that states the per-row reading;
  - `note_r7693`, in both `config` and `manifest`.
- **What did not change:** `ells`, `armA_exact`, `armB_frozen` and `armB_decoupled` are byte-identical (dtype, shape and bytes checked after the rewrite). Key order and the uncompressed `np.savez` format are kept. The sha256s change, `1f0440c67cae → ea771ace7e1d` and `23f79c3f7b08 → 9c07b05767f7`, because `config` and `manifest` are in the files.
- **`check_banked_config`, before and after:** it reads, for every banked `.npz`, whether a `config` exists and is a JSON object carrying `ARM` plus the four defining switches, or else whether the file is in the hash manifest. Neither bank is in the manifest, so no hash is checked. Both runs print the same thing, byte for byte: 302 banked, 88 carrying `config`, 214 in the manifest, PASS. It reads no field the re-key touched except `ARM`'s presence, which is kept.
- **Readers:** no reader reads a `config` field of either bank. The receipt reads `ells` and the three rows, and cc66's `clause_scope.py` reads only whether the keys `config` and `manifest` exist. All three were run by stem after the re-key: the receipt ends ALL CHECKS PASSED, and both scripts exit 0.

## Item 2 — the CAMB fork, priced and not built

**What CR's own sources commit to.** They are not silent.
- **P15 `CR_cosmology.tex`:**
  - :210 "the perturbations … are processes running *in* the content and take that rate [the leaf's], while a comoving separation read across leaves takes the stacking rate";
  - :425–427 "That is the stacking rate's answer, and the perturbations do not take it: they take the leaf's, which carries the radiation term";
  - :234 the L2 leaf readout is "the ordinary Friedmann readout … with radiation gravitating normally";
  - :863–866 and :2996 say the same.
- **P16** :423 "a process running in the content takes the leaf's, at every epoch".
- **P6** (`shadow_of_existence.tex`:353) speaks only to the projection distance on the stacking rate.
- **P5** (`groupoid_paper.tex`) lists the levels (L1 stacking, L2 leaf) and says nothing on perturbations.
- **The instrument:** the arm of record implements this. `Hc = Hl_of(e) if LEAFPERT else Hc_of(e)` (:934, :1512), fractions over the leaf total `_rt`, and the right-hand side multiplied by `Jac = H_grid/H_leaf` (:974, :1555). `GSRC` is flagged as a double count under LEAFPERT.
- **r7677 RESULT_item1** named HIER's pairing as inherited and untested. Nothing in the sources defends it.

**The two choices, physically:**

| | (L) the arm of record's own construction | (H) HIER's split pairing |
|---|---|---|
| Einstein / Poisson | leaf Friedmann constraint, self-consistent: ℋ_leaf² ∝ ρ_tot, radiation gravitating (P15 :234) | stacking ℋ with leaf-total fractions: the source short by ρ_full/ρ_free, ×3.04 at onset to ×1.33 at recombination (PO13 :2113–2119) |
| Perturbation dynamics | leaf conformal time (CAMB's own; the stacking grid is an exact chain rule, ACOUSTIC :289–291) | stacking conformal time |
| Recombination | leaf (CAMB's Recfast as is) | leaf (Recfast's `Hz` re-pointed) |
| Projection distance, comoving geometry | stacking rate | stacking rate |
| Initial data | CAMB's radiation-era adiabatic series is consistent (leaf ℋ has a radiation era) | CAMB's `initial()` assumes ℋ = 1/τ in radiation domination, which a stacking ℋ does not have; the same inconsistency HIER's split carries (r7677: about 0.001 at ℓ = 3 in HIER) |
| CR's sources | **what P15/P16 assign** | the retired `STACKPERT=1`; P15 :425–427 says perturbations "do not take it" |

**Price, in lines and wall time**, from CAMB 2.0.4's own Fortran (sdist, `fortran/`):
- **(L), about 50–80 lines.**
  - Perturbations, `dtauda`, `derivs` and Recfast stay as they are. The edit is the line-of-sight projection: `cmbmain.f90` replaces χ = τ₀ − τ in the Bessel argument with χ_stack(a(τ)) from a stacking-rate spline (about 30–50 lines).
  - Matching ACOUSTIC's two residual stacking reads is about 10 more lines: `VISLEAF=0` weights the visibility measure by the stacking clock, and Ψ in its line-of-sight source uses the stacking `Hc_of` (`_project` :1761–1767).
  - A switch in `model.f90` and the Python wrapper is about 20 lines.
  - **Wall:** install `gfortran` (not on this box) and build CAMB, about 10 min; implement, about 2 h; an unset-is-byte-identical gate against stock 2.0.4 at both points, about 15 min; runs at 7.8 s per point. **About 3 h in all.**
- **(H), about 40–60 lines for the rate, plus about 100+ if the initial data are rewritten.**
  - `dtauda` on the stacking rate (`equations.f90`:5–24, which moves the τ grid, opacity, r_s and every `dtauda` reader in `results.f90`).
  - `adotoa = sqrt(grho/3)` re-pointed in `derivs` (:2365, :2368), in the output and source paths (:1437, :1794, :3006), and in the ℋ′ / `gpres` combinations in the sources.
  - A leaf `dtauda` for Recfast's `Hz` (`recfast.f90`:1239, :808) and HyRec/CosmoRec's exports.
  - `initial()` either left inconsistent, as HIER is, or re-derived for a radiation-free ℋ.
  - **Wall:** about 3–4 h without the initial data, and a day or more with them.

**So an exact transfer of the arm of record can exist, and it is the cheaper of the two.** The arm of record splits the clocks in geometry (the grid is an exact chain rule, and the projection is on the stacking rate), not in dynamics. Choice (H) would reproduce a construction the instrument retired.

**What follows for the hierarchy (proposed, not built: an instrument edit and 69's call).**
- HIER can carry (L) the way ACOUSTIC does. Under `SPLITCLOCK`, `rhs` reads the leaf ℋ (from `_Hrec`) in place of `Hc_of`, and its output is multiplied by `Hc_stack/Hc_leaf`.
  - That touches about 6 sites (`rhs` :189, the FROZEN branches :286 and :296, the onset's `Hcs` :163 and :393), about 10 lines, plus a unset-is-byte-identical gate.
  - Rerun price: about 30 min for both points and both builds.
- I have not registered an ℓ = 3 expectation, because r7677 could not separate the dynamics share from the grid and projection share of the +0.026. The rerun is what separates them.
- **I'd recommend it before cc66's rewrite prints the split depths.**

## Item 3 — "a build with the phase drift removed": definable as a counterfactual, not as an arm

**What the drift is.** Each arm's η-integrated source `S_i` is fitted with one comb period in its own `q = k r_s*/π`: control 1.0170, CR 1.0115 (phases 1.076 and 1.082). The drift is 2πq(1/T_cr − 1/T_lcdm) plus the phase offset, 0.034 to 0.199 rad over q 0.85–5.75. It is mostly a period difference of 0.54%; the phase offset is 0.006 rad.

**Why "removed" is not a physics switch.** The period is each arm's effective acoustic scale measured against its own scalar r_s*. It is made by the arm's whole background and clocks, and it moved 1.0160 → 1.0115 with LEAFREC plus the refit point. No switch in the instrument sets it.
- The dynamics switches that move it all move other physics too: LEAFREC, LEAFSCALES, PHASEONLY/PHASEPOW, NUFS, NODRIVE, VISLEAF, CRPHI and SRCTAPER.
- `SRCINJ=fixed` and `SRCINJ=sweep` remove it by replacing the source; that is the acceptance-law input the departure is measured against.
- So a real arm with "the drift removed and all else equal" does not exist.

**What is definable: a counterfactual on the real source.** Take the CR arm's own source S_cr(k, η) and resample it in k so its comb matches the control's: S′(q) = S_cr(q·T_cr/T_lcdm + Δq), with Δq carrying the 0.006 rad offset. Project it through the CR arm's own geometry (D_M, visibility, projection) and read `retained_own` at the same seven bands.
- That is "the CR plasma with the control's acoustic period, seen through CR's sky". It is well defined, and it is the operation cc66's synthetic `inject2(same=True)` performs, done on the real source and not on an injected one.
- It cannot be done from the banks: `r6911_source_cr_leafrec1` keeps only `S_i` and the value at the visibility peak, not S(k, η).
- **Price:**
  - a guarded switch in ACOUSTIC that resamples S(k, η) in k before `_project`: about 30–40 lines, plus the unset-is-byte-identical gate;
  - one CR source-and-pairs rebuild (r6911 `SRCSAVE` plus r6915 pairs, sliced) and the r6941 fine bank for the step;
  - about 2–3 CPU-h, about 1–1.5 h wall on 4 cores, plus about 1 h to implement and gate.
- **Caveat to register with it:** the resample also stretches the source envelope by the same 0.54%. That is negligible for the band ratios, but it is not zero.

## Gates

- `check_banked_config`: identical PASS before and after.
- `run_touched_readers.sh --class1`: GREEN.
- The banks' readers were run by stem; see the reply.
