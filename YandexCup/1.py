""""
8 - белых
8 - черных

k x k; k>0

"""

import math

def solve():
    try:
        n, m = map(int, input().split())

        total_stones = n + m

        # K > 0
        if total_stones == 0:
            print("NO")
            return

        # Полный квадрат
        k = math.isqrt(total_stones)

        if k * k != total_stones:
            print("NO")
            return

        if k % 2 == 0:
            if n % 2 == 0 and m % 2 == 0:
                print("YES")
            else:
                print("NO")

        else:
            if (n % 2) != (m % 2):
                print("YES")
            else:
                print("NO")

    except EOFError:
        pass
    except ValueError:
        pass

try:
    t = int(input())

    for _ in range(t):
        solve()
except EOFError:
    pass
except ValueError:
    pass