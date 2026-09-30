# r7059 Q1 → 70: does `P10` `sec:lock` say what its cited receipts compute? — PRE-REGISTRATION

*Node 70. Committed before any cited receipt is run and before the tracer touches this passage. Scoping read the
passage and listed its markers; nothing has been matched.*

## The range, declared

- **The passage is `corpus/canonical_time.tex` lines 918–1057 at `a3705946`.** It runs from "The shift at this
  level is then a number rather than a structure" (the two-mode shift) to the end of the back-reaction paragraph
  closed by the four-receipt group.
- **One trailing marker is included**, `P10_the_vertex_numbers_are_exact…` (line 1063). It closes the
  non-resonance and a⁻⁶ sentences, which are part of the same paragraph.
- **Markers:** seven receipts in three groups.
  - **G1:** `same_level_sum…`, `level_cubic_vanishes…`. These close the two-mode shift, the even-level selection rule
    and the orthogonality identity.
  - **G2:** four receipts, one group:
    - `cubic_normalisation…` (r7058);
    - `odd_residue_is_five_levels…` (r7056);
    - `cubic_vertex_is_written_down…` (r7053);
    - `odd_residue_is_the_levels_below_a_crossing…` (r7050/51).

    These close the ε³ identity, the recoupling sums, the covariant-derivative finding, the normalisation, the
    threshold and the residue.
  - **G3:** `vertex_numbers_are_exact…`.

## The instrument (the `r7043` method, unchanged)

- **The claim** is the passage since the previous marker or paragraph break. Its **numbers** are decimals, integers
  of two or more digits, and fractions p/q read as p and q and as their value. They are normalised out of LaTeX.
- **What the receipt says** is its source **and** its output. Every cited receipt is **re-run** from its own
  directory, and one that does not exit 0 is recorded as that.
- **The match** is at the paper's own precision. A number is supported by the GROUP when any member carries it.
- **Every miss is read by hand** before it is scored, as a unit conversion, a restatement, a product or a ratio.
  Each gets a reason.

## The two questions the order adds, and how each is scored

- **Q-S, superseded against superseding.**
  - For every number the passage states, every member of its group that carries a value **for the same quantity**
    is listed.
  - Where two members disagree on that quantity, the paper must be quoting the **later** receipt.
  - ⚠ **Scored by quantity, not by receipt age.** Following the order, a figure from an earlier receipt is stale
    only if a later receipt gives **that quantity** a different value. A receipt being superseded "in part" makes
    nothing in it stale by itself.
- **Q-I, independence.** For each G2 member it is recorded whether it recomputes its quantities, or loads banked
  output (`np.load`, `json.load`, `pickle`) or imports from another member.
  - The report is the dependency graph among the four, and **how many independent derivations stand behind the
    threshold and the sign**.
  - It is reported against how the paper's sentence reads. Four markers on one sentence read as four supports.

## Outcome table — the one costing another seat most FIRST

| | outcome | what it would mean |
|---|---|---|
| ① | the paper quotes a superseded value for a quantity a later co-cited receipt changed | a stale headline in the passage the gate has rewritten four times |
| ② | a number no cited receipt computes (iii), or computed only by an uncited one (ii) | the r7043 classes, routed in the usual way |
| ③ | the four-receipt group is one derivation on banked machinery, and the sentence reads it as four | the "both arms" shape, in the quantum sector |
| ④ | none of ①–③ | **the passage is clean**, read cold against its receipts, and that is said in writing |

## Gates

- Gates are on receipt content: numbers present in or absent from each receipt's source and output, and the
  dependency edges.
- The paper's wording is **reported, never required**.

## ⛔ NOT CLAIMED

- No reconciliation of the two anchors' conventions; that is routed to node 60.
- No verdict on the physics, and no re-derivation.
- No prose edited, and no other seat's receipt touched.
