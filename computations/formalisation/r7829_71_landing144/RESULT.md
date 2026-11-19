# `r7829+71.2` — RESULT: **campaign 144 landed. All fourteen rows are cited beside their claims, at nine sites in P14, P15 and P18. The three PDFs are rebuilt and committed with their source.** ⌗ `601` words of TeX added (band 700–1,500, estimate 1,100: **below band**), at p `0.6`

*The registration is `PREDICTION.md`. Every site was read at `843b40b54` before it was edited. Each landing is a new
`\noindent` paragraph placed directly after the paragraph that makes the claim, as P15's `Cosmology.lean` sentences
are. No existing sentence is changed.*

## The sites

| Site | Paper, after line | Rows | Lean names cited |
|---|---|---|---|
| S1 | P14:368 (the angle and the reflections) | C2, C11 | `nc_LambdaYM_lt`, `nc_reflections` |
| S2 | P14:611 (fifteen or sixteen) | C8 | `nc_anomalies` |
| S3 | P14:892 (Y2) | C1, C7 | `nc_sixteen`, `nc_charges` |
| S4 | P14:894 (Y3) | C12, C13, C10 | `nc_selfdual_swap`, `nc_det_real`, `nc_dirac` |
| S5 | P14:896 (Y4) | C3, C5 | `nc_f_parity`, `nc_f_diff`, `nc_characters` |
| S6 | P14:898 (Y6, Y7) | C9 | `nc_nariai_max` |
| S7 | P15:610 (the in-force length; `r² − 1`) | C6, C4 | `nc_signature_scale`, `nc_signature_number`, `nc_r2_signs` |
| S8 | P18:2808 (the singlet; the closure of four) | C8, C14 | `nc_anomalies`, `nc_four` |
| S9 | P18:3094 (`ν_R` carries `B − L`) | C7 | `nc_charges` |

Each site says what is *not* formalised wherever the paragraph also rests on a cited result:
- S1: the running, the sign change of the topological term, and `π₃`/`π₄` of `SU(3)`;
- S3: `Spin(6) = SU(4)` and `SO(4) = (SU(2) × SU(2))/ℤ₂`;
- S4: the surviving mixing phase and the two-loop estimates;
- S7: the fitted values, which are the receipts'.

**Conventions are stated where the paper uses two.** P14 normalises hypercharge as `Q = I₃ + Y`, which is what
`nc_anomalies` uses (S2). `nc_charges` uses `Q = I₃L + Y/2`, and S3 says so.

## Verification

- **Build.** `pdflatex` was run twice on each paper, as in `check_compile.py`. All three papers have 0 errors, 0
  undefined citations, 0 undefined references and 0 dead receipt links.
- **Overfull boxes.** A baseline build of the unedited source was made for comparison. P14 is at 134 and P18 at 0, both
  unchanged. P15 went from 787 to 791. None of the four extra boxes is inside or beside the new paragraph: the two
  boxes in that range were present before the edit (a receipt-run line). The other changes are reflows elsewhere in
  the paper. Three first drafts did produce overfull lines (the long `\texttt` path in P15 and P18, and S2's opening).
  They were reworded before commit.
- **Checks.**
  - Gate (`run_touched_readers.sh`): GREEN.
  - `check_formalisation_join`, `check_prose_pins`, `check_paper_pins_present`, `check_source_hygiene`,
    `check_glyph_coverage`, `check_tex_tail`, `check_open_references` and `check_citations_resolve`: all exit 0.
  - `check_pdf_current` refuses to run on this shallow clone. The PDFs are committed in the same commit as their
    source, which is the rule it checks.
- **Names.** Every `nc_` name cited in the papers is a theorem in `probes/NewClaims.lean`.

## Against the registration

- **All nine sites landed, the three PDFs rebuilt, and the gate was GREEN on the first push**, so the joint event
  (p 0.6) held. The named stop, the pin gate (p 0.3), did not occur.
- **Size: below band.** The estimate counted roughly twice the words each landing needed. The paragraphs state the
  Lean content and nothing more.
- **The local toolchain is not the CI's.** It is a TeX Live subset (`latex-extra`, `science`, `publishers`,
  `fonts-extra`) and not `texlive-full`. The `compile` job on main is the verdict on the bytes.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
