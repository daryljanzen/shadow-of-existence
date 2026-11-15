# `r7783+cc66` — REGISTRATION ONLY: chasing the ℓ = 3 sign reversal, item ④ of `r7783`

**Registered before any transfer is computed.** What is read at registration time is the *structure*
of the depth — the formulas in `computations/perturbation_verify/verify_lowell_boltzmann.py` — and the
already-published depth moves of `r7779+cc66.2`. No new number has been computed.

## What is to be explained

`r7779+cc66.2` measured the low-ℓ depths' move between the two clocks and found the sign **alternates**:
at the arm-B frozen pair, $\ell = 2$ falls $1.43\,\%$, $\ell = 3$ **rises** $1.55\,\%$, $\ell = 4$ falls
$1.33\,\%$, $\ell = 5$ falls $1.98\,\%$. I reported the $\ell = 3$ reversal as **unexplained** and
declined to assert a mechanism; 69's order ④ asks me to chase it, because *"a mechanism for it says
what the projection does to a discrete source"*.

## The structure the explanation has to come from

The deficit's own producer defines it exactly:

$$C_\ell^{\rm CR} = \sum_{L \ge 2} w_L \left(\tfrac{k_L}{k_{\rm piv}}\right)^{n_s-1}
|\Delta_\ell(k_L)|^2, \qquad
C_\ell^{\Lambda{\rm CDM}} = \int {\rm d}\ln k \left(\tfrac{k}{k_{\rm piv}}\right)^{n_s-1}
|\Delta_\ell(k)|^2$$

with $k_L = \sqrt{L(L+2)}/r_0$ and $w_L = (L+1)/(L(L+2))$, **which is exactly ${\rm d}\ln k_L/{\rm d}L$**.
So the depth is the **$L=2$-floored Riemann sum, step ${\rm d}L = 1$, of the very integral it is
divided by** — the producer says so in its own docstring.

**Two things follow, and they are the whole of the hypothesis:**

 1. **The ladder is fixed by $r_0$ and by nothing else.** The projection distance does not appear in
    $k_L$. It enters only through $\Delta_\ell(k)$, which carries $j_\ell(k\chi)$.
 2. **So, to the extent that changing $\chi$ acts on $\Delta_\ell$ as a stretch in $k$, moving the
    distance is the same operation as moving the ladder** — and the depth's response to the
    projection should be reproducible by changing $r_0$ alone, with the opposite sign.

⛔ **That equivalence is APPROXIMATE and the registration says so before testing it.**
$\Delta_\ell(k) = \int S(k,\eta)\, j_\ell(k(\eta_0-\eta))\,{\rm d}\eta$ is not $S(k)\,j_\ell(k\chi)$:
a global change of $\chi$ is a pure $k$-stretch only in the sharp-visibility limit. **The size of the
mismatch is the measurement, not an embarrassment** — it is how much of the projection's effect on a
discrete source is "sliding the ladder" and how much is not.

## The rows

### R1 — the ladder's own sensitivity, computed exactly from one transfer

**PREDICT** $\partial \ln({\rm depth})/\partial \ln r_0$ at fixed transfer is computable from a single
CAMB run, and is **non-zero and ℓ-dependent**, with the $\ell = 2 \dots 5$ signs
$(+,-,+,+)$ — i.e. the mirror of the measured depth moves under the distance, since a distance
*decrease* should act like an $r_0$ *increase*. **FAILS IF** any of those four signs is wrong.

### R2 — and it reproduces the measured reversal at ℓ = 3

**PREDICT** the sign of $-\partial \ln({\rm depth})/\partial \ln r_0$ agrees with the sign of the
banked depth move at **every** $\ell = 2 \dots 6$, the $\ell = 3$ reversal included. *That is the
mechanism claim: the reversal is the ladder's, not the dynamics'.*
**FAILS IF** the signs disagree at any $\ell \le 6$, which would mean the reversal is not a
commensurability effect and I report that instead.

### R3 — and it reproduces the SIZE to within the stretch approximation

**PREDICT** $|{-\partial \ln({\rm depth})}/{\partial \ln r_0}|$ is within a factor $3$ of the measured
$|\Delta \ln({\rm depth})/\Delta \ln D_M|$ at every $\ell = 2 \dots 5$ — a loose bound, registered
loose on purpose, because the two differ by the non-stretch part of the $\chi$ dependence and by the
instruments (CAMB's control transfer here against HIER's CR arm there). **FAILS IF** any ℓ is outside
it. *A factor-3 agreement across four multipoles with four signs right is the claim; a tighter one is
not available from a control transfer and is not asserted.*

### R4 — and the sign is set by the FLOOR, which is what makes it a statement about a discrete source

Euler–Maclaurin for a step-1 sum against its integral puts the leading correction at the **endpoints**;
here the upper end is dead (the transfer falls away) and the lower end is the hard floor at $L = 2$.

**PREDICT** the sign of $\partial({\rm depth})/\partial \ln r_0$ at each $\ell = 2 \dots 5$ equals the
sign of the floor term's own derivative — computed as the $L=2$ term's change alone, with every
$L \ge 3$ term held — at **at least three of the four**. **FAILS IF** fewer than three agree, in which
case the floor is not what sets the sign and the mechanism is the interior of the sum.

### R5 — what will NOT be claimed

No claim that the reversal is observable; no significance; no new figure for the paper. If R2 holds
and R4 does not, the honest report is *"it is the ladder, and not the floor"*, and I will say that
rather than reach for a story. ⛭ And the vehicle is this producer's own control configuration
($H_0 = 67.4$, $r_0 = 5064$), **not** the CR arm's point — the structural claim is
configuration-independent, and that is stated rather than quietly relied on.

## Failability

R1–R4 move under the transfer, the ladder's definition, the weight $w_L$, or the banked depths.
