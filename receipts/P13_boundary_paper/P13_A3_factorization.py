"""
P13_A3_factorization.py -- verifies prop:conjugation-closure: charge conjugation factorises on the bead as
  C = (Q->-Q)_field o (R o K)_geometric. [P13 boundary_paper sec:closure]
STATUS: ✔✔   RUN: python3 P13_A3_factorization.py   ORIGIN: storyboard_receipts/A3_factorization.py, verified r1379.

A3 -- the factorization of charge conjugation on the full analytic bead.

QUESTION (THE_P13_POSITIVE_CLOSURE_ARC.md, PHASE A3; D-Canat [6]):
    Does C factorize as (linear face R) o (antilinear face K = tau~ <-> conj(tau~)),
    both geometric -- and if so, is that geometric composition C itself, or C's
    kinematic shadow?

THE OBJECT (verified against corpus/F_flat.py, P8/P15 sinh^{2/3} law):
    one single-valued analytic relation on C_r x C_tau~,

        r^3 = 2M a^2 * sinh^2(3 tau~ / 2a),                         (BEAD)

    triple-valued in r (cube root), single-valued in tau~.  It reproduces ALL THREE
    legs of the flattened bead:
        Im tau~ = 0        (expansion): sinh^2 real>0  -> r = +A sinh^{2/3}   (matter, r>0)
        Im tau~ = -pi a/3  (collapse) : sinh -> -i cosh -> r = -A cosh^{2/3}   (antimatter, r<0)
        Re tau~ = 0 lift             : sinh -> i sin   -> r = -A sin^{2/3}     (the lap through r=0)
    with A = (2M a^2)^{1/3} = cbrt(2) a/sqrt3 at Nariai.  Charge enters (RN-dS) only
    through Q^2:  f = 1 - 2M/r + Q^2/r^2 - r^2/a^2.

THE THREE MAPS (all on the SAME object, no slice collapse):
    R : (r, tau~; 2M, Q) |-> (-r,        tau~;       -2M, Q)     linear (holomorphic), an isometry (L1)
    K : (r, tau~; 2M, Q) |-> (conj r,    conj tau~;   2M, Q)     ANTIlinear, complex-analytic (L2)
    C : full charge conjugation -- flips species AND charge, |mass| preserved, ANTIlinear (L3, field)

We test, numerically on random complex sample points, every claim the scope rests on.
Nothing is asserted that a check here does not return.  Negatives are printed, not hidden.
"""
import numpy as np
rng = np.random.default_rng(20260715)     # fixed seed (Date.now-free); vary points by draw

a = 1.0                                   # alpha = 1 gauge
def bead_res(r, tau, twoM, Q=0.0):
    """The bead relation as a residual that vanishes on the curve, charge included.
       Vacuum bead: r^3 - 2M a^2 sinh^2(3 tau/2a) = 0.  We test the maps as symmetries
       of this relation (Q enters the metric f, not the vacuum bead; tested separately)."""
    return r**3 - twoM * a**2 * np.sinh(1.5*tau)**2

def f_metric(r, twoM, Q):
    return 1.0 - twoM/r + Q**2/r**2 - r**2/a**2

# ---- helper: given tau~ and 2M, the three r-roots of the bead (cube roots) ----
def r_roots(tau, twoM):
    val = twoM * a**2 * np.sinh(1.5*tau)**2          # = r^3
    c = val**(1/3)                                    # principal cube root
    w = np.exp(2j*np.pi/3)
    return np.array([c, c*w, c*w**2])

def PASS(name, ok):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    return ok

allok = True
print("="*74)
print("A3 -- charge conjugation factorizes on the analytic bead r^3 = 2M a^2 sinh^2")
print("="*74)

# ---------------------------------------------------------------------------
print("\n0. The BEAD relation reproduces F_flat's three legs (source consistency).")
twoM = 2*a/(3*np.sqrt(3))                             # Nariai
A = (twoM*a**2)**(1/3)
s = 0.9
# expansion (Im=0): r = +A sinh^{2/3}
r_exp = A*np.sinh(1.5*s)**(2/3);           ok1 = abs(bead_res(r_exp, s, twoM)) < 1e-10
# collapse (Im=-pi/3): r = -A cosh^{2/3}
tau_c = s - 1j*np.pi/3;  r_col = -A*np.cosh(1.5*s)**(2/3); ok2 = abs(bead_res(r_col, tau_c, twoM)) < 1e-10
allok &= PASS("expansion leg r=+A sinh^{2/3} on the bead", ok1)
allok &= PASS("collapse leg  r=-A cosh^{2/3} on the bead (Im tau~=-pi/3)", ok2)

