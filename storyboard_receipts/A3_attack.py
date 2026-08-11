"""
ADVERSARIAL PASS on the parallel node's A3 (r1091).
Its ask: "Don't take my A3 on trust -- attack it. Verify it genuinely works the full
object -- no real slice smuggled in, no rigged discriminator -- and genuinely lands on
shadow, not an over-close."

Its claim:  C = (Q->-Q)_field  o  (R o K)_geometric
            [6] RESOLVED, bounded: the L2 antilinear face is C's KINEMATIC shadow.

Four attacks. Each can return against it.
"""
import numpy as np, sympy as sp

a = 1.0
def bead(r, tau, twoM): return r**3 - twoM*a**2*np.sinh(1.5*tau)**2
def f_metric(r, twoM, Q): return 1.0 - twoM/r + Q**2/r**2 - r**2/a**2

print("="*78)
print("ATTACK 1 — IS 'R o K IS BLIND TO sign(Q)' A RIGGED DISCRIMINATOR?")
print("="*78)
print("  Their R : (r, tau~; 2M, Q) |-> (-r, tau~; -2M, Q)     <- Q untouched BY DEFINITION")
print("  Their K : (r, tau~; 2M, Q) |-> (conj r, conj tau~; 2M, Q)  <- Q untouched, Q real")
print("  So 'R o K cannot see sign(Q)' is TRUE THE MOMENT THE MAPS ARE WRITTEN DOWN.")
print("  Rigged-discriminator check: COULD THIS TEST HAVE RETURNED 'R o K SEES Q'?  NO.")
print()
print("  >> BUT IT SURVIVES, and the reason matters: the maps are not DEFINED without Q")
print("     by choice -- they are the geometry's own. R is a substrate isometry")
print("     (diag(1,1,-1,1,1,1) in O(5,1)); K is complex conjugation of cosmic time.")
print("     NEITHER HAS ANYWHERE TO PUT A Q. The absence is structural, not stipulated.")
print("     A test whose answer is forced BY THE OBJECT is not rigged; a test whose")
print("     answer is forced BY THE QUESTION is. This is the first kind.")
print("  VERDICT: not rigged. But it is a WEAK test -- it re-reads a definition. The")
print("  strong test is attack 2, which their receipt does not run.")

print()
print("="*78)
print("ATTACK 2 — THE HOLE: THEY NEVER TEST THE POTENTIAL. And the potential is exactly")
print("           where the fork they warn about went wrong.")
print("="*78)
r, Q, M, alpha = sp.symbols('r Q M alpha', real=True)
At = Q/r
print(f"  Their receipt tests: the bead relation, and f_metric = 1 - 2M/r + Q^2/r^2 - r^2/a^2.")
print(f"  It NEVER tests A_t = Q/r -- the one object in the theory that is LINEAR in Q.")
print()
print(f"  A_t = Q/r   under r -> -r :   {sp.simplify(At.subs(r,-r))}      ODD -- IT FLIPS.")
print("  So under R the METRIC is untouched (Q^2) while the POTENTIAL REVERSES. A reader")
print("  who notices this has an apparent counterexample to 'R o K is blind to Q' -- and")
print("  the receipt has NO ANSWER, because it never looked.")
print()
print("  ** THIS IS THE FORK'S ROAD, AND THEIR OWN WARNING NAMES IT ** -- 'a fork")
print("     over-closed to C is fully geometric, resting on A_t = Q/r being R-odd'. Their")
print("     A3 avoids that conclusion, but it avoids it BY NOT LOOKING, not by refuting it.")
print("     An unexamined counterexample is not a defeated one.")

