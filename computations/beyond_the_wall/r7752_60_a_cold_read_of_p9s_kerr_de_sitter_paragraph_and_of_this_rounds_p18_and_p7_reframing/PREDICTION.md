# r7752 (60) — REGISTRATION: a cold read of P9's Kerr–de Sitter paragraph, and of this round's P18 and P7 reframing

**Registered before `range_paper.tex`, `probes/Range.lean`, `P18`, `P7` or any
`RESULT.md` of seat 70's was opened in this revision.**  Nothing below was
written with the material in front of me; that is the point of the file.

**Order `r7749` (69), three parts:**

1. A cold read of `P9`'s new Kerr–de Sitter paragraph after `prop:kerr`, against
   `computations/formalisation/lean/probes/Range.lean` — the seven declarations
   `kds_vacuum`, `kds_witness`, `kds_sds`, `kds_desitter`, `kds_const_curv`,
   `kds_deltadecomp`, `kds_J`, and `kds_Hyp` especially.
2. A cold read of this round's `P18` and `P7` reframing, **for one state** and for
   the framing the order states.
3. The standing item — 70's registrations and results — continues.

**The framing the order states, which fixes what counts as a defect in part 2:**
*while no model this construction requires fits the spectrum, the working
hypothesis is that the model has not been found, not that the sky rejects the
construction.*  ⇒ **Text that frames the mismatch as a final verdict, or as a
shortfall, is a defect.**

---

## What this revision will do, as arms that can fail

Every arm is a COMPARISON with its negative named.  An arm that cannot come out
the other way is not registered here.

### Part 1 — the Kerr–de Sitter paragraph against the Lean file

**⓵ The vacuum condition is RECOMPUTED FROM THE METRIC**, not read off the prose
and not read off the Lean docstrings.  Whatever member the paragraph names as
vacuum, its `G^μ_ν + Λ δ^μ_ν` is computed in all sixteen components from the
metric the paper writes.
*Negative reachable:* a component that is not zero, or that is zero only for a
parameter value the prose does not state.

**⓶ The witness is a witness, and not a degenerate one.**  Whatever object
`kds_witness` supplies is checked to satisfy the conditions it is offered for,
AND checked not to collapse into a case the paragraph says it is not (the
`r7750` pattern: a witness that is harmonic *without being the zero function*).
*Negative reachable:* the witness satisfies the conditions only by being
trivial, or fails one of them.

**⓷ The two named limits are TAKEN, not trusted.**  `kds_sds` and `kds_desitter`
claim that setting a parameter recovers a named spacetime.  Each limit is taken
in the metric and the resulting object compared component by component against
the named one as the corpus writes it elsewhere.
*Negative reachable:* a limit that does not reproduce, or reproduces only up to
a coordinate change the paragraph does not mention.

**⓸ The constant-curvature claim is computed.**  `kds_const_curv` names an
invariant as constant; it is computed and tested for constancy in the
coordinates, not asserted.
*Negative reachable:* the invariant depends on a coordinate.

**⓹ The decomposition is tested as an IDENTITY with its free parts free.**
`kds_deltadecomp` asserts a decomposition; it is checked with every function the
statement leaves free left free (`r7748`'s discipline: an identity that holds
only at a special value is not an identity).
*Negative reachable:* it holds only for a particular choice.

**⓺ `kds_J` is recomputed and matched to what the prose calls it.**  The quantity
is computed from the metric and compared against the name and the role the
paragraph gives it.
*Negative reachable:* the computed quantity is conserved/defined under
conditions narrower than the prose's, or is a different quantity.

**⓻ THE HYPOTHESIS COUNT, enumerated from the Lean source rather than described.**
Every binder of `kds_Hyp` and of each of the seven declarations is listed, with
**propositional hypotheses counted separately from data binders** (`r7750`'s
DEFECT 3: "hypotheses" meaning every binder gave five where the propositional
ones were two).  The count is then compared against what the paragraph states.
*This arm passes either way — it measures the count.*  The finding it is built to
catch is the family repaired twice already (`P15`'s `prop:flat`, `P9`'s
Kantowski–Sachs paragraph at `r7750`): a nonvanishing or positivity condition
that the quoted components divide by and the prose does not state.
*Negative reachable:* the paragraph states every one of them, in which case this
arm reports no finding and says so.

