# r7704 (60) — REGISTRATION: the two landed fixes in place, and P2's `prop:cycloid` against 71's scope flag

**Order answered:** `r7701` (69), items 1 and 2.

**Registered before measurement**, in its own commit, pushed before `probe.py` exists. At the
moment of writing, **`corpus/janzen_circle_v3.tex` is UNOPENED** beyond two `grep -n` hits that
locate `prop:cycloid`'s `\begin{proposition}` line and one citing line, and its own line count
(659). Nothing of the proposition's statement, its proof, or any citing sentence has been read.
The two P15 sites of item 1 have been located by `grep -n` and not yet read.

**THE TREE: `84fb2b59`** (`origin/main` = this branch's HEAD, `r7701`).

**Why this one is worth registering carefully.** Item 2 is the first read this seat has been given
where **another seat has already named the defect** — 71 flags that the proposition holds only for
the `E = 0` radial geodesic while a general `E` gives amplitude `2M/(1 − E²)`. A probe built after
a flag is the easiest probe in the world to build so that it confirms the flag. So the arms below
are written to be able to come back **NO SCOPE ERROR**, and the negative probes are the ones that
make that answer reachable rather than polite.

---

## ITEM 1 — the two landed fixes, and cross-site agreement

**1a — `l.2612`'s repaired row.** `r7701` says the site now reads "the quadrupole rewards this
cosmology (−2.6 …), the octopole penalises it at +0.9, and the largest single-multipole penalty is
the +2.2 at ℓ = 4". The comparison: each figure against the depth-gap receipt's `r7697` gates,
which pin the arm A `(L)` terms two-sided at `6e-3`. *Reachable negatives:* a figure landed at the
wrong place (a transposition); the fourth term (`+1.1` at `ℓ=5`) is still missing where the
sentence's structure wants it; the structural claim and the digits now disagree (the largest is no
longer at `ℓ=4`).

**1b — THE ORDER'S OWN CHECK: `l.2903`'s row against `l.2612`'s, so the sector's per-multipole
figures agree at EVERY site.** This is a cross-site identity, and the instrument must compare the
same quantity site by site rather than ask each site whether it prints current numbers — the
`r7702` lesson, which is what found the half-re-pointed site in the first place. *Reachable
negatives:* the two sites print different values for one multipole; one prints a two-place form
that rounds differently from the other's three-place form; a third site prints the row and was
missed by both.

**1c — the doubled-opacity clause, branch (b) as landed.** The clause now reads "and the
hierarchy's depths, swept on the control's background, do not move under a doubled opacity grid,
…". The comparison: does the clause as written now name the build its convergence was measured on,
and is that build the one the receipt's knob sweeps use? *Reachable negatives:* the wording names a
build the sweeps do not use; it still attaches the convergence to the `(L)` agreement; it names the
build but drops which quantity was swept.

---

## ITEM 2 — `prop:cycloid`, read for scope

**2a — the proposition's own statement.** Read `\begin{proposition}[Lemaître–Tolman cycloid
form]` through `\end{proposition}`, one hypothesis per reading. Does it carry `E = 0`, a marginal /
parabolic condition, "released from rest", "zero binding energy", or any equivalent — or is it
stated for a general radial geodesic? *Reachable negatives:* the restriction is stated **in the
hypothesis** (⇒ NO SCOPE ERROR in the statement); it is stated only in the **proof**; it is implied
by a definition the proposition inherits from its section (⇒ reported with that definition quoted);
it is absent everywhere (⇒ the flag holds for the statement).

**2b — the amplitude.** 71's flag gives `2M/(1 − E²)` for general `E`, against `2M` at `E = 0`.
Read what amplitude the proposition and its proof actually write. *Reachable negatives:* the
proposition writes `2M` with no `E` in sight; it writes a general amplitude and the flag is about a
different object; it writes `M(1 + cos η)`-type parametric forms whose amplitude is implicit (⇒
reported as implicit, with the expression quoted).

**2c — EVERY sentence that cites it.** A proposition can be correctly scoped and still be
**used** out of scope — this seat's `r7696` lesson that a sentence reasoning from a premise is a
claim about that premise. Each citing site is read for whether its own context supplies `E = 0`.
*Reachable negatives:* a citing sentence reads as general where the proposition is restricted (⇒ a
red, routed with its words); every citing sentence is inside an `E = 0` context (⇒ nothing owed);
a citing sentence is about the proof's method rather than its conclusion (⇒ reported as such).

**2d — THE ORDER'S QUESTION, answered in its own terms: does P2 state the restriction or read as
general?** This arm is the verdict and must be able to answer either way. It is computed from 2a
and 2c and from nothing else — no verdict note in this revision is a sentence written ahead of its
readings.

**2e — the flag itself, checked rather than accepted.** `2M/(1 − E²)` is a claim about the
Lemaître–Tolman solution, and this seat can check the `E = 0` limit of whatever the paper writes
without re-deriving the general case: at `E = 0` the general amplitude must reduce to what the
proposition states. *Reachable negatives:* the paper's amplitude does NOT reduce to the flag's
`E = 0` limit (⇒ either the flag or the paper is wrong about the same object, and that is a fork
for 69, not a conclusion for this seat); it reduces exactly (⇒ the flag and the paper agree at
`E = 0`, which is what makes the scope question the only question).

---

## The instrument

`probe.py`, to the six guard families (G1 one predicate per conjunct; G2 three anchor forms only
with ONE leading backslash for a control sequence, unanchored markers REFUSED; G3 the flip family;
G4 classifiers tested on both classes; G5 reader probes each with its negative; G6 every prose
probe on a whitespace-FLATTENED copy). Sixteen negative probes carried.

**A seventeenth is registered here, and it is this revision's own guard:** *when another seat has
already named the defect, the probe must be able to return NO DEFECT FOUND, and that answer must
be reachable by a reading rather than by the probe failing to look* — so the scope reader is tested
on an injected `E = 0` hypothesis (it must then report the restriction PRESENT) **and** on an
injected general-`E` statement (it must then report it ABSENT). A probe that cannot distinguish
those two is answering about the flag and not about the paper.

Exit `0` with every verdict printed is the only accepted outcome; a verdict the probe cannot
compute prints UNMEASURED; an arm whose verdict would read backwards carries its own label.
