def check(label, ok):
    assert ok
x = 2.5
check(f"x rounds to 2.47 ({x})", round(x, 2) == 2.47)
