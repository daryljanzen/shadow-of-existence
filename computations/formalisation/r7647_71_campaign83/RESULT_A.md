# `r7647+71.2` — RESULT: campaign 83. `KillingChart` now carries `nondeg` (an invertible component matrix at every point). All of campaign 59's theorems re-check unchanged. The witness discharges the field from `det = −1`, and `kw_zero_excluded` replaces `kw_zero_rigidity`: no chart has `g ≡ 0`. No theorem broke. ⌗ `2` probes changed, about `25` lines. ⌗ p: `0.9`, `0.9`, `0.85`: all came true

*Against `PREDICTION.md` (`r7647+71.1`). 71 made the change by hand and re-ran both probes.
`lake env lean probes/KillingHorizon.lean` exits 0 with no errors, and all `18` `#print axioms` lines are standard.
`lake env lean probes/KillingWitness.lean` exits 0 with no errors, and all `30` are standard.*

***The field.*** `nondeg : ∀ p, (Matrix.of (g p)).det ≠ 0`. It is nondegeneracy, not signature.
- No proof in campaign 59 or 82 uses the field or the signature. They only consume a `KillingChart`, and never build
  one.
- So the theorems were about P1's nondegenerate setting already. The structure had admitted more than it needed.

***The witness.***
- `kw_chart` discharges `nondeg` with `Matrix.det_fin_two` (`det = −1`).
- `kw_zero_excluded (K : KillingChart n E) (p) : K.g p ≠ 0` replaces the old `kw_zero_rigidity`, which can no longer
  be stated.
- `kw_lorentzian` still shows signature `(−,+)`.

***The manifold layer: reported, not changed.***
- `LocalKillingChart` (in `FlowManifold.lean` and `LieDerivManifold.lean`) has no metric field. Its components are
  pulled back from the manifold metric `gc` / `hRep g`.
- A grep finds no nondegeneracy hypothesis on that metric anywhere in the two files. The only "invertible" facts there
  are about chart derivatives.
- So the same gap exists one level up. It is harmless today, because no theorem there concludes anything metric. It
  should get the same field whenever the manifold layer gains a Lorentzian structure, which campaign 84's proposal
  would add.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
