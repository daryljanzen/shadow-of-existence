# r7839 (cc66) — a cold read of P14, the matter sector, end to end

**Order:** 69's `r7835`. Read every section in order; check every printed figure against the
receipt its sentence cites; check P14 is in one state and agrees with P16 and P15 on the
right-handed scale's window, the singlets, and Majorana by least-arbitrariness; fix mechanical
defects as read, and list every substantive one with its line and what it should say.

**Receipt:** `receipts/P14_matter_sector_paper/P14_every_printed_figure_reproduces_and_the_single_defect_is_an_unreceipted_discriminant_that_names_the_conjugate_crest.py`
— 62 arms, ALL PASS.

## The verdict

Every printed figure in P14's 1018 lines reproduces. 118 `\rcpt` sites resolve to 98 distinct
receipts, every one of which exists on disk, and none is cited for a figure it does not carry.
P14 is in one state and contradicts neither P15 nor P16.

## The one substantive defect — line 745, and it is sharper than it first looked

`\S`cosmogenesis` said the Nariai crest is the point "where two of the three horizon roots merge
(the discriminant `$4-3r_0^2$` vanishing)". Under the paper's own parametrisation
`2M = r_0 - r_0^3` (lines 84, 694), the discriminant of the horizon cubic `r^3 - r + 2M` through
the designated root is

    -4(-1)^3 - 27(2M)^2  =  (4 - 3 r_0^2) (3 r_0^2 - 1)^2

verified to `9.9e-14` over `2e5` random `r_0`.

**The named factor does not merely drop a factor — it vanishes at the wrong crest.**
`4 - 3 r_0^2 = 0` at `r_0 = 2/sqrt3`, where `2M = -2/(3 sqrt3)`: the negative-mass crest, the
`R`-image. At the crest the sentence is about, `r_0 = 1/sqrt3` with `2M = +2/(3 sqrt3)` — the
member the paper's own Lean-checked maximum at line 916 singles out — the discriminant vanishes
through `(3 r_0^2 - 1)^2`, while `4 - 3 r_0^2` equals **3**.

The sentence carried **no receipt**, citing only `\cite{Nariai1951}`.

**What it should say, and now does:** `(the discriminant $(4-3r_0^2)(3r_0^2-1)^2$ vanishing)`,
cited to this receipt. The correction is settled by the paper's own machine-checked identity at
line 916 and by the receipt's arms, so no reading of 69's was needed for it.

## The dating, which is the point

`git log -L 745,745:corpus/matter_sector_paper.tex` dates the defective line to **`r6683`**, with
`r6679`, `r3137` and `r2419` before it. The Y-series prose 170 lines later — the Majorana and
right-handed-scale material — was rewritten the same day by `20e207cd1` (Y17), and before that at
Y15, Y14 and Y13, and it is **clean**.

⇒ **The risk sat where a claim's precision was never re-derived, not where the edits were.** That
is registered prediction ③ and the P15 guard, transferred and confirmed.

## One precision note, not a defect

Line 914 prints the collider bound on the ratio of vacuum values as "below about `$10^{-2}$`" and
the exclusion as "a factor of thirty". `2/(3 sqrt3) / 10^-2 = 38.5`, not 30; the thirty comes from
the `Y7` receipt's **unrounded** `0.0125`, where the factor is `30.8`. Both printed numbers are
right, and `Y7` is cited, so nothing is owed. Recorded because the two are consistent only through
the unrounded bound.

## Cross-paper

- **Majorana.** P14 carries *both* the experimental decider (neutrinoless double-beta decay) and
  the least-arbitrariness reading, and attributes the latter to P16 by `\cite{JanzenCosmogenesis}`.
  No contradiction.
- **The singlets.** External, one per generation leaving the light neutrinos massless, carrying no
  colour. Stated identically in P14 and P15.
- **The window.** `10^-11` to `10^-5`, whose ends are exactly `v_L/v_R` at the cap `2e13` GeV
  (`1.23e-11`) and the floor `3.5e7` GeV (`7.03e-6`), rounded outward, and which contains the
  unifying models' `10^-8` as the sentence says.
- **Set comparison.** The three figures P14 and P15 both print on this material
  (`1.2e15`, `3.5e7`, `1.2e10`) are the same three, and neither paper prints a neighbouring value
  of any of them. P14 defers the `0.05` eV splitting to P15 rather than restating it — one state
  across two papers, not a disagreement.

## The registered predictions

All five substantive ones **hit**, against three of four missed on P15:

| # | registered | outcome |
|---|---|---|
| ① | 0–3 substantive defects | **1** |
| ② | precision/qualifier class, 0 superseded figures | **precision class; 0 superseded** |
| ③ | NOT at the Y-series seams | **`r6683`, 170 lines from the Y17 rewrite** |
| ④ | 0 contradictions with P16/P18 | **0** |
| ⑤ | ≥90% of figures reproduce | **100%** |

The method predictions held too: ⑦ every paper figure parsed rather than retyped (the direct
consequence of `r7837`'s unread-figure finding); ⑧ no rewording without establishing which the
receipts own — the one fix is settled by the paper's own Lean identity; ⑥ a locally-excluded gate
did catch a first draft, this time `check_figures_pinned`'s own rule, which is why the baryon-ratio
arm now parses the printed integer and the printed power rather than recomputing both sides from
the same constant.
