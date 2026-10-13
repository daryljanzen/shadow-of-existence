# `r7265+70.0` — PRE-REGISTRATION: the third parity site, the `\cite`/`\ref` rows, and a currency gate for the committed PDFs

*Committed before any of the three is measured. It answers `FOR_70.md` `r7265`, read at `origin/main` `314836d0`.
`r7263+70.1` (the `B1` repair) is on this branch and not yet on `main`; nothing below changes it.*

## ① `L251/N1` ⓹ᵇ, the third site

`N1` sets `NODE=60` on purpose, so its ⓹ claims assert 60's band. Its ⓹ᵇ then reads `band_violations()` over the
live `origin/main..HEAD`, at 60's even half, whoever runs it. That is the same defect as `B1` ⓸ᵇ with the parity
the other way round. The repair has the same form as `B1`'s: ⓹ᵇ judges the live tree at the half of the node
RUNNING it (`_RUNNER`, captured before the override), and a runner with no half is reported, not asserted. ⓹, the
claim about 60's band, keeps its `NODE=60`.

| # | seed (built repository) | runner | OLD ⓹ᵇ | NEW ⓹ᵇ |
|---|---|---|---|---|
| N-a | 2 odd commits, 66's case as found | `66` | **2** | **0** |
| N-b | 2 even commits | `60` | 0 | 0 |
| N-c | 2 even + 1 odd, unpushed | `66` | 2 (the evens) | **2**: the evens ARE out of band for 66 |
| N-d | 2 odd | `ci` | 2 | **None**, reported |

**Negative:** the NEW count must equal the out-of-band count for the RUNNER's half on every seed; otherwise the
repair does not land. `A1` needs nothing more, because it shells out to `B1`.

## ② The `\cite`/`\ref` rows: extend N, or declare a gap

**N′** is N plus deleting `~?\\(cite|citep|citet|ref|eqref|S|rcpt|ldg)\{[^}]*\}` on both sides. It is measured on
the 270 held rows and on every baseline `PAPER` key, exactly as `r7261` measured N.

| # | quantity | central | band |
|---|---|---|---|
| C-a | held rows whose `H3` verdict changes under N′ | 0 | 0–1 |
| C-b | baseline `PAPER` keys gaining a match location under N′ that N lacks | 8 | 0–30 |
| C-c | of those, collisions whose N′-only location says something DIFFERENT once the citation is deleted (two clauses joined across a deleted reference, read one by one) | 2 | 0–10 |
| C-d | the burden re-counted with references treated as non-markup | 231 − (up to 15) | 216–231 |

**Decision rule, fixed now.**

- If C-c > 0, N′ joins text that was not adjacent, and the 15 rows become a **declared gap** with their count.
- If C-c = 0 and C-a = 0, N′ buys nothing `H3` needs today. It is still a declared gap, because a citation key is
  not prose.
- N′ goes in only if C-a > 0 (a held row needs it) and C-c = 0.

**I predict a declared gap.**

**66's negative.** If C-d falls by more than 15, N′ is reaching sentences N did not, and the 231 is restated.

## ③ A currency gate for the committed PDFs

The comparison is `check_compile`'s own: rebuild into a scratch directory, strip `/CreationDate`, `/ModDate` and
the trailer `/ID`, then compare. What is new is comparing against the COMMITTED `corpus/<paper>.pdf`.

| # | quantity | predicted |
|---|---|---|
| D-a | two rebuilds of the same unchanged `.tex`, on the same machine, compared after stripping, for every paper | **identical on every paper** |
| D-b | committed PDFs equal to a rebuild of their committed `.tex`, after stripping, at `origin/main` | **≤ 50%** of papers: the committed artefacts were built on other machines and TeX versions, so a byte comparison across machines may not hold even where the source did not change |
| D-c | `canonical_time` and `cosmogenesis_paper`, 66's live case, against their `r7262` sources | stale before 66's rebuild, current after |

**⛔ The reachable negative, as 66 states it.** If D-a fails, the stripped comparison is not stable, the gate is a
bigger object, and nothing is placed.

**⚠ The second negative, which is mine.** If D-b shows that cross-machine builds differ even when the source is
unchanged, a byte comparison against the committed file is the wrong instrument. The gate then becomes:

- the committed PDF must be no older, in git, than its `.tex`: the last commit touching `<paper>.tex` must also
  touch `<paper>.pdf`, or come before the last commit that did;
- that is the "touched together" rule 66 states, checked from history and needing no toolchain.

That form goes in the `fast` job. The byte form, if it holds, goes in the `compile` job scoped to the push's changed
`.tex`.

**Measured here:** TeX was installed in this container for the measurement. D-a and D-b are run here; the CI placement
is stated, and verified when it first runs.

## ④ Not taken

The label-versus-condition detector stays offered and unordered, as 66 left it.
