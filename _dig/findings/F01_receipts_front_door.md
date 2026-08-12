# F01 — The reproducibility layer's front door is a frozen r2376 snapshot, and one registered receipt cannot run where it is registered

*status: BOUNDED NEGATIVE (verified at source, this cut). No closure written; no registered item struck.*
*scope: `receipts/README.md`, `receipts/INDEX.md` row 206, `receipts/P15_CR_cosmology/ROBUST_p1p2_scan.py`, `receipts/shared/`.*
*method: full suite run — 249 `.py` under `receipts/`, each executed in its own directory, return codes collected.*

---

## The census first, because it is the good news

**248 of 249 receipts return 0** once `numpy scipy sympy camb pynucastro` are present. The one that
does not is a packaging defect, not a computation defect (§C below). Nothing in the reproducibility
layer is computationally broken at this cut. That is the headline and it should stay the headline.

Deps installed to get there: `numpy 2.4.4 · scipy 1.17.1 · sympy 1.14.0 · camb 2.0.1 · pynucastro 2.12.0`.

---

## A. The dependency block understates the tree it guards

`receipts/README.md` §⌗ DEPENDENCIES (recorded r2376, c54):

> The receipt set needs **`numpy`, `scipy`, `sympy`, `camb`** (26 receipts import `sympy`, one imports
> `camb`). Missing deps present as `ModuleNotFoundError`, which is **not** a broken receipt — all 75
> receipts registered at r2376 run clean once these are installed. Install: `pip install numpy scipy sympy camb`.

Measured at this cut:

| README says | tree says | how measured |
|---|---|---|
| 26 receipts import `sympy` | **121** | `grep -rl "import sympy\|from sympy" --include=*.py receipts/` |
| one imports `camb` | **4** direct, **6** that fail without it | `grep -rln "from camb\|import camb"`; plus `P15_full_transfer_verdict.py`, `P15_verify_lowell_boltzmann.py` reach it indirectly |
| — (absent) | **`pynucastro`**, 3 receipts | `P16_theory_error_and_likelihood.py`, `P16_validate_bbn.py`, `bbn_network.py` |
| 75 receipts registered | **248 rows** in `INDEX.md`, **249** `.py` on disk | `grep -c "^| P" INDEX.md`; `find receipts -name '*.py' -not -path '*__pycache__*'` |

The install line is the operative harm. A reader who follows it literally gets three
`ModuleNotFoundError`s in P16 and, having just been told by the paragraph above that
`ModuleNotFoundError` is *not* a broken receipt, has no way to tell whether they have hit the declared
benign case or an undeclared dependency. The paragraph's own reassurance is what disarms them.
`pynucastro` is not exotic — `pip install pynucastro` succeeds and all three P16 receipts then return 0
(`bbn_network.py` integrates to `t_end=29767.1s`, `success=True`).

The `75` is the same defect one level up: a true count at r2376 carried forward in the present tense
across ~108 revisions of growth. Nothing was falsified — the sentence was accurate when written and
was never re-measured. This is the `check_currency` failure mode in prose form: a register that states
its own age only in a parenthetical, and against which nothing ever compares.

**Recommended, and stated for reversal:** re-derive the four numbers at the next cut and mark the block
with the revision it was last *measured*, not the revision it was *recorded*. The distinction is the
whole content of the finding.

## B. The ORIGIN drift debt the README still books as open is closed

Same file, §⌗ THE ORIGIN DRIFT GUARD (added r2376, c54):

> **It currently reports 8 pre-existing divergences**, and in the pairs sampled the `receipts/` copy is
> the *developed* one, so those `ORIGIN:` lines name stale ancestors rather than sources of truth.
> **Each needs per-pair adjudication** — which side is authoritative — and none should be swept.

`corpus/check_receipts.py`, run at this cut, reports:

```
ORIGIN drift guard: 0 unexplained, 15 adjudicated
```

with all fifteen pairs named and marked `ADJUDICATED (documented)` — the six P14 pairs, three P15, two
P03, three P07, and `F_flat.py`. The work was done and done properly: the count went *up* from 8 to 15
as the tree grew, and every one of them carries a documented adjudication. The README simply never
learned about it.

