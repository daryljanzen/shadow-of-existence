# `r7649+cc66` — PREDICTION, registered before the computation

*Registered in its own commit and pushed before a line of the measurement exists. The standing rule
is REGISTER BEFORE COMPUTING; a prediction written after the number is read is not a prediction, and
where something below was already measured when this file was written it says so in those words.*

Order: `r7649` (69) names eleven P15 sites that still print the `LEAFREC=0` namesake arm's figures,
and asks for one table — old → new, the receipt re-pointed, and the claim's fate — plus the landed
values pinned and `which_key_gaps` repaired. `which_key_gaps` is done (`cc66.78`, this branch) and is
not a prediction-bearing item: it is a reader whose pin the world moved under.

---

## ⓿ THE ONE STRUCTURAL PREDICTION, WHICH IS THE ONE THAT CAN EMBARRASS ME

**No phase or position claim in the eleven moves materially; every material move is in a contrast,
a residual size or a χ².**

That is not a safe hedge, it is the landing's own structure turned into a falsifiable statement. The
nofit caption already says it in words — *positions and spacing agree while the extrema are
overshot* — and the quartet 69 landed this turn says it in figures: a common displacement of six
tenths of a multipole across four peaks. If re-pointing the phase-intercept pair (site 1), the
driving pair (site 7) or the spacing/drift pair (site 9) moves a phase by more than the window the
paper already prints for it, this prediction is wrong and I say so in the table rather than
restating the prediction to fit.

**Falsifier, stated as a number:** any phase or position quantity in sites 1, 7 or 9 moving by more
than its own printed uncertainty, or by more than one per cent where none is printed.

---

## ⓵ PER SITE: WHAT I EXPECT, AND WHAT WOULD MAKE ME WRONG

The common ground for the directional calls: on the arm of record the lensed no-fit excess fell from
2.57 to 2.35 per bin and the refit from 1.57 to 1.60 — so **the arm's own distance from the data is
SMALLER than the namesake's on the no-fit comparison** and essentially level on the refit. Anything
that measures *how unlike the control this arm's residual is* should therefore shrink, and anything
that measures *how much of the residual the two arms share* should grow. Where I have no such ground
I write NO PREDICTION rather than a direction I cannot defend.

