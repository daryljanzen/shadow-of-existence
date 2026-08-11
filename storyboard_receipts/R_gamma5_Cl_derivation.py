"""
R_gamma5_Cl_derivation.py  --  the MISSING computation (built r1325, Arthur).

P12 sec:strata/§240 and P14 Prop:wall assert: the transverse cut-normal reflection R
(R = diag(1,1,-1,1,1,1) in O(5,1), fixing the four spacetime legs, flipping the fifth,
substrate-transverse direction) acts on the cut's natural spinor as the chirality operator
gamma^5 ITSELF -- GRADING chirality -- "the exchange reading excluded by explicit computation."
That computation (cited as r703 Cl(1,5)) was NOT FOUND in the bundle; conjugation_parity.py
checks it with comm(g5,g5) (a tautology) and R_eq_PT.py takes R=gamma^5 as canon. So the
load-bearing identification on which count=3 rests was ASSERTED, not derived. Here it is derived.

THE NON-CIRCULAR CORE (why this is a derivation, not a relabeling):
  dS_5 (5-dim, spin, 4-component spinors) has tangent Clifford algebra Cl(1,4): FIVE anticommuting
  generators.  Four are the cut's spacetime legs (the 4D Dirac gammas g0..g3).  The FIFTH -- the
  substrate-transverse / cut-normal direction R reflects -- is NOT free: in any 4-component irrep of
  the 5D algebra the fifth generator is forced to equal (up to phase) the product g0 g1 g2 g3, i.e.
  the 4D CHIRALITY OPERATOR.  So "reflect the transverse direction" = "act by the chirality operator"
  is a THEOREM of the algebra, not a choice.  A reflection GRADES iff its Pin element commutes with
  the chirality operator; the transverse generator (= chirality op) commutes with itself => GRADES.
  The in-cut reflections T=g0, P=g1g2g3 anticommute with it => FLIP.  The "exchange reading" is what a
  FLIP (off-diagonal, chirality-swapping) reflection does; R is transverse => graded => not exchange.
"""
import numpy as np
np.set_printoptions(precision=2, suppress=True)

def anticomm(A,B): return A@B + B@A
def comm(A,B):     return A@B - B@A
def is0(M):        return np.allclose(M,0)
def isI(M):        return np.allclose(M,np.eye(M.shape[0]))

results = {}
def check(tag, cond):
    results[tag]=bool(cond); print(f"  [{'PASS' if cond else 'FAIL'}] {tag}")

