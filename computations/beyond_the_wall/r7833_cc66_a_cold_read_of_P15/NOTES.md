# r7833 — the cold read of P15, running notes

`corpus/CR_cosmology.tex`, `3167` lines, `399` `\rcpt` sites over `255` distinct receipts.
Sections read in order, per the order's ①. **Every check recorded, including the ones that found
nothing** — a read whose negatives are not on record cannot be audited.

## Method, and why it is not a line-by-line crawl

`check_compile` already fails on any dead `\rcpt` link and is green, so **no citation is dangling**.
`check_figures_pinned` already establishes, for every printed figure beside a citation, whether the
cited receipt **pins** it — a pinned figure is verified by construction and cannot be stale without
reddening that gate. ⇒ **So the risk surface for ② is the figures the gate baselines as UNPINNED:
`169` of them in P15's prose.** That set, plus the seams the order names, is where this read spends
its attention, and the reasoning is stated so the coverage can be disputed.

## Seam checks — the five landings the order names

| seam | checked | verdict |
|---|---|---|
| `PO-24`'s strike / the joint refit | the four figures **this seat withdrew** at `r7823`/`r7829` (`22.40`σ, `9.02`, `1.0569`, `8.53`) searched across the paper | **`0` hits each — the withdrawals propagated.** ⌗ *Contradicts this revision's own prediction ②, which expected at least one survival* |
| the one rate — `ℓ_D` | `1951.9` / `1497.04` / `1489.58` chain at lines `565`, `578`, `612` | **in one state, each value named with its configuration.** `578` carries the chain explicitly; `612`'s Lean check confirms `1951.9/\sqrt{1.7}` within `0.005` of `1497.04` |
| the one rate — the comb | `299.1` (`6` sites) against `298.5` (`4` sites), `298.94` absent | **not a defect, and it reads like one.** `298.5` is the comb fitted by the paper's own procedure on the sky; `299.1` is the comb with the projection's distance on the rate's geometric part — a *different configuration*, cited to its own receipt. `299.1` vs the sky's `298.4` is "a part in four hundred" (`1/426`), which checks. ⌗ *A receipt is **named** `..._takes_the_comb_from_299_1_to_298_94`, and a second is named `..._the_published_comb_is_298_5_not_298_94`: the second supersedes the first's figure. **Rewriting the paper to match the first receipt's NAME would have been the `⑤` failure exactly*** |
| the half-applied correction (`R1`) | line `695`'s citation of `R1_the_correction_stopped_at_the_sentence_and_the_number_it_defines_was_left_behind` | **correct usage.** The receipt carries its own supersession note (`r6931+70.1`): `1.0816`/`+8.2%` is retired, the paper now carries `r = 0.992` at the visibility peak and `1.023` at a sharp cut, and the receipt states its finding "is checked on the PRESENT paper against the present values, and it holds". Line `695` cites it for the **method** — *"the sentence and the ratio it defines being checked against each other rather than corrected separately"* — not for the retired figure |

⇒ **Four seams, four in one state.** The paper's handling of superseded configurations is, so far,
better than this revision registered expecting.

## Sections read in order

### `§intro` (153), `§background` (169), `§properframe` (181), `§flatlcdm` (201), `§tensions` (230)

Arithmetic checked wherever a sentence prints two figures that must agree:

- **`258`** *"exceeds the baryons by about a factor of six, `\Omega_m\simeq0.31` against
  `\omega_b/h^{2}\simeq0.05`"* — `0.31/0.05 = 6.2` ✓, and the notation is right rather than wrong:
  `\omega_b/h^2` **is** `\Omega_b`, so `0.05` is the figure that belongs there.
- **`266`** the radiation-to-matter ratio chain: `\rho_r=\rho_m` at `T\simeq0.8` eV, the bottleneck at
  `0.07` MeV ⇒ `7\times10^{4}/0.8 = 8.75\times10^{4}`, printed as `{\sim}9\times10^{4}` ✓; four orders
  above that ⇒ `9\times10^{8}`, printed ✓. **Both figures follow from the two it states.**
- **`268`–`272`** the specific-entropy pair, and this one needed resolving rather than reading:
  *"the peak perturbing it by `5.5\times10^{-10}` of a standing `1.15\times10^{10}\,k_B` per baryon"*
  against *"unchanged to one part in `2\times10^{9}`"*. ⇒ **Consistent only under the FRACTIONAL
  reading** — `5.5\times10^{-10}` as a fraction gives `1/(1.8\times10^{9})`, which is the printed
  `2\times10^{9}`. *Read instead as an absolute perturbation in `k_B` per baryon it would give one part
  in `2\times10^{19}`, ten orders out.* ⌗ **Not listed as a defect**: the `2\times10^{9}` forces the
  fractional reading and the two sentences then agree, and the standing value is independently
  plausible (`s/n_b \approx 3.6\,n_\gamma/n_b \approx 6\times10^{9}\,k_B` at `\eta\approx6\times10^{-10}`).
  **It is recorded because the phrasing admits a reading under which the paper would contradict
  itself by ten orders, and a later editor could take that reading.**

## The defect list

### ⛔ ① `§coherence`, lines `466`–`467` — **a bound that is false as written, and a comparison its own receipt says is half the one that matters**

