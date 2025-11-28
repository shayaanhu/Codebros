import sys
from collections import deque, defaultdict

# Increase recursion depth just in case
sys.setrecursionlimit(3000)

def solve():
    # Read all input at once
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        t_str = next(iterator)
        t = int(t_str)
    except StopIteration:
        return

    for _ in range(t):
        try:
            N = int(next(iterator))
            W = int(next(iterator))
            
            adj = defaultdict(list)
            
            # Parse W edges
            for _ in range(W):
                u = int(next(iterator))
                v = int(next(iterator))
                adj[u].append(v)
                adj[v].append(u)
                
            # Global visited set for component handling
            visited_global = set()
            possible = True
            total_districts = 0
            
            # Iterate 1 to N to find components
            for i in range(1, N + 1):
                if i in visited_global:
                    continue
                
                # --- STEP 1: Extract Component & Check Bipartite ---
                component_nodes = []
                q = deque([i])
                visited_global.add(i)
                
                # Color map for bipartite check: node -> 0 or 1
                color = {i: 0}
                component_nodes.append(i)
                is_bipartite = True
                
                # BFS for Component Extraction + 2-Coloring
                # Using a separate queue for traversal to avoid modifying q while iterating? 
                # No, standard BFS is fine.
                
                idx = 0
                while idx < len(component_nodes):
                    u = component_nodes[idx]
                    idx += 1
                    
                    c = color[u]
                    
                    for v in adj[u]:
                        if v not in color:
                            visited_global.add(v)
                            color[v] = 1 - c
                            component_nodes.append(v)
                        elif color[v] == c:
                            # Odd cycle detected
                            is_bipartite = False
                            
                if not is_bipartite:
                    possible = False
                    break
                
                # --- STEP 2: Find Diameter of Component ---
                # We run BFS from every node in this component to find max eccentricity
                max_eccentricity = 0
                
                for start_node in component_nodes:
                    # Optimization: If component is single node, dist is 0
                    if len(component_nodes) == 1:
                        break
                        
                    # BFS to find furthest node from start_node
                    # We don't need to track visited, just distance
                    # We only traverse nodes in adj, which are within component
                    
                    dist = {start_node: 0}
                    bfs_q = deque([start_node])
                    local_max = 0
                    
                    while bfs_q:
                        u = bfs_q.popleft()
                        d = dist[u]
                        if d > local_max:
                            local_max = d
                            
                        for v in adj[u]:
                            if v not in dist:
                                dist[v] = d + 1
                                bfs_q.append(v)
                                
                    if local_max > max_eccentricity:
                        max_eccentricity = local_max
                
                # Districts needed for this component = Diameter + 1
                total_districts += (max_eccentricity + 1)
            
            if possible:
                print(total_districts)
            else:
                print("-1")

        except StopIteration:
            break

if __name__ == "__main__":
    solve()