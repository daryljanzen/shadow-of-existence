"""
R5, ROUTE (b): IS THERE A SPIN-2 OBJECT ON THIS FIGURE AT ALL?  (r1117)

** WHERE THIS QUESTION CAME FROM. ** Route (c) pointed P11's chirality criterion at the bead
and it FAILED A TYPE-CHECK (⊢66): the criterion's input is a SPIN-2 polarization h_+ + i h_x,
transforming as e^{-2i.theta} under a transverse rotation; the bead's r is the areal radius, a
SCALAR, invariant. ** The instrument fit the shape and failed the type. ** So route (b) --
"P11 already has a wave whose energy is the leaf's SHEAR; if a wave can be a bend, ask what
bend these branches are" -- must face the same check, because shear is spin-2 too. Its honest
form is therefore not "what bend are the branches" but:

    ** IS THERE A SPIN-2 OBJECT ON THIS FIGURE AT ALL? **

** AND THERE IS AN OBVIOUS CANDIDATE, WHICH IS WHY THIS IS A TEST AND NOT A FISHING TRIP. **
A symmetric traceless 2x2 tensor has EXACTLY TWO NULL DIRECTIONS, and is determined by them up
to scale -- that is the standard fact underneath h_+ + i h_x. And the substrate is
** DOUBLY RULED: through every point run TWO straight null lines ** (p0 §rulings; ⊢12/⊢13).

    ** So the two rulings at a point are two null directions. Do they define a spin-2 object? **

THE TEST, named before running:
  Q1  build the symmetric traceless tensor whose null directions are the two rulings at a point.
      Does it exist and is it unique up to scale?
  Q2  ** the type-check that killed route (c), run on THIS object: ** does it transform as
      e^{-2i.theta} under a rotation in the plane the two rulings span?
  Q3  if it does -- point P11's criterion at it. Does the polarization plane TURN along a
      ruling, or is it fixed?

** THE PREDICTION, NAMED, AND IT IS A NEGATIVE. ** P11 itself says where chirality onsets:
"the polarized Gowdy edge (residual T^2, one fixed axis) IS STILL ACHIRAL" -- a fixed axis
furnishes a reflection symmetry, parity identifies the helicities, no genuine chirality. ** The
substrate is maximally symmetric and its two ruling families are globally defined; that is as
fixed an axis structure as exists. So I expect a spin-2 object to EXIST and to be ACHIRAL --
fixed polarization, not turning. ** If it turns, the prediction is wrong and that is worth more.

COULD THIS RETURN OTHERWISE? Yes at every step: the tensor either exists or does not; the
transformation law either holds or does not (computed, not asserted); and the turning is read
off a derivative.
"""
import numpy as np

a = 1.0
np.set_printoptions(precision=6, suppress=True)

# ---------------------------------------------------------------- the substrate and its rulings
# -X0^2 + X1^2 + X2^2 = a^2  (the 2+1 slice that carries the overhead figure)
def surface(X0, th):
    R = np.sqrt(a**2 + X0**2)
    return np.array([X0, R*np.cos(th), R*np.sin(th)])

def eta(u, v):
    return -u[0]*v[0] + u[1]*v[1] + u[2]*v[2]

print("="*80)
print("Q1 -- THE TWO RULINGS AT A POINT, AND THE TENSOR THEY DEFINE")
print("="*80)
# at the waist, X0=0, azimuth 0: P = (0, a, 0)
P = surface(0.0, 0.0)
print(f"  take the point P = {P} on the waist.")
# the two rulings through P: straight null lines lying IN the surface.
# parametrise: L(s) = P + s*k must satisfy -X0^2+X1^2+X2^2 = a^2 for all s
# => eta(k,k) = 0  and  eta(P,k) = 0.
# P = (0,a,0):  eta(P,k) = a*k1 = 0 => k1 = 0.  eta(k,k) = -k0^2 + k2^2 = 0 => k2 = ±k0.
k_A = np.array([1.0, 0.0,  1.0])
k_B = np.array([1.0, 0.0, -1.0])
for nm, k in [("A", k_A), ("B", k_B)]:
    print(f"    ruling {nm}: k = {k}   eta(k,k) = {eta(k,k):+.1e}   eta(P,k) = {eta(P,k):+.1e}")
    assert abs(eta(k,k)) < 1e-12 and abs(eta(P,k)) < 1e-12
    for s in [0.5, -1.3, 2.0]:
        Q = P + s*k
        assert abs(eta(Q,Q) - a**2) < 1e-12
    print(f"      and P + s·k stays on the surface for all s: verified")
print("""
  ** Two null directions through P, lying in the surface. That is the double ruling (p0
  §rulings), here in coordinates. ** They span the 2-plane orthogonal to P -- the tangent
  plane -- and in that plane they are the two null directions of its induced Lorentzian metric.""")

