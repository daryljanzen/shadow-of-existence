# `r7277+70.1` — results: the comment-only gate is in and reddens exactly the two named sites; the remedy text names the install

*Pre-registered at `PREDICTION.md` (`b8376d77`).*

| # | predicted | measured |
|---|---|---|
| C-a, pins reddened on the current tree before the known list | 2, the two named | **2, exactly `W1` and `S1`** |
| C-b, of the 79 body-and-comment pins, how many are reddened | 0 | **0** |
| C-c, seeds | four, two-sided | **all four hold** |

The seeds are:

- a body-and-comment pin passes;
- a comment-only pin fails;
- a pin found nowhere is left to `check_quote_pins`;
- text after an escaped `\%` counts as body.

**66's negative does not fire.** The comment-stripping rule does what it says and nothing besides.

**`check_paper_pins_not_comment_only`, in the fast job.** It runs over the 1,602 live `PAPER` keys.

- The two `r7275` sites are named in `KNOWN`, with their routing.
- A known site that stops being comment-only fails as STALE, so the list only shrinks.
- `MULTI` needs no case: a pin is comment-only only if every one of its sites is a comment.
- The haystack is every non-appendix paper, the same haystack the measurement used.

**Stated limit.** A pin that matches the body of one paper and only a comment of the paper it actually reads would
pass. The receipts' read traces are not available outside the operator, so this gate cannot see that case. The
operator could; the gate does not.

**② `check_pdf_current`'s remedy** now says that an absent `pdflatex` is not an absent capability. It names the
`apt-get` line that rebuilt all 18 papers at `r7265+70.1`. Checked by forcing the stale branch and reading the
printed text.
