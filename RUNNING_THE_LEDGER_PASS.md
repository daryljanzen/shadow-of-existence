---
name: RUNNING_THE_LEDGER_PASS
kind: INSTRUMENT
current: r3874
job: How to work corpus/open_ledger.txt one row at a time -- the method, the failure modes it was built against, and what each turn must produce.
sources: [chat]
---

# ⛭ WHAT THIS IS

***An instrument for working `corpus/open_ledger.txt` row by row. It was built over one long session by
failing at the job repeatedly and being corrected each time. Every rule below exists because something
went wrong without it.***

⇒ *The ledger holds **every epistemic qualification in the papers**, keyed by a hash of the sentence, with
a verdict. `check_open_ledger` fails when a qualification exists with no verdict. **A grep is not a list
of what is owed — it is a list of places to look, and the looking has to be written down or it does not
count.***

---

# ⛔ THE THREE CLASSES — *there is no fourth*

***Everything that reads as unfinished must end a turn in exactly one of these states.***

| | |
|---|---|
| **CLOSABLE NOW** | ⇒ *close it. In the paper, in real English, with a receipt if it wants one* |
| **NOT CLOSABLE IN A TURN** | ⇒ *it gets a **PO row** in `THE_REGISTER.md`, plus `ORDER`, `GROUP` and `EST` entries in `scripts/regen_frontier.py`. **All three, or the generator throws.** A routing with no live row is a route nobody can walk* |
| **GENERIC SCIENTIFIC PRACTICE** | ⇒ ***remove it.*** *Not retitled, not softened, not kept as a hidden caveat. "Coherence not correspondence", "self-consistency is not soundness" — these dress ordinary standards as this framework's defects* |

⚠ ***Nothing may sit between them.*** *An item swept into obscurity is worse than one left open, because
it cannot be found again.*

---

# ⌗ THE METHOD, one row at a time

**① READ THE WHOLE PASSAGE, NEVER THE ROW.** *The row is a pointer. Nearly every real finding this
session came from reading the paragraph, the section, or the companion the row cites — and would have
been invisible from the row alone.*

**②ᶜ MARK THE ROW `[read rNNNN]` WHEN YOU HAVE READ IT.** *A row worked and found to need no change otherwise leaves **no trace at all**: worked rows are usually retired when the paper sentence they key on is rewritten, so retirement is the record --- but a row that survives its own reading is indistinguishable from one nobody opened. At `r3872` three of ninety-six rows carried the marker against twenty items worked.*

**②ᵇ A ROW'S OWN NOTE IS EVIDENCE, AND SOMETIMES THE BEST EVIDENCE.** *Ledger rows carry the history of their own disputes --- "RESTORED r2621, r2618's dedupe was WRONG" is a previous node's finding, and it caught an error of mine three revisions old. **Read the note, not just the quotation.***

**② FOLLOW EVERY POINTER TO ITS SOURCE.** *If the row cites `PO-n`, read `PO-n` **and** its `kills/PO-n.md`.
If it cites a receipt, **run the receipt**. Registers and papers disagree, and when they do the **paper
governs** — but only after both have been read.*

**③ WHEN A CLAIM CHANGES, SWEEP THE PHRASE CORPUS-WIDE IN THE SAME TURN.* *A claim fixed in one paper is
usually false in four more. One propagating-spinor claim was found in **seven** places across five
revisions because each pass fixed only what it was looking at.*

**④ USE WORD-BOUNDARY AND WRAPPED-FORM SEARCHES.** *Exact-string matching failed **five separate times**
this session because LaTeX wraps across lines. `grep -c "gated"` reported hits that were "investigated";
`[reach]` missed eleven instances written `[reach ---`. Use `re.search` with `\s+` for whitespace, and
`grep -oE "\bword\b"`.*

**⑤ FINISH THE GRAINS.** *`check_depmatrix` moves whenever citations change: **three grains** — P7's
table row, `fig:dependency-structure`'s edge label, and the HTML companion via
`scripts/gen_matrix_html_tbody.py` run from `corpus/`. The gate names the failure exactly: "the same claim
in two places, and only one was refreshed."*

---

# ⛭ WHAT A TURN MUST PRODUCE

*Every one of these, or the turn is not finished:*

