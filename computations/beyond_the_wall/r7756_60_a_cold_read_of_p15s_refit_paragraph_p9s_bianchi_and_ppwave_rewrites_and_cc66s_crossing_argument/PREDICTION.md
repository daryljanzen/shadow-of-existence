# r7756 (60) — REGISTRATION

**Order `r7755` (69).** A cold read of three things:

1. `P15` `sec:refit-bound`'s new refit paragraph — "Refitted, it stays level …" through "… the only
   one that does this" — against `70`'s and `cc66`'s receipts.
2. `P9`'s rewritten Bianchi and pp-wave paragraphs, against `bi_Rfull`, `bi_W`, `bi_IJ`, `pw_IJ` and
   `pw_typeN` in `computations/formalisation/lean/probes/Range.lean`.
3. `cc66`'s `r7753+cc66` §② and §③: the quotes, the λ algebra, and whether §②'s identification of the
   lapse's congruence with the content's congruence is **stated anywhere in the corpus or assumed** —
   read **as a skeptic of the argument, not of the data**, and for each premise separating where it is
   **argued** from where it is only **carried forward**, by the revision that introduced it.

**Registered before the first read of any of the three objects.** Nothing below is conditioned on what
they say: the arms are written from the order's description of them and from a structural survey only
(which declarations exist in `Range.lean` by name, which `###` headings `cc66`'s reply carries). No
paragraph text, no Lean statement body, no `cc66` section body has been opened at registration time.

**The tree.** Every arm runs on `origin/main` as merged into this branch at registration, and the probe
prints the HEAD it ran on at the top of its output. *`r7754`'s lesson: a search is only as good as the
tree it runs over; the tree is part of the predicate.*

---

## What each arm compares, and what a failure would look like

Each arm is a COMPARISON. The negative named is reachable: it is a state the corpus could be in.

### Part 1 — `P15`'s refit paragraph

**① Every figure the paragraph prints is sourced and reproduces.** For each number in the paragraph,
locate it in a pushed receipt or `RESULT.md` under `70`'s or `cc66`'s trees and recompute or re-read it
from that source's own tables. PASS iff every printed figure has a source and agrees with it.
*Negative: a figure with no source in either receipt, or one that disagrees with its source.*

**② The paragraph's comparative claims are the comparisons the receipts actually made.** For each
comparative ("stays level", "is not improved", or whatever the paragraph says), check the receipt's own
arms compare the same two objects on the same statistic. PASS iff every comparative matches a
comparison the receipt made. *Negative: a comparative whose two sides are not what the receipt scored.*

**③ "the only one that does this" — what it quantifies over, and whether anything establishes the
set.** A uniqueness claim is a claim about a set. Determine, from the paragraph alone, what set the
"only one" ranges over; then check whether a receipt enumerates that set or merely scores members of
it. PASS iff the set is determinate from the sentence AND a receipt establishes it is exhausted.
*Negative: the sentence's set is indeterminate, or no receipt enumerates it — a uniqueness claim
resting on an unenumerated set.* (THE GUARDS: a defence against a state changing must ENUMERATE the
states; before two stretches are identified by a label, check how many-to-one the label is.)

**④ The paragraph does not use `70`'s instrument θ\* pull.** `r7755` states that no paper sentence uses
it and that `70`'s corpus-definition θ\* is in the register only. Search the paragraph — and, as a
control, the whole of `P15` — for the pull and for its figure. PASS iff the paragraph uses neither.
*Negative: the paragraph carries the pull or its number.* This arm has a POSITIVE CONTROL: the same
search run over the version of `P15` before this round's rewrite, where any earlier use would show.

**⑤ The direction of the improvement.** At `r7754` this line established, from `70`'s own figures, that
its **no-fit** arm already scores below the control's no-fit, so the improvement is in the distance
assignment rather than in what the refit does. Check whether the paragraph's wording is consistent with
that decomposition. PASS iff the paragraph either makes the distinction or makes no claim that needs
it. *Negative: the paragraph attributes to the refit what the no-fit arm already had.*

### Part 2 — `P9`'s Bianchi and pp-wave paragraphs

**⑥ Each cited declaration asserts what the sentence citing it says.** For `bi_Rfull`, `bi_W`, `bi_IJ`,
`pw_IJ` and `pw_typeN`, read the Lean STATEMENT and compare it, clause by clause, with the paper
sentence that cites it. PASS iff every citation's claim is in its declaration's conclusion.
*Negative: a sentence claims X and cites a declaration that asserts something weaker than X — in
particular the eigenvalue sentence, whose new form argues from "block form on the bivector pairs":
block form is a statement about an operator, and the arm asks whether a cited declaration states it.*

**⑦ The hypotheses travel with the claim.** Each cited declaration has hypotheses (vacuum, distinct
`Cᵢ`, `cosh 3t > 3`, `0 < t`, harmonic or arbitrary `H`, …). For each, check the paper sentence carries
the condition or its paragraph states it. PASS iff no sentence asserts unconditionally what Lean proves
conditionally. *Negative: a condition load-bearing in Lean and absent from the paper's stem.*
(THE GUARDS: if the hedge is load-bearing it belongs in the stem.)

**⑧ The Bianchi invariants recomputed independently.** Recompute `I` and `J` for the vacuum Bianchi I
family from the metric this line already built at `r7754`, and check `I³ − 27J² = ¼·Π(Eᵢ − E_j)²` and
`I³ ≠ 27J²` under the stated condition, by this seat's own computation rather than by reading Lean.
PASS iff the identity holds as an identity in the `Cᵢ` and the condition is the one that makes the
product nonzero. *Negative: the identity fails, or holds only under a stronger condition than the one
printed.*

**⑨ The pp-wave invariants recomputed independently.** Recompute `I` and `J` for the pp-wave metric and
check they vanish for ARBITRARY `H`, and separately check the type-N criterion on `H = x² − y²`. PASS
iff both reproduce. *Negative: either fails, or holds only for harmonic `H` where the paper says any.*

**⑩ The cited declarations are axiom-clean and non-vacuous.** For each of the five, check `#print
axioms` is clean (no `sorryAx`) and that its hypotheses are satisfiable — by the declaration's own
witness where one exists, by exhibiting one otherwise. PASS iff all five are clean and all five have a
reachable instance. *Negative: a `sorry`, or a theorem whose hypotheses nothing in the file meets.*

**⑪ The paragraph's own reading is checked for a trivially-true citation.** At `r7754` one witness's
statement was trivially true and earned its keep only through its proof. Check each of the five for the
same shape and print the verdict either way. PASS iff the verdict is printed for all five, whichever
way it falls. *Negative: not applicable — this arm fails only by not being carried out.*

### Part 3 — `cc66`'s `r7753+cc66` §② and §③

**⑫ Every quote in §② and §③ is in print verbatim.** Extract each quoted string and match it as an
EXACT string against the tracked corpus at the current HEAD, recording the file and the count. PASS iff
every quote matches exactly once or, where it is a stock phrase, at the site `cc66` names.
*Negative: a quote not in print as quoted, or in print at a different site than the one claimed.*

**⑬ The λ algebra of §③ reproduces.** Redo §③'s algebra symbolically from its own premises. PASS iff
this seat's recomputation reaches §③'s conclusion with the same quantifier.
*Negative: the algebra gives a different relation, or gives it only on a family while §③ states it
for ANY amplitude.*

**⑭ §③'s "at ANY amplitude" is a universal the argument actually supports.** Separate the step that is
universally quantified from any step checked on a family or at a point. PASS iff every step in the
chain to the universal is itself universal. *Negative: a universal conclusion resting on a step
established at sample values.*

**⑮ The identification of the lapse's congruence with the content's congruence: stated or assumed.**
Search the whole tracked corpus for the identification as a stated claim. Then, whatever the answer, locate
the revision that introduced it with `git log -S` over the papers and the receipts, and report whether
that revision ARGUED it or CARRIED IT FORWARD from an earlier one. PASS iff the arm returns a located
answer of either kind with its revision. *Negative: the arm cannot locate it at all — which is itself
the reportable answer, and must then be reported as "not locatable", never as "assumed".*

**⑯ Every premise of §② and §③ is classified argued-vs-carried-forward, by revision.** Enumerate the
premises; for each, find the earliest revision that states it and say whether that revision gives an
argument or cites a predecessor. PASS iff every enumerated premise gets a revision and a verdict.
*Negative: a premise whose first statement cannot be located, reported as such.*

**⑰ A skeptic's arm against this seat's own reading.** For each of the three parts, state one way THIS
read could be wrong and test it. PASS iff all three are tested and the verdicts printed.
*Negative: fails by not being carried out.*

---

## Controls

* **⑤ and ④ carry a positive control over a version where the thing searched for was still present** —
  the pre-rewrite `P15`. *`r7752`'s lesson: a power control must be over a version in which the thing
  searched for was STILL PRESENT, and the parent of the current change is not that version when the
  repair is older than the change.*
* **⑧ and ⑨ are independent of Lean**: they recompute from the metric, so a Lean statement that says
  something other than what it is cited for cannot make them pass.
* **⑫ runs on the merged tree and prints the HEAD it ran on.**

## Arm count

**SEVENTEEN arms: ① ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩ ⑪ ⑫ ⑬ ⑭ ⑮ ⑯ ⑰.** Any arm added after the first read of the
material is marked AMENDMENT and registered in its own pushed commit before it is run.

**This seat is a subject of nothing here.**

---

# AMENDMENT (registered after the first read, in its own pushed commit, before arm ⑱ is run)

**Why it is added.** `cc66`'s `§③` fences its own scope and names the next question outright:
*"Whether ANY admissible cut reproduces `H_leaf` exactly is a different, computable question — invert
`H²(r) = H²_leaf(z(r))` for the mass function it demands and ask whether that `m(r)` is admissible … I
have not computed it, and I am not claiming it."* Arm ⑭ measured the same conclusion on the DISTANCE
for the `r^-4` family; the general question is one inversion away and is the whole of the live row.

**⛔ DISCLOSED, because register-before-measure is the rule this line works under: the algebra was
sketched by this seat during the read, before this amendment was written.** It is registered here so
that the check is run mechanically against the corpus's own printed relations and this seat's own
published instrument, rather than against that sketch, and every figure it yields is labelled
**POST-REGISTRATION** in the result. The outcome is not protected by this registration; the *procedure*
is.

**⑱ The mass function the leaf rate demands, and whether it is admissible.**
Using the corpus's own relations, read by path and not reimplemented — `r7580/lightpath.py`'s `H_stack`,
`H_leaf`, `r_of`, `r₀` and the background, and `P15`'s printed `f(r) = 1 − 2GM/c²r − r²/α²` — form the
mass term `μ(r) ≡ 2Gm(r)/c² = r³[(H/c)² − 1/α²]` on each rate law and compare.
PASS iff **all three** hold: ⑴ `μ_stack(r)` is CONSTANT in `r` to numerical precision (the control: the
stacking rate is the vacuum cut, so a non-constant answer means the setup, not the physics, is wrong);
⑵ `μ_leaf(r)` is reported with the sign of its derivative stated; ⑶ the verdict on admissibility is
stated as what the sign gives — `m′(r) ≥ 0` admissible, `m′(r) < 0` a negative density and therefore
not.
*Negative reachable in both directions: `μ_leaf` increasing would say an admissible cut DOES reproduce
the leaf rate, which would overturn `§③`'s suggestion and this seat's expectation; a non-constant
`μ_stack` would void the arm.*

**Arm count: EIGHTEEN.** ⑱ is this amendment's only arm, and it is the only one run after the first read.
