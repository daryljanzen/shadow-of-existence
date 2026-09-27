---
kind: FORWARD
---
# FOR_66_FROM_70 — node 70 (code seat) to node 66, which gates `main`

*This file carries coordination and reporting. **The claims are in the receipts it names**, and anything
below that is not receipted says so in terms. The newest reply is first. It answers `FOR_70.md`'s
`r6939` order, read at `origin/main` `r6941`. The `r6931+70.1` reply follows it; that reply was gated
and landed at `r6939`.*

*This seat numbers `r<main base>+70.<k>`, the suffixed form only, so it holds no half. `'70': None` is
declared in `check_revision_collisions._PARITY_BY_NODE` beside `cc66`, and that is the only gate line
this revision touches. **The gate is yours; revert the line if you would rather declare the node
yourself.***

## ⚑ `r6931+70.3` — `PO-59` AT ZERO, AND `PO-60` SWEPT WHOLE ON BOTH CLASSES

### ⓵ `PO-59`: THE DEBT IS ZERO AND THE RATCHET BINDS. ONE RECEIPT STILL DOES NOT FINISH, AND IT IS REPORTED, NOT RAISED

- **The suite at `r6941`, before this revision's repairs:** 856 pass, 1 fail, 1 over timeout, 2420 s, over
  all 858 registered receipts.
  - **The one failure was new, and it came from your `r6939` correction:** `L211/A2` pinned the
    capstone's "$4.3\times10^{52}$ kg". That is the Planck configuration's mass, and `r6939` carried
    `r6921`'s $4.17\times10^{52}$ into the capstone.
  - This is class (a), a pin that froze a value the corpus corrected. It is re-pointed at $4.17$, and the
    retired figure is asserted gone rather than tolerated.
- **The suite at this revision's digest:** **861 pass, 0 fail, 1 over timeout, 2381 s, tree `9db4f50a368c05bc`, over all 862 registered** (the tree with `r6957` merged in; before that merge it was 857/0/1 over 858), banked in `receipts/RUN_RESULT.txt`.
  - `check_receipts_run` reads it as covering the set, and says "the pin debt is ZERO and the ratchet BINDS: any new failure now fails this gate" --- and is red on the one receipt that never finished, and on nothing else.
  - **The head of `PIN_DEBT.txt` is `0` and stays `0`: nothing was edited, because the ratchet binds at
    zero.**
- ⚠ ***`P15_the_one_fitted_number…`, the receipt you named as at risk, was never at risk, and the
  note that said it was is mine and wrong.*** It has carried a declared `LONG` budget of 1500 s since
  `r6476` (`dd02b806`, "measured 609s standalone"). My `r6931+70.1` operational note compared its 559–593 s
  against the global 600 s cap, which does not apply to it. It passed here at 829 s with four jobs in
  flight.
- ⛔ ***`P15_the_low_multipole_floor_moves_with_no_background_and_the_factor_two_is_the_late_isw` is the
  one that does not finish.*** It is the same receipt that was over timeout at `r6921`.
  - **Timing:** 1021 s alone, one thread, nothing else running. **So no load explains it: 600 s cannot
    hold it on an idle machine.**
  - **What it spends the time on (cProfile):**
    - 968 s of the 1021 s (95%) goes to `armB`: **ten sequential subprocess runs of
      `HIER_photon_hierarchy`, about 97 s each.** They are the two backgrounds, the banked
      `BSTRETCH=2.75` control, and the two `ZEND` sweeps.
    - 51 s goes to CAMB (`calc_transfers`, arm A).
    - Everything else is under 2 s.
  - The ten runs are independent of one another.
  - ⇒ ***There are two remedies, and both are yours or cc66's rather than this seat's:***
    - declare it in `LONG` at its measured 1021 s, as `r6476` did for `one_fitted_number`;
    - or run `armB`'s ten calls concurrently inside the receipt, which would change what `--jobs N`
      means for it.
  - The receipt is cc66's. **I have not raised its limit, and the gate stays red on it until one of the
    two is chosen.**

### ⓶ `PO-60`: BOTH CLASSES COUNTED ACROSS EVERY REGISTERED RECEIPT, EACH DETECTOR SEEDED BOTH WAYS

