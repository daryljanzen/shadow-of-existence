# r7876+60 — THE MASS ENTERS THE PERTURBATIONS ONLY AS A SUBTRACTION, THE AMPLITUDE EXCESS IS NOT THE LEAN, AND THE REPAIR IS BUILT

*On order `r7875` (69), items ①, ② and ③. ④ waits on ③'s validation and is not begun.*

*Registered in `PREDICTION.md`, committed and pushed before any measurement of this revision ran.
Six reads taken before that registration are declared in it.*

---

## ① HOW THE MASSIVE SPECIES ENTERS THE PERTURBATIONS NOW

**The background already carries the mass epoch-consistently, and already did when `A` was
measured.** `r7874`'s generator ran `NUFD=1`, so the species' energy density there is
`Onu_of(a) = FNU·OR/a⁴·NUF_of(ln a)`, the Fermi–Dirac energy integral, counted once in the stack
and in both rate functions. **The amplitude excess is therefore not a background defect**, and ③ is
a perturbation-side repair only.

**The perturbations never learn the species has mass.** Read off the file:

| | what is there | at which epochs |
|---|---|---|
| the clustering matter | `OCDM = OM − OB − ONU`, with `ONU` the species' **late** constant | every epoch; the line has no epoch dependence |
| its weight in the potential's source | `On_of = FNU·(OR/a⁴)/_rt`, the **strictly massless** one; `NUF_of` does not multiply it | every epoch — it gravitates as pure radiation for all time |
| its continuity equation | `−(4/3)θ_ν + 4Φ'`, i.e. `w = 1/3` hard-coded | every epoch |
| its Euler equation | `k²(δ_ν/4 − σ)`, i.e. `c_s² = 1/3` hard-coded, with no `−H(1−3w)θ` drag and no `ẇ` term | every epoch |
| its `F_ℓ` ladder | the massless free-streaming ladder, no mass term, no momentum integration | every epoch |

⇒ **So the mass enters the perturbations only as a SUBTRACTION and never as a source.** The
clustering matter loses it; the species' own weight and equations never pick it up. The one route by
which the repaired background reaches the perturbations is the shared denominator `_rt`, which
rescales all four weights **together** and so cannot move the neutrino's share.

Two further clauses, both checkable: **`NUW_of`**, the Fermi–Dirac `w_ν(a) = p_ν/ρ_ν` spline, is
built under `NUFD=1` and was **read nowhere** — the no-free-parameter ingredient the repair needs
was already in the file. And **`Om_of` is dead**: defined, never read.

### THE DESIGN NUMBER — the defect measured, before the repair was designed

The four weights the source is built from, plus `OL/_rt`, do not close on 1, and what is missing is
exactly the mass the perturbations do not see:

```
Dclose(a) = (Og + On + Oc + Ob + OL/_rt) − 1 = −(Onu_of(a) − FNU·OR/a⁴)/_rt
```

Measured by **executing the instrument's own prelude** — the file's lines 1‥645 in a fresh
namespace, so nothing is reimplemented:

| Σ | `Dclose` at recombination | `Dclose` today | the instrument's own TT response over ℓ = 100–420, rms | ratio |
|---|---|---|---|---|
| 0.30 eV | `−2.0245e-03` | `−6.9702e-03` | `1.6418e-02` | **`0.123`** |
| 0.60 eV | `−7.5445e-03` | `−1.3978e-02` | `3.8001e-02` | **`0.199`** |

**The defect is the right size.** The registration set a tenth of the response as the floor below
which ③ could not account for a 15 per cent excess; the measured ratios are `0.123` and `0.199`,
above it at both sums, and they are `0.81` and `0.67` of the excess itself. ⇒ **The reachable
negative registered on ③ is not pre-indicated, and ③ is also not licensed to be credited with more
than this.**

And a second number, larger than the first: **`w_ν` at recombination is `0.3205` at 0.30 eV and
`0.2906` at 0.60**, against the `1/3` the species' own equations hard-code — a `4` and a `13` per
cent error in its equation of state at the epoch the first acoustic peak and the early ISW are built
at. The weight deficit is the smaller half of what ③ repairs.

---

## ② THE AMPLITUDE CORRECTION ARM — **Ⓑ: THE EXCESS AND THE LEAN ARE TWO THINGS**

The instrument's TT response divided by `A` over ℓ = 100–420 at each sum, `35` TT bins of the `555`
scored, spanning ℓ = 100–414, of which **12 are among the thirty-six removed**. EE and TE untouched,
because `r7874` measured EE already matching.

**THE REPRODUCTION ARM CAUGHT TWO DEFECTS IN THIS FILE'S FIRST RUN**, and they are reported rather
than quietly corrected: it read the **re-profiled** column where the `−20.09` headline is the
**frozen** one, and it took the move with the **opposite sign** to `r7866`'s own table. Both fixed
at the cause against that record. Uncorrected, both columns now reproduce it:

| column | whole | minus the thirty-six | move | `r7866` recorded | |
|---|---|---|---|---|---|
| frozen (the headline's) | `57.078` | `77.164` | **`−20.0868`** | `−20.09` | reproduced to `0.0032` meV |
| re-profiled (the 389-fold) | `68.133` | `116.335` | **`−48.2020`** | `−48.20` | reproduced to `0.0020` meV |

**Corrected**, with the two no-free-parameter interpolations of `A(Σ)` the registration fixed:

| form | `A(Σ)` | move, frozen | `f` | move, re-profiled | `f` |
|---|---|---|---|---|---|
| L | `1 + 0.496 Σ` | `−19.3306` | `0.0378` | `−46.2848` | `0.0397` |
| Q | `1 + 0.520 Σ − 0.04444 Σ²` | `−19.2995` | `0.0394` | `−46.2115` | `0.0413` |

⇒ **Ⓑ on both forms, on both columns.** The registration set `f ≤ 0.30` for Ⓑ and `f ≥ 0.982` for
Ⓐ; the measured `f` is `0.038`–`0.039`. **Removing the whole 15-to-30 per cent TT amplitude excess
over ℓ = 100–420 removes under four per cent of the lean.** The two interpolations agree to
`0.0015`, far inside the verdict gap, so the arm is decided and not left to the interpolation.

**What this settles, and what it does not.** `r7873` ruled the low-ℓ residual and the lean one
object until a measurement separated them. **This is that measurement, and it separates them.** It
does not say the lean is not an instrument defect — only that whatever carries it is not the
amplitude of the TT sum response over this band. The thirty-six still cost the instrument `162`
times what they cost the reference, with the excess divided out.

---

## ③ THE EPOCH-CONSISTENT NEUTRINO PERTURBATIONS — BUILT, AND VALIDATING

`NUPERT`, default off. **The Fermi–Dirac fluid approximation**, named in the code and here: the
species is carried as a fluid whose equation of state and sound speed are its own Fermi–Dirac ones
at each epoch, `w(a) = NUW_of(ln a)` and `c_s²(a) = w(a)`, with **no fitted quantity anywhere**.
Three changes, each reducing to the line that was there at `w = 1/3`:

- **the weight** — `On_of` becomes `Onu_of(a)/_rt`. Redefined where it is built rather than at its
  use sites, so all **seven** of them — both right-hand sides and the four source paths — take it
  together and cannot disagree.
- **continuity** — `δ_ν' = −(1+w)θ_ν + 3(1+w)Φ'`.
- **Euler** — `θ_ν' = −H(1−3w)θ_ν − (ẇ/(1+w))θ_ν + k²(c_s²/(1+w))δ_ν − k²σ + k²Ψ`.

`OCDM` is **not** changed: the species is now its own correctly-weighted sector, and adding ω_ν back
into the clustering matter would count it twice.

### The arms that pass before any spectrum is read

- **Byte-identical off**, measured on output and not asserted: `origin/main`'s own copy of the
  instrument against the patched one, with `NUPERT` **absent** and with `NUPERT=0` — every array of
  both saves identical element for element, `6` in the TT save and `11` in the polarisation one. The
  `config` string differs, **and must**: it carries the git blob hash of the file's own bytes.
- **It refuses to run half.** `NUPERT=1` without `NUFD=1`, and with a zero sum, both exit non-zero
  naming the reason: the repair *is* the species' own Fermi–Dirac weight.
- **The closure the defect was measured as now holds exactly.** `Dclose` is `1.11e-16` at 0.30 eV
  and `2.22e-16` at 0.60, at recombination and today — the numerator becomes `_rt` term for term.

### The one declared gap, and it is bounded rather than hidden

The `F_ℓ` ladder is left as the massless free-streaming one, so `σ_ν` is the relativistic shear at
all epochs: exact while the species is relativistic and wrong after. **`NUSHOFF=1`** switches that
shear off below the species' own non-relativistic transition, marked at `w(a) = 1/6` — a stated
choice, and the only one in the block. The **spread** between the two runs is the approximation's own
uncertainty on `A`, reported with the validation.

### Validation — the four verdicts were fixed before the repair was written

`A` and `ε` refitted against CAMB at Σ = 0.30 and 0.60 eV by **`r7874`'s own `shift.py`,
executed** — two lines of it rebound, the bank it reads and the file it writes, and nothing else
touched, so the CAMB legs, the `ε` allowance measured from `l_A` against `θ*`, the `ε` grid, the
`A`-across-the-band measurement and the verdict logic are the ones `r7874` was judged on. The same
code is run first on `r7874`'s own bank and must return `A = 1.152` and `1.296` before the repaired
legs are readable.

**The zero leg is the landed one** at every reading: `NUFD` is itself gated on a non-zero sum, so
`NUPERT` is provably inert there — which is also why it refuses to run there rather than pretending
to.

*⌗ The four legs are generating. The validation table, the shear spread and the verdict are appended
below when they land; nothing above this line depends on them.*
