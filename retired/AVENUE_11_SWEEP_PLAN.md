> **⌖ RETIRED r1546.** This was the execution plan for **avenue 11, the corpus receipt sweep** (r1345). **It ran:** the sweep completed at **r1406** across all seventeen papers, and the corpus is receipt-certified — 22 receipt directories, one per paper. The avenues themselves are `THE_ARSENAL`'s method.
> Kept as record; **do not work from it.**


# AVENUE 11 — THE CORPUS RECEIPT SWEEP: pedantic execution plan
*Written r1334 (Arthur), for handoff to a Cowork seat. Stated for reversal. Daryl-directed.*

> **What this is.** A comprehensive, step-by-step procedure to bring the **reproducibility layer** of the
> corpus up to the bar of avenues 1–10 — every verifiable computational claim in P1–P14 (then P15–P16)
> **traced, run, classified, and organized** into one clean `receipts/` directory with a master index.
> The corpus currently has **304 `.py` files scattered across ~15 directories, only 48 cited by any
> paper, and no index.** The end-state is a `receipts/` directory sitting beside the corpus that covers
> **every** verifiable computation, each with a verdict you can trust because it was *run*, not eyeballed.

---

## 0. WHY, and the payoff (read this first — it is the anti-weasel motivation)
- P15 (cosmology) cites **16** receipts, P13/P14 **9** each — the empirical mass of the corpus lives there,
  and it **cannot be checked** without a trustworthy receipt spine under P1–P14 first.
- Several **open-problems items are computations** with no home; this sweep gives them one.
- The payoff is leverage: once every computation is a standing, runnable, classified receipt, verification
  becomes *re-running the directory*, not re-deriving the physics one "continue" at a time.
- **This work does not get to be "passable." A receipt that is not run is not a receipt. A verdict written
  from a filename or a docstring is a lie.** The whole point is that the next person can trust the ledger
  without redoing the work — which is only true if the ledger was built by actually doing the work.

---

## 1. THE DISPOSITION — non-negotiable, and the specific ways a seat weasels out (CATCH YOURSELF)
Every one of these was a real failure mode this programme has already paid for. Re-read before each paper.
1. **VERIFY, NEVER PERFORM.** Run the receipt. Paste the *actual* stdout into the ledger entry. Trace the
   code line by line and confirm it computes the *claim* — not something adjacent that merely sounds right.
2. **The binary: RESOLVE or ELEVATE. Never a third option.** Every receipt that is not ✔✔ is either
   *fixed* (resolve) or its gap is *added to the open-problems list* (elevate). It is **never** left flagged,
   placeholdered, "noted", or made "passable." A placeholder is just "broken in a different way."
3. **Hold your OWN receipts to the bar.** When you write or fix a receipt, hunt it for the failure modes in
   §5 before you record ✔✔. The pull toward "clean/done/all-clear" is the tell that you have stopped checking.
4. **Run a discriminating control.** A check that cannot return NO proves nothing. Every quantitative receipt
   must include a control that *breaks* when the claim is false (wrong scale, wrong sign, perturbed input).
5. **Deliver.** Bundle after each paper. Work that is not in a tar in Daryl's hands does not exist.
6. **Do not overreach.** Touch only what the step licenses. Do not "clean up", rename, delete, or edit papers
   beyond what a receipt verdict warrants and Daryl has authorized. When unsure whether a change is licensed,
   do the receipt work and *flag the paper-edit question* — do not enact it.
7. **Forbidden phrases in a verdict:** "looks fine", "should work", "appears correct", "all clear",
   "seems to", "presumably", "as expected" — unless immediately followed by the pasted output that proves it.

---

## 2. DEFINITIONS (so nothing gets skipped by redefining it away)
- **Verifiable computational claim** — anything a computation can check: a numeric value/bound, an identity,
  an eigenvalue/spectrum, a factorization, a limit, a fit/χ², an integral, a root structure, a plotted
  curve's underlying numbers, a "one verifies directly that…" in a paper. **NOT** verifiable: prose
  arguments, definitions, ontological readings, citations to the literature. When in doubt, it IS a claim —
  err toward listing it.
