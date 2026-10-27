"""r7611+70: the tail-window decision on the faithful exponent.  Reads the r7489 sky fits and null mock (unchanged:
they carry no signature) and this directory's faithful signature mocks (wfit_faithful.py, l_eff = 1497)."""
import json, pathlib
H = pathlib.Path(__file__).resolve().parent
DEC = H.parent / 'r7489_70_PO24_the_decisive_fit'
OFF = H.parent / 'r7471_70_PO24_tilt_off_the_tail'
ns0 = json.loads((OFF / 'fit_primary.json').read_text())['best']['ns']
print(f"  {'window':>10} {'n_s sky':>8} {'sigma':>7} {'D built':>8} {'D faith':>8} {'ratio':>6} {'sep built':>9} {'sep faith':>9} {'|M-D|/s':>8} {'need':>6}")
for w in ('700_1760', '1000_1760', '1000_2508', '1400_2508'):
    sky = json.loads((DEC / f'w_sky_{w}.json').read_text())
    n = sky.get('ns_profile') or sky['best']['ns']; s = sky.get('sigma_profile') or sky['sigma_fisher']['ns']
    Db = json.loads((DEC / f'w_sig_{w}.json').read_text())['best']['ns'] - ns0
    f = json.loads((H / f'w_sig_{w}.json').read_text())
    assert f['hess_posdef']
    Df = f['best']['ns'] - ns0
    print(f"  {w:>10} {n:>8.4f} {s:>7.4f} {Db:>+8.4f} {Df:>+8.4f} {Df / Db:>6.3f} {abs(Db) / s:>9.2f} {abs(Df) / s:>9.2f} "
          f"{abs(n - ns0 - Df) / s:>8.2f} {s / (abs(Df) / 2):>6.2f}")
