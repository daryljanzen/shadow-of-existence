# `r7019 → cc66.61` — PRE-REGISTRATION, WRITTEN BEFORE ANY OF IT WAS COMPUTED

⛔ **Nothing below has been measured.** *Committed as its own commit before `resolving_power.py` is run.*

---

## ⓵ RESOLVE OR EXCLUDE — AND A POWER CALCULATION IS A MEASUREMENT, SO IT IS DEFINED BEFORE IT IS MADE

**THE QUANTITY, NAMED BEFORE USE.** *A channel is **resolved** on the differential estimator when its band-1
departure $d$ exceeds twice its own bands 2–7 scatter $\sigma$. So the **resolving ratio** is $2\sigma/\lvert
d\rvert$: the factor by which $\sigma$ must fall for that channel to be decided. ⌗ *And it is computed twice
— against the channel's **own measured** departure, and against the departure a channel would have if it
carried the **whole** step, $f\,d_{\rm arm}$ at $f=1$ — because those are different questions and only the
second bears on `PO-56`.*

**AND WHAT COULD BRING $\sigma$ DOWN, EACH TESTED RATHER THAN ASSERTED.**

1. **THE HELD-PERIOD AGGREGATION APPLIED TO THE KNOBS AS WELL AS THE ARM.** *`cc66.60` showed the raw band
   dispersion samples $0.70$ of a comb period and is phase-dependent by construction, its ratio to the
   phase-insensitive reading running $0.886$–$1.367$ across bands. ⇒ **That is a band-to-band wobble of
   tens of per cent which is geometry and not signal**, and it enters $\sigma$ directly. *This is the
   candidate I expect most from, and saying so before measuring is the point of writing it down.*
2. **THE ABSCISSA PAIRING** — per common $\ell$ against per common $q$. *`cc66.59` found them agreeing to a
   fiftieth, so I expect little, and it is tested anyway.*
3. **A LONGER LEVER ARM** — the banks reach $q = 6.6$ where the bands stop at $5.75$. *One more band is
   available; whether it lowers $\sigma$ or raises it is not obvious, because the damping tail is steeper
   there.*
4. **MORE BANDS ACROSS THE SAME RANGE** — *finer edges give the trend fit more points; whether the residual
   scatter falls with them is a property of the data and not of the counting, so it is measured.*

**THE OUTCOMES, BOTH PRE-REGISTERED AS THE ORDER ASKED.**

| outcome | what it means |
|---|---|
| ⛭ **something banked brings $\sigma$ down enough** | the channels become decidable and the row has a measurement to make rather than a limit to report |
| ⛔⛔ **nothing available reduces it enough** | ***that is `PO-56`'s terminal exit arriving***: a candidate list whose members cannot be resolved against the object by any statistic this construction can build — **a demonstration, not a shrug**, and it must be stated with the required factor and the achievable one side by side |

⚠ *No prediction on which. I expect the held-period aggregation to help and I do not know whether it helps
**enough**, and those are different claims.*

---

## ⓶ THE PHASE AGAINST THE COMB, BY THIS SEAT'S OWN PRESCRIPTION

**THE MEASUREMENT, NAMED BEFORE USE.** *Not a local fit in a window one period wide, where amplitude and
phase are degenerate. Instead the comb phase is projected over a **long stretch**: for a stretch $[q_0,q_1]$
and the comb period $P$,*
$$C = \int o(q)\cos(2\pi q/P)\,dq,\qquad S = \int o(q)\sin(2\pi q/P)\,dq,\qquad \varphi = \operatorname{atan2}(-S, C),$$
*taken on each arm, with $\Delta = \varphi_a - \varphi_c$. ⌗ *Over five periods the phase is determined by
the whole stretch rather than by one window, which is the point.*

**AND THE UNCERTAINTY IS MEASURED, NOT ASSERTED:** *by splitting the upper range into disjoint stretches and
taking the scatter of $\Delta$ across them.*

| outcome | what it means |
|---|---|
| **$\Delta$ at band 1 is consistent with $\Delta$ above it** | the phase carries no step; **`cc66.60`'s amplitude verdict becomes complete** rather than sign-only |
| ⛭⛭ **$\Delta$ at band 1 differs resolvably** | ***the estimator is not measuring what `cc66.60` ⓵ assumed***, and the amplitude verdict is incomplete — the order is right that this tests ⓵'s premise from the other side |
| ⚠ **the long-stretch reading is itself unresolved** | then the phase channel is beyond this construction's reach and that is said plainly, with the achieved precision quoted |

---

## ⓷ IS THE COMPOSITION CANCELLATION EXACT OR APPROXIMATE?

*Two knobs that **multiply** on the contrast and **cancel** on the step is a structural statement. ⇒ *So the
cancellation is tested for exactness across **all four trend bases and both aggregations** — eight readings —
rather than at one.*

**NAMED BEFORE USE:** *the cancellation is **exact** if the joint's departure is consistent with zero on every
one of the eight, and **approximate** if it is consistent with zero on some and not others; the residual is
quoted against the joint's own scatter and against the size of the two singles it cancels between.*

| outcome | what it means |
|---|---|
| **exact on all eight** | ***a constraint, not a coincidence*** — and a constraint on how two knobs compose on the step is a property of the **projection** rather than of the knobs |
| **approximate** | a coincidence at the sizes their profiles happen to solve, and it is reported as that |

⚠ *And the honest third possibility is named too: **the joint's scatter may be too large for either word**, in
which case ⓷ inherits ⓵'s answer and says so instead of choosing.*

---

## ⓸ AND WHAT IS NOT DONE

⛔ *No envelope, basis, abscissa or aggregation chosen. No new candidate. No mechanism. No corpus edits.*

⚠ **AND THE HAZARD ⓵ CARRIES.** *A power calculation invites its own abuse: **choosing the aggregation that
makes $\sigma$ smallest and then quoting the departure measured on it**. ⇒ *So the resolving ratio is reported
for every aggregation, and any statement that a channel is resolved must hold on the SAME reading that
measured its departure — never one from a different one.*
