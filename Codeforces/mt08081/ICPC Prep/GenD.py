import subprocess
import random
import time
import sys
import os
import string

# CONFIGURATION
SOLUTION_FILE = "D.py"
PYTHON_CMD = sys.executable

def brute_force_solve(calligraphy_pieces, queries):
    results = []
    for q in queries:
        q_sorted = sorted(q)
        count = 0
        q_len = len(q)
        
        for piece in calligraphy_pieces:
            # Check if piece is long enough
            if len(piece) >= q_len:
                # Extract prefix of same length
                prefix = piece[:q_len]
                if sorted(prefix) == q_sorted:
                    count += 1
        
        results.append("-1" if count == 0 else str(count))
    return results

def generate_random_string(length):
    return "".join(random.choices(string.ascii_lowercase, k=length))

def generate_test_case(n, q, max_len=20):
    # Generate N unique pieces
    pieces = set()
    while len(pieces) < n:
        pieces.add(generate_random_string(random.randint(1, max_len)))
    pieces = list(pieces)
    
    # Generate Q queries
    # Make some queries likely to match by picking from existing pieces and shuffling
    queries = []
    for _ in range(q):
        if random.random() < 0.5 and pieces:
            # Create a query that definitely exists as a prefix anagram
            target = random.choice(pieces)
            prefix_len = random.randint(1, len(target))
            prefix = list(target[:prefix_len])
            random.shuffle(prefix)
            queries.append("".join(prefix))
        else:
            # Random query
            queries.append(generate_random_string(random.randint(1, max_len)))
            
    input_str = f"{n}\n" + "\n".join(pieces) + f"\n{q}\n" + "\n".join(queries) + "\n"
    return input_str, pieces, queries

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
    # 5
    # rat
    # art
    # tarp
    # part
    # trap
    # 3
    # tra
    # ar
    # tp
    # Expected: 4, 2, -1
    sample_input = """5
rat
art
tarp
part
trap
3
tra
ar
tp
"""
    try:
        user_out = run_solution(sample_input)
        expected = ["4", "2", "-1"]
        
        if user_out == expected:
            print("Sample Case: PASS")
        else:
            print(f"Sample Case: FAIL")
            print(f"  Expected: {expected}")
            print(f"  Got:      {user_out}")
    except Exception as e:
        print(f"Sample Case Error: {e}")

    # 2. Verify Correctness (Small Inputs)
    print("\n[Phase 2] Correctness Verification (Small inputs)")
    for i in range(1, 11):
        n = 20
        q = 10
        input_str, pieces, queries = generate_test_case(n, q, max_len=5)
        
        try:
            user_ans = run_solution(input_str)
            expected_ans = brute_force_solve(pieces, queries)
            
            if user_ans == expected_ans:
                print(f"Test #{i}: N={n}, Q={q} -> PASS")
            else:
                print(f"Test #{i}: FAIL")
                # Debug print first few mismatches
                for idx, (u, e) in enumerate(zip(user_ans, expected_ans)):
                    if u != e:
                        print(f"  Query '{queries[idx]}': Expected {e}, Got {u}")
                        break
                return
        except Exception as e:
            print(f"Test #{i}: ERROR -> {e}")
            return

    # 3. Performance Test
    print("\n[Phase 3] Performance Test (N=100,000, Q=100,000)")
    n = 100000
    q = 100000
    print("Generating large dataset...")
    # Generate simplified large dataset to save generation time
    # We can't check correctness easily here, just time.
    
    # Efficient generation for large string buffer
    # We create a few base strings and repeat/shuffle slightly to ensure some hits
    base_pieces = ["".join(random.choices(string.ascii_lowercase, k=20)) for _ in range(1000)]
    pieces = []
    for _ in range(n):
        pieces.append(random.choice(base_pieces))
        
    queries = []
    for _ in range(q):
        queries.append("".join(random.choices(string.ascii_lowercase, k=random.randint(1, 20))))
        
    input_str = f"{n}\n" + "\n".join(pieces) + f"\n{q}\n" + "\n".join(queries) + "\n"
    
    print("Running solution...")
    start = time.time()
    run_solution(input_str)
    dur = time.time() - start
    
    print(f"Time: {dur:.4f} seconds")
    if dur < 6.0:
        print("Status: PASS (Within 6s limit)")
    else:
        print("Status: FAIL (Time Limit Exceeded)")

if __name__ == "__main__":
    main()