# r7091 (70) — where the fit is pinned by the implementation: effective degrees of freedom, and the residual's shape

*Pre-registered before any number below is computed. The order is `FOR_70.md` `r7091`, Q1 and Q2. **The numerical-settings question is closed and is not reopened, and the excluded channels stay excluded.** No prose is edited, and no receipt or banked spectrum is changed.*

## The object, read before computing

- **The six-parameter refit** is `computations/beyond_the_wall/refit_grid185/`, read by the registered receipt `P15_the_full_range_refit_holds_the_background_and_the_phase_residual_was_quantised`. It has:
  - 185 plik_lite TT bins, ℓ 100–1996;
  - a base and two-sided steps in H0, Ωm, ωb and n_s on each arm;
  - A_s in closed form;
  - **τ exactly degenerate with A_s**, already measured.

  So the declared six are **five at most** before anything is computed.
- **The onset pin is not in this fit.** Every CR run in the grid sets `ZSTART=3e7`, so the solved onset (`Z_START = None`, "solved for the pinned acoustic scale") is overridden there. **If the reported CR spectrum uses the solved onset and the refit does not, the refit's directions are not the reported model's directions.** That is checked and reported as a fact. It is not argued.
- **The clock Jacobian is present in this fit.** Every CR run sets `LEAFSCALES=1`, the two-clock configuration the order names.

## What is computed (`rigidity.py`)

Everything is whitened by the plik_lite covariance, so a response is measured in the data's own units. The lensing operator is the receipt's own: the banked ratio if present, else CAMB at the control's parameters.

**Q1, the degrees of freedom.**
1. **The rank.** I take the SVD of the whitened response matrix [m0 (amplitude), ∂H0, ∂Ωm, ∂ωb, ∂n_s] per arm, with the columns scaled to the receipt's own step sizes.
   - I report the singular values.
   - I report the **effective rank**: the number of directions whose Δχ² for a one-step move exceeds 1, and the number exceeding 1 % of the largest.
   - I report the **degenerate directions**, the right singular vectors of the small values, in parameter terms.
2. **The coupling the clock Jacobian is named for.** I regress each parameter's whitened response on three templates of m0:
   - the **amplitude**, m0 itself;
   - the **acoustic shift**, −ℓ ∂m0/∂ℓ, a stretch in ℓ;
   - the **contrast**, m0's oscillatory part about its running mean in ℓ, scaled.

   Each parameter's (shift, contrast) coefficient pair is a vector. **If, on the CR arm, all four parameters' vectors are collinear** (the 2×4 matrix has its second singular value small against its first) **while the control's are not**, then the shift and the contrast cannot be varied independently on CR. That coupling is imposed by the computation, since the control's physics, which CR shares in the plasma, does not couple them.
3. **The reach.** I project the whitened residual (data minus the best-fit model) onto the span of the five whitened directions. The question is what fraction of the residual χ² any linear move of the five can remove, and how much is orthogonal to every direction the model has, which **it cannot reach**. I compare with the noise expectation, n − 5.

**Q2, the residual's shape.** Under the null that the residual is noise, I draw 20 000 noise realisations from the plik_lite covariance, remove the same five-direction projection from each, and compute the same statistics on the data's residual:
- the number of **sign changes** across the bins in ℓ order;
- the **longest run** of one sign;
- the **sum of squared run-sums**, which measures the excursion size between crossings, whitened;
- the fraction of the whitened residual's power in the **lowest 10 % of Fourier modes** along the bin index, a coherent swing.

For each I give a two-sided MC p-value per arm, and the weight in noise σ.

## Outcomes, the one that costs another seat most first

1. **The CR arm's (shift, contrast) responses are collinear where the control's are not.** That would be the coupling the clock Jacobian is named for, measured as a number, and it would bear directly on cc66's one-clock rebuild. **Predicted: yes**, with CR's second singular value under 10 % of its first and the control's over 30 %. This is a guess.
2. **The residual's shape is distinguishable from noise on CR** at p < 0.01 on at least one statistic: fewer crossings than noise, longer runs, or larger excursions. **Predicted: yes on CR.** On the control, predicted **weaker but also non-null**, since plik_lite against an implementation at fixed lensing is not expected to be noise either. This is a guess.
3. **The rank.** **Predicted:** four or five effective directions on the control, and one fewer on CR at the 1 %-of-largest threshold.
4. **The reach.** **Predicted:** on CR, the unreachable part of the residual χ² exceeds n − 5 by more than 5σ (√(2(n−5))). On the control it is closer.
