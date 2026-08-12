---
name: s-012-ci-red
kind: FINDING (draft, uncommitted) — operational, and it is the load-bearing kind
current: r2428 / c54.178, HEAD aa2b6ee on main
job: The fast tier's first command exits 1 at HEAD, and `set -e` means the fifteen text gates and the hollow-assertion lint never execute in CI at all. Everything downstream of it passes locally, which is why nothing has surfaced.
sources: [chat]
---

# S-012 · CI's FAST TIER IS RED AT HEAD, AND SIXTEEN GATES NEVER RUN

**`THE_HUB` states what CI buys:**

> *"the **fast** tier: the sixteen text/register gates + all six view `--check`s + `check_id_bands` —
> **every push** — seconds"* … *"what changes is that they run **in CI on every push** rather than
> because somebody remembered."*

⇒ ***They do not run.*** *The step aborts on its first command.*

---

## THE MECHANISM, AND IT IS FOUR LINES OF YAML

`.github/workflows/gates.yml`, job `fast`:

```yaml
- name: the register and view checks
  run: |
    set -e
    python3 scripts/classify_documents.py --check     # ← exits 1 at HEAD
    python3 scripts/regen_teed_up.py --check
    ...five more...
- name: the text gates                                 # ← never runs
- name: the hollow-assertion lint                      # ← never runs
```

**`set -e` aborts the step on the first non-zero exit; a failed step aborts the job.** So on every
push to every branch, CI reports red and **fifteen text gates and the assertion lint are never
executed.**

## THE FAILING CHECK, ON A PRISTINE CLONE

```
$ git rev-parse --short HEAD          aa2b6ee   (main)
$ python3 scripts/classify_documents.py --check
  [FAIL] 28 document(s) unclassified
exit=1
```

*Twenty-eight top-level `.md` files carry neither a `kind:` in frontmatter nor an entry in the
script's explicit tables — among them `RATE_HANDOFF_DERIVATION.md`,
`CR_PERTURBATION_HELD_PICTURE.md`, `CMB_ACOUSTIC_FRONTIER_STATUS.md`, `THE_NEXT_ARC.md`,
`THE_THIRD_ARC.md`, `MATTER_SECTOR_germ.md`, `E1_CITATION_CATALOGUE.md`.*

⌗ **And the script is behaving exactly as designed.** Its docstring: *"The classification is
**DECLARED, not guessed** … Anything that matches neither is reported UNCLASSIFIED, and **the
unclassified count is the step's own done-test**. A guess would be exactly the 'pre-grading a
document you have not opened' move the arc forbids."* ⇒ **28 is ARC 14 step 0 reporting that it is
not finished.** *That is the check working.*

## ⇒ SO THE DEFECT IS THE WIRING, NOT THE CHECK

**A step's *done-test* has been wired in as a *push gate*.** Those are different instruments:

- a **done-test** says *this arc is not finished* — true, useful, and it should stay;
- a **push gate** says *this commit is not fit to land* — which 28 unclassified documents do not mean,
  and which is now blocking sixteen gates that do mean it.

⇒ ***The one check reporting unfinished work is suppressing every check that reports broken work.***

## ✔ AND EVERYTHING DOWNSTREAM IS GREEN, WHICH IS WHY IT HAS NOT SURFACED

Run locally at HEAD on a pristine tree:

| | result |
|---|---|
| the other six view `--check`s | **6/6 PASS** |
| the fifteen text gates | **15/15 PASS** |
| `lint_assertions.py` | **PASS** — *"No hollow assertions."* |
| `run_all_receipts.py` | **288/288 PASS** *(`S-009`)* |

**Nothing is actually broken behind the wall.** *Which is the worst version of this: the pipeline has
been red for long enough that its redness carries no information, and the day something does break,
the signal is a colour that was already that colour.*

⌗ *`THE_HUB`'s own line, turned on itself:* **"an instrument that cannot finish inside the harness
that calls it will be skipped by every caller who does not know that."** *Here the harness finishes;
it just never reaches the instruments.*

---

## ⇒ WHAT TO CHANGE — three options, and the middle one is what I would do

1. **Finish ARC 14 step 0** — classify the 28. *Correct, and it is the arc's own owed work, but it
   blocks sixteen gates until someone does it.*
2. **⛭ Split the step so a done-test cannot mask a gate.** Move `classify_documents --check` into its
   own step (or a separate job), leaving the other six view checks, the fifteen text gates and the
   lint in steps that run regardless. *Then the 28 stay visible as a red done-test, and a real gate
   failure is distinguishable from it.* **This is the smallest change that restores the signal.**
3. **Drop `--check` from the fast tier** and run it at a juncture, as `run_all_receipts` already is.
   *Loses the standing visibility of the count; mentioned for completeness rather than recommended.*

⌗ **And one thing worth doing whichever is chosen: reverse the step order.** *The register and view
checks run before the text gates, so the slowest-to-repair check gates the cheapest and most
diagnostic ones. Nothing requires that order.*

---

## ⌗ TWO SMALLER THINGS FOUND ALONGSIDE

**① The heavy job's dependency line is already right.** `pip install numpy scipy sympy mpmath camb
pynucastro` — *so `S-009`'s point about the container is about the container only, and CI was never
missing the dependencies.* **`THE_HUB`'s prose is what is behind, not the workflow.**

**② Running the receipt suite dirties the tree.** Four tracked PNGs are regenerated in place by
receipts that draw figures — `corpus/figures/CR_hinge_substrate_U3.png`,
`corpus/figures/CR_turnaround_threeness.png`, `figures/U3_hinge_structure.png`,
`receipts/P07_CR_framework/F_flat.png`. *Byte-different, presumably matplotlib metadata.*
⚠ **A node that runs the suite before committing will sweep four unrelated binary diffs into its
commit**, and on a repo where PNGs are LFS-tracked that is not free. *Worth either a `.gitignore`
note, a deterministic-output setting, or a line in `THE_HUB`'s push section.*
