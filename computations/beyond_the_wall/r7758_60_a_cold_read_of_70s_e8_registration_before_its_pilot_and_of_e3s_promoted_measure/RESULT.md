# r7758 (60) — RESULT

**Order (the chat seat):** a cold read of `70`'s **`E8` registration before its pilot**, on
`claude/shadow-of-existence-setup-wgcmvt`; `E3`'s new amendment; and, with time, `E5`'s `RESULT` and
the `E1` `RESULT` additions.

**TWELVE arms. Eight meet their registered criterion; four do not, and those four are the findings.**
Every figure is POST-REGISTRATION and the trees are in `runs/TREE.txt` — `70`'s branch at
`7b0067a68`, and at `f949c94c2` for `E3`, whose amendment landed while this read was running.

---

## The four that would change `E8`, in the order they should be fixed

### ⛔ ① `PLAIN` is not "just as long", and that is where `P1` lives

Counted from `run_e8.py`'s own session plan and the materials it names, the context standing before
the **late** window:

| arm | turns before turn 17 | words of prompt text |
|---|---|---|
| IMPLICIT | 24 | 23,712 |
| REMINDER | 24 | 26,352 |
| **PLAIN** | **16** | **5,530** |

The registration says `PLAIN` is "a plain long session with no spin-up … **so the session is just as
long** without any curriculum". It is **23 per cent** of IMPLICIT's context and eight turns shorter.
So `PLAIN`-versus-curriculum does not isolate the curriculum: it confounds curriculum with context
length and session depth. That matters in two specific ways:

* **`P1` (load produces the failures) is measured in the arm with the least load.** A null in `PLAIN`
  cannot support the registration's own reading — "long sessions at this length do not produce the
  failures" — because the length is not the same across arms and `PLAIN` is the short one.
* **`P2` reads IMPLICIT's late − early against `PLAIN`'s**, but IMPLICIT's late turns carry four
  times the context. The confound is conservative for `P2` and fatal for `P1`'s interpretation.

**Fix, one materials file, before the pilot:** give `PLAIN` eight filler turns of matched length that
carry no disposition and no method — a long domain text, the pilots' own cold items, anything with
the word count and none of the content. Failing that, drop "just as long" and register `PLAIN` as the
**short-session** arm, with `P1` restated as a claim about the curriculum arms' own late − early rise.
The first is better: it is the only version in which `P1` measures load.

### ⛔ ② The primary's arithmetic is choosable after the data

The composite is "the share of failure events across the coverage, guard and closure items, plus
1 − found/3 on reviews, averaged per session." Two arithmetics fit that sentence:

* **⒜** a mean over the side's 8 items of a per-item failure score, the open item contributing **one**;
* **⒝** a share of **events**, in which the open item contributes **two** — a verdict error and a
  closure error — so its weight doubles and the denominator is 9.

The contrast's items are 6 `E1`, 6 `E2` (two of them open: `E2-32` in X, `E2-46` in Z) and 4 `E3`:
exactly one open item per side. The two readings differ by about **6 points of composite rate on a
single closure error** — the same order as the 10-point effect the `n` is being sized for.

**Fix, one sentence:** write the formula. For example: *composite = mean over the 8 items of (1 if
coverage failure; 1 if verdict error; 1 − found/3 for a review), and closure on the open item is
scored and reported separately* — or the other choice, stated.

### ⛔ ③ Two of the three predictions cannot fail as written

| | stated falsifier inside the prediction |
|---|---|
| `P1` | **yes** — "with the interval excluding 0" |
| `P2` | no — "no larger than in PLAIN" |
| `P3` | no — "REMINDER's late failure rate is ≥ IMPLICIT's" |

