# r7852 (60) — the lensing fault is the transfer, and the landed normalisation is a cancellation

**Order `r7849`**, node 69: reconcile this instrument's lensing potential with CAMB at the control's
fixed cosmology, term by term; locate the −14 to +28 per cent shape difference to its term; repair it
there; show the nine bandpowers at or near the reference's 0.98 per dof; and only then re-read the
control. Then compare against `cc66`'s BAO rerun when it lands.

`PREDICTION.md` was committed and pushed at `414b989bd`, eleven arms, before a line of the
computation existed.

---

## The answer in three lines

1. **The fault is the TRANSFER the instrument hands over at the carry start** — 99.80 per cent of the
   source difference, and the source is 98.47 per cent of the whole. The projection carries 0.49 per
   cent; the binning 1.04. **The growth was already right to two per cent**, so three revisions of
   growth repair were repairing a term that was not broken.
2. **The transfer is wrong because the instrument's `Φ` keeps decaying through matter domination
   instead of freezing** — by a factor 1.49473 at the pivot between two handovers and only 1.05275 at
   the largest scales, still moving 4.3 per cent over the last interval where the one omitted term is
   0.4 per cent of the budget. That wavenumber dependence **is** the shape disagreement.
3. **No handover fixes it.** The shape and the absolute normalisation order the handovers oppositely
   and monotonically, and the landed handover's normalisation is right only by a **cancellation** of
   two errors that closes to 1.36 per cent. ⇒ The repair belongs in the instrument's potential
   evolution, which recalibrates every spectrum the corpus rests on and is 69's to order.

---

## ⓪ The controls, because without them nothing below is a reading

**The positive control failed on this file's first version and that is why it exists.** This
revision's projection must reproduce, exactly, the banked run of the code it replicates. Its first
draft did not — by a factor **eight thousand** in the top bandpower — because it clipped the
wavenumber *before* dividing by its cube instead of only inside the power lookup. The two `k`s are
not the same `k`: the clip belongs to the source and the `1/k³` keeps the true value. Every term
share computed before the control passed was a measurement of this file's own bug. It now reads
**0.000e+00** relative over all thirty-six multipoles.

**The reference's Weyl transfer carries a squared wavenumber, and which form is the potential power
is measured rather than asserted.** The `k⁻⁴` form reproduces CAMB's own spectrum to 0.9983, 1.0007
and 1.0012 at three multipoles; the other is out by 2.8e-05 to 6.5e-03, so the seed cannot pass by
accident. ⚠ The first draft of the seed's *criterion* was wrong too: a form out by a factor ten
thousand has a ratio-minus-one of one, which a threshold of ten reads as agreement, so a holding seed
was reported as broken. It is a ratio test now.

**Both sides are linear.** CAMB's lensing potential is non-linear by default and this instrument has
none, so CAMB is forced to `NonLinear_none`. Left alone, that confound put a 4.2 per cent error at
the top multipole into the *projection*'s column, where it did not belong.

---

## The decomposition — Ⓐ① holds

| | what it isolates | share of the movement |
|---|---|---|
| **T1 the source** | the 3D power of the lensing potential | **98.47 %** |
| **T2 the projection** | Limber, the kernel, `χ(z)`, the clip, the multipole spline | 0.49 % |
| **T3 the bandpowers** | the `[L(L+1)]²/2π` convention and the nine windows | 1.04 % |

Closure `1.665e-16`. The source's own two factors are measured **not to interact**: worst
interaction `4.166e-04` against a total movement of `0.929`, so the product decomposes legitimately
rather than by assumption.

| | `χ²` per dof on the nine bandpowers |
|---|---|
| **A** instrument source, instrument projection | **2.048681** |
| **B** CAMB source, instrument projection | **1.070949** |
| C CAMB source, CAMB projection, instrument bins | 1.076675 |
| **D** CAMB exact, exactly binned | **1.066836** |

⇒ **Fed a correct source, the instrument's whole projection reproduces the reference to four parts in
a thousand.** The projection is not the fault.

### Ⓑ② FAILED — and the failure is the finding
Registered: the source agrees to better than ten per cent over the wavenumbers the kernel weights.
Measured, each normalised at `k = 0.05`: **+111.2 %** at `k = 1.2e-3`, +83.90 % at `5e-3`,
+34.82 % at `1e-2`, +12.98 % at `2e-2`, +3.41 % at `0.1`, +5.54 % at `1.0`.

### Ⓒ③ FAILED on both halves — **this seat registered the projection as the fault and it is not**
Registered: the projection carries the majority, and the wavenumber clip is worth more than ten per
cent at the top bandpower. Measured: **0.49 per cent** and **0.17 per cent**. The registered
expectation was backwards, and it is reported as refuted rather than reframed.

