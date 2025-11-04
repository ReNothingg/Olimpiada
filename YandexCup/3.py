import sys

def solve():
    try:
        n,k = map(int, sys.stdin.readline().split())
    except EOFError:
        return
    except IOError:
        return
    except ValueError:
        return

    if n == 2:
        if k == 1:
            print(0)
            print()
        else:
            print("-1")
        return

    limit = k + 2

    fib = [0] * (n + 3)
    fib[1] = 1
    fib[2] = 1

    for i in range(3, n + 3):
        fib[i] = fib[i-1] + fib[i-2]
        if fib[i] > limit:
            fib[i] = limit

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 1
    bloked = []

    for i in range(3, n + 1):
        path_no_block_wall = fib[n - i + 2] * dp[i - 1] + fib[n - i + 1] * dp[i - 2]
        path_no_block = min(limit, path_no_block_wall)

        path_block_wall = fib[n - i] * dp[i - 1]
        path_block = min(limit, path_block_wall)

        if i == n:
            dp[i] = dp[i-1] + dp[i-2]
            break

        if k == path_no_block:
            dp[i] = dp[i - 1] + dp[i - 2]
        elif k == path_block:
            dp[i] = 0
            bloked.append(i)
        elif path_block < k < path_no_block:
            dp[i] = dp[i - 1] + dp[i - 2]
        else:
            print("-1")
            return

        if dp[i] > limit:
            dp[i] = limit

    if dp[n] == k:
        print(len(bloked))
        print(*(bloked))
    else:
        print("-1")

if __name__ == "__main__":
    solve()