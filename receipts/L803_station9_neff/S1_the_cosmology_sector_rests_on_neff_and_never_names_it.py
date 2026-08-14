#!/usr/bin/env python3
r"""S1 -- R-P STATION 9 (cosmology . nuclear/plasma) WALKED, computationally: the sector rests on the
EFFECTIVE NUMBER OF RELATIVISTIC SPECIES, N_eff, at BOTH ends -- the BBN abundances and the CMB acoustic
scale it predicts to 15.7 sigma -- and (at r2541) it NEVER NAMED IT. The field's first BBN/CMB question was
invisible to a reader who searched for it, and the corpus adopted the standard value without stating it did.

** APPLIED r2673-era -- and this receipt is RE-ANCHORED to say so (per r2673's rule: a receipt whose finding
gets acted on is updated to assert the state the corpus now holds, finding preserved). 54 wrote the paragraph
this receipt asked for: cosmogenesis_paper.tex now NAMES $N_{\mathrm{eff}}=3.046$~\cite{Mangano2005}, "adopted
here rather than derived", and states the construction "makes no $N_{\mathrm{eff}}$ prediction; the standard
value is adopted" and is "consistent with the fourth grading". Check (1) below, which found N_eff absent by
name, is therefore now correctly FALSE and is re-anchored to assert the applied state; the physics checks
(2a/2b -- the BBN and camb leverage) are unchanged and still pass, because the finding was never that the
sector was wrong, only that the load-bearing parameter was unnamed. **

** Board lead L-803 (cc54's band); walks R-P station 9 (THE_PHYSICS_REACH: P7/P15/P16 -- BBN, recombination,
the acoustic scale), the last unrun station and the computational one -- cc54's camb/pynucastro instrument.
Same shape as station 6 (the Higgs, "declined and never named") and station 10 (the baby-universe
resolution, "the answer is in the sentence, never named"): here N_eff is ADOPTED and never named. **

** THE DISCIPLINE (from stations 5/6/10). ** Check whether the corpus ANSWERS the field's question before
reporting a gap. It does: the BBN engine commits to the standard neutrino sector, so this is an UNNAMED
ADOPTION, not an owe -- and the finding is that nobody could tell, because the name a reader searches for
is absent while the number is fixed in code.

** THE ABSENCE, measured across the 35 .tex files. **  N_eff / "N_{\rm eff}" / "effective number of" /
"number of neutrino" / "relativistic species" / "3.046" / "3.044": ZERO. The single parameter every BBN
and every CMB analysis organises around does not appear by name anywhere in the corpus. (For contrast the
sector is otherwise deep: the lithium problem is named and worked, deuterium/helium/Yp/nucleosynthesis
are everywhere, the Hubble tension is engaged -- so this is one missing name, not a missing sector.)

** THE ANSWER THAT IS NEVERTHELESS THERE. **  bbn_network.py commits to it in code, unnamed: "nu decoupling
(g_*(T), g_{*s}(T), T_nu/T -> (4/11)^{1/3})" and "3 nu (7/8*2 each, at T_nu)" -- which IS the standard
three-species N_eff ~ 3.046 background. The validation receipt then reproduces Y_p = 0.247, D/H = 2.5e-5,
7Li/H, the lithium problem's 2.8x over-prediction, and confronts the data at D -0.5sigma, He +0.5sigma,
Li +7.8sigma. ** So the sector MEETS the field on abundances -- at a value of N_eff it fixes and never states. **

** THE COMPUTATION (cc54's instrument): N_eff is LOAD-BEARING AT BOTH ENDS. **
  BBN.  Extra relativistic species raise g_*, so the universe expands faster (H ~ sqrt(g_*)), the weak
    n<->p rates freeze out EARLIER (T_f ~ g_*^{1/6}), a larger n/p ratio survives, and Y_p RISES. Computed
    here from the corpus's own g_* accounting: d Y_p / d N_eff > 0 and of order +0.01, the standard BBN
    sensitivity -- so the validated Y_p = 0.247 is a value AT N_eff = 3.046 and would move if N_eff did.
  CMB.  Run through camb: raising N_eff by one shifts the acoustic angular scale 100*theta_* by ~ -3.3%
    and the drag sound horizon r_drag by ~ -4.8 Mpc. ** That is a ~3% lever, per unit N_eff, on exactly the
    quantities R-P station 9's own build predicts -- ell_A to 0.075% and theta_D/theta_* to 15.7 sigma. **
  ** So the corpus's two headline station-9 results, the BBN abundances and the CMB acoustic/damping
    prediction, are BOTH functions of N_eff, and it is named in neither. **

** THE VERDICT (station 9 walked). **  N_eff is the hinge between the sector's two computations and the
field's first question of it, and it is absent by name while fixed to the standard value in code. The fix
is station 6's and station 10's: a paragraph that NAMES the parameter -- states N_eff = 3.046 is adopted,
standard, and confront-able (Planck: N_eff = 2.99 +/- 0.17) -- so a reader can find the corpus's stance.
The reason the missing name is not merely cosmetic: CR carries a specific neutrino structure (a right-handed
nu_R in the colourless four, PO-5/L-221), so whether the construction ADOPTS the standard N_eff or PREDICTS
a departure is a real question -- and the unnamed adoption is exactly what hides it.

WHAT IS NOT CLAIMED, stated for reversal.
  ** Not that CR predicts a non-standard N_eff ** -- the code adopts the standard three-species value, and
  whether CR's nu_R structure implies any departure is a construction question, not examined here. ** Not a
  physics error ** -- the BBN physics is standard and correct and the validation passes; this is an
  arrival-path finding (a missing NAME), the station's own currency, not a defect in the sector. ** Not
  that the sector is thin ** -- it is one of the corpus's deepest, which is why a single unnamed parameter
  is the whole finding. ** Not a new acoustic result ** -- the camb runs quantify the LEVERAGE of the
  unnamed parameter on the existing prediction; they do not re-derive or contest it, and the seam-phase
  front is untouched.

Written r2541 (cc54, L-803, station 9). Asserts against SOURCES (bbn_network.py's own commitment, the
corpus grep) and the computation (camb + the freeze-out sensitivity) -- never against the register.
Planck N_eff = 2.99 +/- 0.17 (Planck 2018, TT,TE,EE+lowE+lensing). Stated for reversal.
"""
import os
import re
import subprocess

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def corpus_count(term):
    """literal-substring count across all corpus .tex, comment lines stripped."""
    n = 0
    tex = os.path.join(ROOT, 'corpus')
    for f in os.listdir(tex):
        if not f.endswith('.tex'):
            continue
        body = '\n'.join(l for l in open(os.path.join(tex, f), encoding='utf-8',
                                         errors='replace').read().split('\n')
                         if not l.lstrip().startswith('%'))
        n += body.count(term)
    return n


