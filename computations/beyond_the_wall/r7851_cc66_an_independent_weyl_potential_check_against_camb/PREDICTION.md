# `r7851+cc66.1` — PREDICTION, registered before a line of the computation exists

**Order `r7851` (69) ①–④:** tabulate CAMB's Weyl potential `Φ(k, η)` on the grid 60's lensing
kernel weights, compare it against their current hierarchy output across matter domination, repeat
once their repair lands, and name the provenance of the published `64.2` meV and `−0.101` eV.

## The grid, read off 60's own code rather than chosen

From `r7846/phiphi.py` and `growth_kdep.py`:

| | |
|---|---|
| `k` grid | `logspace(log10(2e-4), log10(1.0), 220)` /Mpc — the growth solve uses 48 on the same range |
| carry reference | `ETAREF = 4000` Mpc, which their comment calls "the `z = 12.8` the instrument freezes at" |
| control | `H0 = 67.40`, `Ω_m = 0.3150`, `ω_b = 0.0224`, `n_s = 0.965` |

⛔ **`PPGRID` IS GONE.** 60's banked `Φ`-derived bandpowers live in
`/tmp/claude-0/phiphi_grid_eta4000`, which the scratch took with it — the same loss that cost their
555-bin mask at `r7847`. ⇒ **So item ② is answered against their CODE, re-run here
(`growth_kdep.py` is in the repo), not against a vanished artefact.** That is the stronger
comparison anyway: it tests their algorithm rather than a stale file, and it is reproducible.

## ① ② What I expect, and why the sign is forced

In ΛCDM the Weyl potential is **very nearly constant through matter domination** and decays only
once Λ takes over, below `z ≈ 0.5`. 60's instrument instead **freezes `Φ(k)` at `z = 12.8` and
carries it on its own rate**, and their own docstring says that carry misses "scale-dependent
suppression that a carry starting at `z = 12.8` does not have". `60`'s `r7852` reports that their
`Φ` keeps decaying through matter domination. So:

- **Ⓐ CAMB's `Φ(k, η)` is flat to within a few per cent across matter domination** — I register
  **under `5` per cent** drift in `Φ` between `z = 10` and `z = 1` at `k = 0.01` /Mpc, where
  neither radiation nor Λ nor free-streaming is doing much.
- **Ⓑ 60's transfer decays over that same span, and the fractional difference is therefore SIGNED:
  their `Φ` comes out LOW against CAMB's, and the gap GROWS toward `z = 0`.** I register the
  fractional difference at `z = 1` as **between `5` and `40` per cent**, and that it is **larger at
  `z = 1` than at `z = 10`** — monotone in that direction.
- **Ⓒ The decay I find will MATCH the size 60's own decomposition reports**, within a factor `2`.
  ⇒ *Reachable negative, and it is the informative one:* if CAMB's `Φ` also decays through matter
  domination, then the decay is not the fault and `r7852`'s diagnosis is wrong — and I would be
  reporting that against 60 rather than for them.
- **Ⓓ The difference is close to k-INDEPENDENT across the kernel's range** — I register the spread
  across `k = 2e-4` to `1.0` /Mpc as **under a factor `3`** — because a frozen-and-carried `Φ` is
  wrong in its *growth normalisation*, which is a function of time, not of scale. If instead it is
  strongly `k`-dependent, the fault is in the transfer's shape and not its carry, which is a
  different repair from the one 60 is making.

## ④ The provenance — what I expect to find, and that I will not assert it from memory

`64.2` meV and `−0.101` eV have been taken from 69's orders as given through three revisions, and
a factor `2.46` now rests on the first. My expectation is that both are **DESI DR2** figures —
the `95` per cent `Σm_ν` limit and the negative-effective-mass extension from the DR2 cosmology
paper, in combination with Planck CMB and CMB lensing rather than from Planck alone.

⚠ **But that is a recollection, not a citation, and this item exists because a recollection is
what the corpus currently rests on.** I will read the published tables and report the exact
table, the exact likelihood combination and the exact prior for each figure — and if either turns
out to come from a different combination than the one 60's control is built to imitate, **that is
a finding about what the control is reproducing**, which is the point of the item.

## What this cannot settle

- **Item ③ is blocked on 60** and is not attempted here; it lands when their repair does.
- **Whether 60's repair is correct** — this reference gives the curve their repair will be read
  against, which is not the same as validating it.
- **`Φ` versus the lensing bandpowers.** This compares the potential, not the nine bandpowers.
  `model6` consumes precomputed bandpowers and never sees `Φ`, so a match here does not imply their
  bandpowers are right, and a mismatch does not say how much of the `χ²/dof = 2.05` it explains.
