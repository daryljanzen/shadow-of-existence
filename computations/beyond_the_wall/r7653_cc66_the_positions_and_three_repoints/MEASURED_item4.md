# `r7653` item ⓸ — MEASURED: the three-grid truncation on the arm of record (l.1958–1966)

**Instrument.** `computations/beyond_the_wall/r7651_70_three_asks/audit_leafrec1.py`, which is 70's
`r7101_70_three_grid_audit/audit.py` run **unchanged** — the wrapper rewrites one AST node, `GRIDS`, to a
per-run directory of symlinks that resolves `lcdm_*` from the namesake grid and `cr_*` from the
`_leafrec1` sibling, so the imported `rigidity.py` and its `--grid` subprocess driver see the same
resolution. **The measurement is 70's; what is mine is the assertion that the paper quotes it.**

**Reproduced here, this turn.** `python3 audit_leafrec1.py` → exit 0 in **21.5 s**, and its output is
**byte-identical to 70's banked `audit_leafrec1_log.txt`** (`diff` empty). So the audit is cheap and
deterministic, and the receipt can keep driving it as a subprocess rather than reading a log.

---

## ⓵ The truncation scan — the eight cuts, old → new

| cut | n | paper prints | namesake (`r7101` audit) | **arm of record** | moved by |
|---|---|---|---|---|---|
| 850  | 83  | $-1.0$  | −1.0 | **−1.1** | −0.1 |
| 1000 | 100 | $+14.4$ | +14.4 | **+14.2** | −0.2 |
| 1200 | 122 | $+51.0$ | +51.0 | **+49.5** | −1.5 |
| 1400 | 144 | $+67.9$ | +67.9 | **+66.7** | −1.2 |
| 1600 | 161 | $+74.7$ | +74.7 | **+72.6** | −2.1 |
| 1800 | 173 | $+84.0$ | +84.0 | **+81.3** | −2.7 |
| 1900 | 179 | *(not printed)* | +88.3 | **+85.2** | −3.1 |
| 1996 | 185 | $+93.8$ | +93.8 | **+90.2** | −3.6 |

⌗ **The audit has EIGHT cuts and the paper prints SEVEN.** `1900` is in both audits and in neither the
paper nor 69's relay, so the relay is right to give seven: it is the paper's own set. The receipt's
docstring, by contrast, lists all eight and must keep doing so, because its `EXPECT` gate reads the
scan the instrument prints, not the subset the sentence quotes.

⇒ **PREDICTION ⓸ IS FALSIFIED, and on the same clause as the other three.** It said "the paragraph's
reading survives and **only its top figure moves**, 93.8 → 90.2". **All seven move.** The claim's fate
was right; the scope was wrong, and the error has the same shape as ⓵a, ⓵c and ⓶ this turn: I reasoned
from the figure the order happened to name rather than from the table it came out of. Four of five
commitments falsified, each one by reading a neighbouring quantity for the one asked about.

## ⓶ What the paragraph claims, and whether each claim survives

| the paper's claim | namesake | **arm of record** | fate |
|---|---|---|---|
| "more than half the separation already present eight hundred multipoles below the ceiling" | 51.0/93.8 = **54.4 %** | 49.5/90.2 = **54.9 %** | **holds, and by a hair more** |
| monotone above the onset | yes | **yes** | holds |
| "not converged — it grows to the last bin" | +5.5 over the last 96 ℓ | **+5.0** | holds |
| "at every one of those truncations the forbidden configuration sits within about one unit of the control" | max \|forb−ctl\| = **1.1** | max = **0.3** | **holds, and TIGHTENS fourfold** |
| "the bulk of it, about half, falling between ℓ≃850 and 1500" | 29.2 + 23.0 = **52.2 %** | 28.4 + 23.4 = **51.8 %** | holds |
| "a third of the separation on the full-range fit sits there [below the onset]" | 9.3 + 21.5 = **30.8 %** | 10.7 + 21.4 = **32.1 %** | holds |
| "onset falls between ℓ≃850 and 1000" | −1.0 → +14.4 | **−1.1 → +14.2** | holds |
| "already decisive by ℓ≃1200" | +51.0 | **+49.5** | holds |
| $k_{\max}D_M = 3998$ against $\ell_{\max} = 2000$ on each arm | 3998 / 2000 | **3998 / 2000** | holds, unchanged |

**The forbidden-minus-control column in full** (forbidden χ², control χ², difference):

