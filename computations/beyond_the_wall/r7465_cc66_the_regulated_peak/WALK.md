---
kind: WALK
row: PO-88
step: r7399 — the exact regulated peak
revision: r7465+cc66.5
---

# `PO-88` — the regulated peak is $\rho_{\rm Planck}/6\pi$, and the row does not terminate as a boundary

*Every figure below is printed by `peak.py` in this directory (output `peak_out.txt`); every identity is
re-proved symbolically, with controls, in
`receipts/P16_cosmogenesis_paper/P16_the_regulated_peak_is_the_planck_density_over_six_pi.py` — **15 gates,
all pass, 1.0 s.***

## What the row asked, and the concrete model it is asked of

`r7399` added the named step: **the exact regulated peak — how deep the compression runs on the smooth
substrate through the branch point — is a number this row's discharge delivers.** `P16` §`peak` states it
open and says plainly that the peak it does give ($\Tpk\simeq174$ MeV from the infall energy) is
*"argued rather than computed"*.

The concrete model is `P16`'s own worked progenitor, so nothing is invented here: a closed dust-plus-$\Lambda$
interior of $M=4.17\times10^{52}$ kg. **It passes the one condition that makes it a progenitor at all** —
a turnaround exists exactly when $A\le2\alpha/3\sqrt3$, the Nariai mass parameter, and

$$A/A_{\rm Nariai} = 0.9768,$$

sub-Nariai by 2.3 per cent and not by orders. ⌗ *The model the paper hands this row sits just inside its
own admissibility condition, which is worth knowing before anything is computed on it.*

## The consistency check that had to come first

The substrate law is $r^3=2M\alpha^2\sinh^2(3\tilde\tau/2\alpha)$. Its branch-point limit is
$r^3\to(9/2)M\tilde\tau^2$, i.e.

$$\tilde\tau(r)=\frac{\sqrt2}{3}\,\frac{r^{3/2}}{\sqrt M},$$

and that is **identically the Oppenheimer–Snyder marginally-bound dust free-fall time**
$\tfrac23 r^{3/2}/\sqrt{2M}$ — agreeing to twelve figures at three radii spanning 25 orders, and proved as a
symbolic identity in the receipt. ⌗ *A result with no step in common. Until that held, no number of this
file's own was worth printing.*

Two further checks against the paper's own closed forms: $\rho_{\rm hor}=3M/4\pi R_s^3$ is identically
$3c^6/32\pi G^3M^2$; and $\rho_{\rm hor}/\rho_{\rm crit}=4.91$, which is **`P16`'s reductio made
arithmetic** — for a progenitor this massive, a peak pinned at horizon crossing would put the hot dense era
in our future.

## ⛔ Three candidate regulators, and all three fail on the numbers

| | candidate | measured | verdict |
|---|---|---|---|
| **R1** | the substrate's throat, $\alpha/\sqrt3$ | $9.51\times10^{25}$ m against $R_s=6.19\times10^{25}$ m — **1.54× larger** | ⛔ a throat-regulated peak is *less* compressed than horizon crossing |
| **R2** | the collapse branch's extremum, $\lvert r^3\rvert=2M\alpha^2$ | $r=1.19\times10^{26}$ m, **1.92 $R_s$**, reached at $\lvert\tilde\tau\rvert=\pi\alpha/3=18.2$ Gyr | ⛔ a de Sitter-scale time and a radius above the horizon: the **lap's** turnaround, not the matter's |
| **R3** | nothing: the divergence is one instant and the crossing has no duration, so the peak is the last compression of finite duration | the approach from $R_s$ to the branch point lasts **4.364 Gyr** of proper time | ⛔ there is no shortage of time, so *"nothing can act"* is false where R3 needs it true |

⛔ **R3 was my own pre-registered answer** (`FOR_66.md` §`r7465+cc66.102`, pushed in its own commit before
any of this was written). It is dead, and it is dead on a number I could have computed before predicting.

## ⇒ R4, which the price did not name: the proper-time budget

The compression is regulated where **the time left runs out**, not where the substrate bends. Setting the
remaining proper time equal to a response time $t$ and solving,

