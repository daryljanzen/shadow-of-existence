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

*(substantive defects with line and correction.)*

**`0` substantive so far**, across four seams and five sections. ⌗ *Stated plainly because the
registration predicted `3`–`12`: the count is a live score against `④`, not a formality.*

## Still to read

`§what-crosses` (317) and `§coherence` (436) onward — including `sec:refit-bound` (`856`–`2515`),
which is `1659` lines, over half the paper, and holds the joint refit and `PO-24`'s strike. Attention
on the `169` unpinned prose figures and on cross-section consistency (`③`).
