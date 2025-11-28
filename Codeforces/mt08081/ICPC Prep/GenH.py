import subprocess
import random
import time
import sys
import os
import heapq

# CONFIGURATION
SOLUTION_FILE = "H.py"
PYTHON_CMD = sys.executable

def get_primes_naive(n):
    """Naive prime check for verification."""
    primes = []
    for num in range(2, n):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

def solve_reference(N, R, E, T, edges):
    # 1. Reference Shortest Path (Floyd Warshall)
    dist = [[float('inf')] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        dist[i][i] = 0
        
    for u, v, d in edges:
        # Handle multiple edges between same nodes by keeping min
        dist[u][v] = min(dist[u][v], d)
        
    # --- THE MISSING LOOP FIXED HERE ---
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    # -----------------------------------
        
    shortest_dist = dist[1][E]
    if shortest_dist == float('inf'):
        shortest_dist = 2147483647
    else:
        shortest_dist = int(shortest_dist)
        
    # 2. Reference Token
    primes = get_primes_naive(T)
    token_val = sum(primes[-3:]) if primes else 0
    
    return shortest_dist, token_val

def run_solution(input_str):
    process = subprocess.Popen(
        [PYTHON_CMD, SOLUTION_FILE],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate(input=input_str)
    if process.returncode != 0:
        raise RuntimeError(f"Solution crashed: {stderr}")
    return stdout.strip().split('\n')

def main():
    print(f"--- Testing {SOLUTION_FILE} ---")
    
    if not os.path.exists(SOLUTION_FILE):
        print(f"Error: {SOLUTION_FILE} not found.")
        return

    # 1. Verify Sample Case (Reconstructed from logic)
    print("\n[Phase 1] PDF Sample Case Verification")
    sample_input = """2
4 4 3 10
1 2 2
1 3 3
2 3 4
3 4 1
4 2 3 15
1 2 2
3 4 1
"""
    try:
        output = run_solution(sample_input)
        
        if "3 15" in output[0]:
            print("Sample 1: PASS")
        else:
            print(f"Sample 1: FAIL (Got '{output[0]}')")
            
        if "2147483647 31" in output[1]:
            print("Sample 2: PASS")
        else:
            print(f"Sample 2: FAIL (Got '{output[1]}')")
            
    except Exception as e:
        print(f"Sample Error: {e}")

    # 2. Randomized Tests
    print("\n[Phase 2] Random Correctness Tests")
    for i in range(1, 11):
        N = 20
        R = 40
        e = random.randint(1, N)
        t = random.randint(10, 1000)
        edges = []
        for _ in range(R):
            u = random.randint(1, N)
            v = random.randint(1, N)
            d = random.randint(1, 10)
            edges.append((u, v, d))
            
        input_block = f"{N} {R} {e} {t}\n"
        for u, v, d in edges:
            input_block += f"{u} {v} {d}\n"
            
        full_input = f"1\n{input_block}" # 1 test case
        
        try:
            # Run Solution
            user_out_lines = run_solution(full_input)
            if not user_out_lines:
                print(f"Test #{i}: FAIL (No Output)")
                continue
                
            user_dist, user_token = map(int, user_out_lines[0].split())
            
            # Run Reference
            ref_dist, ref_token = solve_reference(N, R, e, t, edges)
            
            if user_dist == ref_dist and user_token == ref_token:
                print(f"Test #{i}: PASS")
            else:
                print(f"Test #{i}: FAIL")
                print(f"  Expected: {ref_dist} {ref_token}")
                print(f"  Got:      {user_dist} {user_token}")
                return
                
        except Exception as e:
            print(f"Test #{i}: ERROR -> {e}")
            return

    print("\n[Phase 3] Performance Test")
    input_str = "1\n100 5000 100 30000\n"
    for _ in range(5000):
        input_str += f"{random.randint(1,99)} {random.randint(1,100)} {random.randint(1,100)}\n"
        
    start = time.time()
    run_solution(input_str)
    dur = time.time() - start
    print(f"Time: {dur:.4f} seconds")
    if dur < 1.0:
        print("Status: PASS")
    else:
        print("Status: FAIL")

if __name__ == "__main__":
    main()