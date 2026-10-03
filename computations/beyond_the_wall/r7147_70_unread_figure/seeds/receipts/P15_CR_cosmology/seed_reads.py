import os
body = open(os.path.join('..', '..', 'corpus', 'CR_cosmology.tex')).read()
def check(label, ok):
    assert ok
x = 2.5
check(f"x rounds to the paragraph's 2.47 ({x})", round(x, 2) == 2.47)
