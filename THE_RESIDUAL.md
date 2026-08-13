---
name: the-residual
kind: PLAN
current: r2593+c54.207
description: THE RESIDUAL — the true state of remaining doubt across the corpus, measured from the papers' own epistemic self-declarations rather than from the registers. Eighty-four qualifications, sorted by whether a proof is discoverable. Written r2592.
sources: [chat]
---

# THE RESIDUAL

> ***`THE_STATE` counted fourteen things from the REGISTERS. This counts from the PAPERS — every place the
> corpus itself says a thing is not settled — and it finds **eighty-four self-declared epistemic
> qualifications**.***
>
> ⌗ *The registers hold what someone routed. **The papers hold what the physics actually owes**, and the
> two are not the same list.*

## ⌗ THE MEASUREMENT

| class | count | papers |
|---|---|---|
| **CONJECTURE / hypothesis** | 36 | 6 |
| **OPEN / remains open** | 27 | 11 |
| **NOT CLAIMED** — explicit declinations | 10 | 7 |
| **stated AT A WEIGHT** | 6 | 5 |
| **TRACED, not computed** | 2 | 1 |
| **INHERITED, not derived** | 2 | 2 |
| **RECALLED, not derived** | 1 | 1 |

⇒ ***84 across the corpus. But the classes are not equally load-bearing, and sorting them is the work.***

---

# 0 · ⛭⛭⛭ THE LEDGER — r2593, and this is what was missing

**⌗ THE FAILURE DARYL NAMED, EXACTLY.** *This line kept discovering that a thing which looked open was not — and
kept **failing to record the verdict**, so the same reading had to be redone every time anyone asked what was left.*
⇒ ***A grep is not a list of what is owed. It is a list of places to look, and the looking has to be written down or
it does not count.***

**✔ `corpus/open_ledger.txt`** — *one line per **distinct** qualification in the paper bodies, with a **verdict**.
**123 raw hits deduplicate to 113 sentences.***

| verdict | n | meaning |
|---|---|---|
| **UNVERDICTED** | ***66*** | ***not yet read — the ONLY bucket that means work*** |
| **DO-NOT-ASSERT** | 18 | a deliberate marked holding; **nothing owed** |
| **SCOPE-BY-DESIGN** | 8 | the paper declining a claim outside its scope; **nothing owed** |
| **METHOD-PROSE** | 5 | prose about how the corpus marks maturity; **not a claim** |
| **REGISTERED** | 5 | a real gap already carried by a `PROTECTED_OPEN` item |
| **STANDARD-PHYSICS** | 3 | someone **else's** open problem; **not CR's debt** |
| **OPEN-DOWNSTREAM** | 3 | open, and downstream of something else open |
| **SELF-ANSWERED** | 2 | ***the next sentence closes it — the class that misled this line five times*** |
| **NAMED-UNBUILT** | 2 | ***a real construction, named and not built — genuinely owed*** |
| **PRECISION** | 1 | the computation exists; its last-percent accuracy does not |

**✔ AND `corpus/check_open_ledger.py`, wired and seeded, checks three things:**
*⓵ every ledger entry still exists in a paper — **an entry whose sentence is gone means the corpus moved and the
ledger did not**; ⓶ **every qualification in the papers is in the ledger** — a new one nobody verdicted **fails the
turn**; ⓷ `--rebuild` re-derives while **preserving existing verdicts**, so verdicting is the only direction the
file moves.*
⚠ ***It does not check that a verdict is CORRECT — that is a reading, and no gate can do it. What it guarantees is
that every qualification HAS one and that none appears without being seen.***

⇒⇒ ***So the answer to "what IS residual" is now a file rather than a re-derivation, and the 66 UNVERDICTED are the
honest remaining work — not the 123, and not the 84.***

---

# I · WHAT IS NOT CR# I · WHAT IS NOT CR's DOUBT AT ALL

