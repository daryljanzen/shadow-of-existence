# P3 — SdS-slicing-curve_v2 — claim inventory (Avenue 11 sweep, r1337; growing as verified)
The slicing curve; hinge geometry; the Euclid-protocol equivalences; the horizon cubic + figures. 3 cited
receipts + figure-math (make_p3_figs.py). Enumeration extended as each is verified.

| # | §label | claim | verifiable? | receipt | status |
|---|--------|-------|-------------|---------|--------|
| 1 | §488 / eq:tripleathinge | the 30°s are ONE (combinatorial/dial/metric) via triple-angle at sin w=½ ⇒ sin 3w=1; 12=3×4 one route | YES | `one_thirty.py` | ✔✔ (minimality via Rule 2, stated) |
| 2 | prop (nine-point item) | the nine-point circle of the hinge triangle IS the throat (Euler R/2=α); a 6th independent route to 2α | YES | `euclid7_nine_point.py` | ✔✔ |
| 3 | α-as-gauge | α alone sets the construction; 2α is the Thales far end (output); anchors √3α, 3α², 60°, tangency forced | YES | `alpha_alone.py` (+asserts) | ✔✔ |
| 4 | prop:factor / prop:locus / sec:ellipse | cubic factors on the ellipse r²+rr₀+r₀²=1 (A₂ norm form); 3 roots sum to 0; ellipse eigenstructure (½,3/2; semi-axes √2,√(2/3); 45°); involution σ; backward-radial reflection | YES | `P03_cubic_factor_ellipse_locus.py` | ✔✔ |
| 5 | prop:gnomonic / prop:triple | r₀=(2/√3)sin w ⇒ 2M=(2/3√3)sin 3w (pure triple-angle), 2/√3 unique; sin u=r₀; Nariai w=π/6 ⇒ r₀=1/√3 | YES | `P03_triple_angle_gnomonic.py` | ✔✔ |
| 6 | prop:flip / sec:seam | seam continuation θ↦π/2+iψ (sin θ→cosh ψ), C¹ join at throat, signature flip (+,+)→(−,+) auto from dθ=i dψ | YES | `P03_seam_continuation.py` | ✔✔ |
| 7 | sec:curvature | K_G=−f′/(2r)=1/α²−M/r³, finite + horizon-blind, one sign flip at r⋆=(Mα²)^⅓ (Schwarzschild-like→de Sitter-like); MS/Komar return M | YES | `P03_curvature_signflip.py` | ✔✔ |
| 8 | sec:overcritical | overcritical SdS = seam's sin→cosh continuation on the horizon angle; 2 roots complex-conjugate on ellipse's complex extension, lone real root negative (backward-radial), f<0 ∀r>0 | YES | `P03_overcritical.py` | ✔✔ |
