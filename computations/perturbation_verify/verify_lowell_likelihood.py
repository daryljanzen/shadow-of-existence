"""
E2 -- the likelihood-level CR-vs-LCDM comparison at low ell.  (added 2026-06-30, r546 spearhead)

P13 sec:scope item 3: "the largest blind spot in the empirical claim" -- the confrontations so far
are parameter-free ratio comparisons, NOT a statistical model selection with an error budget. This
builds the proper instrument: the EXACT low-ell cosmic-variance likelihood, and asks (i) which model
the observed low multipoles prefer, and (ii) whether the low-ell sector can DISCRIMINATE at all.

THE LIKELIHOOD (exact, full-sky, cosmic-variance-dominated -- the right leading instrument at ell<30,
where cosmic variance, not noise/mask, dominates):
  the full-sky estimator Chat_ell = (1/(2ell+1)) sum_m |a_lm|^2 has (2ell+1) dof; given a model C_ell,
  (2ell+1) Chat_ell / C_ell ~ chi^2_{2ell+1}.  So, up to model-independent constants,
     -2 ln L(model) = sum_ell (2ell+1) [ Chat_ell / C_ell + ln C_ell ].
  The model COMPARISON is the likelihood ratio (the absolute baseline B=C_ell^LCDM CANCELS, so only
  the CR/LCDM ratios are needed):  writing r_C = C^CR/C^LCDM and r_obs = Chat/C^LCDM,
     Delta(-2lnL)_ell = (2ell+1) [ r_obs (1/r_C - 1) + ln r_C ]      (CR worse if >0, better if <0).

INPUTS, grounded at source:
  r_C (CR/LCDM, full radiative order: verify_lowell_full_radiative.py / confront_lowell_data.py):
     ell: 2     3     4     5     6     7    >=8
     r_C: 0.22  0.20  0.31  0.70  0.93  0.98  1.00
  r_obs (observed/LCDM, central + estimator range; confront_lowell_data.py literature set:
     Efstathiou astro-ph/0310207; A&A 2021 aa41251-21; Planck 2013 XXIII; Bennett 2011):
     ell:    2            3            4            5            6        >=7
     range:  0.15-0.25    0.58-1.10    0.55-1.05    0.70-1.10    0.85-1.05  ~1.0
  (the ell=3 octopole is the estimator-sensitive one: WMAP-team low ~0.6, Efstathiou mid/high ~1.0.)

WHAT THE NUMBERS MEAN (the cosmic-variance penalty is asymmetric):  (1/r-1)+ln r >= 0 always, so if
LCDM is true CR is disfavoured on average; (1-r)+ln r <= 0, so if CR is true CR is favoured -- the
likelihood is honest in both directions.  Under-predicting power where the data are NOT low (the
octopole, if r_obs(3) ~ 1) is penalised hard (Chat/C blows up); matching low power where the data ARE
low (the quadrupole) is rewarded.  The net is the question.
"""
import numpy as np
rng = np.random.default_rng(0)

ells = np.arange(2, 31)
# CR/LCDM ratio prediction (radiative); 1.0 for ell>=8
rC = {2:0.22, 3:0.20, 4:0.31, 5:0.70, 6:0.93, 7:0.98}
r_C = np.array([rC.get(l, 1.0) for l in ells])
# observed/LCDM: central, low (CR-favourable), high (CR-unfavourable)
obs_c  = {2:0.20, 3:0.84, 4:0.80, 5:0.90, 6:0.95}
obs_lo = {2:0.15, 3:0.58, 4:0.55, 5:0.70, 6:0.85}
obs_hi = {2:0.25, 3:1.10, 4:1.05, 5:1.10, 6:1.05}
def rvec(d): return np.array([d.get(l, 1.0) for l in ells])

g = 2*ells + 1
def dlnL_per_ell(r_obs):                       # Delta(-2lnL) per ell, CR vs LCDM
    return g * (r_obs*(1.0/r_C - 1.0) + np.log(r_C))
def dlnL(r_obs): return dlnL_per_ell(r_obs).sum()