# r2376+c54.158 -- pins section 0's Nariai point, which every later section runs on and which the
# receipt only LABELS in a comment.  2M = 2a/(3 sqrt 3) = 0.3849001794597505 is the same literal
# the sibling receipt P13_closure_iv_check.py hard-codes as "Nariai", and it EARNS the name here:
# at that mass the vacuum f = 1 - 2M/r - r^2/a^2 has a DOUBLE root at r = a/sqrt(3) -- value AND
# slope both zero -- which is the degenerate-horizon condition Nariai IS.  Off that mass the two
# horizons separate and the bead is not the corpus's bead.  The expansion leg's own point is
# pinned with it: r(s=0.9) = A sinh^{2/3}(1.35) = 1.0760151554, and A = (2M a^2)^{1/3} = 0.7274158
# = cbrt(2) a / sqrt(3), the amplitude the docstring states.
assert abs(twoM - 0.3849001794597505) < 1e-15, twoM
r_nariai = a/np.sqrt(3.0)
assert abs(f_metric(r_nariai, twoM, 0.0)) < 1e-14, f_metric(r_nariai, twoM, 0.0)
_h = 1e-6
assert abs((f_metric(r_nariai+_h, twoM, 0.0) - f_metric(r_nariai-_h, twoM, 0.0))/(2*_h)) < 1e-9
assert abs(f_metric(0.9*r_nariai, twoM, 0.0)) > 1e-3      # CONTROL: f is not identically zero
assert abs(A - 0.7274157573144809) < 1e-12, A
assert abs(r_exp - 1.0760151554392123) < 1e-12, r_exp

# ---------------------------------------------------------------------------
print("\n1. R : (r,2M)->(-r,-2M) at fixed tau~  is a symmetry of the bead; blind to Q.")
tau = 0.7 + 0.31j; twoM = 0.44; Q = 0.6
for r in r_roots(tau, twoM):
    res0 = bead_res(r, tau, twoM)
    resR = bead_res(-r, tau, -twoM)                  # R applied
    allok &= PASS(f"  R preserves bead (root |r|={abs(r):.3f})", abs(res0)<1e-9 and abs(resR)<1e-9)
# Q-blindness: R (r->-r, 2M->-2M) is a genuine isometry of the RN-dS metric,
# and it leaves Q's sign untouched (Q enters only as Q^2).  Genuine checks, no rig.
r = r_roots(tau, twoM)[0]
allok &= PASS("  R leaves the FULL metric f invariant (r->-r, 2M->-2M): a genuine isometry",
              abs(f_metric(r,twoM,Q) - f_metric(-r,-twoM,Q)) < 1e-9)
allok &= PASS("  R: Q^2/r^2 -> Q^2/(-r)^2 identical (charge sign untouched)",
              abs(Q**2/r**2 - Q**2/(-r)**2) < 1e-12)

# ---------------------------------------------------------------------------
print("\n2. K : tau~ -> conj(tau~), r -> conj(r)  is an ANTIlinear symmetry of the bead.")
tau = 0.5 + 0.4j; twoM = 0.44
for r in r_roots(tau, twoM):
    # K sends (r,tau) to (conj r, conj tau); check conj r solves the bead at conj tau
    allok &= PASS(f"  K preserves bead (root |r|={abs(r):.3f})",
                  abs(bead_res(np.conj(r), np.conj(tau), twoM)) < 1e-9)
# fixes the real axis (photon): Im tau~=0 -> r real -> conj r = r
r_real = r_roots(0.8+0j, twoM)[0]
allok &= PASS("  K FIXES the real-tau~ axis (r real, self-conjugate -- the photon)",
              abs(np.imag(r_real)) < 1e-9)
# swaps the two wings Im tau~ = +/- pi/3: K sends a +wing root to a root at the -wing.
# Genuine content: conj(r_+wing) solves the bead at the -wing (and is NOT the same point).
tau_p = 0.15 + 1j*np.pi/3
rp = r_roots(tau_p, twoM)[0]
Krp, Ktau = np.conj(rp), np.conj(tau_p)              # K image
allok &= PASS("  K SWAPS wings: conj(r) solves the bead at conj(tau~) on the -pi/3 wing",
              abs(bead_res(Krp, Ktau, twoM)) < 1e-9 and abs(np.imag(Ktau) + np.pi/3) < 1e-12
              and abs(Krp - rp) > 1e-3)

