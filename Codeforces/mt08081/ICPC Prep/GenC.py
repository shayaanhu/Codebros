import subprocess
import random
import time
import sys
import os
from functools import lru_cache

# CONFIGURATION
SOLUTION_FILE = "C.py"
PYTHON_CMD = sys.executable

# --- Reference Solver (Recursive DFS + Memoization) ---
# This is easier to verify logically but slower/hits recursion limits on large inputs.
# Perfect for checking the iterative solution on small inputs.
def solve_reference_recursive(n, k, prices):
    # @lru_cache automatically handles memoization
    @lru_cache(None)
    def dfs(index, transactions_left, holding):
        # Base Cases
        if index == n or transactions_left == 0:
            return 0
        
        # Do nothing choice
        res = dfs(index + 1, transactions_left, holding)
        
        if holding:
            # Choice: Sell
            # If we sell, we gain price[index], holding becomes False, transactions decrement
            res = max(res, prices[index] + dfs(index + 1, transactions_left - 1, False))
        else:
            # Choice: Buy
            # If we buy, we lose price[index], holding becomes True
            # Note: Buying doesn't reduce transaction count yet; selling does (or vice versa).
            # Standard convention: A pair (Buy+Sell) is 1 transaction. 
            # So we decrement only on sell (as done above) or buy.
            # Let's decrement on sell to align with the problem logic.
            res = max(res, -prices[index] + dfs(index + 1, transactions_left, True))
            
        return res

    # Start: Day 0, k transactions allowed, not holding stock
    return dfs(0, k, False)

def generate_test_case(max_n=20, max_k=5):
    """Generates a single test case."""
    n = random.randint(1, max_n)
    k = random.randint(1, max_k)
    prices = [random.randint(1, 100) for _ in range(n)]
    
    input_str = f"{k}\n{n}\n" + " ".join(map(str, prices)) + "\n"
    return input_str, (n, k, prices)

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

    # 1. Verify Sample Cases from PDF
    print("\n[Phase 1] PDF Sample Case Verification")
    # Sample 1: k=2, n=6, prices=[10, 22, 5, 75, 65, 80] -> Profit 87
    # Sample 2: k=1, n=5, prices=[90, 80, 70, 60, 50] -> Profit 0
    sample_input = """2
2
6
10 22 5 75 65 80
1
5
90 80 70 60 50
"""
    try:
        output = run_solution(sample_input).split()
        
        if output[0] == "87":
            print("Sample 1: PASS (Ans: 87)")
        else:
            print(f"Sample 1: FAIL (Expected 87, Got {output[0]})")
            
        if len(output) > 1 and output[1] == "0":
            print("Sample 2: PASS (Ans: 0)")
        else:
            print(f"Sample 2: FAIL (Expected 0, Got {output[1] if len(output) > 1 else 'None'})")
            
    except Exception as e:
        print(f"Sample Test Error: {e}")

    # 2. Verify Correctness (Small Inputs vs Reference)
    print("\n[Phase 2] Correctness Verification (Small inputs)")
    for i in range(1, 11):
        t_input, params = generate_test_case(max_n=15, max_k=4)
        full_input = f"1\n{t_input}"
        
        try:
            user_ans = int(run_solution(full_input))
            expected_ans = solve_reference_recursive(*params)
            
            if user_ans == expected_ans:
                print(f"Test #{i}: N={params[0]}, K={params[1]} -> PASS (Ans: {user_ans})")
            else:
                print(f"Test #{i}: N={params[0]}, K={params[1]} -> FAIL")
                print(f"  Expected: {expected_ans}")
                print(f"  Got:      {user_ans}")
                print(f"  Prices:   {params[2]}")
                return
        except Exception as e:
            print(f"Test #{i}: ERROR -> {e}")
            return

    # 3. Performance Test
    print("\n[Phase 3] Performance Test")
    # Case A: Large N, Small K (DP Path)
    n = 10000
    k = 100
    prices = [random.randint(1, 1000) for _ in range(n)]
    input_str = f"1\n{k}\n{n}\n" + " ".join(map(str, prices))
    
    start = time.time()
    run_solution(input_str)
    dur = time.time() - start
    print(f"Test A (N=10k, K=100): {dur:.4f}s {'(PASS)' if dur < 1.0 else '(FAIL)'}")
    
    # Case B: Large N, Large K (Greedy Path)
    n = 10000
    k = 6000 # > N/2
    prices = [random.randint(1, 1000) for _ in range(n)]
    input_str = f"1\n{k}\n{n}\n" + " ".join(map(str, prices))
    
    start = time.time()
    run_solution(input_str)
    dur = time.time() - start
    print(f"Test B (N=10k, K=6k):  {dur:.4f}s {'(PASS)' if dur < 1.0 else '(FAIL)'}")

if __name__ == "__main__":
    main()