def yp_freezeout(neff):
    """Standard weak n<->p freeze-out Y_p(N_eff), self-contained.
    g_* at ~1 MeV: photons(2) + e+-(7/8*4) + neutrinos(7/8*2*N_eff).  H ~ sqrt(g_*),
    Gamma_weak ~ T^5, so freeze-out T_f ~ g_*^(1/6); n/p = exp(-Q/T_f); Y_p = 2 r/(1+r)
    with a common neutron-decay factor to t_BBN.  Absolute value is a simple-model estimate
    (the corpus's full network gives 0.247); the SIGN and SCALE of dY_p/dN_eff are the point."""
    Q = 1.293                       # MeV, n-p mass gap
    gstar = 2.0 + (7.0 / 8.0) * 4.0 + (7.0 / 8.0) * 2.0 * neff
    # anchor T_f = 0.80 MeV at the standard g_* (N_eff=3.046), scale as g_*^(1/6)
    g0 = 2.0 + (7.0 / 8.0) * 4.0 + (7.0 / 8.0) * 2.0 * 3.046
    T_f = 0.80 * (gstar / g0) ** (1.0 / 6.0)
    r_f = np.exp(-Q / T_f)
    decay = np.exp(-200.0 / 880.0)  # common neutron-decay suppression to ~t_BBN
    r = r_f * decay
    return 2.0 * r / (1.0 + r)


def camb_derived(neff):
    """theta_* and r_drag from camb at a fiducial Planck cosmology, massless neutrinos."""
    import camb
    p = camb.set_params(H0=67.36, ombh2=0.02237, omch2=0.1200, ns=0.9649, As=2.1e-9,
                        tau=0.0544, mnu=0.0, num_massive_neutrinos=0, nnu=neff)
    dp = camb.get_results(p).get_derived_params()
    return dp['thetastar'], dp['rdrag']    # camb's 'thetastar' is already 100*theta_*


