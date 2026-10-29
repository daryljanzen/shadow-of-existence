# `r7637+cc66` — RESULT: the re-point of my share on the arm of record, receipt by receipt

*Every figure below is **re-derived on the instrument in this container**, not quoted from `DRYRUN.md`.
Versions match `requirements-ci.txt` exactly (`camb 2.0.4`, `numpy 2.4.6`, `scipy 1.17.1`,
`sympy 1.14.0`, `mpmath 1.3.0`). Each moved pin is **perturbed until it goes red** before it is reported.*

**How a re-point is expressed, and why.** Each receipt names its arm-of-record spectrum explicitly, via a
per-arm suffix map — `AOR = {'lcdm': '', 'cr': '_leafrec1'}` — rather than the namesake file being
overwritten. ⌗ *This is derived from the order rather than assumed: `r7637` asks for a **partial**
re-point — 18 now, 23 held until `r7637_70_own_comb_statistic` lands. A wholesale swap of the namesake
spectra cannot be partial, and would drag the held family onto the new arm too, which would defeat the
hold. So the move has to be per receipt.* The control carries no suffix because the control does not move.

---

## ⓵ `P15_the_shared_fraction_does_not_mean_what_i_said_and_the_peak_trough_pattern_is_the_arms_alone`

**Re-pointed and green: `rc=0`, 14 PASS, 0 FAIL.** One pin moved; it is re-derived, tightened, and shown
failable twice.

| figure | old arm | arm of record |
|---|---|---|
| shared fraction | `73.1%` | **`71.8%`** |
| cosine of the whitened residuals | `+0.855` | **`+0.848`** |
| arm's excess over the control | `+105.08` | **`+109.02`** |
| of which the model difference carries | `77.3` | **`81.8`** |
| the cross term | `+27.8` | **`+27.2`** |
| arm chi² over 179 bins | `282.96` (`1.581`/bin) | **`286.89`** (**`1.603`**/bin) |
| ‖m_CR − m_control‖ | `8.79` | **`9.04`** |
| ‖r_CR‖ | `16.82` | **`16.94`** |
| ‖r_control‖ | `13.34` | `13.34` (the control does not move) |
| diagonal: corr / slope / **rms ratio** | `+0.8373` / `1.137` / `1.357` | **`+0.8240`** / **`1.145`** / **`1.388`** |
| whitened: corr / slope / rms ratio | `+0.8548` / `1.078` / `1.261` | **`+0.8478`** / **`1.076`** / **`1.269`** |
| peak/trough, diag · whitened | `+0.36/−0.51` · `+0.42/−0.52` | **`+0.38/−0.56`** · **`+0.42/−0.56`** |

**⛔ THE ONE PIN THAT MOVED, AND WHAT IT COSTS ME.** The receipt pinned *"the RMS RATIO reproduces (1.36
against 1.34)"* at `|x − 1.34| < 0.03`. On the arm of record the ratio is **`1.388`**, which is `0.048`
from `r6881`'s quoted `1.34` — **outside the band**. ⇒ *So of `r6881`'s four diagnostics, the one that
reproduced on the old arm no longer does, and **none of the four survives**.*

**I did not widen the tolerance to keep it green**, which is the one move this pin forbids. The claim is
re-worded to what is measured and the pin is re-cut on the measured value to `7e-4`
— `max(0.5·10^-3, 5e-4·1.388)`, the pin rule — **and** on its distance from `1.34`, so it cannot be
satisfied by a drift back toward the quoted number.

⇒ **This strengthens the receipt's verdict rather than weakening it**: its headline is that `r6881`'s
composite reading fails at its premise, and on the arm of record it fails more completely.

**PERTURBED UNTIL RED, twice and independently:**

| perturbation | rms ratio | pin |
|---|---|---|
| the pointer reverted to the old arm | `1.357` | **RED** |
| a shape tilt of `dn_s = +0.0005` on the arm only | `1.384` | **RED** |
| `dn_s = +0.001` | `1.380` | **RED** |
| a pure rescale of the arm by `×1.0012` | `1.388` | green — **correctly** |

⌗ *The rescale cannot move it and should not: the receipt re-fits the amplitude
(`A = mb·F·D / mb·F·mb`), so a multiplicative perturbation is degenerate and is absorbed. **A pin that
survives a rescale is not thereby a weak pin — it is a pin on shape**, and the tilt at `5e-4` shows how
tight it actually is. I record the degenerate direction because trying it and reporting only the
perturbation that worked would have overstated the test.*

**And the quoted claims were left alone.** `cc66.33`'s withdrawn sentence (*"73.1 per cent … is the
TRANSFER'S"*) and `r6881`'s quoted `corr 0.96, slope 1.28, rms ratio 1.34` are **historical quotations**;
only the receipt's own current measurements move. ⌗ *Six of the hardcoded `73.1`s in this file are
quotation and five are measurement, and editing the wrong ones would have falsified a withdrawal.*
