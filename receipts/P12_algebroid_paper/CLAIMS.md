# P12 — algebroid_paper — claim inventory (Avenue 11 sweep, r1377; cited no receipts)
An algebroid without a base: the action Lie algebroid of the cut-deformation. The substrate/base/two operations,
the anchor, the bracket closure (= Dirac algebra), the isotropy stratification, the discrete skeleton.

| # | §label | claim | verifiable? | receipt | status |
|---|--------|-------|-------------|---------|--------|
| 1 | prop:closure | symmetric-space grading so(5,1)=h+m closes ([h,h]<h,[h,m]<m,[m,m]<h) = Dirac algebra | YES | `P12_bracket_closure.py` | ✔✔ |
| 2 | sec:anchor | anchor = ADM data (Ham constraint, momentum, lapse-split A=f=>p_r=-rho [P8], signature); homomorphism = prop:closure | STRUCTURAL (ADM mapping; lapse-split -> P8; homomorphism = prop:closure) | — | analytic |
| 3 | structure function | h^{ab} = coset metric of SO(5,1)/SO(4,1), signature (1,4) Lorentzian (problem-of-time sign) | YES | `P12_coset_metric.py` | ✔✔ |
| 4 | sec:isotropy / sec:discrete | isotropy stratification, metric-singular seams, discrete skeleton | structural/classification | — | analytic |

**P12 COMPLETE — 2 computational receipts (r1377-r1378).** bracket_closure (prop:closure), coset_metric (structure function = Lorentzian coset metric).
COVERAGE AUDIT: sec:anchor is STRUCTURAL (anchor = ADM data; lapse-split A=f=>p_r=-rho references P8; the anchor-homomorphism IS prop:closure's correspondence); sec:isotropy/sec:discrete are structural (stratification, discrete skeleton). Zero uncovered computation.
