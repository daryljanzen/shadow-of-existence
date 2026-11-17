# r7816 (60) — PRE-REGISTRATION: the joint Planck + ACT tail-tilt measurement

**Order `r7815` (69):** *"Register, then build, the joint Planck + ACT tail-tilt measurement, with the
shared sky's covariance handled. Report the signature's distance from the sky's tilt on that joint
likelihood. 70 banks the bandpowers and covariances in your harness layout. Tell 70 exactly what you
need."*

Committed and pushed **before** anything is measured. The data are not in this tree yet; what is
registered here is the construction, the arms, and the request.

---

## 0. THE ORDER'S PREMISE HOLDS, AND NOT FOR THE REASON I FIRST READ INTO IT

The order says the joint arm *"can be built now from public data"*. **It can — but not by any
construction I would have chosen, and the obvious one is unavailable.**

**There is no public Planck × ACT cross-covariance.** `DR6`'s own power-spectrum paper
(arXiv:2503.14452v2 §VI.3) says, in terms: *"We neglect correlations in TT in the 600<ℓ<1000 range
where ACT and Planck overlap; the Planck uncertainties are smaller in this angular range,"* and lists
including that covariance as **future work**, worth `<5 %` on `σ(N_eff)`.

⇒ **So "the shared sky's covariance handled" cannot mean "computed".** What the collaboration does
instead is cut by multipole until the neglected correlation is small: the baseline `P-ACT` uses
**Planck high-ℓ TT only at `ℓ < 1000`** (and `TE/EE` at `ℓ < 600`) *"since there is substantial sky
overlap between the two surveys"*.

**And that construction is SHIPPED, not reconstructed.** The DR6 CMB-only likelihood installs it as
a named dataset variant — `cobaya-install act_dr6_cmbonly.PlanckActCut`, *"if you want to use the
Planck dataset cut at the ACT multipole"*. ⇒ *So the arm that does not double-count is the
collaboration's own, and this seat does not have to invent or defend a split.*

### ⛔ AND ONE LABEL DENOTES TWO DIFFERENT PRESCRIPTIONS — CHECKED BEFORE IT WAS USED

"The ACT–Planck multipole cut" is **not one number**:

| release | prescription |
|---|---|
| `DR4` | ACT TT **below `ℓ = 1800`** not to be combined with Planck, from a Fisher test of the error understatement |
| `DR6` | **Planck TT cut above `ℓ = 1000`**, ACT kept from its own per-array `ℓ_min` (`600` PA6 f150, `800` PA5 f150, `1000` the rest), `ℓ_max = 8500` |

**Had `DR4`'s number been carried into `DR6`, this revision would have reported the window as
undecidable**: `PO-24`'s displacement lives on `ℓ 700–1760`, and "no ACT below `1800`" together with
"no Planck above `1000`" leaves `1000–1760` covered by neither. ⇒ *The window is decidable only
because `DR6` replaced the prescription, and that is a fact about which release is being read.*

⇒ **GUARD (this corpus's own, applied): before two stretches are identified by a label, check how
many-to-one the label is on the object.** Here the label is one phrase over two releases, and the
two disagree by `800` in `ℓ`.

---

## 1. THE CONSTRUCTION, FIXED BEFORE THE MEASUREMENT

**The joint arm takes each multipole from exactly one experiment:**

- **Planck `plik_lite` TT** on bins with `ℓ_hi < 1000` — the harness's present data, unchanged;
- **ACT DR6 CMB-only (foreground-marginalised) TT** on bins from `ℓ ≥ 1000`;
- **no cross-covariance term, because no bandpower pair shares a multipole.**

⌗ The residual shared-sky correlation between *different* multipoles of the two experiments is the
part `DR6` neglects and this construction inherits. **It is inherited explicitly, not silently**, and
Ⓕ⑥ below registers it as a stated limit rather than a handled effect.

**What this changes about the metric.** The published `PO-24` figures score the signature against
**Planck TT `100–1758`**. The joint arm replaces Planck with ACT over `1000–1760` — *the damping tail,
where the signature lives*. ⇒ **It is a different measurement of the same clause, not a tightening of
the old one**, and the two are reported side by side rather than one superseding the other.

---

## 2. THE ARMS — each a comparison, each with a reachable negative

**Ⓐ① The data arrive as the request specified, and the layout difference is real.** The ACT product
is one FITS file carrying bandpower means, covariance and **window functions**; `plik_lite` carries
`blmin`/`blmax`/`bweight` top-hat ranges. The harness's `bin_spectrum` assumes the top-hat form.
*Negative, reachable:* ACT's binning turns out expressible as top-hats with weights, in which case no
new binning path is needed.

**Ⓑ② The split is the collaboration's, verified against the shipped dataset and not against the
paper's prose.** The `ℓ` at which Planck stops and ACT starts, read off the banked product.
*Negative, reachable:* the shipped cut is not `1000`, in which case the prose and the product
disagree and the product wins and is reported.

**Ⓒ③ No bandpower pair in the joint arm shares a multipole.** Asserted by intersecting the two bin
lists. *Negative, reachable:* an overlap survives, and then a cross-covariance **is** needed and this
route is blocked rather than approximated.

**Ⓓ④ ACT is more precise than Planck where it replaces it.** Per-bin `σ` compared on the overlap
region the construction hands to ACT. *Negative, reachable, and it would matter:* ACT is **less**
precise there, in which case the joint arm is a worse ruler than Planck alone and the route does not
decide `PO-24` — **reported as such, not worked around.**

**Ⓔ⑤ The measurement: the signature's distance from the sky's tilt on the joint arm.** The signature
is `S(ℓ) = exp[−(r²−1)(ℓ/ℓ_D)²]` at `r = 1.0926`, `ℓ_D = 1489.5783`; the comparison is the free
power-law tilt the joint data prefer against the tilt the signature requires, in units of the joint
likelihood's own `σ`. **The strict `2σ` rule is applied to that number and to nothing else.**
*Registered as a comparison, not a prediction of the outcome:* either the distance exceeds `2σ` or it
does not, and **both are reported as measured**.

**Ⓕ⑥ The inherited limit is stated with its size, not waved at.** `DR6`'s own estimate of what
neglecting the Planck×ACT covariance costs — `<5 %` on `σ(N_eff)` — is recorded beside this result as
the nearest published bound on the approximation this construction inherits. *Negative, reachable:*
no such published bound is found on re-reading, in which case the limit is recorded as unquantified.

**Ⓖ⑦ The joint arm reproduces the published Planck-only figures where it still uses Planck.** On
bins below the split the joint arm and the present harness must agree to machine precision.
*Negative, reachable:* they differ, and then the joint arm's Planck half is not the harness's and
every comparison with the published numbers is void.

**Ⓗ⑧ Arm count asserted at the end: eight.** Any arm that fails is reported **as failed**, with its
criterion unchanged.

---

## 3. What this revision does NOT do

It does not fetch the ACT data — that is `70`'s, by the order. It does not touch another seat's
receipt, the instrument, or any gate. It does not rewrite `sec:coherence`: the paragraph already says
the row waits on a measurement, and **this revision does not yet have one**. Nothing about `PO-24`'s
status changes until Ⓔ⑤ runs.
