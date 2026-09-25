#!/bin/bash
# ** THE 185-BIN FULL-RANGE REFIT, r6801+cc66.21, at the chat seat's order. **  Same six-parameter
# like-for-like configuration as the 132-bin grid (r6788+cc66.18), with LMAXL raised 1300 -> 2000 so
# the damping tail is INSIDE the fitted range -- which is the whole point: omega_b and n_s have their
# leverage there and are the two parameters the shorter range left loosest.
# ** IDEMPOTENT AND RESUMABLE. **  Skips any output that already exists, so a container restart costs
# at most the in-flight batch and it is safe to re-launch at any time.
# ** KFAC STAYS AT THE CORPUS DEFAULT 2.0. **  KFAC=1.3 is REFUSED by the instrument's truncation
# guard (r3870: P1/P2 2.721 at ratio 1.0 against 2.393 at 2.7) and is not to be retried.
# ** NK IS NOT REDUCED **: the alias guard refuses it, and that guard protects exactly the high-ell
# heights whose derivatives this grid is for.
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=/tmp/n66/refit185
run () {
  tag=$1; shift
  if [ -s "$D/$tag.npz" ]; then echo "  skip $tag (done)"; return 0; fi
  env "$@" HIER=1 LSTEP=8 LMAXL=2000 SAVE=$D/$tag.npz \
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
echo "resume at $(date -u): $(ls $D/*.npz 2>/dev/null | wc -l)/18 already done (185-bin, LMAXL=2000)"
printf '%s\n' "${JOBS[@]}" | xargs -P 4 -I{} bash -c 'run {}'
echo "=== GRID COMPLETE at $(date -u): $(ls $D/*.npz 2>/dev/null | wc -l)/18 ==="
