# `r7879+cc66` — REGISTRATION, pushed before a line of either computation exists

Order `r7879` (69), two items. ⑮ (completion) run my harness on `60`'s newly banked legs and state
the worst distance from their figures. ⑯ a reference for the hierarchy from CAMB itself: TT and EE
sum-response amplitudes with `MassiveNuMethod = Nu_int` against the truncated fluid approximation,
on `60`'s `41` multipoles at `Σ = 0.30` and `0.60`.

## ⛔ TWO FACTS READ OUT OF THE RECORDS BEFORE ANYTHING IS REGISTERED ABOUT THEM

**⒜ There are FIVE newly banked legs, not six.** `69`'s order says *"six newly banked legs, all four
of the decomposition plus the two `c_a²` arms."* `60`'s `parts/` holds `W`, `C`, `E`, `CE` and `A1`,
and `60`'s own `refit_parts.json` and `leverage.json` both record `arms = ['A1', 'C', 'CE', 'E',
'W']`. ** So it is four decomposition legs — weight, continuity, Euler and the `CE` subset — plus
ONE `c_a²` arm. ** I run the five that exist and name them. *This is the same class as the
`shear_on`/`shear_off` ambiguity at `r7877`: a count in a merge paragraph against the directory.*

**⒝ `69`'s "about `6e-6`" misstates my own `r7871` figure by two orders of magnitude.** My record
carries `method_spread_worst = 7.305730e-08`, not `6e-6`. ** And the shape matters more than the
size: `Nu_approx`, `Nu_best` and `Nu_trunc` were BIT-IDENTICAL to each other in that run, with only
`Nu_int` differing, in the ninth decimal. ** That is not a small difference between a hierarchy and
a fluid approximation; it is three settings doing the same thing.

---

## ⑮ — the five legs, completed

**Ⓐ①** Same instrument: the harness IMPORTS `r7875`'s fitter and CAMB leg, and must re-derive the
four landed amplitudes at `0.0` before any leg is read, as at `r7877`. Multipoles are `60`'s `41`,
as `69` ruled. The zero leg is the LANDED one, `60`'s choice and their stated reason.

**Ⓑ②** REGISTERED EXPECTATION, to within `0.005` — `60`'s own figures for the twenty fits:

| leg | TT `0.30` | TT `0.60` | EE `0.30` | EE `0.60` |
|---|---|---|---|---|
| `W` | `0.9951027` | `1.0562072` | `0.9599546` | `0.9403878` |
| `C` | `1.1311122` | `1.2639430` | `1.0123697` | `1.0436065` |
| `E` | `1.0546425` | `1.1390197` | `1.0006048` | `1.0201940` |
| `CE` | `1.0875897` | `1.1895169` | `1.0076871` | `1.0342429` |
| `A1` | `0.9211488` | `0.9078648` | `0.9535036` | `0.9277492` |

A miss is a real disagreement between two fitters on a repair candidate and is reported as one.

**Ⓒ③** THE SEPARATION FLOOR AGAIN, because `r7877` showed it decides what an agreement is worth. For
each pair of legs I report whether my fitter resolves them apart, against my own interpolation
floors — `3.515264e-06` for TT and `5.307333e-05` for EE. ** Any leg pair whose separation falls
below the floor is reported as CONFIRMING THE BANK READING AND NOT THE LEG, as `EE` was at `r7877`. **

**Ⓓ④** `69` has refined the bar to *"TT and EE both within `0.03` of unity on both fitters."* I
report `|A − 1|` against `0.03` for all twenty fits. REGISTERED: on `60`'s figures, `W`'s TT at
`Σ = 0.30` is `0.9951027`, inside `0.03`, while its EE at `0.60` is `0.9403878`, outside it — so I
expect NO leg to pass the joint bar at both sums, and I state which comes closest rather than only
that none passes.

**Ⓔ⑤** I do not expect to adjudicate the family. `69` has ruled on `60`'s leverage finding and
ordered the hierarchy. This item supplies a second fitter's numbers.

---

## ⑯ — CAMB's own hierarchy against its own fluid approximation

**Ⓕ⑥** ⛔ THE LIVENESS CONTROL COMES FIRST, AND THIS ITEM MAY MEASURE NOTHING. My `r7871` record
shows `Nu_trunc` and `Nu_approx` returning spectra BIT-IDENTICAL to `Nu_best`. ** If the truncated
setting does not change the spectrum, it cannot change `A`, and an `A` difference of zero would say
nothing about hierarchies — only that the knob is inert. ** So before any `A` is compared I require
that the two methods' spectra differ at all, and I report the difference I measure. If they are
bit-identical here too, THAT is the answer to `69`'s question and it is reported as such: CAMB's
hierarchy and its fluid approximation are the same object at these sums, so no part of `60`'s
leverage gap can be attributed to the difference.

**Ⓖ⑦** REGISTERED EXPECTATION: `A` and `ε` differ between `Nu_int` and the truncated method by LESS
than `1e-4` in `A` — far below the `0.03` bar `69` has set and far below the `10.8`/`6.4` TT:EE
leverage `60` need. I expect the spectra difference to sit near `7.3e-08`, my `r7871` figure.

**Ⓗ⑧** ⛔ REGISTERED AT RISK: `A` IS A FITTED QUANTITY AND COULD AMPLIFY A TINY SPECTRUM DIFFERENCE.
A least-squares amplitude over `41` multipoles is not a pointwise ratio, and `r7875` measured my own
interpolation sensitivity at `3.5e-06` (TT) and `5.3e-05` (EE). ** So if the methods' `A` differ by
less than those floors, I CANNOT distinguish them and will say so rather than quote a difference. **
`69` asked "whether that difference is as small in `A` and `ε`, and where it is not" — the honest
answer may be that it is below what my fitter can see, which is a different statement from zero.

**Ⓘ⑨** The four methods available are `Nu_best`, `Nu_int`, `Nu_trunc`, `Nu_approx`, all four
confirmed settable at `r7871`. I run `Nu_int` as the hierarchy and BOTH `Nu_trunc` and `Nu_approx`
as the truncated arms, rather than choosing one, because `r7871` found them identical and a single
choice could hide that.
