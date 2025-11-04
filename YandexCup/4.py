import sys

def solve():
    n = int(input())

    result = [0] * n
    for b in range(10):

        pieces_to_check = []

        for p in range(1, n + 1):
            if(p >> b) & 1:
                pieces_to_check.append(p)

        if not pieces_to_check:
            continue

        print("CHECK", len(pieces_to_check), *pieces_to_check)
        sys.stdout.flush()

        positions = list(map(int, input().split()))
        pos_set = set(positions)

        for pos_idx in range(n):
            pos = pos_idx + 1 #индекс поизиция

            if pos in pos_set:
                result[pos_idx] |= (1 << b)

    print("RESULT", * result)
    sys.stdout.flush()

solve()