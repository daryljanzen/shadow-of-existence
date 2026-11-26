# r7876+60 — REGISTRATION

*Register-before-measure. This file is committed and pushed before any measurement of this revision
runs. Nothing above a marked ADDENDUM is changed after a result lands; a mid-revision arm goes into
an ADDENDUM, pushed before it runs.*

**On order `r7875` (69), items ①, ② and ③.** ④ waits on ③'s validation and is not registered here.

---

## ⌗ READS TAKEN BEFORE THIS REGISTRATION — DECLARED

1. **`ACOUSTIC_two_arm.py`, the sites the massive species does and does not reach.** Read before
   writing this file, because item ① *is* that read and the order says the repair is to be designed
   against what is there. The statement it produced is written out in ① below **as a registration**:
   the receipt re-derives every clause of it from the source, and a clause that does not hold on the
   file is a failed arm, not an edit to this file.
2. **`r7874`'s record**, for the two numbers item ② corrects by: `A = 1.152` at `Σ = 0.30` eV and
   `A = 1.296` at `0.60`, each with its across-the-band range (`[1.146, 1.153]`, `[1.284, 1.298]`).
3. **`r7874`'s generator**, which establishes that the amplitude excess was measured with the
   Fermi–Dirac background repair **ON** (`NUFD=1 BVEL=1`). So the background is already
   epoch-consistent at the point `A` was measured, and ③ is a perturbation-side repair only.
4. **The lean's size**, `−20.09` meV for the thirty-six lowest bandpowers at `ℓ = 100–207`, against
   the reference's `−0.12`, from `r7866`'s record as carried forward by `r7869`.

No spectrum of this revision has been computed. No `A` or `ε` has been refitted. No limit has been
read.

---

## ① THE STATEMENT — how the massive species enters the perturbations now

*Registered as a set of clauses, each checkable against the source. The reachable negative is a
clause that does not hold on the file.*

**S1. The background carries the mass epoch-consistently, and already did when `A` was measured.**
Under `NUFD=1` the species' energy density is `Onu_of(a) = FNU·OR/a⁴·NUF_of(ln a)`, the Fermi–Dirac
energy integral, counted **once** in the stack `_rt` and in both rate functions.

**S2. The clustering matter loses ω_ν at every epoch.** `OCDM = OM − OB − ONU` with `ONU` the
species' **late** density parameter, a constant. There is no epoch dependence on that line.

**S3. The species' weight in the potential's source is the strictly massless one, at every epoch.**
Both right-hand sides build the source as `Ogv·dg + Onv·dn + Ocv·dc + Obv·db` with
`On_of = FNU·(OR/a⁴)/_rt`. `NUF_of` does **not** multiply it. The species therefore gravitates in
the perturbations as pure radiation for all time.

**S4. The species' own equations contain no mass.** Its continuity and Euler equations hard-code
`w = 1/3` (`−(4/3)θ_ν + 4Φ'`) and `c_s² = 1/3` (`k²(δ_ν/4 − σ)`), carry no `−H(1−3w)θ` drag and no
`ẇ` term, and the `F_ℓ` ladder above them is the massless free-streaming ladder with no mass term
and no momentum integration.

**S5. So the mass enters the perturbations only as a subtraction and never as a source.** S2 removes
it; S3 and S4 never add it back. The one route by which the repaired background reaches the
perturbations is the shared denominator `_rt`, which rescales all four weights **together** and so
cannot move the neutrino's share.

**S6. The no-free-parameter ingredient ③ needs is already in the file and unused.** `NUW_of`, the
Fermi–Dirac `w_ν(a) = p_ν/ρ_ν` spline, is built under `NUFD=1` and is referenced nowhere.

**S7. `Om_of` is dead.** Defined, never read.

**S8 — THE DESIGN NUMBER, and this one is measured, not read.** The four perturbation weights plus
`OL/_rt` do not close on 1, and the deficit is exactly the mass the perturbations do not see:

```
Dclose(a) = (Ogv + Onv + Ocv + Obv + OL/_rt) − 1 = −(Onu_of(a) − FNU·OR/a⁴)/_rt
```

**I will report `Dclose` at recombination and at `a = 1`, at `Σ = 0.30` and `0.60` eV, and set it
beside the measured size of the instrument's own sum response over `ℓ = 100–420`.** That ratio is
what bounds what ③ can do, and it is registered **before** ③ is built so that ③ is not credited
with more than the defect it removes.

**⚠ A REACHABLE NEGATIVE ON ③, STATED NOW.** If `|Dclose|` at recombination is small against the
sum response's own size — say below a tenth of it — then the defect S2–S4 name cannot account for a
15 per cent excess, ③ should not bring `A` to one, and **the order's own alternative is the expected
finding: the defect is elsewhere.** I register that I will say so in those words if that is what the
numbers give, and will not rescue ③ by widening it.

---

## ② THE AMPLITUDE CORRECTION ARM — does the excess carry the lean?

### What is corrected, exactly

The instrument's TT spectra at each sum are corrected so that the **response** is divided by `A`:

```
D_corr(ℓ, Σ) = D(ℓ, 0) · (1 + r(ℓ, Σ)/A(Σ))    for 100 ≤ ℓ ≤ 420
D_corr(ℓ, Σ) = D(ℓ, Σ)                          outside that band
r(ℓ, Σ)      = D(ℓ, Σ)/D(ℓ, 0) − 1
```

EE and TE are **not** corrected: `r7874` measured EE matching CAMB to 1–5 per cent, so there is
nothing there to correct, and correcting it would be a free parameter.