# the tangent plane at P, with basis e_t (timelike) and e_x (spacelike)
e_t = np.array([1.0, 0.0, 0.0])          # eta = -1
e_x = np.array([0.0, 0.0, 1.0])          # eta = +1
print(f"\n  tangent basis at P:  e_t = {e_t} (eta = {eta(e_t,e_t):+.0f}),  e_x = {e_x} (eta = {eta(e_x,e_x):+.0f})")
print(f"  and k_A = e_t + e_x,  k_B = e_t - e_x   -> the two null directions of the 2-plane")

print("\n" + "="*80)
print("Q1b -- THE SYMMETRIC TRACELESS TENSOR WITH THOSE NULL DIRECTIONS")
print("="*80)
print("""  A symmetric traceless tensor h on a 2-plane has exactly two null directions (the two
  solutions of h(k,k) = 0 up to scale) and is fixed by them up to scale. Build it: with the
  rulings at ±45 deg in the (t,x) plane, the tensor annihilating both is""")
# in the (t,x) basis with metric diag(-1,+1): h symmetric traceless wrt that metric.
# h(k,k)=0 for k = (1,±1) means h_tt + 2*(±1)*h_tx + h_xx = 0 for both signs
#  => h_tx = 0 and h_tt + h_xx = 0.  Traceless wrt diag(-1,1): -h_tt + h_xx = 0 => h_xx = h_tt.
#  Both together force h_tt = h_xx = 0 unless we drop one.  Compute honestly:
import itertools
print("    require h(k_A,k_A) = 0 and h(k_B,k_B) = 0 with k_{A,B} = (1, ±1):")
print("        h_tt + 2 h_tx + h_xx = 0")
print("        h_tt - 2 h_tx + h_xx = 0   =>  h_tx = 0  and  h_tt = -h_xx")
print("    and TRACELESS with respect to the plane's metric diag(-1,+1):")
print("        tr h = -h_tt + h_xx = 0    =>  h_xx = h_tt")
print("    the two together:  h_tt = -h_xx  AND  h_xx = h_tt   =>  h_tt = h_xx = 0")
h = np.zeros((2,2))
print(f"\n    => h = {h.tolist()}  ** THE TENSOR IS ZERO. **")
print("""
  ** SO THERE IS NO SUCH SPIN-2 OBJECT, AND THE REASON IS NOT AN ACCIDENT OF THIS POINT. **
  A symmetric traceless tensor on a LORENTZIAN 2-plane whose two null directions are the
  plane's OWN two null directions is identically zero. The two rulings are not "two null
  directions a tensor picks out" -- ** they are the 2-plane's own light cone **, and the light
  cone is what the metric already is. A tensor annihilating both null directions of a
  2-dimensional Lorentzian metric, and traceless with respect to it, has nothing left.""")

print("\n" + "="*80)
print("Q2 -- AND THE DEEPER REASON: SPIN-2 NEEDS A TRANSVERSE 2-PLANE, WHICH THIS IS NOT")
print("="*80)
print("""  P11's h_+ + i h_x lives on the TRANSVERSE plane of a propagating wave: the 2-plane
  ORTHOGONAL to the null propagation direction, which is SPACELIKE. A rotation in that
  spacelike plane acts as e^{-2i.theta} -- and it is the plane's EUCLIDEAN rotation group
  SO(2) that furnishes the spin-2 phase.
  ** The 2-plane the two rulings span is not that plane. It is the plane they span, which is
  LORENTZIAN -- the rulings ARE its null cone -- and its symmetry group is the BOOST group
  SO(1,1), not SO(2). ** A boost does not act as e^{-2i.theta}; it acts as a real hyperbolic
  scaling on each null direction separately:""")
for lam in [0.3, 1.0]:
    B = np.array([[np.cosh(lam), np.sinh(lam)], [np.sinh(lam), np.cosh(lam)]])
    kA2, kB2 = np.array([1.0, 1.0]), np.array([1.0, -1.0])
    print(f"    boost λ={lam}:  k_A -> {np.round(B@kA2,4)} = e^{{+λ}}·k_A ;  k_B -> {np.round(B@kB2,4)} = e^{{-λ}}·k_B")
    assert np.allclose(B@kA2, np.exp(lam)*kA2) and np.allclose(B@kB2, np.exp(-lam)*kB2)
print("""
  ** A boost scales each ruling by e^{±λ} and NEVER mixes them. ** So the pair (k_A, k_B)
  carries a real one-parameter weight, not a phase: its "spin" under the plane's own symmetry
  is a BOOST WEIGHT (±1 each), which is the standard Newman--Penrose boost weight -- and it is
  not spin-2 and not a helicity. ** The two rulings are eigenvectors of the boost, not a
  polarization. **""")

