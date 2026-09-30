# PRE-REGISTRATION — r7039+cc66.69 — `PO-70`

**Committed before any of `PO-70` was computed.** *Nothing below was run first and written after. Every number
quoted is carried in from `cc66.40`–`cc66.42`, from the instrument's own comments, or from `r7039`'s order.*

---

## ⛔⛔ THE FIRST THING IN THIS FILE IS A CORRECTION TO ITS OWN FIRST DRAFT, AND IT COST NOTHING BECAUSE NOTHING HAD RUN

*The first draft of this pre-registration proposed, as its central stage, the **clock swap on the injection** —
`SRCINJ=sweep` with `SRCINJRS` forced to one clock — and named `Jac_of` as the asymmetry, citing the
instrument's own comment at `r6919+cc66.42`.*

⛔ ***`cc66.42` ALREADY RAN THAT SWAP, AT `r6919`. The comment I cited is the comment that swap wrote.*** *Had I
gone from that draft to a script I would have re-derived a finished result and reported it as new. **The failure
was reading the instrument's comments and not the register the comments came from**, and the fix was to read
`FOR_66.md` before running rather than after.*

⇒ *The staging below is the one that remains after `r6919` is subtracted. **It is a different row, and it is
sharper, because `r6919`'s own numbers contain a tension it did not resolve.***

⌗ ***THE GENERAL FORM, AND IT IS THIS SEAT'S EIGHTH:*** **a pre-registration is finished work in the same sense
a receipt is, so it is written against the register and not against the code.** *An instrument's comment records
what a measurement found; it is not a statement that the measurement is still open.*

---

## ⛔ WHAT IS IN HAND AND IS NOT RE-DERIVED

1. **The object.** *This arm's projection retains $1.054$ times as much of its own source oscillation as the
   control's — $0.2543$ against $0.2413$ — rising $1.031$ below $q=3$ to $1.065$ above, **where the source ratio
   is flat** ($0.9922$, slope $-0.00106$). The floor is $0.6$ per cent.*
2. **The source is not where it is made.** *Source rungs $0.971$–$1.005$, the $\ell$ rung $1.042$–$1.052$.*
3. **Six mechanisms are excluded by direct substitution and are NOT re-run**: the $k$ sampling, the distance, the
   visibility width acting **before** the kernel, the lensing and binning, one source term alone, and the
   interference between two.
4. **`r6919`'s joint object, and it is the starting point rather than the question.**

   | arm | FWHM($\eta$) | $\Delta r_s$ across it (own clock) | $\Delta\chi$ across it | $\Delta r_s/\Delta\chi$ |
   |---|---|---|---|---|
   | control | $38.042$ | $17.3074$ | $38.042$ | $0.454950$ |
   | arm | $43.591$ | $17.2941$ | $43.591$ | $0.396733$ |

   *Term-independent, growing with wavenumber, vanishing for a window under one acoustic period.*
5. **`r6919`'s injections, which are the evidence this row starts from.**

   | injection | ratio | slope / unit $q$ | intercept |
   |---|---|---|---|
   | sweep, each arm's own clock | $1.0659$ | $+0.02260$ | $1.0085$ |
   | sweep at $\varphi=\pi/2$ | $1.0661$ | $+0.02250$ | $1.0090$ |
   | **fixed phase — no advance across the window at all** | $\mathbf{1.0587}$ | $\mathbf{+0.01189}$ | $1.0204$ |
   | **the real source (`cc66.41`)** | $\mathbf{1.054}$ | $\mathbf{+0.01167}$ | $1.0308$ |

6. **And two swaps are settled**: forcing one clock is **ill posed** (it moves $r_s(\eta_{\rm LS})$ and therefore
   the comb, so the regression reads a phase mismatch — $0.078$ overall, alternating in sign band by band), and
   the width swap **overshoots by eight** (ratio $1.0565$, slope $+0.09313$). *Neither is re-run.*
7. **`LEAFSCALES=1` is not in question** — the leaf assignment is what this arm's reported peak positions need.
8. **`PO-56` is struck.** *Nothing below re-derives it and no attribution question is asked.*

---

## ⛭⛭⛭ THE TENSION IN `r6919`'s OWN NUMBERS, WHICH IS WHAT `PO-70` IS ACTUALLY ABOUT

*Two facts from the table above do not sit together under the reading `r6919` offered, and neither was used to
draw a conclusion there:*

* ⚑ ***The sound horizon accumulated ACROSS THE WINDOW agrees between the arms to $0.08$ per cent*** ($17.3074$
  against $17.2941$). *So if retention were set by how much acoustic phase the plasma sweeps across its own
  window, **the two arms would agree** and there would be no excess to explain.*
* ⚑ ***A FIXED-PHASE injection — a standing oscillation, no advance across the window, no rate at all — already
  carries $1.0587$ of the $1.0659$***, *and its $q$-slope $+0.01189$ **reproduces the real source's $+0.01167$ to
  two per cent** where the sweeping injection's $+0.02260$ is nearly double it.*