```
  850   68.8  68.7  +0.1      1600  157.6  157.7  -0.1
 1000   77.3  77.0  +0.3      1800  174.6  174.5  +0.1
 1200  102.1  101.9  +0.2     1900  177.5  177.5   0.0
 1400  135.8  136.1  -0.3     1996  186.1  186.0  +0.1
```

⌗ **This is the one place the re-point makes the paper's wording too weak rather than wrong.** On the
namesake the spread ran to 1.1, so "within about one unit" was the honest bound. On the arm of record it
is **0.3** — the forbidden configuration does not merely sit near the control's floor, it sits **on** it
to three tenths of a unit at every one of eight ceilings. **Recommendation for 69: state what it now
measures, "within three tenths of a unit of the control".** "About one unit" stays true, so this is a
wording call and not a correction; the one-state rule is what argues for taking the tighter form.

## ⓷ Two receipt-internal figures that move, and one that strengthens

- **The distances.** The reach gate pins $D_M$ at `14011.5 / 13941.6` Mpc (licensed / forbidden). On the
  arm of record they are **`14134.0 / 14062.0`**, and the ordering the cancellation argument needs
  (licensed longer) is unchanged. The paper does not print either; the gate does.
- **$\ell_D$ and the ceiling ratio.** `1866 → ℓ_max/ℓ_D = 1.072` (licensed) and `1936 → 1.033`
  (forbidden), against the namesake's `1958 → 1.021` on the forbidden arm.
- **The resolved leg counts, and a correction to my own first label.** The per-arm link directories
  hold **19, 20, 20** files. I first wrote that the 19 was a missing `cr_WBm` leg; it is not. Every
  `cr_*` set has **ten** legs (nine CR steps and `cr_base.log`), each direction pair has ten `lcdm_*`
  legs, and the banked pair has **nine** — `refit_grid185` predates log banking, so it carries no
  `lcdm_base.log`. ⌗ *Counted, not inferred, after writing the wrong reason: the same error class as
  this turn's other four.*
- **⚠ THE STAMPED DIFFERENCE NARROWS FROM A PAIR TO A SINGLE KEY, which is the one thing the re-point
  makes strictly stronger.** On the namesake the licensed and forbidden grids differed in
  `{('LEAFGEOM', 'LEAFREC')}` — two keys — because the forbidden grid predated the `LEAFREC` split. On
  the arm of record both arms' `cr_*` legs come from `_leafrec1` siblings, so they differ in
  **`{('LEAFGEOM',)}`** alone, at every one of the nine CR steps. ⇒ The comparison is now like-for-like
  in the stamps as well as in the sampling, and the receipt's verdict line "arms differing in one
  stamped pair" should read **one stamped switch**.

## ⓸ Four gate defects found while re-pointing, and what I did about each

