import sys
import heapq

# Increase recursion depth just in case
sys.setrecursionlimit(2000)

def get_primes(limit):
    """Generates a list of primes up to limit (exclusive) using Sieve."""
    if limit < 2:
        return []
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit, i):
                is_prime[j] = False
                
    return [x for x, p in enumerate(is_prime) if p]

def solve_token(T):
    """
    Sums the highest 3 primes strictly lower than T.
    """
    # Get all primes strictly less than T
    primes = get_primes(T)
    
    if not primes:
        return 0
        
    # Take highest 3
    # If fewer than 3 primes exist (e.g., T=3 -> primes=[2]), sum what exists.
    top_3 = primes[-3:]
    return sum(top_3)

def solve():
    # Read all input
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        # Read number of test cases
        # The problem text doesn't explicitly say "First line is T", 
        # but standard ICPC format and the Sample Output count implies it.
        if not input_data: return
        num_test_cases_str = next(iterator)
        num_test_cases = int(num_test_cases_str)

        for _ in range(num_test_cases):
            # Format: N R E T
            N = int(next(iterator))
            R = int(next(iterator))
            E = int(next(iterator))
            T = int(next(iterator))
            
            # Build Graph
            adj = {i: [] for i in range(1, N + 1)}
            
            for _ in range(R):
                u = int(next(iterator))
                v = int(next(iterator))
                d = int(next(iterator))
                
                # Text says "from towns u to v", implies directed.
                # But motorways are often undirected. 
                # However, sample 1 has "1 3 3" and "3 4 1". Path 1->3->4 works.
                # Standard graph problems usually imply Directed unless stated "bidirectional".
                # Given "optimal path", we assume Directed.
                if 1 <= u <= N and 1 <= v <= N:
                    adj[u].append((v, d))
                    # If the problem were undirected, we would uncomment the next line.
                    # But based on "u to v" phrasing, we stick to directed.
                    # adj[v].append((u, d)) 

            # --- DIJKSTRA ---
            # Shortest path from 1 to E
            
            start_node = 1
            target_node = E
            
            # (cost, node)
            pq = [(0, start_node)]
            min_dist = {i: float('inf') for i in range(1, N + 1)}
            min_dist[start_node] = 0
            
            final_dist = -1
            
            while pq:
                d, u = heapq.heappop(pq)
                
                if d > min_dist[u]:
                    continue
                
                if u == target_node:
                    final_dist = d
                    break
                
                for v, weight in adj[u]:
                    if min_dist[u] + weight < min_dist[v]:
                        min_dist[v] = min_dist[u] + weight
                        heapq.heappush(pq, (min_dist[v], v))
            
            # Output Logic
            dist_output = final_dist if final_dist != -1 else 2147483647
            
            # Token Logic
            token_val = solve_token(T)
            
            print(f"{dist_output} {token_val}")

    except StopIteration:
        return

if __name__ == "__main__":
    solve()