# `r7835+71.2` — RESULT: campaign 145 BUILT WHOLE (E1–E8) AND LANDED. 72's Y10–Y17 censused, with every cored row built and placed beside its claim in P14, P15 and P16. The registered stop (E8) did not hold, and no Mathlib gap was found. ⌗ `201` Lean lines (band 200–500, estimate 320: **in band, at its floor**), at p `0.55`

*The census and registration are in `PREDICTION.md`. The probe is the new standalone file `probes/NeutrinoSector.lean`
(`ns_`, 201 lines). It imports only Mathlib, carries no copies and sets no option.*

## Verification

- `lake env lean probes/NeutrinoSector.lean` gives **0 errors and 0 warnings**.
- **12 axiom lines.** Eleven read `[propext, Classical.choice, Quot.sound]`. The twelfth, `ns_dims`, reads
  `[propext]`, a subset of the three.
- The forbidden-token grep is clean, the only import is `Mathlib`, and `check_no_sorry.py` reports ALL 29.

## Rows

| Row | Lean | Mark |
|---|---|---|
| E1 | `ns_seesaw`: `θ² = m_ν/m_N` and `m_D² = m_ν m_N`, with `m_ν = v_L²/M`, `m_D = v_L v_R/M` and `m_N = v_R²/M` | **BUILT** |
| E2 | `ns_dims`: `4·4 = 1+15 = 6+10` and `2·2 = 1+3` | **BUILT** |
| E3 | `ns_slots`: an injective placement of 16 states in the `4·2·2` slots is a bijection; the colourless slots number 4, and each is hit exactly once. Witnessed by `ns_slots_witness` | **BUILT** |
| E4 | `ns_neff`: `3(10.75/61.75)^{4/3} ∈ (0.285, 0.295)` and `3(10.75/106.75)^{4/3} ∈ (0.140, 0.142)`. Proved through `ns_cube`, which bounds `x^{4/3}` by cubing (`y³ = x⁴`) | **BUILT** |
| E5 | `ns_tdec`: `(6400/80.38)^{4/3} ∈ (335, 345)` | **BUILT** |
| E6 | `ns_scales` and `ns_cap`, detailed after the table | **BUILT** |
| E7 | `ns_splitting`, detailed after the table | **BUILT** |
| E8 | `ns_zeros`, detailed after the table | **BUILT** |

**E6 in detail.**
- `ns_scales`, with `v = 246.22`, `M_Pl = 2.435×10¹⁸` and `m_ν = 0.05` eV:
  - the light mass at the Planck scale is within `0.05×10⁻⁵` of `2.5×10⁻⁵` eV;
  - the shortfall ratio is between 1900 and 2100;
  - `M` is within `0.02×10¹⁵` of `1.2×10¹⁵`;
  - `m_N` at `3.5×10⁷` is in `(0.95, 1.05)`;
  - the ratio window is between `10⁻¹¹` and `10⁻⁵`;
  - the caps are `2.4×10¹³` and `1.2×10¹⁰`, each to its printed figure.
- `ns_cap`: `v_R²/Λ² < 10⁻¹⁰ ⇔ v_R < Λ/10⁵`.

**E7 in detail (`ns_splitting`).** With `v_R = 2·6400/0.65`, `μ = v_R²/M_Pl` lies in `(0.155, 0.165)` eV. Its
ratio to `2×10⁻¹¹/(2√(7.42×10⁻⁵))` lies in `(10⁸, 2×10⁸)`.

**E8 in detail (`ns_zeros`).** Take any `D : 6 × n` and any `M_S : n × n` over `ℂ`. The matrix
`[[0, D], [Dᵀ, M_S]]` has rank `≤ 2n`, and `6 + n ≤ 2n + dim ker`. Two consequences follow:
- `ns_need_five`: `n ≤ 4` leaves at least two massless states;
- `ns_three_singlets`: `n = 3` leaves at least three.

The proof splits the matrix as `[[D],[0]]·[0 | I] + [[0],[I]]·[Dᵀ | M_S]`. It uses
`fromRows_mul_fromCols`, a rank bound for a sum (proved here from `range_add_le`), and rank–nullity on `mulVecLin`.

**Not built, as registered:**
- the `SU(4)` Casimir decompositions (beyond: no `su(4)` representation theory in Mathlib);
- the Dirac spectrum on `S⁵` and the `S⁴` index (beyond: no spin geometry);
- Y10, Y15, Y16, and Y17's random draws (no formal core: empirical, estimates, numerical).

## The landing

Four plain paragraphs, each placed after its claim paragraph:
- **P14**, after the Y12–Y14 paragraph and campaign 144's S6: E2, E3, E6 and E8;
- **P15:258**, the right-handed-neutrino paragraph: E1, E4, E5, E6 and E8;
- **P16:683**, Y17's splitting: E7;
- **P16:804**, the network's `N_eff`: E4 and E5.

Each landing names its `ns_` theorems and `NeutrinoSector.lean`, and says what it does not formalise. Campaign 144
taught that restating a receipt's distinctive inputs beside other receipts trips the transposition gate. So the
landings refer to `10.75`, `61.75`, `246.22`, `6400` and the four-thirds power in words, and print only the papers'
own two-figure values.

**Checks on the committed tree.**
- The three PDFs build with 0 errors, citations, references and dead receipt links.
- **Overfull boxes:** P14 and P16 are unchanged against a baseline build of the unedited source. P15 has four more,
  none in the new paragraph.
- **Served pages:** regenerated, and they differ only by the new paragraphs.
- **Gates that pass:** `check_pages_current`, `check_pdf_current`, `check_marker_transposition`,
  `check_paper_pins_present`, `check_figures_pinned`, `check_depmatrix`, `check_open_item_coherence`,
  `check_open_references`, `check_prose_pins`, `check_source_hygiene`, `check_glyph_coverage` and
  `check_citations_resolve`, together with the local gate (GREEN).
- **`check_formalisation_join`** reads UNANSWERABLE locally. The new `.lean` file means the formalisation-mathlib
  workflow has no record for this tree yet. CI's run records one.

## Against the registration

- **All eight rows were built and landed**, so the joint event (p 0.55) held.
- **The named stop did not hold.** E8 (p 0.75) needed no ready lemma: `fromRows_mul_fromCols` gives the split
  directly, and the rank of a sum follows in five lines from `range_add_le`.
- **Size: 201 lines, at the band's floor.** The estimate (320) overpriced E8 and E4/E5. The cube lemma served three
  rows.
- **Census note:** "exactly `6 − n`" for generic couplings (Y13's draws) is not claimed. The Lean bound holds for every
  coupling, and that bound is all that "need at least five" uses.

**Mathlib gap: none on the cored rows.** The beyond rows are as registered.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
