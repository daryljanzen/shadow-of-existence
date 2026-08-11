# Cosmological Relativity corpus — bundle r1407

Complete working snapshot of the CR corpus at revision r1407. The 17-paper corpus (P1–P16 + p0/17) is
build-complete and self-knowing, and as of the **r1406 finish-line** it is **fully swept** (the eleven-avenue
per-paper treatment across all 17) and **receipt-cited end to end**: every load-bearing computed claim carries
an inline `\rcpt` marker resolving to a generated *Appendix R* in its paper, backed by the curated `receipts/`
tree — source of truth `receipts/INDEX.md`, generator `corpus/make_receipt_appendix.py`, rendering package
`corpus/receipts.sty`. All appendix entries are **[OK]**, the receipts were exhaustively validated, and all 17
papers compile (355pp). r1407 is the metadoc-reconciliation cut over the r1406 corpus — the orientation blocks
(CORPUS_MAP ⟂ CURRENT STATE, THE_PLAN, THE_ARSENAL, this file) brought up to speed; no paper changed. See the
r1406 and r1407 entries in `CORPUS_MAP.md`.

## What's here
- `corpus/` — all 17 papers as `.tex`, plus every figure they need (`.png`, figure `.pdf`, `figs/`,
  and the `resources/PhD_thesis/` images the papers pull in). The papers compile as-is.
- `computations/` — the original receipt scripts (`.py` + outputs) backing the corpus's computed claims.
- `receipts/` — the curated, corpus-wide receipt set wired into the papers: per-paper subdirs, the
  `INDEX.md` source of truth, `README.md`, `WORKLIST.md`, plus `opens/` and `shared/`. The *Appendix R* in
  each paper (`corpus/appendix_receipts_PN.tex`, and the corpus-wide `appendix_receipts_corpus.tex`) is
  **generated** from `INDEX.md` — never hand-kept.
- All top-level meta/supporting docs (`.md`): CORPUS_MAP, ONTOLOGY_FOUNDATION_INDEX, THE_PLAN,
  THE_EVOLUTION_MAP, CODA_FIELD_NOTE, the CREDO/DEMONSTRATING transcripts, the r966/r968/r969 changelogs, etc.
- `BOOK_INTRO_cosmiCave/`, `scripts/` (incl. `depmatrix.py`), `resources/`, `figures/`, `forks/`,
  `hubble_build/`, and the other working folders.

## What's intentionally NOT here (all regenerable)
- The compiled paper PDFs (`corpus/<paper>.pdf`) — rebuild with any LaTeX toolchain:
  `cd corpus && latexmk -pdf <paper>.tex` (each paper is self-contained: manual `thebibliography`,
  no external `.bib`). Verified: a fresh extract of this bundle compiles cleanly.
- LaTeX build artifacts (`.aux`, `.log`, `.fls`, `.fdb_latexmk`, `.out`, `.synctex.gz`).
- `_backup_r968_psymbol/` — my in-session pre-edit copies of 5 papers (duplicates; not corpus content).

## To rebuild every paper's PDF at once
```
cd corpus
for f in *.tex; do latexmk -pdf -interaction=nonstopmode "$f"; done
```
