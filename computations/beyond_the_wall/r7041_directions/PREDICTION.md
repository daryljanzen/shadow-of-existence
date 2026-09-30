# PRE-REGISTRATION — r7041+cc66.70 — **the convergence validation of the CR arm**

**Committed before any of `r7041` was computed.** *`r7039`'s order is withdrawn. Everything this seat had
in flight on it is named below as kept or held, and nothing held is quoted as a result.*

---

## ⛔ WHAT `r7041` WITHDREW, AND WHAT THIS SEAT HAD IN FLIGHT WHEN IT ARRIVED

*`r7039` posed a mechanism row with two co-equal outcomes. `r7041` withdraws the balance — the presumption
is the instrument — and **fixes the order of work: convergence first.** ⇒ *A mechanism found before the arm
is known to be converged is a mechanism found in an unconverged integral.**

| what was in flight | status under `r7041` |
|---|---|
| the acceptance law `M1`, and its forward predictions | ⛔ **HELD.** *It is a mechanism. Nothing from it is reported as a result and no stage of it is run further until ⓐ–ⓒ are answered.* |
| `DLKSAVE` — the transfer $\Delta_\ell(k)$, saved for the first time | ✔ **KEPT, and it serves this order better than the last one**: truncation and under-sampling in $k$ are visible in the transfer and invisible in its $k$-sum, which is the only thing the instrument used to report. |
| `NLOSW`, `NLOSF` — the $\eta$-grid's half-width and split, made names | ✔ **KEPT.** *These are exactly ⓐ's "$\eta$-sampling of the line-of-sight integral" and they were literals until this revision.* |
| the injection runs already on disk (`NLOS`, `NLOSW`, `NLOSF`, both arms) | ✔ **KEPT as ⓒ data.** *The launcher is idempotent against the same paths, so the four completed slices are reused and not re-run.* |
| one structural fact, measured and reported as available rather than acted on | ⌗ *For the fixed injection the integral factorises exactly — residual $3\times10^{-15}$ on the saved transfer. **It is stated in the reply as a fact and not built on, because building on it is the mechanism this order defers.*** |

⌗ ***AND THE FAILURE MODE WORTH NAMING IS NOT THE ONE `r7039` NAMED.*** *That order warned against looking
for the bug that rescues the fit. **This one's risk is the opposite and it is mine: having built an
apparatus for a mechanism, the temptation is to report its output anyway.** The line I am holding is that
nothing from `M1` appears in a result until the arm is converged.

---

## ⛔ ONE SCOPING CORRECTION TO THE ORDER, BECAUSE IT COMPARES TWO DIFFERENT STATISTICS

*`r7041` ⓒ reads: "the identical-source result … giving $1.066$, **exceeding the real $1.047$**".*

| number | what it is |
|---|---|
| $1.0659$ | the **injection's** arm-to-control ratio of the projected oscillation — its retention ratio, since the injection carries $k^{(1-n_s)/2}$ so its source contrast is identical on the two arms by construction |
| $1.054$ | the **real source's retention** ratio — the $\ell$ rung divided by the source rung |
| $1.0452$ / $1.0468$ | the real source's raw and lensed-and-binned $\ell$-rung contrast ratios |

⇒ ***So $1.047$ is an $\ell$-rung contrast ratio and $1.066$ is a retention ratio.*** *The like-for-like
pair is $1.0659$ against $1.054$.* ⌗ **The order's conclusion is unchanged and slightly weaker than
stated:** *the injection over-delivers by $1.1$ per cent, not $1.8$.* ⚠ *Reported because a $0.7$ per cent
difference matters in a row whose effect is four per cent and whose floor is $0.6$.*

---

## ⛭⛭⛭ ⓐ AND ⓑ — THE MIRROR OF `C59`, ON THE ARM, WITH THE CONTROL AT EVERY SAME SETTING

*Four settings, each varied alone with the others held, **on both arms**, reporting at every setting: the
contrast statistic, the arm-to-control **retention**, $P_1/P_2$, $P_1/P_3$ and $\ell_1/\ell_A$.*

| setting | sequence | why this direction |
|---|---|---|
| $k_{\max}$, via `KFAC` | $2.0 \to 2.6 \to 3.2 \to 4.0$ | ⛔ **UPWARD ONLY, and the downward half is refused by the instrument's own guard**, which fails closed at $k_{\max}/\ell_{\max} < 1.9$. *That refusal is the report, not a thing to work around: `KFAC=2.0` sits at ratio $2.00$, a hair above the guard, so the corpus default is the guard's floor and the only available sequence runs up from it.* |
| the mode count `NK` | default $\to 1.5\times \to 2\times$ | ⚠ **and the arms do not have this knob in the same sense** — see below |
| the $\eta$ sampling | `NLOS` $560\to1120\to2240$; `NLOSW` $6\to9$; `NLOSF` $0.75\to0.90$ | resolution, extent and the split between the two scales are three separate choices and are moved separately |
| the reported $\ell$ grid | `LSTEP` $8 \to 4$ | *the statistic reads an envelope over one comb period in $q$, so the $\ell$ grid is part of the instrument and not only of the output* |

### ⚠ ⓑ's ANSWER MAY BE STRUCTURAL RATHER THAN NUMERICAL, AND I AM SAYING SO IN ADVANCE

