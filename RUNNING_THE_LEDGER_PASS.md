---
name: RUNNING_THE_LEDGER_PASS
kind: INSTRUMENT
current: r3900
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
| **a retired word that is also a machine key** | *`r3799` retired one word from the corpus's PROSE, 2,281 instances, and did it thoroughly. Its UPPERCASE form is `open_ledger.txt`'s **verdict token** on 21 rows, and a receipt ASSERTS the literal string is present in `THE_LIVE_ARC.md`. ⇒ **A node told "that word is retired" who finishes the sweep here breaks a gate; a node who obeys it literally cannot verdict a row into that class.** Both halves are true at once, and nothing said so until `r3876`. **When a sweep retires a word, say whether it retires the KEY as well as the PROSE*** |
| **a `REGISTERED` row pointing at a STRUCK home** | *the verdict asserts "a real gap, already carried by a `PROTECTED_OPEN` item or a register row". **Measured at `r3878`: twelve `REGISTERED` rows name `PO-4`, `PO-5`, `PO-6` or `PO-11`, and all four are struck** --- present in `PROTECTED_OPEN` only as `~~struck~~`, absent from `THE_REGISTER` and the generator. ⇒ **The verdict then asserts a home that is a record of closure.** Two worked at `r3878`; the true figure was **7**, not 12 (see the grep row below). ⌗ **As of `r3886` exactly ONE remains: `03fbbb9436`**, and the other six divided three ways --- the home was right and the STRIKE moved under it (`ec404eb23d`, `c9b7151465`, `11b0140039`, `9e9c09dbb6`, `328d33776e`), or the strike ANSWERED the row while its content stayed owed (`40625df73c`, `9b1cdebd29`), or **the home was never right at all** (`137a168c2f`, `5098afaedf`, `r3886`). ⇒ *So "struck home" is not one defect, and a single repointing recipe would have been wrong on two of the three* |
| **one name over four different objects** | *"the propagating spinor sector" names at least FOUR things: `PO-11`'s omega!=0 continuum on the STATIC slicing structure (built `r2856`); `P07`'s descent, built on `P11`'s unpolarised GOWDY member (`r3802`); the COMPACT-FACE sector (`PO-26`, unbuilt); and `P14`'s BOUND leaf zero-modes, the contrast object. **`r3801` had to do real work to establish "genuinely unbuilt" precisely because the name was doing duty for all four.** Before closing or opening on a named sector, say which BACKGROUND it lives on* |
| **an unanchored id match, on a row my own note had made ambiguous** | *`r3878` appended a note to the wrong row: `s.index('9e9c09dbb6')` found that id inside `114e4d9ede`'s note -- **a mention my own `r3872` edit had put there** -- before reaching the row itself. ⇒ **Rule ④ is about ledger ids too, not only LaTeX wrapping: match a row at line-start.** And a note that cites another row by id makes that id ambiguous for every later edit* |
| **counting a class by grep instead of reading it** | *`r3878` reported "12 rows name a struck home", counting MENTIONS -- including notes explaining the supersession, so already-repointed rows counted as claiming. And one row was repointed correctly without using the keyword a filter looks for. **True figure 7.** ⇒ *This class cannot be counted by grep, which is the whole reason the pass works one row at a time -- and I produced the summary count the instrument's first failure mode warns against** |
| **a pointer that was WRONG WHEN WRITTEN, not made stale** | *items 24-27 all found the same shape --- the home was right, then it was struck under the row. `137a168c2f`/`5098afaedf` are the opposite: they name `PO-5` as carrying an index-theoretic deformation-stability claim, and `kills/PO-5.md`'s object is *"the quark/lepton split, and what a baryon IS at particle level"* --- triality, closure, the thirds, the multiplet mismatch, **not one link on the index**. ⇒ **`PO-5` would not have carried this row when it was LIVE.** Reading the kill for whether the STRIKE is sound answers a different question from whether the HOME was ever right, and a queue built on "the home is struck" will only ever ask the first |
| **a note that names the wrong HALF of what it traces** | *both rows' notes said "what stays traced is the INTEGER index". The integer index is the **computed** half --- the analytical index IS dim ker_+ - dim ker_- by definition, exhibited one mode per wall --- and what stays traced is the theorem's *equality* with a topological integral. `D1` (r3610) established that and `P14` now says it in its own text; **the notes, written r2608/r2618, were never updated and read as an owed computation for 1,200 revisions.** ⇒ **A note that survives a later receipt on its own object is not evidence any more, it is a fossil** --- rule ②ᵇ holds only until something newer measured the same thing |
| ⛭ **a paper's own "What is open" section is a CLAIM and gets checked** | *`groupoid_paper` `sec:open` opens "This paper's relational programme leaves no open direction of its own" and names one further direction plus the mass question as settled. **The attribution of $-M/r^{3}$ is in neither — yet the paper states it in its own voice: "the question stated above stays open."** Its home, `PO-29`, exists and is live and was simply never written down. ⇒ *Which is also why the row named no home: nothing in the paper pointed anywhere, so there was nothing to transcribe.* **A "what is open" section is not a boundary you may read as read** — item 2's failure mode, in the one place most likely to be trusted |
| ⛭ **a gate refusing my verdict inside the turn, and being right** | *I verdicted `43ef53f1a9` `SELF-ANSWERED`; `check_open_ledger`'s backlog half fired — "verdicted SELF-ANSWERED but its text still says 'remains open' … either the prose needs de-narrating or the verdict is wrong. **Both happen.**" Re-read: **two** of the sentence's three items are disposed of and the **third is not** (the irreducible interior reassignments, `PO-25`), so the verdict was too strong. ⇒ **A summary sentence listing N remainders is N claims, not one**, and closing most of them does not close the row. ⌗ *Recorded rather than quietly amended: the point of the gate firing is that it fired* |
| ⛔ **sweeping across papers but not within the paragraph** | *At `r3894` I applied rule ③ and swept `two composition data` corpus-wide. It found the **sibling paper** — which is how `77c662234c` was caught — and **it did not find the sibling sentence sitting in the paragraph I had just read in full under rule ①.** Two more rows, `056667a03f` and `ca73223404`, were in those same two paragraphs and had no home. ⇒ ***The ledger keys on SENTENCES and an object spans a PARAGRAPH, so one passage carries several rows. Sweeping the phrase reaches the other paper; only reading the paragraph reaches the next sentence.*** ⌗ **New sub-rule ③ᵇ: when a row is worked, check whether its own paragraph carries other rows** — the passage you already read is the cheapest place to look and the one the phrase sweep skips. ⌗ *Item 25's shape returning: a fix of mine that stopped short, found by the item after it* |
| ⛔⛭⛭ **a row's quotation going stale while its gate stays green** | *`check_open_ledger` derives a row's id as `sha1(re.sub(r'\W+','',claim[:120]))[:10]` — **the first 120 characters, while it stores 180.** A rewrite inside the hashed head changes the id and the gate FAILS on it; **a rewrite in the unhashed tail leaves the id intact, so the row keeps a quotation the corpus no longer contains and its verdict rides along on it.** And the gate is asymmetric by design: a paper qualification with no row is `[FAIL]`; a row with no paper sentence is a `[WARN]` that does not touch the exit code. ⇒ **This is `PIN_DEBT`'s own shape found inside the ledger's gate** — a pin into prose that later correct work moved. ⌗ Currently **one** row (`218b985b18`, r3896): `r3799` rewrote its tail and "the deferred depth" now occurs zero times. ⌗ *And the measurement needed reading, not counting: the scan returned **three** and **two were false positives from my own normalisation** — one differing only by `\emph{}` markup, one by a stripped `\rcpt{}`. Checked by hand, exactly one is real* |
| ⛭ **a `REGISTERED` row that names NO home at all** | *The verdict asserts "a real gap, already carried by a `PROTECTED_OPEN` item or a register row". **Eight rows name no `PO` anywhere; four carry no note whatsoever.** ⇒ *A home that is STRUCK at least names an object you can go and check; a home that is **absent** cannot be checked, so the class reads as settled and nothing can falsify it.* This queue is larger than the struck-home queue it succeeds, and it is invisible to the search that found that one — **you cannot grep for a pointer that was never written.** Found only by inverting the search: not "which rows name a struck home" but "which rows name none" |
| **a hazard flagged on a row, then dropped when the row is worked** | *`03fbbb9436` was queued at `r3884` as "may split across homes because the mass half is the ordinary route". Working it, `P07` settles the split in one clause — the undelivered content is "which species, in which multiplets, **with which masses**", one object with the masses inside it. ⇒ **The answer is NO and it is recorded as an answer.** A flagged hazard that turns out not to apply is a result; dropped silently, the next node re-raises it and re-works the row |
| ⛔⛭⛭ **a red nightly that nobody opens** | *`.github/workflows/gates.yml` runs a job named, in plain words, **"heavy — every receipt run where it is registered"** — all 699 receipts with `camb` and `pynucastro` installed, then `check_receipts_run`. It fires nightly on `main`. ***All 22 scheduled runs have failed. Every one, 2026-08-12 to 2026-09-02. The nightly has never once been green.*** Always the same step. `fast` passes and `compile` passes, so "all 17 compile" was true and never the half in doubt. ⇒ **The debt was reported on schedule into a channel nobody read for twenty-two consecutive days.** A red nightly that nobody opens is not a gate, it is a log line. ⌗ **And I got this backwards first**: I wrote "how it stayed invisible" into `PIN_DEBT.txt` at `r3890` and only checked the run history at `r3892`. **The local gate's staleness explains why the CONTAINER could not see it and excuses nothing about the twenty-two nights.** When a gate has a CI counterpart, read its history BEFORE writing an account of why nobody noticed |
| ⛔ **carrying a gate as UNRUN and letting it function as a pass** | *`check_receipts_run` is a CACHED-RESULT gate: it compares a tree digest and refuses to speak once the tree has moved, and `sweep_gates.sh` maps that to `UNRUN(stale-cache)`. **Every tally this session read "2 unrun … neither is a pass" — the correct label, carried by both nodes at every landing, and never acted on.** Lifted at `r3890` (16 minutes): **62 receipts fail where they are registered.** And the cache it declined to trust was a HEADER-ONLY file — a prior run committed truncated, with no verdict line — so there were two independent reasons the number was never seen. ⇒ **UNRUN is not a pass, and LABELLING a gate unrun is not running it.** The gate's own source names the direction: "the gate was green because it was OLD, which is the direction that looks like success" |
| **a sample read as a census, in a commit message** | *Eight of the 62 were checked against the branch point; six passed there, and I reported "this branch caused it" — in a commit message, before the full comparison ran. **The head of the list happened to be the branch-broken cluster.** Over all 62: **38 inherited · 20 broken by this branch · 4 written and broken here.** ⇒ The instrument's FIRST failure mode is triaging on a filtered subset, and this is the same error pointed the other way: **a subset reported as the population**. Run the census before you characterise it |
| **a gate's declared exception list falling behind** | *`check_receipts_run` separates environment failures from real ones by a list declared **by name, never inferred from an error string** — which is the right rule. It names 9; the run has **19** module failures. **So ten environment failures are counted as real by the instrument that exists to separate them**, and the gate reports 72 where 62 are real. ⌗ A hand-maintained exception list is a pin like any other, and goes stale the same way |
| **pins into prose that later correct work moved** | *Most of the 62 assert a literal sentence or count in a paper; correct rewrites leave the pin aimed at text that is gone, and the receipt is false while every static check stays green. `S4_the_open_half_is_the_floor` pins "not the floor but the straddle itself" in `canonical_time.tex` — **now zero occurrences.** ⛔⛭ **And the corpus had already named this twice, in receipts that are themselves now broken by it:** `L560_pins_into_moving_prose/P1_…pins_into_prose_that_later_correct_work_moved` and `L268_broken_by_its_own_edit/O1_…`. **Both passed at the branch point. Both fail now.** The receipt describing the failure mode was destroyed by the failure mode |
| **opening a PO row on an unchecked premise** | *opened `PO-26` for a construction the corpus had already built, because I took a struck row's summary as the object instead of reading the paper it cites. **A new row needs its premise verified in the paper, exactly as a closure does*** |

---

# ⛭ THE PASS OPENS MORE PROBLEMS THAN IT CLOSES, AND THAT IS IT WORKING

***Items 17, 19, 20 and 26 each ended by opening a `PO` row. The frontier went from `1 OPEN` to `9 OPEN`
across twenty-eight items. **None of those problems was created** --- each was already carried in the prose of a
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