| # | site | what the paper prints | prediction | falsifier |
|---|------|----------------------|------------|-----------|
| 1 | phase intercepts, l.1028–1029 | $-0.2278$, $-0.2445$ | both move by **less than 0.01**, and both stay inside the sky's own windows ($-0.2378\pm0.0099$, $-0.2448\pm0.0074$). The claim *the arm sits inside the locator's own window-to-window spread* SURVIVES | either intercept moving by more than 0.01, or leaving its window |
| 1b | l.1039, the envelope's fourth-peak move | "a seventh of a multipole against an offset of two" | the move stays **under a quarter of a multipole** and the offset stays near two; the clause survives in form, possibly with the fraction restated | the move exceeding a quarter of a multipole, or the offset moving off two |
| 2 | shared fraction, l.1092–1100 | cosine $0.855$; $73\%$ shared; $105$ in χ² with $77$ from the model difference; factor $1.3$ | cosine **rises**; shared fraction **rises above 73%**; the $105$ **falls**; the $1.3$ **falls toward 1.2**. The model difference's SHARE of the total stays within a few points of 73% | the cosine falling, or the shared fraction falling, or the total rising |
| 3 | model difference, l.1109 | $5.7\%$ | stays **under ten per cent**; *what does is a contrast difference* survives | exceeding ten per cent |
| 4 | composition, l.1227–1228 | "a little over one and a half times … within one per cent" | the **within-one-per-cent part holds** (it is a property of the composition rule, not of the arm's size); the "over one and a half times" may move and I predict no direction for it | the composition agreeing only to worse than one per cent |
| 5 | window channel, l.1190 | "about a third" | **survives verbatim** — the two readings are a quarter-to-a-half and a fifth-to-two-fifths, wide enough to absorb a move of a few per cent | either range moving off "about a third" |
| 6 | three-grid truncation, l.1962 | $-1.0 \ldots +93.8$ | the **monotone rise survives** and the top end **stays above $+80$** | the monotonicity breaking, or the top end falling below $+80$ |
| 7 | `arms_own_driving_pair`, l.2183 | $+0.1259$ against $+0.1265$ | still agrees to **better than one per cent** — this is the reproduction claim, and it is a phase, so ⓿ applies | the two parting by more than one per cent |
| 8 | P18 l.1558 | "$58$ times" | **falls**, and stays **above 30**; the claim *what is not configuration-limited is the ratio* survives with a new figure | the ratio rising, or falling below 30 |
| 9 | spacing period and drift, l.2120/2142 | $312$, $-96.6^{\circ}$ | **ALREADY MEASURED, NOT A PREDICTION.** $309.25$ and $-78.3$ were measured at `r7647` and 69 quotes them back in `r7649`. What is open is only the wording and the receipt's re-point | — |
| 10 | nofit caption, l.1070 | $(68.62,0.2974)$ at $0.958$ | **ALREADY MEASURED BEFORE THIS FILE WAS WRITTEN, AND IT IS NOT A PREDICTION.** See ⓶ | — |
| 11 | INDEX row C71 | "namesake arm's" note | editorial; no figure. The note is either still true of a receipt that still reads the namesake or stale, and which it is follows from the other ten | — |

---

## ⓶ SITE 10 IS ANSWERED ALREADY, AND I SAY SO RATHER THAN DRESSING IT AS A PREDICTION

69 asks whether $(68.62,0.2974)$ is the BAO-alone fit's own minimum — a distinct thing correctly
printed — or a namesake leftover. **I read the answer off an existing gate's own printed output
while surveying the eleven, before writing this file.** So it is recorded here as a measurement
already in hand, not as something I am about to predict:

`…the_1p57_has_no_parameter_address…` prints, from the 13 DESI DR2 points with **no spectrum
involved at all**:

```
arm ruler (D free, r_s leaf):  H0 = 68.6169  Om = 0.29735  chi^2 = 10.539 (0.958 per dof)
```

Rounded, $(68.62,\,0.2974)$ at $0.958$. **It is the BAO-alone fit's own minimum, correctly printed.**
The likelihood is a pure background fit — distances on the arm's radiation-free rate, $r_s$ on the
leaf clock — so `LEAFREC` does not enter it and there is no namesake/arm-of-record distinction for
this number to leak. The pair the spectra are *computed* on is the rounded $(68.60,\,0.2973)$ start,
which is a different (and also correct) thing; whether the caption should name the computation point
rather than the fit's minimum is a wording question, not a residue.

What remains genuinely open at site 10, and is therefore still a prediction: **the $179$-bin figures
in the same caption are the ones to check, not the background pair.** I predict they are already the
arm of record's, because 69 landed $2.35$ and $1.60$ into that caption this turn.

---

## ⓷ THE REST OF THE ORDER, WHICH CARRIES NO PREDICTION AND IS SAID SO

- **Pinning the landed values** (2.35, 2.71, 502.1, 1.60, 1.61, 2.33, 186.135, 11.7, 18.3, 1.015) in
  the receipts that compute them, and lowering `figure_pin_baseline.tsv` from 1484. This is
  instrument work on numbers already measured and landed. No prediction.
- **69's quartet wording.** A check of arithmetic and of whether a capitalised verdict in my own
  locator receipt is read by the paper. No prediction, and if my own receipt's
  `NEAR-CONSTANT ONE-MULTIPOLE` is read anywhere, restating it to the $+0.62$ it prints is a
  correction of mine, not of 69's.

## ⓸ COMMITMENTS FOR THIS TURN

1. Every moved pin is **perturbed**, and the perturbation must **FAIL GATES** rather than crash or
   change nothing. A defaulted switch is perturbed by SETTING THE OPPOSITE VALUE, never by unsetting
   the key — `LEAFREC` defaults to `1`.
2. The pre-push set is run in full, including `scripts/run_touched_readers.sh --both HEAD~N` in its
   RANGED form (it is vacuous on a committed tree) and `corpus/check_quote_pins.py` directly, both
   being documented holes in `scripts/turn_gates.sh`.
3. Any pin on a sentence of 69's is checked for **failure on success**: if the pin would go red the
   day 69 lands the passage correctly, it is written as a disjunction and adjudicated `ALT`.
4. Paren balance is checked on every rewritten multi-line condition, and `ast.parse` fails the patch
   closed before anything is written.
5. Figures I compute are **recomputed**, not read off a rounded print, and where a quantity has two
   printed roundings I do not take the flattering one.
