# How the three spectra here were made (`POLSAVE`, r7631+70)
All three runs are from `computations/beyond_the_wall`, on `ACOUSTIC_two_arm.py` with `HIER=1 LSTEP=8 LMAXL=2000 POLSAVE=<npz>`, plus:
- **pol_lcdm.npz:** `ARM=lcdm LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248`. r6941's control; its TT equals `spectra/cc66_r185_verify_lcdm.npz` exactly.
- **pol_cr_leafrec0.npz:** `ARM=cr CRH0=68.581133 CROM=0.297209 ZSTART=3e7 LEAFSCALES=1 WBH2=0.021524 NS=0.997952 LEAFREC=0`. r6941's configuration; its TT equals `spectra/r6941_fine_cr.npz` to 7e-16 at every shared multipole.
- **pol_cr_leafrec1.npz:** the same with `LEAFREC=1`, the instrument's ruled default since r7095.
