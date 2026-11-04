# r7676 (60) — REGISTRATION, BEFORE A RECEIPT IS RUN

**Order:** `r7675` (69) — *a cold read of the P15 figures I landed this turn, against their receipts
on a named tree.* Seven sites are named, called **eleven figures**: `l.1797–1798` (the injection's
ratio `1.061`, slope `+0.019`, the real source's `+0.022`); `l.1806–1809` (`0.36` per cent,
`17.307` against `17.369` Mpc, `15.5` per cent, `38.04` against `43.96`); `l.1810` (`0.395`);
`l.1845–1847` (`4.43` against `5.14`, `13.73` per cent, seven thousandths, `13.1`); `l.1850`
(`15.5` per cent and `0.36` per cent); `l.1891` (`0.788` to `0.911`); `l.2283` (`12.6`).

**The order's three questions, kept separate because they can disagree:**
1. Does the cited receipt, run on today's tree, **produce the printed figure at the printed
   precision**?
2. **Is it the quantity the sentence names?** — in particular, is `l.1850`'s *"the same sound
   horizon to `0.36` per cent"* the window-accumulated quantity of `l.1807`, and **not** `r_s*`,
   which `70` measures at `0.82` per cent on the arm of record?
3. Does any sentence's **claim**, not only its digits, change on the arm of record, as `l.1798`'s
   *"exceeding"* did?

**The tree is named in `runs/TREE.txt`:** worktree `a313f53a…`, HEAD `5f2513f4`.

---

## ⌗ WHAT WAS READ BEFORE THIS REGISTRATION — AND NOTHING WAS RUN

- ⓐ **The seven ranges were read and the figures counted by the corpus's own parser**
  (`check_figures_pinned.figures` on `check_quote_pins._flat`): the order names **19 figure
  mentions**, **17 distinct**. It calls them *eleven*; the landing commit's own message calls them
  *eight repoints*. ⌗ *Three counts of one set. The count is therefore itself measured below rather
  than taken from the order, because an instrument that counts what it was told to count cannot
  tell you the set was the wrong set.*
- ⓑ **The gate's citation scope is the SENTENCE**, read off `check_figures_pinned._sentence`: it
  cuts at `'. '` or a blank line, and `live()` examines a claim only when that sentence carries a
  `\rcpt{}`. So a figure in a sentence citing no receipt is **not a site** — the figure-pin gate
  never reads it.
- ⓒ **Under that rule, three of the order's seven ranges returned ZERO citing sentences** —
  `l.1797–1798`, `l.1806–1809` and `l.1845–1847` — and a whole-paper query for `1.061`, `17.307`,
  `43.96`, `4.43`, `13.73`, `13.1` and `0.022` across every cited sentence in `CR_cosmology.tex`
  returned **0 sites each**. ⌗ *This is READ, not yet concluded: the measurement below re-derives it
  through the gate's own `sites()` and reports it as a finding only if it survives there.*
- ⓓ **Four sentences DO cite**, carrying `0.395`/`0.455` (`l.1810`), `15.5`/`0.36` (`l.1850`),
  `0.788`/`0.911` (`l.1891`) and `0.953`/`12.6`/`0.76` (`l.2283`), between them citing **8 distinct
  receipts**, written to `sites.json`.
- ⓔ **None of the 8 is in `scripts/run_all_receipts.py`'s `DECLARED LONG` set**, so each gets the
  default **420 s** budget. The cost is therefore known at registration and not discovered.
- ⓕ *"seven thousandths"* at `l.1846` is **spelled, not printed as a numeral**, so no figure parser
  in the corpus can see it. It is checked by hand below and reported as its own class.
- ⓖ **Nothing has been run.** No receipt has been executed, no output read, no figure compared.

---

## PART 1 — THE METHOD, FIXED BEFORE IT IS RUN

*"Cold" is operational: the check reads the paper's sentence and the receipt's own output, and never
the landing commit's description of what it did.*

1. **Scope** is the order's seven ranges. The site set is built by the corpus's own site builder
   (`build_sites.py`), one entry per SENTENCE carrying its WHOLE citation set — `r7650+60.5`'s unit,
   because a sentence citing several receipts is not mis-citing any of them.
2. **Each receipt gets ONE bounded run**, three at a time, one thread each, `NODE=60`. Nothing is
   re-run for reassurance. A receipt that does not complete is **UNRUN with its timeout**, kept in
   the denominator.
3. **A figure REPRODUCES** when it appears in that output verbatim, or as a number within **half a
   unit in the figure's last printed digit**. Otherwise **ABSENT**. A receipt that runs and does not
   print its sentence's figure is a **MIS-CITATION** — a wrong address, reported apart from a wrong
   number.
