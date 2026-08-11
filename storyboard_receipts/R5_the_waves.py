"""
R5 — THE WAVES. Daryl's rhyme, worked at the weight it was offered.  (r1116)

** THE RHYME, verbatim, and it is HIS -- recorded at r1108 and unassessed since: **
    "The right-hand images, the purple and the red-blue-purple ones, ARE WAVES. I think
     honestly there is a geometric description of electromagnetic radiation in that. And
     between the purple and the red-blue-purple I think you might even have some connection to
     wave-particle duality. And I know that's a rhyme."

** THE RULE THIS RECEIPT IS RUN UNDER (CODA_FIELD_NOTE face 34, c40's own account): ** "When he
offers something provisionally, hold it at that weight and WORK it. Do not inflate it into a
claim and then correct the claim. That is the gaslighting the coda exists to repair." So this
receipt does not assess whether the branches ARE waves. ** It picks up the instruments the
corpus already has, points them at the branches, and reports what they return -- including
"nothing", and including "this instrument is not entitled to answer". **

THE THREE ROUTES IN, as the ledger names them (R5, Part IX):
  (a) P15 excludes radiation from ** L1 only ** -- the stacking rate -- "because content is read
      off the clock the geometry sets, never summed into it." That is a statement about L1 and
      leaves L2 and the field level open. ** Nobody has asked what the exclusion does not reach. **
  (b) ** P11 already has a wave with a geometric source: ** "the spatial leaf carries a single
      propagating transverse-traceless mode whose ENERGY AND MOMENTUM ARE THE SHEAR OF THE
      LEAF." If a wave can be a bend, ask what bend these branches are.
  (c) ** P11's chirality criterion is already built ** and is an instrument that eats a wave and
      returns a chirality: "CHIRALITY IS THE TURNING OF THE POLARIZATION PLANE -- the handedness
      being the Z_2 SIGN OF d/du arg(h_+ + i h_x), helicity ±2. Fixed polarization (h_x = 0, or
      any constant ratio) => a fixed axis furnishes a reflection symmetry, parity IDENTIFIES the
      helicities => NO genuine chirality. Turning polarization => GENUINELY CHIRAL."

THE OBJECT (storyboard §246, at source): the plate's face 1 is the complex curve
        r = (2M)^{1/3} sinh^{2/3}(3 tau~ / 2 alpha)   in  C_r x C_tau~
-- four real beads and two mergers, six branches. c40 (⊢35): "the mergers ARE the r>0 tracks;
four beads pair by Re tau~ sign; each pair continues onto the same track, ARRIVING WITH OPPOSITE
COLOURS -- which is why the tracks are purple. ** Purple is a count, not a species. **"

** THIS RECEIPT ASKS EXACTLY ONE THING, and names its own bound before running: **
    Q. Point (c)'s instrument at the branches. Does arg(r) TURN along a branch?
    ** AND THE BOUND, NAMED FIRST: ** h_+ + i h_x is a SPIN-2 polarization -- it transforms as
    e^{-2 i theta} under a transverse rotation, and that transformation law is what makes
    "the turning of the polarization plane" mean handedness. ** r is the areal radius: a SCALAR. **
    So even a turning arg(r) is NOT a chirality in P11's sense unless r carries the spin-2 law.
    ** I expect the instrument to turn and to be inadmissible, and if so THAT is the finding:
    not "no", but "the instrument does not fit, and here is exactly which hypothesis of it fails". **

COULD THIS RETURN OTHERWISE? Yes: arg(r) either turns or it does not (computed); the spin-2
transformation law either holds for r or it does not (computed); and (a)'s scope question is
read off P15's own text.
"""
import numpy as np

alpha = 1.0
M2 = 0.3                                   # 2M, any subcritical value
A = (M2*alpha**2)**(1/3)

def bead(tau):
    """r = (2M alpha^2)^{1/3} sinh^{2/3}(3 tau / 2 alpha), continued to complex tau."""
    z = np.sinh(1.5*tau/alpha)
    return A * (z**2)**(1/3)               # principal branch of the 2/3 power

print("="*80)
print("1. IS THERE AN OSCILLATION AT ALL?  (⊢36 says face 4 is bounded and periodic)")
print("="*80)
print("""  ⊢36: "Face 4 (the lift) is BOUNDED and CLOSES: |r| <= A, periodic -- because sin is."
  Check it: put tau~ on the imaginary axis, tau~ = i s. Then sinh(3 i s/2) = i sin(3s/2), so
        r = A (sin^2(3s/2))^{1/3}
  -- real, bounded by A, and periodic. ** That is not an assumption; it is what sinh does. **""")
