import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)

def solve():
    # Read all input at once to handle messy newlines/whitespace
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        # Parse number of test cases
        T_str = next(iterator)
        T = int(T_str)
    except StopIteration:
        return

    for _ in range(T):
        try:
            N = int(next(iterator))
            e1 = int(next(iterator))
            e2 = int(next(iterator))
            
            # Read Processing Times (w1 and w2)
            w1 = [int(next(iterator)) for _ in range(N)]
            w2 = [int(next(iterator)) for _ in range(N)]
            
            # Read Switching Times (s1 and s2)
            # There are N-1 switching times
            s1 = [int(next(iterator)) for _ in range(N - 1)]
            s2 = [int(next(iterator)) for _ in range(N - 1)]
            
            # Read Exit Times
            x1 = int(next(iterator))
            x2 = int(next(iterator))
            
            # --- DP TRANSITION ---
            
            # Base Case: Station 0 (First station)
            # Time includes entry time + processing time at station 0
            dp1 = e1 + w1[0]
            dp2 = e2 + w2[0]
            
            # Iterate from Station 1 to N-1
            for i in range(1, N):
                prev_dp1 = dp1
                prev_dp2 = dp2
                
                # Calculate min time to finish Station 'i' on Lane 1
                # Option A: Stay on Lane 1 (prev_dp1)
                # Option B: Switch from Lane 2 (prev_dp2 + cost to switch 2->1)
                # Note: s2[i-1] is the cost to switch AFTER station i-1
                dp1 = min(prev_dp1, prev_dp2 + s2[i-1]) + w1[i]
                
                # Calculate min time to finish Station 'i' on Lane 2
                # Option A: Stay on Lane 2 (prev_dp2)
                # Option B: Switch from Lane 1 (prev_dp1 + cost to switch 1->2)
                dp2 = min(prev_dp2, prev_dp1 + s1[i-1]) + w2[i]
                
            # --- FINAL EXIT ---
            # Add exit times
            final_time = min(dp1 + x1, dp2 + x2)
            print(final_time)
            
        except StopIteration:
            break

if __name__ == "__main__":
    solve()