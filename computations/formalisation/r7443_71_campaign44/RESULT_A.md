# `r7443+71.39` — RESULT: campaign 44 BUILT. ⌗ Row 89: every computed part (1–6, 8). Kerr's Pontryagin closed form holds for symbolic `M` and `a`, the general Gowdy density carries exactly the powers {1, 3} of the twist, and the ratio `−1` is a corollary of the transgression identity. ⌗ `2830` lines against `1800` (band 1100–2600, MISSED HIGH by `230`; stop `3200` not fired). ⌗ p `0.30` came true. ⌗ Row 89 → `DONE`; LIBRARY GAP → `0`

*Scored against `PREDICTION.md` (pushed at `r7443+71.32` before any Lean), not revised.
`probes/Row89Pontryagin.lean` builds with no error. 54 theorems print `[propext, Classical.choice, Quot.sound]` and
four `rfl` trace facts print `[propext]` (`PROBE_RUN_A.txt`, `4168 s`). No `native_decide`. The build was done by a
delegated agent and re-run by 71.*

Every registered part is built, including the two Part 6 items the registration priced out: "exactly the powers
{1, 3}" (`grading_exact`) and "bare ω never appears" (`gowdy_shift`). Kerr went beyond the receipt's three spins to
symbolic `M` and `a` (`kerr_pontryagin`, `kerr_odd`, `kerr_psi2`). Part 5 is structural via the parity lemma, for
arbitrary profiles. Part 8 reads `−1` off campaign 43's `ratio_neg_one`.

***Caveats.***
- The engine needs a globally smooth nondegenerate metric. So Kerr is the smooth extension `KerrExt`, which equals
  Boyer–Lindquist Kerr on the open region `r > 2|M| + 2`, `|cos θ| < 5/16`, and the Kerr results hold there.
  Singular profiles elsewhere (`r²`, `sin²θ`, `R = t`) enter as nowhere-zero stand-ins.
- `static_named_zero` carries an unused hypothesis tying `f` to each named formula, because the vanishing holds for
  every profile.
- The anomaly normalisation `1/384π²` and the representation semantics are imported. The Part 7 paper-text checks
  are not formalised.
- About 1200 of the lines are copied infrastructure (the engine, rows 69 and 96, campaign 43), because probes cannot
  import probes. That is the band miss.
- Peak memory was about 12 GB.
- No disagreement with the receipt.
