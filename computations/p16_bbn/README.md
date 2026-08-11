# D1 — P16's owed computation: the Big Bang (multi-abundance BBN) on the cooling leg

This directory discharges **D1**, the sole below-the-line debt owed P16's aspirational title
(`THE_PLAN.md` → THE LINE, SHARPENED): the full multi-abundance nuclear network integrated on the
progenitor collapse's cooling-leg thermal history, earning the title's "**produces** the primordial
light-element abundances" at the criterion of necessity (P6 R2 — the pattern *required*, jointly,
not a tuned fit).

## The physics (P16 §rate, §trev, §peak, §network)
P16 proves the cooling leg of the local collapse history **is** a standard big-bang nucleosynthesis:
the local Friedmann window rate equals the standard rate (§rate); the peak is fully dissociated and
hot, M-independently (§peak); a freeze-out lives only on the cooling leg (§trev). So the abundances
are the standard-BBN pattern at the CMB-inherited η — computed here, not asserted by analogy.

## Files
- **`bbn_network.py`** — the network. {n,p,D,T,³He,⁴He,⁷Li,⁷Be} on **JINA REACLIB** rates (via
  `pynucastro`, forward + detailed-balance reverse) + the corpus's validated finite-T weak n↔p.
  Standard radiation-dominated cooling background; n/p pre-evolved through weak freeze-out (kept
  inside REACLIB's T9≲10 validity); analytic-Jacobian stiff integration with a tolerance retry ladder.
- **`validate_bbn.py`** — the gate. Conservation, abundances vs accepted standard-BBN values,
  η-dependence trends, the lithium problem. **Run this to certify the machinery.**
- **`cooling_leg_reduction.py`** — verifies the reduction the network assumes: M-independent hot
  peak, adiabaticity, standard window rate (mis-extensions fatal), metallicity floor.
- **`make_abundance_figure.py`** → `fig_abundances.pdf`/`.png` — the results figure (in P16 §network).
- **`Yp_freezeout.py`** — the earlier standalone He-4 freeze-out (Y_p=0.2506), the weak-rate machinery.

## Result (η₁₀ = 6.14, the CMB-inherited value)
| | network | standard BBN | observed |
|---|---|---|---|
| Y_p | 0.243 | 0.247 | 0.245 |
| D/H | 2.57e-5 | 2.51e-5 | 2.53e-5 |
| ³He/H | 1.04e-5 | 1.04e-5 | ~1.1e-5 |
| ⁷Li/H | 4.46e-10 | 5.0e-10 | 1.6e-10 (the lithium problem) |

Standard BBN to a few percent, with d ln(D/H)/d ln η = −1.60, the ⁷Li valley reproduced, and baryon
number conserved to 1e-8. The pattern comes out **jointly from the single inherited η** → "produces"
earned at R2. **Above the line remain** the last-percent precision (specially-evaluated vs REACLIB
light-nuclide rates) and the likelihood against measured data — a data-confrontation frontier, not a
debt.

## Supersedes
The r497-era `../CR_seam_turning_point_temperature.py` "inherited (for reversal)" reading — that
estimated the cold *cosmological seam* (L1, ~1.6 eV) and predates §peak's separation of it from the
hot *progenitor collapse peak* (L2). P16's synthesis reading is the one held.

Dependency: `pip install pynucastro --break-system-packages`.
