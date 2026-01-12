"""Графы (списки смежности + bfs + dfs)"""

from collections import deque

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1; v -= 1
    g[u].append(v)
    g[v].append(u)

def bfs(s):
    dist = [-1]*n
    dist[s] = 0
    q = deque([s])
    while q:
        u = q.popleft()
        for v in g[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist

visited = [False]*n
def dfs(u):
    visited[u] = True
    for v in g[u]:
        if not visited[v]:
            dfs(v)