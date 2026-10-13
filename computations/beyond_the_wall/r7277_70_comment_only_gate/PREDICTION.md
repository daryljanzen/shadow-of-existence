# `r7277+70.0` — PRE-REGISTRATION: the comment-only gate, and one line of remedy text

*Committed before the gate is written. It answers `FOR_70.md` `r7277`, read at `origin/main` `6b0d5330`.*

## ① `check_paper_pins_not_comment_only`

**The condition, as 66 ordered it.** A live `PAPER` quote-pin key whose literal matches ONLY inside LaTeX comments
goes red. The haystack is the same as `r7275+70.2`'s G-b:

- every non-appendix `corpus/*.tex`;
- a comment runs from an unescaped `%` to the end of its line;
- a literal carrying a backslash is matched as a regex when it compiles, as the receipts match it.

**Known sites.** The two `r7275` sites (`W1` `"until r2376+c54.179"`, `S1` `"THE RECEIPT WAS MORE HONEST THAN THE
PAPER"`) are named, with their routing, and allowed while they stand. A named site that stops being comment-only is
STALE and fails, so the list can only shrink.

| # | quantity | predicted |
|---|---|---|
| C-a | currently-green `PAPER` pins the gate would redden on the tree as it stands, before the known list applies | **2**, exactly the two named |
| C-b | of the 79 that also match a comment, how many the gate reddens | **0**: each also matches the body |
| C-c | seeds | a body-plus-comment pin passes; a comment-only pin fails; a pin found nowhere is not this gate's (`check_quote_pins` already counts it) |

**⛔ Negative, as 66 sets it.** If C-a is not 2, the comment-stripping rule is doing something besides what it says.
That is reported before the gate lands, with the extra sites read.

**Placement.** The fast job, as the measurement costs seconds. **`MULTI` pins:** no special case. A `MULTI` pin has
more than one body site, so it can be comment-only only if all its sites are comments, which the same condition
catches.

## ② `check_pdf_current`'s remedy text

One line: when `pdflatex` is absent, install TeX first. A seat read the absent toolchain as an absent capability.
The line names the packages that were enough to rebuild all 18 papers at `r7265+70.1`.
