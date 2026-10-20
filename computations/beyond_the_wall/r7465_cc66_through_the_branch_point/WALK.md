---
kind: WALK
row: PO-88
step: the discharge — stress-energy carried THROUGH the branch point
revision: r7465+cc66.10
---

# `PO-88` — the crossing is an **involution**, so the transmitted datum is the whole approach

*Every identity is proved symbolically in `through.py` (output `through_out.txt`) and re-proved with
controls in `receipts/P16_cosmogenesis_paper/P16_the_crossing_is_an_involution_and_the_density_is_even_on_the_unsigned_radius.py`
— **17 gates, all pass, 0.9 s, six of them controls.***

## The question the last revision left

`r7465+cc66.5` fixed the depth and the clock — the regulated peak is $\rho_{\rm Planck}/6\pi$, and the
approach from the horizon to the branch point lasts **4.364 Gyr** of proper time — and integrated no flow.
So the approach has freedom. **Does any of it reach the other side, and in what form?** Three exclusive
answers: a bijection, a filter, or undefined.

## ⒜ The two continuations agree — and they agree on **odd**, which the price got wrong

The corpus carries two, and I had not established they agree:

- **`P3` §`sec:lap`**, the arc-length picture: $r=\alpha\sin\theta$, riding *through $r=0$ and out onto the
  negative branch*. Under $\theta\to-\theta$, $r$ is **odd**.
- **`P2`/`P16`**, the bead law: $r^3=2M\alpha^2\sinh^2(3\tilde\tau/2\alpha)$. Under a **reflection**
  $\tilde\tau\to-\tilde\tau$ this is **even** — ⛔ *but that reflection never leaves the forward branch*,
  because the set of real $\tilde\tau$ with $r^3<0$ is empty. It is the same leg run backwards.
  Under the continuation `P2` actually uses — the imaginary offset at the conjugate critical point —
  $r^3\to-2M\alpha^2\cosh^2(3\tilde\tau/2\alpha)$, equal to $-2M\alpha^2$ at the critical point itself.
  **Negative.**

⇒ **Both carry $r$ through zero onto a branch where it is negative.** ⛔ **My pre-registered ⒜ said both
give $r^3$ even. Half right:** the *agreement* holds and the *parity* does not — I had taken the reflection
for the crossing, and the reflection is not the crossing.

## ⒝ The stress-energy, and the step where the naive answer is unphysical

| component | parity | |
|---|---|---|
| $\rho$ on the **signed** radius, $3M_b/4\pi r^3$ | **odd** | ⛔ it changes sign — a negative mass density, which is no state at all. Taken at face value this is **C3, undefined.** |
| $\rho$ on the **unsigned** radius, $3M_b/4\pi\lvert r\rvert^3$ | **even** | ✔ and this is the right one: the denominator is a **volume**, and `P3` states the areal radius is a *signed coordinate* with $g_{\theta\theta}=r^2$ insensitive to its sign |
| $dr/d\theta$ (signed rate) | even | |
| $d\lvert r\rvert/d\theta$ — the rate **relative to the matter's own outward direction** | **odd** | ✔ **infall becomes outflow** |
| dust pressure | zero, trivially even | |

⛭ **The control is what makes the even answer worth anything.** On the *signed* radius the parity follows
the exponent's parity — dust $r^{-3}$ odd, radiation $r^{-4}$ and stiff matter $r^{-6}$ even — *and whether
a species survives the crossing cannot depend on whether its exponent is an odd number.* That absurdity is
the tell: the signed radius is the wrong variable for a density. On $\lvert r\rvert$ every species is even,
as a density must be. ⇒ *The even result comes from the volume being a volume, not from the arithmetic.*

## ⒞⒟ The map, and why it is a bijection

The crossing's data are $(\rho(l),\,v(l))$, and the map is

$$(\rho(l),\,v(l))\ \longmapsto\ (\rho(-l),\,-v(-l)).$$

Applied twice it is the identity — **an involution, hence a bijection on the state space.** ⇒ **C1.**
Nothing is lost and nothing is added: every moment of the 4.364 Gyr approach has exactly one image.
And **⒟ holds**: the sign flip of the areal rate *is* collapse becoming expansion, and it falls out of the
parity rather than being put in.

⌗ **What that settles about the row's own wording.** `P15` says the crossing *"carries whatever survives it
unchanged … because there is no interval in which anything could act."* Measured: the crossing is not a
filter, so **"whatever survives" is everything** — the survival clause is vacuous rather than restrictive.
And the *"transmitted datum"* is the **whole approach**, not a few numbers taken off it, so **C2 is
excluded rather than merely unchosen.**

## ⛔ What is not claimed

**No pressure is carried across.** Dust has only a density and a radial rate to carry a parity; $T^r{}_r$
and $T^\theta{}_\theta$ are untouched here, and `P16`'s own interior is dust **plus radiation**. On
$\lvert r\rvert$ radiation's density is even too, so there is no parity *difference* — but no computation
here has carried a pressure term across, and that is a different statement from there being nothing to
carry. Nothing either about what the evolution *does* with the freedom; only that the crossing transmits
it bijectively.

⚠ **And one defect of my own, caught before the gate caught it.** A first draft of the receipt ended one
check in `or True` — the `cannot-fail` class this family has measured four times, written by the seat that
measured it. Replaced with a real assertion: the set of real proper times at which $r^3<0$ must be
**empty**, which `solveset` confirms. The note sits at the line that caused it.

## ⇒ The row after this revision

- **Discharged for a pressureless concrete model:** the stress-energy is carried through as an involution
  with no free data — a dynamical answer, not a transmitted datum.
- **The BOUNDARY exit stays dead**, now from the other side: the approach has the freedom (`.5`) and the
  crossing carries it through intact (here), so *"no freedom at all"* fails twice over.
- **Named, not claimed:** the pressure half. A model with pressure has two more components to carry, and
  that is the next step if the row is to close for `P16`'s own dust-plus-radiation interior.
