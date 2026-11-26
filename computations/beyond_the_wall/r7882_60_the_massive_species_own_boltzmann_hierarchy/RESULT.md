---
kind: RESULT
revision: r7882
node: 60
order: r7879 item ②
---
# r7882+60 — THE MASSIVE SPECIES' OWN BOLTZMANN HIERARCHY: BUILT, CONVERGED, AND READ ON `r7879`'s JOINT BANDS

*`r7879` ruled item ② the REPAIR: "the massive species' own Boltzmann hierarchy, momentum-binned,
in the standard form CAMB itself integrates (Ma & Bertschinger 1995) … No fitted quantity: the
q-grid and ℓ-cutoff are numerical and are converged, not tuned." This is that revision.*

⛔ **NO LIMIT IS READ HERE.** `r7879` puts the limit in item ③, on the closed cross-seeded
envelope, with its own registration. Nothing below is a limit or is offered as one.

---

## ⓵ WHAT WAS BUILT

Per momentum node `q_j`, the moments `Ψ_ℓ(q_j, k, η)` evolve with the mass entering ONLY through
that node's own energy `ε_j(a) = √(q_j² + y(a)²)`, the weight being the background's own
Fermi–Dirac `f₀` — the machinery `r7882`'s predecessor already validated, not a second copy of it.
The two numbers the hierarchy carries, the node count and the ℓ-cutoff, are the NUMERICAL ones the
gates below fix.

**Every source sign is DERIVED, not copied from a convention and hoped to agree.** Each was obtained
by requiring the massless limit to reproduce this instrument's OWN landed lines — the neutrino
continuity, the neutrino Euler equation, and the quadrupole's own equation — and the derivation
reproduces all three exactly, including the `8/15` and `3/5` of the landed quadrupole line. The
registered gate then MEASURES that limit rather than trusting the derivation.

Off is byte-identical, both ways of being off. The landed fluid variables keep evolving on their own
lines and simply stop being what the potential reads, so the two closures can be compared inside one
run. The switch REFUSES to run beside the fluid approximation: two models of one sector, and that
sector has one slot.

---

## ⓶ THE DEFECT THE MASSLESS-LIMIT GATE CAUGHT, WHICH NO SWITCH ARM COULD HAVE

All three switch arms passed — off byte-identical, the fluid approximation bit-identical before and
after the diff, all six refusals refusing — and the hierarchy was still **wrong on the arm every
validation number in this revision is read on.**

`Ⓠ⓸`'s first run reported a worst relative difference of **`4.345e-01`** between the hierarchy on
and off at a sum of `1e-3` and at `1e-4`, flat across the decade. The cause: the seeding sat inside
the CR arm's branch of the initial-condition `if`/`else`, so on `lcdm` the moments started at ZERO
and grew from the sources alone. `δ` was a factor eight short at `e/e_rec = 0.01` and only caught up
by recombination.

⌗ **The arms could not have seen it.** Byte-identical-off says nothing about a seed that only the ON
path reads, and the fluid approximation's bit-identity says nothing about a branch the fluid never
enters. The seed/integral inversion had separately been verified exact AT THE INITIAL TIME — which
was true, and was a fact about the seeding function, not about whether the solver ever received it.

The seeding now sits OUTSIDE the `if`/`else`, where one block serves both arms: both data set the
species' `δ` and `θ` to the same two numbers, so one seeding is correct for each. With it fixed the
hierarchy's `δ` and `θ` track the landed fluid's to `≈ 3e-05` relative from the first sample to
recombination, and the massless-limit difference falls to **`2.4e-05`**.

---

## ⓷ THE GATES, EACH MEASURED

### `Ⓠ⓵` — the quadrature against the background already built: **MET**

`12` Gauss–Legendre nodes on `[0, 20]`, worst `3.052e-05` in `ρ_ν(a)/ρ_ν⁰` and `3.331e-05` in
`w_ν(a)` against the registered `1e-04`, at every decade of `a` from `1e-10` to `1`. The scan also
separates truncation from quadrature error: on `[0, 15]` it SATURATES at `2.2e-04` whatever the node
count. And a third weight the registered gate is silent on — the energy flux's `q³f₀`, which no
background spline carries — is named and measured by self-convergence against a 96-node grid on
`[0, 40]`: `3.050e-05` at the chosen grid.

### `Ⓠ⓸` — the massless limit: **MET**, on two arms, after the criterion's own reach was fixed

With the seeding repaired the residual is `2.335e-05` at `Σ = 1e-3` and `2.446e-05` at `1e-4` —
**flat across the decade**, so `limit.py`'s shrink test still reports the gate as not met.

