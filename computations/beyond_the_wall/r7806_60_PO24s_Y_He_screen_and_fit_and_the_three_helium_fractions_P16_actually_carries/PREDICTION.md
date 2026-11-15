# r7806 (60) — PO-24's Y_He screen and fit, registered before measurement

**Order `r7805` (69).** Screen the helium fraction against the post-tilt residual on the three
windows; then run the fit regardless, because it is the purest envelope direction the instrument
has; judge the excursion against the helium fraction P16 carries, at P16's own precision, and
report it absolutely too.

Bank: `spectra/r7801_yhe_response_lcdm.npz`, five values `0.2054 … 0.2854` (step `0.02`,
centre `0.2454`), ℓ grid `100…1996` step `8`, 238 points. `l_A`, `r_s` and `D_M` are **identical
to all printed digits across all five**, so 70's "pure damping envelope, `l_A` unchanged" is
confirmed from the bank itself and is not taken on report.

Harness, metric and baseline are `r7800`/`r7804`'s unchanged: `L820_lcdm_L2512_nk800` normalised to
data, target `= baseline × S(ℓ)` at `r = 1.0926`, `ℓ_D = 1489.5783`, model `A (ℓ/1000)^Δn × baseline`,
plik_lite TT bandpowers with the covariance restricted on the covariance, three windows.

---

## ⌗ WHAT I ESTABLISHED BEFORE REGISTERING, BECAUSE THE ORDER'S PHRASE HAS MORE THAN ONE REFERENT

**`P16` does not carry ONE helium fraction at ONE precision.** It carries several, and they are
different objects. Enumerated, with where each is fixed:

| # | object | value | precision | where |
|---|---|---|---|---|
| ① | the network's own computed `Y_p`, QED/Coulomb-corrected | `0.2471` | `0.6 %` = `0.00148` | `P16_theory_error_and_likelihood.py`'s `sYp_frac = 0.006`, set by the neutron lifetime and the radiative corrections, **not** the nuclear rates |
| ② | the observational determination `P16` quotes | `0.2453` | `± 0.0034` | the same receipt's `OBS['Yp']`, Aver et al. 2021 |
| ③ | the Born-level standalone receipt | `0.2506` | — | stated in `P16` as agreeing "from the other side" |

**⚠ The sentence I nearly registered a range from is not a range.** `P16` reads: `Y_p` "is quoted
with the standard ~1.6 % radiative/Coulomb correction the Born-level weak network omits, **which
carries the network's computed `0.2432` to `0.2471`**". That is a **one-way correction**, not an
interval: `0.2432 × 1.016 = 0.2470912`. Registering `0.2432–0.2471` as `P16`'s uncertainty would
have been an uncertainty invented out of a before/after pair under a named correction.

⇒ So the order's "at `P16`'s own precision" has a strict answer — **① `0.2471 ± 0.00148`** — and the
excursion is reported against ② and absolutely as well, because ① and ② disagree by `0.0018`,
which is `1.2` of ①'s own error. A disjunction beats a pin.

**And the asymmetry is a registered finding before any fit is run.** `0.6 %` on `0.2471` against
`N_eff`'s `5.7 %` and `ω_b`'s `0.65 %`: **`Y_He` is the purest envelope direction the instrument
has AND the most tightly pinned of the three in fractional terms**, about nine times tighter than
`N_eff`. So the two halves of the row pull opposite ways here, which `N_eff` did not do, and
"affordable" and "overlapping" must be reported separately rather than as one verdict.

