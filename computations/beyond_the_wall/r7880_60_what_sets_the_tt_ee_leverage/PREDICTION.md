# r7880+60 — REGISTRATION: item ① of order `r7879`, the bounded leverage diagnostic

**Committed and pushed BEFORE any measurement of this revision runs.**

`r7879` (69) ruled this line's branch **(b)** *"first, bounded to one revision"*: ask what in the
instrument sets the TT:EE response ratio, **on banks that already exist**. *"If a sector outside the
neutrinos carries a TT-heavy signature (10.8 at 0.30 eV, 6.4 at 0.60), name it. If nothing does, say
so, and (b) is closed."*

---

## READS TAKEN BEFORE THIS REGISTRATION, DECLARED

Four, all structural or already landed. **No spectrum of any candidate leg has been read and nothing
has been fitted.**

1. **The bank inventory.** Five `pol_grid*` sum-grid banks exist on the control arm, each carrying
   `lcdm_S000 / S006 / S015 / S030 / S045 / S060 / Sm06 / Sm12` and four parameter offsets at ±
   (`H0`, `NS`, `OM`, `WB`), with TT and polarisation saved separately.
2. **What each bank's own config records.** `pol_grid_bvel1_nufd_only`, `…_nufd_dneff` and
   `…_nufd_dneff044` record `BVEL=1, NUFD=1` and `DNEFF = None / 0.0293 / 0.044`. `pol_grid` and
   `pol_grid_bvel1` are an OLDER format whose config records none of those switches — for those two
   the only evidence of what they ran with is the **directory name**.
