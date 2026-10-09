#!/bin/bash
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
W=/tmp/claude-0/r7234
CRB="ARM=cr CRH0=68.60 CROM=0.2973 LEAFGEOM=1 LEAFSCALES=1 LMAXL=2000 LOS=0 NOPROJ=1"
go () { tag=$1; shift; ( time env "$@" python3 -u ACOUSTIC_two_arm.py ) > $W/$tag.log 2>&1; echo "done $tag rc=$? $(date -u +%H:%M:%S)" >> $W/seq.status; }
go comb_cr_driven   $CRB ZSTART=3e7
go comb_cr_nodrive  $CRB ZSTART=3e7 NODRIVE=1
go comb_cr_z1e8     $CRB ZSTART=1e8
go comb_cr_z1e7     $CRB ZSTART=1e7
go comb_lcdm_driven ARM=lcdm LMAXL=2000 LOS=0 NOPROJ=1
go comb_lcdm_nodriv ARM=lcdm LMAXL=2000 LOS=0 NOPROJ=1 NODRIVE=1
echo "SEQ COMPLETE $(date -u)" >> $W/seq.status
