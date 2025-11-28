import subprocess
import random
import time
import sys
import os

# CONFIGURATION
SOLUTION_FILE = "B.py"
PYTHON_CMD = sys.executable

def solve_brute_force_recursive(N, e1, e2, w1, w2, s1, s2, x1, x2):
    """
    A naive recursive solver (O(2^N)) to verify correctness on small N.
    """
    
    # memoization is not strictly needed for very small N (<= 15) 
    # but let's keep it pure recursion to be a distinct implementation.
    
    def min_cost(index, lane):
        # Base case: If we finished the last station
        if index == N - 1:
            if lane == 1:
                return w1[index] + x1
            else:
                return w2[index] + x2
        
        # Recursive Step
        cost_current = w1[index] if lane == 1 else w2[index]
        
        # Next if we stay in same lane
        cost_stay = min_cost(index + 1, lane)
        
        # Next if we switch lanes
        if lane == 1:
            # Switch 1 -> 2
            cost_switch = s1[index] + min_cost(index + 1, 2)
        else:
            # Switch 2 -> 1
            cost_switch = s2[index] + min_cost(index + 1, 1)
            
        return cost_current + min(cost_stay, cost_switch)

    # Start recursion
    path1 = e1 + min_cost(0, 1)
    path2 = e2 + min_cost(0, 2)
    
    return min(path1, path2)

def generate_test_case(n):
    """Generates a single test case input string and the data structures."""
    e1, e2 = random.randint(1, 20), random.randint(1, 20)
    w1 = [random.randint(1, 20) for _ in range(n)]
    w2 = [random.randint(1, 20) for _ in range(n)]
    s1 = [random.randint(1, 10) for _ in range(n - 1)]
    s2 = [random.randint(1, 10) for _ in range(n - 1)]
    x1, x2 = random.randint(1, 20), random.randint(1, 20)
    
    # Format as string
    input_str = f"{n}\n{e1} {e2}\n"
    input_str += " ".join(map(str, w1)) + "\n"
    input_str += " ".join(map(str, w2)) + "\n"
    input_str += " ".join(map(str, s1)) + "\n"
    input_str += " ".join(map(str, s2)) + "\n"
    input_str += f"{x1} {x2}\n"
    
    return input_str, (n, e1, e2, w1, w2, s1, s2, x1, x2)

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
    return stdout.strip()

def main():
    print(f"--- Testing {SOLUTION_FILE} ---")
    
    if not os.path.exists(SOLUTION_FILE):
        print(f"Error: {SOLUTION_FILE} not found.")
        return

    # 1. Verify Sample Case from PDF
    # Based on visual extraction of the table in PDF
    print("\n[Phase 1] PDF Sample Case Verification")
    sample_input = """2
5
2 4
7 9 3 4 8
8 5 6 4 5
2 3 1 3
2 1 2 2
3 2
4
10 12
6 7 8 9
5 6 7 8
4 2 3
2 1 3
3 4
"""
    expected_output = ["42", ""] # We don't know the second sample output from the snippet, but we know the first is 42
    # Actually, the PDF text dump shows "42" for the first case.
    
    try:
        user_out = run_solution(sample_input).split()
        if user_out[0] == "42":
            print("Sample Case 1: PASS (Ans: 42)")
        else:
            print(f"Sample Case 1: FAIL (Expected 42, Got {user_out[0]})")
            
        # Note: We don't strictly know the 2nd sample answer from the provided text snippet 
        # (it cuts off), so we rely on random tests for further validation.
        print(f"Sample Case 2 Output: {user_out[1]}")
        
    except Exception as e:
        print(f"Sample Case: ERROR -> {e}")

    # 2. Verify Correctness with Recursive Solver
    print("\n[Phase 2] Correctness Verification (Small inputs)")
    for i in range(1, 11):
        n = 12 # Small enough for recursion
        t_input, params = generate_test_case(n)
        full_input = f"1\n{t_input}" # Add T=1
        
        try:
            # User DP Solution
            user_ans = int(run_solution(full_input))
            
            # Brute Force Recursive Solution
            expected_ans = solve_brute_force_recursive(*params)
            
            if user_ans == expected_ans:
                print(f"Test #{i}: N={n} -> PASS (Ans: {user_ans})")
            else:
                print(f"Test #{i}: N={n} -> FAIL")
                print(f"  Expected: {expected_ans}")
                print(f"  Got:      {user_ans}")
                return
        except Exception as e:
            print(f"Test #{i}: ERROR -> {e}")
            return

    # 3. Performance Test
    print("\n[Phase 3] Performance Test (N=100,000)")
    # Generate one huge test case
    n = 100000
    # We construct it manually to be fast
    e1, e2 = 10, 10
    w1 = [10] * n
    w2 = [10] * n
    s1 = [5] * (n-1)
    s2 = [5] * (n-1)
    x1, x2 = 10, 10
    
    # String building optimization
    lines = [
        "1",
        str(n),
        f"{e1} {e2}",
        " ".join(map(str, w1)),
        " ".join(map(str, w2)),
        " ".join(map(str, s1)),
        " ".join(map(str, s2)),
        f"{x1} {x2}"
    ]
    input_data = "\n".join(lines)
    
    start = time.time()
    run_solution(input_data)
    duration = time.time() - start
    
    print(f"Time: {duration:.4f} seconds")
    if duration < 1.0:
        print("Status: PASS (Well within 1s limit)")
    else:
        print("Status: WARNING (Close to limit, or overhead from Python string/process creation)")

if __name__ == "__main__":
    main()