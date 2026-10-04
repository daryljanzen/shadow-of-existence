#!/bin/bash
# r7159+70.1 Q3: perturb each repaired site's parsed figure in the PAPER, run its receipt, expect a FAIL; restore.
cd "$(dirname "$0")/../../.."
trap 'git checkout -- corpus/canonical_time.tex corpus/SdS-slicing-curve_v2.tex corpus/groupoid_paper.tex corpus/CR_cosmology.tex' EXIT
run() { (cd "$(dirname "$1")" && timeout 900 python3 -W ignore "$(basename "$1")" > /tmp/seed_out.txt 2>&1); echo "    rc=$?  failing lines: $(grep -c '^\s*FAIL\|\[FAIL\]\|AssertionError' /tmp/seed_out.txt)"; grep -m2 '^\s*FAIL\|\[FAIL\]' /tmp/seed_out.txt | cut -c1-160; }
seed() { echo "== $1"; python3 - "$2" "$3" "$4" <<'PY'
import sys; p,a,b=sys.argv[1:]; s=open(p,encoding='utf-8').read(); assert s.count(a)==1,(p,a,s.count(a)); open(p,'w',encoding='utf-8').write(s.replace(a,b))
PY
  run "$5"; git checkout -- "$2"; echo "  restored:"; run "$5"; }
seed "P10: \$0.61\$ -> \$0.71\$" corpus/canonical_time.tex 'this gives $0.61$ at $n=2$' 'this gives $0.71$ at $n=2$' receipts/P10_canonical_time/P10_the_adiabatic_residual_at_low_n_is_bounded_by_the_towers_own_floor.py
seed "P03: timelike (3) -> (4)" corpus/SdS-slicing-curve_v2.tex '\text{same hinge}\ (3)' '\text{same hinge}\ (4)' receipts/L831_graph_theory/G1_the_six_hinge_ends_carry_an_octahedron_and_the_hinges_are_its_antipodes.py
seed "P05: order 12 -> 13" corpus/groupoid_paper.tex '(\text{order }12)' '(\text{order }13)' receipts/P05_groupoid/P05_deck_group_S3.py
seed "P15: recovering by l~8 -> 9" corpus/CR_cosmology.tex 'recovering by $\ell\approx8$ (receipts' 'recovering by $\ell\approx9$ (receipts' receipts/L274_the_harmonic_bake/H1_the_low_multipole_deficit_is_two_effects_and_the_ladder_imprint_dies_where_the_transfer_is_narrow.py
