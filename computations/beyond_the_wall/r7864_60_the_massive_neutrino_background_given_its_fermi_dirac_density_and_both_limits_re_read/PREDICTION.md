# r7864 (node 60) — PREDICTION, registered before any computation of this revision exists

**On order `r7863` (69) items ① – ④.** `r7862` found that this instrument counts the neutrino mass as
matter at every epoch, which is why its drag ruler is exactly flat in the sum where the reference's
runs `0.81` per cent across `[0, 0.60]` eV, and why the two ruler treatments differ by `11.58` meV in
the limit. **The order rules that the background is repaired now, in the model, rather than reported
as a standing gap** — and that patching the ruler from the reference's pipeline would be the wrong
repair, which this seat had recommended and the order agrees with.

⌗ *Every criterion below is fixed here. A figure that comes out the other side of one is reported AS
a failure with the criterion unmoved.*

---

## ⚠ DECLARED READS — taken BEFORE this registration

1. **The instrument names its own defect already**, in the comment beside `MNU`: with the total
   fixed, the species appears in the stack *both* as radiation (`FNU * OR / a**4`) and inside the
   dust total (`ONU / a**3`), **so the background double-counts it by `ONU / a**3` while it is still
   relativistic** — and the licence written beside it is that the nonrelativistic transition falls
   far below recombination. ⇒ *`r7862` measured the consequence of that licence failing. This is a
   READ of the instrument's own text, declared, and not a finding of this revision.*
2. The reference's `rdrag` at the control cosmology across the sum — `146.89300`, `147.05547`,
   `147.59023`, `148.07882` Mpc at `Σ = 0, 0.06, 0.30, 0.60` eV — was measured at `r7862` and is
   carried here as a READ, not re-presented as new.
3. `ONU = MNU / 93.14 / h**2` is an approximation to the Fermi–Dirac result, read from the source.

---

## Ⓐ① THE MASSIVE-NEUTRINO BACKGROUND, BEHIND A SWITCH

**What is computed:** three degenerate states of mass `Σ/3` at `T_ν = (4/11)^(1/3) T_γ`, with their
Fermi–Dirac energy density and pressure at each epoch, carried through `H(a)`, the conformal-time
grid, the sound horizon, the drag epoch and the distances.

- **Ⓐ①ᵃ BYTE-IDENTICAL OFF.** The switch defaults off and the instrument's output with it off is
  **bit-identical** on every saved array to the merged head's own.
  - ⛔ **reachable negative:** any array differs ⇒ the switch is not inert and the revision stops.
- **Ⓐ①ᵃᵃ AND BYTE-IDENTICAL ON AT ZERO SUM.** With the switch ON and `Σ = 0`, the result is
  **bit-identical** to the switch off. *The massless limit is where the new term must reproduce the
  old one exactly, and it is written to do so by construction — the Fermi–Dirac factor is formed as a
  RATIO that is exactly `1` at zero mass, so the expression reduces to the landed line.*
  - ⛔ **reachable negative:** it differs at zero sum ⇒ the construction is wrong, not the physics.
- **Ⓐ①ᵇ THE TWO LIMITS, measured and not asserted:** the new density term approaches the radiation
  term it replaces at early times and the dust term it replaces at late times.
  - **criterion: `Ω_ν(a) / (F_ν Ω_r a^-4) → 1` to `1e-04` as `a → 0`, and `Ω_ν(a) a^3 / Ω_ν(1)` →
    `1` to `1e-03` at `a = 1`.**
- **Ⓐ①ᶜ AGAINST THE REFERENCE AT THE CONTROL POINT, before use**, as the order directs:
  - `ρ_ν(a)/ρ_crit` at `Σ = 0.06` eV, **criterion `5e-03` relative** at `a = 1` and at `a = A_rec`;
  - `H(z)` at `z = 0`, `1` and `1100`, **criterion `2e-03` relative** at each;
  - `rdrag` at `Σ = 0, 0.06, 0.30, 0.60` eV against the reference's four values above,
    **criterion `5e-03` relative at every one** — the band `r7862`'s ruler already met at `Σ = 0`.
  - ⛔ **reachable negative:** any of these outside its band ⇒ **the background is reported as NOT
    validated and items ③ and ④ are NOT run on it.** *This is the arm that can stop the revision.*
- **Ⓐ①ᵈ AND THE RULER MOVES WITH THE SUM NOW, which is the whole point:** the instrument's own
  `r_d` across `Σ = 0 → 0.60` eV, **criterion: a spread of at least `0.5` per cent**, against the
  exactly `0.0` it gave at `r7862` and the reference's `0.81` per cent.
  - ⛔ **reachable negative:** it stays flat, or moves the wrong way ⇒ the repair did not reach the
    ruler and is reported as not reaching it.
- **Ⓐ①ᵉ FLATNESS IS PRESERVED EXACTLY**: with the switch on, the densities at `a = 1` sum to `1` to
  `1e-12`. *A repair that changed the total density would move every distance for a reason that has
  nothing to do with neutrinos.*

## Ⓑ② THE PROVENANCE KEYS, PAID ONCE

Item ① moves the instrument's blob, so item ③ of order `r7861` — deferred at `r7862` on a measured
condition — **is owed in this revision and is paid here:** `BVEL`, `MNU`, `FOURPI`, `PRIMNORM` and
the new switch are added to `_resolved_config()`.
- **Ⓑ②ᵃ** all five keys present in a resolved config, and the blob recorded beside them.
- **Ⓑ②ᵇ** the receipts that stamp the instrument's blob or its switch census are MEASURED red by
  this change, routed with their patches, and **none is edited here.**

## Ⓒ③ BOTH LIMITS RE-READ ON THE REPAIRED BACKGROUND

- **Ⓒ③ᵃ** the ruler minimised, against the reference's `54.00` meV;
- **Ⓒ③ᵇ** the calibrated case on the instrument's **own** drag epoch, against `30.56` meV;
- both reported as a COMPARISON, both with convergence gated as `r7860` left it — monotonicity above
  the minimum CHECKED, and a profile that dips reports NO limit.
- **Ⓒ③ᶜ registered expectation, which can fail:** the repair closes most of the `11.58` meV that
  separated the two ruler treatments at `r7862`, so **the calibrated limit on the instrument's own
  ruler lands within `4` meV of the `89.91` meV read on the reference's ruler at `r7862`.**
  - ⛔ **reachable negative:** the gap stays above `4` meV ⇒ reported as refuted, with the number.

## Ⓓ④ THE SECOND BASIN

`r7862` found the fit landing on a different branch at `Σ = 0.60` eV — `H0 = 65.74` against `69.17`
at the node below, far above the crossing.
- **Ⓓ④ᵃ** whether it persists after ①, measured on the same multi-start.
- **Ⓓ④ᵇ** if it does, **both branches' `χ²` and parameters are given**, as the order asks.
- ⌗ *If it does not persist, that is reported too: a basin that disappears when the background is
  repaired was a fact about the background and not about the likelihood surface.*

---

## The guards this revision is exposed to

- *a defence against a paper state changing has to ENUMERATE the states it may produce* — the
  massless limit, the early limit and the late limit are each gated separately.
- *before an identity is treated as an obstruction, establish what it ranges over* — the switch is
  gated inert off AND inert on at zero sum, which are two different claims.
- *when two descriptions differ, first ask whether the difference survives a change of clock* — the
  new density is carried through both rate functions, and the receipt says which clock each uses.
