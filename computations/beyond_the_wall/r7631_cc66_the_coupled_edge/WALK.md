# `r7631+cc66` ① — the coupled edge, walked

What was registered in `PREDICTION.md` before a line of `edge.py` existed, what the computation
found, and the three things I got wrong on the way — including one the registration had itself
flagged as the error I would most easily make in the flattering direction, and then made anyway.

## The result, in one paragraph

**Finiteness of the quadratic form — equivalently, closure of the minimal form domain — selects
exactly one self-adjoint extension on the coupled tower's sub-threshold subspace, and it is the
diagonal, regular-branch member: the same one Hartle–Hawking regularity imposes.** It does so on every
fibre of `spec Γ̂` below the threshold, with margin. So a principle with **no Euclidean content**
closes the coupled condition, the face is **not** the only closer here, and `PO-94`'s quantum half
does **not** meet its test by this route. **This is the outcome the registration expected, and it is
the one that costs the corpus something.** ⇒ But it rests on **one** selector, not two: positivity
turns out not to select at all.

## The scorecard against the registered prices

| # | question | registered | measured | |
|---|---|---|---|---|
| ① | deficiency a finite-dimensional subspace, extensions ↔ `U(n)`? | **medium-high YES** | **YES** — `n = 3` sampled fibres, index `(3,3)`, `U(3)`, **9** real parameters | ✓ |
| ② | does finite form energy select a unique member? | **high YES** | **YES** — the irregular branch's form integral diverges on every physical fibre | ✓ |
| ③ | is it the member Hartle–Hawking selects — diagonal and regular? | **medium-high YES** | **YES**, and the non-diagonal control confirms it | ✓ |
| ④ | does **positivity** select it independently? | **medium YES** | ⚠ **NO — positivity does not select at all** | ✗ |
| ⑤ | do the ledger or covariance select it? | **low-medium**, expected neither | neither reaches the endpoint; reported as a reading | ✓ |

⚠ **④ is a miss, and it is a miss in the direction the registration had named.** The registration
said: *"If positivity and form-finiteness are the same condition wearing two names, then reporting
them as two non-Euclidean selectors would be double counting one fact, which would overstate the case
against the quantum half."* It priced the risk correctly and then the first draft walked into it —
printing *"positivity therefore also prefers the Friedrichs member"* and merging the two "generously"
into one. The merge **hid** the fault: it produced the right count (one) from a false premise (two
agreeing principles), so the arithmetic looked conservative while the physics was wrong. The true
answer is narrower still: **there is nothing to double-count, because the second candidate does not
select.** Being forewarned was not enough; only the measurement was.

## What positivity actually does

Asked in closed form — the negative-energy solutions are `x^{1/2} I_{±ν}(kx)`, so the eigenvalue
condition is exact and needs no mesh:

> a self-adjoint extension labelled `t = B/A` (the ratio of irregular to regular coefficient) has a
> negative eigenvalue **iff** `t ∈ (−b^{2ν}, 0)`.

So positivity **excludes that band** and **admits** `t = 0` (Friedrichs), **every** `t > 0`, and
**every** `t ≤ −b^{2ν}`. It rules out a band and leaves a continuum. ⇒ **It is a constraint on the
family, not a selector of a member.** The two candidates are therefore *nested*, not independent — a
finite form excludes every `t ≠ 0`, positivity only a band of them — and the row counts **one**
selector because there is only one.

⌗ This **agrees** with the corpus rather than denting it: `CR_framework` l.1987 already lists
positivity among the candidates that fail to select — there, the *ordering*. This row finds it also
fails to select the *boundary condition*. A different freedom, the same verdict.

## The three faults, and how each was caught

**① I swept `Γ = 0` as a fibre, and my own table contradicted the conclusion I drew from it.** The
first run printed *"finite form energy … excludes the irregular one, on every sub-threshold fibre"*
while the table's own first row read, for the irregular branch at `Γ = 0`, form energy `0 → 0`,
labelled `(finite)`. `Γ = 0` is the `ν = 1/2` knife-edge: the irregular branch is a **constant**, and
although its integrand exponent `2s−2 = −2` is non-integrable, its **coefficient** `s² + Γ` vanishes
identically, so the energy is zero. The exponent alone never decided it.

*Caught by:* reading the printed table against the sentence printed underneath it.

*Settled by the corpus, not by prose.* `spec Γ̂ = [γ, ∞)` with floor `γ = 1/4` under normal ordering
(`canonical_time` l.461, `CR_framework` l.1988) — so **`Γ = 0` is not a fibre of the operator at
all**, lying `0.25` below the floor. The physical band is `[1/4, 3/4)`, where the smallest irregular
coefficient is `0.292893 > 0` and the largest irregular exponent is `−2.414214 < −1`: divergence with
margin, and the margin is exactly the distance from this hole. The knife-edge is now carried as
**`CONTROL (6)`** — exhibited, measured, and excluded — rather than quietly dropped. And even there
the selection survives, by the **stronger** criterion of form *closure* rather than form
*finiteness*; on the physical band finiteness already suffices and the two coincide.

