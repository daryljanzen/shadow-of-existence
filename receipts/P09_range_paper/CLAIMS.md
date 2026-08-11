# P9 — range_paper — claim inventory (Avenue 11 sweep, r1364; BUILDING — cited no receipts)
The slicing operator's RANGE: which geometries it reaches. so(4,1) symmetry bound; Kerr-dS reached; Type-D
vacuum kernel (Kerr-NUT-(A)dS) + Carter constant; algebraic type no constraint (Type I reached, radiative
absent); the range = symmetry-reducible sector, the wall = inhomogeneity / free gravitational radiation.

| # | §label | claim | verifiable? | receipt | status |
|---|--------|-------|-------------|---------|--------|
| 1 | prop:radiative | pp-wave = Type N (vacuum, Weyl!=0, invariants=0); radiative types absent | YES | `P09_ppwave_typeN.py` | ✔✔ |
| 2 | thm:bound | so(4,1) symmetry bound: H-swept geometry has H as isometries (>= dim H Killing vectors) | YES (structural) | — | ⬚ TO BUILD |
| 3 | prop:kerr | Kerr-dS vacuum-Lambda; Delta_r=r^2 f_SdS+a^2 f_dS; a->0=SdS; M->0=max symmetric | YES | `P09_kerr_deSitter.py` | ✔✔ (J=Ma/Xi^2 Komar noted, not computed) |
| 4 | thm:pd | Carter cut vacuum-Lambda IFF Dr,Dp are the quartics (leading -L/3, shared c0, opposite c2) | YES | `P09_typeD_quartics.py` | ✔✔ |
| 5 | cor:carter | separation splits of its own accord; Carter constant = irreducible Killing tensor (grad_(a K_bc)=0) | YES | `P09_carter_killing.py` | ✔✔ |
| 6 | prop:typeI | generic vacuum-Lambda Bianchi-I is Petrov Type I (3 distinct Weyl eigenvalues) | YES | `P09_bianchiI_typeI.py` | ✔✔ |
| 7 | prop:ksvac | KS vacuum kernel = SdS interior (rho=p_chi=p_perp=0 by direct substitution) | YES | `P09_ks_vacuum.py` | ✔✔ |
| 8 | thm:bound | so(4,1) symmetry bound: H-swept geometry carries H as isometries | STRUCTURAL (construction argument; necessity) | — | analytic |
| 9 | prop:surj | in-class surjectivity (function-count matching, case by case) | STRUCTURAL | — | analytic |
| 10 | thm:range / cor:wall / cor:radiation | range = symmetry-reducible sector; wall = inhomogeneity / free radiation | STRUCTURAL (upper bound thm:bound + filling + boundary via prop:radiative) | — | analytic |

**P9 COMPLETE — all 6 computational claims BUILT + verified (r1364-r1369).** Receipts: ppwave_typeN (prop:radiative), bianchiI_typeI (prop:typeI), kerr_deSitter (prop:kerr), typeD_quartics (thm:pd), carter_killing (cor:carter), ks_vacuum (prop:ksvac).
FULL COVERAGE AUDIT: the computational claims are all receipted; thm:bound (necessity, construction argument), prop:surj (function-count, case by case), thm:range/cor:wall/cor:radiation (upper bound + filling + boundary) are STRUCTURAL. Final scan: "Direct substitution" (prop:ksvac) and "Weyl eigenvalues" (prop:typeI/radiative) covered; L113 intro roadmap. Zero uncovered. NOTE: J=Ma/Xi^2 (Komar) noted in kerr receipt, not computed (optional).