### Ⓓ④ FAILED on both halves
Registered: Limber underestimates at the lowest bandpower by more than three per cent, falling
monotonically. Measured: **−0.16 per cent** at `L = 28.1`, **+0.58** at `L = 377.3`, and **not
monotone**. Once the reference is linear, Limber on its own source is good to better than six parts
in a thousand across the band.

### Ⓔ⑤ FAILED, marginally
Registered under half a per cent. The eight lower bandpowers are within 0.107 per cent; **the top is
+0.71 per cent**, and it is located in the instrument's own 36-node multipole spline at the top of
the band, not in the convention.

### Ⓕ⑥ HOLDS, as a bound
The deflection is sourced by `(Φ+Ψ)/2` and this instrument projects `Φ`. The two are bounded in the
reference, where both are available at the same `(k, z)`: worst **2.29e-04**. ⚠ That bounds what the
variable choice can account for; it is **not a reading of the instrument's own `Φ − Ψ`**, which is
not a state it carries, and this arm does not pretend otherwise.

---

## Where the transfer goes wrong

**The super-horizon value is right.** At the smallest mode and the landed handover the instrument
reads `Φ = −0.901020` against the analytic `−9/10`. So the initial conditions and the super-horizon
evolution are correct to one part in a thousand, and what is wrong is the suppression's **shape in
wavenumber**.

**And it has not frozen.** `Φ(k, η)/Φ(k, η = 4000)`, on the instrument alone:

| `k` [/Mpc] | `η=500` | `914` | `1400` | `1893` | `2500` | `3200` |
|---|---|---|---|---|---|---|
| `0.00099` | 1.05275 | 1.02830 | 1.01617 | 1.00989 | 1.00543 | 1.00232 |
| `0.00505` | 1.21991 | 1.12840 | 1.08066 | 1.05518 | 1.03362 | 1.01564 |
| `0.01968` | 1.45496 | 1.29049 | 1.20183 | 1.13487 | 1.08178 | 1.03859 |
| `0.05006` | 1.49473 | 1.31859 | 1.21543 | 1.15037 | 1.09091 | 1.04191 |
| `1.00000` | 1.53885 | 1.33177 | 1.22086 | 1.15174 | 1.09291 | 1.04296 |

The last interval alone still moves **4.3 per cent**, where the radiation share — the one thing the
growth equation omits — is **0.4 per cent**. A term that is four parts in a thousand of the budget
cannot drive a move ten times its own size.

**The source splits, and the growth was already right.** Swapping only the transfer: **1.071326** per
dof. Swapping only the growth: **2.055264**. Neither: 2.048681. The growth itself agrees with the
reference to between **0.797 and 2.106 per cent** at every mode over the whole interval.

---

## Ⓖ⑦ — it passes as registered, and the criterion was the wrong test

The handover is a switch this revision owns. Scoring the nine bandpowers at **thirteen** handover
times, with nothing else moved:

| `η` | `z` | rad/matter | per dof | preferred/held | per cent low |
|---|---|---|---|---|---|
| 60 | 6979.33 | 2.024 | 31.0007 | 0.0675 | 93.25 |
| 200 | 1696.84 | 0.492 | 2.7478 | 0.2152 | 78.48 |
| 300 | 996.12 | 0.289 | 1.1940 | 0.3009 | 69.91 |
| **400** | **667.27** | **0.194** | **0.8913** | 0.3641 | 63.59 |
| 500 | 482.20 | 0.140 | 0.9168 | 0.4126 | 58.74 |
| 914 | 188.06 | 0.055 | 1.0706 | 0.5441 | 45.59 |
| 1400 | 91.51 | 0.027 | 1.1630 | 0.6406 | 35.94 |
| 1893 | 53.55 | 0.016 | 1.3095 | 0.7122 | 28.78 |
| 2500 | 32.06 | 0.010 | 1.5173 | 0.7818 | 21.82 |
| 3200 | 19.99 | 0.006 | 1.7670 | 0.8471 | 15.29 |
| **4000** | **12.83** | **0.004** | **2.0487** | **0.9096** | **9.04** |

