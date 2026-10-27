# r7611+70 — RESULT: P15's imposed-route figures on the faithful exponent (registration `5fb7354`)

**Faithful signature:** exp[−α(r²−1)(ℓ/1951.9)²] with α = 1.70 measured at r7577+70.2. That is ℓ_eff = 1497. The receipts were not edited; each was copied here with only the signature's exponent changed:
- `collapse_faithful.py` and `jointfit_faithful.py` are the copies;
- `absorber_faithful.py` is exact arithmetic;
- `wfit_faithful.py` is r7489's tail fitter with the faithful S, and `tail_faithful.py` reads its four mocks;
- the as-built outputs are kept beside the faithful ones (`*_asbuilt.txt`, `*_faithful.txt`).

## Scorecard
| arm | figure | as built | **faithful** | band | verdict |
|---|---|---|---|---|---|
| G-1 | collapse, ruled visibility-peak row: χ² amplitude alone, 185 bins | 1.70 | **6.53** (4.93 at the derived ℓ_D) | 4.5–8.0 | HOLDS |
| G-2 | same row: absorbing tilt | +0.0034 (1.1σ) | **+0.0065** (2.1σ); +0.0057 at the derived ℓ_D | +0.0055–0.0080 | HOLDS |
| G-3 | share absorbed by amplitude + tilt | 70 % | **70 %** | 0.62–0.78 | HOLDS |
| G-4 | sign set by the endpoint; collapse against 1.082 | 13- and 100-fold | sign unchanged; **12- and 95-fold** | within ×2 | HOLDS |
| G-5 | joint fit: χ²/bin after the tilt, r = 1.0926 | 1.497 | **1.062** | 0.85–1.35 | HOLDS |
| G-6 | joint fit: the Gaussian survives; tilt share; window running | 69.8 %, 6.3× | **69.6 %, 6.2×** | unchanged | HOLDS |
| G-7 | wrong absorber: dn_eff at ℓ = 2508 | −1.31 | **−1.088** | −1.085 ± 0.01 | HOLDS |
| G-8 | wrong absorber: swing over ℓ 30–2508 | 6989× | **6989×** | exact | HOLDS |
| G-9 | tail: signature mock's shift on ℓ 1000–2508 | +0.0253 | **+0.0218** (×0.86) | +0.018–0.023 | HOLDS |
| G-10 | tail: precision needed to decide on 1000–2508 | 1.25× Planck | **1.44× Planck** | 1.35–1.70 | HOLDS |
| G-11 | tail: any window separated at 2σ? | none (best 1.94) | **none (best 1.65, 700–1760)** | — | HOLDS |
| EFFORT | | | ≈ 1 h of work, 35 min of fits | 3 h | under |

## What moves, and what does not
- **The sizes move, in opposite directions depending on the receipt's ℓ_D.**
  - The joint fit, the wrong absorber and the tail fit wrote ℓ_D = 1362. Their signature gets weaker: the exponent falls to 0.83, so χ² falls by about a third and shifts and slopes by 14–17 %.
  - The collapse receipt derived ℓ_D ≈ 2093–2133. Its signature gets stronger: χ² is 3.8× at the header ℓ_D, 2.9× at the derived one, and the tilt is 1.9×.
- **The ruled visibility-peak row now costs 6.5 in χ² over 185 bins** (0.035 per bin) and a tilt of +0.0065 (2.1σ), where P15 quotes 1.7 and +0.0034.
  - It still passes the receipt's "under 0.1 per bin" and "under 0.15σ per bin after the tilt" tests.
  - The recombination row no longer does (0.28 per bin). That row is not the ruled one.
- **Exponent-independent, as 69 expected:** the 70 % share absorbed by a tilt, the Gaussian-shaped residual, the sign set by the endpoint, the ℓ² running of the tilt with the window (5.7× against 5.5×), and the 7000× slope swing.
- **The r²−1 scaling the collapse receipt rests on loosens.** With the signature larger, the tilt is linear to 3 % (it was under 3 %) and the χ² is quadratic to 15 % (it was under 8 %). Both of the copy's pinned checks on this fail. The re-pricing argument still holds at that looser precision.
- **One as-built agreement was a coincidence.**
  - The joint fit's claim to reproduce C62's instrument-route tilt to 2 % (−0.0830 against −0.0847) compared r = 1.0926 at ℓ_D = 1362 with the instrument at DAMPX = 1.174 (r = 1.0837).
  - On the faithful exponent the same route gives −0.0694. Scaled to the instrument's r²−1 that is about −0.062, 26 % short of −0.0847.
  - This is the non-Gaussian remainder r7577 already measured (closure 0.78 against 0.92 χ²/bin).
- **PO-24's data gate tightens.**
  - On ℓ 1000–2508, deciding needs tail data 1.44× Planck's precision, not 1.25×.
  - The easiest window, 700–1760, needs 1.21× (from about 1.03).
  - Every window still sits within 1.65σ of both predictions, so the question remains decidable and not decided.

## For 69 (P15 text; I do not edit the paper)
- **Figures that change on the faithful route:**
  - 1.7 → 6.5 χ² and +0.0034 → +0.0065;
  - 1.497 → 1.062 per bin, and the joint fit's tilt −0.0830 → −0.0694;
  - −1.31 → −1.09 at ℓ 2508;
  - the tail mock's +0.025 → +0.022;
  - the 1.94 → 1.65 best separation;
  - the 1.25× → 1.44× bar;
  - the 2 % agreement with C62's instrument route becomes 26 %.
- **Unchanged:** 70 %, the Gaussian residual, the endpoint sign, the window running, and the 7000× swing.
- **Census flag (r7577 rule):** P15 and P7/P18 sentences that state the 1.25× precision bar move to 1.44×.
