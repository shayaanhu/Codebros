import subprocess
import random
import time
import sys
import os

# CONFIGURATION
SOLUTION_FILE = "A.py"
PYTHON_CMD = sys.executable  # Uses the current python interpreter

def generate_test_case(n, m):
    """Generates a random graph with N nodes and M edges."""
    edges = set()
    while len(edges) < m:
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)
        if u != v:
            # Store as tuple sorted to ensure undirected uniqueness
            edge = tuple(sorted((u, v)))
            edges.add(edge)
    
    input_str = f"{n} {m}\n"
    for u, v in edges:
        input_str += f"{u} {v}\n"
    
    return input_str, list(edges)

def brute_force_solver(n, edges):
    """
    O(N^3) naive solver to verify correctness on small inputs.
    Checks every triplet (i, j, k) to see if valid edges exist.
    """
    adj = [[False] * n for _ in range(n)]
    for u, v in edges:
        adj[u][v] = True
        adj[v][u] = True
    
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if adj[i][j] and adj[j][k] and adj[k][i]:
                    count += 1
    return count

def run_solution(input_str):
    """Runs the target solution file with the given input string."""
    start_time = time.time()
    process = subprocess.Popen(
        [PYTHON_CMD, SOLUTION_FILE],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate(input=input_str)
    end_time = time.time()
    
    if process.returncode != 0:
        raise RuntimeError(f"Solution crashed: {stderr}")
        
    return int(stdout.strip()), end_time - start_time

def main():
    print(f"--- Testing {SOLUTION_FILE} ---")
    
    if not os.path.exists(SOLUTION_FILE):
        print(f"Error: {SOLUTION_FILE} not found.")
        return

    # 1. Verify correctness with small random tests
    print("\n[Phase 1] Correctness Verification (Small inputs)")
    for i in range(1, 6):
        n = 50
        m = random.randint(n, n * (n - 1) // 4)  # Random density
        input_data, edges = generate_test_case(n, m)
        
        try:
            # Get user output
            user_ans, _ = run_solution(input_data)
            # Get expected output (Brute Force)
            expected_ans = brute_force_solver(n, edges)
            
            if user_ans == expected_ans:
                print(f"Test #{i}: N={n}, M={m} -> PASS (Ans: {user_ans})")
            else:
                print(f"Test #{i}: N={n}, M={m} -> FAIL")
                print(f"  Expected: {expected_ans}")
                print(f"  Got:      {user_ans}")
                return
        except Exception as e:
            print(f"Test #{i}: ERROR -> {e}")
            return

    # 2. Verify Sample Case from PDF
    print("\n[Phase 2] PDF Sample Case Verification")
    sample_input = "6 9\n0 1\n1 2\n1 3\n2 3\n3 4\n4 0\n2 5\n5 0\n5 1\n"
    try:
        user_ans, _ = run_solution(sample_input)
        if user_ans == 3:
             print("Sample Case: PASS (Ans: 3)")
        else:
             print(f"Sample Case: FAIL (Expected 3, Got {user_ans})")
    except Exception as e:
        print(f"Sample Case: ERROR -> {e}")

    # 3. Performance Test (Max Constraints)
    print("\n[Phase 3] Performance Test (N=2000, High Density)")
    n = 2000
    # Create a reasonably dense graph (~10% of max edges for a realistic heavy test)
    # Max edges is ~2,000,000. 10% is 200,000.
    m = 200000 
    print(f"Generating graph with N={n}, M={m}...")
    input_data, _ = generate_test_case(n, m)
    
    print("Running solution...")
    try:
        ans, duration = run_solution(input_data)
        print(f"Result: {ans} triangles found.")
        print(f"Time: {duration:.4f} seconds")
        
        if duration < 18.0:
            print("Status: PASS (Within 18s limit)")
        else:
            print("Status: FAIL (Time Limit Exceeded)")
            
    except Exception as e:
        print(f"Performance Test: ERROR -> {e}")

if __name__ == "__main__":
    main()