print()
print("="*78)
print("ATTACK 3 — SO DOES THE POTENTIAL BREAK THEIR RESULT? Work it.")
print("="*78)
print("  The conjugate branch DOES read as charge -Q, and not as a chart artifact")
print("  (charge_faultline.py): the areal 2-spheres have physical radius |r| on both")
print("  branches, but d/dr points OUTWARD at r>0 and INWARD at r<0, so the same even")
print("  component F_tr = -Q/r^2 is an outward field there and an INWARD field here.")
print("  An observer on the conjugate branch, measuring E against their own outward,")
print("  INFERS -Q. That is physical.")
print()
print("  SO WHY DOESN'T IT BREAK 'BLIND TO Q'?  Because of what R is:")
print("     C is INTERNAL   : charge Q solution -> charge -Q solution, SAME POINT.")
print("                       Same place, different world.")
print("     R is SPACETIME  : point -> another point of the SAME solution.")
print("                       Same world, different place.")
print("  R does not flip the charge. R CARRIES YOU TO WHERE THE SAME CHARGE READS AS ITS")
print("  OPPOSITE. The parameter Q is untouched -- their receipt is right -- and the")
print("  READING flips -- my remark is right -- and these are not in conflict, because")
print("  ** THE AGREEMENT IS OF READINGS, NOT OF OPERATIONS. **")
print()
print("  >> THEIR CONCLUSION SURVIVES, AND MY FINDING STRENGTHENS IT: the potential's")
print("     flip is the sharpest available demonstration of WHY R o K is only the")
print("     KINEMATIC shadow. The geometry can RELOCATE you to the opposite sign; it")
print("     cannot CONJUGATE the sign where you stand. Relocation is not conjugation.")
print("     That is a POSITIVE argument for their horn, and it is one they do not have.")

print()
print("="*78)
print("ATTACK 4 — IS ANY REAL SLICE SMUGGLED IN?")
print("="*78)
rng = np.random.default_rng(11)
bad = 0
for _ in range(400):
    tau = complex(rng.normal(), rng.normal())          # GENUINELY complex tau~
    twoM = rng.uniform(0.05, 2.0)
    val = twoM*a**2*np.sinh(1.5*tau)**2
    for k in range(3):                                  # all three cube roots: complex r
        rr = (abs(val)**(1/3))*np.exp(1j*(np.angle(val)+2*np.pi*k)/3)
        if abs(bead(rr, tau, twoM)) > 1e-8: bad += 1
        # R o K on a genuinely complex point
        rk_r, rk_tau, rk_M = -np.conj(rr), np.conj(tau), -twoM
        if abs(bead(rk_r, rk_tau, rk_M)) > 1e-8: bad += 1
print(f"  400 random points, tau~ complex, r complex (all 3 sheets), R o K applied:")
print(f"  bead residual violations: {bad}   -> {'CLEAN' if bad==0 else 'FAILS'}")
print("  Their maps are applied to genuinely complex (r, tau~). NO real slice is smuggled.")
print("  And species=sign(r) is NOT used anywhere in the factorization argument -- which")
print("  is correct, since it is undefined off the real-r slice ([6*]'s own constraint).")

print()
print("="*78)
print("VERDICT ON THEIR A3")
print("="*78)
print("  * Attack 1 (rigged?)      -> SURVIVES. The absence of Q is structural, not")
print("                               stipulated. But the test is weak: it re-reads a")
print("                               definition rather than probing the object.")
print("  * Attack 2 (the hole)     -> LANDS. The receipt never tests A_t, the only object")
print("                               linear in Q, and so never meets the apparent")
print("                               counterexample its own warning names.")
print("  * Attack 3 (does it break?)-> NO. And the missing piece ARGUES FOR their horn:")
print("                               relocation is not conjugation.")
print("  * Attack 4 (real slice?)  -> SURVIVES, cleanly. Genuinely complex on both axes.")
print()
print("  >> A3 HOLDS, AND ITS CONCLUSION IS RIGHT: the geometric composite is C's")
print("     KINEMATIC SHADOW; only the electric-charge sign closes from the field.")
print("     ** MY A7 CLOSES ON IT. ** The held-open question is answered, on the")
print("     conservative horn I was holding it open for.")
print("  >> ONE THING OWED: their A3 needs the potential test -- not because it changes")
print("     the answer, but because without it the result rests on an ABSENCE ('we found")
print("     no Q in the maps') where a POSITIVE argument is available ('the geometry")
print("     relocates; it does not conjugate'). An argument from a gap is weaker than the")
print("     same conclusion from a mechanism, and the mechanism is in hand.")
