#!/usr/bin/env python3
"""check_foreign_ontology.py -- A COMPUTATION MAY NOT REST ON A QUANTITY THE CORPUS DOES NOT POSIT.

** WHY.  r2726, Daryl: ** "*** we don't pull in standard LCDM modelling infrastructure that has
absolutely nothing to do with the physics of the corpus without ensuring every piece is fully
justified. ***"

** WHAT WENT WRONG AT r2709--r2719, at the root and not the symptom. **  The `PO-10` comparison was
framed as MODEL SELECTION -- AIC/BIC on parameter COUNT, CR at $k=2$ against $\\Lambda$CDM at $k=6$.

      *** omega_b   a baryon density in a flat FRW expansion history
          omega_c   COLD DARK MATTER -- an entity CR does not posit
          tau       reionization optical depth in a LCDM thermal history
          n_s       a primordial tilt from an INFLATON power spectrum
          A_s       that spectrum's amplitude
          theta_*   the acoustic angle -- the ONE of the six CR derives ***

  ⇒ *** FIVE OF SIX ARE OBJECTS CR DOES NOT HAVE.  The error was not holding $n_s$ fixed; it was
      COUNTING PARAMETERS IN A SPACE CR DOES NOT INHABIT, and then negotiating how many dimensions each
      side was allowed. ***

  ⛔⛔ ** AND AIC/BIC PRESUPPOSES EXACTLY WHAT IS FALSE HERE: ** *** model selection by parameter count
  assumes both models live in ONE parameter space and differ only in DIMENSION.  CR and $\\Lambda$CDM are
  different ONTOLOGIES.  Counting across them is not a comparison -- it is arithmetic on a category
  error. ***

** WHAT THIS CHECKS. **  Any receipt naming a quantity from the foreign list below must also carry a
JUSTIFICATION: either a derivation from corpus objects, or an explicit statement that the quantity is
INHERITED and what that costs.

  ⌗ ** The list is of ENTITIES, not of numbers. **  *** A receipt may use Planck's measured $\\ell_D$ as
    a datum -- that is an observation.  What it may not do is treat $\\Omega_c$, $\\tau$ or $n_s$ as though
    the corpus posits them, because the corpus's difference from $\\Lambda$CDM is carried by $H(a)$ and a
    substrate, not by a six-dimensional parameter vector. ***

  ⚠ ** It cannot judge whether a justification is GOOD ** -- *** it checks that one is present.  A
      receipt that says "inherited, and here is what that costs" passes; one that silently uses the
      quantity as its own does not. ***

    python3 corpus/check_foreign_ontology.py

Written r2726.  Stated for reversal.
"""
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

# ** entities LambdaCDM posits and the corpus does not. **
# ** r2726, second pass: match the ONTOLOGY, never a bare symbol.  *** `omega_c` is a
# cornering FREQUENCY in O6 and a probe index in P03; `n_s` is a mode number in three more.
# A gate that flags a variable NAME flags physics that has nothing to do with LambdaCDM --
# so every pattern below names the ENTITY in words, not the letter that happens to carry
# it. ***
FOREIGN = {
    'cold dark matter': r'\bcold dark matter\b|\bCDM density\b|\bdark.matter density\b',
    'reionization': r'\breionization optical depth\b|\btau_reio\b|\boptical depth to reion',
    'primordial tilt': r'\bspectral tilt\b|\bprimordial tilt\b|\bscalar spectral index\b',
    'inflaton': r'\binflaton\b|\bslow.roll\b',
    'six-parameter basis': r'six[- ]parameter (?:basis|set|fit|model)|\bbase.LCDM parameter',
}
# ** a receipt naming one must ALSO carry one of these. **
JUSTIFIED = re.compile(
    r'inherit|adopted|not derived|not predicted|imported|standard value|'
    r'accommodation|foreign|does not posit|LCDM\'s own|control arm|reference',
    re.I)


def main():
    print()
    print('  check_foreign_ontology -- does any receipt rest on an entity the corpus does not posit?')
    print()
    flagged, n = [], 0
    for f in sorted(glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True)):
        if os.path.basename(f) == os.path.basename(__file__):
            continue
        d = open(f, encoding='utf-8', errors='replace').read()
        n += 1
        hits = [k for k, pat in FOREIGN.items() if re.search(pat, d)]
        if hits and not JUSTIFIED.search(d):
            flagged.append((os.path.basename(f)[:56], hits))

    print(f'  {n} receipt(s) checked')
    if flagged:
        print()
        for name, hits in flagged:
            print(f'    [FLAG] {name}: {hits}')
        print()
        print('    ⛔ ** A RECEIPT RESTS ON AN ENTITY THE CORPUS DOES NOT POSIT, WITH NO')
        print('       JUSTIFICATION. **  *** The corpus\'s difference from LambdaCDM is carried by H(a)')
        print('       and a substrate, not by a six-dimensional parameter vector.  A quantity borrowed')
        print('       from that vector must be named as INHERITED, with what it costs stated -- or the')
        print('       computation is testing LambdaCDM\'s ontology and calling the answer CR\'s. ***')
        return 1
    print('  no receipt rests on a foreign entity without naming it as inherited.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
