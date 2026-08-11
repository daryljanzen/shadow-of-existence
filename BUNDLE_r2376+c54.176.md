# BUNDLE r2376+c54.176 — the height target was below the resolution of its own statistic

**Two parts, each under 30 MB, no file split across parts.**

- `CR_bundle_r2376+c54.176_part1_corpus.tar.xz` — top level + `corpus/ figures/ receipts/ verification/`
- `CR_bundle_r2376+c54.176_part2_working.tar.xz` — every other working directory

## What this revision is

**A correction to my own measurement protocol, on front #2.** Since c54.168 every height claim in
this fork — $-13\%$, $-34\%$, $2$–$3\%$, $-0.05\%$ — compared $P_1/P_2$ and $P_1/P_3$ against two
bare numbers, $2.217$ and $2.277$, with no uncertainty attached. **Read off the `plik_lite`
bandpowers with the published covariance the sky's own ratios are $2.256\pm0.077$ and
$2.280\pm0.074$ — $3.4\%$ and $3.2\%$.** The $13\%$ and $34\%$ were four and ten sigma and stand.
**The $2$–$3\%$ is about one sigma and does not.**

Front #2's target — sub-per-cent *heights* — is retired, because it asked for several times more
precision than the statistic it was quoted against possesses. The replacement is the statistic that
was doing the work all along: $\chi^2/\mathrm{dof}$ on the $\Lambda$CDM arm, $22.5$ against CAMB's
$0.96$.

## Five things, in order

1. **The numerics were cleared before anything was attributed.** $1.4\times$ the modes, $1.3\times$
   the $k$-range and $1.8\times$ the $\eta$-sampling move the ratios by $0.09\%$ and $0.37\%$. The
   $2\%$/$7\%$ swings that prompted the check came from `LMAXL=1300`, which sets $k_{\max}$ and was
   truncating the $k$ integral under the **third** peak.
2. **The sky's error bar, from the full $2\times2$ covariance block and not a diagonal estimate.**
   Caught by bookkeeping rather than by suspicion: `X_data` is binned $C_\ell$ and not $D_\ell$, so
   peak-finding on it returned $464/761/1085$ instead of $221/527/815$.
3. **A claim of mine is withdrawn at its own error bar rather than published.** I had written that
   the two ratios select different damping *scales*, so no coefficient can fix both and the residual
   is the envelope's *shape*. A scan of one multiplier on $1/k_D^2$ gives $1.094\pm0.184$ and
   $0.897\pm0.055$ — **a split of $1.03\sigma$. It does not carry.**
4. **$\chi^2$ over $185$ bins does separate the coefficients, prefers $8/9$ over $16/15$ by $1123$,
   and is not allowed to choose.** The minimum sits at a multiplier of $0.865$ against $8/9$'s
   $0.859$. I had changed the shear coefficient to $16/15$ earlier in this revision on recollection
   of the standard polarised result; it is changed back — **not because $8/9$ fits better**, but
   because neither value has ever been derived in this corpus and a remembered number is not a
   derivation any more than a fitted one is. *What the $1123$ measures is a residual error in the
   damping tail of a size a coefficient could absorb, which is exactly why it must not.*
5. **`L-147`'s pinned $\chi^2$ values are recomputable for the first time.** They were produced by a
   script in `/tmp` and typed into a receipt.
   `computations/planck_tt_likelihood/chi2_of_spectrum.py` puts that machinery in the corpus and
   returns $4170.2$ and $50675.2$ exactly from spectra banked under
   `computations/beyond_the_wall/spectra/`.

## Gates

All ten gates plus `run_all_receipts` (**286 pass, 0 fail**, 808 s), `lint_assertions`
(no hollow assertions, zero assertion debt), `audit_index` (105/105), and `check_compile`
(**17 papers, 0 errors, 0 undefined citations, 0 undefined refs, 0 dead receipt links**).

## New in the tree

- `receipts/P15_CR_cosmology/P15_the_height_target_was_below_the_resolution_of_its_own_statistic.py`
- `computations/planck_tt_likelihood/chi2_of_spectrum.py`
- `computations/beyond_the_wall/spectra/` — ten banked spectra and their provenance

## What is owed next, named

**The free-streaming photon hierarchy carrying the polarisation multipoles**, from which the shear
coefficient falls out instead of being chosen — validated on the $\Lambda$CDM arm before this
construction is touched.
