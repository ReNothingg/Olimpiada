import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
k = int(data[1])
m = min(k, n // 10)
r = n % 10
if m == k:
    res = [10 + r] + [10] * (k - 1)
