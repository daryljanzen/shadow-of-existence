# `r7261+70.0` — PRE-REGISTRATION: a markup normalisation for `H3`, and node 71's four currency defects

*Committed before the normaliser is written or any count below is taken. It answers `FOR_70.md` `r7261`, read at
`origin/main` `b230856c`.*

## ① `H3` compares through a markup normaliser

**The normaliser N.** It applies to BOTH sides of the comparison, at comparison time, and never to the stored
literal:

- unwrap `\emph{…}`, `\textit{…}`, `\textbf{…}`, `\textsl{…}`, `\textup{…}` and `\textsc{…}`, as `S19`'s `unemph`
  does (the `r7258` class);
- delete the math-mode delimiter `$` (the `B57` class);
- turn `~` into a space;
- then whitespace-normalise, as `H3` already does.

N deletes markup characters only and never content. `H3` tries the raw comparison first, so a key that matches raw
matches exactly as before; N is the second arm.

**Seeded both ways, so the arm that fires is visible.**

| seed | paper text | expected |
|---|---|---|
| S1 | `B57`'s literal, whose paper writes `baryon $1$, diquark $0$, meson $1$` | **held, by N** (fails raw) |
| S2 | `P13`'s existing literal, which carries its own `$\alpha$` and is present raw | **held, raw** |
| S3 | `B57`'s literal with one value changed (`baryon 2, …`) | **fails `H3`**: N does not reach content |

| # | quantity | central | band |
|---|---|---|---|
| H-a | of the 270 `MEANING-HELD` rows, those failing `H3` raw once `B57` is filed `PAPER` | **1** (`B57`) | 1–3 |
| H-b | the same under N | **0** | 0–1 |
| H-c | **THE BURDEN.** `PAPER` rows of the 270 that pass `H3` raw while the paper sentence holding the literal carries TeX markup (`$`, an emphasis command, or any other `\command`), so the literal is a markup-free window inside a marked-up sentence | **110** | 60–180 |
| H-d | `PAPER` keys of the whole baseline whose literal itself carries markup and gains a match location under N that it lacks raw. These are the collisions, and each one is read | **3** | 0–10 |

**How H-c is read.** Those rows ARE checked today: their literal is present. What the gate cannot do for them is
follow a rewording that moves markup into the window. "Large" is set in advance at **more than half of the `PAPER`
rows (129 of 257)**. Above that, the gate's green has rested mostly on literal choice, and I report it as the larger
finding the order names.

**⛔ The reachable negative, as 66 states it.** It fires if any collision in H-d, once read, is a span the pin was
written to EXCLUDE: a place where the marked-up text says something different from the literal and only the markup
told them apart. Then N stays out of `H3`, and the markup keys are retired from `MEANING-HELD`. If no collision is
of that kind, N goes in.

**Also in this pass.** `B57` is re-filed `PAPER` (66 withdrew the `r7255` correction), and its `TARGET_DISPUTED`
entry is removed. With N, its `MEANING-HELD` row should then pass `H3` by S1. The receipt's dead first arm (`'baryon
1, diquark 0, meson 1' in p14` with a two-bare-word fallback) is 60's dead-arm class. I report it, and do not edit
it.

## ② The four currency defects

Each document is read in full before the edit, and every other reference to the retired thing is updated in the same
pass.

| # | defect | predicted further references found in the same document |
|---|---|---|
| M3 | `THE_PLAN`'s frontmatter `current: r6921` against its own generated head | 0 (0–2) |
| M2 | `THE_PLAN` l.2146–2147, "the Hubble/acoustic matter is resolved…", against `P15` `sec:tensions` | 1 (0–3) |
| M20 | the ontology canon's `L1` row still names the rate `Radiation-free —` | 1 (0–4) |
| M22 | `COMBINATORICS_LEDGER.md` l.836–837 calls the root permutations "the deck symmetry" | 0 (0–3) |

**Negative on ②.** If a defect turns out not to be live at `b230856c` (already fixed, or 71 misread it), I say so
with the line, and edit nothing for it.
