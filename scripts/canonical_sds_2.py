# RETRACTED (r147). This script solved R(T)=alpha*cosh(T/alpha), which is PURE de Sitter
# (M=0) -- the fundamental REPRESENTATION/substrate, NOT the ontological layer S_t. The layer
# is the closed NARIAI member (M != 0), whose matter is the bend (vision §5: "the closed-S^3
# Nariai model is the right one"). It also re-posed a "dust-free deparametrization [reach]",
# re-importing the standard-QG demand for an internal clock that the selection dissolves
# (there is no knot; the deparametrization is standard, the move is the selection). Kept for
# audit only; do NOT build on. See notebook v2 §3 (r147 rework).
import sympy as sp

print("="*78)
print("SdS canonical quantization — STEP 2: the dissolution made concrete on the")
print("ONTOLOGICAL object (closed-cosh substrate, synchronous cosmic time), and the")
print("precise statement of what is genuinely open. Grounded in: operator paper")
print("sec:cosmology/sec:synchronous; cosmology paper canonical remark (Axiom-level).")
print("="*78)

T, al, R, P, N, Lam = sp.symbols('T alpha R P N Lambda', positive=True)

print("""
[0] TWO READINGS OF ONE GEOMETRY (operator paper, read first-hand):
    - FLAT comoving (E=1 / Painleve-Gullstrand): constant-tau slices are flat;
      gives flat-LCDM r(tau)=(2M a^2)^{1/3} sinh^{2/3}(3 tau/2a). This is the
      DERIVATIVE/representational reading. (= Step 1's H_c lived here.)
    - CLOSED synchronous (the second ruling B / horospheres): the substrate
      metric R(T)=alpha cosh(T/alpha), never below the throat alpha, NO Big Bang.
      This is the ONTOLOGICAL layer S_t in its own synchronous cosmic time T.
    Non-synchronous to each other; SAME geometry. The layer S_t (what EXISTS) is
    the closed evolving 3-sphere; flat-LCDM is its comoving projection.
""")

# --- closed-FLRW minisuperspace, computed (k=+1 unit 3-sphere) ---
# ds^2 = -N^2 dT^2 + R^2 dOmega_3^2 ; reduced EH+Lambda action.
print("[1] Closed-FLRW minisuperspace reduced from EH+Lambda (k=+1):")
a = sp.Function('a')
# reduced Lagrangian (standard, units 8piG=1, 3-sphere vol 2pi^2 absorbed):
# L = 3*( -R Rdot^2/N + N R - (Lam/3) N R^3 ) ; vary N -> Hamiltonian constraint
Rd = sp.symbols('Rdot', real=True)
L = 3*( -R*Rd**2/N + N*R - (Lam/3)*N*R**3 )
# momentum conj to R: p_R = dL/dRdot
pR = sp.diff(L, Rd)
print("    p_R =", sp.simplify(pR), "  => Rdot =", sp.simplify(sp.solve(sp.Eq(pR,P),Rd)[0]))
Rdot_of_P = sp.solve(sp.Eq(pR,P),Rd)[0]
# Hamiltonian constraint from varying N (set dL/dN = 0):
dLdN = sp.diff(L, N)
print("    Constraint dL/dN = 0 :", sp.simplify(dLdN), "= 0")
# this is the Friedmann constraint; solve for (Rdot/R)^2:
fried = sp.solve(dLdN, Rd**2)
print("    => Rdot^2 =", sp.simplify(fried[0]), "   i.e. (Rdot/R)^2 = Lambda/3 - 1/R^2")

print("\n[2] Verify the substrate solution R(T)=alpha cosh(T/alpha), Lambda=3/alpha^2:")
Rsol = al*sp.cosh(T/al)
H2 = sp.simplify(sp.diff(Rsol,T)**2/Rsol**2)            # (Rdot/R)^2
target = sp.simplify(Lam/3 - 1/Rsol**2).subs(Lam, 3/al**2)
print("    (Rdot/R)^2 =", H2)
print("    Lambda/3 - 1/R^2 (Lambda=3/a^2) =", sp.simplify(target))
print("    difference =", sp.simplify(H2 - target), "   (0 => closed de Sitter exact)")
print("    R_min = R(0) = alpha  (never contracts below the throat; no Big Bang).")

# --- Hamiltonian constraint in canonical form, synchronous gauge N=1 ---
print("\n[3] Canonical constraint and the DISSOLUTION (cosmology paper, line 171):")
# H_perp ~ 0 is the Friedmann constraint above. In synchronous gauge N=1, T=cosmic time.
print("""    H_perp(R,P) ~ 0  IS the Friedmann constraint [1].  Two readings of it:
    (block)  M is the existent => T is gauge, no dT in the quantum eqn =>
             H_perp^hat Psi = 0  (frozen Wheeler-DeWitt, the 'problem of time').
    (layer)  S_t is the existent, T its real ordering (N=1: dtau=dT the metrical
             advance). The SAME H_perp, read along the real cosmic time T, generates
             the layer's advance R(T): i d/dT Psi = H_perp^hat Psi, unitary.
    'Frozen constraint and true Hamiltonian are the same canonical content under two
     readings, differing only in whether the manifold is granted existence.'
    => the dissolution is ONTOLOGICAL (a category error removed), not a new operation.
""")

print("="*78)
print("WHAT IS ACTUALLY OPEN (the genuine [reach], stated precisely — not manufactured):")
print("="*78)
print("""
 (a) Dust-free realization on the ONTOLOGICAL object. ADM-7 made the deparametrization
     concrete with a Brown-Kuchar DUST clock on flat-FLRW; the layer reading says no
     clock FIELD is needed (cosmic time T is the external ontological ordering). But in
     PURE FLRW minisuperspace the scale R is the only DOF, so 'deparametrize along T'
     has no internal clock variable to solve the constraint for. The precise open
     question: what carries the deparametrization on the ontological object without an
     added field -- the matter bend (the M/r term, real in CR) as the physical clock,
     or the ontological T as a genuine external parameter the formalism must be rebuilt
     to carry? The dissolution says it MUST work; the dust-free FORM is not yet written.

 (b) Flat<->closed bridge. Step 1 (flat comoving H_c, areal radius r) and Step 2 (closed
     synchronous, R(T)) are the same geometry non-synchronously sliced. 'Same canonical
     content under two readings' should be exhibited as an explicit canonical transform
     between them (the non-synchrony tau~ = tau + chi is the seam). Not yet done.

 (c) Quantization details on the closed object: ordering of P^2, self-adjointness of
     H_perp^hat on R in [alpha, inf) (note: domain starts at the throat alpha, not 0 --
     the boundary is the regular throat, a feature, not a singularity to resolve), and
     the S_3 description groupoid as a GAUGE symmetry the Hilbert space must represent
     ('S_3 on a spectrum' stays dead).

 Status: the dissolution is the corpus's RESOLUTION (ontological, line 171; ADM-7 the
 dust-clock proof-of-concept). The dust-free canonical realization on the closed
 ontological object is [reach] -- ready-in-principle, not done. No finished H_phys is
 claimed here; (a) is the next computation.
""")
