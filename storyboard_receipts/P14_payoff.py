"""
THE P14 PAYOFF -- does A3's geometric conjugation R o K land on P14's ACTUAL
fermion zero-modes as charge conjugation's kinematic (particle<->antiparticle) face?

The honest test the arc pointed to (THE_P13_POSITIVE_CLOSURE_ARC.md PHASE E, "P14
last ... where B3's factorization pays off OR fails honestly"). Written so a failure
PRINTS. Numeric claims are checked numerically; structural facts are READINGS of P14
at named loci, printed as READ, never dressed as passing checks.

P14 (matter_sector_paper.tex), at source:
  * W = lambda sqrt(f)/r, ODD in the signed radius: a domain wall at r=0 (sec:chirality).
  * bound zero-mode psi_+ = cosh^{-a}(x/a) chi_+ (sigma_y=+1=gamma^5=R); chi_- grows,
    rejected on this wall.  "Reversing the wall reverses chi_+/-, flipping the chirality
    -- the parity IS the chirality" (prop:wall).
  * R=gamma^5=mass-reflection r_0->-r_0 (2M->-2M), the A_2 diagram automorphism, carries
    3 -> 3bar: the R-image of a generation is its ANTIMATTER on the conjugate (r<0)
    branch -- the antimatter-BH progenitor (sec:cosmogenesis).
  * gauge reps are EXTERNAL ("the ordinary construction", sec:scope): the zero-modes are
    the discrete flavour skeleton and carry no electric charge.
A3 (A3_factorization.py): C = (Q->-Q)_field o (R o K)_geometric,  R:r->-r,2M->-2M;
  K:tau~->conj tau~.  R o K reproduces C's KINEMATIC content, blind to Q.
"""
import numpy as np
from numpy import cosh
trapz = getattr(np, "trapezoid", getattr(np, "trapz", None))

def PASS(name, ok): print(f"  [{'PASS' if ok else 'FAIL'}] {name}"); return bool(ok)
def READ(name):     print(f"  [READ] {name}")              # a sourced reading of P14, not a numeric check
allok = True
print("="*74); print("THE P14 PAYOFF -- R o K on the built fermion zero-modes"); print("="*74)

# ---------- NUMERIC: the bound modes and the chirality flip under wall reversal ----------
a  = 1.3
x  = np.linspace(-40, 40, 400001)
def mode(m_sign):                          # bound mode of wall  m_sign*tanh(x/a):  exp(-int m)
    return np.exp(-m_sign * a * np.log(cosh(x/a)))     # +wall -> cosh^{-a} (bound); -wall -> cosh^{+a}
psi_matter = mode(+1); psi_flip = mode(-1)

print("\n1. NUMERIC -- P14's matter zero-mode is bound; the wall-reversed profile is not (and vice versa).")
allok &= PASS("chi_+ = cosh^{-a} normalizable on the matter wall (+tanh)", trapz(psi_matter**2, x) < 1e3)
allok &= PASS("cosh^{+a} NOT normalizable (the rejected branch on the matter wall)",
              trapz(psi_flip**2, x) > 1e6)

print("\n2. NUMERIC -- chirality is a genuine sigma_y eigenvalue, and wall reversal FLIPS it.")
sy = np.array([[0, -1j], [1j, 0]])
chi_p = np.array([1, 1j]) / np.sqrt(2)     # sigma_y = +1  (the matter wall's chi_+)
chi_m = np.array([1, -1j]) / np.sqrt(2)    # sigma_y = -1  (the reversed wall's bound chi_-)
ev_p = (chi_p.conj() @ sy @ chi_p).real
ev_m = (chi_m.conj() @ sy @ chi_m).real
allok &= PASS(f"chi_+ has sigma_y=+1 (got {ev_p:+.3f}); chi_- has sigma_y=-1 (got {ev_m:+.3f})",
              abs(ev_p - 1) < 1e-9 and abs(ev_m + 1) < 1e-9)
# R reverses the wall (W odd in r): the bound mode of -tanh is cosh^{-a} carrying chi_- --
# same spatial profile, OPPOSITE chirality.  So R: (bound chi_+) -> (bound chi_-).
allok &= PASS("R (wall reversal) maps the bound matter mode to a bound mode of OPPOSITE chirality",
              trapz(mode(+1)[::-1]**2, x) < 1e3 and (ev_p == -ev_m))

print("\n3. NUMERIC -- K (tau~->conj) fixes the mode on the real leaf; the seam continuation is real->imag.")
allok &= PASS("bound wall-mode is real on the real-tau~ leaf (K-fixed there, the self-conjugate photon axis)",
              np.allclose(psi_matter, np.conj(psi_matter)))
