# When a quotation check owes a repair

This is the test a reader applies to one row of `corpus/quote_pin_baseline.tsv` to decide whether the
row is `REPAIR-OWED`. It is written to be applied, not argued: each step asks a question about the
quoted text and about the check that quotes it, and each question has an answer that can be found by
looking, counting or searching, without judging how well the quoted text reads.

Its last section says what a repair writes once a row is owed.

## What the words mean here

- **The receipt** is the Python file that makes the check.
- **The quoted text** is the literal the row records: a string the receipt requires to be present (or
  absent) in some file.
- **The site** is the place in that file where the quoted text is found. Reading the site is part of
  applying this rule, whatever file it is in; a row whose site cannot be read is not decided by it.
- **The claim** is what the receipt says the presence of the quoted text shows. It is read from the
  receipt itself: the label of the check, the comment beside it, or the paragraph of the docstring the
  check belongs to. The claim is the receipt's, never the reader's.
- **A live file** is one the corpus goes on editing: a paper, a register, a gate or other tool. **A
  fixed record** is one whose quoted line has never changed: another receipt's text, a commit message,
  a file read at a named commit.
- **Never changed** is measured on the quoted text, not on the physical line it sits on, because a
  paper keeps a whole paragraph on one line: the quoted text has never changed when the number of times
  it occurs in the file has changed once in the whole history — when it arrived — and never since.

## The order of the questions

Ask them in this order and stop at the first that decides.

When several checks quote the same text in the same file, they share one row. Apply the questions to each
check separately, then give the row the first of these that any check reached: `REPAIR-OWED`, then
`MEANING-HELD`, then `DELIBERATE`, then `NOT-A-PIN`. A quotation is one pin however many checks use it:
the repair is owed if any use of it owes one, and the row is exempt only when every use is.

### 1. Is it a quotation at all?

The row is `NOT-A-PIN` when the quoted text plays one of these roles in the check, and only then:

- a pattern that finds a structure — a heading, a label, a row marker, the next section;
- a pattern that reads a number or a field out of a log or a tool's output;
- a string the receipt checks in the *output* a tool returns or prints when the receipt runs it.

The question is the quoted text's role, not what it looks like. Any text the check requires to be present
or absent in a file — prose, a heading, a check label, a function name, a line of code — is a quotation
and goes on to step 2.

### 2. Is it a fixed record, quoted as itself?

The row is `DELIBERATE` when the quoted text is one of these, and the claim is only that this text
stands where it stands:

- **a quoted line that has never changed** in the full history, in a fixed record or in a live file;
- **a name or a value used as data**: a label, an identifier, a number, a formula, a glyph, where the
  claim is that the name or value is present (not what it means elsewhere);
- **a live tool's own words, when the claim is about the words**: the check says the text was *left
  untouched*, *recorded in place* or *withdrawn in place* — then the unchanged text is exactly the claim.
  When the check says a file *states*, *says*, *prints* or *records* something, the claim is about what is
  stated, and step 2 reaches the quotation only when it is the whole of that statement: a complete clause,
  or the complete heading or label the claim names. A quotation that is part of the statement goes on to
  step 3.

This exemption belongs to a *line*. A token that occurs on several lines, or whose count in the file has
changed, quotes no single line, and step 2 does not reach it; go on to step 3.

When one check requires several quoted pieces, read its claim before step 2. If the claim says something
about the pieces together — that they are beside each other, that between them they state one thing, that
one cites the other — step 2 reaches none of them, and Test 5 decides. Step 2 reaches a piece only when the
claim says something about that piece on its own.

### 3. The seven tests. If any answer is yes, the row is `REPAIR-OWED`.

**Test 1 — The quotation leaves out its subject, a condition, or a negation.**
Read the words around the quotation in its own sentence. The repair is owed when one of these three sits
outside the quotation:

- **its subject** — the quotation begins after the subject of its main verb, so the quoted words do not
  say what they are about ("…has not failed to empty", "admits rather than forces a quantum structure");
