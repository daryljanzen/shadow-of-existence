# r7706 (60) — PREDICTION, registered before measurement

**Order answered:** `r7703` (69), the topmost section of `origin/main:FOR_60.md`. Three items:
① the `prop:cycloid` fix, and **every** sentence in P2 that uses the cycloid or the
horizon-to-singularity time `Mπ` — does any still read as true for *every* radial geodesic?
② the new formal paragraph after `cor:Kretschmann_at_z0`, against
`computations/formalisation/lean/probes/CircleKretschmann.lean` — hypotheses, the
complex-extension reading of the pole, and "not itself built as a chart".
③ P15's trimmed scope sentence, the `FROZEN` comparison having been cut.

**Tree:** `f38156a9` (`origin/main` = `r7703`, this branch fast-forwarded onto it).

## WHAT HAS BEEN READ AT THE MOMENT OF REGISTERING, exactly

- The order section itself, in full, from `origin/main:FOR_60.md`.
- **One** `grep -n "prop:cycloid\|cycloid" corpus/janzen_circle_v3.tex`, whose matched lines
  are long paragraphs, so this is a WIDE read of P2's cycloid prose and is declared as such:
  it is why some candidate sites below are already named. It is NOT a read of the repaired
  statement or proof at source, NOT a read of the new formal paragraph, and NOT a read of any
  `Mπ`-printing site found by content rather than by the word "cycloid".
- `wc -l` and a directory listing for `CircleKretschmann.lean`. **Nothing inside it.**
- Nothing in P15 beyond what earlier revisions established.

## ITEM ① — THE CYCLOID FIX AND THE SURVIVING SITES

`r7704` found `prop:cycloid` reading as general while its proof's first line was the `E = 0`
member, and routed six words. The order says the fix landed: the statement now names
"the radial timelike geodesic of vanishing Killing energy, `E = -g(u,∂_t) = 0`, which reaches
`r = 2M` at rest", and the proof opens with the general `(dr/dτ)² = E² - 1 + 2M/r` and then
sets `E = 0`. **Arm 1a** checks that text is there, at source, in both places.

**THE REAL QUESTION IS THE REST OF THE PAPER, and it has a discriminator that must be
registered BEFORE the sites are read, because afterwards it will look obvious:**

> A sentence that speaks generally of "a radially infalling test particle" or "the infalling
> worldline" is a DEFECT only if what it asserts is `E`-DEPENDENT. Finiteness of the fall is
> `E`-independent — every radial timelike geodesic reaches `r = 0` in finite proper time, and
> `r7704` measured seven members, all finite. The CYCLOID FORM `r = M(1+cos η)`,
> `τ = M(η+sin η)` is `E = 0`'s alone. The VALUE `Mπ` is `E = 0`'s alone.

So the predicate is: **does the sentence attribute an `E = 0` object (the cycloid form, the
figure `Mπ`, "at rest at the horizon") to a general infaller?** A general sentence asserting
only finiteness, or only that the worldline ends at `r = 0`, is CORRECT and must be reported
as correct. **Conflating those two classes would be this revision's own version of the error
`r7704` caught in the paper, one level up, and the probe is built to keep them apart.**

**Registered expectation, moderate-to-high confidence: at least one surviving site attributes
an `E = 0` object to a general infaller.** Two candidates are already visible in the grep and
are named now so that "finding" them later is not mistaken for a result:

- the sentence that the Schwarzschild interior *is* the cycloidal motion of a radially
  infalling test particle, with `τ` the arc length — attributes the FORM;
- the sentence that the cycloid parametrises a single radial geodesic — this one may be
  exactly right, since "a single" is weaker than "any", and that is the point of the
  discriminator.

**Reachable negative, and it must stay reachable:** every surviving site may already be
scoped, or may assert only `E`-independent content. Then the answer is **NO DEFECT FOUND**,
and the probe's readers are tested on an injected general statement AND an injected
restriction so that this answer is produced by a reading and not by failing to look.

**And one site class the grep CANNOT have found: a site that prints `Mπ` (or `πM`, or
`\pi M`) without the word "cycloid".** Those are searched by content, in every spelling the
file could use, and the count is reported with the search named — `r7704`'s own lesson that an
instrument reads the FORM it was given and not the QUANTITY, three instances running.

