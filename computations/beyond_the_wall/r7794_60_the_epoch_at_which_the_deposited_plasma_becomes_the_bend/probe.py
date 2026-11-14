#!/usr/bin/env python3
"""r7794 (60) -- the epoch at which the deposited plasma becomes the bend.

POST-REGISTRATION throughout: PREDICTION.md was committed AND pushed before this file existed.
Nine arms, each a comparison with a reachable negative named in the registration.

READS DECLARED
  corpus/CR_framework.tex    -- thm:bead's material and sec:lift-initial-rate
  corpus/CR_cosmology.tex    -- sec:scope, sec:flatlcdm, sec:properframe
  corpus/cosmogenesis_paper.tex -- the deposition paragraphs
  corpus/dynamics_paper.tex  -- ** A WIDENING OF THE REGISTERED SCOPE, DECLARED AND NOT HIDDEN: the
     registration named four regions and not this paper, and this paper is titled "Why the cut bends".
     A search for an onset of the bend that skipped the paper about the bend would be scoped and
     misleading at once. **  THE_REGISTER.md is read for its own printed crossover figure.
NOTHING HERE FITS ANYTHING.  Every constant is derived below from the published pair and omega_gamma.
"""
import io
import os
import re

import numpy as np

ROOT = '/home/user/shadow-of-existence'
VERDICTS = []


def arm(n, title, ok, *lines):
    VERDICTS.append((n, ok, title))
    print(f"\n{'=' * 100}\nARM {n} -- {title}\n  [{'PASS' if ok else 'FAIL'}]")
    for ln in lines:
        print(ln)


def flat(name):
    return ' '.join(io.open(os.path.join(ROOT, name), encoding='utf-8',
                            errors='replace').read().split())


def sents(t):
    return [' '.join(s.split()) for s in re.split(r'(?<=[.!?])\s+', t) if s.strip()]


P7, P15 = flat('corpus/CR_framework.tex'), flat('corpus/CR_cosmology.tex')
P16, PBEND = flat('corpus/cosmogenesis_paper.tex'), flat('corpus/dynamics_paper.tex')
REG = flat('THE_REGISTER.md')

# ------------------------------------------------------------- the constants, derived not quoted
CLIGHT = 299792.458
H0, OM = 68.6, 0.2973
OMR = 4.15e-5 / (H0 / 100.0) ** 2
OL = 1.0 - OM
hub = H0 / CLIGHT
X0 = (2 * OL / OM) ** (1 / 3)
ALPHA = 1.0 / (hub * np.sqrt(OL))
R0 = ALPHA * X0 / np.sqrt(3.0)
TWOM = 2 * R0 ** 3 / (ALPHA ** 2 * X0 ** 3)
KRAD = hub ** 2 * OMR * R0 ** 4
T_CMB = 2.7255                       # K, the measured photon temperature; INPUT, corpus measured
M_E_EV = 510998.95                   # eV, the electron mass; INPUT, a physical constant
K_B_EV = 8.617333262e-5              # eV/K

print("=" * 100)
print("r7794 (60) -- the epoch at which the deposited plasma becomes the bend (order r7779/r7783)")
print(f"  derived: alpha={ALPHA:.3f} Mpc  r0={R0:.3f} Mpc  2M={TWOM:.4f} Mpc  K={KRAD:.3f} Mpc^2")
print("=" * 100)

# ======================================================= A -- DOES THE CORPUS STATE AN ONSET AT ALL?
REGIONS = {}


def region(text, start, end, label):
    i = text.find(start)
    if i < 0:
        REGIONS[label] = ''
        return
    j = text.find(end, i + len(start))
    REGIONS[label] = text[i:j if j > 0 else len(text)]


region(P7, r'\begin{theorem}[The cosmogenetic bead]', r'\begin{lemma}[Two turnings]', 'P7 thm:bead material')
region(P7, r'\label{sec:lift-initial-rate}', r'\label{sec:central}', 'P7 sec:lift-initial-rate')
region(P15, r'\label{sec:scope}', r'\section', 'P15 sec:scope')
region(P15, r'\label{sec:flatlcdm}', r'\section', 'P15 sec:flatlcdm')
region(P15, r'\label{sec:properframe}', r'\section', 'P15 sec:properframe')
REGIONS['P16 (deposition, whole paper)'] = P16
REGIONS['P-bend "Why the cut bends" (WIDENING, declared)'] = PBEND

