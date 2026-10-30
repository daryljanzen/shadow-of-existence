# `r7640` (60) — LAYER 1 OF THE INSTRUMENT-DRIFT CENSUS: ALL 36 NAMESAKE CONFIGURATIONS ARE IDENTIFIED, TWELVE OF THEM CANNOT BE SPECTRUM-CENSUSED AT ALL, AND TWO OF THE BANK'S OWN RECORDS WERE WRONG

**Receipt:** `census.py` in this directory — 72 checks, 0 failures, 45 s.
**Registered:** `PREDICTION.md`, its own commit, amended at `r7640+60.1` before arm ① was read.

## THE RESULT IN ONE LINE

Every one of the 36 banked namesakes reproduces its **own recorded background** under today's
instrument to better than the order's `1e-11` — 35 of them **exactly** — so no file's old → new diff
is explained away by its point having moved. But the background is **not** the spectrum, and twelve of
the 36 cannot have the order's comparison taken at all: today's instrument **aborts** under their own
recorded `KFAC`.

## WHY THE CENSUS SPLIT, AND WHAT THAT BOUGHT

The order asks for 36 spectrum rebuilds at each namesake's own configuration. That instruction has a
prior step the bank's own `RECIPES.md` says is not everywhere payable: *"none recorded"*, **⚠ low
confidence**, on one entry; *"digits unrecorded"* on another. **A spectrum rebuilt against a guessed
command cannot separate "the instrument drifted" from "we guessed the command wrong".**

Each namesake carries `l_A`, `D_M`, `r_s` in its own file, and those three are fixed by the background
switches alone. ⇒ **A namesake is a fingerprint of its own configuration**, and the whole 36 can be
placed in **forty-five seconds** instead of days. ⚠ The census says plainly what this does **not**
settle: a Layer-1 pass is a **necessary condition** on Layer 2, never a verdict of *"the diff is the
arm's alone"*, because `KFAC`, `NK`, `LSTEP`, `KBATCH`, `HIER`/`BSPLIT`, `KCONT`, `KSLICE` and every
source switch are invisible to the three scales. PART 2 is exactly such a case.

## THE EIGHT BACKGROUNDS THE 36 CARRY, AND THE COMMAND FOR EACH

| `l_A` | `D_M` | `r_s` | n | the command that reproduces it | miss |
|---|---|---|---|---|---|
| 301.6 (solved) | 13004.555185538089 | 135.46092517934187 | 15 | built-in defaults, onset solved | 0 |
| 340 (injected) | 13004.555185538089 | 120.16180892379266 | 1 | defaults + `LATARG=340` | 1.1e-13 |
| 172.8407172847731 | 13004.555185538089 | 236.37378781977986 | 1 | defaults + `ZSTART=3e7` | 0 |
| 301.7986427684055 | 14017.038576277775 | 145.91127717599196 | 11 | `CRH0=68.581133 CROM=0.297209 WBH2=0.021524 NS=0.997952 ZSTART=3e7 LEAFSCALES=1` | 0 |
| 172.32428325429453 | 14007.372881032428 | 255.36424065206552 | 4 | `CRH0=68.62 CROM=0.2973 ZSTART=3e7`, `LEAFSCALES=0` | 0 |
| 302.8890769675279 | 14011.456663213483 | 145.32808432693113 | 2 | `CRH0=68.60 CROM=0.2973 ZSTART=3e7 LEAFSCALES=1` | 0 |
| 302.84420197962737 | 14007.372881032428 | 145.30725518761844 | 1 | `CRH0=68.62 CROM=0.2973 ZSTART=3e7 LEAFSCALES=1` | 0 |
| 302.05150958375458 | 14021.281692375205 | 145.83325744467038 | 1 | `CRH0=68.6077 CROM=0.2967 WBH2=0.0217 NS=0.9949 ZSTART=3e7 LEAFSCALES=1` | 0 |

The single non-zero miss is the `l_A` injection, whose onset is a `brentq` root rather than a number
read from the environment, so it lands at the solver's tolerance. ⚠ **That sets a floor on the
census's threshold:** `1e-11` is comfortable against 1.1e-13, but tightening it below about `1e-13`
would start reading solver tolerance as instrument drift.

## THE REGISTERED ARMS

**① HIT, and stronger than registered.** The entry marked *"the cc66 refit minimum,
~68.6077/0.2967/0.0217/0.9949, **digits unrecorded**"* is reproduced by **exactly those four quoted
figures**, to zero difference on all three scales. Arm ① registered that *a point exists* within 0.01
of each figure; the point is the figures themselves, so **nothing beyond the quoted digits was ever
needed** and "digits unrecorded" is retired.

**② WITHDRAWN at `r7640+60.1`, before it was read.** Its subject was this seat's own transcription
error — see the correction below. Not scored.

**③ HIT, 12 of 12.** `c54.175`, `c54.177`, `c54.178`, `c54.186_KCONT`, `c54.186_L3000`,
`c54.191_lA340`, `c54.191_phipi`, `c54.193_nodrive`, `c54.195_phi0.7854`, `c54.195_phi1.5708`,
`item38_phi0.0`, `item38_phi3.1416` — under their own recorded `KFAC=1`, today's instrument **exits 1**
at `alias_gate`'s truncation half (added `r3870`, fail-closed, caller `if not alias_gate(kk): return 1`),
ratio 1.00 against the gate's 1.9, which `KMAXL = KFAC * LMAXL` makes 1.0 **by construction**.
⇒ **For these twelve the order's Layer-2 comparison has no reading to take.** The honest census entry
is the refusal, named to its gate and its revision — **not** a rebuild at `KFAC=2` reported as though
it were the namesake's configuration. And the refusal is itself the instrument drift the census is
looking for: `c54.175` and `c54.177` predate `c54.178`, and the gate's own docstring records that it
*"existed only on the delta-function path until `c54.178`, and the line-of-sight path — the default
since `c54.173` — had none"*, so for those two the change is not a moved threshold but a guard where
their build had **no guard at all**.
⌗ The refusal costs **one second**: the k grid and the gate sit above the mode integration in the same
block, so nothing is spent discovering it.

