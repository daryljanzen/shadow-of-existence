# Bundle r969 — external references pass (the last contained item) + r968 recap

This bundle closes the **only** thing that was deferred after r968: the external literature citations
(the "AB-1 references pass"). Every flagged named result, metric, theorem, and dataset that the corpus
invoked-but-did-not-cite has been given a **web-verified** primary reference. The corpus is now complete
and self-consistent up to and including its external scholarly apparatus.

## Method (honesty guarantees)

Six parallel readers, one per paper-group, each under a strict protocol: **never fabricate** — every
`\bibitem` had to be confirmed at a primary/authoritative source (publisher DOI, APS/AIP/IOP/Springer
landing page, ADS, arXiv, or official republication) before insertion; cite only where the body actually
invokes the result; match each paper's existing bibitem format; recompile clean. I then verified
independently: full-corpus recompile (0 undefined citations), duplicate-key scan (none), CITE-TODO sweep
(none), and web re-verification of a spot-check sample (Borsanyi Nature 539 = "Lattice QCD for Cosmology",
appropriate for the QCD-transition scale; Nariai 1951 GRG Golden-Oldies reprint; Kretschmann 1915 Annalen).
The readers caught and corrected several candidate errors themselves (Chen–Lü–Pope is Class. Quantum Grav.
23, 5323 — not Nucl. Phys. B; Hubble's M31 V1 is ApJ 69, 103 — not the PNAS redshift paper; the wall's VSI
reference is the **4D** Pravda–Pravdová–Coley–Milson 2002, not the higher-dimensional 2004 paper).

## What landed (≈60 external references; all strong flags closed)

**P1 BH_causality:** Hubble1929M31 (ApJ 69, 103 — M31 V1 Cepheid).
**P2 circle:** Milnor1963 (Morse Theory), Kretschmann1915 (Ann. Phys. 48, 907), Tolman1934 (PNAS 20, 169);
  dangling `lemaitre1933` **wired up** (it is genuinely invoked — Lemaître–Tolman cycloid), not deleted.
**P3 slicing:** Kottler1918 (Ann. Phys. 361, 401), Nariai1951 (Sci. Rep. Tôhoku 35, 62; GRG 31, 963),
  Snyder1987 (USGS PP 1395, gnomonic projection).
**P4 modern_parallax:** Bessel1838 (Astron. Nachr. 16, 65 — 61 Cygni parallax). **[strong flag closed]**
**P5 groupoid:** Humphreys1972 (Lie algebras / A₂ root system) — its first external reference.
**P9 range:** Kerr1963, ChenLuPope2006 (Kerr–NUT–(A)dS), Petrov1954, GoldbergSachs1962, Birkhoff1923,
  TomimatsuSato1972, Zipoy1966, Voorhees1970, WalkerPenrose1970 (Carter constant/Killing tensor),
  Painleve1921, Gullstrand1922, Nariai1951; existing Carter1968 now cited at the separable-cut invocation.
**P10 canonical_time:** HartleHawking1976, Weyl1910 (limit-point/limit-circle), ReedSimon1975 (self-adjointness).
**P11 dynamics:** Wald1983 (cosmic no-hair), BunchDavies1978, MukhanovFeldmanBrandenberger1992,
  Brinkmann1925 (pp-waves), PravdaVSI2002 (4D VSI).
**P12 algebroid:** Mackenzie2005 (Lie algebroids), Helgason1978 (symmetric spaces), Humphreys1972 (A₂),
  LawsonMichelsohn1989 (spin geometry / γ⁵).
**P13 boundary:** GeorgiGlashow1974 (SU(5)), FritzschMinkowski1975 (SO(10)), AtiyahSinger1968,
  Lichnerowicz1963 (Spineurs harmoniques) **[strong flag closed]**, LawsonMichelsohn1989.
**P14 matter:** JackiwRebbi1976 **[strong]**, CallanHarvey1985 **[strong]** (domain-wall zero-mode),
  AtiyahSinger1968, IshimoriEtAl2010 (non-Abelian discrete flavour symmetry) — its first external references.
**P15 CR_cosmology:** Planck2018, Riess2022 (SH0ES), Moresco2016 (cosmic chronometers), Silk1968,
  SachsWolfe1967, Harrison1970, Zeldovich1972, GibbonsHawking1977.
**P16 cosmogenesis:** Planck2018, Cooke2018 (D/H), Aver2021 (Yp), Silk1968, Borsanyi2016 (lattice-QCD
  transition), Sallaska2013 (StarLib), Cyburt2010 (REACLIB), PDG2022 (neutron lifetime), AME2020 (B_D)
  — went from **zero external references to a full empirical bibliography** (it is the BBN paper).
**p0 geometric_core:** GibbonsHawking1977 (de Sitter horizon thermal state).
**P7 CR_framework (dangling cleanup):** `Riess1998` + `Perlmutter1999` **wired up** at the cosmic-acceleration
  invocation; `Aghanim2020` and `Janzen2014` **deleted** (defined, never invoked — the CMB claims defer to
  the companion cosmology paper).
**P8 slicing_operator, P6 shadow:** no additions — nothing external was invoked-uncited (P6 already carries
  its history-of-science apparatus; P8 defers to companions).

## Verification status

All 17 papers compile clean (latexmk exit 0), **zero undefined citations corpus-wide**, no duplicate bibitem
keys, no CITE-TODO placeholders. External-reference coverage per paper is now: P4=21, CR_framework=15,
range=15, canonical_time=14, BH_causality=12, shadow=12, dynamics=10, circle=10, algebroid=10, CR_cosmology=11,
boundary=9, cosmogenesis=9, geometric_core=4, matter=4, slicing=3, groupoid=1, operator=1.

## This bundle also carries r968 (recap)

- **P-symbol canon** resolved corpus-wide: `R` = mass-reflection/orientation/A₂-diagram-automorphism parity
  (= γ⁵); `P` = areal spatial parity r↦−r; `T` = time reflection. Forced by CPT-coherence. (See `BUNDLE_r968.md`.)
- **Coherence cleanup:** P9 Type-D ratio `27J²/I³ ≡ 1` (was wrongly `≡4`); p0 L630 wash-reading; P7 figure
  + full 17×17 dependency matrix refreshed to the authoritative resolver; p0 six-way rung count verified.

## Open items after r969

None that are contained/mechanical. What remains is **genuine frontier**, all publish-open by design and
not claimed-flagged: the high-ℓ acoustic transfer (gated on the perturbation sector), the SM gauge/mass
content (external), the beyond-the-wall radiative sector, the quantum completion, and P6's base-rate
programme. These are research directions, not debts. The corpus is coherent, cohesive, empirically anchored,
and fully cited up to its frontier.
