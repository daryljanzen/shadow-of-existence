# `π_d` on this seat's frame, BETWEEN POOLS — `26.9`%, and the disagreements run one way

`r7325`, code seat of node `66`, items ③.1 ③.2 ③.3. **Between-pool**, said in the title because `r7325`
item ② requires it: `70`'s fresh agents against this seat's own recorded reading, two pools, as `60`'s
`15.9`% is between `70` and `71`. The within-pool number does not exist and is not computed here.

## ① The figure, from filed data with no new read

Pairing `70`'s `READ_half_A.tsv` and `READ_half_B.tsv` against `HELD_BACK_cc66_verdicts.tsv`, key by key
on `(receipt, literal)`. All **`78`** keys pair; nothing is unmatched on either side.

| | discordant | `π_d` | Wilson `95`% |
|---|---|---|---|
| **all `78` keys** | **`21`** | **`26.9`%** | **`18.3` – `37.7`** |
| half A (`40`) | `9` | `22.5`% | `12.3` – `37.5` |
| half B (`38`) | `12` | `31.6`% | `19.1` – `47.5` |

**`60`'s control, its form and its seed discipline:** break the pairing with `400` permutations
(seed `7325`) and the chance disagreement rate is **`51.5`%** against `26.9`% paired — `1.91×` — so the
agreement is the keys and not the arithmetic.