if __name__ == "__main__":
    print("="*74)
    print("E2 -- exact low-ell cosmic-variance likelihood: CR vs LCDM model comparison")
    print("="*74)

    # --- per-ell decomposition (central data) ---------------------------------------------------
    print("\n[1] Delta(-2lnL) per multipole (central data); + = CR worse, - = CR better")
    per = dlnL_per_ell(rvec(obs_c))
    print("  ell  r_C   r_obs   (2l+1)   Delta(-2lnL)   verdict")
    for i, l in enumerate(ells):
        if l <= 8:
            ro = rvec(obs_c)[i]
            v = "CR better" if per[i] < -0.5 else ("CR worse" if per[i] > 0.5 else "~neutral")
            print(f"   {l:2d}  {r_C[i]:.2f}  {ro:.2f}    {g[i]:2d}      {per[i]:+7.2f}      {v}")
    print(f"  ell>=9 contribute ~0 (r_C=r_obs=1).  SUM(2<=ell<=30) = {dlnL(rvec(obs_c)):+.2f}")

    # --- data-range sensitivity -----------------------------------------------------------------
    print("\n[2] Net Delta(-2lnL) across the estimator range (the octopole drives it):")
    for tag, d in (("CR-favourable (low obs) ", obs_lo), ("central                 ", obs_c), ("CR-unfavourable (high)  ", obs_hi)):
        D = dlnL(rvec(d))
        pref = "CR preferred" if D < 0 else "LCDM preferred"
        print(f"   {tag}: Delta(-2lnL) = {D:+6.2f}  -> {pref} (by |Delta| = {abs(D):.1f})")

    # --- Monte-Carlo: CAN the low-ell sector discriminate, and what does the sky say? -----------
    # Under a true model M, Chat_ell = C_ell^M * chi^2_{2l+1}/(2l+1).  In ratio units C^LCDM=1:
    #   LCDM-true: r_obs_sim = g_chi              CR-true: r_obs_sim = r_C * g_chi
    print("\n[3] Monte-Carlo discriminating power (10000 skies each, 2<=ell<=30):")
    N = 10000
    gx = rng.chisquare(df=g[None, :], size=(N, len(ells))) / g[None, :]   # chi^2/(dof), mean 1
    D_lcdm = (g * (gx*(1.0/r_C - 1.0) + np.log(r_C))).sum(axis=1)          # LCDM-true skies
    D_cr   = (g * (r_C*gx*(1.0/r_C - 1.0) + np.log(r_C))).sum(axis=1)      # CR-true skies
    for tag, arr in (("if LCDM true", D_lcdm), ("if CR true  ", D_cr)):
        print(f"   {tag}: <Delta(-2lnL)> = {arr.mean():+6.1f}  std = {arr.std():4.1f}  "
              f"[16-84%: {np.percentile(arr,16):+.1f}, {np.percentile(arr,84):+.1f}]")
    # how often does each true-model sky land on the 'right' side (Delta<0 => looks CR-like)?
    sep = (D_lcdm.mean() - D_cr.mean()) / np.sqrt(0.5*(D_lcdm.var()+D_cr.var()))
    print(f"   model separation (mean gap / pooled std) = {sep:.2f} sigma  "
          f"-> {'DISCRIMINATING' if sep>3 else 'WEAK at low-ell alone' if sep>1 else 'CANNOT discriminate'}")
    Dobs = dlnL(rvec(obs_c))
    pctl_l = (D_lcdm < Dobs).mean()*100; pctl_c = (D_cr < Dobs).mean()*100
    print(f"   observed Delta(-2lnL) = {Dobs:+.1f} sits at the {pctl_l:.0f}th pctile of LCDM-true, "
          f"{pctl_c:.0f}th of CR-true")

    print("\n[VERDICT]")
    Dc, Dl, Dh = dlnL(rvec(obs_c)), dlnL(rvec(obs_lo)), dlnL(rvec(obs_hi))
    print(f" - Net Delta(-2lnL) spans {Dl:+.0f} (low-obs) to {Dh:+.0f} (high-obs), central {Dc:+.0f}:")
    print("   the SIGN itself flips with the octopole estimator -- the low-ell verdict is")
    print("   estimator-limited, not a clean preference either way.")
    print(f" - Model separation ~{sep:.1f}sigma: the low-ell sector ALONE {'can' if sep>3 else 'CANNOT cleanly'}")
    print("   discriminate CR from LCDM -- cosmic variance + the 29-multipole lever arm are too short.")
    print(" - The quadrupole REWARDS CR (matches the low power); the octopole PENALISES it if the")
    print("   octopole is near-LCDM, and the penalty is the larger effect under the exact likelihood")
    print("   -- so the eyeball '<3sigma' was right that it is not decisive, but the proper instrument")
    print("   shows the octopole carries MORE weight than the quadrupole, and the data uncertainty")
    print("   (not cosmic variance alone) is what keeps it from a verdict.")
    print(" - Decisiveness must come from OUTSIDE the low-ell sector: the geometric stacking rate")
    print("   discriminator and the full spectrum -- the low multipoles are a genuine but blunt test.")
    print("="*74)
