# r7037 → 70: the ten passages were one paper. Doing the corpus: PRE-REGISTRATION

*Node 70. This file is committed before the receipt exists.* ⚑ **Unlike earlier pre-registrations, the sweep's scoping
had to read the hits in order to scope them.** So this file does not table open outcomes for facts already seen. It
declares them. What it fixes before the receipt is written is the **instrument**, the **verdict rules**, the **gates**,
and what is claimed.

## The sweep's range, measured during scoping and declared

- **Scope:** every `corpus/*.tex` that is not a generated `appendix_*`, which is 18 papers.
  - Comments are stripped, including an unescaped `%` mid-line.
  - The bibliography is dropped.
- **The first pattern was dominated by the symbol σ.** A bare `\sigma` counted 106 times in `groupoid_paper` alone, all of them
  the root-exchange involution. `\bsigma` also matches `\sigma`, because the backslash is a word boundary.
  - The statistical shapes are therefore fixed as: a number followed by `\sigma` inside math, `several-\sigma`, `standard deviation(s)`, the
    bare word `sigma(s)` not preceded by a backslash, a numeric `\pm`, `nois(e|y)`, `significan(t|ce)`,
    `detect(ed|ion|able)`, `tension`, `uncertaint…`, `\chi^2`, `confidence`, `p-value`, `(told|distinguish…|differ…) from
    zero`, `consistent with (zero|the data)`, `scatter(s)`, and `cosmic variance`.
  - For shares, the shapes are: `share`, `a quarter`, `a fiftieth`, `decidable`, and `accounts for`.
- **Outside `CR_cosmology.tex` this leaves about 96 hits in 13 papers.** Most of them are ordinary English ("tension",
  "detected", "significant"), a coordinate (`\chi` in a line element), numerical precision, or quantum uncertainty.
  These are **excluded, each with its reason named**, not scored.

## The instrument

A claim's noise basis is found **in the source receipt that computes it**, not in the prose around it.

- **Attribution.** Where the paper carries `\rcpt{}`, the nearest marker after the claim is the source. Summary
  passages put every marker in one block at the end, so there **the source is mapped by content**. Where the paper cites a
  companion (`CR_framework` and `CR_synthesis` carry few or no `\rcpt`), the companion's receipt is the source.
- **Evidence classes.** Each is a pattern in the source's own code.
  - `COV`: a covariance is read or solved against.
  - `DRAW`: noise realisations are drawn.
  - `MEAS`: published measurement errors are combined in quadrature with a propagated theory error.
  - `CV`: the exact cosmic-variance likelihood, a scaled χ²₂ℓ₊₁.
  - `EXT`: a published external measurement is quoted with its own errors.
- ⚑ **The r7033 `drawless` test is necessary but not sufficient here.** A source that draws nothing and reads no covariance
  can still carry a real noise model through `MEAS` or `CV`, and the nucleosynthesis confrontation does exactly that.

## Verdict per hit, in the three-way form

- **(i)** A real noise model: the source carries at least one evidence class that bears on **that** claim. The claim stands.
- **(ii)** A spread of computed quantities, analysis choices, or disjoint stretches of noiseless spectra, worded as a
  significance. The wording overclaims, and the honest form is named.
- **(iii)** Cannot be determined from the repository. The σ is plausibly real, but no receipt computes it, or it is an assumed input. This
  is an honest blank and a finding.

## Scope, stated because the order allows it

- **All 17 papers other than `CR_cosmology.tex` are swept in full.** That gives 18 in all with `CR_cosmology.tex`.
- **`CR_cosmology.tex` is RE-swept in full.** Its r7033 enumeration is not taken as exhaustive, because scoping found one
  phrase that was in the paper at the r7033 audit base (`78957ff9`) and is not in the r7033 receipt. I report that
  correction to my own finished work here, unprompted.
- **The r7033 ten** were corrected at r7035. They are checked for the honest form, not re-flagged.

## Outcome table, the outcome that costs another seat most tabled FIRST

| outcome | what it means |
|---|---|
| **a class (ii) under an abstract or conclusion claim** | a headline overclaims; routed to 66 first |
| class (ii) in a body, frontier or discussion section | the wording overclaims below the headline; routed, in paper order |
| class (iii) | an honest blank: the σ is plausibly real but the repository cannot reproduce it |
| no class (ii) outside `P15` | the defect class was local to the one paper that had been audited, and that is a finding in its own right |

## Gates, fixed now: the finding and not the symptom

- **Every gate is on a source receipt's own content:** which evidence classes it carries, what its σ is computed from, or
  whether any receipt computes a quoted σ.
- **The paper's current wording is REPORTED beside each hit, never required.** A correction by 66 must not turn this
  receipt red. That is the r7035 rule, taken here.
- **Counts are gated from the recorded table:** class (ii) per paper, and class (ii) in abstracts and conclusions.

## ⛔ NOT CLAIMED

- No verdict on whether any result is correct, and no re-scoring.
- No paper prose edited. **The enumeration is the deliverable and every hit is routed.**
- No physics, channel or mechanism.
- No `cc66` or other seat's receipt touched.
