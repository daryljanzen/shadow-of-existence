# `r7443+71.71` — RESULT: campaign 55 (programme stage P4) BUILT. ⌗ T★, the completeness of the TT spectrum of S³, is a theorem. ⌗ p `0.35` came true. ⌗ Rows 65 and 66 → `DONE`. ⌗ ***The census is 111 of 111 DONE***

*Scored against `PREDICTION.md` (pushed at `r7443+71.68` before any Lean), not revised. `probes/S3TTComplete.lean`:
20 theorems on `[propext, Classical.choice, Quot.sound]`, `tt_complete` among them. Built in `200 s` with no error;
the only warnings are style linters inside the verbatim P2 copy. 3741 lines, which is over the 700–3200 band because
P2 is carried wholesale (about 2600 lines). The stop of 4500 was not fired. The build was delegated and re-run by
71 (`PROBE_RUN_A.txt`).*

## The theorem

```lean
theorem tt_complete (h : TenA) (lam : ℂ) (hC : CD 2 h)
    (hsym : ∀ x ∈ S3, ∀ b c, h b c x = h c b x)
    (htr : ∀ x ∈ S3, ∑ a, h a a x = 0)
    (hdiv : ∀ x ∈ S3, ∀ c, ∑ b, nabA b h b c x = 0)
    (heig : ∀ x ∈ S3, ∀ b c, lapA h b c x = -lam * h b c x)
    (hne : ∃ x ∈ S3, ∃ b c, h b c x ≠ 0) :
    ∃ m : ℕ, 3 ≤ m ∧ lam = (m : ℂ) ^ 2 - 3 ∧
      ∃ d : ℕ, m + 1 ≤ d ∧ ∃ T : Ten,
        (∀ x ∈ S3, ∀ b c, h b c x = evE (T b c) x) ∧
        (Submodule.Quotient.mk T : Q) ∈ TTQ d lam ∧
        (Submodule.Quotient.mk T : Q) ∈ Submodule.span ℂ (Set.range (famQ m)) ∧
        TTQ d lam = Submodule.span ℂ (Set.range (famQ m)) ∧
        Module.finrank ℂ (TTQ d lam) = 2 * (m ^ 2 - 4) ∧
        Module.finrank ℝ (TTR d lam) = 2 * (m ^ 2 - 4)
```

***In words:*** let a `C²` symmetric traceless tensor field be divergence-free on S³, satisfy `−∇²h = λh` there, and
not vanish on S³. Then `λ = m² − 3`, and `h` restricted to S³ is one of campaign 51's level-`m` eigen-tensors. That
eigenspace has dimension exactly `2(m² − 4)`, over ℂ and over ℝ. The symmetry, trace, divergence and eigen
conditions are required ***only on S³***.

## The route, as registered, every step built

1. ***Bridges.*** P1's analytic `∇²` on polynomials is P2's `lap` (`lapP_eq`, `evT_lap'`). P2's ideal `Z` is exactly
   the fields vanishing on S³ (`mem_Z_iff`).
2. ***Orthogonality.*** `orth` gives `h` orthogonal to every eigenvector of a different eigenvalue, via `lap_symm`.
   `lam_real` shows `λ` is real.
3. ***Projection.*** `proj_exists`: a Gram system on the `λ`-eigenvectors of `P_{D(λ)}`. It is injective by
   positivity and `Ev_linIndep`, hence solvable. Eigenvectors from any degree are re-indexed into `P_{D(λ)}` by the
   degree bound.
4. ***Vanishing.*** `orth_poly` and `vanish`: a field orthogonal to every polynomial is zero on S³. The proof uses
   P3's ***sup-norm*** Stone–Weierstrass, which is simpler than `L²` and removed the registered complex-`L²` risk,
   together with Mathlib's existing full support of `toSphere` (`IsOpenPosMeasure`).
5. ***TT carries.*** The frame derivative is tangential, so `πh` is TT on S³. P2's `tt_spectrum` and `tt_count`
   conclude.

## Scope

T★ is stated for restrictions of `C²` fields on ℝ⁴, as registered. Every smooth field on S³ is such a restriction
(for example `h(x/|x|)` times a radial bump), but that extension is not formalised here.

## The programme, scored

| stage | campaign | p | outcome |
|---|---|---|---|
| P1 integration | 52 | 0.45 | BUILT |
| P2 polynomial spectrum | 53 | 0.30 | BUILT |
| P3 density | 54 | 0.60 | BUILT |
| P4 assembly | 55 | 0.35 | BUILT |
