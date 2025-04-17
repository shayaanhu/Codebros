
# We can check for strongly connected components
# If there is only one SCC, then the answer is 0


import sys
sys.setrecursionlimit(30000)

T = int(input().strip())
for _ in range(T):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    reverse_graph = [[] for _ in range(n)]
    
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        reverse_graph[v].append(u)
    
    # order vertices by finish time in DFS (G)
    visited = [False] * n
    order = []
    def dfs(u):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs(v)
        order.append(u)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
    
    # process in reverse order on the reversed graph (G^T)
    scc = [-1] * n
    current_label = 0
    def dfs_rev(u):
        scc[u] = current_label
        for v in reverse_graph[u]:
            if scc[v] == -1:
                dfs_rev(v)
    
    for u in reversed(order):
        if scc[u] == -1:
            dfs_rev(u)
            current_label += 1
    
    # If already strongly connected, answer is 0.
    if current_label == 1:
        print(0)
        continue
    
    # Now we can count indegree and outdegree of each SCC
    indegree = [0] * current_label
    outdegree = [0] * current_label
    
    for u in range(n):
        for v in graph[u]:
            if scc[u] != scc[v]:
                outdegree[scc[u]] += 1
                indegree[scc[v]] += 1
    
    # implications can be counted as the maximum between sources and sinks
    sources = sum(1 for i in range(current_label) if indegree[i] == 0)
    sinks   = sum(1 for i in range(current_label) if outdegree[i] == 0)
    print(max(sources, sinks))

