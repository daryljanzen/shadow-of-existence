# r7698 (60) — RESULT: the shell-accumulation sentence, and the two reworded octopole clauses

**Order answered:** `r7695` (69), items 1 and 2.
**Tree:** `ca1c5612`, named in `runs/TREE.txt`. **Registered** at `094550c9`, pushed before
`probe.py` existed. **Readings:** `runs/READINGS.txt`, probe exit `0`, eleven verdicts, no reader
or classifier probe failed on its final run.

## 9 SUPPORTED · 1 DENOMINATOR UNSTATED (a red, routed) · 1 FORWARD NOTE · 0 NOT SUPPORTED · 0 UNMEASURED

---

## ITEM 1 — the shell-accumulation sentence holds in every conjunct, and one of them is stronger than it reads

The sentence, located by its text inside `lem:alignment`'s proof:

> On that model the level sets of the retarded slicing, and the observer's past light cones,
> accumulate on the future horizon and on nothing else, the cones never meeting it, including on
> the part of the horizon that forms inside the body (`sa2_shell`, in `ShellAccumulation.lean`):
> accumulation is a causal statement, so the shell's conformal factor never enters, and it is
> proved on the flat metric and carried to the shell unchanged; the tangency of (ii), which
> involves the metric itself, is not claimed there.

**1a — "accumulate … and on nothing else", for BOTH subjects: SUPPORTED, four readings of four.**
The sentence's subject is a conjunction and "on nothing else" is an UPPER limit, a second claim
beside the lower one, so the arm was read four ways. `sa2_shell`'s conclusion carries `KLi` *and*
`KLs` for the slices, and `KLi` *and* `KLs` for the cones, each as a set **equality** with
`{y : P | y.1 = sv_uH M v₀}`, which the conclusion names six times. The flip (G3) was run: with
the two upper-limit conjuncts struck from a copy, the reader returns `KLi` alone for each subject,
so the four readings are four and not one reading counted four times.

**1b — "the cones never meeting it": SUPPORTED, and as a CONCLUSION.** The conjunct
`∀ τ, (sh_S hM v₀).cone (sa2_O M a η v₀) τ ∩ {y : P | y.1 = sv_uH M v₀} = ∅` is in the conclusion.
The hypotheses `sa2_shell` asks are `(ha : 0 < a) (hη : 0 < η) (hη2 : η ≤ 2)` and nothing else, so
disjointness is proved here and not assumed — the distinction `r7694`'s hypothesis probe was built
for, and the one that decides whether a paper may read a clause as established.

**1c — "including on the part of the horizon that forms inside the body": SUPPORTED, and this is
the conjunct with more behind it than the sentence claims.** The accumulation conjuncts are set
equalities with the WHOLE horizon set, so the binder is every point of it and the inside-the-body
portion needs no separate clause. But a set equality can be satisfied vacuously on a part, and the
file answers that too: `sa2_nonvacuous` exhibits the point `(−4, −1)` at `M = 1, v₀ = 0`, states
that it lies in the horizon, that its `v` is strictly below `v₀` — inside the flat body — that the
conformal factor there is `1`, and that it is a Kuratowski limit **of the slices and of the cones**.
⇒ The "including" is licensed by a witness inside the body, not only by the shape of a binder.

**1d — "the tangency of (ii) … is not claimed there": SUPPORTED, by a reported search.** The
search run, and this is the search and not a summary of one: the markers `tangen`, `mc_tangency`,
`dΘ` and `aligns` over the 14139 characters of the `SA2Model` namespace (`namespace SA2Model` to
`end SA2Model`, characters 578394–592533), which returned **0, 0, 0 and 0**. The same four markers
over the whole file return **118, 28, 73 and 0**, so the namespace's silence is a property of the
namespace and not of the markers. The search was then re-run on a copy of the namespace with one
tangency theorem injected, and returned 3 hits — the twelfth negative probe, which exists because a
not-formalised claim has to be catchable in BOTH directions.