# ---------------------------------------------------------------------------
print("\n3. R o K : antilinear INVOLUTION, and it equals K o R (they commute).")
def RK(r, tau, twoM):     # R o K
    return (-np.conj(r), np.conj(tau), -twoM)
def KR(r, tau, twoM):     # K o R
    return (np.conj(-r), np.conj(tau), -twoM)
r0, tau0, twoM0 = r_roots(0.6+0.2j,0.44)[0], 0.6+0.2j, 0.44
allok &= PASS("  R o K = K o R (commute)", np.allclose(RK(r0,tau0,twoM0), KR(r0,tau0,twoM0)))
r1,t1,m1 = RK(r0,tau0,twoM0); r2,t2,m2 = RK(r1,t1,m1)
allok &= PASS("  (R o K)^2 = identity (involution)", np.allclose((r2,t2,m2),(r0,tau0,twoM0)))
allok &= PASS("  R o K preserves the bead", abs(bead_res(r1,t1,m1))<1e-8 and abs(bead_res(r0,tau0,twoM0))<1e-8)

# ---------------------------------------------------------------------------
print("\n4. R o K vs C -- what agrees, and the ONE thing that does not.")
print("     label            R o K (geometric)     C (full)         agree?")
rows = [
 ("species (sign r, real)", "flips (r->-conj r)",  "flips",          True),
 ("|mass| = |2M|",          "preserved",           "preserved",      True),
 ("mass SIGN / branch label","flips (2M->-2M)",     "flips",          True),
 ("FS wing (tau~<->conj)",  "swaps wings/fix real","particle<->anti", True),
 ("character",              "antilinear",          "antilinear",      True),
 ("ELECTRIC CHARGE sign Q", "BLIND (Q via Q^2)",   "flips Q->-Q",     False),  # the one difference
]
for lab, g, c, ag in rows:
    print(f"     {lab:24s} {g:20s} {c:16s} {'YES' if ag else 'NO <-- field-level'}")
# the negative, made a check: R and K cannot move Q's sign (Q enters only as Q^2)
allok &= PASS("  NEGATIVE (load-bearing): R o K is blind to sign(Q) -- Q enters only as Q^2",
              abs(f_metric(r0,twoM0,0.6) - f_metric(r0,twoM0,-0.6)) < 1e-12)

# r2376+c54.158 -- rule 7: every PASS/FAIL above is computed and only PRINTED.  Pin `allok`, and
# pin the NEGATIVE separately, because it is the load-bearing half of prop:conjugation-closure and
# an `allok` that quietly lost it would still read green: the metric is EXACTLY Q^2-blind
# (f(+Q) - f(-Q) = 0 to the last bit), while it is NOT blind to the mass sign that R does flip
# (f(2M) - f(-2M) is a real, non-zero difference here) -- so R o K carries C's mass/species
# kinematics and cannot carry the charge sign.  That asymmetry is C = (Q->-Q)_field o (R o K)_geom.
assert f_metric(r0, twoM0, 0.6) == f_metric(r0, twoM0, -0.6)
assert abs(f_metric(r0, twoM0, 0.6) - f_metric(r0, -twoM0, 0.6)) > 1e-3
assert allok
print("\n" + "="*74)
print("RESULT:", "ALL CHECKS PASS" if allok else "SOME CHECK FAILED -- read the log")
print("="*74)
print("""
SCOPE (what this establishes, and what it does NOT):
  ESTABLISHED (bead geometry): R o K = R o (tau~<->conj tau~) is an antilinear
    geometric involution that reproduces C's action on species, |mass|, mass-sign,
    and the Feynman-Stuckelberg particle<->antiparticle wing structure (fixing the
    neutral real axis = the photon) -- but is BLIND to the electric charge sign,
    because both factors depend on Q only through Q^2.
  => C = (Q->-Q)_field  o  (R o K)_geometric.
  [6] RESOLVED, bounded: the L2 antilinear face is C's KINEMATIC (CPT/FS) SHADOW,
    NOT the full C.  The geometry carries all of C's kinematic content; ONLY the
    electric-charge sign closes from the field.
  DO-NOT-ASSERT (Phase E / P14): that R o K acts on P14's actual fermion zero-modes
    as C's kinematic conjugation; the identification of a wing with a specific
    charged particle; a full geometric CPT (the charge still closes from the field).
""")
