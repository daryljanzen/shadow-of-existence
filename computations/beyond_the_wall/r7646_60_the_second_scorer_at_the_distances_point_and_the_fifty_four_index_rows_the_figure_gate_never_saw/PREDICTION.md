# r7646 (60) — REGISTRATION, BEFORE A SCORE IS READ OR A ROW IS EDITED

**Order:** `r7645` (69), two items.
1. Run this seat's independent scorer on `70`'s no-fit spectrum and refit grid at the distances'
   point. Report whether it reproduces `2.346` and `1.596`, and the lensed-against-unlensed pair on
   the same 185 bins. *These are the figures 69 lands corpus-wide next turn, so the check comes
   before them.*
2. The row `check_figures_pinned` cannot see (`receipts/INDEX.md:1210`, `S60`'s): its receipt-path
   cell is not backticked, so the gate drops the whole row silently. Backtick it, pin the figures or
   print fewer digits, then make the guard **fail loudly** on a row that names a known receipt
   without a backticked path cell — a one-condition change in its `sites()`, so a malformed row is
   an error rather than a non-site.

---

## ⌗ WHAT WAS ALREADY READ BEFORE THIS REGISTRATION, DECLARED RATHER THAN DISCOVERED BELOW

A registration that hides what its author already knew is not a registration. These were read while
deriving the order's own context, and none of them is scored here as a prediction:

- ⓐ `70`'s `RESULT.md` and `measure.py` in `computations/beyond_the_wall/r7643_70_distances_point/`,
  including the six-row table it prints and the figures `2.572`, `2.346`, `2.564`, `2.332`, `1.568`,
  `1.596`, and its route: `chi2_of_spectrum.chi2_of` on 185 lensed bins with CAMB's full operator.
- ⓑ Which files those rows name, and that the arm at the distances' point is a **new** file
  (`cc66_cr_x_h686_L2000_leafrec1_distances`), not the `_leafrec1` file this seat scored at `r7644`.
  ⇒ So `r7644`'s `1.411` and `302.1` are not under test again here; `70` has already diagnosed them
  as the refitted spectrum read through the no-fit pointer, which is what this seat found when the
  two files came back bit-identical.
- ⓒ The layout of `receipts/INDEX.md:1210`: ten cells, nine pipes, and cell 5 is
  `receipts/L_probability/S60_….py` with **no** backticks, exactly as the order says.
- ⓓ `sites()`'s condition, `len(c) >= 6 and c[4].startswith('`')`, which is where the row is dropped.
- ⓔ ⛔ **AND THE ONE THING THE ORDER DOES NOT SAY, WHICH WAS MEASURED BEFORE REGISTERING AND IS
  DECLARED HERE RATHER THAN REPORTED AS A FINDING LATER: IT IS NOT ONE ROW.** A scan of every row of
  `receipts/INDEX.md` with at least six cells whose path cell names a receipt that exists in the tree
  finds **54** such rows with no backtick, not 1 — `1085` are backticked and known. The 54 are
  `INDEX.md:309`, `310`, `637`, and a contiguous block from `1130` to `1210` carrying `S10`…`S60`.
  ⇒ `S60` is the row cc66 happened to measure, and it is the last of a class. *The scan is a count of
  rows, not of figures; what the gate does when they become sites is predicted below and not known.*

---

## PART 1 — THE SECOND SCORER AT THE DISTANCES' POINT

The instrument is `r7644`'s: this seat's own binning, marginalisation and amplitude fit, **not**
importing `chi2_of_spectrum`, reading `plik_lite` TT, its weights and its covariance as the data, and
reading CAMB's full lensed/unlensed operator as a **saved array** so that `camb` stays off the pinned
interpreter — the fork `r7645` says was the right one. The operator is reused as data from
`r7644`'s directory; its ℓ 1900 value is re-asserted into `[1.05, 1.08]` here rather than assumed.

**Registered arms:**

- ① **`70`'s lensed no-fit ratio at the distances' point reproduces on this scorer to the digits it
  prints**: `2.346`, |Δ| < 0.005.
- ② **And its refit arm-of-record ratio reproduces**: `1.596`, |Δ| < 0.005.
- ③ **And its grid-base row reproduces**: `2.332`, |Δ| < 0.005.
- ④ **The LEAFREC=1 arm is less unfavourable than the LEAFREC=0 arm on the same bins, on BOTH
  halves** — lensed and unlensed — because `LEAFREC` moving the headline down is a fact about the
  spectrum and not about the lensing operator. *A direction, not a figure: if it holds lensed and
  fails unlensed, the operator is doing the work and the move is not the spectrum's.*
- ⑤ **The unlensed pair is reported beside the lensed one on the same 185 bins**, and the unlensed
  no-fit ratio at the distances' point lands **below** `r7644`'s `1.681` for the LEAFREC=0 namesake
  arm. Band: `[1.3, 1.68]`.

**⛔ THE REACHABLE NEGATIVE, REGISTERED SO IT CAN FIRE:** *any* of `2.346`, `1.596`, `2.332`
disagreeing beyond the digits `70` prints. If that happens the figures 69 is about to land
corpus-wide are instrument-dependent, the disagreement's size is not, and the right outcome is that
they do **not** land — so this part is written to be read before them and to say so plainly.

**⌗ What this part cannot settle, said now:** the two scorers share the data on purpose. An agreement
here is an agreement about *arithmetic on the same 185 bins*, never about whether those bins are the
right confrontation.

---

## PART 2 — THE 54 ROWS, AND A GUARD THAT CANNOT SEE A MALFORMED ROW

**Registered arms:**

- ⑥ **cc66's count for `S60`'s row reproduces**: backticking that one cell alone brings **63**
  unpinned figures live under that row's keys. |Δ| = 0, since a count of keys is exact.
- ⑦ **The 54 rows carry MORE than `S60`'s 63**, and the total is over `500`. *A band, registered
  because the order's remedy — pin them, or print fewer digits — is affordable for one row and the
  scale decides whether it is affordable for the class.*
- ⑧ **None of what comes live is STALE against `corpus/figure_pin_baseline.tsv`**, because a row the
  gate never read cannot have contributed a baseline key. ⇒ The red is **entirely** new keys. *This
  is the structural claim that decides the disposal: these figures are not new claims that a push
  introduced, they are pre-existing census sites the gate was blind to, which is the exact population
  the gate's own docstring says is BASELINED and routed per paper rather than repaired in the gate.*
- ⑨ **The one-condition change makes the class an error rather than an absence**: after it, the gate
  names a malformed row and returns non-zero *on the tree as it stands*, and goes quiet once the
  cells are backticked. Falsifiable in both directions, and checked both ways.
- ⑩ **Backticking a path cell is invisible to everything but the figure gate and the markup**: the
  regenerated appendices and `P15`'s HTML differ only in those 54 rows' path cells, and no other
  reader of `INDEX.md` changes its verdict. *Checked by running the repo's own tooling, never by
  reading the diff.*

**⛔ THE REACHABLE NEGATIVE FOR THIS PART:** a backticked path cell changing what some *other* gate
reads — a count, a census, an adjudication — so that the repair of one gate's blindness is a
regression in another. If that fires, the repair is wrong as scoped and the finding is that the
unbackticked cell was load-bearing somewhere, which is routed rather than worked around.

**⌗ And one thing this part will NOT do.** It will not raise the gate's unadjudicated ceiling by
pinning 500-odd pre-existing figures into receipts that were never written to hold them; that would
be building an instrument, not repairing one. Whichever disposal the measurement supports —
baselining the pre-existing population with the count recorded, printing fewer digits where a row's
own claim does not need the digits, or pinning where the claim does — is stated with its reason and
its number, and the part of it that belongs to another seat's row is **routed**, not edited.

---

## The line between the two parts

They are one revision because they are one turn's order, not because they are one finding. Part 1 is
a reading; Part 2 is a repair to a gate that is quietly not checking. Neither is used to support the
other.
