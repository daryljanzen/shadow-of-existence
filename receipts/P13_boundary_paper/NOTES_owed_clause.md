# P13 — documentation finding (r1381, from closure_i_check)

**prop:closure (i)** — "R carries 3 -> 3bar because R is the A2 diagram automorphism" — HOLDS, but the
receipt (P13_closure_i_check.py) flags that the corpus is **owed one clause**: the identification
"R negates the roots => R conjugates the representation" is **A2-SPECIFIC**. Its warrant is that
**-1 is NOT in the Weyl group W(A2)** (so the longest Weyl element is not -1, and the negation acts as the
outer automorphism rather than an inner one). The paper currently reads as though "negates the roots" means
"conjugates the rep" generally, which is false outside A2. Suggested fix for Daryl: add a half-sentence at
prop:closure (i) noting the A2-specificity and citing the -1-not-Weyl warrant (cf. P5 negation_outer_A2).
NON-BLOCKING: the leg holds; this is a clarity/rigour clause, not a correction.
