# BUNDLE r2376+c54.178 — the photon hierarchy with polarisation, inside the transfer

**Two parts, each under 30 MB, no file split across parts.**

- `CR_bundle_r2376+c54.178_part1_corpus.tar.xz` — top level + `corpus/ figures/ receipts/ verification/`
- `CR_bundle_r2376+c54.178_part2_working.tar.xz` — every other working directory

## What this revision is

**The build c54.177 specified, and it takes the control most of the remaining distance.**

The photons are now evolved as a Boltzmann hierarchy to $\ell=24$ with the polarisation multipoles
alongside, the baryons have their own velocity **and** their own density contrast, and the source
carries $g\Pi/4$ and $(3/4k^2)\,\dd^2(g\Pi)/\dd\eta^2$ with $\Pi=\Theta_2+\Theta^P_0+\Theta^P_2$.

| | peaks | P1/P2 | P1/P3 | $\chi^2/\mathrm{dof}$ | $\ell\le1600$ |
|---|---|---|---|---|---|
| c54.177 fluid + derived envelope | 220 / 524 / 804 / 1116 | 2.216 | 2.420 | 28.62 | 19.99 |
| c54.178 hierarchy, baryons sharing CDM density | 220 / 532 / 804 / 1124 | 2.115 | 1.969 | 15.14 | 11.39 |
| c54.178 hierarchy, no $\Pi$ source | 220 / 532 / 812 / 1124 | 2.216 | 2.180 | 10.93 | 7.71 |
| **c54.178 hierarchy, complete** | **220 / 540 / 812 / 1124** | **2.201** | **2.201** | **7.14** | **4.17** |
| sky | 220.6 / 538.1 / 809.8 / 1147.8 | $2.256\pm0.077$ | $2.280\pm0.074$ | 0.96 (CAMB) | — |

The second peak is $0.35\%$ out and the third $0.27\%$. The $\ell=1600$ cut is not cosmetic: this
instrument carries $k$ only to $\mathrm{LMAXL}/D_M$, so the top few hundred multipoles score the
truncation rather than the physics.

## A prediction checked against the number it predicted

c54.177 adopted the derived $16/15$ at a cost of $1123$ units of $\chi^2$ and said in terms that the
missing **source** half of the polarisation physics was what that cost measured. Running the same
hierarchy with only those two terms dropped — which is exactly the half an envelope can supply —
gives $2022$ against $1320$: **$\Delta\chi^2 = 702$, $63\%$ of the $1123$.**

## The same lesson twice

**Half the baryon split is worse than none.** Giving the baryons their own density while they still
share the photons' velocity moved $\chi^2/\mathrm{dof}$ from $133$ to $161$ at development settings —
because the density they then carry is the photons' own, oscillating and decaying, with nothing to
let them fall into the wells after decoupling. With both halves it is $15.1\to7.1$. *A physical
effect taken in half is not a small error; it is a different and inconsistent model.* Polarisation at
c54.177, the baryon sector here.

## What is measured rather than argued

- **A double count is impossible rather than merely absent.** The envelope is frozen at the handover,
  so it covers $[\eta_s,\eta_{\rm sw}]$ and the multipoles cover $[\eta_{\rm sw},\eta_0]$ — disjoint
  supports. Only $4.2\%$ of $1/k_D^2$ has accumulated at the handover, so $96\%$ of the damping is
  dynamic. *c54.175 lost a revision to a double count between exactly these two mechanisms.*
- **The arbitrary parts don't matter**: doubling the hierarchy depth moves $\chi^2$ by $0.00\%$;
  doubling the handover opacity by $1.5\%$.

## A hole found by building on the instrument

**The aliasing gate existed only on the delta-function path.** The line-of-sight path has been the
default since c54.173 and had none. It cost a run immediately: a development configuration at 300
modes returned a first peak at $\ell=196$ instead of $220$ and nothing said so. *The failure is
silent by construction — the source comb stays correct while the projected spectrum combs at a
spacing set by the sampling.* The gate is now on both paths; production sits at $5.7$ points per
Bessel period.

## And the CR arm does not move, for the sixth time

$\ell_1/\ell_A = 0.5703$ through a delta-function transfer, a line-of-sight transfer, a derived
damping envelope, a scan of that envelope's scale, a derived shear coefficient, and now the full
hierarchy — while the control's $\chi^2/\mathrm{dof}$ fell from about a hundred to seven.

`L-147`'s verdict is unchanged and the reason is now quantitative: a control seven times worse than a
fit cannot certify what it is compared with. **What has changed is that the gap is a factor of seven
and not a factor of a hundred.** `PO-7` stays protected.

## Gates

All ten gates plus `run_all_receipts` (**288 pass, 0 fail**, 529 s), `lint_assertions` (no hollow
assertions, zero assertion debt), `audit_index` (105/105), and `check_compile` (**17 papers, 0
errors, 0 undefined citations, 0 undefined refs, 0 dead receipt links**).

## New in the tree

- `receipts/P15_CR_cosmology/P15_the_photon_hierarchy_in_the_transfer.py`
- `ACOUSTIC_two_arm.py`: `HIER`, `LG`, `TCSW`, `BSPLIT`, `PISRC`, `KBATCH`, and `alias_gate`
- four banked spectra under `computations/beyond_the_wall/spectra/`

## What is owed next

**The last factor of seven, and there is no longer a named missing sector.** What stands between this
instrument and a control that could arbitrate is accuracy — reionisation, neutrino mass, a lensed
spectrum, and the wavenumber range — not a piece of physics known to be left out.
