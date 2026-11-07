# `r7697` (cc66) — FAILABILITY, and **the sweep caught a false negative in itself**

| leg | perturbation | total FAIL | target failed |
|---|---|---|---|
| **A** | arm A `(L)`'s depths scaled `1.01` | 20 | ✔ |
| **B1** | `STACKPERT` forged to `1` — the retired pairing | 2 | ✔ |
| **B2** | `SPLITCLOCK`'s distances row forged away from `'L'` | 2 | ✔ |
| **C** | the DECOUPLED `(L)` row scaled `1.04` | 2 | ✔ |

## ⛔⛔ LEG B's FIRST FORM TESTED NOTHING, AND IT WAS AIMED AT THE MOST IMPORTANT GATE IN THE REVISION

The first leg B anchored its forgery on `_LE = list(np.asarray(_LAZ['ells'], int))` — **which is
DOWNSTREAM of the pairing check.** The forgery was applied after the gate had already read the config,
so the gate passed and the leg reported `0`.

⇒ *** Had I read the TOTALS rather than the per-leg targets, I would have recorded the pairing gate — the
one assertion that embodies why `r7693` failed — as VERIFIED when it was UNTESTED. *** ⌗ *"The patch
applied" was true: the line was inserted, the count was `1`, the assert passed. **A patch can apply
perfectly and still be in the wrong place**, which is `r7687`'s mis-aimed-probe defect wearing a new
costume.*

## ⛭ SO THE RE-AIMED LEG ASSERTS ITS OWN AIM

```
pl=$(grep -n '# PERTURB' "$R" | cut -d: -f1)
gl=$(grep -n 'THE BANK SAYS OF ITS OWN RUN' "$R" | cut -d: -f1)
[ "$pl" -lt "$gl" ] || { echo "VOID: perturbation at $pl is AFTER the gate at $gl"; return; }
```

**Measured: perturbation at line `870`, gate at line `871` — upstream, so the leg is live.** ⌗ *A
failability leg now carries three assertions about itself: that it applied, **where** it applied
relative to its target, and that its NAMED target is among the failures. Each of the three was added
after the absence of it cost a wrong verdict.*

## WHAT THE PAIRING GATE IS NOW KNOWN TO CATCH

Both directions: **the retired pairing switched ON** (`STACKPERT = 1`) and **the split-clock setting
switched OFF** (`SPLITCLOCK[...] = None`). ⇒ *So a future bank that is not `(L)` cannot be read as
though it were — which is the failure that cost `r7693` its entire landing, and the only one of this
revision's gates whose absence no other check could have covered.*
