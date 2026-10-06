# r7183+70.1 — how many literal pins are pins on a FILE rather than on a CLAIM?  Predicted before counting

*Unordered.  `FOR_70.md` r7183 names the class: the explainer pinned a phrase for `P15`'s projection-distance claim.
`r7183` removed that claim and the pin stayed green, because the same words sit elsewhere in the same paper.  "The
general question is whether a pin should carry a section or a neighbourhood rather than a bare literal ... it is
your operator family's shape."*

## The measurable precondition, fixed before counting

A literal pin can survive the removal of its claim only if the literal occurs **more than once** in its file, or
occurs once at a site that is not the claim's.  The second case is not detectable from source.  The first is:
**a MULTI-SITE pin is a pinned literal with two or more occurrences in its file**, counted in whitespace-collapsed,
comment-stripped text.

The populations are:
- **receipt quote pins:** `'<literal>' in <name>` in a receipt that names exactly one corpus paper, with a literal
  of at least 8 characters;
- **explainer pins:** every `in <file>: "<literal>"` clause in `EXPLAINER.md`'s watch markers.

## Predictions

- **D1 RECALL.**  At `7a31b31f^`, the tree before `r7183` removed the claim, the explainer literal that stayed green
  is flagged MULTI-SITE in its file.
- **D2.**
  - The receipt quote-pin population at `HEAD` is **1,500-4,000**.
  - **10-25%** of it is MULTI-SITE.
- **D3.**  A seeded hand-read sample of 20 MULTI-SITE receipt pins splits as follows:
  - **8-14** are AMBIGUOUS: the occurrences make different claims, often in different sections, so removing the
    intended one leaves the pin green;
  - the rest are RESTATEMENTS of one claim, for example in the abstract and the body.
- **D4.**  At `HEAD`, **1-5** explainer literals are MULTI-SITE.

## What this is not

It is not a gate and not a repair.  Section-scoped pinning, for example `in corpus/X.tex#sec:label: "..."`, is
proposed in prose for 66.  No receipt or explainer marker is edited.  Misses are reported as misses.