3. **The parameter offset legs are all at `MNU = 0.0`**, and of the four parameters only `NS` has its
   value recorded in the bank (`ns = 0.985` against the control's `0.965`); `H0`, `OM` and `WB`
   offsets are evidenced by the leg name alone.
4. **`r7878`'s landed leverage figures**: required `10.791` at `0.30` eV and `6.391` at `0.60`, from
   `A_TT` and `A_EE` of the arm of record; and the five arms' own leverages.

---

## ⛔ THE OBJECT HAS TO BE ESTABLISHED FIRST, BECAUSE THE LABEL IS TWO-TO-ONE

*The guard: before two stretches are identified by a label, check how many-to-one the label is on
the object.* **"TT:EE leverage" names two different quantities here, and only one of them is the one
the order's number refers to.**

- **The SUM-RESPONSE leverage.** `A_TT` and `A_EE` are fitted on `D_ℓ(Σ)/D_ℓ(0) − 1` against CAMB's
  same ratio. `10.791` and `6.391` are leverages *of this object*: the departure to be removed is a
  property of the **sum response**, not of the spectrum.
- **The SPECTRUM leverage.** How much a parameter moves `D_ℓ` itself in TT against EE, at one sum.

They are not the same object, and **a candidate measured in the second does not bound the first.**

### ⇒ AND THAT GIVES THE DIAGNOSTIC ITS SHARP FORM, REGISTERED AS AN ARGUMENT TO BE CHECKED

The sum response is a **ratio to the `Σ = 0` leg of the same configuration**. So any change whose
effect on `D_ℓ` is **independent of the sum** divides out of that ratio exactly and **cannot move the
sum response at all**, whatever its leverage on the spectrum.

> **Registered claim Ⓐ⓵:** a sector can carry the TT-heavy signature of the sum response only if its
> effect on `D_ℓ` is **sum-dependent**. ⌗ *This is an argument, not a measurement, and it is checked
> below on the one candidate the banks measure at more than one sum.*

**Consequence for the existing banks, stated in advance so it is not discovered as a result:** the
four parameter offsets are banked **only at `Σ = 0`**. The banks therefore cannot show their sum
dependence, and no reading of them can answer the order's question. That is **a limit of the banks**,
reported as one — not a finding about the parameters.

---

## THE CANDIDATE SET, ENUMERATED BEFORE IT IS MEASURED

⛔ **Closed here so that no candidate can be added after its number is seen.**

| | candidate | sums available | provenance |
|---|---|---|---|
| **⓵** | `DNEFF = 0.0293` against none | `S000 … S060` | recorded in both banks' configs |
| **⓶** | `DNEFF = 0.044` against none | `S000 … S060` | recorded in both banks' configs |
| **⓷** | `NUFD` on against off | `S000, S006, S030, S060` | the `…_nufd_off` bank's own config |
| **⓸** | `BVEL` on against off | `S000 … S060` | ⚠ **the directory name only** |
| **⓹** | the four parameters `H0`, `NS`, `OM`, `WB`, at ± | `Σ = 0` ONLY | name only, except `NS` |

⓵–⓸ are read as **sum-response** leverages, the object the order's number belongs to. ⓹ is read as a
**spectrum** leverage and is reported as a different quantity, under the limit stated above.

*The three neutrino-perturbation changes and the two sound speeds are NOT in this set: `r7878`
measured them and `r7879` has ruled on them. This item asks what lies OUTSIDE the neutrinos.*

---

## THE BAND, FIXED BEFORE THE RESULT

A candidate **carries the signature** when its sum-response leverage lies within a factor of `4/3`
of the required one **at both sums** — the same band `r7878`'s own leverage table was read on, taken
unchanged so that this revision's answer is comparable with that one. ⌗ *The required leverage
differs between the sums by a factor of `1.69` (`10.791` against `6.391`), so a candidate with a
sum-independent leverage cannot sit in the band at both; that is a property of the target and is
registered here rather than reported as a surprise.*

**And a control on every candidate, registered as a refusal:** a `±` pair must give the **same**
leverage to within the same factor of `4/3`. ⛔ *A leverage that differs between the `+` and the `−`
offset is not a property of the sector — it is a property of the step — and such a candidate is
reported as UNREADABLE rather than as carrying or not carrying the signature.*

---

## REGISTERED OUTCOMES

| | condition | verdict |
|---|---|---|
| **Ⓐ** | at least one of ⓵–⓸ sits in the band at **both** sums, and passes its `±` control where it has one | **a sector outside the neutrinos carries it — NAMED**, and whether it has any freedom left is reported beside it |
| **Ⓑ** | at least one sits in the band at **one** sum and not the other | **named as partial**, with the sum stated; `(b)` is not closed cleanly and the reason is the target's own `1.69` spread |
| **Ⓒ** | none of ⓵–⓸ sits in the band at either sum | **nothing outside the neutrinos carries it, and `(b)` is CLOSED** |
| **Ⓓ** | every candidate of ⓵–⓸ fails its `±` control or has no readable move | **the existing banks cannot answer it**, which is a limit and not a closure, and `(b)` stays open with what new leg would settle it named |

⛔ **`Ⓒ` and `Ⓓ` are different answers and are not to be collapsed.** `Ⓒ` closes `(b)`. `Ⓓ` does not.
*This enumeration is written in four mutually exclusive rows on purpose: `r7878`'s own item ① had two
rows that fired at once because the registration did not make them exclusive, and that defect is not
repeated here.* Exactly one row fires, and the receipt checks that exactly one fires.

⛔ **NO LIMIT IS READ IN THIS REVISION, under any outcome.** `r7879` puts the limit behind item ②'s
joint validation, and nothing here reaches it.

---

## WHAT IS NOT CLAIMED

- **Naming a sector is not proposing it as the repair.** `r7879` ruled `(a)` — the massive species'
  own hierarchy — to be the repair, and `(b)` is a diagnostic *"bounded to one revision"*. Whatever
  is named here is reported with the freedom question attached, and nothing is tuned.
- The fit is `r7874`'s own, executed with its rebinding **imported** from `r7876`'s `refit.py`, and
  its reproduction leg must return `1.15162`, `1.29592`, `1.01405`, `1.04630` on the landed bank
  before anything below it is readable — as in `r7878`.
