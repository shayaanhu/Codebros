import subprocess
import random
import time
import sys
import os
import string

# CONFIGURATION
SOLUTION_FILE = "F.py"
PYTHON_CMD = sys.executable

def solve_brute_force(events):
    """
    O(N^2) verification of the sliding window.
    Finds longest unique subarray.
    """
    n = len(events)
    best_len = 0
    best_sub = []
    
    for i in range(n):
        seen = set()
        current_sub = []
        for j in range(i, n):
            if events[j] in seen:
                break
            seen.add(events[j])
            current_sub.append(events[j])
            
        if len(current_sub) > best_len:
            best_len = len(current_sub)
            best_sub = current_sub
        elif len(current_sub) == best_len:
            # Tie break: lexicographical first element
            if best_sub and current_sub and current_sub[0] < best_sub[0]:
                best_sub = current_sub
                
    return best_len, best_sub

def generate_valid_code():
    cat = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
    num = f"{random.randint(1, 99):02d}"
    return cat + num

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
    sample_input = """5
A01B02C03D04
A01A02A03
G01G02G03G04
A01A01A02A01
A01A02A3D02F09
"""
    # Expected behavior derived from PDF:
    # 1. 4 A01 B02 C03 D04 1 Competitions 1 Entertainment 1 Social Gatherings 1 Dinners
    # 2. 3 A01 A02 A03 3 Competitions
    # 3. 4 G01 G02 G03 G04 4 Exams
    # 4. 2 A01 A02 2 Competitions (A01 A01 A02 A01 -> longest unique is A01 A02 or A02 A01. A01 < A02, so A01 A02)
    # 5. -1 A3D (Invalid code)
    
    try:
        output = run_solution(sample_input).split('\n')
        
        # Basic checks
        if "4 A01 B02 C03 D04" in output[0]: print("Sample 1: PASS")
        else: print(f"Sample 1: FAIL -> {output[0]}")
        
        if "3 A01 A02 A03 3 Competitions" in output[1]: print("Sample 2: PASS")
        else: print(f"Sample 2: FAIL -> {output[1]}")
        
        if "4 G01 G02 G03 G04 4 Exams" in output[2]: print("Sample 3: PASS")
        else: print(f"Sample 3: FAIL -> {output[2]}")
        
        if "2 A01 A02 2 Competitions" in output[3]: print("Sample 4: PASS")
        else: print(f"Sample 4: FAIL -> {output[3]}")
        
        if "-1 A3D" in output[4]: print("Sample 5: PASS")
        else: print(f"Sample 5: FAIL -> {output[4]}")

    except Exception as e:
        print(f"Sample Error: {e}")

    # 2. Randomized Testing (Valid Inputs)
    print("\n[Phase 2] Random Valid Inputs")
    for i in range(1, 6):
        # Generate random stream
        num_events = 20
        events = [generate_valid_code() for _ in range(num_events)]
        stream = "".join(events)
        
        full_input = f"1\n{stream}"
        
        user_out = run_solution(full_input)
        exp_len, exp_seq = solve_brute_force(events)
        
        # Check if output starts with correct length
        try:
            parts = user_out.split()
            u_len = int(parts[0])
            u_seq = parts[1 : 1 + u_len]
            
            if u_len == exp_len and u_seq == exp_seq:
                print(f"Test #{i}: PASS (Len {u_len})")
            else:
                print(f"Test #{i}: FAIL")
                print(f"  Expected: {exp_len} {' '.join(exp_seq)}")
                print(f"  Got:      {user_out}")
        except:
            print(f"Test #{i}: CRASH/PARSE ERROR")

    # 3. Invalid Input Detection
    print("\n[Phase 3] Invalid Inputs")
    invalids = [
        ("A01B2C03", "-1 B2C"), # Middle malformed
        ("A01B02A", "-1 A"),    # Trailing
        ("Z01A02", "-1 Z01"),   # Bad char
        ("A01B0$C02", "-1 B0$") # Bad digit
    ]
    
    for inp, expected_start in invalids:
        res = run_solution(f"1\n{inp}")
        if res.startswith(expected_start):
            print(f"Invalid '{inp}': PASS")
        else:
            print(f"Invalid '{inp}': FAIL (Got '{res}')")

if __name__ == "__main__":
    main()