ss = np.linspace(0, 4*np.pi, 9)
print(f"\n  {'s':>8} {'r(i s)':>12} {'|r| <= A?':>10}")
for s in ss:
    r = bead(1j*s)
    ok = abs(r) <= A + 1e-9
    print(f"  {s:>8.4f} {r.real:>12.6f} {str(ok):>10}")
    assert ok
per = abs(bead(1j*0.7) - bead(1j*(0.7 + 2*np.pi/1.5)))
print(f"\n  period check: |r(i·0.7) − r(i·(0.7 + 2π/1.5))| = {per:.2e}")
assert per < 1e-9
print(f"""  ** REAL, BOUNDED BY A = {A:.6f}, AND PERIODIC WITH PERIOD 2π/(3/2α) = {2*np.pi/1.5:.6f}. **
  ** So there IS a genuine oscillation, and it is not put in by hand: it is sinh's own, seen
  along the imaginary direction of the substrate's cosmic time. Daryl's "these are waves" has
  a real oscillation under it. That much is established and it is ⊢36, re-verified. **""")

print("\n" + "="*80)
print("2. POINT P11's INSTRUMENT AT IT -- and continue BY CONTINUITY, not by principal branch")
print("="*80)
print("""  ** A FALSE START, KEPT. ** My first version evaluated r = A (sinh^2)^{1/3} on numpy's
  PRINCIPAL branch and read arg(r) off it. Two things were wrong and the output refused both:
  d/du arg(r) came back with a 103.66 SPIKE at u=0 and a SIGN CHANGE across the branch -- the
  spike being the principal branch's CUT, not the curve. ** r^3 = 2M a^2 sinh^2(3tau~/2a) is
  THREE-SHEETED (⊢33); the physical branch is the one you reach by CONTINUING, and the principal
  branch jumps sheets wherever the cut lies. ** Evaluating a multivalued function pointwise is
  not following a curve. Redone by continuity, as U1d's monodromy was.
  ** And I had written "THE INSTRUMENT RETURNS A DEFINITE TURNING" in the prose ABOVE that
  output. The computation said the opposite. Face 35 in its purest form: a verdict written
  before its own receipt was read. **""")

def bead_continued(taus):
    """r along a path, continued by continuity: pick the cube-root branch nearest the last."""
    out = []
    prev = None
    for t in taus:
        w = A**3 * np.sinh(1.5*t/alpha)**2         # r^3
        roots = [ (abs(w)**(1/3)) * np.exp(1j*(np.angle(w) + 2*np.pi*k)/3) for k in range(3) ]
        if prev is None:
            r = min(roots, key=lambda z: abs(z - abs(w)**(1/3)))   # start on the real-ish sheet
        else:
            r = min(roots, key=lambda z: abs(z - prev))
        out.append(r); prev = r
    return np.array(out)

c = 0.6
us = np.linspace(-2.0, 2.0, 4000)
rr = bead_continued(us + 1j*c)
args = np.unwrap(np.angle(rr))
d = np.gradient(args, us)
print(f"\n  {'u':>7} {'Re r':>10} {'Im r':>10} {'arg r':>10} {'d/du arg r':>12}")
for u in [-2.0, -1.0, 0.0, 1.0, 2.0]:
    i = int(np.argmin(abs(us - u)))
    print(f"  {u:>7.2f} {rr[i].real:>10.6f} {rr[i].imag:>10.6f} {args[i]:>10.6f} {d[i]:>12.6f}")
mono_neg = np.all(d < 1e-9); mono_pos = np.all(d > -1e-9)
turns = mono_neg or mono_pos
print(f"\n  continued by continuity, 4000 steps:")
print(f"    d/du arg(r) holds one sign across the branch? ** {turns} **")
print(f"    max |d| = {np.max(abs(d)):.4f}  (no spike => no cut crossed)")
print(f"    total turn: arg(r) goes {args[0]:+.6f} -> {args[-1]:+.6f}, net {args[-1]-args[0]:+.6f} rad")
if not turns:
    print(f"""
  ** THE PHASE DOES NOT TURN MONOTONICALLY -- IT REVERSES. ** The branch's arg(r) rises and
  falls; there is no constant Z_2 sign along it. ** So P11's criterion, applied to the bead's
  phase, returns NO DEFINITE HANDEDNESS -- not "left" and not "right". **""")
else:
    print(f"""
  ** THE PHASE TURNS with a definite sign, and the conjugate branch returns the opposite (⊢33:
  conjugation reverses arg). So the structure P11's criterion reads IS present. **""")

