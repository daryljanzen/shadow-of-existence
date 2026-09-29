# PRE-REGISTRATION — r7033+cc66.66

**Committed before any of `cc66.66` was computed.** *Nothing below was run first and written after.*

---

## ⛔ WHAT IS ALREADY IN HAND, SO IT IS NOT TABLED AS OPEN

1. **`cc66.65`'s three projections, measured, and they are not being re-litigated.** `ⓐ` the term mix's own
   cost $4.238$; `ⓑ` the part of the arm's excess it does **not** explain $4.005$; `ⓒ` the part it misplaces
   $1.482$. **The measurement is unchanged. Only the bar changes.**
2. **70's audit of the wrong-period null, which I asked for and which says my instinct about the margin was
   right.** $N_{\rm eff} = 3.07$ against 110 periods, so *"none of 110"* is worth about **one in four**, not one
   in 111; 6 of the 110 correlate with the comb above 0.5; the excluded window is narrower than one resolution
   element. ⇒ ***The wrong-period bar cannot carry an exit and I am not going to pretend otherwise.***
3. **The same audit strengthened `cc66.64`:** the arm's 7.30 clears an instrument-noise null of 2,000 draws with
   **0 reaching it** and a maximum of 2.54, and the five-sixths attribution survives. *That is a better result
   than the one I reported, and it is 70's to have found.*
4. **`cc66.61`'s floor and the band-1 results are finished work.** *Not re-derived, not softened.*

⌗ *And I want it in the record that **the bar I chose was the weak part of `cc66.65`, not the arithmetic gate I
was pleased with.** I flagged the margin as thin and asked for the audit; I did not work out that 82 bins over
$T=2.78$ can only hold about 3.6 independent frequencies, which is the fact that decides it.*

---

## ⛭ THE ORDER: THE SAME THREE PROJECTIONS, AGAINST 70's VALIDATED BAR

*2,000 draws of `COV` through my own pipeline, exactly 70's `Q3(iii)` construction:*

    dstar = shape_fit(mc, 1, dat) + L @ randn        # L = cholesky(COV), control shape + one draw
    -> recompute the excess terms against dstar, detrend over bands 4--7, project at period 1.00

⛔ **And the quadratic term carries no noise by construction** — $d$ is fixed and only $r_c$ moves — *which is
what `cc66.65` said it was and what 70 measured as $1.055 \pm 0.004$. So a quantity whose modulation sits in
$d^{T}Fd$ cannot fail this null, and that must be stated beside any such result rather than read as a pass.*

### ⛔⛔ THE ONE CONSTRUCTION CHOICE 70's AUDIT DID NOT FACE, AND I AM FIXING IT IN ADVANCE

*70 scored the **arm's** excess, which involves no fitted coefficient. **`ⓑ` and `ⓒ` do:* they are built with
$\beta$ and $\gamma$, estimated from the measured excesses.* ⇒ *** SO THE NULL MUST DECIDE WHETHER THOSE
COEFFICIENTS ARE RE-ESTIMATED PER DRAW. ***

* **PRIMARY: re-estimated per draw.** *The null then propagates the estimation, which is the honest bar — under
  the null the coefficients would have been fitted to noisy excesses too.*
* **REPORTED ALONGSIDE: held at their measured values.** *If the two differ materially, the difference is a
  statement about how much of `ⓑ`'s clearance is the regression chasing noise, and it is reported as one.*

⚠ ***This is `cc66.65`'s own guard applied again: a quantity built by fitting is not the same object as a
quantity read off, and the time to say which one is being scored is before the run.***

### THE EXIT, UNCHANGED IN SHAPE

| | reading | `PO-56` |
|---|---|---|
| **`ⓑ` clears, `ⓐ` fails** | the modulation is in what no channel this construction fixes accounts for | **TERMINATES** |
| **`ⓐ` clears** | the carrier is identified | **DISCHARGES** |
| **both or neither** | reported exactly as measured | *66's to place* |

⛔ ***AND THE EXPENSIVE BRANCH IS STILL THE TERMINATING ONE AND IS STILL TABLED FIRST.*** *It says the channel I
found at `cc66.64` — the first ever to cost anything where the arm is rejected — does not carry the structure.*

⚠ ***AND THE OTHER WAY THIS COSTS ME IS NEW:*** *`ⓐ` failed the old bar by **one period of 110**, which on 70's
reading is no margin at all. **A bar worth one in four failing something by one unit is equally capable of
passing it.** ⇒ If `ⓐ` clears the noise null, `cc66.65`'s reading was wrong in the direction I did not flag, and
I will say that in those words.*

---

## ⓶ THE ROUTED FINDING AGAINST `cc66.62`'s SCOPE STATEMENT — MINE TO CONFIRM, AMEND OR REJECT

*`cc66.62` said the anchored locator **"makes no amplitude claim at band 1"**. 70 reads that as true only in the
sense that it quotes no band-1 number: **its first trough anchor is inside band 1**, averaged with two outside.*

⇒ **I check the locator's own anchors against the band-1 edges and answer in one of three ways, fixed now:**
* **CONFIRM 70** — an anchor inside band 1 means the instrument *uses* band 1 even where it quotes nothing from
  it, and the claim needs a qualifier. *Then I write the qualifier.*
* **AMEND** — the anchor is inside band 1 but enters only through an average that cannot carry a band-1
  amplitude. *Then the distinction is stated, not the claim withdrawn.*
* **REJECT** — the anchor is not inside band 1. *Then 70's reading is wrong and I say so with the numbers.*

⛔ *`P15` does not carry the eleven-instrument scope claim, so **nothing in the corpus is affected either way**
and this is a correction to my own record, not to a paper.*

---

## ⓷ AND NOTHING ELSE

*No mechanism. No new candidate. No corpus edits — routed. No basis or aggregation chosen. `cc66.61`'s floor and
the band-1 results stay finished.*

---

## ⛔ WHAT WOULD MAKE THIS FILE WRONG

* *If my reproduction of the arm's 7.30 against the noise null does not match 70's reported 0-of-2,000 and
  maximum 2.54, I have not built 70's instrument and nothing below it can be read. **Checked first, as a gate.***
* *If a quantity's modulation sits in the noise-free quadratic term, it cannot fail this null and a "pass" there
  is not evidence. **Split every projection into its two terms, as before.***
* *If the per-draw and held-coefficient nulls disagree about an exit, no exit is reported.*