for repname, build in [("Dirac", "dirac"), ("Weyl", "weyl")]:
    print("="*78); print(f"REP = {repname}"); print("="*78)
    I2=np.eye(2,dtype=complex); Z=np.zeros((2,2),complex)
    sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.array([[1,0],[0,-1]],complex)
    blk=lambda a,b,c,d: np.block([[a,b],[c,d]])
    if build=="dirac":
        g0=blk(I2,Z,Z,-I2); g1=blk(Z,sx,-sx,Z); g2=blk(Z,sy,-sy,Z); g3=blk(Z,sz,-sz,Z)
    else:  # Weyl / chiral
        g0=blk(Z,I2,I2,Z); g1=blk(Z,sx,-sx,Z); g2=blk(Z,sy,-sy,Z); g3=blk(Z,sz,-sz,Z)
    g=[g0,g1,g2,g3]; eta=np.diag([1,-1,-1,-1]).astype(complex)   # mostly-minus 4D

    # 4D Clifford relations
    cl4 = all(np.allclose(anticomm(g[m],g[n]), 2*eta[m,n]*np.eye(4)) for m in range(4) for n in range(4))
    check("g0..g3 satisfy the 4D Clifford algebra {g^m,g^n}=2 eta^{mn}", cl4)

    # the chirality operator, built from the four legs
    chi = 1j*g0@g1@g2@g3
    check("chi := i g0g1g2g3 squares to +I (chirality involution)", isI(chi@chi))

    # --- THE NON-CIRCULAR CORE: the fifth (transverse) generator is FORCED to be chi ------------
    # Demand a 5th generator G5: anticommutes with all g0..g3 and squares to +/-I.  Show any such G5
    # is proportional to chi (so the transverse Clifford generator = the chirality operator, forced).
    anticommutes_all = all(is0(anticomm(chi,g[m])) for m in range(4))
    check("chi anticommutes with every leg g0..g3  => chi is a valid 5th Cl(1,4) generator", anticommutes_all)
    # forced-ness (GENUINE uniqueness, not a spot-check): the space of 4x4 matrices X with {X,g^m}=0 for
    # ALL four legs is the null space of the stacked anticommutator maps.  vec column-major:
    #   vec(g X) = (I kron g) vec X ,  vec(X g) = (g^T kron I) vec X.
    def anti_map(gm): return np.kron(np.eye(4), gm) + np.kron(gm.T, np.eye(4))
    Amat = np.vstack([anti_map(g[m]) for m in range(4)])          # (64 x 16)
    s = np.linalg.svd(Amat, compute_uv=False)
    nulldim = int(np.sum(s < 1e-9))
    check("the space of operators anticommuting with ALL four legs is exactly 1-DIMENSIONAL", nulldim==1)
    _,_,vh = np.linalg.svd(Amat)
    Xnull = vh[-1].reshape(4,4, order='F')
    dep = np.linalg.matrix_rank(np.vstack([chi.flatten(), Xnull.flatten()]), tol=1e-9)==1
    check("that 1-dim space is spanned by chi => the transverse generator is FORCED to be gamma^5 (not chosen)",
          nulldim==1 and dep)

    # --- R = transverse reflection, via the Pin twisted conjugation  v -> - Gn v Gn^{-1} ----------
    # R reflects the 5th (transverse) direction, whose generator is Gn = chi.
    Gn = chi; Gninv = np.linalg.inv(Gn)
    def reflect_transverse(v): return -Gn@v@Gninv
    fixes_legs = all(np.allclose(reflect_transverse(g[m]), g[m]) for m in range(4))
    flips_5th  = np.allclose(reflect_transverse(chi), -chi)
    check("twisted conj by chi FIXES the four legs g0..g3 (R fixes the spacetime legs)", fixes_legs)
    check("twisted conj by chi FLIPS the 5th/transverse direction (R reflects the cut-normal)", flips_5th)
    print("     => the reflection 'fix 4 legs, flip transverse' has Pin element  R = chi = gamma^5.")

    # --- does R GRADE or EXCHANGE chirality? -----------------------------------------------------
    R = chi
    grades = is0(comm(R, chi))          # commutes with chirality  => preserves L/R eigenspaces
    exchanges = is0(anticomm(R, chi))   # anticommutes             => swaps L<->R (the "exchange reading")
    check("R commutes with the chirality operator  => R GRADES chirality", grades)
    check("R does NOT anticommute with chirality  => R is NOT an exchange (exchange reading EXCLUDED)",
          not exchanges)
    evals = np.linalg.eigvalsh(R if np.allclose(R,R.conj().T) else (R+R.conj().T)/2)
    check("R has eigenvalues +/-1 (it MEASURES chirality, values = chirality)",
          np.allclose(np.sort(np.round(np.linalg.eigvals(R).real)), [-1,-1,1,1]))

    # --- contrast: the IN-CUT reflections T=g0, P=g1g2g3 FLIP (this is what 'exchange' looks like) -
    T = g0; P = g1@g2@g3
    check("contrast: T=g0 (time reflection) ANTICOMMUTES with chi => FLIPS chirality (exchange)",
          is0(anticomm(T,chi)))
    check("contrast: P=g1g2g3 (spatial parity) ANTICOMMUTES with chi => FLIPS chirality (exchange)",
          is0(anticomm(P,chi)))
    # in the Weyl rep the grade-vs-exchange distinction is manifest (diagonal vs off-diagonal):
    if build=="weyl":
        print("     Weyl rep, manifest: chi = diag", np.round(np.diag(chi).real).astype(int),
              "(DIAGONAL => grades)")
        print("     Weyl rep, manifest: g0 is block-off-diagonal (swaps the two Weyl comps => exchange).")
    print()

print("="*78)
allpass = all(results.values())
print("RESULT:", "ALL CHECKS PASS -- R = gamma^5, GRADES chirality, exchange reading EXCLUDED, DERIVED."
      if allpass else "SOME CHECKS FAILED -- see above.")
print("""  The transverse cut-normal reflection's Pin element is the fifth Cl(1,4) generator, which is
  FORCED to be the chirality operator gamma^5; it commutes with chirality (grades, eigenvalues +/-1),
  whereas the in-cut reflections T,P anticommute (flip).  So 'R acts on the cut spinor as gamma^5,
  grading, exchange excluded' is now DERIVED from the Clifford structure, in two independent reps --
  no longer asserted.  (The 6D R=diag(1,1,-1,1,1,1) in O(5,1) restricts, at the fixed cut, to exactly
  this transverse tangent reflection; the ruling-swap face is the same reflection and is the next
  sub-line to render explicitly in the 6D embedding.)""")
print("="*78)
