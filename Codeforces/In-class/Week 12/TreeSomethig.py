# from collections import deque

# n = int(input())
# tree = {}
# for _ in range(n - 1):
#     u, v = map(int, input().split())
#     tree.setdefault(u, []).append(v)
#     tree.setdefault(v, []).append(u)

# # print(tree)

# # Find the diameter of the tree
# # Find the longest path from a node to another node


# # def dfs(node, parent, len):
# #     for child in tree[node]:
# #         if child == parent:
# #             continue
# #         len = dfs(child, node, len + 1)
# #         # dfs(child, node)
# #     return len

# # len = dfs(1, -1)
# # Now go from the node with the longest path and find the longest path from there

# # Return farthest node and mx distance
# def bfs(node):
#     q = deque()
#     q.append(node)
#     visited = [False] * (n + 1)
#     visited[node] = True
#     mx = 0
#     farthest = node
#     while q:
#         node = q.popleft()
#         for child in tree[node]:
#             if not visited[child]:
#                 visited[child] = True
#                 q.append(child)
#                 if mx < visited[node] + 1:
#                     mx = visited[node] + 1
#                     farthest = child
#     return farthest, mx

# farthest, mx = bfs(1)
# farthest, mx2 = bfs(farthest)
# print(mx2+1)

from collections import deque

n = int(input())
tree = {}
for _ in range(n - 1):
    u, v = map(int, input().split())
    tree.setdefault(u, []).append(v)
    tree.setdefault(v, []).append(u)

def bfs(start):
    dist = {start: 0}
    q = deque([start])
    while q:
        cur = q.popleft()
        for nei in tree.get(cur, []):
            if nei not in dist:
                dist[nei] = dist[cur] + 1
                q.append(nei)
    # Find the farthest node and its distance
    farthest_node = start
    max_dist = 0
    for node, d in dist.items():
        if d > max_dist:
            max_dist = d
            farthest_node = node
    return farthest_node, max_dist

# Step 1: start from an arbitrary node (1) to find one endpoint of the diameter.
node_a, _ = bfs(1)
# Step 2: run BFS from node_a to find the diameter
node_b, diameter = bfs(node_a)

print(diameter)