---
kind: PREDICTION
row: PO-88
step: the pressure half — T^r_r and T^θ_θ carried through the branch point
revision: r7473+cc66.11
written: before any line of the build
---

# Pre-registration — `PO-88`'s pressure half

*Written and committed before the computation exists, so the estimate cannot be back-fitted. `r7471` ③ puts
the pre-registration in its own file; this is that file.*

## What is being asked

`r7473` orders the pressure half: **`P16`'s own interior — dust plus radiation — carried through the branch
point with $T^r{}_r$ and $T^\theta{}_\theta$.** `r7465+cc66.10` discharged the row for a **pressureless**
model: the crossing is an involution $(\rho(l),v(l))\mapsto(\rho(-l),-v(-l))$, the density even on the
unsigned radius because its denominator is a volume, the radial rate odd. Dust had only those two
quantities to carry a parity. A fluid with pressure has two more.

## The arithmetic done in advance, so it is not priced

For a perfect fluid in the comoving frame $T^\mu{}_\nu=\mathrm{diag}(-\rho,p,p,p)$, so $T^r{}_r$ and
$T^\theta{}_\theta$ are both the scalar $p$. Radiation's $p=\rho/3$ with $\rho\propto\lvert r\rvert^{-4}$.
⇒ **On the unsigned radius radiation's density and pressure are even by the same argument as dust's**, and
`.10`'s control already measured that: $r^{-4}$ and $r^{-6}$ are even even on the *signed* radius, where
dust's $r^{-3}$ is odd. *That much I am not pricing.*

## ⚠ The one place I cannot compute in advance, named rather than papered over

**The corpus carries a second parity, in a different variable, and I have not established the two are
independent.** `P16` §`interior` solves the closed dust-plus-radiation ball exactly in **conformal time**,
$a=(A/2)(1-\cos\eta)+\sqrt B\sin\eta$, and its receipt
`P16_cosmogenesis/I14_the_interior_is_a_driven_oscillator_and_the_parity_split_is_forced_by_linearity.py`
establishes that *"the parity splits **by species** with no cross terms — the dust term is the entire even
part and the radiation term the entire odd part"*, forced by the linearity of $a''+a=A/2$.

⇒ So **radiation is the ODD part of the scale factor in $\eta$**, while `.10`'s crossing parity is in the
arc-length variable $l$ (or $\theta$). *Two parities, two variables.* Whether they are independent, or
whether radiation's oddness in $\eta$ reaches the crossing and makes its contribution odd there, is the
**build's first measurement and not its assumption.** ⌗ *`.10` failed in exactly this position — I took a
reflection for the crossing in a place the price had flagged and then predicted the flagged answer anyway.
So the entry below is written to be killed.*

## The five answers, each falsifiable alone

| # | what is computed | pre-registered answer |
|---|---|---|
| ⒜ | the parity of $T^r{}_r$ and $T^\theta{}_\theta$ under the crossing | **both EVEN** — they are quadratic in the radial direction the crossing flips, and built from the scalars $\rho$ and $p$ |
| ⒝ | are the $\eta$-parity (`I14`) and the crossing parity (`.10`) independent | **YES, independent** — ⚠ *this is the one above, and the one most likely to be wrong* |
| ⒞ | is the crossing still an involution for dust **plus radiation** | **YES** |
| ⒟ | does `PO-88` discharge for `P16`'s own interior | **YES** |
| ⒠ | does the crossing leave any sector free, per `60`'s `r7462` | **NO sector is left free *by the crossing*.** The composition is free, and that is a fact about the **approach** — total dissociation erases it before the branch point — not about the crossing |

**What would kill each:** ⒜ dies if either component's parity is odd, or if a frame-dependence makes
"parity" ill-defined for it. ⒝ dies if the two parities interact — and *that is the interesting failure*,
because it would make the crossing species-selective and revive the filter outcome `.10` excluded for dust.
⒞ dies with ⒜ or ⒝. ⒟ dies if any component cannot be carried across at all. ⒠ dies if a sector turns out
free at the crossing itself rather than on the approach.

## Cost

| what | predicted (band) |
|---|---|
| the computation script | **180** lines (120–300) |
| `WALK.md` | **100** lines (70–180) — ⌗ *central lowered from 160: the last three came in at 122, 122, 92* |
| wall time | **5 s** (1–60) |
| measurement runs | **4** (2–8) |
| turns to the result | **2** (1–4) |
| a receipt | ⚠ **owed**: parity claims are assertable, with a control — a component whose parity is the other one. ⌗ *`r7471` ① freezes the instruments; a receipt about **physics** is not an instrument about an instrument, and this one asserts a result rather than a gate.* |