ONSET = ('the bend begins', 'begins to bend', 'onset of the bend', 'from the epoch at which',
         'first epoch', 'becomes the bend', 'radiation begins to')
hits = []
for label, txt in REGIONS.items():
    for s in sents(txt):
        low = s.lower()
        for key in ONSET:
            if key in low and ('bend' in low or 'cut' in low):
                hits.append((label, key, s))
print("  regions searched, with their sizes in characters:")
for label, txt in REGIONS.items():
    print(f"      {label:<48s} {len(txt):>8d}")
# the NEAR MISS, kept separate on purpose: a different species at a different locus
near = [s for s in sents(P7 + ' ' + PBEND + ' ' + P16)
        if 'free gravitational radiation begins' in s.lower()]
arm(1, "does any searched region state an ONSET for the bend's radiation term?", len(hits) == 0,
    f"      sentences naming a first epoch for the bend, across the {len(REGIONS)} regions: {len(hits)}",
    *[f"        [{lab}] ...{s[:200]}" for lab, _k, s in hits[:4]],
    f"      ⌗ THE NEAR MISS, counted and set aside: {len(near)} sentence(s) say free GRAVITATIONAL",
    "        radiation BEGINS at the wall -- a different species at a different locus, and reading",
    "        it as the bend's onset is exactly the many-to-one error the guard warns about:",
    *[f"        ...{s[:190]}" for s in near[:2]],
    "  => no region searched, including the paper about the bend, names a first epoch for it")

# -- ARM 2 -------------------------------------------------------------------------------------
eta = [s for s in sents(P7 + ' ' + P16) if 'eta' in s.lower() and
       ('composition' in s.lower() or 'inherited' in s.lower() or 'deposit' in s.lower())]
epochish = [s for s in eta if re.search(r'\bepoch\b|\bredshift\b|\btemperature of\b', s.lower())]
arm(2, 'what the deposition itself fixes: a ratio, or an epoch?', len(eta) > 0 and not epochish,
    f"      sentences tying the inherited datum to the deposition: {len(eta)}",
    *[f"        ...{s[:230]}" for s in eta[:3]],
    f"      of those, any that also fix an epoch, a redshift or a temperature: {len(epochish)}",
    "  => the deposition carries a COMPOSITION, which is a ratio; it carries no time, radius or",
    "     temperature, so it cannot be the thing that fixes 'just outside'")

# ============================================================ B -- THE CROSSOVER, WHICH DOES EXIST
R_EQ = KRAD / TWOM
quart = np.roots([1.0 / ALPHA ** 2, 0.0, 0.0, -TWOM, KRAD])
pos = sorted(float(x.real) for x in quart
             if abs(x.imag) < 1e-7 * max(1.0, abs(x.real)) and x.real > 0)
s_in = pos[0]
rel = abs(s_in - R_EQ) / R_EQ
lam_term = (s_in ** 4 / ALPHA ** 2) / (TWOM * s_in)        # the Lambda term's share at that radius
arm(3, "the equality radius IS the lift's inner zero, and the difference is the Lambda term", 
    rel < 1e-9 and abs(lam_term - rel) / max(rel, 1e-300) < 0.5,
    f"      K/2M, where the radiation term equals the dust offset : {R_EQ:.12f} Mpc",
    f"      the bent radicand's inner zero (r7778, receipted r7780): {s_in:.12f} Mpc",
    f"      relative difference                                    : {rel:.3e}",
    f"      the Lambda term's share of the balance at that radius  : {lam_term:.3e}",
    "  => the lap's FOURTH SEGMENT, found at r7778 and receipted at r7780, is exactly the",
    "     radiation-dominated era of the mass function -- and the two radii differ only by Lambda")

# -- ARM 4 -------------------------------------------------------------------------------------
z_eq = R0 / R_EQ - 1.0
printed = re.findall(r'above\s+\$?z\s*(?:\\approx|≈|~)\s*([0-9]{3,5})', REG)
arm(4, "the redshift there, against the register's own printed figure",
    bool(printed) and any(abs(z_eq - float(p)) / z_eq < 0.01 for p in printed),
    f"      z at the equality radius = r0/r - 1 = {z_eq:.2f}",
    f"      figures the register prints for the mass function's radiation dominance: {printed}",
    "  => the same number, to the printed digits")

# -- ARM 5 -------------------------------------------------------------------------------------
rows, pos_all = [], True
for s in (R_EQ * 1e-2, R_EQ * 1e-1, R_EQ, R_EQ * 1e1, R_EQ * 1e2, R0):
    ratio = (KRAD / s) / TWOM
    rows.append((s, R0 / s - 1.0, KRAD / s, ratio))
    pos_all = pos_all and KRAD / s > 0
