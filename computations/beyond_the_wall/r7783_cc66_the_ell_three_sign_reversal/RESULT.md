# `r7783+cc66` item ④ — THE ℓ = 3 REVERSAL IS THE **LADDER'S**, AND THE SIGN IS SET BY THE **FLOOR**

**5 of 5 rows hold** (`ladder.py`, `rc=0`). Every registered row held on the first run.

## The answer to what the projection does to a discrete source

**It slides a fixed ladder across the transfer — and the sign of each multipole's response is set by
the hard lowest mode.**

The depth is the $L=2$-floored Riemann sum, step ${\rm d}L = 1$, of the very integral it is divided
by: $w_L = (L+1)/(L(L+2))$ is exactly ${\rm d}\ln k_L/{\rm d}L$, as the producer's own docstring says.
The ladder $k_L = \sqrt{L(L+2)}/r_0$ **carries no projection distance**. The distance enters only
through $\Delta_\ell(k)$'s $j_\ell(k\chi)$ — so moving the distance acts on the sum the way moving the
ladder does.

**Moving $r_0$ alone, at fixed transfer, reproduces the measured sign at every multipole tested:**

| $\ell$ | measured move (per cent) | $-\partial\ln({\rm depth})/\partial\ln r_0$ | sign |
|---|---|---|---|
| 2 | $-1.430$ | $-1.494$ | ✔ |
| **3** | $\mathbf{+1.547}$ | $\mathbf{+2.173}$ | **✔** |
| 4 | $-1.333$ | $-3.872$ | ✔ |
| 5 | $-1.976$ | $-2.829$ | ✔ |
| 6 | $-0.738$ | $-0.755$ | ✔ |

**Five of five, the $\ell = 3$ reversal included.** *So the reversal is not in the dynamics and not in
the clock: it is the ladder's.*

**And the magnitudes come out of order unity too** — the ladder-only prediction against the measured
sensitivity is $0.52$, $0.70$, $1.45$, $0.71$ at $\ell = 2\dots5$. I registered a *loose* factor $3$
on purpose, because $\Delta_\ell$ is an integral over the source and a global $\chi$ change is a pure
$k$-stretch only in the sharp-visibility limit; the worst ratio is $1.45$. **So "sliding the ladder"
carries most of the size as well as all of the sign.**

## And the sign is the FLOOR's, which is what makes it a statement about discreteness

Euler–Maclaurin puts a step-1 sum's leading departure from its integral at the endpoints; the upper
end is dead and the lower end is the **hard floor at $L = 2$**.

| $\ell$ | $\partial({\rm depth})/\partial\ln r_0$ | the $L=2$ term alone | same sign |
|---|---|---|---|
| 2 | $+0.706$ | $+0.661$ | ✔ |
| 3 | $-0.891$ | $-1.144$ | ✔ |
| 4 | $+1.378$ | $+0.194$ | ✔ |
| 5 | $+1.912$ | $+2.636$ | ✔ |

**Four of four.** At $\ell = 2, 3, 5$ the floor term carries most of the magnitude as well; at
$\ell = 4$ it carries the sign but only a seventh of the size, so the interior of the sum does the rest
there. ⛭ **The mechanism in one sentence: the projection moves where the fixed ladder samples the
transfer, and because the ladder is floored at $L = 2$ the depth's response at each $\ell$ follows
that one mode — so the $\ell = 3$ reversal is commensurability between the floor and the $\ell = 3$
kernel.**

## What is not claimed

 * **Not that the reversal is observable.** No significance, no likelihood, no new figure.
 * **Not that the floor explains the size** — it explains the **sign** at four of four, and at
   $\ell = 4$ it is a seventh of the magnitude.
 * **Not a CR-arm measurement.** The vehicle is the producer's own control configuration
   ($H_0 = 67.4$, $r_0 = 5064$); the structural claim — the ladder carries no distance, the weight is
   ${\rm d}\ln k_L/{\rm d}L$, the floor is hard — is configuration-independent, and that is stated
   rather than quietly relied on. The measured column is HIER's CR arm through a real `LEAFGEOM`
   change, so the comparison crosses two instruments by construction; **that is exactly why R3's bound
   was registered loose**, and the agreement is better than the bound.