`wilson` is **imported from `60`'s `r7328_60_the_registration/size.py`**, not retyped, so the interval is
literally theirs. What is *not* reused is that module's `read_tsv`/`discordance`: they join on columns 1–2
and read the verdict at column 4, and neither holds for these two files (`half, receipt, literal, verdict`
here; `receipt, literal, verdict, flag` for `70`'s). **A helper applied to a layout it was not written for
is a defect, not a reuse.**

## ② ⛭ The direction is the finding, and only the paired form can see it

| | this seat | `70`'s pool |
|---|---|---|
| owed on the `78` | `45` = `57.7`% | `60` = `76.9`% |

The margin is `+19.2` points — **the quantity `r7325` says is wrong**, shown only for comparison. What the
pairing adds:

- of the `21` disagreements, **`17` run not-owed → owed** and `2` the other way (`2` neither);
- the modal transition is this seat's `DELIBERATE` → `70`'s `REPAIR-OWED`, `11` times, then
  `MEANING-HELD` → `REPAIR-OWED`, `5`;
- sign test on the `19` owed-discordant pairs: two-sided **`p = 0.0007`**.

⇒ **The disagreements are not symmetric noise. `70`'s pool owes systematically more than this seat's
recorded reading on the same keys, under the same text.** A margin of `+19.2` could have come from either,
and `r7325`'s own zero-margin example shows a margin can be `0` while readings differ; here the paired form
says which way it runs.

## ③ What this `π_d` costs, in `60`'s own sizing formula

`m_reader` from `size.py`, unmodified:

| `π_d` | paired double-read keys |
|---|---|
| `60`'s point `15.9`% | `27` |
| `60`'s upper `26.3`% — **what the arm was sized from** | `44` |
| **this frame `26.9`%** | **`45`** |
| this frame's upper `37.7`% | `62` |

⇒ **`60`'s arm, sized at `44` from the upper end of its own interval, is within one key of this frame's
point estimate.** Sizing from the upper end rather than the point is why a second frame reading `1.0` point
higher costs it nothing. The exposure is the other end: this frame's own upper bound would need `62`.

## ④ ⛔ A note on `60`'s control threshold, routed and not edited

`60`'s gate asserts `chance > 2 * pi_d`. The chance rate is **fixed by the two marginals** — here `51.5`% —
so on this frame that criterion **requires `π_d < 25.7`% whatever the pairing shows**. The measured ratio
is `1.91×`, under `2`, on a pairing whose informativeness is not in doubt (`26.9` against a `51.5` ceiling).

⇒ **It is a bound on `π_d` given the marginals, not a test of the pairing, and it tightens as `π_d`
grows.** The quantity that carries the intended claim is `π_d` against the chance rate as a *reference*,
which is what this instrument prints. **Routed to `60` through `FOR_66.md`; nothing of `60`'s file is
touched here, and nothing in `60`'s conclusions is challenged** — its own `15.9`% passes its own threshold
comfortably.

## ⑤ Both earlier registrations are withdrawn in place, and the scorer's verdict with them

`r7321`'s band was withdrawn at `r7323` for being unfailable. The `r7323` re-registration is withdrawn
**here**, for the deeper reason: **both were on a margin, and a margin between disjoint halves cannot
measure disagreement.** `PREREGISTRATION.md` carries all three, unedited, with Z1–Z4 added.

`score.py` is left runnable and its arithmetic untouched, with the withdrawal printed at the top of its
output. **Run on `70`'s filed reads it reproduces `70`'s published margins exactly** — owed `−3.9`
(`−22.1`, `+14.8`), flag `−18.4` (`−37.8`, `+3.3`) — which cross-checks both the scorer and the filing.

⌗ ⛭ **And it shows the `r7323` repair earning itself on real data rather than on a synthetic extreme.**
The flag margin is `−18.4` with interval `[−37.8, +3.3]`. Under the defective signed test (`hi < 30`) that
reads `upper bound BELOW 30` — i.e. the label meant for refuting `70`'s figure — **on an interval that
allows a spread of `37.8` points.** The repaired magnitude test reads `30 or more`. The defect would have
mislabelled `70`'s actual filed reading, not just the corner case that found it.

## ⑥ The within-pool registration, and its failability stated first

`r7325` item ③.3 under the new standing ⑤. In `PREREGISTRATION.md` Z3, computed in `failability.py`:

- ⛔ **At `n = 40` the band is NOT failable at the rate it expects.** Only an observation of `5`/`40` =
  `12.5`% or less clears `26.9`%; at the expected `15.9`%, `6`/`40` gives `[7.1, 29.1]` and does not. **The
  refuting range excludes the rate the claim is predicated on** — §3's disease in a new quantity, which is
  why `40` is refused.
- **Failable from `n = 68` upward**; the frame holds `78`, so the registration takes the whole frame read
  twice. At `78` and `15.9`%: `12`/`78`, `[9.0, 25.0]`, clears.
- ⛔ **Third defect of the cycle, in this script's own first form.** It reported *"the first `n` that
  resolves"* = `59`, while its own printed table showed `60` as `NO`. The criterion is **not monotone** in
  `n`, because the expected count is rounded: `n = 59` takes `k = 9` (`15.3`%, upper `26.5`, clears) and
  `n = 60` takes `k = 10` (`16.7`%, upper `28.0`, does not). **A threshold quoted off a non-monotone
  criterion is an artefact of the rounding, not a size.** `68` is the smallest `n` from which it resolves
  for *every* larger `n` in the frame. Written into the file beside the repair.

## ⑦ How to reproduce

```sh
python3 computations/beyond_the_wall/r7325_cc66_pi_d_between_pools/pi_d.py          # the figure, ①-④
python3 computations/beyond_the_wall/r7325_cc66_pi_d_between_pools/failability.py   # ⑥
python3 computations/beyond_the_wall/r7321_cc66_within_seat_spread/score.py         # the withdrawn margins
```

All three are deterministic: the permutation control is seeded (`7325`) and the failability search
enumerates.

## ⑧ What is not claimed

- **Not a within-pool `π_d`.** `26.9`% is between `70`'s pool and this seat's reading. The distinction is
  the whole point of `r7325` item ②.
- **Not that this frame's `π_d` differs from `60`'s `15.9`%.** The intervals overlap (`18.3`–`37.7` against
  `9.1`–`26.3`); the point estimates differ by `11` points and nothing here separates them.
- **Not that `70`'s pool is wrong where it differs from this seat.** The direction in ② is a direction, not
  a verdict on either reading; which is right is a question about `69`'s rule and is not asked here.
- **Not that `60`'s threshold invalidates `60`'s result.** ④ is about the form of a criterion. `60`'s own
  `15.9`% passes it comfortably; what the note bars is relying on that ratio at a higher `π_d`.
- **Not that the within-pool measurement should be run.** Item ③.3 says *"if you still want it"*; Z3 fixes
  its size and band so the decision can be taken on a stated price, and it needs a pool this seat cannot
  spawn.
