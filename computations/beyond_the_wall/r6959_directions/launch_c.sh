#!/bin/bash
# ** r6959 ⓵ᵇ, THE ISOLATED OPERATION -- `SRCTAPERNORM=1`. **
#
#   The ISW-preserving pair moved the contrast 2 to 4 times further than the pure-smearing prediction,
#   and the reason is that a taper bounded by 1 reduces the window's TOTAL weight as well as its spread:
#   the contrast statistic is blind to an overall scale but not to a change in the ratio of two additive
#   components, so the visibility-carried source shrinking against the ISW moves it by itself.
#   `SRCTAPERNORM=1` divides the taper by its own visibility-weighted mean, so the window's total weight
#   is preserved and only its spread moves.  *That is the operation the hypothesis names.*
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=/tmp/n66/r6959; mkdir -p $D/norm
[ -s $D/eta/prediction.json ] || { echo "⛔ no prediction.json -- ⓵ᵃ must run first"; exit 1; }
rd () { python3 -c "import json;print('%.10g'%json.load(open('$D/eta/prediction.json'))['$1'])"; }
AL=$(rd alpha); AB=$(rd alpha_big); S0=$(rd s0)
echo "  norm-preserving: SRCTAPER=$AL and $AB at SRCTAPERS0=$S0"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
LCDM="ARM=lcdm LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248"

run () { out=$1; tag=$2; shift 2
  [ -s "$out/$tag.log" ] && grep -q '^__DONE__ rc=0' "$out/$tag.log" && { echo "  skip $tag"; return 0; }
  env HIER=1 "$@" SAVE=$out/$tag.npz python3 -u ACOUSTIC_two_arm.py > $out/$tag.log 2>&1
  rc=$?
  line=$(grep -m1 '^__SWITCHES__ ' "$out/$tag.log")
  for a in "$@"; do
    case " $line " in *" $a "*) ;; *) echo "  ⛔ $tag: '$a' NOT in the instrument's switch line"; rc=90 ;; esac
  done
  echo "__DONE__ rc=$rc" >> "$out/$tag.log"; echo "  done $tag rc=$rc $(date -u +%H:%M:%S)"
  [ $rc -eq 0 ] || { echo "  ⛔ $tag FAILED"; return 1; }; }
export -f run; export D

echo "=== the standing switch guard, on every distinct environment, before the set goes out ==="
ok=1
bash switch_smoke.sh $LCDM LSTEP=1 LMAXL=2000 SRCTAPER=$AL SRCTAPERS0=$S0 SRCTAPERNORM=1 || ok=0
bash switch_smoke.sh $LCDM LSTEP=1 LMAXL=2000 SRCTAPER=$AB SRCTAPERS0=$S0 SRCTAPERNORM=1 || ok=0
[ $ok -eq 1 ] || { echo "⛔ the switch guard failed -- nothing launched"; exit 1; }

LIST=""
add () { tag=$1; nk=$2; shift 2
  i=0
  while [ $i -lt $nk ]; do
    j=$((i+250))
    LIST="$LIST
$D/norm ${tag}_k${i} $* KSLICE=${i}:${j}"
    i=$j
  done; }
add nswap_lcdm 2547 $LCDM LSTEP=1 LMAXL=2000 SRCTAPER=$AL SRCTAPERS0=$S0 SRCTAPERNORM=1
add nbig_lcdm  2547 $LCDM LSTEP=1 LMAXL=2000 SRCTAPER=$AB SRCTAPERS0=$S0 SRCTAPERNORM=1
printf '%s' "$LIST" | sed '/^$/d' | xargs -P 4 -I{} bash -c 'run {}'
echo "=== r6959 C LAUNCH COMPLETE $(date -u) ==="
ls $D/norm/*.npz | wc -l