⇒ *** SO THE PHASE SWEEP IS NOT THE DRIVER, AND THE QUANTITY THAT DIFFERS BETWEEN THE ARMS IS THE $\chi$-EXTENT
OF THE SOURCE'S SUPPORT — $38.042$ AGAINST $43.591$, $14.6$ PER CENT — WHICH IS WHAT THE KERNEL READS. ***

⌗ *`r6919` said this in one clause — "a **standing** oscillation already carries most of it, so it is not only
the source's phase sweep; the kernel's own window does part of it" — and then did not follow it. **`PO-70`'s
claim is that it does essentially all of it, and a claim of that shape is a law or it is nothing.***

### THE MECHANISM, NAMED, AND IT IS A STATEMENT ABOUT THE INTEGRAL AND NOT ABOUT THE PLASMA

*For a standing oscillation the integral factorises exactly:*

$$\Delta_\ell(k)=\cos(k r_s^{*}+\varphi)\;G_\ell(k),\qquad
G_\ell(k)=\int v(\chi)\, j_\ell(k\chi)\, d\chi$$

*so the comb is carried untouched into $\Delta_\ell$ and **the only thing that can damp it is the sum over $k$ at
fixed $\ell$**, whose weight is $P(k)G_\ell(k)^2$. ⇒ **Retention is the comb averaged over the kernel's own
$k$-acceptance**, and the acceptance's width in $k$ is set inversely by the $\chi$-extent of $v$.*

> ⛭⛭ **`M1` — THE ACCEPTANCE LAW.** *Retention is a function of the single dimensionless number*
> $$\Sigma \;=\; r_s^{*}\;\delta k_\ell , \qquad \delta k_\ell \;=\; \text{the } k\text{-width of } P G_\ell^2$$
> *— the acoustic phase spanned by the kernel's $k$-acceptance. The arm's window is $14.6\%$ wider in $\chi$
> while accumulating the same sound horizon, so its acceptance is narrower in $k$ and it averages the comb over
> less of an acoustic period.*

⇒ **That is `M1` and it is falsifiable three ways at once**: *it must reproduce the fixed-phase injection's ratio
**and** its $q$-slope; it must say why the sweeping injection over-delivers by exactly the amount it does; and it
must predict the **absolute** retentions $0.2543$ and $0.2413$, not only their ratio.*

---

## ⛭⛭ AND THE ARTEFACT READING IS NOW SHARP RATHER THAN GENERIC

*If retention is set by the $\chi$-extent of the source's support, then it is an **artefact** exactly when that
extent is set by something which is not the physical visibility:*

| | `M2` — the artefact candidates, all on the integral | the test |
|---|---|---|
| **a** | the quadrature window `EE` itself — its end points, and the $75/25$ split at `e_hi` | move the end points and the split with the physics held |
| **b** | the $\eta$ resolution `NLOS=560` against the kernel's own oscillation | refine `NLOS` |
| **c** | the $k$ grid's extent, which sets what acceptance is available to be summed over | the $k$ end, **at fixed physics** — *not* `KCONT`, which is excluded |
| **d** | the switch `e_sw`, which freezes the damping envelope and so shapes $v$ | move it within its validated range |

⛔⛔ ***AND I AM NAMING THE FAILURE MODE THE ORDER NAMES, BECAUSE `M2` IS THE READING THAT RESCUES THE FIT.*** *If
the retention is an artefact the sector's numbers move and the comparison against the sky has not been made.* ⇒
***So `M2` is tested FIRST, on a criterion fixed here — the $0.6$ per cent floor — and if it fails that criterion
I do not return to it later with a different one.*** *Its null result is pre-registered in words: **"the integral
is converged and $1.054$ is not a quadrature artefact."***

⌗ *And the converse, which is what makes `M1` the **required** reading rather than merely a description: the
$\chi$-extent of the visibility and the sound horizon it accumulates are **both** this background's own, and the
leaf assignment that separates them is fixed independently by the arm's peak positions. **If `M1` holds, the
$5.4$ per cent is this cosmology's prediction.***

---

## ⛭ THE STAGING

