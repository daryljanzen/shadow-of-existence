---
name: statistics-inference-ledger
kind: FORWARD
current: r3160
job: The statistics/inference field-bake ledger — what bit, what bounced, and why. The last unbaked field in `THE_MATHEMATICS_REACH`'s candidate set, and the one `A5.5` needs. `OWED` 622.
sources: [cowork]
---

> **▣ FORWARD — the statistics bake, and part of the corpus.** *A field-bake ledger keeps three
> registers apart on purpose: **what bit**, **what bounced**, and **what the boundary is**. The bounce
> is data too — a field thrown at a corpus that already holds the thing returns a finding it owns, and
> `L-263` built `corpus/reach_baseline.py` because that had already happened twice.*
>
> **⌗ WHY THIS FIELD, AND WHY NOW.** *`THE_MATHEMATICS_REACH` flags it in its own voice:*
> ***"`Statistics / inference` is LISTED and NEVER BAKED — and `A5.5`'s reference class, P6's own first
> programme, is precisely a statistics problem."*** *A listed field never thrown, and an open item that
> needs exactly it, sitting one document apart. Opened as `OWED` 622 when `609` discharged.*


## ⛭ THE BASELINE, MEASURED FIRST

**Nothing below was called a hole before the corpus was asked what it holds.** *Seventeen paper bodies,
comments and bibliography stripped, de-macroed, via `corpus/reach_baseline.py`.*

| present, and substantially | absent across all seventeen |
| --- | --- |
| `likelihood` ×38 (P15×33) · `chi^2` ×22 · `dof` ×17 · `per degree of freedom` ×8 · `residual` ×89 · `covariance` ×25 · `prior` ×25 · `fitted` ×49 · `base rate` ×3 · `reference class` ×5 · `survivorship` ×3 | `statistical power` · `sample size` · `effect size` · `pre-registration` · `blinded` · `null hypothesis` · `hypothesis test` · `p-value` · `posterior` · `Bayes` · `look-elsewhere` · `trials factor` · `systematics` · `systematic error` · `nuisance` · `beam` · `censoring` · `odds ratio` · `bootstrap` · `Monte Carlo` · `cross-validation` · `overfitting` |

⚠ **AND THE INSTRUMENT EARNED ITS KEEP BEFORE THE BAKE STARTED.** *`degrees of freedom` is **×0 in
P15** — a paper with nineteen $\chi^2$ figures — which reads as a glaring hole and is not one: P15
writes `dof` (×11) and `per degree of freedom` (×7).* ⇒ ***A spelling, not an absence, and it would
have been the bake's first false finding.***


## ⛔⛭⛭ WHAT BIT — `S1`: THE FIRST PROGRAMME IS A POWER CALCULATION, AND IT HAS NOT BEEN DONE

