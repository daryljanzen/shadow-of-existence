---
name: six-fields-work-order
kind: METHOD
current: r3605
job: The revised field-bake procedure for the six fields below the ×40 floor, written after running one by hand for four turns. Supersedes the r3522 order.
sources: [chat]
---

WORK ORDER FOR 60 - THE SIX REMAINING FIELD BAKES, ON A REVISED PROTOCOL

FROM 59. This supersedes the cc54 order of r3522. Read the whole thing before starting;
the changes are in sections 3 and 5 and they are the reason this is being handed over.


WHAT IS ALREADY DONE, SO YOU START FROM TRUTH

INTEGRABLE_SYSTEMS_LEDGER.md is open on main. I ran it by hand for four turns to find
out what the protocol should be, and I stopped deliberately rather than finishing it.
Its state is stated at the top of the file and is accurate:

  - R0 baseline measured over all seventeen bodies, word-bounded and de-macroed.
  - Four papers READ and scored: P09, P07, P11, P10. Thirteen not read, no verdict.
  - Two probes bitten: I0 (a canon row) and I1 (landed in P09 with its marker).
  - I4 scoped rather than answered.
  - The registry has a nineteenth row and the ledger block already counts it.

Finish that field first, then take the other five. Do not re-run its R0.


1. THE ORDER

  1. INTEGRABLE SYSTEMS - x37 - IN PROGRESS, 4/17 read, finish it
  2. DIFFERENTIAL TOPOLOGY / INDEX THEORY - x24 - Atiyah x17. The
     Atiyah-Hirzebruch obstruction is the whole mechanism of P13's chirality wall,
     and P14's leaf index is an index-theorem claim its own text marks as TRACED
     RATHER THAN COMPUTED. That is the single most load-bearing untested step in
     the matter sector and it is why this field is second despite the count.
  3. INFORMATION THEORY - x32 - screen "entropy" hard; horizon thermodynamic
     entropy will be most of it and is a homonym for this field's object.
  4. NUMBER THEORY - x31 - screen "zeta"; likely a regularisation or a coordinate.
  5. NUMERICAL ANALYSIS - x20 - screen "convergence"; causal convergence dominates.
     This field's real target is the corpus's computational receipts, not its prose.
  6. PROBABILITY / STOCHASTIC - x6 - thinnest. A bounce here is a result.

No field is taken up until the one before it meets the bar.


2. WHAT HAS NOT CHANGED

R0 baseline first, through corpus/reach_baseline.py, before asserting any hole.
Ten or more numbered probes. Receipts that run, at least two, each able to have
returned otherwise. Three registers kept apart - what BIT, what BOUNCED, what the
BOUNDARY is. Register the field in corpus/field_survey.py. The reading standard: a
seventeen-row status table, every paper WORKED or CHECKED-NEGATIVE by name, papers
checked and found negative LISTED. A lead register with every row marked.


3. WHAT HAS CHANGED, AND WHY - THIS IS THE PART THAT MATTERS

THREE CHANGES, EACH FROM A FAILURE THIS CORPUS ACTUALLY HAD.

(a) EVERY PROBE NAMES ITS DESTINATION WHEN SCORED, AND THE DESTINATION IS CHECKED
    AT THE SITE - the paper opened and the passage read, not inferred from the
    register's subject.

    Why: the eighteen-ledger gather campaign found the routing recorded at bake time
    was the least reliable field in every table. Four routings were wrong in ways
    that reading caught: S7 was routed to P06 and belongs in p0; a figure-theorem
    register was routed to P01 and belongs in p0; F13 and K4 were routed to papers
    and belong in the ontology map.

(b) A REGISTER WITH NO HOME IN ANY PAPER GOES TO ONTOLOGY_FOUNDATION_INDEX AT BAKE
    TIME, NOT INTO A PAPER AND NOT LEFT IN THE LEDGER.

    Two kinds qualify. A claim about how corpus pieces RELATE - no single paper owns
    it, which is exactly why no single paper ever carried it. And a claim about which
    of the corpus's WORDS carry two senses - that is a statement about the corpus.
    The precedent is K4, landed in the map at r1895; kernel went there at r3579 and
    integrable's six senses are going there now.

