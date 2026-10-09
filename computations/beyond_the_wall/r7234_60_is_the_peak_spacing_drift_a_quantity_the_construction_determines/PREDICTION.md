---
name: r7234-prediction
kind: PREDICTION
job: the expected sign and order of magnitude of the peak-spacing drift, written down BEFORE the derivation
revision: r7234
seat: 60
order: r7221
---

# ⛭ r7234 — PRE-REGISTRATION

`r7221` ordered this and attached its own lesson as the burden: *state the expected sign and order of
magnitude BEFORE you derive it, and report the prediction against the derivation either way.*  This file
is committed before any computation is run.  Nothing below has been measured; it is what I expect and
what would refute me.

## ⌗ THE QUESTION AS I READ IT

Does the construction COMMIT to a drift of the peak spacing in `$\ell$` at a computable size?  Formally:
with the extrema of the acoustic oscillation at `$k r_s + \varphi(k) = n\pi$` and `$\ell = k D_M$`, the gap
is `$\Delta\ell = \pi D_M/(r_s + \varphi'(k))$` and the drift is

    d(Δℓ)/dℓ  =  −π φ''(k) / (r_s + φ'(k))²

so **the whole question is whether the construction fixes the CURVATURE of the acoustic phase
`$\varphi(k)$`**, and at what size.  A constant phase shift contributes nothing; only a `$k$`-dependent
one that is itself changing contributes.

## ⛭⛭ WHAT I PREDICT

**① SIGN: POSITIVE.  The spacing WIDENS with `$\ell$`, and the widening DECAYS at large `$\ell$`.**
*Reason: every `$k$`-dependent phase source in this construction saturates from one side as
`$k\to\infty$` — the entry phase approaches `$x=1/\sqrt3$` from above, the expansion-leg driving near
equality dies off as `$k_{\mathrm{eq}}/k$`, and the Bessel projection's offset falls as `$1/\ell$`.  A
saturating `$\varphi$` is concave, `$\varphi''<0$`, which by the relation above is a POSITIVE drift.*

**② SIZE: of order `$+5$` to `$+15$` in the comb's quadratic coefficient** (`$\ell=\ell_A v + D v^2$`),
equivalently `$d(\Delta\ell)/d\ell \simeq 0.03$`–`$0.10$` near the second peak, equivalently the mean
spacing changing by of order **5–10 per cent across `$150\le\ell\le1600$`**.
*Reason: the gap sequence `r7221` quotes — `$302/270/312/295$`, highs `$+10$`, lows `$+25$` — gives a
local mean rising `$286\to291\to303$`, about `$17$` per step, and a quadratic rising `$2D$` per step puts
`$D\simeq9$`.  My prediction is that the DERIVATION lands in the same decade, not that it lands on `$9$`.*

**③ STRUCTURE: the handover contributes EXACTLY ZERO, and that is the construction's own statement.**
*`Prop.~\ref{prop:subhorizon}` says the collapse leg hands over the frozen adiabatic state and that its
contribution `is an amplitude and not a phase`; `\S\ref{sec:envelope}` says the `$k$`-dependence `rides
entirely in the amplitude at horizon entry and in the decay of `$\Psi$``, that the envelope is FLAT, and
that the free-streaming correction is a CONSTANT phase shift.  **A constant phase has zero curvature.**
So I predict the drift is carried by the two places that are nobody's in particular — the expansion-leg
driving around equality, whose scale the construction fixes parameter-free through
`$1+z_{\mathrm{eq}}=\omega_m/\omega_r$`, and the projection — and NOT by the piece that is this
construction's own.*

**④ SO THE ANSWER I EXPECT IS: YES, DERIVABLE, AND NOT A DISCRIMINATOR.** *Derivable because nothing in
it is fitted; not a discriminator because the two quantities that carry it — equality and `$D_M$` — the
construction shares with flat `$\Lambda$CDM to a couple of per cent.*

## ⛔ WHAT WOULD REFUTE ME, NAMED IN ADVANCE

1. **The derived drift comes out NEGATIVE** — the spacing narrowing with `$\ell$`.  Refuted on sign, and
   the fit's positive `$D$` would then be something other than what I derived.
2. **The derived drift is an order of magnitude or more from the fitted size.**  Refuted on size.  I am
   claiming the same decade, so `$D_{\mathrm{derived}}<1$` or `$>100$` refutes ②.
3. **The drift proves GRID-DEPENDENT** — it moves with the integration grid, the mode sampling or the
   transfer's resolution.  Then `r7221`'s negative branch is the answer, ① and ② are both void, and the
   tight direction is precise and unscoreable.  **This is the outcome I would most dislike and it is the
   one I am testing hardest.**
4. **The handover turns out to carry a `$k$`-dependent phase after all.**  That refutes ③ and is a larger
   result than the drift, because `Prop.~\ref{prop:subhorizon}`'s `an amplitude and not a phase` is load-
   bearing well beyond this row.
5. **The three sources do not add to the fitted drift** — each derivable, their sum short of or past the
   measurement by more than its own `$\sigma$`.  That is a partial refutation: derivable at a size, wrong
   size, and the deficit is then the result.

## ⌈ AND THE THIRD OUTCOME, PRE-REGISTERED BECAUSE NEITHER BRANCH OF THE ORDER NAMES IT

`r7221` framed two branches: derivable at a size, or not derivable and therefore unscoreable.  **There is
a third and I expect it:** *derivable at a size, and the size being one that any construction with this
equality epoch and these distances returns — so it is a genuine parameter-free prediction OF THE SPECTRUM
and simultaneously no test at all OF THE RATE SPLIT.*  If that is what the derivation gives, I will say so
in those words rather than reporting the positive branch and letting the discrimination be assumed.
