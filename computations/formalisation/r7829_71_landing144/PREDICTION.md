# `r7829+71.1` — REGISTRATION: landing campaign 144's fourteen rows in P14, P15 and P18

*The order is 69's `r7829`: land campaign 144's rows in the papers, as was done for campaigns 140 and 141. Each claim
gets a sentence beside it naming its Lean statement and `NewClaims.lean`, in the form of P14's `prop:wall` paragraph
and P15's `Cosmology.lean` sentences. Each landing site is read before it is edited, and each touched PDF is rebuilt
and committed with its source. This is registered before any paper is edited.*

## The sites, read at `843b40b54`

Each landing is a separate paragraph set directly after the paragraph that makes the claim, as P15's `Cosmology.lean`
sentences are. No existing sentence is edited.

| Site | Paper:line | Paragraph's claim | Rows |
|---|---|---|---|
| S1 | P14:368 | `Λ_YM` lies below `μ`; `P` and `T` reverse the cut's orientation, `R` does not | C2, C11 |
| S2 | P14:607 | the index and the anomaly conditions are blind to fifteen against sixteen | C8 |
| S3 | P14:892 | sixteen in all; `diag(1,1,1,−3)` traceless; `Q` and `Y` returned | C1, C7 |
| S4 | P14:894 | `O(4)` reflection exchanges self-dual and anti-self-dual; the determinant's phase is zero; `γ¹γ²γ³` and its composite with `γ⁵` | C12, C13, C10 |
| S5 | P14:896 | `f(−r;M) = f(r;−M)` and the difference `4M/r`; the characters under `P` | C3, C5 |
| S6 | P14:898 | `2M/α = 2/(3√3)` is the largest value | C9 |
| S7 | P15:577–596 | `ℓ_D/√α` is the only combination; `1951.9 → 1497.04`; the signs and ratio of `r² − 1` | C6, C4 |
| S8 | P18:2802–2806 | the singlet contributes zero on every channel; the smallest closed content is four | C8, C14 |
| S9 | P18:3082 | `ν_R` carries `B − L` | C7 |

**Rows landed: all fourteen, at nine sites in three papers.** C7 and C8 each land twice (P14 and P18).

## The prediction

- **Size:** 9 new paragraphs, about 700–1,500 words of TeX (estimate 1,100, math included).
- **p(all nine land, three PDFs rebuild, gate GREEN on the first push) = 0.6.**
- **The expected stop is the pin gate** (`run_touched_readers.sh`) **at p 0.3**: a receipt quoting a span that a new
  paragraph sits next to may read the touched paper. Because no existing sentence is edited, a quote should not break.
  A local TeX build may also differ from the CI's `texlive-full` (p 0.1).

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
