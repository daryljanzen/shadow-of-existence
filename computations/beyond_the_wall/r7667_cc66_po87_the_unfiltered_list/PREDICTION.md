# `r7667` (cc66) — PO-87's DISCHARGE LIST, REGISTERED BEFORE IT IS BUILT

**The order (`r7667`, 69), item 1, verbatim in its operative part:** *"The complete, unfiltered
list, on a named tree. List every figure P15, P7, P18, P6 or the explainer prints that still rests
on a namesake spectrum (LEAFREC=0) or on an instrument state the arm of record superseded. Give each
its sentence, its receipt, and the spectrum the receipt reads. Include everything: the c54 family
pinned to its superseded state, the twelve namesakes today's instrument cannot rebuild, and any
sentence citing them. An item leaves the list only by being re-derived or by its sentence being
re-grounded."*

**Tree:** `5dac5ff9a` (`origin/main` at `r7667`), branch fast-forwarded to it.

## WHAT IS ALREADY MEASURED, AND IS THEREFORE NOT REGISTERED AS A PREDICTION

Stated so the arms below are honest rather than retrospective. Orientation already run on this tree:

- `receipts/INDEX.md` parses to **1145** rows; **419** carry paper tag `P15`, `P7`, `P6` or `P18`
  (`P18` appears 20 times in the file but on no row this parse keys to a receipt path — resolved below).
- Of those 419, **17** name a receipt path not on disk, **104** reference at least one `.npz`,
  **102** reference at least one spectrum WITHOUT `leafrec1` in its name, **39** reference at least
  one WITH it, **65** read only non-`leafrec1` spectra.
- Of the 102, **90** are cited somewhere in `corpus/*.tex` or `EXPLAINER.md`; **73** are cited in
  `corpus/CR_cosmology.tex` itself. ⛔ The gap matters and is the first thing the list must not
  blur: a citation in `appendix_receipts_P15.tex` or `appendix_receipts_corpus.tex` is the
  GENERATED registered-receipt list, not a sentence printing a figure.

## THE ARMS, REGISTERED

**① The body-sentence count.** Of the 73 candidates cited in `CR_cosmology.tex`, I register that
**between 55 and 73** have at least one body sentence that PRINTS a figure (a number in text or
math mode) in the same sentence as the `\rcpt`, and that the remainder cite the receipt without
printing any of its numbers. *A citation is not a figure; the order asks for figures.*

**② The naming convention is the classifier, and it is checked rather than assumed.** I register
that for every banked pair the arm-of-record file is the namesake's name plus `_leafrec1`, so that
`X_cr.npz` → `X_cr_leafrec1.npz`, and that **at least 30** of the namesake files a candidate reads
have no `_leafrec1` sibling in `computations/beyond_the_wall/spectra/` at all. *Those are the
expensive half: an item with a sibling may be re-derived by repointing, and one without needs the
spectrum built first.*

**③ The twelve are all still load-bearing.** `r7640+60`'s arm ③ names twelve namesakes today's
instrument aborts on under their own `KFAC=1`: `c54.175`, `c54.177`, `c54.178`, `c54.186_KCONT`,
`c54.186_L3000`, `c54.191_lA340`, `c54.191_phipi`, `c54.193_nodrive`, `c54.195_phi0.7854`,
`c54.195_phi1.5708`, `item38_phi0.0`, `item38_phi3.1416`. I register that **at least eight** of the
twelve are read by at least one receipt cited in `CR_cosmology.tex`, so they are not a closed
historical set but a live dependency of the paper's own sentences.

**④ The explainer.** I register that `EXPLAINER.md` cites **zero** of the 102 candidates directly,
and that whatever it carries of this material arrives through `THE_REGISTER.md` rows rather than
through a `\rcpt`. *If that is wrong the list gains an explainer section; the arm is stated so the
answer is readable either way.*

## WHAT THIS DOES NOT SETTLE

The list is an enumeration, not a verdict on any figure. **Whether a figure MOVES when re-derived is
item 2's question and is not predicted here**, and nothing in this directory re-derives anything.
⚠ And `LEAFREC=0` is not by itself a defect: a sentence may be legitimately about the namesake
configuration. The list records what rests on what; re-grounding a sentence is as good as
re-deriving its figure, and the order says so.

Registered before a line of the list exists.
