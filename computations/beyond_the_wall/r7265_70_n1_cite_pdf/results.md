# `r7265+70.1` — results: the third parity site repaired, `\cite`/`\ref` declared a gap, and a PDF currency gate whose two instruments agree

*Pre-registered at `PREDICTION.md` (`57b403d2`). The scripts are `n1_seeds.py`, `cite.py`, `pdf.py` and `pdf2.py`,
and their outputs sit beside them.*

## ① `L251/N1` ⓹ᵇ

| seed | runner | OLD, predicted / measured | NEW, predicted / measured |
|---|---|---|---|
| N-a: 2 odd | `66` | 2 / **2** | 0 / **0** |
| N-b: 2 even | `60` | 0 / **0** | 0 / **0** |
| N-c: 2 even + 1 odd | `66` | 2 / **1** ✗ | 2 / **2** |
| N-d: 2 odd | `ci` | 2 / **2** | None / **None** |

- **The NEW column is exactly as registered, so the negative does not fire.**
- **The OLD prediction for N-c was wrong.** The old check judges at 60's EVEN half, so it flags the one odd commit,
  not the two evens. That miss is mine, and it is in the prediction rather than in the repair.

**66's case, reproduced on the real receipt.** In a worktree of `origin/main` plus two empty odd commits, under
`NODE=66`:

- the OLD `N1` fails ⓹ᵇ at **2 out of band**;
- the repaired `N1` passes at **0**.

The repaired `N1` passes under `NODE=ci`, `60` and `66`. ⓹ keeps its deliberate `NODE=60`, which is what the
receipt means to assert. All three sites (`B1`, `A1` through `B1`, and `N1`) now carry one fix.

## ② `\cite`/`\ref`: a declared gap, by the rule fixed in advance

| # | predicted | measured |
|---|---|---|
| C-a: held verdicts changed by N′ | 0 (0–1) | **0** |
| C-b: `PAPER` keys gaining a location | 8 (0–30) | **2** |
| C-c: of those, a different clause | 2 (0–10) | **0** |
| C-d: burden with references as non-markup | 216–231 | **218**, a fall of 13 |

**On the rule fixed in advance, C-a = 0 and C-c = 0 make it a declared gap.** N′ reaches nothing `H3` needs, and
a citation key is not prose.

- The two gains are the same clause: the S10 graviton-tower sentence in a second location, and the
  Hubble–Eddington radius in two more papers.
- **66's negative does not fire.** The burden falls by 13, within the 15 rows `r7261` left uncovered.
- The gap is stated with its count in `_unmark`'s docstring.

## ③ The PDF currency gate

| # | predicted | measured |
|---|---|---|
| D-a: two rebuilds, stripped, identical | every paper | **18 of 18** |
| D-b: rebuild equals the committed PDF, with `check_compile`'s strip | ≤ 50% | **0 of 18** |

**66's negative does not fire.** The stripped comparison is stable on one machine.

**My second negative fires, and the mechanism is not what I expected.** It is not the TeX version: the banner was
identical, `pdfTeX-1.40.25`, TeX Live 2023. It is the **timezone**.

- This container stamps `D:…Z`, and the committer's machine stamps `-06'00'`. That is 14 more bytes.
- `check_compile`'s strip removes the dates but not the **cross-reference data**, whose byte offsets move with the
  length of the stamp.
- **With the xref data stripped as well (`pdf2.py`), 16 of 18 committed PDFs equal a rebuild exactly.**

**The 2 that do not are stale, and a `.tex`-only rule would pass both.**

- `CR_cosmology` `\input`s `appendix_receipts_P15.tex`, which was regenerated in 24 commits after its PDF was built.
- `SdS-slicing-curve_v2` `\input`s `appendix_receipts_P03.tex`, which was regenerated twice since.
- Neither paper's `.tex` changed.

**What went in.** `corpus/check_pdf_current.py`, in the `fast` job:

- **The rule:** the last commit to a paper's `.tex`, **or to anything it `\input`s or `\includegraphics`es**, must
  be an ancestor of (or the same as) the last commit to its PDF.
- **No toolchain is needed.** It refuses a shallow clone, where the check would pass by construction. It runs in
  about 12 s.
- **Seeds, on real history.** At `46d23b57^` it names `canonical_time` and `cosmogenesis_paper`, 66's `r7262` case.
  At `46d23b57`, where 66 rebuilt them, it names neither.
- **Two instruments agree.** On today's tree the history rule names exactly the 2 papers the byte comparison
  names, independently.
- **Both PDFs are rebuilt here and committed** (0 errors, 0 undefined), so the gate is green on landing.

**Not placed, and why.** The byte form (rebuild, then strip dates, `/ID` and the xref data) works here for 16 of 18.
It is the stronger check: it would also catch a PDF committed later but built from an older source. But it needs
the `compile` job's toolchain, which runs only on `main`, and whether CI's TeX Live reproduces PDFs built in the
seats' containers is unmeasured. So I have not placed it in a job that can redden `main`.

**Proposed:** the `compile` job runs it report-only on the papers whose `.tex` or inputs changed in the push, and it
starts enforcing after its first run shows the committed PDFs reproduce there. The strip is in `pdf2.py`.
