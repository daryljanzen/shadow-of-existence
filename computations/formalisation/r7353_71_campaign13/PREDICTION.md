# `r7353+71.17` — PRE-REGISTRATION: campaign 13, the closed-slicing halves of rows 0, 2, 4 and 5. `R = 6(aä + ȧ² + k)/a²` and `Weyl² = 0` on FRW for EVERY `k` under THE connection, and P10's closed slicing `a = α cosh(T/α)` on `S³` has `R = 12/α²` at every point. ⌗ `90` added lines (band 45–180), ⛔ stop `220`, one `256`-case table (already built, re-proved once). ⌗ p `0.7`. ⌗ If it lands, rows 0, 2, 4 and 5 move from half to DONE

*Orders: `FOR_71.md` §`r7353` ① (register before building, census in the same push). Written before anything is
built.*

## Where the rows stand

- The four rows are halves, and each open half is "the closed slicing" (`r7315` correction at `r7319+71.1`):
  - row 0: `R` of the closed slicing;
  - row 2: `Weyl² = 0` at `k = +1`;
  - row 4: the closed slicing's `R`;
  - row 5: the closed slicing's constant `R`.
- `r7325+71.3` classed these halves as reopenable by the near-point convention.
- `70`'s `frw_closed` (row 72) proves `R` and `Weyl² = 0` on closed FRW with `a` free, in
  `probes/SecondSeatFRW.lean`. Probe files cannot import each other, so this seat cannot compose it with the slicing.
  My own `probes/FRWk.lean` holds the general-`k` table `fRk` (campaign 9), and is extended instead. `70`'s file is
  not touched.

## ① The piece, in `probes/FRWk.lean`

1. ***Refactor, no new mathematics.*** The 256-case table proof inside `frw_gb_k` moves to a lemma `frw_tab_k`, so
   the table is proved once and used three times. `frw_gb_k`'s statement does not change.
2. ***`frw_scal_weyl_k`.*** Under the profile conditions of campaign 9, for every `k`:
   - `R = 6(aä + ȧ² + k)/a²`;
   - `Weyl² = 0`.
3. ***`frw_closed_slicing`.*** Take `a = α cosh(T/α)` (smooth and nonzero on all of `ℝ`), with `S₁ = sin²χ` and
   `S₂ = sin²θ` near the point. Then `R = 12/α²` at every point:
   - `R` is constant, which is row 5;
   - `R` is the de Sitter value, which is rows 0 and 4.
   - `Weyl² = 0` there, and at `k = +1` for any `a`, which is row 2.

***Failable:*** BUILT, BUILT IN PART or REPORTED. p `0.7` under the stop.
- ***Risk 1:*** `Weyl²` on the symbolic table. `riem2C` is 256 terms with free profile values. `frw_gb_k` already
  contracts `riem2C` inside `gbC`, so the shape is known to close.
- ***Risk 2:*** the refactor changes the elaboration of a built proof, and could break it.
- ***Caveat, as in campaign 9:*** the near-point convention. The sphere profiles are `sin²` only NEAR the point,
  because the chart needs them nonzero everywhere.

***Census if BUILT:*** rows 0, 2, 4 and 5 move `DONE (chartable half)` → `DONE`. Then DONE `51` and halves `6`.

## ② Decisive fraction, survival, compile

- ***Decisive:*** step 2's `Weyl² = 0` for a general `k`. That is the only new contraction.
- ***Readings:*** none new. The running rate stays `14` of `21`.
- ***Compile:*** the table is proved once, about `330 s` (campaign 9's measurement), plus the contractions. `6–9`
  minutes in all.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
