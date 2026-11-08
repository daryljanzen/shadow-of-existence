# `r7705+cc66` ITEM 2 — THE SCOPE SENTENCE, BACK TO BOTH BUILDS, WITH EACH FIGURE'S LICENCE

The site is `corpus/CR_cosmology.tex` l.2836–2843, inside `\S`\ref{sec:scope}. **One sentence changes and
one clause inside the sentence before it.** Nothing else at the site moves.

⛭ **NO PROSE-READING RECEIPT IS PINNED TO THIS SENTENCE'S WORDING, and that is established by enumeration
rather than by a spot-check.** Every assertion either receipt makes against `corpus/CR_cosmology.tex` was
listed and each literal located by line:

| receipt | assertions against this file | where each literal sits |
|---|---|---|
| `P15_the_low_ell_minimum_is_at_ell_four` | 5 (`in _TEXn` / `not in _TEXn`) + 2 regexes | l.`2603`, l.`2619`, the quadruple and the likelihood total |
| `P15_the_low_multipole_depth_gap…` | 1 regex, the `expectation at $\ell=2,3,4,5$` quadruple | `sec:largescale` |

⇒ **All of them lie outside l.2836–2843.** The nearest is l.2619's *"the hierarchy agrees to `$2.9$` per
cent at every multipole"*, which is in `sec:largescale` and not in the scope sentence, so the draft's own
re-use of `2.9` per cent neither satisfies nor breaks it. **Nothing needs patching in the same commit.**
What the landing does need is below, under BOOKKEEPING.

---

## ⓵ THE CONVERGENCE CLAUSE (l.2836) — two changes, one of them a correction

**In print:**

> …and the hierarchy's depths, **swept on the control's background**, **do not move** under a doubled opacity
> grid, a halved late step count, or a further-extended continuum.

**Draft:**

> …and the hierarchy's depths, **swept on the arm of record's own background**, **move by under four tenths
> of a per cent** under a doubled opacity grid, a halved late step count, or a further-extended continuum.

**⛔ The second change is a correction, not a polish.** The further-extended continuum *does* move the
decoupled build — by `0.360` per cent, which is 70's own routed bound of `0.36` per cent and twelve times
the bank's resolution. "Do not move" is true of two of the three knobs and false of the third.

| figure | licence |
|---|---|
| "on the arm of record's own background" | ✔ **PINNED.** The convergence bank's rows are `distances__armB_decoupled__L__*` — the distances point under `(L)`, `SPLITCLOCK = L`, `STACKPERT` unset, asserted from the bank's own `config`. |
| "under four tenths of a per cent" | ✔ **PINNED** as a bound: `0.360` per cent (decoupled) and `0.366` (frozen) against the receipt's `< 0.0040`. |
| the three knobs named | ✔ each is a row of the bank, named in its own `numerics`. |

⚠ **What this clause does NOT license, and the paper does not claim:** that the three knobs are one class.
They are three different facts, and the receipt now says so — the halved step count leaves the decoupled
build under the bank's resolution while moving the frozen build **10.0 per cent** at `l = 4`; the extended
continuum moves both, resolvably and by under four tenths; the doubled opacity grid moves **neither** above
the bank's floor, so it distinguishes nothing and is a limit of the bank, not a convergence of one build.
*A sentence that read the doubled grid as evidence about the decoupled build specifically would be reading a
zero that both builds return.*

## ⓶ THE BUILD-OF-RECORD SENTENCE (l.2837–2841) — this is the one 69's order is about

**In print:**

> The hierarchy's depths are read with the photon and neutrino sectors \emph{decoupled} past recombination
> rather than frozen with their free-streaming towers retained, and it is that build which agrees with the
> exact transfer to $2.9$ per cent, so the depth rests on the decoupled build's agreement with the exact
> transfer; the shape---the minimum at $\ell=4$ and the recovery by $\ell=8$---is returned by both
> treatments.

