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
    A, B, k = inlist()  # read A, B, and k
    xs = inlist()       # read the k values for x coordinates
    ys = inlist()       # read the k values for y coordinates
    
    # Create count arrays for A and B
    a = [0] * A
    b = [0] * B
    edges = []
    
    for i in range(k):
        # Adjust indices from 1-indexed to 0-indexed
        x = xs[i] - 1
        y = ys[i] - 1
        edges.append((x, y))
        a[x] += 1
        b[y] += 1

    ans = 0
    for x, y in edges:
        ans += (k - a[x] - b[y] + 1)
    print(ans // 2)

def main():
    t = inint()
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
