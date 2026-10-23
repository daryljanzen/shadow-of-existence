# The census, refreshed at r7577 (69)

`items_keyed.tsv` here replaces the r7371 census as what `check_open_item_coherence` reads.

**How it was read.** The net is `net.py`: 69's r7371 `extract.py`, unchanged (the papers, the openness pattern, the
body extraction, the marker-sentence rule), factored out so the gate and the census extract the same candidates. Run on
the papers as they stand at r7577 it catches 240 candidates. The key is `(paper, marker sentence)`, as `KEY.md` in
`r7371_cc66_the_coherence_key/` names it: a sentence unchanged since r7371 keeps 69's r7371 reading, because the key
says an unchanged statement is the statement that was read. Every other candidate was read again: the ones new or
reworded since r7371, and every one r7371 had classed OPEN, CHECK or STALE, against the stride's 29 rulings
(`THE_COHERENCE_STRIDE.tsv`).

**The classes.** `OPEN`: the paper states the item open, and the register column names the live row that carries it.
`LIMIT`: an r7013 kind-② stated limit, a boundary, a decline or a weight marker, which `PO-86`'s r7451 clause says the
register must not row; the note names the ground, usually a stride ruling. `NOT-OPEN`: the net caught a word and
nothing is stated open. `POINTER`: the sentence points to where an item is carried. `DECLARED-NOT-OWED`: r7371's
class, kept.

**What the read found.** Seven defects in the papers, each fixed at r7577 in its own paper: `P15`'s conclusion
calling the crossing's dynamics "the debt" against its own sec:scope, and handing $\rho_r/\rho_m$ over as a datum
against `P17` sec:frontiers, with the owed pointer at sec:throat added; `P18` leaving open whether the two $A_2$s
coincide by accident against `P5` rem:a2-distinct, and pointing to a sixteenth Weyl fermion its frontier does not
carry; `P7` asking for a derivation of an onset that no longer exists; `P6` calling the matter sector an open edge;
`P1` sending its ultraviolet question to companions that do not carry it. And one item no row carried: `P14`'s
quantised fermion field, now `PO-95`.

**Keeping it current.** The gate fails on any candidate this file has not read and on any row whose sentence is gone.
Add a row by reading the sentence, never by copying a neighbour's class.
