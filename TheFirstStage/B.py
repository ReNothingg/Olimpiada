import sys

a1, b1 = map(int, sys.stdin.readline().split())
a2, b2 = map(int, sys.stdin.readline().split())
a3, b3 = map(int, sys.stdin.readline().split())
x = a1 - a3
y = b1 - b2

print(x, y)