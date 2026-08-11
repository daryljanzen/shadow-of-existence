# P2 — janzen_circle_v3 — claim inventory (Avenue 11 sweep, r1334)
The Schwarzschild interior as a cycloid; two critical points = two metric singularities; Kretschmann as a
chart-labelling artefact; analytic continuations through both seams. 27 equation blocks, no cited receipts.

| # | §label | claim | verifiable? | receipt | status |
|---|--------|-------|-------------|---------|--------|
| 1 | prop:cycloid | r(η)=M(1+cos η), τ(η)=M(η+sin η) solves dτ²=r/(2M−r)dr²; proper time Mπ | YES | `P02_cycloid_and_critical_points.py` | ✔✔ |
| 2 | prop:critical | dr/dη=−M sin η; two non-degenerate critical points (2M max, 0 min) = r-poles of circle (r−M)²+s²=M² | YES | `P02_cycloid_and_critical_points.py` | ✔✔ |
| 3 | sec:kretschmann | K(r)=48M²/r⁶ finite (3/4M⁴) at r=2M, divergent at r=0; the divergence is a chart-labelling / chain-rule artefact (12th-order pole = 2nd-order zero of r × r⁻⁶; label swap moves it to the horizon) | YES (headline) | `P02_kretschmann_chain_rule.py` | ✔✔ |
| 4 | sec:continuation | continuation z=iρ (Region I exterior, matches Schwarzschild) and z=π+iρ' (back-seam onto r<0): trig→hyperbolic | YES | `P02_analytic_continuations.py` | ✔✔ |
| 5 | sec:ring | single horizon as the Λ→0 limit of the SdS root triple (two roots →∞, one →2M; triple sums to zero) | YES | `P02_ring_lambda_limit.py` | ✔✔ |
| 6 | sec:metric-singularities, sec:four_regions | the two critical points are the two metric singularities; Kruskal front + back-seam pair | partly analytic (K-part → #3) | — | n/a/⬚ |

**Progress:** ALL verifiable claims ✔✔ (cycloid+critical, Kretschmann artefact, continuations, Λ→0 ring). #6 (metric-singularities/four-regions) is analytic + the K-part is #3. **P2 at bar.**
