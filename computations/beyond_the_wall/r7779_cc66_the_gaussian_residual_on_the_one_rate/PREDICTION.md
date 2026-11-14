# `r7779+cc66` — REGISTRATION ONLY: the Gaussian residual on the one rate, item ③ of `r7779`

**Registered before any fit is run.** What was read at registration time is the *construction* of the
two objects — the source of
`receipts/P15_CR_cosmology/P15_the_joint_fit_leaves_the_gaussian_and_the_bound_was_chi2_not_sigma.py`
and of the `r7749` arms' configs — and not any residual.

## ⛔ The order's premise joins two different residuals, and the registration says so first

The order asks: *"`sec:coherence` and the abstract placed a Gaussian residual in ℓ 'that no tilt
removes', located by the joint fit with the distance on the geometric part of the rate. Is it present
on the one rate? Read the `r7749_leafgeom_nofit` and refit arms' residuals."*

**Reading those arms' residuals cannot answer that question, because no CR arm spectrum enters the
Gaussian residual at all.** The joint-fit receipt's baseline is the **banked ΛCDM control**
(`spectra/L820_lcdm_L2512_nk800.npz`, normalised to the data) and its target is that baseline times an
**analytic** signature $S(\ell) = \exp[-(r^2-1)(\ell/\ell_D)^2]$ with $r = 1.0926$ and
$\ell_D = 1362$ as declared INPUTS. The fitted model is $A(\ell/1000)^{\Delta n}$ times the baseline.
*So the object is a forecast built from the damping-scale ratio and the control, and the only way a
projection distance can reach it is through $\ell_D$, which is a multipole.*

What the `r7749` arms leave is **the TT contrast residual** — the thing `r7749` measured the leaf-rate
distance to remove ($\chi^2\ 186.85$ against $186.51$, $1.002\times$). **That is a different residual
with a different carrier, and the two must not be reported as one.** R5 and R6 measure the arms'
residual anyway, in the form the order asks for, and R6 states the expected answer: it is *not* the
Gaussian.

## The rows

### R1 — the Gaussian's amplitude is distance-free, so the projection cannot move it

$K = r^2 - 1$ with $r = r_D/r_s$ the damping-scale **ratio**, from which the distance cancels
identically (`r7767` item 1: the damping receipt mentions $D_M$ zero times and returns a double ratio).

**PREDICT** the receipt's `K` is built from `R` alone, with no distance, no $D_M$, no $\chi$ anywhere in
its definition, and the baseline carries no CR arm. **FAILS IF** a distance enters either.

### R2 — but $\ell_D$ is a multipole, so it moves with the projection, by $-0.4984\,\%$

**PREDICT** $\ell_D$ on the one rate is $1362 \times (1 - 0.004984) = 1355.21$, a shift of
$6.79$ multipoles, the same relative move `r7779+cc66.3` pinned for $\ell_A$ and $D_M$.
**FAILS IF** the shift computed from the two banked arms' $D_M$ differs from $6.79$ by more than
$0.01$ multipoles.

### R3 — and the residual SURVIVES the shift: it is present on the one rate

**PREDICT** re-running the joint fit with $\ell_D = 1355.21$ and $K$ unchanged leaves
$\chi^2/{\rm bin}$ after the tilt within $5\,\%$ of the published $1.4967$ over `P15`'s own
$\ell = 100$–$1758$ ceiling window, and in particular **above both** of `C62`'s bounds ($0.92$ by the
instrument route, $0.26$ by the data-shape route). *So the answer to item ③ is yes, and the reason is
that a half-per-cent shift of a smooth Gaussian barely changes its projection onto a power law.*
**FAILS IF** it falls below $0.92$, or moves by more than $5\,\%$.

### R4 — and it is still the predicted SHAPE, not merely nonzero

**PREDICT** the shifted residual still correlates with its own analytic
$S(\ell) - A(\ell/1000)^{\Delta n}$ at $\ge 0.999999$, as the receipt's ⓵ reports at the unshifted
$\ell_D$. **FAILS IF** the correlation drops below that.

### R5 — the absorbed fraction barely moves

**PREDICT** the tilt still absorbs $69.8\,\%$ of the signature to within $1$ percentage point.
**FAILS IF** it moves by more than that.

### R6 — and the `r7749` arms' residual is NOT this Gaussian

Reading the arms as the order asks: bin each `r7749` arm against the control through the same
machinery and correlate its residual with the Gaussian template $S(\ell) - 1$.

**PREDICT** the correlation is **weak** — below $0.5$ in magnitude — because the arms' residual is the
contrast residual, whose own measured carrier is the ratio of the arms' distances to last scattering
($93.6\,\%$ of the $\ell$-varying variance, per the corpus's own receipt), and not a damping-scale
Gaussian. **FAILS IF** the correlation is strong, in which case the order's premise is right and mine
is wrong — *and that would be the finding, reported against this row.*

### R7 — what is NOT claimed

No significance for the Gaussian against the sky; no claim that $1.4967$ is or is not a detection; no
re-adjudication of `C62`'s two routes. The shift is applied to $\ell_D$ **only**: $r$ is held, because
R1 is why it may be.

## Failability

R1 moves under any edit to the joint-fit receipt's signature definition. R2 moves under either banked
arm's $D_M$. R3/R4/R5 move under the control bank, the covariance, or the window. R6 moves under
either `r7749` arm's spectrum.
