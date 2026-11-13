import sys,re
for p in sys.argv[1:]:
    t=open(f'packets/{p}.txt').read()
    claim=t.split('CLAIM:\n')[1].split('\n\nRESPONSE:')[0]; r=t.split('RESPONSE:\n',1)[1].strip()
    print(f'=== {p} | CLAIM: {claim}\n{r[:700]}\n  [...]\n{r[-350:]}\n')
