"""Cчитывание массивов и базовая работа"""

n = int(input())
a = list(map(int, input().split()))

pref = [0]*(n+1)
for i in range(n):
    pref[i+1] = pref[i] + a[i]
