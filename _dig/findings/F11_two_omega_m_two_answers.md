# F11 — P15 quotes ρ_r/ρ_m at the angle-fixed onset as both **1.71** and **1.69**, because the two receipts backing those sentences run CR's own rate at different Ω_m (0.3066 vs 0.3150)

*status: BOUNDED NEGATIVE (verified at source, this cut). Both numbers are correctly receipted; the receipts disagree with each other.*
*scope: `corpus/CR_cosmology.tex` §tensions (the "inherited datum" paragraph) and the withdrawal paragraph ~40 lines later; `P15_the_ratio_is_the_onset_in_imported_units.py`, `P15_zonset_determinations.py`.*
*found by: cross-paper numeric consistency sweep over the 137 decimal literals — the same symbol quoted twice with different values.*

---

## The two sentences

**§tensions, the inherited-datum paragraph** (cites `P15_the_ratio_is_the_onset_in_imported_units`):

> *with Ω_m held at its fitted value the ratio is **2.01** at H₀=67.4 and **1.71** at H₀=73, the two
> readings coinciding at **H₀ ≃ 68** where Ω_m h² reproduces the microwave-background-inferred
> ω_m = 0.143.*

**~40 lines later, the withdrawal paragraph:**

> *at the directly measured H₀ the angle-fixed onset carries ρ_r/ρ_m = **1.69** rather than 2.0.*

Same quantity, same conditions, two values.

## Why

Both are correctly receipted. The receipts disagree on Ω_m.

| receipt | Ω_m | ω_r | z_onset (angle-fixed) | ρ_r/ρ_m at H₀=73 |
|---|---|---|---|---|
| `P15_the_ratio_is_the_onset_in_imported_units` | **0.3066** | 4.15e−5 | **6747.3** | **1.714** → *1.71* |
| `P15_zonset_determinations` | **0.3150** | 4.1833e−5 | **6797** | **1.694** → *1.69* |

Reproduced by running **one** code path — the CR radiation-free rate `H = H₀√(Ω_m a⁻³ + Ω_Λ)` pinned
to the measured 100θ_* = 1.04109 — under each receipt's constants:

```
Om=0.3150 wr=4.1833e-05  -> z_onset=6796.7   H0=73: rho_r/rho_m = 1.6940
Om=0.3066 wr=4.15e-05    -> z_onset=6748.4   H0=73: rho_r/rho_m = 1.7143
Om=0.3070 wr=4.15e-05    -> z_onset=6750.7   H0=73: rho_r/rho_m = 1.7127   (the paper's DESI value)
```

Both receipts compute **CR's own** determination — neither is a ΛCDM reference — and they differ by
**0.74% in z_onset** and **1.2% in the ratio**.

## And the "coincidence at H₀ ≃ 68" moves with it

The §tensions sentence locates the crossing where Ω_m h² = 0.143. Under Ω_m = 0.3066 that is
**H₀ = 68.3** (the receipt says so explicitly). Under Ω_m = 0.3150 it is **H₀ = 67.4** — look at the
table above: ω_m = 0.14310 at H₀ = 67.4 already *is* the CMB-inferred value.

So the argument's own pivot — *"the factor of two is exact at h ≃ 0.68"* — is itself Ω_m-dependent,
and moves from 67.4 to 68.3 across the two receipts the paper cites in the same section.

## The wider spread

Surveying the P15 receipt set, Ω_m appears as **0.3066**, **0.307**, **0.31**, **0.3150**, and
~0.3153 (derived from CAMB's ω_b + ω_c + m_ν). A 2.8% spread.

**Most of that is legitimate and should not be touched.** `BUILD_camb_store`,
`P15_camb_reference`, `P15_damping_ratio_clean` and `P15_full_transfer_verdict` deliberately run
Planck's ΛCDM cosmology at Ω_m ≈ 0.315 as the *reference* the CR result is measured against — using
CR's fitted Ω_m there would be the error, not the fix.

**The one that bites is `P15_zonset_determinations`**, which uses the reference value 0.3150 while
computing CR's own radiation-free quantity. That is very likely how it happened: the file's header
says it was *"built on the conventions of `storyboard_receipts/RATE_assignment_map.py`"*, and a
reference-side constant travelled with the conventions.

## What is and is not damaged

**Not damaged, and worth saying first:**

- **z_onset's H₀-independence** — the load-bearing property — is verified in *both* receipts and is
  untouched. `the_ratio_is_the_onset` gets 6747.3 at H₀ = 67.4/70/73/74 with **zero** spread.
- The falsifiable claim (*radiation carries no term in the expansion rate*) is untouched.
- The DESI confrontation uses Ω_m and BAO ratios, at 0.307, and never ω_m.

**Damaged:** one number, quoted twice, differently, in one section — and the pivot of the argument
that number is serving.

**And the finding supports the paper's own conclusion rather than undercutting it.** §tensions
already says *"the factor of two … should be quoted as an order-unity band, not as a determined
number."* This widens the band's provenance: it is not only the H₀ range (1.71–2.01) but the Ω_m
choice (1.69–1.71 at fixed H₀). The paper's instinct was right and its own receipts demonstrate it
more strongly than the text claims.

## Recommended, stated for reversal

1. **Pick one Ω_m for CR's own determinations** and state it once. The DESI-fitted 0.307 or the
   0.3066 the perturbation receipts run on — the source's call, but not two.
2. Change `P15_zonset_determinations.py`'s `Om = 0.3150` to that value, or add a line saying why the
   reference value is deliberate there. Currently nothing in the file marks the choice.
3. Make the two sentences agree, and say which Ω_m they are at. If they are meant to be at different
   Ω_m, say that — it would be a *better* sentence, since the pair then demonstrates the band.
4. Move the "coincides at H₀ ≃ 68" claim inside the same convention, or state it as a range
   (67.4–68.3) — which is what the two receipts jointly show.

## Not claimed

- No claim that either receipt is wrong. Each is internally consistent and each backs the sentence
  that cites it.
- No claim about which Ω_m is correct. That is a fitting question and is the source's.
- No claim that the ΛCDM-reference receipts at 0.315 are wrong — they are right to be there.
- The Hubble/acoustic result is **RESOLVED and banked** per the README and is not reopened here:
  nothing above touches the rate, the H₀-independence, or the acoustic scale. This is a bookkeeping
  finding about one derived ratio.
- No closure on any registered item. L-150 (`F·1`) remains open and this does not bear on its target,
  which L-149 already restated as an order-unity band.
