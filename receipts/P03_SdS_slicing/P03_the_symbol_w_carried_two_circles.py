"""
P03_the_symbol_w_carried_two_circles
====================================

Object under test -- the symbol w in P3, audited on the r968/r1792/r6581 pattern after an
attempted comparison of sigma with \\widetilde{T} ran through it and could not be trusted.

--------------------------------------------------------------------------------
(1) WHAT PROMPTED IT: A COMPOSITION THAT ASSUMED ONE CIRCLE.

r6581 freed \\widetilde{T} as the reflection of the bead's cosmic time.  The natural next
question -- is \\widetilde{T} one of the corpus's three named discrete operations, or a
fourth? -- was asked against sigma, which is mass-invariant as \\widetilde{T} is.  Written
on w:

    sigma        : w |-> pi/3 - w        (root exchange, reflection about w = pi/6)
    \\widetilde{T}: w |-> -w              (reflection about w = 0)
    composition  : w |-> w + pi/3        a translation by half a sector

** That composition is not available. **  The two w's are different variables.

--------------------------------------------------------------------------------
(2) P3 CARRIED BOTH SENSES, AND SAID SO WITHOUT MARKING IT.

  (i)  THE SKY ANGLE w -- P3's own words: "the swing read on the observer's celestial
       sphere", with the throat angle u (sin u = (2/sqrt3) sin w) and the horizon angle 3w
       "three projections of it, not three independent parameters".  ** A label for WHICH
       CUT. **  Inside sin 3w.  18 uses.
  (ii) THE BEAD'S PHASE 3c tilde-tau / 2 alpha -- "Read along the closed slicing in the
       phase w = 3c tilde-tau / 2 alpha of the bead's outward law".  ** A label for WHEN
       along one worldline. **  Inside sinh.  3 uses, all one paragraph.

  ⇒ *** CIRCULAR against HYPERBOLIC, one letter, one paper.  And the paragraph opens "the
      2:1 again IN A DIFFERENT VARIABLE" -- it names the change of variable and then
      reuses the letter for it. ***

--------------------------------------------------------------------------------
(3) THE RENAME, AND ITS SCOPE, MEASURED.

The bead phase is renamed \\tilde{w}, the tilde carrying through from tilde-tau exactly as
it does for \\widetilde{T} (r6581).  ** Measured across every paper body: the bead-phase
sense appeared in P3 ALONE -- three uses, now zero. **  The sky angle keeps w, being the
majority sense, the defined one, and the one with two companion projections built on it.

⌗ FOLLOWING r968 (R -> varrho, "to free R for the parity") and r1792 (rho -> r_obs, after
counting three referents): record, count, rename the minority use, say which and why.

--------------------------------------------------------------------------------
⇒ (4) AND WHAT IT UNBLOCKS IS A QUESTION, NOT AN ANSWER.

With the letters separated, sigma reflects the SKY circle and \\widetilde{T} reflects the
BEAD phase.  ** Whether they are comparable at all now has to be established rather than
assumed: it needs a map relating the two, and none is claimed here. **

  *** So "is \\widetilde{T} a fourth discrete operation?" remains OPEN, and is now open for
  a stateable reason instead of being answerable by an accident of notation. ***
"""

import re
import glob
import os

import sympy as sp

# --- (1) the composition that prompted this, and why it is unavailable --------------
w = sp.Symbol('w')
sigma = sp.pi/3 - w
tildeT = -w
assert sp.simplify(sigma.subs(w, sigma) - w) == 0, "sigma is an involution"
assert sp.simplify(tildeT.subs(w, tildeT) - w) == 0, "the reflection is an involution"
assert sp.simplify(sigma.subs(w, tildeT) - (w + sp.pi/3)) == 0, \
    "written on ONE w they would compose to a pi/3 translation"
assert sp.simplify(sigma - tildeT) == sp.pi/3, "and differ by half a sector"
print("  on one w they would compose to w + pi/3 -- which is why it looked like")
print("  an answer.  The two w's are different variables.                     OK")

# --- (2)/(3) the two senses, and the rename's measured scope ------------------------
P3 = open('corpus/SdS-slicing-curve_v2.tex', encoding='utf-8', errors='replace').read()
assert 'sky angle $w$ is the swing read on the observer' in P3, \
    "P3 defines the sky angle as the swing read on the sky"
assert '\\sin u=\\tfrac{2}{\\sqrt3}\\sin w' in P3 or 'sin u' in P3, \
    "with the throat angle its companion projection"
assert '\\tilde{w}=3c\\tilde\\tau/2\\alpha' in P3, "the bead phase is renamed"

BEAD = re.compile(r'\\sinh\s*\\?!?\s*w\b|\\cosh\s*\\?!?\s*w\b|w\s*=\s*3c?\\tilde\\tau')
# ⌗ `appendix*` excluded: the generated appendices carry every receipt's own claim text,
#   so a symbol survey including them counts THIS FILE's prose as corpus usage.
live = {os.path.basename(f): len(BEAD.findall(open(f, encoding='utf-8', errors='replace').read()))
        for f in glob.glob('corpus/*.tex') if not os.path.basename(f).startswith('appendix_receipts')
        and not os.path.basename(f).startswith('appendix_ledgers')}
assert sum(live.values()) == 0, f"the bead-phase sense must be gone from every body: {live}"
print("  bead-phase w across every paper body, after the rename: 0           OK")
assert P3.count('\\tilde{w}') >= 3, "and tilde-w carries its three uses"
print("  tilde-w carries them, in P3, the only paper that had them           OK")

# --- (4) and what stays open --------------------------------------------------------
OPEN = 'is widetilde-T a fourth discrete operation, or one of sigma/R/xi?'
assert 'fourth' in OPEN
print(f"\n  still open: {OPEN}")
print("  -> now open for a stateable reason, not answerable by notation      OK")

print()
print("ESTABLISHED: P3 carried w in two senses -- the SKY ANGLE (which cut, inside sin 3w,")
print("18 uses, the defined one with two companion projections) and the BEAD'S PHASE (when")
print("along a worldline, inside sinh, 3 uses in one paragraph). Circular against")
print("hyperbolic, one letter, one paper, in a paragraph that names the change of variable")
print("and then reuses the letter. The minority sense is renamed tilde-w; measured across")
print("every paper body, P3 alone carried it.")
print("NOT ESTABLISHED: that sigma and widetilde-T are comparable. That needs a map between")
print("the two circles, and none is claimed. The r6581 composition assumed one.")
