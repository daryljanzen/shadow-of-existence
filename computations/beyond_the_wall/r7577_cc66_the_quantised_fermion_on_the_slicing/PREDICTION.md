---
kind: PREDICTION
row: PO-95
revision: r7577+cc66.1
---

# `PO-95` — the quantised fermion field on the slicing: completeness, and the continuum-to-wall join

*Written before any computation of mine exists. Nothing below is a result. The scoring goes in `WALK.md`
and the receipt, against these bands and not against a reconstruction of them.*

## The order

`r7577`: `P14` states it open — the wall's tortoise divergence is the normalisation of a radial continuum
with a thermal spectrum, and **what that supplies is the continuum and not the sector**. Two halves
discharge the row:

- ⒜ **completeness** of the wall-bound modes together with the continuum, **shown in the leaf's own
  measure**;
- ⒝ **the matching** of the static region's continuum to the wall-bound modes, **computed across the locus
  the geometry already crosses**.

**Terminal clause, which the order weights equally:** if both turn out to be standard spectral theory of a
Dirac operator on a fixed background with nothing the construction adds, say so, and the row ends as a
stated limit.

## ⚠ THE SOURCE QUESTION FIRST, AND IT PARTLY ANSWERS THE ORDER

The row's own text says *"no row carried it."* That is true of **rows**. It is **not** true of receipts:
`receipts/L221_the_bridge/` carried much of this content under **`PO-11`**, and the prior is the one the
field note's `r1141` face states — in a corpus this comprehensive, *"unstated / open"* is most likely a
stale link. Recorded here **before** computing, so none of it can be reported later as mine:

| receipt | what it establishes | in which measure |
|---|---|---|
| `B25_the_scattering_object_exists` | the scattering object exists; continuum normalisation **defined** on the static region, from `W=\lambda\sqrt f/r`'s Regge–Wheeler partners vanishing at both horizons | tortoise |
| `B26_the_spectrum_computed` | the spectrum **computed**: transmission `0.020` → `0.9997`, unitarity to six figures, on `M=0.12`, `α=1`; `V_+` peaks `1.96307` at `r=0.30385` | tortoise |
| `B27_completeness_follows` | **completeness closes** — potential bounded and exponentially decaying on the line, which is **Kato–Rellich**'s hypothesis and the short-range condition | **tortoise line** |
| `B46_one_matching_not_two` | the two crossings are **not alike**: the inner horizon is at **infinite** tortoise distance, the wall at `r=0` at **finite** — so this is **one matching, not a two-horizon matching** | tortoise |
| `B48_the_field_is_dirac...` | the field is **Dirac**, so the matching is **determined rather than chosen** (`L-828`'s fermion branch) | — |
| `B67_verdict_the_analytic_sqrt_f_operator` | the operator call: the **analytic `\sqrt f`** operator; at `ω=0` there is **no fork** (`\sqrt f` cancels, index real `±λ`), the fork biting only at `ω≠0` where the `ω`-coupling's `1/\sqrt f` does not cancel | — |

⇒ **So the residue this file may claim is narrow, and I state it now rather than discovering it
conveniently later.** Completeness is **already closed in the tortoise measure**, by Kato–Rellich, for
`PO-11`. My order asks for it **in the leaf's own measure**, `d\ell=dr/\sqrt{|f|}` — *a different operator
on a different domain*, where `P14` records the horizons at **finite** distance, the `r=0` crossing an
**integrable** square-root singularity, and the closed leaf of **finite total length** (`1.8138\,α` at
Nariai, `P14_leaf_compactness`). **That is not the same theorem and Kato–Rellich is not available there.**

## The structural crux, stated before it is tested

`P14`: on the static region `d\ell/dr_*=\sqrt f` is bounded, so `L^2(dr_*)\subset L^2(d\ell)` **strictly** —
the leaf norm is the weaker condition. And the leaf is **compact**. A self-adjoint operator on a compact
domain with compact resolvent has **pure point** spectrum and no continuum at all.

⇒ **Then "the completeness of the wall-bound modes together with the continuum, in the leaf's measure"
cannot mean what it means in the tortoise measure**, because in the leaf measure there may be no continuum
to be complete *with*. Either (i) the two measures carry **different spectral types** and the row's
statement is really about a map between them, or (ii) the `r=0` singularity or the wall monodromy supplies
continuous spectrum in the leaf measure after all. **Which of those holds is the computation.**

The wall's local data are fixed and sharp: near it `f\to-2M/r` gives `r^3=\tfrac92 M\ell^2`, so a crossing
is a **half-loop in `\ell`** sending `r\mapsto\omega r` exactly, `\omega=e^{2\pi i/3}`, and a mode
transported across returns multiplied by **`\omega^{-\lambda}`** (`P14_route_or_point`,
`P14_mode_monodromy_at_the_wall`). Three walls, **disjoint support**, at distinct points of the throat
circle.

## The predictions, at the weight I hold them

| # | prediction | confidence | band |
|---|---|---|---|
| ⒜ | the leaf-measure operator on the closed bead has **pure point** spectrum — no continuum branch — because the total length is finite and the horizons sit at finite distance | medium-high | 0 continuum branches; band 0–1 |
| ⒝ | at each `r=0` branch point the operator is in the **limit-circle** case (integrable singularity, bounded phase), so it is **not** essentially self-adjoint there and admits a family of self-adjoint extensions | medium | limit-circle at 3 of 3 walls; band 0–3 |
| ⒞ | the **monodromy `\omega^{-\lambda}`** selects the extension — i.e. the matching condition is fixed by the geometry rather than chosen | medium-low | — |
| ⒟ | completeness in the leaf measure then follows by the **spectral theorem for an operator with compact resolvent**, *not* by Kato–Rellich — so the two measures close completeness by **different theorems** | medium | — |
| ⒠ | the matching across the wall is **computable in closed form** near `r=0`, the mode being `\propto\exp(i c\sqrt{|r|})` there | medium-high | — |

⌗ **Where I am least sure, named now:** ⒞ and the terminal clause. ⒝–⒞ are a deficiency-index computation
I have not done, and `B67` already warns the `\omega\neq0` fork is where `1/\sqrt f` fails to cancel — so
the `ω≠0` problem in the leaf measure may not be self-adjoint at all without a condition I cannot derive
from the geometry. **If that is how it falls, ⒞ fails and I will report it as a failure, not round it.**

## ⚠ What each outcome means — pre-registered, per the order

1. **If ⒜+⒟ hold and ⒞ holds** (monodromy fixes the extension): the row **discharges**, and what the
   construction adds is explicit — two inequivalent measures closing completeness by two different
   theorems, with the wall's `\omega^{-\lambda}` fixing the self-adjoint extension. **Not** a stated limit.
2. **If ⒜+⒟ hold but ⒞ fails** (the extension is a free choice the geometry does not fix): completeness is
   then a **compact-interval theorem on a fixed background with a chosen boundary condition** — textbook —
   and the honest verdict is the **terminal clause**: the row ends as a **stated limit**, with the choice
   named as the thing the construction does not supply.
3. **If ⒜ fails** (a genuine continuum survives in the leaf measure): the row's statement is coherent as
   written, completeness is the tortoise-style theorem transported, and the residue is whether the
   transport is more than a change of variable. That would make `B27` reach further than it claims, which
   is a finding about `B27` and goes to `69` rather than being absorbed here.
4. **If the two measures' spectra disagree on anything physical** (not merely on normalisability of one
   static mode): that is larger than this row and is routed, not claimed.

## The control, and what it is for

A verdict of *"pure point in the leaf measure"* is worthless until the instrument is shown able to find a
continuum where one is **known** to be:

1. **Reproduce `B26` in the tortoise measure** on its own member (`M=0.12`, `α=1`): the barrier peak
   `1.96307` at `r=0.30385`, transmission rising across the band, unitarity to the figures it reports. If
   my machinery cannot see the continuum `B26` computed, its silence in the leaf measure measures the
   machinery.
2. **A known limit-point/limit-circle pair** fed to the same deficiency-index test, which must classify
   both correctly — so ⒝ is a finding about this operator and not about my classifier.
3. **The leaf length** must come back finite and reproduce `P14_leaf_compactness`'s `1.8138\,α` at Nariai,
   since every claim in ⒜ rests on the domain being compact.

## Scope, stated before the fact

- **`P14` and `P7` are not edited**, and the instruments stay frozen per `r7577`: no new gate, ledger,
  census or receipt about receipts.
- **Nothing from `L221_the_bridge` is reported as mine.** `PO-11`'s tortoise-measure completeness,
  spectrum, scattering object, one-matching-not-two and the `\sqrt f` operator call are that line's.
- `r7577`'s new rule is noted: **if a result of mine moves a sentence that says something is or is not
  open**, I say so in my reply so `69` adds the row to
  `computations/beyond_the_wall/r7577_69_the_census_refresh/items_keyed.tsv`. ⌗ *On the state above this
  looks likely rather than hypothetical, since `P14`'s own "remain open" sentence is what the `L221`
  receipts bear on.*
