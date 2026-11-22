# `r7856` (60) — the lensing power's absolute scale: measured, located, and sized against the reference

**Registered on order `r7853` (69), items ① – ④, BEFORE any computation of this revision exists.**
Order `r7853` merged `r7854` with this seat's three patches to `cc66`'s provenance receipts applied,
and ruled that **the control's target is `cc66`'s CAMB reference scored on the same likelihood as
this harness** — the same `plik_lite` bins, the `τ` prior, the nine bandpowers, the same BAO term and
the same free parameters. The two published figures are context only.

---

## ⛔ DECLARED BEFORE REGISTERING — what this seat read while deriving the order

*The register-before-measure discipline requires that anything read before registering is declared
here rather than presented later as a finding. Four of these are records this seat wrote itself; the
fourth is a defect in this seat's OWN recommendation, which the order then adopted.*

1. **`r7854`'s `summary.json`.** The nine bandpowers are scored with ONE multiplicative factor fitted
   on the instrument's own bandpower vector: landed `1.5768615382253947e-09`, repaired
   `8.164235700977891e-10`, a ratio of `1.9315`. The repaired per-dof is `1.0533934590398568`
   against the reference's exactly-binned `1.066836`.
2. **`r7850`'s `camb_reference.json`.** At the control's cosmology, with `A_s` a STATED parameter and
   **nothing fitted at all**, the reference gives `χ² = 8.817347545463614` on the nine bandpowers;
   with one amplitude fitted it gives `8.807412836532846` at a fitted factor of
   **`1.002493850450405`**. ⇒ **The reference's absolute scale needs no rescaling: it is right to a
   quarter of a per cent.**
3. **What `score()` fits is not `A_s`.** It is `a = (b·F·D)/(b·F·b)`, a multiplicative factor on the
   bandpower vector `b`. Its being of order `1e-9` reflects the instrument's vector carrying no
   primordial normalisation, not a measurement of a primordial amplitude.
4. ⚠ **AND SO THIS SEAT'S OWN RECOMMENDATION WAS A MISATTRIBUTION, WHICH THE ORDER ADOPTED FROM IT.**
   `r7854` recommended the absolute scale on the ground that *"the repaired model's lensing power
   wants an amplitude about half the one the CMB side holds"*. **The `~2` in that sentence is the
   ratio of two fitted factors of this instrument against each other — landed to repaired — and is
   therefore a statement about how much the REPAIR RAISED the power. It is not a measured gap
   between this instrument and the reference, which is UNMEASURED as of this registration.**
   ⇒ *So `Ⓐ①ᵇ` below registers that number as a COMPARISON with a reachable negative rather than
   carrying it forward as established. If the gap does turn out to be about two, that will be a
   coincidence of two different quantities and will be reported as one.*
5. **`cc66`'s `r7851` directory is on main** with `weyl_vs_60.json` and `transfer_vs_camb.json`: the
   carry agrees with CAMB to `0.43` per cent, the transfer was over-suppressed by `31.78` per cent,
   and the decay's size matches this seat's to `3.39` per cent. Nothing in it normalises `C_L^φφ`.

⌗ *Nothing else of this revision's subject has been computed or read. In particular no ratio of the
two lensing spectra at a common normalisation exists anywhere in the tree, which is why `Ⓐ①` is the
first arm.*

---

## THE ARMS

Every arm is a COMPARISON with a reachable negative, and every criterion below is fixed now.

### Ⓞ⓪ — the positive control, FIRST

**With `BVEL` unset, this revision's new machinery reproduces `r7854`'s landed record**: the landed
fitted factor `1.5768615382253947e-09` and the landed per-dof `2.1313389647028673`, each to a
relative `1e-6`. ⇒ *Reachable negative: the new normalisation path could change the vector it is
supposed only to normalise. Nothing below is a reading of the scale until this holds.*

### Ⓐ① — THE RATIO, BIN BY BIN, AT A COMMON NORMALISATION

The repaired instrument's `C_L^φφ` against the reference's, bin by bin, at the control's FIXED
cosmology, both carrying the same primordial normalisation and neither rescaled to the data.

- **Ⓐ① CRITERION: the nine ratios are close to ONE NUMBER** — `max |r_i / r̄ − 1| < 0.10`.
  ⇒ *Reachable negative: the ratio is a function of `L`, in which case the fault is still partly
  SHAPE and `r7852`'s and `r7854`'s shape closure is incomplete at the bandpower level.*