(c) THE \ldg MARKER GOES IN THE SAME COMMIT AS THE SUBSTANCE.

    The rail did not exist when the six earlier fields were thrown. It exists now:
    corpus/ledgers.sty, corpus/make_ledger_appendix.py, corpus/ledgers_registry.md.
    A landing without its marker is half done and the fourth grain of
    check_depmatrix will say so. Add your field's row to the registry when you open
    it; nothing hard-codes the count and the block picked up a nineteenth row with
    no code change.

    Concretely, per landing: place the clause with \ldg{your_field}; regenerate that
    paper's Appendix L; if you added a \cite the PAPER matrix moved too, so
    regenerate both grains; run check_depmatrix.


4. THE THING I MOST NEED YOU NOT TO DO

DO NOT SCORE A PROBE FROM A GREP.

I did, twice, in the first turn of the integrable bake, and marked both PROVISIONAL
because of it. One of them - I0 - only became real when I READ P07 and found both
colliding senses of "integrable" sixteen hundred characters apart in one paper. A
cross-paper count shows different papers using a word differently, which is ordinary
and not worth a row. One paper using both senses about one construction is what
actually misleads a reader, and no count can tell those apart.

The screens find candidates. They cannot grade them. Every one of this campaign's
nine instrument failures was a screen returning a confident wrong answer: a filename
search that could not see a landing; an escaped underscore returning a clean zero; a
ledger's vocabulary searched against a corpus that uses its own; \ref and \label
counted as prose; a % masthead counted as prose; a marker buried in a comment; a
double-escaped \b in a raw string; the wrong slice of a ledger; the wrong eigenvalue
convention. Every one was caught by reading or by cross-checking, none by a gate.

AND THE TWO-SIDED RULE, WHICH COST THE MOST TO LEARN:

  A landing-table row is a QUOTATION, not a summary. Read the register's worked
  statement in the ledger body before landing it.

  AND A ROW IS NOT STRUCK ON A SINGLE NEGATIVE SEARCH EITHER.

I struck a register as fabricated, wrote a long note calling it the campaign's worst
failure, and was wrong: the register was real, receipted, and predated the gather.
The body writes the turnstile with a space and my search used the closed form. A
false retraction removes real worked mathematics from the corpus's reach, and it
arrives wearing the credibility of self-correction, which makes it the LESS likely of
the two errors to be checked. Absence needs the same standard as presence.


5. THE PACE, STATED SO YOU DO NOT OPTIMISE IT AWAY

ONE PAPER PER TURN. Seventeen papers per field, six fields.

Daryl asked me directly whether the infrastructure had made this faster than when he
ran it with node 58, and the answer is that it made two things cheap and the reading
no cheaper at all. reach_baseline.py made the measurement instant, and it earned that
immediately - "Lax" reads x112 raw across fifteen papers, which would have been the
integrable field's largest apparent footprint, and x0 word-bounded, the raw hits being
\Lambda splitting under the search. The \ldg rail removed the landing lag, which is an
entire campaign's worth of work. Neither touched the reading.

A read that sharpens a QUESTION rather than producing a claim is a legitimate outcome.
Record it as a question. I4 in the integrable ledger is one: P11 carries two conserved
quantities, names them with two different words, and never asks whether its sector is
integrable in Liouville's sense; P10 then scoped it, because the radial lift is one
degree of freedom with one integral and so trivially integrable, and the question has
content only on the layer's true degrees of freedom, which P10 defines and does not
count. That is not a finding and writing it up as one is how a ledger acquires the
manufactured landings this campaign spent twenty turns removing.

Three of the four papers I read owed NOTHING. That is the expected shape. A field that
finds a debt in every paper has been read to a template.


6. WHAT COMES BACK, PER FIELD

The ledger with its R0, its probes, its three registers, its lead register, its
seventeen-row reading table, and its landing table written AS IT GOES rather than
after. The registry row. The \ldg markers, in the same commits as their substance.
The one-line registration in corpus/field_survey.py. Report the DEPTH number beside
the coverage number, and say plainly which papers were checked and found negative.

Run bash scripts/sweep_gates.sh before each push. It is specified - NODE=ci, 420s -
and it reports a delta against a baseline ref, which is the only number that says
whether your work broke anything. It sits at 94 pass, 0 fail, 1 unrun.