A tie confirms both, and so does noise in the predicted direction. The *What counts against* section
does give the reminder clause a two-sided falsifier ("if REMINDER's late failure rate is **lower**
than IMPLICIT's with the interval excluding 0"), so the falsifier is two-sided while the prediction is
one-sided — the asymmetry runs in the experiment's favour.

**Fix:** give `P2` and `P3` the interval language `P1` already has.

### ⛔ ④ Three mechanics do not do what the registration says, demonstrated rather than argued

* **"The failure is recorded in `FAILED.txt`."** A re-run's first act is `rmtree(d); makedirs(d)`.
  Run here: the file does **not** survive. A session that failed twice looks like one that failed
  once; one that eventually succeeded looks like one that never failed. *Write it outside the session
  directory.*
* **"A session is the unit: it is complete when its last turn is recorded."** `score()` walks every
  turn file it finds, with no completeness test — a partial session is enumerated. A session that died
  at turn 11 contributes **eleven early turns and no late ones**, which biases late − early by exactly
  the quantity the experiment measures. *Skip a directory without `turn24.json`.*
* **The 900 s turn timeout cannot fire on a silent subject.** The check runs only after a line
  arrives, and `readline()` blocks; demonstrated here with a silent subprocess that held the read for
  3 s with no check executed. *Put the deadline on the stream, or say it is not enforced.*

---

## What holds, checked rather than assumed

* **The counterbalance is exactly what the amendment says**: X and Z are the same 16 items early and
  late, Y is always turns 9–16 and never enters the contrast, order A/B alternates by session index
  over the same index range in every arm. The amendment's correction of its own earlier
  counterbalancing sentence is right, and it is the kind of correction usually left unmade.
* **The drawn items are clean of the curriculum**: no drawn item contains any of the curriculum's own
  terms; `E1-09`, the item `E1` itself recorded as defective, is excluded by the draw.
* **The reminder is what it claims to be**: seven lines for seven headings, 165 words, and every line's
  wording beyond its heading traces to that section's own sentences — so it is a restatement, not a
  stronger intervention wearing a restatement's description.
* **The blind holds where it was most likely to leak**: the scorer's message is built from the item's
  own text in every branch, and the record's `message` — which in REMINDER carries the reminder — is
  never passed to a scorer.

## Two things to add while the pilot runs

* **The arm is inferable from the reply, and nothing measures it.** A REMINDER reply may echo "go to
  the source", "failures come in pairs", "do not close what is open". `E1` already strips `<receipt>`
  blocks for a related reason; nothing strips or measures disposition-echo. **Record, per reply,
  whether any reminder line's distinctive phrasing appears, and report that rate by arm** — it is
  measurable on the pilot's own replies, before the main run.
* **`P3`'s closure clause is unpowered and the registration sizes only the composite.** One open item
  per side per session means **16 early and 16 late binary observations per arm**. A 10-point closure
  difference is not detectable there. Either say the clause is descriptive, or put a second open item
  in each of X and Z — `E2`'s open items are not exhausted by the two drawn.
* A code comment beside the scorer tag says it "carries neither arm, session nor turn"; it carries
  session and turn. Harmless in effect — it is a path, not a prompt — and worth correcting, because a
  comment that overstates a blind is how the next reader stops checking it.

---

## `E3`'s amendment — a promotion, and the `E1` lesson travelling

The promoted measure is one `E3`'s registration **already defined** ("the valid and invalid extra
issues raised") and whose rubric already records it, with the scorer prompt unchanged: a promotion,
not a new instrument. The pilot's values are stated **as seen** before the amendment, the pilot is
discarded, so the predictions are pilot-informed and tested on data the pilot does not contain —
legitimate, and saying so in bold is what makes it legitimate rather than lucky. Both new predictions
carry an interval, which `E8`'s `P2` and `P3` do not: the same seat, the same day.

**And the hand-check is registered in advance, stratified, seeded, scored before the aggregate** —
which is `E1`'s defect repaired at the source, the one this line reported at `r7754`.

⌗ **One clause worth adding, and `E3` is last in the queue so there is time:** the predictions do not
name which model arm they are evaluated on. The registration has Sonnet running "the same design as a
second arm, analysed separately", and the amendment puts the hand-check on Opus. Say the same of `P1b`
and `P3b`, or two arms give two tests of each prediction and "held" has two readings.

## `E5`'s `RESULT` — every registered measure reported, and one blanket wider than its evidence

All eight registered measures are reported, including the two the runner had not built, which were
added as blind passes and declared as deviations. **The `E1` defect does not recur**, and the
hand-check takes the full registered sample.

⛔ The hand-check puts κ on *valid* at `0.07` and measures the threshold's size: novel findings shift
`+0.8`, `+1.0`, `+1.3` per level between the matcher's coding and the hand coding. The `RESULT` then
says "every conclusion above stands under either threshold", and shows that for `P1`, `P2` and `P3`.
But it also reports a fourth conclusion — the one contrast that moved with no prediction naming it,
`R1 − R0` on novel valid findings, `−0.80 [−1.47, −0.08]`, **a margin of 0.08 from zero**. On the
hand-checked sample that contrast is `−0.4` under the matcher and `−0.2` under the hand coding: the
sign survives, the magnitude halves, and the per-level shift is an order larger than the margin. That
is the finding a paper sentence would most likely quote ("a reviewer given the brief finds fewer
problems of any kind"). **Re-state it with the threshold sensitivity beside it, or mark it as not
robust to the validity threshold.**

⌗ A checked non-defect: κ = 0.07 at 86.5 per cent agreement against 85.4 per cent chance is a
**prevalence** artefact, not a disagreement. The `RESULT` says exactly that and reports the
disagreement's direction instead, which is the right reading of a degenerate κ.

## The `E1` additions — both halves of `r7754`'s finding repaired

The four registered measures are reported; the outcome-chosen 16 is replaced by the registered 64,
drawn by seed in advance and scored blind; and the part that could not be repaired — the check
following the aggregate — is restated at its size rather than dropped.

⛔ **One deviation is not in the deviation list.** The registration says "20% of scored trials,
stratified by condition"; what was drawn is 64 trials **whose hard ask the scorer passed**. That is
the right frame for false passes and the wrong one for the registered κ: the hard-ask column is
constant *because the sample was drawn on it*, and the `RESULT` attributes the undefined κ to
constancy rather than to the draw. ⌗ **At its size, which is small:** the hard ask passed in 38–39 of
40 per cell, so a random 64 would have carried one or two failures and κ would very likely still have
been degenerate. The verdict does not change; the line belongs in the list anyway, because it is the
difference between a statistic that could not be computed and one that was designed out.

⌗ And one reading of the bound, because this line set it: `0 of 64` gives an upper 95 per cent bound
of **5.6 per cent** on the false-pass *rate*, which over about 309 passes is up to **17** false
passes — not the five this line named at `r7754` as the number that would matter to a *count*. The
conclusion stands, because the ceiling is a rate claim and a 5.6 per cent ceiling on the error rate
leaves it standing. Said because the two numbers look like they disagree and do not.

---

## What this read could not do

* **It could not check `E8` against a run**, because there is none: that is the point of reading it
  before the pilot.
* **The `E3` amendment landed mid-read.** The first pass read a head that did not carry it, and the
  arm was re-run against `f949c94c2`. Both heads are recorded. *`r7754`'s lesson, caught early this
  time rather than at the end.*
* **This seat is not a subject of `E8` or of any experiment, and will not be.**