1. **A VACUOUSLY PASSING GATE, and it is mine.** PART 1's control-byte-identical gate reads
   `bool(re.search(r'1 distinct', OUT)) and ('SHA' in OUT or 'sha' in OUT)`. The audit's output never
   prints a hash — but its **first line is a `RuntimeWarning` carrying the path
   `/home/user/shadow-of-existence/...`**, and `'sha' in OUT` matches **`sha`dow**. So the second
   conjunct has been true by accident since `r7109`, on both audits, and the `1 distinct` it ANDs with
   comes from the *ell-sampling* lines, not the control at all. **A vacuous pass is worse than a
   failure.** ⇒ Repaired: the gate now parses the audit's own line, `control: 9 of 9 files
   byte-identical across all three grids`, and requires the two counts equal and at least nine.
2. **`check_figures_pinned` cannot see this table at all.** The paragraph's `\rcpt` sits in its last
   sentence ("no single parameter set fits the low and the high multipoles together"), and `sites()`
   reads **only the sentence carrying the `\rcpt`**. So `+14.4 … +93.8`, nine lines above it, are never
   offered to `pins()` — which is why they are neither pinned nor baselined, and why re-pointing
   `EXPECT` cannot turn the gate red. Verified: 1488 live under 1388 keys against a baseline of 1488,
   green before and after. ⇒ **This is the FOURTH site of the sentence-scope blind spot reported this
   turn** (l.1126–1137's eight figures were the third). It is not mine to fix in a re-point; it is
   routed, with this as the cleanest demonstration yet — a seven-figure table, cited, invisible.
3. **`EXPECT`'s figures were never pins either, for the independent reason.** They live in a **dict**
   iterated in a comprehension, and `pins()` reads constants only inside an `ast.Compare`; the one
   comparison, `abs(scan.get(c, 1e9) - v) <= 0.05`, yields the pin `(1e9, 0.05)`. ⇒ This is the
   container blind spot in its **fourth** container form (dict, after the `_SIX`/`_PIN6` tuples and the
   comprehension). I have added a literal-comparison twin of the eight cuts beside the dict, as I did
   for `_SIX` and `_PIN6`, so the figures are visible to the instrument whatever `sites()` can reach.

4. **AND THE RECEIPT HAD NEVER OPENED THE PAPER WHOSE FIGURES ITS LABELS ATTRIBUTED TO IT.**
   `check_unread_figure` went red on the re-point, on the label "MORE THAN HALF THE GAP IS PRESENT AT
   ℓ ≤ 1200 … the paper's claim". It was right: **a receipt that attributes a number to a paper it never
   reads stays green when the paper moves**, and that is the whole class the instrument exists for.
   ⌗ **This is the fourth time this seat has been told it** — `cc66.89`, commitment 4 of `r7651`'s own
   `PREDICTION.md` ("a figure attributed to the paper is READ OUT OF THE PAPER, not retyped from it"),
   the figure-pin baseline's own note, and here. ⇒ **Repaired by reading, not by softening the label.**
   The receipt's new **PART 6** opens `corpus/CR_cosmology.tex` and reads nine things out of the
   paragraph, testing each against this run of the audit:
   - the seven-figure run and the ℓ bounds it quotes (850 → 1996), **each figure held as a DISJUNCTION
     over the quantity's two states, plus a summary gate forbidding a MIXED paragraph** — so the gate is
     green before 69's landing and after it, and cannot be green for a half-landed one. It reports
     **0 of 7 in the arm-of-record state**, which is the correct pre-landing reading;
   - $k_{\max}D_M = 3998$ against $\ell_{\max} = 2000$, compared with both arms' reported reach;
   - the words "eight hundred multipoles below the ceiling", **tested where the paper's own words put
     it**: 1996 − 800 = 1196, the scan's nearest cut is 1200, and the gap there is more than half;
   - the band "between ℓ≃850 and 1500", checked to be exactly the union of two of the audit's bands;
   - the word "third" for the share below the onset;
   - **the control-tracking bound as a PHRASE, mapped to a number.** `{'about one unit': 1.0, 'three
     tenths of a unit': 0.35, …}`, and an unrecognised wording **fails** rather than passing, because a
     bound the receipt cannot read is a bound it cannot test. ⇒ This is what lets 69 tighten the
     sentence to the measured 0.3 without the gate having to be rewritten first;
   - the onset pair (850, 1000) and the decisive ceiling (1200), against the scan's own shape — negative
     at 850, positive at 1000, more than half by 1200;
   - the clause "it grows to the last bin".

   ⌗ **The instrument's partition is per-SITE, not per-file**, by taint through the file's own
   assignments — so the one surviving attribution is `READS-PAPER` because its verdict depends on a name
   bound from the read, and the PART 3 label that does **not** read the paper now says only what this
   run computes. **43 checks, 43 pass.** Every new gate was perturbation-tested one at a time (the
   literal, the dict entry, the 0.3 bound, the switch key, the band share, the byte-identity equality):
   each one fails alone when its figure is moved, so none is vacuous.

## ⓹ Flagged, NOT asserted and NOT acted on — for 69

- **l.1953–1955's four-ceiling run lengths are from neither audit, and the re-point does not touch
  them.** The sentence says the three configurations are "indistinguishable below ℓ≃800 — every one of
  them with a longest run of eight or nine bins — and separate only above it, where the specified
  configuration's run grows 9, 9, 13, 22 and the forbidden one's stays 9, 9, 9, 12". The audit's
  `longest` column is **identical on both arms** — specified `4, 5, 11, 20, 23, 23, 27, 33` and
  forbidden `4, 4, 4, 5, 7, 8, 8, 8` across its eight ceilings — so no four of them give `9, 9, 13, 22`
  or `9, 9, 9, 12`, and nothing in the audit reads "eight or nine" at the bottom. **Where those figures
  do appear is the PRECEDING paragraph**, l.1941–1946: "the longest run of one sign goes from 18 to 22
  bins" and "the longest run falls from 18 to 12". ⇒ So the four-ceiling scan is measured under a
  **different run-length convention** from the audit this receipt drives, and the paragraph prints both
  conventions eleven lines apart (22/12 at the top ceiling in one, 33/8 in the other). Its source needs
  establishing before it can be re-pointed, and it is cited to **this** receipt, which gates none of it.
- **The audit's contrast coefficients differ from l.1941–1946's.** The audit's own
  `contrast_size.py` GLS model gives, on the arm of record, licensed `cr c = −0.0670 ± 0.0086`
  (−7.78σ) and forbidden `cr c = −0.0092 ± 0.0085` (−1.09σ), against the paper's `−0.0642` and
  `−0.0069 ± 0.0083`. The namesake audit gave the same −0.0670/−0.0092, so **this is not a re-point
  consequence**; the two routes may simply differ, and that paragraph has its own receipt
  (`…the_licensed_configuration_moves_neither_statistic…`), which is why I state it rather than act.
- **70's own `** DIFFERS **` line.** The audit reports `forbidden cr chi2 186.1350 (receipt 184.989)
  crossings 87 (91)`, and `banked`/`licensed cr 276.3597 (receipt 278.795 / 278.788)`. Those receipt
  literals are the namesake's, which the wrapper's docstring says in terms ("on the arm of record its
  `cr` rows print `** DIFFERS **` by construction"). **It is 70's finding to clear in its own
  instrument, not a failure of this receipt**, and none of my gates reads those rows.

## ⓺ What is landed here

`receipts/P15_CR_cosmology/P15_the_three_grid_comparison_is_like_for_like_and_not_a_ceiling_artefact_because_the_projection_reach_is_fixed_on_every_arm.py`
re-pointed onto `r7651_70_three_asks/audit_leafrec1.py`, with the eight cuts, the band shares, the two
distances, the single switch key and the 0.3 bound asserted on the arm of record, the vacuous
control-hash gate repaired, and the per-arm resolution itself gated so the receipt cannot silently fall
back to the namesake. **The paper's wording is 69's to land; nothing in `corpus/` is touched by this
item.**

## ⓻ The six quote-pin keys the paper-read mints, and why each is hard rather than ALT

Reading the paragraph means locating it, and a locator is a quote pin. The operator reports **six** keys
on this receipt, all `PAPER`, and I adjudicate every one **DELIBERATE**:

| the span | tier | why |
|---|---|---|
| `\rcpt{P15_the_three_grid_comparison_…}` | TOKEN | a NAME, which the baseline's header names DELIBERATE in terms; it fails exactly when l.1971 stops citing this receipt |
| `$k_{\max}D_M=(\d+)$ against $\ell_{\max}=(\d+)$` | SENTENCE | shortest span carrying both figures of an **identity**; the grain clause decides it directly |
| `More than half the separation is already present ([a-z]+ [a-z]+) multipoles below the ceiling` | SENTENCE | subject, main verb and whole claim inside the span; shortest that carries it |
| `about half, falling between $\ell\simeq(\d+)$ and $(\d+)$` | SENTENCE | **reshaped**: the paper's leading `with` is dropped, because a span opening on a preposition is DANGLING under the subject rule |
| `a ([a-z]+) of the separation on the full-range fit sits there` | SENTENCE | **reshaped**: the paper's `even though` is a subordinator and would dangle it the same way |
| `its onset falls between … and it is \emph{not} converged---it grows to the last bin` | SENTENCE | **folded into one span**, because the non-convergence clause's own subject is the pronoun "it" and a span cut to it would dangle |

⛭ **None is flagged ALT, and that is a decision rather than an omission.** The two spans this turn *does*
propose rewording — the seven-figure run and the control-tracking bound — are written as disjunctions
with their misses printed loudly, **and the operator does not report either as a pin**, so they need no
row. Every span above carries a claim the re-point leaves standing on **both** arms, so 69 has no reason
to touch it and a hard pin is the stronger form. ⌗ *Both ALT arms were exercised by perturbing the two
patterns: the miss prints, the gate holds, 43 → 42 checks all pass.*

⛔ **Three of the six spans had to be reshaped before they could be adjudicated**, and that is worth
recording as a method note rather than a chore: a locator written to be convenient opens on whatever
word precedes the figures, and the baseline's subject rule is precisely about not pinning a fragment
whose subject lives outside it. Writing the locator to open on its own subject is free at the time and
decides the verdict.
