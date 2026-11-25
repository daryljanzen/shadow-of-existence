# `r7869+cc66` — REGISTERED BEFORE ANY COMPUTATION

Order `r7869` (69), two items:

- **⑧** the reference's `dχ²/dΣ` on 60's identical `555` bins, with the thirty-six named; both ruler
  modes, each computed on its own parameters.
- **⑨** convert the `r7783` census from a directory list to the property it guards.

⌗ **What was already run before this file, and must not be read as a prediction confirmed.** For ⑨ I
ran a *structural* reconnaissance over the census population — which keys each polarisation `.npz`
carries — because whether the ordered conversion is implementable at all depends on it, and a band
cannot be registered against a field that may not exist. It found: **125** polarisation banks
(`Dl_EE` or `Dl_TE`); **119** carry `config`, **6** do not; **0** carry any rate key in `config`
(`CRH0`, `CROM`, `NS`, `WBH2`, `H0`, `OM`, …); **64** record `LEAFGEOM: true`. Those five counts are
findings already in hand, not registrations. The receipt re-derives each of them.

---

## ⑧ THE REFERENCE'S PER-BIN RESPONSE

The reference is `r7853`'s `profile_likeforlike.py` with `r7865`'s repaired memo. Both modes
(`rd_camb`, `rd_min`) are profiled from **their own** banked parameters — this side never touched
60's shared cache, so neither mode depends on 60's pending fix.

- **Ⓐ① the reference leg reproduces its own record.** Scoring the banked `Σ = 0` point of each mode
  on 60's full `555` bins reproduces that mode's banked `χ²` to `< 1e-9` relative. A departure means
  my own re-score, not the derivative, is wrong.
- **Ⓑ② the thirty-six are 60's, by construction and not by my reading.** The low set is the twelve
  lowest `BIN_LO` per block of 60's own mask, and I register that it lands at multipoles
  `100 ≤ ℓ ≤ 207` and `36` bins, which is what `r7869` states. If the construction gives any other
  count or range, the band fails and 60's own `low_bins.json` rows are used instead.
- **Ⓒ③ THE TWO MODES MUST SEPARATE.** This is the band the cache defect makes worth registering:
  the two modes' per-bin derivative vectors are **not** identical. I register
  `max_bin |dχ²/dΣ|_rd_camb − dχ²/dΣ|_rd_min| > 1e-6`, and expect it far larger, since the modes'
  `H0` differ by `0.426237` km/s/Mpc. ⚠ **If this band FAILS — if my two modes also come out
  identical — then the agreement 60 reported is not a cache artefact and my `r7867` finding is
  wrong.** That is the honest failure condition and it is registered as such.
- **Ⓓ④ the low end carries little of the reference's response.** The thirty-six bins' share of
  `Σ|dχ²/dΣ|` over all `555` is **under `0.15`** in both modes. Registered against this reference
  already moving only `−0.12` meV when they are removed, against the instrument's `−20.09`.
- **Ⓔ⑤ the share is not where the instrument's lean is.** The reference's low-end share is at least
  `5×` smaller than the instrument's own, taken the same way on the same bins.
- **Ⓕ⑥ interiority.** Every banked parameter used sits strictly inside `profile_likeforlike`'s `BOX`.

## ⑨ THE CENSUS CONVERTED TO ITS PROPERTY

⛔ **REGISTERED AS A REFUTATION OF THE ORDERED FORM, because the reconnaissance above already shows
it cannot be implemented as written.** `r7869` ⑨ says *"'on the one rate' is read off each bank's
recorded config"*. Two independent facts defeat that:

- **Ⓖ⑦ no bank's `config` records the rate.** Of the `119` that carry `config`, **none** carries
  `CRH0`, `CROM`, `NS`, `WBH2` or any equivalent. The rate is simply not a config field, so "on the
  one rate" is unreadable there for *every* bank, named or not.
- **Ⓗ⑧ the production path for one-rate polarisation banks writes no config at all.** `ACOUSTIC`'s
  `POLSAVE` records nothing inside the `.npz` — which is *why* `r7783` had to hand-write its own
  `SWITCHES.txt`, and why `r7783`'s own four and its own banked arm are among the six config-less
  files. ⇒ **A newly planted one-rate bank, the exact case the arm must redden on, would carry no
  config and be invisible to a config-keyed test.** The ordered property is blind precisely where it
  has to bite, while the `64` banks that *do* declare `LEAFGEOM: true` are 60's grid, which must
  **not** redden. I register that a config-keyed arm fails the planted-bank trial.

✔ **So the conversion is made on a property that every bank actually records.** `r_s`, `l_A`, `D_M`,
`ns` and `arm` are present in **all** instrument banks, config-less ones included (`124` of the
`125`; the one exception is a likelihood data product, not a bank). "On the one rate" is read off the
bank's own recorded rate outputs against `r7783`'s `SWITCHES.txt` line
(`CRH0=68.585672 CROM=0.294463 NS=0.961379 WBH2=0.022181`):

- **Ⓘ⑨ the substitute discriminates.** On the recorded `ns`, `r_s` and `l_A`, `r7783`'s own
  one-rate banks match its `SWITCHES.txt` rate and 60's `64` `LEAFGEOM: true` grid points do not,
  with no overlap — so the property separates the population without a directory list.
- **Ⓙ⑩ it still reddens on a planted one-rate bank**, planted the way the real one would arrive:
  through `POLSAVE`, carrying **no config**. The ordered config-keyed form stays green on this same
  plant, which is Ⓗ⑧'s point made operational.
- **Ⓚ⑪ it stays green on all four named grids**, all `64` points, and on the live tree.
- **Ⓛ⑫ `r7783`'s own four stay pinned by name**, so one going missing or renamed still reddens.
- **Ⓜ⑬ the directory list is gone.** `R7860_DIRS` no longer appears in the arm's condition.

⌗ **Same defect class, fourth instance in four revisions.** A guard keyed on a spelling (`r7865` ⑦'s
own first cut), a memo keyed on rounded parameters (`r7865` ⑦), a cache keyed on the sum alone
(`r7867` ⑪), and now a census keyed on a directory list — and the ordered repair would have keyed it
on a config field the relevant writer never writes. ⇒ **The general form: a rule keyed on something
the production path does not guarantee is blind exactly where it must bite.**
