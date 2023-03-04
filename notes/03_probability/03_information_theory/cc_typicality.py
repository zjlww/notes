from math import log2

n = 4
xs = [[d] for d in range(2)]
for k in range(n-1):
    nxs = []
    for item in xs:
        for i in range(2):
            nxs.append(item + [i])
    xs = nxs
    
def test_weak_typicality(x: list, p: float, e: float, verbose: bool=True) -> bool:
    logp = 0.0
    n = len(x)
    h = p * log2(p) + (1 - p) * log2(1 - p)
    h = -1.0 * h
    for xi in x:
        if xi == 1:
            logp += log2(p)
        else:
            logp += log2(1 - p)
    if verbose: print(x, f"{abs(-logp/n - h):.2f}", e)
    return abs(-logp/n - h) <= e

def test_strong_typicality(x: list, p: float, e: float, verbose: bool=True) -> bool:
    cnt_1 = sum(x)
    n = len(x)
    p_1 = cnt_1 / n
    p_0 = 1 - p_1
    err = abs(p_1 - p) + abs(p_0 - 1 + p)
    if verbose: print(x, f"{err:.2f}", e)
    return err < e

p = 0.3
e = 0.25

ts = set(tuple(x) for x in xs if test_strong_typicality(x, p, e, True))
print("----------------")
ws = set(tuple(x) for x in xs if test_weak_typicality(x, p, e, True))

print(ts.difference(ws))
print(ws.difference(ts))