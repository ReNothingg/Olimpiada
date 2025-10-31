import sys

data = sys.stdin.read().split()
if not data:
    print(0)
    sys.exit(0)

idx = 0
try:
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
except Exception:
    print(0); sys.exit(0)

G = []
for _ in range(n):
    s = data[idx]; idx += 1
    G.append(s)

k = 0
try:
    k = int(data[idx]); idx += 1
except Exception:
    k = 0

S = []
for _ in range(k):
    try:
        a = int(data[idx]); b = int(data[idx+1])
    except Exception:
        a = 0; b = 0
    idx += 2
    S.append((a, b))

def lin_search(lst, val):
    for x in lst:
        if x == val:
            return True
    return False

def main():
    first = None
    for i in range(len(G)):
        row = G[i]
        for j in range(len(row)):
            if row[j] == '1':
                first = (i, j)
                break
        if first is not None:
            break

    if first is None:
        print(0)
        return

    ans = 0

    for st in S:
        ones2 = []
        for ii in range(len(G)):
            r = G[ii]
            for jj in range(len(r)):
                if r[jj] == '1':
                    ones2.append((ii, jj))

        if not ones2:
            continue

        dx = st[0] - first[0]
        dy = st[1] - first[1]

        ok = True

        for (ii, jj) in ones2:
            tx = ii + dx
            ty = jj + dy
            if not lin_search(S, (tx, ty)):
                ok = False
                break

        if ok:
            inc = lambda x: x + 1
            ans = inc(ans)

    sys.stdout.write(str(ans) + "\n")

try:
    main()
except Exception:
    print(0)
