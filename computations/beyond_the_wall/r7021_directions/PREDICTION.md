# `r7021 → cc66.62` — PRE-REGISTRATION, WRITTEN BEFORE THE MEASUREMENT

⛔ **What has already been looked at, said plainly, because it bears on ⓵'s first branch.** *The likelihood's
**structure** was inspected before this file was written — its bin edges, bin widths and covariance are
properties of the instrument and are fixed on disk regardless of any spectrum. `plik_lite` TT bins at a
median $0.0298$ in $q$, **one thirty-fourth of a comb period**, with $24$ bins inside band 1, and its
bin-to-bin correlation is a flat $\approx 0.15$ floor rather than a coupling that grows over a period.*

⇒ *** SO THE FIRST BRANCH IS ALREADY SETTLED AND I AM NOT PRE-REGISTERING IT AS OPEN: THE LIKELIHOOD IS NOT
A BANDED STATISTIC IN DISGUISE AT THE SCALE THAT MATTERS, AND IT DOES NOT INHERIT THE WIDTH LIMIT THROUGH
ITS COVARIANCE. *** ⌗ *It **does** bin — so the honest word is that it bins **thirty-four times finer than
the period**, which is the opposite of the limit that defeats every statistic in the demonstration.*

⛔ **Nothing else below has been measured.** *Committed as its own commit before `does_the_likelihood_see_it.py`
is run.*

---

## ⓵ DOES THE LIKELIHOOD SEE THE STEP?

**WHAT IS MEASURED, NAMED BEFORE USE.** *The likelihood supplies something no statistic in this row has had:
**a covariance**, so an uncertainty that is the instrument's own rather than an empirical scatter across
bands.*

1. **THE LIKELIHOOD'S DISCRIMINATING POWER PER BAND.** *With $r = m_{\rm arm} - m_{\rm control}$ binned on
   `plik_lite`'s own bins and $F$ the inverse covariance restricted to a band's bins,
   $S_B = \sqrt{r_B^{\mathsf T} F_{BB}\, r_B}$ is how many sigma of separation that band alone carries.*
2. **WHETHER THE STEP IS A LOCALISED CONTRIBUTION.** *$S_B$ at band 1 against its own bands 2–7 trend, on the
   same four bases with none chosen — the statistic this row has used throughout, now with a real error bar.*
3. **WHETHER THE TWO CHANNELS SEPARATE THERE.** *The Fisher distance between the two knob spectra restricted
   to band 1's bins, $\sqrt{(m_w - m_m)^{\mathsf T} F (m_w - m_m)}$, and each knob's distance from the
   control. **A channel is separable at band 1 if that distance exceeds 2.***

**THE OUTCOMES, THE ONE THAT ENDS THE ROW FIRST.**

| outcome | what it means |
|---|---|
| ⛭⛭ **THE LIKELIHOOD CANNOT SEPARATE THE CHANNELS AT BAND 1 EITHER** | ***the exit is proved across both instrument families and `PO-56`'s amended clause is met*** — a much stronger finish than one across statistics alone, and the row closes |
| ⛔ **THE LIKELIHOOD CAN SEPARATE THEM** | ***the row REOPENS with a measurement to make***: the demonstration covers the statistic family and not the instrument the paper runs beside it, and the clause is not met |
| ⚠ **it separates them but cannot localise the step** | the two questions come apart, and each is reported on its own — separability without localisation does not meet the clause and does not reopen it either |

⚠ ***NO PREDICTION IS OFFERED.*** *The likelihood has $24$ bins where the statistics had one band, which
argues one way; it also carries real noise where the statistics were noiseless theory, which argues the
other. **I do not know which dominates and that is exactly why the order is worth filling.***

⛔ **AND THE HAZARD, NAMED BEFORE IT IS MET.** *The statistics in this row are **noiseless** — their scatter
is structure in the spectra, not measurement error. The likelihood's is **real instrument noise**. ⇒ *So a
number from one is not comparable with a number from the other, and **the floor of `cc66.61` must not be
quoted against the likelihood's sigma or the reverse**. Each instrument is reported in its own units and the
comparison is made only in the one place it is legitimate: **whether each can or cannot separate the
channels at band 1.***

---

## ⓶ WHICH INSTRUMENTS THIS ROW HAS USED, AND WHICH OF THEM BAND

*A paragraph and not a measurement, as the order says. It is the **scope statement the terminal clause
needs**, so it is to be complete rather than representative: every instrument on which this row has made a
claim, each marked as banding or not, with the ones that band given the width they band at in units of the
comb period.*

⚠ *And the standard for "does not band" is named before use: **an instrument does not band if it makes its
claim without averaging over a stretch of $q$ comparable to the comb period.** An instrument that bins far
finer than a period bins, but does not band in the sense that defeats the demonstration, and it is to be
listed that way rather than in either bare column.*

---

## ⓷ AND WHAT IS NOT DONE

⛔ *No envelope, basis, abscissa or aggregation chosen. No new candidate. No mechanism. **And the floor
result of `cc66.61` is not revisited, softened or re-derived** — the order says it stands as measured and
this revision does not touch it. No corpus edits.*
