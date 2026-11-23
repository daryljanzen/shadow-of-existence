# `r7859+cc66` — REGISTERED BEFORE ANY COMPUTATION

Order `r7859` (69): **item ③ of `r7857`, unchanged.** *"When `FOURPI` covers the polarisation blocks
and the pairs, rerun your three-block check with it on (TT and EE should read 1 within the raw
spectrum's damping-tail departure; TE by its correlation coefficient), and turn `Ⓔ⑮` over."*

**⚠ THE ITEM IS BLOCKED AND I HAVE MEASURED THAT IT IS, RATHER THAN WAITING ON THE WORD.** Read on
this tree (`e9894377d`), `60`'s repair has NOT landed: `_dec[j, _c]` still carries neither factor,
and `_ee_te[j]` is still `(np.sum(P * _dE ** 2), np.sum(P * _tr * _dE))` with no `_FP_ACC`. So the
switch still moves TT alone, and running the check now would measure the gap, not the repair.
⇒ **This file registers the bands so they are fixed before `r7860` lands, not after.**

---

## WHAT THE CHECK WILL BE

The same comparison `r7855` ran — the committed bank point against my CAMB reference through
`plik_lite`'s own windows, `185` bins, at the control's cosmology — with `FOURPI=1` and the
polarisation blocks and pairs covered. The three blocks as `r7855` measured them, each with the
factor two applied, are the arithmetic the bands below are built on:

| block | `r7855`, switch off | × 2 | its own per-bin spread, × 2 |
|---|---|---|---|
| TT | `0.503313` | **`1.006625`** | `0.056634` → `0.113269` |
| EE | `0.497180` | **`0.994360`** | `0.146394` → `0.292787` |
| TE | `0.622380` | `1.244761` | unusable: it changes sign three times inside the reach |

## BANDS

**Ⓐ TT reads one to within its own spread, and the margin is large.** `|TT_mean − 1| < 0.02`,
expected `1.0066`, which is `0.66` per cent above one against a spread of `0.1133`.
  ⇒ REFUTED outside `±0.02`, which would mean the repair applied something other than the two
  factors to the temperature path.

**Ⓑ EE reads one on the same terms once its blocks are wired.** `|EE_mean − 1| < 0.02`, expected
`0.9944`, `0.56` per cent below one against a spread of `0.2928`.
  ⇒ REFUTED outside `±0.02`. **Two reachable negatives, each diagnostic:** near `0.497` means the
  polarisation blocks were not reached at all; near `1.99` means the factor was applied twice.

**Ⓒ TE is read by its CORRELATION COEFFICIENT, and the sharp half of this band is an invariance.** A
correlation coefficient is scale-free, so it must be **IDENTICAL** with the switch on and off:
`|r_on − r_off| < 1e-12`. *That is the part I am confident of, and it tests the pipeline rather than
the physics — if it moves, something other than a constant has changed.*
  ⌗ And the value itself, registered as a guess with a reachable negative: `r > 0.9` over the `185`
  bins. ⇒ REFUTED below `0.9`, which would say TE's shape disagreement is not confined to its
  normalisation and sign crossings.

**Ⓓ THE REGENERATED BANK IS BIT-FOR-BIT PREDICTABLE, WHICH IS `60`'s OWN CLAIM AND IS TESTED HERE
RATHER THAN BORROWED.** Each block of the regenerated point equals exactly twice the committed one:
worst relative departure from `2` below `1e-12`, on TT, EE and TE alike.
  ⇒ REFUTED if any block departs by more than `1e-12`.

**Ⓔ THE `Dl_pairs` CLOSURE RETURNS.** With the repair in, the ten pairs close on their own `D_l`
under `FOURPI=1` below `1e-12`, against the `0.500000` this seat measured on all four banked
`SRCDEC` files today.
  ⇒ REFUTED if the closure stays at a half, which would mean the repair reached the save line and
  not the accumulation, or the reverse.

**Ⓕ AND MY OWN WATCH ARM TURNS OVER, WHICH IS THE ONE PREDICTION I MADE IN ADVANCE LAST REVISION.**
`Ⓔ⑮` of `P15_the_spread_was_not_like_for_like…` goes **RED** on the repair and `Ⓔ⑭` beside it stays
**GREEN** — the asymmetry was written deliberately and verified by making the edit at `r7857`.
  ⇒ REFUTED if `Ⓔ⑮` stays green (the repair did not reach the decomposition) or if `Ⓔ⑭` goes red
  (the implication arm was written the wrong way round after all). *On the red, `Ⓔ⑮` is re-read as
  the record of the repair, which is what `69` ordered: "turn `Ⓔ⑮` over."*

---

## ⚠ WHAT THIS CANNOT SETTLE

**Agreement to seven parts in a thousand is well inside my own damping-tail spread**, so this check
cannot distinguish a residual few-per-mille normalisation error from none. It says the factor two is
gone, not that the absolute normalisation is now right to better than a per cent.
And it does not validate either side's damping tail: the `−6.35` per cent departure near `ℓ = 1920`
is a difference between the instrument and CAMB that the switch does not touch, and it will still be
there afterwards.
