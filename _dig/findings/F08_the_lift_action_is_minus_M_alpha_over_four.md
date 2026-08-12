# F08 — The lift's Euclidean gravitational action is **S_E = −Mα/4G** exactly, so it is linear in the progenitor mass and its integral has no singularity to regularise

*status: OFFERED (closed form for a quantity the corpus evaluates numerically) + one one-line labelling slip in a sibling receipt.*
*receipt: `DRAFT_P10_the_lift_action_in_closed_form.py`, rc=0.*
*touches: P10 `sec:deparam` eq:grav-action; P7 `sec:lift-quantum`; `LIFT_gravitational_action.py`, `LIFT_instanton_action.py`.*

---

## What the corpus has

P10 derives the reduced action on the lift and reports:

> *The integral converges rapidly and gives* **S_E^grav = −0.0481 α²/G** *on the forced member.*

`LIFT_gravitational_action.py` evaluates it by quadrature from three lower cutoffs (10⁻⁴, 10⁻⁶,
10⁻⁸) and returns −0.048113. P7 quotes the same number.

## The integrand collapses

On the lift r(s) = −A|sin(3s/2α)|^{2/3} with A = (2Mα²)^{1/3}, so r³ = −2Mα² sin², and

> **r(f − 1) = −2M − r³/α² = −2M(1 − sin²) = −2M cos²(3s/2α).**

A pure cosine-squared. Verified symbolically — sympy returns `-2*M*cos(3*s/(2*alpha))**2` and the
residual against that target is exactly 0. Over the segment's full extent [0, πα/3] that is a
**quarter period**:

∫ = −2M·(2α/3)·(π/4) = −Mπα/3, and **S_E = (3/4π)(−Mπα/3) = −Mα/4** (G = 1).

The π cancels — the quarter-period of cos² supplies π/4 and the prefactor 3/4π removes it — which
is why the answer comes out rational in M and α. At the forced member M = α/(3√3):

> **S_E = −α²/(12√3 G) = −0.048112522 α²/G**

matching the receipt's quadrature to every digit it prints.

## Three things the number cannot carry

**① The action is linear in the progenitor mass.** P10 says *"on the forced member"* and is right
to; nothing is misstated. But a reader wanting the lift's weight for any *other* progenitor has to
redo the quadrature, and `S_E = −Mα/4G` gives it in one symbol. **The beginning's Euclidean weight
is proportional to the mass of the hole it came through** — which is a statement about the
cosmogenesis account, not just about an integral.

**② There is no endpoint singularity, so the cutoff ladder is measuring nothing.** Near s = 0,
r ~ s^{2/3} and (f−1) ~ s^{−2/3}; the product is −2M cos², bounded and smooth on the *closed*
segment, reaching exactly −2M at the branch-point end. The cutoff study is truncating a regular
integral, and I can give the missing piece in closed form: **(3/4π)·2M·ε**, linear in ε.

| lower cutoff | quadrature | closed form | shortfall | predicted (3/4π)·2M·ε |
|---|---|---|---|---|
| 10⁻⁴ | −0.048103334 | −0.048112522 | 9.19e−06 | **9.19e−06** |
| 10⁻⁶ | −0.048112431 | −0.048112522 | 9.19e−08 | **9.19e−08** |
| 10⁻⁸ | −0.048112522 | −0.048112522 | 9.19e−10 | **9.19e−10** |
| none | −0.048112522 | −0.048112522 | 6.9e−18 | 0 |

Exact at every ε. So *"converges rapidly"* understates the result — **it does not converge rapidly,
it closes.**

**③ The Hartle–Hawking comparison becomes exact, and mass-dependent.** P10 compares to the
no-boundary de Sitter action, gives it as −α²/8G in its convention, and says the lift's value is
*"the same sign and the same order, smaller by a factor of order two."* With the closed form:

> **S_E^lift / S_E^dS = (Mα/4)/(α²/8) = 2M/α**, exactly.

At the forced member 2M/α = 2/(3√3) = 0.3849 — smaller by a factor **α/2M = 3√3/2 = 2.598**, not
"of order two". And the factor is not a constant: it is the construction's own dimensionless mass
**2M/α**, the same combination the horizon cubic runs on. *(This takes P10's −α²/8G at its word; it
is a statement about the ratio, not an independent check of that value in that convention.)*

## And one labelling slip

`LIFT_instanton_action.py` prints:

> `lift: s in (0, pi a/3];  r(0)= -A = -0.727416 (turnaround) -> r(pi a/3)=0 (branch point)`

while its own `r_of` gives **r(0) = 0** and **r(πa/3) = −A**. The endpoints are swapped in the
sentence, and the table printed two lines below already shows the correct behaviour (|r| grows
with s).

Nothing computed is affected — the action is an integral over the segment and is
orientation-independent, and P10 traces the **sign** to the segment lying on the r < 0 branch
rather than to a direction of travel, which is correct either way. It is a one-line fix in a
receipt whose own table refutes it. Worth noting that this is precisely the class F07's fingerprint
baseline *cannot* catch: it is prose, and the numbers are right.

## Recommended, stated for reversal

1. Replace *"The integral converges rapidly and gives −0.0481 α²/G on the forced member"* with the
   closed form and the number as its evaluation: **S_E^grav = −Mα/4G, which on the forced member
   is −α²/(12√3 G) = −0.0481 α²/G.** Two extra symbols, and the mass scaling comes free.
2. In `LIFT_gravitational_action.py`, replace the cutoff ladder with the identity
   r(f−1) = −2M cos²(3s/2α) and the exact result; keep one quadrature line as the control.
3. Fix the swapped endpoints in `LIFT_instanton_action.py`'s opening line.
4. Optionally sharpen *"smaller by a factor of order two"* to *"smaller by α/2M, which at the
   forced member is 3√3/2 ≈ 2.6"* — the mass-dependence is the informative half.

## Not claimed

- No new physics. This is P10 `eq:grav-action`'s own integral, done in closed form.
- No claim that −0.0481 is wrong; it is exactly −1/(12√3) and is correctly attached to the forced
  member.
- No independent check of the −α²/8G de Sitter value in P10's convention.
- Nothing about the quantum status of the lift, which P10 is explicit is **not** established, nor
  about the adiabatic correction, which is a separate receipt.
- No closure on any registered item.