This one is worth naming separately from §A because the sentence does active damage: it is the only
place in the corpus that tells a reader there is unworked debt in the reproducibility layer, and it is
telling them so about work that is finished. Anyone auditing the corpus for open obligations — which
is precisely what a reader of `receipts/README.md` is doing — picks up a phantom.

**Recommended:** replace the paragraph's second half with the live count and the standing invariant
("every `ORIGIN:` pair carries a documented adjudication; the guard fails on any that does not"), which
is the durable statement. The 8-versus-15 number will go stale again; the invariant will not.

## C. `ROBUST_p1p2_scan.py` cannot run in the directory it is registered in

`INDEX.md` row 206 registers

```
| P15 | sec:refit-bound | CRRUN — THE SAME INTEGRATOR ON CR. ... |
  `P15_CR_cosmology/ROBUST_p1p2_scan.py` | OK |
  runs clean; registered r2376 (c54) from its own docstring and a live run | ...
  | storyboard_receipts/ROBUST_p1p2_scan.py |
```

Run in place:

```
ModuleNotFoundError: No module named 'RD_diffusion_direct'
```

Line 52 of the receipts copy is `from RD_diffusion_direct import xe_history, n_H0_of, sigT, Mpc_m, xe_total`.
`RD_diffusion_direct.py` exists at exactly one path in the tree: `storyboard_receipts/`. It was not
copied alongside its dependent, `receipts/shared/` — which `README.md` line 4 designates for
"multi-paper receipts" — is **empty**, and there is no `sys.path` manipulation anywhere under
`receipts/` (`grep -rn "sys.path" receipts/ --include=*.py` → nothing).

With the sibling on the path the receipt returns 0 and prints its full ℓ-scan. So:

- the **computation** is sound — this is not a physics finding and nothing in P15 §refit-bound is in doubt;
- the **registration** is honest — a live run did happen, at the origin, where the sibling is present;
- the **copy** is not reproducible where the reproducibility layer says it is.

That is a narrow gap but it is exactly the gap the ORIGIN guard was invented to close, displaced by one
step. The guard compares a copy's *code* against its origin's *code*. Here the code matches perfectly —
the copy differs only by the added `ORIGIN:` line — and the guard is right to pass it. What did not
survive the move is the copy's **environment**: a receipt is not just its text, it is its text plus
whatever it imports, and the origin's directory was silently part of the artefact.

Three ways to close it, in increasing order of durability:

1. copy `RD_diffusion_direct.py` into `receipts/P15_CR_cosmology/` (fixes this one; invites divergence
   between two copies of a 300-line ionisation solver, which is the disease the ORIGIN guard treats);
2. place it in `receipts/shared/` — its designated home, since `HIER_photon_hierarchy.py`,
   `VALID_hierarchy_damping.py` and three retired-branch receipts also draw on it — and add the one-line
   path shim to its dependents;
3. **extend `check_receipts.py` to import-check**: for every registered `.py`, resolve its non-stdlib,
   non-third-party imports against the tree and fail on any that do not resolve from the receipt's own
   directory. This catches the *class*, not the instance, and it is cheap — a `grep` for `^from X import`
   / `^import X` and an `os.path.exists` per hit, no execution required.

The corpus's own rule applies and points at (3): *a recurring defect wants a gate* — `check_currency.py`'s
docstring, written for L-42. This is the second time a receipt's identity has turned out to be wider
than the guard's model of it (the first was code-versus-origin, which produced the ORIGIN guard). The
second occurrence is where the gate is earned.

---

## What is NOT claimed here

- No claim that any physics result is affected. The one non-running receipt runs, and agrees, when its
  import resolves.
- No claim that the 8→15 change in the ORIGIN count represents newly-found drift rather than tree growth;
  I did not reconstruct the r2376 pair list. Only that the debt the README books as needing work is
  marked done in the guard's own output.
- No closure is written on any registered item. Per `PROTECTED_OPEN.md`, closures on registered items
  are Daryl's; these are bounded negatives on unregistered prose and one packaging state.
