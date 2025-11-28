import subprocess
import random
import time
import sys
import os
from collections import deque

# CONFIGURATION
SOLUTION_FILE = "G.py"
PYTHON_CMD = sys.executable

def solve_reference(N, edges):
    """
    Reference logic: 
    1. Build Graph
    2. Check Bipartite
    3. Sum (Diameter + 1) for components
    """
    adj = {i: [] for i in range(1, N + 1)}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        
    visited = set()
    total_m = 0
    
    for i in range(1, N + 1):
        if i in visited:
            continue
            
        # Extract Component
        comp_nodes = []
        q = deque([i])
        visited.add(i)
        comp_nodes.append(i)
        color = {i: 0}
        
        is_bipartite = True
        idx = 0
        while idx < len(comp_nodes):
            u = comp_nodes[idx]
            idx += 1
            for v in adj[u]:
                if v not in color:
                    visited.add(v)
                    color[v] = 1 - color[u]
                    comp_nodes.append(v)
                elif color[v] == color[u]:
                    return -1 # Not bipartite
                    
        # Calc Diameter (Brute Force All-Pairs BFS)
        max_dist = 0
        for start in comp_nodes:
            dist = {start: 0}
            dq = deque([start])
            local_max = 0
            while dq:
                curr = dq.popleft()
                local_max = dist[curr]
                for neighbor in adj[curr]:
                    if neighbor not in dist:
                        dist[neighbor] = dist[curr] + 1
                        dq.append(neighbor)
            max_dist = max(max_dist, local_max)
            
        total_m += (max_dist + 1)
        
    return total_m

def generate_test_case(n, m, force_bipartite=False):
    edges = set()
    # To force bipartite, assign random partitions 0/1
    partition = {i: random.randint(0, 1) for i in range(1, n+1)}
    
    attempts = 0
    while len(edges) < m and attempts < m*5:
        attempts += 1
        u = random.randint(1, n)
        v = random.randint(1, n)
        if u == v: continue
        
        edge = tuple(sorted((u, v)))
        if edge in edges: continue
        
        if force_bipartite:
            if partition[u] != partition[v]:
                edges.add(edge)
        else:
            edges.add(edge)
            
    edge_list = list(edges)
    input_str = f"{n}\n{len(edge_list)}\n"
    for u, v in edge_list:
        input_str += f"{u} {v}\n"
        
    return input_str, n, edge_list

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

    # 1. Verify Sample Case
    print("\n[Phase 1] PDF Sample Case Verification")
    # The sample input in PDF is messy/fragmented. 
    # Let's construct a case based on visual inspection of PDF sample output logic.
    # Case 1: N=4, Output=4. Likely a path 1-2-3-4 (Dia=3, M=4)
    # Case 2: N=6, Output=-1. Likely a triangle or odd cycle.
    
    # Let's try manual cases that match the logic
    sample_input = """3
4
3
1 2
2 3
3 4
3
3
1 2
2 3
3 1
2
0
"""
    # Case 1: Path 1-2-3-4 -> Bipartite, Dia=3 -> M=4
    # Case 2: Triangle 1-2-3 -> Not Bipartite -> M=-1
    # Case 3: 2 isolated nodes -> Dia=0, Dia=0 -> M=1+1=2
    
    try:
        output = run_solution(sample_input).split()
        expected = ["4", "-1", "2"]
        
        if output == expected:
            print("Manual Logic Cases: PASS")
        else:
            print(f"Manual Logic Cases: FAIL")
            print(f"  Expected: {expected}")
            print(f"  Got:      {output}")
    except Exception as e:
        print(f"Error: {e}")

    # 2. Randomized Testing
    print("\n[Phase 2] Random Correctness Tests")
    for i in range(1, 11):
        is_bi = random.choice([True, False])
        n = 20
        m = 30
        input_data, n_val, e_list = generate_test_case(n, m, force_bipartite=is_bi)
        
        full_input = f"1\n{input_data}"
        
        try:
            user_ans = int(run_solution(full_input))
            exp_ans = solve_reference(n_val, e_list)
            
            if user_ans == exp_ans:
                print(f"Test #{i} ({'Bipartite' if is_bi else 'Random'}): PASS (Ans: {user_ans})")
            else:
                print(f"Test #{i}: FAIL")
                print(f"  Expected: {exp_ans}")
                print(f"  Got:      {user_ans}")
                return
        except Exception as e:
            print(f"Test #{i}: ERROR -> {e}")
            return

    # 3. Performance
    print("\n[Phase 3] Performance Test (N=500, Dense Bipartite)")
    # Complete Bipartite Graph K_250,250 has Diameter 2.
    # M should be 3.
    n = 500
    edges = []
    # K_250_250
    for i in range(1, 251):
        for j in range(251, 501):
            edges.append((i, j))
            
    input_str = f"1\n{n}\n{len(edges)}\n"
    for u, v in edges:
        input_str += f"{u} {v}\n"
        
    start = time.time()
    res = run_solution(input_str)
    dur = time.time() - start
    
    print(f"Time: {dur:.4f} seconds")
    if res.strip() == "3":
        print("Result: Correct (3)")
    else:
        print(f"Result: Incorrect (Got {res}, Expected 3)")
        
    if dur < 2.0:
        print("Status: PASS")
    else:
        print("Status: SLOW")

if __name__ == "__main__":
    main()