# `r7783+cc66` — REGISTRATION ONLY: the Gaussian-residual receipt, item ② of `r7783`

**Registered before the receipt exists.** The measurements it carries were made and published at
`r7779+cc66.5` (landed at `r7783`); what is new here is the receipt's own assertions — its pins, its
parses of `P15`'s prose, and its re-run of the joint fit inside a gated file. Each run of the
joint-fit receipt costs **5 s**, measured, so the receipt runs it twice rather than reading a bank.

## ⛔ What `P15` actually prints, checked first

The paper's claim is **qualitative**: *"the diffusion-scale signature it carries is located by the
joint fit as a Gaussian residual in $\ell$ that no tilt removes"*, and in `sec:coherence` *"whose
shape is a Gaussian in $\ell$, and no tilt removes a Gaussian"*. **Two sites, and neither prints a
$\chi^2$/bin figure.** So this receipt does not confirm a published number — *it supplies one, so the
claim can be quoted with a size on the rate the universe has*, which is the same service the comb
receipt did for `298.94`.

## The rows

### R1 — the paper's claim is qualitative, and this receipt is what gives it a number

**PREDICT** the phrase *"no tilt removes"* appears exactly **twice** in `corpus/CR_cosmology.tex`, and
that neither `1.4967` nor `1.5238` nor `1.50` appears anywhere in the paper.
**FAILS IF** the paper already carries a figure for this, in which case the receipt must confirm that
figure instead of supplying one, and I report that.

### R2 — the Gaussian's amplitude is distance-free, so only $\ell_D$ can move

**PREDICT** the joint-fit receipt's `K = R**2 - 1` with $R$ the damping-scale **ratio**; its baseline
the banked ΛCDM control `L820_lcdm_L2512_nk800`; no CR arm named anywhere in it; and **zero**
occurrences of a distance (`D_M`, `D_C`, `D_A`, `comoving`) in it or in the damping receipt it takes
$R$ from. ⛔ **Not a bare `chi`:** that file is full of $\chi^2$, and my first form of this test at
`r7779` counted twenty-one of those and reddened its own row.
**FAILS IF** a distance enters either.

### R3 — $\ell_D$ moves with the projection distance, by $6.788$ multipoles

**PREDICT** $1362 \times (1 - 0.004984) = 1355.2123$, a shift of $6.7877$, computed from the two
banked arms' own $D_M$ and not from a retyped percentage. **FAILS IF** it differs by more than
$0.001$ multipoles.

### R4 — the harness is faithful: at the published $\ell_D$ it reproduces $1.4967$ exactly

**PREDICT** running the joint-fit receipt's own source, with only its declared `INPUT` line rewritten
and its `HERE`/`ROOT` anchors pinned, returns $\chi^2/{\rm bin} = 1.4967$, absorbed $69.8\,\%$,
correlation $1.000000$ over the $\ell = 100$–$1758$ window at $171$ covered bins.
⛔ **Both anchors, not just `ROOT`:** the receipt reads a *sibling* receipt (`C62`) off `HERE`, and at
`r7779` pinning only `ROOT` killed both runs before any fit.
**FAILS IF** any of the four differs.

### R5 — and at the shifted $\ell_D$ the residual survives, $1.81\,\%$ larger

**PREDICT** $\chi^2/{\rm bin} = 1.5238$, absorbed $69.8\,\%$, correlation $1.000000$,
$\Delta n_s = -0.08383$ — a move of $1.811\,\%$, **above both** of `C62`'s bounds ($0.92$ by the
instrument route, $0.26$ by the data-shape route). **FAILS IF** it falls below $0.92$ or the move
exceeds $5\,\%$.

### R6 — the `r7749` arms' residual is a different object, and runs the other way

**PREDICT** a plain power law fits those arms' residual **better** than the Gaussian does
($+0.851$ and $+0.839$ against $+0.498$ and $+0.480$), and with the power law projected out the
Gaussian's partial correlation is **large and negative** ($-0.789$, $-0.783$).
⛭ Registered as the *sign*, not the magnitude: at `r7779` I wrote this test as
$|{\rm partial}| \le |{\rm raw}|$, assuming "adds nothing" would read as a partial correlation near
zero, and it does not. **FAILS IF** either partial correlation is not below $-0.5$.

### R7 — every figure the `INDEX` row prints, pinned here

**PREDICT** all of $1362$, $1355.21$, $6.788$, $1.4967$, $1.5238$, $1.811\,\%$, $69.8\,\%$,
$1.000000$, $-0.08304$, $-0.08383$, $0.92$, $0.26$, $+0.851$, $+0.498$, $-0.789$ compare to half
their last printed digit, **written as explicit comparisons in the receipt's source** — because
`check_figures_pinned` parses the receipt rather than running it, so a literal inside a table a loop
walks is not a pin. *That cost a cycle at `r7779+cc66.3`.*
**FAILS IF** any is off its pin.

### R8 — what is NOT claimed

No significance against the sky. `C62`'s two routes are not re-adjudicated. The shift is applied to
$\ell_D$ **only** — $R$ is held, and R2 is the licence for holding it. No claim that the one-rate
residual is more or less consistent with the data than the published one.

## Failability

To be **measured**, not asserted, in `failability.py`: perturbing $R$ should redden the rows that read
the fit and leave the parse rows and the distance-absence row green. The measured result goes in the
receipt's docstring, as `r7779+cc66.3`'s and `r7783+cc66.1`'s did.
