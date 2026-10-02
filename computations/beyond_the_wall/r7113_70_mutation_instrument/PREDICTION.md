# r7113+70.1: pre-registration for the mutation instrument (`FOR_70.md` `r7113` Q1)

*This is committed before any code. It was read at `origin/main` `59a0bd48`. The only things read so far are the four instances `r7111` names and `scripts/sweep_tolerances.py`, the probe this builds on, which is this seat's own.*

## The items owed, with a state against each

| item | source | state at this commit |
|---|---|---|
| Q1: build the mutation instrument | `r7113` | pre-registered here |
| `P15R234` stays with the gate; `audit.py`'s printed lines are an interface | `r7113` | recorded, nothing to do |
| `PO-73` re-posed; the foundations question goes to Daryl | `r7113` | nothing of 70's: **not adjudicated here, as ordered** |

## What the four instances are, read from their sources, and what each needs

| instance | the check | what it passed on | the operator that catches it |
|---|---|---|---|
| `C41b` (pre-`34c27bf3`) | `len(re.findall('8\.2\\%', p15)) >= 1` | a literal in another lane's prose | **static: PROSE-PIN** |
| `R1` | the `likelihood` word count in P15 pinned `== 35` (and so on) | a word count in prose | **static: PROSE-PIN** |
| `C63`, `P15_the_one_fitted_number_…` (pre-`5cf67290`) | `l1 == want`, with `l1` parsed from `ACOUSTIC_two_arm`'s `peaks at l = [...]` at `LSTEP=8` or 2 | the located peak landing in the same grid bin | **dynamic: REGRID** |
| `60`'s 404 sites | `err < 1e-10` with err at 1e-12 | the numerical floor | **the build perturbation (`sweep_tolerances.py`), which already caught it**. *A negative control here: this instrument should not be the one that flags it.* |

⇒ **Mutating the operand at the comparison itself cannot catch any of them.** Displacing `err` past `tol` always flips. The mutation has to act **upstream of the check**, on what the check is supposed to measure. So the instrument is three operators, each with a stated scope.

## The operators

1. **TILT (dynamic, the generic mutation).**
   - The receipt is run instrumented twice:
     - once clean;
     - once with every float array or number it reads from data in-process (`np.load`, `np.loadtxt`, `np.genfromtxt`, `json.load`) multiplied by a smooth relative tilt 1 + δ·u, with u ∈ [−1, 1] along the last axis and **δ = 0.05**.
   - **δ is larger than any resolution a numeric pin on banked data claims**, so a pin that reads its data must FLIP.
   - **A numeric pin (`PREDICTION` or `EXACT` on non-literal operands) whose verdict does not flip and whose operands do not move at all, in a receipt where the tilt demonstrably reached the computation (≥ 1 other site moved), is `DETACHED`: it asserts something other than the data it is filed against.**
   - Operands that move but still pass are `WIDE` (tolerance ≥ 5 %). They are reported and not flagged.
2. **REGRID (dynamic, for the quantized-locator class).**
   - Every `subprocess` call the receipt makes to `ACOUSTIC_two_arm.py` is intercepted, and its `LSTEP` is changed by one unit. A peak on the new grid moves by **less than one original step**.
   - **A site that passes clean and FAILS under re-gridding claims a resolution finer than its own abscissa: `SUBQUANTUM`.**
   - Scope: only receipts that call the instrument. **It is expensive (one full re-run of each), so it runs on a named list, never by default.**
3. **PROSE-PIN (static).**
   - An asserting comparison against a **non-zero** number, whose measured operand traces within the file to a count of pattern matches (`len(re.findall(…))`, `.count(…)`, `sum` over `finditer`) in text read from `corpus/*.tex`.
   - **Zero is exempt:** an absence claim, such as `C41b`'s surviving half, is not this class.

## Predictions, so a miss is visible

- **Recall on the real instances, run on their historical blobs:**
  - PROSE-PIN flags `C41b` at `34c27bf3^` and `R1` at a revision that pins `likelihood`;
  - REGRID flags `C63` and `P15_the_one_fitted_number_…` at `5cf67290^`.
  - I expect **4 of 4**.
  - ⚠ *The two REGRID runs are 900 s and 1500 s receipts. If the container cannot run the instrument, I report that as not measured rather than predicted.*
- **On their CURRENT blobs**, where the defects were repaired:
  - PROSE-PIN does not flag `C41b`'s repaired absence check;
  - REGRID does not flag `C63` or `OFN`, which now tolerate one `LSTEP`.
  - I expect **0 of 3**.
  - **`R1` is expected to still flag**, because it still pins a prose count by design (r4532's *"pinned to the measurement so a move is looked at"*). *That is the class working as specified, and whether R1's pin is a defect is 66's call, not this instrument's.*
- **TILT, on planted seeds:**
  - a pin computed from a banked array: should **not** flag;
  - a pin on a literal sitting beside a banked-array computation: should **flag** DETACHED;
  - a pin on an integer argmax of a smoothly tilted array: should **flag** DETACHED, the quantized class in-process;
  - a pin on an interpolated (continuous) peak: should **not** flag.
  - I expect **exactly the two planted defects flagged**.
- **Population on the current tree:**
  - **PROSE-PIN: I expect 10–60 sites.** I read every one and report precision. My prediction is ≥ 50 %, and I expect the false positives to be counts used as controls (R1's kind) rather than claims.
  - **TILT: run on a scoped sample of receipts that read banked spectra.** I report the number flagged and read each one.
- **Cost:**
  - TILT is one extra instrumented run per receipt, about the price of one probe;
  - REGRID is one full re-run of each instrument-calling receipt on its list;
  - PROSE-PIN takes seconds.
  - *With the tolerance job's two builds, that is about the "twice the tolerance job" `r7113` accepted.*
