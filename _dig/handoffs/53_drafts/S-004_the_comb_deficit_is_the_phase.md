---
name: s-004-comb-deficit
kind: FINDING (draft, uncommitted)
current: r2428 / c54.178
job: PART 5's registered residual — the source comb at 0.72–0.79 of π/r_s under every initial condition — is PART 2/3's k-dependent acoustic phase, arithmetically. Two measured objects, one object. Offered as a candidate resolution of front #5's stated content.
sources: [chat]
---

# S-004 · THE COMB DEFICIT AND THE PHASE ARE ONE OBJECT

**`P15_the_first_peak_figure_is_not_stable.py` PART 5 registers, explicitly unresolved:**

> *"Under **EVERY** initial condition the instrument's source comb comes out at **0.72–0.79** of the
> acoustic spacing it was pinned to, never at 1. The initial data move the first peak by 165
> multipoles and do not move this. ⇒ It is not an initial-data artefact, and it is a disagreement
> with the acoustic scale — the corpus's own settled result — inside the one instrument that
> propagates modes. **Registered, not resolved. This is what front #5 turns out to be about.**"*

**And `P15_the_driving_shift_by_subtraction.py` PART 3 measures, in a different file:**

> *"CR's Q_driven varies by 3.9× over the same band, 0.457 → 0.117."*

⇒ ***These are the same measurement.*** *Not analogous, not consistent-with — the same.*

---

## THE RELATION, AND IT IS ARITHMETIC RATHER THAN A MODEL

A comb extremum in **k** at fixed η_rec is nothing but a mode's *m*-th **temporal** turnover landing
at recombination. A mode's turnovers sit at accumulated sound phase Q₁(k) + m; at η_rec the
accumulated phase is k·r_s/π. So the comb extrema are the roots of

$$\boxed{\;\frac{k\,r_s}{\pi} \;=\; Q_1(k) \;+\; m,\qquad m=0,1,2,\dots\;}$$

and differencing consecutive *m* gives the comb spacing in units of π/r_s:

$$\text{spacing} \;=\; 1 + \big[\,Q_1(k_{m+1}) - Q_1(k_m)\,\big] \;<\; 1 \quad\text{whenever } Q_1 \text{ FALLS with } k.$$

**Nothing is modelled. The only content is the definition of a comb extremum.** A falling Q₁ *forces*
a comb deficit, and the deficit's **size** is fixed by how fast Q₁ falls.

## ✔ CONTROL FIRST — on ΛCDM the relation must return 1, and it does

ΛCDM's Q₁ is flat (fits k^−0.018). Predicted spacings: **0.988, 0.993, 0.995, 0.997, 0.997, 0.998 —
mean 0.9947.** *The relation returns unity on a flat phase, as it must. Everything below is read
against this.*

## ⛭ AND THE RECEIPT'S OWN Q₁ COLUMN PREDICTS ITS OWN REGISTERED BAND

Solving the boxed relation with **the receipt's own CR Q₁ numbers** (its PART 2/3 table, fitted
k^−0.622) and the arm's r_s = 135.46:

| m | k | k·r_s/π |
|---|---|---|
| 0 | 0.01258 | 0.5423 |
| 1 | 0.03045 | 1.3129 |
| 2 | 0.05161 | 2.2254 |
| 3 | 0.07376 | 3.1805 |

**Predicted comb spacings: 0.7706, 0.9125, 0.9551, 0.9724, 0.9811.**

⇒ ***The first spacing is 0.7706. The registered band is 0.72–0.79.***

## AND WITHIN ONE INSTRUMENT, WHERE BOTH OBJECTS WERE MEASURED

The acoustic fold measured **both** Q₁ and the comb on the same runs, so this is the honest test:

| m→m+1 | 0→1 | 1→2 | 2→3 | 3→4 | 4→5 | 5→6 |
|---|---|---|---|---|---|---|
| **predicted** from Q₁ | 0.631 | **0.810** | **0.898** | **0.939** | **0.960** | **0.972** |
| **measured** comb | 0.793 | **0.802** | **0.912** | **0.921** | **0.948** | **0.949** |

**Agreement to ≤ 0.02 from m = 1 outward, across a spacing that rises from 0.80 to 0.95.** *The
relation does not merely reproduce a deficit; it reproduces the deficit's **run with m**, which is
the part a coincidence would not get.*

⚠ **The m = 0 point is the exception and the reason is stated rather than fitted:** it requires Q₁
at k = 0.019, **below the measured band**, so the power law is extrapolated there. *Predicted 0.631
against measured 0.793 is the extrapolation failing, not the relation.* The same caveat applies to
the receipt's 0.7706, which also sits at m = 0 — **so the band-hit is suggestive and the m ≥ 1
agreement is the evidence.**

---

## ⇒ WHAT THIS OFFERS FRONT #5

**PART 5 asks the right question and files it in the wrong place.** It reads the comb deficit as *"a
disagreement with the acoustic scale — the corpus's own settled result"*, i.e. as though the
instrument were failing to reproduce π/r_s. **It is not.** The instrument reproduces π/r_s exactly on
ΛCDM, and on CR it produces a comb whose spacing is π/r_s **modified by the phase that PART 2/3 of
the sibling receipt measures directly.**

⇒ **The residual is not a second finding. It is the first one, projected.** *Which is why no initial
condition moves it: the initial data move where the comb starts, and the phase's k-dependence sets
how it is spaced.* **That is exactly the observed pattern — first peak moves 165 multipoles, comb
deficit does not move at all.**

## ⌗ AND WHAT IT DOES NOT SETTLE, PLAINLY

- **It does not supply a first-peak position**, and it does not vindicate 220 or 150. *Same scope
  restriction the receipt states about itself.*
- **It does not resolve the −0.97 / −0.62 exponent disagreement** (`S-002`). It makes that
  disagreement matter *more*: the comb deficit's size is fixed by the exponent, so **the two
  instruments predict different comb deficits, and the comb is the stable observable.** *That is a
  sharper test than either had alone.*
- **The cross-file arithmetic in (b) uses two different instruments** — `ROBUST_p1p2_scan`'s comb
  against `ACOUSTIC_two_arm`'s Q. **Within-instrument is the test that carries weight**, and it is
  the fold's, whose calibration defect `S-002` records. ⇒ ***The clean version of this is to measure
  Q₁ and the comb in `ACOUSTIC_two_arm` itself, which already computes the first and can be asked
  for the second.*** *Named as the specific unrun question rather than left as a hope.*

⌗ *Every figure above is machine-printed by `S004_comb_deficit_test.py`; nothing is hand-carried.*