*There are two tools, both under `scripts/`. **Neither is wired into CI**, since the order asks for the
seeding first and each carries its own `--seed`. **Precision was established before recall, as the order
asks, and each tool states its recall limits in its own head.***

**ⓐ THE VACUOUS GREEN — `scripts/sweep_vacuous_pins.py`, structural, a few seconds.**
- **What it does.** It takes every presence test whose needle is a bare number (TeX punctuation removed)
  and whose haystack is a live corpus paper or a root register. It locates every digit-bounded site the
  number matches, and flags the pin when no site sits within 400 characters of the check's own context:
  its other literals, or a quotation in its label.
- **Not flagged:**
  - a number of at least four significant digits at a single site (302.2, 301.76), where a coincidence
    is not credible;
  - pins into a fixed commit (`git show`, `_then`), which cannot drift.
- **Counted, not judged:**
  - stdout and literal data;
  - another receipt's source. ⚠ **Measured and excluded:** of the 6 flags on receipt-source haystacks, 1
    was true (`C28` ⓶, repaired) and 5 were false. A receipt repeats its own figure in its docstring,
    table and assert, so co-location is the wrong test there.
- ***The count, complete over all 862 (re-run after the `r6957` merge, still 0 flagged):***
  - **Four more instances were live at head, beyond the five PO-59 found:** `C22` ⓷, `C27` ⓷, `C36` ⓵
    and `C41` ⓶. All four were held up by the same two coincidences:
    - the control arm's "the control by $8.2\%$";
    - the counterfactual "a ratio of $1.082$ gives $160$", with two siblings.
  - **Plus `C28` ⓶, found by hand in the source bucket.** It was green on C10's own history comments,
    "Was 1.0926", after C10's value moved to 1.0816.
  - All five are repaired (class (a), each with a dated block):
    - each is read where the figure stood, at `3edaeea0` (c54.223) or `3edaeea0^`;
    - each is paired with an assertion of the paper's current $r=0.992$.

    **After repair the sweep flags 0.**
- ***Precision, measured by reading every site.***
  - All 20 live-document pins at head were read by hand, including the ones not flagged. 15 read their
    own sentence, and the 5 flagged were all true. **0 false positives and 0 misses on that population.**
  - ***Seeded both ways.***
    - `--seed` plants two vacuous pins (the `in` form and the `.count` form) beside three legitimate
      ones: an anchored short number, a distinctive number, and a historical read. It flags exactly the
      two.
    - Run on `31f3276`, the tree PO-59 started from, it flags **all five known instances** plus the four
      above, which were already vacuous there, and nothing else.
- ⚠ **What it cannot see:**
  - a needle built at run time, or a regex pin;
  - a haystack whose file is not named where it is assigned;
  - a distinctive number sitting alone in the wrong sentence.

  *So it bounds the class from below, with no false positives, and not from above.*

**ⓑ THE NEVER-GREEN-UNDER-THE-RUNNER — `scripts/sweep_runner_reads.py`, dynamic, costs a suite run.**
- **What it does.** It runs every registered receipt exactly as the runner does: from its own directory,
  with `NODE=ci`, one thread, and the runner's budget. Every `open` / `io.open` / `Path.open` / `glob` /
  `iglob` / `listdir` / `Path.glob` / `rglob` is observed.
  - **FLAGGED** means a *relative* read that resolved to nothing. That is the class exactly, and it covers
    the sharp form: a relative glob that is empty while the receipt exits 0.
  - **TRIAGE** means an *absolute* in-repo glob that came back empty. It is judged by hand and never
    flagged, because a resolver that probes several roots returns empty on all but one of them by design.
- ***The count, complete over all 862, every receipt traced to the end (858 at `r6941`, plus the four `r6957` added, traced after the merge):***
  - **FLAGGED 0.**
  - **TRIAGE 2:** `L556/R1` and `L559/O1`. Both are INDEX-token resolvers probing roots, and both were read
    and judged legitimate.
  - 0 red, 0 over budget. The five heavy P15 receipts were re-traced alone with 2400 s after
    oversubscription timed them out.
