# r7695+70 — PREDICTION, step 2 (registered before the build and its runs)

## The method, and why it is not the ordered Fortran edit

r7693 priced (L) as one edit, χ_stack in CAMB's Bessel argument. Working through it, that undercounts. ACOUSTIC's (L), which HIER now mirrors at `SPLITCLOCK=L`, also:
- takes the visibility as a density in **grid** time, with optical depth κ_g = ∫τ′ dη_stack (`VISLEAF=0`);
- reads Ψ in the source on the stacking ℋ.

CAMB's source is a single expanded expression in leaf time with analytic visibility derivatives. Converting it to the grid measure is three different chain-rule substitutions (the non-derivative, first-derivative and second-derivative terms each carry a different power of `Jac`), not one argument change. That is a substantial rewrite of `equations.f90`'s source and `results.f90`'s thermal history.

**The route instead, and it is the cleaner cross-validation:**
- **Dynamics:** CAMB's own exact Boltzmann state, unmodified stock 2.0.4: perturbations on the leaf rate, its own Recfast and reionisation. Extracted in the Newtonian gauge with `get_time_evolution(frame='Newtonian')`: Δ_γ, v_b, Φ_N, Ψ_N, `polter` and the opacity.
- **The grid map:** each HIER grid time η_grid is mapped to a(η_grid) and then to CAMB's leaf conformal time.
- **The projection:** the state is handed to **the same** source assembly (`HIER.source_terms`) and **the same** depth arithmetic as the arm-B harness, with HIER imported under `SPLITCLOCK=L`. That puts χ = η₀ − η on the stacking grid, the visibility in the grid measure (built from CAMB's own opacity), and Ψ on the stacking ℋ.
- **What this buys:** arm A (L) and arm B (L) share every step after the dynamics, so their difference is the dynamics alone: CAMB's exact hierarchy against HIER's truncated one.
- **The conventions,** measured super-horizon:
  - Ψ_N and Φ_N are Ma–Bertschinger's ψ and φ (δγ = −2ψ, φ/ψ = 1.18);
  - θ_b = k·v_b;
  - Π_F = 10·`polter`, from matching CAMB's line-of-sight source to HIER's;
  - Ψ is encoded through σ_ν,eff = (Φ − Ψ)k²/(6ℋ_leaf²Ω_ν), so HIER's formula returns CAMB's Ψ on the leaf ℋ and the stacking-ℋ residual under (L), as ACOUSTIC reads it.
- **No Fortran is changed,** so there is no unset-is-byte-identical gate to run. Its place is taken by G below.

## Gate G (validation, before the (L) run)

With HIER imported **one clock** (`SPLITCLOCK` unset), CAMB's state through HIER's projection must reproduce stock arm A at the distances point (0.4874 / 0.4348 / 0.3590 / 0.6663 / 0.9113 / 0.9831 / 0.9981) **to within 1% at every ℓ = 2–8**. That shows the hand-off and the projection carry CAMB's transfer faithfully. If G fails, nothing under (L) is reported as arm A.

## Expectations for arm A under (L), distances point

- **P6.** Arm A (L) − arm A (one clock) at ℓ = 3 equals HIER's projection share to within ±0.004. On FROZEN that share was +0.0071 (0.4375 − 0.4304), so **arm A (L) ℓ = 3 ≈ 0.442 ± 0.005**.
- **P7.** The minimum stays at ℓ = 4 and the recovery at ℓ = 8.
- **P8.** Step 3: arm A (L) against arm B (L) agrees at every ℓ = 2–8 within the one-clock spreads (DECOUPLED 2.9%, FROZEN 6.3%). The ℓ = 3 exception does not reappear: |A − B| at ℓ = 3 is under 2% on both builds.
- **Price:** about 1 h to build and run (CAMB evolution for about 580 k over about 5000 times, a few minutes per run).