- **Receipt** — a self-contained script whose *execution* verifies one such claim, printing a PASS/FAIL (or
  the value to compare against the paper).
- **Classification (exactly one per claim):**
  - **✔✔ VERIFIED** — runs clean; output matches the paper's claim; the code genuinely computes the claim
    (no tautology, no hardcoded answer); a discriminating control is present; honest bounds stated.
  - **◐ PARTIAL** — runs, but overclaims, or only covers part of the claim, or a check is soft/tautological.
    → must be **resolved** (tighten/extend the receipt) or the uncovered part **elevated**.
  - **✗ BROKEN/WRONG** — does not run, or output contradicts the claim, or computes the wrong object.
    → **resolve** (fix/rebuild) or **elevate**.
  - **? UNCLEAR** — cannot yet tell what it computes or whether it matches. → investigate until it is one of
    the above. `?` is never a resting state in a delivered ledger.
  - **∅ MISSING** — the claim has no receipt. → **build** one (if verifiable) or **elevate** (if genuinely
    open / not yet computable). `∅` is never a resting state either.

---

## 3. THE PER-PAPER LOOP (P1 → P14 in order; then P15 → P16)
Do one paper start-to-finish before the next. For paper **P##**:

**A · ENUMERATE (do not skip; do not trust the cited list).**
  Read the paper. Produce a numbered **claim inventory**: every verifiable computational claim, each with its
  section/`\label`, a one-line statement, and whether the paper cites a receipt for it. Include claims the
  paper makes *without* citing a receipt (those are the ones most likely to be ∅). Save as
  `receipts/P##_<name>/CLAIMS.md`.

**B · MAP.** For each claim, locate the existing receipt(s) among the 304 files — search by cited name, by
  filename, and by *content* (`grep` the distinctive quantity). Record the path, or `∅` if none is found.
  Note when one receipt covers several claims, or several receipts one claim.

**C · TRACE.** Open the receipt. Read it fully. Confirm it computes *this claim*. Actively look for the §5
  failure modes. Where feasible, re-derive the key line independently (a second representation, or by hand)
  and confirm agreement. Write two–three sentences: what it actually computes, and how you confirmed it.

**D · RUN.** Execute it (`python3 <path>`). Paste the real output (trim to the decisive lines). If it needs
  inputs/data, note them and ensure they are in the bundle. If it is slow (>~60 s) or needs an unavailable
  package, note that and either shrink it or record the obstacle honestly (do not fake the output).

**E · CLASSIFY.** Assign exactly one of ✔✔/◐/✗/?/∅ with the pasted evidence.

**F · RESOLVE-OR-ELEVATE.** For anything not ✔✔: fix the receipt (and re-run, back to D), or add the gap to
  `THE_OPEN_PROBLEMS_LEDGER.md` with a precise statement of what remains to compute. Record which you did.

**G · ORGANIZE.** Place the canonical, verified receipt in `receipts/P##_<name>/` with the standard header
  (§4). Give it a clear name tied to the claim. Add/So update its row in `receipts/INDEX.md`. (Copy, do not
  move, during the sweep — some receipts have dependencies or are cited elsewhere; a consolidation/dedup pass
  is the final step, §6, once everything is verified.)

**G2 · CITE IN PLACE (standing rule from r1345).** As each receipt reaches ✔✔, cite it in the paper at its
  computation with `\rcpt{<stem>}` (unobtrusive superscript R -> Appendix R), add `\usepackage{receipts}`
  and `\input{appendix_receipts_P##}` once per paper, regenerate the appendix with
  `make_receipt_appendix.py`, and run `check_receipts.py` (every `\rcpt{}` must resolve to an INDEX row +
  a file; zero uncited). This keeps the paper and the ledger in lockstep -- no retrofitting after P3.

**H · DELIVER.** When the paper's inventory is fully ✔✔-or-resolved-or-elevated: recompile the paper (0/0),
  update the changelog, bundle, `present_files`, and give a one-screen status. Then and only then, next paper.

---