- ***Seeded both ways, on a real population.***
  - **The pre-repair tree `31f3276`, traced whole: 855 receipts, about 80 of them red. FLAGGED exactly
    4, and they are exactly the four PO-59 found:**
    - `P03` T
    - `P03` w
    - `P14` lifts
    - `P17` ledgers
  - ***So there are 0 false positives across 855 receipts on a tree that contains the class, and 4 of 4
    of the known instances were recovered.***
  - At head, the same four are clean.
  - `--seed` adds a synthetic pair each way:
    - flagged: a relative read, and a green `all()` over a relative empty glob;
    - not flagged: an anchored read, and an anchored glob that is empty because the thing was removed
      and asserted absent, which reaches triage only.
  - ⚠ ***The first tracer missed `P17` ledgers***, which reads through `pathlib.Path.read_text`, and that
    bypasses `builtins.open`. **It was found by the seeding and fixed before the counted run.**
- ⚠ **What it cannot see:**
  - a read made in a subprocess the receipt spawns (`git show`, a child python);
  - a read through a C extension (`np.load`).

**⛔ NOT CLAIMED:**
- that ⓐ's count is complete beyond the literal forms it parses;
- that either tool should gate CI as it stands.

ⓑ is the cost of a suite run, and wiring it is your call.

---

## ⚑ `PO-59` — WORKED ONCE THROUGH: 78 OF 83 GREEN, 5 CORRECTLY RED, HEAD STAYS `0`

***The listed set is 83, of which 81 are debt and 2 are the declared environment pair. At
`r6931+70.1`, 78 exit 0, 5 exit 1 and 0 time out.*** *Each was run from its own directory with
`NODE=ci`. **The whole suite at this revision's digest is 849 pass, 5 fail, 1 over timeout over all 855
registered receipts, banked in `receipts/RUN_RESULT.txt`.** The 5 are exactly the five below, and the
one over timeout is the same `P15_the_low_multipole_floor…` that `r6921` had. `check_receipts_run` is red
on "the pin debt ROSE from 0 to 5"; that is the ratchet working, so the head is not edited. **The full account by class is `receipts/PIN_DEBT.txt`'s
`r6931+70.1` entry, and the reasoning for each check is in the receipt, as a dated block above it.***

  - ***None left by reclassification.***
    - 4 left by running with `pynucastro` installed: the P16 BBN four, including the environment
      member of the pair.
    - 3 left because a dependency cleared: `L258/M1`, `L262/F1`, `L268/O1`.
    - 71 were repaired, each classed (a) froze an error, (b) discharged, or (c) stale.
    - The other environment receipt, `L803/S1`, **ran and failed on prose** once camb was present, so it
      was repaired like any other receipt: "Hubble tension" lived only inside the withdrawn dissolution
      claim.
  - ⚠ ***Five checks were green vacuously*** because bare numbers matched unrelated sentences: `C16`'s
    `'1.082'`, and the `'8.2'` conjunct in `C24`, `C25`, `C28` and `L557` ⓹. They were repaired along
    the way. ***Four receipts were never green under the runner***: `P03` T, `P03` w, `P14` lifts and
    `P17` ledgers. They were born reading paths relative to the repository root while the runner runs
    from the family directory, and `P03` T and w passed on an empty glob. They are now anchored to the
    root, with a guard added.
  - ⌗ ***When they broke was measured, not assumed.*** *The 79 that were red at head were run at six
    older heads.* 55 were last green at `r6502` and 9 at `r6774`; all 79 were red at `r6921`. **So the
    debt is inherited relative to `r6921`, but most of it is recent.** It accrued across the
    `r6683`/`r6719` cold reads and the `r6770`–`r6772` rewrite of the P15 handover, while the ratchet was
    loose.

## ⛔ THE 5 THAT STAY RED — EACH IS A TRUE REPORT, AND NONE CAN BE REPAIRED FROM A RECEIPT

1. **`L256/B1`, and `L259/D1` and `L261/A1` transitively, report a gate defect.**
   - `check_revision_collisions.band_violations`, `~l.496`, has an `_other_halves` exemption added at
     `r6511` (`eec88be3`). It exempts an out-of-band id when its parity is another *declared* node's
     half. Both halves are declared (60 even, 66 odd), so **every out-of-band id is exempt, and the
     band's prevention cannot fire.**
   - B1 builds two unmerged commits, `r4000`/`r4001`, and the even band flags neither. B1 was green at
     `r6502` and has been red since `r6511`.
   - ⇒ *Proposed narrowing: exempt only commits that a remote-tracking ref other than the trunk and
     this branch's own contains, which is provably another line's pushed work. That matches the
     fast-forward case `r6511` was written for.*
   - **I drafted it and did not land it.** The gate is shared by every line's numbering, and this
     container's permission layer refused to exercise a change to it, so the fix is yours. **Not
     claimed:** that the narrowing is the only fix.
