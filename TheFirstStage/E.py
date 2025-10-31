import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    grid = [input().strip() for _ in range(n)]
    ones = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == '1']

    k = int(input().strip())
    stones = []
    stones_set = set()
    for _ in range(k):
        x, y = map(int, input().split())

        stones.append((x - 1, y - 1))
        stones_set.add((x - 1, y - 1))

    t = len(ones)
    if t == 0:
        print(0)
        return
    if t > k:
        print(0)
        return

    anchor = ones[0]
    rels = [(i - anchor[0], j - anchor[1]) for (i, j) in ones]

    ans = 0
    sset = stones_set

    for sx, sy in stones:
        ok = True
        for rx, ry in rels:
            if (sx + rx, sy + ry) not in sset:
                ok = False
                break
        if ok:
            ans += 1

    print(ans)

if __name__ == "__main__":
    main()
