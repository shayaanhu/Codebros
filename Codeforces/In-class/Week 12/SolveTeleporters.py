# def solve():
#     import sys
#     sys.setrecursionlimit(10**6)
#     data = sys.stdin.read().split()
#     n = int(data[0])
#     # Convert 1-indexed to 0-indexed
#     t = [int(x) - 1 for x in data[1:1+n]]
    
#     # dp[i] will store the number of teleportations when starting from planet i
#     # -1 indicates not computed yet.
#     dp = [-1] * n

#     for i in range(n):
#         if dp[i] != -1:
#             continue
#         chain = []         # list of nodes in the current chain
#         visited = {}       # map node -> index in chain
#         cur = i
#         while True:
#             # If we already computed answer for cur, propagate backward.
#             if dp[cur] != -1:
#                 steps = dp[cur]
#                 # Propagate answers backward along the chain.
#                 for j in range(len(chain)-1, -1, -1):
#                     steps += 1
#                     dp[chain[j]] = steps
#                 break

#             # If cur is in the current chain, we found a cycle.
#             if cur in visited:
#                 cycle_start = visited[cur]
#                 cycle_length = len(chain) - cycle_start
#                 # For nodes in the cycle: answer equals cycle length.
#                 for j in range(cycle_start, len(chain)):
#                     dp[chain[j]] = cycle_length
#                 # For nodes before the cycle: add the distance to the cycle.
#                 for j in range(cycle_start - 1, -1, -1):
#                     dp[chain[j]] = dp[chain[j+1]] + 1
#                 break

#             # Otherwise, add the current node to the chain.
#             visited[cur] = len(chain)
#             chain.append(cur)
#             cur = t[cur]
    
#     sys.stdout.write(" ".join(map(str, dp)) + "\n")

# if __name__ == '__main__':
#     solve()


from collections import deque, defaultdict

def solve():
    import sys
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    # Convert to 0-based indexing.
    t = [int(x) - 1 for x in input_data[1:1+n]]
    
    # Build graph (each node points to one node) and compute in-degrees.
    in_degree = [0] * n
    for i in range(n):
        in_degree[t[i]] += 1

    # Mark nodes that are removed (not part of a cycle) using a queue.
    removed = [False] * n
    q = deque()
    for i in range(n):
        if in_degree[i] == 0:
            q.append(i)
            removed[i] = True

    while q:
        node = q.popleft()
        nxt = t[node]
        in_degree[nxt] -= 1
        if in_degree[nxt] == 0 and not removed[nxt]:
            removed[nxt] = True
            q.append(nxt)
    
    # Now, nodes not removed are part of cycles.
    ans = [-1] * n
    visited = [False] * n
    for i in range(n):
        if not removed[i] and not visited[i]:
            # Found a new cycle. Traverse it.
            cycle_nodes = []
            cur = i
            while True:
                cycle_nodes.append(cur)
                visited[cur] = True
                cur = t[cur]
                if cur == i:
                    break
            cycle_length = len(cycle_nodes)
            for node in cycle_nodes:
                ans[node] = cycle_length

    # Build reversed graph: for every edge i -> t[i], add edge t[i] -> i.
    rev = defaultdict(list)
    for i in range(n):
        rev[t[i]].append(i)

    # Start BFS from all nodes that are in cycles (or already have an answer).
    q = deque()
    for i in range(n):
        if ans[i] != -1:
            q.append(i)

    while q:
        node = q.popleft()
        for parent in rev[node]:
            # If parent's answer hasn't been set, it is in a tree leading to a cycle.
            if ans[parent] == -1:
                # The parent's answer is one more teleportation than its child.
                ans[parent] = ans[node] + 1
                q.append(parent)
    
    sys.stdout.write(" ".join(map(str, ans)) + "\n")

if __name__ == '__main__':
    solve()
