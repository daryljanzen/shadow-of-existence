# P8 — slicing_operator — claim inventory (Avenue 11 sweep, r1359; BUILDING — cited no receipts)
The de Sitter slicing operator: the construction gauge, the matter functional, vacuum kernel, matter-as-bend, the lapse split/EoS, the E=1 cosmology, the constant-curvature trichotomy.

| # | §label | claim | verifiable? | receipt | status |
|---|--------|-------|-------------|---------|--------|
| 1 | sec:gauge (eq:Ttt/Ttheta) | matter functional from the Einstein tensor; lock p_r=-rho | YES | `P08_matter_functional.py` | ✔✔ |
| 2 | thm:kernel | vacuum T=0 <=> SdS (general solution of r f'+f-1+Lam r^2=0) | YES | `P08_matter_functional.py` | ✔✔ |
| 3 | prop:bend | density rho=m'/(4 pi r^2) is the bend of the cut | YES | `P08_matter_functional.py` | ✔✔ |
| 4 | prop:lapse | lapse split: density=leaf(f) alone; EoS=(f/r)d/dr ln(A/f); A=f -> p_r=-rho | YES | `P08_lapse_split.py` | ✔✔ |
| 5 | prop:cosmo | E=1 = flat-LCDM (scale factor, Friedmann, OS limit); HEB handover min at r_star | YES | `P08_E1_cosmology.py` | ✔✔ |
| 6 | prop:trichotomy | 3 leaves (S^3/horosphere/H^3, k=+1/0/-1) = one congruence at 3 energies (-k=E^2-1); ^3R=6k/a^2 | YES | `P08_trichotomy.py` | ✔✔ |

| 7 | sec:synchronous (eq:embed) | flat horosphere slicing: embedding+induced flat metric; eta(X,B)=(a^2/2)e^{tau/a} level sets; tau->-inf singularity | YES | `P08_synchronous_horosphere.py` | ✔✔ |

**P8 COMPLETE — all 7 computational claims BUILT + verified (r1359-r1363).** 5 receipts: matter_functional (covers thm:kernel+prop:bend+matter functional), lapse_split (prop:lapse/EoS), E1_cosmology (prop:cosmo + HEB handover), trichotomy (prop:trichotomy), synchronous_horosphere (sec:synchronous flat slicing).
FULL COVERAGE AUDIT: all 5 propositions + the sec:synchronous "direct computation" receipted. sec:ontology (setting), sec:dictionary (the vacuum-plane/bend geometric dictionary → prop:bend), sec:open (scope/open problems) are analytic — no further computation. P8 went from CITING NOTHING to fully computed (7 claims, 5 receipts).