## ITEM ② — THE FORMAL PARAGRAPH AGAINST THE LEAN PROBE

Registered as COMPARISONS, no verdict predicted for any:

- **2a** Each of the six names the paragraph prints — `ck_prop_critical`, `ck_prop_Kretschmann`,
  `ck_chain_rule`, `ck_cor_Kretschmann_at_z0`, `ck_horizon`, `ck_interior` — exists in
  `CircleKretschmann.lean` as a declaration, spelled as printed.
- **2b** **THE HYPOTHESIS ARM, and `r7700`'s lesson is that it cuts both ways.** For each
  named theorem, the hypotheses it actually asks are listed from source and compared with what
  the paragraph's sentence implies. Two distinct defects are possible and the arm reports which:
  the sentence omitting a hypothesis the theorem asks (the paper claims more than is proved),
  or the theorem being MORE GENERAL than the sentence (`r7700`'s outcome, which is not a
  defect). The hypothesis lister must be Unicode-aware — at `r7700` an ASCII-only pattern made
  `hτ` invisible and the arm it fed was the *wholeness* of a hypothesis list.
- **2c** "The twelfth-order pole is read as a pole of the complex extension." Checked against
  what the Lean statement is actually ABOUT: an order/pole statement for a complex-analytic
  extension, or an order statement about a real function. These are different objects and the
  paragraph's claim is about which one.
- **2d** "`z` is not itself built as a chart." **This is a TEXTUAL ABSENCE CLAIM about a
  15,399-line file, and it gets a named search, not a glance** — chart/atlas/manifold-structure
  constructions enumerated by marker, every hit's surrounding declaration read, and the
  verdict carrying the marker list and the hit count. `NOT FOUND` is said as `NOT FOUND`, never
  as "there is none". The gate that exists for exactly this collapse is the reason the search
  is registered in advance.
- **2e** Axiom hygiene: whether the probe's `axiom` lines are the standard set the other
  campaigns use, or whether any axiom carries the content the paragraph credits to a proof.

## ITEM ③ — P15'S TRIMMED SCOPE SENTENCE

- **3a** The `FROZEN` comparison is gone from the scope sentence, read at source.
- **3b** Searched, not assumed: does any OTHER site in P15 still print or rely on the cut
  `FROZEN` figure? The search phrases are named in the result.
- **3c** What the trimmed sentence now claims is supported by what remains — the sentence is
  read whole, not just its diff, because a cut can leave a clause whose subject has moved.
  (`r7698`: a clause is confined by the SUBJECT it names, and moving what the subject refers to
  un-confines it without touching a word.)

## GUARDS AND SELF-TESTS, carried forward unchanged

G1 one predicate per conjunct. G2 three anchor forms only (word boundary; escaped control
sequence with one leading backslash; escaped math delimiter) — unanchored markers REFUSED.
G3 the flip family, striking EVERY copy of a conjunct and not only the first (`r7702`).
G4 classifier probes tested on both classes. G5 reader probes with negatives. G6 every prose
probe on a whitespace-FLATTENED copy. Every verdict note BUILT FROM its readings.

**The seventeen negative probes stand. The four this revision is most exposed to:**
(15) a "local"/"scoped" claim is a claim about its SUPPORT, so a restriction that names a
member is not the same as one that names the family; (16) a figure search must distinguish a
SURVIVING old value from a DELIBERATE cross-check, so the label beside each hit is read and
not only the digits; (17) when another seat has already named the defect, the probe must be
able to return NO DEFECT FOUND, and that answer must be reachable by a reading.
And newest, from `r7704`: (18) **a tolerance is part of the instrument**, so a reading that
misses by more than its tolerance is two claims, one about the object and one about the
method, and the method is tested first — no tolerance is loosened in this revision to make an
arm pass.

**WHAT THIS REVISION CANNOT DO, registered before the numbers:** it cannot certify
`CircleKretschmann.lean` as a proof of the paragraph's mathematics. It reads declarations,
hypotheses, axioms and the shape of statements. Whether each proof term closes is CI's
`check_no_sorry` and the Lean build's business, and this probe says so rather than implying
its readings are a verification.
