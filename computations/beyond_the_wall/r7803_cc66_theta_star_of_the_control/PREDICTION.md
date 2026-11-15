# r7803+cc66 — PREDICTION, registered before a line of the computation exists

**Order (69, r7803).** θ\* of the ΛCDM control at the same two points P15 now prints the
construction's pull at: the distances' point `(68.60, 0.2973)` and the refit minimum.  Give the
control's pull from Planck's angle at each.  69's reading of the outcome: *"If the control also sits
several σ high at the distances' point, the +4.8 is the background's tension between the
baryon-acoustic and microwave data, not the construction's.  If it doesn't, it is the
construction's."*

## What is being measured, named exactly

The corpus's definition of θ\* is `r7749_70_leafgeom_refit/theta_corpus.py`'s:

    theta_* = r_snd(H0, Om, wb, z_hi, ZREC, E_leaf) / D_M(ZREC, H0, Om, E_geom)
    E_stack(z,Om,h) = sqrt(Om(1+z)^3 + (1-Om))
    E_leaf (z,Om,h) = sqrt(Om(1+z)^3 + (WR/h^2)(1+z)^4 + (1-Om)),   WR = 4.15e-5
    ZREC = 1090.0,  R0 = 3 wb / (4 WG),  WG = 2.47e-5
    THETA_OBS, THETA_SIG = 0.0104085, 3.1e-6

The sound horizon is ALWAYS on `E_leaf` (node 66's one-clock ruling); only `D_M` changes rate
between the two assignments.  **`E_leaf` is flat ΛCDM's own E(z)** — matter, radiation at the
standard photon+neutrino density `WR/h^2`, and Λ = 1−Ωm.  So "the control on the corpus's
definition of θ\*" means this same expression with `E_geom = E_leaf` and the sound-horizon integral
carried to z→∞ instead of stopping at the arm's start, which is the only thing that distinguishes
ΛCDM's θ\* from the construction's leaf-rate assignment at the same parameter point.

**The two points, and what "its own refit minimum" is.**  The paper's two printed pulls are the
`theta_corpus.json` leaf-rate-assignment rows: `+4.837σ` at the distances' point
`(68.60, 0.2973, 0.02237)` and `+2.333σ` at the leaf-rate refit minimum
`(68.585672, 0.294463, 0.022181)` — the latter is r7749's Ⓑ, the LEAFGEOM=1 minimum on the
185-bin range.  The control's own refit minimum on that same range, same machinery, same `STEP`,
same lensing operator, refitted like-for-like, is

    control, 185-bin refit minimum:  H0 67.410309,  Om 0.309826,  wb 0.021966,  n_s 0.954248

(the companion of the arm of record's `68.570730, 0.291246, 0.021643, 1.015066`).  Both points are
run; the 132-bin control minimum `(67.4054, 0.3095, 0.0220, 0.9559)` is reported beside it so the
range's reach into the answer is visible, and Planck's own `(67.40, 0.3150, 0.02237)` is reported
as the un-refitted control.

## PREDICTIONS

**① The control's θ\* at the distances' point equals the construction's leaf-rate-assignment θ\*
there to better than 0.2σ, so the control sits between +4.7σ and +5.1σ.**  Reason, stated before
measuring: at a fixed `(H0, Om, wb)` the construction's leaf-rate assignment and ΛCDM evaluate the
*same two integrals with the same E(z)*; the only difference is the upper limit of the sound-horizon
integral, and `theta_corpus.json` already shows z_hi = 3e7 → 1e8 moves 100θ by 4.5e-5, which is
0.14σ.  **FALSIFIED** if the control's pull at the distances' point differs from `+4.837σ` by more
than 0.2σ — which would mean `E_leaf` is not ΛCDM's E(z) and my reading of the definition is wrong.

**② Therefore the +4.84σ is the BACKGROUND's, not the construction's** — 69's first branch.  The
construction contributes nothing to it.  **FALSIFIED** if ① is falsified.

**③ What IS the construction's is the gap between the two rate assignments, and it is larger than
the pull being attributed to it.**  At the distances' point the arm of record (D_M on the stacking
rate) sits at `−11.920σ` and the leaf-rate assignment at `+4.837σ`: a swing of `16.76σ` that is
entirely the choice of rate for the projection distance, i.e. entirely the construction's.
**FALSIFIED** if that difference is not 16.7σ–16.8σ.

**④ At the control's own 185-bin refit minimum the control does NOT return to Planck's angle: it
stays positive, between +1σ and +5σ.**  Reason: that minimum is a TT-only fit on this corpus's own
185-bin likelihood, and it lands at `wb = 0.021966`, well below the `0.02237` that Planck's full
fit — the fit that defines `THETA_OBS` — uses; a lower `wb` raises c_s and so raises r_s.  The
instrument's own banked `cc66_r185_verify_lcdm.npz` carries `r_s = 145.38204`, `D_M = 13954.3535`,
whose ratio is already above Planck's angle.  **FALSIFIED** if the control's pull at its own refit
minimum is negative or exceeds +5σ.  *This is the prediction I hold least firmly: the corpus's θ\*
is a simplified r_s at fixed z_rec = 1090, not the instrument's, so the two need not agree.*

**⑤ The refit does not rescue either side.**  Both the control and the construction move toward
Planck's angle when refitted, but neither reaches it: the construction goes +4.837σ → +2.333σ and
the control's own move is in the same direction and of the same order.  **FALSIFIED** if the
control's refit move is opposite in sign to the construction's, or differs from it by more than a
factor of three in magnitude.

## What the clause becomes if the predictions hold

Neither branch 69 offered, but his first one in substance and sharper: on the corpus's own
definition the construction's leaf-rate θ\* *is* ΛCDM's θ\* at the same point, so the +4.84σ is
wholly the background's tension between the baryon-acoustic and the microwave data and the sentence
may not charge it to the construction.  What the construction owns is the 16.8σ between its two
rate assignments — the pull it is entitled to be charged with is the one it has not yet been.

## How it is run

`theta_control.py` imports `theta_corpus.py`'s own functions (no copy) and adds `z_hi = inf`
by integrating to 1e12, reporting 3e7 / 1e8 / 1e12 side by side so the limit's reach is visible.
No new background code is written: the control is the SAME expression at the control's parameters.
