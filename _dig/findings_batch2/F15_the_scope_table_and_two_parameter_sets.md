# F15 — The scope table, and its first yield: P15's receipt layer carries **two parameter sets**, and the paper draws on both

*status: instrument (offered) + BOUNDED NEGATIVE (verified at source, this cut).*
*artefact: `DRAFT_receipt_scope_table.py` — runs in ~1 s, no dependencies. Widens F11 (batch 1).*

---

## The instrument, and the gap it fills

Batch 2's findings share one shape: **a claim verified at one point of a family, stated as if it
held on the family** (F12, F13, F14 — and F11 in batch 1).

- `check_receipts` verifies a citation **resolves**.
- `DRAFT_check_numbers_at_citations` (batch 1) checks the cited receipt **computes the number**.
- **Nothing asks what the receipt's scope is.**

`DRAFT_receipt_scope_table.py` does the first half: for every receipt, the parameter settings it
hard-codes — including default-argument values, which are what a receipt runs at when called bare.
The second half (does the citing sentence quantify more widely?) is a reading, not a computation.
**The table makes the reading cheap.**

It carries a `DELIBERATE` allowlist so that receipts running Planck's ΛCDM at ~0.315 as the
*reference* the CR result is measured against don't show up as drift — forcing CR's fitted value
there would be the error. Curating that list is the maintainer's job; everything **not** on it is a
question someone chose not to answer yet.

```
scanned 249 receipts; 33 hard-code at least one tracked parameter
Omega_m takes 6 distinct settings inside P15_CR_cosmology
H0      takes 4        omega_r takes 2        ombh2 takes 2        z_rec takes 2
M       takes 2 distinct settings inside P14_matter_sector_paper
```

## The yield: there are two parameter sets, not a scatter

Sorting the P15 spread by which receipts move together, it is not noise — it is **two internally
consistent sets**:

| | Ω_m | z_rec | z_onset | ω_r | ω_b h² |
|---|---|---|---|---|---|
| **Set A** — the C-chain (§envelope-consequence) | **0.307** | **1100.0** | 6797 | — | 0.0224 |
| **Set B** — ROBUST / UNC / the-ratio (§tensions, the integrator) | **0.3066** | **1089.9** | 6747.3 | 4.15e−5 | 0.0224 |
| *(outlier)* `P15_zonset_determinations` | 0.3150 | 1089.9 | 6797 | 4.1833e−5 | 0.02237 |
| *(outlier)* `P15_verify_numeric` | 0.3153 | — | — | — | — |

Set A is `C5b_baryon_term`, `C8_diffusion_length`, `C11_early_isw` — the eleven-step derived-pieces
chain L-148's strike celebrates. Set B is `ROBUST_p1p2_scan`, `UNC_error_budget`,
`P15_the_ratio_is_the_onset_in_imported_units`, `C11TEST_radiation_zeroed`.

**F11's 1.71-versus-1.69 sits exactly on the seam between them.**

## What the difference is worth

Computed on one code path, swapping only the set:

| set | Ω_m | z_rec | r_s [Mpc] | D_M [Mpc] | 100 θ_* |
|---|---|---|---|---|---|
| **B** | 0.3066 | 1089.9 | **135.360** | 13004.6 | **1.04087** |
| **A** | 0.307 | 1100.0 | **134.336** | 12999.8 | **1.03337** |

> **r_s differs by 0.76 %, 100 θ_* by 0.72 %.**

The measured value is 100 θ_* = **1.04109**. Set B reproduces it to **0.02 %**; set A misses by
**0.74 %** — because 1100 is a round number and 1089.9 is the measured recombination redshift.

**And that is not by itself a defect of the C-chain.** Its outputs are *ratios* — r_D/r_s,
θ_D/θ_* — where the z_rec sensitivity largely cancels, and it is not claiming to hit θ_*. What the
number does is size the seam: two sets, differing by three-quarters of a percent in the quantity the
cosmology's headline is measured in, **and nothing in the tree records that there are two.**

## Recommended, stated for reversal

1. **Say there are two sets, and why.** If z_rec = 1100 is a deliberate round number for a
   leading-order piece, one comment per receipt makes it deliberate instead of ambiguous — the
   `DELIBERATE` allowlist is exactly the place.
2. **Pin the CR-side Ω_m once.** Four values are in use for CR's own quantities (0.3066, 0.307,
   0.31, 0.3150/0.3153). The paper text says *"the single CMB-calibrated Ω_m = 0.307"*, and
   `H0_acoustic_angle_and_seam.py`'s own comment calls **0.31** *"the corpus's CMB-calibrated value,
   quoted in P15"* — which P15 does not say.
3. **Run the scope table once per major revision** and curate `DELIBERATE`. The list of explained
   settings is more valuable than the report: it is the record of which choices were made on
   purpose.

## Not claimed

- **No claim that any receipt is wrong.** Each is internally consistent; several of the differences
  are certainly deliberate and I have marked what I could identify.
- **No claim that the C-chain's results are affected.** Its outputs are ratios; sizing the seam is
  not the same as propagating it, and I did not propagate it.
- No claim about which set is correct — that is a fitting question and is the source's.
- The Hubble/acoustic result is **RESOLVED and banked** per the README and is not reopened: nothing
  here touches the rate, the H₀-independence of z_onset, or the load-bearing claim.
- **Absence from the table is not evidence of scope** — it reads assignments, not semantics, so a
  receipt that computes or sweeps a parameter shows nothing.
- No closure on any registered item.
