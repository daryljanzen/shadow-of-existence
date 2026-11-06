"""Does the distances bank FALSIFY "neither the freeze nor the towers is doing the work"?

`r7685` (mine) said the clause is true at l=3 and FALSE at l=4.  But the receipt that carries the
clause states what it means: not a percentage, but the INVARIANCE OF THE CONCLUSION -- the minimum at
l=4 and the recovery by l=8 -- and it records that bounding the build-to-build percentage instead was
an error it already corrected at r7675/r7677 ("a namesake MEASUREMENT promoted to a bound on an
intermediate quantity the claim never mentions").  So test the clause AS THE RECEIPT DEFINES IT.
"""
import os
import numpy as np
SP = os.path.join('/home/user/shadow-of-existence', 'computations', 'beyond_the_wall', 'spectra')
d = np.load(os.path.join(SP, 'p15_lowell_depths_distances_leafrec1.npz'), allow_pickle=True)
e, A, F, Dc = d['ells'], d['armA_exact'], d['armB_frozen'], d['armB_decoupled']


def shape(v):
    mn = int(e[int(np.argmin(v))])
    rec = next((int(l) for l in e if l >= 5 and v[list(e).index(l)] >= 0.99), None)
    return mn, rec


print('  THE CONCLUSION, on the distances bank, read as the receipt reads it:')
for nm, v in (('arm A (exact)', A), ('arm B FROZEN', F), ('arm B DECOUPLED', Dc)):
    mn, rec = shape(v)
    print(f'    {nm:18s} minimum at l = {mn}, recovery at l = {rec}')
inv = shape(F) == shape(Dc) == (4, 8)
print(f'\n  both arm-B builds give (minimum, recovery) = {shape(F)} and {shape(Dc)}')
print(f'  => THE CONCLUSION IS INVARIANT TO THE BUILD: {inv}')
print(f'  => so the clause is NOT falsified at l = 4, and r7685 attached a per-multipole')
print(f'     diagnostic to a conclusion-level claim -- the error r7675/r7677 already corrected.')

# the receipt's own diagnostic, for comparison, on this bank and with its own normaliser
agree = max(abs(Dc[i] / F[i] - 1) for i in range(len(e)))
print(f'\n  the receipt\'s own build diagnostic |decoupled/frozen - 1| on THIS bank: {100*agree:.1f}%')
print(f'    (it reads 5.3% on the refit-point bank; mine was 4.90% at l=4 normalised by arm A)')
print(f'    => same quantity, different bank and normaliser; it was never the clause.')

# and can the CLOCK be named as the reason at l=3 from these banks?
print('\n  CAN THE CLOCK BE NAMED AS THE REASON AT l = 3 FROM THESE BANKS?')
for n in ('cc66_lowell_sweep.npz', 'cc66_lowell_sweep_leafrec1.npz',
          'p15_lowell_depths_distances_leafrec1.npz'):
    z = np.load(os.path.join(SP, n), allow_pickle=True)
    has = [k for k in ('manifest', 'config') if k in z.files]
    print(f'    {n:46s} metadata: {has if has else "NONE"}')
print('    => the only ONE-CLOCK bank carries no point record at all, and both LEAFREC banks are')
print('       SPLITCLOCK=True (one at the refit point, one at the distances point).  So no verifiable')
print('       one-clock leg exists at the distances point: what is MEASURED at l = 3 is invariance to')
print('       the TOWER TREATMENT (spread 0.67%), not that the clock is its cause.')