- **a condition the quoted statement depends on** — words that restrict when, where, or under what
  assumption the statement holds, introduced by *if, when, unless, provided, only, given, with, for, on,
  under, at, in the case of*, or a list of premises of which the quotation keeps only some, such that the
  quoted words read alone state something the sentence does not ("on the identification used here" is
  such a condition) ("a degeneracy growing as $n^2$, the shell
  contribution goes as $n^3$", which drops the other two inputs that give $n^3$);
- **a negation that governs the quoted words** — *not, no, never, nor, without*, or a frame such as
  "what is not claimed is", so that the quotation read alone asserts what the sentence denies ("a
  closed-form nonlinear solution", from "what is *not* claimed is a closed-form nonlinear solution").

Nothing else outside the quotation makes the repair owed under this test. That the sentence goes on to say
more, or that the receipt's claim is broader than the quoted words, is not a ground here.

**Test 2 — The quoted text points somewhere else for what it is about.**
The repair is owed when the subject or the object of any clause in the quotation — the main clause or a
clause inside it — is one of these words, or carries one as its possessive (*its* leaves, *their* rate),
standing for something named outside the quotation:

- a pronoun: *it, they, them, its, their, we* when it stands for something named earlier;
- a demonstrative: *this, that, these, those, such*, alone or before a noun ("this row", "these
  structures");
- a quantifier standing for a set named earlier: *all, both, each, either, neither, the one, the other,
  the former, the latter, all three*;
- a noun phrase carrying a pointing word: *the same, the above, the said, the aforementioned, the
  remaining, the rest*.

**A noun phrase that begins with "the" and names its thing in its own words does not owe the repair**
("the degeneracy is $2(n-1)(n+3)$", "the propagating sector is ghost-free to all orders"). The reason:
such a phrase tells the reader what kind of thing the sentence is about without looking back, and the
papers write almost every sentence this way; counting it would mark nearly every quoted sentence owed and
leave the class unable to separate anything. Which particular thing is meant is not asked here: if the quotation
leaves out its subject, a condition or a negation, Test 1 asks it, and otherwise the noun names enough.

A **head noun that names nothing by itself** is treated as a pointer, because it carries no content of its
own: *the result, the consequence, the conclusion, the outcome, the claim, the statement, the fact, the
case, the quantity, the point, the question, the answer, the argument, the finding* — when that word is the
subject and nothing in the quotation says which one. This list is closed: a head noun not on it names its
thing, and does not owe the repair under this paragraph.

The authorial *we* ("We claim no construction here") stands for the authors and points at nothing in the
text; it does not owe the repair.

**Test 3 — A phrase in a live tool stands in for what the tool does, and the check does not run the
tool.**
The claim says the tool *refuses, runs, reads, suppresses, fails, flags, calls* — something it does — and
the check only finds a word, a function name or a line of the tool's code. The repair is owed. It is not
owed when the same check also exercises the behaviour directly (runs the tool, calls the function, seeds a
case), because then the quoted text is not standing in for anything. It is not owed when the claim is
about the tool's words themselves (step 2).

**Test 4 — The quoted text can be found where the claim is not about.**
Count and locate. The repair is owed when:

- the quoted text occurs more than once in the file and the claim concerns one place;
- its count in the file has changed over the history, so no single line is quoted;
- its only occurrence is somewhere the claim does not concern (an error message, a comment, another row);
- the claim is about one row or one section and the check searches the whole file.

When the claim is only that the value is *used* in the file, one occurrence carries it, and Test 4 does not
apply.

**Test 5 — Two or more pieces are required together and nothing joins them.**
The check requires several quoted pieces in one file, and they could sit in unrelated paragraphs while the
check still passes; or the claim needs all of them and the check accepts any one — a disjunction cannot
carry a conjunction. The repair is owed on every piece, including a piece that would be a name or a value
on its own: half of a joint requirement does not carry the claim.

**Test 6 — A choice between alternatives, where the weaker one decides alone.**
The check accepts *this or that*, and one of the alternatives is true for a reason unrelated to the claim
(a bare label, a common word) or can never be true (it matches nothing in the file and never has). The
repair is owed.

**Test 7 — A guard that passes on nothing.**
The check asserts an absence, a count or a comparison over something that may not have been read: a
default empty value when a file is missing, an empty list, an input that is never confirmed present. The
repair is owed.

### 4. Otherwise

When no test is met:

- a complete sentence or clause that names its own subject and carries the claim is `MEANING-HELD`, and
  the row must name the commit at which it holds; a phrase without a verb that names both of its terms
  ("the one non-generic exception, the Nariai branch") counts as a clause here;
- a name, value or unchanged line not already settled in step 2 is `DELIBERATE`;
- anything else — a fragment that is neither a clause nor a name or value, on a line that has changed — is
  `REPAIR-OWED`, recorded as decided at step 4: it asserts nothing on its own, so there is no meaning for it
  to hold.

## The border with `ENCODING-OK`

**Not written here.** When the same thing is written in two notations — `\nu_R`, `nu_R`, `nu_{R}` — this
rule does not say whether a pin that accepts several spellings is owed a repair or is a matter of encoding.
That border belongs to node `60`, which has made the calls on it, and is ordered there. It takes only the
spelling arms: whether accepting several spellings of one thing is itself a defect. Every other arm of the
same check, and the check as a whole, still goes through steps 1 to 4, and a test met there decides the
row. A row is left undecided by this rule only when nothing but its spelling arms is in question.

## What a reader records

For every row decided `REPAIR-OWED`, record which test decided it (1 to 7) and the site detail that met it:
the words left outside, the pointing word, the count, the arm that decides alone, or "step 4". A verdict without its
test cannot be checked by the next reader.

## What a repair writes

This section governs repairs. It says what a repair writes in place of an owed quotation; it is not a
test applied to quotations already standing, which steps 1 to 4 decide.

A repair either withdraws the check, with its case written down, or replaces the owed quotation with a new
pin. The new pin is one span of the site, or several spans required together inside one locus, and it meets
both of these floors.

1. **It carries the whole claim.** Every part of what the check asserts is in the pin: the subject, any
   quantifier, the object named, and any condition or negation Test 1 would find outside it. A pin that
   leaves part of the claim out lets the check pass on the wording's presence instead of the claim's, which
   is the defect being repaired. A single span is therefore a whole clause, never a fragment, and read alone
   it would reach `MEANING-HELD` or `DELIBERATE` under steps 1 to 4. Several spans carry the claim when,
   read together inside their locus, they state it.
2. **It finds one place.** Counts are taken the way the checker compares: whitespace collapsed, emphasis
   commands unwrapped, `$` deleted, `~` read as a space. A single span must occur exactly once in the file
   it is checked against. Several spans meet the floor when:
   - one of them, **the anchor**, occurs exactly once;
   - every other span is required **within the anchor's locus** — the sentence that contains the anchor,
     or a smaller unit the check names, such as a row;
   - the check requires exactly one locus to hold them all.

   The other spans need not occur once on their own: a value or a word that stands many times in the paper
   is located by the anchor beside it. Required anywhere in the file, they would not be joined at all, and
   Test 5 would owe the repair again. A pin none of whose spans occurs once has nothing to locate it, and
   does not meet this floor however its pieces are arranged.

   The floor does not apply when the file is read at a named commit. What it prevents is a later edit
   landing the pin on the wrong place, and a file read at a fixed commit has no later edits.

The normaliser only merges texts, never separates them, so a count can rise under normalisation and never
fall: a raw count is a lower bound on the count this floor is tested against. Every count under this floor
is taken normalised.

The floor is stated through the locus, not through the length or kind of span, because neither predicts
uniqueness. A number the paper states once is unique at five characters; a prose word the paper uses
throughout is not unique at any length it has. What separates them is whether the span is what the claim
says or what the claim is about, and the checker cannot see that difference. The locus lets a pin require
the thing the claim is about without requiring that thing to occur once.

**Then stop.** Words beyond what the floors require add no protection. Each is something a later edit may
change without changing the claim, and when one is changed the check fails in a receipt whose claim still
holds: a new owed row made by the repair. So among pins that meet both floors **and that the quote-pin check
(`corpus/check_quote_pins.py`) can key as pins**, the repair takes the one with the fewest pinned
characters, counted over all its spans. A single span is never a sentence and a half.

A pin the check cannot key is not a cheaper pin; it is not among the pins this ranks. A repair the ledger
cannot see is one no later reader is sent to check, so its shortness buys nothing. This is not a temporary
restriction to be lifted by hand: the pins ranked are whatever the check can key, so when the check learns
to key a new form — a locus-scoped conjunction, say — that form joins the ranking and is preferred wherever
it is shorter, with no change to this rule.
