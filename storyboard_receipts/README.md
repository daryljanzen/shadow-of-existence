# Storyboard receipts — verification scripts behind SYNTHESIS_FIGURE_STORYBOARD.md

Each is a small standalone numpy/sympy check for a claim in the storyboard.
- geom1/2/3.py       — early Nariai/slicing geometry checks
- chiral.py          — species = sign(r) = chirality (hinge handedness), X0-independent
- endoverend.py/2    — the end-over-end involution E = T*P (det +1), charge-conjugating
- wrapsense.py       — sigma (A<->B) preserves species; the charge-preserving vs -conjugating split
- sheets.py          — the 3-sheeted Riemann surface r^3=2M sinh^2; branch at r=0; order-3 monodromy
- autA2.py           — sheets + charge conj + complex conj generate D6 = Aut(A2) = S3 x Z2
- gen_vs_sheets.py   — sheet triple (equal-mag) vs generation triple (unequal): naive bijection dead
- cubic_space.py     — the deformation test: two rays from one center (r=0), no collapsing symmetry
- hornlap.py/2       — the continuous horn->lap mechanism (branch point at r=0 forces the imaginary lift)
