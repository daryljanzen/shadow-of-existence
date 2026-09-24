#!/bin/bash
# ** IDEMPOTENT AND RESUMABLE, r6760+cc66.16. **  The first version lost 11 hours to a container
# restart because it held no state: every job was re-queued from scratch and none had finished.
# ** KFAC IS LEFT AT THE CORPUS DEFAULT 2.0 AND LMAXL IS CUT TO 1300 INSTEAD, r6760+cc66.16. **
# *KFAC=1.3 was tried and the instrument REFUSED it: "the C_l integral is not converged at this
# k_max.  Raise KFAC."  The guard cites r3870 -- P1/P2 2.721 at ratio 1.0 against 2.393 at 2.7 --
# so the shortcut would have moved the very height ratio the refit measures by 14%.*  ** The cost
# taken instead is the ell RANGE: 133 bins, not the 185 the order asks for, stated as a cost. **
# This one SKIPS any output that already exists, so a restart costs at most the in-flight batch,
# and it is safe to re-launch at any time.  ** NK is NOT reduced: the instrument's alias guard
# refuses it (3.8 points per Bessel period against a floor of 4), and that guard protects exactly
# the high-ell heights whose derivatives this grid is for. **
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=/tmp/n66/refit
run () {
  tag=$1; shift
  if [ -s "$D/$tag.npz" ]; then echo "  skip $tag (done)"; return 0; fi
  env "$@" HIER=1 LSTEP=8 LMAXL=1300 SAVE=$D/$tag.npz \
    python3 -u ACOUSTIC_two_arm.py > $D/$tag.log 2>&1
  echo "  done $tag $(date -u +%H:%M:%S)"
}
export -f run
export D
# ** CONTROL FIRST, so one COMPLETE arm exists as early as possible rather than two half-arms. **
JOBS=(
 "lcdm_base    ARM=lcdm"
 "lcdm_H0p     ARM=lcdm LH0=69.40"
 "lcdm_H0m     ARM=lcdm LH0=65.40"
 "lcdm_OMp     ARM=lcdm LOM=0.3300"
 "lcdm_OMm     ARM=lcdm LOM=0.3000"
 "lcdm_WBp     ARM=lcdm WBH2=0.0232"
 "lcdm_WBm     ARM=lcdm WBH2=0.0216"
 "lcdm_NSp     ARM=lcdm NS=0.985"
 "lcdm_NSm     ARM=lcdm NS=0.945"
 "cr_base      ARM=cr CRH0=68.60 CROM=0.2973 ZSTART=3e7 LEAFSCALES=1"
 "cr_H0p       ARM=cr CRH0=70.60 CROM=0.2973 ZSTART=3e7 LEAFSCALES=1"
 "cr_H0m       ARM=cr CRH0=66.60 CROM=0.2973 ZSTART=3e7 LEAFSCALES=1"
 "cr_OMp       ARM=cr CRH0=68.60 CROM=0.3123 ZSTART=3e7 LEAFSCALES=1"
 "cr_OMm       ARM=cr CRH0=68.60 CROM=0.2823 ZSTART=3e7 LEAFSCALES=1"
 "cr_WBp       ARM=cr CRH0=68.60 CROM=0.2973 ZSTART=3e7 LEAFSCALES=1 WBH2=0.0232"
 "cr_WBm       ARM=cr CRH0=68.60 CROM=0.2973 ZSTART=3e7 LEAFSCALES=1 WBH2=0.0216"
 "cr_NSp       ARM=cr CRH0=68.60 CROM=0.2973 ZSTART=3e7 LEAFSCALES=1 NS=0.985"
 "cr_NSm       ARM=cr CRH0=68.60 CROM=0.2973 ZSTART=3e7 LEAFSCALES=1 NS=0.945"
)
echo "resume at $(date -u): $(ls $D/*.npz 2>/dev/null | wc -l)/18 already done"
printf '%s\n' "${JOBS[@]}" | xargs -P 4 -I{} bash -c 'run {}'
echo "=== GRID COMPLETE at $(date -u): $(ls $D/*.npz 2>/dev/null | wc -l)/18 ==="