def main():
    print()
    print('  S1 -- R-P station 9: does the cosmology/nuclear sector name N_eff, the field\'s first question?')
    print()

    # ---- (1) the finding was APPLIED (r2673-era): N_eff is now NAMED, not absent -------------------
    # ** This receipt walked station 9 at r2541 and found N_eff absent by name.  54 applied the fix --
    #    the paragraph that names it -- so the ORIGINAL check ("absent by name, ZERO hits") is now
    #    correctly FALSE.  Re-anchored to the applied state per r2673's rule: a receipt whose finding
    #    gets acted on is updated to assert the state the corpus now holds, finding preserved. **
    variants = ['N_{\\mathrm{eff}}', 'N_{\\rm eff}', 'N_\\mathrm{eff}', 'effective number', '3.046']
    hits = {v: corpus_count(v) for v in variants}
    cosmo = open(os.path.join(ROOT, 'corpus', 'cosmogenesis_paper.tex'),
                 encoding='utf-8', errors='replace').read()
    check('cc54\'s station-9 finding was APPLIED -- N_eff is now NAMED in the corpus '
          f'(variants {", ".join(repr(v) for v in variants[:3])} ... now count {sum(hits.values())}, '
          'not the ZERO this receipt found at r2541)',
          sum(hits.values()) > 0)
    check('and the paper takes the corpus\'s stance in its own voice: it adopts the Standard Model '
          '$N_{\\mathrm{eff}}=3.046$ "rather than derived" and says the construction "makes no '
          '$N_{\\mathrm{eff}}$ prediction; the standard value is adopted" -- the exact paragraph this '
          'receipt asked for',
          'N_{\\mathrm{eff}}=3.046' in cosmo
          and 'makes no $N_{\\mathrm{eff}}$ prediction' in cosmo
          and 'adopted' in cosmo)
    # and the sector is otherwise deep -- so it is one missing name, not a missing sector
    check('yet the sector is deep: "lithium problem", "deuterium", "nucleosynthesis" and "Hubble '
          'tension" are all present -- so this is ONE MISSING NAME, not a missing sector',
          corpus_count('lithium problem') > 0 and corpus_count('deuterium') > 0
          and corpus_count('nucleosynthesis') > 0 and corpus_count('Hubble tension') > 0)

    # ---- the discipline: the corpus ANSWERS N_eff in code, unnamed ---------------------------------
    bbn = open(os.path.join(ROOT, 'computations', 'p16_bbn', 'bbn_network.py'),
               encoding='utf-8', errors='replace').read()
    check('the answer is nonetheless COMMITTED in code (bbn_network.py), unnamed: the standard '
          'three-species neutrino background, "(4/11)^{1/3}" decoupling and "3 nu" in g_* -- '
          'i.e. N_eff ~ 3.046 fixed and never stated',
          ('(4/11)' in bbn) and ('3 nu' in bbn) and ('decoupl' in bbn.lower())
          and 'neff' not in bbn.lower() and '3.046' not in bbn)

    # ---- (2a) BBN: N_eff is load-bearing on Y_p, from the corpus's own g_* accounting --------------
    yp_lo, yp_std, yp_hi = yp_freezeout(2.046), yp_freezeout(3.046), yp_freezeout(4.046)
    dyp = yp_hi - yp_std
    check('BBN: raising N_eff RAISES Y_p (faster expansion -> earlier n/p freeze-out -> more neutrons): '
          f'Y_p({2.046:.3f})={yp_lo:.3f} < Y_p({3.046:.3f})={yp_std:.3f} < Y_p({4.046:.3f})={yp_hi:.3f}',
          yp_lo < yp_std < yp_hi)
    check('and the sensitivity dY_p/dN_eff is positive and of order the standard +0.01 '
          f'(computed {dyp:+.3f} per unit N_eff) -- so the validated Y_p=0.247 is a value AT N_eff=3.046',
          0.003 < dyp < 0.03)

    # ---- (2b) CMB: N_eff is a ~3% lever on the acoustic scale the sector predicts -----------------
    th_std, rd_std = camb_derived(3.046)
    th_hi, rd_hi = camb_derived(4.046)
    dth_pct = 100.0 * (th_hi - th_std) / th_std
    check('CMB (camb): the standard N_eff reproduces the measured acoustic scale, 100*theta_* ~ 1.0404 '
          f'(got {th_std:.4f}) and r_drag ~ 147 Mpc (got {rd_std:.1f})',
          abs(th_std - 1.0404) < 0.01 and abs(rd_std - 147.0) < 2.0)
    check('and raising N_eff by ONE shifts 100*theta_* by ~ -3% and r_drag by ~ -5 Mpc '
          f'(got {dth_pct:+.2f}% and {rd_hi - rd_std:+.1f} Mpc) -- a large lever, per unit N_eff, on '
          'exactly the ell_A/r_s the sector predicts to 0.075%/15.7 sigma',
          dth_pct < -2.0 and (rd_hi - rd_std) < -3.0)

    # ---- the finding matters because CR carries a specific neutrino structure ----------------------
    matter = '\n'.join(open(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex'),
                            encoding='utf-8', errors='replace').read().split('\n'))
    check('and the missing name is load-bearing for CR specifically: the construction carries a '
          'right-handed neutrino (nu_R) in its matter content, so whether it ADOPTS the standard '
          'N_eff or predicts a departure is a real question the unnamed adoption hides',
          ('nu_R' in matter) or ('\\nu_R' in matter) or ('right-handed' in matter.lower())
          or ('nu_{R}' in matter))

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (R-P station 9 walked -- the computational station, cc54\'s instrument -- and APPLIED):')
    print('  ** THE SECTOR RESTS ON N_eff AT BOTH ENDS; at r2541 it never named it, and NOW IT DOES. ** '
          'The BBN')
    print('     abundances (Y_p rises with N_eff) and the CMB acoustic scale (100*theta_* moves ~3% per '
          'unit N_eff)')
    print('     are both functions of it; the code fixes it to the standard 3.046 via the (4/11)^{1/3} '
          'background;')
    print('     and cosmogenesis_paper.tex now NAMES N_eff=3.046 (adopted, standard) and says the '
          'construction')
    print('     makes no N_eff prediction, consistent with the fourth grading -- the paragraph this '
          'receipt asked for.')
    print('  => Station 6\'s and station 10\'s shape, now discharged: the answer was present and unnamed; '
          'it is named.')
    print('     Informs the R-P front (L-204) and, through the nu_R question, L-221 (PO-5). The BBN '
          'physics is standard;')
    print('     the finding is the missing name.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