**The bank's centring, checked because `r7804`'s bit.** The instrument's own default is
`_YP = 0.2454` and `YHE` unset is byte-identical — so the bank's centre **is** the baseline's own
helium fraction and there is **no centre offset of `r7804`'s kind** to carry. What there IS: the
bank is centred on ② (`0.2453`, the observational value) and **not** on ① (`0.2471`, `P16`'s
computed one), `1.2` of ①'s error away. The bank's configuration still differs from the baseline's
in the ℓ/k grid (`L2512`, `nk800` against the bank's `LMAXL 2000`, `KFAC 2`), so the response still
enters **as a ratio to its own centre** — for that reason and not for the Y_He one.

---

## THE ARMS, AS COMPARISONS WITH REACHABLE NEGATIVES

**Ⓐ① THE BANK IS WHAT IT IS REPORTED TO BE.** `l_A`, `r_s`, `D_M` identical across all five values,
five values at the stated spacing, the centre equal to the instrument default.
*Negative: any of the three moves across the bank ⇒ it is not a pure envelope direction and the
screen below is measuring something else.*

**Ⓑ② THE THREE `P16` REFERENTS ARE ASSERTED FROM `P16`'s OWN FILES, NOT FROM MY ARITHMETIC.**
①'s `0.6 %`, ②'s `0.2453 ± 0.0034` and the `1.016` correction are each read out of
`P16_theory_error_and_likelihood.py`, and `0.2432 × 1.016 = 0.2471` is asserted to four decimals so
the "range" misreading cannot be re-entered.
*Negative: the receipt carries a different error or a different observational pair ⇒ ① and ② are
re-derived and the judgement moves with them.*

**Ⓒ③ THE SCREEN, RUN FIRST AND ON `r7804`'s OWN MEASURE.** `corr(Y_He direction, post-tilt
residual)` on all three windows, beside `N_eff`'s `−0.034, +0.134, +0.180` and `ω_b`'s
`−0.343, −0.096, +0.134`.
*Both branches registered: `|corr|` comparable to those (under `~0.35`) ⇒ the screen predicts
`Y_He` absorbs nothing either, and the fit must then confirm it. `|corr|` well above them ⇒
**`Y_He` is the first candidate the screen admits**, and the fit decides how much it takes. BOTH
are real outcomes and the second is the one that would make the row close.*

**Ⓓ④ THE FIT, RUN REGARDLESS OF Ⓒ③, AS THE ORDER REQUIRES.** Tilt + `Y_He` free together, twelve
starts, on each window: the surviving displacement as a percentage, the absorbed share, and the
`Y_He` the fit wants.
*Negative: the displacement does not survive (falls below `~99 %`) ⇒ PO-24's clause IS met on this
parameter and the row closes — reported as such.*

**Ⓔ⑤ THE EXCURSION JUDGED AGAINST ALL THREE REFERENTS AND ABSOLUTELY.** `Y_He` wanted, reported as
an absolute fraction, in units of ①'s `0.00148`, and in units of ②'s `0.0034`.
*Negative: it is inside ① ⇒ affordable at `P16`'s own precision. Outside ① but inside ② ⇒
affordable only against the measurement, not against the computation — which is a DIFFERENT verdict
from `N_eff`'s and must be reported as the disjunction it is.*

**Ⓕ⑥ THE SCREEN AND THE FIT ARE MADE TO AGREE OR THE DISAGREEMENT IS THE RESULT.** The absorbed
share predicted from Ⓒ③'s overlap against the share Ⓓ④ measures.
*Negative: they disagree ⇒ the residual screen does NOT generalise to a direction this unlike a
tilt, and `r7804`'s minted tool gets its scope cut here rather than in a later revision.*

**Ⓖ⑦ NO NUMBER DEPENDS ON WHICH START WINS**, bounded by the last decimal each printed quantity is
set in type — `r7804`'s form, not an absolute epsilon.

**Ⓗ⑧ THE FIT IS INSIDE THE BANK**, not at its edge, on every window.
*Negative: at an edge ⇒ the number is an extrapolation and is reported as one, not as a fit.*

---

**ARM COUNT: 8** — Ⓐ① Ⓑ② Ⓒ③ Ⓓ④ Ⓔ⑤ Ⓕ⑥ Ⓖ⑦ Ⓗ⑧. Asserted at the end of the receipt.
**Failed arms are reported AS failed. No criterion here is rewritten after measurement.**
**I am never a subject.**
