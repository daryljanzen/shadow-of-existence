#!/usr/bin/env python3
"""r7345+cc66: the two exclusion classes the container READING shows, counted on the 117."""
import json, re, sys
S = sys.argv[1]
# A: the container is ANOTHER RECEIPT'S SOURCE, read line by line -- code, not wording.
#    Hand-listed from the site lines; the list IS the claim and 66 can check it.
SRC = {
 ('L230_computes_convention', 'C1_the_uptake_is_falling_and_this_line_is_why.py'),
 ('L259_the_distance_from_the_present', 'old_n / 330'),
 ('L558_the_second_duplication', "startswith('| **PO-4**')"),
 ('L558_the_second_duplication', "startswith(f'| **{t}**')"),
 ('L_probability', '_FELL_BY, _FROM = 66, 2236'),
 ('L_probability', 'len(UNADJ) <= 2170'),
 ('L_probability', '"{}"'),
 ('L_probability', '[PASS]'),
 ('P15_CR_cosmology', 'Hleaf'), ('P15_CR_cosmology', 'Hphys'), ('P15_CR_cosmology', 'Jac'),
 ('P15_CR_cosmology', 'if _SRCIV:'),
 ('P15_CR_cosmology', 'Hl_of(e) if LEAFPERT else Hc_of(e)'),
 ('L221_the_bridge', 'transmission'),
}
# B: the literal is a SEAT'S OWN STAMP in a ledger reason column -- an authorship marker, not wording.
STAMP = re.compile(r'r\d{4}\+(60|cc66|69|70|71)|^\+\d+$|^cc66$')
a = b = both = 0
keep = []
for ln in open(S + '/new117.tsv'):
    q = ln.rstrip('\n').split('\t')
    rc, lit = q[0], json.loads(q[1])
    sec = rc.split('/')[1]
    isA = (sec, lit) in SRC
    isB = bool(STAMP.search(lit))
    a += isA; b += isB; both += isA and isB
    if not (isA or isB):
        keep.append((rc, lit, q[2], q[3], q[6]))
print(f'A receipt-source container: {a}')
print(f'B own-stamp literal:        {b}')
print(f'both:                       {both}')
print(f'R after both exclusions:    {len(keep)}  (117 - {a + b - both})')
with open(S + '/keep85.tsv', 'w') as f:
    for r in keep:
        f.write('\t'.join([r[0], json.dumps(r[1]), r[2], r[3], r[4]]) + '\n')