**⌗ MOST OF THE 36 "CONJECTURE" HITS ARE THE CORPUS DESCRIBING *STANDARD PHYSICS'* CONJECTURES**, *not its
own: **cosmic censorship** ("Penrose's conjecture … pursued through partial theorems and
counterexample-hunting rather than proof"), **chronology protection** ("Hawking's … a proposal about
physics the classical theory does not contain, and unproven"), and the recurring synthesis phrase
**"dissolution by identity, not management by conjecture."***
⇒ ***These are the corpus's ARGUMENT, not its debt. They belong in the residual only as the thing the
framework claims to have removed.***

---

# II · CR's OWN CONJECTURES — **four, and each names its open step**

**⓵ THE GENERATION CONJECTURE** *(p0, marked **do-not-assert**).* ⛔ ***AND READING PAST THE SENTENCE
CORRECTS THIS ENTRY, r2592.*** *p0 names "the one open step---the conjecture proper---is the **descent**:
whether three **vantages** of the one substrate are the three physical **generations** a single observer
sees."* ⇒ ***And the next sentence says: "That construction is built~`\cite{JanzenMatter}`."***

*A spinor on the slicing structure **binds exactly one chiral zero-mode at each throat wall as a bound mode
of the existent leaf** — normalizable in the leaf's proper measure where the propagating Dirac-norm mode is
not — its chirality the parity $R=\gamma^5$; and the maximally-symmetric construction **places a wall at
each of the three hinges**. ⇒ ***The count is three, the $S_3$ permuting the walls is the family symmetry,
and for the discrete flavour structure "the physical identification is therefore a RESULT, forced WITHIN
CR".***

⇒⇒ **SO WHAT ACTUALLY STAYS OPEN IS NARROWER AND p0 STATES IT EXACTLY:** ***"the full PROPAGATING spinor
field sector (the built modes being leaf-bound, not the propagating theory)"*** *— with the gauge content
walled and the mass spectrum the ordinary route.*
⚠ ***My first draft of this file called the descent "the single most precisely-bounded open question in the
corpus". It is closed. The open thing is the propagating sector, which is a different and larger object —
and this is the fifth time this session that reading one sentence further changed the finding.***

**⓶ THE FINE-TUNING CONJECTURE** *(p0, "stated here as the hypothesis it is, to be grounded through the
matter sector").* *"the one scale dissolves the two deepest fine-tuning problems of cosmology at once."*
⇒ *r2564 and c54.207's `L-532` between them showed the two $10^{122}$s are **one dimensionless combination
differing by $3/8$** — so **half the conjecture's content is now arithmetic**. What remains is the
grounding.*

**⓷ THE $P13/P14$ CONJECTURE** — *"the conjugation of charge and the discrete residue of matter are one
structure read two ways", carried at the matter-sector seam.*

**⓸ THE DIMENSION CONJECTURE** — *"the dimension of the **cut**, not of the substrate, on which every
constraint the framework states remains a lower bound."*
⇒ ⛭ ***This one has MOVED and the register should say so: `L-533` (c54.207) showed Rule 2 EMPTIES a second
slicing step, making CUT→SUBSTRATE a consequence rather than a rule of conduct, and `kills/PO-9.md`
narrows what remains to three unreproduced links.***

---

# III · THE TEN EXPLICIT DECLINATIONS — **and three name a discoverable proof**

⛭ **⓵ THE $\{0,1,2\}$ DERIVATION** *(P4).* *"no derivation producing $\{0,1,2\}$ from a single condition
has been exhibited, and the audit's verdict on that claim is accordingly open."*
⇒ ***A formal statement, absent, and its absence is what holds the claim open. This is a proof someone
could find.***

⛭ **⓶ THE MULTIPLICITY** *(P14).* *"the angular decomposition does not supply multiplicity, since
$\lambda=j+\tfrac12$"* — **a negative result that constrains what a construction must supply**, with "we
claim no construction here" beside it.
⇒ ***`PO-5`'s mod-2 index (r2568) is the live candidate for exactly this gap.***

⛭ **⓷ THE MISSING SECTOR'S IDENTIFICATION** *(P7).* *"We claim no derivation here and record only the
identification: the eager target of this item and the walled route of the matter sector **are not separate
debts**."*
⇒ ***An identification without a derivation — and identifying two debts as one is itself the kind of
result a proof could confirm.***

**⌗ THE OTHER SEVEN ARE SCOPE, NOT GAPS**, *and they are the corpus at its best:* *"the horizon-thermodynamic
apparatus … has on a finite layer no realised horizon to be defined on"* (twice, P1 and P7, **declining a
claim it could have made**) · *"nothing here bears on why the cosmological reassignment selects the
degenerate member"* (P3) · *"We claim no novelty in the mechanism"* (P10, on Brown–Kuchař) · *"We do not
claim these programmes are internally flawed"* (P10) · *"we do not claim that the question is closed"*
(P14) · *"they do not entail it as a theorem entails a corollary, and we do not claim more"* (P8).

---

# IV · THE WEIGHT-MARKED AND TRACED ITEMS — **where a computation would upgrade a statement**

*· **TRACED, not computed** (P14): *"Index-theoretic stability under deformations preserving the
three-wall structure is the expected behaviour of such a graded count and is **traced rather than
computed** here … and marks the Atiyah--Singer statement on the branched bead as **traced**."*
⇒ ⛭ ***That is a named, bounded computation. It is also exactly where r2568 found the mod-2 index
question — so ONE calculation may serve both.***
*· **RECALLED, not derived** (P15): the lensing figure the construction's own $\Phi$ matches is *"recalled
rather than derived here, so what is established is internal consistency"*.*
*· **INHERITED, not derived**: the handover datum and the progenitor spectrum, which *"may remain measured
boundary data at no cost to the synthesis"* — ***a declination that is a positive claim about what the
framework needs.***

---

# V · THE SIZE OF THE RESIDUAL, HONESTLY

**⌗ OF 84 QUALIFICATIONS:**
*· ***~36 are about standard physics***, not CR's debt;*
*· ***7 declinations are SCOPE***, correctly stated and needing nothing;*
*· ***4 are CR's own conjectures***, each with its open step named — and ***two have MOVED and one is CLOSED***: the generation conjecture's descent is **built**, leaving the propagating sector;*
*· ***3 declinations name a discoverable proof*** — the $\{0,1,2\}$ derivation, the multiplicity, the
identification of two debts as one;*
*· ***3 are weight-marked items a computation would upgrade*** — the traced index statement chief among
them;*
*· *the remaining ~27 "open/remains" hits are the frontier items the registers already carry.*

⇒⇒ ***So the true residual of DISCOVERABLE work — a proof or computation that exists to be found and would
close a stated gap — is about FIVE items, and three converge on one object: the $\mathbb{Z}_2$-graded
index. `PO-5`'s mod-2 route (r2568), P14's traced Atiyah--Singer statement, and P14's multiplicity gap are
the same question asked three ways.***

⌗ ***And the largest genuinely open thing is not on any register: p0's "full PROPAGATING spinor field
sector", the built modes being leaf-bound. That is a sector, not a lemma.***

⚠ **AND THE HONEST CAVEAT.** *This is a keyword measurement of eight phrase-classes, and **the corpus's
epistemic vocabulary is richer than eight phrases**. ⇒ ***The count is a floor, not a total*** — and the
same caution that has been earned four times this session applies: **a general classifier over prose
finds what it was told to look for.***

*Written r2592. Stated for reversal.*
