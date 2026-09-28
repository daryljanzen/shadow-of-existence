# r6959 ⓵ᵇ/⓵ᶜ — WHAT IS PREDICTED, AND WHAT WOULD REFUTE IT, WRITTEN BEFORE THE SWAP IS RUN

*Committed ahead of the taper runs on purpose. `r6959` ⓵ᵇ asks for the size **in advance** and ⓵ᶜ asks
what would **refute** it; the only way either is checkable afterwards is if the statement is in the
history before the number is. `cc66.41`'s cross term is the failure mode being designed against: it
accounted for the excess only once the excess was known.*

## THE HYPOTHESIS, IN THE FORM THAT CAN FAIL

`r6959`'s candidate is that the arm–control contrast excess is carried by **the transfer's own
normalisation across the visibility window** — the source's conformal-time dependence, not a phase and
not a scale. Written as a mechanism, that is **two** channels and they have different signatures in
$q = \ell/\ell_A$:

* **Ⓐ PHASE SMEARING.** The oscillating source is $A(\eta,k)\cos(k\,r_{s,\rm leaf}(\eta)+\varphi)$, so
  integrating it across a window of finite spread in $r_{s,\rm leaf}$ multiplies the oscillation, and
  not the envelope, by
  $$\mathcal D_X(q)=\Big|\int a_X(\eta)\,e^{\,i k s(\eta)}\,d\eta\Big|\Big/\int a_X(\eta)\,d\eta,
    \qquad k=\pi q/r_{s,X},\quad s=r_{s,\rm leaf},$$
  with $a_X=\sqrt{w_{\rm md}}$ the measured amplitude weight of the monopole-plus-Doppler part over
  $\pm3$ FWHM of the visibility. ⇒ **Predicted excess from this channel alone:**
  $\mathcal R_1(q)=\mathcal D_{\rm cr}(q)/\mathcal D_{\rm lcdm}(q)$.
* **Ⓑ TERM MIX.** The window's shape also fixes how much Doppler and how much ISW ride with the
  monopole at each $\eta$, and that is a normalisation difference too. ⇒ Measured as the
  $\eta$-integrated fractional power in each term per band; reported, and **not** used as a free
  coefficient.

⌗ **The two are distinguishable without any fitting, because Ⓐ must vanish at long wavelength and Ⓑ
need not.** A smearing is a characteristic function: $\mathcal D\to1$ as $k\to0$ identically, so
$\ln\mathcal R_1$ is proportional to $q^2$ through the origin. A term-mix difference has no such
requirement.

## THE NUMBERS PREDICTED IN ADVANCE

1. $\mathcal D_{\rm cr}(q)>\mathcal D_{\rm lcdm}(q)$ — the arm is the **less** smeared of the two,
   because `Jac` $=H_{\rm stack}/H_{\rm leaf}$ runs $0.789$–$0.913$ across the arm's window and is
   identically $1$ on the control, so the arm accumulates less phase per unit of the conformal time
   the kernel is written in.
2. $\mathcal R_1(q)$, band by band on the contrast statistic's own bands
   (`ED = arange(0.85, 5.76, 0.7)`), against the measured excess
   $1.0215,\,1.0574,\,1.0519,\,1.0606,\,1.0748,\,1.0659,\,1.0762$ (`r6941_fine_*`, `cc66.46`).
3. **The swap.** Tapering the control with `SRCTAPER` $=\alpha_c$ solved so its amplitude weight's
   spread in $r_{s,\rm leaf}/r_s$ equals the arm's multiplies the control's contrast, band by band, by
   $\mathcal D^{\rm taper}_{\rm lcdm}(q)/\mathcal D_{\rm lcdm}(q)$ — computed from the measured weight
   times the known taper, with no free parameter. By construction that factor is $\mathcal R_1(q)$, so
   **the excess should close to unity within the tolerance in R3 below.**
4. ⚠ **And one tolerance stated in advance rather than discovered.** The prediction is on the
   *transfer's* oscillation; the contrast is measured on $D_\ell\propto T^2$, whose oscillating part is
   $2T_{\rm osc}T_{\rm smooth}+T_{\rm osc}^2$. So a factor $f$ on $T_{\rm osc}$ moves the contrast by
   between $f$ and $f^2$. **The predicted contrast response is the interval $[\mathcal R_1,\mathcal
   R_1^2]$ and the test is whether the run lands in it**, not whether it hits a point.

## WHAT WOULD REFUTE IT — ⓵ᶜ

* **R5 — SIGN.** $\mathcal D_{\rm cr}<\mathcal D_{\rm lcdm}$ in the measured functions. Refuted
  outright: the channel would predict a deficit where a $6\%$ excess is measured.
* **R1 — SHAPE.** A straight-line fit of $\ln(\text{measured excess})$ against $q^2$ has an intercept
  at $q^2=0$ exceeding **half** the measured excess at the top band. A smearing channel cannot supply
  a $q$-independent offset, so more than half the effect would be outside it whatever $\mathcal R_1$
  comes to. ⇒ *Refutes the candidate as the WHOLE channel; the part that survives is the $q^2$ slope.*
* **R2 — SIZE.** $\ln\mathcal R_1$ at the top band outside $[\tfrac12,2]\times$ the measured
  $\ln(1.0762)$. Under: not the channel. Over: **the `cc66.40` failure repeated** — a channel that
  over-delivers is not the one that delivers.
* **R3 — THE SWAP.** The tapered control's contrast ratio to its own untapered value outside
  $[\mathcal R_1^{2}/1.5,\ 1.5\,\mathcal R_1]$ band by band. That is the interval of ⓵ᵇ4 widened by
  half again, and a miss outside it means the measurement did not predict the size.
* **R4 — THE COMB AND THE DEPTHS.** Even a swap that closes the contrast is **not a mechanism for this
  row** if, on the same tapered control, any of
  * the four peak positions move by more than the sky's own locating width at that peak
    (`PO-47`: $2.36$ at $\ell_4$),
  * $\ell_1/\ell_A$ moves by more than one sky locating width in $\ell_1$,
  * the anchored trough depths move **away** from the sky's by more than the contrast excess the taper
    removes,
  is true. *A mechanism that fixes the contrast and breaks the comb is a different object.*
* **R0 — THE NULL.** `SRCTAPER=0` must return a bit-identical spectrum, and a taper solved for
  $\sigma_{\rm target}=\sigma_{\rm own}$ (coefficient $0$) must change nothing. If the knob moves the
  spectrum where it should not, none of the above is readable.

⌗ **Path provenance.** Every number above is on the **HIERARCHY** path (`LOS=1 HIER=1`), which is where
`_project` — and therefore `SRCETA` and `SRCTAPER` — is reached at all. `PO-47`'s $2.36$ and the sky's
binned spread are taken as given from the line-of-sight quartet's own source and are not recomputed.

⌗ **No detection language.** The $1.8$ of `cc66.46` is one statistic's spread. If the swap moves it,
the number it moves to is still one statistic's.