## 4. DIRECTORY STRUCTURE & FILE CONVENTIONS (the end-state artifact)
```
receipts/
  README.md            # how the dir is organized + how to run everything
  INDEX.md             # THE MASTER LEDGER (table below) — source of truth
  run_all.py           # runs every receipt, prints a PASS/FAIL summary (built as we go)
  P01_BH_causality/    # one dir per paper, canonical verified receipts + CLAIMS.md
  P02_janzen_circle/
  ... P14_matter_sector/
  shared/              # receipts a claim in >1 paper depends on
  opens/               # receipts-in-waiting for open-problems computations (∅/◐ with a plan)
```
**INDEX.md is a table**, one row per claim:
`| paper | §label | claim (one line) | receipt file | status | what it computes | honest bound | origin path |`

**Every receipt file starts with a standard header docstring:**
```
"""
<receipt name> -- verifies: <one-line claim>   [<paper> <section/label>]
STATUS: ✔✔ | ◐ | ✗ | ? | ∅        RUN: python3 <file>        RUNTIME: ~<n>s
COMPUTES: <what it genuinely computes, and the discriminating control>
BOUND: <what it does NOT establish — the honest edge>
ORIGIN: <original scattered path it was canonicalized from>
"""
```
Receipts must be **self-contained** (list imports; bundle any data they read), **deterministic** (seed any
RNG), and **fast** (shrink grids; if a full run is heavy, keep a fast mode + note the full parameters).

---

## 5. THE ANTI-WEASEL CHECKLIST (hunt every receipt for these — they are all real, from this corpus)
- [ ] **Stamped from the name/docstring**, never run. (Fix: run it, paste output.)
- [ ] **Tautology** — the check is `X == X` dressed up. Real examples killed here: `comm(g5,g5)==0`;
      `S3 == S3`; "W matches W" where W was defined to match. (Fix: compute the claim from independent inputs.)
- [ ] **Hardcoded answer** — the "expected" value is the answer typed in, so the test cannot fail.
- [ ] **Assert-then-confirm-its-property** (the P1 lesson, r1334) — asserting the object in closed form and
      checking it has the claimed property is soft (e.g. writing g_tt=−(1−r_h/r) then checking it vanishes at
      r_h). DERIVE the object from more primitive inputs (invert the metric; run the actual coordinate
      transformation; substitute into the governing equation) so the check tests the *derivation*, not the
      typed-in form. If the derived cross-terms/side-quantities also come out standard, the derivation is real.
- [ ] **No discriminating control** — nothing in the receipt breaks when the claim is false. (Fix: add one.)
- [ ] **Overclaim** — receipt computes a piece, the paper (or the receipt's own print) claims the whole.
- [ ] **Missing receipt papered as present** — a placeholder, a stub, or a comment standing in for a run.
- [ ] **Cited receipt absent** — the paper cites a `.py` that is not in the bundle. (Fix: find it, rebuild it,
      or correct the citation — flag the paper edit.)
- [ ] **Fragment/aliasing** — the paper's citation and the file disagree in name; confirm they are the same object.
- [ ] **Silent dependency** — reads a data file or imports a module not in the bundle. (Fix: vendor it in.)

---

## 6. FINAL CONSOLIDATION PASS (after P1–P14 are all at bar)
- Dedup by content-hash; where the canonical `receipts/` copy is byte-identical to a scattered original and
  nothing else imports the original, remove the original (md5-verify first; paper citations are by *name*, not
  path, so a move does not break a paper — but a receipt that *imports* a moved module does).
- Build/finish `run_all.py`; confirm the whole directory runs green (or the non-green are exactly the
  elevated-to-opens set, listed).
- Cross-check `INDEX.md` against the papers: every cited `.py` appears; every ✔✔ row has a runnable file.

## 7. THE BAR (definition of done — per paper, and overall)
- **Per paper:** every verifiable claim is ✔✔ **or** resolved **or** elevated (nothing `?`/`∅`/dangling);
  its `CLAIMS.md` and `INDEX.md` rows are complete; the paper compiles 0/0; the bundle is delivered.
- **Overall:** P1–P14 all at bar; `INDEX.md` complete; `run_all.py` green-or-accounted-for; opens-list
  computations each have a home in `receipts/opens/`. *Then* P15–P16, where the empirical payoff is.
