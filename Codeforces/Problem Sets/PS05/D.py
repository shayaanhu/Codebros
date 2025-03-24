# --- TEMPLATE 1 --- #

# -- IMPORTS -- #
import sys
import os
import math
import bisect
from collections import Counter, deque
import time

# -- LOCAL DEBUG SETUP -- #
LOCAL = os.environ.get("TERM_PROGRAM", "").lower() == "vscode"

def debug(*args, **kwargs):
    if LOCAL:
        print("DBG:", *args, **kwargs)

# -- INPUT SECTION -- #

def inint():
    return int(sys.stdin.readline())

def inlist():
    return list(map(int, sys.stdin.readline().split()))

def instr():
    s = sys.stdin.readline()
    return list(s)

def invars():
    return map(int, sys.stdin.readline().split())

# -- TESTING SECTION -- #
base_path = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(base_path, "wormsort.in")
if os.path.exists(input_path):
    sys.stdin = open(input_path, "r")
    sys.stdout = open(os.path.join(base_path, "wormsort.out"), "w")

# -- START TIMER FOR EXECUTION TIME TRACKING -- #
if LOCAL:
    start_time = time.perf_counter()
    
# --- BEGIN PROBLEM LOGIC --- #

# DSU union find
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n

    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return
        if self.rank[a] < self.rank[b]:
            self.parent[a] = b
        elif self.rank[a] > self.rank[b]:
            self.parent[b] = a
        else:
            self.parent[b] = a
            self.rank[a] += 1

def solve():
    n, m = invars()
    
    # p[i] = cow at location i+1 (using 0-indexing for positions)
    p = inlist()  # permutation of cows, positions 1...N (0-indexed array)
    
    # If cows are already sorted, no wormholes are needed.
    if all(p[i] == i+1 for i in range(n)):
        print(-1)
        return
    
    wormholes = []
    maxW = 0
    for _ in range(m):
        a, b, w = invars()
        # Adjust locations to 0-indexing.
        wormholes.append((a-1, b-1, w))
        maxW = max(maxW, w)
    
    pos = [0] * (n+1)  # using 1-indexing for cows; we'll ignore index 0.
    for i in range(n):
        pos[p[i]] = i
    
    def can_sort(X):
        dsu = DSU(n)
        for a, b, w in wormholes:
            if w >= X:
                dsu.union(a, b)
        for cow in range(1, n+1):
            if dsu.find(pos[cow]) != dsu.find(cow-1):
                return False
        return True

    lo, hi = 1, maxW
    ans = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if can_sort(mid):
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1
    
    print(ans)

# --- END PROBLEM LOGIC --- #

# -- PRINT EXECUTION TIME -- #
if LOCAL:
    end_time = time.perf_counter()
    print("Execution time:", end_time - start_time, "seconds", file=sys.stderr)

if __name__ == "__main__":
    solve()
