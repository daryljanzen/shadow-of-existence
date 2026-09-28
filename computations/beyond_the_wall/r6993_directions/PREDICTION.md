# r6993 — WHAT EACH CANDIDATE SHAPE PREDICTS, AND WHICH PAIRS THIS MEASUREMENT CANNOT SEPARATE

*Committed **before any fit**. ⛭ The tolerances below are written on the estimator resolution **measured**
in `filter_control.py` (the order's ⓷), which is why that control was run first: the alternative is to
guess a resolution, and a guessed tolerance is the defect `cc66.47`'s pre-registration lesson is about.*

## WHAT ⓷ ALREADY ESTABLISHED, AND WHICH THIS PRE-REGISTRATION IS BUILT ON

* ✔ **A known $q$-dependence reads back.** Six forms injected into the control's own spectrum — a
  constant, a rise linear in $q^{2}$, a power law, a logarithm, and two turnovers with a **scale** in
  them — recover with a worst error of $\mathbf{1.3}$ **per cent**. *So the filter can see the shapes it
  is being asked to filter on, including the one that would name a physical length.*
* ⚠ **The estimator carries a fixed per-band bias of about one per cent**, agreed on by all six forms to
  $0.36$ per cent. ⇒ ***A constant contrast reads as a wobble.*** **So band-to-band structure at the
  per-cent level is the instrument and is not to be read as the effect.**
* ✔ **The excess's rise survives the envelope window**: the variation statistic reads $0.44$, $0.44$,
  $0.40$ at mean-envelope windows $0.8$, $1.0$, $1.2$ — far above that bias.
* ⛔ **The median envelope is NOT a valid alternative anchoring, and is excluded with its reason.** It
  would have given $1.49$ and been the headline of the control. *The tell is that it does not move with
  its own window — the last band reads the same to seven figures at $0.8$ and $1.2$ — because at high $q$
  the running median collapses onto the curve itself (within $3.6$ per cent of it) where the mean
  envelope sits $14$–$17$ per cent away and moves.* **An estimator insensitive to its own smoothing
  scale is not measuring what it is meant to.**

⇒ **PER-BAND UNCERTAINTY ADOPTED: $\sigma = 0.013$**, the worst injected-form recovery error. *It is a
systematic, not a scatter, and it is the honest one to use because it is the size of the wobble the
instrument manufactures.*

## THE FORMS TO BE COMPARED

With $R(q)$ the measured band contrast ratio, $A$ a free amplitude and $q_0$ a free scale:

| # | form | $R(q) - 1 \propto$ | free | has a scale? |
|---|---|---|---|---|
| F0 | constant | $A$ | 1 | no |
| F1 | linear in $q^{2}$ | $A\,q^{2}$ | 1 | no |
| F2 | power law | $A\,q^{\alpha}$ | 2 | no |
| F3 | logarithm | $A\ln q$ | 1 | no |
| F4 | turnover | $A\,q^{2}/(q^{2}+q_0^{2})$ | 2 | **yes** |
| F5 | saturating exponential | $A\,(1-e^{-q/q_0})$ | 2 | **yes** |

## ⛔ THE SELECTION RULE, FIXED NOW

* Each form is fitted by least squares on the seven band values at $\sigma = 0.013$.
* **A form is declared PREFERRED only if it beats the next-best by $\Delta\chi^{2} > 4$** — two standard
  errors on one parameter. ⌗ *Anything short of that is reported as "not separated", by name.*
* **A form is declared EXCLUDED only if its own $\chi^{2}/\nu > 3$.** ⌗ *A form that merely fits worse
  than another is not excluded; this sector has enough eliminations claimed on less.*
* ⛔ **Monotonicity is judged on the RISE and not on the band-to-band ordering**, because ⓷ measured that
  the ordering carries a one-per-cent artefact and the wobble in the seven values is that size.

## ⚠ AND WHAT THIS MEASUREMENT CANNOT DO, SAID FIRST

*The clause that made `cc66.49` believable was the one that named a separation the test could not make,
before it failed to make it. The same is owed here, and it is owed with more force, because seven points
at one-per-cent resolution is a weak instrument for choosing a functional form.*

* ⛔ ***F2 (power law) and F3 (logarithm) will NOT be separated.*** *Over $q = 1.2$ to $5.4$ — a factor
  $4.5$ — a power law with a small index and a logarithm are both slowly-varying and concave, and with a
  free amplitude they differ across the range by far less than $\sigma$. **Predicted: $\Delta\chi^{2} < 4$
  between them.***
* ⛔ ***F2 and F4 (turnover) will NOT be separated either*** when the fitted $q_0$ lands at or above the
  top of the measured range: a turnover whose scale sits outside the data is a power law inside it, and
  the data stop at $5.4$. ⇒ ***So a fitted $q_0$ is only meaningful if it lands INSIDE the range with its
  uncertainty, and I state now that a $q_0$ at the edge will be reported as "no scale resolved" and not
  as a scale.***
* ✔ ***What this measurement CAN do is separate the CONVEX family from the CONCAVE one*** — F1, which
  accelerates with $q$, against F2/F3/F4/F5, which all decelerate. *The excess spans about $5.5$ points
  of ratio against $1.3$ of resolution, so the sign of the curvature is reachable where its detailed
  form is not.*
* ⌗ ***And F0 is the null this row already knows is false*** — it is fitted anyway so that the improvement
  over it is a stated number rather than an impression.

## WHAT WOULD MAKE ⓶'s FILTER USABLE, STATED BEFORE IT IS APPLIED

*The order asks for a hard filter: a candidate must vary across wavenumber by something near forty-four
per cent of its own value.* ⇒ **I will quote the filter as a RANGE and not as a point**, spanning the
mean-envelope window variation already measured ($0.40$–$0.44$), and a candidate is ruled out on sight
only if its own variation is below the bottom of that range by more than the estimator bias. ⛔ *A filter
quoted as a single number would reject candidates on a digit the control says is not there.*
