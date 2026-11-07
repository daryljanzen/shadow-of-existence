# `r7697` (cc66) — VERDICT, scored against `PREDICTION.md` arm by arm

**Three registered arms. Two confirmed, one confirmed-with-a-reversal-I-registered-in-advance, and
`0` predicted digits wrong — because the one place I would have been wrong is the one place I declined
to predict.**

| arm | registered | measured | verdict |
|---|---|---|---|
| ⚠ the reversal | `l.134`'s ℓ = 4 `0.36 → 0.35` | `0.3536 → 0.35` | ✔ **CONFIRMED** |
| ① which digits move | **6 of 7** at three places, **ℓ = 7** holds | 6 of 7, ℓ = 7 holds, `max diff = 0.0` | ✔ **CONFIRMED** |
| ② sign pattern | ℓ = 2 rewards, ℓ = 3–5 penalise, nothing above | exactly that | ✔ **CONFIRMED** |
| ② the total | ⛔ **declined** | `+1.5847 → +1.7168` | ✔ **RIGHTLY DECLINED** |
| ③ withdrawal, not refinement | DECOUPLED inside `2.9 %` everywhere, octopole small | `2.91 %` worst, octopole `−0.88` | ✔ **CONFIRMED** |

## ⚑ THE ARM THAT MATTERS MOST WAS THE ONE I ADDED BECAUSE `r7693` FAILED

The registration's own correction to `r7693` was: *"These are read off 69's order row, not computed. The
first thing I do is compute them from the two `(L)` banks myself… Here the bank's pairing is the order's
whole subject, so the check is: does `armA_leafpert` carry `(L)`, read from its own config?"*

⇒ It does — `SPLITCLOCK['distances__armA__L'] == 'L'` with `STACKPERT` unset, stated by the bank about
its own run — and that read is now a **gate inside the receipt**, verified in both directions by
failability legs B1 and B2.

⌗ *** `r7693` was not lost because my arithmetic was wrong. It was lost because my premise was, and the
check I ran could not have caught it: I verified my read against the ORDER'S ROW, which is the same
source the premise came from. The arm added this revision reads the BANK. That is the whole difference,
and it is why the registration made it item zero rather than a note. ***

## ⌗ THE DIGIT I DID NOT PREDICT IS THE DIGIT THAT WOULD HAVE CAUGHT ME

**I declined to predict the total on both rows.** On `r7693`'s mixture row it **fell** to `+1.44`; on
arm A `(L)` it **rises** to `+1.72`. ⇒ *The direction of the total's move is row-dependent — four terms
moving with opposite signs — so there was nothing to predict from. **Had I guessed on either row I
would have been right once**, which is the score of a coin.* ⌗ A declined prediction is recorded here as
a result, not as a gap: *the registration said why it was declined, and the measurement says the reason
was correct.*

**Two figures moved that NEITHER order named**: the octopole estimator's low end (`+0.2 → +0.4` — it had
NOT moved on the `r7693` row) and, at `r7693`, two others. ⌗ *A re-point's blast radius is not the set of
figures the order lists; it is the set of figures that read the row. The site sweep is what finds them,
and ② above is why it is run rather than reasoned about.*

## ⛔ WHAT WENT WRONG IN THIS REVISION — four faults, and only one was new

| | fault | class | caught by |
|---|---|---|---|
| 1 | first diagnostic **re-derived** the paper's two-place digits instead of reading them — wrong printed value AND wrong verdict for ℓ = 3 | **a printed digit re-derived, not read** (3rd tonight) | reading the paper; **before any commit** |
| 2 | failability leg B anchored DOWNSTREAM of the pairing gate — reported `0`, tested nothing | **a harness returning a verdict about a run that did not do what I assumed** | reading per-leg targets, not totals |
| 3 | a quote-pin key minted without adjudication in the same pass | **a rule I knew and skipped** (`r7691`'s own rule) | CI |
| 4 | the forward-looking pin's ABSENT-paper-pin consequence unaccounted for | ⚠ **a consequence I should have DERIVED** — new tonight | CI |

⌗ **Fault 2 is the one that nearly cost a wrong verdict in this very file.** *Had I scored the sweep by
totals, the pairing gate — the single assertion that embodies why `r7693` failed — would be recorded
above as VERIFIED while being UNTESTED. The leg now asserts its own aim by line number.*

⌗ **Fault 4 is a different shape from 1–3 and worth separating.** *Faults 1 and 3 are rules I had
written down and did not apply; fault 2 is an instrument I trusted without checking its aim. Fault 4 is
neither: nothing told me, and nothing had to — a forward-looking assertion in this corpus has **two**
bookkeeping consequences (it mints a quote-pin key AND an absent-paper pin) and I accounted for one.*
⇒ **The note that now exists for it is a note about what the corpus DOES, not an instruction to myself** —
which is the form that worked tonight, where two notes telling me what I should do did not.

## ⇒ THE ONE SENTENCE

**The row, the likelihood, the sign pattern and the cross-validation all came out as registered on a
build whose pairing the receipt now reads from the bank rather than from the order — which is the one
arm `r7693` lacked, and the reason this revision's landing is not another one 69 has to hold.**
