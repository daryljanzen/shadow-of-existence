# r7676 (60) — RESULT: the P15 figures `r7675` landed, read cold against their receipts

**Order:** `r7675` (69). **Tree:** `runs/TREE.txt` — worktree `a313f53a…`, HEAD `5f2513f4`.
**Registered before anything ran:** `PREDICTION.md`, committed and pushed on its own commit.

**20 figures checked across the order's seven ranges. 20 of 20 reproduce to the printed precision,
and 20 of 20 are the quantity their sentence names. 7 of 7 comparators hold. ⇒ Every figure the
order names is right, and nothing printed is wrong.** What the read found instead sits beside the
figures: a **window named at half its size**, a **cited receipt still entirely on the namesake**, and
**half the figures outside what any gate can see.**

---

## ⓵⓸⓻ THE FIGURES — all three questions, and all three come back clean

| | |
|---|---|
| digits | **20 / 20 REPRODUCE** at the printed precision, 0 absent |
| quantity | **20 / 20 CONFIRMED** by the label the receipt itself attaches to the number |
| claims | **7 / 7 comparators HOLD** on the receipts' own numbers |

The quantity column is the order's second question and it is the one that needed an instrument. A
number matching is not the quantity matching, so every reproducing figure carries **the label the
output attaches to it** — for a table, the header cell whose *character span* overlaps the number's,
with the row's own name prefixed; for prose, the line, plus its block header only when no blank line
intervenes. That reader is what makes `17.369` read `arm | d r_s (own clock)` and not `arm | 17.3074`.

**`l.1798`'s hedge is the right way round.** The injection's ratio `1.061` does exceed the real
source's `1.054`; its slope `+0.019` is **lower** than the real source's `+0.022`, and the paper says
only that it is *"close to"* it. The receipt's own gate calls the slope half of the over-delivery
**FALSIFIED** — so the paper's sentence is the more accurate of the two. ⌗ *`l.1798`'s "exceeding"
attaches to the ratio alone, which is exactly what survives.*

---

## ⓹ THE ORDER'S NAMED QUESTION, ANSWERED — and the name is three-to-one

> *is `l.1850`'s "the same sound horizon to `0.36` per cent" the window-accumulated quantity of
> `l.1807`, and not `r_s*`, which `70` measures at `0.82` per cent on the arm of record?*

**Yes — it is `l.1807`'s own, and the order's reading is right.** Measured off the arm-of-record
geometry bank:

| the quantity | control | arm | arm/control |
|---|---|---|---|
| the sound horizon **accumulated across the visibility FWHM** — `l.1807`'s | 17.3074 | 17.3691 | **+0.36 %** |
| **`r_s*`**, the banked sound horizon at last scattering | 145.3820 | 146.5725 | **+0.82 %** |
| the sound horizon **at the visibility peak** on the arm's own clock | 145.3465 | 147.4648 | **+1.46 %** |

`70`'s `0.82` is the second row, exactly. ⌗ **But the name is three-to-one, not two-to-one**: a third
quantity answers to *"the sound horizon"* at `1.46` per cent. `l.1807` does name its window; `l.1850`
says only *"accumulating"*, and leans on `l.1807` forty lines earlier for which one it means. *Before
two stretches are identified by a label, check how many-to-one the label is on the object — and here
it is three.*

---

## ⛔ ⓸ NOT SUPPORTED — `l.1890` NAMES A WINDOW HALF THE SIZE OF THE ONE ITS FIGURES CAME FROM

`l.1889–1890` prints: *the Jacobian "runs `0.788` to `0.911` across `±3` **half-widths** of the
visibility"*.

- The receipt's own prose says **`+-3 FWHM`**, three times.
- The bank carrying `jac_lo`/`jac_hi` builds its grid as `linspace(ETA_LS - 3*w, ETA_LS + 3*w, 201)`
  with `w = M.ETA_LS_W`.
- `ACOUSTIC_two_arm.py:600` defines `ETA_LS_W` as *"its FWHM in conformal time"*, and the module
  itself uses `ETA_LS ± 3 * ETA_LS_W`.

**±3 FWHM is ±6 half-widths.** Measured with the same `Jac_of` at `geom.py`'s own parameters, over
both windows (`jac_windows.py`, banked in `jac_windows.json`):

| window | Jac lo | Jac hi | spread |
|---|---|---|---|
| `±3 FWHM` — the bank's | 0.7908 | 0.9130 | **12.2 pp** |
| `±3 half-widths` — **the sentence's** | 0.8369 | 0.8946 | **5.8 pp** |

The printed `0.788`–`0.911` is the first row. On the window the sentence names the Jacobian runs
`0.837` to `0.895` — **less than half the spread**. ⌗ *The direction is the understating one for the
sentence's own point: a narrower window makes the two clocks look more alike, so the printed pair is
the stronger reading and the named window the weaker. The digits are right and the window is wrong,
which is why a digit check alone could not find it.*

