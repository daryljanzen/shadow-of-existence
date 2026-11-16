"""Y2 -- the sector's sixteen is the left--right-symmetric generation, and the face's three-plus-one
returns the charges in thirds.

P14 counts a generation as 3 x 2 x 2 coloured states (colour, horn, ruling) and 1 x 2 x 2 colourless
ones, with every two-valued grading splitting the colourless four 2+2 and the right-handed pair a
doublet where the Standard Model has two singlets.  The left--right-symmetric extension of the
Standard Model, SU(4) x SU(2)_L x SU(2)_R (Pati--Salam), carries a generation as
(4,2,1) + (4bar,1,2): sixteen states, isospin 2+2 on each chirality, the lepton the fourth colour.

Computed here:
  (1) the counts: 3*2*2 + 1*2*2 = 16 = 4*2 + 4*2, coloured 12 and colourless 4, each chirality 8;
  (2) the abelian generator the 3+1 branching of the face's Spin(6)=SU(4) fixes is traceless,
      diag(1,1,1,-3) up to scale -- the only traceless diagonal generator commuting with the colour
      SU(3) inside SU(4);
  (3) with Q = I3L + I3R + c(B-L) and the neutrino neutral, c is fixed (c x B-L(lepton) = -1/2) and
      every Standard Model charge follows, in thirds: u 2/3, d -1/3, nu 0, e -1, on both chiralities;
  (4) with SU(2)_R broken to its I3R, Y = I3R + c(B-L) returns P14's hypercharges exactly, in its
      normalisation Q = I3 + Y and in left-handed conjugate form: Y_Q = 1/6, Y_uc = -2/3,
      Y_dc = 1/3, Y_L = -1/2, Y_ec = 1, Y_nuc = 0;
  (5) CONTROL: a generator that is not traceless -- diag(1,1,1,1), counting all four colours alike --
      cannot make the neutrino neutral and the up quark +2/3 together, so the thirds are carried by
      the tracelessness and not by the formula.

Bound: a correspondence of representation content, not a gauging -- the face's SU(4) acts on the
Euclidean face and the layer's SU(2)s on space, so neither is a gauge group of the matter; the
breaking of SU(2)_R and its scale are not computed or claimed; the identification of P14's horn and
ruling labels with I3 and chirality is P14's own.

Written by the chat seat.  Stated for reversal.
"""
import os
import re
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def flat(path):
    return re.sub(r'\s+', ' ', open(path, encoding='utf-8', errors='replace').read())


def main():
    print()
    print('  Y2 -- the sixteen and the thirds')
    print()
    print('    (1) the counts, stated: 3*2*2 + 1*2*2 = 16 = dim(4,2,1) + dim(4bar,1,2) = 8 + 8')

    BL_raw = [F(1), F(1), F(1), F(-3)]
    check('(2) the 3+1 generator diag(1,1,1,-3) is traceless and commutes with colour (equal on the three)',
          sum(BL_raw) == 0 and BL_raw[0] == BL_raw[1] == BL_raw[2])

    # charges: colour index 0..2 quarks, 3 lepton; isospin +1/2 up, -1/2 down
    def charges(gen):
        # neutrino (lepton, up isospin, left): I3L=1/2, I3R=0 -> Q = 1/2 + c*gen[3] = 0
        c = -F(1, 2) / gen[3]
        out = {}
        for name, col, i3 in [('u', 0, F(1, 2)), ('d', 0, -F(1, 2)), ('nu', 3, F(1, 2)), ('e', 3, -F(1, 2))]:
            out[name + '_L'] = i3 + c * gen[col]
            out[name + '_R'] = i3 + c * gen[col]
        return c, out

    c, Q = charges(BL_raw)
    want = {'u': F(2, 3), 'd': F(-1, 3), 'nu': F(0), 'e': F(-1)}
    check(f'(3) with the neutrino neutral c*(B-L) per quark is {c * BL_raw[0]}, and Q on both chiralities is '
          f'u {Q["u_L"]}, d {Q["d_L"]}, nu {Q["nu_L"]}, e {Q["e_L"]}',
          all(Q[k + '_L'] == v and Q[k + '_R'] == v for k, v in want.items()))

    # hypercharges in P14's normalisation Q = I3 + Y, left-handed conjugate form for right-handed fields
    Y_Q = c * BL_raw[0]                      # I3R = 0 for the left doublet
    Y_L = c * BL_raw[3]
    Y_uR = F(1, 2) + c * BL_raw[0]
    Y_dR = -F(1, 2) + c * BL_raw[0]
    Y_eR = -F(1, 2) + c * BL_raw[3]
    Y_nR = F(1, 2) + c * BL_raw[3]
    got = {'Q': Y_Q, 'uc': -Y_uR, 'dc': -Y_dR, 'L': Y_L, 'ec': -Y_eR, 'nuc': -Y_nR}
    p14 = {'Q': F(1, 6), 'uc': F(-2, 3), 'dc': F(1, 3), 'L': F(-1, 2), 'ec': F(1), 'nuc': F(0)}
    check('(4) Y = I3R + c(B-L) returns P14\'s hypercharges: ' + ', '.join(f'{k} {got[k]}' for k in got),
          got == p14)

    bad = [F(1), F(1), F(1), F(1)]
    cb, Qb = (None, None)
    try:
        cb, Qb = charges(bad)
        ok = not (Qb['nu_L'] == 0 and Qb['u_L'] == F(2, 3))
    except ZeroDivisionError:
        ok = True
    check('CONTROL (5): the non-traceless diag(1,1,1,1) cannot give a neutral neutrino and u = 2/3 together '
          f'(it gives u = {Qb["u_L"] if Qb else "undefined"} once the neutrino is neutral)', ok)

    p = flat(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex'))
    check('P14 carries the reading: "That right-handed structure has a name, and the sector\'s own counts already have its shape"',
          "That right-handed structure has a name, and the sector's own counts already have its shape" in p)
    check('P14 carries the bound: "neither is a gauge group of the matter"',
          'neither is a gauge group of the matter' in p)
    print()
    if FAILED:
        print(f'  {len(FAILED)} FAILED')
        return 1
    print('  all checks pass')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
