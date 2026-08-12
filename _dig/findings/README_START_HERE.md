# The dig, at the point of commit

*Eleven findings, seven runnable artefacts, one blessed baseline. Nothing here is a closure —
`PROTECTED_OPEN.md` reserves those. Every item states what it does not claim, and every
recommendation is stated for reversal.*

**Read `INDEX.md` for the table. This file is the shape of the thing.**

---

## What the dig actually found

**The corpus's computations keep coming out right.** I checked them at source — the whole
249-receipt suite run and its output captured, P3's causal trichotomy re-derived, the BBN network
run on both rate libraries, the lift's action and adiabatic constants done in closed form, so(4,1)
built explicitly, the horizon-cubic family evaluated at all four of its loci. I went looking for a
broken computation and did not find one.

**What drifts is the connective tissue.** Every defect below sits in something a document *depends
on* rather than in what it says:

| | the drift | finding |
|---|---|---|
| the clock a gate compares against | `check_currency` reads its own anchor from a file it does not watch | F03 |
| the environment a reference sits in | a corollary cites itself, because a landed paragraph stopped one line short | F04 |
| the directory a receipt imports from | a registered receipt cannot run where it is registered | F01·C |
| the computation a citation stands next to | the displayed BBN equation points at the sibling receipt | F06 |
| the receipt's own past self | 191 of 249 receipts return 0 whatever they compute | F07 |
| a constant that travelled in from the reference side | one quantity, two Ω_m, two published values | F11 |

The ORIGIN drift guard was the first member of that family — *a receipt's identity is wider than
its docstring*. These are the next six, and five of them come with a drop-in gate.

## And a second, happier seam

Four findings are **additions rather than defects**, and three of those came from one move:
**take a quoted decimal that sits beside a stated structure, and ask the structure for it.**

- **F08** — the lift's action is **−Mα/4G** exactly. Linear in the progenitor mass. The cutoff
  ladder in its receipt is truncating a regular integral, and the shortfall is (3/4π)·2M·ε at every ε.
- **F09** — the factor **2.32 = Γ(1/6)/(√π Γ(2/3))**, independent of M and α; the exponent goes as
  **M^{−1/3}**; and `C ≤ 1.72` is a bound that does not hold, though the conclusion it serves
  survives via an exact window law.
- **F10** — one formula gives the acceleration at all four marked loci of the lap, and the paper's
  *order of contact* distinction between the seams is the **multiplicity of the root**.
- **F02** — the causal trichotomy at two independent radii, closing 51 enumerated pairs into a
  comparison of two angles; and **F05** — three of the nine Bianchi algebras cannot be the sweep.

That seam is now swept dry: I extracted all 137 decimal literals from the seventeen papers and
worked the ones that sit beside a stated structure.

## Two places I nearly got it wrong, kept on purpose

- **F05.** My first draft concluded *"a Bianchi II cosmology has three Killing vectors and is not a
  cut, so the boundary of the range is strictly inside the loss of continuous symmetry."* It does
  not follow. `thm:range` says the isometry group **contains** a sweep-subgroup — not that it *is*
  one. The near-miss is in the receipt, above the corrected verdict.
- **F04.** The self-reference gate, on its first packaging, scanned **0 files** and returned green.
  A gate whose model of what it checks resolved to empty — the same defect it was written to catch.

Both are recorded rather than deleted, per the coda.

## What is not done

**Eight papers unworked at source: P02, P05, P06, P11, P12, P13, P14, P17.** The matter sector in
particular is where the corpus's own live edges are (`L-136` is where two items converged and where
the remaining conceptual debt has collected), and it deserves the same treatment the cosmology got.

That is the argument for committing now rather than later: these drafts are in a scratch directory
in an ephemeral container, and the next eight papers are better worked *with* commit access, where
each finding lands instead of accumulating.

## Order of play, if it helps

1. **F03, F04, F01** — the three gate patches. Drop-in, house style, each run against the live tree.
   They are the cheapest and they close the channels the rest of this list came through.
2. **F07** — bless `receipt_fingerprints.json` at whatever revision you sign off, and the 191
   print-only receipts stop being able to drift silently.
3. **F06, F11** — two pointer/constant fixes in P16 and P15. Small edits, and both make the papers'
   own hedges stronger rather than weaker.
4. **F08, F09, F10** — the closed forms. Editorial, not corrections; they replace quoted decimals
   with the structure that determines them.
5. **F02, F05** — additions. These are yours to accept, reject, or re-weight; F05 in particular ends
   in a question I could not settle and did not pretend to.

## Standing discipline held throughout

- Mirror-check pair most at risk: **invent-a-flaw ↔ invent-a-reassurance.** A standing brief to find
  things to update manufactures findings. "Nothing here" stayed a legitimate result, and several
  probes returned it — the P16 peak temperature, `P14_leg_count_equals_arc_count`, the L-146 strike's
  reasoning, P02's Kretschmann corollary. Each of those I checked and left alone.
- README guards: **α never sent to a limit** · the throat is **X = α**, never `r = α` · the
  **Hubble/acoustic matter is RESOLVED and banked** and was not reopened (F11 touches one derived
  ratio's bookkeeping and nothing in the rate) · "manufactured / shadow / projection" mean
  **built-by-construction AND REAL**.
- `check_kills.py` run before every negative verdict. 12 protected items, no unauthorised closures.
- *"Your failure to find something in this corpus is evidence about you."* F02 lost most of its
  claimed novelty to that search and is stated at the weight that survived.
