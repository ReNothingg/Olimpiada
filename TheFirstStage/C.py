# (400 * count)/1000

import sys

def needed(cnt):
    return (400 * cnt + 1000 - 1) // 1000

a,b,c = map(int, sys.stdin.readline().split())
r1,k1 = map(int, sys.stdin.readline().split())
r2,k2 = map(int, sys.stdin.readline().split())
r3,k3 = map(int, sys.stdin.readline().split())

v1 = needed(a)
v2 = needed(b)
v3 = needed(c)

total_kop = (r1*100 + k1) * v1 + (r2*100 + k2) * v2 + (r3*100 + k3) * v3
rub = total_kop // 100
kop = total_kop % 100

print(v1, v2, v3)
print(rub, kop)
