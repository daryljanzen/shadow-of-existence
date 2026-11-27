# `r7884` (60) — THE ITEM SPLITS AS REGISTERED, AND THE REVISION'S OWN RESULT IS A DEBT PAID

**Order `r7879` item ⓷** — the control's limits on the jointly validated sector, read on the closed
envelope. **The limit is NOT read in this revision.** `PREDICTION.md` registered the split before
any leg ran, and the condition it registered has occurred.

---

## WHAT THIS REVISION ESTABLISHES

### ⓵ THE CMB GRID IS COMPLETE — 10 of 10 points, `rc=0` on every leg

`bank/pol_grid_bvel1_nuhier`: five sums per arm (`0.06`, `0.15`, `0.30`, `0.45`, `0.60` eV) on both
arms, each point a spectrum file and its TT companion, every leg carrying `NUHIER=1 NQ=12 LMAXNU=12
QMAXNU=20` in its own recorded `config`. ⌗ *The eight parameter-offset directions per arm are
**carried** from the landed no-offset rung rather than re-run, because every one of them sits at a
ZERO sum where the hierarchy is provably inert — reads ③ and ④ of the registration, and the
receipt asserts the zero-sum property off those legs' own configs rather than assuming it.*

### ⓶ `r7882`'s STRIP-CLASS DEBT IS MEASURED AND ROUTED — 8 of 8

⛔ **`r7882` broke three receipts that are not this seat's**, and that is named here rather than
left to the plain suite to report. Two compare the instrument's **reduced-tree source hash** against
the bank's stored `config`; the third is the switch **census**, which asserted `95` and now measures
`99 switches used, 99 bound`. All three were introduced by `00d6dd181` (`r7863+cc66.1`) and carry
`cc66`/`70` markers, so the patch is **routed in `FOR_66_FROM_60.md` and not one of them is edited.**

⌗ **THE PART OF THIS WORTH KEEPING IS THE ERROR.** The first patch extended the eighth strip class
with the **four new switch bindings and nothing else**, because four is what the census counts, and
it **failed the fixed point**. A census is a count; the blob comparison is an *equality*. `r7882`
added a module-level block, four functions, nine guarded statements, two offsets, two aliases and a
narrowed handover slice **as well as** the four bindings.

⇒ *This is the standing guard about labels, walked straight into: "the four switches" labelled a
diff of nine mechanisms, and the label is many-to-one.* The residual diff was then **printed**,
because a gate that compares a hash tells you the trees differ and nothing whatever about where.

The patch is nine parts — `Ⓔ` the four bindings on their exact values, `Ⓚ` the four recorded-`config`
keys, `Ⓕ` four `_nuhier_*` functions dropped whole, `Ⓘ` `if NUHIER:` dropped **both branches**, `Ⓧ`
the `IfExp` reduction, `Ⓞ` `± _NH` dropped from two offsets, `Ⓝ` three names dropped by name, `Ⓐ`
two aliases renamed back with the self-assignment they leave, `Ⓢ` the full-width slice that is the
whole array — and `tighten_nuhier.py` **imports** `r7878`'s `tighten.py` and **subclasses** its
`_Strip` rather than retyping it.

| gate | measured |
|---|---|
| `⓪` the four bindings are the instrument's own lines, read at source | 4 of 4 verbatim |
| `①` THE FIXED POINT | 2986 lines reduce to the banked blob's 2261, **exactly** |
| `①′` EACH HALF IS NECESSARY, FIRST HALF — `Ⓔ`+`Ⓚ` in the unextended machinery | does **not** reduce ⇒ `Ⓕ`–`Ⓢ` are load-bearing |
| `②` EACH HALF IS NECESSARY, SECOND HALF — `Ⓕ`–`Ⓢ` with `Ⓔ` omitted | does **not** reduce ⇒ `Ⓔ` is load-bearing |
| `③` THE HOLE, BOTH WAYS | 4 of 4: a moved DEFAULT passes by-name and is RED on exact value |

⛔ **`①′` and `②` were the wrong way round in this file once**, and the correction is recorded rather
than quietly made: they are not the same measurement and neither implies the other. `①′` drops eight
parts and keeps the bindings; `②` keeps the eight and drops the bindings.

