import sys
import math

# Increase recursion depth just in case
sys.setrecursionlimit(2000)

def solve():
    # Read all input at once for efficiency
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        # Read Number of Test Cases K
        if not input_data: return
        K_str = next(iterator, None)
        if not K_str: return
        K = int(K_str)

        for _ in range(K):
            # Read N, T, M
            N = int(next(iterator))
            T = int(next(iterator))
            M = int(next(iterator))
            
            # Edge Case: 0 Categories
            if N == 0:
                # If we have 0 categories, total count must be 0 to be valid.
                print(1 if T == 0 else 0)
                continue
            
            # Calculate minimum required insects
            min_needed = N * M
            
            # If we don't have enough insects to meet the minimums, 0 ways
            if T < min_needed:
                print(0)
                continue
            
            # Remaining insects to distribute freely
            remaining = T - min_needed
            
            # Stars and Bars Formula: C(n + k - 1, k - 1)
            # where n is items (remaining) and k is bins (N)
            # C(remaining + N - 1, N - 1)
            
            # Python 3.8+ has math.comb
            ans = math.comb(remaining + N - 1, N - 1)
            print(ans)
            
    except StopIteration:
        return

if __name__ == "__main__":
    solve()