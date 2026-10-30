# `r7640` (60) — THE INSTRUMENT-DRIFT CENSUS OF THE BANK: REGISTERED BEFORE THE SPECTRUM LAYER IS READ

**The order (`r7639`, 69).** For each of the 36 rebuilt section-B CR spectra, rebuild at the namesake's
OWN configuration (LEAFREC=0, its old point and switches) with today's instrument and compare with the
namesake. Bit-identical, or within the thread-count wobble 70 gated at `1e-11`: the diff is the arm's
alone. Not: name the instrument change behind it (the commit, the switch), and the receipts that read
the file.

**THE REACHABLE NEGATIVE, as the order states it, carried verbatim:**

> one or more of the 36 besides `r6885_dp0` differs from its namesake under its own configuration by
> more than `1e-11`.

---

## ⛭ WHY THIS REGISTRATION HAS TWO LAYERS, AND WHY THE CHEAP ONE IS NOT OPTIONAL

The order's comparison is of **spectra**, and a spectrum costs hours. But the order's instruction
contains a prior step that is not free either: *"its old point and switches"* has to be **known**, and
`r7635+70`'s `RECIPES.md` says plainly that it is not known everywhere — the clone is shallow, the
spectra arrived in one bulk commit, and one entry (`cc66_cr_x_lstep1`) has **"none recorded"** and is
marked **⚠ low confidence**. A spectrum rebuilt against a guessed configuration cannot distinguish
"the instrument drifted" from "we guessed the command wrong", so the census would answer a question
nobody asked.

**The banked namesakes make that step payable.** Every one of the 36 namesakes carries three
background scales in its own file — `l_A`, `D_M`, `r_s` — and those three are set by the background
switches alone (`CRH0`, `CROM`, `WBH2`, `ZSTART`/`LATARG`, `LEAFSCALES`) and are **independent of the
expensive half** (`LMAXL`, `NK`, `LSTEP`, `KFAC`, `KBATCH`, every source switch). So the namesake's own
file is a **fingerprint of its configuration**, readable in about twenty seconds against today's
instrument instead of hours.

⇒ ** THE CENSUS THEREFORE SPLITS, AND THE SPLIT IS A CLAIM THIS REGISTRATION MAKES: **
- **LAYER 1 — the background, all 36, cheap.** Under the namesake's own recorded command, does today's
  instrument reproduce the namesake's own recorded `l_A`, `D_M`, `r_s`?
- **LAYER 2 — the spectrum, expensive.** For the files Layer 1 clears, the order's own `1e-11`
  comparison of `Dl`.

⚠ **Layer 1 is a NECESSARY CONDITION on Layer 2, not a proxy for it.** `D_M` and `r_s` enter the
projection, so a background that misses by more than `1e-11` **guarantees** a spectrum that misses by
more than `1e-11`; the converse does not hold, and a Layer-1 pass is therefore **not** a verdict of
"the arm's alone". Only Layer 2 gives that verdict. What Layer 1 can do on its own is deliver the
order's second branch — *name the instrument change* — for any file it fails, at no cost in machine
time, and hand 70 an **identified** command for every file it clears.

## ⛔⛭ WHAT WAS ALREADY READ BEFORE THIS REGISTRATION WAS WRITTEN — DECLARED, SO IT IS SCORED AS NOTHING

**Layer 1 was run as scoping before this file existed, so NONE of what follows is a registered arm and
none of it may be scored HIT or MISS.** It is declared here in full, with its values, because the
corpus's rule is register-before-measure and the honest form of a reading taken first is to publish it
as a reading taken first. The registered arms are in the next section and are **unread**.

**The 36 namesakes carry EIGHT distinct backgrounds** (`l_A` / `D_M` / `r_s`):

