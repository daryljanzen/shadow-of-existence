"""D-C, WORKED. Is the particle<->antiparticle / charge-conjugation structure sourced by the
geometry, and how does it factor against P13's 'PT geometric, C (and the antiunitary half of T)
field-level'? Settle it, don't narrate it."""
import numpy as np
A=(2/(3*np.sqrt(3)))**(1/3)

# ---------- 1. the tau~ <-> conj(tau~) involution on the bead: what it fixes, what it swaps ----------
def r_of(tau):                       # r along the bead: r^3 = A^3 sinh^2(1.5 tau), real-r branch
    S=np.sinh(1.5*tau)**2
    roots=[A*abs(S)**(1/3)*np.exp(1j*(np.angle(S)+2*np.pi*k)/3) for k in range(3)]
    real=[z.real for z in roots if abs(z.imag)<1e-7]
    return real
print("== tau~ <-> conj(tau~): fixed set and swapped set ==")
for lbl,tau in [("photon (real axis)",0.7+0.0j),
                ("wing -pi/3",  -0.9-1j*np.pi/3),
                ("wing +pi/3",  -0.9+1j*np.pi/3)]:
    rr=r_of(tau); rrc=r_of(np.conj(tau))
    fixed = abs(tau-np.conj(tau))<1e-9
    print(f"  {lbl:20s} tau~=({tau.real:+.2f},{tau.imag/(np.pi/3):+.2f}pi/3)  r={[f'{x:+.2f}' for x in rr]}"
          f"  |  conj-> Im={np.conj(tau).imag/(np.pi/3):+.2f}pi/3  {'FIXED' if fixed else 'swapped to the other wing'}")
print("  => real axis (photon) FIXED = self-conjugate/neutral; the two r<0 wings SWAPPED = particle<->antiparticle.\n")

# ---------- 2. is tau~->conj(tau~) LINEAR or ANTILINEAR?  (the crux P13's argument turns on) ----------
K=lambda z: np.conj(z)
a,b=1.3+0.6j, 2.1-0.9j   # COMPLEX, so the test discriminates
lin_ok  = np.isclose(K(a*(0.4+0.7j)+b*(0.2-0.5j)), a*K(0.4+0.7j)+b*K(0.2-0.5j))          # linear?
anti_ok = np.isclose(K(a*(0.4+0.7j)+b*(0.2-0.5j)), np.conj(a)*K(0.4+0.7j)+np.conj(b)*K(0.2-0.5j))
print("== character of tau~->conj(tau~) ==")
print(f"  satisfies LINEAR K(a x+b y)=a Kx+b Ky ? {lin_ok}    ANTILINEAR K=conj(a)Kx+conj(b)Ky ? {anti_ok}")
print("  => ANTILINEAR. No real-embedding reflection (all LINEAR, det +-1) can reproduce it.")
print("     So the geometry DOES source an antilinear involution -- exactly what P13's")
print("     'every substrate isometry acts linearly' argument does not reach.\n")

# ---------- 3. charged (RN-dS) bead: what r->-r (=R) and Q->-Q do to metric vs potential ----------
def mass_term(rs,M=0.3): return -2*M/rs
def charge_term(rs,Q=0.5): return Q**2/rs**2
def A_t(rs,Q=0.5): return Q/rs
rs=1.7
print("== r->-r (the geometric R) and Q->-Q on the charged bead ==")
print(f"  mass term -2M/r : r->-r sends {mass_term(rs):+.4f} -> {mass_term(-rs):+.4f}   (ODD: flips)")
print(f"  charge term Q^2/r^2: r->-r sends {charge_term(rs):+.4f} -> {charge_term(-rs):+.4f}   (EVEN: fixed)")
print(f"  metric under Q->-Q: charge term {charge_term(rs,0.5):+.4f} -> {charge_term(rs,-0.5):+.4f}  INVARIANT (Q^2) => C-blind to charge SIGN")
print(f"  potential A_t=Q/r under Q->-Q: {A_t(rs,0.5):+.4f} -> {A_t(rs,-0.5):+.4f}  (ODD: flips) => charge SIGN lives in A, field-level")
print()
# ---------- 4. the factorization, stated as the computation forces it ----------
print("== RESULT (forced) ==")
print("  GEOMETRIC, sourced by the substrate/bead:")
print("   (a) linear rep/mass/chirality skeleton: R=gamma^5 (r->-r: 2M odd, 3->3bar, hand-flip), P, T;")
print("   (b) an ANTILINEAR involution tau~->conj(tau~): fixes the neutral photon, swaps the two r<0")
print("       wings = the Feynman-Stueckelberg particle<->antiparticle relation. (2) proves it antilinear.")
print("  NOT geometric, field-level (P13 right): the ELECTRIC CHARGE SIGN Q->-Q -- metric is Q^2-blind,")
print("       the sign lives in A_t=Q/r.")
print("  => P13's 'PT geometric; C AND THE ANTIUNITARY HALF field-level' UNDERSTATES: the antilinear")
print("     (antiunitary) conjugation has a geometric realization on the complex cosmic time (tau~<->conj).")
print("     What stays genuinely field-level is narrower than P13 drew -- ONLY the internal charge Q,")
print("     not the whole antilinear structure. The 'skeleton' the geometry supplies INCLUDES the")
print("     particle/antiparticle (CPT-kinematic) antilinear involution, not just the linear P,T,gamma^5.")
