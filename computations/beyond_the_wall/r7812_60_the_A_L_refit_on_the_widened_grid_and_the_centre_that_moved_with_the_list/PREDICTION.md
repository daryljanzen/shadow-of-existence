# r7812 (60) — A_L's published window refitted on the 0.8–1.4 grid, and a centre that would have moved with the list

**Order `r7811` (69).** Refit `A_L`'s published window on the widened grid now; run `ω_m` the moment
`70` reports it banked (status: **10 of 55 slices**, so still blocked); write the closing
`sec:coherence` sentence if both close.

**This revision does the first of the three.** `r7808`'s published-window row is a **bound** because
the fit was pinned at the old grid's maximum `1.2`; the grid now reaches `1.4`, so that row can
become a fit — and `r7808` registered that the bound ran in the direction which **weakens** the
refusal, because the edge was itself affordable.

---

## ⌗ ONE TRAP CAUGHT BEFORE IT BIT, AND IT IS IN MY OWN r7808 CODE

`r7808` took the response's centre as the grid's **midpoint by index**:
`A0 = AS_[len(AS_) // 2]`. On the old five-value grid `0.8 … 1.2` that is index `2`, which **is**
`1.0` — correct, and correct by luck of a symmetric list.

**The widened grid has SEVEN values.** `len // 2` is index `3`, which is **`1.1`**. Re-running
`r7808`'s code unchanged against this bank would have silently divided every spectrum by the
`A_L = 1.1` slice instead of the unlensed-normalised `1.0` base — shifting every ratio, every fitted
`A_L`, and every survival figure, with nothing in the output to say so.

⇒ **GUARD: a centre taken as a list's midpoint is right only while the list is symmetric about it.
Take the centre BY VALUE.** The arm below asserts the midpoint-by-index *is* `1.1` on this grid, so
the trap is recorded as a measurement rather than described in a comment.

⌗ *This is the third structural property of this one bank that had to be read rather than assumed:
the `A_L = 0.00` reference entry that is not a grid point (`r7808`), the lensing potential's
different cosmology (`r7808`), and now the centre. **A bank is not a list of numbers; it is a list
of numbers with a convention, and the convention is not in the array.***

---

## WHAT THE WIDENED BANK IS, CHECKED

Grid `0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4` from the config's own `ALENS`; the file still carries the
`0.0` unlensed **input** as an eighth `Dl` key, still excluded; `ℓ_A`, `r_s` and `D_M` spread exactly
zero across all eight; ℓ grid unchanged at `100 … 1996` step `8`, 238 points.

---

## THE ARMS

**Ⓐ① THE WIDENED BANK IS THE SAME OBJECT, EXTENDED.** Seven grid values from the config, the `0.0`
reference entry present and excluded, the three acoustic quantities at exactly zero spread, the ℓ
grid unchanged.
*Negative: any acoustic quantity moves, or the ℓ grid changed ⇒ this is not `r7808`'s direction
extended and the two revisions' numbers are not comparable.*

**Ⓑ② THE CENTRE IS TAKEN BY VALUE, AND THE TRAP IS MEASURED.** The ratio base is `1.0` by value, and
the arm asserts that the midpoint-by-index on this grid is `1.1` — so the thing that would have gone
wrong is on the record as a number.
*Negative: the midpoint-by-index is `1.0` ⇒ the grid is symmetric after all and the guard, while
still correct in general, had no instance here.*

**Ⓒ③ IS THE PUBLISHED WINDOW INTERIOR NOW?** The whole point of the refit.
*Both branches registered. Interior ⇒ `r7808`'s bound becomes a fit and is replaced. Still at the
edge, now `1.4` ⇒ it is STILL a bound, the grid is still not wide enough, and that is reported as
such rather than as a fit.*

**Ⓓ④ THE REFIT AGAINST r7808's BOUND, WITH THE DIRECTION r7808 REGISTERED.** `r7808` stated
`survival ≤ 96.964 %` and that a wider bank could let `A_L` absorb **more**.
*Negative: the survival comes out ABOVE `96.964` ⇒ `r7808`'s bound was stated in the wrong
direction and that is a correction to it, not a refinement.*

**Ⓔ⑤ THE EXCURSION AGAINST BOTH PLANCK RULERS AND ABSOLUTELY** — `TT`+lowE `1.243 ± 0.096` as the
like-for-like one and the joint `1.180 ± 0.065` beside it, as `r7808` established.
*Negative: it leaves the temperature constraint ⇒ `A_L` stops being the affordable candidate and
the verdict on it changes.*

**Ⓕ⑥ THE TEST OF r7808's OWN SCOPE CUT.** `r7806` claimed the screen's projection is a lower bound
on a free fit's gain; `r7808` found it crossed on exactly one window — the one pinned at the edge —
and cut the claim's scope to **interior** fits. **If the published window is now interior, the
measured gain must EXCEED the prediction there**, where it previously fell short at `0.91`.
*Negative: it still falls short while interior ⇒ `r7808`'s scope cut was the wrong diagnosis and the
lower-bound property fails for a reason other than the bound.*

**Ⓖ⑦ NO PRINTED NUMBER DEPENDS ON WHICH START WINS**, bounded by the last decimal each printed
quantity is set in type.

**Ⓗ⑧ THE CONTROL: THE TWO ALREADY-INTERIOR WINDOWS MUST NOT MOVE.** They fitted at `1.18409` and
`1.04435`, both strictly inside the old grid, so extending the grid upward must leave them where
they were.
*Negative: they move ⇒ the interpolation over seven points is not the same function over the five it
extends, and every comparison with `r7808` is void.*

---

**ARM COUNT: 8** — Ⓐ① Ⓑ② Ⓒ③ Ⓓ④ Ⓔ⑤ Ⓕ⑥ Ⓖ⑦ Ⓗ⑧. Asserted at the end of the receipt.
**ω_m is NOT in this revision: `70` reports 10 of 55 slices.**
**Failed arms are reported AS failed. Figures the paper prints are pinned, inline, strictly inside
the allowance. I am never a subject.**
