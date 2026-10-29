# `r7635+71.1` — PRE-REGISTRATION: campaign 71, `r7635` ①, corner-cutting for Lipschitz causal curves (equivalently the generators' C² regularity), via local null geodesics. ⌗ `1200` new lines in one probe (band 400–3500 new), ⛔ stop `5000` total. ⌗ p: local geodesics + their C¹ dependence `0.55`, "a causal curve in a small ball between `p` and `q` that is not the null geodesic gives `p ≪ q`" `0.25`, generators are null geodesics `0.15`

*Under `r7635` ①. The setting combines two earlier probes: campaign 70's `CornerCutting.lean` (one chart, a C¹ metric,
Christoffel symbols) and campaign 62's flow machinery from `FlowC1.lean`, for C¹ dependence of ODE solutions. No Lean
was written before this registration.*

## The chosen route, by price

The alternative is to make the generators C² first, then apply campaign 70. That is the harder of the two, because
the regularity is a *consequence* of the geodesic property. The registered route proves the geodesic property for
Lipschitz curves directly.

## ① Local geodesics (`probes/LipschitzCornerCutting.lean`)

***What is built.***
- The geodesic equation `γ″ = −Γ(γ′,γ′)` as a first-order ODE on `V × V`.
- Its local solutions, via Picard–Lindelöf, given a C¹ metric with Christoffel symbols C⁰; or a C² metric with
  Christoffel symbols C¹, if the C¹ dependence needs it.
- The C¹ dependence of the solutions on initial data, from campaign 62.
- The exponential map `exp_x(v)` near `0`, together with `D exp_x(0) = id`.

## ② The local maximality lemma

***Statement.***
- In a small ball `B`, let a Lipschitz causal curve run from `p` to `q`.
- If `q` is not on the null geodesic from `p`, then `p ≪ q`.
- Equivalently: the boundary of `J⁺(p) ∩ B` is ruled by null geodesics from `p`.

***Route.*** A Gauss-lemma-type argument on the position-vector field `P = exp_p⁻¹`. `g(P,P)` is a local time-type
function whose gradient is timelike inside the light cone. A causal curve along which `g(P,P)` stays zero must
follow a null geodesic.

## ③ The consequence for generators

***Statement.*** An achronal Lipschitz causal curve is, after reparametrisation, a null geodesic, locally and hence
globally.

***On the way.*** The gluing of an inextendible generator's θ-parametrised pieces, as `r7635` allows if needed.

***Failable:*** each piece is BUILT, BUILT IN PART, or REPORTED.

***Reachable negative:*** `②` is the classical hard step, the Gauss lemma in Lorentzian signature. Its likely stop is
the Gauss lemma itself, `g(D exp_p(v) v, D exp_p(v) w) = g(v,w)`. That needs the second variation, or the ODE of the
Jacobi field. If it stops, RESULT names it, and `①` stands alone.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