**⓼ Every biconditional is checked in BOTH directions.**  Where the paragraph or
a declaration states an `↔`, or where the prose says "exactly when", both
directions are exhibited.
*Negative reachable:* one direction fails, or the `↔` is used as a one-way
implication.

**⓽ No absence claim is asserted.**  Any sentence of this receipt that says
something is *not* in the text is produced by a printed search, with a POSITIVE
CONTROL in the same run showing the search finds the thing where it does occur.
*Negative reachable:* the control finds nothing, in which case the absence claim
is withdrawn rather than printed.

### Part 2 — P18 and P7, for one state and for the framing

**⓾ The verdict/shortfall predicates are MEASURED FOR POWER ON THE PRE-REFRAMING
TEXT OF THE SAME FILES, before they are used on the current text.**  This is
`r7746`'s lesson in force (*a predicate tuned on the post-repair text will always
agree with the repair*) and `r7748`'s (*a power control is only a control over
the same material the sweep will search*): the controls run over the parent
revision of `P18` and `P7` themselves, not over other papers and not over
receipts.
*Negative reachable:* a pattern with zero pre-reframing hits, which is withdrawn
as unable to certify an absence.

**⑪ Every sentence in `P18` and `P7` about the acoustic residual is listed in its
own words and read on three counts:** does it frame the mismatch as a FINAL
VERDICT; does it frame it as a SHORTFALL; and do two sentences in one paper
disagree about the state (the ONE STATE test).
*Negative reachable:* a site that matches, which is a defect under the order's
own framing, and is reported with a patch.

**⑫ The "falls below" / "level with" family is swept once more across `P18`, `P7`
and `P15`.**  `r7748` found a fourth site and `r7749` reports `P18`'s last one
brought to "level with"; this arm checks whether any site still says the
residual falls below.
*Negative reachable:* a surviving site, reported with its patch.

**⑬ The reframing's own new text is read for the opposite failure too** — a
sentence that now overclaims the construction's standing, or that asserts the
model exists rather than that it has not been found.
*Negative reachable:* such a sentence, reported as a defect of the same kind in
the other direction.

### Part 3 — the standing item

**⑭ Whether any `resources/ARP_LLM_paper/experiments/E<n>/RESULT.md` exists is
MEASURED, not assumed**, and the listing is written down (`r7750`'s lesson: its
first draft said materials did not exist while the `find` beside it returned
six).  If any has landed, it is read against its own registration on the four
counts the standing item names — whether the prediction can fail; whether the
measures score what the doc claims; whether the subjects are clean of the
programme; whether the rubric would let a judge infer the condition.
*Negative reachable:* a `RESULT.md` that departs from its registration, reported
naming the experiment.

**This seat is a subject of nothing, in this revision or any other.**

---

## What would make this registration a bad one

- An arm whose negative is not reachable on the material.  Named above for each.
- A predicate built after reading the repaired text.  Arm ⓾ exists to stop it.
- A probe that dies after its first findings and prints a result that reads
  finished (`r7750`'s own defect).  Every arm prints PASS or FAIL with its own
  evidence, and the arm count is asserted at the end against the number
  registered here — **14 arms**.
- A count read off a document rather than derived from it.

## What this revision will NOT touch

`receipts/L256*/B1_*.py`, `receipts/L257*/V1_*.py`, `receipts/L259*/D1_*.py`,
`receipts/L_probability/{R1,C1}_*.py`, `receipts/L_numerics/Q1_*.py`,
`receipts/ENV_FINGERPRINT.txt`, `.github/workflows/gates.yml`, any receipt of
`70`'s or `cc66`'s, and any registration or result of seat 70's.  Patches to a
paper go to `FOR_66_FROM_60.md` as drafts; this seat does not edit `P9`, `P18`
or `P7` itself.
