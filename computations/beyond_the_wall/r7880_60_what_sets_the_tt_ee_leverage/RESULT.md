# r7880+60 — what sets the TT:EE leverage: **nothing outside the neutrinos does, and (b) is closed**

**Order:** `r7879` (69) item ①, branch **(b)**, *"first, bounded to one revision, as you
recommend"*: ask what in the instrument sets the TT:EE response ratio, **on banks that already
exist**; name a sector outside the neutrinos that carries the TT-heavy signature, or say nothing
does and close `(b)`.

**Registered in `PREDICTION.md`, committed and pushed as `293a71ade` before any measurement of this
revision ran**, with four reads declared, the candidate set closed, the band fixed at `r7878`'s own
`4/3` and four mutually exclusive outcomes. The fit is `r7874`'s own `shift.py`, executed with the
two lines `r7876` rebinds and **the rebinding function imported** from `r7876`'s `refit.py` — no
second copy of either anywhere. **The reproduction leg reproduced**: `1.15162`, `1.29592`,
`1.01405`, `1.04630`.

⇒ **The required leverage was re-measured by this run rather than carried over**, and it agrees with
`r7878`'s to the last digit: TT is `0.15162` from one against EE's `0.01405` at `0.30` eV, so
**`10.790`**; and `0.29592` against `0.04630` at `0.60`, so **`6.392`**.

---

## THE TABLE

| candidate | provenance | sum | `ΔA_TT` | `ΔA_EE` | leverage | of required | in band |
|---|---|---|---|---|---|---|---|
| ⓵ `DNEFF = 0.0293` | recorded in both configs | 0.30 | −0.004286 | −0.008613 | 0.498 | **0.046** | no |
| | | 0.60 | −0.004733 | −0.008926 | 0.530 | **0.083** | no |
| ⓶ `DNEFF = 0.044` | recorded in both configs | 0.30 | −0.005334 | −0.012633 | 0.422 | **0.039** | no |
| | | 0.60 | −0.006997 | −0.013372 | 0.523 | **0.082** | no |
| ⓷ `NUFD` off | recorded in both configs | 0.30 | −0.492348 | +0.001790 | 275.037 | **25.490** | no |
| | | 0.60 | −0.345364 | +0.033818 | 10.212 | **1.598** | no |
| ⓸ `BVEL` off | ⚠ directory name only | 0.30 | +0.000017 | +0.000000 | **UNREADABLE** | no move > `1e-05` | no |
| | | 0.60 | −0.000002 | −0.000001 | **UNREADABLE** | no move > `1e-05` | no |

⇒ **`Ⓒ` — nothing outside the neutrinos carries it, and `(b)` is CLOSED.** Exactly one registered
row fires (`Ⓐ=no, Ⓑ=no, Ⓒ=FIRES, Ⓓ=no`), and the receipt checks that exactly one does.

---

## WHAT THE TABLE SAYS BESIDES THE NULL

**⓵⓶ The radiation-density correction is EE-HEAVY, which is the wrong sign of asymmetry.** `DNEFF`
spends about twice as much of its move on EE as on TT — leverage `0.42`–`0.53` against a required
`10.8` and `6.4`, so **`4` to `8` per cent** of what is wanted. It is not a weak version of the
right thing; it pulls the other way. **And that is a property of the sector and not of the step**:
the two banked step sizes agree on the leverage to `1.179` and `1.013`, inside the same `4/3` band,
which is the control `PREDICTION.md` registered for exactly this.

**⓷ The ONLY candidate in the banks with a TT-heavy signature at all is the neutrino background
itself** — and that is not a sector outside the neutrinos, so it cannot answer `(b)` whatever its
number. `NUFD` moves TT by `0.49` and `0.35` while moving EE by `0.0018` and `0.034`: leverage
`275` at `0.30` eV and `10.2` at `0.60`. ⌗ *The second of those is the near thing and is reported as
near: `1.598` of required against a band edge of `1.333`. The first is `25` times required, so the
pair is not in band at both sums under any reading, and the leverage is nowhere near constant in the
sum.*

⇒ **So the diagnostic does not only fail to find a non-neutrino carrier; it finds that the TT-heavy
asymmetry in the banks is a neutrino-sector property.** That is a positive result and it points the
same way `r7879`'s ruling does.

**⓸ `BVEL`'s sum response is unmoved at the fit's own precision** — parts in a million in `A`,
against the `0.15` and `0.30` that would have to be removed.

### ⇒ AND THAT CONFIRMS THE ARGUMENT REGISTERED AS `Ⓐ⓵`, ON THE EVIDENCE OF ALL THREE

`PREDICTION.md` registered, as an argument to be checked rather than asserted: *the sum response is
a ratio to the same configuration's own zero leg, so a change whose effect is independent of the sum
divides out exactly and cannot move the sum response at all, whatever it does to the spectrum.* The
three readable candidates line up with it by **size**, not by assumption:

| sector | how sum-dependent it is | its move in `A` |
|---|---|---|
| `BVEL` — a baryon-velocity term, the same at every sum | essentially none | `1e-05` and below |
| `DNEFF` — a radiation density the sum interacts with | some | `4e-03` to `1.3e-02` |
| `NUFD` — the sum's own background | wholly | `0.35` to `0.49` |

*A sector's grip on the sum response is its sum dependence, and nothing else.*

---

## ⛔ A GAP IN THIS SEAT'S OWN REGISTRATION, NAMED RATHER THAN QUIETLY FILLED

`PREDICTION.md` put *"has no readable move"* in `Ⓓ`'s row and **never said what readable means.**
`BVEL` then moved `A` by parts in a million, and a ratio of two such numbers is not a leverage — it
is a ratio of two roundings. Left alone it would have printed `113.805` at `0.30` eV, which is a
number with no content.

⇒ **The threshold is taken from the FIT and not from this measurement**, which is what keeps it from
being a criterion chosen after the result: `shift.py` reports `A` to five decimals, so `1e-05` is
the smallest move it can distinguish at all, and a leverage is readable only when **both** blocks
move more than that. ⌗ *And the verdict row is the same either way — whether the gap is filled like
this or `BVEL` is simply dropped from the set, `Ⓒ` fires and nothing else does. That is stated
because a repair that could have changed the answer would need more than a footnote.*

---

## WHAT THIS REVISION DOES NOT CLAIM

- **No limit is read**, under any outcome. `r7879` puts the limit behind item ②'s joint validation.
- **The four cosmological parameters are not answered, and that was registered in advance as a
  limit of the banks, not a finding about them.** Every parameter-offset leg in the banks is at
  `MNU = 0`, so the banks cannot show a parameter's sum dependence, and by the argument above it is
  exactly the sum dependence that decides whether it can move the sum response. ⌗ *What would settle
  them is one offset leg at a non-zero sum per parameter — named here, not run, because `(b)` was
  bounded to one revision and the answer it was bounded to give is `Ⓒ`.*
- **`BVEL`'s provenance rests on a directory name.** Its two banks are an older format whose configs
  record none of the switches. Declared in the registration, repeated here, and it changes nothing:
  the candidate is unreadable on its move, before provenance is reached.
- Naming a sector would not have proposed it as the repair. `r7879` ruled **(a)** the repair; `(b)`
  was a diagnostic, and it is now closed.
