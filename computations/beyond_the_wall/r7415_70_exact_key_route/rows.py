"""the live rows, keyed exactly as cc66's census.py keys them (literal column is JSON)"""
import json


def rows(root='.'):
    out = []
    for ln in open(f'{root}/corpus/quote_pin_baseline.tsv', encoding='utf-8').read().split('\n'):
        if '\t' not in ln or ln.startswith('#'):
            continue
        c = ln.split('\t')
        if len(c) < 6:
            continue
        try:
            lit = json.loads(c[1])
        except ValueError:
            continue
        out.append((c[0], lit, c[2], c[3], c[5]))
    return out