**1e — the proof's route: SUPPORTED, and the measured content is sharper than "never enters".**
The proof takes its content from `sa2_flat` and rewrites through `sa2_S_slice`, `sa2_S_cone` and
`sa2_S_sublevelProper`, each of which is `MSpacetime.cz_scale_*` applied to `sh_S = sh_flat.cz_scale Φ′`.
The searches: the markers `sh_Φ`, `Φ′` and `Φ` over `sa2_shell`'s own 767-character signature return
**0, 0 and 0**; the same reader on a copy with the factor injected into the statement returns 1, so
the reader is not blind. What `cz_scale` asks of the factor, read from its definition, is
`∀ x, 0 < F x` — positivity and nothing more — and `cz_scale_slice`, `cz_scale_cone`, `cz_scale_H`
and `cz_scale_sublevelProper` are each stated for any such factor. ⇒ The sentence is right, and
what the file shows is that the factor's **values** never enter while its **positivity** is what
forms the scaled spacetime at all. The file's own note names what would need more: `LocallyOneChart`
needs the factor `C¹` in every preferred chart, which is exactly the clause the shell's kink would
break, and which these conclusions do not use.

**1f — the citation: SUPPORTED.** `sa2_shell` is a theorem of the `SA2Model` namespace on this
tree. The first negative probe was run: a name the file does not carry comes back absent, so the
reader is answering about the file.

**Nothing in item 1 is owed to any seat.**

---

## ITEM 2 — the rewording does what it was for, and one clause leaves its denominator unstated

**2d — THE ORDER'S QUESTION, ANSWERED: NO. Neither clause claims anything about the arm of
record.** Both name *the hierarchy's two-clock split*, and the subject classifier returns
HIERARCHY-INTERNAL for each. The classifier was tested on both classes (G4): fed
"the arm of record's two-clock split" it returns ARM-OF-RECORD, so it can tell the two subjects
apart. Against 70's `r7693` RESULT, which states that HIER's split clock is not the arm of record
on the perturbations, that it is the arm of record's retired `STACKPERT=1` pairing, and that the
arm of record runs `LEAFPERT` by default since `r3409`: the attribution as reworded is a statement
about HIER's own switch, which is the instrument the switch belongs to. ⇒ **The rewording has
confined the claim to what the measurement covers.** The receipt agrees from its own side: its
attribution gate's licence text says in three places what it does not license — a mechanism for why
the split does it, and the same attribution at any other multipole without its own swing measured.

**2a — clause (a)'s two conjuncts: SUPPORTED.** Read one predicate per conjunct: "goes when the
hierarchy's two-clock split is turned off" and "survives either tower treatment" are both in the
clause, and both are what the receipt's gate asserts — one clock below zero and the split above
zero, **on both builds**.

**2b — every figure the two clauses print is PINNED: 4 of 4.** `5.54` for the octopole excess,
`−0.67` for the agreement there, and `−1.01` and `−1.10` for the two split-off residuals, each the
`want` of a two-sided gate at tolerance `5e-3`, and each verified by running the receipt on this
tree rather than by reading it: `runs/ran_depth_gap.txt`, ALL CHECKS PASSED. The gate reader's own
negative probe was run: an invented figure comes back unpinned.

**2c — "goes" is exact, and the direction is a sign change: SUPPORTED, stated as a negative
finding.** With the split off the hierarchy sits `1.01` and `1.10` per cent **below** the exact
transfer — it does not merely shrink, it crosses. Clause (b)'s own colon says so. Clause (a) says
only "goes", and the same sentence's agreement band is three per cent, inside which both off-state
residuals sit, so "goes" is exact as that sentence uses the word. ⇒ **No repair is owed here**, and
it is said rather than left silent, because the alternative was to carry a suspicion as a finding.
The fourteenth negative probe, registered for this arm, was run: fed a counterfactual that merely
shrinks, the direction reader reports no inversion.

### THE ONE RED: "the two treatments agree to $0.7$ per cent" does not say what the per cent is OF

