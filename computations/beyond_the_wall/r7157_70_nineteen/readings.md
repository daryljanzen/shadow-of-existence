# r7157+70.1 — the 19 `NO-READ/FIGURE` sites, read against their papers

*Read at `ce28242c`.  The repair of each is its author's; this records where the figure is and the repair shape.*
*Line numbers are `corpus/<paper>.tex` lines at `ce28242c`; a repair parses by the anchor and the sentence, never by line.*

| # | receipt : line | figure attributed | where the paper prints it | class | repair shape |
|---|---|---|---|---|---|
| 1 | `L274/H1…:200` | "recovery by l≈8" | `CR_cosmology` `sec:largescale`, "recovering by $\ell\approx8$" (unique) | **PARSE** | parse `\ell\approx(\d+)` after "recovering by" |
| 2 | `L831/G1…:90` | P03 sec:tour timelike = 3 | `SdS-slicing-curve_v2` `sec:tour`, the display `timelike ⟺ same hinge (3)` | **PARSE** | parse the three counts from the one display |
| 3 | `L831/G1…:91` | spacelike = 6 | same display, `(6)` | **PARSE** | same |
| 4 | `L831/G1…:92` | null = 6 | same display, `(6)` | **PARSE** | same |
| 5 | `P05_deck_group_S3:70` | order 12 | `groupoid_paper` `sec:classification`, `\cong D_{6}\quad(\text{order }12)` | **PARSE** | parse `order }(\d+)` in the section |
| 6 | `P10_the_adiabatic_residual…:90` | 0.61 | `canonical_time`: "this gives $0.61$ at $n=2$, $0.44$ at $n=3$, and $0.16$ by $n=10$" | **PARSE** | parse all three from the one sentence |
| 7 | `…:91` | 0.44 | same sentence | **PARSE** | same |
| 8 | `…:92` | 0.16 | same sentence (and the line before) | **PARSE** | same |
| 9 | `…:95` | 2.32 | `canonical_time`: "larger by a factor $2.32$" (unique) | **PARSE** | parse after "larger by a factor" |
| 10 | `P10_the_floor_is_forced…:187` | 15/4, "sec:lock's own L" | `canonical_time` `sec:lock`, "$\tfrac{15}{4}$, the $1/m$ term of …" | **PARSE** | parse `\tfrac{(\d+)}{(\d+)}, the \$1/m\$ term` |
| 11 | `P10_the_subtraction_is_at_operator_dimension_six…:141` | operator dimension 6 from inverting the order rule | `canonical_time`: "$2k-4$ exactly, … second order admits one operator dimension and no other"; "At dimension six" in words | **DERIVATION** | parse the rule `2k-4`, solve at order 2, assert the paper's "dimension six" |
| 12 | `P10_the_thermal_condition…:146` | "ten at the floor" | `canonical_time`: "ten at the floor $n=2$" (unique, in words) | **PARSE** | parse the word before "at the floor" |
| 13 | `P14_the_lifts_own_measure…:158` | λ < 3/4, "the number sec:lift states" | `matter_sector_paper` (twice, one paragraph): "the condition $\lambda<\tfrac34$" | **PARSE-AMBIGUOUS** | ⛔ **`sec:lift` is not a label anywhere in the corpus** (only `sec:lift-initial-rate` and `sec:lift-quantum`, in `CR_framework`, which print no 3/4). The anchor must be corrected first |
| 14 | `…:190` | "sec:lift's rejection", 3/4 | same | **PARSE-AMBIGUOUS** | same dead anchor |
| 15 | `P14_the_propagating_three…:297` | λ ≡ 0 mod 3, "sec:whichthree's own" | `matter_sector_paper` `prop:wall` ("$\lambda\equiv0\pmod 3$"), **not in `sec:whichthree`** | **PARSE-AMBIGUOUS** | the attribution names the wrong section; anchor on `prop:wall` |
| 16 | `C62…:351` | 185 bins | `CR_cosmology`, three sentences, consistent ("$185$ full-range bins", "on $185$ bins", "$185$ bins") | **PARSE-AMBIGUOUS** | needs an anchor to pick one; all three agree today |
| 17 | `P15_the_low_multipole_depth_gap_closes…:301` | sec:largescale's 0.473 / 0.410 / 0.356 / 0.676 | `sec:largescale` now prints **0.487 / 0.435 / 0.359 / 0.666** (three times), and nowhere the receipt's four | ⛔ **DRIFTED** | the label attributes figures the section no longer prints; the author must say whether the receipt's control values were ever the section's |
| 18 | `P15_the_sky_phase_fit…:45` | φ/π = −0.2404 | `CR_cosmology`: "gives the sky $\phi/\pi=-0.2404$" (unique) | **PARSE** | parse after "gives the sky" |
| 19 | `P15_the_sky_phase_fit…:61` | "the paper's quoted 0.008" (σ(φ/π)) | **not printed as σ(φ/π)** any more; the paper's only `0.008` is "$0.008$ per cent against a floor of $0.6$ per cent", a different quantity | ⛔ **DRIFTED** | ⌗ the r7147 operator filed this `IN-PAPER` on a token match: the 86.5 % chance control, observed on a live site |

**Tally:** `PARSE` **12** · `PARSE-AMBIGUOUS` **4** (two of them a dead anchor, one a wrong section) · `DRIFTED` **2** · `DERIVATION` **1** · `NOT-IN-PAPER` **0**.
