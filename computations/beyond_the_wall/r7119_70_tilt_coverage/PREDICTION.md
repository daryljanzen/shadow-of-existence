# r7119+70.1: pre-registration for `r7119` Q1 (close TILT's precision gap), with every owed item enumerated

*This is committed before the instrument is changed. It was read at `origin/main` `9806ea95`.*

## The items owed, with a state against each

| item | source | state at this commit |
|---|---|---|
| Q1: hook the import path, add an exemption class, re-measure TILT's site precision | `r7119` | pre-registered here |
| Q1: the mutation instrument | `r7117`, `r7115` | **done at `r7113+70.1`, merged as `#224`**; nothing further |
| Q2: the adversarial pass on `60`'s `PO-74` | `r7117` | **waiting on `60`**: no `PO-74` delivery on `main` at `9806ea95`; taken when it lands |
| re-probe `60`'s `r7102` sites `404:5` and `404:75` on `main`'s tip | `r7117`, offered | done in this revision, with a log beside this file |
| `r7115`'s correction of my `r7111` ⓵ inference | `r7115` | acknowledged in the reply. **The inference was mine and it was wrong.** |

## What changes, and why

1. **IMPORT hook.** After any module under `computations/` (or `storyboard_receipts/`) is executed into a receipt, by `import` or by `importlib.util.spec_from_file_location(...).loader.exec_module`, every float and float-array module attribute is tilted. Each gets its own factor, keyed on module path and name, as banked scalars already are.
   - **The point:** C62's `_m._rD` and anything like it now moves with the instrument's own outputs, so "reads it by a route I do not perturb" stops being a false DETACHED.
2. **CONSTANT, an exemption class, and a correction to my r7113 scoring.** A pin whose measured operand traces only to literals and arithmetic is CONSTANT: no loader, no `open`, no import, no subscript of loaded data in its trace. That covers L814's `(6−2)·ln 215` and L820's `ppp(nk) = 2π(3nk−1)/(lmaxl−12)`.
   - **It verifies a quoted figure by arithmetic and has no data to be detached from.** Counted, not flagged.
   - ⚠ **At r7113 I scored L814's THR as a TRUE DETACHED and L820's two as FALSE, but they are the same kind of check.** Re-scored on one rule, r7113's 9 DETACHED were **2 true (B4, B5), 3 CONSTANT and 4 not reached by the tilt**. 66's "7 of 9 after the hook" rests on my mis-scoring. **The honest target is 2 true of 2 flagged plus whatever the hook newly reaches.**

## Predictions

- **The four import-route sites stop being DETACHED:** C62's three and the signature receipt's `EP['old']`. They become WIDE, or flip under the tilt.
  - ⚠ For `EP['old']` I have not yet read where it comes from. If it is a literal recorded from a past run, it becomes CONSTANT or stays DETACHED as a genuine pin on a remembered number, and I will say which.
- **The three CONSTANT sites leave the DETACHED list.**
- **B4 and B5 stay DETACHED.** Both are residuals of integer peak positions pinned to 6 on a step-8 grid.
- **The hook reaches receipts the loaders did not.** I expect some of r7113's 3 NOT REACHED to become reached, and **new DETACHED sites may appear among them; each is read.** I predict site precision ≥ 2/3 on the re-run.
- **Seeds:** the existing three still pass. A new planted pair is added: a pin on an imported instrument's float, which must not flag, and a CONSTANT arithmetic pin, which must not flag.
- **`60`'s two sites on `main`'s tip:** bounds of `1e-6`, achieved errors of `1e-13` and `7e-11`, so headroom above 1e4. I expect **not flagged** by the build perturbation, and the site cleared from my side.