arm(5, 'it is a CROSSOVER and not an onset -- measured on both sides', pos_all,
    "      |r| (Mpc)        z            K/|r| (Mpc)     (K/r)/2M",
    *[f"      {s:12.6g}  {z:12.4g}  {k:14.6g}  {rt:12.6g}" for s, z, k, rt in rows],
    "  => the radiation term is non-zero and POSITIVE at every radius sampled across four decades",
    "     either side.  Nothing switches on at the crossover; only which term is larger changes")

# ================================================================ C -- THE THERMAL QUESTION, APART
T_eq = T_CMB * (1.0 + z_eq)
eV_eq = T_eq * K_B_EV
arm(6, 'the temperature at the crossover, and what is relativistic there',
    eV_eq < M_E_EV / 100.0,
    f"      T = T0 (1+z) = {T_CMB} x {1 + z_eq:.2f} = {T_eq:.1f} K = {eV_eq:.4f} eV",
    f"      the electron mass                                      = {M_E_EV / 1e6:.6f} MeV",
    f"      ratio kT / m_e c^2                                     = {eV_eq / M_E_EV:.3e}",
    "  => far below every species' threshold: NOTHING becomes relativistic at the crossover that",
    "     was not relativistic before it, so the crossover is not a thermal transition of the",
    "     deposited matter.  The thermal question and the crossover are two epochs, not one")

# -- ARM 7 -------------------------------------------------------------------------------------
kdef = [s for s in sents(P15) if 'microwave background' in s.lower() and
        ('temperature' in s.lower() or 'fixed by' in s.lower())]
validity = [s for s in kdef if re.search(r'valid (only )?(from|after|above)|only (after|below|above)', s.lower())]
arm(7, "what the radiation term is made of, and whether it carries an epoch of validity",
    bool(kdef) and not validity,
    f"      Omega_r derived from omega_gamma here: {OMR:.6e}"
    f"   -> K = {KRAD:.3f} Mpc^2",
    f"      sentences in P15 fixing it by the measured temperature: {len(kdef)}",
    *[f"        ...{s[:220]}" for s in kdef[:2]],
    f"      of those, any carrying an epoch of validity: {len(validity)}",
    "  => the term is the photon bath's gravitating energy, fixed by a temperature measured TODAY",
    "     and carried back by the history.  It exists at every epoch of that history, so there is",
    "     no epoch at which the bend BEGINS: it is present throughout and merely subdominant late")

# ===================================================================== D -- THE ANSWER, AND LIMITS
arm(8, "the statement the order asked for", len(hits) == 0 and rel < 1e-9,
    "      ⇒ THE QUESTION PRESUPPOSES AN ONSET AND THERE IS NONE.  What exists is a CROSSOVER,",
    f"        and it has a locus: |r| = K/2M = {R_EQ:.6f} Mpc, z = {z_eq:.1f} -- which is the same",
    "        radius as the bent lift's inner zero, so the lap's fourth segment IS that era.",
    "      ⇒ r7776's 'the bend begins just outside' should be restated:",
    "        ** the bend is SUBDOMINANT outside and DOMINANT inside, and it never begins. **",
    "      ⌗ And the near miss stays named: the corpus does state an onset for free GRAVITATIONAL",
    "        radiation, at the wall.  That is a different species at a different locus, and the",
    "        label 'radiation begins' is two-to-one on this object.")

arm(9, 'what this read cannot settle, registered so it cannot be quietly dropped', True,
    "      ⒜ the deposited plasma's own equation of state AT the branch point -- the concrete matter",
    "         model, which the corpus sends to a companion paper this repository does not carry;",
    "      ⒝ whether the progenitor's branch carries radiation at all, which r7778 left as a",
    "         disjunction over the progenitor and this read does not narrow.",
    "      ⌗ Named, not answered.")

print(f"\n{'=' * 100}")
npass = sum(1 for _, ok, _ in VERDICTS if ok)
print(f"ARMS: {npass} of {len(VERDICTS)} meet their criterion")
for n, ok, t in VERDICTS:
    print(f"  {'PASS' if ok else 'FAIL'}  arm {n}  {t}")
print(f"REGISTERED ARM COUNT: 9   MEASURED: {len(VERDICTS)}")
print('=' * 100)
