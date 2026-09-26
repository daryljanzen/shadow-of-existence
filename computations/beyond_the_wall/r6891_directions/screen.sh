#!/bin/bash
# ** r6891 order (2), measurement half.  For every environment switch this instrument reads, set it
#   away from the value it holds in the REPORTING configuration and record whether D_l moves there.
#   The reporting configuration is LOS=1 (default) + HIER=1, at each arm's own refit minimum.
#   Reduced reach (LMAXL=500, LSTEP=16) because CONNECTIVITY IS PATH-DEPENDENT AND NOT
#   RESOLUTION-DEPENDENT: a switch read on this path is read on it at any l_max.  Every switch that
#   reports NO MOVE here is re-run at full reach (LMAXL=2000) before the table calls it inert.
# ** IDEMPOTENT AND RESUMABLE **: skips any output already on disk.
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=/tmp/n66/r6891/screen; mkdir -p $D
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
LCDM="ARM=lcdm LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248"
CR="ARM=cr CRH0=68.581133 CROM=0.297209 ZSTART=3e7 LEAFSCALES=1 WBH2=0.021524 NS=0.997952"
GRID="HIER=1 LSTEP=16 LMAXL=500"
run () { tag=$1; shift
  [ -s "$D/$tag.log" ] && grep -q '^__DONE__' "$D/$tag.log" && { echo "  skip $tag"; return 0; }
  env $GRID "$@" SAVE=$D/$tag.npz python3 -u ACOUSTIC_two_arm.py > $D/$tag.log 2>&1
  echo "__DONE__ rc=$?" >> $D/$tag.log; echo "  done $tag $(date -u +%H:%M:%S)"; }
export -f run; export D GRID
# ---- the switches, one line each: "tag  base  OVERRIDE" -----------------------------------------
list () { B=$1; A=$2
 printf '%s\n' \
  "base_$A        $B" \
  "BSPLIT_$A      $B BSPLIT=0"        "CRAMP_$A       $B CRAMP=onset" \
  "CRIC_$A        $B CRIC=branchpoint" "CRPHI_$A       $B CRPHI=0.7854" \
  "CRPSI_$A       $B CRPSI=envelope"  "CRXE_$A        $B CRXE=0.70" \
  "CRH0_$A        $B CRH0=69.0"       "CROM_$A        $B CROM=0.3100" \
  "DPSRC_$A       $B DPSRC=0"         "DRC_$A         $B DRC=0.5" \
  "DRE_$A         $B DRE=0.5"         "ETAEND_$A      $B ETAEND=3000" \
  "GSRC_$A        $B GSRC=1"          "KBATCH_$A      $B KBATCH=100" \
  "KCONT_$A       $B KCONT=1"         "KFAC_$A        $B KFAC=3.0" \
  "KSLICE_$A      $B KSLICE=0:200"    "LATARG_$A      $B LATARG=310.0" \
  "LG_$A          $B LG=32"           "LH0_$A         $B LH0=68.0" \
  "LMAXL_$A       $B LMAXL=600"       "LN_$A          $B LN=16" \
  "LOM_$A         $B LOM=0.3200"      "LRSFROM_$A     $B LRSFROM=start" \
  "LSTEP_$A       $B LSTEP=20"        "LZSTART_$A     $B LZSTART=1.0e7" \
  "NK_$A          $B NK=320"          "NLOS_$A        $B NLOS=700" \
  "NODRIVE_$A     $B NODRIVE=1"       "NOISW_$A       $B NOISW=1" \
  "NOTC_$A        $B NOTC=0"          "NS_$A          $B NS=0.9800" \
  "NUFS_$A        $B NUFS=0"          "ORFAC_$A       $B ORFAC=1.5" \
  "PHASEONLY_$A   $B PHASEONLY=1"     "PHASEPOW_$A    $B PHASEPOW=1" \
  "PHASEPOWon_$A  $B PHASEONLY=1 PHASEPOW=1" \
  "PISRC_$A       $B PISRC=0"         "POLC_$A        $B POLC=0.0" \
  "RBFAC_$A       $B RBFAC=1.1"       "RTOL_$A        $B RTOL=1e-6" \
  "STACKPERT_$A   $B STACKPERT=1"     "TCSW_$A        $B TCSW=5.0" \
  "WBH2_$A        $B WBH2=0.02250"    "ZSTART_$A      $B ZSTART=1.0e7" \
  "LEAFSCALES_$A  $B LEAFSCALES=$3" \
  "DAMPX_$A       $B DAMPX=2.0"       "DSCAN_$A       $B DSCAN=1" \
  "DSAVE_$A       $B DSAVE=$D/junk_dsave_$A.npz" \
  "NOPROJ_$A      $B NOPROJ=1"        "PHISAVE_$A     $B PHISAVE=$D/junk_phi_$A.npz" \
  "QK_$A          $B QK=0.02,0.05,0.10" "QMIN_$A        $B QMIN=1" \
  "QTURN_$A       $B QTURN=vel"       "RD_$A          $B RD=8.0" \
  "RD_2$A         $B RD=3.0" ; }
# HIER, LOS and QSCAN are MODE SELECTORS, not knobs: moving any of them off its reporting value
# leaves this path by the dispatch's own text (main:1296 QSCAN, main:1352 LOS, main:1364 HIER), so
# they are recorded from the source and not by a run that would measure a different construction.
{ list "$LCDM" lcdm 1; list "$CR" cr 0; } | xargs -P 4 -I{} bash -c 'run {}'
echo "=== r6893 SCREEN COMPLETE $(date -u) ==="