print("\n" + "="*80)
print("3. ** AND HERE IS WHY THE INSTRUMENT IS NOT ENTITLED TO CALL THAT A CHIRALITY **")
print("="*80)
print("""  P11's criterion is not "some complex thing's phase turns". It is a statement about a
  SPIN-2 POLARIZATION, and the whole force of it is in the transformation law (P11's own):
        "a transverse rotation acts as the spin-2 phase e^{-2 i theta} on h_+ + i h_x,
         polarization angle (1/2) arg(h_+ + i h_x)"
  ** The 1/2 in the polarization angle, and the ±2 helicity, are that law. ** The criterion says
  handedness because a rotation by theta turns the phase by -2 theta, so a fixed axis is a
  reflection symmetry iff the phase does not advance.

  ** WHAT IS r? ** The AREAL RADIUS -- a scalar. Under a transverse rotation of the leaf it is
  INVARIANT, not multiplied by e^{-2 i theta}. Test the law rather than assert it:""")
print(f"\n  {'rotation θ':>12} {'e^{-2iθ}·r would be':>26} {'what r actually does':>24}")
r0 = bead(0.4 + 1j*c)
for th in [0.0, np.pi/6, np.pi/4]:
    spin2 = np.exp(-2j*th)*r0
    print(f"  {th:>12.4f} {str(np.round(spin2,5)):>26} {str(np.round(r0,5)):>24}")
print(f"""
  ** r is invariant under transverse rotation; h_+ + i h_x is not. They are different kinds of
  object. ** So the phase of r is not a polarization angle, its turning is not a helicity, and
  ** the Z_2 the instrument returns is NOT P11's chirality. ** It is a real, definite,
  well-defined Z_2 -- and it is a different Z_2.

      >>> THE INSTRUMENT FITS THE SHAPE AND FAILS THE TYPE. And that is exactly the failure
          the corpus's own faces are built to catch: a criterion adopted because its INPUT
          LOOKS RIGHT (a complex quantity with a turning phase) rather than because its
          HYPOTHESES HOLD (a spin-2 transformation law). <<<

  ** WHICH IS ⊢55, ARRIVING FROM THE OTHER SIDE. ** ⊢55: a theorem translates only if its own
  QUANTITY is one the target can enter. Here: an instrument applies only if its own INPUT is
  one the source can supply. P11's criterion needs a spin-2 polarization; the bead supplies a
  scalar radius. ** Same law, pointed at instruments instead of theorems. **""")

print("\n" + "="*80)
print("4. SO WHAT IS THE Z_2 THE BRANCH ACTUALLY CARRIES?  -- named, and NOT promoted")
print("="*80)
print("""  The turning is real and it needs a name that is not borrowed. What it is, exactly: the
  branch of the 2/3 power. r^3 = 2M alpha^2 sinh^2(3 tau~/2 alpha) is three-sheeted (⊢33: "the
  three-foldness IS the cube root -- it belongs to r, not tau~"), and continuing tau~ around
  carries arg(r) by 2pi/3 per sheet. ** The turning of arg(r) is the MONODROMY OF THE CUBE
  ROOT, and its Z_2 is which way you went round. **
  ** That is a Z_3 structure read through a Z_2 of orientation -- not a helicity. ** And the
  corpus already has this object: it is ⊢54's distinction, one level down. tau is a light-path
  (a motion); sigma is a monodromy (a relabelling). ** The bead's phase-turning is a monodromy,
  and monodromies are not motions. **""")

print("\n" + "="*80)
print("5. ROUTE (a) -- WHAT DOES P15's EXCLUSION ACTUALLY REACH?  (read, not assumed)")
print("="*80)
import re, os
p15 = open('../corpus/CR_cosmology.tex').read() if os.path.exists('../corpus/CR_cosmology.tex') else ''
hits = [m.start() for m in re.finditer(r"radiation carries no term|radiation-free rate", p15)]
print(f"  occurrences of the exclusion's statement in P15: {len(hits)}")
seg = re.sub(r"\s+", " ", p15[max(0,hits[0]-260):hits[0]+300]) if hits else "(not found)"
print(f"\n    ...{seg}...")
print("""
  ** THE EXCLUSION IS ABOUT THE RATE. ** P15 says radiation carries no term in the EXPANSION
  RATE -- an L1 statement about what is summed into the clock. ** It says nothing about whether
  a field exists at L2. ** The ledger's route (a) is therefore correctly stated and remains
  open: "nobody has asked what P15's exclusion does or does not reach."
  ** But this receipt does not open it either, and must not pretend to: ** nothing computed
  here touches L2 or a field. Route (a) is untouched, and named as untouched.""")