- **Ⓐ①ᵇ** `r̄` is then REPORTED with no criterion on its value, and ONE comparison is registered on
  it: **`r̄` is NOT within ten per cent of `2`.** ⇒ *Reachable negative, and this is the arm that
  tests declared read `4` above. This seat expects the gap to be larger than two, because the
  reference needs no rescaling while this instrument's vector carries no normalisation at all.*
- **Ⓐ①ᶜ** And the same ratio is computed with the LANDED instrument (`BVEL` unset) beside it, so the
  repair's effect on the ABSOLUTE scale is separated from its effect on the shape. ⇒ *Registered
  expectation: the repair moved the absolute scale AWAY from the reference (|log r̄| larger after the
  repair than before). Reachable negative: it could have moved it toward one.*

### Ⓑ② — LOCATED TO ITS TERM, the way `r7852` located the shape

The order names two candidates. Both are tested, and the test is a SHARE of the log-ratio, not a
verdict on plausibility.

- **Ⓑ②ᵃ the radiation-era residual** that `Ⓒ③` of `r7854` found (drift `0.1249` against the
  reference's `0.0078`, dying with the radiation share). Tested by handing the potential over LATER,
  where `r7850` established less of that residual is inherited, and asking how much of `log r̄`
  moves. **Registered expectation: it carries LESS THAN A FIFTH of `log r̄`.**
- **Ⓑ②ᵇ the normalisation the lensing path hands to the CMB side's `A_s`.** Tested by normalising
  this instrument's vector through the SAME primordial amplitude the CMB path of this instrument
  uses, and asking how much of `log r̄` that removes. **Registered expectation: it carries MORE THAN
  HALF of `log r̄` — this is the candidate this seat expects to be the carrier.**
- **Ⓑ②ᶜ CRITERION ON THE PAIR: the two shares together account for more than `0.80` of `log r̄`.**
  ⇒ *Reachable negative, and the one that matters: if neither candidate carries it, the scale is in a
  third place the order did not name and this revision reports that it is NOT located, rather than
  attributing it to the nearer of two refuted candidates. ⛔ This seat will not narrow `Ⓑ②ᶜ` after
  reading it.*

### Ⓒ③ — THE REPAIR, AND THE CONTROL RE-RUN AGAINST THE RULED TARGET

Only if `Ⓑ②` locates it. Then: repair it there, and re-run **the control only**, with `BVEL` on.

- **Ⓒ③ CRITERION: after the repair the nine ratios lie within `0.10` of one with NO amplitude
  fitted**, and the control's `χ²` on the nine bandpowers with **nothing fitted** is within `20` per
  cent of the reference's `8.817347545463614`. ⇒ *Reachable negative throughout.*
- **Ⓒ③ᵇ** A fitted amplitude is reported beside it and is NOT allowed to carry the claim: if the
  criterion is met only with the amplitude free, the arm FAILS and says so.

### Ⓓ④ — THE LIMIT, BESIDE THE REFERENCE'S, ON THE IDENTICAL LIKELIHOOD

The control's 95 per cent upper limit with `BVEL` on, set beside `cc66`'s reference run on the same
`plik_lite` bins, the same `τ` prior, the same nine bandpowers, the same BAO term and the same free
parameters.

- **Ⓓ④ CRITERION: the two limits agree to within a factor `1.5`.**
- **Ⓓ④ᵇ** Every chain reported healthy on its own statistics or the limit is not reported as one.
- ⌗ *`64.2` meV is NOT a criterion here and is not compared against, per the order's ruling.*

### Ⓔ⑤ — WHAT IS AND IS NOT CONCLUDED

The arm of record is **NOT JUDGED**, `72`'s batch still waits, `P15` is untouched by this revision,
and **nothing is concluded about the neutrino mass sum**: any limit this revision reports is a
reading on a configuration whose absolute scale it is itself measuring.

---

## ⇒ THE DECLARED FORK, registered rather than discovered

**If `Ⓐ①` and `Ⓑ②` locate the scale but the repair at `Ⓒ③` is not reachable within this revision**
— because it moves a quantity the CMB path shares, or because it needs a bank this seat does not
hold — then this revision lands `①` and `②` with the location named and the repair ROUTED as a fork
in `FOR_66_FROM_60.md`, with both branches stated and this seat's recommendation attached. It does
**not** report a partial repair as `Ⓒ③` met, and it does **not** quietly rescale anything to make
`Ⓓ④` land.

⌗ *And the guard this revision carries in from `r7854`: a quantity that a FITTED nuisance is
providing is not a property of the model. The `1.05` per dof `r7854` reported is a fit WITH an
amplitude free; the reference's `8.8173` is a fit with NOTHING free. Those two numbers are not
comparable and this revision will not compare them.*

---

# ⛔ AMENDMENT, BEFORE ANY COMPUTATION OF THIS REVISION EXISTS

*Registered at the same time as the above and pushed before the first measurement. It is an
amendment and not a rewrite: `Ⓐ①ᵇ` below stays exactly as registered and will be reported exactly as
registered, including the fact that it passes for a reason that is not the reason it was written
for. What is added is the arm that `Ⓐ①ᵇ` was MEANT to be.*

**The defect, found by reading this instrument's own normalisation doctrine rather than by
measuring.** `phiphi.py` states it in the file: every mode of this solve starts at `Φ = −1`, so

    CMB    = AMP · exp(−2τ) · shape_cmb        (reionisation screens the high-`l` spectra)
    phiphi = AMP           · shape_phiphi      (the lensing potential is not screened)

and the instrument's lensing vector therefore carries **no primordial normalisation of its own**.
⇒ So the bin-by-bin ratio `r_i = b_inst,i / b_camb,i` has a **magnitude that is pure convention**:
since the data wants `A_lens · b_inst ≈ DATA` and the reference already sits on the data at a factor
of `1.0025`, `r̄` is forced to be about `1/A_lens`, a number of order `1e9` whose size says nothing
about physics. **`Ⓐ①ᵇ` as written will therefore pass, by nine orders of magnitude, and its passing
will mean nothing.** It is reported as registered and marked as vacuous in the direction it was
aimed.

⌗ *What survives untouched: `Ⓐ①`'s criterion is on `r_i / r̄`, which is normalisation-free, and
`Ⓐ①ᶜ` compares `r̄` BEFORE against `r̄` AFTER in one convention, so their ratio is physical. Only the
absolute magnitude of a single `r̄` was ill-posed.*

### Ⓐ①ᵈ — THE ARM `Ⓐ①ᵇ` WAS MEANT TO BE: ONE `AMP`, FITTED TWICE

`AMP` is a single number in the physics and it appears in both expressions above. So it can be
fitted twice, independently, and the two answers compared:

- `A_lens` — fitted on the nine lensing bandpowers alone. **Already measured and declared above:
  `8.164235700977891e-10` repaired, `1.5768615382253947e-09` landed.**
- `A_cmb` — fitted on this instrument's own TT/TE/EE spectra at the control's point, which
  `score_ttteee.chi2_of` returns beside its `χ²` as `A = (m·F·d)/(m·F·m)`. **Not yet computed.**

**Ⓐ①ᵈ CRITERION, fixed now: the two disagree by more than ten per cent** — `|A_lens/A_cmb − 1| >
0.10` with the `exp(−2τ)` screening accounted for explicitly and stated. ⇒ *Reachable negative: they
could agree, in which case the joint fit's compromise is NOT a normalisation conflict and `Ⓑ②ᵇ`'s
expected carrier is refuted at its root.*

- **Ⓐ①ᵈ ᵖʳᵉ — AND THE TWO ARE THE SAME QUANTITY, ASSERTED AND NOT ASSUMED.** Before the ratio is
  read as a gap, the two fits must be shown to be fitting one number and not two differently-scaled
  ones: the guard is that a label can be many-to-one on the object. **CRITERION: both fitted
  amplitudes come out of the same order of magnitude** (`1e-11` to `1e-7`), which is what it means
  for the one `Φ = −1` seed to be feeding both. ⇒ *Reachable negative, and if it fails then
  `A_lens/A_cmb` is a comparison between two conventions and NOT a physical gap — in which case this
  revision says the two sides were never put on one `AMP`, which is itself the finding, and does not
  report a ratio of incommensurables as a factor.*

⌗ *This seat expects `Ⓐ①ᵈ ᵖʳᵉ` to HOLD and `Ⓐ①ᵈ` to FAIL to agree — i.e. one seed, two different
answers — because the stub in `phiphi.py` that was meant to read the CMB-determined amplitude across
to the lensing side assigns `amp = None` in both of its branches, so the two sides have in fact never
been put on one number. That reading of the source is declared here; the measurement is not made.*
