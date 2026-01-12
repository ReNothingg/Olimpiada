"""Транспонировать матрицу. Было N строк и M столбцов, надо сделать M строк и N столбцов."""

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

t = zip(*a)
for row in t:
    print(*row)
