#!/usr/bin/env python3
"""
`r7267` ① BATCH TWO — THE INPUTS THE HINGE ROWS NEED, HANDED TO `L-104w`'s OWN `sep`.

`r7261`'s backlog named `baryon_edge/L104w_the_excentre_trichotomy.py: sep` as the function
nearest three rows across three receipts of the bridge prefix, with the gap `INPUTS`.

** AND THE GAP IS LITERALLY A PAIR `L-104w` NEVER FORMS. **  `L-104w` runs `sep` over the
fifteen EXCENTRE-EXCENTRE pairs at radius `4 alpha` and the thirty-six HINGE-EXCENTRE pairs,
and the three rows are about neither: they assert that ** the two ends of ONE hinge ** --
same azimuth, opposite horn, at the hinge radius `2 alpha` -- are timelike separated.  *That
pair is one call of `sep` on two points `pt` already builds, and nothing in the corpus had
made it.*

⇒ `sep(pt(a, 2 alpha, +1), pt(a, 2 alpha, -1)) = -12 alpha^2` at every hinge azimuth, which
`character` reads as `timelike`.

⚠ ** AND THE CONVERSE IS REACHABLE AND IT IS NOT A RADIUS AWAY BUT AT THE THROAT. **  The same
two ends taken at `rho = alpha` give `s^2 = 0` -- NULL, not timelike -- because `pt`'s time
component is `sgn sqrt(rho^2 - alpha^2)` and the two ends coincide there.  *So the claim is a
statement about the hinge sitting OUTSIDE the throat, and the predicate is false at it.*

WHAT IS NOT CLAIMED.  ** Not the fourth row of this module's four ** -- `B11`'s `the three
critical loci are the three causal characters` needs `character` at the three CRITICAL LOCI,
and which three loci those are is a reading of the paper that this file does not make.  It is
held with the reason rather than taken, and named in the report.
"""
import os
import sys

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from graft import graft                                        # noqa: E402

MODULE = 'baryon_edge/L104w_the_excentre_trichotomy.py'


class Trichotomy:
    """`L-104w`'s own `pt`, `sep` and `character`, at the pair it never forms."""

    def __init__(self):
        g = graft(MODULE, 'sep', 'character', 'pt',
                  extra=('al', 'hinge_az', 'exc_az'))
        self.pt, self.sep, self.character = g['pt'], g['sep'], g['character']
        self.al, self.hinge_az, self.exc_az = g['al'], g['hinge_az'], g['exc_az']
        self.statements = (g['_STATEMENTS'], g['_OF'])

    def hinge_ends(self, az, radius=None):
        """the two ends of ONE hinge: same azimuth, opposite horn, at the hinge radius"""
        r = 2 * self.al if radius is None else radius
        return self.pt(az, r, 1), self.pt(az, r, -1)

    def ends_interval(self, az, radius=None):
        return sp.nsimplify(self.sep(*self.hinge_ends(az, radius)))

    def ends_character(self, az, radius=None):
        return self.character(self.sep(*self.hinge_ends(az, radius)))

    def all_hinges_timelike(self, radius=None):
        return all(self.ends_character(a, radius) == 'timelike' for a in self.hinge_az)


def at_inputs():
    return Trichotomy()


def _selftest():
    T = at_inputs()
    print('  trichotomy.py -- L-104w grafted, sep called on the pair it never forms')
    print(f"    grafted {T.statements[0]} of {T.statements[1]} top-level statements   "
          f"al = {T.al}")
    for a in T.hinge_az:
        print(f"    hinge azimuth {a:>3}: two ends  s^2 = {T.ends_interval(a)}   "
              f"-> {T.ends_character(a)}")
    assert T.all_hinges_timelike()
    print(f"    converse, the same ends at the THROAT radius rho = al: "
          f"s^2 = {T.ends_interval(T.hinge_az[0], T.al)} -> "
          f"{T.ends_character(T.hinge_az[0], T.al)}")
    assert not T.all_hinges_timelike(T.al)
    return 0


if __name__ == '__main__':
    sys.exit(_selftest())