**Repair is one phrase: `half-widths` → `full widths at half maximum`.** Nothing else in the
sentence moves, and no bank, receipt or instrument is touched.

---

## ⛔ ⓺ NOT SUPPORTED — ONE OF THE FOUR RECEIPTS `l.1850` CITES IS STILL ENTIRELY ON THE NAMESAKE

`P15_the_retention_is_the_combs_average_over_the_kernels_own_k_acceptance_and_the_law_has_no_fitted_coefficient`
reads `r7041_accept_lcdm.npz` and `r7041_accept_cr.npz` — **not one `_leafrec1` form among them** —
while `…the_acceptance_does_not_move…`, cited in the same sentence, reads
`r7041_accept_{digest,Al,sample,nk_slices}_leafrec1.npz`. It also **hardcodes** the namesake's
`d r_s / d chi` in its own prose *and* in the message of the gate that checks the agreement:
`0.454950 against 0.396733`, `12.8 per cent`, where the arm of record is `0.395135` and `13.1`.
`…a_source…`'s own repoint note states that move: `0.3967 -> 0.3951`, `12.8 -> 13.1`.

So **one named quantity has two values in the corpus**, and the paper prints the right one:

| the acceptance, `2 r_s* dk` of acoustic phase | control | arm | narrower by |
|---|---|---|---|
| `…the_retention…` — **namesake banks** | 5.2226 | 4.5364 | **13.1 %** |
| `…the_acceptance…` — **arm of record** | 5.1353 | 4.4301 | **13.73 %** |

`l.1845`'s `4.43` and `5.14` and `l.1846`'s `13.73` are the second row's. ⌗ **And the trap:** the
namesake acceptance narrowing is **also `13.1` per cent** — the same digits as the arm-of-record
*sound-speed* narrowing that `l.1847` quotes. *One number, many-to-one across two quantities and two
arms.* A reader following `l.1850`'s citation into `…the_retention…` finds `13.1` there and `12.8`
for the sound speed — **the opposite assignment** — and the right digits for the wrong reason.

Its agreement gate is `abs(narrow - 12.8) < 5.0`: a **±5 pp** window on a 13 pp quantity, around a
namesake constant. `…the_acceptance…`'s is `abs(mean - 0.131) < 0.01` — 1 pp — and it **declares**
`R6919_NARROWING` a hardcoded constant in its own scope block. ⌗ *So `l.1847`'s "the agreement is
built in nowhere" is defensible as a statement about the physics — the two routes are genuinely
different computations, one of which never computes an acceptance — and the receipt that carries it
says so openly. It is the OTHER receipt, on the namesake with a five-point window, that cannot fail
the distinction it claims.*

**This is routed, not repaired here: the receipt is `cc66`'s repoint territory.**

---

## ⛔ ① THE GATE'S REACH — TEN OF THE TWENTY FIGURES ARE INVISIBLE TO IT

`check_figures_pinned`'s citation scope is the **sentence**: `_sentence` cuts at `'. '` or a blank
line, and `live()` examines a claim only when **that** sentence carries a `\rcpt{}`. A figure in a
sentence citing no receipt is not a site at all.

Through the gate's own `sites()`, over all **329** cited sentences in `CR_cosmology.tex`, **ten of
the order's twenty figures appear in none of them**:

`1.061` · `0.022` · `17.307` · `17.369` · `38.04` · `43.96` · `4.43` · `5.14` · `13.73` · `13.1`

Three of the order's seven ranges — `l.1797–1798`, `l.1806–1809`, `l.1845–1847` — carry their figures
in sentences that cite nothing; the citations sit in the *next* sentence. **Every figure this read
confirmed against a receipt is, for ten of them, a figure the figure-pin gate has never read.** They
are right today because cc66's pass got them right, not because anything would have caught them if
it had not. ⌗ *A gate that is quietly not checking reports the same green as one that is — `r7646`'s
own lesson, on a different blind spot of the same gate.*

**The fork, and I decide it.** Two ways to close it: **(a)** move a `\rcpt{}` into each of the three
uncited sentences, which is three edits and makes the gate read ten more figures; **(b)** widen the
gate's scope from the sentence to the paragraph, which reaches every such site in the corpus at once
and is a gate change on another seat's file. **I recommend (a) now and (b) as a routed question**:
(a) is inside this turn's own subject matter and cannot break anything, while (b) changes what the
gate counts corpus-wide and belongs to whoever owns the gate. Routed either way; neither edited here.

---

## ⌗ TWO RECEIPT PROSE DEFECTS OF ONE CLASS, FOUND WHILE READING THE LABELS

- **`…the_selection…`'s assertion header names the paper's OLD figures.** It reads *"`l.2283-2284`'s
  `$0.953$`, `$12.5$` and `$0.75$`"* while its own measurement, printed two lines above, reads the
  paper as printing `('0.953', '12.6', '0.76')`. The receipt's text disagrees with its own
  computation.
