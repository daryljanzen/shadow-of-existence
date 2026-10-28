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

---

# `r7631+cc66` ② — `PO-89`'s cutoff, walked

What `PREDICTION_part2.md` registered at `82b7d4e2e` before any search of the corpus was run, what the
search found, and the one crash that turned out to be the most informative thing in the row.

## The result, in one paragraph

**The lowest energy at which the corpus uses the interacting tower is `ω₂ = √8/a ≈ 4.07e−33` eV — about
`33.3` orders of magnitude below `PO-89`'s `8.345` eV threshold. So the order's firing condition is
MISSED and `PO-89` does not close as a stated limit by this route.** That is what the registration
expected. ⇒ **But the search turned up something sharper than the expectation, and it changes what the
answer means: the construction's regulator is a SPECTRAL ZETA, not a cutoff.** Its stated values are
pure numbers (`ζ(0) = 10` exactly, the logarithmic coefficient `15/4`, the interacting sum returning the
rational `−4/3`), and the scale factor factors out of the sum identically. **So the construction has no
cutoff parameter for the exit to be about.** The exit is not merely unsatisfied — *it is not addressable
from inside the construction as it stands.*

## The registered test, and why its asymmetry had to be written down first

| what the search finds | what follows |
|---|---|
| the **lowest** use lies **above** `8.345` eV | every use is above it → the cutoff is certainly above it → **the exit fires** |
| the lowest use lies **below** `8.345` eV | ⚠ **nothing follows about the cutoff either way** — a low-energy use does not cap the cutoff, it merely fails to establish a floor for it |

⚠ *"The corpus uses the tower below `8.345` eV"* is **not** *"the cutoff lies below `8.345` eV"*. A
construction can use a tower at the Hubble scale and still carry a Planck-scale cutoff. Registering that
before searching is what kept the low answer from being reported as evidence against the exit — which
would have been the flattering direction for a row that had just closed one exit in part ①.

## What the corpus actually says, located

| statement | where |
|---|---|
| harmonics with Laplace eigenvalues `n(n+2)−2`, `n ≥ 2` | `canonical_time` l.439 |
| `μ_n² = n(n+2)`, `n ≥ 2` | l.389 |
| equivalently `μ² = m²−1` on labels `m = n+1 ≥ 3`, degeneracy `d = 2(m²−4)` | l.488 |
| the **physical** frequency is `ω_n = μ_n/a` | l.373 |
| **the regulator is "the spectral sum over the tower's own frequencies"**, settled **"by exhibiting the continuation rather than by an estimate"** | l.1081–1082 |
| the continuation returns the exact rational `−4/3`; its simple pole sits at label `1`, **outside** a tower beginning at `3` | l.1084, l.1090 |
| `ζ(0) = 10` **exactly**, "a functional of the degeneracy alone"; the logarithmic coefficient `15/4`, "which **a hard cutoff carrying no zeta function** reproduces" | l.489–493 |
| **"the scale factor does not enter it"** — `a` factors out of the sum identically | l.493 |
| the open frontier is the **completion** of the ultraviolet definition of the mode sums | l.144, l.461 |

⌗ *The decisive line is l.493's parenthesis. A hard cutoff appears in the corpus only as a **foil** — the
thing that, "carrying no zeta function", would reproduce one of these coefficients. The construction's
own regulator is the zeta. So `Λ` is not a parameter of it.*

## Both values reproduced, so this is a reading of what the regulator computes

Not quoted — derived from the spectrum:

- `d·μ = 2(m²−4)√(m²−1) = 2m³ − 9m + (15/4)m⁻¹ + (7/8)m⁻³ + (27/64)m⁻⁵ + …` ⇒ the `1/m` coefficient is
  **exactly `15/4`**, the corpus's logarithmic coefficient.
- `ζ(0) = 2[ζ_H(−2,3) − 4ζ_H(0,3)] = 2[(−5) − 4(−5/2)] = ` **`10` exactly**, the corpus's value, and a
  functional of the degeneracy alone exactly as it says.

⌗ *Both are shown **failable** by perturbing the spectrum they come from: with degeneracy `2(m²−5)`
instead of `2(m²−4)` the coefficient becomes `19/4` and the zeta becomes `15`. Neither is an identity
that would hold for any tower.*

## ⚠ The crash that was the best measurement in the row

Control 2 asked the opposite direction: is there *any* usage above the threshold? I wrote it as a loop,
`for n in range(N_MIN, 10**7)`, and it returned `None` — then crashed the row on `None + 2`.

