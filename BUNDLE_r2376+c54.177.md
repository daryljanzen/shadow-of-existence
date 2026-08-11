# BUNDLE r2376+c54.177 — the shear coefficient, derived instead of remembered

**Two parts, each under 30 MB, no file split across parts.**

- `CR_bundle_r2376+c54.177_part1_corpus.tar.xz` — top level + `corpus/ figures/ receipts/ verification/`
- `CR_bundle_r2376+c54.177_part2_working.tar.xz` — every other working directory

## What this revision is

**The derivation c54.176 named as owed, and it costs $\chi^2$ and is taken anyway.**

`C8_diffusion_length` has named "the $8/9$ coefficient against the $16/15$ polarization-corrected
one" in its own text since it was written, and neither value had ever been derived in this corpus.
At c54.176 I set it to $16/15$ on recollection and put it straight back; in the same revision $\chi^2$
through `plik_lite` was found to prefer $8/9$ by $1123$ units, and that preference was recorded and
refused. **Both refusals stand. This revision removes the ambiguity by measuring the coefficient.**

## The measurement

Two integrations of the *same* oscillator on the *same* background, differing in one thing: the
reference is the perfect tight-coupled fluid, undamped by construction; the hierarchy carries photons
to $\ell=24$ with Thomson scattering, the polarisation multipoles evolved alongside, and the baryons
on their own velocity. **Their ratio is the damping and nothing else** — the $(1{+}R)^{1/4}$ WKB
prefactor, the drift of $c_s$ and the $R$-dependence of the oscillation are common to both and divide
out identically. Gravity is off in both, which is not an approximation but the definition of the
object: the WKB damping formula is a statement about the *free* oscillator.

| | measured | leading order | |
|---|---|---|---|
| unpolarised ($G=0$, so the $\ell=2$ term is $-\tfrac{9}{10}\tau'F_2$) | $0.8852$ | $8/9=0.8889$ | $-0.42\%$ |
| polarised ($\Pi=F_2+G_0+G_2$) | $1.0618$ | $16/15=1.0667$ | $-0.45\%$ |
| **the polarisation correction** | **$1.1996$** | **$6/5$** | **$-0.03\%$** |

Both absolute values sit half a per cent low by an amount proportional to $C$, so the residual is a
common normalisation and cancels in the ratio. **The ratio is the derivation; the absolute agreement
at half a per cent is the corroboration.**

$C$ is read *locally*, between consecutive extrema, and extrapolated in $(k/\tau')^2$ — the points
fall on a line with scatter $0.002$ whose slope is the finite-$(k/\tau')$ correction the WKB
derivation drops. A cumulative reading smears that correction over the interval and cannot separate
"the coefficient is not $8/9$" from "we are reading a leading-order formula at finite $k/\tau'$".

## What it costs, and what that buys

**$16/15$ is adopted and the control gets worse: $\chi^2/\mathrm{dof}$ goes $22.5\to28.6$.** A
coefficient chosen because it fits is a fitted parameter whatever it is called.

**And the $1123$ is now a diagnosis rather than a temptation, with the missing piece named.**
Polarisation enters the transfer *twice*: it raises the damping coefficient, and it adds source terms
$g\Pi/4$ and $(3/4k^2)\,\dd^2(g\Pi)/\dd\eta^2$ with $\Pi=\Theta_2+\Theta^P_0+\Theta^P_2$. This
instrument has the half that removes power and not the half that returns it.

Nothing downstream moves: `sec:envelope-consequence`'s $10.8\%$ goes $+10.83\%\to+10.87\%$, because
the coefficient nearly cancels in a ratio of two rates — which is exactly why C8 could name the
ambiguity and still be quoted for a figure.

**And the CR arm does not move again**: $\ell_1/\ell_A = 0.5703$ through the coefficient change — the
fifth distinct instrument state over which that figure has not moved in the fourth decimal.

## Also in this revision

`L-147`'s $\chi^2$ values are now **recomputed live** from banked spectra rather than pinned, so the
cost of the derived coefficient is visible in the file that reports the verdict instead of asserted
from another. The verdict itself is unchanged and now more strongly so: the likelihood cannot
arbitrate.

*One assertion of mine fired on its own data and was loosened honestly rather than deleted: I
demanded both extrapolation slopes be of order unity and they are $-0.150$ and $-0.942$. What
actually matters is that the extrapolation be SHORT, which is what the gate now checks.*

## Gates

All ten gates plus `run_all_receipts` (**287 pass, 0 fail**, 536 s), `lint_assertions` (no hollow
assertions, zero assertion debt), `audit_index` (105/105), and `check_compile` (**17 papers, 0
errors, 0 undefined citations, 0 undefined refs, 0 dead receipt links**).

## New in the tree

- `receipts/P15_CR_cosmology/P15_the_shear_coefficient_derived_not_remembered.py`
- `computations/beyond_the_wall/L171w_hierarchy_damping_coefficient.py`
- `computations/beyond_the_wall/spectra/c54.177_{lcdm,cr}.npz`

## What is owed next, named

**The polarisation source terms**, which need the photon hierarchy carried inside the spectrum
instrument rather than in a side calculation — validated on the $\Lambda$CDM arm before this
construction is touched.
