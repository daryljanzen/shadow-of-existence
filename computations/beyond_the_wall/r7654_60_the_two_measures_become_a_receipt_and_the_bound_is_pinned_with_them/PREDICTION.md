# `r7654` (60) — REGISTER BEFORE WRITING THE RECEIPT: the two measures `P18` now prints, pinned where a reader can run them

**The order (`r7653`, 69).** Branch ⓵ was taken and `P18` l.1557–1559 now prints **$1.77$** and
**$1.35$** ($288.04$ over $214.1$) and the "quarter apart". Those figures live in a computations
directory, not in a registered receipt. So: register one that computes $\chi^2_{\rm sep}$ and $F_2$ on
the arm of record's $185$ lensed bins against its control and **pins $1.77$ and $1.35$**; assert the
identity $F_2 = \chi^2_{\rm sep} - 2\delta^{\mathsf T} F r_c$ and the bound on the same rows; give its
INDEX row so `P18` can cite it. **And if `P18`'s sentence should say something the figures do not
support, say so.**

---

## ⓐ WHERE IT GOES, DECIDED AND NOT LEFT TO THE DIFF

The order offers `receipts/P18_*` **or** P15 "if the computation belongs to P15's likelihood". ⇒ **It
goes under P15**, as `receipts/P15_CR_cosmology/`, because:

- the instrument IS P15's likelihood — `plik_lite` TT, its own binning weights and covariance, the
  $185$ bins at $\ell$ $100$–$1996$, the arm-of-record spectrum and its control;
- there is no `receipts/P18_*` directory in the tree, and adding one is a new instrument, which this
  line does not do;
- **and `P18` itself already points there**: every figure in the surrounding paragraph, the $2.10$ and
  the unlensed $2.09$ included, is cited `\cite{JanzenCRcosmology}` — the cosmology paper. So a `P18`
  sentence citing a P15 receipt for these two figures is the paragraph's existing habit and not a new
  cross-reference.

⌗ *The `\rcpt{}` marker in `P18` is 69's to place; this revision supplies the receipt and the INDEX
row it needs, and says so rather than editing the paper.*

## ⓑ WHAT IT PINS, STATED BEFORE IT IS WRITTEN

A figure an INDEX row prints is pinned only by a **comparison inside the receipt** — a regex that
merely finds its digits is not a pin, and the pin must be **failable**. So each of the four pins below
is a parsed number compared against the paper's printed value, and the receipt carries a
**perturbation arm** that moves the computation and asserts the pin goes red.

| pinned | the paper's printed value |
|---|---|
| $\chi^2_{\rm sep}/\chi^2_c$ on the arm of record | **$1.77$** |
| $F_2/\chi^2_c$ on the arm of record | **$1.35$** |
| $F_2$ and $\chi^2_c$ as the sentence prints them | **$288.04$** over **$214.1$** |
| the two measures' separation, "a quarter apart" | **$23.87\%$**, which rounds to a quarter |

## THE ARMS

**① THE FOUR FIGURES REPRODUCE** from the banked spectra through this seat's own scorer, each to the
digits `P18` prints: $1.77$, $1.35$, $288.04$, $214.1$.

**② `COMPUTES:` IS DECLARED**, because this receipt pins parameters, and the receipt is red without it.

**③ THE IDENTITY IS CHECKED, NOT ASSERTED.** $F_2 = \chi^2_{\rm sep} - 2\delta^{\mathsf T} F r_c$ holds
to floating-point on **every** row the receipt produces — both arms, lensed and unlensed, $185$ and
$133$ bins — eight rows, not the one the paper needs.

**④ THE BOUND HOLDS ON THE SAME ROWS.**
$\lvert F_2/\chi^2_{\rm sep} - 1 \rvert \le 2/\sqrt{\chi^2_{\rm sep}/\chi^2_c}$ on all eight, and on
the `r4236` row read from its own printed numbers, where it is $0.0485 \le 0.2622$.

**⑤ EVERY PIN IS FAILABLE, AND THAT IS MEASURED AND NOT CLAIMED.** The receipt perturbs the arm-of-record
spectrum by $1\%$ and asserts that **each** of the four pins then falls outside its tolerance. *A guard
that cannot fail on the data it is given is not a guard, and this line has now been caught by that
twice.*

**⑥ THE TOLERANCE IS THE PRINTED DIGIT AND NOT A WINDOW CHOSEN TO PASS**: half a unit in the last
printed digit of each figure, stated per pin, with the measured residual printed beside it.

**⑦ AND THE ONE PLACE THE SENTENCE OVERREACHES, IF IT DOES.** The order asks. The sentence says both
measures put *"the arms further from each other than the control is from the data"*. On the arm of
record both ratios exceed $1$ ($1.77$ and $1.35$), so it holds **there** — but the registration records
in advance that it does **not** hold on every configuration this instrument can reach: on the $185$
unlensed rows `r7652` measured $0.67$ and $0.53$, and on the $133$ unlensed rows $0.94$ and $0.88$, all
below $1$. ⇒ **So the clause is true of the configuration the sentence names and false as a general
statement**, and the receipt prints both so a reader cannot take the stronger reading. *Arm ⑦ is
registered as the expected finding, not discovered afterwards.*

**⑧ THE INDEX ROW IS WELL FORMED** — exactly $9$ pipes and $8$ columns, no bare `|` inside a cell —
and the four regenerators run to no change beyond the appendix the new row adds.

---

## WHAT THIS DOES NOT DO

- **It does not edit `P18`.** The re-statement is already landed and is 69's; the `\rcpt{}` marker is
  69's too. No paper is edited here.
- **It adds no gate, ledger or census**, and no new receipt directory. One receipt and one INDEX row.
- **It does not re-open `r7652`'s findings** — the decomposition, the three misses and the bound are
  merged and are not re-argued; this revision only makes the two figures the paper now prints runnable
  by someone who did not write them.
- **The data is shared on purpose**, so this remains arithmetic on the likelihood's own bins and not a
  claim that those bins are the right confrontation.

⌗ **The reachable negative is that all four figures reproduce, every pin is failable, and the sentence
needs no correction.** Arm ⑦ is registered against the last of those three.
