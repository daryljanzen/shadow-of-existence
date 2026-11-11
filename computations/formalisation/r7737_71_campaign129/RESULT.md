# `r7737+71.2` — RESULT: campaign 129, **P5's monodromy and deck group are BUILT: rows 11a, 11b, 12a and 12b.** ⌗ `+640` lines, inside the registered band of 600–950 (point `700`). `533` of them are the verbatim copy of `Row18Monodromy.lean`. ⌗ p `0.75` came true. There was no stop

*Against `PREDICTION.md` (`r7737+71.1`). 71 ran `lake env lean probes/Groupoid.lean`. It exits 0 with no errors and no
warnings. All `57` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`: `41` from campaigns
127–128, `12` from the copy, and `4` new. The forbidden-token grep is clean, the probe imports only Mathlib, and
`check_no_sorry.py` reads ALL 29 THEOREMS COMPILE.*

**The copy.** `Row18Monodromy.lean`, from `open Polynomial` to `end ShadowProbe.Row18Monodromy`, is copied into
`Groupoid.lean` in `section Row18Copy`. A `diff` against the source is empty. Its namespace and every name are kept,
so P5's names are in one file.

## Rows — BUILT

- **11a, `gp_nariai_simple`:** `Δ(m) = 4 − 27m²` (`m = 2M`) vanishes at `m = ±2/(3√3)`, and `dΔ/dm = −54m ≠ 0`
  there: a simple zero. These are the points `27M² = 1` that the cover's base leaves out.
- **11b, `gp_monodromy_swaps`:** `loopPlus` gives monodromy `swap e₀ b` and `loopMinus` gives `swap e₀ c`, with
  `e₀, b, c` distinct. Each Nariai monodromy is a transposition, and the two transpose different pairs, which
  `rem:monodromy-group` says is the computation the generation rests on.
- **12a:** the copied `monodromy_surjective` and `monodromyGroup_equiv_S3` give a monodromy group equal to all of
  `Perm (fibre) ≃* S₃`.
- **12b:**
  - **`gp_deck_trivial`:** a permutation of the fibre that commutes with every monodromy permutation is the
    identity. Its centraliser is trivial.
  - **`gp_not_normal`:** the monodromy group has order 6 on a 3-point fibre and fixes `e₀` by `swap b c ≠ 1`. So it
    does not act regularly, and the cover is not normal.
- **Cited, not formalised:** that the deck group of a connected cover is the centraliser of its monodromy group.

## Marks (P5's inventory, `r7733_71_survey/SURVEY.md`)

- **Built (13):** 1, 2a, 2c, 3, 4, 5, 7b, 8, 11a, 11b, 12a, 12b and 13.
- **Built in part (4):** 2b, 7a, 9 and 10, in `SlicingCurvature.lean` and `SlicingHinge.lean`.
- **No formal core (1):** 6.

**Next (campaign 130):** the copies for 2b, 7a, 9 and 10, which would close P5.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