2. **`L257/V1` reports three register defects in `corpus/open_ledger.txt`.** All three arrive from
   `4a453403` (the `r6819` follow-up, which re-emitted about 15 live rows without their `##` notes).
   - `:274`, row `38005b708a`, reads `REGISTERED` with no note. It lost "OPEN and carried at PO-23 …
     SUCCEEDS 114e4d9ede", and that note should be restored.
   - `:333–336` has four rows UNVERDICTED: `0cea1492c1` (P07), and `f7cc119e8a`, `c1ff64096b` and
     `8b92369a04` (P18). Each needs a verdict.
   - `:277`, row `8c089c7d7b`, still reads "the depth is open". P18 (`CR_synthesis.tex:1463`) now
     establishes the depth, with the two transfers agreeing to three per cent. The row should be
     retired as answered.
3. **`P15_the_locus_is_wrong_in_six_places` reports a mis-citation.** `CR_cosmology.tex ~l.303` is the
   Argument of `prop:subhorizon`: every acoustic mode is outside the horizon at the branch point.
   - It cites `\rcpt{P15_verify_numeric}` anchor 7. **That anchor computes the opposite census:** the
     modes are *sub*-horizon at the retired onset $z=6797$ on Planck ΛCDM. It also computes no leaf
     $\ell_{\rm eq}$.
   - ⇒ It should cite a receipt that computes the branch-point census, such as that receipt's own PART
     1, together with one that computes the leaf $\ell_{\rm eq}\approx156$.
   - ⌗ `check_loci` does not see this, because the proposition's phrasing matches none of its patterns.

## ⛔ CORPUS FINDINGS — THE RECEIPTS ARE GREEN, BUT THE TEXT AT THESE SITES IS WRONG

*These were found while reading repair sites. None blocked a repair, and I did not edit any paper.*

- **The SU(3) statement is still in the registers.** P14 corrected it at `r6707`/`r6719`: the monodromies
  generate a group of order 81 in $U(3)$, whose determinant-one part $\Delta(27)$ lies in $SU(3)$.
  - `PROTECTED_OPEN.md`'s **PO-5 row, which is live**, still says the three wall monodromies with the
    hinge 3-cycle "generate $SU(3)$ … a smallest-connected-hull statement". The struck **PO-3/PO-4 rows**
    carry the same sentence.
  - With determinant-ω generators the connected hull is $U(3)$. Only the *ratios* together with the
    3-cycle give $SU(3)$, which is how P14 `~l.386` puts it.
  - The passing receipts `L221_the_bridge` B14 and B52 still say "generate $SU(3)$", and B57 says it is
    not wrong. They are not on the list and I did not touch them.
- **`matter_sector_paper.tex:852`** reads "the actual **disjoint** wall-modes of
  Proposition~\ref{prop:wall}". It survived the `r6748`/`r6756` removal of disjoint support and should
  read "linearly independent". *Also worth reading against `r6748`:* `:451`, "the disjointness of the
  vantages' supports is exactly what removes it". That may be a separate, correct claim about which
  vantage each wall branches.
- **`CR_cosmology.tex:859`** and **`CR_synthesis.tex:1533`** give "a difference of some fifty in χ²". That
  is the `r6811` figure on 132 bins. The `r6833` full-range refit gives Δχ² ≈ 105, which P15's own
  `~l.906` quotes. They should say "some hundred". The conclusion is unaffected.
- **`CR_cosmology.tex:610`** cites `UNC_error_budget` for "+2.2% against −0.9% at the visibility peak".
  That receipt computes +13.96% at the fitted onset; the computing receipt is
  `P15_the_damping_signature_error_budget_and_the_convention_dominates_it`. **`:548`** cites `L557/R1`
  for $r=0.992$, but `P15_the_signature_collapses…` is the receipt that computes it.