⛔ **That test is stronger than what was registered, and it is unsatisfiable by construction.** The
registered criterion is agreement *"to the fit's own resolution"*. The shrink test is one reading of
it, and the massless map is inverted by a FINITE quadrature, so the on-against-off comparison
carries the `q`-grid's representation error — which depends on the node count and NOT on the mass. A
mass-independent floor cannot shrink with the mass however correct the physics is, so a shrink test
cannot separate a defect from the floor. `limit.py` keeps its verdict as run; nothing was
overwritten.

Two arms were registered before either was run, and both were measured:

| arm | what it asks | measured | registered | verdict |
|---|---|---|---|---|
| `Ⓠ⓸ᵃ` | is the floor the quadrature's? Double the nodes to `24` | falls `3.5×` at `1e-3`, `3.1×` at `1e-4`; stays flat to `1.05×` and `1.16×` | fall `≥ 3×`, flat to `≤ 2×` | **MET** |
| `Ⓠ⓸ᵇ` | the registered criterion on the quantity the fit reads: does `A` move? | worst `1.161e-03` over both blocks and both limit sums | `< 0.003` | **MET** |

⇒ **At the massless limit nothing the fit reads moves, and the floor under it is the grid's.**

⌗ **`Ⓠ⓸ᵇ`'s reach, stated rather than left implicit.** Its legs sit at `1e-3` and `1e-4` and are
fitted against the CAMB targets of the validation sums, so the arm is a DIFFERENCE at a fixed target
and the target cancels. The `A` values themselves are therefore near zero, not near one, and ⛔ **no
`A` from those legs is a validation number.** The consequence is that the arm measures `A`'s
sensitivity in a regime where the response the fit works on is itself tiny, which is not the
sensitivity at `0.30` and `0.60 eV`. It bounds the move at the limit; it does not transport that
bound to the validation sums, and the convergence gates below are what speak there.

---

## ⓸ THE MEASURED COST, WHICH THE REGISTRATION ASKED FOR AS A RISK

The registration declared the cost a RISK and required a MEASURED number: *"If the validation legs
do not fit in one revision, that is reported as a measured cost and the item is split."*

At the banked resolution, four-way parallel, the state vector growing from `20` to `176` per mode:

| leg | wall |
|---|---|
| hierarchy off, `Σ = 1e-3` | `3175 s` |
| hierarchy off, `Σ = 1e-4` | `3161 s` |
| hierarchy on, `Σ = 1e-3` | `3532 s` |
| hierarchy on, `Σ = 1e-4` | `3537 s` |

⇒ **The hierarchy costs `11.5` per cent more wall time, not a multiple**, although the state vector
is nearly nine times larger. The mode solve is not what dominates a banked leg. **So the validation
legs and both convergence banks fit in this revision and the item does NOT split.**

---

## ⓹ THE LABEL IN ROWS `Ⓓ` AND `Ⓔ` WAS MANY-TO-ONE, AND THE READING WAS FIXED BEFORE THE FIT

Rows `Ⓓ` and `Ⓔ` compare this revision's TT against *"the fluid approximation"*. By the guard on
many-to-one labels, that had to be checked — and it does not name one number. `r7878` measured FIVE
fluid arms, read off its own record:

| arm | `∣A−1∣` in TT at `0.30`, `0.60` | the same in EE |
|---|---|---|
| the weight change alone | **`0.00490`**, **`0.05621`** | `0.04005`, `0.05961` |
| continuity alone | `0.13111`, `0.26394` | `0.01237`, `0.04361` |
| Euler alone | `0.05464`, `0.13902` | `0.00060`, `0.02019` |
| the named subset | `0.08759`, `0.18952` | `0.00769`, `0.03424` |
| all three, exact `c_a²` | `0.07885`, `0.09214` | `0.04650`, `0.07225` |

The full fluid model and the weight change alone differ by a factor sixteen in TT at `0.30 eV`, so a
row read on the former is far easier to pass than the same row read on the latter.

⛔ **The reading fixed, and committed and pushed before any leg of this revision was fitted:** `Ⓓ`
and `Ⓔ` are read against **the fluid family's BEST TT at each sum, whichever arm achieves it** —
`0.00490` at `0.30 eV` and `0.05621` at `0.60 eV`, the weight change alone at both. The hardest
available reading, chosen for that reason: the rows exist to ask whether the hierarchy is a better
model of this sector than the fluid approximation was, and a baseline picked to be beatable would
turn a negative finding into its opposite. ⌗ *Note what that means at `0.30 eV`: the weight change's
TT is ALREADY inside the `0.03` band there, so clearing `Ⓓ` at that sum demands TT within `0.00490`
of one — tighter than the validation band itself.*
