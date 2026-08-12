# F09 — The lift's "factor 2.32" is Γ(1/6)/(√π Γ(2/3)) and is mass-independent; the exponent scales as M^{−1/3}; and C is not bounded by 1.72

*status: OFFERED (two closed forms + one mass scaling) and BOUNDED NEGATIVE (one stated bound is false). No verdict changes.*
*receipt: `DRAFT_P10_the_adiabatic_constants_in_closed_form.py`, rc=0.*
*touches: P10 `eq:adiabatic-exponent` and the paragraph after it; P7 `sec:lift-quantum`; `LIFT_adiabatic_correction.py`.*

---

Same paragraph family as F08, so I kept going through it. Three of the four quoted constants have
closed forms, and the fourth is a bound that doesn't exist.

## ① The exponent, closed, and its mass scaling

With |r| = A sin^{2/3}(3s/2α) and A = (2Mα²)^{1/3}, the substitution u = 3s/2α gives a Beta
integral:

> **∫₀^{πα/3} ds/|r| = (√π/3)·[Γ(1/6)/Γ(2/3)]·(α/2M)^{1/3}**

= 3.338738024 α⁻¹ at the forced member, against P10's quoted 3.3387 and the receipt's quadrature
3.338738024. The **M^{−1/3}** law is read off directly — I·M^{1/3} is constant to six figures
across a factor of ten in mass.

Worth putting beside F08: the gravitational action goes as **+M**, the suppression exponent as
**M^{−1/3}**. The two mass dependences run opposite ways, and neither is stated. A lighter
progenitor gives a *longer* exponent and so a *stronger* Euclidean filter.

## ② The factor 2.32 is a pure number — A cancels

> **ratio = 2B/π = Γ(1/6)/(√π Γ(2/3)) = 3Γ(1/3)³/(2^{4/3}π²) = 2.319190534…**

| M | A | I | I_naive | ratio |
|---|---|---|---|---|
| 0.02000 | 0.341995 | 7.101418 | 3.062024 | **2.319190534** |
| 0.10000 | 0.584804 | 4.152934 | 1.790683 | **2.319190534** |
| 0.19245 | 0.727416 | 3.338738 | 1.439614 | **2.319190534** |
| 0.19000 | 0.724316 | 3.353028 | 1.445775 | **2.319190534** |

Identical to nine figures across a factor of ten in mass. **It is a property of the 2/3 exponent —
of the cube-root branch point — and of nothing else.** P10 attaches "2.32" to a sentence ending
*"on the forced member"*; it holds on every member, which is the stronger statement.

## ③ C is not bounded by 1.72

The parameter is exactly `|dω/ds|/ω² = C(s)/μ_n` with
**C(s) = |d|r|/ds| = (A/α)·cos(u)·sin^{−1/3}(u)**, u = 3s/2α.

| s | C(s) | |
|---|---|---|
| 10⁻⁶ | **63.55** | branch-point end |
| 10⁻⁴ | 13.69 | |
| 10⁻² | 2.95 | |
| 0.05 | **1.7206** | *the receipt's first sample* |
| 0.90 | **0.1606** | *the receipt's last sample* |
| πα/3 | **0.0000** | turnaround end |

C diverges as s→0 like (3s/2α)^{−1/3} and vanishes exactly at the turnaround. So P10's *"C running
from 1.72 near the branch point to 0.16 near the turnaround"* is the value at the **first and last
sampled points** of `LIFT_adiabatic_correction`'s four-point table — 4.8% and 86% along the
segment — not the behaviour at the ends. And **P7's "C ≤ 1.72" is a bound that does not hold**: for
every mode there is a neighbourhood of the branch point where the adiabatic treatment is out of
control.

## ④ And the conclusion survives, with a better argument

What matters is not sup C but *how much of the segment* is non-adiabatic. C(s)/μ_n = 1 at
s* = (2α/3)(A/μ_nα)³, and (A/α)³ = 2M/α, so

> **s*/s_max = (2/π)·(2M/α)/μ_n³** — exact.

| n | μ_n² = n(n+2)−2 | 1.72/μ_n | s*/s_max |
|---|---|---|---|
| 2 | 6 | 0.702 | **1.67 %** |
| 3 | 13 | 0.477 | 0.52 % |
| 10 | 118 | 0.158 | 0.019 % |
| 20 | 438 | 0.082 | 0.0027 % |

So even at n = 2 — the coarsest harmonic on S³, there being none below it — the out-of-control
region is **1.7% of the lift**, falling as **μ_n^{−3}**.

That is P10's own conclusion, reached without reading a supremum off a four-point table, and it
carries two things the table cannot: the μ_n^{−3} law, and a linear dependence on the
construction's own dimensionless mass 2M/α — **a heavier progenitor is proportionally less
adiabatic**.

**The paper's verdict gets stronger, not weaker.** The sentence that needs changing is the one
describing C; the sentence drawing the conclusion is right.

## Recommended, stated for reversal

1. P10 `eq:adiabatic-exponent`: give the closed form and the number as its evaluation, and say the
   exponent goes as M^{−1/3}.
2. P10: state 2.32 as Γ(1/6)/(√π Γ(2/3)) and note it is **independent of M and α** — currently it
   sits inside a "on the forced member" sentence that understates it.
3. P10: replace *"C running from 1.72 near the branch point to 0.16 near the turnaround"* with the
   true behaviour (C → ∞ at the branch point, → 0 at the turnaround) **and** the window law
   s*/s_max = (2/π)(2M/α)/μ_n³, which is what the conclusion should rest on.
4. P7 `sec:lift-quantum`: **"C ≤ 1.72" must go** — it is the only place the claim is stated as a
   bound, and P10's own wording is already more careful.
5. `LIFT_adiabatic_correction.py`: sample below s = 0.05 (or plot C on a log axis) so the table
   shows the divergence rather than hiding it behind its first sample point.

## Not claimed

- No verdict changes. *"Adiabatic for all but the lowest few harmonics"* stands; 0.70 / 0.48 / 0.16
  at n = 2 / 3 / 10 are consistent with C = 1.72 and are reproduced.
- No claim about the quantum status of the lift, which P10 is explicit is **not** established.
- No claim that C's divergence damages anything downstream — ④ is the argument that it does not.
  What it damages is one sentence in each of two papers.
- No closure on any registered item.