$$r_{\min}=\Bigl(\tfrac{3tc\sqrt M}{\sqrt2}\Bigr)^{2/3},\qquad
  \rho_{\rm pk}=\frac{3M_{\rm kg}}{4\pi r_{\min}^3}=\frac{1}{6\pi G t^2},$$

**in which the progenitor mass cancels identically** — derived symbolically, checked against the
mass-carrying numeric route to twelve figures, and checked directly by varying $M$ over twelve orders at
fixed $\rho_{\rm pk}$.

A fixed response time is not self-consistent, so the causal fixed point was taken too: nothing acts faster
than light crossing the mean nucleon spacing, giving $r_{\rm fp}=(9/2)k^2M$ with
$k=(4\pi m_N/3M_{\rm kg})^{1/3}$, hence $\rho_{\rm fp}=1.30\times10^{131}$ kg m$^{-3}$ — **34 orders above
the Planck density.** ⇒ The causal bound never bites: the classical description fails first.

So the peak is taken at the last epoch the classical description is entitled to, one Planck time of
remaining proper time, and the closed form collapses because $t_P^2=\hbar G/c^5$:

$$\boxed{\ \rho_{\rm pk}=\frac{1}{6\pi G t_P^2}=\frac{c^5}{6\pi\hbar G^2}=\frac{\rho_{\rm Planck}}{6\pi}
  =2.7347\times10^{95}\ \mathrm{kg\,m^{-3}}\ }$$

at $r_{\min}=3.31\times10^{-15}$ m, **exactly and free of the progenitor mass.** That is the number
`r7399` says this row's discharge delivers.

## ⛔ What is NOT claimed

**No temperature.** The marginally-bound infall energy $m_Nc^2(GM/rc^2)$ leaves its regime inside the
horizon ($GM/rc^2>1/2$), and at $r_{\min}$ it prints $\sim10^{29}$ MeV, which is the formula failing and
not the matter getting hot. ⌗ *That column is left in the output rather than deleted, because a deleted
wrong column teaches nothing.* `P16`'s 174 MeV is neither confirmed nor contradicted here. Nothing below
the Planck density, which is where this stops.

## ⛭ A fourth mass-blindness — and the count had to be read, which changed it

A first draft called this *"a third"*, on the strength of `P16`'s own sentence: *"What this does not show,
and is asserted nowhere: that either result implies the other, or that the pattern extends to a third
quantity."* **The register says otherwise.** `receipts/INDEX.md`'s `sec:peak (mass-blindness)` row carries
**three** — two sharing the amplitude-factorisation mechanism, one independent (the horizon identity) — and
records in its own words that *"the r1619 third instance REVISED this row's earlier
'no extension to a third quantity is claimed'"*.

⇒ **So this is a FOURTH, by a fourth mechanism — a proper-time budget, neither an amplitude exponent nor a
horizon identity.** The grouping becomes 2-of-one-kind + 1 + 1. ⌗ *This is the grep-derived-reader-set rule
applied to a count instead of a file: the number was in the register and I was about to recall it.*

⚠ **And the same read found `P16`'s own paragraph inconsistent with itself, routed and not fixed** — `P16`
is not this seat's file. The disclaimer sentence sits **after** the paragraph that supplies the third
instance (*"A third instance sharpens the grouping rather than merely lengthening the list"*), yet still
reads *"either result"* and *"a third quantity"*. The register records that the revision happened; the
paper's sentence did not follow it.

## ⇒ The row after this revision

- **Delivered:** the named `r7399` step, as an exact mass-free number, from the substrate law applied to the
  paper's own concrete progenitor.
- **The row does NOT terminate as a boundary.** The exit `c54.113` reached for needs the through-crossing
  evolution to have no freedom; the approach has **4.364 Gyr** of proper time and the compression runs
  thirty-four orders past where the substrate's own features could have stopped it.
- **Still open, and now sharply:** what the evolution *does* with that freedom — the field dynamics proper.
  This revision fixes the depth and the clock; it does not integrate a flow.
- **Routed, not taken:** the `P16` paragraph's internal inconsistency, and the register row's count, which
  this result moves from three to four.
