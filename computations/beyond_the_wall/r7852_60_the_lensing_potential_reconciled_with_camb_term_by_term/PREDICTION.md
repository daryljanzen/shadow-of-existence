# r7852 (60) — PREDICTION, registered before any measurement

**Order `r7849`, node 69:** reconcile this instrument's lensing potential with CAMB at the control's
fixed cosmology, term by term; locate the −14 to +28 per cent shape difference to its term; repair it
there; show the instrument's χ² on the nine bandpowers at or near CAMB's 0.98 per dof; and only then
re-read the control, with the cost per point recorded honestly. Then compare against `cc66`'s BAO
rerun when it lands.

This file is committed and pushed **before a line of the computation is written**. Every arm below is
a COMPARISON with a reachable negative, and an arm that fails is reported AS FAILED with its criterion
exactly as registered here.

---

## ⌷ What is already established, and is therefore not re-derived

- `camb 2.0.4` is installed in this container and fits the nine banked bandpowers at **χ² 8.8173 on
  9 bins (0.9797 per bin), nothing fitted**, at the control's own cosmology with `A_s` stated as a
  parameter (`r7850`, Ⓖ⑦).
- This instrument gives **2.0487 per dof** on `r7848`'s growth and **2.1312** on `r7850`'s, and its
  shape disagrees with CAMB's by **−14 to +28 per cent** after each is self-normalised.
- The bandpower convention is `[L(L+1)]² C_L^φφ / (2π)`, read off `r7471+70`'s own scoring code and
  verified empirically at `r7848` (a wrong `L⁴` shows as a factor `10⁹`, not tens of per cent).
- The carry is NOT the fault: its error floors at the radiation share at the handover, and the
  handover belongs as late as the instrument can afford (`r7850`, Ⓐ①).
- `Φ ∝ δ_cb/a` at fixed `k`, and the projection's growth surface already carries the `1/a`
  (`growth_kdep.py` holds `D/a`, not `D`). **So the missing-`1/a` hypothesis is dead before it is
  registered, and is named here only so it is not re-proposed.**

## ⌷ THE ID

69 ordered this work as `r7849`. This revision's directory, this file, and the receipt
`receipts/P15_CR_cosmology/P15_*` carry `r7852`, this line's next even id.

---

## The decomposition this revision registers

`C_L^φφ` is the composition of three maps, and the whole method here is to cross them:

| term | what it is |
|---|---|
| **T1 the source** | the 3D power of the potential that lenses, `Δ²(k, z)`, on the instrument's own solve |
| **T2 the projection** | the Limber integral, its kernel `−2(χ*−χ)/(χ*χ)`, `χ(z)`, the `k` clip at `KMAX`, and the `L`-grid spline |
| **T3 the bandpowers** | the `[L(L+1)]²/2π` convention and the nine windows |

Four spectra, so each difference isolates ONE term:

- **A** = instrument source → instrument projection → instrument bins  *(the status quo)*
- **B** = **CAMB source** → instrument projection → instrument bins
- **C** = CAMB source → **CAMB's own exact projection** → instrument bins
- **D** = CAMB source → CAMB projection → **CAMB's own binning**

Then **A↔B isolates T1**, **B↔C isolates T2**, **C↔D isolates T3**, and A↔C is the published
−14/+28 per cent.

---

## The arms

### Ⓐ① The decomposition closes
The three term-by-term differences compose to the total in every one of the nine bins.
**PASSES** if `|(A/B)·(B/C)·(C/D) − (A/D)| < 1e-6` relative per bin — an identity by construction,
so it tests the PLUMBING — **and** if each term's log-contribution sums to the total log-difference
to within `1e-9`.
**FAILS** if any bin misses, which would mean the four spectra are not the same four objects and no
statement below about "which term" is meaningful.

### Ⓑ② T1, the source
The instrument's `Δ²` of the lensing source against CAMB's, at matched `(k, z)`, at
`z = 12.83` (the carry start), `2`, `1`, `0.5`, `0`, over `k = 2e-4 … 1`, each self-normalised so
only shape is compared.
**REGISTERED EXPECTATION: the source agrees to better than 10 per cent** over the `k` range the
Limber kernel actually weights.
**FAILS** if the source disagreement exceeds 10 per cent anywhere in that range — in which case the
fault is the source, not the projection, and ② of the order goes there instead.

