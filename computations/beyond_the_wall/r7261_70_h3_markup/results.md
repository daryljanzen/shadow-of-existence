# `r7261+70.1` — results: `H3` reads through markup and the normaliser is two-sided; the burden is large

*Pre-registered at `PREDICTION.md` (`6931c785`). The measurement is `measure.py`, and its output is `measure.txt`.*

## ① The markup normaliser

**What went in.** `check_quote_pins._unmark` is applied to BOTH sides, at comparison time, and never to a stored
literal. It does three things:

- unwraps the emphasis family, as `S19`'s `unemph` does;
- deletes `$`;
- reads `~` as a space.

`_present_at` tries the raw comparison first; the normalised one is its second arm. `B57` is filed `PAPER` again
and is held through that arm. The `TARGET_DISPUTED` entry is gone, and the mechanism is kept empty.

**The seeds, in `_held_seeds`, all three as stated.**

| seed | result |
|---|---|
| S1 `B57`, whose paper writes `baryon $1$, diquark $0$, meson $1$` | absent raw, **held through N** |
| S2 `P13`'s literal, which carries its own `$\alpha$` | **held raw** |
| S3 `B57` with one value changed | **fails**: N deletes markup, never content |

| # | quantity | predicted | measured |
|---|---|---|---|
| H-a | held rows failing `H3` raw, with `B57` filed `PAPER` | 1 (1–3) | **1** (`B57`) |
| H-b | the same through N | 0 (0–1) | **0** |
| H-c | `PAPER` held rows passing raw while the literal's paper sentence carries markup | 110 (60–180) | **231 of 258**: refuted high, **above the "large" line of 129** |
| H-d | baseline `PAPER` keys whose literal carries markup and gains a match location under N | 3 (0–10) | **13**: refuted high |

### ⛔ H-c is large, and it is the bigger finding the order named

**231 of 258 `PAPER` held rows are markup-free windows inside marked-up sentences.** The registered count
includes any `\command`, so I broke it down (this breakdown was not scored). The first matching kind wins:

| the sentence carries | rows |
|---|---|
| math (`$`) | **135** |
| emphasis | **81** |
| references only (`\cite`, `\ref`, `\rcpt`, …) | 13 |
| another command | 2 |
| nothing | 25 |

**Even counted narrowly, as math or emphasis only, it is 216 of 257, or 84%.** In addition, 42 held literals carry
markup themselves.

**So the gate's green has rested mostly on where the literal was cut.** The rows were checked, and each literal is
present. But a rewording that moved markup into the window would have read as the sentence vanishing, which is
`B57` exactly. N removes that blind spot for math and emphasis. It does not cover `\cite`, `\ref` or other
commands, which split 15 rows.

### ✔ The negative does not fire: no collision excludes anything

I read all 13. In every location N matches and raw does not, the text carries **the same words as the literal**,
and only the markup differs:

- **6 have literals with `$…$` that are absent raw** (`B9`, `B13`, `B14` ×2, `B23` ×2). The paper writes the same
  clause with `~` before the math.
- **6 gain a second location carrying the identical clause with different markup:**
  - `P4` and `Q1`: "the $R$-odd \emph{departure}", unwrapped in `geometric_core_paper`;
  - `P07`: the Hubble–Eddington radius;
  - `C14` and `C16`: "The end-to-end … transfer is run", without emphasis in `CR_cosmology`;
  - `P15`: "does not \emph{select} it".
- **1 is a fragment, `$A_s`**: 23 locations raw and 25 under N, all the same quantity.

None is a span the pin was written to exclude. N only lets `H3` follow markup, and it is applied in `H3` alone: no
receipt's own test changes. **So N goes in.**

## ② The four currency defects

Each document was read in full before it was edited, all 4,409, 2,422 and 1,068 lines of it. The three reads were
run in parallel by read-only agents, each reporting every line it read. I verified every site below myself before
editing it.

| # | edit | further references, predicted | found |
|---|---|---|---|
| **M3** | `regen_grain_currency.py` now writes each grain's frontmatter `current:` from the register front it already prints. `THE_PLAN`, `THE_OPEN_PROBLEMS_LEDGER` and `THE_WEAVE` read `r7261`; `OPEN_PROBLEMS_MAP` has no `current:` line. `--check` covers it. | 0 (0–2) | **3**: dated hand-written currency headers in the body (l.358 `r2379`, l.394 "STOPS AT c54.137", l.755 the `r1783` audit). Each says its own revision, so they are history and I left them. **Refuted high** |
| **M2** | The l.2145–2147 guard now carries the README's `r7181` form. | 1 (0–3) | **1**: l.2922 "P15 carries the resolution", quoting P15 as fixing $H_0$ "with the acoustic angle". P15 says "alongside the epoch", about the baryon-acoustic distances. Corrected to "the confrontation", with the right quote and the ladder discrepancy left where P15 leaves it |
| **M20** | L1 at l.1064 now reads "Fixed by α and x₀ —", from the notice's own list. | 1 (0–4) | **1**: the notice's own claim to be "the only place" (l.95), corrected to the canon only |
| **M22** | l.836–837 now reads "the **monodromy** (Weyl) `S₃`, not a deck symmetry". | 0 (0–3) | **4**: l.736–738 (p0's quotation, left verbatim with a dated correction note, and the false "P14 says the same"); l.753, the table's "deck/monodromy group"; l.1045 `P07`'s "deck $S_3$ vs $\mathbb{Z}_3$"; l.1050 `P12`'s "deck $S_3$". **Refuted high** |

All four defects were live at `b230856c`, so the negative on ② does not fire.

**Found in the reads, and outside this order's edits:**

- **"radiation-free" is not retired corpus-wide.** It appears 456 times in 111 live files, including P15's body
  ("the distances are radiation-free"). There it qualifies a quantity rather than naming the rate. The canon's
  "corpus-wide" claim is now scoped to what it can hold.
- **The ontology canon breaks three more of its own retirements:**
  - Ψ is still used for the null-boundary correspondence, at l.904 and l.1463–1496.
  - `ρ` is used for the merged root, at l.878, 887 and 2253–2273, against l.720.
  - Bare "the seam" appears at l.1209–1272, against l.818.
- **Three receipts carry the deck/monodromy conflation in their own text:**
  - `P05_dihedral_generators` l.23;
  - `P08_the_branch_point_monodromy_is_Z3` l.218, which is "the Weyl $S_3$ is the deck symmetry";
  - `L203/M1` l.18, 36, 98 and 151.

  They are other seats' receipts, and I left them.