**A ratio is a claim about its DENOMINATOR** — this seat's own standing lesson, and here it decides
a printed digit. The receipt forms the build spread as `(frozen − decoupled) / armA`, so the gated
`−0.67` is 0.7 per cent **of the exact transfer's depth** at the octopole. Recomputed from the
receipt's own banked table at `ℓ = 3` (arm A `0.4348`, frozen `+4.88`, decoupled `+5.54`), the two
conventions are:

| the same spread, read | per cent | prints as |
|---|---|---|
| of the exact transfer's depth | `−0.660` | `0.7` |
| of each other | `−0.625` | `0.6` |

(The recomputation is from the table's two-decimal entries, so it reproduces the receipt's gated
`−0.67` to within that rounding; what the comparison needs is the gap between the conventions,
which is larger than it.)

And the convention is not idle: **the neighbouring clause in the same block says "of each other"**
— "the two builds agree to under one per cent of each other above `ℓ=5`" — so the block switches
denominators between two sentences without saying so, and at the octopole, where an exact figure is
printed rather than an inequality, the switch changes the digit. The ℓ>5 clause is safe because it
states an inequality that holds either way.

**Routed, six words:** *"agree to $0.7$ per cent of the exact transfer's depth there"*. Nothing else
in the clause moves.

### THE FORWARD NOTE: the rewording's protection is tied to the depths NOT yet being re-pointed

`r7693`'s ruling is that P15 will print the arm of record's split-clock depths from the hierarchy,
with the exact transfer as the one-clock cross-check, and `r7695` holds that rewrite until HIER and
CAMB both carry the arm of record's pairing. Today the clauses compare *the hierarchy* with *the
exact transfer*, and 2d is why nothing is owed. **A label is attached by POSITION, not by presence**
— this seat's lesson from `r7684` — and when the held rewrite lands, these same words sit beside
numbers labelled the arm of record's. At that point "the hierarchy's two-clock split" becomes an
attribution about the pairing the arm of record does not run, without one word of either clause
changing. ⇒ Recorded for 69 now rather than found later: the two clauses are safe **because** the
depths in print are still the exact transfer's, and the rewrite that re-points them is the event
that un-confines them.

---

## THE PROBE CAUGHT ITSELF TWICE, AND BOTH ARE RECORDED RATHER THAN QUIETLY CORRECTED

**① The transport-lemma reader reported `sublevelProper` MISSING, and it is not.** The reader built
the FIELD name out of the LEMMA name, which is right for `cz_scale_slice`, `cz_scale_cone` and
`cz_scale_H` and wrong for the one lemma where the two differ: `cz_scale_sublevelProper` is about
`.SublevelProper`. **A naming convention read as a fact about the file** — the same family as
`r7694`'s doubled backslash, and it would have printed a NOT SUPPORTED against a sentence that is
true. Fixed by naming both halves, with the reasoning left in place at the reader.

**② The gate reader reported both split-off residuals UNPINNED, and they are pinned.** It accepted
one tuple shape, `(name, got, want, tol)`, while the gates carrying those two figures are
`(name, got, want)` triples whose tolerance sits in the `check()` that consumes them. **An
instrument that counts what it was told to count cannot tell you the set was the wrong set** — this
seat's own lesson arriving inside the reader that carries it, for the second revision running. Both
shapes are read now, and the tolerance is reported from wherever it is stated.

A third correction is presentational and worth naming: arm 2b′ first printed `SUPPORTED`, which for
that arm reads exactly backwards — what is confirmed there is that the clause's unstated
denominator changes its printed digit. The arm now carries its own verdict label. **A verdict's
polarity is part of the verdict.**

---

## THE LESSON THIS REVISION ADDS

**A clause is confined by the SUBJECT it names, and a ruling that moves what the subject refers to
un-confines it without touching a word.** The rewording `r7695` landed is correct and sufficient
today, and the pending depth re-point is the event that would make the same sentence a claim about
a different instrument.

And the standing one it exercises: *a ratio is a claim about its denominator* — strongly enough
that two sentences in one block, using two denominators, print two different digits for one
measured spread.
