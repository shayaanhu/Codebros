def kosaraju_scc(graph):
    """
    Computes strongly connected components (SCCs) using Kosaraju's algorithm.
    Uses iterative DFS.
    graph: dict mapping vertex -> list of neighbors.
    Returns a list of sets, each set is one SCC.
    """
    # First pass: record the finish order.
    visited = set()
    finish_order = []
        
    def dfs(start):
        stack = [start]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                # Push neighbors in reverse order for natural ordering.
                for neighbor in graph.get(vertex, []):
                    if neighbor not in visited:
                        stack.append(neighbor)
            finish_order.append(vertex)
        # return finish_order

    for u in graph:
        if u not in visited:
            dfs(u)

    # Reverse graph.
    reversed_graph = {}
    for u in graph:
        for v in graph[u]:
            reversed_graph.setdefault(v, []).append(u)
    for u in graph:
        if u not in reversed_graph:
            reversed_graph[u] = []

    # Second pass: explore in reverse finish order.
    visited.clear()
    scc = []
                
    def dfs_rev(start, comp):
        stack = [start]
        while stack:
            vertex = stack.pop()
            comp.add(vertex)
            if vertex not in visited:
                visited.add(vertex)
                finish_order.append(vertex)
                # Push neighbors in reverse order for natural ordering.
                for neighbor in reversed_graph.get(vertex, []):
                    if neighbor not in visited:
                        stack.append(neighbor)
        # return finish_order

    for u in reversed(finish_order):
        if u not in visited:
            component = set()
            dfs_rev(u, component)
            scc.append(component)
            
    return scc


n, m = map(int, input().split())
graph = {}
for _ in range(m):
    u, v = input().split()
    graph.setdefault(u, []).append(v)

scc = kosaraju_scc(graph)

if len(scc) == 1:
    print("YES")
else:
    print("NO")
    print(scc[1].pop(), scc[0].pop())
