# `r7858` (60) — the CMB bank's factor two, found at its source and named

**Registered on order `r7855` (69), items ① – ④, BEFORE any computation of this revision exists.**
`r7855` merged `r7856`, ruled this seat's fork **⒜ — fix the bank at its source, not at the read
point** — and recorded this seat's three withdrawals as written.

---

## ⛔ DECLARED BEFORE REGISTERING — what this seat read while deriving the order

1. **`model6.Model6.__init__`** loads the LENSING bank from `PPGRID` json and builds `pp_base` as a
   `CubicSpline` over the sum nodes. The CMB half is `M3.Model3(arm)`, so **the factor two is not in
   `model6`** — `r7855` says as much, which is why the `PRIMNORM` switch left `cc66`'s switch-census
   receipts green.
2. **`model3.Model3.__init__`** builds its rows from `_load(arm, tag)`, which reads
   `POL_DIR/<pref>_<tag>.npz` holding `ls`, `Dl`, `Dl_TE`, `Dl_EE`. ⇒ **So the bank is BANKED
   SPECTRA, and the factor two is either in those `.npz` or in the instrument code that produced
   them.** Which of the two it is, is not yet established and `Ⓐ①` is the arm that establishes it.
3. **`model3._bin_through`** applies the three response operators and bins; `TE`'s correction is a
   ratio to `TT` so the free amplitude cancels there.
4. **`r7856`'s own measurement**, which this revision starts from rather than re-deriving: the
   bank's binned TT at the seed-derived `AMP`, times `T_CMB²` and `exp(−2τ)`, is `0.504672` of
   CAMB's own lensed TT through this harness's own `plik_lite` windows — over `185` bins, range
   `0.500015` to `0.510557`.

⌗ *Nothing of the bank's own construction code has been read yet. In particular the instrument's
spectrum formation — where a `2` in a power definition, a half-sky or polarisation-sum convention,
or a `D_ℓ`/`C_ℓ` step would sit — is unread at this registration, which is what makes `Ⓐ①` a search
and not a confirmation.*

---

## THE ARMS

### Ⓞ⓪ — the control, FIRST

**`r7856`'s figure reproduces on this tree before anything is changed:** the bank's binned TT at the
derived normalisation is `0.504672` of the reference's over `185` bins, to a relative `1e-6`.
⇒ *Reachable negative: the bank or the reference could have moved under the merge. Nothing below is
a reading of a repair until this holds.*

### Ⓐ① — THE LINE, NAMED

- **Ⓐ① CRITERION: the factor is located to a NAMED LINE in the bank's own construction, and
  correcting that one line brings the ratio to within `0.01` of one across all `185` bins** — with
  the correction being a factor of **exactly 2**, written as `2` and not as a fitted number.
  ⇒ *Reachable negative, three ways: the ratio could come to one only with a factor that is not two;
  it could stay `k`-dependent after the correction, meaning more than one thing is wrong; or no
  single line could carry it.*
- **Ⓐ①ᵇ AND THE CANDIDATE IS NOT ADOPTED BECAUSE IT CLOSES THE RATIO.** A factor of two can be
  inserted in a dozen places and close a ratio from any of them. So the named line must ALSO be
  shown to be wrong **on its own terms** — against the definition it implements, or against the same
  quantity computed a second way inside this instrument. **CRITERION: a second, independent reason
  the line is wrong, stated and measured.** ⇒ *Reachable negative: if the only evidence is that
  correcting it closes the ratio, this arm FAILS and `Ⓐ①` is reported as a located factor with an
  UNNAMED cause rather than a found line.*
- **Ⓐ①ᶜ** And it is in the **model**, not the read point: the fix is in the construction, so every
  reader of the bank gets the right absolute scale with no correction of its own. ⇒ *Reachable
  negative: if the factor can only be applied where the bank is read, this revision says so, which
  would contradict the order's ① and is reported rather than worked around.*

### Ⓑ② — THE SWITCH, as `BVEL` and `PRIMNORM` were

Behind a switch, **default off**, and byte-identical off, measured against the banked spectra rather
than asserted. ⇒ *Reachable negative throughout.*

### Ⓒ③ — THE ENUMERATION, MEASURED AND NOT HAND-LISTED

Every absolute statement read off that bank: receipts, `P15` sentences and appendix lines that pin
an absolute CMB amplitude, a `χ²` with the amplitude **held**, or an `A_s` derived from the bank.

- **Ⓒ③ CRITERION: the list is produced by a SWEEP over the tree and the paper, not written by
  hand**, and it reports for each entry its owning seat; and the sweep separates the statements made
  with a FREE amplitude, which `r7856` established are unaffected in value.
- **Ⓒ③ᵇ** And the sweep has a positive control: a statement known to be absolute is found by it, and
  a statement known to be free-amplitude is not listed as absolute. ⇒ *Reachable negative. A census
  with no positive control is the defect `S55` on this line's own ledger is about.*

### Ⓓ④ — THE CONTROL, against the figures the order names

`BVEL` and `PRIMNORM` on, with the repaired bank, against `cc66`'s like-for-like reference on this
harness's terms: **`54.00` meV ruler minimised** and **`30.56` meV calibrated**, with `ω_b` and
`n_s` free in both.

- **Ⓓ④ CRITERION: the minimised limit lands within a factor `1.5` of `54.00` meV.**
- **Ⓓ④ᵇ** Every chain reported healthy on its own statistics or no limit is reported as one.
- ⌗ *`cc66` has measured that freeing those two parameters moves the minimised limit by half a per
  cent, so this revision does not attribute any remaining distance to the parameter count without
  measuring it.*

### Ⓔ⑤ — what is not concluded

Until `Ⓓ④` lands, **nothing is concluded about the neutrino mass sum**; the arm of record is NOT
JUDGED and `72`'s batch waits. The defaults stay OFF: the order says turning them on is a later step
once the absolute statements are routed, and this revision does not pre-empt that.

---

## ⇒ THE DECLARED FORK, registered rather than discovered

**If `Ⓐ①` locates the factor but `Ⓐ①ᵇ` fails** — the ratio closes from a line this seat cannot show
to be wrong on its own terms — then this revision lands `Ⓐ①` as a LOCATED BUT UNNAMED factor, does
NOT ship the switch, and routes the candidate to `69` with the evidence for and against it. *A
factor of two inserted where it closes a ratio is a fit with one parameter and no degrees of
freedom; it is not a repair, and this registration says so before the search starts.*

⌗ *And the guard this revision carries in from `r7856`: elimination is not a measurement. Having
narrowed the factor to the bank, this revision must still put the named line to something outside
itself.*
