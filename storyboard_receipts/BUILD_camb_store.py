"""BUILD_camb_store  --  the CAMB side of the transfer comparison, with its settings RECORDED.

WHY THIS EXISTS (r2345).  `ENVELOPE_residual.py` and its relatives load `/tmp/camb_tr.npz` and
measure our transfer against CAMB's.  Nothing in the corpus records HOW that store was built --
not the receipt, not the changelog, not the instrument.  Three attempts to rebuild it (default
sampling, boosted lSampleBoost, boosted IntkAccuracyBoost) each gave a different comparison, and
none reproduced r2201's recorded numbers.

That is a reproducibility gap at exactly the place the residual is measured, and it matters more
than usual here: r2201's own headline was that "the step, threshold, k-oscillation and dip were ALL
binning artefacts" -- i.e. this measurement is known to be sensitive to sampling choices.

WHAT THIS FIXES.  The store is built here, from parameters matched to the instrument's own, with
every accuracy setting explicit and asserted.  Anything downstream can now state which store it ran
against.

MATCHING THE INSTRUMENT.  HIER_photon_hierarchy.py sets:
    H0 = 67.40 ; Om = 0.3150 ; ombh2 = 0.02237 ; z_rec = 1089.9 (typed) ; fnu = 0.4089
    omega_r = 4.1833e-5/h^2  (omega_gamma (1+0.2271 N_eff), N_eff = 3.046)
so the store uses the same, and the constraint that the wanted ell values be PRESENT in CAMB's
grid is asserted rather than hoped for -- the receipt selects ell by exact membership,
`for L in [int(v) for v in LC if v in (90,150,250,350,500,700)]`, so a shifted grid silently
yields nothing.
"""
import numpy as np
import camb

WANTED_ELLS = (90, 150, 250, 350, 500, 700)
OUT = "/tmp/camb_tr.npz"

# --- parameters matched to HIER_photon_hierarchy.py ---
H0 = 67.40
ombh2 = 0.02237
Om = 0.3150
h = H0 / 100.0
omch2 = Om * h**2 - ombh2

# --- accuracy settings, EXPLICIT ---
LMAX = 1500
ACCURACY_BOOST = 1.0        # default; raising it does not shift the ell grid
L_SAMPLE_BOOST = 1.0        # MUST stay 1.0: boosting moves the grid off the wanted ells
INTK_BOOST = 1.0            # k sampling; 3.0 triples the window count without changing the shape

pars = camb.CAMBparams()
pars.set_cosmology(H0=H0, ombh2=ombh2, omch2=omch2, mnu=0.0, omk=0, tau=0.0544)
pars.InitPower.set_params(As=2.1e-9, ns=0.965)
pars.set_for_lmax(LMAX, lens_potential_accuracy=0)
pars.Accuracy.AccuracyBoost = ACCURACY_BOOST
pars.Accuracy.lSampleBoost = L_SAMPLE_BOOST
pars.Accuracy.IntkAccuracyBoost = INTK_BOOST

res = camb.get_results(pars)
tr = res.get_cmb_transfer_data()
L = np.array(tr.L)
q = np.array(tr.q)

print("   parameters : H0=%.2f  ombh2=%.5f  omch2=%.5f  (Om=%.4f)" % (H0, ombh2, omch2, Om))
print("   accuracy   : AccuracyBoost=%.1f  lSampleBoost=%.1f  IntkAccuracyBoost=%.1f  lmax=%d"
      % (ACCURACY_BOOST, L_SAMPLE_BOOST, INTK_BOOST, LMAX))
print("   grid       : %d ells (%d..%d) ; %d q (%.2e..%.3f)" % (len(L), L[0], L[-1], len(q), q[0], q[-1]))

present = [int(x) for x in WANTED_ELLS if x in L]
missing = [int(x) for x in WANTED_ELLS if x not in L]
print("   wanted ells present : %s" % present)
if missing:
    print("   wanted ells MISSING : %s" % missing)
assert not missing, ("the receipt selects ell by exact membership; a grid missing %s "
                     "yields an empty comparison silently" % missing)

win = (q >= 0.004) & (q <= 0.095)
print("   q points in the comparison window [0.004,0.095] : %d" % win.sum())
assert win.sum() > 300, "too few k points in the window for extremum matching"

d = tr.delta_p_l_k
print("   delta_p_l_k shape : %s   (axis 0 = T,E,phi ; the receipt uses [0])" % (d.shape,))
assert d.shape[0] >= 1 and d.shape[1] == len(L) and d.shape[2] == len(q)

# derived scales, for the record and for comparison with the instrument's own
der = res.get_derived_params()
print("   derived    : r_star=%.2f  r_drag=%.2f  D_A*=%.1f  100theta*=%.5f"
      % (der['rstar'], der['rdrag'], der['DAstar'] * 1000, der['thetastar']))
print("   (the instrument's control reports r_s=143.99, D=13864, l_A=302.5 -- r_star is the")
print("    like-for-like number, NOT r_drag)")

np.savez(OUT, d=d, L=L, q=q)
print("   saved %s" % OUT)
print()
print("   RECORDED.  Anything measuring against this store should cite these settings.")
