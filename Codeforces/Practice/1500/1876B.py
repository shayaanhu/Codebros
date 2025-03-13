# --- TEMPLATE 0 --- #

# -- IMPORTS -- #

import sys
import os
import math
import bisect
from collections import defaultdict, Counter

# -- INPUT SECTION -- #

def inint():
    return(int(input()))

def inlist():
    return(list(map(int, input().split())))

def instr():
    s = input()
    return(list(s))

def invars():
    return(map(int, input().split()))

# -- TESTING SECTION -- #

base_path = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(base_path, "input.txt")
if os.path.exists(input_path):  
    sys.stdin = open(input_path, "r")

# --- END TEMPLATE --- #

MOD = 998244353

n = inint()
a = inlist()

# Precompute divisors for every index 1..n.
divs = [[] for _ in range(n+1)]
for d in range(1, n+1):
    for j in range(d, n+1, d):
        divs[j].append(d)

groups = defaultdict(list)
for i in range(1, n+1):
    groups[a[i-1]].append(i)

# Process candidate values in descending order.
# For a candidate value v, g(v) = 2^(n - c) - 1, where c is the number of indices
# (from 1 to n) that are divisors of at least one index i with a[i] > v.
# Initially, no index is “forbidden”, so c = 0 and g(max+epsilon) = 2^n - 1.
prev_g = (pow(2, n, MOD) - 1) % MOD
ans = 0

# marked[d] is True if divisor d has been marked (i.e. d divides some index i where a[i] > current candidate).
marked = [False] * (n + 1)
c = 0  # count of marked divisors

for v in sorted(groups.keys(), reverse=True):
    # For every index i with a[i] == v, mark all its divisors (if not already marked).
    for idx in groups[v]:
        for d in divs[idx]:
            if not marked[d]:
                marked[d] = True
                c += 1
    # Now, for the current candidate value v, group1 consists of indices with a value > v.
    # The number of ways to choose black indices that yield a score at most v is:
    new_g = (pow(2, n - c, MOD) - 1) % MOD
    # f(v) = g(v) - g(v') where g(v') corresponds to score < v.
    f_v = (prev_g - new_g) % MOD
    ans = (ans + v * f_v) % MOD
    prev_g = new_g

print(ans)