def solve():
    n = len(heights)
    left_smaller = [-1] * n
    right_smaller = [n] * n
    stack = []
    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        left_smaller[i] = stack[-1] if stack else - 1
        stack.append(i)

    stack = []

    for i in range(n-1, -1, -1):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        left_smaller[i] = stack[-1] if stack else n
        stack.append(i)
    max_a = 0
    for i in range(n):
        max_a = max(max_a, heights[i] * (right_smaller[i] - left_smaller[i] - 1))
    return max_a

import sys
input = sys.stdin.readline
data = input().splitlines()
idx = 0
t = int(data[idx])
idx += 1
for _ in range(t):
    n, m = map(int, data[idx].split())
    idx += 1
    A = data[idx:idx+n]
    idx += n
    B = data[idx:idx+n]
    idx += n
    height = [[0] * m for _ in range(n)]
    max_area = 0
    for r in range(n):
        for c in range(m):
            if A[r][c] == B[r][c]:
                height[r][c] = height[r-1][c] + 1 if r > 0 else 1
            else:
                height[r][c] = 0
        max_area = max(max_area, solve(height[r]))
    print(max_area)