**An interior minimum at `η = 400`, bracketed on both sides, at 0.891264 per dof — below the
reference's own 1.066836, and a factor 2.299 better than where the handover sits.** On the landed
scoring path (the predecessor's initial-condition growth) the same move gives **1.201007** against
**2.131339**. Both pass the registered `≤ 1.3`.

⚠ **`r7850`'s ruling — the handover belongs as late as the instrument can afford — is out by a
factor 2.3 on the shape.** It weighed one error of two.

### ⌗ And why the criterion was the wrong test

**The lensing side of the joint fit carries no fitted amplitude.** `phiphi.py`'s own header is
explicit: `CMB = AMP e^{−2τ} shape_cmb` and `phiphi = AMP shape_phiphi`, one primordial normalisation
shared by both — which is the entire mechanism by which `τ` acquires reach. So the joint fit tests
the **absolute** normalisation while a `χ²` with one amplitude fitted tests only the **shape**, and
the two columns above run in opposite directions, strictly and monotonically, over the eight
handovers from the shape's minimum to the latest probed. Below that minimum both are bad, so there is
no compromise at either end.

### ⌗ The cancellation

| from two records that share no quantity | |
|---|---|
| the instrument's spurious `Φ` decay, `η = 500 → 4000`, in power | **2.23420** |
| the normalisation deficit the later handover must cover | **2.20426** |
| agreement | **1.36 per cent** |

⇒ **The landed handover's absolute normalisation is right by a cancellation of two errors, not by
correctness.** That is why no choice of handover makes the shape and the normalisation right at once,
and why the repair belongs in the potential's evolution rather than in the switch.

---

## Ⓗ⑧ — delivered, and it rules against the repair

Ⓖ⑦ passed, so the arm registered conditional on it is owed. At the handover that minimises the shape:

| | 95 % limit (meV) | effective mass (meV) | joint `χ²`min | below 59 / 64 meV |
|---|---|---|---|---|
| `η = 4000` (`r7850`) | **100.4021 ± 0.3533** | **+21.913 ± 44.423** | **570.3427** | 70.51 % / 75.20 % |
| `η = 400` (this revision) | **583.9810 ± 0.2036** | **+532.588 ± 32.475** | **740.6253** | **0 % / 0 %** |

On healthy chains: every direction below 1.0002 on `R̂`, every effective sample size above 55 000,
acceptance 0.2309 and 0.2240, the minimum **not** on a bound, no direction with unmeasurable
curvature, and the six chains' own limits spanning 1.283 meV against a Monte-Carlo error of 0.2036.

⇒ **So the handover is NOT changed and the control's limit of record stands at `r7850`'s.** A repair
that improves the shape by 2.3 and worsens the joint fit by 170 in `χ²` is not a repair.

⌗ **The same grid through the growth *before* the predecessor's initial-condition repair is worse
still at this handover, and its run record says so in its own guard fields:** `minimum_on_a_bound`
**true**, `curvature_unmeasurable_in` **`['MNU', 'TAU']`**, the minimum at `Σ = +0.600` eV — the
model's own upper edge — with `τ = 0` at `χ²` **`1413.3085`**, and both of those directions taking
the stated fallback widths. Its nominal 95 per cent figure, `599.8626 ± 0.0058` meV, is the grid's
edge and not a limit.

⚠ **So no figure from that run is reported here as a limit, and the receipt pins only its guard
flags.** A minimum on a bound is not a measurement of where the minimum is — and this seat has
already had one guard pass a chain frozen in exactly the direction its result was read off. The run
is in the record for what it is: the alternative growth, at this handover, pressed against the edge
of the grid, with the apparatus saying so unprompted.

---

## Ⓘ⑨ The cost, with its configuration beside every number

Every timing carries `ETAREF`, `NKP`, `NK`, `NOPROJ`, the clip, the clamp and the multipole count —
the defect this line found in `r7848`, where a cost was understated by a factor 16.5 for exactly that
omission. ⌗ **And the cost is set by the end time, not the mode count:** the same 220-mode solve
costs about **700 s** to the landed handover and about **12 s** to the repaired one, which is why
thirteen handovers were affordable at all.

Two record defects of this revision's own, found and fixed here: the banked solve was keyed by its
mode count and not by its output times, so a second run would have read the first's cache and
reported its times as the ones asked for; and the record written beside it was not keyed at all, so
the second run overwrote the first. **Keyed in one place and not the other is not keyed.**

---

## Ⓙ⑩ `cc66`'s reference, and the BAO rerun

**Probed, not taken on the page's word** — this line has found three stated absences false in three
revisions. **`cc66`'s reference HAS landed**: 82.890 meV on 613 bins with the nine bandpowers and a
stated `τ` prior of 0.054 ± 0.007. **The BAO rerun 69 ordered on top of it has NOT.** ⚠ And
`cc66`'s own record states its bin set is not this harness's 555 and is not reproducible there, so
the two limits are **not** on identical data and nothing here treats them as if they were.

---

## ⇒ Recommendation

**Order the potential's evolution, not another handover.** The instrument's `Φ` decays through matter
domination when it must be constant; that single defect is both the shape disagreement and the
normalisation deficit, and the landed configuration hides it by cancellation. Until it is fixed:

- no limit read through this instrument's lensing term is a measurement of anything but the
  cancellation, including the three this line has reported;
- the handover stays where it is, because moving it exposes the deficit the decay was covering;
- and the fix touches the shared hierarchy, so it recalibrates every spectrum in the corpus. **That
  is 69's to order and not this seat's to take.**

`P15` is untouched, and 72's batch still waits.
