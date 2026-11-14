# `r7783+cc66` — REGISTRATION ONLY: the section's opening figures on the one-rate arm, item ③ of `r7783`

**Registered before any figure is read.** What is read at registration time is the *bank's* metadata
— switches, manifests and npz key names — and the producers' own recipes, not a spectrum.

## ⛔ The order expects one arm to serve for all five quantities, and for one of them it cannot

`r7779` ⑤, carried into `r7783` ③, asks for five things off the one-rate arm, *"and the refit arm for
the fourth feature"*:

| | on the arm of record (`r7781`'s labelled figures) | readable from the bank? |
|---|---|---|
| the four peaks | $220.0$ / $536.3$ / $811.6$ / $1125.1$ | **yes** — TT |
| the comb | $299.1$ | **yes** — TT (already receipted at `r7779+cc66.3`) |
| the phase intercept | $-0.2488$ | **yes** — TT |
| the height ratios | $2.291$ and $2.349$ | **yes** — TT |
| the fourth-feature comparison | $0.69$ (TT) / $0.92$ (EE) / $-0.21$ (TE) | ⛔ **no** |

**The fourth-feature comparison needs `Dl_EE` and `Dl_TE`, and no `LEAFGEOM=1` polarisation run exists
anywhere in the tree.** R0 establishes that by census rather than by assertion — *this is the same
shape of claim my `r7767` reply got wrong by stating it too strongly, so it is registered as a census
over every `.npz` under `computations/`, not as a look at the obvious place.*

## The rows

### R0 — the census: four polarisation banks exist, none with `LEAFGEOM=1`

**PREDICT** exactly **four** `.npz` files under `computations/` carry `Dl_EE` or `Dl_TE`
(`r7631_70_PO87_polarisation/pol_cr_leafrec0`, `pol_cr_leafrec1`, `pol_lcdm`, and
`r7633_70_leafrec_refit/verify_cr_leafrec1_pol`), and that **none** of them records `LEAFGEOM: true`
in its config or `LEAFGEOM=1` in its switches. **FAILS IF** a fifth exists, or any of the four is a
`LEAFGEOM=1` arm — in which case no run is needed and I report that instead.

### R1 — the four peaks on the one-rate arm, through the paper's own locator

The paper's locator is its own: *"by parabolic fit to each hump above $\ell=100$"*.

**PREDICT** the four peaks of `r7749_leafgeom_nofit_L2000_cr` land within $2$ multipoles of the arm of
record's $220.0$ / $536.3$ / $811.6$ / $1125.1$ — the comb moves only $-0.055\,\%$, so the peaks
cannot move much — and that **each individual peak moves by less than one multipole**.
**FAILS IF** any peak moves by a multipole or more. *Registered sharp: if a peak does move further,
that is the finding.*

### R2 — the phase intercept

**PREDICT** $\phi/\pi$ on the one-rate arm is within $0.002$ of the arm of record's $-0.2488$, since
the comb and the peaks both barely move. **FAILS IF** it moves further.

### R3 — the height ratios

**PREDICT** the first-to-second and first-to-third height ratios are within $0.01$ of $2.291$ and
$2.349$. ⛭ *Licence stated: these are ratios of peak heights on the SAME grid, so the comparison is
relative and neither side vanishes; the standing absolute-bound rule does not bite.*
**FAILS IF** either moves further.

### R4 — the fourth feature is DEFERRED to a run, with the run's own switches registered here

The scorer is `r7633_70_leafrec_refit/score.py`, which runs PO-47's locator
(`r7631_70_PO87_polarisation/measure.py`, unchanged) on a polarisation npz against the control's.
The producer recipe is `r7631`'s own: `ACOUSTIC_two_arm.py` with
`HIER=1 LSTEP=8 LMAXL=2000 POLSAVE=<npz>` plus the arm's parameters.

**The run this item needs**, taking the refit arm's own switches verbatim and adding `POLSAVE`:

```
ARM=cr CRH0=68.585672 CROM=0.294463 HIER=1 LEAFGEOM=1 LEAFREC=1 LEAFSCALES=1
LMAXL=2000 LSTEP=8 NS=0.961379 WBH2=0.022181 ZSTART=3e7 POLSAVE=<npz>
```

**PREDICT** its TT reproduces the banked `r7749_leafgeom_refit_verify_cr` to within the solver's own
reproducibility at every shared multipole — which is the gate on whether the run is the same arm, and
the row that must pass before any EE or TE number is reported. **FAILS IF** the TT differs.

⛭ **The launcher is idempotent** — it skips a finished `.npz` — because this container restarts
unpredictably, and it is checked for a running solver by reading `/proc/*/environ` for
`ACOUSTIC_two_arm` rather than by a bare `pgrep` name test.

### R5 — and the fourth-feature numbers, only once R4 is green

**PREDICT** the arm-minus-control differences at the fourth feature stay below the combined skies'
spreads ($1.87$ TT, $1.67$ EE) as they do on the arm of record, so the paper's *"the controls' to
under a multipole in all three spectra"* survives the rate. **This row is explicitly conditional:**
if R4 is red or the run does not finish, R5 is **withdrawn, not reported**, and the deferral is what
I report to 69.

### R6 — what is NOT claimed

The comb is not re-measured here: `r7779+cc66.3` receipted it, and this registration carries its
figure for context only. No likelihood, no refit, nothing fitted beyond the comb's own least squares.
No claim about which configuration the section should open on — that is 69's call.

## Failability

R0 moves under any new polarisation bank. R1–R3 move under either banked TT arm. R4 moves under the
run or under the banked refit arm. R5 moves under the run's EE and TE.