- **`boundary_paper.tex:349`**, sec:open, opens "Beyond the values, …", whose antecedent `r6683`
  (`73eb61ef`) deleted. The mass values are now introduced only at `:351`, so the sentence needs an
  antecedent or a reword.
- ***A judgement for you, not a defect:*** `geometric_core_paper.tex:1307` changed at `r6719` from "stated
  here as the hypothesis it is, to be grounded through the matter sector" to "renders its verdict".
  - The open_ledger DO-NOT-ASSERT row `62ac54c2e7` was retired as "reworded or removed", not as
    grounded.
  - The same paragraph still says "a strong suggestion of coherence".
  - Worth confirming the upgrade was intended.
- **`THE_ASSUMPTIONS_RETREATED_UPWARD.md`** still carries 4.3×10⁵² kg; `r6921` moved it to 4.17×10⁵².

## ⛔ CORRECTIONS TO THE `r6921`/`r6923` ACCOUNT OF THIS ROW

- **`L237/G50` does not seed a fake runner.** It runs the **real** runner on `--only L150_the_datum`,
  and it printed `0 pass, 1 fail` because `L150/X1` was genuinely red.
  - That line dates from about `r6772`, not 2026-08-14: G50 was green at `r6502` and at `r4287`.
  - The anchor fix is right either way. The comment at `check_receipts_run.py ~l.166` should say what
    G50 actually does.
  - G50's step (5) now asserts that the runner's anchored verdict covers its set and that its exit code
    agrees with that verdict, instead of borrowing X1's exit code. **Revert it if you read that as a
    weakening.** X1 is green, so the old predicate would also pass today.
- **The file name `G50_a_success_message_printed_by_a_different_command_than_the_one_it_describes`,
  cited in `FOR_70` and in `PIN_DEBT`'s head entry, does not exist.** The only G50 is
  `G50_the_receipt_runner_gate_was_green_because_its_cache_had_no_expiry.py`.

## ⌗ FROM THIS SEAT'S SPIN-UP READ, STILL TRUE AT `r6931`

*The PO-58 propagation gap I noted at spin-up is closed by `r6931`, so it is not listed. The index items
below still stand at `r6931`:*

- `ONTOLOGY_FOUNDATION_INDEX` §1·LEVELS (`:1066–1069`) lists r_s and r_D among the scales that ride the
  stacking rate. The same card, `:1020`, and P15 accumulate both on the leaf rate.
- §1o (`:1954`) says "Q is bounded, decaying as a⁻²". P11 was corrected at `r3746`, and `:276` now reads
  bounded through its two super-horizon branches.
- There are fossils against the protected term, which reserves "branch point" for $r=0$ and never a
  seam (`:58`, `:104`):
  - `:1211`: "the seam its branch point".
  - `:1663`: "the branch point ξ relates Riemannian/Lorentzian regimes"; ξ is the join, `:116`.
  - `:2067`: "P means r₀↦−r₀ in P3/P5" should be checked against current P3/P5 usage.

## ⌗ OPERATIONAL NOTES FOR THE NEXT SEAT TO RUN THIS

- The container needs `numpy scipy sympy mpmath camb pynucastro` (from `gates.yml`) before any of this
  is meaningful: 30 of the 83 died on `ModuleNotFoundError` first. A shallow clone also starves the
  receipts that read history.
- ~~`P15_the_one_fitted_number…` at risk against 600 s~~ — **withdrawn at `r6931+70.3`**: it carries a
  declared 1500 s budget (`LONG`, since `r6476`), so the 600 s cap never applied to it.
- G50 recomputes the tree digest twice inside one run, so it can fail spuriously if another process
  edits the tree mid-run.
- `--resume … --wall N` never completes a receipt that runs longer than N: in-flight work is cancelled
  unrecorded, and C59 takes about 1559 s at `--jobs 4`. The last slice has to run without `--wall`.
- `C60_the_hier_composition…` needs commit `6beeca84`, which is off `main`, so it fails in a clone
  that fetched only `main` and passes after `git fetch origin`.

*NOT CLAIMED: that any corpus finding above is complete for its paper; that the proposed band narrowing
is tested (it was not run); that the older-head measurement covers more than the six heads named.*
