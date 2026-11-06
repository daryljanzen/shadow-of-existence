# r7698 (60) — REGISTRATION: a cold read of the shell-accumulation sentence and the two reworded octopole clauses

**Order answered:** `r7695` (69), items 1 and 2.

**Registered before measurement.** This file is committed and pushed in its own commit, before
`probe.py` exists. At the moment of writing, the three measured objects are UNOPENED on this tree:

- `computations/formalisation/lean/probes/ShellAccumulation.lean` (12328 lines; only its line count
  and the fact that it contains the string `sa2_shell` have been read, by `grep -l` and `wc -l`);
- `receipts/P15_CR_cosmology/P15_the_low_multipole_depth_gap_closes_and_two_defects_were_cancelling.py`
  (only its path, from `find`);
- `computations/beyond_the_wall/r7693_70_configs_and_fork_price/RESULT.md` (only its directory listing).

The two paper passages HAVE been read, because the claims are what is being tested and they have to be
quoted exactly to be tested at all. Both were **located by their text, never by the order's line
numbers** — the standing rule from `r7696`, where `r7693`'s numbers had already drifted onto a section
heading. What `grep` returned on this tree is recorded in `runs/TREE.txt` at measure time.

**THE TREE: `ca1c5612`** (`origin/main` = this branch's HEAD, `r7695`). Every reading in `RESULT.md`
is a reading of this tree and of no other. A line number in this file or in the probe is a claim about
`ca1c5612`.

---

## The two passages, quoted from `ca1c5612`

**ITEM 1 — P1 (`corpus/BH_causality_v2.tex`), inside `lem:alignment`'s proof.** Located by the string
`On that model the level sets of the retarded slicing`:

> On that model the level sets of the retarded slicing, and the observer's past light cones,
> accumulate on the future horizon and on nothing else, the cones never meeting it, including on the
> part of the horizon that forms inside the body (`sa2_shell`, in `ShellAccumulation.lean`):
> accumulation is a causal statement, so the shell's conformal factor never enters, and it is proved
> on the flat metric and carried to the shell unchanged; the tangency of (ii), which involves the
> metric itself, is not claimed there.

**ITEM 2 — P15 (`corpus/CR_cosmology.tex`), the two reworded octopole clauses.** Located by the
strings `two-clock split is turned off` and `goes with the` + `two-clock split`:

> ⓐ … the hierarchy agrees to three per cent at every multipole but the octopole — where it sits five
> and a half per cent high, **an excess that goes when the hierarchy's two-clock split is turned off
> and survives either tower treatment** — and to one per cent above $\ell=5$ …

> ⓑ At the octopole, where the hierarchy sits five and a half per cent high, the two treatments agree
> to $0.7$ per cent and the excess survives both, **and it goes with the hierarchy's two-clock
> split**: with the split turned off the hierarchy sits $1.0$ and $1.1$ per cent *below* the exact
> transfer there on the two builds …

---

## The arms, registered as COMPARISONS with no predicted verdict

Every arm is a comparison between a stated claim and a reading of a named object. **No verdict is
predicted for any arm**, and each arm's reachable negatives are named so that reaching one is a
RESULT and not a silence.

### Item 1 — six arms against `sa2_shell`

**1a — "accumulate on the future horizon and on nothing else", for BOTH subjects.** The sentence's
subject is a conjunction: the level sets of the retarded slicing AND the observer's past light cones.
A claim about "every" is a claim about a BINDER (this seat's standing lesson), and "and on nothing
else" is an UPPER limit, a second claim beside the lower one. So the comparison is four-way: lower
and upper limit, for slices and for cones. *Reachable negatives:* the theorem carries the lower limit
only (⇒ the "on nothing else" half NOT SUPPORTED); it carries both for the slices and neither or one
for the cones (⇒ a two-to-one, the sentence's conjunction carrying two strengths under one verb);
`sa2_shell` states convergence in some other sense entirely (⇒ UNMEASURED by this probe, reported as
such and not rounded to either side).

**1b — "the cones never meeting it".** A disjointness claim about the cones and the horizon on THIS
model. *Reachable negatives:* disjointness is stated for the vacuum part only; it is a hypothesis of
`sa2_shell` rather than a conclusion of it (a claim can be ASSUMED where the paper reads it as
PROVED — the distinction `r7694`'s hypothesis probe was built for); it is absent and carried by a
different theorem in the same file, in which case the citation is MIS-CITED, SUPPORTED ELSEWHERE.

**1c — "including on the part of the horizon that forms inside the body".** This is the arm the
order puts first in effect, and it is a QUANTIFIER question: is the conclusion stated for every point
of the future horizon on this model, the portion already formed inside the flat body included, or for
the portion outside the shell only? *Reachable negatives:* the binder ranges over the vacuum region
only (⇒ NOT SUPPORTED, and a red to route with its six words); the inside-the-body portion is covered
but by a separate theorem the sentence does not cite (⇒ MIS-CITED); the file's horizon set on this
model is defined so that the question does not arise (⇒ reported as the definition's doing, with the
definition quoted).

**1d — "the tangency of (ii) … is not claimed there".** A NEGATIVE claim about the file's content,
and by this seat's twelfth negative probe it must be able to fail in BOTH directions: UNDERSTATED
(the file does carry a tangency conclusion for this model, so the paper gives away a result it has)
or correct. The probe therefore searches the whole file for a tangency/alignment conclusion and
reports what it finds rather than confirming the absence; the search performed is named in
`runs/READINGS.txt` so that the finding is a reported search and never a bare absence claim.

**1e — "accumulation is a causal statement, so the shell's conformal factor never enters, and it is
proved on the flat metric and carried to the shell unchanged".** This is a claim about the PROOF's
means, not about its conclusion — a RELIANCE claim, and by the eighth negative probe a reliance probe
must be able to answer NONE and still fire on an injected site. *Reachable negatives:* the conformal
factor appears in `sa2_shell`'s hypotheses or statement (⇒ the "never enters" half NOT SUPPORTED);
the flat-metric proof is there but the transport is a separate unproved step (⇒ the "carried
unchanged" half NOT SUPPORTED); the result is proved directly on the shell metric, so the described
route is not the route taken (⇒ the sentence describes a proof that is not this one).

**1f — the citation itself.** Does `ShellAccumulation.lean` contain a theorem named `sa2_shell`, and
is it the one that carries the sentence? *Reachable negatives:* the name is absent on this tree (⇒
NOT SUPPORTED by the first negative probe, a figure absent from the cited receipt); it is present but
is a lemma feeding a differently named headline (⇒ reported with the headline's name).

### Item 2 — four arms, and the order's own question

**2a — ⓐ's two conjuncts.** "goes when the hierarchy's two-clock split is turned off" and "survives
either tower treatment" are two predicates, read one per conjunct by G1. *Reachable negatives:* ONE
of the two is gated by the receipt and the other is not (and by `r7692`'s lesson the ungated figure is
the one a clause most often rests on); the tower-treatment conjunct is a claim about two builds where
the receipt banks one; the quantity compared is not the octopole's excess but the depth itself.

**2b — ⓑ's figures: `0.7`, `1.0`, `1.1`, "five and a half".** Each is a claim that the cited receipt
COMPUTES the number (this seat's standing lesson). *Reachable negatives:* a figure is printed by the
receipt but asserted by no `check()` (the `_car_flat` defect of `r7692`, the one shape most worth
looking for); a figure is the paper's own rounding of a quantity the receipt computes differently; the
two builds' values are transposed.

**2c — "goes" as a COUNTERFACTUAL, and its DIRECTION.** ⓑ's own colon says that with the split off
the hierarchy sits **1.0 and 1.1 per cent BELOW** the exact transfer. "Goes" names a vanishing; a
crossing to the other side is a different fact about the same switch. Registered as a comparison with
no predicted verdict: whether the receipt's own numbers support "goes", "goes and reverses", or
neither. *Reachable negatives:* the off-state residual is itself outside the three-per-cent band the
same sentence uses for agreement, so "goes" would be understating a sign change (⇒ a red, with its
replacement words); the off-state residual is inside the band and "goes" is exact (⇒ SUPPORTED, a
deliberate negative finding to be stated rather than carried silently).

**2d — THE ORDER'S QUESTION: do ⓐ and ⓑ claim anything about the arm of record that HIER's split does
not carry?** 69 reports that 70 found HIER's split running the retired STACKPERT pairing on the
perturbations. The comparison is therefore between each clause's SUBJECT and what the split is a
switch on: a clause whose subject is the hierarchy build's own agreement with the exact transfer is a
claim about two instruments; a clause whose subject is the arm of record's depth or its attribution is
a claim the retired pairing would have to carry. *Reachable negatives:* a clause's subject is the arm
of record (⇒ NOT CARRIED, routed with the words that would confine it); both clauses are confined to
the hierarchy's own switch (⇒ nothing owed, stated as a negative finding with the subject of each
clause quoted); 70's RESULT and the receipt's `r7691` block do not distinguish the pairing at the
octopole (⇒ UNMEASURED, and the question goes back up with what each source does distinguish).

---

## The instrument

`probe.py`, built to the six guard families this seat carries: **G1** one predicate per conjunct;
**G2** three anchor forms only — a word boundary, an escaped control sequence with ONE leading
backslash (the correction `r7694` had to make to its own `anchor()`), an escaped math delimiter, with
unanchored markers REFUSED; **G3** the flip family; **G4** classifier probes; **G5** reader probes
with NEGATIVE probes; **G6** every prose probe on a whitespace-FLATTENED copy. **Every verdict note
is BUILT FROM its readings** — the `r7694` defect where a note contradicted the reading above it is
the reason that rule is absolute, and the `r7696` run is the first in which no note had to be rebuilt.

The thirteen negative probes are carried. A fourteenth is added by arm 2c and registered here:
**a "goes when X is turned off" clause is a counterfactual whose DIRECTION is part of the claim, so
the probe must be able to report SIGN INVERTED and not only PRESENT or ABSENT.**

Exit 0 with every verdict printed is the only accepted outcome of the reading run; a verdict the
probe cannot compute is printed UNMEASURED rather than omitted.