*Read off the instrument's own `main`: on the control `lL = linspace(12, KMAXL, NK*3)`, so **sampling and
extent are separable** — `NK` moves the spacing at fixed reach. On the arm the ladder is
$\sqrt{L(L+2)}\,\times$`stretch` out to `KMAXL`, so **the spacing is fixed by the construction and `NK` acts
only as a decimation cap that is not reached at the reported settings.***

⇒ *** SO "THE SAME SETTING" IS NOT THE SAME OPERATION ON THE TWO ARMS FOR `NK`: on the control it is a
convergence knob and on the arm it is inert. *** *If that is what the runs show, ⓑ's answer is that one of
the four settings cannot be compared at all, and the comparison has to be carried by $k_{\max}$, the $\eta$
grid and the $\ell$ grid.* ⌗ *`KCONT=1` is the one operation that gives the arm a uniform grid and it is
**not** re-run — it is among the six excluded, banked with the $\ell$ rung unchanged at $1.0452$.*

---

## ⛭⛭ ⓒ — THE DIRECT TEST, AND IT IS THE CHEAP ONE, SO IT IS RUN FIRST

*The injection skips the solver, so the whole sequence is affordable on both injections and both arms:*

* **`SRCINJ=sweep SRCINJRS=own`** — the $1.0659$ the order names.
* **`SRCINJ=fixed`** — the standing oscillation, $1.0587$, *carried alongside because its $q$-slope matches
  the real source's to two per cent and the order's question is about the real source.*

⇒ **The pre-registered reading:** *if either ratio **walks toward unity** as the settings refine, the
retention is the integrator's and the row is answered against the construction. If both sit still to better
than the floor, the injection's over-delivery is not a convergence artefact.*

---

## ⛭ ⓓ — `r3512`'s GATE ORDER 1, 2 AND 4

*Validating $\Pi$ on the control, the `PISRC` subtraction, and the CR run — named outstanding at `C60` and
still outstanding.* ⌗ *Run after ⓒ and alongside ⓐ, since the CR run is ⓐ.*

---

## ⛔⛔ WHAT COUNTS AS CONVERGED, FIXED HERE AND NOT AFTERWARDS

| quantity | converged when | where the number comes from |
|---|---|---|
| the arm-to-control **retention** | the step between the last two refinements is **under $0.6$ per cent** | `r6911`'s floor, set on a **known injected** contrast |
| $P_1/P_2$, $P_1/P_3$ | the step is **under $1$ per cent** | **`C59`'s own accepted step**: $1800\to2400$ moved $2.399\to2.393$ ($0.25\%$) and $2.791\to2.768$ ($0.82\%$), and it declared that converged |
| $\ell_1/\ell_A$ | within **one grid step** of the previous refinement | the instrument's own resolution |

⚠ *A sequence that has not turned over is **not** converged, whatever its last step: a monotone drift under
refinement is reported as a drift and the setting as unconverged, even if the last step is small.*

⚠ *And nothing under the floor is reported as a difference, in either direction — including a null result.*

---

## ⛭ THE PRE-REGISTERED WORDS

* *If the arm's retention drifts above the floor under any setting:* ***"THE ARM WAS NOT CONVERGED. The
  four per cent was measured on an integral that moves by more than that under its own numerical settings,
  and twelve revisions of `PO-56` plus `cc66.40`'s own step of $5.3$ floors were scored against it."***
* *If every setting converges and the retention survives:* ***"the arm is converged on its own background
  in every setting `C59` moved, the retention survives at $1.05$, and the presumption has been discharged —
  the mechanism question is now asked of a converged integral."***
* *If ⓒ's injection ratio walks toward unity while ⓐ's real-source retention does not, or the reverse:*
  ***"the two disagree, and the disagreement is the finding: the injection is not the real source and this
  row has been reading it as a proxy."***
* *If `NK` turns out inert on the arm:* ***"one of the four settings cannot be compared between the arms at
  all, and the record should say that rather than reporting an agreement that is an identity."***

---

## ⛔ THE GUARDS

*No mechanism — the guard is lifted but the order of work is fixed and convergence comes first. No corpus
edits. Do not re-run the six excluded explanations. No new statistics: `r6911`'s contrast statistic and
`r6919`'s ratio statistic unchanged, and the retention defined exactly as `cc66.40` defined it. `KFAC` is
raised **only** in convergence runs and no reported spectrum moves off $2.0$ on this revision.*

* ⚠ ***A TOTAL IS NOT A MATCH*** — *66's. Converging the heights is not converging the retention, which is
  the whole reason this order exists.*
* ⚠ ***AN ARITHMETIC IDENTITY IS NOT A MEASUREMENT*** — *and `NK` on the arm is the candidate for one.*
* ⚠ ***THE INSTRUMENT MUST MATCH THE QUESTION'S GRAIN*** — *`cc66.60`'s.*
* ⚠ ***A ROUNDED FIGURE IS NOT A BOUND*** — *`cc66.68`'s.*
* ⚠ ***A PRE-REGISTRATION IS WRITTEN AGAINST THE REGISTER, NOT AGAINST THE CODE*** — *`cc66.69`'s, and it
  is why the scoping correction above was found before a run and not after.*
* ⚠ ***AND A HELD STAGE IS NOT A QUIET ONE*** — *new, this revision's. Having built an apparatus for a
  withdrawn order, the risk is reporting its output anyway; `M1` is named as held in the reply so that its
  absence from the results is visible rather than assumed.*
