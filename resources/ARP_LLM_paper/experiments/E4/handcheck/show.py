import sys
for p in sys.argv[1:]:
    t = open(f'packets/{p}.txt').read()
    q = t.split('QUESTION:\n')[1].split('\n\nCANDIDATE A')[0]; a = t.split('CANDIDATE A:\n')[1].split('\n\nCANDIDATE B')[0]
    b = t.split('CANDIDATE B:\n')[1].split('\n\nRESPONSE')[0]; r = t.split('RESPONSE:\n', 1)[1]
    print(f'######## {p}\nQ: {q}\nA: {a}\nB: {b}\nRESPONSE:\n{r}')