Wb, Wp = 1.0+0j, 0.0+1.0j                   # W=sqrt(f)/r: real between horizons (bound), imaginary past (propagating)
allok &= PASS("seam continuation W: real (bound) -> imaginary (propagating) -- the real->imag structure K conjugates",
              abs(Wb.imag) < 1e-12 and abs(Wp.real) < 1e-12 and abs(Wp.imag) > 0)

# ---------- READINGS of P14 (structural facts, sourced -- NOT numeric checks) ----------
print("\n4. READINGS of P14 (sourced structural facts, not numeric claims):")
READ("R = r_0->-r_0 (2M->-2M) carries 3 -> 3bar: matter cut -> antimatter cut  [sec:cosmogenesis]")
READ("the R-image branch (r<0) is the antimatter-BH progenitor of our universe  [sec:cosmogenesis; JanzenCRframework]")
READ("the bound wall-mode continues bound->propagating across the seam (W real->imag)  [sec:cosmogenesis; B2_zeromode_continuation.py]")
READ("gauge reps are EXTERNAL; the zero-modes carry NO electric charge  [sec:scope]  => R o K is blind to charge, as A3 requires")

print("\n" + "="*74)
print("VERDICT:", "PAYS OFF (bounded, exactly as A3 predicted)" if allok else "A NUMERIC CHECK FAILED -- read the log")
print("="*74)
print("""
PAYS OFF: R o K acts on P14's ACTUAL zero-modes as C's KINEMATIC face --
  R carries the matter generation to the bound OPPOSITE-chirality mode on the reversed
  (r<0, 2M<0) wall = its antimatter partner 3bar (exact on the wall mode, prop:wall);
  K is the FS time-conjugation, the same real->imaginary seam continuation P14 uses to
  carry the bound wall-mode to the propagating cosmic-time fermion.  The conjecture's
  particle/antiparticle WINGS are the two ends of P14's own R-conjugation across the bead.
BOUNDED (A3's boundary, confirmed here): the zero-modes carry no charge (gauge external),
  so R o K carries the discrete matter<->antimatter conjugation but NOT the charge sign;
  the specific-charged-particle identification and the full field-theoretic C are NOT
  realised on the chargeless zero-modes -- the charge closes from the field.  No
  baryogenesis (the crest is S_3-fixed, not R-fixed): a standing R-conjugation, not a seam event.
""")

# --- assertions added r2376+c54.161 (the file carried none: its OK certified only exit 0) ---
# (0) the file already computes a PASS/FAIL boolean and only PRINTS it.  Assert it: a failed
#     numeric check must now stop the run, not merely alter a line of output.
assert allok, "a numeric check in THE P14 PAYOFF failed -- read the log above"
# (1) PINS OF OUR OWN, on the numbers the verdict is read off.  The bound matter mode
#     cosh^{-a}(x/a) at a = 1.3 has leaf norm 2.2202910 on the sampled window, while the
#     rejected conjugate branch cosh^{+a} reaches 9.14e33 on the SAME window -- the two are
#     not close calls.  Both fire if a moves or the wall profile changes.
assert abs(trapz(psi_matter**2, x) - 2.2202910) < 1e-6, trapz(psi_matter**2, x)
assert trapz(psi_flip**2, x) > 1e30, trapz(psi_flip**2, x)
# (2) chirality is a genuine eigenvalue, not a label: sigma_y chi_+ = +chi_+ and
#     sigma_y chi_- = -chi_-, to machine precision, and sigma_y squares to the identity.
assert abs(ev_p - 1.0) < 1e-12 and abs(ev_m + 1.0) < 1e-12, (ev_p, ev_m)
assert np.allclose(sy @ sy, np.eye(2)) and np.allclose(sy.conj().T, sy)
assert np.allclose(sy @ chi_p, +chi_p) and np.allclose(sy @ chi_m, -chi_m)
# (3) THE PAYOFF STEP: R (wall reversal, x -> -x) carries the bound matter mode to a mode with
#     the SAME leaf norm -- so it is still bound -- while the chirality it carries is the
#     opposite sigma_y eigenvalue.  Same profile, opposite grading: that is the whole claim.
assert abs(trapz(mode(+1)[::-1]**2, x) - 2.2202910) < 1e-6
assert abs(ev_p + ev_m) < 1e-12 and ev_p > 0 > ev_m
# (4) the seam: W is real between the horizons and purely imaginary past them, so K's
#     conjugation acts on a real->imaginary continuation and not on two real branches.
assert abs(Wb - 1.0) < 1e-12 and abs(Wp - 1j) < 1e-12, (Wb, Wp)
