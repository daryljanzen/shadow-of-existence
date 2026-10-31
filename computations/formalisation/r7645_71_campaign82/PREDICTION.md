# `r7645+71.2` — PRE-REGISTRATION: campaign 82, `r7645` (the owed witness). Non-vacuity of `kh_lemma_killing` and `kh_cor_stationary` by a null Killing orbit in Minkowski space. ⌗ `150` new lines in one probe (band 50–600 new), ⛔ stop `800` total. ⌗ p: witness for `kh_lemma_killing` `0.85`, for `kh_cor_stationary` (a `Rigidity` instance with a non-empty `H`) `0.75`

*Owed by the inventory (`r7643+71.3`). A new probe, `probes/KillingWitness.lean`, copying campaign 59's
`KillingHorizon.lean`. No Lean was written before this registration.*

***The witness.*** A `KillingChart` with `g` constant, so the Killing condition `g(p.1 + s, p.2) = g p` holds trivially.
- Its value at every point is Minkowski space in light-cone form, chosen so that the adapted direction `χ = ∂_s` is
  null: `g(χ,χ) = 0`.
- That is a null translation.

***Then.***
- `kh_lemma_killing`'s hypothesis `hnull` holds at every `x₀`, so `MetricallyCoincident K p q` holds for a concrete
  pair `p ≠ q` on one orbit.
- For `kh_cor_stationary`: `H` is the union of the orbits through a non-empty `X` (a null hyperplane), with `Rigidity`
  built from this chart.
- Each conclusion is then exhibited, not only implied.

***What the witness shows.*** Flat space is P1's own example: "every null hyperplane … is a metric singularity too". So
the witness is the paper's case, not an artefact.

***Failable:*** BUILT or REPORTED, with the step that stopped.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