- ⓵ **the item worked to one of the three classes**
- ⓶ **all 17 papers compiling at 0 errors, 0 undefined** — `python3 corpus/check_compile.py`
- ⓷ **the sweep green** — `NODE=<n> bash scripts/sweep_gates.sh`
- ⓸ **the open ledger settled** — rewrites change hashes; retire dead rows, verdict new ones
- ⓹ **a commit whose message states what was found, including what was found to be wrong in my own earlier work**
- ⓺ **the tally**: ledger rows · items worked · open problems · **known debts** · gates

---

# ⚠ THE FAILURE MODES THIS WAS BUILT AGAINST

***All of these are mine, from this session. They are listed so the next node does not repeat them.***

| the failure | what it looked like |
|---|---|
| **triaging instead of working** | *"only 3 of 113 are really owed" — handing over a filtered subset is what stops the list being finished* |
| **reporting a boundary as read** | *"the rest are in `%` comments" — a comment misleads a node exactly as much as live prose, because a node arrives by grep* |
| **renaming a mess instead of clearing it** | *found an "Open" section full of closures and retitled the section* |
| **calling a handover a debt** | *wrote "its largest unbuilt undertaking" into an abstract for an item the same paper classifies as a **boundary*** |
| **my own edits going stale within two revisions** | *fixed a claim, then left the same claim standing elsewhere in the same paper* |
| **stopping at the first plausible answer** | *nearly claimed an obstruction sub-Planckian by computing the wrong object* |
| **breaking my own rules in the replacement text** | *wrote "what this paragraph once carried as open" while closing an item --- revision-history narration, the one-state rule, in the very sentence fixing a one-state violation. **The replacement is subject to every rule the original was*** |
| **accepting a paper's claim about its own evidence** | *`P12` said a computation "bears on" an attribution; checked, it predicts the same thing under both readings and discriminates nothing. **A paper's characterisation of its own evidence is a claim, and gets checked like any other*** |
| **reading a fix as a bug** | *nearly sent a builder after the Doppler term because a comment WARNED about it; the warning recorded a correction already made. **A comment naming a hazard is as often a fix as a defect --- check the code, not the comment*** |
| **two instruments reporting the same number and meaning different items** | *the tally's `known debts = 1` is derived from `P15`'s list of four buildable debts and is `PO-24`; the ledger's `NAMED-UNBUILT = 1` was a different population and was `PO-23`. **Neither measurement was wrong and they were never the same count** --- but a reader checking one against the other finds the numbers agreeing and the objects not, which is harder to catch than a disagreement. ⇒ **When two counts are reported side by side, say what each is counted OVER*** |
| **a fix that stops one paper short** | *`r3871` repointed the `canonical_time` row off `PO-6`'s superseded warrant and left the `CR_framework` row, its sibling, still saying "the strike and this sentence agree". **The corpus-wide sweep rule (③) applies to LEDGER ROWS and not only to paper prose*** |
| **opening a PO row on an unchecked premise** | *opened `PO-26` for a construction the corpus had already built, because I took a struck row's summary as the object instead of reading the paper it cites. **A new row needs its premise verified in the paper, exactly as a closure does*** |

---

# ⛭ THE PASS OPENS MORE PROBLEMS THAN IT CLOSES, AND THAT IS IT WORKING

***Items 17, 19 and 20 each ended by opening a `PO` row. The frontier went from `1 OPEN` to `8 OPEN`
across twenty items. **None of those problems was created** --- each was already carried in the prose of a
paper with no register row, which is exactly why nobody could work them.***

⇒ ***A rising count is the instrument finding what was hidden.*** *It falls later, when the rows are
worked. Do not read it as failure and do not slow down to keep it flat --- that is the triage this pass
exists to defeat.*

⌗ ***What must stay near zero is the DEBT count***: *a buildable thing the corpus owes and has not
registered. That is currently **1**, and it is `PO-24`.*

---

# ⌗ WHERE THIS SITS IN THE SEQUENCE

**① this pass** — *every ledger row worked, a true PO list delivered* ⟵ **here**
**②** *the synthesis pass — `WHAT_THE_FRAMEWORK_DELIVERS.md`, which will want its own instrument*
**③** *the PO items themselves, worked against a corpus this pass has made coherent*
