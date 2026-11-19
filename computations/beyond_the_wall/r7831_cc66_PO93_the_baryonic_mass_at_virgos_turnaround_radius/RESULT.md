# r7831 — `PO-93`: THE STELLAR HALF OF ITS GATE IS MEASURED TO THE TURNAROUND RADIUS AND CLOSED; THE GAS HALF IS NOT, AND THE GAP IS NOW A FACTOR AND AN ANGLE

**COMPUTES:** nothing of the corpus's. Every number of Virgo's below is a quoted literature value
carrying **the aperture it was measured to**; the only instrument used is `r_HE`, imported by `ast`
from `receipts/P03_SdS_slicing/P03_which_mass_sets_the_hubble_eddington_radius.py` exactly as
`r7484` took it, so there is one copy of the relation in the tree.

**THE ORDER** (`r7829`, `69`): *"`PO-93` … its gate is data: a baryonic mass, gas plus stars,
measured within Virgo's turnaround radius of `7.0` to `7.8` Mpc. ① Search the literature for that
measurement, or for the pieces it can be built from … State what exists, with references and the
radius each figure is measured to. ② If the pieces reach the turnaround radius, build the baryonic
mass there with its error … ③ If they do not, state exactly how far they reach and what measurement
would close the gap."*

---

## ⌈ ⓪ THE ANSWER IN ONE LINE

**The pieces do not both reach `7.0` Mpc. The stellar piece does — exactly, and for the first time
in this row's history with an aperture attached. The gas piece stops at `1.2` Mpc, a factor of
`5.83` short.** And because the stellar term is the minority of the budget, its measured growth
across the aperture gap covers only `5.9`–`17.6` per cent of what `r7484`'s bound would need, so
**≥ `82` per cent of the missing mass must be gas.**

> ⇒ ⚑ **`PO-93`'s gate is therefore not "a baryonic mass" but specifically "a GAS mass". The
> stellar half is closed. That is a narrowing of the row, not a discharge of it.**

---

## ⌈ ① WHAT EXISTS, AND THE RADIUS EACH FIGURE IS MEASURED TO

The order asked for this pairing explicitly, and it is the whole discriminator.

### Hot gas — **MEASURED**