⌗ **The census gate's invariant does not move, and it was checked rather than assumed.**
`len(_ROWENVS - SWEPT_SIXTY_PLUS) == 60` is the clause doing the work in that gate, and the patch
adds the same four names to **both** the asserted total and the swept set, so the difference is
preserved *identically* — independent of the row count, not by arithmetic luck.

### ⓷ THE LENSING GRID DOES NOT FIT, AND THE COST IS THE MEASUREMENT

| attempt | form | outcome |
|---|---|---|
| 1 | tracked background task | died mid-leg |
| 2 | `setsid nohup … & disown` | died within minutes |
| 3 | `setsid nohup … & disown` | ran past an hour on each of four legs, then died with **no leg banked** |
| 4 | `setsid nohup … & disown` | ran `48` min of CPU on each of four legs, then died with **no leg banked** |

⛔ **THE CAUSE IS ESTABLISHED, AND IT WAS NEITHER THE TWO-HOUR TRACKED-TASK CAP NOR THE LAUNCH
FORM.** The container is replaced about every ninety minutes and every process in it dies: this
container booted at `08:40:48` and the legs were found gone at `08:40`, and an earlier reading
places a boot at about `07:07`, which accounts for the previous death. ⇒ *A tracked task, a detached
session and a disowned process die identically, so three of these launches were spent on a
distinction that does not exist.* The filesystem, by contrast, **survives** — checked, not assumed.

⌗ **And the per-point cost was mismeasured.** Timed solo, the growth stage is `12.5` s and the
instrument solve extrapolates to about `33` minutes of CPU at the full mode count — a model
registered on two mode counts and then tested on a third to `1.7` per cent. So a point fits inside a
container lifetime easily. What did not fit was **four legs at once on four cores**: each accrued
more charged CPU than the whole solo solve should need while never finishing, which is contention,
not size. ⇒ **The remedy is one leg at a time and no code change**, since the generator already
banks each point and skips what is banked. *That is running as this is written and is a prediction
under test, not a result.*

⛔ **A leg is not checkpointed, so a death at any point loses the whole leg.** A lensing point
exceeds `1h58m` of CPU — and that is a *floor*, not a duration, so the upper bound is still not
measured. Ten points four at a time is three batches, which is of the order of six hours or more.

⇒ **So the registered condition has occurred: the ten points do not fit in one revision.** The CMB
grid and this cost land now; the limit read follows on the completed grids.

⛔ *Not at a lowered resolution — a grid the banked grids cannot be compared against answers a
different question — and **not** by dropping the lensing grid from the read itself, because the
model reads its bandpowers and a limit without them would not be the control's limit.*
`limits_nuhier.py` lands **as registered and unrun**: its plumbing gates (`Ⓛ⓵`–`Ⓛ⓹`) stand ahead
of any number, with ONE refusal that fires if any of them failed, and both `closed_envelope` reads
— CMB and lensing — are in it.

⛭ **A FIFTH GATE WAS ADDED IN THIS REVISION, AND THE REASON IS WORTH THE LINE.** `Ⓛ⓵` and `Ⓛ⓶`
read the CMB points' own recorded `config`. The lensing side had **no gate at all** — and not
because it passed: `phiphi_point.py` did not record the four hierarchy switches, so there was
nothing to read and the check was *impossible*. ⛔ *The lensing bandpowers enter the same limit, so
an unverifiable half is an unverified limit.* The recorder is completed here (additively — every
reader of a banked switch record parses it by name) and `Ⓛ⓹` reads it. The one point already banked
without the record was **deleted and is being re-run**, so that no point in the grid is one whose
provenance only its log can attest.

---

## ⛔ WHAT IS NOT CLAIMED

- **NO LIMIT IS READ IN THIS REVISION**, and the registered fork `Ⓝ⓵′`/`Ⓝ⓶′`/`Ⓝ⓷′` is **not
  decided**. Nothing here bears on where the minimum sits on the closed envelope.
- **The three receipts are not run with the patch applied**, because applying it means editing them.
  What is measured is the machinery: the reduction is a fixed point again, each half of the patch is
  load-bearing, and the controls are red. That is the same evidence `r7878` routed.
- **The cost figure is a floor.** `1h58m` is where a leg was interrupted, not where it would end.
- **The one-fitter dependency is unchanged.** `r7882` is one fitter; `r7879` required both. If
  `cc66`'s second fit disagrees beyond its own reproduction tolerance, that disagreement is the
  finding and no limit is read through either — which is a further reason the limit read waits.