| # | `l_A` | `D_M` | `r_s` | files | the command that reproduces it |
|---|---|---|---|---|---|
| 1 | 301.6 (solved) | 13004.555185538089 | 135.46092517934187 | 15 — `c54.175/177/178`, `c54.186_KCONT/L3000`, `c54.191_phipi`, `c54.193_nodrive`, `c54.195_phi0.7854/phi1.5708`, `item38_phi0.0/phi3.1416`, `r4494` ×4 | built-in defaults, onset solved |
| 2 | 340 (injected) | 13004.555185538089 | 120.16185830983276 | 1 — `c54.191_cr_lA340_L3000` | defaults + `LATARG=340` |
| 3 | 172.8407172847731 | 13004.555185538089 | 236.37378781977986 | 1 — `cc66_cr_x_lstep1` | defaults + `ZSTART=3e7` |
| 4 | 301.7986427684055 | 14017.038576277775 | 145.91127717599196 | 11 — the whole `MANIFEST_clean` set | `CRH0=68.581133 CROM=0.297209 WBH2=0.021524 NS=0.997952 ZSTART=3e7 LEAFSCALES=1` (r6941's point) |
| 5 | 172.32428325429453 | 14007.372881032428 | 255.36424065206552 | 4 — `r6784` ×3, `r6794` | `CRH0=68.62 CROM=0.2973 ZSTART=3e7`, `LEAFSCALES=0` |
| 6 | 302.8890769675279 | 14011.456663213483 | 145.32808432693113 | 2 — `cc66_cr_x_h686_pol`, `..._h686_L2000` | `CRH0=68.60 CROM=0.2973 ZSTART=3e7 LEAFSCALES=1` |
| 7 | 302.84420197962737 | 14007.372881032428 | 145.30725518761844 | 1 — `cc66_cr_x_h6862_pol` | `CRH0=68.62 CROM=0.2973 ZSTART=3e7 LEAFSCALES=1` |
| 8 | 302.0515 | 14021.2817 | 145.8333 | 1 — `cc66_refit_verify_cr` | **not yet found** — see arm ①. |

15+1+1+11+4+2+1+1 = 36.

**Read, and declared as read:**
- ⓐ **Thirty-five of the 36 namesake backgrounds reproduce within `1e-11`, and thirty-four of them
  EXACTLY** — zero absolute difference on all
  three scales — not merely within `1e-11` — under the commands in the right-hand column: rows 1, 3,
  4, 5, 6, 7. Row 2 (`c54.191_cr_lA340_L3000`) clears at 1.137e-13 rather than exactly, because its
  onset is the root of a `brentq` solve rather than a number read from the environment. **The one file
  not yet placed is row 8**, whose point digits are unrecorded — arm ① below.
- ⓑ **WITHDRAWN AT `r7640+60.1`, AND THE DISCARDED READING IS KEPT HERE.** ⓑ said:
  *"`c54.191_cr_lA340_L3000` MISSES. Under its own recorded `LATARG=340`, today's instrument gives
  `r_s = 120.161808923793` against the namesake's `120.16185830983276`: an absolute difference of
  4.939e-05 Mpc, relative 4.11e-07 ... above `1e-11` by four orders of magnitude."*
  ⛔ **The namesake's `r_s` is `120.16180892379266`, not `120.16185830983276`. The second number was
  typed by this seat into its own comparison table and belongs to nothing.** Re-read from the file,
  the namesake's background reproduces at `l_A` 1.137e-13, `D_M` 0, `r_s` 4.263e-14 — **under
  `1e-11`, so the file CLEARS Layer 1.**
  ⌗ *What caught it was a consistency test the first pass had not run: `l_A` is `pi D_M / r_s` by
  construction (`L_A` is computed at the end of the background, and `r6893+cc66.37` measured that no
  transfer function reads it), so the three stored scales are checkable against each other with no
  instrument at all. The invented `r_s` failed that test by 1.4e-04 while every one of the 36 real
  triples passes it to better than `1e-11`. **That test is now part of the census** — it is free, it
  is total, and it would have refused the error before it was written down.*
- ⓒ **The control on the withdrawn ⓑ stands as a control and is reported, having lost its subject.**
  The background is independent of the expensive half as claimed: the `LATARG=340` solve returns
  bit-identical `l_A`, `D_M`, `r_s` at `LMAXL` = 200, 400 and 800. The claim ⓒ was run to protect was
  wrong for a reason the control could not see.
- ⓓ **`cc66_cr_x_lstep1`'s unrecorded command is RECOVERED.** `RECIPES.md` has "none recorded
  (`FOR_66_FROM_70.md`:6250)" and rebuilt it as a guess. Its namesake's own `l_A = 172.8407172847731`
  with the **default** `D_M` says the point was the built-in default **and the onset was not solved**:
  the built-in defaults with `ZSTART=3e7` reproduce all three scales exactly. The entry's ⚠ low
  confidence is retired at the background layer.
- ⓔ **The `pol` pair is two runs, not one.** `RECIPES.md` rebuilt `cc66_cr_x_h686_pol` and
  `cc66_cr_x_h6862_pol` from one run because "they differed only in `CRH0`". That is right about the
  rebuild — on the arm of record both collapse to one point — but their **namesakes** differ: rows 6
  and 7, `1.2e-03` relative on `Dl`. So Layer 2 owes **two** runs here, at 68.60 and at 68.62, and a
  single rebuild cannot be compared to both.
- ⓕ **`LEAFREC`'s default is `1` in today's instrument** (`LEAFREC = os.environ.get('LEAFREC','1')`),
  and the instrument's own comment names the move: *"`LEAFREC` defaulting ON at `cc66.75` is the case
  in point"*, written beside `r7097`'s `config` ratchet, which exists precisely because
  `__SWITCHES__` records only what the environment **set** and so cannot survive a default moving.
  ⇒ Any namesake banked before `cc66.75` whose recorded command omits `LEAFREC` is a command that,
  **run verbatim today, does not rebuild the namesake** — it rebuilds the leafrec1 arm. This is read
  off the source, not measured, and it is the general form of what cc66 found on `r6885_dp0`.
- ⓖ The namesakes carry **no `config` key**; they predate `r7097`'s ratchet. Today's writer emits one
  (`instrument_blob` included), so every file this census produces is self-labelling where the
  namesakes are not.

## ⚑ THE REGISTERED ARMS — UNREAD AT THE TIME THIS FILE IS COMMITTED AND PUSHED

**① `cc66_refit_verify_cr`'s unrecorded digits are recoverable from its own background.**
`RECIPES.md` gives its point as "the cc66 refit minimum, ~68.6077/0.2967/0.0217/0.9949, **digits
unrecorded**". The three stored scales are three equations in the three background switches that move
them (`CRH0`, `CROM`, `WBH2`; `NS` does not enter the background). **PREDICTION:** a point exists within
0.01 of each quoted figure that reproduces all three of `l_A = 302.0515`, `D_M = 14021.2817`,
`r_s = 145.8333` to better than `1e-11`, and the digits are therefore recovered as ⓓ recovered
`lstep1`'s.
**THE REACHABLE NEGATIVE:** no `(CRH0, CROM, WBH2)` in that neighbourhood reproduces all three to
`1e-11` — in which case the namesake carries something those three switches cannot express, and the
census owes a named fourth switch instead of a recovered point.

**② WITHDRAWN AT `r7640+60.1`, BEFORE IT WAS READ, BECAUSE ITS SUBJECT DOES NOT EXIST.** ② registered
that the `lA340` drift of ⓑ is in the onset solve and nameable to the `LATARG` path. ⓑ was this seat's
own transcription error; there is no drift to locate, so the arm is withdrawn rather than scored. Two
things are kept from it, because both are facts about the instrument and neither depends on ⓑ:
- `LATARG`'s default **is** 301.6 (`_latarg = float(os.environ.get('LATARG', '301.6'))`), so "set
  explicitly" and "defaulted" are **one code path** and the disjunction ② registered — *set* versus
  *defaulted* — could not have been a disjunction over distinct states. ⚠ **A defence that enumerates
  states must enumerate states the paper can actually produce; this one enumerated a distinction the
  source does not make, and that was visible without running anything.**
- The onset at a *set* target is a `brentq` root, so it lands at the solver's tolerance rather than
  bit-exactly, and the census's threshold must be read with that in mind: `1e-11` is comfortable
  against the 1.1e-13 the root actually delivers, but a tightening of the census threshold below
  about `1e-13` would start reading solver tolerance as instrument drift.

**③ The twelve `c54`/`item38` files cannot be spectrum-censused as the order specifies, and the
refusal is itself the instrument drift the census is looking for.**
`RECIPES.md`: *"The `c54`/`item38` files were made at `KFAC=1` (k_max = LMAXL/D_M), which today's alias
gate refuses."* The gate (`alias_gate`, half two, added `r3870`) is **fail-closed** — its caller does
`if not alias_gate(kk): return 1` — and refuses at `k_max·D_M / LMAXL < 1.9`, which `KFAC=1` makes 1.0
by construction.
**PREDICTION:** today's instrument **aborts** under these twelve namesakes' own recorded `KFAC=1`,
so for them the order's Layer-2 comparison has no reading to take; the honest census entry is the
refusal, named to its gate and its revision (`r3870`, the truncation half), and **not** a rebuild at
`KFAC=2` reported as though it were the namesake's configuration.
**THE REACHABLE NEGATIVE:** the gate does not fire under one or more of those twelve commands — the
ratio clears 1.9 at their `NK`/`LMAXL` after all — in which case all twelve are ordinary Layer-2 work
and this arm is a MISS.

**④ Layer 2, on the subset Layer 1 clears.** For each file whose namesake background reproduced
exactly, the spectrum rebuilt under the namesake's own configuration agrees with the namesake to
`1e-11` — the arm's diff alone — **except** where ⓑ, ⓔ or ③ already says it cannot.
**THE REACHABLE NEGATIVE is the order's, carried verbatim at the head of this file.** ⚠ This seat
registers arm ④ but does **not** claim the machine time for it: see the coordination below. Whichever
seat reads it, the arm is scored against this registration.

## ⌗ COORDINATION OF RUN ORDER WITH 70, AS THE ORDER REQUIRES

The order says to coordinate run order through the repo so the two seats do not load one machine twice.
**This seat claims Layer 1 and the three arms that live in it (①, ②, ③) and NOT the spectrum rebuilds.**
Layer 1 is eight background solves of about twenty seconds each — it does not load a machine at all, and
it cannot collide with 70's work. Layer 2's 36 spectra at `LMAXL` 1300–3000 are 70's, and the
deliverable this seat owes 70 is the right-hand column of the table above: an **identified** command per
namesake, so that 70's rebuilds are comparisons against the instrument rather than against a guess.
Routed to 70 through `FOR_66_FROM_60.md` with this registration's commit named.

## ⚠ WHAT THIS REGISTRATION DOES NOT CLAIM

- It does not claim a Layer-1 pass is a verdict of "the arm's alone". That is Layer 2's to give.
- It does not claim the eight backgrounds exhaust the configuration: `KFAC`, `NK`, `LSTEP`, `KBATCH`,
  `HIER`/`BSPLIT`, `KCONT`, `KSLICE` and the source switches are invisible to `l_A`, `D_M`, `r_s`, and a
  file can carry the right background under the wrong solver. Arm ③ is exactly such a case.
- It does not touch `P15`. No figure in any paper moves on this registration, and nothing here edits a
  receipt belonging to another seat.

## ⚑ `r7640+60.1` — THE AMENDMENT, APPENDED AND PUSHED BEFORE ARM ① WAS READ

One reading declared in the already-read section was wrong, by this seat's own hand and not by the
instrument's: ⓑ compared today's `r_s` against a number this seat had typed into its own target table
rather than read from the namesake. The real stored value differs from the typed one in the sixth
significant figure. Corrected above, with the discarded reading kept beside it; arm ②, which existed
only to explain the error, is withdrawn before it was read and is not scored.

**What replaces it is a cheaper guard than the arm was.** `l_A = pi D_M / r_s` holds by construction in
every stored triple, so each namesake file checks its own three scales against each other with no
instrument and no configuration. All 36 pass it to better than `1e-11`. The invented number failed it
by 1.4e-04. ⇒ **The census runs that test first, on every file, before any configuration is claimed.**
