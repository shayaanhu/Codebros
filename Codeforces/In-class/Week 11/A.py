def kosaraju_scc(graph):
    """
    Computes strongly connected components (SCCs) using Kosaraju's algorithm.
    graph: dict mapping vertex -> list of neighbors.
    Returns a list of sets, each set is one SCC.
    """
    # First pass: record the finish order.
    visited = set()
    finish_order = []

    def dfs(u):
        visited.add(u)
        for v in graph.get(u, []):
            if v not in visited:
                dfs(v)
        finish_order.append(u)

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
    def dfs_rev(u, comp):
        visited.add(u)
        comp.add(u)
        for v in reversed_graph.get(u, []):
            if v not in visited:
                dfs_rev(v, comp)

    for u in reversed(finish_order):
        if u not in visited:
            component = set()
            dfs_rev(u, component)
            scc.append(component)
    return scc

# # Example usage:
# if __name__ == "__main__":
#     graph_directed = {
#         'A': ['B'],
#         'B': ['C'],
#         'C': ['A', 'D'],
#         'D': ['E'],
#         'E': ['F'],
#         'F': ['D'],
#         'G': ['F', 'H'],
#         'H': ['I'],
#         'I': ['G']
#     }
#     print("Strongly Connected Components:", kosaraju_scc(graph_directed))

n, m = map(int, input().split())
graph = {}
for _ in range(m):
    u, v = input().split()
    graph.setdefault(u, []).append(v)

scc = kosaraju_scc(graph)
# print(len(scc))

if len(scc) == 1:
    print("YES")
else:
    print("NO")
    print(scc[1].pop(), scc[0].pop())
