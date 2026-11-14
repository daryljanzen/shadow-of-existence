# `r7779+cc66` item ③ — THE GAUSSIAN RESIDUAL IS PRESENT ON THE ONE RATE, AND THE ORDER'S TWO RESIDUALS ARE TWO OBJECTS THAT RUN OPPOSITE WAYS

**8 of 8 rows hold** (`gaussian_on_one_rate.py`, `rc=0`).

## The answer

**Yes — and it barely moves.** The Gaussian residual is built from the damping-scale **ratio**
$r = 1.0926$ and the banked ΛCDM control; **no CR arm spectrum enters it**, so the only way the
projection distance can reach it is through $\ell_D$, which is a multipole. On the one rate
$\ell_D$ moves with $D_M$: $1362 \to 1355.21$, a shift of $6.788$ multipoles.

Re-running the joint fit at the shifted $\ell_D$ — **the receipt's own source, with its one declared
`INPUT` line rewritten, so the machinery is identical and the two runs differ in $\ell_D$ and nothing
else**:

| | $\ell_D$ | bins | $\Delta n_s$ | $\chi^2/{\rm bin}$ after the tilt | absorbed | correlation |
|---|---|---|---|---|---|---|
| as published | $1362.00$ | $171$ | $-0.08304$ | $1.4967$ | $69.8\,\%$ | $1.000000$ |
| **on the one rate** | $1355.21$ | $171$ | $-0.08383$ | **$1.5238$** | $69.8\,\%$ | $1.000000$ |

**The residual survives at $1.5238\ \chi^2$/bin — a move of $1.81\,\%$ — still above both of `C62`'s
bounds ($0.92$ instrument route, $0.26$ data-shape route), still the predicted shape to a correlation
of $1.000000$, and with the tilt absorbing the same $69.8\,\%$.** *A half-per-cent shift of a smooth
Gaussian barely changes its projection onto a power law, which is why.*

⛭ The harness reproduces the published $1.4967$ **exactly** at the unshifted $\ell_D$, which is how
the comparison is known to be measuring the shift and not the copy.

## ⛔ The order's premise joins two different residuals

The order said: *"Read the `r7749_leafgeom_nofit` and refit arms' residuals."* **Those arms cannot
answer the Gaussian's question** — the joint fit's baseline is the control
(`spectra/L820_lcdm_L2512_nk800.npz`) and its target is that baseline times an **analytic** signature.
R1 establishes it: `K = R**2 - 1` with $R$ the ratio; no CR arm named anywhere; and **zero**
occurrences of a distance in either the joint fit or the damping receipt it inherits $R$ from.

The arms were read anyway, in the form asked, and the answer is sharper than "unrelated":

| arm | raw vs the Gaussian | raw vs a PLAIN POWER LAW | partial, power law removed |
|---|---|---|---|
| `LEAFGEOM=1`, nofit | $+0.4977$ | $+0.8513$ | $\mathbf{-0.7885}$ |
| `LEAFGEOM=1`, refit (verified) | $+0.4799$ | $+0.8385$ | $\mathbf{-0.7835}$ |

**A plain power law fits the arms' residual better than the Gaussian does, and once the power law is
projected out the Gaussian's partial correlation is large and NEGATIVE.** So in the part a tilt
cannot absorb, the two residuals run in **opposite** directions. *They are two objects, as the
registration said, and not merely two uncorrelated ones.*

## What I got wrong, recorded

 * **R6's threshold was met by $0.0023$**, which is not a verdict. R8 was added post-hoc to ask the
   question properly, and the raw $0.49$ turns out to be shared smoothness.
 * **R8's own test was the wrong one.** I assumed "the Gaussian adds nothing" would read as a partial
   correlation near zero and wrote $|{\rm partial}| \le |{\rm raw}|$. It reads as $-0.79$. The row now
   asserts the sign.
 * **Three harness defects**, each named in the amendment: a distance test that counted $\chi^2$
   tokens, a re-run harness that pinned `ROOT` but not `HERE` (the receipt reads a sibling receipt off
   `HERE`), and the likelihood module imported from the wrong directory.

## What is NOT claimed

No significance against the sky. No re-adjudication of `C62`'s two routes. The shift is applied to
$\ell_D$ only — $r$ is held, and R1 is the licence for holding it.
