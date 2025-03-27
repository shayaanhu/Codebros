# --- TEMPLATE 0 --- #

# -- IMPORTS -- #

import sys
import os
import math
import bisect
from collections import Counter

# -- INPUT SECTION -- #

def inint():
    return int(input())

def inlist():
    return list(map(int, input().split()))

def instr():
    s = input()
    return list(s)

def invars():
    return map(int, input().split())

# -- TESTING SECTION -- #

base_path = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(base_path, "input.txt")
if os.path.exists(input_path):
    sys.stdin = open(input_path, "r")

# --- END TEMPLATE --- #

def solve():
    n = inint()
    # Use 1-indexed arrays.
    b = [0] * (n + 1)
    leaf = [True] * (n + 1)
    
    # Read parent array.
    arr = inlist()
    for i in range(1, n + 1):
        b[i] = arr[i - 1]
        # Mark the parent as non-leaf.
        leaf[b[i]] = False

    # Special case when there is only one vertex.
    if n == 1:
        print("1")
        print("1")
        print("1")
        print("")
        return

    paths = []
    used = [False] * (n + 1)
    
    # For each vertex, if it's a leaf, trace the chain upward.
    for i in range(1, n + 1):
        if not leaf[i]:
            continue
        used[i] = True
        curr_path = [i]
        v = i
        # Follow the chain upward until reaching the root (b[v] == v) 
        # or until the next vertex is already used.
        while b[v] != v and not used[b[v]]:
            v = b[v]
            used[v] = True
            curr_path.append(v)
        paths.append(curr_path)
    
    # Output the number of paths.
    print(len(paths))
    # For each path, output its length and the reversed chain (to go from parent to child).
    for path in paths:
        rev_path = path[::-1]
        print(len(rev_path))
        print(" ".join(map(str, rev_path)))
    print("")

def main():
    t = inint()
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
