# F16 — P11 already names the place substrate isotropy and geometric isometry part company, and says it is the wall alone. F05's open question is exactly whether that is true — and it now has a sharp form: **polarization**

*status: OFFERED — three sentences from three papers put side by side, plus one computation that locates Bianchi II precisely. Sharpens F05 (batch 1) and F12.*
*receipt: `DRAFT_P11_where_the_two_notions_part_company.py`, rc=0.*
*touches: P11 `sec:strata`; P12 `sec:strata`; P8 `K9_isotropy_obstruction`; P9 `prop:surj`.*

---

## The corpus's most careful statement of this

P11 `sec:strata`:

> *This isotropy is the cut-fixing **substrate** isotropy; **on the symmetry-reducible sector it
> coincides with the generated geometry's own isometry** (the residual symmetry there is inherited
> from the substrate isometry that sweeps the cut) … **At the wall the two notions part company** —
> a point we will need: the substrate isotropy is zero, while the Type-N geometry retains its own
> (large) plane-wave isometry that is not substrate-inherited.*

So the corpus **knows** the two notions are different objects (K9 gives the criterion — Isotropy(c)
preserves the second fundamental form, and may be proper), **knows** they part company somewhere,
and **localises the parting to the wall**, everything reducible being safe.

F05 and F12 put a second candidate on the table, and it is not at the wall.

## Which G₂ class Bianchi II is in — the computation

P11 answers half of F05's question by building the G₂ case: **the polarized Gowdy–de Sitter wave**,
`prop:twoKV`, exactly two Killing vectors, *"the last confined stratum before the wall."* So the
question becomes: **is Bianchi II in the class P11 builds?**

Taking Bianchi II (Taub) with free a(t), b(t), c(t) — no field equations solved, the argument is
purely about symmetry structure:

```
ds² = −dt² + a²(dx − z dy)² + b² dy² + c² dz²
g_xx = a²    g_xy = −z a²    g_yy = z²a² + b²    g_zz = c²
```

- **Three Killing vectors**, verified: ∂_x, ∂_y, y∂_x + ∂_z, with [∂_y, y∂_x+∂_z] = ∂_x — the
  **Heisenberg** algebra.
- **The abelian G₂ = ⟨∂_x, ∂_y⟩ is orthogonally transitive**: g_tx = g_ty = g_zx = g_zy = 0, so
  ⟨∂_t, ∂_z⟩ is orthogonal to the orbits and integrable. *The same structural property the Gowdy
  class has.*
- **But it is unpolarized**: g_xy = −z a² ≠ 0, and asking for a **constant** λ with ∂_y + λ∂_x
  orthogonal to ∂_x gives (λ − z)a² = 0, i.e. **λ = z — not constant.** No change of basis inside
  the G₂ removes it. *(Control: the same test on a diagonal G₂ metric returns λ = 0.)*

P11's `eq:metric` is **diagonal** in (x,y) — linearly polarized, the single transverse-traceless
mode ψ. Bianchi II needs the second polarization.

> **Bianchi II sits in the orthogonally-transitive *unpolarized* G₂ class: one step beyond the
> stratum P11 builds, one step short of the wall.**

Whether the operator's four data — leaf, lapse, shift, vantage — span that class is `prop:surj`'s
counting question at k = 2, asked of a class the corpus has not built.

## What that makes of P11's sentence

| substrate isotropy | stratum | |
|---|---|---|
| 10 | Type O | de Sitter |
| 6 | Nariai | |
| 4 | Type D | SdS, R_t × SO(3) |
| 3 | Type I | Bianchi — **six of the nine** (F12) |
| 2 | Type I | the G₂ stratum — **P11 builds the polarized Gowdy–dS wave here** |
| 0 | Type N | the wall |

- If the unpolarized G₂ class **is** in the range: Bianchi II is a cut with substrate isotropy 2 and
  geometric isometry 3, the two notions part company **inside** the sector, and P11's sentence needs
  the same qualification P12's *"the isotropy dimensions are the Killing-vector counts"* needs (F12).
- If it is **not**: the range has a named remainder inside the symmetric sector — F05's original
  worry standing after all.

**Either way the phenomenon is the one P11 already names at the wall** — geometric isometry
exceeding substrate isotropy. The only open question is whether the wall is its only home, and
P11's sentence asserts that it is.

That is a better question than F05's, and it is the same question. It is also cheap to pose: **is
the orthogonally-transitive unpolarized G₂ class in the range?** One class, one counting argument,
and it decides a sentence in each of two papers.

## Not claimed

- **P11's sentence is not shown to be false.** It is shown to rest on F05's open question, which
  nobody has been carrying as load-bearing for it.
- No claim that the unpolarized G₂ class is or is not in the range — that *is* the question.
- No claim about `prop:twoKV`, which is right and untouched: the **polarized** Gowdy–dS wave has
  exactly two Killing vectors.
- No field equations were solved; a(t), b(t), c(t) are left free precisely so the argument is about
  symmetry structure alone.
- No closure on any registered item.