⌗ A by-product worth stating: under **symmetric** ordering the floor is `3/4`, which **is** the
threshold, so the sub-threshold band `[3/4, 3/4)` is **empty** and the selection question has no
object. That is the corpus's own *"limit-point from the first occupied mode upward"*, reached here by
arithmetic on its two stated floors. **The question has content under normal ordering.**

**② My positivity instrument was blind, and I read its noise as a result.** I reported Friedrichs
`0.00616853` against `θ = 0.30`'s `0.00616843` and called the difference a preference. With
`eps = 1e-4` and grid spacing `h = 1.7e-3`, the mesh **never sampled the region where the extension
lives**: `h ≫ eps`. The same number came back for every member of the family, the pure irregular one
included, and the differences were arithmetic noise in the stencil.

*Caught by:* sweeping the extension label over the whole family, including `t = ∞`, and getting
**one** value to six figures. A difference in the seventh decimal across a family that includes two
qualitatively different boundary conditions is not a small effect; it is no effect.

*Proof it was blind rather than merely imprecise:* its value `11.7767` is the **exact** Friedrichs
ground state `(j_{ν,1}/b)² = 11.776812` computed later in closed form. It was returning the Dirichlet
answer whatever condition was imposed. ⇒ **A blind instrument does not report an error; it reports a
number.** That is the second time this seat has been caught by that shape — `r7629`'s `grep -E`
reporting "clean" on a pattern it could not match — and the lesson is the same: *verify the instrument
responds to the thing it is supposed to measure before trusting what it says about it.*

**③ Then two more instruments failed, for two more reasons, before I stopped discretising.** A direct
Robin condition is stiff — holding an extension fixed as `eps → 0` needs a coefficient growing like
`1/eps`, and the Friedrichs ground state ran to `−5.98e4`. A log substitution `u = x^{1/2}v(ln x)`
fixes the conditioning of the boundary term but turns the weight into `e^{2y} → 0`, so the mass matrix
goes singular in the tail and spurious modes appear at `−3.6e8`. **Three instruments, three distinct
failures.** Only then did I go to closed form — where modified Bessel functions answer it exactly,
with no mesh to be blind with.

⌗ *The order's question did not require a mesh at any point. I reached for one first because the
row's first selector had been measured by quadrature and I carried the habit across. The cost was
three builds and one published false claim.*

## The controls, and what each would have caught

| control | what it does | would have caught |
|---|---|---|
| **(1)** form integral on **both** branches, two values of `eps` | the divergence is seen **growing**, not asserted from an exponent | a branch whose exponent diverges but whose coefficient vanishes — which is exactly the knife-edge |
| **(2)** the threshold recomputed, `ν = √(Γ+1/4)`, sub-threshold ⟺ `Γ < 3/4` | the fibres are the corpus's | working the wrong operator |
| **(3)** a **super-threshold** fibre | `Γ = 1.00`: deficiency `(0,0)`, `U(0)`, **0** parameters — nothing to select | a "selector" that selects where there is no freedom |
| **(4)** a **non-diagonal** `U(2)` member written down | `det = 1`, `UᵀU = I`: a genuine extension, and it mixes fibres, so it is form-infinite | ③ being a statement about the only member I constructed |
| **(5)** each principle asked **separately** | positivity asked about the **spectrum**, form-finiteness about the **domain** | the double-count — and it did catch it, once the instrument worked |
| **(6)** the knife-edge `ν = 1/2` | the one place the argument fails, exhibited and then excluded by the floor | fault ① — added **because** of it |
| *instrument check* | `j_{0,1}`, `j_{1/2,1} = π`, `j_{1,1}` against known values | a first-zero finder that returns the **third** zero — which it did, giving `9.7373` for `ν = 0.7071`, out by a factor of 8 |
| *box-size sweep* | the band edge at `b = 0.5, 1.0, 2.0` against `−b^{2ν}` | at `b = 1` the law reads `−1` whatever `ν` is, so testing it only there tests **nothing** about the exponent |

## What this row does *not* claim

- It does **not** re-adjudicate `60`'s `r7630` finding or `PO-94`'s quantum half. It answers the
  question the order put to this seat; the bearing on `60`'s row is routed, not assumed.
- It does **not** settle whether the **ledger** or **covariance** reach the endpoint. Neither makes a
  statement about a mode's behaviour as `x → 0`, which is what a boundary condition is — but that is a
  **reading** of what those principles are about, reported as such, and the coordinating seat's ruling
  governs.
- It does **not** touch the **ordering** question. The corpus localises that as a single physical
  datum (whether vacuum energy gravitates), and nothing here bears on it.
- It does **not** claim the selector is Euclidean-free *because* it is a form condition and the form
  looks Lorentzian. The claim is narrower and is the one the order asked for: form-finiteness makes no
  appeal to Euclidean smoothness, a horizon period, or a temperature, and it selects the same member.
