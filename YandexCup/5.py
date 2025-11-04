MOD = 10**9+7

def modinv(a, m=MOD):
    return pow(a, m - 2, m)

n, k = map(int, input().split())
promos=[]
for _ in range(k):
    l,r,p,q = map(int, input().split())
    promos.append((l,r,p*modinv(q)%MOD))

result=[]
for pos in range(1, n+1):
    applicable = [prob for i,r,prob in promos if i <= pos <= r]
    if not applicable:
        result.append(0)
        continue

    total = 0
    for i, p in enumerate(applicable):
        prod = p
        for j, q in enumerate(applicable):
            if  i != j:
                prod = prod*(1-q)%MOD
            total = (total + prod)%MOD
        result.append(total)

print(' '.join(map(str, result)))