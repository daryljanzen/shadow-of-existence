# Hand-off to c23 — the Hubble / r_s build, where c22 took it (post-r430 reground)

**From:** c22 (woken on r430, regrounded from `DELOBOTOMISE_c22_hubble.md` + `c22_keepers.md` +
`CMB_ACOUSTIC_FRONTIER_STATUS.md`, then source at P9 `CR_flatLCDM_v2.tex` §477/§479/§516/§521–541/§657/§665/§679–683
and P5 `slicing_operator.tex` §186/§200–211/§263).
**Status:** all do-not-assert. This is a sharpening of the two open problems + a calibrated conditional map +
one corpus-holding question that is yours to settle. Nothing migrated to the corpus.

---

## 1. The platform (confirmed at source, not summary)
- Crux 1 verified: observable redshift–distance and D_M are flat-ΛCDM exactly (reassigned constant-R
  congruence, P9 §436/§516; Janzen 2015). Low-z scares (empty-beam/180×/blueshift) are wrong-congruence
  artifacts, dead.
- Crux 2 reduces to **r_s built right**: θ_* = r_s/D_M, D_M robust flat-ΛCDM.
- Frame locked: r_s in the noumenal dS₄ cosh background R(T)=α cosh(T/α), throat R=α never below, beginning
  at the finite-curvature seam B; then projected. (= c22 turn-87.)
- Source facts that drive the build:
  - §531–541 (eq:friedmann-coth, eq:omega-ratio): ρ_eff ∝ a⁻³ at **every** epoch; **no radiation term in
    the rate, ever**. Early universe is matter-dominated in its rate, never radiation-dominated.
  - §521–527: sinh^{2/3} amplitude = (2^{1/3}/√3)·α, α=√(3/Λ). Only scale is Λ.
  - §263 (P5) + §679–683 (P9): the radiation-filled early universe and the beginning/limits are **named
    open problems in the corpus itself** — unbuilt, decided by early-universe data, not by the geometry.

## 2. The target (firm, modest)
θ_* is data (peaks at ℓ≈220; 100θ_*=1.041, 0.03%). With D_M ∝ 1/H₀ and CR's single H₀ = the directly
measured value:
- H₀=67.4 → D_M≈13870 → need **r_s ≈ 144 Mpc** (= Planck; CR just reproduces standard, no resolution).
- H₀=73   → D_M≈12800 → need **r_s ≈ 133 Mpc** (~7% *below* standard; tension dissolved).
**The construction must come in at or below standard. The danger is always the balloon upward.**

## 3. The calibrated conditional map  (script + output shipped: rs_z_onset_map.py / _OUTPUT.txt)
IF a c/√3 plasma rings against CR's matter-like rate H=H₀√(Ω_m(1+z)³+Ω_Λ), and the this-side sound-travel
integral is cut at z_onset, then r_s(z_onset) is definite (calibration: standard ΛCDM with radiation +
baryon-loaded c_s → 142 Mpc, machinery sound):
- **no cutoff (rings to a→0): r_s ≈ 268 Mpc** — the +74% balloon, FATAL (first peak ℓ≈117 vs 220).
- **seam = recombination (z_onset=z_rec): r_s ≈ 0** — nothing this-side; must inherit from the collapse side.
- **to hit the data: z_onset ≈ 4730 (for r_s=144) … ≈4030 (for r_s=133)** — i.e. a plasma cutoff at z ≈ 4000–4900.

## 4. The sharp reading — why a cutoff does NOT save branch (a) cleanly
- The geometry supplies **no** cutoff at z≈4700. §211: the beginning (null boundary B) is at a→0 / z→∞ in
  the comoving (sinh^{2/3}) reading. The physical CMB-frame observer is that reassigned-ruling congruence
  (§657), and it genuinely reads a→0, H=(1/α)coth(3τ/2α)→∞ as τ→0. The throat's finiteness is the
  **ontological character** of the beginning (finite-curvature B), **not an observable size floor** —
  so it does NOT cut the comoving integral. [This corrects c22's earlier "finite throat floors it" lean.]
- z≈4700 ≈ matter–radiation equality is a **red herring**: in standard cosmology z_eq suppresses
  sound-travel because radiation *gravitates into the rate*; CR denies exactly that, so z_eq leaves CR's
  rate matter-like and the sound-travel un-suppressed. The ρ_m=ρ_γ content-crossover still exists but
  can't do the suppression work.
- ⇒ Branch (a) reproduces the data only by hand-inserting a **plasma-onset** (medium feature, problem #1)
  at a redshift CR's own rate gives no reason for. Not contradictory, but unmotivated and unbuilt.

## 5. THE corpus-holding question for you (load-bearing; c22 will not settle it from a partial read)
Reading §211 directly, the comoving congruence runs from now through a < a_rec all the way down to B at
a→0 — a genuine this-side history below recombination. That sits awkwardly with the status doc's live
"**seam = recombination → no this-side integral, r_s inherited from the collapse side**" candidate,
because geometrically B is at a→0, not at z_rec.
**Two possibilities, and you hold the corpus to decide which:**
- (i) the NBC seam-crossing (P9 §665) makes the comoving sub-recombination range (a<a_rec down to B)
  collapse-side / non-actualised — then seam=recombination is live and r_s is inherited; **or**
- (ii) there is a genuine this-side history below recombination — then seam=recombination does not fit,
  and the only escape from the +74% balloon is **branch (b): CR has no standard relativistic-plasma
  sound-horizon era at all, and the acoustic structure is reorganized.**
This single question decides inheritance-vs-reorganized-acoustics, i.e. the whole resolve mechanism.

## 6. Recommended next moves
1. Settle §5 at source (the NBC seam-crossing / what the sub-recombination comoving range is).
2. The resolution lives in problem #1 (the medium), not the seam geometry. Build (or rule out) CR's
   early-universe matter/radiation sector: does a medium oscillate, with what c_s, and is there an onset?
3. Hold the target: r_s ≈ 133–144 Mpc, at or below standard. Do-not-assert any θ_* until built.

## Files in this package
- `ADVICE_to_c23_rs-build.md` — this note.
- `rs_build_structure.md` — c22's full grounded derivation (source loci, the direction target, the §211
  correction, the sharpened fork).
- `rs_z_onset_map.py` — the calibrated conditional-map script.
- `rs_z_onset_map_OUTPUT.txt` — its output (calibration + the z_onset map).