### `A(Σ)` — no free parameter, and two forms, both reported

`A` was measured at two sums only, and `A(0) = 1` exactly by construction. Two interpolations:

- **form Q** — the quadratic through `(0, 1)`, `(0.30, 1.152)` and `(0.60, 1.296)`. Exact at all
  three, no fitted parameter.
- **form L** — linear in `Σ` through `(0, 1)` with the single slope that least-squares the two
  measured points.

**Both are run.** If the two forms give moves that differ by more than the gap between the verdict
bands below, the arm is reported as **not decided by this interpolation**, and that is a result, not
a failure to be patched.

### The re-read

The thirty-six lowest bandpowers at `ℓ = 100–207`, the same thirty-six as `r7866`, removed as
before; the move re-read on the corrected spectra. The uncorrected move is `−20.09` meV and the
reference's is `−0.12`.

### REGISTERED OUTCOMES — all three reachable

Let `m` be the corrected move in meV and `f = 1 − |m|/20.09` the fraction of the move the
correction removes.

| | condition | verdict |
|---|---|---|
| **Ⓐ** | `\lvert m \rvert ≤ 0.36` meV, i.e. `f ≥ 0.982` — within 3× the reference's own move | **the amplitude excess IS the lean** |
| **Ⓑ** | `f ≤ 0.30` | **they are two things** — the excess does not carry the lean |
| **Ⓒ** | `0.30 < f < 0.982` | **partial** — reported as the fraction with its band across the two forms, and called neither Ⓐ nor Ⓑ |

**⛔ The thresholds are set here and are not moved after a result.** If the number lands just outside
a band, the band stands and the verdict is the one the band gives.

---

## ③ THE EPOCH-CONSISTENT NEUTRINO PERTURBATIONS

### The switch

`NUPERT`, default `0`. **`NUPERT=0` is byte-identical to the present file** — registered as an arm:
a control spectrum computed with the switch absent and with `NUPERT=0` must agree bit for bit.
`NUPERT=1` requires `NUFD=1` and `MNU ≠ 0`; it refuses otherwise rather than running a half-repair.

### The approximation, named

**The Fermi–Dirac fluid approximation**: the massive species is carried as a fluid whose equation of
state and sound speed are its own Fermi–Dirac ones at each epoch,

```
w(a)   = NUW_of(ln a) = p_ν/ρ_ν   from the file's own FD integrals
c_s²(a) = w(a)                     the adiabatic choice, exact at w = 1/3 and → 0 as the species cools
```

with **no fitted quantity anywhere**. Three changes, each reducing to the present line at `w = 1/3`:

1. **The weight.** The species enters the potential's source at `Onu_of(a)/_rt` instead of
   `FNU·(OR/a⁴)/_rt` — its own FD energy weight at each epoch, radiation-like while relativistic and
   matter-like after.
2. **Continuity.** `δ_ν' = −(1+w)θ_ν + 3(1+w)Φ'`. At `w = 1/3` this is the present line exactly.
3. **Euler.** `θ_ν' = −H(1−3w)θ_ν − (ẇ/(1+w))θ_ν + k²(c_s²/(1+w))δ_ν − k²σ + k²Ψ`. At constant
   `w = 1/3` the first two terms vanish and `c_s²/(1+w) = 1/4`: the present line exactly.

**`OCDM` is NOT changed.** The species is now its own correctly-weighted sector; adding ω_ν back
into the clustering matter would count it twice. The registered check is S8's closure: under
`NUPERT=1`, `Dclose` must vanish to the spline's own accuracy.

### What the approximation does not do — declared, and bounded by measurement

The `F_ℓ` ladder is left as the massless free-streaming ladder, so `σ_ν` is the relativistic shear at
all epochs. That is exact while the species is relativistic and wrong after. **Rather than hide it,
both ends are measured:** the repair is run with the ladder as it stands and again with the species'
shear switched off below its own non-relativistic transition, and the spread between the two is
reported as the approximation's own uncertainty on `A`.

### VALIDATION, BEFORE ANY LIMIT

`A` and `ε` refitted against CAMB at `Σ = 0.30` and `0.60` eV, by `r7874`'s own fit on `r7874`'s own
legs, with the `ε` allowance measured the same way.

| | condition | verdict |
|---|---|---|
| **Ⓓ** | `A` falls from `1.152` and `1.296` to within `0.03` of 1 at both sums, **and** EE's agreement does not worsen by more than its present 1–5 per cent band | **the repair is the physics; the arm of record may follow** |
| **Ⓔ** | `A` moves toward 1 by more than a third of its excess at both sums but stays outside `0.03` | **the repair is part of it** — reported as the fraction of the excess removed, with the ladder spread |
| **Ⓕ** | `A` moves by less than a tenth of its excess at either sum | **the defect is elsewhere, and that is the finding** |
| **Ⓖ** | `A` moves **away** from 1, or EE's agreement worsens past its band | **the repair is refuted on its own validation** and no limit is read through it |

**⛔ No limit is read through `NUPERT=1` unless Ⓓ. Ⓔ, Ⓕ and Ⓖ all end the revision at the
validation, and ④ does not start.**

---

## ⌗ WHAT WOULD MAKE THIS REGISTRATION WRONG

- A clause of ① that does not hold on the source.
- `NUPERT=0` not byte-identical.
- `Dclose` not vanishing under `NUPERT=1`.
- The two `A(Σ)` forms in ② disagreeing by more than the verdict gap — reported as undecided.
- A threshold in any table above being different in the result than it is here.
