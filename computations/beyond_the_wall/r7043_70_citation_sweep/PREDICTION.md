# r7043 → 70: does each cited receipt compute what its sentence says? PRE-REGISTRATION

*Node 70. This file is committed before the tracer's first verdict and before the receipt exists. The scoping
counts below were taken to size the job and are **declared**, not tabled as open.*

## The range, measured and declared

- **Markers:** 606 `\rcpt{}` markers across 17 non-appendix papers. `CR_synthesis` carries none.
- **Receipts:** they cite 500 distinct receipts, and **every marker resolves to a file**. Resolution is not in question; content is.
- **Heaviest papers:** `CR_cosmology` has 180 markers (139 distinct receipts) and `matter_sector` has 105 (87).

## The instrument

1. **The claim.** For each marker, the claim is the text between the previous `\rcpt` or sentence boundary, whichever
   comes later, and the marker. Comments are stripped, and the claim is capped at 600 characters.
2. **Its quantities.** These are the numbers the claim states. They include decimals, integers of two or more digits
   that are not section, equation or year references, and `\times10^{n}` forms. They are normalised out of LaTeX.
3. **What the cited receipt says.** This is **both its source and its output from a run**. Every one of the 500 cited
   receipts is run once, in its own directory with a 1500 s limit, and the output is kept.
   ⚑ Many receipts compute a number at run time, so the number appears only in the output. Matching on source alone
   would manufacture false "(iii)"s.
4. **The match.** A claim number with *d* decimals matches when any number the receipt prints or states rounds to it
   at *d* decimals. An integer matches exactly.

## Verdict per marker, in the three-way form

- **(i) The source computes it:** every number in the claim is found in the cited receipt.
- **(ii) The source does not, and a different receipt does:** at least one number is missing from the cited receipt
  and found in another. That receipt is **named**.
- **(iii) No receipt in the repository computes it:** at least one number is found nowhere.
- ⚑ **The tracer's (ii) and (iii) are CANDIDATES, and every candidate is read by hand before it is scored.** A number
  can be missing from a receipt while still being supported by it: a unit conversion, a ratio of two printed numbers,
  a rounded restatement, an input quoted from a paper. Each candidate is resolved into (i), (ii) or (iii) with the
  reason written down.
- **Qualitative markers**, where the claim states no number, cannot be checked by number. They are **counted and not
  verdicted by the tracer.** The ones under an abstract or conclusion are read by hand. The rest are a **stated limit**,
  not a silent pass.
- **A cited receipt that does not run to exit 0** is recorded as that. A number in its partial output is not counted as support.

## Order, and scope

Hand review goes in the order a mis-citation would cost most:
1. markers under an abstract or conclusion;
2. every tracer candidate, paper by paper, `CR_cosmology` first.

If the candidates are too many for one revision, the ones not reached are **named as not reached**.

## Outcome table, the outcome that costs another seat most tabled FIRST

| outcome | what it means |
|---|---|
| **a (iii) under an abstract or conclusion** | a headline number that nothing in the repository computes |
| **a (ii) under an abstract or conclusion** | a headline number cited to the wrong receipt |
| (ii) or (iii) in a body | routed, in paper order |
| no (ii) or (iii) after hand review | the citation layer is sound where it can be checked by number; the qualitative markers remain the limit |

## Gates, fixed now: the finding and not the symptom

- Every (ii) and (iii) is gated on **receipt content**: the number's absence from the cited receipt's source and
  output, and its presence in, or absence from, the rest.
- **The paper's wording is reported, never required.**
- A receipt's output is taken from **a run inside the receipt itself** where it is cheap. Otherwise the gate checks
  the receipt's source for the lines that print the number.

## ⛔ NOT CLAIMED

- No verdict on whether any number is right. Only whether the cited receipt produces it.
- No prose edited: every hit is routed to 66.
- No physics, no re-scoring, no other seat's receipt touched.
