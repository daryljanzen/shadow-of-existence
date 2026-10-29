# r7637+70 ① — every P15 sentence that cites a c54 receipt, and what carries it

The c54 receipts are now pinned HISTORICAL. Each has a docstring naming the superseded state, and a guard that fails unless it reads the LEAFREC=0 namesake. Each P15 sentence citing one of them (line numbers are `corpus/CR_cosmology.tex` at r7637) is either:
- **INSTRUMENT**: the claim is about that superseded instrument. It leaves P15 or is restated as history.
- **CONSTRUCTION**: the claim is about the construction. It is carried by the arm-of-record figure named below.

**1. l.606, `height_target`.** P15 says "what this construction returns for the same quantity is $2.264$ on the polarisation path…" (P₁/P₂).
- **Type:** CONSTRUCTION.
- **Carried by:** P₁/P₂ on the arm of record is **2.135** (r7633 `census_peaks_refit.txt`, the PO-47 locator on `verify_cr_leafrec1`). On the fine grid it is **2.136** (`r6941_fine_cr_leafrec1`; the ladders receipt, re-pointed).
- **Note:** 2.264 was the pinned arm's. The sky's 2.2564 ± 0.0772 and ΛCDM's 2.200 do not move. The arm now sits **1.6σ below** the sky, where the pinned arm sat on it.

**2. l.845, `photon_hierarchy`.** "The control is the arm whose answer is known independently, and it reproduces it."
- **Type:** INSTRUMENT, and about the CONTROL.
- **Carried by:** C59 (`the_control_reproduces_camb…`), already co-cited. The c54 cite can go.

**3. l.910, `height_target`.** "both are removed in this configuration: the wavenumber integral is carried past the reported multipole, and the projection carries the polarisation source".
- **Type:** INSTRUMENT, restated for the arm of record.
- **Carried by:** the arm of record's own config (`verify_cr_leafrec1`, `config`). It runs at KFAC 2.0 (k_max = 2·LMAXL/D_M; the alias gate's 2.00) with HIER=1, the polarised photon hierarchy. Both removals hold there; they are the ruled defaults.

**4. l.913, `control_entered_the_regime`.** "it was 78% of the control's remaining χ², and taking it out brings the control to 1.18 per degree of freedom … against a reference 1.01".
- **Type:** INSTRUMENT (the control's convergence history at KFAC=1 → L3000).
- **Restate as history:** the truncation was removed for good at r3870 (KFAC=2). The control does not move with LEAFREC, so the figure stays true of that history.

**5. l.931, `phase_is_the_driving`.** "removing every coupling to the potential moves the control's first peak from 220 to 274 and ℓ₁/ℓ_A by 0.1792 … Run on this arm the same subtraction gives 0.1717".
- **Type:** CONSTRUCTION.
- **Carried by:** on the arm of record, `c54.193_cr_nodrive_L3000_leafrec1` against `c54.186_cr_L3000_leafrec1`. The first peak moves **220 → 276**, Δℓ₁/ℓ_A = **0.185** against the control's 0.179, so the arm's grip is **3% above** the control's (P15: "within four per cent … slightly" below).
- **Also moved:** the driving's intercept is −0.1242 against the control's −0.1274, a factor of 1.0.
- **Note:** the c54.193 receipt's "driving accounts for 98%" belongs to the pinned arm and leaves P15.

**6. l.955, `where_the_likelihood_sits`.** "And the likelihood is run, both arms scored on the same bins by the same code…"
- **Type:** CONSTRUCTION (the method).
- **Carried by:** the arm of record's own score, **297.7 against the control's 186.5** on the 185 bins (`P15_on_the_arm_of_record…`, r7633).
- **Note:** the c54 receipt's own figures (51817, F3 +50496) are the pinned arm's. On the arm of record its form gives −396.5, which means nothing (unlensed, truncated). The cite should go.
- **Elsewhere in this sentence:** 214.1/550.5 and the factor 2.57 belong to cc66's full-range and 133-bin receipts (the 133-bin factor moves 1.99 → 1.60, r7635).

**7. l.2051, `floor_is_a_distance`.** "taken as a distance between the two models … independent of the configuration's own floor".
- **Type:** INSTRUMENT. The claim is methodological, but its support was the pinned arm's margin (827× to 2438×).
- **On the arm of record:** the same F3 is **706**. The margin falls to **11× to 33×**, and the receipt's own refusal fires ("the reference choice reaches the verdict").
- **Restate:** keep the method, drop the "three orders of magnitude". Or carry it on the arm of record's 297.7 − 186.5 = 111.2, which is not a floor-free figure.

**8. l.2424, `phase_moves_with_the_datum`.** "a contraction of the sky's size is resolved while the smaller ones at lower ℓ are not".
- **Type:** INSTRUMENT (the multipole grid's resolution).
- **Carried by:** the arm of record's fine grid (`r6941_fine_cr_leafrec1`, LSTEP=1). It resolves to one multipole and agrees with the coarse grid to 5e-16 at shared ℓ.
- **Note:** the c54.195 seam-phase figures (φ/π spans) are the pinned arm's and leave P15.
