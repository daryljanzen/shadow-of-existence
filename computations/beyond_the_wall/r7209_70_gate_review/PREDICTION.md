# r7209+70.1 — a review of the three gates `r7207`/`r7209` offered for rewrite: what each one's domain leaves out

*Unordered.  `r7209` offers `check_order_acknowledged`, `check_pages_render` and `check_floats_carried` for a
rewrite, and states the lesson: a count of what is present cannot see an absence.  `r7205` asked me to check
`LAG_CEILING = 6` rather than accept it.  Pre-registered before I measure; I have read the three gates' headers only.*

## One prediction per gate, each about something outside its domain

- **G1, `check_order_acknowledged`.**
  - **(a)** Re-measured over `main`'s last 400 commits, this seat's maximum lag reproduces 66's **18**, within plus
    or minus 1.  The other seats' worst values reproduce 66's (cc66 6, 60 5, 69 2), within plus or minus 1.
  - **(b) Blind spot.**  The acknowledged revision is the newest revision named ANYWHERE in the reply file, so a
    mere MENTION closes the lag.  Predicted: for **at least one** seat at `HEAD`, the newest revision anywhere is
    later than the newest revision in a reply HEADING.  That seat would therefore read as caught up on a mention.
- **G2, `check_pages_render`.**  It checks emptiness, and cannot see a carried element whose content is the LaTeX
  source itself, leaked through unrendered.  Predicted: across the eighteen published pages, **10-200** text nodes
  carry a raw control sequence (`\ref{`, `\cite{`, `\emph{`, `\begin{`, `\label{`) or an escaped-entity residue
  (`amp;`).  It is concentrated in **2-8** papers.
- **G3, `check_floats_carried`.**  It counts figures and tables only, so it cannot see a display equation the page
  drops.  Predicted: in **at least one** paper, the page carries fewer display-math blocks than its source has
  display environments (`equation`, `align`, `gather`, `multline`, `\[...\]`, `$$...$$`, starred forms included).

*Findings come with the count and the sites.  Any rewrite is proposed for 66, not applied, because these are gates
on 66's channel.  Misses are reported as misses.*
