#!/bin/bash
# r7635+70: the older CR files of CENSUS.md §B (c54.*, item38, r4494, r6784/r6794, cc66_cr_x_*, cc66_refit_verify),
# regenerated on the arm of record.  Recipes from spectra/README.md, _item38_seamphase_scan.sh and the receipts'
# docstrings (RECIPES.md has the table and the sources).  The FORM switches are kept; the POINT is the arm of
# record (ZSTART=3e7 LEAFSCALES=1 LEAFREC=1 and the refitted four), replacing both the old built-in-default point
# with its LATARG-solved onset (c54/item38/r4494) and the old CRH0/CROM points (r6784/r6794/cc66).
# ⚠ KFAC=1, which the c54/item38 files were made at, is refused by today's alias gate: these run at KFAC=2.
# ⚠ c54.186_cr_KCONT: at KFAC=2 its NK=600 continuum is 2.8 points per Bessel period and the sampling gate refuses it;
#   NK=1200 restores the namesake's 5.7 points per period (3600 modes), which is the property its README row names.
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=${D:-/tmp/claude-0/-home-user-shadow-of-existence/4913e7eb-3c04-585c-bc52-ac1b69fc5eb8/scratchpad/bank}
mkdir -p $D/old $D/r6794
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
P="CRH0=68.570730 CROM=0.291246 WBH2=0.021643 NS=1.015066 LEAFSCALES=1 LEAFREC=1"
CR="ARM=cr $P ZSTART=3e7"
F178="HIER=1 BSPLIT=1 NK=600 LMAXL=2000 ETAEND=4000 KBATCH=300"
F186="HIER=1 BSPLIT=1 NK=900 LMAXL=3000 ETAEND=4000 KBATCH=300"
run () { out=$1; tag=$2; shift 2
  [ -s "$out/$tag.log" ] && grep -q '^__DONE__ rc=0' "$out/$tag.log" && { echo "  skip $tag"; return 0; }
  env "$@" SAVE=$out/$tag.npz python3 -u ACOUSTIC_two_arm.py > $out/$tag.log 2>&1
  rc=$?
  line=$(grep -m1 '^__SWITCHES__ ' "$out/$tag.log")
  for a in "$@"; do
    case " $line " in *" $a "*) ;; *) echo "  ⛔ $tag: '$a' NOT in the switch line"; rc=90 ;; esac
  done
  echo "__DONE__ rc=$rc" >> "$out/$tag.log"; echo "  done $tag rc=$rc $(date -u +%H:%M:%S)"; }
export -f run; export D
O=$D/old
L="
$O c54.186_cr_L3000 $CR $F186
$O c54.191_cr_lA340_L3000 ARM=cr $P LATARG=340 $F186
$O c54.191_cr_phipi_L3000 $CR $F186 CRPHI=3.1416
$O c54.193_cr_nodrive_L3000 $CR $F186 NODRIVE=1
$O c54.195_cr_phi0.7854_L3000 $CR $F186 CRPHI=0.7854
$O c54.195_cr_phi1.5708_L3000 $CR $F186 CRPHI=1.5708
$O c54.175_cr $CR NK=600 LMAXL=2000 ETAEND=4000 BSPLIT=0 POLC=0.8888888889
$O c54.177_cr $CR NK=600 LMAXL=2000 ETAEND=4000 BSPLIT=0
$O c54.178_cr $CR $F178
$O c54.186_cr_KCONT $CR HIER=1 BSPLIT=1 NK=1200 LMAXL=2000 ETAEND=4000 KBATCH=300 KCONT=1
$O r6784_cr_crossing_hier $CR $F178 CRIC=branchpoint
$O r6784_cr_crossing_hier_noCRIC $CR $F178
$O r6784_cr_crossing_los $CR BSPLIT=1 NK=600 LMAXL=2000 ETAEND=4000 KBATCH=300 CRIC=branchpoint
$O r4494_cr_leaf_ISWon $CR LMAXL=1300 LSTEP=4
$O r4494_cr_leaf_ISWoff $CR LMAXL=1300 LSTEP=4 NOISW=1
$O r4494_cr_stack_ISWon $CR LMAXL=1300 LSTEP=4 STACKPERT=1
$O r4494_cr_stack_ISWoff $CR LMAXL=1300 LSTEP=4 STACKPERT=1 NOISW=1
$O cc66_cr_x_h686_pol $CR HIER=1 LSTEP=2 LMAXL=1300
$O cc66_cr_x_h686_L2000 $CR HIER=1 LSTEP=2 LMAXL=2000
$O cc66_refit_verify_cr $CR HIER=1 LSTEP=8 LMAXL=1300
$O cc66_cr_x_lstep1 $CR HIER=1 LSTEP=1 LMAXL=1300"
for a in 0 450 900 1350 1800 2250; do L="$L
$D/r6794 kc_k$a $CR HIER=1 BSPLIT=1 NK=900 LMAXL=2000 ETAEND=4000 KBATCH=150 KCONT=1 KSLICE=$a:$((a+450))"; done
printf '%s' "$L" | sed '/^$/d' | xargs -P 4 -I{} bash -c 'run {}'
echo "=== r7635 OLD BATCH COMPLETE $(date -u) ==="
