# r7220 — PRE-REGISTRATION, filed before any of this revision's computation is run

**Order answered:** `r7205`/`r7203` — `r7220` is the work: fix this seat's own `r7170` receipt, which has
**no failing gate** and a runtime that explodes about one run in six.

**What is already measured** (at `r7218`, on the PR and in the channel): thirteen timed serial runs on an
idle box gave `12`–`16` s typically — matching its registered `13` s — with roughly one run in six over
`240` s, and that variance survives BOTH a fixed `PYTHONHASHSEED` AND an idle machine. Two earlier
diagnoses were published and withdrawn: "hash-seed dependent" and "contention timeout". **Neither is
revived here.**

---

## 1. What this revision must establish, in order

1. **WHERE the tail lives.** The receipt makes eight heavy symbolic calls. The tail is either localised
   in one of them or spread across all. This is measured by running under a traceback dump on a short
   timer, repeatedly, until a blown run is caught — **not inferred from which call looks expensive.**
2. **Whether a determinate normalisation suffices for what the gates actually need**, which is only:
   an emptiness test on `free_symbols ∩ {θ, φ}`, zero-tests on differences of radial operators, and the
   `ℓ(ℓ+1)` difference read between two degrees.
3. **That the cheaper form still FAILS on a perturbed operator.** ⛔ This is the control that decides
   whether the repair is a repair or a gate that cannot fail.

## 2. The branches, with the likelier named out loud

| # | branch | what it would mean |
|---|---|---|
| ⓐ | the tail is localised in one call and a determinate replacement removes it, with the perturbation control still failing | the fix lands as specified: ⓶ with ⓵ folded in |
| ⓑ | the tail is spread across every heavy call | a one-call replacement will not do it and the whole reduction needs restating, which is a larger revision than this one — say so and scope it |
| ⓒ | the determinate form cannot prove a zero that is true | it is NOT sufficient; the repair would weaken a gate, so the honest route is to keep the exact test and ask the gate for a cap or a scope declaration, which `r7203` has already offered |
| ⓓ | the tail is not in `sympy` at all | both withdrawn diagnoses and this one are wrong together, and the measurement goes back to the start |

**⇒ The likelier branch, named before the run: ⓐ.** The reason, so it is falsifiable: the receipt's own
structure puts one `simplify` on a spherical-harmonic expansion inside a nested
`simplify(expand(simplify(...)))`, and an expression that has been through `expand` is where `simplify`'s
heuristics have the most room to wander.

## 3. What is NOT in scope

- ⛔ No gate's assertion is weakened to make a runtime problem go away. If the cheaper form cannot carry
  a test, the test stays and the problem is reported, per branch ⓒ.
- ⛔ The caching half (⓵) is folded in because it is free and changes nothing, **but it is not claimed as
  the fix**: it removes about a quarter of the work and the tail is an order of magnitude.
- ⛔ `.github/workflows/gates.yml` is not touched. A cap or a runner split is the gate's, as `r7203` says.

## 4. The pass condition, stated as a number before it is measured

**The repaired receipt must run at or under its registered budget on THIRTY consecutive runs**, with no
run exceeding three times that budget — against a pre-repair rate of roughly one in six over `240` s.
Thirty runs at the observed rate would see about five blow-ups, so a clean thirty is a real result and
not a lucky draw. **And the perturbation control must still fail**, on every perturbation tried.

## 5. What would make this revision report a failure

- the tail is not localised ⇒ branch ⓑ, scoped and not attempted here;
- the determinate form proves a false zero or fails a true one ⇒ branch ⓒ, reported with the request the
  gate already offered to take;
- thirty clean runs are not achieved ⇒ the fix is insufficient and is reported as such rather than landed
  on a smaller sample.
