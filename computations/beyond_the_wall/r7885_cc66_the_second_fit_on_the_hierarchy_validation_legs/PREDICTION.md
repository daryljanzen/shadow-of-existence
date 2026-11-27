# r7885 + cc66 — ⑰ THE SECOND FIT ON 60's r7882 VALIDATION LEGS

**REGISTERED BEFORE A LINE OF THE COMPUTATION EXISTS.** This file is committed and pushed in its
own commit. Everything below is read out of `60`'s banked record and directory, which is reading and
not fitting; no amplitude of this seat's has been computed when this is written.

## The order

⑰ refit `A` and `ε` for TT and EE at `Σ = 0.30` and `0.60` eV against this seat's own CAMB leg, on
`60`'s `41` in-band multipoles, as at ⑬ and ⑮, for the three legs
`r7882_60_the_massive_species_own_boltzmann_hierarchy/valid/{base,nq24,lmax18}`. `69` states `60`'s
verdict Ⓐ as TT `0.989`/`0.979`, EE `0.981`/`0.977`, all within `0.03`, and that the verdict is joint
**only on two fitters**. If this seat disagrees beyond its own reproduction tolerance, that is the
finding, and no limit is read.

## Facts read off the bank BEFORE registering, as at r7879

- Three legs are banked, each with `lcdm_S000{,_pol,_tt}.npz`, `lcdm_S030{_pol,_tt}.npz` and
  `lcdm_S060{_pol,_tt}.npz`; the `_pol` files carry `ls, Dl, Dl_EE, Dl_TE, arm, r_s, D_M, l_A, ns,
  sliced, n_modes, config` over `238` multipoles.
- **THE ZERO LEG IS BYTE-IDENTICAL ACROSS ALL THREE LEGS** (one sha for `lcdm_S000_pol.npz`, one for
  `lcdm_S000_tt.npz`). So the convergence switch is provably inert at `Σ = 0`, there is ONE shared
  zero leg, and no choice of zero leg is being made by this seat.
- `60`'s own twelve figures, which are this revision's targets:

| leg | TT 0.30 | TT 0.60 | EE 0.30 | EE 0.60 |
|---|---|---|---|---|
| `base` | `0.9891418529` | `0.9788502587` | `0.9805523438` | `0.9773976912` |
| `nq24` | `0.9899863000` | `0.9792040229` | `0.9808176001` | `0.9775688622` |
| `lmax18` | `0.9891807779` | `0.9788775687` | `0.9805525020` | `0.9773980281` |

- Worst `|A − 1|` per leg on `60`'s numbers: `base` `0.022602`, `nq24` `0.022431`, `lmax18`
  `0.022602` — all inside `69`'s `0.03`.

## THE REGISTERED BANDS

**Ⓐ① THE LEGS AND THE SHARED ZERO.** Three legs are read, twelve fits are run, and the zero leg's
byte-identity across the three is pinned as an ancestry fact rather than asserted.

**Ⓑ② TWELVE OF TWELVE CONFIRM `60` WITHIN `5e-05`.** The registered reproduction tolerance is
`|ΔA| < 5e-05` on every one of the twelve, chosen against this seat's own history: worst `8.818003e-06`
at `r7877` and `1.039197e-05` at `r7879`, so this band carries about five times that headroom.
**PREDICTED: 12 of 12 inside it.** Anything outside is reported as a DISAGREEMENT and is the finding,
per the order.

**Ⓒ③ ⛔ TWO OF THE TWELVE LEG-PAIR COMPARISONS ARE PREDICTED UNRESOLVABLE, AND WHICH TWO IS
REGISTERED NOW.** The three legs are CONVERGENCE VARIANTS, not physically different repairs, so their
separations are small by construction. Measured on `60`'s own amplitudes against this seat's
interpolation floors (`3.515264e-06` TT, `5.307333e-05` EE, both from `r7875`):

| pair | block | `|ΔA|` | resolvable on my floor |
|---|---|---|---|
| `base`–`lmax18` | EE `0.30` | `1.581836e-07` | **NO — 336× below the floor** |
| `base`–`lmax18` | EE `0.60` | `3.369457e-07` | **NO — 158× below the floor** |
| every other pair and block | | `2.73e-05` … `8.44e-04` | yes |

⇒ **PREDICTED: `10` of `12` resolvable, `2` not, and the two that are not are `base`–`lmax18` in EE
at both sums.** For those two the agreement with `60` confirms the BANK READING and **not** the leg,
which is exactly the shape that materialised on `EE` at `r7877` and was registered there in advance
too. This is stated BEFORE the fit so it cannot be a post-hoc excuse.

**Ⓓ④ THE JOINT BAR ON A SECOND FITTER.** `PREDICTED: all three legs within `0.03` of unity in both
blocks at both sums on this seat's own fit as well, so `60`'s verdict Ⓐ becomes joint on two
fitters.** The worst distance is predicted near `0.0226`, `60`'s own value, and well inside the bar.
If any leg exceeds `0.03` on this fitter, verdict Ⓐ is NOT joint and that is reported as the finding.

**Ⓔ⑤ `ε` IS NOT THE DISCRIMINATOR AND IS NOT PREDICTED TO BE.** `60`'s `ε` runs `-0.0016` to
`0.0035`. This seat's own `ε` is a grid quantity, so agreement is predicted only to its grid step and
`ε` is reported, never used to decide the verdict.

**Ⓕ⑥ THE REGRESSION CONTROL.** The harness IMPORTS `r7875`'s fitter and CAMB leg through `r7877` and
`r7879` rather than copying either, and must re-derive `r7879`'s landed amplitudes at **exactly
`0.0`**. A copied fitter could agree with its ancestor's numbers and still differ where it meets the
new legs. PREDICTED: exactly `0.0`.

**Ⓖ⑦ WHAT THIS WILL NOT ESTABLISH.** A second fitter agreeing with `60` on twelve numbers says the
numbers are right; it does not say the hierarchy is the right physics, and it cannot say the three
convergence legs differ, since Ⓒ③ predicts two of their comparisons are below this seat's resolution.
No limit is read: nothing in this revision licenses one.

**Ⓗ⑧ THE REGISTERED RISK.** If the reproduction tolerance in Ⓑ② is missed anywhere, the first
suspects are the ones this seat has been caught by before: the LENSED-versus-UNLENSED leg (`r7871`'s
figure was lensed, `60`'s `shift.py` is unlensed, and that cost a 167× spurious failure at `r7875`),
and the multipole set, which `r7875` measured as worth `0.004311` in `A`. Both are to be checked
before any disagreement is reported as `60`'s.
