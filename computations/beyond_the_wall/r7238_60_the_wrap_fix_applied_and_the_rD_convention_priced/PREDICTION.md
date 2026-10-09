---
name: r7238-prediction
kind: PREDICTION
job: both of r7225's items predicted before either is run — the wrap re-measure checked against 70's count, and the r_D convention's range on the floor, in ONE form
revision: r7238
seat: 60
order: r7225
---

# ⛭ r7238 — PRE-REGISTRATION

`r7225` carries two items and attaches the burden to the second: ***one form, and read the sensitivity
from the PHASE rather than from a peak table.*** *Both are predicted here before either is run. I have
read `70`'s `results.md` for its METHOD — the literal's spaces matched any whitespace run, survival
compared on collapsed strings, every other rule the shipped one — and its six numbers, which is what
makes item ① a CHECK rather than a measurement. I have not read or run `r1_wrap.py`.*

## ⛭⛭ ITEM ① — MY OWN IMPLEMENTATION AGAINST `70`'s SIX ROWS

**The rule I will implement, stated before writing it:** *turn each whitespace run in the literal into
`\s+`, `re.escape` the rest, search the RAW body so clause segmentation is untouched — `CLAUSE_DELIM`
carries `\n\s*\n` and collapsing the body would destroy the paragraph break — and compare survival on
whitespace-collapsed strings.* ⌗ *That is the same rule `70` describes, reached because collapsing the
body is the wrong fix for a segmenter that reads blank lines; arriving at the same rule is the point of
a second implementation.*

> ***I predict exact agreement on `S7`'s `ABSENT` = `$98$` — the number the order singles out, a fall
> of `$120$` — and agreement to within `$\pm2$` on the other five rows: `REVERSAL` `$475$`,
> `DISCRIMINATING` `$324$`, source `ABSENT` `$454$`, `CODE` `$202$`, source `REVERSAL+PARTIAL`
> `$288$`. And the headline `$25.7$` per cent against `$18.4$` with `$z=2.84$`.***

⌗ **Where a legitimate disagreement could come from, named in advance so a mismatch can be diagnosed
rather than argued:** *⓵ whether a literal's LEADING or TRAILING whitespace becomes `\s+` or `\s*`;
⓶ whether `SITE_CAP` bites more often once the pattern is broader, moving keys into `SATURATED`
instead of into a verdict; ⓷ whether a key that was `ABSENT` lands in `NO-CLAUSE` rather than in a
verdict; ⓸ whether `MARKUP` is still tested on the raw literal (it should be — it is a property of the
quotation, not of the body); ⓹ whether the survival comparison collapses the needle as well as the
haystack.*

⛔ **If my `$120$` disagrees with `70`'s, that is the result and the corrected numbers do NOT go into
the row until it is settled** — *`r7225` asked for exactly that and it is the right order.*

## ⛭⛭⛭ ITEM ② — THE `$r_D$` CONVENTION'S RANGE ON THE FLOOR, IN ONE FORM

*The floor is `$|\Delta\Phi_{\rm running}|/96.6$`, measured at `$r_D=7.12$` Mpc — the visibility-peak
convention the runs report — as `$15.46^{\circ}/96.6^{\circ}=16.0$` per cent. `cc66` measured the
endpoint swing as `$+2.21$` against `$-0.89$` per cent, so the two conventions differ by `$3.10$` per
cent in `$r_D$`.*

**The sensitivity, taken from `r7236`'s PHASE table and not from any peak table:** *`$-15.4791^{\circ}$`
at `$r_D=7.10$` and `$-15.4648^{\circ}$` at `$7.12$`, so
`$\mathrm{d}\Phi/\mathrm{d}r_D=+0.715^{\circ}$` per Mpc.* ⇒ `$3.10\%\times7.12 = 0.221$` Mpc, times
`$0.715$`, is `$0.158^{\circ}$`, which is `$0.16$` percentage points of `$96.6$`.

> ***I predict the floor's RANGE across the two `$r_D$` endpoint conventions is `$0.16$` PERCENTAGE
> POINTS — about `$15.9$` to `$16.1$` per cent — with a claimed band of `$0.05$` to `$0.5$`
> percentage points.***

⇒ **So I expect `a sixth` to be SAFE: the convention does not put the floor between a seventh
(`$14.3$` per cent) and a fifth (`$20$`), it moves it by a sixth of one percentage point.** *The
paper's sentence would then want its convention named for completeness rather than for correctness,
which is a different recommendation from the one `r7225` anticipates.*

## ⛔ WHAT WOULD REFUTE ME ON ITEM ②, NAMED IN ADVANCE

1. **The range is `$\ge1.0$` percentage point** — an order above my band. Refuted, and the paper's
   sentence needs the convention beside it as a matter of correctness.
2. **The range is `$\ge2.4$` percentage points** — enough to carry the floor outside
   `$14.3$`–`$20$`. Then `r7225`'s own worry is realised and `a sixth` cannot be said unqualified.
3. **The sensitivity has the opposite sign** — the phase magnitude RISING with `$r_D$`. That would
   contradict `r7236`'s own measured table and is the root-level failure.
4. **The swing is not `$3.10$` per cent in `$r_D$`** — I am taking `cc66`'s `$+2.21$`/`$-0.89$` at
   face value and converting it to a fractional change in the length. If that conversion is wrong the
   input is wrong rather than the arithmetic, and I will say which.
5. **The floor is not `$16.0$` per cent at the shipped convention** when recomputed here. Then
   `r7236`'s own number does not reproduce and nothing downstream of it stands.

## ⌈ AND THE THIRD OUTCOME, PRE-REGISTERED BECAUSE THE ORDER NAMES ONLY TWO

`r7225` frames it as `a sixth is safe` or `a sixth is really between a seventh and a fifth`. **There is
a third and I think it is the live one:** *the ENDPOINT convention is not the exposed choice at all.
`$r_D$` is `$\ell$`-dependent, so ANY single value is a choice, and the floor also depends on the
`$\ell$`-range `running` is defined over — `$104\le\ell\le1886$` is the paper's window and not a
property of the kernel.* ⇒ **If the endpoint moves the floor by a sixth of a point while the
`$\ell$`-window moves it by whole points, then the convention the paper needs beside the floor is the
WINDOW and not the endpoint**, and I will say that in those words rather than answering only what was
asked.