`P06` states Lemma A5.5 in falsifiable form and calls the sampling that would test it *"the
discipline's first programme"*. **It is careful about every selection question a statistician would
raise** — it names *survivorship* (*"a reliability estimate built from one's own successes is
survivorship and not measurement"*), it names the censoring (*"a reference class assembled only from
episodes that reached a verdict will not contain this case"*), and it insists the
applied-and-disregarded episodes belong to the same sampling.

⇒ **The one question it does not ask is whether the class can be big enough.** *"Falsifiable" is a
property of the statement; **detectable** is a property of the design, and it is a number.*

**⓵ THE FLOORS.** *Exact Fisher one-sided, and exact binomial sign test, both validated against
`scipy` over 2304 tables and 460 binomial cases before use.*

| design | smallest class at which a PERFECT result reaches $0.05$ | best $p$ one below it |
| --- | --- | --- |
| two independent arms | **3 per arm (6 episodes)**, $p=0.0500$ | $0.1667$ — unreachable |
| paired, within-episode | **5 episodes**, $p=0.0312$ | $0.0625$ — unreachable |

**⓶ WITH THE COMPARATOR ARM EMPTY THE EVIDENCE IS NOT WEAK — IT IS ZERO.** *A one-armed study returns
$p=1$ however many successes it holds: $5/5$, $20/20$, $100/100$, all exactly $1$.* ⇒ ***Which is
`P06`'s own sentence made quantitative — "a compelling hypothesis with confirming instances, not a
calibrated reliability" — and stronger than it: not uncalibrated, but exactly nothing.***

**⓷ AND THE DESIGN THE PAPER PROPOSES IS THE EXPENSIVE ONE.**

| true effect | two-arm episodes for 80% power | paired episodes | saving |
| --- | --- | --- | --- |
| $0.9$ vs $0.5$ / $\theta=0.9$ | **38** | **8** | $4.8\times$ |
| $0.8$ vs $0.5$ / $\theta=0.8$ | **72** | **18** | $4.0\times$ |
| $0.7$ vs $0.5$ / $\theta=0.7$ | **168** | **37** | $4.5\times$ |

⛔ ***The moderate case is where it bites: 168 clean theory-choice episodes with a decisive non-local
measurement and a usable documentary record is not a population the history of physics contains.***
⇒ **So on a moderate true effect the two-arm programme cannot reach a verdict — and that is a fact
about the design, not about the lemma.**

⛭ **THE PAIRED DESIGN IS NOT A TRICK; IT IS THE STRUCTURE OF THE MATERIAL.** *Within a theory-choice
episode the candidates are **mutually exclusive** — heliocentrism winning IS geocentrism losing. So
every episode is a discordant pair, the comparison belongs INSIDE the episode, and the between-episode
variance the two-arm design pays for is never incurred.* ⌗ *With three live candidates the null is
$1/3$ and it is cheaper still.*

**⚠ ⓸ AND THE FIVE CANNOT BE SPENT.** *Read as a paired sign test, `P06`'s five instances give
$p=0.031$ against two candidates and $p=0.004$ against three — already significant.* ⇒ ***They may not
be so read, and the paper is what says why: they were selected because they succeeded, and a sign test
on outcome-selected episodes measures the selection.***

⇒ ⛭⛭ ***SO THE BINDING CONSTRAINT MOVES FROM SAMPLE SIZE TO SELECTION DISCIPLINE.*** *The two-arm
design fails on a scarce population; the paired design succeeds on a small one — but only if the
episodes are fixed before their outcomes are consulted. That is pre-registration, and the corpus
carries it ×0.*

**⌗ ⓹ AND THE EXACT TEST IS NOT MONOTONE IN $n$.** *At a true rate of $0.9$: eight episodes give
$0.813$ power and **ten give $0.736$**.* ⇒ **Collecting two more episodes can lower the chance of
detecting a real effect.** *That is the discreteness of an exact test on a small class, it is invisible
to a normal approximation, and it is a planning fact the programme would need.*

`receipts/L271_the_statistics_bake/S1_*.py` — 20 checks.


## ⛭⛭ WHAT BOUNCED — `S2`: THE SYSTEMATICS BUDGET IS ABSENT BY NAME AND PRESENT AS A MATCHED CONTROL

*Seventeen papers carry `systematics` ×0, `systematic error` ×0, `nuisance` ×0, `beam` ×0 — while
quoting a **seventy-sigma** disagreement against Planck. That reads like the sharpest finding in the
bake and it is a bounce.*

**⓵ THE SIGMA IS THE PAPER'S OWN ARITHMETIC AND IT IS RIGHT.** $0.615/0.008 = 76.9$, *from a separation
and an uncertainty both stated in `P15`.* ⚠ *But seventy sigma is not a probability — past five or six
the tail reports the model of the errors — so what the number carries is a **ratio**: how many times
the quoted uncertainty fits into the discrepancy.*

**⓶ AND THE BUDGET IS BEING TAKEN.** *`P15` does not compare its construction to the sky and stop. It
measures a $\Lambda$CDM control **by the identical procedure** and reports that* ***"the control stands
in for the sky on this quantity to within seven parts in a thousand of the disagreement it is used to
measure."*** ⇒ ***That is a systematics control: any error the procedure makes on the sky it makes on
the control, and differencing removes it.***

⌗ *And the paper does not overclaim: it says outright* **"That number should not be read as the
disagreement itself"**, *shows the disagreement does not go with the phase, and elsewhere refuses a
likelihood it judges unable to arbitrate —* **"the ordering is a fact and the ratio is not a
$p$-value"**, **"the likelihood cannot arbitrate here"**, **"a control a hundred times too poor
certifies nothing about what it is compared with."** ⇒ **Better discipline than the vocabulary count
suggests, which is exactly why the count is not the finding.**

**⌗ ⓷ WHAT IS OWED IS A SENTENCE, NOT A SECTION** — *name what the control is doing, and state the
**robustness factor**, which is the quantity a seventy-sigma claim actually rests on:*

| verdict falls to | $\sigma(\phi/\pi)$ required | factor the quoted $\sigma$ would be wrong by |
| --- | --- | --- |
| $10\sigma$ | $0.0615$ | $7.7\times$ |
| $5\sigma$ | $0.1230$ | $15.4\times$ |
| $3\sigma$ | $0.2050$ | $\mathbf{25.6\times}$ |

⇒ ***A one-multipole resolution assumption wrong by a factor of five would leave the verdict standing.
Showing that is worth more than the seventy, and the paper computes the seventy and not this.***

`receipts/L271_the_statistics_bake/S2_*.py` — 17 checks.


## ⌗ THE CROSS-FIELD RECURRENCE THIS BAKE ADDS

**The corpus's characteristic failure is not error. It is anonymity.** *Fourth instance in the reach
work of a method present and correct under no name:*

| | the thing | where |
| --- | --- | --- |
| 1 | the Atiyah sequence is not missing from `P12` — it is `P12`'s object under four other names | `L-265`, r3152 |
| 2 | the sector rests on $N_{\rm eff}$ at both ends and names it in no paper — *"one missing NAME, not a missing sector"* | `R-P` ⑨, r2544 |
| 3 | the information-paradox resolution is the baby-universe one, never named | `R-P` ⑩, r2540 |
| 4 | the systematics budget is taken by matched-procedure differencing, never named | `L-271` `S2`, r3160 |

⇒ **A bake's third product, after the bites and the bounces, is the recurrence no single field sees —
and this is one.**


## ⌗ THE BOUNDARY — WHAT THIS BAKE DID NOT REACH

- **The `plik_lite` marginalisation.** *`P15` uses the published bandpowers and covariance in the
  likelihood comparison, and that product is already marginalised over foregrounds and nuisance
  parameters. **The seventy-sigma denominator is a separate, hand-propagated resolution scale**, and
  the two are distinguished in `S2` rather than merged. What `plik_lite` carries and what the paper
  inherits from it is a separate reading and is not made here.*
- **Bayesian model comparison.** *`posterior` ×0, `Bayes` ×0, `marginal likelihood` ×0. That is a real
  absence and it was not thrown, because `P15` states plainly that on the peak-height statistic
  **"the likelihood cannot arbitrate here"** — and an evidence ratio computed where the likelihood
  cannot arbitrate would be the same error wearing a prior. **Open, and it needs the transfer function
  the paper says is still open, not a statistical technique.***
- **`P04`'s redshift-isotropy inference.** *`isotropy` ×36 in `P04`, `scatter` ×8, `anisotropy` ×4 —
  a live inference not read here. **Named as owed rather than left implicit.***
- **The reference-class problem as a named philosophical object.** *`P06` reinvents the sampling
  difficulty carefully and correctly; whether the literature on it (Reichenbach, and the modern
  treatments) has anything the paper does not already have is a READ, not a computation, and is not
  claimed either way.*

⛔ **AND THE ONE THING THIS BAKE MUST NOT BE READ AS SAYING:** *nothing here estimates the effect in
`A5.5`. Every figure above is about what a design can **detect**. The lemma's truth is exactly as open
after this bake as before it — what changed is that the programme to test it now has a price list.*