**Draft:**

> \emph{Both treatments of the sectors past recombination return the depth.} Read with the photon and
> neutrino sectors \emph{decoupled} past recombination, the hierarchy agrees with the exact transfer to
> $2.9$ per cent; read with them \emph{frozen} and their free-streaming towers retained it agrees to $3.2$
> per cent once its late step count is converged, the two agreeing with each other to $1.9$ per cent, at the
> distance point and at the refit point alike. \emph{The frozen build's larger departure was its step count
> and not its treatment of the sectors}: at the count the earlier sweep ran it, its own $\ell=4$ depth sat
> $3.2$ per cent off the limit it converges to. So the depth, like the shape---the minimum at $\ell=4$ and
> the recovery by $\ell=8$---is returned by both.

| figure | licence |
|---|---|
| "$2.9$ per cent" | ✔ already in print and already pinned; unchanged by this revision. |
| "$3.2$ per cent once its late step count is converged" | ✔ **PINNED**: `3.17` per cent at `l = 4` at the distances point, `3.07` at the refit point, against `< 0.032`, with the minimum at `l = 4` and `l = 8` above `0.99` asserted on each row. |
| "$1.9$ per cent" | ✔ **PINNED**: `1.81` per cent at `l = 3` (distances), `1.75` (refit), against `< 0.019`. |
| "at the distance point and at the refit point alike" | ✔ **PINNED**: both points are rows of the converged bank and both are checked. |
| "its own $\ell=4$ depth sat $3.2$ per cent off the limit it converges to" | ✔ **PINNED**: `3.23` per cent, against `0.02 < x < 0.045`. ⛔ *This is the self-move — the banked `NS3` 900 row against its own `h^2` limit — and NOT a departure from arm A.* |
| ⛔ "was its step count and not its treatment of the sectors" | ⚠ **PARTLY LICENSED, AND THE LIMIT IS NAMED.** The receipt pins the self-move (`3.23` per cent) and the converged agreement (`3.17` per cent of arm A). The figure that would close the attribution — the UNCONVERGED row's departure from arm A, `6.2` per cent, 70's `r7695` figure — **is not computed by this receipt and is not in print.** So the clause is carried as a comparison of two pinned numbers (off its own limit by `3.2`, agreeing with arm A at `3.2` once converged) and not as a quoted `6.2`. **If 69 wants the attribution stated with its size, that figure has to be pinned first, and I have not pinned it.** The wording above deliberately avoids printing it. |

## ⓷ THE SENTENCE AFTER (l.2843) NEEDS NO CHANGE

> \emph{So the shape and the depth both cross-validate} --- minimum at $\ell=4$, recovery by $\ell=8$ ---

It already says what the draft above now earns on both builds rather than one. ✔

---

## BOOKKEEPING THE LANDING MINTS — *the `r7697` fault, stated in advance this time*

At `r7697` a forward-looking assertion minted **two** bookkeeping entries — a quote-pin key **and** an
absent-paper pin — and I accounted for one. So, named here rather than discovered after:

1. **Two new PROSE figures** enter `CR_cosmology.tex`: `$3.2$` and `$1.9$` per cent. Neither is in
   `corpus/figure_pin_baseline.tsv` for this receipt today. Both are pinned by a COMPARISON in the block
   (`_FA[_p] < 0.032`, `_FD[_p] < 0.019`), not by a regex over digits, so `check_figures_pinned` has what it
   asks for — but **the rows have to be added in the pass that lands the prose.**
2. **"four tenths of a per cent"** is a new worded figure at the same site, pinned by `< 0.0040`.
3. **No quote-pin key is minted by this draft** — the sentence is prose, not a quoted source line, and the
   two existing `quote_pin_baseline` rows for this receipt are `SOURCE` sentences untouched by the block.
4. **No absent-paper pin is minted**, because nothing in the draft is forward-looking: every figure in it is
   computed by the receipt it cites, today.