- **`…a_source…`'s `ESTABLISHED` paragraph overclaims.** It says the injection's figures are
  *"exceeding the real source's `1.054` **and** `+0.02178`"*, where its own gate says the slope *"is
  NOT steeper any more"* and prints `slope FALSIFIED`.

⌗ *Both are the class `…a_source…` itself named this turn: "a docstring left on namesake numbers is a
receipt whose own text disagrees with its computation, and nothing in the gates would have caught
it." It is now two instances, and in the second the paper is the more accurate document.*

---

## ⑦ THE COUNT — measured, and it matches neither name given to it

| | |
|---|---|
| the order calls them | **eleven** |
| the landing commit calls them | **eight repoints** |
| the corpus's own parser finds, distinct | **17** |
| this read checked | **20** |

Not a defect; a reminder. ⌗ *An instrument that counts what it was told to count cannot tell you the
set was the wrong set, so the scope was measured before it was trusted — and three counts of one set
is exactly the condition under which a figure gets checked by nobody.*

---

## WHAT THE GUARDS CAUGHT — and the one that had to be ADDED mid-run

`PREDICTION.md` registered five families; the run needed **six**.

- **G5, the reader probes, earned their place twice.** The first reader took the line immediately
  above a number as its header — which in a multi-row table is **another row**, and it labelled
  `17.3691` with `17.3074`. Negative probe ③ (*the header lookup must walk past the rows above*) is
  what states that. The second reader aligned header cells **by index**, which mislabelled a
  **ragged** row: `the REAL source (cc66.41)` leaves the ratio and rms columns blank, so its slope
  sat in cell 1 and took the header's cell 1, `ratio`. Alignment is now by **character span**.
- **Negative probe ④** is the one that matters for the order's question: a word true of the *whole*
  row — `arm`, `control` — must not confirm one of its *cells*. Without it, `4.43` and `5.14` both
  came back CONFIRMED on the same line, and the discrimination was empty.
- **G6, the flattening probes, were ADDED DURING THE RUN.** The claim probe on *"both figures quoted
  above survive the change"* read **False**, because the phrase **wraps** in `CR_cosmology.tex`
  between `quoted` and `above` — and the comparator came back CHANGED when it holds. That rule has
  been standing in this line since `r7664` and was simply not written down as a family. **The
  addition is declared rather than folded back into the registration, because a method changed
  mid-run is a thing to report.**
- **G3, the flip family, caught none of the three.** Again. Every verdict did depend on its reading;
  the reading was simply wrong.

⛭ **The lesson holds and sharpens.** *A guard that checks whether a verdict depends on its input
cannot check whether the input was read correctly.* And this turn adds the corollary the reader
needed: **a label is attached by position, not by presence — a word that is true of the whole row
says nothing about one of its cells.**

---

## THE ARMS, SCORED

| arm | registered as | outcome |
|---|---|---|
| ① citation scope | a count, no predicted value | **10 of 20** figures in uncited sentences |
| ② the digits | no predicted split | **20 REPRODUCES, 0 ABSENT** |
| ③ completion | ≥ 6 of 8 inside the window | **HIT** — 8 of 8, the longest at 345 s of 420 s |
| ④ the quantity | no predicted split | **20 CONFIRMED** |
| ⑤ `l.1850`'s `0.36` | a three-way, no predicted branch | **(a)** the window-accumulated quantity; `r_s*` is `0.82` |
| ⑥ the claims | no predicted count | **7 of 7 hold** |
| ⑦ the count | measured, not reconciled | **17** against *eleven* and *eight* |
| ⑧ the guards | every probe, including the negatives | **all pass**, after three reader slips they caught |

**⛔ The reachable negative was reached on the figures and NOT on their surroundings.** Every figure
reproduces, every quantity is the one its sentence names, every claim stands — and the three uncited
ranges are uncited under the only scope the gate uses. *So the repoint itself is clean, and what is
not clean is what sits around it.*

---

## WHAT IS NOT CLAIMED

- **NOT that `jac_windows.py` re-derives the printed pair.** It runs at `geom.py`'s own committed
  `ENV['cr']`, which is the namesake-era parameter set, so it gives `0.7908`–`0.9130` against the
  arm-of-record bank's `0.787931`–`0.911397`. The comparison made is **window against window at
  fixed parameters**, which is what the question needs; it is not a rebuild of the bank.
- **NOT that `…the_retention…`'s numbers are wrong.** They are the namesake's, computed correctly on
  the namesake's banks. What is wrong is that a sentence printing arm-of-record figures cites it
  beside a receipt that disagrees with it.
- **NOT a gate.** Nothing here adds or changes one; the figure-pin scope question is routed.
- **NOT an edit to any receipt.** Both receipt prose defects and the retention repoint are routed in
  `FOR_66_FROM_60.md`.
- **NOT a claim about `P15`'s physics.** This is a correspondence check between printed digits and
  banked computations on one named tree, and nothing else.
