# Theorem 1: the Carter constant's inheritance from the substrate

kerr_schild_congruence_in_de_sitter.py (steps 1-3; step 4 is the slow symbolic form of the next script):
the Kerr-Schild vector k of Kerr-de Sitter (Gibbons-Lu-Page-Pope form), taken on the de Sitter background
g0 (R_ab = Lambda g_ab, verified), is null, affinely geodesic, shear-free, twisting
(twist^2 = a^2 cos^2(theta)/Sigma^2), with expansion r/Sigma, and carries no dependence on the mass.
A null geodesic of de Sitter is a straight null line of the ambient, a ruling, so k is a twisting
shear-free congruence of substrate rulings.

kerr_de_sitter_is_einstein_numeric.py: g = g0 + (2Mr/Sigma) k k satisfies R_ab = Lambda g_ab
(exact rational parameters, four points, all components, residual below 1e-130).

Still to do for the theorem: the Kerr-NUT-de Sitter family through its double Kerr-Schild form, and the
M = 0 limit of the Killing tensor as a quadratic in the so(4,1) Killing vectors.
