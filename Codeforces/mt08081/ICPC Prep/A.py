import sys

# Increase recursion depth just in case, though not needed for this iterative solution
sys.setrecursionlimit(2000)

def solve():
    # Read all input from stdin at once and split by whitespace
    # This handles cases where N and M are on the same line, separate lines, 
    # or weirdly spaced (like "69" appearing as "6 9" in some PDF copies)
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        N = int(next(iterator))
        M = int(next(iterator))
    except StopIteration:
        return

    # Adjacency list using Bitmasks (integers)
    # adj[i] will store a binary number where the j-th bit is 1 if i connects to j
    # This reduces space and allows O(1) bitwise operations for row intersections
    adj = [0] * N
    
    # Parse edges
    for _ in range(M):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
            
            # Skip invalid indices just in case
            if u < 0 or u >= N or v < 0 or v >= N:
                continue
                
            # Set bit v for u, and bit u for v (Undirected Graph)
            adj[u] |= (1 << v)
            adj[v] |= (1 << u)
        except StopIteration:
            break
            
    triangle_count = 0
    
    # ALGORITHM:
    # Iterate through every node 'i'.
    # Iterate through every node 'j' > 'i'.
    # If i and j are connected, then any common neighbor 'k' forms a triangle (i, j, k).
    # The common neighbors are found by (adj[i] & adj[j]).
    # The number of common neighbors is the population count (number of set bits) of that result.
    
    for i in range(N):
        # Optimization: Only check j > i to avoid double counting pairs and self-loops
        # We only care about neighbors of i to prune the search space
        
        # Get the bitmask of neighbors of i
        neighbors_i = adj[i]
        
        # We iterate j from i+1 to N-1. 
        # Optimization: check if 'i' has any neighbors > i.
        if (neighbors_i >> (i + 1)) == 0:
            continue

        for j in range(i + 1, N):
            # Check if there is an edge between i and j
            # (neighbors_i >> j) & 1 checks if the j-th bit is set
            if (neighbors_i >> j) & 1:
                # Find common neighbors using Bitwise AND
                common_neighbors = neighbors_i & adj[j]
                
                # Add the number of set bits to the count
                # .bit_count() is efficient in Python 3.10+
                triangle_count += common_neighbors.bit_count()
                
    # Each triangle (u, v, w) is counted 3 times:
    # 1. When checking edge (u, v) -> finds w
    # 2. When checking edge (u, w) -> finds v
    # 3. When checking edge (v, w) -> finds u
    # So we divide by 3.
    print(triangle_count // 3)

if __name__ == "__main__":
    solve()