**The crash was the useful part.** The label needed is `n = −1 + √(1 + (Λ*a)²) ≈ 5.795e33`. A search
bounded at `10⁷` was not a near miss; it was **the wrong kind of instrument** by twenty-six orders of
magnitude. Solved in closed form instead — and the number is worth having: **the construction's own tower
runs across ~34 decades of label before any single mode's energy reaches `PO-89`'s figure.**

⌗ *A loop that cannot reach its target returns nothing and says nothing about why. This is the third
instrument fault of this revision and the third of a different kind — part ① had a blind mesh and a
guessed Bessel bracket; this one had a search bounded below its answer. **All three were caught by the
instrument's own output being impossible rather than merely wrong**, which is the only reason they were
caught at all.*

## And that unbounded label range does *not* fire the exit

This is the reading most easily got wrong in the row's favour, so it is stated flatly: **a
zeta-regularised sum whose terms run to infinite label is not a claim that the theory is valid up to
infinite energy.** The analytic continuation is precisely the device that avoids committing to a cutoff,
and the corpus calls it a continuation and **not a truncation** (l.1081, l.1088). A summand evaluated at
a label is not an effective theory asserted at an energy.

⇒ **So neither direction establishes a cutoff.** The lowest use is 33 orders below the threshold; the
unbounded label range belongs to a continuation that introduces no cutoff at all.

## What would bound the cutoff — the three registered candidates, answered

| # | candidate | verdict |
|---|---|---|
| ⓵ | **the regulator's own scale** | **there is none.** A spectral continuation has no cutoff; its two stated values are the pure numbers above and its result is a rational |
| ⓶ | **the counterterm scales** | a counterterm's **coefficient** is not a scale, and the corpus's are all pure numbers — the quartic's leading constant from the propagating-component count, the logarithmic `15/4`, a Weyl-squared coefficient twice a real scalar's. ⇒ **They bound nothing by themselves, exactly as registered** |
| ⓷ | **the single-scale ledger** | it makes the constants unit gauges over **one** scale, but `r7627` established the construction fixes **no absolute scale**. ⇒ So it gives a **relation** among scales, not a value. **It permits a cutoff; it does not bound it** |

⇒ **Nothing the construction currently contains bounds the cutoff — and the reason is sharper than
`r7627`'s "no absolute scale": the cutoff is not an unmeasured parameter of the construction, it is not a
parameter of it at all.** Its ultraviolet definition is a continuation, and a continuation has no `Λ` to
be large or small.

**What *would* bound it, stated as the corpus's own open item rather than invented:** the corpus names
*"the **completion** of the ultraviolet definition of the mode sums"* as its open frontier (l.144, l.461).
**That is where a cutoff would enter if it entered anywhere.** A completion that regulates by
**truncation** rather than by **continuation** would carry a `Λ`, and only then is `PO-89`'s exit
decidable. Until then there is nothing to compare to `8.345` eV.

⌗ **I do not name the Planck scale.** The construction does not supply it either, and reaching for it
would be inventing the datum the exit needs — which the registration named as the error to avoid here.

## One more fault, caught by a gate rather than by me

The receipt's `Ⓗ` group first ran **five `literal in canonical_time.tex` presence tests** to locate the
corpus's statements. `check_quote_pins` went from its baseline `2744` keys to **`2749`** — five new pins
minted on another seat's sentences, which this seat does not adjudicate. **That is the `r7627` fault
exactly**, and it is the hollow kind twice over: asserting that a paper *contains a string* is not
asserting that the construction *does* anything.

⇒ Repaired the way `r7627` was: the presence tests are **gone**, the located quotations stay in
`cutoff.py`'s output and in this walk — where they are evidence for a reader rather than a minted pin —
and what the receipt gates is the **substance**, which `Ⓒ` and `Ⓓ` already measure. Back to `2744`.

⌗ *Also caught in passing: `Ⓘ②` was first written ending `nsimplify(_log_coeff + Rational(1,1000)) !=
Rational(15,4)` — constant arithmetic that holds for every operator in the world, the same hollow shape
as part ①'s first `Ⓘ②`. **Twice in one revision.** It now perturbs the spectrum instead.*

## What this row does *not* claim

- It does **not** claim the cutoff is low. It claims there is no cutoff in the construction to be high or
  low, and that the exit's condition is therefore not addressable from inside it.
- It does **not** claim the tower is only ever used at low energy — the sum's terms reach far above the
  threshold, at a label of order `10³⁴`, and the row says so.
- It does **not** supply a value for `a`. `1/a` is a declared cosmological input of order `H₀`, varied
  across a decade, and the conclusion is reported in orders of magnitude because `r7627` established the
  construction fixes no absolute scale.
- It does **not** rule on whether the open frontier *should* be completed by truncation. That is the
  coordinating seat's call; this row only says that is where a `Λ` would have to come from.