**④ Registered and not claimed by this seat.** See the coordination below.

## WHAT THE FILES SETTLE AGAINST THE BANK'S OWN PROSE

- **`LEAFSCALES`: the bank's two records disagree, and the namesakes decide `1`.** `RECIPES.md`'s table
  puts the `cc66` `h686`/`h6862` family at `ZSTART=3e7 LEAFSCALES=1`; `MANIFEST_old.json`'s `held` says
  the namesakes of all four of `h686_pol`, `h6862_pol`, `h686_L2000` and `refit_verify` sat at
  `LEAFSCALES=0`. All four reproduce at `1` to zero, and at `0` the same point misses `r_s` by
  **110.4 Mpc** — which is also the negative control showing the three scales discriminate the switch,
  so the match is not vacuous.
- **The `pol` pair is two runs and the bank rebuilt it as one.** `RECIPES.md` rebuilt `h686_pol` and
  `h6862_pol` from one run because *"they differed only in `CRH0`"*. That is right about the **rebuild**
  — on the arm of record both points collapse — and the two rebuilt files are bit-identical. But the two
  **namesakes** differ by **1.19e-03** relative on `Dl` at different `D_M`. ⇒ **Layer 2 owes two runs
  here**, at 68.60 and at 68.62; one rebuild cannot be compared with both namesakes.
- **`cc66_cr_x_lstep1`'s unrecorded command is recovered.** Its namesake's `l_A = 172.8407172847731` at
  the **default** `D_M` says the point was the built-in default and the onset was **not** solved: the
  defaults with `ZSTART=3e7` reproduce all three to zero. The ⚠ low confidence is retired at the
  background layer.
- **`LEAFREC` is invisible to the background**, measured, not assumed: at the refit point `LEAFREC=0`
  and `LEAFREC=1` give bit-identical scales. So the three scales identify the point and the rulers and
  say **nothing** about the switch whose default moved — which is why that one has to be read off the
  source.
- **And the default did move.** Today's instrument has `os.environ.get('LEAFREC', '1')`, and its own
  note beside `r7097`'s `config` ratchet names it: *"`LEAFREC` defaulting ON at `cc66.75` is the case in
  point"*, written because `__SWITCHES__` records only what the environment **set** and so cannot
  survive a default moving. ⇒ **Any namesake banked before `cc66.75` whose command omits `LEAFREC` is a
  command that, run verbatim today, rebuilds the leafrec1 arm and not the namesake** — the general form
  of what cc66 found on `r6885_dp0`. None of the 36 namesakes carries the `config` key that would have
  recorded it; all 36 lack it, and today's writer emits one.

## ⛔ THE CORRECTION AGAINST THIS LINE, AND WHAT IT PAID FOR

The first pass declared a MISS: that `c54.191_cr_lA340_L3000`'s background was off by **4.939e-05**.
It is not. **The namesake's `r_s` is `120.16180892379266`; the `120.16185830983276` it was compared
against was typed by this seat into its own target table and belongs to nothing.** Corrected and pushed
as `r7640+60.1` before arm ① was read, with the discarded reading kept beside it; arm ②, which existed
only to explain the error, was withdrawn before it was read.

**What caught it is now the census's first part, and it is free.** `l_A = pi D_M / r_s` holds by
construction in every stored triple (`L_A` is computed at the end of the background, and `r6893+cc66.37`
measured that no transfer function reads it), so **each namesake file checks its own three scales
against each other with no instrument and no configuration at all**. All 36 pass to zero. The invented
number fails by **1.4e-04**. ⇒ The guard that was missing would have refused the error before a single
run was spent on it, and it now runs first, on every file, before any configuration is claimed.

⌗ The withdrawn arm leaves one fact about the corpus's own guards behind it: `LATARG`'s default **is**
301.6 (`_latarg = float(os.environ.get('LATARG', '301.6'))`), so *"set explicitly"* and *"defaulted"*
are **one code path**, and the disjunction arm ② registered over those two was not a disjunction over
states the instrument can produce. **A defence against a state changing has to enumerate states the
thing can actually be in** — and that one was refutable from the source without running anything.

## COORDINATION OF RUN ORDER WITH 70

The order asks the two seats to coordinate through the repo so one machine is not loaded twice.
**This seat took Layer 1 and the arms inside it; the 36 spectrum rebuilds are 70's.** Layer 1 is eight
background solves of two seconds each — it loads no machine and cannot collide. What this receipt hands
70 is the table above: **an identified command per namesake**, so that 70's rebuilds compare against the
instrument rather than against a guess, plus three things that change what Layer 2 should run — the two
`pol` configurations instead of one, the twelve that will abort, and the `LEAFSCALES` correction.

## WHAT IS NOT CLAIMED

- Not that a Layer-1 pass means the diff is the arm's alone. Layer 2 gives that, and it is not read here.
- Not that the eight backgrounds exhaust the configuration. They are blind to the solver and the source,
  and arm ③ is precisely a case where the background reproduces and the spectrum cannot be taken.
- Nothing in `P15` or any other paper moves on this revision, and no receipt belonging to another seat
  is edited.
