import subprocess
import random
import time
import sys
import os
import math

# CONFIGURATION
SOLUTION_FILE = "E.py"
PYTHON_CMD = sys.executable

def solve_brute_force(N, T, M):
    """
    Recursively finds number of ways to sum to T with N numbers, each >= M.
    Slow, but 100% logically accurate for verification.
    """
    if N == 0:
        return 1 if T == 0 else 0
    
    count = 0
    
    def backtrack(index, current_sum):
        nonlocal count
        # Pruning: If current sum already exceeds T, stop
        if current_sum > T:
            return
        
        # Base Case: Last category
        if index == N - 1:
            # The last category must take whatever is left
            remaining = T - current_sum
            if remaining >= M:
                count += 1
            return

        # Try giving this category 'val' insects
        # It must have at least M. 
        # Max it can have is T - current_sum - (remaining categories * M)
        # But for brute force simple loop is fine
        max_possible = T - current_sum - (N - 1 - index) * M
        
        for val in range(M, max_possible + 1):
            backtrack(index + 1, current_sum + val)

    backtrack(0, 0)
    return count

def generate_test_case():
    """Generates random inputs."""
    # Small inputs for brute force verification
    N = random.randint(1, 5)
    M = random.randint(0, 5)
    # Ensure T is sometimes valid, sometimes invalid
    min_req = N * M
    T = random.randint(min_req - 2 if min_req > 2 else 0, min_req + 15)
    
    return f"{N} {T} {M}", (N, T, M)

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
    return stdout.strip().split()

def main():
    print(f"--- Testing {SOLUTION_FILE} ---")
    
    if not os.path.exists(SOLUTION_FILE):
        print(f"Error: {SOLUTION_FILE} not found.")
        return

    # 1. Verify Sample Case from PDF
    print("\n[Phase 1] PDF Sample Case Verification")
    # Sample:
    # 2
    # 3 34 10
    # 2 40 15
    # Expected: 15, 11
    
    # Note: The PDF also had a weird line "30 3 15" with output 0.
    # This is likely N=30, T=3, M=15 (Impossible), or T=30, N=3, M=15 (Impossible).
    # Let's test the clear ones first.
    
    sample_input = "2\n3 34 10\n2 40 15\n"
    expected = ["15", "11"]
    
    try:
        user_out = run_solution(sample_input)
        if user_out == expected:
            print("Sample Cases: PASS")
        else:
            print(f"Sample Cases: FAIL")
            print(f"  Expected: {expected}")
            print(f"  Got:      {user_out}")
    except Exception as e:
        print(f"Sample Case Error: {e}")

    # 2. Verify Correctness (Small Inputs)
    print("\n[Phase 2] Correctness Verification (Small inputs)")
    num_tests = 10
    input_lines = [str(num_tests)]
    params_list = []
    
    for _ in range(num_tests):
        line, params = generate_test_case()
        input_lines.append(line)
        params_list.append(params)
        
    full_input = "\n".join(input_lines)
    
    try:
        user_out = run_solution(full_input)
        user_ints = [int(x) for x in user_out]
        
        all_pass = True
        for i, (u, p) in enumerate(zip(user_ints, params_list)):
            expected = solve_brute_force(*p)
            if u != expected:
                print(f"Test #{i+1}: N={p[0]}, T={p[1]}, M={p[2]} -> FAIL")
                print(f"  Expected: {expected}")
                print(f"  Got:      {u}")
                all_pass = False
                break
                
        if all_pass:
            print(f"All {num_tests} Random Small Tests: PASS")
            
    except Exception as e:
        print(f"Verification Error: {e}")

    # 3. Edge Cases
    print("\n[Phase 3] Edge Case Verification")
    # N=1, T=10, M=5 -> 1 way (10)
    # N=3, T=10, M=4 -> 0 ways (Need 12)
    # N=0, T=0, M=5 -> 1 way
    # N=0, T=5, M=5 -> 0 ways
    
    edge_input = "4\n1 10 5\n3 10 4\n0 0 5\n0 5 5"
    expected_edge = ["1", "0", "1", "0"]
    
    try:
        edge_out = run_solution(edge_input)
        if edge_out == expected_edge:
            print("Edge Cases: PASS")
        else:
            print(f"Edge Cases: FAIL")
            print(f"  Expected: {expected_edge}")
            print(f"  Got:      {edge_out}")
    except Exception as e:
        print(f"Edge Error: {e}")

if __name__ == "__main__":
    main()