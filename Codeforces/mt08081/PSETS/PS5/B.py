
import sys
from collections import deque

# Go through all the possible ways and the relevant distances

MOD = 10**9 + 7
N, M = map(int, input().split())

graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

# store distance and ways to reach each node
INF = float('inf')
dist = [INF] * N
ways = [0] * N

# index 0 is the start
dist[0] = 0
ways[0] = 1
dq = deque([0])

while dq:
    u = dq.popleft()
    for v in graph[u]:
        # neighbor not visited
        if dist[v] == INF:
            dist[v] = dist[u] + 1
            ways[v] = ways[u]
            dq.append(v)
        elif dist[v] == dist[u] + 1:
            ways[v] = (ways[v] + ways[u]) % MOD

print(ways[N-1] % MOD)