| figure | value | **aperture** | source |
|---|---|---|---|
| `M_gas` | `(1.98 ± 0.70) × 10¹³ M☉` | **`r₂₀₀ = 974.1 ± 5.7` kpc** | [eROSITA, A&A 2024](https://www.aanda.org/articles/aa/full_html/2024/09/aa49391-24/aa49391-24.html) |
| `M_gas` | `≈ 1.05 × 10¹³ M☉` | **`r₅₀₀`** (interior to `r₂₀₀`) | eROSITA, as above |
| density profile extent | `n_e ∝ r^−β`, `β = 1.21 ± 0.12` | **`r ≈ 1.2` Mpc** (13 XMM pointings, centre northwards) | [Urban et al. 2011, MNRAS 414, 2101](https://academic.oup.com/mnras/article/414/3/2101/1036393) |

⇒ **The furthest any MEASURED gas figure reaches is `1.2` Mpc.**

### Hot gas — **EXTRAPOLATED** ⚠

| figure | value | **aperture** | source |
|---|---|---|---|
| total gas mass | `1.4 × 10¹⁴ M☉` | integrated to a truncation radius of **`2.5` Mpc** | [Planck Intermediate XL, A&A 596, A101](https://arxiv.org/html/1511.05156) |
| total gas mass | `1.6 × 10¹⁴ M☉` | integrated to a truncation radius of **`5` Mpc** | Planck XL, as above |

⚠ **These are extrapolations and are labelled as such throughout.** The density follows Urban et
al.'s `r^−1.2` *beyond the measured region*, `≈ 1` keV is *assumed* for `r > 1` Mpc, and the paper
itself notes that models beyond `~4°` are extrapolations. The SZ *detection* reaches `~8°`,
`~2 ×` the virial radius. ⇒ *Prediction ⑤ of this revision's registration: these are reported, never
offered as a discharge.*

### Stars — **MEASURED**

| figure | value | **aperture** | source |
|---|---|---|---|
| `L_Ks`, collapsed core | `5 × 10¹² L☉` | **`R₂ₜ` projected radius `1.9` Mpc** | [Kourkchi & Tully 2017, ApJ 843, 16 §7.1](https://arxiv.org/pdf/1705.08068) |
| **`L_Ks`, Virgo Association** | **`1 × 10¹³ L☉`** | **`r₁ₜ ∼ 7` Mpc — the infall region** | Kourkchi & Tully 2017 §7.1 |
| `L_K` | `(8.6 ± 1.1) × 10¹² L☉` | inside the **`6°`** radius, `D = 12–22` Mpc (`≈ 1.8` Mpc) | [Kashibadze et al. 2020, A&A 635, A135 §3](https://arxiv.org/pdf/2002.12820) |
| `M_*` | `8.1 × 10¹² M☉` | within **the virial radius**, corrected for diffuse light | [Durrell et al. 2014, NGVS VIII](https://arxiv.org/html/1408.2821) |

⇒ **The stellar term reaches `7.0` Mpc.** Kourkchi & Tully's own words: *"The Virgo Cluster has an
`R₂ₜ` projected radius of `1.9` Mpc while the **Virgo Association, enclosing the infall region, has a
radius of `7` Mpc**."* And: *"The galaxies in the association have an integrated `Ks` band luminosity
of `1 × 10¹³ L☉` with `5 × 10¹² L☉` in the collapsed core (`50 %`)."*

### Dynamical totals inside `R₀`

| figure | value | **aperture** | source |
|---|---|---|---|
| `M_T` | `(7.4 ± 0.9) × 10¹⁴ M☉` | inside `R₀ = 7.0–7.3` Mpc, infall model | Kashibadze et al. 2020 |
| `M_vir` | `(6.3 ± 0.9) × 10¹⁴ M☉` | the virial zone | Kashibadze et al. 2020 |
| total mass | `7 × 10¹⁴ M☉` (`4 × 10¹⁴` in the core) | within the association, `r₁ₜ ∼ 7` Mpc | Kourkchi & Tully 2017 |

⌗ *Kourkchi & Tully's mass is **luminosity-derived** — their own caveat, quoted: "The luminosity
figures are best known because large galaxies dominate and are easily seen across the region of
interest. The mass figures rely on assumptions susceptible to systematics." It is reported for its
agreement with the kinematic `7.4 × 10¹⁴`, not as an independent total.*

### ⛔ AND ONE FIGURE THAT LOOKS LIKE A GAS MASS AT A LARGE APERTURE AND MAY NOT BE USED AS ONE

[HeVICS XVI (Davies et al. 2014)](https://arxiv.org/pdf/1311.1774) quotes a hot-gas mass **density**
of `∼ 10¹² M☉ Mpc⁻³`, which over its `62.4 Mpc³` survey volume is `∼ 6 × 10¹³ M☉`. **Its own
parenthesis says how it was obtained:** *"we have used `20 %` of the gravitational mass measured by
the X-rays"*.

> ⚠ **That is an ASSUMED baryon fraction of `0.20` — which is the very quantity `PO-93` exists to
> have measured. Using it to answer `PO-93` would be circular, and it is excluded on that ground
> rather than on its aperture.**

⌗ *Two further traps in the same paper, recorded because both would have produced a wrong number:
its totals are **densities** in `M☉ Mpc⁻³`, not masses — a figure like `4 × 10¹⁰` for "total cluster
stars" is a density and misreads as a stellar mass two hundred times too small; and the `62.4 Mpc³`
volume is an `85` sq deg sky area times a `17`–`23` Mpc depth — **a slab of projected radius
`≈ 1.7` Mpc, not a sphere of radius `7`.* Its stellar density `× 62.4 Mpc³ = 2.50 × 10¹² M☉`, which
is consistent with the other core-aperture stellar figures.*

---

## ⌈ ② THE ONE BARYONIC TERM THAT IS MEASURED TO THE TURNAROUND RADIUS, BUILT

Both of Kourkchi & Tully's stellar figures are measured, and the pair **straddles exactly the
aperture gap `r7484` identified**:

| | `L_Ks` | aperture |
|---|---|---|
| collapsed core | `5.000 × 10¹² L☉` | `R₂ₜ = 1.9` Mpc |
| Virgo Association | `1.000 × 10¹³ L☉` | `r₁ₜ ∼ 7.0` Mpc |
| **growth factor** | **`2.0000`** | `1.9 → 7.0` Mpc |

> ⚑ **The measured stellar growth factor across the aperture gap is exactly `2.00`, which sits
> inside the `1.70`–`2.35` window `r7484` showed the TOTAL baryons would need.**

With `M_*/L_Ks = 0.6`–`1.0` for old cluster populations:

**`M_*(r₁ₜ ∼ 7` Mpc`) = (6.0` to `10.0) × 10¹² M☉`, midpoint `8.0 × 10¹² M☉`.**

⌗ **This corrects a weakness in `r7484`'s own input.** That revision used `M_* = 1.5 × 10¹³ M☉`
inferred from Kashibadze's remark that the gas is *"an order of magnitude higher than the integral
stellar mass"* — a figure carrying **no stated aperture at all**. The value above agrees with it
within the `M/L` band and **now carries one**. *Its being slightly lower makes the baryon-only
violation marginally stronger, not weaker; it is reported because it is what the photometry gives,
not because of which way it moves the answer.*

---

## ⌈ ③ THE GAP, QUANTIFIED — AND WHY THE MEASURED TERM CANNOT CLOSE IT

`r7484`'s requirement, quoted: *"For the baryon-only bound not to be violated, the baryonic mass
inside `R₀` would have to be `1.70` to `2.35` times the gas-plus-stars measured inside `~3.4` Mpc —
`2.6`–`4.1 × 10¹⁴ M☉`."*

| | value |
|---|---|
| required inside `R₀` | `2.60` to `4.10 × 10¹⁴ M☉` |
| on the books inside `~3.4` Mpc (gas EXTRAPOLATED + stars) | `1.55` to `1.75 × 10¹⁴ M☉` |
| **shortfall to be found between `3.4` and `7.0`–`7.8` Mpc** | **`8.50 × 10¹³` to `2.55 × 10¹⁴ M☉`** |
| what the stellar doubling adds, **at most** | `1.50 × 10¹³ M☉` |
| **fraction of the shortfall the measured stellar term covers** | **`5.9 %` to `17.6 %`** |

*"At most" because `3.4` Mpc already encloses part of the growth measured from `1.9` Mpc, so the
true stellar contribution across `3.4 → 7` Mpc is smaller than the figure used.*

> ⇒ ⚑ **So `≥ 82` per cent of the missing mass must be gas, and no measured gas figure reaches past
> `1.2` Mpc. `PO-93`'s gate is a GAS measurement, specifically.**

### ⚠ AND THE MARGIN ON THAT, BECAUSE IT IS A FACTOR AND NOT AN ORDER OF MAGNITUDE

The receipt's probe `Ⓖ⑦` perturbs the stellar term and the verdict **flips at `M_* × 2`** — so this
finding rests on a factor of two, and saying so is part of reporting it.

| for stars to supply | the inner `M_*` it would take |
|---|---|
| `25 %` of the shortfall (the verdict threshold) | `2.12` to `6.375 × 10¹³ M☉` (`1.42`–`4.25 ×`) |
| `50 %` of the shortfall | `4.25` to `12.75 × 10¹³ M☉` (`2.83`–`8.50 ×`) |

**The largest published Virgo stellar mass at ANY aperture is NGVS VIII's `8.1 × 10¹² M☉`** —
ICL-corrected, inside the virial radius — and `r7484`'s input of `1.5 × 10¹³ M☉` is already larger
than that. **So the nearest flip sits `2.62 ×` above the largest figure the literature provides, and
no measurement reaches it.** ⌗ *The finding is robust against the data that exist, by a factor of
`2.6` rather than by orders of magnitude, and `r7484`'s stellar input is the generous choice: using
NGVS's measured `8.1 × 10¹²` instead would make the stellar contribution to the shortfall `smaller`
(`3.2`–`9.5` per cent), not larger.*

⌗ *And the direction of the row is not in doubt while that gate stays shut.* Substituting the
measured stellar term into the bound: `M_bary = 1.460`–`1.700 × 10¹⁴ M☉` allows
`r_HE = 5.522`–`5.809` Mpc against `R₀ = 7.0`–`7.8` Mpc, so **`R₀/r_HE(M_bary) = 1.205`–`1.413`,
still violated** — `r7484`'s `19`–`33` per cent survives the substitution. Taking even the
*extrapolated* budget at face value gives `M_bary/M_T(R₀) = 0.176`–`0.262`, **below the `33` per cent
floor** a baryon-only Virgo would need. ⚠ *Both lines are bounds, not the measurement the row asks
for, and neither is offered as a discharge.*

---

## ⌈ ④ WHAT MEASUREMENT WOULD CLOSE THE GAP — STATED AS AN APERTURE ON THE SKY

The gap is not a deeper exposure of the same thing. It is an **angular reach**.

At Kourkchi & Tully's weighted distance `D = 15.8 ± 0.5` Mpc:

| | required angular radius |
|---|---|
| `R₀ = 7.0`–`7.8` Mpc at `D = 15.8` Mpc | **`23.9°` to `26.3°`** |
| at `D = 15.0` Mpc | `25.0°` to `27.5°` |
| at `D = 18.0` Mpc | `21.3°` to `23.4°` |
| the deepest existing SZ detection (Planck XL) | `~8°` |

> ⇒ **The closing measurement must reach `3.14 ×` further in angle than the deepest one that
> exists.** A diffuse-phase probe — Sunyaev–Zel'dovich or absorption — of Virgo's infall region out
> to `≈ 24°`–`26°` from M87, resolving a gas mass profile rather than fitting a truncated model to a
> `~8°` detection.

⌗ *That `3.14 ×` is an arithmetic identity, not a new result, and is worth one line precisely so it
is not mistaken for one: Planck's `~8°` reach is close to the second-turnaround angle
(`arctan(1.9/15.8) = 6.9°`), and `ΛCDM` gives `r₁ₜ/r₂ₜ = 3.14 ± 0.28` — the ratio Kourkchi & Tully
quote from Tully 2015. **The required extension is the first-to-second turnaround ratio because that
is precisely what the aperture gap is.** It is the same statement as `§③`, in angle instead of mass.*

---

## ⌈ ⑤ THE ARMS, AGAINST `PREDICTION.md` — registered and pushed before a single search was run

| arm | registered | measured | |
|---|---|---|---|
| **①** the pieces do not reach `7.0` Mpc, and **the GAS is what stops** | *"no published hot-gas mass profile for Virgo reaches beyond about `2` Mpc"* | furthest measured gas aperture **`1.2` Mpc**; short by `5.83 ×` | **HIT** |
| **②** the stellar piece reaches further, and is the minority term | predicted, unhedged | reaches **`7.0` Mpc exactly**; `~6 %` of the budget | **HIT, both clauses** |
| **③** the binding gap is a **diffuse-phase** probe, absorption or SZ-type, not a deeper exposure | predicted | an SZ probe at `≈ 24°`–`26°`, vs `~8°` existing | **HIT** |
| **④** `PO-93` neither discharges nor terminates | predicted | neither; the row narrows to its gas half | **HIT** |
| **⑤** I will not pass an extrapolation off as a measurement | a guard, not a prediction | the Planck figures are labelled `EXTRAPOLATED` at every appearance and excluded from every discharge claim; the HeVICS gas figure excluded as **circular** | **HONOURED** |
| **⑥** every figure carries the radius it was measured to | a guard | every row of `§①` | **HONOURED** |

**Four hits, two guards honoured, nothing reframed and nothing withdrawn.**

⌗ **The registration also under-reached in one place, and it is recorded rather than quietly
upgraded.** ③ predicted the closing measurement *"is an absorption or Sunyaev–Zel'dovich-type probe
rather than more of the same emission"* and left it there. It did not predict that an SZ probe **had
already partly been done** — Planck XL detects SZ excess to `~8°` — so the real gap is not "no SZ
exists" but *"the SZ that exists reaches `~8°` and the masses quoted past it are extrapolated"*.
**The instrument was predicted correctly and the state of the art was not checked first.** That is
the weaker form of the same prediction, and `§④` states the gap in the sharper form the data
support.

---

## ⌈ ⑥ THE CONTROLS

- **Ⓥ① the instrument is the imported one and its control re-runs — PASS.** `r_HE` and its constants
  come out of `P03` by `ast`; the control reproduces `f_b^{−1/3} = 1.854` in radius and
  `1/f_b = 6.37` in mass.
- **Ⓥ② every figure carries its aperture — PASS**, and three figures were **excluded** by it: the
  Planck masses from any discharge claim (extrapolated), the HeVICS gas mass entirely (circular),
  and the HeVICS densities from being read as masses.
- **Ⓥ③ the aperture gap is reported, not absorbed — PASS.** The one term measured at `R₀` is given
  with its growth factor, and its *insufficiency* to close the gap is the result.
- **Ⓥ④ the distance propagated with a number — PASS.** `D = 15.0`–`18.0` Mpc moves the required
  angular radius from `21.3°`–`27.5°`; the conclusion that it exceeds `~8°` survives throughout.
- **Ⓥ⑤ the two stellar routes cross-checked — PASS.** `L_K = (8.6 ± 1.1) × 10¹² L☉` inside `6°`
  (Kashibadze) against `5 × 10¹² L☉` inside `R₂ₜ = 1.9` Mpc (Kourkchi & Tully) and
  `M_* = 8.1 × 10¹² M☉` inside the virial radius (NGVS VIII). ⌗ *The NGVS figure is the highest of
  the three because it is the one that adds intracluster light; the spread is the `M/L` and `ICL`
  systematic and is why `§②` reports a band rather than a value.*

---

## ⌈ ⑦ WHAT IS SUPPLIED, AND WHAT IS NOT

**Supplied:** the literature state of `PO-93`'s gate, every figure with its aperture; the stellar
term **measured at the turnaround radius** — the first baryonic component of this row to carry that
aperture; its growth factor `2.00` across the gap; the demonstration that it covers only `5.9`–`17.6`
per cent of the shortfall, so the gate is specifically a **gas** measurement; the gap restated as an
angular reach of `≈ 24°`–`26°` against `~8°` existing; and `r7484`'s direction re-verified under the
substitution.

**Not supplied:** `f_b` at the turnaround radius as a *number*. **That still needs a measured gas
mass at `R₀`, and it does not exist.** `PO-93` stays open.

**Nothing is applied to the register, and the strike is the register's act, not this file's.
Supplied, not applied.**