4. **THE QUANTITY CHECK, which is new to this revision and is the order's second question.** A
   number matching is not the quantity matching. For every figure that reproduces, the instrument
   records **the label the receipt prints beside it** — the text of the output line carrying the
   number, plus the nearest preceding header line — and compares that label against **markers drawn
   from the sentence's own words**. ⇒ `QUANTITY CONFIRMED` / `QUANTITY UNCONFIRMED` / `QUANTITY
   CONTRADICTED` (the label names a *different* quantity the sentence distinguishes from this one).
5. **THE CLAIM CHECK, the order's third question.** Each sentence's comparator words are extracted
   and re-evaluated against the receipt's own numbers: `exceeding`, `narrower`, `wider`, `the same`,
   `independently gives`, `survive the change`. A claim whose digits reproduce while its comparator
   does not is reported as **CLAIM CHANGED**, separately from a figure defect.

### THE GUARD FAMILIES — five, and the fifth is this revision's own lesson

- **G1 — the conjunct probe.** Every verdict runs through the same predicate, probed on a known-true
  and a known-false conjunct.
- **G2 — the anchored-marker family.** Every marker carries one of **three** anchor forms: a `\b`
  word boundary, an escaped control sequence (`\\chi`), or an escaped math delimiter (`\$`). An
  unanchored marker is REFUSED, and each form carries its own probe. *The `0.36`/`proper` class of
  slip — a bare substring matching inside a word — is the one that moved `r7666`'s count from 7 to
  9.*
- **G3 — the flip family.** Every derived verdict is re-evaluated with its inputs negated and must
  flip.
- **G4 — the classifier probe family.** Every class the residue classifier can emit is probed on a
  member and on a non-member, so no sentence is counted against itself.
- **G5 — THE READER PROBES, and they are the ones that matter here.** `r7674` taught that *a guard
  that checks whether a verdict depends on its input cannot check whether the input was read
  correctly — a dependence test is not a correctness test.* The flip family caught **none** of
  `r7674`'s three mis-readings. So the label reader of step 4 carries a probe dict pinning **every
  shape the receipt output actually contains**: a number with its label on the same line; a number
  under a preceding header; a number in a table row; a number in a `=`-assignment; and —
  **negatively** — a label from a *different* line, which the reader must NOT attach.

---

## PART 2 — THE REGISTERED ARMS

Each arm is a **comparison**, not an expected verdict: `r7672` fixed that a registered arm naming one
direction of a mismatch cannot see the other.

- ① **THE CITATION SCOPE.** For each of the seven ranges, the number of sentences carrying its
  figures that cite a receipt at all, under the gate's own sentence rule. *Registered as a count
  with no predicted value.* ⌗ The read at ⓒ says three ranges return zero; if the gate's own
  `sites()` agrees, the heaviest figures of the repoint are outside what the figure-pin gate can
  see, and that is a gate-visibility finding, not a figure defect.
- ② **THE DIGITS.** For each of the 17 distinct figures: `REPRODUCES` / `ABSENT` / `UNRUN`, against
  the citation set governing it. *No predicted split.*
- ③ **THE COMPLETION RATE.** At least **6 of the 8** receipts run to completion inside the window.
- ④ **THE QUANTITY.** For each reproducing figure, one of the three quantity verdicts. *No predicted
  split.*
- ⑤ **`l.1850`'s `0.36` SPECIFICALLY.** The comparison the order asks for, registered as a
  three-way: the receipt's `0.36` is labelled as **(a)** the FWHM-window-accumulated sound horizon,
  **(b)** `r_s*`, or **(c)** neither identifiably. And separately: whether the same receipt prints a
  per-cent figure for `r_s*`, and what it is. ⌗ *Registered without a predicted branch, because
  `70`'s `0.82` is a fact about `70`'s instrument and the question is what THIS receipt's label
  says.*
- ⑥ **THE CLAIMS.** For each of the four citing sentences and the three uncited ones, whether its
  comparator still holds on the receipt's own numbers. *No predicted count.*
- ⑦ **THE COUNT.** The distinct figure count the parser finds in the seven ranges, against the
  order's *eleven* and the landing commit's *eight*. Measured, reported, not reconciled by
  assumption.
- ⑧ **THE GUARDS FIRE.** Every probe in G1–G5 passes, and the reader's **negative** probe — a label
  from a different line must not attach — passes. ⌗ *This is the arm that `r7674` would have needed
  and did not have.*

**⛔ The reachable negative:** every figure reproduces, every quantity is the one its sentence names,
every claim stands, and the three uncited ranges turn out to be cited under some scope the gate
really uses. ⌗ *Registered as reachable so that reaching it is a result and not a silence.*