| | stage | the gate |
|---|---|---|
| **ⓐ** | **`M2` FIRST**, all four candidates, retention recomputed each time. | *ratio moves **less** than $0.6\% \Rightarrow$ converged; **more** $\Rightarrow$ `M2` confirmed and the row's first outcome is reached* |
| **ⓑ** | **$G_\ell(k)$ AND ITS ACCEPTANCE, EXHIBITED.** $\delta k_\ell$ measured directly off $P G_\ell^2$ on both arms, and $\Sigma = r_s^{*}\delta k_\ell$ formed. | *the two arms' $\Sigma$ must differ in the direction and roughly the size the $14.6\%$ width difference implies, **with no retention number in the construction*** |
| **ⓒ** | **THE LAW, CALIBRATED ONCE AND THEN FORWARD ONLY.** $\rho(\Sigma)$ read off injections at **one** configuration, then used to predict, with no refitting: the fixed-phase ratio $1.0587$, its slope $+0.01189$, and the **absolute** retentions $0.2543$ / $0.2413$. | *a law that needs a new coefficient per configuration is not a mechanism, and is reported as not one* |
| **ⓓ** | **A CONFIGURATION IT WAS NOT FITTED ON.** `SRCINJVIS` at widths outside the calibration, and a $q$ window outside the one the slope was read in. | *forward prediction, stated before it is checked* |
| **ⓔ** | **WHY THE SWEEP OVER-DELIVERS.** The difference $1.0659 - 1.0587$ against what `M1` says a sweep adds. | *if `M1` cannot account for the gap it is incomplete, and is reported as incomplete rather than as confirmed* |

### ⚠ THE ARITHMETIC-IDENTITY GUARD, APPLIED BEFORE THE RUN

*`cc66.66` and `cc66.67` each cost a revision to the rule that a quantity which cannot fail is not a test. Two
places it could bite here:*

* *$\delta k_\ell$ read off a **fitted** width of the same curve whose comb-averaging is then computed from it is
  not two measurements — it is one, twice. ⇒ **$\delta k_\ell$ is measured as a second moment of $PG_\ell^2$,
  fixed before any retention is computed, and printed.***
* *a retention whose source rung is normalised to $1$ by construction is the $\ell$ rung under another name. ⇒
  **both rungs are printed for every configuration**, and any stage whose two rungs are related by an identity
  is reported as arithmetic and not as a measurement.*

⚠ *And the floor: **nothing under $0.6$ per cent is reported as a difference**, in either direction, ⓐ's null
result included.*

---

## ⛭ THE PRE-REGISTERED WORDS, INCLUDING THE ONES THAT COST THIS SEAT MOST

* *If ⓐ moves the ratio above the floor:* ***"`1.054` IS A QUADRATURE ARTEFACT. Twelve revisions of `PO-56` were
  scored against a number the integral was not converged enough to carry, and this seat ran the projection at
  `NLOS=560` for all of them without testing it."***
* *If ⓒ predicts the absolute retentions and the slope forward:* ***"the retention is required by this
  background: the kernel's $k$-acceptance is set by the $\chi$-extent of a window that accumulates the same
  sound horizon on both arms, so the $5.4$ per cent is this cosmology's prediction and the sky's rejection of it
  is a result about the construction."***
* *If ⓒ reproduces the ratio but not the absolute retentions, or needs a coefficient per configuration:*
  ***"`M1` is a description and not a mechanism. `r6919` named the joint object; this revision has added a
  parametrisation of it and nothing more, and the row is not delivered."***
* *If ⓔ leaves the sweep's excess unaccounted:* ***"`M1` is incomplete: a standing oscillation carries most of
  it and the rest is not named, so what is exhibited is a bound and not a mechanism."***
* *If ⓐ is converged and no candidate survives ⓒ:* ***"the stage is located, the mechanism is still not, and the
  acceptance law joins the other seven exclusions."***

⌗ ***THE SELF-CHECK 66 ASKED FOR IS ⓐ's ORDERING*** — *the artefact reading first, on a criterion fixed here.
And the correction at the head of this file is the second one: **the row has already cost itself a stage by
reading code instead of the register**, which is the opposite failure from looking for a rescuing bug and worth
recording as its own kind.*

---

## ⛔ THE GUARDS

*No corpus edits. No re-running the six excluded mechanisms, nor `r6919`'s clock swap, nor its width swap.
Nothing on `PO-56`. `cc66.61`'s floor and the band-1 results not re-derived. No new statistics for their own
sake. Where the question does not fix an aggregation or a basis, both are reported and neither is chosen.*

* ⚠ ***A TOTAL IS NOT A MATCH*** — *66's. Reproducing $1.054$ is not reproducing the $q$-dependence, and neither
  is reproducing the absolute retentions; a mechanism has to do all three.*
* ⚠ ***AN ARITHMETIC IDENTITY IS NOT A MEASUREMENT, AND THE TIME TO SAY SO IS BEFORE THE RUN.***
* ⚠ ***THE INSTRUMENT MUST MATCH THE QUESTION'S GRAIN*** — *`cc66.60`'s.*
* ⚠ ***A ROUNDED FIGURE IS NOT A BOUND*** — *`cc66.68`'s. Every number carries the digits it was measured to.*
* ⚠ ***AND A PRE-REGISTRATION IS WRITTEN AGAINST THE REGISTER, NOT AGAINST THE CODE*** — *new, this file's own,
  and the reason it has a correction at the top instead of a re-derivation in the middle.*
