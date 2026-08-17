# BUNDLE — r2376+c54.142  *(two parts)*
*Cut where the collapse-perturbation arc turns adversarial: the sector is over-determined and, at present, fails its own test.*

**HEAD:** `73e96fd r2376+c54.142 -- correct the rule violation: the over-determination is a result, not a choice`
**Cut:** 2026-08-10 · node c54

---

## ⌗ THE TWO PARTS — *complete between them; neither file is split*

| part | file | size | contains |
|---|---|---|---|
| 1 | `CR_bundle_r2376+c54.142_part1_corpus.tar.xz` | 14 MB | `corpus/` (17 papers + figures), `receipts/` (273 scripts, `INDEX.md` the source of truth), `figures/`, `verification/`, and the 139 standing `.md` documents |
| 2 | `CR_bundle_r2376+c54.142_part2_working.tar.xz` | 14 MB | `computations/` (192 scripts), `resources/`, `scripts/`, `forks/`, `capstones/`, `hubble_build/`, `kills/`, `retired/` and the other working folders |

Both extract into the same `cr_r2376/` root; extract part 1 then part 2 and the tree is whole.
**Verified by extraction**: the union differs from the tracked tree only in build artefacts and `__pycache__`.
Compiled PDFs are excluded as regenerable — `cd corpus && latexmk -pdf <paper>.tex`.

---

## ⌗ WHAT THIS CUT CARRIES THAT c54.137 DID NOT

**THE TENSOR SECTOR (c54.138).** The transfer machine runs with *no* idealisation there — $z_T=aM_{\rm Pl}/2$
exactly, for any content — and returns $\mathcal{P}_T\simeq2\times10^{-93}$ against a ceiling of
$7\times10^{-11}$: **no primordial $B$-modes at any conceivable sensitivity**, no longer resting on the
substrate's floor. The crossing multiplies $r$ by a $k$-independent 24, so the observed bound measures the
parent.

**FRONT #3 CLOSED (c54.138).** Perturbations stay linear by six orders, read off the observed amplitude rather
than assumed; and **the Bianchi shear is not a free datum but the long-wavelength growing tensor mode**, so
bounding the tensors bounded it — six orders at the sky's ceiling, forty-seven at the predicted amplitude.

**THE BOUND, COMPUTED (c54.141).** The mode equation depends on $u=c_sk\rho$ alone, so the collapse leg's
transfer is one curve at unit incoming amplitude: $\mathcal{P}_{\rm out}=c_s^2k^5|g(u)|^2N_k^2/(2\pi^2M^2\rho^2)$.
The sky constrains its **running**, not its knee. $\rho\le6.5\times10^{-5}$ — 180× tighter, and the first
version of this bound that was integrated rather than argued.

**TWO RETRACTIONS (c54.139, c54.141).** c54.133's criterion asked the wrong question; and c54.139's withdrawal
of c54.138 was itself wrong — I checked a claim's wording against a retired assumption instead of recomputing it.
Four versions of this bound were argued and all four were wrong.

**THE OVER-DETERMINATION (c54.142).** Two chains fix the progenitor's equality and neither has a free step: one
bead with one integration constant plus a crossing plasma gives $\rho=5.4\times10^{-2}$; the bound gives
$\rho\le6.5\times10^{-5}$. **They disagree by $831\times$.** Recorded in P16 as a result, with the weakest
step named — whether the surviving mode is fed by the leaked branch at all. Nothing upstream depends on it.

**AND THE LIST WAS UNDER-REPORTING BY TWO-THIRDS.** `THE_WORK.md` omitted all ten protected-open items.
Fifteen live items are now listed there.

---

## ⌗ WHAT IS OPEN — *fifteen items; the full table is in `THE_WORK.md`*

Five live fronts under four register rows — the over-determination (`L-150`), the two acoustic-peak routes
(`L-171`/`PO-7`), the graviton tower's UV definition (`L-165`/`PO-6`), the closed-form nonlinear ⛭⛭ **⟨STRUCK r2993 — both clauses answered: the phase is FORCED then DERIVED, and the $0.615$ deficit is a real disagreement at **$76\sigma$** with a **$0.7\%$** substitution error measured on Planck's own spectrum. `kills/PO-7.md`.⟩**
$\Lambda>0$ solution (`L-165`), and the likelihood verdict (`L-147`, fenced, last) — beside ten
`check_kills`-protected items: `PO-1a`–`PO-1d`, `PO-2`–`PO-5` (the matter sector), `PO-8` (the
reassignment remainder) and `PO-9` (the dimensional descent).

Ten gates green; 17/17 papers compile at 0 errors, 0 undefined citations, 0 undefined refs, 0 dead receipt links.
