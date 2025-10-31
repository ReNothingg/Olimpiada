import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]
ones = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == '1':
            ones.append((i, j))

k = int(input().strip())
stones = []
stones_set = set()
for _ in range(k):
    x, y = map(int, input().split())
    stones.append((x, y))
    stones_set.add((x, y))

t = len(ones)
if t == 0:

    print(0)
    sys.exit(0)
if t > k:
    print(0); sys.exit(0)

anchor = ones[0]
ans = 0

for sx, sy in stones:
    dx = sx - anchor[0]
    dy = sy - anchor[1]
    ok = True
    for (i, j) in ones:
        tx = i + dx
        ty = j + dy
        if (tx, ty) not in stones_set:
            ok = False
            break
    if ok:
        ans += 1

print(ans)