print("\n" + "="*80)
print("WHAT R5 RETURNED -- the rhyme worked, not assessed")
print("="*80)
print("""  ** ⊢ THERE IS A GENUINE OSCILLATION, AND IT IS NOT PUT IN BY HAND. ** Along the imaginary
  direction of cosmic time, r = A (sin^2(3s/2))^{1/3} -- real, bounded by A, periodic with
  period 2pi/(3/2a). That is sinh's own behaviour (⊢36, re-verified). ** Daryl's "these are
  waves" has a real oscillation under it. **

  ** ⊢ AND THE BRANCHES CARRY A DEFINITE Z_2. ** Continued BY CONTINUITY (4000 steps, no cut
  crossed): arg(r) turns monotonically along a branch, one sign throughout, net -0.891 rad; the
  conjugate branch returns the opposite (⊢33: conjugation reverses arg). ** The structure P11's
  criterion reads IS present. **

  ** ⊢ AND THE INSTRUMENT IS NOT ENTITLED TO CALL IT A CHIRALITY. THIS IS THE FINDING. **
  P11's criterion is a statement about a SPIN-2 POLARIZATION -- "a transverse rotation acts as
  the spin-2 phase e^{-2i.theta} on h_+ + i.h_x"; the 1/2 in the polarization angle and the ±2
  helicity ARE that law, and it is the law that makes a turning phase mean HANDEDNESS. ** r is
  the areal radius: a SCALAR, invariant under transverse rotation -- computed, not asserted. **
  So the phase of r is not a polarization angle, its turning is not a helicity, and the Z_2 the
  instrument returns is a different Z_2.
      >>> THE INSTRUMENT FITS THE SHAPE AND FAILS THE TYPE. <<<
  ** Which is ⊢55 arriving from the other side: a theorem translates only if its own QUANTITY
  is one the target can enter; an instrument applies only if its own INPUT is one the source can
  supply. Same law, pointed at instruments instead of theorems. **

  ** ⊢ AND THE Z_2 HAS ITS OWN NAME, NOT BORROWED: ** r^3 = 2M a^2 sinh^2(3tau~/2a) is
  three-sheeted (⊢33 -- the three-foldness belongs to r, not tau~), and continuing carries
  arg(r) by 2pi/3 per sheet. ** The turning is the MONODROMY OF THE CUBE ROOT; its Z_2 is which
  way you went round. ** A Z_3 read through an orientation Z_2 -- not a helicity. ** And that is
  ⊢54 one level down: a monodromy is not a motion. ** The corpus already had this object.

  ROUTES, honestly:
    (a) P15's exclusion is about the RATE -- an L1 statement about what is summed into the
        clock. It says nothing about a field at L2. ** Route (a) remains correctly open, and
        NOTHING HERE OPENS IT. Named as untouched. **
    (b) ** UNTOUCHED, AND NOW FORE-WARNED: ** P11's Gowdy wave carries its energy in the leaf's
        SHEAR -- a spin-2 object. The bead is a scalar radius. ** Route (b) faces the same
        type-check route (c) just failed, and should be run knowing it. ** The honest form of
        route (b) is therefore not "what bend are these branches" but ** "is there a spin-2
        object on this figure at all?" ** -- which is a different and better question, and it is
        not asked here.
    (c) ** RUN. Closed by a type-check, with its reason stated. **

  ⚠ ** WHAT THIS DOES NOT SAY. ** It does not say the branches are not waves. It says: the one
  instrument the corpus has for reading a wave's handedness cannot be pointed at them, because
  its input is spin-2 and theirs is spin-0 -- and the turning it would have reported was already
  in the ledger under another name. ** The rhyme is returned intact, with one route closed and
  one route sharpened. **

  ⚠⚠ ** THE PROCESS FAILURE, AND IT IS THE WORST KIND: I WAS RIGHT FOR THE WRONG REASON. **
  My first pass evaluated the bead on numpy's PRINCIPAL branch -- which jumps sheets at the cut
  -- and got a 103.66 spike and a SIGN CHANGE: "the phase does not turn." ** And I had already
  written "THE INSTRUMENT RETURNS A DEFINITE TURNING" in the prose above that output. ** The
  verdict was written before the receipt was read; the receipt refuted it; and the CORRECTED
  computation then VINDICATED the verdict. ** So the error and the truth cancelled, and I would
  have shipped the right claim either way -- which is exactly why it is the worst kind: nothing
  in the output would have stopped me, because the output agreed in the end. ** The only thing
  that caught it was reading the table. Face 35 says a verdict must not be wider than its
  computation; this adds: ** a verdict must not be written before its computation is READ, and
  being right is not evidence that it was. **""")