**The paper says:** *"the wavenumber-independent `$0.4835\,\Psi_i$`, **within three per cent** of the
frozen value `$\Psi_i/2$` the free oscillator carries at every wavenumber."*

**The arithmetic:** `0.4835/0.5` is **`3.30` per cent** low. `3.30 > 3`, so *"within three per cent"*
is **false as a bound**.

**And the cited receipt already says so, in as many words** —
`P15_the_route_from_the_handover_amplitude_to_the_spectral_parameters...`, lines `35`–`37`:

> *`$0.4835/0.5$` is `3.30` per cent low. On the SPECTRUM that is `$(0.4835/0.5)^2=0.93509$`,
> **`6.49` per cent**, and `$0.4835^2=0.23377$` is the factor itself.* ⇒ *The comparison the paper
> makes on the potential is half the one that reaches the spectrum.*

⇒ **So there are two things wrong and the second is the substantive one.** ⒜ the bound is `3.30`, not
"within three"; ⒝ **the comparison is made on the POTENTIAL, where it is `3.3` per cent, while the
quantity that reaches observables is the SPECTRUM, where it is `6.5` per cent** — a reader takes
"three per cent" as the size of the approximation and the figure that bears on data is double it.

**What it should say:** `3.3` per cent below `$\Psi_i/2$` on the potential, **and `6.5` per cent on the
spectrum**, the latter being the one the acoustic heights carry.

> ⚠ **NOT FIXED HERE, AND THE REASON IS THE REASON THIS ORDER EXISTS.** That receipt **pins the
> paper's present wording as a literal**:
> `_THREE = r"within three per cent of the frozen value $\Psi_i/2$ the free oscillator carries at every "`
> (line `200`), asserted present (line `206`). **Rewording the sentence reddens the receipt that
> owns the finding about it.** So the edit is a coordinated paper-and-receipt change, and whether
> that receipt's finding should be *discharged* by rewording the paper — rather than kept standing as
> a live criticism of it — is a judgement about the receipt's purpose. ⇒ **`69`'s ruling.** *This is
> the `R1_the_correction_stopped_at_the_sentence` shape exactly: correcting the sentence and leaving
> the number it defines behind. Correcting it and leaving the RECEIPT behind is the same error
> mirrored.*

---

**`1` substantive, `0` mechanical fixed**, across five seams and six sections. ⌗ *Stated plainly
because the registration predicted `3`–`12`: the count is a live score against `④`, not a formality.*

## Near-misses — figures that read as superseded and are not

Recorded because each one nearly became a wrong "fix", and guard `⑤` is what stopped it.

- **`§coherence` `499`–`503`, the absorber slope `-0.0002` to `-1.09`.** The first cited receipt
  (`P15_the_tilt_is_the_wrong_absorber`) computes `-0.0002` to **`-1.3141`** at `r=1.0926`,
  `\ell_D=1362`, **no `\alpha`** — so the paper's `-1.09` does not reproduce from it. It reproduces
  from the **second** cited receipt, which pins it: *"absorber: slope at `l = 2508` is `-1.0877`
  (printed `-1.09`) on the faithful exponent, the swing over `30`–`2508` `6989`-fold"*, at
  `\alpha=1.70` and the instrument header's `\ell_D=1951.9`. ⇒ **The paper prints the figure from the
  receipt that owns it; citing both is right, because the first establishes the shape and the second
  the size.** ⌗ *One question for `69` rather than a defect: `1951.9` at `\alpha=1.70` is the
  exponent-one scale `1497.04`, while the in-force scale after the one-rate move is `1489.58`, at
  which the same `r` gives `-1.0988`, i.e. `-1.10`. The `1` per cent does not touch the argument —
  the `6989`-fold swing is `(\ell_{max}/\ell_{min})^2` and carries no `\ell_D` at all — but the
  instrument header's `\ell_D` is pre-move.*

## Arithmetic verified in `§what-crosses` (317–436) — all four MATCH

| line | claim | check |
|---|---|---|
| `325` | the imaginary leg `$=c_0B(\tfrac16,\tfrac12)/2=3.33874$`, `$c_0=2/(\sqrt3\,2^{1/3})$` | `3.338738` ✓ to six figures |
| `345` | `$aH$` normalised to unity at the seam is `$1.96$` at `$0.1\alpha$` and `$19.6$` at `$10^{-3}\alpha$` | `$aH\propto r^{-1/2}$` ⇒ ratio `10` exactly ✓ |
| `377` | the radiation-to-matter ratio `$2r_N/r$` is `$2$` at the seam, `$2^{2/3}$` at the turnaround | forces the turnaround to `$2^{1/3}r_N$` ✓ self-consistent |
| `402` | exponent `$\simeq1.6\times10^{2}c_s/c$` ⇒ `$e^{-1.6}$` at one per cent, `$e^{-16}$` at ten | `1.60` and `16.00` ✓ |

## Still to read

`§what-crosses` (317) and `§coherence` (436) onward — including `sec:refit-bound` (`856`–`2515`),
which is `1659` lines, over half the paper, and holds the joint refit and `PO-24`'s strike. Attention
on the `169` unpinned prose figures and on cross-section consistency (`③`).