print("\n" + "="*80)
print("Q3 -- SO WHERE COULD A SPIN-2 OBJECT LIVE?  -- named, not answered")
print("="*80)
print("""  A spin-2 polarization needs a SPACELIKE transverse 2-plane orthogonal to a null direction.
  On the substrate that means: pick a null ruling k; its orthogonal complement within the
  tangent space is 3-dimensional and contains k itself; the transverse 2-plane is the quotient
  ** and it is spacelike **. THAT is where h_+ + i h_x lives, and it is exactly what P11 uses
  -- its Gowdy leaf carries a TT mode on a spacelike leaf.
  ** The OVERHEAD FIGURE is not that plane either. ** The overhead is the equatorial projection
  -- a 2-plane of the embedding containing the axis -- and the figure's content (the throat, the
  hinges, the sightlines, the bead) is all built in it. ** Nothing in the overhead figure is a
  transverse plane of a propagating mode, so nothing drawn on it carries spin 2. **

      >>> ROUTE (b) ANSWERED: THERE IS NO SPIN-2 OBJECT ON THIS FIGURE. The figure's null
          structure is the substrate's own light cone -- the rulings ARE the cone, not a
          polarization on it -- and the plane they span is Lorentzian, whose symmetry is a
          BOOST (real weight), not a rotation (spin-2 phase). <<<

  ** WHICH IS WHY ROUTE (c) FAILED ITS TYPE-CHECK, STATED PROPERLY: ** it was not that r
  happened to be a scalar. ** It is that the figure has no spin-2 sector at all. ** The bead's
  scalar r was not an unlucky choice of variable; there was nothing else to choose.""")

print("\n" + "="*80)
print("WHAT ROUTE (b) RETURNED")
print("="*80)
print("""  ** ⊢ THERE IS NO SPIN-2 OBJECT ON THE FIGURE, AND THE PREDICTED NEGATIVE HELD -- but for a
  sharper reason than predicted. **
  I predicted: a spin-2 object EXISTS and is ACHIRAL (fixed axis, no turning), on the grounds
  that the substrate's maximal symmetry and globally-defined ruling families are as fixed an
  axis structure as exists. ** Wrong at the first step. It does not exist. **

  (i)  ** The tensor is ZERO, identically. ** A symmetric traceless tensor on a Lorentzian
       2-plane whose two null directions are the plane's OWN null directions must satisfy
       h_tx = 0 and h_tt = -h_xx (annihilating both rulings) AND h_xx = h_tt (traceless wrt
       diag(-1,+1)). Together: h = 0. ** The two rulings are not two null directions a tensor
       picks out -- THEY ARE THE 2-PLANE'S OWN LIGHT CONE, and the light cone is what the
       metric already is. **
  (ii) ** And the symmetry group is wrong. ** Spin-2's e^{-2i.theta} comes from SO(2) acting on
       a SPACELIKE transverse plane. The rulings span a LORENTZIAN plane, whose group is the
       boost SO(1,1): a boost scales each ruling by e^{±λ} and NEVER MIXES THEM (verified).
       ** The pair carries a real BOOST WEIGHT (the Newman--Penrose ±1), not a phase. The two
       rulings are eigenvectors of the boost, not a polarization. **
  (iii)** And the overhead figure is not a transverse plane. ** h_+ + i h_x lives on the
       spacelike 2-plane orthogonal to a null propagation direction -- which is exactly what
       P11's Gowdy leaf supplies. The overhead is the equatorial projection containing the
       axis; the throat, the hinges, the sightlines and the bead are all built in it, and
       ** none of it is a transverse plane of a propagating mode. **

  >>> SO ROUTE (c)'s FAILURE IS RESTATED CORRECTLY: it was not that the bead's r HAPPENED to be
      a scalar and some other variable might have been spin-2. ** THE FIGURE HAS NO SPIN-2
      SECTOR. There was nothing else to choose. ** <<<

  ** AND THAT IS WHERE R5's ROUTES (b) AND (c) BOTH END, TOGETHER, FOR ONE REASON: ** the two
  instruments the corpus has for a wave -- P11's TT shear and P11's polarization chirality --
  are both spin-2, and the figure carries no spin-2. ** The rhyme is not refuted; the corpus's
  wave-instruments simply cannot be pointed at it. ** What the figure carries instead is a boost
  weight on the rulings and a cube-root monodromy on the bead (⊢67) -- both real, both already
  named, neither a helicity.

  ⚠ ** WHAT SURVIVES, AND IT IS ROUTE (a), NOW THE ONLY ONE LEFT: ** P15 excludes radiation
  from the RATE (L1) -- "content is read off the clock the geometry sets, never summed into
  it." ** That is a statement about what is summed into a clock. It is not a statement that no
  field exists at L2. ** And nothing in routes (b) or (c) touches L2: both failed on the
  FIGURE's content, and the figure is an L1/geometry object. ** Route (a) is untouched by both
  failures, and is now R5's whole remaining surface. **""")
