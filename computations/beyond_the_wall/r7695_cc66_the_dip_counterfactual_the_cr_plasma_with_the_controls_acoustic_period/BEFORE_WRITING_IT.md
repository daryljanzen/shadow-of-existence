# `r7695` (cc66) — **TWO FINDINGS BEFORE A LINE OF THE SWITCH IS WRITTEN**

*Arm ⑤ of the registration says the price is checked against the instrument's own code and the existing
banks before the rebuild is launched, because at `r7693` I quoted a cost for a computation that was
already banked. Doing that turned up two things that change the job rather than its price.*

## ⛔ ① **"RESAMPLE `S(k, η)` BEFORE `_project`" IS NOT BATCH-SAFE, AND THE INSTRUMENT SAYS SO ITSELF**

`_project` is called **once per k-batch** (`KBATCH`, default `250`): `hier_run` loops `Cl += _project(kb,
EE, Y, ls, x0, e_sw)` over disjoint slices. ⇒ **A resample in `k` needs neighbours, and a batch's first
and last modes have none from the adjacent batch.** The shift is about one per cent of `k`, so at every
batch edge the interpolation would reach for a mode that is not in the array it was handed.

⌗ **And this is not a guess about the code — the file already states the governing fact for its own
reason:** *"`_project` takes its measure as `dk = np.gradient(kb)` from the BATCH it is handed, not from
the global grid … on CR's PHYSICAL ladder the spacing varies, the one-sided end differences do not equal
the centred ones, and the batch boundaries move the weights slightly."* ⇒ *The same property that makes
`KBATCH` only weakly matter for `dk` makes an in-batch resample wrong at the seams.*

### ⇒ THE EXACT FORM, WHICH NEEDS NO INTERPOLATION AT ALL

**Solve the plasma at `k·ρ` and project at `k`**, where `ρ` is the two arms' sound-horizon ratio. Then
`S_new(k) = S_old(k·ρ)` **exactly**, which is what the resample approximates. ⌗ *Each mode stays
independent, so it is batch-safe by construction and `KSLICE` keeps segmenting exactly; and there is no
interpolation error to carry into a `q ≈ 1.9` band comparison whose whole content is a `+0.019`
difference.* ⇒ **Same object, exactly rather than approximately, and fewer lines than the 30–40 priced.**

⚠ **This is 70's design and the change is mine, so it is routed and not taken.** *The physics is
unchanged — "the CR plasma with the control's acoustic period" — but the construction is theirs to
confirm.*

## ⛔⛭ ② **THE STRETCH IS `0.82` PER CENT ON THE BANKS I CAN READ, NOT THE `0.54` THE ORDER STATES**

```
r_s(lcdm) = 145.38203856796778      r6911_source_lcdm_leafrec1.npz
r_s(cr)   = 146.57252519660550      r6911_source_cr_leafrec1.npz
ratio     = 1.0081886775035223   ⇒  +0.8188677503522257 per cent
```

The comb's period in the retention statistic's own variable is `q = k r_s/π`, so **matching the period
IS matching `r_s`**, and the stretch the resample carries is that ratio. ⇒ **On the two `r6911` source
banks — the ones the retention statistic and the dip test are both computed from — it is `0.82` per
cent.**

⚠ **I am NOT asserting the order is wrong.** *`0.54` per cent is very likely `r_s` at a different point
— the refit licensed point, or the distances point — or a different quantity. **But the stretch that
matters is the one carried by the resample I am about to apply, and that is the ratio between the banks
the comparison is read on.*** ⇒ **Which pair is `0.54` measured on?** *Registered as a question rather
than resolved by picking the number that suits the file I happen to be editing.*

⌗ *** AND THIS IS ARM ① OF THE REGISTRATION DOING ITS JOB. *** *`r7693` was held because I took the
order's word for what a bank WAS and verified only that my read of it matched. The registration for this
revision says: establish what a number is OF before building on it. **The first number I needed, I
checked, and it does not match.** That is the whole value of the arm, and it cost one bank read.*

## WHAT THIS CHANGES ABOUT THE PRICE

The switch is **smaller** than priced (no interpolation, no restructuring of the batch loop) and the
rebuild is unchanged at about `1–1.5 h` wall. ⌗ *Reported per arm ⑤ because the price moved, even though
it moved downward.*
