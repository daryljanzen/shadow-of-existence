# PRE-REGISTRATION — r7039+cc66.69 — `PO-70`

**Committed before any of `PO-70` was computed.** *Nothing below was run first and written after. The only
`PO-70` numbers quoted here are `cc66.40`'s, carried in from `r6911`, and the instrument's own comments.*

---

## ⛔ WHAT IS IN HAND AND IS NOT RE-DERIVED

1. **The object, as one number.** *This arm's projection retains $1.054$ times as much of its own source
   oscillation as the control's does — $0.2543$ against $0.2413$ — and the excess **rises** with wavenumber,
   $1.031$ below $q=3$ to $1.065$ above, **where the source ratio is flat** ($0.9922$, slope $-0.00106$).*
2. **The source is not where it is made.** *Source rungs $0.971$–$1.005$, the $\ell$ rung $1.042$–$1.052$, over
   four envelope windows, both envelope definitions, three term subsets, four $q$ sub-windows and with or
   without the $k$-measure. The step is $5.3$ floors.*
3. **Six mechanisms are excluded by direct substitution and are NOT re-run**: the wavenumber sampling
   (`KCONT=1`, $\ell$ rung unchanged at $1.0452$), the distance (`SRCXS`, and removing the difference takes the
   ratio **up**, $1.045\to1.051$), the visibility width **before** the kernel (rung 1 $\to$ rung 2 moves
   $-0.4\%$ and this arm's window is $15\%$ the wider, which shallows), the lensing and binning
   ($1.045\to1.047$), one source term alone, and the interference between two.
4. **`PO-56` is struck.** *Its characterisation is the input here. Nothing below re-derives it, and no
   attribution question is asked.*
5. **The floor is $0.6$ per cent**, set at `r6911` by the contrast statistic's own bias on a **known injected**
   contrast. *It is the floor for every ratio below, and it is the reason `1.054` is a finding at all.*

---

## ⛭ THE OBJECT, AND WHY IT IS A STATEMENT ABOUT A PHASE RATE

$$\Delta_\ell(k)=\int S(k,\eta)\, j_\ell\!\big(k(\eta_0-\eta)\big)\, d\eta , \qquad
C_\ell=\sum_k P(k)\,\Delta_\ell(k)^2$$

*Retention is the ratio of the oscillation the spectrum carries in $q$ to the oscillation the source carries in
$q$. An oscillation survives this integral to the extent that the source's acoustic phase **does not slide**
across the support the kernel gives it. So the whole question is a rate: **how much acoustic phase the plasma
accumulates per unit of the kernel's own time variable**, measured against the width of the window it is
accumulated over.*

⛭⛭ **AND THIS INSTRUMENT ALREADY WRITES THE ONE ASYMMETRY DOWN, AT `r6919+cc66.42`, IN ITS OWN COMMENT:**

> *"the acoustic phase is accumulated in LEAF conformal time while the projection kernel's argument
> $x_0=\eta_0-\eta$ is in STACKING conformal time, and on the arm those differ … `x0` is the same object on both
> arms: $\chi(\eta)=\eta_0-\eta$, so $d\chi/d\eta \equiv 1$ on each. **The two-clock structure is between $r_s$
> and $\eta$, NOT between $\chi$ and $\eta$.**"*

*`Jac_of` $= d\eta_{\rm leaf}/d\eta_{\rm stack}$ is $1.000000$ everywhere on the control and runs $0.789$ to
$0.913$ across $\pm 3$ FWHM of the visibility on the arm.* ⇒ ***So in the kernel's own variable the arm's
plasma advances its acoustic phase MORE SLOWLY, by that factor, and no other quantity inside the integral
distinguishes the two arms once the six exclusions are taken.***

⚠ ***AND THAT IS A READING, NOT A RESULT.*** *It is written here so that if the measurement says otherwise the
record shows what was expected. **The obvious objection to it is pre-registered below as `ⓔ`, because it is
fatal if it stands**: rung 1 $\to$ rung 2 integrates the source over the same window with the kernel taken out
and shows no excess, so a slide-across-the-window argument must explain why the kernel's weighting is sensitive
to a rate the bare $\eta$-integral is not. *If that cannot be shown, `M1` is dead and I will say so.*

---

## ⛭⛭ THE CANDIDATES, AND BOTH ROW OUTCOMES HAVE ONE

| | mechanism | which row outcome it reaches |
|---|---|---|
| **`M1`** | **PHASE-RATE RETENTION.** Retention is set by the dimensionless slide $\Sigma = k\,(dr_s/d\eta_{\rm stack})\,w$, with $w$ the **kernel-weighted** conformal width of the source's support. On the arm $dr_s/d\eta_{\rm stack} = c_s\,\mathrm{Jac} < c_s$. | **required by this background** |
| **`M2`** | **AN INTEGRATION ARTEFACT.** The $\eta$ quadrature (`NLOS=560`, a $75/25$ split), the $\eta$ end points, or the $k$ end interacting with the kernel's fast oscillation, resolved differently on the two arms' grids. | **an artefact of how the integral is carried** |
| **`M3`** | **A KERNEL-WEIGHT ARTEFACT.** The effective $\eta$-window the kernel gives the source differs between arms for a reason that is not the clock — e.g. the turning point $k\chi=\ell$ falling at a different place inside the visibility. | *either, and the test says which* |

⛔⛔ ***AND I AM NAMING THE FAILURE MODE 66 NAMED, BECAUSE IT IS `M2` THAT RESCUES THE FIT.*** *If the retention
is an artefact, the sector's numbers move and the comparison against the sky has not been made. **That is the
comfortable answer and it is the one this row must not reach by preference.*** ⇒ *So `M2` is tested **first**,
by a convergence test that can only confirm it or kill it, and its null result is pre-registered in words:
**"the integral is converged and $1.054$ is not a quadrature artefact"**. *If `M2` is confirmed I report it as
confirmed and say plainly that it is the reading that favours the construction.*

---

## ⛭⛭⛭ THE STAGING — AND THE INSTRUMENT IS ONE THAT IS ALREADY BUILT

*`SRCINJ=sweep` injects $S = g(\eta)\cos(k\,r_s(\eta)+\varphi)\,k^{(1-n_s)/2}$ — a **known** oscillation
through the real kernel, the real $\chi$, the real $k$ grid and the real visibility — with
`SRCINJRS` $\in$ {`own`, `stack`, `leaf`} choosing **which clock accumulates the phase** and `SRCINJVIS`
setting the window's conformal FWHM. **That is a targeted operation on the integral and nothing else**, and it
is why this row needs no new knob.*

| | stage | the gate |
|---|---|---|
| **ⓐ** | **`M2` FIRST.** `NLOS` refined on both arms, and the $\eta$ end points moved, with the retention ratio recomputed each time. | *the ratio moves by **less** than the $0.6\%$ floor $\Rightarrow$ converged; **more** $\Rightarrow$ `M2` is confirmed and the row's first outcome is reached* |
| **ⓑ** | **THE CLOCK SUBSTITUTION, ON THE INJECTION.** The same injected oscillation projected through the same kernel on the same arm with `SRCINJRS=leaf` against `stack`. Everything but the phase clock is held. | *the retention difference between the two clocks reproduces the sign **and** the size of the arm-minus-control excess $\Rightarrow$ the mechanism is **exhibited on the integral**; it does not $\Rightarrow$ `M1` is dead* |
| **ⓒ** | **A NUMBER NOT USED TO FIND IT.** From the background alone — $\mathrm{Jac}$ across the window, $c_s$, and the conformal FWHM `ETA_LS_W`, **no retention number anywhere in the calibration** — predict $\rho_a/\rho_c$ and the $q$-slope, then compare with $1.0539$ and with $1.031 \to 1.065$. | *the law is calibrated on the injection at **one** (width, clock) pair and must then predict at least **two** it was not calibrated on, and the two real arms* |
| **ⓓ** | **A CONFIGURATION IT WAS NOT FITTED ON.** The injection at a visibility width and a clock outside the calibration pair, and the real arms at a $q$ window outside the one the slope was read in. | *forward, no refitting; a law that needs a new coefficient per configuration is not a mechanism* |
| **ⓔ** | **THE OBJECTION TO `M1`, RUN AS A TEST AND NOT ANSWERED IN PROSE.** The **kernel-weighted** window against the bare one: the same injection projected with the kernel and with the kernel taken out, and the retention of each. | *if the two respond the same way to the clock, `M1` cannot explain why rung 1 $\to$ rung 2 shows no excess, and `M1` is dead on its own evidence* |

### ⚠ THE ARITHMETIC-IDENTITY GUARD, APPLIED BEFORE THE RUN

*`cc66.67` cost this row a revision to learn that a quantity which cannot fail is not a test. **Retention is a
ratio of ratios**, and there are two ways it can be one of those quantities:*

* *if the injected source's oscillation contrast is **normalised** by construction, the "source rung" is $1$ by
  definition and retention is just the $\ell$ rung — **that is fine and it is stated, not hidden***;
* *but if the same normalisation is applied to the $\ell$ rung, the ratio is identically $1$ and measures
  nothing.* ⇒ **Both rungs are printed for every injection, and any stage whose two rungs are related by an
  identity is reported as arithmetic and not as a measurement.**

⚠ *And the floor: **nothing under $0.6$ per cent is reported as a difference**, in either direction, including
a null result at ⓐ.*

---

## ⛭ THE PRE-REGISTERED WORDS, INCLUDING THE ONES THAT COST THIS SEAT MOST

* *If ⓐ shows the ratio moving above the floor under refinement:* ***"`1.054` IS A QUADRATURE ARTEFACT. Twelve
  revisions of `PO-56` were scored against a number the integral was not converged enough to carry, and this
  seat ran the projection at `NLOS=560` for all of them without testing it."***
* *If ⓑ reproduces the excess:* ***"the retention is required by this background: CR's own expansion law puts
  the plasma's phase on a clock the projection kernel does not share, and the $5.4$ per cent is this cosmology's
  prediction rather than a defect of the instrument."***
* *If ⓔ kills `M1`:* ***"the reading I wrote down before the run is wrong, and it is wrong for the reason I
  flagged as fatal in advance rather than one I did not see."***
* *If ⓐ is converged and no candidate is exhibited:* ***"the stage is located, the mechanism is still not, and
  `M1` is now excluded by substitution alongside the other six."*** ⌗ *That is a real outcome and it is
  reported as one, not dressed as progress.*

⌗ ***AND THE STANDING INVITATION IS TAKEN UP IN ADVANCE.*** *66 wrote: if the work starts to feel like looking
for the bug that rescues the fit, say so. **The check I will apply to myself is ⓐ's ordering**: the artefact
reading is tested first, on a criterion fixed here, and if it fails that criterion I do not return to it later
with a different one.*

---

## ⛔ THE GUARDS

*No corpus edits. No re-running the six excluded mechanisms. Nothing on `PO-56`. `cc66.61`'s floor and the
band-1 results not re-derived. No new statistics for their own sake. No aggregation or basis chosen where the
question does not fix one — and where one must be chosen, both are reported.*

* ⚠ ***A TOTAL IS NOT A MATCH*** — *66's, and here it applies to the retention ratio: reproducing $1.054$ is
  not the same as reproducing the $q$-dependence, and a mechanism that gets one and not the other has not been
  exhibited.*
* ⚠ ***AN ARITHMETIC IDENTITY IS NOT A MEASUREMENT, AND THE TIME TO SAY SO IS BEFORE THE RUN.***
* ⚠ ***THE INSTRUMENT MUST MATCH THE QUESTION'S GRAIN*** — *`cc66.60`'s error, met twice since. Retention is a
  property of a **modulated part**, so every comparison below is between modulated parts and never between
  whole vectors.*
* ⚠ ***A ROUNDED FIGURE IS NOT A BOUND*** — *`cc66.68`'s, and new. Every number reported from this row carries
  the digits it was measured to, and no fraction is offered for prose unless the measured value satisfies it.*
