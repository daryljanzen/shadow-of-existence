# BUNDLE — r2376+c54.85
*The c54 fork of the Cosmological Relativity programme, cut at the close of the leads sweep.*

**HEAD:** `39ef69c r2376+c54.85 — the four strategic grains propagated: the leads sweep written into THE_PLAN, THE_WEAVE, the open-problems ledger and the map, with every protected item's movement recorded as a narrowing`
**Cut:** 2026-08-09 · node c54 · working from `/root/corpus/cr_r2376`

---

## ⌗ WHY THIS CUT

The lead register — opened at c54.16 as the instrument that nothing surfaced may escape — has been
**worked to its floor**. It stood at 127 registered / 20 open when the colour arc closed at c54.62.
It now stands at:

```
LEAD REGISTER: 127 registered · 125 struck · 2 open · 0 HOT
  struck fraction: 98.4%   (reported so it cannot quietly fall)
  HOT fraction of open: 0.0%  (ceiling 34%)
```

Both remaining leads are open **by design** rather than by neglect: `L-110` is the matter sector's own
discharge condition (a SPEC, which stays open until it is met, and which is now one live clause instead
of two), and `L-91`'s owed action is a read of the external flavour literature rather than a computation
on the corpus.

**All eight gates green at the cut**, and 17/17 papers compiling at 0 errors, 0 undefined citations,
0 undefined refs, 0 dead receipt links.

| gate | rc |
|---|---|
| `check_receipts` | 0 |
| `check_kills` | 0 |
| `check_burndown` | 0 |
| `check_currency` | 0 |
| `check_queues` | 0 |
| `check_grains` | 0 |
| `check_supersession` | 0 |
| `check_compile` | 0 |

---

## ⌗ WHAT IS IN THE TWO PARTS

The split follows the convention this fork has used since c54.5 — the delivery channel takes ~21 MB
per file, so the tree is cut in two along `corpus/`.

**`cr_r2376+c54.85_part1_corpus.tar.gz`** — *the corpus proper.* All 17 paper sources and their
compiled PDFs, the generated Appendix R files, the figures, and **the eight gates** (`check_receipts`,
`check_kills`, `check_burndown`, `check_currency`, `check_queues`, `check_grains`,
`check_supersession`, `check_compile`) together with `make_all_appendices.py`. LaTeX intermediates
(`.aux`, `.log`, `.bbl`, …) are excluded.

**`cr_r2376+c54.85_part2_rest.tar.gz`** — *everything else.* The standing registers
(`THE_LIVE_ARC`, `THE_PLAN`, `THE_WEAVE`, `OPEN_PROBLEMS_MAP`, `THE_OPEN_PROBLEMS_LEDGER`,
`PROTECTED_OPEN`, `THE_BASE_RATE`, the field ledgers), the full `receipts/` tree with `INDEX.md`
(242 registered rows), all of `computations/`, `storyboard_receipts/`, `capstones/`, `resources/`,
`retired/`, and `FORK_HISTORY_c54.txt` — the 48-commit log of this fork in plain text, so the revision
history is legible without the `.git` directory.

To restore: unpack both in the same parent directory; they reassemble into a single `cr_r2376/`.

The `.git` directory is **not** included (424 MB). The fork's history is carried as
`FORK_HISTORY_c54.txt`; the commits themselves live in the working session.

---

## ⌗ WHAT THIS CUT CARRIES THAT THE LAST ONE (c54.17) DID NOT

**The colour arc, entire (c54.42–c54.62).** The matter sector's bundle question is answered on its
discrete side and closed on its continuous side: every ambient candidate bundle is real and a real
bundle's complexified holonomy lands in the real form, so none can carry $\su(3)$; the wall is a wall
*of a hinge*, so there are three radii and a non-abelian monodromy where one radius gave only
$\mathbb{Z}_3$; the smallest connected group containing the three wall monodromies and the hinge
3-cycle is $SU(3)$ with the lap as its centre; and second quantisation on the wall kernel returns
baryon 1, diquark 0, meson 1 and *selects* the configuration group uniquely. The bundle is flat — no
curvature, no coupling, no force — walled three independent ways.

**The leads sweep (c54.63–c54.85).** Twenty leads closed, almost none needing new geometry. The five
results worth naming:

- **The transverse plane is the $A_2$ weight plane.** The three vantages' signed areal radii are three
  linear forms; their zeros were read at c54.52 and their *mutual angles* never were. Taken: equal
  length, $120°$ apart, sum identically zero, mutual cosine $-1/2$ — the weight system of the
  fundamental, reached from the metric geometry with no representation theory in the derivation. So
  the $\mathbb{Z}_3$-fixed centre carries no wall because it is the **origin of the weight plane** and
  $\mathbf{3}$ has no zero weight.
- **At odd $D$ the horizon polynomial is even in $r$**, and four separate exclusions are that one fact:
  the missing $\gamma^5$; $-r_0$ lying in the geometry's *own* root set so the parity has nothing to
  relate; the monodromy commuting with a fixed-point-free involution so it cannot be $S_{D-1}$; and the
  root set being $\pm$-paired so it is not $A_2$.
- **$\lambda^2/\Omega_c^2 = D-3$ exactly**, for every $M$ and $\alpha$ — so the eikonal quality factor's
  mass-independence was never four-dimensional. What is four-dimensional is the *value* being one.
- **Colour is a spacelike relation and isospin a timelike one.** The causal trichotomy on the six
  hinge-ends is exactly *which of two labels differs*, and both labels are now named.
- **The lepton two-bit match is a labelling, not a gauging.** No $\mathbb{Z}_2$ grading has three blocks
  and $SU(2)_L$ splits the four leptons $2{+}1{+}1$.

**Two new gates and one hardened.** `check_grains` (the seventh) polices the freshness of the four
strategic standing documents against the register; `check_supersession` (the eighth) matches open leads
against banked receipts and found essentially every strike from c54.77 on. And `check_receipts`'
column lint on the receipt index was promoted from a warning to a failure at c54.83 — a mis-celled row
makes the appendix generator drop the receipt silently — which immediately found two long-standing
corrupted rows.

---

## ⌗ COUNTS AT THE CUT

| | |
|---|---|
| papers | 35 `.tex`, all compiling clean |
| registered receipts | 242 |
| lead register | 127 registered · 125 struck · 2 open · 0 HOT |
| matter-sector computations | 56 in `computations/baryon_edge/` |
| fork commits | 48 (c54.36 → c54.85) |

---

## ⌗ WHAT IS OWED NEXT, so the next cut has a stated target

1. **The two remaining leads**, discussed rather than swept: `L-110`'s live clause (does $T$ act on one
   $R$-eigenspace of the wall mode and trivially on the other?) and `L-91`'s literature read.
2. **The open-problems map and the clues ledger**, taken through the treatment the lead register just
   had — including a staleness pass, since `check_supersession` reads `THE_LIVE_ARC` only.
3. **P7's frontier section**, checked for shrinkage and for whether what left it has fed the synthesis
   sections at weight rather than simply vanishing.

*A second cut is warranted when those three are done.*