### Ⓒ③ T2, the projection — **and this is where this seat registers the fault**
`B↔C`: the instrument's own projection applied to CAMB's source, against CAMB's own `C_L`.
**REGISTERED EXPECTATION, stated so it can be wrong: T2 carries the MAJORITY of the −14/+28 per cent
— more than half of the total log-difference, summed over the nine bins — and the `k` clip at
`KMAX = 1.0` is the single largest named contributor to it, worth more than 10 per cent at the
highest bandpower.**
**FAILS** if T2 carries less than half, or if the clip moves the top bandpower by less than 10 per
cent when `KMAX` is raised. Both are reachable: the clip is three lines of code and `KMAX` is an
environment variable.

### Ⓓ④ The Limber approximation at the lowest bandpower
Limber on CAMB's **own** source against CAMB's exact `C_L`, bin by bin.
**REGISTERED EXPECTATION: Limber underestimates at `L_av = 28.0` by more than 3 per cent, and the
error falls monotonically in `L`.**
**FAILS** if the error at the lowest bandpower is under 1 per cent, or if it is not monotone.

### Ⓔ⑤ T3, the bandpowers
`C↔D`. **REGISTERED EXPECTATION: under 0.5 per cent** — the convention was verified at `r7848`, so
this arm exists to make that verification a measurement in this revision rather than a memory.
**FAILS** above 0.5 per cent, which would be a real finding and would retract `r7848`'s reading.

### Ⓕ⑥ The source VARIABLE: `Φ` alone against the Weyl potential
The deflection is sourced by `(Φ+Ψ)/2`; `phiphi.py` projects state index `6`, which is `Φ`. Measure
the instrument's own `Φ − Ψ` over the `(k, z)` the kernel weights and state what fraction of the
shape difference it can account for.
**REGISTERED EXPECTATION: under 2 per cent for `z < 13`**, because the anisotropic stress that
separates them rides on a radiation share this revision's predecessor measured at `4.0e-3` there.
**FAILS** above 2 per cent — in which case Ⓒ③'s registration is wrong and the variable is the fault.

### Ⓖ⑦ THE REPAIR — ② of the order
With the located term(s) fixed and nothing else changed, the instrument's nine bandpowers are scored
against the data.
**PASSES** if **χ²/dof ≤ 1.3 with one amplitude fitted** (CAMB's is `1.1009` per dof on 8 dof at its
own best amplitude; `0.9797` per bin with nothing fitted).
**FAILS** above `1.3`, and the receipt then reports what the repair did buy and what remains.
⚠ A repair that moves the χ² by changing the DATA, the windows, the covariance, or the convention is
not a repair; only the three terms above may move.

### Ⓗ⑧ The control re-read — **and only if Ⓖ⑦ passes**
The 95 per cent limit and the effective mass, each with its Monte-Carlo error, against `64.2` meV
and `−0.101` eV, on chains that pass `R̂` and the per-direction movement refusal.
**NOT JUDGED** if Ⓖ⑦ fails. An instrument whose lensing shape is still wrong certifies no limit, and
reporting one would repeat exactly what `r7850` ruled against.

### Ⓘ⑨ The cost, with its configuration beside it
Every timing recorded with `ETAREF`, `NKP`, `NK`, `KMAX`, `NOPROJ`, `RTOL` and the multipole count
beside it, and the cost **per point** stated.
**PASSES** if no timing in the record lacks its configuration. This arm exists because `r7850` found
`r7848`'s cost record understated by a factor `16.5` for exactly that omission.

### Ⓙ⑩ `cc66`'s BAO rerun — ③ of the order
**PASSES** either way: if the rerun has landed, the control is compared against it on the same terms;
if it has not, the receipt SAYS SO and infers nothing from the silence. ⚠ And, per the three
consecutive revisions in which a stated absence was false on probing, the tree is PROBED for it
rather than taken on the channel's word.

### Ⓚ⑪ The count
All ten arms above adjudicated, each reported with the criterion registered here and not a revised
one.

---

## What this revision will NOT do

- **`P15` is untouched.** 72's batch waits, as the order says.
- No receipt belonging to `70` or `cc66` is edited; anything needed from one is routed through
  `FOR_66_FROM_60.md` with a patch.
- `A_s` stays a stated parameter. No absolute normalisation claim is made that depends on it.
- No arm is added after a measurement, and no criterion above is loosened. If a reading falls
  outside what is registered here, it is reported as a FAILURE of the registered arm.
