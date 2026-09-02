# P7 — CR_framework — claim inventory (Avenue 11 sweep, r1352; growing)
The framework paper: axioms, the cosmogenetic bead, the three-axis reach. 6 cited receipts (5 bead-physics + 1 meta).

| # | §label | claim | verifiable? | receipt | status |
|---|--------|-------|-------------|---------|--------|
| 1 | bead fig / null congruence crosses seam | signed r real & odd through r=0; photon crosses seam bounded | YES | `photon_cross_test.py` | ✔✔ |
| 2 | bead: two cosmic-time legs are complex conjugates | conjugate legs (Schwarz) + e^{2pi i/3} period + pi/3 turnaround | YES | `bead_conjugate.py` | ✔✔ |
| 3 | bead contour / closure on Nariai cut | bounded tau~-contour: real/imag/locked-pi3 legs | YES | `bead_contour.py` | ✔✔ |
| 4 | order-3 bridge (scope corrected r1430) | groupoid Z/3 (r^3-r+2M) vs bead Z/3 (r^3+2M) = DIFFERENT cubics; no AFFINE change of variable identifies their root sets (obstruction at fixed cubic; the two are the E=1 and E=0 ends of one turning-point family, stage 5); identification of root sets not claimed | YES (bounded negative + stage-5 family with control) | `order3_bridge.py` | ✔✔ |
| 5 | fig panel F (arc length) | r(s) vs exact arc length; perpendicular legs; monotonic; tangents | YES | `F_flat.py` | ✔✔ |
| 6 | tab:dependency-matrix | citation-matrix generator | META (runs exit 0, regenerates the dependency table; NOT a physics receipt → stays \texttt{}, not \rcpt) | `depmatrix.py` | ✔ meta |
| — | axioms, three-axis reach, unification-scope | — | analytic (framework) | — | n/a |

**P7 COMPLETE — no missing receipts (confirmed r1358).**
- All 6 cited .py files EXIST; 5 physics receipts ✔✔ (photon_cross_test, bead_conjugate, bead_contour, order3_bridge, F_flat), all cited via \rcpt; depmatrix = meta (runs, not a physics receipt).
- COVERAGE AUDIT: P7's ~21 theorems/props are analytic (lapse/shift, asymptotic non-intersection, smoothness of layers, Minkowski/Schwarzschild projections, no-time-travel, diffeo-invariance, null-boundary, augmentation necessity/sufficiency — all structural proofs, no computation). The bead theorem + two-turnings + progenitor/cosmogenesis are the computational content → fully covered by the 5 receipts. The Hubble–Eddington radius (sec:CR-HEradius) references P3/P6, not re-derived here. No uncovered computational claim; nothing ∅ or ⬚.
